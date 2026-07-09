# Chapter 60: Portfolio-Level Greeks — Hedging a Whole Book

Up to now you have thought about risk one trade at a time: this iron condor has these Greeks, that bull call spread has those. But a professional does not run a drawer full of separate trades — she runs a **book**. A book is the entire collection of open positions treated as **one single object** with one set of risks. The market does not care that you mentally label one trade "my Nifty condor" and another "my expiry-day straddle." When Nifty moves, *everything* moves at once, and what hits your account is the **sum**. The shift from trader to professional is largely the shift from watching individual trades to watching the **aggregate** — and steering that aggregate with deliberate hedges.

The beautiful thing is that the tool for this is one you already have: the Greeks. Because every Greek is a rate of change, and rates of change add, your whole book has a single **net delta**, a single **net gamma**, a single **net theta**, and a single **net vega** — just the signed sum across every position. Once you can see those four numbers for the entire book, you can ask the only questions that actually matter: *Which way am I leaning? How much will I bleed or earn just from the clock? What happens if volatility jumps? And what is my worst plausible day?* This chapter teaches you to compute the book's net Greeks, hedge the aggregate exposure (especially net delta with index futures), respect correlation, stress-test the whole thing, and run it all to a **risk budget** rather than trade by trade.

## Core concepts

### From a pile of trades to one risk book

Imagine four people each shouting a direction at you: one says "buy," one says "sell," two say "buy." If you listen to them as four separate voices you are confused. If you *add up* the votes — net +2 buy — you suddenly know your true position. A book is exactly this. You may have a bullish spread here, a short strangle there, a protective put somewhere else, but the market only ever asks one question: *net, which way and how much are you exposed?*

The professional discipline is to stop looking at the profit-and-loss of individual trades during the day and instead watch the **four aggregate Greeks** of the whole book. Individual trades are how you *enter* risk; the net Greeks are how you *manage* it. This is the single biggest mental upgrade in this book.

### The Greeks aggregate by simple signed addition

For any Greek G:

`Book G = sum over all positions of (signed quantity * lot size * per-unit G)`

- **Signed quantity:** long is positive, short is negative.
- **Lot size:** Nifty is currently about **75 units per lot** (it changes over time; treat it as "about 75"). Multiply to get rupees-per-point at the book level.
- **Per-unit Greek:** delta, gamma, theta, vega per single unit of the underlying.

So the recipe is mechanical: list every leg, write down its signed delta/gamma/theta/vega, scale each by lot size, and add the columns. Four sums, four numbers, one book. There is no hidden interaction term in the arithmetic itself — delta adds to delta, vega adds to vega. (The *economic* interactions, through correlation, come later and live outside this arithmetic.)

A quick reminder of the signs each building block contributes, because they drive the netting:

- **Long call:** +delta, +gamma, −theta, +vega.
- **Long put:** −delta, +gamma, −theta, +vega.
- **Short call:** −delta, −gamma, **+theta**, −vega.
- **Short put:** +delta, −gamma, **+theta**, −vega.
- **Long future:** +1 delta per unit, and **zero** gamma, theta, vega.

That last line is the key to hedging: a future is **pure delta**. It is a clean steering wheel that moves only your directional exposure and touches nothing else.

### Reading the four book Greeks

Once you have the four sums, here is what each tells you about the *whole* book:

- **Net delta** — your directional lean, in units of the index. Positive net delta = you profit if Nifty rises, lose if it falls. This is the exposure you most often want to control, because direction is the hardest thing to forecast.
- **Net gamma** — how fast your net delta will *change* as Nifty moves. Positive net gamma (long options overall) means your delta improves in your favour as the market moves — but you are paying theta for it. Negative net gamma (net short options) means your delta moves *against* you on big moves — the seller's danger, especially into expiry.
- **Net theta** — your daily profit or loss purely from time passing, in rupees per day. A net-short-options book has positive theta (you earn the clock); a net-long book has negative theta (you pay rent).
- **Net vega** — your profit or loss per 1 percentage-point change in implied volatility (think India VIX). Positive net vega earns when IV rises; negative net vega earns when IV falls and is hurt by a volatility spike.

### Hedging the aggregate: flatten net delta with futures

The most common aggregate adjustment is **flattening net delta**. Suppose your whole book nets out to +600 units of long delta. You did not intend to be a Nifty bull — that exposure just *accumulated* from several positions. Rather than unwinding individual trades (which would also disturb your gamma, theta, and vega), you simply **sell 600 units of Nifty futures**. Futures have delta ≈ +1 per unit and zero everything else, so:

- Net delta: +600 − 600 = **0**. Directional bet switched off.
- Net gamma, theta, vega: **unchanged**. You keep exactly the volatility and decay profile you wanted.

That is the elegance of hedging at the book level. To kill positive delta, **sell** futures; to kill negative delta, **buy** futures. The amount is whatever makes the sum zero. In India both Nifty and Bank Nifty futures are deeply liquid and sit right next to the options, so professionals continuously trim the book's delta with futures all day long while the options supply the gamma, theta, and vega they actually came for.

The same logic extends to the other Greeks, though the tools differ:

- **Reduce net vega** by closing or offsetting volatility exposure — buy back some short options (or sell some longs) until net vega shrinks, or add an opposing options structure. You cannot hedge vega with futures (futures have no vega); you must use options.
- **Watch net gamma into expiry.** Gamma explodes for at-the-money options as expiry approaches, so a book that looked tame on Monday can become violently sensitive by Thursday expiry. A large *negative* net gamma into the last hours is the classic way Indian expiry-day sellers get hurt: a small index move produces an outsized, accelerating delta swing against them.

### Why correlation matters: your trades may secretly be one bet

Here is the trap the simple Greek-addition hides. The arithmetic adds delta to delta *as if* the positions were independent. But if you hold a bullish Nifty spread, a short Nifty put, **and** a long position in a heavyweight Nifty constituent like Reliance or HDFC Bank, those are **not three separate bets** — they are three versions of the *same* bet that the Indian market goes up. Because index and large-cap stocks are highly correlated, a single bad day hits all of them together.

Two consequences:

1. **Your true risk is larger than your net index delta suggests.** Stock positions carry index-like exposure (their "beta" to Nifty). To see real directional risk, convert stock deltas into **beta-weighted index delta** — a stock with beta 1.2 contributes 1.2 units of index-equivalent delta per unit of its own delta. Add those to your option deltas to get the book's *honest* directional exposure.
2. **Diversification can be an illusion.** Five "different" bullish positions across index and large caps behave like one big leveraged long when a global risk-off day arrives. The Greeks of each look modest; the *combined* drawdown is brutal because everything moves together. Conversely, genuinely offsetting positions (long one sector, short another) can reduce real risk even when the naive delta sum looks large.

The professional therefore reads net delta *beta-weighted to the index*, and constantly asks: "If I had to describe my entire book in one sentence, what am I really betting on?" If the honest answer is "Nifty goes up," then no amount of trade-count diversity changes the fact that you have one concentrated directional bet.

### Stress testing the book

Net Greeks are a **local, first-order** picture — accurate for *small* moves. Real danger lives in *large* moves, where gamma and vega bend the P&L away from the linear estimate. So professionals do not stop at the Greeks; they **stress test**: re-price the entire book under a grid of nasty scenarios and read off total P&L.

A typical stress grid for an Indian index book shifts two things at once:

- **Spot:** Nifty −5%, −2%, flat, +2%, +5%.
- **Implied volatility:** India VIX +10 points, +5, flat, −5.

The killer combination for option *sellers* is usually **down-and-up**: spot crashes *and* IV spikes at the same time (they almost always happen together — fear sells off the market and bids up option prices). A short-vega, short-gamma book gets hit on **both** axes simultaneously: the gamma loss from the spot fall *and* the vega loss from the IV jump. The stress table reveals the true worst-case rupee loss that no single Greek shows on its own.

This is also where you discover that "delta-neutral" is not "risk-neutral." A book hedged to zero net delta can still lose a fortune in a −5% / +10-vol scenario because of negative gamma and negative vega. The stress test is the honest mirror.

### Portfolio risk limits and the risk budget

Once you can see and stress the book, you manage it to **limits**, not feelings. A professional desk sets hard caps such as:

- **Max net delta:** e.g., book net delta must stay within ±400 index units (beta-weighted). Breach it and you hedge with futures immediately.
- **Max net vega:** e.g., book may not lose more than ₹2,00,000 for a 5-point IV move.
- **Max stress loss:** e.g., the worst cell of the stress grid (−5% spot, +10 vol) may not exceed a fixed rupee loss — say ₹5,00,000, your daily risk budget.
- **Gamma / expiry caps:** tighten position size as expiry nears because gamma balloons.

