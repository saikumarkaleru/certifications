# Chapter 24: Theta — Time Decay, the Buyer's Enemy and Seller's Friend

An option is a melting ice cube. The moment you buy one, a clock starts running, and every day that clock ticks, a little of what you paid evaporates — even if the market does nothing at all. The stock sits still, the news is quiet, the screen is calm, and yet by tomorrow your option is worth slightly less than today simply because there is one fewer day for it to come good. That silent, relentless leak is **time decay**, and **theta** is the Greek that measures it: the rupees of premium an option loses for each day that passes.

Theta is the most emotionally loaded of the Greeks because it is the one thing in options that is genuinely certain. Delta, gamma, vega — those depend on what the market does. Theta happens whether the market moves or not. For the option *buyer* it is a tax on patience, the rent paid for holding a bet. For the option *seller* it is income, the rent collected. This single asymmetry — that time hurts the buyer and helps the seller — explains an enormous amount of how professional Indian options trading actually works, and why so many desks are structurally short premium going into a weekly expiry.

## Core concepts

### What theta actually measures

**Theta** is the change in an option's premium for the passage of **one day**, holding everything else — spot, volatility, interest rates — constant.

`theta = change in option premium per one day of time passing`

By convention theta is quoted as a **negative number for a long option**, because the premium falls as time passes. If a Nifty call has a theta of `-8`, it means that option is expected to lose about ₹8 of premium per day from time decay alone, all else equal. Spread across the lot (Nifty lot size is currently about 75 units), that is roughly `8 * 75 = ₹600` bleeding out of a long position each calendar day.

The signs follow directly from who benefits:

- **Long options have negative theta.** You own a melting asset; time works against you. Every quiet day is a day of premium lost.
- **Short options have positive theta.** You sold the melting asset; time works *for* you. Every quiet day, the option you are short becomes cheaper to buy back, and the difference is your profit.

This is the cleanest statement of the buyer-versus-seller divide from Chapter 15, now made precise: **the buyer pays theta; the seller harvests it.**

### Why time decay exists at all

Recall the split from Chapter 6: an option's premium is **intrinsic value** (how much it is in-the-money right now) plus **time value** (everything else — the value of the *possibility* that it ends up further in-the-money). Theta acts almost entirely on the time-value part.

Time value is the price of optionality, and optionality is worth more when there is more time for things to happen. A 30-day option has thirty days of possible market moves still ahead of it; a 1-day option has only one. As expiry approaches, the menu of things that *could* still happen shrinks, so the value of that possibility shrinks with it. At the instant of expiry, time value is exactly zero — an option is worth only its intrinsic value, nothing more, because there is no future left to pay for.

So theta is not a market opinion or a fee anyone charges. It is the arithmetic of a shrinking opportunity set. Each day, the option has less runway, so the part of its price that was paying for "what might still happen" gets smaller.

### Why ATM theta accelerates near expiry but OTM theta is steadier

This is the single most important practical fact about theta, and it trips up almost every beginner. **Time decay is not linear.** An option does not lose the same rupees each day. The *pattern* of decay depends sharply on moneyness.

For an **at-the-money (ATM)** option — strike near the current spot — time value is at its maximum, and it decays *slowly at first and then faster and faster as expiry nears.* The shape is like a ball rolling off a table that steepens near the edge: gentle far out, a cliff right at the end. Roughly, ATM time value decays in proportion to `sqrt(time remaining)`, so the decay *rate* (theta) behaves like `1 / sqrt(time remaining)` — and that blows up as time remaining goes to zero. With four times less time left, decay runs about twice as fast; in the last day it is brutal.

For an **out-of-the-money (OTM)** option — strike well away from spot — the story is gentler. An OTM option has little time value to begin with (and no intrinsic value), so there is less to bleed. Its decay is steadier and slower in rupee terms, without the violent end-of-life cliff, because by then most of its small value has already quietly drained away. A far-OTM option spends its last days as a near-worthless lottery ticket decaying gently toward zero.

