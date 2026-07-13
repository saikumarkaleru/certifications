# Forecasting & budgeting models

## What it is & where it's used

A forecasting or budgeting model is a spreadsheet that turns **assumptions about the future** into projected P&L, and often cash flow and balance sheet. You feed it *drivers* — units sold, price, headcount, conversion rate, seasonality — and it computes revenue, cost, and margin forward in time (usually 12–36 months).

Where it lives:

- **FP&A / finance business partner** — builds the annual operating plan (AOP) and monthly rolling forecast.
- **Startup finance / founder's office** — revenue build for the board deck and runway model.
- **Corporate finance / treasury** — cash forecast, working-capital planning.
- **Investment banking / equity research** — the projection block in a DCF or three-statement model.
- **Accounts / controllership** — budget-vs-actual (BvA) variance packs each month-end.

Almost every "analyst" job in India that pays above a data-entry salary expects you to *own* a forecast, defend the numbers, and update it monthly without breaking it.

## The gap: why companies want this (and college didn't teach it)

College teaches you to **extrapolate a trend** — "revenue grew 15% last year, so grow it 15%." That is a straight-line forecast and every good FP&A lead will reject it in an interview.

The industry gap this chapter closes:

| College taught | Industry actually wants |
|---|---|
| Grow revenue by a % | **Driver-based** build: `Volume × Price`, `Traffic × Conv × AOV` |
| One annual number | **Monthly granularity** with seasonality |
| A static budget locked in April | A **rolling forecast** re-cut every month |
| "Forecast = prediction" | Forecast = a **structured set of assumptions you can defend and flex** |
| Hardcoded numbers in cells | Clean **assumptions tab**, blue inputs, black formulas, no hardcodes in calc cells |

The commercial reason companies care: a driver-based model lets leadership ask *"what if we hire 3 fewer salespeople?"* and get an answer in 10 seconds. A trend line can't do that. That flex-ability is the paid skill.

## What "proficient" looks like

A job-ready person can, unaided:

1. Separate **inputs (assumptions)** from **calculations** from **outputs** on distinct tabs, with a consistent colour convention.
2. Build a **revenue driver tree** — not one growth %, but the 2–4 levers that actually move revenue.
3. Apply **monthly seasonality** using a seasonality index (12 factors that average to 1.0).
4. Build a **12-month budget** that footsends (rows and columns cross-check to the same total).
5. Convert that budget into a **rolling forecast**: actuals replace forecast as months close, and a new month is added at the far end.
6. Build a **budget-vs-actual variance** view with % variance and a favourable/adverse flag.
7. Never hardcode a number inside a formula; every input traces to the assumptions tab.

## Hands-on: how to actually do it

### 1. Driver-based revenue build

Say revenue = `Units × Price`. Put units and price on the assumptions tab, reference them in the calc.

For a subscription/SaaS or services build, use a **customer roll-forward**:

```
Opening customers  + New adds  − Churn  = Closing customers
Revenue = Avg customers in month × ARPU
```

Excel (row per month, column B = assumptions):

```excel
' Closing customers this month
=Opening + New_Adds - (Opening * Churn_Rate)

' New adds from marketing spend
=Marketing_Spend / CAC

' Revenue
=AVERAGE(Opening, Closing) * ARPU
```

For an e-commerce / retail build:

```excel
Revenue = Sessions * Conversion_Rate * Average_Order_Value
=B$4 * B$5 * B$6
```

Lock the assumption rows with `$` on the row (`B$4`) so you can drag across all 12 months.

### 2. Seasonality with an index

Build 12 seasonality factors that average to exactly 1.0. In India, festive months (Oct–Nov, Diwali) and year-end (Mar) usually spike.

```excel
' Seasonality index row (Jan..Dec), must average 1
Jan 0.85  Feb 0.80  Mar 1.20 ... Oct 1.25  Nov 1.30 ... 
' Check it averages 1.0:
=AVERAGE(B10:M10)   -> should return 1.000

' Seasonalised monthly revenue
=Annual_Revenue/12 * Seasonality_Factor
```

Derive the index from history:

```excel
Factor_for_month = Month_actual / AVERAGE(all 12 months' actual)
```

### 3. Growth over time (driver, not hardcode)

```excel
' This month's units = last month's units grown at monthly rate
=C_prev_units * (1 + MoM_growth)

' Convert an annual growth target to monthly:
=(1 + Annual_Growth)^(1/12) - 1
```

### 4. Rolling forecast switch — actual vs forecast

Add an "Actuals through" date on the assumptions tab. Each month cell picks actual if the month has closed, else forecast:

```excel
=IF(EOMONTH(MonthDate,0) <= Actuals_Through_Date, Actual_Value, Forecast_Value)
```

### 5. Budget-vs-actual variance

```excel
Variance      =Actual - Budget
Variance %    =IFERROR(Actual/Budget - 1, "")
Flag          =IF(Metric_Type="Cost", IF(Actual>Budget,"Adverse","Favourable"),
                                        IF(Actual<Budget,"Adverse","Favourable"))
```

### 6. Python — quick statistical baseline (sanity check your driver model)

```python
import pandas as pd
# monthly revenue history
s = df['revenue']
# 3-month moving average forecast
ma = s.rolling(3).mean().iloc[-1]
# seasonal-naive: same month last year
seasonal = s.shift(12).iloc[-1]
print(ma, seasonal)
```

For a proper seasonal forecast:

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing
model = ExponentialSmoothing(s, trend='add', seasonal='mul',
                             seasonal_periods=12).fit()
