"""
analytics.py -- Probability of Profit (POP), scenario grids, and the screener.

These are the tools that turn a payoff diagram into a *decision*. A trader does
not just want to see the shape of a P&L curve -- they want to know:
  * How LIKELY am I to make money?      -> probability_of_profit
  * What happens if spot AND vol move?  -> scenario_grid
  * Which strategy has the best deal?   -> screen_strategies
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from . import bsm


# ---------------------------------------------------------------------------
# Probability of Profit from the lognormal distribution of S_T
# ---------------------------------------------------------------------------
def probability_of_profit(spec, spot, T, r, sigma, q) -> float:
    """
    Probability that the strategy finishes with P&L > 0 at expiry.

    ASSUMPTIONS (an interviewer WILL ask -- state them):
      1. Under Black-Scholes the terminal price S_T is LOGNORMAL. Equivalently
         ln(S_T) ~ Normal(mean = ln S0 + (mu - sigma^2/2) T, std = sigma*sqrt(T)).
      2. We use the RISK-NEUTRAL drift mu = r - q. This is the simplest
         defensible choice: it is internally consistent with the same BSM model
         used to price the legs. (A real desk might instead plug in a real-world
         drift or just their own view; that only changes the drift term.)

    METHOD:
      * Find the expiry breakevens (spots where P&L crosses zero).
      * The profit region is the union of spot intervals where P&L > 0.
      * Integrate the lognormal density over those intervals using the normal
        CDF of ln(S_T). We sample the sign of P&L in each interval BETWEEN
        consecutive breakevens (plus the two open tails) to decide profit/loss,
        then sum the probability mass of the profitable intervals.

    Returns a probability in [0, 1].
    """
    # Boundaries of the profit/loss regions: 0, each breakeven, +infinity.
    bes = spec.position.breakevens(spot)
    # Build interval edges including the tails.
    edges = [0.0] + bes + [math.inf]

    # Lognormal parameters for ln(S_T).
    mu = (r - q - 0.5 * sigma * sigma) * T
    m = math.log(spot) + mu             # mean of ln(S_T)
    s = sigma * math.sqrt(T)            # std of ln(S_T)

    def lncdf(x):
        """P(S_T <= x) for the lognormal terminal price."""
        if x <= 0:
            return 0.0
        if math.isinf(x):
            return 1.0
        return bsm.norm_cdf((math.log(x) - m) / s)

    total = 0.0
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        # Representative spot inside the interval to test profitability.
        if math.isinf(hi):
            mid = lo * 1.5 + 1.0
        else:
            mid = 0.5 * (lo + hi)
        pnl = float(spec.position.payoff_at_expiry(np.array([mid]))[0])
        if pnl > 0:
            total += lncdf(hi) - lncdf(lo)
    return max(0.0, min(1.0, total))


# ---------------------------------------------------------------------------
# Scenario grid: P&L across a spot x volatility matrix (before expiry)
# ---------------------------------------------------------------------------
def scenario_grid(spec, spot, T, r, sigma, q,
                  spot_moves=(-0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15),
                  vol_mults=(0.7, 1.0, 1.3)):
    """
    Build a P&L matrix showing how the strategy performs if, at time-to-expiry
    T, spot has moved by each `spot_moves` fraction AND implied vol is scaled by
    each `vol_mults` factor. This is the classic "risk board" a desk stares at.

    Returns (spots, vols, matrix) where matrix[i, j] is the before-expiry P&L
    at spots[j] and vols[i].
    """
    spots = np.array([spot * (1.0 + m) for m in spot_moves])
    vols = np.array([sigma * v for v in vol_mults])
    matrix = np.zeros((len(vols), len(spots)))
    for i, v in enumerate(vols):
        matrix[i, :] = spec.position.pnl_before_expiry(spots, T, r, v, q)
    return spots, vols, matrix


# ---------------------------------------------------------------------------
# Cross-strategy screener
# ---------------------------------------------------------------------------
@dataclass
class ScreenRow:
    """One row of the screener output."""
    name: str
    category: str
    net_cd: float           # net debit(-)/credit(+)
    max_profit: float
    max_loss: float
    risk_reward: float      # max_profit / |max_loss|  (nan if unbounded)
    pop: float              # probability of profit [0,1]
    note: str               # e.g. 'unbounded loss'


def screen_strategies(specs, spot, T, r, sigma, q):
    """
    Rank all strategies on two headline numbers a desk cares about:
        risk/reward = max_profit / |max_loss|   (higher = more reward per unit risk)
        POP         = probability of profit

    We compute a simple combined score = risk_reward_capped * POP so that a
    strategy needs BOTH a decent payoff ratio AND a decent chance of working to
    rank highly. Unbounded-loss strategies are flagged and pushed down (their
    risk/reward is undefined / treated as very poor).

    Returns a list of ScreenRow sorted best-first.
    """
    rows = []
    for spec in specs:
        pos = spec.position
        stats = pos.max_profit_loss(spot)
        mp, ml = stats["max_profit"], stats["max_loss"]
        note = ""
        if stats["profit_unbounded"]:
            note = "unbounded profit"
        if stats["loss_unbounded"]:
            note = (note + "; " if note else "") + "unbounded loss"

        # Risk/reward ratio. Undefined if loss is (near) zero or unbounded.
        if stats["loss_unbounded"] or ml >= -1e-9:
            rr = float("nan")
        else:
            rr = mp / abs(ml)

        pop = probability_of_profit(spec, spot, T, r, sigma, q)
        rows.append(ScreenRow(
            name=spec.name, category=spec.category,
            net_cd=pos.net_debit_credit(),
            max_profit=mp, max_loss=ml,
            risk_reward=rr, pop=pop, note=note,
        ))

    def score(row: ScreenRow) -> float:
        # Cap risk/reward at 5 so one lottery-ticket ratio doesn't dominate.
        rr = row.risk_reward
        if math.isnan(rr):
            rr_capped = 0.0            # unbounded-loss trades score poorly here
        else:
            rr_capped = min(rr, 5.0)
        return rr_capped * row.pop

    rows.sort(key=score, reverse=True)
    return rows
