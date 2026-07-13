# The education-vs-industry gap, quantified

## What it is & where it's used

An MBA (or B.Com, or CA Intermediate) certifies that you *understand* finance. A payroll certifies that you can *produce* finance work — a reconciled ledger, a filed GST return, a working three-statement model, a clean variance report — by a deadline, unsupervised, in the tools the company already runs.

Those are different products. The gap between them is what this whole book is about. It shows up in every finance/accounts/tax seat you might target:

| Role | What college trained | What the job actually measures |
|---|---|---|
| Accounts Payable / AR executive | Journal-entry theory, accounting standards | Speed of 3-way match, Tally/ERP entry accuracy, vendor recon |
| GST / Tax associate | Sections of the CGST Act | Filing GSTR-1/3B on the portal, ITC reconciliation (2B vs books) |
| FP&A / Finance analyst | NPV, IRR formulas | Excel modelling, variance decks, pulling actuals from an ERP |
| Data-heavy finance / MIS | Ratio analysis | SQL to extract, Power BI/DAX to present, Python to automate |
| Audit associate | Auditing standards | Sampling in Excel, tick-and-tie, documenting workpapers |

Every one of these is a *doing* skill layered on top of the theory you already have. Employers do not pay for the theory. They pay for the output.

## The gap: why companies want this (and college didn't teach it)

College is optimised for a written exam graded on *conceptual correctness*. Industry is optimised for *repeatable, auditable output under a deadline*. Five concrete gaps result:

1. **Tools.** No MBA syllabus makes you fast in Excel, Tally, SAP, the GST portal, SQL, or Power BI. Firms assume you already are. You are not.
2. **Speed & unaided delivery.** Exams give you 3 hours and a clean question. Jobs give you a messy export, a 5 pm deadline, and no answer key. The bar is "get it right the first time without asking."
3. **Data plumbing.** Real numbers live in ERPs and CSV dumps, not in a textbook table. Nobody taught you `VLOOKUP`/`XLOOKUP`, pivot tables, or a `JOIN`. A ₹40-crore reconciliation is a lookup problem, not a theory problem.
4. **Documentation & audit trail.** "Show your working" in an exam is worth marks; in a job it is a legal and audit requirement. You must leave a trail a reviewer can follow.
5. **Communication.** A 40-mark essay is never asked for. A one-slide "here's why margin dropped 180 bps" is asked for constantly.

The punchline: **"what you can do" beats the degree** because the degree is a *filter* (it gets your CV read) while demonstrable skill is the *decision*. Two candidates with the same MBA are separated entirely by who can open Excel and build the model live.

## What "proficient" looks like

The concrete, unaided bar an employer tests for:

- Open a raw ERP/bank CSV and reconcile it to the books in **under 30 minutes** with `XLOOKUP` + a pivot, flagging every mismatch.
- Build a **3-statement model** where the balance sheet balances and a single driver (sales growth) flows through all three statements without hardcoding.
- File **GSTR-3B** on the portal and reconcile **ITC in books vs GSTR-2B**, explaining every difference.
- Write a **SQL query** with a `JOIN` and `GROUP BY` to answer "revenue by region by month" from a transactions table.
- Pass **journal entries** for accruals, prepaid, depreciation and a GST invoice — with correct Dr/Cr — cold.
- Turn a 50,000-row export into a **Power BI / pivot dashboard** with a YoY-growth measure.

If you can do these unaided, you are ahead of most fresh MBAs and many experienced hires.

## Hands-on: how to actually do it

**Excel — the reconciliation lookup (replace VLOOKUP forever):**

```excel
=XLOOKUP(A2, Bank[Ref], Bank[Amount], "NOT IN BANK", 0)
```

Then flag mismatches vs the books:

```excel
=IF(ROUND(BookAmt - XLOOKUP(A2,Bank[Ref],Bank[Amount],0),2)=0,"OK","CHECK")
```

Aggregate for a quick summary without a pivot:

```excel
=SUMIFS(Ledger[Amount], Ledger[Region], "South", Ledger[Month], "Apr")
```

**SQL — revenue by region by month from a transactions table:**

```sql
SELECT region,
       DATE_FORMAT(txn_date,'%Y-%m') AS month,
       SUM(amount)                   AS revenue
FROM   sales_txns
WHERE  txn_date >= '2025-04-01'
GROUP  BY region, DATE_FORMAT(txn_date,'%Y-%m')
ORDER  BY region, month;
```

