# Overfitting Detection

## The concept

Overfitting is the disease that kills more trading systems than any drawdown, any black swan, any broker outage. It is the reason the backtest looks like a staircase to heaven and the live account looks like a slow leak. Understanding it precisely — and learning to *detect* it before you risk a rupee — is arguably the most valuable quantitative skill a technical trader can own.

The intuition is this. A market's price history is a mixture of **signal** (repeatable structure — trend persistence, mean reversion, volatility clustering, options-expiry effects) and **noise** (unrepeatable randomness — the specific sequence of ticks that will never recur). When you optimise a strategy, the optimiser cannot tell the two apart. It happily fits parameters to whatever produced the best number, and since noise is abundant and signal is scarce, most of what it "learns" is noise. A model that has learned the noise performs brilliantly on the data it was fitted to and terribly on anything new — because the new data has *different* noise.

The formal way to see it: as you add parameters or test more configurations, your **in-sample** performance rises monotonically, but your **true (out-of-sample)** performance rises, peaks, and then falls. The gap between the two is the *generalisation gap*, and overfitting is the state where that gap is large. The whole art of overfitting detection is measuring, or bounding, that gap without the luxury of infinite fresh data.

There's a specifically insidious form in trading called **backtest overfitting from multiple testing**. Even if each individual strategy is honest, if you try 1,000 variations and keep the best, the best one will look great *by chance alone*. With enough trials, some random coin-flipping strategy will show a Sharpe of 2.0 on your sample. This is the "more trials → higher expected best-in-sample Sharpe even with zero real edge" problem, and it is everywhere in retail TA, where people grid-search indicator settings until something sparkles.

## The methods and the maths

There is no single test; overfitting detection is a battery of complementary checks. Here are the ones that matter, from simplest to most rigorous.

**1. In-sample vs out-of-sample degradation.** The first-line check. Split data, optimise on IS, measure on OOS. Compute the degradation ratio:

```
Degradation = OOS_metric / IS_metric
```

A Sharpe that goes from 2.4 IS to 0.3 OOS (ratio 0.12) is overfit. A ratio above ~0.5 for a robust metric is reassuring. Walk-forward (previous chapter) is the industrialised version of this.

**2. The Deflated Sharpe Ratio (DSR).** Developed by Bailey and López de Prado, this is the sharpest tool for the multiple-testing problem. The idea: your observed Sharpe must be discounted for (a) how many strategies you tried, (b) the non-normality (skew and kurtosis) of returns, and (c) the sample length. First compute the expected maximum Sharpe you'd get from *N* independent random trials with zero true edge:

```
E[max SR] ≈ sqrt(Var(SR_trials)) × [ (1−γ)·Z⁻¹(1 − 1/N) + γ·Z⁻¹(1 − 1/(N·e)) ]
```

where γ ≈ 0.5772 (Euler–Mascheroni) and Z⁻¹ is the inverse normal CDF. Then the Probabilistic Sharpe Ratio deflates your observed SR against that benchmark, adjusting for skew (ĝ₃) and kurtosis (ĝ₄) over *T* observations:

```
PSR(SR*) = Z[ (SR_obs − SR*) · sqrt(T−1) / sqrt(1 − ĝ₃·SR_obs + (ĝ₄−1)/4 · SR_obs²) ]
```

Setting SR* = E[max SR] gives the DSR: the probability your Sharpe is real *after* accounting for the fact you went fishing. A DSR below ~0.90–0.95 means you can't reject "this is luck." The single most important lesson here: **the more configurations you tested, the higher your in-sample Sharpe must be to mean anything.**

**3. Combinatorially-Symmetric Cross-Validation (CSCV) and PBO.** The **Probability of Backtest Overfitting** estimates how often the strategy that was best in-sample turns out to be *below median* out-of-sample. You chop the trade-return matrix into *S* blocks (say 16), form all balanced IS/OOS combinations (C(16,8) = 12,870 splits), and for each split find the IS-best configuration and check its OOS rank. PBO is the fraction of splits where the IS-champion falls below the OOS median. **PBO > 0.5 means your selection process is worse than random** — a devastating verdict.

