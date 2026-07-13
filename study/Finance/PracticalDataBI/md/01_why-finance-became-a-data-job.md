# Why Finance Became a Data Job

## What it is & where it's used

Ten years ago a "finance job" meant Excel, a general ledger, and a printer. Today the ledger is a database, the reports are dashboards refreshed hourly, and the person who can *query the raw data* gets promoted over the person who waits for someone to email them a file. This book is about closing that gap.

The shift is structural. Businesses now generate transaction data at a volume Excel physically cannot hold (Excel caps at 1,048,576 rows — a mid-size D2C brand blows past that in a quarter of order lines). So the data moved into databases (SQL Server, PostgreSQL, Snowflake), into ERPs (SAP, Oracle NetSuite, Zoho Books, TallyPrime), and into GST/Income-Tax portals that emit JSON and CSV, not paper. Finance work is now: **pull the data → clean it → model it → explain it.** That pipeline runs on four tools:

| Layer | Tool | Finance use |
|---|---|---|
| Grab & shape small data | Excel / Google Sheets | Ad-hoc analysis, models, reconciliations |
| Pull large data from the source | SQL | GL extracts, sales ledgers, GSTR-2B matching |
| Automate & compute | Python (pandas) | Bank recos, GST reconciliation, forecasting |
| Present to a decision-maker | Power BI / Looker (DAX) | MIS dashboards, board packs, KPI tracking |

Where it's used, by role:

- **FP&A / MIS analyst** — SQL + Excel + Power BI. Builds the monthly MIS.
- **Accounts / R2R (Record-to-Report)** — Tally/SAP + Excel + increasingly SQL for reconciliations.
- **Tax / GST associate** — GST portal + Excel + Python for 2B-vs-books matching at scale.
- **Audit / assurance** — SQL + Excel (CAATs — Computer-Assisted Audit Techniques) to test 100% of transactions, not a sample.
- **Finance business partner / analyst at a startup** — all four, because there's no one else to do it.

## The gap: why companies want this (and college didn't teach it)

An MBA Finance or CA Inter curriculum teaches you *accounting standards, valuation, ratio analysis, cost sheets, and tax law.* All essential. None of it teaches you how to get 400,000 sales rows out of a database and reconcile them against GSTR-1 in twenty minutes.

The gap is not knowledge — it's **execution on real, messy, large data.** College gives you a clean 30-row balance sheet in a question paper. The job gives you a 90-column CSV export with blank cells, dates as text, ₹ symbols glued to numbers, and three spellings of the same vendor.

| What college taught | What the job actually needs |
|---|---|
| Prepare a Trial Balance from given data | *Extract* the TB from SAP via SQL, then tie it to sub-ledgers |
| Calculate current ratio | Build a live ratio dashboard that refreshes every morning |
| Journal entries by hand | Book 5,000 entries via an import template + validate them |
| GST computation for one invoice | Reconcile GSTR-2B vs purchase register for 8,000 invoices |
| VLOOKUP (if at all) | XLOOKUP, Power Query, pivot models, SQL joins |

Employers pay a premium for this because it's *rare among finance graduates and expensive to hire separately.* A data analyst who doesn't understand debits/credits can't do it either. You — finance-literate **and** data-capable — are the expensive hybrid.

## What "proficient" looks like

The concrete bar. A job-ready person can, **unaided**:

1. Take a raw ERP/bank/GST export and turn it into a clean, analysis-ready table (dedupe, fix types, handle blanks) without manual cell-by-cell editing.
2. Write a `SELECT` with a `JOIN`, `WHERE`, `GROUP BY` and `HAVING` to answer a business question directly from the database.
3. Build an Excel model that uses `XLOOKUP`/`SUMIFS`/`INDEX-MATCH` and doesn't break when a row is inserted.
4. Reconcile two data sets (books vs bank, books vs 2B) and produce a clean *difference* report with reasons.
5. Build a Power BI dashboard with a proper date table and 3–4 DAX measures that a CFO can read without asking questions.
6. Explain, in one sentence, what the number *means* for the business — the finance judgment that a pure data analyst lacks.

If you can do these six, you clear 80% of finance-analyst screens in India today.

## Hands-on: how to actually do it

