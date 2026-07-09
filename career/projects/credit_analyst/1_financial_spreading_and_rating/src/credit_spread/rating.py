"""
rating.py -- a transparent internal rating scorecard
====================================================

Real internal-rating models are just weighted scorecards with a lot of
calibration behind them. This is a small, fully transparent version of exactly
that shape, so a fresher can defend every weight and threshold.

Structure
---------
Two blocks of factors, each factor mapped to a 0-100 sub-score by explicit
thresholds, then combined by weight into a composite (0-100):

  FINANCIAL RISK  (65% total)   pulled straight from the spread / serviceability
    Net Debt/EBITDA .......... 18%
    DSCR ..................... 15%
    Interest Coverage ....... 12%
    EBITDA Margin ........... 10%
    Gearing ................. 10%

  BUSINESS RISK   (35% total)   analyst 1-5 judgement (5 = strongest)
    Market Position ......... 12%
    Industry / Cyclicality .. 10%
    Diversification ......... 6%
    Management & Governance . 7%

The composite maps to an internal band (AAA ... D) and an indicative through-
the-cycle 1-year PD. The bands and PDs are illustrative teaching anchors, not a
regulator-calibrated master scale -- but the MECHANICS mirror the real thing.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import ratios as ratio_mod
from . import serviceability as svc

# ---------------------------------------------------------------------------
# Factor weights (must each sum to their block total; asserted at import).
# ---------------------------------------------------------------------------
FINANCIAL_WEIGHTS = {
    "Net Debt/EBITDA": 0.18,
    "DSCR": 0.15,
    "Interest Coverage": 0.12,
    "EBITDA Margin": 0.10,
    "Gearing": 0.10,
}
BUSINESS_WEIGHTS = {
    "MarketPosition": 0.12,
    "Industry": 0.10,
    "Diversification": 0.06,
    "Management": 0.07,
}
assert abs(sum(FINANCIAL_WEIGHTS.values()) - 0.65) < 1e-9
assert abs(sum(BUSINESS_WEIGHTS.values()) - 0.35) < 1e-9

# Rating bands: (min composite score inclusive, band). Checked high -> low.
BANDS = [
    (90, "AAA"), (82, "AA"), (74, "A"), (64, "BBB"), (54, "BB"),
    (44, "B"), (34, "CCC"), (26, "CC"), (18, "C"), (float("-inf"), "D"),
]

# Indicative 1-year PD per band (illustrative anchors, %).
PD_BY_BAND = {
    "AAA": 0.03, "AA": 0.05, "A": 0.10, "BBB": 0.30, "BB": 1.2,
    "B": 4.0, "CCC": 12.0, "CC": 22.0, "C": 35.0, "D": 100.0,
}


# ---------- factor -> sub-score mappings (higher score = better credit) ------
def _banded(value, thresholds, ascending_good):
    """Map a value to a 0-100 score using (cutoff, score) pairs.

    ascending_good=True  -> higher value is better (e.g. DSCR, margin).
    ascending_good=False -> lower value is better  (e.g. leverage).
    """
    if value is None or pd.isna(value):
        return 10.0
    for cutoff, score in thresholds:
        if ascending_good and value >= cutoff:
            return score
        if not ascending_good and value <= cutoff:
            return score
    return 10.0


def score_net_debt_ebitda(x):
    # lower is better; >8x or negative-EBITDA cases fall through to 5
    return _banded(x, [(1, 100), (2, 85), (3, 70), (4, 55),
                       (5, 40), (6, 25), (8, 12)], ascending_good=False) if (
        x is not None and not pd.isna(x) and x >= 0) else 5.0


def score_dscr(x):
    return _banded(x, [(2.0, 100), (1.5, 85), (1.25, 70), (1.1, 55),
                       (1.0, 40), (0.8, 25)], ascending_good=True)


def score_interest_cover(x):
    return _banded(x, [(6, 100), (4, 85), (3, 70), (2, 55),
                       (1.5, 40), (1.0, 25)], ascending_good=True)


def score_ebitda_margin(pct):
    return _banded(pct, [(20, 100), (15, 85), (12, 70), (9, 55),
                         (6, 40), (3, 25)], ascending_good=True)


def score_gearing(pct):
    # Debt/(Debt+Equity) in %. Lower is better; negative equity (>100%) -> 10.
    if pct is None or pd.isna(pct) or pct >= 100 or pct < 0:
        return 10.0
    return _banded(pct, [(30, 100), (45, 85), (60, 70), (75, 55),
                         (90, 40), (99.9, 25)], ascending_good=False)


def _business_score(rank_1to5):
    """1-5 analyst rank -> 0-100 (1->20 ... 5->100)."""
    return 20.0 * rank_1to5


def band_from_score(score):
    for cutoff, band in BANDS:
        if score >= cutoff:
            return band
    return "D"


def scorecard(facts, business, yr=None):
    """Full scorecard for one borrower.

    Returns a dict with:
      table     : DataFrame(Factor, Category, Weight, Value, Sub-score, Contribution)
      composite : weighted score 0-100
      band      : internal rating band
      pd        : indicative 1-year PD (%)
    """
    if yr is None:
        yr = max(facts.columns)
    r = ratio_mod.compute_year(facts, yr)
    d = svc.dscr(facts, yr)

    # (Factor, category, weight, raw value, sub-score)
    rows = [
        ("Net Debt/EBITDA", "Financial", FINANCIAL_WEIGHTS["Net Debt/EBITDA"],
         r["Net Debt/EBITDA (x)"], score_net_debt_ebitda(r["Net Debt/EBITDA (x)"])),
        ("DSCR", "Financial", FINANCIAL_WEIGHTS["DSCR"],
         d, score_dscr(d)),
        ("Interest Coverage", "Financial", FINANCIAL_WEIGHTS["Interest Coverage"],
         r["Interest Coverage (x)"], score_interest_cover(r["Interest Coverage (x)"])),
        ("EBITDA Margin", "Financial", FINANCIAL_WEIGHTS["EBITDA Margin"],
         r["EBITDA Margin (%)"], score_ebitda_margin(r["EBITDA Margin (%)"])),
        ("Gearing", "Financial", FINANCIAL_WEIGHTS["Gearing"],
         r["Gearing (%)"], score_gearing(r["Gearing (%)"])),
        ("Market Position", "Business", BUSINESS_WEIGHTS["MarketPosition"],
         business["MarketPosition"], _business_score(business["MarketPosition"])),
        ("Industry / Cyclicality", "Business", BUSINESS_WEIGHTS["Industry"],
         business["Industry"], _business_score(business["Industry"])),
        ("Diversification", "Business", BUSINESS_WEIGHTS["Diversification"],
         business["Diversification"], _business_score(business["Diversification"])),
        ("Management & Governance", "Business", BUSINESS_WEIGHTS["Management"],
         business["Management"], _business_score(business["Management"])),
    ]

    table = pd.DataFrame(rows, columns=[
        "Factor", "Category", "Weight", "Value", "Sub-score"])
    table["Contribution"] = table["Weight"] * table["Sub-score"]
    composite = table["Contribution"].sum()
    band = band_from_score(composite)
    return {
        "table": table,
        "composite": composite,
        "band": band,
        "pd": PD_BY_BAND[band],
        "year": yr,
    }


def rating_rationale(code, meta, card):
    """One-paragraph committee-style rationale string."""
    t = card["table"]
    strong = t.loc[t["Sub-score"] >= 85, "Factor"].tolist()
    weak = t.loc[t["Sub-score"] <= 40, "Factor"].tolist()
    name = meta.get(code, {}).get("name", code)
    sector = meta.get(code, {}).get("sector", "n/a")
    parts = [
        f"{name} ({sector}) is assigned an internal rating of {card['band']} "
        f"(composite {card['composite']:.1f}/100, indicative 1-yr PD "
        f"{card['pd']:.2f}%).",
    ]
    if strong:
        parts.append("Supported by: " + ", ".join(strong) + ".")
    if weak:
        parts.append("Key credit weaknesses: " + ", ".join(weak) + ".")
    if not weak:
        parts.append("No factor scored in the weak band.")
    return " ".join(parts)
