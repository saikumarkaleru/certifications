# GST in practice III: Annual Return & Notices

## What it is & where it's used

The GST **annual return (GSTR-9)** and the **reconciliation statement (GSTR-9C)** are the year-end "close" of the GST cycle. Every month or quarter you filed GSTR-1 (outward supplies) and GSTR-3B (summary + tax payment); the annual return rolls all of that into one consolidated filing per GSTIN per financial year, reconciled against your books.

Beyond the return, GST is now a **notice-heavy regime**. The department runs automated matching (GSTR-1 vs 3B, 3B vs 2B, e-way bills vs sales, e-invoice vs GSTR-1) and throws out scrutiny notices — **ASMT-10** (scrutiny discrepancy), **DRC-01A / DRC-01** (demand), **DRC-03** (voluntary payment), plus ADT-01 for departmental audit. Knowing how to read, reconcile and *reply* to these is a core, billable skill.

**Roles that need this:** GST/indirect-tax executives, accounts payable/receivable leads doing month-end and year-end, tax analysts in a Big-4 or mid-tier firm, finance managers signing off the annual return, and anyone in a consulting practice handling client compliance. In an audit/consulting firm, "can you draft an ASMT-10 reply and finalise 9C" is a direct hiring criterion.

## The gap: why companies want this (and college didn't teach it)

College teaches GST *law* — sections, definitions, the constitutional backstory. It does **not** teach you to:

- Open a GSTR-9 offline utility, map ledger balances into 17 tables, and explain a `Table 8` ITC difference.
- Reconcile **turnover as per books vs turnover as per GSTR-9** and defend the delta (unbilled revenue, credit notes, schedule-III items, cross-charge).
- Read a system-generated ASMT-10 that says "ITC in 3B exceeds 2B by ₹4,32,118" and produce a line-item reconciliation instead of panicking.
- Decide *when to pay via DRC-03* and *when to contest*, and draft the covering reply.

Employers pay for the person who closes the loop: books → returns → reconciliation → notice reply → resolution. That end-to-end confidence is the gap.

## What "proficient" looks like

A job-ready person can, unaided:

1. **File GSTR-9** end-to-end: pull auto-populated data, correct Tables 4–9, 10–14, and 17–18, and reconcile ITC (Table 6 vs Table 8).
2. **Prepare GSTR-9C**: reconcile turnover (Table 5), tax paid (Table 9), ITC (Table 12–14), and quantify any additional liability payable through DRC-03.
3. **Build a reconciliation working** in Excel that ties GSTR-1, 3B, 2B and books, with a clear "reason for difference" column.
4. **Respond to ASMT-10 within 30 days** with a reasoned reply (ASMT-11) plus annexures.
5. **Handle a DRC-01A/01**: agree-and-pay via DRC-03, or contest via DRC-06, knowing the limitation and pre-deposit rules.

## Hands-on: how to actually do it

### GSTR-9: portal click-path

```
GST Portal → Login → Services → Returns → Annual Return
→ Select FY → GSTR-9 "Prepare Online"
→ Download: (a) GSTR-9 System Computed Summary (PDF)
            (b) GSTR-1 Summary, (c) GSTR-3B Summary
→ Fill Tables 4–19 → Compute Liability → Pay any diff via DRC-03
→ File with DSC/EVC
```

Key tables and where numbers come from:

| Table | Content | Source |
|-------|---------|--------|
| 4 | Outward taxable supplies (B2B, B2C, exports, RCM) | GSTR-1 |
| 5 | Exempt / nil / non-GST outward | GSTR-1 |
| 6 | ITC availed (inputs / capital goods / services / RCM) | GSTR-3B |
| 7 | ITC reversed (Rule 42/43, 37, ineligible) | Books |
| 8 | ITC reconciliation: 2A/2B vs availed | Auto + books |
| 9 | Tax paid | GSTR-3B |
| 10–14 | Prior-year adjustments in next-year returns | GSTR-1/3B of Apr–Oct next FY |
| 17–18 | HSN summary outward / inward | Books |

### The core Excel reconciliation (3B vs 2B ITC — the #1 notice trigger)

Lay out one row per GSTIN of the supplier. Use `SUMIFS` to net books vs portal, then a reason column.

```excel
' Books ITC per supplier (from purchase register)
=SUMIFS(Books[ITC], Books[GSTIN], A2)

' 2B ITC per supplier (from downloaded GSTR-2B)
=SUMIFS(GSTR2B[ITC], GSTR2B[GSTIN], A2)

' Difference
=D2 - E2                     ' Books minus 2B

' Auto-tag the reason
=IFS( ABS(F2)<1, "Matched",
      F2>0,  "In books, not in 2B (supplier not filed / timing)",
      F2<0,  "In 2B, not in books (missed invoice / RCM)" )
```

To match a single invoice both ways, `XLOOKUP` on a concatenated key:

```excel
=XLOOKUP(A2&B2, GSTR2B[GSTIN]&GSTR2B[InvNo], GSTR2B[TaxableValue], "NOT IN 2B")
```

### SQL: pull the mismatch straight from your ERP

```sql
SELECT  b.supplier_gstin,
        SUM(b.igst + b.cgst + b.sgst)          AS itc_books,
        COALESCE(SUM(g.itc_total), 0)          AS itc_2b,
        SUM(b.igst + b.cgst + b.sgst)
          - COALESCE(SUM(g.itc_total), 0)      AS diff
FROM    purchase_register b
LEFT JOIN gstr2b g
       ON  b.supplier_gstin = g.supplier_gstin
       AND b.invoice_no     = g.invoice_no
       AND b.fin_year        = '2024-25'
GROUP BY b.supplier_gstin
HAVING  ABS(SUM(b.igst + b.cgst + b.sgst) - COALESCE(SUM(g.itc_total),0)) > 1
ORDER BY ABS(diff) DESC;
```

### Python: turnover recon for GSTR-9C Table 5

```python
import pandas as pd

books = pd.read_excel("trial_balance_revenue.xlsx")   # ledger-wise revenue
gstr9 = 24_50_00_000        # outward turnover per GSTR-9 Table 4/5

recon = pd.DataFrame([
    ("Turnover as per audited financials", books["amount"].sum()),
    ("Add: Unbilled revenue at year-end",  -12_00_000),  # not yet in GST
    ("Less: Credit notes not in books",     -4_50_000),
    ("Add: Schedule III / non-GST supply",  -8_00_000),
    ("Less: Cross-charge to branches",      15_00_000),
], columns=["particulars", "amount"])

recon.loc[len(recon)] = ("Turnover as per GSTR-9", recon["amount"].sum())
recon["check_vs_9"] = recon["amount"].iloc[-1] - gstr9   # should be ~0
print(recon.to_string(index=False))
```

### Journal entry when 9C throws up extra liability

You pay short-paid GST through **DRC-03** (cash only, no ITC). Book it as:

| Account | Dr | Cr |
|---------|-----|-----|
| GST Expense / Prior-period tax (P&L) | ₹50,000 | |
| Interest on GST (P&L) | ₹9,000 | |
| To Bank (DRC-03 challan) | | ₹59,000 |

If it relates to reversed ITC:

| Account | Dr | Cr |
|---------|-----|-----|
| ITC Reversed – Expense | ₹50,000 | |
| To Input CGST/SGST/IGST | | ₹50,000 |

### Responding to notices — the mechanics

| Notice | Meaning | Your reply form | Deadline |
|--------|---------|-----------------|----------|
| ASMT-10 | Scrutiny discrepancy | ASMT-11 (+ annexures) | 30 days |
| DRC-01A | Pre-show-cause intimation | Part B of DRC-01A / DRC-03 | ~15 days |
| DRC-01 | Show cause notice (demand) | DRC-06 | 30 days |
| DRC-03 | *You* pay voluntarily | — (challan) | Anytime |
| ADT-01 | Departmental audit notice | Produce records | As stated |

Portal path to reply: `Services → User Services → View Additional Notices/Orders → View → Reply`. Attach a signed PDF reconciliation as annexure.

## Worked example / mini-project

**Scenario — Acme Traders Pvt Ltd, FY 2024-25.** Reconcile and respond to an ASMT-10.

Data:

| Item | GSTR-3B (₹) | GSTR-2B (₹) | Books (₹) |
|------|-------------|-------------|-----------|
| ITC availed | 42,00,000 | 39,50,000 | 41,80,000 |

The system issues **ASMT-10**: "ITC availed in GSTR-3B (₹42,00,000) exceeds ITC in GSTR-2B (₹39,50,000) by ₹2,50,000. Explain."

**Step 1 — Build the bridge.**

| Reconciliation item | ₹ |
|---------------------|-----|
| ITC as per 2B | 39,50,000 |
| Add: RCM ITC (self-invoiced, not in 2B) | 1,20,000 |
| Add: Invoices filed by supplier in Apr-2025 2B (timing) | 90,000 |
| Add: Import IGST (from ICEGATE, not vendor 2B) | 60,000 |
| **Explained ITC** | **42,20,000** |
| ITC in 3B | 42,00,000 |
| Excess claimed to reverse | Nil (books ₹41,80,000; ₹20,000 already reversed) |

**Step 2 — Conclusion.** The ₹2,50,000 gap is fully explained by RCM, import IGST and timing — all legitimate. Nothing to pay. A ₹20,000 ineligible item was already reversed in March-2025 3B.

**Step 3 — File ASMT-11** attaching the above table plus RCM self-invoices, bill of entry, and the April 2B extract. Closing line: *"In view of the above reconciliation, the difference is fully explained and no further tax is payable. We request closure of proceedings."*

