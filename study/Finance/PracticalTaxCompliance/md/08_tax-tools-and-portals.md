# Tax Tools & Portals

## What it is & where it's used

Indian tax compliance runs on four government portals and a handful of accounting/tax software packages. You don't "know tax" for a job — you *operate* these tools:

| Tool | Owner | What it does |
|---|---|---|
| **GSTN portal** (gst.gov.in) | Goods & Services Tax Network | File GSTR-1/3B/9, generate e-invoices & e-way bills, claim ITC, reconcile GSTR-2B |
| **TRACES** (tdscpc.gov.in) | Income Tax Dept | TDS returns' aftermath — download Form 16/16A, justification reports, correct TDS defaults, Form 26AS |
| **Income-tax e-filing** (incometax.gov.in) | Income Tax Dept | File ITR, respond to notices, e-verify, pay tax, view AIS/TIS |
| **ClearTax / Zoho Books / TallyPrime** | Private | Bulk GST filing, invoicing, books of accounts, reconciliation at scale |

**Roles that live in these tools daily:** GST executive, TDS/accounts executive, statutory compliance analyst, audit associate (Big 4 and mid-tier), tax consultant, and every SME accountant. If a JD says "hands-on GST & TDS compliance," it means these exact screens.

## The gap: why companies want this (and college didn't teach it)

An MBA/CA-theory background teaches you *sections* — Section 16 ITC conditions, Section 194J TDS on professional fees, Rule 36(4). Employers don't pay you to recite Section 16; they pay you to **click the right buttons, catch a ₹40,000 ITC mismatch, and file before the 20th** without breaking anything.

The gap is procedural and unforgiving:
- College says "reconcile purchases with GSTR-2B." No one showed you the actual GSTR-2B JSON, how to VLOOKUP it against your purchase register, or what to do with an invoice the vendor never uploaded.
- College says "deduct TDS." No one made you generate a challan, map it in an FVU file, and download a corrected Form 16A after a short-deduction default.
- Portals change constantly (new IMS on GSTN, AIS on e-filing). Textbooks are always 2 years stale.

Companies want someone who has *touched the portal*, because the cost of a wrong click is real: late fees, interest, blocked ITC, and notices.

## What "proficient" looks like

A job-ready person can, unaided:

1. Log into GSTN, upload a GSTR-1 via offline tool JSON, file GSTR-3B, and know the offset order (IGST → CGST/SGST).
2. Pull GSTR-2B, reconcile it against the purchase register, and produce a "match / mismatch / not-in-2B" report.
3. Generate an e-invoice IRN and an e-way bill, and cancel one within the time window.
4. On TRACES: download Form 16A, read a Justification Report, and file a TDS correction for a wrong PAN.
5. On e-filing: reconcile Form 26AS + AIS with books, file an ITR, and respond to a 143(1) intimation.
6. In Tally/Zoho: pass a GST-compliant sales entry, run GSTR-1 report, and export the return.

The bar is **speed + zero rework**. A senior can file a month's returns for 20 GSTINs; a junior does 2–3 cleanly and reconciles the rest.

## Hands-on: how to actually do it

### GSTN portal — file GSTR-3B (click-path)
```
Login → Returns Dashboard → select FY & month → GSTR-3B "Prepare Online"
→ 3.1 Outward supplies: enter taxable value, IGST/CGST/SGST
→ 4  Eligible ITC: auto-drafts from 2B; edit 4(A)(5) All other ITC
→ 5  Exempt/nil → 6.1 Payment of tax
→ "Make Payment/Create Challan" if cash needed → File with EVC/DSC
```
Offset rule the portal enforces: **IGST credit first fully utilised, then CGST, then SGST**, cross-utilisation IGST↔CGST/SGST allowed, but CGST credit can never pay SGST.

### GSTR-2B reconciliation in Excel
Purchase register in one sheet, downloaded 2B in another. Match on **GSTIN + Invoice No + Taxable value**:
```excel
=XLOOKUP(A2&"|"&B2, Reg!$A:$A&"|"&Reg!$B:$B, Reg!$D:$D, "NOT IN BOOKS")
```
Flag ITC differences:
```excel
=IF(ABS(D2-E2)<=1,"Match",IF(E2="NOT IN 2B","ITC not available yet","MISMATCH ₹"&D2-E2))
```
Rounding tolerance of ₹1 avoids false mismatches from paise rounding.

