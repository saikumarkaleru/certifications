# Chapter 29: Greeks Through a Trade — How They Evolve

You have now met the Greeks one by one: delta, gamma, theta, vega, rho. Each chapter froze the world, changed one thing, and asked how the option's price responded. That is the right way to *learn* the Greeks, but it is not how you *live* with them. In a real trade nothing stays frozen. Spot moves, a day passes, India VIX jumps, and all five Greeks shift at once — and worse, they shift *each other*. Delta is not a fixed number; gamma is busy changing it. Theta is not a constant drip; it accelerates. Vega quietly shrinks as expiry approaches even if you do nothing.

This chapter stitches the Greeks back together into a single living picture. We will follow one Nifty position through several days — a "diary" of a trade — and watch every Greek update in rupees as the market moves under it. The goal is the most important mindset shift in this book: you stop seeing an option as a *price* you bought and start seeing it as a *bundle of risks* you are holding, each one changing every minute. That shift is what separates a punter from a professional.

## Core concepts

### The Greeks are a system, not a list

Think of your option position as a car driving over hills. **Delta** is your speed — how fast P&L changes as spot moves. **Gamma** is your acceleration — how fast that speed itself changes. **Theta** is fuel quietly burning whether you move or not. **Vega** is how sensitive the whole ride is to the "weather" (volatility). You never watch just one gauge; you watch them together, because a change in spot moves the speedometer (delta) *and* the accelerometer (gamma) *and* alters how much fuel you have left.

The key professional insight: **the Greeks are derivatives of each other.** Gamma is the rate of change of delta. Charm (from the last chapter) is the rate of change of delta as time passes. So when you ask "what will my delta be tomorrow if Nifty rises 200 points?", you are really asking gamma and charm to answer. Holding a position means continuously re-reading all the gauges, not setting them once.

### How a long call's delta evolves: gamma in action

Start with the cleanest case — you are **long one Nifty call**. Delta tells you the option's equivalent exposure: a delta of 0.50 means the call currently behaves like holding 0.50 lots of Nifty futures. But that 0.50 is a snapshot. As spot moves, delta is dragged around by **gamma**.

- **As the call goes in-the-money (ITM):** spot rises above the strike, the option becomes more and more certain to finish with value, and its delta climbs toward **1.0**. Deep ITM, the call moves almost rupee-for-rupee with Nifty — it is effectively a long futures position.
- **As the call goes out-of-the-money (OTM):** spot falls below the strike, the option becomes more likely to expire worthless, and its delta decays toward **0**. Deep OTM, it barely responds to spot at all — a near-dead instrument.
- **At-the-money (ATM):** delta sits near **0.50**, and this is exactly where **gamma is highest**. The delta is changing fastest here, because the option is poised on the knife-edge between "will finish worthless" and "will finish valuable."

So gamma is the engine that *rewrites* delta as spot travels. A long option always has **positive gamma**: your delta automatically grows in your favour (rises as you go ITM, falls as you go OTM). That is the friendly half of being long options. The unfriendly half is theta.

### How theta bleed accelerates near expiry

**Theta** is the premium an option loses to the simple passing of time, holding spot and volatility constant. For a long option, theta is a cost — your position bleeds a little value every day. The crucial dynamic is that **this bleed is not steady; it accelerates as expiry nears**, and it is sharpest for at-the-money options.

The reason is that an option's *time value* (everything above its intrinsic value) must decay to exactly zero at expiry. Far from expiry, with weeks to go, that decay is gentle and spread out. In the final days — especially for the weekly Nifty and Bank Nifty options that dominate Indian volumes — the remaining time value collapses. Roughly, time value decays in proportion to `sqrt(time remaining)`, so the loss per day grows as the clock runs down. An ATM weekly option might shed a few rupees per day early in the week and then dump a large chunk on its final day or two.

This is why the long-option holder is in a race: gamma is helping you (delta grows in your favour on a move), but theta is taxing you every day, and the tax bill rises as expiry approaches. **High gamma and high theta are two sides of the same coin** — the ATM near-expiry option that gives you the most explosive delta also charges you the steepest daily rent.

### How vega fades as expiry nears

