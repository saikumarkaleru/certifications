"""
data.py — get the company's real financials and turn them into model DRIVERS.
============================================================================
What this module does, in plain English:

1. Try to load the three financial statements for a ticker (default MSFT):
      - FIRST from a local cache in input/  (so reruns are instant & offline),
      - else LIVE from yfinance (and we save that pull to the cache),
      - else fall back to bundled ILLUSTRATIVE numbers so main.py ALWAYS runs.
   We print which of the three sources we used.

2. Turn those raw statements into a small set of "drivers" — revenue growth,
   gross margin, opex %, tax rate, capex %, working-capital days, etc. These are
   the assumptions the whole forecast is built on. We derive each driver FROM
   the real data where the number is clean, and clamp it into a sane range so a
   weird one-off figure can't blow up the model.

3. Build a SIMPLIFIED opening balance sheet (cash, receivables, inventory, PP&E
   / payables, debt) and set opening equity as the PLUG so the opening sheet
   balances exactly. (A real balance sheet has dozens of small lines; we model
   the big ones and let equity absorb the rest — that is a normal simplification
   and is easy to defend.)

All money is converted to MILLIONS of dollars for readability.
"""

from __future__ import annotations

import os
import pickle

import pandas as pd

# Folder where we cache the yfinance pull so reruns work with no network.
INPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "input")
os.makedirs(INPUT_DIR, exist_ok=True)

MILLION = 1_000_000.0  # yfinance returns raw dollars; we work in $m.


# ---------------------------------------------------------------------------
# Safe accessor — yfinance DataFrames are messy and some rows simply don't
# exist for some tickers. This never raises; it returns `default` if missing.
# ---------------------------------------------------------------------------
def get(df: pd.DataFrame, row: str, col, default: float = 0.0) -> float:
    """Return df.loc[row, col] as a float, or `default` if anything is missing."""
    try:
        if row not in df.index:
            return default
        val = df.loc[row, col]
        if pd.isna(val):
            return default
        return float(val)
    except Exception:
        return default


def _clamp(x: float, lo: float, hi: float, fallback: float) -> float:
    """Keep a derived driver inside a believable band; if it's junk, use fallback."""
    if x is None or pd.isna(x) or x == 0:
        return fallback
    return max(lo, min(hi, x))


# ---------------------------------------------------------------------------
# BUNDLED ILLUSTRATIVE FALLBACK
# Reasonable, round MSFT-flavoured numbers ($m) used only if BOTH the cache and
# the live pull fail. Guarantees `python main.py` runs anywhere, even offline.
# ---------------------------------------------------------------------------
FALLBACK_DRIVERS = {
    "start_revenue":   245000.0,  # ~$245bn last-year revenue, in $m
    "revenue_growth":  0.12,      # 12% top-line growth
    "gross_margin":    0.69,      # keep 69c of every $1 of revenue
    "opex_pct":        0.30,      # operating expenses (ex-D&A) = 30% of revenue
    "tax_rate":        0.18,      # effective tax rate
    "dep_pct":         0.06,      # depreciation & amortization = 6% of revenue
    "capex_pct":       0.13,      # capex = 13% of revenue (data-centre heavy)
    "dso":             75.0,      # Days Sales Outstanding  -> receivables
    "dio":             20.0,      # Days Inventory Outstanding -> inventory
    "dpo":             80.0,      # Days Payable Outstanding -> payables
    "interest_rate":   0.04,      # interest paid on average debt
    "dividend_payout": 0.25,      # 25% of net income paid as dividends
    "min_cash_pct":    0.05,      # keep cash >= 5% of revenue (rest sweeps debt)
    "forecast_years":  5,
}

FALLBACK_OPENING = {
    "cash":        75000.0,
    "receivables": 50000.0,
    "inventory":    3000.0,
    "ppe":        150000.0,
    "payables":    25000.0,
    "term_debt":   45000.0,
    "revolver":        0.0,
    # equity is the PLUG so the opening sheet balances (set in _finalise_opening)
    "equity":          0.0,
}

FALLBACK_META = {
    "shares_out": 7430.0,   # diluted shares, in millions
    "price":      450.0,    # share price, $ (only used for a sanity cross-check)
    "beta":       0.90,     # equity beta -> feeds CAPM cost of equity in the DCF
}


