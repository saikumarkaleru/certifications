# Q&A — Inventory & Cost of Goods Sold

A mixed bank of conceptual and numerical questions for finance interviews (ER, credit, FP&A, IB). Numericals are fully solved and reconcile to the penny.

---

## Conceptual

### Q1. Explain the cost-flow identity and why it matters.
**Answer.** Beginning Inventory + Purchases − Ending Inventory = COGS. Rearranged, COGS = Goods Available for Sale − Ending Inventory. It matters because inventory and COGS are complementary: whatever cost you don't leave on the balance sheet, you expense. So any error or policy choice in valuing ending inventory *simultaneously* mis-states the income statement. Every cost-flow method is just a different way of splitting Goods Available for Sale into these two buckets.

**Interview line:** "Inventory and COGS are two ends of the same pipe — cost you keep on the balance sheet is cost you didn't expense, and vice versa."

### Q2. FIFO vs LIFO vs weighted average in rising prices — rank profit, COGS, tax and ending inventory.
**Answer.**
- Profit & ending inventory: **FIFO > Weighted avg > LIFO**
- COGS & cash tax: **LIFO > Weighted avg > FIFO**

FIFO puts old cheap costs into COGS (low COGS, high profit) and new costs into inventory (rich balance sheet). LIFO does the reverse. The ranking flips if prices are *falling*.

**Interview line:** "In inflation, FIFO flatters the income statement and the balance sheet but costs you cash in tax; LIFO does the opposite."

### Q3. Why does LIFO exist at all?
**Answer.** Real cash tax savings. Higher COGS under LIFO lowers taxable income and the tax bill, retaining cash. The US LIFO conformity rule requires you to also report the lower LIFO profit to shareholders if you claim the tax benefit — so it's an explicit trade of reported earnings for cash. It's a US-GAAP-only option; IFRS (IAS 2) bans it.

### Q4. Is LIFO permitted under IFRS?
**Answer.** No. IAS 2 prohibits LIFO. It is permitted only under US GAAP (ASC 330). This is why cross-border comparison requires converting a US LIFO firm to a FIFO basis using the LIFO reserve.

### Q5. Periodic vs perpetual — what's the difference and when does it matter?
**Answer.** Periodic updates inventory and COGS only at period-end via a physical count; COGS is a residual (BI + Purchases − EI). Perpetual updates continuously, booking a cost-side entry (Dr COGS, Cr Inventory) at every sale, so quantity on hand is always known. Perpetual isolates shrinkage; periodic buries it in COGS. The choice of *system* also affects the *average* method: FIFO gives the same answer either way, but weighted average (periodic) differs from moving average (perpetual).

### Q6. Define NRV and state the lower-of-cost-or-NRV rule.
**Answer.** NRV = estimated selling price − estimated costs to complete − estimated costs to sell. Inventory is carried at the lower of cost and NRV, applied item-by-item (or by similar group), never netted across the whole pool. IFRS and US GAAP (for FIFO/average) both use NRV; US GAAP for LIFO/retail uses lower-of-cost-or-market with a ceiling of NRV and floor of NRV minus normal margin.

### Q7. Can an inventory write-down be reversed?
**Answer.** IFRS (IAS 2): yes, required if NRV recovers, capped at original cost. US GAAP (ASC 330): no, the written-down amount becomes the new cost basis permanently. This means two identical firms can report different future margins purely due to framework.

### Q8. What is a LIFO liquidation and why is it an earnings-quality red flag?
**Answer.** When a LIFO firm sells more than it buys, it dips into old, cheap cost layers. Those ancient costs flow to COGS, artificially inflating gross margin and profit that period. It's unsustainable, low-quality earnings, often triggered by a production cut, strike, or deliberate drawdown to flatter results. Analysts strip it out.

### Q9. Which costs go into inventory and which don't?
**Answer.** In: purchase price net of trade discounts, import duties and non-recoverable taxes, freight-in, and (for manufacturers) direct labour and production overhead absorbed at normal capacity. Out (period expenses): selling and distribution (freight-out), general admin overhead, abnormal spoilage, storage of finished goods, and generally interest (except for qualifying assets that take a long time to produce, like whisky).

**Interview line:** "Costs to *get it ready and in place* are inventoriable; costs to *sell it* are period costs."

