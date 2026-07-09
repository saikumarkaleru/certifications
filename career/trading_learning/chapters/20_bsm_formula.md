# Chapter 20: Black-Scholes-Merton II — The Formula, d1/d2 & Assumptions

In the previous chapter you saw *where* the Black-Scholes-Merton (BSM) idea comes from: if you can continuously hedge an option with the underlying, the option's fair price is whatever makes that hedged portfolio earn the risk-free rate — no more, no less. That argument is the engine. This chapter hands you the finished machine: the actual closed-form formula that the whole options world quotes, the meaning of its mysterious `d1` and `d2`, and an honest accounting of the assumptions baked into it.

Think of BSM as a recipe that turns five plain ingredients — spot price, strike, time, interest rate, and volatility — into one number: the fair premium. You will never punch this formula into a calculator on the trading desk (your terminal does it in microseconds). But you must understand what every piece *means*, because that is what lets you read an option chain like a professional, sanity-check a quote, and — crucially — understand why the model is *wrong* in a specific, exploitable way that the market itself acknowledges through the "volatility smile."

## Core concepts

### The two formulas

For a European call and put on a non-dividend-paying underlying:

```
C = S * N(d1) - K * e^(-r*T) * N(d2)

P = K * e^(-r*T) * N(-d2) - S * N(-d1)
```

where

```
d1 = ( ln(S/K) + (r + 0.5*sigma^2)*T ) / ( sigma * sqrt(T) )

d2 = d1 - sigma * sqrt(T)
```

The symbols:

- `S` = current spot price of the underlying (e.g. Nifty at 24000).
- `K` = strike price of the option.
- `T` = time to expiry **in years** (a weekly expiry 4 days away is 4/365 ≈ 0.011 years).
- `r` = the risk-free interest rate per year, as a decimal (7% = 0.07).
- `sigma` = the annualised volatility of the underlying's returns, as a decimal (15% = 0.15). This is the one input you cannot look up — you must estimate or imply it.
- `e` = Euler's number, about 2.71828; `e^(-r*T)` is the discount factor that pulls a future rupee back to today's value.
- `ln` = natural logarithm.
- `N()` = the **standard normal cumulative distribution function (CDF)**. Feed it a number, it returns the probability that a standard normal random variable (mean 0, standard deviation 1) lands at or below that number. `N(0) = 0.5`, `N(1.65) ≈ 0.95`, `N(-1.65) ≈ 0.05`. It always returns something between 0 and 1.

Notice the elegant symmetry: the put formula is the call formula with the `N()` terms flipped to their mirror images (`N(-d1)`, `N(-d2)`). This is not a coincidence; it is **put-call parity** hiding inside the algebra, which we will use as a cross-check later.

### Reading the call formula in plain English

The call price is built from two competing pieces — think of it as **"what you expect to receive" minus "what you expect to pay."**

```
C = [ S * N(d1) ]  -  [ K * e^(-r*T) * N(d2) ]
       benefit              cost
```

- The first term, `S * N(d1)`, is the present value of *receiving the stock* if the option finishes in the money. You don't get the whole stock — you get it weighted by `N(d1)`, a number that scales how "deep" and how "likely" the upside is.
- The second term, `K * e^(-r*T) * N(d2)`, is the present value of *paying the strike* if you exercise. `K * e^(-r*T)` is the strike discounted back to today; multiplying by `N(d2)` weights it by the chance you actually exercise.

So a call is "the discounted expected stock you'll collect, minus the discounted expected cash you'll hand over." Everything reduces to those two weighted halves.

### What N(d2) means: roughly, the probability of finishing in the money

`N(d2)` is the closest thing the formula has to a clean probability. In the model's **risk-neutral** world (the pretend world from the hedging argument, where everything drifts at the risk-free rate), `N(d2)` is exactly the probability that a call expires in the money — that spot ends above the strike. For a put, `N(-d2)` is the probability it ends in the money (spot below strike).

This is enormously useful intuition. If you see a 24000 call priced so that `N(d2) ≈ 0.54`, the market is implicitly saying "about a 54% chance Nifty closes above 24000 at expiry" — under risk-neutral assumptions. Traders use this constantly to talk about an option's "probability of being in the money" or, by subtracting from 1, its **probability of expiring worthless**.

