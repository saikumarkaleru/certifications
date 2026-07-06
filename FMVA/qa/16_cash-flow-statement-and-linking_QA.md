# Q&A — The Cash Flow Statement and Linking the Three Statements

Practice bank for Chapter 16. Work each question before reading the answer. The build problems use clean numbers you can reproduce cell-for-cell in Excel; every statement reconciles — the indirect total ties to the identity ΔCash = ΔL + ΔE − ΔNon-cash assets, and ending cash closes the balance sheet. Sign rule throughout: assets `=-(current−prior)`, liabilities `=+(current−prior)`, non-cash expenses added back. Figures in $000s.

---

## Section A — Concept Checks (test the WHY)

**A1. Why can a company report $50m of profit and still go bust the same year?**

Because profit is an *accrual* number and solvency is a *cash* number, booked on different clocks. Revenue is recognised when earned, expense when incurred — regardless of when cash moves. A firm can book $50m of profit yet collect none of it (sales sitting in receivables), pour $80m into a factory (capex never touches the P&L directly), or repay a maturing loan (a balance-sheet event). Each drains cash without touching net income. The cash flow statement exists to measure that gap between the profit story and the bank balance.

**A2. Why does the indirect method start from net income instead of listing actual cash receipts?**

Because it uses numbers you already have. The direct method needs every cash receipt and payment — internal treasury data a modeller rarely possesses. The indirect method takes net income (already on the income statement) and *adjusts it back to cash* using balance-sheet account changes (also already modelled): add back non-cash expenses, then add or subtract working-capital swings. It is the accrual-to-cash bridge built from data the model already contains.

**A3. Why is depreciation *added back* in CFO when it was a real expense that lowered profit?**

Because no cash left the building this year. Depreciation spreads a purchase whose cash actually went out *years ago*, recorded then as capex in CFI. It reduced net income without reducing cash, so to travel from net income back to cash you reverse it — add it straight back. It is the cleanest illustration of the method: strip out entries that moved profit but not money.

**A4. Why does an increase in an asset *subtract* from cash while an increase in a liability *adds* to it?**

It falls out of the identity ΔCash = ΔLiabilities + ΔEquity − ΔNon-cash assets. Intuitively: building an asset consumes cash — buy inventory and cash converts to goods; extend credit and you have earned revenue you have not yet collected, so profit overstates cash and you subtract the receivable growth. Growing a liability is the reverse — delay paying a supplier and you hold cash you would otherwise have parted with; borrow and cash comes in.

**A5. Why must cash on the balance sheet be a *link*, never a typed number?**

Because cash is the model's ultimate *output*, not an input. Ending cash is produced by the cash flow statement (beginning cash + net change), and that number is what balances the sheet. Hardcode it and the sheet may *look* balanced today but is dead — change any assumption and the cash consequence no longer flows, so the check silently breaks or stays zero on a stale number. Balance-sheet cash must always read `=CFS!EndingCash`.

**A6. Why does a correctly linked model *never* fail to balance — making the check a pure error detector?**

Because balance is a mathematical identity. Assets = Liabilities + Equity holds in both periods, so the *changes* balance too, and ΔCash is *fully determined* by the changes in every other account. Capture every non-cash movement correctly and ending cash *must* balance the sheet. So any non-zero check is proof of a linking error — correct arithmetic cannot violate the identity, and the size and column of the imbalance point at the culprit.

**A7. Why is the revolver "plug" legitimate modelling rather than a fudge to force balance?**

Because a correct model already balances without it — the identity guarantees that. The revolver models a *real financing decision*: draw the credit line when cash would dip below a minimum, repay when flush. The plug automates that economic choice. If your sheet only balances *because* the revolver absorbs an unexplained number, you have a linking error hiding inside the plug — it should be doing an economically real job, not masking a mistake.

**A8. Why does the revolver create a deliberate circular reference, and how is it handled?**

Interest on the revolver depends on the balance; the balance depends on the cash shortfall; the shortfall depends on cash flow, which includes interest — a loop. It is intentional, because that is the real economics. Handle it by enabling iterative calculation (File → Options → Formulas) and building a *circularity switch* — a cell that, set to 0, zeroes revolver interest so you can break the loop if the model errors out. Do not sever the interest link permanently; that understates financing cost.

---

## Section B — Build / Computational Problems

**B1. Build CFO from net income (indirect method).** FY2 data: Net income 2,000; Depreciation (from PP&E schedule) 500. Working-capital accounts: AR 900→1,100; Inventory 700→640; Accounts payable 400→520; Accrued expenses 200→260. Apply the sign rules and compute CFO.

