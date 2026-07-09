# Q&A — Free Cash Flow: FCFF vs FCFE

A mixed bank of theory and numerical questions. Theory answers include a model answer plus a crisp "say it in an interview" line. Numerical answers are fully worked and self-verified.

---

## Theory

### Q1. What is free cash flow, and why do we value it instead of net income or dividends?

**Model answer.** Free cash flow is the cash a business generates that is genuinely available to distribute to its capital providers *after* it has funded everything needed to keep operating and growing — tax, capex, and working capital. We value cash rather than net income because value is the present value of *cash* — cash is what you can actually distribute or reinvest, whereas accounting profit is distorted by non-cash items (depreciation) and ignores real cash needs (capex, working capital). We prefer FCF to dividends because dividends are a *policy choice* — a firm can pay less than it could afford (building cash) or more (via debt); FCF measures *capacity* to pay, which is what drives value.

**Interview line:** "We discount cash the business can actually distribute, not accounting profit and not a discretionary dividend policy."

---

### Q2. Distinguish FCFF from FCFE across every dimension that matters.

**Model answer.**

| | FCFF | FCFE |
|---|------|------|
| Available to | Debt + equity | Equity only |
| Levered? | Unlevered | Levered |
| Interest | Excluded | Deducted (after-tax) |
| Net borrowing | Not included | Added |
| Discount rate | WACC | Cost of equity |
| DCF output | Enterprise Value | Equity Value |

FCFF is the cash the operating business throws off *before* the debt-vs-equity split; FCFE is what's left for shareholders *after* lenders are served. The link is **FCFE = FCFF − after-tax interest + net borrowing.**

**Interview line:** "FCFF is unlevered firm cash discounted at WACC to get EV; FCFE is levered equity cash discounted at cost of equity to get equity value directly."

---

### Q3. Why does the FCFF build tax EBIT at the full rate (EBIT×(1−t)) rather than use the firm's actual tax bill?

**Model answer.** FCFF must be *financing-neutral* — the cash the operations produce regardless of how the firm is funded. A levered firm's actual tax bill is *lower* because interest is tax-deductible (the interest tax shield). If we used the actual, lower tax, we'd be smuggling a financing benefit into the cash flow. So we tax EBIT *as if the firm were all-equity* — EBIT×(1−t), the "unlevered" tax — and capture the shield separately, inside WACC, via the after-tax cost of debt Kd×(1−t). The rule: put the tax shield in *one* place, and in an FCFF/WACC model that place is WACC.

**Interview line:** "We tax EBIT unlevered so FCFF is financing-neutral; the interest tax shield lives in WACC, not in the cash flow."

---

### Q4. Why must FCFF be discounted at WACC and FCFE at cost of equity?

**Model answer.** A discount rate must be the required return of exactly the claimants who receive the cash flow. FCFF is available to *all* providers — debt and equity — so it's discounted at their blended required return, WACC, giving the value of the whole firm (Enterprise Value). FCFE belongs to equity alone, so it's discounted at equity's required return, Kₑ, giving equity value directly. Mismatching them — say FCFF at Kₑ — values firm-wide cash as if it all accrued to equity, at the wrong rate.

**Interview line:** "The rate has to match the claimant: FCFF to WACC to EV; FCFE to cost of equity to equity value."

---

### Q5. Walk me through getting from Enterprise Value to value per share.

**Model answer.** Start from Enterprise Value (the output of an FCFF/WACC DCF). Subtract total debt, subtract preferred stock, subtract minority (non-controlling) interest, subtract other debt-like claims such as unfunded pensions if not already in debt. Add back cash and equivalents and any non-operating assets or investments, because those aren't captured in operating FCFF. That gives common equity value. Divide by *diluted* shares outstanding to get value per share.

**Interview line:** "Equity equals EV minus net debt minus minorities minus preferred plus non-operating assets, then divide by diluted shares."

---

### Q6. Why do we add cash back in the EV-to-equity bridge?

**Model answer.** FCFF is built from *operating* earnings (EBIT), so it never captures the interest income the firm earns on its cash balance — cash is a *non-operating* asset that sits outside Enterprise Value. Since equity holders own that cash, we add it back when bridging from EV to equity. (Strictly, only *excess* cash — operating cash needed to run day-to-day may be treated as operating.)

**Interview line:** "Cash is a non-operating asset EV doesn't capture, so it's added in the bridge to equity."

