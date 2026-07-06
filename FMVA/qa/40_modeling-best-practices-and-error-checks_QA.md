# Q&A — Modeling Best Practices and Error Checks

Practice bank for the chapter on Modeling Best Practices and Error Checks. Work each question before reading the answer. The spine of this chapter: a model is a communication tool first and a calculation tool second, so **discipline** (colour coding, one formula per row, inputs separated from calculations) and **redundancy** (compute a number two independent ways and demand they agree) are not decoration — they are what makes a model trustworthy, auditable, and survivable in someone else's hands.

**The reference mini-model (Section B leans on it).** One-period forecast. Openings: cash 100, PP&E 500, debt 100, share capital 200, retained earnings 300 (so opening assets 600 = opening claims 600). Flows for the year: revenue 1,000; cash operating costs 700; depreciation 50; capex 80; dividends 20; interest and tax 0.

Correctly built: net income = 1,000 − 700 − 50 = **250**; cash flow = 250 + 50 (add back dep) − 80 (capex) − 20 (dividends) = **+200** → ending cash = 100 + 200 = **300**; closing PP&E = 500 + 80 − 50 = **530**; closing RE = 300 + 250 − 20 = **530**. Balance sheet: assets 300 + 530 = **830**; liabilities + equity 100 + 200 + 530 = **830**. It balances.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is the colour convention (blue = input, black = formula, green = link to another sheet) worth the keystrokes?**

Because it makes a cell's *type* visible without clicking into it. A reviewer, or you in six months, needs to know instantly which cells are safe to change (blue assumptions) and which must never be overtyped (black formulas that would silently become hard-codes). Colour turns an opaque grid into a map: you can scan a column and see at a glance whether the logic is intact or whether someone has plugged a constant into a calculation row. It is the cheapest audit tool in the workbook.

**A2. Why separate inputs, calculations, and outputs into distinct areas or tabs rather than interleaving them?**

Because the three have different jobs and different edit rules. Inputs are the only things a user should touch; calculations are machinery that should be left alone; outputs are the answer to present. Mixing them means a user hunting for an assumption stumbles through formulas, and a reviewer cannot tell the levers from the wiring. Separation localises change — you tweak one assumptions block and the whole model responds — and it is what lets scenarios, sensitivity tables, and clean handoff work at all.

**A3. Why "one formula per row, copied across" instead of bespoke formulas per cell?**

Because consistency across a row is itself an error check: if column F does something column G does not, either there is a deliberate reason (rare) or a bug (common). A uniform row can be audited by inspecting a single cell and trusting the copy; a ragged row must be checked cell by cell. It also makes the model extensible — drag one more column and next year appears — and it makes anomalies visible, because the one cell that breaks the pattern lights up in a formula-consistency check.

**A4. Why is hard-coding a number inside a formula (e.g. `=Revenue*1.05`) considered a defect even when the number is correct today?**

Because the assumption is now buried where no one will find it and no scenario can reach it. The 1.05 growth rate belongs in a labelled blue input cell so it can be seen, sensitised, and changed in one place. Buried constants are how a model quietly keeps using last year's tax rate or an obsolete FX assumption — the number was right once, nobody knew where it lived, and it never got updated. Every assumption should have exactly one visible home.

**A5. Why is "redundancy" the principle underneath every error check?**

Because a single number cannot verify itself — it can only be checked against a *second, independent* route to the same answer. If two computations agree, the logic between them is almost certainly sound; if they disagree, you have caught a bug for free. The balance check is assets one way versus claims another; the cash tie is cash from the cash flow statement versus cash on the balance sheet; a rollforward is a balance re-derived from its flows versus the balance actually posted. No redundancy, no test.

**A6. A model balances in every period. Does that prove it is correct?**

No. Balancing proves the accounting identities hold, but a model can satisfy Assets = Liabilities + Equity while being economically absurd: negative cash, gross margin above 100%, a debt sweep repaying more than is owed. Those violate reality, not accounting, so they pass the balance check untouched. This is why *sanity checks* (is cash ever negative? is margin plausible?) sit alongside *integrity checks* (does it balance? does cash tie?) — the two families catch different classes of error.

**A7. Why is plugging the balance sheet the cardinal sin?**

