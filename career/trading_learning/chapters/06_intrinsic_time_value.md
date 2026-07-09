# Chapter 6: Intrinsic Value vs Time Value

Every rupee you pay for an option is actually two rupees wearing one coat. One part is the "real, here-and-now" value — what the option would be worth if expiry were this instant. The other part is a bet on what *might* happen between now and expiry. Pull those two pieces apart and almost everything confusing about options pricing starts to make sense: why a premium can fall even when the index sits still, why at-the-money options are the most expensive to *hold*, and why option buyers always feel like they are running up a downward escalator.

This chapter teaches you to split any premium into **intrinsic value** and **time value** (also called extrinsic value). Once you can do that split in your head for a Nifty option, you will understand what you are really buying — and why the clock is your friend or your enemy.

## Core concepts

### The split: premium = intrinsic value + time value

The market quotes one number — the **premium**, the price of the option. But that single number hides a two-part structure:

`Premium = Intrinsic value + Time value`

- **Intrinsic value** is the part of the premium that is "already in the money" — the cash you would collect if the option were exercised right now. It can never be negative.
- **Time value** is everything left over. It is what you pay for *possibility*: the chance the option moves further into profit before expiry.

Think of buying a half-finished house. The **intrinsic value** is the bricks and concrete already standing — solid, real, here today. The **time value** is the *hope* the neighbourhood will boom and the finished house will be worth far more. As the deadline to finish nears, that hope must either turn into bricks or evaporate. At the final moment, only the bricks count.

### Intrinsic value: the formulas

Let `S` be the current spot level of the underlying (say Nifty) and `K` be the option's strike price.

- For a **call** (right to buy at K): `Intrinsic = max(S - K, 0)`
- For a **put** (right to buy... sorry, right to *sell* at K): `Intrinsic = max(K - S, 0)`

The `max(..., 0)` is the whole trick. An option is a *right, not an obligation*, so you would never exercise it at a loss. If the maths gives a negative number, you simply walk away and intrinsic value is zero.

Quick reads of the three "moneyness" states for a **call** with strike K = 24,000:

- Spot at 24,300 → intrinsic = max(24300 - 24000, 0) = **300 points**. The call is **in-the-money (ITM)**.
- Spot at 24,000 → intrinsic = max(0, 0) = **0**. The call is **at-the-money (ATM)**.
- Spot at 23,700 → intrinsic = max(23700 - 24000, 0) = **0**. The call is **out-of-the-money (OTM)**.

Note that OTM and ATM options have **zero intrinsic value**. Their entire premium is time value. A deep-ITM option, by contrast, is mostly intrinsic value.

(Indian index options like Nifty and Bank Nifty are **European** — exercisable only at expiry — and **cash-settled**. So "exercise right now" is a thought experiment for valuation, not something you can literally do mid-week. The intrinsic-value formula still describes the floor under the price.)

### Time value: simply the leftover

You never look up time value in a quote screen. You compute it:

`Time value = Premium - Intrinsic value`

Example: the Nifty 24,000 call trades at ₹180 while spot is 24,300.

- Intrinsic = max(24300 - 24000, 0) = 300 points.

Wait — the premium (180) is *less* than the intrinsic value (300)? That cannot happen in a fair market for a European option near expiry; it would be an arbitrage. In practice for a liquid ITM index option you would see the premium quoted *above* 300, say ₹330. Then:

- Time value = 330 - 300 = **30 points**.

So a deep-ITM option's premium is dominated by intrinsic value (300 of the 330), with only a thin sliver (30) of time value. Hold that thought — it is the key to how time value behaves.

### Why time value exists at all

Time value is the price of **uncertainty plus time**. Two ingredients feed it:

1. **Time remaining.** The longer until expiry, the more chance the underlying swings in your favour. A 30-day option has more "runway" than a 1-day option, so it carries more time value.
2. **Volatility (uncertainty).** The more the underlying tends to move, the wider the range of possible outcomes, and the more an option's one-sided payoff is worth. In India this expected movement is summarised by **India VIX**. Higher VIX → fatter time value. (Volatility's effect on price is measured by the Greek **vega**, covered in a later chapter.)

The reason an option has *any* value beyond intrinsic is asymmetry: a long option's loss is capped at the premium, but its gain is open-ended (for calls) or large (for puts). You are paying for the right tail while the left tail is bounded. That optionality is worth real money — and time value is its price tag.

