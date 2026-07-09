# Q&A — Common Valuation Mistakes & Interview Traps

A mix of theory (with model answers and "how to say it in an interview") and fully worked numerical problems. Every number is self-verified and reconciles.

---

## THEORY

### Q1. What is the single most common catastrophic error in a DCF, and how do you avoid it?

**Model answer.** Mismatching the cash flow and the discount rate — specifically, discounting unlevered free cash flow (FCFF) at the cost of equity, or levered free cash flow (FCFE) at WACC. Value is always *someone's* value: FCFF belongs to all capital providers, so it must be discounted at the blended rate (WACC); FCFE belongs only to equity, so it is discounted at the cost of equity. Avoid it by naming the claimant *first*, then choosing the matching rate.

**How to say it:** *"Name the claimant, then pick the rate. FCFF to everyone means WACC; FCFE to equity means cost of equity. Cross them and you're 30% wrong before any other assumption."*

---

### Q2. On how many axes must cash flow and discount rate be consistent?

**Model answer.** Four. (1) **Claimants** — firm-wide FCFF↔WACC vs equity-only FCFE↔Ke. (2) **Financing treatment** — the interest tax shield lives in the after-tax cost of debt inside WACC, so FCFF must be pre-interest and taxed on EBIT, not EBT. (3) **Inflation** — nominal cash flows with a nominal rate, real with a real rate. (4) **Currency/tax** — cash flows and the discount rate must be built on the same currency's risk-free rate and both post-tax.

---

### Q3. Walk me through how you get from enterprise value to equity value, and why each item moves the way it does.

**Model answer.** Enterprise value is the operating business's value to *all* claimants. To reach equity: **subtract** senior/parallel claims — net debt (total debt minus excess cash), minority interest, preferred stock, and debt-like items such as an underfunded pension — and **add** things equity owns that aren't inside operating EV, namely investments in associates and non-operating assets. Divide the result by fully diluted shares.

- Debt/preferred/pension are *senior* claims paid before equity → subtract.
- Minority interest is the outsiders' slice of a consolidated sub whose 100% is in EV → subtract.
- Cash isn't part of the operating business and belongs to equity → add (it lowers net debt).
- Associates are equity-method — their value was never in operating EV → add.

**How to say it:** *"Subtract everyone senior to equity, add back what equity separately owns, divide by diluted shares."*

---

### Q4. Why do you subtract minority interest — but include it when computing EV multiples?

**Model answer.** Consolidation puts 100% of a controlled sub's revenue, EBITDA, and value into the parent's financials, but the parent's shareholders own only their percentage. When bridging EV to *parent equity*, you subtract minority interest to remove the outsiders' slice. When computing a *consolidated* multiple like EV/EBITDA, the EBITDA denominator is 100% consolidated, so EV in the numerator must also reflect 100% — meaning minority interest is *added* into EV. Same item, opposite direction, depending on whether you're building a multiple or bridging to equity.

---

### Q5. Why do you *add* associates in the bridge, and what double-count must you watch for?

**Model answer.** Associates (20–50% ownership, significant influence, no control) are equity-method: only the parent's *share of profit* flows into net income, and none of the associate's revenue or EBITDA is consolidated. So the associate's value is not in the operating enterprise value — you add it separately (market value if listed, else carrying value or a separate valuation). The double-count trap: in an FCFE model the equity-method income is *already* in net income and hence in FCFE. If you keep that income *and* also add the stake, you count it twice. Fix: strip the equity-method income from FCF, then add the stake once.

---

### Q6. Terminal value is usually 60–80% of EV. What four disciplines keep it honest?

**Model answer.** (1) **g ≤ long-run nominal GDP** — a firm can't outgrow the economy forever. (2) **g comfortably < WACC** — as g→WACC, TV→∞. (3) **Reinvestment must fund growth** — reinvestment rate = g/ROIC, so you can't assume growth for free. (4) **Cross-check the two methods** — back out the implied exit multiple from a Gordon TV and the implied g from an exit multiple; if either is absurd, revisit. Also normalize the terminal year to a steady state (capex ≈ D&A, margins normalized).

---

### Q7. Explain the circularity in WACC and three legitimate ways to handle it.

**Model answer.** WACC needs *market-value* equity weights, but equity value is exactly what the DCF computes — so the input depends on the output. Resolutions: (1) **target capital structure** — use a stable long-run D/(D+E) (industry median or management target) so WACC doesn't swing with the share price; (2) **iterate** — enable iterative calculation and let WACC and equity value converge; (3) **APV** — avoid WACC entirely: value the firm unlevered and add the PV of tax shields separately, ideal when leverage changes (LBOs). Never use book-value weights — book equity is an accounting residual, not a required return.

