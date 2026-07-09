# Q&A — DCF Sensitivity, Scenarios & the Football Field

A mixed bank of theory and fully-solved numerical questions. Numbers are self-verified and reconcile (EV-to-equity bridges close, per-share math checks out). For theory questions, an "In an interview, say it like this" line gives you the crisp version to speak.

---

## Theory

### Q1. Why does a DCF produce a range rather than a single number?

A DCF value is a function of ~40 uncertain inputs (growth, margins, capex, WACC, terminal g, etc.) stacked multiplicatively. Each input carries estimation error, and the output inherits all of it. The single cell the spreadsheet reports is one point drawn from a distribution of possible values; treating it as *the* value confuses arithmetic precision with real-world accuracy. The honest output characterizes the distribution — a most-likely value inside a bounded range.

**In an interview, say it like this:** "The $65 is the center of a distribution, not a fact. A DCF stacks dozens of uncertain assumptions, so the deliverable is a range with a base case inside it — that's why I always run sensitivity and scenarios."

---

### Q2. Why are WACC and terminal growth the two inputs a DCF is most sensitive to?

Two reasons compound. First, **terminal value is usually 60–80% of total EV**, so the terminal assumptions dominate the answer. Second, the Gordon terminal value has `WACC − g` in the denominator — a *difference of two close, uncertain numbers*. When you subtract two numbers that are near each other, the relative error blows up: a 0.5-point move in a ~6-point spread is a ~9% swing in value. Value is therefore *hyperbolically* (not linearly) sensitive to both. That is exactly why the standard two-way table puts WACC on one axis and g on the other.

**In an interview, say it like this:** "Most of the value is terminal, and the terminal value is a perpetuity with `WACC minus g` on the bottom. Those two numbers are close, so small changes move value a lot — that's what the WACC-versus-g table exists to show."

---

### Q3. What is the difference between a sensitivity (data) table and a scenario analysis?

A **data table** flexes one or two inputs at a time, *holding everything else constant*, to reveal the mechanical sensitivity of value to that input — it answers "which lever matters?" A **scenario** bundles many inputs into a coherent story (bear/base/bull) and moves the *correlated* ones together, respecting that in a downturn growth, margins, and multiples all fall at once — it answers "what if the whole story changes?" Data tables ignore correlation by design; scenarios exist precisely to capture it. One-at-a-time sensitivity understates true downside because it doesn't let bad news cluster.

**In an interview, say it like this:** "A data table isolates one variable to show sensitivity; a scenario moves correlated variables together to tell a consistent story. I use tables to find the swing factors and scenarios to bound the realistic range."

---

### Q4. What is a reverse DCF and why is it so useful?

A reverse DCF takes the **market price as given** and solves for the assumption the market must be making — typically terminal growth or the revenue CAGR — by setting the model's per-share output equal to the current price and goal-seeking. It inverts the burden of proof: instead of defending your own forty assumptions, you extract the *one* assumption embedded in the price and ask whether it's believable. If the implied perpetual growth exceeds long-run nominal GDP (~4%), the stock is priced for perfection.

**In an interview, say it like this:** "I set the DCF output equal to the price and solve for the growth the market is implying. If the price requires 6% perpetual growth, the market is betting this company beats GDP forever — that's a testable, and usually losing, claim."

---

### Q5. What is a football field and how do you read one?

A football field is a horizontal bar chart stacking the value *range* from each valuation method — DCF (sensitivity and scenario), trading comps, precedent transactions, 52-week range, LBO, analyst targets — on one page, with the current or offer price marked as a line. You read it by finding the **overlap zone** where most bars intersect: that is the robust, defensible value, because independent methods with different biases rarely all err in the same direction. Outlier bars get interrogated.

**In an interview, say it like this:** "It's triangulation on one page. Each method has different biases, so where the bars overlap is the value I'd defend. It also keeps the presentation honest — a range, not false precision."

---

### Q6. On a football field, why do precedent transactions usually sit above trading comps?

Precedent-transaction multiples come from completed M&A deals, which embed a **control premium** — an acquirer pays extra to own 100% of the company and capture synergies. Trading comps reflect **minority, no-control** stakes at market-clearing prices, so they're lower. The ordering is a direct consequence of *what each method measures*: acquisition value versus market value.

**In an interview, say it like this:** "Precedents include a control premium for owning the whole company and capturing synergies; comps are minority stakes at market price. So precedents typically sit highest on the field."

