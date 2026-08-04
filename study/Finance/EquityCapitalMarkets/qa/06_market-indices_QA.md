# Q&A — Market Indices

Theory and worked scenarios on index construction, weighting, and mechanics.

---

### Q1. How are the Nifty 50 and Sensex constructed, precisely — not just "market-cap weighted"?

**Model answer.** Both are **free-float market-capitalisation weighted** indices of large-cap stocks (50 for Nifty on NSE, 30 for Sensex on BSE) — weight is proportional to the value of each company's *publicly tradable* shares, specifically excluding promoter, government, and other strategic/locked holdings. Saying only "market-cap weighted" without the free-float qualifier is an incomplete answer and a common interview gap, since free-float is the specific design choice that makes the index reflect genuinely investable value rather than raw company size.

---

### Q2. Worked — free-float weight calculation.
*Company P: total market cap ₹5,000 cr, promoter holding 55% (locked/strategic). Company Q: total market cap ₹3,200 cr, promoter holding 15%. Which gets a larger index weight, and by how much (in free-float value terms)?*

**Model answer.**
Company P free-float = 45% × 5,000 = ₹2,250 cr.
Company Q free-float = 85% × 3,200 = ₹2,720 cr.
Despite Company P having a larger total market cap (₹5,000 cr vs ₹3,200 cr), Company Q gets the larger index weight because its free-float value (₹2,720 cr) exceeds P's (₹2,250 cr) — a direct illustration that total company size and index weight are not the same thing once free-float is applied.

---

### Q3. Why doesn't a stock split or bonus issue move the index level, even though it changes the share price and share count?

**Model answer.** The index uses a **divisor** — a normalising constant recalculated whenever a mechanical, non-value change occurs (splits, bonus issues, constituent additions/deletions, buybacks). A split halves the price and doubles the share count with market cap unchanged; the divisor is adjusted so the index's calculated value doesn't move from this purely mechanical change. The divisor is what allows the index to be a continuous, comparable series over time despite constant structural changes to its constituents.

---

### Q4. What's the practical, real-money consequence of a stock being added to (or removed from) a major index like the Nifty 50?

**Model answer.** Passive funds and ETFs that track the index are mandated to hold constituents in index-matching proportions — when a stock is added at a scheduled rebalance, every fund tracking that index must buy it (and sell any removed stock), creating real, mechanical buying (or selling) pressure independent of the company's fundamentals. This is why stocks often see a price bump running into a confirmed index-inclusion date, and why "will this stock get added to the index" is itself a research question with a trading implication, separate from fundamental valuation.

---

### Q5. Price-weighted vs market-cap-weighted indices — what's the practical flaw of price-weighting that market-cap weighting avoids?

**Model answer.** A price-weighted index (like the Dow Jones) gives a higher-priced stock more influence on the index level regardless of the company's actual size — a ₹5,000 stock in a small company would move a price-weighted index more than a ₹200 stock in a much larger company, which is economically arbitrary (share price level is just a function of how many shares are outstanding, not company value). Market-cap weighting (Nifty, Sensex, S&P 500) ties influence to actual company/free-float value, which is both more economically meaningful and matches how a real buy-and-hold portfolio would naturally be weighted.

---

### Q6. What is a total return index (TRI), and why does using a price index instead understate a long-term equity fund's true relative performance?

**Model answer.** A price index tracks only price changes, ignoring dividends paid by constituents. A total return index reinvests those dividends back into the index calculation. Since an actively or passively managed equity fund also earns and (usually) reinvests dividends from its holdings, benchmarking the fund's total return against a price-only index systematically understates the index's true comparable performance — over long periods, the dividend-reinvestment gap between a price index and its TRI equivalent compounds to a meaningful difference, which is why professional performance reporting should always use the TRI, not the more commonly quoted headline price index.

---

### Q7. Worked — divisor mechanics illustrated with numbers.
*A simplified 2-stock index: Stock A, 100 shares free-float at ₹50 (₹5,000), Stock B, 200 shares free-float at ₹40 (₹8,000). Total free-float value = ₹13,000. If the divisor is 130, the index value = 13,000/130 = 100. Stock A now does a 2-for-1 split: 200 shares at ₹25 (still ₹5,000 total). What must the new divisor be to keep the index at 100, and why?*

**Model answer.** Post-split total free-float value is unchanged (200 × 25 = ₹5,000 for A, plus B's unchanged ₹8,000 = ₹13,000 total) — since the underlying value hasn't changed, the divisor also doesn't need to change here (it stays at 130, index value = 13,000/130 = 100). The divisor only needs to be *recalculated* when a change alters the *aggregate free-float value* itself without a corresponding real value change — e.g. when a constituent is swapped for a different one, or free-float percentage changes (a promoter selling down increases free-float value without a price change) — a split alone, since it's price × share-count neutral, is actually one of the simpler cases, though it's still routinely cited alongside divisor mechanics because the underlying principle (isolating real value changes from mechanical ones) is the same.

---

### Q8. Beyond Nifty 50 and Sensex, name and briefly describe two other categories of Indian indices and what each is used for.

**Model answer.** Broader market-cap indices (Nifty 100/500, Nifty Midcap, Nifty Smallcap) — used to benchmark funds and strategies focused outside just the largest 50 companies, giving a fuller picture of mid- and small-cap segment performance. Sectoral/thematic indices (Bank Nifty, Nifty IT, Nifty Auto, Nifty Pharma, etc.) — used to benchmark sector-focused funds, to trade sector-specific derivatives (Bank Nifty options are among the most actively traded derivatives contracts in India), and by analysts to gauge relative sector performance and rotation trends within the broader market.
