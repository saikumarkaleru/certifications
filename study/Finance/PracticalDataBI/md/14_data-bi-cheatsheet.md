# Cheat-sheet: SQL, DAX & pandas

## What it is & where it's used

This chapter is a dense, printable reference for the three languages that do the heavy lifting in a modern finance-analytics job: **SQL** (pull and shape data from a database), **DAX** (build measures inside Power BI / Excel Power Pivot), and **pandas** (Python data-wrangling). You use SQL to answer "how much did we bill client X in FY25?" against a warehouse; DAX to make a P&L dashboard that recalculates as a CFO clicks filters; pandas to reconcile a 200k-row bank statement against the ledger in 30 seconds.

Roles that touch these daily: **FP&A analyst**, **finance/business analyst**, **management-reporting (MIS) executive**, **revenue/GL accountant in a shared-service centre**, **credit / risk analyst**, and **audit-analytics** teams at the Big 4. In Indian GCCs (Deloitte USI, EY GDS, Accenture, Genpact, TresVista) a job ad that says "hands-on with Power BI and SQL" is testing exactly the muscle memory below.

## The gap: why companies want this (and college didn't teach it)

An MBA-Finance or CA course teaches you *what* a P&L, a reconciliation, or a variance is. It does not teach you to compute it over 500,000 rows without Excel choking. The gap is **mechanical fluency at scale**:

- College: `VLOOKUP` two sheets. Job: `LEFT JOIN` a 4-million-row invoice table to a customer master and not create duplicates.
- College: a static ratio in a template. Job: a `CALCULATE(SUM(...), FILTER(...))` measure that stays correct when the user slices by region *and* month.
- College: retype numbers. Job: a pandas script that runs the same reconciliation every morning, unattended.

Employers pay for the person who can turn a vague ask ("why did margin drop in Q3?") into a query, a measure and a chart in an hour. That is a skill nobody grades in an exam, so it screens candidates hard.

## What "proficient" looks like

The concrete bar an interviewer expects you to clear **unaided**:

- **SQL**: write a `JOIN` + `GROUP BY` + `HAVING` query; use a window function (`SUM() OVER`, `ROW_NUMBER()`) for running totals and de-duplication; explain the difference between `WHERE` and `HAVING`, and `INNER` vs `LEFT` join, without notes.
- **DAX**: know that a measure recomputes in *filter context*; write `CALCULATE` with a filter; build a YoY / YTD measure using `SAMEPERIODLASTYEAR` and `TOTALYTD`; understand `SUM` (a column) vs `SUMX` (row-by-row).
- **pandas**: load a CSV/Excel, `merge` two frames, `groupby().agg()`, `pivot_table`, handle NaNs, and export back to Excel — cleanly, in under 20 lines.

## Hands-on: how to actually do it

### SQL — the clauses you use every day

Logical execution order (memorise this — it explains 90% of bugs): `FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.

```sql
-- Revenue by customer for FY25 (Apr-24 to Mar-25), > 10 lakh only
SELECT c.customer_name,
       SUM(i.amount)                      AS total_rev,
       COUNT(*)                           AS invoice_count
FROM   invoices i
JOIN   customers c ON c.customer_id = i.customer_id   -- INNER: only matched rows
WHERE  i.invoice_date BETWEEN '2024-04-01' AND '2025-03-31'
GROUP  BY c.customer_name
HAVING SUM(i.amount) > 1000000            -- filter AFTER aggregation
ORDER  BY total_rev DESC
LIMIT  20;
```

```sql
-- Window functions: running total + latest row per customer
SELECT customer_id, invoice_date, amount,
       SUM(amount) OVER (PARTITION BY customer_id ORDER BY invoice_date) AS running_total,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY invoice_date DESC) AS rn
FROM   invoices;          -- keep WHERE rn = 1 in an outer query to get the latest invoice
```

```sql
-- Categorise ageing (AR buckets) with CASE
SELECT invoice_id, amount,
       CASE WHEN DATEDIFF(CURRENT_DATE, due_date) <= 0   THEN 'Not due'
            WHEN DATEDIFF(CURRENT_DATE, due_date) <= 30  THEN '0-30'
            WHEN DATEDIFF(CURRENT_DATE, due_date) <= 90  THEN '31-90'
            ELSE '90+' END AS ageing_bucket
