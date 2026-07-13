# PivotTables & Dashboards

## What it is & where it's used

A **PivotTable** is Excel's engine for turning a flat list of transactions into a summary you can slice any way you want — total sales by region, expense by cost centre, GST payable by month — without writing a single formula. A **dashboard** is a one-page visual layer built on top of those pivots: a few charts, some KPI tiles, slicers to filter, all refreshing from one data source.

This is the single most-used Excel skill in day-to-day finance work. Where it shows up:

- **FP&A / MIS analysts** — the monthly MIS pack is 90% pivots and dashboards.
- **Accounts / audit** — reconciling a Tally trial-balance dump, ageing debtors, ledger scrutiny.
- **Tax** — reconciling GSTR-2B against your purchase register (both are flat CSV exports → pivot both → compare).
- **Treasury / management reporting** — cash position, DSO/DPO trends.

If a job description says "prepare monthly MIS," "reporting," or "management dashboards," it means PivotTables. Full stop.

## The gap: why companies want this (and college didn't teach it)

MBA and CA syllabi teach you what a *variance* is and how to read a *P&L*. They almost never make you sit with 40,000 rows of raw ledger data and produce a manager-ready one-pager by 10 a.m. That translation step — **raw data → decision-ready summary** — is the actual job, and it's the gap.

Specifically, college leaves you weak on:

| College teaches | The job needs |
|---|---|
| Interpreting a finished P&L | *Building* it from a Tally/ERP dump |
| SUM / VLOOKUP on tidy data | Pivoting 50k messy rows in 30 seconds |
| One static answer | A slicer-driven view a manager self-serves |
| "The number is ₹12L" | Why it moved, shown visually, on one page |

Employers pay for speed and self-service. A manager who can click a slicer instead of emailing you "can you split this by branch?" saves the whole team hours. That's the value.

## What "proficient" looks like

The concrete bar a job-ready person clears unaided:

- Given a raw export, build a PivotTable in under a minute — drag fields, change **Sum → Average/Count**, add a second dimension to Columns.
- Group dates into **Months/Quarters/Years** (right-click a date field → Group).
- Add **% of Column Total**, **Running Total**, and **Difference From** (prior month) as *Show Values As*.
- Insert **Slicers** and a **Timeline**, and connect one slicer to *multiple* pivots (Report Connections).
- Build a **one-page dashboard**: 3–4 PivotCharts + KPI cells, all fed by pivots, all refreshing on one click.
- Use **GETPIVOTDATA** to pull a specific pivot cell into a KPI tile that won't break when the pivot resizes.
- Apply **conditional formatting** (data bars, colour scales, icon sets, top/bottom rules) and **sparklines** for inline trends.
- Refresh everything with **Ctrl+Alt+F5** (Refresh All) and know that pasting new data into the source table auto-updates the pivot.

## Hands-on: how to actually do it

### 1. Prep the data (always do this first)

Turn your raw range into a **Table** so the pivot auto-expands when data grows:

```
Select any cell in the data → Ctrl+T → tick "My table has headers" → OK
Rename it: Table Design tab → Table Name: tblSales
```

Now your pivot source is `tblSales`, not `A1:H40000`. New rows flow in automatically.

### 2. Build the PivotTable

```
Insert → PivotTable → Table/Range: tblSales → New Worksheet → OK
```

Drag fields into the four zones:
- **Rows** = Region, then Product (nested)
- **Columns** = Month
- **Values** = Sales Amount (defaults to Sum)
- **Filters** = FY

Change the calculation: right-click any value → **Summarize Values By** → Average / Count / Max.

### 3. Show Values As (the underused power)

Right-click a value → **Show Values As**:

| Option | Gives you |
|---|---|
| % of Grand Total | Each cell's share of the whole |
| % of Column Total | Product mix within each month |
| Running Total In | Cumulative YTD sales |
| Difference From (prev) | Month-on-month change (₹) |
| % Difference From | MoM growth % |

### 4. Group dates

```
Right-click any date in the pivot → Group → select Months + Years → OK
```

### 5. Slicers, Timeline, and connecting them

