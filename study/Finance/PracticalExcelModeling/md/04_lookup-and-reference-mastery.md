# Lookup & Reference Mastery

## What it is & where it's used

Lookup functions answer one question that every finance job asks a hundred times a day: *"Given this ID, fetch me that value."* Given a vendor code, fetch the GSTIN. Given an employee ID, fetch the CTC. Given a ledger name, fetch the closing balance. Given an ISIN, fetch the market price.

You have a "lookup table" (a master somewhere) and a "working sheet" (your model), and you need to pull data from one into the other by a matching key. That is 60-70% of real analyst work — you rarely type numbers, you *stitch datasets together*.

Where it shows up by role:

| Role | Typical lookup job |
|---|---|
| Accounts payable | Match invoice numbers to a payment register; pull vendor bank details |
| GST / Tax | Reconcile GSTR-2B purchases against your purchase register (match by invoice + GSTIN) |
| FP&A / Analyst | Map trial-balance ledgers to P&L line items; build a driver-based model |
| Audit | Vouch a sample — pull supporting entries by voucher number |
| Treasury | Fetch FX rates or interest rates by date/currency |
| Investment / Equity research | Pull financials by ticker across years |

If you can only do one Excel thing well, make it lookups. It is the single most tested skill in a finance Excel screen.

## The gap: why companies want this (and college didn't teach it)

MBA and CA coursework teaches you *what* a reconciliation is, or *why* you allocate overheads — the concepts. It almost never makes you sit with two messy exports and physically join them. So freshers arrive knowing the theory of a bank reconciliation but not knowing how to match 4,000 bank lines to 4,000 book lines in ninety seconds.

The specific gaps employers see:

- **Manual matching mindset.** Freshers filter, eyeball, and copy-paste. A 2,000-row reconciliation takes them a day; a pro does it in five minutes with a lookup and a `MATCH`-based flag.
- **VLOOKUP-only, and fragile.** Many candidates know only `VLOOKUP`, which breaks the moment someone inserts a column and cannot look leftward. They have never met `INDEX-MATCH` or `XLOOKUP`.
- **No handling of "not found."** Real data has unmatched rows. Untrained users get `#N/A` everywhere and freeze. Pros trap it with a default and turn `#N/A` into a *finding* ("these 12 invoices are in books but not in 2B").
- **No dynamic arrays.** `FILTER`, `UNIQUE`, `SORT` (Excel 365 / 2021+) let you build a live sub-report with one formula. Colleges teach none of this because their labs run Excel 2007.

Closing this gap is what turns a "knows Excel" line on your CV into "does the reconciliation unaided by day two."

## What "proficient" looks like

A job-ready person can, unaided:

- Choose the right tool: `XLOOKUP` for a single fetch, `INDEX-MATCH` for legacy files, `FILTER` when they need *many* matching rows, not one.
- Do a **two-way lookup** (row key × column key) — e.g., pull the March figure for "Salaries" from a month × ledger grid.
- Handle not-found gracefully and treat unmatched rows as an audit output.
- Do an **approximate/range lookup** — slab-based, e.g., income-tax slabs or a commission grid.
- Lock references correctly (`$`) so a formula fills down and across without drifting.
- Explain *why* `XLOOKUP` beats `VLOOKUP` and rewrite an old `VLOOKUP` model without breaking it.

## Hands-on: how to actually do it

### 1. XLOOKUP — the modern default

Syntax: `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`

```
Pull a vendor's GSTIN by vendor code:
=XLOOKUP(A2, Vendors[Code], Vendors[GSTIN], "Not found")

Pull the closing balance for a ledger:
=XLOOKUP(A2, Ledger[Name], Ledger[Closing], 0)
```

- `if_not_found` = `"Not found"` — no more `#N/A`, no `IFERROR` wrapper.
- Return array can be **left of** the lookup array. VLOOKUP cannot.
- Return a whole row by pointing `return_array` at multiple columns: `=XLOOKUP(A2, Ledger[Name], Ledger[Opening]:Ledger[Closing])` spills opening→closing across.

### 2. INDEX-MATCH — works in every Excel version

```
=INDEX(Ledger[Closing], MATCH(A2, Ledger[Name], 0))
```

`MATCH` finds the *position* of the key; `INDEX` returns the value at that position. The `0` means exact match. Use this in any file that must open in Excel 2016 or older, or where colleagues don't have 365.

### 3. Two-way lookup (row × column)

Grid: ledgers down column A, months across row 1, figures inside.

