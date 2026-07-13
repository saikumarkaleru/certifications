# GST in Practice I: Registration, Invoicing, E-Invoice & E-Way Bill

## What it is & where it's used

Every business in India with taxable turnover above the threshold lives inside the GST machine: it registers, raises tax invoices, pushes those invoices to the government's Invoice Registration Portal (IRP) to get an IRN and QR code, and generates an e-way bill before goods move. These four steps are the daily plumbing of the finance-tax function. Get one wrong and the buyer loses input tax credit (ITC), the truck gets detained, or a notice lands.

Roles that do this hands-on:

- **Accounts/AP-AR executives** — raise sales invoices, book purchases, match ITC.
- **GST/Indirect-tax analysts** — registration amendments, e-invoicing exceptions, reconciliations.
- **Finance controllers & CA-firm article/audit staff** — sign off that the invoice-to-e-way-bill chain is compliant.
- **ERP/Tally implementers** — configure the IRP/e-way-bill API integration.

If you can register an entity, cut a compliant tax invoice, generate the IRN, and produce the e-way bill without asking anyone — you are doing what a company actually pays a tax executive for.

## The gap: why companies want this (and college didn't teach it)

An MBA or CA-Inter syllabus teaches you *what* Section 22 says about registration thresholds and *what* Rule 46 lists as mandatory invoice fields. It does **not** put you on the GST portal at `gst.gov.in`, hand you a login, and say "register this Private Limited company by end of day." The gap is procedural muscle memory:

| College teaches | Job needs |
|---|---|
| "Threshold is ₹40L/₹20L" | Which state, goods vs services, which ARN to track |
| "Invoice must have GSTIN, HSN, tax rate" | The exact 16-char invoice numbering rule, place-of-supply logic for IGST vs CGST+SGST |
| "E-invoicing is mandatory over a limit" | The ₹5 crore AATO trigger, generating IRN in Tally/IRP, handling a rejected payload |
| "E-way bill for movement of goods" | ₹50,000 rule, Part-A vs Part-B, validity by distance, extending an expired bill |

Employers pay for the person who has *clicked the buttons*, seen the error `2172: Duplicate IRN`, and knows the fix. That is unteachable from a textbook.

## What "proficient" looks like

A job-ready person can, unaided:

1. **Register** a new GSTIN end-to-end (TRN → Part-B → ARN → GSTIN) and read the 15-digit GSTIN structure.
2. Cut a **tax invoice** that survives an audit: correct series, HSN/SAC, place of supply, IGST vs CGST+SGST split, reverse-charge flag.
3. Generate an **e-invoice** (IRN + signed QR) from the ERP and reconcile IRNs against the GSTR-1 auto-population.
4. Generate and **manage an e-way bill**: Part-A + Part-B, pick the right transport mode, extend/cancel, and know the distance-to-validity table.
5. Know **who is exempt** from e-invoice (SEZ units as suppliers exempt, banks, transporters) and e-way bill (goods < ₹50k, non-motorised transport).

## Hands-on: how to actually do it

### A. GST Registration (portal click-path)

```
gst.gov.in → Services → Registration → New Registration
Part-A: Select "Taxpayer" → State → Legal Name (as per PAN) → PAN → email + mobile
        → OTP verification → TRN (Temporary Reference Number) generated
Part-B (login with TRN): 10 tabs
   Business Details → Promoters/Partners → Authorized Signatory
   → Principal Place of Business → Additional Places → Goods & Services (HSN/SAC)
   → Bank Accounts (can add post-registration) → State Specific → Verification
Submit with DSC (mandatory for Companies/LLP) or EVC/e-Sign
→ ARN generated → track at Services > Track Application Status
→ GSTIN + registration certificate (Form REG-06) in ~7 working days
```

**Decode the GSTIN** `29ABCDE1234F1Z5`:

| Chars | Meaning |
|---|---|
| 1-2 | State code (29 = Karnataka) |
| 3-12 | PAN of entity |
| 13 | Entity number of same PAN in state |
| 14 | `Z` by default |
| 15 | Check-digit |

Excel to validate GSTIN length + embedded PAN:

```excel
=IF(AND(LEN(A2)=15, MID(A2,3,10)=B2), "Valid structure", "Check GSTIN")
```
(A2 = GSTIN, B2 = PAN)

### B. Tax invoice — mandatory contents (Rule 46)

