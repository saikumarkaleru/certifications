# Reconciliations That Matter

Reconciliation is the daily discipline of proving that two independent records of the same money agree — and explaining every rupee that doesn't. It is the single most common task juniors are handed on day one, and the fastest way to lose a manager's trust if you get it wrong.

## What it is & where it's used

A reconciliation compares two versions of "truth" and isolates the differences (called *reconciling items*), each of which must have a documented reason and, if it's a real error, a journal entry. The four that actually matter in an Indian finance job:

| Recon | Compares | Owned by | Consequence if wrong |
|---|---|---|---|
| **Bank (BRS)** | Cash-book / ledger vs bank statement | Accounts / Treasury | Cash misstated, fraud undetected |
| **Vendor (AP)** | Your ledger vs vendor's Statement of Account (SOA) | Accounts Payable | Double payment, disputed dues |
| **Customer (AR)** | Your ledger vs customer's SOA | Accounts Receivable | Bad-debt surprises, wrong collections |
| **Inter-company (ICO)** | Entity A's books vs Entity B's books | Group / consolidation | Consolidation doesn't tie, audit qualification |
| **GST 2B recon** | Purchase register vs GSTR-2B | Tax / Indirect Tax | ITC lost, notices under Sec 16 |

Roles that live and die by this: **Accounts Executive, AP/AR Analyst, R2R (Record-to-Report) associate in a GCC/Shared Service, GST/Indirect-tax executive, Treasury analyst, and audit staff** doing substantive testing.

## The gap: why companies want this (and college didn't teach it)

MBA and CA-Inter teach you *what* a BRS is and make you draw the T-format statement. Employers don't care about the T-format — the bank feed and the ERP already exist. What they pay for is the **matching engine in your head and in Excel**: taking 4,000 bank lines and 3,800 book lines, matching them at speed, and confidently saying "these 12 items are genuine timing differences, these 3 are our posting errors, this one is a fraud." College gives you 20 clean transactions; the job gives you messy exports with different date formats, truncated narrations, part-payments, and TDS/bank-charge noise. Nobody teaches the **GSTR-2B reconciliation** at all, yet it directly controls how much Input Tax Credit a company can claim — real cash. That gap (clean-theory vs messy-volume-with-money-at-stake) is exactly what this chapter closes.

## What "proficient" looks like

A job-ready person can, unaided:

- Take two raw exports and reconcile them in Excel using `XLOOKUP`/`SUMIFS`/`Power Query` within an hour, not a day.
- Explain *every* reconciling item as timing, error, or omission — and pass the "so what's the journal?" test.
- Categorise GST 2B mismatches into *match / mismatch / in-books-not-2B / in-2B-not-books* and know the ITC action for each.
- Build a **repeatable** recon (Power Query refresh, not manual re-keying every month).
- Know when a difference is a red flag (fraud, GST notice) versus routine.

## Hands-on: how to actually do it

### Bank reconciliation (BRS)

The modern BRS is a **two-way tick-mark**: match book lines to bank lines; whatever is left on each side is a reconciling item.

Match on a helper key (amount + date window). In Excel, flag whether each book entry appears in the bank statement:

```excel
' Book sheet, col F = is this cleared in the bank?
=IF(COUNTIFS(Bank[Amount], D2, Bank[Date], "<="&TODAY()) > 0, "Cleared", "Uncleared")

' Better: exact two-way match with XLOOKUP on a composite key
' Build key = Amount&"|"&Narration-token in both sheets, then:
=IFERROR(XLOOKUP(G2, Bank[Key], Bank[Date], "NOT IN BANK"), "NOT IN BANK")
```

The reconciliation itself:

```
Balance as per Cash Book (Dr)                       12,45,000
Add: Cheques issued but not yet presented          + 2,30,000
Less: Cheques deposited but not yet cleared        -  1,10,000
Less: Bank charges not in books                    -     1,850
Add: Interest credited by bank not in books        +     3,200
Less: Direct debit (EMI) not in books              -    45,000
= Balance as per Bank Statement                     13,21,350
```

Every item that is *our* omission (bank charges, interest, direct debits) needs a journal:

| Item | Dr | Cr | Amount |
|---|---|---|---|
| Bank charges | Bank Charges A/c | Bank A/c | 1,850 |
| Interest credited | Bank A/c | Interest Income A/c | 3,200 |
| EMI auto-debit | Loan A/c | Bank A/c | 45,000 |

Cheques not presented / not cleared need **no** entry — they are pure timing.

### Vendor / Customer reconciliation

You get the vendor's **SOA (PDF/Excel)** and match it to your ledger. Load both into **Power Query** and do an anti-join to find one-sided items:

1. Data → Get Data → From File (vendor SOA) and From File (your ledger export from Tally/SAP).
2. On invoice number, `Merge Queries` → **Left Anti** → gives invoices in *your* books not in vendor's.
3. Repeat **Right Anti** for vendor's-not-yours.
4. Net balance check: `= SUM(YourDebits) - SUM(YourCredits)` vs vendor's closing.

Typical causes of a vendor difference and the fix:

| Difference | Reason | Action |
|---|---|---|
| Vendor shows invoice you don't | GRN/invoice not booked | Book the purchase (or dispute) |
| You show payment vendor doesn't | Cheque in transit / wrong UTR | Share UTR, no entry |
| TDS deducted | Vendor booked gross | Reconcile with TDS deducted; educate vendor |
| Debit/credit note timing | Return not yet in vendor books | Confirm CN reference |

### Inter-company reconciliation

Entity A's "due from B" must equal Entity B's "due to A", sign-flipped. Use a shared **ICO matrix**. In SQL against a group ledger:

```sql
SELECT a.doc_id, a.entity AS from_entity, b.entity AS to_entity,
       a.amount AS a_side, b.amount AS b_side,
       a.amount + b.amount AS difference
FROM ico_ledger a
JOIN ico_ledger b
  ON a.doc_id = b.doc_id
 AND a.counterparty = b.entity
WHERE ABS(a.amount + b.amount) > 1        -- non-zero net = mismatch
ORDER BY ABS(a.amount + b.amount) DESC;
```

Differences are usually **FX rate** (each entity used a different rate), **cut-off** (goods in transit at period-end), or a **missed booking**. The elimination entry at consolidation only works if the mismatch is zero, so this must clear before close.

### GST 2B reconciliation

GSTR-2B is the auto-drafted ITC statement. You may claim ITC **only** for invoices appearing in 2B (Sec 16(2)(aa)). Match your **purchase register** to 2B on **GSTIN + Invoice No + Taxable Value + Tax**.

Python is ideal because 2B is a downloadable JSON/Excel and volumes are large:

```python
import pandas as pd

books = pd.read_excel("purchase_register.xlsx")
gst2b = pd.read_excel("GSTR2B.xlsx")

# Normalise keys — invoice numbers are the usual pain point
for df in (books, gst2b):
    df["key"] = (df["GSTIN"].str.strip()
                 + "|" + df["InvNo"].str.upper().str.replace(r"\W", "", regex=True)
                 + "|" + df["TaxableValue"].round(0).astype(int).astype(str))

merged = books.merge(gst2b, on="key", how="outer",
                     suffixes=("_bk", "_2b"), indicator=True)

status = {"both": "Matched",
          "left_only": "In books, NOT in 2B (hold ITC)",
          "right_only": "In 2B, NOT in books (book it)"}
merged["Recon"] = merged["_merge"].map(status)

# Tax-value mismatch even when both present
m = merged["_merge"] == "both"
merged.loc[m & (merged["Tax_bk"].round() != merged["Tax_2b"].round()),
           "Recon"] = "Value mismatch — probe"

merged.to_excel("2B_recon.xlsx", index=False)
```

Action per bucket: **Matched** → claim; **In-books-not-in-2B** → do *not* claim yet, follow up with vendor to file GSTR-1; **In-2B-not-in-books** → book the purchase; **Value mismatch** → check rate/rounding, raise with vendor.

## Worked example / mini-project

**Scenario:** Month-end GST 2B recon for Acme Traders Pvt Ltd, March 2026.

Purchase register (books):

| Vendor GSTIN | Inv No | Taxable | GST | 
|---|---|---|---|
| 29ABCDE1234F1Z5 | INV-101 | 1,00,000 | 18,000 |
| 27PQRSX5678L1Z2 | 5023 | 50,000 | 9,000 |
| 06LMNOP9012K1Z8 | A/778 | 2,00,000 | 36,000 |

GSTR-2B (portal):

| Supplier GSTIN | Inv No | Taxable | GST |
|---|---|---|---|
| 29ABCDE1234F1Z5 | INV101 | 1,00,000 | 18,000 |
| 27PQRSX5678L1Z2 | 5023 | 50,000 | 4,500 |
| 33ZZZZZ0000Z1Z0 | 90 | 80,000 | 14,400 |

Run the Python above (invoice normaliser strips the "-" so INV-101 = INV101). Result:

| Recon status | Invoice | ITC action |
|---|---|---|
| Matched | INV-101 | Claim 18,000 |
| Value mismatch | 5023 | Books 9,000 vs 2B 4,500 — vendor filed at 9% wrongly; hold 4,500, chase |
| In books, not in 2B | A/778 | Vendor hasn't filed GSTR-1; **do not claim 36,000** this month |
| In 2B, not in books | 90 | 14,400 in 2B but no purchase booked — investigate; possibly wrong GSTIN mapped to us |

Eligible ITC to claim in GSTR-3B = ₹18,000 + ₹4,500 = **₹22,500**, versus ₹63,000 the books naively suggest. That ₹40,500 gap is exactly why this recon exists — claiming the full amount invites a Sec 16 notice with interest.

## How it's tested

**Interview questions:**
- "A cheque you issued hasn't cleared — does it need a journal entry?" (No, timing.)
- "Bank statement shows a credit you can't identify. What do you do?" (Park in suspense, investigate, never assume income.)
- "Why can't you claim ITC that isn't in 2B?" (Sec 16(2)(aa).)
- "Inter-company balance doesn't tie by ₹1,200 — likely cause?" (FX rate or cut-off timing.)

**Practical tests companies give:**
- A **timed Excel test**: two sheets, "reconcile and list differences in 30 minutes" — they watch whether you reach for `XLOOKUP`/`COUNTIFS`/Power Query or start eyeballing.
- A **GST case**: raw purchase register + 2B Excel, "how much ITC can we claim?" — the trap is the value-mismatch and not-in-2B rows.
- A **close simulation** in a GCC: "here's a trial balance with an unreconciled bank line, clear it" — they score whether your journals are correct and balanced.

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | Pro habit |
|---|---|---|
| Matching on amount alone | Two ₹50,000 payments collide | Match on composite key (party + inv + amount) |
| Passing entries for timing items | Overstates/understates cash | Only *errors and omissions* get journals |
| Dumping unknowns into a "misc" bucket | Hides fraud | Everything gets a named reason or goes to suspense with a ticket |
| Claiming full ITC ignoring 2B | Interest + penalty under GST | Claim only matched value |
| Re-keying the recon every month | Slow, error-prone | Build once in Power Query, refresh monthly |
| Ignoring rounding | 100s of false mismatches | Round to nearest rupee before comparing |
| Not aging the differences | Old items rot | Track "days open" on every reconciling item |

## Learn-it roadmap & resources

**Time to proficiency: 4–6 weeks** of deliberate practice alongside a job or dummy data.

- **Week 1–2:** Master BRS logic + Excel matching (`XLOOKUP`, `SUMIFS`, `COUNTIFS`). Free: ExcelIsFun / Chandoo lookup playlists.
- **Week 3:** Power Query merge/anti-join for AP/AR recon. Free: Microsoft Power Query docs; "Get & Transform" tutorials.
- **Week 4:** GST 2B recon — read Sec 16 & Rule 36; practice on the **GST portal** (Returns → GSTR-2B → download Excel). Free: GSTN help + ICAI GST background material.
- **Week 5–6:** Automate one recon end-to-end in Python (pandas) or an ERP (TallyPrime bank reconciliation: *Gateway → Banking → Bank Reconciliation*).

Certifications that signal this skill: **ICAI GST certificate course**, **Microsoft PL-300 (Power BI/Query)**, or any R2R/AP-AR training from a GCC. None are mandatory — a clean reconciled workbook you built beats a certificate in interviews.

## Quick-reference

| Need | Formula / step |
|---|---|
| Is book line in bank? | `=COUNTIFS(Bank[Amt],D2,Bank[Date],"<="&TODAY())>0` |
| Two-way match key | `=A2&"|"&TEXT(ROUND(B2,0),"0")` both sheets, then `XLOOKUP` |
| One-sided items | Power Query → Merge → **Left/Right Anti** |
| ICO net difference | `a.amount + b.amount` (should = 0) |
| 2B match key | `GSTIN | InvNo(normalised) | TaxableValue` |
| Bank charge JE | Dr Bank Charges / Cr Bank |
| Bank interest JE | Dr Bank / Cr Interest Income |
| Auto-debit EMI JE | Dr Loan / Cr Bank |

**Reconciling-item rule of thumb:** *Timing → no entry. Error/omission → journal. Unknown → suspense + investigate, never income.*

**GST 2B buckets:** Matched → claim · In-books-not-2B → hold, chase vendor · In-2B-not-books → book it · Value mismatch → probe rate/rounding.

**Legal anchors:** BRS is management practice (no statute) · GST ITC gated by **Sec 16(2)(aa)** and **Rule 36** · TDS reconciliation ties to **Form 26AS / AIS**.
