# Q&A — Intangibles, Goodwill & Business Combinations

A practice bank mixing conceptual/theory questions (with model answers and interview phrasing) and fully solved numerical problems. Every number is self-verified: debits equal credits, statements tie out, totals reconcile.

---

## Section A — Conceptual / Theory

### Q1. Define an intangible asset. What are the recognition criteria?

**Answer.** An intangible asset is an **identifiable, non-monetary asset without physical substance** that the entity controls and from which future economic benefits are expected. To recognize one, three qualifying tests plus two recognition thresholds must be met:
- **Identifiability** — either *separable* (can be sold/licensed on its own) or arising from *contractual or legal rights*.
- **Control** — power to obtain the benefits and restrict others.
- **Future economic benefit** — revenue or cost savings expected.
- Plus: benefits are **probable** and **cost is measurable reliably**.

**How to say it in an interview:** "It's a non-physical, identifiable asset — the identifiability test is the key, because that's what separates a recognizable intangible like a patent or customer list from goodwill, which is just the unidentifiable residual."

---

### Q2. What exactly is goodwill, and when can it appear on a balance sheet?

**Answer.** Goodwill is the **excess of purchase price over the fair value of net identifiable assets acquired**. It is a *residual plug*, not a discrete asset — it captures synergies, assembled workforce, and any premium/overpayment. It appears **only** as the result of a business combination. Internally generated goodwill is never recognized because there is no arm's-length transaction to verify its value.

**Interview line:** "Goodwill is arithmetic — price minus fair value of net identifiable assets. You can only book it when you buy a business, never for one you built yourself."

---

### Q3. Explain the internally generated vs acquired asymmetry.

**Answer.** Money spent *building* intangibles yourself is mostly expensed (marketing to build a brand, most R&D). Money spent *buying* the same intangible is capitalized at fair value. The reason is **verifiability**: a purchase price is arm's-length evidence of value; your own opinion of your homegrown brand is not. So two identical firms — one that built a brand, one that bought it — show very different balance sheets, and price-to-book is not comparable across them.

**Interview line:** "Same economic asset, opposite accounting. It's why acquisitive firms look asset-heavy and why you can't compare P/B naïvely between builders and buyers."

---

### Q4. IFRS vs US GAAP on R&D — what's the difference and why does it matter?

**Answer.**
- **US GAAP (ASC 730):** research *and* development are expensed as incurred, with narrow software exceptions (ASC 985-20 for software to sell after technological feasibility; ASC 350-40 for internal-use software application-development stage).
- **IFRS (IAS 38):** research is expensed; **development is capitalized once six criteria are met** (probable benefits, intention to complete, resources, ability to use/sell, technical feasibility, reliable measurement — mnemonic PIRATE), then amortized once the asset is available for use.

**Why it matters:** an IFRS firm capitalizing development shows higher assets and higher near-term earnings than an otherwise identical US GAAP firm. Analysts normalize R&D before comparing.

**Interview line:** "US GAAP expenses everything; IFRS capitalizes qualifying development. I'd normalize before comparing the two."

---

### Q5. Why was goodwill amortization abolished, and what replaced it?

**Answer.** A fixed amortization schedule (up to 40 years pre-2001 in the US) was arbitrary and communicated nothing — goodwill doesn't decline on a predictable timetable. It was replaced by **annual impairment testing**: keep goodwill at cost, write it down only when the acquired unit's fair value falls below its carrying value. This trades a smooth, meaningless charge for a lumpy but informative one.

---

### Q6. Walk through the three statements when a company impairs goodwill by $200m.

**Answer.** (Assume the goodwill is non-deductible, so no tax shield.)
- **Income statement:** $200m pre-tax operating expense; net income falls ~$200m.
- **Cash flow:** net income down $200m at the top, but impairment is non-cash so it's added straight back → **zero change in cash**.
- **Balance sheet:** goodwill −$200m on the asset side; retained earnings −$200m on the equity side → balances.

**Interview line:** "Non-cash, so cash is unaffected and the balance sheet stays balanced. It's a signal the acquisition underperformed, not a cash event."

---

### Q7. Why does a deferred tax liability *increase* goodwill in a purchase price allocation?

