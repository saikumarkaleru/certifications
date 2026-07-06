# Q&A — The Debt and Interest Schedule (and Circularity)

Practice bank for Chapter 13. Work each question before reading the answer. This chapter has two engines: a **roll-forward** (Ending = Beginning + Draws − Repayments) that any student of the PP&E schedule already recognises, and a genuine **economic loop** — interest → net income → cash → debt paydown → interest — that you must learn to *control* rather than delete. Every number below is built so you can reproduce it cell-for-cell in Excel and watch it tie, including a full manual iteration that converges to the penny.

---

## Section A — Concept Checks (test the WHY)

**A1. Why does a debt schedule exist at all — why not just type the debt balance onto the balance sheet each year?**

Because a balance is not an independent fact; it is the accumulated history of every draw and every repayment. Debt today equals last year's debt plus what you borrowed minus what you repaid. Typing a number onto the balance sheet directly severs it from that history, so a change to a repayment assumption three years earlier would not move it, and the model quietly stops articulating. The schedule is the one authoritative place where the roll-forward lives; the balance sheet merely *links* to its closing line. That single-source-of-truth discipline is also what lets the balance sheet act as a lie detector — if the debt line is wrong, the sheet stops balancing.

**A2. Why is interest expense computed on a *balance*, and why does the choice of *which* balance matter so much?**

Interest is a price charged on borrowed money, so it must be rate times the amount owed — a balance, not a flow. The subtlety is *when* you measure that balance. The company did not owe the beginning amount all year (it amortised), nor the ending amount all year (it started higher). On average it owed `(Beginning + Ending) / 2`, so the average is the honest convention. But that choice reaches *forward* into the ending balance, which is downstream of this year's cash and therefore of this year's interest — and that is exactly what creates the circular reference. The beginning balance, by contrast, is a settled fact inherited from last year, so pricing it forms no loop.

**A3. Why is the interest loop economically *correct* rather than a modelling mistake?**

Because it faithfully describes a real business. A company's borrowing cost depends on how much it owes; how much it owes depends on how much cash it had to pay debt down; how much cash it had depends on its profit; and its profit depends on its borrowing cost. That is a true causal cycle in the world, not an Excel artefact. Deleting the loop (say, by hardcoding interest) would make the model *less* truthful. The right response is to let the loop exist and resolve it by iteration, because the economics guarantee it converges — each pass changes interest by a smaller amount than the last.

**A4. Why does iteration actually converge instead of spiralling?**

Because interest is only a few percent of a balance that is itself only mildly sensitive to interest. When you feed a slightly-too-high interest guess through the loop, it lowers net income a little, lowers cash a little, leaves debt a touch higher, and raises the next interest estimate — but by far less than the original error, because the rate is small. The feedback is damping, not amplifying. Successive passes therefore shrink the gap geometrically until the change falls below Excel's tolerance (e.g. 0.001), at which point the numbers are stable to the penny.

**A5. Why must every repayment line be wrapped in `MIN(..., Beginning balance)`?**

Because you cannot repay principal you no longer owe. In the final years of an amortising loan the scheduled instalment can exceed the remaining balance; without a cap the roll-forward subtracts more than exists and the ending balance goes *negative* — an impossible state that silently corrupts the balance sheet and the interest calculation. `MIN(scheduled, beginning)` repays the lesser of what is due and what is left, so the balance lands cleanly at zero and stays there.

**A6. Why does the revolver make the model self-balancing, and why is it driven off the cash-flow *before financing*?**

The revolver is a shock absorber with two mirror jobs: draw when cash would otherwise fall below the minimum, repay when there is surplus. To know which, you compute the cash position after operations, investing, and every *non-revolver* financing flow — the "cash available before revolver." If that is below the minimum, the revolver draws exactly enough to restore the floor; if it is above, the revolver repays up to what is drawn. Because the draw is sized to whatever gap exists, the cash line can never go impossibly negative — the model closes its own cash hole automatically.

**A7. Why is interest expense placed on the income statement but *not* in the financing section of the cash flow statement?**

