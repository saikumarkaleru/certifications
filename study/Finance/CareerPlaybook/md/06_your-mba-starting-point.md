# Your MBA-Finance starting point: strengths & gaps

## What it is & where it's used

This chapter is a personal audit — a brutally honest map of what you already sell in an interview versus what you have to build before Monday of your first job. Your profile is specific and, frankly, strong: **MBA Finance + NISM Series XV (Research Analyst) + ~2 years on an F&O / derivatives desk + CA Intermediate in progress.** That combination signals markets fluency, valuation literacy, and — once CA is done — accounting and tax depth that most candidates never reach.

But a resume is not a skill set. Employers in India hire for *tasks*: build the three-statement model, reconcile the GST 2B, write the SQL that feeds the MIS deck, close the books by the 5th. Roles that map to your profile:

| Role family | What they actually want daily | Your fit today |
|---|---|---|
| Equity/credit research, buy-side | Valuation models, thesis notes, screening | **Strong** |
| FP&A / Corporate finance | Excel modeling, variance analysis, BI dashboards | Partial |
| Financial / management accounting | Journal entries, close, Tally/ERP, GST/TDS | Gap → closing with CA |
| Risk / treasury / derivatives ops | Greeks, VaR, hedge accounting, position recon | **Strong** on theory, gap on tooling |
| Data-driven finance / analytics | SQL, Python, Power BI, automation | Gap |

The job is to convert *credentials* into *deliverables*.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you to *reason* about finance — NPV, WACC, CAPM, Porter, capital structure. Employers assume you can reason. What they pay for is *execution under a deadline on their data*. That is the education-to-industry gap, and it has four concrete faces for your profile.

1. **Hands-on Excel modeling.** You know DCF conceptually. Can you build a live, circular-reference-safe three-statement model with a working capital schedule, a debt sweep, and toggles — in 90 minutes, no template? That's the test, and college never times you.
2. **SQL / Python / BI.** Company data lives in databases and ERPs, not textbook tables. FP&A and analytics roles now assume you can pull your own data (`SELECT`), not wait for IT. Python replaces the manual monthly copy-paste.
3. **ERP & practical compliance.** CA *theory* teaches Ind AS and GST law. The job needs you to *pass a GST entry in TallyPrime*, file GSTR-3B on the portal, and reconcile 2B — click by click.
4. **FP&A tooling.** Budget vs actual, rolling forecasts, driver-based models, and a Power BI dashboard the CFO opens on their phone. MBA cases end at the recommendation; the job starts there.

## What "proficient" looks like

The bar an employer tests for — what a job-ready person does *unaided*:

- **Excel:** Builds a 3-statement model from a blank sheet; uses `XLOOKUP`, `SUMIFS`, `INDEX/MATCH`, `IFERROR`; finds and kills a circularity; no hardcoded numbers inside formulas; keyboard-driven (Alt shortcuts, no mouse).
- **SQL:** Writes a multi-table `JOIN` with `GROUP BY`, a window function, and a CTE to answer "top 5 customers by overdue receivables this quarter" without googling syntax.
- **Python:** Reads an Excel/CSV with `pandas`, cleans it, does a `groupby`, and exports a formatted output — turning a 2-hour manual task into a 20-second script.
- **BI:** A Power BI model with a proper date table and 4-5 DAX measures (YoY, YTD, variance %).
- **Compliance/ERP:** Passes purchase/sales entries with correct CGST/SGST/IGST split in Tally, reconciles GSTR-2B to books, computes TDS under the right section.

If you can do these five things cold, you clear ~80% of India finance-role practical screens.

## Hands-on: how to actually do it

**Leverage your strength first — a derivatives P&L any desk respects, in Excel:**

```
Payoff of long call at expiry:  =MAX(0, Spot - Strike) - Premium
Long put:                       =MAX(0, Strike - Spot) - Premium
Breakeven (long call):          =Strike + Premium
```

**Fill the Excel gap — the formulas that appear in every modeling test:**

