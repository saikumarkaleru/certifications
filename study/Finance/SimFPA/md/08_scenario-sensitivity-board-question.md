# Scenario & Sensitivity for a Board Question

## The ask

It's **24 July 2026**. The quarterly board meeting is in five days. The CFO forwards you the Chair's email:

> "Given the Q1 volume miss and the noise on copper prices, the board wants to understand our **downside**. Specifically: *what happens to profit if volumes fall 10% and input costs rise 5%?* Show me a **best / base / worst** view, and I want to see **which one variable moves profit the most** so we know where to focus. Keep it to **one slide** — the board doesn't read models, they read the punchline."

Your job: build a **scenario switch** (best/base/worst on one toggle), Excel **What-If Data Tables** (1-variable and 2-variable) to map the sensitivity, a **tornado chart** ranking the drivers by their swing on PBT, and distil it to one slide. Base case = the FY2026-27 budget (Revenue Rs 12.00 cr, PBT Rs 1.506 cr).

## What you're given

**Base case = budget, with the drivers exposed as switchable inputs (Rs cr unless noted):**

| Driver | Base value |
|---|---:|
| Goods volume | 90,000 units |
| Goods ASP | Rs 1,000 |
| Goods COGS / unit | Rs 750 (25% margin) |
| Services revenue | 3.00 |
| Services COGS | 1.65 (55% of rev) |
| Fixed opex (emp + other + dep) | 2.004 |
| Finance cost | 0.09 |

**Base P&L (checks to anchors):** Revenue 12.00, COGS 8.40, GP 3.60, EBIT 1.596, **PBT 1.506**.

**Scenario definitions (agreed with the CFO):**

| Lever | Worst | Base | Best |
|---|---:|---:|---:|
| Goods volume | −10% | 0% | +5% |
| Input cost (all COGS) | +5% | 0% | −2% |

## Build it — step by step

**Step 1 — The scenario switch.** One cell `$B$1 = scenario number` (1 worst / 2 base / 3 best). Each driver reads its value from a small lookup using `CHOOSE` (or `INDEX`):

```
Volume_used  = CHOOSE($B$1, 81000, 90000, 94500)
Cost_factor  = CHOOSE($B$1, 1.05, 1.00, 0.98)
' INDEX equivalent, cleaner for many drivers:
Volume_used  = INDEX(Volume_row, $B$1)
```

Flip `$B$1` and the whole P&L re-solves. This is the **live scenario toggle** the CFO clicks in the meeting.

**Step 2 — Wire the P&L to the switched drivers:**
```
Goods rev   = Volume_used × 1000 / 1e7           (Rs cr)
Goods COGS  = Volume_used × 750 × Cost_factor /1e7
Svc COGS    = 1.65 × Cost_factor
Revenue     = Goods rev + 3.00
COGS        = Goods COGS + Svc COGS
PBT         = Revenue − COGS − 2.004 − 0.09
```

**Step 3 — Compute the three scenarios.**

*Worst:* units 81,000 → goods rev `8.10`; goods COGS `81,000×750×1.05 = 6.38`; svc COGS `1.65×1.05 = 1.73`; COGS `8.11`; GP `2.99`; PBT `2.99 − 2.094 = 0.90`.
*Best:* units 94,500 → goods rev `9.45`; goods COGS `94,500×750×0.98 = 6.95`; svc COGS `1.617`; COGS `8.56`; GP `3.89`; PBT `1.79`.

**Step 4 — 1-variable Data Table (PBT vs goods volume).** Column of unit values, one formula cell `=PBT`, then *Data → What-If Analysis → Data Table*, column input cell = the volume driver:

| Goods units | 81,000 | 85,500 | 90,000 | 94,500 | 99,000 |
|---|---:|---:|---:|---:|---:|
| PBT (Rs cr) | 1.28 | 1.39 | **1.51** | 1.62 | 1.73 |

(Volume alone, input cost held at base.)

