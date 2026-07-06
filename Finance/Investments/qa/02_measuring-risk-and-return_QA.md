# Q&A — Measuring Risk and Return

A practice bank for Chapter 02. Work each item before reading the answer. Formulas match the chapter; every numerical answer is reconciled by an independent route where possible.

---

## Section A — Concept Checks

**A1. Why do we square the deviations when computing variance instead of just averaging them?**
Two reasons. First, raw deviations from the mean sum to exactly zero (positives and negatives cancel), so their average is uninformative. Squaring removes the sign so all dispersion counts positively. Second, squared terms are additive and differentiable, which lets us minimise portfolio variance with calculus later. We then take the square root (σ) to return to return-units (%).

**A2. State when you would report the arithmetic mean and when the geometric mean.**
Use the arithmetic mean to forecast a *single next period's* expected return — it is the unbiased estimate of one draw from the distribution. Use the geometric mean to describe *realised multi-period growth*, because it is the constant compounded rate that turns starting capital into ending capital. GM ≤ AM always.

**A3. What is "volatility drag" and roughly how large is it?**
The gap between the arithmetic and geometric mean, approximately σ²/2. Because losses require larger percentage gains to recover, higher volatility compounds to a lower terminal value; the arithmetic average flatters performance. A fund averaging 14% arithmetically with σ = 19% loses roughly 1.8 percentage points to drag.

**A4. Why is portfolio variance *not* the weighted average of the component variances?**
Because returns co-move. The correct formula carries a covariance cross-term: σ_p² = w_A²σ_A² + w_B²σ_B² + 2w_Aw_Bρ_ABσ_Aσ_B. When ρ < 1 the cross-term is smaller than a naive weighting implies, so portfolio σ falls below the weighted-average σ. That shortfall *is* diversification — ignoring the cross-term erases the entire reason to diversify.

**A5. A covariance of +500 %² — is that a strong relationship?**
Unknowable from covariance alone. Covariance magnitude scales with the two assets' own volatilities, so it has no fixed benchmark. Only correlation, ρ = σ_AB/(σ_Aσ_B), which is bounded in [−1, +1], tells you the *strength* of the linear relationship.

**A6. Why divide sample variance by (n − 1) rather than n?**
Bessel's correction. The sample mean is itself estimated from the same data, consuming one degree of freedom; dividing by n would systematically underestimate the true variance. With given probabilities or a full population, divide by n (weight by pₛ) instead.

**A7. Give two distinct criticisms of standard deviation as a risk measure.**
(1) It is symmetric — it penalises a +40% surprise identically to a −40% loss, yet investors do not fear gains; this motivates downside measures (semi-variance, Sortino). (2) It fully describes risk only if returns are normal, but real equity returns are negatively skewed with fat tails, so σ underprices extreme-loss probability.

**A8. Returns compound but volatility scales by √time — why the difference?**
A multi-period return is the product of period gross returns, so it compounds: (1+r)^m − 1. Variance, however, *adds* across independent (serially uncorrelated) periods, so total variance = m × period variance, and standard deviation = √m × period σ. Applying √m to returns or m to volatility is a classic error.

---

## Section B — Numerical Problems (full working, reconciled)

**B1. Holding-period return with income.**
Buy at ₹250; one year later price is ₹280 and a ₹6 dividend was paid. Find HPR, splitting income and capital-gain yield.
HPR = [(280 − 250) + 6] / 250 = 36 / 250 = **14.4%**.
Split: capital-gain yield = 30/250 = 12.0%; income yield = 6/250 = 2.4%. Sum = 12.0% + 2.4% = **14.4%** ✓ (reconciles with the total).

**B2. Arithmetic vs geometric mean and the drag.**
Annual returns: +40%, −20%, +15%.
Arithmetic mean = (40 − 20 + 15)/3 = 35/3 = **11.67%**.
Geometric mean = [(1.40)(0.80)(1.15)]^(1/3) − 1 = [1.288]^(1/3) − 1.
1.288^(1/3): since 1.088³ = 1.088 × 1.088 × 1.088 = 1.1837 × 1.088 = 1.288, the cube root is **1.088**, so GM = **8.80%**.
Reconciliation: growing ₹1 at a constant 8.80% for three years gives 1.088³ = 1.288, the same terminal factor as the actual path ✓. GM (8.80%) < AM (11.67%) as required; the ~2.9 ppt gap reflects the −20% year's large drag.

