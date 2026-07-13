# The 90-Day Job-Ready Sprint

## What it is & where it's used

This chapter is the operating system for the previous six chapters. It takes the raw skills — Excel modeling, accounting close, GST/TDS compliance, SQL, Python, Power BI/DAX — and sequences them into a **12-week, week-by-week plan** that ends with you being able to sit an interview and a practical test without freezing.

The sprint is designed for the reader who has 2–4 focused hours a day (evenings + weekends around CA classes or a current job). It is used by anyone targeting entry-to-junior roles: **Accounts Executive, Finance Analyst, Audit Associate, FP&A Analyst, Tax Associate, Financial/Data Analyst**. The logic is simple: employers don't pay for what you *know*, they pay for what you can *produce unaided by Friday*. Ninety days is enough to build 3–4 portfolio artifacts that prove exactly that.

## The gap: why companies want this (and college didn't teach it)

An MBA gives you the *vocabulary* (WACC, DCF, contribution margin) and CA gives you the *rules* (Ind AS, GST law). Neither gives you **throughput** — the muscle memory to open a blank workbook and deliver a working model in 90 minutes, or to reconcile a GSTR-2B against your purchase register before a return deadline.

| College teaches | Job requires |
|---|---|
| "Explain a DCF" | Build a 5-year DCF from a P&L in Excel, sensitivity table included |
| "Journal entries in theory" | Close a month in Tally, tie out to a trial balance |
| "GST has 4 slabs" | File GSTR-3B and reconcile ITC from 2B on the portal |
| "SQL is a query language" | Pull revenue by region for last quarter under time pressure |
| Solo exams | Deliver a shared model a manager can audit and trust |

The gap is **speed, accuracy, and format** — turning knowledge into a clean deliverable someone else can rely on. This sprint closes it by forcing daily reps and weekly shippable outputs.

## What "proficient" looks like

The bar at day 90, unaided:

- Build a 3-statement or DCF model in Excel from scratch; no hardcoded numbers inside formulas; every driver on an assumptions tab.
- Perform a bank reconciliation and a month-end close in TallyPrime; produce a trial balance that ties.
- Compute GST liability, reconcile ITC from GSTR-2B, and walk through filing GSTR-3B on the portal.
- Write SELECT queries with JOIN, GROUP BY, and a window function against a real schema.
- Load a CSV in Python/pandas, clean it, and produce a summary; or build a Power BI dashboard with 3–4 DAX measures.
- Talk through each artifact in an interview: what you assumed, why, and what would break it.

## Hands-on: how to actually do it

The sprint is four 3-week blocks. Each block ends with **one portfolio artifact**.

**Block 1 (Wk 1–3): Excel + Accounting core.** The non-negotiable foundation for every finance role.

```
Wk1: Excel mechanics — XLOOKUP, INDEX/MATCH, SUMIFS, IF logic, pivot tables, absolute refs.
Wk2: Accounting close — journal entries, T-accounts, trial balance, BRS, accruals/prepaids.
Wk3: Build a 3-statement model linking P&L → BS → Cash Flow.
```

Core Excel reps to drill until automatic:

```excel
=XLOOKUP(A2, Ledger[Code], Ledger[Name], "Not found")
=SUMIFS(Amount, Region, "West", Month, "Jun")
=INDEX(Rate, MATCH(1, (Item=G2)*(Vendor=H2), 0))   ' Ctrl+Shift+Enter or dynamic array
=IFERROR(Revenue/Prior-1, "n/a")                    ' YoY growth, safe
```

A recurring-revenue driver on the assumptions tab (never type numbers in the P&L):

```excel
Revenue_Y2 = Revenue_Y1 * (1 + Growth_Rate)     ' Growth_Rate lives in cell $B$4
Gross_Profit = Revenue * (1 - COGS_pct)
```

Sales-invoice journal entry (India, 18% GST intra-state):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Debtors / Bank | 1,18,000 | |
| To Sales | | 1,00,000 |
| To Output CGST @9% | | 9,000 |
| To Output SGST @9% | | 9,000 |

**Block 2 (Wk 4–6): Tax & compliance in Tally + GST portal.** Where accounts/tax roles are won.

TallyPrime click-path to record that same sales invoice:
`Gateway of Tally → Vouchers → F8 (Sales) → Party A/c name → select Sales ledger → select stock item → GST auto-computes from ledger rates → Ctrl+A to save.`

GST liability logic you must be able to compute cold:

```
Output GST (on sales)      = 90,000
Less: Input Tax Credit     = 62,000   (from GSTR-2B, only invoices that appear)
Net GST payable in cash    = 28,000   → paid via GSTR-3B, Table 3.1 + 6.1
```

Reconcile ITC in Excel before filing — match purchase register to GSTR-2B:

```excel
=XLOOKUP([@GSTIN&Invoice], TwoB[Key], TwoB[TaxValue], "MISSING in 2B")
```

Any "MISSING in 2B" row = ITC you cannot claim this month. TDS on professional fees (Sec 194J, 10%):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Professional Fees | 50,000 | |
| To TDS Payable (194J) | | 5,000 |
| To Vendor | | 45,000 |

**Block 3 (Wk 7–9): SQL + data.** For analyst-flavored roles.

```sql
-- Revenue by region, last quarter, top to bottom
SELECT region,
       SUM(amount)               AS revenue,
       COUNT(DISTINCT invoice_id) AS invoices
FROM   sales
WHERE  invoice_date >= '2026-04-01' AND invoice_date < '2026-07-01'
GROUP  BY region
ORDER  BY revenue DESC;

-- Running total (window function) — the interview differentiator
SELECT month,
       SUM(revenue) OVER (ORDER BY month) AS cumulative_revenue
FROM   monthly_sales;
```

