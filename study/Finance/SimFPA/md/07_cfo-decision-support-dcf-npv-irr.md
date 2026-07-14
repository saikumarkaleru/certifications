# A CFO Decision-Support Ask: Quick DCF / NPV / IRR

## The ask

It's **21 July 2026**, 4:40 pm. The CFO catches you before she leaves:

> "Sales wants to open a **Hyderabad-East branch** for the industrial-components line — new territory, dedicated stock, two field engineers. They're pitching it to the MD next week and they've handed me a spreadsheet that just says 'huge upside.' I need a **quick, honest read** by tomorrow noon: what's the **NPV** and **IRR** at our 12% cost of capital, and **how sensitive** is the answer to the discount rate and the growth assumption? One page — cash-flow table, the number, and your recommendation. If the terminal value is doing all the work, I want to know that."

This is classic **decision support**: a compact **DCF** on the initiative's free cash flow (FCFF), a terminal value, and `=NPV / =IRR` (and their dated cousins `=XNPV / =XIRR`) — plus a sensitivity grid so nobody hides behind a single point estimate.

## What you're given

**Initiative assumptions (FY2026-27 basis, Rs lakh):**

| Item | Value |
|---|---:|
| Upfront investment (Year 0): fit-out + opening stock | 40 |
| WACC / discount rate | 12% |
| Terminal growth (g) | 3% |
| Forecast horizon | 5 years |
| Tax | 25% + cess (baked into FCFF) |

**Projected incremental Free Cash Flow to Firm (FCFF), Rs lakh** — built by Sales from expected branch revenue less incremental COGS, opex, tax, and maintenance capex/working capital:

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| FCFF | 8 | 11 | 13 | 14 | 15 |

## Build it — step by step

**Step 1 — Lay out the cash-flow line.** Row of years 0–5. Year 0 is the outflow `−40`; Years 1–5 are the FCFF above.

**Step 2 — Terminal value (Gordon growth), computed at end of Year 5:**
```
TV = FCFF₅ × (1 + g) / (WACC − g)
   = 15 × 1.03 / (0.12 − 0.03) = 15.45 / 0.09 = 171.67  (Rs lakh)
```

**Step 3 — Discount factors** `= 1/(1+WACC)^t`:

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| DF @12% | 0.8929 | 0.7972 | 0.7118 | 0.6355 | 0.5674 |

**Step 4 — Present values:**

| Year | FCFF | +TV | Total CF | DF | PV |
|---|---:|---:|---:|---:|---:|
| 1 | 8 | | 8 | 0.8929 | 7.14 |
| 2 | 11 | | 11 | 0.7972 | 8.77 |
| 3 | 13 | | 13 | 0.7118 | 9.25 |
| 4 | 14 | | 14 | 0.6355 | 8.90 |
| 5 | 15 | 171.67 | 186.67 | 0.5674 | 105.93 |
| | | | | **Σ PV** | **139.99** |

Of which PV of operating FCFF = 42.57 and **PV of terminal value = 97.42** — the terminal value is **~70% of enterprise value**. That's the flag the CFO asked for.

**Step 5 — NPV and IRR (the Excel formulas):**
```
Enterprise value  = SUM(PV) = 139.99
NPV  = 139.99 − 40 = 100.0    ' or directly:
NPV  = −40 + NPV(12%, C1:C5)   where C5 includes TV → ≈ 100
IRR  = IRR({−40, 8, 11, 13, 14, 186.67}) ≈ 51%
```

Note the **`=NPV` gotcha**: Excel's `NPV()` assumes the first cash flow is one period away, so you place the Year-0 outflow *outside* the function: `=−40 + NPV(12%, year1:year5)`. Never put Year 0 inside `NPV()`.

**Step 6 — Dated version (`=XNPV / =XIRR`)** for real, irregular cash-flow dates:
```
=XNPV(12%, values, dates)   ' values incl. −40 at the Year-0 date
=XIRR(values, dates)
```
`XNPV/XIRR` discount by actual calendar days, so a branch that opens mid-quarter is valued correctly — more precise than the annual `NPV/IRR`.

**Step 7 — The terminal-value reality check.** IRR of **51%** looks spectacular, but strip out the TV and the 5-year operating IRR on FCFF alone (`IRR{−40, 8, 11, 13, 14, 15}`) is only **~13.5%** — barely above the 12% hurdle. So the *headline return lives in the perpetuity assumption*, not the visible five years. That single sentence is the most valuable thing in the memo.

## The deliverable

**One-page decision memo — Hyderabad-East branch**

