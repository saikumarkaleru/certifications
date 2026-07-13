# Power BI I: Data Model & DAX

## What it is & where it's used

Power BI is Microsoft's business-intelligence tool: you load data, build a **data model** (tables + relationships), write **DAX** (Data Analysis Expressions) formulas, and publish interactive dashboards. Think of it as "Excel PivotTables on steroids" — it handles 10 million rows without choking, refreshes on a schedule, and lets a CFO slice revenue by region/month/product with one click.

Two separate skills live inside Power BI, and this chapter covers the engine, not the paint:
- **Power Query (M)** — the ETL layer: import, clean, reshape.
- **The data model + DAX** — relationships, star schema, and the calculation language.

Where finance roles use it:

| Role | What they build in Power BI |
|---|---|
| FP&A analyst | Monthly MIS, budget-vs-actuals, rolling forecasts |
| Accounts / controller | AR/AP ageing, cash-flow dashboards, GST reconciliation summaries |
| Audit / internal audit | Exception reports, journal-entry testing, sampling views |
| Business finance | Revenue by SKU/region, margin walk, cohort analysis |
| Tax | GSTR-2B vs purchase-register match, ITC tracking |

In India, "Power BI" now appears in ~30-40% of FP&A and MIS job posts, often paired with Excel and SQL. It is the single highest-leverage BI skill you can add to a finance CV.

## The gap: why companies want this (and college didn't teach it)

MBA Finance and CA teach you *what* the numbers mean — variance analysis, ratios, cost sheets. They do **not** teach you to model data. The specific gaps:

1. **You think in one big flat table.** College spreadsheets have everything in one sheet. Real reporting needs a **star schema** — separate fact and dimension tables joined by keys. Nobody explains why.
2. **You confuse a column with a measure.** In Excel every cell is a value. In Power BI a *measure* is a formula that recalculates for whatever the user clicked. Freshers write everything as calculated columns and blow up the file size.
3. **You've never seen "filter context."** DAX's entire personality is that `CALCULATE` manipulates filters. This concept has no Excel equivalent, so it's the #1 thing people fail.
4. **Time-intelligence.** "Show me YTD, same period last year, MoM %" — done in Excel with fragile SUMIFS and helper columns. Power BI does it in one measure *if you have a proper date table*.

Employers pay for this because a good model turns a 3-day monthly-MIS grind into a 5-minute refresh. That is a direct cost saving they can measure.

## What "proficient" looks like

A job-ready person can, unaided:

- Load 3-4 tables, set correct **data types**, and build a **star schema** with one-to-many relationships.
- Explain when to use a **calculated column** vs a **measure** (and default to measures).
- Create a **dedicated Date table** and mark it as such.
- Write measures using `SUM`, `SUMX`, `CALCULATE`, `DIVIDE`, `FILTER`, and the time-intelligence functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`).
- Understand and control **filter context** — knows why a measure returns blank or the grand total in the wrong cell.
- Build a budget-vs-actual with variance and variance %.

That's roughly the bar for an FP&A analyst screen. You do **not** need row-level security or DAX Studio optimization for a first job.

## Hands-on: how to actually do it

### 1. Load data

`Home → Get Data → Excel/CSV/SQL Server`. Pick your files, click **Transform Data** (opens Power Query), verify each column's data type (the icon left of the header), then **Close & Apply**.

Golden rule: **clean in Power Query, calculate in DAX.** Don't do transformations with DAX columns.

### 2. Build the star schema

A star schema = one **fact** table (transactions, many rows) surrounded by **dimension** tables (master data, few rows).

```
        Dim_Date
            |
Dim_Product — Fact_Sales — Dim_Customer
            |
        Dim_Region
```

- **Fact_Sales**: Date, ProductKey, CustomerKey, RegionKey, Qty, Amount.
- **Dimensions**: one row per product/customer/region/date.

In **Model view**, drag `Fact_Sales[ProductKey]` onto `Dim_Product[ProductKey]`. Power BI creates a **one-to-many** relationship (one product → many sales rows). Filters flow **from the "one" side to the "many" side** — this single fact explains 90% of DAX behaviour.

### 3. Measures vs columns

| | Calculated column | Measure |
|---|---|---|
| Computed | Row-by-row, at refresh | On the fly, per filter context |
| Stored | In the model (eats RAM) | Not stored |
| Use for | A category/flag you slice BY | A number you aggregate/show |
| Example | `Margin Band = IF([Margin]>0.3,"High","Low")` | `Total Sales = SUM(Fact_Sales[Amount])` |

**Default to measures.** Only make a column when you need to *filter or group by* the result.

### 4. Core DAX

```dax
Total Sales = SUM ( Fact_Sales[Amount] )

