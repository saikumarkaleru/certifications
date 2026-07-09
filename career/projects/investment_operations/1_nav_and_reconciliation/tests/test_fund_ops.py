"""Unit tests for the fund_ops package.

Runnable two ways:
    python -m pytest tests/ -q
    python tests/test_fund_ops.py    (falls back to running the asserts directly)

Everything runs on small in-memory frames, so the suite is fully offline and
deterministic.
"""

from __future__ import annotations

import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))

from fund_ops import pricing, nav, reconciliation, kyc  # noqa: E402

VDATE = pd.Timestamp("2026-07-08")


# --------------------------------------------------------------------------
# Pricing
# --------------------------------------------------------------------------
def _pricing_fixture():
    positions = pd.DataFrame({
        "security_id": ["S1", "S2", "S3"],
        "ticker": ["AAA", "BBB", "CCC"],
        "asset_class": ["Equity", "Equity", "Bond"],
        "quantity": [100.0, 50.0, 200.0],
        "currency": ["USD", "USD", "USD"],
    })
    prices = pd.DataFrame({
        "security_id": ["S1", "S2"],           # S3 missing today
        "price_date": [pd.Timestamp("2026-07-08"), pd.Timestamp("2026-07-01")],  # S2 stale
        "price": [10.0, 20.0],
    })
    prior = pd.DataFrame({
        "security_id": ["S1", "S2", "S3"],
        "price_date": [pd.Timestamp("2026-07-07")] * 3,
        "price": [9.5, 19.0, 5.0],
    })
    return positions, prices, prior


def test_pricing_good_stale_and_fallback():
    positions, prices, prior = _pricing_fixture()
    val = pricing.price_positions(positions, prices, prior, VDATE)
    by = val.set_index("security_id")
    assert by.loc["S1", "price_source"] == "GOOD"
    assert by.loc["S2", "price_source"] == "STALE"       # 7 days old > 3
    assert by.loc["S3", "price_source"] == "FALLBACK_PRIOR"
    # market values: 100*10 + 50*20 + 200*5(fallback) = 1000 + 1000 + 1000
    assert abs(pricing.total_market_value(val) - 3000.0) < 1e-9
    assert len(pricing.pricing_exceptions(val)) == 2      # stale + fallback


def test_pricing_missing_values_at_zero():
    positions = pd.DataFrame({
        "security_id": ["S9"], "ticker": ["ZZZ"], "asset_class": ["Equity"],
        "quantity": [100.0], "currency": ["USD"],
    })
    empty = pd.DataFrame({"security_id": [], "price_date": [], "price": []})
    val = pricing.price_positions(positions, empty, empty, VDATE)
    assert val.iloc[0]["price_source"] == "MISSING"
    assert val.iloc[0]["market_value"] == 0.0


# --------------------------------------------------------------------------
# NAV
# --------------------------------------------------------------------------
def _fund(prior_nav=1.0):
    return {
        "fund_name": "Test Fund", "valuation_date": VDATE,
        "prior_valuation_date": pd.Timestamp("2026-07-07"), "base_currency": "USD",
        "units_outstanding": 1_000_000.0, "cash_balance": 100_000.0,
        "accrued_income": 10_000.0, "ter_annual": 0.0125, "fee_accrual_days": 30,
        "other_accrued_expenses": 2_000.0, "prior_nav_per_unit": prior_nav,
    }


def test_nav_waterfall_math():
    fund = _fund()
    res = nav.compute_nav(holdings_mv=890_000.0, fund=fund)
    # GAV = 890,000 + 100,000 + 10,000 = 1,000,000
    assert abs(res.gross_asset_value - 1_000_000.0) < 1e-6
    # mgmt fee = GAV * 0.0125 * 30/365
    exp_fee = 1_000_000.0 * 0.0125 * 30 / 365
    assert abs(res.management_fee_accrued - exp_fee) < 1e-6
    # NAV = GAV - fee - other
    assert abs(res.nav - (1_000_000.0 - exp_fee - 2_000.0)) < 1e-6
    # per unit
    assert abs(res.nav_per_unit - res.nav / 1_000_000.0) < 1e-12


def test_nav_move_flag():
    # NAV per unit will be ~0.9968; a low prior forces a >2% jump -> flagged.
    flagged = nav.compute_nav(890_000.0, _fund(prior_nav=0.90))
    assert flagged.move_flagged is True
    # A prior close to today's value stays within tolerance.
    calm = nav.compute_nav(890_000.0, _fund(prior_nav=0.9968))
    assert calm.move_flagged is False


# --------------------------------------------------------------------------
# Reconciliation — one assertion per break type
# --------------------------------------------------------------------------
def _trades():
    cols = ["trade_id", "trade_date", "settle_date", "security_id", "side",
            "quantity", "price", "net_amount", "counterparty"]
    book = pd.DataFrame([
        ["A1", VDATE, VDATE, "S1", "BUY", 100, 10.0, 1000.0, "CP"],   # matches
        ["A2", VDATE, VDATE, "S2", "BUY", 100, 10.0, 1000.0, "CP"],   # qty mismatch
        ["A3", VDATE, VDATE, "S3", "BUY", 100, 10.0, 1000.0, "CP"],   # amount mismatch
        ["A4", VDATE, VDATE, "S4", "BUY", 100, 10.0, 1000.0, "CP"],   # missing at cust
        ["A5", VDATE, VDATE, "S5", "BUY", 100, 10.0, 1000.0, "CP"],   # duplicate at cust
    ], columns=cols)
    cust = pd.DataFrame([
        ["A1", VDATE, VDATE, "S1", "BUY", 100, 10.0, 1000.0, "CP"],
        ["A2", VDATE, VDATE, "S2", "BUY", 150, 10.0, 1500.0, "CP"],   # qty differs
        ["A3", VDATE, VDATE, "S3", "BUY", 100, 11.0, 1100.0, "CP"],   # amount differs
        ["A5", VDATE, VDATE, "S5", "BUY", 100, 10.0, 1000.0, "CP"],
        ["A5", VDATE, VDATE, "S5", "BUY", 100, 10.0, 1000.0, "CP"],   # dup
        ["A9", VDATE, VDATE, "S9", "BUY", 100, 10.0, 1000.0, "CP"],   # orphan
    ], columns=cols)
    return book, cust


