# Chapter 63: Building a Payoff & Strategy Analyzer

Every screenshot of a payoff diagram in this book — the kinked hockey stick of a long call, the tent of a short straddle, the flat-topped table of an iron condor — came out of a small piece of software. You do not draw those curves by hand; you describe a strategy as a few numbers and let code compute the rest. In this chapter you will build that exact tool. By the end you will have a compact Python program that takes *any* options strategy, expressed as a list of **legs**, and tells you its payoff at expiry, its breakeven points, its maximum profit and loss, its net Greeks, its profit-and-loss *before* expiry, the probability that it makes money, and a clean matplotlib chart of the whole thing.

The big idea is **representation**. If you can find one honest way to describe every strategy in the book, then a single set of functions can analyze all of them — bull call spread, straddle, iron condor, ratio spread, covered call — without special-casing any of them. That one representation is a list of legs, where a leg is just `(instrument type, strike, signed quantity, premium)`. This is precisely how a real options-analytics desk models risk: positions are rows in a table, and the analytics are functions over that table. We are building a miniature version of the systems that power broker strategy-builders and risk dashboards.

## Core concepts

### The leg: the atom of every strategy

A **leg** is one line of a trade. A bull call spread has two legs; an iron condor has four. Each leg needs exactly four facts:

- **Kind** — is it a `"call"`, a `"put"`, or `"stock"` (the underlying itself, used for covered calls and synthetics)?
- **Strike (K)** — the price at which the option can be exercised. (Stock legs ignore this.)
- **Quantity (qty)** — a *signed* number. **Positive means long (you bought it), negative means short (you sold it).** This single sign convention is what makes the math collapse to simple sums.
- **Premium** — the price paid or received *per unit* when you opened the leg. You always pay to go long and receive to go short, but we store premium as a plain positive number and let the sign of `qty` handle the cash direction.

In Python a dataclass captures this cleanly:

```python
from dataclasses import dataclass

@dataclass
class Leg:
    kind: str        # "call", "put", or "stock"
    strike: float    # exercise price (ignored for stock)
    qty: float       # +long, -short  (e.g. +1 bought, -2 sold two)
    premium: float   # price per unit paid (long) or received (short)
```

That is the entire data model. Everything else is functions that read a `list[Leg]`.

### Payoff at expiry: intrinsic value minus what you paid

At expiry, time value is gone and each option is worth only its **intrinsic value**: a call is worth `max(S - K, 0)`, a put is worth `max(K - S, 0)`, where `S` is the spot price of Nifty on expiry day. Stock is simply worth `S`.

The profit on one leg is *what it is worth at expiry* minus *what it cost you to get in*, scaled by the signed quantity:

`leg P&L = qty * (value_at_expiry(S) - premium)`

Read the sign carefully. If you are **long** (`qty = +1`) you paid the premium, so you subtract it; that matches `+1 * (value - premium)`. If you are **short** (`qty = -1`) you *received* the premium, and `-1 * (value - premium) = premium - value` — you keep the premium and pay out the option's value. The one formula handles both directions, which is the whole point of the signed convention. The strategy's payoff is just the sum over legs:

`strategy P&L(S) = sum over legs of qty * (value(S) - premium)`

### Breakeven, max profit, max loss — read them off the grid

Once you can compute the payoff at a single price, compute it across a **grid** of prices (say every point from 0.5x to 1.5x of spot). Then:

- **Breakevens** are the prices where the payoff curve crosses zero. We find them by scanning the grid for sign changes and interpolating.
- **Max profit** is the highest point on the curve; **max loss** is the lowest. For defined-risk strategies (spreads, condors) these are real finite numbers. For naked short options the true max loss is unbounded, and our grid will only show the worst case *within the grid* — a limitation worth remembering and one we will flag honestly.

### Net Greeks: sum the per-leg Greeks from the pricing engine

In Chapter 62 you built a Black-Scholes engine that returns the price and Greeks (delta, gamma, theta, vega, rho) of a single option. Because every Greek is a rate of change and rates of change add, the strategy's Greeks are the **signed sum** of its legs' Greeks:

`strategy delta = sum over legs of qty * leg_delta`

and likewise for gamma, theta, and vega. This tells you the live risk of the package *today*: which way it leans, how fast it bleeds to the clock, and how it reacts to a change in India VIX.

### Before-expiry P&L: price the legs with Black-Scholes

The expiry payoff is the destination, but most trades are managed *before* expiry, when options still carry time value. To draw the "P&L now" curve, you re-price every leg with Black-Scholes at each spot on the grid, for the *current* time to expiry, and compare to what you paid:

`leg value now = qty * (BS_price(S, K, T_now, sigma) - premium)`

Plotting this smooth curve against the kinked expiry curve is exactly the long-call "now vs expiry" figure from Chapter 11 — the gap between them *is* the time value you still hold.

### Probability of profit: a lognormal terminal distribution

A payoff curve tells you *what* happens at each price but not *how likely* each price is. The standard model assumes the terminal price is **lognormal** — equivalently, the log-return is normal with standard deviation `sigma * sqrt(T)`. The probability of profit (POP) is then the total probability mass sitting over the price regions where the payoff is positive. We estimate it by weighting each grid point by the lognormal probability density and summing the weights where P&L > 0. (POP is *not* the same as expected value or a good trade — a strategy can have 90% POP and still be a loser if the 10% tail is brutal. We will say this plainly.)

## Building the tool (runnable Python)

First, the Black-Scholes engine — a trimmed version of the Chapter 62 code, using `math.erf` so it needs nothing but the standard library.

```python
import math

def _norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def _norm_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

def bs_price(kind, S, K, T, sigma, r=0.065):
    """Black-Scholes price of a European call/put. r ~ 6.5% Indian rate."""
    if T <= 0:                       # at/after expiry -> intrinsic value
        return max(S - K, 0.0) if kind == "call" else max(K - S, 0.0)
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if kind == "call":
        return S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)
    else:
        return K * math.exp(-r * T) * _norm_cdf(-d2) - S * _norm_cdf(-d1)

def bs_greeks(kind, S, K, T, sigma, r=0.065):
    """Per-unit Greeks. theta is per-day; vega is per 1 vol point (1%)."""
    if T <= 0:
        return {"delta": 0.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0}
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    gamma = _norm_pdf(d1) / (S * sigma * math.sqrt(T))
    vega  = S * _norm_pdf(d1) * math.sqrt(T) / 100.0          # per 1% vol
    if kind == "call":
        delta = _norm_cdf(d1)
        theta = (-S * _norm_pdf(d1) * sigma / (2 * math.sqrt(T))
                 - r * K * math.exp(-r * T) * _norm_cdf(d2)) / 365.0
    else:
        delta = _norm_cdf(d1) - 1.0
        theta = (-S * _norm_pdf(d1) * sigma / (2 * math.sqrt(T))
                 + r * K * math.exp(-r * T) * _norm_cdf(-d2)) / 365.0
    return {"delta": delta, "gamma": gamma, "theta": theta, "vega": vega}
```

Now the leg-level functions: value at expiry, and the whole-strategy payoff over a grid.

```python
def leg_intrinsic(leg, S):
    """Value of one unit of the leg at expiry, given spot S."""
    if leg.kind == "call":
        return max(S - leg.strike, 0.0)
    elif leg.kind == "put":
        return max(leg.strike - S, 0.0)
    elif leg.kind == "stock":
        return S
    raise ValueError(f"unknown kind {leg.kind}")

def payoff_at_expiry(legs, S):
    """Net P&L of the strategy at expiry price S."""
    return sum(leg.qty * (leg_intrinsic(leg, S) - leg.premium) for leg in legs)

def price_grid(legs, spot, lo=0.5, hi=1.5, n=601):
    """Build a price grid spanning lo*spot .. hi*spot."""
    step = (hi - lo) * spot / (n - 1)
    return [lo * spot + i * step for i in range(n)]
```

The summary statistics — breakevens, max profit, max loss — read straight off the grid:

```python
def analyze(legs, spot, lot_size=75):
    """Return payoff stats scaled to one lot (rupees per lot)."""
    grid = price_grid(legs, spot)
    pnl = [payoff_at_expiry(legs, S) for S in grid]

    # breakevens: linear-interpolate every zero crossing
    breakevens = []
    for i in range(1, len(grid)):
        if pnl[i - 1] == 0.0:
            breakevens.append(grid[i - 1])
        elif pnl[i - 1] * pnl[i] < 0:          # sign change between i-1 and i
            f = pnl[i - 1] / (pnl[i - 1] - pnl[i])
            breakevens.append(grid[i - 1] + f * (grid[i] - grid[i - 1]))

    net_premium = -sum(leg.qty * leg.premium for leg in legs)  # +credit / -debit
    return {
        "breakevens": [round(b, 1) for b in breakevens],
        "max_profit_per_lot": round(max(pnl) * lot_size, 0),
        "max_loss_per_lot":   round(min(pnl) * lot_size, 0),
        "net_premium_per_unit": round(net_premium, 2),
        "grid": grid, "pnl": pnl,
    }
```

