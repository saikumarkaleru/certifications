# Month-End Close: Accruals, Prepaids, Depreciation, Provisions

## The situation

It's the morning of **1-May-2026**. This just landed on your desk: the Financial Controller of **Nirvana Traders & Services Pvt Ltd (NTSPL)** drops a sticky note on your monitor — *"April books close today. Lock the month by 5 PM. I want a clean trial balance, all adjusting entries passed, and depreciation split by block. GST 3B and payroll are already booked — you only owe me the period-end adjustments."*

April is the first month of FY 2026-27. The day-to-day vouchers (sales, purchases, bank, payroll journal, the GSTR-3B set-off entry) are already in TallyPrime. What is **not** yet in the books is the batch of **period-end adjusting entries** — the things that don't come from an invoice but from the *matching principle*: expenses incurred but not yet billed, payments made in advance, the wear-and-tear on assets, and provisions for known liabilities. That's the month-end close, and it's yours.

## What you're given

The Controller's close pack for April 2026:

| # | Item | Amount (Rs) | Note |
|---|------|------------:|------|
| 1 | Electricity consumed Apr, bill not yet received | 40,000 | Accrue; bill expected ~10-May |
| 2 | Statutory audit fee (annual) — accrue 1/12 | 25,000 | Provision, TDS 194J on payment |
| 3 | Insurance premium paid 1-Apr for full year | 60,000 | Prepaid; Rs 5,000/month expense |
| 4 | Depreciation for April (WDV, 1/12 of annual) | 1,20,000 | Split by block below |
| 5 | Closing stock 30-Apr-2026 | 45,00,000 | Physical count valued at lower of cost/NRV |

**Fixed-asset register — WDV blocks (opening 1-Apr-2026):**

| Block | Rate (FY2026-27) | Opening WDV (Rs) | Annual dep (Rs) | April dep = annual/12 (Rs) |
|-------|-----------------:|-----------------:|----------------:|---------------------------:|
| Computers & servers | 40% | 12,00,000 | 4,80,000 | 40,000 |
| Plant & machinery (tools/test rigs) | 15% | 48,00,000 | 7,20,000 | 60,000 |
| Furniture & fixtures | 10% | 24,00,000 | 2,40,000 | 20,000 |
| **Total** | | **84,00,000** | **14,40,000** | **1,20,000** |

The Rs 14,40,000 annual figure is the P&L depreciation anchor for FY2026-27; we book 1/12 each month so the monthly MIS is not lumpy.

**Pre-adjustment balances (relevant extract, after day-books, before close):**

```
Electricity expense (Apr paid so far) .... 0
Insurance (prepaid, sitting in expense) .. 60,000  Dr
Audit fee expense ........................ 0
Accumulated depreciation ................. as per FAR
Opening stock (1-Apr) .................... 42,00,000 Dr (in P&L via opening)
```

## Do it — step by step

TallyPrime path for every adjusting entry: **Gateway of Tally → Vouchers → F7 (Journal)**. Set the voucher date to **30-Apr-2026**. Below are the five journals, each to the rupee.

**JV-1 — Accrue electricity (expense incurred, bill not received):**

```
Dr  Electricity Expenses .......... 40,000
    Cr  Outstanding Expenses (Electricity) .... 40,000
(Being April electricity consumed, invoice awaited — accrual)
```

**JV-2 — Provide 1/12 of annual audit fee:**

```
Dr  Audit Fee Expense ............. 25,000
    Cr  Provision for Audit Fee ............ 25,000
(Being monthly provision toward FY2026-27 statutory audit fee)
```
Note: no TDS at provision if payee/amount not crystallised for payment; TDS u/s 194J (10%, FY2026-27) is deducted when the fee is credited to the auditor's account or paid.

**JV-3 — Amortise prepaid insurance (release 1 month):**

The full Rs 60,000 was booked when paid on 1-Apr. Reclassify the unexpired 11 months to an asset and keep only April's Rs 5,000 in expense.

```
Dr  Prepaid Insurance (Current Asset) .... 55,000
    Cr  Insurance Expense .................... 55,000
(Being 11 months' unexpired premium carried forward; Apr expense = 5,000)
```
Result: Insurance Expense net = 60,000 − 55,000 = **5,000** (April charge); Prepaid Insurance asset = **55,000**.

**JV-4 — Depreciation for April by block:**

```
Dr  Depreciation — Computers & servers .... 40,000
Dr  Depreciation — Plant & machinery ...... 60,000
Dr  Depreciation — Furniture & fixtures ... 20,000
    Cr  Accumulated Depreciation ............... 1,20,000
(Being WDV depreciation for April, 1/12 of FY2026-27 annual charge)
```

**JV-5 — Closing stock (30-Apr-2026):**

In TallyPrime with integrated inventory, stock flows from the item masters; where stock is accounted manually, pass the closing-stock entry so the P&L reflects cost of goods sold correctly:

```
Dr  Closing Stock (Balance Sheet — Current Asset) .... 45,00,000
    Cr  Closing Stock (P&L — credit side) ................ 45,00,000
(Being physical stock at 30-Apr valued at lower of cost/NRV, Rs 45,00,000)
```
COGS logic for the month: Opening 42,00,000 + Purchases (net) − Closing 45,00,000. The rising stock (42L → 45L) tells you April purchases outran April sales of inventory — worth a line in the MIS.

