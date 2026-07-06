# Q&A — Power BI for Finance

A practice bank for Chapter 35. Work each question before reading the answer. DAX is shown exactly as it would be typed; Excel cross-checks in Section B are reproducible in a blank workbook so you can prove the numbers by hand.

---

## Section A — Concept-Check

**A1. What structural problem does Power BI solve that Excel cannot?**

Recurring, high-volume, multi-source reporting. Excel is a modelling scratchpad where logic and data share the same cell, the worksheet caps at 1,048,576 rows, and refresh is a manual paste-and-pivot ritual with a bus factor of one. Power BI separates the job into layers so that a messy source is shaped once, related into tables, its metrics defined once, and published as an interactive dashboard that refreshes on a schedule.

**A2. Name the four layers of a Power BI solution and what each does.**

(1) Power Query — connect, clean and reshape source data as a repeatable recipe of steps. (2) The Data Model — several tables linked by keys (a star schema) so you relate instead of copy. (3) DAX — a formula language that computes metrics on demand in the current filter context. (4) Report canvas — visuals and slicers the user interacts with. Underneath, publishing to the Service adds scheduled refresh and sharing.

**A3. Define "filter context" and explain why it lets one measure serve every view.**

Filter context is the set of filters currently applied when a measure is evaluated — supplied by slicers, the row/column a value sits in, and any cross-filtering. A measure has no fixed rows; the engine first applies the context (e.g. Month = March, Region = North), then evaluates the arithmetic over exactly those rows. Because the visual supplies the filter and the measure supplies the calculation, one definition of `Total Revenue` is correct in a card, a slicer-filtered month, and every bar of a by-region chart.

**A4. What is the VertiPaq engine and why does it beat a worksheet for big data?**

VertiPaq is Power BI's columnar, in-memory engine. It stores each column separately and compresses hard — a Region column with six distinct values across two million rows stores each value once and points to it — so tens of millions of rows fit in memory and column aggregations like `SUM` are near-instant. Excel stores data row-by-row in a grid, which bloats the file and lags on every recalculation.

**A5. Distinguish a measure from a calculated column, and state the default.**

A calculated column computes a value for every row at refresh time and stores it, costing memory; use it only for a row-level attribute you must slice or group by. A measure computes on demand in the current filter context, costs no storage, and responds to slicing. Default to measures; make a calculated column only when you need to filter or group by the result.

**A6. Why must you always use `DIVIDE` instead of `/` for ratios?**

`DIVIDE(num, den)` returns blank (or a chosen alternate) when the denominator is zero, instead of throwing a divide-by-zero error that blanks the whole visual. Finance ratios routinely hit zero denominators (a month with no revenue, a new segment), so `DIVIDE` is the safe default for every ratio.

**A7. What is a star schema, and which table sits on the "one" side of a relationship?**

A star schema places one large fact table (measurable events — one row per transaction, keys plus numeric amounts) in the centre, surrounded by small dimension tables (descriptive attributes to slice by: Calendar, Chart of Accounts, Entity, Scenario). Relationships are one-to-many, with the dimension on the "one" side and the fact on the "many" side; filters flow from the one side to the many side.

**A8. Why must a finance model have a dedicated, marked Calendar table?**

