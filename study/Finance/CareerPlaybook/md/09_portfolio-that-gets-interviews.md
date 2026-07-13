# Building a Portfolio That Gets Interviews

## What it is & where it's used

A finance portfolio is a small, curated set of *finished, reviewable deliverables* that prove you can do the job before anyone hires you. For a fresher or a career-switcher with an MBA + CA Inter, it is the single fastest way to jump the resume screen: a recruiter reads 200 identical CVs ("proficient in Excel, strong analytical skills") and one that links to a working 3-statement model, a live Power BI dashboard, and a GitHub repo with SQL. Guess who gets the call.

Four deliverables carry almost every finance/accounts/tax role:

| Deliverable | Roles it opens |
|---|---|
| **3-statement model** (Excel) | FP&A, corporate finance, equity research, investment banking, credit analyst |
| **Power BI / dashboard** | FP&A, business finance, MIS analyst, controllership, finance-BI |
| **SQL / Python project** | Finance analyst, data-heavy FP&A, fintech, revenue/GST analytics |
| **Valuation write-up** | Equity research, IB, PE/VC, corporate development |

You don't need all four. Two done *well* beats four done shabbily. Pick the two that match your target role.

## The gap: why companies want this (and college didn't teach it)

College taught you the *concepts* — CAPM, DCF, ratio analysis, the accounting equation. It graded you on knowing what NPV *is*. Employers pay you to *build the thing that produces the number* and defend it. The gap is almost entirely mechanical and habitual:

- MBA teaches "a DCF discounts free cash flows." It does **not** teach you to build a driver-based revenue schedule, tie a circular interest calculation with an iterative-calc toggle, or make the balance sheet actually balance.
- CA teaches you to *pass* journal entries. It does **not** teach you to pull 5 years of a company's financials from an annual report into a clean, formula-linked model that a manager can audit in 30 seconds.
- Nobody taught you version control, so your "final_v3_FINAL_actual.xlsx" habit screams fresher.

The portfolio closes this because it is *evidence of the mechanical skill*, not a claim about the conceptual one. It also proves the meta-skill employers most quietly value: you can take a messy real-world dataset and produce a decision-grade output, unaided.

## What "proficient" looks like

The bar a hiring manager silently tests for:

- **3-statement model:** IS, BS, CFS fully linked; balance sheet balances to zero in every year and every scenario; assumptions on a separate, colour-coded input tab (blue = input, black = formula); a working scenario toggle; no hardcoded numbers inside formulas; circularity (interest on average debt) handled cleanly.
- **Dashboard:** loads from a data model (not one flat sheet), has slicers that actually filter, uses DAX measures (not calculated columns for everything), and answers a *business question* on the first screen ("are we hitting budget?") — not just "here are 9 charts."
- **SQL/Python:** you can write a multi-table `JOIN` with `GROUP BY`, a window function, and a CTE without googling syntax; Python code runs top-to-bottom in a clean environment and reads a real CSV.
- **Valuation:** a 2-3 page write-up with a thesis, a DCF *and* a comparables cross-check, a sensitivity table, and an explicit "what I'd need to be wrong about" section.

## Hands-on: how to actually do it

### 1) The 3-statement model core mechanics

Keep inputs on a `Assumptions` tab and reference them. Never type a growth rate inside a P&L formula.

```
Revenue (Yr):        =PrevRevenue*(1+Assumptions!$B$4)      // growth driver
COGS:                =Revenue*Assumptions!$B$5              // % of sales
Depreciation:        =Opening_PPE*Assumptions!$B$8          // % of gross block
Interest expense:    =AVERAGE(Opening_Debt,Closing_Debt)*Assumptions!$B$10   // circular
```

Pull the right assumption automatically with a lookup instead of hardcoding scenario numbers:

```
=XLOOKUP($B$1, Scenarios[Case], Scenarios[RevGrowth])
```
where `$B$1` holds "Base" / "Bull" / "Bear".

**The balance-sheet check** (the formula an interviewer looks for first):

```
Check:  =Total_Assets - (Total_Liabilities + Total_Equity)   // must be 0 every year
```

Wrap the whole check row in conditional formatting: red if `ABS(check)>0.5`.

