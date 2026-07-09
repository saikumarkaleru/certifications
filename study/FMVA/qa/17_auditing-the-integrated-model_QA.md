# Q&A — Auditing and Error-Checking the Model

Practice bank for Chapter 17. Work each question before reading the answer. The idea running through it: compute a quantity two independent ways and demand the difference be zero within tolerance. Every number is anchored to one reusable mini-model so you can reproduce each check cell-for-cell and watch the flag flip green to red.

**The reference mini-model (every B problem uses it).** One-period forecast. Openings: cash 100, PP&E 500, retained earnings 300, share capital 200, debt 100. Flows: revenue 1,000; cash operating costs 700; depreciation 50; capex 80; dividends 20; tax and interest 0.

Correctly built: net income = 1,000 − 700 − 50 = **250**; cash flow = 250 + 50 − 80 − 20 = **+200** → ending cash = **300**; closing PP&E = 500 + 80 − 50 = **530**; closing RE = 300 + 250 − 20 = **530**. Balance sheet: assets 300 + 530 = **830**; liabilities + equity 100 + 200 + 530 = **830**. It balances.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is "redundancy" the single principle underneath every check in a model?**

Because a lone number cannot be verified against itself — only against a *second, independent* route to the same answer. If two computations agree, the logic between them is almost certainly sound; if they disagree, you have caught an error for free. Every check is an instance: the balance sheet is assets one way versus claims-on-assets another; the cash tie is cash built bottom-up on the cash flow statement versus cash sitting as a line item; a rollforward is a balance re-derived from its own flows versus the balance actually posted. No redundancy, no test.

**A2. Why does the balance check catch errors almost anywhere in the model, not just on the balance sheet?**

Because the balance sheet sits downstream of everything: retained earnings pulls from net income, cash from the cash flow statement, PP&E from the capex and depreciation schedules, debt from the financing schedule. A break anywhere upstream — a dropped add-back, a mis-signed dividend, a hard-code over a link — distorts one side of the equation but not the other, so the difference goes non-zero. One subtraction surveils dozens of schedules at once — the leverage that makes it the king of checks.

**A3. A model balances perfectly in every period. Can you conclude it is correct?**

No. Balancing proves the accounting identities hold, but a model can honour Assets = Liabilities + Equity while being economically absurd — negative cash, a debt sweep that repays more than is owed and drives debt negative, gross margin above 100%. These violate reality, not accounting, so they slip past the balance check. That is why sanity checks exist alongside integrity checks: the two families catch *different* error classes.

**A4. Why is "plugging" the balance sheet the cardinal sin of error-checking?**

Because it converts your best error *detector* into an error *concealer*. Force one line (equity, cash, a "plug" row) to equal whatever makes the sheet balance, and the balance check becomes `TRUE` by construction and can never fire again — you have wired the smoke detector to the light switch. Balance must *emerge* from every line being built honestly, never be *imposed*. A plug guarantees balance and destroys the only reason balance was worth anything.

**A5. Why must checks compare `ABS(difference) < tolerance` rather than `difference = 0`?**

Because floating-point arithmetic leaves tiny residue — a genuinely balanced model routinely shows something like `4.5E-11` instead of a clean zero. A `= 0` test then returns `FALSE` and cries wolf on a correct model, training you to ignore the flag. Wrapping the difference in `ABS(...)` and comparing to a small tolerance (say 0.001 for dollar figures) passes true balance while still catching any real imbalance. The tolerance must sit just above floating-point noise and well below any error that would matter.

**A6. Why put a status banner on *every* tab instead of just on the Checks tab?**

Because a check nobody looks at is useless, and an analyst racing a deadline lives on the schedule tabs, not the back-of-workbook Checks tab. Linking the master status into a top corner of every sheet (`='Checks'!$B$1`, conditionally formatted red on failure) means a broken model glares at you wherever you are working — the difference between a reviewer-friendly deliverable and a landmine that balances today and silently breaks the moment someone edits a link.

**A7. Why is a check that has never once failed still worth keeping?**

Because it is a smoke detector, not a nuisance. Its silence is not evidence it is redundant — it is evidence the model is healthy. The instant a future edit (by a colleague, or by you in six months) breaks the thing it guards, it is the only reason you will find out before a decision-maker does. Deleting checks to "tidy up" because "they're always green" removes the safety exactly when handoff risk is highest. Checks are structural, not decorative.

---

## Section B — Build / Computational Problems

Convention: outflows (capex, dividends, repayments) are stored **negative**; every check returns `TRUE` when the model is healthy.

