# Q&A — Accounting Foundations — the Three Statements

Practice bank for Chapter 02. Work each question before reading the answer. Every computational answer reproduces cell-for-cell in Excel and ties.

---

## Section A — Concept Checks (test the WHY)

**A1. Why do we need three statements instead of one? Couldn't a single "money in / money out" ledger tell us everything?**

No — because two genuinely different things must be measured, and one ledger can only measure one of them. The Income Statement answers *how much did we earn this period* using accrual (revenue when earned, expense when incurred). The Cash Flow Statement answers *how much cash actually moved*. These diverge whenever a sale is on credit, a cost is prepaid, or a non-cash charge like depreciation hits. The Balance Sheet answers a third, orthogonal question — *what do we own and owe at one instant*. A single cash ledger would miss profit earned but not yet collected. Three questions, three grids.

**A2. Why is "Assets = Liabilities + Equity" always true rather than merely usually true?**

Because it holds *by construction*, not by observation. Double-entry bookkeeping records every transaction in two places whose effects are equal and offsetting. Buy a $100 machine for cash: assets +100 (machine), assets −100 (cash) — net zero. Buy it on credit: assets +100 (machine), liabilities +100 (payable) — both sides rise equally. There is no possible single-entry that shifts one side without an equal move that preserves the identity. So a balance sheet that does *not* balance is not reporting an unusual company; it is reporting a modelling error.

**A3. Why does the accrual convention force the Cash Flow Statement to exist?**

Accrual deliberately decouples the timing of profit from the timing of cash. The moment you recognise revenue you haven't collected, or expense a machine's cost over years rather than when you paid for it, accrual net income stops equalling cash generated. Something must bridge the two, line by line, or an analyst cannot get from reported profit to the change in the bank balance. That bridge *is* the Cash Flow Statement (indirect method): start at net income and undo every accrual so what remains is cash.

**A4. Why is the "balance check = 0" cell the single most important number in a live model?**

Because it is a proof, checked continuously, that the double-entry logic held across every formula. If it reads zero, every link fired with the right sign and magnitude. The instant it goes non-zero, you have a missed or mis-signed wire, and — crucially — you know *before* you trust any downstream valuation. It is a smoke detector: cheap, always-on, and it fails loud.

**A5. Why is hardcoding a number to force the balance to close ("plugging") worse than leaving the model broken?**

