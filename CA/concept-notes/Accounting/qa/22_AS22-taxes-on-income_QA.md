# Q&A — AS 22 — Accounting for Taxes on Income

---

## Section A — Concept-check Questions (test the WHY)

**A1. Why does the "naive" method of charging only the tax actually payable to the P&L violate the matching principle?**
The naive (taxes-payable) method reports as tax expense only the tax legally payable on the *taxable* income of the year. But the P&L reports *accounting* income. When accounting income and taxable income differ because of **timing differences** (e.g. tax depreciation exceeds book depreciation early in an asset's life), the reported tax expense no longer matches the pre-tax accounting profit it relates to. Profit is **overstated today** (low tax charged) and **understated tomorrow** (high tax when the difference reverses). AS 22 fixes this by recognising the tax effect of income and expenses in the *same period* those items are recognised in the accounts.

**A2. Distinguish permanent differences from timing differences. Which one creates deferred tax and why?**
- **Timing difference**: originates in one period and is **capable of reversal** in one or more subsequent periods (e.g. depreciation, s.43B disallowances like bonus/PF paid later, provision for doubtful debts allowed on write-off). Only these create **deferred tax**, because the reversal is the future tax consequence AS 22 must accrue now.
- **Permanent difference**: originates and **never reverses** (e.g. disallowed donations/penalties, agricultural income exempt, tax-free dividends). It has **no deferred tax**; it only makes the effective tax rate differ from the statutory rate.

**A3. State the fundamental AS 22 equation and explain each term.**
`Tax Expense = Current Tax + Deferred Tax`.
- **Current tax** = tax payable on the taxable income of the period as per the Income-tax Act.
- **Deferred tax** = tax effect (at enacted/substantively-enacted rates) of **timing differences** — the DTL created/reversed or DTA created/reversed during the period. It is the balancing charge that makes total tax expense proportionate to accounting profit (adjusted only for permanent differences).

**A4. Why is a Deferred Tax Liability recognised unconditionally, but a Deferred Tax Asset only conditionally?**
This is the **prudence asymmetry**. A DTL is a future tax *outflow* that is virtually assured, so it is always recognised (no risk of overstating assets). A DTA represents a future tax *saving* that materialises only if there are future taxable profits to absorb it — an uncertain benefit. To avoid overstating assets/profits, AS 22 requires that a DTA be recognised only when there is **reasonable certainty** of sufficient future taxable income; a higher **virtual certainty supported by convincing evidence** is required where the DTA arises from **unabsorbed depreciation or carry-forward of losses** under tax law.

**A5. Should deferred tax balances be discounted to present value?**
**No.** AS 22 expressly **prohibits discounting** of deferred tax assets and liabilities. The timing of reversal is often uncertain and a detailed scheduling of reversals across years would be impracticable; the standard opts for measurement at undiscounted amounts using enacted rates.

**A6. Why is depreciation the "flagship" source of deferred tax in India?**
Because almost every company has a systematic, recurring gap between **book depreciation** (AS 10 / Sch II — often SLM, useful-life based) and **tax depreciation** (WDV block-of-assets rates under the Income-tax Act, often accelerated). This generates a large, predictable timing difference that originates early (tax dep > book dep → DTL) and reverses later, present in virtually all asset-owning entities.

**A7. When tax rates change, how are existing deferred tax balances treated?**
Existing DTA/DTL must be **re-measured** using the **newly enacted/substantively enacted rate** applicable to the period of reversal. The adjustment to the carrying amount is generally charged/credited to the **P&L** in the period of the rate change (unless it relates to items taken directly to reserves).

**A8. Is MAT credit a deferred tax asset under AS 22?**
No. **MAT (s.115JB)** credit is *not* a timing difference and is outside AS 22's deferred-tax mechanics. Per the ICAI Guidance Note, MAT credit entitlement is recognised as an **asset ("MAT Credit Entitlement")** only when there is reasonable/convincing evidence that the company will pay normal tax during the credit-carry-forward period and thereby utilise it; it is reviewed each year.

---

## Section B — Graded Computational Problems

### B1 (Easy) — Permanent + one timing difference

**Data.** Accounting profit before tax = ₹10,00,000. It is after debiting a donation of ₹50,000 that is **wholly disallowed** under tax law (permanent). Book depreciation = ₹1,00,000; tax depreciation = ₹1,50,000. Tax rate = 25%.

**Solution.**
Taxable income = 10,00,000 + 50,000 (donation added back) − 50,000 (extra tax depn) = **₹10,00,000**.
Current tax @25% = **₹2,50,000**.
Timing difference (tax dep > book dep) = 50,000 → originating → **DTL created** = 50,000 × 25% = **₹12,500**.
Tax expense = 2,50,000 + 12,500 = **₹2,62,500**.

*Reconciliation:* 25% × (accounting profit + permanent diff) = 25% × (10,00,000 + 50,000) = 2,62,500. ✓ Effective rate 26.25% (deviation entirely due to the permanent donation).

**Journal entry**
```
Tax Expense (P&L)                 Dr  2,62,500
   To Provision for Current Tax          2,50,000
   To Deferred Tax Liability               12,500
```

---

### B2 (Moderate) — Full DTL life-cycle (depreciation), normalising to statutory rate

**Data.** Asset cost ₹15,00,000, life 3 years. Book depreciation SLM = ₹5,00,000 p.a. Tax depreciation = ₹7,50,000 / ₹5,00,000 / ₹2,50,000 in Years 1–3. Profit **before depreciation** = ₹10,00,000 each year. Tax rate = 30% throughout.

**Working table (₹)**

| | Yr 1 | Yr 2 | Yr 3 | Total |
|---|---|---|---|---|
| Profit before depn | 10,00,000 | 10,00,000 | 10,00,000 | 30,00,000 |
| Book depn | 5,00,000 | 5,00,000 | 5,00,000 | 15,00,000 |
| **Accounting profit (PBT)** | **5,00,000** | **5,00,000** | **5,00,000** | **15,00,000** |
| Tax depn | 7,50,000 | 5,00,000 | 2,50,000 | 15,00,000 |
| **Taxable income** | **2,50,000** | **5,00,000** | **7,50,000** | **15,00,000** |
| Timing diff (tax−book depn) | +2,50,000 | 0 | −2,50,000 | 0 |
| Current tax @30% | 75,000 | 1,50,000 | 2,25,000 | 4,50,000 |
| Deferred tax (DTL Δ) @30% | +75,000 | 0 | −75,000 | 0 |
| **Total tax expense** | **1,50,000** | **1,50,000** | **1,50,000** | **4,50,000** |
| Closing DTL balance | 75,000 | 75,000 | 0 | — |

**Observations.** Each year's tax expense = 30% × PBT = ₹1,50,000, exactly. The DTL builds up in Year 1 (tax dep faster), stays flat in Year 2 (no difference), and fully **reverses** in Year 3 when book dep exceeds tax dep. Over the asset's life cumulative timing difference = 0, so cumulative deferred tax = 0. Total tax over 3 years = ₹4,50,000 = 30% × ₹15,00,000. ✓

**Journal entries**
```
Yr 1:  Tax Expense              Dr 1,50,000
          To Provision for Current Tax    75,000
          To Deferred Tax Liability       75,000
Yr 2:  Tax Expense              Dr 1,50,000
          To Provision for Current Tax  1,50,000
Yr 3:  Tax Expense              Dr 1,50,000
       Deferred Tax Liability   Dr   75,000
          To Provision for Current Tax  2,25,000
```

---

### B3 (Exam-hard) — DTA with virtual-certainty gate, then rate change

**Data.** In Year 1 a company incurs a **book/business loss** and has a **carry-forward tax loss (incl. unabsorbed depreciation) of ₹8,00,000**. Tax rate 25%. At end of Year 1 management has *convincing evidence* (signed export contracts, order book) of future taxable profit — **virtual certainty** established. In Year 2 the company earns taxable profit of ₹8,00,000 before set-off and the entire loss is absorbed. Show the deferred tax treatment. Also, suppose instead that at the start of Year 2 the enacted tax rate falls to **22%**; show the re-measurement.

**Solution — base case.**
Year 1: DTA arises from carry-forward loss = 8,00,000 × 25% = **₹2,00,000**. Because it stems from unabsorbed depreciation/carry-forward loss, recognition requires **virtual certainty supported by convincing evidence** — satisfied here, so recognise.
```
Yr 1:  Deferred Tax Asset       Dr 2,00,000
          To Tax Expense (deferred tax credit) 2,00,000
```
Year 2: The loss is set off against ₹8,00,000 taxable profit, so no current tax is payable on that slice, but the timing difference **reverses** — the DTA is consumed:
```
Yr 2:  Tax Expense (deferred)   Dr 2,00,000
          To Deferred Tax Asset            2,00,000
```
Net effect: the ₹2,00,000 tax benefit was recognised in Year 1 (the year of the loss), matching the accounting loss — exactly what AS 22 intends. Closing DTA = 0.

**Solution — rate-change variant (rate 25% → 22% at start of Year 2, loss still unabsorbed).**
The DTA of ₹2,00,000 was measured at 25%. It must be **re-measured** at the new enacted 22%:
New DTA = 8,00,000 × 22% = **₹1,76,000**. Reduction = 2,00,000 − 1,76,000 = **₹24,000**, charged to P&L.
```
Tax Expense (deferred)     Dr 24,000
   To Deferred Tax Asset          24,000
```

**Prudence review note.** If at any subsequent balance-sheet date the future taxable income no longer appears virtually certain, the carrying amount of the DTA must be **written down** (and reversed later if certainty is restored).

---

### B4 (Exam-hard) — Multiple timing differences + permanent difference, net balance

**Data (Year end).** Accounting PBT = ₹20,00,000, arrived at after: (i) provision for doubtful debts ₹1,20,000 (allowed for tax only on actual write-off — timing); (ii) interest on income-tax ₹40,000 (permanently disallowed); (iii) book depreciation ₹3,00,000 vs tax depreciation ₹4,50,000. Opening DTL = ₹90,000. Tax rate = 30%.

**Solution.**
Taxable income:
```
Accounting PBT                           20,00,000
Add: Prov. doubtful debts (disallowed)    1,20,000
Add: Interest on income-tax (permanent)     40,000
Add: Book depn                            3,00,000
Less: Tax depn                          (4,50,000)
Taxable income                           20,10,000
```
Current tax @30% = **₹6,03,000**.

Deferred tax movement (timing differences only):
- Doubtful-debts provision: originating timing diff +1,20,000 → creates **DTA** 1,20,000 × 30% = 36,000 (deductible in future). Recognise (reasonable certainty — ordinary timing difference; assume future profits available).
- Depreciation: tax dep > book dep by 1,50,000 → originating → **DTL** 1,50,000 × 30% = 45,000.

Net deferred tax charge to P&L = DTL created 45,000 − DTA created 36,000 = **₹9,000 (net expense)**.
Closing net DTL = opening 90,000 + 45,000 − 36,000 = **₹99,000**.

Tax expense = 6,03,000 + 9,000 = **₹6,12,000**.

*Reconciliation:* 30% × (PBT + permanent diff) = 30% × (20,00,000 + 40,000) = 30% × 20,40,000 = ₹6,12,000. ✓

**Presentation caution (netting rule).** The DTA (₹36,000) and DTL (₹45,000) here relate to the **same taxable entity and same tax jurisdiction**, so they are presented **net** — a single non-current DTL of ₹99,000. DTA and DTL of *different* entities/jurisdictions must **not** be set off.

**Journal entry**
```
Tax Expense              Dr 6,12,000
Deferred Tax Asset       Dr    36,000
   To Provision for Current Tax   6,03,000
   To Deferred Tax Liability         45,000
```

---

## Section C — Past-paper-style Full Questions (ICAI pattern)

**C1.** *Sun Ltd. has a book profit of ₹12,00,000 for the year. It includes ₹2,00,000 dividend from a domestic company (exempt) and ₹75,000 penalty for law violation (disallowed). Depreciation as per books is ₹5,00,000 and as per Income-tax Act ₹7,00,000. Opening Deferred Tax Liability ₹60,000. Tax rate 25%. Compute current tax, deferred tax and tax expense, and pass the journal entry. Also state the net deferred tax to be shown in the Balance Sheet.*

**Model answer.**
Taxable income:
```
Book profit                              12,00,000
Less: Exempt dividend (permanent)        (2,00,000)
Add: Penalty (permanent, disallowed)        75,000
Add: Book depn                            5,00,000
Less: Tax depn                          (7,00,000)
Taxable income                            8,75,000
```
Current tax @25% = **₹2,18,750**.
Timing difference = tax dep − book dep = 2,00,000 (originating) → DTL created = 2,00,000 × 25% = **₹50,000**.
Deferred tax expense = ₹50,000; Tax expense = 2,18,750 + 50,000 = **₹2,68,750**.
Closing DTL (Balance Sheet, non-current) = 60,000 + 50,000 = **₹1,10,000**.

*Reconciliation:* 25% × (12,00,000 − 2,00,000 + 75,000) = 25% × 10,75,000 = ₹2,68,750. ✓
```
Tax Expense             Dr 2,68,750
   To Provision for Current Tax  2,18,750
   To Deferred Tax Liability        50,000
```

**C2.** *Moon Ltd. reports a carry-forward business loss of ₹10,00,000 and unabsorbed depreciation of ₹4,00,000 at year-end. The company has only just started operations and has no firm evidence of future profits, though it "expects" to turn profitable. Tax rate 30%. Advise on deferred tax asset recognition with reasons.*

**Model answer.**
The potential DTA = (10,00,000 + 4,00,000) × 30% = ₹4,20,000. But because it arises from **carry-forward loss and unabsorbed depreciation**, AS 22 permits recognition **only if virtual certainty supported by convincing evidence** exists that sufficient future taxable income will be available. A mere expectation of profitability, especially for a company that has *just started* with no order book, contracts, or reliable projections, does **not** meet the virtual-certainty test. Therefore **no DTA should be recognised**. The position must be **re-assessed at each balance-sheet date**; the DTA can be recognised in a later year once convincing evidence emerges. (Contrast: ordinary timing differences need only *reasonable* certainty.)

**C3.** *Explain, with an example, how a change in the enacted tax rate is accounted for under AS 22, and why it does not affect current tax of prior years.*

**Model answer.**
Deferred tax measures the future tax effect of timing differences and must use the **rate expected to apply when the difference reverses** — i.e., the newly **enacted/substantively enacted** rate. When the rate changes, **existing DTA/DTL are re-measured** at the new rate and the difference is taken to the **P&L** in the year of change. It does **not** disturb prior-year current tax, because current tax of a past year was correctly computed on that year's taxable income at the then-applicable rate and is final; only the *future* reversal — which is what deferred tax represents — is re-priced.
*Example:* Cumulative timing difference ₹4,00,000, DTL at old 30% = ₹1,20,000. Rate falls to 25% → new DTL = ₹1,00,000. Write back ₹20,000 to P&L:
```
Deferred Tax Liability   Dr 20,000
   To Tax Expense (deferred tax credit)  20,000
```

---

## Section D — MCQs / Case Scenarios

**D1.** Which item creates deferred tax?
(a) Disallowed penalty (b) Exempt agricultural income (c) Excess of tax depreciation over book depreciation (d) Tax-free interest.
**Answer: (c).** Only depreciation timing difference reverses; the others are permanent.

**D2.** A DTA arising from carry-forward business losses is recognised only when there is:
(a) Reasonable certainty (b) Virtual certainty supported by convincing evidence (c) Mere probability (d) Board approval.
**Answer: (b).** Loss/unabsorbed-depreciation DTAs require the higher virtual-certainty threshold.

**D3.** Deferred tax balances under AS 22 are:
(a) Discounted at 8% (b) Discounted at the risk-free rate (c) Not discounted (d) Discounted only if reversal exceeds 5 years.
**Answer: (c).** AS 22 prohibits discounting.

**D4.** In the Balance Sheet (Schedule III), a net deferred tax liability is shown under:
(a) Current liabilities (b) Non-current liabilities (c) Reserves & surplus (d) Contingent liabilities.
**Answer: (b).** DTA/DTL are always **non-current**, shown at the net figure per entity/jurisdiction.

**D5.** Tax rate rises from 25% to 30%; existing DTL of ₹50,000 (on a ₹2,00,000 timing difference) is re-measured to:
(a) ₹50,000 (b) ₹60,000, extra ₹10,000 to P&L (c) ₹40,000 (d) No change till reversal.
**Answer: (b).** ₹2,00,000 × 30% = ₹60,000; the ₹10,000 increase is charged to P&L now.

**D6.** MAT credit entitlement under s.115JB is:
(a) A deferred tax asset under AS 22 (b) A permanent difference (c) An asset recognised per ICAI Guidance Note when utilisation is reasonably/convincingly certain (d) Never recognised.
**Answer: (c).** MAT credit is outside AS 22's deferred-tax scope; it follows the Guidance Note.

**D7.** *Case.* A company nets a DTA of Subsidiary X against a DTL of Subsidiary Y (separate assessees) in the consolidated balance sheet.
**Verdict:** **Incorrect.** DTA and DTL may be set off only for the **same taxable entity and same tax jurisdiction**; different assessees cannot be netted.

**D8.** *Case.* Interest on borrowings ₹1,00,000 is capitalised as part of PPE cost in the books but fully deducted for tax in the year incurred.
**Answer:** This is a **timing difference** (book cost recovered via future depreciation vs immediate tax deduction) → gives rise to a **DTL**. Reasoning: the future book depreciation of the capitalised interest will be non-deductible for tax, reversing the difference.

---

*Master check for any AS 22 problem:* (1) Split book–tax differences into **permanent** (ignore for deferred tax) vs **timing** (create/reverse DTA-DTL). (2) Current tax on **taxable** income. (3) Deferred tax on **timing** differences at **enacted** rates, **no discounting**. (4) Apply the **DTA recognition gate** (reasonable vs virtual certainty). (5) Re-measure on **rate change**; **review** DTA each year. (6) Present **net, non-current**. (7) Confirm **Tax Expense ÷ (PBT + permanent diff) = statutory rate**.
