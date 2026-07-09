# Q&A — Cost of Equity & CAPM

A mix of **theory** (with model answers and interview phrasing) and **numerical problems** (fully solved, numbers self-verified). Work each problem before reading the solution.

---

## Theory

### Q1. What is the cost of equity, and why can't you just read it off a document the way you read the cost of debt?

**Model answer.** The cost of equity is the return equity investors require to hold a company's shares — the discount rate for equity cash flows and the equity component of WACC. Unlike debt, equity has **no contract**: no coupon, no maturity, no promised payment. So the required return isn't observable; it must be **inferred** from a model of how investors price risk (CAPM, or the dividend growth model as a cross-check).

**How to say it in an interview.** "Debt's cost is contractual — you read the yield. Equity promises nothing, so its cost is an inferred required return, not an observed one. That's why we need CAPM."

---

### Q2. Why does CAPM price only systematic risk and ignore firm-specific risk?

**Model answer.** Firm-specific (idiosyncratic) risk can be **diversified away for free** — in a large portfolio, independent shocks cancel and a stock's standalone volatility washes out; only its **covariance with the market** survives. Since a diversified investor bears no idiosyncratic risk, competition means the market won't pay a premium for it. Only non-diversifiable systematic risk — measured by beta — earns a return.

**How to say it.** "You're compensated for risk you can't escape, not risk you chose not to escape by failing to diversify."

---

### Q3. Explain each of the three CAPM inputs and one judgment call for each.

**Model answer.**
- **Risk-free rate** — reward for time value; use the 10-year government bond in the cash-flow currency. *Judgment:* strip sovereign default spread in emerging markets.
- **Beta** — sensitivity to market moves (systematic risk). *Judgment:* single-stock regression betas are noisy; prefer bottom-up/adjusted betas.
- **ERP** — extra return for holding equities over the risk-free asset. *Judgment:* historical vs implied, and arithmetic vs geometric mean (arithmetic for a one-period discount rate).

---

### Q4. Why does financial leverage increase the equity beta?

**Model answer.** Debt is a fixed claim. When operating cash flows swing with the economy, equity holders absorb the entire swing *after* fixed interest, so equity returns become more volatile and more correlated with the market cycle. Leverage amplifies business risk into equity (financial) risk. Hamada captures this: $\beta_L = \beta_U[1+(1-t)D/E]$; the $(1-t)$ softens the effect because the interest tax shield offsets part of the amplification.

**How to say it.** "The asset beta is pure business risk; leverage gears it up into the equity beta."

---

### Q5. How do you estimate beta for a private company with no traded shares?

**Model answer.** **Bottom-up beta**: (1) pick listed comps in the same business; (2) get each comp's levered beta; (3) un-lever each with Hamada to strip financing, giving asset betas; (4) average (or take the median) to cut estimation noise; (5) re-lever at the private firm's target D/E and tax rate; (6) plug into CAPM. This also handles divisions of a conglomerate and firms planning a leverage change.

---

### Q6. What's the difference between the SML and the CML?

**Model answer.** The **SML** plots expected return against **systematic risk (beta)** and prices **every** asset — its slope is the ERP, intercept the risk-free rate. The **CML** plots expected return against **total risk (σ)** and applies only to **efficient portfolios** (combinations of the risk-free asset and the market). Individual inefficient assets lie *below* the CML but *on* the SML if fairly priced.

**Trap flagged.** Don't quote σ on the SML's x-axis — it's beta.

---

### Q7. Raw beta vs adjusted beta — what and why?

**Model answer.** Empirically betas mean-revert toward 1 over time, so a raw regression beta over-states future extremeness. Bloomberg's **adjusted beta** shrinks it: $\beta_{adj} = 0.67\,\beta_{raw} + 0.33(1)$ — two-thirds weight on the estimate, one-third pull to the market beta of 1. It's a Bayesian adjustment that improves out-of-sample forecasts.

---

### Q8. When would you trust the dividend growth model over CAPM, and vice versa?

**Model answer.** Use **DGM** for mature, stable dividend payers — utilities, REITs, consumer staples, banks — where the dividend and its growth are predictable; $K_e = D_1/P_0 + g$. Use **CAPM** for cyclicals, growth firms, non-payers, and private companies (via bottom-up beta). DGM is hyper-sensitive to $g$ and breaks if $g \ge K_e$; CAPM depends on noisy beta and a debated ERP. Best practice: compute both and triangulate.

---

### Q9. What are CAPM's main limitations, and why is it still the industry default?

**Model answer.** Limitations: beta is estimated with error and unstable; the ERP is unobservable and debated; it's single-period and single-factor; the true market portfolio is unobservable (**Roll's critique**); and it empirically misses **size** and **value** effects (hence Fama–French). It survives in corporate valuation because it's **parsimonious** — one beta — and its inputs are estimable, whereas multifactor models add complexity without reliably improving a valuation discount rate. Multifactor models dominate portfolio management and attribution instead.