Time-intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`) require a continuous, gap-free date dimension marked as the date table. Dates buried inside the fact table have gaps (no rows on quiet days), so time intelligence silently returns blank or wrong numbers. A dedicated Calendar guarantees every date exists exactly once.

**A9. What does "unpivot" do and why is it the most valuable finance move in Power Query?**

Budget files arrive wide — one row per account with twelve month columns Jan…Dec. DAX and a Date table need the data tall — one row per account-per-month. Unpivot selects the month columns and turns them into two columns: an Attribute (the month) and a Value (the number). This converts a spreadsheet into a database that can be related to a Calendar and sliced by date.

**A10. When does Excel still beat Power BI?**

Ad-hoc one-off analysis; inventing a brand-new model; complex what-if with iterative or circular logic (interest-on-debt circularity); and small data a grid handles fine. Excel invents the calculation; Power BI operationalizes the recurring report. Use Excel to model, Power BI to monitor.

---

## Section B — Build / Computational Problems

Each answer is reproducible in Excel so you can prove the DAX result by hand. Amounts are in currency units.

**B1. Single-month budget variance.**

Given (March 2025, filter context Month = 3, Year = 2025): Actual revenue = 1,180,000; Budget revenue = 1,100,000.

Measures:
```
Revenue Actual      = CALCULATE ( [Total Revenue], Scenario[Scenario] = "Actual" )
Revenue Budget      = CALCULATE ( [Total Revenue], Scenario[Scenario] = "Budget" )
Budget Variance     = [Revenue Actual] - [Revenue Budget]
Budget Variance Pct = DIVIDE ( [Budget Variance], [Revenue Budget] )
```

Excel check: put Actual in `B2`, Budget in `B3`. `=B2-B3` → **80,000**. `=(B2-B3)/B3` → **0.072727… = +7.27%**.

Reconcile: 1,100,000 × 1.0727 = 1,179,970 ≈ 1,180,000 ✓. Favourable variance of +7.3%. Drag the same three measures into a matrix with Month on rows and the identical formulas produce all twelve months' variances — no re-typing.

**B2. Year-over-year growth with time intelligence.**

Given: Total Revenue 2024 = 12,000,000; 2025 = 13,800,000. Slicer on 2025.

Measures:
```
Total Revenue   = SUM ( FactGL[Amount] )
Revenue PY      = CALCULATE ( [Total Revenue], SAMEPERIODLASTYEAR ( Calendar[Date] ) )
Revenue YoY     = [Total Revenue] - [Revenue PY]
Revenue YoY Pct = DIVIDE ( [Revenue YoY], [Revenue PY] )
```

`SAMEPERIODLASTYEAR` shifts the date filter back one year, so Revenue PY = 2024 = 12,000,000.

Excel check: `=13800000-12000000` → **1,800,000**. `=1800000/12000000` → **0.15 = +15.0%**.

Reconcile: 12,000,000 × 1.15 = 13,800,000 ✓. In a KPI card this shows +15% with an up arrow; split by month in a line chart, each point compares to the same month last year automatically.

**B3. Quarter gross margin — the re-aggregation trap.**

Q4 2025 data:

| Month | Revenue | COGS |
|---|---|---|
| Oct | 1,200,000 | 720,000 |
| Nov | 1,300,000 | 754,000 |
| Dec | 1,500,000 | 840,000 |

Measures:
```
Total COGS       = SUM ( FactGL[COGS] )
Gross Profit     = [Total Revenue] - [Total COGS]
Gross Margin Pct = DIVIDE ( [Gross Profit], [Total Revenue] )
```

Per month: Oct GP = 480,000 (40.0%); Nov GP = 546,000 (42.0%); Dec GP = 660,000 (44.0%).

Quarter totals: Revenue = 4,000,000; COGS = 2,314,000; GP = 1,686,000.

Excel check of the quarter margin: `=1686000/4000000` → **0.42150 = 42.15%**. The naive average `=(0.40+0.42+0.44)/3` → **0.42000 = 42.0%** — wrong.

Reconcile the difference: the correct margin weights by revenue. December (biggest revenue, highest margin) pulls the true figure above the simple mean, giving 42.15% not 42.00%. Because `Gross Margin Pct` is a measure, it re-computes GP ÷ Revenue at every subtotal level, so the matrix total is automatically 42.15%. A stored calculated column of monthly percentages, then averaged, would give the wrong 42.0%. This is the single most important reason finance uses measures.

**B4. Percent-of-total that stays fixed while the visual splits by segment.**

Given three regions: North 4,000,000; South 3,100,000; East 1,900,000. Total = 9,000,000.

Measure:
```
Pct of Total Revenue =
DIVIDE ( [Total Revenue], CALCULATE ( [Total Revenue], ALL ( Entity ) ) )
```

`ALL(Entity)` removes the region filter for the denominator only, so each row divides its own revenue by the fixed grand total.

Excel check: North `=4000000/9000000` → **44.44%**; South `=3100000/9000000` → **34.44%**; East `=1900000/9000000` → **21.11%**.

Reconcile: 44.44 + 34.44 + 21.11 = 99.99 ≈ 100% ✓ (rounding). Without `ALL`, every row's denominator would also be filtered to that region and each percentage would compute to 100%.

**B5. Rolling 12-month revenue.**

The measure sums revenue over the trailing twelve months ending on the latest date in context:
```
Rolling 12M Revenue =
CALCULATE (
    [Total Revenue],
    DATESINPERIOD ( Calendar[Date], MAX ( Calendar[Date] ), -12, MONTH )
)
```

Given monthly revenue of 1,000,000 for each of Jan–Dec 2025 (12 months), with the visual's latest date at 31 Dec 2025:

Excel check: `=1000000*12` → **12,000,000**.

Reconcile: `DATESINPERIOD` builds a window of −12 months back from 31 Dec 2025 = Jan–Dec 2025, so the sum is the full year = 12,000,000 ✓. Move the visual context to 30 Nov 2025 and the window becomes Dec 2024–Nov 2025 — the measure re-slides with no formula change.

**B6. Average ticket (safe ratio under an empty filter).**

Given a segment with Total Revenue = 500,000 and Txn Count = 2,000; and a brand-new segment with Revenue = 0 and Count = 0.

```
Txn Count  = COUNTROWS ( FactGL )
Avg Ticket = DIVIDE ( [Total Revenue], [Txn Count] )
```

Excel check segment 1: `=500000/2000` → **250**. Segment 2 with `/`: `=0/0` → `#DIV/0!`. With `DIVIDE`: returns **(blank)**.

