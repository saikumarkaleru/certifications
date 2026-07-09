# Taxation (Income Tax & GST) — Accuracy Review: Corrections & Caveats

> **Scope of this review.** This is a **spot-review, not an exhaustive audit.** I read six of the most computation- and threshold-heavy chapters end-to-end:
> - 03 — Income under Salaries
> - 04 — Income from House Property
> - 06 — Capital Gains
> - 09 — Deductions under Chapter VI-A
> - 10 — Advance Tax, TDS & TCS
> - 19 — GST Input Tax Credit
>
> I checked section/rule numbers, formulae, thresholds, rates, and every worked example's arithmetic. The remaining chapters (Basic Concepts, Residential Status, PGBP, IFOS, Clubbing/Set-off, Computation, and GST 13–18, 20–23) were **NOT** reviewed and should not be assumed correct on the strength of this note.
>
> **Headline finding:** The reviewed material is **technically strong**. The worked examples all reconcile line-by-line and use correct ICAI methodology. Every chapter also carries its own "verify the current-year numbers" caveat, which is the right posture. The issues below are mostly **amendment-timing** points (rates that changed mid-year or by regime) plus one genuinely **contentious** area and one **typo**. I did not find any fabricated sections or broken formulae.
>
> Confidence legend: **High** = I am confident this needs correction/verification; **Medium** = likely an issue but partly hedged in the text or edition-dependent; **Low** = minor / cosmetic.

---

## Issues found

### 1. Deductions (Ch 09) → 80CCD(2) employer NPS limit stated as "14% for private-sector employees as well"

- **Claim as written** (§4.1 Family 1 and Quick-Revision): *"80CCD(2)… deductible up to 14% of salary (if employer is Central/State Govt) or 14% of salary for private-sector employees as well (harmonised recently)."* Quick-revision restates it flatly as *"80CCD(2) employer NPS, up to 14% salary."*
- **Correct position:** The 14% ceiling is **not** universal under the **old regime**. Under the **old regime**, employer NPS contribution is deductible up to **10% of salary** for non-government (private) employees; **14%** applies only to **Central/State Government** employees. The uniform **14% for all employees (including private)** applies **only under the new regime u/s 115BAC(1A)** (raised from 10% by the Finance (No. 2) Act, 2024, w.e.f. AY 2025-26). A student computing an **old-regime** answer with 14% for a private employee will overstate the deduction.
- **Confidence: Medium** (the text hedges with "harmonised recently — verify current % and category split," but the flat "14%" in the quick-revision table is misleading). **Fix:** state "10% (private, old regime) / 14% (Govt, or any employee under new regime)."

### 2. Advance Tax / TDS (Ch 10) → Section 194O rate shown as 1%

- **Claim as written** (§4B rate table and Quick-Revision): 194O (e-commerce operator to participant) — **rate 1%**, threshold ₹5,00,000.
- **Correct position:** The 194O TDS rate was **reduced from 1% to 0.1%** with effect from **1 October 2024** (Finance (No. 2) Act, 2024). For FY 2024-25 / AY 2025-26 — the very year the chapter says it targets — the current rate is **0.1%**. The ₹5,00,000 threshold for an individual/HUF participant is correct. (Note the chapter *does* flag the parallel 194H reduction "recently reduced from 5%," so this one appears to be an inconsistency rather than a deliberate choice.)
- **Confidence: Medium-High.** **Fix:** change 194O to 0.1% (w.e.f. 01-10-2024).

### 3. Advance Tax / TDS (Ch 10) → mid-year rate cuts for 194H and 194IB not fully signposted

- **Claim as written:** 194H commission = **2%** ("recently reduced from 5%"); 194IB rent (individual/HUF) = **2%**.
- **Correct position (caveat, not a hard error):** Both cuts (5%→2%) took effect **1 October 2024**. So within **FY 2024-25** the correct rate is **5% up to 30-Sep-2024 and 2% from 01-Oct-2024**. For a full-year FY 2024-25 problem, a payment made before October attracts 5%. The chapter's flat "2%" is correct only for the post-October position. Worth a one-line note so students don't apply 2% to an April payment in a dated problem.
- **Confidence: Medium** (edition/date-dependent; the "current" rate is 2%).

### 4. Capital Gains (Ch 06) → indexation of a gifted/inherited asset uses the *previous owner's* year of acquisition

