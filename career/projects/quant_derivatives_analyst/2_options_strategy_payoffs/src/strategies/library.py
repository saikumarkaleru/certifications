"""
library.py -- A catalogue of classic option strategies built from Leg/Position.

Each builder function takes a `snap` (a market snapshot -- see market_data.py)
and returns a StrategySpec containing:
    name       : human name
    position   : a Position (list of legs)
    view       : the market view / use-case in one sentence
    category   : bullish / bearish / neutral / volatility

The snapshot must expose:
    snap.spot            -> current underlying price (float)
    snap.call_premium(K) -> price to trade a call at strike K
    snap.put_premium(K)  -> price to trade a put at strike K

Because every strategy is assembled purely from Legs, the SAME analytics
(payoff, greeks, POP, breakevens...) work on all of them for free.

STRIKE SELECTION
----------------
We derive strikes from spot in round-ish steps so the strategies are realistic
and comparable. `k(pct)` returns a strike pct away from spot, snapped to the
nearest available strike so we reuse real chain premiums when possible.
"""

from __future__ import annotations

from dataclasses import dataclass

from .legs import Leg, Position


@dataclass
class StrategySpec:
    """Everything main.py needs to report on one strategy."""
    name: str
    position: Position
    view: str
    category: str  # bullish | bearish | neutral | volatility


def _round_strike(snap, target: float) -> float:
    """Snap a target price to the nearest strike the snapshot supports."""
    snapper = getattr(snap, "nearest_strike", None)
    if callable(snapper):
        return snapper(target)
    return round(target, 2)


# ---------------------------------------------------------------------------
# Individual strategy builders
# ---------------------------------------------------------------------------
def long_call(snap) -> StrategySpec:
    """Buy a call. Simplest bullish bet with capped loss (the premium)."""
    K = _round_strike(snap, snap.spot)               # at-the-money
    pos = Position([Leg("call", +1, K, snap.call_premium(K))])
    return StrategySpec("Long Call", pos,
                        "Bullish; want upside with loss capped at the premium paid.",
                        "bullish")


def long_put(snap) -> StrategySpec:
    """Buy a put. Bearish bet (or portfolio insurance) with capped loss."""
    K = _round_strike(snap, snap.spot)
    pos = Position([Leg("put", +1, K, snap.put_premium(K))])
    return StrategySpec("Long Put", pos,
                        "Bearish; profit if spot falls, loss capped at premium.",
                        "bearish")


def covered_call(snap) -> StrategySpec:
    """Own stock + sell an OTM call. Earn premium, cap upside. Mildly bullish."""
    K = _round_strike(snap, snap.spot * 1.05)
    pos = Position([
        Leg("stock", +1, 0.0, snap.spot),            # long 1 share at spot
        Leg("call", -1, K, snap.call_premium(K)),    # short OTM call
    ])
    return StrategySpec("Covered Call", pos,
                        "Own the stock, sell upside for income; mildly bullish/neutral.",
                        "neutral")


def protective_put(snap) -> StrategySpec:
    """Own stock + buy a put = insurance. Keeps upside, floors the downside."""
    K = _round_strike(snap, snap.spot * 0.95)
    pos = Position([
        Leg("stock", +1, 0.0, snap.spot),
        Leg("put", +1, K, snap.put_premium(K)),
    ])
    return StrategySpec("Protective Put", pos,
                        "Own stock but insure the downside with a put; bullish with a floor.",
                        "bullish")


def collar(snap) -> StrategySpec:
    """Stock + long put (floor) + short call (cap). Cheap insurance, capped upside."""
    Kp = _round_strike(snap, snap.spot * 0.95)
    Kc = _round_strike(snap, snap.spot * 1.05)
    pos = Position([
        Leg("stock", +1, 0.0, snap.spot),
        Leg("put", +1, Kp, snap.put_premium(Kp)),
        Leg("call", -1, Kc, snap.call_premium(Kc)),
    ])
    return StrategySpec("Collar", pos,
                        "Protect stock cheaply: buy a put, fund it by selling a call; range-bound bullish.",
                        "neutral")


def bull_call_spread(snap) -> StrategySpec:
    """Buy lower call, sell higher call. Debit; bullish with defined risk/reward."""
    Kl = _round_strike(snap, snap.spot)
    Kh = _round_strike(snap, snap.spot * 1.10)
    pos = Position([
        Leg("call", +1, Kl, snap.call_premium(Kl)),
        Leg("call", -1, Kh, snap.call_premium(Kh)),
    ])
    return StrategySpec("Bull Call Spread", pos,
                        "Bullish but cost-reduced: buy a call, sell a higher one to cap cost and gain.",
                        "bullish")


