# Chapter 37: How to Choose a Strategy — View x Volatility x Risk

By now you have met dozens of option structures: long calls and puts, spreads, straddles, strangles, condors, calendars, butterflies. To a beginner this looks like a tangled menu with no obvious order — which one do you pick on a Tuesday morning when Nifty is at 24,000 and you have a hunch? The honest answer most losing traders never learn is this: you should almost never start from the strategy. You should start from your *view*, and let the strategy fall out of it. The strategy is the last decision, not the first.

This chapter gives you the decision framework that opens every professional options trade. It asks three questions — about direction, about volatility, and about how much you can afford to lose — and turns the answers into a shortlist of structures. Get into the habit of answering all three *before* you look at an option chain, and you will stop picking trades because they are exciting and start picking them because they fit what you actually believe. This is the master map for the rest of Part VI; every strategy chapter that follows is one cell in the table you are about to build.

## Core concepts

### Every trade answers three questions

A professional never thinks "I'll buy a call." They think: "I'm mildly bullish, I expect volatility to fall, and I want my risk capped at 2% of capital — therefore a bull put spread." Strategy is the *output* of three inputs:

1. **Directional view** — where do you think the underlying is going? Bullish (up), bearish (down), neutral (sideways / range-bound), or genuinely unsure (you have no edge on direction but a view on movement itself).
2. **Volatility view** — do you expect *movement* and *implied volatility (IV)* to rise or fall? And, separately, is IV *currently* cheap or rich? These are different: a market can have high IV that you still expect to climb, or low IV you expect to stay low.
3. **Risk appetite and capital** — are you willing to take *undefined* risk (option selling, where a bad move can lose far more than you collected), or do you need *defined* risk (your worst case is known and capped up front)? And how much of your capital can this single trade afford to lose?

Answer these three honestly and the strategy is nearly chosen for you. Skip any of them and you are gambling with leverage.

### Question 1 — what is your directional view?

This is the axis everyone already thinks about, so keep it simple. Sort your opinion into one of four buckets:

- **Bullish** — you expect the underlying to rise. Lean on calls, call spreads, or short puts.
- **Bearish** — you expect it to fall. Lean on puts, put spreads, or short calls.
- **Neutral** — you expect it to stay in a range, going roughly nowhere. This is the home of premium-selling structures: condors, butterflies, short straddles/strangles.
- **Unsure on direction, but with a movement view** — you genuinely cannot call up or down, but you *can* say whether the move will be big or small. This points you to pure volatility plays (straddles, strangles) where direction barely matters.

Be honest about conviction, too. "Mildly bullish" and "explosively bullish" lead to different structures — the first wants a defined-risk spread that profits from drift, the second wants a long call that can run.

### Question 2 — what is your volatility view, and is IV cheap or rich?

This is the axis beginners ignore and professionals obsess over. There are two sub-questions hiding inside it.

**(a) Direction of volatility.** Do you expect realised movement and IV to *rise* or *fall*? If you expect a storm — earnings, a budget, an RBI policy decision, an election result — you want to be **long volatility** (own movement: long options, positive vega and gamma). If you expect calm — a quiet week after the event has passed — you want to be **short volatility** (sell movement: collect premium, negative vega, positive theta).

**(b) Level of volatility right now.** Even if you expect IV to fall, *how expensive is it today?* This is where **IV rank** (introduced in Chapter 35) earns its keep. IV rank tells you where current IV sits between its 1-year low and high, on a 0–100 scale:

`IV rank = (current IV - 52-week low IV) / (52-week high IV - 52-week low IV) * 100`

- **High IV rank (say above 50)** — options are *expensive* relative to their own history. Premiums are fat. This favours **selling** premium (short strangles, iron condors, credit spreads): you are being paid richly to take on movement risk, and you profit if that rich IV deflates.
- **Low IV rank (say below 20–30)** — options are *cheap*. Premiums are thin. This favours **buying** options or using structures that are long vega (long calls/puts, debit spreads, calendars): you are buying movement on the cheap, and you profit if IV expands.

The professional discipline is **"sell high IV, buy low IV."** Combine the two sub-questions and you avoid the classic beginner trap: buying a straddle into an event when IV is already sky-high (you pay a fortune for movement, then watch IV collapse after the event even though the index moved — the dreaded *IV crush*).

### Question 3 — defined risk or undefined risk, and how much?

This is the axis that keeps you alive. Two parts again.

**(a) Defined vs undefined risk.** Every structure is one or the other:

- **Defined-risk** — your maximum loss is known and capped the moment you enter. Long options, all vertical spreads (bull call, bear put, bull put, bear call), iron condors, iron butterflies, and long butterflies are defined-risk. The market can gap 10% overnight and you cannot lose a rupee more than you committed.
- **Undefined-risk** — your loss can balloon far beyond what you collected. Naked short calls (theoretically unlimited loss), naked short puts, and short straddles/strangles are undefined-risk. They often have a *high probability* of a *small* profit, paired with a small probability of a *large* loss — and in India, SPAN + exposure margin on these is heavy, and a gap move can blow through your stop before you can act.

For beginners, defined-risk should be the default, not the exception. You will be wrong often while you learn; defined-risk guarantees that being wrong is survivable. Undefined-risk selling is a professional tool that demands strict position sizing, hedging, and the emotional discipline to take a loss — earn your way to it.

**(b) How much can this trade lose?** Even a defined-risk trade is dangerous if it is too big. A workable rule for a learning trader: **risk no more than 1–2% of total capital on any single trade.** If your account is ₹5,00,000, that is ₹5,000–₹10,000 of maximum loss per position. This number *drives the structure and the number of lots* — it is not an afterthought.

### Probability of profit vs payoff size — the eternal trade-off

Two structures can have the same expected value yet feel completely different, because they sit at opposite ends of one trade-off:

- **Buying options** (long calls/puts, debit spreads, long straddles) — *low* probability of profit, *large* payoff when right. You will lose small amounts often (long options usually expire worthless) and win big occasionally. You need to be right about *timing and magnitude*, not just direction.
- **Selling options** (credit spreads, condors, short strangles) — *high* probability of profit, *small* capped payoff, with a fat tail of large loss if you are wrong. You win small amounts often and lose big occasionally.

Neither is "better." A high probability of profit is seductive — winning 80% of the time *feels* like skill — but if the 20% losses are 5x the size of the wins, you bleed out. Always ask: **probability of profit times average win, versus probability of loss times average loss.** The market roughly prices these to balance; your edge comes from a *view* (on direction or volatility) that the market has mispriced, not from the structure itself.

### Position sizing is part of strategy selection, not a separate step

Choosing *which* structure and choosing *how many lots* are the same decision. The flow is:

1. Pick the structure from your three views (the table below).
2. Compute the **maximum loss per lot** of that structure.
3. Divide your **rupee risk budget** (1–2% of capital) by that per-lot loss to get the number of lots.

`Number of lots = (capital * risk % per trade) / (max loss per lot)`

If the answer is less than one lot, the trade is too big for your account — pick a tighter (cheaper) structure or skip it. This is why a defined-risk spread often beats a naked long option for a small account: the capped loss makes the position *sizeable* in a controlled way, instead of forcing you to bet the whole premium and hope.

### The master decision map

Here is the table that ties all three axes together. Read it as: *given my directional view, my volatility view, and my IV-rank/risk preference, here is the strategy family.* Defined-risk choices are marked so beginners know where to start.

| Directional view | Volatility view (and IV rank) | Strategy family | Risk type |
|---|---|---|---|
| Bullish | Expect big move up / IV low (cheap) | Long call, **bull call spread** | Defined |
| Bullish | Expect drift up / IV high (rich) | **Bull put spread** (sell put credit) | Defined |
| Bullish | Mildly bullish, want income | Covered call, short put | Undefined (put) |
| Bearish | Expect big move down / IV low | Long put, **bear put spread** | Defined |
| Bearish | Expect drift down / IV high | **Bear call spread** (sell call credit) | Defined |
| Neutral (range) | IV high (rich), expect calm | Short strangle, **iron condor** | Condor: Defined |
| Neutral (pin to a level) | IV high, expect a precise sit | **Iron butterfly**, short straddle | Iron fly: Defined |
| Neutral (range) | IV low (cheap), expect IV to rise | Calendar / diagonal spread | Defined-ish |
| Neutral (pin to a level) | IV low, low movement expected | **Long butterfly** | Defined |
| Unsure on direction | Expect big move / IV low | **Long straddle** (ATM), **long strangle** (OTM) | Defined |
| Unsure on direction | Expect calm / IV high | Short straddle / short strangle | Undefined |
| Strongly directional + hedge | Own stock/position, want protection | Protective put, collar | Defined |

The bolded, defined-risk cells are your starting playground. Everything in the rest of Part VI is one row of this table explained in full.

