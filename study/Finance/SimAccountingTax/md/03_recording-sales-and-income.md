# Recording Sales and Service Income (with Output GST, e-Invoice & e-Way Bill)

## The situation

It's 30 April 2026, 11:00 a.m. The sales team has closed April. Dispatches of electrical components went out across Telangana and to two customers in other states; the service team billed installation and AMC jobs. Because NTSPL's turnover is Rs 12 cr (> Rs 5 cr), **every B2B tax invoice must carry an IRN (e-invoice)**, and any goods consignment above Rs 50,000 needs an **e-way bill**. Your job: record all April outward supplies in TallyPrime so **output GST**, place-of-supply and the e-invoice/e-way-bill fields are all correct — because these vouchers *are* GSTR-1.

April outward totals to reconcile to:

| Supply | Taxable (Rs) | Output tax |
|---|---:|---|
| Intra-state goods | 60,00,000 | CGST 5,40,000 + SGST 5,40,000 |
| Inter-state goods | 25,00,000 | IGST 4,50,000 |
| Services (intra) | 15,00,000 | CGST 1,35,000 + SGST 1,35,000 |
| **Output tax total** | **1,00,00,000** | **CGST 6,75,000 + SGST 6,75,000 + IGST 4,50,000 = 18,00,000** |

## What you're given

**Sample tax invoice — inter-state goods sale (customer in Karnataka):**

```
NIRVANA TRADERS & SERVICES PVT LTD          TAX INVOICE
Regd office: Hyderabad, Telangana   GSTIN 36AABCN1234A1Z5
Invoice No: NT/GST/0421   Date: 20-Apr-2026
Bill to: Mysore Motors Ltd, Mysuru  GSTIN 29AAACM6789K1Z4
Place of supply: Karnataka (29) — INTER-STATE
------------------------------------------------------------------
Item                         HSN    Qty   Rate      Amount
Industrial contactors 32A    8536   500   5,000   25,00,000
------------------------------------------------------------------
Taxable value                                     25,00,000
IGST @ 18%                                          4,50,000
Invoice total                                     29,50,000
IRN: (to be generated)   Ack No: ___  e-Way Bill No: ___
```

**Sample service invoice — intra-state AMC (Telangana customer):**

```
Invoice No: NT/SVC/0409  Date: 12-Apr-2026
Bill to: Charminar Foods Pvt Ltd, Hyderabad  GSTIN 36AA FC1234H1Z8
Service: Annual Maintenance Contract – electrical    SAC 9987
Taxable 15,00,000   CGST 9% 1,35,000   SGST 9% 1,35,000   Total 17,70,000
Place of supply: Telangana (36) — INTRA-STATE
```

Intra-state goods (Rs 60,00,000) are the sum of many Telangana B2B/B2C dispatch invoices during April.

## Do it — step by step

### Step 1 — Open the Sales voucher

**Alt+G > "Sales" > Enter** (or Gateway > Vouchers > **F8 Sales**). Item-invoice mode for goods (stock + HSN), accounting-invoice mode for services (SAC, no stock).

### Step 2 — The place-of-supply rule (the whole game)

Tax type is decided by **place of supply vs supplier location**, not by where the customer's office is registered on paper:

- Supplier (NTSPL) is in **Telangana (36)**.
- Place of supply **within 36** → **intra-state → CGST + SGST**.
- Place of supply in **another state** (e.g., Karnataka 29) → **inter-state → IGST**.

For goods it's generally where movement terminates; for services (AMC), where the service is performed / the registered recipient sits.

### Step 3 — Book the inter-state goods sale

Customer GSTIN 29… → IGST. Journal Tally writes:

```
Dr  Mysore Motors Ltd                 29,50,000
    Cr  Sales-Goods                            25,00,000
    Cr  Output IGST                             4,50,000
(Being inter-state sale, Inv NT/GST/0421, HSN 8536, POS Karnataka)
```

### Step 4 — Book the intra-state service (AMC)

Accounting-invoice mode, SAC 9987, both parties in 36 → CGST + SGST:

```
Dr  Charminar Foods Pvt Ltd           17,70,000
    Cr  Sales-Services                         15,00,000
    Cr  Output CGST                             1,35,000
    Cr  Output SGST                             1,35,000
(Being AMC service, Inv NT/SVC/0409, SAC 9987, POS Telangana)
```

### Step 5 — Book the intra-state goods (consolidated)

The many Telangana goods invoices net to:

```
Dr  Sundry Debtors (various)          70,80,000
    Cr  Sales-Goods                            60,00,000
    Cr  Output CGST                             5,40,000
    Cr  Output SGST                             5,40,000
(Being intra-state goods sales April, HSN 8536)
```

