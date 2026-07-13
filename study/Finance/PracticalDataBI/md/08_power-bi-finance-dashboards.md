# Power BI II: Finance Dashboards

## What it is & where it's used

Chapter 07 covered the plumbing — Power Query, the star schema, the DAX basics. This chapter is where you turn that model into the three deliverables a finance team actually asks for: a **P&L (Profit & Loss) dashboard**, a **budget-vs-actual (BvA) variance report**, and a **KPI scorecard** — plus the two features that separate a "chart-maker" from a "BI person": **drill-through** and **row-level security (RLS)**.

Who builds these:

| Role | What they ship in Power BI |
|---|---|
| FP&A analyst | Monthly BvA pack, rolling forecast, KPI board for the CFO |
| Management accountant | Cost-centre P&L, margin analysis, drill-through to cost lines |
| Financial analyst / MIS | Revenue/AR/AP dashboards, DSO/DPO trends |
| Controller / Finance Manager | Board deck built off one governed dataset, RLS by entity/region |
| Business finance partner | Region- or product-level P&L where each manager sees only their slice |

In Indian companies (and MNC GCCs in Bengaluru/Hyderabad/Pune), the "monthly MIS pack" is very often a Power BI report refreshed off the ERP (SAP, Oracle, Tally exports, or a data warehouse). If you can own that pack, you are the finance-tech hire they cannot easily replace.

## The gap: why companies want this (and college didn't teach it)

MBA and CA syllabi teach you to *read* a P&L and *compute* a variance. They stop there. Industry needs someone who can:

- Turn a raw ledger dump (10 lakh rows) into a **refreshable, filterable P&L** — not a static Excel that breaks every month-end.
- Build **variance % and favourable/adverse flags** that update automatically when a controller drops in new actuals.
- Let a Regional Head click a total and **drill through to the transactions behind it** without pinging the analyst.
- Show the **Sales VP only the South zone** and the **Finance Head everything** — from *one* report, using RLS, instead of maintaining 6 separate files.

College teaches the *accounting*; the employer pays for the *delivery mechanism*. Nobody in a BCom/MBA classroom builds a `DIVIDE()` variance measure or writes a DAX RLS filter. That is exactly the arbitrage.

## What "proficient" looks like

A job-ready person can, unaided:

1. Build a **date-intelligence P&L** with subtotals (Revenue → Gross Profit → EBITDA → PBT) using measures, not hard-coded columns.
2. Write **variance measures** (Actual − Budget, Var %, favourable/adverse) that respect the sign convention (over-spend on cost is *adverse*, over-shoot on revenue is *favourable*).
3. Configure **drill-through** so right-click → "See transactions" jumps to a filtered detail page.
4. Set up **RLS roles**, write the DAX filter, and **test via "View as role."**
5. Use **conditional formatting** (red/green) and **KPI cards** that a CFO can read in 10 seconds.
6. Schedule a **refresh** and know the difference between Import and DirectQuery.

## Hands-on: how to actually do it

### Data model assumed

Star schema from Chapter 07:
- `Fact_GL` (Date, AccountKey, CostCentreKey, Amount, Scenario) — Scenario = "Actual" or "Budget"
- `Dim_Account` (AccountKey, Account, PLGroup, PLGroupSort, SignConvention)
- `Dim_Date`, `Dim_CostCentre` (CostCentreKey, CostCentre, Region, Manager, ManagerEmail)

### 1. Core P&L measures (DAX)

```dax
Actual =
CALCULATE ( SUM ( Fact_GL[Amount] ), Fact_GL[Scenario] = "Actual" )

Budget =
CALCULATE ( SUM ( Fact_GL[Amount] ), Fact_GL[Scenario] = "Budget" )

-- Revenue and cost stored with natural signs (revenue +, expense −)
Revenue =
CALCULATE ( [Actual], Dim_Account[PLGroup] = "Revenue" )

Gross Profit =
CALCULATE ( [Actual],
    Dim_Account[PLGroup] IN { "Revenue", "COGS" } )

EBITDA =
CALCULATE ( [Actual],
    NOT Dim_Account[PLGroup] IN { "Depreciation", "Interest", "Tax" } )
```

Build the P&L statement itself with a **Matrix visual**: `Dim_Account[PLGroup]` on rows (sorted by `PLGroupSort`), `[Actual]` and `[Budget]` on values. This gives you a real statement layout instead of a bar chart.

### 2. Budget-vs-Actual variance

```dax
Variance = [Actual] - [Budget]

Variance % =
DIVIDE ( [Actual] - [Budget], [Budget] )   -- DIVIDE avoids /0 error

-- Sign-aware flag: cost overrun is adverse, revenue beat is favourable
Var Status =
VAR IsRevenue =
    SELECTEDVALUE ( Dim_Account[SignConvention] ) = "Income"
VAR Fav = IF ( IsRevenue, [Variance] >= 0, [Variance] <= 0 )
RETURN IF ( Fav, "Favourable", "Adverse" )
```

