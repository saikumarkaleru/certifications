# Q&A — The Capital Asset Pricing Model (CAPM)

Practice bank for Chapter 05. Work each question before reading the answer. All figures are in percentages unless stated; betas are unit-free.

---

## Section A — Concept Checks

**A1. In one sentence, what does CAPM claim?**
The expected (required) return on any asset equals the risk-free rate plus its beta times the market risk premium — i.e. investors are paid only for systematic risk, priced at the market's risk premium per unit of beta: $E(R_i) = R_f + \beta_i[E(R_m) - R_f]$.

**A2. Why does the market refuse to reward unsystematic risk?**
Because unsystematic (firm-specific) risk can be diversified away for free. A diversified investor bears none of it, so bearing it is a *choice*, not a service to the market. Only systematic risk survives diversification, so only it earns a premium.

**A3. Define beta two different ways.**
Statistically, $\beta_i = \dfrac{\text{Cov}(R_i, R_m)}{\sigma_m^2}$. Equivalently, $\beta_i = \rho_{i,m}\dfrac{\sigma_i}{\sigma_m}$. Intuitively, beta answers: if the market moves 1%, how much does the stock move on average?

**A4. Why is covariance with the market — not the stock's own variance — the relevant risk?**
When you already hold the market portfolio, the marginal risk a new stock adds is proportional to how it co-moves with your existing holdings, i.e. its covariance with the market, not its standalone variance. Its own variance is mostly diversified away.

**A5. Distinguish the CML from the SML on four dimensions.**
X-axis: CML uses total risk $\sigma$; SML uses systematic risk $\beta$. Scope: CML prices *efficient portfolios only*; SML prices *all* assets and portfolios. Slope: CML slope is the market Sharpe ratio $\frac{E(R_m)-R_f}{\sigma_m}$; SML slope is the ERP $E(R_m)-R_f$. Equilibrium: every asset lies on the SML; only efficient portfolios lie on the CML.

**A6. Why must the risk–return relationship be linear in beta?**
No-arbitrage. If two assets shared the same beta but different expected returns, investors would buy the higher and short the lower, earning return with no extra market risk. Prices adjust until reward per unit of beta is identical for all assets — a straight line through $(0, R_f)$ and $(1, E(R_m))$.

**A7. What does a point above the SML mean, and what action follows?**
Positive alpha → the asset is expected to beat its fair return → it is undervalued → buy. Its price should rise until it falls back onto the line.

**A8. Give the sign and meaning of a negative beta.**
A negative-beta asset moves opposite to the market (e.g. certain hedges/gold at times). By CAPM its required return is *below* the risk-free rate, because it reduces portfolio risk — investors pay for that insurance by accepting a lower return.

**A9. Why is portfolio beta so convenient?**
It is a simple value-weighted average: $\beta_p = \sum w_i \beta_i$. Beta is linear and additive, so you can aggregate portfolio systematic risk directly without re-estimating covariances.

**A10. State CAPM's key assumptions in brief.**
Rational mean-variance investors; homogeneous expectations; single-period horizon; unlimited risk-free borrowing and lending at one rate; frictionless markets (no taxes/costs, divisible assets); all assets tradable, markets in equilibrium, investors are price-takers; free simultaneous information.

**A11. Why does CAPM survive despite failing statistical tests?**
Friedman's defence: a model is judged by the usefulness of its predictions, not the literal truth of its assumptions. CAPM gives a tractable, defensible discount rate and a common language for risk, and no successor is decisively better in practice.

**A12. What is alpha, precisely?**
The gap between the return you *forecast* and the return CAPM says is *fair*: $\alpha_i = E(R_i)^{\text{forecast}} - [R_f + \beta_i(E(R_m)-R_f)]$. It measures mispricing or manager skill; in an efficient market it averages zero.

---

## Section B — Numerical Problems (full working)

**B1. Required return and alpha.**
Given $R_f = 6\%$, $E(R_m) = 13\%$, $\beta = 1.4$; your forecast return is 17%. Find the fair return and alpha.

- ERP $= 13 - 6 = 7\%$.
- Fair return $= 6 + 1.4(7) = 6 + 9.8 = 15.8\%$.
- Alpha $= 17 - 15.8 = +1.2\%$.

