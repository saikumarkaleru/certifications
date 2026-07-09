# Q&A — Common-Size, Trend & Cash-Flow Analysis

A mixed bank of conceptual and numerical questions. Numericals are fully solved and reconciled. For theory questions, an "In an interview, say:" line gives you the crisp phrasing to deliver out loud.

---

## Conceptual / Theory

### Q1. What is common-size (vertical) analysis and what problem does it solve?

**Answer.** Common-size analysis restates every line of a statement as a percentage of a single same-period base — every income-statement line ÷ revenue, every balance-sheet line ÷ total assets. The problem it solves is **comparability across size**: absolute rupees are dominated by scale, so a large and a small company can't be compared directly, and the *structure* of a business (cost mix, margins, capital structure) is invisible. Dividing size out leaves the economic shape, which is directly comparable across firms and across years.

**In an interview, say:** "Common-size strips out size by expressing everything as a % of revenue or total assets, so I can compare a giant with a minnow and see the structure — margins and cost mix — at a glance."

---

### Q2. How does horizontal (trend) analysis differ from vertical analysis, and why use both?

**Answer.** Vertical analysis compares lines *within one period* (shape). Horizontal analysis compares each line *to its own past* (direction), as YoY % change or as an index to a base year. They are complements: vertical tells you the shape of the business now; horizontal tells you which way it's moving and how fast. Used together they produce the "scissors" insight — e.g., indexing revenue and net income to a base year and watching them fan apart reveals margin erosion that neither lens shows alone.

**In an interview, say:** "Vertical is the snapshot, horizontal is the movie. I run both — common-size for structure, trend indexing for direction — because the revenue-vs-earnings scissors only shows up when you overlay them."

---

### Q3. Why is CAGR preferred over the arithmetic average of annual growth rates?

**Answer.** Growth compounds, so the right average is geometric, not arithmetic. The arithmetic mean of yearly growth rates *overstates* true compounded growth whenever rates vary (geometric mean ≤ arithmetic mean). Classic proof: +50% then −50% has an arithmetic mean of 0%, but 1.5 × 0.5 = 0.75, a 25% loss; the honest CAGR is 0.75^(1/2) − 1 = −13.4%. CAGR = (V_end / V_begin)^(1/n) − 1, with **n = number of periods (gaps), not data points**.

**In an interview, say:** "Because growth compounds, I use the geometric CAGR — the arithmetic average of annual rates always overstates it. And n is the number of years between the endpoints, not the count of figures."

---

### Q4. What are the two big limitations of CAGR?

**Answer.** (1) **Path-blindness / smoothing:** CAGR reports a fake-steady equivalent rate and is completely blind to the shape in between — 5%,5%,5%,45% has the same CAGR as a steady 15%, but they're very different businesses. (2) **Endpoint (base-year) sensitivity:** pick a trough as the base and any CAGR looks heroic; pick a peak and it looks dismal. Analysts game this in decks. Always pair CAGR with the year-by-year series and sanity-check the base year.

**In an interview, say:** "CAGR smooths the path and bends to the base year. I always show it next to the annual series and check nobody cherry-picked a trough as year zero."

---

### Q5. Why does accrual accounting make CFO a better reality check than net income?

**Answer.** Accrual accounting deliberately decouples profit from cash — revenue is booked when *earned*, expenses matched to revenue, not to cash movement. That produces a truer single-period picture but hands management legitimate levers (estimates, timing, capitalisation) to flatter profit without cash arriving. Cash is hard to fake — "cash is a fact, profit is an opinion." So comparing CFO to net income tests whether reported earnings are actually being collected.

**In an interview, say:** "Accrual accounting separates profit from cash by design, which lets estimates and timing flatter earnings. Cash can't be faked as easily, so CFO versus net income is my earnings-quality litmus test."

---

### Q6. Define FCFF and FCFE and give the bridge between them.

**Answer.**
- **FCFF** (to firm, unlevered) = EBIT×(1−t) + D&A − Capex − ΔNWC. Cash to *all* providers; discount at WACC.
- **FCFE** (to equity, levered) = Net income + D&A − Capex − ΔNWC + Net borrowing. Cash to equity only; discount at cost of equity.
- **Bridge:** FCFF = FCFE + Interest×(1−t) − Net borrowing.
- Quick proxy used constantly: **simple FCF = CFO − Capex.**

