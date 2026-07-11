# Taxation (Income-tax & GST) — HARD Reasoning-First Q&A (Q1–Q100)

*100 of the toughest CA-Intermediate questions — multi-step problems with twists, integrated cross-concept problems, and "analyse / advise / examine validity" case-style questions. Every answer carries a **"Why this way (the reasoning)"** block that explains the principle behind each step (and why the tempting wrong approach fails), so you learn to think, not memorise. Full chapter coverage, ICAI-depth working notes and statements.*

---

## Part C — HARD Reasoning-First Bank (Q1–Q100)

### Q1. Ch: Basic Concepts — Surcharge & Marginal Relief at ₹50 lakh threshold (Marks: 8) [Problem]
**Question:** Mr. Verma, aged 45, a resident individual, opts OUT of the default new regime and is taxed under the **old regime** for AY 2025-26. His **Total Income after all deductions is ₹51,00,000** (entirely non-special-rate income). Compute his tax liability, clearly demonstrating the operation of **surcharge and marginal relief**. Also state the tax had his income been exactly ₹50,00,000, and explain the "cliff" this addresses.

**Solution:**

**WN-1 — Tax on ₹51,00,000 (old-regime slabs, before surcharge):**

| Slab | Rate | Tax (₹) |
|---|---|---|
| Up to 2,50,000 | Nil | 0 |
| 2,50,001–5,00,000 | 5% | 12,500 |
| 5,00,001–10,00,000 | 20% | 1,00,000 |
| Above 10,00,000 (41,00,000) | 30% | 12,30,000 |
| **Tax before surcharge** | | **13,42,500** |

Surcharge @10% (income > ₹50L ≤ ₹1cr) = ₹1,34,250 → **Tax + SC = ₹14,76,750**

**WN-2 — Tax on ₹50,00,000 (the threshold, no surcharge):**
12,500 + 1,00,000 + (40,00,000 × 30%) = **₹13,12,500** (no surcharge, as income does not exceed ₹50L).

**WN-3 — Marginal relief test:**
Increase in income beyond ₹50L = ₹1,00,000.
Increase in (tax + SC) = 14,76,750 − 13,12,500 = ₹1,64,250.
Since the tax rise (₹1,64,250) exceeds the income rise (₹1,00,000), **marginal relief = 1,64,250 − 1,00,000 = ₹64,250**.

**Statement Showing Tax Liability — Mr. Verma (AY 2025-26, Old Regime):**

| Particulars | ₹ |
|---|---|
| Tax before surcharge | 13,42,500 |
| Add: Surcharge @10% | 1,34,250 |
| Less: Marginal relief | (64,250) |
| Tax + surcharge after relief | 14,12,500 |
| Add: Health & Education Cess @4% | 56,500 |
| **Total tax liability** | **14,69,000** |

**Answer:** Tax liability = **₹14,69,000**. (Had income been ₹50,00,000, tax = ₹13,12,500 + 4% cess ₹52,500 = **₹13,65,000**.)

**Why this way (the reasoning):** Surcharge is levied on the *whole* base tax once income crosses ₹50L, not merely on the excess. So a ₹1 crossing of the threshold would otherwise trigger ₹1.34L of surcharge on the entire ₹13.42L tax — a person earning ₹1 more could pay far more than ₹1 extra. Marginal relief exists precisely to smooth this cliff: it caps the *total additional burden (tax + surcharge)* at the *additional income*. The principle is "no taxpayer just above a threshold should be worse off than one at the threshold plus the extra rupees." That is why we compare the *increase* in tax+SC against the *increase* in income and refund the excess as relief. The tempting wrong move is to apply relief on cess too — cess is charged *after* relief on the net (tax+SC), so it is never part of the relief computation.

*(Full-marks tip: The examiner rewards the explicit WN-2 "tax at exactly ₹50L (nil surcharge)" and the clean relief comparison. Marks are lost for computing relief against tax-before-surcharge, forgetting that at ₹50L there is NO surcharge, or netting cess into relief.)*

---

### Q2. Ch: Basic Concepts — Rebate u/s 87A & its own Marginal Relief (New Regime) (Marks: 6) [Problem]
**Question:** Ms. Kavya, resident aged 30, is taxed under the **default new regime (Sec 115BAC)** for AY 2025-26. Her **Total Income is ₹7,10,000** (no special-rate income). Compute her tax liability. A colleague argues "her income exceeds ₹7,00,000 so she loses the entire 87A rebate and pays full tax." **Examine the validity** of this claim with computation.

**Solution:**

**WN-1 — Tax on ₹7,10,000 (new-regime slabs):**

| Slab | Rate | Tax (₹) |
|---|---|---|
| Up to 3,00,000 | Nil | 0 |
| 3,00,001–7,00,000 | 5% | 20,000 |
| 7,00,001–7,10,000 (10,000) | 10% | 1,000 |
| **Tax before rebate** | | **21,000** |

**WN-2 — Rebate u/s 87A + marginal relief on rebate:**
Full 87A rebate (₹25,000) is available only if total income ≤ ₹7,00,000 → not available here. **But** the proviso grants marginal relief: tax payable cannot exceed the amount by which income exceeds ₹7,00,000.
Income over ₹7,00,000 = ₹10,000. Tax computed = ₹21,000 > ₹10,000.
**Rebate (marginal relief) = 21,000 − 10,000 = ₹11,000.**

**Statement Showing Tax Liability — Ms. Kavya:**

| Particulars | ₹ |
|---|---|
| Tax before rebate | 21,000 |
| Less: Rebate u/s 87A (marginal-relief limb) | (11,000) |
| Tax after rebate | 10,000 |
| Add: HEC @4% | 400 |
| **Total tax liability** | **10,400** |

**Answer:** Tax = **₹10,400**. The colleague's claim is **INVALID** — she does not pay full tax of ~₹21,840; marginal relief caps her tax at ₹10,000 (+cess).

**Why this way (the reasoning):** The 87A rebate under the new regime has *two* limbs. The first limb gives a flat rebate (up to ₹25,000) if income ≤ ₹7,00,000. The second, inserted specifically for the new regime, is a *marginal-relief* limb: for income marginally above ₹7,00,000, tax is limited to the *excess over ₹7,00,000*. The logic mirrors surcharge marginal relief — someone earning ₹7,10,000 should not, after paying tax, be left with less than someone earning ₹7,00,000 (who pays nil). Without this, ₹10,000 of extra income would cost ₹21,000 in tax — an absurd >100% marginal rate. The trap is treating 87A as a simple on/off switch at ₹7L; the second limb makes it a *sliding* relief until tax naturally equals the flat rebate.

*(Full-marks tip: State BOTH limbs of 87A and identify which one applies. Deductions come for omitting the marginal-relief proviso, or applying old-regime figures (₹5,00,000 / ₹12,500) under the new regime.)*

---

### Q3. Ch: Basic Concepts — Surcharge Cap under New Regime (Old vs New) (Marks: 8) [Problem]
**Question:** Mr. Ambani (resident, 50) has **Total Income of ₹5,50,00,000** for AY 2025-26, all taxable at normal rates. Compute and **compare** his tax under (a) the old regime and (b) the default new regime, highlighting the treatment of the **highest surcharge slab**, and advise which regime is beneficial.

**Solution:**

**WN-1 — Old regime, tax before surcharge:**
12,500 + 1,00,000 + (5,40,00,000 × 30%) = 12,500 + 1,00,000 + 1,62,00,000 = **₹1,63,12,500**.
Surcharge @37% (income > ₹5cr) = ₹60,35,625.

**WN-2 — New regime, tax before surcharge:**

| Slab | Rate | Tax (₹) |
|---|---|---|
| 3,00,001–7,00,000 | 5% | 20,000 |
| 7,00,001–10,00,000 | 10% | 30,000 |
| 10,00,001–12,00,000 | 15% | 30,000 |
| 12,00,001–15,00,000 | 20% | 60,000 |
| Above 15,00,000 (5,35,00,000) | 30% | 1,60,50,000 |
| **Tax before surcharge** | | **1,61,90,000** |

Under the new regime the **surcharge is capped at 25%** (the 37% rate is not applicable). Surcharge @25% = ₹40,47,500.

**Statement Showing Comparative Tax Liability:**

| Particulars | Old Regime (₹) | New Regime (₹) |
|---|---|---|
| Tax before surcharge | 1,63,12,500 | 1,61,90,000 |
| Add: Surcharge | 60,35,625 (37%) | 40,47,500 (25%) |
| Tax + surcharge | 2,23,48,125 | 2,02,37,500 |
| Add: HEC @4% | 8,93,925 | 8,09,500 |
| **Total tax liability** | **2,32,42,050** | **2,10,47,000** |

**Answer:** New regime is beneficial by **₹21,95,050**. Advise Mr. Ambani to remain in the **default new regime**.

**Why this way (the reasoning):** For ultra-high incomes the *rate structure* barely differs (both top out at 30%), so the deciding factor is surcharge. The old regime carries a 37% surcharge slab for income above ₹5 crore; the new regime deliberately *omits* the 37% slab and caps surcharge at 25%. This was a policy choice to make the new regime attractive to the very rich and to reduce India's peak marginal rate (old peak ≈ 42.744%, new peak ≈ 39%). Hence for anyone above ₹2 crore, the surcharge cap alone usually outweighs the loss of Chapter VI-A deductions. The wrong approach is to assume "old regime with deductions always wins for the wealthy" — at this income the deductions (a few lakhs) are trivial against a ~₹20L surcharge saving.

*(Full-marks tip: Show the 37% vs capped-25% side by side and quantify the surcharge saving. Marks lost for applying 37% under the new regime or forgetting cess is on tax+surcharge.)*

---

### Q4. Ch: Basic Concepts — Diversion vs Application of Income; Previous Year for New Business (Marks: 5) [Case/Application]
**Question:** **Comment on the validity / correct treatment** in each independent situation for AY 2025-26:
(i) Under a family settlement decree, Mr. X must pay 30% of his professional receipts to his mother as a first charge before the income reaches him. He claims this 30% is not his income.
(ii) Mr. Y voluntarily pays ₹5,00,000 of his salary to his brother out of "love and affection" and excludes it.
(iii) Mr. Z sets up a new consultancy business on 1st December 2024. He argues his first previous year runs a full 12 months to 30th November 2025.

**Answer:**
**Governing principle — Diversion by overriding title vs Application of income:** Income diverted *before it accrues* to the assessee, by a title that overrides his own (a charge/obligation attaching to the *source*), is not taxable in his hands — it never becomes his income. But income the assessee *earns and then spends/gives away* is a mere *application* of his own income and remains fully taxable (the "real income"/*Sitaldas Tirathdas* principle).

- **(i) Valid — diversion by overriding title.** The decree creates a *first charge* diverting 30% *at source* before it reaches Mr. X; that portion never accrues to him. Only 70% is his income. **Conclusion: 30% is excluded.**
- **(ii) Invalid — application of income.** The salary first accrues wholly to Mr. Y; paying his brother is voluntary disposal of income already earned. **Conclusion: full salary, including ₹5,00,000, is taxable in Y's hands.**
- **(iii) Invalid — first previous year for a newly set-up source.** Under Sec 3, where a business/source is *newly set up* in a financial year, the first previous year begins on the date of setting up and **ends on the immediately following 31st March**. Hence Z's first PY = 1.12.2024 to 31.3.2025 (4 months), **not** a 12-month period to 30.11.2025. AY = 2025-26.

**Why this way (the reasoning):** The diversion/application distinction turns on *timing and title*: does an obligation carve out the income *before* it becomes the assessee's (source-level charge = diversion), or does the assessee receive it and *then* discharge an obligation (application)? A decree fixing a first charge on the source overrides the assessee's title; a voluntary gift does not. For the previous year, the Act insists every source is aligned to the uniform financial-year framework — a new source cannot claim a 12-month window straddling two financial years, else assessment years would fragment. The mischief the rule addresses is exactly this: it forces every income into a common April–March measurement window.

*(Full-marks tip: Name the *Sitaldas Tirathdas* test and the words "overriding title" vs "application"; for (iii) cite Sec 3 and give the exact PY dates. Bald conclusions without the principle lose half the marks.)*

---

### Q5. Ch: Basic Concepts — Marginal Relief at the ₹1 crore threshold (Marks: 6) [Problem]
**Question:** Dr. Mehta (resident, 55, old regime) has **Total Income of ₹1,01,00,000** for AY 2025-26. Compute the tax liability with **marginal relief**, and state what his tax would have been at exactly ₹1,00,00,000.

**Solution:**

**WN-1 — Tax on ₹1,01,00,000:** 12,500 + 1,00,000 + (91,00,000 × 30%) = ₹28,42,500. Surcharge @15% (>₹1cr) = ₹4,26,375 → Tax+SC = **₹32,68,875**.

**WN-2 — Tax on ₹1,00,00,000 (surcharge here is only 10%):**
Base = 12,500 + 1,00,000 + (90,00,000 × 30%) = ₹28,12,500. Surcharge @10% = ₹2,81,250 → Tax+SC = **₹30,93,750**.

**WN-3 — Marginal relief:** Income increase beyond ₹1cr = ₹1,00,000. Permissible tax+SC at ₹1.01cr = 30,93,750 + 1,00,000 = ₹31,93,750. Actual tax+SC = ₹32,68,875. **Relief = 32,68,875 − 31,93,750 = ₹75,125.**

**Statement Showing Tax Liability — Dr. Mehta:**

| Particulars | ₹ |
|---|---|
| Tax before surcharge | 28,42,500 |
| Add: Surcharge @15% | 4,26,375 |
| Less: Marginal relief | (75,125) |
| Tax + surcharge after relief | 31,93,750 |
| Add: HEC @4% | 1,27,750 |
| **Total tax liability** | **33,21,500** |

**Answer:** Tax = **₹33,21,500**. (At exactly ₹1cr: 30,93,750 + 4% cess ₹1,23,750 = **₹32,17,500**.)

**Why this way (the reasoning):** The critical trap at the ₹1 crore boundary is that the comparison point already *carries* surcharge at the *lower* slab (10%), unlike the ₹50L boundary where the comparison income bears NO surcharge. When income crosses ₹1cr the surcharge rate *jumps from 10% to 15% on the whole base*, so the reference figure must be "tax + 10% surcharge at ₹1cr," not "tax with no surcharge." Marginal relief again ensures the taxpayer just above ₹1cr keeps the surcharge increment down to the extra income earned. Using the "no surcharge" figure of the ₹50L problem here is the classic error and inflates relief wrongly.

*(Full-marks tip: The examiner specifically checks whether you computed the reference tax with the *lower* 10% surcharge at ₹1cr. Using nil surcharge at the ₹1cr comparison point is the single most common and costly mistake.)*

---

### Q6. Ch: Residential Status — Indian citizen visiting India; 120-day rule & auto-RNOR (Marks: 8) [Case/Application]
**Question:** Mr. Rajan, an **Indian citizen**, has settled in Dubai (UAE, which levies no personal income tax) for many years. During PY 2024-25 he **visits India for 125 days**. In the four immediately preceding previous years he was in India for **400 days** in aggregate. His income for PY 2024-25 comprises ₹18,00,000 accruing in India (from Indian house property and Indian shares) and ₹90,00,000 arising outside India. **Determine his residential status** for AY 2025-26 and briefly its consequence, examining the special provisions that apply.

**Answer:**
**Step 1 — Basic condition, Sec 6(1):** Resident if (a) in India ≥182 days in PY, OR (b) ≥60 days in PY *and* ≥365 days in the 4 preceding PYs.
- (a) 125 < 182 → fails.
- (b) He is an Indian citizen coming on a **visit** to India, so *Explanation 1(b)* normally extends "60 days" to "182 days." **However**, the *second proviso* to Explanation 1 provides that where such a person's **total income (other than income from foreign sources) exceeds ₹15,00,000**, the extended period is **120 days**, not 182. His Indian-source income is ₹18,00,000 (> ₹15L), so the **120-day threshold applies**.
- Test: 125 days ≥ 120 **and** 400 days ≥ 365 in the preceding 4 years → **basic condition (b) satisfied → he is a RESIDENT.**

**Step 2 — Ordinarily resident or not, Sec 6(6):** A person who becomes resident *only by virtue of the 120-day rule* (income > ₹15L, Indian-citizen/PIO visitor) is, by Sec 6(6)(c), deemed to be **Not Ordinarily Resident**. Hence he need not even test the 730-days/2-of-10-years conditions.

**Step 3 — Sec 6(1A) deemed residence:** This applies only to a person who is **NOT** resident under Sec 6(1). Since Rajan is already resident under 6(1), **6(1A) is not invoked** at all.

**Conclusion:** Mr. Rajan is **Resident but Not Ordinarily Resident (RNOR)** for AY 2025-26. Consequence: his ₹18,00,000 Indian income is taxable; his ₹90,00,000 foreign income is taxable **only if** it is derived from a business controlled from / profession set up in India — otherwise it is **not** taxable in India.

**Why this way (the reasoning):** The provision targets high-income Indian-origin persons who "park" abroad in low/no-tax jurisdictions yet spend substantial time in India. The 182-day concession for visitors was being exploited, so Parliament created a *middle band* — if your Indian income exceeds ₹15L, mere 120 days of presence makes you resident, but only as RNOR, so your genuinely foreign income stays largely untaxed while your Indian nexus is captured. Recognising that 6(6)(c) *auto-classifies* him as RNOR is the crux; students who correctly find "resident" then wrongly run the ordinary 6(6) day-counts and land on R&OR go wrong. Equally, invoking 6(1A) here is an error — 6(1A) is a *fallback* only for those who escape 6(1) entirely.

*(Full-marks tip: The three examiner checkpoints are (i) using 120 not 182 because income > ₹15L, (ii) auto-RNOR under 6(6)(c), and (iii) expressly noting 6(1A) does not apply because he is already resident. Missing any one caps the marks.)*

---

### Q7. Ch: Residential Status — Scope of Total Income / Incidence of Tax (Marks: 8) [Case/Application]
**Question:** Mr. Sen, whose status for AY 2025-26 is **Resident but Not Ordinarily Resident (RNOR)**, has the following receipts. **State, with reasons, the taxability of each** under Sec 5, and compute the total income taxable in India.

| # | Nature of income | ₹ |
|---|---|---|
| 1 | Profit from a business in Mumbai | 6,00,000 |
| 2 | Salary earned and received in Germany for services rendered *in India* | 4,00,000 |
| 3 | Profit from a business in Canada, the business being *wholly controlled from India* | 5,00,000 |
| 4 | Profit from a business in Sri Lanka, controlled from Sri Lanka, ₹2,00,000 of which is remitted to India | 3,00,000 |
| 5 | Dividend from a UK company, received in the UK | 1,50,000 |
| 6 | Income earned and received abroad in an earlier year, now brought into India | 8,00,000 |

**Answer:**
**Governing rule (Sec 5(1)):** For a **RNOR**, taxable income comprises: (a) income *received/deemed received* in India; (b) income *accruing/deemed to accrue* in India; and (c) income accruing *outside* India **only if** derived from a **business controlled from / profession set up in India**. All other purely foreign-source income is outside the charge.

| # | Treatment | Taxable? | ₹ |
|---|---|---|---|
| 1 | Accrues & received in India | Yes | 6,00,000 |
| 2 | Services rendered in India → income *deemed to accrue in India* (Sec 9); place of receipt irrelevant | Yes | 4,00,000 |
| 3 | Foreign income BUT from a business *controlled from India* → limb (c) | Yes | 5,00,000 |
| 4 | Foreign income, business controlled outside India → not taxable. The ₹2,00,000 remittance is *not* "first receipt" — mere remittance of already-accrued income is not taxed | No | 0 |
| 5 | Foreign-source income received abroad, no India nexus → taxable only for R&OR, not RNOR | No | 0 |
| 6 | Past income already accrued/received abroad earlier; "bringing into India" is remittance, not receipt → not income of PY | No | 0 |
| | **Total Income taxable in India** | | **15,00,000** |

**Answer:** Total income taxable = **₹15,00,000**.

**Why this way (the reasoning):** The whole scheme hinges on two ideas the student must internalise. First, **"received" means the *first* receipt** — where income is *earned* (accrues) is a different event from where it is *received*, and *remittance* of income that was already received/accrued elsewhere is a third, tax-irrelevant event. That single distinction disposes of items 4 and 6 (remittances, not receipts). Second, the RNOR status is a *deliberate concession*: it exempts genuinely foreign income (items 5) but claws back foreign income that still has an *active Indian management nexus* (item 3, "business controlled from India"). Item 2 catches students because German receipt tempts a "foreign income" label — but the *source* is services rendered in India, so Sec 9 deems it to accrue in India and it is taxable regardless of status. Confusing accrual with receipt is the master error this question tests.

*(Full-marks tip: A one-line reason per item is mandatory. Full marks require expressly rejecting the remittance items (4's ₹2L and item 6) as "not first receipt," and pinning item 3 on the "controlled from India" limb. A bare "taxable/not taxable" table without reasons earns barely half.)*

---

### Q8. Ch: Residential Status — RNOR additional-condition arithmetic (Marks: 6) [Problem]
**Question:** Mr. Iqbal returned to India permanently on 1st April 2024 after living abroad. He satisfies a basic condition of Sec 6(1) for PY 2024-25 (thus **resident**). His stay in India in the seven and ten preceding previous years is tabulated. **Determine whether he is Ordinarily Resident or Not Ordinarily Resident** for AY 2025-26.

| Data point | Value |
|---|---|
| Number of the 10 immediately preceding PYs in which he was **non-resident** | 8 years |
| Number of days in India during the **7 immediately preceding** PYs | 610 days |

**Solution:**
**Sec 6(6) test — a resident individual is Ordinarily Resident only if BOTH:**
- (i) he was **resident in India in at least 2 of the 10** preceding PYs, **and**
- (ii) he was in India for **at least 730 days in the 7** preceding PYs.
A person is **NOT Ordinarily Resident** if he fails *either* condition.

**WN-1 — Condition (i):** Non-resident in 8 of 10 preceding years ⇒ resident in only **2** of 10 years. He is resident in *at least* 2 years → condition (i) is **satisfied**.

**WN-2 — Condition (ii):** Days in 7 preceding years = **610 < 730** → condition (ii) **fails**.

Since **both** conditions must hold for R&OR and condition (ii) fails, he is **Not Ordinarily Resident**.

**Answer:** Mr. Iqbal is **Resident but Not Ordinarily Resident (RNOR)** for AY 2025-26.

**Why this way (the reasoning):** The RNOR bridge exists so a returning Indian is not immediately taxed on worldwide income the very year he lands. The two additional conditions test *depth of past connection*: two-of-ten years of residence AND 730+ days over seven years. Crucially the logic is **conjunctive for R&OR** — you need to clear *both* hurdles to be Ordinarily Resident, so **failing even one** drops you to RNOR. Here he *just* clears the "2 of 10" hurdle (exactly 2), which tempts students to conclude R&OR; but the 730-day hurdle is failed (610), and that alone is decisive. Reading the conditions disjunctively — "he meets one, so he's ordinarily resident" — is the standard trap; the statute requires *both*.

*(Full-marks tip: State that R&OR needs BOTH conditions and RNOR needs failure of AT LEAST ONE. The "resident in ≥2 of 10" is satisfied by *exactly* 2 — do not misread "resident in only 2 years" as a failure. Show both computations even though one failure settles it.)*

---

### Q9. Ch: Residential Status — Sec 6(1A) deemed residence & crew-member day count (Marks: 8) [Case/Application]
**Question:** **Advise** on the residential status for AY 2025-26 in each independent case, citing the exact provision:
(i) Mr. Nair, an **Indian citizen**, earns ₹40,00,000 (₹22,00,000 from Indian sources; rest foreign). He manages his affairs so as to stay in India **only 90 days** in PY 2024-25 and is **not liable to tax in any other country** (he floats between tax-free jurisdictions).
(ii) Mr. Thomas, an **Indian citizen** and **member of the crew of an Indian merchant ship**, was on an eligible international voyage. His passport shows he was physically in India for 130 days including the period covered by the Continuous Discharge Certificate; the CDC-voyage period (from port-departure to port-arrival) covers **20 of those days**.

**Answer:**
**(i) Governing provision — Sec 6(1A) (deemed residence):** An **Indian citizen** whose **total income (other than foreign-source income) exceeds ₹15,00,000** and who is **not liable to tax in any other country** by reason of domicile/residence, and who is **not resident under Sec 6(1)**, is **deemed to be resident** in India. 
Nair is not resident under 6(1) (only 90 days). But Indian-source income ₹22,00,000 > ₹15L and he is not liable to tax anywhere → **Sec 6(1A) is triggered → deemed resident.** Such a deemed resident is, by Sec 6(6)(d), **Not Ordinarily Resident (RNOR)**. **Advice: RNOR** — his ₹22L Indian income is taxed; foreign income taxed only if from a business controlled from India.

**(ii) Governing provision — Explanation 2 to Sec 6(1) / Rule 126:** For an Indian citizen who is a member of the crew of an **Indian ship**, the period *between the CDC "signing-on" (port departure) and "signing-off" (port arrival)* on an **eligible voyage is EXCLUDED** from his period of stay in India. 
Excluding the 20 CDC-voyage days: qualifying stay = 130 − 20 = **110 days**. Since 110 < 182 (and assuming <365 days over 4 preceding years / no prior-year linkage), he **fails Sec 6(1)** and is a **Non-Resident**. (Note: the 120-day rule of Q6 applies to *visitors*, not to a resident-Indian seafarer's exclusion computation — his excluded days simply do not count.) **Advice: Non-Resident.**

**Why this way (the reasoning):** These two provisions patrol opposite ends of "stateless" income. **Sec 6(1A)** stops wealthy Indian citizens from becoming "residents of nowhere" — parking income in tax-free havens while claiming NR status in India. The twin gates are objective: Indian income > ₹15L *and* not taxed anywhere; clear both and India *deems* you resident (but only RNOR, so purely foreign income escapes). The seafarer rule, by contrast, is *relieving*: without it, an Indian sailor would rack up "days in India" merely by sailing on an Indian-flag vessel, unfairly turning him resident. Rule 126 therefore *removes* the voyage days. The trap is mixing the two — applying 6(1A) to the sailor, or forgetting that a person deemed resident under 6(1A) is *always* RNOR, never R&OR. Also note 6(1A) is expressly *subordinate* to 6(1): it never applies to someone already resident on days.

*(Full-marks tip: Cite 6(1A) with its "not liable to tax in any other country" condition AND the ₹15L test, and finish with the 6(6)(d) RNOR classification. For the sailor, name Rule 126 / Explanation 2 and *subtract* the CDC period. Confusing the seafarer exclusion with the 120-day visitor rule is the marked error.)*

---

### Q10. Ch: Residential Status — Incidence: foreign business income & remittance (Marks: 5) [Case/Application]
**Question:** For PY 2024-25, Mr. Ghosh is a **Non-Resident**. He earns ₹7,00,000 profit from a business in Singapore that is **partly controlled from India**, the profit being **received in Singapore**; of this he **remits ₹3,00,000 to his Indian savings account** during the year. He also earns ₹2,00,000 interest on that Indian savings account. **Examine the validity** of his accountant's view that "since ₹3,00,000 was brought into India and the business is controlled from India, ₹3,00,000 of the Singapore profit is taxable in India."

**Answer:**
**Governing rule (Sec 5(2)):** For a **Non-Resident**, only income (a) *received/deemed received* in India, or (b) *accruing/deemed to accrue* in India, is taxable. The "business controlled from India" limb of Sec 5(1)(c) applies **only to residents (R&OR and RNOR)** — it is **irrelevant for a Non-Resident**.

- **Singapore business profit ₹7,00,000:** accrues in Singapore and is *first received* in Singapore. For an NR, the "controlled from India" test does **not** extend the charge. Hence the profit is **not taxable**, irrespective of control.
- **Remittance of ₹3,00,000:** mere *remittance* of income already received abroad is **not a receipt** in India (receipt means the *first* receipt). Not taxable.
- **Indian savings interest ₹2,00,000:** accrues and is received in India → **taxable**.

**Conclusion:** The accountant's view is **INVALID** on both counts — neither "control from India" nor the remittance brings the Singapore profit to tax for an NR. Only the ₹2,00,000 Indian interest is taxable. **Total taxable in India = ₹2,00,000.**

**Why this way (the reasoning):** Two misconceptions are corrected here. First, the "business controlled from India" hook belongs to Sec 5(1) (residents) and has **no counterpart in Sec 5(2)** — an NR's foreign business income is untaxed *however* it is managed. Parliament reserved the control-test for residents precisely because NRs are meant to be taxed only on India-*sourced* or India-*received* income. Second, remittance ≠ receipt: the income was already received in Singapore, so moving the money to India later is a capital transfer, not the earning or first-receipt of income. The accountant fuses two wrong ideas (control + remittance) into a phantom charge. Getting the *status-specific* scope of Sec 5 right is the whole point.

*(Full-marks tip: Explicitly say the control-from-India limb does NOT apply to a Non-Resident, and reject remittance as "not first receipt." Cite Sec 5(2). Stating only the conclusion, or taxing the ₹3L remittance, loses most marks.)*

---

### Q11. Ch: Income under Salaries — Rent-Free Accommodation valuation (revised Rule 3) (Marks: 8) [Problem]
**Question:** Mr. Bose is employed in **Mumbai** (population per 2011 census exceeds 40 lakh). His employer provides **rent-free unfurnished** accommodation *owned by the employer*, later furnished. Compute the value of this perquisite for AY 2025-26 from the data below. He is not a Government employee.

| Particulars | Amount (₹) |
|---|---|
| Basic salary | 60,000 p.m. |
| Dearness allowance (60% enters retirement benefits) | 20,000 p.m. |
| Bonus (paid during the year) | 80,000 |
| Fixed commission | 40,000 |
| Taxable special allowance | 36,000 (year) |
| Employer's contribution to RPF | 90,000 (year) |
| Cost of furniture provided by employer | 1,50,000 |
| Rent recovered from Mr. Bose | 2,000 p.m. |

**Solution:**

**WN-1 — "Salary" for RFA valuation:** Include Basic + DA *to the extent it enters retirement benefits* + bonus + commission + all taxable monetary allowances. **Exclude** employer's RPF contribution and any exempt items.

| Component | ₹ |
|---|---|
| Basic (60,000 × 12) | 7,20,000 |
| DA entering retirement benefits (20,000 × 60% × 12) | 1,44,000 |
| Bonus | 80,000 |
| Fixed commission | 40,000 |
| Taxable special allowance | 36,000 |
| **Salary for RFA** | **10,20,000** |

**WN-2 — Base perquisite (employer-owned, revised slab):** For a city with population > 40 lakh, the value of employer-owned unfurnished accommodation = **10% of salary** = 10% × 10,20,000 = **₹1,02,000**.

**WN-3 — Furniture add-on:** 10% p.a. of cost of furniture = 10% × 1,50,000 = **₹15,000**.

**Statement Showing Value of RFA Perquisite — Mr. Bose:**

| Particulars | ₹ |
|---|---|
| 10% of salary (owned, pop > 40 lakh) | 1,02,000 |
| Add: 10% of cost of furniture | 15,000 |
| Value of furnished accommodation | 1,17,000 |
| Less: Rent recovered (2,000 × 12) | (24,000) |
| **Taxable value of RFA perquisite** | **93,000** |

**Answer:** Value of RFA perquisite chargeable to salary = **₹93,000**.

**Why this way (the reasoning):** RFA valuation rests on the idea that the *saved rent* is a benefit, and the benefit scales with the employee's own pay and with city cost-of-living. Post the 2023 amendment to Rule 3, the population brackets were widened (>40 lakh / 15–40 lakh / <15 lakh) and rates lowered to **10% / 7.5% / 5%**, replacing the old 15/10/7.5 on >25 lakh brackets — you must use the *revised* rates. Two subtleties earn the marks: (1) DA is counted **only to the extent it forms part of retirement benefits** (here 60%) — counting full DA overstates salary; (2) employer's **RPF contribution is not "salary"** for this purpose and must be excluded. Furniture is valued *separately* at 10% of cost (or actual hire charges), and *rent recovered* is deducted last because the perquisite is the *net* benefit conferred. Deducting rent before adding furniture, or using full DA, are the routine errors.

*(Full-marks tip: Show the "salary" build-up as a labelled working — examiners award marks for correctly including only the retirement-linked DA portion and excluding RPF. Use the post-2023 10% rate for a >40-lakh city; using the old 15% is an automatic error.)*

---

### Q12. Ch: Income under Salaries — Gratuity exemption (covered by Payment of Gratuity Act) (Marks: 8) [Problem]
**Question:** Mr. Rao retired on 30th November 2024 from XYZ Ltd (a factory **covered by the Payment of Gratuity Act, 1972**) after **26 years and 8 months** of service, receiving gratuity of **₹22,00,000**. At retirement his **Basic = ₹50,000 p.m.** and **DA = ₹20,000 p.m.** (fully). Compute the taxable gratuity for AY 2025-26 and explain how the answer would differ had he **not** been covered by the Act.

**Solution:**

**WN-1 — Completed years (covered by the Act):** Under the Act, service in excess of six months is rounded **up** to a full year. 26 years 8 months (8 > 6) → **27 years**.

**WN-2 — Exemption under Sec 10(10)(ii) — least of three:**
- (a) Notified monetary ceiling = **₹20,00,000**
- (b) Gratuity actually received = **₹22,00,000**
- (c) 15/26 × last drawn salary (Basic + DA) × completed years
  = 15/26 × 70,000 × 27 = (10,50,000 / 26) × 27 = 40,384.62 × 27 = **₹10,90,385**

Least = **₹10,90,385**.

**Statement Showing Taxable Gratuity — Mr. Rao (covered by the Act):**

| Particulars | ₹ |
|---|---|
| Gratuity received | 22,00,000 |
| Less: Exempt u/s 10(10)(ii) [least of (a)/(b)/(c)] | (10,90,385) |
| **Taxable gratuity** | **11,09,615** |

**WN-3 — If NOT covered by the Act (Sec 10(10)(iii)):** Exemption = least of ₹20,00,000; actual ₹22,00,000; and **½ × average salary of last 10 months × completed years (fractions ignored → 26 years)**, where salary = Basic + DA (if in terms) + commission (% of turnover). With average Basic+DA ≈ ₹70,000: ½ × 70,000 × 26 = **₹9,10,000** → taxable = 22,00,000 − 9,10,000 = **₹12,90,000**.

**Answer:** Taxable gratuity (covered) = **₹11,09,615**; if not covered ≈ **₹12,90,000**.

**Why this way (the reasoning):** Gratuity exemption differs *mechanically* by whether the employer is covered by the 1972 Act, and confusing the two limbs is the classic error. **Covered:** use **15/26** of the *last drawn* Basic+DA and round completed service **up** for >6 months. **Not covered:** use **½ month of the *average* Basic+DA (last 10 months)** and **ignore** any fraction of a year. Two traps sit inside WN-1/WN-3: (1) the "8 months" rounds *up* to a whole year *only* under the covered formula — under the non-covered formula fractions are *dropped* (27 vs 26 years); (2) "salary" for the covered formula is *last drawn*, for the non-covered it is a *10-month average*. The ceiling (₹20L) and actual are common to both. The economic logic: the exemption approximates a statutory/normative gratuity entitlement, so anything the employer pays *above* that norm is a taxable perquisite of employment.

*(Full-marks tip: Label the section (10(10)(ii) vs (iii)) and show all three limbs of "least of." The examiner specifically checks the rounding (up vs ignore) and last-drawn vs average distinction. Using 26 divisor with average salary, or ignoring the fraction under the covered formula, loses marks.)*

---

### Q13. Ch: Income under Salaries — Leave encashment exemption on retirement (Marks: 6) [Problem]
**Question:** Ms. Pillai, a **non-Government employee**, retired on 31st March 2025 after **24 years** of service and received **leave salary of ₹12,00,000**. Her employer allowed **40 days' leave for each year of service**; she had **availed 150 days** during service. Average salary (Basic + DA in terms) for the last 10 months = **₹50,000 p.m.** Compute the taxable leave encashment for AY 2025-26.

**Solution:**

**WN-1 — Leave to the credit (capped at 30 days/year of service, per Sec 10(10AA)):**
Leave credit = (30 days × 24 years) − leave availed, using the statutory 30-day entitlement, *not* the employer's 40 days.
= 720 − 150 = **570 days**.

**WN-2 — Cash equivalent of leave to credit:** Daily salary = 50,000 / 30 = ₹1,666.67. Cash equivalent = 570 × 1,666.67 = **₹9,50,000**.

**WN-3 — Exemption u/s 10(10AA)(ii) — least of four:**
- (a) Notified ceiling (non-Govt, revised w.e.f. 1.4.2023) = **₹25,00,000**
- (b) Leave salary actually received = **₹12,00,000**
- (c) 10 months × average salary = 10 × 50,000 = **₹5,00,000**
- (d) Cash equivalent of leave to credit (WN-2) = **₹9,50,000**

Least = **₹5,00,000**.

**Statement Showing Taxable Leave Encashment — Ms. Pillai:**

| Particulars | ₹ |
|---|---|
| Leave salary received | 12,00,000 |
| Less: Exempt u/s 10(10AA)(ii) [least of four] | (5,00,000) |
| **Taxable leave encashment** | **7,00,000** |

**Answer:** Taxable leave encashment = **₹7,00,000**.

**Why this way (the reasoning):** The single most powerful trap here is limb (d): leave-to-credit must be computed at the **statutory maximum of 30 days per year**, *even though the employer granted 40 days*. A student who uses 40 days (960 − 150 = 810 days) overstates the cash equivalent and mis-picks the least. The other decisive point is that the **10-month-salary cap (limb c = ₹5,00,000)** is usually the binding constraint on retirement — it exists to prevent inflating the exemption by hoarding leave. The raised ₹25 lakh ceiling (from the old ₹3 lakh) is now rarely the binding limb but must still be listed. Conceptually, encashment of *earned but unused* leave is deferred salary; the exemption approximates a reasonable accumulation, and anything beyond the four-fold least is taxed as the salary it truly is.

*(Full-marks tip: Compute leave credit strictly at 30 days/year regardless of the employer's higher grant, and list all four limbs. Full marks require identifying WHY ₹5,00,000 (10-month cap) is the binding limb. Using the employer's 40-day rate is the standard mark-loser.)*

---

### Q14. Ch: Income under Salaries — Commuted pension exemption logic (Marks: 6) [Problem]
**Question:** Mr. Menon, a **non-Government employee**, retired and receives an **uncommuted (monthly) pension of ₹20,000 p.m. for the 6 months** Oct 2024–Mar 2025. On retirement he also **commuted 40% of his pension** and received a lump sum of **₹8,00,000**. Compute the taxable pension for AY 2025-26 (i) if he **also received gratuity**, and (ii) if he **did not receive any gratuity**, explaining the difference.

**Solution:**

**WN-1 — Full value of commuted pension:** He commuted 40% for ₹8,00,000. Therefore 100% commuted value = 8,00,000 ÷ 40% = **₹20,00,000**.

**WN-2 — Exemption of commuted pension u/s 10(10A)(ii):**
- **If gratuity received:** exempt = **1/3 of full value** = 1/3 × 20,00,000 = **₹6,66,667**.
- **If no gratuity received:** exempt = **1/2 of full value** = 1/2 × 20,00,000 = **₹10,00,000**.

**WN-3 — Uncommuted pension:** Fully taxable for all employees. = 20,000 × 6 = **₹1,20,000**.

**Statement Showing Taxable Pension — Mr. Menon:**

| Particulars | Case (i): gratuity received (₹) | Case (ii): no gratuity (₹) |
|---|---|---|
| Commuted pension received | 8,00,000 | 8,00,000 |
| Less: Exempt u/s 10(10A)(ii) | (6,66,667) | (10,00,000 → limited to 8,00,000) |
| Taxable commuted pension | 1,33,333 | Nil |
| Add: Uncommuted pension (taxable in full) | 1,20,000 | 1,20,000 |
| **Total taxable pension** | **2,53,333** | **1,20,000** |

**Answer:** (i) With gratuity = **₹2,53,333**; (ii) without gratuity = **₹1,20,000** (commuted portion fully exempt).

**Why this way (the reasoning):** Pension has two streams and they are taxed differently. **Uncommuted (periodic) pension is always fully taxable** as salary — it is simply deferred wages. **Commuted (lump-sum) pension** is a capitalised advance of future pension, and the law gives a *larger* exemption to those who did *not* also get gratuity (½ of full value) than to those who did (⅓), because gratuity is a *separate* tax-favoured retirement cushion — giving both the ½ commutation relief *and* gratuity relief would over-subsidise. The pivotal step students miss is **grossing up**: ₹8,00,000 is only *40%* of the pension, so the *full* value is ₹20,00,000, and the ⅓ or ½ is applied to that full value, not to the ₹8,00,000 received. In case (ii) the ½ exemption (₹10L) exceeds the amount received (₹8L), so the commuted pension is *fully* exempt — exemption cannot exceed the receipt.

*(Full-marks tip: Gross up to full commuted value BEFORE applying ⅓ or ½ — this is the marked step. Apply ⅓ with gratuity, ½ without; keep uncommuted fully taxable. Cap the exemption at the amount received in case (ii). Applying the fraction directly to ₹8,00,000 is the common error.)*

---

### Q15. Ch: Income under Salaries — Integrated computation: salary + RFA + retirement benefits (Marks: 10) [Problem]
**Question:** Mr. Khanna retired from ABC Ltd (**not** covered by the Payment of Gratuity Act; located in **Delhi**, population > 40 lakh) on **31st December 2024** after **30 years** of service. Compute his **income under the head "Salaries"** for AY 2025-26 (he does not opt for the new regime; standard deduction ₹50,000). All figures relate to the year unless stated p.m.

| Particulars | Amount |
|---|---|
| Basic salary (Apr–Dec 2024) | 80,000 p.m. |
| DA (40% enters retirement benefits) | 30,000 p.m. |
| Rent-free unfurnished accommodation (employer-owned) — provided Apr–Dec 2024 | — |
| Gratuity received on retirement | 15,00,000 |
| Average Basic + DA(in terms) for last 10 months | 92,000 p.m. |
| Leave salary received (leave to credit 300 days @30-day rule) | 9,00,000 |
| Uncommuted pension (Jan–Mar 2025) | 25,000 p.m. |

**Solution:**

**WN-1 — Salary for the 9 working months (Apr–Dec 2024):**
Basic = 80,000 × 9 = ₹7,20,000; DA = 30,000 × 9 = ₹2,70,000 (DA taxable in full as salary). 

**WN-2 — RFA (owned, Delhi >40 lakh, 9 months):** Salary for RFA = Basic + DA-in-retirement portion for the period the accommodation was provided = (80,000 × 9) + (30,000 × 40% × 9) = 7,20,000 + 1,08,000 = ₹8,28,000. RFA = 10% × 8,28,000 = **₹82,800**.

**WN-3 — Gratuity (not covered; Sec 10(10)(iii)):** Exempt = least of ₹20,00,000; actual ₹15,00,000; ½ × avg salary × completed years (ignore fraction) = ½ × 92,000 × 30 = ₹13,80,000. Least = ₹13,80,000. **Taxable gratuity = 15,00,000 − 13,80,000 = ₹1,20,000.**

**WN-4 — Leave encashment (Sec 10(10AA)(ii)):** Exempt = least of ₹25,00,000; actual ₹9,00,000; 10 × 92,000 = ₹9,20,000; cash equiv of leave to credit = 300 × (92,000/30) = 300 × 3,066.67 = ₹9,20,000. Least = ₹9,00,000. **Taxable leave salary = 9,00,000 − 9,00,000 = Nil.**

**WN-5 — Uncommuted pension:** Fully taxable = 25,000 × 3 = **₹75,000**.

**Statement Showing Income under the Head "Salaries" — Mr. Khanna (AY 2025-26):**

| Particulars | ₹ |
|---|---|
| Basic salary | 7,20,000 |
| Dearness allowance | 2,70,000 |
| Value of RFA perquisite (WN-2) | 82,800 |
| Taxable gratuity (WN-3) | 1,20,000 |
| Taxable leave encashment (WN-4) | Nil |
| Uncommuted pension (WN-5) | 75,000 |
| Gross salary | 12,67,800 |
| Less: Standard deduction u/s 16(ia) | (50,000) |
| **Income under the head "Salaries"** | **12,17,800** |

**Answer:** Income under "Salaries" = **₹12,17,800**.

**Why this way (the reasoning):** This question rewards *sequencing* discipline. Each retirement benefit is exemption-tested on its **own** rule before anything is aggregated — you cannot net gratuity, leave and pension together. Note how the differing "salary" definitions bite: RFA counts DA only to its *retirement-benefit* portion (40%), but plain DA is fully taxable salary; gratuity (non-covered) uses *average* salary and *drops* the fraction of a year; leave encashment is capped by the *10-month* limb (here ₹9.2L, though actual ₹9L is lower, giving full exemption). A student who forgets that **DA remains fully taxable** even after being partly used for RFA valuation will understate salary. Finally, the standard deduction of ₹50,000 (old regime) is applied once at the end on the *aggregate* — it is not a per-source deduction. The whole exercise embodies the principle that "Salaries" taxes *total employment reward*, with each statutory exemption a narrowly-defined carve-out you must justify item-by-item.

*(Full-marks tip: Present each retirement benefit as a separate WN with its own "least of" test, then a single consolidated statement. Examiners deduct for netting exemptions, dropping DA from taxable salary after RFA, or applying standard deduction before aggregation. Show the RFA salary base separately from the taxable-DA figure.)*

---

### Q16. Ch: Income under Salaries — Perquisites: interest-free loan, motor car & ESOP (Marks: 8) [Problem]
**Question:** Mr. Sharma is employed with PQR Ltd. Compute the **value of the following perquisites** for AY 2025-26, with reasons.

| Particulars | Details |
|---|---|
| Interest-free loan for a car | ₹6,00,000 taken on 1 Apr 2024, ₹50,000 p.m. repaid from 1 Jan 2025; SBI rate on car loans as on 1 Apr 2024 = 9% p.a. |
| Motor car (1.8 litre engine) | Owned by employer, used for **both official and personal** purposes; **running & maintenance met by employer**; no chauffeur |
| Sweat equity / ESOP shares allotted | 1,000 shares allotted on 1 Aug 2024; FMV on date of exercise ₹500; amount recovered from employee ₹120 per share |
| Free meals in office (working days) | ₹80 per meal for 240 days, paid via non-transferable meal vouchers |

**Solution:**

**WN-1 — Interest-free loan (Rule 3(7)(i)):** Value = SBI rate (9%) on the **maximum outstanding monthly balance** (last day of each month). Loan ₹6,00,000 from Apr–Dec (9 months); repayments of ₹50,000 begin 1 Jan.
- Apr–Dec (9 months): balance ₹6,00,000 → interest = 6,00,000 × 9% × 9/12 = ₹40,500.
- Jan: closing balance 5,50,000; Feb: 5,00,000; Mar: 4,50,000 → sum = 15,00,000 × 9% × 1/12 = ₹11,250.
Perquisite value = 40,500 + 11,250 = **₹51,750**. (No exemption, as loan > ₹20,000 and not for specified medical treatment.)

**WN-2 — Motor car (Rule 3(2), >1.6 litre, part-official/part-personal, expenses by employer, no chauffeur):** Value = **₹2,400 p.m.** = 2,400 × 12 = **₹28,800**. (Actual expenses irrelevant — a flat sum applies since use is mixed and employer bears costs.)

**WN-3 — Sweat equity / ESOP (Sec 17(2)(vi)):** Perquisite = (FMV on exercise − amount recovered) × shares = (500 − 120) × 1,000 = **₹3,80,000**.

**WN-4 — Free meals:** Meal vouchers/meals up to ₹50 per meal are exempt; excess is taxable. Value = (80 − 50) × 240 = **₹7,200** taxable. *(Under old-regime treatment the ₹50/meal concession applies; the entire benefit would be taxable under the new regime.)*

**Statement Showing Value of Perquisites — Mr. Sharma:**

| Perquisite | ₹ |
|---|---|
| Interest-free loan (WN-1) | 51,750 |
| Motor car (WN-2) | 28,800 |
| Sweat equity shares (WN-3) | 3,80,000 |
| Free meals excess (WN-4) | 7,200 |
| **Total perquisite value** | **4,67,750** |

**Answer:** Total taxable perquisites = **₹4,67,750**.

**Why this way (the reasoning):** Each perquisite has a bespoke valuation philosophy. The **loan** perquisite measures the *saved interest*, valued at the **SBI benchmark rate** on the **maximum monthly outstanding balance** — you must track the falling balance after repayments start, not apply 9% flatly to ₹6,00,000. The **motor car** is *not* valued at actual cost when use is mixed and the employer bears expenses: the law substitutes a **standard sum (₹2,400 for >1.6L, ₹1,800 for ≤1.6L)** to avoid disputes over the personal-use fraction — a deliberate proxy. **ESOP** perquisite crystallises the *market gain* at exercise (FMV minus what the employee actually paid) because that discount is a reward for employment. **Meals** enjoy a small ₹50/meal concession to keep ordinary canteen benefits untaxed; only the excess is a perquisite. The consistent thread: a perquisite taxes the *benefit conferred*, but the *method* of measuring it (actual vs prescribed proxy) is fixed by the Rules for each type.

*(Full-marks tip: For the loan, show the month-wise maximum-outstanding-balance working — flat 9% on the original ₹6L is the marked error. Use the ₹2,400 flat car value, not actual expenses. State the FMV-minus-recovery basis for ESOP and the ₹50/meal concession. Reasons alongside each figure are expected at 8 marks.)*

---

### Q17. Ch: Income under Salaries + Basic Concepts — Salary computation & regime choice (Marks: 10) [Problem]
**Question:** Mr. Iyer (resident, 42) furnishes the following for AY 2025-26. Compute his **income under "Salaries" under both regimes** and his **tax liability under each**, then **advise** which regime to choose. He can claim, under the old regime, HRA exemption of ₹1,20,000, Sec 80C ₹1,50,000, and 80D ₹25,000; the new regime allows none of these but a higher standard deduction of ₹75,000.

| Particulars | Amount (₹) |
|---|---|
| Basic salary | 12,00,000 |
| Dearness allowance (fully taxable) | 3,00,000 |
| House rent allowance received | 3,60,000 |
| Employer's contribution to NPS u/s 80CCD(2) (14% of Basic) | 1,68,000 |
| Professional tax paid | 2,500 |

**Solution:**

**WN-1 — Gross salary before standard deduction:**
Basic 12,00,000 + DA 3,00,000 + HRA 3,60,000 + Employer NPS 1,68,000 = **₹19,68,000** (employer NPS contribution is includible in salary, then separately deductible u/s 80CCD(2) under both regimes).

**WN-2 — Income under "Salaries":**

| Particulars | Old Regime (₹) | New Regime (₹) |
|---|---|---|
| Gross salary (WN-1) | 19,68,000 | 19,68,000 |
| Less: HRA exemption u/s 10(13A) | (1,20,000) | Not allowed |
| Less: Standard deduction u/s 16(ia) | (50,000) | (75,000) |
| Less: Professional tax u/s 16(iii) | (2,500) | Not allowed |
| **Gross salary after 16** | 17,95,500 | 18,93,000 |

**WN-3 — Deductions under Chapter VI-A:**
- Old: 80C ₹1,50,000 + 80D ₹25,000 + 80CCD(2) ₹1,68,000 = ₹3,43,000.
- New: only 80CCD(2) ₹1,68,000 (the sole Chapter VI-A deduction allowed under 115BAC).

**Statement Showing Total Income & Tax — Mr. Iyer:**

| Particulars | Old (₹) | New (₹) |
|---|---|---|
| Salary after Sec 16 | 17,95,500 | 18,93,000 |
| Less: Chapter VI-A (WN-3) | (3,43,000) | (1,68,000) |
| **Total Income** | **14,52,500** | **17,25,000** |

**WN-4 — Tax (old regime) on ₹14,52,500:** 12,500 + 1,00,000 + (4,52,500 × 30%) = 12,500 + 1,00,000 + 1,35,750 = ₹2,48,250. + 4% cess ₹9,930 → **₹2,58,180**.

**WN-5 — Tax (new regime) on ₹17,25,000:** 20,000 + 30,000 + 30,000 + 60,000 + (2,25,000 × 30% = 67,500) = ₹2,07,500. + 4% cess ₹8,300 → **₹2,15,800**.

**Answer:** Old-regime tax = **₹2,58,180**; New-regime tax = **₹2,15,800**. **Advise the new regime** — it saves **₹42,380** despite forgoing HRA/80C/80D, because its lower slab rates and ₹75,000 standard deduction outweigh the lost deductions at this income.

**Why this way (the reasoning):** The regime decision is *not* answered by "who has more deductions" but by comparing *final tax*. Two structural facts drive it: (1) **80CCD(2) — the employer's NPS contribution — survives under BOTH regimes**, so it is neutral to the choice and must be allowed even in the new regime (students who deny it under the new regime overstate new-regime income). (2) The new regime's *rate schedule* is materially gentler (a 5/10/15/20% ladder up to ₹15L vs the old 5/20/30% jumps), and its ₹75,000 standard deduction exceeds the old ₹50,000. Here the taxpayer's old-regime deductions (~₹1.75L of 80C/80D/HRA) reduce income by less than the *rate advantage* the new regime confers, so the new regime wins. The lesson: always compute *both* total incomes and *both* taxes — the deduction-rich intuition is frequently wrong once slab rates change.

*(Full-marks tip: Show employer NPS 80CCD(2) as allowed under BOTH regimes — this is the marked discriminator. Compute tax under each regime fully (with cess) and give a quantified advice line. Merely comparing total incomes, or denying 80CCD(2) in the new regime, forfeits the concluding marks.)*

### Q18. Ch: Income from House Property — Self-occupied vs deemed let-out with pre-construction interest (Marks: 8) [Problem]
**Question:** Mr. Arvind owns three houses. He uses House-A and House-B for his own residence and keeps House-C vacant throughout the year (it was never let out and he does not occupy it because he lives in A and B). Compute his income under "Income from House Property" for AY 2025-26 under the **default (new) regime** and, separately, comment on how the answer changes under the **old regime**. Data:

| Particulars | House-A | House-B | House-C |
|---|---|---|---|
| Municipal Value (p.a.) | ₹3,00,000 | ₹2,40,000 | ₹4,20,000 |
| Fair Rent (p.a.) | ₹3,60,000 | ₹2,20,000 | ₹4,00,000 |
| Standard Rent (p.a.) | ₹3,30,000 | — | ₹3,80,000 |
| Municipal taxes paid by owner | ₹30,000 | ₹24,000 | ₹42,000 |
| Interest on loan (current year) | ₹2,60,000 | Nil | ₹1,90,000 |
| Loan taken for | Construction (completed 10-May-2021) | — | Purchase (completed 01-Jun-2019) |

Pre-construction interest for House-A: loan taken 01-Apr-2018, ₹20,00,000 @ 10%; construction completed 10-May-2021.

**Solution:**

**WN-1 — Choice of self-occupied houses.** Sec 23(2)/(4): a person may treat any **two** houses as self-occupied (NAV = Nil); the remaining house(s) are **deemed let-out**. Arvind occupies A and B and keeps C vacant. Since he owns three houses, only two can enjoy Nil NAV; one house must be deemed let-out. He should deem let-out the house that gives the **least taxable income after interest**, i.e. optimise. Test each combination — the deemed-let-out house's income (GAV − taxes − 30% − interest) vs the interest allowed if kept self-occupied (capped ₹2,00,000 old regime / Nil new regime).

**WN-2 — Pre-construction interest, House-A.** Period 01-Apr-2018 to 31-Mar-2021 (year prior to completion year) = 3 years. Annual interest = 20,00,000 × 10% = ₹2,00,000. Total PCI = ₹6,00,000, allowed in 5 equal instalments from completion year (FY 2021-22) → ₹1,20,000 p.a. for FY 2021-22 to 2025-26. AY 2025-26 falls in the window, so PCI instalment = **₹1,20,000**.

**WN-3 — If House-C is deemed let-out (recommended).** GAV = higher of MV/FR, capped at Standard Rent = higher of (4,20,000 MV, 4,00,000 FR) = 4,20,000, but SR 3,80,000 caps it → GAV = ₹3,80,000. Less municipal taxes ₹42,000 → NAV ₹3,38,000. Less 30% std deduction ₹1,01,400 → ₹2,36,600. Less interest ₹1,90,000 → **₹46,600** income.

**WN-4 — Interest on A and B if self-occupied.** New regime: interest on self-occupied house is **not deductible** (loss from SOP disallowed). Old regime: A's interest 2,60,000 + PCI 1,20,000 = 3,80,000, capped at ₹2,00,000 (loan for construction, completed within 5 years). B: Nil.

| Statement of House Property Income (AY 2025-26) | New Regime (₹) | Old Regime (₹) |
|---|---|---|
| House-A (SOP) — NAV | Nil | Nil |
| Less: Interest u/s 24(b) | Nil | (2,00,000) |
| House-B (SOP) — NAV | Nil | Nil |
| House-C (Deemed let-out) — WN-3 | 46,600 | 46,600 |
| **Income from House Property** | **46,600** | **(1,53,400)** |

**Answer:** Income from House Property = **₹46,600** (new regime); **loss of ₹1,53,400** (old regime), of which set-off against other heads is capped at ₹2,00,000 (here the full loss is allowed as it is below the cap).

**Why this way (the reasoning):** The whole question turns on a scarcity: only two houses can be Nil-NAV, so with three houses one is *forced* into deemed-let-out. Students wrongly assume a *vacant* house escapes tax — it does not; Sec 23 taxes ownership capacity to earn, not actual receipt, so a vacant non-let house is deemed let-out on notional rent. The optimisation logic is that you choose to keep as SOP the houses where "losing" the Nil-NAV benefit costs you most, and deem-let-out the one whose net taxable figure is smallest. In the new regime the trap is that self-occupied interest gives *zero* benefit (Sec 24(b) SOP loss barred), so paying ₹2,60,000 interest on House-A yields nothing — a key advisory point that flips regime choice. GAV is capped by standard rent because rent-control law prevents the owner from *ever* legally charging more, so notional income cannot exceed what the law permits him to collect.

*(Full-marks tip: examiners reward showing the two/three-house optimisation explicitly and the PCI 5-instalment schedule with dates; the common deduction is treating the vacant house as Nil-NAV or allowing SOP interest under the new regime.)*

---

### Q19. Ch: Income from House Property — Unrealised rent recovered & arrears of rent (Marks: 6) [Problem]
**Question:** Mrs. Kavita let out a property at ₹40,000 p.m. In FY 2022-23 the tenant defaulted for 4 months; the unrealised rent of ₹1,60,000 satisfied all Rule 4 conditions and was excluded from GAV that year. In FY 2024-25 (AY 2025-26) she recovered ₹1,20,000 of that unrealised rent, and also received ₹90,000 as **arrears of rent** (a court-ordered enhancement for earlier years). The property was let throughout FY 2024-25 at ₹40,000 p.m.; municipal taxes paid ₹30,000; MV ₹4,00,000, FR ₹4,60,000, SR ₹4,80,000. Compute her House Property income for AY 2025-26.

**Solution:**

**WN-1 — GAV for FY 2024-25 (regular letting).** Expected Rent = higher of MV 4,00,000 and FR 4,60,000 = 4,60,000, capped by SR 4,80,000 → 4,60,000. Actual Rent Received = 40,000 × 12 = 4,80,000. GAV = higher of ER and actual rent = **₹4,80,000** (no vacancy, no current-year unrealised rent).

**WN-2 — NAV & standard deduction.** NAV = 4,80,000 − 30,000 = 4,50,000. Less 30% = 1,35,000 → 3,15,000.

**WN-3 — Recovery of unrealised rent u/s 25A.** ₹1,20,000 recovered is taxable in the year of recovery **irrespective of ownership** in that year; a flat **30% deduction** is allowed and no other deduction. Taxable = 1,20,000 × 70% = **₹84,000**.

**WN-4 — Arrears of rent u/s 25A.** ₹90,000 arrears taxable in year of receipt, also after **30% deduction**. Taxable = 90,000 × 70% = **₹63,000**.

| Statement of House Property Income (AY 2025-26) | ₹ |
|---|---|
| GAV (WN-1) | 4,80,000 |
| Less: Municipal taxes | (30,000) |
| Net Annual Value | 4,50,000 |
| Less: Std deduction 30% u/s 24(a) | (1,35,000) |
| Sub-total (regular letting) | 3,15,000 |
| Add: Unrealised rent recovered 25A (net of 30%) | 84,000 |
| Add: Arrears of rent 25A (net of 30%) | 63,000 |
| **Income from House Property** | **4,62,000** |

**Answer:** Income from House Property for AY 2025-26 = **₹4,62,000**.

**Why this way (the reasoning):** Sec 25A is a special charging provision that fixes a timing mismatch. When rent could not be realised earlier and was rightly excluded from GAV, the tax on it was deferred — not forgiven. So when it is finally recovered, the law "catches up" and taxes it, but because the standard 30% deduction under Sec 24(a) was never given on that slice earlier, Sec 25A grants a flat 30% here as a proxy for repairs/collection cost. The crucial subtlety students miss: 25A operates **even if you no longer own the property** in the recovery year — the income attaches to the historical letting, not present ownership — and it is charged *separately*, so you do not re-open the old year's computation. Arrears of rent works on the identical logic (income relating to an earlier period but received now), which is why both get the same 30% treatment and are added after the current year's normal NAV computation, never inside GAV.

*(Full-marks tip: the examiner looks for the flat 30% on 25A items and the statement that current-year ownership is irrelevant; losing marks comes from netting the recovery inside GAV or forgetting the 30% deduction on arrears.)*

---

### Q20. Ch: Profits & Gains of Business or Profession — Section 43B disallowance and the "actual payment" logic (Marks: 8) [Problem]
**Question:** Zenith Ltd (company, accounts audited, due date 31-Oct-2025) debited the following to its P&L for FY 2024-25. Compute the amount to be **added back / allowed** under Sec 43B and state the year of allowance for each:

| Item | Amount (₹) | Payment status |
|---|---|---|
| GST payable | 5,00,000 | ₹3,00,000 paid on 20-Sep-2025; ₹2,00,000 paid on 15-Dec-2025 |
| Employer's PF contribution | 2,40,000 | Paid on 05-Nov-2025 |
| Bonus to employees | 4,00,000 | Paid on 25-Oct-2025 |
| Interest on term loan from a **NBFC** | 3,50,000 | Unpaid; converted into a fresh loan on 31-Mar-2025 |
| Interest on loan from **SBI** | 1,80,000 | ₹1,00,000 paid; ₹80,000 unpaid as on due date |
| Leave encashment payable | 1,20,000 | Unpaid till date of filing |
| Sum payable to a **micro enterprise** (MSME) for goods, due 30 days | 2,60,000 | Paid on 10-May-2025 (beyond 15 days but within return date) |

**Solution:**

**WN-1 — GST (Sec 43B(a)).** Allowed only on actual payment. ₹3,00,000 paid before due date (31-Oct-2025) → allowed FY 2024-25. ₹2,00,000 paid 15-Dec-2025 (after due date) → **disallowed** FY 2024-25, allowed FY 2025-26.

**WN-2 — Employer PF (Sec 43B(b)).** Paid 05-Nov-2025, **after** due date of return (31-Oct-2025) → disallowed FY 2024-25; allowed in FY of payment. (Note: this is the *employer's* own contribution — governed by 43B, not 36(1)(va).)

**WN-3 — Bonus (43B(c)).** Paid 25-Oct-2025, before due date → **allowed** FY 2024-25.

**WN-4 — Interest to NBFC (43B(da)).** Interest converted into a fresh loan is **not** "actually paid" → disallowed. Explanation to 43B: conversion into a loan/advance does not amount to payment. Disallowed ₹3,50,000; allowed when the funded interest is actually paid.

**WN-5 — Interest to SBI (43B(d)).** ₹1,00,000 paid → allowed. ₹80,000 unpaid till due date → disallowed FY 2024-25; allowed on payment.

**WN-6 — Leave encashment (43B(f)).** Allowed only on actual payment; unpaid → **disallowed ₹1,20,000**.

**WN-7 — MSME sum (43B(h)).** Payment to a micro/small enterprise beyond the Sec 15 MSMED time-limit (here 30 days) is allowed **only in the year of actual payment**; the proviso permitting payment up to return-filing date does **NOT** apply to clause (h). Paid 10-May-2025, i.e. FY 2025-26 → **disallowed FY 2024-25**, allowed FY 2025-26.

| Item | Debited (₹) | Disallowed FY 2024-25 (₹) |
|---|---|---|
| GST | 5,00,000 | 2,00,000 |
| Employer PF | 2,40,000 | 2,40,000 |
| Bonus | 4,00,000 | Nil |
| Interest — NBFC (converted) | 3,50,000 | 3,50,000 |
| Interest — SBI | 1,80,000 | 80,000 |
| Leave encashment | 1,20,000 | 1,20,000 |
| MSME payment | 2,60,000 | 2,60,000 |
| **Total add-back** | | **12,50,000** |

**Answer:** Amount to be added back under Sec 43B for FY 2024-25 = **₹12,50,000**.

**Why this way (the reasoning):** Sec 43B enforces a "pay-to-claim" discipline on statutory/contractual liabilities that businesses were parking as accruals to reduce tax while sitting on the cash. For most 43B items the first proviso is generous — pay any time up to the return due date and you still get the current year's deduction. Two traps make this question hard. First, **clause (h) (MSME dues) has no such proviso**: Parliament wanted to force prompt cash to small suppliers, so payment even one day beyond the MSMED limit pushes the deduction to the payment year regardless of return date — the single most examined 2024-25 amendment. Second, the **conversion of interest into a fresh loan is expressly deemed not to be payment**, because otherwise a borrower could "pay" interest with a promise and defeat the section's whole cash-basis purpose. Note the employer's PF here rides on 43B (its own contribution), unlike the *employees'* contribution which lives in 36(1)(va) with the harsher "due date under the PF Act" test.

*(Full-marks tip: state the year of allowance for each disallowed item and flag that 43B(h) excludes the return-date proviso; the classic mark loss is applying the general proviso to the MSME dues or treating loan conversion as payment.)*

---

### Q21. Ch: Profits & Gains of Business or Profession — Section 40(a)(ia) TDS default, 30% disallowance and reversal (Marks: 6) [Problem]
**Question:** Mr. Deepak (individual, turnover ₹3 crore, subject to tax audit) paid the following during FY 2024-25 without/short deducting TDS. Determine the amount disallowed under Sec 40(a)(ia) for AY 2025-26 and the year of subsequent allowance:

| Payment | Amount (₹) | TDS position |
|---|---|---|
| Contractor charges (194C) | 8,00,000 | No TDS deducted |
| Professional fees (194J) | 5,00,000 | TDS deducted, deposited 10-Nov-2025 (before return due date 31-Oct-2025? No — after) |
| Commission (194H) | 2,00,000 | TDS deducted & deposited on time |
| Rent (194I) | 6,00,000 | Payee is a resident who has offered this rent in his ROI and paid tax; Form 26A obtained |
| Interest to resident (194A) | 1,50,000 | Short-deducted: deducted on ₹1,00,000 only |

**Solution:**

**WN-1 — Contractor (no TDS).** 30% of expense disallowed = 30% × 8,00,000 = **₹2,40,000**. Allowed in the year TDS is subsequently deducted & paid.

**WN-2 — Professional fees (deposited after return due date).** TDS deducted but deposited 10-Nov-2025, after 31-Oct-2025 → treated as failure → 30% disallowed = 30% × 5,00,000 = **₹1,50,000**; allowed in FY of deposit (FY 2025-26).

**WN-3 — Commission.** TDS deducted and deposited in time → **no disallowance**.

**WN-4 — Rent, Form 26A route.** Proviso to 40(a)(ia)/Sec 201(1): if the resident payee has furnished his return, included the sum, paid tax thereon and the payer obtains a CA certificate in **Form 26A**, the payer is deemed to have deducted → **no disallowance**.

**WN-5 — Interest, short deduction.** Disallowance applies on the **proportion on which tax was not deducted**. TDS done on 1,00,000 of 1,50,000; shortfall base = 50,000 → 30% × 50,000 = **₹15,000** disallowed.

| Item | Amount (₹) | Disallowed 40(a)(ia) (₹) |
|---|---|---|
| Contractor | 8,00,000 | 2,40,000 |
| Professional fees | 5,00,000 | 1,50,000 |
| Commission | 2,00,000 | Nil |
| Rent (Form 26A) | 6,00,000 | Nil |
| Interest (short) | 1,50,000 | 15,000 |
| **Total** | | **4,05,000** |

**Answer:** Disallowance u/s 40(a)(ia) for AY 2025-26 = **₹4,05,000**; each disallowed sum is allowed in the year TDS is deducted-and-paid (professional fees in FY 2025-26).

**Why this way (the reasoning):** Sec 40(a)(ia) is a *collection* tool, not a penalty on the expense — it withholds only **30%**, a deliberate softening from the earlier 100%, because the object is to nudge deductors into compliance, not to confiscate genuine business costs. The reasoning that unlocks the tricky parts: (1) TDS deducted but deposited after the return due date is treated the same as non-deduction, since the government still hasn't received the money in time — timing is the whole point. (2) For **short** deduction, disallowing the full expense would be disproportionate, so the 30% bites only the *slice* that escaped TDS. (3) The **Form 26A** proviso reflects the principle that TDS is only a *mechanism* to collect the payee's tax — if the payee has already paid it, insisting on disallowance would over-collect, so once a CA certifies the payee's compliance the deductor is off the hook. Students who apply 100%, or disallow the whole interest instead of the shortfall, or ignore the 26A relief, lose the marks that separate a rank-holder answer.

*(Full-marks tip: show the 30% rate, the proportional base for short deduction, and name Form 26A; common deductions are 100% disallowance and ignoring the deposit-timing rule.)*

---

### Q22. Ch: Profits & Gains of Business or Profession — Section 40A(3) cash payments & Rule 6DD exceptions (Marks: 5) [Problem]
**Question:** Examine each transaction of M/s Ganga Traders (FY 2024-25) and state the amount disallowed u/s 40A(3):

| # | Transaction | Amount (₹) |
|---|---|---|
| 1 | Paid ₹28,000 by cash to a supplier on 3-Jun and ₹15,000 cash to the same supplier on 3-Jun (two bills of ₹28,000 & ₹15,000) | 43,000 |
| 2 | Paid ₹45,000 in cash for purchase of goods, on a day the bank was on strike (declared holiday) | 45,000 |
| 3 | Paid ₹1,20,000 to a transporter (plying/hiring of goods carriage) in cash | 1,20,000 |
| 4 | Paid ₹38,000 by bearer cheque for machinery repairs | 38,000 |
| 5 | Paid ₹50,000 cash to a farmer for agricultural produce grown by him | 50,000 |

**Solution:**

**WN-1 — Item 1 (aggregate per person per day).** Sec 40A(3) triggers when payments to **one person in one day** exceed ₹10,000, even across multiple bills. 28,000 + 15,000 = 43,000 > 10,000 → **entire ₹43,000 disallowed**. (Each single payment already exceeds ₹10,000 too.)

**WN-2 — Item 2 (bank holiday, Rule 6DD).** Rule 6DD(j): payment on a day banks were closed due to holiday/strike is an exception → **nil disallowance**.

**WN-3 — Item 3 (transporter, higher limit).** For payment to a transporter for plying/hiring/leasing goods carriages, the threshold is **₹35,000**, not ₹10,000. ₹1,20,000 paid in cash exceeds ₹35,000 → **entire ₹1,20,000 disallowed**.

**WN-4 — Item 4 (bearer cheque).** Payment by bearer/crossed-bearer cheque is treated as cash (not account-payee) → 38,000 > 10,000 → **disallowed ₹38,000**. (It is revenue repair expense, so 40A(3) applies.)

**WN-5 — Item 5 (farmer, Rule 6DD(e)).** Payment to a cultivator/grower for agricultural produce is exempt under Rule 6DD → **nil disallowance**.

| Item | Amount (₹) | Disallowed (₹) | Reason |
|---|---|---|---|
| 1 | 43,000 | 43,000 | Aggregate > ₹10,000, same person same day |
| 2 | 45,000 | Nil | Rule 6DD(j) bank holiday |
| 3 | 1,20,000 | 1,20,000 | Cash > ₹35,000 transporter limit |
| 4 | 38,000 | 38,000 | Bearer cheque ≠ account payee |
| 5 | 50,000 | Nil | Rule 6DD(e) agricultural produce |
| **Total disallowed** | | **2,01,000** | |

**Answer:** Total disallowed u/s 40A(3) = **₹2,01,000**.

**Why this way (the reasoning):** Sec 40A(3) exists to push the economy toward a banking trail so cash cannot be used to inflate expenses or fund the unaccounted. The design principles the question tests: (1) the ceiling is **per person per day in aggregate**, defeating the old trick of splitting one purchase into several sub-₹10,000 bills — so you sum same-day, same-payee payments. (2) The mode must be *account-payee* cheque/draft/ECS; a **bearer cheque encashes like cash**, so it fails, teaching students that it is the traceability, not the instrument's name, that matters. (3) The **₹35,000 transporter limit** is a policy carve-out recognising that goods-carriage operators historically dealt in cash. (4) **Rule 6DD** lists situations where insisting on banking is impractical or unfair — a bank holiday, or a farmer with no bank access — so the disallowance yields to commercial reality. Note the entire payment is disallowed, not merely the excess over ₹10,000 — the section is deliberately harsh to deter the practice.

*(Full-marks tip: cite the ₹35,000 transporter threshold and the specific Rule 6DD clause for each exemption; the common error is disallowing only the excess over the limit or missing the same-day aggregation.)*

---

### Q23. Ch: Profits & Gains of Business or Profession — Depreciation block concept, put-to-use < 180 days & additional depreciation (Marks: 10) [Problem]
**Question:** Surya Manufacturing Ltd (engaged in manufacture) furnishes the following for FY 2024-25. Compute depreciation and the WDV carried forward. Company is in the old regime (additional depreciation available).

| Block | Rate | Opening WDV (01-Apr-2024) (₹) |
|---|---|---|
| Plant & Machinery | 15% | 40,00,000 |
| Furniture | 10% | 8,00,000 |

Transactions during the year:
- New plant purchased and put to use on 12-Aug-2024 (used > 180 days): ₹20,00,000.
- Second-hand plant purchased and put to use on 05-Dec-2024 (used < 180 days): ₹10,00,000.
- New plant (eligible) installed 20-Jan-2025 (used < 180 days): ₹15,00,000.
- Plant sold on 15-Sep-2024: ₹6,00,000.
- Furniture: nil additions; nil sales.

**Solution:**

**WN-1 — Segregate P&M by usage period.** Full-rate assets (used ≥ 180 days): opening WDV 40,00,000 + new plant (12-Aug) 20,00,000 − sale 6,00,000 = **54,00,000**. Half-rate assets (used < 180 days): 2nd-hand plant 10,00,000 + new plant (20-Jan) 15,00,000 = **25,00,000**.

**WN-2 — Normal depreciation @ 15%.** On ≥180-day portion: 15% × 54,00,000 = 8,10,000. On <180-day portion: 7.5% × 25,00,000 = 1,87,500. Normal dep = **₹9,97,500**.

**WN-3 — Additional depreciation @ 20% (Sec 32(1)(iia)).** Available only on **new** plant acquired & installed by a manufacturer; not on **second-hand** plant. Eligible new plant:
- New plant 12-Aug (>180 days): 20% × 20,00,000 = 4,00,000 (full).
- New plant 20-Jan (<180 days): 20% × 15,00,000 = 3,00,000, but restricted to **half** (10%) = 1,50,000; balance 1,50,000 carried to next year u/s 32(1)(iia) proviso.
- Second-hand plant 10,00,000 → **no additional depreciation**.
Additional dep this year = 4,00,000 + 1,50,000 = **₹5,50,000**.

**WN-4 — Furniture block.** 10% × 8,00,000 = **₹80,000**.

| Statement of Depreciation (FY 2024-25) | ₹ |
|---|---|
| P&M — Normal (WN-2) | 9,97,500 |
| P&M — Additional (WN-3) | 5,50,000 |
| Furniture (WN-4) | 80,000 |
| **Total depreciation** | **16,27,500** |

**WN-5 — Closing WDV, P&M block.** Opening + additions − sale − depreciation = (40,00,000 + 20,00,000 + 10,00,000 + 15,00,000) − 6,00,000 − (9,97,500 + 5,50,000) = 85,00,000 − 6,00,000 − 15,47,500 = **₹63,52,500**. Furniture closing WDV = 8,00,000 − 80,000 = **₹7,20,000**.

**Answer:** Total depreciation for FY 2024-25 = **₹16,27,500**; closing WDV — P&M **₹63,52,500**, Furniture **₹7,20,000**; additional depreciation of **₹1,50,000** carried forward to FY 2025-26.

**Why this way (the reasoning):** Depreciation under the Act is a **block-of-assets** concept, not asset-wise: you pool assets of the same class and rate, add purchases, subtract sale proceeds (not book profit/loss), and depreciate the surviving lump — so an individual asset's gain/loss vanishes unless the whole block is emptied. The 180-day rule reflects a matching principle: an asset used only part of the year should earn only half a year's allowance, hence 50% depreciation when put to use **on or after** the 181st-day cut-off. Additional depreciation (20%) is an investment incentive strictly for *manufacturers* buying *new* plant — so second-hand plant is excluded (it was already incentivised once), and if the new asset is used < 180 days you get only half now with the deliberate **carry-forward of the other half** to the next year, a rule unique to additional depreciation that students routinely forget. Deducting sale *proceeds* (not WDV) from the block is the subtle trap — the block absorbs the realisation, and no separate capital gain arises unless proceeds exceed the block or the block ceases.

*(Full-marks tip: the carry-forward of the unclaimed 10% additional depreciation and the exclusion of second-hand plant are the two most-rewarded points; deducting book WDV instead of sale proceeds from the block is the classic error.)*

---

### Q24. Ch: Profits & Gains of Business or Profession — Presumptive taxation: 44AD vs normal, and the 8%/6% split with the "five-year lock-in" (Marks: 8) [Case/Application]
**Question:** Mr. Rehan runs a retail trading business. For FY 2024-25 his turnover is ₹1.80 crore, of which ₹1.20 crore was received through banking channels/UPI and ₹60 lakh in cash. His actual net profit as per books is ₹6,50,000. He declared income u/s 44AD in FY 2021-22, FY 2022-23 and FY 2023-24. In FY 2024-25 he wishes to declare **actual profit of ₹6,50,000** (which is lower than presumptive) and not get his accounts audited. Advise him on: (a) eligibility for 44AD given the turnover, (b) the minimum presumptive income if 44AD is applied, and (c) the consequence of declaring lower actual profit.

**Answer:**

**Principle — Sec 44AD eligibility.** Available to a resident individual/HUF/firm (not LLP) carrying on eligible business, with turnover up to ₹2 crore — **enhanced to ₹3 crore** where cash receipts do not exceed **5%** of turnover. Presumptive income = **8%** of turnover, reduced to **6%** for the portion received through banking/prescribed electronic modes.

**(a) Eligibility.** Turnover ₹1.80 crore is within the basic ₹2 crore limit, so Rehan is eligible for 44AD irrespective of the cash proportion (the ₹3 crore/5% test only matters above ₹2 crore). Cash of ₹60 lakh is 33% of turnover — this would bar the ₹3 crore limit but is irrelevant here as turnover is below ₹2 crore.

**WN-1 — Minimum presumptive income (b).**
- Digital receipts ₹1.20 crore @ 6% = ₹7,20,000.
- Cash receipts ₹60 lakh @ 8% = ₹4,80,000.
- Minimum presumptive income = **₹12,00,000**.

**(c) Consequence of declaring ₹6,50,000.** Under Sec 44AD(4)/(5), if an assessee who *has* opted for 44AD declares income **lower than 8%/6%** (i.e., ₹6,50,000 < ₹12,00,000) and his total income exceeds the basic exemption limit, he must **maintain books u/s 44AA and get them audited u/s 44AB**. Moreover, having opted out of 44AD, Sec 44AD(4) triggers a **five-year lock-out**: he cannot claim 44AD for the *next five* assessment years, and in each of those years, if income exceeds the exemption limit, audit is compulsory.

**Conclusion / Advice.** Rehan cannot declare ₹6,50,000 without audit. His choice is binary: (i) declare presumptive **₹12,00,000** (no books, no audit, but pay tax on the higher figure); or (ii) declare actual **₹6,50,000**, but then **maintain books and undergo tax audit**, and additionally forfeit 44AD for AY 2026-27 to AY 2030-31. Given the ₹5.5 lakh income gap versus the cost/consequence of audit and five-year lock-out, if his books genuinely show ₹6,50,000 and he expects continued low margins, option (ii) with audit may still save tax overall; but if this is a one-off dip, staying in 44AD preserves flexibility.

**Why this way (the reasoning):** 44AD is a *bargain*: the taxpayer trades away deductions and record-keeping for a deemed profit, and the State trades away scrutiny for certainty of collection. The 6%/8% split rewards digital receipts, nudging the cash economy toward banking — so you must bifurcate turnover by mode, never apply a flat 8%. The genuinely hard idea is Sec 44AD(4)'s **anti-abuse lock-in**: without it, a taxpayer would hop into 44AD in high-profit years (to cap tax at 8%) and hop out in low-profit years (to claim actual lower profit) — cherry-picking both ways. The five-year exclusion + mandatory audit removes that arbitrage, forcing a genuine multi-year commitment. Students err by (i) applying flat 8% on the whole turnover, and (ii) thinking one can freely declare lower actual profit — the audit + lock-out consequence is the whole examinable point.

*(Full-marks tip: bifurcate 6%/8%, and articulate the 44AD(4) five-year consequence with the audit trigger; the biggest deduction is missing the lock-out or applying the ₹3 crore limit when cash exceeds 5%.)*

---

### Q25. Ch: Income from House Property — Composite letting, house property vs business income, and part let/part self-occupied (Marks: 6) [Case/Application]
**Question:** Mr. Sanjay owns a building. The ground floor is let out to a bank at ₹80,000 p.m. under a bare lease. The first floor is let out **furnished** at ₹90,000 p.m. of which ₹30,000 p.m. is attributable to furniture, air-conditioning and other amenities under a **composite, inseparable** agreement. The second floor he uses for his own residence. He also lets a separate warehouse where he provides staff, security, loading and complex services as an organised activity. Examine under which head each stream is taxable and why.

**Answer:**

**Governing principle.** Income from letting a building is taxable under **House Property** (Sec 22) only where the assessee is *owner* and the letting is of the property *as such*. Where letting of building is **inseparable** from letting of plant/machinery/furniture, Sec 56(2)(ii)/(iii) taxes the **composite rent under "Income from Other Sources"** (or business, if it is the assessee's business); where services rendered convert the arrangement into a commercial exploitation, income is **business income**.

**Application.**
- **Ground floor (bare lease to bank):** pure letting of building by owner → **House Property**. GAV based on rent/ER; standard 30% and interest deductions apply.
- **First floor (composite, inseparable):** rent for building + amenities cannot be separated → the *entire* ₹90,000 p.m. is taxed under **Other Sources** u/s 56(2)(iii) (not split), because the letting of building and furniture is intended as a single package and is inseparable. Actual expenses/depreciation on furniture are deductible against it.
- **Second floor (self-occupied):** NAV **Nil**; taxed under House Property with only interest deduction (regime-dependent).
- **Warehouse with complex services:** organised activity of providing space + substantial services (staff, security, handling) is **exploitation of property as a commercial asset** → **Business income (PGBP)**, following the "primary intention" test (e.g., *Sultan Bros*, *Shambhu Investment* line of reasoning).

**Conclusion.** Four different treatments: GF → House Property; FF → Other Sources (composite, whole amount); SF → House Property (SOP, Nil NAV); Warehouse → PGBP. Sanjay must not club them under one head.

**Why this way (the reasoning):** The head of income is decided by the *nature and dominant intention* of the arrangement, not by the label "rent". Sec 22 taxes the **owner's capacity to earn from the property as property** — a passive yield — which is why bare letting sits in House Property and enjoys the 30% standard deduction as a proxy for upkeep. The moment the arrangement bundles **inseparable amenities**, the income is no longer purely from the building, so the Act shifts it to Other Sources (or business) where *actual* costs and depreciation are matched — the 30% flat deduction would be inappropriate for furniture-heavy lettings. When the owner goes further and runs an *organised service operation*, the property becomes a tool of trade and the yield is business profit. The examinable subtlety: a **composite inseparable** rent is taxed **wholly** under one head (not artificially split), whereas if the two lettings were *separable* the building rent would go to House Property and amenity rent to Other Sources.

*(Full-marks tip: the "inseparable → single head, whole amount" rule and the primary-intention test for the warehouse earn the marks; wrongly splitting the composite rent or forcing everything into House Property is the common failure.)*

---

### Q26. Ch: Profits & Gains of Business or Profession — Section 32AD / 43CA-type twist: taxability of subsidy, capital receipts and Sec 41(1) (Marks: 8) [Problem]
**Question:** Compute the PGBP adjustments for M/s Meridian Industries (FY 2024-25) from the following items credited/debited in accounts, stating the treatment and section:

| # | Item | Amount (₹) |
|---|---|---|
| 1 | Sales-tax refund of an earlier year (allowed as deduction earlier) now received | 1,50,000 |
| 2 | Waiver by a supplier of a trading liability outstanding 4 years (allowed earlier) | 2,00,000 |
| 3 | Government subsidy for setting up a plant in a notified backward area (capital subsidy, credited to P&L) | 5,00,000 |
| 4 | Profit on sale of a plot held as investment (credited to P&L) | 8,00,000 |
| 5 | Recovery of a bad debt earlier written off and allowed | 90,000 |
| 6 | Cash discount received from creditors | 40,000 |
| 7 | Interest received on income-tax refund | 25,000 |

Net profit as per P&L (after crediting all above) = ₹40,00,000.

**Solution:**

**WN-1 — Sec 41(1) items (remission/cessation of trading liability & recovery).** Items 1, 2 and 5 are **deemed business income** u/s 41(1): a benefit obtained in respect of a loss/expenditure/trading liability *earlier allowed*. Already credited to P&L → no adjustment needed (retain in PGBP): 1,50,000 + 2,00,000 + 90,000.

**WN-2 — Item 3, capital subsidy.** A subsidy given to help set up a plant is a **capital receipt** → not taxable as revenue. Since credited to P&L, **deduct ₹5,00,000** from net profit. (It reduces cost/WDV only if given specifically to meet asset cost; here for "setting up in backward area", treated capital, not business income.)

**WN-3 — Item 4, sale of investment plot.** Profit on an asset held as **investment** is **Capital Gains**, not PGBP → **deduct ₹8,00,000** from net profit (to be taxed separately under Capital Gains head).

**WN-4 — Item 6, cash discount.** Revenue receipt arising from trade → correctly in PGBP; no adjustment.

**WN-5 — Item 7, interest on IT refund.** Taxable under **Other Sources**, not PGBP → **deduct ₹25,000** from net profit.

| Statement — Computation of PGBP (FY 2024-25) | ₹ |
|---|---|
| Net profit as per P&L | 40,00,000 |
| Less: Capital subsidy (capital receipt) | (5,00,000) |
| Less: Profit on sale of investment plot (→ Capital Gains) | (8,00,000) |
| Less: Interest on IT refund (→ Other Sources) | (25,000) |
| Items already correct (41(1) recoveries, cash discount) | Nil adj. |
| **Profits & Gains of Business or Profession** | **26,75,000** |

**Answer:** PGBP income = **₹26,75,000**; ₹8,00,000 goes to Capital Gains and ₹25,000 to Other Sources; ₹5,00,000 subsidy is a non-taxable capital receipt.

**Why this way (the reasoning):** Two distinct principles run through this problem. First, **Sec 41(1) — the "recoupment" rule**: if the revenue earlier let you deduct a loss/liability, and later you recover it or the liability ceases, taxing it back restores symmetry — you cannot keep a deduction for a cost you never ultimately bore. That is why refund of a *previously allowed* sales tax, a *waived* trading liability, and a *recovered* bad debt are all pulled into business income. Second, the **head-of-income and capital/revenue tests**: net profit in accounts mixes items that tax law routes elsewhere, so a correct PGBP figure requires *stripping out* receipts that are capital (subsidy for setting up plant), or belong to another head (investment gain → Capital Gains; refund interest → Other Sources). The trap is treating everything credited to P&L as business income. A capital subsidy for establishing an undertaking is a one-time contribution to the *cost of setup*, not a trading receipt, so it escapes revenue tax — its character is fixed by the *purpose* of the grant, per the purpose test in *Sahney Steel/Ponni Sugars*.

*(Full-marks tip: state Sec 41(1) for each recoupment and justify each deduction by head/character; deducting the 41(1) recoveries by mistake, or taxing the capital subsidy, are the frequent errors.)*

---

### Q27. Ch: Income from House Property — Deemed ownership, co-ownership and interest apportionment (Marks: 6) [Problem]
**Question:** Mr. and Mrs. Bose are **co-owners** (50:50, definite shares) of a house, funded by a joint loan of ₹40,00,000 at 9% p.a. The house is let out at ₹50,000 p.m. Municipal taxes ₹36,000 (paid equally). Additionally, Mr. Bose had **transferred** another house to his minor son without adequate consideration; that house is let at ₹20,000 p.m., municipal taxes ₹12,000, and it carries no loan. Compute the House Property income assessable in the hands of Mr. Bose for AY 2025-26 (old regime).

**Solution:**

**WN-1 — Co-owned let-out house.** GAV = 50,000 × 12 = 6,00,000. Less municipal taxes 36,000 → NAV 5,64,000. Less 30% = 1,69,200 → 3,94,800. Less interest 9% × 40,00,000 = 3,60,000 → income before apportionment = 3,94,800 − 3,60,000 = **₹34,800**. Each co-owner (50%) = **₹17,400**.

**WN-2 — Deemed owner: transfer to minor son.** Sec 27(i): an individual who transfers a house to a **minor child** (not being a married daughter) without adequate consideration is treated as the **deemed owner** → the property income is computed in **Mr. Bose's** hands directly (not via Sec 64 clubbing). GAV = 20,000 × 12 = 2,40,000. Less taxes 12,000 → 2,28,000. Less 30% = 68,400 → **₹1,59,600**.

| Statement — Mr. Bose's House Property Income (AY 2025-26) | ₹ |
|---|---|
| Share in co-owned let-out house (WN-1) | 17,400 |
| Deemed-owned house (transfer to minor son) (WN-2) | 1,59,600 |
| **Income from House Property** | **1,77,000** |

**Answer:** House Property income assessable for Mr. Bose = **₹1,77,000** (Mrs. Bose separately assessable on ₹17,400).

**Why this way (the reasoning):** Two ownership doctrines drive this. **Co-ownership with definite shares** (Sec 26): the property is *not* assessed as an association; instead each co-owner's *share* of the computed income is taxed in his own hands — so you compute the property income once, then apportion, giving each owner the benefit of his own slab and (for self-occupied) his own interest cap. **Deemed ownership** (Sec 27): tax law looks through hollow transfers. When a parent gifts a house to a minor child, legal title moves but the Act treats the *transferor* as owner so the income is computed under House Property in his hands — importantly via Sec 27, *not* the Sec 64 clubbing route, which matters because it means the income keeps its House Property character and gets the 30% standard deduction, and no separate ₹1,500 exemption of Sec 10(32) applies (that exemption is only for Sec 64 clubbing, not Sec 27 deemed ownership). Students who route the minor's house income through clubbing (and wrongly claim the ₹1,500 relief) misapply the scheme; the transfer-to-minor case is squarely a *deemed ownership* case.

*(Full-marks tip: apply Sec 26 apportionment after full computation, and Sec 27 deemed ownership for the minor transfer without the Sec 10(32) relief; the common error is clubbing the minor's income and giving the ₹1,500 exemption.)*

---

### Q28. Ch: Profits & Gains of Business or Profession — Presumptive 44ADA (profession) vs 44AB audit threshold interplay (Marks: 6) [Case/Application]
**Question:** Dr. Nalini, a resident physician (a specified profession), has gross professional receipts of ₹68,00,000 in FY 2024-25, of which cash receipts are ₹2,00,000. Her actual net profit per books is ₹28,00,000. She wants to declare income under Sec 44ADA. Advise: (a) whether she is eligible given the receipts; (b) the presumptive income; (c) whether declaring her actual ₹28,00,000 (below presumptive) requires audit; (d) how the answer changes if her cash receipts were ₹5,00,000.

**Answer:**

**Principle — Sec 44ADA.** A resident individual/firm (not LLP) in a specified profession may declare **50%** of gross receipts as income, if gross receipts do not exceed **₹50 lakh**, enhanced to **₹75 lakh** where cash receipts do not exceed **5%** of gross receipts.

**(a) Eligibility.** Gross receipts ₹68,00,000 exceed the basic ₹50 lakh limit, so eligibility hinges on the enhanced ₹75 lakh limit, which requires cash ≤ 5% of receipts. 5% of ₹68,00,000 = ₹3,40,000. Cash of ₹2,00,000 < ₹3,40,000 → **condition satisfied**; she is eligible (₹68 lakh < ₹75 lakh).

**(b) Presumptive income.** 50% × 68,00,000 = **₹34,00,000**.

**(c) Declaring actual ₹28,00,000.** ₹28,00,000 < 50% presumptive (₹34,00,000). Under Sec 44ADA(4), declaring **less than 50%** while total income exceeds the exemption limit obliges her to **maintain books u/s 44AA and get a tax audit u/s 44AB**. So yes, audit is required if she declares ₹28,00,000. (Unlike 44AD, there is **no five-year lock-out** for 44ADA.)

**(d) If cash were ₹5,00,000.** Then cash (₹5,00,000) exceeds 5% of ₹68,00,000 (₹3,40,000) → the ₹75 lakh limit is **unavailable**, and receipts ₹68,00,000 exceed the basic ₹50 lakh → **44ADA is not available at all**. She must maintain books; audit u/s 44AB is required as receipts exceed ₹50 lakh for a profession. She would then compute actual profits normally.

**Why this way (the reasoning):** 44ADA mirrors 44AD's bargain for professionals but at a steeper 50% deemed margin, reflecting that professions are typically low-cost, high-margin. The **5% cash test** for the enhanced ₹75 lakh limit is the same digital-economy nudge — but note it works differently from a simple limit: cross the 5% cash line and you don't merely lose the higher limit, you fall back to ₹50 lakh, which here *disqualifies* her entirely because receipts already exceed ₹50 lakh. That cliff-edge is the hard, examinable twist in part (d). The other subtlety students conflate: 44ADA has **no five-year lock-out** — that anti-arbitrage device is unique to 44AD(4). So a professional can move in and out of presumptive year to year (subject to audit when declaring lower), whereas a business under 44AD cannot. Recognising that the *same* 5% wording produces *different* consequences in the two sub-parts is what a rank-holder demonstrates.

*(Full-marks tip: the cliff-edge in (d) — cash > 5% drops the limit to ₹50 lakh and disqualifies her — and the absence of a lock-out under 44ADA are the scoring points; wrongly importing the 44AD five-year rule loses marks.)*

---

### Q29. Ch: Income from House Property — Interest set-off cap, carry-forward and the ₹2 lakh house-property loss limit (Marks: 8) [Problem]
**Question:** Mr. Iqbal (old regime) has: (i) one self-occupied house with housing-loan interest of ₹2,80,000 (construction completed within 5 years); (ii) a let-out house with computed loss of ₹3,20,000 after interest of ₹6,00,000. His income under other heads: Salary ₹18,00,000, Business income ₹2,50,000. Compute his gross total income, the house-property loss set off, and the amount carried forward for AY 2025-26.

**Solution:**

**WN-1 — Self-occupied house loss.** NAV Nil; interest allowable capped at **₹2,00,000** (loan for construction completed within 5 years). SOP loss = **(₹2,00,000)**. (Excess ₹80,000 interest is lost — not carried forward.)

**WN-2 — Let-out house.** Loss as computed = **(₹3,20,000)** (GAV − taxes − 30% − interest 6,00,000, given).

**WN-3 — Total House Property loss.** (2,00,000) + (3,20,000) = **(₹5,20,000)**.

**WN-4 — Inter-head set-off cap u/s 71(3A).** Loss from House Property set off against income under **other heads** is capped at **₹2,00,000** per year. So only ₹2,00,000 can be set off against Salary/Business this year.

**WN-5 — Carry forward.** Unabsorbed House Property loss = 5,20,000 − 2,00,000 = **₹3,20,000**, carried forward u/s 71B for up to **8 assessment years**, to be set off **only against House Property income** in future years.

| Statement — Gross Total Income (AY 2025-26) | ₹ |
|---|---|
| Salary | 18,00,000 |
| Business income | 2,50,000 |
| Income from House Property (net loss 5,20,000) | (5,20,000) |
| Less: HP loss set-off restricted to | 2,00,000 |
| **Gross Total Income** (20,50,000 − 2,00,000) | **18,50,000** |
| House Property loss carried forward u/s 71B | 3,20,000 |

**Answer:** GTI = **₹18,50,000**; House-property loss set off this year **₹2,00,000**; loss carried forward **₹3,20,000** (up to 8 years, only vs House Property income).

**Why this way (the reasoning):** Two ceilings operate and students confuse them. The **first cap is on interest** for a *self-occupied* house — ₹2,00,000 under Sec 24(b) — and any excess interest is simply **lost**, never carried forward, because there is no positive House Property income for it to attach to. The **second cap is the Sec 71(3A) inter-head restriction**: introduced to curb taxpayers who bought large let-out properties, generated big interest-driven losses, and wiped out salary tax. So even though the *total* House Property loss is ₹5,20,000, only ₹2,00,000 can shelter other-head income in the current year. The remaining ₹3,20,000 isn't forfeited — Sec 71B lets it be carried forward for 8 years, but the ring-fence is that it can only offset *future House Property income*, not salary again. Distinguishing "interest cap (permanent loss)" from "set-off cap (deferred, carried forward)" is the crux; treating the whole ₹5,20,000 as deductible this year, or carrying forward the lost ₹80,000 SOP interest, are the classic mistakes.

*(Full-marks tip: separate the ₹2 lakh interest cap (lost) from the ₹2 lakh inter-head set-off cap (carried forward under 71B for 8 years vs HP income only); merging the two caps is the common error.)*

---

### Q30. Ch: Profits & Gains of Business or Profession — Section 40(b) partner remuneration & interest, book-profit computation (Marks: 8) [Problem]
**Question:** M/s Kohli & Associates (a firm, old regime) has a partnership deed authorising remuneration and 12% interest on capital to working partners A and B. For FY 2024-25:

| Particulars | ₹ |
|---|---|
| Net profit as per P&L (after debiting the items below) | 9,00,000 |
| Remuneration paid to A and B (debited) | 7,00,000 |
| Interest on partners' capital @ 15% (debited) | 3,00,000 |
| Donation to a charitable trust (80G) debited | 50,000 |

Compute the maximum allowable remuneration u/s 40(b) and the firm's business income. (Interest capital base is ₹20,00,000.)

**Solution:**

**WN-1 — Interest on capital allowable.** Deed allows 12%; actual paid 15% on ₹20,00,000. Sec 40(b) caps allowable interest at **12%**: allowed = 12% × 20,00,000 = 2,40,000. Interest debited = 3,00,000. **Excess disallowed = ₹60,000.**

**WN-2 — Book profit.** Start with net profit 9,00,000. Add back remuneration 7,00,000 (to be re-tested), add back disallowed interest 60,000, add back donation 50,000 (not a business expense; separately eligible u/s 80G). Book profit before remuneration = 9,00,000 + 7,00,000 + 60,000 + 50,000 = **₹17,10,000**.

**WN-3 — Maximum remuneration u/s 40(b)(v).** New slabs (FY 2024-25 onward): on first ₹6,00,000 of book profit — **₹3,00,000 or 90%**, whichever higher; on the balance — **60%**.
- First 6,00,000: higher of 3,00,000 and 90% × 6,00,000 (5,40,000) = **5,40,000**.
- Balance 17,10,000 − 6,00,000 = 11,10,000 @ 60% = **6,66,000**.
- Maximum allowable remuneration = 5,40,000 + 6,66,000 = **₹12,06,000**.

**WN-4 — Remuneration allowed.** Lower of actual (7,00,000) and maximum (12,06,000) = **₹7,00,000** (fully allowed).

| Statement — Firm's Business Income (FY 2024-25) | ₹ |
|---|---|
| Net profit as per P&L | 9,00,000 |
| Add: Excess interest on capital (WN-1) | 60,000 |
| Add: Donation (not business exp.) | 50,000 |
| Add: Remuneration (to re-test) | 7,00,000 |
| Book profit | 17,10,000 |
| Less: Remuneration allowed (WN-4) | (7,00,000) |
| Less: Interest on capital allowed (WN-1) | (2,40,000) |
| **Business income** | **7,70,000** |

**Answer:** Maximum allowable remuneration = **₹12,06,000**; remuneration actually allowed = **₹7,00,000**; firm's business income = **₹7,70,000** (donation ₹50,000 separately deductible u/s 80G subject to limits).

**Why this way (the reasoning):** A firm is taxed as a separate entity, but remuneration/interest to partners are allowed as deductions *only within Sec 40(b) limits* — otherwise partners could strip firm profit into their own hands and dodge the firm-level tax. The **12% interest cap** and the **remuneration slabs** are the ceilings. The pivotal concept is **"book profit"**: remuneration is computed on a figure that is itself *before* remuneration, so you must add remuneration back before applying the slabs — a circularity students trip on. Equally important: items like **interest allowed** stay deducted in book profit, but the **excess interest** and **donation** are added back because they aren't allowable business expenses (donation is a Chapter VI-A deduction, not a Sec 37 expense). Note the FY 2024-25 amendment raised the first-slab threshold to ₹6 lakh and the ₹3 lakh floor — using old slabs is an immediate mark loss. Since actual remuneration (₹7,00,000) is below the statutory maximum (₹12,06,000), it is fully allowed; had it exceeded, only the maximum would be deductible and the excess added back.

*(Full-marks tip: add remuneration back to reach book profit before applying slabs, use the current ₹6 lakh/₹3 lakh slabs, and keep the donation out of business expense; using superseded slabs or forgetting to add remuneration back are the usual errors.)*

---

### Q31. Ch: Income from House Property — Property let then vacant (vacancy allowance) with unrealised rent (Marks: 6) [Problem]
**Question:** Mr. Farhan's house (MV ₹3,60,000; FR ₹4,20,000; SR ₹3,90,000) was let at ₹38,000 p.m. It remained let for 8 months; vacant for 3 months (could not find a tenant); and for 1 month the tenant occupied it but the rent of ₹38,000 was **unrealised** (all Rule 4 conditions met). Municipal taxes paid ₹27,000. Compute House Property income for AY 2025-26.

**Solution:**

**WN-1 — Actual rent received/receivable.** Rent for the period let and realised = 8 months × 38,000 = 3,04,000. The 1 unrealised month is excluded (Rule 4). Vacant 3 months earn nothing. Actual rent = **₹3,04,000**.

**WN-2 — Expected Rent (ER).** Higher of MV 3,60,000 and FR 4,20,000 = 4,20,000, capped by SR 3,90,000 → **ER = ₹3,90,000** (annual).

**WN-3 — GAV with vacancy (Sec 23(1)(c)).** Where the property is let and was **vacant** for part of the year, and owing to the vacancy the actual rent received is **less than ER**, the actual rent (as reduced by vacancy) is taken as GAV. Compare: rent that *would* have been received for the let period (excluding unrealised) is 3,04,000, which is less than ER 3,90,000 **because of the vacancy** → GAV = **₹3,04,000** (Sec 23(1)(c) applies).

**WN-4 — NAV and deductions.** GAV 3,04,000 − municipal taxes 27,000 = NAV 2,77,000. Less 30% = 83,100 → **₹1,93,900**.

| Statement of House Property Income (AY 2025-26) | ₹ |
|---|---|
| Gross Annual Value (Sec 23(1)(c)) | 3,04,000 |
| Less: Municipal taxes | (27,000) |
| Net Annual Value | 2,77,000 |
| Less: Std deduction 30% u/s 24(a) | (83,100) |
| **Income from House Property** | **1,93,900** |

**Answer:** Income from House Property = **₹1,93,900**.

**Why this way (the reasoning):** Sec 23(1)(c) is a relief mechanism: normally GAV is the *higher* of expected rent and actual rent, which would tax an owner on notional rent even for months he could not let the property. That is unfair when a genuine vacancy — not the owner's choice — depresses the actual rent below the expected rent. So the law says: if the shortfall *is caused by the vacancy*, take the (lower) actual rent as GAV, effectively giving a **vacancy allowance**. The sequence matters: you first strip out **unrealised rent** (Rule 4) because rent legally uncollectible was never "received or receivable", then test whether the *remaining* actual rent falls below ER due to vacancy. Here both forces push GAV down to ₹3,04,000. The trap is either (i) taking ER (₹3,90,000) as GAV and ignoring the vacancy relief, or (ii) including the unrealised month's rent. Getting the interaction of Rule 4 (unrealised) and Sec 23(1)(c) (vacancy) right — two different reductions applied in the correct order — is the hard core.

*(Full-marks tip: show that the shortfall below ER is attributable to vacancy (the trigger for 23(1)(c)) and exclude the unrealised month first; taking ER as GAV or double-counting the vacant/unrealised months are the usual slips.)*

---

### Q32. Ch: Profits & Gains of Business or Profession — Section 35/35D/37 disallowances integrated computation (Marks: 10) [Problem]
**Question:** From the P&L of Vega Pharma Ltd (FY 2024-25), compute business income. Net profit as per P&L = ₹52,00,000, arrived at after the following debits/credits:

| # | Item | ₹ |
|---|---|---|
| 1 | Scientific research — revenue expenditure (in-house, approved) | 6,00,000 |
| 2 | Scientific research — capital expenditure (land ₹10,00,000 + building ₹8,00,000) | 18,00,000 |
| 3 | Preliminary expenses (feasibility/market survey) incurred on extending business | 5,00,000 |
| 4 | Advertisement in a political party's souvenir | 1,00,000 |
| 5 | Penalty for infringement of law (pollution control breach) | 2,00,000 |
| 6 | Interest on late payment of GST | 40,000 |
| 7 | Provision for gratuity (not to an approved fund) | 3,00,000 |
| 8 | Contribution to a University for approved research (weighted) | 4,00,000 |

**Solution:**

**WN-1 — Item 1, in-house revenue research (Sec 35(1)(i)).** 100% allowed; already debited → no adjustment.

**WN-2 — Item 2, capital research (Sec 35(1)(iv)).** Capital expenditure on scientific research is fully deductible **except land**. Land ₹10,00,000 not allowed; building ₹8,00,000 allowed 100%. In accounts ₹18,00,000 debited (assume as expense) → **add back ₹10,00,000** (land portion disallowed). Building already effectively allowed.

**WN-3 — Item 3, preliminary/expansion expenses (Sec 35D).** Amortised over **5 years**: allowed = 5,00,000 ÷ 5 = 1,00,000. Debited 5,00,000 → **add back ₹4,00,000** (disallowed this year, allowed over next years).

**WN-4 — Item 4, political souvenir advertisement (Sec 37(2B)).** Advertisement in a political party's publication is **expressly disallowed** as business expense → **add back ₹1,00,000**. (Separately deductible u/s 80GGB for a company, subject to conditions.)

**WN-5 — Item 5, penalty for law infringement.** Penalty for breach of law is **not** allowable (Explanation to Sec 37(1)) → **add back ₹2,00,000**.

**WN-6 — Item 6, interest on late GST.** **Compensatory** (not penal) → allowable business expense; no adjustment.

**WN-7 — Item 7, provision for gratuity (unapproved).** Sec 40A(7): provision for gratuity, other than to an **approved** fund or for actual payment, is disallowed → **add back ₹3,00,000**.

**WN-8 — Item 8, contribution to University for research (Sec 35(1)(ii)).** Sum paid to an approved research association/university — deduction **100%** (weighted 150% withdrawn from AY 2021-22). Debited 4,00,000; allowed 4,00,000 → no adjustment.

| Statement — Computation of Business Income (FY 2024-25) | ₹ |
|---|---|
| Net profit as per P&L | 52,00,000 |
| Add: Research capital — land disallowed (WN-2) | 10,00,000 |
| Add: Preliminary exp. disallowed (4/5) (WN-3) | 4,00,000 |
| Add: Political souvenir advertisement (WN-4) | 1,00,000 |
| Add: Penalty for law infringement (WN-5) | 2,00,000 |
| Add: Provision for unapproved gratuity (WN-7) | 3,00,000 |
| **Business income** | **72,00,000** |

**Answer:** Business income = **₹72,00,000** (with ₹4,00,000 preliminary expense allowable over the next four years, and the political advertisement separately claimable u/s 80GGB).

**Why this way (the reasoning):** This tests the boundary of an *allowable business deduction*. Several coherent principles: (1) **Scientific research (Sec 35)** is generously incentivised — even *capital* research expenditure is written off fully in year one, but **land is always excluded** because land does not depreciate/deplete and could be a store of value, so allowing it would invite abuse. (2) **Sec 35D** spreads genuine setup/expansion costs over five years to match their enduring benefit, so only one-fifth bites now. (3) **Sec 37(1) Explanation** codifies public policy: money spent on *illegal* acts or *penalties* for breaking the law cannot be subsidised by a tax deduction — the State will not share the cost of law-breaking. (4) The **compensatory-versus-penal** distinction saves the GST interest: it merely compensates the exchequer for delayed money, so it's a normal business cost, whereas the pollution penalty punishes wrongdoing. (5) **Sec 40A(7)** blocks provisions for gratuity to unapproved funds to prevent tax deferral on unfunded promises. The examinable art is classifying each debit against the *right* gate and remembering the political-advertisement disallowance is redirected to 80GGB.

*(Full-marks tip: exclude land from Sec 35 capital research, amortise 35D over 5 years, and separate compensatory GST interest from penal payments; treating the whole research capital as allowed, or disallowing the GST interest, costs marks.)*

---

### Q33. Ch: Profits & Gains of Business or Profession — Presumptive 44AE goods-carriage with heavy/other vehicles mix (Marks: 6) [Problem]
**Question:** Mr. Vikram is in the business of plying goods carriages and owns the following vehicles during FY 2024-25. Compute his presumptive income u/s 44AE, and advise whether he can declare lower income based on his actual profit of ₹6,00,000.

| Vehicle | Gross Vehicle Weight | Owned for | 
|---|---|---|
| Truck 1 (heavy goods vehicle) | 16,000 kg | Whole year (12 months) |
| Truck 2 (heavy goods vehicle) | 14,000 kg | Acquired 10-Aug-2024 (part month → count as full months from Aug) |
| Truck 3 (other than heavy) | 9,000 kg | Whole year |
| Truck 4 (other than heavy) | 7,500 kg | Owned 5 months, sold in Sep 2024 |

**Solution:**

**WN-1 — Rates u/s 44AE.** For a **heavy goods vehicle** (GVW > 12,000 kg / 12 MT): **₹1,000 per ton of GVW per month** (or part). For **other** goods carriages: **₹7,500 per vehicle per month** (or part). Part of a month counts as a full month.

**WN-2 — Months of ownership.** Truck 1: 12; Truck 2: Aug to Mar = 8 months; Truck 3: 12; Truck 4: 5 months.

**WN-3 — Heavy vehicles (₹1,000 × ton × month).**
- Truck 1: 16 tons × 1,000 × 12 = ₹1,92,000.
- Truck 2: 14 tons × 1,000 × 8 = ₹1,12,000.

**WN-4 — Other vehicles (₹7,500 × month).**
- Truck 3: 7,500 × 12 = ₹90,000.
- Truck 4: 7,500 × 5 = ₹37,500.

| Statement — Presumptive Income u/s 44AE (FY 2024-25) | Months | ₹ |
|---|---|---|
| Truck 1 (16 T heavy) | 12 | 1,92,000 |
| Truck 2 (14 T heavy) | 8 | 1,12,000 |
| Truck 3 (other) | 12 | 90,000 |
| Truck 4 (other) | 5 | 37,500 |
| **Presumptive income** | | **4,31,500** |

**Advice on lower income:** Under Sec 44AE, an assessee **may** declare income **higher** than presumptive, but if he wishes to declare **lower** than the presumptive figure, he must **maintain books u/s 44AA and get them audited u/s 44AB** (and prove the lower profit). His actual profit ₹6,00,000 is in fact **higher** than presumptive ₹4,31,500 — so declaring ₹6,00,000 (actual) would mean paying tax on more than required. He should declare the **presumptive ₹4,31,500** without books/audit, since 44AE lets him report the lower presumptive figure with no audit.

**Answer:** Presumptive income u/s 44AE = **₹4,31,500**; he should opt for presumptive taxation and declare ₹4,31,500 (lower than actual ₹6,00,000) with no books/audit required.

**Why this way (the reasoning):** 44AE deems income *per vehicle*, and its 2018 redesign made the **heavy-vehicle rate weight-sensitive** (₹1,000 per ton) while keeping the flat ₹7,500 for lighter carriages — recognising that a 25-ton trailer earns far more than a 9-ton truck, so a flat per-vehicle figure would under-tax the big haulers. Hence you must first *classify* each vehicle as heavy (>12 MT) or not, then apply the correct formula. "Part of a month = full month" is a deliberate simplification favouring the exchequer. The advisory subtlety flips the usual presumptive logic: normally students worry about declaring *below* presumptive (which triggers audit), but here actual profit (₹6,00,000) *exceeds* presumptive (₹4,31,500), so the taxpayer's *advantage* is to report the lower presumptive figure — 44AE permits reporting the deemed income even if actual is higher, and that is the tax-planning point. Only the reverse (declaring below presumptive) forces audit.

*(Full-marks tip: apply the ₹1,000-per-ton rate only to >12 MT vehicles, count part-months as full, and note that declaring the lower presumptive figure is permissible while declaring below it triggers audit; using flat ₹7,500 for the heavy trucks is the classic error.)*

---

### Q34. Ch: Profits & Gains of Business or Profession — Section 43CA / ICDS-flavoured twist: closing stock valuation & Sec 145A, plus Sec 145 method (Marks: 8) [Case/Application]
**Question:** M/s Aster Textiles values its closing stock at ₹40,00,000 (cost) in its books, following exclusive method for taxes. Examine and quantify the adjustments for FY 2024-25 given: (a) unpaid GST of ₹2,50,000 included in the value of inputs is *not* added to closing stock or purchases (exclusive method); (b) the firm switched its stock-valuation method this year from FIFO to weighted average without a bona-fide reason, reducing closing stock by ₹1,20,000; (c) it wrote down obsolete stock to net realisable value ₹3,00,000 (cost ₹5,00,000). State the correct treatment under Sec 145/145A and ICDS.

**Answer:**

**Principle — Sec 145A (inclusive method) and Sec 145 (consistency).** Sec 145A mandates that valuation of purchases, sales and inventory shall include **the amount of any tax, duty, cess or fee actually paid or incurred** (inclusive method) — regardless of the accounting method. Sec 145 requires income to be computed by a method **regularly/consistently** followed; ICDS-II (Valuation of Inventories) permits *cost or NRV, whichever is lower*, and does **not** allow a change of method without reasonable cause.

**Application.**
- **(a) Unpaid GST — Sec 145A.** Even though unpaid, GST *incurred* on inputs must be included in inventory valuation under the inclusive method. Closing stock must be increased by **₹2,50,000**. (Correspondingly, purchases also rise, and if the GST is disallowed u/s 43B for non-payment there is a separate add-back — but the *valuation* symmetry under 145A first requires grossing up stock by ₹2,50,000.) Net effect on profit via 145A grossing is generally neutral where purchases and stock both adjust, but the closing-stock understatement of ₹2,50,000 must be corrected.
- **(b) Change of method without bona-fide reason — Sec 145.** A change in valuation method is permitted **only if bona fide and consistently followed thereafter**. Here the change lacks a genuine reason and *artificially* lowers closing stock by ₹1,20,000 (understating profit). The AO can reject it under Sec 145(3); **add back ₹1,20,000** to restore profit.
- **(c) Write-down to NRV — permitted.** Valuing obsolete stock at NRV ₹3,00,000 (below cost ₹5,00,000) is the *lower of cost or NRV* rule under ICDS-II/AS-2 — a **bona fide** and mandated valuation, not a change of method. The ₹2,00,000 write-down is **allowed**; no adjustment.

**Conclusion / quantification.** Adjustments to book stock ₹40,00,000: add ₹2,50,000 (unpaid GST, Sec 145A) and add ₹1,20,000 (reverse the mala-fide method change, Sec 145); the NRV write-down stands. Corrected closing stock ≈ **₹43,70,000**, increasing taxable profit by **₹3,70,000** (subject to the corresponding purchase-side/43B treatment of the GST).

**Why this way (the reasoning):** Closing stock is not a "free" figure — undervaluing it defers profit, so tax law polices it on two axes. **Sec 145A's inclusive method** insists taxes be embedded in valuation because otherwise a taxpayer could keep large tax-inclusive input costs in P&L while carrying tax-exclusive (lower) stock, artificially depressing profit — the section forces symmetry between purchases, sales and inventory. **Sec 145 consistency** stops opportunistic method-switching: a genuine change (say, to comply with a standard) is fine, but a change engineered *only* to reduce this year's stock and profit is rejected, because the whole reliability of accounts rests on comparability year to year. The write-down to NRV is *not* a method change at all — it is the **lower-of-cost-or-NRV** rule applying within the same method, recognising a real economic loss on obsolete goods, so it is respected. The examinable discrimination is distinguishing a *legitimate valuation adjustment (NRV)* from an *illegitimate method change*, and applying 145A's grossing-up even for *unpaid* tax.

*(Full-marks tip: cite Sec 145A inclusive method for the unpaid GST, Sec 145(3) rejection for the mala-fide switch, and defend the NRV write-down as lower-of-cost-or-NRV; treating the NRV write-down as a disallowed change, or ignoring 145A because the GST is unpaid, are the traps.)*

### Q35. Ch: Capital Gains — Indexation + Section 54EC cap across two financial years (Marks: 8) [Problem]
**Question:** Mr. Raghav purchased a plot of urban land on 15 June 2010 for ₹20,00,000. He sold it on 12 June 2024 for ₹1,50,00,000 and paid brokerage of ₹1,50,000. Out of the gains, he invested ₹30,00,000 in NHAI capital-gain bonds on 20 August 2024 and a further ₹30,00,000 in RECL bonds on 5 April 2025 (both within six months of transfer). Compute the taxable capital gain for A.Y. 2025-26 and explain the treatment of his bond investments. (CII: FY 2010-11 = 167; FY 2024-25 = 363.)

**Solution:**

**WN-1 — Nature of gain & applicable regime:** Land held from 15.06.2010 to 12.06.2024 (> 24 months) → **long-term capital asset**. Transfer date 12.06.2024 is **before 23.07.2024**, so the pre-amendment regime applies: **20% with indexation**.

**WN-2 — Indexed cost of acquisition:**
Indexed COA = 20,00,000 × (363 / 167) = 20,00,000 × 2.17365 = **₹43,47,305**.

**WN-3 — Section 54EC exemption:** Investment in specified bonds is eligible, but subject to an **overall ceiling of ₹50,00,000 per assessee across the year of transfer and the succeeding financial year taken together.** He invested ₹30,00,000 + ₹30,00,000 = ₹60,00,000, both within six months. Exemption is **restricted to ₹50,00,000**; the excess ₹10,00,000 gets no benefit.

| Statement Showing Computation of Long-Term Capital Gain (A.Y. 2025-26) | ₹ |
|---|---:|
| Full value of consideration | 1,50,00,000 |
| Less: Expenditure on transfer (brokerage) | (1,50,000) |
| Net consideration | 1,48,50,000 |
| Less: Indexed cost of acquisition (WN-2) | (43,47,305) |
| **Long-term capital gain** | **1,05,02,695** |
| Less: Exemption u/s 54EC (WN-3, capped) | (50,00,000) |
| **Taxable LTCG** | **55,02,695** |

**Answer:** Taxable long-term capital gain = **₹55,02,695**; Section 54EC exemption is limited to **₹50,00,000**.

**Why this way (the reasoning):** Two traps sit inside this problem. First, the proviso to Section 54EC(1) caps aggregate exemption at ₹50 lakh "during any financial year in which the original asset is transferred and in the subsequent financial year." A student who reads the six-month window in isolation would wrongly allow the full ₹60 lakh — the cap is deliberately drafted to stop taxpayers from splitting investment across two years to double the benefit. Second, indexation is available only because the transfer fell before 23.07.2024; had it fallen on or after that date, the new regime (12.5% without indexation) would apply and CII of 363 would be irrelevant. Indexation exists to tax only *real* gains by inflating the historical cost to current rupees, so identifying the correct regime is the very first reasoning step, not an afterthought.

*(Full-marks tip: examiners award the mark for the ₹50 lakh aggregate cap and for a one-line note that the two instalments straddle two FYs but still fall in one 6-month window. Common deduction: allowing ₹60 lakh, or applying 12.5% no-indexation because the student missed the pre-23.07.2024 transfer date.)*

### Q36. Ch: Capital Gains — Section 54F proportionate exemption (Marks: 8) [Problem]
**Question:** Ms. Anita sold gold jewellery (held long-term) on 1 May 2024 for ₹70,00,000, incurring transfer expenses of ₹2,00,000. The jewellery had been purchased in FY 2015-16 for ₹10,00,000. She invested ₹40,00,000 in constructing one residential house. On the date of transfer she owned only the residential flat she lives in (no other house). Compute her taxable capital gain, and state the conditions she must observe to retain the exemption. (CII: FY 2015-16 = 254; FY 2024-25 = 363.)

**Solution:**

**WN-1 — Indexed cost:** Held > 36 months → long-term. Transfer 01.05.2024 is before 23.07.2024 → 20% with indexation.
Indexed COA = 10,00,000 × (363 / 254) = **₹14,29,134**.

**WN-2 — Eligibility for 54F:** The asset transferred is a *long-term capital asset other than a residential house*; on the transfer date she owns **not more than one** residential house (only her self-occupied flat). Both conditions satisfied → 54F available. Since the amount invested (₹40,00,000) is **less than the net consideration** (₹68,00,000), the exemption is **proportionate**.

Exemption u/s 54F = LTCG × (Amount invested in new house ÷ Net consideration).

| Statement Showing Computation of Capital Gain (A.Y. 2025-26) | ₹ |
|---|---:|
| Full value of consideration | 70,00,000 |
| Less: Transfer expenses | (2,00,000) |
| Net consideration | 68,00,000 |
| Less: Indexed cost of acquisition (WN-1) | (14,29,134) |
| **Long-term capital gain** | **53,70,866** |
| Less: Exemption u/s 54F = 53,70,866 × 40,00,000 / 68,00,000 | (31,59,333) |
| **Taxable LTCG** | **22,11,533** |

**Answer:** Taxable LTCG = **₹22,11,533** (exemption u/s 54F = ₹31,59,333).

**Why this way (the reasoning):** 54F rewards *re-channelling the whole sale value* into a house, not merely the gain — that is why the denominator is **net consideration** and not the capital gain. A student who wrongly uses the gain as the base (i.e., exempts the smaller of gain/investment) misunderstands the section's purpose: unlike 54 (which asks you to reinvest only the gain because you already sold a *house*), 54F asks you to reinvest the *entire* proceeds because you sold a *non-house* asset and the law wants the taxpayer genuinely converting other wealth into residential property. She must also not buy/construct another house within the stipulated windows and must hold the new house for 3 years, else the exemption is withdrawn and taxed in the year of default.

*(Full-marks tip: the proportion formula with net consideration as denominator earns the core marks; add the "not more than one house on transfer date" test and the 3-year lock-in. Common deduction: using cost of jewellery or gain as denominator, or forgetting expenses reduce net consideration.)*

### Q37. Ch: Capital Gains — Section 54 and 54F claimed on ONE new house (Marks: 10) [Problem]
**Question:** Mr. Verma, during FY 2024-25 (all transfers before 23 July 2024), made two transfers and one reinvestment:

| Transaction | Amount (₹) |
|---|---:|
| Sale of a residential house (long-term) | 90,00,000 |
| Indexed cost of that house | 40,00,000 |
| Sale of urban vacant land (long-term) | 60,00,000 |
| Indexed cost of that land | 20,00,000 |
| Purchase of ONE new residential house | 1,20,00,000 |

He owns no other residential house. He wishes to claim exemption under Sections 54 and 54F both against the single new house. Advise whether this is permissible and compute his taxable capital gains.

**Solution:**

**WN-1 — Two separate capital gains:**
- House: LTCG = 90,00,000 − 40,00,000 = **₹50,00,000** (eligible for **Sec 54**).
- Land: LTCG = 60,00,000 − 20,00,000 = **₹40,00,000**; net consideration = ₹60,00,000 (eligible for **Sec 54F**).

**WN-2 — Can both be claimed on one house?** Yes. Neither Section 54 nor 54F bars a taxpayer from claiming both against investment in the *same* residential house, **provided the same rupees of investment are not counted twice**. So we allocate the ₹1,20,00,000 cost.

**WN-3 — Section 54 (against house gain):** Investment required = LTCG = ₹50,00,000. Allocate ₹50,00,000 of the new house cost. Since allocation ≥ gain, **entire ₹50,00,000 exempt**.

**WN-4 — Section 54F (against land gain):** Remaining new-house cost = 1,20,00,000 − 50,00,000 = **₹70,00,000**. This exceeds the net consideration of the land (₹60,00,000), so the *entire* land LTCG is exempt:
Exemption = 40,00,000 × 70,00,000 / 60,00,000 → capped at 100% → **₹40,00,000 exempt**.

| Statement Showing Net Taxable Capital Gains | House (₹) | Land (₹) |
|---|---:|---:|
| Long-term capital gain | 50,00,000 | 40,00,000 |
| Less: Exemption (54 / 54F) | (50,00,000) | (40,00,000) |
| **Taxable LTCG** | **Nil** | **Nil** |

**Answer:** Both exemptions are allowable on the single new house; **taxable capital gain = Nil**. The ₹1,20,00,000 cost is sufficient (₹50L used for 54 + ₹70L available for 54F, no double counting).

**Why this way (the reasoning):** Courts (e.g., *Venkata Ramana* and CBDT's acceptance) hold that 54 and 54F are independent beneficial provisions and one house can anchor both, because the statutory language nowhere prohibits it. The single genuine limit is *arithmetic honesty* — the same ₹1 of investment cannot simultaneously shelter two different gains, otherwise a taxpayer could magically exempt ₹90 lakh of gain with only ₹50 lakh of real outlay. Hence we "consume" ₹50 lakh of the house cost for 54 first, then test 54F on the leftover ₹70 lakh. A weak answer either denies both (over-cautious) or double-counts the full ₹1.2 crore for each (dishonest arithmetic); the disciplined allocation is what the examiner is testing.

*(Full-marks tip: state the "no double counting of the same investment" principle explicitly and show the allocation. Common deduction: claiming ₹1.2 crore for each section, or wrongly using gain (not net consideration) in the 54F cap.)*

### Q38. Ch: Capital Gains — Slump Sale under Section 50B (Marks: 10) [Problem]
**Question:** M/s Zenith Ltd. transferred one of its manufacturing undertakings (owned since 2015) as a going concern by way of slump sale on 1 December 2024 for a lump-sum consideration of ₹500 lakh. The undertaking's balance sheet shows:

| Particulars | ₹ (lakh) |
|---|---:|
| Depreciable fixed assets (WDV ₹150; revalued in books to ₹200) | 200 |
| Land (non-depreciable capital asset, book value) | 60 |
| Debtors | 80 |
| Stock-in-trade | 40 |
| Liabilities of the undertaking | 90 |

Compute the capital gain on the slump sale, clearly showing the "net worth," and state its nature.

**Solution:**

**WN-1 — Net worth (deemed cost of acquisition) u/s 50B(2):** Net worth = aggregate value of total assets − value of liabilities, computed on strict rules:
- Depreciable assets → **WDV under the Income-tax Act (₹150 lakh)**, *not* the revalued book figure.
- Other assets → **book value** (Land 60 + Debtors 80 + Stock 40 = 180). **Revaluation is ignored entirely.**

Aggregate assets = 150 + 60 + 80 + 40 = **₹330 lakh**.
Net worth = 330 − 90 (liabilities) = **₹240 lakh**.

**WN-2 — Nature of gain:** Undertaking held > 36 months → **long-term capital gain**. Under the third proviso to Sec 48 / Sec 50B(2), **no indexation** is available on net worth even though the gain is long-term.

| Statement Showing Capital Gain on Slump Sale (Sec 50B) | ₹ (lakh) |
|---|---:|
| Full value of consideration (lump sum) | 500 |
| Less: Net worth (deemed cost, WN-1) | (240) |
| **Long-term capital gain** | **260** |

**Answer:** Long-term capital gain on slump sale = **₹260 lakh** (net worth ₹240 lakh; no indexation).

**Why this way (the reasoning):** A slump sale is the sale of a whole undertaking for one indivisible price without assigning values to individual assets — so the law cannot use "cost of acquisition" in the normal sense. Section 50B invents a proxy: **net worth = deemed cost of acquisition**, and freezes it at tax values so a company cannot inflate its cost (and shrink its gain) by revaluing assets upward in the books. That is precisely why the revaluation to ₹200 lakh is discarded and depreciable blocks are taken at **income-tax WDV** — the whole design is to neutralise book-accounting manoeuvres. Denying indexation is deliberate too: net worth is a residual balancing figure, not a genuine purchase price, so inflation-indexing it would be conceptually meaningless. Students frequently (a) use book/revalued values, or (b) index the net worth — both defeat the section's anti-avoidance logic.

*(Full-marks tip: the marks live in the net-worth working — WDV for depreciable, book value for others, revaluation ignored, liabilities deducted — plus the "no indexation despite LTCG" note. Common deduction: taking revalued ₹200 lakh, or indexing ₹240 lakh.)*

### Q39. Ch: Capital Gains — Section 45(5A) Joint Development Agreement (Marks: 10) [Problem]
**Question:** Mr. Kiran (individual) owned a plot of land acquired in FY 2009-10 for ₹30,00,000. On 1 May 2022 he entered into a registered Joint Development Agreement (JDA) with a builder, handing over possession for development. He was to receive 5 constructed flats plus ₹50,00,000 in cash. The completion certificate for the project was issued on **20 June 2024**; the stamp-duty value of his 5 flats on that date was ₹2,50,00,000, and he received the ₹50,00,000 cash. Compute his capital gain, state the year of taxability, and the cost of the flats for a future sale. (CII: FY 2009-10 = 148; FY 2024-25 = 363.)

**Solution:**

**WN-1 — Year of chargeability (Sec 45(5A)):** For an individual/HUF landowner in a JDA, the capital gain is **not** taxed in the year possession is handed to the builder; it is deferred to the **previous year in which the completion certificate is issued** — i.e., **FY 2024-25 (A.Y. 2025-26)**.

**WN-2 — Full value of consideration:** = **Stamp-duty value of the landowner's share of the project on the date of the completion certificate + cash consideration received**.
FVC = 2,50,00,000 + 50,00,000 = **₹3,00,00,000**.

**WN-3 — Indexed cost:** Land is long-term; CC issued 20.06.2024 (before 23.07.2024) → 20% with indexation, indexation up to FY 2024-25.
Indexed COA = 30,00,000 × (363 / 148) = **₹73,58,108**.

| Statement Showing Capital Gain u/s 45(5A) (A.Y. 2025-26) | ₹ |
|---|---:|
| Full value of consideration (SDV of flats + cash) | 3,00,00,000 |
| Less: Indexed cost of acquisition (WN-3) | (73,58,108) |
| **Long-term capital gain** | **2,26,41,892** |

**WN-4 — Cost of the 5 flats for a future sale:** Under Sec 49(7), the cost of acquisition of the flats = the **stamp-duty value taken as FVC = ₹2,50,00,000** (the cash portion is excluded).

**Answer:** LTCG chargeable in A.Y. 2025-26 = **₹2,26,41,892**; the 5 flats carry a cost of **₹2,50,00,000** for any later sale.

**Why this way (the reasoning):** Ordinarily, handing possession under a development agreement is itself a "transfer" (Sec 2(47)) taxable immediately — which produced a harsh result: landowners were taxed on gains before they received any flat or cash to pay the tax. Section 45(5A) cures this hardship by *postponing* the tax point to completion, when the asset (flats) actually materialises and can be monetised. The full value of consideration is pegged to the **stamp-duty value on the CC date** precisely so that the notional value of what the landowner receives (flats) is captured objectively. The linked Sec 49(7) then makes that same SDV the cost of the flats — otherwise the landowner would be taxed twice on the same value when he eventually sells them. A crucial trap: if the landowner **sells his share before the CC is issued**, Sec 45(5A) is switched off and the gain is taxed in the year of that transfer under normal Sec 45(1) — the concession is only for those who hold on.

*(Full-marks tip: examiners look for (i) year = CC issue year, (ii) FVC = SDV on CC date + cash, and (iii) Sec 49(7) cost link. Common deduction: taxing in the year of the JDA/possession, or omitting the cash in FVC.)*

### Q40. Ch: Capital Gains — New regime: 12.5% without indexation vs 20% with indexation option (Marks: 6) [Problem/Case]
**Question:** Mr. Sharma (resident individual) sold land on 1 September 2024 for ₹1,00,00,000. He had acquired it in FY 2013-14 for ₹25,00,000. Advise which option — (a) 12.5% without indexation, or (b) 20% with indexation — gives him a lower tax, and compute the tax under each. (CII: FY 2013-14 = 220; FY 2024-25 = 363. Ignore surcharge/cess.)

**Solution:**

**WN-1 — Applicability of the option:** Transfer on 01.09.2024 is *after* 23.07.2024, so the default is **12.5% without indexation**. However, because Mr. Sharma is a **resident individual/HUF** and the land (immovable property) was **acquired before 23.07.2024**, he may elect the *lower* of the two computations.

**Option A — 12.5% without indexation:**
LTCG = 1,00,00,000 − 25,00,000 = ₹75,00,000. Tax = 75,00,000 × 12.5% = **₹9,37,500**.

**Option B — 20% with indexation:**
Indexed COA = 25,00,000 × (363 / 220) = 25,00,000 × 1.65 = ₹41,25,000.
LTCG = 1,00,00,000 − 41,25,000 = ₹58,75,000. Tax = 58,75,000 × 20% = **₹11,75,000**.

| Statement Comparing Tax under the Two Options | Option A (₹) | Option B (₹) |
|---|---:|---:|
| Long-term capital gain | 75,00,000 | 58,75,000 |
| Rate | 12.5% | 20% |
| **Tax payable** | **9,37,500** | **11,75,000** |

**Answer:** **Option A (12.5% without indexation) is beneficial** — tax ₹9,37,500 vs ₹11,75,000; saving of **₹2,37,500**.

**Why this way (the reasoning):** The 2024 amendment lowered the rate (20% → 12.5%) but withdrew indexation, and gave resident individuals/HUFs a grandfathering *option* for pre-23.07.2024 property so nobody is worse off than under the old law. The decisive variable is the **ratio of appreciation to inflation**: where the sale price has grown *much faster* than inflation (as here — cost multiplied ~4×, but CII only ~1.65×), indexation shelters relatively little, so the flat 12.5% on a bigger base still beats 20% on a smaller base. Conversely, for slow-appreciating assets held very long, indexation can wipe out most of the gain and Option B wins. The student's job is not to memorise a winner but to *compute both and compare tax (not gain)* — comparing the gain figures alone would mislead, because the rates differ.

*(Full-marks tip: compare the two *tax* amounts, not the two gains, and note the option is confined to resident individual/HUF + immovable property acquired pre-23.07.2024. Common deduction: applying indexation to a post-23.07.2024 transfer without invoking the option, or picking Option B because its "gain" looks smaller.)*

### Q41. Ch: Capital Gains — Listed shares u/s 112A with grandfathering (Marks: 8) [Problem]
**Question:** Mr. Deb acquired 1,000 listed equity shares on 1 May 2016 for ₹2,00,000. Their fair market value on 31 January 2018 (highest quoted price) was ₹5,00,000. He sold all of them on 1 October 2024 for ₹9,00,000 through a recognised stock exchange (STT paid on both purchase and sale). Compute the capital gain and the tax thereon. (Ignore cess/surcharge.)

**Solution:**

**WN-1 — Nature & section:** Listed equity shares held > 12 months, STT paid → **long-term**, taxable under **Section 112A** at **12.5%** (transfer after 23.07.2024) on gains **exceeding ₹1,25,000**. **No indexation** and **no first proviso to Sec 48** benefit.

**WN-2 — Grandfathered cost of acquisition (Sec 55(2)(ac)):** COA = **higher of** (i) actual cost ₹2,00,000, and (ii) **lower of** [FMV on 31.01.2018 ₹5,00,000; sale consideration ₹9,00,000].
Step (ii): lower of (5,00,000, 9,00,000) = ₹5,00,000.
COA = higher of (2,00,000, 5,00,000) = **₹5,00,000**.

| Statement Showing LTCG u/s 112A (A.Y. 2025-26) | ₹ |
|---|---:|
| Full value of consideration | 9,00,000 |
| Less: Grandfathered cost of acquisition (WN-2) | (5,00,000) |
| **Long-term capital gain** | **4,00,000** |
| Less: Exemption threshold u/s 112A | (1,25,000) |
| **Taxable LTCG** | **2,75,000** |
| **Tax @ 12.5%** | **34,375** |

**Answer:** Taxable LTCG = **₹2,75,000**; tax u/s 112A = **₹34,375**.

**Why this way (the reasoning):** When LTCG on listed shares became taxable from 01.04.2018, Parliament did not want to tax gains that had *already accrued* up to 31.01.2018 while the exemption (old Sec 10(38)) was still in force — that would be retrospective. So Sec 55(2)(ac) "grandfathers" the 31.01.2018 value into the cost, sheltering pre-cut-off appreciation. The three-layer formula is engineered so it neither lets you *inflate* cost beyond the actual sale price (the "lower of FMV and sale value" cap prevents manufacturing a loss), nor lets it fall below actual cost (the "higher of" floor). Two figures are commonly misapplied: indexation must **not** be used under 112A, and the exemption is **₹1,25,000** (raised from ₹1,00,000 by the 2024 Budget) — deducted from the gain, not from consideration.

*(Full-marks tip: show the full higher-of/lower-of grandfathering chain and use the ₹1,25,000 threshold at 12.5%. Common deduction: applying indexation, using ₹1,00,000 exemption, or deducting the threshold from sale value instead of from the gain.)*

### Q42. Ch: Income from Other Sources — Sec 56(2)(x) immovable property (Marks: 8) [Problem/Case]
**Question:** During FY 2024-25 Mr. Iqbal (an individual) had the following immovable-property receipts. Determine the amount, if any, chargeable under Section 56(2)(x), with reasons for each.

| Case | Facts |
|---|---|
| (a) | Received a commercial building **as a gift from a friend**; stamp-duty value ₹40,00,000; no consideration paid. |
| (b) | **Purchased** a residential flat for ₹45,00,000 whose stamp-duty value on the date of registration was ₹49,00,000. |
| (c) | Received a house **as a gift from his father**; stamp-duty value ₹80,00,000. |

**Answer:**

**Governing rule (Sec 56(2)(x)):** For immovable property —
- Received **without consideration**: whole **stamp-duty value (SDV)** is taxable if SDV > ₹50,000.
- Received for **inadequate consideration**: (SDV − consideration) is taxable **only if** that difference exceeds **the higher of ₹50,000 and 10% of the consideration** (safe-harbour band).
- **Exception:** receipts from a **"relative"** (which includes father) are wholly exempt, irrespective of value.

**Case (a):** Gift from a *friend* (not a relative), no consideration, SDV ₹40,00,000 > ₹50,000 → **entire ₹40,00,000 taxable**.

**Case (b):** Inadequate consideration. Difference = 49,00,000 − 45,00,000 = ₹4,00,000. Higher of [₹50,000; 10% of 45,00,000 = ₹4,50,000] = **₹4,50,000**. Since the difference (₹4,00,000) does **not exceed** ₹4,50,000 → **nothing taxable** (within safe harbour).

**Case (c):** Gift from **father = relative** → **fully exempt**, even though SDV is ₹80,00,000.

| Statement — Amount Chargeable u/s 56(2)(x) | ₹ |
|---|---:|
| Case (a) — gift from friend (whole SDV) | 40,00,000 |
| Case (b) — within 10% safe harbour | Nil |
| Case (c) — gift from relative (father) | Nil |
| **Total chargeable under IOS** | **40,00,000** |

**Answer:** Total taxable under Sec 56(2)(x) = **₹40,00,000**.

**Why this way (the reasoning):** The section polices *disguised transfers of wealth* — gifts and under-priced sales that would otherwise escape tax. But it draws careful lines. For a *pure gift* the **whole** SDV is taxed (not merely SDV minus zero — the point is the recipient got something for nothing). For an *underpriced purchase* only the shortfall is taxed, and even then a **10% tolerance band** is allowed, recognising that stamp-duty values and negotiated prices legitimately differ by small margins — taxing every ₹1 gap would criminalise normal bargaining. Crucially the two limbs use *different bases*: pure gift → whole SDV; inadequate consideration → gap vs the higher-of test. The **relative** carve-out reflects the policy that intra-family transfers are not attempts to launder untaxed money. A frequent error is applying the 10% band to Case (a) — the band applies only where *some* consideration is paid.

*(Full-marks tip: state the correct base for each limb (whole SDV vs gap), apply the "higher of ₹50,000 or 10%" band only to inadequate-consideration cases, and cite the relative exemption. Common deduction: taxing only the "gap" in a pure-gift case, or missing that 10% of consideration beats ₹50,000 in Case (b).)*

### Q43. Ch: Income from Other Sources — Sec 56(2)(x) money & movable property (Marks: 6) [Problem]
**Question:** Ms. Farah received the following during FY 2024-25. Compute the amount taxable under Section 56(2)(x):

| Receipt | Amount / FMV (₹) |
|---|---:|
| Cash gifts from various friends on her birthday (aggregate) | 80,000 |
| Jewellery received from her fiancé **on the occasion of her marriage** | 3,00,000 |
| Shares of a company gifted by a friend (no consideration) | 60,000 |
| A painting gifted by a friend (no consideration) | 20,000 |

**Solution:**

**WN-1 — Three separate "baskets", each with its own ₹50,000 threshold:** Sec 56(2)(x) tests **(i) money, (ii) immovable property, (iii) other movable property** independently. Within each basket, if the aggregate exceeds ₹50,000, the **whole** aggregate is taxable.

- **Money basket:** cash gifts aggregate ₹80,000 > ₹50,000 → **whole ₹80,000 taxable**.
- **Movable-property basket:** shares ₹60,000 + painting ₹20,000 = ₹80,000 > ₹50,000 → **whole ₹80,000 taxable**.
- **Marriage jewellery ₹3,00,000:** received **on the occasion of the individual's own marriage** → **fully exempt** (specific exclusion), and it is *not* aggregated with the movable basket.

| Statement Showing Income u/s 56(2)(x) | ₹ |
|---|---:|
| Money — cash gifts (whole aggregate) | 80,000 |
| Movable property — shares + painting (whole aggregate) | 80,000 |
| Jewellery on marriage occasion | Exempt |
| **Total taxable under IOS** | **1,60,000** |

**Answer:** Amount taxable under Sec 56(2)(x) = **₹1,60,000**.

**Why this way (the reasoning):** The ₹50,000 threshold is a *per-basket* filter, and once breached it is a **cliff**, not a slab — the *entire* aggregate becomes taxable, not just the excess over ₹50,000. That harsh design deters the splitting of large gifts into many "small" ones. The marriage exclusion is one of the few occasion-based exemptions the section grants (alongside gifts by will/inheritance and from relatives): the legislature accepts that wedding gifts are a social custom, not concealed income — and notably this exemption is tied to the *marriage of the recipient*, not to who gives it, so even a fiancé's gift qualifies. Two classic mistakes: taxing only ₹30,000 (₹80,000 − ₹50,000) instead of the whole basket, and folding the exempt marriage jewellery into the movable basket to breach its threshold.

*(Full-marks tip: treat money and movable as separate baskets, apply the "whole amount once threshold crossed" cliff, and exempt marriage gifts. Common deduction: taxing only the excess over ₹50,000, or aggregating the marriage jewellery.)*

### Q44. Ch: Income from Other Sources — Composite IOS with Sec 57 deductions (Marks: 8) [Problem]
**Question:** Mr. Nair (opting for the **old tax regime**) reports the following for FY 2024-25. Compute his income under the head "Income from Other Sources," showing each deduction under Section 57:

| Item | Amount (₹) |
|---|---:|
| Family pension received (his late father was an employee) | 1,20,000 |
| Interest on enhanced compensation received on compulsory acquisition of land | 2,00,000 |
| Winnings from a lottery (gross) | 50,000 |
| Dividend from a domestic company | 8,000 |
| Interest paid on loan taken to invest in the above shares | 2,000 |

**Solution:**

**WN-1 — Family pension:** Taxable under IOS; deduction u/s **57(iia)** = lower of ₹15,000 or 1/3 of pension (₹40,000) = **₹15,000**. Net = 1,20,000 − 15,000 = **₹1,05,000**.

**WN-2 — Interest on enhanced compensation:** Taxable u/s 56(2)(viii) **in the year of receipt**; a flat **50% deduction** u/s 57(iv) is allowed (no other expense). Net = 2,00,000 × 50% = **₹1,00,000**.

**WN-3 — Lottery winnings:** Taxable u/s 56(2)(ib); **no deduction/expense** allowed, taxed at a flat **30%** (separately). Taxable = **₹50,000**.

**WN-4 — Dividend:** Taxable; only **interest on money borrowed** to earn it is deductible, capped at **20% of the dividend** = 20% × 8,000 = ₹1,600 (against ₹2,000 paid). Net = 8,000 − 1,600 = **₹6,400**.

| Statement Showing Income from Other Sources (A.Y. 2025-26) | ₹ |
|---|---:|
| Family pension (net of 57(iia)) | 1,05,000 |
| Interest on enhanced compensation (net of 57(iv) 50%) | 1,00,000 |
| Dividend (net of capped interest) | 6,400 |
| Lottery winnings (taxed @30%, no deduction) | 50,000 |
| **Income from Other Sources** | **2,61,400** |

**Answer:** Income from Other Sources = **₹2,61,400** (of which ₹50,000 lottery is taxed at the special 30% rate).

**Why this way (the reasoning):** Section 57 is deliberately *stingy and item-specific* because IOS is the residual head — the law allows only expenses with a direct, defined nexus to earning that income. Family pension gets an *ad-hoc* 57(iia) deduction (a proxy for effort/collection cost) because there is no real expense. Interest on enhanced compensation is a windfall spread over years, so 57(iv) fixes a blanket 50% deduction rather than tracing actual costs, and it is taxed on *receipt* (not accrual) to match the taxpayer's cash. Dividend expense is capped at 20% to stop taxpayers from over-leveraging to convert income into a deductible interest loss. Lottery income (Sec 115BB) is ring-fenced at 30% with **zero** deductions and no basic-exemption benefit — the policy is that windfall gains should not be diluted by expenses. A weak answer allows the full ₹2,000 dividend interest, deducts expenses from lottery, or taxes the compensation interest on accrual.

*(Full-marks tip: the four correctly-capped deductions (₹15,000; 50%; nil on lottery; 20% on dividend) each carry marks; flag that lottery is taxed at a flat 30%. Common deduction: giving 1/3 (₹40,000) on family pension, or allowing expenses against lottery.)*

### Q45. Ch: IOS + Capital Gains interplay — Sec 49(4) cost after 56(2)(x) (Marks: 6) [Case]
**Question:** In FY 2022-23, Mr. Bose received unlisted shares as a gift from a friend; their fair market value of ₹5,00,000 was duly charged to tax in his hands under Section 56(2)(x). He sold those shares in FY 2024-25 for ₹8,00,000. Determine his capital gain, and explain how his cost of acquisition and period of holding are fixed. (Assume no indexation benefit is claimed; sale before 23.07.2024 not relevant here — treat gain as arising per the applicable regime.)

**Answer:**

**Governing rule:** Where an asset's value was earlier taxed under Sec 56(2)(x), **Section 49(4)** provides that the **cost of acquisition** on a later sale is **the value that was taken into account for Sec 56(2)(x)** — here ₹5,00,000. The **period of holding** is reckoned from the **date the recipient (Mr. Bose) acquired the asset**, i.e., from FY 2022-23 (the previous-owner's holding is *not* tacked on in a 56(2)(x)-taxed acquisition). Holding from FY 2022-23 to FY 2024-25 on unlisted shares (> 24 months) → **long-term**.

| Statement Showing Capital Gain (A.Y. 2025-26) | ₹ |
|---|---:|
| Full value of consideration | 8,00,000 |
| Less: Cost of acquisition u/s 49(4) | (5,00,000) |
| **Long-term capital gain** | **3,00,000** |

**Answer:** LTCG = **₹3,00,000**, using cost of ₹5,00,000 fixed by Sec 49(4).

**Why this way (the reasoning):** This is the anti-**double-taxation** bridge between two heads. Mr. Bose already paid tax on the ₹5,00,000 "gift value" as IOS. If, on sale, his cost were treated as **nil** (the usual rule for gifted assets received without paying anything), he would be taxed a *second time* on that same ₹5,00,000 as capital gain. Section 49(4) prevents this by stepping up his cost to the already-taxed value, so only the *further* appreciation (₹3,00,000) is taxed on sale. The subtle point examiners probe is the **period of holding** — because the recipient's own tax event (56(2)(x)) crystallised the value, holding runs from *his* acquisition date, not the donor's; there is no "previous owner" tacking as there is for exempt gifts under Sec 49(1). Getting this right decides whether the gain is short- or long-term.

*(Full-marks tip: cite Sec 49(4) for cost and correctly start holding from the recipient's date. Common deduction: taking cost as nil (double taxation) or tacking the friend's holding period.)*

### Q46. Ch: Clubbing & Set-off — Remuneration to spouse from a concern (Sec 64(1)(ii)) (Marks: 8) [Case/Problem]
**Question:** Examine the clubbing implications in each independent situation for A.Y. 2025-26, with reasons:

| Situation | Facts |
|---|---|
| (a) | Mr. A holds 25% of the voting power in P Ltd. His wife, Mrs. A (a qualified MBA in Finance), is employed there as CFO drawing ₹9,00,000 p.a. |
| (b) | Mr. B holds 30% of the shares of Q Ltd. His wife, Mrs. B (no professional/technical qualification), is paid ₹6,00,000 p.a. as a "consultant." |
| (c) | Both Mr. C and Mrs. C hold 22% each in R Ltd. Both are paid a salary of ₹5,00,000 each; Mr. C's other income is ₹12,00,000, Mrs. C's ₹8,00,000. Neither has technical/professional qualifications relevant to the role. |

**Answer:**

**Governing rule (Sec 64(1)(ii)):** Any **salary/commission/fees/remuneration** paid by a concern to the spouse of an individual who has **substantial interest** (≥ 20% of voting power or profits) in that concern is **clubbed** in the individual's income — **unless** the spouse possesses **technical or professional qualifications** and the income is **solely attributable to the application of that knowledge/experience**. Where **both spouses have substantial interest** and both are paid, the remuneration is clubbed in the hands of the spouse whose **total income (before such remuneration) is higher**.

**Situation (a):** Mr. A has substantial interest (25% > 20%). But Mrs. A holds a **relevant professional qualification (MBA Finance)** and earns as CFO by applying it → **exception applies; not clubbed**. Her ₹9,00,000 is taxed in her own hands.

**Situation (b):** Mr. B has substantial interest (30%). Mrs. B has **no qualification** and the payment is not attributable to any special skill → **exception unavailable; ₹6,00,000 clubbed in Mr. B's income**.

**Situation (c):** **Both** spouses have substantial interest (22% each) and are paid; no qualification exception. Clubbing occurs in the hands of the spouse with **higher total income before remuneration** — Mr. C (₹12,00,000 > ₹8,00,000). Therefore **both salaries (₹5,00,000 + ₹5,00,000 = ₹10,00,000)** are clubbed in **Mr. C's** hands. (Once so clubbed, the tax authority need not reshuffle in later years unless satisfied it is necessary.)

**Why this way (the reasoning):** The mischief targeted is **income-splitting within a family** — a controlling shareholder routing part of the company's profit to a spouse as "salary" to exploit two sets of slab rates. Hence, wherever the spouse's pay is really a *disguised return on the individual's control*, it is pulled back. But the law does not want to penalise a spouse who *genuinely earns* through real expertise — so the **qualification-plus-application** exception (situation a) protects bona fide professionals; a mere degree is not enough, the income must flow from *applying* it. In situation (c) both spouses trigger the clause, so a **tie-breaker** is needed; the "higher total income" rule ensures the family cannot pick the lower-income spouse to minimise tax, and the stability proviso avoids annual flip-flopping.

*(Full-marks tip: the exception needs *both* a qualification *and* income attributable to it — say so; and apply the "higher income spouse" tie-breaker in (c). Common deduction: clubbing Mrs. A's professional salary, or splitting (c) across both spouses instead of pooling in the higher-income spouse.)*

### Q47. Ch: Clubbing & Set-off — Minor child's income under Sec 64(1A) (Marks: 8) [Problem]
**Question:** Mr. and Mrs. Rao have three minor children. Mrs. Rao's total income (before clubbing) exceeds Mr. Rao's. For FY 2024-25:

| Child | Income earned |
|---|---|
| Minor son P | Interest on a fixed deposit (gifted by grandfather): ₹40,000 |
| Minor daughter Q | ₹2,00,000 earned from stage/dance performances (her own skill); she invested this and earned FD interest of ₹15,000 |
| Minor son R (suffers from a disability specified u/s 80U) | Interest income of ₹30,000 |

Compute the amount to be clubbed and in whose hands, applying Section 64(1A) and Section 10(32).

**Solution:**

**WN-1 — General rule & exceptions (Sec 64(1A)):** A minor's income is clubbed with the parent whose **total income is higher** (here **Mrs. Rao**). **Exceptions — not clubbed:** (i) income from the minor's **manual work or skill/talent/specialised knowledge**, and (ii) income of a **minor suffering from disability specified u/s 80U** (taxed in the minor's own hands). A **Sec 10(32) exemption of ₹1,500 per child** is allowed against each clubbed income.

**WN-2 — Item-wise treatment:**
- **Son P — FD interest ₹40,000:** ordinary investment income → **clubbed**. Net = 40,000 − 1,500 = **₹38,500**.
- **Daughter Q:** the ₹2,00,000 from performance is earned by **her own skill/talent → NOT clubbed**. **But** the ₹15,000 interest earned by *investing* that money is **not** skill income → **clubbed**. Net = 15,000 − 1,500 = **₹13,500**.
- **Son R (disabled u/s 80U):** interest ₹30,000 → **not clubbed** at all (taxed in his own hands).

| Statement Showing Income Clubbed in Mrs. Rao's Hands | ₹ |
|---|---:|
| Son P — FD interest (40,000 − 1,500) | 38,500 |
| Daughter Q — interest on invested earnings (15,000 − 1,500) | 13,500 |
| Daughter Q — performance income (own skill) | Not clubbed |
| Son R — disabled child (Sec 64(1A) exception) | Not clubbed |
| **Total clubbed** | **52,000** |

**Answer:** **₹52,000** is clubbed in **Mrs. Rao's** income (higher-earning parent).

**Why this way (the reasoning):** Minors cannot ordinarily generate independent income, so passive income arising to a minor is presumed to flow from *the parents' wealth* and is clubbed to stop parents parking investments in a child's name to split income. But the law respects the child's **own effort** — genuine earnings from talent/skill/manual work belong to the child, because there is no parental income being disguised. The trap here is that this protection is *one generation deep*: once the skill-money is **re-invested**, the resulting interest is ordinary investment income and re-enters clubbing — the exception covers the *earning*, not its *future fruits*. The disabled-child exception reflects a welfare policy: such a child's income stays with the child. Finally, the ₹1,500 per-child relief under Sec 10(32) applies **per income clubbed, per child**, not once overall.

*(Full-marks tip: distinguish the skill-earning (exempt from clubbing) from its reinvested income (clubbed), exclude the 80U child, and deduct ₹1,500 per clubbed item. Common deduction: clubbing Q's ₹2,00,000 performance income, or giving only one ₹1,500 deduction.)*

### Q48. Ch: Clubbing & Set-off — Transfer of asset to spouse; income on income; cross transfers (Marks: 8) [Case]
**Question:** Analyse the clubbing consequences for A.Y. 2025-26, with reasons, in Mr. X's hands:

| Situation | Facts |
|---|---|
| (a) | Mr. X gifted ₹10,00,000 to his wife, who deposited it in an FD earning ₹80,000 interest. She then reinvested that ₹80,000 in shares, earning a dividend of ₹6,000. |
| (b) | Mr. X transferred a house property to his wife "for ₹1" (inadequate consideration). The house yields net rental income of ₹3,00,000. |
| (c) | Mr. X gifted ₹5,00,000 to Mr. Y's wife, and (by prior mutual arrangement) Mr. Y gifted an equal ₹5,00,000 to Mr. X's wife. Each amount earns interest of ₹40,000. |

**Answer:**

**Governing rule (Sec 64(1)(iv)):** Income arising to a **spouse** from an asset **transferred directly or indirectly without adequate consideration** (otherwise than in connection with an agreement to live apart) is **clubbed** with the transferor. Two settled riders: **(i)** clubbing catches income from the transferred asset, but **not "income on income"** (accretion); **(ii)** genuine but colourable **cross transfers** are seen through and clubbed as if each person transferred to his own spouse.

**Situation (a):** The ₹80,000 FD interest arises from the gifted ₹10,00,000 → **clubbed in Mr. X (₹80,000)**. The ₹6,000 dividend arises from investing the *interest* (income on income), **not** from the original gifted asset → **not clubbed**; it is the wife's own income.

**Situation (b):** House transferred for grossly **inadequate consideration** → covered by Sec 64(1)(iv). The **₹3,00,000 rental income is clubbed** in Mr. X. (Note: for the *deemed-ownership* fiction under Sec 27, the house may also be treated as belonging to Mr. X, reinforcing that the rent is his.)

**Situation (c):** These are **cross transfers** — intimately connected and designed to sidestep clubbing. Applying the substance-over-form principle (*CIT v. Keshavji Morarji*), they are treated as if **Mr. X gifted to his own wife**. Hence the **₹40,000 interest earned by Mr. X's wife is clubbed in Mr. X** (and correspondingly Mr. Y's wife's ₹40,000 in Mr. Y).

**Why this way (the reasoning):** Sec 64(1)(iv) exists because a straightforward gift to a spouse would otherwise shift the *future income stream* to a lower-taxed person while the family retains the wealth. So the law follows the **income of the transferred asset** back to the transferor. But it stops at *one generation* — once that clubbed income is separately reinvested, the second-level return is genuinely the spouse's own capital at work, and clubbing "income on income" would extend the fiction indefinitely, which the courts have refused to do. The cross-transfer rule is pure **substance over form**: two mirror-image gifts that cancel out economically are an obvious device to dodge the direct-transfer test, so the arrangement is unwound and treated as each spouse funding his own. A weak answer clubs the ₹6,000 dividend, or lets the cross transfers escape because "X did not gift to his own wife."

*(Full-marks tip: club the first-level income but expressly exempt the "income on income," and pierce the cross transfers with the Keshavji Morarji principle. Common deduction: clubbing the ₹6,000 accretion, or treating (c) as outside 64(1)(iv).)*

### Q49. Ch: Clubbing & Set-off — Intra-head then inter-head set-off ordering (Marks: 10) [Problem]
**Question:** Compute the Gross Total Income of Mr. Menon for A.Y. 2025-26 and state the loss, if any, to be carried forward, applying the correct set-off sequence:

| Head / item | Amount (₹) |
|---|---:|
| Income from Salary | 8,00,000 |
| Loss from self-occupied house property (interest on housing loan) | (2,50,000) |
| Loss from a normal (non-speculative) business | (1,50,000) |
| Profit from a speculative business | 40,000 |
| Short-term capital loss | (60,000) |
| Long-term capital gain (taxable) | 1,00,000 |
| Income from other sources (interest) | 90,000 |

**Solution:**

**WN-1 — Intra-head set-off (capital gains):** STCL of ₹60,000 may be set off against any capital gain. Set off against LTCG ₹1,00,000 → **net capital gains = ₹40,000** (LTCG).

**WN-2 — House-property loss (Sec 71B ceiling):** Loss under "house property" can be set off against other heads only up to **₹2,00,000** in a year. Loss = ₹2,50,000 → set off ₹2,00,000 against Salary; **balance ₹50,000 carried forward** (up to 8 years, against house-property income only).

**WN-3 — Business loss (Sec 71):** A **normal business loss cannot be set off against Salary**, but can be set off against any other head (except the specific bars). Available non-salary income after WN-1/WN-2 = Speculation ₹40,000 + Capital gains ₹40,000 + IOS ₹90,000 = ₹1,70,000. Business loss ₹1,50,000 is **fully absorbed** (assessee's choice of order). Balance non-salary income = 1,70,000 − 1,50,000 = ₹20,000.
*(Speculation profit can absorb a normal business loss; the reverse — speculation loss against normal income — is not allowed.)*

| Statement Showing Gross Total Income (A.Y. 2025-26) | ₹ |
|---|---:|
| Salary | 8,00,000 |
| Less: House-property loss set off (max, Sec 71B) | (2,00,000) |
| Salary after set-off | 6,00,000 |
| Speculation profit | 40,000 |
| Capital gains (LTCG net of STCL, WN-1) | 40,000 |
| Income from other sources | 90,000 |
| Sub-total (non-salary) | 1,70,000 |
| Less: Normal business loss (WN-3) | (1,50,000) |
| Non-salary income after set-off | 20,000 |
| **Gross Total Income** | **6,20,000** |

**Carried forward:** House-property loss **₹50,000** (Sec 71B, 8 years).

**Answer:** Gross Total Income = **₹6,20,000**; carry forward house-property loss of **₹50,000**.

**Why this way (the reasoning):** Set-off has a mandatory *architecture*: **first intra-head** (Sec 70) — hence STCL is neutralised inside capital gains before anything leaves the head — **then inter-head** (Sec 71). Two guard-rails then bite. The **₹2,00,000 house-property cap** (Sec 71B, inserted to curb high-value taxpayers wiping out salary with large housing-loan interest) forces the excess ₹50,000 to be carried forward rather than fully set off now. And a **normal business loss cannot touch salary** — a deliberate policy protecting the salary base from business losses — though it *may* be set against speculation profit, capital gains and IOS. Note the asymmetry that trips students: a *normal* loss can be relieved by *speculative* profit, but a *speculative* loss can only be relieved by *speculative* profit (Sec 73). Because the taxpayer may choose the order of inter-head set-off, the business loss here is arranged to be fully absorbed, leaving no business loss to carry forward.

*(Full-marks tip: show intra-head first, apply the ₹2,00,000 HP cap with carry-forward, and keep business loss away from salary. Common deduction: setting HP loss fully against salary, or setting the normal business loss against salary income.)*

### Q50. Ch: Clubbing & Set-off — Carry-forward periods, order of set-off, and return-filing condition (Marks: 6) [Theory/Case]
**Question:** Mr. Sethi incurred, in FY 2024-25, a normal business loss of ₹4,00,000 and unabsorbed depreciation of ₹1,00,000, which could not be set off in the year. He filed his return of income on 15 December 2025 (the Sec 139(1) due date being 31 October 2025). (a) State which of these losses he can carry forward, and for how long. (b) Explain the statutory **order** in which brought-forward losses and depreciation are set off. (c) Summarise the carry-forward periods for the main loss categories.

**Answer:**

**(a) Effect of the belated return (Sec 80 read with Sec 139(3)):** A **business loss** can be carried forward **only if the return is filed within the Sec 139(1) due date**. Mr. Sethi filed *late* (15.12.2025 vs 31.10.2025), so his **₹4,00,000 business loss lapses** — it cannot be carried forward. **However, unabsorbed depreciation** is governed by **Sec 32(2)**, which is **not** subject to the timely-return condition; therefore the **₹1,00,000 depreciation can still be carried forward** despite the late return.

**(b) Order of set-off in a subsequent year** (well-settled sequence): **(1)** current year's depreciation, **(2)** current year's business loss, **(3)** brought-forward business loss, **(4)** unabsorbed depreciation (and unabsorbed capital expenditure on scientific research/family planning). Unabsorbed depreciation is set off **last** because it enjoys the most generous carry-forward and should be preserved.

**(c) Carry-forward periods:**

| Loss category | C/F period | Set off against |
|---|---|---|
| Normal business loss (Sec 72) | 8 assessment years | Business income (any business) |
| Speculation loss (Sec 73) | 4 assessment years | Speculation income only |
| Specified-business loss u/s 35AD (Sec 73A) | Indefinite | Specified-business income |
| Capital loss (Sec 74) | 8 assessment years | Capital gains (LTCL vs LTCG only) |
| House-property loss (Sec 71B) | 8 assessment years | House-property income |
| Loss from owning & maintaining race horses (Sec 74A) | 4 assessment years | Same activity only |
| Unabsorbed depreciation (Sec 32(2)) | Indefinite | Any head except salary |

**Why this way (the reasoning):** The **timely-return condition** (Sec 139(3)/80) is a compliance discipline: the privilege of parking a loss for future relief is granted only to taxpayers who report it on time, so the department can verify it. Unabsorbed depreciation is deliberately carved out — depreciation is a *statutory allowance* that merely could not be absorbed for want of profit, not a "loss" the taxpayer failed to disclose, so it is not penalised by lapse and even survives indefinitely and against most heads. The **set-off order** protects the taxpayer's *most valuable* relief: current depreciation and current/brought-forward business losses (which expire in 8 years) are used up first, and the indefinitely-available unabsorbed depreciation is consumed last, maximising the total relief actually obtained. House-property loss and unabsorbed depreciation are the two items that survive a late return — a distinction examiners love to test.

*(Full-marks tip: nail the late-return rule (business loss lapses, depreciation survives), the four-step set-off order, and the period table. Common deduction: allowing carry-forward of the business loss despite the belated return, or setting unabsorbed depreciation before brought-forward business loss.)*

### Q51. Ch: Clubbing & Set-off (integrated with Capital Gains & IOS) — Composite computation (Marks: 10) [Problem]
**Question:** Compute the total income of Mr. Pillai for A.Y. 2025-26 and the tax on his capital gains, integrating clubbing and set-off. (Mrs. Pillai's independent total income is lower than Mr. Pillai's; the minor son's income is to be clubbed with Mr. Pillai.)

| Item | Amount (₹) |
|---|---:|
| Salary income | 12,00,000 |
| Loss from a **let-out** house property | (3,00,000) |
| Long-term capital gain on Mr. Pillai's **own** listed shares (Sec 112A, STT paid) | 2,00,000 |
| Short-term capital loss on listed shares (Sec 111A) | (80,000) |
| LTCG (Sec 112A) earned by Mrs. Pillai on shares bought with ₹20,00,000 **gifted by Mr. Pillai** | 1,50,000 |
| Fixed-deposit interest of the **minor son** (from grandparent's gift) | 45,000 |

**Solution:**

**WN-1 — Clubbing:**
- Mrs. Pillai's LTCG ₹1,50,000 arises from shares bought with money gifted by Mr. Pillai → **Sec 64(1)(iv)** clubs it in Mr. Pillai. Crucially, the clubbed income **retains its character** as Sec 112A LTCG.
- Minor son's FD interest → **Sec 64(1A)**, clubbed in Mr. Pillai; less Sec 10(32) ₹1,500 = **₹43,500** (taxable as IOS).

**WN-2 — Capital gains set-off (intra-head):** Total Sec 112A LTCG = own ₹2,00,000 + clubbed ₹1,50,000 = **₹3,50,000**. STCL of ₹80,000 (Sec 111A) may be set off against **any** capital gain, including LTCG → LTCG after set-off = 3,50,000 − 80,000 = **₹2,70,000**.
Taxable LTCG u/s 112A = 2,70,000 − 1,25,000 (threshold) = **₹1,45,000**; tax @ 12.5% = **₹18,125**.

**WN-3 — House-property loss:** Let-out property loss ₹3,00,000; inter-head set-off against salary capped at **₹2,00,000** (Sec 71B). Set off ₹2,00,000 against salary; **₹1,00,000 carried forward**.

| Statement Showing Total Income (A.Y. 2025-26) | ₹ |
|---|---:|
| Salary | 12,00,000 |
| Less: House-property loss (Sec 71B cap) | (2,00,000) |
| Income under "Salary" (net) | 10,00,000 |
| Capital gains — LTCG u/s 112A (WN-2) | 1,45,000 |
| Income from Other Sources — clubbed minor's interest (WN-1) | 43,500 |
| **Total Income** | **11,88,500** |

**Working of tax on capital gains:** LTCG u/s 112A above ₹1,25,000 = ₹1,45,000 × 12.5% = **₹18,125** (the balance income is taxed at slab/normal rates; ignored here).
**Carried forward:** House-property loss ₹1,00,000.

**Answer:** Total Income = **₹11,88,500**; tax on the ₹1,45,000 taxable LTCG (112A) = **₹18,125**; carry forward house-property loss **₹1,00,000**.

**Why this way (the reasoning):** This question deliberately interleaves three chapters and rewards *sequencing discipline*. **Clubbing happens first** — you must pull Mrs. Pillai's LTCG and the minor's interest into Mr. Pillai's computation *before* set-off, and the clubbed LTCG **keeps its 112A character**, because clubbing transfers the *income with its head and nature*, not a stripped number. Only then do you apply **intra-head set-off**: the STCL is set against the (now larger) LTCG pool — a taxpayer-favourable move, since a short-term loss is allowed against a long-term gain (though never the reverse). The **₹1,25,000 exemption applies to the aggregate 112A LTCG** (own + clubbed), not per person — a subtle point, since the exemption follows the income into the assessee's return. Finally the **house-property cap** (Sec 71B) limits relief to ₹2,00,000 and forces the ₹1,00,000 carry-forward. Common failure modes: setting the STCL off before clubbing the wife's gain (understating the pool), taxing the clubbed LTCG at slab rates (ignoring 112A character), or giving two ₹1,25,000 exemptions.

*(Full-marks tip: examiners want the exact order — club → intra-head set-off → inter-head cap — plus the clubbed LTCG retaining 112A/12.5% character and a single ₹1,25,000 threshold. Common deduction: taxing clubbed LTCG at normal rates, double-counting the exemption, or setting HP loss beyond ₹2,00,000.)*

### Q52. Ch: Computation of Total Income — Full multi-head computation with every adjustment note (Marks: 10) [Problem]
**Question:** Mr. Arun (aged 45, resident) furnishes the following for PY 2024-25. He opts OUT of the default regime and is taxed under the **old regime**. Compute his Total Income and tax liability, giving a note justifying **every** adjustment.

| Particulars | Amount (₹) |
|---|---|
| Basic salary (₹80,000 × 12) | 9,60,000 |
| Dearness allowance (₹40,000 × 12); 50% forms part of retirement benefits | 4,80,000 |
| HRA received (₹30,000 × 12) — rent paid ₹35,000 p.m. at Mumbai | 3,60,000 |
| Let-out house: MV 3,00,000; FR 3,50,000; SR 3,20,000; actual rent ₹30,000 p.m.; municipal tax paid 30,000; interest on loan 2,20,000 | — |
| LTCG on listed equity shares (STT paid), sold Sept 2024 | 1,50,000 |
| Savings bank interest 12,000; FD interest 60,000; dividend (Indian cos.) 25,000; lottery winning (gross) 50,000 | — |
| 80C investments (PPF + LIC) ₹1,80,000; Mediclaim: self ₹28,000, senior-citizen parents ₹55,000; donation to PM National Relief Fund ₹20,000 | — |

**Solution:**

**WN-1 — HRA exemption (Sec 10(13A)):** Salary for HRA = Basic + DA in terms = 9,60,000 + 2,40,000 = 12,00,000. Least of (a) actual HRA 3,60,000; (b) 50% (metro) of 12,00,000 = 6,00,000; (c) rent 4,20,000 − 10% of 12,00,000 = 3,00,000. Least = **₹3,00,000 exempt**; taxable HRA = 60,000.

**WN-2 — Salary:** 9,60,000 + 4,80,000 + 3,60,000 = 18,00,000 − 3,00,000 (HRA) − 50,000 (std. deduction) = **₹14,50,000**.

**WN-3 — House property:** Expected rent = higher of MV/FR = 3,50,000, capped at SR 3,20,000. Actual rent 3,60,000 > expected ⇒ GAV 3,60,000. NAV = 3,60,000 − 30,000 = 3,30,000. Less 30% = 99,000; less interest 2,20,000 ⇒ **₹11,000**.

**WN-4 — Deductions:** 80C = 1,50,000 (capped). 80D = 25,000 (self, <60) + 50,000 (senior parents) = **75,000**. 80TTA = 10,000 (of 12,000). 80G (PMNRF, 100%, no qualifying limit) = **20,000**.

| Statement of Total Income & Tax — Mr. Arun (AY 2025-26, old regime) | ₹ | ₹ |
|---|---:|---:|
| Salaries (WN-2) | | 14,50,000 |
| Income from house property (WN-3) | | 11,000 |
| Capital gains — LTCG u/s 112A | | 1,50,000 |
| Other sources: SB 12,000 + FD 60,000 + Lottery 50,000 (dividend 25,000 also taxable) | | 1,47,000 |
| **Gross Total Income** | | **17,58,000** |
| Less: 80C 1,50,000 + 80D 75,000 + 80TTA 10,000 + 80G 20,000 | | (2,55,000) |
| **Total Income** | | **15,03,000** |
| Split: Normal 13,03,000; LTCG 112A 1,50,000; Lottery 50,000 | | |
| Tax on normal (12,500 + 1,00,000 + 90,900) | 2,03,400 | |
| LTCG: (1,50,000 − 1,25,000) × 12.5% | 3,125 | |
| Lottery 50,000 × 30% | 15,000 | |
| Tax + HEC 4% (2,21,525 + 8,861) | | **2,30,390** |

**Answer:** Total Income = **₹15,03,000**; Tax liability = **₹2,30,390**.

**Why this way (the reasoning):** The head-wise architecture is not cosmetic — each head has its own charging and computation logic, and mixing them causes error. HRA "salary" deliberately includes only DA *in terms of retirement benefits* because the exemption is a proxy for genuine housing cost measured against retirement-linked pay, not gross pay. In house property, the *expected rent* is capped at standard rent because rent control law caps what the owner could legally have earned — you cannot tax a notional income the law forbids. Crucially, Chapter VI-A deductions and the ₹1,25,000 LTCG shield and the 30% lottery rate operate on *segregated* baskets: 80C/80D/80G can be claimed only against normal income, never against 112A LTCG or casual lottery income — a student who nets deductions against the whole ₹17,58,000 overstates relief and understates tax. The tempting shortcut of taxing everything at slab rates is wrong because special-rate incomes (12.5% and flat 30%) are carved out *before* slabs apply.

*(Full-marks tip: examiners award the "note justifying each adjustment" column — bare figures without the WHY of HRA salary base, SR cap, and the deduction/special-rate segregation lose 3–4 marks even if the ₹ is right.)*

---

### Q53. Ch: Deductions under Chapter VI-A — 80G qualifying-limit ordering logic (Marks: 8) [Problem]
**Question:** For PY 2024-25, Mr. Bose (old regime) has GTI ₹10,00,000, which includes LTCG u/s 112A ₹1,00,000 and STCG u/s 111A ₹40,000. Deductions other than 80G: 80C ₹1,50,000, 80D ₹25,000, 80TTA ₹8,000. Donations: (i) PM National Relief Fund ₹50,000; (ii) Government, for promotion of family planning ₹40,000; (iii) an approved charitable trust ₹1,20,000; (iv) a local temple trust ₹15,000 paid **in cash**. Compute the 80G deduction.

**Solution:**

**WN-1 — Adjusted GTI (base for the 10% qualifying limit):** GTI − LTCG 112A − STCG 111A − deductions under 80C to 80U except 80G. = 10,00,000 − 1,00,000 − 40,000 − (1,50,000 + 25,000 + 8,000) = **₹6,77,000**. Qualifying limit = 10% = **₹67,700**.

**WN-2 — Classify donations:** (i) PMNRF → 100%, **no** qualifying limit. (ii) Family planning to Govt → 100% **with** limit. (iii) Charitable trust → 50% **with** limit. (iv) Cash ₹15,000 > ₹2,000 ⇒ **fully disallowed** (Sec 80G(5D)).

| Statement of 80G deduction | ₹ |
|---|---:|
| Category A — 100% without limit: PMNRF | 50,000 |
| Within qualifying limit ₹67,700 — priority to 100%-with-limit: Family planning 40,000 × 100% | 40,000 |
| Remaining limit = 67,700 − 40,000 = 27,700; trust (50% category) restricted to 27,700, then × 50% | 13,850 |
| Cash temple donation | Nil |
| **Total deduction u/s 80G** | **1,03,850** |

**Answer:** 80G deduction = **₹1,03,850**.

**Why this way (the reasoning):** 80G has a two-tier gate that trips most students. First, the qualifying limit is 10% of *Adjusted* GTI, not GTI — special-rate incomes (112A/111A) and all other Chapter VI-A deductions are stripped out first, because Parliament did not want charity relief inflated by capital gains taxed at concessional rates. Second, *within* the qualifying-limit pool, 100%-with-limit donations are exhausted **before** 50%-with-limit donations. Ordering matters because the ceiling is shared: give priority to the higher-percentage donation and the taxpayer extracts maximum relief; reverse the order and you waste ceiling on a 50% claim, understating the deduction. The ₹2,000 cash bar is an anti-evasion rule — untraceable cash cannot be verified, so it is disallowed outright, not merely capped.

*(Full-marks tip: the classic error is applying 50% to the *whole* ₹1,20,000 before capping. Cap first at the residual qualifying limit, THEN apply 50% — reversing these steps overstates the deduction by thousands.)*

---

### Q54. Ch: Advance Tax / TDS / TCS — Interest u/s 234B and 234C (Marks: 8) [Problem]
**Question:** For AY 2025-26, tax on Mr. Chandra's returned income (incl. cess) is ₹1,80,000; TDS credit ₹30,000. Advance tax paid: 15 Jun ₹20,000; 15 Sep ₹50,000; 15 Dec ₹30,000; 15 Mar ₹20,000. Return filed (with self-assessment tax) on 31 July 2025. Compute interest u/s 234B and 234C.

**Solution:**

**WN-1 — Assessed tax:** 1,80,000 − 30,000 (TDS) = **₹1,50,000**. 90% = ₹1,35,000. Total advance tax paid = ₹1,20,000 < ₹1,35,000 ⇒ **234B applies**.

**WN-2 — 234B:** Shortfall = 1,50,000 − 1,20,000 = 30,000. Period = 1 Apr 2025 to date of payment (July, being month of return/SA tax) = 4 months. Interest = 30,000 × 1% × 4 = **₹1,200**.

**WN-3 — 234C (safe-harbour thresholds on assessed tax ₹1,50,000):**

| Due date | Min. required | Cumulative paid | Short? | Interest |
|---|---:|---:|---:|---:|
| 15 Jun | 12% = 18,000 | 20,000 | No | Nil |
| 15 Sep | 36% = 54,000 | 70,000 | No | Nil |
| 15 Dec | 75% = 1,12,500 | 1,00,000 | 12,500 | 12,500×1%×3 = 375 |
| 15 Mar | 100% = 1,50,000 | 1,20,000 | 30,000 | 30,000×1%×1 = 300 |

234C total = **₹675**.

**Answer:** Interest u/s 234B = **₹1,200** and u/s 234C = **₹675**; total = **₹1,875**.

**Why this way (the reasoning):** 234B and 234C police two different failures and therefore never overlap. 234C is *installment* discipline — it charges interest for paying late *during* the year, computed installment-by-installment on the deferred amount; 234B is the *year-end* deficiency — it charges interest for entering the assessment year with less than 90% paid. The June and September gates use relaxed 12%/36% safe harbours (versus the notional 15%/45%) precisely because early-year income is hard to estimate, so Parliament forgives a small early shortfall. Note the shortfalls compound differently: the December gap of ₹12,500 attracts 3 months, but the March gap of ₹30,000 only 1 month, because interest runs to year-end from each installment. A student who applies 234B on the *gross* tax (ignoring TDS) inflates the base — "assessed tax" is always net of TDS/TCS/relief.

*(Full-marks tip: show the cumulative-paid column and the 12%/36% safe harbours explicitly. Charging 234C at 15%/45% instead of the safe-harbour rates for June/Sep is the most-penalised error.)*

---

### Q55. Ch: Advance Tax / TDS / TCS — TDS section selection & rate (Marks: 6) [Case/Application]
**Question:** ABC Ltd (turnover ₹80 crore last year) makes these payments in FY 2024-25. For each, identify the **correct TDS section, threshold and rate**, and justify the *selection* where two sections compete.

| # | Payment | Amount (₹) |
|---|---|---:|
| 1 | Annual maintenance + repair contract to a proprietor | 90,000 |
| 2 | Professional fee to a Chartered Accountant | 28,000 |
| 3 | Rent of office building for the year | 2,60,000 |
| 4 | Purchase of raw material from a resident seller (aggregate) | 75,00,000 |
| 5 | Payment to a contractor who is also asked to render technical services (composite bill) | 1,20,000 |

**Answer:**
1. **194C** (contract): rate 1% (individual/HUF) as single bill ₹90,000 ≥ ₹30,000 single-payment limit ⇒ TDS ₹900. *Selection*: repair/maintenance is "work", not "professional service", so 194C not 194J.
2. **194J** (professional): threshold ₹30,000; ₹28,000 < 30,000 ⇒ **no TDS**. Trap: the ₹30,000 limit under 194J is head-wise per year, not aggregated with 194C.
3. **194-I** (rent, building): threshold ₹2,40,000; 2,60,000 exceeds ⇒ 10% ⇒ ₹26,000. *Selection*: use of premises is 194-I, not 194C.
4. **194Q** (purchase of goods): buyer turnover > ₹10 cr, purchase > ₹50 lakh ⇒ 0.1% on (75,00,000 − 50,00,000) = ₹2,500. *Selection*: 194Q (buyer's obligation) prevails over 206C(1H) (seller's TCS) when both could apply.
5. **194J** on the technical-service component; if the bill is genuinely composite and inseparable, deduct at the **higher** rate. Advise splitting the invoice so 194C (1%) applies to labour/work and 194J (10%) only to technical fees — else the whole ₹1,20,000 risks 194J.

**Why this way (the reasoning):** TDS is a *characterisation* exercise, not a rate lookup — the same rupee is 1% or 10% depending on whether it buys "work", "use of property", or "skill". 194C covers doing a job to specification (repairs, AMC); 194J covers rendering professional/technical *expertise*; 194-I covers *occupying* an asset. Where a buyer with turnover > ₹10 cr and a seller both cross their thresholds, the statute resolves the clash by making **194Q override 206C(1H)** so tax is collected once, at source, by the party the law trusts more (the buyer with books). The composite-bill trap exists because vague invoicing lets parties arbitrage rates; the safe answer is to segregate, and absent segregation, the higher rate protects revenue.

*(Full-marks tip: state threshold AND rate AND the *reason for choosing* the section over its competitor. Merely naming "194C" without resolving the 194C-vs-194J or 194Q-vs-206C(1H) clash caps you at half marks.)*

---

### Q56. Ch: Return Filing & Assessment — Validity of best-judgment assessment (Marks: 6) [Case/Application]
**Question:** Mr. Dev filed his return for AY 2024-25 declaring ₹9,00,000. The AO issued a notice u/s 143(2), and later a notice u/s 142(1) requiring production of books; Mr. Dev did not comply on two occasions. The AO passed an assessment u/s 144 estimating income at ₹18,00,000 **without giving a show-cause opportunity** and without confronting Mr. Dev with the material relied upon. Examine the validity of the assessment.

**Answer:** **Governing law — Sec 144:** where an assessee fails to comply with a 142(1)/143(2) notice or a special-audit direction, the AO *may* make a best-judgment assessment. But the first proviso to Sec 144(1) mandates that a **show-cause notice** be given before completing the assessment (except where a 142(1) notice was already issued). Best judgment must be *bona fide*, based on relevant material and a rational estimate — not vindictive or arbitrary (principle of *Kachwala Gems* / natural justice).

**Application:** Non-compliance on two occasions validly *triggers* 144. However, the AO (i) failed to confront Mr. Dev with the material used to double the income, breaching audi alteram partem, and (ii) an estimate leaping from ₹9,00,000 to ₹18,00,000 with no disclosed basis is arbitrary. The trigger was lawful; the *manner* was not.

**Conclusion/Advice:** The assessment is procedurally defective and liable to be set aside in appeal (CIT(A)) for violation of natural justice, though the matter may be remanded for fresh assessment rather than annulled, since 144 itself was rightly invoked.

**Why this way (the reasoning):** Best-judgment assessment is a *power coupled with a duty of fairness*, not a licence to punish. The law lets the AO estimate precisely because the assessee withheld cooperation — but "best judgment" means an honest estimate anchored to material (comparable cases, GP ratios, bank data), disclosed to the assessee so he can rebut it. Separate the two questions students conflate: *Was 144 correctly invoked?* (yes — non-compliance) and *Was it correctly conducted?* (no — no opportunity, no rational basis). A defect in the second does not un-trigger the first, which is why the remedy is usually remand, not annulment.

*(Full-marks tip: examiners want the split verdict — trigger valid, procedure invalid — plus the natural-justice principle and the likely relief (set aside/remand). A flat "invalid" or "valid" without this nuance loses marks.)*

---

### Q57. Ch: Computation of Total Income — Set-off & carry-forward across heads (Marks: 8) [Problem]
**Question:** For PY 2024-25 Mr. Farid reports: business (non-speculative) profit ₹5,00,000; speculation loss ₹60,000; loss from house property ₹3,20,000; STCG u/s 111A ₹90,000; STCL (other) ₹50,000; LTCG u/s 112A ₹1,50,000; interest income ₹1,00,000. Compute GTI and state losses carried forward, choosing the tax-optimal set-off.

**Solution:**

**WN-1 — Intra-head capital gains:** STCL ₹50,000 may be set against STCG or LTCG. Set against **STCG 111A** (20%) rather than LTCG 112A (12.5%) to save more tax ⇒ STCG net = 90,000 − 50,000 = 40,000; LTCG stays 1,50,000.

**WN-2 — House property loss:** set-off against other heads capped at **₹2,00,000** (Sec 71(3A)); apply against business income. Balance 3,20,000 − 2,00,000 = **1,20,000 c/f** (up to 8 yrs).

**WN-3 — Speculation loss ₹60,000:** set off only against speculative income; none this year ⇒ **c/f ₹60,000** (4 yrs).

| Statement of GTI — Mr. Farid | ₹ |
|---|---:|
| Business income 5,00,000 − HP loss set-off 2,00,000 | 3,00,000 |
| Capital gains: STCG (WN-1) 40,000 + LTCG 1,50,000 | 1,90,000 |
| Other sources | 1,00,000 |
| **Gross Total Income** | **5,90,000** |

Carried forward: HP loss ₹1,20,000; speculation loss ₹60,000.

**Answer:** GTI = **₹5,90,000**; c/f — house-property loss ₹1,20,000, speculation loss ₹60,000.

**Why this way (the reasoning):** Set-off is a sequence of nested rules, and the *order and choice* change the tax bill. Speculation loss is ring-fenced (Sec 73) — it may touch only speculative profit — because the legislature treats speculation as a distinct, riskier activity that should not shelter ordinary income. House-property loss set-off against other heads is capped at ₹2,00,000 (Sec 71(3A)) to curb high-interest "loss-generating" property used to wipe out salary/business income; the untapped ₹1,20,000 is not lost but carried forward against future *house-property* income only. The subtle optimisation is STCL routing: since STCL can be set against either STCG or LTCG, direct it at the *higher-taxed* gain (STCG @20%) to maximise tax saved — setting it against 112A LTCG (12.5%) wastes relief.

*(Full-marks tip: the marks live in (a) the ₹2,00,000 HP cap with correct c/f, (b) ring-fencing speculation loss, and (c) justifying STCL-against-STCG for tax optimisation. Merely netting everything loses the reasoning marks.)*

---

### Q58. Ch: Return Filing & Assessment — Interest u/s 234A on belated return (Marks: 6) [Problem]
**Question:** Mr. Gopal, an individual (non-audit), was due to file his AY 2025-26 return by 31 July 2025 but filed on 18 December 2025. Tax on total income (incl. cess) ₹2,40,000; TDS ₹40,000; advance tax paid ₹90,000; self-assessment tax ₹1,10,000 paid on 18 Dec 2025. Compute interest u/s 234A and state the late-filing fee u/s 234F.

**Solution:**

**WN-1 — 234A base:** Tax on total income − TDS − advance tax = 2,40,000 − 40,000 − 90,000 = **₹1,10,000**.

**WN-2 — Period:** from **1 Aug 2025** (day after due date) to 18 Dec 2025 = Aug, Sep, Oct, Nov, Dec = **5 months** (part of a month counts as full).

**WN-3 — Interest:** 1,10,000 × 1% × 5 = **₹5,500**.

**WN-4 — Sec 234F fee:** return filed after due date ⇒ **₹5,000** (₹1,000 only if total income ≤ ₹5,00,000).

| Statement | ₹ |
|---|---:|
| Interest u/s 234A (5 months) | 5,500 |
| Late-filing fee u/s 234F | 5,000 |
| **Total additional payable** | **10,500** |

**Answer:** 234A interest = **₹5,500**; 234F fee = **₹5,000**.

**Why this way (the reasoning):** 234A is compensation for *delay in filing*, distinct from 234B (default in payment). It runs on the *unpaid* tax net of TDS and advance tax, because the exchequer is compensated only for the money it was actually kept out of. Note the trap: even though the self-assessment tax was paid on 18 Dec, 234A still charges up to the *date of furnishing the return* — paying the tax early does not stop 234A if the return itself is late; only actual filing stops the clock. Part of a month is treated as a whole month, so a filing on the 18th counts December fully. 234F is a flat statutory *fee* (not interest, not deductible), a fixed deterrent scaled down for small taxpayers to keep the penalty proportionate.

*(Full-marks tip: count months from 1 August, and treat any part-month as full — students frequently compute 4 months. State 234F separately; it is a fee, not interest, and does not vary with the tax amount.)*

---

### Q59. Ch: Advance Tax / TDS / TCS — TCS vs TDS on sale of goods (Marks: 5) [Case/Application]
**Question:** Seller S Ltd (turnover ₹12 crore in FY 2023-24) sells goods to buyer B Ltd (turnover ₹15 crore in FY 2023-24). During FY 2024-25 sales to B aggregate ₹90 lakh (all received). Both cross their thresholds. Determine who must deduct/collect, under which section, and the amount. Also state the position if B's turnover were only ₹6 crore.

**Answer:** **Governing provisions:** Sec 206C(1H) casts **TCS** on a seller (turnover > ₹10 cr) collecting from a buyer where receipts exceed ₹50 lakh; Sec 194Q casts **TDS** on a buyer (turnover > ₹10 cr) on purchases exceeding ₹50 lakh. The second proviso to 206C(1H) resolves the overlap: **if 194Q applies, 206C(1H) does not** — the buyer's TDS prevails.

**Application (B turnover ₹15 cr):** B (buyer) turnover > ₹10 cr and purchases ₹90 lakh > ₹50 lakh ⇒ **194Q applies to B**. Therefore S does NOT collect TCS. B deducts 0.1% on (90,00,000 − 50,00,000) = **₹4,000**.

**If B's turnover were ₹6 cr:** 194Q does not apply (buyer below ₹10 cr). Then **206C(1H) revives** — S collects TCS 0.1% on (90,00,000 − 50,00,000) = **₹4,000**.

**Why this way (the reasoning):** Both sections chase the *same* transaction, so the law needs a tie-breaker to avoid double collection on one sale — it hard-wires **194Q priority** so tax is taken once, by the buyer (who has the deductible payment in hand and better books). The ₹50 lakh is a *cumulative* threshold per counterparty per year, and TDS/TCS bites only on the *excess* over ₹50 lakh, not the whole ₹90 lakh — because the levy is a light-touch information tool, not a tax on the full turnover. When the buyer falls below ₹10 cr, the tie-breaker has nothing to disable, so the seller's TCS obligation automatically re-emerges — the two provisions are designed to be mutually exclusive, never simultaneous.

*(Full-marks tip: the examiner tests the override rule and the "excess over ₹50 lakh" base. Applying the rate to the full ₹90 lakh, or charging both TDS and TCS, are the killer errors.)*

---

### Q60. Ch: Deductions under Chapter VI-A — NPS 80CCD interplay with the ₹1.5L ceiling (Marks: 6) [Problem]
**Question:** Mr. Harish (old regime, private-sector employee) for PY 2024-25: Basic + DA (in terms) ₹8,00,000. Contributions — own PF ₹90,000; PPF ₹60,000; LIC premium ₹40,000; own NPS (Tier-I) ₹70,000; **employer** NPS contribution ₹96,000. Compute the total deduction available under Sections 80C, 80CCD(1), 80CCD(1B) and 80CCD(2), showing the ceiling logic.

**Solution:**

**WN-1 — 80CCE aggregate cap:** 80C + 80CCC + 80CCD(1) together cannot exceed **₹1,50,000**.
- 80C items: PF 90,000 + PPF 60,000 + LIC 40,000 = 1,90,000.
- 80CCD(1) (own NPS) is capped at 10% of salary = 80,000; actual 70,000. But the *combined* cap is ₹1,50,000.

**WN-2 — Optimal allocation:** Route ₹50,000 of NPS into **80CCD(1B)** first (over-and-above ₹1.5L, exclusive slot). Remaining NPS = 70,000 − 50,000 = 20,000 falls under 80CCD(1).
- 80C: 1,90,000 → restricted, but combined with 80CCD(1) 20,000 must fit ₹1,50,000.
- Fill ₹1,50,000 with 80C items (1,90,000 available) ⇒ 80C = 1,50,000; 80CCD(1) 20,000 then exceeds cap ⇒ effectively subsumed/nil extra.

**WN-3 — 80CCD(2) — employer NPS:** deductible separately, **outside** the ₹1.5L cap, up to 10% of salary = 10% × 8,00,000 = 80,000. Employer paid 96,000 ⇒ deduction **₹80,000**.

| Statement of deduction | ₹ |
|---|---:|
| 80C (restricted, within ₹1.5L pool) | 1,50,000 |
| 80CCD(1B) — additional NPS (exclusive) | 50,000 |
| 80CCD(2) — employer NPS (10% of salary) | 80,000 |
| **Total Chapter VI-A (these sections)** | **2,80,000** |

**Answer:** Total deduction = **₹2,80,000**.

**Why this way (the reasoning):** Three NPS slots stack in a deliberate hierarchy, and the *routing* decides how much relief survives the ₹1.5L wall. 80C/80CCC/80CCD(1) share one ₹1,50,000 ceiling (Sec 80CCE) — so when 80C alone already exceeds it, pushing own-NPS into 80CCD(1) buys *nothing extra*. The smart move is to divert ₹50,000 of the NPS into **80CCD(1B)**, a stand-alone slot *outside* the ₹1.5L cap, converting otherwise-wasted contribution into real deduction. 80CCD(2) (employer's share) sits entirely outside 80CCE and is capped at 10% of salary — the excess ₹16,000 the employer paid is simply not deductible. The lesson: identical rupees yield different tax outcomes purely by which sub-section you park them in.

*(Full-marks tip: examiners reward showing that 80CCD(1B)'s ₹50,000 is *over and above* ₹1.5L and that 80CCD(2) is capped at 10% of salary, not the amount paid. Dumping all NPS into 80CCD(1) — wasting the exclusive slot — is the common failure.)*

---

### Q61. Ch: Return Filing & Assessment — Updated return u/s 139(8A) eligibility (Marks: 5) [Case/Application]
**Question:** For AY 2023-24, Mr. Iqbal did not file any return. In March 2026 he wishes to file an **updated return** u/s 139(8A) declaring additional income of ₹4,00,000. Examine (a) whether he can, (b) the additional tax payable, and (c) three situations in which an updated return is barred.

**Answer:** **Governing law — Sec 139(8A):** any person may furnish an updated return within **24 months from the end of the relevant assessment year**, whether or not he filed an original/belated/revised return, provided it does not reduce tax, show/increase a loss, or increase a refund.

**Application:** AY 2023-24 ends 31 Mar 2024; 24 months ⇒ up to **31 Mar 2026**. Filing in March 2026 is within time and increases income ⇒ **permissible**.

**Additional tax (Sec 140B):** since filed in the **second** 12-month window, additional tax = **50%** of (tax + interest) due on the additional income (25% if filed within the first 12 months).

**Barred situations (any three):** (i) it is a return of loss / would reduce total income; (ii) it decreases tax liability or increases refund of an earlier return; (iii) a search u/s 132 / survey u/s 133A (other than 133A(2A)) has been initiated; (iv) assessment/reassessment/revision is pending or completed for that year; (v) already filed an updated return for that year.

**Why this way (the reasoning):** Sec 139(8A) is a *voluntary compliance amnesty* — it lets a taxpayer come clean and pay a *premium* (25%/50% extra) rather than face penalty and prosecution, so the design deliberately permits it only when the exchequer *gains* (more income, more tax). Hence every bar exists to stop misuse: you cannot use it to claim a loss or a refund (that would cost revenue), and you cannot use it to pre-empt an investigation already underway (that would defeat enforcement). The escalating 25%→50% additional tax rewards earlier disclosure — the longer you wait, the higher the price — mirroring the interest-like logic of encouraging prompt correction.

*(Full-marks tip: nail the 24-month window with the correct end date, the 25%/50% distinction by sub-window, and at least three bars. Confusing 139(8A) with belated 139(4) — which had a shorter, now-elapsed window — is the trap.)*

---

### Q62. Ch: Advance Tax / TDS / TCS — Liability & installment computation (Marks: 8) [Problem]
**Question:** Mr. Jacob (aged 62, resident) estimates for PY 2024-25: business income ₹7,50,000, interest ₹1,50,000, LTCG on land sold on 10 Nov 2024 ₹4,00,000. TDS deducted ₹20,000. He opts old regime. Determine (a) whether he is liable to advance tax, (b) each installment amount and due date, given the capital gain arose only in November.

**Solution:**

**WN-1 — Estimated tax:** Total income = 7,50,000 + 1,50,000 + 4,00,000 = 13,00,000. Normal income 9,00,000; LTCG 4,00,000 @20% (with indexation) = 80,000. Tax on 9,00,000 (old): 12,500 + 80,000 = 92,500. Total = 92,500 + 80,000 = 1,72,500 + 4% cess = **₹1,79,400**. Less TDS 20,000 = **₹1,59,400** advance-tax liability (> ₹10,000 ⇒ liable; senior-citizen exemption from advance tax applies only if **no business income** — he has business income, so **not exempt**).

**WN-2 — Installments (assessed tax ₹1,59,400, rounded working ₹1,59,400):**

| Due date | Cumulative % | Amount payable (cumulative) |
|---|---:|---:|
| 15 Jun | 15% | 23,910 |
| 15 Sep | 45% | 71,730 |
| 15 Dec | 75% | 1,19,550 |
| 15 Mar | 100% | 1,59,400 |

**WN-3 — Capital-gains relief:** the LTCG arose on 10 Nov 2024, *after* the first two due dates. Proviso to Sec 234C: tax on such capital gain is payable in the *remaining* installments (or by 15 Mar / 31 Mar). So the June and September installments are computed **excluding** the ₹80,000 LTCG tax; the LTCG tax is loaded into the December and March installments, with no 234C default for the earlier under-payment attributable to it.

**Answer:** He **is liable** (business income defeats the senior-citizen exemption); installments as above, with the LTCG tax of ₹80,000 spread only over the Dec/Mar installments free of 234C.

**Why this way (the reasoning):** Two design principles drive this. First, the senior-citizen advance-tax exemption (Sec 207) is a *hardship relief* for pensioners with only passive income — it is withdrawn the moment there is business income, because a businessman can reasonably estimate and pay. Second, advance tax demands you pay *as you earn*, but capital gains are lumpy and unforeseeable — you cannot pre-pay in June tax on a sale you make in November. So the proviso to 234C shifts the tax on a late-arising capital gain into the installments falling *after* it accrues, sparing the taxpayer interest for a shortfall he could not have avoided. Ignoring this relief and charging 234C from June would penalise foresight the law does not demand.

*(Full-marks tip: state the senior-citizen exemption AND why it is lost, and apply the 234C capital-gains proviso (spread the gain's tax to post-event installments). Charging the whole liability from 15 June loses both concept marks.)*

---

### Q63. Ch: Advance Tax / TDS / TCS — Multi-payment TDS computation (Marks: 8) [Problem]
**Question:** XYZ Ltd made the following payments in FY 2024-25. Compute the TDS on each with section and rate; PANs are available unless stated.

| # | Payee / nature | Amount (₹) |
|---|---|---:|
| 1 | Salary to an employee (estimated tax on salary ₹90,000 for the year) | — |
| 2 | Interest on a loan to a resident, no PAN furnished | 1,00,000 |
| 3 | Fees for technical services to a resident firm | 2,00,000 |
| 4 | Commission to an agent | 22,000 |
| 5 | Payment to a foreign company for royalty (no DTAA relief) | 5,00,000 |

**Solution:**

**WN-1 — Salary (Sec 192):** deduct the *average* rate of income tax on estimated salary. TDS = estimated annual tax ₹90,000 spread over 12 months ⇒ ₹7,500 p.m.; there is **no threshold**, tax is the estimated liability itself.

**WN-2 — Interest, no PAN (Sec 194A r/w 206AA):** normal rate 10%, but absent PAN the rate is the higher of the specified rate or **20%** ⇒ 20% × 1,00,000 = **₹20,000**.

**WN-3 — FTS (Sec 194J):** technical services rate **2%** (professional 10%); 2% × 2,00,000 = **₹4,000**.

**WN-4 — Commission (Sec 194H):** threshold ₹15,000; 22,000 > 15,000 ⇒ 2% (post-Oct 2024 rate) × 22,000 = **₹440** (5% if before the rate change — state assumption).

**WN-5 — Royalty to foreign company (Sec 195):** TDS at rates in force on the gross sum; royalty to a non-resident ⇒ 20% (plus surcharge/cess as applicable) × 5,00,000 = **₹1,00,000** (before surcharge/cess).

| Statement of TDS | Section | ₹ |
|---|---|---:|
| Salary (average rate) | 192 | 90,000 (year) |
| Interest — no PAN | 194A/206AA | 20,000 |
| FTS | 194J | 4,000 |
| Commission | 194H | 440 |
| Royalty (non-resident) | 195 | 1,00,000 |

**Answer:** TDS as tabulated — the no-PAN 20% and the 194J technical-services 2% are the decisive judgment calls.

**Why this way (the reasoning):** Each section answers a different question. Salary (192) is unique — it has *no threshold* and uses the *average rate* on the whole year's estimated liability, because the employer stands in for the taxpayer's own tax, not a flat deduction. 206AA is an anti-avoidance override: a payee who hides his PAN forfeits the benefit of concessional rates and suffers a punitive 20% floor, because without a PAN the department cannot give him credit anyway. 194J deliberately splits into 2% (technical) and 10% (professional) because technical services have lower value-add margins than professional expertise. Section 195 is broadest — it applies to *any* sum chargeable to a non-resident and requires a view on chargeability and treaty relief before deducting, which is why it demands the most judgment.

*(Full-marks tip: the marks concentrate on the 206AA 20% no-PAN rule, the 194J 2% technical-services rate, and 192's average-rate/no-threshold mechanism. Applying 10% flat to salary or FTS shows conceptual gaps.)*

---

### Q64. Ch: Computation of Total Income — Clubbing, deemed income & set-off (Marks: 10) [Problem]
**Question:** Mr. Kiran (resident, old regime), PY 2024-25:

| Particulars | Amount (₹) |
|---|---:|
| Salary income (computed) | 9,20,000 |
| Interest on FDs held in the name of his minor son (from gift by grandfather) | 1,60,000 |
| Minor son's income from a manual talent (dance shows) | 45,000 |
| Cash gift received on 20 Aug 2024 from a friend | 80,000 |
| Gift of a plot (SDV ₹6,00,000) received from friend for ₹2,00,000 | — |
| Loss from a let-out house property | (2,60,000) |
| 80C ₹1,50,000; 80D (self, <60) ₹22,000 | — |

Compute total income with a note for each adjustment.

**Solution:**

**WN-1 — Minor's income (Sec 64(1A)):** FD interest ₹1,60,000 is clubbed (income from investment, not skill). Manual-talent income ₹45,000 is **NOT** clubbed (earned by minor's own skill). Exemption Sec 10(32): ₹1,500 per minor from the clubbed income ⇒ clubbed = 1,60,000 − 1,500 = **₹1,58,500**.

**WN-2 — Cash gift ₹80,000 (Sec 56(2)(x)):** from a non-relative, exceeds ₹50,000 ⇒ **whole ₹80,000** taxable (not just the excess).

**WN-3 — Plot for inadequate consideration:** SDV 6,00,000 − consideration 2,00,000 = ₹4,00,000 > ₹50,000 and > 10% of consideration ⇒ **₹4,00,000** taxable u/s 56(2)(x).

**WN-4 — House-property loss:** ₹2,60,000, set-off against other heads capped at **₹2,00,000**; balance **₹60,000 c/f**.

| Statement of Total Income — Mr. Kiran | ₹ |
|---|---:|
| Salaries | 9,20,000 |
| Less: HP loss set-off (capped ₹2,00,000) | (2,00,000) |
| Income from other sources: minor FD (1,58,500) + cash gift (80,000) + plot (4,00,000) | 6,38,500 |
| **Gross Total Income** | **13,58,500** |
| Less: 80C 1,50,000 + 80D 22,000 | (1,72,000) |
| **Total Income** | **11,86,500** |

C/f: house-property loss ₹60,000.

**Answer:** Total Income = **₹11,86,500**; c/f HP loss ₹60,000.

**Why this way (the reasoning):** Clubbing under 64(1A) targets *income-splitting* — parking passive investments in a minor's name to duplicate exemptions — so it clubs investment income but expressly *spares* what the minor earns by his own skill or talent, which is not an avoidance device. The ₹1,500 per-child relief (Sec 10(32)) is a token acknowledgement of the child's separateness. Section 56(2)(x) is a deeming provision plugging the gift route: once the ₹50,000 threshold is *crossed*, the **entire** amount is taxed, not merely the excess — the ₹50,000 is a de minimis switch, not a standard deduction. For property, the "inadequate consideration" limb taxes the SDV shortfall because a below-market purchase is an economic gift dressed as a sale. Finally the ₹2,00,000 house-property set-off cap ensures interest-heavy property cannot obliterate salary tax. Each rule counters a specific avoidance behaviour — that is the unifying logic.

*(Full-marks tip: the four judgment points — skill income NOT clubbed, ₹1,500 relief, *whole* cash gift taxed once threshold crossed, and the ₹2L HP cap — carry the marks. Taxing only the ₹30,000 "excess" of the cash gift is the classic error.)*

---

### Q65. Ch: Deductions under Chapter VI-A — 80D with age, mode & check-up sub-limits (Marks: 5) [Problem]
**Question:** Mr. Lal (aged 58, old regime), PY 2024-25: mediclaim for self & spouse ₹27,000 (paid by cheque); preventive health check-up for self ₹6,000 (paid in cash); mediclaim for his parents, both aged 67, ₹58,000 (cheque); medical expenditure for his father (no insurance for him separately) ₹12,000 (cash). Compute the 80D deduction.

**Solution:**

**WN-1 — Self & family bucket (self <60):** overall cap ₹25,000. Insurance 27,000 (capped) + check-up: preventive check-up allowed up to ₹5,000 *within* the ₹25,000 cap, and cash is permitted **only** for the check-up. Insurance 27,000 already exhausts the ₹25,000 cap ⇒ deduction = **₹25,000** (check-up subsumed).

**WN-2 — Parents bucket (senior citizens, cap ₹50,000):** insurance 58,000 (capped at 50,000). Medical expenditure ₹12,000 is allowed *only if no insurance* is taken for that person — but parents ARE insured, so the ₹12,000 medical expenditure is **not** separately allowed. Deduction = **₹50,000**.

| Statement of 80D | ₹ |
|---|---:|
| Self & family (cap ₹25,000) | 25,000 |
| Parents — senior (cap ₹50,000) | 50,000 |
| **Total 80D** | **75,000** |

**Answer:** 80D deduction = **₹75,000**.

**Why this way (the reasoning):** 80D is built from *buckets with sub-rules*, and each rule reflects a policy. Insurance premiums must be paid by any mode *other than cash* — the state wants a traceable, banked transaction — but the **preventive health check-up** carve-out uniquely allows cash up to ₹5,000, because it is a small, encouraged wellness spend. The check-up ₹5,000 is *within*, not on top of, the ₹25,000/₹50,000 ceiling, so once premiums fill the ceiling the check-up yields nothing. Medical expenditure (in lieu of insurance) is allowed only for a person for whom **no** health insurance exists, because it substitutes for uninsurable very-senior citizens — here the insured parents disqualify the ₹12,000. Reading these as additive rather than capped is the standard over-claim.

*(Full-marks tip: show that the check-up is subsumed once premiums hit the cap, and that medical expenditure is barred when insurance exists. Adding ₹6,000 and ₹12,000 on top of the caps is the mark-losing mistake.)*

---

### Q66. Ch: Return Filing & Assessment — Belated vs revised vs updated return (Marks: 6) [Case/Application]
**Question:** Mrs. Meena filed her AY 2025-26 return on 30 July 2025 (within due date) declaring ₹8,00,000. In October 2025 she discovers she omitted interest income of ₹1,20,000. In January 2026 she realises a further ₹40,000 was also omitted. Advise: (a) can she correct the October error, and how; (b) can she correct the January error; (c) what if the omission were discovered only in September 2027.

**Answer:** **(a) October 2025 — Revised return (Sec 139(5)):** an original return filed within due date may be revised any time before **31 Dec of the AY** (31 Dec 2025) or completion of assessment, whichever is earlier. She files a revised return including the ₹1,20,000 — it *replaces* the original entirely.

**(b) January 2026 — beyond 31 Dec 2025:** Sec 139(5) window has closed. A revised return is no longer possible; the only route is an **updated return u/s 139(8A)**, available up to 24 months from end of AY (31 Mar 2028), on payment of additional tax (25%/50% of tax+interest) — she declares the further ₹40,000 (and the ₹1,20,000 if not already revised).

**(c) September 2027:** revised return impossible; **updated return u/s 139(8A)** applies (within 24 months to 31 Mar 2028), additional tax at **50%** (second 12-month window) of tax and interest on the omitted income.

**Why this way (the reasoning):** The three return types occupy a *timeline*, and picking the wrong one is a live exam trap. A **revised** return (139(5)) is a costless, full replacement — the law encourages honest correction of *bona fide* omissions, but only within a tight window (to 31 Dec of the AY) so the department can still process the year normally. Once that window shuts, correction is still allowed, but only through the **updated** return (139(8A)) and at a *price* (25%/50% premium), because the taxpayer is now correcting late and the state charges for the indulgence and lost time. The escalating premium mirrors the incentive to correct early. A belated return (139(4)) does not arise here because she already filed on time.

*(Full-marks tip: map each date to the right section (139(5) vs 139(8A)) and the correct deadline. Suggesting a "revised return" for the January/September corrections after 31 Dec is the primary error examiners penalise.)*

---

### Q67. Ch: Advance Tax / TDS / TCS — TCS scope, rates & exceptions (Marks: 5) [Case/Application]
**Question:** For FY 2024-25, examine the TCS obligation, section and rate in each case, and state one exception: (i) sale of scrap ₹5,00,000 to a manufacturer who furnishes Form 27C declaration for use in manufacture; (ii) sale of a motor car for ₹12,00,000 to an individual buyer; (iii) remittance of ₹8,00,000 under LRS for overseas education funded by an education loan; (iv) sale of tendu leaves ₹3,00,000.

**Answer:**
(i) **Scrap — Sec 206C(1):** normally TCS @1%. But a buyer who furnishes **Form 27C** declaring the scrap is for *manufacturing/processing* (not trading) is exempt ⇒ **no TCS**.
(ii) **Motor car > ₹10 lakh — Sec 206C(1F):** TCS @1% on ₹12,00,000 = **₹12,000**, collected by the seller regardless of buyer's status.
(iii) **LRS for education via loan — Sec 206C(1G):** the concessional rate of **0.5%** applies on amounts above ₹7 lakh where funded by a loan from a financial institution ⇒ 0.5% × (8,00,000 − 7,00,000) = **₹500**.
(iv) **Tendu leaves — Sec 206C(1):** TCS @**5%** × 3,00,000 = **₹15,000**.

**Why this way (the reasoning):** TCS is an *information-and-collection net* over trades historically prone to under-reporting (scrap, forest produce, liquor, minerals) and over conspicuous consumption (luxury cars, foreign remittance). The Form 27C exception for scrap exists because the levy targets *traders*, not genuine *manufacturers* who consume the material — taxing input consumption would just block credit and distort production. The luxury-car TCS (206C(1F)) needs no threshold on turnover and applies to any buyer because it is aimed at the *transaction's* visibility, not the parties' size. The LRS education carve-out (0.5% above ₹7 lakh when loan-funded) is a social concession — the state does not want TCS to deter students financing study abroad through institutional loans. Different rates simply reflect different perceived leakage risk.

*(Full-marks tip: the Form 27C exception, the 206C(1F) no-threshold luxury-car rule, and the loan-funded LRS 0.5%-above-₹7L concession are the tested nuances. A flat 1% everywhere earns little.)*

---

### Q68. Ch: Computation of Total Income — Integrated computation, advance tax adequacy & 234C (Marks: 10) [Problem]
**Question:** Dr. Nair (resident, aged 50, **new regime u/s 115BAC**), PY 2024-25:

| Particulars | Amount (₹) |
|---|---:|
| Gross professional receipts | 24,00,000 |
| Professional expenses (allowable) | 9,00,000 |
| Interest on savings & FD | 1,20,000 |
| LTCG on debt mutual funds bought in 2019, sold 15 Feb 2025 (STCG in law — post-Apr-2023 rule N/A; treat as LTCG with indexation ₹2,00,000) | 2,00,000 |
| TDS credit (194J on receipts) | 1,50,000 |
| Advance tax: 15 Jun 40,000; 15 Sep 90,000; 15 Dec 60,000; 15 Mar 30,000 | — |

Compute total income, tax, and interest u/s 234C. (Ignore 234B for brevity; the capital gain arose 15 Feb 2025.)

**Solution:**

**WN-1 — Income:** Professional income = 24,00,000 − 9,00,000 = 15,00,000. Other sources 1,20,000 (no 80TTA in new regime). LTCG 2,00,000 @20% (indexed) = 40,000. **Total income = 15,00,000 + 1,20,000 + 2,00,000 = 18,20,000.**

**WN-2 — Tax (new regime AY 2025-26):** Normal income 16,20,000.
0–3L nil; 3–7L @5% = 20,000; 7–10L @10% = 30,000; 10–12L @15% = 30,000; 12–15L @20% = 60,000; above 15L @30% on (16,20,000 − 15,00,000) = 1,20,000 × 30% = 36,000. Normal tax = 20,000 + 30,000 + 30,000 + 60,000 + 36,000 = **1,76,000**.
LTCG tax = 2,00,000 × 20% = **40,000**. Total = 2,16,000 + 4% cess = **₹2,24,640**.

**WN-3 — Net liability & advance-tax base:** 2,24,640 − 1,50,000 (TDS) = **₹74,640** (assessed tax for 234C ≈ ₹74,640).

**WN-4 — 234C** (capital-gains tax ₹40,000 arose 15 Feb 2025 ⇒ excluded from Jun/Sep/Dec thresholds; only March gate captures it). Non-CG assessed tax = 74,640 − 40,000 = ₹34,640 for the first three gates.

| Due date | Base | Required | Cumulative paid | Short | Interest |
|---|---|---:|---:|---:|---:|
| 15 Jun | 34,640 | 12% = 4,157 | 40,000 | Nil | Nil |
| 15 Sep | 34,640 | 36% = 12,470 | 1,30,000 | Nil | Nil |
| 15 Dec | 34,640 | 75% = 25,980 | 1,90,000 | Nil | Nil |
| 15 Mar | 74,640 | 100% = 74,640 | 2,20,000 | Nil | Nil |

Cumulative advance tax ₹2,20,000 (incl. TDS 1,50,000 counts toward payment? No — TDS is separate; advance tax paid = 40,000+90,000+60,000+30,000 = ₹2,20,000, already exceeding ₹74,640 net). **234C = Nil.**

**Answer:** Total income = **₹18,20,000**; tax = **₹2,24,640**; interest u/s 234C = **Nil** (advance tax ₹2,20,000 comfortably exceeds each gate on the ₹74,640 net liability).

**Why this way (the reasoning):** This integrates three ideas that CA-Inter loves to fuse. First, regime choice drives the *arithmetic*: under 115BAC Chapter VI-A relief (80C/80D/80TTA) is *unavailable*, so the interest income is fully taxed and the slab structure is the wider new-regime grid — a student who mechanically claims 80TTA here is wrong. Second, special-rate LTCG is carved out of the slab computation and taxed at 20% separately, exactly as in the head-wise discipline. Third, 234C is tested on the *net* assessed tax (after TDS), and the capital-gains proviso keeps the Feb-2025 gain out of the June/Sep/Dec gates — but here it is academic because his advance tax already dwarfs the liability, so *no* interest arises. The takeaway: always compute the *net* base and check each installment against it; large early payments can extinguish 234C entirely even when income is lumpy.

*(Full-marks tip: two decisive points — deny Chapter VI-A relief under the new regime, and compute 234C on net-of-TDS assessed tax with the CG proviso. Concluding "234C payable" without checking that advance tax already exceeds the net liability is the trap.)*

### Q69. Ch: GST – Supply — Scope of Supply & Schedule I (Marks: 8) [Case/Application]
**Question:** Examine, with reasons, whether the following independent transactions constitute a "supply" liable to GST, and if so on what value/consideration basis. Comment on the validity of the assessee's stand in each.

| # | Transaction (FY 2025-26) | Assessee's claim |
|---|---|---|
| (i) | Ganesh Ltd. permanently transfers a machine (on which it had availed ITC of ₹1,80,000) to its wholly-owned subsidiary free of cost | "No consideration, hence no supply" |
| (ii) | Head Office in Maharashtra provides internal accounting services (no invoice raised) to its own branch (separate GSTIN) in Karnataka | "Same legal entity, self-service, not a supply" |
| (iii) | A dealer gives a laptop to an unrelated customer free of charge on purchase of goods worth ₹2,00,000 ("buy goods, get laptop free"). ITC was availed on the laptop | "Gift to customer, not a supply" |
| (iv) | Mr. A, an employee, gifts worth ₹80,000 in the year received from his employer under the employment contract | "Perquisite, not a supply" |

**Answer:**
**Governing law:** Section 7(1)(a) CGST Act makes "supply" turn on *consideration in the course/furtherance of business*, BUT Section 7(1)(c) read with **Schedule I** deems **four categories of transactions as supply even WITHOUT consideration**. Section 25(4) treats distinct GSTIN establishments as *distinct persons*; Explanation to Sec 15 treats subsidiary/holding as *related persons*.

- **(i) Taxable supply.** Schedule I, Entry 1: "Permanent transfer/disposal of *business assets where ITC has been availed*" is a supply even without consideration. ITC of ₹1,80,000 was availed, so the free transfer to the subsidiary is a deemed supply. The claim of "no consideration" fails. Value = open market value under Rule 27/28 (related persons). **Assessee's stand invalid.**
- **(ii) Taxable supply.** Schedule I, Entry 2: supply of services between *distinct persons* (Sec 25(4)) in the course of business, even without consideration, is a supply. HO (MH) and branch (KA) hold different GSTINs → distinct persons. Internal accounting service is a deemed inter-State supply, IGST payable on open market value (Rule 28); the recipient branch takes full ITC (revenue-neutral), but the invoice/tax obligation stands. **Stand invalid.**
- **(iii) Taxable supply — but via ITC reversal, not outward tax on the gift.** The customer is *unrelated*, so Schedule I Entry 2 (related/distinct persons) does NOT apply, and there is no consideration → not a supply of the laptop *per se*. However, the "free" laptop is really part of a composite scheme; the ₹2,00,000 is a *single price for goods + laptop* → it is a **composite/mixed bundling** issue, and independently Sec 17(5)(h) blocks ITC on "goods disposed of by way of gift/free sample." The dealer must **reverse the ITC availed on the laptop**. The claim "not a supply" is technically correct on outward tax, but the ITC he availed is not allowed. **Stand partly wrong (ITC reversal required).**
- **(iv) Not a supply.** Schedule III, Entry 1: services by an employee to employer *in the course of employment* are neither supply of goods nor services; and Schedule I Entry 2 proviso specifically excludes **gifts up to ₹50,000 by employer to employee**. Here the gift is ₹80,000 — the **amount exceeding ₹50,000, i.e. ₹30,000, becomes a supply** by the *employer* (not by the employee). So the employee's receipt is not his supply, but the employer is liable on ₹30,000. **Employee's stand valid; employer has a liability.**

**Conclusion:** (i) and (ii) are deemed supplies under Schedule I; (iii) triggers ITC reversal not outward tax; (iv) is exempt for the employee but taxable in the employer's hands beyond ₹50,000.

**Why this way (the reasoning):** The whole trap here is the instinct that "no money changed hands = no GST." GST's charging net is wider than a normal sale because Schedule I *deems* four consideration-free transactions to be supplies — the policy logic is anti-avoidance: if ITC has already been availed on an asset (Entry 1) or if you could shift value costlessly between your own GSTINs or related parties (Entry 2), allowing a tax-free exit would leak input credit already claimed and distort the credit chain. That is why ITC-availment is the hinge in (i), and "distinct person" status in (ii). Conversely the ₹50,000 employer-gift threshold in (iv) exists to keep ordinary employment perquisites out of GST while catching disguised value transfers above a de-minimis line — and critically the tax sits on the *employer*, because the employee's own service is carved out by Schedule III. Students who answer (iii) as "taxable outward supply" miss that an unrelated free item without consideration is genuinely outside Sec 7, and the correct lever is the *blocked-credit* rule 17(5)(h), not an output charge.

*(Full-marks tip: the examiner rewards naming the exact Schedule/Entry AND the anti-avoidance rationale; the classic deduction is treating the "free laptop" as an output supply instead of an ITC reversal, and forgetting that in (iv) the liability shifts to the employer only on the excess over ₹50,000.)*

---

### Q70. Ch: GST – Supply — Schedule II & Schedule III boundary (Marks: 6) [Case/Application]
**Question:** For each item, state whether it is (a) supply of goods, (b) supply of services, or (c) neither (Schedule III), with the governing entry, and comment on the assessee's classification.

| # | Facts | Assessee treated as |
|---|---|---|
| (i) | Transfer of title in goods under an agreement where property passes on future date on payment of last instalment (hire purchase) | Service |
| (ii) | Renting of a commercial building | Goods |
| (iii) | Sale of a plot of land (developed, with drainage/roads) | Taxable service (works contract) |
| (iv) | Job-work: treatment/process applied to another person's goods | Goods |
| (v) | Sale of a running business as a going concern | Taxable supply of goods |
| (vi) | High-sea sale of imported goods before clearance for home consumption | Taxable supply |

**Answer:**
- **(i) Supply of GOODS.** Schedule II, Para 1(c): where goods are transferred under an agreement that *property will pass at a future date upon full payment*, it is a supply of **goods**. Hire-purchase = supply of goods (not service). **Claim wrong.**
- **(ii) Supply of SERVICES.** Schedule II, Para 2(b): any lease/tenancy/licence to occupy land, and Para 5(a) renting of immovable property, is a **service**. **Claim wrong.**
- **(iii) Neither — outside GST.** Schedule III, Entry 5: *sale of land* is neither goods nor service. Mere development (roads/drainage) does not convert a land sale into a works contract as long as what is transferred is the *plot* (title in land). **Claim wrong.**
- **(iv) Supply of SERVICES.** Schedule II, Para 3: any *treatment or process* applied to another person's goods is a **service** (job-work). **Claim wrong.**
- **(v) Neither / Exempt.** Transfer of a *going concern* as a whole is treated as supply of service but is **exempt** (Notification 12/2017, entry for "services by way of transfer of a going concern as a whole"). It is not a taxable supply of goods. **Claim wrong.**
- **(vi) Neither — Schedule III Entry 8(b).** Supply of goods by the consignee *by endorsement of documents of title before clearance for home consumption* (high-sea sales) is neither goods nor service. **Claim wrong.**

**Conclusion:** Correct classification — (i) goods; (ii) service; (iii) neither; (iv) service; (v) exempt service; (vi) neither.

**Why this way (the reasoning):** Schedule II exists solely to *resolve the goods-vs-service character* of borderline transactions where the same economic act could look like either — its function is classification, NOT to create a charge. So hire-purchase is called "goods" because the essence is an eventual transfer of *title*, whereas leasing/renting is "service" because only the *right to use/occupy* passes, not ownership. Schedule III does something different — it lists transactions Parliament chose to keep *entirely outside* GST (land, completed buildings, actionable claims, employment, high-sea sales) either because they fall in the States' domain (land/immovable property) or to avoid double taxation (high-sea sales are taxed at import). The trap in (iii) and (v) is over-classifying: developed land is *still land*, and a going concern is a policy-exempted service, not a taxable sale of each asset. Understanding *why* each Schedule exists — II to classify, III to exclude — lets you place any novel transaction correctly instead of memorising a list.

*(Full-marks tip: quote the Para/Entry number; the frequent deduction is calling a developed-plot sale a "works contract" and taxing a going-concern transfer — both are exam traps testing whether you know Schedule III and the going-concern exemption.)*

---

### Q71. Ch: GST – Supply — Composite vs Mixed Supply (rate determination) (Marks: 8) [Problem]
**Question:** Trendy Home Ltd. makes the following supplies in a single tax invoice. Determine, for each package, whether it is a *composite* or *mixed* supply, the applicable GST rate, and compute the total GST payable. Applicable rates: bedsheet 5%, pillow 12%, mattress 18%, transportation service 18%, chocolates 18%, dry fruits 12%, aerated drink 28%, canned juice 12%, decorative basket 12%.

| Package | Contents & price (₹, exclusive of GST) | Nature of pricing |
|---|---|---|
| A | Mattress ₹20,000 + delivery & installation ₹2,000, sold for a **single price ₹22,000** | Naturally bundled, single price |
| B | Diwali hamper: chocolates ₹1,500 + dry fruits ₹2,000 + aerated drink ₹500 + decorative basket ₹1,000, **single price ₹5,000** | Bundled, single price |
| C | Bedsheet ₹1,000 + pillow ₹600 + mattress ₹8,000, **separately priced** on the invoice | Each item separately priced |

**Solution:**
**WN-1 — Test (Sec 2(30) & 2(74)):** A **composite** supply = two or more *naturally bundled* supplies with one *principal* supply → taxed at the **principal supply's rate**. A **mixed** supply = two or more supplies for a *single price* that are *not naturally bundled* → taxed at the **highest rate** among the items. Where items are *separately priced*, each is taxed at its **own rate** (neither composite nor mixed).

**WN-2 — Package A (Composite):** Mattress + delivery/installation are naturally bundled in the ordinary course; the mattress is the principal supply. → Composite → whole ₹22,000 @ **18%** (mattress rate).
GST = 22,000 × 18% = **₹3,960.**

**WN-3 — Package B (Mixed):** Chocolates, dry fruits, drink and basket are *not* naturally bundled (each can be supplied independently) but sold for one price → **Mixed supply** → highest rate = aerated drink **28%**.
GST = 5,000 × 28% = **₹1,400.**

**WN-4 — Package C (Separately priced):** Items individually priced → each taxed at its own rate (not a single-price bundle).
Bedsheet 1,000 × 5% = 50; Pillow 600 × 12% = 72; Mattress 8,000 × 18% = 1,440.
GST = 50 + 72 + 1,440 = **₹1,562.**

**Statement Showing GST Payable — Trendy Home Ltd.**

| Package | Nature | Value (₹) | Rate applied | GST (₹) |
|---|---|---|---|---|
| A | Composite (principal = mattress) | 22,000 | 18% | 3,960 |
| B | Mixed | 5,000 | 28% (highest) | 1,400 |
| C | Separate items | 9,600 | own rates | 1,562 |
| **Total** | | **36,600** | | **6,922** |

**Answer:** Total GST payable = **₹6,922** (A ₹3,960 composite @18%; B ₹1,400 mixed @28%; C ₹1,562 at individual rates).

**Why this way (the reasoning):** The composite/mixed distinction exists to answer one practical question — *when several things go out under one deal, which single rate governs?* The law's logic is intent-based: if the bundle is how the item is *naturally* sold (you can't sensibly buy a mattress without delivery), the tax should follow the dominant, principal supply — otherwise splitting artificial "services" out of a product would let sellers rate-shop. Hence composite → principal rate. But if unrelated things are jammed together only to quote one price (a hamper of chocolate, drink and basket), the law refuses to reward the bundling and charges the **highest** rate, removing any incentive to hide a high-rate good inside a low-rate package. The subtle third case — Package C — is neither: once each item carries its *own* price on the invoice, there is no "single price," so Sec 2(74) mixed-supply doesn't even trigger and each line is taxed normally. Students lose marks by mechanically calling every bundle "composite"; the correct discipline is first ask "is there a *single* price?", then "is it *naturally* bundled?".

*(Full-marks tip: examiners award the two-step test explicitly stated before you compute; the classic errors are taxing the whole mixed hamper at an average or the principal rate instead of the highest, and treating separately-priced Package C as a mixed supply.)*

---

### Q72. Ch: GST – Supply — Schedule III, actionable claims & inter-State scope (Marks: 5) [Theory]
**Question:** "GST is a tax on supply, but not every dealing in value is a supply." Examine the validity of GST treatment in the following and state the correct position: (i) sale of lottery tickets by a distributor; (ii) sale of shares/securities by an investor; (iii) online money gaming/betting; (iv) inter-State stock transfer of goods between two GSTINs of the same PAN for ₹Nil consideration; (v) services by a member of Parliament / functions of a Court.

**Answer:**
- **(i) Lottery — taxable.** Although "actionable claims" are excluded by Schedule III Entry 6, the exclusion carves out **lottery, betting and gambling**, which remain **taxable actionable claims**. So a lottery ticket sale is a supply of goods and taxable.
- **(ii) Securities — not a supply.** Sec 2(52) defines "goods" to *exclude securities*, and Sec 2(102) excludes securities from "services" (only the *facilitation/brokerage* is a service). Hence sale of shares by an investor is **outside GST**; only the broker's commission is taxable.
- **(iii) Online money gaming/betting — taxable.** Falls in the same "lottery, betting, gambling" exception to Schedule III → taxable actionable claim (28% on full face value of bets).
- **(iv) Inter-State stock transfer — supply (Schedule I Entry 2).** Two GSTINs = distinct persons under Sec 25(4); even at Nil consideration it is a deemed supply, IGST payable on Rule 28 value; recipient takes ITC (revenue neutral).
- **(v) MP services / Court functions — neither (Schedule III).** Schedule III Entries 2 & 3 exclude functions performed by MPs/MLAs/constitutional post-holders and duties of a Court/Tribunal → not a supply.

**Conclusion:** Taxable — (i), (iii), (iv); outside GST — (ii), (v).

**Why this way (the reasoning):** The unifying principle is that Schedule III is a *negative list of exclusions*, but each exclusion has a deliberate boundary the exam probes. Actionable claims are generally excluded because they are mere rights to a debt/benefit and taxing them would tax a claim rather than a good — *except* lottery/betting/gambling, which Parliament deliberately keeps inside the net as a revenue-and-sin-tax measure. Securities are excluded from the very definitions of goods and services because they represent capital, not consumption — taxing every share trade would tax financial intermediation, so only the *service* of broking is caught. And the stock-transfer trap tests whether you remember that "same PAN, same company" does NOT mean "same person": once two branches hold different GSTINs, GST treats them as strangers to preserve the destination-based credit chain across States. Grasping *why* each carve-out is drawn where it is prevents the common blunder of exempting lottery (because "actionable claim") or taxing a share sale.

*(Full-marks tip: the examiner looks for the "actionable claim EXCEPT lottery/betting/gambling" precision and the distinct-person logic for stock transfers; blanket-exempting all actionable claims or all securities-related activity loses marks.)*

---

### Q73. Ch: GST – Charge & RCM — Forward vs Reverse Charge, composition impact (Marks: 8) [Problem]
**Question:** Shakti Traders (regular registered, Rajasthan) furnishes the following inward supplies for October 2025. Determine, for each, who is liable to pay GST (forward/reverse), compute the GST payable under RCM by Shakti, and the ITC of such RCM tax it can claim. All amounts are exclusive of GST; assume 18% unless a rate is stated.

| # | Inward supply | Value (₹) | Supplier |
|---|---|---|---|
| 1 | Legal services (representational) | 1,00,000 | Individual advocate |
| 2 | Goods transport by road | 50,000 | GTA (has NOT opted forward charge, 5% RCM) |
| 3 | Sponsorship of a trade event | 2,00,000 | A partnership firm |
| 4 | Rent of commercial office | 80,000 | Unregistered landlord (individual) |
| 5 | Sitting fees to a director (not an employee) | 40,000 | Director |
| 6 | Purchase of raw material | 5,00,000 | Registered supplier |
| 7 | Cotton (agricultural produce) | 1,50,000 | Agriculturist |

**Solution:**
**WN-1 — Liability determination (Sec 9(3)/9(4) CGST & Notif. 13/2017):**
1. Legal services by advocate to a business entity → **RCM** on recipient.
2. GTA @5% not opting forward charge → **RCM** on recipient.
3. Sponsorship to a body corporate/partnership firm → **RCM** on recipient (Shakti is a firm-recipient business entity).
4. Renting of *commercial* property by an unregistered person to a registered person → since Oct 2024, renting of commercial immovable property under **RCM**; also Sec 9(4)-type coverage.
5. Director's services (not employee) to the company → **RCM**.
6. Normal registered supplier → **Forward charge** (supplier pays; Shakti just takes ITC, not RCM).
7. Cotton by agriculturist → **RCM** on recipient (Sec 9(3) notified good).

**WN-2 — RCM tax computed (recipient's liability):**

| # | Value (₹) | Rate | RCM GST (₹) | ITC of RCM? |
|---|---|---|---|---|
| 1 Legal | 1,00,000 | 18% | 18,000 | Yes |
| 2 GTA | 50,000 | 5% | 2,500 | Yes |
| 3 Sponsorship | 2,00,000 | 18% | 36,000 | Yes |
| 4 Comm. rent | 80,000 | 18% | 14,400 | Yes |
| 5 Director fee | 40,000 | 18% | 7,200 | Yes |
| 7 Cotton | 1,50,000 | 5% | 7,500 | Yes |
| **RCM total** | | | **85,600** | |

*(Item 6 is forward charge — supplier charges 5,00,000 × 18% = ₹90,000 which Shakti pays to the supplier and claims as ITC; NOT part of RCM.)*

**WN-3 — Mechanism:** RCM tax of ₹85,600 must be paid **in cash** (electronic cash ledger; RCM cannot be set off against ITC). Once paid, it becomes **ITC** in the same/next month (subject to eligibility, none blocked here).

**Statement — Net Cash Outflow on RCM**

| Particulars | ₹ |
|---|---|
| RCM GST payable (cash) | 85,600 |
| ITC of RCM available | 85,600 |
| Net cost (revenue neutral, timing cost only) | Nil |

**Answer:** RCM tax payable by Shakti Traders = **₹85,600 (in cash)**, all of which is available as ITC. Item 6 (₹90,000) is under forward charge, not RCM.

**Why this way (the reasoning):** Reverse charge inverts the normal rule (Sec 9(1), supplier pays) for a *targeted list* of supplies where the government's collection is more secure or the supplier is hard to tax — advocates, GTAs, sponsorship, directors, agriculturists. The deep principle students must internalise is that RCM shifts *who deposits* the tax, not *whether* tax exists; and crucially RCM liability must be discharged **in cash**, because allowing ITC to pay your own RCM would let the tax net itself to zero before the credit chain is verified. Only *after* cash payment does the RCM tax convert into ITC — hence it is usually revenue-neutral but carries a working-capital/timing cost. The forward-vs-reverse trap is Item 2 (a GTA that has NOT opted forward charge stays on RCM at 5%) and Item 6 (a normal registered supplier is plain forward charge — putting it in the RCM column is the classic error). Recognising *why* the legislature picked these particular suppliers for RCM (enforcement difficulty, small/unorganised sectors) makes the list logical rather than arbitrary.

*(Full-marks tip: state Sec 9(3)/9(4) and Notif. 13/2017 for each, and stress RCM is paid in cash then taken as ITC; the standard deductions are dumping the forward-charge purchase into RCM and netting RCM against ITC instead of paying cash.)*

---

### Q74. Ch: GST – Charge & RCM — GTA option & threshold interplay (Marks: 6) [Case/Application]
**Question:** Analyse the GST liability and the correct payer in each independent case involving a Goods Transport Agency (GTA), and comment on the assessee's stand.

| # | Facts (FY 2025-26) | Stand taken |
|---|---|---|
| (i) | GTA transports goods for Ravi Manufacturers Ltd. (registered company); GTA has NOT filed the annexure opting for forward charge | GTA: "I will charge 12% forward and take ITC" |
| (ii) | Same GTA transports household goods of an *unregistered individual* (personal shifting) | "RCM applies, recipient pays" |
| (iii) | GTA files Annexure V opting forward charge at 12% for the whole year | "Recipient must still pay under RCM" |
| (iv) | Transport of *agricultural produce* and *milk* by the GTA | "Taxable at 5% RCM" |

**Answer:**
- **(i) RCM — GTA's stand wrong.** If a GTA has *not* opted for forward charge, the specified recipients (incl. any body corporate/registered person) pay under **RCM @5%** (no ITC to GTA). The GTA cannot unilaterally charge 12% forward without exercising the option. **Invalid.**
- **(ii) Not taxable — recipient's stand wrong.** Where the service recipient is an **unregistered individual/personal** consignor (none of the specified categories in Notif. 13/2017), the transaction is *exempt/not under RCM*; in fact GTA service to an unregistered person for personal use is not a notified RCM supply and is effectively outside charge. **RCM stand invalid.**
- **(iii) Forward charge — recipient's stand wrong.** Once the GTA files **Annexure V** opting forward charge (@12% with ITC or 5% without) for the year, the GTA pays; the recipient does **not** pay RCM. **Invalid.**
- **(iv) Wholly exempt — stand wrong.** Transport by a GTA of *agricultural produce, milk, salt, food grains, newspapers, defence equipment,* etc. is **exempt** (Notif. 12/2017). No 5% RCM. **Invalid.**

**Conclusion:** (i) RCM 5%; (ii) not taxable; (iii) forward charge by GTA; (iv) exempt.

**Why this way (the reasoning):** The GTA regime is a deliberate *default-with-opt-out* design. The default is RCM (recipient pays) because road transporters were historically unorganised and hard to bring into compliance — putting the tax on the (usually larger, registered) recipient secures collection. The 2022 reform then gave GTAs an *annual option* (Annexure V) to shift to forward charge, so that GTAs who want to pass on ITC to customers can. The exam tests whether you know the *switch*: the payer depends entirely on whether the option was filed, and a GTA cannot cherry-pick forward charge mid-stream (case i) nor can a recipient insist on RCM once the GTA has opted out (case iii). Cases (ii) and (iv) probe the *outer boundary* of the charge — services to non-specified/personal recipients and transport of exempt commodities never enter the RCM machinery at all. Understanding the policy — default RCM for enforcement, opt-out for credit flow, exemptions for essential goods — lets you answer any GTA permutation.

*(Full-marks tip: pin the answer to the "Annexure V option" fact; examiners deduct when students apply RCM to personal/unregistered consignors or tax the exempt-commodity transport.)*

---

### Q75. Ch: GST – Charge & RCM — Import of service & composition dealer under RCM (Marks: 5) [Problem/Case]
**Question:** Meghna Foods, a **composition dealer** (restaurant, 5% composition), receives in November 2025: (a) advertising/design services from a firm in Singapore for ₹4,00,000 (no Indian GST charged by the foreign supplier); (b) legal services from an Indian advocate ₹60,000; (c) goods from a registered wholesaler ₹8,00,000 (forward charge @5%). Determine Meghna's GST liability under RCM, whether it can use ITC, and the impact on its composition status.

**Solution:**
**WN-1 — Import of service (a):** Import of services for business consideration is a **supply** (Sec 7) and, being from outside India, is taxable under **RCM (Sec 5(3) IGST / Notif. 10/2017)** in the recipient's hands.
IGST @18% = 4,00,000 × 18% = **₹72,000 (RCM, cash).**

**WN-2 — Legal services (b):** Advocate → business entity = **RCM @18%** = 60,000 × 18% = **₹10,800 (cash).**

**WN-3 — Goods from wholesaler (c):** Forward charge; supplier collects tax; a composition dealer **cannot take ITC** — the 5% GST charged (₹40,000) is a **cost**.

**WN-4 — ITC & composition effect:** A composition dealer is **not entitled to ITC** on any inward supply, including RCM tax paid. Therefore the entire RCM of ₹72,000 + ₹10,800 = **₹82,800 is a cost**, paid in cash, with NO credit. RCM liability does **not** breach composition eligibility (Sec 10 permits composition dealers to receive RCM supplies), but it is paid at *normal rates*, not at the composition rate.

**Statement — RCM Liability of Meghna Foods (Nov 2025)**

| Inward supply | Value (₹) | Rate | RCM tax (₹) | ITC |
|---|---|---|---|---|
| Import of ad service | 4,00,000 | 18% (IGST) | 72,000 | No (composition) |
| Legal service | 60,000 | 18% | 10,800 | No |
| Goods (forward charge) | 8,00,000 | 5% | — (supplier pays) | No |
| **RCM payable (cash, cost)** | | | **82,800** | |

**Answer:** Meghna must pay **₹82,800 RCM in cash**, gets **no ITC** (composition), and its composition status **continues** — but this shows the hidden cost of RCM for a composition dealer.

**Why this way (the reasoning):** This problem exposes the harshest interaction in the GST charge scheme: a composition dealer is doubly disadvantaged on RCM. Reverse charge still applies to it in full — the law does not spare small dealers from RCM on imports, legal and other notified services, because RCM is about *securing the tax at the recipient*, and that logic doesn't weaken just because the recipient chose composition. But composition dealers are barred from ITC by Sec 10(4) as the *price* of paying a low turnover-based rate, so the RCM tax they pay in cash becomes a pure sunk cost with no credit relief — unlike a regular dealer for whom RCM is revenue-neutral. The examiner's trap is assuming "composition = only 5%, nothing else": in reality composition covers *outward* liability on turnover, while *inward* RCM sits on top at full rates with no offset. Seeing this teaches why a business with large RCM-heavy inward supplies may be *worse off* under composition despite the headline-low rate.

*(Full-marks tip: the marks are in stating RCM applies to composition dealers AND that they get no ITC, making it a cost; students who exempt composition dealers from RCM, or allow them ITC, lose the core marks.)*

---

### Q76. Ch: GST – Exemptions — Education & Health services (Marks: 8) [Case/Application]
**Question:** M/s Vidya Trust runs an educational institution and an attached hospital. Examine the taxability/exemption of each receipt (Notif. 12/2017) and compute the value of taxable supplies for October 2025.

| # | Receipt | Amount (₹) |
|---|---|---|
| 1 | Tuition fees for its higher-secondary (recognised board) students | 40,00,000 |
| 2 | Fees for a private coaching/competitive-exam wing (no recognised qualification) | 12,00,000 |
| 3 | Transport of its own students & faculty (school bus) | 3,00,000 |
| 4 | Canteen/mess catering to its own students | 2,00,000 |
| 5 | Renting school auditorium to an outside company for a product launch | 5,00,000 |
| 6 | Hospital: room rent for in-patients @ ₹4,000/day (non-ICU) | 6,00,000 |
| 7 | Hospital: room rent for in-patients @ ₹8,000/day (non-ICU) | 4,00,000 |
| 8 | Doctors' consultation & treatment (health care) | 20,00,000 |
| 9 | Cosmetic/plastic surgery (purely aesthetic, not reconstructive) | 3,00,000 |

**Solution:**
**WN-1 — Educational institution (Notif. 12/2017, Entry 66):** Services *by* an educational institution providing education up to a recognised qualification are **exempt**, and services *to* such an institution (transport, catering, security, admission) are also exempt. Coaching giving *no recognised qualification* is **taxable**.
- (1) Tuition (recognised) → **Exempt.**
- (2) Coaching wing (no recognised qualification) → **Taxable ₹12,00,000.**
- (3) Transport of own students/faculty → **Exempt** (service to educational institution).
- (4) Catering to own students → **Exempt.**
- (5) Renting auditorium to an outside company (commercial, not an education service) → **Taxable ₹5,00,000.**

**WN-2 — Health care (Notif. 12/2017, Entry 74):** Health-care services by a clinical establishment are **exempt**, EXCEPT **room rent above ₹5,000/day** (non-ICU) which is *taxable @5% (no ITC)*, and **purely cosmetic** surgery which is taxable.
- (6) Room @₹4,000 (≤₹5,000) → **Exempt.**
- (7) Room @₹8,000 (>₹5,000, non-ICU) → **Taxable ₹4,00,000 @5%.**
- (8) Consultation/treatment → **Exempt.**
- (9) Cosmetic surgery (aesthetic) → **Taxable ₹3,00,000.**

**Statement — Value of Taxable Supplies (Oct 2025)**

| # | Nature | Taxable value (₹) |
|---|---|---|
| 2 | Coaching (no recognised qualification) | 12,00,000 |
| 5 | Auditorium renting | 5,00,000 |
| 7 | Room rent > ₹5,000/day | 4,00,000 |
| 9 | Cosmetic surgery | 3,00,000 |
| **Total taxable value** | | **24,00,000** |

**Answer:** Exempt receipts = ₹71,00,000 (items 1,3,4,6,8); **Taxable value = ₹24,00,000** (items 2,5,7,9). Item 7 room rent is taxable @5% without ITC.

**Why this way (the reasoning):** Education and health exemptions rest on a *merit-goods* rationale — the State subsidises core education and healthcare by keeping them GST-free — but each exemption is fenced tightly to prevent commercial spill-over. Education is exempt only up to a *recognised qualification*; the moment an institute sells competitive-exam coaching that leads to no recognised degree, it is a commercial service and taxable (item 2). Similarly, *ancillary* services to a school (bus, mess) are exempt because taxing them would raise the cost of the exempt core, but letting the auditorium to an outsider for a product launch is plainly commercial and outside the shelter (item 5). Health care is exempt to protect patients, yet the law draws a bright line: rooms above ₹5,000/day signal *luxury* consumption and are taxed (item 7), and cosmetic/aesthetic surgery is *not* "health care" restoring health, so it is taxed (item 9). The examiner is testing whether you see that an exemption follows the *purpose* of the activity, not merely the *identity* of the provider — a trust running a hospital does not make every rupee it earns exempt.

*(Full-marks tip: cite Entries 66 and 74 and the ₹5,000 room-rent threshold and the "recognised qualification" test; the common deductions are exempting the coaching wing, the auditorium letting, and the high-value room rent just because the entity is an educational/charitable trust.)*

---

### Q77. Ch: GST – Exemptions — Charitable, transport & agricultural exemptions (Marks: 6) [Case/Application]
**Question:** Examine whether the following are exempt or taxable under Notif. 12/2017, giving the specific ground, and comment on validity of the claim.

| # | Facts | Claim |
|---|---|---|
| (i) | A charitable trust (registered u/s 12AA/12AB) conducts yoga camps and charges a fee | Exempt |
| (ii) | Same trust rents out its commercial shops (owned property) for ₹15 lakh p.a. | Exempt (charitable) |
| (iii) | Transport of passengers by *non-AC* stage carriage (ordinary bus) | Taxable |
| (iv) | Transport of a consignment of *organic manure* by rail | Taxable |
| (v) | Warehousing/loading of *rice* (agricultural produce after minimal processing) | Exempt |
| (vi) | Services by an agriculturist of *rearing of race-horses* | Exempt (agriculture) |

**Answer:**
- **(i) Exempt.** Charitable activities by a 12AA/12AB trust — including **yoga** and advancement of religion/spirituality — are exempt (Entry 1, "charitable activities" includes yoga). **Valid.**
- **(ii) Taxable.** Renting of *commercial* immovable property is a business activity, **not** a "charitable activity"; the 12AB registration does not exempt commercial rent. **Claim invalid — taxable.**
- **(iii) Exempt.** Transport of passengers by **non-AC** contract/stage carriage (other than radio taxi/AC) is **exempt**. **Claim (taxable) invalid.**
- **(iv) Exempt.** Transport of *agricultural produce, organic manure, milk, salt, food grains* by rail/vessel/GTA is **exempt**. **Claim (taxable) invalid.**
- **(v) Exempt.** Loading/warehousing/storage of **agricultural produce** is exempt; rice retains agricultural-produce character (only minimal processing making it marketable). **Valid.**
- **(vi) Taxable.** "Agricultural produce" and agricultural exemptions **exclude rearing of horses**; rearing of race-horses is specifically **not** an exempt agricultural activity. **Claim invalid — taxable.**

**Conclusion:** Exempt — (i), (iii), (iv), (v); Taxable — (ii), (vi).

**Why this way (the reasoning):** Each exemption is a *purpose-tested* relief, and the exam probes the exact boundary of that purpose. A charitable trust is exempt only for genuinely *charitable* activities (relief of the poor, education, health, yoga, religion) — the 12AB registration is a *gateway*, not a blanket shield, so its ordinary commercial rent is taxed like anyone's (ii). Passenger-transport exemptions favour *mass, non-luxury* travel — non-AC stage carriage is exempt because it serves the common commuter, whereas AC/radio-taxi is taxed as a comfort service (iii). Agricultural exemptions protect the *farm-to-market* chain for essential produce and inputs (manure, food grains, storage), which is why (iv) and (v) are exempt — but the definition of "agricultural produce" deliberately *excludes* horse-rearing because race-horses are a luxury/sport activity, not food/fibre production (vi). The recurring lesson: never answer from the *status of the person* (trust, farmer); answer from whether the *specific activity* falls inside the exemption's protected purpose.

*(Full-marks tip: name the activity-based test, not the entity; examiners routinely trap students into exempting a charity's commercial rent and race-horse rearing, and into taxing exempt manure transport and non-AC bus travel.)*

---

### Q78. Ch: GST – Exemptions — Threshold, small suppliers & mixed exempt/taxable (Marks: 5) [Problem]
**Question:** Neel provides the following services in FY 2025-26 from Rajasthan (intra-State). Determine his aggregate turnover, whether he must register, and the value of taxable supplies. Exemption threshold for services = ₹20 lakh.

| # | Receipt | Amount (₹) |
|---|---|---|
| 1 | Interest on fixed deposits and loans given | 6,00,000 |
| 2 | Renting of residential dwelling to an *unregistered individual* for residence | 4,00,000 |
| 3 | Coaching services (taxable) | 13,00,000 |
| 4 | Renting of a commercial shop | 5,00,000 |

**Solution:**
**WN-1 — Nature of each receipt:**
- (1) Interest on deposits/loans = *exempt* service, BUT it is **included in aggregate turnover** (aggregate turnover includes exempt supplies). Value ₹6,00,000 — exempt.
- (2) Renting of *residential* dwelling for *residence* to an unregistered person = **exempt** (Entry 12). Included in aggregate turnover. ₹4,00,000.
- (3) Coaching = **taxable** ₹13,00,000.
- (4) Commercial shop rent = **taxable** ₹5,00,000.

**WN-2 — Aggregate turnover (Sec 2(6)):** = taxable + exempt + exports + inter-State, of same PAN, all-India.
= 6,00,000 + 4,00,000 + 13,00,000 + 5,00,000 = **₹28,00,000.**

**WN-3 — Registration:** Aggregate turnover ₹28 lakh > threshold ₹20 lakh → **registration compulsory**. (Note: interest and residential rent are counted for the threshold even though exempt.)

**WN-4 — Taxable value:** Only items 3 + 4 bear GST = 13,00,000 + 5,00,000 = **₹18,00,000.**

**Statement — Neel, FY 2025-26**

| Particulars | ₹ |
|---|---|
| Aggregate turnover (for threshold) | 28,00,000 |
| Registration required? | Yes (>₹20 lakh) |
| Exempt supplies (interest + residential rent) | 10,00,000 |
| Taxable value of supplies | 18,00,000 |

**Answer:** Aggregate turnover **₹28,00,000** → **must register**; taxable value **₹18,00,000**; exempt ₹10,00,000. Note the taxable turnover alone (₹18 lakh) is *below* ₹20 lakh, yet registration is triggered because **exempt supplies count toward the threshold.**

**Why this way (the reasoning):** This question turns on a distinction students constantly conflate: the *threshold* for registration is measured on **aggregate turnover** (Sec 2(6)), which deliberately *includes exempt supplies*, whereas the *tax you pay* is only on **taxable supplies**. The policy reason for counting exempt supplies in the threshold is to gauge the true *scale* of a person's business — a supplier doing ₹28 lakh of business, even if much is exempt, is not a "small" supplier the exemption was meant to spare. So Neel's taxable turnover of ₹18 lakh (below ₹20 lakh) is a red herring: the ₹6 lakh interest (an exempt financial service) and ₹4 lakh residential rent push aggregate turnover over the line and force registration. The trap is exactly this — thinking exempt income is invisible for registration. Once registered, of course, he charges GST only on the ₹18 lakh taxable slice. Distinguishing "turnover for threshold" from "value for tax" is the whole lesson.

*(Full-marks tip: show the aggregate-turnover build-up including exempt items; the standard error is excluding exempt interest/residential rent and wrongly concluding no registration is needed.)*

---

### Q79. Ch: GST – Time & Value of Supply — Time of Supply of goods & services with advances (Marks: 8) [Problem]
**Question:** Determine the **time of supply** (TOS) in each independent case and state the rule applied.

| # | Facts | Dates/amounts |
|---|---|---|
| (i) | Supply of **goods** (forward charge): removal 5-Oct; invoice 8-Oct; payment received 30-Sep (advance ₹50,000 of ₹2,00,000) | — |
| (ii) | Supply of **goods**: invoice NOT issued within the due date; goods removed 12-Nov; due date of invoice 12-Nov; payment 20-Nov | — |
| (iii) | Supply of **services**: invoice issued 15-Oct (within 30 days of completion 2-Oct); payment 25-Oct; advance ₹1,00,000 received 28-Sep | — |
| (iv) | Supply of **services**: service completed 4-Nov; invoice issued 20-Dec (beyond 30 days); payment 10-Dec | — |
| (v) | **RCM** supply of goods: date of receipt of goods 8-Oct; invoice by supplier 3-Oct; payment 15-Oct | — |
| (vi) | **RCM** supply of services (associated/import): date of payment 12-Nov; date of entry in books 5-Nov; invoice 1-Nov | — |

**Solution:**
**WN-1 — Governing rules:**
- **Goods, forward charge (Sec 12(2)):** TOS = *earlier of* (a) date of invoice OR the last date invoice *should* have been issued (i.e., date of removal), and (b) — [advance for goods is **NOT** taxed; Notif. 66/2017 removed advance-tax on goods for all suppliers except composition]. So for goods, ignore advances; TOS = earlier of invoice date or due date of invoice (removal).
- **Services (Sec 13(2)):** TOS = *earlier of* (a) invoice date if issued within 30 days, else date of completion; and (b) date of payment. Advances **ARE** taxed for services.
- **RCM goods (Sec 12(3)):** earliest of (a) receipt of goods, (b) date of payment, (c) 30 days from supplier's invoice.
- **RCM services (Sec 13(3)):** earliest of (a) date of payment, (b) 60 days from supplier's invoice (for import/associated enterprises, the book-entry date also relevant).

**WN-2 — Application:**
- **(i)** Goods: advance of 30-Sep is **ignored** (Notif. 66/2017). TOS = earlier of invoice (8-Oct) and removal (5-Oct) = **5-Oct** for the whole ₹2,00,000.
- **(ii)** Goods, invoice not issued by due date: TOS = due date of invoice = date of removal = **12-Nov.**
- **(iii)** Services: invoice 15-Oct (within 30 days), payment 25-Oct, but advance ₹1,00,000 on **28-Sep**. TOS is per receipt: **₹1,00,000 → 28-Sep** (advance taxed); **balance ₹→ 15-Oct** (earlier of invoice 15-Oct vs balance payment 25-Oct).
- **(iv)** Services, invoice beyond 30 days → invoice date irrelevant; TOS = earlier of completion (4-Nov) and payment (10-Dec) = **4-Nov.**
- **(v)** RCM goods: earliest of receipt (8-Oct), payment (15-Oct), 30 days from invoice (3-Oct → 2-Nov) = **8-Oct.**
- **(vi)** RCM services: earliest of payment (12-Nov) and 60 days from invoice (1-Nov → 31-Dec) = **12-Nov.** (Book entry 5-Nov relevant if the other two fail; here payment governs.)

**Statement — Time of Supply**

| Case | Rule (Sec) | TOS |
|---|---|---|
| (i) | 12(2), Notif.66 | 5-Oct (advance ignored) |
| (ii) | 12(2) | 12-Nov |
| (iii) | 13(2) | ₹1L → 28-Sep; balance → 15-Oct |
| (iv) | 13(2) | 4-Nov |
| (v) | 12(3) RCM | 8-Oct |
| (vi) | 13(3) RCM | 12-Nov |

**Answer:** As tabulated — note the pivotal distinction: **advances are taxed for services but NOT for goods.**

**Why this way (the reasoning):** Time of supply fixes *when* the tax liability crystallises, and the design differs for goods and services for a very deliberate reason. For **goods**, the government (via Notif. 66/2017) removed the tax-on-advance because taxing advances on physical goods created reconciliation nightmares (advance received, goods not yet identified/removed) — so for goods TOS keys off the *invoice or removal*, and any advance is simply ignored (case i). For **services**, which are intangible and often paid before performance, advances *remain* taxable, because otherwise a large slice of value (retainers, booking fees) would escape until much later — hence case (iii) splits the liability, taxing the ₹1 lakh advance at receipt. The "invoice within 30 days" condition (cases iii vs iv) is an anti-deferral device: issue the invoice late and you *lose* the benefit of the invoice date, and TOS snaps back to the *completion* date, so a supplier cannot postpone tax by delaying paperwork. Under RCM the recipient has no invoice control, so TOS keys off receipt/payment with an outer cap (30/60 days). Understanding *why* each trigger exists — advance policy, anti-deferral, RCM outer limits — lets you compute TOS for any fact pattern instead of guessing "earlier of everything."

*(Full-marks tip: explicitly state Notif. 66/2017 for goods advances and the 30-day invoice rule for services; the top deductions are taxing goods-advances and using the invoice date in (iv) despite it being beyond 30 days.)*

---

### Q80. Ch: GST – Time & Value of Supply — Change in rate of tax (Sec 14) (Marks: 6) [Problem]
**Question:** The GST rate on a service changed from **12% to 18% with effect from 1-Nov-2025**. Determine the **applicable rate** and **time of supply** in each case using Sec 14.

| Case | Supply of service completed | Invoice issued | Payment received |
|---|---|---|---|
| A | Before (25-Oct) | After (5-Nov) | After (7-Nov) |
| B | Before (25-Oct) | Before (28-Oct) | After (7-Nov) |
| C | Before (25-Oct) | After (5-Nov) | Before (30-Oct) |
| D | After (5-Nov) | Before (28-Oct) | After (7-Nov) |
| E | After (5-Nov) | Before (28-Oct) | Before (30-Oct) |
| F | After (5-Nov) | After (5-Nov) | Before (30-Oct) |

**Solution:**
**WN-1 — Rule (Sec 14):** When supply is completed **before** the rate change: TOS = *earlier* of the two events (invoice/payment) that fall **after**, but if **both** invoice and payment are on the **same side**, TOS is that event and the corresponding rate applies. Precisely:
- If supply **before** change: if invoice & payment are on *opposite sides* → TOS = whichever is *before* is disregarded; if *both after* → TOS after (new rate); if *one before, one after* → TOS = the **earlier** of invoice/payment.
- Standard 2-of-3 logic: TOS and rate follow **whichever two of {supply, invoice, payment} lie on the same side**… Simplified statutory outcomes below.

**WN-2 — Application:**

| Case | Supply | Invoice | Payment | TOS = | Rate |
|---|---|---|---|---|---|
| A | Old | New | New | earlier of invoice(5-Nov)/payment(7-Nov) = **5-Nov** | **18% (new)** |
| B | Old | Old | New | invoice date **28-Oct** | **12% (old)** |
| C | Old | New | Old | payment date **30-Oct** | **12% (old)** |
| D | New | Old | New | payment date **7-Nov** | **18% (new)** |
| E | New | Old | Old | earlier of invoice(28-Oct)/payment(30-Oct) = **28-Oct** | **12% (old)** |
| F | New | New | Old | invoice date **5-Nov** | **18% (new)** |

**Rationale of each:** Sec 14 says when supply is *before* the change (A,B,C): if *both* invoice & payment are after → new rate (not here); if only one is after, TOS = that event's date if the other is before, but the rule takes the date of invoice/payment **received after** as TOS EXCEPT where both are before-... Applying the statutory 2-events-on-same-side test gives the table above: the **rate follows the side (old/new) on which two of the three events fall**.

**Statement — Applicable Rate**

| Case | Rate | TOS |
|---|---|---|
| A | 18% | 5-Nov |
| B | 12% | 28-Oct |
| C | 12% | 30-Oct |
| D | 18% | 7-Nov |
| E | 12% | 28-Oct |
| F | 18% | 5-Nov |

**Answer:** Old rate 12% in cases **B, C, E**; new rate 18% in **A, D, F.**

**Why this way (the reasoning):** Section 14 exists precisely because at a rate change, three events (supply, invoice, payment) can straddle the cut-off date, and the law must pick *one* moment to decide the rate — otherwise suppliers would time paperwork to grab the lower rate. The elegant principle Sec 14 uses is a **"majority/two-of-three" rule**: the tax rate follows the side of the change-date on which **at least two of the three events** fall, and the time of supply is set accordingly. So in Case B (supply and invoice both old-side) the old 12% wins even though payment came later; in Case D (supply and payment both new-side) the new 18% wins despite an early invoice. This prevents rate-arbitrage: you cannot secure the old rate merely by pre-dating an invoice (Case D) or the new rate by delaying one document, because a single stray event cannot override the two that anchor the transaction's real timing. Once you see it as "where do two of the three events sit?", every one of the six permutations becomes mechanical rather than memorised.

*(Full-marks tip: state the "two-of-three events" principle before the table; the usual deduction is picking TOS from a single event (e.g., always the invoice) without checking which side holds the majority of events.)*

---

### Q81. Ch: GST – Time & Value of Supply — Value of Supply Sec 15: inclusions & discounts (Marks: 10) [Problem]
**Question:** From the following, compute the **value of taxable supply** and **GST @18%** for Surya Ltd.'s single invoice to an unrelated customer.

| # | Particulars | ₹ |
|---|---|---|
| 1 | List price of goods (before any discount) | 10,00,000 |
| 2 | Trade discount shown on the face of invoice @5% | ? |
| 3 | Packing charges | 25,000 |
| 4 | Municipal tax / local cess collected by supplier | 40,000 |
| 5 | Subsidy from Central Government (linked to price) | 1,00,000 |
| 6 | Subsidy from a private trust (NOT Government, price-linked) | 60,000 |
| 7 | Late-payment interest for delayed payment (charged separately) | 15,000 |
| 8 | Freight — supplier arranged, recovered from buyer (contract is FOR-destination) | 50,000 |
| 9 | Inspection/testing charges before delivery, recovered | 20,000 |
| 10 | TCS under Income-tax Act collected | 8,000 |
| 11 | Cash discount for early payment, agreed in the contract and buyer complied | 30,000 (post-supply) |

**Solution:**
**WN-1 — Trade discount (item 2):** Discount recorded on the invoice at the time of supply is **deductible** (Sec 15(3)(a)). = 10,00,000 × 5% = **₹50,000 deductible.** Net price = ₹9,50,000.

**WN-2 — Inclusions (Sec 15(2)):**
- **Packing (3):** incidental expense → **include ₹25,000.**
- **Municipal tax/cess (4):** any tax/cess *other than GST* charged by supplier → **include ₹40,000.**
- **Govt subsidy (5):** subsidies given by **Central/State Government are EXCLUDED** → **exclude ₹1,00,000.**
- **Private-trust subsidy (6):** subsidy *not* from Government, directly linked to price → **include ₹60,000** (Sec 15(2)(e)).
- **Interest for delayed payment (7):** interest/late fee/penalty for delayed payment → **include ₹15,000.**
- **Freight FOR-destination (8):** part of composite supply / incidental → **include ₹50,000.**
- **Inspection/testing (9):** amount charged before delivery, incidental → **include ₹20,000.**
- **TCS under Income-tax (10):** TCS is not a consideration for supply (mere tax collection) → **exclude ₹8,000** (CBIC clarification).

**WN-3 — Cash discount (item 11):** Post-supply discount is deductible under Sec 15(3)(b) *only if* (a) established in an agreement *before/at* supply, (b) linked to relevant invoices, and (c) ITC attributable is reversed by the recipient. Here it was **agreed in the contract** and buyer complied → **deductible ₹30,000** (assuming buyer reverses ITC).

**Statement Showing Value of Taxable Supply — Surya Ltd.**

| Particulars | ₹ |
|---|---|
| List price | 10,00,000 |
| Less: Trade discount (on invoice) 15(3)(a) | (50,000) |
| Add: Packing charges | 25,000 |
| Add: Municipal tax/cess (non-GST) 15(2)(a) | 40,000 |
| Add: Private (non-Govt) subsidy, price-linked 15(2)(e) | 60,000 |
| Add: Interest for delayed payment 15(2)(d) | 15,000 |
| Add: Freight (FOR-destination) | 50,000 |
| Add: Inspection/testing charges | 20,000 |
| *Govt subsidy — excluded* | — |
| *TCS (Income-tax) — excluded* | — |
| Sub-total | 11,10,000 |
| Less: Cash discount (post-supply, 15(3)(b) conditions met) | (30,000) |
| **Value of taxable supply** | **10,80,000** |
| **GST @18%** | **1,94,400** |

**Answer:** Value of taxable supply = **₹10,80,000**; GST @18% = **₹1,94,400.**

**Why this way (the reasoning):** Section 15 builds the taxable value on the principle that GST is levied on the **full economic consideration the supplier realises for the supply** — so anything the buyer effectively pays *for the supply* is included, regardless of how it is labelled. That is why incidental charges (packing, freight, inspection) and even *other taxes/cesses* the supplier collects are added: they are all part of what the buyer parts with to get the goods. Subsidies are the sharp test of this logic — a *price-linked* subsidy is money that substitutes for what the buyer would otherwise pay, so it belongs in the value (item 6), *except* Government subsidies, which the law deliberately excludes so that the State's welfare support is not itself taxed (item 5). Discounts split on *timing and certainty*: a discount known at supply (trade discount on the invoice) reduces value straightforwardly, but a *post-supply* discount is allowed only if it was pre-agreed and the buyer reverses the matching ITC — otherwise sellers could erode the tax base after the fact and break the credit chain. TCS is excluded because it is a *collection of someone else's income-tax*, not consideration for the goods. The whole computation is really one question repeated: *is this rupee part of what the buyer pays for the supply?*

*(Full-marks tip: the examiner wants each add/exclude tagged to its Sec 15 sub-clause and the Govt-vs-non-Govt subsidy distinction; the classic deductions are including the Government subsidy and TCS, and allowing the cash discount without stating the ITC-reversal condition.)*

---

### Q82. Ch: GST – Time & Value of Supply — Value under Rule 27–31 (non-monetary / related persons) (Marks: 8) [Problem/Case]
**Question:** Determine the value of supply and comment, applying the Valuation Rules where Sec 15 transaction value cannot apply.

| # | Facts |
|---|---|
| (i) | Rani exchanges a new phone; buyer pays ₹18,000 cash + gives an old phone. Open market value (OMV) of new phone = ₹25,000. |
| (ii) | Ace Ltd. supplies goods to its sister concern (related person). OMV = ₹4,00,000; the sister will use them for further taxable supply and is eligible for full ITC. Price actually charged = ₹3,50,000. |
| (iii) | A principal supplies goods to his agent who will sell them onward; like-kind goods have OMV ₹2,00,000; the agent sells similar goods to unrelated customers at ₹2,10,000. Price charged to agent = ₹1,80,000. |
| (iv) | Value cannot be determined by OMV or like-kind; cost of production = ₹1,00,000. |

**Solution:**
**WN-1 — (i) Consideration not wholly in money (Rule 27):** Value = *OMV*; if not available, consideration in money + money-equivalent of non-money part. OMV of the new phone = **₹25,000** → value of supply = **₹25,000** (not merely the ₹18,000 cash).

**WN-2 — (ii) Related persons (Rule 28):** Value = OMV. **Proviso:** where the recipient is **eligible for full ITC**, the value declared in the invoice is **deemed to be the OMV**. Sister concern gets full ITC → **₹3,50,000 (invoice value) is accepted.** No adjustment to ₹4,00,000 needed.

**WN-3 — (iii) Principal–Agent (Rule 29):** Value = OMV OR, at the supplier's option, **90% of the price charged by the agent (recipient) to unrelated customers** for like goods. 90% × 2,10,000 = **₹1,89,000.** Supplier may choose OMV ₹2,00,000 or ₹1,89,000; the ₹1,80,000 actually charged is not automatically accepted unless recipient has full ITC. Optimal declared value (with full-ITC proviso) could be ₹1,80,000; otherwise **₹1,89,000** (option) or OMV ₹2,00,000.

**WN-4 — (iv) Cost method (Rule 30):** Value = **110% of cost** = 1,00,000 × 110% = **₹1,10,000.** (If even this fails, Rule 31 residual/best-judgement.)

**Statement — Value of Supply under Valuation Rules**

| Case | Rule | Value (₹) |
|---|---|---|
| (i) Barter | 27 | 25,000 |
| (ii) Related (full ITC) | 28 proviso | 3,50,000 (invoice = OMV) |
| (iii) Principal–agent | 29 | 1,89,000 (90% option) / 2,00,000 OMV |
| (iv) No OMV/like-kind | 30 | 1,10,000 (cost + 10%) |

**Answer:** (i) ₹25,000; (ii) ₹3,50,000; (iii) ₹1,89,000 (or OMV ₹2,00,000); (iv) ₹1,10,000.

**Why this way (the reasoning):** The Valuation Rules exist as a *fallback ladder* for the situations where Sec 15's "transaction value" is unreliable — because the price is not the real measure of value (barter), or the parties are not at arm's length (related persons, agents). The logic is to reconstruct what the supply *would* fetch in an open market. In barter (Rule 27) the cash paid understates value, so OMV of the thing supplied governs — otherwise part of the consideration (the old phone) would escape tax. For related persons (Rule 28) the price can be manipulated, so OMV is the default — but the law adds a brilliant *pragmatic proviso*: if the recipient gets **full ITC**, whatever the supplier charges is accepted, because any under- or over-valuation is perfectly offset by a matching ITC and the exercise is **revenue-neutral** — policing it would be pointless bureaucracy. That single proviso resolves cases (ii) and often (iii). The 90%-of-onward-price option in Rule 29 gives the principal a workable proxy for the agent's true value, and Rule 30's cost-plus-10% and Rule 31's residual method are last resorts when no market comparator exists. Seeing the rules as a *sequential ladder anchored to "open market value"* — with a revenue-neutral shortcut when full ITC exists — is the key insight.

*(Full-marks tip: the marks hinge on citing the *full-ITC proviso* to Rule 28 (invoice value accepted) and applying the rules in sequence 27→28→29→30→31; students lose marks forcing OMV on related-party supplies where full ITC makes the invoice value valid.)*

---

### Q83. Ch: GST – Time & Value of Supply — Integrated: supply + value + TOS + charge (Marks: 10) [Case/Application]
**Question:** Zenith Ltd. (registered, Gujarat) enters a contract on 20-Oct-2025 to supply and install industrial machinery. Analyse (a) nature/classification of supply, (b) value of supply, (c) time of supply of each component, (d) who pays GST, and compute the total GST. Data:

| # | Element | ₹ |
|---|---|---|
| 1 | Machinery (goods) | 30,00,000 |
| 2 | Installation & commissioning (service, naturally bundled) | 5,00,000 |
| 3 | Advance received on 20-Oct | 10,00,000 |
| 4 | Machinery removed/delivered 8-Nov; invoice 10-Nov | — |
| 5 | Freight arranged by Zenith, recovered (FOR-destination) | 1,20,000 |
| 6 | Design fee paid by Zenith to a *foreign* consultant (import of service) for this contract | 3,00,000 |
| 7 | Trade discount on machinery, on invoice @4% | ? |
| 8 | Applicable rate on machinery (composite) | 18% |

**Solution:**
**WN-1 — Classification (a):** Machinery + installation, naturally bundled with machinery as the principal supply → **composite supply**; whole taxed at the **principal (machinery) rate 18%.**

**WN-2 — Value of supply (b):**
- Machinery 30,00,000 + installation 5,00,000 = 35,00,000
- Less trade discount 4% of 30,00,000 = (1,20,000) → 33,80,000
- Add freight (FOR-destination, part of composite) 1,20,000 → **Value = ₹35,00,000.**
- (Design fee to foreign consultant is Zenith's *inward* import of service, valued separately under RCM — not part of outward value.)

**WN-3 — Time of supply (c):**
- Outward composite supply is *principally goods* → TOS per Sec 12(2); **advance on goods is not taxed** (Notif. 66/2017). TOS = earlier of invoice (10-Nov) or removal (8-Nov) = **8-Nov** for the whole ₹35,00,000.
- Import of design service (RCM, Sec 13(3)) → earliest of payment date or 60 days from foreign invoice.

**WN-4 — Who pays / charge (d):**
- Outward supply: **forward charge**, Zenith collects 18% from customer.
- Import of design service: **RCM** — Zenith pays IGST @18% on ₹3,00,000 = **₹54,000 (cash)**, then takes ITC (revenue-neutral).

**WN-5 — Computation:**
- Outward GST = 35,00,000 × 18% = **₹6,30,000** (CGST 3,15,000 + SGST 3,15,000, intra-State).
- RCM on import = 3,00,000 × 18% = **₹54,000 (IGST, cash; ITC available).**

**Statement — GST Computation, Zenith Ltd.**

| Particulars | Value (₹) | Rate | GST (₹) | Charge |
|---|---|---|---|---|
| Composite outward supply (machinery + install + freight, net of discount) | 35,00,000 | 18% | 6,30,000 | Forward |
| Import of design service | 3,00,000 | 18% (IGST) | 54,000 | RCM (cash, then ITC) |
| **Outward tax collected** | | | **6,30,000** | |
| **RCM cash outflow** | | | **54,000** | (offset by ITC) |

**Answer:** Composite supply @18%; **value ₹35,00,000, outward GST ₹6,30,000** (TOS 8-Nov, advance on goods not taxed); import design service under **RCM ₹54,000** paid in cash then taken as ITC.

**Why this way (the reasoning):** This is the "everything at once" question and its lesson is that each GST concept answers a *different* question about the *same* transaction, and you must not let them contaminate each other. **Classification** (composite → principal rate) decides the *rate*; the machinery dominates so installation and freight ride along at 18% rather than being split out. **Value** (Sec 15) decides *how much* — trade discount on the invoice comes off, FOR-destination freight goes in because it is part of the delivered price, but the *inward* design fee never touches the outward value because it is Zenith's cost, not the customer's consideration. **Time of supply** decides *when* — and the crucial trap is that although a ₹10 lakh advance was received on 20-Oct, a composite supply that is *principally goods* follows the goods TOS rule, so Notif. 66/2017 **exempts the advance from tax** and the whole liability arises only on removal (8-Nov). Finally **charge** decides *who pays* — the outward supply is ordinary forward charge, while the import of the design service flips to RCM, discharged in cash and then reclaimed as ITC. Keeping these four axes — rate, amount, timing, payer — mentally separate is exactly what distinguishes a rank-holder's answer from a muddled one.

*(Full-marks tip: examiners award marks for treating the advance-on-goods correctly (not taxed) AND separating the inward RCM import from the outward value; the frequent failures are taxing the advance, adding the design fee to outward value, and splitting the composite supply into separate rates.)*

---

### Q84. Ch: GST – Charge & RCM — Composition scheme eligibility & tax computation (Marks: 6) [Problem/Case]
**Question:** Advise whether each person is eligible for the **composition scheme** (Sec 10) for FY 2025-26 and, where a person is eligible, compute the composition tax. Threshold: ₹1.5 crore (goods), ₹50 lakh (service composition u/s 10(2A)).

| # | Person | Facts |
|---|---|---|
| (i) | Traders Ltd. | Turnover ₹1.2 crore (goods); makes an **inter-State** outward supply of ₹5 lakh |
| (ii) | Foodie Restaurant | Turnover ₹90 lakh, only intra-State; supplies food (restaurant service) |
| (iii) | Gadget Store | Turnover ₹1.1 crore of goods + ₹8 lakh of *repair services* (mixed) |
| (iv) | Ice-cream Maker | Turnover ₹80 lakh; **manufactures ice-cream** |
| (v) | Small Consultant | Turnover ₹40 lakh of pure professional services (not restaurant) |

**Solution:**
**WN-1 — Eligibility conditions (Sec 10):** Composition is barred for: (a) inter-State *outward* supply; (b) supply of non-taxable goods; (c) manufacturers of *notified* goods (ice-cream, pan masala, tobacco, aerated water); (d) services beyond restaurant service exceeding the higher of ₹5 lakh or 10% of turnover [10(1) proviso]; a pure-service supplier may use 10(2A) if turnover ≤ ₹50 lakh.

**WN-2 — Application:**
- **(i) Ineligible.** Any **inter-State outward** supply disqualifies composition, regardless of turnover being below ₹1.5 cr. **Not eligible.**
- **(ii) Eligible.** Restaurant service is *specifically allowed* under composition; turnover ₹90 lakh < ₹1.5 cr, intra-State only. **Rate 5% (2.5% CGST + 2.5% SGST).** Tax = 90,00,000 × 5% = **₹4,50,000.**
- **(iii) Eligible.** Goods trader may also supply services up to *higher of ₹5 lakh or 10% of turnover*. 10% of ₹1.1 cr = ₹11 lakh; repair services ₹8 lakh < ₹11 lakh → within limit. Total turnover ₹1.18 cr < ₹1.5 cr. **Eligible. Rate 1% (traders)** on ₹1.18 cr = **₹1,18,000.**
- **(iv) Ineligible.** **Ice-cream is a notified good** whose manufacturer is *barred* from composition. **Not eligible.**
- **(v) Eligible under 10(2A).** Pure services turnover ₹40 lakh ≤ ₹50 lakh → eligible for the **special composition for services @6% (3%+3%).** Tax = 40,00,000 × 6% = **₹2,40,000.**

**Statement — Composition Eligibility & Tax**

| Person | Eligible? | Rate | Composition tax (₹) |
|---|---|---|---|
| (i) Traders Ltd. | No (inter-State) | — | — |
| (ii) Foodie Restaurant | Yes | 5% | 4,50,000 |
| (iii) Gadget Store | Yes | 1% | 1,18,000 |
| (iv) Ice-cream Maker | No (notified good) | — | — |
| (v) Small Consultant | Yes (10(2A)) | 6% | 2,40,000 |

**Answer:** Eligible — (ii) ₹4,50,000, (iii) ₹1,18,000, (v) ₹2,40,000. Ineligible — (i) inter-State supply; (iv) ice-cream manufacturer.

**Why this way (the reasoning):** The composition scheme is a *simplicity-for-small-taxpayers* bargain: pay a low flat percentage of turnover, skip detailed ITC and monthly compliance — but in return accept strict conditions that keep the scheme from being abused by larger or cross-border players. Each disqualification has a clear logic. **Inter-State outward supply** (case i) is barred because composition dealers pay a *State-level* flat tax and take no ITC; letting them supply across State lines would break the destination-based IGST chain and let untaxed value cross borders — hence even a tiny inter-State sale kills eligibility. **Notified-goods manufacturers** like ice-cream (case iv) are excluded as an anti-abuse/sin measure — these are high-margin discretionary goods the government does not want under a concessional flat rate. The **service sub-limit** (case iii) lets a goods dealer provide incidental services (repairs) up to the higher of ₹5 lakh or 10% of turnover, so small mixed businesses aren't forced out, while 10(2A) extends a *separate* concessional route to pure service providers up to ₹50 lakh (case v). The exam trap is judging eligibility on *turnover alone* — but the *nature* of supply (inter-State, notified goods, excess services) is what actually governs, and a taxpayer well within the turnover ceiling can still be disqualified.

*(Full-marks tip: state each disqualifying condition and the correct rate (1% trader, 5% restaurant, 6% service-10(2A)); the standard deductions are allowing composition despite an inter-State supply or for an ice-cream manufacturer, and applying the wrong flat rate.)*

### Q85. Ch: GST – Input Tax Credit — Computation of net GST payable with Sec 17(5) blocked credits (Marks: 10) [Problem]
**Question:** M/s Vaibhav Enterprises, a registered manufacturer at Pune (Maharashtra), furnishes the following particulars for the month of October 2025. All figures are exclusive of GST; assume a uniform rate of 18% (9% CGST + 9% SGST) on all intra-State supplies and 18% IGST on inter-State supplies, unless a different rate is indicated. All inward suppliers are registered, tax invoices are on record, and goods/services have been received. Compute the net GST payable in cash for October 2025.

| Particulars | Value (₹) | Nature |
|---|---|---|
| Intra-State taxable outward supply of goods | 40,00,000 | Output |
| Inter-State taxable outward supply of goods | 15,00,000 | Output |
| Raw material purchased intra-State | 22,00,000 | Inward |
| Inter-State purchase of raw material | 8,00,000 | Inward |
| Motor car (seating capacity 5, for use of GM) purchased intra-State | 12,00,000 | Inward |
| General insurance & repairs of the above motor car | 1,00,000 | Inward |
| Membership of a club for employees (intra-State) | 2,00,000 | Inward |
| Goods given as free samples to dealers (intra-State inward, later distributed free) | 1,50,000 | Inward |
| Inputs used in manufacture, but 5% destroyed in fire | 5,00,000 | Inward |
| Rent paid on factory building (intra-State) | 3,00,000 | Inward |

Opening balance of ITC: CGST ₹40,000; SGST ₹40,000; IGST ₹1,10,000.

**Solution:**

**WN-1 — Output tax liability**
- Intra-State supply ₹40,00,000 × 9% = CGST ₹3,60,000; SGST ₹3,60,000.
- Inter-State supply ₹15,00,000 × 18% = IGST ₹2,70,000.

**WN-2 — Eligibility of ITC (Sec 16 & Sec 17(5))**

| Inward item | Value (₹) | Eligible? | Reason |
|---|---|---|---|
| Raw material (intra) 22,00,000 | 22,00,000 | Yes | Used in course/furtherance of business |
| Raw material (inter) 8,00,000 | 8,00,000 | Yes | Same |
| Motor car (≤13 seats) 12,00,000 | — | **Blocked** — Sec 17(5)(a) | Not used for further supply/transport of passengers/driving training |
| Insurance & repairs of that car 1,00,000 | — | **Blocked** — Sec 17(5)(ab) | Follows the blocked car |
| Club membership 2,00,000 | — | **Blocked** — Sec 17(5)(b)(ii) | Membership of club/health/fitness centre |
| Free samples 1,50,000 | — | **Blocked** — Sec 17(5)(h) | ITC on goods disposed of by way of gift/free sample must be reversed |
| Inputs destroyed in fire (5% of 5,00,000 = 25,000) | 4,75,000 eligible | 25,000 **blocked** — Sec 17(5)(h) | ITC on goods lost/destroyed reversed |
| Factory rent 3,00,000 | 3,00,000 | Yes | Business use, not immovable-property construction |

**WN-3 — Eligible ITC computation**

| Eligible inward (intra) | Value (₹) | CGST @9% | SGST @9% |
|---|---|---|---|
| Raw material | 22,00,000 | 1,98,000 | 1,98,000 |
| Inputs (net, 4,75,000) | 4,75,000 | 42,750 | 42,750 |
| Factory rent | 3,00,000 | 27,000 | 27,000 |
| **Total intra-State ITC** | | **2,67,750** | **2,67,750** |

Inter-State eligible ITC: ₹8,00,000 × 18% = IGST **₹1,44,000**.

**WN-4 — Add opening ITC**
- CGST: 2,67,750 + 40,000 = ₹3,07,750
- SGST: 2,67,750 + 40,000 = ₹3,07,750
- IGST: 1,44,000 + 1,10,000 = ₹2,54,000

**WN-5 — Set-off (Sec 49, Rule 88A: IGST credit first fully utilised, then CGST against CGST, SGST against SGST; CGST cannot pay SGST)**

IGST liability ₹2,70,000 → set off IGST credit ₹2,54,000 → balance IGST liability ₹16,000 (payable in cash, since CGST/SGST credit cannot cross to IGST after IGST credit exhausted? — it can: after IGST credit, IGST liability may be paid using CGST/SGST credit). Use CGST credit ₹16,000 for remaining IGST.

| Statement of net GST payable in cash — October 2025 | CGST (₹) | SGST (₹) | IGST (₹) |
|---|---|---|---|
| Output liability | 3,60,000 | 3,60,000 | 2,70,000 |
| Less: IGST credit (2,54,000) applied to IGST first | — | — | (2,54,000) |
| Balance IGST | — | — | 16,000 |
| Less: CGST credit to remaining IGST | — | — | (16,000) |
| CGST credit left (3,07,750 − 16,000) | (2,91,750) | — | — |
| SGST credit | — | (3,07,750) | — |
| **Net payable in cash** | **68,250** | **52,250** | **Nil** |

**Answer:** Net GST payable in cash for October 2025 — **CGST ₹68,250, SGST ₹52,250, IGST Nil; total ₹1,20,500.**

**Why this way (the reasoning):** ITC is the spine of GST — it removes cascading only for credits actually linked to taxable business supplies. Sec 17(5) carves out a "negative list" precisely for items prone to personal consumption or where the value chain breaks. A motor car ≤13 seats is presumed to have a personal-use element, so its credit (and downstream insurance/repairs under 17(5)(ab)) is blocked unless the assessee is in the business of supplying/transporting vehicles. Free samples and goods destroyed give no taxable outward supply, so allowing their credit would let tax "leak" out untaxed — hence 17(5)(h) reversal. The set-off order matters for cash: IGST credit is a "common pool" usable against any head, and Rule 88A forces it to be exhausted first; CGST credit can never discharge SGST (and vice-versa) because they accrue to different governments. Students who wrongly claim the car/club credit inflate ITC and understate cash payable — the trap is treating "used in business" as sufficient when Sec 17(5) overrides Sec 16.

*(Full-marks tip: Examiners reward a separate eligibility table citing the exact clause of 17(5) for each rejection, and correct Rule 88A cross-utilisation. Common deductions: allowing car/insurance credit, forgetting to reverse the 5% destroyed inputs, and using CGST credit to pay SGST.)*

---

### Q86. Ch: GST – Registration — Aggregate turnover & liability to register (Marks: 8) [Case/Application]
**Question:** Mr. Ramesh, based in Jaipur (Rajasthan, a non-special-category State), is engaged exclusively in the intra-State supply of goods. During FY 2025-26 his receipts are: taxable supplies ₹18,00,000; exempt supplies of agricultural produce ₹6,00,000; export of goods (zero-rated) ₹4,00,000; inward supplies on which he pays tax under reverse charge ₹3,00,000; and interest earned on a fixed deposit ₹2,50,000. He argues he need not register because his "taxable turnover" is only ₹18 lakh, below ₹40 lakh. Examine the validity of his stand and determine whether he is liable to register.

**Answer:**
**Governing law:** Sec 22(1) read with Sec 2(6) (definition of "aggregate turnover") and the threshold notification. For a supplier engaged **exclusively in supply of goods** in a normal-category State, the threshold for compulsory registration is **₹40 lakh** (₹20 lakh for services / special-category States).

**Aggregate turnover (Sec 2(6))** = value of all taxable supplies + exempt supplies + exports + inter-State supplies of persons having the same PAN, computed on all-India basis, **excluding** CGST/SGST/IGST/cess **and excluding** the value of inward supplies on which tax is paid under reverse charge.

**Computation of aggregate turnover:**

| Particulars | Included? | Value (₹) |
|---|---|---|
| Taxable supplies | Yes | 18,00,000 |
| Exempt supplies (agricultural produce) | Yes (exempt is included) | 6,00,000 |
| Export of goods (zero-rated) | Yes | 4,00,000 |
| Interest on FD (exempt service under Notification 12/2017) | Yes, but... see note | — |
| Inward RCM supplies | **Excluded** | — |
| **Aggregate turnover** | | **28,00,000** |

**Note on interest:** Interest on deposits/loans is an exempt supply of service; however, for computing the threshold for a **goods** supplier, the CBIC has clarified interest earned is to be included in aggregate turnover as exempt supply. Even so, whether interest (₹2,50,000) is added or not:
- If excluded → aggregate turnover ₹28,00,000.
- If included → ₹30,50,000.

Either way the turnover is **below ₹40 lakh**, so on the face of it he is not liable under Sec 22. **BUT** — Mr. Ramesh's stand that only "taxable turnover of ₹18 lakh" matters is **wrong in principle**: the law tests **aggregate turnover**, which pulls in exempt and export supplies too, and his aggregate is ₹28-30.5 lakh.

**Twist — the trap:** He is a person **liable to pay tax under reverse charge** (₹3,00,000 inward RCM). Under **Sec 24(iii)**, a person required to pay tax under reverse charge must obtain registration **compulsorily, irrespective of the threshold**. Section 24 begins with a non-obstante clause overriding Sec 22(1).

**Conclusion/Advice:** Mr. Ramesh's reasoning is invalid on two counts. First, the correct test is aggregate turnover (₹28 lakh+), not taxable turnover. Second, and decisively, because he pays tax under reverse charge, **Sec 24(iii) makes registration compulsory regardless of any threshold** — he **must register**.

**Why this way (the reasoning):** Aggregate turnover is deliberately defined widely so that a person cannot fragment supplies into "exempt" or "export" buckets to duck the threshold — the law wants the true scale of a person's economic activity. But the real principle here is the hierarchy of provisions: Sec 24 is a **non-obstante override** of the threshold in Sec 22. The mischief it addresses is that reverse-charge and other specified situations create tax collection/compliance obligations that cannot be left unmonitored merely because turnover is small — an unregistered person paying RCM would otherwise sit outside the return system with no way to be tracked. The tempting wrong answer stops at "₹28 lakh < ₹40 lakh, not liable"; it fails because it never checks Sec 24, which is where the exam mark lies.

*(Full-marks tip: State both the aggregate-turnover computation AND the Sec 24 override — the marks are split. The classic deduction is concluding "not liable" after only the threshold test, missing the RCM compulsory-registration trap.)*

---

### Q87. Ch: GST – Input Tax Credit — Rule 42 apportionment (common credit, taxable vs exempt) (Marks: 8) [Problem]
**Question:** M/s Sunrise Textiles is a registered person making both taxable and exempt supplies. For the month of November 2025 the following ITC data is available. Compute the ITC to be credited to the electronic credit ledger and the common credit to be reversed under **Rule 42** of the CGST Rules.

| Particulars | Amount of ITC (₹) |
|---|---|
| Total input tax on inputs & input services (T) | 6,00,000 |
| Inputs/input services used exclusively for non-business purposes (T1) | 40,000 |
| Inputs/input services used exclusively for exempt supplies (T2) | 60,000 |
| Input tax on which credit is blocked u/s 17(5) (T3) | 30,000 |
| Inputs/input services used exclusively for taxable supplies incl. zero-rated (T4) | 3,20,000 |

Turnover for November: exempt supplies ₹20,00,000; total turnover ₹80,00,000.

**Solution:**

**WN-1 — Credit attributable to business & apportionable (Rule 42)**
Formula per Rule 42(1):
- **C1 = T − (T1 + T2 + T3)** = 6,00,000 − (40,000 + 60,000 + 30,000) = **₹4,70,000** (credited to electronic credit ledger).
- **C2 = C1 − T4** (common credit) = 4,70,000 − 3,20,000 = **₹1,50,000**.

**WN-2 — Reversal of common credit**
- **D1 (attributable to exempt supplies)** = (E ÷ F) × C2, where E = exempt turnover ₹20,00,000, F = total turnover ₹80,00,000.
  D1 = (20,00,000 ÷ 80,00,000) × 1,50,000 = 0.25 × 1,50,000 = **₹37,500**.
- **D2 (deemed non-business, 5% of common credit)** = 5% × C2 = 5% × 1,50,000 = **₹7,500**.

**WN-3 — Eligible common credit**
- **C3 = C2 − (D1 + D2)** = 1,50,000 − (37,500 + 7,500) = **₹1,05,000** (remains in credit ledger).

| Statement showing Rule 42 apportionment — Nov 2025 | Amount (₹) |
|---|---|
| Total ITC (T) | 6,00,000 |
| Less: T1 + T2 + T3 (ineligible/exclusive) | 1,30,000 |
| C1 credited to ledger | 4,70,000 |
| Less: T4 (exclusive taxable) | 3,20,000 |
| Common credit C2 | 1,50,000 |
| Less: D1 (exempt-attributable) | 37,500 |
| Less: D2 (5% deemed non-business) | 7,500 |
| Eligible common credit C3 | 1,05,000 |

**Answer:** ITC to be **reversed** (added to output tax liability) under Rule 42 = **D1 + D2 = ₹45,000**. Eligible ITC retained from common credit (C3) = **₹1,05,000**; ITC exclusively for taxable supplies (T4) = ₹3,20,000; total eligible ITC = **₹4,25,000**.

**Why this way (the reasoning):** Rule 42 exists because ITC is allowed **only to the extent** inputs feed taxable (including zero-rated) outward supplies — credit tied to exempt or non-business use must be stripped out, otherwise the exempt output would be under-taxed at the expense of revenue. The rule first removes the "clean" buckets (T1 non-business, T2 exempt, T3 blocked, T4 pure-taxable) that need no apportionment, leaving only the genuinely **common** credit C2 that serves both streams. That common pool is then split by the turnover ratio (E/F), the fairest proxy for how much of the shared input actually supported exempt output, plus a flat 5% deeming for personal/non-business seepage. Students often wrongly apply the E/F ratio to the **whole** ITC (T) rather than to C2 — that double-counts the exclusive buckets and grossly over-reverses. The logic is: only what is genuinely shared gets apportioned.

*(Full-marks tip: Show the C1→C2→C3 chain with each symbol labelled, and state that D1+D2 is added to output liability with interest if the annual reconciliation under Rule 42(2) later shows a shortfall. Deduction: applying the exempt-ratio to total ITC instead of common credit.)*

---

### Q88. Ch: GST – Tax Invoice, Payment & Returns — Time limit & consequences of invoicing (Marks: 6) [Case/Application]
**Question:** M/s Orbit Consultants (registered, Delhi) supplies management-consultancy services. It completed a project on 5 November 2025, but issued the tax invoice only on 20 December 2025. Separately, on a supply of goods to a customer in Gurugram (Haryana) despatched on 8 November 2025, it raised the invoice on 15 November 2025 after the goods had already been removed. The accountant believes "there is no time limit for issuing invoices as long as tax is paid." Examine the validity of the invoices and the accountant's belief, and state the consequences.

**Answer:**
**Governing law:** Sec 31 of the CGST Act read with Rules 47 & 48 (CGST Rules).

**(a) Supply of services — Sec 31(2) r/w Rule 47:** A tax invoice for services must be issued **within 30 days** from the date of supply of service (45 days for banks/NBFCs/insurers). Here the service was completed on 5 November 2025; the 30-day window ended **5 December 2025**. The invoice dated 20 December 2025 is issued **beyond 30 days** — it is **not a valid tax invoice** in point of time.

Consequence — **time of supply, Sec 13(2):** Where the invoice is **not** issued within the prescribed period, the time of supply of services is the **date of provision of service** (or date of receipt of payment, whichever earlier), i.e. **5 November 2025** — not the invoice date. So GST becomes payable with reference to November 2025, and delay in remitting attracts interest u/s 50, plus the late invoice is a contravention exposing the supplier to a general penalty u/s 122/125.

**(b) Supply of goods — Sec 31(1) r/w Rule 47:** For goods involving **movement**, the invoice must be issued **before or at the time of removal** of goods for supply. Here goods were removed on 8 November 2025 but the invoice was raised on 15 November 2025 — **after removal**. This **violates Sec 31(1)(a)**: the invoice is late, goods moved without a valid tax invoice (and, if applicable, without proper e-way-bill documentation), exposing the consignment to detention u/s 129 and penalty.

**Conclusion:** The accountant's belief is **invalid**. Sec 31 prescribes strict outer time limits — 30 days for services and "before/at removal" for goods. Both invoices are time-defective; the services invoice merely shifts time of supply to 5 November (interest exposure), while the goods invoice is a substantive violation risking detention/penalty. Timely invoicing is mandatory even if tax is ultimately paid.

**Why this way (the reasoning):** The invoice is not a formality — it is the **document that fixes the time of supply and triggers the recipient's ITC**. For goods, tax is meant to attach to the movement itself, so the invoice must accompany removal; otherwise goods could circulate untaxed and the audit trail breaks — hence the "before or at removal" rule and the harsh Sec 129 detention regime. For services (intangible, no physical movement), the law gives a reasonable 30-day window but pins the time of supply back to the service date if you miss it, so a supplier cannot defer liability simply by delaying the invoice. The accountant's "no time limit if tax paid" view fails because the statute ties **when** tax is due to the invoice timing itself, and late invoicing independently attracts penalty regardless of eventual payment.

*(Full-marks tip: Separate the goods and services limbs, quote Sec 31(1)/(2) and the Sec 13(2)/12(2) time-of-supply fallback. The common deduction is treating both alike or forgetting that a missed services window shifts time of supply to the service-completion date.)*

---

### Q89. Ch: GST – Input Tax Credit — Sec 17(5) blocked credits, examine validity (Marks: 6) [Case/Application]
**Question:** M/s Elite Constructions Ltd., a registered works-contract company, claims ITC on the following in December 2025. Examine the eligibility of each and comment on the validity of the claim, citing the relevant clause of Sec 17(5).

| # | Inward supply | ITC claimed (₹) |
|---|---|---|
| 1 | Works-contract service received for constructing a new office building (own use, capitalised) | 5,40,000 |
| 2 | Works-contract service received for constructing a shopping mall which the company will let out on rent (taxable supply) | 9,00,000 |
| 3 | Cement, steel and other materials procured to construct the same office building on own account | 3,60,000 |
| 4 | Rent-a-cab service to ferry employees (not obligatory under any law) | 45,000 |
| 5 | Food and beverages for the annual company function | 60,000 |

**Answer:**
**Governing law:** Sec 17(5)(c), (d), (b) of the CGST Act.

| # | Item | Eligible? | Clause & reasoning |
|---|---|---|---|
| 1 | Works contract for own office building | **Blocked** | Sec 17(5)(c): works-contract service for construction of **immovable property** (other than plant & machinery) is blocked, except where it is an input service for further supply of works contract. Office for own use is not onward WC supply → blocked. |
| 2 | Works contract for shopping mall to be let out | **Blocked (per CGST Act)** | Sec 17(5)(d): goods/services received for construction of immovable property **on own account** are blocked even if used in business. (Note: the *Safari Retreats* line of reasoning on "plant" is contested; strictly per the Act as amended, credit on own-account construction of a building intended for letting is blocked.) |
| 3 | Cement/steel for own office building | **Blocked** | Sec 17(5)(d): goods received for construction of immovable property on own account, capitalised → blocked. |
| 4 | Rent-a-cab (not legally obligatory) | **Blocked** | Sec 17(5)(b)(i): leasing/renting/hiring of motor vehicles for transport of persons is blocked unless used for the specified onward purposes or the employer is obligated under law to provide it. Here not obligatory → blocked. |
| 5 | Food & beverages (company function) | **Blocked** | Sec 17(5)(b)(i): food and beverages blocked unless used for onward taxable supply of the same category or obligatory under law → blocked. |

**Conclusion:** **All five claims are invalid** — the entire ₹19,05,000 ITC is blocked under Sec 17(5). The company must not credit these to its electronic credit ledger.

**Why this way (the reasoning):** The construction blocks in 17(5)(c)/(d) rest on a deliberate policy: an immovable property, once built, exits the GST value chain — it is not "supplied" again as goods — so allowing credit on its construction would break the chain and hand a windfall to real-estate. The legislature therefore blocks credit on both the works-contract service (c) and self-procured materials (d) when the result is a building held on own account, capitalised. The only escape is when construction feeds a **further** works-contract supply (a builder building for a client), because then the chain continues. For rent-a-cab and food/beverages, the rationale is the personal-consumption presumption and the risk of employers routing lifestyle perks through the credit system; the law relents only where the same-category onward supply exists or a **statutory obligation** compels the employer to provide the benefit. The tempting wrong view — "the mall is let out on taxable rent, so credit should flow" — is exactly what 17(5)(d) overrides for own-account construction; students must recognise that "used for business/taxable output" does not defeat a 17(5) block.

*(Full-marks tip: Cite the precise sub-clause for each item and note the "obligatory under law" and "onward supply of same category" exceptions. Deduction: allowing credit on the mall because rent is taxable, ignoring the own-account construction bar.)*

---

### Q90. Ch: GST – Registration — Compulsory registration u/s 24 (Marks: 5) [Case/Application]
**Question:** Determine, with reasons, whether registration is compulsory (irrespective of the threshold) for each of the following persons, citing the relevant clause of Sec 24 of the CGST Act:

| # | Person / situation |
|---|---|
| 1 | Mr. A, a supplier in Rajasthan making inter-State taxable supply of goods worth ₹6,00,000 in the year |
| 2 | Mr. B, an agent supplying goods on behalf of his principal |
| 3 | Ms. C, running an e-commerce operation, required to collect tax at source (TCS) |
| 4 | Mr. D, an Input Service Distributor |
| 5 | Mr. E, providing online information database access & retrieval (OIDAR) services from outside India to unregistered persons in India |

**Answer:**
**Governing law:** Sec 24 — categories of persons required to register **compulsorily notwithstanding the threshold in Sec 22(1)**.

| # | Person | Compulsory? | Clause & reasoning |
|---|---|---|---|
| 1 | Inter-State supplier of **goods** | **Yes** | Sec 24(i): persons making any inter-State taxable supply must register regardless of turnover. (Note: a *services* supplier gets a ₹20 lakh relief under Notification 10/2017, but goods do not — so ₹6 lakh inter-State goods → must register.) |
| 2 | Agent supplying on behalf of principal | **Yes** | Sec 24(vii): persons who supply goods/services on behalf of other taxable persons whether as agent or otherwise. |
| 3 | E-commerce operator liable to collect TCS | **Yes** | Sec 24(x): every electronic commerce operator required to collect tax at source u/s 52. |
| 4 | Input Service Distributor | **Yes** | Sec 24(viii): ISD must register separately, whether or not separately registered under the Act. |
| 5 | OIDAR supplier from outside India to unregistered recipients | **Yes** | Sec 24(xi): every person supplying OIDAR services from a place outside India to an unregistered person in India. |

**Conclusion:** **All five** are compulsorily liable to register under Sec 24 irrespective of any turnover threshold.

**Why this way (the reasoning):** Section 24 is a **non-obstante override** — it begins "Notwithstanding anything in sub-section (1) of section 22" — because each listed category creates a tax-collection or place-of-supply concern that the small-supplier threshold cannot be allowed to shield. Inter-State goods movement (i) engages IGST and cross-border revenue apportionment between States, so it must be captured from rupee one. Agents (vii) hold and pass on someone else's supplies, so leaving them unregistered would create an untracked link. E-commerce operators (x) and ISDs (viii) are conduits collecting/distributing tax for others — their registration is essential to the mechanics of TCS and credit distribution. OIDAR from abroad (xi) is registered so India can tax digital services consumed here despite the supplier being offshore. The unifying principle: wherever a person sits at a **collection, distribution, or cross-jurisdiction node** of the tax chain, the threshold exemption is withdrawn because visibility and revenue integrity outweigh small-supplier relief.

*(Full-marks tip: Cite the exact clause number of Sec 24 for each — bare "yes/no" earns little. Watch the goods-vs-services distinction on inter-State supply: services below ₹20 lakh are exempt, goods are not.)*

---

### Q91. Ch: GST – Tax Invoice, Payment & Returns — Return filing, late fee & consequences (Marks: 6) [Case/Application]
**Question:** M/s Zenith Traders (registered, monthly filer, Karnataka) filed its GSTR-3B for October 2025 (due 20 November 2025) only on 5 December 2025. Its self-assessed tax for October was: CGST ₹1,20,000, SGST ₹1,20,000, of which ₹80,000 (CGST+SGST combined) was to be paid in cash and the rest through ITC. It also filed GSTR-1 for October (due 11 November 2025) on 5 December 2025. Its total turnover in the preceding year was ₹3 crore. Examine the consequences: late fee, interest, and the impact on its recipients' ITC.

**Answer:**
**Governing law:** Sec 47 (late fee), Sec 50 (interest), Sec 37/39 (returns), Sec 16(2)(aa) & Rule 36(4)/GSTR-2B mechanism.

**(1) Late fee — GSTR-3B (Sec 47):** Late fee is ₹50 per day (₹25 CGST + ₹25 SGST) for a return with tax liability, subject to a cap. Delay = 21 November to 5 December = **15 days**.
Late fee = 15 × ₹50 = **₹750** (₹375 CGST + ₹375 SGST), within the cap for a taxpayer with turnover up to ₹5 crore.

**(2) Late fee — GSTR-1 (Sec 47):** Delay 12 November to 5 December = **24 days** × ₹50 = **₹1,200** (₹600 + ₹600), subject to cap.

**(3) Interest u/s 50(1):** Interest at **18% p.a.** is chargeable on the **net cash** portion of tax paid late (proviso to Sec 50(1): interest on delayed filing is only on the amount paid through the electronic **cash** ledger, provided the return is filed after the due date and no proceedings u/s 73/74 are initiated). Net cash tax = ₹80,000; delay 15 days.
Interest = 80,000 × 18% × 15/365 = **₹591.78 ≈ ₹592**.
(The ITC-funded portion of the liability does **not** attract interest, per the proviso to Sec 50(1).)

**(4) Impact on recipients' ITC (Sec 16(2)(aa)):** A recipient can avail ITC only if the invoice appears in its **GSTR-2B**, which is generated from the supplier's GSTR-1. Because Zenith filed GSTR-1 for October only on 5 December, its invoices will reflect in the recipients' GSTR-2B of the **November** period (generated after the filing) — so recipients get their ITC **one month later**, delaying their own credit and possibly forcing cash payment in the interim.

**Conclusion:** Zenith bears late fee of **₹750 (3B) + ₹1,200 (1) = ₹1,950**, interest of **≈ ₹592** on the ₹80,000 cash portion, and inconveniences its customers by pushing their ITC to the next month's 2B.

**Why this way (the reasoning):** GST is a self-assessment, return-driven system where the return is both the payment vehicle and the data feed for everyone downstream. Late fee (Sec 47) is a fixed per-day levy to enforce timeliness independent of tax involved — hence it applies even to nil/ITC-funded returns. Interest (Sec 50), by contrast, compensates the exchequer only for **money withheld**; the 2021 proviso wisely restricts it to the cash-paid portion, because the ITC portion was already sitting with the government as tax collected upstream — charging interest on it would be double recovery. The recipient-ITC angle reflects the **invoice-matching philosophy**: since 16(2)(aa), credit is anchored to what the supplier actually reports in GSTR-1/2B, so a supplier's delay is not just its own problem — it ripples to customers' cash flow. That interconnection is the deeper lesson: one late GSTR-1 freezes credit across the chain.

*(Full-marks tip: Compute interest only on the net cash liability (the proviso) — charging 18% on the full ₹2,40,000 is the classic over-statement. Mention the GSTR-1 → 2B linkage for the recipient-impact mark.)*

---

### Q92. Ch: GST – Input Tax Credit — Sec 16(2) conditions & 180-day reversal (Marks: 8) [Problem]
**Question:** M/s Crest Ltd. (registered, Tamil Nadu) provides the following ITC-related transactions for the quarter. Determine the ITC admissible/reversible and explain the treatment, applying Sec 16(2) conditions and the second proviso (180-day rule).

| # | Transaction | ITC (₹) |
|---|---|---|
| 1 | Purchase of goods on 10 Sep 2025; invoice received, but goods received in two lots — first lot 25 Sep 2025, second (final) lot 8 Oct 2025 | 1,00,000 |
| 2 | Services invoiced 1 Aug 2025; ITC availed; consideration not paid to supplier till 15 Feb 2026 | 90,000 |
| 3 | Purchase invoice dated 12 Sep 2025, appearing in GSTR-2B of Sep; goods received but supplier has not filed GSTR-1 so it does NOT appear in 2B | 50,000 |
| 4 | Capital goods invoice on which depreciation claimed on the **tax component** under Income-tax Act | 70,000 |

**Answer:**
**Governing law:** Sec 16(2)(a)–(d), first proviso (goods in lots), second proviso (180-day payment rule), and Sec 16(3) (depreciation bar).

**Item 1 — Goods received in lots (first proviso to Sec 16(2)):** Where goods are received in instalments/lots against a single invoice, ITC is admissible **only on receipt of the last lot**. The last lot arrived 8 October 2025 → full ITC of **₹1,00,000 admissible in October 2025**, not September. No partial credit on the first lot.

**Item 2 — 180-day payment rule (second proviso to Sec 16(2)):** Recipient must pay the supplier the **value + tax** within **180 days** from the invoice date; else the ITC availed is added back to output liability with interest, and re-availed on later payment. Invoice 1 Aug 2025 → 180 days ends **≈ 28 Jan 2026**. Payment made only 15 Feb 2026 (beyond 180 days). Therefore ITC of **₹90,000 must be reversed** (added to output tax with interest) in the period the 180 days expire, and **re-availed** in Feb 2026 when paid. Net effect: temporary reversal + interest for the gap.

**Item 3 — Sec 16(2)(aa)/(ba) & Rule 36(4):** ITC can be availed only if the invoice **appears in the recipient's GSTR-2B** (i.e., supplier has furnished details in GSTR-1). Here the supplier has not filed GSTR-1, so it is **absent from 2B** → **ITC of ₹50,000 is NOT admissible** currently, even though goods are received and invoice held. Credit becomes available only when the supplier reports it and it flows into 2B.

**Item 4 — Depreciation on tax component (Sec 16(3)):** If depreciation under the Income-tax Act is claimed on the **tax component** of the cost of capital goods, **ITC on that tax component is not allowed**. Since Crest claimed depreciation on the ₹70,000 tax, **ITC of ₹70,000 is disallowed**.

| Statement of admissible ITC — quarter | ₹ | Status |
|---|---|---|
| Item 1 goods (last lot Oct) | 1,00,000 | Admissible (Oct) |
| Item 2 services | 90,000 | Reverse now, re-avail on payment |
| Item 3 not in 2B | 50,000 | Not admissible (till in 2B) |
| Item 4 depreciation on tax | 70,000 | Permanently disallowed |

**Answer:** Currently admissible ITC = **₹1,00,000** (Item 1, in October); Item 2 is reversible-and-re-available; Items 3 and 4 are **not admissible** (Item 3 deferred, Item 4 permanently lost).

**Why this way (the reasoning):** Section 16(2) sets **cumulative** conditions — possession of invoice, receipt of goods/services, tax actually reaching the government (via supplier's GSTR-1/2B), and filing of the recipient's return — every one must be satisfied, because ITC is fundamentally a claim on tax that has actually been paid up the chain. The lot rule reflects that "receipt of goods" is complete only when the whole consignment arrives; giving credit on a part-received invoice would advance credit against goods not yet in hand. The 180-day rule polices the reality that ITC represents tax the supplier will remit only when paid — if the recipient never pays, the supplier may not remit, so the credit is clawed back to protect the chain, then restored once payment (and thus the supplier's incentive to remit) happens. The 2B condition (16(2)(aa)) hard-wires the matching principle: no supplier reporting, no credit. And Sec 16(3) prevents a **double benefit** — you cannot both depreciate the tax and claim it as ITC. Each rule guards a different leak point.

*(Full-marks tip: Time Item 1 to the last-lot month, treat Item 2 as reverse-then-re-avail (not permanent loss), and flag Item 3 as merely deferred while Item 4 is a permanent double-benefit bar. Deduction: crediting Item 1 in September or treating Item 2 as a permanent disallowance.)*

---

### Q93. Ch: GST – Tax Invoice, Payment & Returns — Electronic ledgers & order of set-off (Marks: 8) [Problem]
**Question:** M/s Peak Industries (registered, Gujarat) has the following position for December 2025. Determine the manner of utilisation of ITC and the tax payable in cash, applying Sec 49, Sec 49A/49B and Rule 88A (order and manner of utilisation), and comment on the mandatory sequence.

| Head | Output tax liability (₹) | ITC available (₹) |
|---|---|---|
| IGST | 1,00,000 | 3,00,000 |
| CGST | 2,50,000 | 1,50,000 |
| SGST | 2,50,000 | 1,50,000 |

**Solution:**

**WN-1 — Rule of utilisation (Sec 49A r/w Rule 88A):**
(i) IGST credit must be utilised **first** in full, against IGST, then CGST/SGST **in any order and any proportion**, before any CGST or SGST credit is used.
(ii) CGST credit can be used for IGST then CGST — **never for SGST**.
(iii) SGST credit can be used for IGST then SGST — **never for CGST**.

**WN-2 — Apply IGST credit (₹3,00,000):**
- Against IGST liability ₹1,00,000 → IGST credit left ₹2,00,000.
- Remaining IGST credit ₹2,00,000 may be split against CGST and SGST in any order. Optimal split to avoid cash blockage: apply ₹1,00,000 to CGST and ₹1,00,000 to SGST.
  - CGST liability 2,50,000 − 1,00,000 (IGST cr) = ₹1,50,000 remaining.
  - SGST liability 2,50,000 − 1,00,000 (IGST cr) = ₹1,50,000 remaining.

**WN-3 — Apply own-head credit:**
- CGST credit ₹1,50,000 → against remaining CGST ₹1,50,000 → CGST liability Nil.
- SGST credit ₹1,50,000 → against remaining SGST ₹1,50,000 → SGST liability Nil.

| Statement of ITC utilisation & cash payable — Dec 2025 | IGST | CGST | SGST |
|---|---|---|---|
| Output liability | 1,00,000 | 2,50,000 | 2,50,000 |
| Less: IGST credit | (1,00,000) | (1,00,000) | (1,00,000) |
| Less: CGST credit | — | (1,50,000) | — |
| Less: SGST credit | — | — | (1,50,000) |
| **Cash payable** | **Nil** | **Nil** | **Nil** |

**Answer:** By fully exhausting IGST credit first and splitting it optimally across CGST and SGST, **tax payable in cash is Nil** for all three heads; IGST credit is completely used, and CGST/SGST credits exactly discharge the residual same-head liabilities.

**Why this way (the reasoning):** The set-off order is not arbitrary — it protects **inter-governmental revenue settlement**. IGST is a shared/central pool that gets apportioned to States; forcing IGST credit to be used first (Sec 49A, Rule 88A) prevents taxpayers from hoarding IGST credit while paying CGST/SGST in cash, which would distort the CGST-vs-SGST balance owed to the Centre and the State. The strict wall — CGST credit can never touch SGST and vice-versa — exists because those two taxes belong to **different governments**; letting one fund the other would silently transfer money between the Centre and a State. The optimisation twist is that once IGST credit's mandatory first-use is done, the taxpayer may split the leftover IGST credit between CGST and SGST in **any proportion**, so a smart split (equal here) avoids cash outgo in one head while credit lies idle in another. A student who applies all leftover IGST credit to CGST only would zero out CGST but still owe SGST cash while SGST credit sat unused — the balanced split is what achieves nil cash.

*(Full-marks tip: State the Rule 88A first-use rule and demonstrate the optimal IGST-credit split. Deduction: using CGST credit against SGST, or exhausting IGST credit lopsidedly and leaving a cash liability that a balanced split would have avoided.)*

---

### Q94. Ch: GST – Input Tax Credit — Rule 43 apportionment on capital goods (Marks: 8) [Problem]
**Question:** M/s Nova Ltd. (registered, making both taxable and exempt supplies) purchased a machine on 10 October 2025 for ₹40,00,000 plus IGST ₹7,20,000. The machine is used **commonly** for both taxable and exempt supplies. Compute the common credit attributable to exempt supplies to be reversed under **Rule 43** for the tax period October 2025. Turnover for October: exempt ₹15,00,000; total ₹60,00,000. The useful life of the capital goods is taken as 5 years (60 months) per Rule 43.

**Solution:**

**WN-1 — Nature of credit:** The machine is used **commonly** for taxable and exempt supplies (not exclusively for either), so it is "A" — common capital-goods credit apportioned over its useful life.
Total ITC on machine (Tc) = IGST **₹7,20,000**. This is credited to the electronic credit ledger.

**WN-2 — Common credit and monthly attribution (Rule 43):**
- Useful life = 60 months; the common credit is spread over 60 months.
- Monthly common credit (Tm) = Tc ÷ 60 = 7,20,000 ÷ 60 = **₹12,000 per month**.
- Tr (aggregate Tm of all such common capital goods whose useful life remains) for October = ₹12,000 (only this machine).

**WN-3 — Reversal attributable to exempt supplies (Te):**
Te = (E ÷ F) × Tr, where E = exempt turnover ₹15,00,000, F = total turnover ₹60,00,000.
Te = (15,00,000 ÷ 60,00,000) × 12,000 = 0.25 × 12,000 = **₹3,000**.

| Statement of Rule 43 reversal — October 2025 | Amount (₹) |
|---|---|
| Total ITC on common capital goods (Tc) | 7,20,000 |
| Monthly credit over 60 months (Tm = Tr) | 12,000 |
| Exempt turnover ratio (E ÷ F) | 0.25 |
| ITC attributable to exempt supplies (Te) — reversed | 3,000 |
| Net eligible common capital-goods credit for the month | 9,000 |

**Answer:** ITC of **₹3,000** is to be **added to output tax liability** for October 2025 as the exempt-attributable reversal under Rule 43; ₹9,000 is retained. This exercise repeats every month for the remaining useful life (with the current month's turnover ratio), i.e., ₹12,000/month is apportioned for 60 months.

**Why this way (the reasoning):** Rule 43 applies the same "credit only for taxable use" principle as Rule 42, but capital goods are **durable** — they serve output over years, so the credit cannot be reversed in one shot on the turnover of a single month; that would either over- or under-reverse depending on that month's mix. Instead the law deems a 5-year (60-month) useful life and slices the credit into monthly instalments (Tc ÷ 60), then applies each month's own exempt-to-total ratio to that month's slice. This matches the reversal to the actual pattern of exempt usage over the asset's life — a fairer, more accurate apportionment. The common error is to apply the E/F ratio to the **whole** ₹7,20,000 in the purchase month (₹1,80,000 reversal), which wildly over-reverses; the monthly-slice mechanism is the entire point of Rule 43. Also note: had the machine been used **exclusively** for exempt supplies, the full credit would be blocked upfront; exclusively taxable, fully allowed — Rule 43's apportionment engages only for **common** use.

*(Full-marks tip: Divide ITC by 60 first, then apply the exempt ratio to the monthly slice — not to the full credit. State that the reversal recurs monthly using each period's turnover. Deduction: one-shot reversal on full ITC.)*

---

### Q95. Ch: GST – Registration — Casual taxable person & non-resident taxable person (Marks: 5) [Theory]
**Question:** "A casual taxable person and a non-resident taxable person are treated differently from ordinary registrants under the GST registration scheme." Analyse the special registration provisions applicable to a **casual taxable person (CTP)** and a **non-resident taxable person (NRTP)**, covering threshold, advance deposit, validity, and ITC, and explain the rationale.

**Answer:**
**Governing law:** Sec 2(20) (CTP), Sec 2(77) (NRTP), Sec 24(v) (compulsory registration), Sec 27 (validity & advance deposit).

**1. Compulsory registration (Sec 24(v)):** Both CTP and NRTP must register **compulsorily, without any threshold**. A CTP is one who occasionally supplies goods/services in a State/UT where he has **no fixed place of business** (e.g., an exhibitor at a trade fair). An NRTP supplies goods/services but has **no fixed place of business or residence in India**.

**2. Application timing:** Both must apply for registration **at least 5 days prior** to the commencement of business. An NRTP applies using a **self-attested copy of a valid passport** (or, for a foreign business entity, its tax identification/unique number), and registration is not linked to PAN in the way ordinary registration is.

**3. Advance deposit of tax (Sec 27(2)):** At the time of applying, both must make an **advance deposit of tax** equal to the **estimated tax liability** for the period of registration. This deposit is credited to the electronic cash ledger.

**4. Validity (Sec 27(1)):** The registration certificate is valid for the **period specified in the application or 90 days** from the effective date, **whichever is earlier**. It may be **extended by a further period not exceeding 90 days** on request, subject to depositing additional estimated tax for the extension.

**5. ITC — the key difference:** A **CTP can avail ITC** on its inward supplies (it is otherwise like a normal registrant, just temporary). But an **NRTP cannot claim ITC** except on goods imported by it — Sec 17 read with the NRTP scheme restricts credit, because an NRTP has no ongoing Indian value chain to reconcile.

**Conclusion:** Both are registered compulsorily, both pay an advance deposit and get a time-bound 90+90 day registration; the decisive distinction is that the **CTP enjoys normal ITC** while the **NRTP's ITC is barred** (save on its own imports).

**Why this way (the reasoning):** These categories exist because the ordinary registration model assumes a **fixed, continuing presence** the department can monitor and from which it can recover dues. A CTP (say, a seasonal stall at a fair) and an NRTP (a foreign supplier with no Indian base) have **no fixed establishment** to pursue if they default and vanish after the event. The **advance tax deposit** is therefore a security — the government collects the estimated liability upfront rather than chasing an absent taxpayer later. The **90-day time-box** mirrors the transient nature of the activity. The ITC asymmetry follows from economic substance: a CTP still buys and sells within India's chain, so denying credit would cascade tax unfairly; an NRTP, by contrast, has no genuine Indian input chain to credit (its costs sit abroad), so credit is confined to its imports to prevent revenue leakage. The design is essentially **risk-based**: less permanence, more upfront security, tighter credit.

*(Full-marks tip: Cover all four axes — threshold/Sec 24, advance deposit, 90+90 validity, ITC — and nail the CTP-vs-NRTP ITC contrast, which is where marks separate a top answer.)*

---

### Q96. Ch: GST – Input Tax Credit — Comprehensive net GST payable with RCM & blocked credits (Marks: 10) [Problem]
**Question:** M/s Horizon Ltd. (registered, Maharashtra) furnishes the following for January 2026. Rates: 18% (9%+9%) on intra-State and 18% IGST on inter-State, unless stated. All conditions of Sec 16 are satisfied for eligible credits. Compute the net GST payable in cash, separately identifying tax payable under reverse charge.

| Particulars | Value (₹) |
|---|---|
| Intra-State taxable outward supply of goods | 50,00,000 |
| Inter-State taxable outward supply of services | 10,00,000 |
| Intra-State inward supply of inputs (registered supplier) | 20,00,000 |
| Legal services received from an advocate (intra-State, RCM applicable) | 4,00,000 |
| Goods transport agency (GTA) service, intra-State, tax @5% under RCM | 2,00,000 |
| Works-contract service for repair (not construction) of existing factory | 3,00,000 |
| Purchase of goods used partly (40%) for personal use of directors | 5,00,000 |
| Inter-State inward supply of inputs | 6,00,000 |

Opening ITC: CGST ₹50,000; SGST ₹50,000; IGST Nil.

**Solution:**

**WN-1 — Output tax (forward charge):**
- Intra-State supply ₹50,00,000 × 9% = CGST ₹4,50,000; SGST ₹4,50,000.
- Inter-State services ₹10,00,000 × 18% = IGST ₹1,80,000.

**WN-2 — Tax payable under reverse charge (RCM) — paid in CASH:**
- Legal (advocate) service ₹4,00,000 × 18% = CGST ₹36,000 + SGST ₹36,000 = **₹72,000**.
- GTA service ₹2,00,000 × 5% = CGST ₹5,000 + SGST ₹5,000 = **₹10,000**.
- **RCM tax payable in cash = CGST ₹41,000 + SGST ₹41,000 = ₹82,000.**
  (RCM liability **cannot** be discharged from ITC — it must be paid in cash; the recipient then takes ITC of the same, being eligible business inputs.)

**WN-3 — Eligible ITC:**

| Inward item | Value (₹) | ITC | Eligibility |
|---|---|---|---|
| Inputs (intra) | 20,00,000 | CGST 1,80,000; SGST 1,80,000 | Eligible |
| Legal service (RCM paid) | 4,00,000 | CGST 36,000; SGST 36,000 | Eligible (business input) |
| GTA (RCM paid) | 2,00,000 | CGST 5,000; SGST 5,000 | Eligible |
| WC repair of factory | 3,00,000 | CGST 27,000; SGST 27,000 | Eligible — repair (not construction), not capitalised → not blocked by 17(5)(c)/(d) |
| Goods 40% personal use | 5,00,000 | eligible only on 60% = 3,00,000 → CGST 27,000; SGST 27,000 | 40% (₹2,00,000) blocked — Sec 17(1)/17(5): not for business |
| Inputs (inter) | 6,00,000 | IGST 1,08,000 | Eligible |

**WN-4 — Total eligible ITC (incl. opening):**
- CGST: 1,80,000 + 36,000 + 5,000 + 27,000 + 27,000 + opening 50,000 = **₹3,25,000**
- SGST: same = **₹3,25,000**
- IGST: 1,08,000 + opening Nil = **₹1,08,000**

**WN-5 — Set-off against forward-charge output (Rule 88A):**

| Statement of net GST payable — Jan 2026 | CGST | SGST | IGST |
|---|---|---|---|
| Forward output liability | 4,50,000 | 4,50,000 | 1,80,000 |
| Less: IGST credit (1,08,000) to IGST first | — | — | (1,08,000) |
| Balance IGST | — | — | 72,000 |
| Less: CGST credit to remaining IGST | — | — | (72,000) |
| CGST credit left (3,25,000 − 72,000) = 2,53,000 → to CGST | (2,53,000) | — | — |
| SGST credit to SGST | — | (3,25,000) | — |
| Balance liability | 1,97,000 | 1,25,000 | Nil |
| **Cash (forward charge)** | **1,97,000** | **1,25,000** | **Nil** |

**WN-6 — Total cash outgo:**
- Forward charge: CGST ₹1,97,000 + SGST ₹1,25,000 = ₹3,22,000.
- RCM (WN-2): CGST ₹41,000 + SGST ₹41,000 = ₹82,000.

**Answer:** Net GST payable in **cash** for January 2026 — **RCM: ₹82,000** (CGST ₹41,000 + SGST ₹41,000) **plus forward-charge: CGST ₹1,97,000 + SGST ₹1,25,000 (IGST Nil)**. Total cash ₹4,04,000.

**Why this way (the reasoning):** Two principles drive this problem. First, **RCM liability must be paid in cash, never set off against ITC** — because the recipient is standing in the shoes of the supplier who never collected tax; allowing ITC to fund it would mean no money ever reaches the government at that link. Once paid in cash, that RCM tax becomes an eligible **input** and re-enters the credit pool (subject to Sec 17(5)), so it is tax-neutral over time but cash-positive for the exchequer now. Second, **apportionment for personal use**: Sec 16 allows credit only "in the course or furtherance of business", so the 40% director-personal portion is stripped out — business purpose is a condition precedent, and mixed-use goods are split. The works-contract **repair** is deliberately distinguished from **construction**: 17(5)(c)/(d) block only construction that creates/capitalises immovable property; a revenue repair keeps the factory running and is a normal business input, so its credit survives. Students routinely (a) net RCM against ITC — wrong; (b) block the repair credit by confusing it with construction — wrong; and (c) claim full credit on the personal-use goods — wrong. Getting all three right is the mark of mastery.

*(Full-marks tip: Show RCM as a separate cash line, allow ITC of RCM tax, split the 40% personal-use goods, and keep the factory repair eligible. Biggest deductions: setting off RCM against credit and blocking the repair credit.)*

---

### Q97. Ch: GST – Tax Invoice, Payment & Returns — Bill of supply, receipt voucher & e-invoicing (Marks: 6) [Case/Application]
**Question:** For each situation, state the correct document to be issued and examine the validity of the assessee's practice, citing the relevant provision:

| # | Situation |
|---|---|
| 1 | M/s Kalp Traders, a composition dealer, issues a "tax invoice" showing CGST and SGST separately to its customers |
| 2 | M/s Ria Exports supplies only exempted goods and issues tax invoices charging 0% |
| 3 | M/s Om Ltd. receives an advance of ₹5,00,000 against a future supply of services but issues no document |
| 4 | M/s Zeal Ltd. (aggregate turnover ₹12 crore in FY 2024-25) issues manual tax invoices without generating an Invoice Reference Number (IRN) for its B2B supplies |

**Answer:**
**Governing law:** Sec 31 (tax invoice), Sec 31(3)(c) (bill of supply), Sec 31(3)(d) (receipt voucher), Rule 48(4) (e-invoicing/IRN), Sec 10 (composition).

**Situation 1 — Composition dealer:** A composition dealer under Sec 10 **cannot collect tax** from customers and **cannot issue a tax invoice**; it must issue a **bill of supply** bearing the words "composition taxable person, not eligible to collect tax on supplies." Kalp's practice of issuing a tax invoice with CGST/SGST is **invalid** and exposes it to penalty for unauthorised collection of tax (Sec 76 — tax collected must be paid to government).

**Situation 2 — Exempt supplies only:** A registered person supplying **exempt goods/services** (or paying under composition) must issue a **bill of supply**, not a tax invoice — there is no output tax to charge. Ria's issuing a "tax invoice at 0%" is **incorrect in form**; the proper document is a **bill of supply**.

**Situation 3 — Advance received for services:** On receipt of an advance, the supplier must issue a **receipt voucher** (Sec 31(3)(d)) evidencing the advance and the tax thereon (for **services**, tax on advances is payable). Issuing no document is a **violation**; Om Ltd. must raise a receipt voucher and pay GST on the ₹5,00,000 advance in the month of receipt. (For **goods**, tax on advances is not payable, but a receipt voucher is still required.)

**Situation 4 — E-invoicing threshold (Rule 48(4)):** E-invoicing (generating an IRN via the portal) is **mandatory** for registered persons whose aggregate turnover in **any** preceding financial year exceeds the notified limit of **₹5 crore** (for B2B supplies, exports). Zeal (₹12 crore turnover) exceeds this; issuing manual invoices **without an IRN is invalid** — per Rule 48(5), such an invoice is **"not treated as an invoice"** at all, meaning the recipient cannot claim ITC on it, and Zeal faces penalty.

**Conclusion:** All four practices are **invalid**. Correct documents: (1) bill of supply, (2) bill of supply, (3) receipt voucher + tax on advance, (4) e-invoice with IRN.

**Why this way (the reasoning):** GST prescribes different documents because each signals a different tax event. A **tax invoice** is the only document that entitles the recipient to ITC and evidences tax collected — so persons who **cannot** collect tax (composition dealers, exempt suppliers) must use a **bill of supply**, preventing them from wrongly passing on "tax" that was never leviable and that the recipient would wrongly credit. The **receipt voucher** exists because, for services, the taxable event can be triggered by advance receipt (Sec 13(2)); the document fixes that moment and the tax on it. The **e-invoicing/IRN** regime is an anti-evasion architecture: by validating each B2B invoice on a government portal before it is issued, fake invoices and mismatched ITC claims are choked at source — hence Rule 48(5)'s severe consequence that a non-IRN invoice is legally a non-invoice, killing the recipient's credit. The unifying idea is that **the document must match the substance of the transaction**, and using the wrong one distorts the tax and credit chain.

*(Full-marks tip: Name the exact document AND the consequence for each — the composition penalty (Sec 76), the receipt-voucher advance-tax (services), and Rule 48(5)'s "not an invoice" outcome. Deduction: saying "issue tax invoice" for composition/exempt supplies.)*

---

### Q98. Ch: GST – Tax Invoice, Payment & Returns — Interest on delayed payment u/s 50 (Marks: 6) [Problem]
**Question:** M/s Vega Ltd. (registered, monthly filer) had the following self-assessed liability for the month of September 2025 (due date of GSTR-3B: 20 October 2025). It could file the return and pay only on 12 November 2025. Compute the interest payable under Sec 50, distinguishing the treatment of the cash and ITC portions. Also compute interest on ITC wrongly availed and utilised.

| Particulars | Amount (₹) |
|---|---|
| Total output tax liability (CGST+SGST) for Sep 2025 | 3,60,000 |
| ITC available and utilised | 2,40,000 |
| Balance paid through cash ledger | 1,20,000 |
| ITC wrongly availed AND utilised (detected later) | 30,000 |

**Solution:**

**WN-1 — Interest on delayed payment (Sec 50(1), proviso):**
- Rate = **18% p.a.**
- Interest is charged **only on the portion paid through the electronic cash ledger** (proviso to Sec 50(1)), i.e., ₹1,20,000 — because the return was filed after the due date but the ITC portion represents tax already in the government's hands.
- Delay: due 20 Oct 2025; paid 12 Nov 2025 = **23 days** (21 Oct to 12 Nov).
- Interest = 1,20,000 × 18% × 23 ÷ 365 = 1,20,000 × 0.18 × 0.063014 = **₹1,361.10 ≈ ₹1,361**.

**WN-2 — Interest on wrongly availed and utilised ITC (Sec 50(3) r/w Rule 88B):**
- Where ITC is **wrongly availed and utilised**, interest at **18% p.a.** applies on the amount **utilised**, from the date of utilisation till reversal/payment.
- On ₹30,000 wrongly utilised (assume utilised same period; charge for the same 23-day illustration period, or till date of reversal — here taken as 23 days for computation):
  Interest = 30,000 × 18% × 23 ÷ 365 = **₹340.27 ≈ ₹340**.
- (Note: if ITC is wrongly availed but **not** utilised, no interest arises — Rule 88B levies interest only on wrong availment that is **utilised**.)

| Statement of interest u/s 50 — Sep 2025 | Base (₹) | Rate | Days | Interest (₹) |
|---|---|---|---|---|
| Delayed cash payment (Sec 50(1) proviso) | 1,20,000 | 18% | 23 | 1,361 |
| Wrongly availed & utilised ITC (Sec 50(3)) | 30,000 | 18% | 23 | 340 |
| **Total interest** | | | | **≈ 1,701** |

**Answer:** Interest payable = **≈ ₹1,361** on the delayed cash tax + **≈ ₹340** on wrongly availed-and-utilised ITC = **≈ ₹1,701**. No interest on the ₹2,40,000 legitimately ITC-funded portion.

**Why this way (the reasoning):** Interest under Sec 50 is **compensatory, not penal** — it compensates the government for the **time value of money it was deprived of**. That principle explains both twists. First, the 2021 proviso to Sec 50(1) restricts delay-interest to the **net cash** portion, because the ITC used to pay tax was already collected upstream and lying with the exchequer — the government never actually lost that money, so charging interest on it would be over-compensation. This corrected the earlier harsh practice of charging interest on gross liability. Second, Sec 50(3) read with Rule 88B (amended) charges interest on wrongly availed ITC **only when utilised**, because mere availment (credit sitting unused in the ledger) causes no revenue loss — the loss crystallises only when that wrong credit actually discharges a liability, denying the government real tax. The student trap is charging 18% on the full ₹3,60,000 (ignoring the proviso) and charging interest on wrongly-availed-but-unutilised credit — both over-state interest by misunderstanding that interest tracks actual revenue deprivation.

*(Full-marks tip: Apply the Sec 50(1) proviso (interest on net cash only) and the "utilised" condition of Rule 88B. Deductions: interest on gross liability, or on merely-availed unutilised ITC.)*

---

### Q99. Ch: GST – Registration — Computation of aggregate turnover across States (Marks: 8) [Problem]
**Question:** Mr. Suresh operates under a single PAN with business verticals in three States. Determine (a) his aggregate turnover, and (b) in which State(s) he is liable to register, applying Sec 22 and Sec 2(6). Assume all States are normal (non-special-category) and he supplies **goods only** (except where noted).

| Location | Nature of supply | Value (₹) |
|---|---|---|
| Maharashtra branch | Intra-State taxable supply of goods | 24,00,000 |
| Maharashtra branch | Exempt supply of goods | 5,00,000 |
| Gujarat branch | Intra-State taxable supply of goods | 8,00,000 |
| Gujarat branch | Supply of services (intra-State) | 3,00,000 |
| Rajasthan branch | Inter-State taxable supply of goods | 4,00,000 |
| All-India | Inward supplies taxed under reverse charge | 2,00,000 |

**Solution:**

**WN-1 — Aggregate turnover (Sec 2(6)) — computed on all-India PAN basis:**
Includes all taxable + exempt + inter-State + export supplies; **excludes** taxes and **excludes** inward RCM supplies.

| Component | Include? | Value (₹) |
|---|---|---|
| Maharashtra taxable goods | Yes | 24,00,000 |
| Maharashtra exempt goods | Yes | 5,00,000 |
| Gujarat taxable goods | Yes | 8,00,000 |
| Gujarat services | Yes | 3,00,000 |
| Rajasthan inter-State goods | Yes | 4,00,000 |
| Inward RCM supplies | **No** | — |
| **Aggregate turnover** | | **44,00,000** |

**WN-2 — Liability to register:**
- Aggregate turnover **₹44,00,000 exceeds ₹40 lakh**, so the threshold is crossed. **BUT** — because he makes an **inter-State supply of goods** (Rajasthan, ₹4,00,000), **Sec 24(i)** makes registration **compulsory irrespective of turnover** for that activity anyway.
- Registration is **State-specific** (Sec 22(1) — liable in "every State from where he makes a taxable supply"). Aggregate turnover is computed all-India but tested against the threshold; once crossed (or Sec 24 triggered), he must register in **each State from which he makes taxable supplies**.
  - **Maharashtra** — taxable supplies made → must register.
  - **Gujarat** — taxable supplies made → must register.
  - **Rajasthan** — inter-State taxable supply → must register (Sec 24(i), regardless).

**Note — the ₹40 vs ₹20 lakh twist:** The ₹40 lakh higher threshold applies **only** to a person engaged **exclusively in supply of goods**. Suresh's Gujarat branch also supplies **services** (₹3,00,000). Once services are in the mix, the applicable threshold **drops to ₹20 lakh** for him. His turnover (₹44 lakh) exceeds ₹20 lakh comfortably, reinforcing liability.

**Answer:** (a) Aggregate turnover = **₹44,00,000**. (b) Mr. Suresh is liable to register in **Maharashtra, Gujarat, and Rajasthan** — because his aggregate turnover exceeds the applicable threshold (₹20 lakh, as he also supplies services), and independently because the inter-State supply of goods triggers compulsory registration under Sec 24(i).

**Why this way (the reasoning):** Two design choices of GST intersect here. First, aggregate turnover is deliberately a **PAN-level, all-India** figure (Sec 2(6)) so that a person cannot escape registration by spreading small turnovers across States — the law looks at the whole enterprise to decide *whether* the threshold is crossed. But registration itself is **State-wise** (Sec 22), because GST is a destination-based dual tax where each State needs to see supplies made from within it. Second, the ₹40 lakh enhanced threshold is a concession **only for pure-goods** suppliers; the instant any service supply enters, the person reverts to ₹20 lakh — the exam trap is applying ₹40 lakh and wrongly concluding "just below, not liable." Here the service supply and the inter-State goods supply both independently pull him into registration. The RCM inward supplies are **excluded** from aggregate turnover (they are purchases, not his supplies) but would independently trigger Sec 24(iii) — another reason he must register. The lesson: compute aggregate turnover all-India, pick the *correct* threshold, then decide registration State-by-State, and always cross-check Sec 24 overrides.

*(Full-marks tip: Use ₹20 lakh (not ₹40 lakh) once services are present, exclude inward RCM from turnover, and list each State separately. Deduction: applying ₹40 lakh threshold or treating aggregate turnover as State-wise.)*

---

### Q100. Ch: GST – Input Tax Credit — Integrated net GST payable with Sec 17(5), Rule 42 & RCM (Marks: 10) [Problem]
**Question:** M/s Apex Manufacturing Ltd. (registered, Karnataka), making both taxable and exempt supplies, furnishes the following for February 2026. Rate 18% (9%+9%) intra-State; 18% IGST inter-State, unless stated. Compute the net GST payable in cash, applying ITC eligibility, Sec 17(5), Rule 42 apportionment, and RCM.

| Particulars | Value (₹) |
|---|---|
| Intra-State taxable outward supply | 60,00,000 |
| Intra-State exempt outward supply | 20,00,000 |
| Common inputs & input services (used for both taxable & exempt), intra-State | 10,00,000 |
| Inputs used exclusively for taxable supply, intra-State | 15,00,000 |
| Inputs used exclusively for exempt supply, intra-State | 4,00,000 |
| Motor vehicle (seating capacity 4) for factory manager, intra-State | 8,00,000 |
| Sponsorship service received (RCM applicable), intra-State | 1,00,000 |
| Inter-State inputs (exclusively taxable) | 5,00,000 |

**Solution:**

**WN-1 — Output tax on taxable supply:**
₹60,00,000 × 9% = CGST ₹5,40,000; SGST ₹5,40,000. (Exempt supply — no output tax.)

**WN-2 — RCM (sponsorship) — paid in cash, then eligible ITC:**
₹1,00,000 × 18% = CGST ₹9,000 + SGST ₹9,000 = **₹18,000 payable in cash under RCM**. Sponsorship for business = eligible ITC of ₹18,000 (assume used for taxable/common; here for taxable business, so eligible; if common, subject to Rule 42 — treat as common with the ₹10,00,000 pool for rigour). To keep clean, treat sponsorship as **exclusively taxable** business promotion → ITC eligible fully.

**WN-3 — Classify ITC (Sec 16 & 17(5)):**

| Item | Value | ITC (CGST/SGST each) | Treatment |
|---|---|---|---|
| Exclusive taxable inputs (intra) | 15,00,000 | 1,35,000 | Fully eligible (T4) |
| Exclusive exempt inputs | 4,00,000 | 36,000 | Ineligible (T2) — for exempt |
| Common inputs | 10,00,000 | 90,000 | Common credit → Rule 42 |
| Motor vehicle (≤13 seats) | 8,00,000 | 72,000 | **Blocked — Sec 17(5)(a)** (T3) |
| Sponsorship (RCM) | 1,00,000 | 9,000 | Eligible (taxable business) |
| Inter-State taxable inputs | 5,00,000 | IGST 90,000 | Fully eligible |

**WN-4 — Rule 42 on common credit (per head, CGST):**
- T (common) = 90,000. This C2 = 90,000 (already only common; T1/T2/T3/T4 separated).
- D1 = (Exempt turnover ÷ Total turnover) × C2 = (20,00,000 ÷ 80,00,000) × 90,000 = 0.25 × 90,000 = **₹22,500**.
- D2 = 5% × 90,000 = **₹4,500**.
- Reversal (CGST) = D1 + D2 = **₹27,000**. Eligible common credit (CGST) = 90,000 − 27,000 = **₹63,000**. (SGST identical.)

**WN-5 — Total eligible ITC (per head):**

| Head | Exclusive taxable | Common (net) | Sponsorship RCM | Inter-State | Total |
|---|---|---|---|---|---|
| CGST | 1,35,000 | 63,000 | 9,000 | — | **2,07,000** |
| SGST | 1,35,000 | 63,000 | 9,000 | — | **2,07,000** |
| IGST | — | — | — | 90,000 | **90,000** |

**WN-6 — Set-off (Rule 88A):**

| Statement of net GST payable — Feb 2026 | CGST | SGST | IGST |
|---|---|---|---|
| Output (forward) | 5,40,000 | 5,40,000 | — |
| Less: IGST credit (90,000) to CGST | (90,000) | — | — |
| Less: CGST credit | (2,07,000) | — | — |
| Less: SGST credit | — | (2,07,000) | — |
| Balance (forward) cash | 2,43,000 | 3,33,000 | — |

Wait — reconcile: CGST 5,40,000 − 90,000 (IGST cr) − 2,07,000 (CGST cr) = ₹2,43,000. SGST 5,40,000 − 2,07,000 = ₹3,33,000.

**WN-7 — Total cash:**
- Forward: CGST ₹2,43,000 + SGST ₹3,33,000 = ₹5,76,000.
- RCM (cash): CGST ₹9,000 + SGST ₹9,000 = ₹18,000.

**Answer:** Net GST payable in cash for February 2026 — **RCM: CGST ₹9,000 + SGST ₹9,000 = ₹18,000**, plus **forward charge: CGST ₹2,43,000 + SGST ₹3,33,000 (IGST Nil)**. Common credit reversed under Rule 42 = ₹27,000 each of CGST & SGST; motor-vehicle credit ₹72,000 (each) fully blocked. Total cash outgo ₹5,94,000.

**Why this way (the reasoning):** This problem stitches together the four load-bearing ITC concepts, and the discipline is to **classify before you compute**. Every rupee of input tax must be sorted into one of: exclusively-taxable (fully in), exclusively-exempt (fully out), blocked (Sec 17(5) — out), or common (Rule 42 apportioned) — because each bucket obeys a different rule and mixing them is the surest way to a wrong answer. The motor vehicle (≤13 seats) is blocked upfront (17(5)(a)) and must **never** enter the Rule 42 pool — a common mistake is apportioning a credit that is already dead. The common credit alone is split by the exempt-turnover ratio plus the 5% deeming, reflecting the principle that credit follows taxable output. RCM sponsorship is paid in cash (recipient steps into supplier's shoes) and then re-enters as eligible credit, tax-neutral over time but cash-positive now. Finally, set-off order (Rule 88A) uses the IGST common pool first and keeps CGST/SGST separated for the two governments. The examiner is testing whether the student can **sequence** these — eligibility → 17(5) block → Rule 42 → RCM cash → 88A set-off — without contaminating one step with another.

*(Full-marks tip: Present a classification table first, keep the blocked motor-vehicle credit out of the Rule 42 pool, show RCM as a separate cash line with matching ITC, and apply the 5% D2 deeming. Heaviest deductions: apportioning a Sec 17(5)-blocked credit, netting RCM against ITC, and omitting D2.)*
