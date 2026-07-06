# Q&A — Cost and Expense Modeling

Practice bank for Chapter 09. Work each question before reading the answer. The heart of this chapter is a single discipline: separate the "beans" (variable costs) from the "rent" (fixed costs) so your model breathes like the real business. Every computational problem is built to reconcile two ways and to be reproducible cell-for-cell in Excel.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is copying last year's cost-to-revenue ratio across all forecast years — the "flat-percent" method — often silently wrong?**

Because it assumes *every* cost moves in perfect lockstep with sales — that rent rises when you sell more, that the CFO's salary scales with unit volume, that depreciation on a three-year-old machine tracks this year's revenue. None of that is true. Real businesses are a blend of fixed costs that stay put while volume moves and variable costs that genuinely scale. Blending them into one flat ratio erases the single most important dynamic in the business — operating leverage — and produces dead-flat margins forever, which almost never matches reality and instantly signals a lazy model to any reviewer.

**A2. Why does the fixed-plus-variable split forecast better than a single flat percentage?**

Because it matches the *causal structure* of the business rather than curve-fitting one ratio to last year's happenstance. A lease fixes rent regardless of sales; a raw-material bill is literally a function of units produced. Modeling each cost according to how it actually behaves means the model mirrors real causation — and a model that mirrors causation extrapolates better than one that assumes a coincidental ratio holds forever. It also replaces one opaque assumption ("COGS is 62% of revenue") with several transparent ones ("45% variable materials plus ₹170 fixed overhead") that you can stress independently.

**A3. Why do margins *expand* as a fixed-plus-variable business grows?**

Because the fixed cost base is spread over more units of revenue. The variable portion stays a constant fraction of each sales rupee, but the fixed portion becomes a *smaller* fraction as the denominator grows. So total-cost-to-revenue falls and margin rises with scale — and rises the other way, compressing brutally, when revenue shrinks and the fixed wall still has to be paid. This is operating leverage, and it is exactly what we observe in real companies.

**A4. Why must D&A never be modeled as a percent of revenue?**

Because depreciation is a function of the *asset base and its useful life*, not this year's sales. A machine bought three years ago depreciates on a schedule set by its cost and life; that has nothing to do with whether sales rose or fell this year. Driving D&A off revenue makes it balloon absurdly in a high-growth forecast and breaks the link to the balance sheet's accumulated-depreciation account. D&A must be sourced from the PP&E schedule, subtracted on the income statement, and added back on the cash flow statement.

**A5. Why is it cleaner to drive COGS off an explicit gross-margin assumption than off a COGS-ratio?**

Because gross margin is the number management guides to and analysts debate — it is the legible, discussable metric. Setting a margin path (often a gentle glide from the last actual toward a long-run steady state) makes your assumption visible and defensible, and COGS falls out as the residual `Revenue × (1 − GM%)`. Driving off a raw COGS-ratio hides the same information behind a less-intuitive number that nobody benchmarks directly.

**A6. Why can a flat-percent model never produce a Degree of Operating Leverage other than 1.0 — and why does that make it useless for scenario analysis?**

Because if every cost is a fixed fraction of revenue, then EBIT is also a fixed fraction of revenue, so a 10% rise in revenue produces exactly a 10% rise in EBIT — DOL = 1.0 by construction. The whole point of a model is to answer "what if revenue grows 20%?" A flat model answers "profit grows exactly 20% too," mechanically and wrongly. A fixed-plus-variable model answers "profit grows 28%, because the fixed base is already covered" — the answer a decision-maker actually needs.

---

## Section B — Build / Computational Problems

**B1. High-low method — split a cost into fixed and variable.** You have two historical years of a maintenance cost. High-activity year: volume 1,200 units, cost ₹6,600. Low-activity year: volume 800 units, cost ₹5,000. Find the variable rate per unit and the fixed component, verify against the low point, then forecast the cost at 1,000 units.