```
XLOOKUP nested — fetch Salaries for Mar:
=XLOOKUP(G2, A2:A50, XLOOKUP(H2, B1:M1, B2:M50))

INDEX with two MATCHes — the classic:
=INDEX(B2:M50, MATCH(G2, A2:A50, 0), MATCH(H2, B1:M1, 0))
```

`G2` = "Salaries", `H2` = "Mar". The inner lookup picks the column; the outer picks the row.

### 4. Approximate / slab lookup (tax, commission)

Set a slab table sorted ascending by lower bound. Use `match_mode = -1` (exact or next smaller):

```
Slab table  A:B  →  lower bound | rate
=XLOOKUP(Income, SlabLower, SlabRate, , -1)
```

Old-style equivalent: `=VLOOKUP(Income, SlabTable, 2, TRUE)` — the `TRUE` is the range match.

### 5. Dynamic arrays — FILTER, UNIQUE, SORT (365 / 2021+)

```
Every invoice for one vendor (many rows, one formula):
=FILTER(Data, Data[Vendor]="ABC Traders", "None")

Unmatched invoices (in books, not in 2B):
=FILTER(Books[Inv], ISNA(XLOOKUP(Books[Inv], GSTR2B[Inv], GSTR2B[Inv])), "All matched")

Distinct list of ledgers:
=UNIQUE(Data[Ledger])

Sorted, de-duped vendor master:
=SORT(UNIQUE(Data[Vendor]))

Top 5 debtors by amount:
=SORT(FILTER(Data, Data[Type]="Debtor"), 3, -1)
```

These **spill** — one formula, a whole live block that recalculates as data changes. This is how you build a self-updating exception report.

## Worked example / mini-project: GSTR-2B vs Purchase Register reconciliation

You have two exports. Match input tax credit (ITC) claimed in books against what shows in GSTR-2B.

**Purchase Register** (sheet `PR`), columns: `A` Invoice No, `B` GSTIN, `C` Taxable, `D` GST.
**GSTR-2B** (sheet `2B`), columns: `A` Invoice No, `B` GSTIN, `C` Taxable, `D` GST.

Sample data:

| PR Invoice | GSTIN | PR GST (₹) |
|---|---|---|
| INV-101 | 27AABCU9603R1ZM | 18,000 |
| INV-102 | 29AAACI1234K1Z5 | 9,000 |
| INV-103 | 27AABCU9603R1ZM | 4,500 |

**Step 1 — flag whether each PR invoice is in 2B**, in column `E` of `PR`:

```
=IF(ISNA(XLOOKUP(A2, '2B'!A:A, '2B'!A:A)), "Missing in 2B", "Matched")
```

**Step 2 — compare the GST amount** (catch value mismatches), column `F`:

```
=IFERROR(D2 - XLOOKUP(A2, '2B'!A:A, '2B'!D:D), "Not in 2B")
```

A non-zero, non-error result = the same invoice with a different tax figure — a real reconciliation exception.

**Step 3 — build the exception report** on a fresh sheet, one formula:

```
=FILTER(PR!A2:F100, PR!E2:E100="Missing in 2B", "All reconciled")
```

**Step 4 — total ITC at risk** (in books but not in 2B, i.e., not claimable this month):

```
=SUMIF(PR!E:E, "Missing in 2B", PR!D:D)
```

Result: say ₹9,000 (INV-102) is missing in 2B → that ITC is provisionally not available, flag to the vendor. You just did in four formulas what a fresher does in half a day of filtering. Reverse the direction (2B not in PR) to catch invoices you forgot to book.

## How it's tested

**The practical test (most common).** You get two raw exports and 20-45 minutes: *"Reconcile these and tell me the unmatched items and the total difference."* They watch whether you reach for a lookup or start filtering manually. Reaching for `XLOOKUP`/`INDEX-MATCH` + a `FILTER` exception list is an instant pass.

**Live Excel screen.** Screen-share, a small table, and prompts like: "Pull the salary for employee E-045." "Now the master got a column inserted — did your formula survive?" (Tests whether you hard-coded a column index in `VLOOKUP`.)

**Interview questions you should be able to answer cold:**

- Difference between `VLOOKUP` and `INDEX-MATCH`? (Left-lookup, column-insert safety, speed.)
- Why does `VLOOKUP` return the wrong value sometimes? (Default `TRUE` approximate match on unsorted data.)
- How do you look up to the left? (`INDEX-MATCH` or `XLOOKUP`.)
- How do you return multiple matching rows? (`FILTER`, not any single-cell lookup.)
- What does the 4th argument of `MATCH`/`XLOOKUP` do? (Match mode: exact vs next-smaller for slabs.)

