# GST Monthly I: Filing GSTR-1 from the Sales Register

## The situation

It's the morning of **8 May 2026**. April is closed in TallyPrime, the sales team has stopped raising back-dated invoices, and your reporting head drops a one-line message in the accounts group: *"April GSTR-1 — get it filed well before the 11th, don't wait for the last day again."*

GSTR-1 is the **statement of outward supplies** — the return where NTSPL declares every sale it made in April 2026, invoice by invoice, so that the tax appears in each customer's GSTR-2B and they can claim ITC. It is a self-contained, one-way declaration: whatever you report here (FY2026-27) auto-populates the outward-tax side of GSTR-3B, so an error on the 11th becomes a payment error on the 20th. Because NTSPL's turnover is above Rs 5 cr, **e-invoicing already applies** — most B2B invoices are already reported to the IRP and will flow into GSTR-1 automatically, but you still own the reconciliation, the B2C and HSN summaries, and the final filing.

Your job today: build the return from the sales register, tie it to the books, and file it.

## What you're given

The April 2026 **Sales Register** (Gateway of Tally → Display More Reports → Account Books → Sales Register), summarised by the three revenue streams in the shared case:

| Stream | Nature | Place of supply | Taxable value | CGST 9% | SGST 9% | IGST 18% |
|---|---|---|---|---|---|---|
| Industrial components (intra-TS) | Goods, HSN 8536 | Telangana (36) | 60,00,000 | 5,40,000 | 5,40,000 | — |
| Industrial components (inter-state) | Goods, HSN 8536 | e.g. Karnataka (29) | 25,00,000 | — | — | 4,50,000 |
| Installation & AMC (intra-TS) | Services, SAC 9987 | Telangana (36) | 15,00,000 | 1,35,000 | 1,35,000 | — |
| **Total** | | | **1,00,00,000** | **6,75,000** | **6,75,000** | **4,50,000** |

**Output tax = CGST 6,75,000 + SGST 6,75,000 + IGST 4,50,000 = Rs 18,00,000.**

Two facts you must pull from the register before touching the portal:

- **Customer type split.** Of the intra-state goods (Rs 60,00,000) and services (Rs 15,00,000), assume Rs 70,00,000 is to GST-registered businesses (**B2B**) and Rs 5,00,000 is to unregistered walk-in/AMC customers (**B2C**) — none of the individual B2C invoices exceeds Rs 1,00,000, so all B2C is "small." All inter-state goods (Rs 25,00,000) are to registered dealers (B2B).
- **Documents issued.** Invoices raised for the month: **142** (serial NT/2627/0001–0142), of which **3 are cancelled**; **4 credit notes** (NT-CR/2627/01–04); **0 debit notes**.

## Do it — step by step

**Step 1 — Verify e-invoice coverage.** For every B2B invoice above, an IRN + signed QR must already exist. In Tally: Gateway → Display → Statutory Reports → GST → e-Invoice → check that "Pending" and "Rejected" are both nil. Any B2B invoice without an IRN is legally *not a valid tax invoice* — fix it before filing, because those lines will not auto-populate GSTR-1.

**Step 2 — Generate the GSTR-1 in Tally.** Gateway of Tally → Display More Reports → **GST Reports → GSTR-1**. Set period 1-Apr-2026 to 30-Apr-2026. Tally classifies each voucher into the portal tables. Confirm nothing sits in **"Uncertain Transactions (Not relevant / needs correction)"** — a missing GSTIN, a wrong place of supply, or a blank HSN lands here and will silently drop from the return.

**Step 3 — Map the numbers to the portal tables.**

- **Table 4A — B2B (registered):** intra-state goods B2B + services B2B (Rs 70,00,000) and inter-state goods B2B (Rs 25,00,000) = **Rs 95,00,000** taxable, invoice-wise with each customer's GSTIN.
- **Table 5 — B2C Large (inter-state, invoice > Rs 1,00,000 to unregistered):** **nil** here (no such invoices).
- **Table 7 — B2C Others (small):** the Rs 5,00,000 intra-state retail/AMC supplies, rate-wise consolidated (not invoice-wise).
- **Table 12 — HSN/SAC summary:** mandatory. HSN 8536 (goods) and SAC 9987 (services), with quantity/UQC for goods.
- **Table 13 — Documents issued:** the invoice, credit-note and debit-note serial ranges.

