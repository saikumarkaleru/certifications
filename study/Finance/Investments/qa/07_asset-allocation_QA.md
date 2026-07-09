# Q&A — Asset Allocation

> Scope: Investments — Chapter 07 (Asset Allocation). Every question is followed by a full model answer. All rates are annual and in percent unless stated. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** numerical (full step-by-step, reconciling) · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one line

$$E(R_p)=\sum_i w_i E(R_i), \qquad \sigma_p^2=\sum_i\sum_j w_i w_j \sigma_i \sigma_j \rho_{ij}, \qquad U=E(R_p)-\tfrac12\lambda\sigma_p^2$$

**One-line statement:** The mix of asset classes — not the securities inside them — sets the portfolio's fundamental risk-return signature; the strategic mix is the long-run anchor, tactical tilts are deliberate deviations from it, and rebalancing corrects the unintended drift the market imposes.

---

## Section A — Concept Check

**A1. Define asset allocation and explain why it is described as the "dominant" portfolio decision.**
Asset allocation is the deliberate division of a portfolio among broad asset classes — equities, fixed income, cash, and alternatives — chosen to match the investor's return objective, risk tolerance, and time horizon. It dominates because the weights linearly fix the portfolio's expected return and, together with correlations, its variance. A 100% equity and a 100% government-bond portfolio can hold identically excellent securities yet deliver completely different rides — one may fall 40% in a crash, the other 4%. The mix, not the contents, determines the outcome, which is why the first professional question is never "which stock?" but "what mix?"

**A2. Distinguish strategic asset allocation (SAA), tactical asset allocation (TAA), and rebalancing.**
SAA is the long-run *target* mix — the policy portfolio — derived from objectives and capital-market assumptions; it is the anchor the portfolio lives at most of the time. TAA is a *deliberate*, short-to-medium-term tilt *away* from the policy mix to exploit temporary opportunities, operating only within permitted bands. Rebalancing *corrects the unintended* drift caused by price moves, pulling the actual mix *back toward* policy. Key contrast: TAA pushes away from the target on purpose; rebalancing pushes back toward it mechanically.

**A3. Explain precisely what the Brinson "93%" finding does and does not say.**
Brinson, Hood and Beebower (1986) found that investment-policy allocation explained about 93.6% of the *variability (variance) of a single plan's returns through time*. It does **not** say allocation explains 93% of the *level* of returns, nor 93% of the *differences between funds*. Ibbotson–Kaplan (2000) separated the questions: policy explains ~90% of a single fund's variability over time, ~100% of the average return *level* (because active management is roughly zero-sum before costs), but only ~40% of the *variation across funds*, where selection, timing, and cost do the work. The interview trap is conflating "variability over time" with "how one fund beats another."

**A4. Why is diversification across asset classes called the only "free lunch"?**
Because when assets are imperfectly correlated ($\rho<1$), portfolio risk falls *below* the weighted average of the individual risks, while expected return remains *exactly* the weighted average. You keep the average return but shed risk — an asymmetry no other technique offers for free. As $\rho$ falls, the cross term in the variance formula shrinks (and goes negative if $\rho<0$), pulling total risk down.

**A5. What is the policy portfolio, and what are its two jobs?**
The policy portfolio is the documented long-run target mix (weights, benchmarks, ranges) held in the Investment Policy Statement. Its first job is *strategy* — it is where the portfolio lives and the risk profile the investor signed up for. Its second job is to be the *benchmark*: total return decomposes as $R_{portfolio}=R_{policy}+R_{TAA}+R_{selection}+R_{interaction}$, so active value-add can only be measured against the passive result of just holding the policy mix. It is both the strategy and the yardstick.

**A6. Distinguish ability and willingness to take risk, and state the rule when they conflict.**
Ability is *objective* capacity — horizon, wealth relative to needs, income stability, liquidity needs. Willingness is *psychological* — how much volatility the investor can stomach without panic-selling. When they conflict, anchor to the *lower* of the two (or educate the client), because a mathematically optimal portfolio the client abandons at the bottom is worthless. A wealthy retiree may have high ability but low willingness — the prudent mix respects the willingness.

