# Q&A — Valuation Overview: Intrinsic, Relative & Asset-Based

A mixed bank of theory (with interview-ready phrasings) and fully-solved numerical problems. Numbers are self-verified and reconcile. Work each problem before reading the solution.

---

## Theory

### Q1. Name the three families of valuation and give the one-sentence philosophy of each.

**Answer.**
- **Intrinsic (DCF):** a business is worth the present value of the cash it will generate over its life, discounted for time and risk.
- **Relative (multiples):** similar assets should sell for similar prices, so value the company off the market multiples of comparable companies or precedent transactions.
- **Asset-based (NAV/liquidation):** a business is worth the sum of its assets minus its liabilities — a floor set by replacement or break-up value.

*How to say it:* "Intrinsic values it on its own cash flows, relative borrows the market's pricing of similar assets, and asset-based sums the parts. In practice I triangulate at least two."

---

### Q2. Why is EV/EBITDA capital-structure neutral, and P/E is not?

**Answer.** EBITDA is computed **before** interest, and enterprise value already includes **both** debt and equity claims — so both numerator and denominator sit above the financing line. Changing the debt/equity mix leaves EV and EBITDA (roughly) unchanged, so the multiple is comparable across differently-levered firms. P/E uses **net income**, which is **after** interest, and **price** (equity only). More leverage → more interest → lower net income and a different P/E, even for an operationally identical firm. That's why you compare leveraged peers on EV/EBITDA and reserve P/E for equity-holder shorthand and financials.

---

### Q3. Walk through the EV-to-equity bridge and justify each sign.

**Answer.**
```
Enterprise Value
 − Net debt (= total debt − cash)
 − Preferred stock
 − Minority interest
 = Equity Value
 ÷ diluted shares = value per share
```
- **Subtract debt:** lenders have first claim; the buyer inherits repayment.
- **Add back cash** (inside net debt): cash is non-operating; a buyer effectively recovers it, lowering the net cost of the operating business.
- **Subtract preferred:** preferred holders rank ahead of common.
- **Subtract minority interest:** part of consolidated EV belongs to outside (non-controlling) shareholders of subsidiaries, not to the parent's common.

*Reverse direction:* `EV = Equity + total debt + preferred + minority − cash`.

---

### Q4. "Walk me through a DCF." Give the model answer.

**Answer.** Five steps: (1) project unlevered FCFF for 5–10 years — EBIT×(1−t) = NOPAT, + D&A − capex − ΔNWC; (2) estimate WACC — weighted cost of debt and equity, with Ke from CAPM (Rf + β×ERP); (3) compute terminal value via Gordon growth or an exit EBITDA multiple; (4) discount all FCFFs and TV to today at WACC and sum → enterprise value; (5) bridge to equity — subtract net debt, preferred, minority, divide by diluted shares. Then sanity-check implied multiples and the TV share of EV.

---

### Q5. What is the difference between trading comps and transaction comps, and which is usually higher?

**Answer.** Trading comps use multiples of **public peers trading today** — they reflect minority, no-control public-market prices. Transaction comps use multiples **paid in past M&A deals** — they include a **control premium** (typically 20–40%) and often synergies. Transaction comps are therefore usually **higher**. Use trading comps to value a minority stake, transaction comps to value control (an acquisition).

---

### Q6. Explain price vs value and why the distinction matters.

**Answer.** Price is what the market quotes — set by supply, demand, sentiment, and flows; it's observable and never "wrong," but it can diverge from fundamentals. Value is what the asset is worth on its cash flows, growth, and risk — it must be estimated. Active investing is the bet that the two diverge and eventually converge; you buy with a margin of safety when price < your value estimate. If you treat price as value, you can never identify mispricing — the reasoning becomes circular.

---

### Q7. When is asset-based valuation the *primary* method rather than a floor?

**Answer.** When the going-concern premium has collapsed or the value genuinely lives in the assets: (a) **distressed / bankrupt** firms — liquidation value drives creditor recovery; (b) **holding companies and real estate** — value = marked-to-market NAV of the underlying assets; (c) **investment firms / funds** — NAV is the natural metric. For a healthy operating business with strong cash generation, asset value badly understates worth (it ignores intangible earning power), so it's only a floor.

---

### Q8. What is a football field and how do you read it?

**Answer.** A horizontal bar chart with value (per share/equity/EV) on the x-axis; each valuation method contributes a low-to-high bar, and the current market price is overlaid as a vertical line. You read the **overlap** of the bars as the defensible value zone and judge the recommendation from where price sits relative to it — below the zone leans undervalued/buy, above leans overvalued/sell. Transaction comps typically sit highest (control premium); liquidation sits lowest (floor).

---

### Q9. What's the single biggest weakness of a DCF, and how do you mitigate it?

**Answer.** Extreme sensitivity to assumptions, concentrated in the **terminal value**, which is often 60–80% of total EV. Small moves in perpetual growth (g) or WACC swing the output materially — "garbage in, garbage out." Mitigations: run sensitivity tables on g and WACC, cross-check with an exit-multiple TV, validate implied multiples against comps, cap g at long-run nominal GDP, and always present a **range**, never a single point.

