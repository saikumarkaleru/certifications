# The FP&A Tech Stack

## What it is & where it's used

The FP&A tech stack is the set of tools a finance team uses to *collect actuals, build a plan, and report the variance between the two*. In 90% of Indian companies — from a ₹50 crore manufacturer to the finance shared-service centre of an MNC — that stack is still **Excel plus a source system** (Tally, SAP, Oracle NetSuite, or Zoho Books). As the company scales, a dedicated **planning tool** (Anaplan, Workday Adaptive Planning, Datarails, Oracle EPM Cloud, Board) is layered on top to kill the spreadsheet chaos.

You will touch this stack in almost every finance role:

| Role | What they do with the stack |
|---|---|
| FP&A analyst | Builds the budget model, monthly forecast, variance decks |
| Business finance partner | Slices margin by product/region, runs scenarios |
| Financial reporting / controllership | Feeds actuals from the ERP into the plan |
| Corporate development / strategy | Long-range plans, M&A models |
| Startup finance (fractional CFO) | Runs the whole thing in one Excel/Google Sheets model |

The uncomfortable truth: **the tool is a means, not the skill.** Employers pay for someone who can design a driver-based model and *decide* when a spreadsheet has outgrown its usefulness. This chapter teaches both.

## The gap: why companies want this (and college didn't teach it)

An MBA or CA course teaches you to *read* financial statements and to *value* a business. It never makes you *build the machine that produces a forecast every month*. The gaps employers complain about:

1. **You know accounting, not modelling.** You can pass a consolidation question but can't build a three-statement model that flexes when volume changes.
2. **You've never seen "version hell."** College models are one-shot. Real FP&A runs Budget v1, v2, Reforecast Q2, Actuals — and someone always emails `Budget_FINAL_v3_USE_THIS.xlsx`. You've never felt that pain, so you don't respect the tools built to solve it.
3. **You don't know the data plumbing.** Actuals live in the ERP at transaction-level with 400 GL codes. The plan is at product-line level. Nobody taught you the *mapping* between them — the single hardest, most valuable FP&A skill.
4. **You've never justified a ₹40 lakh/year software purchase.** Knowing *when* to move off Excel and *how to say so to a CFO* is a promotion-grade skill.

Closing this gap is what turns a "reporting analyst" into an "FP&A lead."

## What "proficient" looks like

A job-ready person can, unaided:

- Build a **driver-based P&L** in Excel where changing one assumption (say, price per unit) ripples correctly through revenue, COGS, GST, and EBITDA.
- Pull actuals from an ERP export and **reconcile them to the plan** using a mapping table, not manual retyping.
- Explain a **variance** in business terms: "EBITDA missed by ₹1.2 Cr — ₹80 L volume, ₹40 L price/mix."
- Articulate the **EPM value chain**: model → data integration → workflow → reporting.
- Give a crisp answer to *"When do we move off Excel onto Anaplan/Adaptive?"* with real triggers, not vibes.
- Use structured references, `SUMIFS`, `XLOOKUP`, and dynamic arrays — no hard-coded cell soup.

## Hands-on: how to actually do it

### Excel: the driver-based revenue block

Never hard-code revenue. Build it from drivers so it flexes.

```
Assumptions (named cells / a Assumptions tab):
  Price_Unit   = 1200      (₹ per unit)
  Vol_Growth   = 0.03      (3% MoM)
  Units_Jan    = 10000

Month row  :  Jan      Feb                 Mar ...
Units (B5) :  =Units_Jan   =B5*(1+Vol_Growth)   =C5*(1+Vol_Growth)
Revenue    :  =B5*Price_Unit
```

### XLOOKUP for the GL-to-plan mapping (replaces VLOOKUP)

Your ERP export has GL codes; your plan needs line items. Map them once:

```excel
=XLOOKUP([@GLCode], MapTable[GLCode], MapTable[PlanLine], "UNMAPPED")
```

The `"UNMAPPED"` flag is deliberate — any new GL the ERP throws at you surfaces instead of silently dropping out of the P&L.

### SUMIFS to aggregate actuals to the plan grain

```excel
=SUMIFS(GL[Amount], GL[PlanLine], $A2, GL[Month], B$1, GL[Entity], "IN01")
```

### Variance and % variance, protected against divide-by-zero

```excel
Variance    =Actual - Budget
Var %       =IFERROR((Actual-Budget)/ABS(Budget), "n/m")
```

### Python: pull the ERP CSV, map it, pivot to a plan-ready grid

When the export is 200k rows, Excel chokes. Pandas doesn't.

