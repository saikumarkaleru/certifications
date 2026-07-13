# DCF Valuation Model

## What it is & where it's used

A **Discounted Cash Flow (DCF)** model values a business as the present value of the cash it will generate for *all* capital providers. You project **Free Cash Flow to the Firm (FCFF)** for 5–10 years, discount it at the **Weighted Average Cost of Capital (WACC)**, add a **terminal value** for everything beyond the forecast, and get **Enterprise Value (EV)**. Then you bridge EV to **equity value** and divide by shares to get an intrinsic price per share.

Where it's used:

- **Investment banking / M&A** — the DCF is one of the three "football field" methods (alongside comparable companies and precedent transactions).
- **Equity research** — analysts publish a target price that is usually DCF-anchored.
- **Corporate FP&A / strategy / corp-dev** — evaluating acquisitions, new plants, or business units.
- **Private equity / valuation advisory** — deal screening, purchase price allocation, IND AS impairment testing (value-in-use is literally a DCF).
- **Startups / VC** — less common (cash flows too uncertain), but growth-stage deals still use it as a sanity check.

If your JD says "valuation," "financial modeling," "equity research," or "corporate finance," a DCF is table stakes.

## The gap: why companies want this (and college didn't teach it)

College teaches the **formula** — PV = CF / (1+r)^n — on a slide, with r handed to you. Industry pays you to **generate every input yourself and defend it**:

- Where does WACC come from? You have to build cost of equity via **CAPM**, un-lever and re-lever a **beta**, pull a live risk-free rate, and weight it by an actual capital structure.
- What is "free" cash flow? Not net profit, not EBITDA. You must walk EBIT → NOPAT → add D&A → subtract capex → subtract the change in working capital — and know *why* each step exists.
- Terminal value is 60–80% of the answer. College never warns you that a 0.5% change in the growth rate swings the valuation by 20%.
- It must be a **live, auditable Excel file** with no hardcodes, no circular-reference errors, and a sensitivity table — not a one-cell answer.

The gap is: theory gives you the discounting equation; the job is the **50 assumptions feeding it** and the discipline to make them consistent. That is what the model below builds.

## What "proficient" looks like

A job-ready person can, unaided in Excel, in about 45–90 minutes:

1. Build a FCFF projection from a revenue driver down to unlevered free cash flow.
2. Compute WACC from CAPM + after-tax cost of debt, correctly weighted at market values.
3. Calculate terminal value **both ways** — Gordon Growth and exit-multiple — and reconcile them.
4. Discount using **mid-year convention** if asked, and get period 0 right.
5. Run the **EV → equity bridge** (subtract net debt, minorities, add associates).
6. Build a **two-way data table** for WACC × terminal growth and read the risk off it.
7. Explain in one sentence why the value is what it is ("driven by 3% terminal growth and 11% WACC").

They know that TV dominates, that growth `g` must be below WACC and roughly nominal GDP (~5–6% for India, ~2–3% for developed markets), and that NOPAT tax is a normalized cash rate.

## Hands-on: how to actually do it

Assume a clean tab with years in columns. Below, Year-1 FCFF sits in `C10`.

**1. Build FCFF (the engine).** For each forecast year:

```
FCFF = EBIT × (1 − tax rate) + D&A − Capex − ΔWorking Capital
```

Excel, with EBIT in row 5, tax rate in `$B$2`, D&A row 6, Capex row 7, ΔNWC row 8:

```excel
=C5*(1-$B$2) + C6 - C7 - C8
```

**2. Cost of equity — CAPM.**

```
Ke = Rf + β × Equity Risk Premium
```

```excel
=Rf + Beta*ERP           ' e.g. =0.071 + 1.15*0.075  -> 15.7%
```

Re-lever an industry (unlevered) beta to your target D/E using the Hamada relation:

```excel
' Levered beta = Bu * (1 + (1 - tax) * D/E)
=Bu*(1 + (1-$B$2)*(NetDebt/Equity))
```

**3. After-tax cost of debt.**

```excel
=Kd*(1-$B$2)             ' e.g. =0.095*(1-0.25) -> 7.13%
```

**4. WACC.** With market value of equity `E`, debt `D`:

```excel
=(E/(E+D))*Ke + (D/(E+D))*Kd_aftertax
```

**5. Discount factor** (period `n` in row 9, WACC in `$B$3`):

