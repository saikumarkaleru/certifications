"""
implied_vol.py  --  invert the Black-Scholes price for volatility
=================================================================

WHAT "IMPLIED VOL" MEANS (interview one-liner):
  Every other BSM input (S, K, T, r, q) is observable. Volatility is NOT. So we
  take the option's MARKET price and ask: "what single sigma, plugged into BSM,
  reproduces this price?" That sigma is the IMPLIED volatility -- the market's
  forward-looking estimate of how much the underlying will move. Plotting IV
  against strike gives the famous volatility SMILE / skew.

HOW WE SOLVE IT:
  1. Newton-Raphson: fast (quadratic) because we have the exact derivative, VEGA.
     step:  sigma <- sigma - (price(sigma) - target) / vega_raw
     NOTE: we use RAW vega (dPrice/dsigma), NOT the /100 'reporting' vega, so the
     units of the Newton step are correct.
  2. Bisection fallback: Newton can overshoot for deep ITM/OTM options or when
     vega is tiny. If Newton diverges or leaves the sensible band, we fall back
     to bisection on [1e-4, 5.0], which is slow but CANNOT diverge as long as the
     target price is bracketed.
"""

import math
from .black_scholes import bs_price, d1_d2, norm_pdf


def _vega_raw(S, K, T, r, sigma, q=0.0):
    """Raw vega = dPrice/dsigma (NOT divided by 100). Same for call and put."""
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    return S * math.exp(-q * T) * norm_pdf(d1) * math.sqrt(T)


def _no_arb_bounds(S, K, T, r, option, q):
    """Intrinsic-value bounds a European price must sit inside, else no IV exists.

    Below the discounted-intrinsic lower bound (or above the upper bound) there is
    literally no sigma that reproduces the price -- it would be an arbitrage.
    """
    disc_S = S * math.exp(-q * T)
    disc_K = K * math.exp(-r * T)
    if option.lower() == "call":
        return max(disc_S - disc_K, 0.0), disc_S      # 0 <= C-intrinsic .. <= S e^-qT
    return max(disc_K - disc_S, 0.0), disc_K


def implied_vol(target_price, S, K, T, r, option="call", q=0.0,
                tol=1e-8, max_iter=100):
    """Return the Black-Scholes implied volatility for a given market price.

    Strategy: Newton-Raphson using vega, with a robust bisection fallback.
    Returns float('nan') if the price violates no-arbitrage bounds (no IV exists).
    """
    option = option.lower()
    lo_price, hi_price = _no_arb_bounds(S, K, T, r, option, q)
    # A tiny epsilon lets prices sitting exactly on the bound still solve.
    if target_price < lo_price - 1e-10 or target_price > hi_price + 1e-10:
        return float("nan")

    # ---- Attempt 1: Newton-Raphson ---------------------------------------
    # Start from a sensible guess; 0.2 (20% vol) is a fine neutral seed.
    sigma = 0.2
    for _ in range(max_iter):
        price = bs_price(S, K, T, r, sigma, option, q)
        diff = price - target_price
        if abs(diff) < tol:
            return sigma
        v = _vega_raw(S, K, T, r, sigma, q)
        if v < 1e-10:                      # vega too flat -> Newton is unreliable
            break
        step = diff / v
        sigma_new = sigma - step
        # If Newton wanders out of the sane band, abandon it for bisection.
        if sigma_new <= 1e-6 or sigma_new > 5.0 or not math.isfinite(sigma_new):
            break
        sigma = sigma_new

    # ---- Attempt 2: Bisection (cannot diverge once bracketed) -------------
    lo, hi = 1e-4, 5.0
    f_lo = bs_price(S, K, T, r, lo, option, q) - target_price
    f_hi = bs_price(S, K, T, r, hi, option, q) - target_price
    if f_lo * f_hi > 0:                     # target not bracketed -> unsolvable
        return float("nan")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        f_mid = bs_price(S, K, T, r, mid, option, q) - target_price
        if abs(f_mid) < tol or (hi - lo) < 1e-10:
            return mid
        if f_lo * f_mid < 0:                # root is in the left half
            hi, f_hi = mid, f_mid
        else:                               # root is in the right half
            lo, f_lo = mid, f_mid
    return 0.5 * (lo + hi)
