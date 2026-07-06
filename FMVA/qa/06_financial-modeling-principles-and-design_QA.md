# Q&A — Financial Modeling — Principles and Model Design

Practice bank for Chapter 06. Work each question before reading the answer. This chapter is about *how* you build, not *what* you forecast — so the computational problems test layout discipline, anchoring, checks, and scenario switches. Every number is built so you can reproduce it cell-for-cell in Excel and watch it tie.

---

## Section A — Concept Checks (test the WHY)

**A1. Why separate a model into three physical layers (Inputs → Calculations → Outputs) instead of just typing numbers where they are needed?**

Because separation localises both change and error along a one-directional chain. When inputs, calculations, and outputs are physically apart, a change to an assumption cannot accidentally overwrite a formula, and a formula cannot hide a buried hardcode. When an output looks wrong, you trace *backwards* along a clean chain to exactly one source. In a "warehouse" model where everything touches everything, a wrong number could originate anywhere, so every audit is a full re-check. The layers turn debugging from a search of the whole sheet into a walk up one wire.

**A2. Why is a model judged by how *often* it will be used rather than how well it was built once?**

Because a model is *used* far more than it is *built*. You build it once over a few days; then it is interrogated hundreds of times — every sensitivity, scenario, review comment, and reuse on the next deal. A messy model is cheap to build and ruinously expensive to change; a disciplined model costs slightly more up front and is nearly free to change thereafter. Over the model's life the disciplined one wins overwhelmingly, because the marginal cost of the twentieth "what if" is what actually dominates the economics.

**A3. Why does "one number lives in one cell, everything else points at it" make a model self-consistent by construction?**

Because if the tax rate exists in a single cell and forty formulas reference it, the model *cannot* disagree with itself about the tax rate — inconsistency becomes structurally impossible rather than something you police by hand. The moment a fact is duplicated (the same 25% typed into ten formulas), the possibility of the copies drifting apart is created, and someone will eventually change nine and miss one. Single-sourcing is the same normalisation principle a database uses: store each fact once so it can never contradict itself.

**A4. Why does the row-consistency rule (one formula copied across a row) buy auditability?**

Because it lets a reviewer verify one cell and trust sixty. If every period in a row is the identical formula differing only in relative column references, checking the leftmost forecast cell proves the whole row — it was copied, so it cannot silently diverge in year 3. Hand-typing each period is precisely how you get a subtly different formula in one column that nobody notices, the classic model-killer. Consistency converts an audit of the whole timeline into an audit of a single cell.

**A5. Why are hardcodes buried inside formulas the single most-cited reason a model fails an audit?**

Three compounding reasons. Single source of truth: a literal `1.08` appearing in twelve formulas means the assumption changes in twelve places and one gets missed. Transparency: a reviewer cannot see `1.08` inside a formula bar without clicking every cell, whereas a blue input is self-documenting. Sensitivity: you cannot run a data table or scenario on a number trapped inside a formula — only a cell can be flexed. The hardcode defeats all three of the properties that make a model a live engine rather than a static report.

**A6. Why is the balance-sheet check the most important single cell in an integrated model?**

Because it is a continuously evaluated *proof* that the double-entry logic held across every formula. If `Assets − Liabilities − Equity = 0`, every link fired with the right sign and magnitude; the instant it goes non-zero you have a missed or mis-signed wire — and you learn it *before* trusting any downstream valuation. It is a smoke detector: cheap, always-on, and it fails loud. The most dangerous error is a plausible-looking wrong number; the balance check is what turns that silent error into a visible alarm.

**A7. Why is deliberately "plugging" cash (defining it as whatever makes the sheet balance) worse than leaving a broken model broken?**

Because a broken balance is honest — it tells you an error exists. A plug silences the detector while the fire still burns: cash is defined as `L+E − other assets`, so the balance check can never be non-zero, and any real error elsewhere now flows silently into a wrong cash figure instead of tripping the alarm. Cash must be driven independently by the cash roll (`opening + CFO + CFI + CFF`); only an independently-computed cash makes the balance check a genuine, unfaked proof.