**Answer.** In a stock deal, you step up assets to fair value for book purposes but the tax basis stays at the old carryover value — creating a temporary difference and a **DTL = step-up × tax rate**. That DTL is a liability assumed, so net identifiable assets go *down*, and since goodwill = price − net identifiable assets, goodwill goes *up*.

---

### Q8. Finite vs indefinite life — and how does each get subsequently measured?

**Answer.**
- **Finite life** (patent, customer relationship, license): **amortize** over useful life; impairment-test when indicators exist.
- **Indefinite life** (established brand, renewable broadcast license): **no amortization**; impairment-test at least annually. "Indefinite" means no foreseeable limit today — not "infinite."
- **Goodwill** is treated as indefinite: no amortization, annual test.

---

### Q9. What is a bargain purchase and how is it accounted for?

**Answer.** When purchase price is *below* the fair value of net identifiable assets, the difference is a **bargain purchase gain**. After re-verifying all fair values were measured correctly, it is recognized **immediately in the income statement** — not as a liability, not as negative goodwill. It's rare and usually signals distress or a forced sale.

---

### Q10. Contrast US GAAP and IFRS goodwill impairment mechanics.

**Answer.**
- **US GAAP (ASC 350, one step):** compare the **reporting unit's fair value** to its **carrying value including goodwill**. If FV < CV, impairment = CV − FV, capped at the goodwill balance.
- **IFRS (IAS 36):** compare the **CGU's carrying amount** to its **recoverable amount** = higher of (fair value less costs of disposal, value in use). If recoverable < carrying, the loss hits **goodwill first**, then pro-rata to other assets.
- Both: impairment is non-cash and **can never be reversed** for goodwill.

---

### Q11. Can goodwill ever be written back up if the acquired business thrives?

**Answer.** No. Goodwill can only be written *down* via impairment, never up. Any value created by the acquisition's success is *internally generated goodwill*, which is never recognized. So a great acquisition can carry the same book goodwill for decades while its economic value compounds far above book.

---

### Q12. Why do companies add back acquired-intangible amortization in "adjusted" earnings? Should you trust it?

**Answer.** They argue it's a non-cash, deal-related charge that obscures underlying operating performance — and often it isn't even tax-deductible, so it doesn't reflect a cash cost. The add-back is defensible for comparability, **but** be skeptical when it's large: those intangibles represent real capital deployed to buy the business. A serial acquirer adding back big amortization every year is masking the true cost of its growth strategy.

---

## Section B — Numerical Problems

### Q13. Basic goodwill calculation

**Problem.** AcquirerCo buys 100% of SmallCo for **$450m**. SmallCo's identifiable assets have a fair value of **$520m** and its liabilities have a fair value of **$180m**. No deferred tax. Compute goodwill.

**Solution.**
- FV of net identifiable assets = 520 − 180 = **$340m**.
- Goodwill = Purchase price − FV net identifiable assets = 450 − 340 = **$110m**.

**Check:** Buyer receives $340m of net identifiable assets + $110m goodwill = $450m = cash paid. ✓

---

### Q14. Full PPA with intangibles and deferred tax

**Problem.** MegaCo acquires TechCo for **$1,000m** cash. TechCo book equity is **$350m**. Fair-value review:
- PP&E step-up **+$80m**
- Identifiable intangibles newly recognized: patents **$150m**, customer relationships **$100m**
- Inventory step-up **+$30m**
- Tax rate **25%**, no tax basis on step-ups (stock deal).

Compute goodwill and verify the balance sheet.

**Solution.**

| Step | $m |
|---|---|
| Book net identifiable assets (= book equity) | 350 |
| PP&E step-up | +80 |
| Patents | +150 |
| Customer relationships | +100 |
| Inventory step-up | +30 |
| Total pre-tax step-up | +360 |
| DTL = 360 × 25% | −90 |
| **FV of net identifiable assets** | **620** |
| Purchase price | 1,000 |
| **Goodwill = 1,000 − 620** | **380** |

**Verification (what hits the consolidated balance sheet for $1,000m cash out):**

