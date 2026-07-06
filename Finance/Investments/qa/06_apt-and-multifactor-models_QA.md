# Q&A — APT and Multifactor Models

> Scope: Investments — Chapter 06 (APT and Multifactor Models). Every question is followed by a full model answer. All rates are annual and in percent unless stated. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** numerical (full step-by-step, reconciling) · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one line

$$E(R_i) = R_f + \sum_{k=1}^{K}\beta_{i,k}\lambda_k$$

**One-line statement:** Expected return equals the risk-free rate plus, for each systematic factor, your exposure (β) times that factor's price of risk (λ); CAPM is just the one-factor case, and no-arbitrage — not a market portfolio — is what forces the pricing to be linear.

---

## Section A — Concept Check

**A1. What single assumption does APT rest on, and why does that make it more general than CAPM?**
The **no-arbitrage** condition (no free lunch / law of one price). If a portfolio costs nothing to build and carries no factor risk, it must earn zero. That is a far weaker assumption than CAPM's requirement that *every* investor is a mean-variance optimiser holding the true market portfolio. Because APT needs only a factor structure plus enough assets to diversify, it does not need the (unobservable) market portfolio, homogeneous expectations, normal returns, or single-period preferences. Hence it is more robust and more general — CAPM is a special case.

**A2. Distinguish a factor loading (β) from a factor risk premium (λ).**
β is a property of the **asset** — how much the asset's return moves per one-unit shock to the factor (estimated by regression). λ is a property of the **market** — the expected excess return earned per unit of exposure to that factor (the return of the factor-mimicking portfolio over R_f). Expected return needs *both*, multiplied together: exposure × price of risk.

**A3. Why is only systematic (factor) risk priced, while idiosyncratic risk εᵢ is not?**
εᵢ is firm-specific and uncorrelated across firms, so it washes out in a well-diversified portfolio — you can eliminate it for free by diversifying. The market pays you only for risk you *cannot* escape. Factor risk is common to many assets (they all move together), so it survives diversification and therefore commands a premium.

**A4. Does APT tell you what the factors are?**
No. This is its defining feature. APT proves pricing *must* be linear in *some* set of K factors, but is silent on their identity. Finding the factors is an empirical exercise — that is where Chen-Roll-Ross (macro factors) and Fama-French (characteristic factors) come in. This is both APT's strength (generality) and its weakness (not directly testable without specifying factors).

**A5. Name the Fama-French three factors and say what each long-short portfolio holds.**
(1) **Market (R_m − R_f)** — excess return on the market. (2) **SMB, Small Minus Big** — long small-cap stocks, short large-caps (size premium). (3) **HML, High Minus Low** — long high book-to-market (value) stocks, short low book-to-market (growth) stocks (value premium).

**A6. What two factors did the 2015 five-factor model add, and what motivated them?**
**RMW (Robust Minus Weak)** — long high-profitability firms, short low-profitability — and **CMA (Conservative Minus Aggressive)** — long firms that invest conservatively (low asset growth), short aggressive investors. They were motivated by the dividend discount model: holding valuation fixed, higher profitability and more disciplined investment imply higher expected returns.

**A7. Which factor is *not* in the Fama-French models but defines the Carhart four-factor model, and why do Fama-French exclude it?**
**Momentum — WML / UMD (Winners Minus Losers)**, long past-12-month winners, short past losers. Fama and French exclude it because it lacks a clean risk-based story and has high turnover, but Carhart (1997) added it, and the four-factor model (Mkt, SMB, HML, WML) is the industry standard for mutual-fund performance evaluation.

**A8. In a multifactor world, what is alpha?**
Alpha is the part of return the factor model *cannot* explain: α = (Rᵢ − R_f) − Σ βᵢ,ₖ λₖ. It is the measure of genuine skill or mispricing — but only *relative to the factors you chose*. An omitted true factor leaks its premium into alpha and masquerades as skill.

**A9. Can a factor risk premium λ be negative? Give the intuition.**
Yes. A factor that pays off in *bad* states of the world is a hedge — investors value the insurance and accept a *lower* expected return to hold assets exposed to it. Classic example: an inflation-surprise factor. Assets that rise when inflation surprises upward protect you, so they can carry a negative premium.

**A10. Why can adding more factors be dangerous rather than simply "better"?**
More factors mechanically raise R², but risk **data mining** — the "factor zoo" of 300+ published factors, most of which fail out-of-sample. A legitimate factor needs (i) an economic rationale, (ii) robustness across time and markets, and (iii) low correlation with existing factors.

**A11. How does APT nest CAPM geometrically?**
CAPM's Security Market Line is a *line* in (β, expected-return) space. A multifactor model generalises it into a **hyperplane** in K-dimensional factor-exposure space. Set K = 1 with the market as the factor and λ = E(R_m) − R_f, and the hyperplane collapses back to the SML.

