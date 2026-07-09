"""
reporting.py — write the Excel workbook and the PNG charts.
============================================================================
Nothing analytical happens here — this module just presents the results of the
model cleanly: one Excel workbook with a tab per statement, plus a few charts an
interviewer can glance at (revenue & net income trend, free cash flow, and a
scenario comparison of the DCF value per share).
"""

from __future__ import annotations

import os

import matplotlib
matplotlib.use("Agg")           # no GUI needed — we only save PNG files
import matplotlib.pyplot as plt
import pandas as pd


def _assumptions_frame(drivers: dict, opening: dict, meta: dict, source: str,
                       ticker: str) -> pd.DataFrame:
    """A tidy one-column table of every assumption, for the Assumptions tab."""
    rows = {"Data source": source, "Ticker": ticker}
    rows.update({f"driver: {k}": v for k, v in drivers.items()})
    rows.update({f"opening: {k} ($m)": round(v, 1) for k, v in opening.items()})
    rows.update({f"meta: {k}": v for k, v in meta.items()})
    return pd.DataFrame({"value": rows})


def _dcf_frame(dcf: dict) -> pd.DataFrame:
    """Flatten the DCF result into a readable one-column summary."""
    rows = {
        "Beta": round(dcf["beta"], 3),
        "Cost of Equity (CAPM)": round(dcf["cost_of_equity"], 4),
        "Cost of Debt (after tax)": round(dcf["cost_of_debt_after_tax"], 4),
        "Weight Equity": round(dcf["weight_equity"], 3),
        "Weight Debt": round(dcf["weight_debt"], 3),
        "WACC": round(dcf["wacc"], 4),
        "Terminal Growth": round(dcf["terminal_growth"], 4),
        "PV of FCFF (sum, $m)": round(sum(dcf["pv_fcffs"]), 1),
        "Terminal Value ($m)": round(dcf["terminal_value"], 1),
        "PV of Terminal Value ($m)": round(dcf["pv_terminal"], 1),
        "Enterprise Value ($m)": round(dcf["enterprise_value"], 1),
        "Net Debt ($m)": round(dcf["net_debt"], 1),
        "Equity Value ($m)": round(dcf["equity_value"], 1),
        "Shares Outstanding ($m)": round(dcf["shares_out"], 1),
        "Value per Share ($)": round(dcf["value_per_share"], 2),
    }
    return pd.DataFrame({"value": rows})


def write_excel(path: str, model: dict, scenarios: pd.DataFrame,
                sensitivity: pd.DataFrame, dcf: dict, drivers: dict,
                opening: dict, meta: dict, source: str, ticker: str) -> str:
    """Write every result to a single multi-tab workbook."""
    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        model["income"].to_excel(xl, sheet_name="Income Statement")
        model["balance"].to_excel(xl, sheet_name="Balance Sheet")
        model["cashflow"].to_excel(xl, sheet_name="Cash Flow")
        model["debt"].to_excel(xl, sheet_name="Debt Schedule")
        model["fcff"].to_excel(xl, sheet_name="FCFF")
        scenarios.to_excel(xl, sheet_name="Scenarios")
        sensitivity.to_excel(xl, sheet_name="Sensitivity")
        _dcf_frame(dcf).to_excel(xl, sheet_name="DCF")
        _assumptions_frame(drivers, opening, meta, source, ticker).to_excel(
            xl, sheet_name="Assumptions")
    return path


def write_charts(output_dir: str, model: dict, scenarios: pd.DataFrame,
                 ticker: str) -> list:
    """Save three PNG charts; return the list of file paths written."""
    years = model["years"]
    paths = []

    # 1) Revenue & Net Income trend
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(years, model["income"].loc["Revenue"], label="Revenue", color="#4C72B0")
    ax.plot(years, model["income"].loc["Net Income"], marker="o",
            color="#C44E52", label="Net Income")
    ax.set_title(f"{ticker}: Revenue & Net Income (forecast, $m)")
    ax.set_ylabel("$m"); ax.legend(); fig.tight_layout()
    p = os.path.join(output_dir, "revenue_net_income.png"); fig.savefig(p, dpi=110)
    plt.close(fig); paths.append(p)

    # 2) Free cash flow (FCFF) trend
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(years, model["fcff"].loc["FCFF"], color="#55A868")
    ax.set_title(f"{ticker}: Unlevered Free Cash Flow / FCFF (forecast, $m)")
    ax.set_ylabel("$m"); fig.tight_layout()
    p = os.path.join(output_dir, "free_cash_flow.png"); fig.savefig(p, dpi=110)
    plt.close(fig); paths.append(p)

    # 3) Scenario comparison of DCF value per share
    fig, ax = plt.subplots(figsize=(7, 4.5))
    vps = scenarios.loc["Value per Share ($)"]
    colors = {"Bull": "#55A868", "Base": "#4C72B0", "Bear": "#C44E52"}
    ax.bar(vps.index, vps.values, color=[colors.get(c, "#888") for c in vps.index])
    ax.set_title(f"{ticker}: DCF Value per Share by Scenario ($)")
    ax.set_ylabel("$ / share")
    for i, v in enumerate(vps.values):
        ax.text(i, v, f"${v:,.0f}", ha="center", va="bottom")
    fig.tight_layout()
    p = os.path.join(output_dir, "scenario_value_per_share.png"); fig.savefig(p, dpi=110)
    plt.close(fig); paths.append(p)

    return paths
