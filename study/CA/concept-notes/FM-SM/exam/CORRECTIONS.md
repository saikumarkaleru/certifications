# Financial Management & Strategic Management — Accuracy Review: Corrections & Caveats

**Scope of this review.** This is a *spot-review*, not an exhaustive audit. I read six of the most error-prone (computational) chapters in full and checked their section numbers, formulas, thresholds, and every worked calculation:

- Ch 03 — Ratio Analysis
- Ch 04 — Cost of Capital
- Ch 05 — Capital Structure & Leverage
- Ch 06 — Capital Budgeting
- Ch 08 — Dividend Decisions
- Ch 09 — Working Capital Management

The remaining chapters (01, 02, 07, and the SM chapters 10–15, plus the cheatsheet) were **not** reviewed. Absence of a chapter here does not mean it is clean — it means it was not checked. Treat everything below as "verify before relying on it in an exam."

Overall, the material is **conceptually strong and, on the numbers, unusually reliable.** I found only **one** concrete arithmetic slip and a small number of minor/definitional caveats. Details follow.

---

## Issues found

### 1. Ch 06 Capital Budgeting → Example 2 (Nirvana Ltd NPV) — arithmetic slip in the PV total
- **Claim as written:** "PV of inflows **24,99,110**" and "**NPV = 24,99,110 − 23,00,000 = ₹1,99,110**."
- **Correct position:** The four discounted inflows are 5,58,125 + 6,09,705 + 5,94,520 + 7,37,760 = **25,00,110** (verified). Therefore **NPV = 25,00,110 − 23,00,000 = ₹2,00,110.** The stated figures are each understated by exactly ₹1,000 (an addition error in the final column total). The individual PV rows in the table are all correct; only the total and the resulting NPV are wrong.
- **Impact:** Cosmetic — the accept/reject conclusion (NPV > 0 → accept) is unchanged. But a student copying the numbers would carry a ₹1,000 error.
- **Confidence:** **High** (independently recomputed).

### 2. Ch 06 Capital Budgeting → Example 1 (discounted payback) — rounding
- **Claim as written:** "Discounted payback = **4.27 years**."
- **Correct position:** Unrecovered at start of Year 5 = 49,300; Year-5 PV = 1,86,300; fraction = 49,300 ÷ 1,86,300 = 0.2646, so **≈ 4.26 years.** The text's 4.27 is a slight over-rounding, not a method error.
- **Confidence:** **Medium** — trivial; flag only for precision.

### 3. Ch 03 Ratio Analysis → Example 5.3, ROE / "Return on Net Worth" — definitional imprecision
- **Claim as written:** "ROE = PAT ÷ Shareholders' funds = 3,36,000 ÷ 16,00,000 = 21%," where the ₹16,00,000 of "Shareholders' funds" **includes ₹2,00,000 of preference capital**, and the numerator PAT (₹3,36,000) is **before** deducting preference dividend.
- **Correct position:** This quantity is more precisely **Return on (total) Shareholders' Funds**. The stricter, more common definition of **Return on *Equity*** uses earnings *after* preference dividend over *equity* shareholders' funds: (3,36,000 − 24,000) ÷ 14,00,000 = 3,12,000 ÷ 14,00,000 = **22.3%.** ICAI accepts the broader "return on net worth = PAT ÷ shareholders' funds" formulation, so the chapter's version is *defensible and internally consistent* (the DuPont reconciliation uses the same 16,00,000 base and ties out to 21%). But a student should know both conventions and read which the question wants — labelling it plainly "ROE" without the preference-adjustment could cost marks in a question that expects the equity-holder view.
- **Confidence:** **Medium** as a caveat (not an outright error; it is a labelling/convention nuance).

---

## Items specifically checked and found SOUND

To reassure the student, these high-risk points were recomputed and are **correct**:

