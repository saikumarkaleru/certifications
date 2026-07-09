"""
ratios.py -- the classic credit ratio families
==============================================

Given a standardised spread (from data.py) this computes, for every fiscal
year, the ratios a credit committee actually looks at, grouped into families:

  LEVERAGE        Debt/EBITDA, Net Debt/EBITDA, Debt/Equity, Gearing
  COVERAGE        Interest Coverage (EBIT), EBITDA Interest Coverage, FCCR
  LIQUIDITY       Current Ratio, Quick Ratio
  PROFITABILITY   EBITDA Margin, Net Margin, ROCE
  WORKING CAPITAL DSO, DIO, DPO, Cash Conversion Cycle

DSCR itself lives in serviceability.py because it needs the debt schedule and a
CFADS build; everything here is a one-line ratio off the spread.

Every function is plain division so each number is defensible line by line. A
zero or missing denominator returns NaN rather than raising, because a real
spread frequently has a company with, say, no interest expense in a year.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Fraction of reported capex we treat as *maintenance* (non-discretionary)
# capex when building cash available for debt service. Growth capex is assumed
# to be deferrable under stress, so only maintenance capex is a fixed charge.
MAINT_CAPEX_RATIO = 0.40

DAYS = 365.0

# The headline ratios we surface in the console/summary (order matters).
KEY_RATIOS = [
    "Net Debt/EBITDA (x)",
    "Debt/Equity (x)",
    "Interest Coverage (x)",
    "EBITDA Margin (%)",
    "ROCE (%)",
    "Current Ratio (x)",
    "Cash Conversion Cycle (days)",
]


def _safe(n, d):
    """n / d, but NaN if the denominator is zero / missing / non-positive-sensitive."""
    if d is None or pd.isna(d) or d == 0:
        return np.nan
    return n / d


def maintenance_capex(facts, yr):
    return MAINT_CAPEX_RATIO * facts.at["Capex", yr]


def compute_year(facts, yr):
    """All ratios for a single fiscal year -> dict {ratio name: value}."""
    g = lambda k: facts.at[k, yr]  # noqa: E731  (tiny local getter)

    revenue = g("Revenue")
    cogs = g("COGS")
    ebitda = g("EBITDA")
    ebit = g("EBIT")
    interest = g("Interest Expense")
    net_income = g("Net Income")
    cash = g("Cash & Equivalents")
    debt = g("Total Debt")
    equity = g("Total Equity")
    net_debt = debt - cash
    cur_assets = g("Current Assets")
    cur_liab = g("Current Liabilities")
    inventory = g("Inventory")
    receivables = g("Accounts Receivable")
    payables = g("Accounts Payable")
    total_assets = g("Total Assets")
    principal = g("Scheduled Principal Repayment")
    maint_capex = MAINT_CAPEX_RATIO * g("Capex")

    capital_employed = total_assets - cur_liab
    fixed_charges = interest + principal

    return {
        # --- Leverage ---
        "Debt/EBITDA (x)": _safe(debt, ebitda),
        "Net Debt/EBITDA (x)": _safe(net_debt, ebitda),
        "Debt/Equity (x)": _safe(debt, equity),
        "Gearing (%)": 100.0 * _safe(debt, debt + equity),
        # --- Coverage ---
        "Interest Coverage (x)": _safe(ebit, interest),
        "EBITDA Interest Cover (x)": _safe(ebitda, interest),
        "FCCR (x)": _safe(ebitda - maint_capex, fixed_charges),
        # --- Liquidity ---
        "Current Ratio (x)": _safe(cur_assets, cur_liab),
        "Quick Ratio (x)": _safe(cur_assets - inventory, cur_liab),
        # --- Profitability ---
        "EBITDA Margin (%)": 100.0 * _safe(ebitda, revenue),
        "Net Margin (%)": 100.0 * _safe(net_income, revenue),
        "ROCE (%)": 100.0 * _safe(ebit, capital_employed),
        # --- Working capital cycle ---
        "DSO (days)": DAYS * _safe(receivables, revenue),
        "DIO (days)": DAYS * _safe(inventory, cogs),
        "DPO (days)": DAYS * _safe(payables, cogs),
        "Cash Conversion Cycle (days)": (
            DAYS * _safe(receivables, revenue)
            + DAYS * _safe(inventory, cogs)
            - DAYS * _safe(payables, cogs)
        ),
    }


def compute_ratios(facts):
    """Ratio table for every year -> DataFrame (index=ratio, columns=years)."""
    cols = {yr: compute_year(facts, yr) for yr in sorted(facts.columns)}
    return pd.DataFrame(cols)


def latest_ratios(facts):
    """Just the most recent year's ratios as a dict."""
    return compute_year(facts, max(facts.columns))
