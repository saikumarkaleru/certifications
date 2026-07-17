# Stationarity, ADF & Statistical Tests

The previous two chapters both leaned on a word without fully defining it: *stationarity*. A z-score only means something if the series has a stable mean to revert to. A pairs spread is only tradable if it is stationary. Almost every statistical TA method — from Bollinger Bands to cointegration to ARIMA forecasting to volatility modelling — silently assumes some form of stationarity, and quietly falls apart when the assumption is violated. This chapter makes that assumption explicit, gives you the tests to check it (ADF, KPSS, Hurst, variance-ratio), and — most importantly for a trader — reframes stationarity not as a dry statistics-exam topic but as **the single filter that tells you which strategy family is even allowed to run today**: mean-reversion in a stationary regime, trend-following in a non-stationary one. Getting this backwards is how good setups lose money.

## The concept

A time series is **stationary** if its statistical properties do not change over time. The version that matters in practice is *weak (covariance) stationarity*, which requires three things:

1. **Constant mean** — the series oscillates around a fixed level, not a drifting one.
2. **Constant variance** — the amplitude of the fluctuations is stable (homoscedastic), not exploding or collapsing.
3. **Constant autocovariance** — the relationship between a value and its lag depends only on the *gap* between them, not on *when* you look.

Stock *prices* are the textbook example of a **non-stationary** series: they follow (approximately) a random walk with drift. Today's price is the best forecast of tomorrow's; there is no fixed mean pulling them home; the variance of the level grows with time. This is precisely why you cannot mean-revert raw prices and why "the stock is overbought at ₹1,700" is meaningless without a reference frame. Stock *returns* (first differences of log price), by contrast, are much closer to stationary — they hover around a small mean with roughly stable variance. This is the crucial distinction:

| Series | Typical order | Tradable how |
|---|---|---|
| Price level | I(1) — non-stationary, "unit root" | Trend-following; needs differencing to model |
| Returns (Δlog price) | I(0) — (approximately) stationary | Mean-reversion, volatility models, ARIMA |
| Cointegrated spread | I(0) — stationary combination of two I(1) | Pairs / stat-arb mean-reversion |
| Oscillator (RSI, z-score) | Bounded/stationary by construction | Threshold mean-reversion |

A series that must be differenced `d` times to become stationary is called **integrated of order d**, written **I(d)**. Prices are I(1); their first difference (returns) is I(0). This vocabulary is exactly what cointegration in Chapter 68 was built on.

## The method / maths (precise)

### The unit root — what we are actually testing

Model a series as a simple autoregression:

```
x_t = ρ · x_{t−1} + ε_t
```

- If **|ρ| < 1**, shocks decay and the series pulls back toward its mean → **stationary**.
- If **ρ = 1**, the series is a random walk — each shock persists forever, no reversion → **non-stationary**, it has a "**unit root**."

So "does this series have a unit root?" *is* "is it non-stationary?" The tests below are formal ways to decide between ρ = 1 (random walk) and ρ < 1 (mean-reverting).

### Augmented Dickey–Fuller (ADF)

Rewrite the AR(1) by subtracting `x_{t−1}` from both sides. Let `γ = ρ − 1`:

```
Δx_t = γ · x_{t−1} + Σ δ_i · Δx_{t−i} + (const) + (trend) + ε_t
```

The extra lagged-difference terms (`Σ δ_i Δx_{t−i}`) are the "**augmented**" part — they soak up autocorrelation so the test is valid on real, serially-correlated market data. The test focuses on `γ`:

- **Null hypothesis H₀: γ = 0** (i.e. ρ = 1) → **unit root → non-stationary.**
- **Alternative H₁: γ < 0** (ρ < 1) → **stationary.**

You compute the ADF t-statistic on `γ`. Because under the null the distribution is *not* the usual t-distribution, you compare against **Dickey–Fuller critical values** (or just read the p-value). The decision rule:

> **If p-value < 0.05 (statistic more negative than the critical value) → reject H₀ → the series is stationary.**
> **If p-value ≥ 0.05 → fail to reject → treat as non-stationary (has a unit root).**

A common trap: "fail to reject" does **not** prove non-stationarity; it means you lack evidence of stationarity. ADF has notoriously low power — it struggles to reject the null on short samples or on slowly-reverting series. That is why you pair it with a confirmatory test.

