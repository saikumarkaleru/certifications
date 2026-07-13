# What FP&A & Corporate Finance Actually Do

## What it is & where it's used

**FP&A** (Financial Planning & Analysis) is the team that turns a company's raw accounting data into forward-looking decisions: how much will we earn next quarter, can we afford this hire, why did margin drop 2%, should we approve this ₹40 lakh capex. **Corporate finance** is the broader umbrella — capital structure, funding, treasury, valuation, M&A — of which FP&A is the operational, monthly-heartbeat piece.

Where it lives, by role:

| Role | What the FP&A/corp-fin work looks like |
|---|---|
| FP&A Analyst | Builds/updates the monthly forecast, variance decks, budget templates |
| Business Finance Partner | Sits with a Sales/Ops head, defends their P&L, challenges spend |
| Treasury Analyst | Cash-flow forecast, banking, working-capital, FX exposure |
| Corp Dev / IB Analyst | Valuation models (DCF, comps), deal support, board packs |
| Startup Finance (India) | All of the above at once — MIS, runway, investor reporting, GST |
| Controller / Accounts | Owns the actuals that FP&A forecasts against |

In India this shows up as "MIS Analyst", "Business Finance", "FP&A", or simply "Finance Manager" in a startup. The tool stack is near-universal: **Excel** (the real ERP of finance), a **BI layer** (Power BI/Tableau), the **ERP/ledger** (Tally, SAP, NetSuite, Zoho), and increasingly **SQL/Python** to get data out without begging IT.

## The gap: why companies want this (and college didn't teach it)

Your MBA taught you WACC, CAPM, and the Modigliani-Miller theorem. Your CA course taught you AS/Ind-AS, journal entries, and how to *audit* a set of books. Neither taught you the actual job, which is **80% "get the number, explain the number, project the number" and 20% theory.**

The concrete gaps:

- **College is backward-looking; FP&A is forward-looking.** You were graded on preparing/auditing past financials. Employers pay you to *forecast* the next 12 months and be roughly right.
- **College gives clean data; the job gives garbage.** No textbook problem has duplicate cost centres, a ₹ in a text field, or three spellings of "Reliance". Real data cleaning is 40% of the job.
- **College values the exact answer; the job values the fast, defensible, on-time answer.** A board deck at 90% accuracy on Monday beats 100% on Thursday.
- **Nobody taught you Excel as a modelling language** — dynamic arrays, `INDEX/MATCH`, `SUMIFS`, scenario toggles, clean model architecture. CA and MBA both assume you'll "pick it up."
- **Nobody taught you to talk to a database.** The data you need lives in an ERP behind a `SELECT` statement, not in a nicely formatted PDF.

Close these five and you are hireable. The rest of this chapter (and book) is how.

## What "proficient" looks like

The bar an employer tests for — what a job-ready person does **without hand-holding**:

- Given a raw GL/trial-balance export, build a **3-statement-linked** or at least a clean P&L model in under a day.
- Write a **variance bridge** (Budget → Actual, explaining each ₹ of the gap) and narrate it in three sentences a CFO understands.
- Pull their own data: a `SUMIFS`/`XLOOKUP` in Excel, a `GROUP BY` in SQL, a `groupby` in pandas.
- Build a **rolling 12-month forecast** with driver-based assumptions (volume × price, headcount × cost), not a flat +10%.
- Produce a **cash-flow / runway** view and know the difference between profit and cash.
- Turn all of it into a **1-page board/MIS deck** with a clear story, not a data dump.
- Know the **calendar**: what's due on working-day 1, 3, 5 of the month.

The FP&A monthly calendar (memorise this — interviewers ask):

| Working day | Activity |
|---|---|
| WD 1–3 | Close: accruals booked, actuals locked by Controller |
| WD 3–4 | FP&A pulls actuals, refreshes model, builds variance vs budget/forecast |
| WD 4–5 | Commentary written, MIS/board deck built |
| WD 5–6 | Business reviews with department heads |
| WD 7–10 | Re-forecast next quarter, update rolling forecast |
| Quarterly | Board pack, re-forecast; Annually: the budget (Aug–Nov cycle) |

## Hands-on: how to actually do it

**1. Get actuals against budget — the workhorse `SUMIFS`.** Given a transaction table (`Data` sheet: Cost Centre in A, Account in B, Month in C, Amount in D):

