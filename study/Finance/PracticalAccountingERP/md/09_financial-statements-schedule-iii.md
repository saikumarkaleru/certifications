# Financial Statement Preparation & Schedule III

## What it is & where it's used

Financial statement preparation is the act of converting a raw **trial balance (TB)** — a flat list of ledger balances — into the two statutory face documents every Indian company must file: the **Balance Sheet** and the **Statement of Profit and Loss**, plus the **Notes to Accounts** that explain every line. The mandated format is **Schedule III of the Companies Act, 2013** (Division I for entities on AS, Division II for Ind AS, Division III for NBFCs).

This is the single most common deliverable in an accounts department. It is used by:

- **Accounts/finance executives** doing the monthly and annual "close".
- **Audit article assistants / audit associates** who redraw a client's TB into Schedule III during statutory audit.
- **Consulting/ROC compliance teams** preparing statements for AOC-4 filing.
- **FP&A and controllership** who start every management pack from a Schedule III shell.

If you can take a messy TB and hand back a compliant Balance Sheet, P&L, and notes without supervision, you are doing the core job an accountant is paid for.

## The gap: why companies want this (and college didn't teach it)

An MBA (and even much of CA theory) teaches you the *T-format* balance sheet — the horizontal "Liabilities on left, Assets on right" layout from the 1956 Act. **That format is illegal for companies today.** Schedule III mandates the **vertical format** with a fixed line-item sequence, mandatory sub-note groupings, and prior-year comparatives.

The specific gaps employers see in freshers:

| What college teaches | What the job needs |
|---|---|
| T-format, no notes | Vertical Schedule III + 20-odd notes |
| "Sundry debtors" | "Trade Receivables", split by ageing & security |
| Lump everything as "Reserves" | Reserves & Surplus note with movement |
| Ignore current/non-current split | Every asset/liability classified by 12-month rule |
| One year only | Two-year comparatives, regrouped |

College stops at the TB. The employer's work *starts* at the TB. Schedule III is procedural knowledge — grouping rules and a rigid template — that is simply never drilled academically.

## What "proficient" looks like

A job-ready person can, **unaided**, do all of this:

1. Take a 150-line TB in Excel and map each ledger to its Schedule III line and note number.
2. Apply the **current vs non-current** test correctly (the 12-month / operating-cycle rule).
3. Build **Notes 1–2** (Share Capital, Reserves & Surplus with movement) and Notes for PPE, Trade Receivables (with the mandatory **ageing schedule**), Trade Payables ageing, Borrowings, and each expense head.
4. Ensure the Balance Sheet **ties** (Total Equity & Liabilities = Total Assets) and that P&L profit flows into Reserves.
5. Handle appropriations: **provision for tax, proposed dividend, transfer to reserves**.
6. Deliver with **prior-year comparatives** and note cross-references, ready for audit.
7. Know the FY2021 amendment additions: **ageing schedules, ratios disclosure, promoter shareholding, CSR, Ind AS vs AS differences**.

## Hands-on: how to actually do it

### Step 0 — the extended trial balance in Excel

Lay the TB out with a mapping column. This is the workhorse.

| Col | Header | Content |
|---|---|---|
| A | Ledger | e.g. "Bank – HDFC CC" |
| B | Debit | 4,50,000 |
| C | Credit | |
| D | SIII_Head | "Cash & Cash Equivalents" |
| E | Note_No | 12 |
| F | Nature | Asset / Liab / Inc / Exp |

**Check the TB balances first:**
```
=SUM(B:B)-SUM(C:C)        → must be 0
```

**Pull a note total from the mapping (the key formula):**
```
=SUMIFS($B:$B,$E:$E,12) - SUMIFS($C:$C,$E:$E,12)
```
Sum debits minus credits for every ledger tagged to Note 12. Do this for each note number and the statement builds itself.

**Map ledgers to heads with a lookup table** (build a master `tbl_Map` of ledger→head):
```
=XLOOKUP(A2, tbl_Map[Ledger], tbl_Map[SIII_Head], "**UNMAPPED**")
```
Filter for `**UNMAPPED**` to catch anything you forgot — an unmapped ledger is the #1 cause of a balance sheet that doesn't tie.

### Step 1 — the current / non-current test

A liability is **current** if it is due within 12 months or the operating cycle; else non-current. Same logic for assets.

```
=IF(Due_Date - Reporting_Date <= 365, "Current", "Non-current")
```
Classic split: current maturities of long-term debt → **Other Current Liabilities**; the rest → **Long-term Borrowings**.

### Step 2 — the mandatory ageing schedules (post-2021 amendment)

Trade Receivables must be bucketed. In Excel:
```
=SUMIFS(Amt, Days, ">=0", Days, "<181")            'Less than 6 months
=SUMIFS(Amt, Days, ">180", Days, "<366")           '6 months – 1 year
=SUMIFS(Amt, Days, ">365", Days, "<731")           '1–2 years
```
where `Days = TODAY() - Invoice_Date`. The buckets required: **< 6m, 6m–1y, 1–2y, 2–3y, > 3y**, split into *Undisputed – considered good / doubtful* and *Disputed*.