**4. Learning curves.** Plot performance vs training-window length. A genuine edge stabilises as data grows; an overfit one is erratic and sample-hungry.

**5. Parameter-sensitivity surface.** Covered more in the next chapter, but as a detection tool: if the performance surface over the parameter grid is a lone sharp spike surrounded by losses, you've fit a needle. A real edge is a broad plateau.

**6. Trade-count sanity.** A strategy with 12 trades and a 3.0 profit factor is not a strategy, it's an anecdote. Rule of thumb: you want ≥100 OOS trades before believing a Sharpe, and even then be humble.

| Detection method | What it catches | Verdict threshold |
|---|---|---|
| IS/OOS degradation | Basic curve-fit | ratio < 0.5 = suspect |
| Deflated Sharpe (DSR) | Multiple-testing luck | DSR < 0.90 = not significant |
| PBO (CSCV) | Selection overfitting | PBO > 0.5 = worse than random |
| Learning curve | Sample-hunger | non-convergence = fragile |
| Parameter surface | Needle-fitting | isolated spike = overfit |
| Trade count | Statistical thinness | < 30–100 trades = anecdote |

## A worked example with data and code

Suppose you're building a **Supertrend + RSI filter** system on daily Nifty 50, 2016–2026. You grid-search the Supertrend ATR period ∈ {7,10,14,21}, multiplier ∈ {1,2,3,4}, and RSI threshold ∈ {40,50,60} — that's 4 × 4 × 3 = **48 configurations tested**. The best one shows an in-sample Sharpe of 1.9. Is it real?

Here's the honest-detection workflow in Python-style pseudocode:

```python
import numpy as np
from scipy.stats import norm

# daily returns of the BEST config, in-sample (say 1400 trading days of exposure)
r = strategy_daily_returns          # array of the winning config's returns
T = len(r)
SR_obs = r.mean() / r.std() * np.sqrt(252)   # annualised
g3 = skew(r); g4 = kurtosis(r, fisher=False) # skew, non-excess kurtosis

# --- Deflated Sharpe: benchmark for 48 trials ---
N = 48
# variance of Sharpe across the 48 trials (from the grid search results)
var_sr = np.var(trial_sharpes, ddof=1)
gamma = 0.5772156649
E_max_SR = np.sqrt(var_sr) * (
      (1-gamma)*norm.ppf(1 - 1/N) + gamma*norm.ppf(1 - 1/(N*np.e)) )

# --- Probabilistic Sharpe vs that benchmark (both in daily units) ---
SRd = SR_obs/np.sqrt(252); SRb = E_max_SR      # convert to per-period
num = (SRd - SRb) * np.sqrt(T - 1)
den = np.sqrt(1 - g3*SRd + (g4-1)/4 * SRd**2)
DSR = norm.cdf(num/den)
print(f"Observed SR {SR_obs:.2f}, E[max SR|48 trials] {E_max_SR*np.sqrt(252):.2f}, DSR {DSR:.2%}")
```

Plausible output: `Observed SR 1.90, E[max SR|48 trials] 1.35, DSR 71%`. The interpretation is brutal but useful: because you tested 48 configurations, the *expected best-by-luck* Sharpe was already 1.35, and after adjusting for skew, fat tails and only 1,400 observations, the probability the 1.9 is genuinely above the luck benchmark is just 71% — well short of the ~95% you'd want. **This system fails the detection test.** You either need a much stronger IS Sharpe, more data, or fewer trials.

Now the PBO side, sketched:

```python
# M = matrix (T_obs × 48) of per-period returns for all configs
S = 16                                  # blocks
splits = combinations(range(S), S//2)   # 12,870 balanced IS/OOS splits
below_median = 0; total = 0
for is_blocks in splits:
    oos_blocks = [b for b in range(S) if b not in is_blocks]
    IS = concat_blocks(M, is_blocks); OOS = concat_blocks(M, oos_blocks)
    best = argmax(sharpe(IS))           # champion in-sample
    oos_rank = rank(sharpe(OOS))[best]  # its OOS rank
    below_median += (oos_rank < 0.5)
    total += 1
PBO = below_median/total
print(f"PBO = {PBO:.2%}")              # e.g. PBO = 58%
```

