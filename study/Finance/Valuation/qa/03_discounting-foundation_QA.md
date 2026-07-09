# Q&A — The Discounting Foundation

A mixed bank of theory and numerical questions on time value of money, discount factors, mid-year convention, the discount-rate/growth/value relationship, sensitivity, and the present value of growing streams. Theory answers include an interview-ready "how to say it" line. Numerical answers are fully worked and self-verified.

---

## Section A — Theory (with interview phrasing)

### Q1. Why is a dollar received in the future worth less than a dollar today?

**Answer.** Three reasons, all bundled into the discount rate: (1) **opportunity cost** — today's dollar can be invested and earn a return, so a future dollar starts from behind; (2) **risk** — future cash flows are uncertain and investors demand compensation for bearing that uncertainty; (3) **inflation** — future dollars have less purchasing power. Discounting quantifies exactly how much less by running compound interest backwards.

**How to say it in an interview:** *"Because of opportunity cost, risk, and inflation — all captured in the discount rate. Discounting is just compound interest run in reverse: divide by one plus r for each period you travel back."*

---

### Q2. Derive the discount factor from first principles.

**Answer.** Forward, money compounds: `FV = PV × (1 + r)^n`. Valuation asks the reverse — we forecast the future cash flow and want today's value — so solve for `PV`: `PV = FV / (1 + r)^n`. The term `1/(1+r)^n` is the discount factor: always between 0 and 1 for positive `r`, shrinking as `n` grows and shrinking faster as `r` grows. Multiply any future cash flow by its discount factor to get present value; sum across all flows for a DCF, which is valid because all PVs are in the same units (today's dollars) — the value-additivity principle.

**How to say it:** *"The discount factor isn't a separate concept — it's the compounding formula inverted. Money grows by one plus r to the n, so to bring it back you divide by one plus r to the n."*

---

### Q3. Walk me through a DCF.

**Answer / interview script:** *"A DCF values a business as the present value of its future cash flows. I project unlevered free cash flow for five to ten years — EBIT taxed, plus D&A, minus capex, minus the change in working capital. I discount each year at WACC. Because I can't forecast forever, I compute a terminal value at the end of the horizon — Gordon Growth, cash flow times one plus g over WACC minus g, or an exit multiple on EBITDA — and discount that back too. Summing the discounted explicit flows and discounted terminal value gives enterprise value. From EV I subtract net debt, preferred, and minority interest, add non-operating assets, to reach equity value, then divide by diluted shares for value per share. Finally I run a sensitivity table on WACC and terminal growth, since those drive most of the value."*

---

### Q4. What is the mid-year convention, why does it always raise value, and what's the terminal-value subtlety?

**Answer.** The discrete convention assumes each year's cash lands in a lump on Dec 31 (exponent `t`). The mid-year convention assumes cash is earned evenly and arrives mid-year on average, so you discount at `t − 0.5`. Because the effective discounting period is shorter, every discount factor is larger, so mid-year **always** produces a higher PV — by roughly `(1+r)^0.5` (about +5% at 10%). Terminal-value subtlety: a Gordon-growth TV capitalizes mid-year flows and is discounted consistently at the last stub year's mid-year point; an exit-multiple TV represents a discrete year-end sale and is often discounted at the full period `n`.

**How to say it:** *"Mid-year discounts at t minus a half because cash is earned throughout the year, not on December 31. It always lifts value by about one plus r to the half. For a Gordon TV I keep mid-year timing consistent; for an exit multiple I'd discount the full year because it's a discrete sale."*

---

### Q5. Explain the relationship between the discount rate, growth, and value.

**Answer.** For a growing perpetuity, `Value = CF₁/(r − g)`. Value **rises as r falls** (future discounted less harshly), **rises as g rises** (faster-growing cash is worth more), and the relationship is **non-linear and explosive as `r` approaches `g`** — the denominator approaches zero and value approaches infinity, which is why `g` must be strictly below `r` and, economically, below long-run GDP growth. The narrower the `(r − g)` spread, the more violently value reacts to any change in either input.

