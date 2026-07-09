"""
legs.py -- The Leg / Position abstraction that the whole project is built on.

THE BIG IDEA (say this in an interview)
---------------------------------------
Every option strategy -- no matter how fancy the name (iron condor, butterfly,
collar) -- is just a *sum of simple legs*. A leg is one contract you either buy
or sell. If you can price and risk one leg, you can price and risk any strategy
by adding the legs up. That is the entire trick and it is why this file is the
heart of the codebase.

A Leg is described by four numbers:
    kind    : "call", "put" or "stock"
    strike  : the strike price K (ignored for stock)
    qty     : signed quantity. +1 = long (you bought), -1 = short (you sold).
              Fractions/multiples are allowed (e.g. -2 = short two contracts).
    premium : the price you paid/received PER UNIT for the option. For a stock
              leg this is the entry (purchase) price of the share.

A Position is just a list of Legs plus the analytics a desk cares about:
payoff at expiry, value/P&L before expiry (via BSM), net Greeks, breakevens,
max profit / max loss, and the net debit or credit.

All P&L is expressed on a *per-share* basis (1 contract = 1 share here) to keep
the maths transparent; multiply by the contract multiplier (e.g. 100, or a lot
size) outside if you want dollar figures.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

import numpy as np

from . import bsm


# ---------------------------------------------------------------------------
# A single leg
# ---------------------------------------------------------------------------
@dataclass
class Leg:
    """One tradable contract. See module docstring for the field meanings."""
    kind: str          # "call", "put" or "stock"
    qty: float         # signed: +long / -short
    strike: float = 0.0
    premium: float = 0.0  # price paid (long) or received (short) per unit

    def intrinsic(self, S):
        """
        Value of this leg's underlying instrument at expiry for spot S.
        (This is the value BEFORE subtracting what we paid for it.)
          call  -> max(S - K, 0)
          put   -> max(K - S, 0)
          stock -> S            (a share is simply worth the spot price)
        Works for a scalar S or a numpy array of spots.
        """
        S = np.asarray(S, dtype=float)
        if self.kind == "call":
            return np.maximum(S - self.strike, 0.0)
        if self.kind == "put":
            return np.maximum(self.strike - S, 0.0)
        if self.kind == "stock":
            return S
        raise ValueError(f"unknown leg kind: {self.kind}")

    def payoff_at_expiry(self, S):
        """
        P&L of this leg at expiry:  qty * intrinsic  -  qty * entry_cost.

        The entry cost is `premium` for an option and the purchase price
        (`premium`) for a stock. Because qty is signed this is automatically
        correct for shorts: a short call has qty<0, so `- qty*premium` becomes
        a POSITIVE number -- the credit you collected up front.
        """
        entry_cost = self.premium  # per unit
        return self.qty * self.intrinsic(S) - self.qty * entry_cost

    def entry_cashflow(self) -> float:
        """
        Cash you pay (negative) or receive (positive) to OPEN this leg.
        Long anything => you pay => negative cash. Short => you receive =>
        positive cash. Summed across legs this gives net debit/credit.
        """
        return -self.qty * self.premium

    def value_before_expiry(self, S, T, r, sigma, q):
        """
        Mark-to-market value of the leg at time-to-expiry T > 0 using BSM for
        options (stock is just worth S). Returns qty * per-unit model value.
        """
        S = np.asarray(S, dtype=float)
        if self.kind == "stock":
            return self.qty * S
        if self.kind == "call":
            vals = np.array([bsm.price_call(float(s), self.strike, T, r, sigma, q) for s in S.ravel()])
        else:  # put
            vals = np.array([bsm.price_put(float(s), self.strike, T, r, sigma, q) for s in S.ravel()])
        return self.qty * vals.reshape(S.shape)

    def greeks(self, S, T, r, sigma, q):
        """
        Position-weighted Greeks for this leg at a single spot S.
        Stock: delta = qty (one share has delta 1), all other Greeks 0.
        Options: BSM Greeks * qty.
        """
        if self.kind == "stock":
            return bsm.Greeks(delta=self.qty, gamma=0.0, vega=0.0, theta=0.0)
        g = bsm.greeks(float(S), self.strike, T, r, sigma, q, kind=self.kind)
        return bsm.Greeks(
            delta=self.qty * g.delta,
            gamma=self.qty * g.gamma,
            vega=self.qty * g.vega,
            theta=self.qty * g.theta,
        )


# ---------------------------------------------------------------------------
# A position = a collection of legs
# ---------------------------------------------------------------------------
@dataclass
class Position:
    """
    A full strategy: a list of legs plus analytics. Every method simply loops
    over the legs and sums -- proving the "strategy = sum of legs" idea.
    """
    legs: List[Leg] = field(default_factory=list)

    # --- expiry-time analytics ------------------------------------------
    def payoff_at_expiry(self, S):
        """Total strategy P&L at expiry = sum of each leg's expiry P&L."""
        S = np.asarray(S, dtype=float)
        total = np.zeros_like(S)
        for leg in self.legs:
            total = total + leg.payoff_at_expiry(S)
        return total

    def net_debit_credit(self) -> float:
        """
        Net cash to open the position (sum of leg entry cashflows).
          negative  -> net DEBIT  (you paid to put it on)
          positive  -> net CREDIT (you were paid to put it on)
        """
        return sum(leg.entry_cashflow() for leg in self.legs)

    # --- before-expiry analytics (uses BSM) -----------------------------
    def value_before_expiry(self, S, T, r, sigma, q):
        """Mark-to-market value of the whole position at time-to-expiry T."""
        S = np.asarray(S, dtype=float)
        total = np.zeros_like(S)
        for leg in self.legs:
            total = total + leg.value_before_expiry(S, T, r, sigma, q)
        return total

    def pnl_before_expiry(self, S, T, r, sigma, q):
        """
        P&L if we marked the position today (time-to-expiry T):
            current model value  -  cost we paid to open.

        Cost paid = -net_debit_credit (a debit is money out, i.e. cost > 0).
        This produces the SMOOTH/curved P&L line, versus the KINKED expiry
        payoff -- the difference between the two curves is time value.
        """
        cost_paid = -self.net_debit_credit()
        return self.value_before_expiry(S, T, r, sigma, q) - cost_paid

    # --- risk -----------------------------------------------------------
    def net_greeks(self, S, T, r, sigma, q) -> bsm.Greeks:
        """Net position Greeks = sum of per-leg Greeks at spot S."""
        d = g = v = t = 0.0
        for leg in self.legs:
            lg = leg.greeks(S, T, r, sigma, q)
            d += lg.delta
            g += lg.gamma
            v += lg.vega
            t += lg.theta
        return bsm.Greeks(delta=d, gamma=g, vega=v, theta=t)

    # --- summary statistics over a spot grid ----------------------------
    def _grid(self, S_ref: float, width: float = 0.6, n: int = 801):
        """
        Build a dense spot grid centred on S_ref spanning +/- `width` (fraction)
        so max/min and breakeven searches are accurate. Widened enough to
        capture profit tails of wide strategies.
        """
        lo = max(0.01, S_ref * (1.0 - width))
        hi = S_ref * (1.0 + width)
        return np.linspace(lo, hi, n)

    def breakevens(self, S_ref: float):
        """
        Spot prices where the expiry P&L crosses zero, found by detecting sign
        changes on a dense grid and linearly interpolating each crossing.
        Returns a sorted list (may be empty, one, or several).
        """
        S = self._grid(S_ref)
        y = self.payoff_at_expiry(S)
        bes = []
        for i in range(len(S) - 1):
            y0, y1 = y[i], y[i + 1]
            if y0 == 0.0:
                bes.append(float(S[i]))
            elif y0 * y1 < 0.0:  # sign change between grid points
                # linear interpolation for the zero crossing
                x = S[i] - y0 * (S[i + 1] - S[i]) / (y1 - y0)
                bes.append(float(x))
        # de-duplicate near-identical crossings
        out = []
        for b in sorted(bes):
            if not out or abs(b - out[-1]) > 1e-6:
                out.append(b)
        return out

    def max_profit_loss(self, S_ref: float):
        """
        Max profit and max loss over the spot grid, with a flag for when the
        payoff is (practically) unbounded because a naked long option keeps
        gaining as spot runs away from the grid edge.

        Returns dict: {max_profit, max_loss, profit_unbounded, loss_unbounded}.
        We detect "unbounded" by checking whether the P&L is still climbing at
        the grid edges (slope non-trivial), which flags naked long calls/puts.
        """
        S = self._grid(S_ref, width=0.9)
        y = self.payoff_at_expiry(S)
        max_profit = float(np.max(y))
        max_loss = float(np.min(y))

        # Edge slope test for unbounded tails.
        left_slope = (y[1] - y[0]) / (S[1] - S[0])
        right_slope = (y[-1] - y[-2]) / (S[-1] - S[-2])
        # A meaningful slope at the edge => payoff keeps growing beyond grid.
        profit_unbounded = right_slope > 1e-3 and y[-1] >= max_profit - 1e-6
        loss_unbounded = left_slope < -1e-3 and y[0] <= max_loss + 1e-6
        # Long put profits as spot -> 0 (left edge rising as S falls):
        if left_slope < -1e-3 and y[0] >= max_profit - 1e-6:
            profit_unbounded = True

        return {
            "max_profit": max_profit,
            "max_loss": max_loss,
            "profit_unbounded": bool(profit_unbounded),
            "loss_unbounded": bool(loss_unbounded),
        }

    def describe_legs(self) -> str:
        """Human-readable one-line description of the legs, e.g. '+1 C100'."""
        parts = []
        for leg in self.legs:
            sign = "+" if leg.qty > 0 else ""
            if leg.kind == "stock":
                parts.append(f"{sign}{leg.qty:g} stock@{leg.premium:g}")
            else:
                code = "C" if leg.kind == "call" else "P"
                parts.append(f"{sign}{leg.qty:g} {code}{leg.strike:g}@{leg.premium:g}")
        return ", ".join(parts)
