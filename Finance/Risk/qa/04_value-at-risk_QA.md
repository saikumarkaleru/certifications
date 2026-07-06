# Q&A — Value at Risk (VaR)

Practice bank for Chapter 04. Every question is followed by a full answer. Work each one before reading the solution. One-tailed z-scores used throughout: 95% → 1.645, 99% → 2.326, 97.5% → 1.960, 90% → 1.282.

---

## Section A — Concept Check

**A1. State the one-line definition of VaR and name the three things every VaR statement must quote.**

VaR is the maximum loss on a portfolio over a given time horizon, at a given confidence level, under normal market conditions — formally, a quantile of the loss distribution. Every VaR statement must quote (1) a **horizon** (how long, e.g. 1-day, 10-day), (2) a **confidence level** (how sure, e.g. 95%, 99%), and (3) a **currency amount** (the loss figure itself). A number without horizon and confidence is meaningless.

**A2. Read the statement "the 1-day 99% VaR is ₹46.6 lakh" as a full sentence.**

"We are 99% confident that the portfolio will not lose more than ₹46.6 lakh over the next trading day. Equivalently, on only 1 day in 100 do we expect a loss worse than ₹46.6 lakh." It is a threshold at the edge of the tail, not a forecast of the average or the worst case.

**A3. Why is a quantile — rather than the mean or the standard deviation — the right statistic for risk limits?**

Risk managers care about the **downside tail**, not the whole distribution. The mean gives the expected outcome and standard deviation gives dispersion in both directions, but a limit must be set against *bad* outcomes specifically. A quantile of the loss distribution answers directly: "how far into the bad tail do we go before events become rare (rarer than 1-in-20 or 1-in-100)?" That is exactly what a loss limit needs.

**A4. VaR aggregates thousands of positions into one number. Why can it do this when a table of greeks cannot?**

Greeks (DV01, delta, gamma, vega) are in incompatible units and cannot be added; they also ignore how positions offset. VaR is computed on **portfolio P&L**, not on individual greeks. Each market scenario produces a single portfolio P&L number after revaluing the *whole book*, so correlations and offsets are captured automatically. Once you have a distribution of portfolio P&L, you read off one tail quantile — one comparable, loss-denominated number.

**A5. Name the two things VaR deliberately does NOT tell you.**

(1) It is a **threshold, not an average** — it says nothing about how bad the loss is *when* you breach it. (2) It applies to **"normal" markets** — it is silent about crashes, gaps, and liquidity holes in the extreme tail. These two silences are the source of every famous VaR limitation.

**A6. All three VaR methods share one engine. What is it?**

Every method builds a **distribution of portfolio P&L** over the horizon and then reads off a tail quantile at the chosen confidence level. The methods differ only in *how they generate that distribution*: historical simulation replays past moves, parametric assumes a distribution shape and uses covariances, Monte Carlo simulates random scenarios.

**A7. Why does higher confidence mean larger VaR but a harder-to-validate model?**

Higher confidence asks about a rarer, worse loss, so the quantile moves further into the tail and VaR grows. But a rarer threshold means **fewer exceptions to observe** — at 99% you expect only ~2-3 breaches per year, giving thin data to backtest. At 95% you get more exceptions, making statistical validation more powerful. There is a trade-off between conservatism and testability.

**A8. Distinguish confidence level from exception rate.**

The confidence level α is the probability the loss stays within VaR; the exception (breach) rate is (1 − α). A 99% VaR is breached about 1% of the time — roughly 2-3 days per year over ~250 trading days. Breaches occurring at the expected rate are evidence the model *works*, not that it is broken.

**A9. Why is historical simulation not truly "assumption-free"?**

It drops the Normality assumption but replaces it with an equally strong one: **the chosen historical window represents the future.** A calm two-year window run into a 2008- or 2020-style crash badly understates risk; a single crash in the window can dominate the tail. The assumption moved from "the distribution is Normal" to "the past repeats" — it did not disappear.

**A10. State the square-root-of-time rule and its key assumption.**

VaR_T = VaR_1 × √T. It assumes returns are independent and identically distributed (i.i.d.) with zero mean, so variance grows linearly with time and standard deviation grows with √T. It breaks under volatility clustering, autocorrelation, and mean reversion, so it is an approximation of convenience, not a law.

---

## Section B — Numerical / Applied (with full solutions)

