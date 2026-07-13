# The 6-Month Mastery Roadmap

## What it is & where it's used

Chapters 1–7 gave you the raw skills — Excel, accounting mechanics, SQL, a bit of Python, GST/Tally, a modeling primer. This chapter is the **operating plan** that welds them into a hireable profile. A roadmap is not "study more." It is a sequenced, milestone-gated build where every month produces a **deliverable an interviewer can look at** — a working model, a reconciled book of accounts, a dashboard, a repo.

Where this matters: any candidate 0–3 years out. Hiring managers for FP&A, financial analyst, audit associate, tax executive, credit analyst, and finance-BA roles all screen the same way — they don't ask "did you learn Excel?", they ask "show me something you built." A structured 6-month portfolio is what turns "MBA Finance + CA Inter" (a credential thousands share) into "the person who built a 3-statement model of an actual listed company and can defend every driver."

The roadmap has three parallel tracks you deepen simultaneously:

| Track | Core skill | Proof-of-work artifact |
|---|---|---|
| **Modeling** | 3-statement + valuation in Excel | Fully-linked model of a real Indian listco |
| **Data** | SQL + Python + Power BI/DAX | A dashboard fed by a query you wrote |
| **Domain** | ONE chosen specialization | A case/deliverable specific to that domain |

## The gap: why companies want this (and college didn't teach it)

College teaches **subjects in isolation and tests recall**. Industry rewards **integrated output under a deadline**. The MBA gives you NPV formulas; it never makes you build a model where a change in a revenue-growth assumption ripples through the P&L, working capital, cash flow, and debt schedule and *still balances*. CA Inter drills you on standards and journal entries; it rarely makes you close a full month-end in Tally and produce a variance commentary a CFO would read.

The specific gap this roadmap closes:

- **Integration** — real work links accounting → modeling → data → decision. Nobody hands you a clean, pre-scoped problem.
- **Ownership of a deliverable** — you own something end-to-end, including the ugly reconciliation at the end.
- **Explaining your work** — "walk me through your model" is the single most common finance interview prompt, and it has no textbook answer.

Six months is enough to manufacture that experience *before* anyone pays you for it.

## What "proficient" looks like

The bar an employer tests for at the end of this roadmap:

- Build a **3-statement model from a downloaded annual report in under 3 hours**, balance sheet tying out, no hardcodes over formulas, no circular-reference errors left unresolved.
- Write a **JOIN + GROUP BY SQL query** against an unfamiliar schema in 10 minutes to answer a business question.
- Take a raw transaction dump and produce a **Power BI dashboard with 3–4 DAX measures** (YoY, running total, % of total).
- **Close a set of books**: pass month-end journals, reconcile the bank and GST, produce a Trial Balance that agrees.
- **Defend every number** you present — "why 12% WACC?", "why did receivable days move?" — without freezing.

Proficiency = you can do the above **unaided, under time pressure, and explain it**.

## Hands-on: how to actually do it

### The month-by-month build

| Month | Theme | Milestone (must-ship deliverable) | Checkpoint (pass/fail test) |
|---|---|---|---|
| **1** | Excel + accounting fluency | Rebuild a company's P&L + BS in Excel from its annual report | Balance sheet balances; zero hardcoded totals |
| **2** | 3-statement model | Link IS → BS → CFS with a debt & working-capital schedule | Model flows when you change 1 driver; ties out |
| **3** | Valuation | Add DCF + comparables tab; arrive at a target price | You can justify WACC, terminal growth, exit multiple |
| **4** | Data — SQL | Load transaction data, answer 10 business questions in SQL | Correct JOIN/GROUP BY results, verified against Excel |
| **5** | Data — BI + Python | Power BI dashboard + a Python script that cleans the source | 4 DAX measures correct; script reproducible |
| **6** | Domain track + polish | One domain deliverable + package the portfolio | Mock interview: walk through everything cleanly |

### Modeling track — the driver pattern

Never hardcode a forecast. Drive it. In Excel, a revenue build:

```
Revenue_next = Revenue_this * (1 + Growth_rate)
=B10*(1+$C$3)
```

Working-capital days that feed the cash flow:

```
Debtor Days   = Receivables / Revenue * 365      =B20/B10*365
Receivables   = Debtor Days assumption / 365 * Revenue
```

