"""
reporting.py -- turn the analysis into a workbook and charts
============================================================

Presentation only; no new analysis happens here. We take the tables the other
modules produced and write:

  * one Excel workbook (output/credit_analysis.xlsx) with:
      - Summary     : one row per borrower (rating, PD, headline ratios)
      - Spread_<CODE>: the standardised spread for each borrower
      - Ratios_<CODE>: the full multi-year ratio table for each borrower
      - Serviceability: CFADS / DSCR / ICR (latest year) for all borrowers
      - Rating       : the scorecard breakdown for all borrowers
      - Scenarios    : the stress table for all borrowers
  * three PNG charts:
      - leverage vs coverage scatter (positioning map, latest year)
      - DSCR by scenario, grouped by borrower
      - rating migration: composite base vs downside per borrower

Charts use matplotlib's non-interactive 'Agg' backend so they render to file on
any machine (including a headless server) with no display attached.
"""

from __future__ import annotations

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from . import ratios as ratio_mod
from . import serviceability as svc
from . import rating as rating_mod
from . import scenario as scenario_mod


def _out_dir():
    project = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out = os.path.join(project, "output")
    os.makedirs(out, exist_ok=True)
    return out


# ---------------------------------------------------------------------------
# Excel
# ---------------------------------------------------------------------------
def build_summary(facts_by_company, meta, business):
    """One row per borrower with the headline credit read."""
    rows = []
    for code, facts in facts_by_company.items():
        yr = max(facts.columns)
        r = ratio_mod.compute_year(facts, yr)
        card = rating_mod.scorecard(facts, business[code], yr)
        rows.append({
            "Code": code,
            "Borrower": meta[code]["name"],
            "Sector": meta[code]["sector"],
            "FY": yr,
            "Rating": card["band"],
            "Composite": round(card["composite"], 1),
            "PD % (1yr)": card["pd"],
            "Net Debt/EBITDA (x)": round(r["Net Debt/EBITDA (x)"], 2),
            "DSCR (x)": round(svc.dscr(facts, yr), 2),
            "Interest Cover (x)": round(r["Interest Coverage (x)"], 2),
            "EBITDA Margin (%)": round(r["EBITDA Margin (%)"], 1),
            "Current Ratio (x)": round(r["Current Ratio (x)"], 2),
        })
    return pd.DataFrame(rows)


def write_excel(facts_by_company, meta, business, path=None):
    out = _out_dir()
    path = path or os.path.join(out, "credit_analysis.xlsx")

    with pd.ExcelWriter(path, engine="openpyxl") as xl:
        build_summary(facts_by_company, meta, business).to_excel(
            xl, sheet_name="Summary", index=False)

        # Per-borrower spreads and ratio tables.
        for code, facts in facts_by_company.items():
            facts.to_excel(xl, sheet_name=f"Spread_{code}")
            ratio_mod.compute_ratios(facts).round(2).to_excel(
                xl, sheet_name=f"Ratios_{code}")

        # Serviceability (latest year) stacked across borrowers.
        svc_rows = []
        for code, facts in facts_by_company.items():
            yr = max(facts.columns)
            t = svc.serviceability_table(facts)[yr]
            d = t.to_dict()
            d = {"Code": code, "FY": yr, **d}
            svc_rows.append(d)
        pd.DataFrame(svc_rows).to_excel(xl, sheet_name="Serviceability", index=False)

        # Rating scorecards stacked across borrowers.
        rate_frames = []
        for code, facts in facts_by_company.items():
            card = rating_mod.scorecard(facts, business[code])
            t = card["table"].copy()
            t.insert(0, "Code", code)
            t["Composite"] = round(card["composite"], 1)
            t["Band"] = card["band"]
            rate_frames.append(t)
        pd.concat(rate_frames, ignore_index=True).round(3).to_excel(
            xl, sheet_name="Rating", index=False)

        # Scenarios stacked across borrowers.
        scen_frames = []
        for code, facts in facts_by_company.items():
            t = scenario_mod.scenario_table(facts, business[code])
            t.insert(0, "Code", code)
            scen_frames.append(t)
        pd.concat(scen_frames, ignore_index=True).round(2).to_excel(
            xl, sheet_name="Scenarios", index=False)

    return path


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------
def _save(fig, name):
    p = os.path.join(_out_dir(), name)
    fig.tight_layout()
    fig.savefig(p, dpi=110)
    plt.close(fig)
    return p