### Why time value decays to zero at expiry

At the exact moment of expiry there is no more "time remaining" and no more "uncertainty" — the underlying *is* whatever it is. Possibility has collapsed into fact. So at expiry:

`Time value = 0`, and `Premium = Intrinsic value = max(S - K, 0)` for a call, `max(K - S, 0)` for a put.

This is why the settlement value of a Nifty option is purely its intrinsic value against the expiry-day settlement price. Everything you paid above intrinsic must bleed away as the days, then hours, then minutes tick down. That bleed is called **time decay**, and its Greek measure is **theta** (previewed below).

### How time value behaves across moneyness

Here is the single most useful picture in the chapter: time value is **largest for at-the-money options** and **smallest for deep ITM or deep OTM** options.

- **Deep OTM** (e.g. 24,000 call with spot at 22,500): almost no realistic chance of finishing in the money, so there is little possibility left to pay for. Time value is small, premium is small, intrinsic is zero.
- **At-the-money** (spot ≈ strike): the outcome is a coin-flip. Will it finish a little above or a little below the strike? This maximum uncertainty is exactly what time value prices, so time value peaks here.
- **Deep ITM** (24,000 call with spot at 25,500): the option will almost certainly finish in the money. It now behaves almost like the underlying itself (high delta). There is little *additional* uncertainty about *whether* it pays off, so time value is again small; the premium is nearly all intrinsic.

A handy mental model: time value measures *how much the market is unsure whether this option will expire worth something*. The ATM strike is where the market is most unsure, so that is where time value is fattest.

The figure below shows this split for a single 24,000 call: as spot rises along the horizontal axis, the intrinsic value (the floor) grows as a kicked-in straight line, while the total premium sits *above* it — and the gap between them, the time value, is widest near the strike and tapers off on both sides.

