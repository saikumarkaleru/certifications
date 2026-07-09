"""
reforecast.py - a rolling REFORECAST of the remaining months.

Part-way through the year some months are "closed" (actuals are final) and the
rest are still "open". A reforecast replaces the plan for the open months with a
fresh estimate that blends:

  * the ORIGINAL BUDGET for those months, with
  * the TREND we are seeing in the closed (actual) months so far (YTD).

We measure the trend with simple "attainment" ratios computed on the closed
months:

    volume attainment = YTD actual units   / YTD budget units
    price realisation = YTD actual price    / budget price
    cost ratio        = YTD actual unit cost/ budget unit cost
    opex run-rate     = YTD actual opex      / YTD budget opex

Each ratio is BLENDED toward 1.0 by a weight `alpha` (how much we trust the
trend vs the plan). alpha=0.7 means "lean 70% on the trend, 30% on the plan" -
a judgement call a real analyst makes explicitly.

Full-year reforecast = actuals for the closed months + reforecast for the open
months. We then compare that to the original full-year budget.
"""

import numpy as np
import pandas as pd

from .budget import MONTHS


def _blend(ratio, alpha):
    """Pull a raw attainment ratio toward 1.0 (the plan) by weight (1-alpha).

    alpha=1 -> trust the trend fully; alpha=0 -> ignore trend, keep the plan.
    """
    return alpha * ratio + (1 - alpha) * 1.0


def rolling_reforecast(budget, actuals, closed_months=6, alpha=0.7):
    """Return (reforecast_df, meta).

    reforecast_df: per-product Budget FY vs Reforecast FY for revenue, COGS and
    gross profit, plus a TOTAL row.
    meta: dict describing the split point and the blended attainment factors.
    """
    bp = budget["products"]
    ap = actuals["products"]

    closed = list(range(1, closed_months + 1))          # e.g. months 1..6
    open_m = list(range(closed_months + 1, 13))         # e.g. months 7..12

    b_closed = bp[bp["month_num"].isin(closed)]
    a_closed = ap[ap["month_num"].isin(closed)]
    b_open = bp[bp["month_num"].isin(open_m)]

    rows = {}
    factors = {}
    for product in bp["product"].unique():
        bc = b_closed[b_closed["product"] == product]
        ac = a_closed[a_closed["product"] == product]
        bo = b_open[b_open["product"] == product]

        # --- YTD attainment ratios from the closed months ---
        vol_attain = ac["volume"].sum() / bc["volume"].sum()
        # Realised price / budget price (revenue-weighted via totals).
        price_real = (ac["revenue"].sum() / ac["volume"].sum()) / \
                     (bc["revenue"].sum() / bc["volume"].sum())
        cost_ratio = (ac["cogs"].sum() / ac["volume"].sum()) / \
                     (bc["cogs"].sum() / bc["volume"].sum())

        # --- Blend each ratio toward the plan ---
        vb, pb, cb = _blend(vol_attain, alpha), _blend(price_real, alpha), _blend(cost_ratio, alpha)
        factors[product] = {"vol_attain": vol_attain, "price_real": price_real,
                            "cost_ratio": cost_ratio}

        # --- Reforecast the OPEN months at blended factors ---
        rf_units = bo["volume"].to_numpy() * vb
        budget_price = bo["price"].iloc[0]              # list price (constant)
        budget_unit_cost = bo["unit_cost"].iloc[0]
        rf_rev_open = (budget_price * pb * rf_units).sum()
        rf_cogs_open = (budget_unit_cost * cb * rf_units).sum()

        # --- Full-year reforecast = closed actuals + open reforecast ---
        rf_rev = ac["revenue"].sum() + rf_rev_open
        rf_cogs = ac["cogs"].sum() + rf_cogs_open

        # --- Original full-year budget for comparison ---
        b_all = bp[bp["product"] == product]
        bud_rev = b_all["revenue"].sum()
        bud_cogs = b_all["cogs"].sum()

        rows[product] = {
            "Budget Rev": bud_rev, "Reforecast Rev": rf_rev,
            "Rev Delta": rf_rev - bud_rev,
            "Budget GP": bud_rev - bud_cogs,
            "Reforecast GP": rf_rev - rf_cogs,
            "GP Delta": (rf_rev - rf_cogs) - (bud_rev - bud_cogs),
        }

    df = pd.DataFrame(rows).T
    total = df.sum(numeric_only=True)
    total.name = "TOTAL"
    df = pd.concat([df, total.to_frame().T]).round(2)

    meta = {
        "closed_months": [MONTHS[m - 1] for m in closed],
        "open_months":   [MONTHS[m - 1] for m in open_m],
        "alpha": alpha,
        "factors": factors,
    }
    return df, meta
