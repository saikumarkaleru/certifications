# Theory vs the job: what accounting roles actually do

## What it is & where it's used

An accounting job is not "posting debits and credits." It is *operating a system of record* — usually an ERP (TallyPrime, SAP, Oracle NetSuite, Zoho Books, Microsoft Dynamics) — under deadlines, so that money moves correctly, taxes are filed on time, and management can trust the numbers. The theory you learned (double-entry, AS/Ind AS, ratio analysis) is the *grammar*. The job is *writing paragraphs* in that grammar every day, fast, without errors, and reconciling when it breaks.

Three roles you will actually target, and what they own:

| Role | Owns day-to-day | ERP touchpoints | Typical India CTC (0-4 yrs) |
|---|---|---|---|
| **Accounts Executive / Accountant** | Booking invoices, bank entries, GST/TDS data, vendor payments, ledger scrutiny | Tally/Zoho voucher entry, GST portal, bank statements | ₹3-6 LPA |
| **Assistant Manager (AM) – Finance** | Month-end close, reconciliations, MIS, GST returns, review of juniors' entries | SAP FICO / NetSuite, Excel MIS, GSTN, TRACES | ₹8-16 LPA |
| **Controller / Finance Manager** | Books integrity, statutory audit, board MIS, controls, cash-flow, ERP process design | Full ERP + BI (Power BI), consolidation | ₹18-40 LPA+ |

Every one of these lives inside a **close calendar** (the monthly rhythm of shutting the books) and a **compliance calendar** (GSTR-1 by the 11th, GSTR-3B by the 20th, TDS payment by the 7th). Miss those and the job goes wrong regardless of how well you know accounting standards.

## The gap: why companies want this (and college didn't teach it)

Your MBA/CA syllabus optimized for *exam answers*: "define materiality," "compute the current ratio," "pass the rectification entry." Employers optimize for *throughput and reliability*. The gap is specific:

| College taught | The job needs |
|---|---|
| Prepare a Trial Balance from given balances | *Extract* the TB from Tally/SAP, spot the ₹ that doesn't tie, and fix it before close |
| The GST concept (input credit, output tax) | File GSTR-3B on the portal, reconcile GSTR-2B vs purchase register, claim exactly the eligible ITC |
| Journal entries in a neat notebook | 400 vendor invoices booked with correct TDS section, HSN, cost centre, and GL code |
| "Reconciliation is comparing two statements" | A 3-way bank rec at month-end where ₹18,750 is stuck and you must find *which* entry |
| Ratios from a printed balance sheet | Build a self-refreshing MIS in Excel/Power BI that the CFO reads on the 3rd |

Nobody in college made you close books against a clock, chase a mismatched paise, or defend an ITC number to an auditor. That is the entire gap — and it is closeable in weeks, not years, because it is *procedural* skill, not new theory.

## What "proficient" looks like

The concrete bar an interviewer or a 3-month probation tests for. A job-ready person can, **unaided**:

- Book any voucher in Tally/ERP with the correct ledger, tax, TDS section, and cost centre — and know *why* each leg hits that account.
- Reconcile a bank statement to the books and explain every open item (uncleared cheque, bank charge, direct debit).
- Pull a GSTR-2B, match it against the purchase register in Excel, and produce a clean "eligible ITC" figure with a reason for every mismatch.
- Do a month-end close: accruals, prepaid amortization, depreciation, provisions, and hand over a tied-out TB.
- Build an MIS in Excel using `SUMIFS`, `XLOOKUP`, and a PivotTable that updates when you paste new data.
- Read a GL and answer "why is the telephone expense up 40% this month?" in five minutes.

If you can do those six things without asking anyone, you are worth ₹6-10 LPA in India today.

## Hands-on: how to actually do it

**1. The entries that are 80% of the job.** Real Dr/Cr, India context.

Purchase of raw material ₹1,00,000 + 18% GST from a registered vendor:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases A/c | 1,00,000 | |
| Input CGST A/c | 9,000 | |
| Input SGST A/c | 9,000 | |
| To Vendor (Sundry Creditor) | | 1,18,000 |

Professional fees ₹50,000 to a consultant, TDS u/s 194J @ 10%:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Professional Fees A/c | 50,000 | |
| To TDS Payable (194J) | | 5,000 |
| To Consultant (Creditor) | | 45,000 |

Month-end prepaid insurance (₹24,000 paid for the year, book 1 month):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Insurance Expense A/c | 2,000 | |
| To Prepaid Insurance A/c | | 2,000 |

