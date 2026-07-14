# The Modeling Test & Terminal Interview Drills + Cheat-Sheet

## What you'll be able to do

Walk into a timed modelling test (the 60–90 minute build-a-3-statement-and-DCF-from-a-blank-sheet exercise) and know exactly what the reviewer is watching, how to structure for speed, which keyboard shortcuts save you ten minutes, and how to keep the model auditable. You'll also handle the rapid-fire terminal function quiz and the standing valuation Q&A, and you'll have a one-page cheat-sheet of every formula and function you need under time pressure.

## The drill — step by step

**Step 1 — Before you type, set the frame (2 min).** Read the prompt, note the deliverable (usually: 3-statement + DCF, one or two scenarios, an answer to "is it cheap?"). Lay out tabs: `Assumptions`, `Model` (IS/BS/CF stacked), `DCF`, `Output`. Colour convention immediately — **blue = hardcoded input, black = formula, green = link to another sheet**. Reviewers grade this in the first 30 seconds.

**Step 2 — Build the income statement top-down (10 min).** One driver: revenue growth. Everything else as a % of revenue or a margin. Wire tax off PBT. Don't hardcode any calculated cell — if a number can be computed, compute it.

**Step 3 — Balance sheet and the cash-flow bridge (20 min).** Build working-capital via **days**: DSO, DIO, DPO drive receivables, inventory, payables. PP&E roll-forward: opening + capex − depreciation. Debt and equity from a simple schedule. Then the **cash flow statement links everything**: CFO from net income + D&A ± ΔNWC, CFI = −capex, CFF = debt/equity flows. Ending cash flows back to the balance sheet.

**Step 4 — Make it balance (5 min).** The whole test is really "does your balance sheet balance?" Build a check row: `Assets − Liabilities − Equity = 0` in every column, conditionally formatted red if non-zero. If it doesn't tie, 90% of the time it's the cash flow statement not fully feeding ending cash, or a working-capital sign error.

**Step 5 — DCF on top (15 min).** FCFF = EBIT×(1−t) + D&A − capex − ΔNWC (chapter 5). WACC box, terminal value (Gordon), discount, EV-to-equity bridge, per-share. Add a `Data Table` sensitivity (WACC × g).

**Step 6 — Checks and a one-line answer (5 min).** Turn on every check row. Then, in a cell or out loud, state the conclusion: *"Fair value ₹185 vs price ₹280 — overvalued, DCF-implied exit multiple 8.4× below comps 12×."* The reviewer wants a *view*, not just a number.

### What they're actually watching

| Dimension | Pass | Fail |
|---|---|---|
| Structure | Inputs separated, colour-coded, one driver | Hardcodes buried in formulas |
| Formulas | No plugs, everything links | Balancing figure typed in by hand |
| Checks | Balance check + cash tie, visible | No checks, silent errors |
| Speed | Shortcuts, no mouse for navigation | Formatting the sheet for 20 min |
| Judgement | States a view with a sanity check | Delivers a number with no context |

### Speed shortcuts (no-mouse modelling)

