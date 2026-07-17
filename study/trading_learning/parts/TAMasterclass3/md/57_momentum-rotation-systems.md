# Momentum Rotation Systems

## Origin & idea

Momentum is the closest thing technical analysis has to a law of physics that survives peer review. In 1993, Jegadeesh and Titman published the paper that academics still cite: stocks that outperformed over the past 3–12 months continued to outperform over the next 3–12 months, and the losers kept losing. This "cross-sectional momentum" was not a quirk of one market — it showed up in the US, UK, Europe, Japan (weakly), emerging markets, and later in commodities, currencies and even at the level of whole country indices. It is one of the few effects that Eugene Fama, the father of efficient-markets theory, grudgingly called "the premier anomaly."

A rotation system is the practical machine built on top of that finding. Instead of asking "is this one stock going up?" you rank a whole universe by relative strength, hold the top slice, drop anything that falls out of the top, and rebalance on a fixed schedule. You are always renting the strongest horses and evicting the weak ones. The behavioural engine underneath is simple and durable: investors under-react to news (analysts anchor to old estimates, funds add to winners slowly over quarters), and they chase performance late (retail piles into last year's best fund). That combination creates a persistent drift that a disciplined rotation harvests.

The Indian context makes this especially attractive. The NSE gives you a clean, liquid, sectorally diverse universe — Nifty 50, Nifty 200, Nifty 500, plus tradable sector and thematic indices (Bank Nifty, Nifty IT, Nifty Auto, Nifty Pharma, Nifty FMCG, Nifty Metal, Nifty Energy, Nifty PSU Bank, Nifty Realty). India also runs pronounced sector cycles — PSU banks and metals rip in reflation phases, IT and pharma lead in risk-off and rupee-weakness phases, FMCG defends in drawdowns. A sector-rotation overlay captures the fact that at any time roughly two or three themes are doing the market's heavy lifting.

This chapter treats momentum rotation as a *system* — exact rules, sizing, costs and India-specific plumbing — not as a vibe.

## The two flavours: absolute vs relative momentum

You must be precise about which momentum you are trading, because they behave differently in a crash.

**Relative (cross-sectional) momentum** ranks assets *against each other*. You always hold the top N, whatever the market is doing. In a bear market this still forces you to hold "the best of a bad lot" — the stocks that fall the least. That is a real drawdown exposure.

**Absolute (time-series) momentum**, popularised by Gary Antonacci, asks a second question: is the asset beating cash (or a risk-free proxy) over the lookback? If not, you go to cash / liquid debt regardless of ranking. This is the crash filter. Antonacci's "Dual Momentum" combines both: pick the relatively strongest asset, but only stay invested if it also beats T-bills; otherwise sit in bonds.

For Indian retail, the dual-momentum logic maps cleanly: rank the Nifty sector indices by relative strength, but only deploy if the underlying (say Nifty 500) is above its own long-term trend / beating a liquid-fund proxy. In 2020 March and 2008, the absolute filter is what saved the account.

## Exact rules — a Nifty sector rotation system

Here is a concrete, tradable specification. This is a monthly system suitable for a cash/ETF account or an F&O overlay.

### Universe

| Component | Choice |
|---|---|
| Tradable sleeves | 11 NSE sector/theme indices via ETFs or index futures: Bank Nifty, Nifty IT, Nifty Auto, Nifty Pharma, Nifty FMCG, Nifty Metal, Nifty Energy, Nifty PSU Bank, Nifty Realty, Nifty Fin Services, Nifty Infra |
| Safe asset | Liquid BeES / overnight fund (absolute filter) |
| Benchmark | Nifty 500 TRI |

### Ranking signal

We rank each sleeve by a blended momentum score rather than a single lookback, because single lookbacks are noisy and get whipped around one earnings gap.

Momentum score = 0.4 × (3-month return) + 0.4 × (6-month return) + 0.2 × (12-month return), then divide the whole thing by the sleeve's realised volatility (risk-adjusted momentum). Dividing by volatility stops a single hyper-volatile sleeve (PSU Bank, Realty) from dominating purely because it moves a lot.

Formally, for sleeve *i*:

Score_i = [0.4·R_i(63d) + 0.4·R_i(126d) + 0.2·R_i(252d)] / σ_i(126d)

where R is simple total return over that many trading days and σ is annualised daily-return standard deviation.

### Entry / holding / exit rules

| Rule | Specification |
|---|---|
| Rebalance frequency | Last trading day of each month, execute next morning |
| Hold count (N) | Top 3 sleeves by Score |
| Weights | Equal weight (1/3 each) — or inverse-vol weight for lower drawdown |
| Absolute filter | Deploy a sleeve only if its own 6-month return > 0 AND Nifty 500 > its 200-DMA. Otherwise that slot goes to Liquid BeES |
| Buffer (anti-churn) | Hold a sleeve until it falls out of the top 5 (not top 3). New buys only from the top 3 |
| Skip-a-month | Compute returns to *last month-end minus one week* to sidestep short-term reversal |

The **buffer** is the single most important cost-saving rule. Without it, a sleeve oscillating between rank 3 and rank 4 gets bought and sold every month, bleeding brokerage and STT. With a top-3-in / top-5-out band, turnover roughly halves for a trivial performance cost.

The **skip-a-month** (or one-week skip) detail comes straight from the academic literature: the most recent few days of a winner tend to mean-revert, so momentum works better when you lag the signal slightly. It is a small edge but it is free.

## Worked India example

Assume it is the last trading day of a month. You compute scores for all 11 sleeves. Take a realistic snapshot:

| Sleeve | 3M ret | 6M ret | 12M ret | σ (ann.) | Raw blend | Score (÷σ) | Rank |
|---|---|---|---|---|---|---|---|
| Nifty PSU Bank | +24% | +41% | +78% | 34% | 33.6% | 0.99 | 1 |
| Nifty Metal | +18% | +30% | +40% | 28% | 27.2% | 0.97 | 2 |
| Nifty Realty | +20% | +33% | +55% | 36% | 32.2% | 0.89 | 3 |
| Nifty Auto | +12% | +22% | +34% | 22% | 20.4% | 0.93 | 4 |
| Nifty Fin Serv | +9% | +15% | +21% | 18% | 13.8% | 0.77 | 5 |
| Bank Nifty | +8% | +14% | +19% | 19% | 12.6% | 0.66 | 6 |
| Nifty Infra | +7% | +11% | +18% | 17% | 10.8% | 0.64 | 7 |
| Nifty Energy | +5% | +9% | +14% | 20% | 8.4% | 0.42 | 8 |
| Nifty IT | −2% | +3% | +8% | 21% | 2.2% | 0.10 | 9 |
| Nifty Pharma | +1% | +4% | +9% | 19% | 3.8% | 0.20 | 10 |
| Nifty FMCG | 0% | +2% | +6% | 13% | 2.0% | 0.15 | 11 |

Your top 3 are **PSU Bank, Metal, Realty**. Check the absolute filter: all three have 6-month returns well above zero, and assume Nifty 500 is comfortably above its 200-DMA (a clear reflation uptrend). All three slots deploy.

Say the account is ₹15 lakh. Equal weight: ₹5 lakh into each of PSU Bank ETF, a Nifty Metal ETF (or Metal basket / futures), and Realty exposure. You hold through the month.

Next month-end, IT and Pharma have started leading (rupee weakened, global risk-off), PSU Bank has cooled to rank 4, Metal to rank 2, Realty has fallen to rank 6. New scores:

- Metal: still rank 2 → **hold**.
- PSU Bank: rank 4 → still inside the top-5 buffer → **hold** (do not sell just because it left the top 3).
- Realty: rank 6 → outside top 5 → **sell**. Replace with the highest-ranked sleeve you don't own that is in the top 3 — say Nifty IT has jumped to rank 1. Buy IT.

So the only trade is Realty out, IT in — ₹5 lakh rotated. That is the whole month's activity. This low turnover is what makes the system survivable after costs.

Now imagine a month where Nifty 500 breaks below its 200-DMA and most sleeves show negative 6-month returns. The absolute filter kicks in: sleeves failing the filter are replaced by Liquid BeES. In a full bear you could be 100% in liquid fund, sitting out the crash — earning ~6–7% annualised in an overnight fund while the index halves. That is the dual-momentum insurance premium paying off.

## How to trade the mechanics on NSE

**Vehicles.** For the cash version, use sector ETFs where liquidity is decent (Bank Nifty ETF, PSU Bank ETF, IT ETF, and the broad-index ETFs). Where a sector has no liquid ETF, either build a 5-stock representative basket from the index's top weights, or use index futures for the F&O-eligible ones (Bank Nifty, Fin Nifty, Nifty). Thin ETFs quote wide — always check the NSE-published iNAV and never cross a spread wider than ~0.3% without a limit order.

**F&O overlay.** Instead of buying ETFs, express the top-3 tilt with futures on Bank Nifty / Fin Nifty and options structures on the rest. The advantage is capital efficiency (margin, not full notional); the danger is leverage turning a normal 12% momentum drawdown into a margin call. If you overlay with futures, size so that total notional ≤ 1.5× capital, never more. Roll futures on the Thursday-before-expiry monthly cadence, which conveniently aligns with a monthly rebalance.

**Execution timing.** Signals are computed on close; execute at the next open or in the first 30 minutes using limit orders. Do not execute in the last 15 minutes when closing auctions distort prints.

## Backtest / edge notes & realistic costs

On Indian data, a monthly sector-rotation top-3 system with the absolute filter has historically delivered a meaningful improvement in risk-adjusted return over buy-and-hold Nifty — think of it as capturing most of the index's upside while cutting the worst drawdowns via the cash filter. But be honest about three things.

**Costs are the killer of naive momentum.** Every rotation incurs: brokerage (₹20/order flat on discount brokers), STT (0.1% on delivery sell side, 0.0125% on futures sell), exchange txn charges, GST on brokerage, stamp duty (0.015% buy), and — the real cost — bid-ask slippage on thin ETFs. A monthly system trading roughly one sleeve per month has annual turnover around 100–150%. At a realistic all-in round-trip cost of 0.30–0.50% per rotated leg, that is roughly 0.5–1.0% per year of drag. The buffer rule and monthly (not weekly) cadence are what keep this from eating the entire premium. Weekly rotation on Indian sector ETFs is usually *cost-negative* — do not do it.

**Momentum crashes.** The ugly feature of momentum is that it does not fail gently — it fails violently at sharp trend reversals. When a beaten-down group (PSU banks in 2020–21, or any "junk rally" off a bottom) rockets while yesterday's winners lag, a relative-momentum book gets run over for a few weeks. Daniel and Moskowitz documented these "momentum crashes." The volatility-scaling in the score and the absolute filter both soften this, but nothing removes it. Expect 2–3 nasty months per decade.

**Small samples lie.** India has fewer decades of clean, survivorship-bias-free sector data than the US. A backtest showing a beautiful equity curve on 8 years is not proof of a 20-year edge. Insist on out-of-sample and paper-trade a quarter before committing size.

## Confluence — making it robust

Momentum rotation improves when you layer secondary confirmation rather than trusting rank alone:

- **Breadth confirmation:** only take a sleeve if its own advance-decline / percent-above-50-DMA is healthy. A sector that ranks high on price but has narrow internals (two stocks carrying the index) is fragile.
- **Relative-strength line vs Nifty:** the sleeve's RS line making new highs, not just absolute price, confirms genuine leadership.
- **Regime overlay:** in a confirmed downtrend, shift N from 3 to 2 and raise the cash weight — thin your exposure when the whole board is momentum-hostile.

## Pitfalls

- **Over-fitting lookbacks.** If you tune weights until the backtest is gorgeous, you have curve-fit. Use round, defensible parameters (3/6/12) and accept a plainer curve.
- **Ignoring liquidity.** Ranking a thin thematic index highly and then being unable to exit ₹5 lakh without moving it 1% is a real, recurring loss. Pre-screen for ETF/futures liquidity.
- **Rebalancing on emotion.** The system's edge *is* the discipline. Skipping a rotation because "PSU banks feel toppy" turns a system back into discretionary trading.
- **Whipsaw at regime turns.** The month the market flips, you will buy the new leaders late and sell old leaders late — that is structural. Do not "fix" it by trading more often; that makes it worse.
- **Tax drag.** In a taxable account, monthly rotation generates short-term capital gains (15% on equity/ETF held <12 months, taxed at your applicable STCG rate in 2026). Model this — it can be the largest single cost.

## Interview-ready summary

Momentum rotation systematises the best-documented anomaly in markets — the tendency of recent winners to keep winning over 3–12 months. A rotation system ranks a universe (for India, the 11 NSE sector/theme indices) by a blended, volatility-scaled momentum score, holds the top 3, uses a top-3-in/top-5-out buffer to cut turnover, lags the signal by a week to dodge short-term reversal, and applies an absolute (dual-momentum) filter — deploy only if the sleeve beats zero and the broad market is above its 200-DMA, otherwise rotate to a liquid fund. On NSE you express it via sector ETFs or Bank Nifty / Fin Nifty futures, rebalancing monthly around expiry. The edge is real but fragile: it is destroyed by high turnover and costs (hence monthly, not weekly, plus the buffer), it suffers episodic "momentum crashes" at sharp reversals, and it carries STCG tax drag. The honest pitch: a disciplined monthly sector rotation captures most of the index's upside with materially smaller crash drawdowns, provided you respect costs, liquidity and the absolute filter — and provided you never override it on a hunch.
