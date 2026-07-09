"""
Unit tests for the comps toolkit. Run:  python -m pytest -q

We test the two things an interviewer would poke at:
  * the multiple calculations (P/E, EV/EBITDA, EV/Revenue, P/B, PEG),
  * the implied-value maths (equity vs enterprise multiples),
plus the peer summary, the z-score screen and the OLS regression.
"""

import os
import sys
import math
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "src"))

from comps import multiples, stats, valuation  # noqa: E402


def _mini_universe():
    """A tiny, hand-checkable universe: 1 target + 3 peers."""
    return {
        "target": "TGT",
        "companies": {
            "TGT": {"name": "Target", "price": 20.0, "shares": 100.0,
                    "market_cap": 2000.0, "total_debt": 500.0, "cash": 100.0,
                    "revenue": 1000.0, "ebitda": 250.0, "net_income": 120.0,
                    "book_equity": 800.0, "eps": 1.2, "rev_growth": 0.10,
                    "earn_growth": 0.10, "ebitda_margin": 0.25},
            "P1": {"name": "Peer1", "price": 30.0, "shares": 100.0,
                   "market_cap": 3000.0, "total_debt": 400.0, "cash": 200.0,
                   "revenue": 1200.0, "ebitda": 300.0, "net_income": 150.0,
                   "book_equity": 1000.0, "eps": 1.5, "rev_growth": 0.12,
                   "earn_growth": 0.12, "ebitda_margin": 0.25},
            "P2": {"name": "Peer2", "price": 40.0, "shares": 100.0,
                   "market_cap": 4000.0, "total_debt": 600.0, "cash": 100.0,
                   "revenue": 1500.0, "ebitda": 400.0, "net_income": 200.0,
                   "book_equity": 1200.0, "eps": 2.0, "rev_growth": 0.15,
                   "earn_growth": 0.15, "ebitda_margin": 0.27},
            "P3": {"name": "Peer3", "price": 25.0, "shares": 100.0,
                   "market_cap": 2500.0, "total_debt": 300.0, "cash": 300.0,
                   "revenue": 1100.0, "ebitda": 275.0, "net_income": 100.0,
                   "book_equity": 900.0, "eps": 1.0, "rev_growth": 0.08,
                   "earn_growth": 0.08, "ebitda_margin": 0.25},
        },
    }


class TestMultiples(unittest.TestCase):
    def test_enterprise_value(self):
        c = {"market_cap": 2000.0, "total_debt": 500.0, "cash": 100.0}
        # EV = 2000 + 500 - 100 = 2400
        self.assertAlmostEqual(multiples.enterprise_value(c), 2400.0)

    def test_pe(self):
        m = multiples.company_multiples(
            {"price": 20.0, "shares": 100.0, "market_cap": 2000.0,
             "eps": 2.0, "ebitda": 250.0, "revenue": 1000.0,
             "book_equity": 800.0, "total_debt": 0.0, "cash": 0.0,
             "earn_growth": 0.10})
        self.assertAlmostEqual(m["P/E"], 10.0)          # 20 / 2

    def test_ev_ebitda_and_revenue(self):
        c = {"price": 20.0, "shares": 100.0, "market_cap": 2000.0,
             "total_debt": 500.0, "cash": 100.0, "ebitda": 250.0,
             "revenue": 1000.0, "book_equity": 800.0, "eps": 2.0,
             "earn_growth": 0.10}
        m = multiples.company_multiples(c)
        # EV = 2400 -> EV/EBITDA = 2400/250 = 9.6 ; EV/Revenue = 2.4
        self.assertAlmostEqual(m["EV/EBITDA"], 9.6)
        self.assertAlmostEqual(m["EV/Revenue"], 2.4)

    def test_pb_and_peg(self):
        c = {"price": 20.0, "shares": 100.0, "market_cap": 2000.0,
             "total_debt": 0.0, "cash": 0.0, "ebitda": 250.0, "revenue": 1000.0,
             "book_equity": 800.0, "eps": 2.0, "earn_growth": 0.20}
        m = multiples.company_multiples(c)
        # BVPS = 800/100 = 8 -> P/B = 20/8 = 2.5
        self.assertAlmostEqual(m["P/B"], 2.5)
        # PEG = (P/E=10) / (growth% = 20) = 0.5
        self.assertAlmostEqual(m["PEG"], 0.5)

    def test_negative_denominator_is_nan(self):
        m = multiples.company_multiples(
            {"price": 20.0, "shares": 100.0, "market_cap": 2000.0,
             "eps": -1.0, "ebitda": 250.0, "revenue": 1000.0,
             "book_equity": 800.0, "total_debt": 0.0, "cash": 0.0,
             "earn_growth": 0.10})
        self.assertTrue(math.isnan(m["P/E"]))           # negative EPS -> NaN


class TestPeerSummary(unittest.TestCase):
    def test_median_excludes_target(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        summ = stats.peer_summary(df, u["target"])
        # peer P/E values: 30/1.5=20, 40/2=20, 25/1=25 -> median 20
        self.assertAlmostEqual(summ.loc["P/E", "Median"], 20.0)
        self.assertEqual(int(summ.loc["P/E", "N"]), 3)


class TestImpliedValuation(unittest.TestCase):
    def test_pe_implied_price(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        summ = stats.peer_summary(df, u["target"])
        implied, fb = valuation.implied_valuation(
            u, {"Median": summ["Median"], "Mean": summ["Mean"]})
        pe_row = implied[implied["Method"] == "P/E"].iloc[0]
        # implied P/E price = median P/E (20) * target EPS (1.2) = 24
        self.assertAlmostEqual(pe_row["Implied Price/Share"], 24.0, places=4)

    def test_ev_ebitda_implied_price(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        summ = stats.peer_summary(df, u["target"])
        implied, fb = valuation.implied_valuation(
            u, {"Median": summ["Median"], "Mean": summ["Mean"]})
        row = implied[implied["Method"] == "EV/EBITDA"].iloc[0]
        # peer EV/EBITDA: P1 (3000+400-200)/300=10.67, P2 (4000+600-100)/400=11.25,
        # P3 (2500+300-300)/275=9.09 -> median 10.67
        # implied EV = 10.667 * 250 = 2666.7 ; equity = 2666.7 - (500-100)=2266.7
        # price = 2266.7/100 = 22.67
        self.assertAlmostEqual(row["Implied Price/Share"], 22.67, places=1)

    def test_football_field_bounds(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        summ = stats.peer_summary(df, u["target"])
        implied, fb = valuation.implied_valuation(
            u, {"Median": summ["Median"], "Mean": summ["Mean"]})
        self.assertLessEqual(fb["low"], fb["median"])
        self.assertLessEqual(fb["median"], fb["high"])
        self.assertIn(fb["verdict"], ("UNDERVALUED", "OVERVALUED"))


class TestScreens(unittest.TestCase):
    def test_zscore_mean_zero(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        z = stats.zscore_screen(df, columns=("P/E",))
        # a z-score column has mean ~0 across the universe
        self.assertAlmostEqual(z["z(P/E)"].mean(), 0.0, places=6)

    def test_regression_runs(self):
        u = _mini_universe()
        df = multiples.build_multiples_table(u)
        res, coef, r2 = stats.regression_screen(df)
        self.assertEqual(len(res), len(df))            # a residual per name
        self.assertIn("intercept", coef)
        # residuals of an OLS fit sum to ~0
        self.assertAlmostEqual(res["residual"].sum(), 0.0, places=4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
