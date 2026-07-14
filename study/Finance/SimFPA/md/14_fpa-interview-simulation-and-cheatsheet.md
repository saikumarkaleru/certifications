# The FP&A Interview Simulation + Cheat-Sheet

## The ask

It's **Monday, 27 July 2026**. A friend forwards a role: *FP&A Analyst, mid-market manufacturer, Hyderabad.* The JD reads almost exactly like your Nirvana job — annual budget, monthly variance, forecasting, a bit of capex appraisal, Excel + Power BI. You have a first-round with the FP&A Manager on Thursday and the CFO round after.

This chapter *is* your prep: a realistic mock, using the same Nirvana numbers you've been living in, followed by a one-page cheat-sheet to skim in the cab.

## What you're given

The Nirvana anchors, which you'll quote from memory in the room: **Revenue Rs 12.00 cr** (Goods 9.00 = 90,000 units x Rs 1,000; Services 3.00 = 250 AMCs x Rs 1,20,000). **COGS 8.40 cr, GP 3.60 cr (30%)**. Opex: Employee 1.08 + Other 0.78 + Depreciation 0.144. **EBIT 1.596 cr; Finance cost 0.09; PBT 1.506; PAT ~1.11 cr** (25%+cess). Q1: budget 2.85 cr, actual 2.70 cr (-15 lakh / -5%), GM 28.5% vs 30%. Capex case: Rs 40 lakh, saves Rs 12 lakh/yr x 6, salvage Rs 4 lakh, 12% discount. Working capital: DSO 60, DPO 45, DIO 40.

## Build it — the mock interview

**Q1 — "Walk me through the variance between your Q1 budget and actual."**
"Q1 revenue was Rs 2.70 cr against a Rs 2.85 cr budget — Rs 15 lakh unfavourable, -5%. It's a goods story: volume came in at 21,000 units versus 22,500 budgeted, a ~Rs 15 lakh volume miss at standard price, partly offset by price — ASP realised Rs 1,020 vs Rs 1,000 budget, ~+Rs 4 lakh. Services were on plan. Below the line, gross margin was 28.5% vs 30% on adverse mix and input cost, and opex ran Rs 5 lakh over on two early hires. So: volume-led revenue miss, cushioned by price, with a margin squeeze on top."

**Q2 — "Split that into a price/volume bridge. Formulas?"**
"Volume variance = (actual units - budget units) x budget price = (21,000 - 22,500) x Rs 1,000 = -Rs 15 lakh. Price variance = (actual price - budget price) x actual units = (1,020 - 1,000) x 21,000 = +Rs 4.2 lakh. Net goods variance ≈ -Rs 10.8 lakh; the rest of the -15 is mix/services timing. I always cost the volume variance at *budget* price and the price variance at *actual* volume, so they don't double-count."

**Q3 — "Budget vs forecast — what's the difference?"**
"The budget is the fixed annual target set once, pre-year — my scorecard. The forecast is the latest expected outturn, re-cut each quarter using actuals to date. After a -5% Q1, budget still says Rs 12 cr, but my forecast might say Rs 11.7 cr if the volume softness persists. Budget stays frozen so variances stay honest; the forecast is what management steers by."

**Q4 — "Walk me through the three statements and how they link."**
"P&L ends in net income. That net income flows to the balance sheet via retained earnings, and it's the starting line of the cash flow statement. Cash flow adjusts net income for non-cash items — add back the Rs 14.4 lakh depreciation — and for working-capital moves — a rise in debtors is a cash outflow. The closing cash from the cash flow becomes the cash line on the balance sheet. Depreciation reduces PP&E on the balance sheet; capex increases it. Everything ties: the balance sheet only balances if all three are wired correctly."

**Q5 — "If depreciation goes up Rs 10 lakh, what happens across the three statements?"**
"P&L: EBIT and PBT drop Rs 10 lakh; at ~25% tax, PAT falls Rs 7.5 lakh. Cash flow: start from the lower PAT but add back the full Rs 10 lakh depreciation, so operating cash *rises* Rs 2.5 lakh — the tax shield. Balance sheet: PP&E down Rs 10 lakh, retained earnings down Rs 7.5 lakh, cash up Rs 2.5 lakh — and it still balances."

