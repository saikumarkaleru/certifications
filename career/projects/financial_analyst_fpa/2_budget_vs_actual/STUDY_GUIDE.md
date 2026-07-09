# Study Guide — Budget vs Actual with Variance Analysis

Everything you need to defend this project line-by-line in an interview.
Plain English, no jargon left unexplained. Company modelled:
**Meridian Instruments Co.** (synthetic, seeded data).

---

## 1. The 30-second pitch

"I built a driver-based budget-versus-actual model — the core monthly job in
FP&A. It plans four product lines across four cost centres and twelve months,
where revenue is built from price × volume (not typed in), simulates actual
results with realistic drift, and then runs the whole variance toolkit: dollar
and percent variances flagged favorable/unfavorable, a **price / volume / mix**
decomposition of the revenue variance that reconciles exactly to the total, a
**flex budget** that separates the volume effect from the rate effect, a
**rolling reforecast** of the remaining months, auto-written commentary, and a
CFO KPI summary. It's a `src/` package with unit tests, and the data is seeded
so it always runs offline and reproduces the same numbers. I can explain every
line."

---

## 2. What budget-vs-actual / variance analysis is, and why FP&A lives in it

A **budget** is the financial plan set before the year starts: expected revenue
and planned spend per line. **Actuals** are what really happened. A **variance**
is the difference: `Actual − Budget`.

FP&A (Financial Planning & Analysis) runs this comparison every month during the
"close." The point is never the arithmetic — it's the *story*. Variance analysis
answers the three questions leadership always asks:

1. **Are we on plan?** (Did we hit revenue? Did we overspend?)
2. **Why did we deviate?** (More units, or higher price? A richer product mix?
   Is a cost overrun a one-off or a new run-rate?)
3. **What now?** (Reforecast, cut spend, chase upside, reprice.)

Without variance analysis a budget is a document you file in January and forget.
Variance analysis is what turns the plan into a management tool that drives
decisions all year. This is *the* daily reality of an FP&A analyst, which is why
the whole project is built around it.

---

## 3. THE key interview answer — Price / Volume / Mix decomposition

This is the centrepiece. When you sell more than one product, a revenue miss or
beat has **three** possible causes, and a strong analyst can separate them:

- **Price** — we charged a different price than planned.
- **Volume** — we sold a different *total* number of units (mix held constant).
- **Mix** — we sold a different *blend* of products (e.g. more of the cheap
  line, less of the premium one) at the same total units.

Using full-year figures per product *p* (with `budget_mix[p] = budget_units[p] /
total_budget_units`):

```
Price[p]  = (actual_price[p]  − budget_price[p]) × actual_units[p]
Mix[p]    = (actual_units[p]  − total_actual_units × budget_mix[p]) × budget_price[p]
Volume[p] = (total_actual_units − total_budget_units) × budget_mix[p] × budget_price[p]
```

**Why it reconciles EXACTLY.** Sum the three effects across all products and the
algebra collapses:

```
Σ Price  = Σ actual_price·actual_units − Σ budget_price·actual_units
Σ Mix    = Σ budget_price·actual_units − total_actual_units × budget_avg_price
Σ Volume = total_actual_units × budget_avg_price − total_budget_units × budget_avg_price
```

Add them and every middle term cancels, leaving:

```
Σ(Price + Volume + Mix) = Σ actual_price·actual_units − Σ budget_price·budget_units
                        = Total Actual Revenue − Total Budget Revenue
                        = Total Revenue Variance     ✓
```

Each effect measures its factor while holding the others at a defined base
(actual units for price, budget mix for volume, budget price for mix), so there
is no double-counting — the pieces tile perfectly. The unit test asserts the
residual is ~0 both per product and in total, so a coding slip can't hide.

**Why anyone cares:** "we beat revenue by \$105k" is not insight. "Volume added
\$370k, pricing added \$115k, but an adverse shift in *mix* cost \$380k" tells the
CFO exactly which lever to pull. In this model that mix drag is the real story
behind a modest headline beat.

---

## 4. Walkthrough of each module (`src/fpa/`)

