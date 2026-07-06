# Q&A — Basel Accords and Capital Regulation

A practice bank for the Basel Accords chapter. Work each question before reading the answer. Numerical answers are self-checked against the master identities **CAR = Capital / RWA**, **RWA = credit + market + operational**, and the tier nesting **CET1 ≤ Tier 1 ≤ Total Capital**.

---

## Section A — Concept-Check (short answer)

**A1. State the master equation of capital regulation and name its two parts.**

The Capital Adequacy Ratio (CAR / CRAR): **CAR = Regulatory Capital / Risk-Weighted Assets ≥ minimum %.** The numerator is *loss-absorbing capital* (tiered by quality — CET1, then AT1, then Tier 2). The denominator is *risk-weighted assets* — assets scaled by a weight reflecting how likely they are to lose value, not raw balance-sheet size. The whole framework is an elaboration of this fraction.

**A2. Why does Basel measure capital against risk-weighted assets rather than raw assets?**

A flat "hold 8% of total assets" rule would charge the same capital for a Treasury bill as for a junk loan. Rational banks would then shed safe, low-yield assets (which cost capital but earn little) and pile into risky, high-yield ones (same capital, more return). A raw-asset rule actively *encourages* risk-taking. Risk weighting ties the capital charge to the actual probability and severity of loss, so capital sits where losses are likely to come from.

**A3. Why is bank capital tiered by quality?**

Not all capital absorbs loss equally. Common equity (CET1) absorbs loss immediately and continuously while the bank is alive (going concern) with no obligation to repay. Subordinated debt (Tier 2) only absorbs loss in a wind-down (gone concern). Basel ranks capital by loss-absorbing quality and demands the bulk of the requirement be met with the highest form. 2008 proved the point: banks that looked well-capitalised on total-capital measures had little real equity underneath, and it was the equity the market cared about.

**A4. Note the counter-intuitive tier ordering.**

Tiers rank *downward* in quality: **Tier 1 is better than Tier 2**, and within Tier 1, **CET1 is the best**. A higher tier number is worse capital, not better — the common trap.

**A5. State the three pillars of Basel II.**

**Pillar 1** — minimum capital requirements (quantitative charges for credit, market, operational risk). **Pillar 2** — supervisory review (supervisors assess risks missed by Pillar 1, e.g. concentration, interest-rate risk in the banking book, and can require more capital bank-by-bank via ICAAP). **Pillar 3** — market discipline (mandatory public disclosure so the market can price and monitor bank risk).

**A6. What are the Basel III Pillar 1 minimum ratios?**

CET1 ≥ **4.5%** of RWA; Tier 1 (CET1 + AT1) ≥ **6.0%**; Total Capital (Tier 1 + Tier 2) ≥ **8.0%**. On top sit buffers met with CET1: the **capital conservation buffer (2.5%)**, the **countercyclical buffer (0–2.5%)**, and **G-SIB/D-SIB surcharges (1–3.5%)**.

**A7. What does the leverage ratio do that the CAR cannot?**

The leverage ratio = **Tier 1 / Total Exposure (unweighted) ≥ 3%**. Its denominator applies *no risk weights* — a €1 Treasury and a €1 junk loan count the same. This is the risk-blind backstop: if the risk weights themselves are wrong or gamed (as with AAA structured products pre-2008), the risk-weighted CAR lies, but the leverage ratio still binds. A bank must satisfy *both* a risk-sensitive and a risk-blind constraint.

**A8. Distinguish LCR from NSFR.**

Both are liquidity standards but over different horizons. **LCR** (Liquidity Coverage Ratio) = HQLA / 30-day stressed net outflows ≥ 100% — the *sprint*, survive an acute month-long run. **NSFR** (Net Stable Funding Ratio) = Available Stable Funding / Required Stable Funding over one year ≥ 100% — the *marathon*, be structurally sound so illiquid long assets are funded with sticky money. A bank can pass one and fail the other.

**A9. Capital ratios and liquidity ratios cure different diseases — which?**

Capital protects against **insolvency** (losses exceeding the equity cushion). Liquidity ratios protect against **illiquidity** (unable to meet cash outflows in time, even while solvent). Northern Rock (2007) was solvent but died from a run. Different failure modes, different medicine: CAR/leverage vs LCR/NSFR.

**A10. What is the output floor and what problem does it solve?**

Under the Basel III endgame (2017), RWA computed with a bank's internal (IRB) models cannot fall below **72.5% of the standardised-approach RWA**. It caps how much capital benefit banks can extract from optimistic internal models — a floor against model-gaming while retaining risk sensitivity.