```
PivotTable Analyze → Insert Slicer → tick Region, Product
PivotTable Analyze → Insert Timeline → tick Order Date
```

To drive **multiple pivots** from one slicer:

```
Right-click the slicer → Report Connections → tick every PivotTable it should control
```

### 6. GETPIVOTDATA — for stable KPI tiles

When you type `=` and click a pivot cell, Excel auto-writes GETPIVOTDATA. It looks scary but it's *robust* — it fetches by label, so it won't break if the pivot moves or resizes:

```excel
=GETPIVOTDATA("Sales Amount", $A$3, "Region", "West", "Month", "Jun")
```

Wrap it so a blank returns clean:

```excel
=IFERROR(GETPIVOTDATA("Sales Amount",$A$3,"FY","2025-26"),0)
```

Tip: to force a *normal* reference instead (e.g. `=B5`), turn off **PivotTable Analyze → Options ▾ → Generate GetPivotData**.

### 7. Conditional formatting

```
Select the range → Home → Conditional Formatting →
  • Data Bars       → in-cell bar chart
  • Color Scales    → red-yellow-green heatmap (great for variance %)
  • Icon Sets       → traffic lights on growth
  • Top/Bottom Rules → highlight top 10 debtors
  • New Rule → Use a formula:  =$G2<0   → fill red (flag negative margins)
```

### 8. Sparklines (inline mini-charts)

```
Select where they go → Insert → Sparklines → Line →
  Data Range: C2:N2  Location Range: O2 → OK
Sparkline tab → tick High Point + Low Point (red/green markers)
```

## Worked example / mini-project

**Scenario:** You're the MIS analyst at a mid-size FMCG distributor. You have a FY2025-26 sales export from the ERP: 38,000 rows, columns — `Order Date | Region | Salesperson | Product | Qty | Sales Amount | Cost`.

Reproduce it with a small sample and scale the idea:

| Order Date | Region | Product | Sales Amount (₹) | Cost (₹) |
|---|---|---|---|---|
| 05-04-2025 | West | Soap | 1,20,000 | 78,000 |
| 05-04-2025 | North | Shampoo | 2,40,000 | 1,80,000 |
| 12-05-2025 | West | Shampoo | 3,10,000 | 2,20,000 |
| 08-06-2025 | South | Soap | 95,000 | 61,000 |
| 20-06-2025 | North | Soap | 1,45,000 | 92,000 |

**Step-by-step build:**

1. `Ctrl+T` → name it `tblSales`. Add a helper column `Margin = [@[Sales Amount]]-[@Cost]`.
2. Insert PivotTable → Rows: Region; Columns: Months (group Order Date); Values: Sum of Sales Amount.
3. Add a **second value** — Sum of Margin — then right-click it → Show Values As → **% of Parent Row Total** to get margin %... or add a **calculated field**:

```
PivotTable Analyze → Fields, Items & Sets → Calculated Field
  Name:    Margin %
  Formula: = Margin / 'Sales Amount'
```

4. Insert a **Slicer** on Region and a **Timeline** on Order Date. Connect both to the pivot.
5. Build KPI tiles on a fresh "Dashboard" sheet:

```excel
Total Sales   =IFERROR(GETPIVOTDATA("Sales Amount",Pivot!$A$3),0)
Total Margin  =IFERROR(GETPIVOTDATA("Margin",Pivot!$A$3),0)
Margin %      =[Total Margin]/[Total Sales]
```

6. Insert a **PivotChart** (clustered column: Sales by Region; line: Margin % by month).
7. Add a monthly sparkline row and colour-scale the Margin % column.
8. Slice to "West" — every tile, chart and sparkline updates together. That's the deliverable: a manager clicks "West," sees ₹4.3L sales, 29% margin, June dip — no email to you.

**Refresh next month:** paste new rows below `tblSales`, press **Ctrl+Alt+F5**. Whole dashboard rebuilds.

## How it's tested

**Timed practical (most common — 30–45 min):** "Here's a raw sales/GL export. Build a summary of X by Y, add a slicer, and a chart on a separate tab." Assessors watch whether you make it a Table first, whether you use pivots (fast) or hand-build with SUMIFS (slow), and whether it refreshes cleanly.