**B1. The balance check on the reference model.** Total assets are in cell `F40`, total liabilities-plus-equity in `F60`. Write the raw difference, the tolerance-wrapped flag, and confirm the value.

Raw difference: `=F40-F60` → 830 − 830 = **0.0**.
Tolerance flag: `=ABS(F40-F60)<0.001` → `ABS(0) < 0.001` → **TRUE**.
Across a full horizon `F:K` the per-period flags live in row 62 and you roll them up with `=AND(F62:K62)` → **TRUE** only if every period balances. The model passes.

**B2. The dropped depreciation add-back.** Someone deletes the depreciation add-back row in the cash flow statement. Recompute cash, the new balance sheet, and the balance check. Show that the imbalance equals a number you can name.

Cash flow becomes NI 250 − capex 80 − dividends 20 = **+150**; ending cash = 100 + 150 = **250**. Depreciation still correctly reduces PP&E (530) and still sits inside net income → RE (530); only the cash side lost the add-back.

| Assets | | Liab + Equity | |
|---|---:|---|---:|
| Cash | 250 | Debt | 100 |
| PP&E | 530 | Share capital | 200 |
| | | Retained earnings | 530 |
| **Total** | **780** | **Total** | **830** |

Check: `=ABS(780-830)<0.001` → `ABS(−50) < 0.001` → **FALSE**. The imbalance is exactly **50** — the depreciation figure. The check not only fires, it hands you the magnitude, pointing straight at the depreciation line. Reproduce in Excel and watch the flag turn red.

**B3. The cash-flow tie catches a hard-code.** Starting from the correct model (balanced at 830), a colleague overtypes the balance-sheet cash cell — properly linked `=CF!ending_cash` (300) — with the constant `310`. Build both the balance check and the CF tie, and explain which localises the error.

Assets = 310 + 530 = 840; L+E still 830. Balance check: `=ABS(840-830)<0.001` → **FALSE** (off by 10). That tells you *something* is wrong but not *where*.
CF tie: `=ABS(310-300)<0.001` → `ABS(10) < 0.001` → **FALSE**. Every other check (RE rollforward, PP&E rollforward, debt sweep) stays **TRUE**. Two red flags, both pointing at cash → you go straight to the cash line, `Ctrl+[` to trace precedents, find a constant where a link belongs, restore `=CF!ending_cash`. Under a minute.

**B4. The over-aggressive debt sweep (sanity, not integrity).** A cash sweep repays debt: intended `Repayment = MIN(available_cash, opening_debt)`. Opening debt 100, available cash for sweep 140. The analyst writes `=available_cash`, dropping the `MIN`. Compute closing debt, test the balance check, then the sanity check.

Correct repayment = `MIN(140,100)` = 100 → closing debt 0. The error gives repayment 140 → closing debt = 100 − 140 = **−40**.
Balance check: the −40 debt cuts liabilities by 40, but paying out 40 more cash than intended cuts cash assets by the same 40. Both sides fall 40; the equation still holds → **TRUE**. The balance check is *blind* here.
Sanity check: `=AND(closing_debt>=0, repayment<=opening_debt)` → `AND(−40>=0, 140<=100)` → `AND(FALSE,FALSE)` → **FALSE**. Caught. This is the proof that integrity and sanity checks catch different error classes.

**B5. The retained-earnings rollforward.** The balance sheet posts closing RE of 510. Prior RE 300, net income 250, dividends 20. Write the rollforward check and give its verdict.

`=ABS(RE - (RE_prior + NI - Dividends)) < 0.001` → `ABS(510 - (300 + 250 - 20))` = `ABS(510 - 530)` = **20** → the flag is **FALSE**. The correct RE is 530; the posted 510 is short by exactly the 20 of dividends double-counted (or a dropped slice of net income). Because this check re-derives one balance-sheet line from its own logic, it localises the break to retained earnings without touching the rest of the sheet.

**B6. Aggregating into a master flag.** Your Pass column `B4:B11` holds eight boolean flags. In one run they read: `TRUE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE`. Write the failure count and the status text, and give both values.

Failure count: `=COUNTIF(B4:B11, FALSE)` → there are two `FALSE` cells → **2**.
Status: `=IF(COUNTIF(B4:B11,FALSE)=0, "MODEL OK", "ERROR — "&COUNTIF(B4:B11,FALSE)&" CHECKS FAILED")` → **"ERROR — 2 CHECKS FAILED"**. A healthy model would show `0` and "MODEL OK". Note `COUNTIF` targets the boolean `FALSE`, not the text `"FALSE"` — see D6.

