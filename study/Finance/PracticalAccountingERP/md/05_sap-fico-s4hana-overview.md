# SAP FICO / S/4HANA for Finance

## What it is & where it's used

SAP is the accounting engine that runs most large companies on earth. **FICO** is the finance half of SAP: **FI (Financial Accounting)** produces the statutory books — General Ledger, Accounts Payable, Accounts Receivable, Asset Accounting, Bank — that feed the balance sheet and P&L. **CO (Controlling)** is the management-accounting side — cost centres, profit centres, internal orders, product costing, profitability analysis (CO-PA). **S/4HANA** is SAP's current-generation product (the successor to ECC 6.0) built on the in-memory HANA database, where FI and CO are merged into a single table called the **Universal Journal (ACDOCA)** — one line item now carries both the GL account and the cost object, so there's no more month-end reconciliation between FI and CO.

Where it's used: every Nifty-50 company, most listed mid-caps, and — critically for an India-based candidate — the **Global Capability Centres (GCCs)** and Big-4 / captive shared-service centres in Bengaluru, Hyderabad, Pune, Gurgaon and Chennai. Roles that require it: **R2R (Record-to-Report) analyst, P2P (AP) associate, O2C (AR) associate, GL accountant, SAP FICO consultant, financial analyst, internal auditor, and tax analyst.** If a job description says "hands-on SAP" and pays a premium over a Tally job, this is the skill they mean.

## The gap: why companies want this (and college didn't teach it)

An MBA or CA course teaches you *what* a journal entry is and *how* to prepare a trial balance by hand. It never teaches you that in a real company you **never touch the trial balance directly** — you post a document, the system derives the GL impact, and controls stop you from doing anything stupid. Colleges teach Tally at best, where one person does everything on one screen. SAP is the opposite: it is **built for control and scale**, where AP, AR, GL and treasury are separate teams, every posting leaves an audit trail, and a document once posted **cannot be deleted** (only reversed).

The specific gap employers pay to close:

- You think in **T-accounts**; SAP thinks in **document types, posting keys, and GL account determination**.
- You've never seen **automated postings** (tax, WHT/TDS, exchange differences, GR/IR clearing) that the system generates for you.
- You don't know **org structure** — that a "company" in SAP is a *Company Code*, and one instance can run 40 legal entities across 12 countries simultaneously.
- You've never done a **period-end close** on a clock with SLA penalties.

A fresher who can navigate SAP, post a vendor invoice, run FBL3N, and explain the P2P cycle is instantly worth more than one who only knows theory.

## What "proficient" looks like

The concrete bar an R2R/AP/AR hire is tested against:

1. **Navigate by T-code** without hunting through menus — type `/nFB60`, `Enter`, you're on the vendor-invoice screen.
2. **Post the four core documents unaided**: GL journal (FB50), vendor invoice (FB60), customer invoice (FB70), general posting with both debit and credit lines (F-02).
3. **Read a GL account** using FBL3N and explain every line — distinguish open items from cleared items, drill into the source document (FB03).
4. **Explain the org structure**: Client → Company Code → Chart of Accounts → Business Area / Profit Centre / Cost Centre.
5. **Explain the end-to-end cycles**: P2P (PR → PO → GR → Invoice → Payment) and O2C (Order → Delivery → Billing → Receipt), and where FI hooks in.
6. **Clear open items** (F-32 customer, F-44 vendor, F.13 auto-clearing) and understand **GR/IR** reconciliation.
7. **Know what changed in S/4HANA**: Universal Journal, Business Partner (replaces separate customer/vendor masters), New Asset Accounting, Fiori apps.

## Hands-on: how to actually do it

**Org structure (memorise this hierarchy):**

```
Client (e.g. 100)            ← top of the SAP box; shared master data
  └─ Company Code (e.g. 1000, "ACME India Pvt Ltd")  ← a legal entity, produces B/S + P&L
       ├─ Chart of Accounts (e.g. YCOA)   ← the GL account master list
       ├─ Business Area / Segment
       ├─ Profit Centre     (CO — internal P&L slice)
       └─ Cost Centre       (CO — where costs land: HR, IT, Finance)
```

**The core T-codes (type into the command box, prefix with /n to switch):**

