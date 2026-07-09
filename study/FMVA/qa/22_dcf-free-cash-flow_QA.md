# Q&A — DCF — Free Cash Flow

Practice bank for Chapter 22. Work each question before reading the answer. The chapter rests on one discipline — **the cash flow and the discount rate must serve the same claimants** — and one workhorse formula, `FCFF = EBIT×(1−t) + D&A − CapEx − ΔNWC`. Every build below is reproducible cell-for-cell in Excel and reconciles by at least two independent routes, so you can watch the arithmetic close on itself.

---

## Section A — Concept Checks (test the WHY)

**A1. In one sentence, what makes free cash flow "free"?**

It is the cash left over *after* the business has funded every mandatory reinvestment it needs to sustain and grow itself (replacement capex, the extra working capital a growing firm ties up), so it is genuinely available to hand to capital providers without impairing the ongoing business.

**A2. Why can't you just discount net income to value a company?**

Because net income is polluted twice over. It is an *accrual* number — depreciation reduces it though no cash left that year, while the actual capex cash outflow never appears on the income statement — so it misstates cash timing. And it is *after interest*, so it already reflects one particular financing choice. Discounting it would both double-count the asset (penalise depreciation *and* capex) and entangle operating value with capital structure. FCFF fixes both: it restores cash timing and strips financing out.

**A3. FCFF vs FCFE — who does each serve, and what value does each produce?**

FCFF (unlevered) is the cash available to *all* capital providers before financing effects; discounted at WACC it produces **enterprise value**. FCFE (levered) is the cash left for *equity holders only* after lenders are paid interest and principal and new borrowing is added back; discounted at the cost of equity it produces **equity value directly**. Firm cash pairs with the firm's blended cost of capital; equity cash pairs with the cost of equity.

**A4. Why do we tax EBIT rather than the actual tax the company paid?**

Actual tax was reduced by the interest deduction, so it embeds the debt tax shield. If you carried that lower tax into FCFF, the shield would inflate the cash flow — and then WACC's after-tax cost of debt would count the *same* shield a second time. Taxing EBIT gives a hypothetical *unlevered* tax (EBIT×t) and hence NOPAT, a capital-structure-neutral profit. The shield is not lost; it is captured in exactly one place, the WACC.

**A5. Why is an *increase* in net working capital subtracted in the FCFF build?**

Because a rising NWC means cash has been locked into the business — more receivables extended to customers, more inventory stacked on shelves, net of what suppliers financed. That is a cash *outflow*, so it reduces FCFF. Symmetrically, a *fall* in NWC (collecting receivables, running down stock, stretching payables) releases cash and is added back.

**A6. What is "conspicuously absent" from the FCFF formula, and why does that absence define it?**

Interest expense. FCFF never touches interest — that omission is the entire meaning of *unlevered*. The operating engine's value must not depend on whether the CFO funded it with 20% or 60% debt; financing is handled once, later, inside the WACC. Any interest appearing in an FCFF build makes it a corrupted hybrid, not FCFF.

**A7. Why is FCFF-at-WACC the industry default over FCFE-at-cost-of-equity for general corporate valuation?**

FCFF separates operating performance from financing cleanly and is far more *stable*. FCFE swings violently with lumpy debt drawdowns and repayments, which can make a healthy business look erratic year to year. FCFE remains standard for banks and financial institutions, where debt is raw material rather than mere financing, but for ordinary corporates FCFF's stability and clean separation win.

**A8. Why do professionals build discount factors by hand rather than trust Excel's `NPV`?**

`NPV` hard-assumes the first cash flow is exactly one full period away and offers no mid-year convention. Manual discount factors — `1/(1+r)^period` with the period row set to 1,2,3… (year-end) or 0.5,1.5,2.5… (mid-year) — put the timing under your explicit control and make it auditable.

**A9. What does it mean that "you do not forecast free cash flow directly"?**

FCFF is a *read-out* of the integrated model, not a separate line. Revenue and margin drivers set EBIT; the PP&E schedule sets D&A and capex; working-capital days set ΔNWC. Change one driver and FCFF recomputes everywhere automatically. That is precisely why the three-statement model is built first — the DCF consumes it.

---

