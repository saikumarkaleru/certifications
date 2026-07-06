# Q&A — Expected Shortfall

Practice bank for Chapter 05. Every question is followed by a full answer. Work each one before reading the solution. Losses are positive numbers throughout; α is the confidence level and (1 − α) is the tail probability.

---

## Section A — Concept Check

**A1. Define Expected Shortfall in one precise sentence, and give three of its common synonyms.**

Expected Shortfall at confidence level α is the *average of all losses that are at least as bad as VaR at that same level*, i.e. ES_α = E[L | L ≥ VaR_α] — a conditional expectation of the loss given that we are already inside the tail. Synonyms: Conditional VaR (CVaR), Expected Tail Loss (ETL), and Average VaR.

**A2. VaR and ES are computed at the same α. Why is ES always the larger number?**

Because ES averages a set of losses every one of which is ≥ VaR_α (VaR is the boundary of the tail, ES is the mean of everything past that boundary). The average of numbers that are all ≥ VaR must itself be ≥ VaR. It is *not* larger because ES uses a higher confidence level — both use the same α and the same tail. The gap ES − VaR measures how heavy the tail is.

**A3. Explain the sentence: "VaR is a quantile, ES is an integral," and why that distinction matters.**

VaR is a single order statistic — the α-quantile — so it is sensitive only to *where* the tail boundary sits, not to the magnitude of losses beyond it. You can move the worst 0.5% of outcomes from ₹11 crore to ₹110 crore and the 99% quantile does not move, because the count of outcomes below the threshold is unchanged. ES is an average (an integral) over the whole tail, and integrals are sensitive to magnitude everywhere in their range. Pushing the worst outcomes further out immediately raises the tail average. That is why ES captures tail severity and VaR is blind to it.

**A4. Name the four coherence axioms and state which one VaR can fail.**

Monotonicity (a portfolio that always loses more is riskier), translation invariance (adding c of risk-free cash lowers risk by exactly c), positive homogeneity (scaling the book by λ scales risk by λ), and subadditivity (ρ(A + B) ≤ ρ(A) + ρ(B); merging books never creates more risk than holding them apart). VaR satisfies the first three but can **violate subadditivity**. ES satisfies all four and is therefore always coherent.

**A5. Why is subadditivity the "crucial" axiom, in two respects?**

First, it *encodes diversification*: combining imperfectly correlated risks should never increase total risk, and a measure that can violate this tells lies about diversification. Second, it makes *limits and capital additive*: if risk is subadditive, the sum of desk-level numbers is a conservative (larger-or-equal) bound on the firm total, so a regulator can decompose a firm-wide capital number down to desks safely. Break subadditivity and a trader could split one position across two accounts and report *less* total risk than the single position — gaming the limit system.

**A6. Write the two general formulas for ES and read the integral form in words.**

ES_α = E[L | L ≥ VaR_α] and ES_α = (1/(1−α)) ∫_α^1 VaR_u du. The integral says: sweep the confidence level u from α all the way to 1 (the absolute worst case), read VaR at each level, and average them. ES is a "VaR of VaRs" — the average of every quantile deeper than α — which is exactly why it cannot ignore any part of the tail, and why "Average VaR" is a synonym.

**A7. Under normality, why did Basel pick 97.5% ES to replace 99% VaR rather than 99% ES?**

Because under a normal distribution the 97.5% ES multiplier (2.338) is almost identical to the 99% VaR multiplier (2.326). So switching from 99% VaR to 97.5% ES is roughly capital-neutral for a well-behaved (normal) book — it does not mechanically inflate capital across the board — while the ES formulation *automatically* penalises books with fat tails. Regulators bought tail sensitivity without an arbitrary capital jump.

**A8. What is "elicitability" and why does it matter for backtesting ES?**

Elicitability is a statistical property governing whether a risk measure can be validated with a single scoring/loss function. VaR (a quantile) is elicitable — you simply count exceptions (days losses exceeded VaR should be about 1% of days at 99%). ES, being a conditional expectation, is *not* elicitable in the strict sense, so it cannot be scored with one simple loss function. Consequently FRTB backtests VaR (at 97.5% and 99%) for the traffic-light exception test but uses ES for the actual capital charge. ES can still be validated — via joint (VaR, ES) tests or Acerbi–Székely tests — just not as simply.

**A9. Distinguish ES from the credit-risk Expected Loss (EL = PD × LGD × EAD).**

Both are expected losses, but EL is *unconditional* — the average loss over all outcomes — whereas ES is *conditional* — the expected loss *given* that we are in the worst (1−α) tail. EL is what pricing/provisioning covers; ES sits far out in the tail and relates to the unexpected loss that economic capital must absorb.