```python
import pandas as pd

gl  = pd.read_csv("gl_actuals_apr26.csv")           # TransID, GLCode, Amount, Month, Entity
mp  = pd.read_csv("gl_plan_map.csv")                # GLCode, PlanLine

df  = gl.merge(mp, on="GLCode", how="left")
unmapped = df[df["PlanLine"].isna()]["GLCode"].unique()
print("UNMAPPED GLs (fix the map!):", unmapped)

pivot = (df.dropna(subset=["PlanLine"])
           .pivot_table(index="PlanLine", columns="Month",
                        values="Amount", aggfunc="sum", fill_value=0))
pivot.to_excel("actuals_planready.xlsx")
```

### SQL: the same aggregation straight from the warehouse

If actuals sit in a database, skip the export entirely:

```sql
SELECT m.plan_line,
       g.period,
       SUM(g.amount) AS actual_amt
FROM   gl_transactions g
JOIN   gl_plan_map    m ON g.gl_code = m.gl_code
WHERE  g.entity = 'IN01'
  AND  g.period BETWEEN '2026-04' AND '2026-06'
GROUP  BY m.plan_line, g.period
ORDER  BY m.plan_line, g.period;
```

### DAX: a variance measure in Power BI / EPM reporting

```dax
Variance =
VAR bud = CALCULATE([Amount], 'Scenario'[Name] = "Budget")
VAR act = CALCULATE([Amount], 'Scenario'[Name] = "Actual")
RETURN act - bud

Variance % =
DIVIDE([Variance], CALCULATE([Amount], 'Scenario'[Name] = "Budget"))
```

### What a planning tool (Adaptive / Anaplan) does that Excel can't

In Adaptive or Anaplan the same driver model becomes a **multi-dimensional cube**: `Account × Time × Entity × Product × Version`. You write one formula on a line item and it applies across every intersection. Key mechanics you'll use:

- **Versions**: Budget, Forecast, Actual are first-class — no `_v3_FINAL` files.
- **Data integration**: a scheduled connector loads ERP actuals nightly, auto-mapped.
- **Workflow**: each cost-centre owner enters their numbers; a submit/approve chain locks them.
- **Audit trail**: every cell change is logged with who/when.

## Worked example / mini-project

**Reproduce this.** You are FP&A for a mid-size FMCG distributor. Build the April FY27 flash.

Assumptions:

| Driver | Value |
|---|---|
| Opening units/month | 50,000 |
| Price per unit | ₹250 |
| Gross margin | 32% |
| Fixed opex/month | ₹28,00,000 |
| GST rate (output) | 18% |

Budget P&L (April):

| Line | Formula | Amount (₹) |
|---|---|---|
| Revenue | 50,000 × 250 | 1,25,00,000 |
| COGS | Revenue × 68% | 85,00,000 |
| Gross profit | Rev − COGS | 40,00,000 |
| Fixed opex | given | 28,00,000 |
| **EBITDA** | GP − opex | **12,00,000** |

Now actuals come in from Tally: units sold **46,000**, realised price **₹258** (price hike stuck), COGS ₹82.1 L, opex ₹29.2 L.

| Line | Budget | Actual | Variance | Driver |
|---|---|---|---|---|
| Units | 50,000 | 46,000 | −4,000 | volume |
| Price | 250 | 258 | +8 | price |
| Revenue | 1,25,00,000 | 1,18,68,000 | −6,32,000 | see below |
| COGS | 85,00,000 | 82,10,000 | +2,90,000 (fav) | |
| Gross profit | 40,00,000 | 36,58,000 | −3,42,000 | |
| Opex | 28,00,000 | 29,20,000 | −1,20,000 | |
| **EBITDA** | 12,00,000 | 7,38,000 | **−4,62,000** | |

**Price-volume bridge on revenue** (the answer a CFO wants):

```
Volume effect = (46,000 − 50,000) × ₹250        = −10,00,000
Price effect  = (₹258 − ₹250) × 46,000           = +3,68,000
Net revenue variance                              = −6,32,000  ✓
```

The story: *"Revenue missed ₹6.3 L — we lost ₹10 L on volume (4,000 fewer units) but recovered ₹3.7 L on the price increase. EBITDA fell ₹4.6 L, mostly volume-driven plus a ₹1.2 L opex overrun."* That one sentence is the entire job.

Journal entry for the recognised April sales (net of the price realised):

| Account | Dr (₹) | Cr (₹) |
|---|---|---|
| Trade Receivables | 1,40,04,240 | |
| Revenue | | 1,18,68,000 |
| Output CGST | | 10,68,120 |
| Output SGST | | 10,68,120 |

