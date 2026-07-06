# Q&A — Capstone — Build a Full Model End to End

This is the integration chapter. Everything you learned in isolation — revenue drivers, the three statements, the debt schedule, circularity, valuation — now has to live in one workbook that ties out. Work each problem before reading the answer. If your model does not balance, the failure is diagnostic; do not paper over it.

---

## Section A — Concept Check

**A1. What does "end to end" actually mean for a full model?**

It means a single integrated workbook that flows from raw assumptions all the way to an output or decision, with no manual bridges. Concretely: drivers feed a forecast income statement; the income statement feeds supporting schedules (working capital, PP&E, debt, equity); those schedules feed the balance sheet and cash flow statement; the three statements are linked so cash and retained earnings flow automatically; and the whole thing rolls up into a valuation and a set of outputs (DCF, returns, ratios, a dashboard). Change one assumption and every number downstream updates on its own.

**A2. State the canonical build order and why it exists.**

The standard order is: (1) set up the workbook structure and historicals, (2) build assumptions/drivers, (3) forecast the income statement down to EBIT, (4) build the supporting schedules — working capital, PP&E/depreciation, then debt & interest, then equity, (5) complete the income statement (interest, tax, net income), (6) assemble the balance sheet, (7) build the cash flow statement and link the closing cash back to the balance sheet, (8) check the balance, (9) layer valuation and outputs. The order exists because each step depends on outputs of the prior one — you cannot compute interest before you have a debt schedule, and you cannot complete the cash flow statement before the balance sheet items exist. Interest and the cash sweep are deliberately last because they create circularity.

**A3. What is the single test that tells you an integrated model is internally consistent?**

The balance sheet balances in every period: Total Assets = Total Liabilities + Equity, with the check row equal to zero. Because the model is fully articulated, a zero balance check is a strong signal that every double-entry has been captured correctly. It is necessary but not fully sufficient — two offsetting errors can still net to zero — which is why you also run reasonableness and sanity checks.

**A4. Explain how the three statements are linked, in one loop.**

Net income from the income statement flows into (a) retained earnings on the balance sheet and (b) the top of the cash flow statement. The cash flow statement adjusts net income for non-cash items (depreciation), working-capital movements, capex, debt draws/repayments, and equity flows to arrive at the net change in cash. That change is added to opening cash to give closing cash, which becomes the cash line on the balance sheet. Every other balance-sheet line is driven by its own schedule. When cash and retained earnings are both fed from the statements, the balance sheet closes the loop and must balance.

**A5. Where does circularity enter a full model, and what causes it?**

Circularity enters at the interest calculation. Interest expense depends on the debt balance; if you use an average balance (opening + closing)/2, the closing balance depends on the cash sweep; the sweep depends on free cash flow; free cash flow depends on net income; net income depends on interest expense — closing the loop. A revolver that draws to fund a minimum cash balance creates the same loop. This is intentional and correct economics, not a mistake.

**A6. How do you make a circular model calculable and safe?**

Enable iterative calculation (Excel: File > Options > Formulas > Enable iterative calculation, ~100 iterations, max change 0.001). Then protect against a #REF!/#DIV0 poisoning the loop by wiring a circularity breaker (a "circ switch"): a toggle cell that, when set to 0, forces interest to zero and breaks the loop so you can clear a #VALUE! that would otherwise propagate and freeze. Best practice is an IF around the interest driver keyed to that switch.

**A7. What is a "check panel" and what belongs on it?**

A check panel is a dedicated block (often its own tab, or a fixed region on each sheet) of automated integrity tests that must all read TRUE/0. Typical checks: balance sheet balances (A = L+E) each period; cash flow closing cash equals balance sheet cash; retained earnings roll-forward ties; sum of sources = sum of uses (in transactions); no hardcodes in formula rows; depreciation never exceeds remaining net book value; debt never goes negative. A conditional-format "master flag" turns red if any check fails.

