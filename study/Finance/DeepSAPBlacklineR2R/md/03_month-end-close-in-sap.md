# The Month-End Close in SAP

## What you'll be able to do

You'll be able to run — and explain — a full FI month-end close in SAP: post and auto-reverse accruals, set up recurring entries, clear GR/IR, run foreign-currency revaluation, execute the depreciation run, push cost-centre costs through allocations/assessments, open and close posting periods safely, and produce the financial statements from a Financial Statement Version. Most importantly you'll be able to hand an interviewer a **working-day-by-working-day (WD1–WD5) close calendar mapped to exact T-codes**, which is what a GCC R2R team actually lives by.

## The drill — step by step

We close **period 04/2026 (April)** for company code 1000.

**1. Cut-off & open the new period — `OB52` (Posting Period Variant).**
`OB52` maintains per account-type (S=GL, D=customer, K=vendor, A=asset, M=material) the *from/to* period allowed. Standard practice: keep period 04 open only for the close team (authorisation group), open 05 for operations. At the very end you *close 04* by moving the lower period to 05.

**2. Accruals — `FBS1` (Enter Accrual/Deferral Document).**
For expenses incurred but not invoiced (e.g. April electricity ₹40,000). `FBS1`: posting date `30.04.2026`, **Reversal reason `05`** and **reversal date `01.05.2026`**.
- Dr 403000 Power & Fuel 40,000 (cost centre) / Cr 240100 Accrued Expenses 40,000.
On WD1 of May you run **`F.81` (Reverse Accrual/Deferral Documents)** which auto-reverses every FBS1 doc dated for reversal — so the accrual self-cancels when the real invoice arrives. (The S/4 "Accrual Engine" ACEDT is the newer, schedule-based alternative.)

**3. Recurring entries — `FBD1` (define) → `F.14` (post).**
For fixed monthly postings (rent ₹1,00,000). `FBD1`: first run 30.04.2026, last run 31.03.2027, interval 1 month, the template entry Dr Rent / Cr Rent Payable. Nothing posts yet — it's a template. Each month **`F.14`** (with batch input session run via `SM35`) generates the actual document. Manage/delete via `F.15`.

**4. GR/IR clearing — `MR11` and `F.13`.**
GR/IR (goods-received/invoice-received, acct 191100) holds the timing gap between MIGO and MIRO. **`F.13` (Automatic Clearing)** nets off GR and IR lines that match (same PO, qty, value) → they clear to zero. Genuine mismatches (goods received, invoice never came, or vice-versa) are cleared/written off with **`MR11` (GR/IR Account Maintenance)**. Target: GR/IR aged report shows only in-transit, explainable items.

**5. Foreign-currency revaluation — `FAGL_FCV` (New GL) / older `F.05`.**
Open items and balances in USD/EUR must be restated at month-end closing rate. Load rates in **`OB08`** first. `FAGL_FCV`: company code 1000, valuation key date 30.04.2026, valuation area, run in **test** then **update**.
- Unrealised gain: Dr FC Open Item (adjustment acct) / Cr 415000 FX Gain (unrealised).
- Loss: Dr 415100 FX Loss / Cr adjustment. By default the New-GL run posts a reversal on 01.05 (valuation is provisional until the item is actually settled).

**6. Asset depreciation run — `AFAB` (Post Depreciation).**
Company code 1000, period 04/2026. First run of the month = "Planned posting run"; corrections = "Repeat/Unplanned". Test first. Posts:
- Dr 410000 Depreciation Expense (cost centre) / Cr 020100 Accumulated Depreciation.
Check via asset explorer **`AW01N`**. (S/4 uses `AFAB` still, or the Fiori "Post Depreciation" app; New Asset Accounting posts to all ledgers in real time.)

**7. CO allocations — assessment `KSU5`, distribution `KSV5`.**
Shared-service cost centres (IT-DEL-100) must be pushed to receiving business cost/profit centres.
- **Distribution (`KSV5`)** keeps the *original* primary cost element (e.g. still shows as Salaries on the receiver).
- **Assessment (`KSU5`)** uses a *secondary* assessment cost element (e.g. 9AS100) and hides the primary detail — cleaner for management reporting.
Define the cycle, run in test, then post. IT cost centre balance → 0 after allocation; business centres absorb the cost.

**8. Reconciliations.** Sub-ledger to GL: **AP** (FBL1N/S_ALR reports) = GL Trade Payables 160000; **AR** = 140000; **Assets** (`ABST2` / `AJAB` year-end) = GL. Bank GL 100000 vs bank statement (feeds Blackline — next chapter). Intercompany balances confirmed.

