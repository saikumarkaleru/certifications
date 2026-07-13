# Python for Finance III: Analysis

## What it is & where it's used

This chapter is where Python stops being a fancy calculator and starts *answering business questions that have money attached*: **What will next quarter's revenue be? How risky is this portfolio? What actually drives our costs?**

Four techniques carry most of the load in a finance/FP&A/analytics seat:

| Technique | The question it answers | Library |
|---|---|---|
| **Regression** | "How much does X move Y?" (drivers, sensitivity, beta) | `statsmodels`, `scikit-learn` |
| **Time-series / forecasting** | "What's the number for next month?" | `statsmodels` (ARIMA, ETS) |
| **Monte Carlo simulation** | "What's the *range* of outcomes, not one guess?" | `numpy` |
| **Simple trend/seasonality decomposition** | "Is this growth real or just December?" | `statsmodels` |

Who pays for this: **FP&A analysts** (revenue/expense forecasts), **credit & risk teams** (default probability, VaR), **treasury** (cash-flow forecasting), **equity research** (beta, factor models), **corporate finance** (DCF with simulated scenarios). In India, this is the difference between a ₹6 LPA "Excel MIS" analyst and a ₹14–20 LPA "FP&A / analytics" analyst doing the same numbers with rigour.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you *regression theory* (R², t-stat, p-value) on a clean dataset in a stats exam, and *forecasting* as "take a growth rate and extrapolate." Industry needs the opposite skill: messy monthly data, and a defensible number you can put in a board deck.

The specific gaps:

- **College gave you point estimates; the business wants ranges.** "Revenue will be ₹52 Cr" is a liability. "₹48–56 Cr, 80% confidence" is analysis. Monte Carlo closes this and is almost never taught.
- **You learned regression to *test a hypothesis*; finance uses it to *drive a model*.** Nobody in FP&A cares about your p-value on a slide — they care that "every ₹1 of ad spend returns ₹3.20 of revenue, and here's the confidence interval."
- **Excel's forecast tools are a black box.** `FORECAST.ETS` gives a number with no diagnostics. When the CFO asks "why is the forecast flat?", you need to *see* the trend and seasonal components — statsmodels shows them.
- **Seasonality is ignored.** Freshers extrapolate a December spike into a full-year run-rate. Decomposition prevents this embarrassing mistake.

## What "proficient" looks like

A job-ready person can, unaided:

- Load a monthly revenue/cost series into a pandas DataFrame with a proper `DatetimeIndex`.
- Fit an **OLS regression**, read the coefficients *as business levers*, and quote the confidence interval — not just recite R².
- Decompose a series into **trend + seasonality + residual** and say whether growth is structural.
- Fit a **Holt-Winters (ETS)** or **ARIMA** model and produce a forecast *with a prediction interval*.
- Build a **Monte Carlo** simulation of an NPV, portfolio return, or budget line and report P10/P50/P90.
- Say out loud what could make the forecast wrong (regime change, one-off events).

The bar is *interpretation*, not memorising library syntax. You can Google `.fit()`; you can't Google "what this coefficient means for our pricing."

## Hands-on: how to actually do it

Setup:

```python
import pandas as pd, numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
```

### 1. Regression (drivers & sensitivity)

Say you want to know how **ad spend** and **price discount** drive **units sold**.

```python
df = pd.DataFrame({
    "units":    [1200, 1500, 1400, 1800, 2100, 1950, 2300, 2500],
    "adspend":  [50,   65,   60,   80,   95,   88,   110,  120],   # ₹ '000
    "discount": [5,    8,    6,    10,   12,   9,    14,   15],     # %
})

model = smf.ols("units ~ adspend + discount", data=df).fit()
print(model.summary())
print(model.params)          # the business levers
print(model.conf_int())      # 95% confidence interval per driver
```

Read it like this: the `adspend` coefficient (say `14.2`) means **each extra ₹1,000 of ad spend sells ~14 more units**. That sentence is what goes in the deck. `model.pvalues` under 0.05 = the driver is statistically real; `model.rsquared` = share of variation explained.

Predict for a planned scenario:

```python
scenario = pd.DataFrame({"adspend": [130], "discount": [16]})
model.get_prediction(scenario).summary_frame(alpha=0.20)  # 80% interval
```

### 2. Time-series decomposition (is the trend real?)

```python
rev = pd.read_csv("monthly_revenue.csv", parse_dates=["month"], index_col="month")
rev = rev.asfreq("MS")   # month-start frequency — statsmodels needs this

from statsmodels.tsa.seasonal import seasonal_decompose
dec = seasonal_decompose(rev["revenue"], model="additive", period=12)
dec.trend; dec.seasonal; dec.resid    # plot with dec.plot()
```

If `dec.trend` slopes up while `dec.seasonal` shows a December bump, you know the growth is structural and December is just seasonal — don't annualise December.