| Line | Computation | Amount |
|---|---|---|
| Net income | given | 2,000 |
| Add: Depreciation | non-cash add-back | +500 |
| Change in AR | −(1,100 − 900) | −200 |
| Change in inventory | −(640 − 700) | +60 |
| Change in AP | +(520 − 400) | +120 |
| Change in accrued exp. | +(260 − 200) | +60 |
| **CFO** | sum | **2,540** |

Reading it: receivables grew (cash tied up); inventory fell (released cash); payables and accruals grew (holding cash). Net income of 2,000 became **2,540 of operating cash** — better than 100% conversion, driven by the depreciation add-back and a net inventory/payables release.

**B2. Complete the statement to ending cash and reconcile to the identity.** Continue FY2: CFO 2,540 (B1); Capex 900; Proceeds from equipment sale 100 (at book value); Long-term debt drawn 400; Debt repaid 250; Dividends 300; Beginning cash (FY1 ending BS cash) 600.

| Section | Line | Amount |
|---|---|---|
| CFO | | **2,540** |
| CFI | Capex | −900 |
| | Proceeds from asset sale | +100 |
| | **CFI total** | **−800** |
| CFF | Debt drawn | +400 |
| | Debt repaid | −250 |
| | Dividends | −300 |
| | **CFF total** | **−150** |
| | **Net change in cash** | **+1,590** |
| | Beginning cash | 600 |
| | **Ending cash** | **2,190** |

Net change = 2,540 − 800 − 150 = **1,590**. Ending cash = 600 + 1,590 = **2,190**, written to the FY2 balance-sheet cash line.

**Independent reconciliation** via ΔCash = ΔL + ΔE − ΔNon-cash assets:
- ΔNon-cash assets: AR +200, Inventory −60, net PP&E = capex 900 − depreciation 500 − NBV of asset sold 100 = +300. Total = **440**.
- ΔLiabilities: AP +120, accruals +60, debt +(400 − 250) = +150 → **330**.
- ΔEquity: net income 2,000 − dividends 300 = **+1,700**.
- ΔCash = 330 + 1,700 − 440 = **+1,590** ✓

The identity reproduces +1,590 exactly, so the statement reconciles and ending cash of 2,190 will balance the sheet.

**B3. The revolver plug — a shortfall year.** FY3, a heavy investment year: beginning cash (FY2 ending) 2,190; pre-revolver cash flow (CFO + CFI + CFF *excluding* the revolver) = −2,500; minimum cash 250; revolver beginning balance 0. Does it draw, how much, and what are ending cash and the revolver balance?

Projected cash before revolver = 2,190 − 2,500 = **−310**, below the 250 minimum (and below zero — impossible to hold).

$$\text{Draw} = \max(0,\; 250 - (-310)) = \max(0,\; 560) = \textbf{560}$$

The revolver draws **560**, added to CFF:
- Net change in cash = −2,500 + 560 = **−1,940**
- Ending cash = 2,190 − 1,940 = **250** (exactly the floor, as designed)
- Revolver balance on the FY3 balance sheet = 0 + 560 = **560**

The +560 of debt and the 250 cash floor together keep the sheet balanced while modelling the real decision to tap the credit line.

**B4. The revolver flips to a paydown.** FY4 throws off surplus: beginning cash 250; pre-revolver cash flow +800; minimum cash 250; revolver beginning 560 (from B3). Compute the paydown.

Projected cash = 250 + 800 = 1,050; surplus above minimum = 800. Repay = `MIN(revolver 560, MAX(0, 800))` = **560** — the `MIN` caps repayment at what is owed, so it cannot over-repay into a negative balance. Revolver change = −560; net change = 800 − 560 = +240; ending cash = **490**; revolver balance = **0**. The same plug logic runs in reverse: draw to the floor when short (B3), sweep down the balance when flush.

**B5. Prove the balance sheet balances — the retained-earnings and cash links.** Using FY2 from B1–B2, roll the accounts forward and confirm the check. FY1 (prior) balances: Cash 600, AR 900, Inventory 700, Net PP&E 4,000, AP 400, Accrued 200, Long-term debt 1,000, Common stock 1,500, Retained earnings 3,100 (assets 6,200 = L 1,600 + E 4,600).

Roll forward to FY2:
- Cash = 2,190 (CFS ending, B2); AR 1,100; Inventory 640; AP 520; Accrued 260 (B1)
- Net PP&E = 4,000 + capex 900 − depreciation 500 − disposal NBV 100 = **4,300**
- Long-term debt = 1,000 + 400 − 250 = **1,150**
- Retained earnings = 3,100 + net income 2,000 − dividends 300 = **4,800**; Common stock = 1,500 (no issuance)