---

### Q10. What is the equity risk premium and how is it estimated?

**Model answer.** The ERP is the extra expected return for holding the market portfolio over the risk-free asset. Three approaches: **historical** (long-run average realised $r_m - r_f$; choose arithmetic mean and horizon), **implied/forward-looking** (solve for the rate equating index price to PV of expected cash flows — market-consistent, updates daily), and **survey**. US figures cluster around **4.5%–6%**. For emerging markets, add a **country risk premium** = sovereign default spread scaled by relative equity/bond volatility.

---

### Q11. Explain multifactor models in one minute.

**Model answer.** CAPM's single market factor under-explains returns, so multifactor models add priced systematic factors. **Fama–French 3-factor** adds **SMB** (size — small beats big) and **HML** (value — high book-to-market beats low). The **5-factor** adds profitability (**RMW**) and investment (**CMA**); **Carhart** adds **momentum**. **APT** is the general form: expected return is a linear function of several macro factor betas and their risk premia, with the factors determined empirically. These dominate portfolio and performance-attribution work; corporate finance still defaults to single-factor CAPM.

---

## Numerical Problems

### Q12. Basic CAPM.

$r_f = 3.8\%$, ERP = 5.5%, β = 1.10. Find $K_e$.

**Solution.**
$$K_e = 3.8\% + 1.10 \times 5.5\% = 3.8\% + 6.05\% = \mathbf{9.85\%}$$
**Check.** β slightly above 1, so Ke slightly above the market return $r_m = 3.8+5.5 = 9.3\%$. ✓ (9.85% > 9.3%.)

---

### Q13. Un-lever a beta.

A comp has levered β = 1.60, D/E = 0.90, tax rate = 30%. Find its unlevered (asset) beta.

**Solution.** $(1-t) = 0.70$.
$$\beta_U = \frac{1.60}{1 + 0.70 \times 0.90} = \frac{1.60}{1 + 0.63} = \frac{1.60}{1.63} = \mathbf{0.982}$$
**Check.** Un-levering must *reduce* beta (removing leverage). 0.982 < 1.60 ✓.

---

### Q14. Re-lever and get Ke.

Using the asset beta from Q13 (0.982), re-lever at a target D/E = 0.40, tax = 30%, then find $K_e$ with $r_f = 4\%$, ERP = 5%.

**Solution.**
$$\beta_L = 0.982 \times [1 + 0.70 \times 0.40] = 0.982 \times 1.28 = 1.257$$
$$K_e = 4\% + 1.257 \times 5\% = 4\% + 6.29\% = \mathbf{10.28\%}$$
**Check.** Lower target leverage (0.40 vs 0.90) → lower equity beta (1.257 < 1.60) → sensible. ✓

---

### Q15. Full bottom-up beta.

Value **DivCo** (target D/E = 0.50, tax = 25%). Comps:

| Comp | β_L | D/E |
|---|---|---|
| X | 1.20 | 0.40 |
| Y | 1.35 | 0.70 |
| Z | 1.05 | 0.20 |

All comps taxed at 25%. $r_f = 4.5\%$, ERP = 5.0%. Find DivCo's cost of equity.

**Solution.** $(1-t) = 0.75$.
Un-lever each:
- X: $1.20 / (1 + 0.75\times0.40) = 1.20/1.30 = 0.9231$
- Y: $1.35 / (1 + 0.75\times0.70) = 1.35/1.525 = 0.8852$
- Z: $1.05 / (1 + 0.75\times0.20) = 1.05/1.15 = 0.9130$

Average asset beta $= (0.9231 + 0.8852 + 0.9130)/3 = 2.7213/3 = 0.9071$.

Re-lever at D/E = 0.50: $\beta_L = 0.9071 \times (1 + 0.75\times0.50) = 0.9071 \times 1.375 = 1.2473$.

$$K_e = 4.5\% + 1.2473 \times 5.0\% = 4.5\% + 6.24\% = \mathbf{10.74\%}$$
**Check.** Unlevered betas cluster ~0.885–0.923 despite levered spread 1.05–1.35 — un-levering removed financing noise. ✓

---

### Q16. Dividend growth model — solve for Ke.

Price = \$80, just-paid dividend $D_0 = \$3.20$, sustainable growth $g = 5\%$. Find $K_e$.

**Solution.**
$$D_1 = 3.20 \times 1.05 = \$3.36$$
$$K_e = \frac{3.36}{80} + 0.05 = 0.042 + 0.05 = 0.092 = \mathbf{9.2\%}$$
**Check.** $g$ (5%) < $K_e$ (9.2%), so Gordon is valid. ✓

---

### Q17. Estimate g, then Ke via DGM.

A firm has ROE = 14%, dividend payout = 45%. Price = \$60, $D_0 = \$2.00$. Find the sustainable growth rate and $K_e$.

