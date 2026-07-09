"""
stats.py -- peer statistics and a rich/cheap screen.

Two jobs:

1) Central tendency for each multiple across the peer set:
   median, mean, and the 25th/75th percentiles (quartiles). We lead with the
   MEDIAN because it is robust to one outlier peer that would otherwise drag the
   mean around.

2) A cross-sectional SCREEN that flags which names look rich or cheap RELATIVE
   to their fundamentals, two ways:
     (a) Z-score of each raw multiple across the peer set (how many standard
         deviations a name sits from the peer average).
     (b) An OLS regression of EV/EBITDA on revenue growth and EBITDA margin.
         Higher growth and fatter margins JUSTIFY a higher multiple; the
         regression predicts a "fair" EV/EBITDA for each name, and the residual
         (actual - predicted) says whether the market is paying up (rich) or
         discounting (cheap) versus what fundamentals warrant.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .multiples import MULT_COLS


def peer_summary(mult_df, target):
    """
    Median / mean / Q1 / Q3 for each multiple, computed over PEERS ONLY
    (the target is excluded so we value it against the others).
    """
    peers = mult_df[mult_df.index != target]
    stats = {}
    for col in MULT_COLS:
        s = peers[col].dropna()
        stats[col] = {
            "Median": s.median(),
            "Mean": s.mean(),
            "Q1": s.quantile(0.25),
            "Q3": s.quantile(0.75),
            "Min": s.min(),
            "Max": s.max(),
            "N": int(s.count()),
        }
    return pd.DataFrame(stats).T[["N", "Min", "Q1", "Median", "Mean", "Q3", "Max"]]


def zscore_screen(mult_df, columns=("EV/EBITDA", "P/E", "EV/Revenue")):
    """
    Z-score of each company's multiple across the WHOLE universe.
    z = (x - mean) / std. Positive z = richer than average, negative = cheaper.
    """
    out = pd.DataFrame(index=mult_df.index)
    for col in columns:
        s = mult_df[col]
        mu, sd = s.mean(), s.std(ddof=0)
        out[f"z({col})"] = (s - mu) / sd if sd and sd > 0 else np.nan
    out["z_avg"] = out.mean(axis=1)
    out["flag"] = np.where(out["z_avg"] > 0.5, "RICH",
                           np.where(out["z_avg"] < -0.5, "CHEAP", "in-line"))
    return out


def regression_screen(mult_df, y_col="EV/EBITDA",
                      x_cols=("rev_growth", "ebitda_margin")):
    """
    OLS: EV/EBITDA_i = b0 + b1*growth_i + b2*margin_i + e_i.

    We fit with numpy.linalg.lstsq (plain least squares -- no scipy needed) over
    the companies with complete data, then compute each name's predicted "fair"
    multiple and its residual. A positive residual means the name trades RICHER
    than its growth/margin justify; negative means CHEAPER.

    Returns (result_df, coefficients_dict, r_squared).
    """
    df = mult_df.dropna(subset=[y_col] + list(x_cols)).copy()
    if len(df) < len(x_cols) + 2:
        # Not enough observations to fit a stable regression.
        empty = pd.DataFrame(index=mult_df.index)
        return empty, {}, float("nan")

    y = df[y_col].to_numpy(dtype=float)
    X = df[list(x_cols)].to_numpy(dtype=float)
    # design matrix with an intercept column of 1s
    A = np.column_stack([np.ones(len(df)), X])

    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ coef
    resid = y - pred

    # R^2 = 1 - SS_res / SS_tot
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

    res_df = pd.DataFrame({
        "actual_EV/EBITDA": y,
        "predicted_EV/EBITDA": pred,
        "residual": resid,
    }, index=df.index)
    # standardise residuals so the flag is comparable across peer sets
    rsd = resid.std(ddof=0)
    res_df["resid_z"] = resid / rsd if rsd and rsd > 0 else np.nan
    res_df["flag"] = np.where(res_df["resid_z"] > 0.5, "RICH vs fundamentals",
                              np.where(res_df["resid_z"] < -0.5,
                                       "CHEAP vs fundamentals", "fairly priced"))

    coefficients = {
        "intercept": float(coef[0]),
        x_cols[0]: float(coef[1]),
        x_cols[1]: float(coef[2]),
    }
    return res_df, coefficients, r2
