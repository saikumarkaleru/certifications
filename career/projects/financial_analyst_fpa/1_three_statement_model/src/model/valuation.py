"""
valuation.py — a DCF valuation built off the model's own free cash flow.
============================================================================
A discounted-cash-flow (DCF) values a business as the present value of the cash
it will generate. We use the UNLEVERED free cash flow (FCFF) the forecast
already produced, discount it at the WACC, add a terminal value for everything
beyond the forecast window, and back into an equity value per share.

The steps (this is the whole interview answer):
  1. WACC — the blended required return of debt and equity holders.
        cost of equity  = risk-free + beta * equity-risk-premium   (CAPM)
        cost of debt    = interest rate * (1 - tax)                 (after-tax)
        WACC            = We*Ke + Wd*Kd, weighted by equity vs debt.
  2. Discount each year's FCFF back to today at the WACC.
  3. Terminal value (Gordon growth): TV = FCFF_last*(1+g) / (WACC - g),
        then discount that back too.
  4. Enterprise value (EV) = PV(FCFF) + PV(terminal value).
  5. Equity value = EV - net debt (debt - cash).  Per share = equity / shares.
"""

from __future__ import annotations

# CAPM inputs — standard, defensible market assumptions (change and re-defend).
RISK_FREE = 0.043            # ~10-year US Treasury yield
EQUITY_RISK_PREMIUM = 0.050  # long-run excess return of equities over bonds
TERMINAL_GROWTH = 0.025      # cash flows grow ~2.5% forever (near long-run GDP)


def wacc(drivers: dict, opening: dict, meta: dict) -> dict:
    """Compute the WACC and return the pieces so they can be shown/defended."""
    beta = meta.get("beta", 0.9)
    tax = drivers["tax_rate"]

    cost_of_equity = RISK_FREE + beta * EQUITY_RISK_PREMIUM      # CAPM
    cost_of_debt_after_tax = drivers["interest_rate"] * (1 - tax)

    # Capital weights: market value of equity (price * shares) vs total debt.
    equity_val = meta.get("price", 0) * meta.get("shares_out", 0)
    debt_val = opening["term_debt"] + opening["revolver"]
    total = equity_val + debt_val
    if total <= 0:                       # degenerate data -> equal weights
        w_e = w_d = 0.5
    else:
        w_e, w_d = equity_val / total, debt_val / total

    wacc_val = w_e * cost_of_equity + w_d * cost_of_debt_after_tax
    return {
        "beta": beta,
        "cost_of_equity": cost_of_equity,
        "cost_of_debt_after_tax": cost_of_debt_after_tax,
        "weight_equity": w_e,
        "weight_debt": w_d,
        "wacc": wacc_val,
    }


def run_dcf(model: dict, drivers: dict, opening: dict, meta: dict,
            terminal_growth: float = TERMINAL_GROWTH) -> dict:
    """
    Value the business off the model's FCFF row.

    Returns a dict with the WACC pieces, PV of each year, terminal value,
    enterprise value, equity value and value per share.
    """
    w = wacc(drivers, opening, meta)
    r = w["wacc"]
    g = terminal_growth

    fcff_row = model["fcff"].loc["FCFF"]        # one FCFF per forecast year
    fcffs = list(fcff_row.values)

    # 2) present value of each explicit-year FCFF
    pv_fcffs = [cf / (1 + r) ** (t + 1) for t, cf in enumerate(fcffs)]

    # 3) terminal value at the end of the forecast, then discounted to today
    n = len(fcffs)
    if r > g:
        terminal_value = fcffs[-1] * (1 + g) / (r - g)     # Gordon growth
    else:
        terminal_value = fcffs[-1] * 15.0                  # guard: crude exit multiple
    pv_terminal = terminal_value / (1 + r) ** n

    # 4) enterprise value
    enterprise_value = sum(pv_fcffs) + pv_terminal

    # 5) bridge to equity value: subtract net debt (debt minus cash)
    net_debt = (opening["term_debt"] + opening["revolver"]) - opening["cash"]
    equity_value = enterprise_value - net_debt
    shares = meta.get("shares_out", 0) or 1.0
    value_per_share = equity_value / shares

    return {
        **w,
        "terminal_growth": g,
        "pv_fcffs": pv_fcffs,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "net_debt": net_debt,
        "equity_value": equity_value,
        "shares_out": shares,
        "value_per_share": value_per_share,
    }
