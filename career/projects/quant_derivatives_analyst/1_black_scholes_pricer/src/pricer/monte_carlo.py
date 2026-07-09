"""
monte_carlo.py  --  risk-neutral Monte-Carlo pricer for European options
========================================================================

THE IDEA (interview one-liner):
  Black-Scholes says price = e^(-rT) * E[payoff] under the risk-neutral measure.
  Monte-Carlo just DOES that expectation by brute force: simulate thousands of
  terminal prices, average the payoffs, discount. As the number of paths grows,
  the average converges to the true expectation (Law of Large Numbers).

THE MODEL (Geometric Brownian Motion, exact one-step to maturity):
  S_T = S * exp( (r - q - 0.5*sigma^2) * T  +  sigma*sqrt(T) * Z ),  Z ~ N(0,1)
  We only need S_T (not the whole path) because the payoff is European.

VARIANCE REDUCTION -- ANTITHETIC VARIATES:
  For each random draw Z we ALSO use -Z. Because the two are negatively
  correlated, averaging their payoffs cancels part of the sampling noise, so the
  standard error shrinks for the same number of random numbers. Cheap and always
  valid for a monotone-ish payoff.

We also return the STANDARD ERROR so we can state a confidence band and check
that BSM sits inside it -- that's how we prove the three pricers agree.
"""

import math
import numpy as np


def mc_price(S, K, T, r, sigma, option="call", q=0.0,
             n_paths=200_000, antithetic=True, seed=None):
    """Monte-Carlo price of a European option under risk-neutral GBM.

    Returns (price, standard_error). Set `seed` for reproducibility.
    """
    option = option.lower()
    rng = np.random.default_rng(seed)          # modern, seedable NumPy generator

    if antithetic:
        # Draw half the normals, then mirror them (Z and -Z) so the sample mean
        # of the shocks is exactly zero -- this is the variance reduction.
        half = n_paths // 2
        z = rng.standard_normal(half)
        z = np.concatenate([z, -z])
    else:
        z = rng.standard_normal(n_paths)

    drift = (r - q - 0.5 * sigma * sigma) * T   # deterministic part of log-return
    diffusion = sigma * math.sqrt(T) * z        # random shock, scaled by vol-time
    ST = S * np.exp(drift + diffusion)          # simulated terminal prices

    if option == "call":
        payoff = np.maximum(ST - K, 0.0)
    else:
        payoff = np.maximum(K - ST, 0.0)

    disc_payoff = math.exp(-r * T) * payoff     # discount each payoff to today
    price = disc_payoff.mean()                  # Monte-Carlo estimate of the price

    # Standard error of the mean = sample_std / sqrt(n). It tells us how tight the
    # estimate is; a 95% band is roughly price +/- 1.96 * std_error.
    std_error = disc_payoff.std(ddof=1) / math.sqrt(len(disc_payoff))
    return price, std_error
