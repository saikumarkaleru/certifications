# Cheat-sheet: formulas & shortcuts

## What it is & where it's used

This chapter is the printable last-page you rip out and tape next to your monitor. It compresses the whole guide — lookups, aggregation, cleanup, dates, finance math, keyboard flow, PivotTables, a bit of SQL and Python — into a dense, copy-usable reference. Every analyst, accountant, FP&A associate, tax executive and equity researcher lives in these formulas eight hours a day. In an interview you get judged on how few keystrokes you waste; on the job you get paid for turning a raw dump into a clean answer before the 6 pm review call.

Roles that need it: **FP&A / budgeting**, **financial analyst / equity research**, **accounts & controllership**, **audit**, **GST/tax compliance**, **investment banking associate**, **credit analyst**. If Excel is open on your screen more than your email, this page is your operating system.

## The gap: why companies want this (and college didn't teach it)

MBA and CA classrooms teach *concepts* — NPV, working capital, revenue recognition — but assume the numbers are already in a tidy table. Industry never hands you a tidy table. You get a 40,000-row SAP export with trailing spaces, dates stored as text, ₹ signs glued to amounts, and a "Customer Name" column that's spelled three different ways. The gap is **mechanical fluency**: the ability to reconcile, join, clean and summarise without touching the mouse and without breaking when a row is added.

College rewards the *right final number*. Employers reward *the right number, auditable, refreshable, and delivered in twenty minutes*. This cheat-sheet is the muscle memory that closes that gap.

## What "proficient" looks like

A job-ready person can, unaided:

- Build a two-condition lookup with `XLOOKUP`/`INDEX-MATCH` without converting anything to a helper column.
- Reconcile two ledgers (book vs bank, GSTR-2B vs purchase register) and flag the breaks.
- Clean a dirty export — `TRIM`, `TEXT`-to-date, split names — in under five minutes.
- Drive Excel keyboard-only: `Ctrl+Shift+Arrow`, `Alt+=`, `Ctrl+T`, `F4`.
- Spin up a PivotTable and a `SUMIFS` dashboard that refresh when data grows.
- Know when to leave Excel — pull the raw data with a `SELECT ... GROUP BY` instead of a 500k-row copy-paste.

## Hands-on: how to actually do it

### Lookups & joins

```excel
' Exact lookup, modern (Excel 365 / 2021)
=XLOOKUP(A2, Master[ID], Master[Name], "Not found")

' Two-condition lookup (invoice + line item), array-safe
=XLOOKUP(1, (Master[Inv]=A2)*(Master[Line]=B2), Master[Amount])

' Legacy but universal — works everywhere incl. old corporate builds
=INDEX(Master[Name], MATCH(A2, Master[ID], 0))

' Left-lookup / approximate band (tax slab, ageing bucket) — sorted ascending
=XLOOKUP(A2, Slab[Upper], Slab[Rate], , 1)   ' 1 = next larger match
```

Avoid `VLOOKUP` for new work: it breaks when columns are inserted and can't look left. If you must, lock the table: `=VLOOKUP(A2,$D$2:$F$999,3,FALSE)`.

### Conditional aggregation (the FP&A workhorse)

```excel
=SUMIFS(Amt, Region, "West", Month, ">="&DATE(2026,4,1))
=COUNTIFS(Status, "Open", Ageing, ">90")
=AVERAGEIFS(Margin, Product, "SKU-101")
=SUMPRODUCT((Region="West")*(Qty)*(Price))   ' when SUMIFS can't multiply
```

### Cleanup & text

```excel
=TRIM(CLEAN(A2))                       ' strip spaces + non-printing chars
=VALUE(SUBSTITUTE(A2,"₹",""))          ' text "₹1,200" -> number
=DATEVALUE(TEXT(A2,"dd-mm-yyyy"))      ' text date -> real date
=TEXTSPLIT(A2," ")                     ' 365: split "Ravi Kumar" into cells
=TEXTBEFORE(A2,"@")  =TEXTAFTER(A2,"@")
=PROPER(TRIM(A2))                      ' normalise names
=IFERROR(XLOOKUP(...), "check")        ' never show #N/A in a deck
```

### Dates & finance math

