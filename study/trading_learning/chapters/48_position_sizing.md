# Chapter 48: Position Sizing & the 1-2% Risk Rule

Imagine two traders sit down with the same ₹2,00,000 and the same strategy — a strategy that genuinely wins six times out of ten. The first trader bets a quarter of his account on every idea because he is "confident." The second trader risks two thousand rupees per trade, win or lose, no matter how good the setup looks. Fast-forward three months. The confident trader is broke, blown up by an unlucky cluster of losses that any honest strategy throws out from time to time. The careful trader is still in the game, slowly compounding. Same edge, same market, opposite outcomes. The only difference was **position sizing** — how much capital each one put at risk on a single trade.

This is the most under-glamorised survival skill in all of trading. Picking the right strike, reading volatility, nailing direction — all of it is worthless if a single bad trade or a short losing streak can end your career. Position sizing converts a good strategy into a long career, and it is the precise reason most famous F&O blow-up stories are not about being wrong, but about being **too big when wrong**. This chapter teaches the one rule professionals never break: risk only a small, fixed fraction of your capital — usually 1% to 2% — on any single trade.

## Core concepts

### The single rule: risk a fixed fraction, not a fixed feeling

The rule is deliberately mechanical so that your emotions never get a vote. On every trade you decide, before you enter, the maximum number of rupees you are willing to lose if the trade goes completely against you. That number — your **risk per trade** — is a fixed small percentage of your **trading capital** (the money in your F&O account that you are willing to deploy).

- At **1% risk** on a ₹2,00,000 account, you risk **₹2,000** per trade.
- At **2% risk** on the same account, you risk **₹4,000** per trade.

Notice what this number is *not*. It is **not** the premium you pay, it is **not** the margin SEBI blocks, and it is **not** the notional value of the contract. It is the amount you actually expect to lose in the bad scenario. Everything in position sizing flows from one formula:

`Number of lots = Risk per trade / (Max loss per lot)`

Your job on every trade is to (a) fix the risk per trade as a small percentage of capital, (b) figure out the max loss per lot of the position, and (c) divide. The answer tells you how big you are allowed to be. If the answer is "zero lots," the honest response is to not take the trade, not to round up to one.

### Why a *fraction*, and why so small

A beginner's instinct is that 1-2% is absurdly timid. If you are sure, why not bet 20%? The answer is that you are never as sure as you feel, and trading is a game played thousands of times. The right question is never "how much can I make on this trade?" It is "what sequence of trades can the market throw at me, and will I still be standing at the end of it?"

Small fractions keep you standing because **no single trade can hurt you**. At 2% risk, ten losses in a row — a brutal, rare streak — costs you roughly 20% of capital. Painful, but survivable; you can earn it back. At 25% risk, four losses in a row and you are essentially done. Since any real strategy *will* eventually produce a losing streak, the only thing you control is whether that streak is a flesh wound or a funeral.

### Translating risk into option lots using MAX LOSS

The mechanical heart of sizing is identifying the **max loss** of your position — the worst rupee outcome — because that is the number you divide your risk budget by. There are two cases.

**Defined-risk trades — max loss is known in advance.** Any position where your worst case is mathematically capped:

- A **long option** (buy a call or put). The most you can lose is the premium paid. Max loss per lot = `premium * lot size`.
- A **debit spread** (e.g. a bull call spread). Max loss = net debit paid. Max loss per lot = `net debit * lot size`.
- A **credit spread, iron condor, or iron butterfly**. Max loss = (width of the widest spread minus net credit received). Max loss per lot = `(width - credit) * lot size`.

For these, sizing is clean and exact, because the broker and the math agree on the worst case. This is the single biggest reason beginners should prefer defined-risk structures: you can size them honestly.

**Undefined-risk trades — you must impose a max loss with a stop or a worst-case scenario.** A naked short option or a short straddle has, in theory, unlimited or very large loss. You cannot divide by infinity, so you must *manufacture* a max loss in one of two ways:

1. **A stop-loss rule.** Decide in advance: "I exit if the position's loss hits 2x the credit received," or "I exit if Nifty touches my short strike." That exit level defines your planned max loss per lot, and you size to it. The honest caveat: a stop is a *plan*, not a *guarantee*. A gap opening — Nifty jumping 600 points overnight on global news — can blow straight through your stop. So your stop-based size should still leave room for a gap.
2. **A worst-case (stress) scenario.** Estimate the loss if the market makes a large adverse move — say a 4-5% gap on the index, or India VIX doubling — and treat that as your max loss. This is more conservative and is how professionals size short-premium tail risk (covered below).

The practical rule of thumb: for undefined-risk trades, size off the **stress scenario**, not the comfortable stop, because the stop is exactly what fails on the day that matters.

### The mathematics of ruin: why oversizing kills even a good strategy

Here is the uncomfortable truth that position sizing exists to defend against. **A positive edge does not protect you from ruin if you bet too big.** Edge tells you the long-run average; sizing tells you whether you survive long enough to collect it.

Think of your account as needing to survive a *sequence*. The probability of an eventual catastrophic drawdown rises sharply as bet size rises, even when each individual bet has positive expectancy. Two forces are at work.

**Force one — losing streaks are normal, not freak events.** A strategy that wins 60% of the time still loses 40% of the time, and losses cluster. The chance of seeing a run of *k* consecutive losses over a long career is high. With a 40% loss rate, a string of 5 straight losses has roughly a `0.4^5 = ~1%` chance on any given starting trade — which sounds tiny until you realise you take hundreds of trades a year, so such streaks are essentially guaranteed to occur. You must be sized to survive them as routine weather, not as a once-in-a-lifetime storm.

**Force two — the asymmetry of drawdowns.** To recover a loss you need a *larger* percentage gain than the percentage you lost, because you now compound from a smaller base:

`Gain needed to recover = L / (1 - L)`

where L is the fractional loss. The numbers are sobering:

- Lose **10%**, you need **+11.1%** to get back to even.
- Lose **25%**, you need **+33.3%**.
- Lose **50%**, you need **+100%** — your money must *double* just to undo it.
- Lose **75%**, you need **+300%**.

This is why deep drawdowns are so dangerous: they don't just cost money, they bend the recovery curve against you. A 50% account loss means your strategy, which might earn 20% a year, now needs five years of perfect compounding just to break even. Small position sizes keep your drawdowns shallow enough that the recovery is realistic.

### Kelly criterion intuition — and why pros bet a fraction of it

There is a famous formula, the **Kelly criterion**, that gives the bet size which maximises the long-run growth rate of your capital:

`Kelly fraction f = W - (1 - W) / R`

where `W` is your win probability and `R` is your win/loss ratio (average win / average loss). If you win 55% of the time (W = 0.55) with average win equal to average loss (R = 1), then `f = 0.55 - 0.45/1 = 0.10` — Kelly says bet 10% of capital per trade.

Kelly is mathematically optimal for growth, but in real trading **almost no professional bets full Kelly**, and you should not either. Three reasons:

1. **Your inputs are estimates, not facts.** W and R come from a finite, noisy track record. If you overestimate your edge even slightly, full Kelly overbets massively and the growth-optimal bet becomes a ruin-inducing bet.
2. **Full Kelly is a wild ride.** Even with perfect inputs, full Kelly routinely produces 50%+ drawdowns. Mathematically optimal, psychologically unbearable — and a drawdown you abandon is not optimal at all.
3. **Markets are not coin flips.** Volatility regimes shift, correlations break, and tail events arrive unannounced. The fixed odds Kelly assumes simply don't hold.

So pros bet a **fraction of Kelly** — typically **one-quarter to one-half**. Half-Kelly captures about three-quarters of the growth rate with roughly half the volatility; quarter-Kelly is gentler still. And here is the punchline that ties the chapter together: for most realistic retail edges, **a quarter or half of Kelly lands you right back in the 1-2% per-trade neighbourhood.** The simple fixed-fraction rule isn't a beginner's crutch — it's where the rigorous math sends you too.

