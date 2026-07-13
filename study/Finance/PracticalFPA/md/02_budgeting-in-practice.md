# Budgeting in practice

## What it is & where it's used

A budget is the company's financial plan for the next year (usually the fiscal year, in India **1 April to 31 March**) expressed in numbers: how much revenue each product/region will bring, what each department is allowed to spend, and what profit falls out. In practice, "budgeting" is the **annual process** of collecting numbers from every cost-centre owner, challenging them, consolidating them into a single P&L (and often cash flow and balance sheet), getting board sign-off, and then loading the approved figures into the accounting/ERP system so that **actual vs budget (variance)** reporting can run every month.

Roles that live and die by this:

| Role | What they do in budgeting |
|---|---|
| FP&A Analyst | Builds the template, chases cost-centre owners, consolidates, runs variance |
| Finance Business Partner | Sits with a department head (Sales, Marketing, Ops) to build that unit's budget |
| Management Accountant / Cost Accountant | Standard costs, overhead absorption rates, cost-centre allocation |
| Financial Controller | Owns the calendar, reviews, presents to CFO |
| Startup Finance / "Founder's office" | Runway, burn, hiring plan — the same discipline, lighter tooling |

Budgeting sits next to **forecasting** (which re-estimates mid-year) and **planning** (the strategic 3-5 year view). The budget is the *committed baseline* you get judged against.

## The gap: why companies want this (and college didn't teach it)

An MBA teaches you the *master budget* diagram — sales budget → production budget → materials/labour/overhead budgets → cash budget → budgeted P&L. Cost accounting (CA Inter Paper 4) teaches flexed budgets and variance formulas. Both are correct and both are **useless on day one of the job**, because the real work is:

- **Process and people, not formulas.** 80% of budgeting is chasing 15 cost-centre owners for their numbers, handling the ones who pad, and reconciling versions.
- **A working template.** College never makes you build a driver-based Excel model that 12 departments feed into and that rolls up cleanly.
- **Top-down targets vs bottom-up build.** Textbooks present one clean number. Reality: the CEO says "grow EBITDA 20%" (top-down) while cost-centres submit numbers that imply a *loss* (bottom-up). Closing that gap **is** the job.
- **Version control and audit trail.** V1, V2, "final", "final_CFO_v3". Nobody teaches you how not to lose the plot.

Employers pay for the person who can turn a messy set of departmental asks into one board-ready, defendable number — fast, and without breaking the model.

## What "proficient" looks like

A job-ready person can, unaided:

1. Build a **cost-centre budget template** in Excel that a non-finance manager can fill in, with input cells clearly separated from formula cells.
2. Build **revenue bottom-up from drivers** (units × price, or headcount × productivity), not a single typed number.
3. **Consolidate** many cost-centre tabs into one P&L using structured references / `SUMIFS`, so adding a department doesn't break anything.
4. Run a **top-down reconciliation**: show the CEO's target, the bottom-up submission, and the gap, then run scenarios to close it.
5. Produce **budget vs actual variance** with % and a favourable/adverse flag.
6. Manage a **budget calendar** and know who owes what by when.

## Hands-on: how to actually do it

### 1. The cost-centre input template (one tab per department)

Keep **inputs blue, formulas black** — a real convention. Give each owner a driver, not a blank cell.

```
        A                    B         C        D        E        F        G
1  Cost Centre: Marketing   Owner: R.Sharma   CC Code: 5200
2  Line item        Driver           Rate     Qty      Apr...   Total FY   Notes
3  Salaries         headcount        ₹90,000  6        =C3*D3   =E3*12
4  Digital ads      monthly spend    ₹250,000 1        =C4*D4   =E4*12
5  Events           per event        ₹400,000 8        =C5*D5   =E5*12
```

Monthly phasing (seasonality) instead of flat ÷12 — spread an annual number across months using a weight row:

```excel
=$F$6 * INDEX($Weights, MATCH(H$1, $MonthHdr, 0))
```

### 2. Build revenue bottom-up (driver-based)

Never type a revenue number. Model it:

```excel
Revenue = Units_sold * Avg_price
Units_sold (SaaS) = Opening_customers + New - Churned
=SUMPRODUCT(units_row, price_row)     ' mix of products
```

Growth-rate build for a month row (B = prior month, MoM growth in $C$1):

```excel
=B2*(1+$C$1)
```

### 3. Consolidate cost centres into one P&L

Put every cost-centre line into one long **flat table** (`tblBudget`) with columns `CC_Code | Account | Month | Amount`. Then the P&L is just `SUMIFS`:

```excel
=SUMIFS(tblBudget[Amount],
        tblBudget[Account], $A5,
        tblBudget[Month],   B$4)
```

Adding a 16th department = paste more rows, formulas don't change. This is why pros use a flat table, not 15 differently-shaped tabs.

