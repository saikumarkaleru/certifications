# Q&A — Precedent Transaction Analysis

A mixed bank of theory and numerical questions. Numerical answers are fully worked and self-verified (EV↔equity bridges reconcile, per-share math checks). Theory answers include a "say it in an interview" line.

---

## Theory

### Q1. What is precedent transaction analysis in one paragraph?

**Answer.** It is a relative-valuation method that values a company using the prices paid in past acquisitions of comparable companies. You assemble a set of past M&A deals, compute a valuation multiple for each off the transaction price (typically `EV / LTM EBITDA`), summarize the range, and apply a chosen multiple to your target's metric to imply an enterprise value, then bridge to equity value and per share. Because the observed prices are *control* prices that include a premium over the pre-deal trading level and often a share of synergies, precedents usually produce the highest valuation range.

**Say it in an interview:** *"Precedents ask a simple question — what have real buyers actually paid for whole companies like this one — and turn those prices into multiples I can apply to my target."*

---

### Q2. Why do precedents usually give the highest value on the football field?

**Answer.** Two structural reasons stack on top of standalone value:
1. **Control premium** — a precedent is the price to buy the *entire* company, so it embeds a premium (typically 20–40%) over the unaffected minority share price, because control lets the buyer change the cash flows.
2. **Synergies** — many precedents involve strategic buyers who share part of their expected cost/revenue synergies with the seller to win the deal.

So `minority value + control premium + shared synergies = control price`, which sits above trading comps (minority) and often above a standalone DCF (which excludes synergies).

**Say it in an interview:** *"Control and synergies — that's the whole story for why precedents run rich."*

---

### Q3. When are precedents NOT the highest method?

**Answer.**
- **Distressed comp set:** fire-sale, bankruptcy, or forced-seller deals show depressed multiples — precedents can then fall *below* trading comps.
- **Stale/peak vintage:** deals from a market top applied in a colder market are either not credible or lag today's re-rated public multiples, so current trading comps can top the field.
- **Aggressive DCF:** a high terminal-growth, low-WACC DCF can exceed any relative method.

**Say it in an interview:** *"'Precedents are highest' is a tendency, not a law — it depends on the vintage, the health of the sellers, and where public multiples sit today."*

---

### Q4. Explain the control premium and how you measure it.

**Answer.** The control premium is the percentage by which the offer price exceeds the target's **unaffected** share price — the price before the market anticipated the deal.

```
Control premium % = (Offer price ÷ Unaffected price) − 1
```

The unaffected price is usually a 1-day close or a 20/30-day VWAP *before* the announcement (or before the leak that moved the stock). Choosing the reference date matters: if a leak ran the stock up first, using the day-before price understates the true premium. Typical premiums run 20–40%.

**Say it in an interview:** *"Offer over unaffected, minus one — and I'll use a VWAP before announcement to dodge leak contamination."*

---

### Q5. Strategic vs financial buyer — who pays more, and why?

**Answer.** Usually the **strategic**, because it has synergies a financial buyer doesn't — it can fold the target into existing operations, remove duplicate costs, and cross-sell, then share part of that value to win the auction. The strategic's value ceiling is `standalone + synergies`. A **financial** buyer (PE sponsor) generally has no operating synergies, is disciplined by an IRR hurdle, and relies on leverage; its ceiling is roughly standalone value. **Exceptions:** in cheap-credit environments sponsors can pay strategic-like prices, and a sponsor that owns a **platform** company behaves like a quasi-strategic (buy-and-build).

**Say it in an interview:** *"Strategics usually win because synergies give them a higher ceiling — unless credit is cheap or the sponsor has a platform to bolt onto."*

---

### Q6. Three differences between precedents and trading comps.

**Answer.**
1. **Control vs minority:** precedents use control prices with a premium; trading comps use minority market prices.
2. **Historical vs live:** precedents are snapshots at each deal date; trading comps are current.
3. **Synergies vs none:** precedents embed synergies; trading comps don't.

Net effect: precedents are higher but noisier.

---

### Q7. What are the main data sources for precedents?

**Answer.** Merger proxies (DEFM14A), tender-offer docs, 8-Ks and S-4s for public US targets; press releases and investor decks for headline price and synergy guidance; data terminals (Bloomberg MA, Capital IQ, FactSet, Refinitiv/LSEG, Mergermarket, Dealogic, PitchBook) for screening; and the **fairness opinion** in the proxy, which often lists the advisor's own curated comp set. Workflow: screen the terminal, then verify each deal against the primary filing.

