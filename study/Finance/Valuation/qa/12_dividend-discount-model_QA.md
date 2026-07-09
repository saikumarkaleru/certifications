# Q&A — The Dividend Discount Model

A mix of theory (with interview-ready phrasing) and fully-solved numerical problems. Every number is self-verified and reconciles.

---

## Theory

### Q1. What is the dividend discount model in one sentence, and why is it conceptually the "purest" equity valuation?
**A.** A stock is worth the present value of all future dividends discounted at the cost of equity. It is the purest model because the dividend is the only cash flow that unambiguously and directly reaches an equity holder without any further transaction — capital gains merely reflect the PV of dividends *after* you sell, so they are not an independent source of value.

**How to say it:** *"Even a capital gain is just the next buyer paying you for the dividends they'll collect. Strip that away and a share is nothing but the PV of the cash the company will ever return to owners — that's the DDM."*

### Q2. Derive the Gordon growth formula from the one-period return identity.
**A.** Start from `P₀ = (D₁ + P₁)/(1+r)`. Since `P₁` is itself the PV of future dividends, substitute recursively to get `P₀ = Σ Dₜ/(1+r)ᵗ`. With `Dₜ = D₁(1+g)^{t-1}`, this is a geometric series with ratio `(1+g)/(1+r)`. Summing (valid when `r > g`) gives `P₀ = D₁/(r − g)`. The `r > g` requirement is the series' convergence condition.

### Q3. Why must r > g, and what happens if you violate it?
**A.** `r > g` is the mathematical condition for the infinite geometric series to converge; economically, nothing can grow faster than the cost of equity — or the whole economy — forever. Violate it and the formula returns a negative or nonsensical price, which is the classic sign of the error. Terminal `g` should sit below long-run nominal GDP growth (~4–6%).

### Q4. Where does the growth rate come from? Can you assume any g?
**A.** No. Sustainable growth `g = retention × ROE = b × ROE`. A firm grows earnings only by reinvesting profits at some ROE. So growth, payout, and profitability must reconcile. Example: 8% growth with a 90% payout (10% retention) implies ROE = 80% — implausible, a red flag.

**How to say it:** *"Growth is earned, not assumed — g equals plowback times ROE. If someone hands me a growth number I immediately check it against retention and ROE."*

### Q5. When is DDM the right model, and when is it wrong?
**A.** Right for stable dividend payers where dividends approximate shareholder cash flow: **banks, insurers** (FCFF and EV/EBITDA break down because debt is raw material), **regulated utilities**, **REITs**, and mature high-payout staples. Wrong for non-dividend payers, heavy-buyback firms (DDM undervalues them), and cyclicals/turnarounds (erratic dividends). There, use FCFE.

### Q6. Reconcile the DDM with the FCFE model.
**A.** FCFE is the cash a firm *could* pay after reinvestment and net debt flows — its *capacity*. Dividends are what it *chooses* to pay. If payout = FCFE, the two models give identical values. When a firm retains cash, DDM understates value unless the cash is eventually distributed; when it over-distributes (debt-funded dividends), DDM overstates. Default to FCFE when the two diverge because dividend policy is discretionary.

### Q7. "A company pays no dividend — is it worthless under the DDM?"
**A.** No. The DDM discounts *all future* dividends, including those a firm will pay only once it matures. You'd model rising payout in a multi-stage version. In practice, for a true non-payer, switch to FCFE so the value doesn't hinge on dividend-policy timing — but the principle holds: even a growth stock is ultimately worth the cash it will one day return.

### Q8. Explain the H-model and what H represents.
**A.** The H-model values a firm whose growth *declines linearly* from a high rate `gₛ` to a stable rate `g_L` over `2H` years. `P₀ = D₀(1+g_L)/(r − g_L) + D₀·H·(gₛ − g_L)/(r − g_L)`. The first term is the plain Gordon value at the stable rate; the second is a premium for the extra growth during the fade. **`H` is half the transition period** — the key trap. It approximates a declining-growth path in closed form.

