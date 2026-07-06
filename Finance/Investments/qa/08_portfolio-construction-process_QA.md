# Q&A — The Portfolio Construction Process

> Scope: Investments — Chapter 08 (The Portfolio Construction Process). Every question is followed by a full model answer. All rates are annual and in percent unless stated. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** numerical (full step-by-step, reconciling) · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one line

$$\text{IPS} \rightarrow \text{CME} \rightarrow \text{SAA} \rightarrow \text{selection} \rightarrow \text{sizing} \rightarrow \text{constrained MVO} \rightarrow \text{implementation} \rightarrow \text{monitoring} \rightarrow \text{rebalance} \circlearrowleft$$

**One-line statement:** Portfolio construction is the disciplined, looping industrial process — anchored on the Investment Policy Statement — that converts a research view and a client mandate into a live, cost-aware, monitored book of positions, where allocation drives risk, selection and sizing drive alpha, and implementation decides how much alpha survives.

---

## Section A — Concept Check

**A1. What is the Investment Policy Statement (IPS) and why is it the spine of the whole process?**
The IPS is the governing contract encoding the **return objective**, **risk tolerance**, and the **five constraints** — Liquidity, Time horizon, Taxes, Legal/regulatory, Unique circumstances (LTTLU). It is the spine because every downstream decision must be *traceable* to it: a position that cannot be justified against the IPS does not belong in the book. It converts "grow my money" into a concrete required return and risk budget the optimiser can target.

**A2. State the three-layer insight about where risk and alpha come from.**
**Allocation decides most of your risk; selection and construction decide most of your alpha; implementation decides how much of that alpha survives.** The three layers are separable, each with distinct error characteristics and distinct owners, which lets you apply the right risk budget to each.

**A3. What does the Brinson-Hood-Beebower result actually say — and what is the common misquote?**
It says policy (strategic) asset allocation explains ~90% of the **variability of returns over time** for a diversified balanced fund. The misquote: that allocation explains 90% of the *level* of return or of the *cross-sectional difference* between funds — it does not; selection and timing dominate those. The correct reading motivates real governance effort on the strategic allocation.

**A4. Why are constraints "the definition of the feasible set" rather than annoyances?**
An unconstrained optimiser will concentrate, lever, and short its way to a paper Sharpe ratio that cannot be traded. Constraints (position caps, sector bounds, no-short rules, turnover limits) are what make the output *investable*. The art is imposing enough to keep the portfolio sane without so many that you strangle the alpha.

**A5. Define active weight and explain why it is the PM's natural unit of thought.**
Active weight = portfolio weight − benchmark weight ($w_i^a = w_i - w_{b,i}$). It is the natural unit because a PM's *bets are her active weights* — overweights and underweights, not absolute holdings, generate active return and active (tracking) risk. The benchmark is the origin of the coordinate system.

**A6. Why is an unconstrained mean-variance optimiser called an "error maximiser"?**
Because it loads most heavily onto assets with the highest *estimated* returns, which are frequently the ones carrying the largest *estimation error* — it mistakes noisy high estimates for genuine opportunity. This is why constrained, shrinkage-based, or resampled optimisation — and even plain equal-weight (1/N) — frequently beats naïve MVO out of sample.

**A7. State the Fundamental Law of Active Management and name each term.**
$$IR \approx IC \times \sqrt{BR} \times TC$$
$IR$ = information ratio (active return ÷ tracking error); $IC$ = information coefficient (correlation of forecasts to outcomes, i.e. skill); $BR$ = breadth (number of *independent* bets per year); $TC$ = transfer coefficient (fraction of the ideal portfolio that survives constraints and costs, 0–1). The $TC$ term is precisely the construction/implementation term.

**A8. What is the transfer coefficient and why should a PM manage it explicitly?**
$TC$ is the correlation between the *ideal* (unconstrained) active positions and the *actual* implemented positions — how much of the paper alpha survives the constraint and cost layer. It should be managed explicitly because a low $TC$ silently throws away the alpha the research produced; constraints that look prudent can quietly halve your realised IR.

