# Q&A — Scenario and Sensitivity Analysis

Practice bank for Chapter 18. Work each question before reading the answer. The chapter's engine is one idea — a model output is a function of uncertain inputs, so the honest deliverable is a *range with its drivers labelled*, never a false-precision point. Every build below runs on the same compact DCF used in the chapter, `EV = FCFF₁ / (WACC − g)`, so you can reproduce each figure cell-for-cell in Excel and watch it reconcile.

---

## Section A — Concept Checks (test the WHY)

**A1. What is the single distinction between sensitivity analysis and scenario analysis?**

Number of stories, not number of knobs. **Sensitivity** moves one (or two) inputs *in isolation*, everything else frozen, to measure the *slope* — how much leverage each assumption has on the output. **Scenario** moves *every* input together to a set of values that describe *one coherent world* (Base, Bull, Bear). Sensitivity answers "how much does the output move if this input is wrong?"; scenario answers "what is the output if the world looks like X?" One reveals leverage; the other reveals plausible, survivable futures.

**A2. Why is presenting a single point estimate — "EV = ₹1,250 crore" — described as the central lie of a naive model?**

Because it dresses a guess as a fact. Every input (growth, margin, WACC) is a random variable with a spread, so the output is one draw from a distribution. A decimal-laden number *looks* rigorous but hides the confidence interval, which might be ±40%. Decision-makers are paid to manage exactly that hidden uncertainty — "what happens if I am wrong, and how wrong can I afford to be?" — and a point estimate answers none of it.

**A3. Why is bundling assumptions into scenarios more honest than moving them independently across a grid?**

Because real inputs are *correlated*. Move revenue and margin independently and the grid will happily produce a "high revenue AND high margin" corner that is economically impossible (high growth usually costs margin). A scenario respects correlation by construction: each named world sets every input to a value consistent with one causal story, so it can never present an incoherent bear case where cash flow collapses but the discount rate falls.

**A4. In a % roll-forward-style sensitivity, why must the data table's corner formula point at a cell that is genuinely downstream of the input cell?**

Because a data table has no understanding of your logic — it mechanically drops each test value into the designated input cell, recalculates, and pastes the output back. If the corner references a cell that is not actually a function of that input, every substitution produces the identical answer and the table fills as a flat, identical column. The classic "my data table isn't working" symptom is always a broken input-to-output linkage, never the tool.

**A5. Why does the model have to reference the LIVE column only, never the Bear/Base/Bull scenario columns directly?**

Because the LIVE column is the *single* value per driver that the switch controls. If any statement wires straight to the Base column, flipping to Bear leaves that line stuck on Base — your "bear case" silently contains base numbers. One live value per driver, one switch governing all of them: that discipline is the whole point.

**A6. Why is `CHOOSE($switch, Bear, Base, Bull)` preferred over a nested `IF` for scenario switching?**

Because `CHOOSE` is flat and reads left-to-right in scenario order, so it is auditable at a glance and trivially extended to a fourth scenario by adding one argument. Nested `IF(C1=1,…,IF(C1=2,…,…))` grows deeper and more error-prone with each case and buries the logic. `INDEX(range, switch)` is an equally good alternative that scales even further.

**A7. Why does a tornado chart tell you where to spend your research time?**

Because it ranks inputs by *swing* — how far the output moves when each input alone travels from its low to its high case. The longest bars on top are the assumptions that dominate the answer, so they earn the tightest justification in the memo; the short bars are inputs you can fix at base and stop debating. It converts "which of my twenty assumptions matter?" into a sorted, visual answer.

**A8. Why is a scenario range usually narrower and more defensible than the extreme corners of a two-variable data table?**

Because the grid corners combine each variable's most extreme value regardless of coherence — "everything good at once" and "everything bad at once" — which real economies rarely deliver. A scenario forbids those impossible pairings, so its downside/upside band sits inside the grid's corner-to-corner span and survives a challenge from a sceptical reviewer.

---

## Section B — Build / Computational Problems

All builds use the perpetuity DCF `EV = FCFF₁ / (WACC − g)`. Base case: `FCFF₁ = 100`, `WACC = 11%`, `g = 3%` → `EV = 100 / 0.08 = ₹1,250.0 cr`. Reproduce each in Excel; the arithmetic is shown so it self-checks.

