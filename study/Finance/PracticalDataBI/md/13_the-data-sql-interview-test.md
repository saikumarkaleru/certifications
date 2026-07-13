# The data/SQL interview & test

## What it is & where it's used

The SQL interview is the single most common practical filter between you and a data-touching finance job. Once a job description says "SQL", "data extraction", "pull your own numbers", or "self-serve analytics", assume there is a live or take-home SQL test — an MBA and a CA Intermediate do not exempt you from it.

Where it shows up:

| Role | What the SQL screen looks like |
|---|---|
| FP&A / Finance analyst | 3–5 questions on a sales/GL table, timed 30–45 min |
| Financial / Business analyst (fintech, e-comm) | Live shared editor, 45–60 min, joins + window functions |
| Revenue / Billing analyst | Take-home: reconcile invoices vs. payments |
| Data analyst (finance vertical) | HackerRank/Stratascratch style, 60–90 min |
| Audit analytics / Internal audit | Case: find duplicate vendors, split POs |

The bar is not "can you write a `SELECT *`". It is "can you turn a vague business question into a correct query, unaided, under time pressure, and explain it."

## The gap: why companies want this (and college didn't teach it)

College teaches you to *read* financial statements someone else prepared. The job is to *produce* the numbers from raw transactional tables — and those tables have nulls, duplicates, wrong data types, and 40 million rows. An MBA case study hands you a clean Exhibit 4; the real ERP hands you `sales_line_item` with `amount` stored as text and `INV-0001` sometimes typed `inv 0001`.

The specific gaps a SQL screen exposes:

- **Aggregation logic.** You know GROUP BY conceptually, but freeze on "revenue per customer *for their first month only*."
- **Joins under ambiguity.** LEFT vs INNER changes your revenue number. Getting this wrong = a wrong board deck.
- **Window functions.** Running totals, month-over-month growth, "top 3 per region", rank — never covered in a finance degree, asked in ~60% of screens.
- **Data hygiene instinct.** Pros check for duplicates and nulls *before* trusting a total. Freshers report the first number they get.

Companies test SQL because it is the cheapest reliable proxy for "can this person get the right number without hand-holding."

## What "proficient" looks like

The concrete, job-ready bar. You can, unaided:

1. Filter and aggregate: `WHERE`, `GROUP BY`, `HAVING`, `COUNT/SUM/AVG`.
2. Join 2–4 tables and *know* why you chose INNER vs LEFT.
3. Use `CASE WHEN` for bucketing and conditional sums.
4. Write window functions: `ROW_NUMBER`, `RANK`, `SUM() OVER`, `LAG/LEAD`.
5. Structure a query with CTEs (`WITH`) instead of nested subqueries.
6. Handle nulls (`COALESCE`), dedupe, and cast types.
7. Compute finance staples: MoM growth, running total, top-N-per-group, cohort/retention, churn.
8. Read a business question and translate it — the actual skill being tested.

If you can do 1–6 fluently and reason through 7–8 out loud, you pass most finance-adjacent screens.

## Hands-on: how to actually do it

Assume two tables:

```
customers(customer_id, name, city, signup_date)
orders(order_id, customer_id, order_date, amount, status)
```

**Filter + aggregate — revenue per city, paid orders only:**

```sql
SELECT c.city,
       SUM(o.amount)      AS total_revenue,
       COUNT(*)           AS num_orders
FROM   orders o
JOIN   customers c ON c.customer_id = o.customer_id
WHERE  o.status = 'PAID'
GROUP BY c.city
HAVING SUM(o.amount) > 100000
ORDER BY total_revenue DESC;
```

**Conditional aggregation (pivot without a pivot) — paid vs refunded per month:**

```sql
SELECT DATE_TRUNC('month', order_date) AS mth,
       SUM(CASE WHEN status='PAID'     THEN amount ELSE 0 END) AS paid,
       SUM(CASE WHEN status='REFUNDED' THEN amount ELSE 0 END) AS refunded
FROM   orders
GROUP BY 1
ORDER BY 1;
```

**LEFT JOIN to find the gap — customers who never ordered:**

```sql
SELECT c.customer_id, c.name
FROM   customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE  o.order_id IS NULL;
```

**Window function — running total and month-over-month growth:**