def test_reconcile_detects_each_break_type():
    book, cust = _trades()
    q = reconciliation.reconcile_trades(book, cust, VDATE)
    types = dict(zip(q["key"], q["break_type"]))
    assert types["A2"] == "QUANTITY_MISMATCH"
    assert types["A3"] == "PRICE_AMOUNT_MISMATCH"
    assert types["A4"] == "MISSING_AT_CUSTODIAN"
    assert types["A5"] == "DUPLICATE"
    assert types["A9"] == "ORPHAN_AT_CUSTODIAN"
    assert "A1" not in types            # matched rows are not on the queue
    assert len(q) == 5


def test_reconcile_matched_produces_empty_queue():
    book, _ = _trades()
    q = reconciliation.reconcile_trades(book.iloc[[0]], book.iloc[[0]], VDATE)
    assert q.empty


def test_cash_amount_mismatch_and_aging():
    cols = ["cash_id", "value_date", "currency", "amount", "cash_type", "reference"]
    old = pd.Timestamp("2026-06-30")   # 8 days before valuation -> "6-10d"
    book = pd.DataFrame([["B1", old, "USD", 500.0, "SETTLEMENT", "T1"]], columns=cols)
    cust = pd.DataFrame([["C1", old, "USD", 900.0, "SETTLEMENT", "T1"]], columns=cols)
    q = reconciliation.reconcile_cash(book, cust, VDATE)
    assert q.iloc[0]["break_type"] == "PRICE_AMOUNT_MISMATCH"
    assert abs(q.iloc[0]["difference"] - (-400.0)) < 1e-9
    assert q.iloc[0]["aging_bucket"] == "6-10d"


# --------------------------------------------------------------------------
# KYC / AML
# --------------------------------------------------------------------------
def _customers():
    cols = ["customer_id", "name", "country", "entity_type", "product",
            "pep_flag", "adverse_media", "account_age_months", "expected_monthly_volume"]
    return pd.DataFrame([
        ["K1", "Low Risk", "GB", "Individual", "Savings", 0, 0, 60, 5000],
        ["K2", "PEP", "GB", "Individual", "Savings", 1, 0, 60, 5000],     # override
        ["K3", "Sanctioned Geo", "IR", "Individual", "Brokerage", 0, 0, 60, 5000],  # override
        ["K4", "Med", "VN", "Company", "Derivatives", 0, 0, 24, 5000],    # medium
    ], columns=cols)


def test_kyc_low_risk_customer_is_cdd():
    scored = kyc.score_customers(_customers()).set_index("customer_id")
    assert scored.loc["K1", "risk_tier"] == "Low"
    assert scored.loc["K1", "diligence"] == "CDD"


def test_kyc_pep_and_sanctioned_force_edd_override():
    scored = kyc.score_customers(_customers()).set_index("customer_id")
    assert scored.loc["K2", "risk_tier"] == "High"
    assert scored.loc["K2", "edd_override"]
    assert scored.loc["K3", "risk_tier"] == "High"
    assert scored.loc["K3", "diligence"] == "EDD"


def test_kyc_medium_tier():
    scored = kyc.score_customers(_customers()).set_index("customer_id")
    assert scored.loc["K4", "risk_tier"] == "Medium"


def test_aml_rules_fire():
    cols = ["txn_id", "customer_id", "date", "amount", "direction",
            "channel", "counterparty_country"]
    d = pd.Timestamp("2026-07-01")
    txns = pd.DataFrame([
        ["X1", "C1", d, 15000.0, "IN", "WIRE", "US"],                  # large value
        ["X2", "C2", d, 9000.0, "IN", "CASH", "US"],                   # structuring x3
        ["X3", "C2", d + pd.Timedelta(days=1), 9100.0, "IN", "CASH", "US"],
        ["X4", "C2", d + pd.Timedelta(days=2), 9200.0, "IN", "CASH", "US"],
        ["X5", "C3", d, 100000.0, "IN", "WIRE", "US"],                 # rapid in
        ["X6", "C3", d + pd.Timedelta(days=1), 95000.0, "OUT", "WIRE", "US"],  # rapid out
        ["X7", "C4", d, 5000.0, "IN", "WIRE", "IR"],                   # high-risk cp
    ], columns=cols)
    alerts = kyc.monitor_transactions(txns)
    rules = set(zip(alerts["customer_id"], alerts["rule"]))
    assert ("C1", "LARGE_VALUE") in rules
    assert ("C2", "STRUCTURING") in rules
    assert ("C3", "RAPID_MOVEMENT") in rules
    assert ("C4", "HIGH_RISK_COUNTERPARTY") in rules


# --------------------------------------------------------------------------
# Manual runner
# --------------------------------------------------------------------------
if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS  {fn.__name__}")
    print(f"\n{len(fns)} tests passed.")
