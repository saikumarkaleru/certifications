# Q&A — Types of Financial Risk

Practice bank for Chapter 02. Every question is followed by a full answer. Work each numerical item on paper before reading the solution.

---

## Section A — Concept Checks

**A1. Why is the single word "risk" useless to a Chief Risk Officer, and what is the first job of risk management?**

Because nobody can hedge, reserve capital against, price, or assign an owner to an undifferentiated "risk." You can only manage what you can *name, measure, and attribute*. The first job is **taxonomy**: cutting the fog of "risk" into distinct categories defined by their *source of loss* — market, credit, liquidity, operational, model, legal/compliance, reputational, systemic — because the source dictates the measurement method, the owner, the capital charge, and the hedging tool.

**A2. State the loss driver — "what has to happen in the world to lose money" — for market, credit, liquidity, and operational risk.**

- Market risk: a **price/rate/FX/vol has to move** adversely. Fast, symmetric-ish, observed daily.
- Credit risk: a **counterparty has to break a promise** (default or downgrade). Slow, asymmetric, rare events.
- Liquidity risk: you have to be **unable to raise cash or sell an asset** near fair value. A threshold/knock-out risk, not distributional.
- Operational risk: an **internal process, person, or system has to fail** (or an external event hits). Fat-tailed, control-driven.

**A3. Distinguish "financial" from "non-financial" risks in this taxonomy, and say why the distinction matters.**

Financial risks — market, credit, liquidity — are taken **deliberately to earn a return**; you optimise them (take the right amount for the reward). Non-financial risks — operational, model, legal/compliance, reputational — are **unrewarded by-products** of doing business; you minimise them. It matters because you do not "optimise" an operational-risk appetite the way you size a trading position: unrewarded risk should be driven as low as cost-effectively possible.

**A4. VaR is often described as "the worst case." Correct the statement.**

VaR is the **best of the worst**, not the worst case. The 99% 1-day VaR is the *minimum* loss you'd expect on the worst 1% of days — the threshold you will not exceed at that confidence — not the maximum possible loss. It says nothing about how deep the tail beyond it runs; **Expected Shortfall** (the average loss *given* you breached VaR) answers that.

**A5. "Expected Loss is what capital covers." Why is this backwards?**

Expected Loss (EL = PD × LGD × EAD) is the *average* credit loss; it is a predictable cost, so it is **priced into the spread and provisioned**, not a surprise. **Capital covers Unexpected Loss (UL)** — the volatility of loss around the mean, the tail that a bad year actually delivers. Confusing the two under-capitalises the book: EL is small and priced, UL is large and must be absorbed by equity.

**A6. Why can a fully solvent bank still fail? Name the risk and two historical cases.**

Solvency (assets > liabilities) and liquidity (cash when obligations fall due) are different. A solvent firm can suffer a **funding-liquidity** run — depositors or lenders demand cash faster than assets can be realised — and fail before its assets are ever marked down. Examples: **Lehman Brothers**, **Northern Rock**, and **SVB (2023)**. SVB's bonds were money-good to maturity; it died of funding liquidity, not asset loss.

**A7. Give Basel's definition of operational risk, and state precisely what it includes and excludes.**

Operational risk is the risk of loss from **inadequate or failed internal processes, people, and systems, or from external events**. It **includes legal risk** but **excludes strategic and reputational risk**. This inclusion/exclusion is a classic exam trap.

**A8. Why is model risk called a "meta-risk"?**

Because it does not produce losses directly — it **corrupts the measurement of every other risk**. A wrong PD understates credit risk; a wrong volatility surface understates market risk; a wrong correlation assumption (the Gaussian copula in 2008) misprices a whole book. It has no clean formula: it is **governed** (independent validation, back-testing, benchmarking per SR 11-7), not computed.

**A9. What makes systemic risk different from every other category, and who must manage it?**

It is the risk **of the system itself** — cascade failure through interconnection, common holdings, fire-sale externalities, and funding freezes — not risk *within* one firm. Its defining feature is that **an individual firm cannot diversify it away**, so it must be managed **macro-prudentially by a regulator** (G-SIB surcharges, countercyclical buffers, central clearing, system-wide stress tests), not by a single risk desk.