**A9. Distinguish strategic asset allocation (SAA) from tactical asset allocation (TAA).**
SAA is the **long-run policy mix** (e.g., 60/40) set from capital market expectations to meet the required return at acceptable risk — the single biggest driver of return *variability*. TAA is **short-term, deliberate deviation** from SAA to exploit near-term views; it is an active overlay measured and risk-budgeted against the SAA.

**A10. Why is trading treated as an economic decision rather than a reflex?**
Because a basis point of transaction cost is *certain* while the alpha you trade to capture is *probabilistic*. Rational construction only trades when expected alpha exceeds round-trip cost plus the opportunity cost of the tracking error currently carried — which is why no-trade bands and cost-aware rebalancing exist.

**A11. What is implementation shortfall and why is it the "master" cost metric?**
Implementation shortfall (IS) is the gap between a *paper* portfolio (traded instantly at the decision price) and the *real* one: $IS = \text{Execution cost} + \text{Opportunity cost} + \text{Fees}$. It is the master metric because it captures *all* slippage — explicit and implicit, filled and unfilled — in one number, directly measuring the backtest-to-live gap.

**A12. State the square-root market-impact law and its key implication.**
$\text{Impact} \approx \eta\,\sigma\sqrt{Q/V}$, where $\sigma$ is daily volatility, $Q$ order size, $V$ average daily volume, $\eta$ a stock-specific constant of order 1. The implication: impact scales with the *square root* of participation, so trading twice the size costs only ~√2 ≈ 1.41× the impact — which is why large orders are sliced over time to cut participation per tranche.

**A13. Why is rebalancing described as "mechanically contrarian"?**
Because it sells assets that have risen above target weight (winners) and buys those that have fallen below (losers) to restore the policy mix. It harvests a small rebalancing premium from mean reversion and counteracts the behavioural disposition effect — it is the discipline that acts against the momentum-chasing instinct.

**A14. Give the three canonical rebalancing disciplines and the industry standard.**
(1) **Calendar** — rebalance every fixed period; simple but ignores actual drift. (2) **Threshold (tolerance band)** — rebalance only when a weight breaches ±b%; cost-efficient but needs constant monitoring. (3) **Calendar-and-threshold** — check on a calendar but act only if a band is breached; this hybrid is the **industry standard**.

**A15. Why is tracking error not the same as downside risk?**
Tracking error is the standard deviation of *active* return — deviation from the benchmark in *both* directions. A fund can post high TE purely by *outperforming*. It is a symmetric measure of active risk, not a measure of drawdown or downside loss.

---

## Section B — Numerical Problems

**B1. Required return build-up.** A retiree has ₹2,00,00,000 (₹2 crore) of investable assets, needs ₹9,00,000 per year of spending, receives ₹1,00,000 of other income, and faces 4% expected inflation. Find the required nominal return.

*Solution.* Net spending drawn from the portfolio = 9,00,000 − 1,00,000 = ₹8,00,000.
Real return needed = 8,00,000 / 2,00,00,000 = 0.04 = **4.0%**.
Add inflation: $R_{required} = 4.0\% + 4.0\% = \mathbf{8.0\%}$.
*Reconcile.* At 8% the ₹2 cr earns ₹16,00,000; of that, ₹8,00,000 (the 4% real part) funds spending and ₹8,00,000 (the 4% inflation part) preserves real capital. Spending need is exactly met and purchasing power is maintained. ✓

**B2. Constrained sizing to a position cap.** An optimiser wants active weights of +7.9%, +5.9%, +4.0% on three names, but the mandate caps any single active weight at ±3.0%. What is the constrained active-weight vector, and what does this imply for the transfer coefficient?

