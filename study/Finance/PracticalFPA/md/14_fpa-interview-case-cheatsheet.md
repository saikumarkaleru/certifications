# The FP&A Interview & Case (with cheat-sheet)

## What it is & where it's used

The FP&A interview is the final filter between "I did an MBA / cleared CA Inter" and a ₹6-18 LPA offer as an **FP&A Analyst, Business Finance Analyst, Financial Analyst, or Budgeting Analyst**. It has three moving parts, and every serious company (Amazon, Flipkart, Genpact, EY/Deloitte finance-transformation teams, GCCs like Wells Fargo/JPMC Hyderabad, plus mid-market CFO offices) tests all three:

1. **Conceptual Q&A** — do you understand the three statements, drivers, and variance?
2. **A live/take-home case** — build a mini-model, forecast, and explain the variance.
3. **A timed Excel/technical screen** — XLOOKUP, pivots, sometimes SQL or Power BI.

This chapter is the closing chapter: it assumes you've read the modelling, variance, and budgeting chapters, and now packages everything for the room. Roles that hire on this exact skill set: FP&A Analyst, Cost Analyst, Revenue Analyst, Corporate Finance Associate, and finance roles inside SaaS/D2C startups where "the analyst who owns the model" is a real job title.

## The gap: why companies want this (and college didn't teach it)

College taught you to **calculate** ratios and **pass** journal entries against a given trial balance. It did not teach you to sit in front of a hiring manager and answer *"Revenue missed budget by ₹40 lakh — walk me through why, in 90 seconds."* That answer requires **price/volume/mix decomposition**, a **bridge**, and a **recommendation** — none of which appear in a textbook exam.

The specific gaps this chapter closes:

| College teaches | Job actually tests |
|---|---|
| Compute NPV given cash flows | Build the cash flows yourself from assumptions |
| Define working capital | Forecast WC and explain the cash impact |
| "Variance = Actual − Budget" | *Why* the variance happened + what to do |
| Solve one clean problem | Handle a messy 5,000-row export under time pressure |
| Written exams | Talk while you build, defend your number |

Employers pay for **judgement under ambiguity**, communicated crisply. The interview is engineered to detect exactly that.

## What "proficient" looks like

A job-ready candidate, unaided, can:

- **Answer the three-statement linkage question cold** — how a ₹100 depreciation change flows through P&L, cash flow, and balance sheet (net income −₹75 assuming 25% tax, cash +₹25, retained earnings −₹75, PP&E −₹100... balances).
- **Build a driver-based revenue forecast** in Excel in under 15 minutes (units × price, or customers × ARPU).
- **Decompose a variance** into price, volume, and mix — not just report the delta.
- **Write an XLOOKUP / SUMIFS / pivot** without googling.
- **Read a SQL screen** — `GROUP BY`, `JOIN`, a window function.
- **State a recommendation** in one sentence: "Cut CAC by moving 20% of spend from Google to referral; that recovers ₹22L of the ₹40L miss."

The bar is not "knows everything." It's "can produce a defensible number and a decision from messy inputs, and explain it to a non-finance manager."

## Hands-on: how to actually do it

### The Excel core they will test

```excel
# Lookup a budget figure by cost centre (modern)
=XLOOKUP(A2, Budget[CostCentre], Budget[Amount], "Not found")

# Conditional sum — actuals for one department, one month
=SUMIFS(Actuals[Amt], Actuals[Dept], "Sales", Actuals[Month], "Jun")

# Variance % with divide-by-zero guard
=IFERROR((Actual-Budget)/Budget, 0)

# Two-way lookup (row = account, col = month) without a pivot
=INDEX(Data, MATCH($A2, Accounts, 0), MATCH(B$1, Months, 0))

# CAGR over n years
=(End/Start)^(1/n) - 1
```

### Price / Volume / Mix — the question that separates analysts from clerks

```
Volume variance = (Actual Qty − Budget Qty) × Budget Price
Price variance   = (Actual Price − Budget Price) × Actual Qty
Mix variance     = shift in product mix at standard margins
Total = Volume + Price (+ Mix)
```

