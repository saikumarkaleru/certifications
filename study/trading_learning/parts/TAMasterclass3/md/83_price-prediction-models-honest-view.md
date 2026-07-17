# Price-Prediction Models: An Honest View

## The concept: why this chapter is mostly a warning

If you have spent any time on YouTube or LinkedIn, you have seen the thumbnails: "I built an LSTM that predicts Nifty with 98% accuracy." "This AI forecasts stock prices — get rich." Almost all of it is nonsense, and this chapter exists to explain *precisely why*, using real mathematics rather than cynicism — and then to describe the narrow, honest ways that predictive modelling can add value in a technical-analysis workflow.

The uncomfortable central fact is this: **price levels are extremely close to a random walk, and forecasting the next price is very nearly impossible with any useful precision.** This is not a failure of your model, your GPU, or your feature set. It is a structural property of a liquid, competitive market like Nifty or Bank Nifty. Understanding *why* the impressive-looking models are illusions is more valuable than any model itself, because it inoculates you against a genre of self-deception that has cost retail traders enormous amounts of money.

We will look at three things: the random-walk / efficiency argument, the specific ways price-prediction models fool their builders (and this is a rich catalogue), and finally the legitimate, humble uses — volatility forecasting, distributional forecasting, and regime detection — where prediction genuinely helps.

## The random walk and weak-form efficiency

A **random walk** models price as `P_t = P_{t-1} + ε_t`, where `ε_t` is unpredictable noise. If price truly follows a random walk, then the best possible forecast of tomorrow's price is *today's price*. No amount of past-price data helps, because the increments are independent.

Real markets aren't a perfect random walk — there are mild autocorrelations, momentum and mean-reversion effects, microstructure patterns — but they are *astonishingly close*, especially at the level of price. The **weak-form efficient market hypothesis** says past prices are already reflected in the current price, so you cannot systematically profit from price history alone. In practice Indian markets are weak-form efficient to a very high degree at daily resolution for liquid names; the exploitable inefficiencies are small, fleeting, and mostly live in microstructure, events, and cross-asset relationships — not in "the chart predicts the level."

The mathematical consequence is devastating for naive prediction. If daily Nifty returns have a standard deviation around 0.9–1.1%, then even a *good* directional model with 55% accuracy leaves enormous unpredictable variance in the *level*. Predicting the level to within a few points is not a slightly-hard problem; it is essentially forecasting the noise, which by construction cannot be done.

## The naive-forecast trap: how "98% accurate" models lie

Here is the most important single idea in this chapter. Consider a model that predicts tomorrow's Nifty close from a window of past closes — a common LSTM tutorial setup. You train it, you plot predicted-vs-actual, and the two lines lie almost perfectly on top of each other. The R² is 0.98. The mean absolute percentage error is 0.7%. It looks miraculous.

It is a mirage, and here is the exact mechanism. Because price is near a random walk, the best predictor of tomorrow is *today's value*. Any model fed recent prices quickly learns the laziest possible rule: **"predict tomorrow ≈ today."** Its "prediction" is essentially the previous value shifted forward by one bar. When you overlay predicted vs actual, the prediction line looks like the actual line lagged by one day — and lagged-by-one on a slow-moving series looks like a near-perfect fit. The 98% R² is measuring the model's ability to copy yesterday, not to forecast tomorrow.

You can expose the fraud in two ways:

1. **Compare to the naive baseline.** The naive forecast is "tomorrow = today." Compute the model's error and the naive model's error on the *same* test set. In almost every honest test, the fancy LSTM's error is equal to or *worse* than "tomorrow = today." If your model can't beat that trivial baseline, it has learned nothing.

2. **Predict returns, not prices.** Transform the target to next-day return (a near-stationary, near-zero-mean series). Now the R² collapses to ~0.00–0.02, and you see the truth: there is almost no predictable structure in the level. All that apparent 98% accuracy lived entirely in the persistence of price, not in any forecasting skill.

This is not a subtle bug. It is the *default outcome* of price-level prediction, and it is why so much published and marketed "AI stock prediction" is worthless. The chart looks incredible precisely *because* the model has failed to do anything useful.

## Other ways predictive models fool their builders

Beyond the naive-forecast trap, a whole ecosystem of self-deception:

- **Look-ahead leakage** (covered earlier) — scaling with future statistics, using the close to trade the open. Inflates results silently.
- **Overfitting to a lucky sample.** Deep networks have millions of parameters; a decade of daily Nifty is ~2,500 rows. The model can memorise the training set perfectly and generalise not at all. On a shuffled test set it looks fine (leakage); on a true forward slice it fails.
- **Backtest overfitting via multiple trials.** Try 500 architectures/hyperparameters, keep the best on the test set, and you have simply found the configuration that best fits the test set's noise. López de Prado's "deflated Sharpe ratio" and the "probability of backtest overfitting" quantify how much you must discount a result for the number of trials — and it is a lot.
- **In-sample vs out-of-sample confusion.** Reporting metrics on data the model trained on. Always meaningless.
- **Ignoring transaction costs.** A model with a 0.05% edge per trade is profitable in a spreadsheet and bankrupt after STT, GST, exchange charges and slippage.
- **Regime dependence.** A model trained through 2020–2021's liquidity-fuelled bull run predicts "up" beautifully — until 2022. Markets are non-stationary; yesterday's fitted relationships expire.
- **Survivorship and selection bias** in the universe and in which "successful" models get shown.

The common thread: the market is an adaptive, adversarial, near-efficient system. Any genuine edge in price prediction is small, decays as others find it, and is easily swamped by these methodological errors that all point in the flattering direction.

## Time-series models and where they actually stand

- **ARIMA** (AutoRegressive Integrated Moving Average) — the classical linear workhorse. On price levels it essentially reduces to the random-walk / naive forecast; on returns it finds, at best, tiny autocorrelations of marginal economic value after costs. Worth knowing; rarely worth trading on price alone.
- **LSTM / GRU / Transformers** — sequence models capable of learning non-linear temporal patterns. Genuinely powerful in domains with real signal (language, some sensor data). On daily price levels they collapse to the naive forecast; on returns they find little; and they overfit ferociously on small financial samples. They are *not* magic, and the marketing around them is the most misleading in the entire field.
- **Prophet and similar decomposition tools** — designed for business series with strong seasonality and trend (web traffic, sales). Markets have weak, unstable seasonality; Prophet tends to fit smooth trends that look plausible and predict poorly. Not appropriate for tradable price forecasting.

None of this means neural nets are useless in markets. It means **predicting the price level is the wrong target.** Point the same tools at better-posed problems and they earn their keep.

## The honest, useful applications

Prediction *does* add value — just not where the hype points. The reliable wins:

**1. Volatility forecasting.** Unlike returns, volatility is *strongly* predictable — it clusters. Big moves follow big moves; calm follows calm. This is real, robust, and exploitable. **GARCH** models formalise it:

`σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}`

Tomorrow's variance depends on today's shock and today's variance. GARCH and its cousins (EGARCH for asymmetry — Indian equity vol rises more on down moves) forecast the *range*, not the direction. This is directly tradable: option strategy selection (sell premium when GARCH forecasts falling vol relative to India VIX's implied level; buy vol/straddles when it forecasts a jump), position sizing (smaller size when forecast vol is high), and stop placement (wider stops in high-vol regimes). Forecasting that Bank Nifty's next-day range will expand is a genuine, monetisable edge — and it says nothing about which way.

**2. Distributional / probabilistic forecasting.** Instead of a point estimate, forecast the *distribution* of next-period return — a mean near zero but a well-estimated spread and skew. **Quantile regression** or a model outputting prediction intervals lets you say "80% chance Nifty closes within 24,000–24,450 tomorrow." That is honest and useful — it prices your risk and frames option strikes — precisely because it refuses to pretend to know the point.

**3. Regime detection.** Classify the market's *state* — trending vs mean-reverting, high-vol vs low-vol, risk-on vs risk-off — using **Hidden Markov Models** or clustering. You are not predicting the price; you are identifying which playbook applies. This is one of the most practical ML contributions to a discretionary Indian workflow: "we are in a low-vol grind-up regime, so favour buy-the-dip and premium-selling" vs "we've flipped to a high-vol trend-down regime, favour momentum shorts and long vol." Regime models are imperfect and lag turns, but they add real structure.

**4. Directional classification with humility** — the previous chapter's approach. A 55% edge, sized and filtered properly, is worth far more than any 98%-R² price line, because it is *real*.

## Worked India example: naive baseline vs "AI"

