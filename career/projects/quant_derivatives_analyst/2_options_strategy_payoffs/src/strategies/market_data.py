"""
market_data.py -- Source realistic spot + option-chain data, with offline fallback.

GOAL: main.py must ALWAYS run, network or not. So we try, in order:
    1. LIVE   : pull spot + a real option chain from yfinance, then cache it.
    2. CACHE  : if live fails, load the last good snapshot we saved to input/.
    3. SYNTH  : if there is no cache either, build a self-consistent synthetic
                snapshot by pricing a strike ladder with our own BSM model.

The rest of the code only ever sees a MarketSnapshot, so it does not care which
of the three paths produced the data.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone

from . import bsm

# input/ lives two levels up from this file (src/strategies/ -> project root).
_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
INPUT_DIR = os.path.join(_PROJECT_ROOT, "input")


@dataclass
class MarketSnapshot:
    """
    A frozen picture of the market the strategies are built against.

    Fields:
      ticker  : underlying symbol
      spot    : current underlying price
      sigma   : representative implied vol (annualised, e.g. 0.25 = 25%)
      r       : risk-free rate (annualised, continuous)
      q       : dividend yield (annualised, continuous)
      T       : time to expiry in YEARS for the chain we selected
      expiry  : expiry date string
      source  : 'live' | 'cache' | 'synthetic'  (so we can report provenance)
      calls   : {strike: mid_price} from the real chain (may be empty)
      puts    : {strike: mid_price}
      strikes : sorted list of available strikes
    """
    ticker: str
    spot: float
    sigma: float
    r: float
    q: float
    T: float
    expiry: str
    source: str
    calls: dict = field(default_factory=dict)
    puts: dict = field(default_factory=dict)
    strikes: list = field(default_factory=list)

    # --- premium lookup (chain mid if available, else BSM synthetic) -----
    def nearest_strike(self, target: float) -> float:
        """Return the available strike closest to `target`."""
        if not self.strikes:
            return round(target, 2)
        return min(self.strikes, key=lambda k: abs(k - target))

    def call_premium(self, K: float) -> float:
        """Mid price of the call at strike K; fall back to BSM if missing/zero."""
        v = self.calls.get(K) or self.calls.get(self.nearest_strike(K))
        if v and v > 0:
            return float(v)
        return bsm.price_call(self.spot, K, self.T, self.r, self.sigma, self.q)

    def put_premium(self, K: float) -> float:
        """Mid price of the put at strike K; fall back to BSM if missing/zero."""
        v = self.puts.get(K) or self.puts.get(self.nearest_strike(K))
        if v and v > 0:
            return float(v)
        return bsm.price_put(self.spot, K, self.T, self.r, self.sigma, self.q)

    # --- serialisation for caching --------------------------------------
    def to_dict(self) -> dict:
        d = self.__dict__.copy()
        # JSON keys must be strings; store strike dicts with string keys.
        d["calls"] = {str(k): v for k, v in self.calls.items()}
        d["puts"] = {str(k): v for k, v in self.puts.items()}
        return d

    @staticmethod
    def from_dict(d: dict) -> "MarketSnapshot":
        d = dict(d)
        d["calls"] = {float(k): float(v) for k, v in d.get("calls", {}).items()}
        d["puts"] = {float(k): float(v) for k, v in d.get("puts", {}).items()}
        d["strikes"] = [float(x) for x in d.get("strikes", [])]
        return MarketSnapshot(**d)


def _cache_path(ticker: str) -> str:
    return os.path.join(INPUT_DIR, f"{ticker.upper()}_snapshot.json")


def _save_cache(snap: MarketSnapshot) -> None:
    os.makedirs(INPUT_DIR, exist_ok=True)
    with open(_cache_path(snap.ticker), "w", encoding="utf-8") as f:
        json.dump(snap.to_dict(), f, indent=2)


# ---------------------------------------------------------------------------
# 1. LIVE via yfinance
# ---------------------------------------------------------------------------
def _fetch_live(ticker: str, r: float) -> MarketSnapshot:
    """
    Pull spot + one option expiry (~30-60 days out) from yfinance and turn the
    chain into {strike: mid} dicts. Raises on any failure so callers fall back.
    """
    import yfinance as yf  # imported lazily so the module loads with no network

    tk = yf.Ticker(ticker)

    # Spot: use the last close from a short history (robust across yf versions).
    hist = tk.history(period="5d")
    if hist is None or hist.empty:
        raise RuntimeError("no price history returned")
    spot = float(hist["Close"].dropna().iloc[-1])

    # Dividend yield (best-effort; default 0 if unavailable).
    q = 0.0
    try:
        info = tk.info or {}
        dy = info.get("dividendYield")
        if dy:
            q = float(dy) if dy < 1 else float(dy) / 100.0
    except Exception:
        q = 0.0

    # Pick an expiry roughly 30-60 days out for meaningful time value.
    expiries = list(tk.options or [])
    if not expiries:
        raise RuntimeError("no option expiries available")
    today = datetime.now(timezone.utc).date()
    chosen, chosen_T = None, None
    for e in expiries:
        d = datetime.strptime(e, "%Y-%m-%d").date()
        days = (d - today).days
        if days >= 20:
            chosen, chosen_T = e, days / 365.0
            break
    if chosen is None:  # all near-dated; take the last one
        chosen = expiries[-1]
        chosen_T = max((datetime.strptime(chosen, "%Y-%m-%d").date() - today).days, 1) / 365.0

    chain = tk.option_chain(chosen)
    calls, puts = {}, {}

    def mid_row(row):
        bid, ask, last = row.get("bid", 0), row.get("ask", 0), row.get("lastPrice", 0)
        if bid and ask and bid > 0 and ask > 0:
            return (bid + ask) / 2.0
        return last if last and last > 0 else 0.0

    for _, row in chain.calls.iterrows():
        m = mid_row(row)
        if m > 0:
            calls[float(row["strike"])] = float(m)
    for _, row in chain.puts.iterrows():
        m = mid_row(row)
        if m > 0:
            puts[float(row["strike"])] = float(m)

    strikes = sorted(set(calls) | set(puts))
    if not strikes:
        raise RuntimeError("chain had no usable premiums")

    # Estimate a representative implied vol by backing it out of the ATM call
    # via a quick bisection on our own BSM price (keeps us scipy-free).
    sigma = _implied_vol_atm(spot, calls, chosen_T, r, q)

    snap = MarketSnapshot(ticker=ticker.upper(), spot=spot, sigma=sigma, r=r, q=q,
                          T=chosen_T, expiry=chosen, source="live",
                          calls=calls, puts=puts, strikes=strikes)
    return snap


def _implied_vol_atm(spot, calls, T, r, q) -> float:
    """
    Back out an at-the-money implied vol from the observed ATM call price by
    bisection (no scipy). Returns a sane default (0.25) if it cannot converge.
    """
    if not calls or T <= 0:
        return 0.25
    K = min(calls.keys(), key=lambda k: abs(k - spot))
    target = calls[K]
    lo, hi = 0.01, 3.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        price = bsm.price_call(spot, K, T, r, mid, q)
        if price > target:
            hi = mid
        else:
            lo = mid
    iv = 0.5 * (lo + hi)
    return iv if 0.02 < iv < 2.5 else 0.25


# ---------------------------------------------------------------------------
# 3. SYNTHETIC fallback -- self-consistent BSM-priced ladder
# ---------------------------------------------------------------------------
def _build_synthetic(ticker: str, spot: float, sigma: float,
                     r: float, q: float, T: float) -> MarketSnapshot:
    """
    Construct a realistic strike ladder (+/- 30% around spot in ~2.5% steps) and
    price every call/put with our own BSM. Because we price them ourselves the
    snapshot is internally arbitrage-free -- perfect for a demo when offline.
    """
    step = max(1.0, round(spot * 0.025))
    n = 12
    base = round(spot / step) * step
    strikes = sorted({base + i * step for i in range(-n, n + 1) if base + i * step > 0})
    calls = {k: round(bsm.price_call(spot, k, T, r, sigma, q), 2) for k in strikes}
    puts = {k: round(bsm.price_put(spot, k, T, r, sigma, q), 2) for k in strikes}
    return MarketSnapshot(ticker=ticker.upper(), spot=spot, sigma=sigma, r=r, q=q,
                          T=T, expiry="SYNTHETIC(+45d)", source="synthetic",
                          calls=calls, puts=puts, strikes=strikes)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------
def get_snapshot(ticker: str = "AAPL", r: float = 0.045,
                 allow_live: bool = True,
                 synth_spot: float = 200.0, synth_sigma: float = 0.28,
                 synth_q: float = 0.005, synth_T: float = 45 / 365.0) -> MarketSnapshot:
    """
    Return a MarketSnapshot using the live -> cache -> synthetic waterfall.

    Set allow_live=False to skip the network entirely (used by tests / demos).
    """
    if allow_live:
        try:
            snap = _fetch_live(ticker, r)
            _save_cache(snap)          # remember it for future offline runs
            return snap
        except Exception as exc:       # noqa: BLE001 -- any failure => fall back
            print(f"[market_data] live fetch failed ({exc}); trying cache...")

    # 2. Cache
    path = _cache_path(ticker)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                snap = MarketSnapshot.from_dict(json.load(f))
            snap.source = "cache"
            return snap
        except Exception as exc:       # noqa: BLE001
            print(f"[market_data] cache read failed ({exc}); using synthetic.")

    # 3. Synthetic (always succeeds) -- also cache it so re-runs are stable.
    snap = _build_synthetic(ticker, synth_spot, synth_sigma, r, synth_q, synth_T)
    try:
        _save_cache(snap)
    except Exception:                  # noqa: BLE001
        pass
    return snap
