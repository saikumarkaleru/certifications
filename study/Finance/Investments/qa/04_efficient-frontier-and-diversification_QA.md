# Q&A — The Efficient Frontier and Diversification

*Investments | Portfolio Theory | Companion to Chapter 04 | All returns and standard deviations in % p.a. unless stated | Variances quoted in %² (i.e. "400" means (20%)²)*

---

## SECTION A — Concept Check (Short Answer)

**A1. Why can't an investor simply buy the single highest-expected-return security?**
Because return arrives bundled with risk, and risk is not rewarded linearly. Part of a single stock's risk — its firm-specific (unsystematic) component — is uncompensated: the market pays nothing for risk you could have diversified away for free. Holding one name forces you to bear that unpaid risk. The rational move is to diversify the idiosyncratic risk to near zero, then hold the combination with the best return-per-unit-of-risk (highest Sharpe ratio).

**A2. Define the efficient frontier and distinguish it from the minimum-variance frontier.**
The minimum-variance frontier is the *entire* left boundary of the feasible set of portfolios — the bullet shape giving the lowest risk for every level of return. The efficient frontier is only its *upper* branch, from the Global Minimum Variance Portfolio (GMVP) upward. The lower branch (below the GMVP) is dominated: for any portfolio there, another portfolio directly above it offers the same risk with higher return, so no rational investor holds it.

**A3. Why is the efficient frontier concave (bowed up and to the left) rather than a straight line?**
Concavity is the geometric signature of diversification. Because assets are imperfectly correlated (ρ < 1), the risk of a combination is *less* than the weighted average of the component risks. The cross-term in the variance formula carries ρ, and any ρ < 1 pulls portfolio variance below the linear (ρ = +1) benchmark, bending the curve leftward. Only if every pair had ρ = +1 would the frontier collapse to a straight line.

**A4. Total risk splits into two parts. Name them and state which one is priced.**
Total risk = systematic (market-wide, undiversifiable) risk + unsystematic (firm-specific, diversifiable) risk. Formally σ²ᵢ = βᵢ²σ²_M + σ²(εᵢ). Only systematic risk is priced — it cannot be diversified away, so the market pays a premium for bearing it. Unsystematic risk earns nothing because a diversified investor has already eliminated it.

**A5. As you add equally weighted stocks, what does portfolio variance converge to, and why?**
It converges to the *average covariance* between pairs. With wᵢ = 1/n, σ²_p = (1/n)·(avg variance) + (1 − 1/n)·(avg covariance). The own-variance term is scaled by 1/n and vanishes as n → ∞ (this is the unsystematic risk washing out), while the average-covariance term survives as the systematic floor. Firm-specific noise averages out; economy-wide shocks hit everything and remain.

**A6. Why does combining a risk-free asset with a risky portfolio produce a straight line?**
The risk-free asset has zero variance and zero covariance with the risky portfolio P. So when you put weight y in P, the complete portfolio's return is linear in y — E(R_c) = R_f + y[E(R_P) − R_f] — and its standard deviation is *also* linear, σ_c = y·σ_P (no cross term survives). A linear return plotted against a linear risk traces a straight line, the Capital Allocation Line, running from R_f through P.

**A7. What is the slope of the CAL, and why do we rotate the line to be tangent to the frontier?**
The slope is the Sharpe ratio of P, S_P = [E(R_P) − R_f] / σ_P — extra return per unit of total risk. A steeper CAL dominates a flatter one (more reward per unit risk at every point), so we rotate the line upward until it just touches the efficient frontier. That tangency point is the maximum-Sharpe risky portfolio, optimal for every investor regardless of risk appetite.

**A8. State the Tobin (two-fund) separation theorem and its practical consequence.**
Every investor, whatever their risk aversion, holds the *same* risky portfolio — the tangency portfolio — and adjusts only the split between it and the risk-free asset. The investment decision (which risky mix) is separated from the financing decision (how much cash vs. risky). Practically, this is the theoretical charter for index investing: hold one broad market fund and dial risk up or down with cash or leverage.

**A9. Distinguish the CAL, the CML, and (looking ahead) the SML.**
The CAL is *any* risk-free-plus-risky-portfolio line for a given investor; its slope is that portfolio's Sharpe ratio. The CML is the *specific* CAL through the market portfolio in equilibrium — it prices *efficient* portfolios using total risk σ. The SML (CAPM, next chapter) prices *all individual assets* using β, not σ. Every CML is a CAL; not every CAL is the CML.