# ---------------------------------------------------------------------------
# Step 1 — load the three statements (cache -> live -> None)
# ---------------------------------------------------------------------------
def _cache_path(ticker: str) -> str:
    return os.path.join(INPUT_DIR, f"{ticker.upper()}_financials.pkl")


def _load_statements(ticker: str):
    """Return (statements_dict, info_dict, source) or (None, None, 'fallback')."""
    cache = _cache_path(ticker)

    # (a) cache first — offline & instant on every rerun after the first
    if os.path.exists(cache):
        try:
            with open(cache, "rb") as fh:
                blob = pickle.load(fh)
            return blob["statements"], blob["info"], "cache"
        except Exception:
            pass  # corrupt cache -> fall through to live

    # (b) live pull from yfinance, then save to cache
    try:
        import yfinance as yf
        tk = yf.Ticker(ticker)
        statements = {
            "income":   tk.income_stmt,
            "balance":  tk.balance_sheet,
            "cashflow": tk.cashflow,
        }
        # info can be flaky/slow; guard it so a failure here isn't fatal
        try:
            info = dict(tk.info)
        except Exception:
            info = {}
        if statements["income"] is None or statements["income"].empty:
            raise ValueError("yfinance returned empty statements")
        with open(cache, "wb") as fh:
            pickle.dump({"statements": statements, "info": info}, fh)
        return statements, info, "live"
    except Exception:
        # (c) no cache, no network -> caller uses bundled fallback
        return None, None, "fallback"


# ---------------------------------------------------------------------------
# Step 2 — derive drivers from the real statements
# ---------------------------------------------------------------------------
def _derive_drivers(statements: dict) -> dict:
    inc, bal, cf = statements["income"], statements["balance"], statements["cashflow"]
    cols = list(inc.columns)          # period-end dates, most recent first
    c0 = cols[0]                      # latest actual year

    revenue = get(inc, "Total Revenue", c0)
    if revenue <= 0:
        return dict(FALLBACK_DRIVERS)  # statements unusable -> constants

    cogs = get(inc, "Cost Of Revenue", c0)
    gross = get(inc, "Gross Profit", c0, revenue - cogs)
    op_income = get(inc, "Operating Income", c0, get(inc, "EBIT", c0))
    pretax = get(inc, "Pretax Income", c0)
    tax = get(inc, "Tax Provision", c0)
    net_income = get(inc, "Net Income", c0)
    interest = abs(get(inc, "Interest Expense", c0))
    dep = get(inc, "Reconciled Depreciation", c0,
              get(cf, "Depreciation And Amortization", c0))
    capex = abs(get(cf, "Capital Expenditure", c0))
    dividends = abs(get(cf, "Cash Dividends Paid", c0))

    receivables = get(bal, "Receivables", c0)
    inventory = get(bal, "Inventory", c0)
    payables = get(bal, "Accounts Payable", c0)
    total_debt = get(bal, "Total Debt", c0)

    # revenue growth = historical CAGR across the available years (clamped)
    growth = FALLBACK_DRIVERS["revenue_growth"]
    if len(cols) >= 2:
        oldest = get(inc, "Total Revenue", cols[-1])
        n = len(cols) - 1
        if oldest > 0 and n > 0:
            growth = (revenue / oldest) ** (1.0 / n) - 1.0

    gross_margin = gross / revenue
    # opex here EXCLUDES D&A because the model charges depreciation on its own line
    opex_pct = (gross - op_income - dep) / revenue
    tax_rate = (tax / pretax) if pretax > 0 else FALLBACK_DRIVERS["tax_rate"]
    dep_pct = dep / revenue
    capex_pct = capex / revenue
    dso = receivables / revenue * 365.0
    dio = (inventory / cogs * 365.0) if cogs > 0 else FALLBACK_DRIVERS["dio"]
    dpo = (payables / cogs * 365.0) if cogs > 0 else FALLBACK_DRIVERS["dpo"]
    interest_rate = (interest / total_debt) if total_debt > 0 else FALLBACK_DRIVERS["interest_rate"]
    payout = (dividends / net_income) if net_income > 0 else FALLBACK_DRIVERS["dividend_payout"]

    return {
        "start_revenue":   revenue / MILLION,
        "revenue_growth":  _clamp(growth, -0.05, 0.30, FALLBACK_DRIVERS["revenue_growth"]),
        "gross_margin":    _clamp(gross_margin, 0.10, 0.95, FALLBACK_DRIVERS["gross_margin"]),
        "opex_pct":        _clamp(opex_pct, 0.02, 0.70, FALLBACK_DRIVERS["opex_pct"]),
        "tax_rate":        _clamp(tax_rate, 0.05, 0.35, FALLBACK_DRIVERS["tax_rate"]),
        "dep_pct":         _clamp(dep_pct, 0.01, 0.20, FALLBACK_DRIVERS["dep_pct"]),
        "capex_pct":       _clamp(capex_pct, 0.01, 0.25, FALLBACK_DRIVERS["capex_pct"]),
        "dso":             _clamp(dso, 5.0, 180.0, FALLBACK_DRIVERS["dso"]),
        "dio":             _clamp(dio, 1.0, 200.0, FALLBACK_DRIVERS["dio"]),
        "dpo":             _clamp(dpo, 5.0, 200.0, FALLBACK_DRIVERS["dpo"]),
        "interest_rate":   _clamp(interest_rate, 0.02, 0.10, FALLBACK_DRIVERS["interest_rate"]),
        "dividend_payout": _clamp(payout, 0.0, 0.90, FALLBACK_DRIVERS["dividend_payout"]),
        "min_cash_pct":    FALLBACK_DRIVERS["min_cash_pct"],
        "forecast_years":  FALLBACK_DRIVERS["forecast_years"],
    }