**Interpretation:** positive alpha → plots above the SML → undervalued → buy.
**Reconcile:** if the forecast were exactly 15.8%, alpha = 0 (on the line); a 14% forecast gives alpha $= -1.8\%$ → overvalued → sell. Internally consistent.

**B2. Portfolio beta and return — two routes.**
$R_f = 5\%$, $E(R_m) = 12\%$. Portfolio: A (40%, β 0.80), B (35%, β 1.20), C (25%, β 1.60).

*Route 1 — beta first:*
$\beta_p = 0.40(0.80) + 0.35(1.20) + 0.25(1.60) = 0.320 + 0.420 + 0.400 = 1.14$.
$E(R_p) = 5 + 1.14(12 - 5) = 5 + 1.14(7) = 5 + 7.98 = 12.98\%$.

*Route 2 — returns first:*
A: $5 + 0.80(7) = 10.60\%$; B: $5 + 1.20(7) = 13.40\%$; C: $5 + 1.60(7) = 16.20\%$.
Weighted: $0.40(10.60) + 0.35(13.40) + 0.25(16.20) = 4.24 + 4.69 + 4.05 = 12.98\%$. ✓

**Reconcile:** both routes give 12.98% because CAPM is linear — averaging betas then applying CAPM equals applying CAPM then averaging returns.

**B3. Unlever and relever beta for a valuation.**
PeerCo: equity beta 1.30, D/E 0.60, tax 30%. Target: D/E 0.25, tax 30%. $R_f = 7\%$, ERP 6%.

- Unlever: $\beta_U = \dfrac{1.30}{1 + (1-0.30)(0.60)} = \dfrac{1.30}{1.42} = 0.9155$.
- Relever at target: $\beta_L = 0.9155[1 + (1-0.30)(0.25)] = 0.9155(1.175) = 1.0757$.
- Cost of equity: $k_e = 7 + 1.0757(6) = 7 + 6.45 = 13.45\%$.