Total Qty = SUM ( Fact_Sales[Qty] )

-- SUMX iterates row by row, then sums. Use when the math is per-row.
Revenue = SUMX ( Fact_Sales, Fact_Sales[Qty] * Fact_Sales[Price] )

-- DIVIDE handles divide-by-zero (returns blank, not error)
Avg Price = DIVIDE ( [Revenue], [Total Qty] )
```

**CALCULATE** — the most important function. It evaluates an expression under *modified* filters:

```dax
-- Sales only for the South region, ignoring any region the user clicked
South Sales = CALCULATE ( [Total Sales], Dim_Region[Region] = "South" )

-- Sales ignoring ALL filters (useful for % of total)
All Sales = CALCULATE ( [Total Sales], ALL ( Fact_Sales ) )

Pct of Total = DIVIDE ( [Total Sales], [All Sales] )
```

**Time-intelligence** (needs a marked Date table):

```dax
-- Create a proper date table first
Dim_Date =
CALENDAR ( DATE ( 2023, 4, 1 ), DATE ( 2026, 3, 31 ) )
```

Add columns to it: `Year = YEAR([Date])`, `MonthNo = MONTH([Date])`, `MonthName = FORMAT([Date],"MMM")`, `FY = "FY" & YEAR([Date]) + IF(MONTH([Date])>=4,1,0)` (Indian April-March fiscal year). Then `Table tools → Mark as date table`.

```dax
Sales YTD = TOTALYTD ( [Total Sales], Dim_Date[Date], "31/03" )   -- Indian FY end

Sales LY = CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( Dim_Date[Date] ) )

Sales PM = CALCULATE ( [Total Sales], DATEADD ( Dim_Date[Date], -1, MONTH ) )

MoM % = DIVIDE ( [Total Sales] - [Sales PM], [Sales PM] )

