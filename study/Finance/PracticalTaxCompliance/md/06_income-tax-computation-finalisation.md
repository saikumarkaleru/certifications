# Income-tax computation & finalisation

## What it is & where it's used

Income-tax computation is the process of converting an entity's book profit (or an individual's gross earnings) into **taxable income**, applying the correct slab/rate, adjusting for deductions and reliefs, and arriving at the **final tax payable or refundable** for the year. Finalisation is the year-end ritual — reconciling advance tax, TDS, self-assessment tax, and the return — so the books, Form 26AS/AIS, and the ITR all agree.

Roles that live and die on this skill:

| Role | What they touch |
|------|-----------------|
| Tax associate (Big 4 / CA firm) | Computing income for 50-200 clients per season, ITR filing |
| Accounts / finance executive (industry) | Advance-tax working, provision for tax, deferred tax |
| Financial controller | Sign-off on current-tax and MAT provision at year-end close |
| Payroll / HR-finance | TDS on salary (Sec 192), Form 16 |
| Anyone doing a company statutory audit | Tax provision, MAT, tax reconciliation in notes |

If you can take a trial balance and produce a defensible tax computation sheet, you are immediately useful in March-September (the Indian filing crunch).

## The gap: why companies want this (and college didn't teach it)

MBA and even CA theory teach you the *heads of income* and the *slab rates*. What they don't teach is the **mechanical, spreadsheet-driven finalisation** that a real client engagement demands:

- Books show *depreciation as per Companies Act*; tax needs *depreciation as per Income-tax Act (WDV, block of assets)*. Nobody teaches you to run both.
- You must **add back** disallowances (Sec 40(a)(ia), 43B, 37) that never appear in a textbook profit.
- You must decide **old vs new regime** (115BAC for individuals, 115BAA for companies) — a real Rupee decision, not a definition.
- You must reconcile tax paid to **Form 26AS / AIS** before filing, or the return gets a mismatch notice.
- **MAT (Sec 115JB)** vs normal tax — computing both and paying the higher — is a pure-practice skill.

Colleges test "what is Section 80C." Employers test "here is the trial balance, give me the computation, the advance-tax challans, and the provision entry by 6 pm."

## What "proficient" looks like

A job-ready person can, **unaided**:

1. Build a **computation of total income** sheet in Excel from a trial balance — five heads, adjustments, deductions, tax, cess, interest.
2. Run **tax-depreciation** on the block-of-assets method and reconcile it to book depreciation.
3. Compute **MAT under 115JB** and compare with normal tax; know MAT credit u/s 115JAA.
4. Prepare an **advance-tax schedule** (15%/45%/75%/100% cut-offs) and compute interest u/s 234B/234C.
5. Decide **115BAA / 115BAC** with a side-by-side comparison.
6. Pass the **provision-for-tax and deferred-tax** journal entries and tie them to the computation.
7. Reconcile the computation to **Form 26AS/AIS** and file the correct **ITR** (ITR-6 company, ITR-3/2 individual).

## Hands-on: how to actually do it

### Step 1 — Company computation skeleton (FY 2024-25 / AY 2025-26)

Start from **net profit as per Statement of P&L**, then adjust:

```
Net profit as per books (before tax)            xxxx
Add:  Depreciation as per Companies Act          xxx
      Disallowances u/s 40(a)(i)/(ia)            xxx
      43B items unpaid (GST, PF, bonus, interest) xxx
      Provisions / donations debited             xxx
      Fines & penalties, personal expenses       xxx
Less: Depreciation as per Income-tax Act        (xxx)
      Income taxed under other heads / exempt    (xxx)
      Deductions Chapter VI-A (80G, 80JJAA…)     (xxx)
= Total Income (round off to nearest ₹10, Sec 288A)
```

**Excel — put the add-backs in a signed column so a single SUM works:**

```
' B = amount, C = +1 add / -1 less
=B2 (net profit)
Total Income  =B2 + SUMPRODUCT(add_amounts, add_signs)
Round off     =MROUND(TotalIncome,10)
```

### Step 2 — Tax rate logic (nested IF is fine, choose readable)

Company, opting **115BAA** (22% + 10% surcharge + 4% cess = **25.168%**), no MAT:

```
=ROUND(TotalIncome * 0.25168, 0)
```

Company **not** opting 115BAA — normal rate 25% (turnover ≤ ₹400 cr) or 30%, plus surcharge slab, plus 4% cess. Surcharge helper:

```excel
=IF(TotalIncome>100000000, 0.12, IF(TotalIncome>10000000, 0.07, 0))
```

**Individual — old vs new regime side by side (AY 2025-26 new-regime slabs):**

```excel
=LET(ti, TaxableIncome,
  MAX(0,
   (MIN(ti,700000)-300000)*0.05
 + (MIN(ti,1000000)-700000)*0.10
 + (MIN(ti,1200000)-1000000)*0.15
 + (MIN(ti,1500000)-1200000)*0.20
 + (ti-1500000)*0.30 ))
```

Add 4% cess: `=Tax*1.04`. Apply **87A rebate** if new-regime total income ≤ ₹7,00,000 → tax = 0.

### Step 3 — Tax depreciation (block of assets, WDV)

```
Opening WDV  + Additions − Sale proceeds = Closing base
Dep = base × block rate   (½ rate if asset used < 180 days)
```

| Block | Rate |
|-------|------|
| Plant & machinery (general) | 15% |
| Furniture & fittings | 10% |
| Computers & software | 40% |
| Buildings (non-residential) | 10% |
| Motor cars | 15% |

```excel
Full-rate dep  = (OpenWDV + Add180plus - Sale) * Rate
Half-rate dep  = Add_below180 * Rate/2
```

### Step 4 — MAT (Sec 115JB)

Book profit × **15% + surcharge + cess**. Pay **higher of** normal tax and MAT. Excess MAT over normal tax is **MAT credit** carried 15 years.

```excel
NormalTax = ...           
MAT       = ROUND(BookProfit*0.15*1.04*(1+surcharge),0)
TaxPayable = MAX(NormalTax, MAT)
MATCredit  = MAX(0, MAT - NormalTax)
```

Note: a company under **115BAA is exempt from MAT** — that's a big reason to opt in.

### Step 5 — Journal entries at finalisation

| Date | Particulars | Dr (₹) | Cr (₹) |
|------|-------------|-------:|-------:|
| 31-Mar | Advance income-tax A/c … Dr | 20,00,000 | |
| | To Bank | | 20,00,000 |
| 31-Mar | Income-tax expense (P&L) … Dr | 26,50,000 | |
| | To Provision for tax | | 26,50,000 |
| 31-Mar | Deferred tax expense … Dr | 1,20,000 | |
| | To Deferred tax liability | | 1,20,000 |
| Next yr | Provision for tax … Dr | 26,50,000 | |
| | To Advance tax + TDS | | 24,00,000 |
| | To Bank (self-assessment 140A) | | 2,50,000 |

### Step 6 — Advance-tax & 234C interest

| Due date | Cumulative % | 234C trigger if paid < |
|----------|-------------|------------------------|
| 15 Jun | 15% | 12% |
| 15 Sep | 45% | 36% |
| 15 Dec | 75% | 75% |
| 15 Mar | 100% | 100% |

234B interest = **1% p.m.** on shortfall (if advance tax < 90% of assessed) from April to payment. 234C = 1% p.m. on each instalment shortfall.

## Worked example / mini-project

**Alpha Traders Pvt Ltd, FY 2024-25.** Reproduce this in Excel.

| Line | ₹ |
|------|---:|
| Net profit as per books | 1,00,00,000 |
| Add: Depreciation (Companies Act) | 18,00,000 |
| Add: GST unpaid at year-end (43B) | 3,00,000 |
| Add: Donation to CM Relief debited | 2,00,000 |
| Add: Penalty for late GST filing | 50,000 |
| Less: Depreciation (Income-tax Act) | (22,00,000) |
| **Business income** | **1,01,50,000** |
| Less: 80G (50% of ₹2,00,000) | (1,00,000) |
| **Total income** | **1,00,50,000** |

Turnover ₹380 cr → base rate **25%**. Not opting 115BAA.

```
Tax @25%                       = 25,12,500
Surcharge @7% (TI > ₹1 cr)     =  1,75,875
                                 ----------
                                 26,88,375
Cess @4%                       =  1,07,535
Total normal tax               = 27,95,910
```

MAT check: book profit ≈ ₹1,05,50,000 → MAT @15% × 1.04 × 1.07 = ₹17,60,900 < normal tax. **Pay ₹27,95,910.**

If instead Alpha opts **115BAA**: 1,00,50,000 × 25.168% = **₹25,29,384** — a genuine ₹2.66 lakh saving, no surcharge slab, no MAT. That comparison *is* the deliverable a manager wants.