---

### Q7. What does Monte-Carlo add over three scenarios, and what's its limitation?

Three scenarios give three discrete points; **Monte-Carlo** assigns each input a probability distribution (and, crucially, specifies correlations between inputs), draws thousands of joint samples, and produces the *full distribution* of value. That lets you make probability statements — "68% chance intrinsic value exceeds the price," "P10–P90 range of $54–$79." Its limitation: output quality is entirely bounded by the assumed distributions and correlations — garbage in, garbage out, just with a pretty histogram. It forces explicit uncertainty; it does not manufacture confidence.

**In an interview, say it like this:** "Monte-Carlo turns three cases into a full distribution so I can say '70% chance the value beats the price.' But it's only as good as my input distributions and the correlations between them — it doesn't create precision, it just makes my uncertainty explicit."

---

### Q8. Why is it wrong to run a one-way sensitivity that only drops revenue growth in your bear case?

Because assumptions are **correlated**. In a genuine downturn, revenue growth slows, operating margins compress (operating leverage reverses), the cost of capital rises (risk premia widen), and exit multiples contract — *all together, all in the same direction*. Dropping growth alone while holding margins, WACC, and the multiple constant produces a bear case that is far too kind and *understates* the true downside. Correlated inputs belong in a scenario that moves them jointly.

**In an interview, say it like this:** "Bad news clusters. A real bear case isn't 'growth is 2% lower' — it's lower growth *and* thinner margins *and* higher WACC *and* a lower exit multiple, because those all move together in a downturn."

---

### Q9. How should you present a value range to an MD or PM in under a minute?

Lead with one headline line — "$58 to $72, base case $65, price $60." Then one sentence on what drives the low end (bear scenario / high WACC), one on the high end (bull / low WACC), one on the key swing factor from the tornado analysis, and one reverse-DCF punchline on what the current price is implying. Concede the softest assumption, then show the *decision* is robust to it.

**In an interview, say it like this:** "Value's $58–$72, base $65, price $60. Low end is the bear margin case, high end is share gains. The whole call hinges on terminal margin. And at $60 the market's only implying 2% perpetual growth, which I think is too low — so, modest upside."

---

### Q10. Your interviewer says "I don't believe your 3% growth assumption." How do you respond?

Don't dig in on the point. First concede and bound: "Fair — growth is the softest input, which is why I ran it from 1.5% to 3.0%; that moves value from $58 to $72, and even at the low end the decision holds." Then flip to reverse DCF: "Set my number aside — the *current price itself* requires 4% perpetual growth to justify, which exceeds nominal GDP. So the market is already assuming more than I am. Do you believe this company beats the economy forever?" This turns a vague disagreement about your number into a concrete question about the price's embedded assumption.

**In an interview, say it like this:** "You may be right that 3% is soft — that's why I sensitized it. But notice the price already implies 4%, above GDP. So my assumption is actually the conservative one."

---

## Numerical

### Q11. Base-case DCF, full bridge to per share.

**Given:** PV of explicit 5-year FCFF = $500m. Year-5 FCFF = $90m. WACC = 9%, terminal g = 2.5%. Net debt = $250m. Preferred = $40m. Diluted shares = 60m. Find value per share.

**Solution.**
```
FCFF₆ = 90 × 1.025 = 92.25
TV₅ = 92.25 / (0.09 − 0.025) = 92.25 / 0.065 = 1,419.23
1.09⁵ = 1.538624
PV(TV) = 1,419.23 / 1.538624 = 922.40
EV = 500 + 922.40 = 1,422.40
Equity = EV − Net Debt − Preferred = 1,422.40 − 250 − 40 = 1,132.40
Per share = 1,132.40 / 60 = $18.87
```
**Answer: $18.87.** Note TV is 922.40 / 1,422.40 = **64.8% of EV** — most of the value is terminal.

---

### Q12. Two-way sensitivity: quantify the swing.

Using Q11's base case, recompute value per share at (WACC 8.5%, g 2.5%) and at (WACC 9.5%, g 2.5%). By how much does a ±0.5-point WACC move shift the value?