**A10. Is the GMVP the best portfolio to hold once a risk-free asset exists? Why or why not?**
No. The GMVP minimises risk but usually has a lower Sharpe ratio than the tangency portfolio. Once a risk-free asset exists, the optimal risky holding is the tangency (max-Sharpe) portfolio; you reach any desired risk level by mixing it with the risk-free asset along the CAL, which dominates the frontier everywhere except at the single tangency point.

---

## SECTION B — Numerical Problems (Full Step-by-Step)

*Base data for B1–B4: Asset A — E(R_A) = 10%, σ_A = 20%. Asset B — E(R_B) = 16%, σ_B = 30%.*

### B1 — The diversification effect across correlations
Invest 60% in A, 40% in B. Find portfolio return and risk for ρ = +1, 0, and −1.

**Return** (independent of ρ): E(R_p) = 0.6(10) + 0.4(16) = 6 + 6.4 = **12.4%**.

Weighted-average SD benchmark: 0.6(20) + 0.4(30) = 12 + 12 = 24%.

**ρ = +1:** σ²_p = 0.36(400) + 0.16(900) + 2(0.6)(0.4)(1)(20)(30) = 144 + 144 + 288 = 576 → σ_p = **24%**. Equals the weighted average — no diversification.

**ρ = 0:** σ²_p = 144 + 144 + 0 = 288 → σ_p = √288 = **16.97%**. Risk fell from 24% to 16.97% for the *same* 12.4% return — the free lunch.

**ρ = −1:** σ_p = |0.6(20) − 0.4(30)| = |12 − 12| = **0%**. Perfect hedge.

**Reconciliation:** return is pinned at 12.4% throughout while risk collapses 24% → 16.97% → 0% as ρ falls +1 → 0 → −1. Lower correlation ⇒ more free risk reduction. The ρ = −1 result checks against the risk-eliminating weight w_A = σ_B/(σ_A + σ_B) = 30/50 = 0.60, exactly our 60% ✓.

### B2 — Global Minimum Variance Portfolio (ρ = 0.30)
Covariance σ_AB = ρσ_Aσ_B = 0.30(20)(30) = 180. Find the GMVP weights, return, and risk.

**Weights:**
w_A = (σ_B² − σ_AB) / (σ_A² + σ_B² − 2σ_AB) = (900 − 180) / (400 + 900 − 360) = 720 / 940 = **0.766**.
So w_A = 76.6%, w_B = 23.4%.

**Risk:** σ²_p = 0.766²(400) + 0.234²(900) + 2(0.766)(0.234)(180)
= 0.587(400) + 0.0548(900) + 2(0.1792)(180)
= 234.7 + 49.3 + 64.5 = 348.5 → σ_p = **18.67%**.

**Return:** E(R_p) = 0.766(10) + 0.234(16) = 7.66 + 3.74 = **11.40%**.

**Verification it is the minimum:** test the 60/40 mix at ρ = 0.30. σ²_p = 144 + 144 + 2(0.24)(180) = 144 + 144 + 86.4 = 374.4 → σ_p = 19.35% > 18.67% ✓. The formula genuinely found a lower-risk mix.

### B3 — Optimal risky portfolio, Sharpe ratio, complete portfolio (R_f = 5%, ρ = 0.30)
Excess returns: A → 10 − 5 = 5%; B → 16 − 5 = 11%. σ_AB = 180.

**Tangency weights:**
w_A* = [ (5)(900) − (11)(180) ] / [ (5)(900) + (11)(400) − (5 + 11)(180) ]
= (4500 − 1980) / (4500 + 4400 − 2880) = 2520 / 6020 = **0.4186**.
So P = 41.9% A, 58.1% B.

**Return of P:** 0.4186(10) + 0.5814(16) = 4.186 + 9.302 = **13.49%**.

**Risk of P:** σ²_P = 0.4186²(400) + 0.5814²(900) + 2(0.4186)(0.5814)(180)
= 0.1752(400) + 0.3380(900) + 2(0.2434)(180)
= 70.1 + 304.2 + 87.6 = 461.9 → σ_P = **21.49%**.

**Sharpe ratio of P:** S_P = (13.49 − 5) / 21.49 = 8.49 / 21.49 = **0.395**.

**Verify P beats the GMVP on Sharpe:** GMVP Sharpe = (11.40 − 5) / 18.67 = 6.40 / 18.67 = 0.343 < 0.395 ✓. The tangency portfolio has the steepest CAL, as required.

