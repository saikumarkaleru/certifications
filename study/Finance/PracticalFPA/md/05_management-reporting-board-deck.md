# Management reporting & the board deck

## What it is & where it's used

Management reporting is the monthly ritual where Finance turns the trial balance into a story the leadership team can act on. Two artefacts dominate:

1. **The monthly reporting pack (MIS pack)** — a 15-40 page internal document circulated 5-10 working days after month-end. It carries the P&L vs budget, cash, working capital, department spend, and KPI dashboards.
2. **The board deck** — a tighter 12-20 slide summary presented to the board of directors / investors every month or quarter. It is the pack, distilled and narrated.

Roles that live in this work: **FP&A Analyst/Manager, Management Accountant, Business Finance Partner, Financial Controller, Head of Finance/CFO**, and in startups the **Finance lead** who does all of it alone. If a job description says "prepare monthly MIS," "budget vs actual variance analysis," "board reporting," or "flash reporting," this chapter is that job.

## The gap: why companies want this (and college didn't teach it)

College teaches you to *prepare* financial statements per Ind AS / Schedule III. It does not teach you to **explain** them to a CEO who has 90 seconds. The gap is threefold:

- **From accuracy to insight.** Anyone can show that Gross Margin fell to 38%. The paid skill is stating *why* (input cost up 4%, discounting up 2%, mix shift toward low-margin SKUs) and *what to do*.
- **From statutory to managerial.** The board doesn't care about Schedule III line ordering. They want revenue by segment, contribution margin, cash runway, and CAC/LTV — cuts that never appear in the audited financials.
- **From data to narrative.** MBAs build DCFs; employers need someone who can build a clean waterfall, write a three-bullet commentary, and not blow up the CFO in front of the board. Nobody grades "commentary writing" in a degree, but it's the entire value of the role.

## What "proficient" looks like

A job-ready person can, **unaided**, take a trial balance and a budget file and produce by Day 5:

- A **budget-vs-actual P&L** with variance columns (₹ and %) and a favourable/adverse flag.
- A **bridge/waterfall** explaining the movement in profit (or revenue) from budget to actual, or MoM.
- A **cash and working-capital** view: closing cash, burn, runway, DSO/DPO/DIO.
- A **one-page executive summary**: 3-5 bullets, each a number + cause + action.
- A **board deck** that opens with the punchline, not the appendix.
- Commentary that survives the "so what?" test on every slide.

They know the reporting calendar, tie every number back to the GL, and never present a variance they can't explain.

## Hands-on: how to actually do it

### 1. The variance table (Excel)

Assume actuals in column C, budget in D. Variance and flag:

```
Variance ₹:   =C2-D2
Variance %:   =IFERROR((C2-D2)/ABS(D2),"n/a")
Flag:         =IF(N2=0,"—",IF(ISNUMBER(SEARCH("expense",$A2)), IF(C2<D2,"Fav","Adv"), IF(C2>D2,"Fav","Adv")))
```

For revenue/profit rows, actual > budget is Favourable; for cost rows it flips — hence the `SEARCH("expense"...)` switch, or keep a sign column.

Pull actuals from the GL dump with a keyed lookup instead of manual typing:

```
=XLOOKUP($A2, GL!$B:$B, GL!$H:$H, 0)          'exact GL account match
=SUMIFS(GL!$H:$H, GL!$C:$C, $A2, GL!$E:$E, ">="&$F$1, GL!$E:$E, "<="&$G$1)   'sum by cost centre within date range
```

**Materiality filter** — only comment on what matters. A common rule: variance is reportable if `ABS(₹) > 500000 OR ABS(%) > 10%`.

```
=IF(OR(ABS(E2)>500000, ABS(F2)>0.10), "COMMENT", "")
```

### 2. The profit bridge (waterfall)

Insert → Chart → Waterfall in Excel 365. Data laid out as:

| Step | Value (₹ lakh) |
|---|---|
| Budget EBITDA | 120 |
| Volume | +18 |
| Price | +9 |
| Input cost | -14 |
| Employee cost | -6 |
| Actual EBITDA | 127 |