---

### Q8. Your model outputs ₹1,247.63 per share. Defend or reject that precision.

**Model answer.** Reject it. WACC and terminal growth are point estimates with at least ~1% and ~0.5% of uncertainty; small changes swing output by tens of percent. Honest practice is a *range* with a WACC×g sensitivity table, rounded to a resolution consistent with input error, and triangulated against trading comps, transaction comps, and (in IB) an LBO floor — a "football field," not a single decimal-perfect number. False precision signals you don't understand your own model's error bars.

---

### Q9. Where does the interest tax shield belong, and what happens if you misplace it?

**Model answer.** In the *discount rate* — inside WACC via the after-tax cost of debt, Kd×(1−t). That's why FCFF is built by taxing **EBIT** to get NOPAT, not by taxing EBT. If you tax EBT (which is after interest), the shield enters the cash flow *and* WACC still contains it — a double count that overstates value. Alternatively, use APV: value unlevered, then add the PV of tax shields once. Either way, count the shield exactly once.

---

### Q10. List the classic double-counts and the one-line fix for each.

**Model answer.**
- **Tax shield:** taxing EBT in FCFF + after-tax Kd in WACC → tax EBIT instead.
- **Excess cash:** interest income in FCF + cash added in bridge → strip the interest income first.
- **Associates:** equity-method income in NI + stake added in bridge → strip the income first.
- **Synergies:** in projected costs + as a separate value line → count once.
- **Leases (IFRS-16):** ROU depreciation/interest in P&L + lease liability in bridge → add the lease items back to EBIT if treating the liability as debt.
- **NOLs:** lower cash taxes in FCF + separate DTA add → model once.

**Rule:** for every non-operating asset you add, make sure its income is *out* of your cash flow.

---

### Q11. Basic or diluted shares — and how do you compute diluted?

**Model answer.** Fully diluted, always — basic overstates per-share value by ignoring in-the-money options, RSUs, warrants, and convertibles. Use the **treasury stock method** for options: net new shares = N − (N×K)/P, where the company is assumed to use option exercise proceeds (N×K) to buy back shares at price P. Use the **if-converted method** for convertibles (add the conversion shares, remove the related interest). Sum across all in-the-money instruments to get the diluted count.

---

### Q12. "I raise terminal growth from 2% to 3%." Reason through the effect out loud.

**Model answer.** The denominator (WACC − g) shrinks. At WACC = 10%, it goes from 8% to 7% — TV rises by roughly 8/7 − 1 ≈ 14% before discounting. Because TV is most of EV, equity value jumps materially. The key insight is *convexity*: the closer g gets to WACC, the more violent the move, because the denominator collapses toward zero. That's exactly why terminal growth must be handled with discipline and shown in a sensitivity table.

---

## NUMERICAL PROBLEMS

### Q13. FCFF/WACC mismatch — quantify the error.

**Problem.** FCFF next year = ₹120 crore, g = 3% forever. Weights: 55% equity, 45% debt. Ke = 13%, pre-tax Kd = 9%, tax = 30%. (a) Correct EV. (b) EV if you wrongly discount at Ke. (c) The error.

**Solution.**
- After-tax Kd = 9% × (1 − 0.30) = 6.3%
- WACC = 0.55×13% + 0.45×6.3% = 7.15% + 2.835% = **9.985% ≈ 9.99%**
- (a) Correct EV = 120 / (0.0999 − 0.03) = 120 / 0.0699 = **₹1,716.7 crore**
- (b) Wrong (at Ke): 120 / (0.13 − 0.03) = 120 / 0.10 = **₹1,200 crore**
- (c) Error = 1,716.7 − 1,200 = **₹516.7 crore understatement, ≈ 30.1%**

**Takeaway:** discounting firm-wide cash flow at the equity rate understates EV by ~30% here because Ke > WACC.

---

### Q14. Full EV-to-equity bridge with reconciliation.

**Problem.** EV = ₹8,000 crore. Total debt 2,000; cash 500; minority interest 400; preferred 300; underfunded pension 200; investment in associate (market value) 600; surplus non-operating land 100. Find equity value and verify the bridge reconciles.

**Solution.**
- Net debt = 2,000 − 500 = ₹1,500 crore

| Line | ₹ crore | Running |
|---|---|---|
| EV | 8,000 | 8,000 |
| − Net debt | (1,500) | 6,500 |
| − Minority interest | (400) | 6,100 |
| − Preferred | (300) | 5,800 |
| − Pension | (200) | 5,600 |
| + Associate | 600 | 6,200 |
| + Surplus land | 100 | 6,300 |
| **Equity value** | | **6,300** |

