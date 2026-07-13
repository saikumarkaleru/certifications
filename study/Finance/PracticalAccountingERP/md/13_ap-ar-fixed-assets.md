# AP, AR & Fixed-Asset Registers

## What it is & where it's used

Three sub-ledgers hang off every general ledger, and in a real accounts team they are usually three different desks:

- **Accounts Payable (AP)** — money you owe vendors. Governed by the **Purchase-to-Pay (P2P)** cycle: PR → PO → GRN → 3-way match → vendor invoice → payment.
- **Accounts Receivable (AR)** — money customers owe you. Governed by the **Order-to-Cash (O2C)** cycle: sales order → dispatch → invoice → collection → cash application.
- **Fixed-Asset Register (FAR)** — the list of every capitalised asset, its cost, location, and depreciation, feeding the depreciation schedule that hits P&L every month.

These are the entry-level and mid-level engine rooms of finance. **AP executive, AR / credit-control analyst, R2R (record-to-report) associate, fixed-asset accountant, and GL accountant** roles live here. In a Big-4 or GCC (Global Capability Centre) in Bengaluru/Hyderabad/Pune, "P2P analyst" and "O2C analyst" are literally two of the largest hiring pools. If you can run these three sub-ledgers and reconcile them to the GL, you are employable in accounts on day one.

## The gap: why companies want this (and college didn't teach it)

College teaches you the *journal entry* for a purchase and the *formula* for depreciation. It never shows you:

- That an invoice **cannot be posted** until it three-way-matches a PO and a GRN — so 40% of an AP job is chasing mismatches, not posting.
- **Ageing** — the single most-watched AP/AR metric — and how a bucketed ageing report is built and read.
- That depreciation in practice is driven by a **register with hundreds of line items**, block-of-assets rules under the Income-tax Act, and Schedule II useful lives under the Companies Act — two *different* depreciation numbers on the same asset.
- **GST input tax credit (ITC)** blocking, **TDS** deduction on vendor payments, and **e-invoice / IRN** validation — India-specific gates that decide whether a payable is even legal to pay.

Employers pay for the person who can take a messy vendor ledger and produce a clean, reconciled, aged, tax-correct sub-ledger. That is a *process* skill, not a formula.

## What "proficient" looks like

A job-ready person can, unaided:

1. Take a raw invoice register + PO register + GRN register and run a **3-way match** in Excel, flagging quantity/price/tax mismatches.
2. Build a **31/60/90/90+ ageing report** for AP or AR using formulas, and calculate **DSO / DPO**.
3. Post the full P2P and O2C journal entries **including GST and TDS**, and reconcile the sub-ledger control account to the GL.
4. Maintain a **fixed-asset register** and generate a **depreciation schedule** under both Companies Act Schedule II (SLM/WDV) and Income-tax block-WDV.
5. Do it in **TallyPrime** (India SME reality) and understand the same flow in an ERP (SAP FICO / Oracle / Zoho / NetSuite).

## Hands-on: how to actually do it

### 1. Three-way match (Excel)

Given three sheets — `PO`, `GRN`, `Invoice`, keyed on PO number — pull PO and GRN data next to each invoice line:

```excel
=XLOOKUP([@PO_No], PO[PO_No], PO[PO_Qty], "PO missing")
=XLOOKUP([@PO_No], GRN[PO_No], GRN[Recv_Qty], "GRN missing")
```

Then a match-status flag:

```excel
=IF(AND([@Inv_Qty]<=[@GRN_Qty], ABS([@Inv_Rate]-[@PO_Rate])<0.01),
   "MATCH", "HOLD-"&TEXTJOIN("/",TRUE,
     IF([@Inv_Qty]>[@GRN_Qty],"QTY",""),
     IF(ABS([@Inv_Rate]-[@PO_Rate])>=0.01,"PRICE","")))
```

Anything not `MATCH` goes on hold — you do not pay it.

### 2. Ageing report (Excel)

With an invoice `Due_Date` and a snapshot `AsOf` date:

```excel
=IF([@Balance]=0,"", $AsOf - [@Due_Date])        // days overdue
```

Bucket it:

```excel
=IFS([@Days]<=0,"Not due",[@Days]<=30,"0-30",
     [@Days]<=60,"31-60",[@Days]<=90,"61-90",TRUE,"90+")
```

Summarise the outstanding by bucket per party:

```excel
=SUMIFS(Inv[Balance], Inv[Party],[@Party], Inv[Bucket],"90+")
```

**DSO** (days sales outstanding) and **DPO**:

```excel
DSO = (Total AR / Credit Sales in period) * Days in period
DPO = (Total AP / Credit Purchases in period) * Days in period
```

