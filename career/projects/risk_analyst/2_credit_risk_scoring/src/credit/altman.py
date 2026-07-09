"""Altman Z-score: the classic ACCOUNTING model of bankruptcy risk.

Edward Altman (1968) combined five balance-sheet / income-statement ratios into
one score using discriminant analysis on real bankrupt vs healthy manufacturers.
It blends liquidity, cumulative profitability, operating profitability, market
leverage and asset turnover.

    Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5

    X1 = Working Capital / Total Assets        (liquidity)
    X2 = Retained Earnings / Total Assets      (cumulative profitability / age)
    X3 = EBIT / Total Assets                    (operating profitability)
    X4 = Market Value of Equity / Total Liab    (market leverage cushion)
    X5 = Sales / Total Assets                    (asset turnover / activity)

Zones (original manufacturing model):
    Z > 2.99          -> Safe
    1.81 <= Z <= 2.99 -> Grey
    Z < 1.81          -> Distress
"""

from __future__ import annotations

import math

import pandas as pd

# Altman's original coefficients.
WEIGHTS = {"X1": 1.2, "X2": 1.4, "X3": 3.3, "X4": 0.6, "X5": 1.0}
SAFE_THRESHOLD = 2.99
DISTRESS_THRESHOLD = 1.81


def classify_zone(z: float) -> str:
    """Map a Z-score to Altman's three risk zones."""
    if math.isnan(z):
        return "N/A"
    if z > SAFE_THRESHOLD:
        return "Safe"
    if z >= DISTRESS_THRESHOLD:
        return "Grey"
    return "Distress"


def z_score(x1: float, x2: float, x3: float,
            x4: float, x5: float) -> float:
    """Altman Z from the five pre-computed ratios."""
    return (WEIGHTS["X1"] * x1 + WEIGHTS["X2"] * x2 + WEIGHTS["X3"] * x3
            + WEIGHTS["X4"] * x4 + WEIGHTS["X5"] * x5)


def _ratios(row: pd.Series) -> dict:
    """Compute the five Altman ratios from one company's raw inputs."""
    total_assets = row["total_assets"]
    working_capital = row["current_assets"] - row["current_liabilities"]
    x1 = working_capital / total_assets
    x2 = row["retained_earnings"] / total_assets
    x3 = row["ebit"] / total_assets
    x4 = row["market_cap"] / row["total_liabilities"]
    x5 = row["revenue"] / total_assets
    return {"X1": x1, "X2": x2, "X3": x3, "X4": x4, "X5": x5}


def compute_altman(inputs: pd.DataFrame) -> pd.DataFrame:
    """Return a per-company table of the 5 ratios, Z-score and zone.

    Parameters
    ----------
    inputs : DataFrame indexed by ticker with the columns produced by
             :func:`credit.data.load_credit_inputs`.
    """
    records = {}
    for ticker, row in inputs.iterrows():
        ratios = _ratios(row)
        z = z_score(ratios["X1"], ratios["X2"], ratios["X3"],
                    ratios["X4"], ratios["X5"])
        record = dict(ratios)
        record["Z"] = z
        record["Zone"] = classify_zone(z)
        records[ticker] = record

    result = pd.DataFrame.from_dict(records, orient="index")
    result.index.name = "ticker"
    return result[["X1", "X2", "X3", "X4", "X5", "Z", "Zone"]]
