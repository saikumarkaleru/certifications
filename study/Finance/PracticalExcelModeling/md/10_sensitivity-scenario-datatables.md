# Sensitivity, Scenario & Data Tables

## What it is & where it's used

Sensitivity and scenario analysis answer the question every decision-maker actually asks: *"What if I'm wrong?"* Your model spits out one number — an NPV of ₹4.2 crore, an EPS of ₹18.50, a breakeven of 62,000 units. But that number rests on assumptions (growth, margin, discount rate) that are just educated guesses. Sensitivity analysis measures how much the output moves when an input moves. Scenario analysis bundles several inputs into named cases (Base / Best / Worst). Together they turn a fragile point-estimate into a defensible range.

Where it shows up on the job:

| Role | Use |
|---|---|
| FP&A / Corporate finance | Budget scenarios, revenue sensitivity, board decks |
| Investment banking / PE | DCF valuation sensitivity, LBO returns grids |
| Equity research | Target-price football fields, EPS scenarios |
| Credit / Lending | Stress-testing DSCR and interest-coverage covenants |
| Project finance / Capex | IRR sensitivity to capacity, tariff, delay |
| Treasury | FX and rate impact on cash flow |

The four core Excel tools: **Data Tables** (one/two-variable grids), **Scenario Manager** (named input sets), **Goal Seek** (reverse-solve one input for a target), and **Tornado charts** (rank which drivers matter most).

## The gap: why companies want this (and college didn't teach it)

An MBA finance course teaches you to *calculate* NPV and IRR. It stops there. It hands you clean inputs and asks for one answer. Industry does the opposite: nobody trusts a single answer, and half your inputs are contested in the meeting.

The specific gaps employers see in freshers:

- You built a beautiful DCF, but when the CFO says *"show me NPV if EBITDA margin drops 200 bps and WACC is 13%"* you rebuild the whole thing manually instead of reading it off a two-variable data table in three seconds.
- You hard-coded assumptions inside formulas, so nothing is switchable and no sensitivity is possible.
- You confuse a **scenario** (many inputs change together, e.g. a recession) with a **sensitivity** (one input flexes, all else held). They answer different questions.
- You don't know which of your 30 assumptions actually moves the answer — so you spend hours refining an input the output barely cares about.

Companies pay for the person who can say: *"NPV is positive across every scenario except a demand shock below 45,000 units; the two drivers that matter are price realisation and WACC — everything else is noise."* That sentence is the job.

## What "proficient" looks like

A job-ready person can, unaided:

1. **Structure a model for sensitivity** — every assumption in a labelled input cell, output linked by formula, nothing hard-coded.
2. Build a **one-variable and two-variable data table** correctly (including the notorious "top-left cell must reference the output" rule).
3. Set up **Scenario Manager** with 3+ named scenarios and produce a **Scenario Summary** report.
4. Use **Goal Seek** to reverse-solve (e.g. "what price gives ₹0 NPV?") and know its limits (one changing cell, one target).
5. Build a **tornado chart** to rank drivers by impact.
6. Read a sensitivity grid and **state a decision**, not just present numbers.
7. Know that data tables are **volatile** (recalc-heavy) and how to switch to *Automatic Except Data Tables* on big models.

## Hands-on: how to actually do it

### Setup: a switchable model

Never write `=B5*1.1`. Put the 1.1 (growth) in its own cell and reference it. Assume this layout:

```
        A                         B
1   Units sold               50,000
2   Price per unit (₹)          800
3   Variable cost/unit (₹)      480
4   Fixed cost (₹)       1,20,00,000
5   Tax rate                    25%
6
7   Revenue                  =B1*B2
8   Contribution        =(B2-B3)*B1
9   PBT                    =B8-B4
10  PAT                =B9*(1-B5)
```

`B10` (PAT) is our output. Say it computes ₹78,00,000.

### One-variable data table

Question: how does PAT change as **Units sold** varies from 30,000 to 70,000?

1. In a column, list the input values (say `D2:D6` = 30000, 40000, 50000, 60000, 70000).
2. In the cell **one row up and one column right** of the first value (`E1`), reference the output: `=B10`.
3. Select the rectangle `D1:E6`.
4. **Data ▸ What-If Analysis ▸ Data Table**.
5. Because inputs run down a column, put the input cell in the **Column input cell** box: `$B$1`. Leave Row input blank. OK.

Excel fills `E2:E6` with PAT at each unit level. It substitutes each value into `B1` and reads `B10`.

### Two-variable data table

Question: PAT across combinations of **Units (rows)** and **Price (columns)**.

```
        D            E        F        G        H
1     =B10         750      800      850      900     <- prices across the top
2    30,000
3    40,000
4    50,000
5    60,000
6    70,000
```

