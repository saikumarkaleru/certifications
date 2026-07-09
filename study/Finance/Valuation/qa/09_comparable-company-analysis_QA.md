# Q&A — Comparable Company Analysis (Trading Comps)

A mix of theory (with interview-ready phrasing) and fully solved numerical problems. Numbers are self-checked and reconcile.

---

## Theory

### Q1. What is comparable company analysis and why is it used?

**Answer.** It is a relative valuation method that values a company by applying the trading multiples of similar public companies to the target's own financial metrics. The logic: the stock market has already priced businesses like this one, so their price-to-driver ratios tell you what the target should trade at.

It is used because it is (1) fast — a market-anchored value in an afternoon versus a week for a DCF; (2) market-tested — it reflects real investor opinion, not your own assumptions; and (3) legible — a "peers trade at 9x, we say 8.5x" argument is far easier to defend than a 4,000-row DCF. Its limitation is that it inherits the market's mistakes: it tells you *relative* value, not *intrinsic* value.

**How to say it:** *"Comps value a company off what the market pays for identical businesses right now. It's fast, market-tested and hard to argue with — but it measures relative value, so I always pair it with a DCF for intrinsic value."*

---

### Q2. Explain why a multiple is really "a DCF in disguise."

**Answer.** Start from the Gordon growth model, P0 = D1/(r − g). Divide by next-year earnings and substitute the dividend as payout × earnings:

```
P0 / E1 = payout / (r - g)
```

The forward P/E is literally `payout / (r − g)` — driven by the payout/reinvestment ratio, the cost of equity (risk) and the growth rate. EV/EBITDA behaves the same way: it rises with growth and cash conversion and falls with business risk (WACC). So a multiple is not arbitrary; it silently bundles growth, risk and reinvestment into one number. When two companies trade at different multiples, the reason is always some combination of different growth, cash conversion or risk — never "the market just pays up."

**How to say it:** *"Every multiple is a compressed DCF. Forward P/E equals payout over r minus g, so a high multiple always means high growth, low risk, or low reinvestment need. My job is to name which."*

---

### Q3. State the consistency principle and give the resulting rule for pairing multiples.

**Answer.** A multiple's numerator and denominator must belong to the **same claimants.**

- **Enterprise value** belongs to *all* capital providers (debt + preferred + equity), so it pairs with flows measured *before* financing: Revenue, EBITDA, EBIT, unlevered FCF.
- **Equity value / price** belongs *only* to common shareholders, so it pairs with flows *after* financing: net income, EPS, levered FCF, book equity.

Mixing them — e.g. EV/net income or price/EBITDA — is meaningless. The consequence: EV multiples are capital-structure neutral, equity multiples are not.

**How to say it:** *"EV goes with pre-financing metrics, price goes with post-financing metrics. EV over EBITDA, price over earnings — never cross them."*

---

### Q4. Why is EV/EBITDA usually preferred to P/E?

**Answer.** Three reasons: (1) **capital-structure neutral** — it compares businesses regardless of leverage, whereas P/E is distorted because a levered firm has lower, more volatile net income; (2) **neutral to D&A and tax policy** — EBITDA is before both, so firms with different depreciation schedules or tax situations are comparable; (3) it **proxies pre-financing cash flow**, which is what an acquirer of the whole enterprise is really buying.

Caveats: use P/E for **financials** (EV is ill-defined for a bank), and cross-check capital-intensive firms with EV/EBIT or EV/(EBITDA − capex) because EV/EBITDA ignores the cost of reinvestment.

---

### Q5. Trading comps vs precedent transactions — what is the difference and when do you use each?

**Answer.** Trading comps use **current market prices** of public peers — minority stakes, **no control premium** — so they show where the stock should trade today. Precedent transactions use **prices actually paid in M&A deals**, which embed a **control premium** (typically 20–40%) plus often synergies, so their multiples are systematically higher. Use trading comps for a research target price / "where should the stock trade"; use precedents for "what would an acquirer pay" and to frame a takeover offer.

---

### Q6. What makes a company a good comparable, and how many do you want?

