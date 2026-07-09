"""
Tests for the credit toolkit.

Design goals:
  * A tiny hand-built borrower so every ratio, CFADS and DSCR can be checked by
    mental arithmetic against a known answer.
  * Rating band mapping is exact at the boundaries.
  * Scenarios move the metrics in the RIGHT DIRECTION and reconcile with the
    base case at zero shock.
  * The bundled data loads, validates and rates as expected (regression guard).
Run:  python -m pytest tests/ -q
"""

import os
import sys

import numpy as np
import pandas as pd
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from credit_spread import (  # noqa: E402
    data, ratios, serviceability as svc, rating, scenario,
)


# --- a tiny, hand-checkable borrower (one year, round numbers) --------------
def _toy_facts():
    """FY2024. Revenue 1000, COGS 600, Opex 150 -> EBITDA 250; D&A 50 ->
    EBIT 200; Interest 40 -> PBT 160; Tax 40 (25%) -> NI 120.
    Cash 100, Debt 500 (ST 100 + LT 400), Equity 500.
    Current Assets 400, Current Liab 200, Inventory 120, AR 150, AP 90.
    Capex 100 (maint 40% = 40), Principal due 60.
    """
    f = {
        "Revenue": 1000, "COGS": 600, "Operating Expenses": 150, "EBITDA": 250,
        "Depreciation & Amortization": 50, "EBIT": 200, "Interest Expense": 40,
        "PBT": 160, "Tax": 40, "Net Income": 120,
        "Cash & Equivalents": 100, "Accounts Receivable": 150, "Inventory": 120,
        "Current Assets": 400, "Net PPE": 600, "Total Assets": 1000,
        "Accounts Payable": 90, "Short-term Debt": 100, "Current Liabilities": 200,
        "Long-term Debt": 400, "Total Debt": 500, "Total Liabilities": 500,
        "Total Equity": 500, "Operating Cash Flow": 220, "Capex": 100,
        "Free Cash Flow": 120, "Scheduled Principal Repayment": 60,
    }
    return pd.DataFrame({2024: pd.Series(f)})


# --------------------------- ratio math -------------------------------------
def test_leverage_ratios():
    r = ratios.compute_year(_toy_facts(), 2024)
    assert r["Debt/EBITDA (x)"] == pytest.approx(500 / 250)          # 2.0
    assert r["Net Debt/EBITDA (x)"] == pytest.approx((500 - 100) / 250)  # 1.6
    assert r["Debt/Equity (x)"] == pytest.approx(1.0)
    assert r["Gearing (%)"] == pytest.approx(50.0)                   # 500/1000


def test_coverage_and_margins():
    r = ratios.compute_year(_toy_facts(), 2024)
    assert r["Interest Coverage (x)"] == pytest.approx(200 / 40)     # 5.0
    assert r["EBITDA Interest Cover (x)"] == pytest.approx(250 / 40)  # 6.25
    assert r["EBITDA Margin (%)"] == pytest.approx(25.0)
    assert r["ROCE (%)"] == pytest.approx(100 * 200 / (1000 - 200))  # 25%


def test_working_capital_cycle():
    r = ratios.compute_year(_toy_facts(), 2024)
    dso = 365 * 150 / 1000
    dio = 365 * 120 / 600
    dpo = 365 * 90 / 600
    assert r["DSO (days)"] == pytest.approx(dso)
    assert r["Cash Conversion Cycle (days)"] == pytest.approx(dso + dio - dpo)


def test_safe_division_returns_nan():
    assert np.isnan(ratios._safe(10, 0))
    assert np.isnan(ratios._safe(10, None))


# --------------------------- serviceability ---------------------------------
def test_cfads_and_dscr():
    f = _toy_facts()
    # CFADS = EBITDA 250 - tax 40 - maint capex (40% of 100 = 40) = 170
    assert svc.cfads(f, 2024) == pytest.approx(170.0)
    # Debt service = interest 40 + principal 60 = 100 -> DSCR = 1.70
    assert svc.debt_service(f, 2024) == pytest.approx(100.0)
    assert svc.dscr(f, 2024) == pytest.approx(1.70)