This is the **risk-budget mindset**: you decide in advance how much you are willing to lose in a bad scenario, and you size and hedge the *whole book* to stay inside that number — rather than judging each trade in isolation and hoping the pile stays safe. New trades are evaluated by what they do to the **aggregate**: "Does adding this short strangle push my stress loss past the budget? Does it concentrate my delta further?" A trade that looks attractive standalone is rejected if it breaks the book's budget. That single reframe — *manage the book to a budget, not the trades to a hope* — is the professional's core discipline, and it is exactly what the ~9-in-10 retail F&O traders who lose money (per SEBI studies) almost never do.

## Worked example (₹, Nifty)

Let us aggregate a realistic four-position Nifty book into net Greeks, flatten its delta with futures, and stress test it. Take **Nifty spot = 24,000**, **lot size = 75 units**, weekly options.

**The book (four positions):**

1. **Long 2 lots** of the 24,000 call (bullish, long vol). Per-unit: delta +0.52, gamma +0.0011, theta −7.0, vega +9.0.
2. **Short 3 lots** of the 24,200 call (you sold upside). Per-unit: delta +0.38, gamma +0.0010, theta −6.0, vega +8.5.
3. **Short 4 lots** of the 23,800 put (you sold downside — income). Per-unit: delta −0.40, gamma +0.0010, theta −6.2, vega +8.5.
4. **Long 1 lot** of the 23,600 put (tail hedge). Per-unit: delta −0.28, gamma +0.0008, theta −4.5, vega +7.0.

**Step 1 — Build the aggregation table.** For each leg, signed contribution = (signed lots) * 75 * (per-unit Greek). Signs: long = +lots, short = −lots.

| Position | Lots (signed) | Net Delta (units) | Net Gamma (units/pt) | Net Theta (₹/day) | Net Vega (₹/1% IV) |
|---|---|---|---|---|---|
| Long 24,000 C | +2 | +0.52*150 = **+78.0** | +0.0011*150 = **+0.165** | −7.0*150 = **−1,050** | +9.0*150 = **+1,350** |
| Short 24,200 C | −3 | +0.38*(−225) = **−85.5** | +0.0010*(−225) = **−0.225** | −6.0*(−225) = **+1,350** | +8.5*(−225) = **−1,912.5** |
| Short 23,800 P | −4 | −0.40*(−300) = **+120.0** | +0.0010*(−300) = **−0.300** | −6.2*(−300) = **+1,860** | +8.5*(−300) = **−2,550** |
| Long 23,600 P | +1 | −0.28*75 = **−21.0** | +0.0008*75 = **+0.060** | −4.5*75 = **−337.5** | +7.0*75 = **+525** |
| **BOOK NET** | | **+91.5** | **−0.300** | **+1,822.5** | **−2,587.5** |

(Here "units" of lots = signed lots * 75; e.g., short 3 lots = −225 units.)

**Step 2 — Read the book.**

- **Net delta = +91.5 units.** The book is **net long Nifty** — mostly because the short 23,800 puts contribute positive delta. If Nifty rises 1 point you make about ₹91.5; if it falls 1 point you lose about ₹91.5. This was not a deliberate directional bet; it accumulated.
- **Net gamma = −0.30 units of delta per point.** The book is **net short gamma** (the three short legs outweigh the two long ones). Net delta will move *against* you on a large swing, and this will worsen into expiry.
- **Net theta = +₹1,822.5 per day.** The book **earns** about ₹1,822 a day from time decay — you are a net seller collecting rent.
- **Net vega = −₹2,587.5 per 1% IV.** The book is **short volatility**: a 1-point India VIX rise costs about ₹2,587; a VIX spike of 10 points would cost roughly ₹25,875 on vega alone.

So in one sentence: this is a **short-vol, short-gamma income book with an unwanted long-delta tilt.** Exactly the kind of profile that earns quietly day to day and is vulnerable to a sharp down-move with a volatility spike.

**Step 3 — Flatten the net delta with futures.**

We do not want the +91.5 of directional lean. We **sell Nifty futures** to cancel it. One Nifty future has delta +1 per unit, so we sell **91.5 units** — about **1.2 lots** of futures (91.5 / 75 ≈ 1.22). In practice you would sell 1 lot (75 units) and accept a small residual +16.5, or use the mini/available contract sizing; the principle is **sell whatever futures delta zeroes the book**.

After selling 91.5 units of futures:

- Net delta: +91.5 − 91.5 = **0**. Directionally flat.
- Net gamma: still **−0.30** (futures have no gamma).
- Net theta: still **+₹1,822.5/day** (futures have no theta).
- Net vega: still **−₹2,587.5** (futures have no vega).

We have surgically removed the directional bet and kept the income engine intact. That is book-level hedging in one move.

