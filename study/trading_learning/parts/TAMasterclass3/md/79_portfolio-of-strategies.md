# Portfolio-of-Strategies Construction

Most retail traders spend years hunting for the one perfect system — the single setup that prints money in every market. That search is a dead end. Every edge is regime-dependent: a trend-follower dies in a range, a mean-reverter gets steamrolled in a trend, a volatility-seller is fine until it blows up in one afternoon. The professional answer is not a better single strategy but a *portfolio* of imperfect strategies whose weaknesses do not line up in time. This chapter is about how to build that portfolio for Indian markets — how to combine a Nifty trend system, a Bank Nifty mean-reversion system, a stock-breakout system and an options-premium harvester into one book whose equity curve is smoother, deeper and more survivable than any single component.

This is a STRATEGY-construction chapter, so it is organised around the decisions you actually have to make: what to combine, how to weight, how to size, how to allocate risk, and how to rebalance — all with realistic NSE/MCX costs and rupee numbers.

## Why combine strategies at all — the diversification maths

The single most important number in strategy combination is the *correlation of returns* between two systems — not their correlation of instruments, but of their daily or per-trade P&L. If System A and System B each have an annual return of 24% and volatility of 18%, and you split capital 50/50, your blended volatility is:

`σ_portfolio = √(w_A²σ_A² + w_B²σ_B² + 2·w_A·w_B·ρ·σ_A·σ_B)`

Plug in w = 0.5, σ = 18% each:

| Correlation ρ | Blended volatility | Blended Sharpe (return 24%, rf 6.5%) |
|---|---|---|
| +1.0 | 18.0% | 0.97 |
| +0.5 | 15.6% | 1.12 |
| 0.0 | 12.7% | 1.38 |
| −0.3 | 10.6% | 1.65 |
| −0.5 | 9.0% | 1.94 |

Return stays at 24% in every row (a weighted average of two equal returns), but volatility collapses as correlation falls. At ρ = 0 the Sharpe jumps from 0.97 to 1.38 — a 42% improvement in risk-adjusted return *purely from combination*, with no improvement to either underlying edge. That is the free lunch. The entire craft of portfolio construction is finding strategies whose P&L streams are genuinely uncorrelated and then not accidentally re-correlating them through shared risk, shared instruments or shared regime exposure.

The catch specific to trading strategies (versus buy-and-hold assets) is that correlations are *conditional and unstable*. Two strategies can be uncorrelated for two years and then move together violently on one gap-down day — the March 2020 COVID crash, the Feb 2021 budget rally, the June 2024 election-result day when Nifty gapped 8% intraday. Tail correlation matters more than average correlation, and we will return to it under pitfalls.

## The building blocks — a concrete India strategy set

A workable four-strategy book for an Indian trader with ₹20 lakh of risk capital might look like this. Each is a real, distinct edge type:

| # | Strategy | Instrument | Type | Typical holding | Trades/yr | Standalone edge |
|---|---|---|---|---|---|
| S1 | Nifty 50 trend-follow (20/50 EMA + ADX>20) | Nifty futures | Trend | 8–25 days | ~18 | Momentum / drift |
| S2 | Bank Nifty gap-fade (open-range reversion) | Bank Nifty fut | Mean-revert | Intraday | ~180 | Overreaction |
| S3 | Stock breakout (52-wk high + volume) | 15 NSE cash stocks | Trend/momentum | 5–40 days | ~60 | Breakout continuation |
| S4 | Nifty short-strangle harvester (delta-neutral, IV filter) | Nifty weekly options | Vol premium | 2–5 days | ~45 | Variance risk premium |

Why these four? Their edges come from *different sources*. S1 and S3 both profit from trends but on different timeframes and universes (index vs single stocks), so they diverge often — a stock can break out while the index chops. S2 profits from short-term overreaction, which is structurally the *opposite* trade to S1, so on choppy days when S1 is bleeding whipsaws, S2 tends to earn. S4 earns when realised volatility comes in below implied — it is a bet on calm — which means it makes money in exactly the boring sideways tapes that punish trend systems. The one dangerous overlap: S4 (short vol) and S1/S3 (long trend) can *both* lose on a violent trend-breaking gap. That shared tail is the thing to manage.

## Measuring the actual correlations

