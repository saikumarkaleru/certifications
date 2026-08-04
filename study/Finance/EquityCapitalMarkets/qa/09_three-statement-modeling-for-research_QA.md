# Q&A — Three-Statement Modeling for Research

Theory and worked scenarios on building and troubleshooting a linked financial model.

---

### Q1. Walk me through building a three-statement model from scratch.

**Model answer.** Start with revenue, driven by explicit operating drivers (volume × price, or a growth rate applied to a segment build) rather than a guessed top-line number. Build costs and margins off revenue to reach EBITDA and EBIT. Build supporting schedules — depreciation (linked to the PP&E and capex build), working capital (driven by DSO/DIO/DPO days), and a debt schedule (linked to financing needs and interest). Complete the income statement with interest (from the debt schedule) and taxes to reach net income. Build the cash flow statement starting from net income, adding back non-cash D&A, adjusting for working-capital changes, subtracting capex, and reflecting financing flows. Complete the balance sheet using the cash flow's ending cash, the PP&E roll-forward, working-capital balances, debt, and retained earnings (prior balance plus net income minus dividends). Finally, check that assets equal liabilities plus equity every single year — if it doesn't balance, there is a linking error somewhere.

---

### Q2. Where exactly does circularity arise in a three-statement model, and name two ways to handle it.

**Model answer.** Circularity arises because interest expense depends on the debt balance, the debt balance depends on the cash flow (which determines whether the company draws on or pays down a revolver), and cash flow itself depends on net income, which depends on interest expense — a closed loop. Two standard fixes: (1) enable iterative calculation (Excel's circular-reference setting), letting the model converge numerically over repeated recalculation passes; (2) break the circularity structurally by computing interest on the *opening* (prior period) debt balance rather than the average balance, which removes the current period's own cash flow from the interest calculation entirely.

---

### Q3. Worked — trace how a ₹50 cr increase in capex flows through all three statements.
*A company increases its planned capex by ₹50 cr in Year 1 versus the prior forecast, funded by drawing on its revolver (debt). Tax rate 25%, no immediate change to depreciation policy in Year 1 itself.*

**Model answer.**
Income statement: no immediate Year-1 P&L impact from the capex itself (capex is capitalised, not expensed) — though the higher PP&E base will increase future years' depreciation expense.
Balance sheet: PP&E rises by ₹50 cr (gross additions); debt rises by ₹50 cr (the revolver draw funding it) — assuming no cash was used, cash is unaffected by the capex itself in this financing structure.
Cash flow statement: investing activities show a ₹50 cr outflow (capex); financing activities show a ₹50 cr inflow (the revolver draw) — the two roughly offset in the net-change-in-cash line, but investing and financing cash flow, viewed separately, both move by ₹50 cr in opposite directions.
The check: PP&E is up ₹50 cr and debt is up ₹50 cr on the balance sheet, matching the offsetting ₹50 cr investing outflow and ₹50 cr financing inflow on the cash flow statement — everything ties.

---

### Q4. Why must depreciation be linked to both the PP&E schedule and the income statement, rather than being entered as a flat assumption in each place separately?

**Model answer.** If depreciation is entered independently in the income statement and in the PP&E roll-forward, the two numbers can drift out of sync (e.g. an analyst updates the capex assumption but forgets to update the resulting depreciation expense to match), silently breaking the model's internal consistency and causing the balance sheet to stop balancing without an obvious error message. Linking depreciation as a single calculated schedule feeding both the income statement (as an expense) and the PP&E roll-forward (as a reduction) is what makes the model a genuinely connected machine rather than three separately-typed documents that happen to sit next to each other.

---

### Q5. What are the two balance-sheet-integrity checks every well-built model should include, and what does a failure of each one tell you?

**Model answer.** (1) Assets = Liabilities + Equity, checked every forecast year — a failure means there's a broken link somewhere in how an item flows from one statement to another (a classic culprit: net income not fully flowing to retained earnings, or a working-capital change not correctly reflected on both the cash flow and balance sheet). (2) Cash on the balance sheet equals the ending cash balance from the cash flow statement — a failure specifically flags an error in the cash-flow build itself (a financing or investing line not correctly captured) even if the balance sheet appears superficially to balance via some other, unrelated plug.

---

### Q6. Why is "driving off assumptions" (rather than hard-coding forecast numbers) considered a best practice, beyond just being tidier?

**Model answer.** A driver-based model (e.g. revenue = stores × sales-per-store, rather than a bare "revenue grows 12%" hard-coded number) is transparent about *why* the forecast is what it is, defensible in front of a portfolio manager or interviewer who will ask what's driving the number, and mechanically sensitisable — changing one assumption (e.g. sales-per-store growth from 4% to 6%) automatically ripples correctly through the whole model. A hard-coded forecast number hides the underlying logic, can't be meaningfully stress-tested, and is a strong signal in an interview or work-sample review that the candidate hasn't actually thought through the business drivers.

---

### Q7. A three-statement model outputs FCFF for a DCF. What specific line items from the model does the analyst need to pull, and what must they be careful not to double-count?

**Model answer.** FCFF = EBIT × (1 − tax rate) + D&A − Capex − ΔNWC, so the analyst pulls EBIT (from the income statement), D&A (from the depreciation schedule), capex (from the investing section of the cash flow build), and the change in net working capital (from the working-capital schedule). The care point: EBIT must be taxed as if unlevered (ignoring the model's actual interest expense) specifically to avoid double-counting the interest tax shield, which is captured separately inside WACC when the DCF discounts these cash flows — pulling the model's actual (post-interest) net income and working backward incorrectly is a common error that inflates or corrupts the FCFF figure.

---

### Q8. Interviewer asks: "Your model isn't balancing — where do you look first?" What's a structured troubleshooting approach?

**Model answer.** First check the most common culprits in order: (1) does net income correctly flow to both retained earnings on the balance sheet and the top of the cash flow statement — a mismatch here is the single most frequent error; (2) does the depreciation figure match between the income statement expense and the PP&E roll-forward reduction; (3) are all working-capital changes reflected consistently on both the cash flow statement's operating adjustments and the balance sheet's corresponding line items; (4) does the debt schedule's ending balance match what's shown on the balance sheet, and does the associated interest expense match what's in the income statement. Working through these links systematically, rather than randomly changing numbers until the model happens to balance, is both faster and signals real understanding of how the statements connect.
