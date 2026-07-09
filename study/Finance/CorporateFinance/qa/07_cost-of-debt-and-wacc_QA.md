# Q&A — Cost of Debt & WACC

A mixed bank of theory (with model answers and interview phrasing) and fully-solved numerical problems. Numbers are self-verified. Work every numerical one with pen and paper before reading the solution.

---

## Theory questions

### Q1 (Theory) — Define WACC and explain what it represents.

**Model answer.** WACC is the weighted average of the returns required by all providers of a firm's capital — debt and equity — weighted by the market value of each. Formally, `WACC = (E/V)·Ke + (D/V)·Kd·(1−t)`. It represents the minimum return the firm's *assets* must earn to satisfy every capital provider, and equivalently the opportunity cost of the firm's capital. It is the correct discount rate for a firm's unlevered free cash flow (FCFF) in a DCF.

**How to say it in an interview.** *"WACC is what the whole capital structure costs, blended by market-value weights. It's the hurdle the assets have to clear to keep both lenders and shareholders whole — and it's the discount rate for unlevered free cash flow."*

---

### Q2 (Theory) — Why do we use the *after-tax* cost of debt in WACC, but not an after-tax cost of equity?

**Model answer.** Interest expense is tax-deductible: it's subtracted on the income statement *before* tax, so every rupee of interest reduces the tax bill by `t` rupees. The firm's true cost of a rupee of interest is therefore `Kd·(1−t)`. Dividends and retained earnings, by contrast, are paid out of *after-tax* profit — there is no deduction, hence no shield to apply — so the cost of equity enters WACC at full strength.

**Interview line.** *"The government pays part of the interest bill through the deduction, so debt's real cost is `Kd times one minus t`. Equity sits below the tax line, so there's nothing to shield."*

---

### Q3 (Theory) — Is the cost of debt equal to the coupon rate on the firm's bonds? Explain.

**Model answer.** No. The coupon is fixed at issuance and reflects the rate *at that time* — it's backward-looking. The cost of debt is the rate the firm would pay to borrow *today*, which is the current **yield to maturity** on its debt. If interest rates or the firm's credit have changed since issuance, the bond trades away from par and its YTM differs from its coupon. A bond trading at a discount has a yield *above* its coupon; that yield is the true cost of debt.

**Interview line.** *"Coupon is history; yield is the cost of borrowing now. Discounted bond means yield above coupon, and yield is what we use."*

---

### Q4 (Theory) — Market weights vs book weights: which does WACC use, and why?

**Model answer.** Market weights. WACC is a forward-looking opportunity cost: it describes how *today's* enterprise value is divided among *today's* claimholders and what each demands *now*. Book values are historical costs, potentially decades stale, and for equity can bear no relation to what the shareholders' claim is actually worth. Equity weight uses market capitalisation (price × diluted shares); debt weight ideally uses traded value, though book value of debt is an acceptable proxy for a healthy firm because debt usually trades near par.

**Interview line.** *"Market weights. WACC is an opportunity cost about today's value split — book equity is a stale accounting number that can be wildly off."*

---

### Q5 (Theory) — Target vs current capital structure for the weights. When do you use each?

**Model answer.** Use **current** weights when the firm's present market-value mix is stable and expected to persist. Use **target** weights — the firm's long-run policy structure — when the current mix is temporarily distorted (e.g., just after a debt-funded acquisition, or mid-deleveraging) or when discounting a long horizon over which the firm will drift toward its policy mix. The professional default for a multi-year DCF is target weights, because you're valuing a decade of cash flows and the structure in later years reflects policy, not today's accident. Crucially, you must re-lever beta to the target `D/E` so the cost of equity is consistent with the target weights.

**Interview line.** *"Target for a long DCF — and re-lever beta to that target so `Ke` and the weights are consistent."*

---

### Q6 (Theory) — Describe the effect of increasing leverage on WACC. Why is WACC U-shaped?

**Model answer.** Two opposing forces. **Direct effect:** debt is cheaper than equity and tax-deductible, so replacing equity with debt pulls WACC down. **Indirect effect:** more leverage makes the residual equity riskier, so `Ke` rises; and past some point the credit rating deteriorates, so `Kd` rises too, and expected financial-distress costs mount. Initially the direct effect (plus the tax shield) dominates and WACC falls. Beyond the optimal capital structure, the indirect effects dominate and WACC rises. Hence WACC is U-shaped in leverage, and its minimum is the value-maximising capital structure (minimising the discount rate on a fixed cash-flow stream maximises value).

