# Tax-tech & automation

## What it is & where it's used

"Tax-tech" is the stack of software, scripts and glue that turns a manual, deadline-driven compliance job into a repeatable, auditable pipeline. In practice it means three things:

1. **Reconciliation engines** — matching GSTR-2B vs your purchase register, TDS 26AS/AIS vs books, bank vs cash book, vendor ledger vs their ledger.
2. **Return automation** — pushing invoice data from your ERP/accounting system to the GST portal, TRACES, or the income-tax utility via APIs or JSON, instead of keying it in.
3. **AI/ML assist** — document extraction (OCR of invoices), anomaly flags ("this HSN usually attracts 18%, you booked 5%"), and drafting notice replies.

Who needs it: GST practitioners, indirect-tax analysts in industry, TDS/payroll teams, statutory-audit associates running substantive testing, FP&A analysts who own the tax provision, and anyone in a **GSP/ASP** (GST Suvidha Provider / Application Service Provider) or Big-4 managed-services team. If your job title contains "tax", "compliance", "audit", "AR/AP", or "finance analyst", part of your value is now measured in *how few hours a month you spend keying and matching*.

## The gap: why companies want this (and college didn't teach it)

MBA and CA-Inter teach you **what** GSTR-2B is and the *law* behind Section 16(2)(aa) ITC matching. They do not teach you what to do when you have a 40,000-row purchase register and a 38,000-row 2B that don't tie out, due tomorrow.

The industry reality:

| College taught | Job actually needs |
|---|---|
| "Reconcile ITC as per rules" | Match 40k rows in 20 min with a repeatable macro |
| Definition of TDS sections | Bulk-validate 26AS vs books, isolate mismatches |
| Manual return filing walkthrough | Generate portal JSON from ERP, no re-keying |
| "Maintain documentation" | Version-controlled, audit-trailed, re-runnable |

Companies pay for tax-tech because manual work **doesn't scale, isn't auditable, and breaks at month-end**. A person who can hand back a reconciled file with the mismatches *categorised and explained* is worth 3x one who "will get to it." This chapter closes the gap between knowing the rule and shipping the reconciled file.

## What "proficient" looks like

A job-ready person can, **unaided**:

- Take two exports (register + 2B) and produce a four-bucket reconciliation — *matched, mismatch-in-value, in-books-not-in-2B, in-2B-not-in-books* — in Excel or Python.
- Write a `XLOOKUP`/`SUMIFS` recon and know its failure modes (duplicate GSTINs, trailing spaces, invoice-number formatting).
- Build the same recon in SQL when the data is 500k rows and won't fit Excel.
- Use a pivot / Power Query to refresh the recon monthly with one click.
- Read and generate the **GSTR-1 JSON schema**, understand the offline utility, and know where APIs (via a GSP) replace it.
- Explain what should stay manual (judgement, notice replies) vs automated (matching, arithmetic).

You are *not* expected to build the AI model. You are expected to **use** the tools and **verify** their output — the tool proposes, you dispose.

## Hands-on: how to actually do it

### 1. The GST ITC reconciliation in Excel

Assume `Books` sheet and `GSTR2B` sheet, each with columns: `GSTIN`, `InvoiceNo`, `Taxable`, `IGST`, `CGST`, `SGST`. First build a clean match key (never match on invoice number alone — normalise it):

```excel
' Match key: GSTIN + cleaned invoice no (upper, no spaces/special chars)
=UPPER(SUBSTITUTE(TRIM([@GSTIN])&"|"&[@InvoiceNo]," ",""))
```

Pull the 2B taxable value against each books row:

```excel
=XLOOKUP([@MatchKey], GSTR2B[MatchKey], GSTR2B[Taxable], "NOT IN 2B", 0)
```

Bucket the result:

```excel
=IF(D2="NOT IN 2B","In books, not in 2B",
   IF(ROUND(D2-[@Taxable],0)=0,"Matched",
   "Value mismatch: "&TEXT(D2-[@Taxable],"₹#,##0")))
```

Reverse-check (rows in 2B missing from books) with a `COUNTIFS` on the 2B sheet:

```excel
=IF(COUNTIFS(Books[MatchKey],[@MatchKey])=0,"In 2B, not in books","OK")
```

Summarise with a pivot, or:

```excel
=SUMIFS(Books[IGST], Books[Bucket], "Matched")   ' safe-to-claim ITC
```

### 2. Same recon in SQL (when Excel dies)