Because it converts your best error *detector* into an error *concealer*. Force one line — equity, cash, a "plug" row — to equal whatever makes the sheet balance, and the balance check becomes `TRUE` by construction and can never fire again. You have wired the smoke detector to the light switch. Balance must *emerge* from every line being built honestly; the moment it is *imposed*, every real error hides behind a green flag.

**A8. Why should error checks be aggregated into a single master flag, and that flag mirrored onto every tab?**

Because a check nobody looks at is useless. Rolling every individual check up with an `AND` (or a count of failures) gives one cell that answers "is anything broken?", and linking that cell into the top corner of each sheet — conditionally formatted red — means a break glares at the analyst wherever they happen to be working, not just on a buried Checks tab. A model that balances today but breaks the moment a link is edited is a landmine; the mirrored master flag is what defuses it.

**A9. Why avoid volatile functions and unnecessary array formulas as a best practice?**

Because they degrade the two things that keep a model usable: speed and predictability. Volatile functions (`OFFSET`, `INDIRECT`, `NOW`, `RAND`) recalculate on every change whether or not their inputs moved, so a large model grinds. They also obscure precedent tracing — `INDIRECT` builds a reference from text, so `Ctrl+[` cannot follow it and an auditor is blind. Prefer transparent, traceable functions (`INDEX/MATCH`, direct links) so the model stays fast and every dependency is visible.

---

## Section B — Build / Computational Problems

Convention: outflows (capex, dividends, repayments) are stored **negative** in the cash flow; every check returns `TRUE` when the model is healthy; tolerance for dollar figures is 0.001.

**B1. The balance check on the reference model.** Total assets are in `F30`, total liabilities-plus-equity in `F45`. Write the raw difference and the tolerance-wrapped flag, and confirm the value.

Raw difference: `=F30-F45` → 830 − 830 = **0.0**.
Tolerance flag: `=ABS(F30-F45)<0.001` → `ABS(0) < 0.001` → **TRUE**.
Across a full horizon `F:K`, per-period flags live in row 46 and roll up with `=AND(F46:K46)` → **TRUE** only if every period balances. The model passes.

**B2. Why `ABS(diff) < tolerance` and not `diff = 0`?** Suppose the true difference is floating-point residue of `4.5E-11`. Show both tests.

`=(4.5E-11=0)` → **FALSE** — cries wolf on a perfectly balanced model, and an analyst who sees a red flag on a correct model soon learns to ignore all red flags.
`=ABS(4.5E-11)<0.001` → **TRUE** — passes genuine balance while still catching any real imbalance, because a real error dwarfs 0.001. Tolerance sits just above floating-point noise and well below any error that would matter.

**B3. The dropped depreciation add-back.** Someone deletes the depreciation add-back in the cash flow statement. Recompute cash, the balance sheet, and the balance check; name the imbalance.

Cash flow becomes NI 250 − capex 80 − dividends 20 = **+150** (the 50 add-back is gone); ending cash = 100 + 150 = **250**. Depreciation still correctly reduces PP&E (530) and still sits inside NI → RE (530); only the cash side lost the add-back.

| Assets | | Liab + Equity | |
|---|---:|---|---:|
| Cash | 250 | Debt | 100 |
| PP&E | 530 | Share capital | 200 |
| | | Retained earnings | 530 |
| **Total** | **780** | **Total** | **830** |

Check: `=ABS(780-830)<0.001` → `ABS(−50)` → **FALSE**. The imbalance is exactly **50** — the missing depreciation. The check fires *and* hands you the magnitude, pointing straight at the depreciation line. Reproduce in Excel and watch the flag turn red.

**B4. The cash tie localises a hard-code.** From the correct 830-balance model, a colleague overtypes the balance-sheet cash cell — properly linked `=CF!ending_cash` (300) — with the constant `310`. Build the balance check and the cash tie; explain which localises the error.

Assets = 310 + 530 = 840; L+E still 830. Balance check `=ABS(840-830)<0.001` → **FALSE** (off by 10): tells you *something* is wrong, not *where*.
Cash tie `=ABS(310-300)<0.001` → **FALSE**. Every other check (RE rollforward, PP&E rollforward) stays **TRUE**. Two red flags both pointing at cash → `Ctrl+[` traces precedents, finds a constant where a link belongs, restore `=CF!ending_cash`. Under a minute.

