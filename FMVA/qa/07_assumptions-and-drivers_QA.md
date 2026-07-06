# Q&A — Assumptions and Drivers — the Model Engine

This bank drills the layer that actually powers a three-statement model: the assumptions and the drivers built from them. Every question is followed by a full answer. Work the build problems on paper or in Excel first, then check.

---

## Section A — Concept Check

**A1. What is the difference between an "assumption" and a "driver"?**

An assumption is a raw input you decide on judgementally or from research — e.g. "revenue grows 8% next year," "DSO is 45 days," "tax rate is 25%." A driver is the mechanism that converts an assumption into a line-item value inside the model. The assumption "8% growth" becomes the driver `Prior Revenue x (1 + 8%)`. Assumptions are what you believe; drivers are how that belief flows into the financial statements. Good models expose assumptions as editable cells and bury drivers in formulas.

**A2. Why should every hardcoded number in a model live in a dedicated assumptions area, not inside a formula?**

Three reasons: (1) Auditability — a reviewer can see every input at a glance instead of hunting through formulas. (2) Sensitivity — you can flex one cell and watch the whole model respond, which is impossible if the number is trapped inside `=B12*1.08`. (3) Single source of truth — if a growth rate is referenced in ten places, hardcoding it ten times guarantees an inconsistency the first time you update nine of them. The rule: blue font for inputs, black for formulas, and no number typed inside a formula except genuine constants like 12 (months) or 365 (days).

**A3. What is a "driver-based" forecast and why is it preferred over a straight-line percentage growth forecast?**

A driver-based forecast decomposes a line item into its underlying operational levers before forecasting. Instead of "revenue grows 8%," you model `Revenue = Units x Price`, then forecast units (from capacity, market share, or store count) and price (from inflation or a pricing strategy) separately. It is preferred because it ties the model to the real business, makes assumptions defensible in a diligence meeting, and lets you sensitise the true levers (a 5% price cut vs. a 5% volume drop have very different margin effects that a blended growth rate hides).

**A4. Name the four most common working-capital drivers and the ratio each uses.**

- Accounts Receivable — Days Sales Outstanding (DSO) = AR / Revenue x 365
- Inventory — Days Inventory Outstanding (DIO) = Inventory / COGS x 365
- Accounts Payable — Days Payable Outstanding (DPO) = AP / COGS x 365
- Accrued/other — usually a % of revenue or opex

To forecast, invert the ratio: `Forecast AR = DSO / 365 x Forecast Revenue`.

**A5. What does it mean for an assumption to be a "circularity trigger," and give one classic example.**

An assumption creates circularity when the line it drives feeds back into itself through the statements. The classic case is interest expense: interest depends on the debt balance, the debt balance depends on cash flow (whether you draw or repay the revolver), cash flow depends on net income, and net income depends on interest expense — a loop. The interest-on-average-balance assumption is the trigger. It is handled with an iterative-calculation switch or a circularity breaker cell.

**A6. Why do modellers separate operating assumptions from financing assumptions?**

Because they answer different questions and are owned by different people. Operating assumptions (growth, margins, working capital, capex) describe how the business performs and drive EBIT and unlevered cash flow. Financing assumptions (interest rates, debt schedule, dividends, share issuance) describe how the business is funded and drive the bottom of the model. Keeping them apart lets you value the business independent of its capital structure (the basis of DCF/enterprise value) and swap financing scenarios without touching operations.

---

## Section B — Build / Computational Problems

**B1. Revenue driver — units x price.**

Given: Year 0 sold 100,000 units at $50. You assume units grow 6% per year and price grows 3% per year. Build revenue for Years 1–3.

Step by step:
- Units: Y1 = 100,000 x 1.06 = 106,000; Y2 = 106,000 x 1.06 = 112,360; Y3 = 112,360 x 1.06 = 119,101.6
- Price: Y1 = 50 x 1.03 = 51.50; Y2 = 51.50 x 1.03 = 53.045; Y3 = 53.045 x 1.03 = 54.63635
- Revenue = Units x Price:
  - Y1 = 106,000 x 51.50 = **$5,459,000**
  - Y2 = 112,360 x 53.045 = **$5,959,634** (112,360 x 53.045 = 5,959,633.4)
  - Y3 = 119,101.6 x 54.63635 = **$6,507,738** (119,101.6 x 54.63635 = 6,507,741, rounding)