**A11. Why is expected loss NOT covered by regulatory capital?**

Expected loss (PD × LGD × EAD) is the predictable average, covered by **provisions** and priced into the loan. Regulatory capital covers **unexpected loss** — the deviation *above* the mean. Treating expected loss as a capital item double-counts and inflates the requirement.

**A12. Is Basel law?**

No. The BCBS issues *standards*, not legislation. They become binding only when a jurisdiction transposes them into local rules — EU via CRR/CRD, US via the federal banking agencies, India via RBI norms — often with local deviations and timelines.

---

## Section B — Numerical / Applied (full solutions)

**B1. Compute credit RWA.** A bank holds: cash €400m (0%), top-rated government bonds €800m (0%), interbank exposures €300m (20%), residential mortgages €1,500m (35%), unrated corporate loans €2,000m (100%), past-due loans €100m (150%). Find credit RWA.

Weight each exposure:
- Cash: 400 × 0% = 0
- Govt bonds: 800 × 0% = 0
- Interbank: 300 × 20% = 60
- Mortgages: 1,500 × 35% = 525
- Corporate: 2,000 × 100% = 2,000
- Past-due: 100 × 150% = 150

Credit RWA = 0 + 0 + 60 + 525 + 2,000 + 150 = **€2,735m.**

**B2. Full ratio stack.** Add market RWA = €200m and operational RWA = €400m to B1. Capital: CET1 = €300m, AT1 = €40m, Tier 2 = €90m. Compute total RWA and all three capital ratios.

Total RWA = 2,735 + 200 + 400 = **€3,335m.**
Tier 1 = 300 + 40 = €340m. Total Capital = 340 + 90 = €430m.

- CET1 ratio = 300 / 3,335 = **9.00%**
- Tier 1 ratio = 340 / 3,335 = **10.19%**
- Total CAR = 430 / 3,335 = **12.89%**

*Self-check:* tiers nest, 300 ≤ 340 ≤ 430, and ratios rise accordingly 9.00% ≤ 10.19% ≤ 12.89%. ✅ Against a non-systemic bank's requirements (CET1 7.0% incl. buffer, Tier 1 6.0%, Total 10.5% incl. buffer), the bank passes all three.

**B3. RWA from a capital charge.** A market-risk model produces a capital charge of K = €24m. Express this as RWA.

RWA = K × 12.5 = 24 × 12.5 = **€300m.** (The 12.5 is the reciprocal of the 8% total-capital ratio, so a €24m charge at 8% implies €300m of RWA.)

*Self-check:* 8% × 300 = 24. ✅

**B4. Loss absorption.** The bank in B2 suffers a €260m loss on its corporate book; assume the defaulted exposures (which carried €260m of 100%-weighted RWA) are written off entirely. Trace CET1 and recompute the CET1 ratio.

Losses hit CET1 first: new CET1 = 300 − 260 = **€40m.**
New total RWA = 3,335 − 260 = **€3,075m.**

New CET1 ratio = 40 / 3,075 = **1.30%.**

*Interpretation:* the bank is still solvent (capital > 0) but has crashed through the 4.5% CET1 minimum. Crucially, depositors lost nothing — the entire €260m loss fell on shareholders' equity (CET1 300 → 40). This is exactly what capital is for. AT1 and Tier 2 are untouched because CET1 was not fully exhausted, consistent with the going-concern loss ordering.

**B5. Leverage ratio.** Using B2's capital, the leverage exposure measure (unweighted on- and off-balance-sheet) is €5,500m. Compute the leverage ratio and state whether it or the CET1 ratio is the binding constraint.

Leverage ratio = Tier 1 / Total Exposure = 340 / 5,500 = **6.18% ≥ 3%.** ✅

Leverage headroom is +3.18% (6.18 − 3.0). CET1 headroom is +2.00% (9.00 − 7.0). The **risk-weighted CET1 constraint is tighter**, typical of a bank with genuinely risky assets. For a bank stuffed with 0%-weighted sovereigns, the reverse holds and leverage bites — which is why the backstop exists.

**B6. LCR.** A bank holds HQLA = €900m (all Level 1, 0% haircut). Stress outflows: retail deposits €3,000m × 5% run-off; wholesale funding €1,000m × 40%; undrawn lines €400m × 10%. Contractual inflows €250m (cap at 75% of outflows). Compute the LCR.

