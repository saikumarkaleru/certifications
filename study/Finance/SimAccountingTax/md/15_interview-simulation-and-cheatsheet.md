# The Accounts/Tax Role Interview Simulation + FY2026-27 Cheat-Sheet

## The situation

It's **Thursday, 10 September 2026**, 11:00 a.m. You're in the boardroom of a company just like **Nirvana Traders & Services Pvt Ltd (NTSPL)** — Rs 12 crore turnover, trading + AMC services, GST regular filer, 15 staff — interviewing for **Accounts Executive / Tax Associate**. The Finance Controller has your resume and a laptop with TallyPrime open. This is the working interview: half concept, half "show me on the screen." Below is the real Q&A, then the one-page cheat-sheet you'd revise the night before.

## What you're given

The panel: FC (chartered accountant) + the outgoing associate. On the table: a printed trial balance, an April GST summary, and a payslip. They'll jump between journal entries, GST, TDS, month-end and a live Tally/Excel task. All numbers are the NTSPL FY2026-27 figures so everything reconciles.

## Do it — the mock interview (Q&A with model answers)

**Q1. "Pass the journal entry for a credit sale of Rs 60,00,000 intra-state goods at 18% GST."**
```
Dr  Debtors                       70,80,000
    Cr  Sales — goods (intra)          60,00,000
    Cr  Output CGST @9%                  5,40,000
    Cr  Output SGST @9%                  5,40,000
```
"Intra-state, so CGST + SGST split equally; inter-state would be a single IGST @18% = Rs 4,50,000 on the Rs 25,00,000 inter-state leg."

**Q2. "April output tax is CGST 6,75,000 + SGST 6,75,000 + IGST 4,50,000; ITC is CGST 5,31,000 + SGST 5,31,000 + IGST 2,16,000. Compute net cash GST and show the set-off order."**

| Head | Output | ITC same head | IGST cross-credit | Cash payable |
|---|---|---|---|---|
| IGST | 4,50,000 | 2,16,000 | — | 2,34,000 → paid first from own IGST, nil cash |
| CGST | 6,75,000 | 5,31,000 | balance IGST | see working |
| SGST | 6,75,000 | 5,31,000 | balance IGST | see working |

"**Set-off order (FY2026-27):** IGST credit is used first — against IGST, then CGST, then SGST. CGST credit only against CGST then IGST; SGST only against SGST then IGST; **CGST and SGST never cross-set-off.** After exhausting IGST credit on IGST liability (2,16,000 of 4,50,000), the leftover IGST liability 2,34,000 is met by... actually IGST has no ITC left, so IGST cash = 2,34,000. CGST: 6,75,000 − 5,31,000 = 1,44,000 cash; SGST: 6,75,000 − 5,31,000 = 1,44,000 cash. **Total cash ≈ Rs 5,22,000**, matching the books. Then I defer the Rs 7,200 ITC not in 2B."

**Q3. "Name the TDS section, rate and threshold for: contractor, professional fee, commission, rent, and goods purchase — FY2026-27."**

| Payment | Section | Rate | Threshold |
|---|---|---|---|
| Contractor (agency, housekeeping) | 194C | 1% ind/HUF, **2% others** | Rs 30,000 single / Rs 1,00,000 p.a. |
| Professional/consultant fee | 194J | 10% (2% technical) | Rs 50,000 p.a. |
| Commission | 194H | 2% | Rs 20,000 p.a. |
| Rent (land/building) | 194I | 10% | Rs 2,40,000 p.a. |
| Goods purchase (buyer T/O > 10 cr) | 194Q | 0.1% on amount > Rs 50 L/seller | Rs 50 L/seller |
| Salary | 192 | slab on estimated income | basic exemption |

"Note the **Income-tax Act 2025** re-numbers these from 01-Apr-2026 — salary under **Sec 392**, others under **Sec 393** — but TRACES/Tally still show 194x, so we use those on the job."

**Q4. "April's 194J: consultant fee Rs 1,00,000. Entry and deposit date?"**
```
Dr  Professional fees            1,00,000
    Cr  TDS payable u/s 194J           10,000
    Cr  Vendor / Bank                   90,000
```
"Deposit by the **7th of next month** (7-May-2026); March deductions by 30-Apr. Quarterly 26Q by 31-Jul/31-Oct/31-Jan/31-May."

**Q5. "Prepare a BRS. Book balance Rs 10,00,000; bank statement Rs 9,40,000; a cheque of Rs 80,000 issued not yet cleared; bank charges Rs 20,000 not in books."**

| BRS as at 30-Apr-2026 | Rs |
|---|---|
| Balance per books | 10,00,000 |
| Less: bank charges not recorded | (20,000) |
| Adjusted book balance | 9,80,000 |
| Balance per bank statement | 9,40,000 |
| Add: cheque issued not yet presented | 40,000 |
| ...reconciled | 9,80,000 |

