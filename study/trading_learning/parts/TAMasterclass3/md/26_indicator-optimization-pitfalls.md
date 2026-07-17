# Indicator Optimization & Its Pitfalls

Somewhere on the road from "TA hobbyist" to "systematic trader" sits a trap that has ruined more accounts than any single chart pattern: **optimization.** You build a strategy — say, an RSI mean-reversion system on Bank Nifty — and you notice that RSI(14) with a 30/70 threshold made ₹40,000 last year. Then you wonder: what if I tried RSI(9)? RSI(11)? What about buying at 28 instead of 30? You run the numbers, and lo — RSI(11) buying at 27 and selling at 74 would have made **₹2,10,000.** You feel like a genius. You size up. And over the next six months the "optimised" system quietly gives most of it back, while the boring RSI(14) you abandoned holds up.

This chapter is a **quant** chapter about *why that happens* and how to defend against it. Optimization is not evil — professional quant desks optimise constantly. What kills retail traders is **naïve, in-sample, over-parameterised optimization with no out-of-sample validation and no accounting for the statistics of searching.** We'll cover the concept precisely, the maths of why more parameters guarantee a better-looking-but-worse system, a worked India example with a walk-forward test, code for a proper validation loop, and an unsentimental list of what actually works.

## The concept

**Optimization** = searching over a strategy's free parameters (indicator lengths, thresholds, stop distances, filter values) to find the combination that maximises some objective (net profit, Sharpe ratio, profit factor) on historical data.

The problem is that historical price data contains two things mixed together:

- **Signal** — genuine, repeatable structure (trends persist somewhat; volatility clusters; overreactions partly mean-revert).
- **Noise** — random, unrepeatable accidents of that particular sample (this Tuesday's gap, that expiry's squeeze).

When you optimise, you have no way to tell the algorithm "fit the signal, ignore the noise." It fits **both.** And the more parameters you give it and the more combinations you try, the more of the *noise* it captures — noise that, by definition, will not repeat. This is **overfitting** (also called curve-fitting), and it is the central pitfall of all quantitative TA.

The cruel part: an overfit system looks *better* the more overfit it is. Backtest profit rises monotonically as you add parameters and search harder. So your headline metric actively rewards the very behaviour that destroys live performance. You cannot detect overfitting by looking at in-sample results at all — you must hold data back.

## The maths of why optimization overstates edge

### More parameters → guaranteed better fit to noise

Think of it geometrically. With `k` free parameters you can fit a `k`-dimensional surface to the data. A famous quip (attributed to von Neumann): *"With four parameters I can fit an elephant, and with five I can make him wiggle his trunk."* Every extra knob lets the system contort itself to hug the specific past path, including its noise.

Formally, if the true edge per trade is `μ` and the noise has standard deviation `σ`, then over `N` trades the realised in-sample average is `μ + (sampling noise)`. When you **select the best of `M` tried parameter sets**, you are taking a maximum over `M` noisy estimates. The expected value of that maximum is inflated above the true best by roughly:

```
Inflation ≈ σ / √N × E[max of M standard normals]
```

and `E[max of M standard normals]` grows with `√(2 ln M)`. So:

```
Selection bias ≈ (σ / √N) × √(2 ln M)
```

Read what this says. The apparent edge you "discover" is inflated by an amount that **grows with the number of combinations you try (`M`)** and **shrinks with the number of trades in your sample (`N`).** Try 10,000 parameter combos (a trivial grid search: 100 lengths × 100 thresholds) on a sample of 60 trades, and the selection bias term alone can manufacture a large "edge" out of pure randomness. This is why a hard grid search over a short history is almost guaranteed to hand you a beautiful, worthless system.

### Deflated Sharpe & the multiple-testing problem

The same logic applies to Sharpe ratio. If you test many strategies/parameters and report the best Sharpe, that Sharpe is upward-biased. The **Deflated Sharpe Ratio** (Bailey & López de Prado) formalises the correction: it discounts your best observed Sharpe by how many trials you ran and how non-normal the returns are. The practical takeaway needs no formula: **every parameter combination you test is a lottery ticket; report the winner without adjusting for how many tickets you bought, and you are lying to yourself.**