| Metric @ WACC 12%, g 3% | Value |
|---|---:|
| PV of 5-yr FCFF | Rs 42.6 lakh |
| PV of terminal value | Rs 97.4 lakh |
| Enterprise value | Rs 140.0 lakh |
| Less: upfront investment | Rs (40.0) lakh |
| **NPV** | **Rs 100.0 lakh** |
| **IRR (with TV)** | **~51%** |
| IRR (operating flows only, ex-TV) | ~13.5% |
| TV as % of EV | **~70%** |

**Sensitivity — NPV (Rs lakh) to WACC × terminal growth (2-var Data Table):**

| WACC \ g | 2% | 3% | 4% |
|---|---:|---:|---:|
| **10%** | 123.8 | 142.1 | 166.5 |
| **12%** | 89.4 | **100.0** | 113.2 |
| **14%** | 66.6 | 73.3 | 81.4 |

**Recommendation:** "**Conditional GO.** At our 12% WACC the branch shows **NPV ~Rs 1.0 cr and IRR ~51%** — comfortably value-accretive, and it stays positive (Rs 67–166 lakh) across every WACC/growth combination we tested, so the *decision* is robust. **But** ~70% of the value sits in the terminal value, and the visible 5-year IRR is only ~13.5% — a whisker above the hurdle. My recommendation: approve, but (i) treat the first five years as the real underwriting case, (ii) sanity-check the FCFF ramp with Sales against the actual pipeline (these are their numbers, not audited), and (iii) build a stage-gate — release the Rs 40 lakh in two tranches, second tranche contingent on Year-1 FCFF ≥ Rs 6 lakh. The upside is real; the risk is that the perpetuity is doing the heavy lifting."

## How it's reviewed

- **Year 0 outside `NPV()`.** The CFO will click the NPV cell — if `−40` sits inside the function, the answer is silently discounted an extra year and wrong.
- **TV timing.** Terminal value is a Year-5 figure, discounted by the Year-5 factor — not discounted twice, not left undiscounted.
- **TV as % of EV disclosed.** Any DCF where TV > 65% of value gets scrutiny; hiding it is a red flag.
- **IRR sign changes.** One sign flip (Year 0 negative, rest positive) → one IRR, reliable. Multiple flips can give multiple/► no IRR — then use NPV.
- **WACC consistency:** FCFF is a firm-level (unlevered) cash flow, so it's discounted at WACC — not cost of equity. Mixing them is an instant fail.

## Common mistakes & red flags

- **Putting the initial outlay inside `=NPV()`.** The single most common Excel valuation bug — over-discounts everything.
- **Terminal value with `g ≥ WACC`.** The denominator `(WACC − g)` goes to zero or negative and TV explodes to infinity/nonsense. `g` must be modest (≤ long-run GDP, here 3%).
- **Trusting IRR alone.** IRR ignores scale and reinvestment; a 51% IRR on Rs 40 lakh may matter less than a 20% IRR on Rs 4 cr. Always pair IRR with NPV.
- **No sensitivity.** A single-point NPV invites a single-point argument. The Data Table shows the *range* and where it turns negative.
- **Terminal value doing all the work, undisclosed.** If the five visible years barely clear the hurdle, say so — don't let a perpetuity assumption smuggle the decision through.
- **Nominal vs real mismatch:** nominal cash flows need a nominal WACC and a nominal `g`. Don't mix.

## On the job & in the interview

DCF/NPV/IRR is the language of capital allocation — every branch, machine, or acquisition passes through it. FP&A's value-add isn't the arithmetic (Excel does that); it's **stress-testing the assumptions** and telling the CFO *where the answer is fragile*.

**Q: "NPV vs IRR — which do you trust and why?"**
"NPV, because it's in rupees and additive — it tells you how much value you create and you can sum projects. IRR is an intuitive % and great for ranking, but it breaks with unconventional cash flows (multiple sign changes give multiple IRRs), it's blind to scale, and it implicitly assumes reinvestment at the IRR itself. I lead with NPV and quote IRR alongside; if they disagree on a ranking, NPV wins."

**Q: "Your NPV is Rs 1 crore — how confident are you?"**
"The *decision* is robust — NPV stays positive across every WACC (10–14%) and growth (2–4%) combination. The *magnitude* is not — about 70% of value is terminal, and the five-year operating IRR is only ~13.5%. So I'm confident it's value-accretive but I'd underwrite it on the visible cash flows and stage-gate the funding, rather than bank on the perpetuity."

**Q: "Why discount FCFF at WACC and not the cost of equity?"**
"FCFF is the cash available to *all* capital providers — debt and equity — before financing flows, so it must be discounted at the blended cost of both, the WACC (~12% here). Cost of equity pairs with FCFE, the cash to equity holders only. Match the cash flow to the discount rate or you double-count or miss the financing effect."
