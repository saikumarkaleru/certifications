# Forecasting & Rolling Forecasts

## What it is & where it's used

A forecast is your best current estimate of where the numbers will land — revenue, costs, cash, headcount — given what you know today. It is different from a **budget** (a fixed annual target, locked once) and from **actuals** (what happened). FP&A lives in the gap between them: budget vs actual vs forecast.

A **rolling forecast** drops the "we plan once a year in October and pray" model. Instead you always look 12–18 months ahead, re-forecasting every month or quarter, so the horizon "rolls" forward and never shrinks to zero in December.

Where it shows up on the job:

- **FP&A analyst / manager** — owns the monthly re-forecast and the board deck.
- **Business finance / finance business partner** — forecasts a specific P&L (a region, a product line, a plant).
- **Startup finance / founder's office** — cash runway and revenue forecasts for investors.
- **Treasury** — 13-week cash-flow forecast.
- **Corporate development / IB** — the operating model behind a DCF is a forecast.

If a job description says "variance analysis," "driver-based planning," "cash flow forecasting," or "management reporting," this chapter is the core skill.

## The gap: why companies want this (and college didn't teach it)

College hands you a completed cash-flow statement and asks you to compute a ratio. Employers hand you a blank sheet and last year's messy actuals and say "tell me what Q3 looks like, and defend it." That is a completely different muscle.

Specifically, the gaps:

| College taught | The job needs |
|---|---|
| One "correct" answer | A defensible *estimate* with assumptions written down |
| Static full-year budget | A living forecast updated monthly |
| Revenue as a single number | Revenue broken into **drivers** (units × price, or leads × conversion × ARPU) |
| Ignore what already happened | **Run-rate** the year-to-date actuals into the remaining months |
| Model never checked again | **Forecast accuracy** measured and improved each cycle |

The commercial reason companies pay for this: a forecast that is wrong by 15% every quarter causes the wrong hiring, the wrong inventory buy, and a missed loan covenant. A finance person who forecasts within ±3–5% and *explains the miss* is directly protecting cash and credibility.

## What "proficient" looks like

A job-ready person can, unaided:

1. Take 6 months of actuals + a budget and produce a full-year forecast in Excel with a clean **actuals | forecast** split (bold vertical line at the current month).
2. Choose the right method per line: **run-rate** for stable overheads, **driver-based** for revenue and variable cost.
3. Build a **rolling 12-month** version where changing "current month" re-slices actual vs forecast automatically.
4. Track **forecast accuracy** (MAPE / bias) and show whether they consistently over- or under-call.
5. Write a 5-bullet assumptions box a non-finance manager can challenge.
6. Explain a variance in business language: "Revenue is ₹4L below forecast because conversion dropped from 3.0% to 2.4%, not because traffic fell."

## Hands-on: how to actually do it

### 1. Run-rate (simplest, for stable lines)

Run-rate = annualize what's happened so far. If YTD actual through month `n` is known:

```excel
' YTD actual in B2, current month number in B3 (e.g. 6)
=B2 / B3 * 12                       ' straight run-rate for the full year
=B2 + (B2 / B3) * (12 - B3)         ' actual-to-date + run-rate for remaining months
```

Use run-rate for rent, salaries, subscriptions, insurance — costs that don't swing with volume.

### 2. Driver-based (for revenue and variable cost)

Break the number into the levers a manager actually controls. For a D2C business:

```
Revenue = Sessions × Conversion% × Average Order Value
```

```excel
' Sessions C2, Conversion C3, AOV C4
=C2 * C3 * C4
```

For variable cost tie it to the same driver:

```excel
' Units D2, cost per unit D3
=D2 * D3
```

The power: to model a scenario you change *one driver*, not 40 output cells.

### 3. The actuals-vs-forecast switch (the heart of a rolling model)

Put a single cell `CurrentMonth` (say = 6). Each month column knows if it's actual or forecast:

```excel
' Row of month numbers in C1:N1 (1..12), CurrentMonth in $B$1
' Actual row C2:N2, Forecast-logic below
=IF(C$1 <= $B$1, C_actual, C_forecast)
```

A cleaner pattern using named cells and SWITCH-style logic:

```excel
=IF(C$1<=$B$1, INDEX(Actuals,C$1), INDEX(ForecastDrivers,C$1))
```

Then a live "Full Year" column blends both:

```excel
' Actuals for elapsed months + forecast for the rest
=SUMPRODUCT((MonthNums<=CurrentMonth)*ActualRow)
 + SUMPRODUCT((MonthNums>CurrentMonth)*ForecastRow)
```

### 4. Forecast accuracy (MAPE and bias)

Once actuals land, score last cycle's forecast:

```excel
' Actual A2:A13, Forecast F2:F13
' MAPE  (lower = better; <5% is strong for revenue)
=AVERAGE(ABS(A2:A13 - F2:F13) / A2:A13)     ' enter as array / dynamic array
' Bias  (positive = you over-forecast on average)
=AVERAGE((F2:F13 - A2:A13) / A2:A13)
```

### 5. SQL to pull the actuals your forecast rests on

```sql
SELECT DATE_TRUNC('month', txn_date) AS month,
       SUM(amount)                   AS revenue,
       COUNT(DISTINCT order_id)      AS orders
FROM sales
WHERE txn_date >= '2025-04-01'      -- Indian FY start
GROUP BY 1
ORDER BY 1;
```

### 6. Python for a quick trend / seasonal forecast

```python
import pandas as pd

df = pd.read_csv("monthly_revenue.csv", parse_dates=["month"])
df = df.set_index("month").asfreq("MS")

# 3-month moving-average run-rate
df["run_rate"] = df["revenue"].rolling(3).mean()

# simple seasonal index (this month vs 12-month avg)
df["seasonal_idx"] = df["revenue"] / df["revenue"].rolling(12).mean()
print(df.tail())
```

### 7. DAX (Power BI) — actual vs forecast in one measure

```dax
Actual or Forecast =
IF (
    MAX ( 'Calendar'[MonthNum] ) <= [Current Month],
    [Actual Revenue],
    [Forecast Revenue]
)

MAPE =
AVERAGEX (
    VALUES ( 'Calendar'[MonthNum] ),
    DIVIDE ( ABS ( [Actual Revenue] - [Forecast Revenue] ), [Actual Revenue] )
)
```

## Worked example / mini-project

**Business:** a Bengaluru D2C skincare brand. FY26 (Apr–Mar). You have actuals Apr–Sep; forecast Oct–Mar.

**Actuals (₹, revenue):**

| Month | Sessions | Conv% | AOV (₹) | Revenue (₹) |
|---|---|---|---|---|
| Apr | 80,000 | 2.8% | 950 | 21,28,000 |
| May | 85,000 | 2.9% | 940 | 23,17,100 |
| Jun | 82,000 | 2.7% | 960 | 21,25,440 |
| Jul | 90,000 | 3.0% | 970 | 26,19,000 |
| Aug | 95,000 | 3.1% | 980 | 29,58,100 |
| Sep | 98,000 | 3.0% | 990 | 29,10,600 |

YTD actual revenue = **₹1,50,58,240**.

**Driver forecast Oct–Mar** — assumptions written down:
- Sessions grow 3% MoM (festive push Oct–Nov, +8% those two months).
- Conversion holds at 3.0%.
- AOV rises ₹10/month.

| Month | Sessions | Conv% | AOV (₹) | Forecast Rev (₹) |
|---|---|---|---|---|
| Oct | 1,05,840 (+8%) | 3.0% | 1,000 | 31,75,200 |
| Nov | 1,14,307 (+8%) | 3.0% | 1,010 | 34,63,500 |
| Dec | 1,17,736 (+3%) | 3.0% | 1,020 | 36,02,720 |
| Jan | 1,21,268 | 3.0% | 1,030 | 37,47,180 |
| Feb | 1,24,906 | 3.0% | 1,040 | 38,97,070 |
| Mar | 1,28,653 | 3.0% | 1,050 | 40,52,570 |

Forecast H2 = **₹2,19,38,240**. **Full-year forecast = ₹3,69,96,480.**

**Now the accuracy check.** Say last year you forecast Sep at ₹27,50,000 and actual came in ₹29,10,600:

```
Error% = (27,50,000 - 29,10,600) / 29,10,600 = -5.5%  (you under-forecast)
```

Do this for all six actual months, average the absolute values → your MAPE. If it's 4.2%, you tell the board: "Historical forecast accuracy is ~96%; treat the ₹3.70 Cr as ±₹15L."

**Reproduce it:** put months across columns, `CurrentMonth=6`, drivers in a block, and one `IF(month<=6, actual, driver_forecast)` row. Add a MAPE cell. That single tab is a legitimate portfolio piece.

## How it's tested

