# Advanced Excel Power User: Dynamic Arrays, LAMBDA, LET, Data Model

## What you'll be able to do
Turn Excel from a grid you type into by hand into a small application. By the end you can: write a single formula that spills a filtered, sorted, de-duplicated table; replace nested VLOOKUPs with XLOOKUP and dynamic-array logic; name your own reusable functions with LAMBDA so a 200-cell workbook shrinks to 20; build a proper relational Data Model (Power Pivot) across fact and dimension tables and write DAX measures; run reverse-solve tools (Goal Seek, Solver, Data Tables) for finance scenarios; and drive the whole thing keyboard-only. You'll build a working "Receivables Ageing + Collections" mini-tool that a manager could actually use.

## The essentials
**Dynamic arrays (Excel 365 / 2021+).** One formula returns many results that "spill" into neighbouring cells. The top-left cell holds the formula; the spilled range is referenced with `#` (e.g. `E2#`). A `#SPILL!` error means something blocks the spill area — clear it.

| Function | Does | Signature |
|---|---|---|
| `FILTER` | keep rows meeting a condition | `FILTER(array, include, [if_empty])` |
| `SORT` / `SORTBY` | order results | `SORT(array,[col],[order])` |
| `UNIQUE` | distinct values | `UNIQUE(array)` |
| `XLOOKUP` | lookup left/right, exact by default, returns arrays | `XLOOKUP(lookup, lookup_array, return_array, [if_not_found], [match_mode])` |
| `SEQUENCE` | generate 1..n | `SEQUENCE(rows,[cols],[start],[step])` |

**LET** names intermediate calculations inside one formula so you compute once and read clearly: `LET(name1, value1, name2, value2, …, result)`. It's faster (no repeated sub-expressions) and readable.

**LAMBDA** defines a reusable function. Wrap your logic, name it in Name Manager (Formulas → Define Name), then call it like a built-in. Helpers: `MAP`, `REDUCE`, `SCAN`, `BYROW`, `BYCOL` apply a LAMBDA across arrays.

**SUMPRODUCT** multiplies arrays element-wise then sums — the classic pre-365 way to do conditional maths and weighted averages: `SUMPRODUCT((region="West")*(qty)*(price))`. Coercing booleans with `--` or `*` turns TRUE/FALSE into 1/0.

**Data Model / Power Pivot.** Load tables into the in-memory model (Data → "Add to Data Model" or from Power Query). Create *relationships* (one-to-many, dimension→fact) so you never VLOOKUP again. Write **DAX** measures: `Total Sales := SUMX(Sales, Sales[Qty]*Sales[Price])`. A PivotTable built on the model can slice a 5-million-row fact table instantly.

**What-If tools.** *Goal Seek* (Data → What-If → Goal Seek): set one cell to a target by changing one input. *Data Table*: recompute a formula across one or two varying inputs (sensitivity grid). *Solver* (add-in): optimise a target subject to multiple constraints — used for portfolio weights, capex allocation, blending.

## Hands-on — step by step
Worked example: a raw invoice list on sheet `Data`, columns A–E: `Customer, Invoice, InvDate, Amount, PaidFlag`. Today is 13-Jul-2026. Sample rows: Alpha 001 10-Mar 120000 N; Beta 002 01-Jun 80000 N; Alpha 003 20-Jun 50000 Y; Gamma 004 05-May 200000 N.

1. **Make it a Table.** Click inside data → Ctrl+T → tick "My table has headers" → name it `tblInv` (Table Design → Table Name). Structured references now work: `tblInv[Amount]`.

2. **Open items only, sorted, one formula.** On sheet `Report` cell A1:
```
=SORT(FILTER(tblInv[[Customer]:[Amount]], tblInv[PaidFlag]="N", "No dues"), 4, -1)
```
This spills every unpaid invoice, largest first. No manual filter, no copy-paste.

3. **Ageing bucket with LET.** In a helper column of the model (or a spilled column) compute days overdue and bucket:
```
=LET(days, TODAY()-tblInv[InvDate],
     bucket, IFS(days<=30,"0-30", days<=60,"31-60", days<=90,"61-90", TRUE,"90+"),
     bucket)
```

4. **Reusable ageing function with LAMBDA.** Formulas → Name Manager → New. Name `AGEBUCKET`, Refers to:
```
=LAMBDA(d, IFS(d<=30,"0-30", d<=60,"31-60", d<=90,"61-90", TRUE,"90+"))
```
Now anywhere: `=AGEBUCKET(TODAY()-C2)` returns `61-90` for the 10-Mar invoice.

5. **Unique customers + outstanding per customer.** 
```
=UNIQUE(FILTER(tblInv[Customer], tblInv[PaidFlag]="N"))
```
spills Alpha, Beta, Gamma in G2#. Beside it in H2:
```
=SUMIFS(tblInv[Amount], tblInv[Customer], G2#, tblInv[PaidFlag], "N")
```
Alpha 120000, Beta 80000, Gamma 200000. (SUMIFS accepts the spilled array and returns a spilled result.)

