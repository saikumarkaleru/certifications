# R-Multiple & Expectancy (Deep)

Most Indian retail traders talk about their trades in rupees — "I made ₹8,000 today, I lost ₹15,000 yesterday." That vocabulary is the reason most of them never improve. Rupees mix together three completely different things: how good your edge is, how big you bet, and how lucky you got. R-multiples separate them. This chapter builds the R-multiple language from the ground up, derives expectancy honestly, and shows you how to use both to answer the only question that matters: *does this system make money over 500 trades, and how much per rupee risked?*

## What R Is, and Why It Changes Everything

**R is your initial risk on a trade, in rupees.** It is defined at the moment of entry and never changes afterward. If you buy Reliance at ₹1,420 with a stop at ₹1,400, your R is ₹20 per share. If you hold 500 shares, your R is ₹10,000 for the position. That ₹10,000 is one unit of risk — one "R."

Every outcome of the trade is then measured *in multiples of that initial R*, not in rupees:

- Stop hit at ₹1,400 → you lost 1R (−1R).
- Exit at ₹1,460 → you made ₹40/share = 2R (+2R).
- Exit at ₹1,410 → +0.5R.
- Gap down, exit at ₹1,385 → −1.75R (slippage made your loss bigger than planned).

The power of this is that **it normalises every trade to the same scale regardless of instrument, position size, or price.** A +2R on a ₹90 PSU bank stock and a +2R on a ₹3,500 Bajaj Finance trade are the *same result* in the language that matters. You risked one unit and made two. This lets you pool trades across Nifty options, Bank Nifty futures, cash equity, and MCX crude into a single distribution and study your actual edge.

Rupee-thinking cannot do this. A trader who makes ₹2,000 on a tiny position and loses ₹2,000 on a huge position feels "break-even" but has actually been bleeding edge. R-thinking exposes it instantly: +0.2R and −3R is a disaster disguised as a wash.

### The discipline R forces on you

You cannot compute R unless you define a stop *before* entry. This is the hidden gift. The moment you commit to R-multiple bookkeeping, you can no longer take a trade without knowing where you're wrong. The "I'll watch it and decide" trade has no R, and a trade with no R cannot be logged, cannot be measured, and — in a disciplined process — cannot be taken.

## Constructing R Correctly

R is `|Entry − Initial Stop| × Quantity`. Three rules keep it honest:

**1. Use the *initial* stop, not the trailed stop.** If you enter Bank Nifty long at 51,200 with a stop at 51,000 (R = 200 points), and later trail the stop to 51,400, your R is still 200 points. If price then reverses and you exit at 51,400 for +200 points, that is **+1R**, not "a small win." The trail protected profit; it did not change the risk you originally took. Recomputing R off the trailed stop is the single most common way traders flatter their own statistics.

**2. R is fixed at entry; realised loss can exceed 1R.** Gaps, slippage, and illiquid options mean your actual loss is sometimes −1.3R or −2R. **Log the real number.** A system that "risks 1R" but averages −1.4R on losers because of overnight gaps in stock F&O has a real expectancy far worse than its theoretical one. Honest R-multiple logging is where slippage stops being invisible.

**3. Convert everything to R at the trade level, then forget the rupees.** Your journal's outcome column should be a pure number: −1, +2.3, −0.4, +5.1, −1, −1, +0.8. That column is your edge, stripped of bet-sizing noise.

### A worked R table — one week of Nifty/Bank Nifty trades