YoY % = DIVIDE ( [Total Sales] - [Sales LY], [Sales LY] )
```

## Worked example / mini-project: Budget vs Actual MIS

**Data (reproduce in two CSVs):**

`Fact_Actuals` (sales transactions):

| Date | Region | Product | Amount |
|---|---|---|---|
| 2025-04-05 | South | Widget A | 120000 |
| 2025-04-18 | North | Widget B | 85000 |
| 2025-05-02 | South | Widget A | 140000 |
| 2025-05-20 | West | Widget C | 60000 |

`Fact_Budget`:

| Month | Region | BudgetAmount |
|---|---|---|
| 2025-04 | South | 130000 |
| 2025-04 | North | 90000 |
| 2025-05 | South | 150000 |
| 2025-05 | West | 55000 |

**Steps:**
1. Load both. Build `Dim_Date` and `Dim_Region`; relate both facts to them.
2. Write measures:

```dax
Actual = SUM ( Fact_Actuals[Amount] )
Budget = SUM ( Fact_Budget[BudgetAmount] )
Variance = [Actual] - [Budget]
Variance % = DIVIDE ( [Variance], [Budget] )
Actual YTD = TOTALYTD ( [Actual], Dim_Date[Date], "31/03" )
```

3. Drop a matrix: Rows = `Region`, Values = `Actual`, `Budget`, `Variance`, `Variance %`. Add a `MonthName` slicer.

**Expected April result:** South Actual ₹1,20,000 vs Budget ₹1,30,000 → Variance −₹10,000 (−7.7%). North −₹5,000 (−5.6%). This is a live, filterable MIS you built in under 30 minutes — exactly the deliverable an FP&A team asks a fresher to produce.

Conditional formatting: on `Variance %`, `Format → Cell elements → Background color → rules`: red below 0, green above. Now management sees misses at a glance.

## How it's tested

**Interview questions:**
- "Difference between a calculated column and a measure? When each?"
- "What is a star schema and why not just one flat table?"
- "Explain filter context. What does `CALCULATE` do?"
- "Why do you need a separate date table instead of the date column in your fact?"
- "`SUM` vs `SUMX` — give an example where only `SUMX` works." (Answer: `Qty * Price` per row, since prices differ by row.)
- "Your measure shows blank / shows the grand total in every row — why?"

**Practical test (very common):** They hand you 2-3 raw CSVs/Excel files and a brief — *"Build a dashboard showing sales by region and month, with YoY growth and a budget-vs-actual variance"* — timed 45-90 minutes. Graders check: correct relationships (no many-to-many hacks), measures not columns, a proper date table, working time-intelligence, and clean visuals. Some firms give a broken .pbix and ask you to *fix the model*.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Everything in one flat table | Split into fact + dimensions (star schema) |
| Calculated columns for numbers you aggregate | Use measures — they respond to filters and don't bloat the file |
| Using the fact table's date column for time-intelligence | Always a **dedicated, marked Date table** with continuous dates |
| Gaps in the date table | Use `CALENDAR`/`CALENDARAUTO` so every day exists |
| `/` operator causing errors | Use `DIVIDE()` — safe divide-by-zero |
| Bi-directional / many-to-many relationships everywhere | Keep single-direction one-to-many; filter flows one → many |
| Hardcoding "last year" with a slicer | Use `SAMEPERIODLASTYEAR` / `DATEADD` |
| Wrong FY (Jan-Dec) for Indian data | Set year-end to `"31/03"` and build FY logic (Apr-Mar) |
| Blank measure results | Usually broken relationship or wrong filter direction — check Model view |

## Learn-it roadmap & resources

**Time to proficiency:** 4-6 weeks part-time to clear a fresher FP&A screen; 3 months to be genuinely fast.

| Week | Focus |
|---|---|
| 1 | Power BI Desktop install (free), Get Data, Power Query cleaning |
| 2 | Model view, relationships, star schema |
| 3 | Measures vs columns, `SUM/SUMX/CALCULATE/DIVIDE` |
| 4 | Date table + time-intelligence (YTD, YoY, MoM) |
| 5-6 | Build 2 end-to-end dashboards; learn `FILTER`, `ALL`, `VAR` |

**Resources:**
- **Microsoft Learn — "Power BI Data Analyst" path** (free, official).
- **SQLBI (Marco Russo/Alberto Ferrari)** — free YouTube + *dax.guide* function reference; the gold standard for DAX.
- **Enterprise DNA** and **Kevin Stratvert** on YouTube (free, beginner-friendly).
- **Certification:** **PL-300 (Microsoft Power BI Data Analyst)** — ~₹4,800 exam fee in India, well-recognised, worth it for finance CVs.

Power BI Desktop is **free**. Publishing to the cloud service needs Pro (~$10/month); for learning and interviews, Desktop alone is enough.

## Quick-reference

```dax
-- Aggregation
SUM ( Table[Col] )
SUMX ( Table, Table[A] * Table[B] )      -- per-row then sum
DIVIDE ( num, den [, 0] )                -- safe divide

-- Filter manipulation
CALCULATE ( [Measure], filter1, filter2 )
CALCULATE ( [Measure], ALL ( Table ) )    -- remove filters
CALCULATE ( [Measure], FILTER ( Table, Table[x] > 100 ) )

-- Time-intelligence (needs marked Date table)
TOTALYTD ( [Measure], Dim_Date[Date], "31/03" )   -- Indian FY
CALCULATE ( [Measure], SAMEPERIODLASTYEAR ( Dim_Date[Date] ) )
CALCULATE ( [Measure], DATEADD ( Dim_Date[Date], -1, MONTH ) )
```

| Concept | One-liner |
|---|---|
| Star schema | 1 fact (transactions) + many dimensions (masters) |
| Relationship | One-to-many; filter flows one → many |
| Measure | Formula, recalculates per filter; use for numbers you show |
| Calculated column | Row-by-row, stored; use only to slice/group BY |
| Filter context | The set of filters active when a measure evaluates |
| CALCULATE | Changes the filter context, then evaluates |
| Date table | Dedicated, continuous, "Mark as date table" — required for time-intel |
| Indian FY | April 1 – March 31; set YTD year-end to `"31/03"` |
```

**Muscle memory:** clean in Power Query → model as a star → default to measures → one Date table → `CALCULATE` for everything conditional.