Net Greeks sum the per-leg Greeks from the engine (stock contributes delta 1, no convexity):

```python
def net_greeks(legs, spot, T, sigma, r=0.065):
    total = {"delta": 0.0, "gamma": 0.0, "theta": 0.0, "vega": 0.0}
    for leg in legs:
        if leg.kind == "stock":
            total["delta"] += leg.qty * 1.0
            continue
        g = bs_greeks(leg.kind, spot, leg.strike, T, sigma, r)
        for k in total:
            total[k] += leg.qty * g[k]
    return {k: round(v, 4) for k, v in total.items()}

def pnl_now(legs, S, T, sigma, r=0.065):
    """Mark-to-market P&L of the strategy at spot S, T years to expiry."""
    out = 0.0
    for leg in legs:
        val = S if leg.kind == "stock" else bs_price(leg.kind, S, leg.strike, T, sigma, r)
        out += leg.qty * (val - leg.premium)
    return out
```

Probability of profit under a lognormal terminal distribution:

```python
def prob_of_profit(legs, spot, T, sigma, r=0.065):
    """Lognormal-weighted probability that expiry P&L > 0."""
    grid = price_grid(legs, spot, n=2001)
    mu = math.log(spot) + (r - 0.5 * sigma**2) * T   # drift of log-price
    sd = sigma * math.sqrt(T)
    prob, dens_sum = 0.0, 0.0
    for S in grid:
        if S <= 0:
            continue
        # lognormal density of terminal price S
        dens = _norm_pdf((math.log(S) - mu) / sd) / (S * sd)
        dens_sum += dens
        if payoff_at_expiry(legs, S) > 0:
            prob += dens
    return prob / dens_sum          # normalise the discretised mass
```

### A small strategy library

These builders return ready-made leg lists. Notice each is just a few `Leg`s — the analyzer never changes.

```python
def bull_call_spread(K_long, K_short, prem_long, prem_short):
    return [Leg("call", K_long,  +1, prem_long),
            Leg("call", K_short, -1, prem_short)]

def long_straddle(K, call_prem, put_prem):
    return [Leg("call", K, +1, call_prem),
            Leg("put",  K, +1, put_prem)]

def iron_condor(put_buy, put_sell, call_sell, call_buy,
                p_buy, p_sell, c_sell, c_buy):
    """Sell the inner put+call, buy the outer wings. Net credit."""
    return [Leg("put",  put_buy,   +1, p_buy),    # long put wing  (lower)
            Leg("put",  put_sell,  -1, p_sell),   # short put
            Leg("call", call_sell, -1, c_sell),   # short call
            Leg("call", call_buy,  +1, c_buy)]    # long call wing (upper)
```

### Plotting the payoff diagram

The plot function draws the expiry payoff, the before-expiry curve, the zero line, breakevens, and spot — the same anatomy as every figure in this book.

```python
import matplotlib.pyplot as plt

def plot_strategy(legs, spot, T, sigma, lot_size=75, title="Strategy"):
    stats = analyze(legs, spot, lot_size)
    grid = stats["grid"]
    expiry = [payoff_at_expiry(legs, S) * lot_size for S in grid]
    now    = [pnl_now(legs, S, T, sigma) * lot_size for S in grid]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(grid, expiry, lw=2, label="P&L at expiry")
    ax.plot(grid, now, lw=1.5, ls="--", label="P&L now (Black-Scholes)")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(spot, color="grey", ls=":", label=f"spot {spot:.0f}")
    ax.fill_between(grid, expiry, 0, where=[e >= 0 for e in expiry],
                    color="green", alpha=0.12)
    ax.fill_between(grid, expiry, 0, where=[e < 0 for e in expiry],
                    color="red", alpha=0.12)
    for b in stats["breakevens"]:
        ax.scatter([b], [0], color="black", zorder=5)
    ax.set_xlabel("Nifty at expiry"); ax.set_ylabel("P&L per lot (Rs)")
    ax.set_title(title); ax.legend(); fig.tight_layout()
    return fig
```

## Worked example (₹, Nifty iron condor)

