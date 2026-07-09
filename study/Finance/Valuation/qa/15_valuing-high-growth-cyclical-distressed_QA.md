# Q&A — Valuing High-Growth, Cyclical & Distressed Firms

A mix of theory (with interview-ready phrasing) and fully solved numerical problems. Numbers are self-checked and reconcile across parts.

---

## Theory

### Q1. Why do earnings multiples break down for high-growth loss-makers, and what do you use instead?

**Answer.** A P/E needs a positive, representative "E." A cash-burning growth firm has negative GAAP earnings, so P/E is undefined or meaningless; EV/EBITDA fails too when EBITDA is negative. More deeply, even where earnings are positive-but-small, they're *distorted* by growth investment — S&M and R&D spent to capture the market depress today's profit far below the firm's steady-state earning power. So you move *up* the income statement to a line that's still positive and less distorted: **EV/Revenue**, or **EV/Gross Profit** where gross margins differ across peers. Crucially it must be **enterprise value** in the numerator, because revenue is a pre-financing flow available to all capital providers.

**How to say it:** "No earnings means no P/E, so I go up the income statement to revenue or gross profit and use an EV-based multiple benchmarked to peers with a similar growth-and-margin profile — but the multiple is just shorthand for a DCF that models the path to profitability."

---

### Q2. What is "path to profitability" and which two assumptions dominate the valuation?

**Answer.** It's the modeled bridge from today's loss to a mature profit: revenue growth fading over 7–10 years toward GDP-plus, while operating expenses (especially S&M) fall as a percent of revenue because an installed base generates revenue without proportional new spend. The gap between gross margin and normalized opex percent is the **target operating margin**. Because value in a growth DCF sits overwhelmingly in the terminal year, the two dominant assumptions are **(1) the terminal operating margin** and **(2) the terminal revenue level** (a function of the growth path). Sensitize both relentlessly.

---

### Q3. How do unit economics tell you whether losses are "good" or "bad"?

**Answer.** Losses are rational investment if each customer generates more discounted gross profit than it costs to acquire. The test is **LTV/CAC** — lifetime value over customer acquisition cost — with a target of ≥ 3x, plus a **CAC payback** under ~18 months and **net revenue retention** above 100%. If LTV/CAC > 1, growth spend creates value and the losses are financing future profit; if < 1, growth *destroys* value and you assign little to the growth story. Caveat: the simple LTV = gross profit ÷ churn formula assumes a zero discount rate and overstates value — discount the gross-profit annuity for rigor.

---

### Q4. Why do cyclicals look cheapest at the top of the cycle?

**Answer.** P/E = price ÷ earnings. At the peak, earnings are at their maximum, so the ratio is at its *minimum* — the stock looks cheap right before earnings roll over. At the trough, depressed earnings inflate P/E, making it look expensive precisely when it may be cheapest on normalized numbers. The market's price reflects *average* through-cycle earning power, but the reported "E" is a single distorted point. **The fix is normalization:** replace the one-year "E" with mid-cycle earnings and apply a normal multiple.

**How to say it:** "A low P/E on a cyclical is usually a peak signal, not a bargain — I normalize before judging."

---

### Q5. Walk through how you normalize a cyclical's earnings.