ITC-style reconciliation as a `LEFT JOIN` (books vs portal):

```sql
SELECT b.invoice_no, b.itc AS books_itc, g.itc AS portal_itc,
       (b.itc - COALESCE(g.itc,0)) AS diff
FROM   books_itc b
LEFT   JOIN gstr2b g ON b.invoice_no = g.invoice_no
WHERE  b.itc <> COALESCE(g.itc,0);
```

**Python — automate a monthly reconciliation (pandas):**

```python
import pandas as pd

books = pd.read_excel("books.xlsx")
bank  = pd.read_csv("bank_statement.csv")

merged = books.merge(bank, on="ref", how="outer",
                     suffixes=("_book", "_bank"), indicator=True)
merged["diff"] = merged["amount_book"].fillna(0) - merged["amount_bank"].fillna(0)

unmatched = merged[(merged["_merge"] != "both") | (merged["diff"].abs() > 0.01)]
unmatched.to_excel("exceptions.xlsx", index=False)
print(f"{len(unmatched)} exceptions of {len(merged)} rows")
```

**DAX — a YoY growth measure in Power BI:**

```dax
Revenue YoY % =
VAR ThisYr = [Total Revenue]
VAR LastYr = CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, YEAR))
RETURN DIVIDE(ThisYr - LastYr, LastYr)
```

**TallyPrime — record a purchase with GST (click-path):**
`Gateway of Tally → Vouchers → F9 (Purchase) → select Party → select Purchase ledger → pick Stock item → Tally auto-computes CGST/SGST from the GST ledgers → Ctrl+A to save.`

**GST portal — file GSTR-3B:**
`www.gst.gov.in → Login → Services → Returns → Returns Dashboard → select period → GSTR-3B "Prepare Online" → fill 3.1 outward tax & 4 eligible ITC → Save → Proceed to Payment → offset liability → File with EVC/DSC.`

**Journal entries — the ones you'll pass cold:**

| Transaction | Dr | Cr | Amount (₹) |
|---|---|---|---|
| Purchase of goods with GST (18%) | Purchases 1,00,000 / Input CGST 9,000 / Input SGST 9,000 | To Creditor | 1,18,000 |
| Salary accrued, unpaid | Salary Expense | To Salary Payable | 2,50,000 |
| Prepaid insurance (paid) | Prepaid Insurance | To Bank | 60,000 |
| Monthly depreciation | Depreciation | To Accumulated Depreciation | 12,500 |

## Worked example / mini-project

**Reproduce this in one sitting.** You run accounts for a small trading firm. April sales ledger has 6 invoices; the bank shows 5 receipts.

| Invoice | Book amount (₹) | Bank receipt (₹) |
|---|---|---|
| INV-001 | 1,18,000 | 1,18,000 |
| INV-002 | 2,36,000 | 2,36,000 |
| INV-003 | 59,000 | 59,000 |
| INV-004 | 94,400 | — |
| INV-005 | 1,77,000 | 1,77,000 |
| INV-006 | 47,200 | 47,200 |

Step 1 — put invoices in column A, book amounts in B, bank data in a `Bank` table. In C2:

```excel
=XLOOKUP(A2, Bank[Inv], Bank[Amt], "NOT RECEIVED", 0)
```

Step 2 — status in D2:

```excel
=IF(C2="NOT RECEIVED","OUTSTANDING",IF(ROUND(B2-C2,2)=0,"OK","DIFF"))
```

Step 3 — totals: `=SUM(B2:B7)` gives billed **₹7,31,600**; `=SUMIF(D2:D7,"OK",B2:B7)` gives collected **₹6,37,200**. Outstanding = **₹94,400** (INV-004).

Step 4 — the finance answer: collection efficiency = `=6,37,200/7,31,600` = **87.1%**, one debtor (INV-004) is unpaid. You just did in five minutes what a "reconciliation" job title exists to do all month. Extend it: 500 invoices, same two formulas, and INV-004's GST of ₹14,400 is stuck ITC you'd chase in GSTR-2B.

## How it's tested

Companies almost never test theory alone. Expect:

- **Timed Excel test (30-45 min):** given a raw CSV, "reconcile these two sheets and give me collection % and the exceptions list." Lookups, `SUMIFS`, a pivot, and IF-logic. Speed is scored.
- **SQL screen:** "write a query for top-5 customers by revenue this quarter." (`GROUP BY … ORDER BY … LIMIT 5`.)
- **Case / "close the books":** a trial balance with 8 adjustments — pass the entries, produce P&L and balance sheet.
- **Modelling round (FP&A):** build or extend a 3-statement or DCF model live; they watch your cell logic.
- **Interview questions:** "Walk me through the three statements and how they link." / "What's the entry for accrued expense?" / "How would you reconcile ITC?" / "Depreciation rises ₹100 — what happens to cash?" (Answer: net income down by 100×(1−tax), cash *up* by the tax shield since depreciation is non-cash.)

## Common mistakes & how pros avoid them

- **`VLOOKUP` with approximate match** silently returns wrong numbers. Pros use `XLOOKUP`, or `VLOOKUP(...,FALSE)` at minimum.
- **Hardcoding numbers into model formulas.** A pro drives everything from a labelled assumptions block so one input change flows everywhere.
- **A balance sheet that doesn't balance** and "plugging" it. Pros build a `Assets − (Liab+Equity)` check cell that must read zero.
- **Reconciling on amount alone.** Two invoices of ₹59,000 net to zero difference but are the wrong match. Pros key on a unique ID (invoice/ref no.).
- **No audit trail.** Pros leave source, formula, and date so a reviewer reproduces the number without asking.
- **Filing GSTR-3B before reconciling 2B.** Over-claimed ITC gets reversed with interest. Pros reconcile books-vs-2B first.
- **Float comparison** (`=` on decimals). Wrap in `ROUND(...,2)` — always.

## Learn-it roadmap & resources

Realistic time-to-proficiency, part-time, from an MBA/CA-Inter base:

| Skill | To job-ready | Resource |
|---|---|---|
| Excel (lookups, pivots, IF) | 3-4 weeks | ExcelJet, Chandoo.org (free); Microsoft Excel docs |
| Financial modelling | 6-8 weeks | CFI FMVA (paid), Breaking Into Wall Street; Aswath Damodaran (free, YouTube) |
| SQL | 3-4 weeks | SQLBolt, Mode SQL Tutorial (free); LeetCode DB |
| Power BI + DAX | 4-6 weeks | Microsoft Learn (free); SQLBI.com for DAX |
| Python (pandas) | 4-6 weeks | Kaggle "Pandas" micro-course (free) |
| Tally + GST | 3-4 weeks | Tally Education (TallyPrime), CBIC GST portal help |

Certifications that actually move a CV: **Microsoft Office Specialist – Excel**, **CFI FMVA**, **Tally Certification (TallyPrime)**, **Microsoft PL-300 (Power BI)**. Sequence for an India accounts/tax role: Excel → Tally+GST → SQL/Power BI. For FP&A/analyst: Excel → modelling → SQL. Build a public portfolio (one reconciliation, one model, one dashboard) — it beats any certificate in the interview.

## Quick-reference

| Need | Use |
|---|---|
| Look up a value | `=XLOOKUP(key, lookup_col, return_col, "NA", 0)` |
| Conditional sum | `=SUMIFS(sum, crit_rng1, c1, crit_rng2, c2)` |
| Match check | `=IF(ROUND(a-b,2)=0,"OK","CHECK")` |
| SQL group | `SELECT dim, SUM(x) FROM t GROUP BY dim ORDER BY 2 DESC` |
| SQL reconcile | `LEFT JOIN … WHERE a.v <> COALESCE(b.v,0)` |
| Pandas reconcile | `df1.merge(df2, on="key", how="outer", indicator=True)` |
| YoY in DAX | `DIVIDE([X]-CALCULATE([X],DATEADD(Date,-1,YEAR)), …)` |
| GST purchase entry | Dr Purchases + Dr Input CGST/SGST → Cr Creditor |
| Accrual entry | Dr Expense → Cr Payable |
| GST rate (standard) | 18% = 9% CGST + 9% SGST (intra-state) |
| Balance check | `Assets − (Liabilities + Equity) = 0` |
| Golden rule | Debit what comes in / expenses; Credit what goes out / income |
