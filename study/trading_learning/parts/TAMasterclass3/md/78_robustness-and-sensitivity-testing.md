# Robustness & Parameter-Sensitivity Testing

## The concept

A backtest gives you one number from one path through history using one set of parameters. That single number is almost worthless on its own — not because it's wrong, but because it's fragile. The real question is never "how much did this system make?" but "**how much of what this system made was luck, and how would it hold up if the world had been slightly different?**" Robustness testing is the systematic answer to that question, and parameter-sensitivity testing is its most important sub-discipline.

The governing intuition is a physical one. Imagine your strategy's performance as a landscape where the horizontal axes are the parameters (lookback, stop multiple, threshold) and the vertical axis is profitability. A **robust** strategy sits on a broad, gentle *plateau*: nudge any parameter and performance barely changes. A **fragile, overfit** strategy sits on a lone, sharp *spike*: the optimal parameters are perched atop a peak surrounded by cliffs, so the tiny mis-estimation you will inevitably make — because the future's optimum won't be the past's — drops you off the edge into losses.

You want the plateau. Always the plateau. A system that makes ₹1.2 lakh at its exact optimum but ₹1.1 lakh across a wide band of nearby parameters is vastly more tradeable than one that makes ₹2 lakh at a razor's-edge optimum and −₹40,000 one setting away. The second system's ₹2 lakh is a mirage; you will never actually stand on that peak in live trading because you don't know where the future peak is.

Robustness testing extends this idea beyond parameters to *every* assumption baked into a backtest: the exact price path (Monte Carlo), the exact instrument (cross-market), the exact time period (regime slicing), the exact costs (stress testing), and the exact starting date (start-date sensitivity). A strategy is only trustworthy if it survives being poked, prodded and perturbed along all these dimensions.

## The methods and rules

**1. Parameter-sensitivity surfaces.** The centrepiece. Instead of reporting the single best parameter combination, you evaluate a grid and *visualise the whole surface*. For a two-parameter system you plot a heatmap; for one parameter, a curve. The rules for reading it:

- **Look for a plateau, not a peak.** Adjacent cells should have similar colours (similar performance).
- **Reject isolated optima.** If the best cell is surrounded by losing cells, discard it.
- **Trade the centre of the plateau, not the edge.** Pick parameters from the middle of the robust region, so drift in any direction stays on high ground.
- **Quantify it.** Compute the *neighbourhood degradation*: the average performance of the 8 cells surrounding your chosen cell divided by the chosen cell's performance. Above ~0.7 is robust.

**2. Monte Carlo on the trade sequence.** Your realised equity curve is one ordering of your trades. Was the modest drawdown luck? Reshuffle the trade returns thousands of times (bootstrap resampling, with or without replacement) and rebuild the equity curve each time. This yields a *distribution* of max drawdowns, final returns, and time-under-water. You then size for the 95th-percentile drawdown, not the one lucky path you happened to observe. A variant randomises *entry timing* by ±1 bar to test dependence on exact fills.

**3. Monte Carlo on the price path.** Rather than reshuffling trades, perturb the *data*: add small random noise to each bar (respecting OHLC and volatility structure), or bootstrap blocks of historical returns to synthesise alternative but statistically-similar price histories. Re-run the strategy on each. A robust system survives; a fragile one, tuned to the exact wiggles of the real path, falls apart.

**4. Start-date / window sensitivity.** Re-run the backtest starting from many different dates. If the system is profitable starting in Jan but a disaster starting in Mar, it's fragile to the arbitrary choice of start.

**5. Cross-market / cross-instrument validation.** A trend-following rule that works on Nifty *should* also show at least directional sanity on Bank Nifty, Fin Nifty, and liquid MCX contracts like crude or gold — not identical numbers, but the same *sign* of edge. If it only works on the one instrument you optimised on, suspect a fit.

**6. Cost and slippage stress.** Re-run with costs doubled and slippage tripled. Many "edges" are just unmodelled friction. This is decisive for Indian intraday systems where STT, GST, exchange charges and slippage can eat a whole edge.

