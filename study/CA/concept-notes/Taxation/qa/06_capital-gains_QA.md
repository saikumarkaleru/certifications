# Q&A — Capital Gains

> **AY flag:** Rates, monetary limits and the CII table below are as generally applicable for **AY 2025-26** (and the position after the Finance (No.2) Act, 2024 changes effective **23 July 2024**). Capital-gains law saw a major re-write in July 2024 (holding-period simplification, 12.5% LTCG, removal of indexation for most assets). **Always re-verify the exact rate, holding period and CII number against the current ICAI Study Material / RTP for your attempt.** Section references are to the **Income-tax Act, 1961**.

---

## Section A — Concept Check (short Q&A with section citation)

**A1. What are the four conditions for a charge under "Capital Gains"?**
There must be (i) a **capital asset** [Sec 2(14)], (ii) a **transfer** [Sec 2(47)], (iii) the transfer takes place during the previous year, and (iv) profit/gain arises. Charge is under **Sec 45(1)**; gain is chargeable in the year of transfer.

**A2. Give two items expressly excluded from "capital asset" under Sec 2(14).**
(i) **Stock-in-trade** (taxed as business income), and (ii) **rural agricultural land** in India. Also excluded: personal movable effects (except jewellery, art, drawings, paintings, sculptures, archaeological collections).

**A3. Why does the law tax gains only on "transfer" and not on mere appreciation?**
Because of the **realisation principle** — unrealised paper gains are not income until converted through a transfer event. This is the "realisation" pillar; tax follows the cash-generating event, not annual mark-to-market.

**A4. Name three transactions that are "not regarded as transfer" under Sec 47.**
(i) Distribution of capital asset on **total partition of an HUF** [47(i)]; (ii) transfer under a **gift or will** [47(iii)]; (iii) transfer of a capital asset by a **holding company to its 100% subsidiary** (or vice versa) [47(iv)/(v)]. These break the charge — no capital gain arises.

**A5. State the holding-period thresholds for long-term status (post 23-07-2024).**
Two buckets only: **listed securities & units** — long-term if held **> 12 months**; **all other assets** (including unlisted shares and immovable property) — long-term if held **> 24 months**. (The old 36-month category for other assets is gone.)

**A6. What is the purpose of the Cost Inflation Index (CII) under Sec 48?**
It **neutralises inflation** so that only the real gain is taxed, by grossing up cost: *Indexed cost = Cost × (CII of year of transfer ÷ CII of year of acquisition)*. Post-July 2024, indexation is **withdrawn** for most assets under the new 12.5% regime (with a grandfathering/relief option for resident individuals/HUF on land & building acquired before 23-07-2024).

**A7. Distinguish Sec 111A, 112 and 112A rates.**
- **111A** — STCG on listed equity/units (STT paid): **20%** (raised from 15% w.e.f. 23-07-2024).
- **112A** — LTCG on listed equity/units (STT paid) above ₹1.25 lakh: **12.5%**, no indexation.
- **112** — LTCG on other assets: **12.5%** without indexation (post 23-07-2024).

**A8. What does Sec 55 supply that Sec 48 needs?**
Sec 55 defines **"cost of acquisition" and "cost of improvement"**, including the **Fair Market Value as on 01-04-2001** option for assets acquired before that date, and treats cost of self-generated goodwill etc. as **nil**.

**A9. Why does Sec 49(1) matter for gifted/inherited assets?**
It provides **cost stepping-through**: the previous owner's cost becomes the assessee's cost, and Explanation to Sec 2(42A) makes the **previous owner's holding period** count. This prevents a gift/inheritance from resetting the tax clock.

**A10. What is the anti-avoidance role of Sec 50C?**
For land/building, if actual consideration is **below stamp-duty value**, the **stamp-duty value** is deemed to be the full value of consideration (subject to a **safe-harbour tolerance band of 10%**). Sec 50CA does the same for **unquoted shares** using FMV.

---

## Section B — Graded Computational Problems (full working, self-checked)

### B1 (Easy) — STCG under Sec 111A
Ms. R sold 1,000 listed equity shares (STT paid) on 10-05-2024, holding period 8 months. Sale ₹4,20,000; cost ₹3,00,000; brokerage on sale ₹2,000. Compute tax on this gain (ignore other income; she is a resident individual, opts out is irrelevant).

