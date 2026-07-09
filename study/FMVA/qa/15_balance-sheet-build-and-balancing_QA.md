# Q&A — Building and Balancing the Balance Sheet

Practice bank for Chapter 15. Work each question before reading the answer. The build problems use clean, round numbers you can reproduce cell-for-cell in Excel, and every one reconciles: assets equal liabilities plus equity, check zero. Increases in assets are uses of cash; increases in liabilities/equity are sources. Figures in ₹ '000.

---

## Section A — Concept Checks (test the WHY)

**A1. Why is the balance sheet the one statement you do *not* forecast line by line?**

Because almost every line is an *output* of a schedule you already built, not an independent assumption: cash from the cash flow statement, working-capital items from that schedule, net PP&E from the fixed-asset roll-forward, debt from the debt schedule, retained earnings from the equity roll-forward. Forecasting a line directly would double-count a decision already made in a schedule and sever the link that keeps the model coherent. The balance sheet is a *reporting layer*, not a *calculation layer*.

**A2. Why does a correctly built balance sheet balance automatically, with no plug?**

Because of double-entry bookkeeping. Every economic event moves at least two accounts by equal and offsetting amounts, so each transaction preserves Assets = Liabilities + Equity. The identity holds in the opening (audited) period, and every recorded transaction keeps it holding. Therefore a balance sheet assembled from correctly built schedules *cannot* be out of balance — you do not force it, you earn it.

**A3. Why is cash the linchpin that makes the whole balance sheet close?**

Because cash is the single residual that absorbs the net effect of every other schedule. Every source and use of funds flows through the cash flow statement to produce ending cash, and ending cash is the last asset line. If — and only if — every non-cash change has been captured on the cash flow statement with the correct sign, ending cash will be exactly the number that makes both sides agree. Cash is where the reconciliation lands.

**A4. Why is it literally true that "the balance sheet only balances when the cash flow statement is correct"?**

Because the cash flow statement *is* the reconciliation between two consecutive balance sheets. ΔCash is defined as net income minus the change in non-cash assets plus the change in liabilities and financing equity. Substitute those changes into the prior-period identity and every non-cash term cancels against its mirror on the cash flow statement, leaving Assets = Liabilities + Equity in the new period. If the reconciliation has a gap — one account's change missing or mis-signed — the cancellation is incomplete, and the leftover term *is* the imbalance.

**A5. Why does the size of an imbalance tell you the size of the error?**

Because the imbalance is exactly the uncancelled term from the reconciliation above. If you omit a ₹30 dividend from financing cash flow, ₹30 of cash that should have left is still sitting in assets while equity correctly shows it gone — assets are high by exactly 30. The magnitude is diagnostic: it points straight at the missing, doubled, or sign-flipped cash flow.

**A6. Why is an omission a 1× error but a sign flip a 2× error?**

An omission simply leaves a term out: the imbalance equals that one amount (1×). A sign flip does double damage — it removes the correct −X *and* adds a wrong +X, a swing of 2X. So if your check equals exactly twice a schedule figure, suspect a flipped sign; if it equals the figure once, suspect an omission.

**A7. Why does a broken roll-forward link cause an imbalance that *grows* every period?**

A roll-forward carries a balance forward by setting each period's beginning value equal to the prior period's ending value (retained earnings, PP&E, debt). If that beginning-to-ending link is broken, the error introduced in period 1 is never corrected and each subsequent period adds its own fresh discrepancy on top. The cumulative drift — an imbalance that enlarges period after period — is the fingerprint of broken chaining, distinct from a constant imbalance caused by a one-off omission.

**A8. Why can a model balance perfectly and still be wrong?**

Because balancing proves only that your reconciliation is *complete*, not that your inputs are *correct*. If net income is overstated, both cash and retained earnings move by the same amount, so the identity still closes — around a wrong number. Balancing is necessary but not sufficient for correctness; it catches missing or mis-signed cash flows, not bad assumptions.

**A9. Why must you never enter a liability as a negative to "net it out" on the balance sheet?**

Because on the balance sheet all assets, liabilities, and equity are shown as positives; the sign convention (negatives for uses of cash) lives on the cash flow statement. Mixing a negative into the balance sheet corrupts the totals and defeats the balance check, which relies on both sides being clean positive sums.