**7. Regime slicing.** Partition history by regime — high vs low India VIX, trending vs ranging (ADX), bull vs bear years — and check the system in each. A strategy that only profits in one regime must be traded only in that regime, with a filter.

| Robustness test | What it perturbs | Pass criterion |
|---|---|---|
| Sensitivity surface | Parameters | Broad plateau; neighbourhood ratio > 0.7 |
| Trade-shuffle Monte Carlo | Trade ordering | 95th-pct DD survivable |
| Price-path Monte Carlo | The data itself | Edge persists across synthetic paths |
| Start-date sensitivity | Start date | Profitable across most start dates |
| Cross-instrument | The instrument | Same-sign edge on related markets |
| Cost stress | Frictions | Still profitable at 2× cost, 3× slippage |
| Regime slicing | Market regime | Positive or flat in each regime (or filtered) |

## A worked India example

Take a **mean-reversion system on Nifty 50 daily**: buy when price closes below its lower Bollinger Band (20-period, *k* std devs), exit when it closes back above the middle band; stop at *m*× ATR below entry. Two parameters we'll stress: the band width *k* ∈ {1.5, 2.0, 2.5, 3.0} and the ATR stop *m* ∈ {2, 3, 4, 5}. History: 2015–2026.

**Step 1 — sensitivity surface.** We build a 4×4 heatmap of CAGR/MaxDD (Calmar). Suppose it looks like this (Calmar values):

| k \ m | m=2 | m=3 | m=4 | m=5 |
|---|---|---|---|---|
| k=1.5 | 0.4 | 0.6 | 0.7 | 0.6 |
| k=2.0 | 0.9 | 1.3 | 1.4 | 1.3 |
| k=2.5 | 1.1 | 1.5 | 1.6 | 1.5 |
| k=3.0 | 0.8 | 1.2 | 1.3 | 1.2 |

The high ground is a **broad plateau** around k=2.5, m=3–4 (Calmar 1.5–1.6), with the whole k=2.0–3.0, m=3–5 block sitting comfortably above 1.2. This is exactly what you want. We pick the *centre* of the plateau — k=2.5, m=4 — not the single best cell, because if the future optimum drifts to k=2.0 or m=3 we're still on good ground. The neighbourhood ratio around (2.5, 4): average of its 8 neighbours ≈ 1.36, chosen cell 1.6 → ratio 0.85. Robust.

Contrast: if the surface had shown 1.6 at (2.5,4) but 0.3 at every neighbour, that lone spike would be a fit — rejected.

**Step 2 — trade-shuffle Monte Carlo.** The chosen config took, say, 84 trades over 11 years, realised max drawdown ₹63,000 on a ₹5-lakh notional (using ~2 lots of Nifty). We bootstrap 5,000 reshuffles of the 84 trade returns:

```python
import numpy as np
trades = np.array(trade_pnls)          # 84 realised P&Ls in rupees
dd95 = []
for _ in range(5000):
    path = np.random.choice(trades, size=len(trades), replace=True)
    equity = np.cumsum(path)
    peak = np.maximum.accumulate(equity)
    dd95.append((peak - equity).max())
print(np.percentile(dd95, 95))         # e.g. ₹1,04,000
```

The 95th-percentile drawdown is ₹1,04,000 — far worse than the ₹63,000 we actually saw. So we size off ₹1.04 lakh, not ₹63k. The realised path was on the lucky side.