| | FY1 | FY2 |
|---|---|---|
| Cash | 600 | 2,190 |
| Accounts receivable | 900 | 1,100 |
| Inventory | 700 | 640 |
| Net PP&E | 4,000 | 4,300 |
| **Total assets** | **6,200** | **8,230** |
| Accounts payable | 400 | 520 |
| Accrued expenses | 200 | 260 |
| Long-term debt | 1,000 | 1,150 |
| Common stock | 1,500 | 1,500 |
| Retained earnings | 3,100 | 4,800 |
| **Total L + E** | **6,200** | **8,230** |
| **Balance check (A − L − E)** | **0** | **0** ✓ |

The check is exactly 0 — not forced, but a consequence of the three links: ending cash → BS cash, net income − dividends → retained earnings, and the PP&E/debt rolls. Break one to see the diagnostic: leave RE at 3,100 and the check reads −2,000, pointing straight at the equity roll.

**B6. Derive unlevered free cash flow from the statement.** FY2: EBIT 2,800; tax 25%; depreciation 500; capex 900; ΔNWC +100. Compute unlevered FCF = EBIT × (1 − t) + D&A − Capex − ΔNWC.

- NOPAT = 2,800 × 0.75 = **2,100**; + D&A 500 − Capex 900 − ΔNWC 100
- Unlevered FCF = 2,100 + 500 − 900 − 100 = **1,600**

Every component is a re-cut of the CFS: D&A and ΔNWC are the CFO adjustments, capex is CFI. The difference is that unlevered FCF starts from EBIT (before interest), not net income, because a DCF discounts cash to all capital providers at the WACC — start from net income and you double-count or omit the interest tax shield.

---

## Section C — Interview-Style Questions (model answers)

**C1. "Walk me through the three statements and how they link."**

The income statement runs revenue to net income. Net income flows two ways: into retained earnings on the balance sheet, and into the top line of CFO. On the cash flow statement I rebuild cash from net income — add back non-cash items like D&A, adjust for working-capital changes (movements in operating balance-sheet accounts), then layer in investing (capex, disposals) and financing (debt, equity, dividends). The sections sum to net change in cash; plus beginning cash gives ending cash, written back to balance-sheet cash. Meanwhile capex and D&A drive the PP&E schedule, debt flows the debt schedule, net income less dividends the equity roll. One row validates it all: assets minus liabilities minus equity must equal zero every period.

**C2. "A $10 increase in depreciation — walk it through all three statements, 25% tax rate."**

Income statement: pre-tax income falls 10, tax falls 2.5, net income falls 7.5. Cash flow statement: net income down 7.5, but add back the full 10 of non-cash depreciation, so CFO *rises* 2.5 — exactly the tax shield, the cash tax saved by sheltering income. Balance sheet: cash up 2.5; net PP&E down 10, so assets net to −7.5; retained earnings down 7.5 via lower net income. Both sides fall 7.5 and it still balances. Headline: depreciation, though an expense, is *cash-positive* through the tax shield.

**C3. "Why does the indirect method dominate the direct method in modelling?"**

Because the inputs already exist. The direct method needs actual cash receipts and disbursements — treasury-system data, not published statements. The indirect method rebuilds operating cash from net income plus balance-sheet account changes, both already forecast. It is also more useful analytically: it shows the bridge from accrual profit to cash, exposing exactly how much cash working capital and non-cash charges consume or release. That reconciliation is what an analyst wants.

**C4. "What is a cash sweep, and how does it relate to the revolver plug?"**

The revolver plug is two-way: draw when below minimum cash, repay when flush. A cash sweep is its aggressive LBO cousin — instead of letting surplus cash accumulate, it *forces* excess cash to prepay debt down a priority waterfall (revolver, then term loans, then subordinated tranches). Same mechanic, but mandated by the credit agreement and applied by seniority. Both create the same intentional circularity, since prepaying debt lowers interest, which changes cash available to sweep.

**C5. "Your balance sheet is off by exactly net income. Where do you look first?"**

The retained-earnings link. If the check equals net income (or net income minus dividends), retained earnings is probably not rolling forward as prior RE + net income − dividends — the net income line was never added, dividends were double-counted, or RE is hardcoded. It is a signature error: the imbalance equals the number that failed to flow. Other signatures: off by twice a working-capital swing → a flipped CFO sign; off by a growing amount each year → beginning cash mislinked to the wrong column.

**C6. "How does the cash flow statement feed a DCF valuation?"**

Directly — free cash flow is a re-cut of it (see B6): unlevered FCF pulls D&A and ΔNWC from CFO and capex from CFI, but starts from EBIT rather than net income to stay financing-neutral. So the CFS is a prerequisite for any DCF, and the most common valuation error — forgetting to fund the working-capital build in a high-growth phase — is precisely a CFS mistake.

