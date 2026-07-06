# Q&A — Modern Portfolio Theory (Markowitz)

Practice bank for Chapter 03. Every question is followed by a full answer. Work numericals yourself first, then check the step-by-step reconciliation.

---

## Section A — Concept Check

**A1. In one sentence, what gap did Markowitz's 1952 framework fill that stock-by-stock analysis could not?**

It treated the portfolio as a *system* of interacting assets and gave a rigorous way to quantify a portfolio's risk from its components' risks *and their co-movement*, so investors could find the least-risky mix for any target return — rather than picking "good" securities one at a time in isolation.

**A2. A portfolio's expected return is a weighted average of its assets' returns, but its risk is not a weighted average of their risks. Why the asymmetry?**

Because expected return is *linear* in the weights, so it averages cleanly. Variance is *quadratic*: squaring the weighted sum produces cross-terms — the covariance terms `2 w_A w_B ρ σ_A σ_B`. Whenever ρ < +1 that cross-term is sub-maximal, so portfolio σ comes out *below* the weighted average of the individual σ's. Return averages; risk under-averages.

**A3. Define covariance and correlation and state the relationship between them.**

Covariance `σ_AB = Σ pᵢ(R_A,ᵢ − E(R_A))(R_B,ᵢ − E(R_B))` measures how two assets move together, but its magnitude depends on the assets' scales, so it is hard to interpret. Correlation standardises it: `ρ_AB = σ_AB / (σ_A σ_B)`, giving a unit-free number bounded in [−1, +1]. The rearrangement `σ_AB = ρ_AB σ_A σ_B` is the form plugged into the variance formula.

**A4. True or false: you need negatively correlated assets to gain a diversification benefit. Explain.**

**False.** A benefit exists for *any* ρ < +1. Negative correlation is merely the strongest case (at ρ = −1 risk can be driven to zero with the right weights). Since virtually all real asset pairs are imperfectly correlated, diversification is almost always available — you do not need the assets to move oppositely, only *not perfectly together*.

**A5. Distinguish systematic from unsystematic risk and state which one diversification removes.**

Unsystematic (firm-specific, diversifiable) risk is idiosyncratic to individual assets and washes out as you add more names. Systematic (market-wide, non-diversifiable) risk is the common risk all assets share. Diversification removes only the unsystematic part; systematic risk remains as a floor — mathematically, the *average covariance* that portfolio variance converges to as n → ∞.

**A6. Why do covariances "dominate" variance in a large portfolio?**

An n-asset portfolio's variance has `n` own-variance terms but `n² − n` covariance terms. For 50 stocks that is 50 variance terms versus 2,450 covariance terms. As n grows, covariances vastly outnumber variances, so what drives total risk is not each stock's standalone volatility but how the stocks co-move.

**A7. What is the efficient frontier, and what does it mean for a portfolio to be "dominated"?**

The efficient frontier is the upper-left boundary of the feasible set of portfolios — those offering maximum return for a given risk (equivalently minimum risk for a given return). A portfolio is *dominated* if another feasible portfolio offers more return for the same risk (or less risk for the same return); dominated portfolios lie below the frontier and no rational investor holds them. The frontier's leftmost tip is the Global Minimum Variance (GMV) portfolio.

**A8. Why does MPT use variance as its risk measure, and what is the main criticism?**

Variance is chosen for mathematical tractability: it yields the clean covariance decomposition that makes the whole theory work. The criticism is that variance is *symmetric* — it penalises upside surprises the same as downside — whereas investors only fear the downside. This motivates alternatives like semi-variance, VaR, and the Sortino ratio. Markowitz himself conceded semi-variance was arguably more logical but chose variance for the cleaner algebra.

---

## Section B — Numerical Problems (full step-by-step)

**B1. Two-asset return and risk.** Stock A: E(R) = 12%, σ = 18%. Stock B: E(R) = 8%, σ = 10%. Correlation ρ = 0.30. Weights 50/50. Find the portfolio's expected return and standard deviation, and quantify the diversification benefit.

*Step 1 — Expected return.*
E(R_p) = 0.50(12%) + 0.50(8%) = 6% + 4% = **10.0%**