A PBO of 58% is a fail: more than half the time, the in-sample champion is a below-median performer out-of-sample. Your *selection procedure* is anti-predictive.

## How to use it in a real TA workflow

Detection is not an academic afterthought — it's a gate every strategy must pass before it sees capital. A practical pipeline for an Indian-markets systematic trader:

1. **Pre-register your grid.** Decide the parameter ranges *before* testing and write them down. This makes *N* (trial count) honest, which is the input the DSR needs. Sneaking in extra trials later invalidates the deflation.
2. **Run walk-forward first** (previous chapter) to get an OOS curve.
3. **Compute IS/OOS degradation.** If OOS Sharpe is under half of IS, stop here — it's overfit.
4. **Compute the Deflated Sharpe** using your true trial count. If DSR < 0.90, the apparent edge is indistinguishable from data-mining luck.
5. **Compute PBO via CSCV.** If PBO > 0.5, the selection method is broken; go back and simplify.
6. **Check the parameter surface** for a plateau, not a spike (next chapter).
7. **Only then**, size conservatively using OOS drawdowns, and monitor live degradation.

Concretely, when you're screening breakout setups on the Nifty 500 universe, this pipeline is what stops you from deploying the "9-EMA / 21-EMA crossover with 2.3× ATR trailing stop on stocks with RSI between 47 and 63" system that looks magnificent purely because you tried 300 combinations and kept the shiniest.

## Honest limitations

Overfitting detection is powerful but not omniscient, and pretending otherwise is its own trap.

- **The DSR needs an honest *N*.** If you can't count your trials — because you eyeballed charts, tweaked by intuition, or reused ideas across projects — the deflation is guesswork. The "effective number of trials" including all the informal experimentation is usually far larger than the formal grid, meaning real overfitting is worse than any test reports.
- **All these tests assume the past resembles the future.** They catch fitting to *in-sample noise*, but they cannot catch **regime change** — a system honestly validated on 2016–2023 may still die in 2026 because the market's structure genuinely changed (e.g., a shift in retail options participation, a new STT regime, algo dominance). No detection method protects against non-stationarity.
- **PBO and CSCV assume trades are roughly exchangeable across blocks.** Strongly serially-correlated or trending returns can bias the estimate.
- **Fat tails and small samples degrade everything.** Indian single-stock returns are heavily skewed by events (results, promoter news, circuit filters). Sharpe-based tests understate risk when returns are non-normal, which is exactly when you most need them.
- **Detection is necessary, not sufficient.** Passing every test proves only that the edge is *not obviously* data-mined; it does not prove the edge exists. Forward paper-trading on genuinely unseen future data remains the ultimate — and only truly clean — test.

The honest posture: treat every backtest as guilty until proven innocent, deflate aggressively, prefer simple models with few parameters and broad plateaus, and remember that the market's future noise is guaranteed to differ from its past noise.

## Interview-ready summary

Overfitting is when a strategy learns the unrepeatable noise of its training data rather than the repeatable market signal, producing a large gap between in-sample and out-of-sample performance. Detection is a battery of tests: the simplest is IS/OOS degradation (OOS Sharpe below half the IS Sharpe is a red flag); the most powerful for the multiple-testing problem is the Deflated Sharpe Ratio, which discounts your observed Sharpe by the expected best-by-luck Sharpe from *N* trials and adjusts for skew, kurtosis and sample length — a DSR under ~0.90 means the edge is indistinguishable from data-mining; and the Probability of Backtest Overfitting (via combinatorially-symmetric cross-validation) measures how often the in-sample champion is a below-median out-of-sample performer, with PBO above 0.5 meaning your selection process is worse than random. Supporting checks include learning curves, parameter-surface plateaus versus spikes, and minimum trade counts. The killer insight is that testing more configurations mechanically inflates your best in-sample result even with zero true edge, so you must pre-register your grid and count every trial honestly. The limitations are real: these tests need an honest trial count, cannot detect regime change or non-stationarity, and are only necessary — never sufficient — proof of edge. Passing them earns you the right to forward-test with real money, cautiously sized off out-of-sample drawdowns; failing them saves you from an expensive live lesson.