Suppose Nifty spot is **24,000** with a weekly expiry **7 days** away. India VIX implies about **14%** annualised volatility, so `sigma = 0.14` and `T = 7 / 365 = 0.0192` years. (At 14% vol over 7 days, a one-standard-deviation move in Nifty is about `24000 * 0.14 * sqrt(7/365) = 465 points` — keep that number in mind when we judge how wide the strikes are.) We sell a standard iron condor: short the 23,600 put and 24,400 call (the inner short strikes), and buy the 23,400 put and 24,600 call as protective wings. Lot size is about **75**. From the option chain we read these per-unit premiums: 23,400 put = ₹18, 23,600 put = ₹44, 24,400 call = ₹56, 24,600 call = ₹26.

```python
legs = iron_condor(put_buy=23400, put_sell=23600,
                   call_sell=24400, call_buy=24600,
                   p_buy=18, p_sell=44, c_sell=56, c_buy=26)

spot, T, sigma = 24000, 7/365, 0.14
print(analyze(legs, spot))
print(net_greeks(legs, spot, T, sigma))
print("POP:", round(prob_of_profit(legs, spot, T, sigma), 3))
```

Walk through the economics by hand to check the code. The **net credit** received per unit is the premium taken in minus the premium paid out: `(44 + 56) - (18 + 26) = 100 - 44 = ₹56`. Across one lot of 75 that is `56 * 75 = ₹4,200` collected up front — and that credit is your **maximum profit**, earned if Nifty finishes between 23,600 and 24,400 so all four options expire worthless.

The **maximum loss** happens if Nifty blows through either wing. The spread width on each side is 200 points (e.g. 23,600 − 23,400). The worst case is `width - credit = 200 - 56 = ₹144` per unit, or `144 * 75 = ₹10,800` per lot. Note the asymmetry that defines short premium: you risk ₹10,800 to make ₹4,200. That is *fine* only if the trade wins often enough — which is what POP tells you.

The **breakevens** are the short strikes adjusted by the credit: lower `= 23,600 - 56 = 23,544`, upper `= 24,400 + 56 = 24,456`. As long as Nifty expires inside that 23,544–24,456 band, the condor is profitable. The `analyze` function recovers exactly these numbers from the grid: max profit ₹4,200, max loss −₹10,800, breakevens [23544, 24456].

The **net Greeks** confirm the trade's character. With spot sitting near the centre, net delta is close to zero (roughly market-neutral), net theta is **positive** (about +₹7 per unit per day — the position earns money every day the clock ticks, which is the whole thesis of a condor), and net vega is **negative** (a spike in India VIX hurts you, because you are short options). The probability-of-profit comes out around **0.67** under the 14% lognormal assumption: the breakeven band spans roughly one standard deviation on each side of spot, so the trade wins about two times in three.

![Figure: Nifty iron condor — flat profit plateau between the short strikes, capped losses beyond the wings, with breakevens and spot marked](figs/iron_condor.png)

The figure shows the signature condor shape: a flat green profit plateau over the 23,600–24,400 zone, sloping down to two flat red loss shelves past the wings, with the smoother "P&L now" curve sitting above the kinked expiry line because time value is still in the options.

## Common mistakes / risk note

- **Sign errors on premium.** The single most common bug: forgetting that short legs *receive* premium. Our convention — store premium positive, let `qty` carry the sign — eliminates this, but only if you never sneak a negative premium in by hand.
- **Trusting grid max-loss for naked positions.** For defined-risk trades the grid's minimum *is* the true max loss. For a naked short call the real max loss is unbounded; the grid only shows the loss at its right edge. Always check whether your strategy has a long wing on every side before quoting "max loss."
- **Confusing POP with edge.** A 70% probability of profit is not a 70% chance of a *good* trade. The iron condor above risks three times what it can make; a few maximum-loss weeks erase many winners. POP ignores the *size* of outcomes — pair it always with the max-loss number and the expected value, never alone.
- **Stale volatility and rate.** The before-expiry curve and Greeks are only as good as the `sigma` you feed in. Use the *option chain's implied volatility*, ideally per strike, not one flat number, and remember VIX moves intraday.
- **Forgetting costs.** Real P&L is after brokerage, exchange fees, STT (charged on the sell side, and on exercised ITM index options at expiry), and slippage on four separate legs. A condor crossing four bid-ask spreads can lose a meaningful slice of its ₹50 credit before the market even moves.

## Key takeaways