**Solution.**
- **WACC 8.5%:** TV = 92.25/(0.085−0.025) = 92.25/0.06 = 1,537.50; 1.085⁵ = 1.503657; PV(TV) = 1,537.50/1.503657 = 1,022.51; EV = 500+1,022.51 = 1,522.51; Equity = 1,522.51−250−40 = 1,232.51; /60 = **$20.54**.
- **WACC 9.5%:** TV = 92.25/(0.095−0.025) = 92.25/0.07 = 1,317.86; 1.095⁵ = 1.574239; PV(TV) = 1,317.86/1.574239 = 837.16; EV = 500+837.16 = 1,337.16; Equity = 1,337.16−250−40 = 1,047.16; /60 = **$17.45**.

**Answer.** Value runs from **$17.45 (9.5%) to $20.54 (8.5%)** around the $18.87 base — a 0.5-point WACC change up moves value −$1.42 (−7.5%), down moves it +$1.67 (+8.9%). The asymmetry (bigger up-move than down-move) is the `1/(WACC−g)` convexity. Takeaway: a single ±0.5% WACC uncertainty already swings value ~±8%.

---

### Q13. Reverse DCF for implied growth.

**Given:** Stock trades at $50. Shares = 100m → equity = $5,000m. Net debt = $1,000m → market EV = $6,000m. PV of explicit FCFF = $1,200m at WACC = 8%. Year-5 FCFF = $250m. What terminal g is the market implying?

**Solution.**
```
PV(TV) = 6,000 − 1,200 = 4,800
1.08⁵ = 1.469328
TV₅ = 4,800 × 1.469328 = 7,052.8
7,052.8 = 250 × (1+g)/(0.08 − g)
7,052.8 × (0.08 − g) = 250 + 250g
564.22 − 7,052.8g = 250 + 250g
564.22 − 250 = 250g + 7,052.8g
314.22 = 7,302.8g
g = 0.04303 ≈ 4.30%
```
**Verify:** TV₅ = 250×1.04303/(0.08−0.04303) = 260.76/0.03697 = 7,053; PV = 7,053/1.469328 = 4,800; EV = 1,200+4,800 = 6,000 ✓.

**Answer: implied g ≈ 4.30%** — slightly above nominal GDP (~4%). The market is pricing in modestly-above-economy perpetual growth. Verdict: fully valued to slightly rich unless you believe the terminal growth genuinely clears GDP.

---

### Q14. Probability-weighted scenario value with a full bridge.

**Given:** Three scenarios produce enterprise values Bear $1,800m, Base $3,200m, Bull $4,500m. Bridge (same each case): net debt $900m, minority interest $100m, non-operating assets +$150m. Shares = 80m. Probabilities 25% / 55% / 20%. Find each per-share value and the probability-weighted value.

**Solution.** Bridge: Equity = EV − 900 − 100 + 150 = EV − 850.
- Bear: 1,800 − 850 = 950 → /80 = **$11.88**
- Base: 3,200 − 850 = 2,350 → /80 = **$29.38**
- Bull: 4,500 − 850 = 3,650 → /80 = **$45.63**

Probability-weighted equity = 0.25×950 + 0.55×2,350 + 0.20×3,650 = 237.5 + 1,292.5 + 730 = 2,260 → /80 = **$28.25**.
Cross-check via per-share: 0.25×11.88 + 0.55×29.38 + 0.20×45.63 = 2.97 + 16.16 + 9.13 = **$28.25** ✓.

**Answer.** Range **$11.88 to $45.63**, base **$29.38**, probability-weighted **$28.25** (below base, because bear weight 25% > bull weight 20% — a downward skew).

---

### Q15. Exit-multiple terminal value vs. Gordon — reconcile the implied growth.

**Given:** Year-5 EBITDA = $400m, exit EV/EBITDA = 8.0× → TV₅ = $3,200m. Year-5 FCFF = $180m, WACC = 9%. What terminal growth does the 8.0× exit multiple *imply*?

**Solution.** Set Gordon TV equal to the exit-multiple TV and solve for g:
```
3,200 = 180 × (1+g)/(0.09 − g)
3,200 × (0.09 − g) = 180 + 180g
288 − 3,200g = 180 + 180g
288 − 180 = 3,200g + 180g
108 = 3,380g
g = 0.03195 ≈ 3.20%
```
**Verify:** 180×1.0320/(0.09−0.0320) = 185.75/0.0580 = 3,203 ≈ 3,200 ✓.

