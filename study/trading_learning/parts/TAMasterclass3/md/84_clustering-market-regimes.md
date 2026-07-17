# Clustering Market Regimes

## The concept: why a market has "moods"

Every discretionary trader eventually notices the same thing: the *same setup* that prints money in one stretch of the year quietly bleeds you dry in another. A supertrend-following breakout on Nifty that caught the entire April–September 2023 grind gets chopped to pieces in a range-bound, mean-reverting tape. This is not bad luck. It is a *regime change* — the statistical character of price (its volatility, trendiness, autocorrelation, and dispersion) has shifted, and your edge is conditional on a character it no longer has.

A **market regime** is a persistent state of the market defined by a bundle of statistical properties rather than by a single number. Broadly, Indian index traders live inside four recurring regimes:

- **Quiet trend** — low realised volatility, steady positive drift, India VIX 10–13, tight daily ranges (Nifty daily range ~0.4–0.7%). Buy-the-dip works; option sellers feast.
- **Volatile trend** — a strong directional move but with fat daily ranges and gaps (a Budget rally, an election-result day, a global risk-on burst). VIX 15–22.
- **Range / chop** — no drift, high mean-reversion, VIX moderate but *price* oscillating in a band (Bank Nifty stuck between 47,000–49,000 for weeks). Breakouts fail; fade-the-extreme works.
- **Crisis / panic** — VIX spiking above 25–30, correlations collapsing to 1, gaps of 2–4%, everything selling together (COVID March 2020, the Aug 2024 yen-carry unwind spillover). Trend-down with violent bear rallies.

**Clustering** is the unsupervised-machine-learning way of *discovering* these regimes from data instead of hand-labelling them. You feed an algorithm a set of features that describe "what the market feels like today", and it groups similar days together into clusters. Each cluster becomes a candidate regime. The promise: an objective, repeatable regime tag you can attach to every trading day, then use to switch strategies, size positions, or filter signals.

The honesty up front: clustering *finds structure whether or not structure exists*. It will always hand you k clusters. The hard work — and where most retail attempts go wrong — is (a) choosing features that actually describe regime, (b) validating that the clusters are stable and tradeable rather than artifacts, and (c) handling the fact that regime labels can only be assigned with a lag and can whipsaw.

## The method and the maths

### Features: describe the market, not predict it

Clustering is only as good as its features. For an Indian index (say Nifty spot + India VIX + a breadth series), a robust daily feature vector might be:

| Feature | Formula / definition | What regime property it captures |
|---|---|---|
| Realised vol (20d) | annualised std of daily log returns × √252 | volatility level |
| Vol-of-vol | 20d std of the realised-vol series | regime instability |
| Trend strength | ADX(14) *or* abs(20d return) / (20d realised vol) | trendiness vs chop |
| Return sign persistence | 20d autocorrelation of daily returns (lag 1) | momentum vs mean-reversion |
| VIX level | India VIX close | fear/complacency |
| VIX slope | VIX(today) − VIX(5d ago) | rising vs falling fear |
| Range expansion | ATR(10) / ATR(50) | is the tape widening? |
| Breadth | % of Nifty 50 stocks above 50-DMA | participation / dispersion |
| Skew proxy | (close − 20d low)/(20d high − 20d low) | position within range |

Note what is *absent*: the raw price level, the date, moving-average crossover signals. We want features that are **stationary-ish and comparable across years**. A Nifty at 8,000 in 2016 and 24,000 in 2024 must map to the same regime if they *behaved* the same — so we use ratios, z-scores and vols, never absolute rupee levels.

### Standardisation

Clustering algorithms use distance. If realised vol ranges 0.08–0.45 and breadth ranges 0–100, breadth will dominate the Euclidean distance purely because of scale. So every feature is **z-scored**:

z_i = (x_i − μ_i) / σ_i

using μ and σ computed on the *training window only* (critical for avoiding lookahead — more in the next chapter). Some practitioners prefer robust scaling (subtract median, divide by IQR) because financial features have fat tails and outliers (crisis days) that inflate σ.

### K-Means: the workhorse

K-Means partitions n observations into k clusters, each represented by a centroid (mean vector). It minimises within-cluster sum of squares:

J = Σ_{j=1}^{k} Σ_{x ∈ C_j} || x − μ_j ||²

The Lloyd algorithm iterates: (1) assign each day to its nearest centroid; (2) recompute each centroid as the mean of its members; repeat until assignments stop changing. It is fast, simple, and interpretable — the centroid *is* the "average" of a regime, so you can read off "cluster 2 = high vol, rising VIX, negative persistence = crisis".

Weaknesses: K-Means assumes roughly spherical, equal-size clusters and hard-assigns every point. Crisis days are rare and extreme; K-Means may lump them awkwardly or let them pull a centroid.

