# Sector Rotation Models & RS Ranking

Money does not lift every boat at the same time. On any given month a handful of NSE sectoral indices carry the market while the rest bleed or drift. In 2020–21 it was IT and Pharma; in 2022 it was PSU Banks, Capital Goods and Defence; in 2023–24 it was Realty, PSUs and Auto; through corrections it is FMCG and Pharma that hold. If you can identify *where* the institutional money is flowing and rank stocks by how strongly they lead, you stop fighting the tape and start riding it. This chapter builds a working sector rotation and relative-strength (RS) ranking system for Indian markets — the models, the formulas, the ranking table, and the discipline to trade it.

## What sector rotation is & the logic

Sector rotation is the observable tendency of capital to move between industry groups in a roughly repeatable sequence tied to the economic and liquidity cycle. The logic is simple: large funds cannot exit and re-enter positions daily, so they *tilt* — overweighting sectors they expect to outperform and underweighting the rest. Those tilts leave footprints in price: a sector index that keeps making higher highs while Nifty consolidates is absorbing inflows; one that fails to bounce when Nifty rallies is being distributed.

Two distinct engines drive rotation in India:

**1. The macro/economic cycle.** Classic sector rotation theory (Sam Stovall's model) maps sectors to phases: early-cycle recovery favours rate-sensitives (Banks, Auto, Realty); mid-cycle favours Industrials, Capital Goods, Metals; late-cycle favours Energy and Commodities; slowdown favours defensives (FMCG, Pharma, IT as a USD hedge). India follows this loosely but with local twists — a rate-cut cycle by the RBI lights up Banks and NBFCs; a capex/infra budget lights up L&T, Capital Goods and Cement; a weak rupee lights up IT and Pharma exporters.

**2. The liquidity/flow cycle.** FII and DII flows dominate short-to-medium rotation. When FIIs sell aggressively, high-beta and FII-heavy sectors (Private Banks, IT) underperform, and DII-supported domestic themes (Capital Goods, PSU, Defence, Railways) lead. This "FII-out, DII-in" divergence has been the single most important rotation signal in 2022–2025.

The trader's job is not to forecast the cycle perfectly. It is to *measure* which sectors are strong **right now** using relative strength, confirm the money flow, and concentrate longs in leaders and shorts (or avoidance) in laggards.

## Construction & reading — the RS ranking engine

Relative Strength here means **price ratio**, not RSI. The core object is the ratio line:

```
RS ratio = Sector Index / Benchmark (Nifty 50)
```

If Nifty IT / Nifty 50 is rising, IT is outperforming — regardless of whether IT is going up or down in absolute terms. A rising RS line in a falling market means IT is falling *slower*; that is still leadership and often marks the next up-leg's winner.

### Building a rankable RS score

A single ratio line is visual; to rank 15 sectors you need a number. The cleanest field-tested metric is **RS-Momentum**, a blend of multiple lookback returns relative to the benchmark. Compute for each sector index:

```
RelReturn(n) = [ SectorReturn(n) − NiftyReturn(n) ]   for n = 21, 63, 126 days
RS Score = 0.4 × RelReturn(21) + 0.35 × RelReturn(63) + 0.25 × RelReturn(126)
```

The weights front-load the recent quarter (21 ≈ 1 month, 63 ≈ 3 months, 126 ≈ 6 months) so the rank turns fast enough to be tradable but not so fast it whipsaws. Rank all sectors high-to-low; the top quartile are your hunting grounds, the bottom quartile your avoid/short list.

### The Nifty sectoral universe to rank

| Index | Character | Primary driver |
|---|---|---|
| Nifty Bank | High weight, rate-sensitive | RBI policy, credit growth, FII flows |
| Nifty Financial Services | Banks + NBFCs + insurers | Rates, asset quality |
| Nifty IT | Export/USD play, defensive | USDINR, US tech spend, deal wins |
| Nifty Auto | Cyclical, consumption | Rural demand, festive season, rates |
| Nifty FMCG | Defensive, low beta | Rural demand, input costs, monsoon |
| Nifty Pharma | Defensive + USD | US generic pricing, USFDA |
| Nifty Metal | Global cyclical | China demand, LME, USD |
| Nifty Realty | High beta, rate-sensitive | Rates, launches, absorption |
| Nifty Energy | Large-cap, oil-linked | Crude, refining margins |
| Nifty PSU Bank | High beta, government | Credit, provisioning, capex cycle |
| Nifty Consumer Durables | Discretionary | Consumption, rates |
| Nifty Media | Small, illiquid, high beta | Ad spend, sentiment |
| Nifty Infra / CPSE / PSE | Capex/government theme | Budget, order books |

### Reading the RRG (Relative Rotation Graph)

The most powerful *reading* tool is the Relative Rotation Graph, available on TradingView-style platforms and StockEdge. It plots two axes:

- **X-axis: RS-Ratio** (relative strength level vs Nifty)
- **Y-axis: RS-Momentum** (rate of change of that RS)

This creates four quadrants that sectors rotate through clockwise:

| Quadrant | Meaning | Action |
|---|---|---|
| **Leading** (top-right) | Strong RS, positive momentum | Hold / ride winners |
| **Weakening** (bottom-right) | Strong RS, momentum fading | Trail stops, book partials |
| **Lagging** (bottom-left) | Weak RS, negative momentum | Avoid / short |
| **Improving** (top-left) | Weak RS, momentum turning up | Watchlist — the *next* leaders |

The tradable edge is the **Improving → Leading** transition. A sector crossing from bottom-left into top-left with a lengthening tail heading to the right is a sector where fresh accumulation has begun before the crowd notices.

## Worked India example

**Setting: a rate-cut expectation window, early 2025.** The RBI has signalled the end of its hiking cycle; inflation is cooling; a capex-heavy Union Budget has just passed. You run the RS Score on 1 February.

Assume these relative returns (sector return minus Nifty return, in %):

| Sector | Rel 21d | Rel 63d | Rel 126d | RS Score | Rank |
|---|---|---|---|---|---|
| Nifty PSU Bank | +6.2 | +9.1 | +14.0 | +9.16 | 1 |
| Nifty Realty | +5.5 | +7.8 | +10.2 | +7.48 | 2 |
| Nifty Capital Goods/Infra | +4.1 | +6.0 | +9.5 | +6.13 | 3 |
| Nifty Auto | +3.0 | +4.2 | +5.1 | +3.95 | 4 |
| Nifty Bank | +2.1 | +2.8 | +3.0 | +2.57 | 5 |
| Nifty Metal | +0.5 | −1.0 | +2.0 | +0.35 | 6 |
| Nifty Pharma | −1.2 | −0.5 | +1.0 | −0.41 | 7 |
| Nifty FMCG | −2.0 | −3.1 | −2.5 | −2.51 | 8 |
| Nifty IT | −4.5 | −6.0 | −7.2 | −5.70 | 9 |

**Interpretation.** Rate-sensitives (PSU Bank, Realty) and the capex theme (Capital Goods) lead — exactly what a rate-cut-plus-capex regime predicts. Defensives (FMCG) and the USD-play (IT) lag, telling you the market is in "risk-on, domestic-cyclical" mode. On the RRG, PSU Bank sits deep in Leading, Realty in Leading with a long tail, and Auto is crossing Improving → Leading.

**Trade construction.** You concentrate longs in the top three sectors, then drill into the *strongest stock inside the strongest sector* (RS applied at stock level too). Inside Nifty PSU Bank you screen for the constituent with the best RS Score and a clean chart breaking out — say the index heavyweight making a fresh 52-week high on volume. You size heaviest in rank-1 sector leaders, lighter in rank-3, and you *do not* buy IT or FMCG dips no matter how "cheap" they look, because RS says they will underperform. If you must hedge, a pairs idea writes itself: **long PSU Bank basket / short Nifty IT**, which profits from the rotation itself and is market-neutral if Nifty chops.

**Follow-through.** Three weeks later Auto has moved into Leading and PSU Bank's momentum is flattening (drifting toward Weakening). You trail stops on the PSU Bank longs, rotate freed capital into the newly-confirmed Auto leaders, and keep re-ranking weekly. That is the whole engine: rank, concentrate in leaders, rotate as the RRG turns.

## How to use it for bias & timing

**Weekly cadence, daily awareness.** Re-run the RS ranking every weekend. Sector leadership does not change intraday; a weekly rank keeps you in the dominant theme without overtrading. Use daily charts only to *time entries* into stocks that already sit in top-ranked sectors.

**Top-down funnel.** The correct order is: (1) Is Nifty in an uptrend? (regime filter) → (2) Which sectors rank top-quartile? → (3) Which stocks inside those sectors have the best individual RS and a clean setup? → (4) Time the entry with your usual trigger (breakout, pullback to 20-EMA, etc.). Never invert this. Buying a great chart in a bottom-ranked sector is swimming against the flow.

**Bias in trending vs range markets.** In a strong Nifty uptrend, trade *only* the top 2–3 sectors long and ignore the rest — leadership is narrow and rewards concentration. In a choppy Nifty, rotation becomes a *pairs* game: long the top-ranked sector index/ETF, short the bottom-ranked, capturing the spread while staying market-neutral.

**Timing turns with RRG tails.** The lengthening of a tail signals accelerating momentum; a curling tail signals a stall. A sector whose tail is curling down inside Leading is where you take profits early — leadership is about to pass. A sector with a long tail rising out of Lagging into Improving is your watchlist for the next 4–6 weeks.

**Confirm with flow.** Cross-check the ranking against FII/DII cash-flow data and sector-specific news. If PSU Bank ranks #1 *and* DIIs are net buyers *and* the RBI just turned dovish, the signal is high-conviction. If a sector ranks high purely on one gap-up news day, treat it as suspect — RS built on a single candle is fragile.

## Pitfalls

**RS is relative, not absolute.** A sector can rank #1 and still fall in a bear market — it is just falling *less*. In a Nifty downtrend, top-ranked sectors are for *reducing losses / shorting less*, not for aggressive fresh longs. Always gate the ranking behind a Nifty regime filter (e.g., Nifty above its 200-DMA and 20-week EMA).

**Chasing rank-1 at the top.** By the time a sector is unambiguously #1 with a screaming chart, much of the move is done. The higher-expectancy entry is the *Improving* sector before it becomes the obvious leader. Buying the most extended leader after a 40% run is how rotation traders get caught in the Weakening-quadrant reversal.

**Overfitting the lookbacks and weights.** The 21/63/126 blend is robust, but do not curve-fit weights to last year's winners. A model that only worked because it was tuned to the 2023 PSU rally will fail in the next regime. Keep the weights fixed and let the ranking adapt.

**Whipsaw in low-conviction chop.** When Nifty is directionless, sector ranks reshuffle weekly and RRG tails coil in the centre with no clear rotation. That is a signal to *reduce activity*, not to force rotation trades. Rotation edges are strongest when there is a clear macro driver (rate cut, budget, rupee move).

**Liquidity trap in small sector indices.** Nifty Media and some thematic indices are thin. A high RS rank driven by two illiquid stocks is untradeable at size — you cannot enter or exit cleanly. Weight your capital toward liquid, deep sectors (Bank, IT, Auto, FMCG, Pharma, Metal) and treat thin thematic ranks as information, not tradable signals.

**Index composition drift.** Sectoral indices get rebalanced; a stock's exit or a new heavyweight's entry can distort the RS line. Know the top 3–4 constituents of each index you rank — Nifty Bank is dominated by a couple of private-bank giants, so "Nifty Bank strength" is often just those names, not the whole sector.

## Interview-ready summary

- **Sector rotation** is the cyclical movement of capital between industry groups; it is driven in India by the macro cycle (rate cuts → Banks/Realty; capex budget → Capital Goods; weak rupee → IT/Pharma) and, more powerfully in recent years, by the **FII-out/DII-in flow divergence** that favours domestic-cyclical and PSU themes.
- **Relative Strength** for ranking means the **price ratio** (Sector/Nifty), *not* RSI. A rising ratio = outperformance even in a falling market.
- The rankable metric is an **RS Score** blending 21/63/126-day relative returns (weights 0.40/0.35/0.25); rank all Nifty sectoral indices and concentrate in the **top quartile**.
- The **RRG** plots RS-Ratio vs RS-Momentum into four quadrants (Leading, Weakening, Lagging, Improving) that rotate clockwise; the tradable edge is the **Improving → Leading** transition — the *next* leaders, not the obvious ones.
- Use a strict **top-down funnel**: Nifty regime → top sectors → strongest stocks inside them → time the entry. Never buy a good chart in a bottom-ranked sector.
- **Gate everything behind the Nifty regime**: RS is relative, so top rank in a bear market means "fall less / short-less," not "buy aggressively."
- Key pitfalls: chasing rank-1 at the top, curve-fitting weights, whipsaw in chop, and thin-index liquidity traps. Re-rank weekly, confirm with FII/DII flows, and rotate as RRG tails turn.