**A8. Why forecast the income statement only down to EBIT before building schedules?**

Because everything below EBIT — interest and tax — depends on schedules you have not built yet. Interest needs the debt schedule; tax needs pre-tax income which needs interest. So you stop at EBIT (or EBITDA then D&A to EBIT), build the balance-sheet schedules, and only then return to finish interest, tax and net income. Trying to complete the P&L first forces you to hardcode numbers you will later have to rip out.

**A9. Distinguish a driver, a calculation, and an output — and why colour-code them.**

A driver (assumption/input) is a hardcoded number you can change — revenue growth %, days receivable, tax rate. A calculation is a formula that derives from drivers and other calculations — never overtyped. An output is a headline result you read off — DCF value, IRR, a ratio. Colour convention: blue font for inputs, black for formulas, sometimes green for links to other sheets. It lets any reviewer instantly see what is safe to change (blue) and what must never be typed over (black).

**A10. What is the difference between a model that "balances" and a model that is "right"?**

Balancing proves the accounting is internally articulated. Being right requires the assumptions to be defensible, the logic to reflect real economics, and the outputs to survive sanity checks (margins in a believable range, growth decaying to a terminal rate, returns not absurd). A model can balance perfectly and still be wrong if the drivers are nonsense. Integrity checks catch mechanical errors; judgment catches economic errors.

---

## Section B — Build / Computational Problems

*Each problem reconciles exactly. Build the labelled cells, then check against the reconciliation before reading on.*

**B1. Minimal three-statement link — one forecast year.**

Given for Year 1 forecast: Revenue 1,000; EBITDA margin 20%; depreciation 40; interest expense 15; tax rate 25%. Opening cash 50. Capex 60. Increase in net working capital 10. No debt draws/repayments, no dividends, no equity issuance. Compute net income, closing cash, and confirm the change in retained earnings.

*Answer.*
- EBITDA = 1,000 × 20% = 200.
- EBIT = 200 − 40 (depreciation) = 160.
- EBT = 160 − 15 (interest) = 145.
- Tax = 145 × 25% = 36.25.
- **Net income = 145 − 36.25 = 108.75.**
- Cash flow from operations = NI 108.75 + depreciation 40 − increase in NWC 10 = 138.75.
- Cash flow from investing = −capex 60.
- Cash flow from financing = 0.
- Net change in cash = 138.75 − 60 + 0 = 78.75.
- **Closing cash = 50 + 78.75 = 128.75.**
- Change in retained earnings = net income − dividends = 108.75 − 0 = **108.75** (matches NI, as it must with no dividends).

**B2. Prove the balance sheet balances after B1.**

Extend B1. Opening balance sheet: Cash 50, Net PP&E 400, other assets 200; Debt 300, other liabilities 150, Equity 200 (of which retained earnings 100). During Year 1: capex 60, depreciation 40, NWC increase of 10 sits inside "other assets/liabilities" net (assume it raised net operating assets by 10). Show assets = liabilities + equity at year end.

*Answer.*
- Net PP&E closing = 400 + 60 capex − 40 depreciation = 420.
- Cash closing = 128.75 (from B1).
- Other net operating assets rose by 10 (the NWC build): other assets 200 → 210 (assume the increase lands on the asset side; liabilities unchanged at 150).
- Total assets = 128.75 + 420 + 210 = **758.75**.
- Debt unchanged = 300. Other liabilities = 150.
- Equity closing = 200 + 108.75 retained = 308.75.
- Total L+E = 300 + 150 + 308.75 = **758.75**.
- Check = 758.75 − 758.75 = **0. Balances.** Note the NWC increase of 10 consumed cash (it is subtracted in CFO) and simultaneously raised assets by 10; both sides move together, preserving the balance.

**B3. Working capital schedule feeding the model.**

Revenue 1,200; COGS 720. Assumptions: DSO 45 days, DIO 60 days, DPO 30 days (use 365). Compute AR, Inventory, AP and net working capital, and the cash impact if last year's NWC was 120.