```excel
=1/(1+$B$3)^C9                          ' standard year-end
=1/(1+$B$3)^(C9-0.5)                     ' mid-year convention
```

PV of each year's FCFF: `=C10*C11` (FCFF × discount factor).

**6. Terminal value — Gordon Growth** (on final-year FCFF, `N10`, growth `$B$4`):

```excel
=N10*(1+$B$4)/($B$3-$B$4)                ' TV at end of year N
```

Then discount TV back with the **final-year** discount factor: `=TV*N11`.

**7. Terminal value — Exit multiple** (e.g. 9× terminal-year EBITDA in `N4`):

```excel
=N4*9                                    ' then × discount factor
```

**8. Enterprise Value:** `=SUM(PV of FCFFs) + PV of Terminal Value`.

**9. EV → Equity bridge:**

```excel
Equity Value = EV − Net Debt − Minority Interest − Preferred + Associates/Investments
=EV - NetDebt - Minority + Associates
Price per share = Equity Value / Diluted shares
```

**10. Sensitivity** — select the corner-cell table, then `Data ▸ What-If Analysis ▸ Data Table`, row input = growth, column input = WACC.

## Worked example / mini-project

**Company: "Bharat Consumer Ltd" (FMCG), all figures ₹ crore.** Tax 25%, base year revenue ₹2,000 cr.

Assumptions: revenue grows 12% → 8% tapering; EBIT margin 18%; D&A 3% of revenue; capex 4%; ΔNWC 2% of incremental revenue.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Revenue | 2,240 | 2,486 | 2,734 | 2,980 | 3,218 |
| EBIT (18%) | 403 | 448 | 492 | 536 | 579 |
| NOPAT (×0.75) | 302 | 336 | 369 | 402 | 434 |
| + D&A (3%) | 67 | 75 | 82 | 89 | 97 |
| − Capex (4%) | 90 | 99 | 109 | 119 | 129 |
| − ΔNWC (2% Δrev) | 5 | 5 | 5 | 5 | 5 |
| **FCFF** | **274** | **307** | **337** | **367** | **397** |

**WACC:** Ke = 7.1% + 1.15 × 7.5% = **15.7%**; Kd after-tax = 9.5% × 0.75 = **7.1%**. Capital structure 80% equity / 20% debt → WACC = 0.8×15.7% + 0.2×7.1% = **13.98%** (round to **14%**).

**Discount factors @14%:** 0.877, 0.769, 0.675, 0.592, 0.519.

**PV of FCFF:** 240 + 236 + 227 + 217 + 206 = **₹1,126 cr**.

**Terminal value (Gordon, g = 5%):**
TV = 397 × 1.05 / (0.14 − 0.05) = 417 / 0.09 = **₹4,630 cr**.
PV of TV = 4,630 × 0.519 = **₹2,403 cr**.

**Cross-check (exit multiple, 11× terminal EBITDA of 579):** 579 × 11 = ₹6,369 cr → PV = ₹3,306 cr. The Gordon TV implies a cheaper multiple, so the base case is conservative — note the gap and pick one.

**Enterprise Value** (Gordon basis) = 1,126 + 2,403 = **₹3,529 cr**.

**Bridge:** Net debt ₹400 cr, no minorities → Equity value = 3,529 − 400 = **₹3,129 cr**. Diluted shares 25 cr → **₹125.16 per share**.

Notice TV is 2,403 / 3,529 = **68% of EV** — exactly why the sensitivity table matters.

**Sensitivity (price/share, ₹):**

| WACC ↓ / g → | 4.0% | 5.0% | 6.0% |
|---|---|---|---|
| 13% | 133 | 148 | 169 |
| 14% | 116 | 125 | 138 |
| 15% | 103 | 110 | 119 |

A one-point WACC or growth move shifts value ₹10–20 — report the range, not one number.

## How it's tested

**Interview questions (verbal):**