Because interest already did its work at the top of the cash flow statement: it reduced net income, which is the starting line of cash flow from operations. Repeating it as a financing outflow would count the same cash leaving twice. Only *principal* movements — draws and repayments — belong in financing, because those are the cash events that never touched the income statement. Interest is an operating cost of borrowing; principal is a financing transaction.

---

## Section B — Build / Computational Problems

Convention for all builds: draws are stored **positive**, repayments **negative**, and the closing line is a literal `=SUM(Beginning, Draws, Mandatory, Optional)` so the roll-forward reads itself.

**B1. Amortising term loan with beginning-balance interest (no circularity).** A term loan opens at **1,200**. Mandatory amortisation is **300 per year**, interest is **6%** charged on the *beginning* balance, no draws or sweep. Build four years.

| Line | Y1 | Y2 | Y3 | Y4 |
|---|---:|---:|---:|---:|
| Beginning balance | 1,200 | 900 | 600 | 300 |
| (−) Mandatory repayment | (300) | (300) | (300) | (300) |
| **Ending balance** | **900** | **600** | **300** | **0** |
| Interest @ 6% × Beginning | 72.0 | 54.0 | 36.0 | 18.0 |

Verify the corkscrew: 1,200 − 300 = 900 → becomes Y2 beginning; 900 − 300 = 600 → Y3 beginning; 600 − 300 = 300 → Y4 beginning; 300 − 300 = 0. Interest keys off beginning only (72, 54, 36, 18), so it never touches the ending balance and no loop forms. Total interest over the life = 72 + 54 + 36 + 18 = **180**.

**B2. Same loan on the average balance.** Re-run B1 with interest = 6% × average balance. Because there is no sweep, the ending balances are still fixed by the mandatory schedule, so we can read the averages directly and measure what the convention costs.

| Line | Y1 | Y2 | Y3 | Y4 |
|---|---:|---:|---:|---:|
| Beginning | 1,200 | 900 | 600 | 300 |
| Ending | 900 | 600 | 300 | 0 |
| Average = (Beg+End)/2 | 1,050 | 750 | 450 | 150 |
| Interest @ 6% × Average | 63.0 | 45.0 | 27.0 | 9.0 |

Each year the average charge is exactly **9 less** than the beginning-balance charge (72 vs 63, 54 vs 45, 36 vs 27, 18 vs 9) — and 9 = 6% × 150, six percent of half the annual 300 amortisation. Total average-balance interest = 63 + 45 + 27 + 9 = **144**, versus 180 on the beginning balance — a **36** difference over the life. Neither is wrong; they are different conventions, and this is the material gap the choice creates on a declining balance.

**B3. The `MIN` cap in the final year.** A loan opens at **500** with a scheduled mandatory instalment of **200 per year**. Show why the repayment needs a `MIN` cap.

| Line | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Beginning | 500 | 300 | 100 |
| Scheduled instalment | 200 | 200 | 200 |
| (−) Mandatory = MIN(sched, Beg) | (200) | (200) | (100) |
| **Ending** | **300** | **100** | **0** |

In Y3 the scheduled 200 exceeds the remaining 100, so `MIN(200, 100) = 100` repays only what is owed and the balance lands at zero. Without the cap, Y3 would subtract the full 200 and produce an ending balance of **−100** — the loan "repaying" principal that no longer exists, which then feeds a nonsensical negative average and poisons the interest line.

**B4. Revolver as a cash-flow shock absorber.** Minimum cash required **100**, opening cash **100**, opening revolver **0**. Cash flow *before financing*: Y1 **−60** (shortfall), Y2 **+200** (surplus), Y3 **+40** (surplus). Build the revolver roll-forward and the cash line.

| Line | Y1 | Y2 | Y3 |
|---|---:|---:|---:|
| Beginning revolver | 0 | 60 | 0 |
| Cash avail. before revolver | (60) | 200 | 180 |
| Draw = MAX(0, −avail) | 60 | 0 | 0 |
| Repay = −MIN(Beg, MAX(0,avail)) | 0 | (60) | 0 |
| **Ending revolver** | **60** | **0** | **0** |
| Ending cash | 100 | 240 | 280 |

