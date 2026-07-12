# Tax Invoice, Credit & Debit Notes — Secs 31–34, Rules 46–55A

## Snapshot
GST runs on a chain of documents, not trust. The tax invoice is the pivot: simultaneously the supplier's output-tax evidence AND the recipient's sole basis for ITC. Other documents are substitutes (bill of supply, vouchers, challan), correctors (credit/debit notes), or authenticators (e-invoicing). Three-question filter for "which document?": (1) supply or just money/movement? (2) taxable in this supplier's hands? (3) who charges — supplier or RCM recipient?

## Core concepts
- One document, two mirror consequences: fixes supplier's output tax + authorises buyer's ITC.
- Match document to truth of event; wrong document = false claim.
- Never erase — always link & reverse (credit/debit notes carry original invoice reference).
- Document is not the tax but fixes it: invoice date is usually the earliest time-of-supply trigger.
- Supplier issues everything (including credit/debit notes). Sole exception: RCM self-invoice from unregistered supplier.

## Key provisions / rules

### Tax invoice — Sec 31 + Rule 46 (issue time limits)
| Supply | Time limit |
|---|---|
| Goods (movement) | Before/at REMOVAL [31(1)(a)] |
| Goods (no movement) | Before/at delivery/making available |
| Services | Within 30 days of supply (45 days banks/insurers/NBFCs) [31(2)+Rule 47] |
| Continuous supply of goods | On/before each statement/payment [31(4)] |
| Continuous supply of services | By due date of payment / at receipt / on event [31(5)] |
| Cessation of continuous service | At time supply ceases [31(6)] |
| Sale-or-return (approval) | Earlier of supply or 6 months from removal [31(7)] |

Continuous supply [2(32)/(33)] = recurrent under contract > 3 months with periodic payment.
"Removal" [2(96)] = dispatch by supplier OR collection by recipient (ex-works truck triggers invoice).

Rule 46 particulars (hook WHO-WHAT-HOW MUCH-WHERE-SIGNED): supplier GSTIN; consecutive serial (≤16 chars, unique/FY); date; recipient GSTIN; unregistered & value > ₹50,000 → name/address/State; HSN/SAC; description; quantity; total value; taxable value (post-Sec 15 discount); rate (each head); tax amount (each head); place of supply + State; delivery address if different; RCM flag; signature. Plus e-invoice QR/IRN; export/SEZ endorsement.

Manner of issue [Rule 48]: Goods → TRIPLICATE (Recipient/Transporter/Supplier); Services → DUPLICATE (Recipient/Supplier).
HSN digits: turnover ≤₹5cr → 4 digits; >₹5cr → 6 digits (B2B). Verify slabs.
Small value < ₹200: consolidated day-end invoice IF recipient unregistered AND doesn't require invoice (both).
Revised invoice [31(3)(a)+Rule 53]: between effective date of registration & grant of certificate; mark "Revised Invoice", cross-reference original; consolidated for unregistered (State-wise), separate for each registered recipient.

### Bill of supply — Sec 31(3)(c) + Rule 49
By composition dealer (legend "composition taxable person, not eligible to collect tax on supplies") & exempt supplier. NO tax shown. Composition legend applies to ALL their supplies; a normal dealer uses bill of supply only for exempt lines (or invoice-cum-bill of supply, Rule 46A).

### Vouchers — Sec 31(3)(d)–(g)
| Document | When | By | Section |
|---|---|---|---|
| Receipt voucher | Advance received | Supplier | 31(3)(d)+Rule 50 |
| Refund voucher | Advance refunded, no invoice ever issued | Supplier | 31(3)(e)+Rule 51 |
| Payment voucher | RCM payment to supplier (whether registered or not) | Recipient | 31(3)(g)+Rule 52 |
| Self-invoice | RCM from UNREGISTERED supplier | Recipient | 31(3)(f) |
If rate/place unknown at advance: treat rate 18%, supply inter-State. Consolidated month-end self-invoice allowed.
RCM matrix: unregistered supplier → self-invoice YES + payment voucher YES; registered supplier → self-invoice NO + payment voucher YES.