- **Claim as written** (Example 3, Step 5): For a house gifted by father (bought 2005-06) and sold by son, indexed cost is computed using **CII of 2005-06** (the father's year): `12,00,000 × 348/117`.
- **Correct position (contentious — verify against your ICAI edition):** A literal reading of **Explanation (iii) to Section 48** defines indexation from *"the first year in which the asset was held by the assessee"* — i.e., the **donee's** year (year of gift, 2022-23), even though the **cost** carried over is the father's (Sec 49(1)). The **Bombay High Court in CIT v. Manjula J. Shah** allowed indexation from the previous owner's year (the approach the chapter uses). ICAI study material has, in various editions, followed the **statutory (donee-year)** view in its own illustrations. This is a **known point of divergence**; the numeric answer changes materially depending on which year is used. The chapter *does* flag "subject to case law / current position — verify," which is appropriate.
- **Confidence: Medium.** Not "wrong," but the student must **confirm which method the current ICAI SM adopts** before relying on the 2005-06 indexation in an exam answer. (The holding-period point in the same example — count the previous owner's period → long-term — is unambiguously correct.)

### 5. Capital Gains (Ch 06) → section-number typo in the §4.7 heading

- **Claim as written:** Heading reads *"Advance money forfeited & other adjustments — Sec 51 / **56(2)(x)** interaction."*
- **Correct position:** Forfeited advance money on a failed transfer is taxed under **Section 56(2)(ix)**, which the **body text of the same section correctly cites**. Section **56(2)(x)** is the *gift/receipt-without-consideration* charging clause — a different provision. This is a heading typo, not a conceptual error.
- **Confidence: High** (clear typo). **Fix:** heading should read 56(2)(ix).

### 6. Salaries (Ch 03) → standard deduction illustrated at ₹50,000 (regime-dependent)

- **Claim as written** (Example 3 and §4.7): standard deduction assumed **₹50,000**.
- **Correct position (caveat):** ₹50,000 is correct for the **old regime**. Under the **new regime u/s 115BAC** for AY 2025-26, the salary standard deduction is **₹75,000**. The chapter explicitly flags "verify current figure and regime," so this is a caveat for the student rather than an outright error — but note it, because the new regime is now the default.
- **Confidence: High** on the fact; the chapter already hedges, so treated as a caveat.

---

## Chapters that are sound (within this spot-review)

- **House Property (Ch 04):** No errors found. Sections 22–27, the 30%-of-NAV standard deduction, the ₹2,00,000 / ₹30,000 interest ceilings, two-self-occupied-houses rule, pre-construction 5-instalment spread, and the ₹2,00,000 inter-head set-off cap with 8-year carry-forward are all stated correctly. **Example 3 is impressive** — the vacancy + unrealised-rent + standard-rent-cap + owner-vs-tenant municipal tax + pre-construction interest interaction all reconcile correctly (GAV ₹2,88,000; loss ₹1,200). The GAV/vacancy methodology matches the ICAI approach.
- **GST ITC (Ch 19):** No errors found. Sec 16(1)/(2)(a)-(d)/(aa), the 180-day Rule 37 reversal, Sec 16(4) time limit (earlier of 30 Nov of next FY or annual return), Rule 42 formula (`C2 = T−(T1+T2+T3)−T4; D1 = C2·E/F; D2 = 5%C2`), Rule 43 (60-month/5-year spread), Sec 17(5) blocked list with the plant-&-machinery carve-out, the Sec 49/49A/Rule 88A utilisation order (IGST first; CGST↔SGST never cross), and Sec 18 transition rules are all accurate. All five worked examples reconcile.
- **Advance Tax / TDS / TCS (Ch 10):** Structurally sound apart from items 2–3 above. The 15/45/75/100 schedule, ₹10,000 threshold, resident-senior-without-PGBP exemption (Sec 207(2)), 234B (90% / 1% p.m.) and 234C (safe harbours 12%/36% for Jun/Sep; 3-month vs 1-month) are correct, and **both 234C and 201(1A) worked examples reconcile exactly** (₹1,800 and ₹600). Most 194-series thresholds are correct for AY 2025-26 (194A 40k/50k/5k, 194C 30k/1L, 194I 2.4L, 194J 30k, 194IA 50L).
- **Salaries (Ch 03):** Sound apart from the standard-deduction caveat (item 6). Sec 15–17, the HRA least-of-three, the RFA population-slab valuation (10% for >40 lakh under revised Rule 3), the 12%-of-salary RPF employer cap, the 9.5% interest exemption, gratuity/leave-encashment/pension "least-of" formulae, and the ₹25,00,000 leave-encashment ceiling are all correct. **Example 3 (full salary computation) reconciles to ₹16,13,560** with correct treatment of each perquisite and the PF caps.
- **Deductions (Ch 09):** Sound apart from item 1. The 80C/CCC/CCD(1) shared ₹1.5L umbrella (80CCE), the separate ₹50,000 (80CCD(1B)), 80D buckets (25k/50k, max ₹1L), 80DD/80U (75k/1.25L), 80DDB, 80E (interest only, 8 years, no cap), 80TTA/TTB, 80G two-dimension structure with the ₹2,000-cash bar and Adjusted-GTI qualifying limit, and the new-regime survivors (80CCD(2), 80CCH, 80JJAA) are all correct. **Example 3 reconciles** (Adjusted GTI ₹6,22,000 → 80G ₹55,000 → Total Income ₹7,67,000).

---

## Overall reliability — per reviewed chapter

| Chapter | Reliability | Note |
|---|---|---|
| 03 Salaries | **High** | One regime caveat (std deduction ₹75k under new regime). Examples correct. |
| 04 House Property | **Very High** | No errors found. Hardest example fully reconciles. |
| 06 Capital Gains | **High** | One contentious area (gifted-asset indexation year) + one heading typo (56(2)(ix) not (x)). Concepts and arithmetic sound. |
| 09 Deductions Ch VI-A | **High** | Fix the 80CCD(2) 14% claim (private = 10% under old regime). Rest excellent. |
| 10 Advance Tax/TDS/TCS | **High (with rate caveats)** | Correct 194O to 0.1%; flag 194H/194IB mid-year (Oct-2024) split. Interest examples exact. |
| 19 GST ITC | **Very High** | No errors found. All formulae and examples correct. |

**Bottom line for the student:** You can trust the *reasoning, structure, section map, and computation methods* in these six chapters with confidence. The only things to actively fix/verify before the exam are the five flagged points above — all of them are **rate/threshold amendments or a regime-split**, exactly the category every chapter already warns you to reconcile against the current ICAI Study Material for your Assessment Year. Because this was a spot-review of 6 of 24 chapters, apply the same "verify the numbers, trust the logic" discipline to the unreviewed chapters.
