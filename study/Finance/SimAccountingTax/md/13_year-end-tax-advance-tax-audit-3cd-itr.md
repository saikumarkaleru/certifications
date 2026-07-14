# Year-End Tax: Advance Tax, Company Computation, Tax Audit (3CD) and ITR

## The situation

It's **20-Sep-2027**. This just landed on your desk: the CFO forwards the auditor's email — *"We start signing the tax audit next week. Give me NTSPL's income-tax computation from the audited PBT of Rs 1,50,60,000, tell me whether the 25% route or 115BAA 22% is cheaper, reconcile the advance tax we paid across the four installments (and any 234B/234C interest), confirm 44AB applies and prep the key Form 3CD clauses. We file ITR-6 by 31-Oct."*

This is the year-end tax cycle for a domestic company: **book profit → taxable income (add-backs/deductions) → tax at the chosen rate → advance-tax reconciliation with interest → tax audit (Form 3CA/3CD) → return (ITR-6).** Every number must reconcile to the audited financials you finalised in the previous chapter.

## What you're given

**From the audited FY2026-27 financials:**

| Item | Rs |
|------|---:|
| Profit before tax (per Statement of P&L) | 1,50,60,000 |
| Depreciation charged in books (WDV, same as tax here) | 14,40,000 |
| Turnover FY2026-27 | 12,00,00,000 |
| Cash receipts & payments | each < 5% of total |

**Add-back / deduction working papers (illustrative FY2026-27):**

| Adjustment | Rs | Nature |
|------------|---:|--------|
| Provision for audit fee unpaid at year-end (43B — allow only if paid before ITR due date) | Nil disallowance (paid before 31-Oct) | timing |
| Disallowance u/s 40(a)(ia) — expense where TDS not deducted | Nil (all TDS deducted) | compliance |
| Donations / penalties (not allowable) | Assume nil | permanent |
| Depreciation — books = tax (WDV, same blocks) | No difference | — |

For NTSPL, working papers show **no net book-to-tax adjustment** this year (TDS fully deducted, statutory dues paid before the ITR due date, book WDV = tax WDV). So taxable income ≈ PBT.

**Advance tax actually paid (challans, ITNS-280):**

| Installment | Due date | Cumulative % | Cumulative due (Rs) | Paid on date (Rs) |
|-------------|----------|-------------:|--------------------:|------------------:|
| 1 | 15-Jun-2026 | 15% | 5,94,000 | 5,94,000 |
| 2 | 15-Sep-2026 | 45% | 17,82,000 | 17,82,000 |
| 3 | 15-Dec-2026 | 75% | 29,70,000 | 25,00,000 (short) |
| 4 | 15-Mar-2027 | 100% | 39,60,000 | 39,60,000 |

## Do it — step by step

### Step 1 — Compute taxable income

```
Profit before tax (books) ................. 1,50,60,000
Add:  Inadmissible expenses / provisions ..        NIL
      (audit fee paid before ITR due date u/s 43B;
       all TDS deducted, so no 40(a)(ia) add-back)
Less: Deductions / allowances .............        NIL
                                            -----------
Taxable business income (rounded) ......... 1,50,60,000
```
Rounded to nearest Rs 10 u/s 288A: **Rs 1,50,60,000**.

### Step 2 — Choose the tax rate: 25% + cess vs 115BAA 22%

NTSPL is a domestic company with turnover ≤ Rs 400 cr, so it qualifies for the **25%** base rate. It can instead opt into **Section 115BAA (22%)** by forgoing specified incentives/deductions. Since NTSPL claims no such incentives, the lower base rate wins outright.

| Route | Base rate | Base tax on 1,50,60,000 | Surcharge | Cess 4% | Total tax |
|-------|----------:|------------------------:|----------:|--------:|----------:|
| Normal (turnover ≤ 400 cr) | 25% | 37,65,000 | 7% (income >1cr ≤10cr) 2,63,550 | 4% of (37,65,000+2,63,550)=1,61,142 | **41,89,692** |
| **115BAA** | 22% | 33,13,200 | flat 10% 3,31,320 | 4% of 36,44,520 = 1,45,781 | **37,90,301** |

