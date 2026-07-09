# Q&A — Excel Dashboards and Data Visualisation

Every question below is followed by a full answer. All formulas are written for modern Excel and every number is self-verified so you can reproduce each result in a live workbook.

---

## Section A — Concept Check (test the WHY of the technique)

**A1. What is the difference between a dashboard and a report, and why does it matter to a modeller?**

A report is a static, comprehensive dump of data — every row, every period, for the record. A dashboard is a curated, single-screen decision tool: it shows only the metrics that drive a decision, updates dynamically, and lets the user see status at a glance. The distinction matters because building a dashboard is an act of *editing*, not *listing*. If a stakeholder has to scroll, hunt, or interpret raw numbers, you built a report and called it a dashboard. The discipline is to ask "what decision does this screen support?" and cut everything else.

**A2. Why separate a workbook into distinct layers — a raw-data tab, a calculation tab, and a presentation tab?**

Because mixing them makes a model fragile and unauditable. The convention is three zones: (1) **Data** — raw inputs, imports, tables, untouched; (2) **Calculation/Working** — the formulas, lookups, and pivot sources that transform data; (3) **Presentation/Dashboard** — charts, KPI tiles, and controls that reference the working layer only. This one-way flow (data → calc → dashboard) means the dashboard never contains original logic, so refreshing data cannot break the visuals, and an auditor can trace any chart back to its source without wading through formatting.

**A3. Why is an Excel Table (Ctrl+T) the preferred source for a dashboard's charts and pivots rather than a plain range?**

A Table has a defined name, structured references (`Sales[Revenue]`), and — critically — it **auto-expands**. When new rows are appended, every PivotTable, chart, and formula built on the Table absorbs the new data on refresh without you re-pointing ranges. A plain range `A1:F500` is frozen; add a row 501 and it is silently excluded. Tables also carry banded formatting and header filters for free. For a dashboard that must stay live as data grows, the Table is the foundation.

**A4. What is the purpose of a "control" (a slicer, drop-down, or form control) on a dashboard?**

Controls turn a static picture into an interactive tool: the user selects a region, period, or scenario and the whole dashboard re-renders around that choice. Mechanically the control writes a value into a cell (a slicer filters a pivot; a drop-down/form control sets a selector cell), and the dashboard's formulas and charts read that cell. The "why" is that one dashboard can serve many questions — instead of building twelve regional views, you build one and let the control drive it.

**A5. Why do professionals prefer `INDEX/MATCH` or `XLOOKUP` over nested `IF`s when a control selects which data series to display?**

Because a selector should scale. If a drop-down offers "North / South / East / West", a nested `IF` chain grows one branch per option and must be rewritten every time an option is added. `INDEX(data_block, MATCH(selector, headers, 0))` returns the chosen column with no branching — add a fifth region to the data and the same formula finds it. It is shorter, self-documenting, and immune to the copy-paste errors that plague long `IF` chains.

**A6. What is the single most important principle of data-ink, and how does it apply to a finance chart?**

Maximise the data-ink ratio: every pixel should carry information. In practice that means stripping chartjunk — heavy gridlines, 3-D effects, background fills, redundant legends, drop shadows — so the data speaks. For a finance chart: remove the border, lighten or delete gridlines, label data points directly instead of forcing the eye to a legend, and never use 3-D columns (they distort the very magnitudes you are trying to compare). Clarity, not decoration, is the goal.

**A7. When should you use a line chart, a column/bar chart, or a pie chart?**

Match the geometry to the message. A **line** chart shows a trend or change over a continuous axis (time) — connect the dots because the connection is meaningful. A **column/bar** chart compares discrete categories or a few time points — height/length encodes magnitude, which the eye reads accurately. A **pie** chart shows parts of a single whole and only works with very few slices; beyond ~4 categories the eye cannot compare wedge angles, so a bar chart is almost always better. The rule: time → line, comparison → bar, one-whole-few-parts → (reluctantly) pie.

**A8. Why is conditional formatting (data bars, colour scales, icon sets) useful on a dashboard, and what is its main trap?**

It embeds a visual layer directly in the numbers, so a table of figures also becomes a heat map — the eye spots outliers, trends, and red flags without a separate chart. The trap is over-use: apply three-colour scales, data bars, and icon sets to the same table and you create noise, not signal. Reserve it for the one dimension that matters (e.g. variance to budget) and keep the palette restrained.

**A9. Why avoid a "rainbow" of colours across a dashboard, and what palette discipline replaces it?**

