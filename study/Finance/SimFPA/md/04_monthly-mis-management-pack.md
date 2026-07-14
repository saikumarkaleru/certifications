# The Monthly MIS / Management Pack

## The ask

It's Friday, 10 July 2026, month-end +7 for June. The CFO sets the standing expectation:

> "Every month, by working-day 5 after close, I need the management pack — P&L actual vs budget vs last year, the KPI dashboard, the goods-vs-services split, and half a page of plain-English summary. It goes to the board and the bank. Same format every month, so I can read it in five minutes. And it can't take you five days to build — automate it."

Deadline: recurring, WD+5. Today's pack covers June / Q1 FY27. The job is a *repeatable* pack, not a one-off.

## What you're given

The closed Tally GL for Q1 and the prior-year comparatives:

**Q1 FY27 close (Rs cr):**

| Line | Actual | Budget | Prior Yr (Q1 FY26) |
|---|---:|---:|---:|
| Revenue — goods | 2.142 | 2.250 | 1.950 |
| Revenue — services | 0.750 | 0.750 | 0.620 |
| Returns/adj | (0.192) | 0.000 | 0.000 |
| **Total revenue** | **2.700** | **2.850** | **2.570** |
| COGS | (1.931) | (1.995) | (1.850) |
| **Gross profit** | **0.769** | **0.855** | **0.720** |
| Employee cost | (0.290) | (0.270) | (0.245) |
| Other opex | (0.205) | (0.195) | (0.180) |
| **EBITDA** | **0.274** | **0.390** | **0.295** |
| Depreciation | (0.036) | (0.036) | (0.034) |
| Finance cost | (0.023) | (0.023) | (0.024) |
| **PBT** | **0.215** | **0.331** | **0.237** |

**KPI feeds:** DSO 66 days (target 60); headcount 16 (budget 15); cash Rs 31 lakh.

## Build it — step by step

**Step 1 — One clean data feed.** Export the Tally trial balance to a `GL_Dump` tab with columns: `GL code | GL name | Amount`. Map each GL to a P&L line via a lookup table (`Map` tab: `GL code → P&L line`). The pack's actual column is then one formula:

```
=SUMIFS(GL_Dump[Amount], GL_Dump[PLLine], $B5)
```

dragged down every P&L row. Budget and prior-year columns pull from their own stored tabs with the same key. **Nothing is typed twice** — next month you paste a fresh GL dump and the whole pack refreshes.

**Step 2 — Variance columns.** Two variance blocks: vs budget and vs prior year, each in value and %:

```
Var vs Bud (Rs)  = Actual − Budget
Var vs Bud (%)   = (Actual − Budget) / Budget     (guard with IFERROR for zero rows)
YoY growth (%)   = (Actual − PriorYr) / PriorYr
```

**Step 3 — KPI tiles.** A `Dashboard` tab computes the six headline KPIs with conditional-format traffic lights (green if within tolerance, red if not):

```
GM %      = GrossProfit / Revenue
EBITDA %  = EBITDA / Revenue
DSO       = Debtors / Revenue_annualised × 365
```

**Step 4 — Segment view.** A small goods-vs-services block so the two engines are always visible — this is where the mix story lives.

**Step 5 — Chart choices.** Keep it boring and legible: a **clustered column** for revenue (actual/budget/PY side by side), a **waterfall** for the PBT bridge, a **line** for DSO trend across months, and **KPI cards** for the six numbers. No pie charts, no 3-D. If the CFO reads it on a phone, it has to work in greyscale.

**Step 6 — Power BI option (for the board version).** The same model can live in Power BI off the Tally export. Core DAX measures:

```DAX
Revenue    = SUM(GL[Amount])
GM %       = DIVIDE([Gross Profit], [Revenue])
Var vs Bud = [Revenue] - [Budget Amount]
YoY %      = DIVIDE([Revenue] - [Revenue PY], [Revenue PY])
```

and to pull prior year: `Revenue PY = CALCULATE([Revenue], SAMEPERIODLASTYEAR('Date'[Date]))`.

## The deliverable

**NTSPL Management Pack — Q1 FY2026-27**

**1. P&L — actual vs budget vs prior year (Rs cr)**

| Line | Actual | Budget | Var | Var % | PY | YoY % |
|---|---:|---:|---:|---:|---:|---:|
| Total revenue | 2.700 | 2.850 | (0.150) | −5.3% | 2.570 | +5.1% |
| Gross profit | 0.769 | 0.855 | (0.086) | −10.1% | 0.720 | +6.8% |
| GM % | 28.5% | 30.0% | −1.5pp | | 28.0% | +0.5pp |
| EBITDA | 0.274 | 0.390 | (0.116) | −29.7% | 0.295 | −7.1% |
| PBT | 0.215 | 0.331 | (0.116) | −35.0% | 0.237 | −9.3% |