**B5. A formula-consistency check.** Row 20 forecasts revenue as `=prior*(1+growth)` copied across F:K, but someone overtyped `H20` with `=G20*1.05` (a buried 5%). Design a check that catches this without knowing the correct growth rate.

Compare each cell's *formula text* to its left neighbour's, adjusted one column, using a helper. In practice: `=FORMULATEXT(H20)` returns `=G20*1.05` while `=FORMULATEXT(G20)` returns `=F20*(1+$E$20)` — structurally different. A row flag `=SUMPRODUCT(--(NOT(EXACT( pattern of F20 shifted, actual ))))` counts mismatches; simpler in daily practice is Excel's built-in *inconsistent formula* green triangle, or select the row and `Ctrl+\` (select row differences) to highlight the odd cell. The point: consistency itself is the test — the one cell breaking the copied pattern is the suspect, regardless of what the right number is.

**B6. Sanity check for negative cash.** The model's ending-cash row is F30:K30. Write a single flag that is `TRUE` only if cash never goes negative in any period, and state why this is not caught by the balance check.

`=AND(F30:K30>=0)` → **TRUE** when every period's cash is non-negative. If, say, `H30` = −40, the flag is **FALSE**. The balance check stays green throughout, because negative cash still balances (a negative asset is offset by whatever financed the shortfall) — the accounting is internally consistent, the *economics* are not. Only a sanity check catches "this company ran out of money."

**B7. Rollforward as an independent recompute.** Retained earnings is posted on the balance sheet at 530. Independently rebuild it from flows and write the tie.

Rollforward: opening RE 300 + net income 250 − dividends 20 = **530**. Tie: `=ABS(BS_RE − (openRE + NI − div))<0.001` → `=ABS(530−530)` → **TRUE**. If someone later changes the dividend on the cash flow but not on the RE schedule, the two diverge and the tie fires — redundancy catching a partial edit.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through how you make a model auditable for someone who has never seen it."**

Three habits. First, structure: inputs, calculations, and outputs live in clearly separated areas or tabs, so a reviewer knows where the levers are. Second, colour: blue for inputs, black for formulas, green for cross-sheet links, so cell *type* is visible without clicking. Third, checks: a dedicated Checks tab aggregating balance ties, cash ties, and rollforwards into one master flag mirrored onto every sheet, so any break glares immediately. On top of that, one consistent formula per row so the logic can be audited by inspecting a single cell, and no hard-codes inside formulas — every assumption in a labelled input cell. The test I hold myself to: could a stranger find every assumption and verify every number without asking me a question?

**C2. "What error checks do you build into every model, and why those?"**

Two families. *Integrity checks* confirm the accounting holds: the balance check (assets minus liabilities-plus-equity within tolerance), the cash tie (cash flow statement ending cash equals balance-sheet cash), and rollforwards for PP&E, debt, and equity (each closing balance re-derived from its own flows). *Sanity checks* confirm the economics are plausible: cash never negative, margins in a believable band, a debt sweep never repaying more than is owed. The integrity checks catch mechanical breaks — dropped links, hard-codes, mis-signs. The sanity checks catch results that are arithmetically valid but economically impossible. I need both because they fail on different things.

**C3. "A model balances perfectly. Are you satisfied it's right?"**

No — balancing is necessary, not sufficient. It only proves the accounting identities hold; a model can balance and still show negative cash, a 120% margin, or a repayment larger than the loan. Those are economic errors, not accounting ones, so they slide past the balance check. I'd also want to confirm the balance is *emergent*, not *plugged* — if any line was forced to make it balance, the check is meaningless. So I look for green integrity checks *and* green sanity checks *and* evidence that nothing was plugged.

**C4. "Why do you insist on separating assumptions from calculations?"**

Because it is what makes the model a decision tool rather than a static spreadsheet. When every assumption lives in one labelled block, I can run scenarios, build sensitivity tables, and hand the model to a client who changes inputs safely — all without touching the machinery. Interleaving assumptions inside formulas buries them where they can't be found, sensitised, or updated, which is exactly how models end up silently running on stale rates. Separation is the precondition for everything downstream: scenarios, audit, and clean handoff.

