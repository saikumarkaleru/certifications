# Chapter 44: Calendars & Diagonals — Trading Time & Term Structure

Every strategy you have met so far trades the *same expiry* on both legs. A bull call spread buys one strike and sells another, but both options die on the same Thursday. The calendar spread breaks that rule. For the first time, the two legs live on **different expiry dates** — you sell a near-term option and buy a longer-term option, usually at the **same strike**. That single change turns the trade into something genuinely new: a position whose main fuel is not direction and not even raw volatility, but **time itself** and the **shape of the volatility term structure** you met in Chapter 34.

The intuition is beautiful once it clicks. Time decay (theta) is not constant across expiries — it is brutal and accelerating for the option that expires this week, and gentle and slow for the option that expires next month. So if you sell the fast-decaying near option and own the slow-decaying far option, you collect more decay than you pay, day after day, *as long as the underlying behaves*. India's weekly-versus-monthly expiry structure makes this unusually natural to put on. This chapter shows how calendars work, the "tent"-shaped payoff they produce, why they are secretly **long volatility**, and when the edge is real versus illusory.

## Core concepts

### The trade in one sentence

A **calendar spread** (also called a *time spread* or *horizontal spread*) is built from two options of the **same type** (both calls or both puts) and the **same strike**, but **different expiries**:

- **Sell** the **near-term** option (expires soon — this week's or this month's).
- **Buy** the **far-term** option (expires later — next month or a later series).

Because the longer-dated option always costs more than the shorter-dated one (more time value), you pay a **net debit** to enter. That debit is your maximum loss. The position is therefore *defined-risk* — a big comfort compared with naked selling.

The names tell you the geometry. A **vertical** spread moves up the strike column (same expiry, different strikes). A **horizontal** or **calendar** spread moves sideways across the expiry calendar (same strike, different dates). A **diagonal** does both — different strike *and* different expiry.

### Why selling near and buying far makes money: the theta engine

Recall two facts from the Greeks chapters. First, **theta** (time decay) is the rate at which an option loses value as expiry approaches, all else equal. Second, theta is *not linear in time* — it accelerates as expiry nears, roughly in proportion to `1 / sqrt(time remaining)` for an at-the-money option. A weekly option with three days left bleeds value far faster *per day* than a monthly option with thirty days left.

That asymmetry is the whole engine. Picture two at-the-money options on Nifty at 24000: the near one has 7 days to expiry and decays fast; the far one has 35 days and decays slowly. You are **short** the fast bleeder and **long** the slow bleeder. The near option you sold loses value quickly (good for you, the seller); the far option you own loses value too, but much more slowly. The difference is your daily harvest. That is why a calendar carries **positive net theta** — time is on your side, exactly the opposite of an outright long option.

### The other engine: long vega and the term structure

Here is the part that surprises beginners. A calendar is **net long vega** — it *gains* if implied volatility (IV) rises and *loses* if IV falls. Why? Vega scales with time to expiry: the longer-dated option you own has far more vega than the shorter-dated option you sold. So a rise in IV lifts the value of your long far leg more than it lifts the cost of your short near leg. Net, you are long volatility.

This is the single most important thing to internalise: **a calendar is positive theta AND positive vega at the same time.** That combination is rare and valuable. Most positive-theta trades (short straddles, iron condors) are *short* vega — they get hurt when fear spikes. The calendar collects decay while *also* benefiting from a volatility increase. The price you pay for that lovely combination is **directional fragility**: the position only works if the underlying stays reasonably close to the strike.

Because the long leg lives in a *different expiry* from the short leg, the calendar's profit depends on the **volatility term structure** — the relationship between near-expiry IV and far-expiry IV. You are, in effect, **selling near-term IV and buying far-term IV**. The ideal entry is when near-term IV is *rich* (elevated) relative to longer-term IV — for example, into a scheduled event when the front of the curve bulges upward. After the event, the front-month IV collapses (the "IV crush") while the back month barely moves, and the term structure relationship swings in your favour.

