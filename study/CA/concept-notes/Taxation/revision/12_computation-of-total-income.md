# Chapter 12 — Computation of Total Income & Tax Liability

## Snapshot

Five head-figures are assembled into **one number (Total Income)** and driven through a **fixed, non-negotiable pipeline** to reach tax payable. Order is logic, not ritual — each step consumes the previous one's output. Figures reflect **AY 2025-26**; all rates/limits are *plug-in values* subject to Finance Act change — the **sequence is permanent**.

**The pipeline (chant it):** Heads → Club → Set-off → **GTI** → VI-A → **TI** → Split rates → Rebate → Surcharge → Cess → Relief → **Tax payable** → less prepaid taxes.

**Three currencies (where students slip):** Income rupees (Stages 1–6) · Tax rupees (Stages 7–10) · Cash rupees (Stage 12). Every catastrophic error = a rupee applied in the wrong currency (deduction against tax, surcharge against income, TDS against income).

---

## Core concepts

- **Total Income is built bottom-up in strict order.** Cannot set off a loss before each head is known (aggregation precedes set-off); cannot set your losses against income never yours (clubbing precedes set-off); VI-A is capped at GTI and barred from special incomes (GTI must exist, special incomes identified first); rebate/surcharge/cess act on *tax* so tax comes first.
- **The pipeline is a progressively narrowing filter:** early stages decide *how much is income*; middle stages *how much is taxable*; late stages *how much tax*; last stage *how much cash*.
- **Regime is chosen, not fixed.** New regime (115BAC) is default since AY 2024-25; it switches entire deductions/exemptions on and off, so a full computation may need to be run **twice** (once per regime) and compared.
- **Why order can't be resequenced (stress test):** VI-A before set-off → double benefit; surcharge before rebate → wrong base; cess before surcharge → understated cess; special-income carve-out after VI-A → deductions wrongly shelter LTCG.

---

## Key provisions / rules

### Stage design logic

| Stage | Section | One-line rule |
|---|---|---|
| 5 heads | 14 | Compute each head net (Salary 15-17; HP 22-27; PGBP 28-44; CG 45-55A; OS 56-59) |
| Clubbing | 60-64 | Add diverted income back; keeps its head-character; minor exemption ₹1,500/child (Sec 10(32)) |
| Set-off | 70-71 | Intra-head → inter-head; HP loss inter-head cap ₹2,00,000 (71(3A)) |
| Carry-forward | 72-74A | Each loss its own life & restriction; needs timely return (Sec 80) |
| GTI | 80B(5) | Sum of heads after clubbing & set-off, before VI-A |
| VI-A | 80C-80U | ≤ GTI (80A); not against 111A/112/112A/115BB |
| Total Income | 2(45), 288A | GTI − VI-A; round to nearest ₹10 |

### Stage 1 — heads (Sec 14) traps
- **Salary can NEVER be negative** — floored at nil, never carried negative.
- **Capital Gains splits internally BEFORE the pipeline:** STCG-111A, STCG-other, LTCG-112, LTCG-112A are four different animals — carry each separately from the start.
- **Deemed income (68/69 etc.) → Sec 115BBE: flat 60% + 25% surcharge + cess (≈78%)**, no deduction, no set-off.

### Stage 2 — clubbing (Sec 60-64)
- **Sec 60** — transfer of income without asset → clubbed.
- **Sec 64(1)(ii)/(iv)/(vi)/(vii)** — income to spouse/son's wife from transferred assets.
- **Sec 64(1A)** — minor's income clubbed with higher-income parent; exemption ₹1,500/child (10(32)), capped at that child's income; **unavailable in new regime**.
- **Sec 64(2)** — HUF from converted individual property.
- **A clubbed LOSS is also clubbed** and can be set off by the transferor (favourite twist).

### Stage 3 — set-off & carry-forward (Sec 70-80)

**Intra-head (Sec 70) exceptions:** speculation loss → speculation profit only; LTCL → LTCG only (never STCG); STCL → STCG or LTCG; race-horse loss → race-horse only.