```sql
WITH monthly AS (
  SELECT DATE_TRUNC('month', order_date) AS mth,
         SUM(amount) AS revenue
  FROM   orders
  WHERE  status = 'PAID'
  GROUP BY 1
)
SELECT mth,
       revenue,
       SUM(revenue) OVER (ORDER BY mth)                 AS running_total,
       revenue - LAG(revenue) OVER (ORDER BY mth)       AS mom_change,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY mth))
             / LAG(revenue) OVER (ORDER BY mth), 1)      AS mom_pct
FROM   monthly
ORDER BY mth;
```

**Top-N per group — top 2 customers by spend in each city:**

```sql
WITH ranked AS (
  SELECT c.city, c.name,
         SUM(o.amount) AS spend,
         ROW_NUMBER() OVER (PARTITION BY c.city
                            ORDER BY SUM(o.amount) DESC) AS rn
  FROM   orders o
  JOIN   customers c ON c.customer_id = o.customer_id
  GROUP BY c.city, c.name
)
SELECT city, name, spend FROM ranked WHERE rn <= 2;
```

**Data hygiene — the check pros run first:**

```sql
-- duplicate orders?
SELECT order_id, COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*) > 1;
-- nulls hiding in the money column?
SELECT COUNT(*) FROM orders WHERE amount IS NULL;
```

## Worked example / mini-project

**Case (India e-commerce, reproduce this locally):** "Give me GST-inclusive net revenue by month for FY2024-25, the MoM growth, and flag any month where refunds exceeded 5% of gross."

Seed data (paste into SQLite / Postgres):

```sql
CREATE TABLE orders(order_id INT, customer_id INT, order_date DATE,
                    amount NUMERIC, status TEXT);
INSERT INTO orders VALUES
(1,101,'2024-04-05', 50000,'PAID'),
(2,102,'2024-04-18', 30000,'PAID'),
(3,103,'2024-04-22', 12000,'REFUNDED'),
(4,101,'2024-05-10', 80000,'PAID'),
(5,104,'2024-05-15', 20000,'PAID'),
(6,105,'2024-05-27', 60000,'REFUNDED'),
(7,102,'2024-06-02', 90000,'PAID'),
(8,103,'2024-06-19',  5000,'REFUNDED');
```

Amounts are GST-inclusive at 18%. Solution:

```sql
WITH m AS (
  SELECT DATE_TRUNC('month', order_date) AS mth,
         SUM(CASE WHEN status='PAID' THEN amount ELSE 0 END)     AS gross_paid,
         SUM(CASE WHEN status='REFUNDED' THEN amount ELSE 0 END) AS refunds
  FROM orders
  GROUP BY 1
)
SELECT mth,
       gross_paid,
       ROUND(gross_paid / 1.18, 0)                       AS net_ex_gst,
       ROUND(gross_paid - gross_paid/1.18, 0)            AS gst_component,
       ROUND(gross_paid - LAG(gross_paid) OVER (ORDER BY mth), 0) AS mom_change,
       CASE WHEN refunds > 0.05 * (gross_paid + refunds)
            THEN 'FLAG' ELSE 'OK' END                    AS refund_flag
FROM m
ORDER BY mth;
```

Expected reading: April gross ₹80,000 (net ₹67,797, GST ₹12,203), May ₹100,000 (MoM +₹20,000) but refunds ₹60,000 vs gross ₹100,000 → **FLAG** (>5%). Being able to *narrate* that last line — "May looks great on revenue but refund rate is 37%, so I'd investigate before reporting growth" — is what gets you the offer.

## How it's tested

**Format you'll actually face:**

| Type | Detail |
|---|---|
| Live shared editor | Zoom + DB Fiddle / CoderPad; 3–4 questions, 45 min, they watch you think |
| Timed platform | HackerRank / StrataScratch / DataLemur; auto-graded, 60–90 min |
| Take-home | A CSV + "answer these 5 business questions", 24–48 hr |
| Verbal-only | Whiteboard/no-run; they judge structure, not exact syntax |

**Questions that recur:**