- `F2` edit cell, `F4` toggle absolute refs (`$A$1`), `Ctrl+;` today's date.
- `Alt+=` autosum. `Ctrl+Shift+arrow` select to edge. `Ctrl+D`/`Ctrl+R` fill down/right.
- `Alt,H,O,I` autofit column. `Alt,A,W,T` open Data Table. `Ctrl+[` trace precedent.
- `F9` recalc; `Ctrl+`` (grave) show all formulas for a fast audit.
- Name your WACC and tax cells so formulas read `=EBIT*(1-tax)` not `=D12*(1-$B$4)`.

### Terminal / CapIQ function quiz (rapid fire)

| Task | Bloomberg | CapIQ / free proxy |
|---|---|---|
| Price history to Excel | `=BDH(...)` | `=CIQ(...)` / Screener export |
| Current field (P/E, mkt cap) | `=BDP("TICK","PE_RATIO")` | `=CIQ("IQ_PE_EXCL")` |
| Company financials screen | `FA <GO>` | Financials template |
| Beta | `BETA <GO>` | `SLOPE()` regression (free) |
| Comparable companies | `RV <GO>` | Comps template |
| Relative valuation / football | `EQRV <GO>` | build manually |
| Debt / capital structure | `DDIS <GO>` | annual report |
| Estimates / consensus | `EEO <GO>` / `EE <GO>` | Trendlyne |
| Supply chain | `SPLC <GO>` | annual report |
| News run | `CN <GO>` | Google News |

## The output

A finished test artefact is: a colour-coded 3-statement model that balances in every column (visible check row of zeros), a DCF tab with a WACC box and a WACC×g sensitivity grid, and a one-line verdict. It looks disciplined — inputs in blue on their own tab, no orphaned hardcodes, checks green. And the one-pager below, which you can reconstruct from memory in the first two minutes of any test as your scaffold.

### The one-page cheat-sheet

**Free cash flow**
```
FCFF = EBIT × (1 − t) + D&A − Capex − ΔNWC     → discount at WACC → EV
FCFE = FCFF − Interest×(1−t) + Net borrowing    → discount at Ke  → Equity
```
**WACC & CAPM**
```
Ke   = Rf + β × ERP
Kd   = pre-tax cost of debt × (1 − t)
WACC = (E/V)×Ke + (D/V)×Kd
```
**Terminal value**
```
Gordon:  TV = FCFF_n × (1+g) / (WACC − g)      [g < WACC, g ≤ nominal GDP]
Exit:    TV = EBITDA_n × exit multiple
Implied exit multiple = Gordon TV / EBITDA_n   (cross-check)
```
**Bridge**
```
Equity = EV − Net debt − Minority − Preferred + Associates
Per share = Equity / diluted shares
```
**Multiples**
```
EV/EBITDA, EV/EBIT, EV/Sales   (capital-structure neutral → use EV)
P/E, P/B, P/FCFE               (equity multiples → use price)
PEG = P/E ÷ growth
```
**LBO**
```
Sources = Uses (equity is the plug, fees are a Use)
MOIC = exit equity / entry equity
IRR  ≈ MOIC^(1/years) − 1      (single entry/exit, no interim CF)
Returns = deleveraging + EBITDA growth + multiple change
```
**Best practice:** blue input / black formula / green link · one driver, margins do the rest · no hardcoded plugs · balance-check row = 0 · TV = 60–80% of EV · nominal CF with nominal WACC · state a view.

## Checks & gotchas

- **Balance-sheet imbalance** almost always = cash flow statement not fully wired or a working-capital sign flip. Fix the CF, don't plug the BS.
- **Circularity** (interest ↔ debt ↔ cash) — enable iterative calc *before* it errors, or use opening-balance interest.
- **Hardcoded plugs** are the single fastest way to fail; the reviewer traces one formula and finds it.
- **Formatting over substance** — don't spend 20 minutes on borders and a blank model. Function first, polish last.
- **No view** — a technically perfect model with no "cheap or dear?" conclusion still disappoints. Always land the plane.
- **Mixing real and nominal**, or effective vs marginal tax — silent value errors the reviewer will probe.

## Interview drill

**Q: Your model doesn't balance — walk me through debugging it.** First, isolate the column where the check first goes non-zero — the error started that year. Then check the cash flow statement: does ending cash on the CF equal the cash line on the BS? Usually not, meaning a flow is missing or double-counted — most often a working-capital sign (an increase in receivables is a *use* of cash, negative in CFO) or capex not linked to both PP&E and CFI. I fix the source, never plug the balance sheet, because a plug hides the real error.

**Q: You have 60 minutes for a 3-statement plus DCF — how do you spend it?** Two minutes framing tabs and colour convention, ten on a driver-based income statement, twenty on the balance sheet and the cash-flow bridge, five making it balance with a visible check row, fifteen on the DCF and a sensitivity table, and the last five turning on checks and writing the one-line conclusion. I build ugly-but-linked first and only format if time remains — a balancing model with no borders beats a beautiful model that plugs.

**Q: EV/EBITDA vs P/E — when each?** EV multiples are capital-structure-neutral, so I use EV/EBITDA to compare companies with different leverage or to value the whole enterprise — it's above the interest line. P/E is an equity multiple, sensitive to leverage and tax, useful for comparing similar-capital-structure peers or when the market quotes the sector on earnings. For a leveraged or acquisitive name I lead with EV/EBITDA; for a stable financial or a consumer name the market prices on P/E, so I show both.

## Practise free

Do the whole thing in plain Excel — no terminal required. Grab a company's five years from **Screener.in**, then rebuild the 3-statement model *from a blank sheet* against a timer (start at 90 minutes, work down to 60). Enforce the colour convention and a balance-check row every time. Replace terminal functions with their free equivalents: beta via `=SLOPE()` regression, risk-free from the RBI 10-year, ERP from Damodaran's free January dataset, comps built by hand from Screener. Rehearse the function quiz as flashcards (BDP/BDH, FA, RV, EQRV, BETA, EEO). Run a `Data Table` for the sensitivity grid. Time-box mercilessly and, at the buzzer, force yourself to write the one-line verdict — the muscle you're building is *finishing with a view under time pressure*, which is exactly what the real test grades.
