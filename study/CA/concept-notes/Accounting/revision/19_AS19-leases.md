# AS 19: Leases

## Snapshot
Some leases are financing in disguise (buy-on-EMI); some are genuine rentals. AS 19 draws the line by **substance over form** — who bears substantially all the **risks and rewards** of ownership — and tells lessee and lessor how to account for finance vs operating leases. Classify at inception. Excludes land, natural-resource and licensing agreements.

## Core concepts
- **Substance over form:** ignore the label and legal title; ask who bears the risks and rewards.
- **Risks** of ownership: idle capacity losses, obsolescence, variation in returns. **Rewards:** profitable operation over economic life, gain on residual/appreciation.
- **Finance lease** = transfers substantially all risks and rewards (title may or may not transfer). **Operating lease** = any lease that is not a finance lease (residual box).
- **Inception** = earlier of the lease agreement date and the date of commitment to principal provisions. **Classification fixed here; not revised** unless *terms* change (a modification = new lease). Change of estimate or lessee default does NOT reclassify.
- **Lease term** = non-cancellable period + option periods where at inception exercise is reasonably certain (bargain renewal counts).
- **Economic life** = asset concept (period usable / production units). **Useful life** = lessee concept (remaining period from lease-term start over which lessee consumes benefits; NOT shortened by expected renewals).

## Key provisions / rules

**Classification — finance lease indicators (any one may clinch; weigh for substance, no fixed % thresholds):**
| (a) | Ownership transfers by end of term |
| (b) | Bargain purchase option (price sufficiently below fair value → exercise reasonably certain) |
| (c) | Term is the **major part** of economic life |
| (d) | PV of MLP at inception ≥ **substantially all** of fair value |
| (e) | Asset so specialised only the lessee can use it without major modifications |
Weaker indicators: lessee bears lessor's cancellation losses; residual value fluctuations accrue to lessee; bargain secondary-period renewal.

**Minimum Lease Payments (MLP):** payments over the term the lessee is/can be required to make, **excluding contingent rent** and service/tax costs reimbursed to lessor. PLUS:
- **Lessee's MLP:** residual value guaranteed by lessee or a party related to lessee.
- **Lessor's MLP:** residual guaranteed to lessor by lessee, party related to lessee, OR an **independent third party** financially capable.
- Bargain purchase option → add its exercise price.
Asymmetry: a third-party residual guarantee counts for the **lessor** but never the **lessee** → lessee's and lessor's MLP for the same lease can differ. **Contingent rent** excluded (not fixed at inception); recognised when it arises.

**Interest rate implicit in the lease** = rate making PV of (MLP + unguaranteed residual) = fair value (net of grants/tax credits to lessor). If lessee can't determine it → use **incremental borrowing rate**.

**Lessor's toolkit:**
- Gross investment = MLP receivable + unguaranteed residual value.
- Net investment = gross investment discounted at implicit rate = fair value + initial direct costs.
- Unearned finance income = Gross − Net.

**Initial direct costs:** Lessee (finance) → add to asset. Lessor (finance, non-dealer) → in net investment. Manufacturer/dealer lessor → **expensed at inception**. Lessor (operating) → capitalise & spread over term.

**The four cells:**
| | Finance lease | Operating lease |
|---|---|---|
| **Lessee** | Asset + liability at **lower of FV / PV of MLP**; split rental into interest (constant rate on balance) + principal; depreciate | No asset; rent **straight-lined**; difference → lease equalisation |
| **Lessor** | Derecognise asset; book **net-investment receivable**; finance income at **constant rate of return**; dealer → also selling profit | Keep & **depreciate** asset; income **straight-lined** |

**Lessee finance-lease depreciation period:** if ownership reasonably certain (test a/b) → **useful life**; otherwise → **shorter of lease term and useful life**. Finance charge and depreciation are computed **independently** → P&L charge front-loaded (exceeds rental in early years).

**Manufacturer/dealer lessor — two profits:** (i) selling profit at inception (sales value = fair value, or PV of MLP at commercial rate if lower, less cost); (ii) finance income over term. Artificially low quoted rate → recompute selling profit at a **commercial rate**. IDC expensed now.

**Sale and leaseback:**
- Leaseback = **finance lease:** excess of sale proceeds over carrying amount **deferred and amortised** over the lease term in proportion to depreciation (never recognised now).
- Leaseback = **operating lease:**
  - At fair value → recognise profit/loss **immediately**.
  - Sale price **above** fair value → excess over FV deferred and amortised over expected use.
  - Sale price **below** fair value → recognise now, EXCEPT loss compensated by below-market future rents → defer and amortise over use.
  - Carrying amount > fair value → write down to FV **immediately** as a loss (any leaseback type).

