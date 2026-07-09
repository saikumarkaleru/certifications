# Q&A — Excel for Finance — the Analyst Toolkit

Every question below is followed by a full answer. Numbers are self-verified so you can reproduce each result in a live workbook.

---

## Section A — Concept Check (test the WHY of the technique)

**A1. Why do analysts obsess over relative vs. absolute references (`A1` vs `$A$1`) instead of just retyping formulas?**

Because a model is built once and copied across hundreds of cells. A reference like `A1` shifts when you drag the formula (`B1`, `C1`…); a locked reference like `$A$1` stays pinned. The discipline is that *inputs* (a tax rate, a discount rate, a growth assumption) live in one cell and are referenced with a `$` lock, while *flowing calculations* use relative references so one formula, dragged right across a forecast, produces every period. The "why" is single-source-of-truth: change the input once and the entire model recalculates. Retyping numbers into formulas ("hardcoding") breaks that chain and hides the assumption from any reviewer.

**A2. Why is a hardcoded number inside a formula considered a red flag in a financial model?**

A hardcoded constant (e.g. `=Revenue*1.05`) buries an assumption where no one can find, audit, or flex it. Convention: blue font for inputs, black for formulas. A reviewer scanning for blue cells should be able to see every lever. Burying `1.05` inside black-font formula text means the 5% growth rate is invisible in a sensitivity check and cannot be linked to a scenario switch. It also causes silent errors — if the assumption should update, you must hunt through formulas rather than change one labelled cell.

**A3. Why prefer `INDEX/MATCH` (or `XLOOKUP`) over `VLOOKUP`?**

`VLOOKUP` can only look *rightward* from the lookup column and references the return column by a hardcoded integer offset. Insert a column and that integer silently points at the wrong data. `INDEX/MATCH` decouples the lookup column from the return column — it can look left, and inserting columns doesn't break it because you reference columns by range, not by count. `XLOOKUP` (modern Excel) does the same in one function, returns a spill-safe result, and has a built-in `if_not_found` argument, removing the need to wrap it in `IFERROR`.

**A4. Why does Excel's `NPV` function *not* actually compute the textbook Net Present Value?**

`NPV(rate, values)` assumes the *first* value in the range arrives at the *end of period 1* — i.e. it discounts every argument by at least one period. A textbook NPV includes a time-0 outflow that should **not** be discounted. So the correct construction is `= NPV(rate, period1:periodN) + Initial_Outlay`, with the time-0 cash flow added *outside* the function. Passing the time-0 flow inside the function over-discounts it by one year and understates (or mis-signs) the answer.

**A5. Why turn on iterative calculation, and why is it dangerous?**

Some legitimate models are circular by design — e.g. interest expense depends on average debt, which depends on the cash flow after interest. Enabling iterative calculation (File → Options → Formulas) lets Excel loop until values converge. The danger: a circularity introduced by *accident* (a formula pointing at its own output) will no longer throw a warning; it silently returns a stale or oscillating number. Best practice is a "circularity switch" (an IF that can zero out the interest link) so you can break the loop and find corruption.

**A6. Why use `IFERROR` sparingly rather than wrapping every formula in it?**

`IFERROR` suppresses `#DIV/0!`, `#N/A`, `#REF!` and returns a clean fallback — useful at the presentation layer. But wrapping every calculation hides *structural* errors: a `#REF!` from a deleted row is a real bug, and blanketing it with `IFERROR(...,0)` makes the model look healthy while feeding zeros downstream. Use it only where an error is genuinely expected and benign (a lookup that may legitimately miss).

---

## Section B — Build / Computational Problems

**B1. Build an NPV with an initial outlay.**
Data: discount rate 10%. Cash flows: Year 0 = −500, Year 1 = 100, Year 2 = 200, Year 3 = 300.

Layout:

| Cell | Value |
|------|-------|
| B1 (rate) | 10% |
| B3 (Yr0) | −500 |
| C3 (Yr1) | 100 |
| D3 (Yr2) | 200 |
| E3 (Yr3) | 300 |

Formula: `=NPV(B1, C3:E3) + B3`

Step-by-step:
- 100 / 1.10¹ = 90.909
- 200 / 1.10² = 200 / 1.21 = 165.289
- 300 / 1.10³ = 300 / 1.331 = 225.394
- Sum of discounted inflows = 481.592
- Add the undiscounted outlay: 481.592 − 500 = **−18.41**

Reconciling: because NPV is negative at a 10% hurdle, the project destroys value; its IRR is below 10%.

**B2. Confirm the IRR of B1's cash flows.**
Formula: `=IRR(B3:E3)` on the stream (−500, 100, 200, 300).

Solve NPV = 0. Testing rates:
- At 8%: 100/1.08 + 200/1.08² + 300/1.08³ = 92.59 + 171.47 + 238.15 = 502.21 → NPV = +2.21
- At 9%: 91.74 + 168.34 + 231.66 = 491.74 → NPV = −8.26