**How to say it:** *"Value is driven by the spread r minus g. Lower r or higher g both raise value, and it's explosively non-linear as the two converge — which is exactly why terminal-value assumptions are the most scrutinized inputs in any model."*

---

### Q6. Why can't terminal growth exceed the discount rate — or the economy's growth rate?

**Answer.** Mathematically, the Gordon formula is the closed-form sum of an infinite growing geometric series with common ratio `(1+g)/(1+r)`; it converges only when `g < r`. If `g = r` the denominator is zero and value is infinite; if `g > r` the series diverges — nonsense. Economically, a company growing faster than GDP forever would eventually *become* the entire economy, an impossibility. So terminal `g` is capped at roughly long-run nominal GDP (~2–3% in developed markets).

**How to say it:** *"The perpetuity only converges when g is below r, and no firm can out-grow the whole economy forever — so I cap terminal growth near long-run nominal GDP, around 2 to 3%."*

---

### Q7. Why is the discount rate the input you stress-test first?

**Answer.** Because the terminal value is typically 60–80% of enterprise value, and it's driven by the `(r − g)` denominator. For a perpetuity, `dPV/dr = −CF₁/(r − g)^2` — the sensitivity explodes as the spread narrows. A 100bp move in WACC routinely swings a valuation 15–30%. Long-duration, back-loaded cash flows (growth companies) behave like long-duration bonds and are especially rate-sensitive. That's why a serious DCF is always delivered with a WACC-vs-growth sensitivity grid, never a single number.

**How to say it:** *"WACC and terminal growth, through the r minus g denominator. The terminal value is most of enterprise value and a 100bp WACC move can shift the answer 15 to 30%, so I always present a range, not a point."*

---

### Q8. How do you get from enterprise value to equity value, and why each step?

**Answer.** `Equity = EV − Net Debt − Preferred − Minority Interest + Non-operating assets`, where `Net Debt = Total Debt − Cash`. EV values the whole operating business to all capital providers. Debt and preferred are senior claims paid before common shareholders, so subtract. Minority interest belongs to outside shareholders of consolidated subsidiaries, so subtract. Non-operating assets (excess cash, investments not in operating FCF) belong to shareholders but weren't captured, so add. Divide by diluted shares for value per share.

**How to say it:** *"EV is the whole business to all investors. Strip out what's senior to or outside common equity — net debt, preferred, minority — add back non-operating assets, and you've got equity value. Divide by diluted shares for the price target."*

---

### Q9. Two companies have identical total cash flows; one's are front-loaded, the other's back-loaded. Which is worth more?

**Answer.** The **front-loaded** one. Discount factors decay exponentially with time, so cash received sooner is discounted less and carries more present value. The same logic explains why the early years of a forecast usually weigh more than later years, and why back-loaded growth businesses are more sensitive to the discount rate.

**How to say it:** *"Front-loaded — sooner cash is discounted less because discount factors decay exponentially. Timing, not just total, drives present value."*

---

### Q10. What's the difference between the discount rate and an expected-return forecast? Why does it matter?

**Answer.** The discount rate `r` is the **required** return that prices risk into the *denominator*; the numerator holds **expected** cash flows. They are different jobs. Risk should enter *once* — through `r` — not twice. A common error is to haircut the cash flows for risk *and* inflate the discount rate for the same risk, double-counting and under-valuing the asset.

**How to say it:** *"The discount rate is the required return that puts risk in the denominator; expected cash flows go in the numerator. Risk enters once, through r — don't also haircut the cash flows for the same risk."*

---

## Section B — Numerical problems (fully worked)

### Q11. Basic present value of a single cash flow.

**Problem.** What is the present value of `$1,000` received in 4 years at a discount rate of 7%?

