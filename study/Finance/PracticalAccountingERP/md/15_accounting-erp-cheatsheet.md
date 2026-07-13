# Cheat-sheet: entries, close checklist & shortcuts

## What it is & where it's used

This chapter is the laminated card you tape to your monitor. It collects the journal entries you post 50 times a month, the month-end close checklist that stops you forgetting the depreciation run, and the keyboard shortcuts that separate a 4-hour close from a 40-minute one in TallyPrime and SAP.

Every accounts, tax, and FP&A role touches this:

| Role | Uses this for |
|---|---|
| Accounts Payable/Receivable exec | Repeatable vendor/customer entries, TDS, GST |
| GL / R2R accountant | Month-end close, accruals, provisions, reconciliations |
| Tax executive | GST output/input, RCM, TDS entries |
| FP&A analyst | Reading the TB fast, month-over-month checks |
| Startup finance / founder's office | Owning the whole close solo in Tally/Zoho |

The value is speed with accuracy. Nobody promotes the person who *knows* the accrual entry; they promote the one who posts all 40 of them correctly before the 3rd working day.

## The gap: why companies want this (and college didn't teach it)

College teaches you the *logic* of double-entry — "debit the receiver." It never makes you post 200 entries under a deadline, never shows you a real month-end close calendar, and never times you on Tally. The industry gap is muscle memory plus process:

- **Volume & repetition:** Real jobs are the same 25 entry-types, endlessly. You must post them without thinking.
- **The close is a *process*, not an entry:** Books don't just "close" — someone runs a 30-line checklist in a fixed order (accruals before depreciation before tax before TB freeze).
- **Tool fluency:** An MBA never opens Tally. Employers assume you can do `Alt+G > Voucher`, `Ctrl+A` to save, and F-key navigation blind.
- **Statutory muscle:** TDS sections, GST heads (CGST/SGST/IGST), RCM — these are daily entries, not exam theory.

Close this gap and you are useful on day one instead of day ninety.

## What "proficient" looks like

A job-ready person can, unaided:

- Post any of the 25 common entries correctly with the right TDS section / GST head.
- Run a full month-end close against a checklist and produce a clean trial balance.
- Navigate TallyPrime entirely by keyboard, and do basic SAP FI transactions (FB50, F-02, FBL3N).
- Explain *why* an accrual reverses next month and *why* prepaid sits as an asset.
- Spot a suspense-account balance or a mismatched control account and fix it before the manager sees it.

## Hands-on: how to actually do it

### 1. The 25 entries you post constantly

| # | Transaction | Dr | Cr |
|---|---|---|---|
| 1 | Credit purchase of goods | Purchases + Input CGST + Input SGST | Creditor (Vendor) |
| 2 | Credit sale of goods | Debtor (Customer) | Sales + Output CGST + Output SGST |
| 3 | Interstate sale | Debtor | Sales + Output IGST |
| 4 | Payment to vendor | Creditor | Bank |
| 5 | Receipt from customer | Bank | Debtor |
| 6 | Professional fee bill (TDS 194J @10%) | Professional Fees | Vendor; TDS Payable (194J) |
| 7 | Rent paid (TDS 194I @10%) | Rent | Bank; TDS Payable (194I) |
| 8 | Contractor bill (TDS 194C @2%) | Contract Exp | Vendor; TDS Payable (194C) |
| 9 | Salary paid | Salaries | Bank; TDS Payable (192); PF Payable; ESI Payable |
| 10 | Depreciation | Depreciation | Accumulated Depreciation |
| 11 | Expense accrual (month-end) | Expense | Accrued/Outstanding Expenses |
| 12 | Reversal of accrual (next month) | Accrued Expenses | Expense |
| 13 | Prepaid at payment | Prepaid Expense | Bank |
| 14 | Prepaid amortisation | Expense | Prepaid Expense |
| 15 | Provision for doubtful debts | Bad Debt Expense | Provision for Doubtful Debts |
| 16 | Bank charges | Bank Charges | Bank |
| 17 | Interest accrued on FD | Accrued Interest | Interest Income |
| 18 | RCM on freight/GTA | Input IGST (RCM) | RCM Payable |
| 19 | GST payment (setoff) | Output CGST/SGST/IGST | Input GST + Electronic Cash Ledger |
| 20 | TDS deposit | TDS Payable | Bank |
| 21 | Purchase of fixed asset | Fixed Asset + Input GST | Vendor/Bank |
| 22 | Cash withdrawal (contra) | Cash | Bank |
| 23 | Owner capital introduced | Bank | Capital |
| 24 | Forex gain/loss on settlement | Debtor/Bank (loss: Forex Loss) | Forex Gain / Debtor |
| 25 | Year-end P&L transfer | Sales/Income | Trading & P&L |