A compliant B2B tax invoice must carry: supplier name/address/**GSTIN**; consecutive **invoice number** (≤16 chars, alphanumeric, unique per FY); date; recipient GSTIN + name; **place of supply** (for inter-state); **HSN/SAC**; description; qty; taxable value; **tax rate & amount split into CGST/SGST or IGST**; reverse-charge flag; signature/DSC.

**IGST vs CGST+SGST decision** (the logic that trips freshers):

```excel
' C2 = supplier state code, D2 = place-of-supply state code, E2 = taxable value, F2 = rate%
IGST  =IF(C2<>D2, E2*F2, 0)
CGST  =IF(C2=D2, E2*F2/2, 0)
SGST  =IF(C2=D2, E2*F2/2, 0)
```

**Journal entry — outward B2B sale, ₹1,00,000 + 18% IGST (inter-state):**

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Debtor / Customer A | 1,18,000 | |
| Sales | | 1,00,000 |
| Output IGST | | 18,000 |

**Intra-state (18% = 9% CGST + 9% SGST):**

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Debtor | 1,18,000 | |
| Sales | | 1,00,000 |
| Output CGST | | 9,000 |
| Output SGST | | 9,000 |

### C. E-invoicing (IRN + QR)

Applicable when **Aggregate Annual Turnover (AATO) > ₹5 crore** in any FY since 2017-18. You do **not** create the invoice on the IRP — your ERP generates the JSON, posts it to the IRP, and gets back the **IRN** (64-char hash) + **signed QR** + digitally signed invoice.

**TallyPrime path:**
```
Gateway of Tally → Alter → GST Details → set "e-Invoicing applicable: Yes"
Voucher entry (F8 Sales) → Save → prompt "Provide GST details?" → Yes
Exchange → Send for e-Invoicing → IRP login (via GSP/API) → IRN + QR fetched back
Print → invoice now shows IRN + QR
```

**IRP portal (manual / bulk):** `einvoice1.gst.gov.in` → Login → e-Invoice → Bulk Upload → upload JSON via offline tool → download IRN file.

Python to build a minimal e-invoice payload (concept for API integration):

```python
import requests, json

payload = {
    "Version": "1.1",
    "TranDtls": {"TaxSch": "GST", "SupTyp": "B2B", "RegRev": "N"},
    "DocDtls": {"Typ": "INV", "No": "INV/2026/0042", "Dt": "03/07/2026"},
    "SellerDtls": {"Gstin": "29ABCDE1234F1Z5", "LglNm": "Acme Pvt Ltd",
                   "Addr1": "MG Road", "Loc": "Bengaluru", "Pin": 560001, "Stcd": "29"},
    "BuyerDtls": {"Gstin": "27PQRS5678K1Z2", "LglNm": "Beta LLP", "Pos": "27",
                  "Addr1": "Andheri", "Loc": "Mumbai", "Pin": 400053, "Stcd": "27"},
    "ItemList": [{"SlNo": "1", "PrdDesc": "Steel bracket", "HsnCd": "7308",
                  "Qty": 100, "Unit": "NOS", "UnitPrice": 1000, "TotAmt": 100000,
                  "AssAmt": 100000, "GstRt": 18, "IgstAmt": 18000, "TotItemVal": 118000}],
    "ValDtls": {"AssVal": 100000, "IgstVal": 18000, "TotInvVal": 118000}
}

headers = {"Authorization": auth_token, "Content-Type": "application/json",
           "user_name": user, "Gstin": "29ABCDE1234F1Z5"}
r = requests.post("https://einv-apisandbox.nic.in/eivital/v1.04/invoice",
                  headers=headers, data=json.dumps(payload))
print(r.json()["Data"]["Irn"], r.json()["Data"]["SignedQRCode"])
```

### D. E-way bill

Required when **consignment value > ₹50,000** and goods move (inter-state, or intra-state where the state mandates). Two parts:

- **Part-A**: GSTIN of supplier/recipient, invoice no/date, HSN, value, place-of-dispatch/delivery pincodes.
- **Part-B**: transporter ID, vehicle number / transport doc number.

**Portal path** `ewaybillgst.gov.in`:
```
Login → e-Way Bill → Generate New
Transaction Type: Outward → Sub-type: Supply
Doc type: Tax Invoice → No + Date
From (auto from GSTIN) → To (buyer GSTIN + pincode)
Item: HSN, qty, taxable value, tax rate → system computes value
Part-B: Mode = Road → Vehicle No (KA01AB1234) → Approx distance (km)
Submit → 12-digit EWB number + validity generated
```

**Validity table (regular cargo):**

| Distance | Validity |
|---|---|
| Up to 200 km | 1 day |
| Every additional 200 km (or part) | +1 day |

Expiring bill → **Extend** under e-Way Bill > Extend Validity (only within 8 hrs before/after expiry).

## Worked example / mini-project

**Scenario:** Acme Pvt Ltd (GSTIN 29…, Karnataka, AATO ₹12 cr) sells 100 steel brackets @ ₹1,000 to Beta LLP (Mumbai) on 03-Jul-2026. Distance 980 km by road, vehicle KA01AB1234.

Reproduce the full chain:

1. **Invoice value:** 100 × ₹1,000 = ₹1,00,000 taxable. Inter-state → **IGST 18% = ₹18,000**. Invoice total **₹1,18,000**. Invoice no `INV/2026/0042`.

2. **E-invoice:** AATO > ₹5 cr → mandatory. Post the JSON above to IRP → receive IRN + QR. The IRN auto-populates GSTR-1, so you do **not** re-key this invoice in GSTR-1.

3. **E-way bill:** value ₹1,18,000 > ₹50,000 → mandatory. Part-A from invoice; Part-B vehicle KA01AB1234. Distance 980 km → validity = ceil(980/200) = **5 days**.

4. **Books (Acme, seller):**

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Beta LLP (Debtor) | 1,18,000 | |
| Sales – Steel brackets | | 1,00,000 |
| Output IGST | | 18,000 |

5. **Buyer (Beta LLP) claims ITC** only because Acme's IRN flowed to GSTR-1 → GSTR-2B. Beta's entry:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases | 1,00,000 | |
| Input IGST | 18,000 | |
| Acme Pvt Ltd (Creditor) | | 1,18,000 |

**Reconciliation check** in Excel — match IRN invoices to GSTR-2B:
```excel
=IF(COUNTIF(GSTR2B[InvNo], [@InvNo])>0, "Matched", "MISSING in 2B")
```

## How it's tested

**Interview questions:**
- "Turnover ₹6 cr — is e-invoicing mandatory? From when?" (Yes, > ₹5 cr.)
- "Karnataka seller, Karnataka buyer — CGST+SGST or IGST?" (CGST+SGST; place of supply = Karnataka.)
- "Consignment ₹45,000 — e-way bill needed?" (No, below ₹50k — unless state rule or handicraft exception.)
- "Buyer says no ITC showing — where do you look?" (Did seller generate IRN / file GSTR-1 → check GSTR-2B.)
- "Vehicle broke down mid-transit, bill expiring — what do you do?" (Extend validity; update Part-B with new vehicle.)

**Practical assessment companies give:**
- A timed task: "Here's a PO — raise a compliant tax invoice in Tally/Excel with correct tax split." 
- "Register this dummy entity on the GST portal sandbox and screenshot the ARN."
- "Given this invoice JSON that IRP rejected with error 2172 — fix it." (Duplicate IRN → invoice already registered; don't resubmit.)
- A reconciliation screen: match a purchase register against a GSTR-2B extract and flag missing ITC.

## Common mistakes & how pros avoid them

| Mistake | Fix / pro habit |
|---|---|
| Invoice number > 16 chars or resets mid-year | Keep series ≤16 alphanumeric, unique per FY; document the series scheme |
| Charging IGST for intra-state (or vice versa) | Always derive from **place of supply**, not billing address |
| Generating e-way bill but skipping e-invoice (or vice versa) | Both are separate obligations; build both into the ERP save flow |
| Resubmitting a rejected IRN payload blindly | Read the error code — 2172 = duplicate, don't retry; 2150 = invalid GSTIN |
| Letting e-way bill expire in transit | Track validity; extend within the 8-hr window before/after expiry |
| Assuming ITC is automatic | ITC depends on **seller** filing GSTR-1; reconcile against GSTR-2B monthly |
| Wrong HSN digits (4 vs 6 vs 8) | AATO > ₹5 cr needs **6-digit HSN**; below, 4-digit for B2B |

## Learn-it roadmap & resources

**Time to proficiency:** ~3-4 weeks of hands-on practice alongside a real or dummy books set.

| Week | Focus |
|---|---|
| 1 | Register a dummy entity on GST portal; decode GSTINs; Rule 46 invoice fields |
| 2 | Cut 20 invoices in TallyPrime with correct tax splits and journal entries |
| 3 | E-invoicing sandbox (`einv-apisandbox.nic.in`) — generate IRNs, handle rejects |
| 4 | E-way bills end-to-end; monthly GSTR-2B reconciliation in Excel |

**Resources:**
- GSTN official user manuals — `tutorial.gst.gov.in` (free, authoritative).
- E-invoice & e-way bill sandbox portals for API practice.
- ICAI GST background material (free for students).
- TallyPrime GST self-learning modules; ClearTax / IRIS blogs for edge cases.
- **Certification:** ICAI Certificate Course on GST; NACIN GST practitioner path; MSME GST practitioner courses.

## Quick-reference

| Item | Rule of thumb |
|---|---|
| Registration threshold | ₹40L goods / ₹20L services (₹20L/₹10L special-category states) |
| GSTIN | 15 char: 2 state + 10 PAN + 1 entity + Z + check-digit |
| E-invoice trigger | AATO > ₹5 crore in any FY since 2017-18 |
| E-invoice output | 64-char IRN + signed QR (from IRP, not manually created) |
| E-way bill trigger | Consignment value > ₹50,000 |
| EWB validity | 1 day / 200 km, +1 day per extra 200 km |
| Intra-state tax | CGST + SGST (equal split) |
| Inter-state tax | IGST (= CGST + SGST rate) |
| ITC source | GSTR-2B (depends on seller's GSTR-1) |
| Key portals | gst.gov.in, einvoice1.gst.gov.in, ewaybillgst.gov.in |
| Common error 2172 | Duplicate IRN — invoice already registered, do not resubmit |
| Invoice number | ≤16 chars, alphanumeric, unique per FY (Rule 46) |
| HSN digits | 6-digit if AATO > ₹5 cr, else 4-digit (B2B) |
