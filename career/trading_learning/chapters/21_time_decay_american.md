# Chapter 21: Time Decay & American vs European

An option is a melting ice cube. From the day it is born to the moment it expires, it is shedding value — not because the market moved against you, but simply because there is less time left for anything to happen. The clock never pauses, never reverses, and on the final day it runs out completely. This is **time decay**, and it is the single most important force acting on every option price even when the index sits perfectly still.

This chapter does two things. First, it shows you the *shape* of decay — why it is slow and gentle far from expiry but turns into a cliff in the last few days, and why that cliff is steepest for at-the-money options while out-of-the-money options just quietly bleed to nothing. Second, it sorts out a question that confuses almost every beginner: the difference between **American** and **European** exercise, when early exercise actually pays, and why for Indian index traders the whole debate barely matters because you almost never exercise at all — you sell the option back.

## Core concepts

### Time decay: the price of a shrinking window

Recall from Chapter 6 that every premium splits into two parts:

`Premium = Intrinsic value + Time value`

Intrinsic value (`max(S - K, 0)` for a call, `max(K - S, 0)` for a put) is rock-solid — it just tracks where spot is versus the strike, and it does not decay. **Time value** is the perishable part. It is what you pay for *possibility*: the chance the option drifts further into profit before expiry. As the window shrinks, there is less room for that possibility to play out, so time value shrinks too. At the exact instant of expiry there is no window left at all, so:

`Time value at expiry = 0`, and `Premium at expiry = Intrinsic value`.

**Time decay** is the day-by-day loss of that time value, holding everything else (spot, volatility, interest rates) constant. Its Greek measure is **theta**, usually quoted as a negative number for a long option: theta = -8 means the option loses about ₹8 of value per day from the passage of time alone. We will study theta formally in the next chapter; here we focus on the *intuition and shape* of decay, which is what actually changes how you trade.

### Decay is not a straight line — it accelerates

The crucial fact is that time value does **not** melt at a constant rate. It decays slowly when expiry is far away and then accelerates, collapsing fastest in the final days.

The clean way to see why: time value scales roughly with `sqrt(T)`, where `T` is the time left to expiry. The square root is the key. Going from 30 days to 29 days barely changes `sqrt(T)`, so almost no value is lost. But going from 2 days to 1 day, then 1 day to 0, slashes `sqrt(T)` dramatically — so the value gushes out at the end.

A simple way to feel it: an option with four times as long to run is worth only about *twice* as much time value (because `sqrt(4) = 2`), not four times as much. Time is a depreciating asset whose rate of depreciation speeds up as it nears zero.

- **Far from expiry** (a monthly option with 25+ days left): an ATM option might shed only a point or two of time value per day — barely noticeable against normal price swings.
- **Expiry week**: decay becomes the dominant force; an ATM weekly option can lose a large chunk of its value every single day.
- **Expiry day**: whatever time value remains rushes to zero by the close.

This accelerating shape is exactly why Indian **weekly options** (Nifty and Bank Nifty have weekly expiries on fixed weekdays set by the exchange) are so punishing for buyers and so attractive to sellers: a weekly option lives entirely inside the steep part of the decay curve.

### The value curve: well before expiry vs on expiry day

Picture a long call's value plotted against the spot price. There are really two curves to hold in your head:

- **Well before expiry**, the value is a *smooth, gently rising curve* that sits comfortably *above* the intrinsic-value line everywhere. That cushion above intrinsic is the time value. The curve is rounded near the strike — the market is paying for both "it might go up more" and "it might come back."
- **On expiry day**, that smooth curve has collapsed down onto the hard "hockey-stick" of pure intrinsic value: flat at zero below the strike, then a straight 45-degree line above it. The cushion is gone.

So across the life of the option, the smooth rounded curve sags downward, day after day, until it lands exactly on the kinked intrinsic-value line at expiry. The figure below shows this descent for a single call — each lower curve is a day closer to expiry, with the lowest, kinked line being the expiry-day payoff.