---

### Q7. When is FCFE the right choice over FCFF?

**Model answer.** For **financial institutions** — banks, insurers — where debt is raw material rather than just financing, interest is part of core operations, and a clean unlevered FCFF and a WACC are hard to define. Also when **leverage is stable** and you want equity value directly, or when the equity cash flow is the natural focus. For most non-financial firms, FCFF/WACC is the default because it's robust to *changing* capital structure — FCFE gets volatile when leverage shifts.

**Interview line:** "FCFE for banks and financials, or when leverage is stable; FCFF everywhere else because it's leverage-robust."

---

### Q8. If a company increases its leverage, what happens to FCFF and FCFE?

**Model answer.** FCFF is *unchanged* — it's unlevered, computed before financing; the operations didn't change, so neither did firm cash flow. FCFE *does* change: higher debt means more after-tax interest paid out, which reduces ongoing FCFE, though the act of drawing the new debt adds cash in the year it's raised (via net borrowing). Over time, higher leverage makes FCFE larger in absolute distribution terms but more volatile and riskier — which is also why the cost of equity rises with leverage. This asymmetry is the core reason FCFF is preferred when capital structure is expected to move.

**Interview line:** "FCFF doesn't move — it's unlevered; FCFE falls on higher interest but rises with new borrowing, and gets more volatile."

---

### Q9. What does it mean to "normalise" free cash flow, and name five common adjustments.

**Model answer.** Normalising means adjusting reported cash flow to reflect the *sustainable, ongoing* economics of the business, stripping out noise and one-offs so the DCF isn't built on a distorted base year. Five common adjustments: (1) remove non-recurring items — restructuring, litigation, asset-sale gains, write-downs; (2) normalise capex toward a maintenance/sustainable level, ensuring it supports assumed growth (capex ≥ D&A for a grower); (3) normalise working capital changes to a sustainable % of revenue; (4) use a normalised marginal tax rate rather than a distorted single-year rate; (5) treat stock-based comp as a real cost — don't add it back while ignoring dilution. Every adjustment must be internally consistent, including its tax effect.

**Interview line:** "Normalising strips one-offs and distortions so the DCF base reflects run-rate economics — and every adjustment must be tax-consistent."

---

### Q10. In the terminal value, why can't capex just equal depreciation while the firm grows forever?

**Model answer.** Perpetual growth requires perpetual reinvestment — you can't grow revenue and profits forever without adding assets and working capital. If terminal capex merely equals D&A (just replacing what wears out) and there's no incremental working capital, you've assumed *growth for free*, which massively inflates terminal value. In steady state, reinvestment must be consistent with growth via **reinvestment rate = g ÷ ROIC.** Also, terminal g can never exceed the long-run growth rate of the economy, or the firm eventually becomes larger than the economy.

**Interview line:** "Perpetual growth needs perpetual reinvestment — terminal reinvestment must equal g over ROIC, and g can't beat GDP."

---

### Q11. Why should FCFF computed four different ways (from EBIT, EBITDA, net income, CFO) give the same answer?

**Model answer.** Because they're algebraic rearrangements of one identity, not four different concepts. EBIT, EBITDA, net income, and CFO are just different lines on the same financial statements; each build adds back or removes exactly the items that separate its starting point from unlevered operating cash flow. If the four don't tie, there's a sign error or a double-count — which is exactly why analysts use the cross-check as a debugging tool.

**Interview line:** "They're the same number reached from different lines; if they don't tie, I've got a sign error to hunt."

---

### Q12. What is the single biggest reason a DCF gives a nonsensical value, in your experience?

**Model answer.** Terminal value abuse — either an aggressive terminal growth rate, or terminal cash flows that assume growth without funding the reinvestment for it, or a base-year cash flow that wasn't normalised and then gets grown to perpetuity. Since terminal value is typically 60–80% of EV, small errors there swamp everything in the explicit forecast. The fix: normalise the base, tie terminal reinvestment to g/ROIC, cap g at long-run GDP, and cross-check the implied exit multiple against comparables.

**Interview line:** "Terminal value — it's most of the EV, so an un-normalised base or free-growth assumption there breaks the whole model."

---

## Numerical

### Q13. Build FCFF from EBIT and confirm it from net income.

Given (₹ cr): EBIT = 250, tax = 30%, D&A = 40, Capex = 55, ΔNWC = +15, Interest = 20.