**9. Close the period — `OB52`** move GL/sub-ledger periods to 05 so April is locked. CO period lock via **`OKP1`**.

**10. Financial statements — `F.01` / `S_ALR_87012284` using a Financial Statement Version (FSV).**
The **FSV** (config `OB58`, e.g. `INT`/`CAIN`) is the hierarchy that maps every GL account into Balance Sheet and P&L line items. Run **`F.01`** (or S/4 `FAGLB03` for GL balances, and the Fiori "Balance Sheet/P&L" app) for company code 1000, period 04, ledger 0L → the statutory-format B/S and P&L.

## The output — WD-by-WD close calendar

| WD | Activity | T-code |
|---|---|---|
| WD-1 | Reverse prior-month accruals | F.81 |
| WD1 | Open/restrict periods; post recurring | OB52, F.14 |
| WD1 | Sub-ledger cut-off; last AP/AR postings | FB60/FB70 |
| WD2 | Accruals & provisions | FBS1 |
| WD2 | GR/IR review & clearing | F.13 / MR11 |
| WD3 | FX revaluation | FAGL_FCV (OB08 rates) |
| WD3 | Depreciation run | AFAB / AW01N |
| WD4 | CO assessments/distributions | KSU5 / KSV5 |
| WD4 | Sub-ledger↔GL recons; intercompany | FBL1N/3N/5N |
| WD5 | Close period; lock CO | OB52 / OKP1 |
| WD5 | Trial balance, FSV, B/S & P&L | F.01 / FAGLB03 |

Result artefact — an April trial balance that ties, sub-ledgers agreeing to their recon GLs, GR/IR aged and clean, FX restated at closing rate, depreciation booked, shared costs allocated, and a signed-off B/S + P&L in FSV format.

## Checks & gotchas

- **Accruals with no reversal date** double-count when the real invoice posts — always set the FBS1 reversal reason/date and run F.81 next month.
- Running **AFAB** in the wrong mode (planned vs repeat) either skips assets or posts nothing — always test-run and check the log first.
- **FX rates not loaded in OB08** → FAGL_FCV values everything at 1:1 or errors. Load closing rates before running.
- Closing the period in OB52 **before** all late postings are in blocks the team — coordinate the exact lock time; leave a close-team authorisation group open.
- **Assessment vs distribution** chosen wrong distorts management reports — distribution preserves the primary cost element, assessment masks it under a secondary one.
- Sub-ledger ≠ GL means a **broken reconciliation account** or a direct GL posting to a recon account — investigate before signing the TB.

## Interview drill

**Q1. Walk me through your SAP month-end close.**
"Reverse prior accruals (F.81), open/restrict periods (OB52), post recurring (F.14) and accruals (FBS1), clear GR/IR (F.13/MR11), revalue FX (FAGL_FCV), run depreciation (AFAB), do CO assessments (KSU5), reconcile every sub-ledger to its recon GL, close periods (OB52/OKP1), then produce the trial balance and the B/S/P&L via the Financial Statement Version (F.01/FAGLB03). I map it to a WD1–WD5 calendar with owners and dependencies."

**Q2. Distribution vs assessment in CO?**
"Both move cost from sender to receiver cost objects. Distribution (KSV5) posts using the original primary cost element, so the receiver still sees 'salaries'. Assessment (KSU5) uses a secondary assessment cost element and summarises — better for management view but you lose the primary breakdown."

**Q3. How does GR/IR clearing work and why does it matter?**
"GR/IR is the interim clearing account between goods receipt and invoice receipt. F.13 auto-clears matched GR/IR pairs; MR11 handles genuine quantity/value mismatches. A dirty GR/IR overstates payables or accruals and is an audit red flag, so it's reviewed and aged every close."

## Practise free

- **Excel close pack:** build a 6-tab close — accruals (with an auto-reverse column dated next month), recurring template, GR/IR aging, FX reval (balance × closing rate − book value = gain/loss), a depreciation schedule (WDV/SLM), and a cost-allocation matrix. Running these teaches the *logic* each T-code automates.
- Replicate an **FSV** as an Excel mapping table: GL account → B/S or P&L line → subtotal — then `SUMIF` a trial balance into statements. That's exactly what OB58/F.01 do.
- **openSAP** "Financial Close with SAP S/4HANA" and SAP's Financial Closing cockpit (`CLOCO`) docs walk the sequence; the videos are free.
- On an **SAP CAL trial**, run FBS1→F.81, AFAB in test, and F.01 once — even a single dry run makes the calendar real in interviews.