| T-code  | What it does                                | Tally equivalent            |
|---------|---------------------------------------------|-----------------------------|
| FB50    | Post GL journal (GL accounts only)          | Journal Voucher (F7)        |
| FB60    | Post vendor (AP) invoice                     | Purchase Voucher (F9)       |
| FB70    | Post customer (AR) invoice                   | Sales Voucher (F8)          |
| F-02    | General posting, manual Dr/Cr, any account   | Journal with full control   |
| FB03    | Display any posted document                   | Drill into voucher          |
| FBL3N   | GL account line-item display                  | Ledger display              |
| FBL1N   | Vendor line items                             | Party ledger (creditor)     |
| FBL5N   | Customer line items                           | Party ledger (debtor)       |
| F-53 / F110 | Manual / automatic outgoing payment       | Payment Voucher (F5)        |
| FB08    | Reverse a document                            | Delete/alter voucher        |
| F-32 / F-44 | Clear customer / vendor open items        | Bill-wise adjustment        |

**Posting keys** (the two-digit code that tells SAP debit-or-credit and account type — this trips up every fresher):

| Posting key | Meaning              |
|-------------|----------------------|
| 40          | GL account — Debit   |
| 50          | GL account — Credit  |
| 01          | Customer — Debit (invoice) |
| 31          | Vendor — Credit (invoice)  |
| 25          | Vendor — Debit (payment)   |

**Posting vs Tally — the mental shift.** In Tally you *are* the ledger. In SAP you post a **document** with a header (date, type, company code) and line items; the system derives the GL hit, adds tax and TDS lines automatically, assigns a **document number** from a range, and freezes it. You can't delete — only **reverse (FB08)**, which creates an equal-and-opposite document. Every field is validated against master data before it saves.

**Example: post a vendor invoice via FB60 (click-path).**
1. `/nFB60` → set **Company Code** 1000.
2. **Vendor** = 100234, **Invoice date**, **Posting date**, **Amount** ₹1,18,000, **Currency** INR.
3. **Tax** tab: tax code `V0`/GST code; tick *Calculate tax* so SAP splits the ₹18,000 GST.
4. Line item: GL account 400100 (Office Expenses), amount ₹1,00,000, **Cost Centre** IN-ADMIN.
5. Check the **simulate** button (traffic light green) → **Post**. Document 1900000123 created.

The entry SAP builds behind that one screen:

| Posting key | Account                    | Dr (₹)    | Cr (₹)    |
|-------------|----------------------------|-----------|-----------|
| 40          | Office Expenses (400100)    | 1,00,000  |           |
| 40          | Input CGST (154010)          | 9,000     |           |
| 40          | Input SGST (154020)          | 9,000     |           |
| 31          | Vendor — ACME Supplies (100234) |       | 1,18,000  |

## Worked example / mini-project

**Scenario:** You are a GL analyst at a Bengaluru GCC. Reproduce a mini month-end for Company Code 1000 (April 2026).

**Step 1 — Rent accrual (FB50).** Rent of ₹5,00,000 for April is unpaid at month-end.

| PK | Account                      | Dr (₹)   | Cr (₹)   |
|----|------------------------------|----------|----------|
| 40 | Rent Expense (401200)         | 5,00,000 |          |
| 50 | Accrued Expenses (250100)     |          | 5,00,000 |

**Step 2 — Customer invoice (FB70).** Bill client TechCorp ₹11,80,000 incl. 18% GST.

| PK | Account                        | Dr (₹)     | Cr (₹)     |
|----|--------------------------------|------------|------------|
| 01 | Customer — TechCorp (200500)    | 11,80,000  |            |
| 50 | Consulting Revenue (300100)      |            | 10,00,000  |
| 50 | Output CGST (254010)             |            | 90,000     |
| 50 | Output SGST (254020)             |            | 90,000     |

**Step 3 — Receipt & clearing (F-28, then F-32).** TechCorp pays ₹11,80,000. Post the incoming payment, then clear the open invoice against the receipt so the customer line nets to zero.

**Step 4 — Verify with FBL3N.** Run FBL3N on GL 300100 (Consulting Revenue) for 01.04.2026–30.04.2026, status *All items*. You should see the ₹10,00,000 credit. Drill in (double-click → FB03) to confirm it traces to your FB70 document.

**Step 5 — Reversal test.** Say Step 1 rent should have been ₹4,00,000. Do **not** edit — reverse document via **FB08** (reversal reason 01), then re-post the correct amount. Now FBL3N on 401200 shows three lines (original +5,00,000, reversal −5,00,000, correct +4,00,000) — a clean audit trail no auditor can object to.

This five-step flow *is* what an R2R analyst does 200 times a month.

## How it's tested