**Excel — the modern lookup (stop using VLOOKUP):**
```
=XLOOKUP(A2, Vendors[GSTIN], Vendors[VendorName], "Not Found")
```
Sum sales for one region and month:
```
=SUMIFS(Sales[Amount], Sales[Region], "South", Sales[Month], "Jun")
```
Strip a ₹ symbol and text out of an imported number:
```
=VALUE(SUBSTITUTE(SUBSTITUTE(A2,"₹",""),",",""))
```

**SQL — pull a revenue summary straight from the ledger:**
```sql
SELECT  c.region,
        SUM(s.amount)          AS total_sales,
        COUNT(*)               AS invoice_count
FROM    sales      s
JOIN    customers  c ON c.customer_id = s.customer_id
WHERE   s.invoice_date >= '2026-04-01'
  AND   s.invoice_date <  '2026-07-01'   -- Q1 FY26-27
GROUP BY c.region
HAVING  SUM(s.amount) > 100000
ORDER BY total_sales DESC;
```

**Python (pandas) — a GSTR-2B vs purchase-register reconciliation:**
```python
import pandas as pd

books = pd.read_excel("purchase_register.xlsx")
gstr2b = pd.read_excel("gstr2b.xlsx")

recon = books.merge(
    gstr2b, on=["gstin", "invoice_no"],
    how="outer", suffixes=("_books", "_2b"), indicator=True
)
recon["tax_diff"] = recon["igst_books"].fillna(0) - recon["igst_2b"].fillna(0)

# invoices in books but not in 2B (ITC at risk)
missing_in_2b = recon[recon["_merge"] == "left_only"]
missing_in_2b.to_excel("itc_at_risk.xlsx", index=False)
```

**DAX — Power BI measures for an MIS dashboard:**
```
Total Sales = SUM(Sales[Amount])

Sales YTD = TOTALYTD([Total Sales], 'Date'[Date])

Sales MoM % =
VAR ThisM = [Total Sales]
VAR PrevM = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH))
RETURN DIVIDE(ThisM - PrevM, PrevM)
```

**TallyPrime — export data you can actually analyse:**
`Gateway of Tally → Display More Reports → Trial Balance → Alt+E (Export) → File Format: Excel (Spreadsheet) → Enter.` For raw vouchers: `Display More Reports → Day Book → F2 (change period) → Alt+E → Excel.` That export is your `SELECT * FROM ledger` when you have no database access.

**A journal entry, the thing the data ultimately represents** — credit sale of ₹1,00,000 + 18% GST to a Karnataka customer (intra-state):

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Debtors A/c | 1,18,000 | |
|   To Sales A/c | | 1,00,000 |
|   To Output CGST A/c (9%) | | 9,000 |
|   To Output SGST A/c (9%) | | 9,000 |

## Worked example / mini-project

**Build a one-page monthly MIS from raw exports.** Reproduce this with dummy data.

*Data:* export `Day Book` from Tally to `sales.xlsx` (columns: date, customer, region, amount, gst) — say 4,000 rows for June 2026.

**Step 1 — clean in Power Query (Excel/Power BI):** `Data → Get Data → From File → Excel`. In the editor: set `date` to Date type, `amount` to Decimal, `Remove Duplicates` on invoice number, `Replace Values` to strip ₹. Close & Load.

**Step 2 — the numbers (Excel pivot or SQL):**
```sql
SELECT region,
       SUM(amount)                    AS revenue,
       SUM(amount)*0.18               AS gst_liability,
       ROUND(AVG(amount),0)           AS avg_invoice
FROM   sales
GROUP BY region;
```
Suppose the result:

| Region | Revenue (₹) | GST (₹) | Avg invoice (₹) |
|---|---|---|---|
| South | 42,00,000 | 7,56,000 | 21,000 |
| West | 31,50,000 | 5,67,000 | 18,500 |
| North | 18,00,000 | 3,24,000 | 15,000 |
| **Total** | **91,50,000** | **16,47,000** | — |

**Step 3 — the insight (the finance bit):** South is 46% of revenue but has the highest average invoice — concentration risk if that one region dips. That sentence is what gets you hired; the pivot table is just plumbing.

**Step 4 — dashboard:** load into Power BI, add the DAX `Total Sales`, `Sales MoM %`, a region bar chart and a KPI card. One page, refreshable. You now have an MIS that took an afternoon and refreshes in one click next month.

