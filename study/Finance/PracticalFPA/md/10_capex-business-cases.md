# Capex, project appraisal & business cases

## What it is & where it's used

**Capex (capital expenditure)** is money spent to acquire or upgrade long-lived assets — a new plant, a fleet of delivery vans, an ERP rollout, a warehouse, machinery. Unlike opex (rent, salaries, electricity — expensed in the year), capex sits on the balance sheet and depreciates over years. **Project appraisal** is the discipline of deciding *which* capex is worth doing, and a **business case** is the document that carries that recommendation to the people who sign the cheque.

Every rupee of capex is a bet: pay cash now, receive uncertain cash later. The job is to convert that bet into three numbers — **NPV, IRR, payback** — plus a written argument, and defend it.

Where this skill lives:
- **FP&A analyst** — builds the model, runs sensitivities, owns the capex tracker.
- **Corporate finance / business finance partner** — writes the business case, presents to the investment committee.
- **Treasury** — checks it against the WACC and funding plan.
- **Internal audit / controllership** — runs the **post-investment review** (did we get what we promised?).
- Startups, PE portfolio finance, project finance (infra, renewables) — the entire deal *is* an appraisal.

## The gap: why companies want this (and college didn't teach it)

College teaches you to compute NPV from a clean table of cash flows handed to you. Industry never hands you the cash flows — **you build them**, and 90% of the skill is in the assumptions, not the discounting.

Specific gaps a fresh MBA/CA has:
- **You discount profit instead of cash.** Textbooks blur PAT and cash flow. In practice you must add back depreciation, adjust for working capital, and handle tax on *cash* terms.
- **You ignore the tax shield on depreciation.** In India, depreciation is a WDV block under the Income Tax Act — it changes the cash flows and nobody in college models it.
- **You treat sunk costs and allocated overheads as relevant.** They aren't. Only *incremental* cash flows count.
- **You never touch terminal value, working-capital release, or salvage.**
- **You've never written the one-page ask** that a CFO actually reads, or been forced to say "here's what kills this project."
- **Post-investment review** — closing the loop — is not taught at all, yet it's what auditors and boards demand.

## What "proficient" looks like

A job-ready person can, unaided:

1. Build a **10-year DCF for a project** in Excel from raw assumptions — revenue driver, cost ramp, capex phasing, working capital, tax, depreciation shield, salvage/terminal value.
2. Compute **NPV, IRR, discounted payback, and profitability index** with the correct sign convention and timing (year-0 outflow).
3. Choose the **right discount rate** (WACC or a hurdle rate) and explain *why*.
4. Run a **sensitivity / scenario / tornado** analysis and name the 2-3 variables that actually swing the decision.
5. Write a **one-page business case**: problem, options, recommendation, financials, risks, ask.
6. Design and run a **post-investment review** 12-18 months later against the original baseline.
7. Know the **decision rules and their traps** — IRR on non-conventional cash flows, mutually exclusive projects, capital rationing.

## Hands-on: how to actually do it

### The cash-flow engine (this is the whole game)

Free cash flow to the project each year:

```
FCF = (Revenue − Cash Costs − Depreciation) × (1 − tax)
      + Depreciation                      ← add back non-cash
      − Capex
      − ΔWorking Capital
```

The `Depreciation × tax` piece is the **tax shield** — it's why depreciation belongs in the model even though it's non-cash.

### Core Excel formulas (copy-usable)

Lay years across columns. Put the initial outlay in **Year 0**.

```
NPV (correct way — year-0 outflow is NOT discounted):
=B10 + NPV(rate, C10:L10)          ' B10 = Year-0 cash flow (negative), C10:L10 = Years 1-10

IRR:
=IRR(B10:L10)

XIRR / XNPV (when dates are irregular — use these in real deals):
=XNPV(rate, B10:L10, B1:L1)         ' B1:L1 = actual dates
=XIRR(B10:L10, B1:L1)

Discounted payback — cumulative discounted CF crosses zero:
Discount factor:   =1/(1+$B$2)^C$1
Discounted CF:     =C10*C_DF
Cumulative:        =B_cum + C_disc
Payback year (approx): =MATCH(TRUE, cum_range>0, 0)

Profitability Index:
=NPV(rate,C10:L10) / -B10           ' PV of inflows / initial outlay
```

**Common trap:** `=NPV(rate, B10:L10)` is *wrong* if B10 is the Year-0 outflow — Excel's NPV assumes the first value is one period away. Always keep Year 0 outside the NPV() and add it.

### Depreciation & tax shield — India (WDV block method)

Income-tax depreciation is on the **block of assets** at WDV rates (e.g. plant & machinery general block = 15%). Book depreciation (Companies Act, Schedule II, often SLM over useful life) differs — model the **income-tax** one for cash tax.