**B7. The cash-movement tie (the deeper cash check).** Balance-sheet cash this period 300, prior period 100; the cash flow statement's net change in cash is 200. Write the movement tie and confirm it. Then explain what it catches that the plain CF tie cannot.

`=ABS((BS_Cash - BS_Cash_prior) - CF_NetChange) < 0.001` → `ABS((300 − 100) − 200)` = `ABS(0)` = **TRUE**. The plain CF tie compares two cells that may both link to the same ending-cash number, so it can be `TRUE` even when the *components* inside the cash flow build are wrong but happen to sum to a forced ending balance. The movement tie re-derives the change from balance-sheet deltas, catching a cash flow statement whose internals are broken even though its total was plugged.

**B8. Tolerance calibration.** A correct model shows a balance difference of `0.0000001`. (a) What does `=F40-F60=0` return? (b) What does `=ABS(F40-F60)<0.001` return? (c) Why is a tolerance of `1000` on a model built in thousands dangerous?

(a) `0.0000001 = 0` is **FALSE** — the check cries wolf on a genuinely balanced model, the classic floating-point false alarm. (b) `ABS(0.0000001) < 0.001` is **TRUE** — correct. (c) A tolerance of 1,000 on figures already in thousands means the check ignores any imbalance up to 1,000 units — i.e. up to $1,000,000 of real error in a thousands-denominated model. The tolerance must sit just above floating-point noise, never above a mistake that matters.

**B9. Multi-period roll-up.** Per-period balance flags for 2025–2029 sit in `F62:J62` and read `TRUE, TRUE, TRUE, FALSE, TRUE`. Write the single master cell and give its value; state what the pattern usually signals.

`=AND(F62:J62)` → because one cell is `FALSE`, the result is **FALSE**. A model that balances every year except one (or that goes red only in a downside scenario) almost always has a `MIN`/`MAX`/`IF` that switches branches at an extreme — a debt sweep that empties debt, a revolver that draws, a floor that binds. The single red period tells you exactly which column to interrogate.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "How do you know a three-statement model is right without checking every cell?"**

I never eyeball 4,000 cells — I exploit redundancy. The headline is the balance check: total assets minus total liabilities-plus-equity, wrapped in `ABS(...) < tolerance`, in every period. Because the balance sheet is downstream of every statement and schedule, that one subtraction surveils the whole model — any broken link makes it go non-zero. On top I run the cash-flow tie, the cash-movement reconciliation, rollforward checks on RE, PP&E and debt, plus sanity checks for non-negative cash and a well-behaved sweep. Everything rolls into one master flag that reads "MODEL OK" or counts failures, banner-linked to every tab. A green banner is continuously evaluated proof; a red one tells me something broke the instant it broke.

**C2. "Why should you never force the balance sheet to balance?"**

Because balancing is the most powerful correctness signal in the model, and forcing it throws that signal away. If I set one line — equity, cash, a plug row — equal to whatever makes assets equal claims, the sheet balances no matter how wrong everything upstream is: I have turned my best error detector into a machine that hides errors. The discipline is that every line is built from its own honest schedule and balance *emerges* from double-entry being respected everywhere. When it emerges, its holding is real evidence; when imposed, it means nothing.

**C3. "A model balances perfectly. What could still be wrong?"**

Plenty — balancing only proves the accounting identities hold, not that the model is economically sane. Cash could be negative, meaning a revolver draw I never modelled. A debt sweep could repay more than is outstanding and drive debt negative, which balances (cash out and debt down move together) yet is nonsense. Gross margin could exceed 100%, depreciation could exceed net book value. None of these violate Assets = Liabilities + Equity, so the balance check stays green. That is why I layer sanity checks on top: domain constraints — nothing negative that shouldn't be, nothing unbounded that should be bounded, every rollforward reconciling. Integrity and sanity catch different error classes.

**C4. "Your balance sheet is off by exactly 50 in 2027 only. Walk me through finding it."**

First I read the other checks, because magnitude and pattern are clues. Off by 50 in one period, with the RE and PP&E rollforwards telling me which line disagrees, usually localises it fast — a 50 matching my depreciation figure points at the depreciation add-back or link. If the rollforwards are green but cash is off, I suspect a hard-code and run Go To Special ▸ Constants to reveal any number pasted over a formula. Then I select the failing cell and use `Ctrl+[` to jump to its precedents across sheets, or Trace Precedents, walking backward from the symptom. For a nested formula I use Evaluate Formula, or select a sub-expression in the formula bar and press `F9` to see which term returns garbage (then `Esc`, never `Enter`). The dependency graph turns a needle-in-a-haystack into a guided binary search — minutes, not hours.