Mark "Budget EBITDA" and "Actual EBITDA" as **Totals** (double-click the point → Set as Total) so they anchor to the axis.

### 3. Rolling KPIs (Power BI / DAX)

```dax
Revenue MTD = CALCULATE([Revenue], DATESMTD('Date'[Date]))
Revenue YTD = CALCULATE([Revenue], DATESYTD('Date'[Date]))
Var to Budget % = DIVIDE([Revenue] - [Budget], [Budget])
Gross Margin % = DIVIDE([Revenue] - [COGS], [Revenue])
Cash Runway (months) = DIVIDE([Closing Cash], AVERAGEX(DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -3, MONTH), [Net Burn]))
```

### 4. Pull the trial balance from Tally

TallyPrime → **Gateway of Tally → Display More Reports → Trial Balance → F12 (Configure)** set "Show Closing Balances" = Yes → **Alt+E (Export) → Excel (Spreadsheet)**. For segment cuts, enable **Cost Centres** first (F11 → Maintain Cost Centres = Yes) and export the **Cost Centre Breakup**.

### 5. Automating the merge (Python)

```python
import pandas as pd

actual = pd.read_excel("tb_jun26.xlsx")          # GL account, Amount
budget = pd.read_excel("budget_fy27.xlsx")        # GL account, Jun

rep = actual.merge(budget, on="GL account", how="left", suffixes=("_act","_bud"))
rep["Var_INR"] = rep["Amount"] - rep["Jun"]
rep["Var_pct"] = rep["Var_INR"] / rep["Jun"].abs()
rep["Flag"]    = rep["Var_pct"].apply(lambda x: "Adv" if x < -0.10 else ("Fav" if x > 0.10 else "—"))
rep.to_excel("variance_jun26.xlsx", index=False)
```

## Worked example / mini-project

**Company:** Zephyr Foods Pvt Ltd, a D2C snacks brand. June FY27 close.

**Reporting P&L (₹ lakh):**

| Line | Actual | Budget | Var ₹ | Var % | Flag |
|---|---|---|---|---|---|
| Net Revenue | 480 | 500 | -20 | -4% | Adv |
| COGS | 298 | 300 | -2 | fav cost | Fav |
| **Gross Profit** | **182** | **200** | **-18** | **-9%** | Adv |
| GM % | 37.9% | 40.0% | -2.1pp | | Adv |
| Marketing | 96 | 85 | +11 | +13% | Adv |
| Employee cost | 54 | 55 | -1 | | Fav |
| Other opex | 32 | 30 | +2 | | Adv |
| **EBITDA** | **0** | **30** | **-30** | | Adv |

**Cash:** Opening ₹620L, closing ₹548L, net burn ₹72L → runway = 548 / (avg 3-mo burn ₹68L) = **8.1 months**. DSO 42 days (up from 35), DIO 61 days.

**Executive summary (this is the deliverable that earns the salary):**

- **Revenue ₹480L, 4% below budget** — offline distributor sell-through slowed in Tier-2 (-₹28L); e-com grew +₹8L, partly offsetting.
- **Gross margin fell to 37.9% (-2.1pp)** — heavier discounting on the ₹99 SKU during the Amazon sale drove it; input costs were actually favourable.
- **EBITDA at breakeven vs ₹30L budget** — the miss is 60% margin, 40% a ₹11L marketing overspend on a campaign pulled forward from July.
- **Runway 8.1 months, DSO up 7 days** — one distributor is ₹40L overdue; collections escalated, targeting closure by 15 Jul.
- **Ask:** approve reallocating July marketing (already spent in June) and tighten discount-approval to protect Q2 margin.

**Board deck order (12 slides):** (1) Executive summary, (2) EBITDA bridge budget→actual, (3) Revenue by channel, (4) Gross margin trend + driver, (5) Opex, (6) Cash & runway, (7) Working capital / AR ageing, (8) KPI scorecard (CAC, LTV, repeat rate), (9) Key risks, (10) Decisions requested, (11) Next-month outlook, (12) Appendix.

