# The accounting cycle in a real company

## What it is & where it's used

The accounting cycle is the assembly line that turns a shoebox of receipts into a signed balance sheet. In a real company it runs every single day and closes hard every month. The flow never changes:

**Source document → Voucher → Journal/Ledger → Trial Balance → Adjustments → Financial Statements → Close.**

Every finance role lives somewhere on this line. An **Accounts Payable executive** creates purchase vouchers from vendor invoices. An **AR/billing analyst** raises sales invoices (the source doc for the *customer*). A **staff accountant** posts journals and reconciles ledgers. A **GL/R2R (Record-to-Report) analyst** owns the trial balance and month-end close. A **financial reporting** person builds the P&L and Balance Sheet. In India this happens in **TallyPrime, Zoho Books, or SAP/Oracle**; the artefacts (invoice, voucher, ledger, TB) are identical across all of them. If you can trace one rupee from a supplier invoice all the way to "Trade Payables" on the balance sheet, you understand the job.

## The gap: why companies want this (and college didn't teach it)

College teaches you to *pass* journal entries from a textbook that already tells you "Purchased goods for ₹50,000." It never shows you the actual **tax invoice** that the ₹50,000 came from, why it has a GSTIN, an HSN code, a place-of-supply, and CGST+SGST split — and how one wrong GSTIN kills your Input Tax Credit. It teaches debit-credit rules but not *voucher types*, *bill-wise tracking*, *reconciliation*, or what "the books don't tie" means at 9pm on the 5th of the month.

The industry gap is this: **college gives you the entry, the job gives you the evidence and makes you tie it out.** Employers pay for the person who can take a messy pile of real artefacts and produce a clean, reconciled trial balance that a CA can sign. That's a *process* skill, not a theory skill — and it's exactly what an MBA/CA-Inter syllabus underweights.

## What "proficient" looks like

A job-ready person can, unaided:

- Read a **GST tax invoice** and identify GSTIN, HSN/SAC, taxable value, CGST/SGST/IGST, and place of supply — and know whether ITC is available.
- Pick the **correct voucher type** in Tally (Purchase, Sales, Payment, Receipt, Contra, Journal) — this is the #1 thing juniors get wrong.
- Post entries with **bill-wise details** so payables/receivables can be aged.
- Extract a **trial balance**, spot that it doesn't tie, and find the difference (transposition, one-sided posting, wrong side).
- Pass **month-end adjustments**: depreciation, prepaid, accruals, provisions, closing stock.
- Roll the adjusted TB into a **P&L and Balance Sheet** and prove the BS balances.
- Reconcile **bank, GSTR-2B vs purchase register, and vendor ledgers**.

## Hands-on: how to actually do it

**Step 1 — Source document to journal.** A vendor invoice: goods ₹1,00,000 + 18% GST (intra-state) = ₹18,000 (₹9,000 CGST + ₹9,000 SGST), total ₹1,18,000.

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases | 1,00,000 | |
| Input CGST | 9,000 | |
| Input SGST | 9,000 | |
| To Trade Payables — ABC Traders | | 1,18,000 |

**Step 2 — In TallyPrime (the actual click-path):**
```
Gateway of Tally → Vouchers → F9 (Purchase)
  Party A/c name: ABC Traders  → (bill-wise: New Ref, Inv-042)
  Purchase ledger: Purchases @18% (set GST details, HSN)
  GST auto-computes CGST + SGST
  Ctrl+A to accept
```
Rule of thumb for voucher type: **money out of bank = Payment (F5); money in = Receipt (F6); bank↔cash or bank↔bank = Contra (F4); credit purchase = F9; credit sale = F8; anything with no cash/bank movement (depreciation, provisions) = Journal (F7).**

**Step 3 — Trial balance in Excel.** Say you exported ledger closing balances. Prove it ties:
```
=SUMIF(C:C,"Dr",D:D) - SUMIF(C:C,"Cr",D:D)   → must equal 0
```
Find a suspicious difference that's divisible by 9 (a transposition error, e.g. 5,400 keyed as 4,500):
```
=IF(MOD(ABS(TotalDr-TotalCr),9)=0,"Likely transposition","Check one-sided posting")
```

