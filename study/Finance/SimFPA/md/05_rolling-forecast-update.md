# The Rolling Forecast Update

## The ask

It's **10 July 2026**. Q1 (Apr–Jun) actuals are closed and the variance pack you built last week is on the CFO's desk. In the Monday review she says:

> "The budget is now stale — we missed Q1 by Rs 15 lakh. I don't want to keep reporting against a number we already know is wrong. Give me a **full-year reforecast** by Friday: Q1 actual, plus a fresh view of Q2–Q4. I need to know where we now expect to *land* on revenue and PBT, and I need one page that explains **why the landing is different from budget** so I can walk the board through it. Keep the budget frozen as the yardstick — the reforecast is a separate column."

This is the **rolling forecast**: the budget stays fixed for the year (it's the promise), but every quarter you replace one more quarter of forecast with actuals and re-drive the rest. The deliverable is a **FY2026-27 reforecast that lands ~Rs 11.7 cr** on revenue, with a defendable driver story.

## What you're given

**Budget vs Q1 actual (the anchors):**

| Line | FY Budget | Q1 Budget | Q1 Actual | Q1 Var |
|---|---:|---:|---:|---:|
| Revenue | 12.00 | 2.85 | 2.70 | (0.15) |
| — Goods | 9.00 | 2.25 | 2.10* | |
| — Services | 3.00 | 0.60 | 0.60 | on plan |
| Gross margin % | 30.0% | 30.0% | 28.5% | (1.5pp) |
| Opex (emp+other+dep) | 2.004 | ~0.50 | 0.55 | (0.05) |

*Rs cr. Goods Q1: **21,000 units vs 22,500 budget** (volume miss), realised **ASP Rs 1,020 vs Rs 1,000** (price gain partly offsetting).

**Driver read from Q1:** the volume shortfall is a **timing/demand** slip in the components line (two OEM orders pushed to Q2), not a lost account. Sales says the pipeline recovers but the full year won't fully catch up. Input costs (copper/PVC) ran hot, dragging gross margin. Two extra hires landed early (opex creep).

## Build it — step by step

**Rolling-forecast mechanics = Actual-to-date + Forecast-to-go (ATD + FTG).** In Excel the full-year cell is never hard-typed — it's `=SUM(Q1_actual, Q2_fc, Q3_fc, Q4_fc)`. A single flag cell decides, per quarter, whether to pull actual or forecast:

```
FY_col  =SUMIFS(actuals,period,"<="&last_closed) + SUMIFS(forecast,period,">"&last_closed)
```

**Step 1 — Re-drive the goods volume.** Budget was 90,000 units evenly (22,500/qtr). Reforecast: Q1 actual 21,000; the two pushed orders lift Q2, then a steady recovered run-rate:

| Goods units | Q1 | Q2 | Q3 | Q4 | FY |
|---|---:|---:|---:|---:|---:|
| Budget | 22,500 | 22,500 | 22,500 | 22,500 | 90,000 |
| Reforecast | 21,000 (A) | 21,300 | 21,500 | 21,500 | **85,300** |

Full-year units **85,300 vs 90,000 = −5,200 (−5.8%)** — we do *not* pretend Q1 fully recovers.

**Step 2 — Hold the ASP gain.** The Rs 1,020 realised price holds (a genuine list-price improvement, not a one-off). Goods reforecast = `85,300 × 1,020 = Rs 8.70 cr` (budget 9.00). Services stay on plan at **Rs 3.00 cr**.

`Revenue reforecast = 8.70 + 3.00 = Rs 11.70 cr` — the landing.

**Step 3 — Re-drive margin.** Q1 came in at 28.5%. Procurement has hedged part of the copper exposure, so H2 recovers toward budget but the full year is still below. Blend to **29.0%** → GP = `11.70 × 29.0% = Rs 3.393 cr`; COGS = Rs 8.31 cr.

**Step 4 — Re-drive opex.** The two early hires stick: employee cost `1.08 → 1.10`. Other opex, depreciation, finance cost held at budget (capex and the term loan are on schedule).

**Step 5 — Roll to PBT/PAT.**

```
EBIT = GP − Emp − Other − Dep = 3.393 − 1.10 − 0.78 − 0.144 = 1.369
PBT  = EBIT − Finance = 1.369 − 0.09 = 1.279
PAT  = PBT × (1 − 26%) ≈ 0.94   (25% + 4% cess)
```

## The deliverable

**FY2026-27 Reforecast (Rs cr) — budget frozen as yardstick:**

| Line | Budget | Q1 Actual | Q2–Q4 FTG | **Reforecast** | Var vs Bud | % |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 12.00 | 2.70 | 9.00 | **11.70** | (0.30) | −2.5% |
| COGS | (8.40) | (1.93) | (6.38) | **(8.31)** | 0.09 | |
| Gross profit | 3.60 | 0.77 | 2.62 | **3.39** | (0.21) | −5.8% |
| Gross margin % | 30.0% | 28.5% | 29.2% | **29.0%** | (1.0pp) | |
| Employee | (1.08) | (0.28) | (0.82) | **(1.10)** | (0.02) | |
| Other opex | (0.78) | (0.20) | (0.58) | **(0.78)** | — | |
| Depreciation | (0.144) | (0.036) | (0.108) | **(0.144)** | — | |
| EBIT | 1.596 | 0.254 | 1.112 | **1.366** | (0.23) | −14.4% |
| Finance cost | (0.09) | (0.022) | (0.068) | **(0.09)** | — | |
| **PBT** | **1.506** | 0.232 | 1.044 | **1.276** | **(0.23)** | **−15.3%** |
| PAT (~26%) | 1.11 | | | **0.94** | (0.17) | −15% |

**Quarter phasing of the reforecast:**

| Rs cr | Q1 A | Q2 F | Q3 F | Q4 F | FY |
|---|---:|---:|---:|---:|---:|
| Revenue | 2.70 | 2.85 | 3.05 | 3.10 | 11.70 |
| PBT | 0.23 | 0.30 | 0.36 | 0.39 | 1.28 |

**Analyst commentary (the one-pager):** "We now expect to land the year at **Rs 11.70 cr revenue (−2.5% vs budget)** and **PBT Rs 1.28 cr (−15%)**. Revenue is off by only Rs 30 lakh — the goods volume miss (85,300 vs 90,000 units, the two Q2-slipped OEM orders never fully recovered) is *partly offset* by a genuine ASP improvement to Rs 1,020 and services holding exactly on plan. **The PBT fall is 6× the revenue fall** because two forces compound below the line: (i) input-cost-driven margin down 100bps, and (ii) two hires landing a quarter early. This is operating leverage in reverse — small revenue softness, amplified at the bottom. The recovery is real but back-ended: H2 PBT run-rate returns to plan."

## How it's reviewed

The CFO's checks:
- **ATD ties to the ledger.** Q1 reforecast column must equal the closed Q1 actuals to the rupee — no "smoothing" the past.
- **Bridge closes.** Budget PBT 1.506 → reforecast 1.276. The Rs 23 lakh gap must decompose cleanly: revenue/volume, margin, opex. No plug.
- **Drivers, not a haircut.** "We took 2.5% off revenue" is rejected; "85,300 units × Rs 1,020" is accepted. Every changed number traces to a driver with an owner (Sales owns volume, Procurement owns margin, HR owns headcount).
- **Reforecast ≠ new budget.** The budget column is untouched; bonuses and board commitments still measure against it.
- **Directional sense:** revenue −2.5% but PBT −15% must be *explained*, not buried.

## Common mistakes & red flags

- **Re-opening the budget.** Overwriting the frozen budget destroys accountability. Keep budget, reforecast, and actual as three separate columns forever.
- **Hard-coding the FY total.** Full-year must be `=ATD + FTG` so it auto-updates when Q2 closes. A typed-over FY cell is the classic broken-model tell.
- **Sandbagging or hero numbers.** Assuming Q1's shortfall fully catches up (hero) or writing off the whole year (sandbag). Recovery must match the actual pipeline.
- **Changing volume *and* margin *and* opex with no owner.** If three drivers move, three names sign off.
- **Forgetting the price offset.** Netting volume and price into one "revenue miss" hides that pricing is actually helping — pros keep P and Q separate.
- **Margin creep from rounding.** Re-derive GP from COGS, don't apply a rounded %.

## On the job & in the interview

The rolling forecast is the FP&A heartbeat — most Indian mid-market firms run a **quarterly reforecast** (larger ones monthly), always as ATD + FTG. The phrase to own: *"we replace a quarter of forecast with a quarter of actuals and re-drive the go-forward."*

**Q: "Budget says 12, you're forecasting 11.7 — did you just cut the number?"**
"No — I re-drove it. Goods volume is 85,300 units vs 90,000 because two OEM orders slipped and don't fully recover; that's partly offset by ASP holding at Rs 1,020 and services on plan, landing revenue at Rs 11.70 cr. Every rupee of the Rs 30 lakh delta traces to a driver with an owner — it's a bottoms-up reforecast, not a top-down haircut."

**Q: "Revenue is only down 2.5% but PBT is down 15% — why?"**
"Operating leverage in reverse. The Rs 21 lakh gross-profit loss combines the volume miss with a 100bps input-cost margin hit, and two hires landed a quarter early adding Rs 2 lakh of opex. Fixed opex doesn't flex down with revenue, so a small top-line slip amplifies at PBT. It also tells us the sensitivity: margin and headcount are the levers to defend, not the top line."

**Q: "When do you reforecast vs stick with budget?"**
"Budget is the annual commitment and stays frozen for measurement. I reforecast whenever the actuals materially diverge from plan — here a −5% Q1 — so decision-makers steer off a current view. Two different jobs: budget for accountability, reforecast for steering."