**A7. Why does a longer horizon justify more equity — and what is the interview nuance?**
A long horizon lets the investor *ride out* drawdowns without being forced to sell at the bottom and lets compounding dominate; a young worker also holds large bond-like *human capital*, so more financial-portfolio equity balances the total. The nuance: annual equity volatility does not shrink, and the absolute *dispersion of terminal wealth actually widens* with horizon. Equities are not "safe if held long enough" in a strict variance sense — a long horizon buys the *ability to wait* (low liquidity risk), not the elimination of risk.

**A8. Contrast calendar, threshold, and hybrid rebalancing.**
*Calendar* rebalances on a fixed schedule (e.g., quarterly) regardless of drift — simple and predictable but blind to moves between dates. *Threshold* rebalances whenever a class breaches a tolerance band (e.g., ±5 pp) — it responds to actual risk and captures more of the buy-low/sell-high premium but needs continuous monitoring and can trade often. *Hybrid* checks on a schedule but trades only if outside the band — the professional default, capping monitoring cost while avoiding needless small trades.

**A9. When does rebalancing add return, and when does it hurt?**
Its *dependable* benefit is risk control. A return "bonus" (the volatility/diversification return) appears only when markets *mean-revert* — systematically selling the risen asset and buying the fallen one harvests the reversal. In a strong *sustained trend*, rebalancing *drags* because you keep selling the winner too early. In taxable accounts, over-frequent rebalancing can also trigger capital-gains tax that dwarfs the risk-control benefit.

**A10. What is CPPI and how is it the mirror image of rebalancing?**
Constant Proportion Portfolio Insurance sets risky exposure = $m\times(\text{Portfolio value}-\text{Floor})$, where the bracket is the "cushion." As the portfolio rises, exposure rises; as it falls toward the floor, exposure is cut toward zero. It therefore *buys winners and sells losers* — the opposite of rebalancing, which sells winners and buys losers. CPPI is used when protecting a minimum value matters more than mean reversion.

**A11. What does the RRTTLLU checklist capture, and where does it live?**
It is the IPS constraint framework: **R**eturn objective, **R**isk tolerance, **T**ime horizon, **T**axes, **L**iquidity, **L**egal/regulatory, **U**nique circumstances. It lives in the Investment Policy Statement and ensures the strategic mix is feasible and tailored to the specific investor before any optimisation.

---

## Section B — Numerical Problems

**B1. Expected return and risk of a strategic mix.** A policy portfolio is 60% equity, 30% bonds, 10% gold. E(R): equity 12%, bonds 7%, gold 8%. σ: equity 18%, bonds 6%, gold 15%. Correlations: E–B = −0.20, E–G = 0.10, B–G = 0.30. Find E(R_p) and σ_p, and quantify the diversification benefit.

**Step 1 — Expected return.**
$$E(R_p)=0.60(12)+0.30(7)+0.10(8)=7.20+2.10+0.80=\mathbf{10.10\%}$$

**Step 2 — Variance** (decimals: σ_E=0.18, σ_B=0.06, σ_G=0.15).
Own-variance terms:
- Equity: $0.6^2(0.18^2)=0.36(0.0324)=0.011664$
- Bonds: $0.3^2(0.06^2)=0.09(0.0036)=0.000324$
- Gold: $0.1^2(0.15^2)=0.01(0.0225)=0.000225$

Cross terms ($2w_iw_j\sigma_i\sigma_j\rho$):
- E–B: $2(0.6)(0.3)(0.18)(0.06)(-0.20)=-0.0007776$
- E–G: $2(0.6)(0.1)(0.18)(0.15)(0.10)=0.000324$
- B–G: $2(0.3)(0.1)(0.06)(0.15)(0.30)=0.000162$

Sum: $\sigma_p^2=0.011664+0.000324+0.000225-0.0007776+0.000324+0.000162=0.0129214$
$$\sigma_p=\sqrt{0.0129214}=\mathbf{11.37\%}$$