forecast = model.forecast(12)
```

Use this to *challenge* the business build, not replace it.

## Worked example / mini-project

**"D2C skincare brand — FY27 budget."** Reproduce this in a fresh workbook.

**Assumptions tab:**

| Driver | Value |
|---|---|
| Monthly sessions (Apr) | 4,00,000 |
| Session MoM growth | 3% |
| Conversion rate | 2.2% |
| Average order value | ₹950 |
| Gross margin | 62% |
| Marketing (% of revenue) | 18% |
| Fixed opex / month | ₹35,00,000 |

**Seasonality index (Apr…Mar):** 0.95, 0.90, 0.90, 1.00, 1.05, 1.10, **1.30, 1.25**, 1.05, 0.95, 0.90, 1.15 (avg = 1.0). The Oct–Nov spike is Diwali.

**Monthly revenue formula:**

```excel
Revenue = Sessions_this_month * Conv * AOV * Seasonality_Factor
```

Sample first quarter (rounded):

| Metric | Apr | May | Jun |
|---|---:|---:|---:|
| Sessions | 4,00,000 | 4,12,000 | 4,24,360 |
| Base revenue (₹) | 83,60,000 | 86,10,800 | 88,69,124 |
| × Seasonality | 0.95 | 0.90 | 0.90 |
| **Net revenue (₹)** | **79,42,000** | **77,49,720** | **79,82,212** |
| COGS @ 38% | 30,17,960 | 29,44,894 | 30,33,241 |
| Gross profit (₹) | 49,24,040 | 48,04,826 | 49,48,971 |
| Marketing @ 18% | 14,29,560 | 13,94,950 | 14,36,798 |
| Fixed opex | 35,00,000 | 35,00,000 | 35,00,000 |
| **EBITDA (₹)** | **-5,52,120** | **-1,90,124** | **12,173** |

Now add the **rolling forecast layer**: set `Actuals_Through_Date = 31-May-26`. Suppose actual May revenue came in at ₹82,00,000 (beat). Replace May's forecast with actual via the `IF(EOMONTH...)` switch, then re-forecast Jun–Mar off the *new* higher base. Board question you can now answer instantly: *"May beat by ₹4.5L — does that flow through the year?"* Yes, because Jun sessions grow off May.

**Variance pack for May:**

| Line | Budget | Actual | Var | Var % | Flag |
|---|---:|---:|---:|---:|---|
| Revenue | 77,49,720 | 82,00,000 | 4,50,280 | +5.8% | Favourable |
| Marketing | 13,94,950 | 15,10,000 | 1,15,050 | +8.2% | Adverse |

## How it's tested

**Interview questions:**

- "How would you forecast revenue for a business you know nothing about?" → answer with a driver tree, not a growth %.
- "Difference between a budget and a rolling forecast?" → budget is fixed annual target; rolling forecast is continuously re-cut (e.g. always 12 months ahead).
- "Your forecast beat in Q1 — how do you decide whether to raise the full-year number?" → tests whether you understand run-rate vs one-off.
- "What's a seasonality index and how do you build one?"

**Practical / take-home tests companies actually give:**

- A **timed 60–90 min Excel case**: raw monthly history in one tab, "build a 12-month driver-based forecast with seasonality and a BvA view." Graded on structure (assumptions separated), no hardcodes, and whether it *flexes* when they change an input live.
- A **"break my model"** screen: they hand you a model, change one assumption, and check your cells all update (catches hardcoders).
- FP&A rounds often include a **live case**: "walk me through your model and defend the marketing-as-%-of-revenue assumption."

## Common mistakes & how pros avoid them

| Mistake | Pro fix |
|---|---|
| Hardcoding numbers inside formulas | Every input on assumptions tab; calc cells are pure formulas. Blue = input, black = formula |
| One growth % for all revenue | Break into 2–4 real drivers |
| Seasonality factors that don't average to 1.0 | Add a `=AVERAGE()` check cell that must read 1.000 |
| Forecast doesn't foot | Cross-check: sum of months = annual; sum of segments = total |
| Rebuilding the whole model each month | Build the `IF(EOMONTH<=Actuals_Through)` switch once |
| No scenario capability | Keep a single "case" toggle driving assumptions via `CHOOSE`/`INDEX` |
| Circular references from interest-on-cash | Use a circularity switch or iterative calc deliberately, not by accident |
| Over-precision (forecasting to the rupee) | Forecast drivers, round outputs; defend ranges not points |

## Learn-it roadmap & resources

**Time to proficiency:** ~4–6 weeks part-time if you already know Excel basics.

- **Week 1:** Model structure — separate tabs, colour convention, no hardcodes. Rebuild the worked example above.
- **Week 2:** Driver trees for 3 business types (SaaS, retail, services). Build each from scratch.
- **Week 3:** Seasonality index from real history; MoM vs annual growth conversion.
- **Week 4:** Rolling forecast switch + BvA variance pack.
- **Weeks 5–6:** Add scenario toggle, connect to a simple three-statement model, do a timed 90-min case against a clock.

**Resources:**

- *Financial Modeling* — CFI (Corporate Finance Institute) FMVA track (paid, well-recognised in India).
- Wall Street Prep / Breaking Into Wall Street modeling courses (paid).
- Free: Aswath Damodaran's forecasting lectures (YouTube); Microsoft's own XLOOKUP/dynamic-array docs.
- Certification: **FMVA** (CFI) is the most portable for FP&A roles; for pure Excel, the **Microsoft Excel Expert (MO-201)** cert signals hard skills.

## Quick-reference

```excel
' Driver revenue (lock assumption row)
=Sessions * B$5_Conv * B$6_AOV * B$10_Seasonality

' Annual growth -> monthly growth
=(1+Annual_Growth)^(1/12)-1

' Grow off prior month
=Prev * (1 + MoM_Growth)

' Customer roll-forward
Closing = Opening + Adds - Opening*Churn

' Seasonality check (must = 1.000)
=AVERAGE(seasonality_range)

' Rolling forecast switch
=IF(EOMONTH(MonthDate,0)<=Actuals_Through, Actual, Forecast)

' Variance & flag
Var    =Actual-Budget
Var%   =IFERROR(Actual/Budget-1,"")
Flag   =IF(Actual>Budget,"Adverse","Favourable")   ' for costs
```

| Concept | One-liner |
|---|---|
| Budget | Fixed annual target, locked at start of year |
| Rolling forecast | Re-cut monthly, always N months ahead |
| Driver-based | Revenue = drivers multiplied, not a single % |
| Seasonality index | 12 factors averaging 1.0 applied to base |
| BvA | Budget vs Actual, with variance % and F/A flag |
| Colour code | Blue = input, black = formula, green = link |
