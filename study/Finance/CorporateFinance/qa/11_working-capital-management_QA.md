# Q&A — Working Capital Management

A mixed bank of theory (with model answers and interview phrasing) and fully solved numericals. Numbers are self-verified and internally consistent.

---

## Theory

### Q1. Define working capital and distinguish gross from net working capital.
**Answer.** *Gross working capital* is total current assets — the pool of short-term assets (cash, receivables, inventory) used in daily operations. *Net working capital* is current assets minus current liabilities — the portion of current assets financed by long-term sources, i.e., the genuine liquidity cushion. Analysts usually focus on **operating** NWC (receivables + inventory − payables − accruals), stripping out cash and short-term debt, because that isolates the cash tied up in the operating cycle.
**Say it in an interview:** "Gross WC is the size of the current-asset pool; net WC is what's left after current liabilities — the real cushion. For cash-flow work I use operating NWC and exclude cash and debt."

### Q2. Explain the cash conversion cycle and why a shorter one is better.
**Answer.** CCC = DIO + DSO − DPO. It measures the days between paying cash out to suppliers and collecting from customers — the self-funding window. A shorter CCC means less capital frozen in operations, less need for external financing, and a higher return on capital. Negative CCC means the business is financed by its suppliers and customers.
**Say it:** "CCC is how long my own cash is stuck in the operating cycle. Lower means I free up capital; negative means suppliers and customers fund me."

### Q3. How can a profitable company go bankrupt?
**Answer.** Profit is accrual; solvency is cash. A fast-growing firm with positive working-capital intensity sinks cash into inventory and receivables *ahead* of collecting on sales; payables don't stretch enough to cover the gap; the funding shortfall grows with sales until liquidity runs out. Profit on the P&L, no cash in the bank.
**Say it:** "Profit is an opinion, cash is a fact. Growth with positive working-capital intensity consumes cash faster than profit generates it."

### Q4. What is spontaneous financing, and why is it valuable?
**Answer.** Spontaneous financing arises automatically from operations — trade payables and accrued expenses (wages, taxes owed but unpaid). It scales with the business, requires no negotiation, and is free within terms. It's the first and cheapest layer of working-capital funding; only what spontaneous sources don't cover needs negotiated financing.
**Say it:** "Payables and accruals fund me for free and grow with the business — I only finance the gap they don't cover."

### Q5. Describe the four levers of credit policy.
**Answer.** (1) **Credit standards** — who qualifies (the 5 Cs: Character, Capacity, Capital, Collateral, Conditions); (2) **credit terms** — the discount and net period, e.g., 2/10 net 30; (3) **credit period** — how long customers get; (4) **collection policy** — how aggressively you chase. Relaxing any lever tends to lift sales but raises receivables investment, bad debts, and collection cost. Relax only if incremental contribution beats incremental costs.

### Q6. What is the maturity-matching (hedging) principle?
**Answer.** Match the life of the financing to the life of the asset. Permanent working capital — the baseline of inventory and receivables the firm always carries — should be funded with long-term capital; temporary/seasonal working capital should be funded with short-term sources repaid when the peak recedes. Conservative policy funds some temporary WC with long-term money (safe, low return); aggressive policy funds some permanent WC with short-term money (higher return, rollover risk).
**Say it:** "Fund permanent WC long and temporary WC short — mismatching either way trades liquidity risk against return."

### Q7. When is negative working capital a strength versus a warning sign?
**Answer.** Strength when structural: the firm collects from customers before paying suppliers (supermarkets, Amazon, subscription-prepaid), so stakeholders finance operations and growth generates cash. Warning when it comes from strain — payables ballooning because the firm can't pay, or inventory collapsing because it can't restock. The sign is meaningless without the source.
**Say it:** "Negative WC is a superpower when it's the business model and a red flag when it's a symptom — always trace the source."

### Q8. Explain the trade-off between liquidity and profitability in WC policy.
**Answer.** A fat policy (high cash, inventory, and customer credit; quick supplier payment) maximises liquidity and minimises operational risk but drags return, because low-earning current assets bloat the asset base. A lean policy boosts asset turnover and ROA but raises the risk of stock-outs, lost sales, and a liquidity crunch. The optimum balances the expected cost of illiquidity against the return drag of carrying liquidity — it is neither minimum nor maximum WC.

### Q9. What is EOQ and what does it balance?
**Answer.** Economic Order Quantity, Q* = √(2DS/H), is the order size that minimises total inventory cost by balancing **ordering cost** (rises when you order small and often) against **carrying cost** (rises when you order big and rarely). At the optimum the two are equal. It assumes steady demand and constant costs — a baseline, refined in practice by JIT, safety stock, and quantity discounts.

### Q10. Why do we use COGS for DIO and DPO but revenue for DSO?
**Answer.** Inventory and payables are carried at **cost** — that's what you paid for stock and owe suppliers — so their day-metrics belong on COGS. Receivables are carried at **sale price** — customers owe you the marked-up amount — so DSO belongs on revenue. Mixing bases (e.g., DPO on revenue) distorts the number by the gross-margin factor.

