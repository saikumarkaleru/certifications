"""Data layer: pull real company financials + market data, cache, or fall back.

Public entry point is :func:`load_credit_inputs`. It guarantees that
``python main.py`` runs even with no internet and no cache by shipping a
realistic hard-coded fallback dataset. It reports whether the data is LIVE,
CACHED or FALLBACK so the analysis is honest about its inputs.

yfinance row labels change between versions and companies, so every field is
extracted with a ROBUST helper that scans a list of candidate row names and
returns NaN when nothing matches. That keeps the fetch resilient.
"""

from __future__ import annotations

import math
import os

import numpy as np
import pandas as pd

# --- Universe -------------------------------------------------------------
# Ten liquid US large caps across sectors (tech, banking, energy, healthcare,
# staples, retail, industrials, autos). Original Altman model was fit on
# manufacturers, so a spread of sectors makes the interview discussion richer.
TICKERS = ["AAPL", "MSFT", "JPM", "XOM", "JNJ", "PG", "WMT", "KO", "CAT", "F"]

RISK_FREE_RATE = 0.04       # ~1yr T-bill; used by the Merton model
TRADING_DAYS = 252          # annualisation convention for equity volatility

# Columns cached to input/credit_inputs.csv (all $ figures in USD, raw).
INPUT_COLUMNS = [
    "total_assets", "current_assets", "current_liabilities",
    "retained_earnings", "total_liabilities", "long_term_debt",
    "revenue", "ebit", "market_cap", "equity_vol",
]


# =========================================================================
# Robust extraction helpers
# =========================================================================
def _first_match(frame: pd.DataFrame, candidates: list[str]) -> float:
    """Return the most recent value of the first row whose label matches.

    yfinance financial statements are DataFrames indexed by line-item name
    with one column per reporting period (newest first). Row labels vary, so
    we try several candidate names (case-insensitive, exact then contains).
    Returns NaN if no candidate is found or the value is missing.
    """
    if frame is None or getattr(frame, "empty", True):
        return float("nan")

    index_lower = {str(idx).lower(): idx for idx in frame.index}

    # Pass 1: exact (case-insensitive) label match.
    for name in candidates:
        key = name.lower()
        if key in index_lower:
            value = _latest_value(frame.loc[index_lower[key]])
            if not math.isnan(value):
                return value

    # Pass 2: substring match (handles "Total Non Current Liabilities" etc.).
    for name in candidates:
        key = name.lower()
        for idx_lower, idx in index_lower.items():
            if key in idx_lower:
                value = _latest_value(frame.loc[idx])
                if not math.isnan(value):
                    return value

    return float("nan")


def _latest_value(row: pd.Series) -> float:
    """First non-null value in a statement row (columns are newest-first)."""
    for value in row:
        if pd.notna(value):
            return float(value)
    return float("nan")


def _equity_volatility(prices: pd.Series) -> float:
    """Annualised volatility of daily log returns."""
    prices = prices.dropna()
    if len(prices) < 30:
        return float("nan")
    log_returns = np.log(prices / prices.shift(1)).dropna()
    return float(log_returns.std(ddof=1) * math.sqrt(TRADING_DAYS))


# =========================================================================
# Live download (best effort)
# =========================================================================
def _fetch_one(ticker: str) -> dict | None:
    """Pull one company's inputs from yfinance. Return dict or None on error."""
    try:
        import yfinance as yf

        tk = yf.Ticker(ticker)
        balance = tk.balance_sheet
        income = tk.income_stmt

        total_assets = _first_match(balance, ["Total Assets"])
        current_assets = _first_match(balance, [
            "Current Assets", "Total Current Assets"])
        current_liabilities = _first_match(balance, [
            "Current Liabilities", "Total Current Liabilities"])
        retained_earnings = _first_match(balance, ["Retained Earnings"])
        total_liabilities = _first_match(balance, [
            "Total Liabilities Net Minority Interest",
            "Total Liabilities", "Total Liab"])
        long_term_debt = _first_match(balance, [
            "Long Term Debt", "Long Term Debt And Capital Lease Obligation"])

        revenue = _first_match(income, [
            "Total Revenue", "Operating Revenue", "Sales"])
        ebit = _first_match(income, [
            "EBIT", "Operating Income", "Total Operating Income As Reported"])

        # Market cap: prefer info, else shares * last close.
        market_cap = float("nan")
        try:
            info = tk.info
            market_cap = float(info.get("marketCap") or float("nan"))
        except Exception:
            info = {}
        prices = tk.history(period="2y")["Close"]
        if math.isnan(market_cap):
            shares = info.get("sharesOutstanding")
            if shares and len(prices) > 0:
                market_cap = float(shares) * float(prices.iloc[-1])

        equity_vol = _equity_volatility(prices)

        record = {
            "total_assets": total_assets,
            "current_assets": current_assets,
            "current_liabilities": current_liabilities,
            "retained_earnings": retained_earnings,
            "total_liabilities": total_liabilities,
            "long_term_debt": long_term_debt,
            "revenue": revenue,
            "ebit": ebit,
            "market_cap": market_cap,
            "equity_vol": equity_vol,
        }
        # Require the core fields, otherwise treat as a failed pull.
        core = [total_assets, total_liabilities, market_cap, equity_vol]
        if any(math.isnan(x) for x in core):
            return None
        return record
    except Exception:
        return None