A health warning: this is the *risk-neutral* probability, not the real-world one — the real world drifts faster than `r`, so true odds differ. But as a quick, model-consistent read of "how likely is this strike to pay off," `N(d2)` is the number professionals reach for.

### What N(d1) means: the delta and the hedge ratio

`N(d1)` is even more important on a live desk, because **for a call, N(d1) is the delta** — the rate at which the option's price changes when spot moves by one point, and equivalently the number of units of the underlying you must hold to hedge one option.

- If `N(d1) = 0.56`, the call gains about ₹0.56 for every ₹1 Nifty rises, and to neutralise the directional risk of selling one call you would hold 0.56 "units" of Nifty exposure (in practice, futures or a basket).
- Deep in-the-money calls have `N(d1)` approaching 1 (they move almost one-for-one with spot, like owning the index). Deep out-of-the-money calls have `N(d1)` approaching 0 (they barely react). At-the-money is near 0.5.

So `N(d1)` is the "how much stock does this option behave like right now" term — the hedge ratio from the replication argument made concrete. `N(d2)`, by contrast, is the "will I be exercising" term. They are close in value but mean different things, and the gap between them (`sigma * sqrt(T)`, inside the exponentials) is precisely the contribution of volatility and time.

### Decoding d1 and d2 themselves

Don't be intimidated by `d1`. Read its numerator:

```
ln(S/K) + (r + 0.5*sigma^2)*T
```

