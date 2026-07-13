# Chapter 11: Long Call — The Bullish Bet

Imagine you are sure a stock or an index is about to climb, but you do not want to risk a large sum if you turn out to be wrong. You would love a deal that says: "Pay a small, fixed fee today. If I'm right and the market rises, I capture the whole rally. If I'm wrong, the most I can lose is that small fee — and not one rupee more." That deal exists. It is called **buying a call**, and it is the most natural first trade in all of options.

The **long call** is the purest bullish bet in options: a single position whose risk is capped at the premium you pay, whose reward is theoretically unlimited, and whose personality is shaped by two clocks ticking against each other — the price moving in your favour, and time bleeding the value away. This chapter takes you from the plain intuition to choosing the right strike and expiry like a professional, with a full rupee Nifty example.

## Core concepts

### What "buying a call" actually means

A **call option** is the *right, but not the obligation*, to buy the underlying at a fixed price (the **strike**, written `K`) on or before expiry. When you **buy** (go "long") a call, you pay a one-time **premium** to own that right. The seller of the call collects your premium and takes on the matching obligation.

Because Indian index options (Nifty, Bank Nifty) are **European and cash-settled**, you never literally "buy the index" at the strike. Instead, at expiry the exchange simply pays you the option's intrinsic value in cash. But the intuition is identical: you have locked in a *floor purchase price*, and you profit when the market rises above that floor by more than what you paid.

Think of a call as a **token that locks in a fixed price.** You pay ₹100 for a token to buy a plate at today's price of ₹500. If the price later jumps to ₹800, your token is worth ₹300. If the price drops to ₹400, you throw the token away — out only the ₹100 you paid, never more.

### The payoff: what you make at expiry

At expiry, a long call is worth its **intrinsic value** — how far the spot `S` has risen above the strike `K`:

`Intrinsic value at expiry = max(S - K, 0)`

But you *paid* the premium to own that right, so your actual profit-and-loss is the intrinsic value minus what you spent:

`Payoff (long call) = max(S - K, 0) - premium`

This single formula contains the entire shape of the trade. Read it in three zones:

- **Spot far below strike** (`S < K`): the `max(...)` term is zero. Your payoff is just `- premium`. You lose the whole premium, but nothing more. This is the flat floor of the payoff.
- **Spot above strike but not by much**: the option has intrinsic value, but not yet enough to cover the premium. You are recovering your cost — still at a net loss, but shrinking.
- **Spot well above strike**: intrinsic value exceeds the premium, and every additional point the market rises is a point of pure profit.

### Breakeven, maximum loss, and maximum gain

Three numbers define a long call completely.

**Breakeven** is the spot level at expiry where you exactly recover your premium — profit is zero. Set the payoff to zero and solve:

`Breakeven = strike + premium = K + premium`

You do not just need the market above the strike; you need it above the strike *by the full premium you paid.* That gap is the price of admission.

**Maximum loss** is fixed and known the moment you enter:

`Max loss = premium paid` (occurs whenever `S <= K` at expiry)

This is the defining beauty of a long call. No matter how violently the market crashes, you cannot lose more than the premium. Your risk is **defined, capped, and paid up front** — there are no margin calls, no overnight gaps that wipe you out, no "undefined risk." A long call holder sleeps soundly through a crash.

**Maximum gain** is, in principle, **unlimited**:

`Max gain = unlimited` (the market can, in theory, rise without bound)

In practice a Nifty rally is finite, but the point stands: your upside is open-ended while your downside is bolted to the floor. That asymmetry — small fixed loss, large open gain — is exactly what you are paying the premium for.

### The leverage angle: why not just buy futures or the cash index?

Here is where the long call earns its keep. Suppose Nifty is at 24,000 and you are bullish.