**Conditional formatting** on the Variance column: Format → Cell elements → Background color → *Rules* → if `Var Status` = "Adverse" then red, else green. Now the CFO sees the problem lines instantly.

### 3. KPI measures & cards

```dax
Gross Margin % = DIVIDE ( [Gross Profit], [Revenue] )

EBITDA Margin % = DIVIDE ( [EBITDA], [Revenue] )

-- Month-over-month growth using the date dimension
Revenue MoM % =
VAR Prev =
    CALCULATE ( [Revenue], DATEADD ( Dim_Date[Date], -1, MONTH ) )
RETURN DIVIDE ( [Revenue] - Prev, Prev )

Budget Achievement % = DIVIDE ( [Actual], [Budget] )
```

Drop each into a **Card** or **KPI visual**. For the KPI visual: Value = `[Revenue]`, Target = `[Budget]`, Trend axis = `Dim_Date[Month]`.

### 4. Drill-through

1. Add a new page, rename it `Transaction Detail`.
2. In the **Visualizations → Drill through** well, drag the field you want to drill *by*, e.g. `Dim_Account[Account]` (and/or `Dim_CostCentre[CostCentre]`).
3. Power BI auto-adds a "back" button. Put a Table visual on the page: Date, Account, Cost Centre, Amount, Voucher No.
4. On the summary P&L page, **right-click any total → Drill through → Transaction Detail.** The detail page opens filtered to that account.
5. Toggle **"Keep all filters" = On** so region/month context carries over.

### 5. Row-level security (RLS)

```
Modeling tab → Manage roles → Create
```

Role: **Region_Manager**

```dax
-- Filter Dim_CostCentre so each user sees only their region
[Region] =
    LOOKUPVALUE (
        UserMap[Region],
        UserMap[Email], USERPRINCIPALNAME ()
    )
```

Or the simpler "manager sees own cost centres" pattern:

```dax
-- Applied on Dim_CostCentre
Dim_CostCentre[ManagerEmail] = USERPRINCIPALNAME ()
```

Test before publishing: **Modeling → View as → tick Region_Manager**, optionally enter a test email under "Other user." The whole report re-filters. After **Publish**, in the Power BI Service go to the dataset → **Security** → add the Azure AD users/groups to the role. Without that last step, RLS does nothing in the Service.

> One `USERPRINCIPALNAME()` returns the logged-in user's email — that is what makes one report serve 50 managers.

## Worked example / mini-project

**Scenario:** "Bharat Consumer Products Pvt Ltd" — FY 2025-26, three regions. You are handed a GL export. Reproduce this in ₹ lakhs.

`Fact_GL` (sample, Actual scenario, April):

| Date | Account | PLGroup | CostCentre | Region | Scenario | Amount (₹ L) |
|---|---|---|---|---|---|---|
| 2025-04-30 | Product Sales | Revenue | CC-North | North | Actual | 420 |
| 2025-04-30 | Product Sales | Revenue | CC-South | South | Actual | 510 |
| 2025-04-30 | Raw Material | COGS | CC-North | North | Actual | −250 |
| 2025-04-30 | Raw Material | COGS | CC-South | South | Actual | −290 |
| 2025-04-30 | Salaries | Employee | CC-Head | HO | Actual | −95 |
| 2025-04-30 | Freight | Distribution | CC-North | North | Actual | −38 |

Budget rows exist with Scenario = "Budget" (e.g. North Sales budget 400, South 480).

**Build the P&L matrix** (South region slicer applied):

| P&L line | Actual | Budget | Variance | Var % | Status |
|---|--:|--:|--:|--:|---|
| Revenue | 510 | 480 | +30 | +6.3% | Favourable |
| COGS | −290 | −270 | −20 | +7.4% | Adverse |
| **Gross Profit** | **220** | **210** | **+10** | **+4.8%** | Favourable |
| Distribution | −22 | −20 | −2 | +10% | Adverse |
| **EBITDA (region)** | **198** | **190** | **+8** | **+4.2%** | Favourable |

**KPI cards:** Gross Margin % = 220/510 = **43.1%**; Budget Achievement (Rev) = 510/480 = **106.3%**.

**Drill-through demo:** the Regional Head clicks the COGS −290, drills through, and sees the Raw Material vouchers making up that number — spots that one supplier invoice caused the ₹20 L overrun.

**RLS demo:** publish with role `Region_Manager` on `ManagerEmail = USERPRINCIPALNAME()`. The South manager logs in → the entire report shows only 510 revenue, never North's 420. The Finance Head is in no role → sees the consolidated ₹930 revenue.