Y1: cash available = 100 opening + (−60) − 100 minimum = **−60** → shortfall → draw MAX(0, 60) = 60; ending cash = 100 − 60 + 60 = 100, restored exactly to the floor. Y2: available = 100 + 200 − 100 = **200** → surplus → repay MIN(beginning 60, 200) = 60, so ending revolver = 0; ending cash = 100 + 200 − 60 = 240. Y3: available = 240 + 40 − 100 = **180** surplus but the revolver is already 0, so repay MIN(0, 180) = 0; cash simply builds to 280. The revolver drew just enough to hold the floor, then fully repaid — the self-balancing behaviour that keeps cash from ever going impossibly negative.

**B5. Term-loan cash sweep.** Term loan opens at **1,000**, mandatory **100 per year**, interest **7%** on the beginning balance (kept acyclic). A cash sweep applies **50%** of surplus cash available for prepayment (after operations, investing, mandatory amortisation and interest, holding the minimum cash): surplus is **300** in Y1 and **400** in Y2. Build two years.

| Line | Y1 | Y2 |
|---|---:|---:|
| Beginning | 1,000 | 750 |
| (−) Mandatory = MIN(100, Beg) | (100) | (100) |
| Remaining after mandatory | 900 | 650 |
| (−) Sweep = −MIN(remaining, 50%×surplus) | (150) | (200) |
| **Ending** | **750** | **450** |
| Interest @ 7% × Beginning | 70.0 | 52.5 |

Y1: sweep = MIN(900, 50% × 300) = MIN(900, 150) = **150**; ending = 1,000 − 100 − 150 = **750**. Y2: mandatory = MIN(100, 750) = 100, remaining 650; sweep = MIN(650, 50% × 400) = MIN(650, 200) = **200**; ending = 750 − 100 − 200 = **450**. The sweep accelerates paydown beyond the contractual 100, and the `MIN` against the remaining balance guarantees it can never over-repay.

**B6. Controlled circularity — iterate the loop to convergence.** A company has EBIT **500** and a **25%** tax rate. Debt opens at **1,000**, rate **10%**, interest on the **average** balance. All free cash flow after interest and tax sweeps the debt; assume free cash flow equals net income (no D&A, capex or working-capital movement). So `Ending = 1,000 − Net income`, `Interest = 10% × (1,000 + Ending)/2`, `Net income = (500 − Interest) × 0.75`. Solve by iteration, starting from a beginning-balance interest guess.

| Pass | Interest guess | Net income | Ending debt | New average | New interest |
|---|---:|---:|---:|---:|---:|
| 0 (start) | 100.000 | 300.000 | 700.000 | 850.000 | 85.000 |
| 1 | 85.000 | 311.250 | 688.750 | 844.375 | 84.438 |
| 2 | 84.438 | 311.672 | 688.328 | 844.164 | 84.416 |
| 3 | 84.416 | 311.688 | 688.312 | 844.156 | 84.416 |

The interest column settles at **84.42** after three passes — the change from pass 2 to pass 3 is under 0.001, so Excel's iterative calculation (Max iterations 100, Max change 0.001) would stop here. Confirm algebraically: let `I` be interest. `Ending = 625 + 0.75I` (since Ending = 1,000 − 0.75(500 − I)); `I = 50 + 0.05 × Ending = 50 + 0.05(625 + 0.75I) = 81.25 + 0.0375I`; so `0.9625I = 81.25`, giving `I = 84.416`. Then Ending = 625 + 0.75 × 84.416 = **688.31**, Net income = (500 − 84.416) × 0.75 = **311.69**, and Ending = 1,000 − 311.69 = 688.31 ✓. The iteration and the closed-form solution agree — this is exactly what Excel does for you when iterative calculation is on.

**B7. From schedule to statement links.** Using B5's Y1 figures (draws 0, mandatory 100, sweep 150, interest 70, ending 750), state exactly which number each statement pulls and with what sign.

