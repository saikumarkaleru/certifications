# Q&A — Performance Measurement and Attribution

Practice bank for Chapter 11. Work each question before reading the answer. Returns are in percent unless stated; betas are unit-free. Every numerical answer is worked in full and reconciled against a cross-check.

---

## Section A — Concept Checks

**A1. What single sentence underlies the entire chapter?**
A return is only interpretable relative to (a) the risk taken to earn it and (b) a fair, investable alternative (the benchmark). Every measure here elaborates that one idea.

**A2. Why distrust a raw return like "I made 22%"?**
Because it hides three things that decide whether it was skill: how much risk was taken, whether it beat a passive benchmark the client could have bought cheaply, and whether it was a repeatable decision or a single lucky bet. A 22% from a 6%-vol market-neutral book and a 22% from a 35%-vol leveraged momentum bet are not the same achievement.

**A3. Define TWR and MWR in one line each.**
TWR (time-weighted return) breaks the period at each cash flow and geometrically chains the sub-period returns, stripping out flow timing — it measures the *manager's* decisions. MWR (money-weighted return) is the IRR of the portfolio's cash flows — it embeds flow timing and measures the *investor's* actual dollar experience.

**A4. When does MWR fall below TWR, and when does it exceed it?**
MWR falls below TWR when the investor's large inflows land *before* bad periods (more money is exposed to the loss); it exceeds TWR when large inflows land before good periods. The two are equal when there are no external flows, or when every sub-period return is identical.

**A5. Which return should GIPS-compliant managers report for comparison, and why?**
TWR. It removes the timing and size of client cash flows the manager does not control, so it isolates the manager's investment decisions and makes managers comparable on a like-for-like basis.

**A6. Why must you divide return by risk to detect skill?**
Because higher return is the market's payment for bearing risk. Doubling leverage doubles return but adds no skill — the risk-adjusted ratio is unchanged. Skill shows up only as *more return per unit of risk*: raising return without proportionally raising risk, or cutting risk without cutting return.

**A7. Match each ratio to the question it answers.**
Sharpe — excess return per unit of *total* risk (σ); use when the portfolio is the investor's whole wealth. Treynor — excess return per unit of *systematic* risk (β); use for one sleeve of a diversified whole. Sortino — excess return per unit of *downside* deviation; use when only losses matter. Information ratio — active return per unit of *tracking error*; use to judge an active manager against a benchmark.

**A8. Sharpe and Treynor share a numerator. When do their rankings disagree, and what does the gap diagnose?**
They share $R_p - R_f$ and differ only in the denominator (σ vs β). For a fully diversified portfolio $\sigma_p \approx \beta_p\sigma_m$, so rankings agree. For an under-diversified portfolio carrying idiosyncratic risk, Sharpe (which penalizes total risk) ranks it below Treynor (which ignores diversifiable risk). A large Sharpe-vs-Treynor ranking gap is itself a diagnostic of poor diversification.

**A9. Alpha is *not* the same as beating the benchmark — explain.**
Jensen's alpha is return above the *beta-adjusted CAPM requirement*, $\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$, not return above $R_f$ or above the benchmark. A fund with beta 1.5 in a strong bull market can beat its benchmark yet still post *negative* alpha, because CAPM required an even bigger return for that much systematic risk.

**A10. State the Sortino denominator carefully — where do people go wrong?**
Downside deviation squares only the shortfalls below the MAR, but still divides by the *total* number of observations $n$, not the count of negative months: $\sigma_{p,d} = \sqrt{\tfrac1n\sum[\min(R_i - R_{MAR},0)]^2}$. Dividing by the number of negatives is the classic error.

**A11. What does the SAMURAI mnemonic guarantee about a benchmark?**
A valid benchmark is Specified in advance, Appropriate to the style, Measurable, Unambiguous, Reflective of current opinions, Accountable (the manager accepts it), and Investable. It ensures the benchmark is a genuine passive alternative and not a moving or unbeatable yardstick.