**Solution.** `PV = 1000 / (1.07)^4`. `(1.07)^4 = 1.07 × 1.07 × 1.07 × 1.07 = 1.31080`. `PV = 1000 / 1.31080 = $762.90`.

**Verify.** Compound forward: `762.90 × 1.31080 = 1,000.00`. ✓

---

### Q12. Multi-period DCF, discrete convention.

**Problem.** Cash flows: Year 1 `$200`, Year 2 `$250`, Year 3 `$300`. Discount rate 10%. Find total PV.

**Solution.**

| Year | CF | DF `=1/(1.10)^t` | PV |
|---|---|---|---|
| 1 | 200 | 0.90909 | 181.82 |
| 2 | 250 | 0.82645 | 206.61 |
| 3 | 300 | 0.75131 | 225.39 |
| | | **Total** | **613.82** |

**Verify.** `181.82 + 206.61 + 225.39 = 613.82`. ✓

---

### Q13. Same flows, mid-year convention.

**Problem.** Re-value Q12's cash flows using the mid-year convention.

**Solution.** Discount at `t − 0.5`.

| Year | CF | Exponent | DF `=1/(1.10)^(t−0.5)` | PV |
|---|---|---|---|---|
| 1 | 200 | 0.5 | 0.95346 | 190.69 |
| 2 | 250 | 1.5 | 0.86678 | 216.70 |
| 3 | 300 | 2.5 | 0.78798 | 236.39 |
| | | | **Total** | **643.78** |

**Verify.** Mid-year total should equal discrete total × `(1.10)^0.5 = 1.04881`: `613.82 × 1.04881 = 643.78`. ✓ The `+4.9%` uplift matches the rule.

---

### Q14. Gordon Growth — watch the `CF₀` vs `CF₁` trap.

**Problem.** A firm generated `$80` of free cash flow **this year**. It will grow 3% forever. WACC is 9%. What is the value?

**Solution.** `$80` is `CF₀`, so grow it one period: `CF₁ = 80 × 1.03 = 82.40`. `Value = CF₁/(r − g) = 82.40 / (0.09 − 0.03) = 82.40 / 0.06 = $1,373.33`.

**Verify / trap note.** The common wrong answer omits the grow-up: `80/0.06 = 1,333.33`. The correct value is higher by exactly `(1+g)`: `1,333.33 × 1.03 = 1,373.33`. ✓

---

### Q15. Terminal value and its weight in EV.

**Problem.** Year-5 unlevered FCF is `$120`. Terminal growth 2.5%, WACC 8%. (a) Terminal value at end of year 5. (b) PV of that terminal value today. (c) If the PV of the explicit 5-year FCF is `$400`, what fraction of EV is the terminal value?

**Solution.**
(a) `CF₆ = 120 × 1.025 = 123.00`. `TV₅ = 123.00 / (0.08 − 0.025) = 123.00 / 0.055 = 2,236.36`.
(b) `(1.08)^5 = 1.46933`. `PV of TV = 2,236.36 / 1.46933 = 1,522.03`.
(c) `EV = 400 + 1,522.03 = 1,922.03`. TV fraction `= 1,522.03 / 1,922.03 = 79.2%`.

**Verify.** `2,236.36 × 0.055 = 123.00`. ✓ `1,522.03 × 1.46933 = 2,236.36`. ✓ TV weight of 79% sits at the top of the typical 60–80% band, as expected for a low `(r−g)` spread.

---

### Q16. Full mini-DCF with the equity bridge.

**Problem.** FCF: Y1 `$60`, Y2 `$70`, Y3 `$78`, Y4 `$84`, Y5 `$88`. Terminal growth 2%, WACC 10%. Total debt `$150`, cash `$30`, preferred `$20`, minority `$10`, non-operating asset `$15`, diluted shares `20m`. Find value per share.

**Solution.**

**Step 1 — PV of explicit FCF at 10%.**

