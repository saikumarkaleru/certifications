# SQL for Finance: Practical Queries

## What it is & where it's used

SQL (Structured Query Language) is how you ask a database questions. In finance, the "database" is where the real numbers live — the general ledger, the sales/AR sub-ledger, the payments table, the customer master — usually in PostgreSQL, MySQL, SQL Server, Snowflake, or BigQuery. Excel breaks past ~1 million rows and gets slow at 100k; SQL joins 50 million rows of transactions to a customer table in seconds and never silently corrupts a VLOOKUP.

Roles that live in SQL every day:

| Role | What they query |
|---|---|
| FP&A / Finance analyst | Revenue trends, budget vs actual, cohort retention |
| Revenue / Billing analyst | MRR/ARR, churn, invoicing accuracy |
| Accounts / AR-AP analyst | Ageing buckets, unapplied cash, reconciliations |
| Internal audit / controls | Duplicate payments, journal anomalies, three-way match |
| Data/BI analyst supporting finance | The pipelines feeding Power BI/Tableau |

In Indian startups, fintechs, and GCCs (Global Capability Centres in Bengaluru/Hyderabad/Pune), "SQL is required" appears on almost every finance-analyst JD above fresher level. It is the single highest-leverage non-accounting skill a CA-track candidate can add.

## The gap: why companies want this (and college didn't teach it)

An MBA Finance / CA syllabus teaches you *what* a revenue figure means, how to age receivables, and the accounting behind a reconciliation. It never shows you that in a real company those numbers sit in a `transactions` table with 8 million rows and you are expected to produce them yourself, unaided, by lunchtime.

The specific gap:
- **You know the concept of ageing; you've never written the query that buckets 40,000 open invoices.** College gave you a 10-row textbook example. Work gives you a raw table and a deadline.
- **You've reconciled two statements by hand in Excel.** Nobody told you `FULL OUTER JOIN` does the same match for a million rows and flags every break automatically.
- **You think of data as a finished report.** Employers think of it as rows you filter, join, and aggregate on demand.

Closing this gap means you stop asking the data team for extracts and start answering your own questions — which is exactly what makes an analyst "senior."

## What "proficient" looks like

The bar employers actually test:

1. **You can `JOIN` two or three tables** (invoices to customers to payments) without producing duplicate rows, and you know *why* an inner vs left join changes the answer.
2. **You use `GROUP BY` with `HAVING`** to aggregate and filter aggregates (e.g. customers with total billing > ₹10 lakh).
3. **You write window functions** — `SUM() OVER`, `RANK()`, `LAG()` — for running totals, rankings, and month-on-month growth.
4. **You structure a multi-step query with CTEs** (`WITH`) instead of nesting subqueries five deep.
5. **You handle dates** — truncate to month, compute ageing days, filter a fiscal year.
6. **You reconcile** two sources with a `FULL OUTER JOIN` and isolate the breaks.

If you can do those six unaided on an unfamiliar schema, you pass 90% of finance SQL screens.

## Hands-on: how to actually do it

Assume this schema (typical AR/revenue setup):

```
customers(customer_id, customer_name, segment, region)
invoices(invoice_id, customer_id, invoice_date, due_date, amount, status)
payments(payment_id, invoice_id, payment_date, amount_paid)
```

**Filtering and aggregating — revenue by month:**

```sql
SELECT DATE_TRUNC('month', invoice_date) AS month,
       SUM(amount)                        AS revenue,
       COUNT(*)                           AS num_invoices
FROM   invoices
WHERE  status <> 'cancelled'
GROUP  BY DATE_TRUNC('month', invoice_date)
ORDER  BY month;
```

**Joins — revenue by region (invoices + customers):**

```sql
SELECT c.region,
       SUM(i.amount) AS revenue
FROM   invoices i
JOIN   customers c ON c.customer_id = i.customer_id
GROUP  BY c.region
ORDER  BY revenue DESC;
```

**Window function — running (cumulative) total of revenue by month:**

```sql
SELECT month,
       revenue,
       SUM(revenue) OVER (ORDER BY month
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
                    AS running_total
FROM (
    SELECT DATE_TRUNC('month', invoice_date) AS month,
           SUM(amount)                        AS revenue
    FROM   invoices
    GROUP  BY 1
) m
ORDER BY month;
```

**Window function — rank top customers, and month-on-month growth with `LAG`:**

```sql
-- Top 5 customers by billing
SELECT customer_id,
       SUM(amount) AS total_billed,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS rnk
FROM   invoices
GROUP  BY customer_id
QUALIFY rnk <= 5;          -- Snowflake/BigQuery; else wrap in a subquery
```