**A12. In Brinson attribution, when do you earn positive allocation credit?**
You earn allocation credit for overweighting a segment only if that segment *beat the total benchmark* ($R_{b,i} - R_b > 0$), or for underweighting a segment that *lagged* it. Overweighting a segment that had a positive return but still trailed the overall benchmark is a *negative* allocation call.

---

## Section B — Numerical Problems (full working)

**B1. TWR vs MWR with a mid-year deposit.**
A fund starts at ₹200. Exactly 6 months in, after its value has risen to ₹230, the client adds ₹100. The fund ends the year at ₹363. Find TWR and MWR.

- H1 sub-period: ₹200 → ₹230 before the flow. $r_1 = 230/200 - 1 = 15.0\%$.
- Deposit lifts the base to ₹230 + ₹100 = ₹330 to start H2.
- H2 sub-period: ₹330 → ₹363. $r_2 = 363/330 - 1 = 10.0\%$.
- $R_{TWR} = (1.15)(1.10) - 1 = 1.265 - 1 = 26.5\%$.

MWR (IRR) from the investor's view (outflows negative): −200 at t=0, −100 at t=0.5, +363 at t=1. Solve $200 + \dfrac{100}{(1+r)^{0.5}} = \dfrac{363}{1+r}$.

- Try $r = 25.5\%$: $(1.255)^{0.5} = 1.1203$, so LHS $= 200 + 100/1.1203 = 200 + 89.26 = 289.26$; RHS $= 363/1.255 = 289.24$. Match → **MWR ≈ 25.5%**.