**Solution.**
NOPAT = 250 × (1 − 0.30) = 250 × 0.70 = 175.
FCFF (from EBIT) = 175 + 40 − 55 − 15 = **145.**

Cross-check from net income:
NI = (EBIT − Int)×(1−t) = (250 − 20)×0.70 = 230 × 0.70 = 161.
After-tax interest = 20 × 0.70 = 14.
FCFF = NI + Int(1−t) + D&A − Capex − ΔNWC = 161 + 14 + 40 − 55 − 15 = **145.** ✓

**FCFF = ₹145 cr**, confirmed both ways.

---

### Q14. Build FCFF starting from EBITDA (the tax-shield version).

Given (₹ cr): EBITDA = 300, D&A = 50, tax = 25%, Capex = 80, ΔNWC = +20.

**Solution.**
FCFF = EBITDA×(1−t) + t×D&A − Capex − ΔNWC
= 300 × 0.75 + 0.25 × 50 − 80 − 20
= 225 + 12.5 − 80 − 20 = **137.5.**

Verify via EBIT: EBIT = 300 − 50 = 250. NOPAT = 250 × 0.75 = 187.5.
FCFF = 187.5 + 50 − 80 − 20 = **137.5.** ✓

**FCFF = ₹137.5 cr.** The +12.5 (= t×D&A) is the depreciation tax shield you must add when starting from EBITDA.

---

### Q15. Bridge FCFF to FCFE.

Given (₹ cr): FCFF = 145, Interest = 20, tax = 30%, new debt raised = 30, debt repaid = 10.

**Solution.**
After-tax interest = 20 × 0.70 = 14.
Net borrowing = 30 − 10 = 20.
FCFE = FCFF − Int(1−t) + Net borrowing = 145 − 14 + 20 = **151.**

Here FCFE (151) > FCFF (145) because net borrowing (20) exceeded after-tax interest (14) — the firm drew more new debt than the interest it paid, so extra cash reached equity this year.

**FCFE = ₹151 cr.**

---

### Q16. Build FCFE directly from net income and confirm via CFO.

Given (₹ cr): NI = 120, D&A = 45, Capex = 60, ΔNWC = +25, new debt = 35, debt repaid = 20.

**Solution.**
Net borrowing = 35 − 20 = 15.
FCFE (from NI) = NI + D&A − Capex − ΔNWC + Net borrowing
= 120 + 45 − 60 − 25 + 15 = **95.**

Confirm via CFO. CFO = NI + D&A − ΔNWC = 120 + 45 − 25 = 140.
FCFE = CFO − Capex + Net borrowing = 140 − 60 + 15 = **95.** ✓

**FCFE = ₹95 cr.**

---

### Q17. Full FCFF DCF to Enterprise Value.

Given: FCFF forecast (₹ cr) Y1–Y4 = 90, 100, 108, 115; WACC = 11%; terminal g = 3%.
Compute EV.

**Solution.**
TV₄ = FCFF₄ × (1+g)/(WACC−g) = 115 × 1.03 / (0.11 − 0.03) = 118.45 / 0.08 = **1,480.625.**

Discount factors at 11%: Y1 = 1/1.11 = 0.9009; Y2 = 1/1.11² = 0.8116; Y3 = 0.7312; Y4 = 0.6587.

| Year | FCFF | DF | PV |
|------|------|-----|-----|
| 1 | 90 | 0.9009 | 81.08 |
| 2 | 100 | 0.8116 | 81.16 |
| 3 | 108 | 0.7312 | 78.97 |
| 4 | 115 | 0.6587 | 75.75 |
| | | Sum | 316.96 |

PV(TV) = 1,480.625 × 0.6587 = 975.29.

**EV = 316.96 + 975.29 = ₹1,292.25 cr.**

*Check:* TV share = 975.29 / 1,292.25 = 75.5% — within the normal 60–80% band.

---

### Q18. Continue Q17: bridge to value per share.

Given (₹ cr): Total debt = 350, Cash = 60, Minority interest = 15, Preferred = 25; diluted shares = 80 cr.

**Solution.**

| Line | ₹ cr |
|------|------|
| Enterprise Value | 1,292.25 |
| − Total debt | (350.00) |
| − Minority interest | (15.00) |
| − Preferred | (25.00) |
| + Cash | 60.00 |
| **= Equity Value** | **962.25** |

Value per share = 962.25 / 80 = **₹12.03.**

