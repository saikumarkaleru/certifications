# Essential functions every analyst must know

## What it is & where it's used

This is the working vocabulary of a finance analyst. Ninety percent of real Excel work in accounts, FP&A, audit, tax, and treasury is **conditional aggregation** (sum/count/average by criteria), **decision logic** (if this then that), **date arithmetic** (interest periods, ageing, GST tax periods, TDS due dates), **text surgery** (cleaning ERP exports, splitting GSTINs, formatting reports), and **error control** (so one bad cell doesn't blow up a model).

Where you'll use each one daily:

| Function group | Real job task |
|---|---|
| SUMIFS / COUNTIFS / AVERAGEIFS | Ledger totals by cost centre, sales by region, avg invoice value by customer |
| IF / IFS / AND / OR | Credit-limit checks, TDS-applicability flags, commission slabs |
| EOMONTH / EDATE / YEARFRAC | GST return periods, EMI schedules, depreciation, receivables ageing |
| LEFT / MID / TEXT / TEXTSPLIT | Splitting GSTIN, cleaning Tally/SAP dumps, building report labels |
| IFERROR | Bulletproofing lookups and divisions in a live model |

Roles that live in these functions: **Accounts Executive, AP/AR analyst, FP&A analyst, Statutory/Internal Audit associate, Tax (Direct + GST) associate, Treasury/MIS analyst, Investment Banking/PE junior.**

## The gap: why companies want this (and college didn't teach it)

An MBA or CA Inter teaches you *what* a variance is, *what* receivables ageing means, and *how* GST periods work — conceptually. It almost never sits you in front of a 40,000-row `.csv` dump from Tally/SAP and says "give me month-wise sales by state, net of returns, by 3 PM." That translation layer — concept to a formula that runs on messy real data — is exactly the paid skill.

The specific gaps employers see in fresh hires:
- They reach for `SUMIF` (single condition) and get stuck the moment there are two conditions. **`SUMIFS` is the real-world default.**
- They nest five `IF`s into an unreadable monster instead of `IFS` or a lookup.
- They subtract dates manually and get ageing buckets wrong across month-ends.
- They retype data instead of using `TEXT`/`TEXTSPLIT` to reshape an export in seconds.
- Their models show `#DIV/0!` and `#N/A` in front of a manager — an instant credibility hit that `IFERROR` prevents.

## What "proficient" looks like

The concrete bar. A job-ready person can, **unaided and in minutes**:

1. Write a multi-condition `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` including a **date range** and a **wildcard** criterion.
2. Replace nested `IF`s with `IFS`, and combine conditions with `AND`/`OR`.
3. Build a **receivables ageing** with `EOMONTH`/`TODAY`/`YEARFRAC` without hardcoding dates.
4. Split a GSTIN or clean a "LASTNAME, Firstname" export using `LEFT`/`MID`/`TEXTSPLIT`.
5. Wrap risky formulas in `IFERROR` so the model never shows a raw error.
6. Explain **why** `SUMIFS` (sum-range first) argument order differs from `SUMIF` (range, criteria, sum-range) — a classic interview trap.

## Hands-on: how to actually do it

Assume a sales table: `A:Date, B:State, C:Customer, D:Product, E:Amount, F:Type` (Sale/Return).

**Conditional aggregation**

```excel
' Total SALE amount for Maharashtra
=SUMIFS(E:E, B:B, "Maharashtra", F:F, "Sale")

' Sales in a date window (Q1 FY26: 1-Apr to 30-Jun-2025)
=SUMIFS(E:E, A:A, ">="&DATE(2025,4,1), A:A, "<="&DATE(2025,6,30))

' Wildcard: all customers whose name starts with "Reliance"
=SUMIFS(E:E, C:C, "Reliance*")

' Count of return invoices; average invoice value for a product
=COUNTIFS(F:F, "Return")
=AVERAGEIFS(E:E, D:D, "Widget-A", F:F, "Sale")
```
Note the order: `SUMIFS(sum_range, criteria_range1, criteria1, …)`. Join operators to a cell with `&`: `A:A, ">="&G1`.

**Decision logic**

```excel
' Simple flag: is TDS applicable? (single-vendor limit Rs 30,000 u/s 194J)
=IF(E2>30000, "Deduct TDS", "No TDS")

' Multi-slab commission with IFS (no nesting)
=IFS(E2>=1000000,"5%", E2>=500000,"3%", E2>=100000,"1%", TRUE,"0%")

' AND / OR
=IF(AND(F2="Sale", E2>500000), "High-value sale", "Normal")
=IF(OR(B2="J&K", B2="Ladakh"), "Special zone", "Regular")
```

**Date functions**

```excel
' GST return period end (last day of invoice month)
=EOMONTH(A2, 0)                 ' 15-May-25  -> 31-May-25

' Credit due date = invoice date + 45 days; or +2 months
=A2+45
=EDATE(A2, 2)                   ' same day, two months later

' EMI / depreciation date one month out
=EDATE(A2, 1)

' Receivables ageing in days and in years
=TODAY()-A2                                   ' days outstanding
=YEARFRAC(A2, TODAY(), 1)                      ' fraction of a year (actual/actual)

' Ageing bucket
=IFS(TODAY()-A2<=30,"0-30", TODAY()-A2<=60,"31-60",
     TODAY()-A2<=90,"61-90", TRUE,"90+")
```

**Text functions** (cleaning exports)

```excel
' GSTIN = 27ABCDE1234F1Z5 in cell H2
=LEFT(H2,2)                     ' 27  -> state code
=MID(H2,3,10)                   ' ABCDE1234F -> PAN embedded in GSTIN
=MID(H2,3,10)                   ' also the PAN for TDS matching

' Split "MUMBAI, Maharashtra" into two cells (Excel 365 / dynamic array)
=TEXTSPLIT(I2, ", ")            ' spills MUMBAI | Maharashtra

' Build a clean label / format a number as text
=TEXT(A2,"mmm-yyyy")            ' May-2025
=TEXT(E2,"#,##0")              ' 12,34,567  (use "[>=10000000]#,##,##,##0" for full Indian grouping)
=D2&" ("&TEXT(E2,"Rs #,##0")&")"   ' Widget-A (Rs 5,00,000)
```

**Error control**

```excel
' Never show #N/A / #DIV/0! to a manager
=IFERROR(VLOOKUP(C2, Master!A:D, 4, FALSE), "Not found")
=IFERROR(E2/G2, 0)             ' safe division -> 0 instead of #DIV/0!
```

## Worked example / mini-project

**Build a one-screen receivables + sales MIS.** Data: a debtors export with `A:Invoice No, B:Customer, C:Invoice Date, D:GSTIN, E:Amount, F:State`. 12 rows, realistic:

| Invoice | Customer | Inv Date | GSTIN | Amount (Rs) | State |
|---|---|---|---|---|---|
| INV001 | Reliance Retail | 05-Feb-2025 | 27AAACR... | 4,50,000 | Maharashtra |
| INV002 | Tata Steel | 20-Mar-2025 | 24AAACT... | 8,20,000 | Gujarat |
| INV003 | Infosys Ltd | 12-May-2025 | 29AAACI... | 2,10,000 | Karnataka |

Now build these output cells (today assumed **03-Jul-2025**):

```excel
' 1. State code from GSTIN (audit check vs State column)
=LEFT(D2,2)                                    ' 27 -> should map to Maharashtra

' 2. Days outstanding + ageing bucket
=TODAY()-C2
=IFS(TODAY()-C2<=30,"0-30", TODAY()-C2<=60,"31-60",
     TODAY()-C2<=90,"61-90", TRUE,"90+")       ' INV001 -> 90+

' 3. Total outstanding over 90 days (the number a CFO asks for first)
=SUMIFS(E:E, C:C, "<"&(TODAY()-90))            ' all invoices older than 90 days

' 4. Sales by state (feeds a state-wise summary)
=SUMIFS($E$2:$E$13, $F$2:$F$13, "Maharashtra")

' 5. Count of overdue accounts + safe average ticket
=COUNTIFS($C$2:$C$13, "<"&(TODAY()-60))
=IFERROR(AVERAGEIFS($E$2:$E$13,$F$2:$F$13,"Gujarat"),0)

' 6. Report label
="Overdue >90d: "&TEXT(SUMIFS(E:E,C:C,"<"&(TODAY()-90)),"Rs #,##,##0")
```

Reproduce it: paste 12 rows, drop these formulas, and you have a live dashboard that recalculates every time you refresh the export. That is a deliverable you can show in a first-week task.

## How it's tested

**Interview questions (verbal):**
- "Difference between `SUMIF` and `SUMIFS`?" (answer: multiple criteria; and the sum-range moves to the *first* argument).
- "How do you sum only rows in a date range?" (criteria with `">="&start` and `"<="&end`).
- "How do you avoid `#N/A` in a lookup?" (`IFERROR` / `IFNA`).
- "Why not just nest `IF`s?" (readability, `IFS`, or a lookup table).

**Practical / assessment tests (the real filter):**
- A **timed 30-45 min Excel test**: a raw sheet + 6-10 tasks — "total sales for South region in Q2", "flag invoices over Rs 1,00,000 needing approval", "extract PAN from GSTIN", "age these receivables". No internet, formulas graded on correctness *and* whether they use absolute refs / dynamic dates.
- A **"clean this export"** task: a `LASTNAME, First` or merged-column dump you must split with `TEXTSPLIT`/`MID`.
- Case rounds in FP&A/IB often hand you a messy CSV and expect a summary table built with `SUMIFS` + a pivot within 20 minutes.

Pass signal: you finish, formulas are robust (no hardcoded dates, wrapped in `IFERROR`), and you can explain each one.

## Common mistakes & how pros avoid them

| Mistake | Fix / pro habit |
|---|---|
| Wrong `SUMIFS` argument order (sum-range last) | Sum-range is **first**; muscle-memory it |
| Hardcoding `"01-04-2025"` as text criteria | Use `">="&DATE(2025,4,1)` — real dates, comparable |
| Full-column refs `E:E` in a huge model → slow | Use fixed ranges `$E$2:$E$50000` in big files |
| Nesting 6 `IF`s | Use `IFS`, or a lookup table with `XLOOKUP` |
| Manual date subtraction across month-end | `EOMONTH`/`EDATE`, never add "30" for a month |
| `LEFT/MID` on inconsistent-length text | Anchor with `FIND`/`SEARCH` or use `TEXTSPLIT` on a delimiter |
| `IFERROR` hiding a *real* bug | Only wrap known-safe risks (div-by-zero, missing lookup), not everything |
| Locking references wrong when dragging | `F4` to toggle `$`; lock criteria ranges, not the criteria cell |

## Learn-it roadmap & resources

**Time to proficiency: 2-3 weeks** of daily practice (1 hr/day) to clear a timed test; ~2 months to be genuinely fast on messy data.

| Week | Focus |
|---|---|
| 1 | `SUMIFS/COUNTIFS/AVERAGEIFS`, absolute refs, date criteria |
| 2 | `IF/IFS/AND/OR`, `EOMONTH/EDATE/YEARFRAC`, ageing project |
| 3 | Text functions on real ERP dumps, `IFERROR`, build the MIS above |

**Resources**
- Free: **ExcelJet** (function reference + examples), **Chandoo.org**, **Corporate Finance Institute (CFI)** free Excel course, Microsoft's own function docs.
- Paid: CFI's **FMVA** certification (Excel-heavy, finance-specific), **Wall Street Prep**, Udemy "Microsoft Excel — Excel from Beginner to Advanced" (Kyle Pew).
- Practice data: export your own Tally/any sample GST invoice register and re-solve the mini-project.
- Certification worth naming on a CV: **Microsoft Office Specialist (MOS) Excel Associate/Expert**, or **FMVA** for finance roles.

## Quick-reference

```excel
' AGGREGATION
=SUMIFS(sum_rng, crit_rng1, crit1, crit_rng2, crit2)
=COUNTIFS(crit_rng1, crit1, ...)
=AVERAGEIFS(avg_rng, crit_rng1, crit1, ...)
=SUMIFS(E:E, A:A, ">="&DATE(2025,4,1), A:A, "<="&DATE(2025,6,30))   ' date window
=SUMIFS(E:E, C:C, "Reliance*")                                      ' wildcard

' LOGIC
=IF(test, if_true, if_false)
=IFS(cond1,val1, cond2,val2, TRUE,default)
=AND(c1,c2)   =OR(c1,c2)

' DATES
=EOMONTH(date, months)     ' last day of month, offset
=EDATE(date, months)       ' same day, months out
=YEARFRAC(start, end, 1)   ' year fraction (basis 1 = actual/actual)
=TODAY()-date              ' days outstanding

' TEXT
=LEFT(txt,n)   =RIGHT(txt,n)   =MID(txt,start,n)
=TEXTSPLIT(txt, ", ")      ' split on delimiter (Excel 365)
=TEXT(value,"mmm-yyyy")    ' or "#,##0" / "Rs #,##,##0"

' ERROR CONTROL
=IFERROR(formula, fallback)
=IFNA(VLOOKUP(...), "Not found")
```

**GSTIN cheat:** `LEFT(gstin,2)` = state code, `MID(gstin,3,10)` = PAN. **Argument order trap:** `SUMIF(range, criteria, sum_range)` but `SUMIFS(sum_range, range, criteria)` — sum-range **moves to front** in the plural version.