### KPSS — the complement

The **Kwiatkowski–Phillips–Schmidt–Shin (KPSS)** test flips the hypotheses:

- **Null H₀: the series IS stationary.**
- **Alternative: it has a unit root.**

Because ADF and KPSS have *opposite* nulls, using them together is far more reliable than either alone:

| ADF result | KPSS result | Conclusion |
|---|---|---|
| Reject (stationary) | Fail to reject (stationary) | **Confidently stationary** — trade mean-reversion |
| Fail to reject | Reject | **Confidently non-stationary** — trend regime |
| Reject | Reject | Conflicting → likely **difference-stationary** or structural break; investigate |
| Fail to reject | Fail to reject | Inconclusive / low power → need more data |

This 2×2 is the practical decision table every stat-TA workflow should run before choosing a strategy family.

### Hurst exponent — how strongly, not just whether

ADF/KPSS give a binary-ish verdict; the **Hurst exponent (H)** gives a *degree* of memory, which is more useful for sizing conviction:

- **H < 0.5** → mean-reverting (anti-persistent). The closer to 0, the stronger the pull-back.
- **H ≈ 0.5** → random walk, no exploitable memory.
- **H > 0.5** → trending (persistent); the closer to 1, the stronger the trend.

Estimate H via rescaled-range (R/S) analysis or via the scaling of the variance of lagged differences. A Bank Nifty intraday spread with H = 0.35 is a strong reversion candidate; a Nifty daily close with H = 0.58 leans trend. Hurst turns "stationary yes/no" into a dial you can size against.

### Variance-ratio test

The **Lo–MacKinlay variance-ratio** test checks the random-walk hypothesis directly: if a series is a random walk, the variance of its `q`-period returns should equal `q` times the variance of its 1-period returns. A ratio **below 1** indicates mean-reversion; **above 1** indicates trending/momentum. It is a robust cross-check on Hurst and, unlike ADF, is built specifically around the return-scaling behaviour traders care about.

## A worked example with data/code

Suppose we want to know whether to run a mean-reversion book on the **Bank Nifty vs Nifty spread** on daily data. The workflow:

```python
import numpy as np, pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

# spread = BankNifty - beta * Nifty  (beta from OLS, as in Ch.68)
spread = df['BANKNIFTY'] - beta * df['NIFTY']

# 1) ADF: H0 = unit root (non-stationary)
adf_stat, adf_p, *_ = adfuller(spread.dropna(), autolag='AIC')

# 2) KPSS: H0 = stationary
kpss_stat, kpss_p, *_ = kpss(spread.dropna(), regression='c', nlags='auto')

# 3) Hurst via variance of lagged differences
def hurst(ts, max_lag=40):
    lags = range(2, max_lag)
    tau  = [np.std(ts[lag:] - ts[:-lag]) for lag in lags]
    return np.polyfit(np.log(lags), np.log(tau), 1)[0]  # slope ≈ H

H = hurst(spread.dropna().values)

print(f"ADF  p={adf_p:.3f}  (want <0.05 for stationary)")
print(f"KPSS p={kpss_p:.3f}  (want >0.05 for stationary)")
print(f"Hurst H={H:.3f}      (<0.5 = mean-reverting)")
```

Suppose the output is:

```
ADF  p=0.018   → reject unit root → stationary
KPSS p=0.11    → fail to reject stationarity → stationary
Hurst H=0.38   → mean-reverting, moderately strong
```

All three agree: the spread is **stationary and mean-reverting**. You are cleared to run the z-score pairs strategy of Chapter 68 on it, and the Hurst of 0.38 says you can carry moderate conviction. Now contrast with running the identical tests on **raw Nifty daily closes**:

```
ADF  p=0.62    → fail to reject → unit root
KPSS p=0.01    → reject stationarity
Hurst H=0.57   → mild trending
```

Unanimous non-stationary verdict. Fading Nifty levels with a z-score here is statistically forbidden — the series has no stable mean, so every "2σ overbought" fade is fighting a random walk with drift. This is the concrete, testable version of Chapter 67's warning "never mean-revert a trend." The tests are the guardrail.

### Handling structural breaks

