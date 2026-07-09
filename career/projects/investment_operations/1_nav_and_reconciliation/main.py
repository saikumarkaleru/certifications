"""Investment Operations & Fund Accounting tool - end-to-end pipeline.

Pipeline: load data -> price holdings -> strike NAV -> reconcile trades & cash
-> KYC risk-score customers + AML monitoring -> write Excel + charts -> print
a console summary.

Runs fully offline on the synthetic sample data in input/.

Run from this folder:  python main.py
"""

from __future__ import annotations

import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

from fund_ops import data, pricing, nav, reconciliation, kyc, reporting  # noqa: E402

INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # --- 1. Load ---
    fund = data.load_fund_static(INPUT_DIR)
    positions = data.load_positions(INPUT_DIR)
    prices = data.load_prices(INPUT_DIR, "prices.csv")
    prior_prices = data.load_prices(INPUT_DIR, "prior_prices.csv")
    book_trades = data.load_trades(INPUT_DIR, "book_trades.csv")
    cust_trades = data.load_trades(INPUT_DIR, "custodian_trades.csv")
    book_cash = data.load_cash(INPUT_DIR, "book_cash.csv")
    cust_cash = data.load_cash(INPUT_DIR, "custodian_cash.csv")
    customers = data.load_customers(INPUT_DIR)
    transactions = data.load_transactions(INPUT_DIR)

    # --- 2. Pricing + NAV ---
    valuation = pricing.price_positions(positions, prices, prior_prices, fund["valuation_date"])
    price_exc = pricing.pricing_exceptions(valuation)
    holdings_mv = pricing.total_market_value(valuation)
    nav_res = nav.compute_nav(holdings_mv, fund)

    # --- 3. Reconciliation ---
    trade_breaks = reconciliation.reconcile_trades(book_trades, cust_trades, fund["valuation_date"])
    cash_breaks = reconciliation.reconcile_cash(book_cash, cust_cash, fund["valuation_date"])
    all_breaks = pd.concat([trade_breaks, cash_breaks], ignore_index=True)
    aging = reconciliation.aging_summary(all_breaks)

    # --- 4. KYC / AML ---
    scored = kyc.score_customers(customers)
    alerts = kyc.monitor_transactions(transactions)
    tiers = kyc.tier_distribution(scored)

    # --- 5. Reports ---
    xlsx = reporting.write_excel(
        os.path.join(OUTPUT_DIR, "fund_ops_report.xlsx"),
        nav_res, valuation, trade_breaks, cash_breaks, scored, alerts, fund,
    )
    png1 = reporting.chart_nav_composition(nav_res, os.path.join(OUTPUT_DIR, "nav_composition.png"))
    png2 = reporting.chart_break_aging(aging, os.path.join(OUTPUT_DIR, "break_aging.png"))
    png3 = reporting.chart_risk_tiers(tiers, os.path.join(OUTPUT_DIR, "risk_tier_distribution.png"))

    _print_summary(fund, valuation, price_exc, nav_res, trade_breaks, cash_breaks,
                   scored, alerts, [xlsx, png1, png2, png3])


def _print_summary(fund, valuation, price_exc, nav_res, trade_breaks, cash_breaks,
                   scored, alerts, files):
    line = "=" * 70
    print(line)
    print(f"INVESTMENT OPERATIONS & FUND ACCOUNTING  -  {fund['fund_name']}")
    print(f"Valuation date: {fund['valuation_date'].date()}")
    print(line)

    print("\n1) PRICING")
    print("-" * 70)
    print(f"  Positions priced      : {len(valuation)}")
    print(f"  Holdings market value : ${nav_res.holdings_mv:,.2f}")
    print(f"  Pricing exceptions    : {len(price_exc)}")
    for _, r in price_exc.iterrows():
        print(f"     - {r['ticker']:<7} {r['price_source']}"
              + (f" (age {int(r['price_age_days'])}d)" if r['price_age_days'] == r['price_age_days'] else ""))

    print("\n2) NAV WATERFALL")
    print("-" * 70)
    print(f"  Gross Asset Value     : ${nav_res.gross_asset_value:,.2f}")
    print(f"  Mgmt fee accrued(TER) : ${nav_res.management_fee_accrued:,.2f}")
    print(f"  Other accrued exp.    : ${nav_res.other_accrued_expenses:,.2f}")
    print(f"  Net Asset Value       : ${nav_res.nav:,.2f}")
    print(f"  NAV per unit          : {nav_res.nav_per_unit:.6f}  "
          f"(prior {nav_res.prior_nav_per_unit:.6f})")
    print(f"  Day-over-day move     : {nav_res.nav_move_pct:+.2%}  "
          f"{'*** FLAGGED (>=2%)' if nav_res.move_flagged else '(within tolerance)'}")

    print("\n3) RECONCILIATION  (internal book vs custodian)")
    print("-" * 70)
    print(f"  Trade breaks : {len(trade_breaks)}")
    for _, r in trade_breaks.iterrows():
        print(f"     [{r['severity']:<6}] {r['key']:<8} {r['break_type']:<22} "
              f"age {r['age_days']}d - {r['detail']}")
    print(f"  Cash breaks  : {len(cash_breaks)}")
    for _, r in cash_breaks.iterrows():
        print(f"     [{r['severity']:<6}] {r['key']:<22} {r['break_type']:<22} "
              f"age {r['age_days']}d")

    print("\n4) KYC / AML")
    print("-" * 70)
    dist = scored["risk_tier"].value_counts().to_dict()
    print(f"  Customers scored : {len(scored)}  "
          f"(Low {dist.get('Low',0)} / Medium {dist.get('Medium',0)} / High {dist.get('High',0)})")
    for _, r in scored[scored["risk_tier"] == "High"].iterrows():
        print(f"     - {r['customer_id']} {r['name']:<24} score {r['composite_score']:>5} "
              f"-> {r['diligence']}" + ("  [override]" if r['edd_override'] else ""))
    print(f"  AML alerts       : {len(alerts)}")
    for _, r in alerts.iterrows():
        print(f"     [{r['severity']:<6}] {r['customer_id']:<5} {r['rule']:<22} {r['detail']}")

    print("\nFILES WRITTEN")
    print("-" * 70)
    for f in files:
        print(f"  {f}")
    print(line)


if __name__ == "__main__":
    main()