**B1. Single-asset parametric VaR.** A portfolio is worth V = ₹10 crore with daily return σ = 2%. Assume zero drift, Normal returns. Find the 1-day 99% VaR and the 1-day 95% VaR.

Solution. Use VaR = z × σ × V.

- 99%: z = 2.326. VaR = 2.326 × 0.02 × 10,00,00,000 = 0.04652 × 10,00,00,000 = **₹46,52,000**.
- 95%: z = 1.645. VaR = 1.645 × 0.02 × 10,00,00,000 = 0.0329 × 10,00,00,000 = **₹32,90,000**.

Sanity check: 99% > 95% (₹46.52 lakh > ₹32.90 lakh), as a rarer loss must be larger. Ratio 46.52/32.90 = 1.414 = 2.326/1.645. ✓

**B2. Scaling across horizons.** Using the 1-day 99% VaR of ₹46,52,000 from B1, find the 10-day 99% VaR two ways and reconcile.

Solution.

- Route 1 (scale the VaR): VaR_10 = 46,52,000 × √10 = 46,52,000 × 3.1623 = **₹1,47,11,000** (≈ ₹1.47 crore).
- Route 2 (scale σ first): 10-day σ = 0.02 × √10 = 0.06325; VaR = 2.326 × 0.06325 × 10,00,00,000 = 0.14712 × 10 cr = ₹1,47,12,000.

Both routes agree to rounding. ✓ The tiny difference is rounding only.

**B3. Expected loss vs VaR.** A ₹20 crore book has a daily return with mean μ = +0.05% and σ = 1.8%. Using the full parametric formula VaR = V(z·σ − μ), find the 1-day 99% VaR. Then find it with μ = 0 and comment.

Solution. z = 2.326.

- With drift: z·σ − μ = 2.326 × 0.018 − 0.0005 = 0.041868 − 0.0005 = 0.041368. VaR = 0.041368 × 20,00,00,000 = **₹82,73,600**.
- With μ = 0: VaR = 2.326 × 0.018 × 20,00,00,000 = 0.041868 × 20 cr = ₹83,73,600.

Comment: positive drift *reduces* VaR (expected gain offsets some loss). The difference here is ₹1,00,000 — small over one day, which is exactly why practitioners set μ = 0 intraday. Over a one-year horizon the drift term would be far from negligible.

**B4. Two-asset parametric VaR and diversification benefit.** Asset A: value ₹6 crore, daily σ = 1.5%. Asset B: value ₹4 crore, daily σ = 2.5%. Correlation ρ = 0.30. Confidence 99%. Find diversified VaR, undiversified VaR, and the diversification benefit.

Solution.

Step 1 — currency volatility of each position:
- σ_A$ = 0.015 × 6,00,00,000 = ₹9,00,000 (₹9 lakh)
- σ_B$ = 0.025 × 4,00,00,000 = ₹10,00,000 (₹10 lakh)

Step 2 — portfolio currency volatility (work in lakh):
σ_P$ = √(9² + 10² + 2·0.30·9·10) = √(81 + 100 + 54) = √235 = 15.33 lakh.

Step 3 — diversified VaR: 2.326 × 15.33 = **₹35.66 lakh**.

Step 4 — undiversified VaR (add standalone VaRs):
- VaR_A = 2.326 × 9 = 20.93 lakh; VaR_B = 2.326 × 10 = 23.26 lakh.
- VaR_undiv = 20.93 + 23.26 = **₹44.19 lakh**.

Step 5 — diversification benefit: 44.19 − 35.66 = **₹8.53 lakh**.

Sanity checks: at ρ = 1, σ_P = √(81+100+180) = √361 = 19 lakh → VaR = 2.326 × 19 = ₹44.19 lakh, exactly the undiversified figure (the two definitions coincide at perfect correlation). ✓ At ρ = 0, σ_P = √181 = 13.45 lakh → VaR ₹31.29 lakh, lower still. The diversified figure (₹35.66) sits between the ρ = 0 and ρ = 1 cases, as it must. ✓

**B5. Historical simulation.** Portfolio value V = ₹5 crore. From the 100 most recent daily returns, the ten worst (%) are: −4.20, −3.80, −3.10, −2.90, −2.60, −2.40, −2.20, −2.05, −1.95, −1.80. Find the 95% and 99% VaR.

Solution.