### The "tent"-shaped payoff — described in words

Calendar payoffs confuse people because you cannot draw the usual hockey-stick. The two legs expire on *different days*, so there is no single moment where both payoffs are "at expiry" together. The chart that matters is the **P&L at the near expiry** — the Thursday the short option dies — because that is the day you must act.

On that day, the short near option is worth its intrinsic value (or zero), while the long far option still has weeks of life and therefore still carries time value. Plotting the net position's value against the underlying price on that day produces a shape like a **tent** or a single rounded hill:

- The tent **peaks right at the strike**. If Nifty finishes the near expiry sitting exactly at your strike, the short option you sold expires worthless (maximum gain to you as seller), while the long option still holds its juicy remaining time value. This is the best case — maximum profit.
- The tent **slopes down on both sides**. As the underlying drifts away from the strike in either direction, your edge shrinks. Far enough away, the short option goes deep in- or out-of-the-money and the time-value advantage evaporates.
- The **two lower edges of the tent are your breakevens** — one below the strike, one above. Outside that band you lose money; inside it you profit.
- The **floor is the net debit you paid** — the most you can lose, reached only on an extreme move where both options behave almost identically and the spread collapses to near zero.

So the calendar is a bet that the underlying will **sit near the strike** through the near expiry. It is the mirror image of a long straddle: a straddle is a valley that profits from movement; a calendar is a hill that profits from *stillness near a point* — while staying long vega so a fear spike does not wreck it.

Here is a compact numeric sketch of that tent for a 24000 Nifty call calendar, showing the net position value on the near-expiry day across a range of closing prices (illustrative figures):

| Nifty at near expiry | Short near 24000 call (you owe) | Long far 24000 call (you own) | Net position value | P&L vs ~60 debit |
|---|---|---|---|---|
| 23400 | ~0 | ~25 | ~25 | -35 |
| 23700 | ~0 | ~55 | ~55 | -5 |
| 24000 (strike) | ~0 | ~95 | ~95 | +35 (peak) |
| 24300 | ~300 | ~330 | ~30 | -30 |
| 24600 | ~600 | ~615 | ~15 | -45 |

Read down the "Net position value" column and you can *see* the tent: it climbs to a peak at the 24000 strike and falls away on both sides. The far leg's residual time value is what holds the structure up near the strike; a large move in either direction flattens it.

### The diagonal spread — a directional, cheaper cousin

A **diagonal spread** keeps the "sell near, buy far" calendar skeleton but **shifts the two strikes apart**. You might sell a near-term 24200 call and buy a far-term 24000 call. Now the trade carries two new properties:

1. **A directional tilt.** Because the strikes differ, the position has a non-trivial net delta. A *call diagonal* with the long leg at a lower strike than the short leg leans bullish; arrange the strikes the other way and it leans bearish. You are effectively combining a calendar (time edge) with a vertical spread (directional edge).
2. **Lower cost or even a credit.** Selling a closer-to-the-money near option brings in more premium, shrinking the net debit. With aggressive strike selection a diagonal can be entered for a very small debit, and the long far leg can later be financed by *rolling* — selling a fresh near option against it each week. This "sell weeklies against a monthly long" pattern is the engine behind the **Poor Man's Covered Call**, a capital-light substitute for owning the underlying.

The trade-off: a diagonal's tent is **skewed** toward the direction you leaned, so you can be right that "it'll sit still" yet still lose if it sits still in the *wrong place*. Diagonals reward a more demanding forecast — "it drifts gently toward 24200 and parks there" — than the pure calendar's "it stays near 24000."

### The India angle: weeklies vs monthlies make calendars natural

Indian index options hand you a ready-made calendar toolkit. Nifty has **weekly expiries** (currently Thursdays) stacked in front of the **monthly expiry** (last Thursday of the month), and longer monthly series beyond that. That dense expiry ladder means you almost always have a fast-decaying near leg and a slow-decaying far leg available at the *same strike* — the exact ingredients a calendar needs.