**B3. Real (inflation-adjusted) return via Fisher.**
Nominal return 13.0%, inflation 6.0%. Exact real return = (1.13/1.06) − 1 = 1.06604 − 1 = **6.60%**.
The crude shortcut 13 − 6 = 7.0% overstates the real return by 0.40 ppt — material at Indian inflation levels, so prefer the exact ratio.

**B4. Expected return, variance, standard deviation from scenarios.**
Scenarios for Stock M:

| State | pₛ | Rₛ |
|---|---|---|
| Boom | 0.25 | +24% |
| Normal | 0.50 | +8% |
| Bust | 0.25 | −16% |

E(R) = 0.25(24) + 0.50(8) + 0.25(−16) = 6 + 4 − 4 = **8%**.
Variance = Σ pₛ[Rₛ − E(R)]²:
- Boom: (24 − 8)² = 256; ×0.25 = 64
- Normal: (8 − 8)² = 0; ×0.50 = 0
- Bust: (−16 − 8)² = 576; ×0.25 = 144
σ² = 64 + 0 + 144 = **208 %²**; σ = √208 = **14.42%**.
Reconciliation: E(R) sits symmetrically (Boom and Bust are ±16 from Normal with equal probability), consistent with the 8% centre; the two equal tail contributions (64 and 144 differ only because deviations differ) sum cleanly. Interpretation: 8% expected return, ±14.4% one-σ spread.

**B5. Annualising a sub-period return and a daily volatility.**
(a) A 6-month HPR of 8%. Annualised = (1.08)² − 1 = 1.1664 − 1 = **16.64%** (not 16% — the second half compounds on the first).
(b) Daily σ = 1%, 252 trading days. Annual σ = 1% × √252 = 1% × 15.875 = **15.87%** ≈ 15.9%.

**B6. Covariance, correlation, and the two-asset portfolio (the payoff).**
Stocks A and B over the scenarios below:

| State | pₛ | R_A | R_B |
|---|---|---|---|
| Boom | 0.30 | +25% | −10% |
| Normal | 0.40 | +10% | +8% |
| Recession | 0.30 | −15% | +20% |

Step 1 — expected returns.
E(R_A) = 0.30(25) + 0.40(10) + 0.30(−15) = 7.5 + 4 − 4.5 = **7.0%**.
E(R_B) = 0.30(−10) + 0.40(8) + 0.30(20) = −3 + 3.2 + 6 = **6.2%**.

Step 2 — variances.
σ_A²: (25−7)²=324→×0.30=97.2; (10−7)²=9→×0.40=3.6; (−15−7)²=484→×0.30=145.2. Sum = **246 %²**; σ_A = √246 = **15.68%**.
σ_B²: (−10−6.2)²=262.44→×0.30=78.732; (8−6.2)²=3.24→×0.40=1.296; (20−6.2)²=190.44→×0.30=57.132. Sum = **137.16 %²**; σ_B = √137.16 = **11.71%**.

Step 3 — covariance = Σ pₛ(R_A−7)(R_B−6.2):
- Boom: (18)(−16.2) = −291.6; ×0.30 = −87.48
- Normal: (3)(1.8) = 5.4; ×0.40 = 2.16
- Recession: (−22)(13.8) = −303.6; ×0.30 = −91.08
σ_AB = −87.48 + 2.16 − 91.08 = **−176.4 %²**.

Step 4 — correlation.
ρ_AB = −176.4 / (15.68 × 11.71) = −176.4 / 183.61 = **−0.961**. Strongly negative — B hedges A.

Step 5 — 50/50 portfolio.
E(R_p) = 0.5(7.0) + 0.5(6.2) = **6.6%**.
σ_p² = (0.5)²(246) + (0.5)²(137.16) + 2(0.5)(0.5)(−176.4)
= 0.25(246) + 0.25(137.16) + 0.5(−176.4)
= 61.5 + 34.29 − 88.2 = **7.59 %²**; σ_p = √7.59 = **2.76%**.

