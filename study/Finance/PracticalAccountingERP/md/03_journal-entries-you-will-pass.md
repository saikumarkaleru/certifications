# Journal entries you will actually pass

## What it is & where it's used

A journal entry is the atom of accounting: for every transaction you record which account to **Debit (Dr)** and which to **Credit (Cr)**, in equal amounts. Everything downstream — the trial balance, GST returns, the P&L, the balance sheet, the audit — is just journal entries aggregated. If you can pass the right entry for a real business event, you can do 70% of an accounts executive's job.

This is the core skill of every hands-on finance/accounts role: **Accounts Executive, Accounts Payable/Receivable, GST/Tax executive, Article assistant, Financial Analyst (who must read the entries auditors passed), and Controllers** who review them. In practice you pass these in **TallyPrime, Zoho Books, SAP, Oracle NetSuite, or QuickBooks** — but the tool only asks you the same question: *which head is Dr, which is Cr, and for how much?*

## The gap: why companies want this (and college didn't teach it)

College teaches you the rule ("debit the receiver, credit the giver") and makes you pass textbook entries with clean numbers. Industry throws messy, tax-laden, multi-leg reality at you:

- A single sales invoice has **five lines** — party, sales, CGST, SGST, and possibly TCS or a round-off — not the two-line entry from your textbook.
- Real entries carry **input tax credit (ITC)** logic, **TDS deduction**, **reverse charge (RCM)**, **accruals at month-end**, and **prepaid amortisation** that colleges skip entirely.
- Nobody in a job says "pass a journal entry." They say *"book this vendor bill,"* *"the electricity bill for March hasn't come — provide for it,"* *"amortise the annual insurance,"* *"run depreciation for the quarter."* You must translate business language into Dr/Cr yourself.

The gap employers pay to close: **turning a real document (an invoice, a payslip, a bank statement, a rent agreement) into the correct, tax-compliant entry — first try, without a template.**

## What "proficient" looks like

A job-ready person can, unaided:

1. Look at any **GST invoice** and book it with the correct CGST/SGST vs IGST split (intra- vs inter-state).
2. Know when to **debit an asset vs an expense**, and when tax is an asset (ITC) vs a cost (blocked credit / RCM).
3. Pass **month-end adjustment entries** — accruals, prepaids, depreciation, provisions — so the P&L reflects the *period*, not just cash movement.
4. Handle **TDS on both sides** (deducted by us on expenses; deducted by customers on our income).
5. Self-check: every entry's **total Dr = total Cr**, and the resulting balance makes intuitive sense (an asset stays debit, income stays credit).

## Hands-on: how to actually do it

Golden rule set (modern, balance-sheet approach): **Assets & Expenses increase on Debit; Liabilities, Equity & Income increase on Credit.** Reverse to decrease.

### 1. Sales with GST (intra-state, ₹1,00,000 + 18% GST)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Debtor / Bank A/c | 1,18,000 | |
| To Sales A/c | | 1,00,000 |
| To Output CGST @9% | | 9,000 |
| To Output SGST @9% | | 9,000 |

Inter-state? Replace CGST+SGST with a single **Output IGST @18% ₹18,000**.

### 2. Purchase with GST (ITC claim)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases A/c | 50,000 | |
| Input CGST @9% | 4,500 | |
| Input SGST @9% | 4,500 | |
| To Creditor A/c | | 59,000 |

Input GST is a **current asset** (receivable from government), not an expense.

### 3. Expense with TDS (professional fees ₹1,00,000, TDS 10% u/s 194J)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Professional Fees A/c | 1,00,000 | |
| Input CGST @9% | 9,000 | |
| Input SGST @9% | 9,000 | |
| To Vendor A/c | | 1,08,000 |
| To TDS Payable (194J) | | 10,000 |

TDS is computed on the **taxable value (₹1,00,000), not on GST**. You pay the vendor ₹1,08,000 and deposit ₹10,000 with the government.

### 4. Payroll (gross ₹5,00,000; PF ₹30,000 employee; TDS ₹40,000; net paid ₹4,30,000)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Salaries & Wages A/c | 5,00,000 | |
| To Salary Payable A/c | | 4,30,000 |
| To PF Payable (employee) | | 30,000 |
| To TDS Payable (192) | | 40,000 |

Employer PF/ESI is a **separate** entry: `Dr PF Employer Contribution (expense) / Cr PF Payable`.

### 5. Accrual (electricity for March, bill not yet received, est. ₹25,000)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Electricity Expense A/c | 25,000 | |
| To Outstanding Expenses A/c | | 25,000 |

Reverse next month when the actual bill arrives, then book the real invoice.

### 6. Prepaid (annual insurance ₹1,20,000 paid 1 Apr; monthly charge ₹10,000)

At payment:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Prepaid Insurance A/c | 1,20,000 | |
| To Bank A/c | | 1,20,000 |

Every month-end:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Insurance Expense A/c | 10,000 | |
| To Prepaid Insurance A/c | | 10,000 |

### 7. Depreciation (machine ₹6,00,000, SLM, 10% p.a. → ₹5,000/month)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Depreciation A/c | 5,000 | |
| To Accumulated Depreciation A/c | | 5,000 |

### 8. Provision (audit fees payable, estimated ₹75,000)

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Audit Fees A/c | 75,000 | |
| To Provision for Audit Fees A/c | | 75,000 |