*Step 2 — Variance* (work in decimals; σ_A = 0.18, σ_B = 0.10):
- Term 1: w_A²σ_A² = 0.50² × 0.18² = 0.25 × 0.0324 = 0.008100
- Term 2: w_B²σ_B² = 0.50² × 0.10² = 0.25 × 0.0100 = 0.002500
- Term 3: 2 w_A w_B ρ σ_A σ_B = 2 × 0.50 × 0.50 × 0.30 × 0.18 × 0.10
  - 2 × 0.50 × 0.50 = 0.50; × 0.30 = 0.15; × (0.18 × 0.10 = 0.018) = 0.15 × 0.018 = 0.002700

σ_p² = 0.008100 + 0.002500 + 0.002700 = **0.013300**

*Step 3 — Standard deviation.* σ_p = √0.013300 = **11.53%**

*Step 4 — Reconcile.* The no-benefit (ρ = +1) benchmark is the weighted average of σ's: 0.50(18%) + 0.50(10%) = **14.0%**. Our actual σ_p is 11.53%, a **2.47 pp** reduction earned purely by combining, while still returning 10.0%. Self-check: 11.53% < 14.0% ✓ and it lies between B's 10% and A's 18% ✓.

**B2. Covariance and correlation from scenarios.** Three states of the economy:

| State | Prob | R_A | R_B |
|---|---|---|---|
| Boom | 0.30 | 25% | 5% |
| Normal | 0.50 | 10% | 8% |
| Recession | 0.20 | −15% | 12% |

Find E(R_A), E(R_B), σ_A, σ_B, covariance and correlation.

*Step 1 — Expected returns.*
E(R_A) = 0.30(25) + 0.50(10) + 0.20(−15) = 7.5 + 5 − 3 = **9.5%**
E(R_B) = 0.30(5) + 0.50(8) + 0.20(12) = 1.5 + 4 + 2.4 = **7.9%**

*Step 2 — Variances* (in %², using deviations from the mean):
- σ_A²: 0.30(15.5)² + 0.50(0.5)² + 0.20(−24.5)² = 0.30(240.25) + 0.50(0.25) + 0.20(600.25) = 72.075 + 0.125 + 120.05 = 192.25 → σ_A = **13.87%**
- σ_B²: 0.30(−2.9)² + 0.50(0.1)² + 0.20(4.1)² = 0.30(8.41) + 0.50(0.01) + 0.20(16.81) = 2.523 + 0.005 + 3.362 = 5.89 → σ_B = **2.43%**

*Step 3 — Covariance* (product of deviations, probability-weighted):
- Boom: (15.5)(−2.9) = −44.95, × 0.30 = −13.485
- Normal: (0.5)(0.1) = 0.05, × 0.50 = 0.025
- Recession: (−24.5)(4.1) = −100.45, × 0.20 = −20.090

σ_AB = −13.485 + 0.025 − 20.090 = **−33.55 (%²)**

*Step 4 — Correlation.* ρ_AB = −33.55 / (13.87 × 2.43) = −33.55 / 33.66 = **−0.997**

*Reconcile:* the near −1 correlation is intuitive — A falls in recessions while B rises (a defensive/counter-cyclical pattern). Almost perfectly negatively correlated assets are diversification gold: a well-chosen blend could push portfolio risk close to zero.

**B3. Global Minimum Variance portfolio.** Two assets: σ_A = 30%, σ_B = 10%, ρ = 0. Find the GMV weights, and its standard deviation.

*Step 1 — GMV weight in A:*
w_A^min = (σ_B² − ρσ_Aσ_B) / (σ_A² + σ_B² − 2ρσ_Aσ_B)
= (0.10² − 0) / (0.30² + 0.10² − 0) = 0.0100 / (0.0900 + 0.0100) = 0.0100 / 0.1000 = **0.10**

So GMV = **10% in A, 90% in B**.

*Step 2 — GMV standard deviation* (ρ = 0 kills Term 3):
σ_p² = 0.10²(0.30²) + 0.90²(0.10²) = 0.01(0.09) + 0.81(0.01) = 0.000900 + 0.008100 = 0.009000
σ_p = √0.009000 = **9.49%**