**Answer.** Holding ≤ 12 months → **STCG**, and STT-paid listed equity → **Sec 111A**.
- Full value of consideration = 4,20,000
- Less: expenses on transfer (brokerage) = 2,000
- Net consideration = 4,18,000
- Less: cost of acquisition = 3,00,000
- **STCG = ₹1,18,000**
- Tax @ **20%** (111A, post 23-07-2024) = **₹23,600** (+ cess). *Check: 1,18,000 × 20% = 23,600.* ✔

### B2 (Easy-Moderate) — LTCG on listed equity, Sec 112A
Mr. S sold listed shares (STT paid) held 3 years on 01-02-2025. Net LTCG computed = ₹3,00,000. No other capital gains. Compute tax.

**Answer.** Sec 112A: exemption of first **₹1,25,000**, balance @ **12.5%** (no indexation).
- Taxable LTCG = 3,00,000 − 1,25,000 = 1,75,000
- Tax = 1,75,000 × 12.5% = **₹21,875** (+ cess). *Check: 1,75,000 × 0.125 = 21,875.* ✔

### B3 (Moderate) — LTCG on land WITH indexation (pre-23-07-2024 sale)
Mr. T sold land on **15-06-2023** for ₹80,00,000 (brokerage ₹80,000). Purchased in **FY 2005-06** for ₹8,00,000. CII: 2005-06 = **117**, 2023-24 = **348**. Compute LTCG.

**Answer.** Held > 24 months → LTCG; sale before 23-07-2024 → **indexation available**.
- Indexed cost = 8,00,000 × (348 ÷ 117) = 8,00,000 × 2.97436 = **₹23,79,487**
- Net consideration = 80,00,000 − 80,000 = 79,20,000
- **LTCG = 79,20,000 − 23,79,487 = ₹55,40,513**
- Tax @ 20% (Sec 112, old regime for this date) = ₹11,08,103 (+ cess). *Check: 348/117 = 2.974358…; ×8,00,000 = 23,79,487.* ✔

### B4 (Moderate-Hard) — Gifted house: Sec 49(1) + 2(42A) + Sec 54
Mr. V received a residential house as a **gift from his father** on 01-07-2023. Father had **purchased it in FY 2014-15 for ₹20,00,000**. V sold it on **10-08-2024 for ₹95,00,000** (transfer expenses ₹1,00,000). V bought a new residential house for ₹40,00,000 on 01-12-2024. Compute taxable capital gain. (Sale is after 23-07-2024 → **no indexation**; new 12.5% regime.)

**Answer.**
Cost & holding step through from father [Sec 49(1) + Expln to 2(42A)]. Father held from FY 2014-15 → holding **> 24 months** → **LTCG**.
- Cost of acquisition (previous owner) = 20,00,000 (no indexation — sale after 23-07-2024)
- Net consideration = 95,00,000 − 1,00,000 = 94,00,000
- LTCG before exemption = 94,00,000 − 20,00,000 = **₹74,00,000**
- **Sec 54** exemption (residential house → residential house) = lower of (a) LTCG ₹74,00,000 or (b) amount invested ₹40,00,000 = **₹40,00,000**
- **Taxable LTCG = 74,00,000 − 40,00,000 = ₹34,00,000**
- Tax @ 12.5% (Sec 112) = ₹4,25,000 (+ cess). *Check: 94L−1L expenses−20L cost = 74L; −40L Sec 54 = 34L; ×0.125 = 4,25,000.* ✔

### B5 (Exam-Hard) — Sec 50C + Sec 54F + CGAS clawback
Mr. K, resident, sold a **plot of land** (long-term, acquired FY 2016-17 for ₹15,00,000) on **05-09-2024** for a stated consideration of **₹60,00,000**; **stamp-duty value ₹68,00,000**. Transfer expenses ₹50,000. He does **not own more than one residential house**. He invested ₹30,00,000 in a new residential house and deposited ₹10,00,000 in the **Capital Gains Account Scheme** before the return due date; the CGAS amount was **not utilised** within the 3-year window. Compute LTCG for the year of sale and the amount taxable on clawback. (No indexation — post 23-07-2024.)

