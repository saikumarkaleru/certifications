# Power Query: Cleaning Real Company Data

## What it is & where it's used

Power Query is the built-in **ETL engine** (Extract, Transform, Load) inside Excel and Power BI. You point it at messy source data — a bank statement export, a GST portal download, ten branch files in a folder, a Tally ledger dump — record a sequence of cleaning steps, and it produces a clean table. The magic word is **refreshable**: when next month's file arrives, you drop it in and hit **Refresh**. All your steps replay automatically. No re-cleaning, no re-formulas.

Find it in Excel under **Data → Get Data** (Windows Excel 2016+ and Microsoft 365; the ribbon group is called "Get & Transform Data"). It writes its logic in a language called **M**, but 90% of the job is done with clicks in the Power Query Editor.

Roles that live in Power Query: **FP&A analysts** consolidating branch actuals, **accounts payable/receivable teams** reconciling ledgers, **GST/tax executives** cleaning portal downloads for GSTR-2B vs purchase-register matching, **MIS analysts** building monthly management packs, and anyone who currently spends the first three days of every month copy-pasting and running find-replace.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you ratio analysis on data that was **already clean**. Real company data never is. The gap employers pay to close:

- **Source data is filthy.** Merged cells, ₹ signs stored as text, dates as "01-Apr-25" strings, blank header rows, totals mixed into detail rows, "1,20,000" with Indian comma grouping that Excel reads as text.
- **The same clean-up runs every single month.** College projects are one-shot. A job is the *same* report 12 times a year. Manual cleaning that "only takes 2 hours" costs 24 hours a year and breaks the moment a colleague is on leave.
- **VLOOKUP-and-paste doesn't scale.** When AP hands you a 40,000-row purchase register and 38,000-row GSTR-2B, a manual match is impossible. Power Query merges them in seconds.

Employers have watched analysts burn days on this. Someone who says "give me the raw dump, I'll build a refreshable query" is instantly more valuable than someone who reaches for a fresh round of copy-paste.

## What "proficient" looks like

A job-ready person can, unaided:

1. **Import** from Excel, CSV, a whole folder, and a database — and know that **Get Data → From Folder** stacks 12 monthly files into one table.
2. **Unpivot** a wide "months across columns" report into a tidy long table (the single most-tested skill).
3. **Merge** two queries (Left Outer, Inner, Left Anti) — and know *which* join to use for a reconciliation.
4. **Append** queries to stack same-shape tables.
5. **Remove errors, fill down, split columns, change types, trim/clean text, and replace values** without breaking on next refresh.
6. Understand that steps are **recorded and replayed**, so column names and types must be handled deliberately.

## Hands-on: how to actually do it

### Import from a folder (consolidate 12 branch files)

```
Data → Get Data → From File → From Folder → pick folder → Combine & Transform
```

Power Query samples the first file, applies the transform to all, and stacks them. Add a step to keep the source file name so you know which branch a row came from — it's the `Source.Name` column.

### Unpivot (the interview favourite)

Raw MIS often looks like this:

| Branch | Apr | May | Jun |
|---|---|---|---|
| Mumbai | 120000 | 135000 | 128000 |
| Pune | 90000 | 88000 | 94000 |

Select the **Branch** column → right-click → **Unpivot Other Columns**. Result:

| Branch | Attribute | Value |
|---|---|---|
| Mumbai | Apr | 120000 |
| Mumbai | May | 135000 |

Rename `Attribute` → `Month`, `Value` → `Sales`. Now it's a proper table you can pivot, filter, or feed to Power Pivot. **Always use "Unpivot Other Columns"** so new month columns next quarter are captured automatically.

### Clean Indian-format numbers stored as text

"1,20,000" imports as text. In the Editor, **Transform → Format → Trim & Clean**, then **Replace Values**: replace `,` with nothing, then **Change Type → Whole Number**. The equivalent M step:

```m
= Table.ReplaceValue(Source, ",", "", Replacer.ReplaceText, {"Amount"})
```

### Split columns

A cell like `27AABCU9603R1ZM - Uma Traders` (GSTIN + name):

```
Split Column → By Delimiter → " - " → at each occurrence
```

Or split GSTIN to grab the **state code** (first 2 chars): **Split Column → By Number of Characters → 2 → Once, as far left as possible**. State code `27` = Maharashtra.

### Remove errors and fill down

After a type change, bad rows show `Error`. Select the column → **Remove Errors** (or **Replace Errors** with `0`). For a report where the branch name appears once then blanks below it: select column → **Transform → Fill → Down**.

### Merge queries (reconciliation)

To find purchases in your register that are **missing** from GSTR-2B:

```
Home → Merge Queries → pick PurchaseRegister & GSTR2B
→ match on [GSTIN] + [Invoice No]  (Ctrl-click both keys in each table)
→ Join Kind: Left Anti (rows only in first)
```

**Join kinds you must know:**

| Join Kind | Returns | Use for |
|---|---|---|
| Left Outer | All left + matches | Enrich data (add vendor name) |
| Inner | Only matched rows | Confirmed matches |
| Left Anti | Left rows with NO match | **Missing / unreconciled items** |
| Right Anti | Right rows with NO match | In 2B but not in books |

### Append queries (stack)

```
Home → Append Queries → Three or more tables → add Q1, Q2, Q3, Q4
```

Same columns, stacked into one — a full-year table from four quarterly files.

## Worked example / mini-project: GSTR-2B vs Purchase Register match

**Goal:** find input tax credit (ITC) you can claim, and mismatches to chase.

**Source 1 — `PurchaseRegister.xlsx`** (your books):