![Figure: a call's value as expiry approaches](figs/time_decay.png)

### Why ATM decay accelerates but OTM just bleeds steadily

Not all options decay the same way, and this is one of the most useful distinctions a trader can internalise.

- **At-the-money (ATM) options** carry the *most* time value of any strike (Chapter 6), and that value is what accelerates into the expiry-day cliff. Why the acceleration? Right up until the final hours, an ATM option is a live coin-flip — it could finish a little above or a little below the strike. That genuine uncertainty keeps its time value propped up... until the last day, when the coin must finally land. With no time left for the flip to resolve in your favour, the propped-up value falls off a cliff. ATM theta is small far out and *enormous* on expiry day.
- **Out-of-the-money (OTM) options** behave differently: they **bleed steadily to zero**. A deep-OTM call already has a low, fragile time value (it is unlikely to finish in the money), so there is less to lose and it leaks away in a smooth, grinding fashion rather than a final-day cliff. By the time expiry arrives, an OTM option that never came near its strike has quietly drained to almost nothing well before the close.
- **Deep in-the-money (ITM) options** have little time value to begin with (their premium is mostly intrinsic), so they too decay only modestly — most of their price is the non-decaying intrinsic part.

A clean mental summary: **ATM = cliff at the end; OTM = steady bleed throughout; deep ITM = barely decays.** The reason is the same one from Chapter 6 — time value is largest where the market is most unsure (at the money), and the expiry cliff is just that uncertainty finally being forced to resolve.

### American vs European: two kinds of exercise rights

Now switch topics from *when value decays* to *when you are allowed to use the option*. This is the American-versus-European distinction, and despite the names it has nothing to do with geography.

- **European option**: can be exercised **only at expiry**, never before. You hold the right, but you can cash it in at exactly one moment.
- **American option**: can be exercised **any time** up to and including expiry. You hold the same right plus the *flexibility* to use it early.

An American option therefore can never be worth *less* than the otherwise-identical European option — it includes everything the European has, plus an extra freedom. The interesting question is whether that extra freedom is ever worth anything. Mostly, it is not.

Two terms to keep straight: **exercising** means invoking your right — buying the stock at the strike (call) or selling it at the strike (put). **Selling/squaring off** means handing the option contract to another buyer for its premium. These are different actions with very different payoffs, and confusing them costs beginners money.

### Why you almost never exercise early

Here is the principle that resolves 95% of the confusion: **exercising an option early throws away its remaining time value.** When you exercise, you collect only the intrinsic value (`S - K` or `K - S`). But if you *sell* the option in the market instead, you collect intrinsic value *plus* the leftover time value. As long as any time value remains and the option is liquid, selling beats exercising.

`Sell the option → you get Intrinsic + Time value`
`Exercise the option → you get Intrinsic only (you forfeit the time value)`

So for the vast majority of situations, early exercise is simply *leaving money on the table*. The standard result, which you can take as a rule of thumb: **it is never optimal to exercise an American call early on a non-dividend-paying stock.** You would always do better to sell it. This is why American and European calls on such stocks have essentially the same value — the early-exercise right is worthless.

### The two genuine exceptions

Early exercise *can* be optimal in exactly two narrow cases. Both are worth knowing precisely so you recognise how rare they are.

1. **Deep in-the-money American puts.** A put's maximum possible value is capped — the stock can only fall to zero, so the most a put can ever be worth is its strike `K`. When a put is very deep in the money, it has almost no time value left, and exercising lets you collect the strike *cash now* and earn interest on it, rather than waiting until expiry. The time value of money on that locked-in cash can exceed the tiny remaining option time value, so early exercise becomes optimal. This is the textbook case where an American put is genuinely worth more than a European one.
2. **American calls just before a large dividend.** A stock's price drops by roughly the dividend amount on the ex-dividend date. If you hold a call, that drop hurts you and you do not receive the dividend (you do not own the shares). If the dividend is large enough to outweigh the call's remaining time value, it can pay to exercise *the day before* the ex-date, take delivery of the shares, and capture the dividend. Outside of a chunky dividend, this never applies.

Notice what is *not* on this list: ordinary ITM calls, ordinary ATM options, anything OTM, and anything with meaningful time value left. For the everyday option, early exercise is a mistake.

### The Indian setup: index European, stock American, all auto-handled

Now the part that matters most for an NSE F&O trader, because it determines what you can and cannot do:

- **Index options (Nifty, Bank Nifty, Fin Nifty, etc.) are European and cash-settled.** You cannot exercise them early even if you wanted to — they pay out only at expiry, against the exchange's settlement value, in cash. There is no stock to deliver. The American-vs-European debate is therefore *moot* for index options: you have no early-exercise right, and you do not need one, because you can always sell the option back in the very liquid market any second the market is open.
- **Single-stock options on NSE are American-style but physically settled**, and crucially they are **auto-exercised at expiry** by the exchange if they finish in the money (ITM). You do not phone anyone or click "exercise" — the exchange automatically exercises any ITM stock option at expiry, and physical settlement kicks in: the call holder *takes delivery* of the shares (and must pay the full contract value), the put holder *delivers* shares. This auto-exercise of ITM stock options at expiry is a frequent source of nasty surprises (see the risk note).

The practical upshot: in India you essentially never *manually* exercise. Index options can't be exercised early at all; stock options get auto-exercised for you at expiry. The skill is not "when do I exercise" — it is "when do I sell, and do I want to be holding an ITM stock option *into* expiry given physical settlement."

### The practical rule: capture value by selling, not exercising

Put it all together and the working rule for an Indian trader is simple: **you realise an option's value by squaring it off (selling it back) in the market, not by exercising it.** Selling captures intrinsic *plus* time value, keeps you in cash, and sidesteps physical-delivery headaches. Exercising — when it even happens — captures intrinsic only and, for stocks, can saddle you with a large delivery obligation. The only times you would deliberately let a stock option go to auto-exercise are when you genuinely want the underlying shares (or are running a covered/hedged position designed for delivery).

## Worked example (₹, Nifty/Bank Nifty)

Let's trace decay across the final days of a weekly Nifty option, and then test the exercise logic.

**Setup.** It is Monday. **Nifty spot = 24,000**, and we follow the **24,000 CE** (the ATM weekly call) into Thursday's expiry. Assume India VIX and spot stay roughly flat so we isolate pure time decay. A realistic decay path for that ATM call's premium (all of it time value, since intrinsic is zero at the strike) might look like this:

| Day | Days to expiry | ATM 24,000 CE premium (₹) | Time value lost that day (₹) |
|---|---|---|---|
| Monday | 4 | 96 | — |
| Tuesday | 3 | 80 | 16 |
| Wednesday | 2 | 60 | 20 |
| Thursday morning | ~0.3 | 34 | 26 |
| Thursday close (expiry) | 0 | 0 | 34 |

Read the right-hand column: the *daily* loss grows from ₹16 to ₹20 to ₹26 to a final ₹34. That is the acceleration — the decay cliff — in numbers. The option lost only ₹16 on Monday→Tuesday but a full ₹34 on the last day, even though the index never moved. With a Nifty lot of about 75 units (lot sizes are set by the exchange and change periodically), the buyer who held that lot from Monday open to expiry lost:

`96 points * 75 = ₹7,200` per lot — the *entire* premium — purely to decay, with Nifty unchanged.

**Now contrast an OTM call.** Take the **24,300 CE** (300 points OTM) over the same period, starting at ₹30 of premium (all fragile time value). Its path might be ₹30 → ₹20 → ₹11 → ₹4 → ₹0. Notice the difference: no final-day *cliff*, just a steady grind to zero — it had already bled most of its small value before expiry day even arrived. ATM cliffs; OTM bleeds.

**The exercise test.** Suppose instead you hold a **23,500 CE** (deep ITM) on Wednesday with spot at 24,000. Intrinsic = max(24000 - 23500, 0) = 500 points. Because it is an *index* option (European, cash-settled), you *cannot* exercise it early anyway. But even if it were an American stock option, exercising on Wednesday would hand you only the 500 points of intrinsic, while *selling* it would fetch, say, 512 — the 500 intrinsic plus 12 of leftover time value. Selling wins by 12 points (`12 * 75 = ₹900` per lot). That ₹900 is exactly the time value you would have thrown away by exercising. This is the rule in rupees: **sell, don't exercise.**

## Common mistakes / risk note

- **Believing a flat market is safe for buyers.** It is the opposite. If Nifty goes nowhere, your long option still loses time value every day, fastest in expiry week. "No move" is a losing scenario for a buyer.
- **Holding longs into the expiry-day cliff "hoping it comes back."** Expiry day is the steepest decay of all for ATM options — the value you are counting on to recover is evaporating fastest at precisely that moment.
- **Exercising instead of selling (where exercise is even possible).** Exercising forfeits all remaining time value. Almost always, squaring off in the market captures more. Early exercise pays only for deep-ITM puts or calls just before a big dividend — narrow cases that rarely touch a retail Indian trader.
- **The physical-settlement trap on stock options.** This is the big one in India. An NSE single-stock option that finishes even slightly ITM is **auto-exercised** at expiry into *physical delivery*. A trader holding a cheap ITM stock call into expiry can suddenly owe the **full contract value** of shares (lakhs of rupees), far beyond the small premium paid — and faces hefty margin and possible penalties. Always square off ITM stock options before expiry unless you truly intend to take or give delivery. (Index options have no such trap — they cash-settle.)
- **Confusing "long option = guaranteed to gain if right."** You must be right *enough and fast enough* to outrun decay. A 95-point ATM call needs roughly a 95-point favourable move just to break even at expiry, because that move only replaces the time value you paid.
- **The honest other side.** Selling options to harvest this decay is *not* free money. The tailwind is real, but a naked seller's loss is large and effectively undefined, and a fast adverse move plus a volatility spike can dwarf months of collected decay. SEBI studies find roughly **9 in 10 retail F&O traders lose money** — careless buyers fighting decay *and* over-leveraged sellers blown up by the rare big move.

## Key takeaways

- Time decay is the daily loss of an option's time value; at expiry, time value is zero and `Premium = Intrinsic value`.
- Decay is **not linear** — it scales with `sqrt(T)`, so it is gentle far from expiry and *accelerates* into a cliff in the final days.
- **ATM options cliff at the end; OTM options bleed steadily to zero; deep-ITM options barely decay.**
- The option's smooth value curve sags down over time and lands exactly on the kinked intrinsic-value "hockey stick" at expiry.
- **European** = exercise only at expiry; **American** = exercise any time. Early exercise forfeits time value, so it is almost never optimal — only for deep-ITM puts or calls just before a large dividend.
- In India: **index options are European and cash-settled**; **stock options are American-style, physically settled, and auto-exercised when ITM at expiry.**
- You capture an option's value by **selling it back**, not by exercising — and you should square off ITM stock options before expiry to avoid physical-delivery surprises.

## Practice problems

1. **(Conceptual)** Two Nifty options have identical strikes and identical premiums today, but one has 3 days to expiry and the other has 27 days. Which one will lose a larger *fraction* of its time value over the next single day, and why?

2. **(Numeric)** An ATM weekly Nifty call follows this premium path on consecutive days with spot unchanged: ₹84 → ₹70 → ₹52 → ₹28 → ₹0. Compute the value lost each day and confirm whether the decay is accelerating. What is the total rupee loss on one lot of 75?

3. **(Conceptual)** A trader holds a deep-ITM American call on Reliance with plenty of time value remaining and no upcoming dividend. He is tempted to exercise early to "lock in the gain." What should he do instead, and why is exercising a mistake here?

4. **(Conceptual)** Explain why the early-exercise question is essentially irrelevant for someone trading only Nifty and Bank Nifty options.

5. **(Numeric)** Bank Nifty spot is 52,500 on expiry morning. You hold the 52,000 CE, currently quoted at ₹540. If you exercise (hypothetically) you collect only intrinsic value; if you sell you collect the full ₹540. How much time value would exercising throw away, and what is that in rupees on one lot of 30?

6. **(Conceptual + risk)** A beginner buys one ITM single-stock call option on NSE for a small premium and forgets about it through Thursday expiry. The stock closes slightly above the strike. Describe what happens automatically and why this can be financially dangerous.

## Solutions

**1.** The option with **3 days to expiry** loses a far larger fraction of its time value over the next day. Time value scales with `sqrt(T)`. Going from 27 to 26 days barely changes `sqrt(T)` (about a 2% drop), so almost no value is lost. Going from 3 to 2 days is a much bigger proportional cut in `sqrt(T)` (about 18%), so a much larger slice of time value evaporates. Decay accelerates as expiry nears, so the near-dated option is in the steep part of the curve.

**2.** Daily losses: 84→70 = **14**; 70→52 = **18**; 52→28 = **24**; 28→0 = **28**. The daily loss grows 14 → 18 → 24 → 28, so yes, decay is **accelerating** (the classic ATM expiry cliff, biggest drop on the last day). Total loss on one lot = full premium of 84 points: `84 * 75 = ₹6,300` — lost entirely to decay with spot unchanged.

**3.** He should **sell (square off) the call in the market, not exercise it.** Exercising collects only the intrinsic value and forfeits the remaining time value; selling collects intrinsic *plus* that time value. With no dividend and plenty of time value left, this is the textbook case where early exercise of an American call is never optimal — selling always does at least as well. Exercising would simply gift the leftover time value away.

**4.** Because **Nifty and Bank Nifty options are European and cash-settled.** European means they *cannot* be exercised before expiry at all, so there is no early-exercise decision to make. And cash settlement means at expiry the exchange just pays the intrinsic value in cash — no shares change hands, no delivery logistics. The trader realises value by selling the option back in the (very liquid) market any time, so the American-vs-European distinction never bites.

**5.** Intrinsic = max(S - K, 0) = max(52,500 - 52,000, 0) = **500 points**. The option trades at ₹540, so time value = 540 - 500 = **40 points**. Exercising would collect only the 500 intrinsic and throw away the 40 of time value. In rupees on one lot of 30: `40 * 30 = ₹1,200` left on the table. (In reality Bank Nifty is an index option you cannot exercise early anyway — but the arithmetic shows exactly why selling beats exercising.)

**6.** Because NSE single-stock options are **American-style, physically settled, and auto-exercised when ITM at expiry**, the exchange will automatically exercise his slightly-ITM call. Auto-exercise of a call means he must **take physical delivery** of the shares — paying the *full contract value* (often lakhs of rupees), not just the small premium he paid. He may not have that cash or margin, triggering large margin demands, penalties, or a forced unwind at a loss. The danger is the mismatch: a tiny premium turns into a huge delivery obligation. The fix is to **square off ITM stock options before expiry** unless he genuinely wants the shares. (Index options carry no such risk — they cash-settle.)