**A10. Common confusion: "ES is always 1.25× VaR." Correct it.**

The fixed ES/VaR ratio (about 1.25 at 95%, 1.19 at 97.5%, 1.15 at 99%) holds *only under normality*. For fat-tailed distributions the ratio can be much larger — and that divergence is precisely the reason to use ES. Under fat tails VaR may barely move while ES climbs, so no fixed multiple applies.

---

## Section B — Numerical / Applied (full solutions)

**B1. Parametric VaR and ES under normality.** A ₹100 crore book has daily P&L that is normal with mean 0 and daily volatility σ = 2% = ₹2 crore. Compute the 99% one-day VaR and 99% one-day ES, and state the tail gap.

Solution. VaR uses the quantile multiplier z_0.99 = 2.326:
VaR_99% = z_0.99 · σ = 2.326 × ₹2 cr = **₹4.652 cr**.

ES uses the multiplier φ(z_α)/(1−α). The density at 2.326:
φ(2.326) = 0.3989 × e^(−2.326²/2) = 0.3989 × e^(−2.705) = 0.3989 × 0.0668 = 0.02665.
ES multiplier = 0.02665 / 0.01 = 2.665.
ES_99% = σ × 2.665 = ₹2 cr × 2.665 = **₹5.330 cr**.

Tail gap = 5.330 − 4.652 = **₹0.678 cr**. On the worst 1% of days the book loses *at least* ₹4.65 cr (VaR) but *on average* ₹5.33 cr (ES). Check: ES/VaR = 5.330/4.652 = 1.146, matching the tabulated 99% ratio. ✔

**B2. Confirm the Basel "capital-neutral" claim numerically.** For the same book, compute 97.5% ES and compare with 99% VaR.

Solution. z_0.975 = 1.960, φ(1.96) = 0.0584.
ES_97.5% = σ × φ(1.96)/(1−0.975) = ₹2 cr × (0.0584/0.025) = ₹2 cr × 2.338 = **₹4.676 cr**.
Compare with 99% VaR = ₹4.652 cr from B1. Difference = 4.676 − 4.652 = ₹0.024 cr, about 0.5%. So 97.5% ES ≈ 99% VaR for a normal book — the switch is essentially capital-neutral, exactly as FRTB intended. ✔

**B3. Empirical ES from historical scenarios.** Twenty daily losses (₹ lakh, negative = gain), α = 90% (worst 10% = worst 2 obs):
`12, −5, 3, 40, 8, −2, 15, 60, 1, 7, 22, −10, 5, 30, 18, 9, 2, 11, 25, 50`
Find VaR_90% and ES_90%.

Solution. Sort worst to best: 60, 50, 40, 30, 25, 22, 18, 15, 12, 11, 9, 8, 7, 5, 3, 2, 1, −2, −5, −10.
Worst 10% of 20 = 2 observations. VaR_90% = the 2nd-worst loss = **₹50 lakh** (the cut-off).
ES_90% = average of the worst 2 losses = (60 + 50)/2 = **₹55 lakh**.
Check: ES (55) > VaR (50) ✔ — ES sits deeper in the tail.

**B4. Tail-blindness in one line.** In B3, suppose the single worst day had been 200 instead of 60. Recompute VaR and ES.

Solution. The two worst losses become 200 and 50. VaR_90% is still the 2nd-worst = **₹50 lakh** (unchanged — the quantile does not see the magnitude of the very worst day). ES_90% = (200 + 50)/2 = **₹125 lakh** (up from 55). Same VaR, radically different ES: this is exactly the failure ES fixes. VaR reads the boundary; ES reads the severity. ✔

**B5. The coherence proof — VaR fails subadditivity, ES does not.** Two identical, *independent* corporate bonds A and B. Each: face ₹100, default probability 4%, loss ₹100 if it defaults and ₹0 if it survives. α = 95% (tail = worst 5%). Compute individual and portfolio VaR and ES.

Solution.

*Individual VaR.* For one bond P(loss = 0) = 96% > 95%, so the 95th percentile is 0. VaR_95%(A) = VaR_95%(B) = **0**. Sum = 0.

*Portfolio distribution* (independence):

| Outcome | Probability | Loss (₹) |
|---|---|---|
| Both survive | 0.96 × 0.96 = 0.9216 | 0 |
| Exactly one defaults | 2 × 0.04 × 0.96 = 0.0768 | 100 |
| Both default | 0.04 × 0.04 = 0.0016 | 200 |