### Scaling in and scaling out

You do not have to commit your full position size in one click. **Scaling** spreads entries and exits across price or time, and it interacts directly with sizing.

- **Scaling in** means building the position in tranches — for example, putting on one-third of your intended lots now and adding the rest if the trade moves your way or reaches a better price. The discipline rule: your **total planned size across all tranches** must still respect the 1-2% max-loss limit. Scaling in is a way to *average into* your full size, not a licence to exceed it.
- **Scaling out** means taking profits (or cutting risk) in pieces — closing half the lots at a +50% gain on the premium, letting the rest run, or rolling untested legs. Scaling out reduces your risk on the table as the trade matures, which is exactly the right direction to move.

The trap to avoid is **averaging down into a loser** — adding lots to a position that is going against you to lower your average cost. This silently breaks your sizing rule: each add increases your max loss, so a trade you sized at 2% quietly becomes a 4% or 6% trade precisely when it is hurting you. That is how disciplined-looking traders blow up.

### Sizing for tail risk on short-premium trades

Short-premium trades — selling straddles, strangles, naked options, even iron condors — make money most days and lose money on a few violent ones. The whole risk lives in the tail, so **you must size off the tail, not off the average day.**

1. **Size off a stress move, not the current calm.** When India VIX is low (say 11-12), premiums are thin and it is tempting to sell large because "nothing ever happens." That is exactly when a 4-5% gap is most punishing relative to the credit collected. Ask: "If Nifty gaps 5% against me and VIX doubles overnight, what is my loss?" Size so that even *that* number is a survivable fraction of capital — many pros cap the stress-scenario loss at 3-5% of capital, above the normal 1-2% planned risk, precisely to leave a buffer for the gap.
2. **Respect aggregate and correlated risk.** Five separate Nifty short strangles are not five independent 2% trades — on a crash day they all lose together, so your real risk is closer to 10% in one shot. Budget risk across the whole book, and assume index positions are highly correlated in a sell-off.

## Worked example (₹, Nifty)

You have a **₹2,00,000** trading account and you run two trades. Assume a Nifty **lot size of 75** (it changes over time — check the current NSE contract spec; the method is identical whatever the number).

**Trade A — a defined-risk bull call spread (1% risk).**

Nifty spot is at 24,000. You are mildly bullish into weekly expiry and buy a bull call spread:

- Buy 24,000 call at ₹150
- Sell 24,200 call at ₹70
- Net debit = `150 - 70 = ₹80` per share

Max loss per lot = `net debit * lot size = 80 * 75 = ₹6,000`. This is fully defined — you cannot lose more than the debit.

Risk budget at 1% = `0.01 * 2,00,000 = ₹2,000`.

`Lots = Risk budget / Max loss per lot = 2,000 / 6,000 = 0.33`.

That rounds down to **zero lots** — one lot would risk ₹6,000 (3% of capital), which breaks the rule. The honest choices are: (a) move to 2% risk, giving `4,000 / 6,000 = 0.66`, still under one lot, so still **don't trade it**; or (b) **narrow the spread** to cut max loss. If you instead sell the 24,100 call and the net debit drops so that max loss per lot is ₹3,000, then at 2% risk `4,000 / 3,000 = 1.33`, i.e. **1 lot** fits cleanly. The sizing math is *telling you* that on a ₹2,00,000 account, a single Nifty spread is often already near your risk ceiling — which is the reality check most beginners ignore.

**Trade B — an undefined-risk short straddle (2% risk, sized off a stop).**

Nifty at 24,000, you sell the weekly at-the-money straddle:

- Sell 24,000 call at ₹130
- Sell 24,000 put at ₹120
- Total credit = `130 + 120 = ₹250` per share = `250 * 75 = ₹18,750` per lot

Max loss is theoretically huge, so you impose a rule: **exit if the position's loss reaches 1.5x the credit.** Planned max loss per lot = `1.5 * 18,750 = ₹28,125`.

Risk budget at 2% = `0.02 * 2,00,000 = ₹4,000`.

