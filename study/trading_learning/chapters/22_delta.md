# Chapter 22: Delta — Direction, Hedge Ratio & Probability Proxy

Imagine you are driving and you press the accelerator. Delta is the answer to one simple question: "If the road (the underlying) moves forward by one step, how far does my car (my option premium) move?" That is all delta really is — a sensitivity. For an options trader it is the single most important number on the screen, because it tells you, right now, how much money you make or lose when Nifty ticks up or down by one point. Master delta and you stop thinking of an option as a lottery ticket and start thinking of it as a controllable dose of directional exposure.

This chapter teaches delta three ways at once: as **direction** (how much you are effectively long or short the index), as a **hedge ratio** (how much underlying to trade to cancel that exposure), and as a rough **probability** that your option finishes in-the-money. These three readings are the working vocabulary of every professional desk in Mumbai. We will keep everything in rupees, Nifty points, and weekly-expiry terms so the intuition sticks.

## Core concepts

### Delta is the slope of the premium curve

Delta (the Greek letter, written here as the word "delta") is defined as the **rate of change of the option premium with respect to a 1-point move in the underlying**, holding everything else constant.

`delta = change in option premium / change in underlying`

If a Nifty call has a delta of 0.40, then when Nifty rises by 1 point, the call's premium rises by about 0.40 points. Because Nifty options are quoted in points and each point is worth ₹1 per unit of the lot (Nifty lot is currently about 75 units), that 0.40 also has a direct rupee meaning, which we will compute shortly.

A few facts to anchor:

- **Call delta runs from 0 to +1.** A call gains value when the underlying rises, so its delta is positive. Deep out-of-the-money (OTM) calls have delta near 0 (they barely react). Deep in-the-money (ITM) calls have delta near +1 (they move almost rupee-for-rupee with the index, behaving like the index itself).
- **Put delta runs from 0 to -1.** A put gains value when the underlying falls, so its delta is negative. Deep OTM puts sit near 0; deep ITM puts approach -1.
- **At-the-money (ATM) options have delta near +/-0.5.** When the strike equals spot, the option has roughly a coin-flip chance of finishing ITM, and its premium moves about half a point for every point the index moves.

### Why the curve is S-shaped, not a straight line

Delta is not constant. Plot a call's delta against spot and you get a smooth **S-curve** (a sigmoid): flat and near zero when the option is far OTM, rising steeply through the ATM region, and flattening again near +1 deep ITM. The reason is intuitive. A 22000 call when Nifty is at 18000 is almost dead — a 1-point wiggle in the index changes almost nothing about its near-certain worthlessness, so delta is ~0. The same call when Nifty is at 30000 is almost certain to be exercised; it now tracks the index nearly one-for-one, so delta is ~1. In between, around the strike, the outcome is genuinely uncertain and small moves swing the odds the most — that is where delta changes fastest.

![Figure: call delta vs spot](figs/delta_call.png)

That steepness in the middle has a name: **gamma**, the rate of change of delta itself. We preview it here and devote the next chapter to it. For now, just hold the picture: delta is the slope of the premium curve, and gamma is how fast that slope changes as spot moves.

### Reading 1 — Delta as directional exposure (equivalent units of the underlying)

The first and most practical reading: **delta tells you how many units of the underlying your option behaves like.**

`equivalent underlying units = delta * lot size * number of lots`

A single Nifty call with delta 0.50 on a 75-unit lot behaves, for small moves, like being long `0.50 * 75 = 37.5` units of Nifty. If Nifty moves 100 points, you make roughly `37.5 * 100 = ₹3,750` on that one option — before gamma, theta, and vega complicate things. This is why traders say a position is "long 40 deltas" or "short 200 deltas." Delta is the common currency that lets you compare a fistful of different strikes and expiries on one scale: equivalent index exposure.

### Reading 2 — Delta as the hedge ratio

The second reading flips the first around. If your call behaves like 37.5 units of long Nifty, then to **neutralise** that directional exposure you would short 37.5 units of Nifty (via futures). That is **delta-hedging**, and delta is the **hedge ratio** — the amount of underlying you must trade to make the combined position insensitive to small moves in spot.

