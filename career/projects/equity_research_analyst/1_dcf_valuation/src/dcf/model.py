"""
model.py -- the DCF engine.

Given a base FCFF, a discount rate (WACC) and a handful of assumptions, this
module:
  * projects FCFF for N years with a FADING growth rate (high growth early that
    decays toward the terminal rate -- more realistic than a flat number),
  * builds TWO terminal values (Gordon perpetuity AND an exit EV/EBITDA
    multiple) and averages them,
  * discounts everything to an enterprise value, bridges to equity value and a
    per-share intrinsic value,
  * runs bull / base / bear SCENARIOS,
  * builds a 2-way SENSITIVITY grid (WACC x terminal growth), and
  * runs a REVERSE DCF (what constant growth does today's price imply?).

The maths is deliberately plain (numpy arrays, one perpetuity formula, one
bisection solver) so every line is explainable.
"""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# Growth path
# ---------------------------------------------------------------------------
def fading_growth_path(start_g, terminal_g, years):
    """
    A linearly FADING growth vector from `start_g` (year 1) down to
    `terminal_g` (year N). Companies rarely grow at a constant rate; growth
    typically decays toward the economy's long-run rate.
    """
    return np.linspace(start_g, terminal_g, years)


# ---------------------------------------------------------------------------
# Core single-run DCF
# ---------------------------------------------------------------------------
def run_dcf(base_fcff, start_growth, terminal_growth, wacc, net_debt, shares,
            years=5, base_ebitda=None, exit_multiple=None,
            terminal_weight_gordon=0.5):
    """
    Run one full DCF and return every intermediate number.

    Terminal value is a blend of:
      * Gordon growth: TV = FCFF_N * (1+g) / (WACC - g)
      * Exit multiple: TV = exit_multiple * (projected terminal EBITDA)
    weighted by `terminal_weight_gordon` (0.5 = simple average).
    """
    if terminal_growth >= wacc:
        raise ValueError("Terminal growth must be below WACC (Gordon breaks).")

    yr = np.arange(1, years + 1)
    g_path = fading_growth_path(start_growth, terminal_growth, years)

    # Compound the base FCFF along the fading growth path.
    growth_factors = np.cumprod(1.0 + g_path)
    projected = base_fcff * growth_factors

    discount = 1.0 / (1.0 + wacc) ** yr
    pv_fcff = projected * discount

    # --- Terminal value: Gordon ---
    tv_gordon = projected[-1] * (1.0 + terminal_growth) / (wacc - terminal_growth)

    # --- Terminal value: exit multiple on projected terminal EBITDA ---
    tv_exit = None
    if base_ebitda and exit_multiple:
        term_ebitda = base_ebitda * float(growth_factors[-1])
        tv_exit = exit_multiple * term_ebitda

    if tv_exit is not None:
        w = terminal_weight_gordon
        terminal_value = w * tv_gordon + (1.0 - w) * tv_exit
    else:
        terminal_value = tv_gordon

    pv_terminal = terminal_value * discount[-1]

    enterprise_value = pv_fcff.sum() + pv_terminal
    equity_value = enterprise_value - net_debt
    value_per_share = equity_value / shares

    return {
        "years": yr,
        "growth_path": g_path,
        "projected_fcff": projected,
        "discount_factors": discount,
        "pv_fcff": pv_fcff,
        "tv_gordon": tv_gordon,
        "tv_exit": tv_exit,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "pv_explicit": float(pv_fcff.sum()),
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "value_per_share": value_per_share,
        "terminal_pct_of_ev": pv_terminal / enterprise_value,
    }