- **Top-left corner cell (`D1`) MUST reference the output**: `=B10`. This is the #1 error.
- Units go down column D; prices go across row 1.
- Select `D1:H6` ▸ **What-If Analysis ▸ Data Table**.
- **Row input cell** = `$B$2` (price is along the row). **Column input cell** = `$B$1` (units down the column). OK.

You now have a 5×4 grid of PAT for every unit/price combo.

### Goal Seek — reverse-solve

Question: what **price** makes PAT exactly ₹1,00,00,000?

**Data ▸ What-If Analysis ▸ Goal Seek**
- Set cell: `$B$10`
- To value: `10000000`
- By changing cell: `$B$2`

Excel iterates and drops the required price into `B2`. Classic uses: breakeven price, required volume for a target profit, the interest rate that zeroes an NPV (a manual IRR).

### Scenario Manager — named cases

**Data ▸ What-If Analysis ▸ Scenario Manager ▸ Add**. Changing cells: `$B$1,$B$2,$B$3`.

| Scenario | Units (B1) | Price (B2) | VC/unit (B3) |
|---|---|---|---|
| Base | 50,000 | 800 | 480 |
| Best | 65,000 | 850 | 460 |
| Worst | 38,000 | 740 | 510 |

Add each set of values. Then **Summary ▸ Scenario summary**, result cell `$B$10`. Excel builds a clean comparison sheet of PAT across all three — perfect for a board slide.

### The formula alternative (more robust than data tables)

For a clean sensitivity grid without volatile data tables, use a corner-output cell plus direct recompute, or in modern Excel spill it:

```
=LET(u, SEQUENCE(1,,30000,10000),
     p, SEQUENCE(5,,750,50),
     ((800 - 480) ... )   // build the PAT expression across u and p
)
```

In practice most desks still use data tables — but know that `INDEX`/`CHOOSE` scenario switches are more auditable:

```
Active scenario in B12 (1/2/3):
Units  =CHOOSE($B$12, 50000, 65000, 38000)
Price  =CHOOSE($B$12, 800, 850, 740)
```

Flip `B12` and the whole model swings. This is how professional models toggle scenarios.

### Python cross-check (for larger analyses)

```python
import numpy as np, pandas as pd
units = np.arange(30000, 70001, 10000)
prices = np.arange(750, 901, 50)
def pat(u, p, vc=480, fc=1.2e7, tax=0.25):
    return ((p - vc) * u - fc) * (1 - tax)
grid = pd.DataFrame({p: pat(units, p) for p in prices}, index=units)
print(grid.round(0))
```

## Worked example / mini-project

**Capex decision: should a firm buy a ₹2 crore packaging machine?**

Assumptions (all in input cells):

| Input | Cell | Base |
|---|---|---|
| Initial outlay (₹) | B1 | 2,00,00,000 |
| Annual units | B2 | 5,00,000 |
| Contribution/unit (₹) | B3 | 40 |
| Annual fixed cost (₹) | B4 | 60,00,000 |
| Life (years) | B5 | 5 |
| WACC | B6 | 12% |
| Tax rate | B7 | 25% |

Annual after-tax cash flow (ignoring depreciation tax shield for simplicity):

```
Annual CF  =((B2*B3)-B4)*(1-B7)     -> ((5,00,000*40)-60,00,000)*0.75 = ₹1,05,00,000
NPV        =-B1 + NPV(B6, <5 equal annual CFs>)
```

`NPV(12%, five years of ₹1.05 cr) − ₹2 cr = ₹3.78 cr − 2.00 cr = ₹1.78 cr`. Positive — accept, at base case.

**Now stress it. Two-variable data table: WACC (rows) × Units (columns), output = NPV.**

| NPV (₹ cr) | 3,50,000 | 4,25,000 | 5,00,000 | 5,75,000 |
|---|---|---|---|---|
| **10%** | 0.24 | 1.30 | 2.36 | 3.42 |
| **12%** | 0.05 | 1.06 | 2.08 | 3.10 |
| **14%** | -0.12 | 0.85 | 1.82 | 2.79 |
| **16%** | -0.28 | 0.65 | 1.58 | 2.51 |

**Decision read-off:** NPV stays positive across almost the entire grid. It only turns negative if volume falls to ~3,50,000 units *and* WACC hits 14%+ simultaneously — a genuine double-shock. The project is robust; the binding risk is a demand collapse, not the cost of capital.

**Goal Seek the breakeven:** Set NPV = 0 by changing Units → ~3,35,000 units. So the firm has a ~33% volume cushion below base. That single sentence is what goes to the investment committee.

**Tornado (one-at-a-time ±10%):** flex each input ±10%, record NPV swing, sort descending:

| Driver | NPV low | NPV high | Swing (₹ cr) |
|---|---|---|---|
| Contribution/unit | 1.19 | 2.36 | 1.17 |
| Units | 1.24 | 2.31 | 1.07 |
| Fixed cost | 1.66 | 1.89 | 0.23 |
| WACC | 1.70 | 1.86 | 0.16 |

Plot as a horizontal bar chart sorted widest-at-top → a tornado. Contribution and volume dominate; fixed cost and WACC barely register. Focus diligence there.

## How it's tested

**Interview questions**
- "Difference between sensitivity and scenario analysis?" (one input vs many inputs moving together.)
- "In a two-variable data table, what goes in the top-left cell?" (a reference to the output.)
- "How would you find the price at which NPV = 0?" (Goal Seek / a data table.)
- "Your NPV is very sensitive to WACC — what does that tell you?" (long-duration cash flows; valuation risk; justify the discount rate carefully.)
- "Why is Data Table sometimes disabled or slow?" (it's a volatile array; on big models set Formulas ▸ Calculation ▸ *Automatic Except Data Tables*.)

**Practical / assessment tests**
- **Timed Excel test (30–45 min):** given a P&L or DCF, "build a two-variable data table of NPV vs growth and margin, add a Base/Best/Worst scenario summary, and state your recommendation." They watch whether you hard-code, whether the top-left cell is right, and whether you actually conclude.
- **Case study:** "Here's a project; tell us how sensitive the return is and what would kill it." They want the tornado insight, not a data dump.
- **Live screen-share:** they change an assumption and check your model updates end-to-end (proving nothing is hard-coded).

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Hard-coding assumptions in formulas | Every assumption in its own labelled input cell |
| Top-left cell of a 2-var table has a number, not `=output` | Always point it at the output cell |
| Swapping Row and Column input cells | Row input = the variable running *across*; Column input = the one running *down* |
| Data table input cells on a different sheet | Excel forbids it — inputs must be on the same sheet as the table |
| Confusing scenario with sensitivity | Scenario = many inputs change together; sensitivity = one at a time |
| Model crawls after adding tables | Set *Automatic Except Data Tables*; press F9 to recalc deliberately |
| Presenting the grid with no conclusion | End with one sentence: what's the decision and what's the binding risk |
| Tornado with inconsistent ±ranges | Flex every driver by the *same* % (or same std-dev) so bars are comparable |
| Goal Seek won't converge | Give a sensible start value; it needs a monotonic, solvable relationship |

## Learn-it roadmap & resources

**Time to proficiency:** 1–2 weeks of focused practice if you already know NPV/IRR. A weekend gets you functional; real fluency comes from building 5–6 of your own models.

| Week | Focus |
|---|---|
| Days 1–2 | Switchable model structure; one-variable data table |
| Days 3–4 | Two-variable tables; Goal Seek |
| Day 5 | Scenario Manager + Summary report |
| Days 6–7 | Tornado chart; write decision memos from grids |

**Resources**
- *Free:* Corporate Finance Institute (CFI) free Excel articles; Microsoft's "What-If Analysis" docs; ExcelJet (searchable formula reference); Aswath Damodaran's spreadsheets (nyu.edu/~adamodar) — real DCFs with live sensitivity.
- *Paid / certification:* CFI's **FMVA** (Financial Modeling & Valuation Analyst) — heavy on scenarios and sensitivity; Wall Street Prep / BIWS modeling courses. Any of these signals to Indian recruiters (Big 4, IB, corporate FP&A) that you can model, not just calculate.
- *Practice:* rebuild a listed company's DCF from its annual report and add a WACC × growth grid — the single best portfolio piece for a finance interview.

## Quick-reference

| Tool | Path | Answers |
|---|---|---|
| One-variable data table | Data ▸ What-If ▸ Data Table (fill Column *or* Row input) | Output vs one input |
| Two-variable data table | Same; fill **both** Row & Column input; top-left = `=output` | Output vs two inputs |
| Goal Seek | Data ▸ What-If ▸ Goal Seek | Reverse-solve one input for a target |
| Scenario Manager | Data ▸ What-If ▸ Scenario Manager | Named Base/Best/Worst cases |
| Scenario switch (formula) | `=CHOOSE($B$12, base, best, worst)` | Auditable toggle |
| Tornado chart | ±X% each driver → sorted bar chart | Which drivers matter most |

**Golden rules**
- Top-left cell of a two-variable table = `=` output cell.
- Row input = variable across the top; Column input = variable down the side.
- Data table inputs must be on the **same sheet**.
- Data tables are volatile → *Automatic Except Data Tables* on large models.
- Never hard-code an assumption. Always end with a decision, not a grid.