### e-Way bill validity (know the formula)
Normal cargo: **1 day per 200 km** (part thereof = +1 day). 640 km → ceil(640/200) = 4 days.
```excel
=CEILING(distance_km/200,1)  ' days of validity
```

### TRACES — download Form 16A
```
Login (deductor) → Downloads → Form 16A → enter FY, Quarter, Form type (26Q)
→ submit request → Requested Downloads → download .zip
→ open in TRACES PDF Generation Utility → outputs password-protected PDF
```
Form 16A PDF password = **TAN in caps** (e.g., `BLRA12345B`) unless changed.

### Income-tax e-filing — pay TDS challan (Minor head 200)
```
e-Pay Tax → New Payment → TDS/TCS (Challan 281) → AY → Minor head 200 (regular)
or 400 (demand) → fill section (e.g., 94C) → Net banking → download CIN challan
```

### Journal entries — TDS on ₹1,00,000 professional fee (194J, 10%)
| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| Invoice | Professional Fees A/c Dr | 1,00,000 | |
| | To Consultant A/c | | 90,000 |
| | To TDS Payable (194J) A/c | | 10,000 |
| Payment | Consultant A/c Dr | 90,000 | |
| | To Bank A/c | | 90,000 |
| Deposit | TDS Payable A/c Dr | 10,000 | |
| | To Bank A/c | | 10,000 |

### TallyPrime — GST sales entry click-path
```
Gateway of Tally → Vouchers → F8 Sales → party name → sales ledger (with GST rate)
→ item + qty + rate → CGST/SGST ledgers auto-calc → Ctrl+A save
Reports: Display More Reports → GST Reports → GSTR-1 → export JSON for portal
```

## Worked example / mini-project

**Scenario:** You run March compliance for *Acme Traders Pvt Ltd*, Karnataka (intra-state).

Sales (outward): ₹10,00,000 taxable, GST 18% → CGST ₹90,000 + SGST ₹90,000.
Purchases per books: ₹6,00,000 taxable, ITC CGST ₹54,000 + SGST ₹54,000.
Downloaded **GSTR-2B** shows only ₹5,00,000 (ITC ₹45,000 + ₹45,000) — one vendor (₹1,00,000, ITC ₹9,000+₹9,000) hasn't filed.

**Step 1 — Reconcile.** Your Excel match flags that vendor invoice as "NOT IN 2B." Per Section 16(2)(aa)/Rule 36(4), you can claim ITC **only** to the extent in 2B.

**Step 2 — Claimable ITC:** CGST ₹45,000 + SGST ₹45,000 (not ₹54,000).

**Step 3 — Net cash payable in GSTR-3B:**

| Head | Output tax | ITC (2B) | Cash payable |
|---|---|---|---|
| CGST | ₹90,000 | ₹45,000 | ₹45,000 |
| SGST | ₹90,000 | ₹45,000 | ₹45,000 |
| **Total** | ₹1,80,000 | ₹90,000 | **₹90,000** |

**Step 4 — Challan:** Create PMT-06 for ₹90,000, pay, then file GSTR-3B.

**Step 5 — Follow-up:** Email the defaulting vendor to file their GSTR-1. When it appears in a later month's 2B, claim the ₹18,000. Record it in an "ITC pending" tracker so it isn't forgotten (it lapses if not claimed by Nov 30 of next FY).

Reproduce this in a spreadsheet — it's exactly what a GST executive does 12 times a year per client.

## How it's tested

**Interview questions:**
- "Walk me through filing GSTR-3B. What's the ITC set-off order?"
- "Vendor didn't upload an invoice — can I claim ITC? Until when?"
- "Difference between GSTR-2A and 2B?" (2A is dynamic/live; 2B is static, generated 14th, and is the basis for ITC.)
- "TDS on ₹50,000 rent to an individual — which section, rate?" (194I, 10% on land/building.)
- "What's in Form 26AS vs AIS?"

