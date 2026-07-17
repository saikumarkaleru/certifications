# Regime-Detection Methods

Every strategy that ever worked, worked *in a regime*. Trend-following prints money in a persistent bull leg and bleeds in a chop. Option-selling harvests premium in low-vol drift and blows up in a crash. Mean-reversion buys the dip beautifully — until the dip becomes a bear market. The single biggest reason a "backtested edge" dies in live trading is not that the edge was fake; it's that the market silently changed regime and the trader kept running the wrong tool. Regime detection is the discipline of *knowing which world you are in right now*, so you deploy the strategy that world rewards. This chapter is a practical toolkit — the statistical methods that classify market state, worked on Nifty and Bank Nifty, wired into a real Indian trading workflow, and honest about the lag and false signals every one of them carries.

## What it is and the logic

A **regime** is a persistent statistical state of the market — a stretch during which the *rules* generating returns are roughly stable. The canonical taxonomy for equity indices:

| Regime | Return character | Volatility | Winning tools |
|---|---|---|---|
| Bull / trending-up | Positive drift, higher highs | Low-to-moderate | Momentum, breakout, buy-dips |
| Bear / trending-down | Negative drift, lower lows | Rising/high | Short-rallies, put-buying, cash |
| Range / mean-reverting | ~Zero drift | Low-moderate | Fade extremes, sell straddles |
| Crisis / high-vol | Sharp negative, gaps | Very high | Defence, tail hedges, flat |

The logic of regime detection rests on a well-documented empirical fact: financial volatility **clusters**. Big moves follow big moves; quiet follows quiet. Returns are close to unpredictable in *direction*, but their *variance* is highly persistent and forecastable. That persistence is what makes regimes detectable at all. A day of 2% Nifty range is far more likely to be followed by another wide day than by a sleepy 0.3% day. Regime methods exploit exactly this stickiness.

Crucially, regime detection is **not prediction of the next candle**. It is *classification of the current environment*. You are not forecasting tomorrow's return; you are answering "are we in trend-world or chop-world, calm-world or crisis-world?" — a much more tractable and more useful question.

## Construction: the method family

There is a ladder of methods from crude-but-transparent to sophisticated-but-opaque. Master the whole ladder; the simple ones are often better in practice because you can see why they fired.

### 1. Threshold / rule-based indicators (transparent)

The workhorses. Cheap, explainable, no fitting.

- **Moving-average slope & stack.** Price above a rising 200-DMA with 20 > 50 > 200 stacked = bull regime; the inverse = bear; tangled/flat MAs = range. Simple, robust, and the basis of most institutional "risk-on/risk-off" switches.
- **ADX (Average Directional Index).** ADX > 25 = trending regime (of either direction, read with +DI/−DI); ADX < 20 = non-trending/range. The classic trend-vs-range gate.
- **Choppiness Index (CI).** 0-100 scale from ATR-sum vs range. CI > 61.8 = consolidation/chop; CI < 38.2 = strong trend. A direct regime meter.
- **Volatility bucketing via India VIX / realised vol / ATR.** Bucket the market by vol: VIX < 13 = complacent-low, 13-18 = normal, 18-25 = elevated, > 25 = stress/crisis. Vol regime dictates whether you buy or sell options.
- **Bollinger Band width / Keltner squeeze.** Contracting bands = low-vol coiled regime (breakout pending); expanding = trending/volatile regime.

### 2. Statistical / unsupervised methods (data-driven)

When you want the data to define the states instead of hard thresholds.

- **Rolling volatility-and-return clustering (k-means / GMM).** Build a feature vector per bar — e.g. {20-day return, 20-day realised vol, ADX, VIX level} — standardise it, and cluster into k=3 or 4 groups. Each cluster is an empirically discovered regime. A Gaussian Mixture Model (GMM) is the soft version: it gives *probabilities* of belonging to each regime rather than a hard label, which is far more useful for sizing.
- **Change-point detection.** Algorithms (CUSUM, Bayesian online change-point detection, the PELT algorithm) that flag the *bar at which* the statistical properties broke. Instead of a continuous label, you get "the regime changed on 2024-06-04" — useful for post-mortems and for triggering a strategy switch.
- **Markov regime-switching models (HMM).** The heavyweight — covered fully in the next chapter. A hidden state (regime) evolves with transition probabilities, and each state has its own return/vol distribution. It gives you both the current regime probability *and* the odds of switching next.

### 3. Composite scoring (practical hybrid)

The pragmatic desk approach: combine several transparent signals into a single regime score. Award points — MA stack (+1 bull / −1 bear), ADX>25 (+1 trend), CI<38 (+1 trend), VIX bucket, breadth — and read the aggregate. Robust because no single indicator dominates, and you can always explain *why* the score says what it does.

## Settings and a decision table

A serviceable composite for **daily** Indian index trading:

| Feature | Bull-trend | Bear-trend | Range | Crisis |
|---|---|---|---|---|
| Price vs 200-DMA | Above, rising | Below, falling | Straddling | Below, gapping |
| 20/50/200 stack | Bullish stack | Bearish stack | Tangled | Bearish, steep |
| ADX (14) | > 25, +DI top | > 25, −DI top | < 20 | > 30 |
| Choppiness (14) | < 40 | < 40 | > 60 | variable |
| India VIX | < 16 | 16-25 | 12-16 | > 25 |
| Realised vol (20d, ann.) | 10-16% | 18-30% | 8-14% | > 35% |

Read across: the regime is whichever column the most features agree on. Disagreement itself is a signal — a transition is likely underway, and transitions are when you cut size.

## Worked India example (levels and ₹)

**Case: Nifty across a calm bull leg into a shock.** Imagine Nifty grinding from ~21,800 to ~24,000 over several weeks. Through this leg:
- Price sits above a rising 200-DMA, 20 > 50 > 200 stacked. **+bull.**
- ADX runs 26-32 with +DI dominant. **+trend.**
- Choppiness sits ~35. **+trend.**
- India VIX is quiet at ~13-14. **calm.**

Composite = **calm bull-trend.** Correct play: momentum and buy-the-dip. A pullback to the 20-DMA near, say, 23,400 is an *entry*, not an exit. Running a mean-reversion "sell the highs" system here would have you shorting strength into a trend — the classic way to die.

Then a shock lands — a global risk event, a budget surprise, a geopolitical flare. In two sessions Nifty gaps and slides from 24,000 toward 22,600:
- Price breaks below the 20- and 50-DMA; the stack starts inverting. **bull→transition.**
- India VIX spikes from 14 to 22+. **calm→stress.**
- Realised vol jumps; ADX flips with −DI rising. **trend flipping direction.**

A composite regime detector flips from "calm bull" to "stress/transition" within a bar or two of the VIX spike — VIX is your fastest sensor here. The correct response is not to guess the bottom; it is to *switch toolboxes*: cut trend-long size, stop buying dips blindly, widen stops or move to cash, and if you sell options, respect that a low-vol premium-selling book is now in its danger regime. Straddle sellers who ignored the VIX regime flip from 14 to 22 are the ones who post the ugly loss screenshots.

