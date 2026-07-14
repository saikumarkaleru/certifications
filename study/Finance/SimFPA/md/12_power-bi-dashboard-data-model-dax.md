# Building the Power BI Dashboard Behind the Pack

## The ask

It's **14 July 2026**. Your MIS pack for Q1 (the Excel workbook with the P&L, the variance bridge, and a cover memo) went out last week and the CFO liked it. But this morning she forwards you an email from the Managing Director:

> "The Excel pack is fine for the finance team, but I want to *see* the numbers on my phone. Revenue vs budget, margin trend, top variances — one screen, refreshes itself. The board meets on the 28th. Can you build it in Power BI?"

The CFO adds one line: *"Same numbers as the pack. If the dashboard and the workbook ever disagree, we look like amateurs."*

So the deadline is **Fri 25 July** (dry-run with CFO), board on the 28th. The real job: take the same actuals + budget that feed the Excel MIS and turn them into a Power BI report with a proper data model — not a pile of visuals stuck on a flat table.

## What you're given

Two data sources, both exports you already use for the pack.

**1. Actuals — from Tally, exported monthly as a "GL transaction" CSV** (`Fact_Actuals`). One row per posting, already tagged with an account code and a segment:

| Date | AccountCode | Segment | Amount (Rs) |
|---|---|---|---|
| 2026-04-30 | 4000 (Revenue) | Goods | 3,00,00,000 |
| 2026-04-30 | 4000 (Revenue) | Services | 1,00,00,000 |
| 2026-04-30 | 5000 (COGS) | Goods | -2,25,00,000 |
| ... | ... | ... | ... |

**2. Budget — the FY2026-27 annual budget, phased to months** (`Fact_Budget`), same grain:

| Month | AccountCode | Segment | Amount (Rs) |
|---|---|---|---|
| 2026-04 | 4000 | Goods | 3,00,00,000 |
| 2026-04 | 4000 | Services | 1,00,00,000 |
| ... | ... | ... | ... |

Reconciliation anchors both must hit for the full year: **Revenue Rs 12.00 cr** (Goods 9.00 + Services 3.00), **COGS Rs 8.40 cr**, **Gross Profit Rs 3.60 cr (30%)**, EBIT Rs 1.596 cr, PAT ~Rs 1.11 cr. Q1: budget revenue **Rs 2.85 cr**, actual **Rs 2.70 cr**.

## Build it — step by step

### Step 1 — model shape: star schema, not one fat table

The rookie move is to load one wide table and slice it. The professional move is a **star schema**: two skinny *fact* tables (Actuals, Budget) surrounded by shared *dimension* tables. Dims are what you filter and group by; facts hold the numbers.

```
                 ┌──────────────┐
                 │   Dim_Date   │
                 │ Date, Month, │
                 │ Qtr, FY      │
                 └──────┬───────┘
                        │ (1)
          ┌─────────────┼─────────────┐
          │ (*)                    (*)│
   ┌──────┴──────┐            ┌───────┴──────┐
   │ Fact_Actuals│            │  Fact_Budget │
   │ Date,Acct,  │            │ Date,Acct,   │
   │ Segment,Amt │            │ Segment,Amt  │
   └──────┬──────┘            └───────┬──────┘
          │ (*)                   (*)│
     ┌────┴─────┐   ┌───────────┐    │
     │Dim_Account│  │Dim_Segment│────┘
     │Code,Name, │  │ Goods /   │
     │Group,Sort │  │ Services  │
     └───────────┘  └───────────┘
```

- **Dim_Date** — a proper calendar from 01-Apr-2026 to 31-Mar-2027, with columns `Date, MonthName, MonthNo, Quarter (Q1..Q4), FY`. Mark it as the date table.
- **Dim_Account** — maps code 4000 → "Revenue" → group "Income", 5000 → "COGS" → group "COGS", etc., plus a `SortOrder` so the P&L lines show in P&L order, not alphabetically.
- **Dim_Segment** — Goods / Services.

Both facts join to all three dims on a **single-direction, one-to-many** relationship (the "1" side is the dim). Two fact tables sharing dims is the classic budget-vs-actual pattern; the shared dims are what let one slicer filter both.

### Step 2 — load & shape in Power Query

Get Data → CSV for each. In Power Query:
- Set data types (Date as Date, Amount as Decimal).
- In `Fact_Budget`, the month is text `2026-04`; convert to a real date (first of month) so it joins to Dim_Date.
- Build `Dim_Date` with `= List.Dates(#date(2026,4,1), 365, #duration(1,0,0,0))` then add the Quarter/FY columns.
- Build `Dim_Account` as a small entered table (7-8 rows) — faster than deriving it.

### Step 3 — the DAX measures

Everything downstream is measures, never calculated columns on the facts. Base measures first, then everything is built from them.

```DAX
Actual = SUM ( Fact_Actuals[Amount] )

Budget = SUM ( Fact_Budget[Amount] )

Variance = [Actual] - [Budget]

Variance % =
DIVIDE ( [Variance], [Budget] )        -- DIVIDE avoids /0 errors
```

Because COGS is stored as a negative, a favourable/unfavourable sign flip matters — so for cost/expense lines you want a "signed for the P&L" view. Two clean ways: store costs negative and just SUM (P&L nets naturally), or add a variance-direction helper. Keep it simple: costs negative, revenue positive, `[Actual]` sums the true P&L line.

```DAX
Revenue =
CALCULATE ( [Actual], Dim_Account[Group] = "Income" )

Gross Profit =
CALCULATE ( [Actual], Dim_Account[Group] IN { "Income", "COGS" } )

GM % =
DIVIDE ( [Gross Profit], [Revenue] )

Revenue Budget =
CALCULATE ( [Budget], Dim_Account[Group] = "Income" )

Revenue Var % =
DIVIDE ( [Revenue] - [Revenue Budget], [Revenue Budget] )
```

