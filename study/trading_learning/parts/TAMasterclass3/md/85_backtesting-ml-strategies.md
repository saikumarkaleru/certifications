# Backtesting ML Strategies Correctly

## The concept: why most ML backtests are lies

A machine-learning model that "predicts Nifty direction with 68% accuracy" and shows a backtest equity curve rising smoothly from ₹10 lakh to ₹90 lakh in three years is, almost always, a fantasy. Not because ML cannot work on markets — it sometimes can, at the margins — but because the *evaluation* was contaminated. The model was graded on information it would never have had in real time, or on a metric that hides the losses, or on a single lucky split of the data.

This chapter is about doing the evaluation *honestly*. It is the least glamorous and most important skill in quantitative TA. A mediocre strategy with a rigorous backtest is worth ten brilliant-looking ones with sloppy backtests, because only the first tells you what will actually happen to your capital. The core discipline: **the backtest must simulate, bar by bar, a trader who knows only the past.** Every violation of that principle inflates results.

Financial time-series ML breaks the standard machine-learning playbook in specific ways. Data is serially correlated (today looks like yesterday), non-stationary (the process changes), extremely low signal-to-noise (a great edge is 53–55% directional, not 90%), and the samples overlap (a 20-day forward-return label at day t shares 19 days with the label at day t+1). Ignore these and cross-validation lies to you. The rest of this chapter is the catalogue of traps and the correct procedure.

## The traps, precisely

### 1. Lookahead bias

Using, at decision time t, any data that was not *available* at t. Subtle forms:

- **Feature leakage.** Computing a z-score, a scaler's mean/σ, or a clustering model on the *whole* dataset and then "backtesting" on part of it. The scaler already saw the future. Fit all transforms on the training window only, then apply them forward.
- **Label leakage.** A feature that secretly contains the answer — e.g. using the day's *close* to compute a signal you then act on at that same day's close, or using adjusted-for-later-split prices.
- **Point-in-time data.** Corporate results, index reconstitutions (a stock added to Nifty 50), and even adjusted prices are often stored as *revised*. Backtesting an F&O strategy on a stock using its *current* Nifty-membership, when it wasn't in the index back then, is lookahead.

### 2. Survivorship bias

Testing a stock strategy on *today's* Nifty 500 constituents ignores every company that was delisted, merged, or fell out of the index — usually the losers. Your universe must be the point-in-time membership. This alone can turn a "profitable" small-cap system into a losing one.

### 3. Overlapping labels and leakage across the split

If your label is "return over the next 10 days", then sample at day t and sample at day t+3 share 7 days of outcome. Put one in train and the neighbour in test, and the test is not independent — the model effectively saw it. Standard k-fold cross-validation, which shuffles rows randomly, is *catastrophic* here: it scatters near-identical, outcome-sharing samples across folds and reports gorgeous, fake accuracy.

### 4. Multiple-testing / selection bias

Try 500 feature combinations, 20 model types, 10 hyperparameter sets, and keep the best on the test set — you have *fit the test set* through your own search. The winner's performance is the maximum of many noisy trials, guaranteed to be optimistic. This is the single most common way retail and even pros fool themselves.

### 5. Ignoring costs and market microstructure

Indian frictions are real and must be modelled per trade:

| Cost | Approx level (2026) | Notes |
|---|---|---|
| Brokerage | ₹20/order or 0.03% (discount broker) | flat per leg |
| STT | 0.1% delivery equity; 0.02% intraday sell; 0.1% on option premium (sell); 0.125% on exercised options | asymmetric — check current rates |
| Exchange txn charges | ~0.00297% equity; ~0.03–0.05% options premium | |
| GST | 18% on (brokerage + txn charges) | |
| SEBI + stamp | tiny but nonzero | |
| **Slippage** | 1 tick to several, worse in illiquid strikes / away-from-ATM options | usually the biggest hidden cost |
| **Impact** | scales with your size vs. displayed depth | matters for anything beyond retail size |

A high-frequency ML signal that trades 30 times a day looks great gross and is dead after costs. *Always* subtract realistic round-trip costs and a slippage assumption before believing anything.

### 6. Regime dependence

A model trained on 2015–2019 quiet markets can fail utterly post-2020. If your test period happens to be a single benign regime, your result is a coincidence.

## The method: how to backtest ML correctly

### Walk-forward analysis (the backbone)

Never a single train/test split. Instead, march forward in time:

```
Train [Jan15 — Dec18] → Test [Jan19 — Jun19]
Train [Jul15 — Jun19] → Test [Jul19 — Dec19]
Train [Jan16 — Dec19] → Test [Jan20 — Jun20]
... roll forward ...
```

At each step the model is fit *only* on past data and evaluated on the *next, unseen* block, then rolled. Concatenate all the out-of-sample test blocks into one continuous out-of-sample equity curve — *that* curve, and nothing computed in-sample, is your estimate of live performance. Use either an **anchored/expanding** window (train grows) or a **rolling** window (fixed length, good when you believe old data is stale).

### Purging and embargo

To defeat overlapping-label leakage (Marcos López de Prado's method):

- **Purge**: remove from the training set any sample whose label window *overlaps* the test set's time span. If test starts at t and labels look forward h days, drop training samples whose outcome extends into [t, t+h).
- **Embargo**: additionally drop a small buffer of samples immediately *after* the test block from the next training set, because serial correlation leaks backward too. An embargo of ~1% of the sample length, or at least h bars, is typical.

Combined, this is **purged, embargoed walk-forward (or combinatorial purged) cross-validation** — the correct CV for financial ML. Ordinary shuffled k-fold is banned.

### Correct labelling: the triple-barrier method

Instead of "return after fixed 10 days", label each entry by which of three barriers is hit first: an upper barrier (profit target, e.g. +2×ATR), a lower barrier (stop, e.g. −1.5×ATR), or a vertical barrier (time limit). The label is +1 / −1 / 0. This mirrors how a trade actually ends and produces path-dependent, tradeable labels. Pair it with **sample weighting** that down-weights overlapping/concurrent labels so the model doesn't over-count redundant samples.

### Honest metrics

Accuracy is nearly useless (a model predicting "up" always is ~53% right on Nifty because of drift). Report:

- **Net CAGR and total return** after all costs.
- **Sharpe** (annualised) *and* **Sortino** (penalises only downside).
- **Max drawdown** and **Calmar** (CAGR / max DD) — for a leveraged F&O trader, drawdown is what ends careers.
- **Hit rate, average win/avg loss, profit factor, expectancy per trade** in ₹.
- **Turnover** and **cost drag** (gross vs net) — expose whether costs eat the edge.
- **Deflated Sharpe / probability of backtest overfitting (PBO)** — adjusts your best Sharpe for the number of trials you ran. If you tested 200 configs, your top Sharpe of 1.8 might deflate to 0.4.

### Statistical robustness

- **Reality check / White's test / Monte-Carlo permutation**: shuffle the returns or the signal timing many times and ask how often random luck beats your strategy. If 30% of random shuffles beat you, you have nothing.
- **Parameter sensitivity**: vary each hyperparameter ±20%. A real edge degrades gracefully; a fitted artifact collapses off its single lucky setting. Prefer a broad plateau of good results over a sharp peak.
- **Out-of-sample holdout you never touch** until the very end, once.

## A worked example with data and code

Goal: predict whether **Bank Nifty** closes higher 5 trading days out, trade a simple long/flat rule, evaluate honestly.

**Features (all known at close of day t):** RSI(14), 20d realised vol, distance from 20-DMA (%), India VIX level and 5-day change, ATR(10)/ATR(50), 10-day return, day-of-week and days-to-weekly-expiry (F&O microstructure matters on Bank Nifty). **Label:** triple-barrier over next 5 days, ±1.5×ATR barriers.

```python
import numpy as np, pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def purged_walk_forward(X, y, t1, n_splits=8, embargo=5):
    # t1[i] = timestamp when sample i's label resolves (for purging)
    n = len(X); fold = n // n_splits
    for k in range(1, n_splits):
        tr_end = k*fold
        te_start, te_end = tr_end, min(tr_end+fold, n)
        # purge: drop training rows whose label resolves at/after test start
        test_start_time = X.index[te_start]
        tr_idx = [i for i in range(tr_end) if t1.iloc[i] < test_start_time]
        te_idx = list(range(te_start+embargo, te_end))   # embargo buffer
        yield tr_idx, te_idx

COST = 0.0007  # ~7 bps round-trip: STT+brokerage+GST+slippage estimate
equity, rets = 1.0, []
for tr, te in purged_walk_forward(X, y, t1):
    m = GradientBoostingClassifier(max_depth=3, n_estimators=200)
    m.fit(X.iloc[tr], y.iloc[tr])
    p = m.predict(X.iloc[te])                 # 1 = long, else flat
    pos = (p == 1).astype(int)
    fwd = fwd_ret.iloc[te].values             # realised 1-day fwd returns, aligned
    turns = np.abs(np.diff(np.r_[0, pos]))    # trades on position change
    net = pos*fwd - turns*COST
    rets.extend(net); equity *= np.prod(1+net)

r = np.array(rets)
sharpe = r.mean()/r.std()*np.sqrt(252)
dd = 1 - (np.cumprod(1+r)/np.maximum.accumulate(np.cumprod(1+r)))
print(f"Net CAGR proxy {equity**(252/len(r))-1:.1%}  Sharpe {sharpe:.2f}  MaxDD {dd.max():.1%}")
```

**Interpreting a realistic result.** Suppose gross Sharpe is 1.6 but net Sharpe after the 7 bps cost falls to 0.7, max drawdown 18%, hit rate 54%, avg win/avg loss 1.1. That is a *plausible, modest* edge — not the fantasy curve. Now run the checks: (1) a permutation test shows only 6% of shuffles beat it — encouraging; (2) you tested 40 feature sets, so the deflated Sharpe drops the 0.7 to ~0.45 — still positive but marginal; (3) parameter sensitivity: Sharpe stays 0.4–0.8 across `max_depth` 2–4 and barrier 1.2–1.8×ATR — a plateau, good sign; (4) split by regime (previous chapter): the edge lives almost entirely in trending regimes and vanishes in chop — so in production you gate the model with the regime tag.

That honest pipeline turns "68% accuracy, ₹90 lakh!" into "a ~0.45 deflated-Sharpe, trend-regime-only edge worth trading small with tight risk." The second statement is far less exciting and far more likely to survive contact with your real broker statement.

## How to use it in a real TA workflow

- **Paper/forward test after backtest.** Even a clean walk-forward is retrospective. Run the frozen model live on paper (or tiny size) for 1–3 months; live results should resemble the out-of-sample backtest. A big gap means residual leakage or cost under-modelling.
- **Freeze then trade.** Once validated, freeze features, model, and thresholds. Re-fit on a schedule (say quarterly, expanding window) — never re-tune mid-drawdown by hunting for what "would have worked".
- **Combine with discretion.** Use the ML output as one input — a probability or a filter — layered on regime context and hard risk limits, not as a black-box autopilot from day one.
- **Kill-switch and monitoring.** Track live hit rate and drawdown against backtest confidence intervals; if live falls outside, stop and investigate. Model decay is normal in markets.

## Honest limitations

ML on price data faces a brutally low signal-to-noise ratio; the realistic ceiling is a small statistical edge, not clairvoyance. Non-stationarity means any model decays and must be re-validated. The more you search — features, models, hyperparameters, universes — the more you overfit the very data you test on, and no amount of clever CV fully rescues you from a thousand silent trials; the deflated Sharpe and permutation tests only *estimate* the damage. Costs and slippage in Indian F&O (especially away-from-ATM options and mid-cap stocks) routinely convert gross winners into net losers. And a perfect backtest still cannot promise the future: it certifies that *your evaluation was honest*, not that the edge will persist. The correct mindset is not "prove the strategy works" but "try hard to *break* it — and trade only what survives."

## Interview-ready summary

Correctly backtesting an ML trading strategy means simulating a trader who knows only the past. The cardinal sins are lookahead (fitting scalers/models on future data, non-point-in-time prices), survivorship bias (testing on today's index members), overlapping-label leakage (shuffled k-fold on serially correlated data), selection bias from running many trials, and ignoring realistic Indian costs (STT, brokerage, GST, and especially slippage). The correct toolkit: walk-forward analysis with purging and an embargo to prevent label leakage; triple-barrier labelling with sample weights so labels are tradeable and non-redundant; a concatenated out-of-sample equity curve as the only trusted result; and honest metrics — net Sharpe/Sortino, max drawdown, Calmar, expectancy, turnover, cost drag, and a *deflated* Sharpe that penalises the number of configurations tried. Validate further with permutation tests and parameter-sensitivity plateaus, then forward-test on paper before risking capital, freeze the model, and monitor for decay. A rigorous backtest usually shrinks a dazzling claim to a modest, regime-dependent edge — and that shrinkage is exactly the point: it is the difference between a curve you drew and a return you will actually earn.
