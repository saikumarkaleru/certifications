"""
data.py -- get a REAL target company and its peers for the comps analysis.

Same robustness pattern as project 1:
  * pull live from yfinance,
  * cache the extracted inputs to input/comps_<TARGET>.json,
  * fall back to the cache, then to a bundled snapshot, so `python main.py`
    ALWAYS runs (even offline).

For each company we extract the handful of fields the multiples need. Enterprise
value is COMPUTED (market cap + total debt - cash) rather than taken blindly,
so the number is explainable.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

try:
    import yfinance as yf
except Exception:  # pragma: no cover
    yf = None

_HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.abspath(os.path.join(_HERE, "..", "..", "input"))

DEFAULT_TARGET = "AAPL"
DEFAULT_PEERS = ["MSFT", "GOOGL", "META", "AMZN", "ORCL", "IBM"]


# ---------------------------------------------------------------------------
# Bundled offline fallback: a real snapshot of Apple + 6 mega-cap tech peers.
# ---------------------------------------------------------------------------
_FALLBACK = {
    "target": "AAPL",
    "as_of": "build-time snapshot",
    "source": "bundled_fallback",
    "companies": {
        "AAPL": {"name": "Apple Inc.", "price": 292.51, "shares": 14687356000,
                 "market_cap": 4296198586368, "total_debt": 84710998016,
                 "cash": 68507000832, "revenue": 451442016256,
                 "ebitda": 159975997440, "net_income": 122575003648,
                 "book_equity": 106630204560, "eps": 8.25, "rev_growth": 0.166,
                 "earn_growth": 0.218, "ebitda_margin": 0.35437,
                 "sector": "Technology"},
        "MSFT": {"name": "Microsoft Corporation", "price": 377.59,
                 "shares": 7428434704, "market_cap": 2805051162624,
                 "total_debt": 125431996416, "cash": 78227996672,
                 "revenue": 318272995328, "ebitda": 184457003008,
                 "net_income": 125215997952, "book_equity": 414335802485,
                 "eps": 16.79, "rev_growth": 0.183, "earn_growth": 0.234,
                 "ebitda_margin": 0.57956, "sector": "Technology"},
        "GOOGL": {"name": "Alphabet Inc.", "price": 359.27,
                  "shares": 5867155790, "market_cap": 4383957581824,
                  "total_debt": 95875997696, "cash": 126839996416,
                  "revenue": 422498009088, "ebitda": 161315995648,
                  "net_income": 160207994880, "book_equity": 231834793886,
                  "eps": 13.12, "rev_growth": 0.218, "earn_growth": 0.82,
                  "ebitda_margin": 0.38181, "sector": "Communication Services"},
        "META": {"name": "Meta Platforms, Inc.", "price": 600.45,
                 "shares": 2196045588, "market_cap": 1524196311040,
                 "total_debt": 86769000448, "cash": 81180000256,
                 "revenue": 214962995200, "ebitda": 109308002304,
                 "net_income": 70586998784, "book_equity": 210848925041,
                 "eps": 27.49, "rev_growth": 0.331, "earn_growth": 0.624,
                 "ebitda_margin": 0.5085, "sector": "Communication Services"},
        "AMZN": {"name": "Amazon.com, Inc.", "price": 238.30,
                 "shares": 10757109436, "market_cap": 2563526885376,
                 "total_debt": 235540004864, "cash": 143088992256,
                 "revenue": 742775980032, "ebitda": 155860992000,
                 "net_income": 90797998080, "book_equity": 442041898054,
                 "eps": 7.53, "rev_growth": 0.166, "earn_growth": 0.748,
                 "ebitda_margin": 0.20984, "sector": "Consumer Cyclical"},
        "ORCL": {"name": "Oracle Corporation", "price": 145.30,
                 "shares": 2880471000, "market_cap": 418532458496,
                 "total_debt": 167431995392, "cash": 31893999616,
                 "revenue": 67356999680, "ebitda": 30493999104,
                 "net_income": 16984000512, "book_equity": 37561341840,
                 "eps": 5.83, "rev_growth": 0.206, "earn_growth": 0.219,
                 "ebitda_margin": 0.45272, "sector": "Technology"},
        "IBM": {"name": "International Business Machines", "price": 282.46,
                "shares": 939885280, "market_cap": 265479995392,
                "total_debt": 69802000384, "cash": 11783000064,
                "revenue": 68910997504, "ebitda": 16611000320,
                "net_income": 10732999680, "book_equity": 32973995278,
                "eps": 11.30, "rev_growth": 0.095, "earn_growth": 0.142,
                "ebitda_margin": 0.24105, "sector": "Technology"},
    },
}


def _extract(ticker):
    """Pull one company's comps fields from yfinance. May raise."""
    t = yf.Ticker(ticker)
    info = t.info or {}
    try:
        price = float(t.fast_info.get("lastPrice"))
    except Exception:
        price = info.get("currentPrice")
    shares = info.get("sharesOutstanding")
    if price is None or shares is None:
        raise ValueError(f"Missing market data for {ticker}")
    bv = info.get("bookValue")
    return {
        "name": info.get("shortName") or info.get("longName") or ticker,
        "price": price,
        "shares": shares,
        "market_cap": info.get("marketCap"),
        "total_debt": info.get("totalDebt"),
        "cash": info.get("totalCash"),
        "revenue": info.get("totalRevenue"),
        "ebitda": info.get("ebitda"),
        "net_income": info.get("netIncomeToCommon"),
        "book_equity": (bv * shares) if (bv and shares) else None,
        "eps": info.get("trailingEps"),
        "rev_growth": info.get("revenueGrowth"),
        "earn_growth": info.get("earningsGrowth"),
        "ebitda_margin": info.get("ebitdaMargins"),
        "sector": info.get("sector"),
    }


def _cache_path(target):
    return os.path.join(INPUT_DIR, f"comps_{target.upper()}.json")


def _write_cache(payload):
    os.makedirs(INPUT_DIR, exist_ok=True)
    with open(_cache_path(payload["target"]), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, default=str)


def _read_cache(target):
    path = _cache_path(target)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return None
    return None


def load_universe(target=DEFAULT_TARGET, peers=None, prefer_live=True):
    """
    Return {"target": TICKER, "companies": {ticker: {...}}, ...} for the target
    plus its peers, using the live->cache->fallback preference order.
    """
    peers = peers or DEFAULT_PEERS
    tickers = [target] + [p for p in peers if p != target]

    if prefer_live and yf is not None:
        try:
            companies = {}
            for tk in tickers:
                companies[tk.upper()] = _extract(tk)
            payload = {
                "target": target.upper(),
                "companies": companies,
                "source": "yfinance_live",
                "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            }
            # sanity: target needs the basics
            tgt = companies[target.upper()]
            if tgt.get("ebitda") and tgt.get("revenue"):
                _write_cache(payload)
                return payload
        except Exception as exc:  # noqa: BLE001
            print(f"  [data] live fetch failed ({exc}); trying cache...")

    cached = _read_cache(target)
    if cached is not None:
        cached["source"] = cached.get("source", "cache") + " (loaded from cache)"
        return cached

    print("  [data] no cache found; using bundled offline fallback (AAPL + peers).")
    return dict(_FALLBACK)
