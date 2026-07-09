# Budget vs Actual — Variance Analysis (FP&A)

A compact but real FP&A model. It builds a **driver-based annual budget**,
simulates **actual** results with realistic drift, then runs the full monthly-close
toolkit: variances with favorable/unfavorable flags, a **Price / Volume / Mix**
decomposition of the revenue variance, a **flex (flexible) budget**, a **rolling
reforecast** of the remaining months, auto-written commentary, and a CFO KPI
summary — exported to Excel and charts.

Illustrative company: **Meridian Instruments Co.** — four product lines
(Alpha Sensor, Beta Controller, Gamma Module, Delta Analyzer) sold through four
cost centres (Manufacturing, Sales & Marketing, G&A, R&D), across 12 months.
All figures are **synthetic and seeded** (no market data — this is a budgeting model).

## What it does

- **Driver-based budget** — revenue = price × volume, COGS = unit-cost × volume,
  spread across 12 months with a seasonality curve; plus fixed cost-centre opex.
- **Seeded actuals** — each driver drifts vs plan (systematic bias + random
  noise) from a single fixed RNG, so results are identical every run.
- **Variances + flags** — Actual − Budget in $ and %, flagged Favorable /
  Unfavorable using the correct sign convention (revenue up = good; cost up = bad).
- **Price / Volume / Mix** — splits the revenue variance into three effects that
  reconcile *exactly* to the total (this is the centrepiece; a unit test proves it).
- **Flex budget** — restates the budget at actual volumes to separate the
  volume/activity effect (flex − static) from the rate/efficiency effect (actual − flex).
- **Rolling reforecast** — treats the first 6 months as closed and reforecasts
  the rest, blending YTD trend with the original plan.
- **Commentary + KPIs** — plain-English sentences per product and a CFO summary
  (revenue, gross margin, opex ratio, largest favorable/unfavorable drivers).

## How to run

```
python main.py
```

Only `numpy`, `pandas`, `matplotlib`, and `openpyxl` are required. **No network.**
The data is deterministic-simulated with a fixed seed (**seed = 42**) and cached
to `input/*.csv`, so the model always runs offline and reproduces identical
numbers. Tests:

```
python -m pytest tests/ -q          # or: python tests/test_variance.py
```

## Module map

```
main.py                 orchestrates the whole pipeline + prints the console summary
src/fpa/
  budget.py             driver-based annual budget (products + cost-centre opex, seasonality)
  actuals.py            seeded actuals simulation + CSV cache/load (get_datasets)
  variance.py           variances, F/U flags, Price/Volume/Mix, flex budget, KPIs
  reforecast.py         rolling reforecast of the remaining months
  commentary.py         auto-generated English commentary + KPI narrative
  reporting.py          Excel workbook + matplotlib charts (waterfall, bars, trend)
tests/
  test_variance.py      PVM reconciliation, flex reconciliation, sign convention, determinism
input/                  cached budget & actual CSVs (deterministic)
output/                 generated Excel + PNG charts
```

## Outputs

- `output/budget_vs_actual.xlsx` — sheets: **Budget, Actual, Variance, PVM, Flex,
  Reforecast, KPIs**.
- `output/variance_waterfall.png` — Budget → Price → Volume → Mix → Actual.
- `output/budget_vs_actual_by_product.png` — grouped bars by product.
- `output/monthly_revenue_trend.png` — budget vs actual revenue by month.

See `STUDY_GUIDE.md` for the interview-ready walkthrough (the Price/Volume/Mix
answer, flex-budget logic, reforecast method, and Q&A).