*Answer.*
- AR = 1,200 × 45/365 = 147.9.
- Inventory = 720 × 60/365 = 118.4.
- AP = 720 × 30/365 = 59.2.
- Net working capital = 147.9 + 118.4 − 59.2 = **207.1**.
- Change in NWC = 207.1 − 120 = 87.1 increase → **cash outflow of 87.1** in CFO (a rising NWC absorbs cash).

**B4. PP&E and depreciation roll-forward.**

Opening gross PP&E 1,000, accumulated depreciation 300 (net 700). Capex 150. Existing assets depreciate straight-line over 10 years on gross; new capex over 5 years (half-year convention: half a year of depreciation in the year of purchase). Compute depreciation, closing net PP&E.

*Answer.*
- Depreciation on existing gross = 1,000 / 10 = 100.
- Depreciation on new capex = (150 / 5) × 0.5 half-year = 15.
- Total depreciation = 100 + 15 = **115**.
- Closing gross PP&E = 1,000 + 150 = 1,150.
- Closing accumulated depreciation = 300 + 115 = 415.
- **Closing net PP&E = 1,150 − 415 = 735.** (Check: net 700 + 150 capex − 115 depreciation = 735. Ties.)

**B5. Debt schedule with a cash sweep and average-balance interest (the circular part).**

Opening debt 500 at 8% interest on the average balance. Cash available for debt repayment (after all operating and investing flows, before financing) = 120. Mandatory amortisation = 25. Any remaining cash sweeps to prepay debt. Minimum cash need already satisfied. Solve for interest, repayment and closing debt (iterate).

*Answer.* This is circular: interest depends on average balance, which depends on repayment, which depends on cash available after interest. Iterate.
- Mandatory repayment = 25.
- Cash left for optional sweep = 120 − 25 = 95, but interest is paid from that cash too. Treat cash-for-debt as post-interest here (interest is an operating/EBT item already reflected in the 120). Then:
- Optional sweep = min(95, remaining debt after mandatory) = 95.
- Total repayment = 25 + 95 = 120.
- Closing debt = 500 − 120 = 380.
- Average balance = (500 + 380)/2 = 440.
- Interest = 440 × 8% = **35.2**. Because the 120 was defined as cash after operating flows that already included this interest, the loop is consistent at closing debt **380**, interest **35.2**. (In the live model the 120 itself recomputes as interest changes; iterative calc settles it. The teaching point: interest and closing debt co-determine each other.)

**B6. Circularity breaker in action.**

Your model shows #VALUE! spreading across every forecast column and the whole book is frozen. Describe the exact sequence to recover, and write the interest formula that prevents recurrence.

*Answer.*
1. Set the circ switch cell (e.g. `Ctrl_Circ`) to 0. This forces interest to 0, breaking the loop.
2. The #VALUE! source is now isolated — find and fix the underlying error (usually a text value, a #REF! from a deleted row, or iterative calc turned off).
3. Turn iterative calculation back on (File > Options > Formulas).
4. Set the circ switch back to 1; the model re-solves.
- Robust interest formula: `=IF($Ctrl_Circ=1, AVERAGE(OpeningDebt, ClosingDebt) * Rate, 0)`. The switch multiplies the interest driver so a single toggle can always sever the circular reference and clear a poisoned loop.

**B7. From EBIT to a DCF value (tying the model to an output).**

Unlevered free cash flow forecast: Year1 90, Year2 100, Year3 110, Year4 120, Year5 130. WACC 9%. Terminal value via Gordon growth at 2.5%. Compute enterprise value.