### 3. Ageing / register in SQL

```sql
SELECT party_name,
  SUM(CASE WHEN days<=30            THEN balance END) AS d0_30,
  SUM(CASE WHEN days BETWEEN 31 AND 60 THEN balance END) AS d31_60,
  SUM(CASE WHEN days BETWEEN 61 AND 90 THEN balance END) AS d61_90,
  SUM(CASE WHEN days>90             THEN balance END) AS d90_plus,
  SUM(balance) AS total_due
FROM (
  SELECT party_name, balance,
         DATEDIFF(CURRENT_DATE, due_date) AS days
  FROM ar_open_items WHERE balance <> 0
) t
GROUP BY party_name
ORDER BY total_due DESC;
```

### 4. Depreciation schedule in Python

```python
import pandas as pd
far = pd.DataFrame({
    "asset":["Laptop-01","Plant-A","Delivery Van"],
    "cost":[80000, 2500000, 900000],
    "life_yrs":[3, 15, 8],          # Schedule II useful life
    "method":["SLM","WDV","WDV"]})

def dep(row):
    if row.method == "SLM":
        return round(row.cost / row.life_yrs, 2)          # no residual for simplicity
    rate = 1 - (0.05) ** (1/row.life_yrs)                  # WDV rate, 5% residual
    return round(row.cost * rate, 2)

far["annual_dep"] = far.apply(dep, axis=1)
print(far)
```

The WDV rate formula is the same one Schedule II implies: `rate = 1 − (residual/cost)^(1/life)`.

### 5. Journal entries (India, with GST & TDS)

**Purchase of ₹1,00,000 goods + 18% GST, TDS 194C @1% on a contractor bill:**

| Account | Dr | Cr |
|---|---|---|
| Purchases / Expense A/c | 1,00,000 | |
| Input CGST @9% | 9,000 | |
| Input SGST @9% | 9,000 | |
| &nbsp;&nbsp;To Vendor A/c | | 1,17,000 |

On payment with TDS ₹1,000:

| Account | Dr | Cr |
|---|---|---|
| Vendor A/c | 1,17,000 | |
| &nbsp;&nbsp;To TDS Payable (194C) | | 1,000 |
| &nbsp;&nbsp;To Bank | | 1,16,000 |

**Sale of ₹2,00,000 + 18% IGST (interstate):**

| Account | Dr | Cr |
|---|---|---|
| Customer A/c | 2,36,000 | |
| &nbsp;&nbsp;To Sales A/c | | 2,00,000 |
| &nbsp;&nbsp;To Output IGST | | 36,000 |

**Capitalising the ₹9,00,000 van + monthly depreciation:**

| Account | Dr | Cr |
|---|---|---|
| Fixed Asset – Vehicles | 9,00,000 | |
| Input CGST/SGST | 81,000 | |
| &nbsp;&nbsp;To Vendor | | 9,81,000 |
| Depreciation A/c (monthly) | 9,375 | |
| &nbsp;&nbsp;To Accumulated Depreciation | | 9,375 |

### 6. TallyPrime click-path

- **P2P:** Gateway → Vouchers → F9 Purchase → select party → stock item → GST auto-computes from ledger rates. For 3-way in Tally: enable *Purchase Order* (F11 → Enable PO) → Order → Receipt Note (GRN) → Purchase against them.
- **AR ageing:** Gateway → Display More Reports → Statements of Accounts → Ageing Analysis → set bucket ranges (0-30/31-60/…).
- **FAR:** create asset ledger under *Fixed Assets* group; book depreciation via Journal (F7) at month-end.

## Worked example / mini-project

**Reproduce this.** A trading firm, month of June 2026.

Vendor open items as on 30-Jun-2026:

| Vendor | Invoice | Inv Date | Due Date | Amount (₹) |
|---|---|---|---|---|
| Sharma Traders | P-101 | 05-Apr | 05-May | 1,20,000 |
| Sharma Traders | P-140 | 20-May | 19-Jun | 80,000 |
| Global Supply | P-155 | 02-Jun | 02-Jul | 2,50,000 |

Ageing as on 30-Jun: P-101 is 56 days overdue → **31-60**; P-140 is 11 days → **0-30**; P-155 not yet due. AP ageing:

| Vendor | 0-30 | 31-60 | Not due | Total |
|---|---|---|---|---|
| Sharma Traders | 80,000 | 1,20,000 | – | 2,00,000 |
| Global Supply | – | – | 2,50,000 | 2,50,000 |

**DPO** if June credit purchases were ₹15,00,000: `(4,50,000 / 15,00,000) × 30 = 9 days`.