**Vega** measures how much the premium changes when implied volatility (read off India VIX for the index) moves by one point. The structural fact to internalise: **vega shrinks as expiry approaches.** A longer-dated option has more time for volatility to act, so a change in the *assumed* volatility moves its price a lot — high vega. A weekly option that expires in three days gives volatility almost no runway, so its price is far less sensitive to an IV change — low vega.

The practical consequence for an Indian trader: the *same* India VIX move hits your monthly position much harder than your weekly position. As your option ages from a monthly into its final week, its vega quietly drains away even if you never touch it. So a trade that began as a "volatility bet" gradually becomes a pure "direction-and-time" bet as the calendar advances. You did not change your view; the Greek changed under you.

### Putting it together: the four forces on a long call

At any instant, the change in your long call's value is approximately the sum of the Greek contributions:

`change in premium ≈ delta*(change in spot) + 0.5*gamma*(change in spot)^2 + theta*(days passed) + vega*(change in IV)`

Read it as a sentence: *I make/lose delta for the move, gamma sweetens a big move (it is squared, so it always helps a long-option holder), theta charges me rent for the days, and vega pays or charges me for the shift in fear.* Every one of these terms uses a Greek that is itself changing — which is why we must watch the trade unfold rather than trust the opening snapshot.

The figure below shows the analogous picture for a **put**: how a put's delta evolves with spot, running from near 0 when the put is deep OTM (spot high above the strike) toward -1 when it is deep ITM (spot far below the strike), passing through about -0.50 at the money.

![Figure: put delta vs spot](figs/delta_put.png)

## Worked example (₹, Nifty/Bank Nifty)

Let us keep a real diary. You buy **one lot of a Nifty 24,000 weekly call** on Monday, with expiry that Thursday. One lot is 75 (lot sizes change over time; we use 75 here). Nifty spot is at 24,000 — your call is exactly at-the-money.

**Monday (Day 0): the opening snapshot.** India VIX is 13. The call costs **₹130** per share. Your Greeks per share:

- Delta = **0.50** (ATM, as expected)
- Gamma = **0.004** (delta changes by 0.004 for each 1-point Nifty move)
- Theta = **−₹9 per day** (you bleed about ₹9 of premium daily, all else equal)
- Vega = **₹6 per IV point**

Per lot, you paid `130 * 75 = ₹9,750`. Your effective directional exposure is `delta * lot = 0.50 * 75 = 37.5` "Nifty units" — like being long 37.5 shares of the index.

**Tuesday (Day 1): Nifty rallies 150 points to 24,150.** Now walk the Greeks. The move is +150.

- Delta effect: `0.50 * 150 = +₹75` per share.
- Gamma effect: `0.5 * 0.004 * 150^2 = 0.5 * 0.004 * 22,500 = +₹45` per share. Gamma rewarded the big move.
- Theta effect: one day passed, `−₹9` per share.
- Vega effect: the rally was calm, so VIX *fell* from 13 to 12, a −1 point change: `6 * (−1) = −₹6` per share.

Net change ≈ `75 + 45 − 9 − 6 = +₹105` per share. The call is now worth about **₹235**. Per lot that is a gain of `105 * 75 = ₹7,875`.

But notice what happened to the *Greeks themselves*. The call is now ITM, so **delta has risen to about 0.62** (gamma did this automatically). Gamma has eased slightly. And one day closer to Thursday expiry, **theta has worsened to about −₹12 per day** and **vega has slipped to about ₹4.50**. Your position is now more directional, decaying faster, and less sensitive to volatility than it was yesterday — even though you did nothing.

**Wednesday (Day 2): Nifty stalls, drifts back 50 points to 24,100.** The move is −50, and it is the second-last day.

- Delta effect: `0.62 * (−50) = −₹31` per share.
- Gamma effect: `0.5 * 0.0038 * 50^2 = +₹4.75` per share (gamma still adds on the squared term).
- Theta effect: `−₹12` per share — and this is the accelerating bleed biting.
- Vega effect: VIX flat, ≈ ₹0.

Net ≈ `−31 + 4.75 − 12 + 0 = −₹38` per share. The call drops to about **₹197**. The lesson is visible: a modest pullback *plus* heavy late-week theta wiped out a chunk of value. With expiry one day away, **delta is back near 0.57, gamma is very high, theta is now around −₹18/day, and vega has shrunk to about ₹3.**