Outflows = 3,000×5% + 1,000×40% + 400×10% = 150 + 400 + 40 = **€590m.**
Inflow cap = 0.75 × 590 = 442.5 ≥ 250, so full €250m counts.
Net outflows = 590 − 250 = **€340m.**

LCR = 900 / 340 = **264.7% ≥ 100%.** ✅

*Self-check:* outflows 590 = 150 + 400 + 40. ✅ Inflows uncapped since 250 < 442.5. ✅ The bank holds ~2.6× the HQLA needed for a 30-day stressed run.

**B7. NSFR.** Available Stable Funding = €4,200m; Required Stable Funding = €4,000m. Compute NSFR and interpret.

NSFR = ASF / RSF = 4,200 / 4,000 = **105% ≥ 100%.** ✅ The bank's stable funding exceeds what its assets require over a one-year horizon — structurally sound, though the 5% margin is thin, so growth in illiquid long-term lending (high RSF) without matching stable funding could breach it.

**B8. Buffer requirement for a G-SIB.** A globally systemic bank faces a 2.0% G-SIB surcharge in a period with a 1.0% countercyclical buffer active. What total CET1 (as % of RWA) must it hold?

CET1 minimum 4.5% + conservation buffer 2.5% + countercyclical 1.0% + G-SIB surcharge 2.0% = **10.0% of RWA**, all in CET1.

---

## Section C — Interview-Style (model answers)

**C1. Why add a leverage ratio if you already have the CAR?**

Because the CAR trusts the risk weights, and risk weights can be wrong or deliberately gamed. Before 2008, banks loaded up on AAA-rated structured products and sovereign debt carrying tiny risk weights; their risk-weighted ratios looked healthy right up until they collapsed. The leverage ratio (Tier 1 / total unweighted exposure ≥ 3%) is the risk-blind backstop — it treats every euro of exposure the same, so a bank cannot escape it by claiming its assets are low-risk. The two constraints bind in different situations: the CAR bites on a genuinely risky book, the leverage ratio bites on a book stuffed with low-weight assets. Together they mean a bank must be safe on both a risk-sensitive and a risk-blind measure.

**C2. Explain CET1 versus Tier 2 in one breath, then why it mattered in 2008.**

CET1 absorbs losses while the bank is still alive — a going-concern buffer of common equity and retained earnings that falls the instant the bank loses money, with no repayment obligation. Tier 2 (subordinated debt) only absorbs loss in a wind-down, gone-concern. In 2008, many banks met their headline total-capital requirements largely with lower-quality instruments, so on paper they looked fine, but the market recognised that only real equity could actually absorb the mounting losses. Basel III's central fix was to put CET1 at the centre — raising the CET1 minimum and tightening what qualifies — because it is the capital that actually keeps a bank standing.

**C3. What exactly did Basel III fix from Basel II?**

Four things. First, *soft capital* — Basel III made the framework CET1-centric with stricter definitions. Second, *procyclicality* — the countercyclical buffer leans against the credit cycle, built up in booms, released in busts. Third, *no liquidity standard at all* — it added the LCR (30-day) and NSFR (1-year). Fourth, *over-reliance on internal models and external ratings* — the endgame reforms added an output floor (IRB RWA ≥ 72.5% of standardised) and revised the standardised approaches. It didn't discard Basel II's three-pillar architecture; it hardened every part of it.

**C4. A junior analyst says "our CAR is 12%, so we hold 12% of our assets as capital." Correct them.**

That's 12% of *risk-weighted* assets, not total assets. Because most assets carry weights below 100% — cash and top sovereigns are 0%, mortgages ~35% — RWA is usually much smaller than the balance sheet. So capital as a fraction of *total* assets is materially lower than 12%. That very gap is why the leverage ratio was introduced: it puts capital over *unweighted* exposure to reveal the true fulcrum the bank is levered on.

**C5. How does capital actually protect a depositor?**