Under 115BAA surcharge is a flat **10%** regardless of income level, and MAT (115JB) does not apply. Even though 22% < 25%, run both fully because the surcharge differs. Here **115BAA at Rs 37,90,301 is cheaper by ~Rs 3,99,391** — NTSPL opts in by filing **Form 10-IC before the ITR due date**. (The Balance Sheet chapter carried a simplified provision near Rs 39.6L; the precise, surcharge-and-cess-inclusive liability under the chosen 115BAA route is Rs 37,90,301 — the figure that goes on the return.)

**Decision: opt 115BAA. Total tax liability = Rs 37,90,301 (round to Rs 37,90,300 u/s 288B).**

### Step 3 — Advance-tax and interest u/s 234B / 234C

Assessed tax ≈ Rs 37,90,300. Advance tax should have been paid 15/45/75/100% by the four dates.

**234C (deferment of installments)** — 1% per month for 3 months on each shortfall:
- Installment 3 (15-Dec): required 75% of 37,90,300 = 28,42,725; paid cumulative 5,94,000+17,82,000+25,00,000 = 48,76,000 — wait, cumulative paid by 15-Dec = 5,94,000 + 17,82,000 + 25,00,000 = **48,76,000**, which *exceeds* 75% required. So no 234C shortfall on installment 3 either. In this fact-set NTSPL paid enough cumulatively by each date, so **234C = Nil**.

Let me restate cleanly against the *final* liability of Rs 37,90,300:

| Installment | % req | Cumulative req (Rs) | Cumulative paid (Rs) | Shortfall |
|-------------|------:|--------------------:|---------------------:|----------:|
| 15-Jun | 15% | 5,68,545 | 5,94,000 | none |
| 15-Sep | 45% | 17,05,635 | 23,76,000 | none |
| 15-Dec | 75% | 28,42,725 | 48,76,000 | none |
| 15-Mar | 100% | 37,90,300 | 88,36,000 | none |

Because total advance tax paid (Rs 88,36,000 across the year in this illustration) fully covers the liability and each installment threshold was met, **234C = Nil and 234B = Nil**. (If cumulative advance tax at any date had fallen below 90% by year-end, 234B would run at 1%/month from 1-Apr on the shortfall.) *Note: the installment amounts above are illustrative to demonstrate the 234B/234C test; where a genuine shortfall existed, interest = shortfall × 1% × months.*

### Step 4 — Confirm tax audit u/s 44AB

Turnover Rs 12,00,00,000. Ordinarily the limit is Rs 1 cr, **raised to Rs 10 cr** where both cash receipts and cash payments are ≤ 5% of the respective totals. NTSPL is digital (< 5% cash), so the Rs 10 cr threshold applies — **but turnover (Rs 12 cr) still exceeds Rs 10 cr, so 44AB tax audit applies.** Report in **Form 3CA** (accounts audited under Companies Act) + **Form 3CD**, due **30-Sep-2027**.

### Step 5 — Key Form 3CD clauses (walk-through)

| Clause | What it reports | NTSPL entry |
|--------|-----------------|-------------|
| 8/8a | Section under which audit + 115BAA option | 44AB; opted 115BAA via Form 10-IC |
| 12 | Nature of business | Trading (HSN 8536) + services (SAC 9987) |
| 18 | Depreciation u/s 32 | WDV blocks; dep Rs 14,40,000 |
| 21 | Amounts debited but inadmissible | Nil (all TDS deducted) |
| 26 | Sec 43B — sums allowable only on payment | Audit fee, PF/ESI — paid before due dates |
| 27a | CENVAT/ITC | GST ITC availed per returns |
| 34 | TDS/TCS compliance | 194C/194J/194H/194I/194Q deducted & deposited |
| 40 | Ratios (turnover, GP, NP, stock) | GP 3,60,00,000/12,00,00,000 = 30% |
| 44 | Break-up of expenditure GST-registered vs not | from purchase register |

### Step 6 — File ITR-6

Companies (other than those claiming 11 exemption) file **ITR-6**, electronically with **DSC**. Carry the computed income Rs 1,50,60,000, tax Rs 37,90,300, advance tax paid, TDS credited (Form 26AS), and the 115BAA option. Due date for an audited company: **31-Oct-2027**.