Take Nifty daily closes, 2015–2025. Build the fashionable thing: an LSTM on a 60-day window of scaled closes predicting the next close. Then build the trivial thing: "tomorrow = today." Evaluate both on a true out-of-sample 2024–2025 slice.

```python
import numpy as np

# actual next-day closes on the test slice
actual = nifty_close.loc['2024':'2025'].values

# Naive baseline: predict tomorrow = today
naive_pred = nifty_close.shift(1).loc['2024':'2025'].values

def mae(a, p):
    m = ~np.isnan(p)
    return np.mean(np.abs(a[m] - p[m]))

print("Naive MAE (points):", round(mae(actual, naive_pred), 1))
# ... train LSTM, get lstm_pred on same slice ...
# print("LSTM  MAE (points):", round(mae(actual, lstm_pred), 1))

# Now the honest test — predict RETURNS
ret = np.log(nifty_close / nifty_close.shift(1))
# Fit any model to predict ret_{t+1} from features; measure R^2 out-of-sample.
# Reality: R^2 hovers around 0.00-0.02.  There is almost no level-predictable signal.
```

The naive MAE on Nifty in this range might be roughly 120–160 points (that's just the typical daily move). The LSTM's MAE comes out *about the same or slightly worse* — because it is doing the same thing (copying today) with extra noise and lag. Plotted on price, both lines hug the actual beautifully; on returns, both explain essentially nothing. That side-by-side is the most important experiment in this book: run it once yourself and you will never be fooled by a "prediction" chart again.

By contrast, fit a GARCH(1,1) to the same Nifty returns and forecast next-day volatility, and you get a genuinely useful, statistically significant forecast: high-vol days cluster, the model's forecast tracks realised range with real skill, and you can trade the *size* of the move even though the *direction* remains unforecastable.

## How to use prediction honestly in a TA workflow

1. **Never trade a price-level point forecast.** Treat any such model as suspect until it beats the naive "tomorrow = today" baseline out-of-sample — which it almost never does.
2. **Forecast what is forecastable:** volatility (GARCH/EGARCH, or realised-vol models), distributions/quantiles, and regimes. Use these to choose strategy, size, and strikes — not entry direction.
3. **Get direction from classification** (previous chapter), with calibrated probabilities and a walk-forward, cost-aware backtest.
4. **Always benchmark against the trivial model** — naive forecast for price, "always predict the base rate / majority regime" for classes. If you can't beat trivial, you have nothing.
5. **Discount for trials.** The more models you tried, the more you must haircut the winner. Keep a final untouched hold-out and, ideally, a live paper-trading period before real capital.
6. **Respect non-stationarity.** Retrain, monitor for decay, and stand down around events the model has never seen.

## Pitfalls

- Believing a high R² or near-perfect predicted-vs-actual price chart — it is the naive-forecast artefact, not skill.
- Predicting levels instead of returns — hides the absence of signal.
- Skipping the naive baseline comparison — the single test that exposes most fakes.
- Overfitting deep nets to tiny financial datasets.
- Data-snooping across hundreds of trials and reporting the luckiest.
- Ignoring costs, non-stationarity, and regime change.
- Confusing volatility predictability (real) with return/level predictability (essentially absent).
- Trusting "AI prediction" products and courses that never show an out-of-sample return R² or a naive benchmark — that omission is the tell.

## Interview-ready summary

Price *levels* are so close to a random walk that forecasting the next price with useful precision is effectively impossible, and Indian markets are weak-form efficient enough at daily resolution that past prices alone won't predict future levels. The famous "98%-accurate" models are an artefact: fed recent prices, they learn to copy today's value, so predicted-vs-actual looks perfect while the model has zero forecasting skill — a fraud exposed instantly by (a) comparing to the naive "tomorrow = today" baseline, which it fails to beat, and (b) re-targeting *returns*, where R² collapses to near zero. ARIMA, LSTMs, Transformers and Prophet all reduce to this on price levels and overfit badly on small samples. The honest, valuable applications point elsewhere: **volatility is strongly predictable** (GARCH/EGARCH — trade the range, size, strikes, and stops), distributional/quantile forecasts price your risk honestly, regime models (HMM/clustering) tell you which playbook to run, and directional *classification* with humility gives a small but real edge. The professional's stance is not "I can predict the price" — it is "I cannot predict the level, but I can forecast volatility, estimate a distribution, identify the regime, and tilt the odds — and I always beat the naive baseline before I risk a rupee."