### Delivery challan — Rule 55
Movement with no supply/invoice: quantity unknown at removal, job work, inter-branch/stock transfer, exhibition, SKD/CKD. Triplicate (consignee/transporter/consignor).
Rule 55(5) SKD/lots: complete invoice before FIRST consignment, delivery challan per subsequent consignment (+certified copy of invoice), ORIGINAL invoice travels with LAST consignment.

### Credit & Debit Notes — Sec 34 (always by SUPPLIER)
Credit note [34(1)/(2)] — invoice OVER-stated: over-billing, goods returned, deficient, post-supply discount (Sec 15(3)(b)). Reduces output tax ONLY IF recipient correspondingly reduces ITC (symmetry) AND no unjust enrichment (for non-ITC recipients, tax not passed on).
Declare by 30 Nov following FY of original supply OR annual return date, whichever earlier. After deadline → commercial credit note only, no tax reduction.
Debit note [34(3)/(4)] — invoice UNDER-stated. Increases output tax. NO time limit to issue. Includes supplementary invoice. Recipient's ITC clock runs from debit note's own FY (Sec 16(4)).
Consolidated credit/debit note against multiple invoices allowed (since 2019).
Commercial/financial credit note: if Sec 15(3)(b) not met or deadline passed → no GST reduction, no ITC reversal, supplier bears GST.
Contents [Rule 53]: supplier details, serial, date, corresponding invoice no(s), taxable value, tax adjusted, legend "Credit Note"/"Debit Note".

### E-invoicing — Rule 48(4)
Own-system JSON (INV-01) → upload to IRP → IRP returns IRN (64-char hash) + signed QR. Only then a valid tax invoice; no IRN where required → invalid → recipient loses ITC. Applies to B2B + exports + credit/debit notes where aggregate turnover > ₹5cr in ANY FY from 2017-18 (verify). B2C excluded (large taxpayers show dynamic QR — separate, no IRN). Exempt: banks/NBFCs, insurers, GTAs, passenger transport, cinema/multiplex, SEZ units (not developers), govt. Obligation, once triggered by a past FY, doesn't switch off if turnover falls.

## Worked mini-example
S sells to registered R: value ₹1,00,000 + IGST ₹18,000 (5 May 2025). R returns ₹40,000 (defective) on 20 Jun. S issues credit note ₹40,000 + IGST ₹7,200; reduces output tax to ₹10,800 ONLY because R reverses ₹7,200 ITC. Declare by 30 Nov 2026. If return on 15 Dec 2026 (past deadline) → commercial credit note only, S bears ₹7,200.

## Exam traps & must-remember
- Only the SUPPLIER issues credit/debit notes; a buyer's "credit note" has no GST effect.
- Credit note reduces tax only if recipient reverses ITC AND declared by 30 Nov deadline.
- Debit note: no issue-time-limit; recipient ITC clock from DN's FY.
- Goods invoice date = REMOVAL (incl collection by recipient), not delivery.
- Services 30 days; 45 only for banks/insurers/NBFCs.
- Composition/exempt → bill of supply (no tax).
- Post-supply discount reduces GST only if pre-agreed per Sec 15(3)(b) AND ITC reversed; else commercial CN.
- E-invoicing = authenticate via IRP, not generate on portal; no IRN → invalid → no ITC.
- One consolidated credit/debit note can cover many invoices.
- Goods → triplicate; services → duplicate.
- Refund voucher = advance never invoiced; credit note = invoiced then reversed.
- Self-invoice only when supplier unregistered; payment voucher for all RCM.
- Supplementary invoice = debit note in GST.
- SKD: one invoice before first consignment + challans for rest (Rule 55(5)), not multiple invoices.

## One-line recall
- Tax invoice = supplier output-tax evidence + recipient's sole ITC basis.
- Goods invoice ≤ removal; services ≤ 30 (45) days; sale-or-return ≤ 6 months.
- Supplier issues all notes; credit note reduces tax only with symmetry + by 30 Nov; debit note no time limit.
- Run three-question filter (supply? taxable? who charges?) to pick the document.
- E-invoice IRN+QR for B2B >₹5cr; no IRN → no valid invoice → no ITC.
- Refund voucher ≠ credit note; self-invoice only for unregistered RCM supplier.