`Lots = 4,000 / 28,125 = 0.14` → **zero lots.** The straddle is simply too big for this account under an honest stop. Even at the full 2%, one lot's planned loss is 14% of your capital — and that is *before* a gap blows through the stop. The correct conclusion is not "ignore the rule for this one." It is that a ₹2,00,000 account has no business selling a naked Nifty straddle; the defined-risk version (an iron butterfly, with bought wings capping the loss) is the only responsible way to express the same view at this account size.

**The lesson the arithmetic forces on you:** with ₹2,00,000, you are a one-or-two-lot defined-risk trader, full stop. The rule doesn't just size your trades — it tells you which trades you are allowed to take at all.

## Common mistakes / risk note

- **Sizing off margin instead of max loss.** Your broker blocks SPAN+exposure margin to *hold* the trade; that is a liquidity requirement, not your risk. A trade can require ₹1,50,000 of margin and still only risk ₹4,000 — or require ₹1,50,000 and risk ₹50,000. Always size off max loss.
- **Treating the premium received as the risk on short options.** Selling a put for ₹120 does not mean you risk ₹120. You collect ₹120 and risk far more. Sellers must size off the loss, never the credit.
- **Letting a "high-conviction" trade override the rule.** The trades you are most sure about are not safer — your confidence has no effect on the market. Position sizing must be conviction-blind, or it isn't a rule.
- **Averaging down.** Adding to losers silently multiplies your max loss past the limit. If a trade is wrong, the rule already accounted for that loss; doubling it is a fresh, larger, unplanned bet.
- **Counting correlated index trades as independent.** Multiple Nifty/Bank Nifty short positions all bleed together on a crash. Budget risk across the whole book.
- **Trusting stops on undefined-risk trades.** Stops fail on gaps — the one scenario that produces the catastrophic loss. Size short premium off a stress move, with a buffer.
- **The honest backdrop.** SEBI studies show roughly nine in ten retail F&O traders lose money, and the losers are disproportionately the over-sized ones. Correct sizing won't manufacture an edge you don't have — but incorrect sizing will reliably destroy an edge you do have.

## Key takeaways

- Risk a small, **fixed fraction** of capital — **1% to 2%** — on every single trade, decided before you enter and immune to how good the setup feels.
- `Lots = Risk per trade / Max loss per lot.` Size off **max loss**, never premium, margin, or notional.
- For **defined-risk** trades, max loss is known exactly. For **undefined-risk** trades, manufacture a max loss from a **stop or, better, a stress scenario** — and assume the stop fails on a gap.
- **Ruin math is unforgiving:** losing streaks are routine, and drawdowns are asymmetric — a 50% loss needs a 100% gain to recover. Small size keeps drawdowns shallow enough to come back from.
- **Kelly** gives the growth-optimal bet, but pros bet a **quarter to a half of it** because inputs are noisy and full Kelly is unbearable — which lands right back at 1-2%.
- **Scale in** toward your full size and **scale out** to reduce risk; never **average down** into a loser.
- On a ₹2,00,000 account you are realistically a **one-to-two-lot, defined-risk** trader — the math itself tells you which trades you may take.

## Practice problems

1. **(Conceptual)** A trader says, "I only risk 2%, so I'm safe — I bought 5 Nifty weekly out-of-the-money calls for ₹3,000 total premium." What two things might be wrong with calling this a single 2% trade on a ₹2,00,000 account? (Consider both the sizing and the correlation.)

2. **(Numeric — defined risk)** Account = ₹3,00,000, risk per trade = 1.5%. You trade a Bank Nifty bear put spread with a net debit of ₹100 per share; lot size = 15. What is your max loss per lot, your risk budget, and how many lots may you take?

3. **(Numeric — drawdown asymmetry)** A trader loses 40% of his account in a bad month. What percentage gain on the reduced balance does he need to get back to even? If his strategy earns about 18% a year, roughly how many years of compounding is that?

