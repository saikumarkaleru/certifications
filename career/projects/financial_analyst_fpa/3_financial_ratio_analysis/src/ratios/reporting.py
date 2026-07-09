"""
reporting.py -- turn the analysis into a workbook and charts
============================================================

Nothing analytical happens here; this is presentation only. We take the tables
the other modules produced and write:

  * one Excel workbook (output/financial_ratio_analysis.xlsx) with a sheet per
    view: Ratios (target, multi-year), DuPont, Benchmark, Trends, RedFlags, and
    RawData (the underlying facts for every company); and
  * four PNG charts that a reader can grasp in five seconds each:
      - ROE DuPont bar (the 3 drivers of the target's latest ROE)
      - margin trend (gross/operating/net margin over time)
      - peer benchmark bar (target's percentile on each key ratio)
      - leverage vs peers (debt/equity of every company, latest year)

Charts use matplotlib's non-interactive 'Agg' backend so they render to file on
any machine, including a headless server, with no display attached.
"""

from __future__ import annotations

import os
import matplotlib
matplotlib.use("Agg")                     # render to file, never open a window
import matplotlib.pyplot as plt
import pandas as pd

from .ratios import compute_ratios, latest_year, KEY_RATIOS
from . import dupont, benchmark


def _out_dir():
    project = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out = os.path.join(project, "output")
    os.makedirs(out, exist_ok=True)
    return out


def write_excel(facts_by_ticker, target, path=None):
    """Write the multi-sheet workbook. Returns the path written."""
    out = _out_dir()
    path = path or os.path.join(out, "financial_ratio_analysis.xlsx")
    tfacts = facts_by_ticker[target]

    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        # Ratios: the target across every year (the headline sheet).
        compute_ratios(tfacts).to_excel(xl, sheet_name="Ratios")
        # DuPont: 3- and 5-step decomposition of the latest ROE.
        dupont.dupont_table(tfacts, latest_year(tfacts)).to_excel(
            xl, sheet_name="DuPont", index=False)
        # Benchmark: target's standing vs peers on each key ratio.
        benchmark.benchmark_summary(facts_by_ticker, target).to_excel(
            xl, sheet_name="Benchmark", index=False)
        # Trends: improving/deteriorating flags for the target.
        from .quality import trend_flags, red_flags
        trend_flags(tfacts).to_excel(xl, sheet_name="Trends", index=False)
        # RedFlags: earnings-quality panel for the target.
        red_flags(tfacts).to_excel(xl, sheet_name="RedFlags")
        # RawData: the underlying facts for every company (audit trail).
        for tk, facts in facts_by_ticker.items():
            facts.to_excel(xl, sheet_name=f"Raw_{tk}")
    return path


def _save(fig, name):
    out = _out_dir()
    p = os.path.join(out, name)
    fig.tight_layout()
    fig.savefig(p, dpi=110)
    plt.close(fig)
    return p


def chart_dupont(facts, target):
    """Bar chart of the 3-step DuPont drivers for the target's latest year."""
    d = dupont.dupont_3step(facts, latest_year(facts))
    labels = ["Net Margin", "Asset Turnover", "Equity Multiplier"]
    vals = [d[k] for k in labels]
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(labels, vals, color=["#4C72B0", "#55A868", "#C44E52"])
    ax.set_title(f"{target}: 3-step DuPont drivers of ROE "
                 f"(ROE = {d['ROE (direct)']*100:.1f}%)")
    ax.set_ylabel("driver value")
    for b, val in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height(),
                f"{val:.2f}", ha="center", va="bottom", fontsize=9)
    return _save(fig, "chart_dupont.png")


def chart_margins(facts, target):
    """Line chart of the three margins over time for the target."""
    r = compute_ratios(facts)
    fig, ax = plt.subplots(figsize=(6, 4))
    for ratio, colour in [("Gross Margin %", "#4C72B0"),
                          ("Operating Margin %", "#55A868"),
                          ("Net Margin %", "#C44E52")]:
        ax.plot(r.columns, r.loc[ratio], marker="o", label=ratio, color=colour)
    ax.set_title(f"{target}: margin trend")
    ax.set_ylabel("%")
    ax.set_xlabel("fiscal year")
    ax.legend(fontsize=8)
    return _save(fig, "chart_margins.png")


def chart_benchmark(facts_by_ticker, target):
    """Horizontal bar of the target's percentile rank on each key ratio."""
    ranks = benchmark.percentile_ranks(facts_by_ticker, target)[target]
    ranks = ranks.reindex(KEY_RATIOS).dropna()
    fig, ax = plt.subplots(figsize=(7, 6))
    colours = ["#55A868" if v >= 50 else "#C44E52" for v in ranks]
    ax.barh(ranks.index, ranks.values, color=colours)
    ax.axvline(50, color="grey", linestyle="--", linewidth=1)
    ax.set_xlim(0, 100)
    ax.set_title(f"{target}: percentile rank vs peers (higher = better)")
    ax.set_xlabel("percentile (0-100)")
    ax.invert_yaxis()
    return _save(fig, "chart_benchmark.png")


def chart_leverage(facts_by_ticker, target):
    """Bar of Debt/Equity for every company (latest year), target highlighted."""
    matrix = benchmark.latest_ratio_matrix(facts_by_ticker)
    de = matrix.loc["Debt / Equity"]
    fig, ax = plt.subplots(figsize=(6, 4))
    colours = ["#C44E52" if tk == target else "#4C72B0" for tk in de.index]
    ax.bar(de.index, de.values, color=colours)
    ax.set_title("Debt / Equity vs peers (target in red)")
    ax.set_ylabel("Debt / Equity")
    for i, val in enumerate(de.values):
        ax.text(i, val, f"{val:.2f}", ha="center", va="bottom", fontsize=9)
    return _save(fig, "chart_leverage.png")


def write_charts(facts_by_ticker, target):
    """Render all four charts. Returns the list of file paths."""
    tfacts = facts_by_ticker[target]
    return [
        chart_dupont(tfacts, target),
        chart_margins(tfacts, target),
        chart_benchmark(facts_by_ticker, target),
        chart_leverage(facts_by_ticker, target),
    ]
