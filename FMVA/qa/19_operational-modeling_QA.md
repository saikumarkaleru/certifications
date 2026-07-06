# Q&A — Operational Modeling

Practice bank for Chapter 19. Work each question before reading the answer. The chapter's engine is one sentence — *money is quantity times price, so forecast the quantity in its real units and price it, rather than guessing the money directly.* Every build below rolls a stock forward, averages the base, respects timing, and caps at capacity, so you can reproduce each figure cell-for-cell in Excel and watch it reconcile.

---

## Section A — Concept Checks (test the WHY)

**A1. What is the single defining feature of an operational (driver-based) model versus a percentage-growth model?**

Revenue is an *output*, not an input. A percentage model types `= Prior × (1 + Growth%)` and the growth cell is a hard-coded guess. An operational model builds the top line from the physical units of the business — stores × revenue-per-store, subscribers × ARPU, units × price — so the currency figure *falls out* of an operational grid. Every number traces to a testable claim about how the business runs.

**A2. Why must a stock (stores, subscribers, machines, heads) be carried as a roll-forward rather than typed each period?**

Because `Ending = Beginning + Additions − Losses`, and the *next* period's beginning must link to *this* period's ending. Hard-typing an ending balance silently desynchronises the grid the moment any flow changes, and it destroys auditability. The roll-forward guarantees continuity — change one opening balance or one flow and the whole horizon re-computes correctly.

**A3. Why average the stock when it drives a revenue flow, instead of using the ending balance?**

Because additions arrive *through* the period, not on day one. If you add 24 stores evenly across a year, the count that actually earned revenue is roughly beginning + 12, i.e. the average — not the ending count of beginning + 24. Multiplying full-year revenue-per-unit by the *ending* count overstates the growth year. `AVERAGE(Begin, End)` is the coarse fix; a monthly build is the precise one.

**A4. Why is churn applied to the *opening* subscriber base rather than the ending or average base?**

Because customers who are present at the start of the period are the ones exposed to leaving during it: `Churned = Subs_begin × Churn%`. New adds acquired mid-period have not yet had a full period to churn. Applying churn to the ending base double-taxes the new adds and understates the true loss dynamics; it can also mask a shrinking base.

**A5. Why should rent and store labour be driven by store *count*, not by a percentage of revenue?**

Because they are fixed-per-store costs, not variable-with-sales costs. A lease costs the same whether the store has a great month or a terrible one. Model rent as `% of revenue` and a same-store-sales *decline* makes rent *fall* — economic nonsense. Drive per-store fixed costs off the store count; reserve `% of revenue` for genuinely variable items (COGS, card fees).

**A6. Why does the `MIN(Demand, Capacity × MaxUtil%)` ceiling matter so much in a manufacturing model?**

Because you cannot sell what you cannot make. Without the `MIN`, an optimistic demand assumption lets the model book revenue the plant physically cannot produce — the single most common overstatement in industrial forecasts. The ceiling strands excess demand *and*, via a trigger flag, tells management the exact year a new line must be funded.

**A7. Why is "doubling churn roughly halves LTV" a structural truth, not a coincidence?**

Because average customer lifetime = `1 / monthly churn`. At 2% monthly churn, life = 50 months; at 4%, life = 25 months. Since `LTV = ARPU × GM% × life`, and only the *life* term changed, halving the life halves the LTV. Churn is the most leveraged assumption in a subscription model precisely because it sits in the denominator of lifetime.

**A8. Why must new revenue-generating hires (or new stores) carry a productivity ramp?**

Because a salesperson hired today is not at full quota for months, and a store opened this month has not built its customer base. Assuming day-one full productivity front-loads revenue that will not arrive for several quarters. A ramp vector (e.g. 0% → 25% → 50% → 100% over four quarters) phases contribution in realistically and is what separates a credible model from a fantasy.

**A9. Why must the operational layer flow one way into the statements, and never receive a feedback link from them?**