**Q6 — "Walk me through a DCF."**
"Project free cash flows for a forecast horizon, discount each to today at WACC, add a terminal value for the years beyond, discount that back too, and sum for enterprise value. FCF = EBIT x (1-tax) + depreciation - capex - increase in working capital. Terminal value is usually Gordon growth — final-year FCF x (1+g) / (WACC-g) — or an exit multiple. Subtract net debt to get equity value. For Nirvana at ~12% WACC, the sensitivity is all in WACC and the terminal growth assumption."

**Q7 — "Appraise our warehouse-automation capex: Rs 40 lakh, saves Rs 12 lakh/yr for 6 years, Rs 4 lakh salvage, 12%."**
"Cash flows: -40 now, +12 in years 1-5, +16 in year 6 (12 saving + 4 salvage). At 12%, the annuity factor for 6 years is 4.111, so 12 x 4.111 = Rs 49.3 lakh, plus salvage 4 x 0.507 = Rs 2.0 lakh, gross Rs 51.3 lakh, minus 40 = **NPV ≈ +Rs 11.3 lakh.** Positive, so accept. IRR is roughly 20% — comfortably above the 12% hurdle. Simple payback is 40/12 ≈ 3.3 years."

**Q8 — "NPV vs IRR — which do you trust and why?"**
"NPV, when they conflict. IRR is intuitive as a percentage and fine for independent projects, but it assumes reinvestment at the IRR itself, can give multiple answers with unconventional cash flows, and is blind to scale — a 25% IRR on Rs 2 lakh loses to a 15% IRR on Rs 2 cr. NPV measures rupees of value added at the true cost of capital, so for mutually exclusive choices I rank on NPV."

**Q9 — "Our cash conversion cycle?"**
"CCC = DIO + DSO - DPO = 40 + 60 - 45 = **55 days.** We fund 55 days of operations. The quickest lever is DSO — from the last exercise, our two biggest accounts pay at 70-78 days against a 60 target; tightening them pulls cash in without touching margin."

**Q10 — "Live Excel test: monthly revenue by segment from a transaction dump — formula?"**
"`=SUMIFS(Amount, Segment, $F2, MonthCol, G$1)` with the segment down the rows and months across, mixed references locked so it fills both ways. For pulling a price or a customer attribute I'd use `XLOOKUP(id, id_range, return_range, "not found")` — exact match, no column-count fragility like VLOOKUP. NPV of the capex line: `=NPV(12%, year1:year6) + initial_outlay` where the outlay is a negative in the cell before the range."

**Q11 — "How would you build next year's budget?"**
"Driver-based, bottom-up. Revenue isn't a percentage bump — it's units x ASP per segment: 90,000 units x Rs 1,000 for goods, 250 AMCs x Rs 1,20,000 for services. COGS off segment gross-margin assumptions (25% goods, 45% services). Opex built from headcount (15 to 18 by Q4) and a cost schedule. Then phase to months, layer the balance sheet and cash flow, and check the outputs — 30% GM, ~Rs 1.6 cr EBIT — are sane before locking."

**Q12 — "Guesstimate: AMC market for industrial electrical AMCs in Hyderabad?"**
"Top-down. Say ~5,000 mid/large industrial and commercial sites in greater Hyderabad with meaningful electrical infrastructure; assume 60% outsource AMC = 3,000 contracts; average contract ~Rs 1.2 lakh (our own ASP) = ~Rs 36 cr addressable. We do 250 contracts / Rs 3 cr, so ~8% share — plausible for a regional player, and it says there's room to grow before the market caps us."

**Q13 — "You find a formula error in the pack ten minutes before the board. What do you do?"**
"Quantify it first — is it material to a decision? Flag it to the CFO immediately with the corrected number and the impact; never let a wrong number go into the room to save face. Then fix the source, re-tie the totals to the anchors, and note what control failed so it doesn't recur. Integrity over ego — one silent wrong number costs more than one awkward correction."

