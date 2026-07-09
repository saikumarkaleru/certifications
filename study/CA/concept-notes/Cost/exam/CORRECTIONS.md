# Cost & Management Accounting — Accuracy Review: Corrections & Caveats

**Scope of this review.** This is a *spot-review*, not an exhaustive audit. I read six of the sixteen chapters in full and focused on the most error-prone, computation-heavy material:

- Ch 02 — Material Cost (EOQ, stock levels, FIFO/LIFO/WA, loss valuation)
- Ch 03 — Employee (Labour) Cost (idle time, overtime, turnover, Halsey/Rowan)
- Ch 04 — Overheads / Absorption (primary & secondary distribution, MHR, under/over-absorption)
- Ch 10 — Process & Operation Costing (normal/abnormal loss & gain, equivalent units, inter-process profit)
- Ch 13 — Standard Costing & Variance Analysis (all variance families + reconciliation)
- Ch 14 — Marginal Costing & CVP (contribution, BEP, marginal vs absorption, decisions)

I also spot-checked the definitions in Ch 01 and Ch 11. **I did not review Chapters 05, 06, 07, 08, 09, 12, 15, or the cheatsheet (00).** Absence of a chapter here is *not* a clean bill of health — it simply wasn't examined. Please verify anything material against the current ICAI study module, as the notes are AI-written.

**Headline finding:** The *technical content and arithmetic in the sampled chapters is strong.* Every worked computation I re-performed reconciled correctly, and the conceptual treatment (loss accounting, variance decomposition, contribution logic, absorption treatment) is sound and ICAI-aligned. The defects I did find are (1) a **pervasive internal cross-referencing error** — chapters point to each other using wrong chapter numbers — plus (2) one **garbled table cell** and (3) one **sourcing caveat**. None of these will mislead you on the *technique*; the first will only confuse you when navigating between chapters.

---

## Issue 1 — Wrong chapter numbers in "Connections" sections (systematic, HIGH confidence)

The "Connections" sections (and a few inline references) repeatedly cite **incorrect chapter numbers**. The book's actual numbering is: 01 Intro, 02 Material, 03 Labour, 04 Overheads, 05 ABC, 06 Cost Sheet, 07 Cost Systems, 08 Unit/Batch, 09 Job/Contract, 10 Process, 11 Joint, 12 Service, 13 Standard Costing, 14 Marginal, 15 Budgets. Many references were evidently written against an older numbering and never updated.

| Chapter/Topic | The claim as written | The correct position | Confidence |
|---|---|---|---|
| Ch 13 Standard Costing → Connections | "Marginal costing (Ch. 12)" | Marginal costing is **Ch. 14** | High |
| Ch 13 Standard Costing → Connections & §7 | "Overheads & absorption (Ch. 9)" / "over/under-absorption of Chapter 9" | Overheads is **Ch. 04** | High |
| Ch 13 Standard Costing → Connections | "Budgetary control (Ch. 14)" | Budgets is **Ch. 15** | High |
| Ch 13 Standard Costing → Connections | "Material & labour costing (Ch. 4–5)" | Material **Ch. 02**, Labour **Ch. 03** | High |
| Ch 14 Marginal Costing → Connections | "Standard costing & variances (Ch. 15)" | Standard costing is **Ch. 13** | High |
| Ch 14 Marginal Costing → Connections | "Budgeting & flexible budgets (Ch. 16)" | Budgets is **Ch. 15** (there is no Ch. 16) | High |
| Ch 10 Process Costing → Connections | "Material & Labour Costing (Ch. 3–4)" | Material **Ch. 02**, Labour **Ch. 03** | High |
| Ch 10 Process Costing → Connections | "Overheads (Ch. 6)" | Overheads is **Ch. 04**; Ch. 06 is Cost Sheet | High |
| Ch 11 Joint Products → Connections | "Cost Sheet & overhead apportionment (Ch. 3–4)" | Cost Sheet **Ch. 06**, Overheads **Ch. 04** | High |
| Ch 02 Material → Connections | "Cost Sheet (Ch. 01 / 03)" | Cost Sheet is **Ch. 06** | High |
| Ch 03 Labour → Connections | "Cost Sheet (Ch. 02 / overheads)" | Cost Sheet is **Ch. 06**; Overheads **Ch. 04** | High |
| Ch 04 Overheads → Connections | "Chapter 03 (Material & Labour)" and "cost sheet (Ch. 02)" | Material is **Ch. 02** (labour Ch. 03); Cost Sheet is **Ch. 06** | High |

*Note:* A few references are correct (e.g., Ch 14 citing "Overhead absorption (Ch. 4)" and "Cost sheet (Ch. 6)"; Ch 11 citing Process Ch. 10 and Marginal Ch. 14). The pattern is inconsistent, so treat **every** cross-chapter pointer with suspicion and navigate by chapter title, not number. **This is a navigation/citation defect only — it does not affect any formula or concept.**

---

## Issue 2 — Garbled table cell in Ch 10, Example 5 (inter-process profit) (MEDIUM confidence it is a typo)

- **The claim as written:** In the "Process II — goods available" table, the "Wages added" row shows the Total column as `30,000 → 10,000` (a leftover editing artefact), i.e. the cell reads "30,000 → **10,000**".
- **The correct position:** Wages added = Cost ₹10,000, Profit nil, **Total ₹10,000**. The stray "30,000 →" should not be there. The downstream arithmetic is unaffected — "Goods available" is correctly totalled as Cost 80,000 / Profit 10,000 / **Total 90,000**, and the rest of the example (unrealised profit ₹2,000, realised profit ₹32,000) is correct and reconciles. Purely a display slip in one cell.
- **Confidence:** High that it is a typo; Low impact.