6. **SUMPRODUCT weighted DSO check.** Weighted average age of receivables:
```
=SUMPRODUCT((TODAY()-tblInv[InvDate])*(tblInv[PaidFlag]="N")*tblInv[Amount]) / SUMPRODUCT((tblInv[PaidFlag]="N")*tblInv[Amount])
```

7. **Data Model version.** Select `tblInv` → Data → "Add to Data Model". Add a `dimCustomer` table (Customer, Segment), add to model, then Power Pivot → Diagram View → drag `dimCustomer[Customer]` to `tblInv[Customer]` to make the relationship. In Power Pivot write measures:
```
Outstanding := CALCULATE(SUM(tblInv[Amount]), tblInv[PaidFlag]="N")
```
Build a PivotTable: Segment on rows, `[Outstanding]` in values, slicer by ageing bucket.

8. **Goal Seek scenario.** Cell B20 = target collection this month formula. Data → What-If → Goal Seek: Set B20 to 300000 by changing collection-rate cell B18. Excel solves the rate.

9. **Two-variable Data Table.** Lay a grid: collection rate down the left, discount % across the top, top-left cell = the net-cash formula. Select the block → Data → What-If → Data Table → row input = discount cell, column input = rate cell.

**Keyboard-only speed:** Ctrl+T (table), Ctrl+Shift+L (filter), Alt+= (AutoSum), Ctrl+Shift+↓ (select to end), Ctrl+` (show formulas), F4 (toggle $ absolute / repeat last action), Alt,A,W,G (Goal Seek), Ctrl+Shift+Enter is *no longer needed* for arrays in 365.

## The output
A one-screen tool on `Report`:

```
RECEIVABLES AGEING — as at 13-Jul-2026
Customer   Outstanding   Bucket
Gamma        200,000     61-90
Alpha        120,000     90+
Beta          80,000     0-30
------------------------------
Total open   400,000
Weighted age   ~78 days (DSO proxy)
```
Everything spills from live formulas; change a `PaidFlag` from N to Y and every number, the unique list, and the pivot update instantly. The Data-Model PivotTable gives the same totals sliceable by segment.

## Checks, gotchas & red flags
- **`#SPILL!`** = the spill range is blocked or a merged cell sits in the way. Never merge cells in a data area.
- **Total must tie:** `SUM(H2#)` of per-customer outstanding must equal `SUMIFS` total open (400,000). If not, a PaidFlag has stray spaces — wrap in `TRIM`.
- **XLOOKUP vs VLOOKUP:** XLOOKUP defaults to *exact* match; VLOOKUP defaults to *approximate* (TRUE) — the classic silent-wrong-number bug. Always set VLOOKUP's 4th arg to FALSE.
- **Data Model relationships must be one-to-many** on a *unique* dimension key. Duplicate customer names in `dimCustomer` break the relationship (ambiguous).
- **Data Tables recalc the whole column** — slow on big models; switch calculation to "Automatic except data tables" (Formulas → Calc Options).
- **Solver** needs the add-in enabled (File → Options → Add-ins → Manage Excel Add-ins → Solver). It can return a *local* optimum; try different starting weights.
- Volatile functions (`TODAY`, `OFFSET`, `INDIRECT`) recalc on every change — avoid in huge sheets.

## Interview drill
**Q: When would you use LET over just writing the formula out?**
A: When a sub-expression repeats or the formula is unreadable. LET computes each named value once, so a formula that references `TODAY()-InvDate` three times evaluates it once — faster and self-documenting. It's the readability/performance bridge before you graduate to a named LAMBDA.

**Q: You have a 4-million-row transaction file and need sales by region by month. Excel or Power Pivot, and why?**
A: Power Pivot / Data Model. The columnar in-memory engine compresses and aggregates millions of rows a normal grid can't hold (1,048,576-row limit), relationships replace lookups, and a DAX measure like `SUMX` computes on the fly. A regular PivotTable off raw rows would be slow and hit the row cap.

**Q: Difference between SUMIFS and SUMPRODUCT for conditional sums?**
A: SUMIFS is faster and clearer for straightforward AND conditions on ranges. SUMPRODUCT is the tool when you need OR logic, arithmetic *inside* the condition (weighted averages, `days*amount`), or must support pre-365 files without dynamic arrays.

## Learn/practise (free)
All of this works in the free web/desktop trial of Microsoft 365; if you only have Excel 2016 you'll miss dynamic arrays and LAMBDA — practise those in **Excel for the web** (free with a Microsoft account) which has them. ExcelJet's function reference and Chandoo.org are excellent free tutorials. For DAX, Microsoft Learn's "Power Pivot" path and SQLBIT (sqlbi.com) free articles. Rehearse by downloading any public CSV (e.g. NSE bhavcopy, RBI datasets) and rebuilding the ageing tool above; then reproduce the same report three ways — dynamic arrays, SUMPRODUCT, and a Data-Model PivotTable — to prove they tie out.