### A simple checklist before every trade

1. **Direction:** up / down / sideways / unsure?
2. **Volatility:** rising or falling? And is IV rank high (sell) or low (buy)?
3. **Risk:** defined (default) or undefined? Max rupee loss = 1–2% of capital.
4. **Structure:** read it off the map.
5. **Size:** lots = risk budget / max loss per lot.
6. **Exit plan:** at what profit or loss do I get out, before I enter?

If you cannot fill in all six lines, you do not have a trade — you have a hunch.

## Worked example (₹, Nifty/Bank Nifty)

It is a quiet week. Nifty is at **24,000**. You have a **mildly bullish** view — you think Nifty drifts up to around 24,300 over the next week, but you do not expect fireworks. You check **India VIX and IV rank**: VIX is elevated and the weekly options carry an **IV rank of about 70** (rich). Your account is **₹5,00,000** and your rule is to risk **2% (₹10,000)** per trade. Nifty lot size is **75**.

**Step 1 — run the three questions.**
- *Direction:* mildly bullish (drift up, not explosive). 
- *Volatility:* IV rank 70 is high — options are expensive, so you want to be a *seller*, not a buyer. You also expect calm, so falling IV would help you. 
- *Risk:* you want defined risk; max loss ₹10,000.

**Step 2 — read the map.** Bullish + high IV (rich) + defined risk points to a **bull put spread** (sell a put credit spread below the market). You collect rich premium, you profit if Nifty stays above your short strike, and rich IV deflating helps you. A long call would be the *wrong* choice here — you would be *buying* expensive premium against your own volatility view and exposing yourself to IV crush.

**Step 3 — build the structure.** Sell the 23,900 put and buy the 23,700 put (a 200-point-wide spread, both below the current 24,000):
- Sell 23,900 put: collect about **₹120** per unit.
- Buy 23,700 put: pay about **₹60** per unit.
- **Net credit = 120 - 60 = ₹60** per unit.

**Step 4 — compute per-lot economics.**
- Net credit per lot = `60 * 75 = ₹4,500` (your maximum profit per lot).
- Spread width = `23,900 - 23,700 = 200` points.
- Max loss per unit = `width - net credit = 200 - 60 = ₹140`.
- Max loss per lot = `140 * 75 = ₹10,500`.

**Step 5 — size the position.**
`Lots = risk budget / max loss per lot = 10,000 / 10,500 = 0.95`, which rounds down to **1 lot**. One lot fits inside your ₹10,000 risk budget (just); two lots would risk ₹21,000 and break your rule, so you trade exactly **one lot**.

**Step 6 — define the outcomes.**
- *Breakeven:* `23,900 - 60 = 23,840`. As long as Nifty expires above 23,840, you make money.
- *Max profit:* ₹4,500, if Nifty expires anywhere above 23,900 (your mild bullishness only needs Nifty to *not fall* much).
- *Max loss:* ₹10,500, if Nifty collapses below 23,700.
- *Probability:* because both strikes are below the current price, this trade has a *high* probability of the small ₹4,500 win — exactly the high-POP, capped-payoff profile of premium selling, kept survivable by the defined-risk wings.

The whole trade was *selected*, not guessed: three views in, one structure and one lot out.

## Common mistakes / risk note

- **Starting from the strategy, not the view.** "I like iron condors" is not a reason to sell an iron condor. If your three answers don't point to it, don't trade it.
- **Ignoring the volatility axis entirely.** Buying a straddle before results when IV rank is 90 is a classic loss: the index can move and you *still* lose because IV crushes after the event. Buy cheap vol, sell rich vol.
- **Confusing high probability of profit with low risk.** Naked short options win most days, then hand back months of gains in one gap. A high POP with undefined risk is *more* dangerous to a beginner, not less.
- **Treating position sizing as optional.** Picking the right structure and then trading 5 lots when 1 fits your budget converts a good trade into a blow-up. Sizing is part of selection.
- **Defaulting to undefined-risk selling too early.** SEBI studies are blunt: roughly nine in ten retail F&O traders lose money, and undefined-risk selling is where the biggest single-day wipeouts happen. Earn your way to it with defined-risk structures first.
- **No pre-planned exit.** Decide your profit-take and stop-loss *before* entering, while you are calm. After entry, your judgement is compromised by the position.

## Key takeaways

