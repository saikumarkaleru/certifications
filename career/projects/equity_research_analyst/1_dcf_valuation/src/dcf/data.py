"""
data.py -- get a REAL company's financials for the DCF.

Design goals (all interview-defensible):
  * Pull live data from yfinance (income statement, balance sheet, cash-flow
    statement, market data) plus a live risk-free rate from the 10Y Treasury
    (^TNX).
  * Cache the extracted inputs to input/<TICKER>_dcf.json so a re-run is fast
    and reproducible.
  * Degrade gracefully: if the network is down we fall back to the cached file,
    and if there is no cache we fall back to a bundled snapshot -- so
    `python main.py` ALWAYS runs.

We deliberately extract a small, clean dict of the exact numbers the model
needs rather than passing giant DataFrames around. Every field has a clear
meaning that maps to a line on the financial statements.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

# yfinance is optional at import-time: if it is missing or offline we still run.
try:
    import yfinance as yf
except Exception:  # pragma: no cover - environment without yfinance
    yf = None


# ---------------------------------------------------------------------------
# Where cache files live (project_root/input)
# ---------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.abspath(os.path.join(_HERE, "..", "..", "input"))


# ---------------------------------------------------------------------------
# Bundled offline fallback (a real AAPL snapshot).
# This is what lets the project run on a fresh machine with no internet.
# The numbers are genuine yfinance values captured at build time; a live run
# overwrites them in the cache with fresh figures.
# ---------------------------------------------------------------------------
_FALLBACK = {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "price": 289.36,
    "shares": 14_687_356_000,
    "beta": 1.086,
    "risk_free_rate": 0.0449,
    "history": [
        # Most recent fiscal year first. All figures in USD.
        {
            "year": "2025",
            "ebit": 133_050_000_000.0,
            "ebitda": 144_748_000_000.0,
            "pretax_income": 132_729_000_000.0,
            "tax_provision": 20_719_000_000.0,
            "tax_rate": 0.156,
            "dep_amort": 11_698_000_000.0,
            "capex": -12_715_000_000.0,        # yfinance reports capex negative
            "change_in_wc": -25_000_000_000.0,  # cash impact (as reported in CF)
            "operating_cash_flow": 111_482_000_000.0,
            "interest_expense": None,          # AAPL: not broken out -> assume
        },
    ],
    "total_debt": 98_657_000_000.0,
    "cash": 54_697_000_000.0,
    "net_debt": 62_723_000_000.0,
    "source": "bundled_fallback",
    "as_of": "build-time snapshot",
}


# ---------------------------------------------------------------------------
# Small helpers to read a labelled row out of a yfinance statement DataFrame.
# yfinance keeps line items as the index and fiscal years as columns.
# ---------------------------------------------------------------------------
def _row(df, name, col_idx=0):
    """Return the value of a named statement row for a given year column."""
    try:
        if df is not None and name in df.index and df.shape[1] > col_idx:
            val = df.loc[name].iloc[col_idx]
            if val is None:
                return None
            fval = float(val)
            return None if fval != fval else fval  # drop NaN (NaN != NaN)
    except Exception:
        pass
    return None


def _first(df, names, col_idx=0):
    """Return the first row that exists among several possible labels."""
    for n in names:
        v = _row(df, n, col_idx)
        if v is not None:
            return v
    return None


# ---------------------------------------------------------------------------
# Live fetch
# ---------------------------------------------------------------------------
def _fetch_risk_free_rate():
    """10-year US Treasury yield from ^TNX (quoted in %, so divide by 100)."""
    try:
        tnx = yf.Ticker("^TNX")
        y = tnx.fast_info.get("lastPrice")
        if y is not None:
            return float(y) / 100.0
    except Exception:
        pass
    return None


def _fetch_live(ticker):
    """Pull and extract the DCF inputs for one ticker. May raise on failure."""
    t = yf.Ticker(ticker)
    inc, bs, cf = t.income_stmt, t.balance_sheet, t.cashflow
    info = t.info or {}

    # Market data
    try:
        price = float(t.fast_info.get("lastPrice"))
    except Exception:
        price = info.get("currentPrice")
    shares = info.get("sharesOutstanding")
    beta = info.get("beta")

    if price is None or shares is None:
        raise ValueError(f"Missing market data for {ticker}")

    # Build a short per-year history of the FCFF ingredients.
    n_years = min(inc.shape[1] if inc is not None else 0, 4)
    history = []
    for i in range(max(n_years, 1)):
        year = None
        try:
            year = str(inc.columns[i].year)
        except Exception:
            year = str(i)
        ebit = _row(inc, "EBIT", i)
        pretax = _row(inc, "Pretax Income", i)
        tax = _row(inc, "Tax Provision", i)
        tax_rate = _row(inc, "Tax Rate For Calcs", i)
        if tax_rate is None and pretax and tax is not None and pretax != 0:
            tax_rate = tax / pretax
        history.append({
            "year": year,
            "ebit": ebit,
            "ebitda": _first(inc, ["EBITDA", "Normalized EBITDA"], i),
            "pretax_income": pretax,
            "tax_provision": tax,
            "tax_rate": tax_rate,
            "dep_amort": _first(cf, ["Depreciation And Amortization",
                                     "Depreciation Amortization Depletion",
                                     "Reconciled Depreciation"], i),
            "capex": _row(cf, "Capital Expenditure", i),
            "change_in_wc": _row(cf, "Change In Working Capital", i),
            "operating_cash_flow": _first(cf, ["Operating Cash Flow",
                                               "Cash Flow From Continuing "
                                               "Operating Activities"], i),
            "interest_expense": _first(inc, ["Interest Expense",
                                             "Interest Expense Non Operating"], i),
        })

    total_debt = _row(bs, "Total Debt") or info.get("totalDebt")
    cash = _first(bs, ["Cash Cash Equivalents And Short Term Investments",
                       "Cash And Cash Equivalents"]) or info.get("totalCash")
    net_debt = _row(bs, "Net Debt")
    if net_debt is None and total_debt is not None and cash is not None:
        net_debt = total_debt - cash

    return {
        "ticker": ticker.upper(),
        "name": info.get("shortName") or info.get("longName") or ticker.upper(),
        "price": price,
        "shares": shares,
        "beta": beta,
        "risk_free_rate": _fetch_risk_free_rate(),
        "history": history,
        "total_debt": total_debt,
        "cash": cash,
        "net_debt": net_debt,
        "source": "yfinance_live",
        "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------
def _cache_path(ticker):
    return os.path.join(INPUT_DIR, f"{ticker.upper()}_dcf.json")


def _write_cache(data):
    os.makedirs(INPUT_DIR, exist_ok=True)
    with open(_cache_path(data["ticker"]), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, default=str)


def _read_cache(ticker):
    path = _cache_path(ticker)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return None
    return None


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------
def load_company(ticker="AAPL", prefer_live=True):
    """
    Return the clean DCF-input dict for `ticker`.

    Order of preference:
      1. live yfinance pull (then cached for next time),
      2. an existing cache file,
      3. the bundled fallback snapshot.

    So the caller ALWAYS gets usable data and the script never crashes offline.
    """
    if prefer_live and yf is not None:
        try:
            data = _fetch_live(ticker)
            # sanity check: we need at least a usable latest year
            if data["history"] and data["history"][0].get("ebit") is not None:
                _write_cache(data)
                return data
        except Exception as exc:  # noqa: BLE001 - we intentionally swallow
            print(f"  [data] live fetch failed ({exc}); trying cache...")

    cached = _read_cache(ticker)
    if cached is not None:
        cached["source"] = cached.get("source", "cache") + " (loaded from cache)"
        return cached

    print("  [data] no cache found; using bundled offline fallback (AAPL).")
    return dict(_FALLBACK)