def _download_live() -> pd.DataFrame | None:
    rows = {}
    for ticker in TICKERS:
        rec = _fetch_one(ticker)
        if rec is None:
            return None            # all-or-nothing keeps the table consistent
        rows[ticker] = rec
    frame = pd.DataFrame.from_dict(rows, orient="index")
    frame.index.name = "ticker"
    return frame[INPUT_COLUMNS]


# =========================================================================
# Cache
# =========================================================================
def _cache_path(input_dir: str) -> str:
    return os.path.join(input_dir, "credit_inputs.csv")


def _save_cache(frame: pd.DataFrame, input_dir: str) -> None:
    os.makedirs(input_dir, exist_ok=True)
    frame.to_csv(_cache_path(input_dir))


def _load_cache(input_dir: str) -> pd.DataFrame | None:
    path = _cache_path(input_dir)
    if not os.path.exists(path):
        return None
    try:
        frame = pd.read_csv(path, index_col=0)
        frame.index.name = "ticker"
        if frame.empty:
            return None
        return frame
    except Exception:
        return None


# =========================================================================
# Hard-coded fallback (plausible ~2023 figures, in USD)
# =========================================================================
def _fallback() -> pd.DataFrame:
    """Realistic hard-coded dataset so the app ALWAYS runs offline.

    Figures are rounded, plausible values inspired by recent 10-K filings and
    market caps. They are illustrative, not exact filings, but keep every
    ratio in a believable range for demonstration and testing.
    """
    B = 1_000_000_000.0  # billions -> USD
    data = {
        #             tot_asset cur_ast cur_liab ret_earn tot_liab lt_debt  rev    ebit  mktcap  eq_vol
        "AAPL": [352.0*B, 143.6*B, 145.3*B,  4.3*B, 290.4*B,  95.3*B, 383.3*B, 114.3*B, 2900*B, 0.28],
        "MSFT": [411.9*B, 184.3*B,  95.1*B, 118.8*B, 205.8*B,  47.2*B, 211.9*B,  88.5*B, 2800*B, 0.26],
        "JPM":  [3875*B,  1400*B,  1300*B, 332.9*B, 3583*B, 391.8*B, 239.4*B,  61.6*B,  550*B, 0.30],
        "XOM":  [376.3*B, 96.6*B,  63.0*B, 442.0*B, 163.8*B,  41.2*B, 344.6*B,  55.0*B,  420*B, 0.30],
        "JNJ":  [187.4*B, 55.0*B,  55.2*B, 122.5*B, 109.3*B,  29.3*B,  85.2*B,  22.0*B,  380*B, 0.18],
        "PG":   [120.8*B, 21.9*B,  33.1*B, 100.2*B,  74.8*B,  22.0*B,  82.0*B,  18.1*B,  360*B, 0.17],
        "WMT":  [243.2*B, 76.9*B,  92.4*B,  83.1*B, 161.8*B,  44.3*B, 611.3*B,  25.6*B,  430*B, 0.20],
        "KO":   [97.7*B,  26.7*B,  23.6*B,  71.0*B,  69.2*B,  35.8*B,  45.8*B,  13.0*B,  260*B, 0.17],
        "CAT":  [87.5*B,  44.0*B,  38.1*B,  40.1*B,  70.1*B,  27.1*B,  67.1*B,  12.9*B,  145*B, 0.28],
        "F":    [273.3*B, 116.0*B, 100.0*B, 30.0*B, 228.0*B, 138.0*B, 176.2*B,   6.0*B,   48*B, 0.40],
    }
    frame = pd.DataFrame.from_dict(data, orient="index", columns=INPUT_COLUMNS)
    frame.index.name = "ticker"
    return frame


# =========================================================================
# Public entry point
# =========================================================================
def load_credit_inputs(input_dir: str = "input",
                        use_live: bool = True) -> tuple[pd.DataFrame, str]:
    """Return (inputs DataFrame, source) where source is LIVE/CACHED/FALLBACK.

    Order of preference: live download -> refresh cache; else cache; else the
    built-in fallback dataset. The returned frame is indexed by ticker with the
    columns in INPUT_COLUMNS.
    """
    if use_live:
        live = _download_live()
        if live is not None:
            _save_cache(live, input_dir)
            return live, "LIVE"

    cached = _load_cache(input_dir)
    if cached is not None:
        return cached, "CACHED"

    fallback = _fallback()
    _save_cache(fallback, input_dir)   # seed the cache for reproducibility
    return fallback, "FALLBACK"