A few India-specific points:

- **Event calendars are crowded and scheduled.** The Union Budget (1 February), RBI policy days, monthly F&O expiry, US Fed decisions, and election results all bulge the near-week IV — precisely the term-structure condition calendars want.
- **Index options are European and cash-settled.** No early assignment risk on the short Nifty leg. (On single-stock F&O, which is physically settled, an in-the-money short leg near expiry can drag you into delivery obligations — another reason to keep index calendars as your default.)
- **Margins.** Because a calendar is defined-risk with a long option in a *later* expiry hedging the short, SPAN+exposure margin under the SEBI framework is far lighter than naked selling.
- **Costs bite.** STT, exchange charges, GST, and the bid-ask spread are paid on *both* legs, and again when you roll. On a trade whose edge might be only ₹30-40 of net theta, taxes and slippage are a material part of the P&L. Trade liquid at-the-money strikes only.

### Managing the trade at near expiry

The defining decision comes on the **near expiry day**. You have three choices:

1. **Close the whole thing.** Buy back the near-worthless short option and sell the long option, capturing whatever the tent is worth. Simplest, especially if your thesis has played out or the underlying has wandered.
2. **Roll the short leg.** Let the near option expire (or buy it back cheap) and **sell the next week's option** at the same strike against your still-living long leg. This restarts the theta engine and reduces your cost basis — how the structure becomes an *income* position. Re-examine the strike each roll: if the underlying has drifted, roll to a strike nearer the new price to keep the tent centred.
3. **Convert.** If your view has turned strongly directional, drop the short leg and keep the long far option as an outright bet — though you give up the theta protection.

The discipline is to decide your management rule *before* you enter, with a hard stop on the downside: if the underlying makes a large move away from the strike well before the near expiry, the tent has collapsed and rolling will not save you — take the defined loss.

## Worked example (₹, Nifty)

Suppose it is mid-month and Nifty spot sits at **24000**. There is an RBI policy decision next week, so the **near weekly IV is elevated** relative to the next monthly — the term structure has a front-end bump. You believe Nifty will chop around 24000 into and just after the event, and you want to be long vega in case fear spikes, while still collecting decay. A **call calendar at the 24000 strike** is the textbook trade.

You execute (illustrative premiums; Nifty lot size assumed 75):

- **Sell** the near weekly 24000 call (7 days to expiry) at **₹110**.
- **Buy** the monthly 24000 call (35 days to expiry) at **₹170**.
- **Net debit = 170 - 110 = ₹60 per share.**
- Per lot: `60 * 75 = ₹4,500`. This ₹4,500 is your **maximum loss**.

**The Greeks at entry** (approximate, per share):

- **Net delta:** near and far 24000 calls each have delta near +0.50, so the short and long roughly cancel — the position is close to **delta-neutral**. Good: you are not making a strong directional bet.
- **Net theta: positive.** The near call you sold might decay at ~₹9/day while the far call you own decays at only ~₹4/day, for a **net gain of ~₹5/day** as long as Nifty hovers near 24000. That is the harvest.
- **Net vega: positive.** The far call's vega (~₹32 per 1 IV point) exceeds the near call's vega (~₹18), so you are **net long ~₹14 of vega per 1 IV point**. If IV rises 2 points into the event, the position gains roughly `14 * 2 = ₹28` per share from vega alone — about ₹2,100 per lot.

**The good case.** Nifty meanders and finishes the near weekly expiry around **24000**. The short weekly 24000 call expires **worthless** — you keep the ₹110. The long monthly 24000 call still has ~28 days left and, with spot at the strike, might be worth **₹95**. Net position value `95 - 0 = ₹95` against the ₹60 paid: a profit of **₹35 per share = ₹2,625 per lot**, a ~58% return on the debit. If the event also crushed the front-month IV after the decision while the monthly held its IV, the long leg keeps more value and the gain is larger still — the term-structure edge at work.