**Thursday (Day 3): expiry day decision.** Nifty is at 24,100, your 24,000 call is ₹100 ITM in intrinsic value but still carries a sliver of time value that will vanish by close. You are now holding an almost-pure directional bet with brutal theta and explosive gamma — a coin flip on the last few hours. This is the moment the Greeks tell you to *act*: either book the ₹197-ish premium (a healthy gain on your ₹130 cost), or accept that the remaining time value is about to be incinerated. A professional reads the Greek profile — tiny vega, huge theta, gamma-dominated — and recognises this is no longer the trade they put on Monday. They exit or roll.

### Managing the position by its Greeks

The diary shows the levers a trader actually pulls:

- **Adjust (re-hedge) when delta drifts too far from your intent.** If you wanted a roughly directional bet sized at 37.5 units and gamma has pushed delta to 0.62 (46.5 units), you can sell a small amount of futures or a higher call to trim delta back. Option sellers running delta-neutral books do this constantly — re-hedging to flat as gamma keeps nudging delta.
- **Watch theta versus your edge.** If your reason to be long is a *view that needs time to play out*, accelerating late-week theta is your enemy; roll to a later expiry before the bleed peaks. If you have no fresh catalyst, the rising theta is a signal to exit.
- **Respect vega around events.** Before a budget, RBI policy, or major data, India VIX is often elevated and your long vega is rich; that same vega can collapse the moment the event passes ("IV crush"), hurting long-option holders even if direction was right.
- **Exit when the trade is no longer the trade you analysed.** By Thursday the Greek mix had completely changed character. Holding on out of habit means holding a *different* risk than the one you signed up for.

### The mindset shift: from price to risk

The beginner stares at the premium: "I paid ₹130, it's ₹197, I'm up." The professional stares at the Greeks: "I am long 46 units of delta, long gamma, paying ₹18 a day in theta, with only ₹3 of vega left and a day to expiry." Same position, two completely different mental models. Price is a single backward-looking number. The Greeks are a forward-looking *risk profile* that tells you what will happen next under every scenario — a 1% rally, a quiet day, a VIX spike. Trading by price is gambling on an outcome; trading by Greeks is managing a portfolio of risks. That is the leap this entire Part has been building toward.

## Common mistakes / risk note

- **Trusting the opening snapshot.** The biggest error is sizing a trade by Monday's Greeks and never updating them. By Wednesday your delta, theta, and vega can be unrecognisable. Re-read the gauges every day.
- **Forgetting that gamma and theta are linked.** Beginners love high-gamma near-expiry weeklies for the explosive moves and ignore that the *same* options carry savage theta. You cannot have the cheap lottery ticket without the fast bleed.
- **Being long options into an IV crush.** Buying expensive options before a known event (high VIX) and being right on direction but still losing money because vega collapsed afterward is one of the most common, demoralising retail mistakes.
- **The honest risk.** A long option is a decaying asset; most expire worthless, and time is working against you every single day, faster near expiry. Option *selling* turns these Greeks around in your favour (positive theta, short vega) but exposes you to large, potentially undefined losses when gamma works against you on a sharp move. SEBI studies show roughly nine in ten retail F&O traders lose money — frequently because they held a decaying long position too long, or sold gamma they could not manage. Understanding how the Greeks *evolve* is precisely the defence against being on the wrong side of these forces.

## Key takeaways

- The Greeks form a connected system that changes continuously; gamma rewrites delta, charm and theta change things as time passes, and vega fades with the calendar.
- A long call's delta rises toward 1 as it goes ITM and falls toward 0 as it goes OTM — gamma is the engine, and gamma peaks at-the-money.
- Theta bleed accelerates as expiry nears (roughly with `sqrt(time)`), hitting ATM weekly options hardest in their final days.
- Vega shrinks as expiry approaches, so a position's volatility sensitivity quietly drains away even if you do nothing.
- Manage a position by its Greeks: adjust when delta drifts, roll or exit when theta peaks, respect vega around events, and recognise when the trade has become a different risk.
- The professional mindset reads a position as a live risk profile (delta, gamma, theta, vega), not as a single price.

## Practice problems

1. **Conceptual.** You are long an ATM Nifty weekly call on Monday. Without any change in spot or volatility, will your delta, gamma, theta, and vega be larger or smaller by Wednesday? Explain the direction of each.

