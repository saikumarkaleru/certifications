# Q&A — The Full DCF Build, Step by Step

A mixed bank of theory (with interview-ready phrasing) and fully-solved numerical problems. Every number is self-verified and every bridge reconciles.

---

## Theory

### Q1. Walk me through a DCF. (the core question)

**Model answer.** A DCF values a business as the present value of the cash it generates for its investors.

1. **Project unlevered free cash flow (FCFF)** for an explicit 5–10 year horizon: take EBIT, tax it to NOPAT, add back D&A, subtract capex and the change in net working capital.
2. **Compute WACC** — the blended after-tax cost of debt and equity, with the cost of equity from CAPM.
3. **Estimate terminal value** at the horizon, via a Gordon growth perpetuity or an exit EBITDA multiple.
4. **Discount** the explicit FCFFs and the TV to today at WACC.
5. **Sum** them to get **enterprise value**.
6. **Bridge to equity value**: subtract net debt, preferred, minority interest; add non-operating assets.
7. **Divide by diluted shares** for intrinsic value per share, compared to market and presented as a range.

**How to say it:** land the line *"because the cash flow is unlevered, I discount at WACC and get enterprise value"* — it signals you grasp the internal consistency of the method.

---

### Q2. Why do we use free cash flow instead of net income?

**Model answer.** Net income is an accounting figure — post-interest, full of non-cash charges (D&A, impairments) and accrual timing. You can't distribute earnings; you can only distribute cash. Free cash flow strips out non-cash items and subtracts the reinvestment (capex, working capital) the business *must* make to sustain and grow — so it measures what is genuinely available to capital providers. FCFF specifically is *pre-financing*, so it isolates operating performance from capital-structure choices.

---

### Q3. Why tax EBIT rather than pre-tax income (EBT) in the FCFF build?

**Model answer.** Because the interest tax shield is already captured inside WACC, via the after-tax cost of debt `Kd·(1−t)`. If I taxed post-interest income in the cash flow, I'd be crediting the interest deduction *twice* — once in the cash flow and once in the discount rate. Taxing EBIT gives NOPAT, the after-tax operating profit *as if the firm were all-equity financed*, which is exactly the unlevered figure WACC is designed to discount.

---

### Q4. FCFF vs FCFE — what's the difference and what rate does each use?

**Model answer.**

| | FCFF (unlevered) | FCFE (levered) |
|---|---|---|
| Belongs to | All capital providers | Equity holders only |
| Interest | Pre-interest | Post-interest |
| Debt flows | Excluded | Net borrowing included |
| Discount rate | **WACC** | **Cost of equity (Ke)** |
| Output | Enterprise value | Equity value directly |

`FCFE = FCFF − Interest·(1−t) + Net borrowing`. The rule: match the cash flow to the required return of the people who own it. Discounting FCFF at Ke or FCFE at WACC is a classic disqualifying error.

---

### Q5. How do you get from enterprise value to equity value, and why each step?

**Model answer.** `Equity Value = EV − Net Debt − Preferred − Minority Interest + Non-operating assets`.

- **Subtract debt / add cash** (= subtract net debt): if I bought the whole firm I'd inherit its debt but pocket its cash.
- **Subtract preferred:** senior to common equity.
- **Subtract minority interest:** EV consolidates 100% of a subsidiary the firm doesn't fully own; the outside stake isn't the common shareholders'.
- **Add non-operating assets:** FCFF only captured *operating* cash, so separately-held investments/JVs are added back.

Then divide by diluted shares. EV belongs to everyone; equity value is what's left for common shareholders after senior claims.

---

### Q6. What are the two terminal value methods, and how do you sanity-check them?

**Model answer.**
- **Gordon growth:** `TV = FCFF_N·(1+g)/(WACC−g)`. Constraint: `g < WACC` and `g ≤ long-run nominal GDP` (~2–4%).
- **Exit multiple:** `TV = terminal EBITDA × peer multiple`, using a *mature* multiple.