- 95% VaR (100 observations): the worst 5% are the 5 worst days; the 5th-worst return, −2.60%, marks the cutoff. VaR = 0.026 × 5,00,00,000 = **₹13,00,000**.
- 99% VaR: the worst 1% is the single worst day, −4.20% (conservative reading; some conventions interpolate the 1st and 2nd worst). VaR = 0.042 × 5,00,00,000 = **₹21,00,000**.

Cross-check vs parametric: the book's empirical daily σ is about 1.6%, so a Normal 99% VaR would be 2.326 × 0.016 × 5 cr = ₹18.6 lakh — *less* than the historical ₹21 lakh. The historical figure is larger because the real left tail (−4.20%) is fatter than a bell curve predicts. ✓ That is the whole point of historical simulation.

**B6. Expected Shortfall cross-check.** Using B5's data, compute ES at 95% and confirm ES ≥ VaR.

Solution. ES_95% = average loss in the worst 5% of days = mean of the 5 worst returns = (4.20 + 3.80 + 3.10 + 2.90 + 2.60)/5 = 16.60/5 = 3.32%. ES = 0.0332 × 5,00,00,000 = **₹16.6 lakh**. This exceeds VaR_95% of ₹13 lakh because ES averages *into* the tail rather than reading the edge. ES ≥ VaR always holds at the same confidence. ✓

**B7. Diversification with three equal standalone VaRs.** Three desks each have standalone 99% VaR of ₹10 lakh, pairwise correlation ρ = 0.5 between all pairs (equal σ$ of ₹4.30 lakh each, since 2.326 × 4.30 ≈ 10). Find the portfolio VaR and the benefit.

Solution. Work with σ$ = 4.30 lakh each (10/2.326). For n equal-σ positions with common correlation ρ:
σ_P$ = σ$ × √(n + n(n−1)ρ) = 4.30 × √(3 + 6·0.5) = 4.30 × √6 = 4.30 × 2.449 = 10.53 lakh.
VaR_P = 2.326 × 10.53 = **₹24.49 lakh**. Undiversified = 3 × 10 = ₹30 lakh. Diversification benefit = 30 − 24.49 = **₹5.51 lakh**.

Check: at ρ = 1, σ_P = 4.30√(3+6) = 4.30×3 = 12.9 → VaR = 30 lakh (undiversified). ✓ At ρ = 0, σ_P = 4.30√3 = 7.45 → VaR = ₹17.33 lakh (maximum benefit). The ρ = 0.5 result lies between. ✓

**B8. Back-out the confidence level.** A ₹8 crore book has daily σ = 1.25%. Its reported 1-day VaR is ₹23,26,000. What confidence level (z-score) was used?

Solution. VaR = z × σ × V → z = VaR / (σ × V) = 23,26,000 / (0.0125 × 8,00,00,000) = 23,26,000 / 10,00,000 = 2.326. That is the 99% one-tailed z. **Confidence = 99%.**

**B9. Number of expected breaches.** A trading desk uses a 1-day 97.5% VaR over 250 trading days. How many exceptions should it expect in a year, and what would 15 exceptions suggest?

Solution. Expected exception rate = 1 − 0.975 = 2.5%. Expected breaches = 0.025 × 250 = **6.25 ≈ 6 per year**. Fifteen exceptions is roughly 2.4× the expected count — strong evidence the model **understates risk** (σ too low, or the window too calm), and it would move toward the amber/red zone in a traffic-light backtest.

**B10. Undiversified vs diversified ratio.** Two assets have equal standalone VaR and correlation ρ = −0.2. What fraction of the undiversified VaR is the diversified VaR?

Solution. Let each σ$ = s. σ_P$ = √(s² + s² + 2ρs²) = s√(2 + 2ρ) = s√(2 + 2(−0.2)) = s√1.6 = 1.2649s. Undiversified = 2s (before applying z, which cancels in the ratio). Ratio = 1.2649s / 2s = **0.632**, i.e. diversified VaR is about 63% of undiversified — a 37% reduction. Negative correlation gives an even larger benefit than the zero-correlation case (which would give √2/2 = 0.707). ✓

---

## Section C — Interview-Style (with model answers)

**C1. "Explain VaR to a board member in thirty seconds."**