*Reconcile:* σ_p = 9.49% is *below* B's own standalone risk of 10% — even though we added 10% of an asset three times riskier (30%). This is the counterintuitive heart of MPT: because A is uncorrelated with B, a small slice of A offsets some of B's variance. Correlation, not standalone risk, governs the effect. ✓

**B4. Zero-risk weight under perfect negative correlation.** σ_A = 20%, σ_B = 12%, ρ = −1. What weight in A drives portfolio risk to zero, and verify it?

*Step 1 — Zero-risk weight:* w_A = σ_B / (σ_A + σ_B) = 12 / (20 + 12) = 12 / 32 = **0.375** → 37.5% A, 62.5% B.

*Step 2 — Verify* using the ρ = −1 special case σ_p = |w_A σ_A − w_B σ_B|:
|0.375 × 20 − 0.625 × 12| = |7.5 − 7.5| = **0%** ✓

*Reconcile:* at ρ = −1 the two assets' movements exactly offset when their weighted volatility contributions are equal (w_A σ_A = w_B σ_B). This is the only correlation value that allows a genuinely riskless combination of two risky assets.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through why diversification is called the only free lunch in finance."**

Normally in finance you pay for reward with risk: more return demands more risk. Diversification is the exception. By combining imperfectly correlated assets, you *reduce* portfolio risk without giving up any expected return — because return is a weighted average (so a blend keeps the average return) while risk under-averages thanks to the covariance term. You aren't forecasting better or taking a directional view; you're exploiting the mathematical fact that less-than-perfectly-correlated risks partly cancel. Reward held constant, risk lowered — that's free.

**C2. "Can adding a riskier asset ever lower a portfolio's total risk? Convince me."**

Yes, and it's a favourite counterintuitive result. Take a bond portfolio with σ = 8% and add equity with σ = 20% but low correlation. In the chapter's example the GMV mix (8% equity, 92% bonds, ρ = 0.20) has σ = 7.84% — *below* the bond's own 8%. The reason: what matters is the new asset's *correlation* with what you already hold, not its standalone volatility. If the correlation is low enough, the offsetting (negative or small positive) cross-term outweighs the extra own-variance the asset brings, and total risk falls.

**C3. "Your firm runs a 60/40 stock-bond fund. In 2022 it had one of its worst years. What went wrong, and what does it teach about MPT?"**

The 60/40 works because bonds historically carried low-to-negative correlation with equities, smoothing the ride. In 2022, inflation spiked, central banks hiked aggressively, and stocks *and* bonds fell together — correlation flipped positive. The diversification benefit is only as good as the correlation input, and correlations are not constant. The lesson is a core limitation of MPT: it assumes stable correlations, but in regime shifts (and crises generally) correlations across risky assets spike toward +1 exactly when you most need the offset — "diversification works until you need it most."

**C4. "What are the assumptions behind Markowitz's model, and where do they break?"**

Assumptions: investors are rational and risk-averse; they decide on mean and variance alone over a single period (which holds if returns are normally distributed *or* utility is quadratic); markets are frictionless (no taxes/costs); and, in the equilibrium extension, investors agree on inputs. They break in practice because: inputs (expected returns, variances, correlations) are *estimated* and noisy — garbage in, garbage out, and optimisers amplify estimation error; correlations are unstable and jump in crises; it's single-period while real investing is multi-period; and variance ignores higher moments — real returns have fat tails and negative skew that mean-variance simply doesn't see.

**C5. "How many stocks do I need to be diversified, and why doesn't more always help?"**

Most of the diversifiable risk is removed by roughly 20–30 well-chosen stocks; beyond that the marginal risk reduction is tiny. The reason is the decomposition σ_p² = (1/n)·(avg own-variance) + (1 − 1/n)·(avg covariance). The first term — unsystematic risk — shrinks fast as n rises, but the second term converges to the *average covariance*, which is the systematic floor. Adding names past ~30 chips at an already-small first term while the floor stays put, so you approach the floor with diminishing returns rather than eliminating risk entirely.

**C6. "Why does the two-asset combination trace a curve rather than a straight line in risk-return space?"**