### Step 3 — the closing journal entries

Before statements, pass the closing/appropriation entries:

| # | Particulars | Dr | Cr |
|---|---|---|---|
| 1 | Depreciation Expense A/c … Dr | 8,00,000 | |
|   | &nbsp;&nbsp;&nbsp;To Accumulated Depreciation A/c | | 8,00,000 |
| 2 | Profit & Loss A/c … Dr | 12,00,000 | |
|   | &nbsp;&nbsp;&nbsp;To Provision for Tax A/c | | 12,00,000 |
| 3 | Surplus in P&L (Retained Earnings) … Dr | 5,00,000 | |
|   | &nbsp;&nbsp;&nbsp;To General Reserve A/c | | 5,00,000 |
| 4 | All Revenue A/cs … Dr / All Expense A/cs … Cr | x | x |
|   | &nbsp;&nbsp;&nbsp;To/By Profit & Loss A/c (closing) | | |

### Step 4 — TallyPrime shortcut

Tally already outputs Schedule III if ledgers are grouped correctly:
`Gateway of Tally → Balance Sheet → F12 (Configure) → "Method of showing Balance Sheet: Vertical" → Yes`. Then `Alt+F5` for detailed, `Ctrl+B` to change the schedule basis. But you still verify the grouping — Tally trusts your ledger's parent group.

## Worked example / mini-project

**Sunrise Traders Pvt Ltd** — FY2024-25 trial balance (₹):

| Ledger | Dr | Cr |
|---|---|---|
| Equity Share Capital (1,00,000 × ₹10) | | 10,00,000 |
| General Reserve (opening) | | 4,00,000 |
| Surplus in P&L (opening) | | 1,50,000 |
| Term Loan – SBI (repay 2028) | | 6,00,000 |
| Trade Payables | | 3,20,000 |
| Plant & Machinery (gross) | 18,00,000 | |
| Accumulated Depreciation | | 5,00,000 |
| Inventory | 4,10,000 | |
| Trade Receivables | 5,60,000 | |
| Cash & Bank | 2,40,000 | |
| Revenue from Operations | | 40,00,000 |
| Purchases | 22,00,000 | |
| Employee Benefits Expense | 6,50,000 | |
| Depreciation | 1,80,000 | |
| Other Expenses | 3,30,000 | |
| **Totals** | **63,70,000** | **69,70,000** |

Difference ₹6,00,000 = profit not yet closed. **Statement of P&L:**

| Particulars | Note | 2024-25 (₹) |
|---|---|---|
| Revenue from Operations | 16 | 40,00,000 |
| Total Income | | **40,00,000** |
| Purchases of Stock-in-Trade | 18 | 22,00,000 |
| Employee Benefits Expense | 19 | 6,50,000 |
| Depreciation & Amortisation | | 1,80,000 |
| Other Expenses | 20 | 3,30,000 |
| Total Expenses | | **33,60,000** |
| **Profit before Tax** | | **6,40,000** |
| Less: Tax @ 25% | | 1,60,000 |
| **Profit for the year** | | **4,80,000** |

Appropriate: transfer ₹1,00,000 to General Reserve. Closing Surplus = 1,50,000 + 4,80,000 − 1,00,000 = **₹5,30,000**. General Reserve = 4,00,000 + 1,00,000 = **₹5,00,000**.

**Balance Sheet as at 31 Mar 2025:**

| Particulars | Note | ₹ |
|---|---|---|
| **I. EQUITY AND LIABILITIES** | | |
| (1) Shareholders' Funds | | |
| &nbsp;&nbsp;(a) Share Capital | 1 | 10,00,000 |
| &nbsp;&nbsp;(b) Reserves & Surplus | 2 | 10,30,000 |
| (2) Non-current Liabilities | | |
| &nbsp;&nbsp;Long-term Borrowings | 3 | 6,00,000 |
| (3) Current Liabilities | | |
| &nbsp;&nbsp;Trade Payables | 4 | 3,20,000 |
| &nbsp;&nbsp;Provision for Tax | 5 | 1,60,000 |
| **TOTAL** | | **31,10,000** |
| **II. ASSETS** | | |
| (1) Non-current Assets | | |
| &nbsp;&nbsp;PPE (18,00,000 − 6,80,000) | 6 | 11,20,000 |
| (2) Current Assets | | |
| &nbsp;&nbsp;Inventories | 7 | 4,10,000 |
| &nbsp;&nbsp;Trade Receivables | 8 | 5,60,000 |
| &nbsp;&nbsp;Cash & Cash Equivalents | 9 | 2,40,000 |
| **TOTAL** | | **31,10,000** |

Note accumulated depreciation = 5,00,000 opening + 1,80,000 current = 6,80,000. Both sides tie at **₹31,10,000**. 

**Note 2 – Reserves & Surplus (show the movement):**