**Answer.** (1) Identify the cycle length and use an averaging window spanning at least one full cycle including a downturn. (2) Choose the variable to normalize — usually margin (more stable than absolute earnings), or a through-cycle commodity price for producers. (3) Apply the normalized margin/price to *current* revenue/volume/capital to get **normalized earnings**. (4) Apply a **mid-cycle multiple** — never a peak multiple to normalized earnings, that double counts. (5) Sanity-check implied normalized ROIC against cost of capital and history, and cross-check with EV/replacement cost (Tobin's Q < 1 supports a bottom).

---

### Q6. Explain why equity in an insolvent firm can still be worth something.

**Answer.** Equity holders have limited liability: downside capped at zero, upside unlimited. They receive `max(V − F, 0)` where V is asset value and F is the face of debt — the exact payoff of a **call option** struck at F, written on the firm's assets (Merton 1974). Even if V < F today, if assets are volatile and debt matures in the future, there's real probability V climbs above F before maturity — the option's **time value**. So insolvent ≠ worthless. It also explains why equity holders favor volatility near default (asset substitution / risk-shifting): higher σ raises the call value they hold and lowers the debt value creditors hold.

---

### Q7. What is the fulcrum security and why does a distressed investor care?

**Answer.** When you waterfall a restructured enterprise value down the capital structure by strict seniority (absolute priority rule), the **fulcrum** is the most senior claim *not* paid in full — where the money runs out. Claims above it are "money-good" (fully recovered, low return); claims below are typically zeroed. The fulcrum usually **converts into the post-reorganization equity**, so it captures the recovery upside. Distressed investors aim to identify and own the fulcrum: it's the pivot between debt-like safety and equity-like upside.

---

### Q8. Why not just DCF a distressed company at a high discount rate?

**Answer.** Because you'd risk double-counting default risk — once in a punitive discount rate and again if your cash flows already reflect distress. The cleaner approach is **scenario / probability-weighted** cash flows (survive-and-recover, restructure, liquidate) discounted at a more normal rate, so risk shows up in the *probabilities*, not twice. You also can't ignore the **capital structure**: enterprise value is meaningless to a specific security until you waterfall it, and equity should be modeled as an option, not a discounted dividend stream. Watch **debt overhang** too — high leverage can distort the cash flows themselves via underinvestment.

---

### Q9. Why is probability-weighting the correct approach for binary outcomes, and what's a "real option"?

**Answer.** A DCF discounts *expected* cash flows. When outcomes are binary or highly skewed — drug approval, litigation, restructuring — a single "base case" is just one branch, not the expected value. The mathematically correct value is **Σ p·V**: weight the *valuations* of each scenario, not the inputs, to respect non-linearity. A **real option** is managerial flexibility — to abandon, expand, delay, or switch — that a static DCF ignores, thereby *understating* value. Optionality is worth **more** when uncertainty is **higher**, which is why volatile pipelines, undeveloped reserves, and staged investments carry option value beyond their expected DCF.

---

### Q10. How do you bridge enterprise value to equity value per share — and how does it differ in distress?

**Answer.** Going concern: **Equity = EV − net debt − preferred − minority interest**, where net debt = total debt − cash. Divide by **fully diluted** shares (treasury method for in-the-money options/RSUs — material for growth firms). In **distress**, you do *not* net debt at par, because it won't be repaid in full: you waterfall EV through the claims by seniority, and equity is the residual (often zero on a going-concern basis, but with option time value). The bridge is replaced by the recovery waterfall.

---

## Numerical problems

### Q11. Revenue multiple and equity bridge

A pre-profit software firm has revenue of $250m growing 45%, net cash of $180m, and 60m fully diluted shares. Comparable firms with similar growth trade at EV/Revenue of 7x.

**Solve.**
- EV = 7 × $250m = **$1,750m**.
- Equity value = EV + net cash = 1,750 + 180 = **$1,930m**.
- Per share = 1,930 / 60 = **$32.17**.

**Check.** Implied P/S on equity value = 1,930 / 250 = 7.72x > EV/Sales 7x, as it should be for a net-cash company (equity worth more than EV). Consistent.

---

### Q12. Unit economics — simple vs discounted LTV

ARPU = $5,000/yr, gross margin = 75%, annual churn = 10%, CAC = $9,000, discount rate = 12%.

**Solve.**
- Gross profit per customer/yr = 5,000 × 0.75 = **$3,750**.
- Simple LTV = 3,750 / 0.10 = **$37,500**; simple LTV/CAC = 37,500 / 9,000 = **4.17x**.
- r_retain = 1 − 0.10 = 0.90. Discounted LTV = 3,750 × [0.90 / (1 + 0.12 − 0.90)] = 3,750 × (0.90 / 0.22) = 3,750 × 4.09 = **$15,341**.
- Discounted LTV/CAC = 15,341 / 9,000 = **1.70x**.
- CAC payback = 9,000 / (3,750/12) = 9,000 / 312.5 = **28.8 months**.

**Verdict.** Value-creating on both measures (>1x), but the discounted ratio (1.70x) is far below the naive 4.17x, and payback of ~29 months is long — growth is worthwhile but cash-hungry. **Lesson: the simple LTV formula flatters the economics; always discount.**

---

### Q13. Full path-to-profitability margin bridge

A firm has $300m revenue, 76% gross margin, S&M 50%, R&D 22%, G&A 14% of revenue today. Project Year 5 with S&M → 28%, R&D → 18%, G&A → 10%, gross margin → 80%.

**Solve.**
- Today's operating margin = 76% − (50 + 22 + 14)% = 76% − 86% = **−10%** → −$30m on $300m. Loss-maker confirmed.
- Year 5 operating margin = 80% − (28 + 18 + 10)% = 80% − 56% = **+24%**.
- If revenue compounds to, say, $900m by Year 5, operating profit = 24% × 900 = **$216m**.
- NOPAT at 23% tax = 216 × 0.77 = **$166.3m**.

**Check.** The 34-point margin swing (−10% → +24%) comes almost entirely from opex leverage: S&M+R&D+G&A falls from 86% to 56% of revenue (−30 pts) plus +4 pts of gross margin = +34 pts. Reconciles exactly.

---

### Q14. Cyclical normalization and fair value

A cyclical prints peak revenue $8,000m, peak EBIT margin 22% (EBIT $1,760m). Through-cycle average EBIT margin = 12%. Net debt = $3,000m, 400m shares, share price $30. A fair mid-cycle EV/EBIT is 7x.

**Solve.**
- Market cap = 30 × 400 = $12,000m; EV = 12,000 + 3,000 = **$15,000m**.
- Headline EV/EBIT = 15,000 / 1,760 = **8.5x** (looks cheap).
- Normalized EBIT = 12% × 8,000 = **$960m**.
- Normalized EV/EBIT = 15,000 / 960 = **15.6x** (actually expensive).
- Fair EV = 7 × 960 = **$6,720m**; fair equity = 6,720 − 3,000 = **$3,720m**; fair per share = 3,720 / 400 = **$9.30**.

**Verdict.** At $30 vs normalized fair value ~$9.30, the stock discounts peak margins as permanent — a **cyclical value trap**. The 8.5x headline is an artifact of peak EBIT.

**Check.** If margins revert to 12%, EBIT falls 45% (1,760 → 960) *and* the multiple compresses toward mid-cycle — the classic double hit. Internally consistent.

---

### Q15. Recovery waterfall and fulcrum

Debt (face): secured $250m, senior unsecured $350m, subordinated $150m. Restructured going-concern EV = $500m (EBITDA $100m × 5x). Liquidation value = $380m.

**Solve — going concern ($500m):**

| Claim | Face | Paid | Recovery |
|---|---|---|---|
| Secured | $250m | $250m | 100% |
| Senior unsecured | $350m | $250m | 71.4% |
| Subordinated | $150m | $0 | 0% |
| Equity | — | $0 | 0% |

Fulcrum = **senior unsecured** (money runs out at $500m; it gets remaining $250m / $350m = 71.4%).

**Liquidation ($380m):** secured $250m (100%), senior unsecured $130m (37.1%), sub/equity 0%.

**Blended senior-unsecured recovery** at 55% reorg / 45% liquidation:
= 0.55 × 71.4% + 0.45 × 37.1% = 39.3% + 16.7% = **56.0%**.

**Check.** In both scenarios secured is fully covered and the fulcrum is the senior unsecured — consistent. If the senior notes trade below 56 cents, the fulcrum offers positive expected recovery *plus* equity conversion upside.

---

### Q16. Equity as a call option (Merton)

Asset value V = $500m, total debt face F = $700m, σ_V = 55%, r = 4%, T = 2 years. Shares = 80m.

**Solve.**
```
ln(V/F) = ln(500/700) = ln(0.7143) = −0.3365
(r + σ²/2)T = (0.04 + 0.55²/2)(2) = (0.04 + 0.15125)(2) = 0.3825
d1 = (−0.3365 + 0.3825) / (0.55·√2) = 0.0460 / 0.7778 = 0.0591
d2 = 0.0591 − 0.7778 = −0.7187
N(d1) ≈ 0.5236 ,  N(d2) ≈ 0.2362
E = 500(0.5236) − 700·e^(−0.04·2)(0.2362)
  = 261.8 − 700(0.9231)(0.2362)
  = 261.8 − 152.6 = $109.2m
```
- Equity per share = 109.2 / 80 = **$1.37**.
- Risk-neutral default probability = N(−d2) = N(0.7187) ≈ **76.4%**.

**Interpretation.** The firm is underwater (V $500m < F $700m) yet equity is worth ~$109m of pure time value; a 23.6% survival-to-recovery chance keeps it alive. Debt value = V − E = 500 − 109 = **$391m** (≈ 56 cents on $700m face) — consistent with a deeply distressed bond.

**Check.** E + D = 109 + 391 = $500m = V. The claims sum to asset value exactly. Reconciles.

---

### Q17. Probability-weighted (scenario) valuation of a growth name

A firm is worth $180/share if it captures its TAM (bull), $60 base case, $15 if competition compresses margins (bear). Probabilities: bull 25%, base 50%, bear 25%.

**Solve.**
- E[value] = 0.25×180 + 0.50×60 + 0.25×15 = 45 + 30 + 3.75 = **$78.75/share**.

**Check.** Probabilities sum to 1.00. Note E[value] $78.75 exceeds the base case $60 because the bull upside ($180) is far larger than the bear downside relative to base — the skew pulls expected value above the median scenario. Correctly captured only by weighting *valuations*, not averaging assumptions.

---

### Q18. Binary event — biotech

A biotech is worth $90/share if its Phase 3 drug is approved and $12/share (net cash minus burn) if it fails. Probability of approval = 65%.

**Solve.**
- E[value] = 0.65×90 + 0.35×12 = 58.5 + 4.2 = **$62.70/share**.

**Interpretation.** A single point estimate is meaningless here — the stock is neither $90 nor $12; it's the probability-weighted $62.70, and it will gap violently to one pole on the readout. If the market prices it at $45, it's implying a lower success probability: solve 45 = p×90 + (1−p)×12 → 45 = 78p + 12 → p = 33/78 = **42.3%** implied.

**Check.** Plug p = 0.423: 0.423×90 + 0.577×12 = 38.1 + 6.9 = $45.0. Reconciles.

---

### Q19. Peak vs normalized — quick multiple flip

A miner reports EPS of $8 at the peak; you estimate mid-cycle EPS at $3. The stock is $48.

**Solve.**
- Headline P/E = 48 / 8 = **6.0x** (screams cheap).
- Normalized P/E = 48 / 3 = **16.0x** (average-to-rich for a cyclical).

**Verdict.** The 6x is a peak illusion. On normalized $3 EPS and a fair mid-cycle 8x, fair value = 8 × 3 = **$24** — half the current price. **Don't buy the low P/E at the peak.**

---

### Q20. Cash runway for a loss-maker

A firm burns $12m/month (FCF), holds $216m cash, and burn will shrink 5% per month as it scales. Roughly how long is the runway ignoring the reduction, and does the taper matter?

**Solve.**
- Flat-burn runway = 216 / 12 = **18 months**.
- With a 5%/month declining burn, cumulative burn is a geometric series; months to exhaust $216m: the series 12(1 + 0.95 + 0.95² + …) sums to 12/0.05 = $240m at infinity, which *exceeds* $216m, so the firm nearly — but let's check: cumulative after n months = 12 × (1 − 0.95ⁿ)/0.05 = 240(1 − 0.95ⁿ). Set = 216 → 1 − 0.95ⁿ = 0.90 → 0.95ⁿ = 0.10 → n = ln0.10/ln0.95 = −2.3026 / −0.0513 = **≈ 44.9 months**.

**Verdict.** The taper is *enormous*: runway extends from ~18 months (flat) to ~45 months. **Lesson: for loss-makers, the *trajectory* of burn matters as much as the level — always model the ramp, not a static burn rate.**

**Check.** Total lifetime burn ceiling = 12/0.05 = $240m > $216m cash, so the firm *does* run out (barely) — consistent with a finite 45-month runway rather than infinite survival.

---

### Q21. Rule of 40 screen

Three SaaS firms: A grows 60% with −25% FCF margin; B grows 30% with +12% margin; C grows 15% with +18% margin.

**Solve.**
- A: 60 + (−25) = **35** → fails 40.
- B: 30 + 12 = **42** → passes.
- C: 15 + 18 = **33** → fails.

**Interpretation.** B best balances growth and profitability. A's hyper-growth doesn't yet pay for its burn; C is profitable but growth is too slow to justify a premium multiple. The Rule of 40 is a quick screen, not a valuation — but it flags which growth/margin trade-offs the market rewards.

---

### Q22. Distressed enterprise-to-equity, two lenses reconciled

Using Q15's firm (going-concern EV $500m, debt face $750m total), and separately an option model giving equity time value of $40m: is there double counting if you report both "equity recovers $0 in restructuring" and "equity worth $40m"?

**Answer.** No. The **$0** is the recovery *if the restructuring crystallizes today* — on a $500m EV against $750m of debt, subordinated and equity are wiped. The **$40m** is the market's price for the *chance* the firm trades out of distress before its maturity wall, i.e. the option's time value on volatile assets. They describe different states of the world (immediate reorg vs. survive-and-recover), so both can be true simultaneously. The $40m is *not* additional enterprise value layered on top of the $500m — it's a claim-splitting/optionality effect. Reporting both is correct and, in fact, explains why distressed equity routinely trades at a small positive price.

**Check.** If you (wrongly) added $40m of equity *on top of* the $500m EV and *also* paid creditors their waterfall from $500m, you'd have distributed $540m of value from a $500m pie — that would be the double count. The option value instead redistributes claims *within* the $500m-plus-volatility framework; it does not inflate EV. Consistent.

---

*End of Q&A.*