### The SQL screen (revenue by month from a transactions table)

```sql
SELECT DATE_TRUNC('month', invoice_date) AS mth,
       SUM(amount)                       AS revenue,
       COUNT(DISTINCT customer_id)       AS active_customers,
       SUM(amount) / COUNT(DISTINCT customer_id) AS arpu
FROM   invoices
WHERE  invoice_date >= '2025-04-01'
GROUP  BY 1
ORDER  BY 1;

-- Month-over-month growth with a window function
SELECT mth, revenue,
       revenue - LAG(revenue) OVER (ORDER BY mth) AS mom_delta
FROM   monthly_rev;
```

### Python (if the JD mentions it)

```python
import pandas as pd
df = pd.read_csv("actuals.csv")
piv = df.pivot_table(index="account", columns="month",
                     values="amount", aggfunc="sum")
piv["variance"] = piv["Jun"] - piv["budget"]
piv["var_pct"]  = piv["variance"] / piv["budget"]
print(piv.sort_values("variance").head(10))   # 10 worst misses
```

### DAX (Power BI screens)

```dax
Variance = SUM(Actuals[Amount]) - SUM(Budget[Amount])
Var % = DIVIDE([Variance], SUM(Budget[Amount]))
YTD Actual = TOTALYTD(SUM(Actuals[Amount]), 'Date'[Date])
```

## Worked example / mini-project

**The case (typical take-home, India SaaS):** "Q1 FY26 revenue was budgeted at ₹5.00 Cr; actual came in at ₹4.60 Cr. Explain the ₹40L miss and recommend one action."

Given data:

| Metric | Budget | Actual |
|---|---|---|
| New customers | 500 | 460 |
| ARPU (₹/customer) | ₹1,00,000 | ₹1,00,000 |
| Marketing spend | ₹75L | ₹80L |
| CAC (₹/customer) | ₹15,000 | ₹17,391 |

**Step 1 — bridge the revenue miss.**

```
Revenue = Customers × ARPU
Volume variance = (460 − 500) × ₹1,00,000 = −₹40,00,000
Price/ARPU variance = (1,00,000 − 1,00,000) × 460 = 0
Total = −₹40L   → 100% a volume (customer-acquisition) problem
```

The miss is **not** pricing. ARPU held. We acquired 40 fewer customers.

**Step 2 — why fewer customers?** CAC rose from ₹15,000 to ₹17,391 (+16%) *while* spend rose ₹5L. So we spent **more** and got **fewer** — efficiency collapsed. Customers acquired = ₹80L ÷ ₹17,391 ≈ 460. Had CAC held at ₹15,000, ₹80L would have bought ~533 customers.

**Step 3 — the one-sentence recommendation.**
> "The ₹40L miss is entirely a volume problem driven by a 16% CAC spike, not pricing. Reallocate spend from the underperforming paid channel toward referral (historically ₹8,000 CAC); at that efficiency, the existing ₹80L budget recovers the 40-customer shortfall and ₹40L of revenue within one quarter."

**Step 4 — the Excel that backs it:**

```excel
Volume var =(460-500)*100000          → -4000000
CAC actual =80000000/460              → 17391
Cust if CAC held =80000000/15000      → 5333
```

That is a complete, defensible answer: bridge → root cause → decision → number. Reproduce it in a blank sheet in under 20 minutes and you clear most FP&A case rounds.

## How it's tested

**Round 1 — conceptual (verbal), the greatest hits:**

- "Walk me through the three statements. Now change depreciation by ₹100 — trace it."
- "What's the difference between a budget, a forecast, and a plan?" (Budget = fixed target set once; forecast = updated view of reality; plan = the strategy behind the numbers.)
- "Revenue is up but cash is down — how?" (WC bloat: receivables/inventory up, or capex.)
- "What KPIs would you track for a D2C brand?" (CAC, LTV, LTV/CAC, contribution margin, repeat rate, cash conversion cycle.)
- "How do you build a revenue forecast?" (Driver-based: units × price, cohort, or run-rate — never a flat % without a driver.)