## Common mistakes & how pros avoid them

| Mistake | What breaks | Pro fix |
|---|---|---|
| `VLOOKUP` with `TRUE` (or omitted 4th arg) | Silent wrong values on unsorted data | Always pass `0`/`FALSE` for exact; use `-1` deliberately for slabs |
| Hard-coded column index (`VLOOKUP(...,4,0)`) | Breaks when a column is inserted | `XLOOKUP`/`INDEX-MATCH` reference the column by name/range |
| Forgetting `$` locks | Formula drifts when filled down | Lock the lookup array: `XLOOKUP(A2,$D$2:$D$99,$E$2:$E$99)` — or use Tables |
| Wrapping everything in `IFERROR` | Hides *real* errors, not just `#N/A` | Use `XLOOKUP`'s `if_not_found`, or `IFNA` (traps only `#N/A`) |
| Lookup key type mismatch | "INV-101" text vs 101 number → `#N/A` | Standardise with `TRIM`, `TEXT`, or `VALUE`; watch trailing spaces |
| Duplicate keys | Lookup returns only the first match | De-dupe with `UNIQUE`, or `FILTER` to see all; add a composite key |
| Composite matching (invoice **and** GSTIN) | Same invoice no. across vendors matches wrong row | Concatenate a key: `A2&"|"&B2` in both sheets, then look up that |
| Volatile giant ranges (`A:A`) on 100k rows | Workbook crawls | Reference actual used range or a Table |

## Learn-it roadmap & resources

**Realistic timeline:** 2-3 weeks of daily practice to interview-ready; solid in a couple of months of real use.

- **Days 1-3:** `XLOOKUP` and `INDEX-MATCH` exact matches; absolute references; `IFNA`.
- **Days 4-7:** Two-way lookups; approximate/slab lookups; convert an old `VLOOKUP` file to `XLOOKUP`.
- **Week 2:** Dynamic arrays — `FILTER`, `UNIQUE`, `SORT`; build the GSTR-2B recon above end to end.
- **Week 3:** Composite keys, duplicate handling, and doing a full reconciliation timed under 20 minutes.

**Resources**

- Microsoft's own `XLOOKUP` / `FILTER` support pages (free, authoritative — search "XLOOKUP function Microsoft").
- ExcelJet (free formula reference with examples) — excel​jet.net.
- Chandoo.org and Leila Gharani (YouTube) — free, finance-flavoured.
- Paid, if you want a certificate: **Microsoft Office Specialist: Excel Associate (MO-200)** or **Expert (MO-201)** — recognised, exam-based, ~₹4,000-5,000. For finance modelling context, a Corporate Finance Institute (CFI) or Wall Street Prep Excel module.
- Practice data: export any GSTR-2B JSON from the GST portal and your own purchase register — real data beats toy datasets.

## Quick-reference

```
XLOOKUP    =XLOOKUP(key, lookup_col, return_col, "not found", match_mode, search_mode)
INDEX-MATCH =INDEX(return_col, MATCH(key, lookup_col, 0))
Two-way     =INDEX(grid, MATCH(rowkey,rows,0), MATCH(colkey,cols,0))
Slab/range  =XLOOKUP(val, lower_bounds, rates, , -1)   'exact-or-next-smaller
Left lookup =XLOOKUP or INDEX-MATCH  (VLOOKUP cannot)
Many rows   =FILTER(data, criteria_range=criteria, "none")
Distinct    =UNIQUE(range)      Sorted =SORT(range, col, -1)
Composite   key = A2&"|"&B2  in both sheets, then look up the key
Trap N/A    =IFNA(formula, "-")   'only #N/A, not other errors
```

| VLOOKUP | XLOOKUP | Winner |
|---|---|---|
| Looks only rightward | Looks either direction | XLOOKUP |
| Hard-coded column index breaks on insert | Column referenced directly | XLOOKUP |
| Default approximate match (dangerous) | Default exact match | XLOOKUP |
| `#N/A` needs `IFERROR` wrapper | Built-in `if_not_found` | XLOOKUP |
| Works in all versions | Excel 365 / 2021+ only | VLOOKUP (legacy only) |

**Match modes (XLOOKUP/MATCH):** `0` exact · `-1` exact or next smaller (slabs, ascending) · `1` exact or next larger · `2` wildcard.