### Choosing k

There is no "true" k. Use two guides together:

- **Elbow method** — plot J against k=2…10; look for the kink where added clusters stop reducing J much.
- **Silhouette score** — for each point, s = (b − a)/max(a,b), where a = mean distance to own cluster, b = mean distance to nearest other cluster. Average s over all points; higher (closer to 1) = better-separated clusters. Values above ~0.3–0.4 on financial data are already respectable.

For index regimes, k = 3 or 4 usually wins on interpretability. More clusters fragment into micro-states you cannot trade differently anyway.

### Gaussian Mixture Models (GMM): soft regimes

A GMM models the data as a weighted sum of k Gaussians, each with its own mean μ_j and covariance Σ_j:

p(x) = Σ_j π_j · N(x | μ_j, Σ_j)

Fit by Expectation-Maximisation. The payoff over K-Means: (1) it gives a **probability** of membership in each regime, not a hard label — "today is 70% quiet-trend, 25% range, 5% crisis"; (2) covariances let clusters be elliptical, matching correlated features; (3) you can threshold on probability to *stay flat when the regime is ambiguous*. That soft assignment is genuinely useful for position sizing: scale exposure by P(favourable regime).

### Hierarchical & HMM alternatives

- **Agglomerative hierarchical clustering** builds a dendrogram by repeatedly merging the closest points/clusters; you cut the tree at a chosen height. Good for *exploring* how many natural groups exist without pre-committing to k.
- **Hidden Markov Models (HMM)** deserve a mention because they explicitly model *transitions* between hidden states and the *persistence* of a regime (a transition matrix with high diagonal probabilities). This directly addresses regime stickiness and reduces whipsaw — arguably the "right" tool for regimes, though heavier to fit and easier to overfit. Plain clustering treats each day independently and therefore flickers; an HMM smooths naturally.

## Worked India example: four regimes on Nifty

Suppose we take Nifty daily data from Jan 2015 to Dec 2024, build the nine-feature vector above, z-score on a rolling basis, and run K-Means with k = 4. A representative result (centroids read back in original units):

| Cluster | Realised vol | VIX | VIX slope | Trend str | Persistence | Breadth | Label |
|---|---|---|---|---|---|---|---|
| C0 | 10% | 12 | flat/down | high (+) | +0.15 | 72% | **Quiet uptrend** |
| C1 | 16% | 17 | up | high | −0.10 | 40% | **Volatile trend** |
| C2 | 12% | 14 | flat | low | −0.20 | 55% | **Range / chop** |
| C3 | 34% | 29 | sharply up | high (−) | +0.25 | 12% | **Crisis** |

Reading a few real windows against these:

- **Apr–Sep 2023**: Nifty climbs from ~17,400 to ~20,200 with VIX pinned near 11 and breadth strong. Almost every day tags **C0 (quiet uptrend)**. A dip-buyer or a delta-positive trend follower thrives; an option *seller* running short strangles on Bank Nifty collects theta with rare pain.
- **Jan–Mar 2020 (COVID)**: as Nifty falls from 12,200 to 7,500, VIX explodes to 84 (all-time high), realised vol above 60%, breadth near zero. Days flip hard into **C3 (crisis)**. Any short-vol strategy is destroyed here; the regime tag would have screamed "flat or hedged only".
- **Bank Nifty, Oct–Nov 2022** stuck roughly 40,000–43,000: alternating **C2 (range)** tags. Breakout systems get chopped; fade-the-band with defined risk is the regime-appropriate play.
- **Jun 2024 (election result week)**: 4 Jun sees Nifty gap down ~8% intraday then recover; VIX had spiked to ~27 pre-result. Days around it tag **C1/C3**. The lesson: known event risk pushes the tape into volatile/crisis regimes *predictably* — you can pre-empt the tag with the F&O event calendar.

The practical output is a single column appended to your data: `regime = {C0,C1,C2,C3}` (or four probabilities from a GMM). You now condition everything on it.

### A minimal code sketch (Python)

```python
import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# df has Nifty OHLC + India VIX, daily
r = np.log(df.close).diff()
feat = pd.DataFrame({
    "rv20":  r.rolling(20).std()*np.sqrt(252),
    "volvol":(r.rolling(20).std()).rolling(20).std(),
    "trend": (df.close.pct_change(20)).abs()/(r.rolling(20).std()+1e-9),
    "persist": r.rolling(20).apply(lambda x: x.autocorr(), raw=False),
    "vix":   df.vix,
    "vix_sl":df.vix.diff(5),
    "rangex":df.atr10/df.atr50,
    "breadth":df.pct_above_50dma,
}).dropna()

# IMPORTANT: fit scaler + kmeans on TRAIN slice only, then transform later data
train = feat.loc[:"2021-12-31"]
scaler = StandardScaler().fit(train)
km = KMeans(n_clusters=4, n_init=20, random_state=0).fit(scaler.transform(train))

feat["regime"] = km.predict(scaler.transform(feat))   # assign all days
```

