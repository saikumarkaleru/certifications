# Correlation & Beta Analysis for Traders

Most traders think in single charts: one instrument, one setup, one trade. But money is made and lost across a *portfolio* of positions, and the hidden killer of trading accounts is not a bad trade — it is five "different" trades that turn out to be the same trade wearing five costumes. Long Reliance, long HDFC Bank, long Infosys, long an index future, and short a put on Nifty look like diversification. On a red day they all bleed together, because they share one dominant driver: the Nifty. Correlation and beta are the two numbers that expose this. They convert the vague feeling of "these move together" into something you can measure, size, and hedge. This chapter is a working trader's treatment — not a statistics lecture — grounded in Nifty 50, Bank Nifty, individual NSE names, USDINR, and gold on MCX.

## What they are and the logic

**Correlation** measures how two return streams move *together*, on a scale from −1 to +1. A correlation of +1 means they move in perfect lockstep; −1 means perfectly opposite; 0 means no linear relationship. The crucial word is *linear* — correlation only sees straight-line co-movement and is blind to curved or threshold relationships (more on that pitfall later).

**Beta** measures how much one instrument moves *for a given move in a benchmark*, and it carries direction and magnitude. If Bank Nifty has a beta of 1.3 to Nifty, then when Nifty rises 1%, Bank Nifty tends to rise about 1.3%. Beta answers "how much," correlation answers "how reliably."

The two are cousins. Beta of asset *i* to benchmark *m* is:

> β = ρ(i, m) × (σ_i / σ_m)

where ρ is the correlation and σ is the standard deviation (volatility) of returns. So beta is correlation *scaled by the ratio of volatilities*. A stock can have a high correlation to Nifty but a beta above or below 1 depending on whether it is more or less volatile than the index. Adani Enterprises, for example, may correlate ~0.6 with Nifty yet carry a beta near 1.6 because its own volatility dwarfs the index's. HUL might correlate ~0.5 with Nifty but show a beta near 0.6 because it is a low-volatility defensive.

Why should a *technical* trader care? Three reasons. First, **risk aggregation**: your true exposure to a Nifty crash is the sum of each position's beta-weighted size, not the count of positions. Second, **hedging**: to neutralise a basket you must short the *beta-weighted* quantity of the hedge instrument, not an equal rupee amount. Third, **pair and relative-value setups**: correlation is the raw material of pairs trading, sector rotation, and hedged directional bets. If you trade F&O, beta is the difference between a hedge that works and one that leaves you dangerously long or over-hedged.

## Construction, formulas and settings

### Returns, not prices

Always compute correlation and beta on **returns**, never on raw price levels. Two rising stocks will show a spuriously high price-level correlation simply because both trend up over time; that number is meaningless. Use daily (or intraday) percentage or log returns:

> r_t = ln(P_t / P_{t−1})

Log returns are preferred because they are additive across time and roughly symmetric.

### Correlation formula

For two return series X and Y over n observations:

> ρ = Σ[(X_t − X̄)(Y_t − Ȳ)] / [ √Σ(X_t − X̄)² × √Σ(Y_t − Ȳ)² ]

The numerator is covariance; the denominator normalises by both volatilities so the result sits in [−1, 1].

### Beta by regression

Beta is the slope of an ordinary-least-squares regression of the asset's returns on the benchmark's returns:

> r_i = α + β · r_m + ε

- **β (slope)** = sensitivity to the market.
- **α (intercept)** = average return not explained by the market — the instrument's idiosyncratic drift.
- **R²** = the fraction of the asset's variance explained by the benchmark. R² = ρ². A stock with ρ = 0.7 has R² = 0.49, meaning roughly half its movement is "the market" and half is its own story.

### Lookback windows — the key setting

The single biggest decision is the **lookback window**. Common choices:

| Window | Trading days | Use case |
|---|---|---|
| Short | 20 | Regime-sensitive, noisy; intraday/swing hedging |
| Medium | 60 | The workhorse; balances responsiveness and stability |
| Long | 250 (1 year) | Structural beta; position sizing, "book" beta |