# ---------------------------------------------------------------------------
# Scenarios: bull / base / bear
# ---------------------------------------------------------------------------
def run_scenarios(base_fcff, wacc, net_debt, shares, years,
                  base_ebitda, exit_multiple,
                  base_growth=0.08, base_terminal=0.025):
    """
    Three coherent stories. Bull = faster growth + slightly lower WACC; Bear =
    slower growth + higher WACC. This shows a valuation RANGE, not false
    precision.
    """
    specs = {
        "Bear": dict(start=base_growth - 0.04, term=base_terminal - 0.005,
                     wacc=wacc + 0.010, exit_m=(exit_multiple or 0) * 0.85),
        "Base": dict(start=base_growth, term=base_terminal,
                     wacc=wacc, exit_m=exit_multiple),
        "Bull": dict(start=base_growth + 0.04, term=base_terminal + 0.005,
                     wacc=wacc - 0.010, exit_m=(exit_multiple or 0) * 1.15),
    }
    out = {}
    for name, s in specs.items():
        res = run_dcf(base_fcff, s["start"], s["term"], s["wacc"], net_debt,
                      shares, years, base_ebitda,
                      s["exit_m"] if s["exit_m"] else None)
        out[name] = {
            "start_growth": s["start"],
            "terminal_growth": s["term"],
            "wacc": s["wacc"],
            "value_per_share": res["value_per_share"],
            "enterprise_value": res["enterprise_value"],
            "result": res,
        }
    return out


# ---------------------------------------------------------------------------
# Two-way sensitivity: value/share across WACC (rows) x terminal g (cols)
# ---------------------------------------------------------------------------
def sensitivity_grid(base_fcff, start_growth, net_debt, shares, years,
                     base_ebitda, exit_multiple,
                     wacc_center, terminal_center,
                     wacc_step=0.01, term_step=0.005, n=5):
    """
    Return (wacc_values, term_values, matrix) where matrix[i][j] is the intrinsic
    value/share at wacc_values[i] and term_values[j]. Cells with g>=WACC are NaN.
    """
    half = n // 2
    wacc_vals = [round(wacc_center + (i - half) * wacc_step, 4) for i in range(n)]
    term_vals = [round(terminal_center + (j - half) * term_step, 4)
                 for j in range(n)]
    matrix = np.full((n, n), np.nan)
    for i, w in enumerate(wacc_vals):
        for j, g in enumerate(term_vals):
            if g < w and w > 0:
                try:
                    res = run_dcf(base_fcff, start_growth, g, w, net_debt,
                                  shares, years, base_ebitda, exit_multiple)
                    matrix[i][j] = res["value_per_share"]
                except Exception:
                    matrix[i][j] = np.nan
    return wacc_vals, term_vals, matrix


# ---------------------------------------------------------------------------
# Reverse DCF: what constant growth does the current price imply?
# ---------------------------------------------------------------------------
def reverse_dcf(current_price, base_fcff, terminal_growth, wacc, net_debt,
                shares, years, base_ebitda=None, exit_multiple=None,
                lo=-0.20, hi=0.60, tol=1e-4, max_iter=200):
    """
    Solve for the (constant) year-1 growth rate that makes the DCF's intrinsic
    value/share equal the current market price -- i.e. "what is the market
    assuming?" We use bisection, which is robust and easy to explain: value is
    monotonically increasing in growth, so we squeeze the bracket.
    """
    def value_at(g):
        res = run_dcf(base_fcff, g, terminal_growth, wacc, net_debt, shares,
                      years, base_ebitda, exit_multiple)
        return res["value_per_share"]

    f_lo = value_at(lo) - current_price
    f_hi = value_at(hi) - current_price
    if f_lo > 0 and f_hi > 0:
        return {"implied_growth": None, "note": "price below even bearish case"}
    if f_lo < 0 and f_hi < 0:
        return {"implied_growth": None, "note": "price above even bullish case"}

    a, b = lo, hi
    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fm = value_at(mid) - current_price
        if abs(fm) < tol or (b - a) / 2.0 < tol:
            return {"implied_growth": mid,
                    "note": "constant year-1 growth implied by price"}
        if (value_at(a) - current_price) * fm < 0:
            b = mid
        else:
            a = mid
    return {"implied_growth": (a + b) / 2.0, "note": "max iterations reached"}