```sql
SELECT
    COALESCE(b.match_key, g.match_key)               AS match_key,
    b.taxable                                        AS books_taxable,
    g.taxable                                        AS gstr2b_taxable,
    CASE
        WHEN b.match_key IS NULL THEN 'In 2B, not in books'
        WHEN g.match_key IS NULL THEN 'In books, not in 2B'
        WHEN ROUND(b.taxable - g.taxable, 0) = 0 THEN 'Matched'
        ELSE 'Value mismatch'
    END                                              AS bucket,
    ROUND(COALESCE(b.taxable,0) - COALESCE(g.taxable,0), 2) AS diff
FROM books b
FULL OUTER JOIN gstr2b g ON b.match_key = g.match_key
ORDER BY bucket, diff DESC;
```

A `FULL OUTER JOIN` on the normalised key is the entire recon — both "missing" buckets fall out for free. (In MySQL, which lacks FULL OUTER JOIN, emulate with `LEFT JOIN ... UNION ... RIGHT JOIN`.)

### 3. Automating it in Python (monthly, re-runnable)

```python
import pandas as pd

def clean_key(df):
    df["key"] = (df["GSTIN"].str.strip().str.upper() + "|" +
                 df["InvoiceNo"].str.replace(r"[^A-Za-z0-9]", "", regex=True))
    return df

books = clean_key(pd.read_excel("books.xlsx"))
b2b   = clean_key(pd.read_excel("gstr2b.xlsx"))

m = books.merge(b2b, on="key", how="outer",
                suffixes=("_bk", "_2b"), indicator=True)

def bucket(r):
    if r["_merge"] == "left_only":  return "In books, not in 2B"
    if r["_merge"] == "right_only": return "In 2B, not in books"
    return "Matched" if round(r.Taxable_bk - r.Taxable_2b) == 0 else "Value mismatch"

m["bucket"] = m.apply(bucket, axis=1)
m.to_excel("recon_output.xlsx", index=False)
print(m["bucket"].value_counts())
```

Run it every month by dropping two files in a folder — 30 seconds vs a day.

### 4. AI-assist: invoice extraction + anomaly flag

OCR a scanned invoice to structured fields (Tesseract free, or cloud Document AI), then apply a rules layer the "AI" can't be trusted to get right alone:

```python
# after OCR gives fields dict: {"hsn":"8471", "rate":5, "taxable":100000}
EXPECTED = {"8471": 18}          # HSN 8471 (computers) → 18%
flag = "REVIEW: rate looks wrong" if EXPECTED.get(fields["hsn"]) != fields["rate"] else "ok"
```

The model reads; **your rules table decides**. That is the professional pattern for AI in compliance.

### 5. Portal / Tally click-paths

- **GSTR-1 (offline utility):** GST portal → Downloads → Offline Tools → *Returns Offline Tool* → paste/import Excel → *Generate JSON* → upload on portal → *Preview* → *Submit* → *File with EVC/DSC*.
- **GSTR-2B download:** portal → Returns Dashboard → select period → GSTR-2B → *Download* (Excel/JSON) — this is your recon input.
- **TallyPrime GSTR-1 export:** Gateway of Tally → Display More Reports → GST Reports → GSTR-1 → `Alt+E` (Export) → JSON → upload to portal.
- **API route:** enterprises skip the portal and file through a **GSP** (ClearTax/Cygnet/Zoho) via authenticated API — data flows ERP → GSP → GSTN with an audit trail and no manual JSON.

## Worked example / mini-project

**Scenario:** Acme Traders Pvt Ltd, March 2026. You must finalise ITC before filing GSTR-3B.

Purchase register (books): 5 invoices. GSTR-2B (as downloaded): 5 lines. Amounts in ₹.

**Books**

| GSTIN | InvoiceNo | Taxable | IGST |
|---|---|---|---|
| 27AAAC…1Z5 | INV-001 | 1,00,000 | 18,000 |
| 27AAAC…1Z5 | inv 002 | 50,000 | 9,000 |
| 29BBBC…4Z1 | 445 | 2,00,000 | 36,000 |
| 24CCCC…7Z9 | A-99 | 80,000 | 14,400 |
| 07DDDD…2Z3 | 771 | 60,000 | 10,800 |

**GSTR-2B**

| GSTIN | InvoiceNo | Taxable | IGST |
|---|---|---|---|
| 27AAAC…1Z5 | INV001 | 1,00,000 | 18,000 |
| 27AAAC…1Z5 | INV002 | 50,000 | 9,000 |
| 29BBBC…4Z1 | 445 | 1,80,000 | 32,400 |
| 07DDDD…2Z3 | 771 | 60,000 | 10,800 |

After `clean_key` normalises invoice numbers, the recon produces:

| Bucket | Invoice | Diff (Taxable) | Action |
|---|---|---|---|
| Matched | INV-001, inv 002, 771 | 0 | Claim ITC fully |
| Value mismatch | 445 | ₹20,000 | Vendor under-reported; claim ₹32,400 only, follow up |
| In books, not in 2B | A-99 (₹80,000) | — | ITC **not eligible** yet (Sec 16(2)(aa)); park in "ITC not available" |

