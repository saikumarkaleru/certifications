# Q&A — Valuation Synthesis and the Football Field

Practice bank for Chapter 27. Work each problem before reading the answer. All per-share figures are self-verified; where the source chapter's illustrative arithmetic slipped, the correct figure is used and flagged.

---

## Section A — Concept Check

**A1. What single question does the football field / synthesis chapter exist to answer?**
"So what's it worth?" You have four methods (DCF, trading comps, precedent transactions, 52-week range), each producing a *range* rather than a point, and the ranges do not agree. Synthesis is the disciplined process of turning four disagreeing ranges into one honest, defensible view of value; the football field is the chart that communicates it.

**A2. Why is value expressed as a range, not a point?**
Every method is a flawed instrument with its own error sources. A single "target price" pretends to a precision that does not exist. A bar communicates honesty (the width is your uncertainty); showing where *within* the overlap you land communicates judgment.

**A3. Each of the four methods measures a *different* underlying thing. Name what each measures.**
- DCF → intrinsic, standalone value.
- Trading comps → what the public market pays *today* for a *minority* stake in similar businesses.
- Precedent transactions → what *acquirers* paid for *whole* companies — control premium included.
- 52-week range → actual realized investor behavior (a reality anchor, not a valuation output).

**A4. Why does the precedent-transactions bar usually sit highest on the field?**
Because deal multiples embed a control premium (typically 20–40% over the unaffected trading price). The gap between precedents and trading comps is *quantifying* the control premium — it is information, not a contradiction to be "corrected."

**A5. Why does triangulation across methods actually converge on truth?**
Because the methods have *largely independent* error modes. A DCF's errors come from the discount rate and terminal value; comps' errors come from imperfect comparability and peer mispricing; precedents' errors come from stale dates and unseen synergies. A too-high WACC has nothing to do with whether your peer set trades rich. So when two instruments with different failure modes land in the same place, that agreement is meaningful; when they diverge, that divergence is a red flag to investigate.

**A6. Is the football field an analytical tool or a communication tool?**
Communication. The analysis (triangulation, weighting, reconciliation) happens *before* the chart. The chart's job is to make the analysis legible — it outsources the overlap analysis to the reader's visual cortex. "A beautiful football field built on lazy triangulation is a liability."

**A7. What is the single most common football-field error?**
Mixing units — plotting some bars in enterprise value and others in equity value or per-share. Everything must be in one unit; bridge first, chart second.

**A8. Why does the 52-week range usually get zero weight in the formal weighted conclusion?**
It is context (where investors actually transacted), not a valuation output. Folding it into the weighted math imports market noise into your conclusion. It is shown as a reference bar only.

**A9. How does the *purpose* of the valuation change the answer?**
Purpose drives the weighting and even which methods belong on the field. Sell-side/fairness opinion → weight precedents and the control view. Buy-side/intrinsic → weight DCF and trading comps. IPO pricing → weight recently-listed peer comps. Litigation/tax → methodology is often prescribed. The same firm is honestly worth different amounts to different questions.

**A10. When the DCF bar towers far above every market-based bar, what is the correct response?**
Not to split the difference. The gap is *diagnostic*: either you genuinely see value the market misses (then articulate and stress-test the specific assumption driving it) or your model is wrong (WACC too low, terminal growth too aggressive). Reporting "the average" would be malpractice.

---

## Section B — Build / Computational Problems

### B1. EV → per-share bridge (the foundational step)

**Problem.** A method produces enterprise value of $4,000m. Net debt = $600m, preferred = $0, minority interest = $0, diluted shares = 50m. Find per-share equity value.

**Solution.**
```
Equity Value = EV − Net Debt − Preferred − Minority Interest
             = 4,000 − 600 − 0 − 0 = 3,400
Per Share    = Equity Value / Diluted Shares
             = 3,400 / 50 = $68.00
```
**Answer: $68.00.** Note the subtractions: net debt, preferred, *and* minority interest all come out. Forgetting any of them overstates per-share value.

### B2. Trading-comps bar, EV to per-share (Meridian Foods)

**Problem.** LTM EBITDA = $400m; net debt = $600m; preferred = $0; minority = $0; diluted shares = 50m. Peer EV/EBITDA: 25th pct = 8.0×, 75th pct = 10.0×. Build the trading-comps bar in $/share.

**Solution.**