### Degrees of freedom vs. data

A rough sanity rule: you need **far more independent trades than free parameters** — a common heuristic is at least 30–50 trades *per parameter*, and more for noisy data. A 4-parameter system validated on 40 trades is fitting noise. A 1-parameter system validated on 500 trades might mean something.

## Worked India example — RSI mean-reversion on Bank Nifty

Let's make the trap concrete, then defeat it.

**The naïve approach (in-sample optimization).** We take Bank Nifty daily data for **2023** and a simple system: buy when RSI(len) < lower, exit when RSI(len) > upper. We grid-search:

- `len` ∈ {7, 9, 11, 14, 21} (5 values)
- `lower` ∈ {20, 25, 30, 35} (4 values)
- `upper` ∈ {60, 65, 70, 75} (4 values)

That's 5 × 4 × 4 = **80 combinations** tested on one year (~30–40 trades). The grid's winner comes out as, say, **RSI(9), buy < 25, sell > 65**, showing a backtested **profit factor of 2.4** and a tidy equity curve. The temptation is overwhelming: deploy it.

**Why it's a mirage.** With M = 80 trials and only ~35 trades, the selection-bias term `(σ/√N)·√(2 ln M)` is large. RSI(9)/25/65 didn't win because it captures a real Bank Nifty tendency more than RSI(14)/30/70 does — it won because its noise happened to line up with 2023's specific accidents. Nothing forces those accidents to recur in 2024.

**The disciplined approach — walk-forward / out-of-sample.**

1. **Split the data.** In-sample (IS) = 2023. Out-of-sample (OOS) = 2024 (data we never touch during optimization).
2. **Optimise on IS only.** Find the best combo on 2023 → RSI(9)/25/65 (PF 2.4 in-sample).
3. **Test that frozen combo on OOS 2024.** No re-tuning. Suppose it delivers **PF 1.15** and a much choppier curve. That collapse from 2.4 → 1.15 is the size of the overfit. The *honest* expectation of live performance is the OOS number, **1.15**, not 2.4.
4. **Compare to a robust baseline.** The un-optimised RSI(14)/30/70 might show IS PF 1.5 and OOS PF 1.4 — *lower in-sample but far more stable across the split.* The parameter set whose performance barely changes between IS and OOS is the one to trust, even though it "looks worse" on the training year.

**The lesson in one line:** the goal of optimization is **not** to find the highest backtest number — it is to find the parameter *region* that is **robust**, i.e. performs similarly across time periods and across nearby parameter values.

### The parameter-plateau test

A powerful, cheap robustness check: plot the objective across the parameter grid and look at the *shape*, not the peak.

| Pattern | Interpretation |
|---|---|
| Sharp, isolated spike — one combo brilliant, neighbours poor | **Overfit.** RSI(9) makes ₹2L, RSI(8) and RSI(10) lose. This is noise. Reject. |
| Broad plateau — a whole region performs similarly well | **Robust.** RSI 10–16 all make decent money. Pick the *centre* of the plateau (~13), not the peak. |

If tweaking a length by 1 or a threshold by 2 collapses performance, you have found noise, not edge. Real market tendencies are not that fragile.

## Code — a proper walk-forward validation loop

```python
import pandas as pd, numpy as np, itertools

def rsi(close, n):
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    return 100 - 100/(1 + up/dn)

def backtest(df, length, lower, upper, cost=0.0004):
    r = rsi(df.close, length)
    pos, entry, pnl = 0, 0.0, []
    for i in range(len(df)):
        if pos == 0 and r.iloc[i] < lower:
            pos, entry = 1, df.close.iloc[i]
        elif pos == 1 and r.iloc[i] > upper:
            ret = (df.close.iloc[i] - entry)/entry - 2*cost  # both-side cost
            pnl.append(ret); pos = 0
    pnl = np.array(pnl)
    if len(pnl) < 5: return -np.inf, len(pnl)
    pf = pnl[pnl>0].sum() / max(1e-9, -pnl[pnl<0].sum())
    return pf, len(pnl)

# --- Walk-forward: optimise on IS, report ONLY on OOS ---
IS, OOS = df["2023"], df["2024"]

grid = itertools.product([7,9,11,14,21], [20,25,30,35], [60,65,70,75])
best, best_pf = None, -np.inf
for L, lo, up in grid:                         # search happens on IS ONLY
    pf, n = backtest(IS, L, lo, up)
    if pf > best_pf: best_pf, best = pf, (L, lo, up)

is_pf, _   = backtest(IS,  *best)
oos_pf, no = backtest(OOS, *best)              # frozen params, unseen data
print(f"Best IS params {best}: IS PF={is_pf:.2f}  ->  OOS PF={oos_pf:.2f} ({no} trades)")
# TRUST oos_pf. If IS>>OOS, you overfit. A robust system has IS ~ OOS.
```

