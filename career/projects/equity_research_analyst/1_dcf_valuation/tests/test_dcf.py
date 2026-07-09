"""
Unit tests for the DCF toolkit. Run:  python -m pytest -q   (or python -m unittest)

We test the two things an interviewer would poke at:
  * the present-value / discounting maths,
  * the Gordon terminal-value formula,
plus FCFF derivation, WACC blending and the reverse-DCF round-trip.
"""

import os
import sys
import math
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "src"))

from dcf import fcff, wacc as wacc_mod, model  # noqa: E402


class TestPresentValue(unittest.TestCase):
    def test_discount_factor(self):
        # A dollar in year 1 at 10% is worth 1/1.1 today.
        res = model.run_dcf(base_fcff=100.0, start_growth=0.0,
                            terminal_growth=0.0, wacc=0.10, net_debt=0.0,
                            shares=1.0, years=1)
        self.assertAlmostEqual(res["discount_factors"][0], 1 / 1.1, places=6)
        # projected FCFF grows 0% -> stays 100; PV = 100/1.1
        self.assertAlmostEqual(res["pv_fcff"][0], 100 / 1.1, places=6)

    def test_pv_sums_correctly(self):
        # Flat FCFF of 100 for 3 years at 10%: PV = 100(1/1.1 + 1/1.1^2 + 1/1.1^3)
        res = model.run_dcf(100.0, 0.0, 0.0, 0.10, 0.0, 1.0, years=3,
                            base_ebitda=None, exit_multiple=None)
        expected = sum(100 / 1.1 ** t for t in (1, 2, 3))
        self.assertAlmostEqual(res["pv_explicit"], expected, places=6)


class TestTerminalValue(unittest.TestCase):
    def test_gordon_formula(self):
        # TV = FCFF_N*(1+g)/(WACC-g). With flat FCFF=100, N=1, g=2%, WACC=10%.
        res = model.run_dcf(100.0, 0.0, 0.02, 0.10, 0.0, 1.0, years=1)
        expected_tv = 100 * 1.02 / (0.10 - 0.02)
        self.assertAlmostEqual(res["tv_gordon"], expected_tv, places=4)

    def test_terminal_growth_above_wacc_raises(self):
        with self.assertRaises(ValueError):
            model.run_dcf(100.0, 0.0, 0.12, 0.10, 0.0, 1.0, years=1)

    def test_exit_multiple_blend(self):
        # With a 50/50 blend the terminal value sits between the two methods.
        res = model.run_dcf(100.0, 0.0, 0.02, 0.10, 0.0, 1.0, years=1,
                            base_ebitda=200.0, exit_multiple=8.0,
                            terminal_weight_gordon=0.5)
        tv_g = 100 * 1.02 / 0.08
        tv_e = 8.0 * 200.0 * 1.0   # growth factor = 1 in year 1 with g feeding
        # exit uses projected terminal EBITDA = base_ebitda * growth_factor
        self.assertTrue(min(tv_g, tv_e) <= res["terminal_value"] <= max(tv_g, tv_e))


class TestFcff(unittest.TestCase):
    def test_fcff_buildup(self):
        year = {
            "year": "T", "ebit": 1000.0, "tax_rate": 0.20,
            "dep_amort": 100.0, "capex": -150.0, "change_in_wc": -50.0,
            "operating_cash_flow": None, "interest_expense": None,
        }
        out = fcff.fcff_from_year(year)
        # NOPAT = 1000*0.8 = 800; FCFF = 800 + 100 - 150 - 50 = 700
        self.assertAlmostEqual(out["nopat"], 800.0)
        self.assertAlmostEqual(out["fcff"], 700.0)

    def test_tax_rate_clamped(self):
        year = {"ebit": 100.0, "tax_rate": 0.99}  # absurd -> default
        out = fcff.fcff_from_year(year)
        self.assertLessEqual(out["tax_rate"], 0.5)


class TestWacc(unittest.TestCase):
    def test_capm_cost_of_equity(self):
        ke = wacc_mod.cost_of_equity(risk_free=0.04, beta=1.2, erp=0.05)
        self.assertAlmostEqual(ke, 0.04 + 1.2 * 0.05, places=6)

    def test_wacc_blend(self):
        company = {
            "price": 10.0, "shares": 100.0, "total_debt": 500.0,
            "risk_free_rate": 0.04, "beta": 1.0,
            "history": [{"tax_rate": 0.25, "interest_expense": 25.0}],
        }
        w = wacc_mod.estimate_wacc(company)
        # E = 1000, D = 500, V = 1500
        self.assertAlmostEqual(w["weight_equity"], 1000 / 1500, places=6)
        self.assertAlmostEqual(w["weight_debt"], 500 / 1500, places=6)
        # WACC must lie between after-tax Kd and Ke
        self.assertTrue(min(w["cost_of_debt_after_tax"], w["cost_of_equity"])
                        <= w["wacc"] <=
                        max(w["cost_of_debt_after_tax"], w["cost_of_equity"]))


class TestReverseDcf(unittest.TestCase):
    def test_round_trip(self):
        # Value the company at a known growth, then reverse-solve for it.
        g_true = 0.10
        res = model.run_dcf(100.0, g_true, 0.02, 0.10, 200.0, 50.0, years=5,
                            base_ebitda=None, exit_multiple=None)
        price = res["value_per_share"]
        rev = model.reverse_dcf(price, 100.0, 0.02, 0.10, 200.0, 50.0, years=5)
        self.assertIsNotNone(rev["implied_growth"])
        self.assertAlmostEqual(rev["implied_growth"], g_true, places=2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
