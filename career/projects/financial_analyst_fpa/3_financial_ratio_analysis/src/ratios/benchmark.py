"""
benchmark.py -- how does the target stack up against its peers?
==============================================================

A ratio in isolation is almost meaningless. "ROE of 150%?" -- is that good?
Only compared to the right peer set. Here we take the LATEST year and, for each
key ratio, rank the target company against the whole peer group using a
PERCENTILE RANK from 0 to 100.

Reading a percentile:
  * 100 = best in the peer set on that ratio
  *  50 = middle of the pack
  *   0 = worst in the peer set
We flip the direction for "lower is better" ratios (debt, DSO, cash cycle) so a
LOW debt/equity still scores a HIGH percentile. That way, across the board,
"higher percentile = better positioned" -- easy to read at a glance.

Method note (defendable): we use pandas' rank(pct=True), which assigns the
i-th smallest of n values the percentile i/n. With 5 companies the possible
scores are 20/40/60/80/100. It is simple, monotonic, and always in (0,100].
"""

from __future__ import annotations

import pandas as pd

from .ratios import compute_ratios, latest_year, KEY_RATIOS, LOWER_IS_BETTER


def latest_ratio_matrix(facts_by_ticker):
    """Build a DataFrame of latest-year ratios: rows = ratio, cols = ticker.

    Each company may end on a slightly different fiscal year; we just take each
    company's own most recent year, which is the standard cross-sectional cut.
    """
    cols = {}
    for tk, facts in facts_by_ticker.items():
        r = compute_ratios(facts)
        cols[tk] = r[latest_year(facts)]
    return pd.DataFrame(cols)


def percentile_ranks(facts_by_ticker, target):
    """Percentile-rank every company on each KEY ratio (0-100).

    Returns a DataFrame: rows = key ratio, cols = ticker, values = percentile.
    'higher percentile = better' after direction adjustment.
    """
    matrix = latest_ratio_matrix(facts_by_ticker).reindex(KEY_RATIOS)
    ranks = {}
    for ratio in KEY_RATIOS:
        row = matrix.loc[ratio]
        # ascending=True normally -> biggest value gets the top percentile.
        # For "lower is better" ratios we rank ascending=False so the SMALLEST
        # value gets the top percentile.
        ascending = ratio not in LOWER_IS_BETTER
        ranks[ratio] = row.rank(pct=True, ascending=ascending) * 100
    out = pd.DataFrame(ranks).T          # rows = ratio, cols = ticker
    return out.round(1)


def benchmark_summary(facts_by_ticker, target):
    """Human-readable strengths/weaknesses for the target vs peers.

    Returns a DataFrame: for each key ratio, the target's raw value, its
    percentile, and a plain-English standing (Strong / Middle / Weak).
    """
    matrix = latest_ratio_matrix(facts_by_ticker).reindex(KEY_RATIOS)
    ranks = percentile_ranks(facts_by_ticker, target)
    rows = []
    for ratio in KEY_RATIOS:
        pct = ranks.at[ratio, target]
        if pd.isna(pct):
            standing = "n/a"
        elif pct >= 75:
            standing = "Strong"
        elif pct >= 40:
            standing = "Middle"
        else:
            standing = "Weak"
        rows.append({
            "Ratio": ratio,
            f"{target} value": round(matrix.at[ratio, target], 3),
            "Percentile vs peers": pct,
            "Standing": standing,
        })
    return pd.DataFrame(rows)