| # | Instrument | Entry | Init. Stop | R (pts/₹) | Exit | Result (pts) | R-multiple |
|---|-----------|-------|-----------|-----------|------|-------------|-----------|
| 1 | Nifty fut long | 24,180 | 24,130 | 50 | 24,265 | +85 | +1.70R |
| 2 | Bank Nifty fut short | 51,600 | 51,720 | 120 | 51,750 | −150 | −1.25R |
| 3 | Reliance long | 1,420 | 1,400 | 20 | 1,412 | −8 | −0.40R |
| 4 | Nifty 24,200 CE | ₹95 | ₹70 | 25 | ₹70 | −25 | −1.00R |
| 5 | Bank Nifty fut long | 51,300 | 51,180 | 120 | 51,640 | +340 | +2.83R |
| 6 | Fin Nifty short | 23,400 | 23,470 | 70 | 23,410 | −10 | −0.14R |
| 7 | HDFC Bank long | 1,690 | 1,672 | 18 | 1,672 | −18 | −1.00R |
| 8 | Nifty fut long | 24,050 | 24,000 | 50 | 24,190 | +140 | +2.80R |

Notice trade 2: the stop was 120 points but the exit was −150, a −1.25R loss. That is a real gap/slippage event, and logging it as "−1R" would have quietly lied. Notice trade 6, cut early for −0.14R — a discretionary bail-out that is neither a full loss nor a win. These fractional results are where most of a discretionary trader's true behaviour lives, and only R-multiples reveal them.

The R column for this week: **+1.70, −1.25, −0.40, −1.00, +2.83, −0.14, −1.00, +2.80.**

## Expectancy: The Number That Decides Everything

Expectancy is the **average R-multiple per trade**. It answers: *for every 1R I risk, how much do I make (or lose) on average, over many trades?*

Sum the R-multiples above: 1.70 − 1.25 − 0.40 − 1.00 + 2.83 − 0.14 − 1.00 + 2.80 = **+3.54R** over 8 trades.

Expectancy = 3.54 / 8 = **+0.44R per trade.**

That single number is the heartbeat of your trading. It says: *on average, this trader nets 0.44 units of risk per trade.* If you risk ₹10,000 per trade, your mathematical expectation is ₹4,400 per trade before costs — over a large sample.

### The formula, and why win rate is a trap

The clean expectancy formula:

**Expectancy = (Win% × Average Win in R) − (Loss% × Average Loss in R)**

For a system with 40% win rate, average winner +2.5R, average loser −1R:

Expectancy = (0.40 × 2.5) − (0.60 × 1.0) = 1.00 − 0.60 = **+0.40R.**

This is the most liberating equation in trading. **A system that loses 60% of the time is highly profitable** because its winners are 2.5× its losers. Indian retail traders obsess over win rate — "my strategy has 80% accuracy!" — and it is almost always a trap. An 80%-accurate system that makes +0.3R on winners and loses −2R on losers (the classic option-selling-without-stops profile) has:

Expectancy = (0.80 × 0.3) − (0.20 × 2.0) = 0.24 − 0.40 = **−0.16R.**

Eighty percent right, and it bleeds. This is *exactly* how naked option sellers on Bank Nifty blow up: months of small +0.3R wins, then one expiry-day spike takes −6R and erases a quarter. High win rate with a fat left tail is negative expectancy wearing a confidence mask.

Conversely, a trend-following breakout system on Nifty stocks might win 35% of the time and feel awful — five losers for every three winners — yet:

Expectancy = (0.35 × 3.2) − (0.65 × 1.0) = 1.12 − 0.65 = **+0.47R.** Excellent.

The lesson: **never evaluate a system on win rate alone. Win rate is meaningless without the average win/loss ratio.** The two must always be quoted together, and expectancy is the number that fuses them.

### Payoff ratio and the breakeven win-rate map

The **payoff ratio** is Average Win (R) ÷ Average Loss (R). Given a payoff ratio, there is a *minimum win rate* below which you lose money. Setting expectancy to zero and solving:

Breakeven Win% = 1 / (1 + Payoff Ratio)

| Payoff (Avg Win : Avg Loss) | Breakeven Win% | You need to beat |
|-----------------------------|---------------|------------------|
| 1 : 1 | 50.0% | 50% |
| 1.5 : 1 | 40.0% | 40% |
| 2 : 1 | 33.3% | 33% |
| 3 : 1 | 25.0% | 25% |
| 5 : 1 | 16.7% | 17% |
| 0.5 : 1 (typical option seller) | 66.7% | 67% |

