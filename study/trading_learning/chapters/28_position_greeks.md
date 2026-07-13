# Chapter 28: Position Greeks — Delta-Neutral & Gamma Scalping

So far you have met the Greeks one option at a time: a single call has this much delta, that much gamma, so much theta. But nobody trades a single option in isolation. A real position is a *basket* — a straddle, a spread, a hedge with futures bolted on — and what matters is the risk of the **whole basket**, not its parts. The good news is that the Greeks were built for exactly this: they simply **add up**. Sum the delta of every leg and you have the position's delta. Sum the gamma, the theta, the vega. The basket's behaviour is just the arithmetic of its pieces.

Once you can see a position's *net* Greeks, a whole professional style of trading opens up. You can deliberately build a position with **zero net delta** — so that small moves in Nifty, up or down, leave you flat — and then make your money from something else entirely: from the market *moving a lot* (if you are long options) or from the market *sitting still* (if you are short options). This chapter teaches you to compute net Greeks, build a delta-neutral position, and run the two engines that sit at the heart of professional options trading: **gamma scalping** and its mirror image, **premium selling**.

## Core concepts

### Greeks add — that is the whole trick

Every Greek is a *rate of change* of the option price, and rates of change are additive across positions. If you own two options, the rate at which your total value changes when Nifty moves one point is just the sum of the two individual rates. So:

`Position delta = sum over all legs of (quantity * delta per option)`

and the same for gamma, theta, and vega. "Quantity" is signed: **positive if you are long the option, negative if you are short.** It is also scaled by lot size when you want the answer in rupees per index point per *lot*, but the cleanest way to think is first in *per-share* (per-unit) Greeks, then multiply by lot size at the end.

A few sign rules you must internalise, because they drive everything below:

- **Long a call:** positive delta, positive gamma, negative theta, positive vega.
- **Long a put:** negative delta, positive gamma, negative theta, positive vega.
- **Short a call:** negative delta, negative gamma, **positive** theta, negative vega.
- **Short a put:** positive delta, negative gamma, **positive** theta, negative vega.

Notice the deep symmetry: **anyone who is long options is long gamma and short theta** (they pay time decay to own convexity), and **anyone who is short options is short gamma and long theta** (they collect time decay in exchange for taking on convex risk). Gamma and theta are two sides of the same coin. Hold that thought — it is the engine of the entire chapter.

### Net delta and what "delta-neutral" means

**Delta** is how much your position's value changes per one-point move in the underlying. A position delta of +50 means: if Nifty rises 1 point, you make about ₹50 (before lot scaling); if it falls 1 point, you lose about ₹50. Delta is your *directional* exposure — your bet on which way the market goes.

**Delta-neutral** means your net position delta is **zero**. A one-point move up and a one-point move down both leave you, to first order, unchanged. You have switched off your directional bet. You are no longer trading the *direction* of Nifty; you are trading something else — its *movement*, its *volatility*, or its *stillness*.

Why would anyone want that? Because direction is the hardest thing to forecast and the easiest way to be wrong. A delta-neutral trader sidesteps the coin-flip of "up or down" and instead bets on a quantity that is often more forecastable: **how much the market will move**, regardless of which way.

### Building delta-neutral: two tools

There are two ways to cancel out delta.

**1. Offset options against options.** A long straddle (long call + long put at the same strike) is *naturally* near delta-neutral when struck at-the-money, because the call's positive delta (about +0.5) and the put's negative delta (about -0.5) roughly cancel. Many option structures are built to be born neutral.

**2. Offset with futures (or the underlying).** Index **futures have a delta of essentially +1 per unit** (one Nifty future moves one-for-one with the index, ignoring the small basis). This makes futures the perfect hedging tool: if your option position has a net delta of, say, **+40 units of Nifty**, you **sell futures worth 40 units** to bring net delta to zero. Sell index futures to kill positive delta; buy futures to kill negative delta. Because a future has zero gamma, zero theta, and zero vega, it adjusts *only* your delta and leaves all your other Greeks untouched — a clean steering wheel.

