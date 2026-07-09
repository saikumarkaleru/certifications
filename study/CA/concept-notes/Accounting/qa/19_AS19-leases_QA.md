# Q&A — AS 19 — Leases

> Companion question bank to the concept chapter. Every question is followed immediately by its full model answer. All computations are self-reconciled. Currency: Indian Rupees (₹). Standard: AS 19 (ICAI).

---

## Section A — Concept-check questions (test the WHY)

**A1. Why does AS 19 exist at all — what abuse was it built to stop?**
Before lease accounting rules, a company could obtain the full economic use of an asset on long-term instalments yet keep both the asset and the matching liability *off* its balance sheet, disclosing only rent. This understated gearing and overstated return on assets — "off-balance-sheet financing." AS 19 forces a lease that is, in substance, a purchase-on-EMI to be shown as an asset and a borrowing. It is an application of **substance over form**.

**A2. State the single decisive test for classifying a lease and name the five indicators.**
Decisive test: **does the lease transfer substantially all the risks and rewards incident to ownership?** If yes → *finance lease*; if not → *operating lease*. Classification is at inception and does not change over the term (except on renegotiation). Five indicators that normally point to a finance lease:
1. Ownership transfers to the lessee by the end of the term.
2. Lessee has a bargain purchase option (price expected to be well below fair value).
3. Lease term is for the **major part** of the asset's economic life.
4. PV of minimum lease payments (MLP) at inception ≥ **substantially all** of the asset's fair value.
5. The leased asset is so specialised that only the lessee can use it without major modification.

**A3. Why must escalating rentals under an operating lease normally be straight-lined?**
The lessee enjoys a broadly even benefit (use of the asset) across the term; loading more expense into later years merely because the contract back-loads cash does not reflect the *time pattern of the user's benefit*. AS 19 therefore requires recognition on a **straight-line basis** over the lease term unless another systematic basis is more representative of the benefit pattern. The timing difference is parked as prepaid rent (asset) or accrued rent (liability).

**A4. Why is a lease of *land* usually an operating lease?**
Land normally has an **indefinite economic life**. If ownership is not expected to pass to the lessee by the end of the term, the lessee never receives substantially all the rewards (residual value at term-end can be enormous), so risks and rewards are *not* transferred — hence operating. For land-and-building leases, the two elements are assessed separately, splitting rentals by relative fair value of the leasehold interests.

**A5. Distinguish gross investment, net investment and unearned finance income (lessor, finance lease).**
- **Gross investment** = MLP receivable by the lessor **+** any unguaranteed residual value accruing to the lessor.
- **Net investment** = gross investment discounted at the **interest rate implicit in the lease** (equals fair value/cost at inception).
- **Unearned finance income** = gross investment − net investment. It is recognised as income over the term to give a **constant periodic rate of return on the net investment**.