**Interview questions (verbal screen):**
- "Walk me through the P2P cycle and where FI gets hit." (Expected: PR → PO → GR posts *Dr Inventory / Cr GR-IR*; Invoice posts *Dr GR-IR / Cr Vendor*; Payment posts *Dr Vendor / Cr Bank*.)
- "Difference between FB50, FB60 and F-02?" (FB50 = GL only; FB60 = vendor sub-ledger; F-02 = fully manual, any account/posting key.)
- "What is GR/IR and why does it need clearing?"
- "Cost centre vs profit centre vs internal order?"
- "What changed in S/4HANA vs ECC?" (Universal Journal ACDOCA, Business Partner, New Asset Accounting, Fiori, no FI-CO reconciliation.)
- "How do you correct a wrongly posted document?" (Reverse via FB08 — never delete.)

**Practical / assessment tests:**
- A **live-system or screenshot exercise**: "Here's a vendor bill — post it in FB60 and show the document number and the resulting entry."
- A **journalising test**: given 8–10 business events, write the Dr/Cr with correct posting keys.
- A **"read this FBL3N" screen**: identify open vs cleared items and explain a suspense balance.
- A **close case**: "These four accruals are pending and the sub-ledger doesn't tie to GL — what do you do first?"

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | Pro habit |
|---------|-------------|-----------|
| Trying to *delete* a posted document | Impossible; flags you as a non-user | Always **reverse (FB08)** |
| Confusing Company Code with Client | Wrong-entity posting | Company Code = legal entity; check it first, every time |
| Wrong posting key (40 vs 50) | Entry lands on the wrong side | Memorise 40/50/01/31/25 cold |
| Ignoring **document date vs posting date** | Wrong period / GST return mismatch | Posting date drives the accounting period |
| Manually keying tax/TDS lines | SAP auto-derives them; manual = imbalance | Use tax codes, tick *Calculate tax* |
| Posting to a **cost element without a cost object** | Hard error in CO | Always attach cost centre/order on P&L accounts |
| Confusing open-item vs cleared | Reconciliation chaos | Learn F-32/F-44 clearing early |
| Leaving items in **GR/IR** unresolved | Audit finding at year-end | Run **MR11 / F.13** regularly |

## Learn-it roadmap & resources

**Realistic time-to-proficiency:** 4–8 weeks part-time to interview-ready as an *end user* (post, display, clear, explain cycles). 4–6 months for a **consultant-level** understanding (configuration, org structure setup, integration).

| Week | Focus |
|------|-------|
| 1 | Navigation, org structure, GL master data, FB50 |
| 2 | AP: FB60, F-53, vendor line items (FBL1N) |
| 3 | AR: FB70, F-28, clearing (F-32) |
| 4 | Month-end: accruals, reversals (FB08), FBL3N reporting |
| 5–6 | CO basics: cost centres, profit centres, CO-PA concept |
| 7–8 | P2P & O2C end-to-end; S/4HANA differences; Fiori |

**Resources:**
- **SAP Learning Hub / learning.sap.com** — free "SAP S/4HANA for Financial Accounting Associates" learning journey (aligns with cert **C_TS4FI**).
- **openSAP** free courses on S/4HANA Finance.
- Practice access: a **free trial/IDES sandbox** or an institute-provided server (a real login beats any video).
- Books: *SAP S/4HANA Finance: An Introduction* (SAP Press); *Configuring SAP S/4HANA Finance*.
- **Certification worth doing:** SAP Certified Associate — SAP S/4HANA Cloud Public Edition, Finance (`C_TS4FI` / `C_S4CFI`). For an *accountant* role, hands-on beats the cert; for a *consultant* role, the cert matters.

## Quick-reference

**Org hierarchy:** Client → Company Code (legal entity) → Chart of Accounts → Business Area / Profit Centre / Cost Centre.

**Must-know T-codes:** FB50 (GL post) · FB60 (vendor inv) · FB70 (customer inv) · F-02 (general/manual) · FB03 (display doc) · FBL3N (GL items) · FBL1N (vendor) · FBL5N (customer) · FB08 (reverse) · F-32/F-44 (clear cust/vendor) · F110 (auto payment run) · F.13 (auto-clear) · MR11 (GR/IR clear).

**Posting keys:** 40 = GL Dr · 50 = GL Cr · 01 = Customer Dr · 31 = Vendor Cr · 25 = Vendor Dr.

**P2P entries:** GR → *Dr Inventory / Cr GR-IR* · Invoice → *Dr GR-IR / Cr Vendor* · Payment → *Dr Vendor / Cr Bank*.

**O2C entries:** Billing → *Dr Customer / Cr Revenue + Output GST* · Receipt → *Dr Bank / Cr Customer*.

**S/4HANA one-liners:** Universal Journal = **ACDOCA** (FI + CO in one table) · **Business Partner** replaces separate customer/vendor masters · **New Asset Accounting** · **Fiori** UI · no FI-CO reconciliation.

**Golden rule:** Never delete — **reverse (FB08)**. Every posting leaves a trail.
