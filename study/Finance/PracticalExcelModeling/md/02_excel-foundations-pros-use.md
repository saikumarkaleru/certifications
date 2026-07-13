# Excel Foundations Pros Use

## What it is & where it's used

Excel is the default operating system of finance. Not because it's the best tool for every job, but because it is the one tool every analyst, controller, banker, auditor, and CFO can open on any machine and immediately read. In an Indian finance job you will live inside Excel for MIS reports, budget vs actuals, receivable ageing, GST reconciliations (GSTR-2B vs purchase register), invoice trackers, DCF and valuation models, and the monthly deck that goes to management.

"Foundations pros use" means the boring, invisible layer that separates a fast analyst from a slow one: working without touching the mouse, structuring a workbook so it can be audited, formatting numbers so a ₹ figure reads correctly at a glance, and knowing exactly when a reference should lock. Roles that test this on day one: **FP&A / MIS analyst, audit associate (Big 4 and mid-tier), investment banking / equity research associate, accounts executive, treasury, and tax analyst.** Every one of them assumes you already have this. Nobody trains you on it.

## The gap: why companies want this (and college didn't teach it)

An MBA Finance course teaches you what WACC *means*. It does not teach you that the WACC cell should be a single blue input feeding twenty grey formula cells, or that hard-coding 0.12 inside a formula is a firing-level habit in a model that gets reviewed. College evaluates *answers*; employers evaluate *the workbook that produced the answer* — because someone else has to audit, update, and trust it next quarter.

The specific gaps:

- You were graded on getting a number; industry grades you on a model a stranger can follow.
- You used the mouse; a pro closes books using the keyboard because at 200 rows the mouse is the bottleneck.
- You typed numbers into formulas; industry demands separation of **inputs, calculations, and outputs**.
- You never had to explain *why* a cell shows what it shows — pros use auditing tools (F2, F9, Ctrl+[) to defend every figure.

Closing this gap is the cheapest, highest-return week of study before any finance interview.

## What "proficient" looks like

The concrete bar. A job-ready person can, **unaided and mostly without a mouse**:

- Navigate and edit a 5,000-row sheet using only the keyboard (Ctrl+Arrows, Ctrl+Shift+Arrows, Ctrl+PgUp/PgDn).
- Build a workbook with a clear structure: an **Inputs** tab (blue font), **Calc** tabs (black), and an **Output/MIS** tab (formatted for print).
- Format Indian financials: lakhs/crores scaling, `(1,234)` for negatives in red, `-` for zero, ₹ symbol only where needed.
- Explain absolute vs relative refs and fix a broken drag by adding `$` in the right place — using F4, not retyping.
- Create and use named ranges so `=Price*Qty` reads instead of `=B4*C4`.
- Audit any formula: trace precedents (Ctrl+[), evaluate a sub-part with F9, and step through with Evaluate Formula.

If you can do those six without hesitating, you clear the practical filter for most entry finance roles.

## Hands-on: how to actually do it

### Keyboard-first workflow

Train your hands off the mouse. The core set:

| Shortcut | Does |
|---|---|
| `Ctrl + Arrow` | Jump to edge of data block |
| `Ctrl + Shift + Arrow` | Select to edge of data block |
| `Ctrl + Space` / `Shift + Space` | Select column / row |
| `Alt + =` | AutoSum |
| `Ctrl + ;` | Insert today's date (static) |
| `F2` | Edit cell (see the formula) |
| `F4` | Toggle `$` locks / repeat last action |
| `Ctrl + [` | Select precedent cells |
| `Ctrl + \` | Select cells whose value differs across a row |
| `Alt + E, S, V` | Paste Special → Values |
| `Ctrl + T` | Convert range to Table |
| `Ctrl + PgUp / PgDn` | Move between sheets |

The **ribbon accelerator** `Alt` is the master key: press `Alt` and Excel prints letters over every command. `Alt, H, 0` deletes a decimal. `Alt, A, S, S` opens Sort. Learn the path once and you never reach for the mouse.

### Number formatting for finance (India)

Use **Custom Format** (`Ctrl + 1` → Number → Custom). The four sections are `positive;negative;zero;text`.

```
Standard accounting (red negatives, dash for zero):
#,##0.00;[Red](#,##0.00);"-"

Whole rupees with symbol:
[$₹-en-IN] #,##0;[Red]([$₹-en-IN] #,##0)

Indian lakh/crore digit grouping (12,34,56,789):
[>=10000000]##\,##\,##\,##0;[>=100000]##\,##\,##0;##,##0

Show figures in ₹ lakhs (scale by /100000 using a trailing comma trick won't work in INR;
instead divide in a formula, then format):
#,##0.00" L"
```

Rule pros follow: **never divide by 100000 inside the number format for lakhs** — do the division in a helper cell or state "₹ in lakhs" in the header and divide the source. Keep formatting and math separate.

### Absolute / relative references

- `A1` – relative: both move when copied.
- `$A$1` – absolute: locked.
- `A$1` – row locked (mixed).
- `$A1` – column locked (mixed).

Press `F4` while the cursor is on a reference to cycle `A1 → $A$1 → A$1 → $A1`. The classic use: a tax-rate cell you multiply every row against.

```
=E4*$B$1        // B1 holds the GST rate; lock it so every row hits the same cell
```

### Named ranges

Select the cell, type a name in the **Name Box** (top-left) or `Ctrl + F3` (Name Manager). Now formulas read like English:

```
=Taxable_Value*GST_Rate
=SUMIFS(Amount, State, "Karnataka")
```

Scope named ranges to the workbook, avoid spaces (use underscores), and never name a range something that looks like a cell (`Q1` is illegal).

### Auditing tools

- **Trace Precedents:** `Alt, M, P` (or Formulas ribbon) draws arrows to the cells feeding this one. `Ctrl + [` jumps to them.
- **Trace Dependents:** `Alt, M, D`.
- **F9 inside a formula:** highlight any part of a formula in edit mode and press F9 — Excel replaces it with its live result so you can see *which piece* is wrong. Press `Esc` (not Enter) to avoid overwriting.
- **Evaluate Formula:** `Alt, M, V` steps through calculation order.
- **Show Formulas:** `Ctrl + ` `` (grave) toggles the whole sheet between values and formulas — the fastest audit view.

## Worked example / mini-project

Build a one-tab **GST output MIS** for a trading firm. Reproduce this exactly.

Inputs (blue font, put the rate in a locked cell `B1`):

| | A | B | C | D |
|---|---|---|---|---|
| 1 | GST Rate | 18% | | |
| 3 | Invoice | State | Taxable (₹) | GST (₹) |
| 4 | INV-001 | Karnataka | 1,20,000 | =C4*$B$1 |
| 5 | INV-002 | Maharashtra | 85,000 | =C5*$B$1 |
| 6 | INV-003 | Karnataka | 2,40,000 | =C6*$B$1 |
| 7 | INV-004 | Tamil Nadu | 60,000 | =C7*$B$1 |

Now the summary block using **named ranges**. Select `C4:C7`, name it `Taxable`; name `B4:B7` as `State`; name `D4:D7` as `GST`.

```
Total taxable:      =SUM(Taxable)                → 5,05,000
Total GST:          =SUM(GST)                    → 90,900
Karnataka taxable:  =SUMIFS(Taxable,State,"Karnataka")   → 3,60,000
Invoice count:      =COUNTA(State)               → 4
Highest invoice:    =MAX(Taxable)                → 2,40,000
```

Add a lookup so a user can type a state and get its GST:

```
=SUMIFS(GST, State, G1)     // G1 = "Maharashtra" → 15,300
```

Format column C and D with `#,##0;[Red](#,##0)`. Now **audit it**: click the Total GST cell, press `Ctrl + [` — arrows should point only to `D4:D7`. Click a single GST cell, press `F2`, highlight `$B$1`, press `F9` — it shows `0.18`. Press `Esc`. If you change `B1` to 12%, every GST cell and both totals update because you locked the rate instead of hard-coding it. That single behaviour — one input, cascading correctly — is what an interviewer is checking for.

## How it's tested

**Timed practical (most common for FP&A/MIS/audit):** you get a raw dump — say 2,000 rows of sales — and 20–30 minutes to produce a summary. They watch whether you reach for the mouse, whether you use `Ctrl+T` and `SUMIFS`, and whether your negatives are formatted. Speed with keyboard navigation is the visible signal.

**Big 4 audit assessment:** clean a messy trial balance, tie a subtotal, and flag hard-coded overrides inside formulas. They deliberately plant a cell like `=SUM(B2:B40)+500` for you to catch using audit tools.

**Interview questions you should answer instantly:**

- "Difference between `A1`, `$A$1`, and `A$1`, and when do you use each?"
- "How do you check what feeds a total?" (Trace Precedents / Ctrl+[)
- "A formula copied down gives wrong answers from row 2 — what's the likely cause?" (missing `$` on a constant reference)
- "How would you present ₹4,50,00,000 in a board deck?" (in ₹ crore, one decimal, labelled)
- "What does F9 do inside a formula?"

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | The pro habit |
|---|---|---|
| Hard-coding numbers in formulas (`=C4*0.18`) | Nobody can find or update the rate | One input cell, referenced everywhere |
| Forgetting `$` before dragging | Silent wrong totals | F4 to lock, then drag |
| Using the mouse for everything | Slow; visible in a timed test | Ctrl+Arrow navigation |
| Merged cells everywhere | Breaks sorting, `SUMIFS`, selection | "Center Across Selection" instead |
| Dividing by 1,00,000 inside number format | Format ≠ math; breaks totals | Divide in a helper cell, label the header |
| No colour coding | Reviewer can't tell input from formula | Blue = input, black = formula, green = link |
| Overwriting after F9 | Corrupts the formula | Always Esc, never Enter, after F9 |
| Volatile clutter (`NOW()`, `INDIRECT` everywhere) | Slow, recalcs constantly | Use static `Ctrl+;` dates, minimise volatiles |

## Learn-it roadmap & resources

Realistic time to the employable bar: **2–3 weeks at 1 hour/day**, if you actually rebuild examples rather than watch.

- **Week 1:** Keyboard navigation + shortcuts. Rule: unplug the mouse for one hour daily. Practise `Ctrl+Arrow`, `Alt` ribbon paths, `F2`, `F4`.
- **Week 2:** Number formatting, absolute refs, named ranges. Rebuild the GST MIS above from scratch three times.
- **Week 3:** Auditing (Trace Precedents, F9, Evaluate Formula) + workbook structure (inputs/calc/output separation, colour coding).

Resources:

- **Free:** ExcelJet shortcut list and "Excel Formula" glossary; Microsoft's own support pages for Custom Number Formats; Corporate Finance Institute's free Excel fundamentals articles.
- **Free video:** Leila Gharani and ExcelIsFun (YouTube) — pick one 30-minute foundations playlist and finish it.
- **Paid/certification:** **Microsoft Office Specialist: Excel Associate (MO-200)** — globally portable, cheap, and a real line on a CV. CFI's **FMVA** covers this plus modelling (more relevant once you hit Chapter 3+). For India roles, no certificate beats being visibly fast in the timed test — but MO-200 gets you shortlisted.

Practice data: export any bank statement or a GSTR-2B to Excel and force yourself to summarise it keyboard-only.

## Quick-reference

**Navigation & editing**

```
Ctrl+Arrow         jump to data edge
Ctrl+Shift+Arrow   select to edge
Ctrl+T             make a Table
Alt+=              AutoSum
Ctrl+;             static date
F2                 edit / see formula
F4                 toggle $ locks
Alt,E,S,V          Paste values
Ctrl+`             show all formulas
```

**References**

```
A1     relative      $A$1   fully locked
A$1    row locked    $A1    column locked
F4     cycles all four states
```

**Auditing**

```
Ctrl+[        select precedents
Alt,M,P       trace precedents (arrows)
Alt,M,D       trace dependents
F9            evaluate selected formula part (then Esc)
Alt,M,V       Evaluate Formula step-through
```

**Finance number formats (Ctrl+1 → Custom)**

```
#,##0.00;[Red](#,##0.00);"-"        accounting, red negatives
[$₹-en-IN] #,##0                     rupee symbol
#,##0.00" L"                         label as lakhs (divide source separately)
```

**Golden rules:** one input cell per assumption · lock rates with `$` · blue inputs / black formulas · never hard-code · Esc after F9 · label ₹ scale in the header.