**A6. What is the "interest rate implicit in the lease"?**
The discount rate that, at inception, makes the **aggregate PV of (MLP + unguaranteed residual value) equal to the fair value of the leased asset** (adjusted for lessor's initial direct costs). The lessee uses it to discount MLP; if not determinable, the lessee uses its **incremental borrowing rate**.

**A7. In a sale-and-leaseback that results in an operating lease, how is a "profit" on sale treated?**
If sale price = fair value → recognise profit/loss immediately. If sale price **above** fair value → the excess is **deferred and amortised** over the lease term (it is really a rent subsidy, not a gain). If sale price **below** fair value → recognise loss immediately, unless compensated by below-market future rentals, in which case defer and amortise. (If the leaseback is a *finance* lease, any excess of sale proceeds over carrying amount is deferred and amortised over the lease term.)

---

## Section B — Graded computational problems

### B1 (Easy) — Operating lease with escalating rent (straight-lining)

A company takes premises on a 4-year operating lease. Annual rentals payable at year-end, escalating 10% p.a.: Year 1 ₹1,00,000; Year 2 ₹1,10,000; Year 3 ₹1,21,000; Year 4 ₹1,33,100. Compute the annual expense and the accrual movement.

**Solution.**
Total rent = 1,00,000 + 1,10,000 + 1,21,000 + 1,33,100 = **₹4,64,100**.
Straight-line expense = 4,64,100 ÷ 4 = **₹1,16,025 p.a.**

| Year | SL expense | Cash paid | Movement in accrued rent | Closing accrued rent (liability) |
|---|---|---|---|---|
| 1 | 1,16,025 | 1,00,000 | +16,025 | 16,025 |
| 2 | 1,16,025 | 1,10,000 | +6,025 | 22,050 |
| 3 | 1,16,025 | 1,21,000 | −4,975 | 17,075 |
| 4 | 1,16,025 | 1,33,100 | −17,075 | 0 |

Reconciliation: cumulative expense 4×1,16,025 = 4,64,100 = cumulative cash paid. Closing accrual returns to zero. ✔

Journal (Year 1): Rent A/c Dr 1,16,025 / To Bank 1,00,000 / To Rent payable (accrued) 16,025.

### B2 (Moderate) — Lessee finance lease: full amortisation + depreciation

A machine (fair value = PV of MLP = ₹2,48,685) is taken on a 3-year finance lease; annual lease rentals ₹1,00,000 payable at each year-end; interest rate implicit in the lease **10%**. Useful life 3 years, no residual, ownership not transferred. Show the finance-charge allocation, depreciation, and Year-1 entries.

**Solution — leased liability amortisation (actuarial method):**

| Year | Opening liability | Interest @10% | Rental paid | Principal repaid | Closing liability |
|---|---|---|---|---|---|
| 1 | 2,48,685 | 24,869 | 1,00,000 | 75,131 | 1,73,554 |
| 2 | 1,73,554 | 17,355 | 1,00,000 | 82,645 | 90,909 |
| 3 | 90,909 | 9,091 | 1,00,000 | 90,909 | 0 |

Check: total interest 24,869 + 17,355 + 9,091 = **51,315**; total rentals 3,00,000 − principal 2,48,685 = 51,315. ✔ (Year 3 interest taken as balancing figure to clear the liability.)

**Depreciation** (shorter of lease term / useful life = 3 yrs): 2,48,685 ÷ 3 = **₹82,895 p.a.**

**Year-1 journals:**
- At inception: Machinery (leased asset) A/c Dr 2,48,685 / To Lessor (lease liability) 2,48,685.
- Interest: Finance charges A/c Dr 24,869 / To Lessor 24,869.
- Payment: Lessor A/c Dr 1,00,000 / To Bank 1,00,000.
- Depreciation: Depreciation A/c Dr 82,895 / To Machinery 82,895.

Year-1 P&L charge = interest 24,869 + depreciation 82,895 = **₹1,07,764** (front-loaded, unlike straight-line rent).

### B3 (Exam-hard) — Lessor finance lease with unguaranteed residual value

A finance company leases equipment. Lease term 3 years; annual lease payment ₹3,50,000 receivable at each year-end; **unguaranteed** residual value at term-end ₹1,00,000; interest rate implicit in the lease **7%** (given). PV factors @7%: Y1 0.9346, Y2 0.8734, Y3 0.8163; 3-yr annuity factor 2.6243. Compute gross investment, net investment, unearned finance income, and the income-recognition schedule.

**Solution.**
- **Gross investment** = MLP + unguaranteed RV = (3 × 3,50,000) + 1,00,000 = 10,50,000 + 1,00,000 = **₹11,50,000**.
- **Net investment (PV @7%)** = MLP PV + RV PV = (3,50,000 × 2.6243) + (1,00,000 × 0.8163) = 9,18,505 + 81,630 = **₹10,00,135** (= cost/fair value of asset).
- **Unearned finance income** = 11,50,000 − 10,00,135 = **₹1,49,865**.

**Income allocation (constant 7% return on net investment):**

| Year | Opening net investment | Finance income @7% | Receipt | Capital recovered | Closing net investment |
|---|---|---|---|---|---|
| 1 | 10,00,135 | 70,009 | 3,50,000 | 2,79,991 | 7,20,144 |
| 2 | 7,20,144 | 50,410 | 3,50,000 | 2,99,590 | 4,20,554 |
| 3 | 4,20,554 | 29,446 | 3,50,000 | 3,20,554 | 1,00,000 |

Reconciliation: closing balance after Year 3 = ₹1,00,000 = unguaranteed residual value recovered on asset return/sale. ✔ Total finance income 70,009 + 50,410 + 29,446 = ₹1,49,865 = unearned finance income. ✔ (Year-3 income taken as balancing figure to absorb rounding.)

At inception the lessor **derecognises the asset** and records: Lease receivable (gross) Dr 11,50,000 / To Equipment 10,00,135 / To Unearned finance income 1,49,865. Each year, unearned income is transferred to P&L per the table.

### B4 (Judgement) — Classification test

An asset with fair value ₹10,00,000 and economic life 6 years is leased for 5 years; PV of MLP at inception = ₹9,40,000; no ownership transfer, no bargain option. Classify.

**Solution.** Apply indicators: lease term (5) = major part of life (6) → points to finance. PV of MLP 9,40,000 = **94%** of fair value → "substantially all" fair value → finance. Two strong indicators satisfied ⇒ **finance lease**, notwithstanding no legal ownership transfer. Substance (risks/rewards transferred) overrides form. The lessee capitalises the asset at the **lower of fair value and PV of MLP = ₹9,40,000**.

---

## Section C — Past-paper-style full questions (ICAI pattern)

**C1.** *X Ltd. leased a machine to Y Ltd. on the following terms (₹ in lakhs): fair value 20.00; lease term 5 years; guaranteed residual value 0.40; expected residual value 1.00; internal rate of return 15%; depreciation on SLM at 10% p.a. Ascertain the unearned finance income.* (ICAI-style.)

**Model answer.**
Annual lease rental is derived so that PV of (5 rentals + expected RV 1.00) @15% = fair value 20.00. Annuity factor @15%, 5 yrs = 3.3522; PV factor Y5 = 0.4972.
PV of expected residual = 1.00 × 0.4972 = 0.4972.
PV to be covered by rentals = 20.00 − 0.4972 = 19.5028.
Annual rental = 19.5028 ÷ 3.3522 = **5.818** (≈ ₹5.82 lakh).

- **Gross investment** = (5 × 5.818) + expected RV 1.00 = 29.09 + 1.00 = **30.09**.
- **Net investment** = fair value = **20.00**.
- **Unearned finance income** = Gross − Net = 30.09 − 20.00 = **₹10.09 lakh**.

(Note: the *guaranteed* portion 0.40 is part of MLP for the lessee; the lessor uses total expected RV 1.00 in gross investment. Unearned finance income is spread over 5 years at a constant 15% return on the declining net investment.)

**C2.** *A Ltd. sold machinery (carrying amount ₹8,00,000) to a leasing company for ₹9,50,000 (fair value ₹9,00,000) and leased it back under an operating lease. How is the transaction accounted?*

**Model answer.** This is a **sale and leaseback resulting in an operating lease**. Compare sale price with fair value:
- Sale price ₹9,50,000 **exceeds** fair value ₹9,00,000 by ₹50,000. This excess over fair value is **deferred and amortised** over the lease term (it is a prepayment of rent by the lessor, not real profit).
- The remaining gain = fair value 9,00,000 − carrying amount 8,00,000 = **₹1,00,000**, recognised **immediately** in P&L.

Entry: Bank Dr 9,50,000 / To Machinery 8,00,000 / To Profit on sale (P&L) 1,00,000 / To Deferred income 50,000. The ₹50,000 deferred income is released to P&L over the lease term (reducing rent expense).

**C3.** *Explain the disclosure requirements for a lessee under a finance lease.*

**Model answer.** A lessee must disclose, for finance leases: (a) net carrying amount of each class of leased asset at the balance-sheet date; (b) reconciliation of **total MLP** to their **present value**, and the future MLP split into **not later than one year / later than one year but not later than five years / later than five years**; (c) total contingent rents recognised in P&L; (d) total future minimum sublease payments expected under non-cancellable subleases; and (e) a general description of significant leasing arrangements (basis of contingent rent, renewal/purchase options and escalation clauses, restrictions imposed). Leased assets are presented in the balance sheet as assets, with the corresponding obligation shown as a liability, split current/non-current.

---

## Section D — MCQs / case scenarios

**D1.** The interest rate implicit in a finance lease equates the PV of (MLP + unguaranteed residual) to —
(a) carrying amount (b) **fair value of the asset** (c) gross investment (d) minimum lease payments.
**Answer: (b).** By definition the implicit rate discounts gross investment to fair value (net investment).

**D2.** Under an operating lease with escalating rentals, the lessee recognises rent —
(a) as paid (b) on reducing-balance (c) **straight-line over the term** (d) only in the last year.
**Answer: (c).** Reflects the even time pattern of benefit unless another basis is more representative.

**D3.** A lease of land where ownership is *not* expected to transfer is normally —
(a) finance (b) **operating** (c) either (d) not a lease.
**Answer: (b).** Land's indefinite life means risks/rewards (huge residual) stay with the lessor.

**D4.** A lessee capitalises a finance-leased asset at —
(a) fair value always (b) PV of MLP always (c) **lower of fair value and PV of MLP** (d) contract price.
**Answer: (c).** AS 19 requires the lower of the two at inception.

**D5.** In a sale-and-leaseback giving a *finance* lease, excess of sale proceeds over carrying amount is —
(a) recognised at once (b) **deferred and amortised over the lease term** (c) ignored (d) taken to reserves.
**Answer: (b).** No genuine sale occurs in substance; the "gain" is deferred over the term.

**D6.** Which is NOT within the scope of AS 19?
(a) machinery lease (b) **lease to explore for minerals/oil & gas** (c) office equipment lease (d) vehicle lease.
**Answer: (b).** Leases for natural-resource exploration/use (and licensing of films, patents, copyrights) are excluded.

**D7.** For a lessor's finance lease, unearned finance income is recognised so as to give —
(a) equal amounts each year (b) **a constant periodic return on net investment** (c) more income later (d) SLM.
**Answer: (b).** The actuarial method yields a constant rate of return on the declining net investment.

**D8.** Lease classification is determined —
(a) at each year-end (b) **at the inception of the lease** (c) when rentals change (d) at term-end.
**Answer: (b).** Classification is fixed at inception; it changes only on renegotiation of terms.

**D9. Case.** *Z Ltd. leases equipment for 4 of its 5-year life, no purchase option, PV of MLP = 96% of fair value. Contingent rent based on usage.* Classify and state treatment of contingent rent.
**Answer:** **Finance lease** — term is the major part of life and PV of MLP is substantially all of fair value. **Contingent rent is excluded from MLP** and is charged to P&L in the period incurred (it is not capitalised).

**D10.** The lessee discounts MLP using the incremental borrowing rate only when —
(a) always (b) never (c) **the implicit rate is not practicable to determine** (d) rentals escalate.
**Answer: (c).** The implicit rate is used if determinable; otherwise the lessee's incremental borrowing rate.