**A12. Why did HML become partly redundant in the five-factor model?**
Because RMW (profitability) and CMA (investment) are correlated with the value characteristic and absorb much of the value premium. In US data, once RMW and CMA are included, HML adds little explanatory power — an active, unsettled debate.

**A13. Distinguish macroeconomic factors from fundamental (characteristic) factors.**
**Macro factors** (Chen-Roll-Ross) are *surprises* in observable economic variables — industrial-production growth, unexpected inflation, term spread, default spread. Economically interpretable but noisy to estimate. **Fundamental factors** (Fama-French, BARRA) are long-short portfolios sorted on firm characteristics (size, value, profitability); their returns are directly observable and stable, which is why industry practice is dominated by them.

---

## Section B — Numerical Problems

**B1. Two-factor APT pricing.** A two-factor APT holds. R_f = 5%; λ₁ (industrial-production surprise) = 6%; λ₂ (inflation surprise) = −2%. Stock A has β₁ = 1.2, β₂ = 0.5. Find its required return.

**Solution.**
$$E(R_A) = 5\% + (1.2)(6\%) + (0.5)(-2\%)$$
Step by step: factor-1 reward = 1.2 × 6% = **7.2%**; factor-2 reward = 0.5 × (−2%) = **−1.0%**.
$$E(R_A) = 5\% + 7.2\% - 1.0\% = \mathbf{11.2\%}$$
The negative λ₂ *reduces* the required return: exposure to a hedging factor is rewarded with less return, not more.

**B2. Arbitrage from mispricing.** Continue B1. Stock A actually offers an expected return of 13%. Is it mis-priced? Construct the arbitrage and state the profit.

**Solution.** Required = 11.2% (B1); offered = 13%. Since 13% > 11.2%, A is **underpriced** — a positive alpha of 13% − 11.2% = **+1.8%**.
Arbitrage: build a replicating portfolio from R_f and the two factor-mimicking portfolios with the *same* exposures (β₁ = 1.2, β₂ = 0.5); it fairly yields 11.2%. Go **long Stock A** (+13%) and **short the replicating portfolio** (−11.2%).
- Net cost = 0 (short funds the long).
- Net factor exposure: β₁ = 1.2 − 1.2 = 0; β₂ = 0.5 − 0.5 = 0. Riskless.
- Net return = 13% − 11.2% = **+1.8% riskless**.
Arbitrageurs scale this up, bidding A's price up until its expected return falls to 11.2% and the alpha vanishes. This is the enforcement mechanism behind the APT equation.

**B3. Fama-French three-factor return, reconciled against CAPM.** Small-cap value "Stock V": β = 1.10, s = 0.80, h = 0.60. R_f = 4%; λ_Mkt = 5.5%; λ_SMB = 2.5%; λ_HML = 3.5%. Find the FF expected return and the CAPM expected return, and reconcile.

**Solution — Fama-French:**
$$E(R_V) = 4\% + (1.10)(5.5\%) + (0.80)(2.5\%) + (0.60)(3.5\%)$$
Contributions: market 1.10 × 5.5% = 6.05%; size 0.80 × 2.5% = 2.00%; value 0.60 × 3.5% = 2.10%.
$$E(R_V) = 4\% + 6.05\% + 2.00\% + 2.10\% = \mathbf{14.15\%}$$
**CAPM (same market beta):**
$$E(R_V)_{CAPM} = 4\% + (1.10)(5.5\%) = \mathbf{10.05\%}$$
**Reconciliation.** The gap = 14.15% − 10.05% = **4.10%**, exactly the sum of the size (2.00%) and value (2.10%) rewards CAPM is blind to. If V actually earns 14.15%, a CAPM regression records a fake **+4.10% alpha** ("genius stock-picking"), whereas Fama-French shows **α = 0** — the return was just harvested size and value premia. The CAPM "alpha" *is* the FF "factor return."

**B4. Performance attribution (Carhart four-factor).** A fund returns 18%; R_f = 4%. Loadings and realised factor premia: Market β = 1.00 (8%), SMB = 0.50 (3%), HML = 0.40 (2%), WML = 0.60 (4%). Decompose the excess return and find alpha.

**Solution.** Excess return = 18% − 4% = 14%.
| Factor | Loading | Realised premium | Contribution |
|---|---|---|---|
| Market | 1.00 | 8% | 8.0% |
| SMB | 0.50 | 3% | 1.5% |
| HML | 0.40 | 2% | 0.8% |
| WML | 0.60 | 4% | 2.4% |
| **Sum** | | | **12.7%** |