## Section B — Build / Computational Problems

*Reproduce each in Excel. Link inputs by cell reference; the arithmetic is shown so it self-checks.*

**B1. Single-year FCFF from EBIT.** FY1: EBIT = 500, D&A = 120, CapEx = 180, NWC rose 300 → 340, tax = 25%. Compute FCFF.

| Line | Formula | Value |
|---|---|---:|
| EBIT | given | 500 |
| Unlevered tax | 500 × 0.25 | (125) |
| **NOPAT** | 500 × 0.75 | **375** |
| + D&A | +120 | 120 |
| − CapEx | −180 | (180) |
| − ΔNWC | −(340 − 300) | (40) |
| **FCFF** | 375 + 120 − 180 − 40 | **275** |

FCFF = **275**. The $40 working-capital build is a drain on a growing business.

**B2. Reconcile B1 from net income.** Same company, interest expense = 60. Prove FCFF = 275 bottom-up.

Pre-tax income = 500 − 60 = 440; tax @25% = 110; net income = 330.
`FCFF = NI + Interest×(1−t) + D&A − CapEx − ΔNWC = 330 + 60×0.75 + 120 − 180 − 40`
= 330 + 45 + 120 − 180 − 40 = **275** ✓. Two independent routes agree, proving no financing leaked into the operating flow.

**B3. Reconcile B1 from EBITDA.** Using the EBITDA-start formula, confirm 275.

EBITDA = EBIT + D&A = 500 + 120 = 620.
`FCFF = EBITDA×(1−t) + D&A×t − CapEx − ΔNWC = 620×0.75 + 120×0.25 − 180 − 40`
= 465 + 30 − 180 − 40 = **275** ✓. Three starting points, one answer — the definitional check the chapter demands.

**B4. Project a five-year FCFF stream.** FY1 revenue = 1,000 growing 10%/yr; EBIT margin 20%; tax 25%; D&A 8% of revenue; CapEx 10% of revenue; NWC 15% of revenue; FY0 revenue 909.1 (so FY0 NWC = 136.4).

Revenue: 1,000.0 / 1,100.0 / 1,210.0 / 1,331.0 / 1,464.1.
EBIT (20%): 200.0 / 220.0 / 242.0 / 266.2 / 292.8. NOPAT (75%): 150.0 / 165.0 / 181.5 / 199.7 / 219.6.

| | FY1 | FY2 | FY3 | FY4 | FY5 |
|---|---:|---:|---:|---:|---:|
| NOPAT | 150.0 | 165.0 | 181.5 | 199.7 | 219.6 |
| + D&A (8%) | 80.0 | 88.0 | 96.8 | 106.5 | 117.1 |
| − CapEx (10%) | (100.0) | (110.0) | (121.0) | (133.1) | (146.4) |
| − ΔNWC | (13.6) | (15.0) | (16.5) | (18.2) | (20.0) |
| **FCFF** | **116.4** | **128.0** | **140.8** | **154.9** | **170.3** |

ΔNWC(FY1) = 150.0 − 136.4 = 13.6; thereafter 15% of the revenue increase (FY2: 15% × 100 = 15.0). Spot-check FY1: 150 + 80 − 100 − 13.6 = 116.4 ✓.

**B5. Discount the B4 stream at WACC = 10%, year-end.**

| | FY1 | FY2 | FY3 | FY4 | FY5 |
|---|---:|---:|---:|---:|---:|
| Factor 1/1.1^n | 0.9091 | 0.8264 | 0.7513 | 0.6830 | 0.6209 |
| PV of FCFF | 105.8 | 105.8 | 105.8 | 105.8 | 105.7 |

Sum of PV = 105.8 + 105.8 + 105.8 + 105.8 + 105.7 = **528.9**. (Check FY1: 116.4 × 0.9091 = 105.8 ✓; FY5: 170.3 × 0.6209 = 105.7 ✓.) The near-constant PVs are a coincidence of ~10% cash-flow growth almost cancelling 10% discounting — a nice internal-consistency signal, not a general rule. This is the PV of the *explicit* stream only; terminal value is added in Chapter 23.

**B6. Same stream, mid-year convention.** Recompute the PV total using periods 0.5, 1.5, 2.5, 3.5, 4.5.