### TallyPrime click-path (Sales voucher)
`Gateway of Tally → Vouchers → F8 (Sales) → Party A/c name → Sales ledger → select Item/amount → GST ledgers auto-calc if rates are set in the stock item → Ctrl+A to save.` For a pure JV use **F7 (Journal)**.

## Worked example / mini-project

**Reproduce March books for "Kaleru Traders" (Telangana, intra-state).**

Transactions:
1. Sold goods ₹2,00,000 + 18% GST on credit to a Hyderabad customer.
2. Bought raw material ₹80,000 + 18% GST on credit from a local vendor.
3. Paid March rent ₹40,000 + 18% GST; landlord deducts nothing, we deduct TDS 10% u/s 194I.
4. Ran payroll: gross ₹1,00,000, TDS ₹8,000, net ₹92,000.
5. Month-end: depreciation ₹5,000; provide ₹15,000 for unbilled electricity.

**Entries:**

| # | Account | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 1 | Debtors | 2,36,000 | |
| | To Sales | | 2,00,000 |
| | To Output CGST / SGST | | 18,000 / 18,000 |
| 2 | Purchases | 80,000 | |
| | Input CGST / SGST | 7,200 / 7,200 | |
| | To Creditors | | 94,400 |
| 3 | Rent | 40,000 | |
| | Input CGST / SGST | 3,600 / 3,600 | |
| | To Landlord | | 43,200 |
| | To TDS Payable (194I) | | 4,000 |
| 4 | Salaries | 1,00,000 | |
| | To Salary Payable | | 92,000 |
| | To TDS Payable (192) | | 8,000 |
| 5a | Depreciation | 5,000 | |
| | To Accumulated Dep. | | 5,000 |
| 5b | Electricity | 15,000 | |
| | To Outstanding Expenses | | 15,000 |

**Net GST payable check:** Output ₹36,000 − Input (₹14,400 + ₹7,200) = **₹14,400 payable** in GSTR-3B. This single reconciliation is what a GST executive computes every month.

## How it's tested

**Interview questions:**
- "Pass the entry for a credit sale of ₹1,00,000 with 18% GST, inter-state." (Expect: IGST, not CGST/SGST.)
- "Insurance paid for the full year — how do you treat it?" (Prepaid + monthly amortisation.)
- "Difference between provision and accrual?" (Provision = estimated known liability; accrual = expense incurred, bill awaited.)
- "Is input GST an expense?" (No — a current asset / ITC.)
- "Bill received but goods not yet delivered — book it?" (Match to period; goods-in-transit / accrual logic.)

**Practical assessment:** Firms hand you **5–10 vouchers or a stack of invoices and a 30-minute timer** in Tally or on paper, and ask you to book them and produce a trial balance that ties. Some give a "close these books" case: raw transactions + instructions to pass month-end adjustments and hand back a P&L. Big-4 article interviews probe the *why* behind each Dr/Cr.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Charging CGST/SGST on an inter-state sale | Check place of supply first: same state → C+S; different state → IGST. |
| Deducting TDS on the GST portion | TDS is on the **taxable value only**. |
| Treating input GST as an expense | Book it as **Input CGST/SGST/IGST (asset)** so ITC flows to GSTR-3B. |
| Capitalising a repair / expensing an asset | Asset = future benefit > 1 yr; repair = restore current condition. |
| Forgetting to reverse accruals next period | Pass a reversing JV on day 1 of the new month. |
| Provision & actual bill both hitting expense (double count) | Reverse the provision when the real invoice is booked. |
| Entry doesn't balance | Always verify **ΣDr = ΣCr** before saving. |

## Learn-it roadmap & resources

**Time to proficiency: 4–6 weeks** of daily practice (you already have the theory from CA Inter).

- **Week 1–2:** Master the modern golden rules; hand-write the 8 entry types above until automatic.
- **Week 3:** TallyPrime — do the free **Tally Education** course or ICAI's Tally module; book 50+ real invoices.
- **Week 4:** GST layer — practise CGST/SGST/IGST/RCM and reconcile a month to GSTR-3B on the GST portal (sandbox).
- **Ongoing:** Pull a real company's financials and reverse-engineer what entries produced each line.

**Resources:** ICAI Accounting & Taxation study material (free), TallyPrime GST self-learning (free), Zoho Books "Accountant" free plan for sandbox practice, and Cleartax/TaxGuru articles for TDS/GST rate updates. **Certifications that signal competence:** Tally ACE/Professional, and your CA Inter itself.

## Quick-reference

| Event | Debit | Credit |
|---|---|---|
| Credit sale (intra) | Debtor | Sales + Output CGST + Output SGST |
| Credit sale (inter) | Debtor | Sales + Output IGST |
| Purchase | Purchases + Input CGST/SGST | Creditor |
| Expense + TDS | Expense + Input GST | Vendor + TDS Payable |
| Payroll | Salaries | Salary Payable + PF + TDS |
| Accrual | Expense | Outstanding Expenses |
| Prepaid (pay) / (charge) | Prepaid Asset / Expense | Bank / Prepaid Asset |
| Depreciation | Depreciation | Accumulated Depreciation |
| Provision | Expense | Provision A/c |

**Rules:** Assets & Expenses ↑ = Dr · Liabilities, Equity, Income ↑ = Cr · TDS on taxable value only · Input GST = asset · Same state → CGST+SGST, different state → IGST · Always ΣDr = ΣCr.

**Common rates:** GST 5/12/18/28% · TDS 194J (professional) 10% · 194I (rent) 10% · 194C (contractor) 1–2% · 192 (salary) at slab.