**Step 4 — Stress test the (now delta-flat) book.** Net delta is zero, so a *small* move barely registers. But we are short gamma and short vega — the danger is a *big* move plus a VIX spike. Approximate each scenario's P&L as:

`P&L ≈ (delta * spot move) + 0.5 * gamma * (spot move)^2 + (vega * IV change)`

with delta = 0 after the hedge. Take a **−5% Nifty crash = −1,200 points**, with India VIX **+10**:

- Delta term: `0 * (−1,200) = 0`.
- Gamma term: `0.5 * (−0.30) * (−1,200)^2 = 0.5 * (−0.30) * 1,440,000 = −₹216,000`.
- Vega term: `(−2,587.5) * (+10) = −₹25,875`.
- **Total stress loss ≈ −₹241,875**, partly offset over the days by collected theta (a few thousand rupees) — negligible against the shock.

That is the number that matters. Despite being **perfectly delta-neutral**, the book loses roughly **₹2.4 lakh** in a −5% / +10-vol day, driven almost entirely by **negative gamma** (the convex spot loss) with vega adding insult. If your risk budget for a single bad day is ₹2,00,000, this book is **over the limit** — and the fix is not more futures (delta is already zero) but **buying back some short options to cut net gamma and vega**, e.g., closing one or two of the short 23,800 puts. This is precisely the decision the stress test forces, and the Greeks alone would never have shown it.

## Common mistakes / risk note

- **Managing trades instead of the book.** Watching each position's P&L tab while the *aggregate* delta quietly drifts to +600 is how surprises happen. The market sums your positions whether or not you do.
- **Trusting net delta of zero as "safe."** Delta-neutral removes only the *first-order, small-move* directional risk. A delta-flat book that is short gamma and short vega can still lose lakhs in a crash — as the worked example shows. Neutral is a posture, not protection.
- **Ignoring correlation — fake diversification.** Holding a bullish index spread, a short index put, and long Reliance/HDFC Bank feels diversified but is one concentrated "India up" bet. Beta-weight stock deltas into index terms to see the truth, or a single risk-off day will teach it expensively.
- **Forgetting gamma's expiry explosion.** A net-short-gamma book that is comfortable on Monday can become violently sensitive by Thursday expiry as ATM gamma spikes. Reduce size into expiry; do not assume the morning's Greeks hold by afternoon.
- **No stress test, no budget.** Relying only on the four Greeks misses the convex tail. Without a stress grid (−5% spot, +10 vol) and a pre-set rupee loss limit, you discover your worst case *during* the worst case. And remember SPAN + exposure margin balloons exactly when volatility spikes — forcing the worst-timed exits if you are not sized for it.
- **Hedging the wrong Greek with the wrong tool.** Futures fix delta only; they cannot reduce vega or gamma. Trying to "hedge" a volatility problem by trading futures just moves your direction around while the real risk sits untouched.

## Key takeaways

- A professional runs a **book**, not a drawer of trades: the market only sees the **aggregate**, so manage the four net Greeks of the whole portfolio.
- **Greeks aggregate by signed addition:** `Book G = sum of (signed lots * lot size * per-unit G)`. Four sums — net delta, gamma, theta, vega — describe the entire book.
- **Flatten net delta with index futures** (delta ≈ +1 per unit, zero everything else): sell futures to kill positive delta, buy to kill negative, leaving gamma/theta/vega untouched.
- **Vega needs options to hedge; gamma explodes into expiry** — reduce a short-gamma book's size as expiry nears.
- **Correlation can make many trades one bet.** Beta-weight stock deltas into index-equivalent delta to read your honest directional exposure and avoid fake diversification.
- **Stress test** the book across a spot × IV grid; the −5% spot / +10-vol cell usually reveals the true worst case that no single Greek shows. Delta-neutral is not loss-proof.
- **Run the book to a risk budget:** set hard limits on net delta, vega, and stress loss, and judge every new trade by its effect on the aggregate — not in isolation.

## Practice problems

1. **Aggregate the delta (numeric).** A book holds: long 3 lots of a Nifty 24,000 call (delta +0.50), short 2 lots of a 24,300 call (delta +0.30), and short 5 lots of a 23,700 put (delta −0.35). Lot size 75. Compute the book's net delta in index units. Is it net long or short?

2. **Hedge the book (numeric + conceptual).** Using the net delta from problem 1, how many units (and roughly how many lots) of Nifty futures do you trade, and in which direction, to flatten it? Why does this leave net theta and net vega unchanged?

