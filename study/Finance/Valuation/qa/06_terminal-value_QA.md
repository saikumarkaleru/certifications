# Q&A — Terminal Value

A mixed bank of theory and numerical questions on terminal value for equity research, investment banking, and credit interviews. Theory answers include a "say it like this" interview line; numericals are fully solved and self-checked.

---

## Theory

### Q1. What is terminal value and why does a DCF need one?

**Answer.** A company is a going concern with an indefinite life, but you can only forecast cash flows credibly for a limited window (typically 5 years). Terminal value collapses **all cash flows beyond the explicit forecast** into a single number, struck as of the final forecast year *n*, which is then discounted back to today. Without it, a DCF would ignore the vast majority of a company's economic life.

**Say it like this:** "Terminal value captures everything after my explicit forecast — it's how a five-year model values a business that lives forever."

---

### Q2. Roughly what share of DCF value is terminal value, and why isn't that a defect?

**Answer.** Usually **60–85%** of enterprise value. It's not a defect — it reflects the reality that most of a going concern's value sits in cash flows beyond any forecast horizon. It *does* mean the terminal assumptions carry the most weight, so they get the most scrutiny and a sensitivity table.

**Say it like this:** "Most of the value is in the tail — that's not a bug, it's why I stress-test g and WACC and sanity-check the implied multiple."

---

### Q3. Name the two terminal-value methods and contrast them.

**Answer.**
- **Gordon (perpetuity) growth:** `TV_n = FCFF_n×(1+g)/(WACC−g)`. Intrinsic, theoretically clean, but highly sensitive to g and WACC.
- **Exit multiple:** `TV_n = EBITDA_n × EV/EBITDA`. Market-grounded, but imports today's sentiment and freezes it at year *n*.

They are duals: each implies the other, and a good model reconciles them.

**Say it like this:** "Perpetuity is intrinsic, exit multiple is market-based — I run both and cross-check."

---

### Q4. Why can't the terminal growth rate exceed long-run GDP growth?

**Answer.** If a firm grew faster than the economy *forever*, it would eventually become larger than the entire economy — impossible. So g is capped at long-run **nominal** GDP (real GDP + inflation), roughly 2–4% for a developed market. Staying below GDP is conservative.

**Say it like this:** "Nothing outgrows its economy in perpetuity, so g is capped at nominal GDP — I usually sit a touch below."

---

### Q5. Why is there a `(1 + g)` in the Gordon numerator?

**Answer.** The growing-perpetuity formula requires the cash flow **one period after** the valuation date. TV sits at year *n*, so the first terminal cash flow is year *n+1 = FCFF_n×(1+g)*. Omitting `(1+g)` understates TV by a factor of `(1+g)`.

---

### Q6. At what exponent do you discount the terminal value, and why is `n+1` wrong?

**Answer.** Discount TV at `(1+WACC)^n`, the same factor as the year-*n* cash flow, because TV is **valued as of year *n***. Using `n+1` double-counts a year of discounting and understates value. The `(1+g)` growth already handles the step from year *n* to *n+1* — the discounting stops at *n*.

---

### Q7. Why must you use an EV-based multiple (not P/E) for exit-multiple TV in an unlevered DCF?

**Answer.** An unlevered DCF discounts FCFF and produces an **enterprise value**. EV/EBITDA yields an enterprise value directly, keeping units consistent. A P/E multiple on net income yields an **equity value**, which floating inside an enterprise-value model is a units mismatch that corrupts the EV → equity bridge.

**Say it like this:** "EBITDA is pre-financing, so I pair it with an EV multiple to keep the whole model on an enterprise basis."

---

### Q8. How do you sanity-check a terminal value?

**Answer.** Run the two-way check:
- From the **Gordon TV**, compute the **implied exit multiple** = `TV_n / EBITDA_n`; verify it's near where mature comps trade.
- From the **exit-multiple TV**, compute the **implied growth rate** `g = (WACC×TV − FCFF)/(TV + FCFF)`; verify it's at or below nominal GDP.

If either implied number is absurd, an input (g, WACC, or the multiple) is off.

---

### Q9. Explain the mid-year convention and its directional effect.

**Answer.** Standard DCF assumes year-end cash receipt; mid-year assumes cash arrives evenly through the year, i.e. on average at the midpoint. You discount each flow **half a year less** (exponents 0.5, 1.5, 2.5…), which **raises** the valuation by roughly `(1+WACC)^0.5 − 1` ≈ 3–5%. For a Gordon TV you apply the half-year uplift; an exit-multiple TV is often treated as a point-in-time year-end sale and left un-bumped. Be consistent and disclose it.

---

### Q10. How does ROIC relate to terminal growth, and why does it matter?

**Answer.** Growth requires reinvestment: `g = Reinvestment rate × ROIC`, so `Reinvestment = g/ROIC` and terminal `FCFF = NOPAT×(1 − g/ROIC)`. If terminal **ROIC = WACC**, growth creates essentially **no value** (the extra capital earns exactly its cost). Value from growth only appears when **ROIC > WACC**. Cranking g without checking ROIC manufactures fake value.