The single most important line is the comment: **trust the OOS number.** Everything before it is where overfitting hides; the OOS test is the only honest read. Note the explicit `cost` term — a system that only survives at zero cost is already dead on NSE, where brokerage, STT (higher on the sell side), exchange fees, GST, stamp duty, and spread/slippage all bite, and bite hardest on options.

## How to use optimization safely in a real TA workflow

1. **Hold out data before you start.** Reserve the most recent chunk (or several folds) and do not look at it until the very end. Look once. If you tune after peeking, it's no longer out-of-sample.
2. **Minimise parameters.** Every knob multiplies your `M` and your selection bias. Prefer a 1–2 parameter system. Ruthlessly delete filters that don't survive OOS.
3. **Seek plateaus, not peaks.** Choose the centre of a broad well-performing region; avoid isolated spikes.
4. **Walk forward, don't just split once.** Roll the IS/OOS window through history (e.g. optimise on 12 months, trade the next 3, roll forward) so you validate across many regimes — bull, bear, sideways, high-vol, low-vol.
5. **Penalise complexity explicitly.** Judge candidates on OOS performance and stability, not IS profit. Deflate your best Sharpe for the number of trials.
6. **Always include realistic costs and slippage.** Optimise net of the full NSE cost stack, not gross.
7. **Prefer economically-motivated parameters.** RSI(14) works across markets because it captures a real overreaction horizon, not because someone grid-searched it. A parameter with a *reason* is more likely to persist than one that merely won a search.
8. **Forward-test / paper-trade before sizing.** OOS backtest is necessary but not sufficient; live paper data is the final referee.

## Honest limitations

- **OOS is not a guarantee.** If you run enough different systems and only keep the ones that pass OOS, you've re-introduced multiple-testing at the meta level — you're now overfitting to your validation set. Discipline about *how many* whole strategies you try matters too.
- **Markets change (non-stationarity).** Even a genuinely robust system decays as market structure evolves (algos, regulation, participant mix). Robustness buys durability, not permanence; periodic re-validation is mandatory.
- **Small samples defeat everything.** Indian F&O history is deep, but *independent* swing trades in a given regime are few. With 30–50 trades, statistical confidence is low no matter how careful you are — treat conclusions as tentative.
- **You cannot fully escape the bias, only shrink it.** Every choice you made — which instrument, which years, which indicator family — was itself a form of selection. Humility, not a magic validation trick, is the real defence.

## Interview-ready summary

Optimization means searching a strategy's free parameters for the combination that maximises a historical objective — and its cardinal pitfall is **overfitting**: because price data mixes repeatable signal with unrepeatable noise, and optimisers fit both, the apparent edge is inflated by a selection-bias term that **grows with the number of combinations tested (√(2 ln M)) and shrinks with sample size (1/√N)**. More parameters and harder searching always *raise* the backtest number while *lowering* live performance, so in-sample results cannot detect the problem — you must hold data out. The defences are: keep parameters few, **optimise in-sample and judge only out-of-sample (walk-forward)**, choose broad parameter *plateaus* over isolated spikes (a system that dies when RSI length changes by 1 is noise), demand IS≈OOS stability rather than peak IS profit, penalise complexity, and always net out realistic NSE costs. Demonstrated on a Bank Nifty RSI mean-reversion grid where the "best" in-sample combo (PF 2.4) collapsed to PF 1.15 out-of-sample while the un-optimised RSI(14)/30/70 stayed stable — proving that the honest expectation of an edge is its out-of-sample number, never its optimised backtest.