- Every options trade should answer three questions in order: **direction, volatility, risk** — and only then name a strategy.
- The volatility question has two halves: *which way will IV move* and *is IV cheap or rich right now* (use IV rank). Sell rich vol, buy cheap vol.
- **Defined-risk structures are the correct default for beginners** — they make being wrong survivable.
- Buying options gives low probability / large payoff; selling options gives high probability / small payoff with a fat loss tail. Neither is free money — your edge is a *view*, not a structure.
- **Position sizing is part of strategy selection:** `lots = (capital * risk%) / (max loss per lot)`. If that is under one lot, the trade is too big.
- The master decision map turns the three views into a strategy family; the rest of Part VI explains each cell in detail.

## Practice problems

1. **(Conceptual)** A trader is bearish on Bank Nifty and notices IV rank is 75 (very rich). Using the framework, which is more appropriate: buying a put, or selling a bear call (call credit) spread? Explain via the volatility axis.

2. **(Conceptual)** Explain why a long straddle bought the morning of an RBI policy announcement, when IV rank is 90, can lose money *even if* Nifty moves 300 points that day.

3. **(Numeric — sizing)** Your capital is ₹3,00,000 and your rule is 1.5% risk per trade. You want a Nifty bull call spread whose maximum loss is ₹3,400 per lot. How many lots can you trade?

4. **(Numeric — structure economics)** You sell a Nifty bear call spread: sell the 24,200 call for ₹90 and buy the 24,400 call for ₹40 (lot size 75). Compute net credit per lot, max loss per lot, and the breakeven level.

5. **(Conceptual)** A beginner says: "Short strangles win 85% of the time, so they're the safest way to trade." Identify the flaw using the probability-of-profit vs payoff-size idea.

6. **(Application)** You are neutral on Nifty (expect it to stay near 24,000 for a week) and IV rank is only 15 (cheap). Which two families from the decision map fit, and which one is defined-risk and beginner-appropriate?

## Solutions

1. **Sell the bear call spread.** With IV rank at 75, options are *expensive*. Buying a put means *paying* that rich premium and fighting IV crush — your volatility view (rich IV likely to fall) is working against a long option. A bear call credit spread is a *seller* of that rich premium: you profit from the bearish drift *and* from IV deflating, and the long wing caps your risk. Direction (bearish) is satisfied by both, but the volatility axis breaks the tie in favour of selling.

2. **IV crush.** At IV rank 90 the straddle is priced for a *huge* expected move; you pay a very fat premium. Once the announcement passes, uncertainty collapses and IV falls sharply, deflating both legs' time value. A 300-point move might be *less* than the move the inflated premium required to break even, and the vega loss from collapsing IV can exceed the gamma/intrinsic gain. You were right that it would move, but you overpaid for the movement — the wrong side of the "buy cheap vol" rule.

3. **Risk budget = `3,00,000 * 0.015 = ₹4,500`.** `Lots = 4,500 / 3,400 = 1.32`, round down to **1 lot.** Two lots would risk ₹6,800 and exceed the ₹4,500 budget, so you trade one lot.

4. **Bear call spread economics.**
   - Net credit per unit = `90 - 40 = ₹50`; per lot = `50 * 75 = ₹3,750` (max profit).
   - Spread width = `24,400 - 24,200 = 200` points; max loss per unit = `200 - 50 = ₹150`; per lot = `150 * 75 = ₹11,250` (max loss).
   - Breakeven = short strike + net credit = `24,200 + 50 = 24,250`. You profit if Nifty expires below 24,250; max profit below 24,200; max loss above 24,400.

5. **The flaw is ignoring payoff size and risk type.** An 85% win rate sounds safe, but a short strangle is *undefined-risk*: the 15% of losing trades can each lose many times the small premium collected. Compare expected values: if you win ₹4,000 with 85% probability but lose ₹30,000 with 15% probability, expected value = `0.85*4,000 - 0.15*30,000 = 3,400 - 4,500 = -₹1,100` — a losing strategy despite the high win rate. "Wins often" is not "safe"; a high probability of profit paired with a fat loss tail is exactly how beginners blow up.

6. **Neutral + low IV (cheap) fits the calendar/diagonal spread and the long butterfly.** Both want a quiet, range-bound market and benefit from cheap premium / rising IV. The **long butterfly** is the cleanly **defined-risk, beginner-appropriate** choice: you buy it for a small known debit, your maximum loss is that debit, and it pays off best if Nifty pins near the body strike (24,000). The calendar is also broadly defined-risk but is more sensitive to IV changes and trickier to manage, so the long butterfly is the better starting point.