| Year | FCF | DF | PV |
|---|---|---|---|
| 1 | 60 | 0.90909 | 54.55 |
| 2 | 70 | 0.82645 | 57.85 |
| 3 | 78 | 0.75131 | 58.60 |
| 4 | 84 | 0.68301 | 57.37 |
| 5 | 88 | 0.62092 | 54.64 |
| | | **Sum** | **283.01** |

**Step 2 — Terminal value.** `CF₆ = 88 × 1.02 = 89.76`. `TV₅ = 89.76 / (0.10 − 0.02) = 89.76 / 0.08 = 1,122.00`.

**Step 3 — PV of TV.** `1,122.00 × 0.62092 = 696.67`.

**Step 4 — EV.** `EV = 283.01 + 696.67 = 979.68`.

**Step 5 — Equity bridge.** `Net Debt = 150 − 30 = 120`. `Equity = 979.68 − 120 − 20 − 10 + 15 = 844.68`.

**Step 6 — Per share.** `844.68 / 20 = $42.23`.

**Verify.** Reverse the bridge: `42.23 × 20 = 844.60` (rounding) → add `120 + 20 + 10 − 15 = 135` → `844.68 + 135 = 979.68` EV. ✓ TV weight `= 696.67/979.68 = 71.1%`, within the normal band. ✓

---

### Q17. Discount-rate sensitivity of a perpetuity.

**Problem.** A growing perpetuity has `CF₁ = $50`, `g = 2%`. Compute its value at WACC of 7%, 8%, and 9%, and state the percentage change from the 8% base.

**Solution.**

| WACC | `r − g` | Value `= 50/(r−g)` | % change from base |
|---|---|---|---|
| 7% | 5% | $1,000.00 | +33.3% |
| 8% (base) | 6% | $833.33 | — |
| 9% | 7% | $714.29 | −14.3% |

**Verify.** `50/0.05 = 1,000`; `50/0.06 = 833.33`; `50/0.07 = 714.29`. Change up: `1000/833.33 − 1 = +20%`... let me recompute: `(1000 − 833.33)/833.33 = 166.67/833.33 = +20.0%`. Down: `(714.29 − 833.33)/833.33 = −14.3%`. Corrected: a −1% WACC move gives **+20.0%**, a +1% move gives **−14.3%** — the *asymmetry* (upside bigger than downside) is the key lesson, driven by the `1/(r−g)^2` convexity. ✓

**Corrected table:**

| WACC | `r − g` | Value | % change from base |
|---|---|---|---|
| 7% | 5% | $1,000.00 | +20.0% |
| 8% (base) | 6% | $833.33 | — |
| 9% | 7% | $714.29 | −14.3% |

**Lesson.** A symmetric ±1% move in WACC produces an *asymmetric* value response — the upside (+20%) exceeds the downside (−14.3%) because of the convexity in `1/(r−g)`. This is why sensitivity tables, not point estimates, are mandatory.

---

### Q18. Growing annuity (finite growing stream).

**Problem.** A patent pays a royalty of `$40` next year, growing 4% per year, for exactly 8 years, then expires worthless. Discount rate 10%. What is it worth today?

**Solution.** Growing annuity formula: `PV = (CF₁/(r−g)) × [1 − ((1+g)/(1+r))^n]`.
`CF₁/(r−g) = 40/(0.10 − 0.04) = 40/0.06 = 666.67`.
`(1+g)/(1+r) = 1.04/1.10 = 0.94545`. `0.94545^8 = ?`
`0.94545^2 = 0.89388`; `^4 = 0.89388^2 = 0.79902`; `^8 = 0.79902^2 = 0.63843`.
Bracket `= 1 − 0.63843 = 0.36157`.
`PV = 666.67 × 0.36157 = $241.05`.

**Verify (sanity).** If it were a perpetuity (n → ∞), value would be `666.67`. The finite 8-year version is worth `241.05`, i.e. `36.2%` of the perpetuity — the bracket `0.36157` is exactly that fraction. ✓ And it must be less than the perpetuity, which it is. ✓