**Answer.**
Step 1 — Full value of consideration [Sec 50C]. Stamp value 68,00,000 vs stated 60,00,000. Variation = 8,00,000 = 13.3% of stated, which **exceeds the 10% tolerance band** → adopt **stamp value ₹68,00,000**.
Step 2 — LTCG before exemption:
- 68,00,000 − 50,000 (expenses) − 15,00,000 (cost, no indexation) = **₹52,50,000**
Step 3 — Sec 54F (transfer of a non-residential LTCA + investment in one residential house). Exemption is **proportionate to net consideration**:
- Net consideration for 54F = 68,00,000 − 50,000 = 67,50,000
- Amount invested/deposited = 30,00,000 + 10,00,000 = 40,00,000
- Exemption = LTCG × (Investment ÷ Net consideration) = 52,50,000 × (40,00,000 ÷ 67,50,000) = 52,50,000 × 0.592593 = **₹31,11,111**
- **Taxable LTCG in year of sale = 52,50,000 − 31,11,111 = ₹21,38,889**
Step 4 — Clawback of unutilised CGAS. The ₹10,00,000 not utilised is proportionately withdrawn from exemption and **taxed as LTCG in the year the 3-year period expires**:
- Reversed exemption = 52,50,000 × (10,00,000 ÷ 67,50,000) = 52,50,000 × 0.148148 = **₹7,77,778**
*Check: exemption used only for ₹30L actual house = 52,50,000 × (30,00,000/67,50,000) = 23,33,333; original exemption 31,11,111 − 23,33,333 = 7,77,778.* ✔
**Result:** Year-of-sale taxable LTCG **₹21,38,889** (tax @12.5% Sec 112); clawed-back LTCG **₹7,77,778** taxed in the year the CGAS period lapses.

---

## Section C — Past-Paper-Style Full Questions

### C1. "Compute the income under the head Capital Gains" (mixed portfolio)
Mr. A, resident individual, during **FY 2024-25** had: (i) STCG on listed shares STT-paid ₹2,00,000 [111A]; (ii) LTCG on listed shares STT-paid ₹2,00,000 [112A]; (iii) LTCG on sale of gold (bought FY 2019-20 ₹5,00,000, sold 01-01-2025 ₹9,00,000, no indexation post-July-2024) [112]. State the head income and tax on each stream.

**Model answer.**
| Stream | Section | Amount | Rate | Tax |
|---|---|---|---|---|
| STCG listed equity | 111A | 2,00,000 | 20% | 40,000 |
| LTCG listed equity | 112A | 2,00,000 − 1,25,000 = 75,000 | 12.5% | 9,375 |
| LTCG gold | 112 | 9,00,000 − 5,00,000 = 4,00,000 | 12.5% | 50,000 |

- Income under head Capital Gains = 2,00,000 + 2,00,000 + 4,00,000 = **₹8,00,000**.
- Total CG tax = 40,000 + 9,375 + 50,000 = **₹99,375** (+ cess). *Checks: 112A exempts first 1.25L; gold LTCG 4L×12.5%=50,000.* ✔
- **Note:** Special-rate incomes (111A/112/112A) are **excluded** when checking the basic-exemption-adjustment and the deductions under Chapter VI-A cannot be set against them.

### C2. Interplay of set-off (Sec 70/74) with capital gains
Mr. B has **STCL ₹3,00,000** (non-111A), **STCG ₹1,00,000** (111A), and **LTCG ₹4,00,000** (112). Show set-off.

**Model answer.**
- **STCL can be set off against BOTH STCG and LTCG** [Sec 70(2)/71 rule]. **LTCL can be set off only against LTCG.**
- Set STCL 3,00,000: first against STCG 1,00,000 (balance loss 2,00,000), then against LTCG → LTCG 4,00,000 − 2,00,000 = **₹2,00,000**.
- Net taxable: STCG 111A = **Nil**; LTCG 112 = **₹2,00,000** @12.5% = **₹25,000**.
- *Check: total loss 3,00,000 fully absorbed (1,00,000 + 2,00,000).* ✔ Unabsorbed capital loss carries forward **8 assessment years** [Sec 74].

### C3. Depreciable asset — Sec 50
X Ltd sold the **only asset** in its plant block. Opening WDV ₹6,00,000; additions ₹1,00,000; sale consideration ₹9,00,000. Compute gain and its character.

**Model answer.** Under **Sec 50**, when the block ceases to exist (or sale exceeds WDV), the excess is **deemed Short-Term Capital Gain** irrespective of actual holding period.
- Block value = WDV 6,00,000 + additions 1,00,000 = 7,00,000
- STCG = 9,00,000 − 7,00,000 = **₹3,00,000**, taxed as STCG at **normal slab rates** (Sec 50 gain is STCG but not 111A). *Check: 9L−7L=3L.* ✔

---

## Section D — MCQs / Case Scenarios

