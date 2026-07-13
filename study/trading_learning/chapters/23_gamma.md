# Chapter 23: Gamma — The Curvature That Bites Near Expiry

In the last chapter you met delta — how much an option's price moves for a one-point move in the index. But delta is not a fixed number stamped on the option. It shifts. As Nifty climbs, a call's delta drifts up toward 1; as Nifty falls, it drifts down toward 0. **Gamma** is the Greek that measures that drift — it tells you *how fast your delta itself changes* as the market moves. If delta is your speed, gamma is your acceleration.

Why does a second-order number matter so much that professionals obsess over it? Because gamma is what turns a quiet position into a violent one without warning. It is harmless on a long-dated option far from its strike, and it becomes a monster on a Bank Nifty weekly option on expiry afternoon, where a thirty-point flick of the index can flip your whole profit-and-loss from green to red in seconds. This chapter teaches you to *feel* gamma — where it lives, when it explodes, why owning it costs you money every day, and how the pros harvest it.

## Core concepts

### Delta is not constant — gamma measures the change

Recall the payoff of a long call at expiry: flat at zero below the strike, then a straight 45-degree line above it. That bend at the strike is a **kink** — a sudden change in slope. Before expiry, the option's value curve is a *smooth, rounded* version of that hockey stick. Smooth means curved, and **gamma is the curvature of that price curve.**

Put precisely, delta is the *slope* of the option-price-versus-spot curve, and gamma is the *rate of change of that slope*:

`gamma = change in delta / change in spot (per 1-point move)`

In calculus terms, if delta is the first derivative of the option price with respect to spot, gamma is the **second derivative**. You do not need the calculus to trade it; you need the picture. A curve that bends sharply has high gamma; a nearly straight line has near-zero gamma.

A concrete way to read the number: **gamma tells you how many delta-points you gain or lose for each 1-point move in the index.** If a Nifty call has delta 0.50 and gamma 0.004, then if Nifty rises 1 point the new delta is about 0.504; if Nifty rises 10 points the delta climbs to roughly 0.54. The delta is *self-adjusting*, and gamma is the rate of that adjustment.

### The sign of gamma: long options are long gamma

Here is the single most important fact about gamma, and it is beautifully simple:

- **If you BUY an option (call or put), you are LONG gamma.** Your gamma is positive.
- **If you SELL an option (call or put), you are SHORT gamma.** Your gamma is negative.

Notice this is unlike delta, where calls and puts have opposite signs. For gamma, *buying* anything gives you positive gamma; *selling* anything gives you negative gamma. Both a long call and a long put have positive gamma.

What does positive gamma actually *do* for you? It makes your delta move *in your favour*:

- You own a call (positive delta). The market rallies. Gamma pushes your delta *up*, so you get longer and longer exactly as the market keeps rising — you make money at an *accelerating* rate.
- The market instead falls. Gamma pushes your delta *down* toward zero, so you get shorter and shorter — you lose money at a *decelerating* rate. Your losses brake themselves.

This is the magic of **positive convexity**: when you are right you get more right, and when you are wrong you become less exposed. The option buyer's delta is always reshaping itself to lean into the move. That asymmetry — accelerating gains, braking losses — is precisely what you are paying the premium for.

The seller lives in the mirror world. **Short gamma means your delta moves against you.** Sell a call, the market rallies, and your (negative) delta gets *more* negative just as the market climbs — your losses accelerate. The market falls and your short-call delta shrinks toward zero just as you would have wanted it large — your gains decelerate. The short-gamma trader is run over on every sharp move in either direction.

### Where gamma lives: highest at the money

Gamma is not spread evenly across strikes. It is concentrated, and the rule is clean:

**Gamma is highest for at-the-money (ATM) options and falls away to nearly zero for deep in-the-money and deep out-of-the-money options.**

The intuition flows straight from delta. Think about where delta is *changing fastest* as spot moves:

- A **deep ITM** call has delta near 1.00. Push spot up or down a little and the delta barely budges — it is already pinned near 1. Slope is steady, curvature is low, **gamma is tiny.**
- A **deep OTM** call has delta near 0.00. Nudge spot and it stays near 0. Again the delta hardly moves, **gamma is tiny.**
- An **ATM** call has delta around 0.50, and this is exactly the region where delta is *most sensitive* to spot. A small move up flips the option toward "probably finishes in the money" (delta racing toward 1); a small move down flips it toward "probably worthless" (delta sliding toward 0). The delta is on a knife-edge, swinging fast — **gamma peaks here.**

So gamma traces a bell-shaped hump centred on the strike: low in the wings, tall and narrow over the money. The figure below shows this shape — notice how the peak sits right at the at-the-money spot and decays on both sides.

![Figure: gamma vs spot, peaks ATM](figs/gamma.png)