| Item | $m |
|---|---|
| Book net assets | 350 |
| + step-ups & new intangibles | 360 |
| − DTL | (90) |
| + Goodwill | 380 |
| **Total** | **1,000** |

Total = $1,000m = cash paid. ✓ Balanced.

**Note:** without the $90m DTL, net identifiable assets would be $710m and goodwill only $290m. The DTL pushed $90m into goodwill.

---

### Q15. Amortization impact on income statement

**Problem.** Using Q14's intangibles: patents $150m over **5 years**, customer relationships $100m over **10 years**, both straight-line, zero residual. Incremental PP&E depreciation from the $80m step-up over **8 years**. Tax rate 25%. Compute the annual (steady-state) net income impact.

**Solution.**

| Charge | $m/yr |
|---|---|
| Patents 150 ÷ 5 | 30.0 |
| Customer relationships 100 ÷ 10 | 10.0 |
| PP&E depreciation 80 ÷ 8 | 10.0 |
| **Pre-tax total** | **50.0** |
| Tax shield @ 25% | (12.5) |
| **Net income impact** | **37.5 lower** |

**Cash check:** Since the intangible/PP&E step-ups have no tax basis, the amortization isn't tax-deductible. Net income falls $37.5m, add back $50m non-cash D&A, subtract the $12.5m deferred (non-cash) tax benefit → −37.5 + 50.0 − 12.5 = **0 cash impact**. The DTL unwinds by $50m × 25% = $12.5m each year. ✓

---

### Q16. Goodwill impairment — US GAAP one step

**Problem.** A reporting unit has carrying value: net identifiable assets $600m + goodwill $380m = **$980m**. Its fair value is estimated at **$820m**. Compute the impairment and book the entry.

**Solution.**
- FV $820m < CV $980m → impairment indicated.
- Loss = CV − FV = 980 − 820 = **$160m**.
- Cap at goodwill balance: min(160, 380) = **$160m** (goodwill covers it).
- Goodwill: 380 − 160 = **$220m** remaining.

**Entry:**
```
Dr  Goodwill impairment loss (P&L)   160
    Cr  Goodwill                            160
```
**Statement impact:** IS −$160m pre-tax (non-deductible → ~full hit); CF zero (add back non-cash); BS goodwill −$160m, equity −$160m; irreversible. ✓

---

### Q17. Goodwill impairment when the loss exceeds goodwill

**Problem.** A reporting unit's carrying value is **$500m**, of which goodwill is **$90m**. Fair value is **$380m**. How much impairment is recorded (US GAAP)?

**Solution.**
- Loss indicated = CV − FV = 500 − 380 = **$120m**.
- Cap at goodwill balance = min(120, 90) = **$90m**.
- Goodwill is written down to **$0**. The remaining $30m shortfall is **not** recorded against goodwill (the cap); other assets in the unit would be evaluated for impairment under their own standards, but goodwill impairment is limited to $90m.

**Entry:**
```
Dr  Goodwill impairment loss   90
    Cr  Goodwill                     90
```
✓ Goodwill cannot go negative.

---

### Q18. IFRS impairment — recoverable amount

**Problem.** Under IFRS, a CGU has a carrying amount of **$700m** (including goodwill of $120m). Fair value less costs of disposal = **$610m**; value in use (PV of cash flows) = **$650m**. Compute the impairment and its allocation.

**Solution.**
- Recoverable amount = higher of (610, 650) = **$650m**.
- Carrying $700m > recoverable $650m → impairment = 700 − 650 = **$50m**.
- Allocation: **first to goodwill**. Goodwill $120m absorbs the full $50m → goodwill reduced to $70m; no allocation to other assets.

**Entry:**
```
Dr  Impairment loss (P&L)   50
    Cr  Goodwill                  70... 
```
Correction — credit goodwill $50m only:
```
Dr  Impairment loss (P&L)   50
    Cr  Goodwill                  50
```
Goodwill: 120 − 50 = **$70m**. ✓

---

### Q19. Bargain purchase

**Problem.** DistressCo is acquired for **$200m**. Fair value of identifiable assets = **$310m**; liabilities assumed = **$60m**. No deferred tax. Compute the result and book it.