In India both tools are everyday reality: liquid Nifty and Bank Nifty futures sit right alongside the options, so professionals continuously trim delta with futures while their options supply the gamma, theta, and vega they actually want.

### Gamma: why delta-neutral does not stay neutral

Here is the catch that makes the whole game interesting. **Gamma** is the rate at which your *delta* changes as the underlying moves. If you are long options you have **positive gamma**, which means:

- When Nifty **rises**, your delta becomes **more positive** (your position starts leaning long).
- When Nifty **falls**, your delta becomes **more negative** (your position starts leaning short).

Read that twice, because it is the most beautiful property in options. A long-gamma position *automatically* gets longer as the market rises and shorter as it falls. It leans into winners and away from losers, all by itself. So if you start delta-neutral and Nifty moves, you are no longer neutral — you have *accumulated* a profitable directional position in the direction of the move. The market handed you a winning delta for free.

That free delta is the raw material of **gamma scalping**.

### Gamma scalping: harvesting movement

**Gamma scalping** is the technique of repeatedly resetting a long-gamma, delta-neutral position back to neutral, locking in profit each time the market moves. The recipe:

1. Build a delta-neutral position that is **long gamma** (long options — a straddle is the classic).
2. Nifty moves up. Your positive gamma turns your delta positive — you are now long, and you are in profit on that move.
3. **Re-hedge:** sell futures to bring delta back to zero. You have just **sold high** and pocketed the gain.
4. Nifty moves back down. Now your delta swings negative — you are short into the fall, again profiting.
5. **Re-hedge:** buy futures to return to neutral. You have just **bought low**.

Every oscillation lets you sell into strength and buy into weakness — a disciplined "buy low, sell high" that you are *forced* into by the mathematics, not by judgment. The more the market thrashes around, the more scalps you collect. **You are being paid for realised movement.** This is why gamma scalping is sometimes called "getting paid to be long volatility."

### The catch: theta is the rent you pay

Nothing is free. Remember the coin: **long gamma is also short theta.** To own that lovely positive gamma you bought options, and those options **decay every single day.** Theta is the rent you pay to hold the gamma. Each day your straddle is worth a little less just from the clock ticking.

So gamma scalping is a race between two forces:

- **Gamma profits** — the scalps you collect from re-hedging as the market moves. These grow with *realised volatility* (how much the market actually thrashes).
- **Theta cost** — the daily decay bleeding out of your long options. This is fixed the moment you put the trade on, and it reflects the *implied volatility* you paid.

This gives the single most important equation in volatility trading, in words:

`Gamma scalp profit ≈ value of REALISED volatility − value of IMPLIED volatility you paid`

**You make money only if the market actually moves more than the option's implied volatility was charging you for.** Implied vol (visible through India VIX and the option's own IV) is the *price* of expected movement. When you buy a straddle, you are buying movement at that price. If the market then delivers *more* movement than priced, your scalps beat your theta and you win. If the market goes quiet and delivers *less*, theta grinds you down and you lose — even though you were "neutral" and never made a directional bet at all.

This is the professional's reframing of options: **a long straddle is not a bet on direction; it is a bet that realised volatility will exceed implied volatility.** Direction is hedged away. Volatility is the whole trade.

### The mirror image: short gamma, the premium seller

Flip every sign and you get the other great archetype: the **option seller**. Sell a straddle and you are **short gamma, long theta.**

- **Long theta:** every day, decay flows *into* your pocket. You collect rent. As long as the market sits still, you win automatically — time is on your side.
- **Short gamma:** this is the danger. Your delta moves *against* you. When Nifty rises, your delta goes negative (you get shorter into a rising market — losing); when Nifty falls, your delta goes positive (you get longer into a falling market — losing). To hedge, you are forced to **buy high and sell low** — the exact opposite of the scalper, and you *pay* each time you re-hedge.