Cumulative from the bottom: P(loss ≤ 0) = 0.9216 < 0.95, so the 95th percentile jumps to the next outcome: VaR_95%(A+B) = **₹100**.

*VaR subadditivity check:* VaR(A+B) = 100 > 0 = VaR(A) + VaR(B). **VaR violated subadditivity** — diversifying two independent bonds raised the reported risk from 0 to 100. ✘

*Individual ES.* Fill the worst 5% (0.05) mass from the worst outcome down: the 4% default mass (loss 100) plus 1% of the survive mass (loss 0):
ES_95%(A) = (1/0.05)[0.04 × 100 + 0.01 × 0] = 4/0.05 = **₹80**. Sum = 160.

*Portfolio ES.* Fill 0.05 of mass from the worst down:
- Both default: 0.0016 at loss 200.
- Remaining 0.05 − 0.0016 = 0.0484 from the "one defaults" bucket at loss 100.
ES_95%(A+B) = (1/0.05)[0.0016 × 200 + 0.0484 × 100] = (0.32 + 4.84)/0.05 = 5.16/0.05 = **₹103.2**.

*ES subadditivity check:* ES(A+B) = 103.2 ≤ 160 = ES(A) + ES(B). **ES is subadditive** — diversification cut risk from 160 to 103.2 (a 35% reduction), as intuition demands. ✔

Side by side:

| Measure | A | B | Sum of parts | Portfolio A+B | Subadditive? |
|---|---|---|---|---|---|
| VaR 95% | 0 | 0 | 0 | 100 | No — violated |
| ES 95% | 80 | 80 | 160 | 103.2 | Yes — holds |

**B6. ES falls as the confidence level falls (direction check).** For a normal book with σ = ₹5 crore (μ = 0), compute ES at 95%, 97.5% and 99% and confirm the ordering.

Solution. Using ES multipliers φ(z_α)/(1−α): 95% → 2.063, 97.5% → 2.338, 99% → 2.665.
- ES_95% = 5 × 2.063 = **₹10.32 cr**
- ES_97.5% = 5 × 2.338 = **₹11.69 cr**
- ES_99% = 5 × 2.665 = **₹13.32 cr**

So ES_95% < ES_97.5% < ES_99% in rupee terms. A *lower* confidence level means a *wider* tail that pulls in less-extreme losses, giving a *lower* absolute ES. Careful: "bigger tail probability" does not mean "bigger ES." ✔

**B7. ES from a discrete P&L distribution.** A position has the following loss distribution: ₹0 with prob 0.90, ₹50 with prob 0.06, ₹120 with prob 0.03, ₹300 with prob 0.01. Compute VaR_95% and ES_95%.

Solution. Cumulative probability from best to worst: P(loss ≤ 0) = 0.90; P(loss ≤ 50) = 0.96. The smallest loss ℓ with P(L ≤ ℓ) ≥ 0.95 is **₹50**, so VaR_95% = ₹50.
ES_95% = average loss over the worst 5% mass, filled from the worst outcome down:
- ₹300 at 0.01
- ₹120 at 0.03
- remaining 0.05 − 0.04 = 0.01 of the ₹50 bucket
ES_95% = (1/0.05)[0.01×300 + 0.03×120 + 0.01×50] = (3 + 3.6 + 0.5)/0.05 = 7.1/0.05 = **₹142**.
Check: ES (142) > VaR (50) ✔, and ES reflects the ₹300 catastrophe that VaR ignores.

**B8. Scaling to a longer horizon.** A book's 1-day 97.5% ES is ₹8 crore, returns i.i.d. and roughly normal. Estimate the 10-day 97.5% ES using the square-root-of-time rule.

Solution. Under i.i.d. normal returns with zero mean, both VaR and ES scale with the square root of the horizon (they are fixed multiples of σ, and σ scales as √T).
ES_10-day = ES_1-day × √10 = ₹8 cr × 3.162 = **₹25.30 cr**.
Caveat: this assumes i.i.d. zero-drift normal returns; FRTB instead uses liquidity-adjusted horizons (10–120 days) by risk class rather than a blanket √T scale.

---

## Section C — Interview-Style (model answers)

**C1. "In one minute, why did the industry move from VaR to Expected Shortfall?"**

Model answer: "VaR has two fatal weaknesses. First, it is tail-blind — it reports only the boundary loss at a confidence level and says nothing about how bad losses are beyond it, so two books with identical VaR can have wildly different true tail risk, and traders can game a VaR budget by selling deep out-of-the-money risk that sits just past the cut-off. Second, VaR is not coherent: it can violate subadditivity, meaning a diversified portfolio can show *higher* VaR than the sum of its parts, which is nonsensical and breaks capital aggregation. Expected Shortfall fixes both: it averages the entire tail beyond VaR, so it captures tail severity, and it satisfies all four coherence axioms including subadditivity. That is why Basel's FRTB replaced 99% VaR with 97.5% ES for market-risk capital."