Short windows react fast but whipsaw. A 20-day correlation between two stocks can swing from 0.2 to 0.8 and back within a month, mostly from noise. Long windows are stable but stale — they'll tell you two names are correlated 0.4 long after a business change made them decouple. Professionals monitor **rolling** correlation and beta: recompute over a sliding window each day and *plot the series*. The plot itself is the signal. A rising rolling correlation across the market is a warning that diversification is evaporating — which is exactly what happens in crashes.

### Exponential weighting

A refinement: weight recent observations more heavily using an exponentially weighted moving covariance (the same idea as EWMA volatility). This gives you responsiveness without the abrupt "drop-off" artefact of a fixed window, where a single large day exits the window and correlation jumps for no fresh reason.

## Worked India example (levels and ₹)

Suppose you are running a swing book on 17 July 2026 with three longs, and Nifty sits at 24,800.

| Position | Qty (₹ notional) | Beta to Nifty (60-day) | Beta-weighted exposure |
|---|---|---|---|
| Reliance Industries | ₹5,00,000 | 1.05 | ₹5,25,000 |
| HDFC Bank | ₹4,00,000 | 1.15 | ₹4,60,000 |
| Infosys | ₹3,00,000 | 0.85 | ₹2,55,000 |
| **Total** | **₹12,00,000** | — | **₹12,40,000** |

Your gross book is ₹12,00,000, but your **effective Nifty exposure** is ₹12,40,000 — you are *more* exposed to a market drop than your rupee total suggests, because your book leans toward high-beta banking. If Nifty falls 2% (to ~24,300), your expected loss from market beta alone is 2% × ₹12,40,000 = **₹24,800**, before any stock-specific moves.

**Hedging with Nifty futures.** One Nifty future = 25 units. At 24,800, one lot ≈ ₹6,20,000 of notional. To neutralise ₹12,40,000 of beta-weighted exposure you need:

> Hedge lots = ₹12,40,000 / ₹6,20,000 = 2 lots short

Short 2 Nifty futures and your book becomes roughly market-neutral: you now profit or lose only on how your three stocks perform *relative to* Nifty (their alpha), not on the market's direction. If you had naively hedged on rupee notional (₹12,00,000 → ~1.94 → 2 lots) you'd have been close here, but with a defensive-heavy book the two numbers can diverge enough to leave you meaningfully over- or under-hedged.

**A pair example.** Consider ICICI Bank vs Axis Bank, two private banks that historically correlate ~0.8. Over 60 days you regress ICICI returns on Axis returns and find beta ≈ 1.2. If you want a market-and-sector-neutral bet that ICICI outperforms Axis, you go long ₹6,00,000 ICICI and short ₹6,00,000 × (1/1.2) worth... no — you hedge so the *beta-weighted* legs match. Long ₹6,00,000 Axis has beta-1 reference; to match ICICI's higher sensitivity you short a smaller rupee amount of ICICI, or scale the Axis leg up. The discipline is: **equalise beta-weighted notional across the two legs**, so a broad banking rally cancels out and only the *spread* between the two names drives P&L.

## How to trade it

Correlation and beta support several concrete tactics:

**1. Beta-weighted portfolio hedging.** Sum beta-weighted exposure across the whole book (longs positive, shorts negative), then short/long the index future to bring net beta to your target. Full neutrality = net beta 0. If you're mildly bullish, leave net beta at, say, +0.3 of your capital. Recompute weekly; beta drifts.

**2. Pairs / statistical arbitrage.** Find two names with high, *stable* correlation and a mean-reverting spread. Enter when the spread (or the ratio) stretches to ±2 standard deviations, exit at the mean. Beta sets the hedge ratio. Classic NSE pairs: ICICI/Axis, Tata Motors/M&M, HDFC Bank/Kotak, Reliance/ONGC (weaker). The trade lives or dies on the correlation *staying* high — always check the rolling series before entry.

**3. Correlation as a market-regime gauge.** When average pairwise correlation across index constituents spikes toward 1, breadth is collapsing and the market is trading as one macro block — typically fear-driven. This is a signal to cut gross exposure and widen stops, because "diversification" is temporarily fictional. When correlations fall, stock-picking and pairs setups work better.

