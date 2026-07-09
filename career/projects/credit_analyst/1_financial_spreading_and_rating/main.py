"""
Corporate / NBFC Credit Analysis -- Financial Spreading, Serviceability & Rating
================================================================================

One command -> a full junior-analyst credit read on a set of borrowers.

Pipeline (each step lives in its own module under src/credit_spread/):
  1. LOAD    3 years of financials for 3 borrowers from input/, standardise a
             spread, validate the accounting identities.            [data]
  2. RATIOS  leverage, coverage, liquidity, profitability, WC cycle. [ratios]
  3. SERVICE cash-flow-based DSCR / ICR vs the debt schedule.  [serviceability]
  4. RATING  weighted scorecard -> internal rating band + rationale. [rating]
  5. STRESS  EBITDA / rate / revenue shocks, rating migration.     [scenario]
  6. REPORT  console summary, then Excel workbook + PNG charts.   [reporting]

Everything runs fully OFFLINE on bundled synthetic-but-realistic data.
Run:  python main.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from credit_spread import data, ratios, serviceability as svc, rating, scenario, reporting


def main():
    facts_by_company, meta, business = data.load_all()

    print("\n" + "=" * 74)
    print(" CORPORATE / NBFC CREDIT ANALYSIS  --  spreading | DSCR | internal rating")
    print("=" * 74)
    print(f" Borrowers: {', '.join(meta[c]['name'] for c in facts_by_company)}")
    print(" Figures in INR crore. Data: bundled synthetic (fully offline).")

    for code, facts in facts_by_company.items():
        yr = data.latest_year(facts)
        r = ratios.compute_year(facts, yr)
        d = svc.dscr(facts, yr)
        card = rating.scorecard(facts, business[code], yr)

        print("\n" + "-" * 74)
        print(f" {meta[code]['name']}  [{code}]   FY{yr}   ({meta[code]['sector']})")
        print("-" * 74)
        print(f"   Leverage    Net Debt/EBITDA {r['Net Debt/EBITDA (x)']:>6.2f}x"
              f"   Debt/Equity {r['Debt/Equity (x)']:>6.2f}x"
              f"   Gearing {r['Gearing (%)']:>5.1f}%")
        print(f"   Coverage    Interest Cover  {r['Interest Coverage (x)']:>6.2f}x"
              f"   DSCR {d:>6.2f}x ({svc.headroom_class(d)})"
              f"   FCCR {r['FCCR (x)']:>5.2f}x")
        print(f"   Liquidity   Current {r['Current Ratio (x)']:>5.2f}x"
              f"   Quick {r['Quick Ratio (x)']:>5.2f}x"
              f"      Profit  EBITDA mgn {r['EBITDA Margin (%)']:>5.1f}%"
              f"   ROCE {r['ROCE (%)']:>5.1f}%")
        print(f"   WC cycle    DSO {r['DSO (days)']:>5.0f}d"
              f"   DIO {r['DIO (days)']:>5.0f}d"
              f"   DPO {r['DPO (days)']:>5.0f}d"
              f"   CCC {r['Cash Conversion Cycle (days)']:>5.0f}d")
        print(f"   >> RATING   {card['band']}  (composite {card['composite']:.1f}/100,"
              f"  indicative 1-yr PD {card['pd']:.2f}%)")
        print("   " + rating.rating_rationale(code, meta, card))

        # Rating migration to the combined downside scenario.
        stab = scenario.scenario_table(facts, business[code]).set_index("Scenario")
        dn = stab.loc["Downside (EBITDA -20% & +200bps)"]
        print(f"   Stress      Downside -> DSCR {dn['DSCR (x)']:.2f}x,"
              f"  Net Debt/EBITDA {dn['Net Debt/EBITDA (x)']:.2f}x,"
              f"  rating {dn['Band']} (from {card['band']})")

    # ---- write outputs ----
    xlsx = reporting.write_excel(facts_by_company, meta, business)
    charts = reporting.write_charts(facts_by_company, meta, business)
    print("\n" + "=" * 74)
    print(" OUTPUT WRITTEN")
    print(f"   Excel: {xlsx}")
    for c in charts:
        print(f"   Chart: {c}")
    print(" Done. Every ratio, DSCR and rating factor is defensible line by line.")
    print("=" * 74 + "\n")


if __name__ == "__main__":
    main()