**C2. "Give me the single cleanest example that shows VaR is not coherent but ES is."**

Model answer: "Two independent bonds, each ₹100 face, 4% default probability, ₹100 loss on default, at 95% confidence. Each bond alone has a 96% chance of zero loss, so its 95% VaR is 0 — sum of parts is 0. But the combined portfolio has only a 92.16% chance of zero loss, so its 95th percentile jumps to ₹100 — the portfolio VaR (100) exceeds the sum of individual VaRs (0). VaR says diversification *created* risk. ES tells the opposite, correct story: each bond's 95% ES is ₹80, summing to 160, while the portfolio ES is ₹103.2 — diversification cut risk by 35%. Same data, and only ES behaves sensibly."

**C3. "Why 97.5% for ES? Isn't a higher confidence level more conservative?"**

Model answer: "It was chosen for continuity, not conservatism. Under normality the 97.5% ES multiplier is 2.338, almost exactly the 99% VaR multiplier of 2.326, so switching from 99% VaR to 97.5% ES keeps capital roughly unchanged for a normal, well-behaved book. That avoids an arbitrary mechanical jump in capital. The benefit is that when a book has fat tails, ES automatically produces a higher number than the equivalent VaR would — you get tail sensitivity for free without recalibrating the whole framework. Higher confidence isn't the point; tail *shape* sensitivity is."

**C4. "If ES is better, why does FRTB still compute VaR at all?"**

Model answer: "Backtesting. VaR is elicitable — you can validate it by counting exceptions against a simple expected exception rate, which regulators formalise as the traffic-light test. ES is a conditional expectation and is not elicitable, so it can't be scored with one simple loss function. FRTB's pragmatic split is to backtest VaR at 97.5% and 99% for the exception test while using ES for the actual capital charge. VaR survives as a validation tool even though ES does the capital work."

**C5. "A trader tells you two strategies have the same VaR, so they're equally risky. How do you respond?"**

Model answer: "Equal VaR only means the tail *boundary* is the same; it says nothing about what's behind it. I'd compute ES for both. If one strategy sells catastrophe or deep out-of-the-money risk, its losses beyond the VaR line are far larger, so its ES will be much higher even though VaR matches. I'd also check the ES/VaR ratio: near the normal value (about 1.15 at 99%) suggests a well-behaved tail; a ratio well above that flags a fat tail the VaR number is hiding. VaR equality is a red flag to look deeper, not a proof of equal risk."

**C6. "What are the practical downsides of ES you'd flag to a risk committee?"**

Model answer: "Three. First, estimation: ES averages the worst (1−α)·N observations, so it needs more tail data than VaR to be stable — at 97.5% with 1,000 scenarios you're averaging just 25 points, and the estimate is noisy if the tail is sparse. Second, backtesting: ES isn't elicitable, so validation needs joint (VaR, ES) or Acerbi–Székely tests rather than a simple exception count — harder to explain to supervisors. Third, model risk in the extreme tail: for very high confidence you may need Extreme Value Theory (a Generalised Pareto fit) rather than raw empirical averaging. None of these outweigh coherence and tail sensitivity, but they're real operational costs."

**C7. "Explain the link between ES and convex optimisation, and why a portfolio manager might care."**

Model answer: "ES is convex and coherent, so minimising ES is a well-posed convex optimisation — Rockafellar and Uryasev showed CVaR minimisation reduces to a linear program that's fast and has a unique global optimum. Minimising VaR, by contrast, is non-convex and can have many local minima, so an optimiser can get stuck or return unstable weights. For a manager building a tail-risk-controlled portfolio, ES gives a tractable, reliable objective; VaR does not."

---

## Section D — Multiple Choice (with reasoning)

**D1. At the same confidence level α, which is always true?**
A) VaR ≥ ES  B) ES ≥ VaR  C) ES = VaR  D) No fixed relationship

Answer: **B**. ES averages losses all of which are ≥ VaR (the tail boundary), so its average is ≥ VaR. A and C are wrong; D ignores this guaranteed ordering. Equality only occurs in the degenerate case where all tail losses equal VaR exactly.

**D2. Which coherence axiom can VaR violate?**
A) Monotonicity  B) Translation invariance  C) Positive homogeneity  D) Subadditivity

Answer: **D**. VaR satisfies the first three but can fail subadditivity (e.g. the two-independent-bonds example), which is its fatal theoretical flaw. ES satisfies all four.

