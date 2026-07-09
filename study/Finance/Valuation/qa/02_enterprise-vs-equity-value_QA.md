# Q&A — Enterprise Value vs Equity Value — the Bridge

A mixed bank of **theory** (with model answers and "how to say it in an interview") and **numerical problems** (fully solved, numbers self-verified and reconciling). Work each one before reading the answer.

---

## Theory questions

### Q1. Define enterprise value and equity value in one breath each.

**Answer.** *Equity value* is the value of the business to its common shareholders — for a public company, share price times diluted shares (market cap). *Enterprise value* is the value of the core operating business to **all** capital providers — debt, preferred, minority interest and equity combined — and is independent of capital structure.

**How to say it:** "Equity value is what the stock is worth; enterprise value is what the whole operating business is worth to everyone who financed it. EV strips out how the company is financed so you can compare businesses cleanly."

---

### Q2. Why is enterprise value described as "capital-structure neutral," and why does that matter?

**Answer.** Two companies can run identical operations but finance themselves differently — one all-equity, one half-debt. Their equity values differ (debt sits ahead of equity, making the levered company's equity smaller and riskier), but the *operating machine* is worth the same, so their enterprise values are equal. It matters because when you compare companies via multiples you want to compare the *businesses*, not the financing choices. EV neutralises leverage; equity value is contaminated by it.

**How to say it:** "EV is the number that stays the same whether you fund the business with debt or equity, so it's the right basis for comparing operations across companies."

---

### Q3. Walk me through the full bridge from equity value to enterprise value. Explain every sign.

**Answer.**
- **Start: Equity Value.**
- **+ Debt** — a senior claim; an acquirer inherits and must repay it, so it adds to the true cost.
- **+ Preferred stock** — senior to common; behaves like debt, so add it.
- **+ Minority interest** — the financials consolidate 100% of controlled subsidiaries, but outside shareholders own a slice; add it so EV reflects the whole consolidated enterprise.
- **− Cash** — a non-operating asset the acquirer receives and can use to repay debt; it offsets cost.
- **− Investments / marketable securities** — non-operating; not part of core operations.
- **− Investments in associates** — non-operating; their earnings sit outside operating metrics, so hand their value back to equity.
- **= Enterprise Value.**

**Principle to state:** "Going up to EV, I add every claim senior to equity and subtract every non-operating asset. Reverse all signs to go back down to equity value."

---

### Q4. Which financial metrics pair with enterprise value and which with equity value? Give the underlying rule.

**Answer.** The rule: **numerator and denominator must belong to the same investors.**
- **EV metrics** are *pre-interest* (available to all): Revenue, EBITDA, EBIT, unlevered FCF, NOPAT.
- **Equity metrics** are *post-interest* (available to equity only): Net income, EPS, levered FCF, book value, dividends.

**The on-the-spot test:** "Is interest deducted before you reach this metric? If no, it's a whole-firm number → use EV. If yes, it's an equity number → use equity value." So EV/EBITDA and P/E are right; EV/Net Income and P/EBITDA are wrong.

---

### Q5. Why do we subtract cash when going from equity value to EV? Give more than one reason.

**Answer.** Three consistent reasons:
1. **Acquirer's view** — cash becomes yours on acquisition and can repay debt, reducing net cost.
2. **Non-operating view** — EV captures only the operating enterprise; cash is a non-operating asset, so remove it.
3. **Consistency view (the strongest)** — EBITDA is pre-interest and excludes interest *income* earned on cash; to keep EV/EBITDA consistent, the cash that generates that excluded income must also be excluded from the numerator.

**How to say it:** "Cash comes out because it isn't part of operations and because an acquirer uses it to pay down the debt they inherit — net debt, not gross debt, is what you're really buying."

---

### Q6. Can equity value exceed enterprise value? Can EV be negative?

**Answer.** Yes to both. If a company holds more cash (and liquid investments) than debt — a **net cash** position — then EV = Equity Value + Net Debt is *less* than equity value. Many cash-rich tech companies show this. In extreme cases (huge cash pile, tiny operating value, or distress) EV can even be negative. There is no law that EV must exceed equity value.

**How to say it:** "It's driven entirely by net debt. Net cash flips equity value above EV — that's normal, not an error."

---

### Q7. Why must minority interest be added to EV, and why must associates be subtracted?

**Answer.** They are opposite situations:
- **Minority interest** arises when the parent *controls but doesn't fully own* a subsidiary. The income statement **consolidates 100%** of that subsidiary's revenue and EBITDA. To make EV consistent with that 100%-consolidated metric, you must add the value of the slice owned by outsiders — the minority interest.
- **Associates** (equity-method stakes, typically 20–50% ownership, no control) are **not consolidated**; only a one-line "share of profit" appears *below* operating income. Operating EBITDA/EBIT therefore contains *none* of the associate. So its value must be *removed* from EV (subtracted) and handed to equity, to stay consistent.

**One-liner:** "Minority interest is in the operating numbers but not owned, so add it; associates are owned but not in the operating numbers, so subtract them."

---

### Q8. What is the treasury stock method and when do you use it?

**Answer.** The TSM converts **in-the-money** options and warrants into net new shares for the diluted count. Assume all in-the-money options are exercised (adds shares) and the company uses the strike proceeds to buy back shares at the current market price (removes shares). Net new shares = Options × (1 − Strike ÷ Price). Out-of-the-money options are ignored. You use it whenever you compute diluted shares for equity value / per-share figures.

**How to say it:** "In-the-money options exercise, the company takes the strike cash and repurchases stock at market, and the difference is the net dilution."

---

### Q9. "Walk me through a DCF" — describe just the ending, from cash flows to share price.

**Answer.** "I discount the unlevered free cash flows and the terminal value at WACC — because unlevered FCF is pre-financing, discounting it gives **enterprise value**. Then I bridge to equity: subtract net debt, preferred and minority interest, add investments in associates, to get **equity value**. Finally I divide equity value by **diluted** shares — treasury stock method for options — to get the implied share price, and compare it to the current market price."

**Why this is right:** unlevered cash flow belongs to all capital providers, so its present value is a whole-firm number (EV); you then peel off the non-equity claims to isolate equity.

---

### Q10. A company issues $500m of debt and holds the proceeds as cash. What happens to EV and equity value?

**Answer.** Nothing changes. Debt rises $500m (adds to EV) but cash rises $500m (subtracts from EV); net debt is unchanged, so EV is unchanged. Equity value is also unchanged — no operating asset moved. This is the textbook demonstration that EV looks through financing.

---

### Q11. Does a share buyback funded with cash change enterprise value?

**Answer.** No (at fair value). Equity value falls by the cash spent; cash falls by the same amount, so net debt rises by that amount. The two effects offset — equity down X, net debt up X — leaving EV unchanged. The buyback re-levers the equity but doesn't change the value of the operating business.

---

### Q12. Why is EV/EBITDA often preferred to P/E when comparing companies?

**Answer.** Because EV/EBITDA neutralises both **capital structure** (EBITDA and EV are both pre-financing) and **non-cash/accounting choices** like depreciation and, to a degree, tax. P/E is distorted by leverage (interest hits net income), by different tax rates, and by D&A policy. So EV/EBITDA compares the *operating economics* more cleanly; P/E is more affected by how the company is financed and taxed.

---

## Numerical problems

### Q13. Basic bridge. Share price $25, diluted shares 200m, total debt $1,500m, cash $400m, no preferred/minority/associates. Find equity value and EV.

**Solution.**
Equity Value = $25 × 200m = **$5,000m**.
Net Debt = 1,500 − 400 = $1,100m.
EV = 5,000 + 1,100 = **$6,100m**.

**Check (reverse):** 6,100 − 1,500 + 400 = 5,000 ✓.

---

### Q14. Full bridge with all items. Equity value $3,000m, debt $900m, preferred $200m, minority interest $100m, cash $250m, associates $150m. Find EV, then reverse to confirm.

**Solution.**

| Line | Amount | Running |
|---|---:|---:|
| Equity Value | 3,000 | 3,000 |
| + Debt | +900 | 3,900 |
| + Preferred | +200 | 4,100 |
| + Minority interest | +100 | 4,200 |
| − Cash | −250 | 3,950 |
| − Associates | −150 | **3,800** |

**EV = $3,800m.**
**Reverse check:** 3,800 − 900 − 200 − 100 + 250 + 150 = 3,000 ✓ — reconciles to equity value.

---

### Q15. Treasury stock method. Basic shares 80m, price $40, options 10m at strike $24 (in the money), 4m at strike $50 (out of the money). Find diluted shares.

**Solution.**
Tranche 1 (strike $24 < $40 → in the money): net new = 10m × (1 − 24/40) = 10m × 0.40 = **4.0m**.
(Longhand: cash received 10m × 24 = 240m; buyback 240/40 = 6m; net = 10 − 6 = 4m ✓.)
Tranche 2 (strike $50 > $40 → out of the money): **0**.
Diluted shares = 80 + 4.0 + 0 = **84.0m**.

---

### Q16. TSM into equity value and a multiple. From Q15's 84.0m diluted shares at $40: total debt $700m, cash $100m, LTM EBITDA $300m. Find equity value, EV and EV/EBITDA.

**Solution.**
Equity Value = $40 × 84.0m = **$3,360m**.
Net Debt = 700 − 100 = $600m.
EV = 3,360 + 600 = **$3,960m**.
EV/EBITDA = 3,960 ÷ 300 = **13.2x**.

**Consistency note:** EBITDA is pre-interest, correctly paired with EV. Using market cap instead would give 3,360/300 = 11.2x and wrongly ignore the $600m net debt that also has a claim on that EBITDA.

---

### Q17. Reverse bridge — net cash company. DCF gives EV $4,500m; debt $500m, cash $1,800m, preferred $0, minority $0, associates $200m; diluted shares 120m. Find equity value and share price.

**Solution.**
Equity Value = EV − Debt + Cash + Associates = 4,500 − 500 + 1,800 + 200 = **$6,000m**.
Share price = 6,000 ÷ 120 = **$50.00**.

**Observation:** Equity value ($6,000m) exceeds EV ($4,500m) because the company is net cash (cash $1,800m ≫ debt $500m). That is correct, not a mistake.
**Reverse check:** 6,000 + 500 (debt) − 1,800 (cash) − 200 (assoc) = 4,500 ✓.

---

### Q18. Convertible in the money (if-converted). EV $10,000m; straight debt $2,000m; convertible face $600m converting into 30m shares at $20 conversion price; preferred $400m; minority $200m; cash $900m; basic shares 200m; current price ~$45. Find equity value and share price.

**Solution.**
The convert is in the money ($45 > $20), so it converts: **remove $600m from debt** and **add 30m shares**.
Diluted shares = 200 + 30 = 230m (assume no options here).
Walk down: Equity = EV − straight debt − preferred − minority + cash (convert excluded as it converted)
= 10,000 − 2,000 − 400 − 200 + 900 = **$8,300m**.
Share price = 8,300 ÷ 230 = **$36.09**.

**Check the conversion decision holds:** implied $36.09 still far above the $20 conversion price, so if-converted treatment stands. ✓
**Reverse check:** 8,300 + 2,000 + 400 + 200 − 900 = 10,000 ✓ (convert nets to zero on both sides).

---

### Q19. "Issue debt to buy a factory." A firm with EV $6,000m and equity value $5,000m issues $500m of debt and immediately spends it all on a factory. State EV and equity value right after.

**Solution.**
Step 1 — raise debt: debt +$500m, cash +$500m → net debt unchanged → EV unchanged at $6,000m; equity unchanged at $5,000m.
Step 2 — spend cash on factory: cash −$500m, operating assets +$500m → net debt rises $500m, *but* this is offset in EV by the new operating asset only insofar as it changes future cash flows; at the instant of purchase the fair value swap leaves EV ≈ **$6,000m** and equity value = **$5,000m** unchanged. Net debt is now $500m higher than at the very start, offset by the factory's value inside the operating enterprise.

**Interview line:** "Financing and the asset swap don't move EV; only the future operating returns from the factory will."

---

### Q20. Full end-to-end. Basic shares 150m; price $60; options 8m strike $30 (ITM), 5m strike $80 (OTM); RSUs 2m; total debt $1,200m; preferred $300m; minority $150m; cash $500m; associates $250m; LTM EBITDA $900m. Find diluted shares, equity value, EV, and EV/EBITDA.

**Solution.**
TSM: ITM tranche net new = 8m × (1 − 30/60) = 8m × 0.5 = 4.0m. OTM tranche = 0. RSUs = 2.0m.
Diluted shares = 150 + 4.0 + 0 + 2.0 = **156.0m**.
Equity Value = $60 × 156.0m = **$9,360m**.
EV = Equity + Debt + Preferred + Minority − Cash − Associates
= 9,360 + 1,200 + 300 + 150 − 500 − 250 = **$10,260m**.
EV/EBITDA = 10,260 ÷ 900 = **11.4x**.

**Reverse check:** 10,260 − 1,200 − 300 − 150 + 500 + 250 = 9,360 ✓.

---

### Q21. Multiple-consistency catch. Company A: EV $8,000m, EBITDA $1,000m, net income $400m, market cap $6,000m. A junior quotes "EV/Net Income = 20x" and "P/EBITDA = 6x." Are these valid? Fix them.

**Solution.** Both are **inconsistent** (they mix whole-firm and equity metrics).
- EV/Net Income mixes a whole-firm numerator with an equity denominator. Correct equity metric with EV's partner: **EV/EBITDA = 8,000/1,000 = 8.0x**.
- P/EBITDA mixes equity price with a whole-firm metric. Correct pairing: **P/E = 6,000/400 = 15.0x**.

**Rule restated:** pre-interest metric (EBITDA) → EV; post-interest metric (net income) → equity value.

---

### Q22. Net cash to negative-ish EV intuition. Company holds $3,000m cash, $200m debt, no other claims; market cap $2,500m; 100m diluted shares. Compute EV and comment.

**Solution.**
Net Debt = 200 − 3,000 = **−$2,800m** (net cash).
EV = Equity Value + Net Debt = 2,500 + (−2,800) = **−$300m**.
**Comment:** EV is *negative* — the market values the equity below its net cash. That signals the market expects the operating business to *destroy* value (burn the cash) or there are hidden liabilities; it is a real, if unusual, situation. Share price = 2,500/100 = $25, of which $28/share is net cash — the operations carry −$3/share of implied value.

**Interview line:** "Negative EV means the company's net cash exceeds its whole market cap — the market is pricing the operating business as a net liability."

---

### Q23. Circularity in TSM (stretch). EV $5,000m; net debt $500m; basic shares 90m; options 10m strike $25. Current market price $45. Find the implied share price using (a) current price for TSM, then (b) one iteration at the implied price. Comment on convergence.

**Solution.**
Equity Value = EV − Net Debt = 5,000 − 500 = $4,500m (fixed).
(a) TSM at $45: net new = 10m × (1 − 25/45) = 10m × 0.4444 = 4.444m; diluted = 94.444m; price = 4,500/94.444 = **$47.65**.
(b) Iterate at $47.65: net new = 10m × (1 − 25/47.65) = 10m × 0.4753 = 4.753m; diluted = 94.753m; price = 4,500/94.753 = **$47.49**.
Iterate again at $47.49: net new = 10m × (1 − 25/47.49) = 4.736m; diluted = 94.736m; price = 4,500/94.736 = **$47.50**.
**Comment:** the sequence $47.65 → $47.49 → $47.50 converges within two cents in one to two iterations. In interviews, fixing TSM at the current price is close enough; in a model you'd toggle a circular reference to converge exactly.

---

*End of Q&A bank — 23 questions (12 theory, 11 numerical), all bridges reconciled and per-share math verified.*