- Variable rate `v = (Cost_high − Cost_low) ÷ (Vol_high − Vol_low) = (6,600 − 5,000) ÷ (1,200 − 800) = 1,600 ÷ 400 = ₹4.00 per unit.`
- Fixed `= Cost_high − v × Vol_high = 6,600 − 4 × 1,200 = 6,600 − 4,800 = ₹1,800.`
- Verify at low point: `4 × 800 + 1,800 = 3,200 + 1,800 = 5,000` ✓ reconciles to the actual.
- Forecast at 1,000 units: `4 × 1,000 + 1,800 = 4,000 + 1,800 = ₹5,800.`

In Excel with more than two points, replace the two-point slope with `=SLOPE(cost_range, volume_range)` for `v` and `=INTERCEPT(cost_range, volume_range)` for Fixed — a regression that uses every data point.

**B2. Flat-percent vs fixed-plus-variable — the divergence.** Year 0 actual: Revenue ₹1,000; COGS ₹700 (gross margin 30%). High-low analysis decomposes COGS into variable = 55% of revenue and fixed manufacturing overhead = ₹150. Revenue now grows 40% to ₹1,400. Compute COGS, Gross Profit, and Gross Margin under both methods and quantify the gap.

First verify the split against Year 0: `0.55 × 1,000 + 150 = 550 + 150 = 700` ✓.

- **Flat-percent:** COGS `= 0.70 × 1,400 = ₹980`; GP `= 1,400 − 980 = ₹420`; GM `= 420 ÷ 1,400 = 30.0%` (unchanged, by construction).
- **Fixed-plus-variable:** COGS `= 0.55 × 1,400 + 150 = 770 + 150 = ₹920`; GP `= 1,400 − 920 = ₹480`; GM `= 480 ÷ 1,400 = 34.3%`.

| Metric | Flat-percent | Fixed+variable |
|---|---|---|
| COGS | 980 | 920 |
| Gross Profit | 420 | 480 |
| Gross Margin % | 30.0% | 34.3% |

The gap is **₹60 of gross profit** — every year, growing with revenue. The flat method understates profit in a growing business because it never spreads the fixed ₹150 over the larger base. On a multi-year forecast with a valuation multiple attached, that error compounds into a materially wrong enterprise value.

**B3. Gross-margin glide path.** Revenue forecast: Yr1 ₹1,200, Yr2 ₹1,350, Yr3 ₹1,500. Instead of a flat margin, set a glide from the last actual toward a steady state: GM% = 42%, 41%, 40%. Compute COGS (as residual) and Gross Profit each year. Use the sign convention where COGS is negative.

`COGS = −Revenue × (1 − GM%)`.

| Year | Revenue | GM% | COGS | Gross Profit |
|---|---|---|---|---|
| Yr1 | 1,200 | 42% | −1,200 × 0.58 = −696.0 | 504.0 |
| Yr2 | 1,350 | 41% | −1,350 × 0.59 = −796.5 | 553.5 |
| Yr3 | 1,500 | 40% | −1,500 × 0.60 = −900.0 | 600.0 |

Check the margin row: `504.0 ÷ 1,200 = 42.0%`, `553.5 ÷ 1,350 = 41.0%`, `600.0 ÷ 1,500 = 40.0%` ✓. Driving off an explicit GM assumption makes the compression legible: gross profit still grows in rupees while the margin deliberately steps down toward the long-run steady state.

**B4. Contribution margin, break-even, and DOL — with the self-check.** A SaaS business: Revenue ₹800; variable costs (hosting, payment processing, per-customer support) = 30% of revenue; fixed costs (engineering, office, fixed marketing) = ₹400. Compute variable costs, contribution margin, CM ratio, EBIT, break-even revenue, and DOL. Then grow revenue 10% and confirm the DOL prediction.

- Variable costs `= 0.30 × 800 = ₹240`.
- **Contribution Margin `= 800 − 240 = ₹560`**; CM ratio `= 560 ÷ 800 = 70%`.
- EBIT `= CM − Fixed = 560 − 400 = ₹160`.
- **Break-even revenue `= Fixed ÷ CM ratio = 400 ÷ 0.70 = ₹571.43`** — below this, the company loses money.
- **DOL `= CM ÷ EBIT = 560 ÷ 160 = 3.50`.**

