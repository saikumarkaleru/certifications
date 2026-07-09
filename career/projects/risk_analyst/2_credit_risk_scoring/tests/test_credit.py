"""Unit tests for the credit risk models.

Runnable two ways:
    pytest tests/test_credit.py
    python tests/test_credit.py     (falls back to plain asserts)

Covers: Altman ratio/Z math against a hand-computed value; Merton solver
sanity (PD in [0,1], DD finite, converges) and a leverage-monotonicity check
(more debt -> higher PD).
"""

import math
import os
import sys

import pandas as pd

# Make src/ importable regardless of the working directory.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from credit import altman, merton, portfolio  # noqa: E402


# =========================================================================
# Altman
# =========================================================================
def test_altman_z_math():
    """Hand-computed Z from known ratios matches the weighted sum."""
    x = dict(x1=0.20, x2=0.30, x3=0.15, x4=2.00, x5=1.10)
    # 1.2*.2 + 1.4*.3 + 3.3*.15 + 0.6*2 + 1.0*1.1
    expected = 0.24 + 0.42 + 0.495 + 1.20 + 1.10   # = 3.455
    z = altman.z_score(**x)
    assert abs(z - expected) < 1e-9
    assert altman.classify_zone(z) == "Safe"


def test_altman_ratios_from_inputs():
    """compute_altman derives the ratios correctly from raw inputs."""
    row = {
        "total_assets": 1000.0, "current_assets": 400.0,
        "current_liabilities": 100.0, "retained_earnings": 300.0,
        "total_liabilities": 500.0, "long_term_debt": 200.0,
        "revenue": 1200.0, "ebit": 150.0, "market_cap": 2000.0,
        "equity_vol": 0.3,
    }
    frame = pd.DataFrame({"CO": row}).T
    out = altman.compute_altman(frame)
    r = out.loc["CO"]
    assert abs(r["X1"] - 0.30) < 1e-9   # (400-100)/1000
    assert abs(r["X2"] - 0.30) < 1e-9
    assert abs(r["X3"] - 0.15) < 1e-9
    assert abs(r["X4"] - 4.00) < 1e-9   # 2000/500
    assert abs(r["X5"] - 1.20) < 1e-9
    # Z = 1.2*.3+1.4*.3+3.3*.15+0.6*4+1.0*1.2 = 0.36+0.42+0.495+2.4+1.2 = 4.875
    assert abs(r["Z"] - 4.875) < 1e-9
    assert r["Zone"] == "Safe"


def test_altman_zones():
    assert altman.classify_zone(3.5) == "Safe"
    assert altman.classify_zone(2.5) == "Grey"
    assert altman.classify_zone(1.0) == "Distress"
    assert altman.classify_zone(float("nan")) == "N/A"


# =========================================================================
# Merton
# =========================================================================
def test_norm_cdf():
    assert abs(merton.norm_cdf(0.0) - 0.5) < 1e-12
    assert merton.norm_cdf(5.0) > 0.999999
    assert merton.norm_cdf(-5.0) < 1e-6


def test_merton_solver_sane():
    """Solver returns a valid PD, finite DD, and converges on good inputs."""
    res = merton.solve_merton(equity=2000.0, equity_vol=0.30,
                              default_point=500.0, r=0.04, t=1.0)
    assert res["converged"] is True
    assert 0.0 <= res["PD"] <= 1.0
    assert math.isfinite(res["DD"])
    assert res["asset_value"] > 0
    assert res["asset_vol"] > 0


def test_merton_leverage_monotonic():
    """Higher leverage (bigger debt barrier) => higher PD."""
    low = merton.solve_merton(2000.0, 0.30, 300.0)
    high = merton.solve_merton(2000.0, 0.30, 1800.0)
    assert low["PD"] < high["PD"]
    assert low["DD"] > high["DD"]        # farther from default when less levered


def test_merton_bad_inputs():
    """Degenerate inputs return NaN and a non-converged flag, not a crash."""
    res = merton.solve_merton(equity=float("nan"), equity_vol=0.3,
                              default_point=500.0)
    assert res["converged"] is False
    assert math.isnan(res["PD"])


# =========================================================================
# Portfolio
# =========================================================================
def test_expected_loss_identity():
    """EL = PD * LGD * EAD, summed across issuers."""
    merton_tbl = pd.DataFrame({
        "PD": [0.01, 0.05],
        "DD": [3.0, 1.5],
        "converged": [True, True],
    }, index=["A", "B"])
    el = portfolio.expected_loss(merton_tbl, lgd=0.45, ead=10_000_000.0)
    assert abs(el.loc["A", "EL"] - 0.01 * 0.45 * 10_000_000.0) < 1e-6
    summary = portfolio.portfolio_summary(el)
    assert abs(summary["total_ead"] - 20_000_000.0) < 1e-6
    expected_total = (0.01 + 0.05) * 0.45 * 10_000_000.0
    assert abs(summary["total_el"] - expected_total) < 1e-6


def _run_all():
    """Plain-python runner so the file works without pytest installed."""
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in tests:
        fn()
        print(f"  PASS  {fn.__name__}")
        passed += 1
    print(f"\n{passed}/{len(tests)} tests passed.")


if __name__ == "__main__":
    _run_all()
