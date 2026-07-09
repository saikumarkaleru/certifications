"""
data.py -- get the raw financial statements we need, robustly
=============================================================

The job of this module is simple to say and fiddly to do well:

    "Give me a clean table of financial-statement line items for a company,
     for the last few years, and never crash."

How it works (three layers, tried in order):

  1. CACHE   -- if we already saved this ticker to input/<TICKER>.pkl, read it.
                Reruns are then fully offline and fast, and we never hammer
                Yahoo's servers twice for the same data.
  2. LIVE    -- otherwise pull it live from yfinance and immediately cache it.
  3. FALLBACK-- if there is no cache AND no network, fall back to bundled,
                clearly-illustrative numbers so `python main.py` ALWAYS runs.

Every company ends up as a tidy "facts" DataFrame:
    index   = canonical line-item names WE choose (Revenue, Net Income, ...)
    columns = fiscal years as integers, sorted oldest -> newest
This canonical table is what every other module consumes, so the messy job of
matching Yahoo's exact row spellings lives here and nowhere else.
"""

from __future__ import annotations

import os
import pickle
import pandas as pd

# Where we cache pulls. input/ sits next to main.py (two levels up from here).
_PKG_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.abspath(os.path.join(_PKG_DIR, "..", ".."))
INPUT_DIR = os.path.join(_PROJECT_DIR, "input")
os.makedirs(INPUT_DIR, exist_ok=True)

# The companies we analyse. Target first, then a clean large-cap peer set.
TARGET = "AAPL"
PEERS = ["MSFT", "GOOGL", "AMZN", "META"]
ALL_TICKERS = [TARGET] + PEERS

# How many fiscal years to keep. yfinance typically gives ~4 annual columns.
N_YEARS = 4

# ---------------------------------------------------------------------------
# Canonical line items -> the exact row label yfinance uses on each statement.
# We deliberately keep OUR names stable so the rest of the code never has to
# know how Yahoo spells things this week.
# ---------------------------------------------------------------------------
INCOME_MAP = {
    "Revenue": "Total Revenue",
    "COGS": "Cost Of Revenue",
    "Gross Profit": "Gross Profit",
    "Operating Income": "Operating Income",
    "EBIT": "EBIT",
    "Pretax Income": "Pretax Income",
    "Tax Provision": "Tax Provision",
    "Net Income": "Net Income",
    "Interest Expense": "Interest Expense",
}
BALANCE_MAP = {
    "Total Assets": "Total Assets",
    "Current Assets": "Current Assets",
    "Current Liabilities": "Current Liabilities",
    "Total Liabilities": "Total Liabilities Net Minority Interest",
    "Equity": "Stockholders Equity",
    "Cash": "Cash And Cash Equivalents",
    "Receivables": "Receivables",
    "Inventory": "Inventory",
    "Net PPE": "Net PPE",
    "Payables": "Accounts Payable",
    "Total Debt": "Total Debt",
    "Invested Capital": "Invested Capital",
}
CASHFLOW_MAP = {
    "Operating Cash Flow": "Operating Cash Flow",
    "Capital Expenditure": "Capital Expenditure",
    "Free Cash Flow": "Free Cash Flow",
    # Depreciation & amortisation lets us build EBITDA. Yahoo's label varies,
    # so we try the common one and fall back to 0 if it is missing.
    "D&A": "Depreciation And Amortization",
}


# ---------------------------------------------------------------------------
# The one safe accessor everything uses.
# ---------------------------------------------------------------------------
def get(df, row, col, default=float("nan")):
    """Safely read df.loc[row, col].

    Peers differ: Google and Meta carry ~no inventory, some rows are simply
    absent. Rather than sprinkle try/except everywhere, we funnel every lookup
    through here and return `default` (NaN by default) when the row/column is
    missing or the value is blank. NaN then propagates naturally through the
    ratio math, which is exactly what we want.
    """
    if df is None or row not in df.index or col not in df.columns:
        return default
    val = df.loc[row, col]
    if isinstance(val, pd.Series):      # duplicate row label -> take the first
        val = val.iloc[0]
    return default if pd.isna(val) else float(val)


def _normalise_columns(df):
    """Turn a raw yfinance statement into columns keyed by fiscal YEAR (int),
    sorted oldest->newest, keeping the most recent N_YEARS.

    yfinance gives period-end Timestamps as columns, most recent first. We only
    care about the year, so we relabel columns to their year, drop duplicates,
    and sort. This makes the three statements line up on a common year key.
    """
    if df is None or df.empty:
        return None
    out = df.copy()
    out.columns = [c.year if hasattr(c, "year") else c for c in out.columns]
    out = out.loc[:, ~pd.Index(out.columns).duplicated()]   # first wins
    years = sorted(out.columns)[-N_YEARS:]                   # keep last N years
    return out[years]