**Interview line.** *"Cheap tax-shielded debt lowers WACC at first; rising equity risk, worse credit, and distress costs raise it past the optimum. U-shaped — and the bottom is the optimal structure."*

---

### Q7 (Theory) — State Modigliani–Miller Proposition II and explain how it makes WACC constant without taxes.

**Model answer.** MM Prop II (no taxes): `Ke = Ka + (Ka − Kd)·(D/E)`, where `Ka` is the unlevered cost of capital. As `D/E` rises, the cost of equity rises **linearly**. In a world with no taxes or distress costs, this increase in `Ke` exactly offsets the substitution of cheaper debt for equity, so WACC stays pinned at `Ka` regardless of leverage. Capital structure is irrelevant to firm value (MM Prop I) — you're only re-slicing a fixed pie. Adding corporate taxes breaks the symmetry: the debt tax shield makes WACC fall with leverage (`WACC = Ka·[1 − t·D/V]`), and adding distress costs turns that into the U-shape.

**Interview line.** *"Without taxes, the rising cost of equity exactly cancels the cheap debt, so WACC is flat at `Ka`. Taxes tilt it down; distress bends it back up."*

---

### Q8 (Theory) — When is WACC *not* the appropriate discount rate? Give three situations and the fix.

**Model answer.**
1. **Discounting FCFE** (cash flow to equity, after debt service): use the **cost of equity**, not WACC — FCFE belongs to shareholders alone, so blending in the debt return double-counts the debt benefit.
2. **A project whose risk differs from the firm's:** use a **project-specific WACC** built from pure-play comparable betas, re-levered to the project's financing. The firm WACC embeds the wrong beta.
3. **Changing capital structure** (e.g., an LBO paying down debt): WACC assumes constant `D/V`, which is violated. Use **APV** — value the firm unlevered, then add the present value of the tax shields year by year.

**Interview line.** *"FCFE means use `Ke`; different project risk means pure-play WACC; changing leverage means APV. WACC is only right for FCFF, stable leverage, matching risk."*

---

### Q9 (Theory) — How would you estimate the cost of debt for a private company with no traded bonds?