**Step 4 — File.** On the GST portal, Returns Dashboard → FY 2026-27 → April → GSTR-1 → **Prepare Online** (or upload the JSON exported from Tally's GSTR-1 screen via *Export → e-Return*). Because e-invoicing is on, most of Table 4A/5 is pre-filled from the IRP; you add/confirm B2C (7), HSN (12) and documents (13). Then **Generate Summary → Preview → Submit → File with DSC** (a private company must use the **Digital Signature Certificate**, not EVC).

**No accounting entry is posted for filing GSTR-1** — the output tax was already booked when each sales voucher was raised:

```
On each April sale (illustrative, intra-state goods invoice of Rs 1,00,000):
  Dr  Debtor / Bank                 1,18,000
      Cr  Sales – Goods                 1,00,000
      Cr  Output CGST @9%                  9,000
      Cr  Output SGST @9%                  9,000
```

## The deliverable — the filed GSTR-1

| Table | Description | Taxable value | CGST | SGST | IGST |
|---|---|---|---|---|---|
| 4A | B2B supplies (invoice-wise) | 95,00,000 | 6,30,000 | 6,30,000 | 4,50,000 |
| 5 | B2C Large (inter-state > 1L) | 0 | — | — | 0 |
| 7 | B2C Others (intra, consolidated) | 5,00,000 | 45,000 | 45,000 | — |
| **Total outward** | | **1,00,00,000** | **6,75,000** | **6,75,000** | **4,50,000** |

**Table 12 — HSN/SAC summary**

| HSN/SAC | Description | UQC | Qty | Taxable value | Rate | CGST | SGST | IGST |
|---|---|---|---|---|---|---|---|---|
| 8536 | Elec. apparatus ≤1000V | NOS | (as per stock) | 85,00,000 | 18% | 5,40,000 | 5,40,000 | 4,50,000 |
| 9987 | Installation/maintenance | NA | — | 15,00,000 | 18% | 1,35,000 | 1,35,000 | — |

**Table 13 — Documents issued**

| Document | From | To | Total | Cancelled | Net issued |
|---|---|---|---|---|---|
| Tax invoices | NT/2627/0001 | NT/2627/0142 | 142 | 3 | 139 |
| Credit notes | NT-CR/2627/01 | NT-CR/2627/04 | 4 | 0 | 4 |
| Debit notes | — | — | 0 | 0 | 0 |

## How it's checked

- **Table totals vs books:** GSTR-1 taxable value **Rs 1,00,00,000** must equal the sales-register taxable turnover for April; output tax **Rs 18,00,000** must equal the credit balance movement in Output CGST/SGST/IGST ledgers.
- **4A + 5 + 7 tax = HSN Table 12 tax = Rs 18,00,000.** All three cross-foot.
- **e-invoice vs 4A:** the portal flags any B2B invoice whose IRN differs from what you filed.
- **Downstream:** on 20 May, GSTR-3B **Table 3.1(a)** auto-drafts these exact figures. If 3.1 doesn't read Rs 18,00,000 output, GSTR-1 was wrong.

## Common mistakes & red flags

| Mistake | Consequence | Fix |
|---|---|---|
| Wrong place of supply (put inter-state sale as intra) | Customer's ITC blocked; you paid CGST/SGST when IGST was due | Correct PoS in the invoice; amend via Table 9A next month |
| B2B invoice with no IRN | Not a valid tax invoice; drops from 4A | Generate IRN before filing |
| HSN Table 12 left blank/short | Portal error (mandatory > Rs 5 cr); notice risk | Fill 6-digit HSN with UQC |
| Missed the 11th | Late fee + customer can't see ITC in their 2B | File on time; there is no revision — only next-month amendment |
| GSTIN typo on a customer | Their 2B won't reflect; they chase you | Validate GSTINs before upload |

## On the job & in the interview

GSTR-1 is where you *tell the government who bought what* — it feeds the whole ITC chain, so accuracy here protects your customers' credit and your own reputation. On the job you live in the "Uncertain Transactions" list and the e-invoice pending list; clearing those is 80% of the work.

**Q: "GSTR-1 has no revision. A customer calls on 15 May saying their April invoice has the wrong GSTIN — what do you do?"**
A: I can't revise the filed GSTR-1. I amend it in the **next** period's return using **Table 9A (amended B2B)**, entering the original invoice details and the corrected GSTIN. It reflects in their GSTR-2B for that later month. I document the correction and warn the customer of the one-month ITC timing lag.

**Q: "How does GSTR-1 relate to GSTR-3B?"**
A: GSTR-1 is invoice-level outward detail; GSTR-3B is the monthly summary-and-pay return. My 3.1(a) output figures auto-draft from GSTR-1, so I file GSTR-1 first (by 11th) and 3B after (by 20th). They must tie to the rupee — any gap between GSTR-1 and 3B is a classic notice trigger.

**Q: "What's the point of Table 13, documents issued?"**
A: It's a control — the department reconciles serial-number continuity to catch suppressed invoices (a gap in the series, or fewer invoices reported than issued). I report the full range, cancellations included, so the count ties.