Because drivers → operations → statements is a clean, acyclic chain. If a statement line fed back into the operational grid it would create circularity beyond the one deliberate loop (interest on average debt) that belongs *inside* the statements. Keeping the arrow pointing one way makes the model auditable and keeps the operational sheet the single source of truth.

---

## Section B — Build / Computational Problems

Reproduce each in Excel; the arithmetic is shown so it self-checks. Currency figures in thousands (000s) unless noted.

**B1. Retail store roll-forward, average, and revenue.** A chain starts Year 1 with **30 stores**, opens **12/year**, closes **3/year**. Revenue per store is **900/year**, growing at same-store sales of **5%/year**. Build the roll-forward and revenue for three years.

Roll-forward `Ending = Begin + Openings − Closures`; `Avg = AVERAGE(Begin, End)`; `Rev/store(t) = Rev/store(t−1) × 1.05`; `Revenue = Avg × Rev/store`:

| | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Stores begin | 30 | 39 | 48 |
| Openings | 12 | 12 | 12 |
| Closures | −3 | −3 | −3 |
| **Stores end** | **39** | **48** | **57** |
| Average stores | 34.5 | 43.5 | 52.5 |
| Rev per store | 900.00 | 945.00 | 992.25 |
| **Revenue** | **31,050.0** | **41,107.5** | **52,093.1** |

Verify: end Y1 = 30 + 12 − 3 = 39, which carries to Y2 begin ✓. Avg Y1 = (30+39)/2 = 34.5 ✓. Rev/store Y3 = 900 × 1.05² = 992.25 ✓. Revenue Y3 = 52.5 × 992.25 = 52,093.1 ✓. Note revenue grew 32.4% Y1→Y2 while store count grew only 23% — the gap is the 5% same-store lift compounding on a larger average base.

**B2. SaaS subscriber roll-forward and unit economics (annual).** Start the year with **8,000 subscribers**, monthly churn **2.5%**, marketing spend **2,000**, CAC **200**, ARPU **35/month**, gross margin **75%**.

First convert monthly churn to annual: `1 − (1 − 0.025)¹² = 1 − 0.975¹² = 1 − 0.7380 = 26.2%`.

- Gross adds = `2,000,000 / 200` = **10,000**
- Churned = `8,000 × 26.2%` = **2,096** (on the opening base)
- Subs end = `8,000 + 10,000 − 2,096` = **15,904**
- Average subs = `(8,000 + 15,904) / 2` = **11,952**
- Revenue = `11,952 × (35 × 12)` = `11,952 × 420` = **5,019,840 ≈ 5.02m**

Unit economics:

| KPI | Formula | Value |
|---|---|---:|
| Avg lifetime (months) | 1 / 0.025 | 40 |
| LTV | 35 × 0.75 × 40 | **1,050** |
| CAC | 2,000,000 / 10,000 | **200** |
| **LTV/CAC** | 1,050 / 200 | **5.25×** |
| CAC payback (months) | 200 / (35 × 0.75) | **7.6** |

Verify: 0.975¹² = 0.7380 ✓; LTV/CAC of 5.25× clears the informal 3× health bar, and payback under 8 months is healthy. This business acquires customers profitably and could arguably spend *more* on marketing.

**B3. Manufacturing capacity ceiling, trigger, and operating leverage.** A plant has installed capacity **60,000 units/year**, max sustainable utilisation **85%** (so ceiling = 51,000), price **80/unit**, variable cost **50/unit**, fixed cost **900**. Demand: Y1 45,000; Y2 52,000; Y3 58,000.

`Units = MIN(Demand, 51,000)`; `Contribution/unit = 80 − 50 = 30`; `Operating profit = Units × 30 − 900,000`:

| | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Demand (units) | 45,000 | 52,000 | 58,000 |
| Capacity ceiling (85%) | 51,000 | 51,000 | 51,000 |
| **Units produced** | **45,000** | **51,000** | **51,000** |
| Utilisation actual | 75% | 85% | 85% |
| Trigger flag | OK | **ADD LINE** | **ADD LINE** |
| Revenue (000s) | 3,600 | 4,080 | 4,080 |
| Contribution (000s) | 1,350 | 1,530 | 1,530 |
| Less fixed | −900 | −900 | −900 |
| **Operating profit (000s)** | **450** | **630** | **630** |

