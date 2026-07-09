"""
validation.py  --  check analytic Greeks against FINITE DIFFERENCES
====================================================================

WHY BOTHER (interview one-liner):
  Our Greeks are hand-derived calculus. A single sign error or misplaced e^(-qT)
  would be invisible in the price but poison a hedge. Finite differences give an
  INDEPENDENT numeric estimate of each derivative: bump one input by a tiny h,
  re-price, and measure the slope. If the analytic and numeric numbers match to
  ~1e-4, we trust the calculus. This is exactly how a desk quant sanity-checks a
  new pricer before it touches real risk.

METHOD -- central differences (second-order accurate):
    df/dx  ~= ( f(x+h) - f(x-h) ) / (2h)
  Central (not forward) differences cancel the leading error term, so a modest h
  gives a clean estimate. We match each analytic Greek's SCALING (per 1% / per
  day) so the comparison is apples-to-apples.
"""

import pandas as pd
from .black_scholes import bs_price, all_greeks


def validate_greeks(S, K, T, r, sigma, option="call", q=0.0):
    """Return a DataFrame comparing analytic vs finite-difference Greeks.

    Columns: Greek, Analytic, Numeric, AbsError. Covers the first-order Greeks
    plus vanna (a mixed second derivative) as a representative cross-check.
    """
    analytic = all_greeks(S, K, T, r, sigma, option, q)

    # Small, well-conditioned bump sizes for each input (absolute bumps).
    hS = S * 1e-4          # spot bump
    hSig = 1e-4            # vol bump (absolute, e.g. 0.0001 = 0.01 vol points)
    hT = 1e-5             # time bump (years)
    hr = 1e-6             # rate bump

    def price(s=S, k=K, t=T, rr=r, sig=sigma):
        return bs_price(s, k, t, rr, sig, option, q)

    # --- DELTA = dPrice/dSpot (central difference in S) ---
    num_delta = (price(s=S + hS) - price(s=S - hS)) / (2 * hS)

    # --- GAMMA = d2Price/dSpot2 (second central difference in S) ---
    num_gamma = (price(s=S + hS) - 2 * price() + price(s=S - hS)) / (hS * hS)

    # --- VEGA = dPrice/dsigma, reported per 1% -> divide raw slope by 100 ---
    num_vega = (price(sig=sigma + hSig) - price(sig=sigma - hSig)) / (2 * hSig) / 100.0

    # --- THETA = dPrice/dT, per calendar day. Note: as calendar time passes, T
    #     shrinks, so theta = -dPrice/dT. Divide by 365 to match our scaling. ---
    num_theta = -(price(t=T + hT) - price(t=T - hT)) / (2 * hT) / 365.0

    # --- RHO = dPrice/dr, reported per 1% -> divide raw slope by 100 ---
    num_rho = (price(rr=r + hr) - price(rr=r - hr)) / (2 * hr) / 100.0

    # --- VANNA = dDelta/dsigma. Bump sigma, recompute delta numerically, per 1%. ---
    def delta_num(sig):
        return (price(s=S + hS, sig=sig) - price(s=S - hS, sig=sig)) / (2 * hS)
    num_vanna = (delta_num(sigma + hSig) - delta_num(sigma - hSig)) / (2 * hSig) / 100.0

    numeric = {
        "Delta": num_delta,
        "Gamma": num_gamma,
        "Vega": num_vega,
        "Theta": num_theta,
        "Rho": num_rho,
        "Vanna": num_vanna,
    }

    rows = []
    for g, num in numeric.items():
        ana = analytic[g]
        rows.append({
            "Greek": g,
            "Analytic": ana,
            "Numeric": num,
            "AbsError": abs(ana - num),
        })
    return pd.DataFrame(rows)