The intuition: theta is largest where time value is largest, and time value is largest **at the money, close to expiry.** That is the exact corner of the option grid — ATM, near expiry — where decay is most savage. It is also, not coincidentally, where most Indian weekly-expiry trading concentrates.

![Figure: theta vs spot](figs/theta.png)

The figure plots theta against the spot price. Notice the deep trough centred at the strike: theta is most negative (decay is fastest) for the at-the-money option and tapers toward zero as you move far in- or out-of-the-money in either direction. Deep ITM and deep OTM options have little time value left to lose, so their theta is small; the ATM option, holding the most time value, bleeds the fastest. As expiry nears, this trough deepens and narrows — the decay concentrates ever more tightly around the at-the-money strike.

### The deep link to gamma: no cheap convexity

Here is where theta stops being an isolated fact and connects to the whole structure of options. Theta and **gamma** (Chapter 23, the rate at which delta changes) are two sides of the same coin. They have **opposite signs and they travel together.**

- A **long option** has **positive gamma** (its delta moves in your favour as spot moves — you accelerate into gains, decelerate into losses) and **negative theta** (it decays). You are paid in convexity but you pay in time.
- A **short option** has **negative gamma** (delta moves against you — the dangerous "wrong-way" acceleration) and **positive theta** (it earns time decay). You are paid in time but you pay in convexity risk.

There is no free lunch here, and the link is almost mathematical. In the Black-Scholes world, for a position with no directional or vol bias, the daily theta you pay is essentially the rent for the gamma you own, scaled by how much the market actually moves:

`theta (per day) ≈ -0.5 * gamma * (expected daily move in points)^2`

Read that sentence carefully, because it is the heart of options trading. **High gamma comes bundled with high theta.** You cannot buy the convexity of a near-expiry ATM option — the explosive, fast-moving delta that makes lottery-ticket gains possible — without simultaneously paying the steepest time decay in the market. The two are quoted by the same formula. If you want a lot of gamma, the market makes you rent it at a high theta; if you want to collect a lot of theta, you must sell a lot of gamma and accept that the position will hurt fast when spot runs.

So "buy weekly options for the gamma" and "sell weekly options for the theta" are *the same trade seen from opposite ends.* The buyer is long gamma / short theta; the seller is short gamma / long theta. Whoever is right about how much the market actually moves, relative to what the premium implied, wins. Theta is simply the price tag the market has stapled to gamma.

### How sellers harvest theta — and the tail they accept

Because short options have positive theta, selling premium is, on a calm day, like being a landlord: the buyer pays you rent every day the option decays. A trader who sells a Nifty straddle (short the ATM call and the ATM put) on a quiet expiry week collects theta from both legs and watches the position bleed in their favour. This is the engine behind an enormous share of Indian options activity: structured premium-selling, "theta harvesting," income strategies built on the certainty that, most days, options decay.

But theta is **not free money**, and this is the honest core of the chapter. The seller's positive theta is paid for by **negative gamma** — the convexity risk above. The landlord collecting daily rent sits on a position that loses money *fast and accelerating* if the market makes a large move. The income is small, steady, and high-probability; the loss is large, sudden, and low-probability. A premium seller is picking up coins in front of a roller: most days you collect, but the day the roller moves you can give back weeks of theta in an hour.

The market is roughly fair about this: the premium you collect (the implied volatility) is the price for that tail risk. Sellers profit *on average* only when realised volatility comes in below the implied volatility they sold — when the market moves *less* than the premium feared. When a budget, an election result, or an RBI surprise makes the market move more than implied, the sellers pay disproportionately. Theta-harvesting is a bet that the world will be calmer than the option prices assumed, financed by accepting a nasty tail.

### Weekly-expiry theta dynamics in India

Indian index options trade on a **weekly expiry** cycle (Nifty and Bank Nifty each have a weekly expiry, alongside monthly contracts), and this short cycle makes theta a front-row, every-week phenomenon. With only days to run, a weekly option lives almost entirely in the steep part of the decay curve.

The pattern premium sellers obsess over:

- **Early in the week**, decay is gentle. The option still has several days of optionality, so time value drains slowly — the flat part of the curve.
- **The last 2–3 days** are where decay accelerates violently for ATM options. This is the cliff. The expiry day itself can see an ATM option shed most of its remaining time value, especially across **non-trading hours** — decay for two calendar days (a weekend, or simply overnight) is credited even though the market was shut. Many sellers deliberately put on short-premium positions for exactly this window, capturing the fastest decay while minimising the nights they hold the dangerous negative-gamma tail.

This creates the well-known expiry-day tension in Indian markets: ATM weeklies are simultaneously the **highest-theta** instruments on the board (great for sellers harvesting decay) and the **highest-gamma** (lethal for those same sellers if spot lunges toward the strike near the close). The "expiry pin," where spot seems magnetised to a heavily-traded strike, is partly the visible footprint of this gamma-theta tug-of-war in the final hours.

![Figure: ATM theta accelerates near expiry](figs/theta_vs_time.png)

The figure shows the value of an at-the-money option as expiry approaches, reading time from left (many days out) to right (expiry). The curve falls gently at first and then plunges in the final days — the characteristic convex "cliff" of ATM time decay. The slope of this curve at any point *is* theta; you can see it steepen dramatically near expiry. An OTM option's curve, by contrast, would start much lower and slide down more steadily, without the same end-of-life collapse, because it had little time value to lose in the first place.

### Estimating daily decay in rupees for a Nifty / Bank Nifty position

A professional always converts theta from an abstract number into rupees of P&L. The recipe:

1. **Read theta per unit** from your option chain or pricing tool (most Indian broker platforms display it). Say a Nifty weekly ATM call shows theta `-9`.
2. **Multiply by the lot size** to get rupees per lot per day. Nifty lot size is currently about 75, so one long lot decays about `9 * 75 = ₹675` per day.
3. **Multiply by the number of lots** and sum across all legs (with sign) to get the **net theta of the position**. A short straddle is the sum of two positive thetas — your daily income; a long straddle is the sum of two negative thetas — your daily cost.
4. **Adjust for the calendar.** Theta is a *per-calendar-day* number, so holding over a weekend or a market holiday racks up two or three days of decay at once even though only one trading session passes. Sellers love this; buyers dread it.

A quick sanity check: net theta tells you what the position makes or loses *if the market does nothing*. If your short strangle shows net theta of `+₹1,400` per day, that is your reward for a flat day — and your job is to judge whether that ₹1,400 adequately compensates the negative-gamma risk you are carrying to earn it.

## Worked example (₹, Nifty / Bank Nifty)

Let us make theta concrete with a short-straddle seller, the archetypal Indian theta harvester.

**Setup.** It is Monday of an expiry week. Nifty spot is **24,000** with the weekly expiry on Thursday (4 calendar days away, counting the expiry day). A trader sells one lot each of the **24,000 ATM call** and the **24,000 ATM put** — a short straddle. The chain shows:

- 24,000 call: premium **₹130**, theta **-9**, gamma small but positive (so the trader's gamma is negative).
- 24,000 put: premium **₹120**, theta **-8**.

Nifty lot size is **75**.

**Step 1 — Premium collected.** Selling both legs brings in `(130 + 120) * 75 = 250 * 75 = ₹18,750` per straddle. This is the maximum the trader can make, and it is collected up front.

**Step 2 — Net theta on day one.** The trader is *short* both options, so their thetas flip to positive income. Net theta per unit is `+9 + 8 = +₹17`. Per lot: `17 * 75 = ₹1,275` per day. If Monday and Tuesday pass with Nifty parked near 24,000, the trader pockets roughly ₹1,275 each day from decay alone — the straddle gets cheaper to buy back.

**Step 3 — The acceleration into expiry.** Because these are ATM options, theta does not stay at ₹17. As Thursday approaches, time value collapses and theta *grows in magnitude.* By Wednesday the combined theta per unit might be ₹25–30, and on expiry-day morning the remaining time value evaporates almost entirely by the close. The trader harvests the steep part of the curve precisely as it steepens; most of the ₹18,750 is captured in the final two sessions.

**Step 4 — The tail the trader is renting against.** Suppose on Wednesday Nifty gaps to **24,400** on surprise news — a 400-point move. The short call is now ₹400 in-the-money on intrinsic value; buying it back might cost ₹430, while the put collapses toward ₹10. The trader must repurchase the straddle for around `(430 + 10) * 75 = ₹33,000` against the ₹18,750 collected — a loss of about **₹14,000** on one lot, wiping out roughly *eleven days* of ₹1,275 daily theta in a single move. This is negative gamma in action: the loss exploded far faster than the steady income accrued. And on a SPAN-margined short straddle, the broker's margin would have ballooned into the move, possibly forcing an exit at the worst moment.

**Step 5 — The lesson.** On quiet days the trader is right and theta pays ₹1,275 a day like clockwork. On the one violent day, negative gamma takes back a fortnight of income at once. The theta was never "free"; it was rent the buyer paid for carrying exactly this tail. Whether the trade is good *on average* depends entirely on whether Nifty's realised moves came in below the roughly ₹250 of combined premium (the implied move) the market charged.

## Common mistakes / risk note

- **Treating theta as guaranteed income.** Positive theta is real, but it is *paid for* with negative gamma. The steady daily credit is the bait; the tail loss is the hook. Never look at your daily theta without also looking at what a 1–2% gap in Nifty (or 2–3% in Bank Nifty) would do to the same position.
- **Assuming decay is linear.** Beginners hold an ATM weekly long option expecting to lose a little each day and are shocked when most of the premium vanishes in the final two sessions. ATM decay is a cliff, not a slope.
- **Forgetting the weekend / holiday decay.** Theta is per calendar day. A long option held Friday to Monday eats two extra days of decay over a closed market. Buyers who hold over long weekends and holidays pay theta for nothing happening; sellers specifically target those gaps.
- **Buying far-OTM "cheap" weeklies for the lottery.** They look cheap because they are nearly all gone — a low-priced far-OTM weekly is a melting near-worthless ticket whose theta will grind it to zero unless a big move arrives fast. Cheap is not the same as good value.
- **Over-leveraging the theta engine.** Because premium selling wins on most days, it lulls traders into adding size — right up to the day a gap takes out months of accumulated income and, with SPAN margins expanding into the move, can threaten the account. Around 9 in 10 retail F&O traders lose money (SEBI studies); over-confident, over-sized theta selling into tail events is one of the classic routes there.

## Key takeaways

- **Theta** is the premium an option loses per **day** from the passage of time: **negative for long options** (the buyer's enemy), **positive for short options** (the seller's friend).
- Time decay acts on **time value**, which shrinks to zero at expiry because the opportunity set runs out.
- **ATM theta accelerates near expiry** (decay behaves like `1 / sqrt(time left)` — a cliff in the final days), while **OTM theta is steadier** and smaller because there is less time value to lose.
- Theta and **gamma** are inseparable and opposite in sign: `theta ≈ -0.5 * gamma * (daily move)^2`. **High gamma always carries high theta — there is no cheap convexity.**
- **Sellers harvest theta as income** but accept the **negative-gamma tail**: small steady gains financed by a large, sudden possible loss. Theta is rent for that tail, not free money.
- In India's **weekly expiry** cycle, the **last 2–3 days** see the fastest ATM decay; premium sellers target this window, including weekend/overnight calendar decay.
- Convert theta to rupees as **theta per unit × lot size × lots**, summed across legs, and judge it against the gamma risk you carry to earn it.

## Practice problems

1. **Sign and intuition.** A trader is long one Nifty 24,000 weekly call. Is their theta positive or negative? In one line, explain what that means for their P&L on a day when Nifty does not move at all.

2. **Rupee decay (numeric).** A Bank Nifty 52,000 ATM weekly put shows a theta of **-22**. Bank Nifty lot size is about **15 units**. If a trader is **long 4 lots** and the market is flat tomorrow, roughly how much do they lose to time decay? What if they were *short* 4 lots instead?

3. **ATM vs OTM decay.** Two traders each buy a Nifty weekly option on Monday: one buys the ATM 24,000 call, the other a far-OTM 24,600 call. Both hold to Thursday with Nifty pinned at 24,000 the whole week. Qualitatively, whose option loses the larger *fraction* of its value, and why does the ATM option's loss arrive mostly at the end?

4. **The gamma link.** A trader says: "I want the huge gamma of an expiry-day ATM option, but I don't want to pay much theta." Explain why this wish is essentially impossible, referencing the relationship between the two Greeks.

5. **Weekend decay (conceptual + numeric).** A long Nifty ATM call has a theta of **-10** per unit. The trader holds it over a Friday-to-Monday period with no market holidays. Roughly how much time-value decay (per unit) should they expect when the market reopens Monday, and why is it more than a single day's worth?

6. **Is the income enough? (judgement).** A short Nifty strangle collects net theta of **₹1,000 per lot per day** three days before expiry. The trader is carrying negative gamma such that a 300-point overnight gap in Nifty would cost about ₹9,000 per lot. In plain English, what question must the trader answer to decide whether this is a sound trade?

## Solutions

1. **Negative theta.** A long option always has negative theta. On a day when Nifty is unchanged, the position still loses money — the call's time value erodes by roughly its theta in rupees (theta × lot size) purely because one day of optionality has been used up. Doing nothing costs the buyer money; that is the buyer's enemy at work.

2. **Long 4 lots:** decay per lot is `22 * 15 = ₹330` per day, so four lots lose about `330 * 4 = ₹1,320` to theta on a flat day. **Short 4 lots:** the sign flips — the trader *earns* about ₹1,320 from time decay on a flat day, because short options have positive theta. Same magnitude, opposite direction: the buyer's loss is the seller's income.

3. **The ATM 24,000 call loses the larger fraction of its value** — in fact, pinned at 24,000 to Thursday, it decays toward roughly its (near-zero) intrinsic value, losing almost all of its substantial time value. The far-OTM 24,600 call started with very little value, and although it too goes to near-zero, the *rupee* loss is small because there was little to lose. The ATM option's loss arrives **mostly at the end** because ATM time decay is non-linear: it follows roughly `sqrt(time left)`, so the steepest erosion — the cliff — is concentrated in the final two or three sessions. Monday and Tuesday bleed gently; Wednesday and Thursday collapse.

4. **Because theta and gamma are bound by the same formula:** `theta ≈ -0.5 * gamma * (daily move)^2`. The huge gamma of an expiry-day ATM option is *defined* alongside, and paid for by, an equally huge negative theta. The market prices convexity and time decay as two ends of one trade: anyone selling you that explosive gamma demands the steep theta in return, and the pricing makes them move together. You cannot have one without the other — there is no cheap convexity. Wanting big gamma but little theta is wanting to buy something for less than its price.

5. **Expect about three days' worth — roughly `10 * 3 = ₹30` per unit** (give or take, since the per-day theta itself rises slightly as expiry nears). Theta is a **per-calendar-day** quantity, and Friday-close to Monday-open spans three calendar days (Friday night, Saturday, Sunday) even though only one trading session is lost. Time value decays on the calendar, not the trading clock, so the option reopens Monday having shed roughly three days of premium. This is exactly why sellers favour holding short premium over weekends and buyers dread it.

6. **The trader must answer: how likely is a move large enough to overwhelm the accumulated theta, and is the daily income fair compensation for that tail?** Concretely: ₹1,000 a day of theta means it takes about nine quiet days to earn what a single 300-point overnight gap (about ₹9,000) would cost — but only three days remain, so a few quiet sessions earn perhaps ₹3,000 while one bad gap erases ₹9,000. The real question is whether the **realised** volatility of Nifty over those final days will come in **below** the **implied** volatility embedded in the strangle's premium. If the market stays calmer than the premium feared, the theta is genuine profit; if a gap arrives, the negative gamma gives back far more than the theta ever paid. Theta income is only sound when it is correctly priced rent for the tail being carried — never assume it is free.
