"""
pricer -- a small, fully-explainable options analytics package.

Modules:
  black_scholes : BSM prices + first/second-order Greeks (with dividend yield q)
  implied_vol   : Newton-Raphson IV solver with bisection fallback
  binomial      : Cox-Ross-Rubinstein tree (European AND American)
  monte_carlo   : risk-neutral GBM Monte-Carlo with antithetic variates
  market_data   : live option chain via yfinance, with offline fallback
  validation    : analytic Greeks vs finite differences

Everything is re-exported here so callers can do e.g.
    from pricer import bs_price, implied_vol, crr_price, mc_price
"""

from .black_scholes import (
    norm_cdf, norm_pdf, d1_d2, bs_price, put_call_parity_gap,
    greeks, second_order_greeks, all_greeks,
)
from .implied_vol import implied_vol
from .binomial import crr_price
from .monte_carlo import mc_price
from .market_data import get_option_chain
from .validation import validate_greeks

__all__ = [
    "norm_cdf", "norm_pdf", "d1_d2", "bs_price", "put_call_parity_gap",
    "greeks", "second_order_greeks", "all_greeks",
    "implied_vol", "crr_price", "mc_price",
    "get_option_chain", "validate_greeks",
]