Two things this sketch already does right: it fits the scaler and the model on an in-sample slice, then *predicts* on later data (rather than re-fitting on everything), and it uses stationary features. The next chapter makes this discipline rigorous.

## How to use regimes in a real TA workflow

Clustering is not itself a trading strategy. It is a **switch** and a **sizing knob**. Concrete uses:

**1. Strategy switching.** Keep a small stable of edges and route by regime:
- C0 quiet uptrend → trend-following / dip-buying / short-strangle option selling.
- C1 volatile trend → momentum with wider stops, ride the direction but cut option *selling* size.
- C2 range → mean-reversion, fade Bollinger extremes, iron condors with the range as strike guide.
- C3 crisis → flat, or long-vol / long-put hedges only; disable all short-vol.

**2. Position sizing.** With a GMM you have P(favourable). Set exposure ∝ P(C0)+P(C1 aligned) and cut it as P(C3) rises. This alone smooths an equity curve dramatically because it deleverages *before* the worst days cluster.

**3. Signal filtering.** Take your existing breakout system's signals but only act on them when regime ∈ {C0,C1}. Backtest with and without the filter; the filtered version usually trades less and keeps more.

**4. Diagnostics / expectations.** Tag your *own* trade log by regime. You will often discover your edge is entirely concentrated in one or two regimes and you have been donating money in the others. That insight is worth more than any indicator.

**5. Event overlay.** Because Indian volatility regimes are partly *scheduled* — Budget (Feb 1), monetary-policy days, big-cap earnings, expiry weeks, election counting — you can anticipate a shift to C1/C3 from the calendar and pre-position (reduce short vol, buy cheap protection) rather than wait for the lagging cluster label.

The regime tag pairs naturally with everything else in this volume: use it as the top-level context, then apply order-flow, DeMark, or your named strategy *inside* the appropriate regime.

## Honest limitations

**Labels lag and flicker.** A cluster label is computed from trailing features (20-day vol, etc.), so it confirms a regime *after* it has begun. Worse, on regime boundaries the day can flip C0→C2→C0 on noise. Mitigations: require the label to persist N days before acting; smooth with an HMM; or use GMM probabilities with a hysteresis band (enter a regime at P>0.6, exit only below 0.4).

**k and features are choices, not truths.** Change the feature set or k and you get different regimes. Clustering will *always* return clusters even on random data, so apparent structure is not evidence of real, tradeable structure. Guard by insisting the regimes are (a) economically interpretable, (b) stable across sub-periods, and (c) associated with genuinely different forward return/vol distributions — test that, don't assume it.

**Non-stationarity.** The market evolves; a regime map fit on 2015–2019 may misclassify the post-2020 world (higher retail flow, weekly-then-daily expiries changing the vol surface). Periodically re-fit, but beware that re-fitting on all-history bakes in lookahead if you then "backtest" on that same history.

**Instability of K-Means.** Different random seeds/initialisations can give different partitions; crisis outliers can hijack a centroid. Use many initialisations (`n_init` high), consider robust scaling, and sanity-check that C3 really isolates the extreme days.

**No forward guarantee.** A clean regime map explains the past beautifully and can still whipsaw live. Regimes describe *conditions*, not the future; they improve the *odds and sizing* of a pre-existing edge — they do not manufacture edge from nothing.

**Overfitting to labels.** It is tempting to build a strategy that works spectacularly *within each cluster* — but the cluster boundaries themselves were fit to the same data. Any performance measured on the fitting sample is optimistic. Regime work must be validated with the walk-forward discipline of the next chapter.

## Interview-ready summary

Market-regime clustering is unsupervised learning applied to *stationary* descriptors of the tape — realised vol, vol-of-vol, trend strength, return persistence, India VIX and its slope, range expansion, and breadth — all z-scored, then grouped by K-Means, a GMM, or an HMM into a handful of interpretable states: quiet uptrend, volatile trend, range, and crisis. For Nifty/Bank Nifty these map cleanly onto real windows (the calm 2023 grind = quiet uptrend; COVID March 2020 = crisis; range-bound Bank Nifty = chop). The regime tag is not a signal; it is a *context switch* and a *sizing knob* — route trend systems, mean-reversion, and option selling to the regimes where each earns, and deleverage into crisis. GMMs add soft probabilities for smoother sizing; HMMs add transition modelling for less whipsaw. The honest caveats: labels lag and flicker, k and features are subjective choices, clustering finds "structure" even in noise, and everything must be validated walk-forward on data the model never saw. Used with that discipline, regime clustering turns "the market has moods" from a trader's superstition into a measurable, tradeable input.