**`budget.py` — the driver-based budget.**
Holds the drivers, never the answers: each of 4 products has an annual volume,
a price, and a unit cost. Annual volume is split across 12 months by a
**seasonality** curve (dips in summer, peaks at year-end). `revenue = price ×
volume` and `cogs = unit_cost × volume` are *derived* — that's what makes the
price/volume/mix split possible later. Four **cost centres** (Manufacturing,
Sales & Marketing, G&A, R&D) carry fixed annual opex spread over the year.
Output is two tidy (long) DataFrames: `products` and `opex`.

**`actuals.py` — the seeded simulation.**
Real life never lands on plan, so each driver drifts: a **systematic bias** (the
deliberate story — e.g. Beta holds a price premium but has a volume shortfall,
Gamma's unit cost creeps up) plus small monthly **random noise**. All randomness
comes from one `numpy` generator seeded at **42**, so the run is deterministic.
`get_datasets()` caches the budget and actuals to `input/*.csv` and reloads them
next time — the "always-runs, offline, reproducible" guarantee.

**`variance.py` — the analytical core.**
Computes variances (`Actual − Budget`) and applies the **sign convention** via
`flag()` (income vs cost). Contains `pvm_decomposition()` (section 3),
`flex_budget()` (section 5 below), the per-product and per-cost-centre variance
tables, and `kpi_summary()`.

**`reforecast.py` — the rolling reforecast (section 5).**

**`commentary.py` — auto-written English.**
Turns the variance tables into sentences ("Beta Controller revenue was −\$110k
unfavorable, driven mainly by product mix, partly offset by favorable pricing").
Building the words *from* the numbers means the narrative can never drift out of
sync with the figures.

**`reporting.py` — presentation only.**
Writes the Excel workbook (Budget, Actual, Variance, PVM, Flex, Reforecast,
KPIs) and three PNG charts: a **variance waterfall** (Budget → Price → Volume →
Mix → Actual), a budget-vs-actual **bar chart** by product, and a **monthly
trend** line. Uses matplotlib's headless "Agg" backend so it renders to file
with no screen.

**`main.py` — orchestration.**
Runs the pipeline in order and prints the console summary.

---

## 5. Flex budget and rolling reforecast (the two managerial pieces)

**Flex (flexible) budget.** The original "static" budget assumed *budget*
volumes. The **flex** budget re-states it at *actual* volumes but still at
*budget* rates. That lets us split any variance into two clean effects:

```
Volume / activity effect = Flex   − Static   (we ran at a different volume, rate fixed)
Rate / efficiency effect = Actual − Flex     (our per-unit rate differed, volume fixed)
Total variance           = Actual − Static   = activity + rate     (identity, by construction)
```

For revenue the rate effect *is* the price variance (the test checks flex rate ==
PVM price). For COGS the rate effect is a unit-cost efficiency variance. **Opex
is fixed** — it doesn't flex with sales volume, so its whole variance is a pure
spending variance. The value of a flex budget: it stops you blaming a cost
overrun on simply selling more. It answers "what *should* costs have been for the
volume we actually did?"

**Rolling reforecast.** Part-way through the year some months are closed
(actuals final) and the rest are open. The reforecast replaces the plan for the
open months with an estimate that **blends** the original budget with the trend
we're seeing YTD. We measure the trend with attainment ratios on the closed
months — `volume attainment = YTD actual units / YTD budget units`, price
realisation, cost ratio — then pull each ratio partway toward 1.0 by a weight
`alpha` (here 0.7 = "lean 70% on the trend, 30% on the plan", an explicit
judgement call). Full-year reforecast = closed actuals + reforecast of the open
months, compared back to the original budget.

---

## 6. Interview Q&A

**Q1. What's a favorable versus unfavorable variance — and the sign trap?**
The math is always `Actual − Budget`, but the label depends on line type. On an
income line (revenue, gross profit) actual *above* budget is favorable; on a cost
line (COGS, opex) actual *below* budget is favorable. So a *positive* dollar
variance is good on revenue but bad on cost. The trap is judging a variance by
its sign alone — Sales & Marketing \$142k *over* budget is a positive number but
*unfavorable*; G&A \$33k *under* budget is negative but *favorable*. My `flag()`
function encodes exactly this by taking an "income" or "cost" argument.

**Q2. Walk me through price / volume / mix.**
Revenue moves for three reasons, so I split it three ways. Price = the price gap
times actual units. Volume = the total-unit gap times budget price, holding mix
constant. Mix = the shift in product blend at budget prices. They reconcile
exactly to the total revenue variance because each effect holds the other factors
at a defined base, so nothing is double-counted — I have a unit test asserting the
residual is zero. In this model volume added ~\$370k and price ~\$115k, but an
adverse mix shift cost ~\$380k, leaving a ~\$105k net beat.

**Q3. What is a flex budget and why use it?**
A flex budget restates the plan at actual volumes but budget rates. It splits any
variance into a volume/activity effect (flex − static) and a rate/efficiency
effect (actual − flex). You use it so you don't credit or blame a cost line for
simply doing more or less business — you isolate "did we run at a different
volume?" from "were our per-unit rates off?" It's the honest way to judge cost
performance.

**Q4. How do you build a rolling reforecast?**
Take the closed months as final, measure attainment ratios on them (actual vs
budget for volume, price, unit cost), blend each ratio toward the plan by a
confidence weight alpha, apply the blended factors to the open months, and add
that to the closed actuals for a fresh full-year number. The blend keeps you from
over-reacting to a couple of noisy months while still respecting the trend.

**Q5. What drove the biggest variance in this model?**
The largest unfavorable driver is **Gamma Module COGS**, running ~\$248k over
budget — Gamma's unit cost drifted up ~5%, a margin/efficiency problem the flex
budget flags as a *rate* effect, not a volume effect. On revenue, Beta's adverse
*mix* is the notable story. That's the kind of specific, decomposed answer the
commentary and KPIs surface automatically.

**Q6. What KPIs would you show a CFO?**
Total revenue budget vs actual and the variance %, gross margin % (plan vs
actual), the opex ratio (opex / revenue), operating-profit variance, and the
single largest favorable and unfavorable drivers by operating-profit impact. That
one screen answers "are we on plan, is the margin holding, and what moved it" —
which is exactly what the KPIs sheet and the CFO summary print.

---

## 7. Vocabulary to know cold

- **Variance** — `Actual − Budget`, in dollars or as a percent of budget.
- **Favorable / Unfavorable** — whether a variance helps or hurts profit vs plan.
  Favorable = revenue above plan *or* cost below plan; unfavorable = the reverse.
  Not the same as positive/negative.
- **Price variance** — the part of a revenue/cost variance from a change in
  price/rate, holding quantity fixed.
- **Volume (quantity) variance** — the part from a change in *total* units,
  holding price and mix fixed.
- **Mix variance** — the part from selling a different *blend* of products than
  planned, separate from total-volume and price effects.
- **Static budget** — the original plan, built at *budget* volumes.
- **Flex (flexible) budget** — the plan restated at *actual* volumes but budget
  rates; used to separate volume effects from rate/efficiency effects.
- **Rolling reforecast** — an updated full-year estimate mid-year: closed
  actuals plus a fresh estimate for the open months, blending YTD trend with plan.
- **Cost centre** — an organisational unit that owns a spend budget (e.g.
  Manufacturing, S&M, G&A, R&D) but isn't measured on revenue.
- **Contribution margin** — price − variable unit cost per unit (what each unit
  contributes toward fixed costs and profit).
- **Seasonality** — the systematic within-year pattern of activity (e.g.
  year-end peak) used to spread an annual budget across months.
- **COGS** — Cost of Goods Sold: the direct cost of what you sold; scales with
  volume. **Gross Profit** = Revenue − COGS. **Operating Profit** = Gross Profit
  − operating expenses (opex).
- **Opex ratio** — operating expenses as a percent of revenue; a spend-efficiency
  gauge. **Run-rate** — annualizing a recent period to judge if a variance is a
  one-off or the new normal.
- **Attainment** — actual ÷ budget for a driver (e.g. volume attainment); the
  YTD trend signal that feeds the reforecast.