**The bad case.** Nifty gaps to **24600** on a hawkish surprise. The short 24000 call is ₹600 in-the-money; the long monthly 24000 call is worth perhaps ₹615. Net value `615 - 600 = ₹15`, versus ₹60 paid — a loss of **₹45 per share = ₹3,375 per lot**. Far from the strike both options behave almost like the underlying and converge. A large move in *either* direction does this — but the loss is capped at the ₹60 debit, the defined-risk comfort.

**The management decision.** On the near expiry, if Nifty is near 24000 and your view holds, you **roll**: buy back the expiring weekly cheap and **sell the next weekly 24000 call** for, say, ₹95, restarting the theta clock and cutting your cost basis. If instead Nifty has run to 24600, you close for the defined loss rather than hope.

## Common mistakes / risk note

- **Treating a calendar as "free money."** It is positive theta, yes — but **a large directional move in either direction destroys it.** The tent is narrow; traders who sell calendars mechanically without a stop get wiped out by the occasional gap.
- **Forgetting it is long vega — and that vega cuts both ways.** Entering when front-month IV is already *cheap* relative to the back month means buying expensive far IV and selling cheap near IV, with the term structure against you. **Enter when near IV is rich vs far IV, not the reverse.**
- **Ignoring IV-crush timing.** The event calendar assumes the front-month IV collapses after the event while the back month holds. Sometimes the *whole curve* drops, and your long far leg loses IV too — term structure can move against you even when direction is fine.
- **Wrong-footed by physical settlement on stocks.** A deep in-the-money short near leg on single-stock options can be assigned into share delivery and a margin spike. Prefer European, cash-settled **index** calendars.
- **Underestimating costs and strike drift.** Two legs in, two out, plus weekly rolls — taxes and spread can eat a third of a ₹35-edge trade. And the tent only profits *near the strike*: if price has drifted, re-centre the strike when you roll rather than keeping an off-centre tent past its peak.

Honest framing: calendars are elegant and they genuinely let a retail trader harvest a real structural edge (differential theta plus a long-vega kicker). But they are not low-risk. They demand a correct view that the underlying will *sit still near a point*, and they punish large moves and adverse term-structure shifts. Like all F&O, most retail participants lose money; defined risk caps the damage per trade but does not make the strategy a sure thing.

## Key takeaways

- A **calendar spread** sells a near-term option and buys a longer-term option at the **same strike** for a **net debit** (your max loss), harvesting the **faster decay of the near leg**.
- Its P&L at the near expiry is a **tent**: it **peaks at the strike** and slopes down to breakevens on both sides — a bet that the underlying **sits still near the strike**.
- Net Greeks are **positive theta** (time works for you) and **positive vega** (you gain if IV rises) — a rare and valuable combination; the cost is **directional fragility**.
- The trade is really a play on the **volatility term structure**: sell rich near-term IV, own cheaper far-term IV — ideal **into a scheduled event** that bulges front-month IV.
- A **diagonal spread** uses different strikes *and* expiries to add a **directional tilt** and lower cost; the "sell weeklies against a monthly long" version is the Poor Man's Covered Call.
- India's **weekly-vs-monthly expiry ladder** and **European cash-settled index options** make calendars natural and assignment-safe; manage them at the near expiry by **closing or rolling**, and re-centre the strike if price has drifted.
- The big risks: a **large move in either direction** collapses the tent, and an **adverse term-structure / IV move** can lose money even when direction is fine. Costs on multiple legs matter.

## Practice problems

1. **(Conceptual)** Explain in one or two sentences why a calendar spread is *positive theta* even though you own (are long) one of the two options. Which leg's decay dominates, and why?

2. **(Conceptual)** A trader says, "Calendars are short volatility, like a short straddle, because they profit when the market is quiet." Identify the error and state the calendar's true vega sign, with the reason.