Excel: units cell `=B_units*(1+$units_growth)`, price `=B_price*(1+$price_growth)`, revenue `=units*price`. Note revenue grows ~9.18% (1.06 x 1.03 − 1 = 0.0918), not 9%, because growth rates compound multiplicatively, not additively.

**B2. Working-capital driver — build the AR/Inventory/AP schedule.**

Given forecast: Revenue $6,000,000; COGS $3,600,000. Assumptions: DSO 45, DIO 60, DPO 40 days. Compute each balance.

- AR = 45 / 365 x 6,000,000 = 0.123288 x 6,000,000 = **$739,726**
- Inventory = 60 / 365 x 3,600,000 = 0.164384 x 3,600,000 = **$591,781**
- AP = 40 / 365 x 3,600,000 = 0.109589 x 3,600,000 = **$394,521**

Net working capital (these three) = 739,726 + 591,781 − 394,521 = **$937,486**. Reconciliation check — invert AR: 739,726 / 6,000,000 x 365 = 45.0 days. Good.

**B3. Change in NWC and its cash-flow impact.**

Prior year the same three balances were AR $700,000, Inventory $550,000, AP $360,000 (NWC = 890,000). Using B2's forecast NWC of $937,486, what is the cash-flow effect?

Change in NWC = 937,486 − 890,000 = +$47,486 (an increase in NWC).
An increase in NWC is a **use of cash**, so it reduces cash flow by **$47,486** on the cash flow statement (shown as −47,486 in operating activities). Intuition: you tied up more money in receivables and inventory than you released through payables.

**B4. Depreciation driver — straight-line off a rolling PP&E schedule.**

Given: opening gross PP&E $2,000,000, existing depreciation $200,000/year on the opening base. New capex: Y1 $300,000, Y2 $300,000. New capex is depreciated straight-line over 10 years (so $30,000/year each), with a full year of depreciation in the year of purchase. Build depreciation and closing net PP&E for Y1 and Y2 (opening net PP&E $1,000,000).

Depreciation:
- Y1 = 200,000 (base) + 30,000 (Y1 capex) = **$230,000**
- Y2 = 200,000 (base) + 30,000 (Y1 capex) + 30,000 (Y2 capex) = **$260,000**

Net PP&E roll-forward (Net_close = Net_open + Capex − Depreciation):
- Y1 = 1,000,000 + 300,000 − 230,000 = **$1,070,000**
- Y2 = 1,070,000 + 300,000 − 260,000 = **$1,110,000**

Excel pattern: `Closing = Opening + Capex - Depreciation`, and next year's Opening `=` this year's Closing. Reconciliation: net PP&E rose $110,000 over two years; capex $600,000 − depreciation $490,000 = $110,000. Ties.

**B5. Debt schedule driver — interest on average balance.**

Given: opening debt $1,000,000, mandatory repayment $100,000/year, interest rate 8% on the **average** of opening and closing balance. Build Y1.

- Opening = 1,000,000; Repayment = 100,000; Closing = 900,000
- Average balance = (1,000,000 + 900,000) / 2 = 950,000
- Interest expense = 8% x 950,000 = **$76,000**

If instead interest were charged on the opening balance: 8% x 1,000,000 = $80,000. The average-balance method is more accurate but introduces circularity when the closing balance depends on a revolver that flexes with cash flow; the opening-balance method avoids circularity at the cost of slight overstatement.

**B6. Tax driver and reconciling the income statement bottom.**

Given: EBIT $500,000, interest expense $76,000 (from B5), tax rate 25%. Compute EBT, tax, and net income.

- EBT = 500,000 − 76,000 = **$424,000**
- Tax = 25% x 424,000 = **$106,000**
- Net income = 424,000 − 106,000 = **$318,000**

Check: net income / EBT = 318,000 / 424,000 = 0.75 = (1 − 25%). Correct. Tax must be computed on EBT (after interest), never on EBIT, or you double-count the tax shield on debt.

**B7. Assemble a mini one-year forecast and confirm the balance sheet balances.**

Pull it together. Opening cash $50,000. Net income $318,000 (B6). Depreciation $230,000 (B4, non-cash add-back). Increase in NWC $47,486 (B3, use of cash). Capex $300,000. Debt repayment $100,000. No dividends, no equity issuance.

