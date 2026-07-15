# Systematic Strategy Families

## Why this matters

Retail traders collect setups; pros collect *strategy families* and the regimes each one survives in. A candlestick pattern or an RSI cross is a signal — a strategy family is a whole philosophy about *why* an edge exists and *when* it stops working. You already know how to read a chart and price an option. What separates a professional systematic trader is knowing that there are only about half a dozen durable sources of edge, that each one is really a bet on market *regime*, and that running the wrong family in the wrong regime is how accounts die slowly. Indian markets are not the S&P 500: Nifty and Bank Nifty trend hard in some years and chop violently in others, single stocks gap on results, and liquidity is concentrated in a handful of names. Picking the family that fits the instrument and the regime is 80% of the job.

## The essentials

There are six workhorse families. Each is a bet on a different statistical property of returns.

| Family | Core bet | Signal example | Works when | Dies when | India fit |
|---|---|---|---|---|---|
| Trend-following | Prices auto-correlate over weeks/months | Price > 200-DMA; 50/200 cross | Strong directional regimes | Range-bound chop | Nifty/Bank Nifty index futures, commodity (MCX crude, gold) |
| Momentum (cross-sectional) | Recent winners keep winning vs peers | Rank Nifty 100 by 6-mo return, long top decile | Broad dispersion | Sharp reversals/junk rallies | Nifty 500 stock universe, monthly rebalance |
| Mean-reversion | Short-term over-extension snaps back | RSI(2) < 10 near support | Range/high-liquidity regimes | Trending breakouts, news gaps |Index intraday, large-cap stocks |
| Breakout | Range expansion continues | Close above 20-day high (Donchian) | Volatility expansion | False-break chop | Bank Nifty, stock futures on results |
| Pairs / stat-arb | Two related prices revert to a spread | Z-score of spread > 2 | Stable relationships | Structural break (one name re-rates) | HDFCBANK/ICICIBANK, TCS/INFY, PSU banks |
| Volatility | Vol is mean-reverting & has a risk premium | India VIX percentile, IV vs realised | Vol clustering | Vol regime shifts | Options on Nifty (covered in the options book) |

Two India-specific realities shape all of this. First, **cost drag is brutal**: STT (from 01-Apr-2026: equity intraday 0.025% on sell, futures ~0.05% on sell, options ~0.15% on premium sell), plus exchange txn charges, 18% GST on brokerage+txn, stamp duty and SEBI fees. A mean-reversion system that trades 200 times a month can have a real edge on paper and still lose after costs. Trend and cross-sectional momentum trade rarely, so they survive costs far better. Second, **regimes flip**: 2021 and 2023 rewarded trend; 2022 and much of 2018-19 punished it and rewarded mean-reversion. Pros run *multiple* uncorrelated families so that the drawdown of one is funded by another (next chapter).

A simple cointegration idea for pairs: two stocks A and B are *cointegrated* if some linear combination `A − β·B` is stationary (mean-reverting) even though A and B each wander. You estimate β by regressing A on B (hedge ratio), form the spread, standardise it to a z-score, and trade the z-score back to zero. You are not betting on direction — you are betting the *relationship* holds. The danger is a structural break: if one bank gets an RBI action or a merger (think HDFC twins in 2023), the spread never reverts and you bleed.

*All rules and rates as of July 2026 — verify on NSE / your broker / SEBI, because they change.*

## Worked example

**Mean-reversion, Nifty 50 index (spot 24,000 basis, one lot future = 25 units, tick ₹0.05).** Rule: on the daily chart, buy one Nifty future when RSI(2) closes below 10 *and* price is above the 200-DMA (only fade dips in an uptrend); exit when the close is back above the 5-DMA. Suppose Nifty dips to 23,650, RSI(2) prints 8, 200-DMA is 22,900 — trade is on. Entry 23,650; two days later it closes at 23,880 above the 5-DMA — exit.

- Gross move: 230 points × 25 = **₹5,750** per lot.
- Costs (round trip, indicative): STT on futures sell 0.05% of (23,880×25=₹5,97,000) ≈ **₹298**; brokerage ₹20+₹20 = ₹40; exchange txn ~0.0019% both sides ≈ ₹22; GST 18% on (₹40+₹22) ≈ ₹11; stamp ~0.002% buy ≈ ₹12; SEBI ~₹1. Total ≈ **₹384**.
- Net ≈ **₹5,366** per lot. Margin blocked ~₹1.2–1.4 lakh, so ~4% on margin in two days — but only because RSI(2)<10 with a 200-DMA filter is genuinely rare (a handful of trades a month). Strip the trend filter and you catch falling knives.

**Momentum rule (cross-sectional).** Universe = Nifty 100. Monthly: rank stocks by their trailing 6-month return *skipping the last 21 days* (the skip avoids short-term reversal). Go long an equal-weighted basket of the top 10, hold one month, rebalance. This trades ~12 times a year per slot, so STT/GST barely dents it. In India this has historically beaten buy-and-hold in dispersion-rich years but suffered "momentum crashes" when beaten-down junk rips (e.g., recovery months). The skip-month and a simple market-regime filter (only run it when Nifty > 200-DMA) tame the worst crashes.

## How pros do it / common mistakes

- **Pros match family to instrument and cost.** High-turnover mean-reversion goes on low-cost, high-liquidity index futures — never on illiquid mid-caps where slippage eats the edge.
- **They add a regime filter, not more indicators.** One filter (200-DMA, or VIX percentile) that switches a family on/off beats stacking five oscillators.
- **They diversify across families.** Trend + mean-reversion are naturally negatively correlated; running both smooths the equity curve.
- **Classic retail errors:** running mean-reversion into a trend ("it's oversold" all the way down); backtesting a pairs trade over one stable window and ignoring the break risk; ignoring costs so an intraday scalp that "wins" on the chart loses in the ledger; and curve-fitting RSI thresholds to one year of Nifty data.
- **Red flags:** an edge that only appears with fees set to zero; a pair whose cointegration p-value is borderline; a breakout system with a >60% false-break rate on the chosen instrument.

## Checklist / drill

Before deploying any systematic strategy, answer:

1. Which **family** is this, and what statistical property is the bet?
2. In which **regime** does it make money, and what filter turns it off otherwise?
3. Does the edge survive **real Indian costs** (STT dated 01-Apr-2026, GST, exchange, stamp) at my turnover?
4. Is the **instrument liquid** enough that slippage < edge? (Prefer index futures / top F&O names.)
5. For pairs: is the pair **cointegrated out-of-sample**, and what's my break-risk stop?

**Drill:** Take 3 years of daily Nifty data. Code the RSI(2)<10 + above-200-DMA long rule, then the same rule *without* the 200-DMA filter. Compare number of trades, win rate, and net-of-cost P&L. Seeing the filter turn a losing system into a profitable one — purely by respecting regime — is the lesson.