**A10. Explain the phrase "crises live in the arrows, not the boxes."**

The neat taxonomy boxes are how we measure risk in calm times. But real crises **transmit and amplify across categories**: a market shock triggers margin calls (liquidity), forced fire sales deepen the price fall (market-liquidity feedback), covenant breaches follow (credit), and correlated de-risking spreads it (systemic). Standalone or summed VaR assumes the arrows are switched off; a crisis switches them on and correlations converge toward 1, so isolated measurement systematically **understates stressed loss**.

---

## Section B — Numerical / Applied (full solutions)

**B1. Parametric VaR and square-root-of-time scaling.**
A desk holds a ₹80 crore equity position with daily return volatility σ = 1.5%. Find the 1-day 99% VaR and the 10-day 99% VaR.

*Solution.* Parametric VaR = z_c × σ × V × √h, with z₉₉ = 2.326.
1-day: VaR = 2.326 × 0.015 × 80 = **₹2.7912 crore ≈ ₹2.79 cr.**
10-day: scale by √10 = 3.1623. VaR₁₀ = 2.7912 × 3.1623 = **₹8.826 cr ≈ ₹8.83 cr.**
*Check:* dimensional sanity — 1.5% of ₹80 cr is ₹1.2 cr of one-sigma move; 2.326 sigma ≈ ₹2.79 cr ✓. Scaling assumes i.i.d. returns and a constant position.

**B2. Portfolio VaR and the diversification benefit.**
Add to B1's equity VaR (₹2.7912 cr) a ₹80 cr bond position with daily σ = 0.4%, correlation ρ = 0.25 with the equity. Find the bond VaR, the portfolio 1-day 99% VaR, and the diversification benefit.

*Solution.*
Bond VaR = 2.326 × 0.004 × 80 = **₹0.74432 cr.**
Portfolio: VaR_p = √(VaR₁² + VaR₂² + 2ρ·VaR₁·VaR₂)
= √(2.7912² + 0.74432² + 2·0.25·2.7912·0.74432)
= √(7.7908 + 0.5540 + 1.0388) = √9.3836 = **₹3.0633 cr.**
Undiversified sum = 2.7912 + 0.74432 = ₹3.5355 cr.
**Diversification benefit = 3.5355 − 3.0633 = ₹0.4722 cr (13.4%).**
*Check:* set ρ = 1 → √((2.7912+0.74432)²) = 3.5355, exactly the undiversified sum, confirming the algebra. For ρ < 1 the portfolio VaR must be lower ✓.

**B3. Expected Loss and break-even spread.**
An NBFC lends ₹60 crore (EAD) at 1-year PD = 3%, recovery rate = 45% (so LGD = 55%). Find EL and the minimum spread (over funding cost) that just covers expected credit loss.

*Solution.*
EL = PD × LGD × EAD = 0.03 × 0.55 × 60 = **₹0.99 cr = ₹99 lakh.**
Break-even spread = EL / EAD = 0.99 / 60 = **1.65% = 165 bps.**
So the loan must earn ~165 bps over funding **just to break even on expected losses** — before profit or the capital charge on unexpected loss.

**B4. Unexpected Loss from first principles.**
For the B3 loan (EAD ₹60 cr, PD 3%, LGD 55% deterministic), find UL and confirm it against a direct two-state variance calculation.

*Solution (formula).*
UL = EAD × LGD × √(PD(1−PD)) = 60 × 0.55 × √(0.03 × 0.97)
= 33 × √0.0291 = 33 × 0.17059 = **₹5.629 cr.**
*Direct check.* Loss is ₹0 with prob 0.97, and LGD×EAD = 0.55×60 = ₹33 cr with prob 0.03.
Mean = 0.03 × 33 = ₹0.99 cr = EL ✓.
Variance = 0.03 × 0.97 × 33² = 0.0291 × 1089 = 31.69; std dev = √31.69 = **₹5.629 cr = UL** ✓.
*Insight:* UL (₹5.63 cr) is ~5.7× EL (₹0.99 cr). A single default costs ₹33 cr, not ₹0.99 cr — that tail is what capital must absorb; the mean is merely what the spread covers.