**Step 3 — Reconcile.** Weighted-average σ (the all-$\rho=1$ case) = $0.6(18)+0.3(6)+0.1(15)=10.8+1.8+1.5=14.1\%$. Actual 11.37% < 14.1% — diversification shaved ~2.7 pp of volatility while keeping the 10.10% return. The negative E–B correlation drives the largest cross term negative, pulling risk well below the weighted average — the free lunch, quantified.

**B2. Rebalancing versus doing nothing in a reversal.** Start ₹10,00,000 at 60/40 → ₹6,00,000 equity, ₹4,00,000 bonds. Year 1: equity +25%, bonds +4%. Rebalance back to 60/40. Year 2: equity −15%, bonds +5%. Compare rebalanced vs never-rebalanced ending wealth.

**Year 1 growth.** Equity → 6,00,000×1.25 = ₹7,50,000; bonds → 4,00,000×1.04 = ₹4,16,000; total = ₹11,66,000. Equity weight = 7,50,000/11,66,000 = **64.3%** (drifted above 60%, now riskier).

**Rebalance.** Target equity = 0.60×11,66,000 = ₹6,99,600 → sell ₹50,400 equity, buy ₹50,400 bonds (bonds to ₹4,66,400).

**Year 2, Path A (rebalanced).** Equity 6,99,600×0.85 = ₹5,94,660; bonds 4,66,400×1.05 = ₹4,89,720; **total = ₹10,84,380**.

**Year 2, Path B (never rebalanced).** Equity 7,50,000×0.85 = ₹6,37,500; bonds 4,16,000×1.05 = ₹4,36,800; **total = ₹10,74,300**.

**Result & reconciliation.** Rebalanced wins by ₹10,84,380 − ₹10,74,300 = **₹10,080**. Check the mechanic: Path A had ₹50,400 less equity exposed to the Year-2 return gap (bonds +5% vs equity −15% = 20 pp). ₹50,400 × 0.20 = **₹10,080** — exact match. The bonus exists because markets reversed; had equity kept rising, Path B would have won.

**B3. Mapping risk aversion to a mix via utility.** Two candidate mixes — Aggressive (80/20): E(R)=11.5%, σ=15.0%; Balanced (60/40): E(R)=10.1%, σ=11.4%. Using $U=E(R)-\tfrac12\lambda\sigma^2$, which does an investor with λ=4 choose, and which with λ=1.5?

**λ=4.**
- Aggressive: $0.115-0.5(4)(0.15^2)=0.115-2(0.0225)=0.115-0.045=\mathbf{0.0700}$
- Balanced: $0.101-0.5(4)(0.114^2)=0.101-2(0.012996)=0.101-0.025992=\mathbf{0.0750}$
- **Balanced wins** (0.0750 > 0.0700).

**λ=1.5.**
- Aggressive: $0.115-0.5(1.5)(0.0225)=0.115-0.016875=\mathbf{0.0981}$
- Balanced: $0.101-0.5(1.5)(0.012996)=0.101-0.009747=\mathbf{0.0913}$
- **Aggressive wins** (0.0981 > 0.0913).

**Break-even λ (reconcile).** Set utilities equal: $0.115-0.5\lambda(0.0225)=0.101-0.5\lambda(0.012996)$ → $0.014=0.5\lambda(0.009504)=0.004752\lambda$ → $\lambda=2.95$. So λ below 2.95 → aggressive, above → balanced. λ=1.5 (below) chose aggressive; λ=4 (above) chose balanced — consistent.

**B4. Threshold rebalancing trigger.** Policy equity weight is 55% with a ±5-percentage-point band. Current portfolio: equity ₹6,30,000, bonds ₹3,70,000. Is a trade required, and if so how much equity is bought/sold?

Total = ₹10,00,000; equity weight = 6,30,000/10,00,000 = **63%**. Band is 50%–60%; 63% > 60%, so the band is **breached** and a trade is required. Target equity = 0.55×10,00,000 = ₹5,50,000 → **sell ₹80,000 of equity** and buy ₹80,000 of bonds. Check: new equity 5,50,000/10,00,000 = 55% ✓, bonds 4,50,000 = 45% ✓.