---

## Section B — Build / Computational Problems

**B1. Anchoring a row.** Base-year revenue is in `C4` = 100.0; growth rate in `C5` = 8.0%. You will build a four-year revenue row in cells E6:H6, first period referencing the base year. Write the exact formula for E6, state which references are absolute vs relative and why, then give the copied formula in F6 and the four resulting values.

- `E6: =$C$4*(1+$C$5)`
- `$C$4` and `$C$5` are **absolute** (dollar-anchored) so they stay pinned to the assumption cells when the formula is copied right. Nothing else needs to move for period one.
- When copied to F6 it must chain off the prior period, so from F6 onward the prior-period reference is **relative**: `F6: =E6*(1+$C$5)`, `G6: =F6*(1+$C$5)`, `H6: =G6*(1+$C$5)`. The prior-year reference marches right; the growth assumption stays pinned by the `$`.
- Values: `100×1.08 = 108.00`; `108×1.08 = 116.64`; `116.64×1.08 = 125.97`; `125.97×1.08 = 136.05`.

The payoff: change `C5` to 6% and the row becomes `106.00, 112.36, 119.10, 126.25` with no formula edited — one number, one place, four outputs recomputed.

**B2. De-hardcoding a formula.** A row currently reads `=D10*1.08 - D10*0.30` (8% growth then a 30% cost ratio, both typed literals). Rewrite it to professional standard, listing the input cells you would create, and confirm the number is unchanged for `D10 = 200`.

Create two blue inputs: growth in `$C$4` = 8%, cost ratio in `$C$5` = 30%. The faithful de-hardcode is `=D10*(1+$C$4) - D10*$C$5` — the `1` in `(1+…)` is a tolerated arithmetic constant, not an assumption.

Check: `200×1.08 − 200×0.30 = 216 − 60 = 156`, unchanged. The exercise exposes why hardcodes are dangerous: pulling the literals into labelled cells reveals an ambiguity the buried numbers hid — does the 30% apply to the *base* (`D10*$C$5 = 60`, giving 156) or to *grown* revenue (`=D10*(1+$C$4)*(1-$C$5) = 216×0.70 = 151.20`)? A number trapped inside a formula silently makes that choice for you and no reviewer can see it.