### 3. Forecasting with Holt-Winters (ETS)

Best default for monthly business data with trend + seasonality:

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

fit = ExponentialSmoothing(
    rev["revenue"], trend="add", seasonal="add", seasonal_periods=12
).fit()

forecast = fit.forecast(6)        # next 6 months
print(forecast.round(0))
```

For a prediction interval, use ARIMA/SARIMAX:

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX
sar = SARIMAX(rev["revenue"], order=(1,1,1),
              seasonal_order=(1,1,1,12)).fit(disp=False)
pred = sar.get_forecast(6)
pred.predicted_mean                    # the forecast
pred.conf_int(alpha=0.20)              # 80% band — this is what CFOs want
```

### 4. Monte Carlo simulation (the range, not the point)

Simulate NPV of a project where revenue and cost are uncertain:

```python
np.random.seed(42)
N = 50_000
rev  = np.random.normal(500, 60, N)      # ₹ Lakh, mean 500, sd 60
cost = np.random.normal(320, 40, N)      # ₹ Lakh
disc = 0.12
years = 5

cashflow = rev - cost                     # annual, ₹ Lakh
npv = sum(cashflow / (1+disc)**t for t in range(1, years+1))

print(f"P10: ₹{np.percentile(npv,10):.0f} L")
print(f"P50: ₹{np.percentile(npv,50):.0f} L")
print(f"P90: ₹{np.percentile(npv,90):.0f} L")
print(f"P(NPV<0): {(npv<0).mean():.1%}")   # probability of loss
```

That last line — **"11% chance this project loses money"** — is worth more than any single-point NPV.

## Worked example / mini-project: forecast + risk a ₹ retail chain's revenue

You run FP&A for a 20-store apparel chain. You have 36 months of revenue and need a **12-month forecast with a risk band** for the annual budget.

**Step 1 — build the data (reproducible):**

```python
import pandas as pd, numpy as np
idx = pd.date_range("2023-01-01", periods=36, freq="MS")
np.random.seed(7)
trend = np.linspace(180, 260, 36)                       # ₹ Lakh, growing
season = 40*np.sin(np.arange(36)*2*np.pi/12) + \
         np.where(pd.Series(idx).dt.month==10, 60, 0)   # Diwali (Oct) spike
noise = np.random.normal(0, 10, 36)
rev = pd.Series((trend+season+noise).round(1), index=idx, name="revenue").to_frame()
rev = rev.asfreq("MS")
```

**Step 2 — decompose to confirm the Diwali seasonality:**

```python
from statsmodels.tsa.seasonal import seasonal_decompose
seasonal_decompose(rev["revenue"], model="additive", period=12).seasonal.head(12)
# October seasonal factor is large & positive → real festive uplift
```

**Step 3 — forecast next 12 months with an 80% band:**

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX
m = SARIMAX(rev["revenue"], order=(1,1,1), seasonal_order=(1,1,0,12)).fit(disp=False)
fc = m.get_forecast(12)
out = pd.concat([fc.predicted_mean.rename("base"),
                 fc.conf_int(alpha=0.20)], axis=1).round(0)
print(out)
annual_base = fc.predicted_mean.sum()
print(f"FY budget (base): ₹{annual_base:.0f} L")
```

**Step 4 — Monte Carlo the annual total** (because point forecasts lie):

```python
resid_sd = m.resid.std()
sims = fc.predicted_mean.values[:, None] + \
       np.random.normal(0, resid_sd, (12, 20_000))
annual = sims.sum(axis=0)
print(f"Budget P10 ₹{np.percentile(annual,10):.0f} L | "
      f"P50 ₹{np.percentile(annual,50):.0f} L | "
      f"P90 ₹{np.percentile(annual,90):.0f} L")