**Complete portfolio for A = 4:**
y* = [E(R_P) − R_f] / (A·σ²_P) = 0.0849 / (4 × 0.04619) = 0.0849 / 0.18476 = **0.459**.
Put 45.9% in P, 54.1% in T-bills.
- Return: 5 + 0.459(8.49) = 5 + 3.90 = **8.90%**.
- Risk: 0.459(21.49) = **9.86%**.
- Sharpe (must be unchanged on the CAL): (8.90 − 5) / 9.86 = 3.90 / 9.86 = **0.395** ✓.

**Reconciliation:** the complete portfolio sits *on the same CAL* as P — identical Sharpe, but lower risk and return because it lies between R_f and P. Mixing the risk-free asset with the one optimal risky portfolio just slides you along a single straight line — two-fund separation in action.

### B4 — Large-portfolio limit (systematic floor)
Suppose 50 stocks each have σ = 30% (variance 900) and every pair has covariance 100 (average correlation ≈ 100/900 ≈ 0.11). Equal weights. Find portfolio variance for n = 50 and the limit as n → ∞.

**n = 50:** σ²_p = (1/n)·(avg variance) + (1 − 1/n)·(avg covariance)
= (1/50)(900) + (49/50)(100) = 18 + 98 = 116 → σ_p = √116 = **10.77%**.

**n → ∞:** σ²_p → average covariance = 100 → σ_p = √100 = **10%**.

**Reconciliation:** a single stock carried σ = 30%; diversifying into 50 cut it to 10.77%, and the theoretical floor is 10%. The extra 0.77% is the last sliver of unsystematic risk (the 18 own-variance term shrinking as n grows). No amount of diversification breaks below 10% — that is the systematic floor equal to the average covariance.

---

## SECTION C — Interview-Style Questions (Model Answers)

**C1. "Walk me through why diversification is called a free lunch."**
It is free because you give up nothing in expected return to get it. Portfolio return is just the weighted average of component returns, so mixing assets never lowers expected return below its components' average. But portfolio *risk* is below the weighted average whenever assets are imperfectly correlated, because the covariance cross-terms carry ρ < 1. So you buy risk reduction at zero cost in return. In B1 the 60/40 mix held return fixed at 12.4% while risk dropped from 24% to 16.97% simply by moving from ρ = +1 to ρ = 0. That gap is the free lunch, and it is the only such gift in finance.

**C2. "A stock is very volatile in isolation. Would you ever add it to a diversified portfolio?"**
Yes — standalone σ is the wrong lens. What matters is the asset's *marginal contribution* to portfolio risk, which is driven by its covariance with what you already hold, not its own variance. A high-σ asset with low or negative correlation can actually *lower* total portfolio risk. That is exactly why long-duration bonds or gold earn a place in equity portfolios despite being volatile: their low or negative correlation with equities damps the combined swings. The extreme case is B1's ρ = −1, where adding the volatile asset in the right weight drove risk to zero.

**C3. "How many stocks does it take to be diversified?"**
Most unsystematic risk is gone by roughly 20–30 well-chosen, low-correlation names; beyond that the marginal benefit is tiny because you are already close to the systematic floor. The math is that own-variance falls like 1/n while average covariance does not, so portfolio variance asymptotes to the average covariance — you can never diversify below it. In B4, going from one stock (30%) to fifty (10.77%) captured almost all the benefit, and the infinite-stock floor was still 10%. Adding the 200th stock barely moves the needle.

**C4. "Explain CAL versus CML to a client without jargon."**
A CAL is your personal menu line: pick any risky portfolio, mix it with cash, and you get a straight risk-return line whose steepness is that portfolio's reward-to-risk ratio. There are infinitely many CALs — one per risky portfolio you might pick. The CML is the single best one: the line through the *market portfolio*, which in an efficient market is the steepest line achievable and therefore the one everyone should ride. So the CML is just the winning CAL. The client's only real choice is where to sit on it — more cash for safety, more market (or borrowing) for growth.

**C5. "Why does modern finance say only systematic risk is rewarded?"**
Because rewards must reflect risk you cannot avoid. Unsystematic risk is avoidable for free through diversification, so a competitive market will not pay a premium for bearing it — anyone demanding compensation for diversifiable risk is undercut by an investor who has already diversified it away. What is left, systematic risk, hits every asset and cannot be escaped by any investor, so it commands a premium. This is precisely why CAPM prices assets on β (systematic sensitivity) rather than total σ, and it flows directly from the variance decomposition σ²ᵢ = βᵢ²σ²_M + σ²(εᵢ).