def chart_leverage_vs_coverage(facts_by_company, meta):
    """Positioning map: x = Net Debt/EBITDA, y = Interest cover (latest year)."""
    fig, ax = plt.subplots(figsize=(7, 5))
    for code, facts in facts_by_company.items():
        yr = max(facts.columns)
        r = ratio_mod.compute_year(facts, yr)
        x = r["Net Debt/EBITDA (x)"]
        y = r["Interest Coverage (x)"]
        ax.scatter(x, y, s=120)
        ax.annotate(code, (x, y), xytext=(6, 6), textcoords="offset points",
                    fontsize=10, weight="bold")
    ax.axvline(3.0, color="grey", ls="--", lw=1)
    ax.axhline(2.0, color="grey", ls="--", lw=1)
    ax.set_xlabel("Net Debt / EBITDA (x)  -- lower is safer")
    ax.set_ylabel("Interest Coverage (x)  -- higher is safer")
    ax.set_title("Credit positioning: leverage vs coverage (latest FY)")
    ax.grid(True, alpha=0.3)
    return _save(fig, "leverage_vs_coverage.png")


def chart_dscr_scenarios(facts_by_company, business):
    """Grouped bars: DSCR under each scenario, one group per borrower."""
    codes = list(facts_by_company.keys())
    labels = [lbl for lbl, _ in scenario_mod.SCENARIOS]
    data = {}
    for code in codes:
        t = scenario_mod.scenario_table(facts_by_company[code], business[code])
        data[code] = t.set_index("Scenario")["DSCR (x)"].reindex(labels).values

    fig, ax = plt.subplots(figsize=(11, 5.5))
    n = len(codes)
    x = np.arange(len(labels))
    width = 0.8 / n
    for i, code in enumerate(codes):
        ax.bar(x + i * width, data[code], width, label=code)
    ax.axhline(1.0, color="red", ls="--", lw=1, label="DSCR = 1.0 (breakeven)")
    ax.axhline(1.25, color="orange", ls=":", lw=1, label="DSCR = 1.25 (typical covenant)")
    ax.set_xticks(x + width * (n - 1) / 2)
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel("DSCR (x)")
    ax.set_title("Debt-service coverage under stress scenarios")
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    return _save(fig, "dscr_scenarios.png")


def chart_rating_migration(facts_by_company, business):
    """Composite score base vs downside per borrower, with band labels."""
    codes = list(facts_by_company.keys())
    base, down, base_band, down_band = [], [], [], []
    for code in codes:
        t = scenario_mod.scenario_table(facts_by_company[code], business[code]).set_index("Scenario")
        base.append(t.loc["Base", "Composite"])
        base_band.append(t.loc["Base", "Band"])
        down_row = t.loc["Downside (EBITDA -20% & +200bps)"]
        down.append(down_row["Composite"])
        down_band.append(down_row["Band"])

    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(codes))
    w = 0.38
    b1 = ax.bar(x - w / 2, base, w, label="Base", color="#2b8cbe")
    b2 = ax.bar(x + w / 2, down, w, label="Downside", color="#d95f0e")
    for rect, band in zip(b1, base_band):
        ax.annotate(band, (rect.get_x() + rect.get_width() / 2, rect.get_height()),
                    ha="center", va="bottom", fontsize=9, weight="bold")
    for rect, band in zip(b2, down_band):
        ax.annotate(band, (rect.get_x() + rect.get_width() / 2, rect.get_height()),
                    ha="center", va="bottom", fontsize=9, weight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(codes)
    ax.set_ylabel("Composite score (0-100)")
    ax.set_title("Rating migration: base vs downside")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_ylim(0, 100)
    return _save(fig, "rating_migration.png")


def write_charts(facts_by_company, meta, business):
    return [
        chart_leverage_vs_coverage(facts_by_company, meta),
        chart_dscr_scenarios(facts_by_company, business),
        chart_rating_migration(facts_by_company, business),
    ]