**Solution.**
Retention $b = 1 - 0.45 = 0.55$. Sustainable $g = b \times \text{ROE} = 0.55 \times 14\% = 7.7\%$.
$$D_1 = 2.00 \times 1.077 = \$2.154$$
$$K_e = \frac{2.154}{60} + 0.077 = 0.0359 + 0.077 = 0.1129 = \mathbf{11.29\%}$$
**Check.** $g$ (7.7%) < $K_e$ (11.3%) ✓.

---

### Q18. CAPM vs DGM triangulation.

Same firm as Q17: also β = 1.30, $r_f = 4\%$, ERP = 5.5%. Compute CAPM Ke and reconcile with the DGM's 11.29%.

**Solution.**
$$K_e^{CAPM} = 4\% + 1.30 \times 5.5\% = 4\% + 7.15\% = \mathbf{11.15\%}$$
**Reconciliation.** DGM 11.29% vs CAPM 11.15% — within ~0.15 pp, so the two methods **agree**, giving high confidence in a cost of equity of ~11.2%. When methods converge like this you quote the range with conviction; if they'd diverged you'd interrogate g (DGM) or beta/ERP (CAPM).

---

### Q19. Walking the SML — is it mispriced?

$r_f = 3.5\%$, ERP = 6%. A stock has β = 0.80 and an expected return of 9.5%. On, above, or below the SML? What's the alpha and the action?

**Solution.**
SML required $= 3.5\% + 0.80 \times 6\% = 3.5\% + 4.8\% = 8.3\%$.
Expected 9.5% > required 8.3% → **above the SML**.
$$\alpha = 9.5\% - 8.3\% = +1.2\%$$
Positive alpha → **undervalued → buy.** As buyers push the price up, expected return falls back toward 8.3%.

---

### Q20. Debt-beta version of un-levering.

A comp: β_L = 1.40, D/E = 1.00, tax = 25%, and its debt is risky with β_D = 0.20. Un-lever using the debt-beta formula and compare with the βD = 0 result.

**Solution.** $(1-t) = 0.75$.
Debt-beta formula: $\beta_U = \dfrac{\beta_L + \beta_D(1-t)D/E}{1+(1-t)D/E}$.
Denominator $= 1 + 0.75 \times 1.00 = 1.75$.
Numerator $= 1.40 + 0.20 \times 0.75 \times 1.00 = 1.40 + 0.15 = 1.55$.
$$\beta_U = 1.55 / 1.75 = \mathbf{0.886}$$
Compare βD = 0: $\beta_U = 1.40/1.75 = 0.800$.
**Interpretation.** Ignoring debt beta *understates* the asset beta (0.800 vs 0.886), because part of the firm's systematic risk sits in the risky debt; the debt-beta formula reallocates it back to the asset. ✓

---

### Q21. Country risk premium in an emerging market.

An Indian company: US ERP = 5.0%. India sovereign default spread = 2.0%; relative volatility $\sigma_{equity}/\sigma_{bond} = 1.5$. β = 1.10, INR risk-free (G-Sec, default-stripped) = 6.5%. Find the total ERP and $K_e$.

**Solution.**
$$\text{CRP} = 2.0\% \times 1.5 = 3.0\%$$
$$\text{ERP}_{India} = 5.0\% + 3.0\% = 8.0\%$$
$$K_e = 6.5\% + 1.10 \times 8.0\% = 6.5\% + 8.8\% = \mathbf{15.3\%}$$
**Check.** Emerging-market Ke (15.3%) sits well above a comparable US name because of both a higher risk-free rate and the added country risk premium. ✓

---

### Q22. Sensitivity — why long-duration DCFs sweat the discount rate.

A stable firm's next-year FCFE = \$10, growing at g = 3% forever. Value the equity at (a) Ke = 9% and (b) Ke = 8%. By what % does value change for a 1-point Ke cut?

**Solution.** Gordon: $V = \text{FCFE}_1 / (K_e - g)$.
- (a) $V = 10 / (0.09 - 0.03) = 10 / 0.06 = \$166.7$
- (b) $V = 10 / (0.08 - 0.03) = 10 / 0.05 = \$200.0$

Change $= (200 - 166.7)/166.7 = 33.3/166.7 = \mathbf{+20\%}$.
**Interpretation.** A single percentage-point cut in Ke lifts value by 20% here, because value depends on the *spread* $(K_e - g)$, which is small. This is exactly why interviewers stress-test your Ke inputs — beta and ERP choices move valuations far more than they look. ✓

---

### Quick self-test checklist

- Can you state CAPM and justify each input from first principles?
- Can you un-lever and re-lever a beta *with* the $(1-t)$ term, and know the debt-beta and no-tax variants?
- Can you compute Ke from the DGM and know when it's more reliable than CAPM?
- Can you place a stock on the SML, compute alpha, and give the buy/sell call?
- Can you add a country risk premium and keep currency consistent?