```excel
=SUMIFS(Data!$D:$D, Data!$B:$B, $A2, Data!$C:$C, F$1)
```
This sums Amount where Account = the row label and Month = the column header — the entire skeleton of an MIS pulls this way.

**2. Look up master data — `XLOOKUP` (or `INDEX/MATCH` for legacy Excel):**

```excel
=XLOOKUP(A2, Master!$A:$A, Master!$C:$C, "NOT MAPPED")
=INDEX(Master!$C:$C, MATCH(A2, Master!$A:$A, 0))
```

**3. The variance bridge column:**

```excel
Variance      =Actual - Budget
Variance %    =IFERROR((Actual-Budget)/Budget, 0)
Fav/Unfav     =IF(AND(N("expense"),Actual>Budget),"Unfav","Fav")
```

**4. Pull the raw data yourself with SQL** (don't wait for IT):

```sql
SELECT cost_centre,
       account_name,
       DATE_TRUNC('month', txn_date) AS period,
       SUM(amount) AS actual
FROM   gl_transactions
WHERE  txn_date >= '2026-04-01'          -- FY26-27 (Indian FY)
GROUP  BY cost_centre, account_name, period
ORDER  BY period, cost_centre;
```

**5. Clean and aggregate in Python** when Excel chokes on volume:

```python
import pandas as pd
gl = pd.read_csv("gl_export.csv")
gl["amount"] = pd.to_numeric(gl["amount"], errors="coerce").fillna(0)
gl["month"]  = pd.to_datetime(gl["txn_date"]).dt.to_period("M")

pivot = (gl.groupby(["cost_centre", "month"])["amount"]
           .sum()
           .unstack(fill_value=0))
pivot["FY_total"] = pivot.sum(axis=1)
pivot.to_excel("actuals_by_cc.xlsx")
```

**6. A driver-based revenue line (DAX for Power BI MIS):**

```dax
Revenue Fcst = SUMX(VALUES(Product[SKU]),
    [Avg Price] * [Forecast Units])

Var to Budget % =
DIVIDE([Actual] - [Budget], [Budget], 0)
```

**7. The accrual journal** FP&A insists Controllers book so the number is complete (electricity bill not yet received, ₹2,00,000):

| Account | Dr | Cr |
|---|---|---|
| Power & Fuel (Expense, P&L) | ₹2,00,000 | |
| Accrued Expenses (Liability, BS) | | ₹2,00,000 |

Reversed next month when the actual invoice lands. Understanding this is why FP&A and accounting can't be separated.

## Worked example / mini-project

**Reproduce this: a monthly MIS for "Nimbus Retail Pvt Ltd" (India), month = Apr-2026.**

Budget vs Actual, ₹ lakh:

| Line | Budget | Actual | Var (₹) | Var % | Comment |
|---|---|---|---|---|---|
| Revenue | 500.0 | 472.0 | (28.0) | -5.6% | 2 stores opened late |
| COGS | 300.0 | 288.9 | 11.1 | fav | in line with volume |
| **Gross Profit** | **200.0** | **183.1** | **(16.9)** | **-8.5%** | GM 38.8% vs 40.0% |
| Employee cost | 70.0 | 74.0 | (4.0) | -5.7% | 3 early hires |
| Rent | 25.0 | 25.0 | 0.0 | — | fixed |
| Marketing | 30.0 | 41.0 | (11.0) | -37% | pulled forward launch spend |
| Other opex | 20.0 | 19.5 | 0.5 | fav | |
| **EBITDA** | **55.0** | **23.6** | **(31.4)** | **-57%** | see bridge |

**The EBITDA bridge (the deliverable a CFO actually reads):**

```
Budget EBITDA                       55.0
  Revenue shortfall (volume)       (11.2)   <- 28 x 40% GM
  Gross margin slip (1.2pt)         (5.7)
  Extra headcount                   (4.0)
  Marketing pull-forward           (11.0)
  Other opex saving                  0.5
Actual EBITDA                       23.6
```

**Three-sentence narrative:** "EBITDA missed by ₹31.4L, but ~₹11L is marketing we deliberately pulled forward and ₹4L is hiring ahead of Q2 — both timing, not structural. The real concern is the ₹17L gross-profit miss from two delayed store openings. Recovery expected from June once stores stabilise." That narrative — not the spreadsheet — is what gets you promoted.

Build it: dump the 8 lines in Excel, add `Var`/`Var %` formulas above, build the bridge as a waterfall chart. Thirty minutes of work; it *is* the job.

## How it's tested

**Interview questions:**
- "Walk me through the three financial statements and how they connect." (cash is the linking answer)
- "Budget vs Actual vs Forecast — what's the difference?" (annual-fixed vs actual vs latest-estimate)
- "You forecast ₹100 revenue, actual is ₹80. How do you investigate?" (decompose: volume vs price vs mix, by segment)
- "Difference between profit and cash?" (working capital, non-cash items, capex)
- "What is a rolling forecast and why use it?"

**Practical tests (increasingly the real filter):**
- **Timed Excel test (30–60 min):** given a raw transaction dump, build a P&L pivot, add variance columns, `XLOOKUP` a mapping table, and write two bullets of commentary. Graded on speed, correct absolute referencing, and no hardcoded numbers.
- **Case / "close these books":** an accrual + prepaid adjustment set, produce adjusted EBITDA.
- **SQL screen:** "write a query for revenue by region by month." A `GROUP BY` with a date filter.
- **Take-home model:** build a 12-month driver-based forecast from assumptions and present a 1-slide recommendation.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Hardcoding numbers inside formulas | Every input is a labelled, coloured (blue) cell; formulas are black |
| Flat "+10%" forecasts | Driver-based: units × price, heads × cost, so you can defend each ₹ |
| Reporting variance without a *why* | Every variance gets a one-line cause: price/volume/mix/timing |
| Confusing profit with cash | Always keep a cash/runway view beside the P&L |
| Circular refs / broken 3-statement links | Iterative calc on; isolate the interest-on-debt circularity |
| Dumping a 40-row table on the CFO | One page, one chart, three sentences, one recommendation |
| Waiting for IT to give data | Learn `SUMIFS`, SQL `GROUP BY`, pandas `groupby` and self-serve |
| Model with no version/date | Filename `MIS_Apr26_v3_2026-05-06.xlsx`; never overwrite last close |

## Learn-it roadmap & resources

**Realistic time-to-proficiency: 3–6 months** of deliberate practice alongside a job or CA prep.

| Weeks | Focus | Milestone |
|---|---|---|
| 1–3 | Excel modelling: `SUMIFS`, `XLOOKUP`, `INDEX/MATCH`, pivots, dynamic arrays | Build the Nimbus MIS unaided |
| 4–6 | 3-statement model + variance bridge | Link IS→BS→CFS, no plugs |
| 7–9 | SQL basics: `SELECT/WHERE/GROUP BY/JOIN` | Pull actuals from a sample DB |
| 10–12 | Power BI/DAX + a driver-based rolling forecast | 1-page live dashboard |
| 13–20 | Python/pandas for cleaning; a DCF/valuation | Portfolio of 3 models |

**Resources:**
- **Free:** Corporate Finance Institute (CFI) free courses; Aswath Damodaran's NYU valuation lectures (YouTube, gold standard); Microsoft/Kaggle SQL & pandas tracks; ICAI study material for the accounting base.
- **Paid/cert:** CFI's **FMVA** (financial modelling), Wall Street Prep / Breaking Into Wall Street for bankers, Coursera Excel-to-BI specialisations. In India, your **CA / CFA** is the credibility layer; FMVA/BIWS is the *skills* layer employers actually test.
- **Practice data:** any company's published annual report — rebuild their P&L and forecast a year forward.

## Quick-reference

| Need | Tool / formula |
|---|---|
| Actual by account & month | `=SUMIFS(amt, acct, $A2, month, F$1)` |
| Map master data | `=XLOOKUP(key, lookup, return, "NA")` |
| Legacy lookup | `=INDEX(ret, MATCH(key, look, 0))` |
| Variance % (safe) | `=IFERROR((Act-Bud)/Bud, 0)` |
| Pull DB data | `SELECT dim, SUM(amt) ... GROUP BY dim` |
| Clean/aggregate big data | `df.groupby("x")["amt"].sum()` |
| BI variance | `DIVIDE([Actual]-[Budget], [Budget], 0)` |
| Accrual entry | Dr Expense / Cr Accrued liability |
| Indian FY | 1 Apr – 31 Mar; label FY26-27 |
| Close cadence | Actuals WD3, variance WD4, deck WD5 |
| Model hygiene | Blue = input, black = formula, never hardcode |
| The deliverable | 1 page, 1 chart, 3 sentences, 1 recommendation |