Model answer: "Value at Risk turns our entire trading book into a single rupee figure. Our 1-day 99% VaR is, say, ₹46 lakh. That means on a normal day we are 99% confident we won't lose more than ₹46 lakh, and we'd expect to breach that only about two or three days a year. It lets you compare risk across desks and against limits with one comparable number. The one thing it does not tell you is how bad the loss gets on those rare breach days — for that we look at Expected Shortfall."

**C2. "Walk me through the three ways to compute VaR and their trade-offs."**

Model answer: "All three build a distribution of portfolio P&L and read off a tail quantile; they differ in how they build it. **Historical simulation** replays actual past market moves on today's book — no distributional assumption, captures fat tails and real correlations, handles options if you fully revalue, but assumes the past window represents the future and has thin data in the deep tail. **Parametric / variance-covariance** assumes Normal returns and uses z × σ × V with a covariance matrix — fast, closed-form, easy to decompose, but underweights fat tails and linearises options so it misses gamma. **Monte Carlo** simulates thousands of modelled scenarios with full revaluation — most flexible, handles non-linearity and any distribution, but computationally heavy and exposed to model risk. The trade-off is assumptions vs speed vs flexibility."

**C3. "Why did Basel move from 99% VaR to 97.5% Expected Shortfall under FRTB?"**

Model answer: "Two reasons. First, VaR is **tail-blind** — it's just the threshold and says nothing about the severity of losses beyond it, so two books with identical VaR can have very different tail risk. Second, VaR is **not a coherent risk measure** — it can violate sub-additivity, meaning a combined portfolio's VaR can exceed the sum of parts, which perversely penalises diversification, especially with skewed payoffs like short options or credit. Expected Shortfall averages the losses beyond the quantile, so it captures tail severity and is sub-additive (coherent). FRTB picked 97.5% ES because, under Normality, it sits close to 99% VaR in magnitude while adding tail information."

**C4. "A junior analyst calls a 99% VaR breach a model failure. How do you respond?"**

Model answer: "I'd correct the framing. A 99% VaR is *designed* to be breached about 1% of the time — roughly two to three days per year. A breach at the expected rate is evidence the model is calibrated correctly, not that it failed. The concern is the opposite: too *many* breaches, or none at all over a long period. We validate this formally by backtesting exceptions against Basel's traffic-light zones. One breach is business as usual; a cluster of breaches is the signal to investigate."

**C5. "What's wrong with computing 10-day VaR as 1-day VaR times the square root of ten?"**

Model answer: "The √T rule assumes returns are i.i.d. with zero mean, so variance scales linearly with time. Real markets violate that: there's **volatility clustering** (calm and stormy periods bunch together) and autocorrelation, and over longer horizons mean reversion or trending. So √time scaling can under- or over-state true multi-day risk. It's a convenient approximation — fine for a quick estimate — but Basel's FRTB moved away from naive scaling toward instrument-specific liquidity horizons precisely because it's unreliable in stress."

**C6. "Your parametric VaR and your historical VaR disagree materially. Which do you trust and why?"**

Model answer: "It depends on the book. If the disagreement is that historical VaR is *higher*, it usually means the real return distribution has fatter tails than the Normal assumption behind parametric VaR — I'd lean toward the historical number and treat parametric as optimistic. If the book holds significant options, parametric delta-normal linearises them and misses gamma/convexity, so it's structurally unreliable there and I'd prefer historical or Monte Carlo with full revaluation. But if the historical window is calm and short, it may understate risk, so I'd also run a stressed-window VaR. The right answer is rarely 'trust one blindly' — it's to understand *why* they differ and use the method whose assumptions fit the portfolio."

**C7. "Why isn't VaR additive across desks, and why does that matter for limit-setting?"**

Model answer: "VaR combines through volatilities and correlations, not by addition. Summing desk VaRs implicitly assumes correlation of 1 and so overstates total risk — it ignores the diversification benefit from imperfect correlation. If we set a firm-wide limit as the sum of desk limits we'd be over-conservative in normal times. The subtler danger is the reverse: VaR can occasionally be super-additive, so a naive sum can also *understate* combined risk for skewed books. That non-coherence is why we allocate limits using a proper covariance aggregation and, increasingly, Expected Shortfall."

---

## Section D — Multiple Choice (with reasoning)

**D1. The 1-day 99% VaR of a book is ₹40 lakh. Which statement is correct?**
(a) The book can never lose more than ₹40 lakh in a day.
(b) The book will lose exactly ₹40 lakh on 1 day in 100.
(c) On about 1 day in 100 the loss will exceed ₹40 lakh.
(d) The average daily loss is ₹40 lakh.

