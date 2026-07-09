"""
scenario.py -- stress testing the credit
=========================================

A rating on last year's numbers is only half the job; a credit analyst asks
"what breaks it?". This module re-runs the whole spread under a set of stress
scenarios and re-derives leverage, DSCR, interest cover and the internal rating
for each, so we can see the rating migrate from base to downside.

Stress levers (applied to the latest fiscal year):
  * EBITDA haircut          -10% / -20% / -30%   (margin compression)
  * Interest-rate shock     +100bps / +200bps    (added to the full debt stack)
  * Revenue shock           -15%                  (flows to EBITDA via the gross
                                                   margin, opex held fixed =
                                                   operating leverage)
  * Downside (combined)      EBITDA -20% AND rates +200bps

Every lever rebuilds a stressed copy of the spread and then re-uses the SAME
ratio, serviceability and rating code as the base case -- so a scenario number
is computed identically to the base number, just on shocked inputs. No stress
logic is duplicated inside the rating model.
"""

from __future__ import annotations

import pandas as pd

from . import ratios as ratio_mod
from . import serviceability as svc
from . import rating as rating_mod

# (label, kwargs for make_stressed)
SCENARIOS = [
    ("Base", {}),
    ("EBITDA -10%", {"ebitda_mult": 0.90}),
    ("EBITDA -20%", {"ebitda_mult": 0.80}),
    ("EBITDA -30%", {"ebitda_mult": 0.70}),
    ("Rates +100bps", {"interest_add_bps": 100}),
    ("Rates +200bps", {"interest_add_bps": 200}),
    ("Revenue -15%", {"revenue_shock": 0.15}),
    ("Downside (EBITDA -20% & +200bps)", {"ebitda_mult": 0.80, "interest_add_bps": 200}),
]


def make_stressed(facts, yr, ebitda_mult=1.0, interest_add_bps=0, revenue_shock=0.0):
    """Return a copy of the spread with the latest year shocked.

    Revenue shock hits EBITDA through the gross margin (variable costs scale,
    operating expenses stay fixed). Then an optional flat EBITDA haircut is
    applied on top, and the rate shock is added to interest on the whole debt
    stack. Downstream lines (EBIT, PBT, tax, net income) are re-derived so the
    stressed spread stays internally consistent.
    """
    s = facts.astype(float).copy()   # float so stressed (fractional) values fit
    rev = facts.at["Revenue", yr]
    cogs = facts.at["COGS", yr]
    opex = facts.at["Operating Expenses", yr]
    da = facts.at["Depreciation & Amortization", yr]
    debt = facts.at["Total Debt", yr]

    rev_new = rev * (1 - revenue_shock)
    cogs_new = cogs * (1 - revenue_shock)
    ebitda_after_rev = rev_new - cogs_new - opex          # opex held fixed
    ebitda_new = ebitda_after_rev * ebitda_mult
    ebit_new = ebitda_new - da
    interest_new = facts.at["Interest Expense", yr] + debt * (interest_add_bps / 10000.0)
    pbt_new = ebit_new - interest_new
    eff = svc.effective_tax_rate(facts, yr)
    tax_new = max(0.0, pbt_new) * eff
    ni_new = pbt_new - tax_new

    s.at["Revenue", yr] = rev_new
    s.at["COGS", yr] = cogs_new
    s.at["EBITDA", yr] = ebitda_new
    s.at["EBIT", yr] = ebit_new
    s.at["Interest Expense", yr] = interest_new
    s.at["PBT", yr] = pbt_new
    s.at["Tax", yr] = tax_new
    s.at["Net Income", yr] = ni_new
    return s


def recompute(facts, business, yr=None, **shock):
    """Key credit metrics + rating under one shock -> dict."""
    if yr is None:
        yr = max(facts.columns)
    s = make_stressed(facts, yr, **shock)
    r = ratio_mod.compute_year(s, yr)
    card = rating_mod.scorecard(s, business, yr)
    return {
        "EBITDA": s.at["EBITDA", yr],
        "Net Debt/EBITDA (x)": r["Net Debt/EBITDA (x)"],
        "DSCR (x)": svc.dscr(s, yr),
        "ICR (x)": svc.icr(s, yr),
        "Composite": card["composite"],
        "Band": card["band"],
        "Headroom": svc.headroom_class(svc.dscr(s, yr)),
    }


def scenario_table(facts, business, yr=None):
    """Run every scenario -> DataFrame (one row per scenario)."""
    rows = {}
    for label, shock in SCENARIOS:
        rows[label] = recompute(facts, business, yr=yr, **shock)
    df = pd.DataFrame(rows).T
    df.index.name = "Scenario"
    # keep numeric columns numeric for charting / rounding
    for c in ["EBITDA", "Net Debt/EBITDA (x)", "DSCR (x)", "ICR (x)", "Composite"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df.reset_index()