Because return moves *linearly* with the weight while risk moves *sub-linearly* — σ_p is the square root of a quadratic in the weights. Under ρ = +1 the risk relation collapses to a straight weighted average (a straight line). For any ρ < +1 the curve bows in toward the left of that line; the size of the bow *is* the diversification benefit. The lower the correlation, the more the curve bows left, and the bigger the free lunch.

---

## Section D — Multiple Choice (with reasoning)

**D1. Two assets have σ of 15% and 9%, weighted 50/50. The resulting portfolio σ is 10.5%. The correlation between them is:**
(a) exactly +1  (b) less than +1  (c) exactly −1  (d) cannot be determined

**Answer: (b).** The ρ = +1 benchmark is the weighted average of the σ's: 0.5(15) + 0.5(9) = 12%. The actual portfolio σ of 10.5% is *below* 12%, which can only happen when ρ < +1 — the covariance cross-term is sub-maximal and drags risk below the weighted average. (a) would require σ_p to *equal* 12%; (c) would push σ_p far lower (toward the |w_Aσ_A − w_Bσ_B| = 3% level); (d) is wrong because the sub-benchmark σ pins down ρ < +1.

**D2. Diversification eliminates:**
(a) all portfolio risk  (b) systematic risk  (c) unsystematic (firm-specific) risk  (d) correlation

**Answer: (c).** Diversification removes only firm-specific, diversifiable risk. Systematic (market-wide) risk remains as a floor — the average covariance that variance converges to as assets increase. (a) is wrong because the floor cannot be removed; (b) is exactly backwards; (d) confuses a statistical input with risk itself.

**D3. Two assets have ρ = −1. A specific weighting can make portfolio σ equal to:**
(a) the average of the two σ's  (b) zero  (c) the larger σ  (d) infinity

**Answer: (b).** At ρ = −1 the movements perfectly offset, and the weight w_A = σ_B/(σ_A + σ_B) makes w_A σ_A = w_B σ_B, so σ_p = |w_A σ_A − w_B σ_B| = 0. This is the only correlation value permitting a riskless two-risky-asset combination. (a) describes ρ = +1; (c) and (d) are impossible for a diversified blend.

**D4. In a 50-stock portfolio, the number of distinct covariance terms relative to variance terms is:**
(a) equal  (b) fewer covariances  (c) far more covariances  (d) exactly double

**Answer: (c).** There are n = 50 variance terms and n² − n = 2,450 covariance terms. Covariances vastly outnumber variances, which is the mathematical proof that co-movement, not standalone volatility, dominates a large portfolio's risk.

**D5. The Global Minimum Variance portfolio is best described as:**
(a) the highest-return portfolio on the frontier  (b) the leftmost point of the feasible set  (c) always 100% in the lower-risk asset  (d) the tangency portfolio with the risk-free asset

**Answer: (b).** The GMV portfolio is the least-risky feasible portfolio — the leftmost tip of the frontier. (a) is the opposite corner; (c) is false because an imperfectly correlated riskier asset usually earns a positive GMV weight (recall the 8%-equity GMV that beat 100% bonds); (d) is the max-Sharpe portfolio, a CAPM concept, not the GMV.

**D6. Which is the single biggest practical weakness of applying MPT?**
(a) the return formula is wrong  (b) it needs estimated inputs that are noisy and unstable  (c) it cannot handle more than two assets  (d) it ignores expected return

**Answer: (b).** MPT's algebra is exact; the problem is empirical. Expected returns, variances and especially correlations must be *estimated* from data, they are unstable (correlations spike in crises), and optimisers amplify estimation error — garbage in, garbage out. (a) and (d) are false (return is a simple, correct weighted average and is central to the model); (c) is false — the n-asset matrix form w′Σw generalises freely.

---

*Self-verification note:* All numericals were recomputed in decimals and cross-checked against the ρ = +1 weighted-average benchmark. Key results — B1 σ_p = 11.53% (< 14% benchmark), B3 GMV σ_p = 9.49% (< the 10% low-risk asset), B4 zero-risk weight 37.5% verified to σ_p = 0 — all reconcile with the chapter's principle that risk under-averages whenever ρ < +1.