Cross-check the roll-up two ways (belt and braces):

```excel
=SUMIFS(...)                 ' by account
=SUMPRODUCT((tblBudget[CC_Code]=code)*tblBudget[Amount])   ' by cost centre
' the two grand totals MUST tie
```

### 4. Top-down vs bottom-up reconciliation

| | Amount (₹ Cr) |
|---|---|
| CEO target EBITDA (top-down) | 12.0 |
| Bottom-up submission EBITDA | 8.4 |
| **Gap to close** | **3.6** |

Close the gap with a lever table and `Goal Seek` (Data → What-If Analysis → Goal Seek: *Set cell* = EBITDA, *To value* = 12, *By changing* = a cost-cut % or price-uplift cell).

### 5. Variance (budget vs actual), the monthly output

```excel
Variance   =Actual - Budget
Variance % =(Actual-Budget)/Budget
Flag (cost)=IF(Actual<=Budget,"Favourable","Adverse")
Flag (rev) =IF(Actual>=Budget,"Favourable","Adverse")
```

### 6. Same thing in SQL (when data lives in a warehouse)

```sql
SELECT  cc.cost_centre,
        a.account,
        SUM(CASE WHEN f.scenario='BUDGET' THEN f.amount END) AS budget,
        SUM(CASE WHEN f.scenario='ACTUAL' THEN f.amount END) AS actual,
        SUM(CASE WHEN f.scenario='ACTUAL' THEN f.amount END)
      - SUM(CASE WHEN f.scenario='BUDGET' THEN f.amount END) AS variance
FROM    fact_gl f
JOIN    dim_cost_centre cc ON cc.cc_key = f.cc_key
JOIN    dim_account     a  ON a.acc_key = f.acc_key
WHERE   f.fiscal_year = 2027
GROUP BY cc.cost_centre, a.account
ORDER BY variance;
```

### 7. Python — phase an annual budget across 12 months with seasonality

```python
import pandas as pd
weights = pd.Series([0.06,0.06,0.07,0.08,0.08,0.09,
                     0.09,0.09,0.09,0.09,0.10,0.10])   # sums to 1.0
annual = 24_000_000                                    # ₹2.4 Cr
monthly = (annual * weights).round(0)
print(monthly)
```

### 8. Power BI DAX for the dashboard

```dax
Budget      = CALCULATE(SUM(Fact[Amount]), Fact[Scenario]="Budget")
Actual      = CALCULATE(SUM(Fact[Amount]), Fact[Scenario]="Actual")
Variance    = [Actual] - [Budget]
Variance %  = DIVIDE([Variance], [Budget])
```

## Worked example / mini-project

**Company:** *Nirmaan Interiors Pvt Ltd*, a Pune SME. Build FY2027-28 budget. Reproduce this.

**Step 1 — Revenue (bottom-up).** Two streams:

| Stream | Driver | Value | Annual revenue |
|---|---|---|---|
| Residential projects | 40 projects × ₹6,00,000 | | ₹2,40,00,000 |
| Commercial fit-outs | 8 projects × ₹18,00,000 | | ₹1,44,00,000 |
| **Total revenue** | | | **₹3,84,00,000** |

**Step 2 — Direct costs (COGS ~55% of revenue).**

| Item | Basis | ₹ |
|---|---|---|
| Materials | 40% of revenue | 1,53,60,000 |
| Site labour (contract) | 15% of revenue | 57,60,000 |
| **Gross profit** | | **1,72,80,000 (45%)** |

**Step 3 — Cost-centre budgets (overheads).**

| CC | Line | Monthly ₹ | Annual ₹ |
|---|---|---|---|
| Admin (5100) | Salaries (5 staff) | 3,00,000 | 36,00,000 |
| Admin | Office rent | 1,20,000 | 14,40,000 |
| Marketing (5200) | Digital + events | 1,50,000 | 18,00,000 |
| Design (5300) | Software + salaries | 4,00,000 | 48,00,000 |
| **Total overheads** | | | **1,16,40,000** |

**Step 4 — Budgeted P&L.**

| | ₹ |
|---|---|
| Revenue | 3,84,00,000 |
| COGS | (2,11,20,000) |
| Gross profit | 1,72,80,000 |
| Overheads | (1,16,40,000) |
| **EBITDA** | **56,40,000 (14.7%)** |

**Step 5 — Top-down challenge.** CEO wants EBITDA ₹70,00,000. Gap = ₹13,60,000. Levers modelled: +5% price on commercial (₹7,20,000), cut events budget 30% (₹3,00,000), one design hire deferred 6 months (₹3,60,000) → closes ₹13,80,000. Re-run: **EBITDA ₹70,20,000**. Present both versions plus the bridge.