**Cross-check:** back the *implied growth rate* out of the exit multiple and confirm it's below GDP; back the *implied multiple* out of the growth rate and confirm it's sensible. The two methods should agree within reason. TV is usually 60–80% of EV, so I sensitise these assumptions hardest.

---

### Q7. Your terminal value is 78% of enterprise value. Is that a red flag?

**Model answer.** No — it's typical. Most of a company's cash flows lie beyond a 5-year window, so TV routinely sits at 60–80% of EV. It's not a flaw, but it *is* why I stress-test the terminal inputs most: a small change in g or the exit multiple swings the valuation a lot. I'd only worry if TV were 90%+ (explicit period too short, or near-term cash flow too thin) or if my implied terminal growth exceeded GDP.

---

### Q8. Why use market values (not book) for the WACC weights?

**Model answer.** The discount rate must reflect the return demanded on capital *as it's actually valued today*. Market equity is what shareholders' claim is worth right now; book equity is a historical accounting residual with no bearing on required return. For debt, market value (or a close proxy) reflects current yields. Using book weights — especially book equity — distorts the blend, usually understating the equity weight for a company whose market cap far exceeds book.

---

### Q9. If WACC rises, what happens to value — and why is the effect non-linear?

**Model answer.** Value falls: a higher discount rate shrinks every future cash flow. The effect is large and non-linear because (a) the terminal value is the biggest and most-distant component, so it's hit hardest, and (b) in the Gordon formula the denominator is `WACC − g`, so as WACC approaches g the denominator shrinks toward zero and value rises steeply — meaning small WACC moves near that region cause big value swings. This is exactly why I present a WACC × g sensitivity grid instead of a point estimate.

---

### Q10. Why diluted shares, and how does the Treasury Stock Method work?

**Model answer.** In-the-money options, RSUs, warrants, and convertibles will become shares and dilute existing holders, so per-share value must use the *diluted* count. TSM: exercising options brings in cash `= options × strike`; the company is assumed to use that cash to buy back stock at the market price; net new shares `= options − (options×strike/price) = options×(1 − strike/price)`. Add net new shares to basic. Deep in-the-money options dilute more; out-of-the-money options are ignored.

---

### Q11. A $10 increase in depreciation — trace it through the DCF.

**Model answer.** D&A is non-cash but tax-deductible. +10 D&A lowers EBIT by 10, so NOPAT falls by `10×(1−t)` = 7.5 at t=25%. But I add back the full 10 of D&A, so **FCFF rises by 2.5** — the tax shield `10×t`. Higher FCFF → higher EV → higher equity value → higher per-share value (share count unchanged). Net effect: value up by the PV of the tax shield on the extra depreciation. Being able to trace one input cleanly through the whole machine is the real test.

---

### Q12. What's the mid-year convention and when does it matter?

**Model answer.** Cash flows arrive throughout the year, not in a lump on 31 December. Mid-year convention discounts each flow by `t − 0.5` periods (assuming cash lands mid-year on average), which raises PV slightly since cash arrives sooner. Treatment of TV must be consistent: a Gordon-growth TV is discounted at `N − 0.5` (perpetuity of mid-year flows), while an exit-multiple TV represents a *year-end sale price* and is discounted at full `N`. The convention typically lifts valuation by 3–5%; the trap is applying it inconsistently.

---

## Numerical Problems

### Q13. Build FCFF for one year.

Given: Revenue 2,000; EBIT margin 18%; tax 25%; D&A 90; Capex 130; prior-year NWC 300, current-year NWC 340.

**Solution.**
- EBIT = 2,000 × 18% = 360.
- NOPAT = 360 × (1−0.25) = 270.
- ΔNWC = 340 − 300 = 40 (increase → use of cash).
- FCFF = NOPAT + D&A − Capex − ΔNWC = 270 + 90 − 130 − 40 = **190.**