- "Walk me from EBIT to FCFF." (Must recite NOPAT + D&A − capex − ΔNWC.)
- "Why FCFF discounted at WACC, not FCFE at Ke?" (Consistency: firm cash flows ↔ blended firm cost.)
- "Terminal value is 70% of your DCF — is that a problem?" (Show you'd sanity-check the implied exit multiple.)
- "What if g > WACC?" (Gordon formula breaks — value goes negative/infinite; g must be below WACC.)
- "Rf is 7%, ERP 7.5%, beta 1.2 — cost of equity?" (Instant: 16%.)
- "Does WACC use book or market weights?" (Market.)

**Practical / assessment tests:**

- A **timed 60–90 min Excel case**: raw financials given, build a DCF from scratch, output a price and a data table. Graders check for **no hardcoded numbers in formulas**, a working sensitivity table, and correct EV→equity bridge.
- A **"break my model"** review: they hand you a DCF with a planted error (tax applied twice, TV not discounted, book-value net debt) and ask you to find it.
- Equity research shops give a **"initiate coverage"** take-home: full model + one-page thesis.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Forgetting to discount the terminal value | TV is at end of year N — multiply by year-N discount factor before adding |
| Terminal growth ≥ nominal GDP (e.g. 10%) | Cap g at ~5–6% India / 2–3% developed; g < WACC always |
| Using net profit instead of NOPAT | Start from EBIT, apply tax to EBIT (unlevered), never after interest |
| Double-counting the tax shield | If Kd is already after-tax in WACC, don't also add interest tax savings to cash flow |
| Book-value net debt in the bridge | Use market value of debt and current net debt |
| Ignoring ΔWorking Capital | Growing firms consume cash in NWC — always subtract the *change* |
| Mismatch: FCFF discounted at Ke | FCFF ↔ WACC; FCFE ↔ Ke. Never cross them |
| Circular reference (WACC ← equity value ← WACC) | Use target weights, or enable iterative calc `File ▸ Options ▸ Formulas` |
| One-number answer, no sensitivity | Always ship a WACC × g data table |
| Hardcoding assumptions inside formulas | Every driver in a labeled input cell, colored blue |

## Learn-it roadmap & resources

**Time to proficiency:** ~30–40 focused hours to build one clean model unaided; ~3 months to be interview-fast.

| Week | Focus |
|---|---|
| 1 | FCFF mechanics, EBIT→NOPAT→FCFF; rebuild the example above by hand |
| 2 | WACC: CAPM, beta lever/unlever, market weights; pull real Rf from RBI 10-yr G-sec |
| 3 | Terminal value both methods, mid-year convention, EV→equity bridge |
| 4 | Sensitivity, scenario toggles, formatting discipline; build a full model on a real listed company (e.g. from screener.in data) |

**Resources:**

- **Free:** Aswath Damodaran (NYU) — his valuation lectures and datasets (ERP, betas by industry) are the global gold standard, free on his site/YouTube. Corporate Finance Institute free articles. `screener.in` for Indian company financials.
- **Paid:** Wall Street Prep / Breaking Into Wall Street (BIWS) DCF modeling courses; CFI's **FMVA** certification (globally portable, covers DCF end-to-end); Wall Street Oasis modeling tests for practice.
- **India-relevant:** CFA Level II (Equity) covers FCFF/FCFE rigorously; NISM Research Analyst certification touches valuation.

## Quick-reference

```
FCFF = EBIT×(1−t) + D&A − Capex − ΔNWC
Ke   = Rf + β×ERP                      (CAPM)
Kd,at= Kd×(1−t)
WACC = E/(E+D)×Ke + D/(E+D)×Kd,at      (market weights)
βL   = βU×(1 + (1−t)×D/E)              (Hamada re-lever)
DF   = 1/(1+WACC)^n   [mid-year: n−0.5]
TV_Gordon = FCFF_N×(1+g)/(WACC−g)      → then ×DF_N
TV_Exit   = EBITDA_N × multiple        → then ×DF_N
EV   = Σ(FCFF×DF) + TV×DF_N
Equity = EV − NetDebt − Minority − Pref + Associates
Price = Equity / Diluted shares
```

| Input | Sensible range (India) | Developed markets |
|---|---|---|
| Risk-free (Rf) | 6.5–7.5% (10-yr G-sec) | 3.5–4.5% (US 10-yr) |
| Equity risk premium | 7–9% | 4.5–5.5% |
| Terminal growth g | 4–6% | 2–3% |
| WACC (typical) | 11–15% | 7–10% |
| Terminal value as % of EV | 60–80% — always stress-test it |

**Golden rules:** g < WACC always. Discount the TV. FCFF↔WACC, FCFE↔Ke. Every assumption in a blue input cell. Ship the sensitivity table.