2. **Numeric.** A Nifty 52,000 (Bank Nifty) call has delta 0.45, gamma 0.003, theta −₹20/day, vega ₹8. Overnight Bank Nifty rises 300 points and India VIX rises 2 points. Using the Greek decomposition, estimate the change in the call's premium per share. (Treat one day as passing.)

3. **Conceptual.** Two traders both hold a Nifty 24,000 call. One bought a 30-day monthly; the other bought a 3-day weekly. India VIX jumps 3 points. Whose position gains more from the VIX move, and why?

4. **Numeric.** After the move in Problem 2, the call's delta has risen to 0.60. You originally wanted exposure equivalent to about 0.45 of a lot. By how much (in delta terms) are you now over-exposed, and name one way to trim it back.

5. **Conceptual / risk.** A trader buys an ATM weekly call the evening before the RBI policy announcement when India VIX is unusually high. The next day the market moves up modestly in the trader's favour, yet the call *loses* money. Give the most likely Greek explanation.

6. **Numeric.** An ATM weekly call is worth ₹120 with 4 days left. Assuming its remaining time value decays roughly in proportion to `sqrt(days left)` and it is entirely time value, estimate its value after one day passes with spot and IV unchanged. What does this say about late-week theta?

## Solutions

1. By Wednesday, two days closer to expiry: **gamma is larger** (gamma rises for ATM options as expiry nears), **theta is larger in magnitude** (the bleed accelerates), **vega is smaller** (volatility sensitivity fades with time), and **delta** stays near 0.50 *only if* the option is still exactly ATM — but its sensitivity to spot is now sharper because gamma is higher. The headline: the option becomes a more violent, faster-decaying, less vol-sensitive instrument as expiry approaches.

2. Decompose the move (change in spot = +300, one day passes, change in IV = +2):
   - Delta: `0.45 * 300 = +₹135`
   - Gamma: `0.5 * 0.003 * 300^2 = 0.5 * 0.003 * 90,000 = +₹135`
   - Theta: `−₹20`
   - Vega: `8 * 2 = +₹16`
   - Net ≈ `135 + 135 − 20 + 16 = +₹266` per share. (Per lot of 35, that is about `266 * 35 = ₹9,310`; lot sizes vary, so scale to the current Bank Nifty lot.) Note how gamma contributed as much as delta on a 300-point move — the value of being long gamma on a large move.

3. **The monthly holder gains more.** Vega scales with time to expiry: the 30-day option has far more vega than the 3-day option, because volatility has more runway to act over a month than over three days. A 3-point VIX jump therefore lifts the monthly premium substantially while the weekly barely responds. This is exactly why vega fades as expiry nears.

4. You are now at delta 0.60 against a target of 0.45, so you are **over-exposed by 0.15 of delta** (about 0.15 of a lot of long Nifty exposure). To trim it back toward 0.45 you can **sell a small amount of the underlying futures, or sell a higher-strike call** to shed roughly 0.15 of delta, restoring your intended directional size. This is routine delta re-hedging — gamma keeps pushing delta away from target, and you keep nudging it back.

5. The most likely culprit is **vega and an IV crush.** Before the RBI event, implied volatility (India VIX) was elevated, so the trader paid a rich, vega-heavy premium. Once the announcement passed and uncertainty resolved, IV collapsed. The negative vega impact from the falling IV outweighed the positive delta gain from the modest favourable move, so the call lost money despite direction being right. Late-week theta on an expiry-week option would have added to the loss.

6. With 4 days left the time value is ₹120. After one day, 3 days remain. Scaling by `sqrt(days)`: new value ≈ `120 * sqrt(3)/sqrt(4) = 120 * 1.732/2 = 120 * 0.866 ≈ ₹104`. So the option loses about **₹16 in a single day** — a 13% drop purely from time. Repeat the calculation from 2 days to 1 day: `value at 2 days = 120*sqrt(2)/2 ≈ ₹85`, and from 2 to 1 it falls to `120*sqrt(1)/2 = ₹60`, a **₹25 drop**. The per-day loss grows as expiry approaches — that is accelerating late-week theta in numbers, and why holding long weekly options into the final days is a race against a steepening clock.