Read the last row carefully. If your winners are only half your losers — which is precisely the shape of premium-selling without disciplined stops — you must win **two out of every three trades just to break even**, before brokerage and STT. That is a brutal bar, and it explains why the option-selling crowd that "wins most days" so often ends the year red.

Print this table. Before you trade any setup, ask: *what is my realistic payoff ratio, and does my win rate clear the breakeven line with margin?* If it doesn't, no amount of discipline saves you — the math is against you.

## A Fuller Worked Example: Validating a Real Setup

Suppose you trade a specific setup: **Bank Nifty ORB (opening-range breakout) on trending days**, with a fixed initial stop at the opposite end of the 15-minute opening range, targeting the day's extension. Over 60 logged trades you record:

- 24 winners, 36 losers → Win% = 40%.
- Winners average +2.6R (some run to +5R on strong-trend days, most around +1.8R).
- Losers average −1.05R (slight overshoot beyond stop due to fast moves).

**Expectancy = (0.40 × 2.6) − (0.60 × 1.05) = 1.04 − 0.63 = +0.41R per trade.**

Now translate to money and to a year. If you take roughly 60 such trades a quarter (about one per trading day on qualifying days) and risk ₹15,000 per trade:

- Expected R per quarter: 60 × 0.41 = **+24.6R.**
- In rupees: 24.6 × ₹15,000 = **₹3.69 lakh per quarter, gross.**
- Annualised (240 trades): 240 × 0.41 = **+98.4R ≈ ₹14.76 lakh gross.**

Then subtract costs *in R terms* — and this is where many edges die. If round-trip brokerage + STT + exchange charges + slippage average ₹450 per Bank Nifty futures trade, and your R is ₹15,000, costs are 450/15,000 = **0.03R per trade.** Net expectancy = 0.41 − 0.03 = **+0.38R.** Survives comfortably.

But run the same setup on **weekly options** where round-trip friction (bid-ask spread on OTM strikes + STT on premium + slippage) can easily be 0.15–0.25R per trade, and net expectancy collapses toward 0.41 − 0.20 = **+0.21R** or worse. Same edge, different instrument, half the profit. **R-multiple accounting is the only framework that makes this cost-drag visible before it bankrupts you.**

## Standard Error: Is Your Edge Real, or Noise?

A +0.41R expectancy over 8 trades means nothing — you could get that from luck. Over 300 trades it means a great deal. The bridge is the **standard error of expectancy**, which tells you how much your measured expectancy could be off due to sample size.

The rough rule: the uncertainty in your expectancy shrinks with the square root of the number of trades. A practical field formula:

Standard Error ≈ (Standard Deviation of R-multiples) / √N

If your R-multiples have a standard deviation of about 1.6 (typical for a 40%/2.5R system) and you have N = 50 trades:

SE ≈ 1.6 / √50 ≈ 1.6 / 7.07 ≈ **0.23R.**

Your measured +0.41R has a one-sigma band of roughly 0.41 ± 0.23, i.e. the *true* expectancy could plausibly be anywhere from +0.18R to +0.64R. That's a wide, humbling range — the edge is probably real but you shouldn't bet the farm on 0.41.

At N = 200 trades: SE ≈ 1.6 / 14.1 ≈ **0.11R.** Now the band is 0.41 ± 0.11 → +0.30R to +0.52R. Much firmer. **You need on the order of 100–200 trades before your expectancy is trustworthy.** This is the honest reason not to abandon a sound system after 15 bad trades, and not to bet big on a hot system after 15 good ones. Both are inside the noise band.

## System Quality: Expectancy Isn't the Whole Story

Two systems can both have +0.4R expectancy but feel utterly different to trade. One takes 8 trades a month; the other takes 80. The second compounds your edge ten times faster. Van Tharp's **SQN-style thinking** captures this by combining expectancy, its consistency, and frequency:

System Quality ≈ (Expectancy / StdDev of R) × √(Trades per period)