**B1. One-variable data table (EV vs WACC).** Hold `g = 3%`. Compute EV for WACC = 9%, 10%, 11%, 12%, 13%.

`EV = 100 / (WACC − 0.03)`:

| WACC | WACC − g | EV = 100 / (WACC − g) |
|---|---:|---:|
| 9%  | 0.06 | 1,666.7 |
| 10% | 0.07 | 1,428.6 |
| 11% | 0.08 | 1,250.0 |
| 12% | 0.09 | 1,111.1 |
| 13% | 0.10 | 1,000.0 |

Verify: 100/0.06 = 1,666.67; 100/0.07 = 1,428.57; 100/0.08 = 1,250.00; 100/0.09 = 1,111.11; 100/0.10 = 1,000.00. In Excel: inputs down column A, `=EV` in the corner one row up and one column right, select the block, `Data ▸ What-If ▸ Data Table`, **Column input cell** = the WACC cell. Note the effect is *non-linear* — the 9→10% step drops EV by 238.1 but the 12→13% step only by 111.1, because the denominator is larger at high rates.

**B2. Two-variable data table (EV vs WACC and g).** Rows = WACC (9%–13%); columns = g (1%–4%). Fill the grid.

`EV = 100 / (WACC − g)`:

| WACC \ g | g=1% | g=2% | g=3% | g=4% |
|---|---:|---:|---:|---:|
| **9%**  | 1,250.0 | 1,428.6 | 1,666.7 | 2,000.0 |
| **10%** | 1,111.1 | 1,250.0 | 1,428.6 | 1,666.7 |
| **11%** | 1,000.0 | 1,111.1 | **1,250.0** | 1,428.6 |
| **12%** | 909.1 | 1,000.0 | 1,111.1 | 1,250.0 |
| **13%** | 833.3 | 909.1 | 1,000.0 | 1,111.1 |

Spot-checks: (9%,1%) = 100/0.08 = 1,250.0; (11%,3%) = 100/0.08 = 1,250.0 (base, bold); (13%,1%) = 100/0.12 = 833.3; (9%,4%) = 100/0.05 = 2,000.0. In Excel: `=EV` in the top-left corner, g across the top row, WACC down the left column, select the block, `Data Table`, **Row input cell** = the g cell, **Column input cell** = the WACC cell. The band ₹833–2,000 cr is the honest range. Notice the equal-value diagonal (9%,1%),(10%,2%),(11%,3%),(12%,4%) — all 1,250.0 — because each shares the same spread `WACC − g = 0.08`.

**B3. Scenario table via CHOOSE (Base/Bull/Bear).** Build coherent bundles and compute EV for each. Drivers:

| Driver | Bear (1) | Base (2) | Bull (3) |
|---|---:|---:|---:|
| FCFF₁ (₹ cr) | 85 | 100 | 115 |
| Growth g | 2% | 3% | 4% |
| WACC | 13% | 11% | 10% |

LIVE driver = `=CHOOSE($C$1, Bear, Base, Bull)`; `EV = FCFF₁ / (WACC − g)`:

- **Bear** (C1=1): 85 / (0.13 − 0.02) = 85 / 0.11 = **772.7**
- **Base** (C1=2): 100 / (0.11 − 0.03) = 100 / 0.08 = **1,250.0**
- **Bull** (C1=3): 115 / (0.10 − 0.04) = 115 / 0.06 = **1,916.7**

Verify: 85/0.11 = 772.73; 100/0.08 = 1,250.00; 115/0.06 = 1,916.67. Flip the single switch cell C1 through 1→2→3 and the whole model swings. The coherent span ₹773–1,917 cr sits *inside* B2's grid corners (833–2,000) precisely because the scenario refuses to pair a bull discount rate with bear cash flow.

**B4. Tornado (rank the drivers).** Vary each driver alone from its Bear to its Bull value with the other two held at Base; measure the EV swing.

| Driver (others at Base) | Low case → EV | High case → EV | Swing |
|---|---:|---:|---:|
| WACC (13%→10%) | 100/(0.13−0.03) = 1,000.0 | 100/(0.10−0.03) = 1,428.6 | **428.6** |
| FCFF₁ (85→115) | 85/0.08 = 1,062.5 | 115/0.08 = 1,437.5 | **375.0** |
| Growth g (2%→4%) | 100/(0.11−0.02) = 1,111.1 | 100/(0.11−0.04) = 1,428.6 | **317.5** |