### Where gamma bites: it explodes near expiry

The bell shape tells you *which strike* has the most gamma. The second dimension — and the one that maims retail sellers — is *time*. As expiry approaches, the ATM gamma hump does not just stay put; it grows **taller and narrower**, spiking toward infinity in the final hours.

The reason is the same uncertainty story from the time-decay chapter, viewed through delta. Far from expiry, an ATM option's delta moves gently because there is lots of time for spot to wander either way — a 50-point move today is no big deal when thirty days remain, so delta inches along. But on expiry day, that same ATM option is a coin standing on its edge about to land. A tiny move *now* decides everything: a few points above the strike and the option is going to finish in the money (delta snapping to 1.00); a few points below and it expires worthless (delta collapsing to 0.00). Delta has to travel its entire 0-to-1 range over a razor-thin band of spot. That is enormous curvature — **gamma explodes.**

The figure below makes the time effect concrete: ATM gamma is modest with weeks to go, then rockets up as expiry nears.

![Figure: ATM gamma explodes near expiry](figs/gamma_vs_time.png)

This is the precise mathematical reason Indian **weekly expiries** are so treacherous. A Nifty or Bank Nifty weekly option spends its entire short life in the steep, high-gamma zone, and its final day is the most explosive gamma environment most traders will ever touch. The option seller who is comfortably in profit at 1 p.m. on expiry day can be deep in the red by 2 p.m. on a move that, on any other day, would barely register — because near-expiry ATM gamma converts small spot moves into giant delta swings.

### The gamma-theta trade-off: you rent gamma with theta

Nothing in options is free, and gamma is no exception. There is a hard, unavoidable bargain at the heart of options trading:

**To be long gamma, you must be short theta. To be long theta, you must be short gamma.**

When you buy an option you own positive gamma (good — convexity works for you) but you pay negative theta (bad — the option bleeds time value every day, as Chapter 21 showed). You are essentially *renting* convexity, and theta is the daily rent. Each day the index sits still, you pay that rent and get nothing for it.

The seller takes the opposite side: she collects theta every day (the rent flows to her) but carries negative gamma, the risk that a sharp move blows up in her face. She is paid to insure the buyer against big moves.

So the central question both sides are really betting on is: **will the market move more than the theta is charging for?**

- If realised movement is *large* relative to the premium's daily decay, the long-gamma buyer wins — the convexity earns more than the rent costs.
- If the market is *quiet* relative to the decay, the short-gamma seller wins — she pockets rent while the dreaded move never comes.

And here is the cruellest part of the trade-off for sellers: **gamma and theta both peak at the same place — ATM, near expiry.** The fat theta that tempts sellers into weekly ATM options is inseparable from the fat gamma that can destroy them. You cannot collect the high rent without taking on the high risk. They are two faces of one coin.

### A first look at gamma scalping

If long gamma costs theta every day, how does anyone make money owning it without simply betting on a big directional move? The professional answer is **gamma scalping**, and it is worth meeting now even though it deserves its own deeper treatment later.

The idea: hold a long-gamma position but stay **delta-neutral** — meaning you offset the option's delta with an opposite position in Nifty futures so your net delta is roughly zero and you are not making a directional bet. Now watch what positive gamma does for you:

- The index rises. Your long gamma makes your delta turn *positive*. To get back to neutral you **sell** some futures — locking in a small gain at the higher level.
- The index falls. Your gamma makes your delta turn *negative*. To re-neutralise you **buy** futures — at the lower level.

You are mechanically **buying low and selling high**, again and again, harvested purely from the option's curvature. Each re-hedge banks a little cash. Over a choppy day those crumbs add up. If the total scalped profit exceeds the theta you paid to own the gamma, you come out ahead — *regardless of where the index finally closes.*

That is the whole game in miniature: gamma scalping is a bet that the market will be **more volatile** (move around more) than the option's implied volatility — the theta — is charging you for. It converts the abstract "long gamma, short theta" trade-off into a concrete daily cash-collection routine. The short-gamma seller, naturally, is doing the reverse and praying the market stays calm.

## Worked example (₹, Nifty/Bank Nifty)

Let us watch delta change under gamma, then feel the expiry-day version on Bank Nifty.

**Setup.** Nifty spot is at 24,000. You buy one 24,000 weekly call (ATM). From the option chain you read:

- Premium = ₹120
- Delta = 0.50
- Gamma = 0.004 (delta change per 1-point move in Nifty)
- Lot size = 75 (use the current NSE lot; it changes from time to time)

**Step 1 — Delta after a 50-point rally.** Nifty rises from 24,000 to 24,050, a 50-point move.

`new delta ≈ old delta + gamma * move = 0.50 + 0.004 * 50 = 0.50 + 0.20 = 0.70`

