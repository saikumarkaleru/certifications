# Working with Auditors

## What it is & where it's used

Every company of any size gets audited. In India a statutory audit under the Companies Act, 2013 is mandatory for **every** company (private, public, one-person) regardless of turnover. On top of that a **tax audit** under Section 44AB of the Income-tax Act kicks in when business turnover crosses ₹1 crore (₹10 crore if cash receipts and payments are each ≤ 5%) or professional receipts cross ₹50 lakh. Add GST audit/reconciliation (GSTR-9C), internal audit, and — for listed or PE-backed firms — quarterly limited reviews and often a US-GAAP/IFRS group audit.

"Working with auditors" is the recurring job of the person who owns the books: the **accountant, finance executive, financial controller, or FP&A analyst**. You are the auditor's counterparty. You hand over the trial balance, build the supporting schedules, answer queries, produce documents from the **PBC list** (Prepared By Client), and defend your numbers. Do it well and the audit closes in three weeks with a clean report. Do it badly and it drags for three months, throws up adjustments that dent your P&L, and burns your reputation with management. This is a career skill that quietly separates a "junior who does entries" from a "controller who runs the close."

## The gap: why companies want this (and college didn't teach it)

Your B.Com/MBA taught you *audit theory from the auditor's chair* — sampling, materiality, SA 500, assertions, the audit risk model. What no classroom teaches is the **auditee's craft**: how to keep books that survive scrutiny, how to build a schedule that ties to the GL to the paisa, how to respond to a query without opening ten new ones, and how to project-manage a team of CAs who are sitting in your office asking for the 47th document.

Employers feel this gap acutely because audit season is expensive. A messy auditee means overtime, delayed financials, delayed board meetings, and delayed loan renewals (banks want audited statements). When a hiring manager asks *"Have you handled audits?"* they mean: can you produce a fixed-asset register that reconciles to the GL, explain a variance without panicking, and close the audit on schedule? That skill is learned only by doing — which is exactly why it commands a premium.

## What "proficient" looks like

A job-ready person can, unaided:

- Produce a **clean trial balance** that ties to the GL, with no suspense balances and no "misc" dumping grounds.
- Build every schedule on the standard PBC list from the accounting system, each **reconciling to the TB line** to zero.
- Anticipate the **common audit queries** and keep the backup ready *before* it's asked.
- Draft a **lead schedule** (a one-page summary per FS caption that rolls up to the number in the financial statements).
- Handle the **BRS, GST reconciliation (GSTR-1 vs 3B vs books), TDS reconciliation (26AS vs books), and inter-company reconciliation**.
- Respond to a query in writing with the entry, the document, and the rationale — closing it, not extending it.
- Run the audit as a **project**: a PBC tracker, a query log, and a status call cadence.

## Hands-on: how to actually do it

### 1. Build an audit-ready trial balance

Export the TB from Tally/ERP, then sanity-check it. Two rules: **debits = credits**, and **no orphan/suspense balances**.

```excel
' TB balances?
=SUM(D2:D500)-SUM(E2:E500)          ' Dr total minus Cr total → must be 0

' Flag suspense / clearing accounts that should be nil at year-end
=IF(AND(ISNUMBER(SEARCH("suspense",A2)),ABS(F2)>0),"CLEAR ME","")
```

### 2. The lead schedule (ties GL → FS)

For each financial-statement line, a lead schedule groups the underlying ledgers. Use `SUMIFS` against your TB dump so it auto-ties:

```excel
' Trade Receivables lead = sum of all ledgers mapped to "Debtors"
=SUMIFS(TB[ClosingBal], TB[FSGroup], "Trade Receivables")

' Tie-out check against the balance sheet figure
=ROUND(SUMIFS(TB[ClosingBal],TB[FSGroup],"Trade Receivables")-BS_TradeReceivables,0)  ' must be 0
```

### 3. Debtors ageing (the #1 requested schedule)

```excel
' Bucket each invoice by days outstanding from invoice date
=LOOKUP((TODAY()-[@InvoiceDate]),{0,31,61,91,181},{"0-30","31-60","61-90","91-180",">180"})
```

If your data is in SQL, generate the ageing straight from the ledger:

```sql
SELECT customer,
       SUM(CASE WHEN dso <=30 THEN amount ELSE 0 END) AS "0-30",
       SUM(CASE WHEN dso BETWEEN 31 AND 90 THEN amount ELSE 0 END) AS "31-90",
       SUM(CASE WHEN dso BETWEEN 91 AND 180 THEN amount ELSE 0 END) AS "91-180",
       SUM(CASE WHEN dso > 180 THEN amount ELSE 0 END) AS ">180"
FROM (SELECT customer, amount,
             DATEDIFF(CURRENT_DATE, invoice_date) AS dso
      FROM ar_open_items) t
GROUP BY customer
ORDER BY 5 DESC;
```

### 4. Bank reconciliation (auditors always vouch this)

```python
import pandas as pd
books = pd.read_csv("bank_ledger.csv")     # your GL bank ledger
stmt  = pd.read_csv("bank_statement.csv")   # bank's statement

# Un-reconciled: entries in books not matched by (date, amount) in the statement
merged = books.merge(stmt, on=["value_date","amount"], how="left", indicator=True)
unpresented = merged[merged["_merge"]=="left_only"]      # cheques issued, not cleared
print("Book balance     :", books.amount.sum())
print("Un-reconciled amt:", unpresented.amount.sum())
```

### 5. GST reconciliation (GSTR-1 vs 3B vs books)

On the GST portal: **Login → Returns Dashboard → select FY → GSTR-9 → Download GSTR-1/3B summary (PDF/Excel)**. Then in Excel:

```excel
' Difference between books' output tax and GSTR-3B tax paid — should be ~0
=Books_OutputGST - GSTR3B_TaxPaid
```

### 6. TDS reconciliation (26AS / AIS vs books)

Download Form 26AS from the income-tax portal (**Login → e-File → Income Tax Returns → View Form 26AS → TRACES**). Match TDS credited per 26AS to TDS receivable in books; the delta usually means a customer deducted but didn't file, or a timing mismatch.

### 7. A typical audit adjustment (JV) you'll pass

When the auditor finds an unrecorded expense (say, ₹1,20,000 audit fee not provided for):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Legal & Professional Charges (P&L) | 1,20,000 | |
| Provision for Audit Fees (Current Liab.) | | 1,20,000 |

*Narration: Being provision for FY 2025-26 statutory audit fee not recorded, adjustment per audit.*

## Worked example / mini-project

**Scenario:** You're the accountant at *Nimbus Traders Pvt Ltd*, FY 2025-26. Turnover ₹8.4 crore. The statutory auditor's team arrives Monday. Build the audit file.

**Step 1 — TB and lead schedules.** Export the TB. It shows Trade Receivables ₹92,40,000. Your debtors ageing (built with the `SUMIFS`/`LOOKUP` above) sums to ₹92,40,000 — **it ties**. Good. The `>180 days` bucket is ₹6,10,000 across two customers.

**Step 2 — Anticipate the query.** The auditor will ask *"Is provision for doubtful debts needed on the ₹6.1 lakh?"* One customer (₹4,10,000) paid ₹4,00,000 in April 2026 — attach the bank credit as **subsequent-receipt evidence**, no provision needed. The other (₹2,00,000) is disputed — you provide 100%.

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Provision for Doubtful Debts (P&L) | 2,00,000 | |
| Allowance for Doubtful Debts (contra-asset) | | 2,00,000 |

**Step 3 — Bank & GST.** BRS shows ₹35,000 of unpresented cheques — documented. GSTR-3B tax paid = ₹14,90,000; books output GST = ₹15,02,000. Delta ₹12,000 → a March sales invoice was booked but reported in the April return. Note it in the reco; no adjustment needed (timing).

**Step 4 — Fixed assets.** FAR shows additions of ₹4,50,000 (a machine). Depreciation per Schedule II (WDV, useful life 15 yrs) for 9 months = you compute and tie to the depreciation ledger.

**Step 5 — Deliverable.** A single workbook: `Nimbus_Audit_FY26.xlsx` with tabs — *TB, Lead Schedules, Debtors Ageing, Creditors Ageing, BRS, GST Reco, TDS Reco, FAR, Query Log*. Every schedule footer ties to the FS to zero. That workbook *is* the difference between a 2-week and a 2-month audit.

## How it's tested

