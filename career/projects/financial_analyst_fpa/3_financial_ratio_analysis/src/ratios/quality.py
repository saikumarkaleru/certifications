"""
quality.py -- trends over time + a simple earnings-quality screen
=================================================================

Two related "is this getting better or worse, and can I trust it?" checks.

1) TREND FLAGS
   For the TARGET company, look at each key ratio from the first year to the
   last and label it Improving / Deteriorating / Flat. We compare the earliest
   and latest values, respect direction (for debt/DSO, DOWN is good), and treat
   moves smaller than a set percentage as Flat (noise, not a trend).

2) EARNINGS-QUALITY RED FLAGS
   Reported profit is an accountant's opinion; cash is a fact. When the two
   diverge, earnings quality is suspect. Two classic, easy-to-defend screens:

   * ACCRUALS RATIO = (Net Income - Operating Cash Flow) / Total Assets.
     Big positive accruals mean profit is being booked well ahead of the cash
     arriving -- lower earnings quality, and empirically a bad sign. We flag
     > 10% as a concern.

   * CASH CONVERSION = Operating Cash Flow / Net Income.
     Healthy firms turn each dollar of profit into roughly a dollar (or more)
     of operating cash, so this should be >= 1. Below 1 is a yellow flag that
     earnings are not being backed by cash.
"""

from __future__ import annotations

import pandas as pd

from .ratios import compute_ratios, KEY_RATIOS, LOWER_IS_BETTER

# A ratio must move more than this fraction of its starting value to count as a
# real trend; smaller moves are "Flat". 5% is a reasonable noise threshold.
FLAT_BAND = 0.05


def trend_flags(facts):
    """Improving / Deteriorating / Flat for each key ratio of ONE company.

    Returns a DataFrame with the first value, last value, % change, and flag.
    """
    r = compute_ratios(facts)
    years = list(r.columns)
    first_y, last_y = years[0], years[-1]
    rows = []
    for ratio in KEY_RATIOS:
        if ratio not in r.index:
            continue
        first, last = r.at[ratio, first_y], r.at[ratio, last_y]
        if pd.isna(first) or pd.isna(last) or first == 0:
            flag, pct = "n/a", float("nan")
        else:
            pct = (last - first) / abs(first)
            if abs(pct) < FLAT_BAND:
                flag = "Flat"
            else:
                went_up = last > first
                good = (not went_up) if ratio in LOWER_IS_BETTER else went_up
                flag = "Improving" if good else "Deteriorating"
        rows.append({
            "Ratio": ratio,
            f"{first_y}": round(first, 3) if not pd.isna(first) else None,
            f"{last_y}": round(last, 3) if not pd.isna(last) else None,
            "Change %": round(100 * pct, 1) if not pd.isna(pct) else None,
            "Trend": flag,
        })
    return pd.DataFrame(rows)


def red_flags(facts):
    """Earnings-quality panel for ONE company, across all years.

    Returns a DataFrame: rows = metric, cols = year, plus a final 'Latest flag'
    column giving a plain verdict on the most recent year.
    """
    years = list(facts.columns)
    accruals, cash_conv = {}, {}
    for y in years:
        ni = facts.at["Net Income", y]
        ocf = facts.at["Operating Cash Flow", y]
        ta = facts.at["Total Assets", y]
        accruals[y] = (ni - ocf) / ta if ta not in (0, None) and not pd.isna(ta) else float("nan")
        cash_conv[y] = ocf / ni if ni not in (0, None) and not pd.isna(ni) else float("nan")

    last = years[-1]
    acc_last, cc_last = accruals[last], cash_conv[last]

    # Verdicts on the latest year.
    acc_flag = "RED (high accruals)" if (not pd.isna(acc_last) and acc_last > 0.10) else \
               ("watch" if (not pd.isna(acc_last) and acc_last > 0.05) else "OK")
    cc_flag = "YELLOW (cash < profit)" if (not pd.isna(cc_last) and cc_last < 1.0) else "OK"

    df = pd.DataFrame({
        "Accruals Ratio (NI-OCF)/Assets": pd.Series(accruals).round(3),
        "Cash Conversion (OCF/NI)": pd.Series(cash_conv).round(3),
    }).T
    df["Latest flag"] = [acc_flag, cc_flag]
    return df