## How it's tested

**Interview questions:**

- "Walk me through building a driver-based revenue forecast."
- "You get an ERP export at transaction level; the plan is at product level. How do you bridge them?" (They want to hear *mapping table*, not "I retype it.")
- "EBITDA missed budget. How do you find out why?" (Price-volume-mix bridge.)
- "When would you recommend moving off Excel to Anaplan or Adaptive?"

**The practical test — this is what actually decides it:**

- A **timed Excel case (45–90 min):** raw actuals + budget on two tabs. Build a variance report, a price-volume bridge, and a one-line commentary. They watch whether you use `SUMIFS`/`XLOOKUP` or manual filtering.
- A **"break my model" review:** they hand you a spreadsheet with a hard-coded total and ask you to find the error.
- Occasionally a **SQL/Power BI screen** for FP&A roles at data-mature firms: "aggregate these GL rows to plan lines and compute variance."

Good answer to the move-off-Excel question:

> "Move off Excel when three things co-occur: (1) the model breaks on version control — multiple people editing, `FINAL_v3` emails; (2) actuals load is a manual monthly copy-paste that eats two days; (3) we need bottom-up input from 10+ cost-centre owners with approval workflow. At that point a tool like Adaptive pays back — roughly ₹20–40 L/year, justified by analyst time saved and fewer errors."

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Hard-coding numbers inside formulas | All assumptions in one labelled Assumptions tab, referenced by name |
| `VLOOKUP` with hard column index | `XLOOKUP` / `INDEX-MATCH` — survives inserted columns |
| No "UNMAPPED" catch on GL mapping | Default flag so new GL codes surface, never silently drop |
| Manual monthly copy-paste of actuals | Structured tables + a repeatable pull (Power Query/Python/connector) |
| Reporting variance without the *why* | Always a price-volume-mix bridge and a one-line story |
| Buying Anaplan to fix a modelling problem | Fix the model design first; a tool amplifies good design, not bad |
| One giant tab | Separate Inputs / Calcs / Outputs; colour-code inputs (blue) vs formulas (black) |
| Divide-by-zero in Var % | Wrap in `IFERROR`, show "n/m" |

## Learn-it roadmap & resources

**Realistic time-to-proficiency:** 3–4 months of deliberate practice to clear an FP&A Excel test; 6–12 months on the job to be trusted with a planning tool.

| Phase | Weeks | Focus |
|---|---|---|
| Excel modelling core | 1–4 | `SUMIFS`, `XLOOKUP`, dynamic arrays, structured refs, a 3-statement model |
| Driver-based planning | 5–8 | Build a budget + reforecast; price-volume-mix bridges |
| Data layer | 9–12 | Power Query, basic SQL, pandas for large actuals |
| EPM exposure | ongoing | Free Adaptive/Anaplan trials, model-builder tutorials |

**Resources:**

- **Free:** Corporate Finance Institute free courses; Anaplan "Level 1 Model Builder" (free); Workday Adaptive product tutorials; Microsoft Learn (Power Query, DAX); `pandas` docs.
- **Paid / cert:** CFI **FMVA** (globally portable, strong in India), Anaplan **Certified Model Builder**, Adaptive Planning certification (usually employer-sponsored), Wall Street Prep for modelling drills.
- **Practice:** rebuild your own company's or a listed FMCG's segment P&L from its annual report as a driver model.

## Quick-reference

| Need | Formula / step |
|---|---|
| Lookup (modern) | `=XLOOKUP(key, lookup_col, return_col, "NA")` |
| Aggregate to grain | `=SUMIFS(amt, key_col, key, month_col, mth)` |
| Safe % variance | `=IFERROR((Act-Bud)/ABS(Bud),"n/m")` |
| Volume effect | `(Act_units − Bud_units) × Bud_price` |
| Price effect | `(Act_price − Bud_price) × Act_units` |
| SQL aggregate | `SELECT plan_line, period, SUM(amount) … GROUP BY plan_line, period` |
| DAX variance | `act - bud` via `CALCULATE([Amount], Scenario[Name]="Actual"/"Budget")` |
| Move-off-Excel triggers | version hell + manual actuals load + multi-owner input/workflow |
| EPM tools (India-relevant) | Anaplan, Workday Adaptive, Oracle EPM Cloud, Board, Datarails |
| EPM value chain | Model → Data integration → Workflow → Reporting/Audit |
| Output GST split | CGST 9% + SGST 9% (intra-state) or IGST 18% (inter-state) |
