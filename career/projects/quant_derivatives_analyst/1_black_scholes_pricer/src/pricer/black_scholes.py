"""
black_scholes.py  --  Black-Scholes-Merton pricing + Greeks (with dividend yield q)
====================================================================================

WHAT LIVES HERE (plain English):
  * The normal distribution helpers N(x) and n(x), built from math.erf (NO scipy).
  * d1 / d2, the two standardized distances that drive the whole model.
  * Closed-form CALL and PUT prices for a stock paying a CONTINUOUS dividend yield q.
  * FIRST-order Greeks : delta, gamma, vega, theta, rho.
  * SECOND-order Greeks: vanna, volga (vomma), charm.

WHY THE DIVIDEND YIELD q MATTERS (interview intuition):
  A stock that pays dividends "leaks" value while you hold the option. In the
  risk-neutral world the stock drifts at (r - q) instead of r, and today's spot is
  effectively discounted by e^(-qT) everywhere the raw spot S used to appear. Set
  q = 0 and every formula collapses back to the classic Black-Scholes you know.

SCALING CONVENTIONS (state these out loud in an interview so nobody is surprised):
  * vega  is reported PER 1% vol move   -> raw dPrice/dsigma divided by 100.
  * rho   is reported PER 1% rate move  -> raw dPrice/dr     divided by 100.
  * theta is reported PER CALENDAR DAY  -> raw dPrice/dT (annual) divided by 365.
  * vanna, volga, charm scaling is documented on each function individually.

Every function is small and independently testable so each line is defensible.
"""

import math

# ---------------------------------------------------------------------------
# 1. NORMAL DISTRIBUTION HELPERS  (no scipy -- built from the standard library)
# ---------------------------------------------------------------------------

