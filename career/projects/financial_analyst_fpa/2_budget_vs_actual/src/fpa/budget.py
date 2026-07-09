"""
budget.py - build the DRIVER-BASED annual budget.

"Driver-based" means we do NOT hard-code revenue. We hold the underlying
business drivers - how many units we plan to sell (volume), at what price, and
at what unit cost - and let revenue and COGS fall out of arithmetic:

    revenue = price      x volume
    COGS    = unit_cost  x volume

Holding the drivers separately is what later lets us split a revenue miss into
a PRICE effect and a VOLUME effect (see variance.py). If you hard-code revenue
you can never decompose it - so a good FP&A model always keeps the drivers.

On top of the product P&L we add four COST CENTRES (Manufacturing overhead,
Sales & Marketing, G&A, R&D). These carry fixed operating-expense budgets that
are spread across the year with a monthly seasonality curve.
"""

import numpy as np
import pandas as pd

# The 12 month labels, in order. Kept here so every module speaks the same
# calendar. "month_num" (1..12) is the sortable integer version.
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ---------------------------------------------------------------------------
# PRODUCT DRIVERS - the heart of the budget.
#   annual_volume : units we plan to sell across the whole year
#   price         : planned selling price per unit ($)
#   unit_cost     : planned variable cost per unit ($)  -> drives COGS
# Contribution per unit = price - unit_cost, so each line earns its keep
# differently (Delta is low-volume/high-margin; Gamma is high-volume/thin).
# ---------------------------------------------------------------------------
PRODUCT_SPECS = {
    "Alpha Sensor":    {"annual_volume": 24_000, "price": 120, "unit_cost": 70},
    "Beta Controller": {"annual_volume": 12_000, "price": 260, "unit_cost": 150},
    "Gamma Module":    {"annual_volume": 36_000, "price": 80,  "unit_cost": 55},
    "Delta Analyzer":  {"annual_volume": 6_000,  "price": 540, "unit_cost": 300},
}

# ---------------------------------------------------------------------------
# SEASONALITY - relative weight of each month. These are RELATIVE numbers;
# the code normalises them to sum to 1.0, then splits each product's annual
# volume across the months by these weights. The curve dips in summer
# (Jul/Aug) and peaks at year end (Dec) - a common industrial pattern.
# ---------------------------------------------------------------------------
SEASONALITY = np.array(
    [0.7, 0.7, 0.9, 1.0, 1.1, 1.0, 0.8, 0.8, 1.1, 1.2, 1.0, 1.3]
)

# ---------------------------------------------------------------------------
# COST CENTRES - annual operating-expense budgets (fixed-ish overheads).
# These are spread across the year with the same seasonality curve. In the
# flex-budget logic (variance.py) opex is treated as FIXED: it does not flex
# with sales volume, so its whole variance is a "spending" variance.
# ---------------------------------------------------------------------------
COST_CENTRE_SPECS = {
    "Manufacturing":     1_200_000,   # factory overhead (not per-unit COGS)
    "Sales & Marketing": 2_400_000,   # demand generation, sales team
    "G&A":               1_500_000,   # finance, HR, admin, rent
    "R&D":               1_800_000,   # engineering / new products
}


def _monthly_weights():
    """Return the seasonality curve normalised so the 12 weights sum to 1.0."""
    return SEASONALITY / SEASONALITY.sum()


def build_products():
    """Build the product-level budget in TIDY (long) form.

    One row per product x month, with the drivers and the derived revenue and
    COGS. Volumes are rounded to whole units (you cannot sell half a sensor).

    Columns: product, month, month_num, volume, price, unit_cost, revenue, cogs
    """
    weights = _monthly_weights()
    rows = []
    for product, spec in PRODUCT_SPECS.items():
        # Split the annual volume across months by the seasonality curve.
        monthly_volume = np.round(spec["annual_volume"] * weights).astype(int)
        for i, month in enumerate(MONTHS):
            vol = int(monthly_volume[i])
            rows.append({
                "product":   product,
                "month":     month,
                "month_num": i + 1,
                "volume":    vol,
                "price":     spec["price"],
                "unit_cost": spec["unit_cost"],
                # Revenue and COGS are DERIVED, never hard-coded:
                "revenue":   spec["price"] * vol,
                "cogs":      spec["unit_cost"] * vol,
            })
    return pd.DataFrame(rows)


def build_opex():
    """Build the cost-centre operating-expense budget in TIDY (long) form.

    Each cost centre's annual budget is spread across months with the same
    seasonality curve. Columns: cost_centre, month, month_num, opex
    """
    weights = _monthly_weights()
    rows = []
    for centre, annual in COST_CENTRE_SPECS.items():
        monthly = annual * weights
        for i, month in enumerate(MONTHS):
            rows.append({
                "cost_centre": centre,
                "month":       month,
                "month_num":   i + 1,
                "opex":        round(float(monthly[i]), 2),
            })
    return pd.DataFrame(rows)


def build_budget():
    """Return the full budget as a dict of two tidy DataFrames.

    Keys:
      'products' : product x month revenue/COGS driver table
      'opex'     : cost-centre x month operating-expense table
    """
    return {"products": build_products(), "opex": build_opex()}