**Step 6 — Month 1 variance.** April actual overheads ₹10,20,000 vs budget ₹9,70,000 → variance ₹50,000 **Adverse (+5.2%)** — flag to Admin owner.

## How it's tested

**Interview questions**
- "Walk me through how you'd build a company's annual budget from scratch." (They want *process + calendar*, not formulas.)
- "Top-down vs bottom-up — which do you use and why?" (Answer: both — bottom-up build, top-down target, reconcile the gap.)
- "A cost-centre owner submits a number ₹20L above last year with no justification. What do you do?"
- "How do you handle version control across 15 departments?"
- "Difference between a fixed and a flexed budget?" (Flexed = re-cast at actual activity level for fair variance.)

**Practical assessments**
- **Timed Excel test (45-60 min):** given a raw cost-centre extract, build a consolidated budget with `SUMIFS`, add a driver-based revenue build, and produce a variance column. They watch for input/formula separation, no hard-coding, and a tie-out.
- **Case:** "Here's the CEO's EBITDA target and the bottom-up submission — close the gap and justify each lever" (often with Goal Seek).
- **Modelling test:** build a 3-scenario (base/best/worst) budget with a scenario switch (`CHOOSE`/`INDEX`).

## Common mistakes & how pros avoid them

| Mistake | How pros avoid it |
|---|---|
| Hard-coding numbers into formulas | Every assumption in a labelled blue input cell |
| ÷12 flat phasing | Seasonality weight row that sums to 100% |
| 15 differently-shaped tabs that won't roll up | One flat table + `SUMIFS`; template locked for owners |
| Typing a revenue number | Driver-based build (units × price, headcount × output) |
| No top-down check | Always show target vs bottom-up vs gap bridge |
| Version chaos ("final_v7") | Dated filenames + a change-log tab; single source of truth |
| Padding / sandbagging by owners | Challenge against prior-year actuals and per-unit ratios |
| Budget ignored after April | Monthly budget-vs-actual pack with variance commentary |
| No cash budget, only P&L | Add a cash/working-capital line — profit ≠ cash |

## Learn-it roadmap & resources

**Time to proficiency:** 6-10 weeks part-time if you already know Excel basics.

| Weeks | Focus |
|---|---|
| 1-2 | Excel for FP&A: `SUMIFS`, `INDEX/MATCH`, `XLOOKUP`, tables, data validation |
| 3-4 | Build a driver-based revenue model + cost-centre template |
| 5-6 | Consolidation, top-down/bottom-up reconciliation, Goal Seek, scenarios |
| 7-8 | Variance reporting + a Power BI / DAX dashboard |
| 9-10 | End-to-end mock budget for a fictional company (portfolio piece) |

**Resources**
- CA Inter Cost & Management Accounting — *Budgets & Budgetary Control* chapter (free ICAI module) for the theory backbone.
- CFI *FP&A* / *Budgeting & Forecasting* course (paid) — job-shaped.
- Corporate Finance modelling on YouTube (free): "driver-based budgeting", "budget vs actual dashboard Power BI".
- Practise on real templates: build the *Nirmaan Interiors* example above yourself.

**Certifications:** CMA (India) or CMA (US) both weight budgeting heavily; CFI **FMVA** is the practical badge recruiters recognise for FP&A.

## Quick-reference

| Need | Formula / step |
|---|---|
| Consolidate cost centres | `=SUMIFS(tbl[Amount], tbl[Account],A5, tbl[Month],B$4)` |
| Revenue from mix | `=SUMPRODUCT(units, price)` |
| MoM growth | `=Prior*(1+growth%)` |
| Phase annual → months | `annual * weight_row` (weights sum to 1) |
| Variance | `=Actual-Budget` |
| Variance % | `=(Actual-Budget)/Budget` |
| Cost flag | `=IF(Actual<=Budget,"Fav","Adv")` |
| Close top-down gap | Data → What-If → **Goal Seek** |
| Scenario switch | `=CHOOSE(switch, base, best, worst)` |
| DAX variance | `Variance = [Actual]-[Budget]` |

**Golden rules:** FY = Apr-Mar · inputs blue, formulas black · never hard-code · build revenue from drivers · one flat table, not 15 tabs · always reconcile top-down vs bottom-up · budget is worthless without monthly variance.

**Typical budget calendar (SME/mid-market):**

| When | Milestone |
|---|---|
| Nov | CFO issues assumptions + top-down targets, template out |
| Early Dec | Cost-centre owners submit bottom-up (V1) |
| Mid Dec | FP&A consolidates, first gap-to-target review |
| Late Dec | Iterations V2/V3, lever decisions |
| Jan | CFO / board review and sign-off |
| Feb-Mar | Load approved budget into ERP; lock baseline |
| Apr | Year starts; first budget-vs-actual pack |