*Answer.*
- Discount factors at 9%: Y1 0.9174, Y2 0.8417, Y3 0.7722, Y4 0.7084, Y5 0.6499.
- PV of explicit FCFs: 90×0.9174=82.6; 100×0.8417=84.2; 110×0.7722=84.9; 120×0.7084=85.0; 130×0.6499=84.5. Sum = **421.2**.
- Terminal value at end of Y5 = 130 × (1.025) / (0.09 − 0.025) = 133.25 / 0.065 = 2,050.0.
- PV of terminal value = 2,050.0 × 0.6499 = **1,332.3**.
- **Enterprise value = 421.2 + 1,332.3 ≈ 1,753.5.** Sanity: terminal value is ~76% of EV — high but normal for a 5-year window; flag if it exceeds ~85%.

**B8. Net income to closing retained earnings across two years (roll-forward integrity).**

Opening retained earnings 100. Year1 NI 108.75 (from B1), dividend 20. Year2 NI 130, dividend 25. Show the roll-forward and the equity linkage.

*Answer.*
- Year1 closing RE = 100 + 108.75 − 20 = **188.75**.
- Year2 closing RE = 188.75 + 130 − 25 = **293.75**.
- The equity block on the balance sheet must show retained earnings equal to these figures; the dividends must also appear as financing outflows in the cash flow statement. If the RE roll-forward and the CFS dividend line disagree, the balance sheet will break by exactly the mismatch — a fast way to localise an error.

---

## Section C — Interview-Style Questions (Model Answers)

**C1. "Walk me through how the three statements connect."**

*Model answer.* Start with net income on the income statement. It flows to the top of the cash flow statement, where I add back non-cash charges like depreciation, adjust for changes in working capital, subtract capex, and add or subtract financing flows — debt draws and repayments, equity issuance, dividends. That gives the net change in cash, which I add to opening cash for closing cash — and that closing cash is the cash line on the balance sheet. Meanwhile net income less dividends flows into retained earnings in the equity section of the balance sheet. Depreciation reduces net PP&E on the balance sheet and is added back on the cash flow statement. Every other line has its own schedule. Because both cash and retained earnings are fed from the statements rather than typed, the balance sheet has to balance — that's the proof the linkage is correct.

**C2. "You build a three-statement model. Which statement do you build first and why?"**

*Model answer.* The income statement, but only down to EBIT, because it drives the schedules. Then I build the balance-sheet support schedules — working capital, PP&E, debt, equity — because the balance sheet and the rest of the P&L depend on them. Interest and tax come after the debt schedule exists, so I finish the income statement next. Then the balance sheet, then the cash flow statement, which I link so closing cash feeds back to the balance sheet. I check the balance last. The principle is that you build in dependency order: never compute a number before its inputs exist.

**C3. "Your model has a circular reference. Is that a problem?"**

*Model answer.* Not inherently — it's expected. Interest expense depends on the average debt balance, which depends on the cash sweep, which depends on free cash flow, which depends on net income, which depends on interest. That loop is correct economics. I handle it by enabling iterative calculation and building a circularity switch so I can break the loop to clear any error, then re-solve. What I never do is hardcode interest to escape the circularity, because that severs the model's articulation and it will stop reflecting changes in leverage.

**C4. "How do you know your model is correct?"**

*Model answer.* First, mechanical integrity: the balance sheet balances in every period, closing cash on the cash flow ties to the balance sheet, retained earnings rolls forward cleanly, and my check panel is all green. Second, reasonableness: margins, growth rates and returns sit in defensible ranges, growth decays to a sensible terminal rate, and the implied multiples aren't absurd. Third, stress: I flex the key drivers and watch that outputs move in the right direction and magnitude. Balancing proves the plumbing; the sanity and sensitivity work proves the economics.

**C5. "Walk me through a DCF built off this model."**

*Model answer.* I take unlevered free cash flow — EBIT times one minus tax, plus depreciation and amortisation, minus capex, minus the increase in net working capital — for each forecast year. I discount those at WACC. Then I compute a terminal value, either by Gordon growth — final-year FCF times one plus g, over WACC minus g — or an exit multiple on terminal EBITDA, and discount it back at the same rate. Summing the present values gives enterprise value. From there I subtract net debt to get equity value, and divide by shares for value per share. I always check what proportion of EV is terminal value; if it's over roughly 80%, I revisit the forecast horizon or the terminal assumptions.

