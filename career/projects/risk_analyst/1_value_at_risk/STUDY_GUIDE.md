# Study Guide — Value at Risk (VaR)

## 30-second pitch
"I built a market-risk engine for an eight-stock, one-million-dollar equity
portfolio. It computes one-day Value-at-Risk and Expected Shortfall three ways —
historical, variance-covariance, and Monte Carlo — then decomposes the risk by
stock and *backtests* the model with the Kupiec and Christoffersen tests to prove
the number is actually reliable. It pulls live prices, falls back to cached or
synthetic data if the network is down, and exports a formatted Excel workbook and
charts."

## What it is
Value-at-Risk answers one question: **"On a normal day, how much could I lose?"**
A 1-day 95% VaR of $18,000 means: on 95% of days the loss should be smaller than
$18,000; roughly 1 day in 20 it will be worse. Expected Shortfall (ES / CVaR)
answers the follow-up: **"When it *is* a bad day, how bad on average?"** — the
mean loss in that worst 5% tail.

## The key interview answer
There is no single "true" VaR — it depends on your assumptions, so I compute it
three ways and cross-check them:
- **Historical** makes no distribution assumption; it just reorders the actual
  past returns and reads off the 5th percentile. Honest about fat tails, but
  limited to what already happened.
- **Parametric (variance-covariance)** assumes returns are normal. Portfolio
  volatility is `sqrt(wᵀ Σ w)`, and VaR = `-(μ_p + z·σ_p)`, where at 95% the
  normal quantile `z ≈ -1.645`. Fast and analytic, but understates tail risk.
- **Monte Carlo** simulates 50,000 correlated return scenarios by multiplying
  independent normals through the Cholesky factor `L` of the covariance matrix
  (`sim = μ + L·z`), aggregates to the portfolio, and reads the empirical
  quantile. Flexible; here it should closely match the parametric number because
  both assume normality — that agreement is itself a sanity check.

## Code walkthrough
- **`data.py`** — downloads 2.5 years of adjusted closes via yfinance, computes
  simple daily returns, caches to `input/prices.csv`, and if all else fails
  generates a *synthetic* correlated dataset from plausible vols and a
  hand-built correlation matrix. Always prints LIVE / CACHED / SYNTHETIC.
- **`var_methods.py`** — the maths. Includes scipy-free normal `pdf/cdf/ppf`
  (Moro's rational approximation for the inverse-normal), the three VaR methods,
  historical + parametric ES, component/marginal VaR, and rolling VaR.
- **`backtest.py`** — walks forward estimating VaR on a trailing 250-day window,
  counts exceptions, and runs Kupiec, Christoffersen, and combined tests. The
  chi-square p-value comes from a hand-written regularised incomplete gamma.
- **`reporting.py`** — openpyxl workbook (Returns, VaR_Summary, Component,
  Backtest) and three matplotlib charts.
- **`main.py`** — orchestrates everything and prints the console summary.

## Interview Q&A
1. **Why is parametric VaR usually the smallest?** It assumes normal returns,
   which have thin tails; real markets have fat tails, so historical VaR that
   captures actual crash days is often larger.
2. **What does the covariance matrix buy you?** Diversification. Portfolio risk
   `sqrt(wᵀΣw)` is less than the weighted sum of individual risks because the
   off-diagonal correlations are below 1. That cross-term is the whole point.
3. **What is Cholesky doing in the Monte Carlo?** `Σ = L Lᵀ`. Multiplying
   independent standard normals by `L` injects the correct correlations and
   volatilities, so simulated assets move together the way the real ones do.
4. **Component vs marginal VaR?** Marginal VaR is the sensitivity of portfolio
   VaR to a tiny increase in one holding. Component VaR = weight × marginal, and
   the component VaRs *sum to total VaR* (Euler's theorem). It tells you which
   position to trim to cut risk fastest — here NVDA and the tech names dominate.
5. **What is a VaR "exception" and why backtest?** An exception is a day the loss
   exceeded the VaR forecast. A 95% model should breach ~5% of days. Backtesting
   checks the model is neither too optimistic nor too conservative — regulators
   require it (Basel traffic-light).
6. **Kupiec vs Christoffersen?** Kupiec (POF) tests only the *count* of
   exceptions (unconditional coverage). Christoffersen adds *independence* —
   exceptions shouldn't cluster (which would signal the model ignores volatility
   regimes). The combined `LR_cc = LR_uc + LR_ind` tests both at once (2 df).
7. **VaR vs Expected Shortfall — why care?** VaR ignores how bad the tail is and
   isn't sub-additive (can penalise diversification). ES averages the tail loss,
   is coherent, and is now the Basel FRTB standard. I report both.

## Vocabulary
- **VaR** — worst expected loss at a confidence level over a horizon (here 1 day).
- **Expected Shortfall / CVaR** — average loss *given* you're in the tail beyond VaR.
- **Variance-covariance (delta-normal)** — analytic VaR assuming normal returns,
  using `σ_p = sqrt(wᵀΣw)`.
- **Cholesky decomposition** — factor `Σ = L Lᵀ`; used to generate correlated draws.
- **Monte Carlo** — VaR from many simulated scenarios rather than a formula.
- **Marginal VaR** — sensitivity of portfolio VaR to one asset's weight.
- **Component VaR** — each asset's additive share of total VaR (sums to total).
- **Backtesting exceptions** — days where realised loss beat the VaR forecast.
- **Kupiec POF** — likelihood-ratio test on the *number* of exceptions.
- **Christoffersen** — likelihood-ratio test on exception *independence* /
  conditional coverage.
- **Confidence level** — 95% or 99%; the probability the loss stays within VaR.