**Reconciliation:** 6,300 + 1,500 + 400 + 300 + 200 − 600 − 100 = 8,000 = EV. ✓

---

### Q15. Treasury stock method and per-share dilution.

**Problem.** Equity value = ₹6,300 crore. Basic shares = 120 crore. Options: 8 crore struck at ₹300; current share price ≈ ₹525. Compute diluted shares and per-share value, and the dilution impact vs basic.

**Solution.**
- Options in the money (₹525 > ₹300). Cash raised = 8 × ₹300 = ₹2,400 crore
- Shares repurchased = 2,400 / 525 = 4.571 crore
- Net new shares = 8 − 4.571 = 3.429 crore
- Diluted shares = 120 + 3.429 = **123.429 crore**
- Per share (diluted) = 6,300 / 123.429 = **₹51.04**
- Per share (basic) = 6,300 / 120 = ₹52.50
- Dilution impact = 52.50 − 51.04 = **₹1.46 (≈ 2.8%) lower**

---

### Q16. Terminal value — Gordon vs exit multiple with cross-checks.

**Problem.** Year-6 EBITDA = ₹700 crore, FCFF = ₹350 crore, WACC = 11%. (a) Gordon TV at g = 3.5%. (b) Implied exit multiple. (c) Exit-multiple TV at 8×. (d) Implied g from the 8× multiple.

**Solution.**
- (a) TV = 350 × 1.035 / (0.11 − 0.035) = 362.25 / 0.075 = **₹4,830 crore**
- (b) Implied multiple = 4,830 / 700 = **6.90× EV/EBITDA** (reasonable)
- (c) Exit TV = 8 × 700 = **₹5,600 crore**
- (d) Set 5,600 = 350(1+g)/(0.11 − g): 5,600(0.11 − g) = 350 + 350g → 616 − 5,600g = 350 + 350g → 266 = 5,950g → **g = 4.47%**

**Takeaway:** the 8× multiple implies ~4.5% perpetual growth — at the high end, worth justifying against long-run GDP.

---

### Q17. The "growth for free" trap — reinvestment consistency.

**Problem.** Terminal year: NOPAT = ₹400 crore, ROIC = 10%, assumed perpetual g = 4%. (a) What reinvestment does 4% growth require? (b) What is the *consistent* terminal FCFF? (c) If an analyst instead uses FCFF = ₹400 crore (zero net reinvestment) with WACC = 10% and g = 4%, by how much is TV overstated?

**Solution.**
- (a) Reinvestment rate = g/ROIC = 4%/10% = **40%**; reinvestment = 0.40 × 400 = ₹160 crore
- (b) Consistent FCFF = 400 − 160 = **₹240 crore**
- (c) Consistent TV = 240 × 1.04 / (0.10 − 0.04) = 249.6 / 0.06 = **₹4,160 crore**
  - "Growth for free" TV = 400 × 1.04 / 0.06 = 416 / 0.06 = **₹6,933 crore**
  - Overstatement = 6,933 − 4,160 = **₹2,773 crore (≈ 67% too high)**

**Takeaway:** assuming growth without funding it with reinvestment inflates terminal value by two-thirds here.

---

### Q18. Double-counting excess cash and associate income (strip-and-add).

**Problem.** FCFE = ₹250 crore includes ₹20 crore pre-tax interest income on ₹350 crore excess cash and ₹50 crore equity-method income from a 25% associate (stake market value ₹450 crore). g = 4%, Ke = 10%, tax = 30%. (a) The double-counted (wrong) equity value. (b) The correct strip-and-add value.

**Solution.**
- (a) *Wrong:* value FCFE = 250 / (0.10 − 0.04) = 250/0.06 = ₹4,166.7 crore, then also add cash 350 + associate 450 = **₹4,966.7 crore** (income counted twice).
- (b) *Correct — strip the non-operating income:*
  - After-tax interest income = 20 × (1 − 0.30) = ₹14 crore
  - Associate income = ₹50 crore
  - Core FCFE = 250 − 14 − 50 = ₹186 crore
  - Core equity value = 186 × 1.04 / (0.10 − 0.04) = 193.44 / 0.06 = ₹3,224 crore
  - Add assets once: + 350 cash + 450 associate = **₹4,024 crore**
- Difference = 4,966.7 − 4,024 = **₹942.7 crore (≈ 19%) overstatement** from double counting.