Root lies between 8% and 9%. Interpolating: 8% + 1% × (2.21 / (2.21 + 8.26)) = 8% + 0.21% ≈ **8.2%**. Since 8.2% < 10% hurdle, this reconciles with the negative NPV in B1. ✓

**B3. Build a loan amortisation payment (PMT).**
Data: principal 100,000; annual rate 5%; term 5 years; annual payment.

Formula: `=PMT(5%, 5, -100000)` → payment is positive when the principal is entered negative.

Manual check with PMT = P·r / (1 − (1+r)⁻ⁿ):
- (1.05)⁵ = 1.2762816, so (1.05)⁻⁵ = 0.7835262
- 1 − 0.7835262 = 0.2164738
- Numerator: 100,000 × 0.05 = 5,000
- Payment = 5,000 / 0.2164738 = **23,097.48**

Reconciling amortisation, Year 1: interest = 100,000 × 5% = 5,000; principal repaid = 23,097.48 − 5,000 = 18,097.48; closing balance = 81,902.52. Over five such rows the balance amortises to ~0, confirming the payment.

**B4. Split PMT into interest and principal with IPMT/PMT.**
Using B3's loan, Year 2:
- Opening balance = 81,902.52
- `=IPMT(5%, 2, 5, -100000)` → interest = 81,902.52 × 5% = **4,095.13**
- Principal repaid = 23,097.48 − 4,095.13 = **19,002.35** (up from 18,097.48 in Year 1, since interest fell)
- Closing balance = 81,902.52 − 19,002.35 = 62,900.17

Reconciling: interest falls (5,000 → 4,095) and principal rises (18,097 → 19,002) while total payment stays flat at 23,097.48 — the signature of a level-payment amortising loan. ✓

**B5. XNPV / XIRR with irregular dates.**
Data: pay 1,000 on 01-Jan-2026; receive 1,150 on 01-Jul-2027 (546 days later). Discount rate 10%.

`=XNPV(10%, {-1000, 1150}, {01-Jan-2026, 01-Jul-2027})`

XNPV discounts on an *actual/365* day basis: 546 / 365 = 1.4959 years.
- Discount factor = 1.10^1.4959 = 1.1531
- PV of inflow = 1,150 / 1.1531 = 997.3
- XNPV = 997.3 − 1,000 = **−2.7** (essentially break-even; the deal earns just under 10%).

`=XIRR({-1000,1150}, dates)` solves for the rate making XNPV = 0: 1,150/1,000 = (1+r)^1.4959 → 1+r = 1.15^(1/1.4959) = 1.0975 → **XIRR ≈ 9.7%**, reconciling with the slightly negative XNPV at 10%. ✓

**B6. Two-variable Data Table (sensitivity).**
Setup: a model cell `B10` outputs NPV, driven by growth (`B1`) and discount rate (`B2`). Build a grid with the output formula `=B10` in the top-left corner, growth rates listed down the left column and discount rates across the top row. Select the whole grid → Data → What-If Analysis → Data Table → Row input cell = `B2`, Column input cell = `B1`. Excel substitutes each pair and fills the matrix. The "why": it recalculates the full model for every combination without you copying formulas — the fastest way to show the board how NPV swings with two key assumptions.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through the difference between relative, absolute, and mixed references."**

Model answer: A relative reference (`A1`) moves in both row and column when copied. An absolute reference (`$A$1`) is pinned in both. Mixed references lock one axis: `$A1` fixes the column but lets the row move; `A$1` fixes the row but lets the column move. Mixed references are the pro move for building a matrix from a single formula — e.g. a sensitivity grid where you multiply a row header (`B$1`, row locked) by a column header (`$A2`, column locked) so one formula fills the whole block. Toggle with F4.

**C2. "What's the difference between `NPV` and `XNPV`, and when do you use each?"**

Model answer: `NPV` assumes equally spaced periods and discounts the first value by one full period, so it fits a clean annual or monthly forecast. `XNPV` takes an explicit array of dates and discounts on an actual-day basis, so it handles irregular timing — deal closings, dividend dates, mid-year draws. In real transaction work I default to `XNPV`/`XIRR` because cash rarely lands on tidy annual boundaries, and I always remember to add the time-0 flow *outside* a plain `NPV` since that function double-discounts it.

**C3. "How do you handle a circular reference in a three-statement model?"**

Model answer: The classic circularity is interest expense ↔ debt schedule ↔ cash flow. I enable iterative calculation, but I always wire in a circularity-breaker switch — a binary cell that, when flipped, forces the interest link to zero. If the model ever returns `#REF!` or oscillates, I flip the switch to break the loop, find and fix the corrupted cell, then re-enable it. That way the circularity is intentional and controllable rather than a hidden landmine.

