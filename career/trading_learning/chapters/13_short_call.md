# Chapter 13: Short Call — Selling Premium and the Unlimited-Risk Warning

Picture an insurance company. It collects a small, steady premium from thousands of motorists, and most years it simply keeps that money because most cars never crash. The business looks wonderful — cash flows in, nothing flows out — right up until a hailstorm flattens an entire city's worth of cars on the same afternoon and the company must pay every claim at once. That single bad day can erase years of quiet profit. When you **sell (write) a call option**, you become exactly that insurer. You collect a small premium today for promising to cover someone else's upside, you win quietly most of the time, and you carry the risk of one violent up-move that pays out far more than you ever collected.

This chapter is deliberately written to scare you a little, because a **naked short call** — selling a call with no offsetting position — is the single most dangerous beginner trade on the entire NSE F&O menu. Its loss is genuinely **unlimited**. Not "large." Not "scary." Mathematically unbounded, because there is no ceiling on how high an index can go. We will work the rupees honestly, look at a real Indian gap-up that destroyed sellers, and then show the two ways the position becomes survivable: **covering it** (covered call) or **capping it** (bear call spread), both of which we preview here and study fully in later chapters.

## Core concepts

### What you are actually selling

A **call option** gives its *buyer* the right to buy the underlying at the **strike price (K)** on or before expiry. When you **write** (sell) that call, you take the opposite side: you receive the premium up front and accept the **obligation** to deliver — in cash, for index options — whatever the call is worth at expiry. You have sold someone else the right to your upside.

- **Premium:** the price of the option, quoted per unit of the underlying. If you sell the Nifty 24000 CE at ₹250 and Nifty's lot size is 75, you receive `250 * 75 = ₹18,750` in cash immediately.
- **Your right:** essentially none. You have already been paid; you cannot force the buyer to do anything.
- **Your obligation:** if at expiry the underlying (S) is above the strike, you must pay the buyer the difference `S - K` per unit. You are forced, in effect, to sell at a price below the market.
- **Your view:** bearish-to-neutral. You want the market to stay **at or below the strike** so the call expires worthless and you keep every rupee of premium.

The payoff at expiry, per unit, is the exact mirror of the long call from Chapter 3:

`Payoff (short call) = premium - max(S - K, 0)`

Read that formula slowly, because the entire danger lives inside it. The `premium` term is a fixed number — the most you can ever make. The `max(S - K, 0)` term has **no upper bound**: as S climbs, it climbs with it forever. A fixed gain minus an unbounded loss is the definition of an asymmetric trade stacked against you.

### Maximum profit is capped; maximum loss is unlimited

Let us pin down the two numbers that define every short call.

- **Maximum profit = the premium received.** This is achieved, and only achieved, when the underlying finishes **at or below the strike** at expiry. Then `max(S - K, 0) = 0` and you keep the whole premium. You can never make one rupee more than the premium, no matter how far the market falls. Whether Nifty closes at 23,900 or crashes to 18,000, your gain on a 24000 short call is identical: the premium. Falling markets do not reward you extra — they just guarantee the maximum, which is already small.
- **Maximum loss = unlimited.** For every point the underlying finishes above the strike, you lose one point per unit (times the lot size), forever. There is no level at which the bleeding stops on its own. If you sold the 24000 call and Nifty closes at 25,000, you lose `(25000 - 24000) - premium` per unit. At 27,000 you lose `(27000 - 24000) - premium`. The index can, in principle, double; your loss simply tracks it upward without limit.

This is the inverse of the long call you already know. The long call buyer has limited loss (the premium) and unlimited gain. You, the writer, are on the other side of that very contract: **limited gain, unlimited loss.** Options are zero-sum between the two parties — every rupee the buyer makes is a rupee you lose, and vice versa.

### Breakeven

You do not start losing money the instant the market crosses the strike — first the buyer has to "use up" the premium you collected. The level where your profit turns into a loss is:

`Breakeven (short call) = strike + premium`

For the 24000 call sold at ₹250, breakeven is `24000 + 250 = 24,250`. Between the strike (24,000) and breakeven (24,250) you still make a partial profit; the call is in-the-money for the buyer, but not by enough to exceed the premium you banked. Above 24,250 you are in net loss territory, and that loss grows one-for-one with the index from there to infinity.

### The figure: visualising the asymmetry

![Figure: payoff of a short 24000 call at expiry](figs/short_call.png)

The chart tells the whole story at a glance. To the left of the strike the line is **flat** at a small positive level — the premium. That flat ceiling is your best possible outcome, no matter how far left the market travels. At the strike the line begins to slope downward; it crosses zero at breakeven (24,250) and then keeps falling at 45 degrees with no floor. A long call's payoff is a hockey stick that points hopefully up and to the right; the short call is that same stick flipped — a small flat reward and a downward ramp that **never turns back up.** When a payoff diagram has a flat top and an open-ended bottom, your job is to respect the bottom, because that is where the account-ending losses live.