**Say it like this:** "Growth only adds value if it earns above the cost of capital — otherwise you're just reinvesting to stand still."

---

### Q11. Walk me from terminal value to equity value per share.

**Answer.** TV is an enterprise value. Bridge: **EV − total debt − preferred − minority interest + cash = equity value**, then **÷ diluted shares** for per-share value. Debt and preferred are senior claims, minority interest is the non-owned slice of a consolidated sub, and cash is a non-operating asset that equity owns.

---

### Q12. Why is a razor-thin `WACC − g` spread dangerous?

**Answer.** TV is `cash flow / (WACC − g)`. As the denominator shrinks toward zero, TV explodes and becomes hypersensitive: a 50 bp move in g or WACC can swing value 20–30%. Valuations resting on a 1% spread are fragile — always show the sensitivity grid.

---

## Numerical

### Q13. Basic Gordon TV and its PV.

Year-5 FCFF = $80m, WACC = 10%, g = 3%. Find TV at year 5 and its PV today.

**Solution.**
```
TV_5 = 80 × 1.03 / (0.10 − 0.03) = 82.4 / 0.07 = $1,177.1m
Discount factor = 1/(1.10)^5 = 1/1.61051 = 0.62092
PV(TV) = 1,177.1 × 0.62092 = $730.9m
```
**TV_5 = $1,177.1m; PV = $730.9m.**

---

### Q14. Exit-multiple TV and implied growth.

Year-5 EBITDA = $150m, exit EV/EBITDA = 9.0x, year-5 FCFF = $70m, WACC = 9%. Find TV and the implied perpetual growth rate.

**Solution.**
```
TV_5 = 150 × 9.0 = $1,350m
Implied g = (WACC×TV − FCFF)/(TV + FCFF)
          = (0.09×1,350 − 70)/(1,350 + 70)
          = (121.5 − 70)/1,420
          = 51.5/1,420
          = 3.63%
```
**TV = $1,350m; implied g = 3.63%** — below nominal GDP, so the 9x is defensible.

---

### Q15. Implied exit multiple from a Gordon TV.

Year-5 FCFF = $110m, year-5 EBITDA = $210m, WACC = 8.5%, g = 2.5%. Compute the Gordon TV and its implied EV/EBITDA.

**Solution.**
```
TV_5 = 110 × 1.025 / (0.085 − 0.025) = 112.75 / 0.06 = $1,879.2m
Implied EV/EBITDA = 1,879.2 / 210 = 8.95x
```
**TV = $1,879.2m; implied multiple = 8.95x** — reasonable for a mature business.

---

### Q16. Full DCF to per-share value.

Given: PV of explicit FCFF (years 1–5) = $250m. Year-5 FCFF = $90m, WACC = 9%, g = 2%. Net debt = $300m, diluted shares = 40m. Find enterprise value, equity value, and value per share.

**Solution.**
```
TV_5 = 90 × 1.02 / (0.09 − 0.02) = 91.8 / 0.07 = $1,311.4m
DF_5 = 1/(1.09)^5 = 1/1.53862 = 0.64993
PV(TV) = 1,311.4 × 0.64993 = $852.4m
EV = 250 + 852.4 = $1,102.4m
Equity = 1,102.4 − 300 = $802.4m
Per share = 802.4 / 40 = $20.06
TV share of EV = 852.4/1,102.4 = 77.3%
```
**EV = $1,102.4m; equity = $802.4m; per share = $20.06** (TV is 77% of EV).

---

### Q17. Mid-year uplift on terminal value.

Take Q16's TV_5 = $1,311.4m, WACC = 9%, n = 5. Compute PV(TV) under the mid-year convention and the % uplift vs the whole-year PV of $852.4m.

**Solution.**
```
PV(TV, mid-year) = TV_5 × (1.09)^0.5 / (1.09)^5
                 = 1,311.4 × 1.04403 / 1.53862
                 = 1,369.1 / 1.53862
                 = $889.8m
Uplift = 889.8 / 852.4 − 1 = 4.39% ≈ (1.09)^0.5 − 1
```
**Mid-year PV(TV) = $889.8m, a 4.4% uplift** — exactly the half-year discount factor.

---

### Q18. Reinvestment-consistent terminal value.

Terminal-year NOPAT = $100m, g = 3%, terminal ROIC = 15%, WACC = 8%. Terminal EBITDA = $170m. Find the reinvestment rate, terminal FCFF, TV, and implied exit multiple.

**Solution.**
```
Reinvestment rate = g/ROIC = 3%/15% = 20%
NOPAT_(n+1) = 100 × 1.03 = 103
Terminal FCFF = 103 × (1 − 0.20) = 103 × 0.80 = $82.4m
TV = 82.4 / (0.08 − 0.03) = 82.4 / 0.05 = $1,648.0m
Implied EV/EBITDA = 1,648.0 / 170 = 9.69x
```
**Reinvestment 20%; FCFF $82.4m; TV $1,648.0m; implied 9.69x.**