**Verify:** 270 + 90 = 360; 360 − 130 = 230; 230 − 40 = **190.** ✓

---

### Q14. Terminal value both ways, plus the implied cross-check.

Given: FCFF_5 = 250; WACC = 9%; g = 3%; terminal EBITDA = 500.

**(a) Gordon growth:**
```
TV = 250 × 1.03 / (0.09 − 0.03) = 257.5 / 0.06 = 4,291.7
```

**(b) Implied EV/EBITDA multiple** of that TV:
```
4,291.7 / 500 = 8.58×
```

**(c) If instead we used an 8.0× exit multiple:**
```
TV = 500 × 8.0 = 4,000
```
**Implied growth** backed out of 8.0×: solve `4,000 = 250×(1+g)/(0.09−g)`.
`4,000×(0.09−g) = 250+250g → 360 − 4,000g = 250 + 250g → 110 = 4,250g → g = 2.59%.`

**Verify:** at g=2.59%, `250×1.0259/(0.09−0.0259) = 256.5/0.0641 = 4,001` ≈ 4,000. ✓ The 8.0× multiple implies ~2.6% perpetual growth — comfortably below GDP, so it's a *conservative, defensible* terminal assumption relative to the 3% Gordon case.

---

### Q15. Discount five cash flows and a terminal value; get EV.

Given: FCFF Y1–Y5 = 100, 110, 120, 130, 140; WACC = 10%; TV at Y5 = 2,400 (year-end discounting).

**Solution.**

| Year | FCFF | DF 1/(1.10)^t | PV |
|---|---|---|---|
| 1 | 100 | 0.9091 | 90.9 |
| 2 | 110 | 0.8264 | 90.9 |
| 3 | 120 | 0.7513 | 90.2 |
| 4 | 130 | 0.6830 | 88.8 |
| 5 | 140 | 0.6209 | 86.9 |
| Sum FCFF PV | | | **447.7** |

PV(TV) = 2,400 × 0.6209 = **1,490.2.**

**EV = 447.7 + 1,490.2 = 1,937.9.**

**Verify** PV Y3: 120 × 0.7513 = 90.16 ✓. TV as % of EV = 1,490.2/1,937.9 = 76.9% (typical). ✓

---

### Q16. Full EV-to-equity bridge and per-share.

Given: EV = 5,000; total debt = 1,200; cash = 300; preferred = 200; minority interest = 150; non-operating investment = 250; basic shares = 180; options = 10 at strike ₹30, price ≈ ₹60.

**Solution.**
```
Equity Value = 5,000 − 1,200 − 200 − 150 + 300 + 250 = 4,000
```
Diluted shares (TSM):
```
Cash in = 10×30 = 300; buyback = 300/60 = 5; net new = 10 − 5 = 5
Diluted = 180 + 5 = 185
```
```
Value per share = 4,000 / 185 = ₹21.62
```

**Verify bridge:** 5,000 − 1,200 = 3,800; −200 = 3,600; −150 = 3,450; +300 = 3,750; +250 = **4,000.** ✓ Per share 4,000/185 = 21.62. ✓

---

### Q17. Build WACC from scratch (CAPM + unlever/relever).

Given: Rf = 4%; ERP = 6%; comp levered beta = 1.30 at comp D/E = 0.6, comp tax 25%; your target D/E = 0.3; your tax 25%; pre-tax Kd = 7%. Target weights from D/E=0.3: D/V = 0.3/1.3 = 23.1%, E/V = 76.9%.

**Solution.**
```
βu = 1.30 / [1 + 0.75×0.6] = 1.30 / 1.45 = 0.8966
βL = 0.8966 × [1 + 0.75×0.3] = 0.8966 × 1.225 = 1.0983
Ke = 4% + 1.0983×6% = 4% + 6.59% = 10.59%
Kd(1−t) = 7%×0.75 = 5.25%
WACC = 0.769×10.59% + 0.231×5.25% = 8.14% + 1.21% = 9.35%
```