Cash flow statement:
- CFO = 318,000 + 230,000 − 47,486 = **$500,514**
- CFI = −300,000 (capex) = **−$300,000**
- CFF = −100,000 (debt repayment) = **−$100,000**
- Net change in cash = 500,514 − 300,000 − 100,000 = **$100,514**
- Closing cash = 50,000 + 100,514 = **$150,514**

The balance-sheet proof: retained earnings rise by net income $318,000; cash rises $100,514; net PP&E rises by 300,000 − 230,000 = 70,000; NWC (net of the AP piece) rises 47,486; debt falls 100,000. Assets side change = 100,514 + 70,000 + 47,486 = 218,000. Liabilities+equity change = 318,000 (RE) − 100,000 (debt) = 218,000. **Balances.** The single most important self-check in any model.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through how you would forecast revenue for a company you have never modelled before."**

Model answer: "I start top-down and bottom-up and reconcile. Bottom-up, I break revenue into the real drivers — for a retailer that's stores x sales-per-store, for SaaS it's customers x ARPU with a churn assumption, for a manufacturer it's units x price. I forecast each driver from something observable: historical trend, capacity, contracted backlog, or management guidance. Top-down, I sanity-check total revenue against market size and market share so my bottom-up numbers don't imply an impossible share. Where they disagree I dig into the gap. The output is a revenue build where every number traces to an assumption I can defend, not a single blended growth percentage."

**C2. "Your model has 40 assumptions. How do you decide which ones actually matter?"**

Model answer: "I run a sensitivity analysis — flex each key assumption up and down by a set amount and rank them by impact on the output metric, usually equity value or IRR. Typically two or three drivers explain most of the variance: revenue growth, gross margin, and the discount rate or exit multiple. Those get the most research and a data table or tornado chart. The rest I set reasonably and leave. This stops me from over-engineering assumptions that don't move the answer while I under-research the ones that do."

**C3. "What is the danger of building a forecast on straight-line percentage growth?"**

Model answer: "It hides the operating reality and can silently break. If I grow revenue 8% and hold every cost as a fixed percent of revenue, I've assumed constant margins forever, which ignores operating leverage, price/volume mix, and fixed-cost dilution. It also lets impossible things through — a company can't grow 30% a year for a decade without capex and working capital that the percent-of-revenue approach may under-provide. Driver-based forecasting forces me to confront capacity, headcount, and unit economics, so the model fails loudly when an assumption is unrealistic instead of quietly producing a wrong number."

**C4. "How do you keep a model's assumptions honest — from being just the number that makes the deal work?"**

Model answer: "First, I triangulate every major assumption against an external anchor — historical actuals, industry benchmarks, analyst consensus, or management guidance — and document the source next to the cell. Second, I build a base, downside, and upside case rather than a single point estimate, so the model shows a range and I'm not anchored to one hopeful path. Third, I check that the implied metrics are sane: does my terminal growth exceed GDP forever? Does implied ROIC drift above what competitors earn? If the assumptions individually look fine but the implied economics are heroic, that's the tell that I've reverse-engineered the answer."

**C5. "Where does circularity come from in a three-statement model and how do you handle it?"**

Model answer: "The main loop is interest expense: interest depends on debt, debt depends on the revolver draw, the revolver depends on the cash shortfall, cash depends on net income, and net income depends on interest — a circle. I handle it one of two ways. Either enable Excel's iterative calculation and add a circularity-breaker switch — a cell that zeroes interest to clear a `#REF!`/circular error, then flips back on. Or I avoid it entirely by charging interest on the opening balance instead of the average. The switch is essential; without it a single error propagates and freezes the whole workbook."

---

## Section D — Common-Error Spotting

**D1. What is wrong here?**

`Forecast AR  =  DSO * Revenue / 365   where DSO cell = 45, Revenue = 6,000,000`
Formula returns 45 * 6,000,000 / 365 = 739,726.

Answer: Nothing is wrong with the arithmetic — this is the correct AR driver and returns $739,726, matching B2. This is a control item: verify that the formula references the DSO **assumption cell**, not a hardcoded 45. If someone typed `=45*Revenue/365`, the number is right today but the sensitivity is dead — flexing the DSO assumption cell does nothing. Correct: `=$DSO_cell/365*Revenue`.

**D2. Broken driver — spot the error.**