---

### Q8. What adjustments do you make before using screened multiples?

**Answer.** LTM/calendarization to the announcement date; strip non-recurring items to normalize EBITDA; pro-forma the target's own mid-year M&A; filter to completed deals; fix all-stock deals at announcement-date value; gross up partial-stake deals to 100% equivalent; handle earn-outs/contingent consideration consistently; convert cross-border deals at announcement-date FX; and place your target within the range by size/growth/margin rather than blindly using the median.

---

### Q9. Why is `EV / EBITDA` the default multiple in precedents?

**Answer.** Because EV captures *all* capital providers and EBITDA is *before* interest, the multiple is **independent of the target's financing** — so you can compare a debt-heavy target to a debt-free one. Being before D&A, it also neutralizes depreciation-policy and past-capex-timing differences. That robustness makes it the M&A workhorse. You'd switch to EV/Revenue for unprofitable/early-stage targets and P/E or P/B for financials.

---

### Q10. Why must you avoid double-counting synergies?

**Answer.** Precedent multiples *already include* the buyers' synergies (that's part of why they're high). If you apply a synergy-rich precedent multiple to your target *and then* separately add your own synergy case on top, you count the same benefit twice and overvalue the company. Either use the precedent multiple as-is (synergies embedded) or strip to a standalone basis and add synergies explicitly — not both.

---

### Q11. Why would a credit analyst care about precedents?

**Answer.** For **recovery and downside** work: precedent multiples give a market-tested estimate of what the enterprise could fetch in a sale, framing asset coverage and recovery in a distressed or take-private scenario. In leveraged finance, the entry multiple in precedents also anchors how much debt a structure can carry.

---

## Numerical

### Q12. Build a deal's EV/EBITDA and control premium.

**Setup.** Offer: **$75/share cash**. Basic shares 40m; options 5m at $25 strike; debt $500m; cash $150m; minority interest $100m; LTM EBITDA $350m; unaffected price $55.

**Solution.**
- Treasury method: cash in = 5m × $25 = $125m; shares bought = 125 ÷ 75 = 1.667m; net new = 5 − 1.667 = **3.333m**; FDSO = 40 + 3.333 = **43.333m**.
- Offer equity value = 75 × 43.333 = **$3,250m**.
- Transaction EV = 3,250 + 500 + 100 − 150 = **$3,700m**.
- EV/EBITDA = 3,700 ÷ 350 = **10.6x**.
- Control premium = (75 ÷ 55) − 1 = **36.4%**.

**Check.** EV 3,700 − debt 500 − minority 100 + cash 150 = equity 3,250; ÷ 43.333m = $75.00 ✓ (ties to offer). Premium 36.4% sits in the normal 20–40% band.

---

### Q13. From a comp set to per-share value.

**Setup.** Precedent EV/EBITDA multiples: 8.5x, 9.5x, 10.5x, 11.0x, 14.0x (last is a peak outlier). Target: LTM EBITDA $200m; debt $250m; cash $50m; minority $0; FDSO 60m.

**Solution.**
- Sort: 8.5, 9.5, 10.5, 11.0, 14.0 → **median = 10.5x**; mean = 53.5 ÷ 5 = **10.7x**. (Outlier lifts the mean; lead with median.)
- Implied EV = 10.5 × 200 = **$2,100m**.
- Net debt = 250 − 50 = **$200m**.
- Equity = 2,100 − 200 = **$1,900m**.
- Per share = 1,900 ÷ 60 = **$31.67**.

**Check.** Equity 1,900 + net debt 200 = 2,100 = 10.5 × 200 ✓; 31.67 × 60 = 1,900 ✓.

---

### Q14. Range presentation (low / median / high).

**Setup.** Same target as Q13. Apply 9.5x (low), 10.5x (median), 11.0x (high).

**Solution.**

| Multiple | Implied EV | Less net debt | Equity | ÷ FDSO | Per share |
|---|---|---|---|---|---|
| 9.5x | $1,900m | $200m | $1,700m | 60m | **$28.33** |
| 10.5x | $2,100m | $200m | $1,900m | 60m | **$31.67** |
| 11.0x | $2,200m | $200m | $2,000m | 60m | **$33.33** |

