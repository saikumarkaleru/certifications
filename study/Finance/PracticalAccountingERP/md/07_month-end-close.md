# Month-end close: the checklist & journals

## What it is & where it's used

**Month-end close (MEC)** is the disciplined process of finalising a company's books for a period so the numbers can be trusted, reported, and locked. It's the difference between a ledger that *has* transactions and financials that are *complete, accurate, and cut off correctly*. Every accrual, prepaid, provision, depreciation run, reconciliation, and inter-company match happens in a fixed window — typically **Working Day 1 (WD1) to WD5** — ending with a signed-off Trial Balance and a flux (variance) commentary sent to management.

Roles that live and die by the close:

| Role | What they own in the close |
|---|---|
| Accounts Executive / AP-AR | Cut-off, accruals of unbilled expenses, vendor/customer recons |
| GL Accountant / Financial Analyst | Journals, depreciation, provisions, prepaid amortisation, TB |
| Assistant Manager – Finance | Flux analysis, review, sign-off, schedules |
| FP&A | Actual vs budget variance, board pack |
| Statutory/Internal Audit | Tests cut-off, provisions, and the close controls |

In India this maps directly to the monthly cycle around **GSTR-1 (11th), GSTR-3B (20th), TDS payment (7th)**, and quarterly Ind AS/Schedule III reporting. Globally the same skeleton drives US GAAP/IFRS closes on a "5-day close" or "faster close" mandate.

## The gap: why companies want this (and college didn't teach it)

College teaches you to pass a *single* adjusting entry in an exam — "provide depreciation @15% WDV" — with the numbers handed to you. It never teaches the **operational reality**:

- Nobody hands you the numbers. You *derive* the accrual from open POs, GRNs, and a rate card.
- Everything is **time-boxed**. The CFO wants a P&L by WD3, not "whenever it's ready."
- **Cut-off** is a control, not a concept — an invoice dated 30-Sep that hits on 3-Oct must still land in September.
- The books must **tie out**: bank recon, GST 2B vs books, AP sub-ledger to GL control account.
- You must **explain movements** (flux), not just produce them. "Why is repairs up 40% MoM?" is the actual job.

Employers pay for someone who can take a messy set of sub-ledgers and produce a defensible TB *on a deadline, unaided*. That reliability — checklist-driven, self-reviewing — is what an MBA syllabus skips entirely.

## What "proficient" looks like

A job-ready person can, without supervision:

1. Own a **close calendar** and drive owners to hit WD deadlines.
2. Compute and post **accruals, prepaids, provisions, and depreciation** with a supporting schedule for each.
3. Apply **cut-off** correctly across revenue, expenses, and inventory.
4. Reconcile **sub-ledger to GL** (AP, AR, fixed assets, bank) and clear differences.
5. Produce a **flux analysis** with real commentary (drivers, not restated numbers).
6. Deliver a **reusable checklist** with maker/checker sign-off and an audit trail.
7. Reverse accruals cleanly the next period and avoid double-counting.

## Hands-on: how to actually do it

### 1. The close calendar

Build it once, reuse forever. A minimal WD-based calendar:

| WD | Task | Owner |
|---|---|---|
| WD1 | Freeze sub-ledgers (AP/AR/inventory), post cut-off accruals | AP/AR |
| WD1-2 | Bank recon, GST 2B vs books, TDS reconciliation | GL |
| WD2 | Prepaid amortisation, depreciation run, provisions | GL |
| WD3 | Inter-company match, draft TB, first flux | AM |
| WD4 | Review adjustments, finalise schedules | AM |
| WD5 | Lock period, MIS pack + flux commentary to CFO | FP&A |

### 2. The core journals

**Accrual — unbilled expense** (services received in Sep, invoice not in). Say ₹1,80,000 of consultancy, GRN raised, no bill:

| Account | Dr | Cr |
|---|---|---|
| Professional fees (P&L) | 1,80,000 | |
| Accrued expenses (Provision for expenses) | | 1,80,000 |

Reverse on 1-Oct so the actual invoice doesn't double-count:

| Account | Dr | Cr |
|---|---|---|
| Accrued expenses | 1,80,000 | |
| Professional fees | | 1,80,000 |

**Prepaid amortisation** — annual insurance ₹1,20,000 paid 1-Apr, monthly charge:

```
Monthly = 1,20,000 / 12 = 10,000
```

| Account | Dr | Cr |
|---|---|---|
| Insurance expense (P&L) | 10,000 | |
| Prepaid insurance (BS) | | 10,000 |