**B3. Build a scenario switch.** A switch input sits in `C1`. The scenario table lists revenue growth: Base 8% (E10), Bull 12% (E11), Bear 3% (E12). Write the active-growth formula two ways (`INDEX/MATCH`-style and `CHOOSE`), then give active growth and Year-1 revenue (off B1's 100 base) for `C1 = 1, 2, 3`.

- `INDEX`: `=INDEX($E$10:$E$12, $C$1)` — the switch integer is the row offset into the table.
- `CHOOSE`: `=CHOOSE($C$1, $E$10, $E$11, $E$12)`.
- `C1 = 1` → 8% → `100×1.08 = 108.00`
- `C1 = 2` → 12% → `100×1.12 = 112.00`
- `C1 = 3` → 3% → `100×1.03 = 103.00`

Every downstream statement recomputes off that one blue integer — the scenario is now the single source of truth.

**B4. Mini three-statement close with a balance check.** Opening: Cash 50, PP&E (net) 200, Debt 100, Share capital 100, Retained earnings 50. Year-1 assumptions: Revenue 300; operating costs (excl. dep.) 200; depreciation 20; interest 5% on opening debt; tax 25%; capex 30; dividends 10; debt repayment 20. Build all three statements and prove the balance.

**Income statement:**

| Line | Working | Value |
|---|---|---|
| Revenue | input | 300 |
| Operating costs | input | (200) |
| Depreciation | input | (20) |
| EBIT | `=SUM(above)` | 80 |
| Interest | `−5% × 100` | (5) |
| Profit before tax | | 75 |
| Tax | `−25% × 75` | (18.75) |
| **Net income** | | **56.25** |

**Cash flow statement:**

| Line | Value |
|---|---|
| Net income | 56.25 |
| + Depreciation (non-cash) | 20 |
| **Cash from operations** | **76.25** |
| − Capex | (30) |
| − Debt repayment | (20) |
| − Dividends | (10) |
| **Net change in cash** | **16.25** |
| Opening cash | 50 |
| **Closing cash** | **66.25** |

**Closing balance sheet:**

| Assets | | Liabilities + Equity | |
|---|---|---|---|
| Cash (50 + 16.25) | 66.25 | Debt (100 − 20) | 80.00 |
| PP&E (200 − 20 + 30) | 210.00 | Share capital | 100.00 |
| | | Retained earnings (50 + 56.25 − 10) | 96.25 |
| **Total assets** | **276.25** | **Total L + E** | **276.25** |

**Balance check:** `276.25 − 276.25 = 0.` ✓ Net income flowed to RE; depreciation added back in CFO reconciles to the PP&E roll-forward; debt repayment hit both the cash flow and the debt balance.

**B5. Watch the check catch an error.** Take B4 and deliberately break one link: code retained earnings as `=Opening RE + Net income` (forgetting dividends). Recompute RE, the L+E total, and the balance check. State the sign and magnitude of the failure.

- Broken RE = `50 + 56.25 = 106.25` (should be 96.25) — **10 too high**.
- Cash is unaffected (the 10 dividend still left via CFF), so assets stay 276.25.
- Total L+E = `80 + 100 + 106.25 = 286.25`.
- **Balance check = `276.25 − 286.25 = −10`.** The alarm fires at exactly the size of the omitted dividend, pointing straight at the RE roll-forward. That is the check doing its one job.

**B6. Build the check block.** For B4 you have three checks: (a) balance `Assets − Liab − Equity`; (b) cash tie `CFS closing cash − BS cash`; (c) RE roll `Opening RE + NI − Div − Closing RE`. Write the master-check formula and evaluate it for B4 (correct) and for B5 (broken RE).

Master (using a tolerance to absorb floating-point rounding):
`=IF(SUMPRODUCT(ABS(check_range)) < 0.01, "OK", "ERROR")`
or the Boolean form `=IF(AND(a=0, b=0, c=0), "OK", "ERROR")`.

- **B4:** a = 0, b = `66.25 − 66.25 = 0`, c = `50 + 56.25 − 10 − 96.25 = 0` → all zero → **"OK"**.
- **B5:** a = −10, c = `50 + 56.25 − 10 − 106.25 = −10` → `SUMPRODUCT(ABS(...)) = 20 > 0.01` → **"ERROR"**. Pin this one cell in view (or on the cover tab) with conditional formatting and you cannot miss the model going wrong mid-build.

---

## Section C — Interview-Style Questions

**C1. "What makes a good financial model? What do you look for when you open someone else's?"**

Model answer: I look for structure before I look at the numbers. Are inputs, calculations, and outputs separated and flowing one way? Is the colour code honest — blue for inputs, black for same-sheet formulas, green for links — so I can see in seconds what drives the model? Do the rows use one formula copied across, so I can audit the first cell and trust the row? Are there no hardcodes buried inside formulas? And critically, is there a live balance check reading zero in every period, ideally pinned somewhere visible? A model that has those properties I can trust and flex in the room; one that doesn't, I have to reverse-engineer before I believe a single output.

**C2. "Why does the colour-coding convention actually matter — isn't it just cosmetic?"**

Model answer: It is metadata, not decoration. Colour tells the reader the *nature* of a cell at a glance: blue means "an input you may change," black means "a same-sheet formula, don't type over it," green means "a link to another sheet." The single load-bearing rule is that if it's blue you can flex it and if it's black or green you must not overwrite it. That is what stops a reviewer or my future self from typing a number over a formula and silently corrupting the model, and it is what lets someone scanning for "what drives this" find every assumption instantly. Convention converts my specific model into the familiar shape all good models share, and familiarity is what lets someone verify it fast.

**C3. "How do you handle circular references in a model — say interest on average debt?"**

Model answer: First, I distinguish deliberate from accidental. Interest on average debt or a cash sweep is a genuine circularity — interest feeds net income, which feeds cash, which feeds the debt balance, which feeds interest. I handle it by enabling iterative calculation (File → Options → Formulas), and I always build a circularity breaker: a switch cell that zeroes the circular link so if the model blows up into a `#REF!` or `0` cascade I can flip it off, restore stability, and switch it back. I also add an error check so a broken circular is visible. Accidental circularity, though, I avoid entirely by respecting the one-directional Inputs → Calculations → Outputs flow — an output should never feed back into an early calculation.

**C4. "You change one assumption and the whole model recalculates. What design choices made that possible?"**

Model answer: Three, working together. Single source of truth — the assumption lives in exactly one labelled cell, so changing it there is the only edit needed. No hardcodes — because the number was never duplicated inside formulas, there is nothing else to update and nothing to miss. And one-directional flow with row consistency — every dependent cell references that input directly or transitively, so the recalculation propagates automatically down a clean chain. The scenario switch is the extreme version: a single integer flips Base/Bull/Bear via `INDEX` or `CHOOSE`, and the entire model is that integer's obedient function.

**C5. "What's the first thing you do when you sit down to build a new model?"**

Model answer: I sketch the skeleton on a blank sheet *before* typing a single formula — which assumptions drive the business, which supporting schedules I need (revenue, depreciation/PP&E, debt, working capital), and which statements and metrics are the actual deliverable. Then I reserve tabs in dependency order: Cover, Dashboard, Assumptions, the three statements, Schedules, Valuation, Checks. Only then do I build, inputs first, then calculations, then outputs — so that when I write a calculation the input it points at already exists. Design is the first decision, made before any number is typed, because retrofitting structure onto a warehouse model is harder than rebuilding it.

**C6. "Why keep a dedicated Checks tab instead of just eyeballing whether the model looks right?"**

Model answer: Because the most dangerous error is the plausible-looking wrong number — the one that passes an eyeball test and reaches the committee. A checks tab aggregates every integrity test (balance sheet balances, cash ties to the balance sheet, retained earnings rolls forward, debt and cash stay non-negative, sources equal uses) into Boolean or zero-difference cells, then rolls them into one master check I watch continuously with conditional formatting. It converts silent errors into loud ones the instant they appear. I'd rather the model tell me it's wrong than trust my eye across a hundred cells I changed in the last five minutes.

---

## Section D — Common-Error Spotting

**D1. Hardcoded growth.** A revenue row reads `=D10*1.08` copied across, with `D10 = 200`. It "works" — Year 1 shows 216. Name every professional failing and give the fix.

The `1.08` is a hardcode buried inside the formula. It (1) violates single source of truth — the 8% appears invisibly in every period cell, so changing the assumption means editing every formula and inevitably missing one; (2) is opaque — a reviewer can't see it without clicking each cell; (3) can't be sensitised — no data table or scenario can reach a number trapped inside a formula. Fix: put 8% in a blue input `$C$4` and write `=D10*(1+$C$4)`. The `1` is a tolerated arithmetic constant; the 8% is a business assumption that must be a labelled cell.

**D2. Anchoring failure.** An analyst writes `E6: =D6*(1+C5)` with the growth rate in `C5`, then copies it across the row. Year 1 is correct at 108 but later years are wildly wrong. What broke?

The growth reference `C5` was left **relative** instead of absolute. On copy to F6 it became `=E6*(1+D5)`, pointing at `D5` (an empty or unrelated cell) rather than staying pinned to the growth assumption. The prior-period reference marching right is correct and *should* be relative; the assumption must be anchored. Fix: `E6: =D6*(1+$C$5)` — press F4 on the `C5` reference while editing to lock it. This is the exact bug the row-consistency rule guards against: the formula wasn't truly identical-with-shifted-columns because one reference that should have been pinned wasn't.

**D3. Plugged cash.** A model's balance check reads zero in every period, but tracing the cash cell shows `=Total L&E − (Receivables + Inventory + PP&E)` rather than `=Opening cash + Net change in cash`. Why is this a serious defect even though it "balances"?

Cash has been made a **plug** — defined as whatever forces assets to equal L+E — so the balance check is structurally incapable of ever being non-zero. The detector is disabled. Any real error elsewhere (a wrong margin, a missed dividend, a broken debt link) now flows silently into a wrong cash number instead of tripping the check, and the model looks perfectly consistent while producing a false answer. Cash must be driven independently by the cash roll (`opening + CFO + CFI + CFF`); only an independently-computed cash makes the balance check a genuine, unfaked proof. An interviewer who presses Ctrl+[ on the cash cell finds this in seconds.

**D4. Inconsistent row.** A five-year cost row was hand-typed period by period. Years 1, 2, 4, 5 read `=revenue*$C$6` (cost ratio in C6), but Year 3 reads `=revenue*0.32` — a one-off override someone typed during a meeting and never reverted. The totals look plausible. Why is this the "classic model-killer," and how would you have caught it?

Because it is invisible: the forecast is silently wrong for exactly one period, and nothing flags it — the number is plausible and the row *looks* uniform. It violates row consistency (the formula is not identical-with-shifted-columns across the row) and smuggles in a hardcode (`0.32`). Catch it two ways: (1) audit discipline — check the first cell then confirm the row was *copied*, not typed, so a lone divergent cell stands out; (2) press Ctrl+` (Show Formulas) and scan the row — a stray literal `0.32` among `$C$6` references is immediately visible. Fix: re-enter the first cell correctly and copy across the whole row.

**D5. Broken master check.** A checks tab computes three differences and a master `=IF(SUM(check1:check3)=0, "OK", "ERROR")`. The individual checks are +12, −12, and 0. The master proudly reads "OK." What's wrong with the aggregation?

Summing signed differences lets errors **cancel**: `+12 + (−12) + 0 = 0`, so two real, offsetting failures report as "OK." A master check must aggregate *magnitudes*, not signed values. Fix: `=IF(SUMPRODUCT(ABS(check1:check3)) < 0.01, "OK", "ERROR")`, which gives `24 > 0.01 → "ERROR"` and correctly flags the model. Also prefer a small tolerance (0.01) over exact `=0` to absorb harmless floating-point rounding while still catching genuine breaks.

**D6. ROUND in live logic.** To make outputs "look clean," a modeller wraps `=ROUND(EBIT*(1-taxrate), 0)` inside the net-income calculation that feeds the cash flow and retained earnings. The balance check now reads 0.4 in some periods. Diagnose and fix.

Rounding *inside live logic* discards fractional cents that the downstream statements still expect to be there, so the cash roll and RE roll-forward no longer tie to full precision and the balance sheet fails to close by pennies. `ROUND` belongs to *display*, not calculation. Fix: remove `ROUND` from the formula, keep full precision throughout the model, and control appearance with a number *format* (e.g. `#,##0`) which rounds only what is shown, not what is stored. The rule: never let a display concern corrupt a figure that must reconcile.

---

*Self-check: rebuild B4 in Excel with every number as a live formula, then perform B5 — deliberately break the retained-earnings link and confirm the master check flips to "ERROR" at exactly −10. If your check catches the error you planted, your linkages are formulas, not hardcodes, and you have the design discipline every three-statement, DCF, and LBO chapter that follows is built on.*
