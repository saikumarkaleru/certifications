"""
fcff.py -- derive UNLEVERED free cash flow (Free Cash Flow to the Firm) from
the financial statements.

FCFF is the cash the whole business throws off BEFORE any financing decisions
(before interest, after tax) -- i.e. the cash available to all capital
providers (debt + equity). It is the correct numerator to discount at the WACC.

Textbook build-up (the one we use as primary):

    FCFF = EBIT x (1 - tax rate)          <- unlevered, after-tax operating profit
         + Depreciation & Amortization    <- add back non-cash charge
         - Capital Expenditure            <- cash reinvested in fixed assets
         - Increase in Net Working Capital

We keep yfinance's native signs to avoid sign-flip bugs:
  * capex is reported NEGATIVE, so we ADD it (it reduces FCFF).
  * "Change In Working Capital" on the cash-flow statement is already the CASH
    IMPACT (a build in working capital shows up negative), so we ADD it too.

We also compute a cross-check from the cash-flow statement:

    FCFF (check) = Operating Cash Flow + Interest x (1 - tax) - Capex

If the two agree, the derivation is sound.
"""

from __future__ import annotations


def _tax_rate(year, default=0.21):
    """Effective tax rate for a year, clamped to a sane [0, 0.5] range."""
    tr = year.get("tax_rate")
    if tr is None:
        pretax, tax = year.get("pretax_income"), year.get("tax_provision")
        if pretax and tax is not None and pretax != 0:
            tr = tax / pretax
    if tr is None or tr < 0 or tr > 0.5:
        return default
    return tr


def fcff_from_year(year, cost_of_debt_hint=0.05):
    """
    Compute FCFF (and its components) for a single fiscal-year dict.

    Returns a dict with the build-up, the cross-check, and the tax rate used.
    """
    ebit = year.get("ebit")
    if ebit is None:
        raise ValueError("Cannot compute FCFF without EBIT.")

    t = _tax_rate(year)
    dep = year.get("dep_amort") or 0.0
    capex = year.get("capex") or 0.0                 # negative in yfinance
    chg_wc = year.get("change_in_wc") or 0.0         # cash impact, signed

    nopat = ebit * (1.0 - t)                          # unlevered after-tax profit
    fcff = nopat + dep + capex + chg_wc

    # Cross-check straight off the cash-flow statement.
    cfo = year.get("operating_cash_flow")
    interest = year.get("interest_expense")
    check = None
    if cfo is not None:
        # If interest expense is not disclosed, approximate it from a hint.
        if interest is None:
            interest = 0.0  # conservative: treat as ~0 add-back
        check = cfo + interest * (1.0 - t) - abs(capex)

    return {
        "year": year.get("year"),
        "ebit": ebit,
        "tax_rate": t,
        "nopat": nopat,
        "dep_amort": dep,
        "capex": capex,
        "change_in_wc": chg_wc,
        "fcff": fcff,
        "fcff_check": check,
    }


def build_fcff_history(company):
    """Compute FCFF for every year we have, most-recent first."""
    rows = []
    for year in company.get("history", []):
        try:
            rows.append(fcff_from_year(year))
        except Exception:
            continue
    if not rows:
        raise ValueError("No years with enough data to compute FCFF.")
    return rows


def base_fcff(company, method="latest"):
    """
    The starting FCFF we project forward.

    method="latest"  -> most recent fiscal year (default).
    method="average" -> average of the available years (smooths one odd year).
    """
    rows = build_fcff_history(company)
    values = [r["fcff"] for r in rows]
    if method == "average" and len(values) > 1:
        return sum(values) / len(values), rows
    return values[0], rows


def latest_ebitda(company):
    """Most recent EBITDA (needed for the exit-multiple terminal value)."""
    for year in company.get("history", []):
        if year.get("ebitda") is not None:
            return year["ebitda"]
    return None