(Net debt here = 350 − 60 = 290; equity = 1,292.25 − 290 − 15 − 25 = 962.25. ✓)

---

### Q19. Reconciliation: show FCFF/WACC and FCFE/Kₑ give the same equity value.

Given: FCFF₁ = ₹120 cr, g = 4%, WACC = 12%. Debt = ₹500 cr, Cash = 0, Kd(pre-tax) = 8%, tax = 25%, leverage held constant.

**Solution — Route A (FCFF/WACC):**
EV = 120 / (0.12 − 0.04) = 120 / 0.08 = 1,500.
Equity = EV − net debt = 1,500 − 500 = **₹1,000 cr.**

**Route B (FCFE/Kₑ):**
Interest = 500 × 0.08 = 40; after-tax = 40 × 0.75 = 30.
Net borrowing (debt grows at g) = 500 × 0.04 = 20.
FCFE₁ = 120 − 30 + 20 = 110.

Derive Kₑ from WACC. V = D + E = 500 + 1,000 = 1,500. E/V = 0.6667, D/V = 0.3333.
0.12 = Kₑ×0.6667 + 0.08×0.75×0.3333 = 0.6667 Kₑ + 0.06×0.3333 = 0.6667 Kₑ + 0.02.
Kₑ = (0.12 − 0.02)/0.6667 = 0.10/0.6667 = **0.15 = 15%.**

Equity = FCFE₁/(Kₑ − g) = 110 / (0.15 − 0.04) = 110 / 0.11 = **₹1,000 cr.** ✓

**Both routes give ₹1,000 cr** — they must, because they value the same equity from opposite sides of the capital structure.

---

### Q20. Quick mental-math drill (interview-speed).

EBIT = 400, tax = 25%, D&A = 80, Capex = 90, ΔNWC = −10 (working capital *fell*). FCFF?

**Solution.**
NOPAT = 400 × 0.75 = 300.
A *fall* in NWC releases cash, so − ΔNWC = − (−10) = +10.
FCFF = 300 + 80 − 90 + 10 = **380.**

Trap check: the negative ΔNWC is a *source* of cash — subtracting a negative adds it. **FCFF = ₹380 cr.**

---

### Q21. Normalisation problem.

Reported EBIT = 500 includes a one-time ₹60 gain on sale of a division and a ₹30 non-recurring impairment. Reported tax rate 15% reflects one-off credits; marginal rate is 25%. D&A = 70; reported capex = 40 (management deferred maintenance; sustainable ≈ 75); reported ΔNWC = −50 (one-off receivables collection; sustainable ≈ +20). Compute *normalised* FCFF and compare to the naive reported FCFF.

**Solution.**
Normalised EBIT = 500 − 60 (strip gain) + 30 (add back impairment) = 470.
Normalised FCFF = 470 × (1 − 0.25) + 70 − 75 − 20 = 352.5 + 70 − 75 − 20 = **327.5.**

Naive reported FCFF = 500 × (1 − 0.15) + 70 − 40 − (−50) = 425 + 70 − 40 + 50 = **505.**

The reported figure (₹505 cr) overstates sustainable cash flow by **₹177.5 cr (54%)** — it banks a one-off gain, a favourable one-off tax rate, deferred capex, and a one-time working-capital release. Feeding ₹505 into a terminal value would grossly overvalue the firm; the defensible base is **₹327.5 cr.**

---

### Q22. FCFF vs FCFE sensitivity to a debt repayment.

A firm has FCFF = ₹200 cr, interest = ₹40 cr, tax = 25%. Case A: it raises ₹50 cr net new debt. Case B: it repays ₹60 cr of debt (no new borrowing). Compute FCFE in each case and explain.

**Solution.**
After-tax interest = 40 × 0.75 = 30.

Case A: Net borrowing = +50. FCFE = 200 − 30 + 50 = **220.**
Case B: Net borrowing = −60. FCFE = 200 − 30 − 60 = **110.**

FCFF is identical in both cases (₹200 cr) — it's unlevered and doesn't care about financing. But FCFE swings from ₹220 cr to ₹110 cr purely on debt flows: drawing debt puts cash in equity's hands this year; repaying it takes cash away. This is exactly why FCFE is volatile under changing leverage and FCFF is the leverage-robust choice.

**FCFE: Case A = ₹220 cr, Case B = ₹110 cr; FCFF = ₹200 cr in both.**