**Circularity:** interest depends on debt, debt depends on cash, cash depends on interest. Enable File > Options > Formulas > **Enable iterative calculation** (max 100, 0.001). Add a `Circuit Breaker` cell (a 1/0 switch) that zeroes interest so you can kill a `#REF!` spiral.

### 2) Power BI / DAX

Load data via Power Query (Get Data > CSV/Excel > Transform), then write measures — not calculated columns:

```dax
Total Revenue = SUM(Sales[Amount])

Revenue LY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))

YoY % = DIVIDE([Total Revenue] - [Revenue LY], [Revenue LY])

Budget Variance % = DIVIDE([Total Revenue] - SUM(Budget[Amount]), SUM(Budget[Amount]))
```

Build a proper `Date` table so time-intelligence works:

```dax
Date = CALENDAR(DATE(2022,4,1), DATE(2025,3,31))   // Indian FY start
```

### 3) SQL project

A revenue-and-collections query a finance analyst actually writes:

```sql
WITH monthly AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', invoice_date) AS mth,
        SUM(amount) AS revenue
    FROM invoices
    WHERE status = 'PAID'
    GROUP BY customer_id, DATE_TRUNC('month', invoice_date)
)
SELECT
    mth,
    SUM(revenue) AS total_rev,
    SUM(revenue) - LAG(SUM(revenue)) OVER (ORDER BY mth) AS mom_change
FROM monthly
GROUP BY mth
ORDER BY mth;
```

### 4) Python

```python
import pandas as pd

df = pd.read_csv("gst_sales_register.csv", parse_dates=["invoice_date"])
df["gst"] = df["taxable_value"] * 0.18

summary = (df.groupby(df["invoice_date"].dt.to_period("M"))
             .agg(taxable=("taxable_value", "sum"),
                  gst=("gst", "sum"),
                  invoices=("invoice_no", "count"))
             .round(0))
print(summary)
```

## Worked example / mini-project

**Project: "Kirana-to-Cloud Pvt Ltd — FY24 Finance Pack."** Invent a small D2C company. Build one repo/model that produces three linked outputs.

**Step 1 — Model.** Assumptions: FY24 revenue ₹12,00,00,000, growing 20%; COGS 55% of sales; opex ₹2,40,00,000; debt ₹3,00,00,000 at 11%; tax 25%; capex ₹80,00,000.

Sample P&L (₹ lakh):

| Line | FY24 | FY25E |
|---|---|---|
| Revenue | 1,200 | 1,440 |
| COGS (55%) | 660 | 792 |
| Gross profit | 540 | 648 |
| Opex | 240 | 264 |
| EBITDA | 300 | 384 |
| Depreciation | 40 | 48 |
| EBIT | 260 | 336 |
| Interest (11%) | 33 | 33 |
| PBT | 227 | 303 |
| Tax (25%) | 57 | 76 |
| **PAT** | **170** | **227** |

**Step 2 — Dashboard.** Export the sales register to CSV, load into Power BI, build a one-screen view: revenue vs budget card, YoY % KPI, monthly trend line, top-10 SKUs bar, a state slicer (ties to GST filing).

**Step 3 — Valuation.** Quick DCF: FY25E FCFF ≈ EBIT(1−t) + Dep − Capex − ΔWC = 336×0.75 + 48 − 80 − 20 ≈ ₹200 lakh. Grow at 6% terminal, WACC 13%: terminal value = 200×1.06 ÷ (0.13−0.06) ≈ ₹3,028 lakh. Cross-check with comps: peers trade at 12× EBITDA → 384×12 = ₹4,608 lakh EV. Write 2 pages: thesis, both methods, a WACC sensitivity table, and your honest range (₹30–46 cr EV).

Reproduce it, screenshot the dashboard, commit the Excel + `.pbix` + a `README.md`.

## How it's tested

Two layers: interview questions **and** a practical assessment.

**Interview questions**
- "Walk me through your 3-statement model. If revenue grows 10%, what happens to the cash flow statement?"
- "How does depreciation flow through all three statements?" (P&L −, add back in CFS, accumulated on BS)
- "Your DCF gives ₹40 cr, comps give ₹46 cr. Why the gap, and which do you trust?"
- "What DAX measure did you use for YoY, and why a measure not a column?"