So the seller's equation is the inverse: they win if **realised volatility comes in *below* the implied volatility they sold.** They are paid the premium up front (high implied), and they keep it if the market under-delivers on movement. Their nightmare is a violent move — a gap, a crash, an event — where short-gamma losses pile up faster than the theta they collect. This is the honest, brutal asymmetry of selling: **steady small wins from theta, punctuated by occasional large losses from gamma.** It is why naked option selling, popular in India for its smooth equity curve, can blow up an account in a single session when the market gaps.

In short: **gamma scalpers and premium sellers are the same trade run in opposite directions.** One pays theta to own gamma and prays for movement; the other collects theta by being short gamma and prays for calm. Between them they price the difference between implied and realised volatility — the deepest game in options.

## Worked example (₹, Nifty)

Let us do both halves concretely: first sum the net Greeks of a position, then run a gamma-scalping P&L.

**Setup.** Nifty spot is **24,000**. We buy one lot of the **at-the-money long straddle**: long the 24,000 call and long the 24,000 put, weekly expiry. Take the per-unit Greeks (typical ATM weekly values) as:

| Leg | Delta | Gamma | Theta (₹/unit/day) | Vega (₹/unit per 1% IV) |
|---|---|---|---|---|
| Long 24,000 Call | +0.50 | +0.0010 | −7.0 | +9.0 |
| Long 24,000 Put | −0.48 | +0.0010 | −6.5 | +9.0 |
| **Net (per unit)** | **+0.02** | **+0.0020** | **−13.5** | **+18.0** |

**Step 1 — Read the net Greeks.**
- **Net delta ≈ +0.02 per unit** — essentially neutral. The call's +0.50 and put's −0.48 almost perfectly cancel. (The tiny +0.02 is because the put is a hair out-of-the-money relative to the forward; we will neutralise it.)
- **Net gamma = +0.0020 per unit** — positive and doubled (both legs contribute). This is the engine.
- **Net theta = −₹13.5 per unit per day** — we are paying decay on both legs. With a Nifty lot of about **75 units**, that is `13.5 * 75 ≈ ₹1,012 per day` of rent.
- **Net vega = +₹18 per unit per 1% IV** — long volatility; an India VIX drop will hurt the mark-to-market, a spike will help.

**Step 2 — Make it exactly delta-neutral.**
Net delta is +0.02 per unit, or `0.02 * 75 = +1.5` units of Nifty per lot. To zero it we sell a tiny sliver of futures — `1.5` units. In practice on one lot this is a rounding detail, but on **20 lots** the net delta would be `+30` units, and we would sell **30 units of Nifty futures** to flatten it. The principle scales: *whatever your net option delta is, trade the opposite in futures.*

**Step 3 — Gamma scalp through an intraday move.**
Now run the position through a day. Net gamma is `0.0020 * 75 ≈ 0.15` delta-units **per lot per 1-point move** — meaning every 1-point move in Nifty changes our delta by 0.15 units. Let us trade 20 lots so the numbers are visible: **position gamma ≈ 3.0 units of delta per Nifty point** (`0.15 * 20`).

Nifty starts at 24,000, delta-hedged to zero. Watch it move intraday:

- **Nifty rises 100 points to 24,100.** Gamma turns our delta positive: `delta gained ≈ gamma * move = 3.0 * 100 = +300` units. Roughly speaking we picked up an *average* long exposure of about `+150` units across that 100-point climb (delta ramped from 0 to +300 linearly), so the gain on the move is about `150 * 100 ≈ ₹15,000`. We **re-hedge: sell 300 units of futures** at 24,100, banking the rise and resetting delta to zero.
- **Nifty falls 100 points back to 24,000.** Now from a flat delta, gamma drives delta negative as it drops: it reaches about `−300` units at 24,000. We were *net short* into the fall — averaging about `−150` units over the 100-point drop — so we gain about `150 * 100 ≈ ₹15,000` again. We **re-hedge: buy 300 units of futures** at 24,000, back to neutral.

Two scalps, one round trip, roughly **₹30,000 of gamma profit** — and crucially, Nifty ended exactly where it started. We made money purely from the *path*, the back-and-forth, not from any net direction.