**Inter-head (Sec 71) restrictions:** HP loss → any head but **capped ₹2,00,000** (71(3A)), balance c/f; capital-gains loss → NO other head; business loss → NOT against salary (71(2A)); casual income → no loss set off against it.

| Loss type | Section | C/F period | Set off in future only against |
|---|---|---|---|
| House property loss | 71B | 8 yrs | HP income |
| Non-speculation business loss | 72 | 8 yrs | Business income (any) |
| Speculation loss | 73 | 4 yrs | Speculation income |
| Specified business (35AD) loss | 73A | Indefinite | Specified business income |
| Short-term capital loss | 74 | 8 yrs | STCG or LTCG |
| Long-term capital loss | 74 | 8 yrs | LTCG only |
| Race-horse loss | 74A | 4 yrs | Race-horse income |
| Unabsorbed depreciation | 32(2) | Indefinite | Any income except salary |

- **Sec 80:** business/speculation/capital/race-horse losses need return filed by **139(1) due date** to c/f; **HP loss & unabsorbed depreciation do NOT.**
- **Optimisation:** set losses off first against normal (slab) income (preserve special rates + basic-exemption absorption); exhaust shortest-life losses first; current-year before b/f; within year: current depreciation → b/f business loss → unabsorbed depreciation.
- **₹2,00,000 cap is inter-head only** — intra-head HP set-off is uncapped.
- **Unabsorbed depreciation is NOT a business loss** — merges into next year's depreciation.

### Stage 4-6 — GTI, VI-A, Total Income
- **Adjusted GTI** (for 80G/80GG/80GGC "% of AGTI" caps) = GTI − special incomes (111A/112/112A) − other VI-A already claimed. Do NOT reuse plain GTI.
- **Sec 80A golden restrictions:** (1) total VI-A ≤ GTI (can reach nil, never below); (2) not allowed against LTCG (112/112A), STCG-111A, casual (115BB) — carve these out first.
- **Sec 288A rounding:** round Total Income to nearest ₹10, once. ₹6,32,004 → ₹6,32,000; ₹6,32,006 → ₹6,32,010.

| Section | For | Ceiling / rule |
|---|---|---|
| 80C | LIC, PPF, ELSS, housing principal, tuition, 5-yr FD | ₹1,50,000 (combined 80C+80CCC+80CCD(1) via 80CCE) |
| 80CCD(1B) | Additional NPS self | ₹50,000 (outside 80C bucket) |
| 80CCD(2) | Employer NPS | 10% of salary (14% govt/new regime); outside bucket |
| 80D | Health insurance | ₹25,000 self/family; ₹50,000 senior; +₹50,000 senior parents |
| 80DD/80DDB/80U | Disabled dependant / treatment / self-disability | Fixed amounts |
| 80E | Education loan interest | No cap, 8 years |
| 80EEA | Affordable housing loan interest | ₹1,50,000 |
| 80G | Donations | 50% or 100%, some with 10%-of-AGTI cap; cash > ₹2,000 gets nothing |
| 80GG | Rent paid (no HRA) | Least of ₹5,000 p.m. / 25% AGTI / rent − 10% AGTI |
| 80TTA / 80TTB | Savings interest / senior interest | ₹10,000 / ₹50,000 |

- **80TTA vs 80TTB mutually exclusive:** senior → 80TTB (₹50,000, savings+FD); non-senior → 80TTA (₹10,000, savings only). Never both; never 80TTA on FD.
- **New regime kills almost all VI-A** — only survivors: **80CCD(2)** (employer NPS) and **80CCH** (Agniveer). Standard deduction & family pension deduction still allowed.
- **80G computed LAST within Stage 5** (needs AGTI after other deductions).

### Stage 7 — split & rates

| Income | Section | Rate |
|---|---|---|
| STCG listed equity (STT paid) | 111A | 15% (20% for transfers on/after 23-Jul-2024) |
| LTCG listed equity above threshold | 112A | 10% above ₹1,00,000 (12.5% above ₹1,25,000 post-23-Jul-2024) |
| Other LTCG | 112 | 20% with indexation / 12.5% without (post-23-Jul-2024) |
| Winnings — lottery/betting/games | 115BB / 115BBJ | 30% flat, no deduction, no basic-exemption benefit |