Your call now behaves like 0.70 of a Nifty unit, up from 0.50. You got *longer* simply because the market rose — gamma did that for you.

**Step 2 — Delta after a 50-point fall (from the start).** Now suppose instead Nifty had fallen to 23,950.

`new delta ≈ 0.50 + 0.004 * (-50) = 0.50 - 0.20 = 0.30`

You got *shorter*, down to 0.30. Your downside exposure shrank exactly as the market went against you. This is positive convexity in numbers: bigger delta into the rally, smaller delta into the fall.

**Step 3 — Why this beats a fixed-delta position.** Approximate the option's price change using delta plus the gamma "kicker". For the 50-point rally:

`price change ≈ delta * move + 0.5 * gamma * move^2`
`= 0.50 * 50 + 0.5 * 0.004 * 50^2`
`= 25 + 0.5 * 0.004 * 2500`
`= 25 + 5 = ₹30`

A plain delta estimate would have predicted only ₹25 (0.50 * 50). Gamma added ₹5 of *extra* gain. On the downside the same gamma term *subtracts* from your loss: a 50-point fall costs about `0.50*50 - 5 = ₹20`, not the full ₹25. Per lot of 75, that gamma cushion is worth `5 * 75 = ₹375` of help on each leg — you make more on the way up and lose less on the way down. The option *seller* eats the mirror image: she loses the extra ₹375 on the rally.

**Step 4 — Expiry-day gamma on Bank Nifty.** Now the dangerous version. It is expiry day. Bank Nifty is at 52,000 and you have **sold** one 52,000 call for ₹60 to collect theta — you are short gamma. With only hours to expiry the ATM gamma is enormous; say gamma = 0.02 (five times the relaxed weekly figure, because gamma has spiked into expiry).

Bank Nifty jolts up 100 points to 52,100 on a news headline:

`delta change = gamma * move = 0.02 * 100 = 2.0 ... (delta is capped at 1, so it pins near 1.00)`

Your short call's delta rockets from about -0.50 to nearly -1.00 almost instantly — you are now effectively short a full Bank Nifty future right as it screams higher. The loss on the move, including the gamma term, is roughly:

`loss ≈ delta*move + 0.5*gamma*move^2 = 0.50*100 + 0.5*0.02*100^2 = 50 + 100 = ₹150 per unit`

Against the ₹60 premium you collected, you are now down about ₹90 *per unit* — `90 * 35 = ₹3,150` on one lot of 35 (use the current Bank Nifty lot) — from a single 100-point flick that took two minutes. And if the index keeps running, your now-full delta means you bleed one-for-one with it. That is short gamma on expiry day: the thing that pays pennies of theta for weeks can take rupees in minutes.

## Common mistakes / risk note

- **Selling weekly ATM options "for the theta" without respecting the gamma.** This is the classic retail blow-up. The juicy daily decay you are collecting is inseparable from the gamma that can hand you a multiple of that premium back in one move. The premium is small precisely because it is risky. SEBI's studies showing roughly 9 in 10 F&O traders lose money are populated heavily by exactly this trade gone wrong.
- **Holding short options into the last hour of expiry.** Gamma is at its lifetime maximum then. A position that was safe all week becomes a live grenade on expiry afternoon. Many professionals simply close or roll short gamma before the final hours rather than gamble on pin risk.
- **Treating delta as a constant.** Beginners hedge once with delta and assume they are covered. Gamma means your hedge goes stale the instant the market moves — a delta-hedge set at 24,000 is wrong by lunchtime if Nifty has travelled 80 points. Without re-hedging, gamma quietly rebuilds your exposure.
- **Forgetting that long gamma is not free.** Buying options for the convexity feels safe — your risk is capped at the premium. True, but in a quiet, range-bound market theta grinds that premium to zero day after day while the big move you paid for never arrives. Long gamma loses money in calm markets just as reliably as short gamma loses it in violent ones.
- **Position-sizing on premium, not on gamma risk.** "It's only ₹60, how bad can it be?" The worst-case on a short ATM option near expiry is many multiples of the premium. Size by the move you could suffer, not by the cash you collect. SPAN margin partly forces this on you, but do not let the margin be your only risk check.

## Key takeaways

- **Gamma is the rate of change of delta** per 1-point move in the index — the curvature (second derivative) of the option-price curve. Delta is speed; gamma is acceleration.
- **Buying any option (call or put) is long gamma (positive); selling any option is short gamma (negative).** Long gamma = positive convexity: your delta moves *with* you (gains accelerate, losses brake). Short gamma is the dangerous mirror.
- **Gamma is highest at the money and near-zero deep ITM/OTM**, and it **explodes as expiry approaches** — peaking on weekly expiry day, which is why short weekly options can flip P&L violently on small moves.
- **The gamma-theta trade-off is unavoidable:** to own gamma you pay theta (daily rent); to collect theta you take on gamma risk. Both peak at the same spot — ATM, near expiry.
- **The real bet** under any gamma position is whether realised movement will exceed what the theta is charging — buyers want big moves, sellers want calm.
- **Gamma scalping** harvests long gamma by staying delta-neutral and re-hedging into every move (sell futures as it rises, buy as it falls), banking small profits that beat theta if the market is choppy enough.