The circular-reference reality: interest depends on debt, debt depends on cash, cash depends on interest. Turn on **File → Options → Formulas → Enable iterative calculation** (max 100 iterations), and keep a **circularity switch** cell so you can break it when auditing:

```
Interest = IF($C$1=0, 0, Avg_Debt * Interest_rate)
```

### Data track — SQL you will actually be asked

```sql
-- Top 5 customers by revenue in FY2024-25
SELECT c.customer_name,
       SUM(s.amount) AS total_revenue
FROM sales s
JOIN customers c ON c.customer_id = s.customer_id
WHERE s.invoice_date BETWEEN '2024-04-01' AND '2025-03-31'
GROUP BY c.customer_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Month-on-month revenue with a window function
SELECT DATE_TRUNC('month', invoice_date) AS mth,
       SUM(amount) AS revenue,
       SUM(amount) - LAG(SUM(amount)) OVER (ORDER BY DATE_TRUNC('month', invoice_date)) AS mom_change
FROM sales
GROUP BY 1
ORDER BY 1;
```

### Data track — Python to clean the raw dump

```python
import pandas as pd

df = pd.read_csv("tally_export.csv")
df.columns = df.columns.str.strip().str.lower()
df["amount"] = (df["amount"].astype(str)
                .str.replace(",", "", regex=False)
                .astype(float))
df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)

# Monthly revenue by state (GST use-case)
summary = (df.groupby([df["invoice_date"].dt.to_period("M"), "state"])["amount"]
             .sum().reset_index())
summary.to_csv("monthly_by_state.csv", index=False)
```

### Data track — DAX measures for the dashboard

```dax
Total Revenue = SUM(Sales[Amount])

Revenue YoY % =
VAR Curr = [Total Revenue]
VAR Prior = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(Curr - Prior, Prior)

Running Total =
CALCULATE([Total Revenue],
    FILTER(ALLSELECTED('Date'[Date]), 'Date'[Date] <= MAX('Date'[Date])))
```

### Accounting track — a month-end close journal set

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 31-Mar | Depreciation A/c … Dr | 50,000 | |
| | To Accumulated Depreciation | | 50,000 |
| 31-Mar | Salaries A/c … Dr | 2,00,000 | |
| | To Salaries Payable (accrual) | | 2,00,000 |
| 31-Mar | Prepaid Insurance A/c … Dr | 12,000 | |
| | To Insurance Expense | | 12,000 |

### Choose ONE domain track (Month 6)

| Domain | Deliverable | Signature skill |
|---|---|---|
| **FP&A / Corporate finance** | Rolling 12-month budget vs actuals + variance memo | Driver-based forecasting |
| **Equity research** | 2-page initiation note with a rating | Valuation + thesis writing |
| **Tax / GST** | GSTR-2B vs purchase register reconciliation + ITC note | Portal + reconciliation |
| **Audit** | Sample testing workpaper + a control-deficiency memo | Sampling, documentation |
| **Credit / lending** | Credit appraisal note with ratio + DSCR analysis | Debt-serviceability judgement |

## Worked example / mini-project

**The spine project: a full model + dashboard on an Indian listco (say, an FMCG mid-cap).**

1. **Source data (Month 1).** Download the latest annual report. Type the last 3 years of P&L and BS into a `Historicals` tab. Verify: Assets = Liabilities + Equity for every year. Suppose Revenue ₹4,200 Cr, PAT ₹380 Cr.

2. **Build drivers (Month 2).** Assume revenue growth 11%, EBITDA margin 18%, debtor days 32, inventory days 45, tax 25%. Forecast 5 years. Link IS → BS → CFS. Add a debt schedule; opening ₹600 Cr, ₹100 Cr annual repayment. Confirm closing cash on the CFS = cash on the BS.

3. **Value it (Month 3).** WACC 12%, terminal growth 5%. Discount 5 years of FCFF plus a Gordon terminal value:

```
FCFF = EBIT*(1-tax) + Dep&Amort - Capex - Change in WC
Terminal Value = FCFF_year5 * (1+g) / (WACC - g)
Enterprise Value = SUM(PV of FCFF) + PV of Terminal Value
```

Cross-check with comparables (EV/EBITDA of 3 peers). Arrive at a target price, e.g. ₹1,450 vs market ₹1,300 → "Buy."

