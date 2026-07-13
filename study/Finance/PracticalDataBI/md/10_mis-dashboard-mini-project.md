# Mini-project: An End-to-End Finance MIS Dashboard

## What it is & where it's used

An **MIS (Management Information System) dashboard** is the one-page monthly picture that finance hands to a CEO/CFO/promoter: revenue vs target, gross margin, cash position, receivables ageing, top customers, expense heads, and where the business is bleeding. It sits on top of raw General Ledger (GL) exports and sales registers and turns thousands of transaction rows into 8-10 numbers a decision-maker actually reads.

This is the single most common "real" deliverable in Indian finance jobs. It's owned by **MIS Analysts, FP&A Analysts, Business Finance/Finance Business Partners, Financial Analysts, and Accounts Managers** in every SME, startup, and mid-cap. If you can build one unaided, you are immediately useful on day one — most freshers cannot.

The chapter builds the **full pipeline**: raw GL + sales CSV → a clean data model (star schema) → a Power BI / Excel dashboard → a monthly-reproducible process. Do it once here and you own a portfolio piece.

## The gap: why companies want this (and college didn't teach it)

College teaches you to *read* a P&L and Balance Sheet that someone else prepared. Industry needs you to **manufacture** the P&L from a messy 40,000-row Tally/SAP dump — every month, on the 3rd working day, with zero errors, and explain the variances.

The specific gaps this closes:

| College taught | Job needs |
|---|---|
| Interpret a finished P&L | Build P&L from a raw GL trial-balance export |
| Ratios in isolation | Ratios trended month-on-month with drill-down |
| "Prepare a statement" (once) | A *repeatable* process that runs every month unattended |
| One clean textbook dataset | Reconciling GL total to sales register, catching duplicates |
| Static answers | A live dashboard the CFO can filter by branch/product/month |

The unstated skill is **data plumbing**: mapping a ledger's chart-of-accounts to reporting heads, joining sales to a calendar, and building it so next month is a one-click refresh, not a rebuild.

## What "proficient" looks like

A job-ready person can, given a raw GL CSV and a sales register, unaided:

- Build a **cost-centre/account-head mapping table** so GL accounts roll up into P&L reporting lines.
- Construct a **star schema**: fact tables (GL, Sales) + dimension tables (Calendar, Account, Customer, Product).
- Write measures that produce **Revenue, COGS, Gross Margin %, EBITDA, MoM and YoY growth, MTD/YTD** correctly.
- Produce a **receivables ageing** bucket (0-30/31-60/61-90/90+).
- Tie the dashboard revenue back to the GL to the rupee (reconciliation).
- Refresh next month by **dropping in a new file** — no formula rewrites.
- Explain the top 3 variances in plain English.

## Hands-on: how to actually do it

**Raw inputs.** Two files exported from Tally/ERP:

`gl.csv` — `Date, Voucher, AccountCode, AccountName, CostCentre, Debit, Credit`
`sales.csv` — `Date, Invoice, CustomerCode, Customer, ProductCode, Product, Qty, Amount, GSTAmount`

And a mapping file you build by hand: `map_accounts.csv` — `AccountCode, ReportLine, ReportGroup` (e.g. `4001 → Sales → Revenue`, `5001 → Raw Material → COGS`, `6002 → Salaries → OpEx`).

### Step 1 — Clean & shape in Python (repeatable)

```python
import pandas as pd

gl   = pd.read_csv("gl.csv", parse_dates=["Date"])
mp   = pd.read_csv("map_accounts.csv")
sal  = pd.read_csv("sales.csv", parse_dates=["Date"])

# GL: signed amount (Dr +, Cr -) then map to report lines
gl["Amount"] = gl["Debit"].fillna(0) - gl["Credit"].fillna(0)
gl = gl.merge(mp, on="AccountCode", how="left")

# Catch unmapped accounts BEFORE they silently drop from the P&L
missing = gl[gl["ReportLine"].isna()]["AccountName"].unique()
assert len(missing) == 0, f"Unmapped accounts: {missing}"

gl["Month"] = gl["Date"].dt.to_period("M").astype(str)

# Monthly P&L pivot (income lines are credit-heavy so flip sign for reporting)
pnl = gl.groupby(["Month","ReportGroup","ReportLine"])["Amount"].sum().reset_index()
pnl.to_csv("fact_gl.csv", index=False)
sal.to_csv("fact_sales.csv", index=False)
```

