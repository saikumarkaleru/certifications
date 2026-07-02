# Advanced Accounting — Accuracy Review: Corrections & Caveats

**Scope of this review.** This is a *spot-review*, not an exhaustive audit. I read six of the most error-prone (computation-, section-, and threshold-heavy) chapters in full:

- Ch 31 — Redemption of Preference Shares
- Ch 32 — Buyback of Securities
- Ch 33 — Bonus Issue
- Ch 39 — Amalgamation, Absorption & External Reconstruction (AS 14)
- Ch 40 — Internal Reconstruction
- Ch 20 — AS 20 Earnings Per Share

I re-worked every numerical example in these chapters and cross-checked the section numbers, thresholds, and formulae. The overall quality is high: the arithmetic in the worked examples is **correct throughout**, and the conceptual reasoning is sound. The issues below are mostly citation/legal-position nuances plus one stray figure — not computation errors. Chapters *not* listed here were not reviewed and carry no assurance either way.

Format of each entry: **Chapter/Topic → claim as written → correct position → confidence**.

---

## Findings

### 1. Ch 31 — CRR citation "Section 55(4)"
- **Claim as written (§4.3, repeated in §8 and §10):** *"By Section 55(4) read with Section 63, CRR may be used only for issuing fully paid bonus shares."*
- **Correct position:** There is **no Section 55(4)** in the Companies Act, 2013. Section 55 has only sub-sections (1), (2) and (3). The CRR mechanism on redemption sits in the **proviso to Section 55(2)** (which requires the transfer to CRR and says the CRR "shall be treated as if it were paid-up share capital"), and the permission to *use* CRR for **fully paid bonus shares** comes from **Section 63(1)** (CRR is a listed permitted source for a bonus issue). The *substantive rule* stated (CRR usable only for bonus) is correct — only the "Section 55(4)" pin-cite is wrong.
- **Confidence:** High (that 55(4) does not exist). The rule itself is right.

### 2. Ch 33 — Using free reserves to convert *existing partly-paid* shares into fully-paid
- **Claim as written (§4.6 "Transaction B", and Worked Example 3 part (a)):** existing partly-paid shares can be made fully paid by capitalising **free reserves** (final call raised, then satisfied out of General Reserve with no cash from members), treated as a valid bonus-type application.
- **Correct position — flag for verification:** This was expressly permitted under the **Companies Act, 1956** (old Table A). Under **Section 63 of the Companies Act, 2013**, a bonus issue can only produce **fully paid-up new shares**; the Act does **not** carry forward an explicit route to capitalise reserves to convert partly-paid shares into fully-paid ones. Several current ICAI-aligned readings treat this conversion as **no longer available** under the 2013 Act. The chapter itself hedges ("technically a separate application of reserves"), but presenting Example 3(a) as a clean, valid procedure could mislead in an exam that tests the 2013-Act position. **Verify against the current ICAI Advanced Accounting module** before relying on this in an answer.
- **Confidence:** Medium. (Genuinely contested area; treat as "doubtful — confirm.")

### 3. Ch 39 — Liquidation/amalgamation expenses borne by transferee charged to Capital Reserve
- **Claim as written (Example 3, entry (v)):** the transferor's liquidation expenses (₹40,000 + ₹25,000) reimbursed by the transferee are debited to **Capital Reserve** ("as it is a cost of acquisition"), reducing it to ₹4,35,000.
- **Correct position:** AS 14 gives no explicit rule for the *transferee's* amalgamation expenses, so this is a matter of convention — but the more common ICAI treatment charges such expenses to the **Statement of Profit and Loss** (they are period costs of the acquirer), not to Capital Reserve; some texts add them to Goodwill. The chapter *does* flag the assumption, which is good practice, but the default it picks is not the most widely taught one. If a question is silent, charging to P&L is the safer default and should at least be stated as the alternative.
- **Confidence:** Low-Medium (defensible but not the standard default; the chapter self-flags it).

### 4. Ch 20 — Stray Diluted EPS figure in the presentation extract
- **Claim as written (§6, P&L extract):** for Vega Ltd (Example 1) it shows *"Diluted (Rs.) …… 5.90"* alongside Basic 6.41.
- **Correct position:** Example 1 has **no dilutive instruments** and no diluted-EPS computation anywhere in the chapter; where there are no potential equity shares, **Diluted EPS = Basic EPS = 6.41**. The "5.90" is an unexplained placeholder inconsistent with the worked figure. This is a **cosmetic/illustrative slip**, not a conceptual error, but a student copying the format could be confused.
- **Confidence:** High that it is inconsistent; impact is minor.