**Model answer.** Use a **synthetic rating**. Compute the interest coverage ratio (`EBIT / interest expense`), map it to an implied credit rating using a published coverage-to-rating table (e.g., Damodaran's), read off the default spread associated with that rating, and add it to a maturity-matched risk-free rate: `Kd = rf + default spread`. Cross-check against the interest rate on any debt the firm has raised recently. Avoid the crude `interest expense / total debt` book rate as a primary estimate — it's backward-looking and contaminated by old fixed-rate debt.

**Interview line.** *"Synthetic rating: coverage ratio → implied rating → default spread → add the risk-free rate. Sanity-check against any recent borrowing."*

---

### Q10 (Theory) — What is the WACC circularity problem, and how is it resolved?

**Model answer.** WACC requires market-value weights, but the market value of equity is itself the *output* of the DCF you intend to discount using WACC — so the input depends on the answer. Two resolutions: (1) assume **target weights** as a fixed policy input, which breaks the loop cleanly; or (2) **iterate** — start with a guessed WACC, run the DCF to get an equity value, recompute the weights, re-run, and repeat until the weights and value converge.

**Interview line.** *"The equity weight depends on the equity value, which depends on the WACC. Break it with target weights, or iterate to convergence."*

---

### Q11 (Theory) — A regulated utility with a 6% WACC wants to fund a speculative tech venture and discounts it at 6%. What's the error and the correct approach?

**Model answer.** The firm-wide 6% WACC embeds the utility's very low asset beta. The venture is far riskier, so discounting its cash flows at 6% massively understates the hurdle — almost any project clears 6% — and will greenlight value-destroying investments. The fix: build a **project-specific WACC** using the unlevered beta of pure-play tech comparables, re-lever it to the venture's target financing, compute a project cost of equity via CAPM, and blend with the venture's own cost of debt. The discount rate must reflect the risk of the *project*, not the *company*.

**Interview line.** *"Wrong beta. Discount the venture at a pure-play tech WACC, not the utility's rate — the rate follows the project's risk, not the parent's."*

---

## Numerical problems

### Q12 (Numerical) — Cost of debt from a discounted bond, then after-tax.

**Problem.** A bond has face value ₹1,000, pays a 7% annual coupon (₹70), has 4 years to maturity, and trades at ₹950. The tax rate is 30%. Find the pre-tax and after-tax cost of debt.

**Solution.**
Since the bond trades below par, YTM > 7%. Solve `950 = Σ 70/(1+y)^t + 1000/(1+y)^4`. Try `y = 8.5%`:
- Discount factor at year 4: `1.085⁻⁴ = 1/1.3859 = 0.7216`.
- Annuity factor(8.5%, 4) = `(1 − 0.7216)/0.085 = 0.2784/0.085 = 3.2753`.
- PV coupons = `70 × 3.2753 = 229.3`; PV face = `1000 × 0.7216 = 721.6`; total = `950.9`. ✓ (≈ 950)

So **YTM ≈ 8.5%** → pre-tax `Kd = 8.5%`.
After-tax `Kd = 8.5% × (1 − 0.30) = 8.5% × 0.70 =` **5.95%**.

**Key point.** The 7% coupon was not the cost of debt; the 8.5% market yield was.

---

### Q13 (Numerical) — Straightforward WACC build.

**Problem.** Cost of equity 14%, pre-tax cost of debt 8%, tax rate 25%, capital structure 40% debt / 60% equity (market values). Compute WACC.

**Solution.**
- After-tax `Kd = 8% × 0.75 = 6.0%`.
- `WACC = 0.60 × 14% + 0.40 × 6.0% = 8.4% + 2.4% =` **10.8%**.

**Sanity check.** 10.8% lies between 6.0% and 14%, closer to equity because equity is the heavier weight. ✓

---

### Q14 (Numerical) — WACC from raw market data (CAPM + market weights).

**Problem.** Share price ₹80, 50 million diluted shares, debt ₹1,000 million (book ≈ market). Risk-free 6.5%, beta 1.3, ERP 5%, pre-tax `Kd` 8.5%, tax 25%. Compute WACC.

**Solution.**
- `Ke = 6.5% + 1.3 × 5% = 6.5% + 6.5% = 13.0%`.
- After-tax `Kd = 8.5% × 0.75 = 6.375%`.
- `E = 80 × 50m = ₹4,000m`; `D = ₹1,000m`; `V = ₹5,000m`.
- `E/V = 0.80`; `D/V = 0.20`.
- `WACC = 0.80 × 13.0% + 0.20 × 6.375% = 10.40% + 1.275% =` **11.675% ≈ 11.7%**.

**Sanity check.** Between 6.375% and 13.0%, near the equity end (80% equity). ✓

---

### Q15 (Numerical) — Include preferred stock (three components).

**Problem.** A firm is financed 50% equity, 10% preferred, 40% debt (market weights). `Ke = 15%`, preferred dividend ₹8 on a preferred price of ₹100, pre-tax `Kd = 9%`, tax 30%. Compute WACC.

**Solution.**
- `Kp = 8 / 100 = 8.0%` (no tax adjustment on preferred).
- After-tax `Kd = 9% × 0.70 = 6.3%`.
- `WACC = 0.50 × 15% + 0.10 × 8.0% + 0.40 × 6.3%`
- `= 7.5% + 0.8% + 2.52% =` **10.82%**.

**Key point.** Preferred enters at its full dividend yield — no `(1 − t)` — because preferred dividends are not tax-deductible.

---

### Q16 (Numerical) — Re-lever beta and recompute WACC at a new target structure.

**Problem.** A firm is currently 30% debt / 70% equity (`D/E = 0.4286`), levered beta 1.25, risk-free 7%, ERP 5.5%, tax 25%, pre-tax `Kd` 8.5%. It targets 50% debt / 50% equity, at which pre-tax `Kd` rises to 9.5%. Compute WACC at both structures using Hamada.

**Solution.**
**Un-lever current beta** (`D/E = 0.4286`):
`βU = 1.25 / [1 + 0.75 × 0.4286] = 1.25 / 1.3214 = 0.9460`.

**Current WACC (30/70):**
- `Ke = 7% + 1.25 × 5.5% = 7% + 6.875% = 13.875%`.
- After-tax `Kd = 8.5% × 0.75 = 6.375%`.
- `WACC = 0.70 × 13.875% + 0.30 × 6.375% = 9.7125% + 1.9125% =` **11.625%**.

**Re-lever to target (`D/E = 1.0`):**
`βL = 0.9460 × [1 + 0.75 × 1.0] = 0.9460 × 1.75 = 1.6555`.

**Target WACC (50/50):**
- `Ke = 7% + 1.6555 × 5.5% = 7% + 9.105% = 16.105%`.
- After-tax `Kd = 9.5% × 0.75 = 7.125%`.
- `WACC = 0.50 × 16.105% + 0.50 × 7.125% = 8.0525% + 3.5625% =` **11.615%**.

**Interpretation.** WACC barely moves (11.625% → 11.615%) — the extra tax-shielded debt is almost exactly offset by the sharply higher cost of equity (13.9% → 16.1%) and the higher cost of debt (8.5% → 9.5%). This firm is sitting near the flat bottom of its WACC U-curve; the marginal benefit of more leverage has nearly vanished.

**Round-trip check.** Re-levering `βU` back to `D/E = 0.4286`: `0.9460 × 1.3214 = 1.250` ✓.

---

### Q17 (Numerical) — Project-specific WACC from pure-play comps.

**Problem.** A conglomerate (firm WACC 9%) evaluates a logistics project. Comparable pure-play logistics firms have an unlevered beta of 0.95. The project will be funded 40% debt / 60% equity (`D/E = 0.6667`). Risk-free 7%, ERP 5.5%, project pre-tax `Kd` 8%, tax 25%. What discount rate should the project use?

**Solution.**
**Re-lever the comp beta to the project's financing** (`D/E = 0.6667`):
`βL = 0.95 × [1 + 0.75 × 0.6667] = 0.95 × 1.5 = 1.425`.

**Project cost of equity:**
`Ke = 7% + 1.425 × 5.5% = 7% + 7.8375% = 14.8375%`.

**After-tax cost of debt:** `8% × 0.75 = 6.0%`.

**Project WACC:**
`= 0.60 × 14.8375% + 0.40 × 6.0% = 8.9025% + 2.40% =` **11.30%**.

**Answer.** Use **~11.3%**, not the firm's 9%. The project is riskier than the conglomerate average (levered beta 1.425 vs whatever the firm-wide blend is), so its hurdle is higher. Discounting at the 9% firm WACC would over-value the project.

---

### Q18 (Numerical) — WACC when the firm cannot fully use the tax shield.

**Problem.** A firm borrows at a pre-tax `Kd` of 10%. Its statutory tax rate is 30%, but it currently generates **no taxable income** (it is loss-making). It is 50% debt / 50% equity with a cost of equity of 16%. Compute WACC (a) assuming the full tax shield and (b) assuming no usable shield this year.

**Solution.**
(a) **Full shield:** after-tax `Kd = 10% × 0.70 = 7.0%`.
`WACC = 0.50 × 16% + 0.50 × 7.0% = 8.0% + 3.5% =` **11.5%**.

(b) **No usable shield** (effective tax benefit = 0, so after-tax `Kd = pre-tax Kd = 10%`):
`WACC = 0.50 × 16% + 0.50 × 10% = 8.0% + 5.0% =` **13.0%**.

**Key point.** The tax shield is only worth `t` if the firm has enough taxable income to use the deduction. A loss-making firm's effective after-tax cost of debt rises toward the pre-tax rate, pushing WACC up by 1.5 points here. Interviewers use this to test whether you understand *why* the `(1 − t)` term exists.

---

### Q19 (Numerical) — Solve for the implied cost of equity given a target WACC.

**Problem.** A firm wants a WACC of 10%. It is 35% debt / 65% equity, pre-tax `Kd` 8%, tax 25%. What cost of equity does this imply?

**Solution.**
After-tax `Kd = 8% × 0.75 = 6.0%`.
`WACC = (E/V)·Ke + (D/V)·Kd(1−t)`
`10% = 0.65·Ke + 0.35 × 6.0%`
`10% = 0.65·Ke + 2.10%`
`0.65·Ke = 7.90%`
`Ke = 7.90% / 0.65 =` **12.15%**.

**Check.** `0.65 × 12.15% + 0.35 × 6.0% = 7.8975% + 2.10% = 9.9975% ≈ 10%` ✓.

---

### Q20 (Numerical) — Credit spread and cost of debt decomposition.

**Problem.** A BBB-rated firm's bonds trade at a spread of 1.6% over the 5-year government bond, which yields 7.2%. The tax rate is 25%. What are the pre-tax and after-tax costs of debt, and what would the after-tax cost be if a downgrade to BB widened the spread to 3.5%?

**Solution.**
**BBB:** pre-tax `Kd = rf + spread = 7.2% + 1.6% = 8.8%`. After-tax `= 8.8% × 0.75 =` **6.6%**.
**After downgrade to BB:** pre-tax `Kd = 7.2% + 3.5% = 10.7%`. After-tax `= 10.7% × 0.75 =` **8.025%**.

**Key point.** A one-notch-plus downgrade widened the spread by 1.9 points and raised the after-tax cost of debt by ~1.4 points — illustrating exactly *why* adding leverage past the optimum raises `Kd` and bends WACC upward. Cost of debt is `risk-free + credit spread`, and the spread is a direct function of the rating.

---

### Q21 (Numerical) — Full DCF-context WACC with market-value debt below par.

**Problem.** A distressed firm has 20 million shares at ₹25 (equity market cap). Its debt has a face value of ₹800 million but, because of distress, trades at 70% of par. Pre-tax `Kd` (the current yield on that distressed debt) is 14%, tax 25%. Cost of equity 22%. Compute WACC using (a) book debt weight and (b) market debt weight, and explain which is correct.

**Solution.**
- Equity `E = 20m × 25 = ₹500m`.
- After-tax `Kd = 14% × 0.75 = 10.5%`.

(a) **Book debt = ₹800m:** `V = 500 + 800 = ₹1,300m`; `D/V = 0.6154`, `E/V = 0.3846`.
`WACC = 0.3846 × 22% + 0.6154 × 10.5% = 8.46% + 6.46% =` **14.92%**.

(b) **Market debt = 0.70 × 800 = ₹560m:** `V = 500 + 560 = ₹1,060m`; `D/V = 0.5283`, `E/V = 0.4717`.
`WACC = 0.4717 × 22% + 0.5283 × 10.5% = 10.38% + 5.55% =` **15.93%**.

**Which is correct?** The **market-value** version (b). For a distressed firm the debt trades far below par, so book value overstates the debt weight and understates the equity weight, producing a WACC that is ~1 point too low. Using market debt values gives the true opportunity-cost weighting.

---

### Q22 (Numerical) — Rapid-fire (do this in your head / on scratch paper in under 60 seconds).

**Problem.** Beta 1.4, risk-free 5%, ERP 6%, pre-tax `Kd` 7.5%, tax 20%, 30% debt / 70% equity. WACC?

**Solution.**
- `Ke = 5% + 1.4 × 6% = 5% + 8.4% = 13.4%`.
- After-tax `Kd = 7.5% × 0.80 = 6.0%`.
- `WACC = 0.70 × 13.4% + 0.30 × 6.0% = 9.38% + 1.80% =` **11.18% ≈ 11.2%**.

**Sanity check.** Between 6.0% and 13.4%, closer to equity (70% equity). ✓ Deliver both the number and this one-line check — it signals you understand what WACC *means*.

---

## One-page numerical summary

| # | Topic | Answer |
|---|---|---|
| Q12 | Cost of debt from discounted bond | Pre-tax 8.5%, after-tax 5.95% |
| Q13 | Simple WACC | 10.8% |
| Q14 | WACC from market data | 11.7% |
| Q15 | WACC with preferred | 10.82% |
| Q16 | Re-lever beta, two structures | 11.625% → 11.615% |
| Q17 | Pure-play project WACC | 11.3% |
| Q18 | Shield usable vs not | 11.5% vs 13.0% |
| Q19 | Implied cost of equity | 12.15% |
| Q20 | Spread → cost of debt | 6.6% → 8.025% after-tax |
| Q21 | Distressed, book vs market debt | 14.92% vs 15.93% |
| Q22 | Rapid-fire | 11.2% |