Advance tax paid ₹24,00,000; TDS credit (26AS) ₹1,50,000; balance ₹2,45,910 → pay as **self-assessment tax (Sec 140A)** via challan before filing **ITR-6**.

## How it's tested

**Interview questions**
- "Company book profit is ₹50 lakh, tax depreciation is higher than book — walk me through the computation."
- "When would a company still pay MAT under the old regime but not under 115BAA?"
- "Difference between 234B and 234C interest?"
- "Advance tax first instalment date and percentage?"
- "Deferred tax vs current tax — which timing differences create DTL?"

**Practical assessments**
- **Timed Excel test (60-90 min):** given a trial balance + fixed-asset schedule, produce the computation sheet, tax, MAT, and advance-tax working.
- **"Finalise these books" case:** pass provision, advance-tax adjustment, and deferred-tax entries; tie the ITR figure to the ledger.
- **26AS reconciliation:** they hand you a 26AS PDF and books; find the TDS mismatch.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---------|-----|
| Using book depreciation for tax | Always maintain a separate **block-of-assets** register; never copy Companies-Act dep. |
| Forgetting 43B — claiming unpaid GST/PF/bonus | Add back anything statutory **unpaid by the ITR due date**. |
| Ignoring MAT because "we have profit" | Compute **both** every year; pay the higher. |
| Missing the ½-rate rule on assets used < 180 days | Tag every addition with its put-to-use date. |
| Not reconciling to **AIS/26AS** before filing | Download 26AS + AIS first; match TDS line by line. |
| Applying old surcharge slabs to a 115BAA company | 115BAA has a **flat 10% surcharge**, no slab. |
| Forgetting 234C on quarterly shortfall | Model the four cut-offs in the advance-tax sheet. |
| Rounding wrong | Round **total income** to nearest ₹10 (288A), tax to nearest ₹1. |

Pros keep a **standard computation template** and a **checklist of add-backs** so nothing is missed under season pressure.

## Learn-it roadmap & resources

| Phase | Time | What to do |
|-------|------|-----------|
| Basics | 2 weeks | Five heads, slabs, both regimes — CA Inter Taxation module |
| Computation | 3 weeks | Build 10 company + 10 individual computations in Excel from scratch |
| Depreciation & MAT | 1 week | Block-of-assets register; MAT under 115JB |
| Filing | 1 week | File a dummy ITR-3 and ITR-6 on the income-tax portal |
| Provision & deferred tax | 1 week | AS 22 / Ind AS 12 entries, tie to computation |

**Resources**
- Income-tax portal (incometax.gov.in) — free ITR utilities, Form 26AS, AIS
- ICAI Study Material — Taxation (authoritative, free)
- CBDT rate cards / Finance Act each year (surcharge, slabs change annually)
- Cleartax / Taxmann computation guides for worked examples
- **Certification:** CA / CMA; or a practical GST+ITR filing course (Cleartax, Udemy) for non-CA roles

Realistic time-to-proficiency: **6-8 weeks** of daily practice to independently finalise a straightforward company.

## Quick-reference

**Company rates (AY 2025-26)**

| Basis | Rate (+cess 4%) |
|-------|-----------------|
| 115BAA | 22% + 10% surcharge = **25.168%** (no MAT) |
| Turnover ≤ ₹400 cr | 25% + surcharge slab |
| Others | 30% + surcharge slab |
| MAT (115JB) | 15% of book profit |

**Company surcharge:** 7% (TI > ₹1 cr), 12% (TI > ₹10 cr).

**Individual new-regime slabs (AY 25-26):** Nil ≤3L; 5% 3-7L; 10% 7-10L; 15% 10-12L; 20% 12-15L; 30% >15L. **87A rebate** up to ₹7L → tax nil.

**Advance tax:** 15% Jun · 45% Sep · 75% Dec · 100% Mar.

**Interest:** 234A (late filing), 234B (< 90% paid), 234C (instalment shortfall) — all **1% p.m.**

**Key sections:** 40(a)(ia) TDS disallowance · 43B statutory dues on payment · 115JB MAT · 115JAA MAT credit (15 yrs) · 115BAA company concessional · 115BAC individual new regime · 140A self-assessment · 288A round-off.

**Forms:** ITR-6 (company) · ITR-3 (business individual) · ITR-2 (no business) · Form 26AS + AIS (reconcile before filing).