**Fixed asset added 15-Jun-2026:** Plant ₹12,00,000, Schedule II life 15 yrs, SLM, 5% residual.
- Annual dep = (12,00,000 − 60,000) / 15 = ₹76,000.
- June (pro-rata 16 days of 30) = 76,000 × 16/365 ≈ **₹3,331**.
- Income-tax side: Plant & Machinery block, WDV @15%. Since put to use < 180 days in FY, **half depreciation** = 12,00,000 × 15% × ½ = ₹90,000 for the year. Two different numbers — that's the point.

Build the ageing sheet with the formulas above and tie the sub-ledger total (₹4,50,000) back to the AP control account in the GL. If it doesn't tie, you have an unposted invoice or a duplicate.

## How it's tested

- **Timed Excel test (30–45 min):** "Here's an invoice dump and a PO dump — build an ageing report and flag mismatches." They want XLOOKUP/SUMIFS/IFS, a pivot, and correct buckets.
- **SQL screen:** write the ageing CASE-WHEN query; compute DSO.
- **Case / "close these books":** given trial balance + a list of pending items, post accruals, book depreciation, reconcile AP/AR sub-ledger to GL.
- **Interview questions:** "Walk me through P2P." "What is a 3-way match and why?" "GRN posted, invoice not received at month-end — what entry?" (Answer: **GR/IR / goods-received-not-invoiced accrual**.) "Difference between Companies Act and Income-tax depreciation?" "How do you treat capital WIP?" "What is DSO and how do you reduce it?" "Blocked ITC under GST — give examples."

## Common mistakes & how pros avoid them

- **Paying an unmatched invoice.** Pros never release payment on a HOLD line; the match is the control.
- **Expensing a capital item** (or capitalising a repair). Rule of thumb: if it extends life or capacity → capitalise.
- **One depreciation number.** Pros keep the **Companies Act book and the Income-tax block-WDV in parallel**, and reconcile the deferred-tax difference.
- **Ignoring GR/IR at close.** Received-not-invoiced and invoiced-not-received both need accruals or the P&L is wrong.
- **Claiming blocked ITC** (motor vehicles, personal use, works contract) — reverses later with interest.
- **Ageing off invoice date, not due date.** Overdue is measured from the *due* date.
- **Sub-ledger not tied to GL.** Always reconcile the control account monthly — the number employers trust is the reconciled one.

## Learn-it roadmap & resources

| Stage | Time | Do this |
|---|---|---|
| Excel for AP/AR | 1 wk | XLOOKUP, SUMIFS, IFS, pivots on a sample ledger |
| P2P & O2C process | 1 wk | Map both cycles end-to-end; learn GR/IR, 3-way match |
| TallyPrime | 2 wks | Book purchases/sales with GST, PO/GRN, ageing, FAR |
| GST + TDS + Depreciation | 2 wks | ITC rules, TDS sections (194C/194J/194Q), Schedule II vs blocks |
| ERP exposure | ongoing | SAP FICO or Oracle basics; free NetSuite/Zoho trials |

**Resources:** ICAI study material (Accounting + Taxation) — you already have it; TallyPrime free educational mode; GSTN portal help; SAP FICO intro on Udemy; the *Corporate Finance Institute* AP/AR primers. **Certifications:** Tally certification, SAP FICO, or a GCC's internal R2R/P2P badge. Realistic time to job-ready: **6–8 weeks** of focused practice.

## Quick-reference

| Item | Key thing |
|---|---|
| P2P order | PR → PO → GRN → 3-way match → invoice → pay |
| O2C order | SO → dispatch → invoice → collect → cash apply |
| 3-way match | PO ≈ GRN ≈ Invoice (qty & price) |
| Ageing buckets | 0-30 / 31-60 / 61-90 / 90+ from **due date** |
| DSO | AR ÷ Credit Sales × Days |
| DPO | AP ÷ Credit Purchases × Days |
| Accrual at close | GR/IR (goods recd not invoiced) |
| SLM dep | (Cost − Residual) ÷ Life |
| WDV rate | 1 − (Residual/Cost)^(1/Life) |
| IT depreciation | Block WDV; ½ rate if used <180 days |
| TDS sections | 194C (contract 1/2%), 194J (prof 10%), 194Q (purchase 0.1%) |
| Blocked ITC | Motor vehicles, personal, works contract |
| Excel core | `XLOOKUP`, `SUMIFS`, `IFS`, `DATEDIF`, PivotTable |

Master these three sub-ledgers and their reconciliations, and you can walk into any AP/AR/R2R desk in an Indian GCC or SME and be productive in a week.