Reproduce it: paste the two tables into Excel, load via Get Data → Excel, mark `Dim_Date`, write the six measures above, and you have a working pack in ~30 minutes.

## How it's tested

**Interview questions:**
- "How do you build a P&L in Power BI without hard-coding rows for each line item?" (Answer: measures + Account dimension with a sort/group column.)
- "Actuals came in over budget on marketing spend — how does your report show that as *adverse* while a revenue beat shows *favourable*?" (Sign convention logic.)
- "Difference between a slicer filter and RLS?" (Slicer = user choice, removable; RLS = enforced at dataset, user cannot bypass.)
- "Import vs DirectQuery — which for a monthly MIS pack?" (Import; faster, scheduled refresh.)
- "What does `USERPRINCIPALNAME()` return and why does it matter for RLS?"

**Practical/assessment test:** Very common — a 45–60 min take-home or on-site. Typical brief: *"Here's a GL extract and a budget file. Build a P&L with Actual/Budget/Variance, add a Gross Margin KPI card, enable drill-through to transactions, and create an RLS role so a region manager sees only their region. Publish and share a test link."* They grade: correct variance signs, no `/0` errors, working drill-through, and — the pass/fail line — whether RLS actually restricts data when they "View as role."

## Common mistakes & how pros avoid them

| Mistake | Fix |
|---|---|
| Hard-coding P&L rows as separate measures per line | Use one Account dimension + PLGroup + sort column; drive rows dynamically |
| `Variance % = Var / Budget` throwing errors on zero budget | Always use `DIVIDE()` |
| Variance sign wrong (cost overrun shown green) | Store a `SignConvention` and build a sign-aware `Var Status` |
| Building 6 separate files, one per region | One dataset + RLS |
| Forgetting to add users to the role in the Service | RLS in Desktop alone does nothing; assign members under dataset → Security |
| Totals in matrix look wrong ("the total isn't the sum of rows") | That's measure context — verify with a test filter, don't "fix" by summing columns |
| Drill-through page not filtered | Ensure the drill-by field is in the Drill through well and "Keep all filters" is On |
| Refresh fails after month-end | Use a parameterised folder/date path in Power Query, not a fixed filename |

## Learn-it roadmap & resources

**Time to proficient:** ~3–4 weeks part-time if you already did Chapter 07's modelling.

| Week | Focus |
|---|---|
| 1 | P&L matrix + core measures; conditional formatting |
| 2 | Budget-vs-Actual, DIVIDE, sign-aware variance, KPI cards |
| 3 | Drill-through, bookmarks, tooltips, a clean CFO-ready layout |
| 4 | RLS (static + dynamic), publish to Service, scheduled refresh |

**Resources:**
- Microsoft Learn — "Power BI data analyst" learning path (free).
- SQLBI (Marco Russo / Alberto Ferrari) — free articles/YouTube on variance, RLS, time intelligence. The gold standard for DAX.
- Book: *The Definitive Guide to DAX* (Russo & Ferrari) for depth.
- **Certification:** Microsoft **PL-300: Power BI Data Analyst Associate** — the one recruiters recognise; covers modelling, DAX, RLS, and publishing. ~₹4,800 exam fee in India, strongly worth listing on your CV.

## Quick-reference

```dax
Actual   = CALCULATE(SUM(Fact_GL[Amount]), Fact_GL[Scenario]="Actual")
Budget   = CALCULATE(SUM(Fact_GL[Amount]), Fact_GL[Scenario]="Budget")
Variance = [Actual] - [Budget]
Var %    = DIVIDE([Actual]-[Budget], [Budget])
GM %     = DIVIDE([Gross Profit], [Revenue])
MoM %    = DIVIDE([Revenue]-CALCULATE([Revenue],DATEADD(Dim_Date[Date],-1,MONTH)),
                  CALCULATE([Revenue],DATEADD(Dim_Date[Date],-1,MONTH)))
RLS      = Dim_CostCentre[ManagerEmail] = USERPRINCIPALNAME()
```

| Task | Click-path |
|---|---|
| P&L layout | Matrix visual → PLGroup on Rows, Actual/Budget on Values |
| Red/green variance | Format → Cell elements → Background color → Rules |
| Drill-through | Detail page → drag field to *Drill through* well → right-click total on summary |
| Create RLS role | Modeling → Manage roles → new role → DAX filter |
| Test RLS | Modeling → View as → tick role |
| Activate RLS live | Service → dataset → Security → add users to role |
| Refresh | Service → dataset → Schedule refresh (Import mode) |

**Sign rule:** Income favourable when Actual ≥ Budget; Expense favourable when Actual ≤ Budget. Always `DIVIDE()`, never `/`. One dataset + RLS beats many files, every time.