---

### Q19. Value of growth: ROIC = WACC vs ROIC > WACC.

Terminal NOPAT_(n+1) = $103m, WACC = 8%, g = 3%. Compare TV when (a) ROIC = 8% and (b) ROIC = 16%, and against a no-growth harvest (g = 0, NOPAT = $100m).

**Solution.**
```
(a) ROIC = 8% = WACC:
    Reinvestment = 3%/8% = 37.5%
    FCFF = 103 × (1 − 0.375) = 103 × 0.625 = 64.375
    TV = 64.375 / 0.05 = $1,287.5m

(b) ROIC = 16%:
    Reinvestment = 3%/16% = 18.75%
    FCFF = 103 × (1 − 0.1875) = 103 × 0.8125 = 83.6875
    TV = 83.6875 / 0.05 = $1,673.8m

No-growth harvest (g = 0):
    TV = 100 / 0.08 = $1,250.0m
```
**Interpretation:** at ROIC = WACC, 3% growth adds only `1,287.5 − 1,250.0 = $37.5m` (~3%). At ROIC = 16%, the *same* 3% growth adds `1,673.8 − 1,250.0 = $423.8m` (~34%). **Growth is only valuable when ROIC > WACC.**

---

### Q20. Diagnose a broken terminal value.

An analyst's Gordon TV implies a 19x exit multiple while mature comps trade at 9–11x. Inputs: year-5 FCFF = $100m, year-5 EBITDA = $190m, WACC = 8%, g = 5%. What's wrong and fix it.

**Solution.**
```
Current TV = 100 × 1.05 / (0.08 − 0.05) = 105 / 0.03 = $3,500m
Implied multiple = 3,500 / 190 = 18.4x  → too rich
```
Problem: **g = 5% exceeds plausible nominal GDP** and the `WACC − g` spread is only 3%, inflating TV. Fix by cutting g to ~2.5%:
```
TV = 100 × 1.025 / (0.08 − 0.025) = 102.5 / 0.055 = $1,863.6m
Implied multiple = 1,863.6 / 190 = 9.81x  → in line with comps
```
**Root cause: g too high (above GDP). Corrected g = 2.5% → 9.8x, consistent with peers.**

---

### Q21. Two methods bracketing a value range.

Year-5 FCFF = $120m, year-5 EBITDA = $230m, WACC = 9.5%, g = 3%, exit EV/EBITDA = 8.5x. PV of explicit FCFF = $300m. Net debt = $250m, shares = 45m. Give the per-share value under each method.

**Solution.**
```
DF_5 = 1/(1.095)^5 = 1/1.57424 = 0.63523

Gordon:
  TV = 120 × 1.03 / (0.095 − 0.03) = 123.6 / 0.065 = $1,901.5m
  PV(TV) = 1,901.5 × 0.63523 = $1,207.9m
  EV = 300 + 1,207.9 = $1,507.9m
  Equity = 1,507.9 − 250 = $1,257.9m
  Per share = 1,257.9 / 45 = $27.95

Exit multiple:
  TV = 230 × 8.5 = $1,955.0m
  PV(TV) = 1,955.0 × 0.63523 = $1,241.9m
  EV = 300 + 1,241.9 = $1,541.9m
  Equity = 1,541.9 − 250 = $1,291.9m
  Per share = 1,291.9 / 45 = $28.71
```
**Range: $27.95 (Gordon) to $28.71 (exit multiple)** — a tight, well-triangulated band. Cross-check: Gordon implied multiple = 1,901.5/230 = 8.27x vs the 8.5x assumption — consistent.

---

### Q22. Sensitivity of TV to g and WACC.

Year-5 FCFF = $100m. Build the Gordon TV_5 grid for WACC ∈ {8%, 9%, 10%} and g ∈ {2%, 3%}. Comment.

**Solution.** `TV = 100×(1+g)/(WACC−g)`:

| | g = 2% | g = 3% |
|---|---|---|
| **WACC 8%** | 102/0.06 = **$1,700.0m** | 103/0.05 = **$2,060.0m** |
| **WACC 9%** | 102/0.07 = **$1,457.1m** | 103/0.06 = **$1,716.7m** |
| **WACC 10%** | 102/0.08 = **$1,275.0m** | 103/0.07 = **$1,471.4m** |

**Comment:** Holding WACC at 8%, moving g from 2% to 3% lifts TV 21% ($1,700m → $2,060m). Holding g at 3%, moving WACC from 8% to 10% cuts TV 29% ($2,060m → $1,471m). Terminal value is extremely sensitive to both — hence always present a grid, never a point estimate, and keep the `WACC − g` spread realistic.

---

**Self-check note:** all EV → equity → per-share bridges reconcile, discount factors use `1/(1+WACC)^n`, and every Gordon TV carries the `(1+g)` numerator. Implied-multiple and implied-growth cross-checks are internally consistent across Q13–Q22.
