"""
scenarios.py — bull / base / bear cases and a 2-way DCF sensitivity table.
============================================================================
Two classic FP&A techniques sit here:

1. SCENARIOS — re-run the whole model under different assumptions to bracket the
   outcome. We flex the two drivers that matter most: revenue growth and gross
   margin. Bull = optimistic, Base = the derived assumptions, Bear = stress.

2. SENSITIVITY TABLE — a 2-way grid that shows how one output moves as two
   inputs change. Rows = revenue growth, columns = gross margin, and each cell
   is the DCF equity value PER SHARE. It answers "what has to be true for the
   valuation to hold?" at a glance.
"""

from __future__ import annotations

import pandas as pd

from . import forecast, valuation

# How each scenario tilts the base drivers (added to base growth / margin).
SCENARIOS = {
    "Bull": {"growth_delta": +0.04, "margin_delta": +0.03},
    "Base": {"growth_delta":  0.00, "margin_delta":  0.00},
    "Bear": {"growth_delta": -0.05, "margin_delta": -0.04},
}


def _with_overrides(drivers: dict, growth: float = None, margin: float = None) -> dict:
    """Copy the drivers and swap in a new growth and/or gross margin."""
    d = dict(drivers)
    if growth is not None:
        d["revenue_growth"] = growth
    if margin is not None:
        d["gross_margin"] = max(0.05, min(0.95, margin))
    return d


def run_scenarios(base_drivers: dict, opening: dict, meta: dict) -> pd.DataFrame:
    """
    Build every scenario and summarise the headline numbers side by side.
    Columns = Bull/Base/Bear; rows = the metrics an interviewer would ask for.
    """
    out = {}
    for name, tilt in SCENARIOS.items():
        d = _with_overrides(
            base_drivers,
            growth=base_drivers["revenue_growth"] + tilt["growth_delta"],
            margin=base_drivers["gross_margin"] + tilt["margin_delta"],
        )
        m = forecast.build_model(d, opening)
        dcf = valuation.run_dcf(m, d, opening, meta)

        last = m["years"][-1]
        out[name] = {
            "Revenue Growth": d["revenue_growth"],
            "Gross Margin": d["gross_margin"],
            "Final-Year Revenue ($m)": m["income"].loc["Revenue", last],
            "Final-Year Net Income ($m)": m["income"].loc["Net Income", last],
            "Final-Year Ending Cash ($m)": m["balance"].loc["Cash", last],
            "Final-Year Equity ($m)": m["balance"].loc["Equity", last],
            "Enterprise Value ($m)": dcf["enterprise_value"],
            "Equity Value ($m)": dcf["equity_value"],
            "Value per Share ($)": dcf["value_per_share"],
            "Max Balance-Sheet Imbalance": m["max_imbalance"],
        }
    return pd.DataFrame(out).round(2)


def sensitivity_table(base_drivers: dict, opening: dict, meta: dict,
                      growth_steps=(-0.04, -0.02, 0.0, 0.02, 0.04),
                      margin_steps=(-0.04, -0.02, 0.0, 0.02, 0.04)) -> pd.DataFrame:
    """
    2-way sensitivity of the DCF value per share.

    Rows    = revenue growth   (base +/- each step)
    Columns = gross margin      (base +/- each step)
    Cells   = DCF equity value per share ($)
    """
    base_g = base_drivers["revenue_growth"]
    base_m = base_drivers["gross_margin"]

    rows = {}
    for gd in growth_steps:
        g = base_g + gd
        row = {}
        for md in margin_steps:
            m_val = base_m + md
            d = _with_overrides(base_drivers, growth=g, margin=m_val)
            model = forecast.build_model(d, opening)
            dcf = valuation.run_dcf(model, d, opening, meta)
            row[f"GM {m_val:.0%}"] = round(dcf["value_per_share"], 2)
        rows[f"Growth {g:.0%}"] = row

    return pd.DataFrame(rows).T  # rows = growth, cols = margin