### Margin: why selling ties up real capital

When you buy an option, you pay the premium and that is the most you can lose, so the exchange asks for nothing more. When you **sell** an option, your potential loss is open-ended, so NSE forces you to post **margin** — collateral that proves you can honour the obligation.

This margin is computed by a system called **SPAN** (which simulates how your position would lose across a range of price and volatility moves) plus an **exposure margin** add-on. For a single naked index short call, expect to block roughly **₹1.2 to ₹1.6 lakh or more per lot**, varying with how close the strike is and how high **India VIX** (the market's volatility gauge) sits. Compare that to the ₹18,750 premium: you tie up well over a lakh to earn a fraction of it, and that margin can be **increased intraday** if the market moves against you, triggering a **margin call**. If you cannot top up, your broker may square off at the worst possible moment. The premium feels like free income; the margin is the market reminding you it is not.

### Assignment risk

**Assignment** is what happens when the option buyer exercises and you, the writer, are called upon to settle. For **Indian index options** (Nifty, Bank Nifty) this is mercifully clean: they are **European** (exercisable only at expiry) and **cash-settled**, so at expiry you simply pay the cash difference `S - K` per unit if you are in-the-money. No shares change hands, and there is no early surprise.

For **stock options** the rules are harsher: they are **American-style** (the buyer can exercise any day before expiry) and **physically settled**. If you write a call on, say, Reliance and it finishes in-the-money, you are obliged to **deliver the actual shares** — and the margin/penalty regime for physical settlement is severe. Many beginners who casually sold stock calls have been hit with sudden delivery obligations and large physical-settlement margins in the final days before expiry. Know which kind of option you are writing.

### Why a naked short call is so dangerous for a beginner

Put the pieces together and the trap becomes obvious:

1. **The risk is mathematically unlimited.** No other common beginner position has a truly unbounded loss. (A short *put* is dangerous too, but its loss stops when the underlying hits zero. A short *call* has no such floor — there is no maximum price for an index.)
2. **The reward is small and fixed.** You risk lakhs to make thousands. One bad trade can wipe out the premium from many good ones.
3. **Markets gap.** The danger is not the slow grind upward — you could buy that back. The danger is the **overnight or pre-open gap**, where the market reopens far above your strike and there was never a chance to exit at a sensible price. Your stop-loss is useless against a gap.
4. **It seduces with a high win rate.** Most options expire worthless, so a naked seller wins *often* — maybe 8 or 9 times out of 10. That long string of small wins breeds overconfidence and oversizing, right up to the single loss that dwarfs them all. High win rate is not the same as positive expectancy.

### How it becomes safe: cover it or cap it

The naked short call is dangerous because the top of the position is open. There are two standard ways to close that top, and both are previewed here and taught in full later.

- **Covered call (own the underlying):** if you already **hold** the underlying — long Nifty futures, or the actual basket of stocks — and write a call against it, then if the market rockets, the gains on your holding rise to offset the losses on the short call. You have *covered* your obligation with the asset itself. The unlimited loss disappears; in exchange, your upside on the holding is capped at the strike. This is a legitimate, conservative income strategy used by long-term holders. (Covered in its own chapter.)
- **Bear call spread (buy a higher call):** if you simultaneously **buy** a call at a higher strike, that long call acts as insurance — above its strike, your losses are frozen. You collect a smaller net premium, but your maximum loss becomes a **known, finite number** (the gap between strikes minus the net premium). You have *capped* the open top. This is how disciplined traders express a bearish-to-neutral view without betting the account. (Covered in the spreads chapter.)

The lesson to carry forward: **never leave the top of a short call open.** Either own the asset beneath it or buy a higher call above it.

## Worked example (₹, Nifty)

Nifty is trading at **24,000**. You are mildly bearish-to-neutral over the next two weeks and decide to **write one lot of the 24000 CE** (the at-the-money call) at a premium of **₹250**. Nifty's lot size is **75**.

**Step 1 — Cash received and margin blocked.**
`Premium received = 250 * 75 = ₹18,750`, credited to you immediately. This is your **maximum profit** — full stop. To hold the position, the exchange blocks SPAN + exposure margin of roughly **₹1.3 lakh** (it varies). So you have tied up about ₹1.3 lakh of capital to earn at most ₹18,750.

**Step 2 — Breakeven.**
`Breakeven = strike + premium = 24000 + 250 = 24,250.` You profit if Nifty finishes below this, and lose above it.

**Step 3 — Outcomes at expiry.** Per-unit payoff is `250 - max(S - 24000, 0)`; multiply by 75.

- **Nifty closes at 23,000 (fell hard).** `max(23000 - 24000, 0) = 0`. Net per unit = ₹250. **P&L = +₹18,750.** Note: a 1,000-point crash earns you exactly the same as a 1-point dip below the strike — the premium, and not a rupee more.
- **Nifty closes at 24,000 (flat).** Intrinsic value 0. **P&L = +₹18,750** (maximum profit).
- **Nifty closes at 24,250 (breakeven).** `max(24250 - 24000, 0) = 250`. Net per unit = `250 - 250 = 0`. **P&L = ₹0.**
- **Nifty closes at 24,500.** Intrinsic = 500. Net = `250 - 500 = -250`. **P&L = -₹18,750.** A move of just 500 points has already wiped out the entire premium.
- **Nifty closes at 25,000.** Intrinsic = 1,000. Net = `250 - 1000 = -750`. **P&L = -₹56,250** — three times the premium you collected.
- **Nifty closes at 26,000 (a violent rally).** Intrinsic = 2,000. Net = `250 - 2000 = -1750`. **P&L = -₹1,31,250** — your entire margin, gone, on one position.

**Step 4 — See the asymmetry plainly.** Best case, market falls to *any* level: **+₹18,750**, capped forever. Market at 25,000: **-₹56,250.** At 26,000: **-₹1,31,250.** At 27,000: **-₹2,06,250** — and there is still no upper limit. You collected ₹18,750 to expose yourself to losses running into lakhs. That is the bargain of the naked call writer, written out in rupees.

### A real cautionary tale: the gap-up that punishes sellers

Imagine you wrote out-of-the-money Bank Nifty calls one evening, comfortable that the index sat well below your strike, collecting a tidy premium. Overnight, surprisingly strong election exit-poll results hit. The market did not *drift* toward your strike — it **gapped open** the next morning far higher, blowing straight past your strike before you could click "exit." On 20 May 2019, Bank Nifty jumped roughly **2,000 points (about 7%)** in a single session on exit-poll optimism. A seller who thought they were "safely" 500 points away woke up deep in-the-money with no chance to manage the trade. Premiums that were ₹40 the previous evening reopened at ₹400 or more, and SPAN margins spiked at the same time, forcing square-offs at the worst prices. Accounts that had ground out small premiums for months were halved in one morning. **A stop-loss order cannot protect you against a gap, because the price you wanted to exit at never traded.** This is precisely the hailstorm that ruins the naive insurer.

## Common mistakes / risk note

**Treating premium as "income" and ignoring the tail.** The cash hits your account on day one and feels like salary. It is not income; it is a liability you have sold, and its eventual cost is unknown and potentially enormous. Judge a short call by its worst case, never by the cheerful premium credit.

**Selling naked because "most options expire worthless."** True — and irrelevant to survival. A high win rate with an unlimited loss on the rare loss is a classic route to ruin. One 8% gap can erase the premiums of a dozen winning weeks. Frequency of winning says nothing about the *size* of the loss when you lose.

**Believing a stop-loss makes naked selling safe.** Stops fail exactly when you need them most — during gaps and fast moves, when the market leaps over your stop level and fills you far worse, if at all. The only reliable cap on a short call's loss is a *bought higher call* (a spread) or *ownership of the underlying* (a covered call).

**Forgetting margin can rise against you.** SPAN margin is not fixed. As the market moves toward and past your strike, and as India VIX spikes, your required margin balloons, and a margin call can force you out at the worst moment. Always keep a large buffer; never sell options on a tightly-funded account.

**Writing stock calls without understanding physical settlement.** In-the-money stock calls at expiry mean delivering actual shares and facing heavy physical-delivery margins in the final days. If you do not intend to deliver shares, close the position well before expiry — or do not write it.

**The honest big picture.** SEBI's studies find that roughly **9 in 10 individual F&O traders lose money.** Naked option *selling*, with its open-ended risk, is one of the fastest ways to join the losing nine — not because the strategy is irrational for professionals, but because beginners size it wrongly and meet a gap before they meet discipline. Add costs: **STT** is charged on the premium when you sell and on the settlement value of in-the-money options at expiry, plus brokerage, exchange fees and GST. Sell only what you can either cover or cap.

## Key takeaways

- Writing a call collects a premium today in exchange for the **obligation** to pay `S - K` per unit if the underlying finishes above the strike. `Payoff (short call) = premium - max(S - K, 0)`.
- **Maximum profit = the premium**, achieved whenever the market finishes at or below the strike. Falling markets pay you nothing extra — the gain is capped.
- **Maximum loss is unlimited.** There is no ceiling on how high an index can go, so there is no floor on your loss. This is the only common beginner position with truly unbounded risk.
- **Breakeven = strike + premium.** Between the strike and breakeven you still profit; above breakeven, losses grow one-for-one with the index, forever.
- Selling requires **SPAN + exposure margin** (often well over a lakh per lot), which can rise intraday and trigger forced square-offs. The premium is small relative to the capital and risk involved.
- **Gaps are the killer.** Stop-losses do not protect against overnight or pre-open jumps; a single gap-up (e.g. Bank Nifty's ~2,000-point election-day jump in May 2019) can destroy a naked seller.
- A naked short call becomes survivable only when **covered** (you own the underlying — covered call) or **capped** (you buy a higher-strike call — bear call spread). Never leave the top open.

## Practice problems

1. **(Conceptual)** In one or two sentences, explain why the maximum loss on a short call is described as "unlimited," whereas the maximum loss on a short *put* is large but finite.

2. **(Numeric)** You write one lot of **Nifty 24200 CE** at a premium of **₹180**, lot size **75**. Compute (a) the premium received, (b) your maximum profit, (c) your breakeven level.

3. **(Numeric)** Using the position in Problem 2, find your net P&L if Nifty closes at expiry at (a) 23,800, (b) 24,200, (c) 24,380, (d) 24,800, (e) 25,500.

4. **(Numeric / risk)** You write one lot of **Bank Nifty 52000 CE** at **₹300**, lot size **30**. Overnight the market gaps up and Bank Nifty closes the next session's expiry at **54,000**. What is your net P&L? Compare it to the premium you collected and to a hypothetical best case.

5. **(Conceptual)** A friend says: "I sold Nifty calls every week for three months and won 11 weeks out of 12 — selling calls clearly works." Explain what this track record does and does not tell you about the strategy's safety.

6. **(Conceptual)** Briefly describe the two ways to remove the unlimited-loss feature of a short call, and state what you give up in each case.

## Solutions

**1.** A short call loses `S - K` per unit as the underlying S rises above the strike K, and an index has **no maximum price** — it can keep climbing without bound — so the loss has no upper limit. A short put loses `K - S` as S *falls* below K, but the underlying cannot fall below **zero**, so the worst case is bounded at `K - premium` per unit (when S = 0). No floor on price means unlimited loss for the call; a floor of zero means a large-but-finite loss for the put.

**2.** (a) Premium received = `180 * 75 = ₹13,500`. (b) Maximum profit = the premium = **₹13,500** (whenever Nifty finishes at or below 24,200). (c) Breakeven = `strike + premium = 24200 + 180 = 24,380`.

**3.** Per-unit payoff = `180 - max(S - 24200, 0)`, times 75.
- (a) **23,800:** `max(23800 - 24200, 0) = 0`; net = `180`; total = `180 * 75 = +₹13,500` (max profit).
- (b) **24,200:** intrinsic 0; net = `180`; total = **+₹13,500** (still max profit, at the strike).
- (c) **24,380:** intrinsic = `24380 - 24200 = 180`; net = `180 - 180 = 0`; total = **₹0** (breakeven).
- (d) **24,800:** intrinsic = `600`; net = `180 - 600 = -420`; total = `-420 * 75 = -₹31,500`.
- (e) **25,500:** intrinsic = `1300`; net = `180 - 1300 = -1120`; total = `-1120 * 75 = -₹84,000`.
Note how the loss in (e) is more than six times the premium collected — and would keep growing if Nifty rose further.

**4.** Per-unit payoff = `300 - max(54000 - 52000, 0) = 300 - 2000 = -1700`. Total = `-1700 * 30 = -₹51,000`. You collected only `300 * 30 = ₹9,000` in premium, so the gap turned a ₹9,000 "income" into a **₹51,000 loss** — more than five times the premium — with no chance to exit, since the move happened on a gap. The best case was capped at +₹9,000; the realised loss shows the asymmetry brutally. Had the gap been larger (say to 56,000), the loss would have been `(300 - 4000) * 30 = -₹1,11,000`, with still no upper bound.

**5.** The 11-of-12 record reflects only the **frequency** of small wins, which is expected because most options expire worthless — it says nothing about the **size** of the loss in the rare losing case. A naked short call has unlimited downside, so a single bad week (especially a gap) can lose more than the combined premium of all 11 winning weeks, turning a "winning" strategy into a net loss. High win rate is not the same as positive expectancy or safety; you must weigh each loss by how large it can be, not just how often it occurs. Three months is also far too short to have encountered a tail event.

**6.** (i) **Covered call:** hold the underlying (e.g. long Nifty futures or the stock basket) and write the call against it; gains on the holding offset the short call's losses if the market rallies, removing the unlimited loss. **You give up** the upside on your holding above the strike (your gains are capped there). (ii) **Bear call spread:** simultaneously buy a higher-strike call as insurance; above that strike your losses are frozen, making the maximum loss a known, finite number (strike difference minus net premium). **You give up** part of the premium (the net credit is smaller because you paid for the higher call). In both, you trade away some reward to convert an unlimited risk into a defined one.