```
WDV depreciation, Year n:
=Opening_WDV * 15%
Closing_WDV = Opening_WDV − Dep         ' carries to next year's opening
```

Also model the **additional depreciation** (20% extra in year of purchase for new plant in manufacturing, where still applicable) if relevant.

### Sensitivity in Excel

Use a **Data Table** (What-If Analysis → Data Table). Put NPV in a corner cell `=NPV_cell`, discount rates down the left, a swing variable across the top. For a one-way tornado, flex each input ±10% and chart the NPV delta.

### Python — same appraisal, reproducible

```python
import numpy_financial as npf
import numpy as np

cf = [-500, 120, 140, 160, 180, 200]   # Year 0..5, in ₹ lakh
rate = 0.13                             # WACC 13%

npv = cf[0] + npf.npv(rate, cf[1:])     # or npf.npv(rate, cf) if cf[0] is t=0-discounted convention
irr = npf.irr(cf)
disc = [c/(1+rate)**t for t, c in enumerate(cf)]
cum = np.cumsum(disc)
payback = next(t for t, v in enumerate(cum) if v > 0)

print(f"NPV ₹{npv:,.1f}L | IRR {irr:.1%} | Disc. payback ~Yr {payback}")
```

Note: `npf.npv` treats the first element as t=0 (already un-discounted), so pass the whole `cf` list directly — different convention from Excel. Verify once with a hand calc.

### Journal entries — when capex actually hits the books

| Event | Dr | Cr | Amount |
|---|---|---|---|
| Purchase machine on credit | Plant & Machinery | Vendor payable | ₹50,00,000 |
| GST input on capital goods | Input CGST/SGST (ITC) | Vendor payable | ₹9,00,000 |
| Installation cost (capitalise) | Plant & Machinery | Bank | ₹2,00,000 |
| Year-end depreciation (Schedule II) | Depreciation expense | Accumulated depreciation | ₹5,20,000 |
| Salvage on disposal | Bank / Accum. dep. | Plant & Machinery / Gain | at exit |

ITC on capital goods is fully available (not amortised over 60 months post-2017, except for the common-credit reversal rule under Rule 43 if used partly for exempt supplies).

## Worked example / mini-project

**Project:** A mid-size Indian manufacturer evaluates a new packaging line.

Assumptions:
- Capex ₹500 lakh, installed Year 0. Life 5 years, salvage ₹50 lakh.
- Incremental revenue ₹400 lakh/yr; cash costs 55% of revenue.
- Working capital = 15% of revenue, built in Year 0, released in Year 5.
- Tax 25%. WACC 13%. Depreciation for cash tax: WDV 15%.

**Working-capital block** = 15% × 400 = ₹60 lakh outflow at Year 0, released Year 5.

| ₹ lakh | Yr 0 | Yr 1 | Yr 2 | Yr 3 | Yr 4 | Yr 5 |
|---|---|---|---|---|---|---|
| Revenue | | 400 | 400 | 400 | 400 | 400 |
| Cash costs (55%) | | −220 | −220 | −220 | −220 | −220 |
| WDV Dep @15% | | −75 | −64 | −54 | −46 | −39 |
| PBT | | 105 | 116 | 126 | 134 | 141 |
| Tax @25% | | −26 | −29 | −31 | −34 | −35 |
| PAT | | 79 | 87 | 94 | 101 | 106 |
| + Dep (add back) | | 75 | 64 | 54 | 46 | 39 |
| − Capex | −500 | | | | | |
| − ΔWC | −60 | | | | | +60 |
| + Salvage (net) | | | | | | +50 |
| **FCF** | **−560** | **154** | **151** | **149** | **147** | **255** |

Now the numbers (rate 13%):

```
NPV  = −560 + 154/1.13 + 151/1.13² + 149/1.13³ + 147/1.13⁴ + 255/1.13⁵
     ≈ −560 + 136 + 118 + 103 + 90 + 138  ≈  ₹125 lakh   → POSITIVE, accept
IRR  ≈ 21%   (> 13% WACC → accept)
Discounted payback ≈ 4.3 years
PI   = (560+125)/560 ≈ 1.22   (>1 → accept)
```

**One-page business-case skeleton** you'd attach:
1. **Problem/opportunity** — current line at 95% capacity; turning away ₹400L of orders.
2. **Options** — (a) do nothing, (b) outsource, (c) new line. Recommend (c).
3. **Financials** — NPV ₹125L, IRR 21%, payback 4.3 yrs, PI 1.22.
4. **Risks & sensitivity** — NPV turns negative if revenue falls >18% or costs exceed 63%. Volume is the swing variable.
5. **The ask** — approve ₹560L capex+WC; funded from internal accruals; go-live Q3.

## How it's tested