- Represent **every** strategy the same way: a list of legs, each `(kind, strike, signed qty, premium)`. One representation, one set of analytics.
- Expiry payoff is `sum of qty * (intrinsic(S) - premium)`; computing it across a price grid hands you breakevens, max profit, and max loss for free.
- Net Greeks are the **signed sum** of per-leg Greeks from your Black-Scholes engine — instant whole-position risk.
- Re-pricing the legs with Black-Scholes gives the **before-expiry** P&L curve; the gap to the expiry line is the remaining time value.
- Probability of profit comes from weighting the payoff grid by a **lognormal** terminal distribution — useful, but never a substitute for looking at max loss.
- This leg-based design is how real strategy-analytics tools are built: positions are rows, analytics are functions over the rows.

## Practice problems

1. **Extend the data model.** Add a `bear_put_spread(K_long, K_short, prem_long, prem_short)` builder to the library (buy the higher-strike put, sell the lower-strike put). What legs does it return?
2. **Hand-check a spread.** A Nifty bull call spread: buy 24,000 call at ₹120, sell 24,200 call at ₹55. Compute net debit, max profit, max loss, and breakeven per unit (lot size 75 for the per-lot figures).
3. **Net Greeks intuition.** Without running code, state the sign (positive/negative/near-zero) of net delta, theta, and vega for a **long straddle** placed at-the-money. Explain each in one line.
4. **POP vs edge.** The chapter's iron condor has POP ≈ 0.67, max profit ₹4,200, max loss ₹10,800 per lot. Compute a rough expected value assuming the only two outcomes are full win (prob 0.67) and full loss (prob 0.33). What does this say about the trade?
5. **Find the bug.** A junior codes a short put as `Leg("put", 23600, +1, 44)` and is surprised the analyzer shows a long-put payoff. What is wrong and what is the fix?
6. **Volatility sensitivity.** You run `prob_of_profit` for the condor with `sigma = 0.14` and again with `sigma = 0.22` (a VIX spike). Which gives the higher POP, and why does that match the negative net vega?

## Solutions

1. **Bear put spread builder.** You want to profit as Nifty falls, with defined risk: buy the higher-strike put (more expensive, the one you want value from) and sell the lower-strike put (cheaper, finances it).

   ```python
   def bear_put_spread(K_long, K_short, prem_long, prem_short):
       return [Leg("put", K_long,  +1, prem_long),   # higher strike, bought
               Leg("put", K_short, -1, prem_short)]  # lower strike, sold
   ```
   It returns two put legs, long the higher strike and short the lower — a net debit trade.

2. **Bull call spread by hand.** Net debit `= 120 - 55 = ₹65` per unit (you pay 120, receive 55). Max profit happens above 24,200: the spread is worth its full 200-point width, so profit `= 200 - 65 = ₹135` per unit = `135 * 75 = ₹10,125` per lot. Max loss is the debit itself, ₹65 per unit = `65 * 75 = ₹4,875` per lot, realised below 24,000 where both calls expire worthless. Breakeven `= lower strike + debit = 24,000 + 65 = 24,065`.

3. **Long straddle Greeks.** Net **delta ≈ 0**: a long ATM call (delta ≈ +0.5) and long ATM put (delta ≈ −0.5) cancel, so it is direction-neutral at entry. Net **theta negative**: you own two options, both bleeding time value every day — the clock is your enemy. Net **vega positive**: you are long two options, so rising implied volatility (a VIX spike) inflates both and helps you. A straddle is a bet on a *big move or a vol jump*, paid for with daily decay.

4. **Rough expected value.** EV `= 0.67 * 4,200 + 0.33 * (-10,800) = 2,814 - 3,564 = -₹750` per lot. Despite a roughly two-in-three win rate the trade has *negative* expected value under these crude assumptions — the rare losses are too large. In reality the loss is usually partial (Nifty rarely settles far past a wing) and good traders manage the position before max loss, but the lesson stands: **high POP does not mean positive edge.** You must size and manage, not just collect premium.

5. **The bug.** `qty = +1` means *long*, so `Leg("put", 23600, +1, 44)` is a **bought** put — exactly the long-put payoff the analyzer correctly shows. To represent a *short* put (premium received, the seller's position) the quantity must be negative: `Leg("put", 23600, -1, 44)`. The premium stays positive; only the sign of `qty` flips the cash flow and the payoff shape.

6. **Volatility sensitivity.** The **lower** sigma (0.14) gives the **higher** POP. Lower volatility means the lognormal terminal distribution is tighter around spot, so more probability mass lands inside the 23,750–24,250 profit band. Raising sigma to 0.22 fattens the tails, pushing mass out past the wings and lowering POP. This is the same fact the **negative net vega** reports from the Greek side: rising implied volatility is bad for a short-premium condor. Two different tools — a probability integral and a first-order Greek — telling you the identical economic truth.