**Q14 — "Why FP&A and not audit or accounting?"**
"Accounting tells you what happened; FP&A asks what it means and what to do next. I like living in the model — connecting a volume miss to a forecast cut to a cash impact to a decision the CFO can act on. It's forward-looking and business-facing, which is where I want to be."

## The deliverable — one-page FP&A cheat-sheet

**Core formulas**

| Metric | Formula |
|---|---|
| Gross Margin % | Gross Profit / Revenue |
| Volume variance | (Actual units - Budget units) x **Budget** price |
| Price variance | (Actual price - Budget price) x **Actual** units |
| Contribution | Revenue - variable costs |
| EBIT | Revenue - COGS - Opex |
| NPV | Σ CFₜ / (1+r)ᵗ - initial outlay |
| IRR | rate where NPV = 0 |
| Payback | Outlay / annual cash inflow |
| WACC | E/V·Re + D/V·Rd·(1-tax) |
| CCC | DIO + DSO - DPO |
| DSO | Debtors / Revenue x 365 |
| FCF | EBIT(1-tax) + Deprec - Capex - ΔWC |
| Terminal value | FCF(1+g) / (WACC-g) |

**FP&A annual calendar**

| When | Activity |
|---|---|
| Jan-Mar | Annual budget build (driver-based), board approval |
| Monthly (by day 5-7) | Close, actuals load, MIS pack, variance bridge |
| Quarterly | Re-forecast, board deck, reforecast vs budget |
| Ad-hoc | Capex appraisals, pricing, scenario/what-if |
| Year-end | True-up, next-year planning kickoff |

**Must-know tools**

- Excel: `SUMIFS`, `XLOOKUP`/`INDEX-MATCH`, `NPV`, `IRR`, `PMT`, mixed refs `$A1`/`A$1`, data tables for sensitivity, PivotTables.
- DAX: `Actual = SUM(...)`, `Variance = [Actual]-[Budget]`, `DIVIDE()`, `TOTALYTD()`, `CALCULATE()`.
- SQL: `JOIN`, `GROUP BY`, `RANK() OVER(...)`, `CASE WHEN`.

**KPI definitions to state crisply**

- **Budget** = fixed annual target; **Forecast** = latest expected outturn; **Actual** = what happened.
- **Favourable/Unfavourable** — revenue above budget or cost below budget = favourable.
- **Gross margin** vs **EBIT margin** vs **PAT margin** — know all three for Nirvana: 30% / 13.3% / ~9.3%.
- **Accretive/dilutive, run-rate, YoY, YTD, variance bridge, waterfall.**

## How it's reviewed

The interviewer is checking three things: (1) can you *reconcile* — do your numbers tie, do you quote the 30% GM and Rs 1.6 cr EBIT without fumbling; (2) do you connect the dots — variance → forecast → cash → decision, not isolated facts; (3) judgment under pressure — the error-before-the-board answer matters as much as the DCF. Precise numbers spoken with a "so what" beat vague theory every time.

## Common mistakes & red flags

- Costing volume variance at actual price (double-counts with price variance) — use budget price.
- Confusing budget and forecast, or calling a re-forecast a "revised budget."
- Quoting IRR as always superior — misses scale and reinvestment flaws.
- A DCF walk-through that forgets to subtract net debt or hand-waves terminal value.
- Guesstimates with no stated assumptions — the number matters less than the structure.
- Rounding away the anchors — if you can't get back to Rs 12 cr / Rs 3.6 cr / Rs 1.11 cr, you don't know your own case.

## On the job & in the interview

FP&A interviews reward the person who *lives in one model* and can speak it fluently — which is the whole point of running the Nirvana case end to end. Bring one printed page, know your anchors cold, and always answer a number question with the number *and* the "so what." The three questions they almost always ask: a variance walk-through, a three-statement linkage, and a capex/DCF — all three are answered above, in rupees, from your own book.