**4. Cross-asset confluence.** USDINR and Nifty are usually *negatively* correlated (rupee weakness pressures equities via FII outflows); Nifty IT is *positively* correlated to USDINR (weak rupee helps exporters). Gold on MCX often rises when equities fall (a risk-off hedge), though this breaks in liquidity crunches when everything sells together. Knowing the sign and strength of these links stops you from stacking positions that are secretly the same macro bet.

**Entry/stop/target/management for a pairs trade.** Entry: spread z-score ≥ +2 → short the rich leg, long the cheap leg, beta-weighted. Stop: z-score ≥ +3.5 (the relationship may be breaking, not reverting) *or* a hard time stop of ~15 sessions. Target: z-score back to 0 (mean). Management: recompute the rolling correlation daily; if it drops below ~0.5, exit regardless of P&L — your hedge assumption is void.

## Confluence

Beta and correlation are strongest when combined with structure, not used in a vacuum:

- **With relative strength:** A high-beta name breaking out *while* its beta to a falling market is dropping suggests genuine idiosyncratic strength — a leadership candidate.
- **With breadth:** Rising market-wide correlation + narrowing advance-decline = a fragile, top-heavy rally. Falling correlation + broadening breadth = healthy trend.
- **With OI and options:** If you're short Nifty futures as a beta hedge, you can instead buy puts; delta then plays the role of a dynamic, non-linear beta. Understanding your book's beta tells you *how many* deltas of protection you need.
- **With sector rotation:** Track rolling beta of each sector index to Nifty. When defensives (FMCG, Pharma) see beta fall and cyclicals (Auto, Metal, Banks) see beta rise, the market is turning risk-on.

## Pitfalls

**Correlation is not causation, and it is not stable.** The number you compute is a *historical* snapshot. In calm markets correlations look moderate; in a crash they converge toward 1 — precisely when you were counting on diversification. Never size a book on placid-period correlations.

**Correlation only measures linear co-movement.** Two instruments can be strongly related in a curved or threshold way and show near-zero correlation. Options and non-linear payoffs are the obvious trap: a long straddle has essentially zero *linear* correlation to the underlying's direction while being enormously sensitive to its *magnitude*.

**Beta is noisy and regime-dependent.** A 20-day beta can read 1.4 one month and 0.8 the next for the same stock. Use it as a range, not a precise constant, and prefer 60–90 day windows for sizing. Also beware **beta from thin data** — illiquid mid-caps produce unreliable regressions because their stale prices understate true co-movement.

**Spurious correlation from trends.** Computing correlation on prices instead of returns manufactures fake relationships. Always de-trend by using returns.

**The single-benchmark illusion.** A stock's "beta to Nifty" hides that it may really be driven by USDINR, crude, or global rates. R² tells you how much the benchmark explains; a low R² (say 0.2) means beta is capturing only a sliver of the story and shouldn't be trusted as a hedge ratio.

**Overfitting pairs.** Data-mine 200 NSE names and you'll "find" beautiful historical pairs that were coincidences. Insist on an economic reason for the relationship (same sector, same driver) before trusting a correlation.

## Interview-ready summary

Correlation measures how reliably two return streams move together on a −1 to +1 scale; beta measures how much an instrument moves per unit move in a benchmark, and equals correlation times the ratio of volatilities. Both must be computed on returns, not prices, over a chosen lookback (60 days is the workhorse), and both are unstable — they drift with regime and converge toward 1 in crashes, which is why beta-weighted exposure, not rupee notional, is the honest measure of portfolio risk. Traders use them to hedge a book with beta-weighted index futures (sum beta-weighted exposure, short the matching number of Nifty lots), to size market-neutral pairs on stable-correlation NSE names like ICICI/Axis, and to read regime through rising or falling market-wide correlation. The discipline that separates professionals is watching the *rolling* series and treating every correlation as provisional: it is a description of the past, not a promise about the next crash.