FROM   invoices WHERE status = 'OPEN';
```

`COALESCE(col, 0)` swaps NULLs for 0; `LEFT JOIN` keeps unmatched left rows (use it to find invoices with **no** payment: `WHERE p.payment_id IS NULL`).

### DAX — measures for a Power BI P&L

```dax
Total Sales     = SUM(Sales[Amount])
Total Cost      = SUM(Sales[Cost])
Gross Margin %  = DIVIDE([Total Sales] - [Total Cost], [Total Sales])   -- DIVIDE = safe /0

-- Filter context override: sales only for the North region, ignoring page slicers
North Sales     = CALCULATE([Total Sales], Sales[Region] = "North")

-- Row-by-row: value = qty * price computed per row, then summed
Revenue         = SUMX(Sales, Sales[Qty] * Sales[Price])

-- Time intelligence (needs a marked Date table)
Sales YTD       = TOTALYTD([Total Sales], 'Date'[Date], "31-03")   -- Indian FY year-end
Sales LY        = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
YoY %           = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
```

`SUM` aggregates one column; `SUMX` iterates a table and evaluates an expression per row — use `SUMX` whenever the math is `A * B` at row level. `CALCULATE` is the one function to truly master: it *modifies filter context*.

### pandas — reconciliation and reshaping

```python
import pandas as pd

ledger = pd.read_excel("ledger.xlsx", sheet_name="GL")
bank   = pd.read_csv("bank_stmt.csv", parse_dates=["txn_date"])

# Clean + merge on a key
recon = ledger.merge(bank, on="utr_no", how="outer", indicator=True)
unmatched = recon[recon["_merge"] != "both"]          # breaks to investigate

# Group & aggregate (the SQL GROUP BY equivalent)
summary = (ledger
           .groupby("cost_centre")
           .agg(total=("amount", "sum"), count=("amount", "size"))
           .reset_index())

# Pivot to a matrix (months across columns)
pt = ledger.pivot_table(index="account", columns="month",
                        values="amount", aggfunc="sum", fill_value=0)

ledger["amount"] = ledger["amount"].fillna(0)          # handle blanks
summary.to_excel("mis_summary.xlsx", index=False)      # ship it
```

## Worked example / mini-project

**Task:** monthly MIS — revenue by region with a YoY view — from a raw sales table.

Sample `sales` table (₹ lakh):

| sale_date | region | amount |
|-----------|--------|--------|
| 2024-05-10 | South | 12.5 |
| 2024-05-22 | North | 8.0 |
| 2025-05-08 | South | 15.0 |
| 2025-05-19 | North | 9.5 |

**Step 1 — SQL to pull the monthly base:**

```sql
SELECT region,
       DATE_FORMAT(sale_date, '%Y-%m') AS mth,
       SUM(amount)                     AS rev
