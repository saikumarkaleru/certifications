# GL / AP / AR Transaction Drills (with Entries)

## What you'll be able to do

You'll be able to post the everyday finance transactions of a company through SAP by T-code from memory, and — this is what separates an operator from a button-pusher — state the exact **Dr/Cr accounting entry with amounts** behind each posting *before* you hit save. You'll post a GL journal (FB50), a vendor invoice (FB60), a customer invoice (FB70), receive and make payments (F-28 / F-53), park for approval (FV50), display and drill into any document (FB03), read open items (FBL1N/FBL3N/FBL5N), and reverse a mistake (FB08). We'll carry one week of April transactions for **Acme India (company code 1000)** all the way through.

## The drill — step by step

**Setup for the example:** COA `CAIN`, currency INR, period 01/2026 open. GLs: 400000 Salaries, 401000 Rent, 160000 Trade Payables, 140000 Trade Receivables, 200000 Sales, 100000 Bank, 154000 Input GST, 175000 Output GST.

**1. Straight GL journal — `FB50` (Enter G/L Account Document).**
Screen: Document Date `05.04.2026`, Posting Date `05.04.2026`, Company Code 1000, Currency INR. Grid rows: G/L acct, D/C indicator (S=Debit, H=Credit), Amount, Cost Center (for P&L lines).
*Txn A — book April rent accrued, no invoice yet:*
- Row1: 401000 Rent, **S** 100,000, Cost Center FIN-DEL-200
- Row2: 240000 Rent Payable, **H** 100,000
Simulate (Shift+F9 / Document → Simulate), check the entry balances to 0, **Post (Ctrl+S)** → document number e.g. `100000123`.
**Entry:** Dr Rent 1,00,000 / Cr Rent Payable 1,00,000.