Reconciliation via direct portfolio returns (50/50 each state):
- Boom: 0.5(25) + 0.5(−10) = 7.5%
- Normal: 0.5(10) + 0.5(8) = 9.0%
- Recession: 0.5(−15) + 0.5(20) = 2.5%
E(R_p) = 0.30(7.5) + 0.40(9.0) + 0.30(2.5) = 2.25 + 3.6 + 0.75 = **6.6%** ✓.
σ_p²: devs from 6.6 → +0.9, +2.4, −4.1; weighted squares = 0.30(0.81) + 0.40(5.76) + 0.30(16.81) = 0.243 + 2.304 + 5.043 = **7.59 %²** ✓.
Both routes agree. The weighted-average σ would have been 0.5(15.68) + 0.5(11.71) = 13.70%, yet the portfolio σ is only 2.76% — the negative covariance term (−88.2) collapsed risk by nearly 11 ppt while return barely moved (6.6% vs A's 7.0%). That is diversification in one number.

**B7. Interview-style portfolio-σ drill across correlations.**
Two assets, σ_A = σ_B = 20%, equal weights. Compute σ_p at ρ = +1, 0, −1.
σ_p² = 0.25(400) + 0.25(400) + 2(0.5)(0.5)ρ(20)(20) = 100 + 100 + 200ρ = 200 + 200ρ.
- ρ = +1: σ_p² = 400 → σ_p = **20%** (no benefit; risks add linearly).
- ρ = 0: σ_p² = 200 → σ_p = √200 = **14.14%**.
- ρ = −1: σ_p² = 0 → σ_p = **0%** (risk fully hedged).
Reconciliation at ρ = +1: σ_p should equal the weighted-average σ = 0.5(20)+0.5(20) = 20% ✓; at ρ = −1 with equal σ and equal weights, offsetting is complete, giving 0% ✓.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Why use the geometric, not the arithmetic, mean to report a fund's past performance?"**
Model answer: Because investors experience compounding, and only the geometric mean reproduces the actual growth of capital. The arithmetic mean averages independent single-period returns and systematically overstates realised growth whenever returns vary — the gap is the volatility drag, roughly σ²/2. Example: returns of +50% then −50% average to 0% arithmetically, but ₹100 becomes ₹150 then ₹75 — a −25% cumulative, i.e. a geometric mean of about −13.4% per year. Quoting the arithmetic 0% would be a lie about what the money did. So: arithmetic for forecasting the next period, geometric for describing history.

**C2. "Why do you care more about covariance than about an asset's own volatility?"**
Model answer: Because portfolio variance is driven by the covariance cross-term, not by individual variances alone. A highly volatile asset that is uncorrelated — or negatively correlated — with the rest of the book can *lower* total portfolio risk. Conversely, adding a low-volatility asset that moves in lockstep with everything else adds little diversification. The logical consequence is that risk which cancels within a portfolio should not be compensated by the market — only non-diversifiable, systematic covariance risk is priced. That is the seed of CAPM, where beta is exactly a rescaled covariance with the market.

**C3. "Standard deviation — what's wrong with it as a risk measure?"**
Model answer: Two structural problems. First, it is symmetric: it treats a large gain as just as "risky" as an equal loss, which does not match how investors define risk. Downside measures like semi-variance and the Sortino ratio address this by penalising only below-target returns. Second, σ fully characterises risk only under normality, but real returns are negatively skewed and fat-tailed (leptokurtic) — crashes like 1987, 2008 and March 2020 occur far more often than a bell curve predicts. So mean-variance analysis and Gaussian VaR systematically underprice tail risk. σ remains useful as a tractable, additive first approximation, but a good analyst names its limits.

**C4. "Returns aren't normally distributed. Practically, so what?"**
Model answer: It matters most in the tails, which is where portfolios blow up. Fat tails mean extreme losses are more likely than a normal distribution implies, and negative skew means the big surprises tend to be on the downside. Any tool that reads risk off a Gaussian — mean-variance optimisation, a 95%/99% VaR of μ − 1.645σ or μ − 2.33σ — will understate the probability and size of large drawdowns. The fixes are to stress-test beyond the model (scenario analysis, expected shortfall, historical simulation) and to treat optimiser outputs with scepticism because they assume a distribution reality does not honour.

**C5. "Explain expected versus historical return to a client."**
Model answer: Expected return is a forward-looking, probability-weighted forecast — the centre of the distribution of what *could* happen next. A historical average is a single realised sample drawn from that unknown distribution; it is an *estimate* of the expected return, not the truth. Because it is one sample, it carries estimation error and is unstable, especially over short windows — which is why feeding raw historical means into an optimiser produces fragile, extreme allocations. We use history to inform the forecast, not to equal it.

**C6. "Annualise a 1% daily volatility, and explain the rule."**
Model answer: Roughly 1% × √252 ≈ 15.9%, using ~252 trading days. Volatility scales with the square root of time because variances add across independent periods while returns compound. If daily returns are serially uncorrelated, annual variance = 252 × daily variance, so annual σ = √252 × daily σ. The common mistake is multiplying the daily figure by 252 (that annualises variance, not volatility) or applying the √-rule to returns, which should compound instead.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1.** A stock returns +30% then −30% in two years. Its geometric mean annual return is closest to:
A) 0%  B) −4.6%  C) −9%  D) +4.6%
**Answer: B.** (1.30)(0.70) = 0.91, terminal factor for two years. GM = 0.91^(1/2) − 1 = 0.9539 − 1 = −4.61%. The arithmetic mean is 0%, but compounding a symmetric up/down pair always loses money — the drag. A (0%) is the arithmetic-mean trap.