| | ₹ |
|---|---|
| General Reserve (4,00,000 + 1,00,000) | 5,00,000 |
| Surplus: Opening 1,50,000 + Profit 4,80,000 − Transfer 1,00,000 | 5,30,000 |
| **Total** | **10,30,000** |

Reproduce this in a workbook: TB on sheet 1, mapping column, `SUMIFS` per note, statements auto-populate.

## How it's tested

**Interview questions:**
- "Difference between T-format and Schedule III vertical format?"
- "How do you classify current vs non-current — give the rule."
- "Where does proposed dividend go now vs pre-2016?" (Now: disclosed in notes, provided only when declared.)
- "Walk me from trial balance to balance sheet."
- "What new disclosures did the March 2021 Schedule III amendment add?" (Ageing schedules, ratios, promoter holding, CSR, shortfall utilisation.)

**Practical/assessment tests:**
- A **timed Excel test (60–90 min):** here's a TB, produce Balance Sheet + P&L + Notes 1 and 2. They check if it ties and if groupings are right.
- **"Regroup this" case:** a competitor-style messy TB with wrong heads; fix the classification.
- **Audit-firm test:** given a client TB and last year's signed accounts, prepare current-year statements *with comparatives* and flag reclassifications.
- Sometimes a **Tally practical:** post given entries, group ledgers, generate the vertical balance sheet.

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Balance sheet doesn't tie | Reconcile via the `SUM(Dr)−SUM(Cr)=0` check *before* building; hunt `**UNMAPPED**` ledgers |
| Netting off — showing TR net of advances | Never net; show gross assets and gross liabilities separately |
| Forgetting current maturities of long-term debt | Split loan repayment schedule; reclassify the next-12-months portion to current |
| Missing ageing schedules / ratios (post-2021) | Keep a checklist of the 8 new mandatory disclosures |
| Depreciation shown as reduction in gross PPE | Keep gross block and accumulated depreciation as separate note columns |
| Prior-year figures not regrouped | Regroup comparatives to match current classification and add a note |
| Wrong reserve movement | Always present Reserves & Surplus as opening + additions − deductions = closing |
| Rounding chaos | Fix one unit (₹ lakhs/₹ full) across all statements; state it in the header |

Pros build **one linked template** and reuse it — they never rekey. They also keep a **lead schedule** per note tying back to the TB, which is exactly what auditors ask for.

## Learn-it roadmap & resources

**Time to proficiency: 3–5 weeks** of deliberate practice if you already know debits/credits.

- **Week 1:** Read Schedule III Division I text (it's short — MCA website, free). Memorise the line-item order.
- **Week 2:** Rebuild 3 real published company balance sheets from their notes backwards into a TB, then forward again.
- **Week 3:** Do 5 timed TB→statements exercises in Excel with `SUMIFS` mapping.
- **Week 4:** Add the 2021 amendment disclosures (ageing, ratios). Do the same in TallyPrime.
- **Week 5:** Practise comparatives and appropriations.

**Resources:**
- **Schedule III, Companies Act 2013** — the primary source, free on mca.gov.in.
- **ICAI "Guidance Note on Division I & II of Schedule III"** — free PDF, the definitive reference.
- **Taxmann / Bharat's "Company Balance Sheet & P&L"** — worked formats (paid).
- **TallyPrime learning (Tally Education)** for the ERP path.
- **Certification:** CA Intermediate (Advanced Accounting) covers this fully; ICAI's Certificate Course on Financial Reporting; any "Company Final Accounts" MOOC.

## Quick-reference

**Schedule III Balance Sheet order (Division I):**
```
EQUITY & LIABILITIES
  1 Shareholders' Funds → Share Capital | Reserves & Surplus | Money pending allotment
  2 Non-current Liabilities → Long-term Borrowings | Deferred Tax Liab | Other | LT Provisions
  3 Current Liabilities → ST Borrowings | Trade Payables | Other CL | ST Provisions
ASSETS
  1 Non-current Assets → PPE | Intangibles | Non-current Investments | LT L&A | Other
  2 Current Assets → Inventories | Current Investments | Trade Receivables | Cash & Cash Eq | ST L&A | Other
```

**P&L order:** Revenue from Operations → Other Income → Total Income → (Cost of Materials, Purchases, Change in Inventory, Employee Benefits, Finance Costs, Depreciation, Other Expenses) → PBT → Tax → PAT → EPS.

| Item | Rule / value |
|---|---|
| Current classification | Due / realised within 12 months or operating cycle |
| TB check | `=SUM(Dr)-SUM(Cr)` must = 0 |
| Note total formula | `=SUMIFS(Dr,Note,n)-SUMIFS(Cr,Note,n)` |
| Ageing buckets | <6m, 6m-1y, 1-2y, 2-3y, >3y |
| 2021 new disclosures | Ageing, ratios, promoter holding, CSR, title deeds, shortfall use |
| Proposed dividend | Not provided; disclosed in notes until declared |
| Format | Vertical only (T-format illegal for companies) |
| Filing form | AOC-4 to ROC |