**C5. "What's the difference between an integrity check and a sanity check?"**

An integrity check verifies an accounting identity — the balance sheet balances, ending cash ties, the movement reconciles. These hold *by double-entry* if the model is wired correctly, so a failure means a broken link, dropped row, sign flip or hard-code. A sanity check verifies economic reality — non-negative cash and debt, a sweep no larger than the balance owed, bounded margins, depreciation within net book value. These hold *by the real world*, not accounting, so a model can pass every integrity check and still fail a sanity one. Integrity catches wiring errors, sanity catches absurd-but-consistent states; a robust model carries both, plus the rollforward checks that sit between them.

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Testing equality to zero.**
```
Balance check (F):  =F40-F60=0
```
**Wrong:** floating-point residue means a truly balanced model shows something like `4.5E-11`, so `=0` returns `FALSE` and the check cries wolf. Fix: `=ABS(F40-F60)<0.001` — wrap in `ABS` and compare to a small tolerance that clears floating-point noise but sits well below any real error.

**D2. Plugging the balance sheet.**
```
Equity = Total_Assets - Other_Liabilities   ' forced so the sheet always balances
```
**Wrong:** one line is forced to whatever makes assets equal claims, so the balance check is `TRUE` by construction and can never catch anything again. Fix: build equity (and every line) from its own honest schedule — retained earnings from the RE rollforward, share capital from the equity schedule — and let balance emerge. Never impose it.

**D3. Blanket `IFERROR` hiding real errors.**
```
=IFERROR( <entire schedule formula> , 0)
```
**Wrong:** wrapping whole schedules in `IFERROR(...,0)` makes `#DIV/0!` and `#REF!` vanish — but those errors are information, often the exact symptom you need. The model looks clean while silently zeroing broken cells. Fix: use `IFERROR` only where a benign error is genuinely expected (e.g. a ratio in period zero). A visible error is a gift; fix the cause, don't gag the symptom.

**D4. A cash tie that can't catch a build error.**
```
BS_cash = CF!ending_cash               ' link
CF tie  = ABS(CF!ending_cash - BS_cash) < 0.001
```
**Wrong (partially):** because the balance-sheet cash *is* the same link, the CF tie is `TRUE` by construction and — while it will still catch someone later overtyping the link with a constant (its real purpose as a tripwire) — it cannot catch an error *inside* the cash flow statement's own build. Fix: pair it with the cash-*movement* tie, `=ABS((BS_Cash - BS_Cash_prior) - CF_NetChange) < 0.001`, which re-derives the change from balance deltas and catches broken CF internals.

**D5. Tolerance set larger than real errors.**
```
=ABS(F40-F60) < 1000        ' model is denominated in thousands
```
**Wrong:** on a thousands-denominated model this ignores any imbalance up to 1,000 units — up to $1,000,000 of real error. Fix: set the tolerance just above floating-point noise (0.001 for dollar figures; scale to your units), never above a mistake that would matter.

**D6. `COUNTIF` matching the wrong kind of FALSE.**
```
=COUNTIF(B4:B11, "FALSE")    ' checks return boolean FALSE, not text
```
**Wrong:** the checks return the boolean value `FALSE`, but `"FALSE"` in quotes matches the *text string* "FALSE" — so a column of genuine boolean failures counts as **0** and the model reads healthy while broken. Fix: `=COUNTIF(B4:B11, FALSE)` with no quotes (or count with `=SUMPRODUCT(--(B4:B11=FALSE))`). Confirm the flags are true booleans, not text.

**D7. Status flag only on the back tab.**
```
Checks!B1 = "ERROR — 2 CHECKS FAILED"    ' lives only on the Checks tab
```
**Wrong:** an analyst working on the model tabs never sees it, so a broken model ships. Fix: link the master status into a top-corner cell of *every* sheet — `='Checks'!$B$1` — and conditionally format it red when it contains "ERROR". A broken model must glare from whatever tab you are on.

**D8. `SUM` that silently drops a row.**
```
Total assets:  =SUM(F5:F10)     ' a new asset line was inserted in F11
```
**Wrong:** the inserted line sits just outside the range, so the total under-counts and the balance check fails for a reason unrelated to any logic error. Fix: rebuild the total to include the new row (`=SUM(F5:F11)`), heed Excel's green-triangle "formula omits adjacent cells" warning, run Formulas ▸ Error Checking to sweep for others, and build totals with a spare buffer row or structured references so future inserts are captured automatically.