---

## Issue 3 — CAS-1 attribution of the terminology definitions (LOW–MEDIUM confidence; verify)

- **The claim as written (Ch 01, §3):** "Two definitions to anchor the vocabulary (ICAI, *Cost Accounting Standards / CAS-1*)," then defines **Cost** as "the amount of expenditure (actual or notional) incurred on, or attributable to, a specified thing or activity," plus **Costing / Cost Accounting / Cost Accountancy**.
- **The correct position:** The wording quoted for "Cost" is the classic **CIMA/ICMA Terminology** definition, and the Costing / Cost Accounting / Cost Accountancy definitions are also traditionally from that terminology, *not* from CAS-1. **CAS-1's** title is "Classification of Cost," and its own definition of cost reads "a measurement, in monetary terms, of the amount of resources used for the purpose of production of goods or rendering of services." So attributing this specific wording to CAS-1 is imprecise. The *definitions themselves are standard and exam-acceptable* — only the citation is questionable.
- **Confidence:** Low–Medium. Harmless for problem-solving, but if a theory question asks you to "state the CAS-1 definition of cost," quote the CAS-1 wording above, not the CIMA one. Verify against your ICAI module.

---

## Things I specifically checked and found SOUND

These are areas where students often catch AI errors; I re-performed the maths and found them correct:

- **Ch 02 EOQ (Example 1):** √(2×12,000×150/4) = 948.68 units; ordering cost = carrying cost = ₹1,897.4 at EOQ. Correct. Cost-table (Example 2) correctly bottoms out at EOQ. Stock-level formulas (ROL = max×max, Min, Max, Danger) all correct; the two average-stock formulas giving 2,100 vs 2,450 are honestly flagged. FIFO/LIFO/WA ledger (Example 4) reconciles to ₹11,600 in every method; rising-price profit ranking correct. Abnormal-loss valuation (Example 5) uses expected good output (900), not actual — correct.
- **Ch 03 Labour:** Halsey/Rowan formulas and the 50%-time-saved crossover are correct, including the algebraic proof and the T=30 (equal) and T=20 (Halsey wins) cross-checks. Turnover example correctly isolates the 125 expansion hires from the 25 replacements. Overtime split (Factories Act, double rate; premium traced by cause) correct.
- **Ch 04 Overheads:** MHR build-up (Example 1) reconciles to ₹1,20,000. Reciprocal distribution by simultaneous equations (S1 = 9,581.56, S2 = 7,382.98) and repeated distribution both land P1 ≈ 45,548 / P2 ≈ 34,452 = ₹80,000. Under/over-absorption sign logic and supplementary-rate treatment correct. Apportionment-basis table correct.
- **Ch 10 Process Costing:** Normal-loss denominator (input − normal loss), abnormal loss/gain at normal cost per unit, the abnormal-gain scrap correction, and the WA-vs-FIFO equivalent-unit example (both reconcile to ₹3,38,000; WA transfer 3,15,000 vs FIFO 3,13,500) are all correct.
- **Ch 13 Standard Costing:** All four worked examples reconcile at every node of the variance tree (material price+usage=cost, mix+yield=usage; labour rate+efficiency+idle=cost; VOH exp+eff=cost; FOH exp+volume=cost, capacity+efficiency=volume; sales margin price+volume=total, mix+quantity=volume). The mix/yield example (MCV 12,050 A = MPV 2,300 A + MUV 9,750 A; MMV 7,833.33 A + MYV 1,916.67 A) checks exactly, and the sales-margin reconciliation lands on ₹53,500. Sign conventions and hours-paid-vs-worked handling are correct.
- **Ch 14 Marginal Costing:** Full CVP toolkit (Example 1) including after-tax gross-up (₹63,000/0.7 = ₹90,000 → sales ₹7,25,000) correct. Marginal-vs-absorption reconciliation (₹30,000 fixed OH in 2,000 units of closing stock) correct. Limiting-factor mix (rank by contribution/machine-hour: B 30, A 20, C 15 → profit ₹3,40,000, with the ₹40,000 proof of optimality) correct.

---

## Overall reliability — per reviewed chapter

- **Ch 02 Material Cost — RELIABLE.** Only defect: a wrong cross-reference to the cost-sheet chapter. Computations and concepts solid.
- **Ch 03 Labour Cost — RELIABLE.** No technical errors found. Only a wrong cost-sheet/overheads cross-reference.
- **Ch 04 Overheads — RELIABLE.** No technical errors found. Wrong chapter numbers in Connections only.
- **Ch 10 Process Costing — RELIABLE, with one cosmetic typo** (Issue 2) and wrong cross-reference numbers. Core accounting is correct.
- **Ch 13 Standard Costing — RELIABLE.** Strongest chapter computationally; every variance reconciles. Only the Connections chapter numbers are wrong.
- **Ch 14 Marginal Costing — RELIABLE.** No technical errors; two wrong forward-references (to standard costing and budgeting chapters).
- **Ch 01 Intro — mostly sound**, but treat the CAS-1 citation (Issue 3) with care.
- **Ch 11 Joint Products — definitions and method logic spot-checked and sound** (NRV, physical-units, market-value-at-split-off correctly described); not fully audited.

**Bottom line:** For exam preparation the sampled chapters are trustworthy on *method and numbers*. Fix the cross-reference numbers in your head (navigate by title), ignore the one garbled cell in Ch 10 Example 5, and quote the CAS-1 definition from the ICAI module rather than the notes if a theory question demands it. Chapters not listed above remain unverified — apply the same "verify against ICAI" caution there.