Through the loss waterfall. When the bank loses money, the loss falls on CET1 (shareholders' equity) first, then AT1, then Tier 2, and only if all of that is exhausted do depositors and senior creditors take a hit. So the larger the CET1 cushion, the more loss the bank can absorb before a depositor loses a cent. In my B4 example, a €260m loss took CET1 from €300m to €40m and depositors were entirely untouched — equity did its job. Capital is the shield standing between asset losses and the deposit base.

**C6. Why not just require banks to hold 50% capital and end the fragility debate?**

Because capital isn't free from the bank's perspective. Equity investors demand a higher return than depositors, and frictions like the tax-deductibility of debt and the safety-net subsidy make equity privately expensive, so more equity can raise funding costs and shrink lending. (The Modigliani-Miller view argues leverage shouldn't change *total* funding cost, but those frictions break the idealisation in practice.) Regulation therefore sits on a trade-off curve: too little capital and the system is fragile; too much and credit becomes scarce and costly. Basel's minimums are the negotiated answer to where on that curve to sit — not a claim that more is always better.

---

## Section D — MCQs (with reasoning)

**D1. Under Basel III, the minimum CET1 ratio (before buffers) is:**
(a) 2.0% (b) 4.5% (c) 6.0% (d) 8.0%

**Answer: (b) 4.5%.** 6.0% is the Tier 1 minimum; 8.0% is Total Capital. Adding the 2.5% conservation buffer brings the *effective* CET1 requirement to 7.0%, but the hard minimum is 4.5%.

**D2. The leverage ratio differs from the CAR primarily because its denominator:**
(a) uses Tier 1 capital only (b) applies no risk weights (c) excludes off-balance-sheet items (d) is measured over 30 days

**Answer: (b) applies no risk weights.** The leverage ratio's exposure measure is unweighted — that risk-blindness is the entire point of a backstop. (a) describes the numerator, not the denominator; (c) is false — it *includes* off-balance-sheet items; (d) confuses it with the LCR.

**D3. Expected loss on a loan book is properly covered by:**
(a) CET1 capital (b) Tier 2 capital (c) provisions (d) the countercyclical buffer

**Answer: (c) provisions.** Expected loss (PD×LGD×EAD) is the predictable average, provisioned and priced in. Regulatory capital of all tiers covers *unexpected* loss. Charging expected loss to capital double-counts.

**D4. Which correctly orders capital from highest to lowest loss-absorbing quality?**
(a) Tier 2 > AT1 > CET1 (b) AT1 > CET1 > Tier 2 (c) CET1 > AT1 > Tier 2 (d) CET1 > Tier 2 > AT1

**Answer: (c) CET1 > AT1 > Tier 2.** Tiers rank downward in quality; CET1 (common equity, going-concern) is best, AT1 next (perpetual, converts/writes down at trigger), Tier 2 (subordinated debt, gone-concern) last.

**D5. The LCR requires a bank to survive a stressed period of:**
(a) 7 days (b) 30 days (c) 90 days (d) one year

**Answer: (b) 30 days.** LCR is the short-term sprint over 30 days; the one-year structural test is the NSFR.

**D6. The output floor under the Basel III endgame sets modelled (IRB) RWA at no less than:**
(a) 50% (b) 60% (c) 72.5% (d) 100% of standardised RWA

**Answer: (c) 72.5%.** IRB RWA ≥ 72.5% × standardised RWA — a cap on the capital benefit of internal models while keeping risk sensitivity.

**D7. To convert a capital charge K into RWA under Basel, you multiply by:**
(a) 8 (b) 10 (c) 12.5 (d) 0.08

**Answer: (c) 12.5.** RWA = K × 12.5, the reciprocal of the 8% total-capital ratio. Multiplying by 0.08 would go the wrong direction (RWA → charge).

**D8. A bank with a 6% CET1 ratio, 3% conservation buffer requirement, and no other buffers:**
(a) fully meets its CET1 requirement with headroom (b) meets the minimum but is inside the conservation buffer (c) breaches the hard CET1 minimum (d) must be resolved immediately

**Answer: (b) meets the minimum but is inside the conservation buffer.** The 4.5% hard minimum is met (6% > 4.5%), but the effective requirement is 4.5% + 2.5% = 7.0% (the standard conservation buffer is 2.5%, not 3%). At 6% the bank sits *inside* the buffer, which restricts dividends and bonuses but does not trigger resolution — buffers are designed to be usable in stress. (The 3% in the question is a distractor; the standard conservation buffer is 2.5%.)

---

*Self-verification note.* Every numerical answer was checked against CAR = Capital/RWA and the tier nesting CET1 ≤ Tier 1 ≤ Total. B2 ratios rise monotonically with tier (9.00 ≤ 10.19 ≤ 12.89). B3/B7 reconcile by the 12.5 and 100% identities. B4 confirms losses hit CET1 first and depositors are protected. Minimums used throughout: CET1 4.5%, Tier 1 6.0%, Total 8.0%, conservation buffer 2.5%, leverage 3%, LCR/NSFR 100%, output floor 72.5%.