A rainbow assigns colour randomly, so colour carries no meaning and the eye finds no anchor. Disciplined dashboards use a limited palette with **semantic** colour: one neutral for context, one accent for the metric in focus, and reserved colours for meaning (e.g. red = adverse/over budget, green = favourable). Grey-out everything that is context and let colour highlight only what the reader should act on. Also account for colour-blindness — never encode meaning by red/green alone; pair it with position, labels, or icons.

**A10. What is a KPI tile (a "card"), and why do dashboards lead with them?**

A KPI tile is a large single number — revenue, margin, cash — often paired with a comparison (vs. prior period or budget) and a tiny trend sparkline. Dashboards lead with tiles because the human eye reads a big number in a fraction of a second: the top strip answers "how are we doing?" before the reader looks at any chart. The supporting charts below then answer "why?" The tile is the headline; the chart is the article.

**A11. What is a sparkline and where does it belong?**

A sparkline is a tiny, word-sized chart drawn inside a single cell (Insert → Sparklines), showing a trend without axes or labels. It belongs beside a KPI tile or inside a table row, giving instant context in the space of one cell. It is a glanceable companion to a number, not a substitute for a full chart.

**A12. Why use dynamic named ranges or spill formulas behind a chart instead of a fixed range?**

So the chart grows and shrinks with the data automatically. A dynamic name defined with `OFFSET`/`COUNTA` (or a modern spill range `A2#`) resizes as rows are added or filtered, so the series always plots exactly the live data. This is what makes a control-driven dashboard feel alive — change the driver and the plotted range recomputes.

---

## Section B — Build / Computational Problems

**B1. Build an interactive KPI tile: revenue vs. budget with a variance %.**

Data (working tab):

| Cell | Item | Value |
|------|------|-------|
| B2 | Actual revenue | 1,240,000 |
| B3 | Budget revenue | 1,150,000 |

Tile formulas (presentation tab):
- Headline value: `=B2` → **1,240,000**
- Variance (absolute): `=B2-B3` → 1,240,000 − 1,150,000 = **90,000**
- Variance (%): `=(B2-B3)/B3` → 90,000 / 1,150,000 = 0.078260… → **7.83%**
- Status label: `=IF(B2>=B3,"Favourable","Adverse")` → 1,240,000 ≥ 1,150,000 → **"Favourable"**

Reconciling: 1,150,000 × (1 + 0.0783) = 1,150,000 × 1.0783 = 1,240,000. ✔ The tile is internally consistent — the % variance grosses the budget back up to the actual.

---

**B2. Drive a data series from a drop-down using `INDEX/MATCH`.**

Data block (working tab), regional quarterly revenue:

| | A | B | C | D |
|---|---|---|---|---|
| 1 | Quarter | North | South | East |
| 2 | Q1 | 300 | 220 | 180 |
| 3 | Q2 | 340 | 210 | 200 |
| 4 | Q3 | 360 | 250 | 190 |
| 5 | Q4 | 380 | 240 | 210 |

Selector cell G1 holds a data-validation list {North, South, East}. Suppose the user picks **South**.

Pull the chosen column into a chart-feed range (G2 down):
`=INDEX($B$2:$D$5, ROW()-1, MATCH($G$1,$B$1:$D$1,0))` filled G2:G5.

Step-by-step for G2:
- `MATCH("South", B1:D1, 0)` → South is the 2nd header → **2**
- `ROW()-1` in row 2 → 2 − 1 = **1**
- `INDEX(B2:D5, 1, 2)` → row 1, column 2 of the block → **220**

Filling down gives 220, 210, 250, 240 — exactly South's column. ✔

Reconciling: total plotted = 220+210+250+240 = **920**, which equals `=SUM(C2:C5)` on the raw South column. The `INDEX/MATCH` feed matches the source, so the chart is faithful.

---

**B3. Compute the numbers behind a KPI card with a QoQ growth sparkline.**

Quarterly total revenue: Q1 820, Q2 970, Q3 940, Q4 1,010 (in G-column feed from B2 above summed across regions, illustrative).

- Latest value (card headline) = Q4 = **1,010**
- QoQ growth Q3→Q4: `=(1010-940)/940` = 70 / 940 = 0.074468… → **7.45%**
- Full-year total: `=SUM(820,970,940,1010)` = **3,740**
- Average quarter: `=3740/4` = **935**

Reconciling: the sparkline plots 820, 970, 940, 1010 — one dip (Q2→Q3, −30) then recovery. The card shows 1,010 with +7.45%; the tiny chart shows the shape the single number cannot. Both read from the same four cells, so they cannot disagree.

---

**B4. Build a dynamic chart range with `OFFSET` + `COUNTA`.**

Data in A2:A100 (dates) and B2:B100 (values), currently only 6 months filled (A2:B7).

