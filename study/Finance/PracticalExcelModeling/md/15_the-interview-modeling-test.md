# The interview Excel & modeling test

## What it is & where it's used

The interview Excel/modeling test is a **timed, hands-on assessment** where you build or fix something live — no ChatGPT, no calling a friend, often no internet. It is the single most common filter between "sounds good on the CV" and an offer for roles in **investment banking, private equity, equity research, corporate FP&A, transaction advisory / valuations, credit analysis, and startup finance (fundraise/CFO-track)**.

Formats you will meet in India and globally:

| Format | Duration | Where |
|---|---|---|
| Live shared-screen build (Zoom + Excel) | 30–90 min | Most banks, PE, boutique advisory |
| Take-home model (emailed, deadline) | 3–24 hrs | Startups, mid-market PE, research |
| "Fix my broken model" / audit | 20–45 min | FP&A, controllership |
| Aptitude + Excel combo (SHL/Kenexa style) | 45–60 min | BPO/KPO, Big 4 analytics, GCC roles |

For an India-based candidate targeting Big 4 (Deloitte/PwC/EY/KPMG), GCCs (Wells Fargo, JPMC, Goldman Bengaluru/Hyderabad), or a domestic AMC/broker, expect the "fix + build" variant far more than a full LBO.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you what NPV *means*. It did not make you build a 3-statement model that **balances**, under time pressure, with a keyboard-only workflow, correct sign conventions, and a circularity toggle for interest-on-average-debt. CA Inter drilled accounting rules but on paper, not linked in Excel where the P&L flows to retained earnings which flows to the balance sheet.

The gap employers pay to close:

- **Speed under the keyboard** — pros navigate with `Alt` shortcuts, not the mouse. A mouse-user is spotted in 30 seconds.
- **Structure** — inputs (blue), formulas (black), links (green), clearly separated. College spreadsheets are one giant messy tab.
- **A model that ties** — Assets = Liabilities + Equity to the rupee, cash flow reconciles to the balance sheet cash line.
- **Judgment** — sensible assumptions with a stated rationale, not a random 10% growth.

## What "proficient" looks like

An interviewer's mental checklist for a "job-ready" candidate:

1. Builds a clean **3-statement model** from a blank sheet in ~45 min, statements linked, BS balancing.
2. **Keyboard-first**: no mouse for navigation, formatting, or fill.
3. Uses **relative/absolute references** correctly (`$` discipline) and **named ranges** or structured refs where sensible.
4. Handles **circularity** (interest ↔ cash ↔ debt) knowingly — iterative calc on, or a circ-breaker switch.
5. Writes **auditable** formulas: no hardcodes inside formulas, no `=B2+B3+B4` where `SUM` belongs, colour-coded inputs.
6. Can **stress a driver** (revenue −20%) and immediately explain the covenant/cash impact.
7. Talks while building — narrates assumptions.

## Hands-on: how to actually do it

### Keyboard shortcuts that signal "pro" (Windows)

```
Ctrl + ~            Toggle show-all-formulas (audit view)
Alt + =             AutoSum
F2                  Edit cell / F4 = toggle $ absolute
Ctrl + Shift + →/↓  Select to edge of data
Alt + E, S, V       Paste Special > Values (older) / Ctrl+Alt+V
Alt + H, O, I       Autofit column width
Ctrl + [            Jump to precedent cell (trace)
F9                  Recalculate (and evaluate part of a formula)
Alt + A, T          Add filter
```

### The lookup you MUST use

```excel
=XLOOKUP(lookup_value, lookup_array, return_array, "Not found", 0)
```
Legacy fallback interviewers still test:
```excel
=INDEX($D$2:$D$500, MATCH(A2, $B$2:$B$500, 0))
```
`VLOOKUP` is acceptable but flag that it breaks on column insertion — `INDEX/MATCH` or `XLOOKUP` shows maturity.

### Core modeling formulas

```excel
Revenue growth:        =Prev_Rev * (1 + growth_%)
Depreciation (SLM):    =(Cost - Salvage) / Useful_life
Ending debt:           =Opening_debt + Drawdown - Repayment
Interest (on avg):     =Rate * AVERAGE(Opening_debt, Closing_debt)
Retained earnings:     =Opening_RE + PAT - Dividends
Cash (from CFS):       =Opening_cash + CFO + CFI + CFF
Balance check:         =Total_Assets - (Total_Liab + Total_Equity)   'must = 0
```

### Circularity switch (interest on average debt creates a loop)

Put a toggle in one cell `Circ_Switch` (1/0):
```excel
=IF($Circ_Switch=1, Rate*AVERAGE(Open_debt,Close_debt), Rate*Open_debt)
```
And enable **File > Options > Formulas > Enable iterative calculation** (100 iterations, 0.001). Narrate this — it is a classic "do they even know?" test.

### Error-proofing

```excel
=IFERROR(Sales/Units, 0)
=SUMIFS(Amount, Region, "West", Month, ">="&DATE(2026,4,1))
```

## Worked example / mini-project

**Prompt (45 min):** "Build a 3-year projection for a mid-market manufacturer. FY26 revenue ₹500 cr, growing 12% then 10%. EBITDA margin 18%. Term loan ₹200 cr at 10%, ₹40 cr repaid annually. Tax 25%. Show that the balance sheet balances."

Build a driver block, then link:

| Line (₹ cr) | FY26 | FY27 | FY28 | Formula (FY27) |
|---|---|---|---|---|
| Revenue | 500 | 560 | 616 | `=E_rev*(1+0.12)` |
| EBITDA (18%) | 90.0 | 100.8 | 110.9 | `=Rev*0.18` |
| Depreciation | 20 | 20 | 20 | input |
| EBIT | 70.0 | 80.8 | 90.9 | `=EBITDA-Dep` |
| Interest (10% avg) | 18.0 | 16.0 | 12.0 | `=0.10*AVERAGE(OpenDebt,CloseDebt)` |
| PBT | 52.0 | 64.8 | 78.9 | `=EBIT-Int` |
| Tax @25% | 13.0 | 16.2 | 19.7 | `=PBT*0.25` |
| **PAT** | 39.0 | 48.6 | 59.2 | `=PBT-Tax` |
| Closing debt | 160 | 120 | 80 | `=OpenDebt-40` |

Then the tie-out that wins the round:

```excel
Cash_close = Cash_open + PAT + Dep - Debt_repay - Capex + Δ Working_capital
Balance_check = Total_Assets - Total_Liab_Equity   → 0.00
```

If `Balance_check` isn't zero, **stop and trace with `Ctrl+[`** before adding anything else. A model that doesn't balance but looks pretty scores lower than a simpler one that ties.

## How it's tested

**The practical test itself** — a typical live shared-screen script:
1. "Here's a blank sheet. Build me a revenue build with these drivers." (structure + speed)
2. "Now link it to a simple P&L." (references, sign convention)
3. "Add debt with interest on average balance — make it work." (circularity)
4. "The balance sheet is off by ₹4 cr, find it." (audit under pressure)
5. "Flex revenue down 20% — what breaks?" (judgment)

**The take-home** — you get an .xlsx of a real-ish company; deliver a model + a 5-line email summarising the investment view. They grade formatting and the *email* as much as the math.

**Verbal questions fired mid-build:**
- "Walk me through a 3-statement model — if depreciation goes up ₹100, what happens to all three statements?" (Answer: P&L PAT −75 at 25% tax; CFS add back +100 so cash +25; BS: cash +25, PP&E −100, RE −75 → still balances.)
- "How do you break circularity?" / "Difference between deferred tax asset and provision?"
- "Why is my cash flow not matching the balance sheet?"

**GCC/Big-4 aptitude combo:** SHL-style timed Excel — pivot a 5,000-row table, `SUMIFS` a summary, spot the duplicate. Practise pivots and `SUMIFS` cold.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Reaching for the mouse | Keyboard-only; learn 15 shortcuts to reflex |
| Hardcoding numbers inside formulas (`=B2*1.12`) | Growth rate lives in its own labelled input cell |
| No colour coding | Blue = input, black = calc, green = cross-sheet link |
| Building fancy tabs before it balances | Get BS to tie *first*, decorate later |
| Silent on assumptions | Narrate: "I'll assume WC stays 15% of sales because…" |
| Panicking when balance check ≠ 0 | Trace precedents `Ctrl+[`; check sign on one line at a time |
| Circular ref error ignored | Toggle iterative calc, explain the loop out loud |
| Over-engineering under time pressure | Deliver a working simple model over a broken complex one |

**Red flags interviewers actively watch for:** mouse-dragging to select, retyping the same number in multiple cells, `=A1+A2+A3+A4` instead of `SUM`, a model that doesn't balance and the candidate not noticing, freezing silently when stuck, and formatting a chart before the numbers work.

## Learn-it roadmap & resources

**Realistic time to test-ready:** 4–6 weeks of ~1 hr/day if you already know accounting (you do, from CA Inter).

| Week | Focus |
|---|---|
| 1 | Keyboard shortcuts + `XLOOKUP`/`INDEX-MATCH`/`SUMIFS`, drilled daily |
| 2 | Single-statement builds; `$` discipline; colour convention |
| 3 | Full 3-statement link; get the BS to balance from scratch 5× |
| 4 | Circularity, debt schedule, sensitivity tables (`Data > What-If`) |
| 5–6 | Timed mocks: 45-min builds, then "find the error" drills |

**Resources:**
- **Breaking Into Wall Street (BIWS)** / **Wall Street Prep** / **CFI** — paid, the industry standard 3-statement + LBO courses.
- **Macabacus** and **Corporate Finance Institute** free formula/shortcut guides.
- Free: rebuild a listed company's model from its annual report (screener.in gives Indian financials free).
- Certification: **CFI FMVA** (globally recognised, ~₹25–40k) or **NISM** for domestic markets roles; BIWS for banking.

Practice the *timed* condition — set a 45-minute timer and build from blank. Untimed practice does not prepare you for the thing being tested: performance under the clock.

## Quick-reference

```
BUILD ORDER:  Assumptions → Revenue → P&L → Debt schedule → CFS → BS → Balance check
BALANCE:      Total Assets  =  Total Liabilities + Equity   (to the rupee)
CASH TIE:     Cash_close = Cash_open + CFO + CFI + CFF
DEP TEST:     +100 Dep → PAT −75, Cash +25, PP&E −100, RE −75  (BS still ties)
```

| Need | Formula |
|---|---|
| Lookup | `=XLOOKUP(val, arr, ret, "NA", 0)` |
| Robust lookup | `=INDEX(ret,MATCH(val,key,0))` |
| Conditional sum | `=SUMIFS(amt, crit_rng, crit)` |
| Safe divide | `=IFERROR(a/b,0)` |
| Interest (avg) | `=rate*AVERAGE(open,close)` |
| Retained earnings | `=open_RE + PAT − div` |
| Balance check | `=Assets − (Liab + Equity)` → 0 |

| Colour convention | Meaning |
|---|---|
| Blue font | Hardcoded input / assumption |
| Black font | Formula within the sheet |
| Green font | Link from another sheet |
| Red font | Warning / external link / check |

**Top shortcuts:** `F2` edit · `F4` toggle `$` · `Alt+=` sum · `Ctrl+[` trace precedent · `Ctrl+~` show formulas · `Ctrl+Shift+arrow` select range · `Ctrl+Alt+V` paste special.