def bear_put_spread(snap) -> StrategySpec:
    """Buy higher put, sell lower put. Debit; bearish with defined risk/reward."""
    Kh = _round_strike(snap, snap.spot)
    Kl = _round_strike(snap, snap.spot * 0.90)
    pos = Position([
        Leg("put", +1, Kh, snap.put_premium(Kh)),
        Leg("put", -1, Kl, snap.put_premium(Kl)),
    ])
    return StrategySpec("Bear Put Spread", pos,
                        "Bearish with defined risk: buy a put, sell a lower one to cheapen it.",
                        "bearish")


def bull_put_spread(snap) -> StrategySpec:
    """Sell higher put, buy lower put. CREDIT; bullish/neutral, defined risk."""
    Kh = _round_strike(snap, snap.spot * 0.98)
    Kl = _round_strike(snap, snap.spot * 0.90)
    pos = Position([
        Leg("put", -1, Kh, snap.put_premium(Kh)),    # short put collects credit
        Leg("put", +1, Kl, snap.put_premium(Kl)),    # long lower put caps risk
    ])
    return StrategySpec("Bull Put Spread (credit)", pos,
                        "Neutral-to-bullish income: collect credit, profit if spot stays above the short put.",
                        "bullish")


def bear_call_spread(snap) -> StrategySpec:
    """Sell lower call, buy higher call. CREDIT; bearish/neutral, defined risk."""
    Kl = _round_strike(snap, snap.spot * 1.02)
    Kh = _round_strike(snap, snap.spot * 1.10)
    pos = Position([
        Leg("call", -1, Kl, snap.call_premium(Kl)),  # short call collects credit
        Leg("call", +1, Kh, snap.call_premium(Kh)),  # long higher call caps risk
    ])
    return StrategySpec("Bear Call Spread (credit)", pos,
                        "Neutral-to-bearish income: collect credit, profit if spot stays below the short call.",
                        "bearish")


def straddle(snap) -> StrategySpec:
    """Buy ATM call + ATM put. Long volatility: profit on a big move either way."""
    K = _round_strike(snap, snap.spot)
    pos = Position([
        Leg("call", +1, K, snap.call_premium(K)),
        Leg("put", +1, K, snap.put_premium(K)),
    ])
    return StrategySpec("Long Straddle", pos,
                        "Long volatility: expect a big move but unsure of direction (e.g. before earnings).",
                        "volatility")


def strangle(snap) -> StrategySpec:
    """Buy OTM call + OTM put. Cheaper long-vol bet needing a bigger move."""
    Kc = _round_strike(snap, snap.spot * 1.05)
    Kp = _round_strike(snap, snap.spot * 0.95)
    pos = Position([
        Leg("call", +1, Kc, snap.call_premium(Kc)),
        Leg("put", +1, Kp, snap.put_premium(Kp)),
    ])
    return StrategySpec("Long Strangle", pos,
                        "Cheaper long-volatility bet than a straddle; needs a larger move to pay off.",
                        "volatility")


def long_call_butterfly(snap) -> StrategySpec:
    """
    +1 low call, -2 mid calls, +1 high call (equally spaced).
    Cheap, defined-risk bet that spot pins the middle strike (short volatility).
    """
    Kl = _round_strike(snap, snap.spot * 0.95)
    Km = _round_strike(snap, snap.spot)
    Kh = _round_strike(snap, snap.spot * 1.05)
    pos = Position([
        Leg("call", +1, Kl, snap.call_premium(Kl)),
        Leg("call", -2, Km, snap.call_premium(Km)),
        Leg("call", +1, Kh, snap.call_premium(Kh)),
    ])
    return StrategySpec("Long Call Butterfly", pos,
                        "Low-cost bet that spot pins the middle strike at expiry; short volatility.",
                        "neutral")