*Solution.* Cap each at +3.0% ⇒ constrained vector = **(+3.0%, +3.0%, +3.0%)**.
The ideal vector totalled 17.8% of active exposure; the constrained one totals 9.0% — roughly half — and the cap also *flattens the ranking* (the optimiser wanted A > B > C; now they're equal). Both effects lower the correlation between ideal and actual positions, so $TC$ falls well below 1.
*Reconcile.* Since $IR \approx IC\sqrt{BR}\,TC$, halving the effective transfer roughly halves realised IR for the same skill and breadth — the position cap has a direct, quantifiable cost in IR. ✓

**B3. Tracking error from independent active bets.** A PM holds three independent active bets: A (active weight +2.5%, residual vol 24%), B (+2.0%, 30%), C (+1.5%, 28%). Find the total tracking error.

*Solution.* Variance contribution of each = $(w^a)^2\sigma^2$:
A: $0.025^2 \times 0.24^2 = 0.000625 \times 0.0576 = 0.000036$.
B: $0.020^2 \times 0.30^2 = 0.0004 \times 0.09 = 0.000036$.
C: $0.015^2 \times 0.28^2 = 0.000225 \times 0.0784 = 0.00001764$.
Independence ⇒ variances add: $0.000036 + 0.000036 + 0.00001764 = 0.00008964$.
$TE = \sqrt{0.00008964} = 0.00947 = \mathbf{0.95\%}$.
*Reconcile.* Three modest bets deliver under 1% TE — far short of a typical 3% budget. To reach 3% the PM must scale bets by 3/0.95 ≈ 3.2× (risking position caps) or add breadth. The math confirms the Fundamental Law's lesson: breadth, not oversized bets, is the safe route to a risk budget. ✓

**B4. Required breadth from the Fundamental Law.** A PM has skill $IC = 0.06$, faces a transfer coefficient $TC = 0.75$, and targets an information ratio $IR = 0.6$. How many independent bets per year does she need?

*Solution.* Rearranging $IR = IC\sqrt{BR}\,TC$:
$$BR = \left(\frac{IR}{IC \cdot TC}\right)^2 = \left(\frac{0.6}{0.06 \times 0.75}\right)^2 = \left(\frac{0.6}{0.045}\right)^2 = (13.33)^2 \approx \mathbf{178 \text{ bets/year}}.$$
*Reconcile.* Forward-check: $IC\sqrt{BR}\,TC = 0.06 \times \sqrt{178} \times 0.75 = 0.06 \times 13.34 \times 0.75 = 0.600$. ✓ Matches the target exactly. Note how sensitive this is: if constraints cut $TC$ to 0.5, required breadth jumps to $(0.6/0.03)^2 = 400$ bets — the implementation term dominates the workload.

**B5. Market impact and the trade / no-trade gate.** A model says stock Y is 0.90% cheap (90 bps expected alpha). Target trade = ₹6,00,00,000 (₹6 cr). Y: price ₹1,000, ADV = 500,000 shares, daily vol σ = 2.5%, impact constant η = 1. Half-spread = 5 bps, commission = 3 bps. Should she trade today?

*Solution.*
Step 1 — shares: 6,00,00,000 / 1,000 = 60,000 shares. Participation $Q/V$ = 60,000/500,000 = 0.12 = 12% of ADV.
Step 2 — impact: $\eta\,\sigma\sqrt{Q/V} = 1 \times 2.5\% \times \sqrt{0.12} = 2.5\% \times 0.3464 = 0.866\%$ ≈ **87 bps**.
Step 3 — total entry cost: 87 + 5 + 3 = **95 bps**.
Step 4 — net: 90 bps alpha − 95 bps cost = **−5 bps**. *Do not trade in one clip today.*
*Reconcile via slicing.* Slice over, say, 4 days at 3% ADV/day: impact per tranche = $2.5\% \times \sqrt{0.03} = 2.5\% \times 0.1732 = 0.433\%$ ≈ 43 bps. Blended entry cost ≈ 43 + 5 + 3 = 51 bps ⇒ net = 90 − 51 = **+39 bps**. Slicing turns a losing trade into a winner — exactly why execution algorithms exist. ✓
*Consistency check on the law:* cutting participation from 12% to 3% is a 4× reduction; impact fell from 87 to 43 bps, a factor of √4 = 2. ✓

**B6. Rebalancing tolerance band.** A 60/40 policy portfolio uses ±5% *relative* tolerance bands on the equity weight. Equities rally and the mix drifts to 68/32. Has the band been breached, and what is the rebalancing trade on a ₹1 cr book?

*Solution.* A ±5% *relative* band around a 60% target means the allowable range is $60\% \times (1 \pm 0.05) = [57\%, 63\%]$. Current equity weight 68% > 63% ⇒ **band breached**, rebalance triggered.
Trade: target equity = 60% × ₹1 cr = ₹60,00,000; current = ₹68,00,000. **Sell ₹8,00,000 of equities, buy ₹8,00,000 of bonds.**
*Reconcile.* The action is contrarian — it sells the asset that just rose — and restores the 60/40 policy mix. A ±10% relative band ([54%, 66%]) would *still* be breached by 68%; only ±13.3% or wider would leave the drift alone. ✓

---

## Section C — Interview-Style (with model answers)

**C1. "Walk me through your portfolio construction process in 30 seconds."**
*Model answer.* "Start with the IPS — objective, risk budget, and the five constraints. Set capital market expectations, then a strategic allocation that meets the required return. Layer security-selection views as *active weights*, size them to a tracking-error budget, and run a *constrained* optimisation so the output is actually investable. Implement carefully — every trade must clear its cost hurdle, and big orders get sliced because impact scales with the square root of participation. Then monitor: run attribution, watch for drift past the no-trade bands, and rebalance in a cost-aware, contrarian way. Feed attribution back into selection, and repeat for the life of the mandate."

**C2. "A junior analyst hands you an optimiser output with 40% in one small-cap. What's wrong and how do you fix it?"**
*Model answer.* "It's un-investable — that breaches any sane position cap and the liquidity floor; you couldn't build or exit it without huge impact. It's also the classic *error-maximiser* symptom: 40% in one name usually means that name had the highest *estimated* return, i.e. the largest estimation error. Fix: add constraints (position caps, sector bounds, turnover limit), apply shrinkage to the return inputs or resample the frontier, and sanity-check against equal-weight. I'd compare the transfer coefficient before and after to see what the constraints actually cost in alpha."

**C3. "How do you decide whether to act on a signal that says a stock is 0.5% cheap?"**
*Model answer.* "Through the trade/no-trade gate: expected alpha versus *round-trip cost plus the opportunity cost of the tracking error I'm currently carrying*. I estimate impact with the square-root law given my order as a fraction of ADV, add spread and commissions, and compare. Fifty bps is a thin edge — if participation pushes impact near that, I either don't trade or slice over several days. Cost is certain, alpha is probabilistic, so a marginal edge doesn't automatically justify a trade."

**C4. "Your fund has 1% tracking error but the client wants 4%. What are your options and their risks?"**
*Model answer.* "By the Fundamental Law, $IR \approx IC\sqrt{BR}\,TC$, and TE is the scale of my active bets. Three levers: *scale up existing bets* — fast, but drives concentration, may breach caps, and adds risk without improving IR; *add breadth* — more independent bets — which raises TE *and* preserves IR, the safe route but needs genuinely uncorrelated skilled forecasts; and *raise the transfer coefficient* by relaxing over-tight constraints. I'd favour breadth plus a TC review, and be honest that manufacturing TE by concentrating is buying risk without buying skill."

**C5. "Is rebalancing worth the cost? Convince me either way."**
*Model answer.* "It's a cost-benefit decision, not a reflex. Benefit: it keeps risk aligned with the IPS — an un-rebalanced 60/40 drifts to 80/20 after a bull run, no longer the client's risk — and harvests a mean-reversion premium while counteracting behavioural biases. Cost: every rebalance incurs impact, spread, and possibly taxes. The reconciliation is no-trade bands: tolerate more drift when trading is expensive and the drift is cheap in risk terms, using a calendar-and-threshold rule. Worth it — but only inside a disciplined band, never on a hair-trigger."

**C6. "Why not just maximise Sharpe with an unconstrained optimiser?"**
*Model answer.* "Because that portfolio is usually un-tradable and fragile. It shorts freely, concentrates into high-estimation-error names, and its weights swing wildly with tiny input changes — it maximises estimation error as much as return. Real construction adds constraints for investability and shrinkage or resampling for robustness. I'm not after the theoretically optimal paper portfolio; I want the best one *that survives constraints and costs and holds up out of sample* — and I track the transfer coefficient to know what that trade-off costs."

---

## Section D — MCQs (with reasoning)

**D1.** The Brinson-Hood-Beebower studies are best summarised as: policy asset allocation explains ~90% of...
A) the level of a fund's return
B) the cross-sectional difference between funds
C) the variability of a diversified fund's returns over time
D) the alpha generated by security selection

