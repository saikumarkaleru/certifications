"""
ratios.py -- the four families of financial ratios
==================================================

Given one company's `facts` table (field x year, from data.py) we compute the
ratios an analyst actually quotes, grouped the way an analyst thinks:

  PROFITABILITY -- is the business making good money on sales and capital?
  LIQUIDITY     -- can it pay its bills over the next 12 months?
  LEVERAGE      -- how much debt, and can it comfortably service it?
  EFFICIENCY    -- how hard is it working its assets and working capital?

Two small conventions used throughout, both standard on a real desk:

  * Income-statement items are FLOWS (earned over the year) while balance-sheet
    items are STOCKS (a snapshot at year-end). When we divide a flow by a stock
    (ROA, ROE, turnover) we use the AVERAGE of this year's and last year's
    balance, because the flow was earned across the whole year. The first year
    has no prior, so we fall back to the year-end balance.
  * Anything that would divide by zero (e.g. Google/Meta have ~no inventory)
    returns NaN rather than crashing. NaN just means "not meaningful here".

Output of compute_ratios(): a DataFrame, rows = ratio names, cols = years.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Days in a year for the "days" efficiency ratios (DSO/DIO/DPO). 365 is the
# convention; some shops use 360. Either is defensible; we state ours.
DAYS = 365


def _safe_div(a, b):
    """a / b, but return NaN if b is zero/NaN/None (instead of raising)."""
    if b is None or pd.isna(b) or b == 0:
        return float("nan")
    if a is None or pd.isna(a):
        return float("nan")
    return a / b


def _avg(facts, field, year, prior_year):
    """Average balance = (this year-end + last year-end) / 2.

    Falls back to the single year-end value when there is no prior year.
    """
    cur = facts.at[field, year] if field in facts.index else float("nan")
    if prior_year is None:
        return cur
    prev = facts.at[field, prior_year] if field in facts.index else float("nan")
    if pd.isna(prev):
        return cur
    return (cur + prev) / 2.0


def compute_ratios(facts):
    """Compute every ratio for one company across all available years.

    Returns a DataFrame: index = ratio name, columns = years (oldest->newest).
    """
    years = list(facts.columns)
    out = {}

    for i, y in enumerate(years):
        prior = years[i - 1] if i > 0 else None

        def v(field):                     # this-year value shortcut
            return facts.at[field, y] if field in facts.index else float("nan")

        def avg(field):                   # average-balance shortcut
            return _avg(facts, field, y, prior)

        r = {}

        # ---------------- PROFITABILITY ----------------
        # Margins: what fraction of each sales dollar survives to each line.
        r["Gross Margin %"] = 100 * _safe_div(v("Gross Profit"), v("Revenue"))
        r["Operating Margin %"] = 100 * _safe_div(v("Operating Income"), v("Revenue"))
        r["Net Margin %"] = 100 * _safe_div(v("Net Income"), v("Revenue"))
        # ROA/ROE: profit per dollar of assets / of shareholder capital.
        r["ROA %"] = 100 * _safe_div(v("Net Income"), avg("Total Assets"))
        r["ROE %"] = 100 * _safe_div(v("Net Income"), avg("Equity"))
        # ROIC: after-tax operating profit (NOPAT) per dollar of invested
        # capital. NOPAT = EBIT x (1 - effective tax rate). This strips out how
        # the company is financed, so it is comparable across capital structures.
        tax_rate = _safe_div(v("Tax Provision"), v("Pretax Income"))
        if pd.isna(tax_rate):
            tax_rate = 0.21               # sensible corporate default if missing
        nopat = v("EBIT") * (1 - tax_rate)
        r["ROIC %"] = 100 * _safe_div(nopat, avg("Invested Capital"))

        # ---------------- LIQUIDITY ----------------
        # Current: all short-term assets vs short-term bills.
        r["Current Ratio"] = _safe_div(v("Current Assets"), v("Current Liabilities"))
        # Quick: strip inventory (hardest to turn into cash fast).
        r["Quick Ratio"] = _safe_div(
            v("Current Assets") - (v("Inventory") if not pd.isna(v("Inventory")) else 0),
            v("Current Liabilities"))
        # Cash: the most conservative -- only cash covers the bills.
        r["Cash Ratio"] = _safe_div(v("Cash"), v("Current Liabilities"))

        # ---------------- LEVERAGE / SOLVENCY ----------------
        r["Debt / Equity"] = _safe_div(v("Total Debt"), v("Equity"))
        r["Debt / Assets"] = _safe_div(v("Total Debt"), v("Total Assets"))
        # Interest coverage: how many times operating profit covers interest.
        r["Interest Coverage"] = _safe_div(v("EBIT"), v("Interest Expense"))
        # Net debt / EBITDA: years of cash earnings to repay debt net of cash.
        ebitda = v("EBIT") + (v("D&A") if not pd.isna(v("D&A")) else 0)
        net_debt = v("Total Debt") - (v("Cash") if not pd.isna(v("Cash")) else 0)
        r["Net Debt / EBITDA"] = _safe_div(net_debt, ebitda)

        # ---------------- EFFICIENCY ----------------
        r["Asset Turnover"] = _safe_div(v("Revenue"), avg("Total Assets"))
        # Receivables turnover / DSO: how fast customers pay (days sales out).
        rec_turn = _safe_div(v("Revenue"), avg("Receivables"))
        r["Receivables Turnover"] = rec_turn
        r["DSO (days)"] = _safe_div(DAYS, rec_turn)
        # Inventory turnover / DIO: how fast stock sells (days inventory out).
        # COGS is the right numerator (inventory is carried at cost, not price).
        inv_turn = _safe_div(v("COGS"), avg("Inventory"))
        r["Inventory Turnover"] = inv_turn
        r["DIO (days)"] = _safe_div(DAYS, inv_turn)
        # Payables turnover / DPO: how slowly the company pays suppliers.
        pay_turn = _safe_div(v("COGS"), avg("Payables"))
        r["Payables Turnover"] = pay_turn
        r["DPO (days)"] = _safe_div(DAYS, pay_turn)
        # Cash conversion cycle = DSO + DIO - DPO. Days of cash tied up in
        # working capital. Lower (even negative) is better -- Apple famously
        # runs negative CCC because suppliers finance its inventory.
        dso = r["DSO (days)"]
        dio = r["DIO (days)"] if not pd.isna(r["DIO (days)"]) else 0
        dpo = r["DPO (days)"] if not pd.isna(r["DPO (days)"]) else 0
        r["Cash Conversion Cycle (days)"] = (dso + dio - dpo) if not pd.isna(dso) else float("nan")

        out[y] = r

    df = pd.DataFrame(out)                # index = ratio, columns = year
    return df.round(3)


# The ratios we headline in benchmarking / trends, in a stable display order.
KEY_RATIOS = [
    "Gross Margin %", "Operating Margin %", "Net Margin %",
    "ROA %", "ROE %", "ROIC %",
    "Current Ratio", "Quick Ratio",
    "Debt / Equity", "Interest Coverage", "Net Debt / EBITDA",
    "Asset Turnover", "DSO (days)", "Cash Conversion Cycle (days)",
]

# For these ratios a LOWER number is the better outcome. Everything else in
# KEY_RATIOS is "higher is better". Used by benchmarking and trend logic so we
# score direction correctly.
LOWER_IS_BETTER = {
    "Debt / Equity", "Net Debt / EBITDA",
    "DSO (days)", "Cash Conversion Cycle (days)",
}


def latest_year(facts):
    """The most recent fiscal year present (facts columns are sorted)."""
    return list(facts.columns)[-1]
