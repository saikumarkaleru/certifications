# Tableau & Choosing Your BI Tool

## What it is & where it's used

Tableau is a drag-and-drop data-visualization and dashboarding tool. You connect it to a data source (Excel, CSV, SQL Server, Snowflake, Google Sheets), drag fields onto "shelves," and it draws charts. String a few charts together and you have an interactive dashboard that a CFO can filter by region, month, or product without touching a formula.

In finance/accounts roles, BI tools live wherever numbers need to be *seen* repeatedly by non-analysts:

| Role | What they build in Tableau/Power BI |
|---|---|
| FP&A analyst | Budget vs actual dashboard, refreshed monthly |
| Revenue/AR analyst | Ageing dashboard, DSO trend, collection heatmap |
| Cost/plant controller | Cost-per-unit, variance waterfall by cost centre |
| Treasury | Cash-position dashboard across bank accounts |
| Tax/compliance | GST liability vs ITC trend, filing-status tracker |
| MIS executive | The monthly management deck, auto-refreshed |

The pattern is identical everywhere: raw data → clean model → chart → published dashboard that others self-serve. Tableau is the market-leading tool for the "chart + dashboard" half. Power BI is its main rival. Excel is the third leg — and still the one you'll actually use most days.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you to *analyse* a company. It does not teach you to build a thing that 40 people open every Monday. The gap is **repeatable, self-service reporting**:

- College output = a one-off answer in a slide. Industry output = a *living dashboard* that refreshes itself and lets the viewer drill down without emailing you.
- Nobody in a B-school case study asks "how will this refresh next month?" or "can the regional head filter to just South zone?" Every real MIS job asks exactly that.
- Excel charts break when data grows or columns move. BI tools separate the *data model* from the *view*, so the report survives new months of data. That architectural idea — model once, visualise many — is the actual skill, and it's never taught.

Companies pay for BI because manual monthly reporting is a tax: a junior spends three days rebuilding the same deck. A good dashboard turns three days into a five-minute refresh. That saving is the job.

## What "proficient" looks like

The bar an employer tests for — what a job-ready person does unaided:

- **Connect and shape:** pull data from Excel/SQL, fix data types, create a clean join or relationship, without needing pre-cleaned data.
- **Calculated fields:** write a profit-margin, YoY-growth, or running-total calc from scratch.
- **The right chart:** knows a trend = line, a part-to-whole = bar (not pie), a variance = waterfall or bar with reference line. Doesn't decorate.
- **Interactivity:** adds filters, parameters, and drill-downs so the viewer answers their own follow-up.
- **Publish & control access:** pushes to Tableau Server/Cloud or Power BI Service, sets a refresh schedule, and shares to the right people (not "everyone in company").
- **Tool judgment:** can say *why* this report is Tableau and that one is just an Excel PivotTable — and not over-engineer.

## Hands-on: how to actually do it

**1. Connecting data (Tableau Public / Desktop)**
`Connect → Microsoft Excel → select file → drag sheet to canvas`. Tableau splits fields into **Dimensions** (text/date — the "by what") and **Measures** (numbers — the "how much"). Sales *by* Region *over* Month: drag `Order Date` to Columns, `Sales` to Rows, `Region` to Colour.

**2. A calculated field** (`Analysis → Create Calculated Field`):

```
// Profit Margin %
SUM([Profit]) / SUM([Sales])
```
```
// YoY Sales Growth (table calc alternative)
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))
```
```
// Bucketing AR ageing
IF [Days Overdue] <= 30 THEN "0-30"
ELSEIF [Days Overdue] <= 60 THEN "31-60"
ELSEIF [Days Overdue] <= 90 THEN "61-90"
ELSE "90+" END
```