Python for a quick reconciliation/summary — the reusable pattern:

```python
import pandas as pd
gl = pd.read_csv("general_ledger.csv")
gl["amount"] = pd.to_numeric(gl["amount"], errors="coerce")
summary = (gl.groupby("cost_center")["amount"]
             .sum()
             .sort_values(ascending=False))
print(summary.head(10))
```

**Block 4 (Wk 10–12): Power BI/DAX + packaging.** Turn it into a dashboard and a story.

```dax
Total Revenue = SUM(Sales[Amount])
Revenue YoY % =
VAR Curr = [Total Revenue]
VAR Prior = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(Curr - Prior, Prior)
```

## Worked example / mini-project

**Project: "Kaveri Traders FY25-26 Finance Pack"** — one dataset, carried through all four blocks. Invent a small trading firm: revenue ₹1.2 crore, COGS 65%, opex ₹18 lakh.

1. **Excel model:** Assumptions tab with growth 12%, COGS 65%, tax 25%. Build P&L → BS → Cash Flow. Add a 2-way data table flexing growth (8/12/16%) against COGS (60/65/70%) to see PAT swing. PAT at base ≈ ₹9.75 lakh.
2. **Tally + GST:** Book 12 months of sales/purchase vouchers. Compute net GST: output ₹21.6 lakh − ITC ₹14 lakh = **₹7.6 lakh cash payable**. Reconcile a deliberately-broken 2B (one vendor didn't file) and flag the ₹90,000 ITC you must hold.
3. **SQL/Python:** Load the 12-month sales CSV, GROUP BY region, find that "South" is 41% of revenue but declining QoQ.
4. **Power BI:** One page — revenue trend, region split, GST payable card, YoY% measure.

Ship it as a GitHub repo + a 1-page PDF summary. This *is* your portfolio.

## How it's tested

Companies rarely take your word. Expect:

- **Timed Excel test (30–60 min):** "Here's a raw sales dump — build a pivot, compute margin by product, flag items below 20% margin." Or a lookup/cleanup task. Speed and no-hardcoding matter.
- **SQL screen (HackerRank / live share):** 2–3 queries escalating to a JOIN + window function.
- **"Close these books" case:** given a trial balance with errors, find and fix them; or record 5 vouchers in Tally and produce the TB.
- **GST/tax scenario:** "Sales ₹10L, purchases ₹6L, one supplier hasn't filed — what's your net payable and what do you do about the ITC?"
- **Model walkthrough:** they open your file and ask "why is this cell a formula and that one a constant?" and "what happens if growth halves?"

Interview questions: *Walk me through your DCF. What's the difference between GSTR-2A and 2B? When is ITC blocked (Sec 17(5))? How do you reconcile a bank statement? Explain a LEFT vs INNER JOIN.*

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Hardcoding numbers inside formulas | All inputs on an assumptions tab; formulas reference them |
| Studying 6 skills shallowly, shipping nothing | One artifact per block — depth over breadth |
| Claiming ITC on everything | Claim only what's in GSTR-2B; check Sec 17(5) blocks |
| Circular refs / #REF! left in the model | Trace precedents, wrap risky bits in IFERROR, build clean |
| Memorizing DCF theory but never building one | Build the model 3×; the third time is muscle memory |
| No sensitivity/scenario view | Always add a data table — managers ask "what if" |
| Cramming, no spaced revision | Weekly review of prior blocks so Wk1 skills survive to Wk12 |

## Learn-it roadmap & resources

Realistic time-to-proficiency at ~3 hrs/day: **the 90 days gets you interview-ready for entry/junior roles**, not senior. Extend to 6 months for depth.

| Skill | Free | Paid / cert |
|---|---|---|
| Excel | ExcelJet, Leila Gharani (YouTube) | Microsoft MO-201 |
| Accounting/Tally | Tally Education free courses | TallyPrime + GST certificate |
| GST/TDS | GST portal help, ClearTax guides | ICAI GST certificate course |
| SQL | Mode SQL Tutorial, SQLBolt, HackerRank | Google Data Analytics (Coursera) |
| Python | Kaggle "Pandas" micro-course | — |
| Power BI/DAX | Microsoft Learn (free) | Microsoft PL-300 |

Weekly cadence: 5 days new material, Saturday build the artifact, Sunday spaced review + mock question.

## Quick-reference

```
Block 1 (Wk1-3): Excel + 3-statement model      → Artifact: financial model
Block 2 (Wk4-6): Tally + GST/TDS + portal        → Artifact: closed books + GST recon
Block 3 (Wk7-9): SQL + Python                     → Artifact: query pack + analysis
Block 4 (Wk10-12): Power BI/DAX + packaging       → Artifact: dashboard + repo
```

| Need | Formula / step |
|---|---|
| Lookup | `=XLOOKUP(key, col, return, "NA")` |
| Conditional sum | `=SUMIFS(sum, crit_rng, crit)` |
| YoY | `=IFERROR(this/prior-1,"n/a")` |
| Net GST | Output GST − ITC (in 2B only) |
| TDS 194J | 10% on professional fees |
| SQL group | `SELECT dim, SUM(x) ... GROUP BY dim` |
| Window | `SUM(x) OVER (ORDER BY month)` |
| DAX YoY | `DIVIDE(Curr-Prior, Prior)` |
| Rule | Inputs on assumptions tab, never hardcode |
```
```