### Q10. What's the "inventory profit" problem with FIFO in inflation?
**Answer.** Under FIFO, part of the reported gross profit isn't from operating better — it's from holding cheap old stock while selling at today's higher prices. That "holding gain" isn't repeatable and overstates sustainable margin. LIFO removes it by matching current costs against current revenue, which is why LIFO's income statement is more economically honest in inflation (at the cost of a stale balance sheet).

---

## Numerical

### Q11. Three-method comparison (periodic, rising prices).
No beginning inventory. Purchases: 200 @ ₹20; 200 @ ₹24; 200 @ ₹30. Sold 400 units at ₹40. Opex ₹1,000. Tax 25%.

**Solution.**
Goods available = 600 units, cost = 4,000 + 4,800 + 6,000 = **₹14,800**. Ending inv = 600 − 400 = 200 units. Sales = 400 × 40 = ₹16,000.

- **FIFO COGS** (oldest 400): 200@20 + 200@24 = 4,000 + 4,800 = **₹8,800**; ending inv = 200@30 = ₹6,000. Check 8,800+6,000=14,800 ✓
- **LIFO COGS** (newest 400): 200@30 + 200@24 = 6,000 + 4,800 = **₹10,800**; ending inv = 200@20 = ₹4,000. Check 10,800+4,000=14,800 ✓
- **Weighted avg**: 14,800 ÷ 600 = ₹24.667/unit. COGS = 400 × 24.667 = **₹9,866.67**; ending inv = 200 × 24.667 = ₹4,933.33. Check ✓

| | FIFO | Wtd avg | LIFO |
|---|---:|---:|---:|
| Sales | 16,000 | 16,000 | 16,000 |
| COGS | (8,800) | (9,867) | (10,800) |
| Gross profit | 7,200 | 6,133 | 5,200 |
| Opex | (1,000) | (1,000) | (1,000) |
| Pre-tax | 6,200 | 5,133 | 4,200 |
| Tax 25% | (1,550) | (1,283) | (1,050) |
| **Net income** | **4,650** | **3,850** | **3,150** |
| Ending inv | 6,000 | 4,933 | 4,000 |

LIFO reserve = FIFO inv − LIFO inv = 6,000 − 4,000 = ₹2,000; tax saved by LIFO vs FIFO = 1,550 − 1,050 = ₹500 = 2,000 × 25% ✓.

### Q12. Convert a LIFO company to FIFO.
A US firm reports: LIFO inventory ₹500 (this year), ₹420 (last year); LIFO reserve ₹180 (this year), ₹140 (last year); LIFO COGS ₹2,000; LIFO pre-tax income ₹600; tax 30%. Restate to FIFO.

**Solution.**
- FIFO ending inventory = LIFO inv + LIFO reserve = 500 + 180 = **₹680**.
- FIFO beginning inventory = 420 + 140 = ₹560.
- Change in LIFO reserve = 180 − 140 = ₹40.
- FIFO COGS = LIFO COGS − ΔReserve = 2,000 − 40 = **₹1,960**.
- FIFO pre-tax income = LIFO pre-tax + ΔReserve = 600 + 40 = **₹640**.
- FIFO net income = 640 × (1 − 0.30) = ₹448 (vs LIFO net = 600 × 0.70 = ₹420).
- FIFO retained earnings uplift = full reserve × (1 − tax) = 180 × 0.70 = **₹126** higher than LIFO RE.
- Cumulative extra tax the firm avoided by using LIFO ≈ reserve × tax = 180 × 30% = ₹54.

### Q13. Perpetual FIFO vs moving average.
Beginning: 100 @ ₹8. Buy 100 @ ₹10 (Feb 4). Sell 120 (Feb 10). Buy 80 @ ₹12 (Feb 18). Sell 100 (Feb 25).

**Solution.** Available = 280 units; cost = 800 + 1,000 + 960 = ₹2,760. Sold = 220; ending = 60 units.

**FIFO (perpetual):**
- Feb 10 sell 120: 100@8 + 20@10 = 800 + 200 = ₹1,000. Remaining 80@10.
- Feb 18 buy 80@12 → hold 80@10 + 80@12.
- Feb 25 sell 100: 80@10 + 20@12 = 800 + 240 = ₹1,040. Remaining 60@12 = ₹720.
- COGS = 1,000 + 1,040 = **₹2,040**; ending = **₹720**. Check 2,040+720=2,760 ✓

