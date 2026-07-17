# ML Features from Technical Data

## The concept: garbage in, garbage out — features are 80% of the work

Every practitioner who has ever tried to point a machine-learning model at a price chart eventually collides with the same brutal truth: the model is only as good as the numbers you feed it, and raw OHLCV (open, high, low, close, volume) is almost never those numbers. A model does not "see" a chart the way you do. It sees a table of floats. If you hand it a column of Nifty closing prices — 24,180, 24,205, 24,150, 24,310 … — the model learns almost nothing useful, because the *level* of the index carries no repeatable, generalisable information. Nifty at 24,000 in 2024 is a completely different regime from Nifty at 8,000 in 2016, yet numerically the model treats 8,000 as "smaller" and tries to interpolate. That is the single most common rookie mistake in market ML.

**Feature engineering** is the discipline of transforming raw market data into numbers that (a) are stationary or near-stationary, (b) encode the behaviour a discretionary trader actually reacts to, and (c) are computed without peeking into the future. In quant TA, feature engineering routinely accounts for 70–80% of whatever edge the final model has. The algorithm — logistic regression, gradient boosting, a neural net — is often the *least* important choice. This chapter is about building a clean, honest, India-aware feature set from technical data, and about the traps that silently destroy backtests.

We will assume you already know the *indicators* themselves (RSI, ADX, ATR, Bollinger Bands, VWAP, supertrend, OI) from earlier volumes. Here we care about how to turn them into model-ready **features**, and — critically — how to avoid poisoning them.

## Why raw price is the wrong input: stationarity

A time series is **stationary** when its statistical properties (mean, variance) don't drift over time. Price is emphatically non-stationary — it trends, it compounds, it changes scale by orders of magnitude. Machine-learning models, especially tree-based and linear ones, implicitly assume that a feature value of X means the same thing in the training set and in live trading. Price violates that.

The classic fix is to work with **returns** instead of levels:

- Simple return: `r_t = (C_t / C_{t-1}) − 1`
- Log return: `lr_t = ln(C_t / C_{t-1})`

Log returns are additive across time (a 5-day log return is the sum of five daily log returns) and roughly symmetric, which is why quants prefer them. For Nifty, a daily log return of +0.008 means the same thing whether the index is at 8,000 or 24,000. That is stationarity — and it is the foundation of every good feature below.

But returns alone throw away *memory*. A pure return series is close to white noise; it forgets that price is 3% below its 50-day average. Marcos López de Prado's work on **fractional differentiation** addresses exactly this — differentiate just enough to make the series stationary (pass an ADF test) while retaining as much memory as possible, using a fractional order `d` (say 0.4) rather than the full first difference `d=1`. For most retail-scale TA-ML, you don't need fractional differencing; you can get memory back through *ratio features* (price relative to a moving average) which are naturally stationary.

## Categories of technical features

Think in families. A robust feature set samples across all of them so the model isn't over-reliant on one behaviour.

**1. Return & momentum features**
- Log returns over multiple horizons: 1, 2, 3, 5, 10, 20 days.
- Cumulative return over N bars (momentum).
- Rate of change: `ROC_n = C_t / C_{t-n} − 1`.
- Distance from moving average, as a *ratio*: `C_t / SMA_50 − 1`. This is far better than raw SMA. A value of −0.03 means "3% below the 50-DMA" and is comparable across all price levels and all instruments.