**Reconcile:** MWR (25.5%) < TWR (26.5%) because the large ₹100 deposit was exposed to the weaker H2 (10% vs H1's 15%). The extra money at work during the softer half dragged the investor's dollar return below the manager's decision return — exactly the timing effect TWR is built to strip out. ✔

**B2. The full risk-adjusted suite, cross-checked.**
For one year: $R_p = 16\%$, $R_f = 5\%$, $R_m = 11\%$, $\sigma_p = 18\%$, $\sigma_m = 14\%$, $\beta_p = 1.1$.

- **Sharpe:** $S_p = (16-5)/18 = 11/18 = 0.611$. Market Sharpe $= (11-5)/14 = 6/14 = 0.429$. Portfolio wins on total risk (0.611 > 0.429). ✔
- **Treynor:** $T_p = (16-5)/1.1 = 11/1.1 = 10.0$ (10% excess per unit beta). Market Treynor $= 6/1.0 = 6.0$. Portfolio wins on systematic risk too. ✔
- **Jensen's alpha:** CAPM required $= 5 + 1.1(11-5) = 5 + 6.6 = 11.6\%$. $\alpha = 16 - 11.6 = +4.4\%$. ✔
- **Cross-check (α ↔ Treynor):** $\alpha = \beta_p(T_p - T_m) = 1.1(10 - 6) = 1.1 \times 4 = 4.4\%$ — matches the Jensen alpha exactly. ✔
- **M²:** $M^2 = R_f + S_p\sigma_m = 5 + 0.611 \times 14 = 5 + 8.56 = 13.56\%$. De-levered to the market's 14% vol the portfolio returns 13.56% vs the market's 11% — an **M² spread of +2.56%**, consistent with the Sharpe advantage. ✔

Every measure agrees the manager added value; they just quantify it against different risk yardsticks.

**B3. Sortino vs Sharpe from monthly data.**
Monthly returns in excess of MAR = 0% over 8 months: **+5, −2, +3, −4, +1, −6, +4, +3**.

- Mean $= (5-2+3-4+1-6+4+3)/8 = 4/8 = 0.5\%$.
- **Downside deviation:** negatives −2, −4, −6 → squares 4, 16, 36 → sum 56. $\sigma_{d} = \sqrt{56/8} = \sqrt7 = 2.646\%$.
- **Sortino** $= (0.5 - 0)/2.646 = 0.189$.
- **Sharpe (same data):** deviations from mean 0.5 are 4.5, −2.5, 2.5, −4.5, 0.5, −6.5, 3.5, 2.5; squares 20.25, 6.25, 6.25, 20.25, 0.25, 42.25, 12.25, 6.25 → sum 114; sample variance $= 114/7 = 16.29$; $\sigma = 4.036\%$. Sharpe $= 0.5/4.036 = 0.124$.

**Reconcile:** Sortino (0.189) exceeds Sharpe (0.124) because much of this fund's volatility came from *upside* months (+5, +3, +4, +3), which Sharpe penalizes but Sortino ignores. The gap is the signature of a positively-skewed return stream. ✔

**B4. Brinson attribution — three segments that must reconcile.**

| Segment | $w_p$ | $w_b$ | $R_{p,i}$ | $R_{b,i}$ |
|---|---|---|---|---|
| Equity | 60% | 50% | 14% | 12% |
| Bonds | 30% | 40% | 6% | 5% |
| Cash | 10% | 10% | 3% | 3% |

- $R_b = 0.50(12) + 0.40(5) + 0.10(3) = 6 + 2 + 0.3 = 8.3\%$.
- $R_p = 0.60(14) + 0.30(6) + 0.10(3) = 8.4 + 1.8 + 0.3 = 10.5\%$.
- **Total active return** $= 10.5 - 8.3 = +2.2\%$ (the target our effects must sum to).

**Allocation** $A_i = (w_p - w_b)(R_{b,i} - R_b)$:
- Equity: $(0.10)(12 - 8.3) = 0.10 \times 3.7 = +0.37\%$
- Bonds: $(-0.10)(5 - 8.3) = (-0.10)(-3.3) = +0.33\%$
- Cash: $(0)(3 - 8.3) = 0$
- **Allocation total = +0.70%.**

**Selection** $S_i = w_b(R_{p,i} - R_{b,i})$:
- Equity: $0.50(14 - 12) = +1.00\%$
- Bonds: $0.40(6 - 5) = +0.40\%$
- Cash: $0.10(3 - 3) = 0$
- **Selection total = +1.40%.**

**Interaction** $I_i = (w_p - w_b)(R_{p,i} - R_{b,i})$:
- Equity: $(0.10)(2) = +0.20\%$
- Bonds: $(-0.10)(1) = -0.10\%$
- Cash: $0$
- **Interaction total = +0.10%.**

**Reconcile:** $0.70 + 1.40 + 0.10 = +2.20\%$ = total active return. ✔ The edge here is mostly *selection* (good picks in both equity and bonds). Folding interaction into selection (the two-factor convention) gives Allocation +0.70%, Selection +1.50%, still summing to +2.20%.

**B5. Is the track record statistically significant?**
A manager posts active return 3%, tracking error 4%, over 5 years.

- $IR = 3/4 = 0.75$.
- t-stat $\approx IR \times \sqrt{\text{years}} = 0.75 \times \sqrt5 = 0.75 \times 2.236 = 1.68$.
- Years needed for t ≈ 2: $(2/IR)^2 = (2/0.75)^2 = 2.667^2 = 7.1$ years.

**Reconcile:** t = 1.68 < 2, so even a healthy IR of 0.75 over 5 years is *not* significant at 95% — you need about 7 years. Short track records prove little; this is why hiring on 3-year numbers rewards noise. ✔

**B6. Arithmetic vs geometric mean.**
Annual returns: +30%, −20%, +30%, −20%.

- Arithmetic mean $= (30 - 20 + 30 - 20)/4 = 20/4 = +5.0\%$.
- Geometric: $(1.30 \times 0.80 \times 1.30 \times 0.80)^{1/4} - 1 = (1.0816)^{1/4} - 1$. $\sqrt{1.0816} = 1.0400$, $\sqrt{1.0400} = 1.0198$ → **geometric = +1.98%**.
- Cross-check via $R_g \approx \bar R - \sigma^2/2$: σ of the four returns = 25% (deviations ±25 from mean 5), so $\sigma^2/2 = 0.25^2/2 = 0.03125$; $5\% - 3.125\% = 1.875\%$ ≈ 1.98%. ✔

**Reconcile:** the arithmetic 5% overstates what an investor actually compounded (1.98%); the gap widens with volatility. Report the geometric mean for realized growth. ✔

---

## Section C — Interview-Style Questions (model answers)

**C1. "A manager reports 22%. What do you ask next?"**
Four things. First, is that time-weighted (comparable across managers) or money-weighted (the client's dollar experience)? Second, what was the volatility, beta, and max drawdown — 22% at 6% vol is very different from 22% at 35%. Third, what did the benchmark return; if the Nifty did 21%, she added almost nothing and is a closet indexer charging active fees. Fourth, is it net of fees, and over how long — a one-year number is statistically meaningless. Only after those does 22% become a judgment about skill.

**C2. "Why use TWR rather than MWR to rank managers?"**
Because TWR removes the timing and size of client cash flows, which the manager doesn't control. If a client dumps money in right before a bad quarter, MWR punishes the manager for the client's timing. MWR is the *right* measure only when the manager controls the flows — a private-equity GP calling capital — or when you specifically want the client's realized dollar outcome. For like-for-like manager comparison, GIPS mandates TWR.

**C3. "Sharpe or Treynor — which would you use and when?"**
Same numerator, different risk denominator. Use Sharpe when the portfolio is the investor's entire wealth, because total volatility is what actually hurts them. Use Treynor when the portfolio is one sleeve inside a diversified book, because only its systematic risk survives diversification and matters at the margin. Practically, if the two give very different rankings, that gap itself is telling me the portfolio is under-diversified — it's carrying idiosyncratic risk that Sharpe punishes and Treynor ignores.

**C4. "A fund beat its benchmark by 3% — is that alpha?"**
Not necessarily. Alpha is return above the *beta-adjusted* CAPM requirement, not above the benchmark. If the fund ran a beta of 1.5 in a market that rose strongly, CAPM might have required, say, 5% of outperformance for that much systematic risk — so a 3% beat is actually *negative* alpha. It beat the benchmark by taking more market risk, not by skill. I'd compute $\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$ before calling anything skill.

**C5. "Why report a Sortino ratio alongside Sharpe?"**
Because Sharpe penalizes *all* volatility, including upside. For a positively-skewed or option-like strategy — one whose swings are mostly to the upside — Sharpe unfairly understates quality. Sortino divides only by downside deviation (volatility below a minimum acceptable return), so it matches what investors actually fear: losses. When a fund's Sortino is much higher than its Sharpe, that's the fingerprint of favourable skew, and the Sortino is the more relevant picture.

**C6. "Walk me through Brinson attribution."**
It decomposes active return — portfolio minus benchmark — into the decisions that produced it. Allocation asks: did over/underweighting segments help? You get credit only if the segment you overweighted beat the *total* benchmark. Selection asks: within each segment, did you pick better securities than the benchmark held? — measured at benchmark weights to isolate pure picking. Interaction is the joint term: overweighting a segment where you also picked well. The three sum exactly to total active return, and that reconciliation is the discipline — if they don't sum, the attribution is wrong. The split tells an allocator whether they're hiring an asset-allocation shop or a stock-picker.

**C7. "How much track record do you need to trust an Information Ratio?"**
The t-stat of the IR is roughly IR times the square root of the number of years. To be 95% confident it's real you want t ≈ 2, so you need about $(2/IR)^2$ years. An IR of 0.5 needs ~16 years; even a strong IR of 0.75 needs ~7. That's the uncomfortable truth about the industry: three-year track records, which drive most hiring and firing, are statistically indistinguishable from luck.

**C8. "First thing you check on any track record?"**
Benchmark validity and hygiene. Is the benchmark SAMURAI — specified in advance, style-appropriate, investable, and one the manager actually accepts? Then: are the returns net of fees, time-weighted, and long enough to be significant? A great-looking Sharpe against a soft or drifting benchmark, gross of fees, over two years, tells me nothing. Get those foundations right before interpreting a single ratio.

---

## Section D — MCQs (with reasoning)

**D1.** To compare two managers who each experienced different client cash flows, you should use:
(a) MWR (b) TWR (c) IRR (d) arithmetic mean.
**Answer: (b).** TWR strips out flow timing, isolating the managers' own decisions; MWR/IRR embed the flows the manager didn't control.

**D2.** MWR will be *below* TWR when:
(a) there are no cash flows (b) large inflows precede a strong period (c) large inflows precede a weak period (d) returns are constant.
**Answer: (c).** More money exposed to the loss drags the dollar-weighted return below the strategy return. Inflows before strong periods raise MWR above TWR; no flows or equal sub-period returns make them equal.

**D3.** The Sharpe and Treynor ratios differ only in:
(a) the numerator (b) the risk-free rate (c) the risk in the denominator (d) the benchmark used.
**Answer: (c).** Both use excess return $R_p - R_f$ in the numerator; Sharpe divides by total risk σ, Treynor by systematic risk β.

**D4.** Jensen's alpha measures return in excess of:
(a) the risk-free rate (b) the benchmark (c) the CAPM-required (beta-adjusted) return (d) the market return.
**Answer: (c).** $\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$ — the vertical distance from the Security Market Line, not a simple benchmark beat.

**D5.** In computing downside deviation for the Sortino ratio, you divide the sum of squared shortfalls by:
(a) the number of negative observations (b) the total number of observations $n$ (c) $n-1$ negatives (d) the number of positive observations.
**Answer: (b).** Only shortfalls below the MAR are squared, but the divisor is the *total* count $n$. Dividing by the number of negatives is the classic error.

**D6.** A large gap between a portfolio's Sharpe and Treynor rankings signals:
(a) high fees (b) poor diversification (c) negative alpha (d) survivorship bias.
**Answer: (b).** The gap means total risk (σ) and systematic risk (β) diverge, i.e. the portfolio carries meaningful idiosyncratic risk — it is under-diversified.

**D7.** In Brinson attribution, allocation effect for a segment is positive when you:
(a) overweight any segment with a positive return (b) overweight a segment that beat the *total* benchmark (c) pick better stocks in the segment (d) match the benchmark weight.
**Answer: (b).** $A_i = (w_p - w_b)(R_{b,i} - R_b)$ — credit comes from over/underweighting relative to how the segment did versus the *overall* benchmark, not its absolute return.

**D8.** The Information Ratio is defined as:
(a) $(R_p - R_f)/\sigma_p$ (b) $(R_p - R_f)/\beta_p$ (c) $(R_p - R_b)/\text{tracking error}$ (d) $R_f + S_p\sigma_m$.
**Answer: (c).** Active return over active risk (tracking error). (a) is Sharpe, (b) is Treynor, (d) is M².

**D9.** M² (Modigliani-squared) re-expresses which ratio as a percentage return?
(a) Treynor (b) Sharpe (c) Information ratio (d) Sortino.
**Answer: (b).** $M^2 = R_f + S_p\sigma_m$ restates the Sharpe ratio as the return the portfolio would earn if scaled to the market's volatility, making it directly comparable to the market return.

**D10.** A three-year Information Ratio of 0.8 is best described as:
(a) definitive proof of skill (b) statistically strong (c) statistically indistinguishable from luck (d) evidence of negative alpha.
**Answer: (c).** t ≈ $0.8 \times \sqrt3 = 1.39$, well below 2; roughly $(2/0.8)^2 ≈ 6$ years are needed for 95% confidence. Short records prove little.

**D11.** The geometric mean of a return series is:
(a) always ≥ the arithmetic mean (b) always ≤ the arithmetic mean (c) equal to it (d) unrelated.
**Answer: (b).** Geometric ≤ arithmetic always, with the gap ≈ $\sigma^2/2$, widening with volatility. It is the true compounded growth rate.

**D12.** The identity $\alpha = \beta_p(T_p - T_m)$ serves primarily as:
(a) a definition of Sharpe (b) a self-check linking Jensen's alpha and Treynor (c) the M² formula (d) the Sortino numerator.
**Answer: (b).** Alpha equals beta times the Treynor advantage over the market — a consistency check confirming both live in systematic-risk (beta) space.
