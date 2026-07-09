"""
reporting.py - write the Excel workbook and the PNG charts.

Nothing analytical happens here; this module only PRESENTS the results that the
other modules computed. Two outputs:

  1. An Excel workbook with one sheet per view (Budget, Actual, Variance, PVM,
     Flex, Reforecast, KPIs).
  2. Three PNG charts:
       - a revenue variance WATERFALL (Budget -> Price -> Volume -> Mix -> Actual)
       - a Budget-vs-Actual grouped bar chart by product
       - a monthly revenue TREND line (budget vs actual across the 12 months)

matplotlib uses the non-interactive "Agg" backend so charts render to file even
with no screen attached (important for a script that "always runs").
"""

import os
import matplotlib
matplotlib.use("Agg")               # render to file, never open a window
import matplotlib.pyplot as plt
import pandas as pd

from .budget import MONTHS
from . import variance as var_mod
from . import reforecast as rf_mod


# ---------------------------------------------------------------------------
# EXCEL
# ---------------------------------------------------------------------------
def write_excel(budget, actuals, kpis, output_dir):
    """Write the multi-sheet workbook and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "budget_vs_actual.xlsx")

    # Pre-compute the analytical tables once.
    pvm = var_mod.pvm_decomposition(budget, actuals)
    flex = var_mod.flex_budget(budget, actuals)
    prod_var = var_mod.product_variance(budget, actuals)
    opex_var = var_mod.opex_variance(budget, actuals)
    reforecast_df, meta = rf_mod.rolling_reforecast(budget, actuals)

    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        # Raw driver tables (tidy form) for full transparency.
        budget["products"].to_excel(xl, sheet_name="Budget", index=False)
        budget["opex"].to_excel(xl, sheet_name="Budget",
                                startrow=len(budget["products"]) + 2, index=False)
        actuals["products"].to_excel(xl, sheet_name="Actual", index=False)
        actuals["opex"].to_excel(xl, sheet_name="Actual",
                                 startrow=len(actuals["products"]) + 2, index=False)

        # Variance summary: products then opex, stacked on one sheet.
        prod_var.to_excel(xl, sheet_name="Variance")
        opex_var.to_excel(xl, sheet_name="Variance", startrow=len(prod_var) + 3)

        pvm.to_excel(xl, sheet_name="PVM")
        flex.to_excel(xl, sheet_name="Flex")

        reforecast_df.to_excel(xl, sheet_name="Reforecast")
        # A little note under the reforecast table on the assumptions used.
        note = pd.DataFrame({
            "Assumption": [
                f"Closed (actual) months: {', '.join(meta['closed_months'])}",
                f"Open (reforecast) months: {', '.join(meta['open_months'])}",
                f"Trend blend alpha: {meta['alpha']} (weight on YTD trend vs plan)",
            ]
        })
        note.to_excel(xl, sheet_name="Reforecast",
                      startrow=len(reforecast_df) + 3, index=False)

        # KPI sheet: one metric per row, plain and CFO-readable.
        kpi_rows = [
            ["Budget revenue", round(kpis["budget_revenue"], 0)],
            ["Actual revenue", round(kpis["actual_revenue"], 0)],
            ["Revenue variance", round(kpis["revenue_var"], 0)],
            ["Revenue variance %", round(kpis["revenue_var_pct"], 2)],
            ["Budget gross margin %", round(kpis["budget_gross_margin_pct"], 2)],
            ["Actual gross margin %", round(kpis["actual_gross_margin_pct"], 2)],
            ["Budget opex ratio %", round(kpis["budget_opex_ratio_pct"], 2)],
            ["Actual opex ratio %", round(kpis["actual_opex_ratio_pct"], 2)],
            ["Budget operating profit", round(kpis["budget_operating_profit"], 0)],
            ["Actual operating profit", round(kpis["actual_operating_profit"], 0)],
            ["Operating profit variance", round(kpis["operating_profit_var"], 0)],
            ["Largest favorable driver", f"{kpis['largest_favorable'][0]} "
                                         f"({round(kpis['largest_favorable'][1], 0)})"],
            ["Largest unfavorable driver", f"{kpis['largest_unfavorable'][0]} "
                                           f"({round(kpis['largest_unfavorable'][1], 0)})"],
        ]
        pd.DataFrame(kpi_rows, columns=["KPI", "Value"]).to_excel(
            xl, sheet_name="KPIs", index=False)

    return path


# ---------------------------------------------------------------------------
# CHARTS
# ---------------------------------------------------------------------------
def _waterfall(budget, actuals, path):
    """Revenue variance waterfall: Budget -> +Price -> +Volume -> +Mix -> Actual."""
    pvm = var_mod.pvm_decomposition(budget, actuals).loc["TOTAL"]
    start = pvm["Budget Rev"]
    steps = [("Budget", start, "base"),
             ("Price", pvm["Price"], "step"),
             ("Volume", pvm["Volume"], "step"),
             ("Mix", pvm["Mix"], "step"),
             ("Actual", pvm["Actual Rev"], "end")]

    fig, ax = plt.subplots(figsize=(9, 5))
    running = 0.0
    for label, value, kind in steps:
        if kind == "base":
            ax.bar(label, value, color="#4C72B0")
            running = value
        elif kind == "end":
            ax.bar(label, value, color="#4C72B0")
        else:
            color = "#55A868" if value >= 0 else "#C44E52"   # green up / red down
            ax.bar(label, value, bottom=running, color=color)
            running += value
    ax.set_title("Revenue Variance Waterfall (Budget -> Actual)")
    ax.set_ylabel("Revenue ($)")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def _budget_vs_actual_bars(budget, actuals, path):
    """Grouped bars: budget vs actual revenue by product."""
    pv = var_mod.product_variance(budget, actuals)
    products = list(pv.index)
    x = range(len(products))
    width = 0.38

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar([i - width / 2 for i in x], pv["Budget Rev"], width,
           label="Budget", color="#4C72B0")
    ax.bar([i + width / 2 for i in x], pv["Actual Rev"], width,
           label="Actual", color="#DD8452")
    ax.set_xticks(list(x))
    ax.set_xticklabels(products, rotation=15)
    ax.set_title("Budget vs Actual Revenue by Product")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def _monthly_trend(budget, actuals, path):
    """Line chart: total company revenue by month, budget vs actual."""
    b = budget["products"].groupby("month_num")["revenue"].sum().reindex(range(1, 13))
    a = actuals["products"].groupby("month_num")["revenue"].sum().reindex(range(1, 13))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(MONTHS, b.values, marker="o", label="Budget", color="#4C72B0")
    ax.plot(MONTHS, a.values, marker="s", label="Actual", color="#DD8452")
    ax.set_title("Monthly Total Revenue: Budget vs Actual")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)


def write_charts(budget, actuals, output_dir):
    """Write all three PNG charts and return their paths."""
    os.makedirs(output_dir, exist_ok=True)
    paths = {
        "waterfall": os.path.join(output_dir, "variance_waterfall.png"),
        "bars":      os.path.join(output_dir, "budget_vs_actual_by_product.png"),
        "trend":     os.path.join(output_dir, "monthly_revenue_trend.png"),
    }
    _waterfall(budget, actuals, paths["waterfall"])
    _budget_vs_actual_bars(budget, actuals, paths["bars"])
    _monthly_trend(budget, actuals, paths["trend"])
    return paths