"The Rs 80,000 uncleared cheque figure was a trap — only the un-presented portion reconciles; I record the bank charge in books via a journal (Dr Bank charges, Cr Bank)."

**Q6. "Under which Schedule III head does a 5-year term loan go? And GST payable?"**
"**Schedule III, Companies Act 2013:** term loan = **Non-current liabilities → Long-term borrowings** (the portion due within 12 months moves to Other current liabilities). **GST payable** = Current liabilities → Other current liabilities (statutory dues). Trade payables sit separately under current liabilities."

**Q7. "Walk me through your month-end close for April."**
"1. Book all sales/purchases, reconcile to GST portal. 2. Run payroll — gross Rs 9,00,000, deduct EPF/ESI/PT/TDS. 3. **Provisions & accruals:** depreciation Rs 1,20,000, accrued electricity Rs 40,000, audit-fee provision Rs 25,000, prepaid insurance Rs 60,000 amortised at Rs 5,000/month. 4. **BRS** on HDFC xxxx4567. 5. GST set-off + GSTR-1 (11th) and 3B (20th). 6. TDS challan by 7th. 7. Closing stock Rs 45,00,000 (lower of cost/NRV). 8. Trial balance tie-out and MIS to the director."

**Q8. "Depreciation provision entry for April?"**
```
Dr  Depreciation                 1,20,000
    Cr  Accumulated depreciation      1,20,000
```
"Annual Rs 14,40,000 ÷ 12; Companies Act Schedule II useful lives for books, Income-tax block/WDV rates for the tax computation — the two differ, creating deferred tax."

**Q9. "Priya Rao earns Basic 30,000 + HRA 15,000 + Special 10,000 = Rs 55,000 gross. Compute PF and PT (Telangana)."**
"**EPF** on basic capped at the Rs 15,000 ceiling: employee 12% = Rs 1,800; employer 12% = Rs 1,800 (EPS 8.33% = Rs 1,250 + EPF 3.67% = Rs 550). **ESI** — nil, gross > Rs 21,000 ceiling. **PT Telangana** — Rs 200/month (wage > Rs 20,000). Salary entry: Dr Salaries, Cr PF/ESI/PT/TDS payable, Cr Bank (net)."

**Q10. "Company PBT is Rs 1,50,60,000. Two tax routes?"**
"**25% + 4% cess** (domestic co, turnover ≤ Rs 400 cr) or **22% u/s 115BAA + 10% surcharge + 4% cess** (no incentives, ~25.17% effective). At 25% route, tax ≈ Rs 39.16 L incl. cess, **PAT ≈ Rs 1,11,00,000.** 115BAA is chosen only if you're not using major deductions — it locks you in."

**Q11. "e-invoicing and tax audit — do they apply to NTSPL?"**
"**e-invoicing:** yes, turnover Rs 12 cr > Rs 5 cr threshold — IRN + QR mandatory. **Tax audit u/s 44AB:** normally > Rs 1 cr, but raised to Rs 10 cr since cash receipts and payments are each < 5%; NTSPL is Rs 12 cr, so audit applies — **3CB-3CD due 30-Sep**, ITR-6 by 31-Oct."

**Q12. "Live Tally task: I purchased goods Rs 55,00,000 + 18% GST intra-state. Voucher and ITC?"**
"Gateway of Tally → Vouchers → **F9 Purchase**:
```
Dr  Purchases — goods            55,00,000
Dr  Input CGST @9%                4,95,000
Dr  Input SGST @9%                4,95,000
    Cr  Creditor / Bank               64,90,000
```
ITC of Rs 9,90,000 flows to the electronic credit ledger once it's in GSTR-2B."

**Q13. "Excel test: given a column of invoice values, sum only those > Rs 50,000 for 194Q. Formula?"**
"`=SUMIF(B2:B200,\">50000\",B2:B200)` — or `SUMIFS` for multiple criteria (seller + date). For the 194Q base I'd compute `=SUMIF(range,\">50000\")` on the YTD-per-seller, then 0.1% on the amount exceeding Rs 50 lakh, using `=MAX(0,total-5000000)*0.001`."

**Q14. "How do you defer ITC not yet in 2B?"**
"Book the purchase and its input tax, but in GSTR-3B claim ITC only to the extent in 2B (Rule 36(4)). The Rs 40,000 + 7,200 bill in books but not in 2B — I hold the Rs 7,200 in an 'ITC to be availed' ledger and claim it in the month it reflects."

**Q15. "You spot a GSTR-2B item Rs 50,000 + 9,000 not in your books. Action?"**
"Don't claim it — no ITC without the underlying invoice and booking. I check whether it's a genuine missed purchase (then book it) or a wrong GSTIN by the supplier (then it's their error). Claiming un-booked ITC triggers an ASMT-10 mismatch."

## The deliverable — one-page FY2026-27 cheat-sheet

**INCOME TAX — new regime (default), individual, FY2026-27**