**2. Vendor invoice — `FB60` (Enter Incoming Invoice, FI only).**
Header: Vendor `V1000` (Sharma Supplies), Invoice date `06.04.2026`, Posting date, Amount `1,18,000` (incl GST), Calculate tax OFF (we post GST manually) or ON with tax code. Payment terms default from master.
GL tab lines:
- 402000 Office Supplies, **S** 1,00,000, Cost Center
- 154000 Input CGST/SGST, **S** 18,000
The vendor line (Cr 160000 Trade Payables 1,18,000) is generated **automatically** from the vendor master's reconciliation account.
**Entry:** Dr Office Supplies 1,00,000 + Dr Input GST 18,000 / Cr Vendor (Trade Payables) 1,18,000.
*(For procurement with a PO + goods receipt you'd use **MIRO** instead — the 3-way match invoice; FB60 is the FI-only direct invoice with no PO.)*

**3. Customer invoice — `FB70` (Enter Outgoing Invoice, FI only).**
Header: Customer `C2000` (Rao Retail), Amount `2,36,000`, invoice/posting date.
GL tab:
- 200000 Sales, **H** 2,00,000, Profit Center PC-RETAIL
- 175000 Output GST, **H** 36,000
Customer line Dr 140000 Trade Receivables 2,36,000 is auto-generated from the customer recon account.
**Entry:** Dr Customer (Trade Receivables) 2,36,000 / Cr Sales 2,00,000 + Cr Output GST 36,000.

**4. Incoming payment from customer — `F-28`.**
Header: posting date `20.04.2026`, Bank acct 100000, Amount received `2,36,000`, Value date. Under "Open item selection": Account `C2000`, Account type D (customer). Click **Process Open Items** → the ₹2,36,000 invoice shows; double-click to *activate* it so "Not assigned" = 0.00. Post.
**Entry:** Dr Bank 2,36,000 / Cr Customer 2,36,000 — and the invoice open item is **cleared** (fully applied).

**5. Outgoing payment to vendor — `F-53` (Post Outgoing Payments).**
Header: Bank acct 100000, Amount `1,18,000`. Open item selection: Account `V1000`, type K (vendor). Process open items → activate the ₹1,18,000 invoice → Not assigned 0.00 → Post.
**Entry:** Dr Vendor 1,18,000 / Cr Bank 1,18,000 — vendor open item cleared. (Bulk/automatic payments use the payment run **F110**.)

**6. Park for approval — `FV50` (park GL) / `FV60` (park vendor).**
Use when a junior enters but a senior must approve. Same screen as FB50 but you **Park (document not yet posted, no GL update)**. Approver opens `FBV0` to display/post parked docs, or `FV50` change → Post. Nothing hits the ledger until posting.

**7. Display line items — the reading tools.**
- `FBL1N` — Vendor line items (open/cleared/all). Filter V1000, "Open items at key date".
- `FBL3N` — GL line items. Filter 100000 Bank to see every movement.
- `FBL5N` — Customer line items. Filter C2000.
(These are the ECC classics; the S/4 apps are "Display Line Items – General Ledger/Supplier/Customer". FAGLL03 is the new-GL GL line item report.)

**8. Display any document — `FB03`.** Enter document number 100000123 / company code / fiscal year → see header, all line items, and via Environment → Document Environment the FI/CO postings.

**9. Reverse — `FB08` (Individual Reversal).** Enter the wrong document number, reversal reason (e.g. `01` reversal in current period, `02` reversal in closed → posts in current), posting date. Post → SAP creates a mirror document with debits/credits flipped and links the two. Mass reversal = `F.80`.

## The output — Acme April sub-ledger picture

| Doc | T-code | Dr | Cr | Amount |
|---|---|---|---|---|
| 123 | FB50 | Rent 401000 | Rent Payable 240000 | 1,00,000 |
| 124 | FB60 | Office Supp + Input GST | Vendor V1000 (160000) | 1,18,000 |
| 125 | FB70 | Customer C2000 (140000) | Sales + Output GST | 2,36,000 |
| 126 | F-28 | Bank 100000 | Customer C2000 | 2,36,000 |
| 127 | F-53 | Vendor V1000 | Bank 100000 | 1,18,000 |

Vendor V1000 open items after: **0** (invoice cleared by pmt). Customer C2000: **0**. Bank net movement: +2,36,000 − 1,18,000 = **+1,18,000**. GST: Input 18,000, Output 36,000 → net payable 18,000.

## Checks & gotchas

- **Every document must balance to zero** by company code and (with document splitting) by profit centre/segment — SAP won't post otherwise.
- Don't post directly to a **reconciliation account** (160000/140000) via FB50 — it's controlled only through the vendor/customer line. Trying gives "account is a reconciliation account, not allowed for direct posting."
- **Posting date drives the period**, not document date. Wrong posting date = wrong month = restated close.
- After F-28/F-53 confirm the item shows as **cleared** in FBL5N/FBL1N (clearing doc number populated). A payment that doesn't clear the invoice leaves *two* open items (a debit and a credit) — the classic "why is AR overstated" bug.
- FB60 vs MIRO: FB60 has no PO/GR match; using it where a PO exists breaks the 3-way match and leaves GR/IR dangling.
- FB08 with reason 01 fails if the original period is closed — use reason 02 to post the reversal in the current open period.

## Interview drill

**Q1. Walk me through a vendor invoice-to-pay in SAP.**
"PO in ME21N → goods receipt MIGO (Dr GR/IR clearing, Cr stock/expense) → invoice receipt MIRO doing the 3-way match PO-GR-Invoice (Dr GR/IR, Dr Input GST, Cr Vendor) → payment F110/F-53 (Dr Vendor, Cr Bank). For a non-PO/FI-only invoice I skip to FB60. I'd verify GR/IR nets to zero and the vendor open item clears on payment."

**Q2. What's the entry behind F-28 and how do you know it worked?**
"Dr Bank, Cr Customer, with the specific invoice selected as an open item so it's applied, not just a cash receipt on account. It worked when FBL5N shows the invoice as cleared with a clearing document, and 'not assigned' was 0.00 at posting."

**Q3. FB08 vs a manual reversing entry — why prefer FB08?**
"FB08 keeps a linked audit trail (original ↔ reversal), uses the correct reversal reason for period handling, and avoids fat-finger errors from re-keying. A manual opposite entry breaks that linkage and audit clarity."

## Practise free

- **Excel sub-ledger simulator:** build a journal sheet with columns Doc, Date, GL, Dr, Cr, Party; a `SUMIF` trial balance; and separate vendor/customer tabs with an "open/cleared" flag. Re-post the April set above and reconcile — that *is* the FBL1N/FBL5N logic by hand.
- Post the same five transactions in **Tally** (you already know it) and note how SAP's recon-account/open-item model differs from Tally's ledger posting — great interview colour.
- **SAP CAL S/4HANA trial** or a rented training server: actually key FB50/FB60/FB70/F-28/F-53/FB08 once end-to-end; muscle memory beats theory.
- openSAP "Financial Accounting in SAP S/4HANA" has guided posting exercises with screenshots you can shadow even without a live system.