```excel
=XLOOKUP(A2, Master[Code], Master[Name], "Not found")
=SUMIFS(Sales[Amt], Sales[Region],"West", Sales[Month],">="&DATE(2026,4,1))
=IFERROR(INDEX(Rate, MATCH(1,(T=B2)*(Tenor=C2),0)), 0)   'array match
=NPV(0.11, C5:C14) + C4        'C4 = year-0 cash flow, kept outside NPV
=IRR(C4:C14)
```

**Close the SQL gap — the query pattern FP&A lives on:**

```sql
-- Top 5 customers by overdue receivables, current quarter
SELECT c.customer_name,
       SUM(i.amount_due) AS overdue
FROM invoices i
JOIN customers c ON c.id = i.customer_id
WHERE i.due_date < CURRENT_DATE
  AND i.status = 'OPEN'
GROUP BY c.customer_name
ORDER BY overdue DESC
LIMIT 5;

-- Month-on-month revenue with a window function
SELECT month,
       revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS mom_change
FROM monthly_revenue;
```

**Close the Python gap — kill a recurring manual task:**

```python
import pandas as pd

df = pd.read_excel("ledger.xlsx", sheet_name="GL")
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

summary = (df.groupby(["month", "cost_center"])["amount"]
             .sum()
             .reset_index()
             .pivot(index="cost_center", columns="month", values="amount"))

summary.to_excel("cost_center_MIS.xlsx")
```

**Close the BI gap — DAX measures for a variance dashboard:**

```dax
Revenue YTD    = TOTALYTD(SUM(Fact[Revenue]), 'Date'[Date])
Revenue LY     = CALCULATE(SUM(Fact[Revenue]), SAMEPERIODLASTYEAR('Date'[Date]))
YoY %          = DIVIDE([Revenue YTD] - [Revenue LY], [Revenue LY])
Bud Variance   = SUM(Fact[Actual]) - SUM(Fact[Budget])
```

**Close the compliance gap — an actual GST purchase entry (goods bought within Maharashtra, ₹1,00,000 @ 18%):**

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Purchases A/c | 1,00,000 | |
| Input CGST @ 9% | 9,000 | |
| Input SGST @ 9% | 9,000 | |
| To Creditor (ABC Ltd) | | 1,18,000 |

TallyPrime path: `Gateway of Tally → Vouchers → F9 Purchase → select party → item → GST auto-computes if the ledger's GST rate + place of supply are set`. Interstate? The CGST/SGST lines collapse into a single **IGST @ 18% = ₹18,000**.

## Worked example / mini-project

**Project: One-page FP&A pack for a mid-size distributor, FY 2026-27.** Reproduce this end to end — it exercises your gaps and shows off your strengths.

Assume budgeted annual revenue ₹12 crore (₹1 cr/month, flat), actuals below for Q1:

| Month | Budget (₹) | Actual (₹) |
|---|---|---|
| Apr | 1,00,00,000 | 92,00,000 |
| May | 1,00,00,000 | 1,05,00,000 |
| Jun | 1,00,00,000 | 1,11,00,000 |

**Step 1 — Excel variance:**
```excel
Variance ₹   =Actual - Budget          'Apr = -8,00,000
Variance %   =(Actual-Budget)/Budget   'Apr = -8.0%
Q1 Actual    =SUM(Actuals)             '=3,08,00,000
Run-rate FY  =AVERAGE(Q1)*12           '=12,32,00,000
```

**Step 2 — SQL for the underlying pull** (if data sits in a DB):
```sql
SELECT DATE_TRUNC('month', invoice_date) AS month, SUM(net_amount) AS actual
FROM sales WHERE invoice_date >= '2026-04-01'
GROUP BY 1 ORDER BY 1;
```

**Step 3 — Python to auto-build the deck data** (from `sales.xlsx`) using the snippet above, exporting a clean pivot.

**Step 4 — DAX in Power BI** to show `Bud Variance` and `YoY %` as cards with a monthly bar chart.

**Result you present:** "Q1 revenue is ₹3.08 cr, tracking ₹32 lakh *ahead* of the ₹3 cr budget after a soft April; FY run-rate ₹12.32 cr vs ₹12 cr budget, +2.7%." That one sentence — data-backed, tool-built — is what an FP&A hire is paid to produce.