- **Cash/ETF route:** to ride one lot-equivalent (about 75 units) you tie up roughly `24,000 * 75 = ₹18,00,000`. No leverage, but also no decay and no expiry.
- **Futures route:** one Nifty futures lot needs **SPAN + exposure margin** of roughly ₹1.5–2 lakh (set by the exchange, varying with volatility). You get the full point-for-point move, but your risk is symmetric and **undefined on the downside** — a 5% gap down costs 5% of ₹18 lakh notional, and may trigger a margin call.
- **Long call route:** you pay, say, ₹150 per unit for an ATM call, i.e. `150 * 75 = ₹11,250` for one lot. That ₹11,250 is your *entire* risk. Yet if Nifty rallies 1,000 points, the call's intrinsic value alone is worth `~₹70,000+` per lot before costs.

So a long call gives **futures-like upside for a fraction of the capital, with downside capped at the premium.** That is real leverage. But the call's hidden cost — the thing futures and cash do *not* charge you — is **time decay**. You are renting directional exposure, and rent must be paid.

### Choosing the strike: ITM vs ATM vs OTM

Not all calls are the same bet. The strike you pick changes the whole character of the trade. Suppose Nifty is at 24,000.

- **In-the-money (ITM) call** — e.g. the 23,800 CE. Strike is *below* spot, so it already has 200 points of intrinsic value. It is **expensive** (high premium), but it is mostly "real" value, so it has **little time value to lose** and a **high delta** (it moves nearly point-for-point with Nifty, behaving like a leveraged future). Best when you have **high conviction** and want the position to track the index closely without much decay drag. Lower percentage leverage, higher probability of finishing in profit.

- **At-the-money (ATM) call** — e.g. the 24,000 CE. Strike ≈ spot. It is **all time value**, carries the **most time value of any strike**, and has a delta near 0.5. It is the **most sensitive to a move starting now** (highest gamma) but also bleeds time value the fastest. The balanced, middle-of-the-road choice for a clear directional view over a short horizon.

- **Out-of-the-money (OTM) call** — e.g. the 24,300 CE. Strike is *above* spot. **Cheap** premium, low delta, **lottery-ticket** profile. A small move does almost nothing; you need a *big, fast* rally to pay off. The percentage gains can be enormous if you are right, but **most OTM calls expire worthless.** Buying these because "they cost so little" is the single most common way retail buyers lose money.

The trade-off in one line: **deeper ITM = costlier, higher win-rate, lower leverage, less decay; further OTM = cheaper, lower win-rate, explosive leverage, brutal decay.**

### Choosing the expiry: theta vs time to be right

The expiry you choose is a tug-of-war between two forces.