Factors 1/1.1^0.5… = 0.9535, 0.8668, 0.7880, 0.7164, 0.6512.
PVs: 111.0 / 111.0 / 110.9 / 111.0 / 110.9 → sum ≈ **554.8**. Mid-year lifts value ~4.9% (a factor of 1.1^0.5 = 1.0488 on every flow) because cash is assumed to arrive half a year sooner. Same cash flows, different timing assumption, materially different value — which is exactly why timing must be explicit.

**B7. FCFF → FCFE bridge.** B1 company (FCFF = 275, interest = 60, tax = 25%) drew 50 of new debt and repaid 30 in FY1. Compute FCFE.

Net borrowing = 50 − 30 = +20.
`FCFE = FCFF − Interest×(1−t) + Net Borrowing = 275 − 60×0.75 + 20 = 275 − 45 + 20 = 250.`
Cross-check bottom-up: `FCFE = NI + D&A − CapEx − ΔNWC + Net Borrowing = 330 + 120 − 180 − 40 + 20 = 250` ✓. FCFE = **250** — discount at the cost of equity for equity value, never at WACC.

**B8. Excel reconciliation check row.** Write the formula that flags a definitional error between the EBIT-route and NI-route FCFF.

`=IF(ROUND(C_FCFF_EBIT − C_FCFF_NI, 0)=0, "OK", "ERR")`. Rounding to the nearest whole number absorbs harmless floating-point noise; any real leak of financing into the operating flow (e.g. taxing EBT instead of EBIT) breaks the equality and the cell reads "ERR".

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me from EBIT to unlevered free cash flow."**

Start with EBIT — operating profit before any financing. Tax it at the full marginal rate *as if the firm had no debt* to get NOPAT; this deliberately ignores the actual interest deduction. Add back D&A because it is a non-cash charge that reduced EBIT but consumed no cash this year. Subtract capital expenditure — the real cash spent on long-term assets. Subtract the increase in net working capital — the cash a growing business ties up in receivables and inventory net of payables. What remains is FCFF: the unlevered cash the operating business generates for all capital providers. I'd discount it at WACC to get enterprise value.

**C2. "Why strip interest out of the cash flow only to handle the tax shield in the discount rate — isn't that circular?"**

It's the opposite of circular; it's what keeps the model consistent. The debt tax shield must be counted exactly once. FCFF is computed before interest and taxed at the unlevered rate, so the shield is entirely absent from the cash flow. It then reappears in precisely one place: WACC's after-tax cost of debt, `k_d×(1−t)`. Cash flow handles operations, discount rate handles financing — one benefit, one location. If I instead left interest in the cash flow *and* used an after-tax WACC, I'd count the shield twice and overvalue the firm.

**C3. "A junior analyst hands you a DCF where FCFF is discounted at the cost of equity. What's wrong and what's the impact?"**

The claimant levels don't match. FCFF is firm-level cash belonging to debt *and* equity, so it must be discounted at the blended firm rate, WACC. The cost of equity is higher than WACC (equity is riskier and the after-tax cost of debt is lower), so discounting firm cash at the equity rate over-discounts and *understates* enterprise value. The fix is either discount FCFF at WACC, or convert to FCFE (subtract after-tax interest, add net borrowing) and keep the cost of equity — but you can't cross the wires.

**C4. "When would you value on FCFE instead of FCFF?"**

Primarily for banks and financial institutions, where leverage isn't a financing sideshow — debt (deposits, borrowings) is the raw material of the business, and separating operations from financing is artificial. FCFE, discounted at the cost of equity, values the equity directly, which is what you want there. For ordinary corporates I default to FCFF/WACC because FCFE is volatile — it lurches with lumpy debt repayments and drawdowns — and because FCFF cleanly isolates operating value before you layer on the specific capital structure.

**C5. "Your model's revenue growth assumption changes from 8% to 12%. Where does that show up in free cash flow?"**

Everywhere, automatically, if the model is built right. Higher revenue lifts EBIT through the margin, raising NOPAT. It raises D&A and capex if those are driven as a percentage of revenue. It enlarges the working-capital base, so ΔNWC — the cash consumed — grows too, partially offsetting the gain. Net FCFF usually rises but by less than revenue, because faster growth is self-funding-hungry. The key point: I never retype FCFF; it's a read-out of linked drivers, so one assumption change ripples through the whole stream.