- **Income statement:** interest expense **70.0** above pre-tax income (reduces EBT, and hence tax and net income).
- **Cash flow — financing:** mandatory repayment **(100)** and sweep **(150)**, i.e. total debt repayment **(250)** as an outflow; no draws this year.
- **Cash flow — operations:** interest is **not** shown here — it already sits inside net income at the top of CFO.
- **Balance sheet — liabilities:** **ending debt 750**, a direct link to the closing row.

Interest touches one statement (the income statement); principal touches one statement (financing on the cash flow); the balance sheet just reads the closing line.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through what happens to the three statements when the company draws 100 on its revolver."**

The draw itself is an asset-and-liability swap. On the **cash flow statement**, financing shows a **+100** inflow, so cash rises 100. On the **balance sheet**, cash rises 100 on the asset side and the revolver rises 100 on the liability side — both sides up by the same amount, so it still balances with no plug, and nothing has hit the **income statement** yet. Then the borrowing cost appears: say the revolver rate is 5%, so on the average drawn balance the interest might be roughly 2.5 in the first year. That interest reduces pre-tax income by 2.5; at a 25% tax rate net income falls about 1.9. On the cash flow statement that lower net income and the offsetting tax saving flow through operations, and on the balance sheet retained earnings fall about 1.9 while cash falls by the after-tax interest paid — both sides move together and it stays balanced. Headline: the draw is a swap; only its interest and tax shield touch income.

**C2. "What is a circular reference in a three-statement model, and why does the debt schedule create one?"**

A circular reference is a chain of formulas that loops back on itself — a cell that ultimately depends on its own output. In a debt schedule it arises the moment you charge interest on the *average* balance. Interest depends on the ending balance (half of the average); the ending balance depends on how much debt you repaid; repayment depends on cash available; cash available depends on cash flow from operations; CFO depends on net income; and net income depends on interest. So interest depends on interest — a true loop. Excel flags it and shows zeros until you enable iterative calculation, which spins the loop until the numbers stabilise. The loop is not a bug; it is the honest representation of a business whose borrowing cost and cash generation feed each other.

**C3. "How do you handle circularity so the model doesn't break?"**

Three tools. First, **enable iterative calculation** (File → Options → Formulas: Max iterations 100, Max change 0.001) so Excel resolves the loop instead of showing zeros. Second — and this is the robust professional pattern — add a **circularity switch**: a control cell, say `CircSwitch`, and route interest through `IF(CircSwitch=1, Rate × Average, 0)`. If a stray `#REF!` or `#DIV/0!` ever poisons the loop, iteration keeps feeding that error back on itself and it persists even after you fix the source; flipping the switch to 0 severs the loop, clears every error, and lets the model recalc clean, then you flip it back to 1 and it re-converges. Third, if the file will be widely shared or stress-tested, I sidestep the loop entirely by charging interest on the **beginning balance**, which is a settled fact from last year and forms no cycle — trading a fraction of a percent of precision for bulletproof robustness.

**C4. "Beginning, average, or ending balance for interest — which do you use and why?"**

**Average** `(Beginning + Ending)/2` is the most accurate because it reflects that the balance changes through the year, but it creates the circular reference and needs iteration plus a switch. **Beginning** balance is the robust choice: it forms no loop because it is inherited from last year, so the model is portable and can't be poisoned by a stray error — the cost is a slight, systematic overstatement of interest when debt is falling. **Ending** balance is rarely used because it both creates circularity *and* understates interest on a declining balance, giving you the worst of both. My default is average-plus-switch when I control the file and precision matters, and beginning-balance when the model must be shared, audited, or heavily stress-tested.

**C5. "Why isn't interest expense in the financing section of the cash flow statement, when principal repayments are?"**

Because interest and principal are different kinds of cash. Interest is a cost of doing business — it was already deducted to arrive at net income, which is the top line of cash flow from operations, so it is captured there. Putting it in financing as well would double-count the same cash leaving. Principal draws and repayments, on the other hand, never touched the income statement; they are pure balance-sheet financing transactions, so financing is the only place they appear. The clean rule: interest flows through operations via net income; only principal movements sit in financing.

**C6. "What is a cash sweep, and why do analysts model one?"**