**A10. Why round the balance check to a few decimals instead of testing raw `=0`?**

Because Excel's floating-point arithmetic can leave a residue like 0.0000000004 that is not a real error but would trip a strict equality test. `ROUND(check, 3)` tolerates that sub-unit noise while still catching any genuine imbalance, which is always at least a whole currency unit.

---

## Section B — Build / Computational Problems

**B1. Retained-earnings roll-forward over two years.** Opening RE = 250. Year 1: net income 120, dividends 20. Year 2: net income 140, dividends 30. Compute ending RE each year and give the Excel chaining.

Formula `RE_end = RE_beg + NI − Dividends`.

- Year 1: 250 + 120 − 20 = **350**
- Year 2: 350 + 140 − 30 = **460**

In Excel, Year 2's beginning RE cell links to Year 1's ending cell (`=C_RE_end`), never re-typed. That single link is what carries equity through the forecast; break it and the imbalance grows every period (A7).

**B2. Full one-year build and balance check.** Year 0 (₹ '000): Cash 50, AR 200, Inventory 150, Net PP&E 600 (assets 1,000); AP 100, Long-term debt 400, Common stock 250, Retained earnings 250 (L+E 1,000). Year 1 assumptions: net income 120; dividends 20; AR → 230; Inventory → 170; AP → 120; Capex 100; Depreciation 70; Debt repayment 60; no share issuance. Build the roll-forwards, the cash flow statement, assemble the balance sheet, and prove the check is zero.

*Roll-forwards:*
- RE = 250 + 120 − 20 = **350**
- Net PP&E = 600 + 100 − 70 = **630** (`=Beg + Capex − Dep`)
- Long-term debt = 400 − 60 = **340**

*Cash flow statement:*
- CFO `=NI + Dep − ΔAR − ΔInv + ΔAP` = 120 + 70 − 30 − 20 + 20 = **160**
- CFI `=−Capex` = **−100**
- CFF `=−Debt repay − Dividends` = −60 − 20 = **−80**
- ΔCash = 160 − 100 − 80 = **−20**; Ending cash = 50 − 20 = **30**

*Assembled Year 1 balance sheet:*

| Assets | | Liab + Equity | |
|---|---|---|---|
| Cash | 30 | Accounts payable | 120 |
| Accounts receivable | 230 | Long-term debt | 340 |
| Inventory | 170 | Common stock | 250 |
| Net PP&E | 630 | Retained earnings | 350 |
| **Total assets** | **1,060** | **Total L+E** | **1,060** |

Balance check = 1,060 − 1,060 = **0. ✓** Ending cash (30) was never assumed — it is the residual that closes the identity.

**B3. Extend to Year 2 and confirm the chaining holds.** Continue B2. Year 2: net income 140; dividends 30; AR → 250; Inventory → 190; AP → 130; Capex 110; Depreciation 80; Debt repayment 60.

*Roll-forwards (beginning = Year 1 ending):*
- RE = 350 + 140 − 30 = **460**
- Net PP&E = 630 + 110 − 80 = **660**
- Long-term debt = 340 − 60 = **280**

*Cash flow statement:*
- CFO = 140 + 80 − (250−230) − (190−170) + (130−120) = 140 + 80 − 20 − 20 + 10 = **190**
- CFI = **−110**
- CFF = −60 − 30 = **−90**
- ΔCash = 190 − 110 − 90 = **−10**; Ending cash = 30 − 10 = **20**

*Year 2 balance sheet:* Assets = 20 + 250 + 190 + 660 = **1,120**; L+E = 130 + 280 + 250 + 460 = **1,120**. Check = **0. ✓** Because each beginning balance linked to the prior ending balance, the identity propagated cleanly into a second period.

**B4. Solve for the missing cash flow.** A Year 1 model shows Total assets = 1,060 and Total L+E (excluding cash's effect) is fully built and correct at 1,060, but the analyst has *not yet* filled the CFF dividend line. Given opening cash 50, CFO 160, CFI −100, and debt repayment 60 already in CFF, what dividend figure makes ending cash consistent with a balancing sheet, and what is that ending cash?

Work backwards from the requirement that the sheet balances. From B2 we know the balancing ending cash is 30. So required ΔCash = 30 − 50 = −20. With CFO 160 and CFI −100, CFF must be −80. Since debt repayment already contributes −60, the dividend must be **−20**. Ending cash = **30**. This is the inverse of the diagnostic principle: a known correct balance pins down exactly the cash flow you are missing.

**B5. Compute the balance-check formula and its wrapper.** Total assets are in cell `B40`, total liabilities-and-equity in `B55`. Write (a) the raw check, (b) the rounded, human-readable wrapper, and (c) a master roll-up across period checks in `C60:F60`.

- (a) `=B40-B55`
- (b) `=IF(ROUND(B40-B55,3)=0,"OK",B40-B55)` — prints "OK" when clean, the signed difference when broken.
- (c) `=SUM(ABS(C60:F60))` entered so it aggregates every period's raw check; a single non-zero here flags the whole model. Pair (b) with conditional formatting that fills red when `ABS(B40-B55)>0.5`.

**B6. Prove the propagation numerically.** Using B2, verify that ΔCash equals net income minus the change in non-cash assets plus the change in liabilities and financing equity — i.e. that the cash flow statement is the reconciliation of the two balance sheets.

Change in non-cash assets = ΔAR 30 + ΔInv 20 + ΔNetPP&E (630−600)=30, total **+80**.
Change in liabilities = ΔAP 20 + ΔLTD (340−400)=−60, total **−40**.
Change in financing/other equity = share issuance 0 − dividends 20 = **−20**.
Reconciliation: ΔCash = NI 120 − 80 + (−40) + (−20) = 120 − 80 − 40 − 20 = **−20.** This equals the −20 computed directly on the cash flow statement in B2. The non-cash terms cancel exactly, which is *why* the sheet balances.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through how you assemble the projected balance sheet in a three-statement model."**

I build the balance sheet *last*. The income statement runs to net income; the supporting schedules — working capital, PP&E, debt, equity — each feed the cash flow statement, which produces ending cash. Only then do I assemble the balance sheet, where every line is a *link* to its schedule: cash to ending cash, receivables/inventory/payables to working capital, net PP&E to the fixed-asset roll-forward, debt to the debt schedule, retained earnings and common stock to the equity roll-forward. No cell is a fresh assumption or hard-code. Finally I add a balance-check row — total assets minus total liabilities-and-equity — which must read zero every period.

**C2. "Your model is out of balance by 4,732 in Year 3. How do you find the error?"**

I treat the number as a signal. First: does it grow each period? If so it's a broken roll-forward link, so I trace the chaining on retained earnings, PP&E, and debt. If it's constant, I test whether 4,732 equals a known schedule figure (an omitted cash flow) or exactly twice one (a sign flip in the cash flow statement). If neither matches, I go to the first period that breaks and reconcile line by line: every balance-sheet delta must appear on the cash flow statement with the correct sign — asset increase as a use, liability/equity increase as a source. The line where they disagree is the error. And before anything, I confirm cash links to ending cash and isn't a plug.

**C3. "Why can't you just hard-code ending cash to make the model balance?"**

Because that destroys the model's integrity. Hard-coding cash — or inserting a plug line — forces the check to read zero while the underlying business no longer reconciles: money has appeared or vanished without being recorded. The balance check would go green and give false confidence. Cash must always be the residual output of the cash flow statement, so that the check remains a live proof that every source and use of funds is accounted for.

**C4. "Explain why net income affects the balance sheet in two places at once."**

Net income enters equity through retained earnings — beginning RE plus net income minus dividends — and it simultaneously enters cash as the first line of cash flow from operations. Those are the two halves of the same transaction, which is exactly why earning profit keeps the balance sheet in balance: equity rises by net income and assets rise by the same net income (as cash, or as the receivables/inventory it's tied up in). If net income only hit one side, the sheet would break.

**C5. "What is a circular reference in a model, and how do you manage it?"**

It arises when interest is computed on average debt that includes a cash-sweeping revolver: interest affects net income, which affects cash, which affects the revolver, which affects interest. Excel resolves it only with iterative calculation enabled. I manage it with a circularity switch — a cell that, set to zero, forces interest to a fixed value and breaks the loop. When the check breaks, I flip the switch off, fix the genuine logic error, then switch it back on. That isolates real errors from circularity artifacts like stray zeros or `#REF!` values.

**C6. "If a model balances, is it correct? Why or why not?"**

Not necessarily. Balancing proves the reconciliation between successive balance sheets is complete — no missing or mis-signed cash flows — but it says nothing about whether the inputs are right. Overstate revenue and both cash and retained earnings move together, so the identity still closes around a wrong figure. Balancing is a structural check, not an accuracy check; you still validate assumptions, margins, and ratios separately.

---

## Section D — Common-Error Spotting

For each, identify the error and the tell-tale signature.

**D1.** A model links Year 1 balance-sheet cash to a typed value of 30 rather than to `=CashFlow!EndingCash`. The check reads zero. What's wrong?

Cash is *plugged*. The check is green only by coincidence (the typed number happens to match). The moment any driver flexes, cash won't update and the model breaks silently. Signature: a blue (hard-coded) cell in a forecast column where every other cell is a black link. Fix: link cash to the cash flow statement's ending cash.

**D2.** Dividends of 20 are recorded in the equity roll-forward (RE reduced) but omitted from CFF. The check reads **+20**. Diagnose.

An omitted cash flow. Retained earnings correctly dropped 20, but cash was never reduced, so assets are high by exactly the omitted amount. Signature: imbalance = 1× a known schedule figure. Fix: add the dividend line to CFF.

**D3.** A debt repayment of 60 is entered in CFF as **+60** instead of −60. The debt schedule correctly shows the balance falling by 60. The check reads **+120**. Diagnose.

A sign flip. Removing the correct −60 and adding a wrong +60 is a 120 swing; cash is overstated by 120 while debt correctly declined. Signature: imbalance = exactly 2× a schedule figure — the hallmark of a flipped sign, not an omission. Fix: correct the sign in CFF.

**D4.** Across Years 1–4 the imbalance is +15, +33, +52, +70 — growing each year. Diagnose.

Broken roll-forward chaining: a beginning balance (likely retained earnings, PP&E, or debt) is not linked to the prior period's ending balance, so a fresh discrepancy accumulates each period. Signature: an imbalance that enlarges period after period rather than staying constant. Fix: re-establish every beginning-equals-prior-ending link.

**D5.** Depreciation of 70 is added back in CFO, but the PP&E roll-forward subtracts 60. The check is off by **10**. Diagnose.

Inconsistent depreciation — the cash flow statement and the PP&E schedule reference different figures. Net PP&E is 10 too high relative to the cash added back. Signature: imbalance = the difference between the two depreciation numbers. Fix: point both the CFO add-back and the PP&E roll-forward at the *same* depreciation cell.

**D6.** The same working-capital increase in inventory is captured once in CFO and again mistakenly in CFI. The check is off by the inventory change. Diagnose.

Double-counting: one movement hit the cash flow statement twice, over-reducing cash. Signature: imbalance = the doubled amount. Fix: record each change on exactly one line.

**D7.** A modeller enters accounts payable on the balance sheet as **−120** to "net it against receivables," and the totals no longer tie even though every schedule is correct. Diagnose.

A sign-convention violation on the balance sheet itself. All balance-sheet items must be positive; signs belong on the cash flow statement. The negative liability corrupts total L+E. Fix: show AP as +120.

**D8.** With a revolver-and-interest circularity, iterative calculation is turned off and the check shows scattered non-zero values with a few `#REF!` cells. Is this a logic error?

Likely not — it's a circularity artifact. With iteration disabled, Excel can't resolve the interest-cash-revolver loop and emits zeros or `#REF!` that masquerade as balance errors. Signature: the imbalance appears only with iteration off. Fix: enable iterative calculation, or flip the circularity switch off to test the logic, then re-enable.

---

*Self-check note: every Section B build was verified to reconcile (check = 0), and Section D's magnitudes follow the 1× (omission) / 2× (sign flip) / growing (broken chain) rules. Reproduce them cell-for-cell in Excel and expect exact agreement — whole numbers, no rounding.*
