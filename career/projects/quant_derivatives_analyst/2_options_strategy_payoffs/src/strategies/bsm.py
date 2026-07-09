"""
bsm.py -- A minimal Black-Scholes-Merton (BSM) option pricing engine.

WHY THIS EXISTS
---------------
An option's payoff at EXPIRY is simple: max(S-K, 0) for a call. But BEFORE
expiry an option is worth more than its intrinsic value because there is still
time for the stock to move in your favour -- this extra amount is "time value".
To draw the smooth, curved P&L line of a strategy *before* expiry we need a
model that prices an option at any time-to-expiry T > 0. BSM is the industry
standard closed-form model for European options, so we implement it here.

We deliberately keep it tiny and dependency-free:
  * No scipy -- we build the standard-normal CDF from math.erf (see norm_cdf).
  * We include a continuous dividend yield q (the "Merton" extension), which
    also lets us price options on indices / dividend-paying stocks correctly.

Everything an options-desk candidate should be able to defend line-by-line.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Standard normal distribution helpers (no scipy available)
# ---------------------------------------------------------------------------
def norm_cdf(x: float) -> float:
    """
    Cumulative distribution function of the standard normal N(0,1).

    The error function erf() is related to the normal CDF by:
        N(x) = 0.5 * (1 + erf(x / sqrt(2)))
    math.erf is in the standard library, so we get a high-accuracy CDF for
    free -- this is what feeds the d1/d2 terms in BSM and our probability-of-
    profit calculations.
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    """
    Probability density function of the standard normal N(0,1).
    Needed for gamma, vega and theta (they contain the density term phi(d1)).
    """
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


# ---------------------------------------------------------------------------
# Core BSM building blocks
# ---------------------------------------------------------------------------
def _d1_d2(S: float, K: float, T: float, r: float, sigma: float, q: float):
    """
    Compute the two BSM auxiliary variables d1 and d2.

    d1 = [ ln(S/K) + (r - q + sigma^2/2) * T ] / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    Intuition: d2 is (roughly) the risk-neutral "how many standard deviations
    is the option in the money", and N(d2) is the risk-neutral probability a
    call expires in the money.
    """
    # Guard against T or sigma being zero to avoid divide-by-zero; callers
    # that hit T<=0 should use intrinsic value instead (handled in price_call/put).
    vol_sqrt_t = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t
    return d1, d2


def price_call(S: float, K: float, T: float, r: float, sigma: float, q: float = 0.0) -> float:
    """
    Black-Scholes-Merton price of a European CALL with dividend yield q.

        C = S * e^{-qT} * N(d1) - K * e^{-rT} * N(d2)

    If T <= 0 (at/after expiry) or sigma <= 0, there is no time value left, so
    we return the intrinsic value max(S-K, 0) -- this keeps the function safe to
    call anywhere in the codebase.
    """
    if T <= 0 or sigma <= 0:
        return max(S - K, 0.0)
    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    return S * math.exp(-q * T) * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)


def price_put(S: float, K: float, T: float, r: float, sigma: float, q: float = 0.0) -> float:
    """
    Black-Scholes-Merton price of a European PUT with dividend yield q.

        P = K * e^{-rT} * N(-d2) - S * e^{-qT} * N(-d1)

    Falls back to intrinsic value max(K-S, 0) when T <= 0 or sigma <= 0.
    """
    if T <= 0 or sigma <= 0:
        return max(K - S, 0.0)
    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * math.exp(-q * T) * norm_cdf(-d1)


# ---------------------------------------------------------------------------
# The Greeks -- sensitivities of the option price to market inputs
# ---------------------------------------------------------------------------
@dataclass
class Greeks:
    """A small container for the four Greeks a desk watches most."""
    delta: float   # d(price)/d(spot)        -- directional exposure
    gamma: float   # d(delta)/d(spot)        -- how fast delta changes
    vega: float    # d(price)/d(vol)  per 1 vol-point (i.e. per 0.01 sigma)
    theta: float   # d(price)/d(time) per calendar day -- time decay


def greeks(S: float, K: float, T: float, r: float, sigma: float,
           q: float = 0.0, kind: str = "call") -> Greeks:
    """
    Analytic BSM Greeks for a single option.

    Conventions chosen to match how a trading desk quotes them:
      * vega is per +1 volatility POINT (0.01 change in sigma), so we divide
        the raw dPrice/dSigma by 100.
      * theta is per CALENDAR DAY, so we divide the raw annual theta by 365.
    These conventions make the numbers immediately readable ("this position
    loses $X per day, makes $Y per vol point").

    If T <= 0 or sigma <= 0 the option is at expiry: gamma/vega/theta collapse
    to 0 and delta becomes a step (1 or 0 for a call). We return that limit.
    """
    if T <= 0 or sigma <= 0:
        if kind == "call":
            delta = 1.0 if S > K else 0.0
        else:  # put
            delta = -1.0 if S < K else 0.0
        return Greeks(delta=delta, gamma=0.0, vega=0.0, theta=0.0)

    d1, d2 = _d1_d2(S, K, T, r, sigma, q)
    sqrt_t = math.sqrt(T)
    disc_q = math.exp(-q * T)   # dividend discount factor
    disc_r = math.exp(-r * T)   # interest discount factor
    pdf_d1 = norm_pdf(d1)

    # Gamma and vega have the SAME formula for calls and puts.
    gamma = disc_q * pdf_d1 / (S * sigma * sqrt_t)
    vega = S * disc_q * pdf_d1 * sqrt_t / 100.0   # per 1 vol point

    if kind == "call":
        delta = disc_q * norm_cdf(d1)
        # Annual theta (Merton form) then convert to per-day.
        theta_annual = (
            -(S * disc_q * pdf_d1 * sigma) / (2.0 * sqrt_t)
            - r * K * disc_r * norm_cdf(d2)
            + q * S * disc_q * norm_cdf(d1)
        )
    else:  # put
        delta = disc_q * (norm_cdf(d1) - 1.0)
        theta_annual = (
            -(S * disc_q * pdf_d1 * sigma) / (2.0 * sqrt_t)
            + r * K * disc_r * norm_cdf(-d2)
            - q * S * disc_q * norm_cdf(-d1)
        )

    return Greeks(delta=delta, gamma=gamma, vega=vega, theta=theta_annual / 365.0)
