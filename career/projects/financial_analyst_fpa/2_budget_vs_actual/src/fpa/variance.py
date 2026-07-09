"""
variance.py - variances, favorable/unfavorable flags, Price/Volume/Mix
decomposition, and the flex (flexible) budget.

This is the analytical core of the project. Four ideas live here:

1. VARIANCE + SIGN CONVENTION
   Variance = Actual - Budget (dollars). Whether that is "good" depends on the
   line type:
       income lines (revenue, gross profit): Actual > Budget  -> FAVORABLE
       cost   lines (COGS, opex):            Actual < Budget  -> FAVORABLE
   Getting this sign convention right is the classic FP&A trap.

2. PRICE / VOLUME / MIX decomposition of the revenue variance.
   Revenue moves for three reasons: we charged a different PRICE, we sold a
   different total VOLUME, or we sold a different MIX of products. These three
   pieces RECONCILE EXACTLY to the total revenue variance (proved by the unit
   test). This is the centrepiece of the whole project.

3. FLEX BUDGET
   The static budget assumed budget volumes. The flex budget re-states the
   budget at ACTUAL volumes (but still at budget rates). That lets us split any
   variance into:
       Activity/Volume effect = Flex   - Static  (we ran at a different volume)
       Rate/Efficiency effect = Actual - Flex    (our per-unit rates differed)
   The two effects sum back to the total variance by construction.

4. KPIs are assembled here for the CFO summary.
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# 1. FAVORABLE / UNFAVORABLE FLAG
# ---------------------------------------------------------------------------
def flag(kind, dollar_var, tol=1e-6):
    """Classify one dollar variance as Favorable / Unfavorable / On Plan.

    kind        : "income" (revenue-like) or "cost" (expense-like)
    dollar_var  : Actual - Budget in dollars
    """
    if abs(dollar_var) <= tol:
        return "On Plan"
    if kind == "income":
        # Earning MORE than plan is good.
        return "Favorable" if dollar_var > 0 else "Unfavorable"
    elif kind == "cost":
        # Spending LESS than plan is good, so a NEGATIVE variance is favorable.
        return "Favorable" if dollar_var < 0 else "Unfavorable"
    raise ValueError(f"kind must be 'income' or 'cost', got {kind!r}")


# ---------------------------------------------------------------------------
# Helpers to collapse the tidy month-level tables to annual (full-year) totals.
# ---------------------------------------------------------------------------
def _annual_products(products):
    """Full-year totals per product, plus effective (realised) price.

    Effective price = total revenue / total units. For the budget this equals
    the list price; for actuals it is the blended price actually achieved.
    """
    g = products.groupby("product", sort=False).agg(
        volume=("volume", "sum"),
        revenue=("revenue", "sum"),
        cogs=("cogs", "sum"),
    )
    g["eff_price"] = g["revenue"] / g["volume"]       # realised $/unit
    g["eff_unit_cost"] = g["cogs"] / g["volume"]      # realised cost/unit
    return g


# ---------------------------------------------------------------------------
# 2. PRICE / VOLUME / MIX decomposition
# ---------------------------------------------------------------------------
def pvm_decomposition(budget, actuals):
    """Split the full-year revenue variance into Price, Volume and Mix.

    Formulae (per product p, using full-year figures):

      Price[p]  = (actual_price[p] - budget_price[p]) * actual_units[p]
      Mix[p]    = (actual_units[p] - total_actual_units * budget_mix[p])
                  * budget_price[p]
      Volume[p] = (total_actual_units - total_budget_units)
                  * budget_mix[p] * budget_price[p]

    where budget_mix[p] = budget_units[p] / total_budget_units.

    Summed over products, Price + Volume + Mix == total revenue variance,
    EXACTLY (that identity is the unit test). Intuition:
      * Price  = charged a different price on what we actually sold.
      * Volume = sold more/fewer TOTAL units, holding the product mix constant.
      * Mix    = shifted toward richer/cheaper products at the same total units.
    """
    b = _annual_products(budget["products"])
    a = _annual_products(actuals["products"])

    total_bu = b["volume"].sum()          # total budget units (all products)
    total_au = a["volume"].sum()          # total actual units
    budget_mix = b["volume"] / total_bu   # each product's share of budget units

    bp = b["eff_price"]                   # budget price per product
    ap = a["eff_price"]                   # actual (realised) price per product
    au = a["volume"]                      # actual units per product

    price_var  = (ap - bp) * au
    mix_var    = (au - total_au * budget_mix) * bp
    volume_var = (total_au - total_bu) * budget_mix * bp

    out = pd.DataFrame({
        "Budget Rev":  b["revenue"],
        "Actual Rev":  a["revenue"],
        "Price":       price_var,
        "Volume":      volume_var,
        "Mix":         mix_var,
    })
    out["Total Var"] = out["Actual Rev"] - out["Budget Rev"]
    # "Check" should be ~0: the three effects must rebuild the total variance.
    out["Check"] = out["Total Var"] - (out["Price"] + out["Volume"] + out["Mix"])

    # Append a totals row.
    total = out.sum(numeric_only=True)
    total.name = "TOTAL"
    out = pd.concat([out, total.to_frame().T])
    return out.round(2)


# ---------------------------------------------------------------------------
# 3. FLEX BUDGET  (static vs flex vs actual)
# ---------------------------------------------------------------------------
def flex_budget(budget, actuals):
    """Build the flex budget and split variances into activity vs rate effects.

    For each product we compute three revenue and three COGS numbers:
        static = budget rate x BUDGET volume   (the original plan)
        flex   = budget rate x ACTUAL volume   (plan re-flexed to real activity)
        actual = actual rate x ACTUAL volume   (what happened)

    Then:
        Volume/Activity effect = flex   - static  (volume moved, rate fixed)
        Rate/Efficiency effect = actual - flex    (rate moved, volume fixed)
        Total variance         = actual - static  = activity + rate  (identity)

    For revenue the "rate effect" IS the price variance; for COGS it is a
    unit-cost efficiency variance. Opex is fixed (handled separately) so it has
    no activity effect - its whole variance is a spending variance.
    """
    b = _annual_products(budget["products"])
    a = _annual_products(actuals["products"])

    bp, buc = b["eff_price"], b["eff_unit_cost"]    # budget rates
    ap, auc = a["eff_price"], a["eff_unit_cost"]    # actual rates
    bu, au = b["volume"], a["volume"]               # budget vs actual volume

    rows = {}
    for p in b.index:
        # Revenue line
        rev_static = bp[p] * bu[p]
        rev_flex   = bp[p] * au[p]
        rev_actual = ap[p] * au[p]
        # COGS line
        cogs_static = buc[p] * bu[p]
        cogs_flex   = buc[p] * au[p]
        cogs_actual = auc[p] * au[p]
        rows[p] = {
            "Rev Static": rev_static, "Rev Flex": rev_flex, "Rev Actual": rev_actual,
            "Rev Volume Eff": rev_flex - rev_static,   # activity effect
            "Rev Rate Eff":   rev_actual - rev_flex,   # = price variance
            "COGS Static": cogs_static, "COGS Flex": cogs_flex, "COGS Actual": cogs_actual,
            "COGS Volume Eff": cogs_flex - cogs_static,
            "COGS Rate Eff":   cogs_actual - cogs_flex,   # unit-cost efficiency
        }
    out = pd.DataFrame(rows).T
    total = out.sum(numeric_only=True)
    total.name = "TOTAL"
    out = pd.concat([out, total.to_frame().T])
    return out.round(2)


# ---------------------------------------------------------------------------
# Product & opex variance summary tables (used by reporting/commentary)
# ---------------------------------------------------------------------------
def product_variance(budget, actuals):
    """Full-year revenue, COGS and gross-profit variance per product, flagged."""
    b = _annual_products(budget["products"])
    a = _annual_products(actuals["products"])

    df = pd.DataFrame({
        "Budget Rev":  b["revenue"],
        "Actual Rev":  a["revenue"],
        "Budget COGS": b["cogs"],
        "Actual COGS": a["cogs"],
        "Budget Units": b["volume"],
        "Actual Units": a["volume"],
    })
    df["Rev Var"]  = df["Actual Rev"] - df["Budget Rev"]
    df["COGS Var"] = df["Actual COGS"] - df["Budget COGS"]
    df["Budget GP"] = df["Budget Rev"] - df["Budget COGS"]
    df["Actual GP"] = df["Actual Rev"] - df["Actual COGS"]
    df["GP Var"]   = df["Actual GP"] - df["Budget GP"]
    # Flags: revenue is income; COGS is cost; gross profit is income.
    df["Rev Flag"]  = [flag("income", v) for v in df["Rev Var"]]
    df["COGS Flag"] = [flag("cost", v)   for v in df["COGS Var"]]
    df["GP Flag"]   = [flag("income", v) for v in df["GP Var"]]
    return df.round(2)


def opex_variance(budget, actuals):
    """Full-year opex variance per cost centre, flagged (cost convention)."""
    b = budget["opex"].groupby("cost_centre", sort=False)["opex"].sum()
    a = actuals["opex"].groupby("cost_centre", sort=False)["opex"].sum()
    df = pd.DataFrame({"Budget Opex": b, "Actual Opex": a})
    df["Opex Var"] = df["Actual Opex"] - df["Budget Opex"]
    df["Flag"] = [flag("cost", v) for v in df["Opex Var"]]
    return df.round(2)


# ---------------------------------------------------------------------------
# 4. KPI SUMMARY for the CFO
# ---------------------------------------------------------------------------
def kpi_summary(budget, actuals):
    """Return a dict of headline KPIs: revenue, gross margin, opex ratio, and
    the single largest favorable & unfavorable drivers (by operating-profit
    impact)."""
    pv = product_variance(budget, actuals)
    ov = opex_variance(budget, actuals)

    # Company totals (exclude the per-product index; sum the columns).
    b_rev, a_rev = pv["Budget Rev"].sum(), pv["Actual Rev"].sum()
    b_cogs, a_cogs = pv["Budget COGS"].sum(), pv["Actual COGS"].sum()
    b_opex, a_opex = ov["Budget Opex"].sum(), ov["Actual Opex"].sum()

    b_gp, a_gp = b_rev - b_cogs, a_rev - a_cogs                 # gross profit
    b_op, a_op = b_gp - b_opex, a_gp - a_opex                   # operating profit

    # Rank drivers by their impact on OPERATING PROFIT (positive = favorable).
    #   product revenue up   -> +Rev Var
    #   product COGS up      -> -COGS Var (costs hurt profit)
    #   cost-centre opex up  -> -Opex Var
    drivers = {}
    for p in pv.index:
        drivers[f"{p} (revenue)"] = pv.loc[p, "Rev Var"]
        drivers[f"{p} (COGS)"]    = -pv.loc[p, "COGS Var"]
    for c in ov.index:
        drivers[f"{c} (opex)"]    = -ov.loc[c, "Opex Var"]

    best = max(drivers, key=drivers.get)     # largest positive OP impact
    worst = min(drivers, key=drivers.get)    # largest negative OP impact

    return {
        "budget_revenue": b_rev, "actual_revenue": a_rev,
        "revenue_var": a_rev - b_rev,
        "revenue_var_pct": (a_rev - b_rev) / b_rev * 100,
        "budget_gross_margin_pct": b_gp / b_rev * 100,
        "actual_gross_margin_pct": a_gp / a_rev * 100,
        "budget_opex_ratio_pct": b_opex / b_rev * 100,
        "actual_opex_ratio_pct": a_opex / a_rev * 100,
        "budget_operating_profit": b_op, "actual_operating_profit": a_op,
        "operating_profit_var": a_op - b_op,
        "largest_favorable": (best, drivers[best]),
        "largest_unfavorable": (worst, drivers[worst]),
    }
