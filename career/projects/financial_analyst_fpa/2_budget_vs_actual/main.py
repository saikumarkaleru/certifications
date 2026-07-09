"""
main.py - orchestrate the whole Budget vs Actual analysis.

Pipeline:
    1. Build the driver-based budget (or load cached CSVs).
    2. Simulate actuals with a seeded RNG (or load cached CSVs).
    3. Compute variances + favorable/unfavorable flags.
    4. Decompose the revenue variance into Price / Volume / Mix.
    5. Build the flex budget (activity vs rate effects).
    6. Roll a reforecast of the remaining months.
    7. Write plain-English commentary + a CFO KPI summary.
    8. Print a console summary, then write Excel + PNG charts.

Company: "Meridian Instruments Co." (all figures synthetic, seeded).
Run with:  python main.py
"""

import os
import sys

# Make the src/ package importable no matter where the script is launched from.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

from fpa import actuals as actuals_mod
from fpa import variance as var_mod
from fpa import reforecast as rf_mod
from fpa import commentary as cm
from fpa import reporting

INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")


def _fmt(x):
    """Format a plain dollar figure like $1,234,567."""
    return f"${x:,.0f}"


def main():
    print("=" * 74)
    print("  MERIDIAN INSTRUMENTS CO.  -  BUDGET vs ACTUAL (FULL YEAR)")
    print("=" * 74)

    # --- 1 & 2. Data (build+simulate or load cache) ------------------------
    budget, actuals, source = actuals_mod.get_datasets(INPUT_DIR)
    print(f"  Data source: {source}")
    print(f"  Products: {budget['products']['product'].nunique()} lines  x  "
          f"12 months   |   Cost centres: "
          f"{budget['opex']['cost_centre'].nunique()}")

    # --- 3. Variances + flags ---------------------------------------------
    prod_var = var_mod.product_variance(budget, actuals)
    opex_var = var_mod.opex_variance(budget, actuals)
    kpis = var_mod.kpi_summary(budget, actuals)

    print("\n" + "-" * 74)
    print("  PRODUCT VARIANCE (full year)")
    print("-" * 74)
    show = prod_var[["Budget Rev", "Actual Rev", "Rev Var", "Rev Flag",
                     "GP Var", "GP Flag"]].copy()
    for c in ["Budget Rev", "Actual Rev", "Rev Var", "GP Var"]:
        show[c] = show[c].map(_fmt)
    print(show.to_string())

    print("\n  COST-CENTRE OPEX VARIANCE (full year)")
    oshow = opex_var.copy()
    for c in ["Budget Opex", "Actual Opex", "Opex Var"]:
        oshow[c] = oshow[c].map(_fmt)
    print(oshow.to_string())

    # --- 4. Price / Volume / Mix ------------------------------------------
    pvm = var_mod.pvm_decomposition(budget, actuals)
    t = pvm.loc["TOTAL"]
    print("\n" + "-" * 74)
    print("  REVENUE VARIANCE  ->  PRICE / VOLUME / MIX  (full year)")
    print("-" * 74)
    print(f"  Total revenue variance : {_fmt(t['Total Var'])}")
    print(f"    Price  effect        : {_fmt(t['Price'])}")
    print(f"    Volume effect        : {_fmt(t['Volume'])}")
    print(f"    Mix    effect        : {_fmt(t['Mix'])}")
    print(f"    Reconciliation check : {t['Check']:.4f}  (must be ~0)")

    # --- 5. Flex budget ----------------------------------------------------
    flex = var_mod.flex_budget(budget, actuals)
    ft = flex.loc["TOTAL"]
    print("\n" + "-" * 74)
    print("  FLEX BUDGET  -  activity vs rate effects (revenue, full year)")
    print("-" * 74)
    print(f"  Static budget revenue  : {_fmt(ft['Rev Static'])}")
    print(f"  Flex budget revenue    : {_fmt(ft['Rev Flex'])}  (budget rates @ actual volume)")
    print(f"  Actual revenue         : {_fmt(ft['Rev Actual'])}")
    print(f"    Volume/activity eff. : {_fmt(ft['Rev Volume Eff'])}  (flex - static)")
    print(f"    Rate/price effect    : {_fmt(ft['Rev Rate Eff'])}  (actual - flex)")

    # --- 6. Reforecast -----------------------------------------------------
    reforecast_df, meta = rf_mod.rolling_reforecast(budget, actuals)
    rt = reforecast_df.loc["TOTAL"]
    print("\n" + "-" * 74)
    print(f"  ROLLING REFORECAST  (closed: {meta['closed_months'][0]}-"
          f"{meta['closed_months'][-1]}, reforecast rest, alpha={meta['alpha']})")
    print("-" * 74)
    print(f"  Original budget revenue: {_fmt(rt['Budget Rev'])}")
    print(f"  Reforecast revenue     : {_fmt(rt['Reforecast Rev'])}")
    print(f"  Revenue delta vs budget: {_fmt(rt['Rev Delta'])}")

    # --- 7. Commentary + KPIs ---------------------------------------------
    print("\n" + "-" * 74)
    print("  AUTO-GENERATED COMMENTARY")
    print("-" * 74)
    for line in cm.revenue_commentary(budget, actuals):
        print(f"  - {line}")
    for line in cm.cost_commentary(budget, actuals):
        print(f"  - {line}")

    print("\n  CFO KPI SUMMARY")
    for line in cm.kpi_commentary(kpis):
        print(f"  - {line}")

    # --- 8. Write outputs --------------------------------------------------
    xlsx = reporting.write_excel(budget, actuals, kpis, OUTPUT_DIR)
    charts = reporting.write_charts(budget, actuals, OUTPUT_DIR)

    print("\n" + "=" * 74)
    print("  OUTPUTS WRITTEN")
    print("=" * 74)
    print(f"  Excel : {xlsx}")
    print("          sheets: Budget | Actual | Variance | PVM | Flex | Reforecast | KPIs")
    for name, p in charts.items():
        print(f"  Chart : {p}")
    print("=" * 74)


if __name__ == "__main__":
    main()