**B5. Expected Shortfall vs VaR (discrete tail).**
A ₹100 cr book has these loss outcomes over the horizon: ₹0 (prob 0.90), ₹5 cr (0.06), ₹20 cr (0.03), ₹50 cr (0.01). Find the 95% VaR and the 95% Expected Shortfall.

*Solution.* Order losses ascending and find the 95th percentile of loss. Cumulative probabilities: ≤₹0 → 0.90; ≤₹5 cr → 0.96; ≤₹20 cr → 0.99; ≤₹50 cr → 1.00.
The 95% quantile falls where cumulative first reaches 0.95 → that lies at the ₹5 cr outcome (0.90 < 0.95 ≤ 0.96). So **VaR₉₅ = ₹5 cr.**
ES₉₅ = average loss in the worst 5% tail. The worst 5% by probability = the top 0.05 of outcomes: ₹50 cr (0.01), ₹20 cr (0.03), and 0.01 of the ₹5 cr bucket to fill 0.05.
ES = [0.01×50 + 0.03×20 + 0.01×5] / 0.05 = [0.50 + 0.60 + 0.05] / 0.05 = 1.15 / 0.05 = **₹23 cr.**
*Insight:* ES (₹23 cr) ≫ VaR (₹5 cr) because the tail beyond VaR is fat. VaR alone would badly understate the danger; this is why FRTB moved to 97.5% ES — it is tail-sensitive and coherent (sub-additive).

**B6. The compounding cascade — market shock → liquidity call.**
A fund holds ₹300 cr of bonds financed by ₹270 cr repo (10% haircut, ₹30 cr equity). Rates spike; bond prices fall 4%. The repo lender re-marks collateral and raises the haircut to 20%. Trace the loss across categories.

*Solution.*
*Market loss:* 4% × 300 = **₹12 cr.** Equity falls ₹30 cr → ₹18 cr. Collateral re-marks to 300 × 0.96 = ₹288 cr.
*Liquidity transmission:* new required equity = 20% × 288 = ₹57.6 cr. Fund has ₹18 cr. **Shortfall = 57.6 − 18 = ₹39.6 cr of cash due today.**
*Amplification:* a ₹12 cr price move has become a **₹39.6 cr funding demand — 3.3× larger.** If unmet, the fund defaults on the repo (credit event); forced fire sales push the price down further, hitting every co-holder (systemic channel).
*Insight:* summing standalone category VaRs would have assumed these arrows were off and understated the stressed outcome. The initiating ₹12 cr never appears as the final loss — the transmission does.

**B7. LCR check.**
A bank holds ₹500 cr of HQLA and projects ₹620 cr of gross cash outflows and ₹200 cr of inflows over the 30-day stress window (inflows capped at 75% of outflows). Compute the LCR and state whether it passes.

*Solution.* Net outflows = outflows − min(inflows, 75%×outflows) = 620 − min(200, 465) = 620 − 200 = ₹420 cr.
LCR = HQLA / Net outflows = 500 / 420 = **1.19 = 119%.** Since 119% ≥ 100%, the bank **passes** the LCR.
*Note:* the 75% inflow cap did not bind here (200 < 465). Had projected inflows been ₹500 cr, they'd be capped at ₹465 cr, giving net outflows of ₹155 cr and LCR = 500/155 = 323%.

---

## Section C — Interview-Style (model answers)

**C1. "Walk me through why classification isn't just academic pedantry."**

Four operational reasons. **Measurement:** market risk uses VaR/ES on a price distribution, credit uses PD×LGD×EAD over a year, operational uses frequency×severity — apply the wrong math and you get nonsense. **Ownership:** the CRO must point at a specific desk head, credit committee, or COO and say "this is yours"; unowned risk is unmanaged risk. **Capital:** Basel charges capital by risk type, so mislabel and you hold too little (and blow up) or too much (and destroy ROE). **Hedging:** you hedge market risk with derivatives, credit with CDS or provisions, liquidity with an HQLA buffer — the tool depends on the label. In 2008, mortgage exposure booked as slow-moving "credit risk" was really market, liquidity, model, and systemic risk; because it was mislabelled it was mismeasured, under-capitalised, and owned by nobody.

**C2. "Explain the EL/UL split to a new credit analyst."**

