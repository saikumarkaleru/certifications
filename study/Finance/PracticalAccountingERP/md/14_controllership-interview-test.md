# The accounting/controllership interview & practical test

## What it is & where it's used

Every accounts, finance, tax, audit and controllership role in India ends with two filters: a **structured interview** (technical + situational) and a **practical test** — a timed hands-on assessment where you actually pass entries, build a reconciliation, or "close the books" on a mock trial balance. This is standard at Big 4 (Deloitte, PwC, EY, KPMG), captive GCCs (JPMorgan, Amazon, Genpact, Accenture), mid-market CFO teams, and startups hiring an R2R (Record-to-Report), AP/AR, or GL accountant.

The interview tests whether you *understand* debit-credit logic, accruals, and month-end. The practical test verifies you can *execute* it in Excel and Tally/SAP under time pressure. Roles that hit this: GL Accountant, R2R Analyst, AP/AR Executive, Financial Analyst, Assistant Manager–Finance, Tax Associate, and Audit Associate.

## The gap: why companies want this (and college didn't teach it)

An MBA or CA-Inter teaches you *why* a provision is created and how AS/Ind AS classifies it. It rarely makes you sit down and **book 40 entries against a bank statement in 45 minutes** or explain why a suspense account won't clear. Colleges grade theory papers; employers pay for a clean, tied-out trial balance by Working Day 3 (WD+3).

The specific gaps this chapter closes:

- **Speed + accuracy on entries** — knowing the entry vs. keying it correctly with the right sign, ledger, and cost centre.
- **Reconciliation muscle** — bank recon, GSTR-2B vs. books, AP/AR sub-ledger vs. GL, intercompany.
- **Month-end sequencing** — you can't accrue before you cut off; you can't close before recons pass.
- **Explaining the "why"** — interviewers probe *"why did you debit that?"* College never made you defend an entry out loud.

## What "proficient" looks like

A job-ready candidate can, unaided:

1. Pass any routine entry (accrual, prepaid, depreciation, provision, forex, TDS, GST) with correct Dr/Cr, narration, and cost centre.
2. Build a **bank reconciliation** from a statement + cashbook and explain every reconciling item.
3. Reconcile **GSTR-2B to purchase register** and quantify ITC to claim/hold.
4. Take an **unadjusted trial balance → post adjusting entries → produce an adjusted TB → P&L and Balance Sheet** that balances.
5. Explain the **month-end close calendar** (WD-2 to WD+5) and what happens each day.
6. Answer *"accruals vs. provisions,"* *"deferred revenue,"* *"why does depreciation hit P&L but not cash"* crisply.

## Hands-on: how to actually do it

### The entries they will ask you to pass

| Scenario | Journal Entry (Dr / Cr) |
|---|---|
| Accrue Dec electricity bill Rs.50,000 not yet received | Dr Electricity Expense 50,000 / Cr Outstanding Expenses (Accrued Liab) 50,000 |
| Prepaid insurance Rs.1,20,000 for 12 months, book monthly | On payment: Dr Prepaid Insurance 1,20,000 / Cr Bank 1,20,000. Monthly: Dr Insurance Exp 10,000 / Cr Prepaid Insurance 10,000 |
| Depreciation on machinery (WDV) Rs.80,000 | Dr Depreciation 80,000 / Cr Accumulated Depreciation 80,000 |
| Provision for doubtful debts Rs.25,000 | Dr Bad Debt Provision (P&L) 25,000 / Cr Provision for Doubtful Debts 25,000 |
| Salary Rs.5,00,000, TDS u/s 192 Rs.40,000, PF Rs.30,000 | Dr Salaries 5,00,000 / Cr TDS Payable 40,000 / Cr PF Payable 30,000 / Cr Salary Payable 4,30,000 |
| Purchase Rs.1,00,000 + 18% GST from registered vendor | Dr Purchases 1,00,000 / Dr Input CGST 9,000 / Dr Input SGST 9,000 / Cr Vendor 1,18,000 |
| Vendor invoice, TDS 194J @10% on Rs.1,00,000 | Dr Professional Fees 1,00,000 / Cr TDS Payable 10,000 / Cr Vendor 90,000 |
| Deferred revenue: received Rs.1,20,000 annual SaaS upfront | On receipt: Dr Bank 1,20,000 / Cr Deferred Revenue 1,20,000. Monthly: Dr Deferred Revenue 10,000 / Cr Revenue 10,000 |
| Forex payable USD 10,000 @ 83 booked, settled @ 85 | Dr Import Purchase 8,30,000 / Cr Vendor 8,30,000. On settlement: Dr Vendor 8,30,000 / Dr Forex Loss 20,000 / Cr Bank 8,50,000 |

