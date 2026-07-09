"""Data layer: download real prices, cache them, or fall back to synthetic data.

The public entry point is :func:`load_price_data`. It guarantees that
``python main.py`` runs even with no internet and no cache by generating a
realistic correlated returns dataset as a last resort. The function reports
whether the data is LIVE, CACHED or SYNTHETIC so the analysis is honest about
its inputs.
"""

from __future__ import annotations

import os
from datetime import datetime

import numpy as np
import pandas as pd

# --- Portfolio definition -------------------------------------------------
# Eight liquid, well-known US large caps across sectors. Weights sum to 1.0.
TICKERS = ["AAPL", "MSFT", "JPM", "XOM", "JNJ", "PG", "WMT", "NVDA"]
WEIGHTS = np.array([0.18, 0.18, 0.12, 0.10, 0.10, 0.10, 0.10, 0.12])
PORTFOLIO_NOTIONAL = 1_000_000.0

# Plausible annualised volatilities (used only for the synthetic fallback).
_ANNUAL_VOL = {
    "AAPL": 0.28, "MSFT": 0.26, "JPM": 0.30, "XOM": 0.32,
    "JNJ": 0.18, "PG": 0.17, "WMT": 0.20, "NVDA": 0.45,
}
# Plausible annualised drifts for the synthetic fallback.
_ANNUAL_MU = {
    "AAPL": 0.15, "MSFT": 0.15, "JPM": 0.10, "XOM": 0.08,
    "JNJ": 0.06, "PG": 0.06, "WMT": 0.09, "NVDA": 0.25,
}


def _cache_path(input_dir: str) -> str:
    return os.path.join(input_dir, "prices.csv")


def _download_live(start: str, end: str) -> pd.DataFrame | None:
    """Try a real yfinance download. Return a clean price frame or None."""
    try:
        import yfinance as yf

        raw = yf.download(
            TICKERS, start=start, end=end,
            auto_adjust=True, progress=False, group_by="column",
        )
        if raw is None or len(raw) == 0:
            return None
        # With multiple tickers yfinance returns a column MultiIndex; grab Close.
        if isinstance(raw.columns, pd.MultiIndex):
            prices = raw["Close"].copy()
        else:  # single ticker edge case
            prices = raw[["Close"]].copy()
        prices = prices[[t for t in TICKERS if t in prices.columns]]
        prices = prices.dropna(how="all").ffill().dropna()
        if prices.empty or prices.shape[1] < len(TICKERS):
            return None
        return prices
    except Exception:
        return None


def _synthetic_correlation() -> np.ndarray:
    """A hand-built, plausible correlation matrix for the 8 names."""
    n = len(TICKERS)
    # Base correlation of 0.35 for broad market co-movement.
    corr = np.full((n, n), 0.35)
    np.fill_diagonal(corr, 1.0)
    idx = {t: i for i, t in enumerate(TICKERS)}

    def set_corr(a, b, v):
        corr[idx[a], idx[b]] = corr[idx[b], idx[a]] = v

    # Tech cluster moves together.
    set_corr("AAPL", "MSFT", 0.65)
    set_corr("AAPL", "NVDA", 0.60)
    set_corr("MSFT", "NVDA", 0.62)
    # Defensives move together.
    set_corr("JNJ", "PG", 0.55)
    set_corr("PG", "WMT", 0.45)
    set_corr("JNJ", "WMT", 0.40)
    # Energy is more idiosyncratic / lower correlation to tech.
    set_corr("XOM", "AAPL", 0.20)
    set_corr("XOM", "NVDA", 0.18)
    set_corr("XOM", "JPM", 0.30)
    return corr


def _generate_synthetic(n_days: int = 500, seed: int = 7) -> pd.DataFrame:
    """Simulate correlated daily returns and turn them into a price frame."""
    rng = np.random.default_rng(seed)
    n = len(TICKERS)
    daily_vol = np.array([_ANNUAL_VOL[t] for t in TICKERS]) / np.sqrt(252.0)
    daily_mu = np.array([_ANNUAL_MU[t] for t in TICKERS]) / 252.0

    corr = _synthetic_correlation()
    cov = np.outer(daily_vol, daily_vol) * corr
    chol = np.linalg.cholesky(cov)

    z = rng.standard_normal((n_days, n))
    returns = daily_mu + z @ chol.T

    prices = 100.0 * np.cumprod(1.0 + returns, axis=0)
    dates = pd.bdate_range(end=datetime.today(), periods=n_days)
    return pd.DataFrame(prices, index=dates, columns=TICKERS)


def load_price_data(input_dir: str, years: float = 2.5) -> tuple[pd.DataFrame, str]:
    """Return (prices, source) where source is LIVE, CACHED or SYNTHETIC.

    Order of preference: live download -> cached csv -> synthetic generation.
    A successful live download refreshes the cache.
    """
    os.makedirs(input_dir, exist_ok=True)
    cache = _cache_path(input_dir)

    end = datetime.today()
    start = end - pd.Timedelta(days=int(years * 365))
    prices = _download_live(start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))

    if prices is not None:
        prices.to_csv(cache)
        return prices, "LIVE"

    if os.path.exists(cache):
        try:
            cached = pd.read_csv(cache, index_col=0, parse_dates=True)
            cached = cached[[t for t in TICKERS if t in cached.columns]].dropna()
            if not cached.empty and cached.shape[1] == len(TICKERS):
                return cached, "CACHED"
        except Exception:
            pass

    synthetic = _generate_synthetic()
    synthetic.to_csv(cache)  # cache it so charts/tests are reproducible
    return synthetic, "SYNTHETIC"


def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Simple daily returns (pct change), first NaN row dropped."""
    return prices.pct_change().dropna()


def portfolio_returns(returns: pd.DataFrame, weights: np.ndarray) -> pd.Series:
    """Daily portfolio return series given asset weights."""
    values = returns[TICKERS].to_numpy() @ weights
    return pd.Series(values, index=returns.index, name="portfolio")
