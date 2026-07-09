"""
test_variance.py - the safety net for the analytical core.

These tests protect the three claims the model makes:

  1. Price + Volume + Mix reconciles EXACTLY to the total revenue variance.
  2. Flex-budget logic reconciles: (flex - static) + (actual - flex) == total.
  3. Favorable / Unfavorable flags obey the sign convention.

The file also runs standalone (python test_variance.py) if pytest is missing.
"""

import os
import sys

# Import the package whether run under pytest (conftest handles path) or directly.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from fpa import budget as budget_mod
from fpa import actuals as actuals_mod
from fpa import variance as var_mod


def _data(seed=42):
    """Fresh budget + seeded actuals (no cache) for a clean, deterministic test."""
    budget = budget_mod.build_budget()
    actuals = actuals_mod.simulate_actuals(budget, seed=seed)
    return budget, actuals


# ---------------------------------------------------------------------------
# 1. PRICE + VOLUME + MIX must reconcile to the total revenue variance.
# ---------------------------------------------------------------------------
def test_pvm_reconciles_total():
    budget, actuals = _data()
    pvm = var_mod.pvm_decomposition(budget, actuals)

    # Per product AND for the TOTAL row, the three effects rebuild the total.
    for idx in pvm.index:
        total = pvm.loc[idx, "Total Var"]
        parts = pvm.loc[idx, "Price"] + pvm.loc[idx, "Volume"] + pvm.loc[idx, "Mix"]
        assert abs(total - parts) < 1e-4, f"PVM does not reconcile for {idx}"

    # And the "Check" column should be ~0 everywhere.
    assert pvm["Check"].abs().max() < 1e-4


def test_pvm_total_equals_actual_minus_budget():
    budget, actuals = _data()
    pvm = var_mod.pvm_decomposition(budget, actuals)
    total_var = pvm.loc["TOTAL", "Actual Rev"] - pvm.loc["TOTAL", "Budget Rev"]
    parts = pvm.loc["TOTAL", ["Price", "Volume", "Mix"]].sum()
    assert abs(total_var - parts) < 1e-3


# ---------------------------------------------------------------------------
# 2. FLEX BUDGET: activity effect + rate effect == total variance.
# ---------------------------------------------------------------------------
def test_flex_reconciles_revenue():
    budget, actuals = _data()
    flex = var_mod.flex_budget(budget, actuals)
    for idx in flex.index:
        total = flex.loc[idx, "Rev Actual"] - flex.loc[idx, "Rev Static"]
        split = flex.loc[idx, "Rev Volume Eff"] + flex.loc[idx, "Rev Rate Eff"]
        assert abs(total - split) < 1e-4, f"Flex revenue split fails for {idx}"


def test_flex_reconciles_cogs():
    budget, actuals = _data()
    flex = var_mod.flex_budget(budget, actuals)
    for idx in flex.index:
        total = flex.loc[idx, "COGS Actual"] - flex.loc[idx, "COGS Static"]
        split = flex.loc[idx, "COGS Volume Eff"] + flex.loc[idx, "COGS Rate Eff"]
        assert abs(total - split) < 1e-4, f"Flex COGS split fails for {idx}"


def test_flex_rate_effect_equals_price_variance():
    """The flex 'rate effect' on revenue must equal the PVM price variance."""
    budget, actuals = _data()
    flex = var_mod.flex_budget(budget, actuals)
    pvm = var_mod.pvm_decomposition(budget, actuals)
    assert abs(flex.loc["TOTAL", "Rev Rate Eff"] - pvm.loc["TOTAL", "Price"]) < 1e-2


# ---------------------------------------------------------------------------
# 3. FAVORABLE / UNFAVORABLE sign convention.
# ---------------------------------------------------------------------------
def test_flag_sign_convention():
    # Income line: over budget is favorable, under is unfavorable.
    assert var_mod.flag("income", +100) == "Favorable"
    assert var_mod.flag("income", -100) == "Unfavorable"
    # Cost line: under budget (negative) is favorable, over is unfavorable.
    assert var_mod.flag("cost", -100) == "Favorable"
    assert var_mod.flag("cost", +100) == "Unfavorable"
    # Zero is on plan for both.
    assert var_mod.flag("income", 0) == "On Plan"
    assert var_mod.flag("cost", 0) == "On Plan"


def test_flags_applied_correctly_in_tables():
    """Spot-check that the product/opex tables label rows with the right flag."""
    budget, actuals = _data()
    pv = var_mod.product_variance(budget, actuals)
    for p in pv.index:
        rev_var = pv.loc[p, "Rev Var"]
        expected = "Favorable" if rev_var > 0 else ("Unfavorable" if rev_var < 0 else "On Plan")
        assert pv.loc[p, "Rev Flag"] == expected

    ov = var_mod.opex_variance(budget, actuals)
    for c in ov.index:
        var = ov.loc[c, "Opex Var"]
        expected = "Favorable" if var < 0 else ("Unfavorable" if var > 0 else "On Plan")
        assert ov.loc[c, "Flag"] == expected


# ---------------------------------------------------------------------------
# 4. Determinism: same seed => identical numbers.
# ---------------------------------------------------------------------------
def test_determinism():
    b1, a1 = _data(seed=42)
    b2, a2 = _data(seed=42)
    assert a1["products"]["revenue"].sum() == a2["products"]["revenue"].sum()


# Standalone runner so the file works even without pytest installed.
if __name__ == "__main__":
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