### Step 2 — Reconcile (never skip this)

```python
gl_sales   = -gl.loc[gl["ReportLine"]=="Sales","Amount"].sum()   # credit → positive
reg_sales  = sal["Amount"].sum()
print("GL:", gl_sales, "Register:", reg_sales, "Diff:", gl_sales - reg_sales)
```

If the diff isn't zero (or a known GST/rounding gap), stop and investigate before dashboarding.

### Step 3 — SQL alternative for the same rollup

```sql
SELECT  strftime('%Y-%m', g.Date)          AS Month,
        m.ReportGroup,
        m.ReportLine,
        SUM(g.Debit - g.Credit)            AS Amount
FROM    gl g
JOIN    map_accounts m ON g.AccountCode = m.AccountCode
GROUP BY Month, m.ReportGroup, m.ReportLine
ORDER BY Month;
```

Receivables ageing straight from open invoices:

```sql
SELECT CASE
         WHEN julianday('now') - julianday(Date) <= 30  THEN '0-30'
         WHEN julianday('now') - julianday(Date) <= 60  THEN '31-60'
         WHEN julianday('now') - julianday(Date) <= 90  THEN '61-90'
         ELSE '90+' END                    AS Bucket,
       SUM(Amount)                         AS Outstanding
FROM sales WHERE Paid = 0 GROUP BY Bucket;
```

### Step 4 — Model it in Power BI (star schema)

Load `fact_gl`, `fact_sales`, and dimensions. Build a **Calendar** table and DAX measures:

```dax
Revenue     = CALCULATE( -SUM(fact_gl[Amount]), fact_gl[ReportLine]="Sales" )
COGS        = CALCULATE(  SUM(fact_gl[Amount]), fact_gl[ReportGroup]="COGS" )
Gross Margin   = [Revenue] - [COGS]
Gross Margin % = DIVIDE([Gross Margin], [Revenue])

Revenue LM  = CALCULATE([Revenue], DATEADD(Calendar[Date], -1, MONTH))
MoM %       = DIVIDE([Revenue] - [Revenue LM], [Revenue LM])
Revenue YTD = TOTALYTD([Revenue], Calendar[Date])
```

### Step 5 — The Excel-only version (no Power BI)

Same result with `SUMIFS` off a helper table:

```excel
=SUMIFS(fact_gl[Amount], fact_gl[ReportLine],"Sales", fact_gl[Month],$B$1)*-1
=XLOOKUP([@AccountCode], map[AccountCode], map[ReportLine], "UNMAPPED")
=LET(rev, B5, cogs, B6, (rev-cogs)/rev)          // Gross Margin %
```

Use a PivotTable on `fact_gl` (Rows = ReportGroup/ReportLine, Columns = Month, Values = Sum of Amount) as the P&L engine, then a clean dashboard sheet referencing it with `GETPIVOTDATA`.

## Worked example / mini-project

**Fictional co: Surya Traders Pvt Ltd, April 2026.** Raw GL rolls up to:

| ReportGroup | ReportLine | Apr (₹) |
|---|---|---|
| Revenue | Sales | 82,50,000 |
| COGS | Raw Material | 44,10,000 |
| COGS | Freight Inward | 3,20,000 |
| OpEx | Salaries | 11,40,000 |
| OpEx | Rent | 2,50,000 |
| OpEx | Power & Fuel | 1,80,000 |
| Other | Interest | 1,95,000 |

**Derived dashboard KPIs:**

| Metric | Formula | Value |
|---|---|---|
| Revenue | — | ₹82,50,000 |
| COGS | 44.10L + 3.20L | ₹47,30,000 |
| Gross Margin | Rev − COGS | ₹35,20,000 |
| Gross Margin % | 35.20 / 82.50 | **42.7%** |
| OpEx | 11.40+2.50+1.80 | ₹15,70,000 |
| EBITDA | GM − OpEx | ₹19,50,000 |
| EBITDA % | 19.50 / 82.50 | **23.6%** |
| PBT | EBITDA − Interest | ₹17,55,000 |

**Reconciliation:** sales register total = ₹82,50,000 → matches GL Sales line to the rupee. Green tick.

**Receivables ageing (from sales register, unpaid):**

| Bucket | ₹ | % |
|---|---|---|
| 0-30 | 9,80,000 | 55% |
| 31-60 | 4,60,000 | 26% |
| 61-90 | 2,10,000 | 12% |
| 90+ | 1,30,000 | 7% |