**Step 5 — 2-variable Data Table (the board's exact question).** Rows = volume change, columns = input-cost change; top-left corner cell = `=PBT`; row input = cost factor, column input = volume:

| PBT (Rs cr) — vol ↓ / cost → | +5% | 0% | −5% |
|---|---:|---:|---:|
| **−10%** | **0.90** | 1.28 | 1.67 |
| **−5%** | 0.99 | 1.39 | 1.80 |
| **0%** | 1.09 | **1.51** | 1.93 |
| **+5%** | 1.18 | 1.62 | 2.06 |

The board's scenario (volume −10%, cost +5%) is the **top-left corner: PBT Rs 0.90 cr** — a 40% fall, but still solidly profitable.

**Step 6 — Tornado (drivers ranked by PBT swing).** Flex each driver one at a time by a comparable range and record the PBT swing (high − low):

| Driver | Flex | PBT low | PBT high | **Swing** |
|---|---|---:|---:|---:|
| Goods ASP | ±5% | 1.06 | 1.96 | **0.90** |
| Input cost (COGS) | ±5% | 1.09 | 1.93 | **0.84** |
| Goods volume | ±10% | 1.28 | 1.73 | **0.45** |
| Services revenue | ±10% | 1.37 | 1.64 | **0.27** |
| Fixed opex | ±5% | 1.41 | 1.61 | **0.20** |

Sorted widest-to-narrowest, this is the tornado: **price and input cost dominate**; volume is third; opex barely moves the needle.

## The deliverable

**One slide — "Downside sensitivity of FY27 PBT"**

**Scenario summary (Rs cr):**

| | Worst | Base | Best |
|---|---:|---:|---:|
| Revenue | 11.10 | 12.00 | 12.45 |
| Gross profit | 2.99 | 3.60 | 3.89 |
| EBIT | 0.98 | 1.60 | 1.88 |
| **PBT** | **0.90** | **1.51** | **1.79** |
| vs base | −40% | — | +19% |

**The board's question, answered:** *"If volumes fall 10% and input costs rise 5% simultaneously, PBT lands at **Rs 0.90 cr — down 40%, but still firmly positive**. NTSPL does not go loss-making even in the compound-downside corner."*

**Where profit is most sensitive (tornado punchline):** *"PBT is most exposed to **selling price** (±Rs 0.90 cr) and **input cost** (±Rs 0.84 cr) — the margin levers — far more than to volume (±Rs 0.45 cr). Management focus should be a **pricing pass-through clause on AMC/goods and copper hedging**, not chasing volume. A 5% price increase alone offsets the entire modelled cost shock."*

**Analyst commentary:** "The business is margin-sensitive, not volume-sensitive — a 5% move in price or input cost swings PBT twice as hard as a 10% volume move, because volume drags COGS with it while price and input cost fall straight to the bottom line. The downside is uncomfortable but survivable; the *actionable* message is to defend margin, and the cheapest insurance is a contractual price-escalation on new orders."

## How it's reviewed

- **Base scenario ties to budget.** With `$B$1 = 2` the model must reproduce PBT Rs 1.506 cr exactly — if the switch drifts off budget, every scenario is wrong.
- **Corner check.** The 2-var table's worst corner must equal the standalone worst scenario (Rs 0.90 cr both ways).
- **Data Table input cells correct.** Row/column input cells must point at the actual driver cells, not the formula — the classic Data Table mis-wire produces a flat grid.
- **Tornado symmetry sanity.** Linear drivers give near-symmetric swings; a wildly asymmetric bar signals a formula error or a genuine non-linearity worth flagging.
- **One decision, not ten numbers.** The CFO wants the punchline (still profitable; margin is the lever) — the grid is evidence, not the message.

## Common mistakes & red flags

- **Hard-coding scenario outputs** instead of a live switch. When the board asks "what if volume falls 8%, not 10%?" a hard-coded deck can't answer; a `CHOOSE`/`INDEX`-driven model re-solves in one keystroke.
- **Data Table input cell pointing at the wrong reference** → the whole table returns the base value in every cell. Always test one corner by hand.
- **Flexing everything at once and calling it sensitivity.** Sensitivity = one variable at a time (that's the tornado); scenarios = a *coherent* combination. Don't confuse them.
- **Volatile Data Tables slowing the file.** Large 2-var tables recalc on every edit — set *Calculation → Automatic except for Data Tables* on big models.
- **Ranking the tornado by raw driver size, not PBT impact.** A big revenue line with thin margin may swing PBT less than a small high-margin one. Rank by the *output* swing.
- **Presenting worst case with no probability or action.** "PBT could be Rs 0.90 cr" is scary and useless alone; "…and here's the pricing/hedging lever that protects it" is decision-grade.

## On the job & in the interview

Scenario and sensitivity work is where FP&A earns its seat: turning "what if?" into a decision. Boards think in ranges and downside, not point estimates — the analyst who can toggle a live model in the room is worth ten static decks.

**Q: "Difference between a scenario and a sensitivity?"**
"A sensitivity flexes *one* variable and holds the rest — it isolates which lever matters most (that's the tornado). A scenario moves a *consistent set* of variables together to tell a coherent story — 'demand recession' might combine lower volume, lower price, and higher cost at once. Sensitivity finds the levers; scenarios tell the story. I use both: tornado to prioritise, best/base/worst to communicate."

**Q: "How do you build a scenario switch in Excel?"**
"A single selector cell drives every input via `CHOOSE(selector, worst, base, best)` or `INDEX(range, selector)`. Each driver has its three values in a table and reads the chosen column. Flip the one cell and the whole model re-solves — no copy-paste, fully auditable, and I can demo live in the board meeting. For decision variables I'll layer a two-variable Data Table on top for the grid."

**Q: "The board asks 'what's our biggest risk to profit?' — how do you answer with data?"**
"I'd point to the tornado: PBT swings most on selling price (±Rs 0.90 cr) and input cost (±Rs 0.84 cr), roughly double the volume sensitivity, because those hit margin directly. So the biggest risk isn't losing units — it's margin compression from copper prices without a pricing pass-through. That reframes the discussion from 'sell more' to 'protect the spread,' and I'd recommend a price-escalation clause and a hedging policy as the mitigations."