```sql
-- Month-on-month % growth
SELECT month,
       revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / LAG(revenue) OVER (ORDER BY month), 1) AS growth_pct
FROM   monthly_rev;
```

**CTEs — chaining steps readably:**

```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', invoice_date) AS month,
           SUM(amount) AS revenue
    FROM   invoices
    GROUP  BY 1
),
with_growth AS (
    SELECT month, revenue,
           revenue - LAG(revenue) OVER (ORDER BY month) AS mom_change
    FROM   monthly
)
SELECT * FROM with_growth WHERE mom_change < 0;   -- months that declined
```

**Date logic — AR ageing buckets:**

```sql
SELECT i.invoice_id, c.customer_name, i.amount,
       CURRENT_DATE - i.due_date AS days_overdue,
       CASE
         WHEN CURRENT_DATE - i.due_date <= 0   THEN 'Not due'
         WHEN CURRENT_DATE - i.due_date <= 30  THEN '0-30'
         WHEN CURRENT_DATE - i.due_date <= 60  THEN '31-60'
         WHEN CURRENT_DATE - i.due_date <= 90  THEN '61-90'
         ELSE '90+'
       END AS bucket
FROM   invoices i
JOIN   customers c ON c.customer_id = i.customer_id
WHERE  i.status = 'open';
```

**Reconciliation — match GL to bank/sub-ledger and find breaks:**

```sql
SELECT COALESCE(g.txn_id, b.txn_id) AS txn_id,
       g.amount AS gl_amount,
       b.amount AS bank_amount,
       CASE
         WHEN b.txn_id IS NULL THEN 'Missing in bank'
         WHEN g.txn_id IS NULL THEN 'Missing in GL'
         WHEN g.amount <> b.amount THEN 'Amount mismatch'
       END AS break_type
FROM   gl g
FULL OUTER JOIN bank b ON g.txn_id = b.txn_id
WHERE  g.txn_id IS NULL
   OR  b.txn_id IS NULL
   OR  g.amount <> b.amount;
```

## Worked example / mini-project

**Scenario:** You're the FP&A analyst at an Indian SaaS company. Build a monthly-cohort retention view — do customers acquired in a given month keep paying?

Sample `invoices` data (₹, one row per customer-month):

| customer_id | invoice_date | amount |
|---|---|---|
| 1 | 2025-01-15 | 5,000 |
| 1 | 2025-02-15 | 5,000 |
| 1 | 2025-03-15 | 5,000 |
| 2 | 2025-01-20 | 8,000 |
| 2 | 2025-02-20 | 8,000 |
| 3 | 2025-02-10 | 3,000 |

**Step 1 — find each customer's cohort (first billing month):**

```sql
WITH cohort AS (
    SELECT customer_id,
           MIN(DATE_TRUNC('month', invoice_date)) AS cohort_month
    FROM   invoices
    GROUP  BY customer_id
),
activity AS (
    SELECT i.customer_id,
           c.cohort_month,
           DATE_TRUNC('month', i.invoice_date) AS active_month
    FROM   invoices i
    JOIN   cohort c ON c.customer_id = i.customer_id
)
SELECT cohort_month,
       -- months since acquisition (0, 1, 2 ...)
       (EXTRACT(YEAR FROM active_month) - EXTRACT(YEAR FROM cohort_month)) * 12
        + (EXTRACT(MONTH FROM active_month) - EXTRACT(MONTH FROM cohort_month)) AS month_offset,
       COUNT(DISTINCT customer_id) AS active_customers,
       SUM(1) AS billings_count
FROM   activity
GROUP  BY cohort_month, month_offset
ORDER  BY cohort_month, month_offset;
```

**Result (retention triangle):**

| cohort_month | month_offset | active_customers |
|---|---|---|
| 2025-01 | 0 | 2 |
| 2025-01 | 1 | 2 |
| 2025-01 | 2 | 1 |
| 2025-02 | 0 | 1 |

Read it: the Jan cohort started with 2 customers, both stayed in month 1, one dropped by month 2 (50% retention). That single query — cohort CTE + offset date math + `COUNT(DISTINCT)` — is exactly the deliverable a startup finance team calls "the retention curve." Reproduce it locally with any free SQLite/PostgreSQL install and the six rows above.

## How it's tested

Companies test SQL far more concretely than accounting:

**The live SQL screen (most common).** You share screen on HackerRank / DataLemur / a scratch database and solve 3-5 problems in 45 minutes. Typical prompts:
- "Return the top 3 customers by revenue per region." (window function `RANK()` partitioned by region)
- "Show month-on-month revenue growth %." (`LAG`)
- "Bucket these open invoices into ageing bands." (`CASE` + date math)
- "Find invoices with no matching payment." (`LEFT JOIN … WHERE payments.id IS NULL`)