| Slab | Rate |
|---|---|
| 0 – 4,00,000 | Nil |
| 4 – 8 L | 5% |
| 8 – 12 L | 10% |
| 12 – 16 L | 15% |
| 16 – 20 L | 20% |
| 20 – 24 L | 25% |
| > 24 L | 30% |

Rebate 87A: **Rs 60,000** (nil tax up to Rs 12 L taxable). Standard deduction (salary): **Rs 75,000**. **Company:** 25% (T/O ≤ Rs 400 cr) or 22% u/s 115BAA + surcharge + **4% cess**.

**TDS — sections / rate / threshold (FY2026-27)**

| Sec | Payment | Rate | Threshold |
|---|---|---|---|
| 192 | Salary | slab | exemption limit |
| 194C | Contractor | 1% ind, 2% others | 30k single / 1L p.a. |
| 194H | Commission | 2% | 20k p.a. |
| 194I | Rent (land/bldg) | 10% | 2.4L p.a. |
| 194J | Professional | 10% (2% tech) | 50k p.a. |
| 194Q | Goods (buyer T/O>10cr) | 0.1% over 50L | 50L/seller |

Deposit by **7th** of next month (March by 30-Apr). Returns **24Q/26Q**: 31-Jul, 31-Oct, 31-Jan, 31-May.

**GST**

- Returns: **GSTR-1** by 11th, **GSTR-3B** by 20th, **GSTR-9/9C** by 31-Dec of next FY.
- **Set-off order:** IGST credit → IGST, then CGST, then SGST. CGST → CGST then IGST. SGST → SGST then IGST. **CGST ⊗ SGST never cross.**
- Blocked credits: **Sec 17(5)**. e-invoice > Rs 5 cr T/O. e-way bill > Rs 50,000 consignment.

**PAYROLL**

- **EPF** 12% + 12% (employer = EPS 8.33% + EPF 3.67%), ceiling Rs 15,000.
- **ESI** employee 0.75% + employer 3.25%, ceiling Rs 21,000. PF & ESI paid by **15th**.
- **PT Telangana:** nil ≤ 15,000; Rs 150 for 15,001–20,000; **Rs 200** > 20,000.

**TAX AUDIT 44AB:** business > Rs 1 cr (→ Rs 10 cr if cash receipts & payments each ≤ 5%); profession > Rs 50 L. **3CA/3CB-3CD due 30-Sep; ITR-6 (audited co) 31-Oct.**

**KEY FORMS:** ASMT-10/11 (GST scrutiny), DRC-03 (voluntary pay), 143(1) (intimation), 154 (rectification), 26AS/AIS (TDS credit), 16/16A (TDS certs), 3CB-3CD (tax audit).

## How it's checked

The FC scores you on: (i) do your **journal entries balance** and use the right heads; (ii) do you know the **set-off order cold** (CGST/SGST never cross); (iii) do TDS section-rate-threshold come out instantly; (iv) does your BRS **tie both sides**; (v) can you actually **drive TallyPrime** (voucher shortcuts F7/F8/F9) and Excel (SUMIF/SUMIFS/VLOOKUP). A wrong set-off or a made-up threshold is an instant flag.

## Common mistakes & red flags

| Mistake | Why it fails |
|---|---|
| Cross-setting CGST against SGST | Not allowed — cash short-paid, GST notice |
| Quoting old TDS thresholds | Signals you're not current on FY2026-27 |
| BRS that doesn't reconcile to the rupee | Shows you don't understand timing differences |
| Claiming ITC not in 2B | Rule 36(4) breach → ASMT-10 |
| Confusing Schedule II (dep, books) with Income-tax WDV rates | Deferred tax errors |
| Saying "115BAA is always better" | It's a lock-in; only if no incentives used |

## On the job & in the interview

The **"why"**: an accounts/tax role is 20% concept, 80% *"can you close a month and file a return without a notice bouncing back."* Interviewers test recall (rates, sections) because those are the daily reflexes, then a **case** ("walk me through month-end") because that's the actual job. Speak in the jargon — set-off order, 36(4), 44AB, 3CD, 26AS, deferred tax, Schedule III heads.

**Three closing interview questions with strong answers:**

*"Why do books and tax depreciation differ?"* — "Books follow Companies Act Schedule II useful lives (SLM/WDV per policy); tax follows Income-tax block-of-assets WDV rates. The gap creates a timing difference and hence **deferred tax** under AS 22 / Ind AS 12."

*"A vendor asks why you deducted TDS on his full invoice including GST."* — "TDS under 194J/194C is on the taxable value **excluding GST** if GST is shown separately on the invoice (CBDT circular). If it's not separately shown, I deduct on the gross. So I'd deduct on the fee, not the GST component."

*"How do you make sure a GST return never triggers a notice?"* — "Reconcile three ways before filing: sales in books = GSTR-1, ITC claimed ≤ GSTR-2B (Rule 36(4)), and 3B = 1. Defer ITC not in 2B, never claim un-booked 2B items, and match turnover to 26AS at year-end. If those tie, the portal's auto-scrutiny has nothing to flag."
