# SQL for Finance: Foundations

## What it is & where it's used

SQL (Structured Query Language) is how you *ask questions of data that lives in a database* instead of a spreadsheet. When your company's transactions, ledgers, invoices, and customer masters outgrow Excel — usually past a few hundred thousand rows — they move to a database (PostgreSQL, MySQL, SQL Server, Snowflake, or the SQL layer inside your ERP). SQL is the language you use to pull, filter, and summarise that data.

In finance and accounting, SQL is the everyday tool for:

- **FP&A / financial analysts** — pulling actuals from the GL to build variance reports and MIS.
- **Accounts / R2R teams** — reconciling sub-ledgers to control accounts, ageing analysis, finding unposted entries.
- **Tax / GST analysts** — extracting invoice-level data to reconcile GSTR-1 vs books, matching ITC.
- **Internal audit & controls** — sampling transactions, testing for duplicate payments, journal-entry testing.
- **Revenue / collections** — customer ageing, DSO, overdue exposure.

You do not need to *build* databases. You need to *read* from them confidently. That is 90% of the finance SQL job, and it rests on six clauses: `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`.

## The gap: why companies want this (and college didn't teach it)

An MBA or CA course teaches you *what* a trial balance, an ageing schedule, or a GST reconciliation should look like. It assumes the data arrives clean. In a real company, the data sits in a database with 40 tables, cryptic column names, and 2 million rows — and *nobody hands you the summarised sheet*. You have to extract it yourself.

The specific gap:

- College says "the accountant will give you the ledger." Industry says "here's read access to the `gl_transactions` table — get what you need."
- Excel breaks, freezes, or silently truncates past ~1M rows. A single month of a mid-size company's transactions can exceed that.
- Analysts who can't write SQL become *dependent on the IT/BI team* for every data request, waiting days for a pull. Analysts who can write SQL are self-sufficient — and that self-sufficiency is exactly what gets you hired and promoted.

Employers have stopped treating SQL as an "IT skill." For any finance analyst role in a mid-to-large company, a basic SQL screen is now as standard as an Excel test.

## What "proficient" looks like

The bar for a finance analyst (not a data engineer) is narrow and achievable. Job-ready means you can, *unaided*:

- Write a `SELECT` with a `WHERE` filter on dates, amounts, and text — and get the exact rows you intend.
- `JOIN` two or three tables (e.g. transactions → customers → GL accounts) and know the difference between `INNER` and `LEFT JOIN`.
- Aggregate with `GROUP BY` (sum by account, by month, by customer) and filter groups with `HAVING`.
- Sort and rank with `ORDER BY ... DESC` and `LIMIT`.
- Read a query someone else wrote and explain what number it produces.
- Sanity-check your output against a known control total (does the SUM tie to the trial balance?).

You do *not* need window functions, stored procedures, or query tuning to clear this bar — those come later.

## Hands-on: how to actually do it

Assume three tables. This is a realistic mini-schema for an Indian company.

**`gl_transactions`**

| txn_id | txn_date | account_code | customer_id | debit | credit | narration |
|---|---|---|---|---|---|---|
| 1001 | 2026-04-05 | 4000 | C-01 | 0 | 118000 | Sales invoice INV-201 |
| 1002 | 2026-04-05 | 1200 | C-01 | 118000 | 0 | Debtor INV-201 |
| 1003 | 2026-04-08 | 5100 | NULL | 45000 | 0 | Office rent |

**`accounts`** ( `account_code`, `account_name`, `account_type` ) — the chart of accounts.
**`customers`** ( `customer_id`, `customer_name`, `state`, `gstin` ).

### SELECT + WHERE — pick columns and filter rows

```sql
-- All sales-account entries in April 2026, above ₹50,000
SELECT txn_date, account_code, credit, narration
FROM   gl_transactions
WHERE  account_code = 4000
  AND  txn_date BETWEEN '2026-04-01' AND '2026-04-30'
  AND  credit > 50000;
```

Key operators: `=`, `<>`, `>`, `<`, `BETWEEN`, `IN (…)`, `LIKE '%rent%'` (text search), `IS NULL`. Combine with `AND` / `OR`. Wrap `OR` groups in brackets so precedence is unambiguous.

### JOIN — combine tables

```sql
-- Attach account names and types to each transaction
SELECT t.txn_date, a.account_name, a.account_type,
       t.debit, t.credit
FROM   gl_transactions t
JOIN   accounts a  ON t.account_code = a.account_code
WHERE  t.txn_date >= '2026-04-01';
```

- **`INNER JOIN`** (just `JOIN`) — keeps only rows that match in both tables.
- **`LEFT JOIN`** — keeps *all* left-table rows; unmatched right side comes back `NULL`. Use `LEFT JOIN` when you want to find what's *missing*:

```sql
-- Customers with NO transactions this year (dormant accounts)
SELECT c.customer_id, c.customer_name
FROM   customers c
LEFT JOIN gl_transactions t ON c.customer_id = t.customer_id
WHERE  t.txn_id IS NULL;
```

### GROUP BY + HAVING — summarise, then filter groups

```sql
-- Net movement per GL account, only accounts with net > ₹1,00,000
SELECT a.account_name,
       SUM(t.debit)  AS total_debit,
       SUM(t.credit) AS total_credit,
       SUM(t.debit) - SUM(t.credit) AS net_debit
FROM   gl_transactions t
JOIN   accounts a ON t.account_code = a.account_code
GROUP BY a.account_name
HAVING SUM(t.debit) - SUM(t.credit) > 100000
ORDER BY net_debit DESC;
```

The mental model: `WHERE` filters **rows** *before* grouping; `HAVING` filters **groups** *after* aggregation. You cannot put `SUM()` in a `WHERE` — that is what `HAVING` is for.

### ORDER BY — sort the result

```sql
ORDER BY net_debit DESC   -- largest first
ORDER BY txn_date ASC, txn_id ASC   -- oldest first, tie-break by id
```

Add `LIMIT 10` (MySQL/Postgres) or `TOP 10` (SQL Server) to get the top N.

### Aggregate functions you'll use daily

`SUM()`, `COUNT(*)`, `COUNT(DISTINCT customer_id)`, `AVG()`, `MIN()`, `MAX()`. Wrap monthly grouping with a date-truncation function — dialect varies: Postgres `DATE_TRUNC('month', txn_date)`, MySQL `DATE_FORMAT(txn_date,'%Y-%m')`, SQL Server `FORMAT(txn_date,'yyyy-MM')`.

## Worked example / mini-project

**Goal: a debtor ageing summary by state for the quarter — the kind of MIS a finance analyst produces monthly.**

