"""
test_pricer.py  --  unit tests for the pricer package
=====================================================

Runs two ways:
    python -m pytest tests/test_pricer.py        (if pytest is installed)
    python tests/test_pricer.py                  (plain asserts, no pytest needed)

The asserts live inside test_* functions so pytest can collect them, and the
__main__ block at the bottom runs them all with a friendly PASS/FAIL summary.

WHAT WE PROVE:
  * Put-call parity holds (model-free identity).
  * BSM == CRR tree == Monte-Carlo, within tolerance (three roads, one price).
  * Implied-vol round-trip recovers the sigma we priced with (~1e-6).
  * Analytic Greeks match finite differences (calculus is correct).
  * American put >= European put (early-exercise premium is non-negative).
"""

import os
import sys
import math

# Make the src/ package importable no matter where pytest is launched from.
_HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(_HERE, "..", "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from pricer import (bs_price, put_call_parity_gap, crr_price, mc_price,
                    implied_vol, validate_greeks)

# A representative, slightly off-ATM contract with a non-zero dividend yield so
# the q terms are actually exercised by the tests.
S, K, T, r, sigma, q = 100.0, 105.0, 0.75, 0.04, 0.25, 0.02


def test_put_call_parity():
    """C - P must equal S*e^(-qT) - K*e^(-rT) exactly (model-free)."""
    c = bs_price(S, K, T, r, sigma, "call", q)
    p = bs_price(S, K, T, r, sigma, "put", q)
    assert abs((c - p) - put_call_parity_gap(S, K, T, r, q)) < 1e-10


def test_bsm_vs_tree():
    """CRR European price converges to Black-Scholes for large N."""
    for opt in ("call", "put"):
        bsm = bs_price(S, K, T, r, sigma, opt, q)
        tree = crr_price(S, K, T, r, sigma, opt, q, N=2000, american=False)
        assert abs(bsm - tree) < 1e-2, f"{opt}: BSM {bsm} vs tree {tree}"


def test_bsm_vs_monte_carlo():
    """BSM price sits within a few standard errors of the MC estimate."""
    for opt in ("call", "put"):
        bsm = bs_price(S, K, T, r, sigma, opt, q)
        mc, se = mc_price(S, K, T, r, sigma, opt, q,
                          n_paths=400_000, seed=42)
        assert abs(bsm - mc) < 4 * se + 1e-3, f"{opt}: BSM {bsm} vs MC {mc}+/-{se}"


def test_implied_vol_roundtrip():
    """Price with a known sigma, then recover it from the price."""
    for opt in ("call", "put"):
        px = bs_price(S, K, T, r, sigma, opt, q)
        iv = implied_vol(px, S, K, T, r, opt, q)
        assert abs(iv - sigma) < 1e-6, f"{opt}: recovered {iv} vs true {sigma}"


def test_greeks_vs_finite_diff():
    """Every analytic Greek matches its finite-difference estimate."""
    for opt in ("call", "put"):
        df = validate_greeks(S, K, T, r, sigma, opt, q)
        assert df["AbsError"].max() < 1e-3, f"{opt}: {df}"


def test_american_premium_nonneg():
    """An American put is worth at least its European twin (early exercise)."""
    eu = crr_price(S, K, T, r, sigma, "put", q, N=800, american=False)
    am = crr_price(S, K, T, r, sigma, "put", q, N=800, american=True)
    assert am >= eu - 1e-9, f"American put {am} < European {eu}"
    # With these in-the-money-ish inputs the premium should be strictly positive.
    assert am > eu, "expected a positive early-exercise premium"


def _run_all():
    """Plain-python runner so `python tests/test_pricer.py` works without pytest."""
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    passed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}")
        except Exception as e:
            print(f"  ERROR {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(tests)} tests passed.")
    return passed == len(tests)


if __name__ == "__main__":
    print("Running pricer unit tests...\n")
    ok = _run_all()
    sys.exit(0 if ok else 1)