| GSTIN | Invoice No | Taxable | IGST |
|---|---|---|---|
| 27AABCU9603R1ZM | INV-001 | 100000 | 18000 |
| 29AAGCB1286Q1ZP | INV-002 | 50000 | 9000 |
| 07AABCU9603R1ZX | INV-003 | 20000 | 3600 |

**Source 2 — `GSTR2B.csv`** (portal download):

| GSTIN | Invoice No | IGST_2B |
|---|---|---|
| 27AABCU9603R1ZM | INV-001 | 18000 |
| 29AAGCB1286Q1ZP | INV-002 | 8500 |

Steps:

1. **Get Data → From Excel** → load `PurchaseRegister` as a connection-only query. Repeat **From Text/CSV** for `GSTR2B`.
2. In each, **Trim** the Invoice No (portal data has trailing spaces — a classic silent mismatch killer) and set types.
3. On `PurchaseRegister`: **Merge Queries** → `GSTR2B`, match on `GSTIN` + `Invoice No`, **Left Outer**. Expand `IGST_2B`.
4. Add a **Custom Column** to flag status:

```m
= if [IGST_2B] = null then "Missing in 2B"
  else if [IGST] <> [IGST_2B] then "Tax mismatch"
  else "Matched"
```

Result:

| Invoice No | IGST | IGST_2B | Status |
|---|---|---|---|
| INV-001 | 18000 | 18000 | Matched |
| INV-002 | 9000 | 8500 | Tax mismatch |
| INV-003 | 3600 | (null) | Missing in 2B |

**Close & Load** to a sheet. INV-002 has a ₹500 mismatch to query with the vendor; INV-003's ₹3,600 ITC can't be claimed until the vendor files. Next month, drop in the new files and **Refresh** — the whole reconciliation rebuilds in seconds.

## How it's tested

**In interviews (verbal):**
- "You have sales in columns Jan–Dec, one row per product. How do you get one row per product-month?" → *Unpivot Other Columns.*
- "Which join finds invoices in your books but not on the GST portal?" → *Left Anti.*
- "Difference between Merge and Append?" → *Merge = join sideways on a key; Append = stack rows.*
- "How do you consolidate 15 branch files with one click each month?" → *From Folder → Combine & Transform.*

**Practical test (very common):** you're given a deliberately messy workbook — merged cells, ₹ text amounts, months across columns, a second sheet to reconcile against — and 30–45 minutes to produce a clean, refreshable output. They then **change the data and hit Refresh** to check your query didn't hard-code anything.

**Red flag they watch for:** did you clean it with manual find-replace on the sheet (breaks on refresh) or inside Power Query (survives refresh)? The whole point is the second one.

## Common mistakes & how pros avoid them

| Mistake | Consequence | Pro fix |
|---|---|---|
| Hard-coding a "Changed Type" with fixed column names | Breaks when a column is renamed upstream | Delete unneeded auto-type steps; type only what you need, late |
| Using "Unpivot Columns" instead of "Unpivot **Other** Columns" | New month columns get dropped next quarter | Always unpivot *other* columns |
| Not trimming text before a merge | Silent non-matches from trailing spaces | Trim + Clean both key columns first |
| Filtering by a specific value (e.g. keep only "Apr") | Wrong data after refresh | Filter on logic, not a snapshot value |
| Loading giant tables to a sheet you don't need | Slow, bloated file | Use **Connection Only** + load to Data Model |
| Renaming columns then referencing old names later | Step errors on refresh | Rename once, early, and keep it consistent |

## Learn-it roadmap & resources

**Time to proficiency: about 2–3 weeks** of evening practice for someone comfortable in Excel. Power Query is unusually learnable because it's click-driven — you can be productive before you understand M.

- **Week 1:** Import (Excel/CSV/Folder), change types, remove columns, split, trim, replace values, fill down.
- **Week 2:** Unpivot, group by, merge (all join kinds), append.
- **Week 3:** Custom columns, conditional columns, a light touch of M, and building one real refreshable monthly report end-to-end.

**Resources:**
- **Microsoft Learn — "Get & Transform in Excel"** (free, official).
- **Excel Is Fun** and **MyOnlineTrainingHub** (Mynda Treacy) — free YouTube, finance-friendly examples.
- **Book:** *Master Your Data with Excel and Power BI* — Ken Puls & Miguel Escobar (the definitive Power Query reference).
- **Certification:** it's covered inside the **Microsoft PL-300 (Power BI Data Analyst)** exam — worth listing on a CV, though for most finance jobs a demonstrated project matters more than the cert.

## Quick-reference

| Task | Click-path |
|---|---|
| Import one file | Data → Get Data → From File → From Workbook/CSV |
| Stack many files | Get Data → From File → From Folder → Combine & Transform |
| Wide → long | Select key cols → right-click → Unpivot Other Columns |
| Fill blanks below | Column → Transform → Fill → Down |
| Clean text | Transform → Format → Trim, then Clean |
| Split GSTIN state code | Split Column → By Number of Characters → 2 |
| Reconcile / find missing | Home → Merge Queries → Join Kind: **Left Anti** |
| Enrich (add name) | Merge → **Left Outer** → Expand |
| Stack same-shape tables | Home → Append Queries |
| Don't load to sheet | Close & Load To → **Connection Only** |
| Re-run everything | Data → **Refresh All** |

**Join cheat:** Left Outer = enrich · Inner = confirmed matches · Left Anti = missing in second · Right Anti = extra in second.

**Golden rule:** never fix data on the sheet — fix it in Power Query, so next month is one click: **Refresh**.
