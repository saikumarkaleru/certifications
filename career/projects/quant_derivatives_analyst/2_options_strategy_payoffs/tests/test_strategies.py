"""
test_strategies.py -- Unit tests for the options toolkit.

Run either way:
    pytest tests/test_strategies.py
    python tests/test_strategies.py     (falls back to a tiny runner at the bottom)

Coverage:
    * Leg payoff math (long call, short put) at expiry.
    * Breakeven correctness for a known bull call spread.
    * Put-call parity: a synthetic long stock (long call + short put, same strike)
      reproduces the actual long-stock payoff (proved cleanly with r=q=0).
    * BSM sanity: price >= intrinsic; put-call parity relationship.
"""

from __future__ import annotations

import os
import sys

import numpy as np

# Make the project importable when run directly as a script.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from src.strategies import bsm
from src.strategies.legs import Leg, Position


# ---------------------------------------------------------------------------
# Leg payoff math
# ---------------------------------------------------------------------------
def test_long_call_payoff():
    """Long call K=100 paid 5: loses the premium below K, +1 slope above K."""
    leg = Leg("call", +1, strike=100.0, premium=5.0)
    # Below strike: worthless intrinsic, lose the 5 premium.
    assert np.isclose(leg.payoff_at_expiry(90.0), -5.0)
    # At strike: still -5.
    assert np.isclose(leg.payoff_at_expiry(100.0), -5.0)
    # Above: intrinsic 15 - premium 5 = +10 at S=115.
    assert np.isclose(leg.payoff_at_expiry(115.0), 10.0)


def test_short_put_payoff():
    """Short put K=100 collected 4: keep credit above K, lose below (net)."""
    leg = Leg("put", -1, strike=100.0, premium=4.0)
    # Above strike: put expires worthless, keep the +4 credit.
    assert np.isclose(leg.payoff_at_expiry(110.0), 4.0)
    # Well below: intrinsic -20 (assigned) + 4 credit = -16 at S=80.
    assert np.isclose(leg.payoff_at_expiry(80.0), -16.0)
    # Breakeven should be at 96 (K - credit).
    assert np.isclose(leg.payoff_at_expiry(96.0), 0.0)


def test_short_call_collects_credit():
    """A short position must ADD the premium as a credit (sign check)."""
    leg = Leg("call", -1, strike=100.0, premium=6.0)
    # entry_cashflow is +6 (we received money).
    assert np.isclose(leg.entry_cashflow(), 6.0)
    # Far above strike: -40 intrinsic + 6 credit = -34 at S=140.
    assert np.isclose(leg.payoff_at_expiry(140.0), -34.0)


# ---------------------------------------------------------------------------
# Breakeven for a known spread
# ---------------------------------------------------------------------------
def test_bull_call_spread_breakeven():
    """
    Buy 100 call @3, sell 110 call @1  => net debit 2.
    Breakeven = lower strike + net debit = 102.
    Max profit = width - debit = 10 - 2 = 8; max loss = -2.
    """
    pos = Position([
        Leg("call", +1, 100.0, 3.0),
        Leg("call", -1, 110.0, 1.0),
    ])
    bes = pos.breakevens(S_ref=100.0)
    assert len(bes) == 1
    assert abs(bes[0] - 102.0) < 0.05

    stats = pos.max_profit_loss(S_ref=100.0)
    assert abs(stats["max_profit"] - 8.0) < 0.05
    assert abs(stats["max_loss"] - (-2.0)) < 0.05
    assert not stats["loss_unbounded"]
    assert not stats["profit_unbounded"]
    # Net debit => negative cashflow of -2.
    assert np.isclose(pos.net_debit_credit(), -2.0)


# ---------------------------------------------------------------------------
# Put-call parity: synthetic long stock
# ---------------------------------------------------------------------------
def test_synthetic_long_stock_parity():
    """
    Long call + short put at the SAME strike = synthetic long forward.
    Intrinsic (before premiums) is exactly S - K for every spot.

    With r = q = 0 the BSM call/put premiums satisfy c - p = S0 - K, so the
    synthetic's TOTAL P&L equals an actual long-stock P&L (S - S0). We verify
    that across a grid of spots.
    """
    S0, K, T, r, sigma, q = 100.0, 100.0, 0.5, 0.0, 0.30, 0.0
    c = bsm.price_call(S0, K, T, r, sigma, q)
    p = bsm.price_put(S0, K, T, r, sigma, q)

    synthetic = Position([
        Leg("call", +1, K, c),
        Leg("put", -1, K, p),
    ])
    stock = Position([Leg("stock", +1, 0.0, S0)])

    grid = np.linspace(60, 140, 17)
    assert np.allclose(synthetic.payoff_at_expiry(grid),
                       stock.payoff_at_expiry(grid), atol=1e-6)

    # And the raw intrinsic (ignore premiums) must be exactly S - K.
    raw = (Leg("call", +1, K).intrinsic(grid) - Leg("put", +1, K).intrinsic(grid))
    assert np.allclose(raw, grid - K, atol=1e-9)


# ---------------------------------------------------------------------------
# BSM sanity checks
# ---------------------------------------------------------------------------
def test_bsm_price_above_intrinsic_and_parity():
    """Option value >= intrinsic, and put-call parity holds numerically."""
    S, K, T, r, sigma, q = 105.0, 100.0, 0.75, 0.03, 0.25, 0.01
    c = bsm.price_call(S, K, T, r, sigma, q)
    p = bsm.price_put(S, K, T, r, sigma, q)
    assert c >= max(S - K, 0) - 1e-9
    assert p >= max(K - S, 0) - 1e-9
    # Parity: c - p = S e^{-qT} - K e^{-rT}.
    import math
    lhs = c - p
    rhs = S * math.exp(-q * T) - K * math.exp(-r * T)
    assert abs(lhs - rhs) < 1e-6


def test_bsm_expiry_limits_to_intrinsic():
    """At T=0 the model returns intrinsic value and zero time-Greeks."""
    assert np.isclose(bsm.price_call(110, 100, 0.0, 0.05, 0.2, 0.0), 10.0)
    assert np.isclose(bsm.price_put(90, 100, 0.0, 0.05, 0.2, 0.0), 10.0)
    g = bsm.greeks(110, 100, 0.0, 0.05, 0.2, 0.0, kind="call")
    assert g.gamma == 0.0 and g.vega == 0.0 and g.theta == 0.0
    assert g.delta == 1.0  # in-the-money call at expiry


def test_net_greeks_sum_of_legs():
    """Net delta of long call + long put (straddle) should be near 0 at ATM."""
    S, K, T, r, sigma, q = 100.0, 100.0, 0.5, 0.02, 0.25, 0.0
    straddle = Position([
        Leg("call", +1, K, bsm.price_call(S, K, T, r, sigma, q)),
        Leg("put", +1, K, bsm.price_put(S, K, T, r, sigma, q)),
    ])
    g = straddle.net_greeks(S, T, r, sigma, q)
    assert abs(g.delta) < 0.15      # roughly delta-neutral at the money
    assert g.gamma > 0 and g.vega > 0  # long options => long gamma & vega


# ---------------------------------------------------------------------------
# Minimal runner so `python tests/test_strategies.py` works without pytest.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for t in tests:
        t()
        print(f"PASS  {t.__name__}")
        passed += 1
    print(f"\n{passed}/{len(tests)} tests passed.")