---

### Q19. Net debt with market value of debt.

**Problem.** Company has ₹1,000 crore face value of bonds trading at 92; ₹300 crore bank loans (floating, at par); cash ₹250 crore; short-term investments (excess) ₹150 crore. EV = ₹5,000 crore. Compute net debt and equity value.

**Solution.**
- Market value of bonds = 1,000 × 0.92 = ₹920 crore; loans at par = ₹300 crore → total debt (market) = ₹1,220 crore
- Cash + excess investments = 250 + 150 = ₹400 crore
- Net debt = 1,220 − 400 = **₹820 crore**
- Equity value = 5,000 − 820 = **₹4,180 crore**

**Note:** using face value (₹1,300 debt) would give net debt ₹900 and equity ₹4,100 — the market-value adjustment matters when bonds trade away from par.

---

### Q20. Circular WACC — target vs current weights.

**Problem.** Ke = 12%, pre-tax Kd = 8%, tax = 25%. Current market values: equity ₹6,000 crore, debt ₹4,000 crore. Industry target structure is 70% equity / 30% debt. Compute WACC under (a) current weights and (b) target weights, and explain which to use.

**Solution.**
- After-tax Kd = 8% × 0.75 = 6.0%
- (a) Current weights: E = 6,000/10,000 = 60%, D = 40%. WACC = 0.60×12% + 0.40×6% = 7.2% + 2.4% = **9.6%**
- (b) Target weights: WACC = 0.70×12% + 0.30×6% = 8.4% + 1.8% = **10.2%**

**Which to use:** the **target** (10.2%) for the DCF, because current market-value equity is itself the model's output (circularity) and swings with the share price. A stable target structure breaks the loop and gives a WACC you can defend through market noise.

---

### Q21. Minority interest in a consolidated multiple.

**Problem.** Parent owns 80% of a consolidated sub. Consolidated EBITDA = ₹900 crore. Parent equity market cap = ₹4,000 crore; net debt = ₹1,500 crore; minority interest (book/fair) = ₹500 crore; associate stake = ₹300 crore. Compute the correct EV/EBITDA multiple.

**Solution.**
- EV = market cap + net debt + minority interest − associates = 4,000 + 1,500 + 500 − 300 = **₹5,700 crore**
- EV/EBITDA = 5,700 / 900 = **6.33×**

**Why:** EBITDA is 100% consolidated, so EV must include minority interest (add) to match the numerator to the denominator; associates are excluded from consolidated EBITDA, so their value is removed from EV for the multiple.

---

### Q22. Nominal vs real mismatch — quantify.

**Problem.** Real FCFF next year = ₹100 crore growing at 2% real forever. Real discount rate = 6%; expected inflation = 4% (so nominal rate ≈ 10.24%, nominal g ≈ 6.08% via Fisher). (a) Correct value using real terms. (b) The error if you discount the *real* cash flow at the *nominal* rate.

**Solution.**
- (a) *Consistent (real):* Value = 100 / (0.06 − 0.02) = 100 / 0.04 = **₹2,500 crore**
- (b) *Mismatch — real CF at nominal rate:* 100 / (0.1024 − 0.02) = 100 / 0.0824 = **₹1,213.6 crore**
- Error = 2,500 − 1,213.6 = **₹1,286.4 crore understatement (≈ 51%)**

**Takeaway:** discounting real cash flows at a nominal rate roughly halves the value here — mixing inflation bases is a first-order error. Fix by matching: real↔real or nominal↔nominal.

---

### Q23 (bonus). Reconcile FCFF and FCFE numerically.

**Problem.** EBIT = ₹500, tax = 25%, D&A = ₹120, capex = ₹150, ΔNWC = ₹30, interest expense = ₹60, net borrowing = ₹40. Compute FCFF and FCFE two ways and confirm they reconcile.

**Solution.**
- NOPAT = 500 × 0.75 = ₹375
- FCFF = 375 + 120 − 150 − 30 = **₹315**
- FCFE (Route B, from FCFF) = FCFF − interest×(1−t) + net borrowing = 315 − 60×0.75 + 40 = 315 − 45 + 40 = **₹310**
- FCFE (Route A, from net income): Net income = (EBIT − interest)×(1−t) = (500 − 60)×0.75 = 440×0.75 = ₹330. FCFE = 330 + 120 − 150 − 30 + 40 = **₹310** ✓

Both routes give ₹310 — the reconciliation confirms the tax shield (interest × t = ₹15) is handled consistently: FCFE exceeds "FCFF − pre-tax interest + borrowing" precisely by that shield.