## Practice problems

1. **(Conceptual)** A trader says, "I sold a put, so I have positive gamma because puts go up when the market falls." What is wrong with this reasoning? State the correct gamma sign for a short put.

2. **(Numeric)** A Nifty 24,200 call has delta 0.45 and gamma 0.005. Nifty rallies 40 points. Estimate the new delta. If Nifty had instead dropped 40 points, what would the new delta be?

3. **(Numeric)** Using the same option as Problem 2 (delta 0.45, gamma 0.005, premium ₹95), estimate the option's new price after a 40-point rally using `price change ≈ delta*move + 0.5*gamma*move^2`. How much of the gain came from the gamma term alone?

4. **(Conceptual)** Two Nifty calls are quoted: a deep-ITM 23,000 call and an ATM 24,000 call, both expiring this week. Which has the larger gamma, and why? What happens to that comparison as expiry day arrives?

5. **(Numeric / risk)** On Bank Nifty expiry day you are short one ATM 52,000 straddle's worth of gamma with combined gamma 0.03 and you collected ₹140 total premium. Bank Nifty moves 120 points. Roughly estimate your loss per unit using the gamma approximation (take starting net delta ≈ 0 for an ATM straddle). Are you still in profit?

6. **(Conceptual)** Explain in plain English why a gamma scalper can make money even if Bank Nifty closes exactly where it opened, and what market condition would make the same scalper *lose* money.

## Solutions

**1.** The trader is confusing delta with gamma. Yes, a short put has *positive delta* (it profits when the market rises). But **gamma sign depends only on whether you bought or sold**, not on call versus put. Selling *anything* gives **negative gamma**. So a short put is **short gamma**: its delta moves against the seller — as the market falls, the short put's delta turns more positive (longer) just as the trader is losing, accelerating the pain. Correct sign: gamma is negative.

**2.** New delta after a rally: `0.45 + 0.005 * 40 = 0.45 + 0.20 = 0.65`. After a 40-point fall: `0.45 + 0.005 * (-40) = 0.45 - 0.20 = 0.25`. The call gets longer into the rally (0.65) and shorter into the decline (0.25) — positive convexity.

**3.** `price change ≈ 0.45 * 40 + 0.5 * 0.005 * 40^2 = 18 + 0.5 * 0.005 * 1600 = 18 + 4 = ₹22`. New price ≈ `95 + 22 = ₹117`. The gamma term contributed **₹4** of the ₹22 gain; delta alone would have predicted only ₹18. That ₹4 is the convexity bonus that a fixed-delta estimate misses.

**4.** The **ATM 24,000 call has the larger gamma.** Its delta sits near 0.50, the most sensitive region — a small spot move swings the delta sharply, so curvature is high. The deep-ITM 23,000 call has delta near 1.00 and barely responds to spot moves, so its gamma is small. As **expiry day arrives**, the gap widens dramatically: the ATM call's gamma *explodes* (delta must traverse its whole 0-to-1 range over a tiny band of spot), while the deep-ITM call's gamma stays low and even fades further. ATM-versus-ITM gamma divergence is greatest right at expiry.

**5.** Loss ≈ `delta*move + 0.5*gamma*move^2`. With starting delta ≈ 0: `0 + 0.5 * 0.03 * 120^2 = 0.5 * 0.03 * 14400 = ₹216` per unit. You collected ₹140, so you are now down roughly `216 - 140 = ₹76 per unit` — **no longer in profit.** Note the loss came *entirely* from the gamma term because the straddle started delta-neutral; this is pure short-gamma damage, and it grows with the *square* of the move, so a 240-point move would hurt four times as much (≈ ₹864 per unit).

**6.** A gamma scalper holds long options (positive gamma) but neutralises the directional bet by shorting Nifty/Bank Nifty futures against the option delta. As the index swings up during the day, his delta turns positive and he sells futures into the strength; as it swings back down, his delta turns negative and he buys futures into the weakness. He is mechanically **selling high and buying low** on every wiggle, banking small profits — even though the index finishes exactly where it started, the *path* (the chop) generated cash. He **loses** money when the market is **too quiet**: if the index barely moves all day, there are no swings to scalp, and the **theta** he is paying to own the long gamma steadily eats his premium with nothing harvested to offset it. Long gamma wins on movement and loses on stillness.