### Step 6 — Generate the e-invoice (IRN + QR)

Mandatory for NTSPL (T/O > Rs 5 cr, FY2026-27) on **B2B / exports / credit-debit notes** — not B2C. Two routes in TallyPrime:

1. **Online, from the voucher:** after saving, press **Alt+Z (Exchange) > Send for e-Invoicing**, log in to the IRP (NIC) with GSP/API credentials. The IRP validates and returns the **IRN (64-char hash)**, **Acknowledgement No. + date**, and a **signed QR code**. Tally stamps them back on the invoice and prints the QR.
2. **Bulk/offline:** export the JSON (e-Invoice report), upload on the IRP portal, import the signed response.

An invoice **without a valid IRN is not a legal tax invoice** — the buyer's ITC and your GSTR-1 both depend on it. The IRN also auto-populates GSTR-1, so you don't re-key B2B invoices.

### Step 7 — Generate the e-way bill (goods movement)

For any **consignment value > Rs 50,000** carrying goods, an **e-way bill** is required before the vehicle moves. The Rs 29,50,000 Mysore consignment clearly needs one. From the same **Alt+Z** menu, generate the e-way bill alongside the IRN (Part-A auto-fills from the invoice; add **Part-B: vehicle no., transporter ID, distance**). You get an **EWB number** valid for a distance-based period. Services (AMC) carry no goods → **no e-way bill**.

## The deliverable

**April GSTR-1 outward summary (from the sales register):**

| Table | Supply | Taxable | CGST | SGST | IGST |
|---|---|---:|---:|---:|---:|
| B2B/B2C intra | Goods (36) | 60,00,000 | 5,40,000 | 5,40,000 | — |
| B2B inter | Goods (29 etc.) | 25,00,000 | — | — | 4,50,000 |
| B2B intra | Services (9987) | 15,00,000 | 1,35,000 | 1,35,000 | — |
| **Total** | | **1,00,00,000** | **6,75,000** | **6,75,000** | **4,50,000** |

**Output tax = Rs 18,00,000.** Every B2B line carries an IRN; goods consignments > Rs 50,000 carry an EWB number. GSTR-1 due **11 May 2026**.

## How it's checked

- **Output ledger totals** = CGST 6,75,000 / SGST 6,75,000 / IGST 4,50,000 — tie to the sales register.
- **IRN present on every B2B invoice**; the IRP acknowledged them (no failed/pending status).
- **Place-of-supply logic:** Karnataka invoice shows IGST, Telangana invoices show CGST+SGST. One mis-tagged POS = GSTR-1 error + buyer ITC mismatch.
- **HSN 8536 (goods) / SAC 9987 (services)** correct in the HSN summary table.
- **GSTR-1 (11th) → auto-flows to GSTR-3B (20th):** the Rs 18,00,000 output must match between GSTR-1 and 3B or a system flag fires.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Charging CGST+SGST on an inter-state sale | Wrong tax, buyer ITC denied, GSTR-1 error | Drive tax off place of supply, not billing address |
| Skipping IRN on a B2B invoice | Invoice invalid; ITC & GSTR-1 fail | Generate IRN before dispatch/print |
| e-invoice generated but e-way bill forgotten | Goods detained, penalty | Any consignment > Rs 50,000 needs EWB before movement |
| Generating an e-way bill for a service (AMC) | Rejected — no goods movement | EWB only for physical goods |
| GSTR-1 output ≠ 3B output | Portal mismatch, notice | Reconcile before filing; both must show 18,00,000 |

## On the job & in the interview

The "why": under GST the **invoice is the return**. Because e-invoices auto-populate GSTR-1, an error at voucher entry becomes a filed error. Place of supply is the single most consequential field — it decides CGST+SGST vs IGST and whether the customer can claim ITC at all.

**Q: A Hyderabad customer asks you to ship goods to their Bangalore site. Which GST applies?**
A: Place of supply is where movement terminates — Karnataka — so it's inter-state: **IGST @ 18%**, regardless of the customer's HO being in Hyderabad.

**Q: NTSPL's turnover is Rs 12 cr. What e-invoicing obligation follows, and on which documents?**
A: Above the Rs 5 cr threshold (FY2026-27), e-invoicing is mandatory on all **B2B invoices, exports and credit/debit notes** — each must carry an IRN and signed QR. B2C is excluded.

**Q: When is an e-way bill required and what's different from an e-invoice?**
A: An e-way bill is for **movement of goods where consignment value > Rs 50,000**; an e-invoice is for the tax document itself (B2B, T/O > 5 cr). A goods invoice can need both; a service invoice needs the e-invoice but no e-way bill.