Expected Loss is the *average* loss you'll suffer on a portfolio — PD × LGD × EAD. It's predictable, so you treat it like any other cost: price it into the spread and hold provisions against it. It should never surprise you. Unexpected Loss is the *volatility* around that average — the difference between a normal year and a bad year. That's what threatens solvency, so that's what **capital** exists to absorb. Concretely, on a ₹60 cr loan at 3% PD and 55% LGD, EL is ₹0.99 cr but a single default costs ₹33 cr; the UL of ₹5.6 cr captures that tail. Rule of thumb: **EL is priced, UL is capitalised.** Basel's IRB formula sizes credit capital off UL at 99.9% confidence over one year.

**C3. "Why did Basel move from 99% VaR to 97.5% Expected Shortfall under FRTB?"**

Two reasons. First, **VaR is blind to the tail** beyond the cut-off — it tells you the threshold but not how catastrophic the breach is; two books with identical VaR can have wildly different tail losses. ES averages the losses beyond VaR, so it *sees* tail thickness. Second, **VaR is not a coherent risk measure** — it can violate sub-additivity, meaning a merged portfolio's VaR can exceed the sum of parts, which perversely penalises diversification. ES is coherent (it satisfies sub-additivity), so diversification never increases it. The confidence level dropped from 99% to 97.5% because 97.5% ES sits at roughly the same severity as 99% VaR for a normal distribution, while adding tail sensitivity — you get the tail information without an arbitrary jump in required capital.

**C4. "A bond you own is going to pay par at maturity — how can you have a liquidity problem?"**

Because solvency and liquidity are different questions. The bond being money-good answers the *solvency* question — assets will exceed liabilities eventually. Liquidity asks whether I have **cash when my obligations fall due**. If I funded that bond with short-term deposits or repo and the funding runs — depositors leave, the repo lender raises the haircut or refuses to roll — I need cash *today*, and "par in five years" doesn't help. I'm forced to sell into a market that may be thin (market-liquidity risk), crystallising a real loss on an asset that was never impaired. That's exactly how SVB died in 2023: its held-to-maturity bonds were fine on paper, but a deposit run forced sales and the mark-to-market gap became fatal.

**C5. "Give me a concrete example of risks compounding, and tell me why it matters for measurement."**

A leveraged fund takes a market shock — bond prices drop, say ₹12 cr on a ₹300 cr book. That alone is a clean, small market loss. But the repo lender re-marks the collateral and hikes the haircut, converting a ₹12 cr price move into a ₹40 cr cash call due today — funding-liquidity risk, three times larger. To raise that cash the fund dumps bonds into a thin market, deepening the price fall (market-liquidity feedback) and triggering margin calls on everyone else holding the same bond (systemic). If it can't pay, it defaults on the repo (credit). It matters for measurement because the standard approach — measure each category standalone and sum the VaRs — **assumes those arrows are switched off**. In a crisis they switch on and correlations go to 1, so isolated measurement systematically *understates* stressed loss. That's the case for stress testing and integrated scenario analysis over naive additive VaR.

**C6. "How do you manage a risk you can't put a formula on — model risk or reputational risk?"**

You govern it rather than compute it. For **model risk**, the discipline is independent model validation (a team separate from the developers), back-testing outputs against realised outcomes, benchmarking against alternative models, conservative reserves for model uncertainty, and an inventory with owners and review cycles — the SR 11-7 framework. The failures — the Gaussian copula, the London Whale VaR re-parameterisation — weren't buggy code; they were plausible-looking models with wrong assumptions, so validation must challenge assumptions, not just arithmetic. For **reputational risk**, you can't hold "reputational VaR," but you can monitor its proxies (funding-spread widening, deposit attrition, share-price reaction to conduct events) and, more importantly, manage its *sources*, since it's almost always a second-order effect of an operational, legal, or credit failure going public. The management lever is controlling the first-order failure and having a credible crisis-response and disclosure posture.

---

## Section D — MCQs (with reasoning)

**D1. The 99% 1-day VaR of a book is ₹4 cr. Which statement is correct?**
(a) The maximum possible 1-day loss is ₹4 cr.
(b) On the worst 1% of days the loss will be exactly ₹4 cr.
(c) There is a 1% chance the daily loss exceeds ₹4 cr.
(d) The average loss on the worst 1% of days is ₹4 cr.