- **Near expiry (this week's weekly):** cheap in absolute rupees, but **time decay (theta) is savage** — you are sitting in the steepest part of the decay curve. You need the move to happen *now*. Great if your catalyst is today or tomorrow; merciless if the market dawdles.
- **Far expiry (next month):** **more expensive**, but theta is gentle and you buy yourself **time to be right.** If your thesis needs a few weeks to play out, the slower decay is worth the higher premium.

The professional's rule of thumb: **match the expiry to your catalyst.** If you expect a move within two days, a weekly is fine. If you are playing a theme that needs three weeks, do not buy a weekly and pray — buy enough time, or you will be stopped out by decay before you are proven right.

### The reality of theta drag: today's line sits below the expiry line

Here is the concept that separates beginners from professionals, and the one the figure below makes unforgettable.

The clean payoff diagram — flat at `-premium`, then kinking up at the breakeven — describes your P&L **only at the instant of expiry.** *Before* expiry, your position is worth more than its intrinsic value because it still carries **time value**. So if you plotted your P&L *today* against the spot level, the curve would be a **smooth bowed line sitting below the hard expiry hockey-stick** in the profit region, and *above* it in the loss region (your loss today is smaller than the eventual max loss, because some time value remains).

As each day passes with the market sitting still, that smooth "today" curve **sinks down toward the angular expiry line.** This sinking is **theta drag** — the daily erosion of time value. It means:

- You can be **right on direction and still lose**, if the move is too slow. The decay can outrun a gentle rally.
- A long call needs the market to move **enough, and fast enough,** to outrun theta. Standing still is a slow loss.
- The closer to expiry, the faster the "today" line collapses onto the expiry line — decay accelerates in the final days.

This is the long-call buyer's escalator-going-the-wrong-way problem. You are not just betting on direction; you are racing the clock.

![Figure: long call P&L today vs at expiry](figs/long_call_time.png)

In the figure, the straight kinked line is the **at-expiry** payoff. The curve above it is your **P&L today**, with time left on the clock. The gap between them is the **time value you would surrender** if the market never moved — and the curve droops toward the straight line a little more each day. That droop is theta at work.

## Worked example (₹, Nifty/Bank Nifty)

Let's make it concrete. It is Monday. **Nifty spot = 24,000.** You are bullish and expect a rally this week. You buy **one lot of the 24,000 ATM weekly call (24,000 CE)** at a premium of **₹150**. Lot size is **75** (set by the exchange; it changes periodically).

**Your position summary:**

- Premium paid = `150 * 75 = ₹11,250`. This is your **maximum loss**, full stop.
- Breakeven at expiry = `K + premium = 24,000 + 150 = 24,150`.
- Maximum gain = unlimited (rises with Nifty).

**P&L at several expiry levels.** At expiry the call is worth `max(S - K, 0)` per unit, and your net payoff per unit is `max(S - K, 0) - 150`. Multiply by 75 for the lot.

| Nifty at expiry (S) | Intrinsic = max(S-24000,0) | Per-unit P&L = Intrinsic - 150 | Lot P&L = per-unit * 75 |
|---|---|---|---|
| 23,500 | 0 | -150 | **-₹11,250** (max loss) |
| 23,800 | 0 | -150 | **-₹11,250** (max loss) |
| 24,000 | 0 | -150 | **-₹11,250** (max loss) |
| 24,100 | 100 | -50 | **-₹3,750** |
| 24,150 | 150 | 0 | **₹0** (breakeven) |
| 24,250 | 250 | +100 | **+₹7,500** |
| 24,400 | 400 | +250 | **+₹18,750** |
| 24,700 | 700 | +550 | **+₹41,250** |

Read what the table teaches:

- **At or below 24,000**, every outcome is the same flat loss of ₹11,250. The market crashing 500 points hurts no more than it closing exactly at the strike. That flat floor is your defined risk.
- Between 24,000 and 24,150 you are **above the strike but still losing**, because the rally has not yet repaid the ₹150 premium. Being "right" (market up 100 points) still leaves you down ₹3,750. This is the breakeven gap in action.
- **24,150 is breakeven.** Nifty had to rally 150 points — about 0.6% — *just to get you to zero*, purely because that move replaces the time value you paid.
- Above 24,150, profit climbs point-for-point and is **open-ended**. A 700-point rally turns ₹11,250 of risk into ₹41,250 of profit — nearly 4x. That is the leverage and the asymmetry working for you.

**Now the theta-drag reality.** Suppose it is Wednesday and Nifty is *still* 24,000 — unchanged. Your call has not lost on direction, but two days of time value have bled out. The premium might have fallen from ₹150 to about ₹95. On paper you are down `(150 - 95) * 75 = ₹4,125` despite the index being exactly where you bought it. To *break even now* you would need Nifty to rally enough to push the premium back to ₹150 — and with less time left, that takes a bigger move than it would have on Monday. This is precisely the "today line sinking toward the expiry line" from the figure: you are right that the market did not fall, yet you are losing to the clock.

**Costs note:** real P&L is slightly lower after **STT** (charged on the premium for buyers, and on intrinsic value at expiry/exercise — a reason many traders square off before expiry rather than letting ITM options settle), brokerage, exchange fees, and GST. These are small relative to the moves above but real, and they matter most for cheap OTM trades.

## Common mistakes / risk note

- **Treating "no move" as safe.** A flat market is a *losing* scenario for a long call. Every quiet day, theta takes a bite. You need movement, and you need it before expiry.
- **Buying far-OTM weeklies because they're cheap.** A ₹15 OTM call feels like a small bet, but it is almost pure low-probability time value. The vast majority expire worthless. Cheap is not the same as good value — you are buying a lottery ticket and paying STT on it.
- **Ignoring the breakeven gap.** Beginners think "Nifty above my strike = profit." Wrong. You profit only above `strike + premium`. The premium is a hurdle the market must clear before you make a single rupee.
- **Mismatching expiry to thesis.** Buying a weekly for a view that needs three weeks to play out. The decay will kill you long before you are proven right. Match the clock to the catalyst.
- **Forgetting the volatility risk (vega).** You can be right on direction and still lose if **India VIX** falls and crushes the time-value portion of your premium — a "vol crush," common right after an expected event. Buying calls into high VIX (expensive premiums) and watching VIX collapse is a classic trap.
- **The honest big picture.** The long call's risk is genuinely capped, which makes it one of the *safer* ways to express a view — but "capped risk" still means you can lose **100% of the premium**, and long options frequently do exactly that. SEBI studies find roughly **9 in 10 retail F&O traders lose money**, and over-paying for time value then watching it decay is one of the main reasons. The defined risk protects you from ruin; it does not hand you an edge.

## Key takeaways

- A long call is a **defined-risk bullish bet**: `Payoff = max(S - K, 0) - premium`.
- **Breakeven = strike + premium.** You must be right *by more than the premium*, not merely right on direction.
- **Maximum loss = the premium**, fixed and paid up front; **maximum gain is theoretically unlimited.** This asymmetry is the whole point.
- It delivers **futures-like upside on a fraction of the capital**, with downside capped — but charges **time decay (theta)** as rent that futures and cash do not.
- **Strike choice** trades cost against probability: ITM (costly, high win-rate, low decay) → ATM (balanced, max time value) → OTM (cheap, lottery, brutal decay). **Expiry choice** trades premium against time to be right — match it to your catalyst.
- Before expiry your P&L sits on a **curve that sinks toward the at-expiry hockey-stick** as theta bleeds time value. Being right on direction is not enough — you must be right **enough and fast enough** to outrun the clock.

## Practice problems

1. **(Conceptual)** You buy a Nifty 24,200 CE for a premium of ₹90 with spot at 24,000. State the breakeven, the maximum loss, and the maximum gain. At what spot at expiry do you start making a net profit?

2. **(Numeric)** Bank Nifty spot is 52,000. You buy one lot of the 52,000 CE at ₹600. Lot size is 30. Compute your premium outlay, breakeven, and your lot P&L if Bank Nifty expires at (a) 51,500, (b) 52,000, (c) 52,600, (d) 53,400.

3. **(Numeric)** With Nifty at 24,000, you are choosing between the 23,800 CE at ₹320 (ITM) and the 24,300 CE at ₹40 (OTM). For each, find the breakeven and the per-unit P&L if Nifty expires at 24,500. Which gave the higher *percentage* return on premium, and which had the higher chance of finishing in profit?

4. **(Conceptual)** You buy an ATM weekly Nifty call on Monday. By Wednesday the index is exactly where you bought it, yet your call has lost about 35% of its value. Nothing went "wrong" directionally. Explain what happened, using the idea of the today-line sinking toward the expiry-line.

5. **(Numeric)** You buy a Nifty 24,000 CE at ₹150 (lot size 75). At expiry Nifty settles at 24,090. Are you above or below your strike? Above or below breakeven? Compute your exact lot P&L and explain the apparent paradox to a friend who says "but the market went up, you should have made money."

6. **(Conceptual)** A trader with a three-week bullish thesis on Nifty buys this week's expiry call "because it's the cheapest." Critique this choice in terms of theta and expiry selection, and state what you would do instead.

## Solutions

**1.** Premium = ₹90, strike `K` = 24,200. Breakeven = `K + premium = 24,200 + 90 = 24,290`. Maximum loss = the premium = **₹90 per unit** (occurs at any expiry spot ≤ 24,200). Maximum gain = **unlimited**, rising point-for-point above breakeven. You begin making a *net profit* once spot at expiry exceeds **24,290** (above 24,200 you have intrinsic value, but you only turn net-positive past the breakeven).

**2.** Premium outlay = `600 * 30 = ₹18,000` (also the max loss). Breakeven = `52,000 + 600 = 52,600`. Per-unit payoff = `max(S - 52000, 0) - 600`; lot P&L = that × 30.
- (a) 51,500: intrinsic 0, per-unit -600, lot = **-₹18,000** (max loss).
- (b) 52,000: intrinsic 0, per-unit -600, lot = **-₹18,000** (max loss).
- (c) 52,600: intrinsic 600, per-unit 0, lot = **₹0** (breakeven).
- (d) 53,400: intrinsic 1,400, per-unit +800, lot = `800 * 30 =` **+₹24,000**.

**3.** Both bought with Nifty at 24,000; expiry at 24,500.
- **23,800 CE (ITM), premium ₹320:** breakeven = `23,800 + 320 = 24,120`. Intrinsic at 24,500 = `24,500 - 23,800 = 700`. Per-unit P&L = `700 - 320 =` **+₹380**. Percentage return on premium = `380 / 320 =` **+119%**.
- **24,300 CE (OTM), premium ₹40:** breakeven = `24,300 + 40 = 24,340`. Intrinsic at 24,500 = `24,500 - 24,300 = 200`. Per-unit P&L = `200 - 40 =` **+₹160**. Percentage return = `160 / 40 =` **+400%**.

The **OTM call gave the far higher percentage return (400% vs 119%)** — that is its lottery-ticket leverage. But the **ITM call had the higher chance of finishing in profit**: its breakeven (24,120) was just above spot, needing only a small rally, whereas the OTM needed Nifty above 24,340 to even break even. This is the core ITM-vs-OTM trade-off: explosive percentage upside comes bundled with a lower probability of winning.

**4.** Directionally nothing went wrong — but a long call's premium is partly **time value**, and an ATM call is **all** time value with the most of any strike. From Monday to Wednesday, two days of that time value decayed away (**theta drag**), so even with the index unchanged the premium fell. Visually, your **P&L-today curve sank toward the at-expiry hockey-stick**: with the spot sitting at the strike, the at-expiry payoff there is the full max loss, and each passing day pulls your present value down toward it. You needed the market to *move up* to offset the decay; standing still guaranteed a loss to the clock.

**5.** Strike = 24,000, so at 24,090 you are **above the strike** (intrinsic = `24,090 - 24,000 = 90`). But breakeven = `24,000 + 150 = 24,150`, so you are **below breakeven**. Per-unit P&L = `90 - 150 = -60`; lot P&L = `-60 * 75 =` **-₹4,500**. The paradox resolved: the market *did* rise 90 points, but you paid ₹150 for the option, and the rally only repaid 90 of those 150. You needed a 150-point move just to break even; a 90-point move recovers part of your premium but leaves you net down ₹4,500. Being right on direction is not enough — you must clear the **strike + premium** hurdle.

**6.** The mistake is **mismatching expiry to thesis.** A three-week view paired with this week's expiry puts the entire position in the **steepest part of the theta-decay curve**: even if the thesis is correct, the call will likely lose most of its value to time decay before the three-week move plays out, and may expire worthless mid-thesis. "Cheapest" in absolute rupees is the most decay-exposed, not the best value. **Better:** buy an expiry that comfortably covers the catalyst — the next monthly (or a longer-dated) call — accepting a higher premium in exchange for **gentle theta and time to be right**. Match the clock to the catalyst, not to the price tag.