After-tax interest is added back for FCFF because FCFF is a *pre-financing* pool — remove the financing cost, and only after-tax because interest is deductible.

**In an interview, say:** "FCFF is pre-financing to everyone, EBIT after tax plus D&A less capex and working-capital investment. FCFE strips debt effects and is net-income based. Bridge: FCFF equals FCFE plus after-tax interest minus net borrowing."

---

### Q7. What is the cash conversion cycle, and what does a negative CCC signify?

**Answer.** CCC = DIO + DSO − DPO — the number of days a rupee is trapped between paying suppliers and collecting from customers. DIO + DSO is cash tied up; DPO is the free financing suppliers grant. Lower is better. A **negative CCC** means the firm collects from customers *before* it pays suppliers — customers and suppliers fund its working capital. It's a structural cash machine (Amazon, peak Dell) that funds growth without external capital.

**In an interview, say:** "CCC is DIO plus DSO minus DPO — the days cash is stuck in operations. Negative means suppliers and customers finance you; that's a self-funding growth engine."

---

### Q8. A company reports rising profits. What five things would make you suspicious of earnings quality?

**Answer.**
1. **CFO growing slower than net income** (cash-conversion ratio < 1 and falling).
2. **Rising DSO** — revenue booked faster than collected (aggressive recognition / channel stuffing).
3. **Inventory building faster than COGS** — obsolescence or demand miss.
4. **Capex persistently above D&A** with quiet capitalisation of ordinary costs (protects CFO and P&L).
5. **Reliance on non-recurring gains** (asset sales, settlements) inflating headline profit.
High accruals (net income − CFO) are statistically linked to future underperformance (Sloan's accruals anomaly).

**In an interview, say:** "I check whether cash follows the profit: CFO lagging net income, DSO creeping up, inventory outrunning COGS, capex above D&A, and one-off gains propping up the P&L. A widening accruals gap is my first red flag."

---

### Q9. Under IFRS, is CFO comparable across companies? Contrast with US GAAP.

**Answer.** Not without checking. **IAS 7** lets firms classify interest paid and dividends paid in either CFO or CFF, and interest/dividends received in CFO or CFI — a policy choice. **US GAAP (ASC 230)** is stricter: interest paid and interest/dividends received sit in CFO, dividends paid in CFF. So CFO under IFRS isn't strictly comparable across a peer set until you normalise everyone to the same classification.

**In an interview, say:** "Under IAS 7, interest and dividend classification is a policy choice, so IFRS CFO isn't apples-to-apples. US GAAP forces interest into CFO and dividends paid into CFF. I normalise before benchmarking."

---

### Q10. What is segment analysis and why does a group margin mislead?

**Answer.** Under **IFRS 8 / ASC 280** (management approach), firms disclose revenue, profit, assets, and often capex by operating segment. A consolidated margin is a weighted average that hides its composition — a 9% group margin could be a 35%-margin jewel subsidising a loss-making unit. Segment analysis restores that information: compute per-segment margins, growth, and capital consumption; find value creators and destroyers; then sum-of-the-parts value each on its own multiple to test for a conglomerate discount and a break-up thesis.

**In an interview, say:** "A blended margin is an average that hides dispersion. I pull IFRS 8 segments, compute margin and capital use per unit, and run a sum-of-the-parts — that's how you find the conglomerate discount and the value-unlock thesis."

---

### Q11. What is the sustainable growth rate and why does it matter?

**Answer.** SGR = ROE × (1 − dividend payout) = ROE × retention ratio. It's the rate a firm can grow **without issuing new equity**, self-funded from retained profits at its current profitability and reinvestment. It matters because it ties growth ambitions back to reality: if a firm targets growth above its SGR, it must raise external equity, take on more leverage, or improve ROE — otherwise the plan doesn't fund itself.

**In an interview, say:** "SGR is ROE times retention — the growth a firm can fund from its own retained earnings. Grow faster than that and you need new equity, more debt, or higher returns."

---

### Q12. Explain the working-capital sign convention in the indirect cash flow statement.

**Answer.** Starting from net income to get CFO: **an increase in an operating asset is a *use* of cash (subtract); an increase in an operating liability is a *source* of cash (add).** Receivables up → sales booked but not collected → subtract. Inventory up → cash tied in stock → subtract. Payables up → bought on credit, cash retained → add. Reversing any of these signs flips CFO and is a classic error.

**In an interview, say:** "Increase in an operating asset uses cash, increase in an operating liability provides cash. Receivables and inventory up are subtractions; payables up is an addition."

---

### Q13. How do you build a clean peer/comp set for benchmarking?

**Answer.** Same industry and business model, similar size, geography, and accounting regime. **Normalise for accounting differences** (IFRS vs GAAP, lease treatment, one-offs) before comparing. Match the metric to the claimant: enterprise metrics (EV/EBITDA, EV/Sales) vs enterprise metrics; equity metrics (P/E, ROE) vs equity metrics — never compare levered metrics across firms with very different capital structures without adjusting. Triangulate cross-sectional (vs peers today) with time-series (vs own history): a metric strong on both is genuinely strong; strong vs history but weak vs peers just means the whole industry improved.

**In an interview, say:** "Clean comps means same model, size, geography, and accounting — normalised for one-offs and lease treatment — and I match enterprise metrics to enterprise, equity to equity. Then I triangulate versus peers and versus the company's own history."

---

## Numerical Problems

### Q14. Common-size and margin migration

A company reports:

| Line | Year 1 | Year 2 |
|---|---:|---:|
| Revenue | 800 | 1,000 |
| COGS | 480 | 640 |
| SG&A | 160 | 210 |
| Depreciation | 40 | 50 |
| Interest | 20 | 30 |
| Tax @ 25% | 25 | 17.5 |

Compute common-size margins and explain the story.

**Solution.**
First derive the ladder.
- Year 1: Gross = 800 − 480 = 320; EBIT = 320 − 160 − 40 = 120; PBT = 120 − 20 = 100; Tax 25; NI = 75.
- Year 2: Gross = 1,000 − 640 = 360; EBIT = 360 − 210 − 50 = 100; PBT = 100 − 30 = 70; Tax 17.5; NI = 52.5.

Common-size (÷ revenue):

| Line | Year 1 | Year 2 |
|---|---:|---:|
| Revenue | 100.0% | 100.0% |
| COGS | 60.0% | 64.0% |
| Gross margin | 40.0% | 36.0% |
| SG&A | 20.0% | 21.0% |
| EBIT margin | 15.0% | 10.0% |
| Net margin | 9.375% | 5.25% |

*Checks:* Y2 COGS 640/1,000 = 64% ✓; EBIT 100/1,000 = 10% ✓; NI 52.5/1,000 = 5.25% ✓; Y1 tax 25 = 25% of PBT 100 ✓, Y2 tax 17.5 = 25% of 70 ✓.

**Story:** revenue grew 25% but net income *fell* from 75 to 52.5 (−30%). Gross margin dropped 400 bps (COGS grew 33% vs revenue 25%), SG&A deleveraged (+100 bps), and higher interest compounded it. EBIT margin collapsed 500 bps. Textbook unprofitable growth.

---

### Q15. CAGR with the period-count trap

Revenue: FY19 = 250, FY24 = 500. Six annual figures are printed (FY19–FY24). Compute the revenue CAGR.

**Solution.** The endpoints span FY19→FY24 = **5 periods** (not 6 — six data points, five gaps).
$$\text{CAGR} = \left(\frac{500}{250}\right)^{1/5} - 1 = 2^{0.2} - 1 = 1.1487 - 1 = 14.87\%$$

*Check:* 250 × 1.1487^5 = 250 × 2.0 = 500 ✓.

**Trap flagged:** using n = 6 gives 2^(1/6) − 1 = 12.25%, understating the true 14.87%. Always count gaps between the first and last year.

---

### Q16. The growth scissors — revenue vs earnings index

| Year | Revenue | Net income |
|---|---:|---:|
| Y0 | 400 | 48 |
| Y1 | 480 | 53 |
| Y2 | 560 | 56 |
| Y3 | 660 | 59 |
| Y4 | 800 | 60 |

Index both to Y0 = 100, compute both CAGRs (n = 4), and state the conclusion.

**Solution.**

| Year | Rev index | NI index | Net margin |
|---|---:|---:|---:|
| Y0 | 100 | 100 | 12.0% |
| Y1 | 120 | 110 | 11.04% |
| Y2 | 140 | 117 | 10.0% |
| Y3 | 165 | 123 | 8.94% |
| Y4 | 200 | 125 | 7.5% |

Revenue CAGR = (800/400)^(1/4) − 1 = 2^0.25 − 1 = **18.92%.**
Net income CAGR = (60/48)^(1/4) − 1 = 1.25^0.25 − 1 = **5.74%.**

*Checks:* Y4 margin 60/800 = 7.5% ✓; rev index 800/400×100 = 200 ✓; NI index 60/48×100 = 125 ✓.

**Conclusion:** revenue doubled (index 200) while net income rose only 25% (index 125) — a widening scissors. Net margin eroded every year, 12.0% → 7.5% (450 bps). The 18.9% revenue CAGR is a vanity metric; earnings compounded at just 5.7%. Growth is bought, not earned.

---

### Q17. Full CFO build (indirect method)

Given: Net income 220; Depreciation 90; Amortisation 15; Stock-based comp 25; Gain on sale of equipment 10; Receivables +70; Inventory +40; Prepaid expenses +5; Payables +35; Accrued expenses +12. Compute CFO.

**Solution.**

| | Amount |
|---|---:|
| Net income | 220 |
| + Depreciation | +90 |
| + Amortisation | +15 |
| + Stock-based comp | +25 |
| − Gain on sale (reclass to CFI) | −10 |
| − Increase in receivables | −70 |
| − Increase in inventory | −40 |
| − Increase in prepaids | −5 |
| + Increase in payables | +35 |
| + Increase in accrued expenses | +12 |
| **CFO** | **272** |

*Check:* 220 + 90 + 15 + 25 − 10 − 70 − 40 − 5 + 35 + 12 = 272 ✓.

Note the gain on sale is *subtracted* from CFO (its cash proceeds belong in CFI); non-cash add-backs (D&A, SBC) are added; operating-asset increases subtracted; operating-liability increases added.

---

### Q18. FCFF, FCFE, and simple FCF from one data set

Given: EBIT 300; tax rate 25%; D&A 90; Capex 130; ΔNWC +40; Interest expense 50; Net borrowing +60; Net income = (EBIT − interest)×(1−t) = (300 − 50)×0.75 = 187.5. Compute simple FCF (CFO − capex), FCFF, and FCFE, and verify the bridge.

**Solution.**
First, CFO (indirect, simplified): NI 187.5 + D&A 90 − ΔNWC 40 = 237.5.
- **Simple FCF = CFO − Capex** = 237.5 − 130 = **107.5.**
- **FCFF = EBIT×(1−t) + D&A − Capex − ΔNWC** = 300×0.75 + 90 − 130 − 40 = 225 + 90 − 130 − 40 = **145.**
- **FCFE = NI + D&A − Capex − ΔNWC + Net borrowing** = 187.5 + 90 − 130 − 40 + 60 = **167.5.**

**Bridge check:** FCFF = FCFE + Interest×(1−t) − Net borrowing = 167.5 + 50×0.75 − 60 = 167.5 + 37.5 − 60 = **145** ✓.

Also FCFF via CFO: CFO + Interest×(1−t) − Capex = 237.5 + 37.5 − 130 = 145 ✓.

---

### Q19. Cash conversion cycle

COGS 1,500; Revenue 2,400. Average inventory 300; average receivables 400; average payables 250. Compute DIO, DSO, DPO and the CCC. Interpret.

**Solution.**
- DIO = (300 / 1,500) × 365 = 0.20 × 365 = **73.0 days**
- DSO = (400 / 2,400) × 365 = 0.16667 × 365 = **60.83 days**
- DPO = (250 / 1,500) × 365 = 0.16667 × 365 = **60.83 days**
- **CCC = 73.0 + 60.83 − 60.83 = 73.0 days**

*Check:* DSO and DPO happen to be equal here (400/2,400 = 250/1,500 = 0.1667), so they cancel and CCC = DIO. Cash is tied up ~73 days — entirely in inventory in this case. To improve, the firm should turn inventory faster or stretch supplier terms (raise DPO).

---

### Q20. Quality of earnings — spotting the accrual gap

Two companies, same reported net income of 150:

| | Alpha | Beta |
|---|---:|---:|
| Net income | 150 | 150 |
| D&A | 60 | 60 |
| Δ Receivables | +20 | +130 |
| Δ Inventory | +10 | +60 |
| Δ Payables | +15 | +5 |

Compute CFO, the cash-conversion ratio, and accruals for each. Which is higher quality?

**Solution.**
- **Alpha CFO** = 150 + 60 − 20 − 10 + 15 = **195.** Ratio = 195/150 = **1.30.** Accruals = 150 − 195 = **−45** (cash exceeds profit).
- **Beta CFO** = 150 + 60 − 130 − 60 + 5 = **25.** Ratio = 25/150 = **0.17.** Accruals = 150 − 25 = **+125.**

*Checks:* Alpha 150+60−20−10+15 = 195 ✓; Beta 150+60−130−60+5 = 25 ✓.

**Verdict:** Alpha is far higher quality — CFO exceeds net income (ratio 1.3, negative accruals: profit is fully cash-backed). Beta reports identical profit but converts only 17% to cash, with a huge +125 accrual driven by a ₹130 receivables build and ₹60 inventory build. Beta's earnings are a red flag: possibly aggressive revenue recognition or channel stuffing. Same headline profit, completely different reality — exactly why you never stop at net income.

---

### Q21. Segment analysis and margin unlock

| Segment | Revenue | EBIT |
|---|---:|---:|
| Cloud | 500 | 175 |
| Devices | 800 | 64 |
| Retail | 700 | −35 |

Compute each segment margin, the group margin, and the group margin if Retail is divested.

**Solution.**
- Cloud margin = 175/500 = **35.0%**
- Devices margin = 64/800 = **8.0%**
- Retail margin = −35/700 = **−5.0%**
- Group EBIT = 175 + 64 − 35 = 204; Group revenue = 500 + 800 + 700 = 2,000; **Group margin = 204/2,000 = 10.2%.**
- **Ex-Retail:** EBIT = 175 + 64 = 239; Revenue = 500 + 800 = 1,300; margin = 239/1,300 = **18.38%.**

*Checks:* 35% ✓, 8% ✓, −5% ✓; group 204/2,000 = 10.2% ✓; ex-Retail 239/1,300 = 18.38% ✓.

**Insight:** the 10.2% blended margin hides a 35%-margin Cloud jewel dragged by a loss-making Retail arm consuming 35% of revenue. Divesting Retail lifts group margin to 18.4% — an 820 bps jump — and a sum-of-the-parts valuation (Cloud on a rich multiple, Devices on an industrial one) likely exceeds the consolidated market value. Classic break-up / value-unlock thesis.

---

### Q22. Putting it together — is the growth real?

A company grows revenue from 1,000 (Y0) to 1,600 (Y2), net income from 100 to 150, and CFO from 110 to 95 over the same span. DSO went from 45 to 78 days. Compute the revenue and NI CAGRs (n = 2), the cash-conversion ratio in each year, and give a one-line verdict.

**Solution.**
- Revenue CAGR = (1,600/1,000)^(1/2) − 1 = 1.6^0.5 − 1 = 1.2649 − 1 = **26.5%.**
- NI CAGR = (150/100)^(1/2) − 1 = 1.5^0.5 − 1 = 1.2247 − 1 = **22.5%.**
- Cash-conversion Y0 = 110/100 = **1.10** (healthy); Y2 = 95/150 = **0.63** (poor).

*Checks:* 1.2649² = 1.6 ✓; 1.2247² = 1.5 ✓.

**Verdict:** headline growth looks strong (revenue +26.5% CAGR, earnings +22.5%), but the story falls apart on cash. CFO *fell* from 110 to 95 even as profit rose 50%, so cash conversion collapsed from 1.10 to 0.63, and DSO nearly doubled (45→78 days). The growth and profit are not converting to cash — receivables are ballooning. This is aggressive-recognition or channel-stuffing territory; I'd discount the earnings heavily and drill into revenue quality and collections.

**In an interview, say:** "Great-looking growth, but CFO fell while profit rose and DSO jumped from 45 to 78 days — cash conversion dropped from 1.1 to 0.63. The profit isn't turning into cash; I'd suspect aggressive revenue recognition before I'd trust the numbers."