**Step 4 — Pull the vendor sub-ledger with SQL** (any ERP with a DB behind it):
```sql
SELECT v.party_name,
       SUM(CASE WHEN j.dc = 'D' THEN j.amount ELSE 0 END) AS debit,
       SUM(CASE WHEN j.dc = 'C' THEN j.amount ELSE 0 END) AS credit,
       SUM(CASE WHEN j.dc = 'C' THEN j.amount ELSE -j.amount END) AS balance
FROM journal_lines j
JOIN parties v ON v.id = j.party_id
WHERE j.ledger = 'Trade Payables'
  AND j.txn_date <= '2026-03-31'
GROUP BY v.party_name
HAVING balance <> 0
ORDER BY balance DESC;
```

**Step 5 — Reconcile GSTR-2B vs purchase register in Python** (the ITC check every AP team runs):
```python
import pandas as pd
pr   = pd.read_excel("purchase_register.xlsx")   # your books
b2b  = pd.read_excel("gstr2b.xlsx")              # from GST portal

merged = pr.merge(b2b, on=["gstin", "invoice_no"],
                  how="outer", indicator=True, suffixes=("_books", "_2b"))

print(merged.loc[merged["_merge"]=="left_only"])   # in books, NOT in 2B → ITC at risk
print(merged.loc[merged["_merge"]=="right_only"])  # in 2B, NOT in books → missed entry

merged["tax_diff"] = merged["tax_books"].fillna(0) - merged["tax_2b"].fillna(0)
print(merged.loc[merged["tax_diff"].abs() > 1])    # value mismatches
```

## Worked example / mini-project

**Reproduce a one-month close for "Nashik Auto Parts Pvt Ltd."** Opening: Capital ₹5,00,000, Bank ₹5,00,000. March transactions:

| Date | Event | Voucher | Entry |
|---|---|---|---|
| 02 | Buy stock ₹1,00,000 +18% GST on credit (ABC) | Purchase F9 | Dr Purchases 1,00,000 / Dr Input CGST 9,000 / Dr Input SGST 9,000 / Cr ABC 1,18,000 |
| 10 | Sell goods ₹1,50,000 +18% GST on credit (XYZ) | Sales F8 | Dr XYZ 1,77,000 / Cr Sales 1,50,000 / Cr Output CGST 13,500 / Cr Output SGST 13,500 |
| 15 | Pay rent ₹20,000 by bank | Payment F5 | Dr Rent 20,000 / Cr Bank 20,000 |
| 20 | Receive ₹1,77,000 from XYZ | Receipt F6 | Dr Bank 1,77,000 / Cr XYZ 1,77,000 |
| 28 | Pay ABC ₹1,18,000 | Payment F5 | Dr ABC 1,18,000 / Cr Bank 1,18,000 |

**Month-end adjustments (Journal F7):**
- Depreciation on ₹1,20,000 machinery @15% p.a. for 1 month = **₹1,500** → Dr Depreciation / Cr Machinery.
- Closing stock ₹40,000 → shown in P&L (credit) and BS (asset).
- GST payable = Output ₹27,000 − Input ₹18,000 = **₹9,000** net liability.

**Trial Balance (extract), then the statements:**

*P&L:* Sales 1,50,000 + Closing stock 40,000 − Purchases 1,00,000 − Rent 20,000 − Depreciation 1,500 = **Net profit ₹68,500.**

*Balance Sheet:*

| Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Capital 5,00,000 + Profit 68,500 | 5,68,500 | Bank (5,00,000−20,000+1,77,000−1,18,000) | 5,39,000 |
| GST payable | 9,000 | Closing stock | 40,000 |
| | | Machinery (1,20,000−1,500) | 1,18,500 |
| Wait — Machinery wasn't bought this month; treat opening PPE ₹1,20,000 funded from capital | | | |
| **Total** | **5,77,500** | **Total** | **5,77,500** |