---

### Q10. Two operationally identical firms; Firm B has more debt. Compare their EV and equity value.

**Answer.** EV is (to first order) the **same** — it reflects the identical operating business and is capital-structure-neutral. Equity value is **lower** for the levered Firm B, because `Equity = EV − net debt` and its net debt is higher. Second-order effects: leverage can slightly raise EV via the interest tax shield and slightly lower it via distress risk, but the headline answer is same EV, lower equity for the more-levered firm.

---

## Numerical problems

### Q11. Basic EV build. Market cap ₹4,000 cr; total debt ₹1,500 cr; cash ₹500 cr; preferred ₹200 cr; minority interest ₹300 cr. Find enterprise value.

**Solution.**
```
EV = Equity + Debt + Preferred + Minority − Cash
   = 4,000 + 1,500 + 200 + 300 − 500
   = 5,500 cr
```
**EV = ₹5,500 crore.**

---

### Q12. Reverse bridge. A DCF gives EV = ₹9,000 cr. Net debt ₹2,000 cr, preferred ₹500 cr, minority ₹300 cr, diluted shares 40 cr. Find value per share, then reconcile back to EV.

**Solution.**
```
Equity = EV − net debt − preferred − minority
       = 9,000 − 2,000 − 500 − 300 = 6,200 cr
Per share = 6,200 / 40 = ₹155.00
```
**Reconcile (assume cash of, say, 400 inside net debt → total debt = 2,400):**
```
EV = Equity + total debt + preferred + minority − cash
   = 6,200 + 2,400 + 500 + 300 − 400 = 9,000 cr ✓
```
**Value per share = ₹155; bridge closes to ₹9,000 cr.**

---

### Q13. EV/EBITDA valuation. EBITDA ₹1,200 cr; peer median EV/EBITDA 8.5x; net debt ₹3,000 cr; 50 cr shares. Implied equity value per share?

**Solution.**
```
Implied EV     = 8.5 × 1,200 = 10,200 cr
Less net debt  = − 3,000
Equity value   = 7,200 cr
Per share      = 7,200 / 50 = ₹144.00
```
**₹144 per share.**

---

### Q14. P/E cross-check. Same company as Q13: net income ₹600 cr, peer median P/E 12x, 50 cr shares. Compare to the EV/EBITDA answer.

**Solution.**
```
Equity value = 12 × 600 = 7,200 cr
Per share    = 7,200 / 50 = ₹144.00
```
Both methods give **₹144** — the multiples are internally consistent (they imply the same equity value). In reality you'd rarely get an exact match; a tight range is the goal, and here it's a single point, confirming the peer set is coherent.

---

### Q15. Clean 5-year DCF. FCFF₁ = ₹500 cr growing 10%/yr for 5 years; WACC 12%; terminal g 4%; net debt ₹2,000 cr; 30 cr shares. Find value per share.

**Solution.**

**Project & discount FCFF (factor = 1/1.12ᵗ):**

| Yr | FCFF | Factor | PV |
|---|---|---|---|
| 1 | 500.0 | 0.8929 | 446.4 |
| 2 | 550.0 | 0.7972 | 438.5 |
| 3 | 605.0 | 0.7118 | 430.6 |
| 4 | 665.5 | 0.6355 | 423.0 |
| 5 | 732.1 | 0.5674 | 415.4 |
| | | **Σ** | **2,153.9** |

**Terminal value:**
```
TV₅ = FCFF₅×(1+g)/(WACC−g) = 732.1×1.04/(0.12−0.04)
    = 761.4 / 0.08 = 9,517.3
PV(TV) = 9,517.3 × 0.5674 = 5,400.1
```

**Bridge:**
```
EV        = 2,153.9 + 5,400.1 = 7,554.0
− net debt = − 2,000.0
Equity    = 5,554.0
Per share = 5,554.0 / 30 = ₹185.13
```
**≈ ₹185 per share.** (TV is 5,400/7,554 ≈ **71.5% of EV** — normal, and a reminder of terminal-value dominance.)

---

### Q16. Sensitivity. Redo Q15's terminal value only, with g = 3% and WACC = 13%. What happens to per-share value? (Keep explicit-period PV approximated at the new rate.)

**Solution.**
```
New TV₅ = 732.1×1.03/(0.13−0.03) = 754.1/0.10 = 7,540.6
New factor 1/1.13^5 = 0.5428
PV(TV) = 7,540.6 × 0.5428 = 4,093.0
```
Recompute explicit PV at 13% (factors 0.8850, 0.7831, 0.6931, 0.6133, 0.5428):
```
500×0.8850=442.5; 550×0.7831=430.7; 605×0.6931=419.3;
665.5×0.6133=408.2; 732.1×0.5428=397.4  → Σ = 2,098.1
EV = 2,098.1 + 4,093.0 = 6,191.1
Equity = 6,191.1 − 2,000 = 4,191.1
Per share = 4,191.1 / 30 = ₹139.70
```
**Value falls from ₹185 to ₹140 — a ~24% drop** from a 1-point rise in WACC and 1-point fall in g. This is the textbook illustration of DCF fragility and why you present a range.