**Practical / take-home tests you'll actually get**
- **Timed Excel test (45–90 min):** build a mini P&L from raw data, add a scenario toggle, VLOOKUP/XLOOKUP + INDEX-MATCH, a pivot. No internet.
- **SQL screen (HackerRank/live):** joins, `GROUP BY`, a window function, a CTE.
- **Case study:** "Here's a trial balance / annual report — build the model and email it back in 24 hours."
- **Dashboard task:** "Here's a CSV, build a dashboard that tells us if we're hitting target."

Your portfolio is the pre-loaded answer to all of these.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Hardcoding numbers inside formulas | All drivers on an input tab, referenced |
| Balance sheet doesn't balance; hidden plug | A visible `Check = Assets − (Liab+Equity)` row flagged red |
| No colour convention | Blue = input, black = formula, green = link to another tab |
| One giant flat sheet feeding Power BI | A Date table + star schema + measures |
| Dashboard with 12 charts, no message | One business question answered above the fold |
| "final_v4.xlsx" chaos | Git / GitHub with a real README |
| Copying a public model and calling it yours | Rebuild it yourself; you must defend every cell |
| Ignoring units | State "₹ lakh" once, top-left, and stay consistent |

## Learn-it roadmap & resources

Realistic time to a *credible two-deliverable portfolio*: **6–8 weeks** at ~1.5 hrs/day.

| Week | Focus |
|---|---|
| 1–2 | Excel modeling mechanics; build the 3-statement model |
| 3 | DCF + valuation write-up |
| 4–5 | Power BI: Power Query, data model, DAX, one dashboard |
| 6 | SQL basics + one query project |
| 7 | Python + pandas for one data task |
| 8 | GitHub cleanup, READMEs, screenshots, polish |

**Resources**
- **Free:** Corporate Finance Institute free lessons; Microsoft Learn (Power BI); Mode SQL Tutorial / SQLBolt; Kaggle "Python" + "pandas" micro-courses; Aswath Damodaran's valuation lectures (YouTube, free).
- **Paid (optional, India-relevant):** CFI FMVA certificate (adds a line + structure); WallStreetPrep / Breaking Into Wall Street for modeling reps; Microsoft PL-300 (Power BI Data Analyst) if targeting BI-heavy finance roles.
- Your CA Inter already gives you the accounting depth most competitors lack — lean on it; your gap is *tooling*, not concepts.

**Showcasing:** Create one GitHub repo, `finance-portfolio`. Structure: `/3-statement-model` (Excel + PDF export + README), `/valuation` (write-up PDF), `/powerbi` (`.pbix` + screenshot PNG in README — GitHub renders it), `/sql-python` (`.sql`, `.ipynb`). Write a top-level README with a one-line description and a screenshot per project. Put the repo link and the Power BI "Publish to web" link **on your resume and LinkedIn**. Pin the repo. That link is your interview magnet.

## Quick-reference

```
Balance check:   =Assets-(Liabilities+Equity)              // target 0
Scenario pull:   =XLOOKUP($B$1,Scenarios[Case],Scenarios[RevGrowth])
Avg-debt interest: =AVERAGE(OpenDebt,CloseDebt)*rate       // needs iterative calc
Two-way lookup:  =INDEX(rng,MATCH(row,rows,0),MATCH(col,cols,0))
```

| DAX | Purpose |
|---|---|
| `SUM(Sales[Amount])` | base measure |
| `CALCULATE([Rev],SAMEPERIODLASTYEAR('Date'[Date]))` | last-year |
| `DIVIDE(a,b)` | safe division (no /0 error) |

```sql
-- window function pattern
SUM(x) - LAG(SUM(x)) OVER (ORDER BY month)   -- MoM change
```

| Convention | Rule |
|---|---|
| Colour | Blue input, black formula, green cross-tab link |
| Circularity | Enable iterative calc (100 / 0.001) + circuit breaker |
| Units | Declare "₹ lakh/cr" once, keep consistent |
| Version control | Git + README + screenshots; never `final_v3` |
| Showcase | Pinned GitHub repo + Power BI web link on resume & LinkedIn |

**One-line rule:** ship two deliverables you can defend cell-by-cell, put the links where a recruiter will see them, and let the work skip you past the resume pile.