def _derive_opening(statements: dict) -> dict:
    bal = statements["balance"]
    c0 = bal.columns[0]
    opening = {
        "cash":        get(bal, "Cash And Cash Equivalents", c0) / MILLION,
        "receivables": get(bal, "Receivables", c0) / MILLION,
        "inventory":   get(bal, "Inventory", c0) / MILLION,
        "ppe":         get(bal, "Net PPE", c0) / MILLION,
        "payables":    get(bal, "Accounts Payable", c0) / MILLION,
        "term_debt":   get(bal, "Total Debt", c0) / MILLION,
        "revolver":    0.0,
        "equity":      0.0,  # set below as the plug
    }
    return _finalise_opening(opening)


def _finalise_opening(opening: dict) -> dict:
    """Set equity so the SIMPLIFIED opening balance sheet ties out to exactly 0."""
    assets = opening["cash"] + opening["receivables"] + opening["inventory"] + opening["ppe"]
    liabilities = opening["payables"] + opening["term_debt"] + opening["revolver"]
    opening["equity"] = assets - liabilities  # the balancing plug
    return opening


def _derive_meta(info: dict, statements: dict) -> dict:
    """Shares, price and beta for the DCF's per-share and WACC steps."""
    bal = statements["balance"]
    c0 = bal.columns[0]
    shares = get(bal, "Ordinary Shares Number", c0) / MILLION
    if shares <= 0:
        shares = (info or {}).get("sharesOutstanding", 0) / MILLION or FALLBACK_META["shares_out"]
    price = (info or {}).get("currentPrice") or (info or {}).get("previousClose") \
        or FALLBACK_META["price"]
    beta = (info or {}).get("beta") or FALLBACK_META["beta"]
    return {"shares_out": float(shares), "price": float(price), "beta": float(beta)}


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------
def load(ticker: str = "MSFT") -> dict:
    """
    Load everything the model needs for one ticker.

    Returns a dict:
        source   : 'cache' | 'live' | 'fallback'
        ticker   : the ticker string
        drivers  : the assumption dict (see FALLBACK_DRIVERS for the keys)
        opening  : the opening balance sheet ($m), already balanced
        meta     : {shares_out ($m), price ($), beta}
    """
    statements, info, source = _load_statements(ticker)

    if source == "fallback":
        return {
            "source": "fallback",
            "ticker": ticker.upper(),
            "drivers": dict(FALLBACK_DRIVERS),
            "opening": _finalise_opening(dict(FALLBACK_OPENING)),
            "meta": dict(FALLBACK_META),
        }

    try:
        drivers = _derive_drivers(statements)
        opening = _derive_opening(statements)
        meta = _derive_meta(info, statements)
        return {"source": source, "ticker": ticker.upper(),
                "drivers": drivers, "opening": opening, "meta": meta}
    except Exception:
        # any parsing surprise -> degrade gracefully to the bundled numbers
        return {
            "source": "fallback",
            "ticker": ticker.upper(),
            "drivers": dict(FALLBACK_DRIVERS),
            "opening": _finalise_opening(dict(FALLBACK_OPENING)),
            "meta": dict(FALLBACK_META),
        }