**Rupee frame.** Say you swing-trade three Nifty futures lots (lot 75; at 24,000 that's ~₹54 lakh notional per lot, so heavy). In the calm bull regime you carry full size with a trailing stop. The moment the composite flags stress (VIX > 18, MA break), your rules cut to one lot or flat. If that discipline saves you from a 600-point adverse Nifty move, that's 600 × 75 × 2 lots exited = **₹90,000 of drawdown avoided** — the entire economic value of regime detection in one number. It doesn't make you money in the good regime; it stops the bad regime from taking it back.

**Bank Nifty intraday nuance.** Intraday, Bank Nifty flips regime *within* a session — a trending morning off a gap can dissolve into a dead lunch-hour range and then a volatile expiry-afternoon. An intraday composite (5-min ADX, opening-range status, VWAP slope, rolling 30-bar realised vol) that reclassifies every bar lets an option scalper switch between "ride the trend with call/put buying" in the trending window and "sell the range / fade VWAP extremes" in the chop — the same instrument, two regimes, two strategies, one day.

## How to trade it

Regime detection is a **switch**, not a signal. The workflow:

1. **Classify** the current regime each bar (composite or model).
2. **Route** to the strategy that regime rewards (the mapping table above).
3. **Only take signals** consistent with the regime. In a range regime, ignore breakout buys; in a trend regime, ignore mean-reversion fades.
4. **Size by conviction.** When regime indicators agree strongly, full size. When they disagree (transition), half size or flat.
5. **Manage exits by regime.** Trend regime → trail and let it run. Range regime → fixed targets at the band edges. Crisis regime → defence first, tighten or hedge.

**The transition zone is where money is made and lost.** Detectors lag — by construction, they need data to confirm a change. So build an explicit "transition/unknown" state and treat it as *reduce risk*, not *reverse aggressively*. The worst error is flipping fully long-to-short on the first bar of a suspected change and getting whipsawed when it was noise.

## Confluence

Regime detection is the *master layer* that other TA sits under. Confluence here means multiple independent sensors agreeing on the state:

- **Price structure + volatility + breadth.** MA stack (price) + VIX bucket (vol) + advance-decline / % stocks above 200-DMA (breadth) agreeing is a high-confidence regime read. Breadth deteriorating while the index still rises is a classic late-bull-transitioning-to-distribution tell that price-only detectors miss.
- **Cross-asset.** USDINR strengthening sharply, US 10-year yields spiking, or crude gapping often coincide with an Indian-equity risk-off regime shift. A regime model fed only Nifty prices is blind to these; a good desk watches them as leading regime inputs.
- **Hurst exponent (previous chapter).** H measures trend-vs-mean-revert texture directly and is a natural companion: H > 0.55 confirming an ADX-trend read, or H < 0.45 confirming a Choppiness-range read, gives you two orthogonal votes for the same regime.

## Pitfalls

**Lag is unavoidable.** Every detector confirms a regime *after* it has begun. You will always give back some of the move at each turn. Accept it; the alternative — anticipating regimes — is just prediction, and prediction near turning points is unreliable. Optimising a detector to be faster usually just makes it noisier.

**Whipsaw at the boundary.** Around VIX 16-18 or ADX 20-25, a detector can flip-flop bar to bar, generating costly strategy switches. Use hysteresis: require a firmer threshold to *enter* a regime than to *stay* in it (e.g. enter trend at ADX 25, exit at ADX 20), and demand N consecutive confirming bars. This dramatically cuts false switches at the price of a little more lag — a trade worth making.

**Overfitting the classifier.** Cluster into 6 exquisitely-tuned regimes on 3 years of data and you've fit noise; the labels won't generalise. Fewer, economically-meaningful states (3-4) survive out-of-sample far better than many clever ones. If you can't explain *why* a cluster is a regime, distrust it.

**Regimes are not stationary either.** The characteristics of a "bull regime" in 2017 low-vol India differ from 2020. A model calibrated on one era mislabels another. Retrain and sanity-check periodically; don't assume the thresholds are eternal.

**Data artifacts on the NSE.** Expiry days, holidays, circuit breakers, and index rebalances inject vol and gaps that fool volatility-based detectors into flagging false "crisis." Flag known-event days and treat their readings with suspicion.

**Detection ≠ profit.** Knowing the regime is worthless if you don't have a *working strategy for that regime*. Regime detection multiplies the edge of good strategies; it can't create edge from nothing. Many traders build a beautiful detector and still lose because their per-regime playbook is weak.

## Worked snippet: a soft GMM regime classifier

A compact, honest data-driven detector giving *probabilities* (so you can size continuously):

```python
import numpy as np, pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

# df: daily Nifty with 'close'; assume 'vix' column too
r = np.log(df.close).diff()
feat = pd.DataFrame({
    'ret20':  r.rolling(20).sum(),
    'vol20':  r.rolling(20).std()*np.sqrt(252),   # annualised realised vol
    'trend':  (df.close/df.close.rolling(50).mean() - 1),
    'vix':    df.vix
}).dropna()

X = StandardScaler().fit_transform(feat)
gmm = GaussianMixture(n_components=3, covariance_type='full',
                      random_state=42).fit(X)
proba = gmm.predict_proba(X)          # soft regime membership
label = gmm.predict(X)

# inspect each cluster's mean features to NAME the regimes (never trust
# the raw cluster index — cluster 0 is not inherently "bull")
centres = pd.DataFrame(
    StandardScaler().fit(feat).inverse_transform(gmm.means_),
    columns=feat.columns)
print(centres)   # read off which cluster is trend / range / stress
```

The essential discipline shown here: **you must interpret the clusters by their feature means and name them yourself.** The algorithm hands you unlabelled buckets; the trader supplies the economic meaning. And use `predict_proba`, not `predict` — a 55/45 split between range and trend should size you smaller than a 95/5, and only soft probabilities let you do that.

## Interview-ready summary

A **regime** is a persistent statistical state — bull-trend, bear-trend, range, or crisis — during which one family of strategies is rewarded and others punished. Regime detection is *classification of the present environment*, not prediction of the next bar, and it works because volatility **clusters**: variance is persistent and therefore detectable even when direction isn't. The method ladder runs from **transparent thresholds** (MA slope/stack, ADX for trend-vs-range, Choppiness Index, India VIX and ATR for vol buckets, Bollinger width for coiled states), through **data-driven statistics** (k-means/GMM clustering on return-vol-trend features, change-point detection, HMMs), to **composite scoring** that blends several votes robustly. In practice, classify the regime, *route* to the strategy that regime rewards, take only regime-consistent signals, size by how strongly your indicators agree, and match your exit style to the regime (trail in trends, fixed targets in ranges, defend in crises). The core Indian example: a calm bull Nifty (above rising 200-DMA, ADX>25, VIX~14) says buy dips and run momentum; a VIX spike from 14 to 22+ flips the detector to stress within a bar or two and says cut size and stop selling premium — potentially ₹90,000+ of drawdown avoided on a multi-lot book. Honest limits: detectors **lag** by construction, **whipsaw** at boundaries (fix with hysteresis and confirmation bars), **overfit** if you invent too many states, and are only as valuable as the per-regime playbook behind them. Detection multiplies a good strategy's edge; it cannot manufacture edge from a bad one.