**Answer: C.** The result is about time-series *variability* of a diversified fund's returns, not the level (A) or cross-fund differences (B), where selection and timing dominate. The most-misquoted stat in the chapter.

**D2.** Market impact scales with the square root of participation. Quadrupling the order size (as a fraction of ADV) multiplies impact by approximately:
A) 4× B) 2× C) 1.41× D) 16×

**Answer: B.** $\sqrt{4} = 2$. The square-root law means impact grows *sublinearly* — quadruple the size, only double the impact. (Doubling size would give √2 ≈ 1.41×, option C, which is the distractor for a 2× order.)

**D3.** In the Fundamental Law $IR \approx IC\sqrt{BR}\,TC$, the term most directly controlled by portfolio construction and implementation is:
A) IC B) BR C) TC D) IR

**Answer: C.** The transfer coefficient measures how much of the ideal portfolio survives constraints and trading costs — that is precisely the construction/implementation layer. IC is skill, BR is the research opportunity set, IR is the output.

**D4.** An investor's active weight in a stock is +2%. This means:
A) the stock is 2% of the portfolio
B) the portfolio holds 2% more of the stock than the benchmark does
C) the stock returned 2% more than the benchmark
D) the stock has a beta 2% above the market

**Answer: B.** Active weight = portfolio weight − benchmark weight. It is a positioning (overweight) statement, not an absolute holding (A), a realised return (C), or a beta (D).