**Practical assessments companies actually give:**
- A **timed reconciliation test**: here's a purchase register and a GSTR-2B export — produce the mismatch report in Excel in 30 minutes.
- A **Tally case**: "Enter these 10 vouchers and generate GSTR-1." They check your GST ledgers and HSN.
- A **login demo**: they hand you a sandbox/their portal and say "show me where you'd download Form 16A" or "file this nil GSTR-3B."
- **TDS challan mapping**: given payments, compute TDS, section, and due dates.

## Common mistakes & how pros avoid them

| Mistake | Consequence | Pro habit |
|---|---|---|
| Claiming full book ITC, ignoring 2B | Notice, ITC reversal + 24% interest | Reconcile 2B *every* month, claim only what's reflected |
| Filing 3B before reconciling 2B | Locked-in error (3B can't be revised) | 2B recon → then 3B, in that order |
| Wrong TDS section/rate | Short-deduction default on TRACES | Keep a section-rate cheat-sheet; verify PAN status |
| Missing e-invoice for B2B (turnover > ₹5 cr) | Invoice invalid, ITC denied to buyer | Auto-generate IRN at billing in Tally/Zoho |
| Filing GSTR-1 after 3B | 3B ITC/liability mismatch | Always GSTR-1 first, then 3B |
| Forgetting DSC vs EVC | Companies/LLPs *must* use DSC | Keep DSC token drivers installed & tested |
| Ignoring AIS before ITR | Mismatch notice u/s 143(1) | Reconcile AIS + 26AS + books first |

Pros also **never file on the last day** — portals crash on the 20th. They keep a filing calendar and file 2–3 days early.

## Learn-it roadmap & resources

**Time to job-ready: 6–10 weeks** of hands-on practice alongside theory.

| Week | Focus |
|---|---|
| 1–2 | GST basics + GSTN portal navigation; file a dummy nil GSTR-3B/1 |
| 3–4 | GSTR-2B reconciliation in Excel; e-invoice + e-way bill |
| 5–6 | TDS: sections, challans, TRACES, Form 16/16A |
| 7–8 | TallyPrime GST + Zoho Books; end-to-end monthly cycle |
| 9–10 | Income-tax e-filing: ITR, 26AS/AIS, notices |

**Resources:**
- **Free:** GSTN's own tutorials (tutorial.gst.gov.in), TRACES e-tutorials, Income Tax Dept YouTube, CBIC flyers. Practice on GSTN's offline tools (free download).
- **Paid:** ClearTax GST certification, Tally's TallyPrime with GST course (TallyEducation), Udemy "GST + TDS practical" courses (₹500–1,500 on sale).
- **Certifications that signal proficiency:** Tally ACE/Professional, ClearTax certifications, ICAI's GST certificate course (if eligible).

Best practice: get a **free trial ClearTax/Zoho account** and a GSTN test login, and actually file dummy returns. Nothing beats muscle memory on the real screens.

## Quick-reference

**GST return due dates**

| Return | Frequency | Due |
|---|---|---|
| GSTR-1 | Monthly / QRMP | 11th / 13th |
| GSTR-3B | Monthly / QRMP | 20th / 22nd–24th |
| GSTR-9 (annual) | Yearly | 31 Dec |

**Common TDS sections**

| Section | Payment | Rate |
|---|---|---|
| 192 | Salary | Slab |
| 194C | Contractor | 1% (indiv) / 2% (co.) |
| 194J | Professional/technical | 10% / 2% |
| 194I | Rent (land/bldg) | 10% |
| 194H | Commission | 2% |
| 194Q | Purchase of goods >₹50L | 0.1% |

**Key portal facts**
- GSTR-2B generated on the **14th**; basis for ITC. GSTR-2A is dynamic.
- ITC set-off: **IGST first**, then CGST, then SGST (no CGST↔SGST).
- e-Way bill validity: **1 day / 200 km**.
- Form 16A password = **TAN (caps)**.
- TDS deposit due: **7th of next month** (April–Feb); March by **30 April**.
- Company/LLP e-filing: **DSC mandatory**; others EVC allowed.
- ITC lapse deadline: **30 Nov** of next FY.
