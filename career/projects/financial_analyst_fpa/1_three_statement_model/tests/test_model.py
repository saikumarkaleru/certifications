"""
tests/test_model.py — prove the model is internally consistent.
============================================================================
These are the checks a reviewer actually cares about:
  * the balance sheet ties out to ~0 EVERY year (assets = liab + equity),
  * ending cash rolls forward correctly (CF ending cash == BS cash, and the
    year-on-year change equals the CF net change),
  * the DCF produces a positive, finite value,
  * the sensitivity table has the shape we expect.

Runs under pytest (`python -m pytest tests/ -q`) OR standalone
(`python tests/test_model.py`) via the __main__ block at the bottom.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

from model import data, forecast, scenarios, valuation  # noqa: E402

# Use the bundled fallback so tests are deterministic and never need a network.
DRIVERS = dict(data.FALLBACK_DRIVERS)
OPENING = data._finalise_opening(dict(data.FALLBACK_OPENING))
META = dict(data.FALLBACK_META)


def _model():
    return forecast.build_model(DRIVERS, OPENING)


def test_opening_balance_sheet_balances():
    assets = (OPENING["cash"] + OPENING["receivables"]
              + OPENING["inventory"] + OPENING["ppe"])
    liab_eq = OPENING["payables"] + OPENING["term_debt"] + OPENING["revolver"] + OPENING["equity"]
    assert abs(assets - liab_eq) < 1e-6


def test_balance_sheet_ties_out_every_year():
    m = _model()
    check = m["balance"].loc["Balance Check (=0)"]
    assert check.abs().max() < 1e-3, f"balance sheet does not tie out: {check.to_dict()}"


def test_ending_cash_rolls_forward():
    """CF ending cash must equal BS cash, and match last cash + net change."""
    m = _model()
    cf, bs = m["cashflow"], m["balance"]
    years = m["years"]

    # CF ending cash == BS cash for every year
    for y in years:
        assert abs(cf.loc["Ending Cash", y] - bs.loc["Cash", y]) < 1e-6

    # year 1 change is measured off the opening cash; later years off prior year
    prev_cash = OPENING["cash"]
    for y in years:
        rolled = prev_cash + cf.loc["Net Change in Cash", y]
        # tolerance of 0.2 absorbs the display rounding (frames are round(1))
        assert abs(rolled - cf.loc["Ending Cash", y]) < 0.2
        prev_cash = cf.loc["Ending Cash", y]


def test_cash_never_below_buffer():
    """The revolver should keep cash at or above the minimum buffer every year."""
    m = _model()
    # min cash buffer is a % of that year's revenue
    for y in m["years"]:
        revenue = m["income"].loc["Revenue", y]
        min_cash = revenue * DRIVERS["min_cash_pct"]
        assert m["balance"].loc["Cash", y] >= min_cash - 1e-3


def test_dcf_value_is_positive_and_finite():
    import math
    m = _model()
    dcf = valuation.run_dcf(m, DRIVERS, OPENING, META)
    assert math.isfinite(dcf["enterprise_value"]) and dcf["enterprise_value"] > 0
    assert math.isfinite(dcf["equity_value"]) and dcf["equity_value"] > 0
    assert math.isfinite(dcf["value_per_share"]) and dcf["value_per_share"] > 0
    assert 0 < dcf["wacc"] < 0.30  # sane discount rate


def test_scenarios_ordered_and_balanced():
    """Bull should value higher than Bear, and each scenario must still tie out."""
    scen = scenarios.run_scenarios(DRIVERS, OPENING, META)
    assert list(scen.columns) == ["Bull", "Base", "Bear"]
    vps = scen.loc["Value per Share ($)"]
    assert vps["Bull"] > vps["Base"] > vps["Bear"]
    assert scen.loc["Max Balance-Sheet Imbalance"].abs().max() < 1e-3


def test_sensitivity_table_shape():
    sens = scenarios.sensitivity_table(DRIVERS, OPENING, META)
    assert sens.shape == (5, 5)          # 5 growth rows x 5 margin cols
    # values should generally rise left-to-right (higher margin -> higher value)
    mid = sens.iloc[2]
    assert mid.iloc[-1] > mid.iloc[0]


if __name__ == "__main__":
    # allow `python tests/test_model.py` with no pytest installed
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {fn.__name__}: {e}")
    print(f"\n{len(fns) - failed}/{len(fns)} tests passed")
    sys.exit(1 if failed else 0)