---

## Section D — Common-Error Spotting (what is wrong?)

**D1. Working-capital sign flip.** A model writes the change-in-AR line as `=+(AR_this − AR_prior)`. In B1 that adds +200 to CFO instead of −200. Why does the balance sheet break, and by how much?

An asset increase is a *use* of cash, so it must subtract: correct is `=-(AR_this − AR_prior)` = −200. Writing +200 injects a 400 error into cash. Since ending cash is the balance-sheet plug, the check is off by exactly 400 — twice the swing. Fix: mechanically, assets `=-(current−prior)`, liabilities `=+(current−prior)`, never eyeball. This is the most common model-breaker; when the check is off by an even, round number, suspect a flipped WC sign first.

**D2. Hardcoded cash on the balance sheet.** An analyst types the FY2 cash figure onto the balance sheet instead of linking to CFS ending cash. The check reads 0 today. What is wrong?

The model looks alive but is dead. Cash is an *output* of the CFS; hardcoding it severs the loop, so when any upstream assumption moves — margins, capex, WC days — the cash consequence never reaches the balance sheet. The check then breaks, or stays zero on a stale number. Fix: balance-sheet cash must always be `=CFS!EndingCash`, and CFS beginning cash must reference the prior year's balance-sheet cash, chaining the periods.

**D3. Depreciation entered twice with two values.** D&A is typed as 500 on the income statement and 480 in the CFO add-back. The balance sheet is off by 20. Diagnose.

D&A must be *one* source — the PP&E schedule — linked to the income-statement expense, the CFO add-back, and accumulated depreciation. Two typed copies drift: net income was cut by 500 but only 480 added back, leaving cash short by 20. Fix: compute D&A once in the PP&E roll-forward and reference it everywhere with `=Sheet!Cell`. Never retype a number that already lives somewhere.

**D4. Beginning cash mislinked.** In a multi-year model, FY3 beginning cash points at FY1's ending cash instead of FY2's. Each later year looks progressively more wrong. Why?

Beginning cash must reference the *immediately prior* period's ending cash — that is what chains the statements through time. Pointing FY3 at FY1 skips FY2's net change, so FY3 ending cash is wrong by that amount, and every later year compounds it. The check breaks by a *growing* amount each year — the signature that distinguishes it from a static sign error. Fix: beginning cash in each column = prior column's ending cash; drag one formula across so the reference steps consistently.

**D5. Double-counted capex.** A modeller enters capex as −900 in CFI *and* separately types 900 into the PP&E schedule as an independent assumption. Later someone changes the CFI capex to 1,000 but forgets the schedule. What breaks?

Capex is *one* assumption linked to both uses — the CFI line and the PP&E roll-forward (`Ending PP&E = Beginning + Capex − Depreciation − Disposals`). Two separate hardcodes diverge: CFI now cuts cash by 1,000 while PP&E grows by only 900, so the sheet is off by 100. Fix: put capex in one cell, reference it from both. Same discipline for debt draws (CFF ↔ debt schedule) and dividends (CFF ↔ equity roll).

**D6. Revolver forced to hide an error.** A model won't balance, so the analyst wires the revolver to plug whatever makes the check zero — it "draws" 47 in a strong cash year with no shortfall. Why is this a review failure?

The revolver has become a fudge, not an economic decision. A correctly linked model balances *without* the plug, so a revolver drawing an odd number in a surplus year is masking a real linking error (flipped sign, missing add-back, broken RE roll). Fix: drive the revolver only by its own logic — draw to reach minimum cash when short, repay when flush. If it is doing anything else to balance the sheet, hunt the real bug.

**D7. Non-cash items beyond D&A ignored.** A software firm expenses $300 of stock-based compensation, but the CFO section only adds back depreciation. CFO looks low and the sheet is off by 300. What is missing?

Stock-based compensation is non-cash — it cut net income but no cash left (settled in equity). It must be added back in CFO like depreciation, with its counterpart (paid-in capital) rising 300. Omitting the add-back understates CFO by 300, and with the equity credit also missing, the sheet is off by 300. Same for deferred taxes and write-downs. Fix: sweep *all* non-cash charges into the CFO add-back, each paired with its balance-sheet movement.

---

*Master check: from a blank sheet, can you (1) rebuild CFO from net income with correct WC signs, (2) add CFI and CFF to reach ending cash, (3) verify it independently via ΔCash = ΔL + ΔE − ΔNon-cash assets, (4) link ending cash and retained earnings to the balance sheet, and (5) watch the check snap to 0 in every column without a single hardcode? If yes, you own this chapter — and you are ready to build FCF and a DCF on top of it.*
