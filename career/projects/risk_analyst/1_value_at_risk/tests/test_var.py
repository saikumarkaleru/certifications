"""Unit tests for the var_engine package.

Runnable two ways:
    python -m pytest tests/ -q
    python tests/test_var.py        (falls back to running the asserts directly)

The tests use the synthetic data generator so they never touch the network.
"""

from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))

from var_engine import data, var_methods, backtest  # noqa: E402


def _fixture():
    prices = data._generate_synthetic(n_days=500, seed=7)
    returns = data.compute_returns(prices)
    port = data.portfolio_returns(returns, data.WEIGHTS)
    return returns, port


def test_norm_ppf_matches_known_quantiles():
    assert abs(var_methods.norm_ppf(0.05) - (-1.6448536)) < 1e-4
    assert abs(var_methods.norm_ppf(0.01) - (-2.3263479)) < 1e-4
    assert abs(var_methods.norm_ppf(0.5)) < 1e-9


def test_parametric_equals_textbook_at_95():
    # VaR = -(mu - 1.645*sigma) at 95%.
    returns, _ = _fixture()
    mu_p, sigma_p, _, _ = var_methods.portfolio_moments(returns, data.WEIGHTS)
    got = var_methods.parametric_var(mu_p, sigma_p, 0.95)
    textbook = -(mu_p - 1.6448536 * sigma_p)
    assert abs(got - textbook) < 1e-6


def test_parametric_vs_historical_sanity():
    returns, port = _fixture()
    mu_p, sigma_p, _, _ = var_methods.portfolio_moments(returns, data.WEIGHTS)
    p_var = var_methods.parametric_var(mu_p, sigma_p, 0.95)
    h_var = var_methods.historical_var(port, 0.95)
    assert p_var > 0 and h_var > 0
    # Same order of magnitude (within a factor of 2).
    assert 0.5 < p_var / h_var < 2.0


def test_component_var_sums_to_total():
    returns, _ = _fixture()
    comp = var_methods.component_var(returns, data.WEIGHTS, 0.95, data.TICKERS)
    mu_p, sigma_p, _, _ = var_methods.portfolio_moments(returns, data.WEIGHTS)
    # Component VaR uses z*sigma (zero-mean); compare against the same construction.
    z = var_methods.norm_ppf(0.95)
    total_zero_mean = z * sigma_p
    assert abs(comp["component_var"].sum() - total_zero_mean) < 1e-8
    assert abs(comp["pct_contribution"].sum() - 1.0) < 1e-8


def test_monte_carlo_close_to_parametric():
    returns, _ = _fixture()
    mu_p, sigma_p, mean_vec, cov = var_methods.portfolio_moments(returns, data.WEIGHTS)
    p_var = var_methods.parametric_var(mu_p, sigma_p, 0.99)
    mc_var, _ = var_methods.monte_carlo_var(mean_vec, cov, data.WEIGHTS, 0.99)
    # Both are normal-based; MC should be within 5% relative of parametric.
    assert abs(mc_var - p_var) / p_var < 0.05


def test_expected_shortfall_exceeds_var():
    returns, port = _fixture()
    mu_p, sigma_p, _, _ = var_methods.portfolio_moments(returns, data.WEIGHTS)
    assert var_methods.parametric_es(mu_p, sigma_p, 0.95) > var_methods.parametric_var(mu_p, sigma_p, 0.95)
    assert var_methods.historical_es(port, 0.95) > var_methods.historical_var(port, 0.95)


def test_chi2_sf_reasonable():
    # chi2, 1 df: P(X > 3.841) ~= 0.05.
    assert abs(backtest.chi2_sf(3.841, 1) - 0.05) < 0.01
    # chi2, 2 df: P(X > 5.991) ~= 0.05.
    assert abs(backtest.chi2_sf(5.991, 2) - 0.05) < 0.01


def test_backtest_runs_and_counts():
    _, port = _fixture()
    bt = backtest.run_backtest(port, window=250, conf=0.95)
    assert bt.n_obs > 0
    assert 0 <= bt.n_exceptions <= bt.n_obs
    assert bt.verdict() in ("PASS", "FAIL")


def _run_all():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    for fn in fns:
        fn()
        print(f"  PASS  {fn.__name__}")
        passed += 1
    print(f"\n{passed}/{len(fns)} tests passed.")


if __name__ == "__main__":
    _run_all()