**Answer.** In rough priority: same **business and end markets**, then similar **growth**, **margins**, **size**, **geography**, and **capital intensity** — because a multiple is `payout/(r − g)`, so you are matching risk, growth and reinvestment. Industry classification codes are a starting filter, never the final list; prune manually. Target **6–12 genuinely comparable names** — fewer is noise, more means you loosened comparability. Be ready to defend every inclusion and exclusion.

---

### Q7. LTM vs NTM (forward) multiples — which do you use?

**Answer.** Markets discount the future, so peer prices reflect *forward* expectations — lead with **NTM / FY1** as the headline basis, especially in equity research. Show **LTM** alongside as the factual, un-forecast anchor. For a growing company the forward multiple is *lower* than the trailing one (bigger denominator), and that gap is the market's implied growth. LTM's virtue is that it is actual and un-manipulable; its flaw is that it understates a fast-grower's run-rate.

---

### Q8. Why use the median rather than the mean as the benchmark?

**Answer.** The median is robust to outliers. In a small peer set, a single company at 40x drags the *mean* up several turns but barely moves the median. Best practice: benchmark off the **median**, but display the full distribution — min, 25th, median, mean, 75th, max — so the reader sees the spread. Never quietly delete an outlier to hit a number; exclude only with disclosure and justification.

---

### Q9. What does "cleaning" a multiple involve?

**Answer.** Making numerator and denominator comparable and sustainable.

- **Denominator:** strip non-recurring items (restructuring, impairments, litigation, one-off gains/losses), remove non-operating income, normalize accounting differences (LIFO/FIFO, capitalized vs expensed R&D, lease treatment), apply a *consistent* SBC policy across all peers, and use pro-forma figures for recent M&A.
- **Numerator (EV):** diluted share count (treasury method + in-the-money converts), most recent debt and cash, include preferred/minority/capital leases/pension as debt-like, net out non-operating assets.
- **Outliers:** median over mean; exclude negative/nonsensical multiples with a footnote.

---

### Q10. The company you are valuing grows slower and is riskier than its peers. How do you handle it?

**Answer.** Don't apply the peer median blindly — from `multiple = payout/(r − g)`, lower g and higher r both compress the multiple, so the target deserves a **discount**. Options, crude to refined: (1) a judgmental haircut (e.g. −15% to −20%); (2) position it at the low end of the peer range near the other slow-growers; (3) growth-adjusted multiple (PEG); (4) a **regression** of peer multiples against the driver (e.g. EV/EBITDA vs growth, or EV/Sales vs EBITDA margin) to quantify how many turns each point of growth/margin is worth. State the adjustment explicitly rather than hide it.

---

### Q11. Your DCF says $60 and your comps say $45. Which is right?

**Answer.** Neither — they answer different questions. The DCF is intrinsic value from your assumptions; comps are relative value from the market. The gap means your DCF encodes something the peer prices reject — probably you are more optimistic on growth or margins than the market. Interrogate that assumption, present both as a range on a **football field**, and be explicit about the source of the difference rather than pick one.

---

### Q12. Walk me through comparable company analysis end to end.

**Answer (five steps).** *"First, select a peer set — public companies similar in business, size, geography, growth and margins. Second, standardize — calendarize to a common period, choose LTM or forward, and build a clean diluted enterprise value. Third, calculate and clean the multiples, usually EV/EBITDA and P/E, stripping one-offs from the denominators. Fourth, take the peer median and apply it to my company's matching metric to get implied enterprise value, then bridge to equity and per share. Fifth, adjust for how my company differs on growth, margins and risk, and present a range, not a point."*

---

## Numerical problems

### Q13. Build EV and compute EV/EBITDA.

**Problem.** Company: share price $40, diluted shares 100m, total debt $1,200m, cash $300m, preferred $100m, minority interest $50m, LTM EBITDA $500m. Compute enterprise value and EV/EBITDA.

**Solution.**
```
Equity value = 40 x 100 = $4,000m
EV = 4,000 + 1,200 (debt) + 100 (pref) + 50 (MI) - 300 (cash) = $5,050m
EV/EBITDA = 5,050 / 500 = 10.1x
```
**Answer:** EV = **$5,050m**, EV/EBITDA = **10.1x**.
*Check:* reverse the bridge — 5,050 − 1,200 − 100 − 50 + 300 = 4,000 = equity value. ✓