`Tax expense = Tax_rate * EBIT` with EBIT = 500,000, rate 25%, giving 125,000. Net income is then computed as EBIT − Interest − Tax = 500,000 − 76,000 − 125,000 = 299,000.

Answer: Tax is computed on **EBIT** instead of **EBT**. Tax must be levied after interest: EBT = 500,000 − 76,000 = 424,000, tax = 25% x 424,000 = 106,000, net income = 318,000 (per B6). The broken version taxes the interest deduction away, understating net income by 19,000 and destroying the interest tax shield. Correct formula: `=Tax_rate * (EBIT - Interest)`.

**D3. What is wrong with this NWC sign?**

Model shows: change in NWC = +47,486, and the cash flow statement adds it: `CFO = NetIncome + Depreciation + ChangeInNWC`.

Answer: The sign is inverted. An **increase** in net working capital is a **use** of cash and must be **subtracted**. The formula adds it, overstating CFO by 2 x 47,486 = 94,972. Correct: `CFO = NetIncome + Depreciation - ChangeInNWC`, giving 318,000 + 230,000 − 47,486 = 500,514 (per B7). A reliable convention: build the cash flow line as `-(NWC_close - NWC_open)` so the sign is automatic and can't be flipped by mistake.

**D4. Spot the compounding error.**

An analyst wants revenue to grow with 6% volume and 3% price, and writes `Revenue = Prior * (1 + 6% + 3%) = Prior * 1.09`.

Answer: Growth rates that multiply must compound, not add. The true combined factor is 1.06 x 1.03 = 1.0918, i.e. 9.18% growth, not 9%. On $5,000,000 the additive shortcut gives 5,450,000 vs. the correct 5,459,000 — a $9,000 error in year one that compounds every subsequent year. Correct: `=Prior*(1+vol_growth)*(1+price_growth)`, or better, model units and price on separate rows and multiply them (per B1).

**D5. What is wrong with this depreciation roll-forward?**

`Closing Net PP&E = Opening + Depreciation - Capex`, giving 1,000,000 + 230,000 − 300,000 = 930,000.

Answer: Signs are swapped. Capex **adds** to the asset base; depreciation **reduces** it. The correct roll-forward is `Closing = Opening + Capex - Depreciation` = 1,000,000 + 300,000 − 230,000 = 1,070,000 (per B4). The broken formula shows the asset shrinking when the company is actually investing net-positive, and it will throw the balance sheet out by 140,000 (the double-counted swing).

**D6. The balance sheet is off by exactly the change in cash. What is the likely cause?**

Answer: When a three-statement model is out of balance by precisely the net change in cash, the closing cash on the balance sheet is almost always **not linked** to the cash flow statement's ending cash — someone hardcoded it or linked it to opening cash. Fix: set balance-sheet cash `=` the CFS closing cash line (50,000 + 100,514 = 150,514 in B7). The general debugging move: an imbalance equal to a single statement line points you straight at the missing or broken link for that line.

**D7. What is wrong with charging interest and why might the model freeze?**

Interest is set to `= Rate * Average(Opening debt, Closing debt)`, the closing debt includes a revolver that draws to cover any cash shortfall, and Excel returns a circular-reference warning with zeros everywhere.

Answer: This is intended circularity (interest → net income → cash → revolver → debt → interest), but iterative calculation is **off**, so Excel refuses to resolve the loop and blanks the cells. Two fixes: (1) turn on File > Options > Formulas > Enable iterative calculation, and add a circularity-breaker switch cell so you can reset if an error propagates; or (2) charge interest on the **opening** balance to break the loop entirely — 8% x 1,000,000 = 80,000 — accepting a small overstatement versus the average-balance figure of 76,000 (per B5).

---

## Quick reference — the driver formulas

- Revenue (unit): `Units x Price`, each grown on its own row
- AR: `DSO / 365 x Revenue`  |  Inventory: `DIO / 365 x COGS`  |  AP: `DPO / 365 x COGS`
- Change in NWC on CFS: `-(NWC_close - NWC_open)` (increase = use of cash)
- Net PP&E: `Opening + Capex - Depreciation`
- Debt interest (average): `Rate x (Opening + Closing) / 2`
- Tax: `Rate x (EBIT - Interest)` → net income = EBT x (1 − Rate)
- The one check that matters: change in assets = change in liabilities + equity