**Interview questions:**
- "Walk me through how you prepare for a statutory audit." (They want: PBC list → schedules → tie-outs → query handling.)
- "What is a PBC list? Name 8 items on it."
- "How do you reconcile GSTR-1, GSTR-3B and books? What causes differences?"
- "A customer is 200 days overdue but paid after year-end. Do you provide for it?" (No — subsequent receipt is audit evidence.)
- "What's the entry for an unrecorded expense the auditor finds?"
- "Difference between statutory audit, tax audit, and internal audit?"

**Practical/assessment tests:**
- A **timed Excel case**: given a raw TB dump and a ledger extract, build a debtors ageing and a lead schedule that ties — in 45 minutes.
- A **"here's a messy BRS, reconcile it"** exercise with planted un-presented cheques and a bank charge not in books.
- A **query-response drill**: they hand you five auditor queries and grade whether your written answers *close* them (entry + document + rationale) or invite follow-ups.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Schedules don't tie to the TB | Every schedule footer has a `=schedule - TB line` cell that must show 0 before sending. |
| "Suspense" / "misc" ledgers with balances | Clear all suspense to nil before the audit; auditors treat suspense as a red flag. |
| Answering queries verbally | Maintain a **written query log**: query, response, document ref, status, owner, date. |
| Giving auditors raw system access with no map | Provide a clean export + a "where things are" index; control the narrative. |
| Passing adjustments only in the audit file, not in books | Post every agreed adjustment in the ERP so next year opens clean. |
| Re-doing schedules from scratch each request | Build **formula-driven** schedules off a single TB dump so a re-export refreshes everything. |
| Missing subsequent events | Review April–May bank statements and post-year-end invoices before finalising. |

## Learn-it roadmap & resources

**Time to proficiency:** ~2–3 months of focused effort, or one full audit cycle on the job.

| Week | Focus |
|---|---|
| 1 | TB hygiene, lead schedules, tie-outs in Excel (SUMIFS, ROUND checks) |
| 2 | Debtors/creditors ageing, BRS, FAR + Schedule II depreciation |
| 3 | GST reco (GSTR-1/3B/2B/9C), TDS reco (26AS/AIS), inter-co |
| 4 | Build a full mock audit file end-to-end; run a query-log drill |
| 5–8 | Shadow a real audit; own the PBC tracker |

**Resources:**
- ICAI Standards on Auditing (free PDFs) — read SA 500 (evidence), SA 560 (subsequent events), SA 580 (representations) from the *auditee's* angle.
- GST portal help + GSTR-9C reconciliation format (free, cbic-gst.gov.in).
- TallyPrime "Audit & Compliance" and any ERP's standard schedules export.
- **Certifications:** CA Intermediate (Audit paper) is the gold standard in India; for tooling, an advanced-Excel course pays off fastest.

## Quick-reference

**Standard PBC list (keep these ready):**

| # | Item |
|---|---|
| 1 | Trial balance + general ledger dump |
| 2 | Lead schedules per FS caption |
| 3 | Debtors & creditors ageing |
| 4 | Bank statements + BRS (all accounts) |
| 5 | Fixed-asset register + depreciation working |
| 6 | GST reco (GSTR-1/3B/2B, GSTR-9C) |
| 7 | TDS reco (26AS/AIS vs books) + challans |
| 8 | Inventory listing + valuation basis |
| 9 | Loan statements, sanction letters, interest working |
| 10 | Payroll register, PF/ESI/PT challans |
| 11 | Related-party transactions list |
| 12 | Board/AGM minutes, statutory registers |

**Key thresholds & checks:**

| Item | Value / Rule |
|---|---|
| Tax audit (Sec 44AB) — business | Turnover > ₹1 cr (₹10 cr if cash ≤ 5%) |
| Tax audit — profession | Receipts > ₹50 lakh |
| Statutory audit | All companies, no threshold |
| GSTR-9C reconciliation | Aggregate turnover > ₹5 cr |
| TB tie-out | Dr total − Cr total = 0 |
| Schedule tie-out | `Schedule − FS line = 0` |

**Golden rules:** tie every schedule to zero · clear all suspense · answer queries in writing with entry + document + rationale · post agreed adjustments in the ERP · review subsequent events before sign-off.