def _build_facts(raw):
    """Assemble the canonical facts table from the three raw statements.

    `raw` is a dict with keys 'income', 'balance', 'cashflow' (each a DataFrame
    or None). We normalise each to year columns, take the union of years present
    on the income statement, and pull every canonical field with get().
    """
    inc = _normalise_columns(raw.get("income"))
    bal = _normalise_columns(raw.get("balance"))
    cfs = _normalise_columns(raw.get("cashflow"))

    # Years driven by the income statement (revenue must exist to be useful).
    years = list(inc.columns) if inc is not None else []
    facts = {}
    for year in years:
        col = {}
        for name, src in INCOME_MAP.items():
            col[name] = get(inc, src, year)
        for name, src in BALANCE_MAP.items():
            col[name] = get(bal, src, year)
        for name, src in CASHFLOW_MAP.items():
            col[name] = get(cfs, src, year)

        # --- gentle derived fallbacks so a missing headline row is survivable ---
        # EBIT missing? Operating Income is the standard stand-in.
        if pd.isna(col["EBIT"]):
            col["EBIT"] = col["Operating Income"]
        # Gross Profit missing? Revenue - COGS.
        if pd.isna(col["Gross Profit"]) and not pd.isna(col["COGS"]):
            col["Gross Profit"] = col["Revenue"] - col["COGS"]
        # D&A missing? Treat as 0 (EBITDA then collapses toward EBIT).
        if pd.isna(col["D&A"]):
            col["D&A"] = 0.0
        facts[year] = col

    df = pd.DataFrame(facts)            # index = field, columns = years
    return df.reindex(sorted(df.columns), axis=1)   # oldest -> newest


# ---------------------------------------------------------------------------
# Layer 1 + 2: cache-then-live for a single ticker.
# ---------------------------------------------------------------------------
def _cache_path(ticker):
    return os.path.join(INPUT_DIR, f"{ticker}.pkl")


def _load_raw_cached_or_live(ticker):
    """Return (raw_dict, source_label) for one ticker.

    source_label is 'cache' or 'live'. Raises on failure so the caller can
    decide whether to fall back to bundled data.
    """
    path = _cache_path(ticker)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            return pickle.load(fh), "cache"

    # Not cached -> pull live. Import here so the offline fallback path does
    # not even require yfinance to be installed.
    import yfinance as yf

    tk = yf.Ticker(ticker)
    raw = {
        "income": tk.income_stmt,
        "balance": tk.balance_sheet,
        "cashflow": tk.cashflow,
    }
    # A valid pull must have a non-empty income statement.
    if raw["income"] is None or raw["income"].empty:
        raise RuntimeError(f"empty income statement for {ticker}")

    with open(path, "wb") as fh:        # cache immediately -> reruns go offline
        pickle.dump(raw, fh)
    return raw, "live"


# ---------------------------------------------------------------------------
# Layer 3: bundled illustrative data (only used if cache AND network fail).
# Numbers are rounded, plausible large-cap figures in $ millions. They are
# CLEARLY illustrative -- flat, smooth trends -- not the real filings.
# GOOGL and META carry ~zero inventory on purpose, to exercise the code's
# divide-by-zero / NaN handling for inventory-based ratios.
# ---------------------------------------------------------------------------
_YEARS_FALLBACK = [2021, 2022, 2023, 2024]


def _fallback_company(rev, gp, opinc, ni, ta, eq, ca, cl, cash, recv,
                      inv, ppe, ap, debt, ic, pretax, tax, intexp, ocf,
                      capex, da):
    """Helper: build one company's facts from four-year lists (oldest->newest)."""
    fields = {
        "Revenue": rev, "COGS": [r - g for r, g in zip(rev, gp)],
        "Gross Profit": gp, "Operating Income": opinc, "EBIT": opinc,
        "Pretax Income": pretax, "Tax Provision": tax, "Net Income": ni,
        "Interest Expense": intexp, "Total Assets": ta, "Current Assets": ca,
        "Current Liabilities": cl, "Total Liabilities": [a - e for a, e in zip(ta, eq)],
        "Equity": eq, "Cash": cash, "Receivables": recv, "Inventory": inv,
        "Net PPE": ppe, "Payables": ap, "Total Debt": debt, "Invested Capital": ic,
        "Operating Cash Flow": ocf, "Capital Expenditure": capex,
        "Free Cash Flow": [o - c for o, c in zip(ocf, capex)], "D&A": da,
    }
    return pd.DataFrame(fields, index=_YEARS_FALLBACK).T