**D2.** Which pair of correlations gives, respectively, the *most* and *least* portfolio-risk reduction?
A) ρ = 0 most, ρ = +1 least  B) ρ = −1 most, ρ = +1 least  C) ρ = +1 most, ρ = −1 least  D) ρ = −1 most, ρ = 0 least
**Answer: B.** Diversification benefit rises as ρ falls. ρ = −1 permits the largest reduction (risk can reach zero with suitable weights); ρ = +1 gives none (portfolio σ equals the weighted-average σ). C reverses the logic; D wrongly ranks ρ = 0 as worst.

**D3.** Sample variance uses an (n − 1) divisor because:
A) it makes σ smaller  B) it corrects downward bias from using an estimated sample mean  C) the population is always unknown  D) it matches the probability-weighted formula
**Answer: B.** Bessel's correction offsets the degree of freedom consumed by estimating the mean from the same data; dividing by n would bias variance downward. A is a side effect, not the reason; D is false — the probability-weighted (population) form divides by n, not n − 1.

**D4.** Monthly volatility is 5%. The annualised volatility is closest to:
A) 60%  B) 17.3%  C) 5%  D) 8.7%
**Answer: B.** σ_annual = 5% × √12 = 5% × 3.464 = 17.32%. A (×12) wrongly annualises variance rather than volatility; it is the classic error.

**D5.** Two assets each have σ = 25%, held 60/40, with ρ = 0.20. Portfolio σ is closest to:
A) 25.0%  B) 19.6%  C) 15.8%  D) 22.4%
**Answer: B.** σ_p² = 0.6²(625) + 0.4²(625) + 2(0.6)(0.4)(0.20)(25)(25) = 0.36(625) + 0.16(625) + 0.48(0.20)(625) = 225 + 100 + 60 = 385. σ_p = √385 = 19.62%. Cross-term check: 2(0.6)(0.4) = 0.48; ×0.20 = 0.096; ×625 = 60 ✓. So σ_p ≈ **19.6%**. Option A (25%) is the "no-diversification" distractor — the weighted-average σ, which holds only at ρ = 1.

**D6.** Expected return differs from a historical average because expected return is:
A) always larger  B) a realised outcome  C) a forward-looking probability-weighted forecast  D) computed with (n − 1)
**Answer: C.** Expected return is ex-ante, E(R) = Σ pₛRₛ; a historical average is one ex-post sample estimate of it. Neither is systematically larger (A false), it is not a realised outcome (B false), and the divisor point (D) is irrelevant to the ex-ante/ex-post distinction.

---

*One-line close:* return is the mean of the distribution, risk is its spread, and portfolio risk is governed less by how volatile assets are than by how they move together.