---

### Q17. FCFF from EBIT. EBIT ₹900 cr; tax 25%; D&A ₹200 cr; capex ₹350 cr; increase in NWC ₹80 cr. Compute FCFF.

**Solution.**
```
NOPAT = 900 × (1−0.25) = 675
FCFF  = 675 + 200 − 350 − 80 = 445 cr
```
**FCFF = ₹445 crore.**

---

### Q18. FCFE and the two routes. Same firm as Q17: also net income ₹560 cr and net borrowing +₹100 cr. Compute FCFE, and state which discount rate pairs with each flow.

**Solution.**
```
FCFE = Net income + D&A − Capex − ΔNWC + Net borrowing
     = 560 + 200 − 350 − 80 + 100 = 430 cr
```
**FCFE = ₹430 crore.** Pairing: **FCFF (₹445) → discount at WACC → gives EV**; **FCFE (₹430) → discount at cost of equity Ke → gives equity value directly** (no EV bridge needed). Mixing them (FCFF at Ke, or FCFE at WACC) is a classic error.

---

### Q19. Liquidation floor. Book values: cash 200, receivables 600, inventory 500, PP&E 2,500, goodwill 400. Recovery rates: 100%, 80%, 50%, 60%, 0%. Total liabilities 1,800. Wind-down costs 150. Shares 20 cr. Find liquidation value per share.

**Solution.**

| Asset | Book | Rec% | Realizable |
|---|---|---|---|
| Cash | 200 | 100% | 200 |
| Receivables | 600 | 80% | 480 |
| Inventory | 500 | 50% | 250 |
| PP&E | 2,500 | 60% | 1,500 |
| Goodwill | 400 | 0% | 0 |
| **Total** | | | **2,430** |

```
Less liabilities   = − 1,800
Less wind-down     = − 150
Liquidation equity = 480
Per share          = 480 / 20 = ₹24.00
```
**Liquidation floor = ₹24 per share.** If the stock trades well above ₹24, the market is pricing going-concern value; ₹24 is the theoretical downside if operations are wound up.

---

### Q20. DDM. A mature bank pays D₁ = ₹8 next year; cost of equity 12%; perpetual growth 5%. Intrinsic price? Then, if it trades at ₹95, is it cheap or dear?

**Solution.**
```
P₀ = D₁/(Ke − g) = 8/(0.12 − 0.05) = 8/0.07 = ₹114.29
```
Intrinsic ≈ **₹114** vs price ₹95 → price is **below** value by ~17%, so on this model the stock looks **cheap** (undervalued), assuming the 5% growth and 12% Ke are defensible.

---

### Q21. Sum-of-the-parts. A conglomerate has: Division A EBITDA ₹400 cr valued at 7x; Division B EBITDA ₹250 cr valued at 10x; a listed stake worth ₹1,200 cr at market; net debt ₹1,500 cr; 60 cr shares. Find equity value per share.

**Solution.**
```
Division A EV = 7 × 400  = 2,800
Division B EV = 10 × 250 = 2,500
Listed stake  =           1,200
Total gross value        = 6,500
Less net debt            = − 1,500
Equity value             = 5,000
Per share = 5,000 / 60   = ₹83.33
```
**≈ ₹83 per share.** SOTP shines here because each arm earns a different multiple — a single blended multiple would misprice the mix.

---

### Q22. Full triangulation & recommendation. For one company you compute: DCF base ₹185 (bear ₹140), EV/EBITDA comps ₹144, P/E comps ₹144, liquidation floor ₹24. Market price ₹120. Build the football-field verdict.

**Solution.**

| Method | Value/share |
|---|---|
| Liquidation floor | ₹24 |
| Trading comps (EV/EBITDA & P/E) | ₹144 |
| DCF bear → base | ₹140 → ₹185 |
| **Market price** | **₹120** |

The overlap zone (comps ₹144 and DCF bear ₹140) clusters around **₹140–185**; the floor at ₹24 caps downside in a wind-up scenario; price is ₹120 — **below every fundamental estimate except the extreme liquidation floor.** 

**Verdict:** the stock looks **undervalued** — price ₹120 vs a triangulated value zone of roughly ₹140–185, i.e. ~15–35% upside, with the ₹24 floor showing the theoretical worst case. The recommendation (lean **buy**) hinges on whether the DCF's growth assumptions and the peer multiples are justified; if forecast confidence is low, weight the ₹144 comps more and treat ₹140–150 as the anchor, still above price. *Say it as:* "Two independent methods converge near ₹144; the DCF supports at least that with upside; the asset floor bounds downside — price at ₹120 offers a margin of safety."

---

**Self-check note.** All EV↔equity bridges in Q11–Q22 reconcile; every DCF sums explicit PV + PV(TV) and nets debt correctly; multiple-based and DCF estimates are presented as ranges, consistent with the chapter's "no single number" discipline.