**Interview questions:**
- "Walk me through building a revenue forecast for a business you know." (They want *drivers*, not "I'd grow it 10%.")
- "Difference between budget, forecast, and actual?"
- "Your forecast was off by 12% — how do you find out why?" (Bridge it by driver.)
- "Run-rate vs driver-based — when each?"
- "What's a rolling forecast and why bother?"

**Practical assessments (very common in FP&A hiring):**
- **Timed Excel case (45–60 min):** given raw actuals + a budget, build a full-year forecast with an actuals/forecast split and a variance column. Scored on structure, correct `SUMPRODUCT`/`IF` logic, and a written assumptions box.
- **"Break this forecast" exercise:** they hand you a model and ask what's wrong (hardcoded numbers inside formulas, no assumptions tab, circular references).
- **Variance bridge:** turn a ₹4L revenue miss into a volume/price/mix waterfall.
- **Case presentation:** 3–5 slides — forecast, key drivers, risks, ask. Communication is graded as heavily as the math.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Hardcoding numbers inside formulas (`=C2*1.1`) | Every assumption lives in its own labelled cell; formulas only reference cells |
| No assumptions tab | One box: growth %, conversion, AOV, headcount plan — dated and initialled |
| Forecasting the total, not the drivers | Always decompose: units × price, or funnel steps |
| Ignoring YTD actuals — re-forecasting from budget | Anchor on actuals; only the *remaining* months are forecast |
| Straight-lining seasonal businesses | Apply a seasonal index; festive/quarter-end spikes are real in India |
| Never scoring past accuracy | Track MAPE + bias each cycle; a persistent bias means fix the method |
| Sandbagging (deliberately low) or hockey-sticks | Bias metric exposes it; pros forecast the honest number and flag risk separately |
| One number, no range | Give base / best / worst, or "±X% based on historical accuracy" |

Pros also keep a **version log** — snapshot each month's forecast so you can see how your Dec call for full-year revenue drifted from Aug to Nov. That drift *is* the story the CFO wants.

## Learn-it roadmap & resources

**Time to job-ready: 4–8 weeks** of deliberate practice if your Excel is already decent.

| Week | Focus |
|---|---|
| 1 | Excel mechanics: `INDEX`, `SUMPRODUCT`, `IF`, `XLOOKUP`, dynamic arrays; build a run-rate |
| 2 | Driver-based revenue model + assumptions tab |
| 3 | Rolling 12-month structure with the `CurrentMonth` switch |
| 4 | Variance bridge + MAPE/bias tracking |
| 5–6 | Full mini-project (like above) end to end; write the assumptions & risks |
| 7–8 | Power BI/DAX or Python version; present a 3-slide case out loud |

**Resources:**
- *Free:* Corporate Finance Institute (CFI) FP&A free lessons; Microsoft's Excel forecast docs; `statsmodels`/`pandas` docs for Python; any real company's investor deck (reverse-engineer their drivers).
- *Paid / high-signal:* CFI **FMVA** certification (financial modeling + FP&A modules), Wall Street Prep FP&A course, Rob Marlow / Leila Gharani Excel on YouTube (free but excellent).
- *Cert worth naming on a resume in India:* FMVA (CFI). Your CA Intermediate + MBA already cover the accounting depth — the modeling cert closes the "can you build it in Excel" question.

Build one public forecast model (dummy or a listed company's segment) and put it on GitHub/LinkedIn. That artifact beats any line on a CV.

## Quick-reference

| Need | Formula / step |
|---|---|
| Straight run-rate (full year) | `=YTD / MonthNo * 12` |
| Actual + run-rate remainder | `=YTD + (YTD/MonthNo)*(12-MonthNo)` |
| Driver revenue | `=Sessions * Conv% * AOV` |
| Actual/forecast switch | `=IF(Month<=CurrentMonth, Actual, Forecast)` |
| Blended full year | `=SUMPRODUCT((M<=Cur)*Act)+SUMPRODUCT((M>Cur)*Fcst)` |
| MAPE | `=AVERAGE(ABS(Act-Fcst)/Act)` (array) |
| Bias | `=AVERAGE((Fcst-Act)/Act)` |
| Variance % | `=(Actual-Forecast)/Forecast` |

**Rules of thumb:** revenue MAPE < 5% is strong; run-rate stable overheads, driver-model everything volume-linked; anchor on actuals and only forecast the remaining months; every assumption in its own cell; snapshot each forecast version; always give a range, never a false single point.
