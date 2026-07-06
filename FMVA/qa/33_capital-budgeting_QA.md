# Q&A — Capital Budgeting

Practice bank for Chapter 33. Work each question before reading the answer. The chapter rests on one discipline — **decide on incremental, after-tax cash flows discounted at the opportunity cost of capital, and let NPV be the tie-breaker** — and one workhorse identity, `OCF = (Sales − Costs − Dep)×(1−t) + Dep`. A single project ("**Project Zeta**") runs through Section B so every number is reproducible cell-for-cell in Excel and reconciles by at least two independent routes.

**Project Zeta reference case:** equipment cost 120,000 at t0; life 4 years; straight-line depreciation to zero (30,000/yr); incremental sales 100,000/yr; incremental cash operating costs 45,000/yr (so EBITDA 55,000); tax 30%; net working capital of 10,000 invested at t0 and fully recovered at t4; salvage 0; cost of capital (WACC) 12%.

---

## Section A — Concept Checks (test the WHY)

**A1. What is capital budgeting actually deciding?**

Whether committing cash today to a long-lived asset creates more value than the next-best use of that same cash. It is a *value* question, not a *profit* question — the yardstick is the opportunity cost of capital, and the verdict is whether the project's discounted cash inflows exceed its outflows.

**A2. Why do we discount cash flows rather than accounting profits?**

Because cash pays the bills and accrual profit does not. Depreciation reduces reported profit though no cash leaves; the capex cash outflow never touches the income statement; revenue booked on credit isn't yet collected. Accounting profit misstates both the amount and the *timing* of cash, and the time value of money is entirely about timing. Only cash can be reinvested or paid out, so only cash can be discounted honestly.

**A3. What makes a cash flow "incremental," and why is that the only cash flow that counts?**

Incremental means *with the project minus without it* — the change in the firm's total cash flows caused by accepting the project. That is the only thing the decision changes, so it is the only thing the decision should weigh. It forces you to ignore sunk costs (already spent, unchangeable), include opportunity costs (cash foregone by using a resource here), and capture side-effects like erosion of an existing product's sales.

**A4. Sunk cost vs opportunity cost — define each and its treatment.**

A **sunk cost** is cash already spent that no decision can now recover (e.g. a completed 2m feasibility study) — it is *excluded* because it's identical with or without the project. An **opportunity cost** is the value a resource would earn in its best alternative use (e.g. the market rent of a warehouse you'd otherwise lease out) — it is *included* as a cost, because using the resource here forfeits that cash.

**A5. Why is depreciation added back in the operating cash flow build, yet still matters?**

Depreciation is a non-cash charge, so to get to cash you add it back after it has done its one useful job: shielding income from tax. The shield is worth `Depreciation × tax rate` in cash each year. So depreciation never *is* a cash flow, but it *creates* one — the tax it saves.

**A6. Why does an increase in net working capital reduce a project's cash flow, and why is it recovered at the end?**

Growth ties cash up in receivables and inventory net of payables — cash the project consumes but the income statement never shows. At the project's end that working capital unwinds (last receivables collected, last inventory sold, payables settled), releasing the cash back. Omitting the recovery understates terminal-year cash and NPV.

**A7. NPV vs IRR — what does each answer, and why is NPV the senior rule?**

NPV answers "how many dollars of value does this create?" — an absolute, currency amount that is directly additive across projects. IRR answers "what compound return does it earn?" — a percentage. NPV is senior because it (a) assumes reinvestment at the realistic cost of capital rather than IRR's own optimistic rate, (b) never multiplies into two answers, and (c) correctly ranks mutually exclusive projects of different size or timing. When they disagree, follow NPV.

**A8. Why can IRR be unreliable or even multiple-valued?**