Alpha = 14% − 12.7% = **+1.3%**.
Interpretation: of the 14% excess return, 12.7% is replicable factor beta (a full market position plus small, value, and momentum tilts an investor could buy cheaply); only **1.3% is genuine skill**. This is precisely the check an allocator runs before paying "2 and 20."

**B5. Detecting closet indexing / negative alpha.** Fund X returns 11%; R_f = 3%. A three-factor regression gives β = 0.95 (λ_Mkt = 7%), s = 0.20 (λ_SMB = 2%), h = 0.10 (λ_HML = 3%). Compute the factor-implied return and the alpha, and comment.

**Solution.** Factor contributions to *excess* return: 0.95 × 7% = 6.65%; 0.20 × 2% = 0.40%; 0.10 × 3% = 0.30%. Sum = **7.35%**. Factor-implied total return = R_f + 7.35% = 3% + 7.35% = **10.35%**.
Alpha = actual − implied = 11% − 10.35% = **+0.65%** (small positive). But note the loadings are close to the market (β ≈ 0.95, tiny size/value tilts): the fund is *almost* a levered index fund, so the 0.65% alpha is thin and, after typical active fees of ~1%, the *net* alpha is **negative**. Multifactor regression exposes "closet indexing" — near-index exposure sold at active prices.

**B6. Solving for a factor premium by no-arbitrage.** Two well-diversified portfolios load on one factor. Portfolio P: β = 1.5, E(R) = 17%. Portfolio Q: β = 0.5, E(R) = 9%. Find R_f and the factor premium λ, then price a portfolio with β = 1.0.

**Solution.** APT: E(R) = R_f + βλ. Two equations:
- 17% = R_f + 1.5λ
- 9% = R_f + 0.5λ

Subtract: 8% = 1.0λ → **λ = 8%**. Back-substitute into the second: 9% = R_f + 0.5(8%) = R_f + 4% → **R_f = 5%**.
A β = 1.0 portfolio should price at E(R) = 5% + 1.0 × 8% = **13%**. If any β = 1 portfolio traded away from 13%, you could arbitrage it against a mix of P and Q with net β = 1.

---

## Section C — Interview-Style Questions

**C1. "How does APT differ from CAPM — and what does APT give up in exchange for its generality?"**
APT allows *many* systematic factors and rests on **no-arbitrage** rather than on everyone holding the mean-variance-efficient market portfolio. Consequently it does not require the unobservable market portfolio, so it sidesteps Roll's Critique, and it needs only a handful of arbitrageurs rather than universally rational optimisers. CAPM is simply the one-factor special case. The trade-off: APT does *not* tell you what the factors are or how many — you must find them empirically, and the theory is hard to test without committing to a factor set. So APT buys robustness at the cost of specificity.

**C2. "A fund returned 20% last year. Was the manager skilled?"**
You cannot say from the raw number — decompose it. Run a multifactor regression (Carhart or five-factor) of the fund's excess returns on the factors. Split the 20% into (a) factor contributions — the return explained by the fund's market, size, value, momentum, profitability tilts, all of which an investor can buy cheaply through index/ETF products — and (b) alpha, the residual. If most of the 20% is levered market plus small/value/momentum exposure, there is little skill; it is replicable **smart beta**. Only the alpha, and only if it is statistically significant and survives fees, reflects genuine skill.

**C3. "Explain the no-arbitrage argument that produces the APT equation."**
Assume returns follow a factor model: Rᵢ = E(Rᵢ) + Σ βᵢ,ₖ Fₖ + εᵢ, where the F's are mean-zero factor shocks and εᵢ is diversifiable noise. Form a portfolio that (i) costs nothing (longs funded by shorts), (ii) has zero exposure to every factor (all β_p = 0), and (iii) is well-diversified so ε ≈ 0. Such a portfolio has no risk and no capital at stake, so by the law of one price it must earn zero. If it earned anything positive, arbitrageurs would scale it infinitely — free money. Imposing "zero return for zero-cost, zero-risk portfolios" across all portfolios forces expected returns to be a linear function of the betas: E(Rᵢ) = R_f + Σ βᵢ,ₖ λₖ. No behavioural or market-portfolio assumptions are needed.

**C4. "Why do the size and value premia exist — risk or mispricing?"**
Two camps. **Risk-based (Fama-French):** small and value firms are more distressed and their earnings are more sensitive to bad economic times, so their extra return is fair compensation for bearing that systematic risk. **Behavioural:** investors over-extrapolate — they over-price glamorous growth stocks and under-price dull value stocks — so the premium is a slowly-correcting mispricing. The debate is unsettled, but the factors have worked under either interpretation. Crucially, if they are risk premia they can, and do, disappear for long stretches (value underperformed roughly 2007–2020) — factor investing carries factor risk, which is *why* it pays on average.