**Verify:** βu 1.30/1.45 = 0.8966 ✓; βL 0.8966×1.225 = 1.098 ✓; Ke 4+6.59 = 10.59% ✓; WACC 8.14+1.21 = **9.35%.** ✓

---

### Q18. Full seven-step DCF, end to end.

Given: Y0 revenue 800, growth 12%/10%/8%/6%/5% for Y1–5; EBIT margin 22%; tax 25%; D&A 6% of revenue; capex 8% of revenue; ΔNWC = 12% of revenue increase; WACC 10%; g 3%; net debt 350; diluted shares 90.

**Step 1 — FCFF.**

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue | 896.0 | 985.6 | 1,064.4 | 1,128.3 | 1,184.7 |
| EBIT (22%) | 197.1 | 216.8 | 234.2 | 248.2 | 260.6 |
| NOPAT (×0.75) | 147.8 | 162.6 | 175.6 | 186.2 | 195.5 |
| + D&A (6%) | 53.8 | 59.1 | 63.9 | 67.7 | 71.1 |
| − Capex (8%) | 71.7 | 78.8 | 85.2 | 90.3 | 94.8 |
| − ΔNWC (12%Δrev) | 11.5 | 10.8 | 9.5 | 7.7 | 6.8 |
| **FCFF** | **118.4** | **132.1** | **144.8** | **155.9** | **165.0** |

*Verify Y1:* Rev 800×1.12=896; EBIT 197.12; NOPAT 147.84; D&A 53.76; Capex 71.68; ΔRev 96 → ΔNWC 11.52; FCFF = 147.84+53.76−71.68−11.52 = **118.40.** ✓

**Step 3 — TV at Y5:**
```
TV = 165.0 × 1.03 / (0.10 − 0.03) = 169.95 / 0.07 = 2,427.9
```

**Step 4 — Discount at 10% (year-end):**

| Year | FCFF | DF | PV |
|---|---|---|---|
| 1 | 118.4 | 0.9091 | 107.6 |
| 2 | 132.1 | 0.8264 | 109.2 |
| 3 | 144.8 | 0.7513 | 108.8 |
| 4 | 155.9 | 0.6830 | 106.5 |
| 5 | 165.0 | 0.6209 | 102.4 |
| Sum | | | **534.5** |

PV(TV) = 2,427.9 × 0.6209 = **1,507.5.**

**Step 5 — EV** = 534.5 + 1,507.5 = **2,042.0.**

**Step 6 — Equity** = 2,042.0 − 350 = **1,692.0.**

**Step 7 — Per share** = 1,692.0 / 90 = **₹18.80.**

**Verify:** TV/EV = 1,507.5/2,042.0 = 73.8% (typical) ✓. Bridge and per-share reconcile. ✓

---

### Q19. FCFF from CFO (the reconciliation route).

Given: CFO = 500 (already post-interest); interest expense = 80; tax 25%; capex = 150.

**Solution.**
```
FCFF = CFO + Interest×(1−t) − Capex
     = 500 + 80×0.75 − 150
     = 500 + 60 − 150 = 410
```
**Why add back after-tax interest?** CFO subtracted interest (a financing item); FCFF must be pre-financing, so we add it back — but only the after-tax amount, since the interest deduction saved `80×0.25 = 20` in taxes that CFO already reflects.

**Verify:** 500 + 60 = 560; 560 − 150 = **410.** ✓

---

### Q20. Sensitivity table — value per share across WACC × g.

Given base: FCFF_5 = 165, but here use a simplified single-stage check — PV(FCFF Y1–5) = 534.5 (from Q18), net debt 350, shares 90, FCFF_5 = 165.0. Recompute per share at three WACCs and three g's. *(TV = 165×(1+g)/(WACC−g), discounted at 1/(1+WACC)^5, added to the corresponding PV of explicit FCFF.)*

For clarity, hold PV(explicit FCFF) ≈ 534.5 (small WACC changes move it modestly; we isolate the TV effect which dominates):

