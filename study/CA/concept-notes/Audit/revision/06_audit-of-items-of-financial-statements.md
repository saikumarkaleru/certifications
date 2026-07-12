# Audit of Items of Financial Statements

## Snapshot

The financial statements are not one claim but hundreds of **assertions**, and each can be false in a different way. Double-entry means profit can be flattered by inflating the asset/income side OR deflating the liability/expense side — so **motive gives every misstatement a direction**. **Assets & income → audit for OVERSTATEMENT** (test recorded items for reality, ownership, value). **Liabilities & expenses → audit for UNDERSTATEMENT** (search for what's missing). The evidence must match the *nature* of the assertion. Where an assertion is chronically abused, ICAI hard-coded a dedicated SA (501 inventory/litigation, 505 confirmations, 540 estimates, 510 opening balances). Effort scales to **risk x materiality (SA 320)**. Item audit is risk assessment (SA 315) and response (SA 330) applied figure by figure; substantive procedures can never be skipped entirely (SA 330 para 18) because of management override.

## Core concepts

- **Assertion is the hinge** between risk and procedure: *for this item, which assertion is most likely false, in which direction, because of whose motive? → that is the risk → choose the procedure that disproves that assertion.* Never jump item → procedure.
- **Three assertion families:** Classes of transactions (Occurrence, Completeness, Accuracy, Cut-off, Classification, Presentation); Account balances (Existence, Rights & obligations, Completeness, Valuation & allocation, Classification, Presentation); Presentation & disclosure.
- **Existence vs Occurrence:** Existence = is the asset here at reporting date? (inspect). Occurrence = did the transaction happen in the period? (vouch to dispatch). Ghost machine fails Existence; fictitious sale fails Occurrence.
- **Completeness is genuinely harder than Existence:** missing items are not in the records to sample — must find an independent complete population OUTSIDE the ledger (GRN register, bank statement, post-year-end payments). This is why "search for unrecorded liabilities" is a named technique.
- **"Audit for overstatement" = primary thrust, not only-recorded-items.** The reverse direction survives at lower risk. Risk is degree and direction, not binary.

## Key provisions / SAs

### Seven procedure verbs (SA 500 A14–A25)
| Verb | Best proves |
|---|---|
| Inspection (records/assets) | Existence; supports Valuation |
| Observation | Existence + process effectiveness (e.g. the count) |
| External confirmation | Existence + Rights (independent third party) |
| Recalculation | Accuracy, Valuation |
| Reperformance | Whether a control worked |
| Analytical procedures | Completeness, Accuracy (screening) |
| Inquiry | **Weak alone — always corroborate** |

**Inquiry is never sufficient on its own** (SA 500). Vouch = Occurrence; Trace = Completeness; Inspect = Existence; Confirm = Existence + Rights; Recompute = Valuation.

**SA 500 reliability ladder:** auditor's own direct knowledge > external obtained directly by auditor > external held by entity > internal (strong controls) > internal (weak controls/photocopy/oral). Originals beat photocopies. External evidence more reliable only if it reaches the auditor without passing through interested hands (why SA 505 insists the auditor controls confirmation mail).

### Governing standards carried into every item
SA 315 (assertions/risk), SA 320 (materiality), SA 330 (responses; substantive mandatory for each material item), SA 450 (aggregate misstatements), SA 500 (evidence), SA 501 (inventory/litigation/segments), SA 505 (confirmations), SA 510 (opening balances), SA 520 (analytics), SA 530 (sampling), SA 540 (estimates), SA 550 (related parties), SA 560 (subsequent events), SA 570 (going concern), SA 580 (written reps — corroborative, **never a substitute** for evidence reasonably obtainable).

### Item-by-item: assertion at risk → signature procedure

**Revenue** — Occurrence, Cut-off (also Accuracy, Completeness). **SA 240 rebuttable presumption of fraud in revenue recognition.** Tricks: fictitious sales (Occurrence), cut-off manipulation. Procedures: vouch to order/dispatch challan/gate register/customer acknowledgement; cut-off testing; analytics (margin, month-wise, post-year-end returns = channel-stuffing); test credit notes after year-end; confirm year-end large customers; review policy vs **Ind AS 115 five-step model** (identify contract → performance obligations → transaction price → allocate → recognise on satisfaction). Edge cases: **bill-and-hold** (recognise only if substantive reason, goods separately identified as customer's, ready to transfer, seller can't redirect); **principal vs agent** (agent recognises net commission, not gross). **Direction reversal — cash business** (jeweller/restaurant): motive flips to suppressing sales for tax → **Completeness/understatement**; analytics of margins, stock-to-sales reconciliation.

**Purchases & Expenses** — Completeness + Cut-off (profit inflation via omitting/deferring); Occurrence (fictitious/personal spend). Procedures: **search for unrecorded liabilities** (post-year-end payments, un-entered invoices); vouch to PO/GRN/invoice/payment; purchase cut-off (goods received before year-end must hit both purchases AND closing inventory); analytical review; capital vs revenue classification. **Three-way match** (PO + GRN + invoice) — fictitious purchase usually lacks the GRN. Capital vs revenue is **bidirectional**: revenue-expense capitalised overstates profit; capital item expensed (tax-driven) understates profit + asset.

**PPE** — Existence, Valuation, Rights, Completeness of additions/disposals. Procedures: verify additions to invoice/board approval/only directly attributable cost (Ind AS 16); physical inspection reconciled to fixed asset register; recompute depreciation (SA 540 — depreciation is an estimate; starts when **available for use**, not first used); test disposals; examine title deeds (Schedule III title-deed disclosure); impairment (Ind AS 36); charges/mortgages. **Register walk two directions:** register-to-floor tests **Existence** (ghost assets); floor-to-register tests **Completeness** (unrecorded/expensed assets). **Directly attributable cost includes** purchase price net of discount, site prep, delivery, installation, professional fees, dismantling/restoration; **excludes** admin overheads, initial operating losses, training, costs after ready-for-use. **Component accounting:** significant components with different lives depreciated separately. **Impairment: recoverable amount = HIGHER of (fair value less costs of disposal, value in use).** If asset can't generate cash independently → test the **cash-generating unit (CGU)**. Revaluation model → whole class, not cherry-picked.

**Inventory** — Existence (headline), Valuation, Rights, Completeness, Cut-off. **Profit leverage:** COGS = Opening + Purchases − **Closing**; every rupee added to closing stock adds a rupee to profit. **SA 501** (when inventory material): (1) **attend physical count** — evaluate instructions, observe, inspect, test counts; (2) if count date differs from B/S date → procedures on intervening transactions (roll-forward/back); (3) if can't attend → count on alternative date + reconcile; (4) if attendance impracticable → alternative procedures (inspect subsequent sales of pre-counted items); if impossible → **modify opinion (scope limitation)**; (5) inventory held by **third parties** → external confirmation (SA 505). **Test counts:** sheets → floor tests Existence of recorded items; floor → sheets tests Completeness of records (state the purpose). **Perpetual/continuous system** may replace year-end count if well-controlled; large unexplained cycle-count differences → full count needed. **Valuation:** cost vs NRV at the **lower**, **item by item** (Ind AS 2; healthy items cannot subsidise loss-makers; only similar/related items may be grouped); LIFO not permitted; test obsolete/slow/damaged; cut-off. **Cost includes** purchase cost net of discounts + conversion (labour + production overhead at **normal capacity**) + costs to bring to location/condition; **excludes** abnormal waste, storage (unless needed pre-further-processing), admin, selling costs.

**Trade Receivables** — Existence, Rights, Valuation (recoverability), Cut-off. Overstated to inflate assets / under-provided bad debts. Procedures: **External confirmation (SA 505)** — flagship; auditor controls send/receive. **Positive** (reply always) for material/risky; **Negative** (reply only if disagree) only if ALL four: (i) low RMM, (ii) large number of small homogeneous balances, (iii) very low expected exception rate, (iv) no reason recipients disregard. **Blank** positive (debtor fills the amount) — stronger, lower response. Non-response → **alternative procedures**: subsequent receipts matched to invoice (strongest), shipping docs + invoice + order, subsequent correspondence. Management refusal → evaluate reason, alternatives, unreasonable refusal = scope limitation. Test **provision/ECL (SA 540)** — age receivables. Watch **teeming and lading** (odd ageing though balances confirm).

**Investments** — Existence, Rights, Valuation, Presentation (current/non-current). Procedures: physical inspection or **custodian/depository confirmation (SA 505)** + DP statement; verify valuation (Ind AS 109/AS 13); classification; income accrual; charges/liens. **Fair-value hierarchy (Ind AS 113):** L1 quoted (hard to fudge), L2 observable, **L3 unobservable** (management model — valuation risk concentrates here, SA 540 bites, may use auditor's expert SA 620). **AS 13:** long-term at cost, written down only for **other-than-temporary** decline; current at **lower of cost and fair value**.

**Cash & Bank** — Existence, Completeness, Rights, Cut-off. Procedures: **bank confirmation (SA 505)** covering overdrafts/loans/liens/guarantees/unused facilities; BRR review (stale cheques, uncleared deposits); cash count (surprise, get written acknowledgement); receipts/payments cut-off. **Teeming and lading** = ongoing defalcation, lapping receipts (steal A's, cover with B's...) — attacks completeness of receipts. **Window dressing** = year-end cosmetic (record cheques issued but hold them → understate cash + payables to improve current ratio; related-party bridging deposit banked 31 Mar, bounces April) — attacks Cut-off/Presentation. One is theft, the other lying about the picture. Undispatched cheque is NOT a payment; liability still exists.

**Borrowings** — **Completeness (headline)**, Accuracy, Rights, Presentation/Classification, Cut-off (accrued interest). Procedures: confirm with lenders (SA 505); examine agreements (rate, security, covenants); verify charge registration with ROC; recompute + accrue interest at year-end; classify current vs non-current; check defaults (Schedule III/CARO). **Covenant breach at reporting date → loan is CURRENT** even if long tenure, unless lender waives on or before reporting date for >= 12 months; a waiver AFTER year-end does not save classification. Cascades to going concern (SA 570). Interest **accrues with time, not payment due date**.

**Trade Payables** — **Completeness (headline)**, Existence, Cut-off, Accuracy, Presentation. Signature risk: understatement through omission; vouching is blind — must **search for unrecorded liabilities** (post-year-end payments, unmatched GRNs, supplier statements, un-entered invoices). Reconcile supplier statements. **Confirm SMALL/nil balances with high purchase activity** (not large ones) — sampling inverts with risk direction. Purchase cut-off. **MSME dues** disclosure (principal + interest) per MSMED Act/Schedule III; unpaid MSME interest accrues by law = unrecorded liability.

**Provisions & Contingent Liabilities (SA 540 + SA 501)** — Completeness, Valuation, Presentation. Risk: under-provide (inflate profit) or over-provide (cookie-jar smoothing); contingents understated/undisclosed. **Ind AS 37 / AS 29 spine — PROVIDE only if all three:** (i) present obligation (legal/constructive) from past event; (ii) outflow **probable (>50%)**; (iii) reliably estimable. Only **possible** or not measurable → **DISCLOSE** as contingent liability. **Remote** → do nothing. Procedures: understand estimate method/assumptions; recompute + independent estimate/range; **subsequent events (SA 560)**; litigation → review board minutes + legal ledgers + **direct communication with legal counsel (SA 501)**. Hunt **management bias** (estimates clustered at favourable extreme). **Warranty** = expected-value (probability-weighted) for a large population; a **single** obligation uses most-likely outcome. **Onerous contract** provided at lower of cost-to-fulfil and exit penalty; **anticipated future operating losses NOT provided** (no past event).

**Equity/Share Capital & Reserves** — Occurrence/Rights, Accuracy, Presentation, Completeness of disclosure. Lower fraud risk, high compliance/authorisation. Procedures: verify movements to board/shareholder resolutions, MOA/AOA, ROC filings, register of members; check compliance (buy-back Sec 68, further issue Sec 62, reduction); securities premium used only for permitted purposes; dividends per Sec 123; reconcile reserves. **Securities premium (Sec 52) permitted uses:** fully paid bonus shares, write off preliminary expenses, write off share/debenture issue expenses/commission/discount, premium on redemption of RPS/debentures, buy-back. **Dividend (Sec 123):** deposit in separate account within 5 days; unpaid → Unpaid Dividend Account within 30 days; unclaimed 7 years → IEPF (with shares).

### SA 450 aggregation
Accumulate all misstatements above trivial threshold; evaluate individually AND in aggregate against materiality. Small individually-immaterial errors can sum to material (e.g. cut-off 16 + unrecorded expenses 18 + inventory 10 + under-provision 56 = 100 lakh). A candidate who fixes each in isolation but never sums them misses the point.

## Exam traps & must-remember

- **Wrong-direction test** — vouching payables earns no marks; want search for unrecorded liabilities. Confirm large receivables but SMALL/nil high-activity payables.
- **Vouching vs tracing** — vouch (record→doc) = Occurrence/Existence; trace (doc→record) = Completeness.
- **Existence vs Occurrence** — balance-date fact vs transaction-in-period.
- **Inquiry never alone (SA 500); written reps (SA 580) corroborate, never originate.**
- **SA 240 revenue presumption** — always invoke; flip to understatement in a cash business.
- **SA 501 escape hatch** — don't qualify immediately; go alternative date → alternative procedures → qualify only if evidence still unobtainable.
- **External confirmation control** — auditor sends/receives; refusal → evaluate + alternatives + maybe scope limitation.
- **Negative confirmations need all four conditions.**
- **Lower of cost/NRV item-by-item** — healthy items can't subsidise loss-makers.
- **Impairment uses HIGHER of FVLCD and VIU** (recoverable amount); never write up under cost model.
- **Netting prohibited** — debit balances in payables and credit in receivables reclassified; overdraft = borrowing not negative cash.
- **Cut-off bidirectional** — goods received before year-end hit both inventory AND creditors.
- **Accrual != payment due date** — interest accrues with time.
- **Adjusting vs non-adjusting subsequent events (SA 560)** — post-year-end insolvency/court ruling on a pre-existing condition = **adjusting** (change numbers).
- **Physical inspection proves Existence, not Rights** — still need title deeds; counting stock doesn't prove ownership (consignment) or NRV.
- **Selective revaluation prohibited** — whole class of PPE.
- **Window dressing vs teeming and lading** — cosmetic year-end vs ongoing lapping defalcation.
- **Anticipated future operating losses not provided; onerous contract is.**
- **Covenant waiver after reporting date** does not prevent current classification.

## One-line recall

- Assets & income → audit for OVERSTATEMENT; liabilities & expenses → audit for UNDERSTATEMENT.
- Vouch = Occurrence; Trace = Completeness; Inspect = Existence; Confirm = Existence + Rights; Recompute = Valuation.
- Completeness can only be tested from a population outside the ledger — hence "search for unrecorded liabilities".
- The sample must be chosen for the direction of the lie: large balances for overstatement, small/nil high-activity for understatement.
- SA 501 ladder: attend count → alternative date + roll-forward → alternative procedures → qualify; inventory lower of cost/NRV item-by-item.
- Provision tree: present obligation + probable + reliably estimable → provide; possible → disclose; remote → ignore; impairment at higher of FVLCD and VIU.
- SA 450: aggregate all misstatements before judging the opinion; inquiry never stands alone.