Answer: **(c)**. VaR is a threshold exceeded (1 − α) = 1% of the time. (a) is the "worst-case" fallacy — losses can be far larger on breach days. (b) confuses a threshold with an exact value. (d) confuses VaR with the mean.

**D2. For a one-tailed 95% parametric VaR, the correct z-score is:**
(a) 1.960 (b) 1.645 (c) 2.326 (d) 1.282

Answer: **(b) 1.645**. VaR uses the one-tailed z because only the loss (left) tail matters. 1.960 is the *two-tailed* 95% value — a classic trap that overstates a 95% VaR by ~19%. 2.326 is one-tailed 99%; 1.282 is one-tailed 90%.

**D3. Diversification benefit in a two-asset portfolio is zero when:**
(a) ρ = 0 (b) ρ = −1 (c) ρ = +1 (d) volatilities are equal

Answer: **(c) ρ = +1**. At perfect positive correlation, portfolio σ$ equals the sum of position σ$, so diversified VaR equals undiversified VaR and the benefit is zero. Any ρ < 1 produces a positive benefit; equal volatilities alone don't determine it.

**D4. Which method captures option gamma most reliably?**
(a) Delta-normal parametric (b) Variance-covariance (c) Monte Carlo with full revaluation (d) None can

Answer: **(c)**. Monte Carlo (and historical simulation) with *full revaluation* reprices the option in each scenario, capturing convexity. Delta-normal / variance-covariance linearise via delta and miss gamma. (a) and (b) are the same linearising approach.

**D5. A 99% daily VaR model produces 9 exceptions in 250 trading days. This most likely indicates:**
(a) The model is well-calibrated.
(b) The model overstates risk.
(c) The model understates risk.
(d) The confidence level is too high.

Answer: **(c)**. Expected breaches = 1% × 250 ≈ 2-3. Nine is roughly 3-4× that, so actual losses breach VaR far more often than the model predicts — VaR is set too low, understating risk. This pushes the model toward the amber/red backtesting zone.

**D6. Scaling a 1-day VaR to 10 days by √10 assumes:**
(a) Returns are Normally distributed.
(b) Returns are i.i.d. with zero mean.
(c) Volatility clusters over time.
(d) Correlations equal 1.

Answer: **(b)**. The √T rule requires i.i.d. zero-mean returns so variance scales linearly with time. Normality is not strictly required for the scaling itself (it's a variance argument). Volatility clustering (c) actually *breaks* the rule.

**D7. Compared with VaR at the same confidence level, Expected Shortfall is:**
(a) Always smaller (b) Always equal (c) Always greater or equal (d) Unrelated

Answer: **(c)**. ES averages the losses *beyond* the VaR threshold, so ES ≥ VaR at the same confidence — strictly greater whenever any tail mass exists. ES is also coherent (sub-additive), which VaR is not.

**D8. The main reason regulators prefer Expected Shortfall to VaR is that VaR:**
(a) Is harder to compute.
(b) Requires more data.
(c) Is not sub-additive and is tail-blind.
(d) Cannot be backtested.

Answer: **(c)**. VaR can violate sub-additivity (non-coherent) and says nothing about loss severity beyond the quantile (tail-blind). ES fixes both. Note VaR is actually *easier* to backtest than ES, so (d) is false.

**D9. Which is the correct two-asset portfolio currency-volatility formula?**
(a) σ_P = σ_A + σ_B
(b) σ_P = √(σ_A² + σ_B²)
(c) σ_P = √(σ_A² + σ_B² + 2ρσ_Aσ_B)
(d) σ_P = σ_A² + σ_B² + 2ρσ_Aσ_B

Answer: **(c)**. The correlation cross-term 2ρσ_Aσ_B is essential; (b) is only the special case ρ = 0; (a) is only ρ = 1; (d) forgets the square root (units would be wrong).

**D10. Historical simulation's key hidden assumption is that:**
(a) Returns are Normal.
(b) The chosen historical window represents the future.
(c) Volatility is constant.
(d) There is no assumption at all.

Answer: **(b)**. Historical simulation drops Normality but assumes the past window is representative of the future — a calm window understates risk into a crash. (d) is the common misconception; the assumption moved, it did not disappear.

---

*End of Q&A — Value at Risk (VaR).*