---

### Q14. From peer median to value per share (full bridge).

**Problem.** Peers' median NTM EV/EBITDA = 8.5x. Target NTM EBITDA = $600m, total debt $1,500m, cash $200m, no preferred/minority, diluted shares 80m. Find implied value per share.

**Solution.**
```
Implied EV = 8.5 x 600 = $5,100m
Implied equity = 5,100 - 1,500 (debt) + 200 (cash) = $3,800m
Value per share = 3,800 / 80 = $47.50
```
**Answer:** **$47.50 per share.**
*Check:* equity 3,800 + net debt 1,300 (1,500 − 200) = 5,100 EV → ÷ 600 = 8.5x, the multiple applied. ✓

---

### Q15. Median and mean from a peer table; explain the difference.

**Problem.** Six peers' EV/EBITDA: 7.0, 7.5, 8.0, 8.5, 9.0, 15.0. Compute median and mean and say which to use.

**Solution.**
```
Sorted: 7.0, 7.5, 8.0, 8.5, 9.0, 15.0 (already sorted)
Median = average of 3rd and 4th = (8.0 + 8.5)/2 = 8.25x
Mean = (7.0+7.5+8.0+8.5+9.0+15.0)/6 = 55.0/6 = 9.17x
```
**Answer:** median **8.25x**, mean **9.17x**. Use the **median** — the 15.0x outlier inflates the mean by ~0.9 turns but barely moves the median. Check whether the 15.0x peer is a data error or a genuinely different (faster-growing) business; consider footnoting or excluding it.

---

### Q16. LTM bridge.

**Problem.** December year-end company. FY2025 EBITDA = $420m; H1-2026 (Jan–Jun) = $250m; H1-2025 (Jan–Jun) = $210m. Compute LTM EBITDA as of Jun-2026.

**Solution.**
```
LTM = FY2025 + H1-2026 - H1-2025
    = 420 + 250 - 210 = $460m
```
**Answer:** **$460m.**
*Logic check:* we swapped the stale first half of 2025 ($210m) for the fresh first half of 2026 ($250m), a +$40m uplift over the $420m base → $460m. Consistent with a growing firm. ✓

---

### Q17. Calendarization.

**Problem.** A June year-end peer: FY ending Jun-2026 EBITDA = $400m; FY ending Jun-2027 (est) = $480m. Estimate calendar-year 2026 EBITDA using the weighted-fiscal-year method.

**Solution.** Calendar 2026 (Jan–Dec) = second half of FY Jun-2026 + first half of FY Jun-2027, each weight 0.5:
```
Calendar-2026 EBITDA = 0.5 x 400 + 0.5 x 480 = 200 + 240 = $440m
```
**Answer:** **$440m.** This lets you compare the June year-end peer against December year-end peers on a common calendar-2026 basis.

---

### Q18. Cleaning EBITDA before computing the multiple.

**Problem.** Reported EBITDA = $300m, but it includes: a $25m restructuring charge (one-off cost), a $15m gain on asset sale (one-off), and $10m of SBC that was added back (house policy: SBC is a real expense). EV = $2,400m. Compute clean EBITDA and clean EV/EBITDA.

**Solution.**
```
Clean EBITDA = 300 + 25 (add back one-off cost)
                   - 15 (remove one-off gain)
                   - 10 (reverse the SBC add-back)
             = $300m
Clean EV/EBITDA = 2,400 / 300 = 8.0x
```
**Answer:** clean EBITDA = **$300m**, clean EV/EBITDA = **8.0x**. (Coincidentally the adjustments net to zero here — the point is that on *reported* EBITDA the ratio might have looked different; always normalize before comparing.)

---

### Q19. Growth adjustment via PEG.

**Problem.** Peers trade at a median forward P/E of 21.0x and grow EPS at 14%/yr, giving a peer PEG of 1.5x. The target grows EPS at only 9%/yr. Using the peer PEG, what forward P/E does the target deserve, and if target EPS = $3.00, what is the implied share price?