**Answer: the 8.0× exit multiple implies ~3.2% perpetual growth.** This is the standard cross-check: whenever you use an exit multiple, back out the implied g and confirm it's sensible (≤ GDP). At 3.2% it's reasonable; if it had implied 6%, the exit multiple would be too aggressive.

---

### Q16. TV as a share of EV — why terminal assumptions dominate.

**Given:** PV of explicit FCFF = $350m. PV of terminal value = $1,150m. What fraction of EV is terminal, and if your terminal g estimate is off such that PV(TV) is actually 10% higher, how much does total EV move?

**Solution.**
```
EV = 350 + 1,150 = 1,500
TV share = 1,150 / 1,500 = 76.7%
If PV(TV) rises 10%: new PV(TV) = 1,150 × 1.10 = 1,265
New EV = 350 + 1,265 = 1,615
EV change = 1,615/1,500 − 1 = +7.7%
```
**Answer.** Terminal value is **76.7% of EV**; a 10% error in the terminal value moves total EV by **7.7%**. Lesson: because TV is three-quarters of the answer, terminal-assumption error passes almost directly through to value — sensitize the terminal value first.

---

### Q17. Building a mini two-way table (exit multiple × WACC).

**Given:** Year-5 EBITDA = $300m. PV of explicit FCFF = $250m (treat as fixed). Net debt = $400m. Shares = 40m. Fill per-share values for exit multiples {7×, 8×, 9×} and WACC {8%, 9%}.

**Solution.** TV₅ = EBITDA × multiple; PV(TV) = TV₅/(1+WACC)⁵; discount factors 1.08⁵=1.469328, 1.09⁵=1.538624. Equity = 250 + PV(TV) − 400; /40.

- **7× → TV = 2,100:** WACC 8%: PV=2,100/1.469328=1,429.2; Eq=250+1,429.2−400=1,279.2; /40=**$31.98**. WACC 9%: PV=2,100/1.538624=1,364.8; Eq=1,214.8; /40=**$30.37**.
- **8× → TV = 2,400:** WACC 8%: PV=1,633.4; Eq=1,483.4; /40=**$37.08**. WACC 9%: PV=1,559.8; Eq=1,409.8; /40=**$35.24**.
- **9× → TV = 2,700:** WACC 8%: PV=1,837.6; Eq=1,687.6; /40=**$42.19**. WACC 9%: PV=1,754.8; Eq=1,604.8; /40=**$40.12**.

| Exit ↓ / WACC → | 8% | 9% |
|---|---|---|
| 7× | $31.98 | $30.37 |
| 8× | $37.08 | $35.24 |
| 9× | $42.19 | $40.12 |

**Answer.** Value spans **$30.37 to $42.19**. The exit multiple (vertical) drives value far more than the 1-point WACC step here — a sign that for this company the terminal *multiple* is the dominant lever, which is where diligence should concentrate.

---

### Q18. Expected value and probability of upside.

**Given:** A Monte-Carlo run yields per-share values with these summary stats: mean $63, median $60, P10 $48, P90 $82. Current price $55. 62% of simulated draws exceed $55. How do you summarize this to a PM?

**Solution / model summary.** "Intrinsic value has a mean of $63 and a median of $60 — the mean above the median tells you the distribution is right-skewed, upside-tailed. The practical range is $48 to $82 (P10–P90). Most importantly, 62% of simulations put value above the $55 price, so the modeled probability of upside is about 62%. The base case supports a long, but the 38% downside tail to $48 (−13%) is real, so size accordingly."

**Answer.** Key numbers to lead with: **P(value > price) = 62%**, range **$48–$82**, mean **$63** vs price **$55**. The probability statement is the decision-useful headline; the range bounds it; the skew (mean > median) flags upside optionality.

---

### Q19. Reverse DCF on the explicit-period CAGR (not terminal g).

**Given:** Stock at $40, shares 150m → equity $6,000m; net debt $500m → EV $6,500m. Terminal value is fixed at 8× a Year-5 EBITDA that depends on revenue. The model says: at 6% revenue CAGR, EV = $6,000m; at 8% CAGR, EV = $6,900m (roughly linear between). What revenue CAGR does the $6,500m market EV imply?