Reconcile: `DIVIDE` keeps the new segment's row clean instead of erroring and blanking the whole visual — exactly the edge case a raw `/` crashes on.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through the difference between Power Query and DAX, and when each runs."**

Power Query is the extract-and-transform layer: it connects to a source and records reshaping steps — remove columns, set types, unpivot, merge, append — in the M language. It runs once per refresh and does the heavy cleaning. DAX is the calculation layer: measures and calculated columns written in a formula language. Measures run on every user interaction, doing only aggregation in the current filter context. The discipline is: clean in Power Query (once, cheap), aggregate in DAX (on demand). Cleaning data in DAX bloats the model and slows every click; aggregating in Power Query freezes the numbers and loses interactivity.

**C2. "A stakeholder says the dashboard's quarterly margin looks too low versus averaging the monthly margins. How do you explain it?"**

The quarterly margin is not the average of monthly margins — it is total gross profit divided by total revenue for the quarter. Averaging the three monthly percentages weights each month equally, but the months have different revenue. A high-revenue, high-margin month should count more. The measure computes `DIVIDE(SUM(GP), SUM(Revenue))` fresh at the quarter level, so it correctly revenue-weights. The averaged figure is the error; the dashboard is right. This is why margins are measures, never stored-and-averaged columns.

**C3. "Why do you insist on a separate Calendar table when the fact table already has dates?"**

Two reasons. First, time-intelligence functions need a continuous, gap-free date range; the fact table has no rows on days with no transactions, so YTD and prior-year calculations break on the gaps. Second, a dedicated Calendar gives clean, reusable attributes — Year, Quarter, Month, YearMonth — with the Month text sorted by a MonthNo column so it orders Jan…Dec rather than alphabetically. I mark it as the date table so DAX knows it is authoritative, and relate Calendar[Date] one-to-many to the fact.

**C4. "When would you choose DirectQuery over Import, and why is Import the finance default?"**

Import copies data into the VertiPaq engine — fast queries, full DAX support, but data is only as fresh as the last refresh. DirectQuery leaves data in the source and queries it live — always current and no size limit, but slower and with DAX restrictions. Finance dashboards almost always use Import: monthly close data does not change intraday, the datasets fit comfortably in memory, and speed and full DAX matter more than real-time freshness. DirectQuery is for data too large to copy or genuinely needing live updates.