**Moving average:**
- After Feb 4: 200 units, 1,800 cost, avg 9.00.
- Feb 10 sell 120 @ 9.00 = ₹1,080. Remaining 80 @ 9.00 = 720.
- Feb 18 buy 80@12=960 → 160 units, cost 1,680, avg 10.50.
- Feb 25 sell 100 @ 10.50 = ₹1,050. Remaining 60 @ 10.50 = 630.
- COGS = 1,080 + 1,050 = **₹2,130**; ending = **₹630**. Check 2,130+630=2,760 ✓

FIFO COGS (₹2,040) < moving-average COGS (₹2,130) as expected in rising prices.

### Q14. Lower of cost and NRV, item by item.
Four products, cost under FIFO:

| Product | Cost | Selling price | Cost to sell |
|---|---:|---:|---:|
| P1 | 1,000 | 1,300 | 100 |
| P2 | 1,000 | 950 | 80 |
| P3 | 800 | 900 | 150 |
| P4 | 600 | 700 | 40 |

**Solution.** NRV = price − cost to sell.
- P1 NRV 1,200 vs cost 1,000 → carry 1,000, write-down 0
- P2 NRV 870 vs cost 1,000 → carry 870, write-down 130
- P3 NRV 750 vs cost 800 → carry 750, write-down 50
- P4 NRV 660 vs cost 600 → carry 600, write-down 0

Total write-down = 130 + 50 = **₹180**. New carrying value = (1,000+870+750+600) = ₹3,220 (vs cost 3,400). Entry: **Dr COGS 180 / Cr Inventory 180.** Note P1's ₹200 headroom is *not* used to offset P2/P3 — item-by-item.

### Q15. Three-statement impact of a write-down.
Inventory written down by ₹300; tax rate 25%. Trace all three statements.

**Solution.**
- **Income statement:** COGS +300 → pre-tax income −300 → tax −75 → **net income −225**.
- **Cash flow (indirect):** start net income −225; add back non-cash write-down +300 → **operating cash flow +75** (purely the tax saving; no cash left the firm).
- **Balance sheet:** Inventory −300 (assets). Retained earnings −225; taxes payable/deferred −75. Assets −300 = Equity −225 + Liabilities −75. **Balances ✓.**

### Q16. LIFO liquidation effect.
A LIFO firm holds three layers: 100 @ ₹10 (oldest), 100 @ ₹15, 100 @ ₹20 (newest). Current replacement cost ₹22. It sells 250 units at ₹30 but buys nothing this period. Compute COGS and flag the issue.

**Solution.** Under LIFO, sell newest first: 100@20 + 100@15 + 50@10 = 2,000 + 1,500 + 500 = **₹3,750** COGS. Sales = 250 × 30 = ₹7,500 → gross profit ₹3,750.
If the firm had *replaced* stock (current cost ₹22), COGS would be closer to 250 × 22 = ₹5,500 → gross profit only ₹2,000. The extra ₹1,750 of profit is **LIFO liquidation gain** — it came from consuming cheap old ₹10/₹15 layers, not from operating performance. It's unsustainable and should be stripped out for margin analysis. (Firms disclose LIFO liquidation gains in the footnotes.)

### Q17. Manufacturer COGS build-up.
Direct materials used ₹40,000; direct labour ₹25,000; manufacturing overhead ₹18,000; opening WIP ₹5,000; closing WIP ₹7,000; opening finished goods ₹12,000; closing finished goods ₹9,000. Find COGM and COGS.

**Solution.**
- COGM = DM + DL + MOH + opening WIP − closing WIP = 40,000 + 25,000 + 18,000 + 5,000 − 7,000 = **₹81,000**.
- COGS = opening FG + COGM − closing FG = 12,000 + 81,000 − 9,000 = **₹84,000**.

### Q18. Deflation flips the ranking.
No beginning inventory. Buy 100 @ ₹30, then 100 @ ₹20 (prices *falling*). Sell 100 units. Which method gives higher profit — FIFO or LIFO?