**Depreciation** — SLM, asset ₹6,00,000, life 5 yrs, no residual:

```
Monthly dep = 6,00,000 / (5*12) = 10,000
```

| Account | Dr | Cr |
|---|---|---|
| Depreciation expense | 10,000 | |
| Accumulated depreciation | | 10,000 |

**Provision — doubtful debts** (Expected Credit Loss, Ind AS 109), 2% on ₹40,00,000 receivables:

| Account | Dr | Cr |
|---|---|---|
| Impairment loss / Bad debt expense | 80,000 | |
| Provision for doubtful debts | | 80,000 |

### 3. Prepaid & accrual schedules in Excel

Auto-compute the monthly prepaid charge and remaining balance:

```
Monthly amort:  =IF(EOMONTH($D2,0)>=E$1, $C2/$B2, 0)
   where C2 = total prepaid, B2 = months, D2 = start date, E$1 = period-end date

Closing balance: =$C2 - SUMPRODUCT(($A$1:E$1>=$D2)*($A$1:E$1<=EOMONTH($D2,$B2-1))*($C2/$B2))
```

Pull the current period's accrual from an open-PO extract:

```
=SUMIFS(GRN[Value], GRN[Billed], "No", GRN[GRN_Date], "<="&EOMONTH(TODAY(),0))
```

### 4. Cut-off test (SQL)

Catch invoices booked in the wrong period — doc date in Sep but posting date in Oct:

```sql
SELECT doc_no, vendor, doc_date, posting_date, amount
FROM ap_invoices
WHERE doc_date  <= '2026-09-30'
  AND posting_date > '2026-09-30'
  AND posting_date <= '2026-10-05';   -- likely September cut-off items
```

### 5. Sub-ledger to GL tie-out (SQL)

```sql
SELECT g.control_balance,
       s.subledger_balance,
       g.control_balance - s.subledger_balance AS difference
FROM (SELECT SUM(amount) control_balance FROM gl WHERE account='AP_CONTROL') g
CROSS JOIN (SELECT SUM(open_amount) subledger_balance FROM ap_open_items) s;
-- difference MUST be 0
```

### 6. Flux analysis (Python)

```python
import pandas as pd
tb = pd.read_excel("TB.xlsx")  # cols: Account, Sep, Aug
tb["MoM_abs"] = tb["Sep"] - tb["Aug"]
tb["MoM_pct"] = (tb["MoM_abs"] / tb["Aug"].replace(0, pd.NA)) * 100
# flag anything moving > 10% AND > 50k for commentary
flux = tb[(tb["MoM_pct"].abs() > 10) & (tb["MoM_abs"].abs() > 50000)]
print(flux.sort_values("MoM_abs", key=abs, ascending=False))
```

### 7. TallyPrime click-path (recurring journals)

`Gateway of Tally > Vouchers > F7 (Journal)` → Dr expense, Cr provision → in the narration tag the reversal. For depreciation, keep an **Accounting Voucher** template and `Ctrl+D` won't help — instead duplicate last month's voucher via `Alt+2` from the Day Book and edit the date. Verify posting under `Display > Trial Balance > F5 (detailed)`.

## Worked example / mini-project

**Scenario:** Close September 2026 for *Meridian Traders Pvt Ltd*. Draft TB shows PBT of ₹12,00,000 before adjustments. Post these:

| # | Adjustment | Basis | Amount |
|---|---|---|---|
| 1 | Electricity accrual (bill due Oct) | Meter reading | ₹45,000 |
| 2 | Prepaid insurance charge | ₹1,20,000 / 12 | ₹10,000 |
| 3 | Depreciation — plant | SLM ₹6,00,000 / 60 | ₹10,000 |
| 4 | Provision — doubtful debts | 2% × ₹40,00,000 | ₹80,000 |
| 5 | Interest accrual on loan | ₹50,00,000 × 9% / 12 | ₹37,500 |

**Impact on PBT:**

```
Adjusted PBT = 12,00,000 - 45,000 - 10,000 - 10,000 - 80,000 - 37,500
             = 10,17,500
```

**Flux commentary (Sep vs Aug), driver-based:**

| Account | Aug | Sep | MoM % | Commentary |
|---|---|---|---|---|
| Power & fuel | 38,000 | 45,000 | +18% | Higher production run + summer load |
| Provision – debtors | 60,000 | 80,000 | +33% | Debtor book grew ₹8L; ECL rate held at 2% |
| Interest cost | 0 | 37,500 | new | New ₹50L WC loan drawn 1-Sep |