Golden rule to recite: **Debit what comes in / expenses & assets; Credit what goes out / income & liabilities.** Modern form: *assets & expenses increase on debit; liabilities, equity & income increase on credit.*

### Bank reconciliation in Excel

Match cashbook to bank statement. Flag unmatched items:

```excel
=IF(COUNTIFS(Bank[Amt],[@Amt],Bank[Date],[@Date])>0,"Matched","Open")
```

Reconciliation math:

```
Balance as per Cashbook               1,00,000
Add: Cheques issued not yet presented   +15,000
Less: Cheques deposited not yet cleared  -8,000
Less: Bank charges not in books          -1,200
Add: Interest credited not in books      +2,000
= Balance as per Bank Statement        1,07,800
```

### GSTR-2B vs. purchase register (ITC reconciliation)

```excel
Books ITC per invoice   :  =SUMIFS(PR[GST],PR[GSTIN],[@GSTIN],PR[Inv],[@Inv])
2B ITC per invoice      :  =SUMIFS(GSTR2B[GST],GSTR2B[GSTIN],[@GSTIN],GSTR2B[Inv],[@Inv])
Status                  :  =IF(ROUND(Books-2B,0)=0,"OK",IF(Books>2B,"Not in 2B - HOLD ITC","Vendor billed extra"))
```

Only ITC appearing in 2B is claimable — books-only invoices get held.

### Post adjusting entries to a trial balance with SQL

```sql
-- Adjusted trial balance from a journal_lines table
SELECT a.account_name,
       SUM(jl.debit)  AS total_dr,
       SUM(jl.credit) AS total_cr,
       SUM(jl.debit - jl.credit) AS net
FROM journal_lines jl
JOIN accounts a ON a.id = jl.account_id
WHERE jl.period = '2026-03'
GROUP BY a.account_name
ORDER BY a.account_name;

-- Sanity check: total debits MUST equal total credits
SELECT SUM(debit) AS dr, SUM(credit) AS cr,
       SUM(debit) - SUM(credit) AS diff
FROM journal_lines WHERE period = '2026-03';   -- diff must be 0
```

### Tally / GST portal click-paths

- **Pass a journal in TallyPrime:** Gateway of Tally → Vouchers → press **F7** (Journal) → Dr ledger → amount → Cr ledger → amount → narration → **Ctrl+A** to save.
- **Bank recon in Tally:** Banking → Bank Reconciliation → select bank ledger → enter "Bank Date" against each voucher → unreconciled balance shows at bottom.
- **Download GSTR-2B:** gst.gov.in → login → Returns Dashboard → select period → **GSTR-2B** → Download (Excel).

## Worked example / mini-project — "Close these books" (Rs.)

You get this unadjusted trial balance for **Meghna Traders Pvt Ltd, March 2026**:

| Ledger | Dr | Cr |
|---|---|---|
| Cash & Bank | 4,50,000 | |
| Debtors | 6,00,000 | |
| Machinery | 10,00,000 | |
| Purchases | 25,00,000 | |
| Salaries | 8,00,000 | |
| Sales | | 42,00,000 |
| Creditors | | 5,50,000 |
| Share Capital | | 8,00,000 |
| Rent | 1,50,000 | |
| **Total** | **55,50,000** | **55,50,000** |

**Adjustments to book (WD+2):**

1. Depreciation @10% on machinery → Dr Depreciation 1,00,000 / Cr Accum. Dep 1,00,000
2. Salary for March Rs.72,000 unpaid → Dr Salaries 72,000 / Cr Salary Payable 72,000
3. Rent Rs.30,000 prepaid (Apr) → Dr Prepaid Rent 30,000 / Cr Rent 30,000
4. Provision for doubtful debts @2% of debtors → Dr Bad Debt Prov 12,000 / Cr Provision 12,000

**Adjusted P&L:**

| Item | Rs. |
|---|---|
| Sales | 42,00,000 |
| Less: Purchases | (25,00,000) |
| Less: Salaries (8,00,000+72,000) | (8,72,000) |
| Less: Rent (1,50,000−30,000) | (1,20,000) |
| Less: Depreciation | (1,00,000) |
| Less: Bad debt provision | (12,000) |
| **Net Profit** | **5,96,000** |