### Q9. How do you back out the cost of equity from the DDM, and what's the "implied ERP"?
**A.** Rearrange Gordon: `r = D₁/P₀ + g` — required return = forward dividend yield + growth. Applied to the whole index, this gives the market-implied cost of equity; subtracting the risk-free rate gives the **implied equity risk premium**, a forward-looking alternative to historical-average ERP (Damodaran's method).

### Q10. What is the biggest practical weakness of the DDM?
**A.** Extreme sensitivity to the `(r − g)` denominator. When `r` and `g` are close, the denominator is a small difference of large numbers, so tiny input changes swing value dramatically. Always run an r–g sensitivity table, and be suspicious of any DDM where `g` is within a point or two of `r`.

### Q11. Why does a high P/E only make sense when ROE > r?
**A.** Justified forward P/E = `payout/(r − g)` = `(1 − b)/(r − b·ROE)`. If ROE = r, reinvestment earns exactly the required return, adding no value, and P/E collapses to `1/r` regardless of growth. Only when **ROE > r** does retaining and growing create value and justify a premium multiple. Growth without excess returns is value-neutral.

### Q12. Why do you use D₁ (not D₀) in the Gordon numerator?
**A.** Valuation is forward-looking: `P₀` is the PV of dividends received *starting one period out*. `D₀` has already been paid and isn't part of the future stream. If given the trailing `D₀`, gross it up: `D₁ = D₀(1+g)`.

---

## Numerical problems

### Q13. Basic Gordon.
Divis Ltd just paid `D₀ = ₹6.00`, expected to grow 5% forever; cost of equity 11%. Value the share.

**Solution.**
`D₁ = 6.00 × 1.05 = ₹6.30`
`P₀ = D₁/(r − g) = 6.30/(0.11 − 0.05) = 6.30/0.06 = ₹105.00`

**Check (reverse):** `r = 6.30/105 + 0.05 = 0.06 + 0.05 = 0.11` ✓

### Q14. Sustainable growth and consistency.
A firm has ROE = 15% and pays out 40% of earnings. Next-year EPS = ₹20, cost of equity 12%. Find g, D₁, and value.

**Solution.**
Retention `b = 1 − 0.40 = 0.60`; `g = b × ROE = 0.60 × 0.15 = 0.09 = 9%`
`D₁ = EPS₁ × payout = 20 × 0.40 = ₹8.00`
`P₀ = 8.00/(0.12 − 0.09) = 8.00/0.03 = ₹266.67`

**Check (justified P/E):** `P₀/EPS₁ = payout/(r − g) = 0.40/0.03 = 13.33×`; `13.33 × 20 = ₹266.67` ✓

### Q15. Two-stage DDM (full working).
BharatCo just paid `D₀ = ₹4.00`. Growth 12% for 4 years, then 6% forever. `r = 10%`. Value it.

**Solution — explicit dividends:**

| Year | `Dₜ = 4·(1.12)ᵗ` | `1/(1.10)ᵗ` | PV |
|---|---|---|---|
| 1 | 4.4800 | 0.90909 | 4.0727 |
| 2 | 5.0176 | 0.82645 | 4.1468 |
| 3 | 5.6197 | 0.75131 | 4.2222 |
| 4 | 6.2941 | 0.68301 | 4.2989 |

Sum of PV (explicit) = 4.0727 + 4.1468 + 4.2222 + 4.2989 = **₹16.741**

**Terminal value at end of year 4:**
`D₅ = 6.2941 × 1.06 = 6.6717`
`TV₄ = 6.6717/(0.10 − 0.06) = 6.6717/0.04 = ₹166.79`
`PV(TV₄) = 166.79 × 0.68301 = ₹113.92`

**Total:** `P₀ = 16.741 + 113.92 = ₹130.66`

**Checks:** TV is 87% of value (113.92/130.66) — reasonable for a low-`r`, moderate-`g` case. Off-by-one: `D₅` in numerator, discounted by `(1.10)⁴`. ✓ `r > g` (10% > 6%). ✓

### Q16. H-model.
NeoCo just paid `D₀ = ₹2.50`. Growth 18% now, fading linearly to 6% over 8 years; `r = 12%`. Value it.

**Solution.**
`2H = 8 → H = 4`
Stable term: `2.50 × 1.06/(0.12 − 0.06) = 2.65/0.06 = ₹44.167`
Premium term: `2.50 × 4 × (0.18 − 0.06)/0.06 = 2.50 × 4 × 0.12/0.06 = 1.20/0.06 = ₹20.00`
`P₀ = 44.167 + 20.00 = ₹64.17`

**Check:** Value lies above the pure-stable Gordon of ₹44.17 (as it must, since growth exceeds 6% during the fade). ✓

### Q17. Cost of equity from price (reverse DDM).
A stock trades at ₹250, pays `D₀ = ₹10`, dividends grow 7% forever. What return are you earning?

**Solution.**
`D₁ = 10 × 1.07 = ₹10.70`
`r = D₁/P₀ + g = 10.70/250 + 0.07 = 0.0428 + 0.07 = 0.1128 = 11.28%`

**Check:** `P₀ = 10.70/(0.1128 − 0.07) = 10.70/0.0428 = ₹250.00` ✓

### Q18. Preferred / zero-growth.
A preferred share pays a fixed ₹9 dividend forever; required return 7.5%. Value it.

**Solution.** `P₀ = D/r = 9/0.075 = ₹120.00`. (Gordon with `g = 0`.)

### Q19. Implied equity risk premium at the index level.
An index is at 24,000 with forward dividend of 720 points; long-run growth 6%; 10-year bond yield 7.2%. Find the implied cost of equity and ERP.

**Solution.**
Forward yield = 720/24,000 = 3.0%
`r = 0.030 + 0.060 = 0.090 = 9.0%`
`ERP = r − r_f = 9.0% − 7.2% = 1.8%`

**Interpretation:** a compressed 1.8% premium implies an expensive market or optimistic growth.

### Q20. Bank valuation via DDM with sustainable growth.
A bank earns ROE = 14%, retains 45% of earnings, next-year EPS = ₹50, cost of equity 13%. Value the equity per share and state the justified P/E.

**Solution.**
`g = 0.45 × 0.14 = 0.063 = 6.3%`
`D₁ = 50 × (1 − 0.45) = 50 × 0.55 = ₹27.50`
`P₀ = 27.50/(0.13 − 0.063) = 27.50/0.067 = ₹410.45`
Justified forward P/E = `payout/(r − g) = 0.55/0.067 = 8.21×`; `8.21 × 50 = ₹410.45` ✓

**Why DDM here:** for a bank, FCFF/EV multiples are meaningless (debt is operating raw material); regulatory-capital-constrained dividends are the cleanest shareholder cash flow.

### Q21. Sensitivity trap illustration.
Using Q13 (`D₁ = 6.30`, `r = 11%`, `g = 5%`, `P₀ = ₹105`), show the value if growth rises just 1% to 6%.

**Solution.**
`P₀ = 6.30/(0.11 − 0.06) = 6.30/0.05 = ₹126.00`
A 1-point change in `g` raised value from ₹105 to ₹126 — **+20%**. This is the `(r − g)`-denominator sensitivity that makes DDM outputs fragile and mandates a sensitivity table.

### Q22. DDM vs FCFE convergence.
A firm has FCFE per share of ₹12 next year, all of which it pays as dividends; growth 4%, `r = 10%`. Value it both ways.

**Solution.**
DDM: `P₀ = D₁/(r − g) = 12/(0.10 − 0.04) = 12/0.06 = ₹200.00`
FCFE: `P₀ = FCFE₁/(r − g) = 12/0.06 = ₹200.00`

**Point:** when payout = FCFE (dividends = capacity), the two models are identical. They diverge only when the firm retains or over-distributes relative to FCFE — and then FCFE is the more reliable measure of value because it reflects capacity, not discretionary policy.