Verify swings: |1,428.6 − 1,000.0| = 428.6; |1,437.5 − 1,062.5| = 375.0; |1,428.6 − 1,111.1| = 317.5. Sorted descending: **WACC (428.6) > FCFF₁ (375.0) > g (317.5)**. WACC is the dominant lever, so it earns the tightest justification. Build it as a stacked horizontal bar chart, longest bar on top, with a vertical line at the base EV (1,250).

**B5. Reconciliation check — do the instruments agree?** Confirm the scenario Bear/Base/Bull outputs are internally consistent with the tornado's one-at-a-time swings.

The scenario Bear (772.7) is *below* every single-driver low in the tornado (the smallest is WACC's 1,000.0), and Bull (1,916.7) exceeds every single-driver high (largest 1,437.5). That is expected: the scenario moves all three drivers adversely (or favourably) at once, so its downside must be worse than any one driver moving alone. If your scenario Bear were *inside* the single-driver lows, LIVE is not pulling all three bear values — a wiring bug. This cross-check is the fastest way to catch a half-switched model.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through how you'd set up a two-variable sensitivity table for a DCF."**

I isolate my two most important assumptions — usually WACC and terminal growth, since terminal value dominates most DCFs. I put the EV output formula in the top-left corner of a blank grid, list WACC values down the left column and g values across the top row. I select the whole block, go to `Data ▸ What-If Analysis ▸ Data Table`, and — this is the step people get wrong — I set the **Row input cell** to the model's g cell (because g runs across the top row) and the **Column input cell** to the WACC cell (down the left column). I hide the corner formula with a `;;;` custom format, apply a green-red colour scale so the gradient reads at a glance, and border the base-case cell so the reader anchors on it.

**C2. "A colleague hands you a model where the bear scenario looks suspiciously close to the base case. What's your first hypothesis?"**

That the model is wired to the scenario columns instead of the LIVE column. If a statement line references the Base column directly, flipping the switch to Bear never touches it, so the "bear" output is partly base numbers. I'd trace the output cell upstream: does EV reference LIVE, does LIVE reference `CHOOSE(switch, …)`, and does the switch actually change? A fast confirmation is the cross-check from B5 — a genuine bear must be worse than any single driver moving alone. If it isn't, the switch isn't reaching every driver.

**C3. "Why not just use Excel's Scenario Manager? It's built in."**

Because its values live inside a dialog box, not on the sheet — invisible to a reviewer, impossible to audit at a glance, and easy to forget when the model is handed off. For a delivered model I want every scenario value visible, version-controllable, and on the grid, which is exactly what a `CHOOSE`-switch gives. I use Scenario Manager to teach the concept or for a throwaway comparison, but I ship the switch.

**C4. "How many scenarios should a model have, and why?"**

Three — Base, Bull, Bear — is the sweet spot. It gives a central case plus a survivable downside and a credible upside, which is all a decision-maker can hold in their head. Five or six named worlds dilute the message and no one remembers them. I only add a fourth, like a "Stress" or "Management" case, when it drives a specific, named decision — for example a covenant-breach stress case a lender explicitly asks for.

**C5. "You've built a tornado chart and WACC has the biggest bar. So what?"**

It tells me where to concentrate. WACC is the assumption my valuation is most exposed to, so it earns the most rigorous justification in the memo — a defensible cost of capital build, a cross-check against comparable yields, and probably its own sensitivity grid. It also tells me which inputs I can stop debating: the short-bar drivers can sit at base without materially moving the answer, so arguing about them wastes everyone's time. The tornado turns "everything matters" into a priority list.

**C6. "How do you decide the low and high values for a sensitivity or tornado analysis?"**

They should be *plausible*, not arbitrary. I anchor them to something defensible — historical volatility of the input, analyst ranges, a ±1 standard deviation move, or the Bear/Bull values I already defined so the tools stay mutually consistent. A ±20% flat shock is a reasonable default when I have nothing better, but I'd never apply it if the result implies an absurd rate. The credibility of the whole exercise rests on ranges a sceptic would accept.

---

## Section D — Common-Error Spotting

For each, identify the error and give the fix.

**D1.** An analyst builds a two-variable data table, puts WACC across the top and g down the side, then sets **Row input cell** = WACC cell and **Column input cell** = g cell. The grid fills with plausible-looking numbers. What's wrong?

This specific mapping is actually *correct* (WACC across the top → Row input = WACC cell). The trap is the common inverse: WACC across the top but **Row input cell** pointed at the g cell. The rule is mechanical — *values across the top row map to the Row input cell; values down the left column map to the Column input cell.* Re-derive the mapping from where the values sit, not from the variable's name; if a grid fills with garbage, swap the two boxes.

**D2.** A data table's result column is completely flat — every WACC produces EV = 1,250.0. Diagnosis?

The corner formula points at a cell that is not downstream of the WACC input cell — most likely EV is hard-coded as `1250` or references a *copy* of WACC rather than the live WACC cell the table substitutes into. Fix: make EV a live formula `= FCFF₁/(WACC_cell − g)` and confirm the Column input cell is that same WACC_cell. The table can only vary an output that genuinely depends on the input it swaps.

**D3.** A bear scenario sets revenue growth to 2%, gross margin to 46%, and WACC to 10%. Spot the error.

The bundle is *incoherent*. A bear world with collapsing growth should carry *compressing* margins and a *higher* discount rate, not expanding margins (46% is the bull value) and a low WACC (10% is the bull value). This mixes bull and bear inputs into a fantasy that no causal story supports. Fix: set every driver to its bear-consistent value — g 2%, margin 38%, WACC 13% — so the scenario tells one story.

**D4.** A memo headline reads: "Downside EV = ₹833 crore," taken from the (13%, 1%) corner of the two-variable WACC×g grid. Why is that the wrong number to headline?

Because it is a grid *corner* — the simultaneous worst of two independent axes — not a coherent scenario. Reporting the corner treats an economically unlikely "everything bad at once, and nothing else moves" combination as the planning downside. The defensible headline downside is the *scenario* Bear (₹772.7 cr), which moves all correlated drivers together in one story. Use grid corners to explore, scenario ranges to headline. (Here the scenario Bear is actually lower still because it also cuts FCFF₁, which the grid held fixed.)

**D5.** A user types `4` into a switch cell feeding `CHOOSE($C$1, Bear, Base, Bull)` and the model returns `#VALUE!`. Root cause and fix?

`CHOOSE` only has three value arguments, so an index of 4 is out of range and errors. Root cause: the switch cell was never constrained. Fix: apply **Data Validation** (`Data ▸ Data Validation ▸ List`, values `1,2,3`) so the cell only accepts a valid scenario number, ideally as a dropdown, and shade it yellow with a border so it reads as the master control.

**D6.** Someone tries to delete a single cell inside a data-table grid to "clean it up" and Excel refuses with "cannot change part of a data table." Bug or expected?

Expected. A data table is a single array formula (`{=TABLE(...)}`); Excel forbids editing or deleting any individual cell of an array. To remove or resize it you must select the entire result block and clear it as a whole. This is a feature protecting the array's integrity, not a bug.

**D7.** A large model with four live data tables has become painfully slow to edit. What's the fix, and what's the trade-off?

Data tables recalculate on *every* workbook calculation, so several of them multiply recalc time. Switch to `Formulas ▸ Calculation Options ▸ Automatic Except for Data Tables`. The trade-off: the tables no longer refresh automatically, so you must press **F9** (or Ctrl+Alt+F9 for a full rebuild) whenever you want them current — and you must remember to do so before screenshotting for a memo, or you'll ship stale grids.

**D8.** A model reports "EV = ₹1,247.63 crore" as its headline, and separately a sensitivity band of ₹773–1,917 cr. What's the presentation error?

False precision. Quoting two decimals implies confidence to the lakh when the honest band spans over ₹1,000 crore. The precision of the deliverable should match the precision of the underlying uncertainty. Fix: round to "≈ ₹1,250 cr" and, crucially, *show the range* — "Base ₹1,250 cr; downside ₹773 cr, upside ₹1,917 cr." The range, not the decimal, is what informs the decision.

---

*Self-check: every EV in this bank derives from `EV = FCFF₁ / (WACC − g)` with base 100/(0.11−0.03) = 1,250.0. If any figure of yours disagrees, re-check whether you are holding the right variables at base and whether your LIVE column pulls all scenario values, not just one.*