**Solution.**
- FV net identifiable assets = 310 − 60 = **$250m**.
- Purchase price $200m < $250m → **bargain purchase gain = 250 − 200 = $50m**.
- After re-verifying fair values, recognize the $50m as an immediate gain in the income statement. No goodwill.

**Entry:**
```
Dr  Identifiable assets      310
    Cr  Liabilities assumed         60
    Cr  Cash                        200
    Cr  Bargain purchase gain (P&L)  50
```
**Check:** Debits 310 = Credits 60 + 200 + 50 = 310. ✓

---

### Q20. Partial acquisition — full vs partial goodwill

**Problem.** ParentCo buys **80%** of SubCo for **$400m**. FV of SubCo's net identifiable assets = **$450m**. The fair value of the 20% NCI is assessed at **$95m**. Compute goodwill under (a) full-goodwill and (b) partial-goodwill methods.

**Solution.**

**(a) Full goodwill (US GAAP required; IFRS option):**
- Goodwill = (Consideration + FV of NCI) − FV net identifiable assets = (400 + 95) − 450 = **$45m**.

**(b) Partial goodwill (IFRS option):**
- NCI = 20% × 450 = $90m.
- Goodwill = (400 + 90) − 450 = **$40m** (only the parent's share).

**Sense check:** Full-goodwill grosses up NCI to fair value ($95m vs $90m), so goodwill is $5m higher ($45m vs $40m) — exactly the $5m NCI premium. ✓

---

### Q21. Amortization of a purchased finite-life intangible + carrying value

**Problem.** A company buys a patent for **$60m** with a **12-year** useful life, zero residual, straight-line. Compute annual amortization and the carrying value after 4 years. Book year-1 entry.

**Solution.**
- Annual amortization = 60 ÷ 12 = **$5m/yr**.
- After 4 years: accumulated amortization = 5 × 4 = $20m. Carrying value = 60 − 20 = **$40m**.

**Entry (each year):**
```
Dr  Amortization expense       5
    Cr  Accumulated amortization    5
```
✓

---

### Q22. R&D — IFRS vs US GAAP earnings difference

**Problem.** BioCo spends **$120m** in a year: **$50m research**, **$70m development** — all of the development qualifies for capitalization under IFRS. The capitalized development amortizes over **7 years** starting the *following* year (nothing amortized in the current year). Tax ignored. Compare current-year pre-tax income impact and balance-sheet assets under IFRS vs US GAAP.

**Solution.**

| | US GAAP | IFRS |
|---|---|---|
| Research expensed | 50 | 50 |
| Development expensed | 70 | 0 (capitalized) |
| **Current-year expense** | **120** | **50** |
| Intangible asset added to B/S | 0 | 70 |

- **Pre-tax income:** IFRS is **$70m higher** in the current year (only $50m expensed vs $120m).
- **Balance sheet:** IFRS carries a **$70m** development intangible; US GAAP carries nothing.
- **Following years:** IFRS amortizes 70 ÷ 7 = **$10m/yr** for 7 years — the deferred cost catches up. US GAAP has no future drag.

**Takeaway:** Over the asset's life total expense is identical ($120m); IFRS just *defers* $70m of it. This is exactly why analysts normalize R&D before comparing an IFRS firm to a US GAAP peer. ✓

---

## Reconciliation summary

| Problem | Key result | Verified |
|---|---|---|
| Q13 | Goodwill $110m | ✓ |
| Q14 | Goodwill $380m; DTL $90m | ✓ balances to $1,000m |
| Q15 | Net income −$37.5m/yr; cash impact 0 | ✓ |
| Q16 | Impairment $160m; goodwill → $220m | ✓ |
| Q17 | Impairment capped at $90m; goodwill → $0 | ✓ |
| Q18 | IFRS impairment $50m; goodwill → $70m | ✓ |
| Q19 | Bargain gain $50m in P&L | ✓ debits = credits |
| Q20 | Full GW $45m vs partial GW $40m | ✓ $5m NCI premium |
| Q21 | Amort $5m/yr; CV after 4 yrs $40m | ✓ |
| Q22 | IFRS pre-tax income $70m higher; $70m asset | ✓ |