Deliverable: signed TB + these five schedules + flux note. On 1-Oct, reverse adjustments #1 and #5 (accruals), keep #2–#4 (they're period charges, not reversing accruals).

## How it's tested

**Interview questions**
- "Walk me through your month-end close, day by day." (Tests you actually did it.)
- "Difference between accrual, provision, and reserve?" (Accrual = known amount, timing gap; provision = estimated liability; reserve = appropriation of profit.)
- "An invoice dated 29-Sep arrives on 4-Oct — which period?" (September; cut-off follows the event, not the receipt.)
- "How do you make sure an accrual isn't double-counted next month?" (Auto-reverse on WD1.)
- "Your AP sub-ledger is ₹2,000 off the control account — what do you do?"

**Practical tests companies give**
- A **timed Excel case**: raw sub-ledger dump → build prepaid & accrual schedules and a corrected TB in 45–60 min.
- A **"close these books" case study**: 8–10 adjustments described in words; you must journalise, produce adjusted P&L, and write 3-line flux.
- A **SQL/data screen** for analyst roles: write the cut-off and tie-out queries above.
- A **reconciliation drill**: bank statement vs cash book, find and classify the differences.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Forgetting to reverse accruals → double expense | Post accruals as **auto-reversing** journals dated WD1 next month |
| Cut-off by invoice-received date, not event date | Apply the "goods/services received" test; run the SQL cut-off query |
| No supporting schedule behind a journal | One journal = one schedule; auditor's first ask |
| Flux that restates numbers ("up because it went up") | Commentary must name a **driver**: volume, rate, one-off, timing |
| Provisions that swing wildly with no policy | Fix a documented rate/methodology (e.g. ECL matrix) and hold it |
| Closing before sub-ledgers tie to GL | Tie-out difference must be **zero** before you lock the period |
| Posting to a period you've already locked | Lock the period in the ERP; late items go to the next open period with a note |
| Depreciation on the wrong pro-rata basis | Confirm policy: full-month, mid-month, or days-based; be consistent |

## Learn-it roadmap & resources

**Time to proficiency:** ~6–8 weeks of deliberate practice if you already know debits/credits.

| Week | Focus |
|---|---|
| 1–2 | Journals cold: accrual, prepaid, provision, depreciation, and their reversals |
| 3 | Cut-off + reconciliations (bank, AP/AR, GST 2B vs books) |
| 4 | Build a close calendar + reusable checklist in Excel |
| 5 | Flux analysis — write real commentary on 3 months of dummy TBs |
| 6–8 | Run a full mock close end-to-end, timed, in Tally + Excel |

**Resources**
- *ICAI* Ind AS material — provisions (Ind AS 37), ECL (Ind AS 109), PP&E (Ind AS 16).
- TallyPrime free trial — practise recurring journals and the Day Book workflow.
- Corporate Finance Institute (CFI) — free "Month-End Close" and financial-accounting lessons.
- CPA/ACCA record-to-report (R2R) notes for the globally-portable framing.
- Practice data: generate a dummy sub-ledger in Excel and close it three months running.

**Certifications that signal this:** CA Intermediate (Accounting + Advanced Accounting), ACCA FA/FR, or any employer's internal R2R certification. For BPO/GCC "record-to-report" roles, the close checklist *is* the job description.

## Quick-reference

**Reversing vs non-reversing**
- Reverse next period: accruals (unbilled expense, interest, salary accrual).
- Do NOT reverse: prepaid amortisation, depreciation, provisions (they're period charges/estimates).

**Standard journals (Dr / Cr)**

| Entry | Dr | Cr |
|---|---|---|
| Accrual | Expense | Accrued liabilities |
| Prepaid charge | Expense | Prepaid asset |
| Depreciation | Depreciation exp | Accumulated dep |
| Provision (ECL) | Impairment loss | Provision |
| Interest accrual | Interest exp | Interest payable |

**Key formulas**
```
Monthly prepaid = Total / No. of months
Monthly SLM dep = (Cost - Residual) / (Life in years * 12)
WDV dep        = Opening WDV * rate / 12
MoM flux %     = (Current - Prior) / Prior * 100
Tie-out diff   = GL control - Sub-ledger  (must = 0)
```

**Close discipline**
- Freeze sub-ledgers → post adjustments → tie out → flux → lock.
- One journal = one schedule = one owner.
- Cut-off follows the **event date**, not the receipt date.
- Flux commentary names a **driver**, never restates the number.
