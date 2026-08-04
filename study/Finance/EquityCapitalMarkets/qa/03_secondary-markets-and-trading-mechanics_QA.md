# Q&A — Secondary Markets & Trading Mechanics

Theory and worked scenarios on order types, spreads, and settlement.

---

### Q1. Market order vs limit order — what does each guarantee, and what does each not guarantee?

**Model answer.** A market order guarantees execution (it fills immediately against the best available price on the other side of the book) but not the price you'll pay — in a fast-moving or thin market you can be filled well away from the last traded price. A limit order guarantees the price (it will only execute at your specified price or better) but not execution — if the market never trades at your price, the order simply sits unfilled. The choice is a direct trade-off between price certainty and execution certainty.

---

### Q2. Worked — computing market impact from the order book.
*Best bid ₹248.50 (2,000 shares), next bid ₹248.20 (5,000 shares); best ask ₹249.00 (1,500 shares), next ask ₹249.40 (4,000 shares). You need to sell 5,000 shares immediately as a market order.*

**Model answer.** Selling into the bid side: the first 2,000 shares execute at ₹248.50, the remaining 3,000 shares execute at ₹248.20 (the next price level down), since the top level's depth is exhausted. Volume-weighted average execution price = (2,000×248.50 + 3,000×248.20) / 5,000 = (497,000 + 744,600) / 5,000 = ₹248.32 — worse than the ₹248.50 best bid, illustrating market impact: a large order "walks the book" and gets a worse average price than the top-of-book quote suggests.

---

### Q3. Why is a short seller's maximum loss theoretically unlimited, while a long position's maximum loss is capped?

**Model answer.** A long position's downside is capped at the amount invested — the price can only fall to zero. A short position involves selling borrowed shares with the obligation to buy them back later to return them; since a stock's price has no theoretical ceiling, the cost to buy back and close a short position can rise without bound, making the potential loss theoretically unlimited. This asymmetry is why short positions require margin, active risk management, and often stop-loss discipline that a comparable long position may not need as urgently.

---

### Q4. What roles do the clearing corporation and the depository each play in a single trade, and why are they separate entities?

**Model answer.** The clearing corporation (e.g. NSE Clearing) becomes the central counterparty to every matched trade — it guarantees settlement to both sides, so neither party bears the other's default risk. The depository (NSDL/CDSL) holds securities in dematerialised electronic form and executes the actual transfer of shares between demat accounts on settlement. They're separate because they solve different frictions: the clearing corp manages counterparty/credit risk across the whole market, while the depository manages custody and the mechanical transfer of ownership records — conflating them (a common interview trap) misses that one guarantees the trade and the other physically moves the asset.

---

### Q5. What does "market depth" measure, and why does an analyst or trader care about it beyond the headline bid-ask spread?

**Model answer.** Depth measures the quantity available at each price level near the top of the order book, not just the best bid/ask. A narrow spread can be misleading if depth is thin — a seemingly liquid-looking stock with a tight spread but only 200 shares at the best bid will show significant market impact (Q2) on any order larger than that, even though the quoted spread alone looks attractive. Depth, not spread alone, determines how much size can actually be traded near the current price.

---

### Q6. Explain price-time priority in order matching with a worked example.
*Two limit buy orders both at ₹100: Order A for 500 shares placed at 9:15:02am, Order B for 800 shares placed at 9:15:05am. A sell market order for 600 shares arrives.*

**Model answer.** Price-time priority matches the best price first, and among orders at the same price, the earliest-placed order first. Order A (earlier, same price) fills completely (500 shares), and the remaining 100 shares of the incoming sell order fill against Order B, leaving Order B with 700 shares still resting in the book. Time priority at a given price level rewards being first in the queue, not just posting a competitive price.

---

### Q7. What's the difference between an order-driven and a quote-driven market structure?

**Model answer.** An order-driven market (NSE/BSE's central limit order book) lets any participant post bids/asks directly, with the exchange's matching engine pairing them by price-time priority — price discovery emerges from aggregated public orders. A quote-driven market relies on designated dealers/market-makers who continuously post two-way (buy and sell) quotes that others trade against — price discovery is mediated through the dealer's quoted spread rather than a fully open book. Most modern equity markets, including Indian exchanges, are primarily order-driven, though market-makers/liquidity providers still operate within that order-driven structure to supply depth.

---

### Q8. Why would a trader use a stop-limit order instead of a plain stop-loss order?

**Model answer.** A plain stop-loss becomes a *market* order once the trigger price is hit, guaranteeing execution but not the price — in a fast-falling/gapping market, the actual fill can be significantly worse than the trigger level. A stop-limit becomes a *limit* order once triggered, capping the worst acceptable execution price — but risks not executing at all if the price gaps straight through the limit without trading at an acceptable level. The choice reflects the same execution-certainty-vs-price-certainty trade-off as Q1, applied specifically to risk-management/exit orders.