Now test the DOL prediction. Grow revenue 10% to ₹880:

- Variable `= 0.30 × 880 = ₹264`; CM `= 880 − 264 = ₹616`; EBIT `= 616 − 400 = ₹216`.
- `%ΔEBIT = (216 − 160) ÷ 160 = 35%`. Revenue rose 10%, EBIT rose 35%. Ratio `= 35 ÷ 10 = 3.50 = DOL` ✓.

The model reconciles exactly. A 70% CM ratio on a fat fixed base makes profit hypersensitive to revenue — and a 10% *drop* to ₹720 would give CM = 504, EBIT = 104, a 35% EBIT fall. High leverage cuts both ways.

**B5. Full one-year operating block, reconciled two ways.** Retailer. Revenue ₹1,500. Assumptions: gross margin 45%; variable SG&A 8% of revenue; fixed SG&A ₹120; R&D 5% of revenue; D&A ₹80 (from PP&E schedule). Build the block (negative-cost convention), then reconcile EBIT via the contribution-margin route.

| Line | Formula | Value (₹) |
|---|---|---|
| Revenue | input | 1,500.0 |
| COGS | −1,500 × (1 − 0.45) | −825.0 |
| **Gross Profit** | 1,500 − 825 | **675.0** |
| Gross margin % | 675 ÷ 1,500 | 45.0% |
| SG&A | −(0.08 × 1,500 + 120) | −240.0 |
| R&D | −0.05 × 1,500 | −75.0 |
| D&A | from schedule | −80.0 |
| **EBIT** | 675 − 240 − 75 − 80 | **280.0** |
| Operating margin % | 280 ÷ 1,500 | 18.7% |

**Reconciliation via contribution margin.** Variable costs = COGS (modeled via margin, treat all as variable) 825 + variable SG&A 120 + R&D 75 = ₹1,020. CM `= 1,500 − 1,020 = ₹480` (CM ratio 32%). Fixed = fixed SG&A 120 + D&A 80 = ₹200. EBIT `= 480 − 200 = ₹280` ✓. Both routes give ₹280 — the block is internally consistent.

**B6. Multi-year fixed cost that grows with inflation, not revenue.** Fixed SG&A is ₹100 in Yr1 and grows 5% per year for inflation/headcount. Revenue is ₹1,000 in Yr1 growing 20% per year. Build the fixed SG&A line for three years, then show what it would wrongly become if an analyst tied it to revenue at the Yr1 ratio (10%).

Correct — grows at inflation: `Fixed_1 = 100`; `Fixed_t = Fixed_{t−1} × 1.05`.

| Year | Correct fixed SG&A | Wrong (10% × revenue) |
|---|---|---|
| Yr1 | 100.00 | 0.10 × 1,000 = 100.00 |
| Yr2 | 100 × 1.05 = 105.00 | 0.10 × 1,200 = 120.00 |
| Yr3 | 105 × 1.05 = 110.25 | 0.10 × 1,440 = 144.00 |

The two lines agree in Yr1 (100 = 100) then diverge sharply: by Yr3 the revenue-tied version is ₹144 versus the correct ₹110.25 — 31% too high — because it lets "fixed" costs balloon with sales. That single error destroys operating leverage: the fixed wall that should have been spread over growing revenue instead grows with it, flattening the margin the model was built to reveal.

---

## Section C — Interview-Style Questions

**C1. "Walk me through how you'd forecast the cost side of an income statement."**

Model answer: I get the ordering right first — COGS feeds gross profit; SG&A, R&D, and D&A feed EBIT. Then I model each line by its true behavior rather than one flat ratio. COGS I drive off an explicit gross-margin path, glided from the last actual toward a defensible steady state. SG&A I split into a variable selling piece that scales with revenue and a fixed G&A piece that grows with inflation and headcount. R&D is typically a policy percent of revenue, but I check guidance because it's discretionary and lumpy. D&A I never drive off revenue — it comes from the PP&E schedule. The point is to replace one opaque ratio with several transparent, flexible assumptions I can stress independently.