## The deliverable

**NTSPL — Income-tax computation, AY 2027-28 (FY2026-27):**

| Particulars | Rs |
|-------------|---:|
| Profit before tax (audited) | 1,50,60,000 |
| Add: inadmissible items | Nil |
| Less: deductions | Nil |
| **Total income** | **1,50,60,000** |
| Tax u/s 115BAA @ 22% | 33,13,200 |
| Add: surcharge @ 10% | 3,31,320 |
| Sub-total | 36,44,520 |
| Add: health & education cess @ 4% | 1,45,781 |
| **Total tax liability** | **37,90,301** (rounded 37,90,300) |
| Less: advance tax paid | (37,90,300) |
| Add: interest 234B/234C | Nil |
| **Net payable / (refund)** | **Nil** |

**Filing calendar:**

| Form | Purpose | Due date |
|------|---------|----------|
| Form 10-IC | Opt into 115BAA | Before ITR due date |
| Form 3CA + 3CD | Tax audit report | 30-Sep-2027 |
| ITR-6 | Company return | 31-Oct-2027 |

## How it's checked

- **PBT ties to the audited P&L:** computation starts from Rs 1,50,60,000 exactly — the finalized figure.
- **26AS / AIS reconciliation:** TDS credited in ITR-6 must match Form 26AS; advance-tax challans (BSR code, challan no.) must match OLTAS.
- **3CD ↔ financials:** depreciation clause 18 = P&L depreciation Rs 14,40,000; ratios in clause 40 recompute from the audited statements (GP 30%).
- **115BAA validity:** Form 10-IC acknowledgement number must be quoted in ITR-6; if not filed timely, the 22% rate is denied and 25% applies.
- **234B/234C:** the system recomputes interest from the assessed tax; if advance tax < 90%, 234B triggers automatically on e-filing.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Opting 115BAA in ITR but not filing Form 10-IC | 22% denied, tax recomputed at 25% + demand | File 10-IC before ITR due date, quote ack no. |
| Ignoring surcharge difference (7% vs flat 10%) | Wrong route chosen | Compare *total* tax incl. surcharge + cess |
| Audit fee/PF unpaid at year-end but claimed | 43B disallowance, higher tax | Pay before ITR due date or add back |
| TDS not deducted on a vendor expense | 30% disallowance u/s 40(a)(ia) | Deduct/deposit; report correctly in clause 21/34 |
| Filing 3CD after 30-Sep | Penalty u/s 271B (0.5% of turnover, max Rs 1.5L) | File on time |

## On the job & in the interview

Year-end tax is where accounting profit and *taxable* profit part ways, then get reconciled on a single computation sheet the auditor and the assessing officer both read. For NTSPL the two happen to converge (no add-backs), but the *discipline* — start from audited PBT, layer statutory adjustments, pick the cheaper lawful rate, prove advance-tax timing — is the job.

**Q: 25% vs 115BAA — how do you decide?**
A: Compute total tax under both, including surcharge and cess, because 115BAA carries a flat 10% surcharge while the normal route steps 7%/12%. For NTSPL with no incentive deductions, 115BAA (22%) at Rs 37.90L beats the 25% route at Rs 41.90L. If the company claimed heavy incentives (SEZ, additional depreciation), the maths could flip — 115BAA forgoes them.

**Q: What triggers 234B vs 234C?**
A: 234C is for *deferment* — missing the 15/45/75/100% installment schedule; interest is 1%/month for 3 months on each installment shortfall. 234B is for *default* — paying less than 90% of assessed tax as advance tax, charged 1%/month from 1-April of the AY until payment. They can both apply in the same year.

**Q: Does tax audit apply given the Rs 10 cr limit?**
A: Yes. The Rs 1 cr limit is raised to Rs 10 cr only when cash receipts and payments are each ≤ 5%, which NTSPL meets — but turnover is Rs 12 cr, still above Rs 10 cr, so 44AB applies. We file Form 3CA/3CD by 30-Sep, then ITR-6 by 31-Oct.
