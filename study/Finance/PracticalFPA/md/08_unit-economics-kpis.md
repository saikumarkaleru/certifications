# Unit Economics, KPIs & Metrics

## What it is & where it's used

**Unit economics** is the profit-and-loss of a *single unit* — one customer, one order, one subscription, one delivery — stripped of company-wide noise. If you can't make money on one unit, scaling only makes you lose money faster. **KPIs and metrics** are the small set of numbers that tell you whether that unit is healthy and whether the business is on track.

This is the language of modern FP&A. It shows up in:

- **FP&A / business finance** — building the operating model, board decks, and "burn multiple" narratives.
- **Startup / SaaS / D2C finance** — CAC, LTV, payback, cohort retention, contribution margin per order.
- **Strategy & investor relations** — same metrics translated for VCs and lenders.
- **Corporate FP&A in traditional firms** — contribution margin by SKU/region, gross margin bridges.

Anyone touching a **board deck, a fundraise model, or a "why are we burning cash" review** lives in this chapter. In India, every funded startup (Zomato, Meesho, Nykaa, a Series-A SaaS firm) reports these numbers — and every finance hire is expected to compute and defend them.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you the **income statement top-down**: Revenue → COGS → Gross Profit → EBITDA. That's an *accounting* view. It tells you the company made ₹X, not whether the *next customer* is worth acquiring.

The industry works **bottom-up and forward-looking**:

| College taught | Industry needs |
|---|---|
| Gross margin % for the whole firm | Contribution margin **per unit**, after variable selling/logistics |
| Historical P&L | LTV — *future* value of a customer you just acquired |
| "Marketing is an expense" | CAC as an **investment** with a payback period |
| Revenue growth | Retention, cohorts, and *quality* of that growth |
| One blended number | Metrics **by business model** (SaaS ≠ D2C ≠ marketplace) |

The gap: colleges teach financial *accounting* and static ratio analysis. Employers need you to model the *economics of growth* — connect a marketing spend today to a cash return 14 months later, and prove the business gets *more* efficient as it scales, not less. Nobody teaches cohort analysis or the CAC payback formula in a classroom.

## What "proficient" looks like

A job-ready person can, unaided:

1. Build a **contribution margin** waterfall for a unit and name every variable cost line.
2. Compute **CAC** correctly (fully-loaded, not just ad spend) and **LTV** three different ways.
3. State the **LTV:CAC** and **payback** rules of thumb and explain *why* they matter for cash.
4. Build a **cohort retention table** in Excel/SQL and read revenue retention (NRR/GRR) off it.
5. Pick the **right KPIs for the business model** in front of them and defend the choice.
6. Spot when a metric is being **gamed** (blended CAC hiding paid CAC, LTV using revenue not margin).

The bar is not memorising formulas — it's judgement about *which* number is honest.

## Hands-on: how to actually do it

### Contribution margin (per unit)

Contribution margin = Revenue − **variable** costs. Fixed costs (rent, salaries, tools) are excluded.

```
Contribution Margin (CM1) = Net Revenue − COGS − variable selling/logistics
CM per unit               = CM1 / units
CM %                      = CM1 / Net Revenue
Breakeven units           = Fixed Costs / CM per unit
```

Excel for a D2C order:

```
Net revenue      =  B2 - B3                         'AOV minus discount
COGS             =  B4
Contribution     =  B2 - B3 - B4 - B5 - B6 - B7     'less shipping, payment gateway, returns provision
CM %             =  (B2-B3-B4-B5-B6-B7) / (B2-B3)
Breakeven units  =  Fixed_Costs / Contribution_per_unit
```

### CAC — Customer Acquisition Cost

```
CAC = (Total Sales + Marketing spend, fully loaded) / New customers acquired
```

Fully loaded = ad spend + salaries of the sales/marketing team + tools + agency fees + attributed discounts/coupons. **Blended CAC** divides by *all* new customers (incl. organic). **Paid CAC** divides by only paid-channel customers — always higher, always the honest one.

```
Blended CAC = 12,00,000 / 4,000 = ₹300
Paid CAC    = 12,00,000 / 2,000 = ₹600   ← the number a VC will ask for
```

### LTV — Lifetime Value (three ways)

```
1. Simple:        LTV = ARPU × Gross Margin% × Avg customer lifespan (in periods)
2. Churn-based:   LTV = (ARPU × Gross Margin%) / Monthly churn rate
3. Discounted:    LTV = Σ  [ margin_t / (1+r)^t ]   over expected life
```

