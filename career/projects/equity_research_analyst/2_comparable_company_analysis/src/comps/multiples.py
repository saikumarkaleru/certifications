"""
multiples.py -- compute trading multiples for every company in the universe.

Relative valuation logic: a company should be worth roughly what similar
companies trade for, per dollar of earnings / EBITDA / revenue / book value.

Multiples computed:
  P/E        = Price / EPS                       (equity multiple)
  EV/EBITDA  = Enterprise Value / EBITDA         (capital-structure neutral)
  EV/Revenue = Enterprise Value / Revenue        (useful when margins vary)
  P/B        = Price / Book value per share      (price vs. accounting equity)
  PEG        = (P/E) / (earnings growth in %)    (P/E adjusted for growth)

Equity multiples (P/E, P/B) use price / market cap -> value to shareholders.
Enterprise multiples (EV/EBITDA, EV/Revenue) use EV -> value to ALL capital
providers, so they pair with pre-interest metrics.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

MULT_COLS = ["P/E", "EV/EBITDA", "EV/Revenue", "P/B", "PEG"]


def enterprise_value(c):
    """EV = market cap + total debt - cash (computed, not taken on faith)."""
    mc = c.get("market_cap")
    if mc is None and c.get("price") and c.get("shares"):
        mc = c["price"] * c["shares"]
    debt = c.get("total_debt") or 0.0
    cash = c.get("cash") or 0.0
    if mc is None:
        return None
    return mc + debt - cash


def _safe_div(a, b):
    """Divide, returning NaN when the denominator is missing/zero/negative."""
    if a is None or b is None or b == 0 or (isinstance(b, float) and b != b):
        return np.nan
    if b < 0:  # a negative denominator makes the multiple meaningless
        return np.nan
    return a / b


def company_multiples(c):
    """Return the five trading multiples for one company dict."""
    price = c.get("price")
    shares = c.get("shares")
    ev = enterprise_value(c)

    eps = c.get("eps")
    if eps is None and c.get("net_income") and shares:
        eps = c["net_income"] / shares
    bvps = None
    if c.get("book_equity") and shares:
        bvps = c["book_equity"] / shares

    pe = _safe_div(price, eps)
    ev_ebitda = _safe_div(ev, c.get("ebitda"))
    ev_rev = _safe_div(ev, c.get("revenue"))
    pb = _safe_div(price, bvps)

    # PEG = P/E divided by the earnings growth rate expressed in %.
    growth_pct = c.get("earn_growth")
    peg = np.nan
    if pe == pe and growth_pct and growth_pct > 0:  # pe not NaN & positive growth
        peg = pe / (growth_pct * 100.0)

    return {
        "P/E": pe, "EV/EBITDA": ev_ebitda, "EV/Revenue": ev_rev,
        "P/B": pb, "PEG": peg, "EV": ev, "EPS": eps, "BVPS": bvps,
    }


def build_multiples_table(universe):
    """
    Return a DataFrame indexed by ticker with the five multiples + fundamentals
    used later (growth, margin) for the screen.
    """
    rows = {}
    for tk, c in universe["companies"].items():
        m = company_multiples(c)
        rows[tk] = {
            "name": c.get("name"),
            "price": c.get("price"),
            "P/E": m["P/E"],
            "EV/EBITDA": m["EV/EBITDA"],
            "EV/Revenue": m["EV/Revenue"],
            "P/B": m["P/B"],
            "PEG": m["PEG"],
            "rev_growth": c.get("rev_growth"),
            "ebitda_margin": c.get("ebitda_margin"),
            "is_target": (tk == universe["target"]),
        }
    df = pd.DataFrame.from_dict(rows, orient="index")
    df.index.name = "ticker"
    return df