![Figure: a 24000 call's value split into intrinsic and time value](figs/time_value.png)

### How time value behaves as expiry approaches

Time value does not melt at a constant rate. It decays **slowly at first and then accelerates**, collapsing fastest in the final days for an ATM option. A 30-day ATM option might lose only a point or two of time value per day early on, but in expiry week it can shed a large chunk daily, and on expiry day itself the remaining time value rushes to zero.

This non-linear, accelerating decay is why Indian **weekly options** (Nifty and Bank Nifty expiries land on fixed weekdays as set by the exchange) are so brutal for buyers and so attractive to sellers: a weekly option is *all* in the steep part of the decay curve. The detailed shape is the subject of the next chapters on **time decay** and **theta**.

### The link to extrinsic value and theta

"Time value" and **extrinsic value** are two names for the same thing: everything in the premium that is *not* intrinsic. Some books say extrinsic to remind you it depends on *external* factors (time left, volatility, interest rates) rather than the simple spot-minus-strike arithmetic.

**Theta** is the Greek that measures how much time value (and therefore premium) the option loses per day, holding everything else constant. Theta is typically quoted as a negative number for a long option — e.g. theta = -8 means the option loses about ₹8 of value per day from the passage of time alone. We preview it here only to make one point unmistakable.

### Why option BUYERS fight a constant headwind

When you **buy** an option, you pay the full premium — intrinsic *plus* time value. The intrinsic part you can recover (it tracks the spot). But the **time value you paid is guaranteed to reach zero by expiry.** Every single day that the underlying does *nothing*, your option is worth a little less. That is the headwind.

Picture the option buyer walking up a downward-moving escalator. To make money you do not merely need to be right about direction — you need to be right *enough, fast enough* to outrun the time decay pulling you down. Stand still (the index goes nowhere) and the escalator carries you backward into a loss.

The mirror image: the option **seller** collects that time value upfront and pockets it as the option decays — they are riding the escalator *down*, in their favour. This is the deep reason behind a sober statistic: most long options expire worthless, and SEBI studies have found roughly **9 in 10 retail F&O traders lose money**. The time-value headwind is a structural cost of being long options, not bad luck. It does not make buying options wrong — it makes *overpaying for time value, or holding too long, or trading direction without enough movement* wrong.

## Worked example (₹, Nifty/Bank Nifty)

Let's do a full split with realistic numbers. Suppose it is mid-week and **Nifty spot = 24,150**. We look at three call options expiring this Friday, plus one put, and pull each premium apart.

| Option | Strike K | Premium (₹) | Intrinsic = max(S-K,0) | Time value = Premium - Intrinsic |
|---|---|---|---|---|
| 24,000 CE (ITM call) | 24,000 | 215 | max(24150-24000,0) = 150 | 215 - 150 = **65** |
| 24,150 CE (ATM call) | 24,150 | 95 | max(24150-24150,0) = 0 | 95 - 0 = **95** |
| 24,400 CE (OTM call) | 24,400 | 22 | max(24150-24400,0) = 0 | 22 - 0 = **22** |
| 24,000 PE (OTM put) | 24,000 | 50 | max(24000-24150,0) = 0 | 50 - 0 = **50** |

Read what this table is telling you:

- The **ITM call** (24,000 CE) holds 150 points of solid intrinsic value and only 65 of time value. Most of what you pay is "bricks."
- The **ATM call** (24,150 CE) has *zero* intrinsic value — its entire ₹95 premium is time value. This is the strike with the most time value, exactly as the moneyness rule predicts.
- The **OTM call** (24,400 CE) is cheap (₹22) and 100% time value, but it is small time value because finishing above 24,400 by Friday is a long shot.
- The **OTM put** is also pure time value (₹50) — a bet that Nifty falls below 24,000.

**Now apply the time-value headwind.** Suppose by the next morning Nifty is still 24,150 — it has not moved at all — and one day of time value has bled out. Roughly, the ATM 24,150 CE might fall from ₹95 to about ₹83. You were "right" that the market did not crash, yet you lost about ₹12 per unit purely to decay. With a Nifty lot size of about 75 units (lot sizes are set by the exchange and change periodically), that ATM call holder lost roughly:

`12 points * 75 = ₹900` on one lot, in a single quiet day — with the index unchanged.

The seller of that same call collected that ₹900. That is the buyer's headwind and the seller's tailwind, in rupees.

**A second pass — what the buyer needs to break even.** The ATM buyer paid ₹95, all of it time value. To merely break even at expiry, Nifty must finish at `24,150 + 95 = 24,245`. So even a 95-point rally (about 0.4%) by Friday leaves the buyer flat, because that entire move just *replaces* the time value they paid. Anything less and the position loses. This is the precise sense in which the buyer "pays for the option to be wrong, but still has to be right to win."

## Common mistakes / risk note

- **Thinking a flat market is a safe market for option buyers.** It is the opposite. If the index goes nowhere, your long option still loses time value every day. "No move" is a losing scenario for buyers.
- **Assuming premium tracks intrinsic value one-for-one.** A 50-point favourable move in Nifty does *not* add 50 points to an OTM option's premium, and it can even be *swamped* by time-value decay or a drop in India VIX. Premium = intrinsic + time value, and both parts move.
- **Buying cheap deep-OTM options because they "cost so little."** They are cheap precisely because they are almost all unlikely time value. They usually expire worthless. Cheap is not the same as good value.
- **Ignoring volatility's effect.** Time value depends on India VIX. You can buy an option, be right on direction, and still lose if VIX falls and crushes the time-value portion (a "vol crush," common right after an event).
- **Holding longs into expiry week out of hope.** That is the steepest part of the decay curve. Time value you are counting on to recover is evaporating fastest exactly then.
- **The honest risk on the other side.** Selling options to collect time value is *not* free money. The decay tailwind is real, but the seller's loss is large and, for a naked option, effectively undefined. SEBI's data showing about 9 in 10 retail F&O traders lose money applies to *both* careless buyers and over-leveraged sellers. Understanding intrinsic vs time value tells you *where* your edge has to come from; it does not hand you an edge.

## Key takeaways

- Every premium splits in two: `Premium = Intrinsic value + Time value`.
- Intrinsic value is `max(S - K, 0)` for a call and `max(K - S, 0)` for a put — never negative, and zero for ATM/OTM options.
- Time value = Premium - Intrinsic. It is the price of uncertainty plus time, and it is also called extrinsic value.
- Time value is **largest at-the-money** and **smallest deep ITM or deep OTM**; it always decays to **zero at expiry**, and it decays *faster* as expiry nears.
- Theta measures the daily loss of time value — the structural headwind that makes long options lose value when the market stands still.
- Buyers pay for time value and watch it bleed; sellers collect it. This is a core reason most long options expire worthless and most retail F&O traders lose money — trade accordingly.

## Practice problems

1. **(Conceptual)** A Nifty 23,800 PE (put) has a premium of ₹140 with spot at 23,900. Is this option ITM, ATM, or OTM? What is its intrinsic value and its time value?

2. **(Numeric)** Bank Nifty spot is 52,400. The 52,000 CE trades at ₹560. Split the premium into intrinsic value and time value.

3. **(Numeric)** For Nifty spot = 24,100, you observe three calls: 23,800 CE at ₹360, 24,100 CE at ₹110, and 24,500 CE at ₹28. Compute the time value of each and identify which strike has the most time value. Does this match the moneyness rule?

4. **(Conceptual)** Two days pass and Nifty is unchanged at 24,100. Which of the three calls in Problem 3 will, in percentage terms, be hurt most by time decay, and why?

5. **(Numeric)** You buy one lot of the Nifty 24,100 ATM call from Problem 3 at ₹110 (lot size 75). For you to break even at expiry, where must Nifty settle? What is your maximum possible loss in rupees?

6. **(Conceptual)** A trader says, "I'll buy a deep-ITM call instead of the stock — it's like owning the index but cheaper." Using the intrinsic/time-value split, explain what is true and what is misleading about this.

## Solutions

**1.** Spot 23,900 is *above* the strike 23,800, so the right to *sell* at 23,800 is worthless to exercise now → the put is **OTM**. Intrinsic = max(K - S, 0) = max(23800 - 23900, 0) = **0**. Time value = Premium - Intrinsic = 140 - 0 = **₹140**. The entire premium is time value — typical for an OTM option.

**2.** Bank Nifty 52,000 CE with spot 52,400. Intrinsic = max(S - K, 0) = max(52400 - 52000, 0) = **400 points**. Time value = 560 - 400 = **160 points**. So this ITM call's premium is mostly intrinsic (400) with 160 of time value.

**3.** All are calls, intrinsic = max(S - K, 0):
- 23,800 CE: intrinsic = max(24100 - 23800, 0) = 300. Time value = 360 - 300 = **60**.
- 24,100 CE: intrinsic = max(24100 - 24100, 0) = 0. Time value = 110 - 0 = **110**.
- 24,500 CE: intrinsic = max(24100 - 24500, 0) = 0. Time value = 28 - 0 = **28**.

The **24,100 CE (ATM)** has the most time value (110), versus 60 for the ITM and 28 for the OTM. Yes — this matches the rule that time value peaks at-the-money and is smaller deep ITM or far OTM.

**4.** In *percentage* terms, the **24,500 OTM call** is hurt most. Its entire ₹28 premium is fragile time value, and OTM time value decays toward zero quickly when the underlying does not move toward the strike — a few points lost off ₹28 is a large percentage. The ITM 23,800 call, by contrast, holds 300 points of intrinsic value that does *not* decay; only its 60 points of time value erode, so the percentage hit to its ₹360 premium is much smaller. (The ATM call loses the most in *absolute* points, but the OTM loses the most in percentage terms.)

**5.** You paid ₹110, all time value (intrinsic is zero at the 24,100 strike with spot 24,100). Break-even at expiry: Nifty must finish at `K + premium = 24,100 + 110 = 24,210`. Maximum loss is the full premium paid, since a long call cannot lose more than what you spent: `110 points * 75 = ₹8,250` per lot. That maximum loss occurs if Nifty settles at or below 24,100 at expiry, where the call expires worthless.

**6.** *What's true:* a deep-ITM call has high intrinsic value and a high delta, so it moves nearly point-for-point with the index, and it ties up less cash than buying the index basket outright — so it does feel like "owning the index, cheaper." *What's misleading:* even a deep-ITM call still contains some time value, and **that time value decays to zero by expiry** — the actual underlying never decays. So the ITM-call holder still pays a (small) time-value headwind and faces expiry, whereas a holder of the underlying does not. The call is a *leveraged, time-limited* proxy for the index, not a free substitute. The leverage cuts both ways, and the time-value sliver is a recurring cost the stock holder never pays.