**Round 2 — the case:** a take-home model or a live "build a 3-year forecast from these assumptions," followed by defending every number.

**Round 3 — the timed technical screen:** 30-45 min. A messy CSV; deliver a pivot, an XLOOKUP-driven variance report, and often a chart. GCCs increasingly add a SQL screen and a Power BI task.

**What they're really scoring:** structure (did you bridge, not just subtract?), speed, accuracy under pressure, and whether you *ended with a decision*.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Reporting a variance without explaining *why* | Always bridge: price / volume / mix, then root cause |
| Hardcoding numbers inside formulas | Every driver lives in a labelled input cell; formulas reference cells |
| Forecasting revenue as a flat "+10%" | Tie growth to a driver (customers, price, capacity) |
| Silent during the live case | Narrate: "I'm laying inputs top-left, calcs below, output right" |
| No recommendation | End every answer with one decision sentence + the ₹ impact |
| Circular refs / broken balance sheet | Know the depreciation and interest-on-debt linkages cold |
| Over-engineering the model | Deliver a clean, right answer fast; polish only if time remains |
| Guessing on Excel syntax | Drill XLOOKUP, SUMIFS, INDEX-MATCH, IFERROR until automatic |

## Learn-it roadmap & resources

**Time to interview-ready: 6-10 weeks** if you already have the MBA/CA base.

| Weeks | Focus |
|---|---|
| 1-2 | Excel drills: XLOOKUP, SUMIFS, pivots, INDEX-MATCH — daily reps |
| 3-4 | Three-statement model from scratch, 5x, no template |
| 5-6 | Variance/bridge cases; price-volume-mix until reflexive |
| 7-8 | SQL basics (SELECT/JOIN/GROUP BY/window) + one Power BI dashboard |
| 9-10 | Mock interviews out loud; timed 30-min Excel cases |

**Resources**
- **Free:** CFI free Excel & FP&A intros; Corporate Finance Institute cheat-sheets; Ben Felix / Aswath Damodaran (valuation intuition); LeetCode/StrataScratch (easy SQL); Microsoft Learn (Power BI/DAX).
- **Paid (high ROI):** CFI **FMVA** (~₹40-70k, globally recognised for FP&A), Wall Street Prep / Breaking Into Wall Street modelling courses.
- **India-specific:** for controllership-flavoured roles your **CA Inter** costing + accounting is already a strong differentiator — lead with it.

## Quick-reference

**Core formulas**

| Metric | Formula |
|---|---|
| Variance | Actual − Budget |
| Variance % | (Actual − Budget) / Budget |
| Volume var | (Act Qty − Bud Qty) × Bud Price |
| Price var | (Act Price − Bud Price) × Act Qty |
| CAGR | (End/Start)^(1/n) − 1 |
| Gross margin | (Revenue − COGS) / Revenue |
| Contribution margin | (Revenue − Variable cost) / Revenue |
| EBITDA | EBIT + Dep + Amort |
| LTV | ARPU × Gross margin × Avg lifetime |
| LTV/CAC | Healthy ≥ 3× |
| CAC | Total S&M spend / New customers |
| CCC | DSO + DIO − DPO |
| Working capital | Current assets − Current liabilities |
| Free cash flow | CFO − Capex |

**Excel one-liners**

| Task | Formula |
|---|---|
| Lookup | `=XLOOKUP(key, lookup, return, "NA")` |
| Conditional sum | `=SUMIFS(sum, crit1, val1, crit2, val2)` |
| Two-way lookup | `=INDEX(d, MATCH(r,rows,0), MATCH(c,cols,0))` |
| Guarded divide | `=IFERROR(a/b, 0)` |
| Count by criteria | `=COUNTIFS(rng, crit)` |

**The interview mantra:** *Bridge the number → find the root cause → end with one decision and its ₹ impact.* Structure beats speed; a decision beats a correct-but-mute calculation.