Define a name `ChartVals`:
`=OFFSET(Sheet1!$B$2, 0, 0, COUNTA(Sheet1!$B$2:$B$100), 1)`

Walk-through today (6 filled cells):
- `COUNTA($B$2:$B$100)` counts non-blank values → **6**
- `OFFSET($B$2, 0, 0, 6, 1)` → a range starting at B2, 6 rows tall, 1 column wide → **B2:B7**

Add a 7th month in B8: `COUNTA` now returns 7, `OFFSET` returns B2:B8, and the chart series (set to `=Sheet1!ChartVals`) redraws with the new point automatically. ✔ No manual range edit.

Reconciling: the height argument equals the count of data points, so the plotted range and the data length are always equal by construction — the chart can never lag or overshoot the data.

---

**B5. Variance table with conditional-format thresholds.**

Actual vs. budget by department:

| Dept | Actual | Budget | Var % `=(A-B)/B` |
|------|--------|--------|------|
| Sales | 540 | 500 | (540−500)/500 = **+8.0%** |
| Ops | 610 | 650 | (610−650)/650 = **−6.15%** |
| IT | 300 | 300 | 0 / 300 = **0.0%** |

Apply an icon set / colour rule on Var %: green if ≥ +2%, amber if between −2% and +2%, red if ≤ −2%.
- Sales +8.0% → ≥ +2% → **green**
- Ops −6.15% → ≤ −2% → **red**
- IT 0.0% → within band → **amber**

Reconciling: sum the variances in currency — Sales +40, Ops −40, IT 0 → net **0**. The portfolio is exactly on budget in total even though two departments deviate; the colour layer surfaces the offsetting movements a single total would hide.

---

**B6. Build a "% of total" contribution for a (small) pie or 100%-stacked bar.**

Segment revenue: A 480, B 300, C 120, D 100. Total = 480+300+120+100 = **1,000**.

Shares (`=segment/total`):
- A: 480/1000 = **48.0%**
- B: 300/1000 = **30.0%**
- C: 120/1000 = **12.0%**
- D: 100/1000 = **10.0%**

Check: 48 + 30 + 12 + 10 = **100%**. ✔ Because there are only four parts of one whole and the shares sum to 100%, this is a legitimate (rare) case for a pie — or better, a single 100% stacked bar for easier comparison across periods.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Walk me through how you would structure a workbook so a monthly dashboard refreshes cleanly."**

Model answer: "I use a strict three-layer architecture. Tab one is raw data, ideally an Excel Table or Power Query connection so appending a month is automatic. Tab two is a working/calculation layer — lookups, aggregations, and pivot sources; nothing formatted for display. Tab three is the dashboard: KPI tiles, charts, and slicers that reference only the working layer. Data flows one way, data → calc → dashboard, so a refresh can never break the visuals. I drive charts off dynamic ranges or Table references so they auto-expand. To refresh monthly I drop in new data, hit refresh-all, and every tile updates without touching a range."

**C2. "A stakeholder says your dashboard is 'too busy'. How do you diagnose and fix it?"**

Model answer: "I'd apply the data-ink test — strip anything that isn't carrying information. First, cut chartjunk: kill 3-D effects, heavy gridlines, borders, and background fills. Second, reduce colour to a purpose — grey for context, one accent for the metric in focus, reserved red/green only for good/bad. Third, check whether every chart earns its place; if two charts answer the same question I merge or delete one. Fourth, establish hierarchy — big KPI tiles on top for the headline, supporting detail below. The test is whether a reader gets the main message in five seconds. Usually 'too busy' means I've shown everything I have instead of everything they need."

**C3. "Why might you choose a bar chart over a pie chart for market share?"**

Model answer: "The eye reads length and position accurately but judges angles and areas poorly. A pie forces the viewer to compare wedge angles, which is hard beyond three or four slices, and it makes ranking and small differences almost invisible. A bar chart lets you sort by size, add precise data labels, and compare across periods side by side. I'd only keep a pie for a single 'part of one whole' snapshot with two or three segments; for anything comparative or time-based, a bar or column wins on both accuracy and honesty."

**C4. "How do you make a dashboard accessible and honest with colour?"**

Model answer: "Two rules. Accessibility: never encode meaning by colour alone — about 8% of men are red-green colour-blind — so I pair colour with labels, icons, or position, and I test with a colour-blind simulator. Honesty: I keep axes starting at zero for bar charts so heights aren't exaggerated, I don't truncate axes to dramatise a trend, and I avoid dual axes that imply a false correlation. Colour should mean something consistent across the whole dashboard — red is always adverse, green always favourable — never decoration."