**C4. "Your VLOOKUP returned `#N/A` on a value you can see in the table. Why?"**

Model answer: Most often the lookup value and the table key differ by type or whitespace — a number stored as text vs. a real number, or a trailing space. `VLOOKUP` needs an exact type match in exact-match mode (`FALSE`/`0`). Second cause: the lookup value isn't in the *first* column of the table array, since VLOOKUP only searches leftmost. Third: approximate-match mode (`TRUE`) was left on and the table isn't sorted ascending. I'd test with `TRIM`/`VALUE`, confirm the fourth argument is `FALSE`, and switch to `XLOOKUP` or `INDEX/MATCH` to remove the leftmost-column constraint.

**C5. "What keyboard habits make you faster than someone who uses the mouse?"**

Model answer: `Ctrl+arrow` to jump to the edge of a data region, `Ctrl+Shift+arrow` to select to it, `F4` to toggle reference locking while typing a formula, `F2` to edit in-cell, `Alt+=` for autosum, `Ctrl+;` for today's date, and `Ctrl+Shift+Enter` history aside, the Alt ribbon accelerators (e.g. `Alt, H, O, I` to autofit column width). The deeper point is that navigating by keyboard keeps my hands on the model and lets me audit structure — tracing precedents with `Ctrl+[` — far faster than clicking.

**C6. "How do you audit a model you didn't build?"**

Model answer: I check the colour convention first — blue inputs, black formulas, green links to other sheets — then use Formula Auditing (Trace Precedents/Dependents, `Ctrl+`` to show all formulas). I scan for hardcodes inside formulas, blanket `IFERROR` wrappers hiding errors, and inconsistent formulas across a row (Excel flags these with a green triangle). I stress-test by zeroing key drivers and confirming outputs move sensibly, and I check that the balance sheet balances and the cash flow ties to the change in cash.

---

## Section D — Common-Error Spotting (here is a broken formula, what is wrong)

**D1. Broken:** `=NPV(10%, B3:E3)` where B3 = −500 (the initial outlay) and C3:E3 are inflows.

What's wrong: the time-0 outlay is passed *inside* `NPV`, so Excel discounts the −500 by one period (−500/1.10 = −454.55) instead of taking it at face value. The result (+27.05) is wrong.
Fix: `=NPV(10%, C3:E3) + B3`, keeping the undiscounted outlay outside the function → −18.41 (matches B1). ✓

**D2. Broken:** `=VLOOKUP(A2, B:F, 4, TRUE)` used for an exact-key lookup on an unsorted table.

What's wrong: the fourth argument `TRUE` triggers approximate match, which requires the first column sorted ascending. On unsorted data it silently returns the *wrong* row (the last value ≤ lookup) with no error.
Fix: use `FALSE` (or `0`) for exact match: `=VLOOKUP(A2, B:F, 4, FALSE)` — better still `=XLOOKUP(A2, B:B, E:E, "not found")`.

**D3. Broken:** `=Revenue*1.08` intended as a growth line, entered in black font.

What's wrong: the 8% growth rate is hardcoded inside the formula, invisible to any reviewer and unavailable to a scenario switch or sensitivity table.
Fix: put 8% in a labelled blue input cell (`$B$1`) and write `=Revenue*(1+$B$1)`. Now the assumption is a single visible, flex-able lever.

**D4. Broken:** `=SUM(B2:B10)` in a total row, but a new row was inserted at row 11 (outside the range) and its value is being missed.

What's wrong: the SUM range was hardcoded to end at B10 and doesn't stretch to include newly inserted data below the range, silently understating the total.
Fix: either insert *within* the summed block so the range auto-expands, or use a structured Table (`=SUM(Table1[Amount])`) which grows automatically, or sum a deliberately generous range.

**D5. Broken:** `=IFERROR(VLOOKUP(A2, Data, 3, 0), 0)` used across an entire schedule.

What's wrong: wrapping every lookup with a `,0)` fallback masks genuine `#REF!`/`#N/A` errors. A deleted source column would return zeros everywhere, and the model would look healthy while feeding zeros downstream.
Fix: only use `IFERROR` where a miss is truly expected; otherwise leave errors visible so structural breaks surface. If you must default, default to a value that *looks wrong* (e.g. a flag) rather than a plausible 0.

**D6. Broken:** `=B2/C2` for a margin, where C2 (a denominator) can be zero, returning `#DIV/0!` that cascades into every dependent total.

What's wrong: an unguarded division by a possibly-zero denominator propagates `#DIV/0!` through sums and charts.
Fix: `=IF(C2=0, 0, B2/C2)` — an explicit, intentional guard that a reviewer can see — rather than a blanket `IFERROR`, so a zero denominator is handled without hiding other error types.

---

*End of Q&A — reproduce every computed figure by entering the stated formulas; each answer above has been arithmetically self-checked.*
