# Q&A — DCF — WACC and the Cost of Capital

Practice bank for Chapter 23. Answer each question before reading the solution. The discount rate is the highest-leverage assumption in a DCF, so the goal is to *reconstruct* WACC from first principles and reproduce every number cell-for-cell in Excel. Every computational problem ties out to a clean figure so you can check yourself to the decimal.

---

## Section A — Concept Checks (test the WHY)

**A1. Why do we discount future cash flows at all, and why does a *higher* discount rate mean a *lower* value?**

Because a dollar in the future is worth less than a dollar today for two reasons: time value (today's dollar can be invested and earn a return) and risk (the future dollar may never arrive). The discount rate *is* the return investors require to bear that waiting and that risk. Dividing a future cash flow by `(1+rate)^n` translates it into today's purchasing power. A higher rate means investors demand more compensation, so they will pay less today — hence a lower present value. Risk and discount rate are two names for the same thing.

**A2. Why is WACC a *weighted average* rather than just the cost of equity?**

Because the cash flow being discounted — unlevered free cash flow (FCFF) — belongs to *all* capital providers jointly, before any split between interest to lenders and dividends to shareholders. If the cash pool serves both debt and equity, the required return on it must blend both groups' demands, weighted by how much capital each supplied. Discounting FCFF at the cost of equity alone would apply the shareholders' (higher) required return to cash that partly belongs to lenders, overstating the discount rate and understating value.

**A3. Why does CAPM price only *systematic* risk and ignore company-specific risk?**

Because investors hold diversified portfolios. Company-specific ("idiosyncratic") risk — a factory fire, a lawsuit — can be diversified away by holding many stocks, so the market does not pay you to bear it. What cannot be diversified away is the tendency of a stock to move *with the whole market* (systematic risk), measured by beta. CAPM therefore prices beta only: `ke = rf + beta*ERP`. Rewarding diversifiable risk would pay investors for something they could eliminate for free.

**A4. Why do we use the *after-tax* cost of debt but *not* an after-tax cost of equity?**

Because interest is tax-deductible and dividends are not. Every dollar of interest reduces taxable income, cutting the tax bill by `t` dollars, so the true economic cost of debt is `kd*(1-t)`. Dividends are paid out of after-tax profit and create no such shield, so the cost of equity needs no `(1-t)` adjustment. Building the shield into WACC lets FCFF stay a clean pre-financing number — we do not also subtract the shield inside the cash flows, or we would double-count it.

**A5. Why market-value weights instead of book-value weights?**

Because the discount rate must reflect what investors require *today* on capital priced at *today's* values. Book values are accounting records of past transactions. A firm trading at three times book has far more equity value than its balance sheet shows; using book equity would understate the equity weight, hand too much influence to the cheaper debt, and depress WACC — inflating the valuation. Market cap for equity, market (or par-proxy) value for debt.

**A6. Why must a comparable's beta be *unlevered* before you can use it, then *relevered* to the target?**

Because an observed equity ("levered") beta blends two risks: the underlying business risk *and* the extra volatility that leverage piles onto equity returns. Two firms in the identical business can show different equity betas purely because one carries more debt. Unlevering strips leverage out to isolate pure asset (business) risk, which is comparable across firms. You take the median asset beta of the comp set, then relever it to the *target's own* D/E so the final beta reflects the target's actual financial risk, not the comps'.

**A7. Why must the cash-flow type and the discount rate agree?**

Because each cash-flow definition already embeds a financing assumption. FCFF is pre-financing cash to *all* providers, so it must be discounted at the all-providers rate, WACC. FCFE is levered cash left for *shareholders* after interest and debt flows, so it must be discounted at the cost of equity. Discounting FCFF at `ke`, or FCFE at WACC, mixes a whole-firm cash stream with an equity-only rate (or vice versa) — the single most common structural error in valuation.

**A8. Why is WACC always an axis in the DCF sensitivity table?**

Because WACC is *estimated*, not observed — every input (ERP, beta, spread) carries error bars of whole percentage points — and because it compounds against every year and dominates the terminal value, where the tiny `WACC − g` denominator makes value hypersensitive. A one-point move in WACC can swing enterprise value 10–20%. Showing a single point estimate hides that fragility; a two-way data table over WACC and terminal growth discloses it honestly.

---

## Section B — Build / Computational Problems

*Convention: percentages to one decimal (betas to two), inputs would be blue in Excel, calculations black. Every answer reconciles by hand.*

**B1. Cost of equity via CAPM.** Risk-free rate 4.0%, ERP 5.0%, beta 1.10, no size or country premium. Compute `ke`.

`ke = rf + beta*ERP = 4.0% + 1.10 * 5.0% = 4.0% + 5.5% = 9.5%`.
Excel: `=Rf + Beta*ERP`. Sanity check: beta > 1 means above-market risk, so `ke` (9.5%) sits above the implied market return `rf + ERP = 9.0%`. Consistent.

**B2. Adjusted (Bloomberg) beta.** A raw regression beta is 1.50. Convert to an adjusted beta.

`beta_adj = 0.67*beta_raw + 0.33*1.0 = 0.67*1.50 + 0.33 = 1.005 + 0.330 = 1.335`.
Excel: `=0.67*B + 0.33`. The adjustment pulls a noisy raw estimate toward the market mean of 1.0, reflecting the empirical tendency of betas to mean-revert.

**B3. Unlever a single comparable.** Comp has levered beta 1.25, D/E 0.50, tax 25%. Find its asset (unlevered) beta.

`beta_U = beta_L / (1 + (1-t)*D/E) = 1.25 / (1 + 0.75*0.50) = 1.25 / 1.375 = 0.9091`.
Excel: `=BetaL/(1+(1-t)*DE)`. The asset beta (0.91) is below the levered beta (1.25) because we removed the risk that leverage added.

**B4. After-tax cost of debt two ways.** The firm is rated BBB; risk-free 4.0%, credit spread 2.0%, marginal tax 25%. Compute pre-tax and after-tax `kd`.

Pre-tax `kd = rf + spread = 4.0% + 2.0% = 6.0%`. After-tax `kd = 6.0% * (1 - 0.25) = 4.5%`.
Excel: `=Rf+Spread` then `=Kd*(1-t)`. The 1.5-point gap (6.0% → 4.5%) is the tax shield the government effectively funds.

**B5. Market-value weights from a share price.** Share price 50, diluted shares 20 million, book debt 500 million trading near par. Compute the weights.

`E = 50 * 20m = 1,000m`. `D = 500m` (par proxy acceptable). `E + D = 1,500m`.
`we = 1,000 / 1,500 = 66.7%`, `wd = 500 / 1,500 = 33.3%`. They sum to 1. Excel: `=E/(E+D)` and `=D/(E+D)`.

**B6. Full WACC with bottom-up beta (the flagship reconciliation).** Build WACC end to end from these inputs. Risk-free 4.0%, ERP 5.0%, marginal tax 25%, target D/E 0.50, size premium 1.0% (mid-cap), country premium 0%, credit spread 2.0%. Comp set for beta:

| Comp | Levered β | D/E | Tax |
|------|----------:|----:|----:|
| X | 1.15 | 0.30 | 25% |
| Y | 1.25 | 0.50 | 25% |
| Z | 1.40 | 0.80 | 25% |

*Step 1 — Unlever each comp* with `=BetaL/(1+(1-t)*DE)`:

| Comp | Calculation | Asset β |
|------|-------------|--------:|
| X | 1.15 / (1 + 0.75·0.30) = 1.15 / 1.225 | 0.9388 |
| Y | 1.25 / (1 + 0.75·0.50) = 1.25 / 1.375 | 0.9091 |
| Z | 1.40 / (1 + 0.75·0.80) = 1.40 / 1.600 | 0.8750 |

*Step 2 — Median asset beta.* Sorted: 0.8750, 0.9091, 0.9388 → median = **0.9091** (`=MEDIAN(range)`; the median resists the two outliers).

*Step 3 — Relever to the target's D/E = 0.50:*
`beta_L = 0.9091 * (1 + 0.75*0.50) = 0.9091 * 1.375 = 1.25`.
(Notice it lands back on 1.25 — because comp Y already had exactly the target's D/E, its levered beta is unchanged, a useful reasonableness cross-check.)

*Step 4 — Cost of equity (CAPM + size premium):*
`ke = 4.0% + 1.25*5.0% + 1.0% = 4.0% + 6.25% + 1.0% = 11.25%`.

*Step 5 — After-tax cost of debt:*
`kd = 4.0% + 2.0% = 6.0%` pre-tax; `6.0%*(1-0.25) = 4.5%` after-tax.

*Step 6 — Market-value weights from D/E = 0.50:* set E = 1, D = 0.5, total 1.5 → `we = 1/1.5 = 66.7%`, `wd = 0.5/1.5 = 33.3%`. (Same D/E drives both the relever step and the weights — consistent.)

*Step 7 — Assemble WACC:*
`WACC = we*ke + wd*kd(1-t) = 0.6667*11.25% + 0.3333*4.5% = 7.50% + 1.50% = 9.0%`.

**WACC = 9.0%.** Reconciliation checks: it lies strictly between the after-tax cost of debt (4.5%) and the cost of equity (11.25%) — mandatory for a weighted average; it leans toward equity because equity is two-thirds of the structure; the weights sum to 1; one tax rate (25%) and one D/E (0.50) run through every step. Excel one-liner once helper cells exist: `=We*Ke + Wd*Kd*(1-Tax)`.

**B7. Sensitivity — move one input.** Take B6 and change *only* the ERP from 5.0% to 6.0%. Recompute `ke` and WACC.

New `ke = 4.0% + 1.25*6.0% + 1.0% = 4.0% + 7.5% + 1.0% = 12.5%`.
New `WACC = 0.6667*12.5% + 0.3333*4.5% = 8.33% + 1.50% = 9.83%`.
A one-point ERP change moved WACC by ~0.83 points (9.0% → 9.83%). In a DCF that alone can cut enterprise value 8–15%, which is exactly why the two-way data table is mandatory.

**B8. Reconcile a WACC that is "too low."** A junior analyst reports WACC = 4.8% for the B6 firm. Without redoing the build, show it must be wrong.

WACC is a weighted average of 4.5% (after-tax debt) and 11.25% (equity); a weighted average must lie *between* its inputs. 4.8% sits essentially on top of the debt cost, which would require a ~97% debt weight — impossible for a firm with D/E = 0.50 (only 33% debt). The reported figure violates the bounds check, so an input (almost certainly a mis-keyed weight or a missing equity term) is wrong. The correct value, 9.0%, sits sensibly two-thirds of the way toward equity.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through how you build a WACC."**

"WACC is the weighted average of the cost of equity and the after-tax cost of debt, weighted by market values. I start with the cost of equity via CAPM: the current risk-free rate — the 10-year government bond in the cash flows' currency — plus beta times the equity risk premium, plus any size or country premium the target warrants. For beta I take a set of listed comps, unlever each one's equity beta to strip out leverage, take the median asset beta, and relever it to my target's capital structure. Then the cost of debt: ideally the yield to maturity on the company's own bonds, otherwise the risk-free rate plus a rating-implied credit spread, times one minus the marginal tax rate. Finally I weight both by market values of equity and debt and blend them. Throughout I keep the tax rate, D/E, and currency consistent, and I sensitise the output because it's the model's highest-leverage assumption."

**C2. "Your DCF value looks high. Which single WACC input would you pressure-test first, and why?"**

"Beta, because it drives the cost of equity, which usually carries the largest weight, and it's the most judgemental input — the choice of comp set, regression window, and lever/relever mechanics all swing it. I'd check whether the comps are genuinely comparable in business risk, whether I used the median rather than a mean pulled by an outlier, and whether I relevered at the same D/E I used in the weights. After beta I'd re-examine the ERP and the terminal growth rate, since the `WACC − g` gap in terminal value amplifies any WACC error."

**C3. "Why not just use the company's historical average interest rate as the cost of debt?"**

"Because interest expense divided by total debt is a backward-looking blended rate on borrowings the company took out years ago at yesterday's rates and credit spreads. WACC needs the *marginal* cost — what the firm would pay to raise a fresh dollar of debt *today*. If rates or the company's credit have moved, the historical rate misstates the true cost. I'd prefer the yield to maturity on its traded bonds, or the risk-free rate plus a spread implied by its current credit rating, and only fall back to the historical average as a last-resort proxy."

**C4. "A private company has no market cap and no traded beta. How do you get a discount rate?"**

"Beta comes from the bottom-up method, which never needed the target's own regression — I unlever the median beta of listed comparables and relever it to the private firm's target capital structure. For the weights I face a circularity, because equity value depends on WACC but the weights depend on equity value. I resolve it by assuming a *target* or industry-norm capital structure rather than the firm's own iterated equity value, so the weights are set exogenously. Cost of debt comes from a synthetic rating: estimate the rating from the interest coverage ratio, then apply the matching spread. I'd also consider a size premium, since small private firms tend to out-earn what plain CAPM predicts."

**C5. "Should WACC ever change across the forecast?"**

"In principle yes — if you expect the capital structure to migrate materially (a leveraged firm deleveraging toward an industry norm), the weights and the relevered beta both shift, so a rigorous model steps WACC over time. In practice most DCFs hold a single constant WACC, because the added precision is usually swamped by input noise. The defensible middle ground is to build to a stable *target* capital structure, hold WACC constant, and disclose that assumption."

---

## Section D — Common-Error Spotting

*Each item shows a wrong build. Identify the error and give the fix.*

**D1.** An analyst discounts FCFF (unlevered free cash flow) at the cost of equity of 12%.

**Error:** cash-flow/rate mismatch. FCFF is pre-financing cash to all providers and must be discounted at WACC, not `ke`. Using `ke` applies the equity-only required return to cash that partly belongs to lenders, overstating the rate and understating value. **Fix:** discount FCFF at WACC; reserve `ke` for FCFE.

**D2.** Weights are computed from the balance sheet: book equity 400, book debt 600, so `we = 40%`. The stock actually trades at 2.5× book.

**Error:** book-value weights. True equity value is 400 × 2.5 = 1,000, so with debt near par at 600 the real equity weight is 1,000/1,600 = 62.5%, not 40%. Book weights understate equity and depress WACC. **Fix:** use market cap for equity (and market/par value for debt).

**D3.** Beta is relevered at D/E = 0.30, but the WACC weights are built from D/E = 0.60.

**Error:** inconsistent capital structure. The same D/E must drive both the relever step and the weights; mixing two leverage ratios makes the beta and the weights describe different companies. **Fix:** pick one capital structure (current stable, or target) and use it in both places.

**D4.** Cash flows are in INR; the risk-free rate used is the 4.2% US 10-year Treasury yield.

**Error:** currency mismatch. The risk-free rate, ERP, and cash flows must all live in one currency — INR cash flows require the INR government bond yield (which embeds INR inflation). Mixing currencies double-counts or omits inflation. **Fix:** use the local-currency risk-free rate, or convert cash flows to USD consistently.

**D5.** For a small emerging-market target, the analyst uses plain CAPM (`rf + beta*ERP`) with a mature-market ERP and adds *no* premia, getting `ke = 9%`.

**Error:** omitted premia. Plain CAPM systematically under-predicts required returns for small and emerging-market firms. **Fix:** add a size premium (from valuation handbooks) and a country risk premium (sovereign spread), documenting each — while taking care not to also inflate the ERP for the same country risk (that would double-count).

**D6.** Beta unlevering uses tax 30%, the after-tax debt term uses tax 21%, and the cash flows are taxed at 25%.

**Error:** inconsistent tax rate. The same marginal tax rate must run through the beta unlever/relever, the after-tax cost of debt, and the operating cash flows. Three different rates make the shield and the leverage adjustment mutually incoherent. **Fix:** choose one marginal rate and reuse it everywhere.

**D7.** A single-company regression gives a raw beta of 1.85; it is fed straight into CAPM.

**Error:** raw single-name regression beta — noisy, unstable, sensitive to the window and index chosen. **Fix:** at minimum apply the adjusted-beta shrinkage (`0.67*raw + 0.33`), and preferably build a bottom-up median beta from a comp set, which is far more robust.

**D8.** The report states WACC = 10.213% and stops there.

**Error:** false precision with no sensitivity. The inputs carry whole-percentage-point uncertainty, so three decimals imply confidence the estimate does not have, and a single point hides the DCF's fragility. **Fix:** report WACC to one decimal and always accompany it with a two-way sensitivity table (WACC × terminal growth).

**D9.** A private-company model shows a circular reference: equity value feeds WACC, WACC feeds the DCF, the DCF feeds equity value. The analyst just clicks "OK" past the warning and the cells show 0.

**Error:** an accidental, unresolved circularity that silently zeroed out. **Fix:** break it deliberately — use a *target* capital structure so the weights are exogenous, or enable iterative calculation on purpose (File → Options → Formulas) with a controlled convergence — never leave a circular reference to resolve itself to zero.

---

*Self-check note:* the flagship build (B6) resolves to exactly WACC = 9.0% because comp Y's D/E equals the target's, so the median asset beta relevers back to 1.25 — reproduce it in Excel and confirm each helper cell before trusting any downstream valuation.