**Balance Sheet ties:** Equity 8,00,000 + Profit 5,96,000 = 13,96,000; Liabilities = Creditors 5,50,000 + Salary Payable 72,000 + Provision 12,000 + Accum Dep 1,00,000. Assets = Bank 4,50,000 + Debtors 6,00,000 + Machinery 10,00,000 + Prepaid Rent 30,000. **Both sides = 20,80,000.** Books closed.

## How it's tested

**Interview questions (rapid-fire):**
- Difference between accrual and provision? (Accrual = known amount, incurred; provision = estimated liability.)
- Deferred revenue — asset or liability, and why? (Liability — you owe service.)
- Why does depreciation reduce profit but not cash? (Non-cash allocation of past capex.)
- Three golden rules / modern accounting equation.
- What is a contra entry? A suspense account? Why would a TB not tie?
- Walk me through your month-end close.
- Prepaid vs. outstanding expense — where does each sit on the balance sheet?

**Practical assessments companies actually give:**
- **Timed Excel test (30–45 min):** given a bank statement + cashbook, build the BRR; or given raw data, use SUMIFS/VLOOKUP/pivot to produce a summary.
- **"Pass these entries":** 8–12 scenarios on paper or in Tally, graded on Dr/Cr, amount, and narration.
- **"Close these books" case** (like the worked example above): unadjusted TB + adjustments → adjusted TB + financials.
- **Recon screen:** GSTR-2B vs. purchase register or AP sub-ledger vs. GL; quantify and explain the gap.
- **SQL/BI screen** (GCC/analyst roles): write a GROUP BY to produce a TB or aging.

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Reversing Dr/Cr on accruals/provisions | Say the entry aloud: "expense up = debit; liability up = credit." |
| Forgetting the reversal in next period | Book accruals as auto-reversing (JV type in ERP). |
| Claiming full ITC ignoring 2B | Claim only 2B-matched ITC; park the rest in "ITC on hold." |
| TB doesn't tie, chasing randomly | Diff ÷ 2 = a wrong-sign posting; diff ÷ 9 = transposition. |
| Netting TDS wrong on vendor payment | TDS credited to *payable*, not netted into expense. |
| No narration / no cost centre | Every entry needs a narration + dimension; auditors reject blanks. |
| Closing before recons pass | Recons are a *gate*, not a *report* — fix breaks first. |

## Learn-it roadmap & resources

| Phase | Time | Focus |
|---|---|---|
| 1 | 1 week | Drill 50 journal entries until reflexive; recite golden rules. |
| 2 | 1 week | Bank recon + GST recon in Excel (SUMIFS, XLOOKUP, pivots). |
| 3 | 1 week | Full close cycle: unadjusted TB → adjustments → financials. |
| 4 | Ongoing | Mock interviews; explain every entry out loud. |

**Resources:** ICAI Accounting/Cost study material (free); TallyPrime education mode (free); GST portal help section; Zoho Books / QuickBooks free trials for close practice; ExcelJet for lookup/SUMIFS; NISM & ICAI for credibility. Certifications that signal readiness: **CA Inter**, **Tally Certification**, Microsoft **Excel Associate (MO-201)**, and any GCC-run R2R bootcamp.

Time to practical proficiency: **3–4 focused weeks** if you already know the theory — the bottleneck is speed, not concepts.

## Quick-reference

| Item | Rule / Formula |
|---|---|
| Modern rule | Assets & Expenses ↑ = Dr; Liab, Equity & Income ↑ = Cr |
| Accrual entry | Dr Expense / Cr Outstanding Liability |
| Prepaid entry | Dr Prepaid Asset / Cr Bank; then Dr Expense / Cr Prepaid |
| Deferred revenue | Dr Bank / Cr Deferred Rev; then Dr Deferred Rev / Cr Revenue |
| Depreciation | Dr Depreciation / Cr Accumulated Depreciation |
| GST purchase | Dr Purchase + Dr Input CGST + Dr Input SGST / Cr Vendor |
| TDS on payment | Dr Expense / Cr TDS Payable / Cr Vendor (net) |
| BRR direction | Cashbook + unpresented cheques − uncleared deposits ± bank items = Bank |
| TB won't tie | Diff÷2 = sign error; Diff÷9 = transposition |
| ITC test | Claim only GSTR-2B-matched invoices |
| Close calendar | WD-2 cutoff → WD+1 accruals → WD+2 recons → WD+3 TB → WD+5 report |
| Tally journal | F7 → Dr / Cr → narration → Ctrl+A |
| Adjusted TB (SQL) | `SELECT account, SUM(debit-credit) GROUP BY account` (diff must be 0) |