4. **Analyze the data (Month 4–5).** Export segment/region sales into SQLite, run the top-customer and MoM queries above. Clean with the Python snippet. Build a Power BI page: revenue trend, YoY %, margin bridge, region split — with the three DAX measures.

5. **Domain wrap (Month 6).** If FP&A track: turn the forecast into a budget-vs-actual with a one-page variance commentary ("EBITDA ₹42 Cr below plan; ₹30 Cr is raw-material inflation, ₹12 Cr volume").

Ship it as one folder + a GitHub repo. This single project touches every track.

## How it's tested

- **The model walkthrough (universal).** "Take me through your model." They watch whether you know why each cell exists. Then a stress test: "revenue growth drops to 5% — what happens to the debt covenant?" You should be able to change it live.
- **Timed Excel test (60–90 min).** Build a mini 3-statement or a schedule from a given trial balance. Common at Big 4, corporate FP&A, KPO/GCC roles.
- **SQL screen (30–45 min).** HackerRank/DataCamp-style: JOINs, GROUP BY, window functions against a schema you've never seen.
- **The close case.** "Here's a trial balance and 6 adjustments — produce the finalized P&L and BS." Audit and controllership roles.
- **Case + guesstimate.** Equity research and credit: "value this business" or "would you lend to this company?" — judgement, not just arithmetic.
- **Behavioral.** "Tell me about a project you built end-to-end." Your portfolio *is* the answer.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Hardcoding numbers into formula cells | **Colour code**: blue = input, black = formula. Never type a number in a black cell. |
| Model doesn't balance, so they plug it | Build a **balance check row** (`=Assets - L - E`, should be 0). Find the error, never plug. |
| Ignoring the debt/interest circularity | Add an iterative-calc switch; understand *why* it's circular before disabling. |
| Learning tools in isolation | Force integration — the SQL query should feed the same company you modeled. |
| Chasing 5 domains shallowly | Pick **one** domain track. Depth beats breadth in interviews. |
| No commentary, just numbers | Always write the "so what" — 2 lines of insight per deliverable. |
| Studying without shipping | A milestone that isn't a file you can open didn't happen. |

## Learn-it roadmap & resources

**Realistic time:** 6 months at 10–12 focused hours/week gets you interview-ready; 20 hrs/week compresses it to ~3–4 months. The binding constraint is *shipping deliverables*, not watching lectures.

| Need | Free | Paid / Cert |
|---|---|---|
| Modeling | Aswath Damodaran (NYU) YouTube + spreadsheets | WallStreetPrep, CFI FMVA |
| Excel | ExcelJet, Chandoo | Microsoft Excel Expert (MO-201) |
| SQL | Mode SQL Tutorial, SQLBolt, HackerRank | DataCamp |
| Python | Kaggle "Pandas" micro-course | — |
| Power BI / DAX | Microsoft Learn, SQLBI (Marco Russo) | PL-300 (Power BI Data Analyst) |
| Valuation / thesis | Damodaran, Tijori/Screener.in for data | CFA L1 (India-recognized) |
| Tax/GST/Tally | GST portal + CBIC videos | TallyPrime certification |

**Sequencing rule:** don't collect certificates first. Build the artifact, then take the cert that certifies what you already built — it reads as validation, not aspiration.

## Quick-reference

**The 6 milestones:** (1) rebuilt financials → (2) linked 3-statement → (3) valuation + target price → (4) SQL answers → (5) BI dashboard + Python clean → (6) domain deliverable + portfolio.

**Checkpoint questions (ask yourself monthly):**
- Does my balance sheet balance without a plug?
- Can I change one driver and watch it flow?
- Can I write a JOIN + GROUP BY unaided?
- Can I defend every assumption out loud?
- Is each month a *file I can send someone*?

**Key formulas:**

```
Growth-driven forecast   =PrevCell*(1+GrowthRate)
Debtor days              =Receivables/Revenue*365
FCFF                     EBIT*(1-t)+D&A-Capex-ΔWC
Terminal value           FCFF*(1+g)/(WACC-g)
SQL essentials           JOIN ... ON | GROUP BY | LAG() OVER()
DAX YoY                  DIVIDE(Curr-Prior, Prior) with SAMEPERIODLASTYEAR
Balance check            =TotalAssets-TotalLiab-Equity   (must=0)
```

**Colour convention:** blue input · black formula · green = links to other sheets.

**The one rule:** every month ends with a shippable file, or the month didn't count.