**C5. "What's the advantage of slicers and PivotTables for interactivity versus writing everything with formulas?"**

Model answer: "PivotTables plus slicers give you filtering, grouping, and drill-down almost for free, and a slicer can control several pivots and charts at once, so one click re-renders the whole dashboard. They refresh with the data and need very little maintenance. Formula-driven dashboards using `INDEX/MATCH` or `SUMIFS` give finer control over exact layout and calculated metrics that pivots handle awkwardly. In practice I combine them: pivots and slicers for the interactive filtering backbone, formulas for bespoke KPI tiles and variance logic that sit on top."

**C6. "How would you show a single metric's actual, target, and prior-year on one compact chart?"**

Model answer: "A bullet-style chart. The primary bar is the actual value, a thin vertical marker shows the target, and a lighter shaded band behind shows prior-year or qualitative ranges. It packs 'where are we, where should we be, where were we' into one horizontal bar per metric, so you can stack several down the page and read a whole scorecard at a glance. It's far more compact and honest than three separate gauges, which waste space and exaggerate small differences."

---

## Section D — Common-Error Spotting

**D1. Spot the error:** A chart is built on the fixed range `=Sheet1!$B$2:$B$13` (12 months). Next year the team adds months 13–24 in B14:B25, but the chart still shows only the first 12.

Fix: the range is hardcoded, so new rows are excluded. Convert the source to an Excel Table and point the series at the Table column, or use a dynamic named range `=OFFSET($B$2,0,0,COUNTA($B$2:$B$1000),1)`. Then the series auto-expands. The lesson: never anchor a live chart to a static range.

---

**D2. Spot the error:** A selector uses `=IF(G1="North",B2,IF(G1="South",C2,IF(G1="East",D2)))`. When the user picks "West" (a newly added column E), the cell returns `FALSE`.

Fix: the nested `IF` has no branch for West and no default, so the final `IF` with no value_if_false returns `FALSE`. Replace the whole chain with `=INDEX($B$2:$E$2, MATCH($G$1,$B$1:$E$1,0))`, which finds any header including new ones. Nested `IF`s don't scale; a lookup does.

---

**D3. Spot the error:** A "% of total" pie shows slices of 48%, 30%, 12%, and 15%, summing to 105%.

Fix: the shares don't sum to 100%, so a denominator is wrong — most likely one share divides by a subtotal, not the grand total, or a segment is double-counted. Recompute each as `=segment/SUM($all_segments)` with an absolute-locked total. A pie whose slices exceed 100% is mathematically impossible and instantly discredits the dashboard.

---

**D4. Spot the error:** A column chart of monthly revenue starts its value axis at 900 instead of 0, making a rise from 940 to 1,010 look like the bar tripled.

Fix: for bar/column charts the axis must start at zero — bar length encodes magnitude, and a truncated axis lies about the ratio. Set the axis minimum to 0. (A truncated axis is defensible only on a *line* chart, where slope, not length, carries the message — and even then flag it clearly.)

---

**D5. Spot the error:** Every formula on the dashboard is wrapped in `IFERROR(…,0)`. A deleted source column produces `#REF!`, but the dashboard shows clean zeros and a stakeholder circulates it.

Fix: blanket `IFERROR` masked a structural `#REF!` error, feeding silent zeros into KPIs. Remove the reflexive wrapping; use `IFERROR` only where a miss is genuinely expected and benign (e.g. a lookup that may legitimately not find a match). Structural errors must be allowed to surface so they get fixed.

---

**D6. Spot the error:** The dashboard tab contains original calculation formulas (`=RawData!B2*1.05` etc.) alongside the charts. After a data refresh, half the tiles break.

Fix: logic leaked into the presentation layer, violating the one-way data → calc → dashboard flow. Move all calculation into the working tab and let the dashboard reference only finished results. The presentation layer should hold formatting and cell references, never source logic — that keeps refreshes safe.

---

**D7. Spot the error:** A KPI tile shows revenue with a green up-arrow, but the underlying variance is `=(Budget-Actual)/Budget` and Actual came in *below* budget.

Fix: the variance is computed the wrong way round, so an adverse result shows as a positive number and triggers the green "good" icon. Standardise on `=(Actual-Budget)/Budget` so a shortfall is negative, and tie the icon logic to the sign. A tile that colours bad news green is worse than no tile at all.

---

*Self-verification note:* every percentage and total above was recomputed longhand — B1 (7.83% grossing back to 1,240,000), B2 (South column sum 920), B3 (7.45% QoQ, FY 3,740), B5 (net variance 0), and B6 (shares sum to exactly 100%) all reconcile.
