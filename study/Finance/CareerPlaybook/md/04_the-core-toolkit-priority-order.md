# The core toolkit every finance pro needs

You cannot learn every tool, and you should not try. There is a priority order that maps to how much of your day each tool touches and how quickly it pays back. Learn them in this sequence: **Excel first (non-negotiable) → a data layer (SQL / BI / Python, pick one deeply) → domain tools (ERP like Tally/SAP, the GST portal, an FP&A/planning tool)**. Go deep where your role lives; stay literate everywhere else. This chapter shows you the actual formulas, queries, and click-paths — not adjectives about them.

## What it is & where it's used

| Layer | Tools | Roles that live here |
|---|---|---|
| 1. Spreadsheet | Excel, Google Sheets | Every finance role, without exception |
| 2. Data | SQL, Power BI/Tableau, Python (pandas) | FP&A, data-heavy analyst, treasury, revenue/RevOps finance |
| 3. Domain | TallyPrime, SAP/Oracle, GST portal, Zoho/QuickBooks, planning tools (Anaplan, Cube) | Accounts payable/receivable, audit, tax, controllership, statutory compliance |

A day-1 accounts executive in an Indian SME lives in **Tally + Excel + GST portal**. An FP&A analyst at a mid-cap lives in **Excel + Power BI + SQL**. A Big 4 audit associate lives in **Excel + the client's ERP + CaseWare/IDEA**. Same toolkit, different depth dial.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you *what* a contribution margin is and *why* WACC matters. It did not make you build a 12-tab rolling forecast that ties out to the penny, write a `GROUP BY` to reconcile 40,000 invoice lines, or file a GSTR-3B before the 20th. Colleges grade concepts; employers pay for **artifacts produced under a deadline with real, messy data**.

The specific gaps:
- **Speed and correctness on dirty data.** Textbooks give clean tables. Reality gives you trailing spaces, ₹ stored as text, and duplicate vendor codes.
- **Auditability.** A pro's model can be checked by someone else. College spreadsheets are write-once.
- **Tool fluency = throughput.** The person who does keyboard-only Excel and writes a SQL join does in 20 minutes what a manual analyst does in a day.

Closing this gap is the single highest-ROI thing you can do before your first role.

## What "proficient" looks like

The bar employers actually test for, per layer:

- **Excel (must clear this to be hireable):** builds a model with no hardcoded numbers inside formulas, uses `XLOOKUP`/`INDEX-MATCH`, `SUMIFS`, `IF`/`IFS`, absolute vs relative references (`$`), pivot tables, and a basic three-statement or cash-flow linkage. Navigates with keyboard (Alt keystrokes, `Ctrl+Arrow`, `F4`). Knows why circular references break a model.
- **Data (pick one deeply):** writes a multi-table `JOIN` with `GROUP BY` and a filter, OR builds a Power BI report with a DAX measure and a slicer, OR loads a CSV in pandas and does a `groupby().agg()`. You do not need all three — you need one you can defend in an interview.
- **Domain:** for accounts/tax roles — posts correct journal entries, runs a Tally ledger and GST report, and files/reconciles a GST return (GSTR-2B vs purchase register). For FP&A — owns a budget-vs-actual variance pack.

## Hands-on: how to actually do it

### Excel — the formulas that earn their keep

```excel
# Modern lookup — replaces VLOOKUP; searches any direction, handles "not found"
=XLOOKUP(A2, Vendors[Code], Vendors[Name], "Not found")

# Conditional sum across multiple criteria (the FP&A workhorse)
=SUMIFS(Sales[Amount], Sales[Region], "South", Sales[Month], ">="&DATE(2026,4,1))

# Robust lookup that survives inserted columns
=INDEX(Price[Rate], MATCH(A2, Price[SKU], 0))

# Tiered logic without nested IFs
=IFS(B2>=1000000,"Large", B2>=100000,"Mid", TRUE,"Small")

# Clean dirty numbers stored as text with stray spaces / ₹ symbols
=VALUE(SUBSTITUTE(SUBSTITUTE(A2,"₹",""),",",""))

# Spill a unique, sorted list (dynamic arrays, Excel 365)
=SORT(UNIQUE(Sales[Customer]))
```

`F4` toggles `$` anchoring — `A$1`, `$A1`, `$A$1`. Lock your assumption cells; leave calculation cells relative. That single discipline separates an auditable model from a broken one.

### SQL — reconcile and aggregate at scale