### 2. TallyPrime keyboard shortcuts (v3.x)

```
Alt+G      Go To (jump to any report/voucher)
F1         Help / switch company
Ctrl+A     Accept & save the current screen (the money shortcut)
Ctrl+Q     Quit without saving
F4         Contra        F5  Payment      F6  Receipt
F7         Journal       F8  Sales        F9  Purchase
Alt+F7     Stock Journal
Ctrl+F9    Debit Note    Ctrl+F8  Credit Note
Alt+C      Create master on the fly (ledger/item)
Alt+D      Delete voucher / line
Alt+X      Cancel voucher
Alt+2      Duplicate a voucher (from Day Book)
Ctrl+Enter Drill into / edit a master mid-entry
Alt+F1     Detailed view in reports
F2         Change period      Alt+F2  Change period range
F12        Configure current screen
D (Gateway)Day Book
```

### 3. SAP FI T-codes you must know

```
FB50    Enter G/L account document (fast entry)
F-02    General posting (with posting keys 40 Dr / 50 Cr)
FB60    Vendor invoice        FB70   Customer invoice
F-53    Outgoing payment      F-28   Incoming payment
FBL1N   Vendor line items     FBL5N  Customer line items
FBL3N   G/L account line items
FS10N   G/L balance display
F.01    Financial statements   S_ALR_87012277  GL balances report
FB08    Reverse a document     F-44   Vendor clearing
```

### 4. The month-end close checklist (order matters)

```
[ ] 1.  Cut-off: all invoices/bills for the month entered
[ ] 2.  Bank reconciliation — every account tied to statement
[ ] 3.  Cash count vs cash ledger
[ ] 4.  AR ageing reviewed; AP ageing reviewed
[ ] 5.  Accruals for unbilled expenses posted
[ ] 6.  Prepaid amortisation for the month posted
[ ] 7.  Depreciation run
[ ] 8.  Inventory valuation / stock reconciliation
[ ] 9.  Inter-company & control account reconciliation
[ ] 10. Provisions (doubtful debts, bonus, gratuity) reviewed
[ ] 11. GST: GSTR-2B vs books input reco; output liability tied out
[ ] 12. TDS: deducted vs payable reconciled, challan ready
[ ] 13. Payroll reconciled (salary, PF, ESI, PT)
[ ] 14. Suspense account = ZERO
[ ] 15. Trial balance drawn; P&L and BS reviewed vs last month
[ ] 16. Variance/flux commentary for FP&A
[ ] 17. Lock/freeze the period
```

## Worked example / mini-project

Reproduce a mini month-end for **Nova Traders Pvt Ltd** (Karnataka), month of June.

**Transactions during June:**

1. Credit sale to a Karnataka customer, ₹1,00,000 + 18% GST.

```
Dr  Debtors — Sharma & Co        1,18,000
    Cr  Sales                        1,00,000
    Cr  Output CGST (9%)                 9,000
    Cr  Output SGST (9%)                 9,000
```

2. Professional fee bill from an auditor ₹50,000, TDS 194J @10%.

```
Dr  Professional Fees             50,000
    Cr  ABC & Associates (net)         45,000
    Cr  TDS Payable — 194J              5,000
```

**Month-end adjustments (close checklist steps 5–7):**

3. Electricity bill for June not yet received, estimated ₹12,000 (accrual):

```
Dr  Electricity Expense           12,000
    Cr  Outstanding Expenses           12,000
```

4. Insurance ₹24,000 paid 1-June for the year → ₹2,000/month amortisation:

```
Dr  Insurance Expense              2,000
    Cr  Prepaid Insurance               2,000
```

5. Depreciation on equipment (WDV ₹6,00,000 @ 15% p.a. = ₹7,500/month):

```
Dr  Depreciation                   7,500
    Cr  Accumulated Depreciation        7,500
```

**GST tie-out (step 11):** Output = ₹18,000. Suppose Input from GSTR-2B = ₹6,300. Net payable in cash = ₹11,700.

```
Dr  Output CGST                    9,000
Dr  Output SGST                    9,000
    Cr  Input CGST/SGST                  6,300
    Cr  Electronic Cash Ledger          11,700
```

**Quick TB sanity check in Excel** — paste ledger balances, then verify it balances:

```
=IF(ROUND(SUM(Debit)-SUM(Credit),2)=0,"BALANCED","OUT BY "&SUM(Debit)-SUM(Credit))
```

Month-over-month flux for FP&A commentary:

```
=IFERROR((Jun-May)/May, "n/a")   ' format as %; flag any line moving >10%
```

In Tally: `Alt+G > Trial Balance > Alt+F1` (detailed) confirms suspense = 0 and totals match.

## How it's tested

Interview questions:

- "Pass the entry for a professional fee bill of ₹50,000 with TDS." (they want section + net vendor amount)
- "What reverses at the start of next month and why?" (accruals)
- "Walk me through your month-end close, in order."
- "CGST vs IGST — when do you charge which?"
- "Where does a prepaid expense sit and why is it an asset?"

Practical assessments companies actually give:

- **Timed Tally test:** "Here are 15 vouchers — enter them in 20 minutes and produce the TB." Graded on speed, correct heads, and a zero suspense.
- **"Close these books" case:** a messy trial balance with missing accruals/depreciation; you must clean it and explain adjustments.
- **Excel screen:** bank reconciliation from two datasets, or a TB that won't balance — find the plug.
- **SAP navigation:** "Post a vendor invoice in FB60 and display it in FBL1N."

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Forgetting to reverse last month's accrual → double-count | Post accrual + reversal as a *pair* immediately; or use auto-reversing journals |
| Wrong GST head (CGST/SGST vs IGST) | Rule: same state = C+S, different state = I. Check place of supply, not billing address |
| Ignoring suspense account balance | Suspense must be ZERO before freezing — it's the first thing a reviewer checks |
| TDS on gross vs net confusion | TDS is on the base amount; vendor gets base − TDS; deposit TDS by the 7th |
| Closing before bank reco | Bank reco is step 2, not optional. Unreconciled = books not closed |
| Editing a posted voucher instead of reversing | In SAP use FB08; keep an audit trail — never silently overwrite |
| Skipping cut-off | An invoice dated 30-June entered in July inflates next month. Enforce a hard cut-off date |

## Learn-it roadmap & resources

**Time to proficiency:** 6–10 weeks of daily practice to be job-ready on entries + close; Tally fluency in ~3 weeks of real use.

| Week | Focus |
|---|---|
| 1–2 | Master the 25 entries cold; drill TDS sections & GST heads |
| 3–4 | TallyPrime end-to-end: masters, vouchers, GST, reports — by keyboard only |
| 5–6 | Run a full mock month-end close against the checklist |
| 7–8 | Bank reco + GSTR-2B reco in Excel; TB troubleshooting |
| 9–10 | SAP FI basics (if targeting large corporates) |

Resources:

- **Tally**: TallyPrime free educational version + Tally Education's official "TallyEssential" certification (paid, recognised in India).
- **GST/TDS**: CBIC and Income-tax portal help sections; ICAI study material (free, you already have it).
- **SAP FI**: free openSAP courses; any SAP FICO end-user PDF for T-code drills.
- **Excel/recons**: practise with a downloaded bank statement + ledger dump.
- **Certifications worth it in India:** TallyEssential/TallyProfessional; add SAP FICO only if targeting MNC ERP roles.

## Quick-reference

**GST rule:** same state → CGST + SGST; different state → IGST. Setoff order: IGST first, then CGST/SGST.

| Statutory | Rate / Section | Due |
|---|---|---|
| TDS Professional | 194J @ 10% | 7th next month |
| TDS Rent (land/bldg) | 194I @ 10% | 7th |
| TDS Contractor | 194C @ 1%/2% | 7th |
| TDS Salary | 192 (slab) | 7th |
| GST return | GSTR-1 / 3B | 11th / 20th |
| PF / ESI | — | 15th |

**Tally survival keys:** `Alt+G` go-to · `Ctrl+A` save · `F5` payment · `F6` receipt · `F7` journal · `F8` sales · `F9` purchase · `Alt+C` create master · `Alt+2` duplicate.

**SAP survival codes:** `FB50` GL post · `FB60` vendor invoice · `FBL3N` GL line items · `FS10N` balance · `FB08` reverse.

**Close order:** cut-off → bank reco → AR/AP → accruals → prepaids → depreciation → inventory → provisions → GST/TDS/payroll → suspense=0 → TB → freeze.

**Excel balance check:** `=IF(ROUND(SUM(Debit)-SUM(Credit),2)=0,"BALANCED","OUT")`