A cash sweep is a rule that uses surplus cash to pay down debt early, above the contractual mandatory amortisation — often 50% or 100% of free cash flow after the revolver is repaid, per the credit agreement. It matters because it makes the model behave like a real leveraged business: excess cash doesn't just pile up, it deleverages the company, which lowers future interest, which raises future cash, which sweeps more debt — the same feedback that drives the returns in an LBO. Modelled correctly with a `MIN` cap against the remaining balance, the sweep accelerates paydown without ever over-repaying, and it is one of the main reasons the interest loop is economically alive.

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Hardcoded debt on the balance sheet.**
```
Balance sheet, long-term debt (2026):  600   ' typed as a value
```
**Wrong:** the debt line is a typed constant instead of `=` the schedule's ending balance. The two will drift the moment any assumption changes, and the balance sheet will stop balancing. Fix: always *link* the balance sheet debt line to the schedule's authoritative ending-balance cell — one number, one place.

**D2. Repayment with no `MIN` cap.**
```
Mandatory repayment = −Scheduled amortization      ' flat −200 every year
```
**Wrong:** in the final years the scheduled instalment exceeds the remaining balance, so the roll-forward subtracts more than exists and the ending balance goes negative. Fix: `= −MIN(Scheduled amortization, Beginning balance)`, which repays the lesser of what is due and what is left and lands cleanly at zero.

**D3. Double-counting interest in the cash flow.**
```
Cash flow (operations):  starts from Net income (already net of interest)
Cash flow (financing):   − Interest paid   ' subtracted again
```
**Wrong:** interest already reduced net income at the top of operations, so subtracting it again in financing counts the same cash outflow twice and understates cash. Fix: only *principal* draws and repayments belong in financing; remove the interest line from there entirely.

**D4. Circularity switch left off.**
```
CircSwitch = 0        ' flipped to clear an error, never flipped back
Interest = IF(CircSwitch=1, Rate*Average, 0)   ' evaluates to 0
```
**Wrong:** the model is shipping with **zero interest expense**, silently overstating net income, cash and equity. Fix: flip `CircSwitch` back to 1 after clearing the error, and add conditional formatting that turns the cell bright red when it is 0 so it can't be missed.

**D5. Average-balance interest without iteration enabled.**
```
Interest 2025 = Rate * (Beginning + Ending)/2   ' shows 0, status bar: "Circular References"
```
**Wrong:** the analyst assumes the model is broken and hardcodes a number. It isn't broken — the average legitimately creates a loop, and Excel just hasn't been told to resolve it. Fix: File → Options → Formulas → enable iterative calculation (Max 100, change 0.001); the numbers converge. Do not hardcode over a real, solvable loop.

**D6. Sign-convention chaos.**
```
Row: Draws        +150     ' inflow positive
Row: Repayment    +200     ' also positive — subtracted somewhere else by hand
Ending = Beginning + Draws + Repayment    ' balance grows when it should fall
```
**Wrong:** repayments are stored positive but the roll-forward `SUM`s them, so paying down debt *increases* the balance. Fix: pick one convention — draws positive, repayments negative — everywhere, including the financing links, so the closing line is a single clean `SUM`.

**D7. Wrong first-year beginning balance.**
```
Beginning balance (Year 1) = D15    ' points at a forecast ending cell, not last actual
```
**Wrong:** the first forecast year's opening must link to the last *historical/actual* debt balance; pointing it at a forecast cell (or hardcoding a stale number) feeds an error into the very first link, and the whole roll-forward chain inherits it. Fix: `Year 1 Beginning = last actual closing balance`; every subsequent year is `= prior year ending`.

**D8. Revolver that over-borrows or silently repays.**
```
Revolver draw = Minimum cash − Cash available before revolver   ' no MAX(0, …)
```
**Wrong:** in surplus years the formula returns a *negative* draw — the revolver "borrows" a negative amount, i.e. silently repays without capping against what is actually drawn, and it can even push the balance negative. Fix: separate the two behaviours — `Draw = MAX(0, −Cash available)` and `Repay = −MIN(Beginning revolver, MAX(0, Cash available))` — so a draw is never negative and a repayment never exceeds the drawn balance.
