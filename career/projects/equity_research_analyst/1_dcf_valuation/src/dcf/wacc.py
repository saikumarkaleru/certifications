"""
wacc.py -- estimate the discount rate: the Weighted Average Cost of Capital.

WACC is the blended annual return that ALL of the company's investors (debt +
equity) require. Because FCFF belongs to all of them, WACC is the right rate to
discount it.

    WACC = (E / V) * Ke  +  (D / V) * Kd * (1 - tax)

where
    Ke  = cost of equity, from CAPM: Ke = rf + beta * ERP
    Kd  = pre-tax cost of debt (interest expense / total debt, or an estimate)
    E   = market value of equity  (price * shares)
    D   = market value of debt    (~ total debt on the balance sheet)
    V   = E + D
    tax = marginal/effective tax rate (interest is tax-deductible -> after-tax)

Every input here maps to a live data point or a clearly stated assumption.
"""

from __future__ import annotations

# Assumptions we can defend in one sentence each (see STUDY_GUIDE.md).
DEFAULT_ERP = 0.050          # equity risk premium ~5% (long-run US average)
DEFAULT_BETA = 1.0           # market beta if none reported
DEFAULT_RF = 0.043           # fallback risk-free if ^TNX is unavailable
DEFAULT_CREDIT_SPREAD = 0.015  # spread over rf if we must estimate cost of debt
DEFAULT_TAX = 0.21           # US federal statutory-ish rate


def cost_of_equity(risk_free, beta, erp=DEFAULT_ERP):
    """CAPM: required equity return = risk-free + beta * equity risk premium."""
    rf = DEFAULT_RF if risk_free is None else risk_free
    b = DEFAULT_BETA if beta is None else beta
    return rf + b * erp


def cost_of_debt(company, risk_free, tax_rate):
    """
    Pre- and after-tax cost of debt.

    Preferred: interest expense / total debt (what the firm actually pays).
    Fallback:  risk-free + a credit spread (when interest isn't disclosed,
               as is the case for e.g. Apple in yfinance).
    """
    rf = DEFAULT_RF if risk_free is None else risk_free
    total_debt = company.get("total_debt") or 0.0
    interest = None
    if company.get("history"):
        interest = company["history"][0].get("interest_expense")

    if interest and total_debt:
        pre_tax = abs(interest) / total_debt
        # Guard against nonsense (e.g. tiny debt): clamp to a plausible band.
        if not (0.005 <= pre_tax <= 0.20):
            pre_tax = rf + DEFAULT_CREDIT_SPREAD
    else:
        pre_tax = rf + DEFAULT_CREDIT_SPREAD

    return pre_tax, pre_tax * (1.0 - tax_rate)


def estimate_wacc(company, tax_rate=None, erp=DEFAULT_ERP):
    """
    Return a dict with the full WACC build: weights, Ke, Kd and the blend.
    """
    rf = company.get("risk_free_rate")
    if rf is None:
        rf = DEFAULT_RF
    beta = company.get("beta")

    if tax_rate is None:
        # use latest year's effective rate if available, else default
        tax_rate = DEFAULT_TAX
        if company.get("history"):
            tr = company["history"][0].get("tax_rate")
            if tr is not None and 0 <= tr <= 0.5:
                tax_rate = tr

    ke = cost_of_equity(rf, beta, erp)
    kd_pre, kd_after = cost_of_debt(company, rf, tax_rate)

    equity_val = (company.get("price") or 0.0) * (company.get("shares") or 0.0)
    debt_val = company.get("total_debt") or 0.0
    v = equity_val + debt_val
    if v <= 0:
        raise ValueError("Total capital (E+D) must be positive.")

    we, wd = equity_val / v, debt_val / v
    wacc = we * ke + wd * kd_after

    return {
        "risk_free_rate": rf,
        "beta": DEFAULT_BETA if beta is None else beta,
        "erp": erp,
        "cost_of_equity": ke,
        "cost_of_debt_pre_tax": kd_pre,
        "cost_of_debt_after_tax": kd_after,
        "tax_rate": tax_rate,
        "equity_value": equity_val,
        "debt_value": debt_val,
        "weight_equity": we,
        "weight_debt": wd,
        "wacc": wacc,
    }