IRR solves a polynomial: an *n*-period cash-flow stream can have as many roots as sign changes (Descartes' rule). A conventional project (one sign change: outflow then inflows) has one IRR. A stream that flips sign more than once — e.g. a big decommissioning outflow at the end — can produce two or more IRRs or none, all economically meaningless. NPV always returns a single, well-defined number.

**A9. What is the profitability index, and when is it the right tool?**

PI = PV of future cash inflows ÷ initial investment. It is NPV re-expressed as "value per dollar invested" (PI = 1 + NPV/investment). Under **capital rationing** — a hard budget cap — you can't just take every positive-NPV project, so you rank by PI to squeeze the most value out of each scarce dollar.

**A10. Two mutually exclusive projects have different lives. Why can't you compare NPVs directly, and what fixes it?**

A 3-year and a 7-year machine chosen "once" aren't comparable — the shorter one frees capital to redeploy sooner. Convert each NPV to an **equivalent annual annuity** (EAA = NPV ÷ annuity factor for that life), which is the level per-year value, and compare those. Equivalently, compare over a common horizon (least common multiple of the lives).

---

## Section B — Build / Computational Problems

*Reproduce each in Excel. Link inputs by cell reference; the arithmetic is shown so it self-checks. All figures use Project Zeta above.*

**B1. Build the annual operating cash flow two ways.**

Route 1 — top-down: `OCF = (Sales − Costs − Dep)×(1−t) + Dep = (100,000 − 45,000 − 30,000)×0.70 + 30,000 = 25,000×0.70 + 30,000 = 17,500 + 30,000 = 47,500.`
Route 2 — tax-shield: `OCF = (Sales − Costs)×(1−t) + Dep×t = 55,000×0.70 + 30,000×0.30 = 38,500 + 9,000 = 47,500.` ✓

Both give **OCF = 47,500/yr**. The agreement proves the depreciation tax shield (9,000) is counted once and correctly.

**B2. Assemble the full incremental FCF timeline.**

| | t0 | t1 | t2 | t3 | t4 |
|---|---:|---:|---:|---:|---:|
| Equipment | (120,000) | | | | |
| NWC | (10,000) | | | | +10,000 |
| Operating CF | | 47,500 | 47,500 | 47,500 | 47,500 |
| **Net FCF** | **(130,000)** | **47,500** | **47,500** | **47,500** | **57,500** |

t0 = −(120,000 + 10,000) = −130,000; t4 adds the 10,000 NWC recovery to OCF → 57,500. Salvage is 0, so no terminal asset sale.

**B3. Compute NPV at 12%.**

| | t1 | t2 | t3 | t4 |
|---|---:|---:|---:|---:|
| Factor 1/1.12^n | 0.89286 | 0.79719 | 0.71178 | 0.63552 |
| PV of FCF | 42,410.7 | 37,866.7 | 33,809.6 | 36,542.3 |

Sum of PVs = 42,410.7 + 37,866.7 + 33,809.6 + 36,542.3 = **150,629.3**.
`NPV = 150,629.3 − 130,000 = 20,629.` **NPV ≈ +20,629 → accept.** (Spot-check t4: 57,500 × 0.63552 = 36,542.3 ✓.)

**B4. Find the IRR by interpolation.**

IRR is the rate where PV of inflows = 130,000. Test-discount the B2 stream:
- At 19%: PVs 39,916 + 33,543 + 28,187 + 28,674 = 130,320 → NPV = **+320.**
- At 20%: PVs 39,583 + 32,986 + 27,488 + 27,730 = 127,787 → NPV = **−2,213.**

Interpolate: `IRR ≈ 19% + 320/(320 + 2,213) × 1% = 19% + 0.13% ≈ 19.1%.`
**IRR ≈ 19.1%**, comfortably above the 12% hurdle — same accept verdict as NPV, as it must be for a conventional (single sign-change) project.

**B5. Compute payback and discounted payback.**

Undiscounted cumulative: t1 47,500 → t2 95,000 → t3 142,500. The 130,000 is recovered during year 3: `Payback = 2 + (130,000 − 95,000)/47,500 = 2 + 0.737 = 2.74 years.`

Discounted cumulative (from B3): 42,410.7 → 80,277.4 → 114,087.0 → 150,629.3. Recovered during year 4: `Disc. payback = 3 + (130,000 − 114,087.0)/36,542.3 = 3 + 0.435 = 3.44 years.` Discounting always lengthens payback because early dollars are shrunk.

**B6. Compute the profitability index and the MIRR.**

PI: `= PV of inflows / investment = 150,629.3 / 130,000 = 1.159.` PI > 1 ⇔ NPV > 0 — the same signal, per dollar.

MIRR: compound each inflow to t4 at the 12% cost of capital, then annualise against the t0 outflow.
Terminal value = 47,500×1.12³ + 47,500×1.12² + 47,500×1.12 + 57,500 = 66,734.1 + 59,584.0 + 53,200.0 + 57,500 = **237,018.1.**
`MIRR = (237,018.1 / 130,000)^(1/4) − 1 = 1.82322^0.25 − 1 = 16.20%.`
Sanity: MIRR (16.2%) sits *between* WACC (12%) and IRR (19.1%) — exactly where the reinvestment-corrected return belongs.

**B7. Equivalent annual annuity for an unequal-life comparison.**

Zeta's NPV is 20,629 over a 4-year life. The 4-year annuity factor at 12% = (1 − 1.12⁻⁴)/0.12 = 0.364482/0.12 = 3.03735.
`EAA = 20,629 / 3.03735 = 6,792/yr.` If a rival 6-year machine returned an EAA below 6,792, Zeta wins despite the shorter life; if above, the rival wins — because EAA neutralises the life difference by spreading each NPV into a level annual value.

**B8. NPV–IRR conflict on two mutually exclusive projects, plus the crossover rate.** Cost of capital 10%.
- **Project A:** −10,000 now, +12,000 at t1.
- **Project B:** −10,000 now, 0 at t1, +13,500 at t2.

IRRs: A → 12,000/10,000 − 1 = **20.0%**. B → √(13,500/10,000) − 1 = √1.35 − 1 = **16.19%.**
NPVs at 10%: A = 12,000/1.10 − 10,000 = 10,909.1 − 10,000 = **+909.1.** B = 13,500/1.21 − 10,000 = 11,157.0 − 10,000 = **+1,157.0.**

Conflict: A has the higher IRR (20% > 16.19%) but B has the higher NPV (1,157 > 909). Since they're mutually exclusive, **follow NPV → take B.**
Crossover rate (set NPVs equal): 12,000/(1+r) = 13,500/(1+r)² → 12,000(1+r) = 13,500 → 1+r = 1.125 → **r = 12.5%.** Below 12.5% B dominates; above, A does. The 10% hurdle is below the crossover, confirming B — the NPV answer.

**B9. Excel reconciliation check row.**

Guard the two OCF routes from B1: `=IF(ROUND(OCF_route1 − OCF_route2, 0)=0, "OK", "ERR")`. And verify the model's NPV cell against the primitives: `=IF(ROUND(NPV(0.12,C_t1:C_t4)+C_t0, 0)=ROUND(ManualNPV,0),"OK","ERR")` — note `NPV()` discounts its first argument as t1, so the t0 outflow is added *outside* the function.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through building a project's free cash flow for a capital budgeting decision."**

Start with incremental EBITDA — the extra sales the project brings less its extra cash costs. Tax it, but give credit for the depreciation tax shield: I use `(Sales − Costs − Dep)×(1−t) + Dep`, which taxes operating profit and then adds back depreciation because it's non-cash. Then I layer on the capital items the income statement misses: the initial capex outflow and any net working capital the project ties up, both up front, with the working capital recovered at the end and any salvage (net of tax on gain) at disposal. Financing costs — interest, principal — stay out entirely; they live in the discount rate. Discount the resulting stream at the cost of capital and the sign of the NPV is the decision.

**C2. "Why do you exclude interest expense from project cash flows when the project is partly debt-funded?"**

Because the cost of debt is already inside the discount rate. WACC blends the after-tax cost of debt and the cost of equity, so discounting at WACC charges the project for its financing. If I also subtracted interest from the cash flows, I'd count the financing cost twice and understate value. The clean separation is: cash flows capture the *operating* story unlevered, the discount rate captures the *financing* story once.

**C3. "A colleague ranks two mutually exclusive projects by IRR and picks the higher one. When is that wrong?"**

Whenever the projects differ in scale or in cash-flow timing, which is most of the time. IRR is a rate, blind to size — a 30% return on 10 can be worth less in dollars than an 18% return on 100. And IRR implicitly assumes interim cash is reinvested at the IRR itself, which flatters high-IRR projects. The correct rule for mutually exclusive choices is highest NPV, because NPV measures actual value created and assumes reinvestment at the realistic cost of capital. I'd show the crossover rate to make the disagreement concrete, then defer to NPV.

**C4. "The sunk cost fallacy — give me a capital budgeting example and the right treatment."**

A firm has spent 2m on R&D for a product and now decides whether to spend 8m to launch. The 2m is gone regardless of the launch decision, so it must be excluded — the launch is evaluated purely on the incremental 8m against the incremental cash inflows it generates. Including the 2m to "recoup it" would wrongly reject value-creating launches or, worse, chase good money after bad. The only relevant question is forward-looking: does the incremental future cash beat the incremental future cost?

**C5. "How do you handle a project that cannibalises an existing product?"**

The lost margin on the existing product is an incremental cost of the new project and must be subtracted from its cash flows — that's erosion. But only the *genuinely* lost sales count: if competitors would have taken those customers anyway, that portion isn't caused by our project and shouldn't be charged against it. The test is always "with the project versus without it," and erosion is one of the classic side-effects that test is designed to catch, alongside opportunity costs and synergy benefits to other lines.

**C6. "Two machines do the same job; one is cheaper but shorter-lived. How do you choose?"**

I can't compare their NPVs directly because they occupy the asset slot for different lengths of time — the shorter machine frees capital to redeploy sooner. I convert each project's NPV into an equivalent annual annuity, the level yearly value over its own life, and pick the higher EAA. Equivalently I'd replicate each over the least common multiple of the two lives and compare NPVs over that common horizon. Either way the point is to put both on a per-year footing before judging.

---

## Section D — Common-Error Spotting

*Each item states a modeling move. Identify the error and give the fix.*

**D1.** *"The analyst used net income as the project's annual cash flow."*
Net income is after non-cash depreciation and possibly after interest. Fix: build operating cash flow — add depreciation back for its non-cash nature (keeping only its tax shield) and strip out any financing. Cash, not accrual profit, is discounted.

**D2.** *"Depreciation was both added back AND the full capex subtracted every year."*
Double counting the asset. Capex is a one-time outflow at purchase (t0); depreciation thereafter is only added back as a non-cash charge. You don't expense the machine twice — once as capex, again as annual depreciation cash.

**D3.** *"Interest expense on the project loan was subtracted from the cash flows, and the flows were discounted at WACC."*
Financing counted twice — once in the cash flow, once in the WACC. Fix: remove interest from the cash flows; let the after-tax cost of debt inside WACC carry the financing cost.

**D4.** *"A completed 500k market study was added as a year-0 project cost."*
Sunk cost. Already spent, unaffected by the accept/reject decision, so it's excluded. Only incremental future cash flows belong in the analysis.

**D5.** *"A warehouse the firm already owns was treated as free because 'we paid for it years ago.'"*
Missing opportunity cost. The warehouse could be leased out or sold; its foregone market value (net rent or sale proceeds) is a real incremental cost of using it for this project and must be included.

**D6.** *"Working capital was invested at t0 but never recovered at project end."*
Terminal cash understated. At wind-down, receivables are collected and inventory sold, releasing the working capital — add it back in the final year. Omitting it understates NPV.

**D7.** *"Real (inflation-free) cash flows were discounted at a nominal WACC."*
Rate/flow mismatch. Discount nominal cash flows at a nominal rate, or real flows at a real rate — never cross them, or inflation is either double-counted or ignored.

**D8.** *"A project with a large end-of-life cleanup outflow was ranked by its IRR, which the tool reported as 8%."*
Two sign changes (outflow, inflows, outflow) can yield multiple IRRs, so any single reported IRR is suspect. Fix: decide by NPV, which is always single-valued; use MIRR if a rate is needed.

**D9.** *"Two mutually exclusive projects of different size were ranked by profitability index."*
PI ranks well under capital rationing but can mislead for mutually exclusive choices, favouring the small project with high value-per-dollar over the large project with more total value. Fix: for a straight mutually exclusive pick with no budget cap, rank by NPV.

**D10.** *"The discount rate used was the project's own IRR."*
Circular and wrong. The discount rate is the opportunity cost of capital — the return available on equivalent-risk alternatives (WACC or a risk-adjusted rate) — set independently of the project. Using the IRR guarantees NPV = 0 and destroys the test.