Setup (reproduce in any free SQL sandbox — SQLite via [sqliteonline.com](https://sqliteonline.com) needs no install):

```sql
CREATE TABLE invoices (
  inv_id INTEGER, customer_id TEXT, inv_date TEXT,
  due_date TEXT, amount REAL, status TEXT
);
INSERT INTO invoices VALUES
 (201,'C-01','2026-04-05','2026-05-05',118000,'OPEN'),
 (202,'C-02','2026-04-18','2026-05-18',236000,'OPEN'),
 (203,'C-01','2026-03-02','2026-04-01', 59000,'OPEN'),
 (204,'C-03','2026-05-10','2026-06-09',472000,'PAID'),
 (205,'C-02','2026-02-15','2026-03-17', 90000,'OPEN');

CREATE TABLE customers (customer_id TEXT, customer_name TEXT, state TEXT);
INSERT INTO customers VALUES
 ('C-01','Sharma Traders','Karnataka'),
 ('C-02','Nova Textiles','Maharashtra'),
 ('C-03','Delta Foods','Karnataka');
```

Now the ageing query. Assume "today" is 2026-06-30.

```sql
SELECT c.state,
       COUNT(*)              AS open_invoices,
       SUM(i.amount)         AS total_outstanding,
       SUM(CASE WHEN julianday('2026-06-30') - julianday(i.due_date) <= 30
                THEN i.amount ELSE 0 END) AS due_0_30,
       SUM(CASE WHEN julianday('2026-06-30') - julianday(i.due_date) > 30
                THEN i.amount ELSE 0 END) AS overdue_30_plus
FROM   invoices i
JOIN   customers c ON i.customer_id = c.customer_id
WHERE  i.status = 'OPEN'
GROUP BY c.state
ORDER BY total_outstanding DESC;
```

**Result:**

| state | open_invoices | total_outstanding | due_0_30 | overdue_30_plus |
|---|---|---|---|---|
| Maharashtra | 2 | 326000 | 236000 | 90000 |
| Karnataka | 2 | 177000 | 0 | 177000 |

In four clauses you filtered to open invoices (`WHERE`), attached the state (`JOIN`), bucketed the amounts (`CASE` inside `SUM`), rolled up by state (`GROUP BY`), and ranked by exposure (`ORDER BY`). That is a real deliverable, not a toy.

## How it's tested

Companies test SQL two ways.

**1. The live SQL screen (30–45 min, shared editor or HackerRank).** You get a schema and are asked to write queries against it. Typical prompts:

- "Return total sales per customer for FY26, highest first." (`JOIN` + `GROUP BY` + `ORDER BY`)
- "Find customers with more than 5 transactions but total spend under ₹10,000." (`GROUP BY` + `HAVING`)
- "List invoices with no matching payment." (`LEFT JOIN … IS NULL`)
- "What's the difference between `INNER` and `LEFT JOIN`? When would net totals differ?"
- "`WHERE` vs `HAVING` — why can't I filter `SUM()` in the `WHERE`?"

**2. The take-home / case.** A CSV or database dump plus a business question: "Reconcile this sub-ledger to the GL and list the mismatched accounts," or "Produce a monthly revenue trend." They're checking whether your number *ties* to a control total — accuracy over cleverness.

Interview verbal questions also probe: "What does `COUNT(*)` count vs `COUNT(column)`?" (the latter skips `NULL`s), and "Why did your `JOIN` inflate the total?" (a one-to-many join fanning out rows — a classic trap).

## Common mistakes & how pros avoid them

| Mistake | Symptom | Fix |
|---|---|---|
| Filtering an aggregate in `WHERE` | `SQL error: aggregate not allowed` | Move it to `HAVING`. |
| Double-counting from a one-to-many `JOIN` | SUM is too high, won't tie to TB | Aggregate first in a subquery, then join; or `COUNT(DISTINCT …)`. |
| `INNER JOIN` silently dropping rows | Total is *lower* than expected | Use `LEFT JOIN` when the right table may not match; then check for `NULL`. |
| Forgetting `NULL` logic | Rows with `NULL` vanish from `<>` filters | `NULL` is not equal to anything; use `IS NULL` / `COALESCE(col,0)`. |
| Ambiguous date strings | Wrong month pulled | Always `YYYY-MM-DD`; use half-open ranges `>= '2026-04-01' AND < '2026-05-01'`. |
| Non-aggregated column in `GROUP BY` | Error or wrong grouping | Every non-aggregated `SELECT` column must appear in `GROUP BY`. |
| Not sanity-checking | Wrong number ships to management | Always tie your `SUM` to a known control (trial balance, invoice register). |

Pros write the `WHERE` filter *first* and eyeball a few raw rows before they aggregate — you cannot trust a total you haven't spot-checked.

## Learn-it roadmap & resources

Realistic time to the finance-analyst bar (able to clear a SQL screen): **3–5 weeks at ~1 hour/day.** SQL rewards small daily reps on a real dataset far more than long theory sessions.

| Week | Focus |
|---|---|
| 1 | `SELECT`, `WHERE`, operators, `ORDER BY`, `LIMIT` |
| 2 | `JOIN` (inner/left), multi-table queries |
| 3 | `GROUP BY`, aggregates, `HAVING`, `CASE` |
| 4 | Subqueries, reconciliation-style problems, date handling |
| 5 | Timed practice on HackerRank/StrataScratch |

**Free:** SQLBolt (interactive, ~2 hrs to core), Mode Analytics SQL Tutorial (has an *Analytics* track with real business data), Kaggle "Intro to SQL", W3Schools (reference), sqliteonline.com (zero-install practice sandbox). **Practice with pressure:** HackerRank SQL track (what many screens are built on), LeetCode Database, StrataScratch (real finance/company questions).

**Paid / certification (optional, only if a JD asks):** Microsoft **PL-300 (Power BI Data Analyst)** includes SQL-adjacent skills; **Google Data Analytics Certificate** (Coursera) covers SQL for analysts. For finance roles in India, a certificate is rarely required — a clean take-home submission carries more weight.

## Quick-reference

```sql
SELECT col1, SUM(col2) AS total   -- pick columns / aggregate
FROM   table_a a
JOIN   table_b b ON a.key = b.key -- INNER: matches only
LEFT JOIN table_c c ON …          -- keep all left rows
WHERE  a.date >= '2026-04-01'     -- filter ROWS (before grouping)
  AND  a.amount > 50000
GROUP BY col1                     -- one output row per group
HAVING SUM(col2) > 100000         -- filter GROUPS (after aggregation)
ORDER BY total DESC               -- sort; ASC is default
LIMIT 10;                         -- top N (TOP 10 in SQL Server)
```

| Need | Clause / function |
|---|---|
| Filter rows | `WHERE` |
| Filter aggregated groups | `HAVING` |
| Text search | `LIKE '%text%'` |
| Match a list | `IN ('A','B')` |
| Range | `BETWEEN x AND y` |
| Missing values | `IS NULL`, `COALESCE(col,0)` |
| Count uniques | `COUNT(DISTINCT col)` |
| Bucketing (ageing) | `CASE WHEN … THEN … ELSE … END` |
| Find unmatched rows | `LEFT JOIN … WHERE right.key IS NULL` |
| Month grouping | `DATE_TRUNC` / `DATE_FORMAT` / `FORMAT` |

**Order of clauses (always):** `SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT`. **Order of execution (what actually runs):** `FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`. Knowing execution order explains why you can't reference a `SELECT` alias in `WHERE`, and why `HAVING` sees aggregates that `WHERE` can't.