def norm_cdf(x):
    """Standard normal CDF  N(x) = P(Z <= x).

    Uses the exact identity  N(x) = 0.5 * (1 + erf(x / sqrt(2))).
    erf is the 'error function' shipped in Python's math module, so we need
    neither scipy nor a lookup table.
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x):
    """Standard normal PDF  n(x) = e^(-x^2/2) / sqrt(2*pi).

    This is the height of the bell curve; it appears in gamma, vega, theta and
    every second-order Greek below.
    """
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


# ---------------------------------------------------------------------------
# 2. THE d1 / d2 TERMS  (with continuous dividend yield q)
# ---------------------------------------------------------------------------

def d1_d2(S, K, T, r, sigma, q=0.0):
    """Return the (d1, d2) pair used everywhere in Black-Scholes-Merton.

    d1 = (ln(S/K) + (r - q + 0.5*sigma^2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    Intuition: d2 is (roughly) how many standard deviations in-the-money the
    option is in risk-neutral terms; N(d2) is the risk-neutral probability a call
    finishes ITM. d1 = d2 + sigma*sqrt(T); e^(-qT)*N(d1) is the call's delta.
    """
    if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
        raise ValueError("S, K, T, sigma must all be positive.")
    vol_time = sigma * math.sqrt(T)                       # one 'vol-time' unit
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / vol_time
    d2 = d1 - vol_time
    return d1, d2


# ---------------------------------------------------------------------------
# 3. BLACK-SCHOLES-MERTON PRICES
# ---------------------------------------------------------------------------
# Core idea: today's fair price = DISCOUNTED EXPECTED PAYOFF under the
# risk-neutral measure. With a dividend yield the spot leg carries e^(-qT).

def bs_price(S, K, T, r, sigma, option="call", q=0.0):
    """Black-Scholes-Merton price of a European option.

    Call = S*e^(-qT)*N(d1) - K*e^(-rT)*N(d2)
    Put  = K*e^(-rT)*N(-d2) - S*e^(-qT)*N(-d1)
    """
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    disc_S = S * math.exp(-q * T)        # spot discounted for dividends "leaked"
    disc_K = K * math.exp(-r * T)        # strike discounted back to today
    option = option.lower()
    if option == "call":
        # Long-stock exposure minus the present value of paying the strike.
        return disc_S * norm_cdf(d1) - disc_K * norm_cdf(d2)
    elif option == "put":
        # Symmetric formula on the left tail N(-d).
        return disc_K * norm_cdf(-d2) - disc_S * norm_cdf(-d1)
    raise ValueError("option must be 'call' or 'put'")


def put_call_parity_gap(S, K, T, r, q=0.0):
    """Return the theoretical value of C - P = S*e^(-qT) - K*e^(-rT).

    This is model-free: it must hold for ANY volatility or the market is
    arbitrageable. main.py uses it as a sanity check on the prices above.
    """
    return S * math.exp(-q * T) - K * math.exp(-r * T)


# ---------------------------------------------------------------------------
# 4. FIRST-ORDER GREEKS  (analytic closed forms, with q)
# ---------------------------------------------------------------------------

def greeks(S, K, T, r, sigma, option="call", q=0.0):
    """Return a dict of first-order Greeks for one option.

    Scaling (see module header): vega & rho per 1% move, theta per calendar day.
    """
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    disc_S = S * math.exp(-q * T)
    disc_K = K * math.exp(-r * T)
    pdf_d1 = norm_pdf(d1)
    sqrtT = math.sqrt(T)
    option = option.lower()

    # DELTA = dPrice/dSpot -- the hedge ratio. With dividends it carries e^(-qT).
    if option == "call":
        delta = math.exp(-q * T) * norm_cdf(d1)            # in (0, 1)
    else:
        delta = math.exp(-q * T) * (norm_cdf(d1) - 1.0)    # in (-1, 0)

    # GAMMA = dDelta/dSpot -- convexity of the position; identical for call & put.
    # High gamma => delta moves fast => you must re-hedge frequently.
    gamma = math.exp(-q * T) * pdf_d1 / (S * sigma * sqrtT)

    # VEGA (raw) = dPrice/dsigma -- identical for call & put. Reported per 1% vol.
    vega_raw = disc_S * pdf_d1 * sqrtT
    vega = vega_raw / 100.0

    # THETA = dPrice/dT -- time decay. Divide by 365 for a per-calendar-day number.
    term1 = -disc_S * pdf_d1 * sigma / (2.0 * sqrtT)       # decay of time value
    if option == "call":
        theta = (term1
                 - r * disc_K * norm_cdf(d2)
                 + q * disc_S * norm_cdf(d1)) / 365.0
    else:
        theta = (term1
                 + r * disc_K * norm_cdf(-d2)
                 - q * disc_S * norm_cdf(-d1)) / 365.0

    # RHO = dPrice/dr -- rate sensitivity, reported per 1% rate move.
    if option == "call":
        rho = disc_K * T * norm_cdf(d2) / 100.0
    else:
        rho = -disc_K * T * norm_cdf(-d2) / 100.0

    return {"Delta": delta, "Gamma": gamma, "Vega": vega,
            "Theta": theta, "Rho": rho}


# ---------------------------------------------------------------------------
# 5. SECOND-ORDER GREEKS  (why an options DESK cares -- see STUDY_GUIDE)
# ---------------------------------------------------------------------------
# These describe how the FIRST-order Greeks themselves move. A desk that is
# delta/vega-hedged today still bleeds if vol or time shifts its Greeks tomorrow;
# vanna/volga/charm quantify exactly that drift.

def second_order_greeks(S, K, T, r, sigma, option="call", q=0.0):
    """Return a dict with vanna, volga (vomma) and charm.

    SCALING (documented so it is defensible):
      * vanna : dDelta/dsigma = dVega/dSpot. RAW per 1.00 change in sigma, then
                divided by 100 so it reads 'delta change per 1% vol move'.
      * volga : dVega/dsigma (a.k.a. vomma). Built as vega * d1*d2/sigma using the
                RAW vega, then divided by 100^2 so it is consistent with our
                'per 1% vol' vega scaling (i.e. change in the reported vega per 1%
                vol move). Same for call & put.
      * charm : dDelta/dTime. Computed as the analytic dDelta/dt (calendar) and
                divided by 365 to read 'delta drift per calendar day'. The sign
                differs for calls vs puts; we return the standard dDelta/dt value.
    """
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    pdf_d1 = norm_pdf(d1)
    sqrtT = math.sqrt(T)
    disc_S = S * math.exp(-q * T)
    option = option.lower()

    # VANNA = -e^(-qT) * n(d1) * d2 / sigma.  How delta reacts to a vol move
    # (equivalently how vega reacts to spot). Per 1% vol -> divide by 100.
    vanna_raw = -math.exp(-q * T) * pdf_d1 * d2 / sigma
    vanna = vanna_raw / 100.0

    # VOLGA / VOMMA = vega_raw * d1*d2/sigma.  Convexity of the option in vol:
    # tells you how fast your vega itself grows as vol rises. Per 1% vol move on
    # the already-per-1% vega -> divide by 100 twice (100^2).
    vega_raw = disc_S * pdf_d1 * sqrtT
    volga = (vega_raw * d1 * d2 / sigma) / (100.0 * 100.0)

    # CHARM = dDelta/dt (a.k.a. delta decay). How your hedge drifts purely with
    # the passage of time -- critical near expiry and over weekends/holidays.
    # Standard closed form (with q); divide by 365 for a per-calendar-day figure.
    common = pdf_d1 * (2.0 * (r - q) * T - d2 * sigma * sqrtT) / (2.0 * T * sigma * sqrtT)
    if option == "call":
        charm_annual = q * math.exp(-q * T) * norm_cdf(d1) - math.exp(-q * T) * common
    else:
        charm_annual = -q * math.exp(-q * T) * norm_cdf(-d1) - math.exp(-q * T) * common
    charm = charm_annual / 365.0

    return {"Vanna": vanna, "Volga": volga, "Charm": charm}


def all_greeks(S, K, T, r, sigma, option="call", q=0.0):
    """Convenience: merge first- and second-order Greeks into one dict."""
    out = greeks(S, K, T, r, sigma, option, q)
    out.update(second_order_greeks(S, K, T, r, sigma, option, q))
    return out