- "Second-highest salary / order value." (Tests window functions or subquery.)
- "Customers who ordered in Jan but not Feb." (Anti-join / `NOT IN` / `EXCEPT`.)
- "Difference between `WHERE` and `HAVING`; `INNER` vs `LEFT JOIN`." (Verbal.)
- "MoM revenue growth %." (Window + `LAG`.)
- "Top 3 products per category." (`ROW_NUMBER` + `PARTITION BY`.)
- "Deduplicate this table keeping the latest row." (`ROW_NUMBER()` then `WHERE rn=1`.)
- "How would you check this number is right?" (The hygiene answer — most freshers miss it.)

**How they grade:** correctness first, then whether you clarified assumptions, then readability (CTEs > nested subqueries), then that you sanity-checked the output.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Diving into SQL before understanding the question | Restate it: "So 'active customer' means ordered in last 30 days?" — always clarify first |
| Using `INNER JOIN` when the question needs unmatched rows | If the ask is "who *didn't*", it's a `LEFT JOIN … IS NULL` or `EXCEPT` |
| `COUNT(*)` vs `COUNT(column)` confusion | `COUNT(col)` ignores nulls; know which you mean |
| Filtering on an aggregate in `WHERE` | Aggregate conditions go in `HAVING`, not `WHERE` |
| Nulls silently breaking sums/joins | `COALESCE(amount,0)`; check `IS NULL` early |
| Wrong grain → double counting after a join | Aggregate before joining, or check for fan-out with a row count |
| Reporting the first number without checking | Run the dedupe + null check first; state "I verified no dupes" |
| Nested subquery spaghetti | Use `WITH` CTEs — readable and graders reward it |
| Integer division (`1/2 = 0`) | Multiply by `100.0` or cast for percentages |

## Learn-it roadmap & resources

Realistic time-to-proficiency from zero, part-time: **4–6 weeks** to pass most finance screens.

| Week | Focus |
|---|---|
| 1 | SELECT/WHERE/GROUP BY/ORDER BY/HAVING — SQLBolt (free, ~4 hrs) |
| 2 | Joins (all types), CASE, subqueries — Mode SQL Tutorial (free) |
| 3 | Window functions + CTEs — the part that actually differentiates you |
| 4 | Drill interview questions — DataLemur (free tier), StrataScratch |
| 5–6 | Timed mocks + one take-home; build the mini-project above in SQLite |

Resources:

- **Free:** SQLBolt, Mode Analytics SQL Tutorial, DataLemur (Nick Singh, finance-heavy), PostgreSQL Tutorial, LeetCode Database (50 problems).
- **Practice envs:** DB Fiddle, sqliteonline.com — zero install, paste and run.
- **Paid (optional):** StrataScratch (~$30/mo, real company questions), "Ace the Data Science Interview" book.
- **Certification:** not required and rarely asked for in finance roles — a GitHub repo with 3 solved case queries beats a certificate. If you want one, Google Data Analytics (Coursera) or Microsoft DP-900 signal basics.

Install SQLite locally (`sqlite3`, ships free) and reproduce every query above — running beats reading.

## Quick-reference

```sql
-- Skeleton
SELECT col, AGG(x) FROM t
JOIN t2 ON t.id=t2.id
WHERE  filter_rows
GROUP BY col
HAVING AGG(x) > n            -- filter on aggregate
ORDER BY col LIMIT k;

-- Window
ROW_NUMBER() OVER (PARTITION BY g ORDER BY x DESC)  -- top-N per group
SUM(x)     OVER (ORDER BY d)                        -- running total
LAG(x)     OVER (ORDER BY d)                        -- prev row → MoM
RANK() / DENSE_RANK()                               -- ties handling

-- Patterns
COALESCE(x,0)                       -- null-safe
LEFT JOIN … WHERE b.id IS NULL      -- anti-join ("didn't")
A EXCEPT B                          -- rows in A not in B
100.0 * a / b                       -- avoid integer division
WITH cte AS (…) SELECT … FROM cte   -- readable > nested
```

| Question type | Weapon |
|---|---|
| Top-N per group | `ROW_NUMBER() … PARTITION BY` |
| MoM / running total | `LAG` / `SUM() OVER` |
| "Who didn't…" | LEFT JOIN … IS NULL / `EXCEPT` |
| Nth highest | window or correlated subquery |
| Pivot | `SUM(CASE WHEN …)` |
| Dedupe | `ROW_NUMBER()`, keep `rn=1` |

**Golden rule:** clarify the question → check the data → write the CTE → sanity-check the number → explain it out loud.