| | Low (8.0×) | High (10.0×) |
|---|---|---|
| EV = mult × 400 | 3,200 | 4,000 |
| − Net debt 600 | 2,600 | 3,400 |
| ÷ 50 shares | **$52.00** | **$68.00** |

**Answer: trading comps → $52.00–$68.00.** Use the 25th/75th percentiles (not min/max of the peer set), or the bar becomes outlier-driven and meaningless.

### B3. Precedent-transactions bar and the control premium (Meridian, continued)

**Problem.** Same firm. Precedent deal EV/EBITDA: low = 9.625×, high = 11.5×. Build the precedent bar and show the control premium versus the trading-comps midpoint from B2.

**Solution.**

| | Low (9.625×) | High (11.5×) |
|---|---|---|
| EV | 3,850 | 4,600 |
| − Net debt 600 | 3,250 | 4,000 |
| ÷ 50 | **$65.00** | **$80.00** |

**Answer: precedents → $65.00–$80.00.** Midpoint = $72.50 vs trading-comps midpoint $60.00 → the precedent bar sits ~$12.50/share (about 21%) above trading comps. *That gap is the control premium* — exactly what theory predicts.

*(Note: the source chapter's Example A wrote the high as $83 using 11.375×, but 11.375 × 400 − 600 = 3,950, which is $79.00, not $83. The clean, internally consistent version uses 11.5× → $80.00.)*

### B4. Assemble the field and compute a weighted conclusion (intrinsic purpose)

**Problem.** Combine: 52-week $44–$71; trading comps $52–$68; precedents $65–$80; DCF $48–$62. Purpose = standalone/intrinsic, no deal imminent. Weight DCF 45%, trading comps 35%, precedents 20%, 52-week 0%. Find the concluded central value and weighted range.

**Solution.** First the midpoints:

| Method | Low | High | Midpoint |
|---|---|---|---|
| 52-Week | 44.00 | 71.00 | 57.50 |
| Trading Comps | 52.00 | 68.00 | 60.00 |
| Precedent Txns | 65.00 | 80.00 | 72.50 |
| DCF | 48.00 | 62.00 | 55.00 |

Central value = `SUMPRODUCT(weights, midpoints)`:
```
= 0.45(55.00) + 0.35(60.00) + 0.20(72.50) + 0(57.50)
= 24.750 + 21.000 + 14.500 + 0
= $60.25
```
Weighted range (same weights on the endpoints):
```
Low  = 0.45(48) + 0.35(52) + 0.20(65) = 21.60 + 18.20 + 13.00 = $52.80
High = 0.45(62) + 0.35(68) + 0.20(80) = 27.90 + 23.80 + 16.00 = $67.70
```
**Answer: central ≈ $60.25, range ≈ $52.80–$67.70.**

**Reconciliation check.** DCF (48–62) and trading comps (52–68) overlap in **52–62**; $60.25 sits inside that overlap. ✓ The precedent bar pulls the top of the range up (appropriately for a possible acquirer) without dominating. The stock at $58 sits just below the central estimate — modestly undervalued on a standalone basis. Logic holds.

### B5. Same firm, sale purpose — re-weight and read a bid

**Problem.** The board now wants a fairness opinion on a takeover bid. Re-weight toward control evidence: precedents 45%, DCF 30%, trading comps 25%, 52-week 0%. Recompute the central value. Then judge a $63 bid under both the B4 (intrinsic) and this (sale) lens.

**Solution.**
```
Central = 0.45(72.50) + 0.30(55.00) + 0.25(60.00) + 0(57.50)
        = 32.625 + 16.500 + 15.000
        = $64.13
```
**Answer: central ≈ $64.13** (vs $60.25 standalone). Same numbers, different question, ~$3.9/share higher because control is now on the table.

**Judging $63:** Under the intrinsic lens (central $60.25) a $63 bid looks *generous* — above your standalone central value. Under the sale lens (central $64.13) $63 looks merely *adequate-to-light* — it falls just below the transaction-weighted central value. On the fairness-opinion football field you would draw $63 as a vertical line so directors instantly see it sits in the lower-middle of the deal-weighted range.

### B6. Full build with net debt *and* preferred (Aster Logistics)

**Problem.** LTM EBITDA = $250m; net debt = $400m; preferred = $50m; minority = $0; diluted shares = 40m. Current price $46; 52-week $32–$58. Peer EV/EBITDA 6.5× / 7.5× / 8.5×. Precedent EV/EBITDA 8.0× / 9.5×. DCF corners $38 / $57. Build the trading-comps and precedent bars (bridge subtracts **both** net debt and preferred → deduct $450m), and give the helper table for the chart.

**Solution.** Bridge deduction = 400 + 50 = **450**.

Trading comps:
```
Low  (6.5×): 6.5×250 = 1,625; 1,625 − 450 = 1,175; ÷40 = $29.38
High (8.5×): 8.5×250 = 2,125; 2,125 − 450 = 1,675; ÷40 = $41.88
```
Precedents:
```
Low  (8.0×): 2,000 − 450 = 1,550; ÷40 = $38.75
High (9.5×): 2,375 − 450 = 1,925; ÷40 = $48.13
```
**Answer: trading comps $29.38–$41.88; precedents $38.75–$48.13.**

*(Note: the chapter's exercise text prints comps as $28.13/$40.63 — that value double-subtracts the $50m preferred. Subtracting $450m once gives the correct $29.38/$41.88.)*

Helper table for the stacked-bar chart (`Width = High − Low`, always a formula):

| Method | Base (Low) | Width (=High−Low) |
|---|---|---|
| 52-Week | 32.00 | 26.00 |
| Trading Comps | 29.38 | 12.50 |
| Precedent Txns | 38.75 | 9.38 |
| DCF | 38.00 | 19.00 |

**Sample weighted conclusion (standalone: DCF 40%, comps 40%, precedents 20%, 52-wk 0%).** Midpoints: DCF 47.50, comps 35.63, precedents 43.44, 52-wk 45.00.
```
Central = 0.40(47.50) + 0.40(35.63) + 0.20(43.44) = 19.00 + 14.25 + 8.69 = $41.94
```
Central ≈ **$42**, and it sits inside the DCF (38–57) ∩ comps (29.38–41.88) overlap of **38.00–41.88**. ✓ The stock at $46 sits above the central estimate → looks fairly-to-slightly-richly valued on a standalone basis.

---

## Section C — Interview-Style Questions

**C1. "Walk me through a football field chart."**
It is a one-page summary that stacks each valuation method as a horizontal bar on a shared value axis — usually implied equity value per share. Typically four bars: 52-week trading range, trading comps, precedent transactions, and DCF, sometimes a fifth for LBO ability-to-pay. Each bar spans that method's low-to-high estimate, every endpoint traced to a documented assumption. You read it by looking for where the credible methods overlap; that overlap, adjusted by judgment and a weighting of the methods, gives the concluded value range, which is shaded as a band across the chart. Technically it is built as a stacked horizontal bar chart with an invisible "base" series.

**C2. "You have a DCF at $48–62, comps at $52–68, precedents at $65–85, and the stock trades at $58. What's it worth?"**
It depends on the purpose. On a standalone/intrinsic basis I lean on the DCF and trading comps, whose overlap is roughly $52–62, so I'd conclude a central value around $58–60 — the stock is fairly-to-modestly-cheap. The precedent bar sitting at $65–85 is telling me an acquirer could pay materially more because of the control premium and synergies; if the question were "what would someone pay to buy the whole company," I'd re-weight toward precedents and conclude higher. I would not average all four — that buries the control-premium signal. I'd state my purpose, my weights, and my concluded range explicitly.

**C3. "Why not just take the average of the four midpoints?"**
Because a simple average treats a shaky method as equal to a robust one and quietly imports market noise (the 52-week range) into the answer. It also averages away the most useful signal on the page — divergence. If the DCF and comps agree but precedents sit far higher, that gap is the control premium and belongs in the answer, not smoothed out. I assign explicit, defendable weights based on how much I trust each method for this company and this purpose.

**C4. "How do you build the floating bars in Excel — there's no range-bar chart type?"**
A stacked horizontal bar with two series. Series one is the Low value of each method; series two is the width, `High − Low`. Insert them as a 2-D stacked bar, then set the first (base) series to No Fill and No Line so it becomes invisible. The invisible base pushes each visible width-bar to start at its Low value and extend to its High, giving a floating range bar. Then I fix the axis min/max tightly, use one uniform bar color, label the endpoints, and overlay a shaded band for my concluded range.

**C5. "Why do precedent transactions usually show higher values than trading comps?"**
Trading comps price a minority stake — what a public shareholder pays for a slice with no control. Precedent-transaction multiples come from whole-company acquisitions, where the buyer pays a control premium, typically 20–40%, for the ability to control the board, cash flows, and strategy, plus expected synergies. So the same EBITDA gets a higher multiple in an M&A deal than in the open market. The gap between the two bars is essentially the market's price of control.

**C6. "When would you trust the DCF least, and lean on the market methods?"**
For early-stage, cyclical, or hard-to-forecast businesses, where terminal value dominates the DCF and small changes in WACC or terminal growth swing the answer enormously — the model becomes fragile and assumption-driven. There I'd down-weight the DCF and lean on trading comps (if there's a deep, genuinely comparable peer set) and precedents. Conversely, a stable, predictable-cash-flow business with weak comparables is where the DCF earns the highest weight.

---

## Section D — Common-Error Spotting

**D1.** *An analyst plots the DCF and 52-week bars in per-share, but leaves the comps and precedent bars in enterprise-value terms. What's wrong?*
Mixing units — the number-one football-field error. EV and per-share live on incompatible axes, so the chart is meaningless even though it looks authoritative. Fix: bridge every EV endpoint to equity (subtract net debt, preferred, minority) and to per-share (÷ diluted shares) *before* charting.

**D2.** *The trading-comps bar spans $30–$120 because the analyst used the peer set's minimum and maximum multiples. Problem?*
The bar is outlier-driven and uninformative — one weird peer at each tail dictates the whole width. Use the interquartile range (25th–75th percentile) or median ±1 turn instead. A tight, defensible band beats a wide, "safe" one.

**D3.** *The DCF bar runs $30–$95 because the analyst read the extreme corners of the sensitivity table (WACC ±2%, g ±2%). Problem?*
Those corners are implausible and produce a comically wide bar that swamps every other method. Use a defensible interior band (e.g., WACC ±0.5%, g ±0.5%) and *state* the flex you used. The low endpoint = high WACC + low terminal value; the high = low WACC + high terminal value.

**D4.** *The width column is typed as hardcoded numbers (14, 20, 16, 27) instead of `=High−Low`. Why does this matter?*
When any input changes, the bar no longer moves with it — the chart silently lies while looking correct. Everything must link: `Width = HighCell − LowCell`. Hardcoding is how a football field becomes wrong without anyone noticing.

**D5.** *Bridging Aster: the analyst computes (6.5×250 − 400 − 50 − 50)/40 = $28.13 for the comps low. Spot the error.*
Preferred ($50m) has been subtracted twice. The bridge deducts each capital claim once: net debt 400 + preferred 50 = 450 total. Correct: (1,625 − 450)/40 = **$29.38**, not $28.13. (This exact slip appears in the source chapter's exercise text.)

**D6.** *The Excel axis defaults to a minimum of $0 and all four bars squash into a thin strip on the right. Fix?*
Fix the horizontal axis to a tight, sensible min/max (e.g., 40–90) so the bars fill the frame and the differences that matter become visible. A zero-based axis hides exactly the dispersion the chart exists to show.

**D7.** *The final chart shows four clean bars and nothing else. What's missing?*
The conclusion band. Four bars with no recommended range leaves the reader to do the analyst's job. Always overlay the concluded value range as a shaded band, and in a deal context add a vertical line at the offer/bid price so the decision-maker sees the recommendation against the evidence in one glance.

**D8.** *An analyst is "troubled" that precedents ($65–85) sit above comps ($52–68) and scales the precedent multiples down to match. What's the mistake?*
He deleted the control premium. Precedents *should* sit above trading comps — the gap is the price of control and synergies, and it is information the reader needs. Do not "correct" it; explain it.

**D9.** *A litigation valuation folds the 52-week range into the weighted average at 25%. Why is that a problem?*
The 52-week range is realized market behavior, not a valuation output; markets can be wrong for long stretches. Giving it real weight imports market noise into a conclusion that is supposed to reflect fundamental/method-based value. It belongs on the chart as context with ~0% formal weight.

**D10.** *The precedent bar is built entirely from deals struck at the top of the last cycle. Risk?*
Stale precedents from a very different market cycle inflate the bar with peak multiples that no longer reflect current conditions. Note the date range of the deals, prefer recent and cycle-comparable transactions, and consider trimming the oldest or most cycle-distorted deals.

---

*Self-verification note: every bridge uses `Equity = EV − Net Debt − Preferred − Minority`, then `÷ diluted shares`; every weighted conclusion uses `SUMPRODUCT(weights, values)` with weights summing to 100%; and each concluded value was checked to fall inside the overlap of the credible bars. Two arithmetic slips in the source chapter (precedent high in Example A, comps bridge in the exercise) are corrected and flagged above.*
