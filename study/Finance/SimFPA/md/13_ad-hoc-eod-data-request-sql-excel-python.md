# The "By EOD" Ad-Hoc Data Request

## The ask

It's **3:55pm on Tuesday, 21 July 2026**. You're heads-down on the Q2 forecast when the CFO stops at your desk on her way to a meeting:

> "Sales director thinks a few big accounts are eating our margin *and* paying late. Before I sit with him at 6, get me the **top 20 customers by gross margin**, and flag which ones are slow-paying. One page. By EOD."

No spec, no template, two hours. This is the bread-and-butter FP&A ad-hoc: pull it fast, get it *right*, present it in three lines the CFO can read walking into a room. You'll hit the ERP (SAP/Tally sits on a SQL database) directly, with Excel and Python as backups depending on where the data actually lives.

## What you're given

Three tables in the reporting database (read replica of the ERP):

**`sales`** — one row per invoice line:

| invoice_id | customer_id | invoice_date | revenue | cogs |
|---|---|---|---|---|
| INV-1001 | C-014 | 2026-04-12 | 4,20,000 | 3,15,000 |
| INV-1002 | C-003 | 2026-04-15 | 1,80,000 | 99,000 |
| ... | ... | ... | ... | ... |

**`customer`**:

| customer_id | customer_name | segment |
|---|---|---|
| C-014 | Deccan Switchgear | Goods |
| C-003 | Krishna AMC Corp | Services |

**`payments`** — settlements against invoices:

| invoice_id | paid_date | amount |
|---|---|---|
| INV-1001 | 2026-06-30 | 4,20,000 |

Company context: **DSO target 60 days**. Anything materially over 60 is "slow-paying." Total FY revenue reconciles to **Rs 12.00 cr**; blended gross margin **30%** — so any single customer far below 30% is a margin drag worth the CFO's attention.

## Build it — step by step

### The SQL query (primary route)

One statement: join the three tables, aggregate per customer, compute margin and average days-to-pay, rank, take the top 20 by *margin rupees*.

```sql
WITH cust AS (
    SELECT
        s.customer_id,
        c.customer_name,
        SUM(s.revenue)                        AS revenue,
        SUM(s.revenue - s.cogs)               AS gross_margin_rs,
        SUM(s.revenue - s.cogs) * 1.0
            / NULLIF(SUM(s.revenue), 0)        AS gm_pct,
        AVG( DATEDIFF(day, s.invoice_date, p.paid_date) ) AS avg_days_to_pay
    FROM sales s
    JOIN customer c  ON c.customer_id = s.customer_id
    LEFT JOIN payments p ON p.invoice_id = s.invoice_id   -- LEFT: unpaid still count
    GROUP BY s.customer_id, c.customer_name
)
SELECT
    RANK() OVER (ORDER BY gross_margin_rs DESC) AS rnk,
    customer_name,
    revenue,
    gross_margin_rs,
    ROUND(gm_pct * 100, 1)          AS gm_pct,
    ROUND(avg_days_to_pay, 0)       AS days_to_pay,
    CASE WHEN avg_days_to_pay > 60 THEN 'SLOW' ELSE 'OK' END AS pay_flag
FROM cust
ORDER BY gross_margin_rs DESC
LIMIT 20;                          -- SQL Server: use SELECT TOP 20 instead
```

The load-bearing bits:
- **`LEFT JOIN payments`** — an inner join would silently drop unpaid invoices, understating exposure. The slow-payers are exactly the ones you must not lose.
- **`NULLIF(SUM(revenue),0)`** — guards the margin division against a zero-revenue customer.
- **`RANK() OVER (ORDER BY gross_margin_rs DESC)`** — the window function does the ranking in-query; no eyeballing.
- Rank by **margin rupees**, not margin %, because the CFO cares about who moves the P&L — a 15% GM customer doing Rs 80 lakh matters more than a 60% GM customer doing Rs 2 lakh.
- Unpaid invoices push `avg_days_to_pay` up correctly only if you also treat NULL `paid_date` as "still open" — for a sharper version, `COALESCE(p.paid_date, CURRENT_DATE)` ages open invoices to today.

### The Excel PivotTable alternative

If the ERP only gives you a dumped invoice register (`.xlsx`), no SQL access:
1. Add helper columns on the raw sheet: `Margin = revenue - cogs`; `DaysToPay = paid_date - invoice_date` (blank → `=IF(paid_date="", TODAY()-invoice_date, paid_date-invoice_date)`).
2. PivotTable: **Rows** = customer_name; **Values** = Sum of Revenue, Sum of Margin, Average of DaysToPay.
3. Add a calculated **GM%** column next to the pivot: `=Margin / Revenue`.
4. Sort the pivot by Sum of Margin descending, **Top 20** via Value Filters → Top 10/20.
5. Flag column: `=IF(DaysToPay>60,"SLOW","OK")`, conditional-format SLOW red.

Equivalent single-cell pull without a pivot: `=SUMIFS(Margin, CustID, C-014)` and `=AVERAGEIFS(DaysToPay, CustID, C-014)`.

### The Python / pandas version (repeatable / big file)

When it's a recurring ask or the file is too big for Excel to be pleasant:

```python
import pandas as pd

sales    = pd.read_csv("sales.csv", parse_dates=["invoice_date"])
cust     = pd.read_csv("customer.csv")
pay      = pd.read_csv("payments.csv", parse_dates=["paid_date"])

df = (sales
      .merge(cust, on="customer_id", how="left")
      .merge(pay[["invoice_id", "paid_date"]], on="invoice_id", how="left"))

df["margin"] = df["revenue"] - df["cogs"]
df["days_to_pay"] = (df["paid_date"].fillna(pd.Timestamp("2026-07-21"))
                     - df["invoice_date"]).dt.days

g = (df.groupby("customer_name")
       .agg(revenue=("revenue", "sum"),
            margin=("margin", "sum"),
            days_to_pay=("days_to_pay", "mean"))
       .assign(gm_pct=lambda x: (x.margin / x.revenue * 100).round(1),
               pay_flag=lambda x: (x.days_to_pay > 60).map({True: "SLOW", False: "OK"}))
       .sort_values("margin", ascending=False)
       .head(20)
       .round({"days_to_pay": 0}))

g.to_excel("top20_margin.xlsx")
print(g)
```

Same logic as the SQL, in nine lines, and it re-runs next month by dropping in fresh CSVs.

## The deliverable

Top of a single page, the table (extract — top rows shown):

| Rank | Customer | Revenue (Rs) | Margin (Rs) | GM % | Days to pay | Flag |
|---|---|---|---:|---:|---:|---|
| 1 | Deccan Switchgear | 82,00,000 | 14,80,000 | 18.0% | 78 | SLOW |
| 2 | Godavari Controls | 61,50,000 | 24,60,000 | 40.0% | 44 | OK |
| 3 | Krishna AMC Corp | 55,00,000 | 24,75,000 | 45.0% | 52 | OK |
| 4 | Vijaya Electricals | 71,00,000 | 12,78,000 | 18.0% | 71 | SLOW |
| ... | ... | ... | ... | ... | ... | ... |

Then the **three lines** the CFO actually reads:

> - **Top 20 customers = ~Rs 9.1 cr revenue (76% of book), ~Rs 2.6 cr margin.** Concentrated book.
> - **Margin drag:** Deccan and Vijaya together do ~Rs 1.5 cr revenue at **18% GM** vs our 30% blend — biggest pull on blended margin.
> - **These same two are the slowest payers (78 & 71 days vs 60 target)** — high revenue, thin margin, *and* slow cash. That's the account to renegotiate first.

That last sentence is the whole value: the CFO walks into the 6pm meeting knowing not just the data but the *action*.

## How it's reviewed

- **Does the total tie?** Sum of all-customer margin should reconcile toward the 30% blended margin on Rs 12 cr; if your top-20 margin is implausibly high/low, a join fanned out or dropped rows.
- **Join integrity** — did a customer appear twice (duplicate in `customer`)? Did unpaid invoices vanish (inner join instead of left)?
- **Rank basis** — did you rank by margin Rs, as asked ("by margin"), not by revenue or GM%?
- **Slow-pay definition stated** — 60-day DSO target named on the page, so "SLOW" isn't arbitrary.
- **One page, plain English.** The CFO won't read the query; she reads the three lines.

## Common mistakes & red flags

- **Inner join on payments** dropping unpaid (the slowest) invoices — understates exposure, hides the very accounts asked about.
- **Ranking by GM%** — surfaces tiny high-margin accounts and buries the big margin-rupee drivers.
- **Averaging averages** — computing DSO per invoice then averaging the percentages instead of the days; average days-to-pay is fine, but never average an already-averaged ratio.
- **Divide-by-zero** on a credit-note-only customer (negative/zero revenue) — guard with NULLIF/`fillna`.
- **No reconciliation** — handing over a number that doesn't roll up to the Rs 12 cr / 30% anchors; always sanity-check the total.
- **Over-building** — a 40-line script when a PivotTable answers it in 10 minutes. Match the tool to a 2-hour deadline.

## On the job & in the interview

The "why": ad-hoc requests are ~30% of an FP&A analyst's week. The skill isn't just SQL — it's turning a vague question into the *right* cut, reconciling it, and compressing it to a decision. Jargon: **JOIN types, GROUP BY, window function (RANK/ROW_NUMBER), fan-out, DSO, margin concentration, the three-line summary.**

**Q: "You have a sales table and a payments table. How do you find slow-paying customers, and why LEFT JOIN?"**
A: "Left join sales to payments on invoice_id so unpaid invoices survive — they're precisely the slow/non-payers. Compute days-to-pay as paid_date minus invoice_date, coalescing NULL to today to age open items, group by customer, average it, and flag anything over our 60-day DSO target. An inner join would silently drop the worst offenders."

**Q: "Rank the top 20 by margin — SQL?"**
A: "Aggregate `SUM(revenue-cogs)` per customer in a CTE, then `RANK() OVER (ORDER BY margin DESC)` and take 20. I rank by margin rupees, not %, because the CFO cares about P&L impact — a big low-margin account outranks a tiny high-margin one."

**Q: "It's 4pm, due at 6. Excel or Python?"**
A: "For a one-off, whichever gets a correct, reconciled answer fastest — usually a PivotTable if I already have the dump. I'd only reach for Python/SQL if it's recurring or the file's too big for Excel. Speed and a clean tie-out beat elegance on a two-hour deadline."