def test_icr_and_headroom():
    f = _toy_facts()
    assert svc.icr(f, 2024) == pytest.approx(200 / 40)   # EBIT/interest = 5.0
    assert svc.headroom_class(1.70) == "Comfortable"
    assert svc.headroom_class(1.30) == "Adequate"
    assert svc.headroom_class(1.05) == "Thin"
    assert svc.headroom_class(0.80) == "Shortfall"


# --------------------------- rating scorecard -------------------------------
def test_band_from_score_boundaries():
    assert rating.band_from_score(90) == "AAA"
    assert rating.band_from_score(89.9) == "AA"
    assert rating.band_from_score(64) == "BBB"
    assert rating.band_from_score(17.9) == "D"


def test_weights_sum_correctly():
    assert abs(sum(rating.FINANCIAL_WEIGHTS.values()) - 0.65) < 1e-9
    assert abs(sum(rating.BUSINESS_WEIGHTS.values()) - 0.35) < 1e-9


def test_scorecard_composite_matches_manual():
    f = _toy_facts()
    biz = {"MarketPosition": 4, "Industry": 4, "Diversification": 3, "Management": 4}
    card = rating.scorecard(f, biz, 2024)
    # Recompute contribution sum independently.
    manual = (card["table"]["Weight"] * card["table"]["Sub-score"]).sum()
    assert card["composite"] == pytest.approx(manual)
    assert 0 <= card["composite"] <= 100
    assert card["band"] in rating.PD_BY_BAND


# --------------------------- scenarios --------------------------------------
def test_base_scenario_matches_unstressed():
    f = _toy_facts()
    biz = {"MarketPosition": 3, "Industry": 3, "Diversification": 3, "Management": 3}
    base = scenario.recompute(f, biz, yr=2024)          # no shock
    assert base["DSCR (x)"] == pytest.approx(svc.dscr(f, 2024))
    assert base["Net Debt/EBITDA (x)"] == pytest.approx(
        ratios.compute_year(f, 2024)["Net Debt/EBITDA (x)"])


def test_ebitda_haircut_worsens_credit():
    f = _toy_facts()
    biz = {"MarketPosition": 3, "Industry": 3, "Diversification": 3, "Management": 3}
    base = scenario.recompute(f, biz, yr=2024)
    down = scenario.recompute(f, biz, yr=2024, ebitda_mult=0.70)
    assert down["EBITDA"] < base["EBITDA"]
    assert down["DSCR (x)"] < base["DSCR (x)"]
    assert down["Net Debt/EBITDA (x)"] > base["Net Debt/EBITDA (x)"]
    assert down["Composite"] <= base["Composite"]


def test_rate_shock_raises_leverage_neutral_but_cuts_dscr():
    f = _toy_facts()
    biz = {"MarketPosition": 3, "Industry": 3, "Diversification": 3, "Management": 3}
    base = scenario.recompute(f, biz, yr=2024)
    shocked = scenario.recompute(f, biz, yr=2024, interest_add_bps=200)
    # +200bps on 500 debt = +10 interest -> DSCR falls, leverage unchanged.
    assert shocked["DSCR (x)"] < base["DSCR (x)"]
    assert shocked["Net Debt/EBITDA (x)"] == pytest.approx(base["Net Debt/EBITDA (x)"])


# --------------------------- bundled data -----------------------------------
def test_bundled_data_loads_and_rates():
    facts, meta, business = data.load_all()
    assert set(facts) == {"AARTI", "SUNRISE", "DECCAN"}
    # The three borrowers were designed as strong / moderate / distressed.
    order = {c: rating.scorecard(facts[c], business[c])["composite"] for c in facts}
    assert order["AARTI"] > order["SUNRISE"] > order["DECCAN"]
    assert rating.scorecard(facts["AARTI"], business["AARTI"])["band"] in {"AAA", "AA", "A"}
    assert rating.scorecard(facts["DECCAN"], business["DECCAN"])["band"] in {"CCC", "CC", "C", "D"}