3. **Sign the book Greeks (conceptual).** A book is overall a *net seller* of options (more short premium than long). State the likely sign of its net gamma, net theta, and net vega, and describe in one sentence the market condition it quietly wants and the scenario it fears.

4. **Stress test (numeric).** A delta-flat book has net gamma = −0.20 units/point and net vega = −₹3,000 per 1% IV. Estimate its P&L if Bank Nifty falls 4% from 52,000 (a 2,080-point drop) while India VIX rises 8 points. Use `P&L ≈ 0.5 * gamma * move^2 + vega * IV change`.

5. **Correlation (conceptual).** A trader holds a bullish Nifty call spread, a short Nifty put, and a long position in Reliance futures (beta ≈ 1.1 to Nifty). Each "looks small." Explain why the book's true directional risk is larger than summing the option deltas suggests, and how you would measure it honestly.

6. **Risk budget decision (conceptual + numeric).** Your daily risk budget is a maximum stress loss of ₹3,00,000 in a −5% / +10-vol scenario. Your current book stress-loses ₹2,70,000 in that cell. A new short strangle would add −₹90,000 of stress loss in the same cell. Should you put it on as-is? What could you do to fit it within budget?

## Solutions

1. **Net delta = +33.75 units, net long.** Long call: `+3 * 75 * (+0.50) = +112.5`. Short call: `−2 * 75 * (+0.30) = −45.0`. Short put: `−5 * 75 * (−0.35) = +131.25`. Sum: `112.5 − 45.0 + 131.25 = +198.75`... let us recompute carefully: 112.5 − 45.0 = 67.5; 67.5 + 131.25 = **+198.75 units**. The book is strongly **net long** Nifty (the five short puts contribute large positive delta). To flatten it you would sell about 199 units of futures. *(If you mis-signed the short put's delta, you would get a very different answer — note that shorting a negative-delta put gives positive delta.)*

2. **Sell ≈ 199 units ≈ 2.65 lots of Nifty futures.** Net delta is +198.75, so sell **198.75 units** of futures (each future = +1 delta per unit) to bring net delta to zero; that is about 198.75 / 75 ≈ **2.65 lots** (you would sell 2 or 3 lots and accept a small residual). It leaves net theta and net vega unchanged because a **future has zero theta and zero vega** — it is pure linear delta, so it adjusts only directional exposure and nothing else. That is exactly why futures are the book's delta steering wheel.

3. **Net gamma negative, net theta positive, net vega negative.** A net seller is short more options than long, so gamma is negative (delta moves against you on big moves), theta is positive (you collect daily decay), and vega is negative (you profit if IV falls, lose if it rises). In one sentence: it **wants the market to sit still with falling or steady volatility** (so it harvests theta), and it **fears a sharp move accompanied by a volatility spike** — the down-and-up combination that hits its short gamma and short vega at the same time.

4. **Stress loss ≈ −₹456,200.** Gamma term: `0.5 * (−0.20) * (2,080)^2 = 0.5 * (−0.20) * 4,326,400 = −₹432,640`. Vega term: `(−3,000) * (+8) = −₹24,000`. Total ≈ `−432,640 − 24,000 = −₹456,640` (about −₹4.57 lakh). Even though the book is delta-flat, the **negative gamma** dominates because the loss scales with the *square* of a large move, and the **vega** loss adds to it as IV spikes — the classic short-vol crash scenario.

5. **Because index and large caps are highly correlated, the three positions are really one "India up" bet.** Summing only the option deltas ignores the Reliance exposure entirely and treats correlated positions as independent. The honest measure is **beta-weighted index delta**: convert the Reliance futures delta into index-equivalent units by multiplying by its beta (≈ 1.1) and add it to the option deltas. The combined beta-weighted delta is the book's true directional risk — and on a risk-off day all three lose together, so the real drawdown is larger and more concentrated than the naive delta sum implies. The fix is to read net delta beta-weighted to Nifty and hedge that total with index futures.

6. **No — adding it as-is breaches the budget.** Current stress loss ₹2,70,000 + new ₹90,000 = **₹3,60,000**, which exceeds the ₹3,00,000 limit by ₹60,000. To fit it, either (a) **reduce the new structure's size** — it adds ₹90,000 at full size, so put on at most one-third of it (about ₹30,000 of stress loss) to land at the ₹3,00,000 ceiling, or (b) **first trim existing risk** — buy back some short options or buy a cheap protective wing to cut net gamma and vega — to create headroom, then add the trade. The discipline is that the decision is made against the **book's aggregate stress loss versus the budget**, not on whether the strangle looks attractive on its own.