**Interview questions:**
- "Walk me through building free cash flow for a project from scratch." (They want dep add-back, WC, tax shield, capex phasing.)
- "NPV vs IRR — which do you trust for two mutually exclusive projects, and why?" (NPV; IRR can mislead on scale and reinvestment.)
- "A project has two IRRs — what happened?" (Non-conventional cash flows / sign changes; use NPV or MIRR.)
- "What discount rate did you use and why?" (WACC for average-risk; risk-adjusted hurdle otherwise.)
- "Payback ignores what?" (Time value and cash flows after payback — that's why it's a screen, not a decision rule.)

**Practical tests companies give:**
- A **timed 30-45 min Excel case**: raw assumptions in one tab, "return NPV/IRR/payback and a recommendation." They check the year-0 handling, the tax shield, and whether your formulas are dynamic (change an input, does NPV update).
- A **business-case writing test**: given a scenario, produce a one-pager with a recommendation.
- A **"critique this model"** test: they hand you a flawed model and ask what's wrong (sunk cost included, NPV discounting year 0, hard-coded values).

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Discounting Year-0 outflow inside `NPV()` | Keep Yr 0 outside: `=B10+NPV(rate,C10:L10)` |
| Including **sunk costs** (already-spent feasibility study) | Only incremental future cash flows are relevant |
| Allocating **corporate overhead** that won't change | Include only *incremental* overhead |
| Discounting **PAT instead of FCF** | Add back depreciation, adjust working capital |
| Ignoring the **depreciation tax shield** | Model it; it can flip a marginal NPV |
| Forgetting **working-capital release** and **salvage** at the end | Add both in the terminal year |
| Comparing projects of **different lives** on raw NPV | Use equivalent annual annuity (EAA) |
| Trusting **IRR** on non-conventional flows | Use NPV or MIRR |
| Nominal cash flows discounted at a **real** rate (or vice versa) | Match: nominal↔nominal, real↔real |
| No **post-investment review** | Bake the baseline into the approval so it can be audited |

**Post-investment review (PIR)** — the pro move most people skip. 12-18 months after go-live, pull actual capex, actual revenue/cost, actual payback, and compare to the approved case. Document variances and *why*. This is what internal audit and the board look for, and it's how the FP&A team gets its next forecast right.

## Learn-it roadmap & resources

**Time to proficiency:** 3-4 weeks of focused practice to pass an Excel appraisal test; 2-3 months to write business cases confidently.

- **Week 1** — DCF mechanics: build 5 project models by hand in Excel; drill NPV/IRR/XNPV/XIRR/PI.
- **Week 2** — Cash-flow building: incremental analysis, tax shield, WC, terminal value, EAA, MIRR.
- **Week 3** — Sensitivity, scenario, Data Tables, tornado charts; Python `numpy_financial`.
- **Week 4** — Write 3 one-page business cases; design a PIR template.

**Resources:**
- CFA Level I / II "Corporate Issuers — Capital Budgeting" readings (free curriculum outlines; the clearest treatment).
- ICAI CA Inter **Financial Management** — Capital Budgeting chapter (India tax + depreciation context, free study material).
- Damodaran Online (NYU) — free capital budgeting lectures and spreadsheets.
- CFI's **Financial Modeling & Valuation Analyst (FMVA)** — paid, hands-on, good for the Excel muscle.
- `numpy-financial` docs for Python; Microsoft Excel Data Table / What-If docs.

**Certifications that signal this skill:** CFA, FMVA, CIMA/CMA, and for India the CA qualification itself.

## Quick-reference

| Metric | Formula / rule | Accept if |
|---|---|---|
| **NPV** | `=B0 + NPV(rate, Yr1:YrN)` | NPV > 0 |
| **IRR** | `=IRR(range)` / `=XIRR(cf, dates)` | IRR > WACC/hurdle |
| **Discounted payback** | cumulative discounted CF crosses 0 | ≤ target years |
| **Profitability Index** | PV inflows ÷ initial outlay | PI > 1 |
| **MIRR** | `=MIRR(cf, fin_rate, reinv_rate)` | > hurdle (use for weird flows) |
| **EAA** | `NPV × rate / (1−(1+rate)^−n)` | higher, for unequal lives |

**Free cash flow:** `(Rev − CashCost − Dep) × (1−t) + Dep − Capex − ΔWC`
**Tax shield:** `Depreciation × tax rate`
**India WDV P&M general block:** 15%; **book dep:** Schedule II (SLM/WDV over useful life)
**GST:** ITC on capital goods fully available (watch Rule 43 reversal for exempt use)
**Decision hierarchy:** NPV rules > IRR; screen with payback; rank under rationing by PI.
**Only relevant cash flows:** incremental, future, after-tax. Ignore sunk costs & unchanged overhead.
**Always close the loop:** approve with a baseline → post-investment review at 12-18 months.
