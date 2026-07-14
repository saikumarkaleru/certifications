# Alteryx for Finance

## What you'll be able to do
Build a **repeatable, self-documenting data-prep workflow** in Alteryx Designer that a finance team runs every close without touching a formula. You'll know the canvas and the core tools — Input, Select, Filter, Formula, Join, Summarize, Output — and chain them into a visual pipeline that reconciles two ledgers and consolidates multi-entity data. You'll be able to explain *when Alteryx beats Excel* (and when it doesn't), read a workflow someone else built, and produce a clean output file plus a report of breaks. This is the tool GCC finance-transformation teams use to retire fragile macro-and-VLOOKUP spreadsheets.

## The essentials
**Alteryx Designer** is a desktop drag-and-drop ETL tool. You place **tools** on a **canvas** and connect them with wires; data flows left→right. Each tool shows a config panel and, at runtime, row counts on every wire — so you can see exactly where records drop. A saved workflow is a `.yxmd` file; run it and it reproduces identically every time. No coding required, though it supports formulas and R/Python.

**The core tool palette (the 80% you'll use):**
| Tool | Palette | Does |
|---|---|---|
| **Input Data** | In/Out | read a file/DB (xlsx, csv, SQL, etc.) |
| **Output Data** | In/Out | write result to file/DB |
| **Select** | Preparation | keep/drop/rename columns, set data types |
| **Filter** | Preparation | split rows by a condition (True/False outputs) |
| **Formula** | Preparation | add/modify columns with expressions |
| **Sort** | Preparation | order rows |
| **Join** | Join | match two inputs on key → **L** (left-only), **J** (matched), **R** (right-only) outputs |
| **Union** | Join | stack inputs (append) |
| **Summarize** | Transform | group & aggregate (sum, count, min…) |
| **Unique** | Preparation | de-duplicate |

**The Join tool is the heart of reconciliation.** Its three anchors are gold: **J** = matched pairs, **L** = records only in the left source, **R** = records only in the right. In recon, L and R *are* your breaks — no formula needed.

**Formula language** resembles Excel: `IF [Sales] > [Budget] THEN "Over" ELSE "OK" ENDIF`, `ABS([Ledger]-[Bank])`, `Trim([Ref])`, `DateTimeToday()`.

**When Alteryx beats Excel:** repeatable monthly processes; combining many files/sources; data too big for a sheet; when you need an *auditable* pipeline (every step visible, row counts prove nothing was lost); when handing a process to a team so it doesn't depend on one person's macro. **When Excel wins:** one-off analysis, ad-hoc modelling, final presentation formatting, or when no one on the team has an Alteryx licence (it's expensive — see below).

## Hands-on — step by step
Goal: reconcile **Ledger.xlsx** (our books: Ref, Amount) against **Bank.xlsx** (statement: Ref, Amount), flag amount differences and one-sided items, and output a clean workbook.

1. **Input Data ×2.** Drag two Input Data tools. Point the first at `Ledger.xlsx` (select the sheet), the second at `Bank.xlsx`. Run once (Ctrl+R) — wires show 3 rows and 3 rows.
2. **Select on each.** Add a Select tool after each Input. Rename `Amount` → `LedgerAmt` on the ledger branch and `Amount` → `BankAmt` on the bank branch (so columns don't clash after the join). Confirm `Ref` is a String type and `*Amt` is Double.
3. **Clean the key.** Add a Formula tool on each branch: overwrite `Ref` with `Trim([Ref])` to kill trailing spaces (the classic false-break cause).
4. **Join.** Drag a Join tool; wire ledger to the **L** input, bank to the **R** input. In config, join on `Ref = Ref`. Run. Now:
   - **J** anchor = refs in both. 
   - **L** anchor = refs only in the ledger → *"Missing in Bank."* 
   - **R** anchor = refs only in the bank → *"Missing in Ledger."*
5. **Compare amounts (off the J anchor).** Add a Formula tool: new column `Diff` = `[LedgerAmt] - [BankAmt]`, and `Status` = `IF ABS([LedgerAmt]-[BankAmt]) < 0.01 THEN "MATCHED" ELSE "DIFF" ENDIF`.
6. **Label the one-sided items.** Off **L**, a Formula adds `Status` = `"MISSING IN BANK"`. Off **R**, a Formula adds `Status` = `"MISSING IN LEDGER"`.
7. **Union everything.** Drag a Union tool; wire the J-branch, L-branch and R-branch into it. It auto-aligns columns by name (fill gaps with null). You now have one table of every ref with a Status.
8. **Filter breaks.** Add a Filter: `[Status] != "MATCHED"`. The **True** output = the breaks worth reviewing.
9. **Summarize a control total.** In parallel, add a Summarize off the ledger branch: Group nothing, Sum `LedgerAmt`; do the same for bank. This gives you a tie-out control (total ledger vs total bank).
10. **Output Data.** Wire the Union to an Output Data tool → write `Recon_Output.xlsx`, sheet `AllItems`; wire the Filter-True to a second Output → sheet `Breaks`. Save the workflow as `LedgerRecon.yxmd`.
11. **Re-run next month:** replace the two input files (same names) and press Ctrl+R. Identical logic, new numbers, in seconds.

**Consolidation variant:** to consolidate five entity files, use **Input** (or a single Input with a wildcard `*.xlsx` and "Output File Name as Field"), a **Select** to standardise columns, a **Union** to stack them, a **Formula** to tag the entity from the filename, then **Summarize** grouping by Account to get the consolidated trial balance.

## The output
`Recon_Output.xlsx` → sheet **AllItems**:

```
Ref     LedgerAmt   BankAmt    Diff     Status
INV001   120000     120000        0     MATCHED
INV002    80000      79500      500     DIFF
INV003    50000       (null)      -     MISSING IN BANK
INV009    (null)      30000      -     MISSING IN LEDGER
```
sheet **Breaks** (Filter-True) shows only INV002, INV003, INV009 — the exact list a reviewer works. The workflow canvas itself is the documentation: anyone can open `.yxmd` and see Input → Select → Formula → Join → Union → Filter → Output with live row counts proving 3+3 records fully accounted for.

## Checks, gotchas & red flags
- **Row-count reconciliation:** L-count + J-count must equal the left input count; R + J must equal the right. If not, a null or type-mismatch in the key silently dropped rows.
- **Join keys must be same data type.** `Ref` as String on one side and Int64 on the other → zero matches. Set types in Select first.
- **Trim keys** on both sides — trailing spaces are the number-one false break; do it before the Join, not after.
- **Union aligns by name by default;** if a source misspells a column it lands in a new column full of nulls. Check the Union config's field map.
- **Float comparison:** use `ABS(a-b) < 0.01`, never `a = b`.
- **Don't confuse Join's L/R anchors** — L is the *top* input (unmatched-left), R the bottom. Mislabelling flips "missing in bank" vs "missing in ledger."
- **Licensing red flag:** Alteryx Designer is a paid annual licence (roughly USD 5k+ per user/year list). Don't propose it for a one-analyst one-off — that's where Excel/Power Query wins. It earns its cost on recurring, multi-source, audited team processes.

## Interview drill
**Q: How do you reconcile two ledgers in Alteryx without a single formula for matching?**
A: A Join tool on the reference key. The J anchor gives matched pairs (then a Formula compares amounts), the L anchor gives items only in the first source, the R anchor items only in the second. L and R are the one-sided breaks by construction — the tool separates them for you; I only add a status label and Union them back for reporting.

**Q: When would you choose Alteryx over Excel/Power Query?**
A: When the process repeats every close, pulls from several files or databases, must be auditable (visible steps and row counts prove completeness), and is handed to a team rather than owned by one person's macro. For a one-off analysis or final formatting, Excel is faster and cheaper — and Power Query covers many mid-size repeatable jobs for free, so I'd only reach for Alteryx when scale, source variety, or governance justify the licence.

**Q: A join returns far fewer matched rows than expected. How do you debug?**
A: Check the L and R anchors' row counts to see what didn't match, then inspect the key: data-type mismatch (String vs Int), casing, and trailing spaces are the usual causes. Add Trim/UpperCase Formulas before the Join and confirm both keys are the same type in the Select tool; re-run and verify L+J and R+J reconcile to the input counts.

## Learn/practise (free)
Alteryx offers a **free 30-day Designer trial** and, importantly, **Alteryx Community** (community.alteryx.com) with the **Weekly Challenges** — dozens of free, graded data-prep puzzles with sample data and solution workflows; work through the beginner set to drill Join/Union/Summarize. The **Alteryx SparkED** programme gives students free learning licences and courses. If you can't get a licence, replicate every workflow above in **Power Query** (free) — the concepts map one-to-one (Merge = Join, Append = Union, Group By = Summarize), so you learn the pattern and can speak to Alteryx credibly in interviews. Rehearse by building the ledger recon end-to-end, deliberately introducing a trailing space and a type mismatch, and watching the L/R anchors reveal the breaks.