**Answer: (c).** VaR is the loss threshold breached with 1% probability. (a) is wrong — VaR is not a maximum; losses beyond it are unbounded. (b) is wrong — ₹4 cr is the threshold, not the exact loss on tail days. (d) describes **Expected Shortfall**, not VaR.

**D2. Which risk did the Basel definition of operational risk explicitly exclude?**
(a) Legal risk (b) Internal fraud (c) System failure (d) Strategic and reputational risk

**Answer: (d).** Basel's operational-risk definition *includes* legal risk (a) and covers internal fraud (b) and system failure (c) among its seven loss-event categories, but **excludes strategic and reputational risk**.

**D3. A loan has PD = 4%, LGD = 50%, EAD = ₹25 cr. Expected Loss is:**
(a) ₹0.50 cr (b) ₹0.25 cr (c) ₹5.00 cr (d) ₹1.00 cr

**Answer: (a).** EL = PD × LGD × EAD = 0.04 × 0.50 × 25 = ₹0.50 cr. (b) omits LGD's correct application; (c) and (d) misplace the decimal / drop a factor.

**D4. Two positions each have standalone VaR of ₹3 cr with correlation ρ = 0. The portfolio VaR is:**
(a) ₹6 cr (b) ₹0 cr (c) ₹4.24 cr (d) ₹3 cr

**Answer: (c).** VaR_p = √(3² + 3² + 2·0·3·3) = √18 = ₹4.243 cr. (a) is the ρ = 1 answer (simple sum); (b) would need ρ = −1 with equal VaRs; (d) ignores the second position entirely.

**D5. Which pair correctly matches risk type to its primary metric?**
(a) Credit risk → Expected Shortfall
(b) Liquidity risk → PD × LGD × EAD
(c) Operational risk → LCR / NSFR
(d) Market risk → VaR / Expected Shortfall

**Answer: (d).** Market risk uses VaR/ES (FRTB). Credit uses EL = PD×LGD×EAD (a and b are swapped); operational uses frequency×severity / SMA, not LCR/NSFR (c); LCR/NSFR are the *liquidity* metrics.

**D6. A firm is solvent (assets > liabilities) but cannot meet a deposit run and collapses. This is primarily:**
(a) Market risk (b) Funding-liquidity risk (c) Credit risk (d) Model risk

**Answer: (b).** Solvency is intact, so it isn't asset value (market) or counterparty default (credit). The failure is inability to raise cash when obligations fall due — **funding-liquidity risk** (Lehman, Northern Rock, SVB).

**D7. Why did FRTB replace 99% VaR with 97.5% Expected Shortfall?**
(a) ES is easier to compute
(b) ES is coherent (sub-additive) and captures tail thickness beyond VaR
(c) VaR is always larger than ES
(d) ES ignores diversification

**Answer: (b).** ES is a coherent measure — it satisfies sub-additivity, so diversification never increases it — and it averages losses beyond the cut-off, capturing tail thickness that VaR ignores. (a) is false (ES is typically harder). (c) is false (ES ≥ VaR at the same confidence). (d) is the opposite of the truth.

**D8. "Total portfolio risk = sum of each category's VaR." This is true only when:**
(a) All pairwise correlations equal 1
(b) All correlations equal 0
(c) The book is fully hedged
(d) Never — it's always false

**Answer: (a).** Simple addition of VaRs holds only under perfect positive correlation (ρ = 1). For ρ < 1 the sum overstates risk (diversification); in a crisis, when arrows switch on and correlations approach 1, even the sum can understate stressed loss. (b) gives the lowest, not additive, risk.

---

*Self-verification note:* All B-section figures were checked two ways where possible — portfolio VaR against the ρ = 1 collapse (B2), UL against a direct two-state variance (B4), and ES against its discrete tail-averaging definition (B5). Formulas used: parametric VaR = z_c·σ·V·√h (z₉₅ = 1.645, z₉₉ = 2.326); EL = PD·LGD·EAD; UL = EAD·LGD·√(PD(1−PD)); VaR_p = √(VaR₁²+VaR₂²+2ρ·VaR₁·VaR₂); LCR = HQLA / net 30-day stressed outflows (inflows capped at 75% of outflows).