3. **(Numeric)** You set up a Bank Nifty put calendar at strike 52000: sell the weekly 52000 put at ₹240, buy the monthly 52000 put at ₹360. (a) What is the net debit per share and your maximum loss? (b) If, at the near expiry, Bank Nifty closes exactly at 52000 and the monthly put is then worth ₹300, what is your profit per share?

4. **(Numeric / reasoning)** Same Bank Nifty 52000 put calendar (₹120 debit). At the near expiry Bank Nifty has crashed to 50000. The short weekly 52000 put is now worth its intrinsic ₹2000; the long monthly 52000 put is worth ₹2030. What is the net position value and the P&L? What does this illustrate about the tent's edges?

5. **(Application)** It is two days before the RBI policy decision. The Nifty weekly IV is 18% and the monthly IV is 13%. Is this a favourable or unfavourable term-structure setup for entering a Nifty calendar at the at-the-money strike? Explain what you expect to happen to each leg's IV after the announcement and why that helps or hurts.

6. **(Application)** Describe how you would convert a plain Nifty 24000 call calendar into a *bullish diagonal*, and state two consequences (one on cost, one on the payoff shape) of doing so.

## Solutions

1. The near (short) option decays much faster than the far (long) option because theta accelerates as expiry approaches — roughly with `1 / sqrt(time remaining)`. You collect the near leg's large daily decay and pay only the far leg's small daily decay, so the **net of the two is a daily gain**: positive theta. The short near leg's decay dominates because it has far less time left.

2. The error is the assumption that "profits when quiet" implies "short volatility." A calendar is **net long vega (positive vega)**: the far option you own has more vega than the near option you sold (vega scales with time to expiry), so a rise in IV helps the long leg more than it hurts the short leg. The calendar profits from *stillness in the underlying* while *also* benefiting from *rising IV* — unlike a short straddle, which is short vega and loses when IV spikes. "Quiet underlying" and "long volatility" are not contradictory here.

3. (a) Net debit = `360 - 240 = ₹120` per share. That ₹120 (times the Bank Nifty lot size) is the **maximum loss**. (b) At the near expiry with Bank Nifty at 52000, the short weekly 52000 put expires **worthless** (you keep the ₹240). The long monthly put is worth ₹300. Net position value = `300 - 0 = ₹300`. Profit = `300 - 120 = ₹180` per share — the peak of the tent at the strike.

4. Net position value = `2030 - 2000 = ₹30`. P&L = `30 - 120 = -₹90` per share, a loss. This illustrates the **edges of the tent**: far from the strike, both the short and long options are deep in-the-money and their values nearly converge (here only ₹30 apart), so the spread collapses toward zero and you lose most of the debit. A big move in *either* direction does this — the calendar wants the underlying to *stay near the strike*. (The loss is still capped at the ₹120 debit.)

5. This is a **favourable** setup. Near-term (weekly) IV at 18% is **rich relative to** the monthly at 13% — exactly the front-end bump a calendar wants, because you are *selling* the expensive near IV and *buying* the cheaper far IV. After the announcement, the event uncertainty resolves and the **weekly IV typically collapses (IV crush)** — say back toward 12-13% — which **helps your short near leg** (it loses value fast, good for the seller). The **monthly IV** is anchored to longer-run conditions and usually falls far less, so your long far leg holds most of its value. The term-structure relationship swings in your favour, adding to the theta harvest — provided Nifty also stays near the strike.

6. To make it a **bullish diagonal**, keep selling the near-term option but **buy the far-term call at a lower strike** than the short call — for example, *sell* the near weekly 24100 call and *buy* the monthly 24000 call. (Equivalently, sell a higher-strike near call against a lower-strike far call.) Two consequences: **(i) Cost** — because the short near option is now closer to (or further into) the money it brings in more premium, **reducing the net debit** (sometimes substantially). **(ii) Payoff shape** — the position gains a **net positive delta** (bullish tilt) and its tent is **skewed to the upside**: maximum profit now occurs above the original strike, so you need the underlying to drift *up* toward the short strike rather than simply sit still at 24000.
