"""Merton structural model: the market-implied probability of default.

Merton (1974) treats a firm's equity as a CALL OPTION on its assets, struck at
the value of its debt. If assets end up worth less than debt at maturity, equity
holders walk away (default). We observe equity value E and equity volatility
sigma_E but NOT the asset value V or asset volatility sigma_V, so we solve two
equations simultaneously:

    (1) E       = V*N(d1) - D*exp(-r*T)*N(d2)          (Black-Scholes call)
    (2) sigma_E = (V/E)*N(d1)*sigma_V                   (Ito / option delta)

    d1 = (ln(V/D) + (r + 0.5*sigma_V^2)*T) / (sigma_V*sqrt(T))
    d2 = d1 - sigma_V*sqrt(T)

Then:
    Distance-to-Default  DD = d2   (how many std devs assets are above default)
    Probability of Default PD = N(-d2)

We solve with a clean fixed-point iteration; no scipy required. The standard
normal CDF is built from math.erf.
"""

from __future__ import annotations

import math

import pandas as pd

MAX_ITER = 200
TOLERANCE = 1e-8


def norm_cdf(x: float) -> float:
    """Standard normal CDF via the error function (no scipy dependency)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _d1_d2(v: float, d: float, sigma_v: float,
           r: float, t: float) -> tuple[float, float]:
    sqrt_t = math.sqrt(t)
    d1 = (math.log(v / d) + (r + 0.5 * sigma_v ** 2) * t) / (sigma_v * sqrt_t)
    d2 = d1 - sigma_v * sqrt_t
    return d1, d2


def solve_merton(equity: float, equity_vol: float, default_point: float,
                 r: float = 0.04, t: float = 1.0) -> dict:
    """Solve the Merton system for one firm.

    Parameters
    ----------
    equity        : market value of equity E (market cap).
    equity_vol    : annualised equity volatility sigma_E.
    default_point : debt barrier D (short-term debt + 0.5 * long-term debt).
    r, t          : risk-free rate and horizon (years).

    Returns a dict with asset value, asset vol, DD, PD and a convergence flag.
    """
    # Guard against degenerate inputs.
    if (equity is None or default_point is None or equity_vol is None
            or equity <= 0 or default_point <= 0 or equity_vol <= 0
            or any(math.isnan(x) for x in (equity, equity_vol, default_point))):
        return {"asset_value": float("nan"), "asset_vol": float("nan"),
                "DD": float("nan"), "PD": float("nan"), "converged": False}

    # Initial guesses (standard starting point in the literature).
    v = equity + default_point
    sigma_v = equity_vol * equity / (equity + default_point)
    converged = False

    for _ in range(MAX_ITER):
        d1, d2 = _d1_d2(v, default_point, sigma_v, r, t)
        n_d1 = norm_cdf(d1)
        n_d2 = norm_cdf(d2)

        # Update asset value from the option pricing identity (eq. 1),
        # and asset vol from the delta relationship (eq. 2).
        new_v = (equity + default_point * math.exp(-r * t) * n_d2) / n_d1
        if new_v <= 0 or n_d1 <= 0:
            break
        new_sigma_v = equity_vol * equity / (new_v * n_d1)
        if new_sigma_v <= 0 or math.isnan(new_sigma_v):
            break

        if (abs(new_v - v) < TOLERANCE * v
                and abs(new_sigma_v - sigma_v) < TOLERANCE):
            v, sigma_v = new_v, new_sigma_v
            converged = True
            break
        v, sigma_v = new_v, new_sigma_v

    d1, d2 = _d1_d2(v, default_point, sigma_v, r, t)
    dd = d2                      # distance-to-default
    pd_ = norm_cdf(-d2)         # probability of default
    return {"asset_value": v, "asset_vol": sigma_v,
            "DD": dd, "PD": pd_, "converged": converged}


def default_point(row: pd.Series) -> float:
    """Debt barrier D: current liabilities + 0.5*LT debt (KMV convention).

    Falls back to total liabilities if the components are missing.
    """
    cl = row.get("current_liabilities", float("nan"))
    ltd = row.get("long_term_debt", float("nan"))
    if not math.isnan(cl) and not math.isnan(ltd):
        return cl + 0.5 * ltd
    if not math.isnan(cl):
        return cl
    return row.get("total_liabilities", float("nan"))


def compute_merton(inputs: pd.DataFrame, r: float = 0.04,
                   t: float = 1.0) -> pd.DataFrame:
    """Per-company Merton table: default point, asset value/vol, DD, PD, flag."""
    records = {}
    for ticker, row in inputs.iterrows():
        dp = default_point(row)
        res = solve_merton(row["market_cap"], row["equity_vol"], dp, r=r, t=t)
        res["default_point"] = dp
        records[ticker] = res

    result = pd.DataFrame.from_dict(records, orient="index")
    result.index.name = "ticker"
    return result[["default_point", "asset_value", "asset_vol",
                   "DD", "PD", "converged"]]