- System A: Expectancy 0.40R, StdDev 1.5R, 20 trades/month → (0.40/1.5) × √20 = 0.267 × 4.47 = **1.19.**
- System B: Expectancy 0.40R, StdDev 1.5R, 80 trades/month → (0.40/1.5) × √80 = 0.267 × 8.94 = **2.39.**

Same expectancy, same consistency — but System B, by trading four times as often, delivers roughly double the compounding rate. **Frequency multiplies edge.** This is why intraday index traders with a modest +0.25R edge can out-earn swing traders with a +0.6R edge: 250 chances a month versus 15. It also warns the other way — a high-frequency system with *negative* expectancy destroys you four times faster too.

## How to Use R and Expectancy for Bias, Sizing, and Review

**1. Position sizing flows directly from R.** Fix your R as a percentage of capital (say 1% — the standard). On ₹20 lakh capital, R = ₹20,000. Then quantity is always `R ÷ (stop distance)`. Wide stop → fewer shares; tight stop → more. Every trade risks exactly the same 1R, so your equity curve reflects your *edge*, not your emotional bet-sizing on days you "feel sure."

**2. Expectancy sets your realistic income.** Expected monthly R = Expectancy × Trades/month. On +0.38R net and 40 trades/month, that's +15.2R. At 1% risk, that's roughly 15% of capital per month *in expectation* — but with the standard-error band and drawdowns making the path violent. Under-promise to yourself.

**3. Review by cohort.** Slice your R-log by setup, instrument, day of week, time of day. You will often find your overall +0.35R is actually +0.9R on ORB trades and −0.3R on "reversal" trades you take out of boredom. Cutting the negative-expectancy cohort raises your whole system. This is the single highest-return activity in trading, and it is *only possible* with R-multiple records.

**4. Use expectancy to hold your nerve.** When you're 6 trades into a −5R streak, the R-log reminds you that a +0.4R system produces 6-loss streaks routinely (a 40%-win system throws 6 straight losers about once every ~55 trades). The math gives you permission to keep executing the edge instead of abandoning it at the worst moment.

## Pitfalls

- **Recomputing R off the trailed stop** to inflate R-multiples. Always the initial stop.
- **Ignoring costs.** Log costs in R. An edge that's +0.4R gross and +0.05R net after option friction is barely an edge.
- **Cherry-picking the sample.** "My expectancy since I started using this new rule" with N = 12 is noise. Report full samples and the standard-error band.
- **Averaging across regimes.** A trend system shows +0.7R in trending quarters and −0.2R in chop. The blended +0.25R hides that you must *not trade it* in chop. Segment by regime.
- **Mistaking a lucky streak for edge improvement.** Big +R runs feel like skill; they're often the right tail of the same distribution. Wait for N ≥ 100.
- **Fat left tails.** Naked option selling shows lovely expectancy until the −8R day. Expectancy computed without ever having taken the tail loss is a mirage. Always ask: *what is my worst plausible single-trade R, and is it in the sample?*

## Interview-Ready Summary

R is your initial per-trade risk in rupees, fixed at entry; every outcome is measured as a multiple of it, which normalises trades across instruments and bet sizes. Expectancy is the average R-multiple per trade — `(Win% × AvgWinR) − (Loss% × AvgLossR)` — and it, not win rate, decides whether a system makes money. A 40%-win system with 2.5:1 payoff is strongly positive (+0.4R); an 80%-win option-selling system with a fat loss tail can be negative. The breakeven win rate is `1/(1+payoff)`, so a 0.5:1 payoff needs 67% wins just to break even. Costs must be logged in R because option friction can halve an edge. Expectancy is only trustworthy after ~100–200 trades because of the standard-error band `StdDev(R)/√N`. Frequency multiplies edge (System Quality ≈ Expectancy/StdDev × √trades), which is why modest-edge high-frequency index traders out-earn high-edge low-frequency swing traders. Size every trade to a fixed 1% R so the equity curve reflects the edge, review by setup cohort to cut negative-expectancy trades, and remember that a positive system still throws routine 6-loss streaks — the math is your reason to keep executing.