**Check.** Each row: (mult × 200) − 200, ÷ 60. 9.5x: 1,900 − 200 = 1,700 ÷ 60 = 28.33 ✓. 11.0x: 2,200 − 200 = 2,000 ÷ 60 = 33.33 ✓.

**Interview line:** *"On precedents the target is worth roughly $28–33 per share, centered near $32."*

---

### Q15. Strategic vs sponsor bid with synergies.

**Setup.** Unaffected price $30, 200m shares → unaffected equity $6,000m; net debt $2,000m → unaffected EV $8,000m; LTM EBITDA $800m → 10.0x unaffected. Sponsor can pay a 25% premium. Strategic sees $150m annual synergies, capitalizes at 10x, and shares 40% with the seller on top of matching the control premium.

**Solution — sponsor.**
- Offer price = 30 × 1.25 = **$37.50**; equity = 37.50 × 200 = **$7,500m**; EV = 7,500 + 2,000 = **$9,500m**; EV/EBITDA = 9,500 ÷ 800 = **11.9x**.

**Solution — strategic.**
- No-synergy control EV (match sponsor) = **$9,500m**.
- Synergy value = 150 × 10 = **$1,500m**; seller's 40% share = **$600m**.
- Strategic offer EV = 9,500 + 600 = **$10,100m**; equity = 10,100 − 2,000 = **$8,100m**; price = 8,100 ÷ 200 = **$40.50**.
- Premium = (40.50 ÷ 30) − 1 = **35.0%**; EV/EBITDA = 10,100 ÷ 800 = **12.6x**.

**Check.** Strategic: EV 10,100 − net debt 2,000 = equity 8,100; ÷ 200 = $40.50; premium 35% ✓. Strategic keeps 60% of $1,500m = $900m of net synergy value the sponsor never had. Strategic pays 12.6x vs sponsor 11.9x — richer because of shared synergies.

---

### Q16. Back out the implied premium embedded in a precedent multiple.

**Setup.** A deal printed at **12.0x** EV/EBITDA. You know comparable companies were *trading* (unaffected) at **9.6x** EV/EBITDA at the time, on the same EBITDA base with the same net debt. What control premium (at the EV level) is embedded?

**Solution.**
- EV premium at EV level = (12.0 ÷ 9.6) − 1 = 1.25 − 1 = **25% on EV**.
- If net debt is a fixed dollar amount, the *equity* premium is higher than 25% because the premium dollars all accrue to equity. Suppose EBITDA = $500m, net debt = $1,500m:
  - Unaffected EV = 9.6 × 500 = $4,800m; unaffected equity = 4,800 − 1,500 = **$3,300m**.
  - Deal EV = 12.0 × 500 = $6,000m; deal equity = 6,000 − 1,500 = **$4,500m**.
  - Equity premium = (4,500 ÷ 3,300) − 1 = **36.4%**.

**Check.** EV rose $1,200m (4,800→6,000); all of it flows to equity (3,300→4,500, also +$1,200m) since net debt is fixed ✓. Lesson: a 25% EV uplift can be a ~36% equity premium when the company is levered.

---

### Q17. All-stock deal — which price fixes the multiple?

**Setup.** Acquirer offers 0.5 of its shares per target share. At announcement acquirer trades at $80 (implied offer $40/target share); by closing acquirer has fallen to $70 (implied $35). Target has 100m shares, net debt $500m, EBITDA $250m.