**Step 4 — Net the theta against it.**
That day's theta cost on 20 lots is `13.5 * 75 * 20 ≈ ₹20,250`. So the day's net:

`Net P&L ≈ gamma scalps − theta = 30,000 − 20,250 ≈ +₹9,750.`

We came out ahead because the **realised movement (a 200-point round trip) was large enough to beat the implied volatility we were paying for.** Had Nifty instead drifted just 20 points all day, our scalps might have totalled only ₹2,000–3,000 against the same ₹20,250 of theta — a clear **loss**, despite being perfectly delta-neutral the whole time. That is the trade in a nutshell: **delta-neutral does not mean risk-free; it means your P&L is now a pure bet on realised vs implied volatility.**

## Common mistakes / risk note

- **Thinking delta-neutral means safe.** It only removes *first-order direction*. You are still fully exposed to gamma, theta, and vega. A delta-neutral long straddle loses every quiet day; a delta-neutral short straddle can be destroyed by a single gap. Neutral is a starting posture, not a safety guarantee.
- **Forgetting that gamma scalping needs *realised* movement, not a *forecast*.** Buying a straddle because "a big move is coming" only pays if the move *actually arrives and exceeds the implied vol you paid*. If the event passes quietly, implied vol collapses (the dreaded **IV crush**), your vega loses *and* theta keeps bleeding. Many Indian traders buy expiry-week or pre-results straddles and lose on a flat tape.
- **Re-hedging too often or too rarely.** Scalp on every tiny wiggle and transaction costs (brokerage, STT, slippage) eat your scalps alive — and Indian STT plus charges are not trivial at high frequency. Re-hedge too rarely and you give back gains when the market reverses before you lock in. Choosing the re-hedge band is the real craft.
- **Underestimating the seller's tail.** Short gamma feels wonderful — smooth daily theta income — right up until it doesn't. The losses are convex: a 2% Nifty gap can wipe out months of collected premium. Sizing for the *gap*, not the average day, is what separates surviving sellers from blown-up ones.
- **Ignoring lot-size and margin reality.** Net Greeks must be scaled by lot size to mean anything in rupees, and short-gamma positions carry heavy SPAN + exposure margin that balloons exactly when volatility spikes — forcing the worst-timed exits.

## Key takeaways

- **Position Greeks are just the signed sum of leg Greeks:** add delta, gamma, theta, vega across all legs (long positive, short negative), then scale by lot size for rupees.
- **Delta-neutral** means net delta zero — no first-order directional exposure. Build it by offsetting options against options, or by trading **futures (delta ≈ +1 per unit)** against your option delta.
- **Long options = long gamma + short theta;** **short options = short gamma + long theta.** Gamma and theta are two sides of one coin.
- **Gamma scalping:** hold long gamma delta-neutral, then re-hedge as the market moves — you are forced to sell high and buy low, harvesting **realised volatility**, while paying **theta** as rent.
- The core trade-off: **a long straddle profits only if realised volatility exceeds the implied volatility you paid.** Direction is hedged away; volatility is the whole bet.
- **Premium sellers** run the mirror: collect theta, short gamma, and win only if **realised volatility stays below the implied vol they sold** — with smooth gains punctuated by sharp, convex tail losses.
- **Neutral is not safe.** A delta-neutral book is a pure implied-vs-realised volatility position, with real money at stake every day.

## Practice problems

1. **Net delta (conceptual + numeric).** You are long 2 lots of a Nifty 24,000 call (delta +0.55 each) and short 1 lot of a Nifty 24,200 call (delta +0.35). Lot size 75. What is your net delta in units of Nifty? Are you net long or short the market?

2. **Hedge with futures.** Your option book has a net delta of **−1,800 units** of Nifty. How many units of Nifty futures, and in which direction (buy/sell), do you trade to become delta-neutral? Why does this leave your gamma and theta unchanged?

3. **Sign the Greeks.** For a **short** at-the-money Nifty straddle (short call + short put), state the sign of net delta, net gamma, net theta, and net vega, and say in one sentence what market condition this position wants.