**C5. "When would you use a Fama-French model instead of CAPM to estimate a firm's cost of equity?"**
When the firm has strong size or value characteristics that CAPM's single beta misses. CAPM systematically *understates* the required return for small-cap and value (high book-to-market) firms because it ignores the priced size and value risks they carry. Using a three- or five-factor model gives a discount rate that reflects those exposures, producing a more accurate valuation. The cost is added estimation error from more betas and the need for factor-premium inputs.

**C6. "What is the single biggest practical use of multifactor models in asset management?"**
Separating **true alpha from replicable beta** ("smart beta"). Before a multifactor lens, a manager tilting toward small and value stocks looked like a genius under CAPM (big positive alpha). A factor regression reveals that "alpha" was just cheap, rules-based factor exposure. This drives manager due diligence, fee negotiation, closet-indexing detection, and the entire factor-ETF industry — packaging what used to be alpha as low-cost beta.

---

## Section D — MCQs with Reasoning

**D1. APT differs from CAPM primarily because APT —**
A) requires the market portfolio  B) assumes normally distributed returns  C) permits multiple priced factors and rests on no-arbitrage  D) ignores systematic risk
**Answer: C.** APT allows K factors and is built on no-arbitrage; A and B are (partly) CAPM's requirements, and D is false — APT prices systematic risk, just across several factors.

**D2. In E(Rᵢ) = R_f + Σ βₖλₖ, the term λₖ represents —**
A) the asset's sensitivity to factor k  B) the expected excess return per unit of exposure to factor k  C) idiosyncratic risk  D) the risk-free rate
**Answer: B.** λ is the factor's *price of risk* (a market property). A describes β (an asset property); C and D are unrelated.

**D3. A factor risk premium λ can be negative when the factor —**
A) has a high beta  B) pays off in bad states of the world (acts as a hedge)  C) is diversifiable  D) is the market factor
**Answer: B.** Assets that pay off in bad states provide insurance; investors accept lower returns to hold them, so the premium is negative. A confuses β with λ; C describes unpriced risk; D (the market) carries a positive premium.

**D4. In the Fama-French three-factor model, HML is long —**
A) large-cap, short small-cap  B) high book-to-market (value), short low book-to-market (growth)  C) winners, short losers  D) high-profitability, short low-profitability
**Answer: B.** HML = High Minus Low book-to-market = value minus growth. A is (reversed) size, C is momentum, D is RMW.

**D5. The Carhart four-factor model adds which factor to the Fama-French three?**
A) RMW  B) CMA  C) WML (momentum)  D) Term spread
**Answer: C.** Carhart adds momentum (Winners Minus Losers). RMW and CMA belong to the five-factor model; term spread is a Chen-Roll-Ross macro factor.

**D6. A fund's entire excess return is explained by its factor loadings (alpha = 0). This means —**
A) the manager has strong skill  B) the return was replicable factor exposure, i.e. smart beta  C) the fund took no risk  D) the model is misspecified
**Answer: B.** Zero alpha means the return came entirely from bearing priced factor risks an investor could buy cheaply — no skill beyond beta. It does not imply zero risk (C) or, by itself, misspecification (D).

**D7. Idiosyncratic risk εᵢ is not priced because it —**
A) is larger than systematic risk  B) can be diversified away for free  C) has a negative premium  D) equals the risk-free rate
**Answer: B.** Firm-specific risk vanishes in a diversified portfolio, so the market pays nothing to bear it — only non-diversifiable factor risk earns a premium.

**D8. The main danger of building models with many factors is —**
A) R² becomes too low  B) data mining / the factor zoo — factors that fail out-of-sample  C) alpha becomes impossible to compute  D) betas can no longer be estimated
**Answer: B.** Adding factors always *raises* in-sample R² (so A is backwards), but risks overfitting spurious factors that do not survive out-of-sample. Alpha and betas remain computable.

**D9. CAPM is best described within APT as —**
A) a contradiction of APT  B) the special case where K = 1 and the single factor is the market  C) a five-factor model  D) a model with no factors
**Answer: B.** Set one factor (the market) with λ = E(R_m) − R_f and the APT equation reduces to the CAPM/SML.

**D10. HML is often found to be "redundant" in the five-factor model because —**
A) value stocks no longer exist  B) RMW and CMA are correlated with the value characteristic and absorb its premium  C) HML has a negative beta  D) the market factor replaces it
**Answer: B.** Profitability (RMW) and investment (CMA) overlap with value, so in US data they soak up most of HML's explanatory power.

---

*End of Q&A — APT and Multifactor Models.*
