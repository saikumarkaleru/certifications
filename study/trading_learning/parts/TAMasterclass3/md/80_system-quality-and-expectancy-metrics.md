# System Quality & Expectancy Metrics

A backtest that says "78% win rate, ₹4.2 lakh profit" tells you almost nothing about whether you should trade the system, size it up, or bin it. Two systems with identical net profit can be worlds apart: one made its money in a smooth grind you could actually hold through, the other made it all in two lucky trades and spent the rest of the year in a 40% drawdown that would have flushed you out. This chapter is the toolkit for turning a raw list of trades into honest, comparable *numbers* — expectancy, expectancy per unit risk, the System Quality Number, MAR, Sharpe, Sortino, profit factor, and the drawdown geometry — and for using those numbers to size positions, compare systems and, most importantly, detect when a live system has stopped working. This is a QUANT chapter, so the maths is precise and each metric comes with a worked Indian example.

## The foundation: expectancy

Everything starts with **expectancy** — the average rupees you expect to make (or lose) *per trade*, over a large sample:

`Expectancy (₹) = (Win% × Avg Win) − (Loss% × Avg Loss)`

Consider a Bank Nifty intraday breakout system, 200 trades:

| Metric | Value |
|---|---|
| Wins | 84 (42%) |
| Losses | 116 (58%) |
| Average win | ₹6,800 |
| Average loss | ₹3,100 |

Expectancy = (0.42 × 6,800) − (0.58 × 3,100) = 2,856 − 1,798 = **₹1,058 per trade**.

Note the win rate is only 42% — this system loses more often than it wins, yet it is profitable because winners are 2.2× losers. This kills the beginner obsession with win rate. A 42%-win system with a 2.2 reward-to-risk beats a 70%-win system with a 0.35 reward-to-risk. Win rate alone is meaningless; expectancy is the truth.

Over 200 trades this system's gross profit is 200 × ₹1,058 = ₹2.12 L. But expectancy is *pre-cost*. Subtract real friction: at ~₹350 all-in per Bank Nifty options round-turn (brokerage, STT, exchange, GST, stamp), cost per trade is ₹350, so **net expectancy = ₹708/trade** — a 33% haircut. Always state expectancy net of costs, or you are lying to yourself.

## Expectancy per unit risk (R-multiples)

Rupee expectancy depends on how big you traded, which makes it hard to compare systems. Normalise by expressing every trade as an **R-multiple** — its P&L divided by the rupee amount you *risked* (your stop distance × size) on entry. A trade that made twice what you risked is +2R; one stopped out at your planned stop is −1R.

`Expectancy (R) = average of all trade R-multiples`

If the Bank Nifty system risked ₹3,100 per trade on average (the loss size = the stop), then expectancy in R = ₹1,058 ÷ ₹3,100 = **+0.34R per trade**. This is the single most portable performance number in trading: it says "for every rupee I put at risk, I get 34 paise back on average, regardless of account size." A system with +0.3R or better and a decent trade frequency is genuinely tradeable; below +0.1R the edge is too thin to survive cost and slippage drift.

R-multiples also let you build the **R-distribution** — a histogram of every trade's R outcome. This is far more informative than any single average. You might find your edge is entirely in a few +8R to +15R trades (a trend system's fat right tail) while the mode is a small loss. That shape tells you *never* to cut winners early and to accept a low win rate — the whole edge lives in the tail.

## The System Quality Number (SQN)

Van Tharp's **System Quality Number** answers "how *reliable* is this expectancy?" by scaling it by consistency and sample size. It is the t-statistic of your R-distribution:

`SQN = (Mean R ÷ StdDev of R) × √N`

capped at N = 100 in Tharp's original (to avoid rewarding sheer trade count). Suppose the Bank Nifty system's R-multiples have mean +0.34 and standard deviation 1.9, over 200 trades (use √100):

SQN = (0.34 ÷ 1.9) × 10 = **1.79**

Tharp's rough grading:

| SQN | Quality |
|---|---|
| < 1.6 | Below average / hard to trade |
| 1.6 – 1.9 | Average |
| 2.0 – 2.5 | Good |
| 2.5 – 3.0 | Excellent |
| 3.0 – 5.0 | Superb |
| > 5.0 | Suspect — probably curve-fit or too few trades |

Our system at 1.79 is "average" — real, tradeable, but not spectacular; its low win rate and high R-variance (1.9) drag the score. The insight in SQN is the `Mean/StdDev` term: a system with the *same* expectancy but tighter, more consistent outcomes (lower R-std) scores higher and is easier to trade and to size confidently. Reducing variance of outcomes is as valuable as raising average return. Note the caveat in the last row: an SQN above 5 on a backtest almost always signals overfitting or a sample too small and too clean to be real — treat suspiciously high scores as red flags, not trophies.

## Profit factor and payoff ratio

Two quick, intuitive ratios:

**Profit factor** = gross profit ÷ gross loss. For our system: gross profit = 84 × 6,800 = ₹5.71 L; gross loss = 116 × 3,100 = ₹3.60 L; PF = **1.59**. Interpretation: for every ₹1 lost, the system makes ₹1.59. Rules of thumb: PF < 1.25 is fragile (costs and slippage can push it under 1.0), 1.5–2.0 is solid, > 2.5 on a large sample is excellent, and > 4 is again suspicious of overfitting.

**Payoff ratio (reward-to-risk)** = avg win ÷ avg loss = 6,800 ÷ 3,100 = **2.19**. Combined with win rate via the breakeven identity, a system survives if `Win% > 1 ÷ (1 + payoff)`. Here breakeven win% = 1 ÷ 3.19 = 31.3%; the system's 42% is comfortably above, so it has margin. This identity is the fastest sanity check on any setup: know your reward-to-risk, and you instantly know the win rate you must clear.

## Drawdown geometry — the risk that actually ends careers

Expectancy tells you the destination; drawdown tells you whether you survive the journey. The metrics:

- **Maximum drawdown (MaxDD):** the largest peak-to-trough equity decline, in % of peak equity. This is the single number that most determines whether you can *hold* a system. A system with a 45% MaxDD is nearly untradeable psychologically even if profitable — almost no one keeps trading through a near-halving of capital.
- **Longest drawdown duration:** how many days/months from equity peak back to a new peak. A system can have a modest 15% MaxDD but take 14 months to recover — that is 14 months of doubting yourself. Duration breaks more traders than depth.
- **MAR ratio (a.k.a. Calmar):** `CAGR ÷ MaxDD`. This is the professional's favourite single robustness number because it directly trades return against the pain of achieving it.

Worked example: a Nifty swing system compounds at **CAGR 26%** with a **MaxDD of 19%**. MAR = 26 ÷ 19 = **1.37**. Grading:

| MAR | Interpretation |
|---|---|
| < 0.5 | Weak — return doesn't justify the pain |
| 0.5 – 1.0 | Acceptable |
| 1.0 – 2.0 | Good (most tradeable real systems live here) |
| > 2.0 | Excellent (rare over long, honest samples) |
| > 3.0 | Verify for overfitting / short sample |

Our 1.37 is a genuinely good, holdable system. Note how MAR punishes deep drawdowns harshly: a system with 40% CAGR but 50% MaxDD scores 0.80 — *worse* than our 26%/19% system despite far higher headline return. That is the correct verdict: the 40% system is a heart-attack machine you will abandon at the bottom.

## Risk-adjusted return ratios: Sharpe and Sortino

**Sharpe ratio** = (annualised return − risk-free rate) ÷ annualised volatility. In India use the risk-free ~6.5% (T-bill). For a system returning 26% with 17% volatility: Sharpe = (26 − 6.5) ÷ 17 = **1.15**. Above 1 is good, above 2 is excellent, above 3 is rare and worth double-checking. Sharpe's flaw: it penalises *upside* volatility as much as downside — a system with big winning months gets dinged for the very thing you want.

**Sortino ratio** fixes this by dividing excess return only by *downside* deviation (volatility of negative returns). Because most systems' big moves are the winners you keep, Sortino is usually higher than Sharpe. If downside deviation is 11%, Sortino = (26 − 6.5) ÷ 11 = **1.77**. For trend and momentum systems with fat positive tails, Sortino is the fairer measure — it doesn't punish you for the +12R trade that spiked your return variance upward.