**Reconcile:** the lazy shortcut (use PeerCo's raw 1.30) gives $k_e = 7 + 1.30(6) = 14.8\%$ — over-discounting and undervaluing the target, which carries less debt. Unlevering corrects for the different capital structures.

**B4. Solve CAPM for the ERP.**
A stock's fair return is 14%, $R_f = 6\%$, $\beta = 1.6$. Find the implied ERP and market return.
$14 = 6 + 1.6 \times \text{ERP} \Rightarrow \text{ERP} = \dfrac{8}{1.6} = 5\%$. Then $E(R_m) = 6 + 5 = 11\%$.
**Reconcile:** plug back: $6 + 1.6(5) = 6 + 8 = 14\%$. ✓

**B5. Solve CAPM for beta.**
$R_f = 4\%$, $E(R_m) = 11\%$; a stock's required return is 15.1%. Find beta.
$15.1 = 4 + \beta(11 - 4) \Rightarrow \beta = \dfrac{11.1}{7} = 1.586$.
**Reconcile:** $4 + 1.586(7) = 4 + 11.1 = 15.1\%$. ✓ A beta above 1 is consistent with a required return above the market's 11%.

**B6. Beta from correlation and volatilities.**
$\rho_{i,m} = 0.6$, $\sigma_i = 30\%$, $\sigma_m = 18\%$. Find beta, then required return with $R_f = 5\%$, $E(R_m) = 12\%$.
$\beta = 0.6 \times \dfrac{30}{18} = 0.6 \times 1.667 = 1.0$. $E(R) = 5 + 1.0(7) = 12\%$.
**Reconcile:** despite the stock's much higher standalone volatility (30% vs 18%), its modest correlation pulls beta to exactly 1, so it earns the market return. This shows why total risk (σ) is the wrong yardstick — only the co-moving part is priced.

**B7. Treynor ranking (CAPM-family).**
$R_f = 5\%$. Fund X: return 14%, β 1.30. Fund Y: return 12%, β 0.80.
- Treynor X $= (14 - 5)/1.30 = 9/1.30 = 6.92$.
- Treynor Y $= (12 - 5)/0.80 = 7/0.80 = 8.75$.

**Y wins** — more reward per unit of systematic risk despite the lower headline return.
**Reconcile:** X's higher 14% is largely compensation for taking more market risk (β 1.30), not skill. Treynor uses beta because it assumes a diversified investor; Sharpe (using σ) would be the right lens for an undiversified investor.

**B8. Jensen's alpha for a fund.**
$R_f = 6\%$, $E(R_m) = 13\%$. A fund realised 15% with β 1.1.
Fair return $= 6 + 1.1(7) = 13.7\%$. Jensen's alpha $= 15 - 13.7 = +1.3\%$.
**Reconcile:** positive alpha means the fund beat its risk-adjusted benchmark by 1.3 points — genuine outperformance after accounting for the market risk it took.

**B9. Decomposing total risk.**
A stock has β 1.2, $\sigma_m = 20\%$, and total variance $\sigma_i^2 = 0.09$ (σ = 30%). Find systematic and unsystematic variance.
Systematic $= \beta^2\sigma_m^2 = 1.2^2 (0.20)^2 = 1.44 \times 0.04 = 0.0576$.
Unsystematic $= 0.09 - 0.0576 = 0.0324$.
**Reconcile:** systematic is 64% of total variance ($0.0576/0.09$), diversifiable is 36%. Only the 0.0576 slice is priced by the SML; the rest earns no premium.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through CAPM."**
CAPM says the required return on an asset is the risk-free rate plus beta times the market risk premium: $R_f + \beta(E(R_m) - R_f)$. $R_f$ compensates you for waiting; the second term compensates you for market risk. Beta measures systematic risk — sensitivity to the market. The model's core claim is that only systematic risk is priced, because idiosyncratic risk is diversifiable and bearing it earns nothing. It emerges from Markowitz portfolio theory: when everyone holds the tangency portfolio, in equilibrium that portfolio *is* the market, and no-arbitrage forces expected return to be linear in beta — the Security Market Line.

**C2. "What's the difference between the CML and the SML?"**
The CML plots expected return against total risk (σ) and applies only to efficient portfolios — combinations of the risk-free asset and the market. Its slope is the market Sharpe ratio. The SML plots expected return against beta and applies to *every* asset and portfolio, efficient or not. Its slope is the equity risk premium. A key error is plotting individual stocks on the CML — they belong on the SML because their relevant risk is systematic, not total.

**C3. "A stock plots above the SML. What do you do and why?"**
Above the line means its expected return exceeds the CAPM-fair return — positive alpha, so it is undervalued. I'd buy it. As other investors recognise the mispricing and buy, the price rises, expected return falls, and the stock moves back down onto the line. In an efficient market this alpha is arbitraged away, which is exactly why CAPM is the null hypothesis for judging active skill.

**C4. "How do you estimate the cost of equity for a private company?"**
The company has no traded beta, so I take a listed comparable, unlever its equity beta to strip out its financial leverage (getting the asset/business-risk beta), then relever at the target's own D/E using the Hamada relation $\beta_L = \beta_U[1 + (1-t)\frac{D}{E}]$. Plug that target beta into CAPM with an appropriate $R_f$ and ERP. This isolates pure business risk and then adds back the target's specific leverage, avoiding the error of importing the peer's capital structure.

**C5. "What's wrong with CAPM?"**
Several things. Roll's critique: the true market portfolio (all global assets including human capital) is unobservable, so any test is a joint test of CAPM and the proxy's efficiency — arguably it's untestable. Empirically the SML is too flat: low-beta stocks earn more and high-beta stocks less than predicted (the low-beta anomaly). Fama–French showed size and value explain returns beta cannot, spawning multifactor models. Beta itself is unstable and noisy, depending on window, frequency, and index. And the assumptions — one borrowing rate, no frictions, homogeneous expectations, single period — are unrealistic. Still, I'd use it for cost of equity and sanity-check with a multifactor model.

**C6. "Why doesn't the market reward unsystematic risk?"**
Because it can be eliminated for free through diversification. If the market paid a premium for diversifiable risk, an arbitrageur could build a diversified portfolio that captures the premium while the risk itself cancels out — a free lunch. Competition removes it, so in equilibrium only non-diversifiable (systematic) risk carries a premium.

**C7. "Two stocks have the same standard deviation but different betas. Which has the higher required return?"**
The one with the higher beta. CAPM prices systematic risk, not total risk. Equal σ means equal total volatility, but the higher-beta stock co-moves more with the market — it contributes more non-diversifiable risk to a diversified portfolio — so it commands a higher required return. The lower-beta stock's volatility is more idiosyncratic and largely diversified away.

**C8. "What's a reasonable equity risk premium for India, and how would you estimate it?"**
Commonly discussed around 6–8%, higher than developed markets' roughly 4–5% because of greater country and growth risk. I'd estimate it two ways: a historical average of realised (market − risk-free) returns over a long window, and a forward-looking implied premium backed out of current index levels via a dividend-discount or earnings model. I'd blend them, sanity-check against surveys, and always state my source rather than quoting a single textbook number.

---

## Section D — MCQs (with reasoning)

**D1.** The slope of the Security Market Line equals:
(a) the market Sharpe ratio (b) $E(R_m) - R_f$ (c) $\sigma_m$ (d) beta
**Answer: (b).** The SML's slope is the equity risk premium $E(R_m) - R_f$. The Sharpe ratio $\frac{E(R_m)-R_f}{\sigma_m}$ is the slope of the *CML*, not the SML.

**D2.** A stock with beta 0 has a CAPM required return equal to:
(a) 0 (b) $E(R_m)$ (c) $R_f$ (d) the ERP
**Answer: (c).** At $\beta = 0$, $E(R) = R_f + 0 \times \text{ERP} = R_f$. Zero systematic risk earns only the risk-free rate.

**D3.** Which risk measure belongs on the x-axis of the SML?
(a) standard deviation (b) variance (c) beta (d) covariance
**Answer: (c).** The SML prices assets by systematic risk, measured by beta. Standard deviation (total risk) is the CML's axis.

**D4.** Increasing a firm's financial leverage, holding business risk constant, will:
(a) lower its equity beta (b) raise its equity beta (c) leave equity beta unchanged (d) lower its asset beta
**Answer: (b).** By Hamada, $\beta_L = \beta_U[1 + (1-t)\frac{D}{E}]$ — more debt (higher D/E) raises the multiplier and thus the equity beta and cost of equity. Asset (unlevered) beta reflects business risk and is unaffected.

**D5.** A stock plotting *below* the SML is:
(a) undervalued, buy (b) fairly priced (c) overvalued, sell (d) risk-free
**Answer: (c).** Below the line means the expected return is less than the fair return — negative alpha — so it is overvalued; sell or short.

**D6.** Portfolio beta is computed as:
(a) the simple average of component betas (b) the value-weighted average of component betas (c) the square root of weighted variances (d) covariance with the market
**Answer: (b).** $\beta_p = \sum w_i \beta_i$, a value-weighted average — beta is linear and additive. A simple average only coincides when weights are equal.

**D7.** Roll's critique argues that CAPM is problematic because:
(a) beta is always negative (b) the true market portfolio is unobservable (c) the risk-free rate is unknown (d) alpha is always positive
**Answer: (b).** The true market portfolio includes all assets globally (including human capital) and cannot be observed, so any empirical test is a joint test of CAPM and whether the chosen proxy is efficient.

**D8.** The Treynor ratio measures reward per unit of:
(a) total risk (b) unsystematic risk (c) systematic risk (beta) (d) variance
**Answer: (c).** Treynor $= (R_p - R_f)/\beta_p$ — excess return per unit of systematic risk. Sharpe uses σ (total risk) instead and suits an undiversified investor.

**D9.** Under CAPM, an asset with negative beta should have a required return that is:
(a) above the market return (b) equal to $R_f$ (c) below the risk-free rate (d) always zero
**Answer: (c).** A negative beta reduces portfolio risk (acts as a hedge), so investors accept a required return below $R_f$: $R_f + (\text{negative})\times\text{ERP} < R_f$.

**D10.** Which of the following would earn NO risk premium under CAPM?
(a) systematic risk (b) market risk (c) unsystematic (firm-specific) risk (d) beta risk
**Answer: (c).** Firm-specific risk is diversifiable, so the market pays nothing for it. Options (a), (b), and (d) all describe the same priced, non-diversifiable risk.

---

*End of Chapter 05 Q&A. Drill Section B until CAPM rearrangement for any of its four inputs — $R_f$, $E(R_m)$, $\beta$, $E(R_i)$ — is reflexive, and be able to unlever/relever beta on demand.*