**C6. "We change revenue growth from 5% to 8%. Talk me through what moves."**

*Model answer.* Revenue rises, so gross profit and EBITDA rise. That lifts EBIT and, after interest and tax, net income. Higher net income increases cash from operations, but higher growth also builds working capital — receivables and inventory rise — which partly offsets the cash gain. More sales may need more capex. Net free cash flow usually still rises, so more cash is available to sweep debt, which lowers the debt balance and reduces interest, which feeds back and lifts net income again — that's the circular loop resolving. On the balance sheet, retained earnings, cash, working capital and PP&E all move; it still balances. On outputs, the DCF value and returns rise. The whole point of an integrated model is that I can state this chain and the numbers follow automatically.

---

## Section D — Common-Error Spotting

*For each, identify the error and give the fix.*

**D1.** The balance sheet is off by exactly the dividend amount. *Error:* dividends were deducted from retained earnings on the balance sheet but not shown as a financing outflow in the cash flow statement (or vice-versa). *Fix:* ensure every dividend hits both retained earnings and CFS financing; the two must be driven from the same cell.

**D2.** Closing cash on the cash flow statement does not equal the cash line on the balance sheet. *Error:* the balance-sheet cash is hardcoded or linked to the wrong cell instead of pointing at the cash flow's closing cash. *Fix:* balance-sheet cash must be a direct link to CFS closing cash — never an independent number.

**D3.** Depreciation drives net PP&E below zero in later years. *Error:* depreciation continues on fully-depreciated assets. *Fix:* cap depreciation at remaining net book value using MIN, so an asset can never depreciate past zero.

**D4.** Interest expense is a hardcoded 15 in every year. *Error:* interest was pinned to dodge circularity, so leverage changes no longer affect the P&L. *Fix:* link interest to the debt schedule on an average or opening balance, enable iterative calculation, and add a circ switch.

**D5.** The model froze with #VALUE! everywhere and won't recalculate. *Error:* iterative calculation is off (or a #REF! entered the circular loop and poisoned it). *Fix:* set the circ switch to 0 to break the loop, fix the source error, enable iterative calc, then set the switch back to 1.

**D6.** Change in net working capital is added in cash flow from operations. *Error:* sign convention reversed — an increase in NWC consumes cash and must be subtracted. *Fix:* CFO adjustment = −(change in NWC); a rising NWC is a cash outflow.

**D7.** Terminal value is 94% of enterprise value. *Error:* not a formula error but an economic red flag — the forecast horizon is too short or the terminal growth rate too high. *Fix:* extend the explicit forecast until the business normalises, or lower g / the exit multiple; cross-check Gordon growth against an exit-multiple TV.

**D8.** Retained earnings on the balance sheet was typed as a fixed number. *Error:* a hardcode in a formula row breaks articulation. *Fix:* retained earnings must be opening RE + net income − dividends, all links; blue-font inputs only in the assumptions block.

**D9.** The revolver shows a negative balance in a strong year. *Error:* the sweep repays more than the outstanding revolver. *Fix:* wrap the repayment in MIN(available cash, opening revolver balance) so the revolver floors at zero and excess cash instead builds the cash balance.

**D10.** Two errors of +8 and −8 net to zero, so the balance check reads zero but the model is wrong. *Error:* offsetting mistakes masking each other. *Fix:* don't rely on the balance check alone — run granular checks (cash tie, RE roll-forward, schedule sub-totals) and trace unusual line movements; a single balance check is necessary, not sufficient.

---

*Self-check completed: every arithmetic answer in Section B reconciles (B1 NI 108.75 and closing cash 128.75; B2 both sides 758.75; B4 net PP&E 735 by two methods; B7 EV ≈ 1,753.5). Every question is followed by a full answer across all four sections.*