**Solution.** Interpolate linearly between the two model points:
```
Between 6% CAGR (EV 6,000) and 8% CAGR (EV 6,900): slope = (6,900−6,000)/(8%−6%) = 900 per 2 points = 450 per point.
Needed EV above the 6% point: 6,500 − 6,000 = 500.
Extra CAGR = 500 / 450 = 1.11 points.
Implied CAGR = 6% + 1.11% ≈ 7.1%.
```
**Answer: the price implies ~7.1% revenue CAGR** over the explicit period. Now judge it: if the industry is growing 4% and the company has been compounding at 6%, a 7.1% required CAGR is a stretch — mild overvaluation. Reverse DCF works on *any* single driver, not just terminal g; here we decoded the near-term growth the price demands.

---

### Q20. Football field — placing an M&A offer.

**Given:** Standalone method ranges (per share): DCF $46–$58; trading comps $42–$54; precedent transactions $55–$70; 52-week range $40–$56. An acquirer offers $62. Interpret.

**Solution.** Rank the tops: precedents ($70) highest — control premium; DCF and comps middle; 52-week the market's own recent range. Overlap zone (where DCF, comps, 52-week intersect) is roughly **$46–$54** — the standalone consensus value. The $62 offer sits **above every standalone method except the upper half of precedent transactions**.

**Answer.** The $62 offer implies a premium of roughly 15–35% over the standalone consensus (~$46–$54), and it falls inside the *precedent-transaction* range — consistent with a control premium a buyer would pay. For the target's board, an offer above standalone ranges and within the precedent range is defensible as fair-to-attractive; the fairness opinion would lean on precedents to justify it.

---

### Q21. Convexity check — why the up-move beats the down-move.

**Given:** Base perpetuity value uses FCFF₆ = $100m, WACC = 9%, g = 3%. Compute value at g = 3%, then at g = 2% and g = 4% (WACC fixed). Show the asymmetry.

**Solution.**
```
g=3%: TV = 100/(0.09−0.03) = 100/0.06 = 1,666.7
g=2%: TV = 100/(0.09−0.02) = 100/0.07 = 1,428.6   → change −238.1 (−14.3%)
g=4%: TV = 100/(0.09−0.04) = 100/0.05 = 2,000.0   → change +333.3 (+20.0%)
```
Wait — here FCFF₆ was held fixed at 100 for all three to isolate the denominator effect. (In a full model FCFF₆ = FCFF₅×(1+g) also rises with g, amplifying the up-move further.)

**Answer.** A symmetric ±1-point move in g produces an **asymmetric** value response: −14.3% down vs. +20.0% up. The `1/(WACC−g)` function is **convex** — as g rises toward WACC the denominator shrinks and value accelerates. Practical consequence: the upper-right corner of a WACC/g table always stretches further than the lower-left contracts, so a naive "±X%" symmetric range understates the upside tail.

---

### Q22. Full end-to-end: scenario table + reverse-DCF gut check.

**Given:** Company at $30/share, 200m shares → equity $6,000m, net debt $1,500m → EV $7,500m. You build Bear/Base/Bull equity values of $4,400m, $6,600m, $8,800m (probabilities 30/45/25). Also, at the base case the model's terminal g that reconciles to your $6,600m base equity is 2.5%. (a) Probability-weighted per share? (b) Is the $30 price cheap or dear vs. your work?

**Solution.**
(a)
```
E[equity] = 0.30×4,400 + 0.45×6,600 + 0.25×8,800
          = 1,320 + 2,970 + 2,200 = 6,490
E[per share] = 6,490 / 200 = $32.45
Per-share cases: Bear 4,400/200=$22.00; Base 6,600/200=$33.00; Bull 8,800/200=$44.00.
```
(b) Market equity is $6,000m vs. your base $6,600m and probability-weighted $6,490m. The price sits **below both** your base ($33.00) and expected ($32.45) per-share values — the stock looks **~8–10% cheap** on your central estimates, and it's below the *bear-to-base* midpoint too. Reverse-DCF cross-check: since your base ($6,600m equity, $8,100m EV) reconciles at 2.5% terminal g, the market's lower $7,500m EV must imply a *sub-2.5%* terminal g — i.e., the market is pricing slightly more conservative perpetual growth than your base. Verdict: **modestly undervalued**, contingent on the base case's 2.5% terminal growth being achievable; the 30% bear weight ($22 floor, −27%) is the risk to size against.

**Answer.** (a) **$32.45** probability-weighted. (b) At $30 the stock is ~8% below the probability-weighted value and implies a terminal g below your 2.5% base — a modest long, with the bear case to $22 as the bounded downside.