**Solution.** Available = 200 units, ₹5,000. Sold 100, ending 100.
- FIFO COGS = 100@30 = ₹3,000; ending = 100@20 = ₹2,000.
- LIFO COGS = 100@20 = ₹2,000; ending = 100@30 = ₹3,000.
Here **LIFO gives lower COGS and higher profit** — the opposite of the inflation case. Lesson: never memorize "FIFO = high profit"; reason from *which costs hit COGS*. In deflation the oldest costs (FIFO's COGS) are the highest.

### Q19. Effect on inventory turnover of method choice.
Using Q11 data (FIFO vs LIFO), sales ₹16,000, no beginning inventory (use ending inventory as the denominator proxy). Compare COGS/ending-inventory turnover and comment.

**Solution.**
- FIFO: COGS 8,800 ÷ ending inv 6,000 = **1.47×**.
- LIFO: COGS 10,800 ÷ ending inv 4,000 = **2.70×**.
LIFO shows dramatically higher turnover — but it's an *artifact*: LIFO stuffs high current costs into COGS (numerator up) and leaves stale cheap costs in inventory (denominator down). An analyst must restate to FIFO before comparing turnover across firms, or the LIFO firm looks misleadingly efficient.

### Q20. Freight-in vs freight-out.
Purchases ₹50,000; freight-in ₹3,000; freight-out (delivery to customers) ₹2,000; purchase returns ₹1,000; opening inventory ₹8,000; closing inventory ₹6,000. Compute COGS.

**Solution.** Net purchases = 50,000 + 3,000 (freight-in is inventoriable) − 1,000 = ₹52,000. Freight-out is a *selling expense*, NOT in COGS. COGS = opening 8,000 + net purchases 52,000 − closing 6,000 = **₹54,000**. Freight-out ₹2,000 sits below gross profit as an operating expense.

### Q21. IFRS write-down and reversal across two years.
Year 1: inventory cost ₹10,000, NRV ₹8,500 → written down. Year 2: same stock still held, NRV recovers to ₹11,000. Give both entries under IFRS and state the US GAAP difference.

**Solution.**
- Year 1: write-down ₹1,500. **Dr COGS 1,500 / Cr Inventory 1,500.** Carry at ₹8,500.
- Year 2 (IFRS): NRV recovered to 11,000 but reversal is capped at *original cost* ₹10,000. Reversal = 10,000 − 8,500 = ₹1,500. **Dr Inventory 1,500 / Cr COGS 1,500.** Carry at ₹10,000 (not 11,000 — you never write inventory *above* cost).
- **US GAAP:** no reversal permitted. Inventory stays at ₹8,500 (new basis). Year 2 gross profit is ₹1,500 lower than under IFRS for identical economics.

### Q22. Full income + tax comparison with beginning inventory.
Beginning inventory 50 units @ ₹40 = ₹2,000. Purchases: 100 @ ₹44; 100 @ ₹50. Sold 200 units at ₹70. Opex ₹1,500. Tax 30%. Compute net income under FIFO and LIFO.

**Solution.** Available = 250 units; cost = 2,000 + 4,400 + 5,000 = ₹11,400. Sold 200; ending 50. Sales = 200 × 70 = ₹14,000.
- **FIFO COGS** (oldest 200): 50@40 + 100@44 + 50@50 = 2,000 + 4,400 + 2,500 = ₹8,900; ending = 50@50 = ₹2,500. Check 8,900+2,500=11,400 ✓
- **LIFO COGS** (newest 200): 100@50 + 100@44 = 5,000 + 4,400 = ₹9,400; ending = 50@40 = ₹2,000. Check 9,400+2,000=11,400 ✓

| | FIFO | LIFO |
|---|---:|---:|
| Sales | 14,000 | 14,000 |
| COGS | (8,900) | (9,400) |
| Gross profit | 5,100 | 4,600 |
| Opex | (1,500) | (1,500) |
| Pre-tax | 3,600 | 3,100 |
| Tax 30% | (1,080) | (930) |
| **Net income** | **2,520** | **2,170** |
| Ending inv | 2,500 | 2,000 |

LIFO reserve = 2,500 − 2,000 = ₹500; tax saved = 1,080 − 930 = ₹150 = 500 × 30% ✓. FIFO net income is ₹350 higher, exactly ΔReserve × (1 − tax) = 500 × 0.70 = ₹350 ✓.
