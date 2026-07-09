"""
market_data.py  --  fetch a real option chain, with a bullet-proof offline path
================================================================================

WHAT THIS DOES:
  Pull a live option chain (calls) for a ticker + expiry from Yahoo Finance via
  yfinance, and cache it to input/ so we never depend on the network twice.

THE FALLBACK LADDER (so main.py ALWAYS runs, even on a plane):
  1. Try the live yfinance fetch. On success, cache to input/<ticker>_<exp>.csv.
  2. If the network fails, load the most recent cached CSV from input/.
  3. If there is NO cache either, synthesize a realistic chain (a gentle vol
     smile around spot) so the demo still produces a smile and pricing stats.

Every returned chain is a tidy pandas DataFrame with the same columns regardless
of source: [strike, mid, bid, ask, spot, T, r, q, source].
"""

import os
import math
import datetime as dt
import pandas as pd

# input/ lives next to the project root (two levels up from this file's src/pricer).
_HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(_HERE, "..", "..", "input")
INPUT_DIR = os.path.abspath(INPUT_DIR)
os.makedirs(INPUT_DIR, exist_ok=True)

# Assumptions used to turn a raw chain into pricer inputs. A real desk would pull
# the OIS curve and a dividend forecast; for a demo these constants are honest and
# fully explainable.
DEFAULT_R = 0.05     # ~risk-free rate (annual)
DEFAULT_Q = 0.0      # dividend yield assumption


def _year_fraction(expiry_str):
    """Convert an 'YYYY-MM-DD' expiry into T = years from today (ACT/365)."""
    expiry = dt.datetime.strptime(expiry_str, "%Y-%m-%d").date()
    days = (expiry - dt.date.today()).days
    return max(days, 1) / 365.0     # floor at 1 day so T is always positive


def _synthetic_chain(ticker="SYNTH", spot=100.0, T=0.25):
    """Build a believable option chain with a mild volatility smile.

    Used only when there is neither network nor cache. The smile is quadratic in
    log-moneyness so the demo's IV-vs-strike plot still looks like a real smile.
    """
    from .black_scholes import bs_price
    strikes = [round(spot * m, 2) for m in
               (0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20)]
    rows = []
    for K in strikes:
        moneyness = math.log(K / spot)
        # Base 22% vol, curving up in the wings -> classic smile.
        iv = 0.22 + 0.35 * moneyness * moneyness
        mid = bs_price(spot, K, T, DEFAULT_R, iv, "call", DEFAULT_Q)
        spread = max(0.02 * mid, 0.01)      # a small synthetic bid/ask spread
        rows.append({
            "strike": K,
            "mid": round(mid, 4),
            "bid": round(mid - spread, 4),
            "ask": round(mid + spread, 4),
            "spot": spot,
            "T": T,
            "r": DEFAULT_R,
            "q": DEFAULT_Q,
            "source": "synthetic",
        })
    return pd.DataFrame(rows)


def _cache_path(ticker, expiry):
    return os.path.join(INPUT_DIR, f"{ticker.upper()}_{expiry}.csv")


def get_option_chain(ticker="AAPL", expiry=None, force_offline=False):
    """Return a tidy call-option chain DataFrame, trying live -> cache -> synthetic.

    ticker        : underlying symbol.
    expiry        : 'YYYY-MM-DD'; if None, the nearest listed expiry is used.
    force_offline : skip the network entirely (handy for tests / demos).
    """
    # ---- 1. Try live yfinance unless told to stay offline ----------------
    if not force_offline:
        try:
            import yfinance as yf
            tk = yf.Ticker(ticker)
            expirations = tk.options
            if not expirations:
                raise RuntimeError("no expirations returned")
            if expiry is None or expiry not in expirations:
                expiry = expirations[0]      # nearest expiry

            chain = tk.option_chain(expiry)
            calls = chain.calls.copy()

            # Current spot from recent history (robust to market hours).
            hist = tk.history(period="1d")
            spot = float(hist["Close"].iloc[-1])
            T = _year_fraction(expiry)

            calls = calls[["strike", "bid", "ask", "lastPrice"]].copy()
            # Mid price when both quotes exist, else fall back to last traded.
            calls["mid"] = calls.apply(
                lambda x: (x["bid"] + x["ask"]) / 2.0
                if x["bid"] > 0 and x["ask"] > 0 else x["lastPrice"], axis=1)
            calls = calls[calls["mid"] > 0]
            # Keep strikes reasonably near the money -> cleaner smile, valid IVs.
            calls = calls[(calls["strike"] > 0.7 * spot) &
                          (calls["strike"] < 1.3 * spot)]

            df = pd.DataFrame({
                "strike": calls["strike"].values,
                "mid": calls["mid"].values,
                "bid": calls["bid"].values,
                "ask": calls["ask"].values,
                "spot": spot,
                "T": T,
                "r": DEFAULT_R,
                "q": DEFAULT_Q,
                "source": f"yfinance:{ticker}:{expiry}",
            }).reset_index(drop=True)

            if len(df) >= 3:
                df.to_csv(_cache_path(ticker, expiry), index=False)   # cache it
                return df
            raise RuntimeError("live chain too small after cleaning")
        except Exception as e:
            print(f"  [market_data] live fetch failed ({e}); trying cache...")

    # ---- 2. Fall back to the most recent cached CSV ----------------------
    cached = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]
    if cached:
        cached.sort(key=lambda f: os.path.getmtime(os.path.join(INPUT_DIR, f)),
                    reverse=True)
        path = os.path.join(INPUT_DIR, cached[0])
        print(f"  [market_data] using cached chain: {cached[0]}")
        return pd.read_csv(path)

    # ---- 3. Last resort: bundled synthetic chain ------------------------
    print("  [market_data] no cache found; using synthetic chain.")
    return _synthetic_chain()