Verify: Y2 demand 52,000 exceeds the 51,000 ceiling, so production caps at 51,000 and the flag fires; Y3 demand of 58,000 is stranded at 51,000 — the model refuses 7,000 units of phantom revenue (a 560 overstatement a percentage model would have booked). Operating leverage: revenue rose **13.3%** Y1→Y2 (3,600→4,080) while operating profit rose **40%** (450→630), because the 900 fixed cost spread over more units. That non-linear profit response is the signature of a capacity model.

**B4. Sales headcount build with loaded cost and productivity ramp.** You hire **8 reps** at the start of Year 1. Base salary **90**, benefits and payroll load **33.3%**. Fully-ramped quota is **400/rep/year** (100/quarter). Ramp vector across the first four quarters: **0%, 25%, 50%, 100%** of quota.

Loaded cost per rep = `90 × (1 + 0.333)` = **120**. Labour cost = `8 × 120` = **960**.

Bookings per rep in Year 1 = `100 × (0% + 25% + 50% + 100%)` = `0 + 25 + 50 + 100` = **175**.

- Team Year-1 bookings = `8 × 175` = **1,400**
- Fully-ramped run-rate = `8 × 400` = **3,200**
- Year-1 realised as % of run-rate = `1,400 / 3,200` = **43.75%**

Verify: the ramp means the team delivers under half its steady-state capacity in the hiring year, even though the full cost of 960 lands immediately. A model that ignored the ramp would book 3,200 of bookings against the same 960 — overstating first-year output by 1,800 and badly misjudging the payback on the sales hire.

**B5. Reconcile two revenue paths (the essential audit check).** For the B1 chain in Year 2, confirm revenue two independent ways. Path A (the build): `Average stores × Rev/store` = `43.5 × 945` = **41,107.5**. Path B (unit decomposition): compute revenue per store-month `945 / 12 = 78.75`, then `43.5 stores × 78.75 × 12 months` = `43.5 × 945` = **41,107.5**. The two paths tie exactly. If your two paths disagree by more than rounding, you have a timing or averaging error — the reconciliation is how you catch it before the number reaches the P&L.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through how you would build revenue for a retail chain operationally, in 60 seconds."**

I start with a store roll-forward: beginning stores plus openings minus closures equals ending stores, and I carry ending into next year's beginning. I take the average of beginning and ending because stores open through the year and only earn on average. I set a revenue-per-store figure and grow it by same-store-sales for the mature base. Revenue is average stores times revenue-per-store. Then I drive costs off their true driver — COGS as a percent of revenue because it is variable, but rent and store labour off the store *count* because they are fixed-per-store. Finally, openings times build-cost-per-store gives me capex, which feeds PP&E. Every P&L line links back to that grid, so nothing on the income statement is a bare guess.

**C2. "Why do you average the store or subscriber count instead of just using the year-end number? Isn't that less precise?"**

It is actually *more* accurate for the revenue base. Units are added through the year, so the ending count overstates what was live and earning. If I add 24 stores evenly, the ending count is beginning + 24 but the earning average is roughly beginning + 12. Using the ending count would overstate the growth year's revenue. The truly precise answer is to build monthly and let each cohort earn only from its open date — but where an annual model is adequate, `AVERAGE(begin, end)`, or a mid-period convention that assumes additions arrive halfway through, captures the timing correctly.

**C3. "A founder tells me churn crept from 2% to 4% monthly but 'it's only 2 points, no big deal.' React."**

It is a very big deal, and the maths is unforgiving. Average customer lifetime equals one divided by monthly churn, so 2% churn means a 50-month life and 4% means a 25-month life — the lifetime *halves*. Since lifetime value is ARPU times gross margin times lifetime, LTV roughly halves too. If they were at a healthy LTV/CAC of six, they are now near three, the danger line, and the subscriber roll-forward compounds the pain: churn hits the base every single month, so the steady-state size shrinks meaningfully. A "2-point" move on churn is the most leveraged change in the entire model.