**D3. Under normality with μ = 0, the ES multiplier at confidence α is:**
A) z_α  B) φ(z_α)/(1−α)  C) (1−α)/φ(z_α)  D) z_α/(1−α)

Answer: **B**. ES_α = μ + σ·φ(z_α)/(1−α); the factor φ(z_α)/(1−α) is the ES analogue of z_α. A is the VaR multiplier. C and D are not valid forms.

**D4. FRTB replaced 99% VaR with:**
A) 99% ES  B) 97.5% ES  C) 95% ES  D) 99.9% VaR

Answer: **B**. FRTB uses 97.5% ES because under normality its multiplier (2.338) is nearly identical to the 99% VaR multiplier (2.326), making the switch roughly capital-neutral while adding tail sensitivity.

**D5. Why does FRTB still backtest with VaR rather than ES?**
A) ES is always inaccurate  B) VaR is more conservative  C) ES is not elicitable  D) Regulators prefer older methods

Answer: **C**. ES, a conditional expectation, lacks elicitability, so it can't be validated with a single scoring function. VaR (a quantile) is elicitable and is retained for the exception test. A and B are false; D is not the reason.

**D6. Two portfolios have identical 99% VaR but portfolio X loses far more in the extreme tail. Which measure distinguishes them?**
A) VaR  B) ES  C) Neither  D) Both equally

Answer: **B**. VaR sees only the tail boundary, which is identical, so it cannot distinguish them. ES averages the whole tail and will be higher for portfolio X. This is the core tail-blindness point.

**D7. Lowering the confidence level from 99% to 95% (all else equal) does what to the absolute ES in rupees?**
A) Increases it  B) Decreases it  C) Leaves it unchanged  D) Cannot tell

Answer: **B**. A lower α means a wider tail that pulls in less-extreme losses, lowering the tail average. So ES_95% < ES_99% in rupee terms even though 95% is a "bigger tail probability." Direction is a classic trap.

**D8. For the empirical method with N = 1,000 scenarios at α = 97.5%, ES equals:**
A) The 25th-worst loss  B) The average of the worst 25 losses  C) The single worst loss  D) The average of all 1,000 losses

Answer: **B**. The worst 2.5% of 1,000 is 25 observations; VaR is roughly the 25th-worst loss (the cut-off) and ES is the *average* of those worst 25. A describes VaR, not ES.

**D9. The statement "ES is always exactly 1.25× VaR" is:**
A) Always true  B) True only under normality at 95%  C) True for all fat-tailed books  D) Never true

Answer: **B**. The 1.25 ratio is the normal-distribution value specifically at 95% (it is 1.19 at 97.5%, 1.15 at 99%). For fat tails the ratio can be much larger, which is the whole reason to use ES. So the fixed factor holds only under normality, and 1.25 specifically at α = 95%.

**D10. In the two-independent-4%-bond example at 95%, the portfolio VaR and the sum of individual VaRs are:**
A) 0 and 0  B) 100 and 0  C) 100 and 200  D) 200 and 0

Answer: **B**. Each bond's 95% VaR is 0 (96% chance of no loss), so the sum of parts is 0; the portfolio's 95th percentile jumps to 100 because P(loss ≤ 0) = 0.9216 < 0.95. VaR(A+B) = 100 > 0, violating subadditivity.

**D11. ES relates to the credit-risk Expected Loss (PD × LGD × EAD) how?**
A) They are identical  B) ES is unconditional, EL is conditional  C) ES is conditional (on the tail), EL is unconditional  D) They are unrelated

Answer: **C**. EL is the unconditional average loss over all outcomes; ES is the expected loss *conditional* on being in the worst (1−α) tail. ES sits far out in the tail and maps to unexpected loss / economic capital.

**D12. Which is the strongest single theoretical argument for ES over VaR?**
A) ES is easier to compute  B) ES is easier to backtest  C) ES is always coherent (satisfies subadditivity)  D) ES uses a higher confidence level

Answer: **C**. Coherence — specifically guaranteed subadditivity — is the deepest argument: it makes ES safe for diversification, aggregation and optimisation. A and B are actually false (ES is harder to backtest and needs more tail data); D is not generally true.

---

*Self-check note: All parametric figures use z_0.95 = 1.645, z_0.975 = 1.960, z_0.99 = 2.326, and ES multipliers 2.063 / 2.338 / 2.665 respectively; the two-bond coherence numbers (VaR 0/0/100, ES 80/80/103.2) and the empirical B3/B4 results reconcile exactly with the chapter's worked examples.*