- **Basic-exemption absorption:** resident individual/HUF may use *unused* basic exemption against 111A and 112/112A (never against 115BB). **Non-residents cannot.** Absorb against **higher-rate special income first** (shield 111A before 112A, both pre- and post-23-Jul).

**New regime slabs (AY 2025-26 — default):**

| Slab | Rate |
|---|---|
| Up to ₹3,00,000 | Nil |
| ₹3,00,001 – ₹7,00,000 | 5% |
| ₹7,00,001 – ₹10,00,000 | 10% |
| ₹10,00,001 – ₹12,00,000 | 15% |
| ₹12,00,001 – ₹15,00,000 | 20% |
| Above ₹15,00,000 | 30% |

**Old regime slabs (individual < 60):**

| Slab | Rate |
|---|---|
| Up to ₹2,50,000 | Nil |
| ₹2,50,001 – ₹5,00,000 | 5% |
| ₹5,00,001 – ₹10,00,000 | 20% |
| Above ₹10,00,000 | 30% |

Old regime basic exemption: **₹3,00,000** seniors (60-80), **₹5,00,000** super-seniors (80+). New regime: everyone ₹3,00,000.

**Regime opt-out (heavily tested, asymmetric):** Business income → file **Form 10-IEA by 139(1) due date** to opt out; can revert to new regime **only once**, then **locked** (can never return to old while business continues). No-business/salaried → free choice **every year** in return.

### Stage 8 — Rebate 87A (resident individual only)

| Regime | TI ceiling | Max rebate |
|---|---|---|
| Old | ₹5,00,000 | ₹12,500 |
| New (115BAC) | ₹7,00,000 | ₹25,000 |

- **Marginal relief (new):** just above ₹7L, tax capped at income-excess-over-₹7L (tapers to nil ~₹7,78,000). It's a *cap, not a cliff*.
- **Not available against 112A LTCG tax** (verify current stance). Eligibility base = Total Income **including special incomes** (a tiny STCG can tip over the cliff).

### Stage 9 — Surcharge (% of tax)

| Total Income | Old | New |
|---|---|---|
| ₹50L – ₹1cr | 10% | 10% |
| ₹1cr – ₹2cr | 15% | 15% |
| ₹2cr – ₹5cr | 25% | 25% |
| Above ₹5cr | 37% | **25% (capped)** |