## How it's tested

**Interview questions:**
- "Walk me through how you'd build a monthly MIS pack from a trial balance."
- "Gross margin dropped 200bps this month. How do you find out why?"
- "What's the difference between a statutory P&L and a management P&L?"
- "How do you decide what goes on a board slide vs the appendix?"
- "What's your reporting calendar look like around close?"

**Practical assessments:**
- **Timed Excel/case (60-90 min):** given a raw TB and a budget tab, build the variance P&L, a waterfall, and write a 5-bullet summary. Graded on formula cleanliness (no hardcoding), correct fav/adverse logic, and whether commentary explains *causes*.
- **"Fix the deck" test:** they hand you a bloated 40-slide deck and ask you to cut it to 12 and rewrite the opening slide.
- **Live commentary drill:** here's the variance table — give me three bullets in two minutes.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Reporting *what* happened, never *why* | Every material variance gets a one-line cause and action |
| Commentary restates the number ("Revenue was ₹480L") | State cause + quantify + implication |
| Data doesn't tie to the GL | Reconcile the pack total to the TB before circulating — always |
| 40-slide deck, punchline on slide 31 | Answer-first: executive summary is slide 1 |
| Commenting on every line | Apply a materiality threshold; stay silent on noise |
| Hardcoded numbers, broken next month | Formula-driven, refreshable from a single data tab |
| Inconsistent numbers across slides | One source-of-truth data model feeds every slide |
| Presenting a variance you can't explain | Never take a number to the board you haven't traced |
| Colours/signs flipped (adverse shown green) | Lock a convention: adverse = red, favourable = green, consistently |

## Learn-it roadmap & resources

**Time to proficiency:** 6-10 weeks of deliberate practice if you already know Excel and basic accounting.

- **Weeks 1-2:** Master variance tables, SUMIFS/XLOOKUP, and fav/adverse logic. Rebuild a real company's segment P&L from its annual report.
- **Weeks 3-4:** Waterfalls, bridges, and writing commentary. Draft a 5-bullet exec summary daily on any dataset.
- **Weeks 5-6:** Build a KPI dashboard in Power BI or Excel. Learn the close calendar and reconciliation discipline.
- **Weeks 7-10:** Assemble a full mock board deck end-to-end and get it critiqued.

**Resources:**
- CFI **FP&A** and **Financial Modeling (FMVA)** courses (paid) — strong on reporting structure.
- Free: **Corporate Finance Institute** blog on variance analysis; **Microsoft Learn** for DAX; the "Financial Times of variance commentary" — practice by writing your own on public quarterly results.
- Books: *Financial Planning & Analysis and Performance Management* (Alexander).
- India: ICAI SFM/Cost material for cost-variance mechanics; study any listed company's investor deck as a board-deck template.

## Quick-reference

| Item | Formula / Step |
|---|---|
| Variance ₹ | `=Actual-Budget` |
| Variance % | `=IFERROR((Act-Bud)/ABS(Bud),"n/a")` |
| Pull actual from GL | `=SUMIFS(GL!Amt, GL!Acct, key, GL!Date, ">="&start, GL!Date,"<="&end)` |
| Materiality flag | `=IF(OR(ABS(var)>500000,ABS(pct)>0.10),"COMMENT","")` |
| Runway (months) | `Closing cash / avg monthly net burn` |
| DSO | `AR / Revenue × days` |
| DPO | `AP / COGS × days` |
| DIO | `Inventory / COGS × days` |
| GM % (DAX) | `DIVIDE([Rev]-[COGS],[Rev])` |
| Tally TB export | Display More Reports → Trial Balance → Alt+E → Excel |
| Deck rule | Answer-first; exec summary slide 1; appendix last |
| Commentary formula | Number + Cause + Implication + Action |
| Colour convention | Adverse = red, Favourable = green |
| Close cadence | Pack by working day 5; board deck by day 7-10 |

**The one line to remember:** the board doesn't pay you to report the number — they pay you to explain the number and tell them what to do about it.