**Interview questions you should nail:**
- "What's the difference between a slicer and a report filter?" → Slicers are visual, show current selection, and can drive multiple pivots; filters are a dropdown on one pivot.
- "Your pivot won't include new rows — why?" → Source is a fixed range, not a Table; or you didn't refresh.
- "Why does `=B5` become GETPIVOTDATA?" → Auto-generation is on; explain when it *helps* (stable KPIs) vs when to turn it off.
- "How do you show month-on-month growth in a pivot?" → Show Values As → % Difference From → (previous).
- "How would you flag debtors over 90 days?" → Conditional formatting rule / Top-Bottom / icon set.

**Case tell:** if given data with dates as text or numbers stored as text, they're testing whether you *notice* and fix it (Text-to-Columns / `VALUE`) before pivoting.

## Common mistakes & how pros avoid them

| Mistake | Fix / pro habit |
|---|---|
| Pivoting a fixed range → new data ignored | Always `Ctrl+T` into a Table first |
| Forgetting to refresh | Muscle-memory **Ctrl+Alt+F5** before every save |
| Numbers stored as text won't sum | Check with a quick COUNT vs SUM; fix via Text-to-Columns |
| Merged cells in source data | Never merge in data ranges — it breaks pivots |
| Hard-coding `=B5` from a pivot into a report | Use GETPIVOTDATA so it survives resizing |
| Rainbow dashboard, 6 fonts | 2–3 colours, one accent for "bad," align everything to a grid |
| Blank cells showing as `(blank)` | PivotTable Options → "For empty cells show: 0" or `-` |
| Grand totals mislead on averages | Understand Sum vs Average totals before presenting |
| Slicer drives only one of three pivots | Report Connections → tick all relevant pivots |

## Learn-it roadmap & resources

**Realistic time-to-proficiency:** the mechanics take a focused **weekend**. Being *fast and clean* under a 30-minute test takes **2–3 weeks** of doing it on real data.

| Week | Focus |
|---|---|
| 1 | Tables, basic pivots, Show Values As, date grouping |
| 2 | Slicers/timelines, Report Connections, GETPIVOTDATA, calculated fields |
| 3 | Full one-page dashboard on your own dataset; conditional formatting + sparklines |

**Resources:**
- Microsoft's official "Create a PivotTable" support docs (free, authoritative).
- **ExcelIsFun** and **Leila Gharani** on YouTube — free, project-based.
- Chandoo.org — dashboard design patterns and free templates.
- Paid: Microsoft **MO-201 (Excel Expert)** certification signals employer-recognised proficiency.
- Practice data: export your own Tally/Zoho Books ledger, or download a GSTR-2B JSON→CSV and reconcile it against a purchase register — the most job-realistic drill you can do.

Next step when data outgrows pivots: **Power Query** (clean/merge) + **Power Pivot / DAX** (data model). Pivots are the on-ramp to both.

## Quick-reference

| Task | How |
|---|---|
| Make source dynamic | `Ctrl+T` → name the Table |
| New PivotTable | `Insert → PivotTable` |
| Refresh all | `Ctrl+Alt+F5` |
| Group dates | Right-click date → **Group** → Months/Years |
| % of total / running total | Right-click value → **Show Values As** |
| MoM change | Show Values As → **% Difference From (previous)** |
| Custom metric | Analyze → **Calculated Field** |
| Filter visually | Analyze → **Insert Slicer / Timeline** |
| One slicer, many pivots | Right-click slicer → **Report Connections** |
| Stable KPI pull | `=GETPIVOTDATA("Sales Amount",$A$3,"Region","West")` |
| Turn off auto-GETPIVOTDATA | Analyze → Options ▾ → uncheck **Generate GetPivotData** |
| Heatmap / bars / icons | Home → **Conditional Formatting** |
| Flag negatives | CF → New Rule → formula `=$G2<0` → red fill |
| Inline trend chart | `Insert → Sparklines → Line` |
| Show 0 for blanks | PivotTable Options → **For empty cells show: 0** |