The point of the exercise: pass every entry in Tally, export the TB, and confirm **Assets = Liabilities + Equity to the rupee.** If it's off, walk back through the ledgers.

## How it's tested

**Interview questions:**
- "Walk me from a supplier invoice to the balance sheet." (Trace the artefact chain.)
- "Which voucher type for paying salary? For depreciation?" (Payment; Journal.)
- "Your trial balance is off by ₹900 — what do you check first?" (Divisible by 9 → transposition.)
- "What's GSTR-2B and why reconcile it?" (ITC eligibility.)
- "Golden rules of accounting?" (Debit the receiver / what comes in / expenses & losses.)

**Practical assessments companies actually give:**
1. A **timed Tally test**: "Here are 15 vouchers, post them and give me the P&L in 30 minutes."
2. An **Excel case**: raw ledger dump → build the TB, find the ₹X difference, produce statements.
3. A **reconciliation screen**: two files (books vs bank / books vs 2B), find the mismatches — often live in Excel with `VLOOKUP/XLOOKUP`.

```
=XLOOKUP(A2, GST2B!B:B, GST2B!E:E, "MISSING IN 2B")
```

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Using Journal (F7) for a bank payment | Any cash/bank movement gets Payment/Receipt/Contra, never Journal |
| Booking gross invoice to Purchases (GST included) | Split tax to Input CGST/SGST; only net goes to Purchases |
| Not enabling bill-wise details | Turn on bill-wise → payables/receivables become ageable |
| Claiming ITC not in GSTR-2B | Reconcile 2B monthly *before* filing GSTR-3B |
| Forcing the TB to tie with a "Suspense" plug and forgetting it | Investigate the difference; suspense is temporary, not a fix |
| Ignoring the sign of closing stock | Appears twice: P&L credit AND balance-sheet asset |
| Posting to the wrong period | Lock periods after close; date-stamp every voucher |

Pros reconcile *as they go*, keep a **close checklist**, and never trust a TB that ties without also checking that individual sub-ledgers (AP/AR/bank) match their supporting schedules.

## Learn-it roadmap & resources

**Time to proficiency: 6–10 weeks** of daily practice from a working debit-credit base.

- **Weeks 1–2:** Golden rules, voucher types, pass 50 entries by hand.
- **Weeks 3–5:** TallyPrime end-to-end — company creation, GST setup, all voucher types, export TB and statements. (Free: *Tally Education* self-learning; YouTube *FinTaxPro*, *CA Rahul Malodia*.)
- **Weeks 6–8:** Excel reconciliations (XLOOKUP, SUMIF, pivot the ledger), one full month-end close.
- **Weeks 9–10:** GST portal — file a practice GSTR-3B, reconcile 2B; touch SAP FICO concepts.

**Certifications that carry weight:** Tally's **TallyPrime with GST** certificate; **SAP FICO** (for MNC GL roles); your **CA-Inter** itself is the strongest signal. Free portal practice: log into `gst.gov.in` with a sandbox/test GSTIN.

## Quick-reference

| Item | Detail |
|---|---|
| Cycle | Source doc → Voucher → Ledger → TB → Adjustments → Financials → Close |
| Golden rules | Personal: Dr receiver, Cr giver · Real: Dr in, Cr out · Nominal: Dr expenses/losses, Cr income/gains |
| Tally voucher keys | F4 Contra · F5 Payment · F6 Receipt · F7 Journal · F8 Sales · F9 Purchase |
| TB tie test | Σ Debits = Σ Credits; diff ÷ 9 → transposition; diff even → one-sided |
| GST intra-state | CGST + SGST (9%+9%); inter-state → IGST 18% |
| ITC check | Purchase register must match GSTR-2B before GSTR-3B |
| Accounting equation | Assets = Liabilities + Equity (must tie to the rupee) |
| Excel workhorses | `=XLOOKUP()` `=SUMIF()` `=MOD(diff,9)` pivot tables |
| Key adjustments | Depreciation, prepaid, accruals, provisions, closing stock |
| Depreciation (SLM/month) | Cost × rate ÷ 12 → Dr Depreciation / Cr Asset |
