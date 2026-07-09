"""
serviceability.py -- can the borrower actually pay the debt?
===========================================================

Leverage ratios tell you HOW MUCH debt there is; serviceability tells you
whether the CASH FLOW covers what falls due. The centre of gravity here is
DSCR (Debt-Service Coverage Ratio):

        DSCR = CFADS / Debt Service

where
   Debt Service = Interest Expense + Scheduled Principal Repayment
   CFADS (Cash Flow Available for Debt Service)
                = EBITDA - Cash Taxes - Maintenance Capex

We build CFADS from EBITDA (a cash proxy) minus the two unavoidable cash
outflows that rank ahead of, or alongside, lenders in practice: taxes and the
capex needed just to keep the asset base running. Growth capex is treated as
discretionary (see ratios.MAINT_CAPEX_RATIO) so it is NOT a fixed charge.

We also report ICR (interest-only cover) because a covenant pack usually tests
both: a borrower can clear ICR comfortably yet fail DSCR once bulky principal
amortisation is layered on top.

Headroom classes turn the DSCR number into the sentence a committee wants:
   >= 1.50  Comfortable      1.25-1.50  Adequate
   1.00-1.25 Thin            < 1.00     Shortfall
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .ratios import MAINT_CAPEX_RATIO


def effective_tax_rate(facts, yr):
    """Cash-tax proxy: reported tax / PBT, floored at 0 (losses pay no tax)."""
    pbt = facts.at["PBT", yr]
    tax = facts.at["Tax", yr]
    if pd.isna(pbt) or pbt <= 0:
        return 0.0
    return max(0.0, tax / pbt)


def cfads(facts, yr, ebitda=None, tax=None):
    """Cash Flow Available for Debt Service.

    Optional overrides let scenario.py feed a stressed EBITDA / tax without
    duplicating the formula.
    """
    if ebitda is None:
        ebitda = facts.at["EBITDA", yr]
    if tax is None:
        tax = max(0.0, facts.at["Tax", yr])
    maint_capex = MAINT_CAPEX_RATIO * facts.at["Capex", yr]
    return ebitda - tax - maint_capex


def debt_service(facts, yr, interest=None):
    if interest is None:
        interest = facts.at["Interest Expense", yr]
    return interest + facts.at["Scheduled Principal Repayment", yr]


def dscr(facts, yr, ebitda=None, interest=None, tax=None):
    ds = debt_service(facts, yr, interest=interest)
    if ds == 0 or pd.isna(ds):
        return np.nan
    return cfads(facts, yr, ebitda=ebitda, tax=tax) / ds


def icr(facts, yr, ebitda=None, interest=None):
    """Interest cover on an EBIT basis (EBIT / interest)."""
    if interest is None:
        interest = facts.at["Interest Expense", yr]
    if interest == 0 or pd.isna(interest):
        return np.nan
    if ebitda is None:
        ebit = facts.at["EBIT", yr]
    else:  # stressed EBITDA flows to EBIT via unchanged D&A
        ebit = ebitda - facts.at["Depreciation & Amortization", yr]
    return ebit / interest


def headroom_class(d):
    if pd.isna(d):
        return "n/a"
    if d >= 1.50:
        return "Comfortable"
    if d >= 1.25:
        return "Adequate"
    if d >= 1.00:
        return "Thin"
    return "Shortfall"


def serviceability_table(facts):
    """Per-year CFADS / debt service / DSCR / ICR + headroom -> DataFrame."""
    rows = {}
    for yr in sorted(facts.columns):
        d = dscr(facts, yr)
        rows[yr] = {
            "EBITDA": facts.at["EBITDA", yr],
            "Cash Tax": max(0.0, facts.at["Tax", yr]),
            "Maintenance Capex": MAINT_CAPEX_RATIO * facts.at["Capex", yr],
            "CFADS": cfads(facts, yr),
            "Interest": facts.at["Interest Expense", yr],
            "Principal Due": facts.at["Scheduled Principal Repayment", yr],
            "Debt Service": debt_service(facts, yr),
            "DSCR (x)": d,
            "ICR (x)": icr(facts, yr),
            "Headroom": headroom_class(d),
        }
    return pd.DataFrame(rows)