```

**The deliverable sentence:** *"FY revenue budget of ₹3,180 L (base), with an 80% range of ₹2,980–3,390 L. October carries a ~₹60 L festive uplift; a stretch target above ₹3,390 L is < 10% likely."* That is FP&A, not MIS.

## How it's tested

**Interview questions:**

- "Difference between R² and adjusted R²? Why prefer adjusted when adding variables?"
- "Your forecast says revenue drops next month but the business is growing — how do you debug it?" (Answer: check seasonality, check for a stationarity/differencing issue, look at residuals.)
- "What's a prediction interval and why is it more useful than a point forecast to a CFO?"
- "You have monthly sales for 2 years. Walk me through building a forecast." (They want: inspect → decompose → choose ETS/ARIMA → validate on a hold-out → forecast with interval.)
- "Explain Monte Carlo to a non-technical CEO in 30 seconds."

**Practical/take-home tests:**

- A CSV of 24–48 months of revenue: *"Forecast the next 6 months and justify your method."* Graded on validation (did you hold out the last 6 months and check error?), not on the model name.
- A regression screen: *"Here are marketing spend and sales — quantify the ROI per rupee and state your confidence."*
- A risk case: *"Given these cost/price distributions, what's the probability this launch is NPV-negative?"* — pure Monte Carlo.

Pro move in any test: **always back-test.** Fit on data up to month N-6, forecast the last 6 months you *do* have, and report MAPE. Showing `mean(abs((actual-pred)/actual))` proves the model, and freshers never do it.

## Common mistakes & how pros avoid them

| Mistake | Why it's wrong | The fix |
|---|---|---|
| No `DatetimeIndex` / no `.asfreq()` | statsmodels forecasts silently break or mis-align | Always `parse_dates`, set index, `.asfreq("MS")` |
| Reporting a point forecast only | Hides all risk; CFO gets blindsided | Always attach a prediction interval / P10–P90 |
| Extrapolating a seasonal spike | Annualising Diwali/December = wild over-forecast | Decompose first; forecast on de-seasonalised logic |
| Confusing correlation with driver | "Ad spend correlates" ≠ "ad spend causes" | State assumptions; watch for omitted variables |
| Overfitting ARIMA orders | Great fit, garbage forecast | Back-test on hold-out; prefer simple orders |
| Monte Carlo with wrong distribution | Normal on bounded/skewed data lies | Use lognormal/triangular where appropriate; sanity-check tails |
| Not setting a random seed | Results change every run; not reproducible | `np.random.seed(...)` in any deliverable |

## Learn-it roadmap & resources

**Realistic time-to-proficiency (assuming you can already do pandas from Chapters 04–05):**

| Phase | Time | Milestone |
|---|---|---|
| Regression with statsmodels | 1 week | Read a `.summary()`, interpret coefficients as business levers |
| Decomposition + ETS/ARIMA | 2 weeks | Forecast a real monthly series with a validated hold-out |
| Monte Carlo | 3–4 days | Simulate an NPV/portfolio, report P10/P50/P90 |
| Portfolio project | 1 week | End-to-end forecast+risk memo on your own data |

**≈ 5–6 weeks part-time** to interview-ready.

**Resources (free-first):**

- **statsmodels docs** — the time-series and OLS example galleries are excellent and free.
- **"Forecasting: Principles and Practice" (Hyndman)** — free online, the standard text. It's in R but the concepts (ETS, ARIMA, back-testing) map 1:1 to statsmodels.
- **Kaggle** — "Store Sales" / retail time-series datasets to practice on real messy data.
- **QuantEcon** (free) — for Monte Carlo and numpy-heavy finance.
- **Certification worth having:** none specific to this; a **Google Data Analytics** or **CFA Level I quant** signal helps in India, but a GitHub repo with one clean forecast+Monte-Carlo notebook beats any cert in interviews.

## Quick-reference

```python
# --- Regression ---
import statsmodels.formula.api as smf
m = smf.ols("y ~ x1 + x2", data=df).fit()
m.summary(); m.params; m.pvalues; m.conf_int(); m.rsquared_adj
m.get_prediction(new_df).summary_frame(alpha=0.20)   # 80% interval

# --- Prep a series ---
s = df.set_index("month").asfreq("MS")["revenue"]

# --- Decompose ---
from statsmodels.tsa.seasonal import seasonal_decompose
seasonal_decompose(s, model="additive", period=12).plot()

# --- Forecast: Holt-Winters ---
from statsmodels.tsa.holtwinters import ExponentialSmoothing
ExponentialSmoothing(s, trend="add", seasonal="add",
                     seasonal_periods=12).fit().forecast(6)

# --- Forecast: SARIMAX (with interval) ---
from statsmodels.tsa.statespace.sarimax import SARIMAX
f = SARIMAX(s, order=(1,1,1), seasonal_order=(1,1,1,12)).fit(disp=False)
f.get_forecast(6).predicted_mean
f.get_forecast(6).conf_int(alpha=0.20)

# --- Monte Carlo NPV ---
np.random.seed(42)
cf = np.random.normal(180, 30, 50_000)
npv = sum(cf/(1.12)**t for t in range(1,6))
np.percentile(npv,[10,50,90]); (npv<0).mean()

# --- Back-test (always do this) ---
train, test = s[:-6], s[-6:]
pred = ExponentialSmoothing(train, trend="add", seasonal="add",
        seasonal_periods=12).fit().forecast(6)
mape = (abs((test-pred)/test)).mean()   # < 0.10 is good
```

| Concept | Rule of thumb |
|---|---|
| R² vs adj-R² | Use adjusted when comparing models with different # of variables |
| p-value | < 0.05 → driver is statistically real |
| Prediction interval | Always report; `alpha=0.20` = 80% band |
| MAPE | < 10% good, 10–20% acceptable, > 20% rethink |
| Monte Carlo output | Report P10 / P50 / P90 + probability of loss |
| Seasonality | Decompose before forecasting monthly data |
| Reproducibility | `np.random.seed()` on every deliverable |