FROM   sales
GROUP  BY region, DATE_FORMAT(sale_date, '%Y-%m')
ORDER  BY region, mth;
```

**Step 2 — load into Power BI, build measures:**

```dax
Rev     = SUM(sales[amount])
Rev LY  = CALCULATE([Rev], SAMEPERIODLASTYEAR('Date'[sale_date]))
YoY %   = DIVIDE([Rev] - [Rev LY], [Rev LY])
```

For May: South ₹15.0L vs ₹12.5L LY → **+20%**; North ₹9.5L vs ₹8.0L → **+18.75%**. Drop a matrix visual (rows = region, values = Rev, Rev LY, YoY %) and a Date slicer.

**Step 3 — same answer in pandas as a sanity check:**

```python
df["yr"] = df["sale_date"].dt.year
piv = df.pivot_table(index="region", columns="yr", values="amount", aggfunc="sum")
piv["yoy_%"] = (piv[2025] - piv[2024]) / piv[2024] * 100
print(piv.round(2))
```

Three tools, one number — that cross-check *is* the job.

## How it's tested

- **SQL screen (30–45 min, HackerRank / live editor):** you're given 2–3 tables and asked "top 5 customers by revenue", "second-highest salary" (window function), or "invoices with no payment" (`LEFT JOIN … IS NULL`). Interviewers love `WHERE` vs `HAVING` and `INNER` vs `LEFT`.
- **Power BI / DAX case:** a take-home dataset — "build a P&L dashboard with YoY and a region slicer." They check whether your measures survive slicing (filter-context awareness) and whether you used `DIVIDE` not `/`.
- **pandas / Python round:** "read these two files, reconcile, output the breaks" or a `groupby` + `pivot_table` puzzle.
- **Verbal:** "Explain filter context." "SUM vs SUMX?" "How do you avoid a fan-out / duplicate join?"

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Duplicated rows after a join (fan-out) | Join on a **unique** key; check row count before/after; aggregate before joining |
| `WHERE` used to filter an aggregate | Aggregates go in `HAVING`, not `WHERE` |
| Dividing by zero blows up DAX | Always `DIVIDE(a, b)` — returns blank on /0 |
| Using `SUM` where math is row-level | Use `SUMX(table, qty*price)` |
| No Date table → time intelligence fails | Add a marked `Date` table, join it, use `TOTALYTD`/`SAMEPERIODLASTYEAR` |
| `merge` silently drops rows | Use `how="outer", indicator=True`, inspect `_merge` |
| Chained-assignment / SettingWithCopy warning | Use `.loc[]` or `.copy()` |
| Trusting NULL == NULL in SQL | Test with `IS NULL`; `COALESCE` before comparing |

## Learn-it roadmap & resources

Realistic time to interview-ready (2 hrs/day):

- **SQL:** 3–4 weeks. Free: SQLBolt, Mode Analytics SQL tutorial, LeetCode Database (Easy/Medium), StrataScratch.
- **DAX / Power BI:** 4–6 weeks. Free: Microsoft Learn "Power BI" path, SQLBI.com (Marco Russo), "Learn DAX" YouTube. Cert (optional but strong on a resume): **PL-300 Microsoft Power BI Data Analyst** (~US$165 / ~₹4,800).
- **pandas:** 3–4 weeks. Free: Kaggle "Pandas" + "Python" micro-courses, the official 10-minutes-to-pandas guide.

Practice on real data: your bank statement, a GST sales register, or public datasets (data.gov.in). Rebuild one MIS report end-to-end across all three tools — that single project teaches more than 20 tutorials.

## Quick-reference

**SQL**
```
SELECT col, AGG(x) FROM t JOIN u ON t.k=u.k
WHERE ...  GROUP BY col  HAVING AGG(x)>n  ORDER BY col DESC  LIMIT n;
Joins: INNER (matched) | LEFT (keep left) | anti-join: LEFT + IS NULL
Window: SUM()/AVG() OVER(PARTITION BY .. ORDER BY ..), ROW_NUMBER(), RANK(), LAG()/LEAD()
NULLs: COALESCE(c,0) | IS NULL | NULLIF(a,b)
Dates: BETWEEN, DATEDIFF(), DATE_FORMAT()
```

**DAX**
```
SUM / AVERAGE / COUNTROWS(col)          -- aggregate one column
SUMX(tbl, expr)                         -- row-by-row then sum
CALCULATE(expr, filter1, filter2)       -- modify filter context (the key one)
DIVIDE(num, den[, 0])                   -- safe division
FILTER(tbl, cond) | ALL() | ALLEXCEPT() -- filter helpers
SAMEPERIODLASTYEAR / TOTALYTD / DATESYTD-- time intelligence
RELATED() | RELATEDTABLE()              -- cross-table lookup
```

**pandas**
```
pd.read_csv / read_excel / to_excel
df.merge(o, on="k", how="left"/"outer", indicator=True)
df.groupby("c").agg(t=("x","sum"), n=("x","size"))
df.pivot_table(index=, columns=, values=, aggfunc="sum", fill_value=0)
df.loc[mask, "col"] = v   |  df["c"].fillna(0)  |  df.drop_duplicates()
df.assign(newcol=...)  |  df.sort_values("c", ascending=False)
```

**Mental map:** SQL `GROUP BY` = pandas `groupby` = DAX aggregate in filter context. SQL `JOIN` = pandas `merge` = DAX relationship. Same idea, three dialects.