**C2. "What is operating leverage, and how does your model capture it?"**

Model answer: Operating leverage is the disproportionate move in profit relative to revenue caused by a fixed cost base. Once fixed costs are covered, every incremental sales rupee drops mostly to profit, so margins expand as the business grows and compress hard when it shrinks. My model captures it by splitting fixed from variable costs, which lets me compute contribution margin — revenue minus variable costs — and then the Degree of Operating Leverage as CM over EBIT. A DOL of 3.5 means a 10% rise in revenue drives a 35% rise in EBIT: it tells the reader exactly how leveraged and how risky the cost structure is, and it falls straight out of a fixed-plus-variable build. A flat-percent model can never show it because it forces DOL to 1.0.

**C3. "Where does depreciation belong, and why shouldn't it be a percent of revenue?"**

Model answer: Depreciation on manufacturing equipment technically sits in COGS; depreciation on the head office is an operating expense. The cleanest convention is to pull D&A out as its own explicit line below gross profit and source it from the PP&E schedule — opening PP&E plus capex minus depreciation equals closing, with depreciation a function of asset cost and useful life. It is never a percent of revenue because it depends on the asset base, not this year's sales — a revenue-driven line balloons in a growth forecast and breaks the tie to accumulated depreciation on the balance sheet. Whatever convention I pick, I state it in a note cell so nobody double-counts D&A already buried in COGS ratios.

**C4. "You only have historical totals for a cost, not a fixed/variable split. How do you separate them?"**

Model answer: The high-low method for a quick cut: take the highest- and lowest-activity periods, divide the change in cost by the change in volume to get the variable rate, then plug back in to solve for the fixed intercept. With more than two data points I prefer a regression — Excel's SLOPE gives the variable rate and INTERCEPT gives the fixed component, using every observation instead of just two, which is more robust to an outlier year. Then I sanity-check the split by reconstructing a historical year: variable rate times its volume plus fixed should reproduce the actual cost. If it doesn't tie, the cost probably isn't linear in that volume driver and I rethink the driver.

**C5. "What's the difference between gross margin and contribution margin — aren't they the same thing?"**

Model answer: No, and conflating them is a common slip. Gross margin is revenue minus *COGS* — an accounting subtotal that mixes fixed and variable production costs, since COGS often contains fixed manufacturing overhead and even some depreciation. Contribution margin is revenue minus *all variable costs* wherever they sit — variable COGS, variable SG&A, variable selling — and strips out everything fixed. Gross margin answers "what's the accounting profitability of the product?"; contribution margin answers "how much does each incremental sale contribute toward covering fixed costs and profit?" CM is the one that drives break-even and DOL, because those are questions about behavior, not statement geography.

**C6. "How do you keep operating margins from drifting to impossible levels in a long forecast?"**

Model answer: Unchecked operating leverage can push a five-year forecast to a 45% operating margin for a business that's never cleared 20% — the fixed base spreads over so much revenue that the model mechanically inflates the margin. I guard against it three ways. First, I display gross and operating margin rows next to the currency lines so the trajectory is visible at a glance. Second, I cap the forecast against the company's own history and industry benchmarks — if it exceeds anything the business or its peers achieved, I need a specific reason. Third, I use step-fixed costs over long horizons: if revenue triples, the business needs new factories and staff, so I step the fixed base up at capacity thresholds rather than pretending it's fixed forever.

---

## Section D — Common-Error Spotting

**D1. D&A as a percent of revenue.** A model computes `D&A = 6% × Revenue`, and revenue grows 25% a year. By Year 5 the D&A line is enormous and the balance sheet won't tie. Diagnose and fix.

The error is driving D&A off revenue. Depreciation depends on the asset base and useful life, not sales, so a revenue link makes it balloon with growth and — fatally — decouples it from the PP&E schedule, so the income-statement D&A no longer equals the depreciation rolling through accumulated depreciation on the balance sheet, and the sheet won't close. Fix: source D&A from the PP&E schedule (opening PP&E + capex − depreciation = closing), subtract it on the income statement, add it back on the cash flow statement. For a rough first pass you may approximate D&A as a percent of prior-year PP&E or of capex — but never of revenue.