Real Indian series have **structural breaks** — the pandemic crash, a Budget shock, a large index reconstitution, a demerger. A break can make a genuinely stationary series *look* non-stationary to ADF (or vice versa), because the mean shifted once rather than wandering. Diagnose with a rolling ADF or a Chow / Zivot–Andrews break test, and either (a) test within homogeneous sub-periods, or (b) re-anchor after the break. A single COVID-scale dislocation can flip every test in your dashboard; do not read the tests without eyeballing the chart for an obvious break.

## How to use it in a real TA workflow

Stationarity testing is not an academic ritual — it is the **regime gate** at the top of the funnel. A practical daily routine:

1. **Pre-market regime check.** Run ADF + KPSS + Hurst on your operating series (index, spread, or basket) over a rolling window. The 2×2 table decides the day's playbook: stationary → mean-reversion book is live; non-stationary/trending → switch to breakout/trend-following and *disable* fade signals.
2. **Choose the right transform.** If you intend to model or forecast (ARIMA, GARCH), difference the price to returns first so the input is I(0). Feeding non-stationary prices into a regression or ML model produces **spurious relationships** — high R², meaningless predictions.
3. **Validate every reversion trade's premise.** Before trading a spread or oscillator, confirm the traded series is I(0). This is the mandatory pre-filter that Chapters 67–68 kept deferring to here.
4. **Monitor for drift.** Re-run the tests on a rolling basis. A spread whose ADF p-value creeps from 0.02 toward 0.15 is a cointegration/stationarity break in progress — the exit signal that saves you from averaging into a broken mean.
5. **Size by strength, not just direction.** Use Hurst / variance-ratio as a conviction dial: stronger anti-persistence → larger reversion size; near 0.5 → stand down (no exploitable memory).

## Honest limitations

Be clear-eyed about what these tests can and cannot do:

- **Low power.** ADF frequently fails to reject on short or slowly-mean-reverting samples. Absence of rejection is *not* proof of a random walk. Always cross-check with KPSS and Hurst; never hang a strategy on a single test.
- **Sample-length and window sensitivity.** Results swing with the lookback and the number of lags chosen. A spread can test stationary on 250 days and non-stationary on 60. Report the window; prefer results stable across several windows.
- **Structural breaks masquerade as unit roots.** A one-time regime shift fools the tests. Human chart-reading remains essential.
- **Stationarity is a property of the *sample*, not a promise about the future.** A series that has been stationary can break — markets are non-stationary at the deepest level because participants, regulation, and macro regimes change. The tests describe the past; risk management handles the future.
- **Fat tails and heteroscedasticity.** Financial returns have volatility clustering; "constant variance" is an approximation. GARCH-type models exist precisely because variance is *not* truly constant. Treat weak-stationarity conclusions as workable approximations, not laws.
- **They tell you the regime, not the trade.** Passing an ADF test does not make a spread profitable after costs; it only certifies that a mean exists to revert to. Edge still comes from entries, exits, and cost discipline.

## Interview-ready summary

- **Stationarity** = constant mean, variance, and autocovariance over time. Prices are **non-stationary (I(1), unit root)**; returns and cointegrated spreads are **stationary (I(0))**. You can only mean-revert stationary series.
- **ADF test**: H₀ = unit root (non-stationary); **p < 0.05 → reject → stationary**. The "augmented" lags remove autocorrelation. Low power — failing to reject is not proof of non-stationarity.
- **KPSS** has the *opposite* null (H₀ = stationary); run ADF + KPSS together and use the 2×2 table for a confident verdict.
- **Hurst exponent**: H < 0.5 mean-reverting, ≈ 0.5 random walk, > 0.5 trending — a conviction dial. **Variance-ratio** cross-checks the random-walk hypothesis (ratio < 1 reversion, > 1 trend).
- Workflow role: stationarity testing is the **regime gate** — it decides whether mean-reversion (Ch. 67) or pairs (Ch. 68) are even permitted today, and it flags cointegration breaks as exit signals.
- India use: test the index, the spread, or the basket pre-market; difference prices to returns before any ARIMA/ML modelling to avoid **spurious regression**; watch for **structural breaks** (COVID, Budget, reconstitution) that fool the tests.
- Honest limits: low power, window sensitivity, break-vulnerability, and the deep truth that stationarity is a property of the past sample, never a guarantee about the future — which is why risk management, not the test, has the final word.
