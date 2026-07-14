# Deferred Tax, Provisions, Employee Benefits & Key GAAP/IFRS Differences

## What you'll be able to do
Build and defend a deferred-tax working (DTA/DTL) from a fixed-asset temporary difference, recognise and measure a provision under Ind AS 37 / IAS 37, split a warranty vs a contingent liability, do a basic Ind AS 19 / IAS 19 employee-benefit computation (gratuity/leave, current service cost, actuarial gains through OCI), and answer the classic "how does US GAAP differ from IFRS here?" question across the topics an Indian GCC or reporting team touches daily. You will produce the journal entries, the tax-reconciliation note, and a movement schedule that a reviewer or auditor can tie out.

## The essentials

**Deferred tax (Ind AS 12 / IAS 12) — balance-sheet / temporary-difference method.** Tax is not booked on accounting profit; you book *current tax* (per the return) plus *deferred tax* on **temporary differences** = carrying amount of an asset/liability minus its **tax base**.
- Taxable temporary difference → **DTL** (you'll pay more tax later). Classic cause: book depreciation < tax depreciation (asset carrying value > tax WDV).
- Deductible temporary difference → **DTA** (you'll pay less later). Causes: provisions disallowed until paid (40(a), gratuity u/s 43B), carry-forward losses, unabsorbed depreciation.
- **Measure at the tax rate expected when the difference reverses** (enacted/substantively enacted). In India use the rate you've opted for — e.g. **25.168%** under the 115BAA concessional regime (22% + 10% surcharge + 4% cess).
- DTA recognised only to the extent **future taxable profit is probable**. Losses need "convincing evidence."
- **No discounting** of deferred tax. Never.

**Provisions & contingencies (Ind AS 37 / IAS 37).** A **provision** (liability of uncertain timing/amount) is recognised when **all three** hold: (a) a **present obligation** (legal or constructive) from a past event; (b) outflow **probable** (>50%); (c) a **reliable estimate**. Measure at **best estimate** — for a large population use expected value; for a single item use the most likely outcome. **Discount** if the time-value effect is material (unlike deferred tax). A **contingent liability** (obligation only possible, or not reliably measurable) is **disclosed, not booked**. A **contingent asset** is disclosed only when inflow is probable; recognised only when virtually certain. No provisions for **future operating losses**; onerous contracts *are* provided.

**Employee benefits (Ind AS 19 / IAS 19).**
- *Short-term* (salary, bonus, leave expected to be settled within 12 months): booked undiscounted as incurred.
- *Defined contribution* (PF, NPS): expense = contribution. No further liability.
- *Defined benefit* (gratuity, pension): actuarial. Book the **net defined benefit liability** = PV of obligation (DBO) − plan assets. P&L takes **current service cost + net interest** (net interest = discount rate × opening net liability). **Remeasurements** (actuarial gains/losses, return on plan assets above interest) go to **OCI and are never recycled** to P&L.

## Hands-on — step by step

**Worked deferred tax — fixed asset.** Buy a machine for ₹100,00,000 on 1-Apr-2025.
- Books: straight-line over 10 years → depreciation ₹10,00,000/yr → carrying value 31-Mar-2026 = **₹90,00,000**.
- Tax: WDV block @ 15% → tax depreciation ₹15,00,000 → tax WDV = **₹85,00,000**.
- Temporary difference = 90,00,000 − 85,00,000 = **₹5,00,000** (carrying > tax base → **taxable** → DTL).
- Tax rate 25.168%. **DTL = 5,00,000 × 25.168% = ₹1,25,840.**
- Entry: **Dr Deferred Tax Expense (P&L) 1,25,840 / Cr Deferred Tax Liability 1,25,840.**

Add a deductible item: a gratuity provision of ₹8,00,000 expensed in books but disallowed for tax until paid (43B) → deductible temporary difference → **DTA = 8,00,000 × 25.168% = ₹2,01,344**. Entry: **Dr DTA 2,01,344 / Cr Deferred Tax Income (P&L) 2,01,344.** Net deferred position this year = DTA 2,01,344 − DTL 1,25,840 = **net DTA ₹75,504**.

**Tax reconciliation (rate reconciliation note).** Say accounting profit before tax = ₹50,00,000. Expected tax @ 25.168% = ₹12,58,400. Add tax effect of permanent disallowance (say CSR ₹2,00,000 × 25.168% = ₹50,336). Effective tax expense ≈ ₹13,08,736; ETR ≈ 26.17%. This note must reconcile "tax at statutory rate" to "actual tax expense" — reviewers check it first.

**Worked provision — warranty.** You sell 10,000 units in FY26. History: 4% need minor repair (₹200 each), 1% major (₹1,500 each). Expected value = (10,000×4%×200) + (10,000×1%×1,500) = 80,000 + 1,50,000 = **₹2,30,000**. Entry: **Dr Warranty Expense 2,30,000 / Cr Provision for Warranty 2,30,000.** A separate ₹40,00,000 tax dispute where you expect to *win* (outflow possible, not probable) is a **contingent liability — disclose only**.

**Worked employee benefit — gratuity (defined benefit).**
- Opening DBO ₹40,00,000; opening plan assets ₹30,00,000 → opening net liability ₹10,00,000.
- Discount rate 7.2% (G-sec benchmark). **Current service cost** (from actuary) ₹4,50,000.
- **Net interest** = 7.2% × 10,00,000 = ₹72,000. → **P&L charge = 4,50,000 + 72,000 = ₹5,22,000.**
- Actuary reports experience/assumption loss of ₹1,20,000 → **remeasurement to OCI**, not P&L.
- Benefits paid ₹2,00,000; employer contribution ₹5,00,000.
- Closing net liability = 10,00,000 + 5,22,000 + 1,20,000(OCI) − 5,00,000 = **₹11,42,000**.

## The output

**Deferred tax movement schedule (₹):**

| Item | Carrying | Tax base | Temp diff | DTA/(DTL) @25.168% |
|---|---|---|---|---|
| Machine | 90,00,000 | 85,00,000 | 5,00,000 | (1,25,840) |
| Gratuity prov. | 8,00,000 | 0 | 8,00,000 | 2,01,344 |
| **Net** | | | | **75,504 DTA** |

**Defined-benefit reconciliation (₹):** Opening net liability 10,00,000 → +CSC 4,50,000 → +Net interest 72,000 → +Remeasurement (OCI) 1,20,000 → −Contributions 5,00,000 → **Closing 11,42,000**. P&L 5,22,000; OCI 1,20,000.

## US GAAP vs IFRS — consolidated differences

| Topic | IFRS / Ind AS | US GAAP |
|---|---|---|
| Inventory | FIFO/weighted avg; **LIFO banned**; write-downs reversible | LIFO allowed; write-downs **not** reversible |
| Fixed assets | Cost **or revaluation** model; component depreciation | Cost model only (no revaluation) |
| Dev. costs | Capitalise if criteria met (IAS 38) | Expense R&D (except software ASC 985/350) |
| Impairment | One-step, recoverable amt; **reversals allowed** (not goodwill) | Two-step legacy; **no reversals** |
| Leases (lessee) | Single model, ROU asset (IFRS 16) | Dual: finance vs operating (ASC 842) |
| Deferred tax | All non-current; no discounting | All non-current; valuation allowance approach |
| DB remeasurements | OCI, **never recycled** | OCI, amortised (corridor) into P&L |
| Provisions | "Probable" = >50%; discount if material | "Probable" ~ higher threshold (~75-80%) |
| Extraordinary items | Prohibited | Prohibited (removed 2015) |

## Checks, gotchas & red flags
- **DTA and DTL are netted only within the same tax jurisdiction/entity.** Don't offset an Indian DTA against a US DTL.
- Deferred tax is **never discounted** — but provisions **are** if material. Candidates swap these.
- Revaluation surplus and OCI-routed items carry deferred tax to **OCI**, not P&L (backwards-tracing).
- DTA on losses without "convincing evidence" of future profit is a classic overstatement red flag.
- Remeasurements to OCI must **not** be recycled under IFRS; if you see them hitting P&L next year, it's an error (or it's US GAAP corridor).
- Contingent asset booked before virtually certain = overstated income.

## Interview drill
**Q1. Book depreciation is lower than tax depreciation — DTA or DTL?** Asset carrying value exceeds tax WDV, so there's a *taxable* temporary difference — you've claimed more tax relief now and will pay more later. That's a **DTL**. Reverse the logic for a provision disallowed till paid (DTA).

**Q2. Where do actuarial gains/losses on a gratuity plan go, and do they ever hit P&L?** Under Ind AS 19 / IAS 19 they're **remeasurements booked to OCI** and are **never reclassified to P&L**. Only current service cost, past service cost, and net interest go through P&L. (US GAAP amortises them via the corridor — a key difference.)

**Q3. Name three IFRS vs US GAAP differences that change reported profit.** LIFO (US allows, IFRS bans — hits COGS/inventory); impairment reversals (IFRS allows for non-goodwill assets, US never); and development-cost capitalisation (IFRS capitalises if criteria met, US expenses R&D). Each moves both the P&L and the balance sheet.

## Learn/practise (free)
- **MCA Ind AS text** (mca.gov.in) and **IFRS Foundation** free-to-read standards summaries — read IAS 12, 37, 19 side by side.
- **ICAI Study Material** (Advanced Accounting / Financial Reporting) — free PDFs with solved deferred-tax and gratuity problems.
- Rehearse in **Excel**: build the temporary-difference table, a DB reconciliation roll-forward, and a rate reconciliation. Feed it real numbers from any listed company's Note on Income Taxes (e.g. Infosys, TCS annual report) and re-derive their ETR — best free practice there is.
- **KPMG / EY / PwC "IFRS vs US GAAP" comparison PDFs** — free, authoritative, and the exact table interviewers quiz from.