**B5. The "110 minus age" heuristic and a glide path.** An investor is 35 today. Using equity % ≈ 110 − age, what is the target equity weight now and at 65, and what is the average annual reduction in equity weight along the glide path?

Now: 110 − 35 = **75% equity**. At 65: 110 − 65 = **45% equity**. Change over 30 years = 75 − 45 = 30 pp → **1 percentage point per year**. This mechanical decline is exactly what a target-date/lifecycle fund automates as it de-risks toward the retirement year.

**B6. CPPI exposure.** Portfolio value ₹20,00,000, floor ₹15,00,000, multiplier m = 3. What is the target equity exposure, and what happens to it if the portfolio falls to ₹16,00,000?

At ₹20,00,000: cushion = 20,00,000 − 15,00,000 = ₹5,00,000; exposure = 3×5,00,000 = **₹15,00,000** (75% of the portfolio). At ₹16,00,000: cushion = ₹1,00,000; exposure = 3×1,00,000 = **₹3,00,000** (18.75%). As the portfolio fell toward the floor, exposure was cut sharply — CPPI de-risks into weakness, the mirror image of rebalancing.

---

## Section C — Interview-Style Questions

**C1. "Your client's adviser says asset allocation determines 90% of returns. Is that right?"**
Model answer: It is right only with careful wording. The Brinson evidence is that policy allocation explains ~90% of the *variability of a single portfolio's returns over time* — sensible, because if you are 60% equity your quarter-to-quarter swings track equities. Ibbotson–Kaplan showed it also explains ~100% of the *average level* of returns, since active management is roughly zero-sum before costs. But it explains only ~40% of the *differences between funds* — there, selection, timing, and fees decide. So allocation dominates the risk you take and the return you can expect, but it is not the whole story of why one manager beats another. I would never say "90% of returns" unqualified.

**C2. "Walk me through how you would set a strategic asset allocation for a 40-year-old with a stable salary and a 25-year horizon."**
Model answer: Start with the IPS and RRTTLLU. Return objective and risk tolerance come first — I separate *ability* (high: long horizon, stable income, large bond-like human capital) from *willingness* (I would probe with drawdown scenarios) and anchor to the lower. Then capital-market assumptions per asset class feed a mean-variance optimiser to trace the efficient frontier, and I pick the frontier point matching the client's risk-aversion λ via $U=E(R)-\tfrac12\lambda\sigma^2$. Because raw optimisers are hyper-sensitive to input errors, I temper them with constraints/ranges, Black–Litterman blending, or a heuristic anchor like "110 − age" (~70% equity here). I document target weights, bands, benchmarks, and a rebalancing rule. Given his profile I would land near 70–75% equity with a diversified fixed-income and modest alternatives sleeve, then de-risk along a glide path.

**C3. "In 2022 both stocks and bonds fell. Doesn't that prove the 60/40 and diversification are dead?"**
Model answer: No — it proves correlations are *regime-dependent*, which is a known caveat, not a refutation. Equity and high-quality government bonds are usually negatively or weakly correlated because bonds rally in flights to safety, which is why 60/40 became the default. But 2022 was an inflation/rate shock that drove both down together, so the equity-bond diversification broke for a year — and alternatives like commodities and gold earned their keep. The lesson is to stress-test correlation assumptions and hold genuinely differentiated diversifiers, not to abandon diversification. Over long horizons the imperfect correlation still delivers the free lunch; you just cannot assume it holds in every regime.

**C4. "Why not just rebalance daily to keep risk perfectly on target?"**
Model answer: Because rebalancing has costs that eventually swamp its benefit. Its dependable payoff is risk control, and a modest return bonus when markets mean-revert — but each trade incurs transaction costs, and in taxable accounts realises capital-gains tax. Daily rebalancing multiplies both while the marginal risk-control gain over, say, a quarterly hybrid rule is tiny. The professional default is hybrid: check on a schedule but trade only when a class breaches its tolerance band. That captures nearly all the risk control while trading rarely. Tighter bands make sense only for high-volatility assets, low-cost or tax-sheltered accounts, and low-risk-tolerance clients.