## How it's tested

Indian and global finance interviews increasingly split into a talk round and a *do* round.

| Screen | What they hand you | Time |
|---|---|---|
| Timed Excel test | Blank sheet + assumptions → build DCF or 3-statement model | 60-120 min |
| SQL screen | Schema + 3-4 questions ("2nd highest salary", "running total") | 30-45 min |
| Case: "close these books" | Trial balance with errors → adjust, produce P&L + BS | 60 min |
| Compliance task | Invoice set → compute GST/TDS, say which return & due date | 30 min |
| Markets round (your home turf) | "Price this option / explain contango / what's your view" | Live |

Common interview questions: *Walk me through a DCF. How does depreciation flow through three statements? What's the TDS rate on professional fees? Difference between GSTR-1, 2B, 3B? When would you use INDEX/MATCH over VLOOKUP?* Prepare to **do**, not describe.

## Common mistakes & how pros avoid them

- **Leading with credentials, not deliverables.** "I have an MBA and NISM" → weak. "I built a 3-statement model and a Power BI variance pack" → hired. Pros open with artifacts.
- **Hardcoding numbers inside Excel formulas.** `=A2*1.18` is a red flag; put 18% in a labeled input cell and reference it. Assumptions live in one colored block.
- **Mouse-driving Excel in a timed test.** Learn Alt-key shortcuts; speed is graded.
- **Treating SQL/Python as "IT's job."** Analysts who pull their own data get promoted; those who raise tickets wait.
- **Confusing CA *theory* with ERP *practice*.** Knowing Section 194J ≠ passing the entry in Tally and filing 26Q. Do both.
- **Ignoring reconciliation.** GSTR-2B vs books mismatch is the #1 real-world compliance task; models must tie out to the rupee.
- **Underselling the derivatives edge.** Few finance hires can price an option or explain the Greeks. That's a differentiator — name it.

## Learn-it roadmap & resources

Realistic time-to-proficiency assuming ~1 hr/day alongside CA:

| Skill | To job-ready | Resource |
|---|---|---|
| Excel modeling | 3-4 weeks | CFI free Excel courses; Wall Street Prep; Chandoo.org (free) |
| SQL | 3-4 weeks | SQLBolt (free), Mode SQL tutorial, LeetCode DB easy/medium |
| Python (pandas) | 4-6 weeks | Kaggle "pandas" micro-course (free); *Python for Data Analysis* |
| Power BI + DAX | 2-3 weeks | Microsoft Learn (free); SQLBI.com; DAX Guide |
| Tally + GST practical | 2-3 weeks | Tally EDU free lessons; ICAI GST material (you already have via CA) |

Certifications worth it: **Microsoft PL-300 (Power BI Data Analyst)**, **CFI FMVA** (modeling), and finish **CA** — it dominates every other line item. Sequence: Excel → SQL → Power BI → Python, folding Tally/GST practice in parallel with your CA GST paper.

## Quick-reference

```text
STRENGTHS to sell:  Markets/derivatives · valuation · NISM RA · CA depth (incoming)
GAPS to close:      Excel modeling · SQL · Python · Power BI · Tally/GST practical

Excel:   =XLOOKUP() =SUMIFS() =INDEX/MATCH =IFERROR() =NPV() =IRR()  (inputs in one block)
SQL:     SELECT ... JOIN ... GROUP BY ... ; window: LAG() OVER(ORDER BY ...)
Python:  pd.read_excel → groupby → pivot → to_excel
DAX:     TOTALYTD · SAMEPERIODLASTYEAR · DIVIDE for YoY%
GST:     Intra-state = CGST+SGST split · Inter-state = IGST · reconcile 2B to books
Options: Long call P/L = MAX(0,S-K) - premium ; breakeven = K + premium
```

**One-line self-brief:** *"MBA + markets desk + CA-in-progress who ships models, dashboards, and clean books — not just opinions."* Build three artifacts (a 3-statement model, a Power BI pack, a Tally close) and your gap is closed.