**C6. "What is the significance of the tangency portfolio being the market portfolio in equilibrium?"**
If every investor faces the same information and the same risk-free rate, they all compute the same tangency portfolio and all want to hold it. For markets to clear, that common portfolio must contain every risky asset in proportion to its market value — otherwise some asset has no buyer. So the tangency portfolio *is* the value-weighted market portfolio, and its CAL becomes the Capital Market Line. This is the hinge between Markowitz's optimisation and CAPM: it converts a personal optimisation into an equilibrium pricing statement about the whole market.

---

## SECTION D — Multiple Choice (with Reasoning)

**D1. The lower branch of the minimum-variance frontier (below the GMVP) is:**
(a) part of the efficient frontier (b) the Capital Market Line (c) dominated and not efficient (d) where the tangency portfolio lies
**Answer: (c).** For any portfolio on the lower branch, a portfolio directly above it has the same risk and higher return, so it is dominated. Only the upper branch above the GMVP is efficient. (b) and (d) involve the risk-free asset, not the risky-only frontier.

**D2. Two assets have ρ = −1, σ₁ = 20%, σ₂ = 30%. The weight in asset 1 that eliminates all risk is:**
(a) 40% (b) 50% (c) 60% (d) risk cannot be eliminated
**Answer: (c).** With ρ = −1, σ_p = |w₁σ₁ − w₂σ₂|; setting it to zero gives w₁ = σ₂/(σ₁ + σ₂) = 30/50 = 0.60. (d) is wrong precisely because ρ = −1 is the knife-edge case where a perfect hedge exists.

**D3. As the number of equally weighted, imperfectly correlated stocks grows without bound, portfolio variance approaches:**
(a) zero (b) the average variance of the individual stocks (c) the average covariance between pairs (d) the market variance σ²_M
**Answer: (c).** σ²_p = (1/n)(avg variance) + (1 − 1/n)(avg covariance); the own-variance term vanishes as n → ∞, leaving the average covariance as the systematic floor. It only reaches zero (a) if all pairwise covariances are zero, which real equities never satisfy.

**D4. The slope of the Capital Allocation Line equals:**
(a) beta of the portfolio (b) the Sharpe ratio of the risky portfolio (c) the risk-free rate (d) portfolio variance
**Answer: (b).** The CAL is E(R_c) = R_f + [(E(R_P) − R_f)/σ_P]·σ_c, so its slope is (E(R_P) − R_f)/σ_P, the Sharpe ratio. Maximising this slope is what identifies the tangency portfolio.

**D5. Which statement about the CML and the SML is correct?**
(a) both price individual assets using beta (b) the CML uses total risk σ for efficient portfolios; the SML uses β for all assets (c) the CML uses β; the SML uses σ (d) they are the same line
**Answer: (b).** The CML relates expected return of *efficient* portfolios to total risk σ. The SML (CAPM) relates expected return of *any* asset to systematic risk β. Confusing which risk measure applies to which line is the classic exam trap.

**D6. An investor with risk aversion A = 4 faces an optimal risky portfolio with excess return 8.49% and variance 0.04619. The optimal weight in the risky portfolio is closest to:**
(a) 0.23 (b) 0.46 (c) 0.92 (d) 1.15
**Answer: (b).** y* = [E(R_P) − R_f]/(A·σ²_P) = 0.0849/(4 × 0.04619) = 0.0849/0.18476 = 0.459 ≈ 0.46. Matches B3. Since y* < 1 the investor lends some money at R_f rather than borrowing to leverage.

**D7. Adding a risk-free asset to the set of risky portfolios changes the optimal risky holding so that:**
(a) every investor holds the GMVP (b) every investor holds the same tangency (max-Sharpe) portfolio (c) risk-averse investors hold a different risky mix from risk-tolerant ones (d) the efficient frontier disappears
**Answer: (b).** This is two-fund (Tobin) separation: all investors hold the identical tangency portfolio and differ only in the risk-free/risky split. (a) is wrong because the GMVP is not max-Sharpe; (c) contradicts separation.

---

*Self-check note: every numerical answer in Section B was reconciled against an independent route — the ρ = −1 hedge weight (B1), a higher-risk comparison mix (B2), the Sharpe ratio recomputed on the complete portfolio and compared to the GMVP (B3), and the single-stock-versus-floor bracket (B4). All formulas match Chapter 04 §4.1–4.10.*
