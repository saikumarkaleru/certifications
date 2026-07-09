"""
src.strategies -- an options-strategy payoff & risk toolkit.

Modules:
    bsm          : Black-Scholes-Merton pricing + Greeks (scipy-free).
    legs         : Leg / Position abstraction (every strategy = sum of legs).
    library      : 16 classic strategies built from Legs.
    analytics    : probability of profit, scenario grids, screener.
    market_data  : live/cache/synthetic market snapshots.
"""

from . import bsm, legs, library, analytics, market_data  # noqa: F401

__all__ = ["bsm", "legs", "library", "analytics", "market_data"]