**Close checklist (tick before locking):**

| ✔ | Step |
|---|------|
| ☐ | Bank reconciliation (HDFC xxxx4567) done; closing balance matches statement |
| ☐ | GSTR-3B set-off entry posted; net cash Rs 5,22,000 paid; ITC deferral of Rs 7,200 noted |
| ☐ | Payroll journal posted; EPF/ESI/PT/TDS-192 payables carried to next month |
| ☐ | All 5 adjusting JVs (accruals, provision, prepaid, depreciation, stock) posted at 30-Apr |
| ☐ | Depreciation reconciles to FAR (block-wise) |
| ☐ | Suspense / round-off cleared to nil |
| ☐ | Trial balance tallies (Dr = Cr) |
| ☐ | Draft P&L + Balance Sheet reviewed; freeze period in Tally (Security → Change period) |

## The deliverable

**Adjusting entries summary (April 2026):**

| JV | Debit | Credit | Amount (Rs) |
|----|-------|--------|------------:|
| 1 | Electricity Exp | Outstanding Exp | 40,000 |
| 2 | Audit Fee Exp | Provision for Audit Fee | 25,000 |
| 3 | Prepaid Insurance | Insurance Exp | 55,000 |
| 4 | Depreciation (3 blocks) | Accumulated Dep | 1,20,000 |
| 5 | Closing Stock (BS) | Closing Stock (P&L) | 45,00,000 |

**Post-close trial balance — extract of adjusted lines (30-Apr-2026):**

| Ledger | Debit (Rs) | Credit (Rs) |
|--------|-----------:|------------:|
| Depreciation — Computers | 40,000 | |
| Depreciation — P&M | 60,000 | |
| Depreciation — Furniture | 20,000 | |
| Electricity Expenses | 40,000 | |
| Audit Fee Expense | 25,000 | |
| Insurance Expense (net) | 5,000 | |
| Prepaid Insurance (CA) | 55,000 | |
| Closing Stock (CA) | 45,00,000 | |
| Accumulated Depreciation | | 1,20,000 |
| Outstanding Expenses | | 40,000 |
| Provision for Audit Fee | | 25,000 |
| Closing Stock (P&L, credit) | | 45,00,000 |

Every debit above has its matching credit; the adjusting block is internally balanced (Rs 46,90,000 each side).

## How it's checked

- **Trial balance tallies:** total debits = total credits. If not, a one-sided or wrong-side JV exists — Tally won't let you save an unbalanced journal, so a mismatch means a *classification* error (asset booked as expense), caught in review, not by Tally.
- **Depreciation ties to the FAR:** the three P&L depreciation lines (40k + 60k + 20k) must equal accumulated-depreciation movement (1,20,000) and each block must reconcile to opening WDV × rate ÷ 12.
- **Prepaid runs to zero over the year:** Rs 55,000 opening prepaid ÷ 11 remaining months = Rs 5,000/month; by 31-Mar-2027 prepaid insurance = nil. The reviewer scans the schedule.
- **Accruals reverse or settle:** the Rs 40,000 outstanding electricity must be knocked off when the actual bill arrives in May — no double-counting.
- **Stock cut-off:** closing stock date = 30-Apr; goods received on 1-May must NOT be in April's count, and April sales must have their goods removed.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Leaving full Rs 60,000 insurance in April expense | April profit understated by 55,000 | Pass JV-3 prepaid reclass |
| Depreciating on cost (SLM) when tax/books are WDV | Wrong asset carrying value, tax-audit query | Use block WDV × rate |
| Forgetting to reverse the electricity accrual in May | Double expense, understated May profit | Auto-reverse or manual knock-off |
| Booking audit-fee provision *net of TDS* | TDS 194J deducted twice | Provide gross; deduct TDS at payment/credit |
| Not freezing the period after close | Back-dated entries corrupt filed figures | Lock period in Tally security |

## On the job & in the interview

The month-end close is where the **matching principle** stops being a textbook line and becomes a set of five journals. Accruals and prepaids exist so each month's P&L shows *the cost of running the business that month* — not the cost of whatever invoices happened to arrive. Depreciation is the same idea for capital assets: NTSPL bought test rigs once, but consumes them over years, so 1/12 of the annual WDV charge hits April.

**Q: Difference between a provision and an accrual?**
A: Both are liabilities for costs already incurred, but an *accrual* is a fairly certain amount for goods/services received (electricity consumed — Rs 40,000), while a *provision* is a best estimate where amount or timing is less certain (audit fee Rs 25,000/month toward a year-end bill). Both satisfy matching; provisions carry more estimation judgement under Ind AS 37 / AS 29.

**Q: Company uses WDV — how do you get April's depreciation?**
A: Take each block's opening WDV, apply the block rate (computers 40%, P&M 15%, furniture 10% — FY2026-27), that's the annual charge; divide by 12 for the month. For NTSPL: 4,80,000 + 7,20,000 + 2,40,000 = 14,40,000 annual, so 1,20,000 in April, split 40k/60k/20k. The reviewer ties this to the fixed-asset register.

**Q: Why carry prepaid insurance as an asset?**
A: Because the Rs 55,000 unexpired premium is a future economic benefit NTSPL has already paid for — coverage it will consume over the next 11 months. Expensing it all in April would violate matching and understate April profit; parking it as a current asset and releasing Rs 5,000/month spreads the cost correctly.