**D1.** Post 23-07-2024, an unlisted equity share is long-term if held for more than:
(a) 12 months (b) 24 months (c) 36 months (d) 48 months
**Ans: (b).** Sec 2(42A) — non-listed assets now use the 24-month line.

**D2.** LTCG on STT-paid listed equity above the ₹1.25 lakh threshold is taxed at:
(a) 10% (b) 12.5% (c) 15% (d) 20%
**Ans: (b).** Sec 112A rate raised to 12.5% w.e.f. 23-07-2024.

**D3.** Sec 50C tolerance band (stamp value vs consideration) is:
(a) 5% (b) 10% (c) 15% (d) 20%
**Ans: (b).** If variation ≤ 10%, actual consideration is accepted.

**D4.** Exemption under Sec 54EC (investment in NHAI/REC bonds) is capped at:
(a) ₹25 lakh (b) ₹50 lakh (c) ₹1 crore (d) no cap
**Ans: (b).** Max ₹50 lakh, within 6 months, 5-year lock-in.

**D5 (Scenario).** A gifts jewellery to B; B sells it after 6 months (A had held it 10 years). Character of gain in B's hands?
(a) STCG (b) LTCG (c) Exempt (d) Business income
**Ans: (b) LTCG.** Sec 49(1) + Expln to 2(42A) — previous owner's holding period is included, so total > 24 months.

**D6 (Scenario).** Rural agricultural land in India is sold at a large profit. Taxable as capital gain?
(a) Yes, STCG (b) Yes, LTCG (c) No — not a capital asset (d) Only if > ₹50 lakh
**Ans: (c).** Sec 2(14) excludes rural agricultural land from "capital asset".

**D7.** Cost of a **self-generated goodwill** of a business, for capital-gains computation, is taken as:
(a) FMV (b) Nil (c) Book value (d) Indexed cost
**Ans: (b).** Sec 55 — cost of self-generated goodwill/right etc. is nil.

---

## Decision Map (which rate/section applies)

```mermaid
flowchart TD
    A[Capital asset transferred?] -->|No / excluded 2(14) or 47| Z[No capital gain]
    A -->|Yes| B{Holding period}
    B -->|Listed sec &gt; 12m / others &gt; 24m| L[Long-Term]
    B -->|Otherwise| S[Short-Term]
    S --> S1{STT-paid listed equity?}
    S1 -->|Yes| S2[Sec 111A — 20%]
    S1 -->|No| S3[Slab rates]
    L --> L1{STT-paid listed equity?}
    L1 -->|Yes| L2[Sec 112A — 12.5% above 1.25L]
    L1 -->|No| L3[Sec 112 — 12.5% no indexation]
    L3 --> L4{Reinvestment?}
    L4 -->|House 54/54F| E1[Exemption]
    L4 -->|Bonds 54EC| E2[Exemption max 50L]
```

---

## Quick-Revision Trigger Sheet

| Item | Section | Key number (AY 25-26) |
|---|---|---|
| Charge | 45(1) | Year of transfer |
| Capital asset / exclusions | 2(14) | rural agri land, stock, personal effects |
| Transfer | 2(47) | includes extinguishment |
| Not transfer | 47 | partition, gift/will, holding↔subsidiary |
| Holding period | 2(42A) | 12m listed / 24m others |
| Computation | 48 | FVC − expenses − cost − improvement |
| STCG listed | 111A | 20% |
| LTCG listed | 112A | 12.5% > ₹1.25L |
| LTCG other | 112 | 12.5%, no indexation |
| Prev-owner cost | 49(1) | cost + holding step-through |
| Stamp value / FMV deeming | 50C / 50CA | 10% band |
| Cost / FMV 01-04-2001 | 55 | goodwill nil |
| House→House | 54 | LTCG or reinvest, lower |
| Any LTCA→House | 54F | proportionate to net consideration |
| Bonds | 54EC | max ₹50L, 6 months, 5-yr lock |
| Depreciable block | 50 | deemed STCG |

**First-principles recap:** capital gains tax exists to catch *realised, real* appreciation — hence the transfer trigger (realisation), historical indexation / lower flat rate (inflation), and rollover exemptions 54/54F/54EC (deferral where the taxpayer merely re-invests, not consumes). Every rule maps to one of those three problems.

> Re-confirm all rates, the ₹1.25 lakh/₹50 lakh limits, holding periods and CII figures against the **current ICAI Study Material and the Finance Act applicable to your attempt** before the exam.