Rule: **always use margin, never revenue.** LTV on revenue overstates value by (1 − margin).

```
ARPU (monthly)      = ₹500
Gross margin        = 70%   →  contribution ARPU = ₹350
Monthly churn       = 5%    →  avg life = 1/0.05 = 20 months
LTV (churn method)  = 350 / 0.05 = ₹7,000
LTV:CAC             = 7,000 / 600 = 11.7x
```

### Payback period

```
CAC Payback (months) = CAC / (monthly contribution margin per customer)
                     = 600 / 350 = 1.7 months
```

### SQL — cohort retention

```sql
WITH first_order AS (
  SELECT customer_id,
         DATE_TRUNC('month', MIN(order_date)) AS cohort_month
  FROM orders
  GROUP BY customer_id
),
activity AS (
  SELECT o.customer_id,
         f.cohort_month,
         DATE_TRUNC('month', o.order_date) AS active_month,
         SUM(o.net_revenue) AS revenue
  FROM orders o
  JOIN first_order f ON o.customer_id = f.customer_id
  GROUP BY 1,2,3
)
SELECT cohort_month,
       DATEDIFF('month', cohort_month, active_month) AS month_index,
       COUNT(DISTINCT customer_id) AS active_customers,
       SUM(revenue) AS cohort_revenue
FROM activity
GROUP BY 1,2
ORDER BY 1,2;
```

### Python — churn and LTV from the cohort table

```python
import pandas as pd

df = pd.read_csv("cohorts.csv")  # cohort_month, month_index, active_customers
pivot = df.pivot(index="cohort_month", columns="month_index",
                 values="active_customers")

# Retention % = each month vs month 0
retention = pivot.div(pivot[0], axis=0)

# Monthly churn implied by month 1 retention
churn = 1 - retention[1].mean()
arpu, gm = 500, 0.70
ltv = (arpu * gm) / churn
print(f"Avg monthly churn: {churn:.1%}  |  LTV: Rs {ltv:,.0f}")
```

### DAX — Net Revenue Retention in Power BI

```
NRR :=
VAR StartRev = CALCULATE([Revenue], DATEADD('Date'[Date], -12, MONTH))
RETURN DIVIDE([Revenue], StartRev)   -- >100% = expansion beats churn
```

## Worked example / mini-project

**"Kirana Cloud" — a B2B SaaS billing app for Indian retail shops.** Reproduce this in Excel.

Inputs (monthly, per customer):

| Item | Value |
|---|---|
| Subscription (ARPU) | ₹1,500 |
| Gross margin | 80% → contribution ARPU ₹1,200 |
| Monthly logo churn | 4% |
| Fully-loaded S&M / month | ₹8,00,000 |
| New paying customers / month | 100 |

Step-by-step:

```
CAC            = 8,00,000 / 100                = ₹8,000
Avg lifespan   = 1 / 0.04                      = 25 months
LTV            = 1,200 × 25                     = ₹30,000
LTV:CAC        = 30,000 / 8,000                = 3.75x     ✅ (>3 healthy)
CAC payback    = 8,000 / 1,200                 = 6.7 months ✅ (<12 healthy)
Annual GRR     = (1 − 0.04)^12                 = 61%       ⚠️ churn too high
```

**The catch a good analyst spots:** LTV:CAC looks fine (3.75x), but **61% gross retention means 39% of customers gone within a year** — the LTV is propped up by a long theoretical tail. Fix churn before scaling spend. This is exactly the kind of "the headline metric hides the problem" insight FP&A gets hired for.

Now add **NRR**: if surviving customers upgrade seats and expansion adds 8% while churn removes 4%, NRR = 104% — the business grows revenue even with zero new logos. That single number reframes the entire investment case.

Build it: one sheet with the input block, one CAC/LTV/payback block, and a 12-column cohort retention grid using `=B0*(1-churn)^col`. Add conditional formatting (green >100% NRR, red <90% GRR).

## How it's tested

**Interview questions:**

- "Walk me through CAC and LTV. What's a good LTV:CAC ratio and why 3x?"
- "Difference between blended and paid CAC? Which would a founder quote to look good?"
- "Company has LTV:CAC of 5x but is burning cash. How?" (Answer: long payback — cash out now, LTV realised over years.)
- "What KPIs matter for a marketplace vs a SaaS vs a D2C brand?"
- "GRR vs NRR — which can exceed 100% and why?"