**MoM:** March revenue was ₹78,00,000 → MoM = (82.50−78.00)/78.00 = **+5.8%**. Dashboard shows the KPI card in green with the arrow.

**The one-page dashboard** then has: 4 KPI cards (Revenue, GM%, EBITDA, PBT) with MoM arrows, a 12-month revenue+margin trend line, a top-10-customers bar, an expense-head donut, and the ageing bar. Filters: Month, CostCentre. Next month: replace `gl.csv` and `sales.csv`, rerun the script / hit Refresh — done.

## How it's tested

**Practical assessment (the real gate):** You're handed a raw GL CSV and told *"Build me a monthly P&L and a gross-margin trend by 5 pm."* They watch whether you (a) map accounts, (b) reconcile, (c) get the sign convention right, (d) make it refreshable.

**Common interview questions:**
- "Walk me through how you'd build an MIS from a Tally export." (They want: export → map → model → reconcile → visualize → refresh.)
- "Your dashboard revenue is ₹2L higher than the sales register. What do you check first?" (Duplicate voucher, credit note not netted, GST mixed into amount, unmapped account.)
- "Difference between MTD and YTD, and how you'd compute both."
- "How do you make this reproducible next month without rebuilding?"
- "What's the difference between gross margin and EBITDA margin?"

**Timed Excel/SQL screen:** SUMIFS across a criteria set, XLOOKUP with a fallback, a GROUP BY rollup, an ageing CASE statement. 30-45 minutes.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Unmapped GL accounts silently dropped from P&L | `assert` / `XLOOKUP(...,"UNMAPPED")` check every refresh |
| Wrong Dr/Cr sign → income shows negative | Fix sign convention once in the model, flip income for display |
| GST amount counted as revenue | Keep taxable value and GST in separate columns; report net |
| Hard-coded month → breaks next cycle | Use a Calendar dimension + slicer, never type "April" in formulas |
| No reconciliation → confident but wrong numbers | Always tie dashboard revenue to the GL and sales register |
| Rebuilding from scratch monthly | Parameterise the file path; make refresh one click |
| Averaging percentages (avg of GM%s ≠ total GM%) | Compute ratios from summed numerator/denominator (DIVIDE) |
| Credit notes / returns ignored | Net them before totalling revenue |

## Learn-it roadmap & resources

**Time to proficiency:** ~3-4 weeks of focused evenings if you already know basic Excel.

- **Week 1** — Excel: SUMIFS, XLOOKUP, PivotTables, Power Query (get-and-transform). Build the P&L from CSV.
- **Week 2** — Data modelling: star schema, Calendar tables, DAX basics. Rebuild in Power BI (free desktop).
- **Week 3** — SQL: SELECT/JOIN/GROUP BY/CASE. Redo the rollup in SQLite/DB Browser (free).
- **Week 4** — Polish: reconciliation, ageing, variance commentary; write a one-page README so it's reproducible.

**Resources:** Power BI Desktop (free); DB Browser for SQLite (free); Microsoft Learn "Power BI" path (free); ICAI/company Tally exports for realistic data. **Certifications that carry weight:** Microsoft **PL-300 (Power BI Data Analyst)** and any structured SQL course. Build one real dashboard end-to-end and put the `.pbix` + screenshots in a portfolio — that beats any certificate in interviews.

## Quick-reference

| Need | Tool / snippet |
|---|---|
| Map account → report line | `=XLOOKUP(code, map[Code], map[Line], "UNMAPPED")` |
| Monthly P&L rollup | `SUMIFS(Amount, Line, "Sales", Month, B1)` |
| SQL rollup | `SUM(Debit-Credit) ... GROUP BY Month, ReportLine` |
| Revenue (DAX) | `CALCULATE(-SUM(Amount), Line="Sales")` |
| Gross Margin % | `DIVIDE([Revenue]-[COGS],[Revenue])` |
| MoM % | `DIVIDE([Rev]-[Rev LM],[Rev LM])` |
| YTD | `TOTALYTD([Revenue], Calendar[Date])` |
| Ageing bucket | `CASE WHEN days<=30 THEN '0-30' ...` |
| Reconcile | GL Sales total == sales register total == dashboard Revenue |

**Golden rule:** map → model → **reconcile** → visualise → make it one-click refreshable. If it doesn't tie to the rupee, it isn't done.