**ITC decision:** Eligible now = 18,000 + 9,000 + 32,400 + 10,800 = **₹70,200**. Held back = ₹14,400 (A-99) + ₹3,600 (445 shortfall) = ₹18,000, tracked in a register until it appears in a later 2B.

Journal for the eligible ITC:

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases | 3,90,000 | |
| Input IGST (eligible) | 70,200 | |
| ITC on hold (not in 2B) | 18,000 | |
| Trade Payables | | 4,78,200 |

That single reconciled file + register + entry is exactly the deliverable an employer means by "close the GST."

## How it's tested

**Interview questions**
- "Your purchase register shows ₹5L ITC but 2B shows ₹4.6L. Walk me through what you do." (Answer: four-bucket recon, hold ineligible under 16(2)(aa), track in a register, chase vendors.)
- "How do you match when invoice numbers are formatted differently?" (Normalise: TRIM, UPPER, strip special chars; match on GSTIN+cleaned no, not amount.)
- "When would you move from Excel to SQL/Python?" (Row count > ~100k, monthly repeatability, audit trail.)

**Practical assessments companies give**
- A **timed Excel test (30–45 min):** two messy sheets, "reconcile and give me the mismatch summary." They watch for XLOOKUP/Power Query, key normalisation, and whether you catch duplicates.
- A **SQL screen:** "write the join that shows only mismatches" — they want FULL OUTER JOIN and a CASE bucket.
- A **case study:** raw GSTR-2B + register files emailed to you, produce a recon and an ITC eligibility note. Grading is on *correct buckets and the eligibility judgement*, not fancy formulas.

## Common mistakes & how pros avoid them

| Mistake | Why it bites | Pro habit |
|---|---|---|
| Matching on invoice number alone | Same number across vendors → false matches | Always GSTIN + normalised invoice key |
| Ignoring trailing spaces / case | `INV 001` ≠ `INV001` → false mismatches | `TRIM`, `UPPER`, `SUBSTITUTE`/regex first |
| Trusting VLOOKUP with duplicates | Returns first hit, hides duplicates | `COUNTIFS` to detect dupes before matching |
| Claiming ITC not in 2B | Sec 16(2)(aa) violation → interest + penalty | Park in "ITC on hold" register |
| Overwriting last month's file | No audit trail | Dated files / Git / Power Query source refresh |
| Blindly trusting AI/OCR output | Silent wrong HSN or rate | Rules layer + human review of exceptions |
| Hard-coding, no re-run | Breaks next month | Parameterise (Power Query, function, script) |

## Learn-it roadmap & resources

**Time to job-ready: 8–10 weeks, part-time.**

| Weeks | Focus | Resource (free unless noted) |
|---|---|---|
| 1–2 | Excel recon: XLOOKUP, SUMIFS, COUNTIFS, pivots | ExcelJet, Chandoo.org |
| 3–4 | Power Query (refreshable recons) | Microsoft Learn: Power Query |
| 5–6 | SQL joins on real files | SQLBolt, Mode SQL Tutorial |
| 7–8 | Python + pandas merges | Kaggle "Pandas" micro-course |
| 9–10 | GST portal/JSON + a GSP trial | GSTN offline utility docs; ClearTax/Zoho free tier |

**Certifications that signal this:** ICAI's *Certificate Course on GST*; Microsoft **PL-300 (Power BI)** for the analytics angle; any GSP vendor's product certification (ClearTax/Cygnet) if you target managed-services roles. None are mandatory — a **portfolio recon file** on GitHub beats a certificate in interviews.

## Quick-reference

| Task | Tool | Command / step |
|---|---|---|
| Match key | Excel | `=UPPER(SUBSTITUTE(TRIM(GSTIN)&"|"&Inv," ",""))` |
| Pull value | Excel | `=XLOOKUP(key, rng_key, rng_val, "NOT FOUND")` |
| Detect duplicate | Excel | `=COUNTIFS(rng, key)>1` |
| Full recon | SQL | `FULL OUTER JOIN ... ON key` + `CASE` bucket |
| Missing rows | SQL | `WHERE b.key IS NULL OR g.key IS NULL` |
| Monthly recon | Python | `df1.merge(df2, on="key", how="outer", indicator=True)` |
| Refreshable recon | Power Query | Data → Get Data → merge queries → Refresh |
| GSTR-1 file | Portal | Offline Tool → Generate JSON → upload → File (EVC/DSC) |
| GSTR-2B | Portal | Returns Dashboard → 2B → Download |
| Tally export | TallyPrime | GST Reports → GSTR-1 → `Alt+E` → JSON |
| API filing | GSP | ERP → GSP (ClearTax/Cygnet) → GSTN |

**Golden rules:** normalise before you match · never claim ITC absent from 2B · the tool proposes, you dispose · every recon must re-run next month unchanged.