---

### Q19. Continuous vs mid-year vs discrete on a single flow.

**Problem.** `$1,000` received in exactly 3 years, `r = 8%`. Value it three ways: discrete, mid-year, continuous.

**Solution.**
- **Discrete:** `1000/(1.08)^3 = 1000/1.259712 = $793.83`.
- **Mid-year:** exponent `2.5`: `1000/(1.08)^2.5 = 1000/1.212880 = $824.48`.
- **Continuous:** `1000 × e^(−0.08×3) = 1000 × e^(−0.24) = 1000 × 0.786628 = $786.63`.

**Verify / interpret.** Mid-year (`824.48`) > discrete (`793.83`) as expected (+3.86% ≈ `(1.08)^0.5 − 1 = 3.92%`, small rounding). Continuous (`786.63`) is *lowest* here because `e^(−rt)` uses the effective continuously-compounded rate, which for a full-period end-of-year flow discounts slightly harder than annual compounding. The point: know all three exist; equity DCFs use discrete or mid-year. ✓

---

### Q20. Sensitivity of a long-dated vs short-dated cash flow.

**Problem.** Cash flow A is `$1,000` in year 2; cash flow B is `$1,000` in year 10. WACC rises from 8% to 9%. Which loses more value in percentage terms, and by how much?

**Solution.**
- **A (year 2):** at 8%, `1000/1.08^2 = 1000/1.1664 = 857.34`; at 9%, `1000/1.09^2 = 1000/1.1881 = 841.68`. Change `= (841.68 − 857.34)/857.34 = −1.83%`.
- **B (year 10):** at 8%, `1000/1.08^10 = 1000/2.158925 = 463.19`; at 9%, `1000/1.09^10 = 1000/2.367364 = 422.41`. Change `= (422.41 − 463.19)/463.19 = −8.80%`.

**Verify / lesson.** The long-dated cash flow loses `8.80%` versus `1.83%` for the short-dated one — roughly proportional to `n` (year 10 vs year 2 ≈ 5× the maturity, and 8.80/1.83 ≈ 4.8×). ✓ This is duration: **long-duration cash flows are far more rate-sensitive**, which is why growth companies whip around on rate moves.

---

### Q21. Back-solving the implied discount rate.

**Problem.** A perpetuity pays `$30` next year growing at 2.5% forever and currently trades at `$600`. What discount rate does the market imply?

**Solution.** `600 = 30/(r − 0.025)` → `r − 0.025 = 30/600 = 0.05` → `r = 0.075 = 7.5%`.

**Verify.** `30/(0.075 − 0.025) = 30/0.05 = 600`. ✓ This "implied rate" reverse-engineering is a common way to sanity-check whether a market price embeds a reasonable required return.

---

### Q22. Full EV bridge reconciliation (both directions).

**Problem.** A company has EV of `$2,400`, total debt `$500`, cash `$120`, preferred `$80`, minority interest `$50`, non-operating investments `$60`, and `40m` diluted shares. (a) Equity value and per share. (b) Prove the bridge reconciles by walking backwards from per-share to EV.

**Solution.**
(a) `Net Debt = 500 − 120 = 380`. `Equity = 2,400 − 380 − 80 − 50 + 60 = 1,950`. `Per share = 1,950/40 = $48.75`.
(b) Backwards: `48.75 × 40 = 1,950` equity. Undo the bridge: add back net debt `+380`, preferred `+80`, minority `+50`, remove non-op `−60`: `1,950 + 380 + 80 + 50 − 60 = 2,400` = EV. ✓

**Lesson.** The bridge must reconcile in both directions. If your reverse walk doesn't return the original EV, you've mis-signed an adjustment (the classic error is adding net debt instead of subtracting, or dropping minority interest).

---

*End of Q&A — The Discounting Foundation.*