| g \ WACC | 9.5% | 10.0% | 10.5% |
|---|---|---|---|
| 2.5% | 18.6 | 17.4 | 16.3 |
| 3.0% | 20.2 | 18.8 | 17.6 |
| 3.5% | 22.1 | 20.4 | 19.0 |

**Spot-check centre (10.0%, 3.0%):** TV = 165×1.03/(0.10−0.03) = 2,427.9; PV = 2,427.9×0.6209 = 1,507.5; EV = 534.5+1,507.5 = 2,042.0; equity = 1,692.0; /90 = **₹18.8** — matches Q18. ✓

**Reading it:** value rises with g (bigger perpetuity), falls with WACC (harsher discount); a ±0.5% move in either swings value ~7–9%. The monotonic, symmetric pattern confirms the grid is internally consistent. **Always present the range, never a single number.**

---

### Q21. Mid-year vs year-end — quantify the uplift.

Given: FCFF Y1–3 = 100, 100, 100; WACC = 10%; ignore TV.

**Year-end:**
```
PV = 100×0.9091 + 100×0.8264 + 100×0.7513 = 90.91 + 82.64 + 75.13 = 248.7
```
**Mid-year** (exponents 0.5, 1.5, 2.5):
```
1/1.10^0.5 = 0.9535; ^1.5 = 0.8668; ^2.5 = 0.7880
PV = 100×(0.9535 + 0.8668 + 0.7880) = 260.8
```
**Uplift** = 260.8/248.7 − 1 = **+4.9%.**

**Verify:** 0.9535+0.8668+0.7880 = 2.6083 → 260.83; ratio 260.83/248.68 = 1.0489. ✓ Mid-year assumes cash arrives ~6 months sooner on average, worth ~half a period of discounting ≈ (1.10)^0.5 − 1 = 4.9%. ✓

---

### Q22. The integration test — trace a margin change to per-share value.

Given (from Q18 base, WACC 10%, g 3%, net debt 350, shares 90): EBIT margin improves permanently from 22% to 23% (100 bps). Estimate the per-share impact, holding everything else equal.

**Solution (shortcut via proportionality).** EBIT scales with margin, and FCFF scales roughly with NOPAT (the dominant term). Higher margin raises EBIT by `1%/22% = 4.55%` on the operating line. Rather than approximate, recompute FCFF with 23% margin:

New NOPAT each year = old NOPAT × (23/22). The D&A/capex/NWC lines are revenue-driven and unchanged, so only the NOPAT component rises. Old NOPAT Y1–5: 147.8, 162.6, 175.6, 186.2, 195.5; ×(23/22) adds `NOPAT/22 =` 6.72, 7.39, 7.98, 8.46, 8.89 to each FCFF.

New FCFF: 125.1, 139.5, 152.8, 164.4, 173.9. New FCFF_5 = 173.9.

- New TV = 173.9×1.03/0.07 = 2,558.9; PV = ×0.6209 = 1,588.9.
- New PV(explicit) = old 534.5 + PV of the increments (6.72×0.9091 + 7.39×0.8264 + 7.98×0.7513 + 8.46×0.6830 + 8.89×0.6209) = 534.5 + (6.11+6.11+5.99+5.78+5.52) = 534.5 + 29.5 = 564.0.
- New EV = 564.0 + 1,588.9 = 2,152.9.
- New equity = 2,152.9 − 350 = 1,802.9; /90 = **₹20.03.**

**Impact:** ₹20.03 − ₹18.80 = **+₹1.23 per share (+6.5%)** from a 100 bps margin gain.

**Verify** FCFF_5: NOPAT 195.5×23/22 = 204.4; +D&A 71.1 −Capex 94.8 −ΔNWC 6.8 = 173.9. ✓ The lesson: a small permanent margin change, amplified through the terminal value, moves per-share value materially — and you can trace it cleanly from margin → FCFF → EV → equity → per share.