### Q11. How does factoring work and what does it trade?
**Answer.** The firm sells its receivables to a factor for immediate cash at a discount. **Recourse** factoring: the firm keeps the default risk (cheaper). **Non-recourse**: the factor absorbs defaults (dearer). Factoring drives DSO toward zero and unlocks liquidity instantly, at the cost of the factor's fee — a classic liquidity-for-return trade, useful when growth is starving the firm of cash.

### Q12. What does a rising DSO tell an equity research analyst?
**Answer.** It's an early warning. Rising DSO means customers are taking longer to pay — which can signal weakening demand, looser credit to prop up sales, channel stuffing (booking shipments to distributors who can't sell through), or deteriorating collections. Because it shows up in the working-capital line of the cash flow statement, it often flags trouble before revenue or margins visibly crack.
**Say it:** "A DSO creeping up while revenue looks fine is a yellow flag — I'd check whether sales are being pulled forward with easy credit or channel stuffing."

---

## Numerical Problems

### Q13. Compute the cash conversion cycle.
**Given:** Revenue ₹7,300,000; COGS ₹5,110,000; average inventory ₹420,000; average receivables ₹600,000; average payables ₹350,000. Use 365 days.

**Solution.**
- DIO = (420,000 ÷ 5,110,000) × 365 = 0.082192 × 365 = **30.0 days**
- DSO = (600,000 ÷ 7,300,000) × 365 = 0.082192 × 365 = **30.0 days**
- DPO = (350,000 ÷ 5,110,000) × 365 = 0.068493 × 365 = **25.0 days**
- Operating cycle = 30 + 30 = **60 days**
- **CCC = 30 + 30 − 25 = 35 days**

**Check:** WC = inventory + receivables − payables = 420,000 + 600,000 − 350,000 = ₹670,000. Daily COGS = 14,000; daily revenue = 20,000. Rebuild: 30×14,000 + 30×20,000 − 25×14,000 = 420,000 + 600,000 − 350,000 = **₹670,000**. Consistent.

### Q14. Cost of forgoing a cash discount.
**Given:** Terms 3/15 net 60. Compute the simple annualised cost and the effective annual rate.

**Solution.**
- Effective rate for the extra period: d/(100−d) = 3/97 = 0.030928 (over 60 − 15 = 45 days).
- **Simple:** 0.030928 × (365/45) = 0.030928 × 8.1111 = **25.09%**
- **EAR:** (1.030928)^(365/45) − 1 = (1.030928)^8.1111 − 1 = 1.2827 − 1 = **28.27%**

**Decision:** if bank funds cost less than ~25%, take the discount. At a typical 12–14% cost of funds, taking the discount earns an 11–13 point spread.

### Q15. Should the firm take the discount given its borrowing rate?
**Given:** Terms 1/10 net 40; short-term borrowing rate 15%.

**Solution.**
- d/(100−d) = 1/99 = 0.010101 over (40 − 10) = 30 days.
- Simple annualised cost = 0.010101 × (365/30) = 0.010101 × 12.1667 = **12.29%**.

**Decision:** the implied cost of forgoing the discount (12.29%) is **below** the 15% borrowing rate. **Do NOT take the discount** — it's cheaper to keep the cash and pay on day 40. This is the exception that proves the rule: small discount (1%) over a relatively long extra window (30 days) makes trade credit *cheap*.

### Q16. EOQ, order frequency, and total cost.
**Given:** Annual demand 40,000 units; ordering cost ₹200/order; carrying cost ₹10/unit/year.

**Solution.**
- EOQ = √(2 × 40,000 × 200 ÷ 10) = √(16,000,000 ÷ 10) = √1,600,000 = **1,264.9 units**
- Orders/year = 40,000 ÷ 1,264.9 = **31.6 orders**
- Ordering cost = 31.6 × 200 = **₹6,325** (≈ √(2·40000·200·10)/2 check below)
- Carrying cost = (1,264.9 ÷ 2) × 10 = 632.46 × 10 = **₹6,325**
- **Total relevant cost = ₹12,649**

**Check:** at EOQ, ordering = carrying (both ₹6,325). Minimum total cost = √(2·D·S·H) = √(2×40,000×200×10) = √160,000,000 = ₹12,649. Matches.

### Q17. Credit-policy relaxation decision.
**Given:** Current credit sales ₹8,000,000 at net 30 (DSO 30). Contribution margin 25% (variable cost 75%). Proposed: extend to net 50; sales rise ₹1,500,000; DSO on all sales becomes 50; bad debts on new sales 5% (existing 1%, unchanged); required return on receivables investment 18%; base investment on cost; 365 days.

**Solution.**
- **Incremental contribution:** 1,500,000 × 25% = **₹375,000**
- **Incremental bad debts:** 1,500,000 × 5% = **₹75,000**
- **Old receivables investment (at cost):** cost of sales = 8,000,000 × 75% = 6,000,000; (6,000,000/365) × 30 = **₹493,151**
- **New receivables investment:** new sales 9,500,000; cost = 9,500,000 × 75% = 7,125,000; (7,125,000/365) × 50 = **₹976,027**
- **Incremental investment:** 976,027 − 493,151 = **₹482,876**
- **Carrying cost:** 482,876 × 18% = **₹86,918**