A subtlety for Indian intraday systems: annualising from daily returns assumes independence. If your trades cluster (e.g. you're always long during a trend), returns autocorrelate and the naïve annualisation overstates Sharpe. When in doubt, report the *per-trade* R-statistics (expectancy-R and SQN) alongside the annualised ratios — they don't depend on the annualisation assumption.

## A worked comparison — three systems, one table

The whole point of these metrics is *comparison*. Suppose you've backtested three candidate systems on 2019–2025 NSE data, all net of realistic costs:

| Metric | A: Nifty trend | B: Bank Nifty fade | C: Stock momentum |
|---|---|---|---|
| Trades/yr | 22 | 190 | 55 |
| Win rate | 41% | 58% | 47% |
| Payoff ratio | 2.8 | 0.95 | 2.1 |
| Expectancy (R) | +0.44 | +0.19 | +0.36 |
| SQN | 2.1 | 2.4 | 1.9 |
| Profit factor | 1.9 | 1.4 | 1.7 |
| CAGR | 21% | 34% | 27% |
| MaxDD | 16% | 22% | 20% |
| MAR | 1.31 | 1.55 | 1.35 |
| Sharpe | 1.2 | 1.4 | 1.1 |

Naïve reading: B wins — highest CAGR, SQN, MAR, Sharpe. But look deeper. B's edge is only +0.19R per trade — thin, and it fires 190 times a year, so it is *exquisitely* sensitive to any rise in slippage or cost: a ₹150 increase in per-trade friction could nearly halve its edge. A's +0.44R is far more robust per trade; it will degrade gracefully. C sits in between. The mature conclusion is not "trade B" but "these three are *different* and complementary — combine them" (which is exactly the previous chapter's lesson). Metrics don't make the decision for you; they surface the trade-offs — B trades high frequency and thin edge (fragile to costs), A trades low frequency and fat edge (robust but idle, and dependent on a few tail trades). Knowing *which kind* of system you hold dictates how you size and monitor it.

## Using expectancy to size — the link to Kelly

Expectancy-R and the R-distribution feed directly into position sizing. The **Kelly fraction** for a system with win probability p, payoff b (avg win / avg loss):

`f* = p − (1 − p) ÷ b`

For system A: f* = 0.41 − 0.59 ÷ 2.8 = 0.41 − 0.21 = **0.20**, i.e. full-Kelly says risk 20% of capital per trade. *Never* trade full Kelly — its drawdowns are savage (a full-Kelly system routinely suffers 50%+ drawdowns) and it assumes your estimated p and b are exact, which they never are. Standard practice is **quarter- to half-Kelly**: risk 5% (quarter) of the sleeve per trade for A, which captures most of the growth with a fraction of the drawdown. The expectancy metrics thus close the loop: they tell you both *whether* to trade and *how big*.

## Detecting a dead edge — live vs backtest monitoring

The highest-value use of these metrics is not choosing systems but *catching decay* in a live one. Markets adapt; edges fade. You need an objective trip-wire, not a gut feeling.

Method: from your backtest, you know the *distribution* of expectancy over rolling windows — e.g. the mean and standard deviation of 30-trade rolling expectancy-R. Live, you track the same rolling window. As long as live expectancy stays within, say, the backtest's historical range (roughly mean ± 2 standard deviations of the rolling estimate), the system is behaving normally — even a painful drawdown may be statistically ordinary. But if live rolling expectancy-R falls *below* the worst rolling window ever seen in the backtest, that is a statistical signal the edge may have structurally changed — time to cut size or halt and investigate.

Concrete rule for system A: backtest 30-trade rolling expectancy averaged +0.44R with the worst-ever 30-trade window at −0.15R. Live, after 30 trades you're at −0.28R — *worse than anything the backtest ever produced*. That is not "a bad patch"; that is your objective evidence to stand down. This converts the hardest emotional decision in trading — "is my system broken or just unlucky?" — into a pre-committed statistical test. Combine it with a simpler equity-curve rule (e.g. stop trading a system when its equity closes below its own 200-day moving average) as a coarse backup.

## Pitfalls

- **Small samples lie.** SQN, Sharpe and profit factor all need ~100+ trades to mean anything; a 20-trade backtest with SQN 4 is noise, not a superb system. Report the sample size next to every metric.
- **In-sample glory.** All these numbers computed on the data you *optimised* on are inflated. The honest figures come from out-of-sample / walk-forward testing; expect metrics to degrade 20–40% out of sample, and be suspicious if they don't degrade at all.
- **Ignoring costs and slippage.** Every metric here must be net of realistic NSE/MCX friction. High-frequency, thin-edge systems (like the fade) can look great gross and be unprofitable net.
- **Averages hide tails.** Expectancy is an average; a system whose entire edge is three +15R trades has huge tail dependence — miss those and the edge vanishes. Always inspect the R-distribution, not just its mean.
- **Overfit-flag metrics.** SQN > 5, profit factor > 4, MAR > 3 on a backtest usually signal curve-fitting or too-clean a sample, not genius. Treat suspiciously good numbers as warnings.
- **Chasing one metric.** No single number captures a system. A high Sharpe with a 14-month recovery time is still untradeable. Read expectancy, SQN, MAR *and* drawdown duration together.

## Interview-ready summary

Judge a system by *expectancy* — average rupees or R-multiples per trade, net of costs — not by win rate, since a 42%-win system with 2.2× payoff beats a 70%-win system with a poor payoff. Normalise to R-multiples for portability, then layer on quality metrics: **SQN** (= mean-R ÷ std-R × √N, the t-stat of your edge; 2.0+ is good), **profit factor** (gross profit ÷ gross loss; 1.5–2.0 solid), and the **payoff/win-rate breakeven** identity as a fast sanity check. Weigh return against pain with **MAR** (CAGR ÷ MaxDD; 1.0–2.0 is a genuinely holdable system) and risk-adjusted return with **Sharpe** (using India's ~6.5% risk-free) and its downside-only cousin **Sortino**, which fairly rewards the fat positive tails of trend systems. Always read drawdown *depth and duration* together — duration ends more careers than depth. Feed expectancy and payoff into a *fractional* Kelly for sizing (quarter- to half-Kelly, never full). And use the metrics' greatest gift: an objective decay trip-wire — when live rolling expectancy falls below the worst window your backtest ever produced, the edge is likely broken and you cut size, converting the hardest emotional call in trading into a pre-committed statistical test. Beware small samples, in-sample inflation, ignored costs, tail dependence, and suspiciously perfect numbers that betray overfitting.