```sql
-- Sales by region for Q1 FY26-27, only regions above a ₹10L threshold
SELECT r.region_name,
       SUM(s.amount)          AS total_sales,
       COUNT(*)               AS invoice_count
FROM   sales s
JOIN   regions r ON r.region_id = s.region_id
WHERE  s.invoice_date BETWEEN '2026-04-01' AND '2026-06-30'
GROUP  BY r.region_name
HAVING SUM(s.amount) > 1000000
ORDER  BY total_sales DESC;

-- Find purchase invoices in your books but NOT in GSTR-2B (mismatch hunt)
SELECT p.invoice_no, p.gstin, p.taxable_value
FROM   purchase_register p
LEFT   JOIN gstr2b g ON g.invoice_no = p.invoice_no
                    AND g.gstin      = p.gstin
WHERE  g.invoice_no IS NULL;
```

`LEFT JOIN ... WHERE right IS NULL` is the anti-join — the core pattern for every reconciliation you will ever do.

### Python (pandas) — when data outgrows a spreadsheet

```python
import pandas as pd

df = pd.read_csv("sales_fy26.csv", parse_dates=["invoice_date"])
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")   # coerce dirty text to NaN

# Region-wise revenue and average ticket
summary = (df.groupby("region")
             .agg(total=("amount", "sum"),
                  avg_ticket=("amount", "mean"),
                  invoices=("amount", "count"))
             .sort_values("total", ascending=False))

# Reconcile books vs portal via a merge (same idea as SQL anti-join)
mismatch = books.merge(portal, on=["invoice_no", "gstin"],
                       how="left", indicator=True)
mismatch = mismatch[mismatch["_merge"] == "left_only"]
print(summary)
```

### DAX — for Power BI reports

```dax
Total Sales   = SUM(Sales[Amount])
Sales LY      = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
YoY Growth %  = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
```

### TallyPrime + GST portal — the domain click-path

- **Post a purchase in Tally:** Gateway of Tally → Vouchers → `F9` (Purchase) → select party → item → tax ledgers (CGST/SGST or IGST) auto-compute → `Ctrl+A` to save.
- **See a ledger:** Gateway → Display More Reports → Account Books → Ledger.
- **GST filing:** log in at gst.gov.in → Returns Dashboard → pick period → **GSTR-1** (outward supplies) → **GSTR-3B** (summary + tax payment) → offset liability from Electronic Credit/Cash Ledger → file with DSC/EVC. Reconcile **GSTR-2B** (auto-drafted ITC) against your purchase register *before* claiming input credit.

### Journal entries — the language underneath every tool

| Transaction | Account | Dr (₹) | Cr (₹) |
|---|---|---|---|
| Credit purchase, goods ₹1,00,000 + 18% GST | Purchases A/c | 1,00,000 | |
| | Input CGST A/c | 9,000 | |
| | Input SGST A/c | 9,000 | |
| | To Vendor A/c | | 1,18,000 |
| Salary accrued | Salary A/c | 50,000 | |
| | To Salary Payable | | 50,000 |

## Worked example / mini-project

**Build a budget-vs-actual variance pack for "Kaveri Traders" (FY 2026-27, Q1).**

1. **Data.** Two sheets: `Budget` and `Actuals`, columns = Cost Centre, Month, Amount. Say budgeted opex ₹42,00,000; actual ₹45,60,000.
2. **Pull actuals against budget** with a keyed lookup:
   ```excel
   =SUMIFS(Actuals[Amount], Actuals[CostCentre], A2, Actuals[Month], B2)
   ```
3. **Variance and %:**
   ```excel
   =Actual - Budget                      # ₹3,60,000 unfavourable
   =(Actual - Budget)/Budget             # 8.6% over
   ```
4. **Flag the outliers** so a manager reads it in 5 seconds:
   ```excel
   =IF(ABS(VarPct)>0.10, "REVIEW", "OK")
   ```
5. **Summarise** with a pivot: rows = Cost Centre, values = Sum of Variance, then sort descending. Marketing is ₹2,10,000 over on a ₹5,00,000 budget (42%) — that is your headline.
6. **One-line narrative:** "Q1 opex ran 8.6% (₹3.6L) over budget, driven by Marketing (+42%) on an unplanned campaign; travel and utilities were on-plan."

That deliverable — numbers that tie out, outliers flagged, a one-line story — is exactly what an FP&A hiring manager wants to see.

## How it's tested