**2. KPI dashboard**

| KPI | Actual | Target | Flag |
|---|---:|---:|:--:|
| Revenue (Rs cr) | 2.70 | 2.85 | 🔴 |
| Gross margin % | 28.5% | 30.0% | 🔴 |
| EBITDA (Rs cr) | 0.274 | 0.390 | 🔴 |
| DSO (days) | 66 | 60 | 🔴 |
| Headcount | 16 | 15 | 🟡 |
| Cash (Rs lakh) | 31 | 35 | 🟡 |

**3. Segment view (Rs cr)**

| Segment | Revenue | GM % | vs Budget |
|---|---:|---:|---:|
| Goods | 1.95 (net of adj) | 25.0% | (0.30) |
| Services | 0.75 | 45.0% | 0.00 |
| **Blended** | **2.70** | **28.5%** | **(0.15)** |

**4. Written summary (analyst voice):**

> "June closes Q1 at Rs 2.70 cr revenue, 5% below budget but 5% ahead of last year — the miss is versus an ambitious plan, not a decline. The gap is goods volume (21,000 vs 22,500 units); pricing was favourable (ASP Rs 1,020). EBITDA at Rs 0.27 cr is the pressure point — the revenue miss de-leveraged margin (28.5% vs 30%) and opex ran Rs 4 lakh over on an early hire. DSO drifting to 66 days and cash at Rs 31 lakh (vs Rs 35 lakh opening) is a collections watch-item — Rs 6 lakh of the Rs 4 lakh cash drop is timing on receivables. **Actions:** (1) tighten collections to pull DSO back toward 60; (2) hold the remaining Q4 hires pending Q2 volume; (3) full-year Rs 12 cr still intact given the March-loaded plan, contingent on Q2 volume recovery."

## How it's reviewed

The controller checks the pack **ties to the ledger** — total revenue and PBT in the pack must equal the Tally-closed numbers to the rupee. She checks **internal consistency**: EBITDA − depreciation − finance cost = PBT; segment revenue sums to total. She checks the **KPI flags** are computed, not hand-coloured. And the CFO checks the **summary is decision-oriented** and consistent with the variance pack from the prior chapter — the same Rs 15 lakh volume story, told the same way. Any number that appears in two places must match everywhere.

## Common mistakes & red flags

- **Rebuilding from scratch monthly.** If the pack isn't a paste-and-refresh, WD+5 becomes WD+9. Invest once in the GL-map + SUMIFS engine.
- **Typing numbers into the output.** Every cell must trace to the GL dump or a stored budget/PY tab. Hand-keyed figures are how packs contradict the ledger.
- **No prior-year column.** Actual vs budget alone hides whether the business is growing. YoY reframes a "miss" (+5% YoY) honestly.
- **Vanity charts.** Pie/3-D charts that don't survive greyscale or a phone screen. Board packs are read fast — clustered columns and a waterfall.
- **KPIs with no target.** A DSO of 66 means nothing without the 60-day target and the flag. Always show the benchmark.
- **Inconsistent numbers across the pack.** Revenue Rs 2.70 cr on page 1 and Rs 2.69 cr on the chart destroys trust instantly.

## On the job & in the interview

The "why": the MIS pack is FP&A's monthly heartbeat — it tells the board and the bank whether the plan is on track, in a format they can absorb in five minutes. Repeatability is the skill; a pack that takes a week to build is worthless by the time it's read.

Jargon: **MIS / management pack**, **actual vs budget vs PY**, **WD+5 (working-day 5)**, **tie-out to ledger**, **traffic-light KPIs**, **de-leverage**, **single source of truth**.

**Q: "How do you build a monthly pack that's both fast and reliable?"**
A: "One clean data feed and zero hand-keying. I map every Tally GL to a P&L line once, then the actual column is a SUMIFS off the monthly GL dump; budget and prior-year sit in their own tabs on the same key. Next month I paste a fresh dump and the whole pack — P&L, KPIs, segment, charts — refreshes. It ties to the ledger by construction, and it's a WD+5 job, not a WD+9 one."

**Q: "Why show prior year as well as budget?"**
A: "They answer different questions. Budget tells you if you hit the plan; prior year tells you if the business is actually growing. Our Q1 was 5% under budget but 5% up on last year — without the PY column you'd read that as pure bad news, when structurally the business is still expanding."

**Q: "What KPIs would you put on the front page for a trading-and-services firm like this?"**
A: "Six: revenue, gross margin %, EBITDA, DSO, headcount, and cash. Revenue and GM% show the top line and mix health; EBITDA is the operating profit signal; DSO and cash flag the working-capital risk that a goods-heavy trader lives on; headcount tracks the biggest opex lever. Each with a target and a traffic light so the reader sees exceptions in two seconds."