def _fallback_facts():
    """Return {ticker: facts DataFrame} for all five companies."""
    F = {}
    # AAPL (target): fat margins, high leverage (buybacks), real inventory.
    F["AAPL"] = _fallback_company(
        rev=[366, 394, 383, 391], gp=[152, 171, 169, 181],
        opinc=[109, 119, 114, 123], ni=[95, 100, 97, 94],
        ta=[351, 353, 353, 365], eq=[63, 51, 62, 57],
        ca=[135, 135, 143, 153], cl=[125, 154, 145, 176],
        cash=[35, 24, 30, 30], recv=[51, 61, 60, 66], inv=[6, 5, 6, 7],
        ppe=[39, 42, 43, 45], ap=[54, 64, 62, 68], debt=[124, 120, 111, 106],
        ic=[170, 170, 173, 163], pretax=[109, 119, 114, 124],
        tax=[14, 19, 17, 30], intexp=[3, 3, 4, 4],
        ocf=[104, 122, 111, 118], capex=[11, 11, 11, 10], da=[11, 11, 11, 11])
    # MSFT: high margin, strong balance sheet, low leverage.
    F["MSFT"] = _fallback_company(
        rev=[168, 198, 212, 245], gp=[115, 135, 146, 171],
        opinc=[70, 83, 89, 109], ni=[61, 73, 72, 88],
        ta=[334, 365, 412, 512], eq=[142, 166, 206, 268],
        ca=[184, 169, 184, 159], cl=[88, 95, 104, 125],
        cash=[130, 105, 111, 75], recv=[38, 44, 48, 56], inv=[2, 3, 3, 1],
        ppe=[70, 87, 96, 135], ap=[15, 19, 18, 21], debt=[67, 61, 59, 97],
        ic=[209, 227, 265, 365], pretax=[71, 83, 89, 108],
        tax=[10, 11, 17, 20], intexp=[2, 2, 2, 3],
        ocf=[76, 89, 87, 118], capex=[24, 28, 32, 55], da=[11, 14, 14, 22])
    # GOOGL: high margin, near-zero inventory (tests NaN handling), low debt.
    F["GOOGL"] = _fallback_company(
        rev=[257, 282, 307, 350], gp=[146, 156, 174, 203],
        opinc=[78, 74, 84, 112], ni=[76, 60, 74, 100],
        ta=[359, 365, 402, 450], eq=[251, 256, 283, 325],
        ca=[188, 164, 171, 163], cl=[64, 69, 81, 89],
        cash=[21, 21, 24, 23], recv=[39, 40, 47, 53], inv=[0, 0, 0, 0],
        ppe=[97, 113, 134, 171], ap=[6, 6, 8, 8], debt=[28, 29, 28, 26],
        ic=[279, 285, 311, 351], pretax=[90, 71, 86, 120],
        tax=[14, 11, 12, 20], intexp=[1, 1, 1, 1],
        ocf=[91, 91, 102, 125], capex=[24, 31, 32, 52], da=[13, 15, 15, 15])
    # AMZN: thin margins, big asset base, real inventory, heavy capex.
    F["AMZN"] = _fallback_company(
        rev=[470, 514, 575, 638], gp=[197, 226, 270, 311],
        opinc=[25, 12, 37, 68], ni=[33, -3, 30, 59],
        ta=[420, 462, 528, 625], eq=[138, 146, 201, 286],
        ca=[161, 146, 172, 191], cl=[142, 155, 164, 179],
        cash=[36, 54, 73, 78], recv=[32, 43, 53, 59], inv=[32, 34, 34, 35],
        ppe=[161, 187, 205, 253], ap=[78, 79, 85, 95], debt=[116, 140, 135, 130],
        ic=[254, 286, 336, 416], pretax=[38, -6, 37, 68],
        tax=[4, -3, 7, 9], intexp=[2, 2, 3, 3],
        ocf=[46, 47, 85, 116], capex=[55, 59, 53, 78], da=[34, 41, 49, 52])
    # META: high margin, near-zero inventory, low debt, heavy capex.
    F["META"] = _fallback_company(
        rev=[118, 116, 135, 165], gp=[93, 90, 108, 135],
        opinc=[47, 29, 47, 69], ni=[39, 23, 39, 62],
        ta=[166, 186, 230, 276], eq=[124, 126, 154, 183],
        ca=[66, 61, 85, 100], cl=[21, 27, 31, 37],
        cash=[16, 15, 42, 44], recv=[14, 13, 16, 17], inv=[0, 0, 0, 0],
        ppe=[57, 79, 96, 115], ap=[5, 4, 5, 6], debt=[14, 26, 37, 49],
        ic=[138, 152, 191, 232], pretax=[47, 29, 47, 78],
        tax=[8, 6, 8, 16], intexp=[0, 1, 1, 1],
        ocf=[57, 51, 71, 91], capex=[19, 32, 28, 37], da=[8, 9, 11, 15])
    return F


# ---------------------------------------------------------------------------
# Public entry point.
# ---------------------------------------------------------------------------
def load_all(tickers=None):
    """Load canonical facts for every ticker.

    Returns (facts_by_ticker, source) where:
      facts_by_ticker : {ticker: facts DataFrame (field x year)}
      source          : 'live', 'cache', 'mixed', or 'fallback'

    Strategy: try cache-or-live per ticker (sequentially, gentle on Yahoo). If
    ANY ticker fails and we cannot assemble the full set, we drop to bundled
    illustrative data so the program always completes.
    """
    tickers = tickers or ALL_TICKERS
    facts, sources = {}, set()
    try:
        for tk in tickers:
            raw, src = _load_raw_cached_or_live(tk)
            built = _build_facts(raw)
            if built.empty:
                raise RuntimeError(f"could not build facts for {tk}")
            facts[tk] = built
            sources.add(src)
    except Exception as exc:            # network down + nothing cached, etc.
        print(f"[data] live/cache load failed ({exc}); using bundled fallback data.")
        return _fallback_facts(), "fallback"

    source = sources.pop() if len(sources) == 1 else "mixed"
    return facts, source