```excel
=EOMONTH(A2,0)                         ' month-end (period close)
=EDATE(A2,12)                          ' same day next year
=YEARFRAC(A2,B2,1)                     ' actual/actual for interest
=NPV(0.12, C2:C11) + C1                ' C1 = year-0 outflow
=XNPV(0.12, Cash, Dates)               ' irregular cash flows
=IRR(C1:C11)   =XIRR(Cash, Dates)
=PMT(0.09/12, 60, -500000)             ' EMI on ₹5,00,000, 9%, 5 yrs
=FV(0.07,10,-100000)   =PV(0.08,5,,-1000000)
```

### SQL — pull, don't copy-paste

```sql
-- Monthly sales by region, straight from the source
SELECT region, DATE_TRUNC('month', invoice_date) AS mth,
       SUM(taxable_value)  AS sales,
       SUM(igst+cgst+sgst) AS tax
FROM   sales_register
WHERE  invoice_date >= '2026-04-01'
GROUP  BY region, mth
ORDER  BY mth, sales DESC;
```

### Python — when the file is too big for Excel

```python
import pandas as pd
df = pd.read_excel("sap_dump.xlsx")
df["amount"] = (df["amount"].astype(str)
                .str.replace("₹","").str.replace(",","").astype(float))
pivot = df.pivot_table(index="region", columns="month",
                       values="amount", aggfunc="sum", margins=True)
pivot.to_excel("summary.xlsx")
```

### DAX (Power BI / Power Pivot)

```dax
Total Sales   = SUM(Sales[Amount])
Sales LY      = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
YoY %         = DIVIDE([Total Sales]-[Sales LY], [Sales LY])
Margin %      = DIVIDE([Total Sales]-[Total COGS], [Total Sales])
```

## Worked example / mini-project

**GSTR-2B vs Purchase Register reconciliation** — the monthly task every tax executive does.

You have two sheets: `Books` (your recorded purchases) and `GSTR2B` (what the portal says your vendors filed). Goal: find Input Tax Credit (ITC) you can safely claim.

Sample rows:

| GSTIN | Invoice | Taxable (₹) | IGST (₹) |
|---|---|---|---|
| 27ABCDE1234F1Z5 | INV-091 | 1,00,000 | 18,000 |
| 29PQRSX9876G1Z2 | INV-104 | 50,000 | 9,000 |

Build a match key and lookup in `Books`:

```excel
' Key in both sheets
=TRIM(A2)&"|"&TRIM(B2)

' In Books, pull the 2B tax against each invoice
=XLOOKUP([@Key], GSTR2B[Key], GSTR2B[IGST], "Not in 2B")

' Break flag
=IF([@BooksIGST]=[@IGST_2B], "Match",
   IF([@IGST_2B]="Not in 2B","Missing in 2B","Value diff"))

' Claimable ITC = only what appears in 2B
=SUMIFS(Books[IGST], Books[Status], "Match")
```

Then a PivotTable on `Status` gives the summary the manager wants:

| Status | Count | IGST (₹) |
|---|---|---|
| Match | 142 | 11,84,000 |
| Missing in 2B | 8 | 61,200 |
| Value diff | 3 | 4,500 |

Claimable this month = ₹11,84,000. The ₹61,200 "Missing in 2B" is chased with vendors — that's the deliverable. Whole thing: 15 minutes once the keys are built.

## How it's tested

**Timed Excel test (most common, 30–45 min):** given a raw sheet, you're asked to (1) clean it, (2) build a lookup between two tables, (3) produce a `SUMIFS` summary or PivotTable, (4) sometimes an EMI/NPV. Graders watch whether you use structured references and keyboard shortcuts — mouse-heavy candidates run out of time.

**SQL screen (analyst/BI roles):** "Write monthly revenue by region" or "top 5 customers by outstanding" — a `GROUP BY` + `ORDER BY ... LIMIT`, sometimes a `JOIN`.

**Case / "close these books":** a mini reconciliation (bank vs book, or 2B) with intentional breaks planted. They want to see you *find* the breaks, not just tie the total.

