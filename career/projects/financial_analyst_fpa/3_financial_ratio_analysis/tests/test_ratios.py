"""
Tests for the ratio math and the DuPont / benchmark logic.

Design goals of these tests:
  * DuPont must RECONCILE -- the product of the drivers must equal ROE computed
    directly. This is the whole promise of the decomposition, so it is checked
    for both the 3-step and 5-step versions, on real/cached data.
  * Percentile ranks must always live in [0, 100].
  * A known ratio must compute to a known answer on tiny, hand-checkable inputs.
Run:  python -m pytest tests/ -q
"""

import os
import sys

import pandas as pd
import pytest

# Make src/ importable when pytest is run from the project root.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from ratios import data, ratios as ratio_mod, dupont, benchmark  # noqa: E402


# A tiny, hand-built company so we can check ratios by mental arithmetic.
def _toy_facts():
    """One year of clean, round numbers (year 2024).

    Revenue 1000, COGS 600 -> Gross Profit 400; Operating Income/EBIT 200;
    Interest 20 -> Pretax 180; Tax 36 -> Net Income 144.
    Assets 800, Equity 400 (so leverage 2x), Current Assets 300,
    Current Liab 150, Inventory 100, Cash 90, Receivables 100, Payables 60,
    Debt 200, Invested Capital 600, OCF 160, D&A 50.
    """
    fields = {
        "Revenue": 1000, "COGS": 600, "Gross Profit": 400,
        "Operating Income": 200, "EBIT": 200, "Pretax Income": 180,
        "Tax Provision": 36, "Net Income": 144, "Interest Expense": 20,
        "Total Assets": 800, "Current Assets": 300, "Current Liabilities": 150,
        "Total Liabilities": 400, "Equity": 400, "Cash": 90,
        "Receivables": 100, "Inventory": 100, "Net PPE": 300, "Payables": 60,
        "Total Debt": 200, "Invested Capital": 600,
        "Operating Cash Flow": 160, "Capital Expenditure": 40,
        "Free Cash Flow": 120, "D&A": 50,
    }
    return pd.DataFrame({2024: fields})


@pytest.fixture(scope="module")
def loaded():
    """Load whatever data is available (cache/live/fallback). Always succeeds."""
    facts_by_ticker, source = data.load_all()
    return facts_by_ticker, source


# --------------------------------------------------------------------------
# 1. Known ratio on toy inputs.
# --------------------------------------------------------------------------
def test_known_ratios_on_toy_inputs():
    r = ratio_mod.compute_ratios(_toy_facts())
    y = 2024
    # Gross margin = 400/1000 = 40%.
    assert r.at["Gross Margin %", y] == pytest.approx(40.0)
    # Net margin = 144/1000 = 14.4%.
    assert r.at["Net Margin %", y] == pytest.approx(14.4)
    # Current ratio = 300/150 = 2.0.
    assert r.at["Current Ratio", y] == pytest.approx(2.0)
    # Quick ratio = (300-100)/150 = 1.333... (ratios are rounded to 3 dp).
    assert r.at["Quick Ratio", y] == pytest.approx(200 / 150, abs=1e-3)
    # Debt/Equity = 200/400 = 0.5.
    assert r.at["Debt / Equity", y] == pytest.approx(0.5)
    # Interest coverage = EBIT/Interest = 200/20 = 10.
    assert r.at["Interest Coverage", y] == pytest.approx(10.0)


def test_divide_by_zero_is_nan_not_crash():
    """Inventory = 0 (like Google/Meta) must give NaN turnover, not an error."""
    facts = _toy_facts()
    facts.at["Inventory", 2024] = 0
    r = ratio_mod.compute_ratios(facts)
    assert pd.isna(r.at["Inventory Turnover", 2024])
    assert pd.isna(r.at["DIO (days)", 2024])


# --------------------------------------------------------------------------
# 2. DuPont reconciliation (the headline invariant).
# --------------------------------------------------------------------------
def test_dupont_3step_reconciles_toy():
    d = dupont.dupont_3step(_toy_facts(), 2024)
    assert d["Reconciliation diff"] == pytest.approx(0.0, abs=1e-9)
    # ROE = 144/400 = 36%.
    assert d["ROE (direct)"] == pytest.approx(0.36)


def test_dupont_5step_reconciles_toy():
    d = dupont.dupont_5step(_toy_facts(), 2024)
    assert d["Reconciliation diff"] == pytest.approx(0.0, abs=1e-9)


def test_dupont_reconciles_on_real_data(loaded):
    """3- and 5-step must reconcile for every company, every year."""
    facts_by_ticker, _ = loaded
    for tk, facts in facts_by_ticker.items():
        for year in facts.columns:
            eq = facts.at["Equity", year]
            if pd.isna(eq) or eq == 0:
                continue
            d3 = dupont.dupont_3step(facts, year)
            d5 = dupont.dupont_5step(facts, year)
            assert d3["Reconciliation diff"] == pytest.approx(0.0, abs=1e-6)
            assert d5["Reconciliation diff"] == pytest.approx(0.0, abs=1e-6)


# --------------------------------------------------------------------------
# 3. Percentile ranks must be in [0, 100].
# --------------------------------------------------------------------------
def test_percentile_ranks_in_range(loaded):
    facts_by_ticker, _ = loaded
    ranks = benchmark.percentile_ranks(facts_by_ticker, data.TARGET)
    vals = ranks.values.flatten()
    vals = vals[~pd.isna(vals)]
    assert (vals >= 0).all() and (vals <= 100).all()


def test_benchmark_summary_has_all_key_ratios(loaded):
    facts_by_ticker, _ = loaded
    bench = benchmark.benchmark_summary(facts_by_ticker, data.TARGET)
    assert list(bench["Ratio"]) == ratio_mod.KEY_RATIOS