A broken balance is honest — it flags that an error exists so you can hunt it. A plug *silences the detector while the fire still burns*: the underlying error remains and corrupts every ratio, cash flow, and valuation downstream, but the check reads zero so nobody looks. An interviewer who presses Ctrl+[ (trace precedents) on the balance check finds the hardcode in seconds.

**A6. Why does depreciation appear three times in an integrated model, and why is that not double-counting?**

It plays three distinct roles, each once. (1) On the Income Statement it reduces EBIT because using up an asset is a real economic cost of the period. (2) In CFO it is *added back*, because although it reduced profit it moved no cash. (3) On the Balance Sheet it reduces net PP&E, because the asset is now worth less. Each appearance records a different consequence of the same event — cost recognised, cash unaffected, asset consumed. Miss any one and the statements stop tying.

---

## Section B — Build / Computational Problems

**B1. Build a full Income Statement.** Revenue 800; COGS 480; SG&A 120; D&A 40; Interest 25; tax rate 25%. Compute every subtotal down to net income.

Step by step:
- Gross profit = 800 − 480 = **320**
- EBITDA = Gross profit − SG&A = 320 − 120 = **200**
- EBIT = EBITDA − D&A = 200 − 40 = **160**
- EBT = EBIT − Interest = 160 − 25 = **135**
- Tax = 135 × 25% = **33.75**
- Net income = 135 − 33.75 = **101.25**

Excel: put 800, 480, 120, 40, 25, 25% as blue inputs; every line below is a formula (`=Rev-COGS`, etc.); tax `=EBT*taxrate`.

**B2. Build the CFO section (indirect method).** Net income 101.25 (from B1); D&A 40. Receivables rose 60→75; Inventory fell 90→82; Payables rose 50→58.

Apply the sign rule (asset up → −, asset down → +, liability up → +):
- Δ Receivables = 75 − 60 = +15 increase → cash effect **(15)**
- Δ Inventory = 82 − 90 = −8 decrease → cash effect **+8**
- Δ Payables = 58 − 50 = +8 increase → cash effect **+8**

CFO = 101.25 + 40 − 15 + 8 + 8 = **142.25**

**B3. Complete the cash roll and net change in cash.** Continue B2. Capex 55 (CFI). Financing: debt repayment 20, dividends 30 (CFF). Opening cash 45.

- CFI = **(55)**
- CFF = −20 − 30 = **(50)**
- Net change in cash = CFO + CFI + CFF = 142.25 − 55 − 50 = **37.25**
- Closing cash = 45 + 37.25 = **82.25**

**B4. Full reconciling period — build all three and prove the balance.**

*Opening Balance Sheet (Year 0):* Cash 60, Receivables 50, Inventory 40, PP&E 300 → Assets 450. Payables 40, Debt 150, Share capital 120, Retained earnings 140 → L+E 450. (Balanced: 450 = 450.)

*Year 1 assumptions:* Revenue 700; COGS 420; SG&A 110; D&A 30; Interest = 10% × opening debt 150 = 15; tax 25%. Capex 45. Dividends 25. Debt repayment 20. Closing working capital: Receivables 62, Inventory 46, Payables 52.

**Income Statement:**

| Line | Value |
|---|---|
| Revenue | 700 |
| COGS | (420) |
| Gross profit | 280 |
| SG&A | (110) |
| EBITDA | 170 |
| D&A | (30) |
| EBIT | 140 |
| Interest | (15) |
| EBT | 125 |
| Tax @ 25% | (31.25) |
| **Net income** | **93.75** |

**Cash Flow Statement:**

| Line | Value |
|---|---|
| Net income | 93.75 |
| Add: D&A | 30 |
| Δ Receivables (50→62) | (12) |
| Δ Inventory (40→46) | (6) |
| Δ Payables (40→52) | +12 |
| **CFO** | **117.75** |
| Capex | (45) |
| **CFI** | **(45)** |
| Debt repayment | (20) |
| Dividends | (25) |
| **CFF** | **(45)** |
| **Net change in cash** | **27.75** |

CFO check: 93.75 + 30 − 12 − 6 + 12 = 117.75. Net change: 117.75 − 45 − 45 = 27.75.

**Closing Balance Sheet (Year 1):**

| Assets | | Liabilities & Equity | |
|---|---|---|---|
| Cash (60 + 27.75) | 87.75 | Payables | 52 |
| Receivables | 62 | Debt (150 − 20) | 130 |
| Inventory | 46 | Share capital | 120 |
| PP&E (300 + 45 − 30) | 315 | Retained earnings (140 + 93.75 − 25) | 208.75 |
| **Total assets** | **510.75** | **Total L & E** | **510.75** |

Verify each wire:
- Retained earnings: 140 + 93.75 − 25 = 208.75 ✓
- PP&E: 300 + 45 − 30 = 315 ✓
- Cash: 60 + 27.75 = 87.75 ✓
- Debt: 150 − 20 = 130 ✓
- Assets 87.75 + 62 + 46 + 315 = 510.75; L&E 52 + 130 + 120 + 208.75 = 510.75. **Balance check = 0.** ✓

**B5. Stress the B4 model.** Raise capex to 70 (from 45) and cut dividends to 0. Recompute cash, PP&E, retained earnings, and re-prove the balance. (Nothing on the Income Statement changes — capex and dividends never touch the P&L.)

- Net income unchanged: 93.75. CFO unchanged: 117.75 (capex and dividends are not CFO items).
- CFI = (70). CFF = debt repayment 20 only = (20). Net change in cash = 117.75 − 70 − 20 = **27.75**. Closing cash = 60 + 27.75 = **87.75**. (Coincidentally identical to B4: the extra 25 capex outflow is exactly offset by the 25 dividend no longer paid.)
- PP&E = 300 + 70 − 30 = **340** (up 25 vs B4's 315).
- Retained earnings = 140 + 93.75 − 0 = **233.75** (up 25 vs B4's 208.75).
- Assets: 87.75 + 62 + 46 + 340 = **535.75**. L&E: 52 + 130 + 120 + 233.75 = **535.75**. **Balance check = 0.** ✓

The two 25s land on opposite sides (asset PP&E vs equity RE) and both totals rise by 25 — the sheet still ties, proving the links are live.

**B6. Compute FCFF from the B4 statements.** Use FCFF = EBIT × (1 − t) + D&A − Capex − ΔNWC.

- EBIT = 140; t = 25% → EBIT × (1 − t) = 140 × 0.75 = **105**
- D&A = +30
- Capex = −45
- ΔNWC = Δ(Receivables + Inventory − Payables) = (62 + 46 − 52) − (50 + 40 − 40) = 56 − 50 = **+6** increase → −6
- FCFF = 105 + 30 − 45 − 6 = **84**

Every term traces to a line already built: EBIT and tax from the Income Statement, D&A and capex from Cash Flow, ΔNWC from the Balance Sheet working-capital moves.

---

## Section C — Interview-Style Questions

**C1. "Walk me through how the three statements link."**

Model answer: Net income from the bottom of the Income Statement flows to two places — it starts the Cash Flow Statement, and it increases retained earnings on the Balance Sheet (retained earnings = prior + net income − dividends). Within the Cash Flow Statement you add back D&A (non-cash), adjust for working-capital changes taken off the Balance Sheet, then add investing flows (capex) and financing flows (debt and equity). The net change in cash flows to the cash line on the Balance Sheet (cash = prior cash + net change). D&A also reduces PP&E, and capex increases it. When every one of those links is live, the Balance Sheet balances — and that balance is proof the whole thing tied.

**C2. "A company has positive net income but is going bankrupt. How?"**

Model answer: Profit is accrual, not cash. If the firm sells hard on credit, receivables balloon and the cash was never collected; if it stockpiles inventory ahead of demand, cash is buried in stock. Both are cash outflows in CFO despite a healthy P&L. Say net income is 100 with D&A 10, but receivables rise 90 and inventory 60 while payables rise only 20: CFO = 100 + 10 − 90 − 60 + 20 = **−20**. It earned 100 of profit and *lost* 20 of cash. Add debt repayments or capex on top and it can't make payroll. This is exactly why the Cash Flow Statement exists as a separate document — reading only the P&L hides the liquidity risk.

**C3. "If you could pick only one of the three statements to value a company, which and why?"**

Model answer: The Cash Flow Statement. Valuation is the present value of *cash* a business generates, not accrual profit, so cash flow is closest to intrinsic value and hardest to manipulate — you can manage earnings with accrual judgement, but cash is cash, and it drives a DCF most directly. It's a forced choice, though: cash flow alone hides leverage (Balance Sheet) and margin structure (Income Statement), so in practice I'd never value on one grid.

**C4. "What happens to all three statements if depreciation increases by 10, tax rate 25%?"**

Model answer: *Income Statement* — EBIT falls 10, so EBT falls 10, tax falls 2.5, net income falls **7.5**. *Cash Flow* — net income down 7.5, but D&A of 10 is added back, so CFO rises by 10 − 7.5 = **+2.5** (the tax shield); cash rises 2.5. *Balance Sheet* — cash up 2.5; PP&E down 10 (extra depreciation); retained earnings down 7.5 via lower net income. Check: assets change = +2.5 − 10 = −7.5; equity change = −7.5. Both sides fall 7.5, still balanced. The net benefit of more depreciation is the **2.5 cash tax shield**.

**C5. "Why do we use the indirect method for cash flow in a model rather than the direct method?"**

Model answer: The indirect method starts at net income and adjusts, so every line explicitly references either the Income Statement or a Balance Sheet change — which makes the three-statement linkage visible and auditable. The direct method lists actual cash receipts and payments, which is cleaner to read but requires data models rarely forecast line by line and severs the tidy link to net income. For a linked model where I need CFO to obviously tie back to the other two statements, indirect wins.

**C6. "I increase inventory by 50, paying cash. Effect on the three statements immediately?"**

Model answer: No Income Statement effect yet — buying inventory isn't an expense until it's sold (matching). Balance Sheet: inventory +50, cash −50; assets net zero, still balanced. Cash Flow: the inventory increase is a −50 working-capital use in CFO. So net income is unchanged but cash drops 50. It only hits the P&L as COGS when the goods are sold.

---

## Section D — Common-Error Spotting

**D1. Broken CFO.** An analyst writes: `CFO = Net income + D&A + Δ Receivables + Δ Inventory − Δ Payables`, referencing raw period-over-period changes. Given NI 63, D&A 20, receivables 40→55, inventory 30→35, payables 30→40, their sheet shows CFO = 63 + 20 + 15 + 5 − 10 = 93. What's wrong?

The working-capital **signs are inverted**. An increase in an operating asset *uses* cash and must be subtracted; an increase in an operating liability *provides* cash and must be added. The correct formula is `NI + D&A − Δ(operating assets) + Δ(operating liabilities)` = 63 + 20 − 15 − 5 + 10 = **73**, not 93. Their error overstates CFO by 20 (the swing is 2 × 10). Fix: `Δ Receivables = −(AR_new − AR_old)` and `Δ Payables = +(AP_new − AP_old)`.

**D2. Plugged balance.** A model's closing balance check reads zero, but tracing the cash cell shows `=Total L&E − (Receivables + Inventory + PP&E)` instead of `=Opening cash + Net change in cash`. Why is this dangerous even though the sheet "balances"?

Because cash has been made a **plug**: it's defined as whatever makes assets equal L&E, so the balance check *can never* be non-zero — the detector is disabled. Any real error elsewhere (a wrong margin, a missed dividend) now silently flows into a wrong cash figure instead of tripping the check. Cash must be driven independently by the cash roll (`opening + CFO + CFI + CFF`); only then does the balance check become a genuine, independent proof.

**D3. Retained earnings error.** Retained earnings is coded `=Prior RE + Net income`. The firm paid a 15 dividend. Prior RE 90, NI 63. The sheet won't balance — by how much and which way?

Dividends are missing. Correct RE = 90 + 63 − 15 = **138**; the broken formula gives 90 + 63 = 153, which is **15 too high**. Equity is overstated by 15, so total L&E exceeds total assets by 15 (the 15 of cash that actually left for the dividend was correctly removed on the asset side via CFF, but equity wasn't reduced to match). Fix: `RE_end = Prior RE + Net income − Dividends`.

**D4. Double-counted / missing D&A.** A build reduces EBIT by D&A of 20 and reduces PP&E by 20, but the modeller *forgot to add D&A back in CFO*. Net income is 63. What breaks and by how much?

CFO is understated by 20. Net income (63) already absorbed the 20 non-cash charge; failing to add it back leaves CFO 20 too low, so net change in cash and closing cash are each **20 too low**. On the Balance Sheet, cash is 20 short while PP&E and retained earnings are correct, so assets fall 20 short of L&E — the check reads **−20**. D&A must appear exactly three times: minus on the P&L, plus in CFO, minus in PP&E. Here the CFO add-back was the missing third appearance.

**D5. Cash item on the P&L.** A modeller subtracts the 25 capex and 20 debt repayment as expenses on the Income Statement to "be conservative." What's conceptually wrong, and what's the effect?

Both are **cash/financing items, not accrual expenses**, and neither belongs on the P&L. Capex buys an asset (it's spread into the P&L over time as depreciation, not expensed at once); debt repayment is a return of principal, purely a financing flow. Putting them on the Income Statement understates net income by 45, double-counts them (they already appear in CFI/CFF), and unbalances the sheet. The Income Statement is accrual throughout; capex lives in CFI, debt repayment in CFF.

**D6. Wrong subtotal mechanics.** A modeller computes Gross profit as `=B5+B6` where B5 is revenue and B6 is COGS entered as a positive 480. Result shows 1,280 for revenue 800. Two problems — name them.

(1) **Sign/convention error:** COGS is a cost. Either enter it as negative (−480) and sum, or subtract a positive (`=Revenue − COGS`). Adding a positive COGS inflates gross profit to 800 + 480 = 1,280 instead of 800 − 480 = **320**. (2) **Chained `+` instead of `SUM`:** using `=B5+B6` rather than `=SUM(B5:B6)` means an inserted row between them is silently excluded from the subtotal — a classic source of drift in a growing model. Fix both: consistent negative-cost convention and `=SUM(range)` for stacks.

---

*Self-check: rebuild B4 and B5 in Excel. If both balance checks read exactly zero and survive the B5 stress, your linkages are live formulas, not hardcodes — the standard every later FMVA chapter assumes.*