**Solution.**
```
Implied target P/E = PEG x growth = 1.5 x 9 = 13.5x
Implied share price = 13.5 x 3.00 = $40.50
```
**Answer:** implied forward P/E **13.5x**, price **$40.50.** The slower grower is worth a materially lower P/E (13.5x vs the peers' 21.0x), quantified through PEG rather than eyeballed.
*Check:* peer P/E 21.0 ÷ growth 14 = 1.5 PEG; applying the same PEG to 9% growth gives 13.5x. Internally consistent. ✓

---

### Q20. Full valuation with cleaning, adjustment, and cross-check.

**Problem.** Peers: median NTM EV/EBITDA = 11.0x, median NTM P/E = 20.0x. Target reported EBITDA = $520m including a $40m impairment (one-off) and a $20m one-off insurance gain. Target is riskier and slower-growing than peers → apply a 10% discount to peer multiples. Target: debt $1,800m, cash $300m, preferred $200m, minority $100m, diluted shares 60m, clean net income $180m. Find implied value per share by EV/EBITDA, then cross-check with P/E.

**Solution.**

*Clean EBITDA:*
```
Clean EBITDA = 520 + 40 (add back impairment) - 20 (remove gain) = $540m
```

*Adjusted multiples (−10%):*
```
Adj EV/EBITDA = 11.0 x 0.90 = 9.9x
Adj P/E       = 20.0 x 0.90 = 18.0x
```

*EV/EBITDA path:*
```
Implied EV = 9.9 x 540 = $5,346m
Implied equity = 5,346 - 1,800 (debt) - 200 (pref) - 100 (MI) + 300 (cash)
              = 5,346 - 1,800 = $3,546m
Per share = 3,546 / 60 = $59.10
```

*P/E cross-check:*
```
Implied equity (P/E) = 18.0 x 180 = $3,240m
Per share = 3,240 / 60 = $54.00
```

**Answer:** EV/EBITDA implies **$59.10**, P/E implies **$54.00** → present a range of roughly **$54–$59 per share.** The gap reflects that the two multiples weight leverage and D&A differently; a range is more honest than a single number.
*Check on EV bridge:* equity 3,546 + debt 1,800 + pref 200 + MI 100 − cash 300 = 5,346 EV → ÷ clean EBITDA 540 = 9.9x, the multiple applied. ✓

---

### Q21. Reverse-engineering an implied growth rate from a multiple.

**Problem.** A company trades at a forward P/E of 25x. Its payout ratio is 40% and cost of equity is 10%. Using the identity P/E = payout/(r − g), what growth rate is the market implying?

**Solution.**
```
25 = 0.40 / (0.10 - g)
0.10 - g = 0.40 / 25 = 0.016
g = 0.10 - 0.016 = 0.084 = 8.4%
```
**Answer:** the market is implying **~8.4% perpetual earnings growth.** This is how you sanity-check a rich multiple — if 8.4% forever looks implausible for a mature firm, the stock is priced for more growth than it can deliver.
*Check:* 0.40 / (0.10 − 0.084) = 0.40 / 0.016 = 25x. ✓

---

### Q22. EV/Sales for a loss-making company, with a margin adjustment.

**Problem.** A pre-profit software target has NTM revenue of $250m and negative EBITDA, so EV/EBITDA is unusable. Peers trade at a median EV/Sales of 6.0x at a median EBITDA margin of 30%. The target's expected steady-state margin is only 20%. Adjust EV/Sales proportionally to margin and value the equity. Target has no debt, $80m cash, 25m diluted shares.

**Solution.** Since EV/Sales scales roughly with margin, adjust for the margin gap (20% vs 30%):
```
Adj EV/Sales = 6.0 x (20% / 30%) = 6.0 x 0.667 = 4.0x
Implied EV = 4.0 x 250 = $1,000m
Implied equity = 1,000 - 0 (no debt) + 80 (cash) = $1,080m
Per share = 1,080 / 25 = $43.20
```
**Answer:** implied value **$43.20 per share.** EV/Sales is the right tool when EBITDA is negative, but because it ignores profitability you *must* adjust for the margin gap — a 20%-margin firm should not command the same EV/Sales as a 30%-margin peer.
*Check:* equity 1,080 − cash 80 = 1,000 EV → ÷ sales 250 = 4.0x, the adjusted multiple. ✓