**Step 3 — cost stress.** Re-run at 2× costs. Mean-reversion on daily bars trades infrequently, so the Calmar drops only from 1.6 to 1.4 — survives. (An intraday system would often collapse here; that's the value of the test.)

**Step 4 — regime slice.** Split by India VIX. The system earns most of its money in high-VIX periods (2020, 2022 spikes) when reversions are violent, and grinds sideways in calm bull years. Verdict: keep it, but recognise it's a volatility-harvesting engine — pair it with a trend system that earns in calm uptrends, so the portfolio has an all-weather profile.

**Step 5 — cross-instrument.** Applied unchanged to Bank Nifty and Fin Nifty, the same k=2.5, m=4 shows positive Calmar (1.1 and 0.9) — lower, but *same sign*. That's confirmation the edge is a genuine mean-reversion tendency in Indian index prices, not a Nifty-specific artefact.

## How to use robustness testing in a real workflow

Robustness testing sits *after* you have a candidate strategy and *before* you deploy — it's the final gauntlet. The disciplined sequence:

1. Develop and optimise the strategy (in-sample).
2. Validate with walk-forward and overfitting tests (previous two chapters).
3. **Build the sensitivity surface** and pick parameters from the centre of the plateau — never the peak.
4. **Monte Carlo the trades** to get the true drawdown distribution; size off the 95th percentile.
5. **Stress costs and slippage** at realistic Indian levels (full STT/GST/exchange charges plus 1–2 ticks slippage, doubled).
6. **Slice by regime** to know *when* the system works, and add a filter or a complementary strategy for the other regimes.
7. **Cross-check on related instruments** for same-sign edge.
8. Only a strategy that passes all of these earns live capital — and even then, at a fraction of the size the backtest tempts you toward.

In live operation, robustness testing also guides *degradation monitoring*: because you know the plateau and the Monte Carlo drawdown envelope, you can tell whether a live losing streak is within normal variation (still inside the 95th-percentile band) or a genuine breakdown (worse than any Monte Carlo path), which tells you whether to hold or halt.

## Pitfalls

- **Optimising *then* trading the peak.** The commonest error: people build the surface, admire the plateau, and then still trade the single best cell. Trade the centre.
- **Too fine a grid mistaken for robustness.** A plateau made of 50 nearly-identical over-tested cells can still be a broad fit. Keep grids coarse and economically motivated.
- **Monte Carlo with the wrong assumptions.** Reshuffling trades assumes independence; if your trades are serially correlated (e.g., a trend system that rides one big move across several trades), naive shuffling *understates* drawdown. Use block bootstrap instead.
- **Ignoring cost realism.** Testing a beautiful intraday scalper without STT, GST, exchange transaction charges, SEBI fees and slippage is self-deception — these can exceed the gross edge entirely.
- **Cross-instrument false comfort.** Nifty and Bank Nifty are highly correlated, so "it works on both" is weaker evidence than it feels; test genuinely different markets (an index vs a commodity vs USDINR) for stronger confirmation.
- **Regime-slicing into tiny samples.** Cut history too finely and each slice has too few trades to mean anything. Balance granularity against sample size.
- **Survivorship and look-ahead in the data itself.** No amount of robustness testing fixes a biased dataset; if your stock universe silently excludes delisted names, every test inherits the optimism.

## Interview-ready summary

Robustness and sensitivity testing answer the question a single backtest number can't: how much of the result is luck, and how would the system fare if the world had been slightly different. The centrepiece is the parameter-sensitivity surface — you evaluate a whole grid and demand a broad performance *plateau* rather than an isolated *spike*, then trade the centre of that plateau so inevitable parameter drift keeps you on high ground; a neighbourhood-degradation ratio above ~0.7 signals robustness. Around it sits a battery of perturbation tests: Monte Carlo reshuffling of the trade sequence to derive the true drawdown distribution and size off its 95th percentile rather than the one lucky realised path; Monte Carlo on the price data itself; start-date sensitivity; cross-instrument validation demanding at least same-sign edge on related markets like Bank Nifty, Fin Nifty and MCX; cost-and-slippage stress at doubled realistic Indian frictions; and regime slicing by India VIX or ADX to learn *when* the edge lives. A strategy earns live capital only after surviving all of these, and even then at conservative size. The recurring wisdom is to prefer the wide plateau over the tall peak, to size for the unlucky path you didn't get, and to remember that robustness testing bounds fragility but cannot conjure an edge that isn't there — it tells you how much to trust the edge you have.