**Interview questions you'll hear:**
- "VLOOKUP vs INDEX-MATCH vs XLOOKUP — when and why?"
- "Your SUMIFS returns 0 but you know data exists — debug it." (Answer: text-vs-number mismatch, trailing spaces, wrong criteria range.)
- "Difference between NPV and XNPV / IRR and XIRR?"
- "How do you make a report auto-refresh when rows are added?" (Answer: Excel Tables + structured refs, or Power Query.)

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| `SUMIFS` returns 0 — numbers stored as text | `=A2+0` or `VALUE()`, or Data > Text to Columns |
| `VLOOKUP` breaks after column insert | Use `XLOOKUP`/`INDEX-MATCH` |
| Forgetting `$` locks, formula drifts | `F4` to toggle absolute refs |
| `NPV()` including year-0 in the range | Keep year-0 outside: `=NPV(r,C2:C11)+C1` |
| Merged cells killing sort/pivot | Never merge in data ranges; use Center Across Selection |
| Hard-coding numbers inside formulas | Put assumptions in labelled input cells |
| Ranges not growing with data | Convert to Table (`Ctrl+T`) so refs auto-extend |
| Comparing dates as text | Parse with `DATEVALUE`/`TEXT` first |
| Circular reference in interest calc | Enable iterative calc knowingly, or restructure |

Pros also **audit before they trust**: `Ctrl+[` to trace precedents, `F9` to evaluate a selected formula chunk, and a `SUM` cross-check at the bottom of every reconciliation.

## Learn-it roadmap & resources

Realistic time to interview-ready fluency: **6–8 weeks** at 1 hr/day if you already know finance concepts.

- **Weeks 1–2:** Lookups, SUMIFS/COUNTIFS, Tables, keyboard shortcuts. Rebuild a real bank statement into a summary.
- **Weeks 3–4:** Text cleanup, dates, IFERROR, PivotTables. Do the GSTR-2B reco above with your own data.
- **Weeks 5–6:** Finance functions (NPV/IRR/PMT), then Power Query + one SQL `GROUP BY`.
- **Weeks 7–8:** Basic Python/pandas for big files, and DAX if the role touches Power BI.

Resources: **ExcelJet** (free formula reference), **Chandoo.org** (dashboards), **Microsoft Learn** (Power Query + DAX, free), **Mode SQL Tutorial** (free), **Corporate Finance Institute (CFI)** — paid but recognised for FMVA. Certifications worth the line on a resume: **Microsoft Office Specialist: Excel Expert**, **CFI FMVA**, **Google/DataCamp SQL** for BI-leaning roles.

## Quick-reference

**Top keyboard shortcuts**

| Shortcut | Action |
|---|---|
| `Ctrl+Shift+↓/→` | Select to end of data |
| `Alt+=` | AutoSum |
| `Ctrl+T` | Convert range to Table |
| `F4` | Toggle `$` / repeat last action |
| `Ctrl+;` | Insert today's date |
| `Ctrl+Shift+L` | Toggle filters |
| `Ctrl+D` / `Ctrl+R` | Fill down / right |
| `Alt+H+O+I` | Autofit column width |
| `F2` | Edit cell / `F9` evaluate selection |
| `Ctrl+[` | Trace precedents |
| `Ctrl+PgUp/PgDn` | Move between sheets |
| `Ctrl+Shift+V` | Paste Special (values) |

**Top formulas**

| Need | Formula |
|---|---|
| Lookup | `=XLOOKUP(k, ids, vals, "NA")` |
| 2-key lookup | `=XLOOKUP(1,(a=x)*(b=y),vals)` |
| Conditional sum | `=SUMIFS(amt, reg,"West", mth,">="&d)` |
| Count | `=COUNTIFS(rng,">90")` |
| Clean text | `=TRIM(CLEAN(A2))` |
| ₹text→number | `=VALUE(SUBSTITUTE(A2,"₹",""))` |
| Month-end | `=EOMONTH(A2,0)` |
| EMI | `=PMT(r/12,n,-P)` |
| Irregular NPV/IRR | `=XNPV(r,cf,dt)` / `=XIRR(cf,dt)` |
| No errors in deck | `=IFERROR(x,"check")` |

**SQL skeleton:** `SELECT dim, SUM(x) FROM t WHERE d>='2026-04-01' GROUP BY dim ORDER BY 2 DESC LIMIT 5;`

**pandas skeleton:** `df.pivot_table(index="region", values="amt", aggfunc="sum", margins=True)`