You never assume correlations — you measure them from a common daily P&L series, in rupees, on the *same* backtest calendar. Suppose over three years of daily returns (each strategy's daily mark-to-market as a fraction of its own allocated capital) you compute this matrix:

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| **S1** | 1.00 | −0.18 | 0.46 | −0.11 |
| **S2** | −0.18 | 1.00 | −0.05 | 0.09 |
| **S3** | 0.46 | −0.05 | 1.00 | −0.07 |
| **S4** | −0.11 | 0.09 | −0.07 | 1.00 |

Reading this: S1 and S3 are meaningfully correlated (0.46) — both trend, as expected — so they should *not* both get full weight; they partly double-count the same bet. Everything else is near-zero or negative, which is excellent. The average pairwise correlation is roughly 0.02 — a genuinely diversified book. If instead you had built four trend systems on four indices, you would see 0.7–0.9 everywhere and the "portfolio" would be one bet wearing four costumes.

A quick diagnostic: the *diversification ratio* = (weighted average of individual volatilities) ÷ (portfolio volatility). Above 1.4 is a well-diversified book; near 1.0 means your strategies are clones. With the matrix above and equal weights, this book scores about 1.55.

## Weighting schemes — from naïve to risk-parity

Once you have distinct edges, the question is *how much capital or risk each gets*. Four standard approaches, in increasing sophistication:

**1. Equal-weight capital (1/N).** Give each strategy ₹5 lakh. Simple, robust, hard to overfit. Its flaw: it ignores that S2 (intraday Bank Nifty) is far more volatile per rupee than S1, so equal *capital* means unequal *risk* — S2 will dominate the P&L swings.

**2. Equal-weight risk (inverse-volatility).** Allocate capital inversely proportional to each strategy's volatility so each contributes the *same* rupee risk. If daily volatilities are S1 1.1%, S2 2.4%, S3 1.6%, S4 0.9% of allocated capital, the inverse-vol weights are:

| Strategy | 1/σ | Weight | Capital (₹) |
|---|---|---|---|
| S1 | 0.909 | 0.243 | 4.86 L |
| S2 | 0.417 | 0.111 | 2.23 L |
| S3 | 0.625 | 0.167 | 3.34 L |
| S4 | 1.111 | 0.297 | 5.94 L |
| **Sum** | 3.062 | 1.000 | 20.0 L |

Now each strategy contributes roughly equal risk, not equal money. The volatile Bank Nifty fader gets the least capital; the calm strangle harvester gets the most. This is the sensible default for most traders — it needs only volatility estimates, which are far more stable than return or correlation estimates.

**3. Risk parity (correlation-aware).** Goes one step further and equalises each strategy's *contribution to portfolio volatility*, accounting for correlations. Because S1 and S3 are correlated, true risk parity trims both slightly and pushes weight toward the uncorrelated S2 and S4. The marginal contribution to risk of strategy i is `w_i · (Σw)_i / σ_p`; you iterate weights until all four contributions are equal. In practice for this book it shifts maybe 3–4 percentage points from S1/S3 to S2/S4 versus plain inverse-vol — a refinement, not a revolution.

**4. Mean-variance / Kelly optimal.** Maximises Sharpe or geometric growth using expected returns *and* the covariance matrix. Mathematically optimal, practically dangerous: it is exquisitely sensitive to the expected-return estimates, which are the noisiest inputs you have. A tiny error in expected return produces wildly concentrated, unstable weights. The professional fix is to shrink hard — cap any single weight (say 35%), use half-Kelly or quarter-Kelly, and blend the optimiser output 50/50 with inverse-vol. Full unconstrained mean-variance on backtested returns is one of the most reliable ways to overfit a book into failure.

**Recommendation for a real Indian retail/prop book:** start with inverse-volatility, cap each strategy at 35% and each *bet type* (all-trend, all-short-vol) at 50%, and only layer correlation-aware tilts once you have a year of live data. Elegance is not the goal; survivability is.

## Position sizing across the book — the two-layer model

There are two sizing decisions and traders constantly conflate them:

- **Layer 1 — strategy allocation:** how much of the ₹20 L book each strategy commands (the weights above).
- **Layer 2 — per-trade sizing within a strategy:** how large each individual trade is inside its allocation.

For Layer 2, fixed-fractional risk is the workhorse: risk a fixed fraction f of the *strategy's allocated capital* per trade. Say S1 gets ₹4.86 L and you risk 1.5% per trade = ₹7,290 risk. If a Nifty long entry is at 24,600 with a stop at 24,380 (220-point risk, and Nifty lot = 25, so ₹5,500 risk per lot at ₹1/point... actually ₹1 index point = ₹25 per lot × ... let me use point value): Nifty futures point value is ₹25 per point per lot (lot size 25 in 2026 convention will vary — check current NSE lot). Risk per lot = 220 points × ₹25 = ₹5,500. Number of lots = ₹7,290 ÷ ₹5,500 ≈ 1 lot. Round *down*, never up.

Critically, the per-trade risk fraction is set against the *strategy sleeve*, not the whole book — otherwise a hot strategy quietly bloats and re-concentrates the portfolio you carefully diversified.

There is also a *portfolio heat* cap sitting on top: the sum of all open risk across all four strategies at any moment must not exceed, say, 6% of the total book (₹1.2 L). If S1, S3 and S4 are all in trending-market mode with full positions, their combined open risk might hit the cap and *block* S2 from adding a new fade until something closes. This global heat governor is what stops a "diversified" book from becoming a single leveraged directional bet on a day when every strategy happens to want to be long.

## Worked India example — a month in the life of the book

Take a stylised but realistic July 2026. Book = ₹20 L, inverse-vol weights as above.

- **Week 1 (trending up):** Nifty grinds from 24,200 to 24,900. S1 is long 1 lot, up ₹17,500 open. S3 catches breakouts in an auto stock and a PSU bank, +₹22,000 combined. S2 (fade) has a rough week — every gap keeps running, three losing fades, −₹9,400. S4 short strangle earns theta in the calm grind, +₹6,800. **Net week: +₹36,900 (+1.85%).** Note S2 lost while S1/S3 won — exactly the intended offset, just running the other way here.
- **Week 2 (sharp two-day correction):** Nifty drops 24,900 → 24,300 on a US-CPI scare. S1 stop hit at 24,650, gives back ₹6,000 of the open profit but locks a small net gain. S3 two stops hit, −₹11,000. S4 — danger zone — the vol spike hurts the short strangle; the position is delta-hedged and IV-filtered so the loss is contained to −₹14,500 rather than catastrophic. S2 finally shines: the panic-driven gap-downs mean-revert intraday, five winning fades, +₹19,200. **Net week: −₹12,300 (−0.62%).** The drawdown is shallow *because* S2 and the rest are negatively correlated in this regime.
- **Weeks 3–4 (choppy range 24,300–24,700):** S1 and S3 whipsaw, small net loss −₹8,000 combined. S2 loves the range: +₹21,000. S4 loves the low realised vol: +₹15,300. **Net: +₹28,300 (+1.42%).**

**Month total: +₹52,900, roughly +2.6%,** with a worst intra-month drawdown of about 1%. Any single strategy run alone would have shown a far bumpier path — S2 alone would have been deeply underwater in Week 1, S1 alone would have given back most of Week 1 in Week 2. The book is smoother than its parts. That smoothness is the entire product.

## Backtest, edge and realistic-cost notes

When you backtest the *combined* book, three cost realities dominate and are routinely ignored:

1. **Costs scale with the highest-frequency strategy.** S2 fires ~180 intraday round-trips a year; at Bank Nifty futures with brokerage + STT + exchange + GST + stamp, realistic all-in cost is roughly ₹1,000–1,400 per round-turn per lot. That is ~₹2 L/year of friction on a ₹2.2 L sleeve — the edge must clear that before it contributes anything. Always net every strategy's returns *individually* after its own true costs before you even compute the correlation matrix, or you will diversify into a strategy that is actually a net loser gross of the portfolio effect.
2. **Slippage on shared events.** On the June-2024-style result days, S1, S3 and S4 might all need to trade at once, into the same illiquid, gapping tape. Model an extra slippage penalty on days flagged high-volatility; a book that looks great assuming mid-price fills can bleed on the 5–6 days a year that actually matter.
3. **Margin and capital efficiency.** F&O strategies (S1, S2, S4) consume SPAN + exposure margin. A ₹20 L book running futures and short options can easily need ₹12–14 L in margin at peak, leaving thin buffer. Backtest the *margin* path, not just the P&L path — a strategy combination that is profitable but occasionally demands more margin than you hold will force liquidation at the worst moment.

The honest edge statement: combining these four should lift the blended Sharpe from the ~1.0 of the best single component to roughly 1.5–1.8, and — more importantly — cut the maximum drawdown from the 20–30% typical of a lone trend or short-vol system to maybe 10–14%. The *return* does not magically rise; the *risk-adjusted* return and *survivability* do. Anyone promising that combination triples returns is selling leverage, not diversification.

## Rebalancing — when and how

Weights drift as strategies win and lose. Rebalancing sells the winners and tops up the losers back to target — mildly counter-intuitive but it is what keeps risk allocation honest and harvests mean-reversion between sleeves. Rules that work in practice:

- **Calendar + threshold hybrid:** review monthly; only actually rebalance a sleeve if its weight has drifted more than ±5 percentage points from target. This avoids churning costs for tiny drifts.
- **Recompute volatilities on a rolling 60–90 day window**, not the full history — regime volatility changes, and inverse-vol weights should breathe with it. But cap how fast weights move (e.g. max 20% weight change per rebalance) to avoid chasing noise.
- **Never rebalance *into* a strategy that has structurally broken.** Threshold rebalancing assumes losers mean-revert; a strategy whose edge has genuinely decayed (see the next chapter's tracking of live-vs-backtest expectancy) should be *cut*, not topped up. Distinguishing a normal drawdown from a dead edge is the hardest judgment in portfolio management, and it is a statistical question (are the recent returns within the historical drawdown distribution?) not an emotional one.

## Confluence — how strategies reinforce each other

Beyond diversification, a portfolio lets strategies *talk*. Practical confluence rules:

- **Regime gating:** use a simple market-state classifier (e.g. Nifty ADX and realised-vol percentile) to *dial* sleeves up or down rather than run all four flat always. In a confirmed strong-trend regime, tilt toward S1/S3 and cut S2/S4; in a low-vol range, do the reverse. This is a soft overlay, not on/off, to avoid whipsawing the whole book on a regime misread.
- **Cross-confirmation for the tail:** since S4 (short vol) is your one fat-tail risk, use S1/S3's trend signal as a *veto*: if both trend systems flip strongly directional and ADX is high, reduce S4 size — that is precisely the environment (a starting trend) where short strangles get hurt.

## Pitfalls

- **Fake diversification.** Four trend systems, or four strategies all long the same crowded momentum stocks, share one hidden bet. Always measure P&L correlation, not instrument names.
- **Correlation regime shift in the tail.** Everything can go to +1 on a crash day. Size for the tail-correlation, not the calm-period average; assume the diversification benefit halves in a crisis.
- **Overfitting the weights.** Mean-variance optimisers will hand you gorgeous backtested weights that are pure curve-fit. Prefer robust inverse-vol; cap concentration; shrink Kelly.
- **Complexity you can't operate.** A four-strategy book with dynamic weights, regime gating and hedged options is a lot to run correctly at 9:15 a.m. every day. A simpler book you execute flawlessly beats an elegant one you fumble.
- **Ignoring margin and operational risk.** The best-diversified P&L is worthless if peak margin forces a liquidation, or if one strategy's bug corrupts the others' capital.
- **Rebalancing into a dead edge.** Topping up a structurally broken strategy is throwing good capital after decayed alpha.

## Interview-ready summary

A portfolio of strategies beats any single system because blending low- or negatively-correlated P&L streams cuts volatility and drawdown without cutting return — the diversification free lunch, worth 40–90% on the Sharpe ratio at low correlations. Build it from genuinely *different edge types* (index trend, intraday mean-reversion, stock breakout, options-premium harvest for an Indian book), measure the *return* correlation matrix, and diversify the *bets* not just the tickers. Weight by inverse-volatility as a robust default, cap concentration and bet-type exposure, and only add correlation-aware or Kelly tilts once you have live data — full mean-variance optimisation on a backtest is a classic overfit trap. Size in two layers (strategy sleeve allocation, then fixed-fractional per trade) under a global portfolio-heat cap, cost every strategy individually after real NSE/MCX friction, model the *margin* path and the *tail* correlation (which spikes toward +1 on crash days), rebalance on a calendar-plus-threshold rule, and cut — not top up — any sleeve whose edge has statistically decayed. The payoff is not higher returns but a smoother, deeper, more survivable equity curve — which is what lets you keep compounding.