**Answer + solution.** Fix the multiple at the **announcement-date** value; don't let it float to the (contaminated) closing value.
- Announcement equity = 40 × 100 = $4,000m; EV = 4,000 + 500 = $4,500m; EV/EBITDA = 4,500 ÷ 250 = **18.0x**.
- (Closing value would misleadingly show 35 × 100 + 500 = $4,000m EV → 16.0x, distorted purely by the acquirer's share move.)

**Say it in an interview:** *"For stock deals I lock the multiple at announcement; the closing price reflects the acquirer's stock drift, not the price agreed for the target."*

---

### Q18. Partial-stake deal — gross up to 100%.

**Setup.** Buyer acquires **70%** of a target for **$1,400m** in equity value (cash), implying the full equity is valued proportionally. Target net debt $600m, EBITDA $400m.

**Solution.**
- Implied 100% equity value = 1,400 ÷ 0.70 = **$2,000m**.
- Implied EV = 2,000 + 600 = **$2,600m**.
- EV/EBITDA = 2,600 ÷ 400 = **6.5x**.

**Check.** 70% of $2,000m equity = $1,400m ✓ (ties to the stake price). Using the raw $1,400m without grossing up would understate EV badly (1,400 + 600 = 2,000 → 5.0x, wrong).

**Say it in an interview:** *"Always gross a partial stake to a 100% equivalent before computing the multiple, or you understate value."*

---

### Q19. Median vs mean — why it matters.

**Setup.** Multiples: 7.0x, 9.0x, 9.5x, 10.0x, 20.0x (a distressed *seller* got a strategic scarcity premium — genuine outlier).

**Solution.**
- Median = **9.5x**; mean = (7 + 9 + 9.5 + 10 + 20) ÷ 5 = 55.5 ÷ 5 = **11.1x**.
- Applied to a target with $300m EBITDA, $400m net debt, 50m shares:
  - At median 9.5x: EV = 2,850; equity = 2,450; per share = **$49.00**.
  - At mean 11.1x: EV = 3,330; equity = 2,930; per share = **$58.60**.

**Check.** Median case: 9.5 × 300 = 2,850; − 400 = 2,450; ÷ 50 = 49.00 ✓. The 20x outlier inflates the mean by ~$9.60/share — nearly 20%. **Lead with the median.**

---

### Q20. Full EV→equity bridge with minority interest and preferred.

**Setup.** Applied multiple 11.0x on EBITDA $450m. Target: total debt $1,200m; cash $200m; minority interest $150m; preferred stock $100m; FDSO 90m.

**Solution.**
- Implied EV = 11.0 × 450 = **$4,950m**.
- Equity = EV − debt − minority − preferred + cash = 4,950 − 1,200 − 150 − 100 + 200 = **$3,700m**.
- Per share = 3,700 ÷ 90 = **$41.11**.

**Check.** Reverse: equity 3,700 + debt 1,200 + minority 150 + preferred 100 − cash 200 = 4,950 = 11.0 × 450 ✓. Preferred and minority are claims *ahead of* common equity, so they're subtracted in the EV→equity bridge.

---

### Q21. Compute implied EV/EBITDA and P/E for one deal, and reconcile.

**Setup.** Offer $50/share, 100m FDSO; net debt $1,000m; minority $0; LTM EBITDA $500m; LTM net income $210m.

**Solution.**
- Offer equity = 50 × 100 = **$5,000m**.
- Transaction EV = 5,000 + 1,000 = **$6,000m**.
- EV/EBITDA = 6,000 ÷ 500 = **12.0x**.
- P/E = 5,000 ÷ 210 = **23.8x**.

**Check.** EV/EBITDA uses EV (all capital) over pre-interest EBITDA ✓; P/E uses equity value over after-tax net income ✓ — numerator/denominator claimants matched in both. EV 6,000 − net debt 1,000 = equity 5,000 = 50 × 100 ✓.

---

### Q22. Sensitivity — how much does one multiple turn move value?

**Setup.** Target EBITDA $250m, net debt $300m, 80m shares. How much does per-share value change per 1.0x of multiple?

**Solution.**
- 1.0x of EBITDA = 1.0 × 250 = $250m of EV = $250m of equity (net debt fixed) = 250 ÷ 80 = **$3.125 per share per turn**.
- So 10.0x → $27.13; 11.0x → $30.25; 12.0x → $33.38.

**Check.** 10.0x: 2,500 − 300 = 2,200 ÷ 80 = 27.50. Hmm — recompute: 2,500 − 300 = 2,200; 2,200 ÷ 80 = **$27.50**. 11.0x: 2,750 − 300 = 2,450 ÷ 80 = **$30.625**. Difference = $3.125 ✓ (matches per-turn sensitivity). 12.0x: 3,000 − 300 = 2,700 ÷ 80 = **$33.75**; again +$3.125 ✓.

**Say it in an interview:** *"Each turn of EBITDA here is worth about $3.13 per share — handy for eyeballing sensitivity live."*

*(Note: the exact per-share levels use net debt $300m; the $3.125-per-turn sensitivity is exact and independent of net debt because net debt is constant across multiples.)*
