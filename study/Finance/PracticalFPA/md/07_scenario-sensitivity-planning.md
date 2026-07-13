# Scenario & sensitivity planning

## What it is & where it's used

Scenario and sensitivity planning is the discipline of asking **"what if the world is different from my base plan?"** and answering it with numbers, not adjectives. Two distinct techniques hide under this umbrella:

- **Sensitivity analysis** — change *one* driver at a time (price, volume, GST rate, USD/INR, interest rate) and watch what happens to profit, cash, or valuation. Answers: "How fragile is my number?"
- **Scenario analysis** — change *a bundle* of drivers together into a coherent story (Base / Best / Worst), because in real life a demand crash also drags price and forex with it. Answers: "What range of outcomes am I actually staring at?"

Where it shows up on the job:
- **FP&A analyst** — building the annual operating plan (AOP) with upside/downside cases the CFO presents to the board.
- **Corporate finance / M&A** — DCF valuations always carry a sensitivity table on WACC and terminal growth.
- **Credit & lending** — banks stress-test a borrower's DSCR under a downside case before sanctioning.
- **Treasury** — forex and interest-rate sensitivity on covenants and cash runway.
- **Investment / equity research** — bull/base/bear target prices.
- **Startup finance** — runway under fast-burn vs slow-burn cases for the next fundraise.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you to compute *one* NPV, *one* IRR, *one* EPS. Real business runs on **ranges and triggers**, not point estimates. The board never asks "what's the number?" — it asks "what happens if China dumps, if the rupee hits 90, if we lose our largest client?"

The specific gaps:
- College builds **static** models. Industry needs a model where you change an input cell and everything downstream recalculates cleanly — which requires you to actually *link* formulas instead of hardcoding.
- College treats assumptions as given. Industry pays you to **isolate the 3-4 drivers that matter** out of 200 line items, and to know which one, if wrong, sinks the plan.
- College stops at the answer. Industry wants the **decision**: at what volume do we break even, at what forex rate do we breach our loan covenant, how much can price fall before this deal is NPV-negative.

A person who can build a clean driver-based model with a working scenario switch and a two-variable data table is worth 2-3x a person who can only reproduce a textbook NPV.

## What "proficient" looks like

A job-ready person can, unaided:

1. **Structure a model so every assumption lives in one place** (a colour-coded input block) and flows through formulas — no hardcoded numbers buried in calculations.
2. Build a **scenario switch** (one cell drives Base/Best/Worst) using `CHOOSE` or `INDEX`, so the whole P&L flips with one dropdown.
3. Run a **one-variable and two-variable Data Table** (Excel's `What-If Analysis`) and read a **tornado chart** to rank drivers by impact.
4. State the **decision-useful output**: break-even point, margin of safety, the threshold value of a driver (e.g. "NPV goes negative below ₹92/unit"), and the probability-weighted expected value.
5. Explain **which scenario is realistic vs stress** — Best/Worst are planning bookends, not forecasts, and shouldn't be simple ±10% on everything.

## Hands-on: how to actually do it

### 1. The scenario switch (the heart of it)

Put a single control cell, say `C1`, holding 1, 2, or 3 (Base/Best/Worst). Lay assumptions in a grid, then pull the active one with `CHOOSE`:

```
                B          C(Base)    D(Best)    E(Worst)
Row5  Volume    =CHOOSE($C$1,C5,D5,E5)   1,00,000  1,20,000   75,000
Row6  Price     =CHOOSE($C$1,C6,D6,E6)   500       540        460
Row7  Var cost  =CHOOSE($C$1,C7,D7,E7)   300       290        320
```

Cell `B5` formula: `=CHOOSE($C$1, C5, D5, E5)` — flip `C1` and the entire model recalculates. `INDEX` works too: `=INDEX(C5:E5, $C$1)`.

Make `C1` a dropdown: **Data → Data Validation → List → 1,2,3**, or map to text with `=MATCH(F1,{"Base","Best","Worst"},0)`.

### 2. One-variable sensitivity (Data Table)

Layout: put your output formula (say EBITDA in `H1`) at top-right, list the driver values down a column, then select the block and **Data → What-If Analysis → Data Table → Column input cell = the price cell**.

```
        =H1(EBITDA formula)
460      2,10,00,000
480      3,00,00,000
500      3,90,00,000   ← base
520      4,80,00,000
540      5,70,00,000
```

### 3. Two-variable sensitivity (the classic valuation table)

Corner cell = output (NPV). Rows = terminal growth, columns = WACC. Select the whole grid → Data Table → **Row input = WACC cell, Column input = growth cell.**

```
NPV      10%      11%      12%      13%
2.0%   1,240    1,050      900      770
2.5%   1,380    1,160      985      840
3.0%   1,560    1,290    1,085      920
```

### 4. Threshold / break-even with Goal Seek

**Data → What-If → Goal Seek → Set NPV cell To 0 by changing Price cell.** It solves for the price where NPV = 0 — your decision trigger.

Break-even volume by formula:
```
=Fixed_Cost / (Price - Variable_Cost_per_unit)
Margin of Safety % = (Actual_Sales - BEP_Sales) / Actual_Sales
```

### 5. Python — Monte Carlo when ranges beat three cases

```python
import numpy as np
rng = np.random.default_rng(42)
n = 100_000
volume = rng.normal(100_000, 15_000, n)          # demand uncertainty
price  = rng.triangular(460, 500, 540, n)         # min, mode, max
varcost= rng.triangular(290, 300, 320, n)
fixed  = 2_00_00_000
ebitda = volume*(price-varcost) - fixed
print(f"Mean EBITDA: Rs {ebitda.mean():,.0f}")
print(f"P(loss): {(ebitda<0).mean():.1%}")
print(f"5th pctile (worst case): Rs {np.percentile(ebitda,5):,.0f}")
```

### 6. Python — one-line tornado (driver ranking)

```python
base = {"price":500,"vol":100000,"vc":300,"fixed":20000000}
def ebitda(p): return p["vol"]*(p["price"]-p["vc"])-p["fixed"]
b = ebitda(base)
for k in ["price","vol","vc"]:
    lo, hi = dict(base), dict(base)
    lo[k]*=0.9; hi[k]*=1.1
    print(f"{k:6} swing: Rs {abs(ebitda(hi)-ebitda(lo)):,.0f}")
```

Sort the swings descending and you have a tornado chart's data.

## Worked example / mini-project

**Company:** a mid-size auto-component maker, "Bharat Forgings Ltd." Build a one-year EBITDA plan with three cases and find the decision triggers.

**Base assumptions:**

| Driver | Base | Best | Worst |
|---|---|---|---|
| Volume (units) | 1,00,000 | 1,20,000 | 75,000 |
| Price (₹/unit) | 500 | 540 | 460 |
| Variable cost (₹/unit) | 300 | 290 | 320 |
| Fixed cost (₹) | 2,00,00,000 | 2,00,00,000 | 2,10,00,000 |

**Compute EBITDA per case** — `Volume × (Price − VarCost) − Fixed`:

| Case | Contribution/unit | EBITDA |
|---|---|---|
| Base | ₹200 | 1,00,000 × 200 − 2,00,00,000 = **₹0** |
| Best | ₹250 | 1,20,000 × 250 − 2,00,00,000 = **₹1,00,00,000** |
| Worst | ₹140 | 75,000 × 140 − 2,10,00,000 = **−₹99,00,000** |

The Base case sits *exactly at break-even* — a red flag that leaps out the moment you build the table. This is the value of the exercise.

**Probability-weighting** (management assigns 60% Base, 15% Best, 25% Worst):
```
Expected EBITDA = 0.60(0) + 0.15(1,00,00,000) + 0.25(-99,00,000)
                = 0 + 15,00,000 - 24,75,000 = -Rs 9,75,000
```
Expected value is *negative* even though the base looks fine — the fat downside tail dominates. Decision: renegotiate the fixed-cost base or lock in a minimum-volume contract before committing.

**Break-even trigger (Goal Seek on Base):** to reach EBITDA of ₹50 lakh, solve required price: `Price = (Fixed + Target)/Volume + VarCost = (2,00,00,000 + 50,00,000)/1,00,000 + 300 = ₹550`. So management needs a **10% price rise** or the plan under-delivers.

**Reproduce it:** put the four drivers in rows with a `CHOOSE` switch in `C1`, drop a two-variable Data Table of Price (rows) × Volume (columns) against EBITDA, and add a tornado using the Python snippet above.

## How it's tested

**Interview questions:**
- "Walk me through how you'd build a Base/Best/Worst case for this business."
- "What's the difference between sensitivity and scenario analysis?"
- "Your DCF says NPV is ₹500 cr. Which two inputs would you sensitise and why?"
- "Volume falls 20% — is that best handled by a scenario or a sensitivity?"
- "What's margin of safety and why does the board care?"

**Practical/assessment tests you will actually get:**
- **Timed Excel test (45-60 min):** given a raw P&L, build a driver-based model with a working scenario dropdown and a two-variable data table. Graders check: are inputs separated from formulas, does flipping the switch recalc everything, is there any hardcoded number inside a calculation.
- **Case study:** "Here's a factory investment. Should we build it?" — expected deliverable is NPV with a sensitivity table and a written recommendation naming the trigger variable.
- **Live model audit:** they hand you someone's model and ask "what breaks this?" — you're expected to find the assumption that swings the answer most.

## Common mistakes & how pros avoid them

| Mistake | Why it's wrong | Pro fix |
|---|---|---|
| Best/Worst = base ±10% on every line | Drivers don't move independently; this is lazy | Build coherent *stories* — a demand shock also hits price and utilisation |
| Hardcoding numbers inside formulas | Scenario switch can't reach them; model lies | Every assumption in a coloured input cell, formulas reference cells only |
| Sensitising 15 variables | Noise, no signal | Tornado-rank first, sensitise the top 3-4 |
| Symmetric up/down assumptions | Downside is usually fatter (costs spike faster than they fall) | Use asymmetric ranges; check the loss tail |
| Presenting three numbers, no decision | Board wants the "so what" | Always state the trigger/threshold and the recommended action |
| Forgetting cash & covenants | A profitable worst case can still breach DSCR and default | Stress the balance sheet and covenants, not just EBITDA |
| Circular references from interest-on-debt | Model shows `#REF`/circular warning | Enable iterative calc deliberately, or use a copy-paste interest toggle |

## Learn-it roadmap & resources

**Time to proficiency: 4-6 weeks** part-time if you already know Excel basics.

- **Week 1-2:** Master `CHOOSE`, `INDEX/MATCH`, Data Validation dropdowns, and the What-If Analysis menu (Data Table, Goal Seek, Scenario Manager). Rebuild any past P&L as a driver-based model.
- **Week 3:** One- and two-variable data tables + tornado charts. Do 5 DCF sensitivity tables.
- **Week 4:** Break-even, margin of safety, probability-weighting, expected value.
- **Week 5-6:** Monte Carlo in Python (`numpy`), and stress-testing balance-sheet covenants.

**Resources:**
- *Free:* Corporate Finance Institute (CFI) free scenario-analysis lessons; ASimpleModel.com (excellent free model-building series); Aswath Damodaran's NYU valuation lectures on YouTube (the gold standard for sensitivity in DCF).
- *Paid:* CFI's **FMVA** certification (has a dedicated scenario & sensitivity module) — most recognised for FP&A/corp-fin roles. Wall Street Prep / Breaking Into Wall Street modelling courses.
- *India-specific:* For CA students, the Cost & FM papers already cover marginal costing, break-even and margin of safety — connect that theory directly to the Excel build.

## Quick-reference

| Task | Tool / Formula |
|---|---|
| Scenario switch | `=CHOOSE($C$1, base, best, worst)` or `=INDEX(range,$C$1)` |
| Dropdown control | Data → Data Validation → List |
| 1-var sensitivity | Data → What-If → Data Table → Column input cell |
| 2-var sensitivity | Corner=output; Data Table → Row input + Column input |
| Solve for a threshold | Data → What-If → Goal Seek → Set cell To 0 by changing |
| Break-even volume | `=Fixed / (Price − VarCost/unit)` |
| Margin of safety | `=(Actual − BEP) / Actual` |
| Contribution/unit | `=Price − Variable cost/unit` |
| Expected value | `=Σ(Probabilityᵢ × Outcomeᵢ)` |
| Monte Carlo | Python `numpy.random` → percentiles + P(loss) |
| Driver ranking | Tornado chart: ±10% each driver, sort by swing |

**Golden rules:** inputs separate from formulas · never hardcode inside a calc · rank drivers before sensitising · state the trigger and the decision · stress cash & covenants, not just profit.