Time intelligence — YTD and prior-period, which the board always wants:

```DAX
Actual YTD =
TOTALYTD ( [Actual], Dim_Date[Date], "31-03" )   -- fiscal year-end 31 Mar

Revenue YTD =
TOTALYTD ( [Revenue], Dim_Date[Date], "31-03" )

Budget YTD =
TOTALYTD ( [Budget], Dim_Date[Date], "31-03" )
```

A conditional-format helper so unfavourable variances go red automatically:

```DAX
Variance Colour =
VAR v = [Variance]
RETURN
IF ( v < 0, "#C0392B", "#1E8449" )   -- red if below budget, green if above
```

That's 10 measures. Notice none of them hard-code "Q1" or a segment — the slicers and the row context of each visual supply that, which is exactly why the star schema pays off.

### Step 4 — sanity tie to Excel

Before building visuals, drop `[Revenue]` and `[Revenue Budget]` into a card with the Quarter slicer on Q1. You must see **Rs 2.70 cr** actual and **Rs 2.85 cr** budget. `[GM %]` on Q1 must read **28.5%**. Full-year `[Revenue]` = **12.00 cr**, `[Gross Profit]` = **3.60 cr**. If any of these are off, the model is wrong — fix it now, not after 12 charts are built.

## The deliverable

Two report pages.

**Page 1 — "Board Summary"** (the MD's phone screen):

| Zone | Visual | Measures |
|---|---|---|
| Top KPI row | 4 cards | Revenue, Var %, GM %, EBIT (all YTD) |
| Left | Clustered column: Actual vs Budget by month | Actual, Budget |
| Right | Line: GM % trend by month vs 30% target line | GM % |
| Bottom | Bar: Variance by P&L line (sorted, red/green) | Variance + Variance Colour |
| Filters | Slicers: Quarter, Segment | — |

**Page 2 — "P&L Detail"**: a matrix — rows = Dim_Account (sorted by SortOrder), columns = Actual, Budget, Variance, Variance %, with the Quarter/Segment slicers carried across via *Sync slicers*.

Commentary in analyst voice, pinned as a text box: *"Q1 revenue Rs 2.70 cr, Rs 15 lakh (-5%) below budget, driven by a goods-volume miss (21,000 vs 22,500 units) partly cushioned by firmer pricing (ASP Rs 1,020 vs 1,000). Gross margin 28.5% vs 30% on mix and input cost. Services on plan. FY guidance unchanged pending Q2."*

Set a **scheduled refresh** (Power BI Service, 8am daily) pointed at the same CSV/gateway folder finance drops the Tally export into — so it self-updates, which is the whole point of the ask.

## How it's reviewed

The CFO/controller checks:
1. **Tie-out first.** Card totals must equal the Excel pack to the rupee — Q1 Rs 2.70 cr, GM 28.5%, FY 12.00 cr. This is the trust test.
2. **Sign logic.** Is an over-budget *cost* shown red (bad) not green? Revenue below budget red? Get the direction right per line.
3. **Slicer behaviour.** Pick "Services" — does *every* visual respond, and does the number reconcile (Services Rs 3.00 cr FY, on plan in Q1)?
4. **Blank/zero handling.** Months with no data show blank, not error; DIVIDE prevents #DIV/0.
5. **Refresh actually works** end-to-end from the gateway, not just on your laptop.

## Common mistakes & red flags

- **One flat table.** Works for 3 charts, collapses when you add budget, prior year, or a second segment. Star schema from day one.
- **Calculated columns instead of measures.** A column can't respond to a slicer's filter context the way a measure does, and it bloats the model.
- **Bi-directional relationships "to make it work."** Almost always a sign the model is wrong; keep single-direction dim→fact.
- **Two date columns, no Dim_Date.** Time intelligence (TOTALYTD) needs one marked date table shared by both facts.
- **Not using DIVIDE** — a single zero-budget line throws #DIV/0 and the whole visual errors on the board screen.
- **Dashboard disagreeing with the pack** by even a rupee — instant credibility loss. Tie out before you style anything.

## On the job & in the interview

The "why": a dashboard isn't decoration — it's the *same governed numbers* in a self-refreshing, drill-able form. FP&A owns the semantic layer (the measures), so the definition of "Gross Margin %" lives in one place and can't drift. Jargon to own: **star schema, fact vs dimension, grain, filter context, measure vs calculated column, semantic model, RLS (row-level security), scheduled refresh**.

**Q: "Why a star schema and not just one table?"**
A: "Facts hold the numbers at a single grain; dims hold the things I filter and group by. Separating them lets one slicer — say Segment — filter both my actuals and budget facts through shared dimensions, keeps the model small, and makes DAX behave predictably via filter context. A flat table can't cleanly do actual-vs-budget or time intelligence."

**Q: "Walk me through a variance measure in DAX."**
A: "Base measures `Actual = SUM(Fact_Actuals[Amount])` and `Budget = SUM(Fact_Budget[Amount])`, then `Variance = [Actual]-[Budget]` and `Variance % = DIVIDE([Variance],[Budget])`. DIVIDE handles zero budgets gracefully. Every visual reuses these, so Q1's -Rs 15 lakh / -5% falls straight out of the Quarter slicer's filter context — I never hard-code the period."

**Q: "How do you make sure it matches the Excel MIS?"**
A: "I tie out before styling: cards for Revenue, GM%, EBIT at Q1 and full year against the pack — Rs 2.70 cr, 28.5%, and the FY 12.00 cr / 3.60 cr anchors. If a number's off, the model's wrong. A dashboard that disagrees with the pack is worse than no dashboard."