**C5. "Explain the difference between tactical asset allocation and rebalancing to a client who thinks they are the same."**
Model answer: Both move the actual mix, but in opposite spirit. Rebalancing is *maintenance*: the market pushes your weights away from target as prices drift, and rebalancing trims what grew and tops up what shrank to restore the intended risk — it pulls you *back toward* policy and requires no forecast. TAA is a *deliberate bet*: I intentionally tilt *away* from policy — say to 68% equity from a 60% target — because I judge equities temporarily cheap, then revert once the view plays out. Rebalancing corrects drift you did not choose; TAA is drift you chose. Both stay inside the strategic bands.

---

## Section D — Multiple Choice (with reasoning)

**D1. The Brinson (1986) result that policy explains ~93.6% refers to:**
(a) the level of a fund's return · (b) the variability of a single fund's return over time · (c) the differences in returns across funds · (d) after-fee alpha
**Answer: (b).** It measured variance of one plan's returns through time. Level is ~100% (Ibbotson–Kaplan); cross-fund variation is ~40%.

**D2. Rebalancing reliably provides:**
(a) higher return in all markets · (b) risk control, plus a return bonus only when markets mean-revert · (c) tax savings · (d) protection of a floor value
**Answer: (b).** Risk control is dependable; the return bonus needs mean reversion and reverses in sustained trends. Floor protection is CPPI's job (d).

**D3. An investor with high ability but low willingness to take risk should be given a mix that is:**
(a) aggressive, matching ability · (b) conservative, anchored to the lower (willingness) · (c) the average of the two · (d) 100% cash
**Answer: (b).** Anchor to the lower of ability and willingness; an optimal portfolio the client abandons in a panic is worthless.

**D4. A portfolio's expected return relative to the weighted average of asset-class returns is:**
(a) lower, due to diversification · (b) higher, due to diversification · (c) exactly the weighted average · (d) unpredictable
**Answer: (c).** Expected return is linear in weights — diversification reduces *risk*, not expected return. That asymmetry is the free lunch.

**D5. CPPI with multiplier m and floor F sets risky exposure equal to:**
(a) $m\times F$ · (b) $m\times(\text{Value}-F)$ · (c) $(\text{Value}-F)/m$ · (d) $m\times\text{Value}$
**Answer: (b).** Exposure = m × cushion, where cushion = Value − Floor. Exposure falls to zero as value approaches the floor.

**D6. Under $U=E(R)-\tfrac12\lambda\sigma^2$, raising the risk-aversion coefficient λ moves the chosen strategic mix toward:**
(a) more equity · (b) more bonds and cash · (c) no change · (d) more leverage
**Answer: (b).** Higher λ penalises variance more heavily, so the optimum sits at lower σ — more fixed income and cash.

**D7. Which rebalancing method is generally the professional default?**
(a) daily calendar · (b) pure threshold with no schedule · (c) hybrid: scheduled check, trade only if outside the band · (d) never rebalance
**Answer: (c).** Hybrid caps monitoring cost while avoiding needless small trades — best risk control per unit of cost and tax.

**D8. The "110 minus age" rule and target-date fund glide paths primarily encode:**
(a) tax optimisation · (b) declining equity weight as horizon shortens and risk-aversion rises with age · (c) tactical timing · (d) currency hedging
**Answer: (b).** Equity share falls automatically as the target date approaches — de-risking over the lifecycle.

---

### Self-check log
B1: σ_p 11.37% < weighted-avg 14.1% ✓ (negative E–B corr drives it). B2: ₹10,080 gap reconciled via 50,400×0.20 ✓. B3: λ=1.5→aggressive, λ=4→balanced, break-even λ=2.95 consistent ✓. B4: post-trade 55/45 hits target ✓. B5: 75%→45% over 30 yrs = 1 pp/yr ✓. B6: exposure 15,00,000→3,00,000 as value falls toward floor ✓.