- `ln(S/K)` measures **moneyness on a log scale**. If spot equals strike, this is `ln(1) = 0`. If spot is above strike (call already in the money), it's positive; below, negative. Logs are used because returns compound multiplicatively, not additively — a move from 100 to 110 and from 110 to 121 are "the same size" in log terms.
- `(r + 0.5*sigma^2)*T` is the **expected log-drift** of the underlying over the life of the option in the risk-neutral world: it grows at the risk-free rate, plus a `0.5*sigma^2` convexity adjustment that arises because of the lognormal math (Jensen's inequality — the average of a lognormal sits above its median).

The denominator `sigma * sqrt(T)` is the **total volatility over the option's life** — the standard deviation of the log-return between now and expiry. Note the `sqrt(T)`: volatility scales with the *square root* of time, not time itself, so doubling the days to expiry multiplies expected dispersion by about 1.41, not 2. This square-root-of-time rule is one of the most-used facts in all of options trading.

So `d1` is essentially "how many standard deviations is the (drift-adjusted) strike from spot," and `d2` is the same distance without the upper drift kicker — which is why `N(d2)` is the probability term while `N(d1)` carries the extra `0.5*sigma^2` that makes it the hedge/delta term.

### The dividend-adjusted (Merton) version

The basic formula assumes the underlying pays no income. Real assets often do: stocks pay dividends, and an *index* like Nifty has a continuous dividend yield from its constituents. Robert Merton extended the model for a continuous dividend yield `q` (per year, as a decimal) by **replacing every `S` with `S * e^(-q*T)`** — the spot discounted for the dividends you forgo by holding the option instead of the stock:

```
C = S*e^(-q*T) * N(d1) - K*e^(-r*T) * N(d2)

P = K*e^(-r*T) * N(-d2) - S*e^(-q*T) * N(-d1)

d1 = ( ln(S/K) + (r - q + 0.5*sigma^2)*T ) / ( sigma * sqrt(T) )

d2 = d1 - sigma * sqrt(T)
```

The drift term becomes `(r - q)` because a dividend-paying asset grows more slowly in price terms (some of its return leaks out as cash). For Nifty, the dividend yield is small (roughly 1-1.5% currently), so for short weekly options the dividend effect is tiny but not zero. For single stocks around a big dividend, or for longer-dated options, it matters. India's index options are also **cash-settled and European**, which is exactly what BSM assumes — a nice fit. (American-style options, like some single-stock contracts, technically need a different model because of early exercise, but that is a later concern.)

### The assumptions — and where reality breaks them

BSM is a beautiful machine built on idealised parts. Knowing where those parts don't match reality is what separates a professional from someone who blindly trusts a screen. The core assumptions:

1. **Returns are lognormal with constant volatility.** The model assumes the underlying follows "geometric Brownian motion" — log-returns are normally distributed, and `sigma` is a single fixed number for the option's whole life. Reality: volatility *clusters* (calm periods and stormy periods), spikes during crashes, and is plainly not constant. India VIX itself moves every day.

2. **No jumps — prices move continuously.** The math assumes the price never gaps; it slides smoothly so you can always re-hedge. Reality: markets gap. A surprise RBI decision, an election result, a global shock, or a bad earnings print can move Nifty 3% between one print and the next, with no chance to hedge in between. Gap risk is real risk that the model ignores.

3. **Constant, known risk-free rate.** `r` is assumed fixed and the same for borrowing and lending. Reality: rates move and the rate you actually fund at is higher than the rate you earn. For short-dated options this matters little; for longer ones, more.

4. **Continuous, frictionless, costless trading.** The replication argument requires you to re-hedge constantly with zero transaction costs, infinitely divisible quantities, and no market impact. Reality: you re-hedge discretely, pay brokerage and STT, cross bid-ask spreads, post SPAN margin, and move the market when you trade size. Every re-hedge leaks money.

5. **No taxes or short-selling restrictions; the underlying is perfectly tradable.** Reality: STT on exercised options, capital-gains treatment, position limits, and the practical difficulty of shorting an index basket all intrude.

None of this makes BSM useless — it makes it a *common language*. The whole market agrees to speak in BSM terms, then prices in the messiness through the one free input: volatility.

### Why the volatility smile exists (preview)

Here is the punchline that the assumptions set up. Suppose BSM were perfectly true. Then every option on the same underlying and expiry — every strike — would have to be priced with the *same* `sigma`, because there is only one true volatility for the underlying. If you took market prices and ran the formula backwards to extract the volatility each price implies (the **implied volatility**), every strike would return the identical number. A flat line.

In real markets it is *not* flat. Plot implied volatility against strike and you get a **smile** or, in equity indices, a downward **skew** — far out-of-the-money puts trade at noticeably higher implied volatility than at-the-money options. Why? Because the assumptions above are false in a directional way. Markets jump (especially *down*), crashes are fatter-tailed than the lognormal allows, and traders pay up for crash protection. The market is, in effect, telling you it does not believe BSM's tidy bell curve — and it expresses that disbelief by bending the volatility input strike-by-strike. We devote a full later chapter to the smile and skew; for now, just lodge the idea: **the smile is the market's correction to BSM's wrong assumptions, written in the language of volatility.**

## Worked example (₹, Nifty)

Let's price an **at-the-money 24000 Nifty call** by hand, the way the formula demands, step by step.

**Inputs:**
- `S = 24000` (Nifty spot)
- `K = 24000` (at-the-money strike)
- `sigma = 0.15` (15% annualised volatility — a calm-market figure)
- `r = 0.07` (7% risk-free rate)
- `T = 30/365 = 0.08219` years (about a month to expiry)
- Dividends ignored (`q = 0`) for simplicity.

**Step 1 — Compute sigma * sqrt(T) (the total volatility over the option's life).**

```
sqrt(T) = sqrt(0.08219) = 0.28669
sigma * sqrt(T) = 0.15 * 0.28669 = 0.04300
```

Interpretation: over one month, Nifty's one-standard-deviation log-move is about 4.3%, i.e. roughly +/- 1032 points around 24000.

**Step 2 — Compute the drift term in the numerator of d1.**

```
ln(S/K) = ln(24000/24000) = ln(1) = 0
(r + 0.5*sigma^2)*T = (0.07 + 0.5*0.15^2) * 0.08219
                    = (0.07 + 0.01125) * 0.08219
                    = 0.08125 * 0.08219
                    = 0.006678
```

**Step 3 — Compute d1 and d2.**

```
d1 = (0 + 0.006678) / 0.04300 = 0.1553
d2 = d1 - sigma*sqrt(T) = 0.1553 - 0.04300 = 0.1123
```

Even though the call is exactly at the money, `d1` and `d2` are slightly positive — that is the risk-free drift nudging the expected terminal price above today's spot.

**Step 4 — Look up N(d1) and N(d2) from the standard normal table.**

```
N(d1) = N(0.1553) = 0.5617
N(d2) = N(0.1123) = 0.5447
```

Read those as: delta of this call is about **0.56** (it behaves like 0.56 units of Nifty), and the risk-neutral probability of finishing in the money is about **54.5%**.

**Step 5 — Discount the strike.**

```
K * e^(-r*T) = 24000 * e^(-0.07*0.08219)
             = 24000 * e^(-0.005753)
             = 24000 * 0.99426
             = 23862.31
```

**Step 6 — Assemble the call price.**

```
C = S*N(d1) - K*e^(-r*T)*N(d2)
  = 24000*0.5617 - 23862.31*0.5447
  = 13481.0 - 12998.1
  = 482.9
```

**The fair premium is about ₹483 per unit of Nifty.** At the current Nifty lot size of 75, one contract costs roughly `483 * 75 = ₹36,225` to buy.

**Sanity checks a pro would run:**
- An at-the-money call with a month to go and 15% vol should be worth a few hundred points — ₹483 passes the smell test.
- A rough rule of thumb for an ATM straddle is `0.8 * S * sigma * sqrt(T) = 0.8 * 24000 * 0.043 ≈ 826` for call + put combined; our call (₹483) plus a put of about ₹345 sums to ₹828 — bang on.
- The put price by put-call parity: `P = C - S + K*e^(-r*T) = 482.9 - 24000 + 23862.31 = 345.2`, i.e. about **₹345**, matching the straddle check. The slight gap between the call (₹483) and put (₹345) at the same strike is entirely the interest-rate carry on the discounted strike.

## Common mistakes / risk note

- **Putting time in days instead of years.** `T` must be in years. Plugging `T = 30` instead of `30/365` will produce an absurd price. This is the single most common beginner error.
- **Putting percentages in as whole numbers.** `sigma = 15`, not `0.15`, will blow the formula up. Always convert to decimals.
- **Treating N(d2) as the real-world probability of profit.** It is the *risk-neutral* probability of finishing in the money, and "in the money" is not the same as "profitable" — you still have to recover the premium you paid. A call that finishes ₹10 in the money after you paid ₹483 is a loss. Breakeven is strike plus premium, not the strike.
- **Trusting the formula's price over the screen.** If your BSM price disagrees with the live mid-price, the market is not wrong — your **volatility input** is. The market's price *defines* the implied volatility; the formula is a translator, not an oracle.
- **Forgetting the assumptions before a known event.** BSM assumes smooth, continuous, constant-vol markets. Around budget day, RBI policy, big results, or elections, gap risk and a vol spike make the model's "fair" price dangerously comforting. Long options can still bleed from theta even if you are right on direction; short options can be obliterated by a single gap. The model does not warn you — you have to.
- **The honest backdrop.** None of this changes the base-rate truth: most long options expire worthless, option selling carries large and sometimes undefined risk, and SEBI's own studies show roughly 9 in 10 retail F&O traders lose money. A pricing formula tells you what is *fair*, not what is *safe*.

## Key takeaways

- BSM turns five inputs (`S, K, T, r, sigma`) into one fair premium; only `sigma` cannot be observed and must be estimated or implied.
- The call is `S*N(d1) - K*e^(-r*T)*N(d2)` — "discounted expected stock received" minus "discounted expected cash paid"; the put mirrors it with `N(-d1)` and `N(-d2)`.
- `N(d1)` is the **delta / hedge ratio** (how much stock the option behaves like); `N(d2)` is approximately the **risk-neutral probability of finishing in the money**.
- `d1`'s numerator is log-moneyness plus risk-neutral drift; its denominator `sigma*sqrt(T)` is total volatility over the option's life — and volatility scales with **sqrt(time)**.
- The Merton extension swaps `S` for `S*e^(-q*T)` to handle a continuous dividend yield; India's European, cash-settled index options fit BSM cleanly.
- BSM's assumptions — lognormal returns, constant vol, no jumps, costless continuous hedging — are all violated in reality; the market patches the gap by varying implied volatility across strikes, which is the **volatility smile/skew**.

## Practice problems

1. **Concept.** In one sentence each, state what `N(d1)` and `N(d2)` represent on a live trading desk, and explain why `N(d1) > N(d2)` for a call.
2. **Numeric — d1/d2.** A Bank Nifty 52000 call has `S = 52500`, `K = 52000`, `sigma = 0.18`, `r = 0.07`, `T = 14/365`. Compute `sigma*sqrt(T)`, `d1`, and `d2`. (You need not finish the price.)
3. **Numeric — price.** Continuing problem 2, suppose you look up `N(d1) = 0.617` and `N(d2) = 0.589`. Compute the call premium per unit, and the cost of one lot if the Bank Nifty lot size is 30.
4. **Put-call parity.** For the ATM Nifty example in this chapter (`C = 482.9`, `S = 24000`, `K*e^(-r*T) = 23862.31`), find the fair price of the 24000 put without using the put formula directly.
5. **Assumptions.** It's the morning of the RBI policy announcement. Your BSM model, using yesterday's 12% volatility, says the ATM weekly straddle is "worth" ₹140, but the market is quoting ₹210. Explain in plain English why the market price is higher and what the ₹210 implies about the market's volatility view. Is the market "wrong"?
6. **Dividend adjustment.** A single stock trades at `S = 1000` with a continuous dividend yield `q = 0.03`. Write down the adjusted spot term `S*e^(-q*T)` you would feed into the Merton formula for a `T = 0.5` year option, and explain in one line why dividends lower a call's value.

## Solutions

**1.** `N(d1)` is the option's **delta** — the hedge ratio, i.e. how many units of the underlying you hold per option to neutralise direction (and roughly how much the premium moves per 1-point spot move). `N(d2)` is the **risk-neutral probability the option finishes in the money**. For a call, `N(d1) > N(d2)` because `d1 = d2 + sigma*sqrt(T)`, so `d1` is always the larger argument and `N()` is increasing; intuitively, the delta term carries an extra volatility/convexity kicker (the `0.5*sigma^2` drift) that the pure probability term does not.

**2.** 
```
sqrt(T) = sqrt(14/365) = sqrt(0.03836) = 0.19586
sigma*sqrt(T) = 0.18 * 0.19586 = 0.03525
ln(S/K) = ln(52500/52000) = ln(1.009615) = 0.009569
(r + 0.5*sigma^2)*T = (0.07 + 0.5*0.0324)*0.03836 = (0.07+0.0162)*0.03836 = 0.0862*0.03836 = 0.003307
d1 = (0.009569 + 0.003307) / 0.03525 = 0.012876 / 0.03525 = 0.3653
d2 = 0.3653 - 0.03525 = 0.3300
```
So `d1 ≈ 0.365`, `d2 ≈ 0.330`. (A slightly in-the-money call, deltas in the low-0.6s — consistent with the given `N` values.)

**3.** First discount the strike:
```
K*e^(-r*T) = 52000 * e^(-0.07*0.03836) = 52000 * e^(-0.002685) = 52000 * 0.997319 = 51860.6
C = S*N(d1) - K*e^(-r*T)*N(d2)
  = 52500*0.617 - 51860.6*0.589
  = 32392.5 - 30545.9
  = 1846.6
```
Premium ≈ **₹1,847 per unit**. One lot of 30 costs `1846.6 * 30 = ₹55,398`.

**4.** Use put-call parity, `P = C - S + K*e^(-r*T)`:
```
P = 482.9 - 24000 + 23862.31 = 345.2
```
The fair put price is about **₹345**, matching the chapter's straddle cross-check. (The call is dearer than the put at the same strike purely because of the interest carry embedded in discounting the strike — the right to *receive* the upside is worth slightly more than the right to *sell* at a strike whose present value is below spot.)

**5.** The market quote (₹210) sits well above your model value (₹140) because your `sigma` is stale. On a policy morning, traders expect a **larger-than-normal move and a possible gap** when the decision hits, so they bid up options to compensate for that risk — exactly the jump/changing-volatility behaviour BSM's constant-vol assumption ignores. Backing volatility out of ₹210 (running the formula in reverse) would yield an **implied volatility well above 12%** — that elevated number *is* the market's forecast of event risk. The market is not "wrong"; it is pricing information your yesterday-vol model doesn't contain. If anything, a model still showing ₹140 is the thing that's wrong, because it's blind to the event.

**6.** 
```
S*e^(-q*T) = 1000 * e^(-0.03*0.5) = 1000 * e^(-0.015) = 1000 * 0.98511 = 985.11
```
You would feed **985.11** in place of `S` (and use `r - q` in the drift). Dividends lower a call's value because the holder of the option, unlike the holder of the stock, does **not collect the dividends** paid before expiry; that forgone cash reduces the effective price the option is "tracking," so the right to buy is worth a little less.