**2. TallyPrime click-path (voucher entry).**
`Gateway of Tally → Vouchers → F9 (Purchase)` → set *Party A/c name* → select *Purchase ledger* → *GST ledgers auto-populate from the ledger's tax setup* → enter qty/rate → `Ctrl+A` to save. For TDS, the expense ledger must have *"Is TDS applicable = Yes"* and the correct *Nature of Payment* set, so Tally deducts automatically.

**3. GST portal path (GSTR-3B).**
`gst.gov.in → Login → Returns Dashboard → select period → GSTR-3B → Prepare Online` → fill 3.1 (outward tax), 4 (eligible ITC from 2B) → `Save` → `Proceed to Payment` → create challan (PMT-06) → `File with DSC/EVC`.

**4. The reconciliation in Excel.** Match purchase register to GSTR-2B on invoice number + GSTIN:

```excel
=XLOOKUP(A2&B2, GSTR2B!$A:$A & GSTR2B!$B:$B, GSTR2B!$D:$D, "NOT IN 2B")
```

Flag tax mismatches:

```excel
=IF(ABS(C2-VLOOKUP(A2,GSTR2B!$A:$D,4,0))>1,"MISMATCH","OK")
```

Sum eligible ITC by GST rate:

```excel
=SUMIFS(ITC_Amount, Rate, 18, Status, "OK")
```

**5. SQL, when the data lives in a database (NetSuite/SAP export, or a startup on Postgres).** Ledger movement for one account:

```sql
SELECT gl_account, SUM(debit) - SUM(credit) AS net_movement
FROM journal_lines
WHERE posting_date BETWEEN '2026-06-01' AND '2026-06-30'
  AND gl_account = '5100-Telephone'
GROUP BY gl_account;
```

Top 10 vendors by spend this quarter:

```sql
SELECT vendor_name, SUM(amount) AS total_spend
FROM ap_invoices
WHERE invoice_date >= '2026-04-01'
GROUP BY vendor_name
ORDER BY total_spend DESC
LIMIT 10;
```

**6. Python for the reconciliation nobody wants to do by hand:**

```python
import pandas as pd
books = pd.read_excel("purchase_register.xlsx")
portal = pd.read_excel("gstr2b.xlsx")
merged = books.merge(portal, on="invoice_no", how="outer",
                     suffixes=("_books", "_2b"), indicator=True)
only_books = merged[merged["_merge"] == "left_only"]   # ITC claimed but not in 2B → risk
only_2b    = merged[merged["_merge"] == "right_only"]   # in 2B but not booked → missed ITC
print(only_books[["invoice_no", "tax_books"]])
```

**7. Power BI / DAX measure for MIS:**

```dax
Gross Margin % =
DIVIDE(
    SUM(Sales[Revenue]) - SUM(Sales[COGS]),
    SUM(Sales[Revenue])
)
```

## Worked example / mini-project

**Close June 2026 books for "Kaveri Traders Pvt Ltd" and produce the MIS.** Reproduce this in Excel + Tally.

Given for June: Sales ₹42,00,000; Purchases ₹28,00,000; Salaries ₹6,00,000 (TDS 192 ₹40,000); Rent ₹1,50,000 (TDS 194I 10% = ₹15,000); Insurance ₹24,000 paid 1 Apr for 12 months; Machinery ₹12,00,000 (dep @ 15% WDV, book 1 month).

**Step 1 — Accruals & adjustments.**

| Entry | Dr (₹) | Cr (₹) |
|---|---|---|
| Insurance Expense / To Prepaid | 2,000 | 2,000 |
| Depreciation / To Acc. Depreciation (12,00,000×15%÷12) | 15,000 | 15,000 |
| Rent / To TDS 194I / To Landlord | 1,50,000 | 15,000 + 1,35,000 |

**Step 2 — Provisional P&L (MIS):**

| Line | ₹ |
|---|---|
| Revenue | 42,00,000 |
| Less: Purchases (COGS) | 28,00,000 |
| **Gross Profit** | **14,00,000** |
| Salaries | 6,00,000 |
| Rent | 1,50,000 |
| Insurance | 2,000 |
| Depreciation | 15,000 |
| **Net Profit** | **6,33,000** |

**Step 3 — Compliance figures to file:** GST output (say 18%) ₹7,56,000; ITC from purchases ₹5,04,000; net GST payable ₹2,52,000 (GSTR-3B by 20 Jul). TDS payable = 40,000 + 15,000 = ₹55,000 (deposit by 7 Jul, challan 281).

**Step 4 — MIS one-liner in Excel** (from a transactions sheet):

```excel
=SUMIFS(Amount, Type, "Revenue", Month, "Jun") - SUMIFS(Amount, Type, "Expense", Month, "Jun")
```