## Journal entries
**Lessee finance lease (Year 1):**
```
Machinery A/c        Dr.  (lower of FV / PV of MLP)
    To Lease Liability A/c
Interest A/c         Dr.  (opening liability × rate)
    To Lease Liability A/c
Lease Liability A/c  Dr.  (rental)
    To Bank A/c
Depreciation A/c     Dr.
    To Machinery A/c
```
**Lessor finance lease:** Lease Receivable (Net Investment) Dr / To Asset (derecognise). Each year: Bank Dr / To Lease Receivable (principal) / To Finance Income (interest).
**Operating lease (lessee, escalating rent):** Rent A/c Dr (straight-line) / To Bank (cash) / To Lease Equalisation (difference).

## Worked mini-example
Lessee: 3 year-end rentals of ₹1,00,000; FV ₹2,50,000; IBR 10%. PV of MLP = 1,00,000 × PVIFA(10%,3) = 1,00,000 × 2.48685 = ₹2,48,685 (~99.5% of FV → finance lease). Record at lower = **₹2,48,685**.

| Year | Opening | Interest @10% | Rental | Principal | Closing |
|---|---|---|---|---|---|
| 1 | 2,48,685 | 24,869 | 1,00,000 | 75,131 | 1,73,554 |
| 2 | 1,73,554 | 17,355 | 1,00,000 | 82,645 | 90,909 |
| 3 | 90,909 | 9,091 | 1,00,000 | 90,909 | 0 |

Depreciation = 2,48,685 ÷ 3 = ₹82,895/yr. P&L = interest + depreciation, front-loaded (Yr 1 = ₹1,07,764 vs ₹1,00,000 rent); 3-yr total ₹3,00,000 = total rentals.
**Advance rentals:** use annuity-due factor; day-0 payment carries zero interest; "lower of" may flip to FV.

## Disclosures
**Lessee finance:** net carrying amount by class within PPE; reconciliation of total MLP to PV by maturity bands **≤1 yr / 1–5 yrs / >5 yrs**; contingent rents in P&L; future minimum sublease payments; general description of significant leasing arrangements (contingent rent basis, renewal/purchase/escalation options, restrictions).
**Lessee operating:** future MLP under non-cancellable leases in the three maturity bands; future minimum sublease receipts; lease payments in P&L (split MLP/contingent/sublease); general description.
**Lessor finance:** reconciliation of gross investment to PV of MLP receivable in three bands; unearned finance income; unguaranteed residual values; accumulated provision for uncollectible MLP; contingent rents; general description.
**Lessor operating:** future MLP under non-cancellable leases in aggregate + three bands; contingent rents; gross carrying amount, accumulated depreciation and period depreciation of leased assets; general description.

## Exam traps & must-remember
- "Lower of" is one-directional: lessee records at lower of FV and PV of MLP; flips with advance payments.
- Rental ≠ P&L expense in finance lease — split into interest + principal; P&L = interest + depreciation, front-loaded. Charging the whole rental is wrong.
- Guaranteed residual → in MLP (guaranteeing party). Unguaranteed → out of MLP but in lessor's gross investment. Third-party guarantee counts for lessor only.
- Advance vs arrears: advance (annuity-due) day-0 payment has zero interest; changes every figure.
- Contingent rent never in MLP.
- Title transfer neither necessary nor sufficient for finance lease.
- Depreciate over useful life only if ownership reasonably certain; else shorter of term/life.
- AS 19 excludes land — assess building element separately in "land and building".
- Sale & leaseback: finance leaseback → defer & amortise gain (immediate recognition is the classic wrong answer).
- Classify at inception; don't reclassify for market movement/estimate/default — only term change.
- Dealer's upfront selling profit at commercial rate; dealer IDC expensed now.
- Lessee's and lessor's MLP for the same lease can legitimately differ (residual asymmetry).
- Bargain renewals are inside the lease term (can swing "major part of life").
- IDC placement differs by cell (lessee finance → asset; lessor finance non-dealer → net investment; dealer → expense; lessor operating → capitalise & spread).

## One-line recall
- Substance over form: who bears risks & rewards? Finance = yes; operating = residual box.
- Five indicators (ownership transfer, bargain option, major part of life, PV of MLP ≈ FV, specialised); no fixed % under AS 19.
- Lessee finance: asset + liability at lower of FV / PV of MLP; split rental (constant rate); depreciate; front-loaded P&L.
- Lessor finance: net-investment receivable, finance income at constant rate; dealer books two profits.
- Operating: straight-line rent/income; lessor keeps & depreciates asset.
- Sale & leaseback: finance → defer gain; operating at FV → recognise now.
- Excludes land; Ind AS 116 = single lessee model + covers land.