**D5.** The optimal no-trade band around a target weight should be *wider* when:
A) transaction costs are low and drift risk is high
B) transaction costs are high and drift risk is low
C) both costs and drift risk are low
D) tracking error must be minimised at all costs

**Answer: B.** You tolerate more drift when trading is expensive (high cost of acting) and the drift adds little risk (low cost of *not* acting). Cheap trading or risky drift (A) argues for a *narrow* band; option D would force a near-zero band regardless of cost.

**D6.** Which statement about the unconstrained mean-variance optimiser is correct?
A) It is robust because it uses all available information
B) It tends to concentrate in assets with the largest estimation error
C) It always beats equal-weight out of sample
D) It requires no expected-return inputs

**Answer: B.** The optimiser overweights the highest *estimated* returns, which are disproportionately the highest *estimation-error* assets — hence "error maximiser." It is fragile not robust (A), often *loses* to equal-weight out of sample (C), and depends heavily on return inputs (D).

**D7.** A PM wants to raise tracking error from 1% to 3% while preserving her information ratio. The soundest approach is to:
A) triple the size of her three largest bets
B) add more independent, equally-skilled bets (increase breadth)
C) remove all position caps
D) increase portfolio turnover

**Answer: B.** Adding independent bets raises TE while holding IC and TC roughly constant, preserving IR (the Fundamental Law). Tripling three bets (A) buys risk through concentration without improving skill; removing caps (C) risks un-investability; turnover (D) is a cost, not a source of active risk.

---

*Self-check note:* All numericals reconciled — B1 spending funded with real capital preserved; B3 three bets give 0.95% TE (under budget); B4 forward-check reproduces IR = 0.60; B5 slicing cuts impact by exactly √4 = 2×; B6 rebalance restores 60/40.