**3. LOD expression** (Tableau's signature feature — compute at a different grain than the view):

```
// Sales per customer, regardless of what's on the view
{ FIXED [Customer Name] : SUM([Sales]) }
```

**4. The Power BI / DAX equivalent** (same logic, different language). In Power BI you write measures:

```dax
Total Sales = SUM(Sales[Amount])

Profit Margin % =
DIVIDE(SUM(Sales[Profit]), SUM(Sales[Amount]))

YoY Growth % =
VAR CurYr = [Total Sales]
VAR PrevYr = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, YEAR))
RETURN DIVIDE(CurYr - PrevYr, PrevYr)
```

**5. The Excel equivalent** (for when a dashboard is overkill). A PivotTable + slicer *is* a mini-BI dashboard. To pull a value into a management sheet:

```excel
=XLOOKUP(A2, Data!$A:$A, Data!$D:$D, "Not found")

=SUMIFS(Sales[Amount], Sales[Region], "South", Sales[Month], "Apr")
```

**6. Publishing (Tableau):** `Server → Publish Workbook → sign in to Tableau Cloud → choose Project (folder) → set Permissions → set Data Source refresh schedule (e.g. daily 7am)`. Viewers open a URL; no Tableau install needed.

**7. Publishing (Power BI):** `Home → Publish → pick Workspace`. Then in the browser: `Workspace → Dataset → Schedule refresh → set gateway + time`. Share via `App` or add users to the workspace.

## Worked example / mini-project

**Build: an Accounts Receivable ageing dashboard for an Indian mid-size firm.**

Sample data (`invoices.csv`), reproduce with ~200 rows like:

| Invoice | Customer | Region | Invoice Date | Due Date | Amount (₹) | Paid? |
|---|---|---|---|---|---|---|
| INV-1001 | Reliance Retail | West | 2026-04-05 | 2026-05-05 | 4,50,000 | No |
| INV-1002 | Infosys | South | 2026-05-12 | 2026-06-11 | 2,20,000 | No |
| INV-1003 | Tata Steel | East | 2026-03-01 | 2026-03-31 | 8,75,000 | No |

Steps:

1. Connect the CSV in Tableau. Create `Days Overdue = DATEDIFF('day', [Due Date], TODAY())`.
2. Create the ageing bucket calc from section 4 above.
3. **Chart 1 (bar):** `Ageing Bucket` on Columns, `SUM(Amount)` on Rows. Instantly shows ₹ stuck in 90+.
4. **Chart 2 (heatmap):** `Region` on Rows, `Ageing Bucket` on Columns, `SUM(Amount)` on Colour. Red = West's 90+ bucket is your problem child.
5. **KPI:** `Total Outstanding = SUM([Amount])` filtered to `Paid? = "No"`; add `DSO ≈ (AR / Credit Sales) × 365` as a text tile.
6. Add a **Region filter** and a **Customer** quick filter. Combine all four onto one Dashboard sheet.
7. Publish to Tableau Cloud, schedule daily refresh, share to the collections team's email group only.

Outcome: the collections head opens one URL, filters to "West / 90+", and sees ₹8.75L from Tata Steel is the single biggest overdue — a decision that used to need a half-day Excel pull.

## How it's tested

Interviews mix concept questions with a **live build test**.

Typical questions:
- "When would you use Tableau over an Excel PivotTable?" (Answer: recurring, multi-user, needs scheduled refresh and interactivity; Excel for one-off analysis or heavy ad-hoc modelling.)
- "Difference between a filter and a parameter?" (Filter limits data shown; parameter is a user-input value you plug into calcs/what-ifs.)
- "What's an LOD expression / why FIXED?" (Compute at a grain independent of the view.)
- "Bar vs pie — when?" (Almost always bar; pie only for 2–3 slices summing to 100%.)
- "Star schema vs one flat table — why care?" (Fact + dimension tables; faster, cleaner measures, avoids duplication.)

The practical test (60–90 min, take-home or live): "Here's a messy sales/AR CSV. Build a dashboard showing [trend + breakdown + one KPI], make it filterable by region, and tell us the top insight." They score: correct chart choice, working calculated field, interactivity, cleanliness (no chartjunk), and whether you *found the insight*, not just drew boxes.

## Common mistakes & how pros avoid them

- **Pie charts and 3D everything.** Pros default to bars and lines; colour carries one meaning, not five.
- **Building on a flat, un-modelled table.** Learn a simple star schema (one fact table, dimension tables for Date/Region/Customer). Makes measures correct and fast.
- **Over-engineering.** If two people need it once, it's an Excel PivotTable, not a Tableau server workbook. Pros match tool to lifespan.
- **No refresh plan.** A dashboard nobody scheduled dies in month two. Set the schedule *before* you share.
- **Sharing to "everyone."** Finance data is sensitive; set row/folder-level permissions.
- **Hard-coding dates/values in calcs.** Use `TODAY()`, parameters, and relative-date filters so it survives next month.
- **Ignoring performance.** Extracts (not live) for large data; filter at source; don't drag 2M rows into Tableau Public.

## Learn-it roadmap & resources

Realistic time-to-proficiency: **3–5 weeks** part-time to job-ready if you already know Excel PivotTables.

| Week | Focus |
|---|---|
| 1 | Excel PivotTables + charts mastery (the foundation) |
| 2 | Tableau Public: connect, dimensions/measures, basic charts |
| 3 | Calculated fields, LOD, filters, parameters, dashboards |
| 4 | Publishing, refresh, permissions; build 2 portfolio dashboards |
| 5 | Learn Power BI + DAX basics so you're tool-agnostic |

Resources:
- **Tableau Public** — free desktop tool + free portfolio hosting. Build here and put the link on your CV.
- Tableau's official free training videos + "Makeover Monday" community datasets for practice.
- **Power BI Desktop** — free download; the Microsoft Learn "PL-300" path is the best free curriculum.
- Certifications: **Tableau Desktop Specialist** (~US$100) or **Microsoft PL-300 (Power BI Data Analyst)** — PL-300 is more recognised in Indian corporates because most run Microsoft 365.

Pick Power BI first if you're India-targeting and cost-sensitive: it's cheaper for employers, bundled with Office 365, and dominates Indian mid-market finance teams. Add Tableau for MNCs and analytics-heavy shops.

## Quick-reference

| Need | Excel | Tableau | Power BI |
|---|---|---|---|
| One-off analysis | ✅ Best | Overkill | Overkill |
| Recurring multi-user dashboard | Weak | ✅ | ✅ |
| Scheduled auto-refresh | No | ✅ | ✅ |
| Cost for employer | Owned | ₹₹₹ | ₹ (in O365) |
| Language for calcs | Formulas | Calc fields | DAX |
| Ad-hoc modelling / what-if | ✅ Best | Weak | Medium |

**Chart cheat-sheet:** trend → line · comparison → bar · part-to-whole → stacked bar (not pie) · variance → waterfall · relationship → scatter · distribution → histogram · concentration → heatmap.

**Tableau essentials:** Dimensions = "by what", Measures = "how much" · Filter = limit data · Parameter = user input · `{FIXED [X] : SUM([Y])}` = LOD · Extract = fast snapshot, Live = real-time.

**Publish flow:** clean model → build sheets → assemble dashboard → set filters → publish to Cloud/Service → schedule refresh → set permissions → share URL.

**Decision rule:** *Will 3+ people open this repeatedly?* → BI tool. *Just me, just now?* → Excel PivotTable.