**Take-home case.** "Here's a CSV of 20k transactions — build the AR ageing report and list the 10 largest overdue balances." They check whether your joins double-count and whether your buckets are right at the boundaries.

**Conceptual interview questions:**
- Difference between `WHERE` and `HAVING`? (row filter vs group filter)
- `INNER` vs `LEFT` vs `FULL OUTER JOIN` — when does each change a reconciliation result?
- What does a window function do that `GROUP BY` cannot? (keeps every row while adding an aggregate)
- Why is `COUNT(*)` different from `COUNT(column)`? (the latter ignores NULLs)

## Common mistakes & how pros avoid them

| Mistake | Why it hurts | Pro habit |
|---|---|---|
| Joins that fan out rows | Summing a customer's invoices *after* joining to multiple payments doubles revenue | Aggregate each side in a CTE *before* joining, or join on a unique key |
| Filtering a `LEFT JOIN` in `WHERE` | `WHERE b.col = x` silently turns it back into an inner join and hides the breaks | Put the condition in the `ON`, or filter for `IS NULL` |
| Ageing boundary errors | `<= 30` and `>= 30` both include day 30 → double-count | Use clean `<= 30` then `<= 60`, never overlapping ranges |
| `SELECT *` on a huge table | Pulls 40 columns you don't need, slow and unreadable | Select only the columns you'll use |
| Ignoring NULLs in reconciliation | A NULL amount silently drops from `SUM` or a `=` comparison | `COALESCE(amount,0)`; test `IS NULL` explicitly |
| Trusting `GROUP BY` without checking counts | You never notice the join fanned out | Sanity-check: does total match the known control figure? |
| Rounding currency mid-query | Compounds paise-level errors | Round once, at the final SELECT |

## Learn-it roadmap & resources

Realistic time-to-proficiency for a finance person who already knows Excel: **6-8 weeks, ~45 min/day.**

| Week | Focus |
|---|---|
| 1 | SELECT, WHERE, ORDER BY, basic aggregates |
| 2 | GROUP BY, HAVING, the join types |
| 3 | CTEs (`WITH`), subqueries |
| 4 | Window functions — the finance sweet spot |
| 5 | Date functions, `CASE`, ageing/cohort patterns |
| 6-8 | Timed practice on real finance-style problems |

**Free:**
- **SQLBolt** and **Mode SQL Tutorial** — interactive, browser-based, start here.
- **DataLemur** (Ambitious with SQL) — window-function and analytics problems, many finance-flavoured.
- **PostgreSQL** + **DBeaver**, both free — install locally and load your own CSVs.
- **StrataScratch** free tier — real company-style questions.

**Paid / certification:**
- **Google Data Analytics Professional Certificate** (Coursera) — includes SQL, recruiter-recognised in India.
- **Microsoft PL-300 / DP-900** if you're pairing SQL with Power BI/Azure.
- **HackerRank SQL (Intermediate/Advanced) badge** — free to earn, cheap signal to put on a CV.

For a CA-track candidate, SQL + Power BI is the combination that moves you from "accounts executive" to "finance analyst" pay bands.

## Quick-reference

```sql
-- Month truncation
DATE_TRUNC('month', d)              -- Postgres
DATE_FORMAT(d,'%Y-%m-01')           -- MySQL
FORMAT(d,'yyyy-MM')                 -- SQL Server

-- Days overdue
CURRENT_DATE - due_date             -- Postgres
DATEDIFF(day, due_date, GETDATE())  -- SQL Server
```

| Need | Pattern |
|---|---|
| Running total | `SUM(x) OVER (ORDER BY d ROWS UNBOUNDED PRECEDING)` |
| Rank | `RANK() OVER (PARTITION BY region ORDER BY sales DESC)` |
| Prev period | `LAG(x) OVER (ORDER BY month)` |
| Next period | `LEAD(x) OVER (ORDER BY month)` |
| Multi-step query | `WITH cte1 AS (...), cte2 AS (...) SELECT ...` |
| Ageing bucket | `CASE WHEN days<=30 THEN '0-30' ... END` |
| Unmatched rows | `LEFT JOIN ... WHERE b.id IS NULL` |
| Full reconciliation | `FULL OUTER JOIN ... WHERE a.id IS NULL OR b.id IS NULL OR a.amt<>b.amt` |
| Filter aggregates | `GROUP BY ... HAVING SUM(x) > 1000000` |
| Distinct count | `COUNT(DISTINCT customer_id)` |

**Order of execution to remember:** `FROM → JOIN → WHERE → GROUP BY → HAVING → window functions → SELECT → ORDER BY → LIMIT`. Knowing this explains why you can't reference a `SELECT` alias in `WHERE` but can in `ORDER BY`.