**C4. "How do you decide between a monthly and an annual operational build?"**

It depends on how cohort-sensitive the business is. If contribution phases in over time — subscription cohorts churning monthly, stores ramping, sales reps on a productivity curve — I build monthly and roll up to annual with SUMIFS, because an annual model would systematically overstate the first-year contribution of anything added mid-year. If the business is stable and additions are modest relative to the base, an annual model with a half-year convention — additions counted as live for half the period — is accurate enough and far lighter to build and audit. The key discipline is deciding *before* I build, because retrofitting monthly granularity into an annual model is a full rebuild.

**C5. "How does the operational model connect to the three statements without creating circularity?"**

The flow is strictly one-directional: drivers feed the operational grid, and the statements *pull* from the grid by link. Revenue on the income statement links to the operating sheet's revenue row; COGS and labour link to their driven cost rows; capex from the capacity or store build feeds PP&E and the investing section of the cash flow; and working capital often scales off the operational base, like inventory per store. What never happens is a statement feeding *back* into the operational layer — that would introduce circularity beyond the one deliberate loop, interest on average debt, which lives inside the statements themselves. Keeping the operational layer strictly upstream is what keeps the whole model auditable.

---

## Section D — Common-Error Spotting

Each item shows a flawed approach and the correction.

**D1. Fixed cost modelled as a percent of revenue.**
Flawed: `Rent = Revenue × 8%`. When same-store sales fall, this makes rent fall too — but a lease does not shrink in a bad month. Fix: `Rent = Average_stores × Rent_per_store`. Drive per-store fixed costs off the store count; reserve percent-of-revenue for genuinely variable costs.

**D2. Ending balance drives full-year revenue.**
Flawed: `Revenue = Stores_end × Rev_per_store`. This assumes every store, including those opened in December, earned a full year. Fix: `Revenue = AVERAGE(Stores_begin, Stores_end) × Rev_per_store`, or build monthly so each store earns only from its open month. The ending-balance error systematically overstates every growth year.

**D3. Churn applied to the wrong base.**
Flawed: `Churned = Subs_end × Churn%` or `× Average_subs`. This taxes the freshly-acquired adds that have not yet had a period to leave. Fix: `Churned = Subs_begin × Churn%` — churn hits the customers present at the start of the period, before new adds arrive.

**D4. No capacity ceiling.**
Flawed: `Units = Demand`, so a 105,000 demand against a 90,000-capacity plant books all 105,000. Fix: `Units = MIN(Demand, Capacity × Max_util%)`, plus a trigger `IF(Demand > Capacity × Max_util%, "ADD LINE", "OK")`. Without the MIN, the model invents revenue the plant cannot physically produce, and a checks row (utilisation ≤ 100%) will never catch it because the utilisation calc itself is uncapped.

**D5. Base salary instead of loaded cost, and no ramp.**
Flawed: `Labour = Heads × Base_salary`, with new reps at full quota on day one. This understates the largest cost line by the 25–40% of benefits and payroll taxes, and overstates new-hire output. Fix: `Loaded_cost = Base_salary × (1 + Benefits%)` for the cost, and apply a productivity ramp vector (0% → 25% → 50% → 100%) so new-hire revenue phases in over quarters rather than landing all at once.

**D6. Broken roll-forward continuity.**
Flawed: hard-typing `Stores_end` as a number, or leaving next year's `Stores_begin` unlinked to this year's `Stores_end`. The grid silently desynchronises the moment a flow changes. Fix: every ending balance is a formula (`Begin + Additions − Losses`) and every beginning balance links to the prior period's ending — never a typed constant.

---

*Self-check: if your B1 two-path reconciliation ties to the cent, your B2 churn conversion gives 26.2%, your B3 trigger fires in Y2 with 40% profit growth on 13.3% revenue growth, and your B4 ramp shows the team at ~44% of run-rate in Year 1, you have internalised the four golden mechanics — roll-forward, average, timing, and the capacity ceiling — that make an operational model reconcile.*