4. **(Numeric — credit spread)** Account = ₹2,00,000, risk per trade = 2%. You sell a Nifty iron condor: the call spread and put spread are each 100 points wide, and you collect a net credit of ₹40 per share. Lot size = 75. Find the max loss per lot and the number of lots allowed.

5. **(Conceptual — Kelly)** Your records show a win rate of 50% with average wins equal to twice your average losses (R = 2). Compute the full-Kelly fraction. Why would you trade at, say, one-quarter of it, and what per-trade risk does that imply?

6. **(Numeric — undefined risk / stress)** Account = ₹5,00,000. You want to sell one lot of a naked Nifty strangle for a total credit of ₹150 per share (lot size 75). You estimate that in a 5% adverse gap with VIX spiking, the position loses about ₹90,000. Express that loss as a percentage of capital. Under a "stress loss must stay under 5% of capital" rule, may you take the trade?

## Solutions

**1.** First, **sizing by premium is not the same as sizing by risk for a portfolio of longs, but here the issue is concentration and correlation.** ₹3,000 is indeed the max loss (long calls can only lose the premium), so 1.5% of capital is genuinely at risk — that part is fine. The two problems are: (a) all five calls are the *same underlying, same direction, same expiry*, so they are one concentrated bet, not five diversified ones — if Nifty doesn't rally, all ₹3,000 is gone together, and out-of-the-money weekly calls very often expire worthless; and (b) if this is one of several simultaneous bullish Nifty positions, the *aggregate* directional risk across the book can far exceed 2%. The 2% label is only meaningful trade-by-trade *and* in aggregate.

**2.** Max loss per lot = `net debit * lot size = 100 * 15 = ₹1,500`. Risk budget = `0.015 * 3,00,000 = ₹4,500`. Lots = `4,500 / 1,500 = 3 lots`. Clean fit — you may take **3 lots**, risking exactly 1.5%.

**3.** Gain needed = `L / (1 - L) = 0.40 / 0.60 = 0.667 = +66.7%` on the reduced balance. At ~18% per year, the number of years to grow 66.7% is found from `1.18^n = 1.667`, so `n = ln(1.667) / ln(1.18) = 0.511 / 0.166 ≈ 3.1 years`. A single 40% drawdown costs over three years of compounding just to recover — the core argument for small size.

**4.** For an iron condor, max loss = `(spread width - net credit) * lot size = (100 - 40) * 75 = 60 * 75 = ₹4,500` per lot. Risk budget = `0.02 * 2,00,000 = ₹4,000`. Lots = `4,000 / 4,500 = 0.89` → rounds down to **zero lots.** One lot would risk ₹4,500 = 2.25% of capital, just over the limit. You either accept a slightly-over-2% single lot as a deliberate exception (not ideal), widen the credit, or pass. The math says one Nifty iron condor is right at the ceiling of a ₹2,00,000 account.

**5.** Full Kelly: `f = W - (1 - W)/R = 0.50 - 0.50/2 = 0.50 - 0.25 = 0.25`, i.e. 25% of capital per trade. You trade a fraction of it because: the 50%/R=2 inputs are noisy estimates and overbetting on an overestimated edge courts ruin; full Kelly produces gut-wrenching 50%+ drawdowns; and markets aren't fixed-odds bets. Quarter-Kelly = `0.25 * 0.25 = 0.0625`, about 6% per trade — still aggressive for options, which is why real traders pull it down further toward the 1-2% zone once they account for gap risk and correlation. The lesson: Kelly sets a *ceiling*, prudence sets the *working number*.

**6.** Stress loss as a percentage of capital = `90,000 / 5,00,000 = 0.18 = 18%`. Under a "stress loss under 5% of capital" rule, **18% fails badly** — you may *not* take even one lot. To get the stress loss under `0.05 * 5,00,000 = ₹25,000`, you would need a structure whose worst-case gap loss is roughly a quarter of this naked strangle's — i.e. buy protective wings (turning it into an iron condor/butterfly) or trade a much smaller notional. This is the tail-risk discipline: the calm-day credit of ₹150 is irrelevant; the gap day decides your size.