---

## Points checked and found CORRECT (worth noting for confidence)

These are the kinds of things that are easy to get wrong; they were verified and are right:

- **Ch 31:** No-irredeemable-pref & 20-year rule (Sec 55(1)/(2)); infrastructure exception 20→30 years with min 10% redemption p.a. from 21st year (Rule 9(6)); CRR = nominal redeemed − fresh-issue nominal; premium on redemption *never* enters CRR; Securities Premium cannot fund CRR. All three worked examples reconcile to the rupee (Capital + CRR preserved).
- **Ch 32:** Sec 68/69/70 framework; the two 25% ceilings (value on capital+reserves vs count on paid-up **equity**) kept correctly separate; post-buyback debt-equity **2:1**; premium written off Securities Premium first then free reserves; CRR on **face** less fresh-issue face; 7-day destruction / no treasury stock; 6-month bar on same-kind fresh issue; 1-year gap between buybacks; board route ≤10%. Examples 1-3 all tie (incl. the 2:1 back-check of 1.27:1). The "securities premium counts in free reserves for the 25% test" point is *self-flagged* and is consistent with ICAI treatment.
- **Ch 33:** Sec 63 six conditions and two prohibitions; Sec 2(43) free-reserves definition (excludes unrealised/revaluation); Revaluation Reserve prohibited; Securities Premium & CRR restricted to fully-paid bonus; SEBI ICDR Ch XI (Regs 293-295) with 15-day / 2-month completion windows and no-withdrawal rule. Net-worth-invariance shown correctly in all three examples.
- **Ch 39:** AS 14 five merger conditions; PC = payments to **shareholders only** (debenture-holders/creditors excluded); Goodwill if PC>NA, Capital Reserve if PC<NA (Purchase); reserves carry over only under Pooling; goodwill amortised over a period presumed ≤5 years. Examples 1-3 balance to the rupee (final BS ₹66,35,000 both sides).
- **Ch 40:** Sec 61 (alteration, ordinary resolution, no Tribunal) vs Sec 66 (reduction, special resolution + NCLT); consolidation-that-changes-voting needs Tribunal; arrears of preference dividend = **no entry** (disclosure only); revaluation *gains* route through the pot; capital-reduction account cannot carry a debit balance. Examples 1-3 all reconcile (the hard Example 3 closes the pot to nil at ₹13,68,000 and the BS ties at ₹12,58,000).
- **Ch 20:** Basic/Diluted formulae; cumulative-vs-non-cumulative preference-dividend rule; bonus/split retrospective (no time-weighting) with comparative restatement; rights-issue TERP and adjustment factor; treasury-stock method for options; anti-dilution sequencing (rank by incremental EPS, most-dilutive first). Every computation verified: Ex 1 = 6.41; Ex 2 restatement 3.00→2.00; Ex 3 TERP 23, factor 25/23, EPS 4.21, prior 3.68; Ex 4 diluted 1.71 with the anti-dilutive preference (incremental 5.00) correctly excluded.

---

## Overall reliability — per reviewed chapter

- **Ch 31 (Redemption of Pref Shares):** **High.** One bad section pin-cite ("Sec 55(4)") to fix; all mechanics and numbers correct.
- **Ch 32 (Buyback):** **High.** No errors found; the only caveat (securities premium in the 25% base) is already self-flagged and matches ICAI.
- **Ch 33 (Bonus Issue):** **High on core; one item to verify.** The partly-paid→fully-paid-via-reserves route (Finding 2) reflects the older Act and should be confirmed against the current 2013-Act/ICAI position before exam use.
- **Ch 39 (Amalgamation):** **High.** Only the liquidation-expenses-to-Capital-Reserve convention (Finding 3) is debatable, and it is disclosed as an assumption.
- **Ch 40 (Internal Reconstruction):** **Very High.** No technical or arithmetic errors found; the hardest example is fully consistent.
- **Ch 20 (AS 20 EPS):** **High.** Conceptually and numerically sound; only a stray "5.90" in a format extract (Finding 4) needs cleaning.

**Bottom line:** Across the six chapters spot-checked, there are **no computation errors and no wrong thresholds/ratios**. The flags are (a) one incorrect statutory sub-section number, (b) one possibly-outdated legal procedure to verify, (c) one debatable-but-disclosed accounting convention, and (d) one cosmetic stray figure. The material is reliable for study, subject to confirming Finding 2 against the current ICAI module. Chapters outside this list were not examined.