Deliverable: a tied-out TB, a P&L that a manager reads in 30 seconds, and two compliance numbers ready to file. *That* is a month-end close.

## How it's tested

**Interview questions (verbal):**
- "Walk me through the entry for a purchase with GST and TDS." (They watch whether you know TDS is on the base, not on GST.)
- "GSTR-2B shows ₹5 lakh ITC, your books show ₹5.4 lakh. What do you do?"
- "What's the difference between provision and accrual? Give a real example."
- "Bank balance per books is ₹2,00,000, per statement ₹1,85,000. Reconcile."

**Practical assessments (this is what filters people):**
- **Timed Excel test (30-45 min):** given a raw transaction dump, build a PivotTable, write `SUMIFS`/`XLOOKUP`, and produce a summary. No internet.
- **"Close these books" case:** a messy trial balance with 5 missing adjustments; find and pass them.
- **Reconciliation screen:** two files (bank statement + ledger), identify every unmatched line.
- **SQL screen (for FinTech/analyst roles):** join AP invoices to payments, find unpaid > 60 days.
- **Tally live test:** book 10 vouchers correctly with tax and cost centres in front of them.

## Common mistakes & how pros avoid them

| Mistake | Why it happens | How pros avoid it |
|---|---|---|
| Deducting TDS on the GST-inclusive amount | Confusing base vs total | TDS is always on the *taxable value*, not GST |
| Claiming full ITC without checking 2B | Trusting the invoice | Reconcile 2B *before* filing 3B, every month |
| Hard-coding numbers in the MIS | Speed under pressure | Formulas + references only; never type a total |
| Forgetting reversing entries for accruals | Not thinking about next month | Pass accrual + auto-reverse on the 1st |
| `VLOOKUP` breaking on inserted columns | Column-index fragility | Use `XLOOKUP`/`INDEX-MATCH` |
| Posting to the wrong cost centre / GL | Autopilot | Ledger scrutiny before close; review top 10 variances |
| Round-off / paise mismatches ignored | "It's only ₹2" | Reconcile to zero; ₹2 today is ₹2 lakh mislabeled tomorrow |

## Learn-it roadmap & resources

Realistic time-to-proficiency from an MBA/CA-Inter base: **6-10 weeks of deliberate practice.**

| Week | Focus | Resource |
|---|---|---|
| 1-2 | Tally end-to-end + real vouchers | TallyPrime (free 7-day licence), Tally Education, YouTube: FinTaxPro |
| 2-3 | GST returns + reconciliation | GST portal sandbox, ICAI GST material, ClearTax blogs |
| 3-4 | TDS, month-end close, accruals | TRACES portal, ICAI practical guides |
| 4-6 | Excel for finance | Excel: `SUMIFS/XLOOKUP/INDEX-MATCH`, PivotTables — Chandoo.org, Corporate Finance Institute (CFI) |
| 6-8 | Power BI / SQL for MIS | Microsoft Learn (free), Mode SQL tutorial, DataCamp |
| 8-10 | ERP exposure | SAP FICO fundamentals (openSAP free), NetSuite/Zoho trial |

**Certifications worth listing:** CFI's *Financial Modeling & Valuation Analyst (FMVA)*, Microsoft PL-300 (Power BI), TallyPrime certification, and — highest signal in India — your CA articleship/CA Inter itself. Pair one tool cert with demonstrable practice files.

## Quick-reference

| Item | Value / formula |
|---|---|
| GSTR-1 due | 11th of next month |
| GSTR-3B due | 20th of next month |
| TDS deposit due | 7th of next month |
| TDS 194J (professional) | 10% |
| TDS 194I (rent, plant/machinery / land-building) | 2% / 10% |
| TDS 194C (contractor, non-individual) | 2% |
| TDS 192 (salary) | slab-based |
| Standard GST slabs | 0 / 5 / 12 / 18 / 28% |
| Match invoice to 2B | `=XLOOKUP(inv&gstin, 2B!inv&gstin, 2B!tax, "NOT IN 2B")` |
| Conditional sum | `=SUMIFS(sum_range, crit_range, criteria)` |
| Net GST payable | Output tax − Eligible ITC |
| Depreciation (WDV, monthly) | `Opening WDV × rate ÷ 12` |
| Bank rec identity | Book bal ± uncleared items = Bank bal |
| Ledger movement (SQL) | `SUM(debit) - SUM(credit) GROUP BY account` |
| Gross Margin % (DAX) | `DIVIDE(Revenue - COGS, Revenue)` |

**The one line to remember:** the exam rewarded *knowing* the entry; the job rewards *booking 400 of them correctly, reconciling to zero, and filing on time.* Close that gap and you are job-ready.