**C5. "Tell me about a time a check saved you — or would have."**

The pattern I rely on: a colleague overtypes a linked cell with a constant that happens to be right today. Nothing looks wrong, the model balances, the deck goes out. Weeks later an upstream assumption changes, every linked cell updates — except the hard-coded one, which is now stale, and the model quietly reports a wrong number. A cash tie or a rollforward would have fired the instant the constant diverged from its source, before it ever reached a decision-maker. That is why I keep checks even when they've been green for months: their silence is the evidence the model is healthy, and they're the only reason I'll learn about a break before someone acting on the number does.

---

## Section D — Common-Error Spotting

For each, identify the defect and the fix.

**D1.** `=SUM(F10:F14)*0.21` sits in the tax row, black font.

Defect: the 0.21 tax rate is hard-coded inside a formula — invisible, unsensitisable, and un-updatable. Fix: move 0.21 to a labelled blue input cell (say `$C$5`) and write `=SUM(F10:F14)*$C$5`. Now the rate has one visible home and every scenario can reach it.

**D2.** The balance check reads `=IF(F30=F45,"OK","ERROR")`.

Defect: exact equality on floating-point figures will report "ERROR" on a genuinely balanced model whenever residue like `3E-11` appears, training the user to ignore the flag. Fix: `=IF(ABS(F30-F45)<0.001,"OK","ERROR")` — tolerance above noise, below any real error.

**D3.** Equity on the balance sheet is entered as `=Assets-Liabilities`.

Defect: this is a plug — equity is forced to whatever makes the sheet balance, so the balance check becomes `TRUE` by construction and can never fire. Fix: build equity from its own rollforward (opening equity + net income − dividends + issuance), and let the balance *emerge*. If it then doesn't balance, that is the check doing its job.

**D4.** Row 22 is `=F21*1.03`, `=G21*1.03`, `=H21*1.04`, `=I21*1.03` across the columns.

Defect: an inconsistent formula — the `1.04` in one cell breaks the copied pattern and is almost certainly a typo or a buried override. Fix: put the growth rate in an input row and reference it (`=F21*(1+F$5)`), so the row is uniform and any intended change is made in the visible driver, not inside a formula.

**D5.** A check cell reads `=OFFSET(INDIRECT("Sheet2!A1"),0,period)`.

Defect: two volatile, opaque functions — `INDIRECT` builds the reference from text so `Ctrl+[` can't trace it, and `OFFSET` recalculates on every change, slowing the model and hiding dependencies from an auditor. Fix: replace with a direct link or `INDEX(Sheet2!$A:$Z, row, period)` — transparent, traceable, non-volatile.

**D6.** The workbook has a Checks tab with twelve individual flags, but no summary and nothing on the other sheets.

Defect: the checks exist but nobody working on a schedule tab will see them fire. Fix: aggregate the twelve into one master flag (`=AND(range)` or `=COUNTIF(range,FALSE)=0`) and mirror that master cell into the top corner of every tab with conditional formatting turning red on failure. Now a break glares wherever the analyst is working.

**D7.** Cash on the balance sheet is typed as `250` (blue font); the cash flow statement computes ending cash of 300.

Defect: cash is a hard-coded input where it should be a link, and it disagrees with the cash flow statement — the model will balance to the wrong figure or not at all. Fix: `=CF!ending_cash` (green link) and add a cash tie `=ABS(BS_cash − CF_cash)<0.001` so any future divergence fires immediately.

---

*Self-verification note.* Section A covers the WHY of colour coding, input/calc/output separation, one-formula-per-row, hard-code avoidance, redundancy, balance-is-not-sufficiency, plugging, master-flag mirroring, and volatile-function avoidance — nine concept checks. Section B works seven build problems anchored to the reference model, each reproducible cell-for-cell (B3 explicitly restates the model to the 830 variant so the imbalance equals depreciation exactly). Section C gives five interview answers in first person. Section D spots seven concrete defects with fixes. Every question is followed by a full answer; conventions (negative outflows, 0.001 tolerance, colour scheme) are stated once and held throughout.