- **Cap 15%** on surcharge attributable to 111A/112/112A/dividend, even above ₹2cr — split the tax and surcharge each bucket at its own rate (don't apply 25/37% to CG tax).
- **Marginal relief at every threshold:** increase in (tax+surcharge) cannot exceed increase in income above threshold.

### Stage 10-12 — Cess, Relief, Payable
- **Cess: flat 4%** on (tax after rebate + surcharge). No marginal relief on cess itself; fully-rebated taxpayer pays zero cess.
- **Sec 89(1)** — arrears/advance salary spread-back (Form 10E); relief = difference of differences (may be nil). **Sec 90/90A** — FTC under DTAA. **Sec 91** — unilateral relief, no DTAA.
- **AMT (115JC):** 18.5% + surcharge/cess of adjusted TI for non-corporates claiming certain deductions; higher of normal tax/AMT payable; credit c/f **15 years**. Does NOT apply if adjusted TI ≤ ₹20L (ind/HUF/AOP) or generally if new regime opted.
- **Stage 12:** less TDS/TCS/advance/self-assessment; add interest **234A** (late filing, 1% p.m.) / **234B** (advance-tax shortfall, paid < 90%) / **234C** (deferment of instalments) — all simple 1% p.m.; round net to nearest ₹10 (**288B**).

---

## Worked mini-example

**Ms. B, resident, 45, AY 2025-26, OLD regime.** Business income ₹6,00,000; HP LOSS ₹2,80,000; LTCG land (112) ₹3,00,000; STCG listed (111A) ₹1,00,000; 80C ELSS ₹1,50,000.

**Stage 3 set-off:** HP loss ₹2,80,000 → inter-head cap ₹2,00,000 set against business → business ₹4,00,000; balance ₹80,000 c/f (71B). Preserve special incomes.

| Head | ₹ |
|---|---|
| Business (after ₹2L HP set-off) | 4,00,000 |
| LTCG (112) | 3,00,000 |
| STCG (111A) | 1,00,000 |
| **GTI** | **8,00,000** |

**Stage 5 VI-A:** 80C ₹1,50,000 cannot hit 111A/112 → set only against normal ₹4,00,000 → normal ₹2,50,000. **Total Income = ₹6,50,000** (2,50,000 + 3,00,000 + 1,00,000).

**Stage 7:** Normal ₹2,50,000 = exemption limit → tax nil, **exemption fully used**, nothing left to shelter special incomes.
- STCG 111A ₹1,00,000 @ 15% = ₹15,000
- LTCG 112 ₹3,00,000 @ 20% = ₹60,000
- **Tax before rebate = ₹75,000**

**Stage 8:** TI ₹6,50,000 > ₹5L → no 87A. **Cess 4% = ₹3,000. Tax payable = ₹78,000.** HP loss ₹80,000 noted for c/f.

*Examiner tweak:* had normal income been below ₹2,50,000, the unused exemption is absorbed against **STCG 111A first** (preserve LTCG benefit), cutting tax further.

---

## Exam traps & must-remember

1. **Netting heads before set-off** — always intra-head → capped inter-head (HP ₹2,00,000, 71(3A)) → c/f.
2. **Claiming VI-A against special incomes** — 80C etc. cannot reduce 112/112A/111A/115BB; carve out first.
3. **Wrong basic-exemption absorption order** — residents use it against **higher-rate STCG 111A first**, never against casual income; non-residents get none.
4. **87A on LTCG tax** — doesn't shelter 112A (verify); residents only.
5. **Wrong regime deductions** — new regime kills HRA, LTA, self-occupied interest, professional tax, almost all VI-A; only 80CCD(2)/80CCH + standard deduction survive.
6. **Ignoring surcharge 15% cap** (111A/112/112A/dividend) and marginal relief at every threshold.
7. **Cess base error** — 4% of (tax after rebate + surcharge), not before surcharge.
8. **Rounding at wrong place** — only Total Income (288A) and net tax payable (288B) to ₹10, not intermediates.
9. **Carry-forward without timely return** — business/speculation/capital/race-horse need 139(1) filing (Sec 80); HP loss & unabsorbed depreciation don't.
10. **Salary never negative;** business loss NOT against salary (71(2A)).
11. **Double-counting 80C bucket** — 80C+80CCC+80CCD(1) share ONE ₹1,50,000 cap (80CCE); only 80CCD(1B) & 80CCD(2) sit outside.
12. **80TTA/80TTB confusion** — never both; never 80TTA on FD interest.
13. **Plain GTI where adjusted GTI required** — 80G/80GG/80GGC run on AGTI, computed after other deductions.
14. **Regime lock-in & Form 10-IEA deadline** — business assessees flip back to new only once; file 10-IEA by 139(1) date.
15. **Missing 234-series interest at Stage 12** — "return filed late"/"no advance tax" = add-back after cess.
16. **Clubbed loss** — clubbing runs both ways; clubbed HP loss is set off in transferor's hands.

---

## One-line recall

- **Chant:** Heads → Club → Set-off → GTI → VI-A → TI → Split → Rebate → Surcharge → Cess → Relief → Payable → less prepaid.
- **HP loss inter-head cap ₹2,00,000; VI-A ≤ GTI and never against 111A/112/112A/115BB.**
- **87A:** Old TI ≤ ₹5L → ₹12,500; New TI ≤ ₹7L → ₹25,000 (+ marginal relief); residents only.
- **Surcharge:** 10%/15%/25%/37% (>50L/1cr/2cr/5cr); new regime caps at 25%; 15% cap on 111A/112/112A/dividend; marginal relief everywhere.
- **Cess 4%** on (tax after rebate + surcharge); round TI & net payable to ₹10 (288A/288B).
- **80C bucket = one ₹1,50,000 cap (80CCE);** 80CCD(1B) +₹50,000 & 80CCD(2) employer NPS sit outside.