## How it's tested

Interviews for finance-analyst roles now split into a *talk* round and a *do* round.

**Interview questions you'll hear:**
- "What's the difference between `WHERE` and `HAVING`?" (WHERE filters rows before grouping; HAVING filters after.)
- "VLOOKUP vs XLOOKUP — why switch?" (XLOOKUP searches right-to-left, defaults to exact match, returns a not-found value.)
- "How would you reconcile GSTR-2B with the purchase register for 8,000 invoices?"
- "Walk me through building an MIS from a raw ERP dump."

**The practical/assessment tests (the real filter):**
- **Timed Excel test (30–45 min):** given a messy sheet, build a summary with SUMIFS/XLOOKUP + a pivot. No internet.
- **SQL screen (HackerRank/DataCamp or live):** write 3–4 queries with joins and aggregation against a sample schema.
- **A "close these books" / reconciliation case:** here are two files, find and explain the differences.
- **Case + dashboard take-home:** "Here's 12 months of sales, build a dashboard and tell us what you'd flag to the CFO."

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Manually editing cells to "fix" data | Use Power Query / pandas — repeatable, auditable, one click next month |
| VLOOKUP everywhere; breaks on column insert | XLOOKUP or INDEX-MATCH; reference by column name |
| Reconciling by eyeballing two sheets | `merge(..., indicator=True)` or full-outer join; let the machine find diffs |
| Dumping a 40-column table on the CFO | One page, 3 KPIs, one insight sentence |
| `SELECT *` on a 10M-row table | Select only needed columns; filter dates in `WHERE` |
| Numbers with no "so what" | Always end with the business implication |
| Hard-coding dates/rates in formulas | Parameter cells / a Date table; change once |

## Learn-it roadmap & resources

Realistic time-to-proficiency for someone with a finance base, ~1 hour/day:

| Skill | To job-ready | Free resource | Paid / cert |
|---|---|---|---|
| Modern Excel | 3–4 weeks | ExcelJet, Chandoo.org | Microsoft MO-201 |
| SQL | 4–6 weeks | SQLBolt, Mode SQL Tutorial, LeetCode DB | DataCamp track |
| Power BI | 3–4 weeks | Microsoft Learn (free), Guy in a Cube (YouTube) | Microsoft PL-300 |
| Python/pandas | 6–8 weeks | Kaggle "pandas", freeCodeCamp | DataCamp / Coursera |

**Sequence:** Excel → SQL → Power BI → Python. Excel earns immediately; SQL is the highest ROI hire-signal; Power BI makes you visible to management; Python scales you. Don't chase all four at once — get *proficient* in Excel + SQL first (8–10 weeks) and you're already employable.

**Cert worth having in India:** Microsoft **PL-300 (Power BI Data Analyst)** — cheap, recognised, and directly maps to MIS roles. SQL needs no cert; a portfolio of 5 solved case dashboards on GitHub beats any certificate.

## Quick-reference

```
-- SQL skeleton
SELECT col, SUM(x) FROM t JOIN u ON t.id=u.id
WHERE date >= '2026-04-01' GROUP BY col HAVING SUM(x)>0 ORDER BY 2 DESC;
```
```python
# pandas reconciliation
a.merge(b, on="key", how="outer", indicator=True)   # _merge: left_only/right_only/both
```

| Need | Formula / step |
|---|---|
| Lookup | `=XLOOKUP(val, lookup_col, return_col, "NA")` |
| Conditional sum | `=SUMIFS(sum, crit_rng1, c1, crit_rng2, c2)` |
| Clean ₹ number | `=VALUE(SUBSTITUTE(SUBSTITUTE(A2,"₹",""),",",""))` |
| Import & clean | `Data → Get Data → Power Query → set types → Close&Load` |
| Tally export | `Report → Alt+E → Excel` |
| DAX YoY | `TOTALYTD([Measure], 'Date'[Date])` |
| GST (intra-state) | Output CGST 9% + SGST 9% on taxable value |
| Excel row limit | 1,048,576 — past this, use SQL |

**The one idea:** finance is now *pull → clean → model → explain.* Master the pipeline, keep the judgment, and you're the hybrid employers overpay for.
