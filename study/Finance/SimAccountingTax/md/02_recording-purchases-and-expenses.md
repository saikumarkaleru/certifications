# Recording Purchases and Expenses (with Input GST)

## The situation

It's 30 April 2026, 4:15 p.m. The month's supplier bills have piled up in the "TO BOOK" tray and the Finance Manager wants April purchases fully entered before the GSTR-2B pulls tomorrow. On top: a stack of vendor tax invoices — intra-state goods, one inter-state consignment, and the usual office expenses (rent, telecom) that also carry input GST. Your job: book every one in TallyPrime so the **Input Tax Credit (ITC)** is captured correctly and the creditor ledgers show the right outstanding.

The month's purchase totals you're reconciling to:

| Category | Taxable (Rs) | ITC |
|---|---:|---|
| Intra-state goods purchases | 55,00,000 | CGST 4,95,000 + SGST 4,95,000 |
| Inter-state goods purchases | 12,00,000 | IGST 2,16,000 |
| Expenses with ITC (rent, telecom, etc.) | 4,00,000 | CGST 36,000 + SGST 36,000 |
| **Total ITC (books)** | | **CGST 5,31,000 + SGST 5,31,000 + IGST 2,16,000 = 12,78,000** |

## What you're given

**Sample vendor bill 1 — intra-state (Telangana supplier):**

```
TAX INVOICE          Supplier: Deccan Electricals Pvt Ltd, Hyderabad
Invoice No: DE/0417   Date: 18-Apr-2026    GSTIN: 36AAECD5678B1Z2
------------------------------------------------------------------
Item                         HSN    Qty   Rate      Amount
MCB 32A industrial contactor 8536   400   2,500   10,00,000
------------------------------------------------------------------
Taxable value                                     10,00,000
CGST @ 9%                                             90,000
SGST @ 9%                                             90,000
Invoice total                                     11,80,000
Place of supply: Telangana (36)
```

**Sample vendor bill 2 — inter-state (Maharashtra supplier):**

```
TAX INVOICE          Supplier: Bombay Switchgear LLP, Pune
Invoice No: BS-2231   Date: 22-Apr-2026   GSTIN: 27AABFB9012C1Z9
------------------------------------------------------------------
Item                         HSN    Qty   Rate      Amount
Modular switchgear panels    8536    60  20,000   12,00,000
------------------------------------------------------------------
Taxable value                                     12,00,000
IGST @ 18%                                          2,16,000
Invoice total                                     14,16,000
Place of supply: Telangana (36) — inter-state, IGST
```

**Expense bill — office rent (registered landlord):**

```
Landlord: Cyber Estates LLP, Hyderabad   GSTIN: 36AABCC3456D1Z1  SAC 9972
Monthly office rent (Apr-2026)  Taxable 1,50,000  CGST 9% 13,500  SGST 9% 13,500  Total 1,77,000
```

(Rent is one component of the Rs 4,00,000 ITC-bearing expenses; telecom, housekeeping consumables etc. make up the rest.)

## Do it — step by step

### Step 1 — Open the Purchase voucher

**Alt+G > type "Purchase" > Enter** (or Gateway > Vouchers > **F9 Purchase**). Two modes exist:

- **Item Invoice mode** — for stock items (goods). Feeds inventory + HSN into GSTR-1/2 automatically. Use for the two goods bills.
- **Accounting Invoice mode** — no stock movement, only a ledger. Use for expenses (rent, telecom). Toggle with **Ctrl+H (Change Mode)** > As Voucher / As Invoice, and the "Item invoice / Accounting invoice" button on the right panel.

### Step 2 — Book bill 1 (intra-state goods, Item Invoice mode)

| Field | Entry |
|---|---|
| Supplier invoice no. / date | DE/0417 · 18-Apr-2026 |
| Party A/c name | Deccan Electricals Pvt Ltd (Sundry Creditors, bill-wise) |
| Purchase ledger | Purchases-Goods |
| Item | MCB 32A contactor, HSN 8536, 400 × 2,500 = 10,00,000 |
| CGST | 90,000 (auto) |
| SGST | 90,000 (auto) |

Because both supplier and place of supply are Telangana (36), Tally picks **CGST + SGST**. The journal it writes:

```
Dr  Purchases-Goods            10,00,000
Dr  Input CGST                    90,000
Dr  Input SGST                    90,000
    Cr  Deccan Electricals Pvt Ltd        11,80,000
(Being intra-state purchase, Inv DE/0417, HSN 8536, ITC availed)
```

### Step 3 — Book bill 2 (inter-state goods → IGST)

Supplier GSTIN starts **27** (Maharashtra), place of supply Telangana → **inter-state → IGST**. Tally auto-selects Input IGST:

```
Dr  Purchases-Goods            12,00,000
Dr  Input IGST                  2,16,000
    Cr  Bombay Switchgear LLP             14,16,000
(Being inter-state purchase, Inv BS-2231, HSN 8536, IGST ITC availed)
```

### Step 4 — Book the rent expense (Accounting Invoice mode, with ITC)

Rent is a service (SAC 9972), no stock. Switch to Accounting Invoice mode:

```
Dr  Rent (Indirect Expenses)    1,50,000
Dr  Input CGST                     13,500
Dr  Input SGST                     13,500
    Cr  Cyber Estates LLP                  1,77,000
(Being office rent Apr-2026, ITC availed, SAC 9972)
```

Note: this rent bill *also* triggers **194I TDS** — that entry is handled in the TDS chapter; here we focus on the expense + ITC. Telecom and other ITC-expenses are booked the same way, together totalling taxable Rs 4,00,000 / ITC CGST 36,000 + SGST 36,000.

### Step 5 — The reverse-charge (RCM) flag

Some inward supplies (e.g., a **goods transport agency** freight bill, legal fees from an advocate, purchase from an unregistered dealer above threshold) attract **reverse charge** — NTSPL pays the GST itself instead of the supplier. In the purchase voucher set **"Is reverse charge applicable? = Yes"** (or use the RCM nature on the ledger). Tally then:

1. Does **not** book input tax against the supplier's invoice value, and
2. Raises a **self-invoice / RCM liability** — you pay it in cash in 3B, and claim the same as ITC in the next step. It's a two-line wash, but the liability must hit the cash ledger. In April none of the three sample bills is RCM (all registered forward-charge suppliers), so the flag stays **No** — but the reviewer will ask whether you checked.

### Step 6 — Watch the GSTR-2B gate

Two April mismatches to remember (they surface at reconciliation):

- One supplier bill **Rs 50,000 + GST 9,000 appears in GSTR-2B but is NOT in books** — chase the physical invoice; do not claim ITC until booked.
- One **book bill Rs 40,000 + GST 7,200 is in books but NOT yet in 2B** — **defer that ITC** (Rule 36(4): ITC only when it reflects in 2B). Park it; claim next month when it appears.

## The deliverable

**April purchase register (books) — feeds GSTR-2/3B ITC:**

| Type | Taxable | CGST | SGST | IGST | Invoice value |
|---|---:|---:|---:|---:|---:|
| Intra-state goods | 55,00,000 | 4,95,000 | 4,95,000 | — | 64,90,000 |
| Inter-state goods | 12,00,000 | — | — | 2,16,000 | 14,16,000 |
| ITC-expenses | 4,00,000 | 36,000 | 36,000 | — | 4,72,000 |
| **Total ITC (books)** | **71,00,000** | **5,31,000** | **5,31,000** | **2,16,000** | **83,78,000** |

Gross ITC in books = **Rs 12,78,000**. After deferring the Rs 7,200 not-in-2B and excluding the Rs 9,000 not-in-books, the **eligible ITC for April 3B** aligns with 2B (worked in the GST-return chapter).

## How it's checked

- **Tax split matches the bill:** intra → CGST+SGST, inter → IGST. A single mis-mapped supplier state throws the whole 2B match.
- **Input ledger totals** (Gateway > Display > Statutory Reports > GST) equal CGST 5,31,000 / SGST 5,31,000 / IGST 2,16,000.
- **Creditor sub-ledgers** show each invoice open bill-by-bill; the control matches Sundry Creditors.
- **GSTR-2B reconciliation:** books ITC vs 2B — the Rs 9,000 and Rs 7,200 are the only two open differences, both explained.
- **HSN 8536** on goods, correct SAC on services — mismatched HSN triggers a GSTR-1/2 HSN-summary error.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Claiming ITC before it shows in 2B | Rule 36(4) breach, interest on reversal | Defer the Rs 7,200 bill to the month it appears |
| Booking inter-state bill as CGST+SGST | 2B mismatch, ITC denied | Read supplier GSTIN state code (27 ≠ 36) |
| Booking a blocked credit (Sec 17(5)) as ITC | ITC reversal + interest | Flag motor cars, staff food, personal use as ineligible |
| Missing the RCM flag on a GTA/advocate bill | Under-paid RCM liability, notice | Set "reverse charge = Yes" and pay in cash |
| Expense booked without capturing input GST | ITC lost, cost overstated | Use accounting-invoice mode and add Input CGST/SGST |

## On the job & in the interview

The "why": ITC is working capital. Every rupee of eligible credit not captured is cash NTSPL pays twice. But claiming credit that isn't in 2B invites reversal with interest — so the discipline is *book everything, claim only what 2B supports.*

**Q: A vendor bill is in your books but not in GSTR-2B this month. Do you claim the ITC?**
A: No. Under Rule 36(4) (FY2026-27) ITC is available only when it reflects in 2B. I defer the Rs 7,200 and claim it the month it appears; meanwhile I chase the supplier to file.

**Q: When do you use accounting-invoice mode vs item-invoice mode?**
A: Item mode for goods that move stock (HSN, quantity — the 8536 purchases); accounting mode for pure expenses/services with no inventory (rent SAC 9972, telecom), still capturing Input CGST/SGST.

**Q: What's reverse charge and give one NTSPL example where you'd flag it?**
A: RCM shifts GST liability to the recipient. Example: a goods-transport-agency freight bill — NTSPL self-invoices, pays IGST/CGST+SGST in cash in 3B, and claims the same as ITC next step.