| Role | Interview questions | Practical test |
|---|---|---|
| FP&A analyst | "VLOOKUP vs INDEX-MATCH vs XLOOKUP — when each?" "How do you avoid circular refs in a model?" | **Timed Excel test (30–60 min):** given raw sales data, build a pivot, compute variance %, flag exceptions. No internet. |
| Data/BI analyst | "Explain the anti-join." "INNER vs LEFT JOIN." "What does `GROUP BY` return?" | **Live SQL screen** on HackerRank/DataLemur: write a query against a schema they hand you. |
| Accounts / tax | "Pass the journal entry for a credit purchase with GST." "GSTR-2A vs 2B?" | **"Close these books" case:** post vouchers in Tally, produce a trial balance, reconcile 2B vs purchase register. |
| Controllership | "Walk me through a 3-statement model." | Take-home model with a broken link to fix. |

Assume the practical test is unaided and timed. Prepare by *doing*, not watching.

## Common mistakes & how pros avoid them

- **Hardcoding numbers inside formulas** (`=B2*1.18`). Pros put the 18% in a labelled assumption cell and reference it. Auditable, changeable.
- **VLOOKUP breaking on inserted columns.** Use `XLOOKUP` or `INDEX-MATCH`.
- **Trusting dirty data.** Numbers stored as text silently break `SUMIFS`. Run `=ISNUMBER()`, use `VALUE()`/`TRIM()`, watch for the green triangle.
- **`SELECT *` in SQL** and forgetting `GROUP BY` non-aggregated columns. Name columns; aggregate deliberately.
- **Claiming GST input credit before 2B reconciliation** — a real compliance error that triggers notices. Always reconcile first.
- **No version control on models.** Pros date filenames (`Model_2026-07-03_v3.xlsx`) and freeze the assumptions tab.
- **Learning three tools shallowly.** One deep skill beats three you can't defend under questioning.

## Learn-it roadmap & resources

| Skill | Time to job-ready | Resources |
|---|---|---|
| Excel (core) | 4–6 weeks, daily practice | Microsoft Excel help; ExcelJet cheat-sheet; Chandoo.org; *Excel to the max* problems. Cert (optional): **Microsoft Office Specialist – Excel Associate**. |
| SQL | 3–4 weeks | Mode SQL Tutorial (free), SQLBolt, DataLemur, LeetCode Database. |
| Power BI | 3–4 weeks | Microsoft Learn (free); **PL-300** cert is well-recognised in India. |
| Python/pandas | 6–8 weeks | Kaggle "Pandas" micro-course (free); *Python for Data Analysis* (McKinney). |
| Tally + GST | 2–3 weeks | TallyEducation.com; GSTN free videos; practise on the GST **offline/sandbox**. Cert: **Tally ACE/Professional**. |

Realistic total to a strong finance-toolkit baseline: **~3 months** of focused daily practice alongside your CA prep. Sequence: nail Excel → add SQL *or* Power BI → layer Tally + GST (which your CA syllabus already reinforces).

## Quick-reference

| Need | Tool | Formula / command |
|---|---|---|
| Directional lookup | Excel | `=XLOOKUP(key, lookup_col, return_col, "NA")` |
| Multi-criteria sum | Excel | `=SUMIFS(sum, c1, v1, c2, v2)` |
| Robust lookup | Excel | `=INDEX(ret, MATCH(key, look, 0))` |
| Clean text→number | Excel | `=VALUE(SUBSTITUTE(A2,",",""))` |
| Anchor references | Excel | `F4` → `$A$1` |
| Aggregate w/ filter | SQL | `SELECT col, SUM(x) ... GROUP BY col HAVING ...` |
| Find non-matches | SQL | `LEFT JOIN ... WHERE b.id IS NULL` |
| Group summary | pandas | `df.groupby("k").agg(total=("x","sum"))` |
| YoY measure | DAX | `CALCULATE([Sales], SAMEPERIODLASTYEAR('Date'[Date]))` |
| GST input credit | Portal | Reconcile **GSTR-2B** vs purchase register *before* claiming |
| GST monthly file | Portal | GSTR-1 → GSTR-3B → offset → file (by 11th / 20th) |
| Purchase entry | Tally | `F9` → party → item → tax ledgers → `Ctrl+A` |

**Standard GST rates:** 0%, 5%, 12%, 18%, 28%. **Filing dates:** GSTR-1 by 11th, GSTR-3B by 20th of the following month (monthly filers). Keep this card next to your keyboard for your first 90 days.