**C6. "How long should the explicit forecast be, and what must the final year look like?"**

Typically 5 to 10 years — long enough for the business to reach steady state, short enough that projections stay credible. The final explicit year should look *mature*: growth decelerating toward a sustainable long-run rate, margins stable, working capital growing proportionally with revenue, and crucially capex roughly equal to D&A — a mature firm only replaces what wears out. That steady state is what lets you attach a clean terminal value in the next step; a terminal year with capex far above D&A modeled into perpetuity would understate FCFF forever.

---

## Section D — Common-Error Spotting

*Each item states a modeling move. Identify the error and give the fix.*

**D1.** *"I computed FCFF as EBT × (1−t) + D&A − CapEx − ΔNWC."*

Error: taxing **EBT**, which is *after* interest, smuggles the financing tax shield into the cash flow — and WACC then counts it again. Fix: tax **EBIT**, not EBT, so you get the unlevered NOPAT and the shield lives only in WACC.

**D2.** *"My growing company's ΔNWC line is adding cash to FCFF every year."*

Error: sign flip. A growing business builds working capital, which *uses* cash, so ΔNWC should *reduce* FCFF. If growth is boosting cash via working capital, the sign is backward. Fix: enter ΔNWC as `−(NWC_this − NWC_last)`, so an increase is negative.

**D3.** *"I added interest expense back into FCFF and also discounted at the cost of equity."*

Two errors. Interest has no place in FCFF (it's unlevered) — leaving it in makes a corrupted hybrid. And FCFF, being firm-level, pairs with WACC, not the cost of equity. Fix: remove interest from the flow and discount at WACC; or, if you genuinely want equity value, build FCFE properly (subtract after-tax interest, add net borrowing) and keep the cost of equity.

**D4.** *"For FCFE I added the total net debt balance of 800 for the year."*

Error: confusing a *balance* with a *flow*. FCFE adds **net borrowing** — new debt drawn minus principal repaid *during the period* — not the total net-debt balance. The balance is used only at the very end, to bridge enterprise value to equity value. Fix: use `drawdowns − repayments` for the year.

**D5.** *"I used `=NPV(WACC, FY1:FY5)` for the PV and applied mid-year timing in my head."*

Error: `NPV` assumes the first cash flow is one full period out and has no mid-year convention, so it silently contradicts the mid-year assumption. Fix: build an explicit discount-period row (0.5, 1.5, …) and factor row `=1/(1+WACC)^period`, then `SUMPRODUCT` the flows and factors.

**D6.** *"I typed the free-cash-flow numbers straight in as a clean input row."*

Error: FCFF divorced from the model won't respond when an operating driver changes — the DCF will silently lie. Fix: assemble FCFF from linked EBIT, D&A, capex and NWC cells so any driver change flows through; add the NI-route check row to prove it reconciles.

**D7.** *"My terminal (FY5) year has capex at 10% of revenue and D&A at 4%, and I extend FY5 straight into perpetuity."*

Error: capex far above D&A is a *growth* profile, not a steady state; perpetuating it understates FCFF forever and distorts terminal value. Fix: converge the final year toward capex ≈ D&A before capitalising into perpetuity, reflecting a mature company that only replaces worn assets.

**D8.** *"My EBITDA-route and EBIT-route FCFF differ by the full D&A amount."*

Error: on the EBITDA route you likely added back the *full* D&A after taxing EBITDA, instead of only the tax shield on D&A. The correct EBITDA formula is `EBITDA×(1−t) + D&A×t − CapEx − ΔNWC` — add back `D&A×t`, not `D&A`, because EBITDA already contains the pre-tax D&A. Fix that term and the two routes reconcile exactly (see B3).

---

*Reconciliation habit to carry forward: a valuation-grade FCFF line should tie out from EBIT, EBITDA and net income to the same number, respond automatically to every operating driver, and pair only ever with WACC. When all three routes read "OK" and a margin tweak ripples cleanly through the PV total, you have an engine ready for terminal value in Chapter 23.*
