"""
valuation.py -- apply peer multiples to the target for an implied value range.

For each multiple we take the peer MEDIAN and apply it to the target's own
metric to back out an implied share price:

  Equity multiples (P/E, P/B, PEG):
      implied price = multiple x target per-share metric
  Enterprise multiples (EV/EBITDA, EV/Revenue):
      implied EV = multiple x target metric
      implied equity = implied EV - net debt
      implied price = implied equity / shares

The set of implied prices forms a "football field": a low/median/high range we
compare to the current market price. The median of the methods is the headline.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _target_metrics(universe):
    """Pull the target's own metrics needed to apply the multiples."""
    c = universe["companies"][universe["target"]]
    shares = c["shares"]
    eps = c.get("eps")
    if eps is None and c.get("net_income") and shares:
        eps = c["net_income"] / shares
    bvps = c["book_equity"] / shares if c.get("book_equity") and shares else None
    net_debt = (c.get("total_debt") or 0.0) - (c.get("cash") or 0.0)
    return {
        "shares": shares,
        "eps": eps,
        "bvps": bvps,
        "ebitda": c.get("ebitda"),
        "revenue": c.get("revenue"),
        "net_debt": net_debt,
        "price": c.get("price"),
        "earn_growth": c.get("earn_growth"),
    }


def implied_valuation(universe, peer_stats):
    """
    Build the per-method implied-price table using the peer MEDIAN multiple.
    Returns (implied_df, football_dict).
    """
    tm = _target_metrics(universe)
    med = peer_stats["Median"]
    rows = []

    # P/E -> price = median P/E * EPS
    if tm["eps"] and tm["eps"] > 0 and med.get("P/E") == med.get("P/E"):
        rows.append(("P/E", med["P/E"], med["P/E"] * tm["eps"]))

    # EV/EBITDA -> EV -> equity -> price
    if tm["ebitda"] and med.get("EV/EBITDA") == med.get("EV/EBITDA"):
        ev = med["EV/EBITDA"] * tm["ebitda"]
        rows.append(("EV/EBITDA", med["EV/EBITDA"],
                     (ev - tm["net_debt"]) / tm["shares"]))

    # EV/Revenue -> EV -> equity -> price
    if tm["revenue"] and med.get("EV/Revenue") == med.get("EV/Revenue"):
        ev = med["EV/Revenue"] * tm["revenue"]
        rows.append(("EV/Revenue", med["EV/Revenue"],
                     (ev - tm["net_debt"]) / tm["shares"]))

    # P/B -> price = median P/B * BVPS
    if tm["bvps"] and tm["bvps"] > 0 and med.get("P/B") == med.get("P/B"):
        rows.append(("P/B", med["P/B"], med["P/B"] * tm["bvps"]))

    # PEG -> implied P/E = median PEG * target growth(%); price = implied P/E * EPS
    if (tm["eps"] and tm["eps"] > 0 and tm.get("earn_growth")
            and tm["earn_growth"] > 0 and med.get("PEG") == med.get("PEG")):
        implied_pe = med["PEG"] * (tm["earn_growth"] * 100.0)
        rows.append(("PEG", med["PEG"], implied_pe * tm["eps"]))

    implied_df = pd.DataFrame(rows, columns=["Method", "Peer Median Multiple",
                                             "Implied Price/Share"])

    prices = implied_df["Implied Price/Share"]
    football = {
        "low": float(prices.min()),
        "median": float(prices.median()),
        "high": float(prices.max()),
        "current_price": tm["price"],
        "upside_to_median": float(prices.median()) / tm["price"] - 1,
        "verdict": ("UNDERVALUED" if prices.median() > tm["price"]
                    else "OVERVALUED"),
    }
    return implied_df, football