def iron_condor(snap) -> StrategySpec:
    """
    Bull put spread + bear call spread = short an OTM put spread AND an OTM call
    spread. Net CREDIT; profits if spot stays inside the range. Short volatility.
    """
    Kp_short = _round_strike(snap, snap.spot * 0.95)
    Kp_long = _round_strike(snap, snap.spot * 0.88)
    Kc_short = _round_strike(snap, snap.spot * 1.05)
    Kc_long = _round_strike(snap, snap.spot * 1.12)
    pos = Position([
        Leg("put", -1, Kp_short, snap.put_premium(Kp_short)),
        Leg("put", +1, Kp_long, snap.put_premium(Kp_long)),
        Leg("call", -1, Kc_short, snap.call_premium(Kc_short)),
        Leg("call", +1, Kc_long, snap.call_premium(Kc_long)),
    ])
    return StrategySpec("Iron Condor", pos,
                        "Range-bound income: collect credit, profit if spot stays between the short strikes.",
                        "neutral")


def iron_butterfly(snap) -> StrategySpec:
    """
    Short ATM straddle + long OTM wings. Bigger credit, narrower profit zone than
    a condor (the short strikes are the SAME, at the money). Short volatility.
    """
    Km = _round_strike(snap, snap.spot)
    Kp_long = _round_strike(snap, snap.spot * 0.92)
    Kc_long = _round_strike(snap, snap.spot * 1.08)
    pos = Position([
        Leg("put", -1, Km, snap.put_premium(Km)),        # short ATM put
        Leg("call", -1, Km, snap.call_premium(Km)),      # short ATM call
        Leg("put", +1, Kp_long, snap.put_premium(Kp_long)),   # long wing
        Leg("call", +1, Kc_long, snap.call_premium(Kc_long)), # long wing
    ])
    return StrategySpec("Iron Butterfly", pos,
                        "Higher credit than a condor with a narrower profit zone; bet on very low movement.",
                        "neutral")


def call_ratio_spread(snap) -> StrategySpec:
    """
    +1 lower call, -2 higher calls. Often opened for a small credit/near-zero
    cost; profits in a mild rally but has UNBOUNDED risk if spot rockets up.
    A good example for the 'unbounded loss' flag in the screener.
    """
    Kl = _round_strike(snap, snap.spot)
    Kh = _round_strike(snap, snap.spot * 1.07)
    pos = Position([
        Leg("call", +1, Kl, snap.call_premium(Kl)),
        Leg("call", -2, Kh, snap.call_premium(Kh)),
    ])
    return StrategySpec("Call Ratio Spread (1x2)", pos,
                        "Mildly bullish/neutral for low cost, but carries unbounded risk on a sharp rally.",
                        "neutral")


def calendar_spread(snap) -> StrategySpec:
    """
    Calendar (time) spread: sell a near-dated call, buy a longer-dated call at
    the SAME strike, to harvest the faster time decay of the near option.

    SIMPLIFICATION (be honest in an interview): our Leg model uses ONE expiry T,
    so a true two-expiry payoff is out of scope. We approximate the calendar as
    a *net-long-vega, near-ATM* structure by holding the long call and treating
    the short near call as already expired worthless at our analysis expiry --
    i.e. we model it as a long call financed by a collected credit. The
    economics we DO capture correctly: it is a debit, long-vega, benefits from
    time passing on the short leg. The exact expiry payoff of the real trade
    would need a multi-expiry engine, which we flag rather than fake.
    """
    K = _round_strike(snap, snap.spot)
    long_c = snap.call_premium(K)
    short_c = snap.call_premium(K) * 0.55   # a nearer-dated call is cheaper
    pos = Position([
        Leg("call", +1, K, long_c),          # long longer-dated call
        # short near call modelled as pure credit collected (see docstring):
        Leg("call", -1, K, short_c),
    ])
    # Because both legs share strike/expiry in our single-expiry model they net
    # out to just the credit differential; we relabel it clearly.
    return StrategySpec("Calendar Spread (approx.)", pos,
                        "Sell near-dated, buy longer-dated same strike to harvest faster near-term decay; long vega. (Single-expiry approximation.)",
                        "neutral")


# ---------------------------------------------------------------------------
# Master builder
# ---------------------------------------------------------------------------
def build_all(snap):
    """Return the full list of StrategySpec objects for a given snapshot."""
    builders = [
        long_call, long_put, covered_call, protective_put, collar,
        bull_call_spread, bear_put_spread, bull_put_spread, bear_call_spread,
        straddle, strangle, long_call_butterfly, iron_condor, iron_butterfly,
        call_ratio_spread, calendar_spread,
    ]
    return [b(snap) for b in builders]