- **Ch 04 Cost of Capital:** All component-cost formulas (irredeemable/redeemable debt with tax shield on interest only, preference, Gordon `D₁/P₀ + g`, CAPM `Rf + β(Rm−Rf)`, `Kr = Ke`). Example 2 book-WACC 18.30% and market-WACC 19.52% verified. Example 3 break point ₹30,00,000, MCC 13.28% / 13.64% / weighted 13.42% all verified. Ordering rule `Kd < Kp < Ke` correctly used as a self-check throughout.
- **Ch 05 Capital Structure & Leverage:** DOL/DFL/DCL formulas and the preference-dividend grossing-up `PD/(1−t)` correct. Example 3 indifference EBITs (A–B = ₹24,00,000; A–C = ₹36,00,000) verified, including the large intermediate products. Example 4 MM figures: NOI `V=EBIT/Ko`; `Ke = Ko+(Ko−Kd)(D/S) = 20%`; MM-with-tax `V_L = V_U + tD` (32.5L + 7L = 39.5L); NI `Ko = 13.9%` — all verified. Theory attributions (NI/NOI/Traditional/MM) accurate.
- **Ch 06 Capital Budgeting:** Cash-flow rules (incremental, sunk, opportunity, working-capital recovery, depreciation only via tax shield, no financing flows) all correct. Example 3 NPV_S ₹1,29,400, NPV_L ₹1,78,000, PIs, IRRs (~25.6% / ~18.9%), incremental IRR ~14.1%, MIRR_S ~18.8%, and the scale-conflict resolution all verified. Straight-line depreciable base = (Cost − Salvage) stated correctly.
- **Ch 08 Dividend Decisions:** Walter `P = [D + (r/Ke)(E−D)]/Ke` and Gordon `P = E(1−b)/(Ke−br)` correct; the `Ke > br` guardrail correctly flagged. All Example 5.1/5.2 prices verified (₹104.17, ₹83.33, ₹100, ₹133.33, etc.). MM Example 5.3 fully verified — both cases give firm value ₹1,00,00,000 (D₁ cancels). Author/year attributions (Walter 1963, Gordon 1962, MM 1961) and **Companies Act 2013 Section 123** for dividends are correct.
- **Ch 09 Working Capital:** Operating-cycle stage denominators (RM→consumption, WIP→cost of production, FG→COGS, debtors→sales, creditors→purchases) correct. Example 1 (GOC 170, CCC 120), Example 2 (WC ₹26,95,000 with correct 100% RM / 50% conversion in WIP), Example 3 credit-policy net gain ₹3,16,667, Example 4 cost-of-forgoing-discount 24.8%, Example 5 Baumol `C* ≈ ₹94,868` — all verified. EOQ `√(2AO/C)`, Baumol `√(2bT/i)`, Miller-Orr spread `3∛(3bσ²/4i)` and return point, reorder level = max usage × max lead time — all stated correctly.

---

## Overall reliability — per reviewed chapter

- **Ch 03 Ratio Analysis:** Reliable. One definitional caveat on the ROE/Return-on-Net-Worth label (Issue 3); all arithmetic and reconciliations (Capital Employed two-route check, DuPont 3-step and 5-step both tie to 21%) are correct.
- **Ch 04 Cost of Capital:** Highly reliable. No errors found; formulas, worked WACC/MCC numbers, and conceptual framing all sound.
- **Ch 05 Capital Structure & Leverage:** Highly reliable. No errors found, including the messy large-number indifference-EBIT algebra.
- **Ch 06 Capital Budgeting:** Reliable, with one ₹1,000 addition slip in Example 2's NPV total (Issue 1) and a trivial rounding in Example 1 (Issue 2). Everything else — including the harder Example 3 IRR/MIRR/incremental analysis — checks out.
- **Ch 08 Dividend Decisions:** Highly reliable. No errors found; models, worked numbers, assumptions, and attributions all correct.
- **Ch 09 Working Capital Management:** Highly reliable. No errors found across five worked examples and all formulas.

**Bottom line:** Of six computational chapters audited line-by-line, only Chapter 06 contains a genuine (and minor, decision-neutral) numerical error. The guide is trustworthy for study; nonetheless, always re-derive final totals yourself, and note the unreviewed chapters (01, 02, 07, 10–15, cheatsheet) have not been checked.