**C5. "How does Power BI fit alongside our Excel three-statement model — does it replace it?"**

No. Power BI does not build the driver-based projection; Excel still does the forecast with its iterative and circular logic. Power BI is the monitor: it loads the ERP actuals and the Excel budget, relates them through a Scenario dimension, and the actual-versus-budget variance dashboard writes itself with reusable DAX measures. Excel is the model; Power BI is the reporting and monitoring layer on top. They interoperate — Power BI can import an Excel data model, and Excel can pivot live against a published Power BI dataset.

**C6. "What is `CALCULATE` and why is it the most important DAX function?"**

`CALCULATE` modifies the filter context before evaluating an expression. Its signature is `CALCULATE(<expression>, <filter1>, <filter2>, …)` and each filter argument adds to or overrides the incoming context. It is how you build `Revenue Actual` (filter Scenario to Actual), `% of total` (use `ALL` to strip a filter), and every time-intelligence pattern (the time functions return a table of dates that `CALCULATE` applies). Master `CALCULATE` and filter context together and you have grasped roughly 80% of DAX.

---

## Section D — Common-Error Spotting

For each item, identify the mistake and give the fix.

**D1.** An analyst creates a calculated column `Margin = FactGL[GP] / FactGL[Revenue]`, drops it in a matrix, and the quarter subtotal shows 42.0% when it should be 42.15%.

Error: a per-row margin averaged at the subtotal. Fix: delete the column and use a measure `Gross Margin Pct = DIVIDE(SUM(FactGL[GP]), SUM(FactGL[Revenue]))`, which re-aggregates numerator and denominator at every level. Also `/` should be `DIVIDE`.

**D2.** A budget file is loaded with columns Account, Jan, Feb, … Dec and related to the Calendar table, but no month slicing works.

Error: wide data — twelve month columns cannot relate to a Date table. Fix: in Power Query select the month columns and Unpivot into Month and Amount, convert the month into a real date, then relate to Calendar.

**D3.** `Revenue YoY = [Total Revenue] - CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(FactGL[Date]))` returns blank for every period.

Error: time intelligence pointed at the fact table's date, which has gaps and is not marked. Fix: build a dedicated Calendar, mark it as the date table, relate it to the fact, and reference `Calendar[Date]` in the time function.

**D4.** Month names on the axis read Apr, Aug, Dec, Feb… instead of Jan, Feb, Mar.

Error: the Month text column sorts alphabetically. Fix: add a MonthNo column (1–12) and set the Month column to Sort by Column → MonthNo.

**D5.** An analyst trims whitespace, fixes text case, and splits an account code inside DAX calculated columns; the report has become sluggish on every click.

Error: cleaning done in DAX (runs on interaction and bloats the model) instead of Power Query (runs once per refresh). Fix: move all trimming, type-fixing and splitting into Power Query steps.

**D6.** A ratio measure `= [Revenue] / [Count]` blanks the entire visual whenever a segment has zero transactions.

Error: raw `/` throws `#DIV/0!` on a zero denominator, which cascades. Fix: `DIVIDE([Revenue], [Count])`, which returns a clean blank.

**D7.** The model relies on Power BI's auto-detected relationships; a regional total is silently wrong.

Error: auto-detected relationships guess and often guess wrong, sometimes creating bidirectional or wrong-cardinality links. Fix: delete auto relationships, build them deliberately in Model view as one-to-many with the dimension on the one side, single-direction unless a specific need justifies bidirectional.

**D8.** Dates imported as text sort alphabetically and every time-intelligence measure fails.

Error: wrong data type set (or not set) in Power Query. Fix: set the Date column type to Date explicitly and early in the Applied Steps, before any downstream step depends on it.

---

## Self-Check Summary

If you can (1) explain why one measure is correct under every slice (filter context), (2) prove a quarterly margin re-aggregates to GP ÷ Revenue rather than the average of monthly percentages, (3) tell a measure from a calculated column and default to measures, and (4) reach for a marked Calendar, a star schema, `DIVIDE`, and unpivoted data by reflex — you have understood the chapter. The rest of DAX is composition on top of those foundations.