**Practical / take-home tests:**

1. **Timed Excel case (45–60 min):** raw orders table given → build contribution margin, CAC, LTV, payback, and a cohort retention grid with conditional formatting.
2. **SQL screen:** "Write a cohort retention query from this `orders` table" (the query above is the expected answer).
3. **Metrics-audit case:** a deck with inflated numbers → "find what's wrong." Expected catches: LTV on revenue not margin, blended CAC hiding paid CAC, churn understated by counting only voluntary churn.
4. **Board-deck build:** given a P&L, produce the 6 KPIs that matter and a one-line narrative each.

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| LTV computed on **revenue**, not gross margin | Always multiply ARPU by GM% first |
| Quoting **blended CAC** to hide expensive paid channels | Report paid CAC separately; segment by channel |
| Ignoring **CAC payback** — a 5x LTV:CAC with 30-month payback still kills cash | Show payback alongside the ratio |
| Putting **fixed costs** into contribution margin | CM uses variable costs only |
| Assuming churn is constant | Early cohorts churn faster; use the cohort curve, not one rate |
| Using **one KPI set** for every business | Match KPIs to model (see cheat-sheet) |
| Counting a cancelled-then-resubscribed user as retained | Define churn rules explicitly and document them |
| LTV with **infinite lifespan** on high churn | Cap horizon (e.g., 36 months) or discount future margin |

Pros write down every definition (a "metrics dictionary") so nobody argues about what "active customer" means at month-end.

## Learn-it roadmap & resources

**Time to proficiency: 3–5 weeks part-time.**

- **Week 1** — Contribution margin, CAC, LTV, payback. Rebuild the worked example from scratch in Excel.
- **Week 2** — Cohort analysis in Excel, then reproduce it in SQL.
- **Week 3** — Business-model KPIs; read 3 real investor decks (Zomato, Nykaa, a SaaS S-1) and recompute their metrics.
- **Week 4–5** — Python/DAX automation of a cohort report; build a KPI dashboard.

**Resources (mostly free):**

- *For Entrepreneurs* (David Skok) — the canonical SaaS metrics essays. Free.
- a16z & Bessemer "Cloud metrics" primers — free, investor-grade definitions.
- Zomato / Nykaa investor presentations (India context) — free on their IR pages.
- *Financial Intelligence* (Berman & Knight) — margin thinking. Paid.
- Practice data: Kaggle "Online Retail" and "Telco Churn" datasets — build cohorts on real rows.
- **Certification:** none required specifically, but **FMVA (CFI)** and **Wall Street Prep** cover this inside their FP&A tracks. For most India roles, a strong Excel + SQL portfolio project beats a certificate.

## Quick-reference

**Formulas:**

| Metric | Formula | Healthy |
|---|---|---|
| Contribution margin | Revenue − variable costs | > 0, ideally 30%+ |
| CAC (paid) | Fully-loaded S&M / paid customers | model-dependent |
| LTV | (ARPU × GM%) / churn | — |
| LTV:CAC | LTV / CAC | **3–5x** |
| CAC payback | CAC / monthly contribution/customer | **< 12 months** |
| GRR | 1 − revenue churn | > 90% (SaaS) |
| NRR | (Start + expansion − churn) / Start | **> 100%** |
| Rule of 40 (SaaS) | Growth% + Profit margin% | ≥ 40 |
| Burn multiple | Net burn / Net new ARR | < 1 great, > 2 poor |

**KPIs by business model:**

| Model | The metrics that matter |
|---|---|
| **SaaS** | MRR/ARR, NRR, GRR, logo churn, CAC payback, Rule of 40, magic number |
| **D2C / e-commerce** | AOV, contribution margin/order, repeat rate, RTO %, blended vs paid CAC, cohort repeat |
| **Marketplace** | GMV, take rate, contribution/order, buyer & seller retention, liquidity |
| **Lending / fintech** | NIM, CAC, GNPA, credit cost, LTV net of losses, collection efficiency |
| **Subscription media** | ARPU, churn, engagement (DAU/MAU), content cost per sub |

**The one-liner to remember:** *If contribution margin per unit isn't positive, no amount of scale, funding, or growth fixes it.*