4. **Gamma scalp P&L (numeric).** A delta-neutral position has gamma of **2 units of delta per Nifty point**. Nifty moves from 52,000 (Bank Nifty) up 150 points and back to 52,000. Estimate the gamma-scalp profit from the round trip (use the average-delta method). If theta for the day is ₹18,000, did the position make or lose money?

5. **Implied vs realised (conceptual).** You buy a Nifty straddle when India VIX is 16. Over the week, Nifty barely moves and realised volatility works out to about 10 annualised. Without computing anything, explain whether your gamma-scalping campaign made or lost money, and which Greek did the damage.

6. **The seller's nightmare.** A trader sells weekly Nifty straddles and is delighted by months of steady profits. One morning Nifty gaps down 3% on global news. Explain, using gamma and theta, why a single day can erase months of gains, and what the trader's re-hedging is forced to do during the crash.

## Solutions

1. **Net delta = +0.75 units, net long.** Long leg: `2 lots * 75 * (+0.55) = +82.5` units. Short leg: `−1 lot * 75 * (+0.35) = −26.25` units. Net: `82.5 − 26.25 = +56.25` units of Nifty. (If the question is read as per-unit before lot scaling, it is `2*0.55 − 1*0.35 = +0.75` per unit, which times 75 gives the same +56.25.) Positive net delta means you are **net long** — you profit if Nifty rises.

2. **Buy 1,800 units of Nifty futures.** Net delta is −1,800 (you behave like a short position), so you add **+1,800** of delta by **buying** 1,800 units of futures, bringing the total to zero. It leaves gamma and theta untouched because **a future has zero gamma, zero theta, and zero vega** — it is pure linear delta. Futures are a clean delta steering wheel: they move only the directional exposure and nothing else.

3. **Net delta ≈ 0** (the ±0.5 deltas cancel at the money), **net gamma negative**, **net theta positive**, **net vega negative.** Being short both options, you are short gamma and short vega but long theta. The position **wants the market to sit still** (low realised volatility) and ideally wants implied volatility to fall — it collects theta as long as Nifty does not make a large move.

4. **Scalp profit ≈ ₹45,000; net ≈ +₹27,000.** On the 150-point rise, delta ramps from 0 to `2 * 150 = +300` units, averaging about +150 units, so the gain on that leg ≈ `150 * 150 ≈ ₹22,500` (equivalently `0.5 * gamma * move^2 = 0.5 * 2 * 150^2 = ₹22,500`); re-hedge by selling 300 units at the top. The 150-point fall back to 52,000 earns another ₹22,500 the same way, re-hedged by buying 300 units at the bottom. Total scalps ≈ **₹45,000.** Against theta of ₹18,000, the position **made money: net ≈ +₹27,000.** With gamma = 2 and a 150-point round trip, the realised movement comfortably beat the day's decay, so it is a winning day.

5. **It lost money, and theta did the damage.** You paid for movement priced at 16 vol but the market delivered only about 10 — realised came in *well below* implied. With little movement, your gamma scalps were tiny, while theta bled out of your long straddle every day regardless. On top of that, a quiet market usually means India VIX drifts lower, so your positive **vega** lost on the IV decline too. The campaign loses because **realised volatility (10) fell short of the implied volatility (16) you paid** — exactly the condition under which long gamma cannot pay its own rent.

6. **Because the seller is short gamma, and a gap is the one event short gamma cannot survive.** On calm days, **long theta** drips steady premium into the account — the smooth equity curve. But a 3% gap is a huge, *instantaneous* move with no chance to re-hedge along the way, and **short gamma** means the loss grows with the *square* of the move: a move 5x larger than a normal day produces a loss roughly 25x larger, dwarfing any single day's theta. During the crash the seller's delta swings sharply positive (the short puts deltas balloon), so to re-hedge they are **forced to sell futures into the falling market — locking in losses, selling low** — the exact opposite of the scalper's buy-low/sell-high. One gap thus delivers a convex loss that can exceed many months of accumulated theta, which is the defining asymmetry — and danger — of premium selling.