| Item | ₹ |
|---|---|
| Incremental contribution | +375,000 |
| Incremental bad debts | −75,000 |
| Incremental carrying cost | −86,918 |
| **Net benefit** | **+213,082** |

**Decision: relax the policy** — net gain ≈ ₹213,082.

### Q18. Cash released by cutting DSO.
**Given:** Annual credit sales ₹36,500,000; current DSO 55 days; target DSO 40 days. 365 days. How much cash is freed, and what's the annual saving at a 12% cost of funds?

**Solution.**
- Daily sales = 36,500,000 ÷ 365 = ₹100,000
- Current receivables = 55 × 100,000 = ₹5,500,000
- Target receivables = 40 × 100,000 = ₹4,000,000
- **Cash released = 5,500,000 − 4,000,000 = ₹1,500,000** (one-time)
- **Annual saving = 1,500,000 × 12% = ₹180,000** every year

### Q19. Change in working capital and its FCF impact.
**Given:** Year 1 — receivables ₹500,000, inventory ₹700,000, payables ₹400,000. Year 2 — receivables ₹640,000, inventory ₹820,000, payables ₹470,000. Compute ΔNWC and state its effect on FCF.

**Solution.**
- NWC₁ = 500,000 + 700,000 − 400,000 = **₹800,000**
- NWC₂ = 640,000 + 820,000 − 470,000 = **₹990,000**
- **ΔNWC = 990,000 − 800,000 = +₹190,000** (an increase)
- **Effect on FCF:** an increase in NWC is a **use of cash**, so FCF is **reduced by ₹190,000**.

**Interpretation:** receivables (+140k) and inventory (+120k) grew faster than payables (+70k); net 190k of cash got locked into working capital and is subtracted in the FCF bridge.

### Q20. Negative working capital and the growth cash effect.
**Given:** DIO 15, DSO 3, DPO 55; annual COGS ₹36,500,000; revenue ₹47,450,000; 365 days. Compute CCC, rupee WC, and the cash effect of 25% growth.

**Solution.**
- **CCC = 15 + 3 − 55 = −37 days**
- Daily COGS = 100,000; daily revenue = 130,000
- Inventory = 15 × 100,000 = 1,500,000; receivables = 3 × 130,000 = 390,000; payables = 55 × 100,000 = 5,500,000
- **Operating WC = 1,500,000 + 390,000 − 5,500,000 = −₹3,610,000**
- Grow sales/COGS 25%: new WC = −3,610,000 × 1.25 = −₹4,512,500
- **ΔWC = −4,512,500 − (−3,610,000) = −₹902,500 → a cash INFLOW of ₹902,500 generated by growth**

**Interpretation:** negative CCC means growth *funds itself*; scaling up releases nearly ₹0.9m of supplier/customer financing.

### Q21. Financing strategy comparison.
**Given:** A firm needs ₹10,000,000 of total working capital, of which ₹6,000,000 is permanent and ₹4,000,000 is seasonal (peaks 4 months a year, zero otherwise — average temporary need ≈ ₹4,000,000 × 4/12 = ₹1,333,333). Long-term funds cost 14%; short-term funds cost 9%. Compare a **conservative** plan (fund all ₹10,000,000 with long-term) versus a **matching** plan (permanent long-term, seasonal short-term on average balance).

**Solution.**
- **Conservative:** 10,000,000 × 14% = **₹1,400,000/year** financing cost. Off-peak, ₹4,000,000 of long-term funds sit idle (safe but wasteful).
- **Matching:** permanent 6,000,000 × 14% = 840,000; seasonal (average) 1,333,333 × 9% = 120,000; total = **₹960,000/year**.
- **Saving from matching ≈ ₹440,000/year**, at the cost of higher rollover risk and less liquidity buffer.

**Takeaway:** matching is cheaper (short rates below long, and you don't pay to carry idle funds off-peak); conservative buys safety at ~₹440k/year.

### Q22. Quick and current ratio interpretation.
**Given:** Cash ₹200,000; marketable securities ₹100,000; receivables ₹500,000; inventory ₹900,000; current liabilities ₹1,000,000. Compute current, quick, and cash ratios and comment.

**Solution.**
- Current assets = 200,000 + 100,000 + 500,000 + 900,000 = ₹1,700,000
- **Current ratio = 1,700,000 ÷ 1,000,000 = 1.70**
- **Quick ratio = (1,700,000 − 900,000) ÷ 1,000,000 = 800,000 ÷ 1,000,000 = 0.80**
- **Cash ratio = (200,000 + 100,000) ÷ 1,000,000 = 0.30**

**Comment:** current ratio of 1.7 looks healthy, but the quick ratio of 0.8 (< 1) reveals heavy dependence on **inventory** for liquidity — over half of current assets are stock. If that inventory is slow-moving or obsolete, the firm is less liquid than the current ratio suggests. The cash ratio of 0.30 shows only 30% of current liabilities could be met from cash immediately — normal for most operating firms, but worth watching if receivables collection slows.