`hedge = - (delta * lot size * number of lots) units of the underlying`

A market maker who sells you that 0.50-delta call is now short 37.5 deltas. To avoid betting on direction (they want to earn the spread and the volatility edge, not gamble on Nifty's path), they buy 37.5 units of Nifty futures. Their book is now **delta-neutral**: a 1-point move up loses on the short call but gains on the long futures, and the two cancel. Because delta changes as spot moves (gamma again), they must **re-hedge** continuously — and the cost of that constant re-hedging is exactly what theta and vega are paying for. This is the heartbeat of the entire options market.

### Reading 3 — Delta as an approximate probability of finishing ITM

The third reading is the one beginners love and pros use with care: **delta is roughly the probability that the option expires in-the-money.** A 0.30-delta call is loosely "about a 30% chance of finishing ITM."

This works because, in the Black-Scholes world, call delta equals `N(d1)` — the cumulative normal of the term d1. The cleaner, more honest probability of finishing ITM is actually `N(d2)`, which is always a bit smaller than `N(d1)` because d2 = d1 - sigma*sqrt(T). So:

- Delta `approx= N(d1)` slightly **overstates** the true risk-neutral probability of finishing ITM.
- `N(d2)` is the proper "probability ITM" under the risk-neutral measure.
- For short-dated, low-vol options the two are close; for long-dated or high-vol options the gap widens.

So treat delta as a quick, free probability proxy — a 0.20-delta OTM put is "roughly a 1-in-5 shot" — but do not confuse it with a precise figure, and remember it is a *risk-neutral* probability, not a real-world forecast. Honest pedagogy: the market does not owe you your delta as a payout rate.

### How delta itself changes — with spot, time, and volatility

Delta is a snapshot. Three forces move it:

- **As spot moves (gamma):** delta rises as the underlying rises (calls) and the S-curve carries delta toward 1 (ITM) or 0 (OTM). Near the ATM strike this happens fastest, especially close to expiry.
- **As time passes (charm):** for an OTM option, the dwindling time to expiry pushes delta toward 0 (it is running out of chances to get ITM). For an ITM option, delta drifts toward 1 (call) or -1 (put) as expiry nears and the outcome firms up. An ATM option stays near 0.50 but its delta becomes *knife-edge* sensitive — gamma explodes on expiry day.
- **As volatility changes (vanna):** higher implied volatility flattens and spreads the S-curve. With more vol, even a fairly OTM option has a realistic chance of finishing ITM, so its delta rises toward 0.50; deep-ITM deltas fall back toward 0.50 too. Low vol does the opposite — it sharpens the curve, pushing deltas toward 0 or 1. In short, high vol drags all deltas toward the middle (0.50).

### Position delta — adding it all up

For a portfolio, exposures simply add. **Position delta** is the signed sum of every leg's delta times its lot size and quantity.

`position delta (units) = sum over legs of (delta_leg * lot size * lots * +1 if long / -1 if short)`

A long call adds positive delta; a short call adds negative delta; a long put adds negative delta; a short put adds positive delta. Long futures contribute +1.0 delta per unit. Once you can total position delta, you can answer the only directional question that matters: **"If Nifty moves 1 point, how many rupees do I make?"** And you can convert any options book into its equivalent in Nifty lots — divide position delta in units by the lot size.

### Using delta to size a directional bet

If you have a view — say you expect Nifty to rise 300 points — delta lets you size the trade to a target exposure rather than guessing a lot count. Decide how much rupee profit you want per point (your target delta in rupees), then pick strikes and quantities whose combined delta hits that target. High-delta (deep ITM) options give you near-futures exposure with a smaller premium outlay and less time decay per delta; low-delta (OTM) options give cheap, leveraged, lower-probability exposure that bleeds theta. Delta is the dial that sets the dose.

## Worked example (₹, Nifty/Bank Nifty)

Setup: Nifty spot = 24,000. Lot size = 75 units. You are looking at the weekly options.

- 24,000 CE (ATM call), premium ₹120, **delta = +0.52**
- 24,300 CE (OTM call), premium ₹40, **delta = +0.28**
- 23,800 PE (OTM put), premium ₹55, **delta = -0.30**

**Step 1 — Equivalent units (Reading 1) for one ATM call.**
`equivalent units = 0.52 * 75 * 1 = 39 units of Nifty (long).`
If Nifty rises 100 points, expected P&L `approx= 39 * 100 = ₹3,900`. The premium itself rises about `0.52 * 100 = 52 points`, i.e. from ₹120 to ~₹172; in rupees `52 * 75 = ₹3,900`. Same answer, two routes.

**Step 2 — The hedge ratio (Reading 2).**
A desk short this one call is short 39 deltas. To go delta-neutral it buys `39` units of Nifty futures (about half a lot of exposure). Now a small move in either direction nets to roughly zero P&L — until gamma forces a re-hedge.

**Step 3 — Probability proxy (Reading 3).**
The 24,300 CE has delta +0.28, so a rough "about 28% chance of finishing above 24,300" at expiry. The true `N(d2)` probability would be a touch lower, perhaps ~25%. So if someone sells this call collecting ₹40 (`40 * 75 = ₹3,000`), they are taking on something like a 1-in-4 risk of it going ITM. Fair, not free money.

**Step 4 — Position delta of a two-leg trade.**
You buy 2 lots of the 24,000 CE and sell 1 lot of the 23,800 PE (a mildly bullish structure).

- Long 2 ATM calls: `+0.52 * 75 * 2 = +78 units`
- Short 1 OTM put: short a -0.30 put adds positive delta: `-(-0.30) * 75 * 1 = +22.5 units`
- **Position delta = +78 + 22.5 = +100.5 units.**

**Step 5 — Convert to equivalent Nifty lots and to rupees per point.**
`equivalent lots = 100.5 / 75 = approx 1.34 lots long Nifty.`
Rupees per 1-point Nifty move `= 100.5 * ₹1 = ₹100.5`. So a 200-point rally is worth roughly `200 * 100.5 = ₹20,100` to this book, before time decay and any change in implied vol. That single number — "I am long about 1.34 Nifty lots" — is what a professional carries in their head all day.

## Common mistakes / risk note

- **Treating delta as a constant.** Delta is a local slope. A 0.30-delta call does not stay 0.30 after a 300-point move; gamma changes it. Your sizing math is only good for *small* moves — re-check after any big swing.
- **Reading delta as a real-world probability.** Delta `approx N(d1)` is a *risk-neutral* proxy and overstates true ITM probability relative to `N(d2)`. It is a rough guide, never a guarantee. "70-delta so 70% safe" is sloppy thinking that gets sellers hurt.
- **Forgetting the sign on short options.** Selling a put is *positive* delta (bullish), not negative. Selling a call is negative delta. Get the signs wrong and you hedge the wrong way.
- **Ignoring that delta-neutral is not risk-free.** A delta-hedged book is still exposed to gamma, theta, and vega. Being delta-neutral only kills the *first-order* directional risk for *small* moves. India VIX spiking or a gap opening can blow through a hedge overnight.
- **Over-leveraging via low-delta OTM options.** Cheap 0.05-delta weekly options look like a tiny bet but, sold in size, carry large tail risk; bought in size, they usually expire worthless. Remember the honest base rate: most long options expire worthless, and SEBI studies show roughly 9 in 10 retail F&O traders lose money. Delta sizing helps you take *measured* risk, not unlimited risk.

## Key takeaways

- Delta is the rate of change of premium per 1-point move in the underlying: calls 0 to +1, puts 0 to -1, ATM near +/-0.5.
- Read delta three ways: directional exposure (equivalent underlying units), the hedge ratio for delta-hedging, and an approximate probability of finishing ITM.
- The honest probability caveat: delta `approx N(d1)` overstates ITM odds; `N(d2)` is the cleaner risk-neutral probability, and both are risk-neutral, not real-world.
- Delta changes with spot (gamma), with time (toward 0 or +/-1 for OTM/ITM), and with volatility (high vol drags deltas toward 0.50).
- Position delta is the signed sum of leg deltas times lot size and quantity; divide by lot size to read your book as equivalent Nifty lots, and multiply by ₹1 to read rupees per point.
- Use delta to *size* a directional bet to a target exposure instead of guessing lot counts — but always re-check after large moves.

## Practice problems

1. **Conceptual.** A trader says "my 24,500 CE is 0.18 delta, so there's roughly an 18% chance it finishes ITM." What is technically wrong, or at least imprecise, about equating delta with the probability of finishing ITM? Which quantity is the cleaner probability?

2. **Numeric — equivalent units.** Nifty is at 24,000, lot size 75. You are long 3 lots of a call with delta +0.45. How many equivalent units of Nifty are you long, and what is your approximate P&L if Nifty rises 80 points (ignore gamma/theta/vega)?

3. **Numeric — hedge ratio.** A market maker is short 4 lots of a Bank Nifty 52,000 CE with delta +0.55. Bank Nifty lot size is 35 units. How many units of Bank Nifty futures must they buy or sell to be delta-neutral, and in which direction?

4. **Numeric — position delta.** You hold: long 2 lots of 24,000 CE (delta +0.50) and long 2 lots of 24,000 PE (delta -0.50), lot size 75. What is your net position delta? What does this tell you about your directional exposure, and what risk are you actually taking?

5. **Numeric — sizing and conversion.** You want to be long the equivalent of exactly 1.5 Nifty lots using a single OTM call with delta +0.25 (lot size 75). How many lots of that call do you need (rounded to the nearest lot), and what is your resulting position delta in units?

6. **Conceptual.** India VIX jumps from 12 to 22 overnight with Nifty unchanged at 24,000. Qualitatively, what happens to the delta of a fairly OTM 24,600 CE, and why?

## Solutions

**1.** Delta approximately equals `N(d1)`, while the risk-neutral probability of finishing ITM is `N(d2)`, which is smaller because `d2 = d1 - sigma*sqrt(T)`. So delta slightly *overstates* the ITM probability — the true figure is a bit below 18%. Two further caveats: it is a *risk-neutral* probability, not a real-world forecast, and delta is only a local snapshot that shifts as spot, time, and vol change. The cleaner probability measure is `N(d2)`.

**2.** Equivalent units `= 0.45 * 75 * 3 = 101.25` units long. Approximate P&L for an 80-point rise `= 101.25 * 80 = ₹8,100`. (Check via premium: the option gains about `0.45 * 80 = 36 points`, and `36 * 75 * 3 = ₹8,100`.)

**3.** The maker is short `0.55 * 35 * 4 = 77` deltas (short the call means negative delta exposure). To neutralise, they must add +77 deltas by **buying 77 units** of Bank Nifty futures (about 2.2 lots). Buying, because a short call is bearish/negative-delta and futures must offset it.

**4.** Long call: `+0.50 * 75 * 2 = +75`. Long put: `-0.50 * 75 * 2 = -75`. Net position delta `= +75 - 75 = 0` units — delta-neutral. This is a long straddle: directionally flat at this instant, so a small move makes little, but you are **long gamma and long vega and short theta** — you profit from a large move in *either* direction or a vol spike, and you bleed time decay every day Nifty sits still. Delta-neutral is not risk-free; it is a bet on movement, not direction.

**5.** Target exposure `= 1.5 lots * 75 = 112.5` units. Each call lot gives `0.25 * 75 = 18.75` units. Lots needed `= 112.5 / 18.75 = 6 lots` exactly. Resulting position delta `= 0.25 * 75 * 6 = 112.5` units, i.e. exactly 1.5 equivalent Nifty lots. (Note the trade-off: matching the exposure with low-delta OTM calls needs many lots and carries heavy theta — a higher-delta ITM call would reach 1.5 lots with far fewer contracts.)

**6.** A jump in India VIX means higher implied volatility. Higher vol flattens and widens the delta S-curve, dragging all deltas toward 0.50. The 24,600 CE is OTM with delta below 0.50, so its delta **rises** — with more volatility, finishing above 24,600 by expiry becomes more plausible, so the option behaves more like a coin flip and tracks the index more strongly. (This sensitivity of delta to volatility is called vanna.)