**Step 4 — If ₹20,000 were NOT already reversed:** pay via DRC-03 (`Services → User Services → My Applications → Intimation of Voluntary Payment DRC-03 → Cause = Scrutiny`), ₹20,000 tax + interest @18% p.a., and reference the ARN in the ASMT-11 reply.

## How it's tested

**Interview questions**

- "Turnover per books is ₹50 Cr but GSTR-9 shows ₹48.5 Cr. Give me five reasons for the difference." (Unbilled revenue, credit notes, Schedule-III, cross-charge, financial-year cut-off / advances.)
- "Difference between Table 6 and Table 8 of GSTR-9?"
- "You get an ASMT-10 for 3B-vs-2B ITC excess. Walk me through your reply."
- "When do you use DRC-03 vs DRC-06?"
- "Is GSTR-9C still audited by a CA?" (Now self-certified since FY 2020-21; no mandatory CA audit, but a reconciliation statement is filed if turnover > ₹5 Cr.)

**Practical assessment (very common)** — you're handed three files (GSTR-1 summary, 3B summary, purchase register) and asked to:

1. Produce a 3B-vs-2B ITC reconciliation with a reason column (timed, ~45 min in Excel).
2. Draft a one-page ASMT-11 reply from a sample notice.
3. Fill Table 8 of GSTR-9 and state the eligible ITC.

Firms grade on whether your reconciliation *ties* and whether your reasons are defensible.

## Common mistakes & how pros avoid them

- **Treating GSTR-9 as auto-filed.** The portal pre-fills, but *you* must correct Tables 6–8 and 17. Pros always download and re-derive.
- **Ignoring next-year adjustments (Tables 10–14).** Amendments and ITC of last FY claimed in Apr–Oct of the next FY must be reported here — most people miss it and create a false mismatch.
- **Reversing ITC on RCM/import just because it's not in 2B.** RCM and import IGST legitimately don't appear in 2B — never reverse them to "match".
- **Missing the 30-day ASMT-10 window.** No reply → best-judgment assessment (ASMT-13). Diarise every notice the day it lands.
- **Paying disputed demand via DRC-03 out of fear.** If you have a defensible position, contest via DRC-06; a DRC-03 payment can be read as admission.
- **Not reconciling e-invoice / e-way bill to GSTR-1.** The department does — a sales-vs-eway gap is a fresh notice waiting to happen.
- **Interest not computed.** Any short-paid tax carries 18% p.a.; forgetting it invites a follow-up demand.

## Learn-it roadmap & resources

**Time to proficiency:** ~6–8 weeks part-time if you already know monthly GST.

| Week | Focus |
|------|-------|
| 1–2 | Master 3B-vs-2B and 1-vs-3B reconciliation in Excel |
| 3 | GSTR-9 tables end-to-end on the offline utility |
| 4 | GSTR-9C turnover, tax and ITC reconciliation |
| 5 | Notices: ASMT-10/11, DRC family, draft sample replies |
| 6 | Departmental audit (ADT-01), records to keep, limitation |
| 7–8 | Full mock: file a dummy 9/9C and answer a sample notice |

**Resources**

- GST Portal help + downloadable GSTR-9/9C **offline utilities** (free, hands-on practice).
- **CBIC** notifications & the CGST Act s.44 (annual return), s.61 (scrutiny), s.65 (audit), s.73/74 (demands).
- ICAI *Technical Guide on Annual Return & Reconciliation Statement* (free PDF) — the practitioner's bible.
- ClearTax / TaxGuru walkthroughs for portal screens; Taxmann GST reckoner for rates.
- **Certification:** ICAI Certificate Course on GST, or the government **GST Practitioner (GSTP)** enrolment for practice.

## Quick-reference

| Form | Purpose |
|------|---------|
| GSTR-9 | Annual return (turnover > ₹2 Cr; optional below) |
| GSTR-9C | Reconciliation statement, self-certified (turnover > ₹5 Cr) |
| ASMT-10 / 11 | Scrutiny notice / reply |
| ASMT-13 | Best-judgment assessment (if no reply) |
| DRC-01A | Pre-SCN intimation |
| DRC-01 / 06 | Show cause notice / reply |
| DRC-03 | Voluntary / scrutiny payment (cash only) |
| ADT-01 / 02 | Audit notice / findings |

**Key deadlines:** GSTR-9 & 9C — **31 Dec** of next FY. ASMT-10 reply — **30 days**. DRC-01 reply — **30 days**.

**Interest:** 18% p.a. on short-paid tax; ITC-related interest under s.50.

**Limitation for demands:** s.73 (non-fraud) — 3 years; s.74 (fraud) — 5 years from annual-return due date.

**Golden rules of reconciliation**
```
Books  ─┐
GSTR-1 ─┼─► must tie ◄─┬─ GSTR-3B
2B     ─┘             └─ e-invoice / e-way bill
RCM & Import IGST → in books, NOT in 2B → never reverse to match
Every difference needs a named reason. No unexplained delta.
```