**2. Volatility features**
- ATR normalised by price: `ATR_14 / C_t` (so it's a percentage, comparable across Reliance at ₹2,900 and IRFC at ₹150).
- Realised volatility: standard deviation of log returns over a rolling window, annualised by ×√252.
- Bollinger Band width: `(Upper − Lower) / Middle`.
- High-low range as fraction of close: `(H_t − L_t) / C_t`.
- Parkinson / Garman-Klass estimators if you want efficiency from OHLC.

**3. Trend / directional features**
- ADX (already a bounded 0–100 oscillator — model-friendly).
- Slope of a linear regression over the last N closes, normalised by price.
- Supertrend distance: `(C_t − Supertrend_t) / C_t`.
- Count of consecutive up/down closes.

**4. Oscillator / mean-reversion features**
- RSI, Stochastic %K, %D, Williams %R — all already bounded, use directly.
- Z-score of price: `(C_t − SMA_n) / σ_n` — how many standard deviations from the mean. This single feature is one of the most predictive mean-reversion inputs on Indian large-caps and on Bank Nifty intraday.
- Distance from VWAP (intraday): `(C_t − VWAP_t) / VWAP_t`.

**5. Volume & participation features**
- Volume ratio: `V_t / SMA(V, 20)` — today's volume vs its own norm.
- On-balance-volume slope.
- Volume-weighted return.

**6. India-specific / F&O features** (a genuine edge NSE data gives you)
- Change in open interest, normalised: `ΔOI / OI_{t-1}`.
- Price-OI quadrant encoded as a categorical: long build-up (price↑ OI↑), short build-up (price↓ OI↑), long unwinding (price↓ OI↓), short covering (price↑ OI↓).
- PCR (put-call ratio) and its z-score.
- India VIX level and its 1-day change — a powerful regime feature; Bank Nifty behaves completely differently when VIX is 11 vs 22.
- Rollover percentage near expiry, days-to-expiry as a cyclical feature.
- FII/DII net cash flows (daily) — slower but real.

**7. Calendar / seasonality features**
- Day of week, day of month, month — encoded cyclically with sine/cosine so the model understands that Friday is adjacent to Monday: `sin(2π·dow/5)`, `cos(2π·dow/5)`.
- Expiry-week flag (weekly Bank Nifty / Nifty expiries dominate Indian intraday behaviour).
- Budget day, RBI policy day flags.

## Normalisation and scaling — done without cheating

Linear models, SVMs, k-NN and neural nets need features on comparable scales; tree models (random forest, XGBoost, LightGBM) are scale-invariant and don't strictly need it. Common approaches:

- **Standardisation (z-score):** `(x − μ) / σ`.
- **Min-max:** `(x − min) / (max − min)`.
- **Rank / quantile transform:** convert each feature to its percentile rank in a rolling window — extremely robust to outliers, which markets produce constantly (think 4 June 2024, election-result day, when Nifty gapped and swung ~8% intraday).

The non-negotiable rule: **fit the scaler on training data only, then apply it to validation/test.** If you compute μ and σ over the *entire* dataset including future rows, you have leaked information from the future into the past. Your backtest will look brilliant and your live trading will bleed. More on this next.

Even better for markets: use **rolling / expanding** normalisation. Compute the z-score of RSI using only the trailing 252 days. This way every feature value is knowable at that bar in real time, and the scaling adapts to regime.

## The cardinal sin: look-ahead bias and leakage

This is the section that separates people who make money from people who make beautiful equity curves that never survive contact with a broker. **Look-ahead bias** (a.k.a. data leakage) is when a feature or label contains information that would not have been available at the moment the trade is placed.

Concrete Indian examples, each of which I have seen destroy a strategy:

1. **Using the day's close to trade the day's open.** If your feature is `today's close > today's SMA20` and you "enter at today's open", you used a value from 3:30 PM to trade at 9:15 AM. Fix: features must be computed on *closed* bars, and the trade executes on the *next* bar.

2. **Centred indicators.** A centred moving average or a zig-zag/pivot indicator that repaints uses future bars by construction. Never feed a repainting indicator to a model as a feature.

3. **Global scaling.** As above — `StandardScaler().fit(all_data)` leaks the future mean.

4. **Adjusted-price splits done wrong.** Corporate action adjustments (splits, bonuses — very common on NSE) applied retroactively can inject information. Ensure adjustment factors known only after the event aren't used to label earlier bars in a way that reveals the event.

5. **Survivorship bias in the universe.** If you build features on today's Nifty 50 constituents and backtest over 10 years, you have silently excluded the Yes Banks and DHFLs that got kicked out — inflating results.

6. **Label leakage via overlapping windows.** If your label is "20-day forward return" and your samples are daily, consecutive labels overlap by 19 days. This inflates apparent sample size and correlates errors; use event-based sampling or sample weights.

The mechanical discipline: for every feature, ask "at bar *t*, at the exact second I would act, is every input to this number already printed and final?" If the answer is no, the feature is poison.

## Multicollinearity and feature redundancy

Technical indicators are notoriously redundant. RSI, Stochastic, Williams %R and CCI are near-linear transforms of the same recent-price information. Feeding 40 correlated oscillators to a linear model produces unstable, uninterpretable coefficients; to a tree model it dilutes importance and encourages overfitting.

Tactics:
- Compute a correlation matrix; when two features exceed |ρ| ≈ 0.9, drop one.
- Use **feature importance** (from a tree model) or **permutation importance** to rank and prune.
- Principal Component Analysis (PCA) can compress a block of oscillators into 2–3 orthogonal components — though you sacrifice interpretability, which discretionary traders hate.
- Prefer a *small, diverse* set: one momentum, one volatility, one trend, one mean-reversion, one volume, one OI feature often beats forty oscillators.

Parsimony is not just elegance. Every extra feature is another axis along which the model can memorise noise. With Indian daily data you might have only ~2,500 usable rows for a single instrument over a decade — that is a *tiny* dataset by ML standards, and it cannot support 50 features without overfitting.

## Worked India example: a Bank Nifty daily feature table

Let's build a compact, leak-free feature set for Bank Nifty daily bars, aimed at a swing model that decides whether to hold long into the next 5 sessions. Suppose the latest closed bar (say a Wednesday) shows:

- Close = 51,200; previous close = 50,850.
- SMA20 = 50,400; SMA50 = 49,900.
- ATR14 = 720.
- RSI14 = 61.
- 20-day σ of log returns = 0.011.
- India VIX = 13.4 (prev 14.1).
- Nifty Bank futures OI up 6% vs prior day, price up → long build-up.
- Two trading days to weekly expiry.

The engineered feature row (all knowable at that close, used to trade *next* day's open):

| Feature | Formula | Value |
|---|---|---|
| Log return 1d | ln(51,200/50,850) | +0.0069 |
| Dist from SMA20 | 51,200/50,400 − 1 | +0.0159 |
| Dist from SMA50 | 51,200/49,900 − 1 | +0.0261 |
| ATR% | 720/51,200 | 0.0141 |
| Realised vol (ann.) | 0.011 × √252 | 0.175 |
| RSI14 | (bounded) | 61 |
| Price z-score (20) | (51,200−50,400)/(0.011×51,200) | ≈ +1.42 |
| VIX level | raw | 13.4 |
| VIX Δ | 13.4 − 14.1 | −0.7 |
| OI quadrant | categorical | long_build_up |
| Days to expiry | count | 2 |
| DoW sin | sin(2π·3/5) | −0.951 |

Notice every feature is dimensionless or bounded, comparable to the same feature computed in 2019 when Bank Nifty was at 30,000. The z-score of +1.42 flags a modest stretch above the mean; the long build-up plus falling VIX is a bullish confluence; two days to expiry warns of gamma-driven whippiness. This is a table a model can *learn from* — and one you could sanity-check by eye, which matters because you should never trust a feature you can't reason about.

## A minimal, honest code snippet

```python
import numpy as np
import pandas as pd

def make_features(df):
    # df indexed by date, columns: open, high, low, close, volume
    f = pd.DataFrame(index=df.index)
    c = df['close']

    # Returns / momentum (stationary)
    f['ret_1']  = np.log(c / c.shift(1))
    f['ret_5']  = np.log(c / c.shift(5))
    f['roc_20'] = c / c.shift(20) - 1

    # Distance from moving averages (ratio = stationary)
    f['d_sma20'] = c / c.rolling(20).mean() - 1
    f['d_sma50'] = c / c.rolling(50).mean() - 1

    # Volatility
    tr = pd.concat([df['high'] - df['low'],
                    (df['high'] - c.shift()).abs(),
                    (df['low']  - c.shift()).abs()], axis=1).max(axis=1)
    f['atr_pct'] = tr.rolling(14).mean() / c
    f['rvol']    = f['ret_1'].rolling(20).std() * np.sqrt(252)

    # Mean reversion
    m20, s20 = c.rolling(20).mean(), c.rolling(20).std()
    f['zscore'] = (c - m20) / s20

    # Volume participation
    f['vol_ratio'] = df['volume'] / df['volume'].rolling(20).mean()

    # Calendar (cyclical)
    dow = df.index.dayofweek
    f['dow_sin'] = np.sin(2 * np.pi * dow / 5)
    f['dow_cos'] = np.cos(2 * np.pi * dow / 5)

    return f.dropna()   # drop warm-up rows; NEVER forward-fill features

feat = make_features(banknifty)
# CRITICAL: shift features by 1 so bar-t features predict bar t+1
X = feat.shift(1).dropna()
```

The `feat.shift(1)` at the end is the whole ballgame: it guarantees the features used to predict day *t* come from day *t−1* and earlier. Miss this and everything downstream lies to you.

## How to use these features in a real TA workflow

1. **Compute on closed bars only,** store to a feature store (even a CSV or a small SQLite table keyed by date and symbol).
2. **Split chronologically** — train on 2015–2021, validate 2022–2023, test 2024–2025. Never shuffle time-series rows randomly; that leaks the future.
3. **Fit scalers/encoders on the training slice**, persist them, reuse identically in live.
4. **Audit each feature's live availability** — write the code so the *same function* produces features in backtest and in the live loop. Divergence between research and production code is where most silent leakage lives.
5. **Keep the feature set small and interpretable** so that when the model does something, you can look at the feature row and understand why. In Indian markets — thin mid-caps, expiry-day gamma, event gaps — an interpretable model that you can override beats a black box you must obey.

## Pitfalls — a checklist

- Feeding raw price levels or raw index values (non-stationary). Use returns and ratios.
- Global normalisation (leaks future statistics). Use train-only or rolling.
- Repainting indicators (zig-zag, non-causal filters). Banned as features.
- Too many correlated oscillators. Prune to a diverse handful.
- Tiny datasets (single stock, daily) with dozens of features. Overfitting is guaranteed.
- Ignoring survivorship and corporate-action adjustment in the Indian universe.
- Overlapping labels inflating sample counts.
- Forgetting the final `shift(1)` — the most common leak of all.
- Assuming intraday features (VWAP distance) are usable for gap-prone opens; NSE gaps regularly on global cues, so an intraday mean-reversion feature can be meaningless across the overnight break.

## Interview-ready summary

Feature engineering is where most of the edge in technical-data ML actually lives — usually 70–80% of it. Raw price is non-stationary and useless as a direct input; transform it into stationary features: log returns, ratios to moving averages, z-scores, normalised ATR, and bounded oscillators. Sample across families — momentum, volatility, trend, mean-reversion, volume — and add India-specific signal from F&O (ΔOI, PCR, India VIX, days-to-expiry) and calendar effects (expiry week, encoded cyclically). Normalise using train-only or rolling statistics, never global ones. Prune redundant, collinear features to a small interpretable set, because Indian single-instrument datasets are small and overfit easily. Above all, hunt look-ahead bias relentlessly: every feature must be final and knowable at the instant of the trade, features must predict the *next* bar (the `shift(1)` discipline), and the same code must generate features in research and in production. Get the features clean and honest, and even a simple model can work; get them wrong, and no algorithm will save you.