**D2. "Fixed" cost tied to revenue.** Fixed SG&A is entered as `=0.10 × Revenue` because that happened to be the Year-1 ratio. The modeller labels it "fixed." Why does this quietly destroy the model's usefulness?

Because a cost that references revenue is not fixed — it scales with sales, so the fixed wall grows with the tide instead of staying put. That erases operating leverage entirely: the margin can no longer expand as revenue grows because the "fixed" base grows in lockstep, and DOL collapses toward 1.0. The model becomes a flat-percent model wearing a fixed-cost label. Fix: fixed costs grow at an inflation/headcount rate — `Fixed_{t−1} × (1 + g)` — or stay flat, and never reference the revenue line.

**D3. The flat-percent trap.** An analyst pastes last year's ratios — COGS 62%, SG&A 18%, R&D 6% — across all five forecast years. Every margin is identical in every year. What's wrong, and what does it cost?

Every cost is being treated as purely variable, which assumes rent, executive salaries, and depreciation all scale with sales — they don't. The tell is dead-flat margins: gross and operating margin identical across all five years, which almost never happens in a real growing or shrinking business. It also forces DOL to 1.0, making every scenario answer "profit moves exactly with revenue," so the model is useless for the what-if questions it exists to answer. Fix: split each cost into fixed and variable, or at minimum let the cost-to-revenue ratios glide with scale so margins move the way a real business's margins move.

**D4. Sign-convention chaos.** In a block using the negative-cost convention, one analyst typed COGS and SG&A as positives while D&A stayed negative, then wrote `Gross Profit = Revenue + COGS`. The subtotals are wrong and nobody can trace it. Fix it.

The convention was mixed: some costs positive, some negative, so the SUM-based subtotals silently add where they should subtract. With COGS entered positive, `Revenue + COGS` *inflates* gross profit instead of reducing it. Fix: pick one convention and enforce it everywhere — the clean choice is revenue positive, all costs entered as negatives, and every subtotal a simple `SUM` (so `Gross Profit = Revenue + COGS` is correct *only* when COGS is negative). Re-enter COGS and SG&A as negatives; then the subtotals tie with no sign-flip logic to trace.

**D5. Double-counted depreciation.** A model builds COGS and SG&A from historical ratios that *already include* embedded depreciation, then adds a separate D&A line sourced from the PP&E schedule. Profit looks too low. What happened?

Depreciation is being counted twice — once buried inside the COGS and SG&A ratios, and again on the explicit D&A line — so total expense is overstated and EBIT is understated. The mirror-image error is stripping D&A out of the ratios but forgetting to add the separate line, which understates expense. Fix: pick one convention and document it in a note cell. The clean approach is to model COGS and SG&A on a *cash* basis (excluding depreciation) and show D&A as one explicit line from the schedule — then check that total D&A on the income statement equals total D&A in the PP&E schedule.

**D6. Working capital driven off the wrong line.** A model forecasts inventory and accounts payable as "days of revenue." The inventory and payables balances look inflated versus history. Why, and what's the correct driver?

Inventory and payables are driven by the cost of goods flowing through them, not by sales price — you hold and owe for goods at *cost*, not at *revenue*. Because revenue exceeds COGS by the gross margin, days-of-revenue overstates both balances by roughly the margin. Fix: base inventory days and payable days on **COGS**, not revenue — `Inventory = Inventory days ÷ 365 × COGS`. This is a second reason to get COGS right as a clean standalone number: it feeds the working-capital schedule, not just the income statement.

---

*Self-check: rebuild B5 in Excel with every cost as a live formula off labelled blue assumption cells, then reconcile EBIT both ways — down the income statement (₹280) and via contribution margin (CM ₹480 − Fixed ₹200 = ₹280). If both routes tie and your margin rows update when you flex the gross-margin cell, you've separated the beans from the rent and escaped the flat-percent trap. Now drop revenue growth to 5% and watch EBIT fall faster than revenue: that asymmetry is operating leverage, and only a fixed-plus-variable model shows it.*
