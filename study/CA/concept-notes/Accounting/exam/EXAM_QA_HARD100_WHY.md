# Advanced Accounting — HARD Reasoning-First Q&A (Q1–Q100)

*100 of the toughest CA-Intermediate questions — multi-step problems with twists, integrated cross-concept problems, and "analyse / advise / examine validity" case-style questions. Every answer carries a **"Why this way (the reasoning)"** block that explains the principle behind each step (and why the tempting wrong approach fails), so you learn to think, not memorise. Full chapter coverage, ICAI-depth working notes and statements.*

---

## Part C — HARD Reasoning-First Bank (Q1–Q100)

### Q1. Ch: AS 2 Inventory — Cost formula (FIFO vs Weighted Average) meeting NRV (Marks: 8) [Problem]
**Question:** Vega Ltd values inventory of a single product. There was no opening inventory. Movements during the year and the year-end market data are given below. The company is undecided between FIFO and Weighted Average. Compute the value of closing inventory under **both** cost formulas and state, with reasons, the amount at which it must appear in the Balance Sheet.

| Particulars | Units | Rate ₹/unit |
|---|---|---|
| Purchase 1 (Apr) | 100 | 100 |
| Purchase 2 (Jul) | 200 | 110 |
| Purchase 3 (Oct) | 300 | 120 |
| Purchase 4 (Jan) | 200 | 130 |
| Units sold during year | 500 | — |
| Estimated selling price (year-end) | — | 128 |
| Estimated selling/distribution cost | — | 8 |

**Solution:**

**WN-1 — Closing quantity:** 100 + 200 + 300 + 200 = 800 purchased; less 500 sold = **300 units** in stock.

**WN-2 — FIFO cost of closing stock (latest layers remain):** 200 units @ ₹130 = 26,000 + 100 units @ ₹120 = 12,000 → **₹38,000** (₹126.67/unit).

**WN-3 — Weighted-average cost:** Total cost = (100×100)+(200×110)+(300×120)+(200×130) = 10,000+22,000+36,000+26,000 = ₹94,000 for 800 units → ₹117.50/unit. Closing = 300 × ₹117.50 = **₹35,250**.

**WN-4 — Net Realisable Value (NRV):** Selling price ₹128 − selling cost ₹8 = ₹120/unit → 300 × ₹120 = **₹36,000**.

**Statement Showing Value of Closing Inventory (lower of cost and NRV — AS 2 para 5)**

| Basis | Cost (₹) | NRV (₹) | Balance-Sheet value (₹) |
|---|---|---|---|
| FIFO | 38,000 | 36,000 | **36,000** |
| Weighted Average | 35,250 | 36,000 | **35,250** |

**Answer:** Under **FIFO** inventory is carried at **₹36,000** (NRV, since cost ₹38,000 > NRV); under **Weighted Average** at **₹35,250** (cost, since cost < NRV ₹36,000).

**Why this way (the reasoning):** AS 2 measures inventory at the **lower of cost and NRV** — a two-stage test. Stage one assigns a cost using an assumed physical flow (FIFO assumes the oldest units are sold first, so the newest, dearest units survive in stock; weighted average smooths all costs into one rate). The cost formula is only a *cost-assignment convention* — it never overrides the ceiling. Stage two compares that assigned cost with NRV — the actual net cash the units will fetch — and NRV wins whenever it is lower, because inventory is an asset and must never be carried above its recoverable amount (the prudence/no-overstatement principle). Here FIFO loads the closing stock with the ₹130 units, pushing cost above NRV, so it is written down; weighted average dilutes those dear units, so its cost stays below NRV and needs no write-down. The tempting error is to stop at the cost figure once a formula is chosen — but the NRV test is mandatory and independent of the formula.

*(Full-marks tip: examiners reward showing BOTH the cost figure and the separate NRV comparison for each formula; the classic deduction is quoting only the cost under FIFO and forgetting the ₹2,000 write-down, or netting selling cost incorrectly.)*

---

### Q2. Ch: AS 2 Inventory — Item-by-item NRV and write-down of raw materials (Marks: 8) [Problem]
**Question:** Sourabh Ltd holds finished goods and the raw materials used to make them. Determine the Balance-Sheet value of each line, applying AS 2 correctly. Data (all ₹ per relevant unit, totals in ₹):

| Line | Cost | Estimated selling price | Cost to complete & sell | Replacement cost of RM |
|---|---|---|---|---|
| Finished Product X (200 u.) | 200 | 190 | 20 | — |
| Raw Material for X (100 u.) | 100 | — | — | 90 |
| Finished Product Y (150 u.) | 150 | 250 | 30 | — |
| Raw Material for Y (120 u.) | 100 | — | — | 88 |

**Solution:**

**WN-1 — NRV of finished goods:**
- Product X: NRV = 190 − 20 = ₹170 < cost ₹200 → **write down to ₹170**. Loss ₹30/unit.
- Product Y: NRV = 250 − 30 = ₹220 > cost ₹150 → **carry at cost ₹150** (no write-down).

**WN-2 — Raw materials (AS 2 para 24):** Raw materials are written down below cost **only if the finished product in which they will be incorporated is expected to be sold at or below cost**; and then replacement cost is the best measure of NRV.
- RM for X: finished Product X is loss-making (NRV ₹170 < cost ₹200) → RM **written down to replacement cost ₹90** (from ₹100).
- RM for Y: finished Product Y is profitable (NRV ₹220 > cost ₹150) → RM **held at cost ₹100**, even though replacement cost ₹88 is lower.

**Statement Showing Inventory Valuation**

| Line | Units | Rate to carry (₹) | Value (₹) |
|---|---|---|---|
| Finished Product X | 200 | 170 | 34,000 |
| Raw Material for X | 100 | 90 | 9,000 |
| Finished Product Y | 150 | 150 | 22,500 |
| Raw Material for Y | 120 | 100 | 12,000 |
| **Total** | | | **77,500** |

**Answer:** Total closing inventory = **₹77,500** (X ₹34,000; RM-X ₹9,000; Y ₹22,500; RM-Y ₹12,000).

**Why this way (the reasoning):** The lower-of-cost-and-NRV test is applied **item by item**, never by grossing profitable and loss lines together — offsetting Y's unrealised gain against X's loss would hide a real loss and overstate assets, defeating prudence. The subtle part is raw materials: a fall in a material's replacement price does **not** automatically justify a write-down. Materials are inputs; their recoverable value is realised *through* the finished product. If that finished product will still sell at or above its total cost, the materials will be fully recovered in the sale, so writing them down would create a fictitious loss now and an inflated profit later. Only when the finished product itself is loss-making does the material lose value, and replacement cost then approximates the material's NRV. Hence RM-Y stays at ₹100 despite replacement cost ₹88, while RM-X drops to ₹90 — the two identical-looking materials are treated oppositely purely because of the profitability of *their* end product.

*(Full-marks tip: the marks sit in the AS 2 para 24 logic — state the "sold at or below cost" condition explicitly and justify why RM-Y is NOT written down. The common trap is mechanically writing every material down to replacement cost.)*

---

### Q3. Ch: AS 2 Inventory — Costs includible in / excludible from cost of inventory (Marks: 6) [Problem]
**Question:** Compute the value of closing stock of 1,000 units of Amrit Ltd from the data below, clearly showing which items enter cost and which are excluded and why.

| Particulars | Amount (₹) |
|---|---|
| Purchase price of materials (list) | 8,00,000 |
| Trade discount on above | 40,000 |
| GST on purchase (input credit fully available) | 96,000 |
| Freight inward | 25,000 |
| Import duty (non-refundable) | 35,000 |
| Abnormal wastage of material | 30,000 |
| Storage cost (not necessary for further production) | 18,000 |
| Fixed production overhead (normal capacity basis) | 60,000 |
| Selling & distribution overhead | 22,000 |
| Interest on working-capital loan | 15,000 |

The above relate to 1,000 units produced and still in stock.

**Solution:**

**WN-1 — Items INCLUDED in cost:** Purchase price 8,00,000 − trade discount 40,000 = 7,60,000; + freight inward 25,000; + import duty (non-refundable) 35,000; + fixed production overhead 60,000 = **₹8,80,000**.

**WN-2 — Items EXCLUDED (with reason):**
- GST ₹96,000 — refundable input credit, recoverable from tax authority, not a cost (para 7).
- Abnormal wastage ₹30,000 — abnormal amounts excluded (para 13).
- Storage ₹18,000 — storage not necessary before a further production stage is excluded (para 13).
- Selling & distribution ₹22,000 — excluded; not incurred to bring inventory to present location/condition.
- Interest ₹15,000 — borrowing/finance cost, excluded (para 12, except qualifying assets under AS 16).

**Statement Showing Cost of Closing Inventory**

| Element | ₹ |
|---|---|
| Net purchase price (after trade discount) | 7,60,000 |
| Freight inward | 25,000 |
| Non-refundable import duty | 35,000 |
| Fixed production overhead (normal capacity) | 60,000 |
| **Cost of inventory (1,000 units)** | **8,80,000** |

**Answer:** Closing inventory = **₹8,80,000** (₹880 per unit).

**Why this way (the reasoning):** AS 2 defines cost as everything incurred to bring inventory to its **present location and condition** — a "getting it ready to sell/use" test. Purchase cost is net of trade discount (a genuine price reduction, not income) but includes non-refundable duties (a real, unrecoverable outflow). GST input credit is excluded because it is recoverable — including it would inflate the asset with money the tax department owes back. Abnormal wastage and unnecessary storage fail the test because they add no value and represent inefficiency, so charging them to inventory would defer a loss that has already occurred. Selling costs come *after* the inventory is ready, and interest is a financing decision, not a production cost — both are period costs. The discipline is to ask of each line: "did this expenditure move the goods closer to a sellable/usable state?" — only then does it belong in inventory.

*(Full-marks tip: state a reason for each exclusion citing the "present location and condition" principle; markers deduct for including GST or omitting the trade-discount netting.)*

---

### Q4. Ch: AS 2 Inventory — Fixed overhead absorption at normal capacity (Marks: 8) [Problem]
**Question:** Neelkanth Ltd budgets fixed production overhead of ₹18,00,000 for the year. Normal capacity is 30,000 units. In the year, due to a market slump, only **20,000 units** were actually produced; 5,000 units remain in closing stock. Variable production cost is ₹120 per unit and there were no work-in-progress or opening stock. Actual fixed overhead incurred equalled budget. Compute the value of closing stock and show the treatment of any unabsorbed overhead. Would your answer change if production had been 33,000 units?

**Solution:**

**WN-1 — Fixed overhead per unit at NORMAL capacity (para 9):** ₹18,00,000 ÷ 30,000 = **₹60/unit**. This rate is fixed and is *not* recalculated on actual low volume.

**WN-2 — Overhead absorbed into 20,000 units produced:** 20,000 × ₹60 = ₹12,00,000. **Unabsorbed overhead = 18,00,000 − 12,00,000 = ₹6,00,000** → charged to P&L as an expense of the period (NOT capitalised into stock).

**WN-3 — Cost per unit of production:** Variable ₹120 + fixed absorbed ₹60 = **₹180/unit**.

**Statement Showing Value of Closing Stock (5,000 units)**

| Element | ₹/unit | ₹ (5,000 units) |
|---|---|---|
| Variable production cost | 120 | 6,00,000 |
| Fixed overhead (normal-capacity rate) | 60 | 3,00,000 |
| **Closing stock value** | **180** | **9,00,000** |

**If production = 33,000 units (above normal):** the rate is reduced to actual = ₹18,00,000 ÷ 33,000 = ₹54.55/unit, so that fixed overhead is not carried at more than cost. Fixed cost per unit at ₹54.55 is used; total fixed overhead is fully absorbed (no over-absorption credited to stock).

**Answer:** Closing stock = **₹9,00,000**; unabsorbed fixed overhead of **₹6,00,000** is expensed in the P&L. In a high-volume year the per-unit rate falls to **₹54.55** (actual production used).

**Why this way (the reasoning):** Fixed overhead is absorbed on **normal capacity**, not actual, precisely so that idle-capacity cost is not smuggled into the balance sheet. If we spread the whole ₹18,00,000 over the depressed 20,000 units, each unit would carry ₹90 of fixed cost — the extra ₹30 being purely the cost of *not producing*. Capitalising that into 5,000 unsold units would defer a loss caused by the slump and overstate the asset; AS 2 instead forces the ₹6,00,000 shortfall straight into current-year P&L. The rule is asymmetric on purpose: in a **high** output year the rate is dropped to actual so that inventory is never valued **above** actual cost (you cannot "over-absorb" into an asset). So low volume → fixed rate held, excess expensed; high volume → rate lowered. The guiding idea is that inventory should reflect the cost of *efficient* normal production, with abnormal idle cost recognised immediately.

*(Full-marks tip: the marks are for (i) using 30,000 not 20,000 as the denominator, (ii) routing ₹6,00,000 to P&L, and (iii) the reverse treatment above normal capacity. A frequent error is dividing by actual 20,000 and capitalising the idle cost.)*

---

### Q5. Ch: AS 7 Construction Contracts — Percentage completion turning into an expected loss (Marks: 10) [Problem]
**Question:** Bridgeworks Ltd has a fixed-price contract of ₹100 lakh. It uses the cost-proportion method to measure stage of completion. Data for the first two years:

| Particulars | Year 1 | Year 2 (cumulative) |
|---|---|---|
| Contract price (₹ lakh) | 100 | 100 |
| Costs incurred to date (₹ lakh) | 30 | 66 |
| Estimated further costs to complete (₹ lakh) | 50 | 44 |

Compute the revenue, expense and profit/loss to be recognised in **each** year's Statement of Profit and Loss, and any provision required.

**Solution:**

**WN-1 — Year 1:** Total estimated cost = 30 + 50 = ₹80 lakh. Expected profit = 100 − 80 = ₹20 lakh. Stage of completion = 30 ÷ 80 = **37.5%**.
- Revenue = 37.5% × 100 = **₹37.5 lakh**
- Expense = 37.5% × 80 = **₹30 lakh**
- Profit Year 1 = **₹7.5 lakh**

**WN-2 — Year 2 (contract now loss-making):** Total estimated cost = 66 + 44 = ₹110 lakh > contract price 100 → **foreseeable total loss = 100 − 110 = ₹10 lakh**. Under AS 7 para 35, the *entire* expected loss is recognised immediately, irrespective of stage of completion.
- Stage of completion = 66 ÷ 110 = **60%**
- Cumulative revenue = 60% × 100 = **₹60 lakh** → Year-2 revenue = 60 − 37.5 = **₹22.5 lakh**
- Required cumulative profit = **(10) lakh** (the whole foreseeable loss). Already recognised in Year 1 = +7.5 → **Year-2 P&L = −10 − 7.5 = −₹17.5 lakh (loss)**

**WN-3 — Reconciliation / provision:** Cumulative expense to be shown = cumulative revenue − cumulative result = 60 − (−10) = ₹70 lakh. Cost actually incurred to date = ₹66 lakh. Difference ₹4 lakh = **provision for expected loss on remaining work**, recognised now.

**Statement Showing Recognition**

| Particulars | Year 1 (₹ lakh) | Year 2 (₹ lakh) |
|---|---|---|
| Revenue recognised | 37.5 | 22.5 |
| Expense (incl. loss provision) | 30.0 | 40.0 |
| **Profit / (Loss)** | **7.5** | **(17.5)** |
| Cumulative result | 7.5 | (10.0) |

**Answer:** Year 1 profit **₹7.5 lakh**; Year 2 loss **₹17.5 lakh**; cumulative recognised result equals the full foreseeable loss of **₹10 lakh**, with a ₹4 lakh provision on unexecuted work.

**Why this way (the reasoning):** The percentage-of-completion method matches revenue and cost to work done — as long as the contract is profitable. But AS 7 overrides matching the moment the contract becomes loss-making: para 35 requires the **whole expected loss to be booked at once**, not spread over the remaining stage. Prudence demands you never defer a loss you can already foresee. So in Year 2 we cannot simply take 60% of a notional profit; we must first ask "is the contract in overall loss?" — yes, ₹10 lakh — and force cumulative results down to that figure. Because Year 1 optimistically recognised ₹7.5 lakh profit (a fair estimate then), Year 2 must claw that back *and* book the loss, hence the large −₹17.5 lakh. The ₹4 lakh provision represents the loss attaching to work not yet performed — recognised today even though the cost has not yet been incurred. The tempting wrong answer is to recognise only 60% of the ₹10 loss (= ₹6) — that violates para 35 by deferring foreseeable loss.

*(Full-marks tip: examiners specifically test whether you recognise the FULL ₹10 lakh loss immediately and reverse Year 1 profit; the classic deduction is prorating the loss by 60%. Show the cumulative-result reconciliation to prove it.)*

---

### Q6. Ch: AS 7 Construction Contracts — Stage of completion excluding unused materials (Marks: 8) [Problem]
**Question:** Rockfort Constructions Ltd measures completion by the cost-input method. For a ₹250 lakh contract, the "costs incurred to date" figure of ₹120 lakh includes ₹20 lakh of standard materials delivered to site **but not yet consumed**, and ₹8 lakh of an advance paid to a sub-contractor for work **not yet performed**. Estimated further costs to complete are ₹110 lakh. Compute the correct stage of completion and the profit to be recognised, and state the treatment of the excluded items.

**Solution:**

**WN-1 — Adjust costs incurred for completion measurement (para 24):** Costs that do not reflect work performed must be excluded from the numerator.
- Costs to date as booked = ₹120 lakh
- Less: materials at site not yet used = ₹20 lakh
- Less: sub-contractor advance (work not done) = ₹8 lakh
- **Costs reflecting work performed = ₹92 lakh**

**WN-2 — Total estimated cost of contract:** Costs to date (all, ₹120) + further costs (₹110) = ₹230 lakh. Expected profit = 250 − 230 = ₹20 lakh. *(Note: total estimated cost uses full ₹120; only the completion % numerator is adjusted.)*

**WN-3 — Stage of completion:** 92 ÷ 230 = **40%**.

**Statement Showing Recognition (to date)**

| Particulars | ₹ lakh |
|---|---|
| Revenue = 40% × 250 | 100 |
| Cost of work performed | 92 |
| **Profit recognised** | **8** |

Treatment of excluded items: the ₹20 lakh unused materials are carried as **contract work-in-progress / inventory**; the ₹8 lakh advance is shown as an **advance to sub-contractor (asset)** — both to be picked up as costs when consumed/performed.

**Answer:** Stage of completion = **40%**; revenue **₹100 lakh**, cost **₹92 lakh**, profit recognised = **₹8 lakh**.

**Why this way (the reasoning):** The cost-input method assumes that costs incurred are a proxy for *work done*. That assumption breaks for costs relating to **future** activity — materials sitting in a stack not yet built in, or an advance for work not yet performed. Including them would overstate the percentage complete and pull forward profit that has not been earned. AS 7 para 24 therefore strips such costs out of the numerator, while they remain assets (WIP/advance) to be recognised when the underlying work actually happens. A neat subtlety many miss: these excluded items still form part of *total estimated cost* (denominator and overall profit), because they will genuinely be consumed on the contract — they are merely mistimed, not fictitious. So the fix is surgical: reduce only the "work-performed" numerator, keep total cost intact.

*(Full-marks tip: markers look for the numerator adjustment AND retaining the items in total cost; a common error is deducting the ₹28 lakh from both numerator and total, or expensing the advance immediately.)*

---

### Q7. Ch: AS 7 Construction Contracts — Uncertain outcome: cost-recovery method (Marks: 8) [Problem/Case]
**Question:** Zenith Infra Ltd is executing a ₹400 lakh contract in a politically unstable region. At the reporting date, ₹150 lakh of costs have been incurred, of which the company is confident of recovering only ₹130 lakh from the customer because a dispute has arisen over the enforceability of a variation and total costs cannot yet be reliably estimated. Advise how much revenue and cost to recognise, and contrast this with the position once the outcome becomes reliably estimable (assume then: total estimated cost ₹360 lakh, costs to date ₹150 lakh).

**Answer:**

**Principle (AS 7 paras 31–32):** When the outcome of a contract **cannot be estimated reliably**, no profit is recognised. Revenue is recognised **only to the extent of contract costs incurred that it is probable will be recovered**, and contract costs are expensed as incurred. This is the "cost-recovery" approach — it prevents booking a profit that may never materialise, while also avoiding an artificial loss on costs that will be recovered.

**Application — current (outcome not reliably estimable):**

| Particulars | ₹ lakh |
|---|---|
| Costs incurred to date | 150 |
| Revenue = recoverable portion of costs | 130 |
| Cost recognised as expense | 150 |
| **Result (loss on non-recoverable costs)** | **(20)** |

The ₹20 lakh of costs unlikely to be recovered is charged immediately (it is effectively a foreseeable loss on that portion); no profit is taken.

**Application — once outcome becomes reliably estimable:** Stage of completion = 150 ÷ 360 = 41.67%. Total expected profit = 400 − 360 = ₹40 lakh.
- Revenue = 41.67% × 400 = **₹166.67 lakh**
- Cost = 41.67% × 360 = **₹150 lakh**
- Profit = **₹16.67 lakh**

**Conclusion/Advice:** While uncertainty persists, recognise revenue of ₹130 lakh against cost ₹150 lakh (net ₹20 lakh charge) and **no profit**. Once total costs and recoverability become reliably measurable, switch to the percentage-of-completion method and recognise ₹16.67 lakh profit — the change being applied prospectively as a change in estimate.

**Why this way (the reasoning):** AS 7 splits contract accounting into two regimes hinged on **reliability of estimate**. Percentage-of-completion presumes you can reliably forecast total revenue and cost; if you cannot — genuine uncertainty over enforceability or ultimate cost — recognising a stage-based profit would be guessing, so the standard falls back to a conservative floor: recover your costs through revenue only to the extent recovery is probable, and take no profit. This is not a loss-avoidance dodge; costs judged unrecoverable are still expensed at once (the ₹20 lakh), so prudence is preserved on both sides. When the fog clears, you do not restate the past — you move forward on percentage-of-completion, because the improved ability to estimate is a change in *estimate*, applied prospectively. The wrong instinct is either to book stage-profit through the uncertainty (overstatement) or to expense all ₹150 lakh with zero revenue (understating recoverable value).

*(Full-marks tip: name the "cost-recovery method" explicitly, state the "probable recovery" test, and show the prospective switch. Deductions come from recognising profit during uncertainty or from writing off all costs.)*

---

### Q8. Ch: AS 7 Construction Contracts — Change in estimate and combining/segmenting (Marks: 6) [Case/Application]
**Question:** Examine the validity of the accounting treatment adopted by Prime Builders Ltd in each situation and advise the correct approach under AS 7:
(a) A ₹500 lakh contract's total estimated cost was revised from ₹450 lakh to ₹480 lakh in Year 3. The company restated Years 1 and 2 profits to reflect the new cost.
(b) A single contract covers a factory building and a separate office block, each separately negotiated and the customer could accept either; the company accounts for both as one contract.
(c) An incentive payment of ₹15 lakh for early completion is included in revenue although, at the reporting date, the project is behind schedule and the incentive is not probable.

**Answer:**

**(a) Change in estimate — treatment invalid.** AS 7 treats a revision in estimated contract costs as a **change in accounting estimate** (para 21, read with AS 5). Its effect is recognised **prospectively** — in the period of change and future periods — by adjusting the current-period revenue/cost via the cumulative catch-up in the percentage-of-completion computation. Restating prior years is **wrong**; prior figures were correct on the information then available. *Advice:* reverse the restatement; absorb the effect of the ₹30 lakh higher cost through the Year-3 stage-of-completion recalculation.

**(b) Segmenting a contract — treatment invalid.** Under para 8, when a contract covers assets that were **separately negotiated**, the contractor and customer could accept/reject **each asset separately**, and costs/revenues of each are identifiable, each asset is treated as a **separate contract**. All three conditions are met, so the building and office block must be **segmented** and profit measured on each independently. *Advice:* split the contract into two.

**(c) Incentive in revenue — treatment invalid.** Incentive payments are included in contract revenue only when the contract is **sufficiently advanced that it is probable the performance standard will be met** and the amount can be reliably measured (para 16). The project being behind schedule means the incentive is **not probable** → it must be **excluded** from revenue. *Advice:* remove ₹15 lakh until conditions are met.

**Conclusion:** All three treatments are invalid; correct them as advised above.

**Why this way (the reasoning):** Each limb tests a distinct AS 7 discipline. (a) The percentage-of-completion method is inherently estimate-driven; when better information arrives you update *going forward* — reopening settled years would imply the earlier estimates were errors, which they were not, and would destroy the comparability and finality of reported results (this is the AS 5 estimate-vs-error boundary). (b) The segmenting rule protects against averaging a profitable job with a loss-making one under a single "contract" wrapper — if the market treats the two assets as separately biddable, so must the accounts, so that each asset's true result surfaces. (c) Variations, claims and incentives are *contingent* revenue; AS 7 admits them only when **probable and measurable**, mirroring the realisation principle — you do not bank a bonus you are currently on track to miss. The unifying logic is faithful representation of what has actually been earned and reliably estimated at the reporting date.

*(Full-marks tip: for each limb quote the specific test — "prospective", the three segmenting conditions, and "probable + measurable" — then conclude invalid. The deduction is asserting "wrong" without citing the condition that is breached.)*

---

### Q9. Ch: AS 9 Revenue Recognition — Timing of sale of goods under special conditions (Marks: 8) [Case/Application]
**Question:** For each transaction of Meridian Traders Ltd, examine when (and whether) revenue should be recognised at the year ended 31 March 2026 under AS 9, giving reasons:
(a) Goods worth ₹12 lakh dispatched to a consignee on 20 March 2026; the consignee had sold ₹5 lakh of them by year-end.
(b) A machine sold for ₹30 lakh on "sale-on-approval" terms on 25 March 2026; the approval period of 30 days had not expired and the buyer had not confirmed acceptance by year-end.
(c) Goods worth ₹8 lakh sold and delivered, but the sale contract requires the seller to install and test the equipment, a significant part of the contract, which is incomplete at year-end.
(d) A retail sale of ₹2 lakh made on 28 March 2026 under the company's "money-back within 15 days, no questions asked" policy; past experience shows 4% of such sales are returned.

**Answer:**

**Governing principle:** AS 9 recognises revenue from sale of goods when (i) the seller has **transferred to the buyer the property in the goods / significant risks and rewards of ownership**, and (ii) **no significant uncertainty** exists regarding the amount and collectability of consideration.

**(a) Consignment — ₹5 lakh only.** In a consignment the consignee holds goods as agent; risks and rewards pass only on the consignee's onward sale to a third party. Recognise revenue of **₹5 lakh** (goods actually sold by the consignee); the ₹7 lakh unsold is closing stock with the consignee — **no revenue**.

**(b) Sale on approval — nil.** Risks and rewards do not pass until the buyer signifies approval or the approval period lapses. As neither has occurred, **no revenue** is recognised; the machine remains the seller's inventory.

**(c) Sale with significant installation — nil (defer).** Where installation/inspection is a **significant** part of the contract, revenue is recognised only on completion. As installation is incomplete, **defer the ₹8 lakh** until installed and tested. *(If installation were incidental, revenue would be recognised on delivery.)*

**(d) Retail sale with return right — ₹2 lakh, with provision.** Risks and rewards pass on delivery and the amount is measurable; recognise full **₹2 lakh** revenue and separately **provide for expected returns (4% = ₹8,000)** and reverse the related margin. The right of return is a measurable uncertainty handled by provision, not by deferral.

**Conclusion:** Recognise (a) ₹5 lakh, (b) nil, (c) nil, (d) ₹2 lakh (with ₹8,000 returns provision).

**Why this way (the reasoning):** AS 9 pivots on **transfer of significant risks and rewards**, not the mechanical moment of dispatch or invoicing — because revenue represents value the seller has genuinely earned and is reasonably sure of keeping. Consignment and sale-on-approval both fail this: the seller still bears the risk of the goods (they can come back), so recognising revenue would anticipate a sale that may never close. Installation that is *significant* means the earning process is unfinished — the buyer is paying for a working, installed asset, so revenue waits for performance; but if installation is trivial, it does not hold up recognition. The return-policy case is different in kind: the sale *has* happened and risks *have* passed; the only issue is a **measurable** estimate of returns, which prudence handles by a provision rather than by refusing to recognise the sale. The craft is distinguishing "risks not yet transferred" (defer entirely) from "risks transferred but outcome estimable" (recognise and provide).

*(Full-marks tip: state the risks-and-rewards + no-significant-uncertainty test once, then apply per limb; the classic error is deferring the return-sale entirely instead of recognising-and-providing, or recognising full ₹12 lakh on consignment.)*

---

### Q10. Ch: AS 9 Revenue Recognition — Multiple-element / composite arrangement (Marks: 8) [Problem]
**Question:** Technovision Ltd sells a "bundle" for ₹90,000: a projector plus a 3-year on-site maintenance service. Sold separately, the projector's stand-alone price is ₹80,000 and 3-year maintenance is ₹20,000. During the year (bundle sold on 1 April 2025) the projector was delivered immediately. Show how the ₹90,000 revenue should be allocated and recognised in the year ended 31 March 2026, and the balance carried forward.

**Solution:**

**WN-1 — Allocate bundle price on relative stand-alone values:** Total stand-alone = 80,000 + 20,000 = ₹1,00,000.
- Projector = 90,000 × (80,000 / 1,00,000) = **₹72,000**
- Maintenance = 90,000 × (20,000 / 1,00,000) = **₹18,000**

**WN-2 — Recognition pattern:**
- Projector (goods): risks/rewards pass on delivery 1 Apr 2025 → recognise **₹72,000** fully in Year 1.
- Maintenance (service over 3 years): recognise on a time/proportionate basis → per year = 18,000 ÷ 3 = ₹6,000. Year 1 = **₹6,000**; deferred = ₹12,000.

**Statement Showing Revenue Recognition (Year 1)**

| Element | Allocated price (₹) | Recognised Year 1 (₹) | Deferred (₹) |
|---|---|---|---|
| Projector (on delivery) | 72,000 | 72,000 | — |
| Maintenance (1 of 3 yrs) | 18,000 | 6,000 | 12,000 |
| **Total** | **90,000** | **78,000** | **12,000** |

**Answer:** Recognise **₹78,000** in Year 1 (₹72,000 projector + ₹6,000 service); carry forward **₹12,000** as deferred revenue (unearned service income) to Years 2 and 3 (₹6,000 each).

**Why this way (the reasoning):** A single price hides two **separately identifiable performance obligations** with different earning patterns — the projector is earned instantly on delivery, the maintenance is earned continuously as the service is rendered. Recognising the whole ₹90,000 up front would front-load unearned service income and overstate Year-1 profit; recognising nothing until maintenance ends would defer genuinely earned product revenue. AS 9's substance-over-form principle requires you to **unbundle** and match each element to its own recognition trigger. Allocation uses **relative stand-alone selling prices** so the ₹10,000 bundle discount is shared fairly across both components rather than dumped on one. The service portion follows the proportionate-completion method (here time-based, as the service accrues evenly), leaving the unrecognised part as a liability — deferred revenue — reflecting the obligation still owed to the customer.

*(Full-marks tip: examiners reward the relative-stand-alone-price allocation AND spreading the service over 3 years; deductions arise from recognising all ₹90,000 immediately or allocating the discount arbitrarily.)*

---

### Q11. Ch: AS 9 Revenue Recognition — Interest, royalty, dividend and services (Marks: 6) [Problem]
**Question:** Determine the revenue Sunrise Ltd may recognise for the year ended 31 March 2026 from the following, stating the basis under AS 9:

| Item | Details | Amount (₹) |
|---|---|---|
| (a) Interest on a debenture investment | ₹10,00,000 @ 9% p.a., held whole year | ? |
| (b) Royalty | Licensee's sales ₹40,00,000; royalty @ 5%; agreement effective full year | ? |
| (c) Dividend | Investee declared dividend on 10 April 2026 | 60,000 |
| (d) Service contract (advisory) | Fee ₹5,00,000; 60% of the work performed by year-end; outcome reliably estimable | ? |
| (e) Interest on a loan to a party | ₹4,00,000 @ 10%; borrower in serious financial difficulty, recovery doubtful | 40,000 |

**Solution:**

**WN — Basis of recognition (AS 9 para 13):** Interest — time-proportion basis; Royalty — accrual per the agreement's substance; Dividend — when the **right to receive** is established (declaration); Services — proportionate completion (outcome reliable).

| Item | Basis | Revenue Year 1 (₹) |
|---|---|---|
| (a) Interest | 10,00,000 × 9% (time basis, full year) | **90,000** |
| (b) Royalty | 40,00,000 × 5% (accrual per agreement) | **2,00,000** |
| (c) Dividend | Declared 10 Apr 2026 → right arises *after* year-end | **Nil (Year 1)** |
| (d) Service | 5,00,000 × 60% (proportionate completion) | **3,00,000** |
| (e) Doubtful interest | Significant uncertainty of collection → postpone | **Nil** |

**Answer:** Recognise **₹90,000** (interest) + **₹2,00,000** (royalty) + **₹3,00,000** (service) = **₹5,90,000**. Dividend of ₹60,000 falls in Year 2 (declared after year-end); the ₹40,000 doubtful interest is **not** recognised until collection is reasonably certain.

**Why this way (the reasoning):** AS 9 recognises "other" revenues on bases that reflect *when the enterprise's right to the reward crystallises and collection is reasonably certain*. Interest accrues purely with the passage of time (the lender earns it continuously), so a time-proportion basis is used. Royalties accrue as the licensee exploits the right, captured through the agreed formula. Dividends are different — the investor has **no enforceable right** until the payer *declares*; an April declaration is a post-balance-sheet event, not Year-1 income, so recognising it would anticipate income not yet legally due. The advisory service uses proportionate completion because the benefit is delivered progressively and the outcome is reliably estimable. Item (e) invokes the second pillar of AS 9 — **no significant uncertainty of collectability**; when recovery is doubtful *at the point of sale/accrual*, recognition is postponed altogether (not recognised-then-provided), because the very certainty that revenue underlies is absent.

*(Full-marks tip: the dividend-declaration timing and the doubtful-interest postponement are the two trap-marks; state the "right to receive established" and "collection certainty" tests explicitly.)*

---

### Q12. Ch: AS 9 Revenue Recognition — Uncertainty of collection vs measurement, price escalation (Marks: 5) [Case/Application]
**Question:** Comment on the validity of the following revenue recognitions by Crystal Ltd for the year ended 31 March 2026, applying AS 9:
(a) The company sold goods for ₹20 lakh to a customer whose financial position was sound at the sale date but who was declared insolvent two months *after* the year-end. Crystal did not recognise the ₹20 lakh, treating collection as uncertain.
(b) A contract permits a **price escalation** claim; at year-end the claim of ₹3 lakh is under negotiation and its acceptance and amount are uncertain. Crystal recognised the ₹3 lakh as revenue.

**Answer:**

**Principle:** AS 9 recognises revenue when risks and rewards pass and there is **no significant uncertainty as to measurability or collectability at the time of the transaction**. Where uncertainty over *collection* arises **only later**, revenue is still recognised at sale, and the later default is a **separate bad-debt expense**, not a reversal of revenue.

**(a) Non-recognition invalid.** At the date of sale the customer was sound — collection was reasonably certain then, so revenue of ₹20 lakh should have been **recognised in full**. The subsequent insolvency is a fresh event; it does not retract the earned revenue but is dealt with as a **provision for doubtful debts / bad-debt write-off** (and, being a post-balance-sheet condition arising from events *after* the year-end, assessed under AS 4). Suppressing the revenue conflates a collection problem with a recognition problem.

**(b) Recognition invalid.** A price-escalation claim is recognised only when it is **not unreasonable to expect ultimate collection and the amount can be measured reliably**. Here acceptance and amount are uncertain and under negotiation → the ₹3 lakh fails the measurability/collectability test and must **not** be recognised. It is a contingent gain, disclosed at most.

**Conclusion:** (a) recognise ₹20 lakh revenue and separately provide for the debt; (b) exclude the ₹3 lakh claim until it is reliably measurable and acceptance is probable.

**Why this way (the reasoning):** The two cases sit on opposite sides of the same test and expose a common confusion between *recognition uncertainty* and *subsequent collection failure*. Revenue recognition asks a question **at the transaction date**: were the risks/rewards transferred and was consideration reasonably certain and measurable *then*? In (a) the answer was yes, so the revenue is real and earned; a later insolvency is an ordinary credit loss, and netting it against revenue would distort both the sales figure and the picture of bad debts. In (b), the uncertainty exists *at* recognition — the claim may be rejected and its quantum is unknown — so booking it would import an unrealised, unmeasurable gain, breaching the "no significant uncertainty" gate and prudence. The discipline: measurement/collectability uncertainty *existing at the transaction* blocks recognition; uncertainty *emerging afterwards* is an expense, never a revenue reversal.

*(Full-marks tip: the examiner wants the crisp distinction — recognise-then-provide in (a) vs postpone in (b). Deductions come from reversing revenue in (a) or recognising the contingent claim in (b).)*

---

### Q13. Ch: AS 10 PP&E — Componentisation and replacement of a component (Marks: 10) [Problem]
**Question:** Skyline Airways Ltd acquires an aircraft on 1 April 2020 for ₹1,00,00,000. The purchase can be split into identifiable components with differing useful lives:

| Component | Cost (₹) | Useful life (years) |
|---|---|---|
| Airframe | 60,00,000 | 20 |
| Engines | 30,00,000 | 10 |
| Cabin fittings & interiors | 10,00,000 | 5 |

Depreciation is straight-line, no residual value. On 1 April 2025 the entire cabin fittings are replaced with new fittings costing ₹12,00,000 (new life 5 years). Compute (i) annual depreciation for years 1–5, (ii) the accounting on replacement, and (iii) depreciation for year 6.

**Solution:**

**WN-1 — Component-wise annual depreciation (years 1–5):**
- Airframe: 60,00,000 ÷ 20 = ₹3,00,000
- Engines: 30,00,000 ÷ 10 = ₹3,00,000
- Cabin fittings: 10,00,000 ÷ 5 = ₹2,00,000
- **Total per year = ₹8,00,000**

**WN-2 — Carrying amount of cabin fittings on 1 Apr 2025:** Cost 10,00,000 − (5 × 2,00,000) = **₹0** (fully depreciated over its 5-year life).

**WN-3 — Replacement accounting (AS 10 paras 13–14):** Derecognise the old component (carrying amount ₹0 → no loss/gain) and **capitalise** the new fittings ₹12,00,000 as a new component (it meets recognition criteria — future benefits, reliably measured).

**WN-4 — Depreciation, Year 6 (2025-26):**
- Airframe 3,00,000 + Engines 3,00,000 + New cabin fittings 12,00,000 ÷ 5 = 2,40,000
- **Total Year-6 depreciation = ₹8,40,000**

**Statement Showing Carrying Amount at 31 March 2026**

| Component | Cost (₹) | Acc. dep (₹) | Carrying (₹) |
|---|---|---|---|
| Airframe (6 yrs) | 60,00,000 | 18,00,000 | 42,00,000 |
| Engines (6 yrs) | 30,00,000 | 18,00,000 | 12,00,000 |
| Cabin fittings (new, 1 yr) | 12,00,000 | 2,40,000 | 9,60,000 |
| **Total** | **1,02,00,000** | **38,40,000** | **63,60,000** |

**Answer:** Annual depreciation years 1–5 = **₹8,00,000**; on replacement the old fittings (carrying ₹0) are derecognised with no loss and the new ₹12,00,000 capitalised; Year-6 depreciation = **₹8,40,000**; carrying amount at 31 Mar 2026 = **₹63,60,000**.

**Why this way (the reasoning):** AS 10 requires each **significant part** of an asset with a *different useful life or pattern of benefit* to be depreciated **separately** (component approach). A single 20-year rate on the whole aircraft would grossly under-depreciate the engines and fittings, which wear out far sooner, and would leave phantom value on the books when they are scrapped. Componentisation makes the depreciation reflect the *actual* consumption of each part. It also makes replacement clean: when the fittings are swapped, you **derecognise** the old component's carrying amount (here ₹0, so no loss) and **capitalise** the replacement as a fresh component — you do *not* expense the ₹12,00,000 as mere "repairs," because it delivers new future benefits over 5 years. The old repair-vs-capitalise dilemma dissolves once each part is tracked separately: the cost of the replacement part is capitalised and the replaced part is removed, avoiding the double-counting that would occur if you simply added the new cost while still carrying the old.

*(Full-marks tip: marks are for separate rates per component, derecognising the old part (state carrying = 0, no loss), capitalising the new part, and the revised total. The classic error is expensing the ₹12,00,000 or continuing to depreciate the removed fittings.)*

---

### Q14. Ch: AS 10 PP&E — Revaluation model: surplus, deficit and reversal (Marks: 8) [Problem]
**Question:** Granite Ltd adopts the revaluation model for a plot of land bought on 1 April 2022 for ₹100 lakh. Fair values determined by valuers: 31 Mar 2023 → ₹140 lakh; 31 Mar 2024 → ₹90 lakh; 31 Mar 2025 → ₹115 lakh. Show the accounting treatment of each revaluation, identifying amounts routed through the Revaluation Surplus (in reserves / OCI) versus the Statement of Profit and Loss.

**Solution:**

**WN-1 — 31 Mar 2023 (100 → 140): increase ₹40 lakh.** Carrying goes up ₹40 lakh; as it is the first revaluation, the whole **₹40 lakh is credited to Revaluation Surplus** (reserve). Carrying = ₹140 lakh.

**WN-2 — 31 Mar 2024 (140 → 90): decrease ₹50 lakh.** A revaluation *decrease* is first debited to the Revaluation Surplus **to the extent of the existing surplus on that asset** (₹40 lakh), the balance charged to P&L.
- Debit Revaluation Surplus ₹40 lakh (surplus now nil)
- Debit **P&L ₹10 lakh** (revaluation loss)
- Carrying = ₹90 lakh

**WN-3 — 31 Mar 2025 (90 → 115): increase ₹25 lakh.** A revaluation *increase* is credited to P&L **to the extent it reverses a previous decrease charged to P&L** for that asset (₹10 lakh), the balance to Revaluation Surplus.
- Credit **P&L ₹10 lakh** (reversal of prior loss)
- Credit Revaluation Surplus ₹15 lakh
- Carrying = ₹115 lakh

**Statement Showing Revaluation Effects (₹ lakh)**

| Date | Carrying before | Carrying after | To Reval. Surplus | To P&L |
|---|---|---|---|---|
| 31-Mar-23 | 100 | 140 | +40 | — |
| 31-Mar-24 | 140 | 90 | −40 | −10 |
| 31-Mar-25 | 90 | 115 | +15 | +10 |

**Answer:** Cumulative Revaluation Surplus at 31 Mar 2025 = ₹15 lakh; net P&L impact over the period = nil (₹10 lakh loss in 2024 reversed by ₹10 lakh gain in 2025); carrying amount = **₹115 lakh**.

**Why this way (the reasoning):** Revaluation accounting is deliberately **asymmetric and symmetric at once**, governed by a "same-asset memory" rule. An initial gain is unrealised, so it bypasses profit and sits in a Revaluation Surplus — recognising it as profit would let a company inflate earnings by revaluing assets it has not sold (prudence). But a *loss* is recognised more readily: it first eats into any surplus previously created on that same asset (a genuine reversal of an earlier unrealised gain), and only the excess hits P&L as a real impairment-type charge. On a later recovery the mirror applies: the increase is credited to P&L **only up to** the loss previously charged there — you are giving back to profit exactly what you earlier took from it — and any surplus beyond the original cost level returns to the reserve. This asset-by-asset tracking prevents a gain on one asset masking a loss on another and stops double-counting. The frequent mistake is dumping the entire ₹50 lakh 2024 fall into P&L (ignoring the ₹40 lakh surplus available to absorb it) or sending the whole 2025 gain to the reserve (ignoring the ₹10 lakh P&L reversal owed).

*(Full-marks tip: examiners specifically test the "to the extent of prior surplus/prior loss" splits at each of the second and third revaluations; losing those two splits loses most of the marks.)*

---

### Q15. Ch: AS 10 PP&E — Decommissioning liability in cost of an asset (Marks: 8) [Problem]
**Question:** Deepsea Oil Ltd installs an offshore rig on 1 April 2025 at a construction cost of ₹500 lakh. Law obliges the company to dismantle and restore the site at the end of the rig's 10-year life; the present estimate of that future cost is ₹100 lakh. The appropriate discount rate is 8%. (PV factor of ₹1 at 8% for 10 years = 0.4632.) Compute (i) the initial cost of the rig and its Year-1 depreciation, (ii) the Year-1 finance cost on the provision, and state (iii) how a later upward revision of the estimate is treated.

**Solution:**

**WN-1 — Present value of decommissioning obligation:** 100 × 0.4632 = **₹46.32 lakh**. This is recognised now as a provision (AS 29) and added to the asset's cost (AS 10 para 16(c)).

**WN-2 — Initial cost of the rig:** Construction cost 500 + PV of decommissioning 46.32 = **₹546.32 lakh**.

**WN-3 — Year-1 depreciation (SLM over 10 years):** 546.32 ÷ 10 = **₹54.632 lakh**.

**WN-4 — Year-1 finance cost (unwinding of discount):** Opening provision 46.32 × 8% = **₹3.71 lakh**, charged to P&L as a finance cost; provision at year-end = 46.32 + 3.71 = ₹50.03 lakh.

**Statement Showing Year-1 Charges (₹ lakh)**

| Particulars | ₹ lakh |
|---|---|
| Cost of rig (capitalised) | 546.32 |
| Depreciation for Year 1 | 54.632 |
| Finance cost (unwinding of provision) | 3.71 |
| Closing decommissioning provision | 50.03 |

**(iii) Later upward revision of estimate:** A change in the estimated decommissioning cost (or discount rate) is a **change in estimate**. The change in the *present value* of the liability is **added to (or deducted from) the carrying amount of the asset** prospectively and depreciated over the remaining life (it is not routed straight to P&L, save for the excess if the asset's carrying amount would fall below zero).

**Answer:** Initial cost of rig = **₹546.32 lakh**; Year-1 depreciation = **₹54.632 lakh**; Year-1 finance cost = **₹3.71 lakh**; a subsequent estimate revision adjusts the asset's carrying amount prospectively.

**Why this way (the reasoning):** AS 10 defines the cost of an asset to include the **initial estimate of dismantling and site-restoration costs** the entity is *obliged* to incur as a consequence of installing it. The logic: that future outflow is an unavoidable cost of *having* the rig, so it belongs in the rig's cost and should be consumed (depreciated) over the same life that generates the benefits — matching the full economic cost against the revenue the rig earns. Because the outflow is 10 years away, it is measured at **present value**; recognising the undiscounted ₹100 lakh would overstate both the asset and the liability today. As time passes, the discount **unwinds** — the provision grows toward ₹100 lakh — and that growth is a **finance cost** (the time-value of money on the liability), kept separate from depreciation so users see the financing effect distinctly. Revisions to the estimate are changes in estimate, so they flow into the asset prospectively rather than restating the past, preserving the matching of cost to remaining benefits. The error to avoid is expensing the decommissioning cost only when finally paid (mismatching a 10-year obligation into one year) or capitalising the undiscounted amount.

*(Full-marks tip: the marks are (i) PV not undiscounted, (ii) adding PV to asset cost, (iii) depreciating the grossed-up cost, and (iv) the separate finance-cost unwinding. Deductions come from forgetting the unwinding or the prospective treatment of revisions.)*

---

### Q16. Ch: AS 10 PP&E — Directly attributable costs and exchange of assets (Marks: 6) [Problem]
**Question:** Compute the cost at which the new machine of Pioneer Ltd should be recognised, and separately state the amount to be expensed. Also state the cost of the plant acquired in Part B.

**Part A — New machine purchased:**
| Particulars | Amount (₹) |
|---|---|
| Invoice price | 20,00,000 |
| GST (input credit available) | 3,60,000 |
| Trade discount | 1,00,000 |
| Freight and insurance in transit | 50,000 |
| Installation and site preparation | 70,000 |
| Initial operating loss before machine reached planned performance | 40,000 |
| Cost of staff training to operate machine | 30,000 |
| Administration & general overhead | 25,000 |

**Part B — Exchange:** Pioneer gives up an old machine (carrying amount ₹2,00,000, fair value ₹2,60,000) plus ₹40,000 cash for a plant. The exchange has commercial substance and fair values are reliable.

**Solution — Part A:**

**WN-1 — Includible directly attributable costs:** Invoice 20,00,000 − trade discount 1,00,000 = 19,00,000; + freight & insurance 50,000; + installation & site preparation 70,000 = **₹20,20,000**.

**WN-2 — Excluded (expensed) items with reason:** GST 3,60,000 (recoverable credit); initial operating loss 40,000 (not needed to bring asset to working condition — a post-ready cost); staff training 30,000 (para 19 — training is not a cost of the asset); admin/general overhead 25,000 (not directly attributable). **Total expensed = ₹95,000** (excluding recoverable GST).

**Statement Showing Cost of Machine (Part A)**

| Element | ₹ |
|---|---|
| Invoice price net of trade discount | 19,00,000 |
| Freight & insurance | 50,000 |
| Installation & site preparation | 70,000 |
| **Cost of machine** | **20,20,000** |

**Solution — Part B (exchange with commercial substance, AS 10 para 24):** Cost = **fair value of asset given up** = 2,60,000 + cash paid 40,000 = **₹3,00,000**. Gain on disposal of old machine = FV 2,60,000 − carrying 2,00,000 = ₹60,000 to P&L.

**Answer:** Part A — machine capitalised at **₹20,20,000**, ₹95,000 expensed (GST recoverable). Part B — plant recognised at **₹3,00,000**, with ₹60,000 disposal gain.

**Why this way (the reasoning):** The cost of PP&E is purchase price **plus only those costs directly attributable to bringing the asset to the location and condition necessary to operate as management intends** — a strict "necessary to get it working" filter. Freight, installation and site preparation pass; training, initial operating losses and general admin fail because the asset is *already capable* of working without them (training equips people, not the machine; early losses arise after readiness; admin is a period cost). Capitalising them would inflate the asset and defer expenses that are really current-period costs — para 19 of AS 10 lists these very exclusions. For the exchange, AS 10 measures the acquired asset at the **fair value of what is given up** when the swap has commercial substance and fair value is reliable — because an exchange is, in substance, a sale of the old asset (crystallising its ₹60,000 gain) followed by a purchase; using carrying amount would suppress that real gain. Only where commercial substance or reliable fair value is absent do you fall back to carrying amount.

*(Full-marks tip: the training cost, initial operating loss and GST are the trap items — exclude them with reasons; in Part B use fair value of asset GIVEN UP and recognise the disposal gain. Deductions for capitalising training or measuring the plant at ₹2,40,000.)*

---

### Q17. Ch: AS 10 PP&E — Revaluation: frequency, depreciation and transfer of surplus (Marks: 5) [Case/Application]
**Question:** Examine the validity of the following, applying AS 10, and advise the correct treatment:
(a) Everest Ltd revalued only its most valuable building while carrying the other buildings in the same class at historical cost.
(b) After revaluing a machine upward, the company continued to charge depreciation on the *original* cost rather than the revalued amount, arguing the surplus is unrealised.
(c) The company revalued its factory buildings once in 2018 and has not reviewed the fair value since (2026), though prices have moved significantly.
(d) On the revalued machine, the company wishes to transfer part of the revaluation surplus to retained earnings each year.

**Answer:**

**(a) Invalid — selective revaluation not permitted.** If an item is revalued, the **entire class** of PP&E to which it belongs must be revalued (para 32), to prevent cherry-picking assets with gains and reporting a mixture of costs and values. *Advice:* revalue all buildings in the class.

**(b) Invalid — depreciate the revalued amount.** After revaluation, depreciation is charged on the **revalued carrying amount** over remaining useful life; charging it on original cost understates the expense and overstates profit. *Advice:* base depreciation on the revalued figure.

**(c) Invalid — revaluations must be kept current.** Revaluations must be made with **sufficient regularity** that the carrying amount does not differ materially from fair value at the reporting date (para 31). An eight-year gap with significant price movement breaches this. *Advice:* obtain a fresh valuation.

**(d) Valid (optional).** An enterprise **may** transfer the **difference between depreciation on the revalued amount and depreciation on original cost** from the Revaluation Surplus to retained earnings each year (para 39A/40) — this is a permitted realisation of the surplus as the asset is used, made directly through reserves, **not through P&L**. *Advice:* the transfer is allowed but must not pass through the Statement of Profit and Loss.

**Conclusion:** (a), (b), (c) require correction; (d) is a permissible reserve movement.

**Why this way (the reasoning):** Revaluation is allowed but ring-fenced by rules that protect comparability and prudence. **Whole-class** revaluation (a) stops management from revaluing only the assets that have risen, which would present an inconsistent, flattering mix. **Depreciating the revalued amount** (b) follows from the basic idea that depreciation measures consumption of the asset's *current* carrying value — once you write the asset up, the higher value is what is being used up, so the charge must rise; keeping it on old cost would let the write-up boost the asset without any matching expense. **Regular revaluation** (c) is essential because a stale valuation is neither cost nor fair value — it is meaningless; the "sufficient regularity" test keeps the number faithful. The **surplus-to-retained-earnings transfer** (d) recognises that the revaluation gain becomes *realised* gradually as the asset is depreciated; moving the extra depreciation portion out of the surplus keeps retained earnings distributable-correct — but routing it through P&L would double-count income (the gain was never a profit), so it moves *directly* between reserves.

*(Full-marks tip: for (d) specify it is the extra-depreciation portion and that it bypasses P&L — the most common error is claiming the transfer must go through profit or denying it altogether; for (b) and (c) cite "revalued amount" and "sufficient regularity".)*

### Q18. Ch: AS 4 — Events Occurring After the Balance Sheet Date (Marks: 8) [Case/Application]
**Question:** Sunrise Ltd's financial year ended on 31 March 2026. The financial statements were approved by the Board on 15 June 2026. Examine, with reasons, the treatment of each of the following in the financial statements for 2025-26:

| # | Event (all occurred between 1 Apr 2026 and 15 Jun 2026) |
|---|----------------------------------------------------------|
| a | A major debtor owing ₹40,00,000 as on 31.3.2026 was declared insolvent on 20.4.2026; only ₹10,00,000 is expected to be recovered. |
| b | Inventory costing ₹25,00,000 (held on 31.3.2026) was destroyed by an uninsured fire on 10.5.2026. |
| c | The Board, on 5.6.2026, proposed an equity dividend of ₹50,00,000 for FY 2025-26. |
| d | A customer's suit pending on 31.3.2026 (provision carried ₹8,00,000) was settled on 30.4.2026 for ₹15,00,000. |
| e | On 12.5.2026 the company publicly announced a restructuring plan to close a division, cost ₹60,00,000. |

**Answer:**
Governing principle — AS 4 distinguishes **adjusting events** (those providing *further evidence of conditions that existed at the balance sheet date*) from **non-adjusting events** (those reflecting conditions that *arose after* the date). Only adjusting events change the amounts in the statements; material non-adjusting events are disclosed in the report of the approving authority.

- **(a) Debtor insolvency — ADJUSTING.** The debt existed on 31.3.2026; insolvency on 20.4.2026 only confirms the *recoverability condition already present*. Write down the debtor by ₹30,00,000 (40 − 10) through P&L.
- **(b) Fire destroying inventory — NON-ADJUSTING.** The inventory existed and was in good condition on 31.3.2026; the fire on 10.5.2026 is a *new condition arising after* the date. No adjustment; disclose the ₹25,00,000 loss (its nature and estimate) if material to users' decisions, and consider the **going concern** impact.
- **(c) Proposed dividend — NON-ADJUSTING, NOT PROVIDED.** Post-amendment (Companies (AS) Rules), a dividend proposed *after* the balance sheet date does **not** meet the definition of a present obligation on 31.3.2026. It is **not recognised as a liability**; it is **disclosed in the notes**.
- **(d) Litigation settled for ₹15,00,000 — ADJUSTING.** The obligating event (the suit) existed on 31.3.2026; the settlement confirms the amount. Increase the provision by ₹7,00,000 (15 − 8) through P&L.
- **(e) Restructuring announced 12.5.2026 — NON-ADJUSTING.** No obligation existed on 31.3.2026 (announcement/plan crystallised later). No provision; disclose nature and financial effect if material.

**Conclusion:** Adjust (a) and (d); disclose (b), (c) and (e).

**Why this way (the reasoning):** The whole standard turns on one test — *did the condition exist on the balance sheet date?* If yes, later information is merely better evidence of a value that was already uncertain on that date, so the figure must be corrected (that is why insolvency and the suit are adjusted). If the condition is genuinely new, adjusting would distort the true-and-fair view of the *year that ended*, so it is only disclosed. The proposed-dividend trap catches most students: pre-amendment it was provided; the amended AS 4 recognises there is no obligation until the members approve it, so it fails the "present obligation" gate and is only a note. Confusing "material" with "adjusting" is the other common error — materiality decides *disclosure*, not *recognition*.

*(Full-marks tip: the examiner rewards the explicit "condition-existed-on-31.3" reasoning for each item and the correct amount (₹30,00,000 and ₹7,00,000). Marks are lost for providing the proposed dividend as a liability, or for adjusting the fire loss.)*

---

### Q19. Ch: AS 5 — Prior Period Items, Change in Estimate vs Policy, Ordinary vs Extraordinary (Marks: 6) [Case/Application]
**Question:** Classify each item below under AS 5 (prior period item / change in accounting estimate / change in accounting policy / extraordinary item / ordinary activity) and state its treatment in the statement of profit and loss of Meridian Ltd for FY 2025-26:

| # | Situation |
|---|-----------|
| 1 | A sales invoice of ₹6,00,000 pertaining to March 2025 was, by oversight, not recorded and is now booked. |
| 2 | Provision for doubtful debts changed from 2% to 5% of debtors following a fresh recovery review. |
| 3 | The company switched inventory valuation from FIFO to weighted average cost. |
| 4 | An earthquake destroyed a factory; loss ₹80,00,000. |
| 5 | Profit of ₹12,00,000 on routine sale of an old delivery van. |

**Answer:**
- **(1) Prior period item.** It is an income *omitted through error* relating to a prior period, arising from oversight — squarely a prior period item. Recognise the ₹6,00,000 in the current P&L but **disclose it separately** so that current-year performance is not misread.
- **(2) Change in accounting estimate.** Doubtful-debt percentages are *estimates* revised with new information, not a change of principle. Apply **prospectively**; the incremental charge hits current P&L. No restatement of the past.
- **(3) Change in accounting policy.** FIFO → weighted average is a change in the *measurement basis*. Permissible only if required by statute/standard or if it gives a **more appropriate presentation**. Disclose the **amount of the effect** on current results (and note if not ascertainable).
- **(4) Extraordinary item.** An earthquake is *not related to ordinary activities* and is not expected to recur. Disclose the ₹80,00,000 loss **separately on the face** of the P&L so ordinary performance is clear.
- **(5) Ordinary activity item.** Sale of a used van is incidental to ordinary operations; the ₹12,00,000 gain is an **ordinary item**, disclosed separately by size/nature but **not** as extraordinary.

**Why this way (the reasoning):** AS 5 exists to protect the *comparability and predictive value* of reported profit. A prior period item and an extraordinary item are both shown separately, but for opposite reasons — the former because it does not belong to *this* year, the latter because it will not recur. The estimate-vs-policy distinction is the examiner's favourite trap: an estimate change is a refinement of judgement (prospective, no restatement), whereas a policy change alters the *recognition/measurement principle* itself and demands disclosure of its quantified effect. Calling the estimate revision a "policy change" (or restating prior years) is the classic error; so is dressing up an ordinary asset-sale gain as "extraordinary."

*(Full-marks tip: state the *category* AND the *treatment* (prospective/separate disclosure) for each — half marks are lost when only the label is given without saying prospective vs separate-line.)*

---

### Q20. Ch: AS 11 — Foreign Exchange: Monetary vs Non-Monetary Translation (Marks: 10) [Problem]
**Question:** Zenith Ltd (reporting in ₹) has the following foreign-currency items at 31 March 2026. The closing exchange rate is ₹75/USD. Determine the amount at which each item appears in the Balance Sheet and the net exchange difference to be routed through the Statement of Profit and Loss.

| # | Item | Amount (USD) | Recorded at rate (₹) | Nature |
|---|------|-------------|----------------------|--------|
| 1 | Sundry creditor (raw material), unpaid | 60,000 | 73.00 (15.2.2026) | Monetary |
| 2 | Foreign-currency term loan (general purpose) | 2,00,000 | 72.00 (1.4.2025) | Monetary |
| 3 | Export debtors, unrealised | 50,000 | 74.00 (avg) | Monetary |
| 4 | Imported machinery, fully paid | 80,000 | 73.50 (1.6.2025) | Non-monetary (at cost) |
| 5 | Investment in foreign subsidiary shares | 30,000 | 72.00 | Non-monetary (at cost) |
| 6 | Advance paid to supplier for machinery | 10,000 | 73.00 | Non-monetary (advance for goods) |

**Solution:**

**WN-1 — Classify and apply the rule.** Under AS 11: at each balance sheet date, **monetary items are retranslated at the closing rate**; **non-monetary items carried at historical cost stay at the transaction-date rate** (not retranslated).

**WN-2 — Exchange difference on monetary items (retranslate to ₹75):**

| Item | USD | Old ₹ value | New ₹ value (@75) | Exchange diff |
|------|-----|-------------|-------------------|---------------|
| Creditor | 60,000 | 43,80,000 | 45,00,000 | (1,20,000) loss |
| Term loan | 2,00,000 | 1,44,00,000 | 1,50,00,000 | (6,00,000) loss |
| Debtors | 50,000 | 37,00,000 | 37,50,000 | 50,000 gain |
| **Net to P&L** | | | | **(6,70,000) loss** |

**WN-3 — Non-monetary items: NOT retranslated.**
- Machinery = 80,000 × 73.50 = **₹58,80,000** (carry at cost; depreciate on this).
- Investment = 30,000 × 72.00 = **₹21,60,000**.
- Advance for machinery = 10,000 × 73.00 = **₹7,30,000** (an advance for goods gives no right to fixed cash → non-monetary → frozen at transaction rate).

**Statement of Balance Sheet carrying amounts & P&L impact**

| Item | Carrying amount (₹) | Basis |
|------|--------------------|-------|
| Creditor | 45,00,000 | Closing rate |
| Term loan | 1,50,00,000 | Closing rate |
| Debtors | 37,50,000 | Closing rate |
| Machinery | 58,80,000 | Transaction rate (frozen) |
| Investment | 21,60,000 | Transaction rate (frozen) |
| Advance | 7,30,000 | Transaction rate (frozen) |
| **Net exchange loss to P&L** | **6,70,000** | Monetary items only |

**Answer:** Net exchange **loss of ₹6,70,000** is charged to the Statement of Profit and Loss; monetary items are carried at ₹75/USD while machinery (₹58,80,000), investment (₹21,60,000) and the advance (₹7,30,000) remain at their historical rates.

**Why this way (the reasoning):** The monetary/non-monetary split is the beating heart of AS 11. A *monetary* item is a fixed-rupee-count of foreign currency you will pay or receive — as the rate moves, the number of rupees you must part with (or will get) genuinely changes, so the gain/loss is real and belongs in P&L now. A *non-monetary* item (a machine, an investment, an advance for goods) is already *consumed into* an asset; you are not going to settle it in cash, so its rupee cost was locked in the day you recognised it — retranslating it would invent a phantom gain/loss. The three traps here are (i) treating the imported machine as monetary because it was "in foreign currency," (ii) revaluing the cost-carried investment, and (iii) revaluing the advance — an advance for goods carries no right to receive money, so it is non-monetary.

*(Full-marks tip: the examiner specifically checks that machinery, investment and the advance are left un-restated and that only the ₹6,70,000 net figure hits P&L; students routinely lose 3-4 marks by retranslating non-monetary items.)*

---

### Q21. Ch: AS 11 — Forward Exchange Contract (Premium Amortisation + Spot Revaluation) (Marks: 8) [Problem]
**Question:** On 1 February 2026 Orion Ltd owes USD 1,00,000 to a supplier, payable on 30 June 2026. On the same day it enters a **forward contract to buy USD 1,00,000 at ₹77**, to hedge the payable (not for trading/speculation). Spot rate on 1.2.2026 was ₹75. On 31 March 2026 (year end) the spot rate is ₹75.60. Show the amounts to be recognised in the Statement of Profit and Loss for FY 2025-26.

**Solution:**

**WN-1 — Split the forward into its two AS 11 components.**
AS 11 (paras 36-39) requires a forward contract *not* held for trading to be accounted in two parts:
(a) the **premium/discount** = (forward rate − spot rate at inception) — amortised over the life of the contract; and
(b) the **exchange difference** = movement in *spot* rates on the contract amount — recognised in P&L in the period of change.

**WN-2 — Premium amortisation.**
Premium = (77.00 − 75.00) × 1,00,000 = ₹2,00,000, over the contract life of **5 months** (1 Feb → 30 Jun).
Amortised for FY 2025-26 (Feb + Mar = 2 months) = 2,00,000 × 2/5 = **₹80,000** (expense).

**WN-3 — Exchange difference (spot movement) on the contract.**
= (Closing spot 75.60 − Inception spot 75.00) × 1,00,000 = ₹0.60 × 1,00,000 = **₹60,000** (expense).
(The underlying creditor is simultaneously restated from ₹75 to ₹75.60, a ₹60,000 loss, which this contract gain economically offsets — but AS 11 records the contract's spot movement in P&L as above.)

**Statement of P&L impact for FY 2025-26**

| Component | ₹ | Nature |
|-----------|-----|--------|
| Premium amortised (2 of 5 months) | 80,000 | Expense |
| Exchange difference on spot movement | 60,000 | Expense |
| **Total charged to P&L** | **1,40,000** | |

**Answer:** ₹1,40,000 is charged to the Statement of Profit and Loss for 2025-26 — ₹80,000 premium amortisation and ₹60,000 spot-rate exchange difference. The remaining premium of ₹1,20,000 is carried forward and amortised over April–June 2026.

**Why this way (the reasoning):** A forward contract taken to hedge a known payable does two distinct economic things, and AS 11 insists you separate them. The **premium** (₹2 over spot) is essentially the *pre-agreed cost of certainty* — you willingly pay more than spot to lock the rate; because that cost is earned by the passage of time over the contract, it is spread on a time basis, not dumped in one period. The **spot revaluation** captures actual currency movement and is recognised as it happens, mirroring the restatement of the hedged creditor so that the two largely cancel — which is the point of a hedge. The classic error is to book the whole ₹2,00,000 premium at once, or to value the contract at the *forward* rate at year-end; AS 11 (for non-trading forwards) deliberately uses spot movement plus straight-line premium, precisely so the hedge relationship shows through.

*(Full-marks tip: show the premium (forward−spot at inception) and the spot difference as *separate* lines with the 2/5 time fraction; a single lumped figure or use of a year-end forward rate loses half the marks.)*

---

### Q22. Ch: AS 12 — Government Grants (Recognition, Presentation, Refund) (Marks: 8) [Problem]
**Question:** Comment on and give accounting treatment for the following, applying AS 12, for Vantage Ltd (year ended 31.3.2026):

| # | Situation |
|---|-----------|
| a | Received a grant of ₹40,00,000 towards a plant costing ₹2,00,00,000 (useful life 10 years, SLM). Show both permitted presentation methods for Year 1. |
| b | Received ₹15,00,000 as promoter's contribution (nature-of-promoters' capital, no repayment, not linked to any specific asset). |
| c | A grant of ₹20,00,000 received earlier (for a plant, credited to deferred income, of which ₹4,00,000 already recognised) becomes **refundable** in FY 2025-26 due to breach of conditions. |

**Solution:**

**WN-1 — (a) Grant related to a depreciable asset — two methods:**
- *Method I (deduction from cost):* Asset = 2,00,00,000 − 40,00,000 = ₹1,60,00,000; annual depreciation = 1,60,00,000 / 10 = **₹16,00,000**.
- *Method II (deferred income):* Asset stays at ₹2,00,00,000; depreciation = ₹20,00,000; grant of ₹40,00,000 credited to P&L over 10 years = **₹4,00,000 p.a.**; net charge = 20,00,000 − 4,00,000 = **₹16,00,000** (same net effect).

**WN-2 — (b) Promoters' contribution:** A grant in the nature of promoters' contribution, with no repayment expected and **not related to any specific asset**, is treated as **capital reserve** — credit ₹15,00,000 to Capital Reserve (not to P&L).

**WN-3 — (c) Refundable grant (deferred-income method):** On becoming refundable, first adjust against any *unamortised deferred grant balance*, and charge the excess immediately to P&L.
- Unamortised deferred income = 20,00,000 − 4,00,000 = ₹16,00,000.
- Refund ₹20,00,000 → set off ₹16,00,000 against deferred income; balance **₹4,00,000 charged to P&L** as an expense (extraordinary item).

**Answer:** (a) Net charge ₹16,00,000 under either method; (b) ₹15,00,000 to Capital Reserve; (c) ₹16,00,000 adjusted against deferred income and ₹4,00,000 charged to the Statement of Profit and Loss.

**Why this way (the reasoning):** AS 12 rests on the **matching principle** — a grant is not free money to be taken to income at once; it must be recognised over the *periods that bear the cost it is meant to compensate*. For an asset-linked grant, that "cost" is depreciation, which is why both methods spread the benefit over the 10-year life and arrive at the identical net charge — the choice is only about *presentation*, not profit. Promoters' contribution is different in substance: it is *owners' money injected*, not a subsidy against a cost, so it belongs in reserves, never in P&L. On refund, AS 12 treats it as a *reversal of a benefit previously granted*: you unwind what remains unamortised and expense any shortfall immediately, because the earlier income recognition is now shown to have been unwarranted. Taking the whole grant to income in Year 1, or crediting promoters' contribution to P&L, are the standard mistakes.

*(Full-marks tip: showing that both presentation methods give the *same ₹16,00,000 net charge* is what earns the concept marks; for the refund, the set-off-then-expense sequence must be explicit.)*

---

### Q23. Ch: AS 16 — Borrowing Costs: Eligible Amount with Specific + General Borrowings (Marks: 10) [Problem]
**Question:** Apex Ltd is constructing a qualifying factory building during FY 2025-26. Determine the borrowing cost eligible for capitalisation.

| Particulars | Details |
|-------------|---------|
| Specific loan for the building | ₹60,00,000 @ 10% p.a., drawn 1.4.2025 |
| Income on temporary investment of idle specific-loan funds | ₹1,50,000 |
| General borrowing – Loan A | ₹80,00,000 @ 12% p.a. (whole year) |
| General borrowing – Loan B | ₹1,20,00,000 @ 11% p.a. (whole year) |
| Expenditure on building: 1.4.2025 | ₹60,00,000 |
| 1.7.2025 | ₹40,00,000 |
| 1.10.2025 | ₹50,00,000 |
| 1.1.2026 | ₹30,00,000 |

**Solution:**

**WN-1 — Capitalisation rate for general borrowings (weighted average):**
= (80,00,000 × 12% + 1,20,00,000 × 11%) / (80,00,000 + 1,20,00,000)
= (9,60,000 + 13,20,000) / 2,00,00,000 = 22,80,000 / 2,00,00,000 = **11.4%**.

**WN-2 — Weighted-average accumulated expenditure on the asset:**

| Date | Expenditure (₹) | Months in year | Weighted (₹) |
|------|-----------------|----------------|--------------|
| 1.4.2025 | 60,00,000 | 12/12 | 60,00,000 |
| 1.7.2025 | 40,00,000 | 9/12 | 30,00,000 |
| 1.10.2025 | 50,00,000 | 6/12 | 25,00,000 |
| 1.1.2026 | 30,00,000 | 3/12 | 7,50,000 |
| **Total** | **1,80,00,000** | | **1,22,50,000** |

**WN-3 — Split funding between specific and general borrowings:**
- Funded by specific loan (weighted) = ₹60,00,000 (loan drawn 1.4.2025, full year).
- Funded by general borrowings (weighted) = 1,22,50,000 − 60,00,000 = **₹62,50,000**.

**WN-4 — Eligible borrowing cost:**

| Source | Computation | ₹ |
|--------|-------------|-----|
| Specific loan | 60,00,000 × 10% = 6,00,000 **less** investment income 1,50,000 | 4,50,000 |
| General borrowings | 62,50,000 × 11.4% | 7,12,500 |
| **Total to capitalise** | | **11,62,500** |

(Check: general cost ₹7,12,500 does not exceed actual general borrowing cost of ₹22,80,000 — so no ceiling restriction.)

**Answer:** Borrowing cost eligible for capitalisation = **₹11,62,500** (₹4,50,000 specific, net of income + ₹7,12,500 general).

**Why this way (the reasoning):** AS 16 capitalises only borrowing cost that would have been *avoided* had the asset not been built — the "but for" logic. Funds specifically borrowed for the asset are traced directly, and any income earned by parking idle specific funds is *netted off*, because to that extent the borrowing cost was recovered and not truly a cost of the asset. Once specific funds are exhausted, further construction is presumed financed from the general pool, so we apply the *weighted-average* rate of general borrowings to the *weighted-average* expenditure — weighting by time because a rupee spent on 1 January ties up borrowed funds for only three months, not twelve. The two big errors are (i) forgetting to deduct the ₹1,50,000 temporary income (only *specific*-loan income is deducted, never general), and (ii) applying the general rate to the whole ₹1,80,00,000 instead of the portion beyond the specific loan.

*(Full-marks tip: the capitalisation-rate working, the time-weighting of expenditure, and the netting of investment income against *specific* interest are the three scoring points; a flat interest-on-total approach caps you at half marks.)*

---

### Q24. Ch: AS 17 — Segment Reporting: Identifying Reportable Segments (Marks: 8) [Problem]
**Question:** Nova Ltd has five business segments. Using the AS 17 quantitative thresholds, identify the reportable segments and verify the 75% external-revenue test.

| Segment | External revenue (₹ lakh) | Inter-segment revenue (₹ lakh) | Segment result Profit/(Loss) (₹ lakh) | Segment assets (₹ lakh) |
|---------|---------------------------|--------------------------------|----------------------------------------|--------------------------|
| P | 300 | 20 | 60 | 500 |
| Q | 90 | 10 | (40) | 260 |
| R | 40 | 0 | 8 | 120 |
| S | 25 | 5 | (6) | 60 |
| T | 15 | 0 | 2 | 60 |
| **Total** | **470** | **45** | | **1,000** |

**Solution:**

**WN-1 — Total revenue (external + inter-segment) per segment and the 10% revenue test:**
Total revenue of all segments = 470 + 45 = ₹515 lakh. Threshold = 10% × 515 = **₹51.5 lakh**.

| Segment | Total revenue | ≥ 51.5? |
|---------|---------------|---------|
| P | 320 | Yes |
| Q | 100 | Yes |
| R | 40 | No |
| S | 30 | No |
| T | 15 | No |

**WN-2 — Result test (10% of greater of total profits or total losses, in absolute terms):**
Total profits = 60 + 8 + 2 = ₹70 lakh; total losses = 40 + 6 = ₹46 lakh. Greater = ₹70 lakh. Threshold = **₹7 lakh**.

| Segment | |Result| | ≥ 7? |
|---------|----------|------|
| P | 60 | Yes |
| Q | 40 | Yes |
| R | 8 | Yes |
| S | 6 | No |
| T | 2 | No |

**WN-3 — Assets test (≥ 10% of ₹1,000 lakh = ₹100 lakh):** P (500), Q (260), R (120) qualify; S (60), T (60) do not.

**WN-4 — Reportable segments:** A segment is reportable if it clears **any one** test → **P, Q and R** are reportable.

**WN-5 — 75% test:** External revenue of reportable segments = 300 + 90 + 40 = ₹430 lakh. Total external revenue = ₹470 lakh. Coverage = 430/470 = **91.5% ≥ 75%.** No further segment need be added.

**Answer:** Reportable segments are **P, Q and R**; they cover 91.5% of external revenue, satisfying the 75% requirement. S and T are shown in "all other segments."

**Why this way (the reasoning):** AS 17 wants the financial statements to reveal the *material engines and drags* of the business, so a segment need clear only *one* of the three 10% gates (revenue, result or assets) to be reportable — being big on any single dimension makes it decision-relevant. Two subtleties trap students: the revenue test uses *total* revenue including inter-segment (515, not 470), because internal sales still consume resources; and the result test compares against the *greater of aggregate profits or aggregate losses in absolute value* (70, not the net figure), so a loss-making segment like Q is captured — precisely the segment investors most want to see. Finally the 75% floor ensures the disclosed segments actually explain most of the enterprise; if they had fallen short, additional segments would be designated even if they failed all three tests.

*(Full-marks tip: the ₹515 lakh (not ₹470) revenue base and the "greater of profits or losses = ₹70 lakh" result base are the two figures examiners check; using net result or excluding inter-segment revenue is the common deduction.)*

---

### Q25. Ch: AS 18 — Related Party Disclosures: Identifying Relationships (Marks: 6) [Case/Application]
**Question:** Examine, under AS 18, whether the following are "related parties" of Crestview Ltd and whether transactions with them require disclosure:

| # | Relationship |
|---|--------------|
| a | Falcon Ltd, which holds 55% of Crestview's equity. |
| b | Mr A, a non-executive director who is not part of key management and takes no operating decisions. |
| c | Sigma Ltd, in which Crestview holds 30% and exercises significant influence (an associate). |
| d | The wife of the Managing Director, to whom Crestview sold goods. |
| e | Crestview's principal banker, from which it has a ₹50 crore loan on normal commercial terms. |
| f | Crestview and Delta Ltd are both subsidiaries of the same parent, Falcon Ltd (fellow subsidiaries). |

**Answer:** AS 18 covers parties where one **controls**, is **controlled by**, or can exercise **significant influence** over the other — and specified categories: holding/subsidiary/fellow-subsidiary companies, associates & JVs, key management personnel (KMP) and their relatives, and enterprises controlled by KMP/relatives.

- **(a) Falcon Ltd — RELATED (holding company; control via 55%).** Disclose.
- **(b) Non-executive director, no decision power — NOT a related party.** AS 18's KMP definition hinges on *authority and responsibility for planning, directing and controlling*; a director with no such power is excluded. No disclosure on this ground.
- **(c) Sigma Ltd (associate, significant influence) — RELATED.** Disclose.
- **(d) Wife of the Managing Director — RELATED (relative of KMP).** Sale of goods to her must be disclosed.
- **(e) Principal banker — NOT related.** AS 18 *specifically excludes* providers of finance in the ordinary course of business merely by virtue of the lending relationship. No disclosure under AS 18.
- **(f) Delta Ltd (fellow subsidiary) — RELATED.** Disclose.

**Conclusion:** Related parties are Falcon (a), Sigma (c), the MD's wife (d) and Delta (f); the non-executive director (b) and the banker (e) are not.

**Why this way (the reasoning):** AS 18 targets relationships where the *arm's-length assumption may not hold* — where control or influence could bend the terms of a transaction — so control (holding, fellow-subsidiary), significant influence (associate) and personal proximity to those who wield power (KMP and their relatives) are all caught. The two deliberate exclusions test whether a student reads the standard or guesses: a lender and (in the same vein) trade unions or government agencies are *not* related merely through their normal dealings, because a routine loan does not confer the power to distort other transactions; and a titular director without genuine decision authority is not KMP. Treating the banker as related, or missing the MD's wife, are the two classic errors.

*(Full-marks tip: state the *basis* (control / significant influence / KMP-relative) for each "yes" and cite the *specific exclusion* for the banker and the powerless director — bare yes/no answers earn little.)*

---

### Q26. Ch: AS 19 — Finance Lease: Classification and Finance-Charge Allocation Schedule (Marks: 10) [Problem]
**Question:** On 1 April 2025 Titan Ltd (lessee) takes a machine on lease. Fair value ₹10,00,000; four annual payments of **₹3,15,470** at the end of each year; interest rate implicit in the lease **10%**; machine's useful life 4 years with nil residual value; ownership passes at the end. Show that this is a finance lease, prepare the finance-charge allocation schedule, and state the Year-1 accounting.

**Solution:**

**WN-1 — Classification.** The lease transfers ownership at term-end and the lease term (4 years) equals the asset's useful life; substantially all risks and rewards pass to the lessee → **finance lease**.

**WN-2 — Recognition amount.** Record the asset and liability at the **lower of fair value and PV of minimum lease payments**. PV of MLP = 3,15,470 × PVIFA(10%, 4 yr = 3.1699) = ₹10,00,000 = fair value. Capitalise at **₹10,00,000**.

**WN-3 — Finance-charge allocation (effective-interest / actuarial method):**

| Year | Opening liability (₹) | Interest @10% (₹) | Payment (₹) | Closing liability (₹) |
|------|----------------------|-------------------|-------------|-----------------------|
| 1 | 10,00,000 | 1,00,000 | 3,15,470 | 7,84,530 |
| 2 | 7,84,530 | 78,453 | 3,15,470 | 5,47,513 |
| 3 | 5,47,513 | 54,751 | 3,15,470 | 2,86,794 |
| 4 | 2,86,794 | 28,676* | 3,15,470 | 0 |

*Year-4 interest adjusted by ₹3 rounding to fully extinguish the liability.

**WN-4 — Depreciation.** Since ownership will pass, depreciate over the **useful life (4 years)**: 10,00,000 / 4 = **₹2,50,000 p.a.**

**Year-1 charge to P&L** = finance charge ₹1,00,000 + depreciation ₹2,50,000 = **₹3,50,000**.

**Journal (Year 1):**
- Machinery A/c Dr ₹10,00,000 / To Lessor (Lease liability) ₹10,00,000
- Finance charge A/c Dr ₹1,00,000 & Lessor A/c Dr ₹2,15,470 / To Bank ₹3,15,470
- Depreciation A/c Dr ₹2,50,000 / To Machinery A/c ₹2,50,000

**Answer:** Finance lease capitalised at ₹10,00,000; Year-1 P&L charge ₹3,50,000 (₹1,00,000 finance + ₹2,50,000 depreciation); closing lease liability ₹7,84,530.

**Why this way (the reasoning):** AS 19 applies **substance over form** — although Titan does not legally own the machine at inception, it bears the wear, obsolescence and residual risk for the asset's whole life, so economically it has *bought an asset on credit*, and the accounts must show both the asset and the borrowing. The payment is therefore split: the part representing the *cost of financing* (interest on the outstanding balance) goes to P&L, while the rest *repays the liability*. The effective-interest method produces a **falling** finance charge because interest accrues on a shrinking balance — mirroring a normal loan — which is why a straight-line split of the ₹2,61,880 total finance charge would be wrong. The depreciation twist: because ownership will transfer, you depreciate over *useful life*; had ownership **not** been reasonably certain to pass, you would use the *shorter of lease term and useful life*.

*(Full-marks tip: lower-of-FV-and-PV recognition, the declining-balance finance schedule, and depreciation over useful life (because ownership transfers) are the three scoring pillars; straight-lining the finance charge or depreciating over lease term when ownership transfers are the usual deductions.)*

---

### Q27. Ch: AS 19 — Sale and Leaseback Transactions (Marks: 8) [Case/Application]
**Question:** Beacon Ltd sells an asset (carrying amount ₹8,00,000) and immediately leases it back. Advise, under AS 19, on the treatment of the resulting profit/loss in each independent scenario:

| Scenario | Leaseback type | Sale price (₹) | Fair value (₹) |
|----------|----------------|----------------|----------------|
| A | Finance lease | 11,00,000 | 10,00,000 |
| B | Operating lease | 11,00,000 | 11,00,000 |
| C | Operating lease | 12,00,000 | 10,00,000 |
| D | Operating lease | 6,00,000 (loss; future rentals below market) | 10,00,000 |

**Answer:**

- **Scenario A — Finance-lease leaseback.** Any excess of sale price over carrying amount (₹11,00,000 − ₹8,00,000 = ₹3,00,000) is **deferred and amortised over the lease term**, *not* recognised at once. Rationale: the seller-lessee has not really disposed of the asset — it has, in substance, *raised finance against it* and retained the risks/rewards; recognising a "profit" on what is effectively a secured borrowing would be misleading.

- **Scenario B — Operating leaseback, sale price = fair value (₹11,00,000).** This is a genuine sale at market value. Profit = 11,00,000 − 8,00,000 = **₹3,00,000 recognised immediately**.

- **Scenario C — Operating leaseback, sale price (₹12,00,000) above fair value (₹10,00,000).** Split the gain: profit up to fair value = 10,00,000 − 8,00,000 = **₹2,00,000 recognised now**; the excess of sale price over fair value = ₹2,00,000 is **deferred and amortised over the period of expected use**, because that ₹2,00,000 is not a real gain — it is compensation for above-market future rentals.

- **Scenario D — Operating leaseback at a loss, compensated by below-market rentals.** The apparent loss (₹10,00,000 fair value − ₹6,00,000 sale price = ₹4,00,000) is **deferred and amortised** in proportion to lease payments, because the low sale price is offset by *below-market future rentals* — so the "loss" is really a prepaid reduction of future rent, not a current loss.

**Why this way (the reasoning):** The single principle is: **recognise a gain or loss only to the extent a real, arm's-length transfer has occurred at fair value.** In a finance-lease leaseback nothing has genuinely left the seller's economic control, so any "profit" is deferred — it is a financing transaction dressed as a sale. In operating-lease leasebacks the asset does leave, so profit is real *up to fair value*; anything above fair value is not profit but disguised pre-payment for inflated rentals, hence deferred. Likewise a sale below fair value looks like a loss but is really compensated by cheap future rent, so it too is spread. The examiner's trap is booking the full sale-vs-carrying difference immediately in every case, ignoring the fair-value ceiling and the financing substance.

*(Full-marks tip: for Scenario C, explicitly *bifurcate* the ₹4,00,000 into ₹2,00,000 immediate + ₹2,00,000 deferred at the fair-value line; treating the whole gain as immediate is the standard error.)*

---

### Q28. Ch: AS 20 — Basic and Diluted EPS with Rights Issue and Convertible Debentures (Marks: 10) [Problem]
**Question:** Compute Basic and Diluted EPS of Pinnacle Ltd for the year ended 31 March 2026.

| Particulars | Details |
|-------------|---------|
| Net profit after tax | ₹52,00,000 |
| Preference dividend for the year | ₹2,00,000 |
| Equity shares outstanding on 1.4.2025 | 10,00,000 shares of ₹10 |
| Rights issue | 1 new share for every 4 held, at ₹15, on 1.8.2025 |
| Fair value per share immediately before rights exercise | ₹20 |
| 12% Convertible debentures (outstanding whole year) | ₹40,00,000; each ₹100 debenture converts into 4 equity shares |
| Tax rate | 30% |

**Solution:**

**WN-1 — Earnings for equity (Basic):** 52,00,000 − 2,00,000 = **₹50,00,000**.

**WN-2 — Theoretical ex-rights price (TERP) and rights adjustment factor:**
Rights shares = 10,00,000 / 4 = 2,50,000.
TERP = [(20 × 10,00,000) + (15 × 2,50,000)] / (10,00,000 + 2,50,000) = (2,00,00,000 + 37,50,000)/12,50,000 = **₹19**.
Adjustment factor = Fair value before rights / TERP = 20 / 19.

**WN-3 — Weighted-average number of shares (Basic):**
- Pre-rights (1.4 – 31.7, 4 months), adjusted: 10,00,000 × (20/19) × 4/12 = **3,50,877**.
- Post-rights (1.8 – 31.3, 8 months): 12,50,000 × 8/12 = **8,33,333**.
- Weighted average = **11,84,210 shares**.

**WN-4 — Basic EPS** = 50,00,000 / 11,84,210 = **₹4.22**.

**WN-5 — Diluted EPS (test convertible debentures):**
- Interest saved if converted = 40,00,000 × 12% = ₹4,80,000; net of tax = 4,80,000 × (1 − 0.30) = **₹3,36,000**.
- Adjusted earnings = 50,00,000 + 3,36,000 = ₹53,36,000.
- Potential shares on conversion = (40,00,000 / 100) × 4 = **1,60,000 shares**.
- Dilution check: incremental EPS = 3,36,000 / 1,60,000 = ₹2.10 < Basic EPS ₹4.22 → **dilutive** (include).
- Diluted weighted shares = 11,84,210 + 1,60,000 = 13,44,210.

**WN-6 — Diluted EPS** = 53,36,000 / 13,44,210 = **₹3.97**.

**Statement of EPS**

| Particulars | ₹ |
|-------------|-----|
| Basic EPS | 4.22 |
| Diluted EPS | 3.97 |

**Answer:** Basic EPS **₹4.22**; Diluted EPS **₹3.97**.

**Why this way (the reasoning):** A rights issue at ₹15 when the share is worth ₹20 contains a hidden **bonus element** — shareholders get value for nothing — so AS 20 does not treat it as a plain fresh issue. If you ignored this, EPS would look artificially better because the extra shares came cheap. The adjustment factor (20/19) *retrospectively inflates* the pre-rights shares as though the bonus element had always existed, making the series comparable — this is the step most students miss. For diluted EPS, the logic is "what if every dilutive instrument had already converted?": add back the *after-tax* interest the company would save (because converted debentures pay no interest) and add the shares that would be issued. Crucially, you include a potential issue only if it *reduces* EPS — the incremental-EPS test (₹2.10 < ₹4.22) confirms dilution; an anti-dilutive instrument (incremental EPS above basic) would be excluded, otherwise you'd wrongly report a *higher* diluted figure.

*(Full-marks tip: the TERP/adjustment-factor working and the explicit dilution test are the two highest-value steps; forgetting the tax effect on debenture interest, or including an anti-dilutive instrument, are the common heavy deductions.)*

---

### Q29. Ch: AS 22 — Deferred Tax on Timing Differences (Marks: 10) [Problem]
**Question:** From the following data of Solaris Ltd for FY 2025-26, compute the current tax, the deferred tax charge, and the net deferred tax balance. Tax rate 30%.

| Particulars | ₹ |
|-------------|-----|
| Accounting profit before tax | 40,00,000 |
| Depreciation as per books | 12,00,000 |
| Depreciation as per Income-tax | 20,00,000 |
| Provision for doubtful debts (disallowed now; deductible on actual write-off) | 2,50,000 |
| Bonus unpaid, disallowed u/s 43B (deductible on payment) | 1,50,000 |
| Donation disallowed (permanent) | 1,00,000 |

**Solution:**

**WN-1 — Identify timing vs permanent differences:**
- Depreciation difference = 20,00,000 − 12,00,000 = ₹8,00,000 → tax dep higher now, will reverse later → **taxable timing difference → DTL**.
- Provision for doubtful debts ₹2,50,000 → disallowed now, deductible later → **deductible timing difference → DTA**.
- Bonus u/s 43B ₹1,50,000 → disallowed now, deductible on payment → **deductible timing difference → DTA**.
- Donation ₹1,00,000 → never deductible → **permanent difference (no deferred tax).**

**WN-2 — Computation of taxable income & current tax:**

| Particulars | ₹ |
|-------------|-----|
| Accounting profit before tax | 40,00,000 |
| Add: Book depreciation | 12,00,000 |
| Less: Tax depreciation | (20,00,000) |
| Add: Provision for doubtful debts | 2,50,000 |
| Add: Bonus disallowed u/s 43B | 1,50,000 |
| Add: Donation (permanent) | 1,00,000 |
| **Taxable income** | **37,00,000** |
| **Current tax @30%** | **11,10,000** |

**WN-3 — Deferred tax:**

| Timing difference | Amount (₹) | Type | DT @30% (₹) |
|-------------------|-----------|------|-------------|
| Depreciation | 8,00,000 | DTL | 2,40,000 |
| Provision for doubtful debts | 2,50,000 | DTA | (75,000) |
| Bonus u/s 43B | 1,50,000 | DTA | (45,000) |
| **Net deferred tax liability (charge)** | | | **1,20,000** |

**WN-4 — Total tax expense reconciliation:**
Current tax ₹11,10,000 + Deferred tax ₹1,20,000 = **₹12,30,000**.
Check: (Accounting profit ₹40,00,000 + permanent donation ₹1,00,000) × 30% = ₹12,30,000. **Reconciles.**

**Answer:** Current tax **₹11,10,000**; net deferred tax charge **₹1,20,000 (DTL)**; total tax expense **₹12,30,000**.

**Why this way (the reasoning):** AS 22 exists because taxable profit and accounting profit diverge, and the *matching principle* demands that tax expense reflect the profit *reported this year*, not merely the tax *payable this year*. **Timing differences** reverse over time — excess tax depreciation now means less depreciation (higher tax) later, creating a *deferred tax liability*; a disallowed provision means a *future* deduction, creating a *deferred tax asset*. **Permanent differences** (the donation) never reverse, so they create **no** deferred tax — recognising deferred tax on them is the single most common error. The reconciliation is the proof of correctness: total tax expense should equal accounting profit adjusted *only* for permanent differences, times the rate — if it doesn't reconcile to ₹12,30,000, a timing item has been mis-classified. Note also that DTAs on items like the provision are recognised only where their reversal against future taxable income is *reasonably certain* (virtually certain if there are carried-forward losses).

*(Full-marks tip: correctly excluding the donation from deferred tax and showing the ₹12,30,000 reconciliation are the concept-marks; students routinely lose marks by computing DT on the permanent difference or by netting DTA against DTL without justifying recognition.)*

---

### Q30. Ch: AS 24 — Discontinuing Operations (Marks: 5) [Case/Application]
**Question:** Horizon Ltd's Board, on 20 January 2026, approved and publicly announced a detailed plan to sell its entire "Textiles Division" — a separate major line of business with its own assets, results and cash flows — by 30 September 2026. A binding sale agreement is expected by June 2026. Examine, under AS 24, whether this is a "discontinuing operation," identify the "initial disclosure event," and list the key disclosures required in the 31.3.2026 financial statements.

**Answer:**
**Is it a discontinuing operation?** AS 24 defines a discontinuing operation as a **component that is a separate major line of business or geographical area**, distinguishable operationally and for financial reporting, that the enterprise is disposing of under a **single plan**. The Textiles Division — a separate major line with its own assets, results and cash flows, being sold entirely under one plan — **qualifies as a discontinuing operation.**

**Initial disclosure event.** Disclosure begins on the *earlier* of (a) entering into a **binding sale agreement**, or (b) the Board **approving and announcing** a detailed formal disposal plan. Here the Board approved *and publicly announced* the plan on **20 January 2026** — that is the initial disclosure event, and it falls *before* year-end, so disclosures are triggered in the 2025-26 statements (even though the binding agreement comes only in June 2026).

**Key disclosures required:** (i) a description of the discontinuing operation and the business/geographical segment it falls in; (ii) the date and nature of the initial disclosure event and the expected timing of completion; (iii) the **carrying amounts of the total assets and liabilities** to be disposed of; (iv) the **revenue, expenses, pre-tax profit/loss** and the related **income tax** of the discontinuing operation; and (v) the net cash flows attributable to operating, investing and financing activities.

**Conclusion:** The Textiles Division is a discontinuing operation; the initial disclosure event is 20 January 2026; full AS 24 disclosures must appear in the 2025-26 financial statements.

**Why this way (the reasoning):** AS 24 is a **disclosure** standard, not a measurement one — its purpose is to let users separate the *continuing* business (which drives future results) from the part being wound down, so they can forecast better. That is why disclosure is pinned to the *initial disclosure event* — the moment the enterprise becomes *demonstrably committed* to the disposal, whether by a binding contract or a board-approved, announced plan, whichever is earlier. The trap is to wait for the binding agreement (June 2026) and conclude nothing is disclosed at 31.3.2026 — but the *announced board plan* in January already commits the entity and triggers disclosure. Note AS 24 does **not** itself require a special provision; any impairment is dealt with under AS 28 and any restructuring provision under AS 29.

*(Full-marks tip: correctly picking 20 January (the announced plan) as the initial disclosure event — not the June agreement — plus listing the asset/liability and result disclosures earns full marks; merely defining a discontinuing operation without applying the "earlier of" test is under-marked.)*

---

### Q31. Ch: AS 25 — Interim Financial Reporting: Estimated Annual Effective Tax Rate (Marks: 8) [Problem]
**Question:** Comet Ltd prepares quarterly interim reports. For the quarter ended 30 June 2025, advise on the treatment of the following and compute the interim tax expense.

| Particulars | ₹ |
|-------------|-----|
| Pre-tax accounting income for the quarter (Q1) | 10,00,000 |
| Estimated annual pre-tax accounting income | 48,00,000 |
| Estimated permanent disallowances for the year | 2,00,000 |
| Statutory tax rate | 30% |

Also advise on: (i) seasonal revenue that peaks in Q3; (ii) a lump-sum year-end staff bonus expected to be ₹8,00,000; (iii) a major planned plant overhaul scheduled for Q4; (iv) a one-off insurance gain of ₹3,00,000 arising in Q1.

**Solution:**

**WN-1 — Estimated annual effective tax rate (ETR):**
Estimated annual taxable income = 48,00,000 + 2,00,000 (permanent disallowance) = ₹50,00,000.
Estimated annual tax = 50,00,000 × 30% = ₹15,00,000.
**ETR = 15,00,000 / 48,00,000 = 31.25%.**

**WN-2 — Interim tax for Q1** = Q1 pre-tax income × ETR = 10,00,000 × 31.25% = **₹3,12,500.**
(Note: applying the bare statutory 30% would give ₹3,00,000 — *wrong*, because it ignores the permanent difference embedded in the annual estimate.)

**WN-3 — Treatment of other items (interim principle: view the year as the primary period, but measure each item on the same basis as for annual accounts):**
- **(i) Seasonal revenue (Q3 peak):** recognise **only as earned**; do **not** anticipate or defer to smooth quarters — anticipating Q3 sales in Q1 is prohibited.
- **(ii) Year-end bonus ₹8,00,000:** provide **proportionately (₹2,00,000 in Q1)** *only if* a present obligation (contractual/constructive) exists at quarter-end; otherwise do not anticipate it.
- **(iii) Planned Q4 overhaul:** **no provision now** — a mere intention to incur future expenditure is not a present obligation (AS 29); recognise only when incurred.
- **(iv) One-off insurance gain ₹3,00,000:** recognise **fully in Q1** when it arises; do **not** spread it over the year.

**Answer:** Interim tax for Q1 = **₹3,12,500** (using ETR 31.25%). Seasonal income is recognised as earned, the bonus is accrued only if an obligation exists, the planned overhaul is not provided, and the insurance gain is recognised fully in Q1.

**Why this way (the reasoning):** AS 25 adopts the **integral view for tax** but the **discrete view for most other items** — a deliberate hybrid. Tax is charged using the *estimated annual effective rate* because income tax is inherently an *annual* levy computed on the whole year's income (with slabs, rebates and permanent adjustments), so estimating the year and applying that blended rate to each quarter prevents distortions that a naïve quarterly 30% would cause — which is exactly why ₹3,12,500, not ₹3,00,000, is correct. For revenues and costs, however, an interim period is *not* a mini-year to be smoothed: income is recognised when earned and costs when the obligating event occurs, so you may neither anticipate the Q3 seasonal peak nor pre-provide the Q4 overhaul (no present obligation), and a genuine one-off gain belongs wholly to the period it arises. The recurring error is forcing artificial smoothing across quarters, which defeats the standard's aim of *faithful* interim reporting.

*(Full-marks tip: the ETR computation (grossing up for the permanent difference) is the key numeric mark; for the narrative items, tie each to "present obligation exists?" and "earned yet?" — vague "provide proportionately" answers without the obligation test lose marks.)*

---

### Q32. Ch: AS 26 — Intangible Assets: Research vs Development and Internally Generated Items (Marks: 8) [Case/Application]
**Question:** Advise Insignia Ltd, under AS 26, on the treatment of each item during FY 2025-26:

| # | Expenditure | ₹ |
|---|-------------|-----|
| a | Research phase of a new process — investigating alternatives | 10,00,000 |
| b | Development phase after technical/commercial feasibility, adequate resources and probable future benefits were all demonstrated | 25,00,000 |
| c | Cost of internally generating and building the company's own brand | 15,00,000 |
| d | Purchase of a patent from an outside party | 12,00,000 |
| e | Staff training cost and a launch advertising campaign | 6,00,000 |

**Answer:**

- **(a) Research expenditure — EXPENSE ₹10,00,000.** In the research phase an enterprise *cannot demonstrate* that an intangible generating future benefits exists; AS 26 therefore mandates that **all research cost be charged to P&L** as incurred.
- **(b) Development expenditure — CAPITALISE ₹25,00,000.** Development cost is capitalised **only when all six criteria are met**: technical feasibility, intention to complete, ability to use/sell, probable future economic benefits (existence of a market/usefulness), availability of adequate resources, and ability to measure cost reliably. All conditions are satisfied here, so recognise an intangible asset and amortise it (rebuttable presumption of useful life; systematic amortisation).
- **(c) Internally generated brand — EXPENSE ₹15,00,000.** AS 26 *specifically prohibits* recognising internally generated brands, mastheads, publishing titles and goodwill, because their cost **cannot be distinguished** from the cost of developing the business as a whole.
- **(d) Purchased patent — CAPITALISE ₹12,00,000.** A *separately acquired* intangible has a reliably measurable cost and identifiable future benefits, so it is recognised as an intangible asset and amortised over its useful life.
- **(e) Training & advertising — EXPENSE ₹6,00,000.** These do not create an *identifiable, controlled* resource — the enterprise cannot control the trained staff or the goodwill from advertising — so they are charged to P&L as incurred.

**Conclusion:** Capitalise (b) ₹25,00,000 and (d) ₹12,00,000; expense (a), (c) and (e) totalling ₹31,00,000.

**Why this way (the reasoning):** AS 26 recognises an intangible only when it meets **identifiability, control and probable future economic benefit** *and* its cost can be measured reliably — a high bar that internally generated items rarely clear. The research/development split embodies this: in *research* you cannot yet prove an asset exists, so it is expensed; only once the six *development* criteria establish that a saleable/usable, benefit-yielding asset is emerging does capitalisation become justified. Internally generated brands and goodwill are barred because you cannot separate their cost from routine business-building — capitalising them would let a company inflate its balance sheet with self-created "value." Training and advertising fail the *control* test: you don't own your employees or your customers' goodwill. The examiner's trap is capitalising the brand or the advertising by analogy to the purchased patent — but *purchased* intangibles pass the reliable-measurement test that *internally generated* ones fail.

*(Full-marks tip: listing the six development-recognition criteria and citing the explicit prohibition on internally generated brands are the concept-marks; capitalising research or the internally built brand is the standard heavy deduction.)*

---

### Q33. Ch: AS 28 — Impairment: Recoverable Amount and Allocation Across a CGU with Goodwill (Marks: 10) [Problem]
**Question:** A cash-generating unit (CGU) of Everest Ltd has the following carrying amounts on 31.3.2026. Owing to adverse conditions an impairment test is done. Estimated future cash flows are ₹95,00,000 per year for 5 years; the appropriate discount rate is 10% (PVIFA 10%, 5 yr = 3.7908). Net selling price of the CGU is ₹3,40,00,000. Compute the impairment loss and allocate it.

| Asset in CGU | Carrying amount (₹) |
|--------------|---------------------|
| Goodwill | 1,00,00,000 |
| Building | 2,00,00,000 |
| Plant | 1,50,00,000 |
| Other assets | 50,00,000 |
| **Total** | **5,00,00,000** |

**Solution:**

**WN-1 — Value in use** = 95,00,000 × 3.7908 = ₹3,60,12,600 ≈ **₹3,60,00,000**.

**WN-2 — Recoverable amount** = higher of (Value in use ₹3,60,00,000, Net selling price ₹3,40,00,000) = **₹3,60,00,000.**

**WN-3 — Impairment loss** = Carrying amount − Recoverable amount = 5,00,00,000 − 3,60,00,000 = **₹1,40,00,000.**

**WN-4 — Allocation (AS 28 order): first to goodwill, then pro rata to other assets on carrying-amount basis.**
- Step 1: write off **goodwill ₹1,00,00,000** in full.
- Step 2: remaining loss = 1,40,00,000 − 1,00,00,000 = ₹40,00,000, allocated across Building, Plant and Other assets (pro-rata base = 2,00 + 1,50 + 0,50 = ₹4,00,00,000):

| Asset | Base (₹) | Share | Allocated loss (₹) | Revised carrying (₹) |
|-------|----------|-------|--------------------|-----------------------|
| Building | 2,00,00,000 | 200/400 | 20,00,000 | 1,80,00,000 |
| Plant | 1,50,00,000 | 150/400 | 15,00,000 | 1,35,00,000 |
| Other assets | 50,00,000 | 50/400 | 5,00,000 | 45,00,000 |
| **Total** | 4,00,00,000 | | **40,00,000** | 3,60,00,000 |

**WN-5 — Floor check:** No individual asset is reduced below its own recoverable amount (none is separately measurable higher), so the pro-rata allocation stands.

**Post-impairment CGU carrying amount** = 0 (goodwill) + 1,80,00,000 + 1,35,00,000 + 45,00,000 = **₹3,60,00,000** = recoverable amount. ✔

**Answer:** Impairment loss **₹1,40,00,000** — goodwill ₹1,00,00,000 written off entirely, and ₹40,00,000 apportioned as Building ₹20,00,000, Plant ₹15,00,000 and Other assets ₹5,00,000.

**Why this way (the reasoning):** AS 28 asks a simple economic question: *is the asset worth more to us than its book value?* "Worth" is the **recoverable amount** — the *higher* of what we'd get by selling (net selling price) and what we'd earn by using it (value in use, the discounted future cash flows) — because a rational owner keeps the asset only if using it beats selling it, and vice versa. Here value in use (₹3.60 cr) exceeds net selling price (₹3.40 cr), so the unit is worth ₹3.60 cr and the ₹1.40 cr shortfall is a real loss. The **allocation order** is deliberate: goodwill is the least tangible, most fragile value — it is the first to evaporate when a unit underperforms — so it absorbs the loss first; only the residual is spread across identifiable assets *pro rata to carrying amount*, subject to the floor that no asset falls below its own recoverable amount. Two traps: taking the *lower* of the two measures (or only net selling price) as recoverable amount, and spreading the loss evenly instead of hitting goodwill first.

*(Full-marks tip: recoverable amount as the *higher* of VIU and NSP, the goodwill-first allocation order, and the floor check are the scoring pillars; using the lower figure or allocating to goodwill last are the classic errors.)*

---

### Q34. Ch: AS 29 — Provisions, Contingent Liabilities and Contingent Assets (Marks: 8) [Case/Application]
**Question:** Classify each of the following for Vertex Ltd (year ended 31.3.2026) as a **provision**, a **contingent liability**, a **contingent asset**, or **no accounting**, and where a provision is required, measure it:

| # | Situation |
|---|-----------|
| a | The company gives a 1-year warranty on products sold. Of ₹1,00,00,000 sales, past experience: 80% no defect; 15% minor defect (repair cost 4% of sales); 5% major defect (repair cost 10% of sales). |
| b | A customer has sued Vertex for ₹30,00,000; legal opinion says an outflow is *possible but not probable*. |
| c | Vertex has an onerous contract: unavoidable cost ₹12,00,000 exceeds the expected benefit ₹7,00,000. |
| d | The Board intends to restructure a division next year but has not announced or begun any plan. |
| e | Vertex expects future operating losses of ₹5,00,000 in the coming year. |
| f | Vertex has filed a claim against a supplier; recovery of ₹4,00,000 is *probable but not virtually certain*. |

**Answer:**

- **(a) Warranty — PROVISION (measure by expected value):**
  Minor: 15% × 1,00,00,000 × 4% = ₹60,000; Major: 5% × 1,00,00,000 × 10% = ₹50,000; No-defect: nil.
  **Provision = ₹1,10,000.** (A past obligating event — the sale — creates a present legal obligation; outflow is probable; reliably estimable by expected value.)
- **(b) Lawsuit (outflow possible, not probable) — CONTINGENT LIABILITY.** Present obligation is *possible*, not probable, so **no provision** — disclose the ₹30,00,000 by way of note.
- **(c) Onerous contract — PROVISION ₹5,00,000** (the *lower* of the cost of fulfilling and the cost of exiting; here the *net* unavoidable loss = 12,00,000 − 7,00,000 = ₹5,00,000). AS 29 requires the *present obligation under an onerous contract* to be provided.
- **(d) Mere intention to restructure — NO ACCOUNTING.** A present obligation arises only when the entity has a **detailed formal plan** *and* has raised a valid expectation by starting to implement or announcing it. A bare intention creates no obligation → no provision, no disclosure.
- **(e) Future operating losses — NO PROVISION.** These relate to *future* events; there is **no present obligation from a past event** — provisions are prohibited for future operating losses. (They may signal impairment under AS 28.)
- **(f) Probable recovery of ₹4,00,000 — CONTINGENT ASSET.** Not recognised (prudence); disclosed only where inflow is *probable*. Recognition would await inflow becoming **virtually certain**.

**Why this way (the reasoning):** AS 29 recognises a provision only when the **three gates** are all open: a *present obligation from a past event*, a *probable* outflow of resources, and a *reliable estimate*. Every classification above is just this test applied — the warranty and the onerous contract pass all three (so they are provided), the lawsuit fails the "probable" gate (contingent liability, disclosed), and mere intentions and future losses fail the "present obligation from a past event" gate entirely (nothing is booked). The **asymmetry** between (b) and (f) is the standard's prudence at work: possible *liabilities* are disclosed but possible *assets* are not recognised until virtually certain — losses are anticipated, gains are not. Measuring the warranty by **expected value** (probability-weighting the outcomes) rather than the worst case reflects that the provision covers a *large population* of items where the statistical average is the best estimate. The classic errors are provisioning the merely-intended restructuring, providing for future operating losses, and recognising the contingent asset.

*(Full-marks tip: the ₹1,10,000 expected-value warranty computation and the onerous-contract *net* ₹5,00,000, plus refusing to provide for future losses and the restructuring intention, are the scoring points; recognising the contingent asset or provisioning future losses are the heavy deductions.)*

### Q35. Ch: AS 3 Cash Flow Statements — Full Indirect-Method Statement with Tricky Adjustments (Marks: 10) [Problem]
**Question:** From the following Balance Sheets of Vishwas Ltd. and the additional information, prepare a Cash Flow Statement for the year ended 31 March 2026 using the **indirect method** as per AS 3.

**Balance Sheets as at 31 March (₹ in lakh)**

| Particulars | 2026 | 2025 |
|---|---:|---:|
| **EQUITY & LIABILITIES** | | |
| Equity share capital (₹10 each) | 600 | 500 |
| Securities premium | 80 | 50 |
| General reserve | 150 | 120 |
| Surplus (Statement of P&L) | 110 | 80 |
| 10% Debentures | 150 | 200 |
| Long-term provision (warranty) | 28 | 20 |
| Trade payables | 110 | 90 |
| Provision for tax | 50 | 40 |
| **Total** | **1,278** | **1,100** |
| **ASSETS** | | |
| Property, plant & equipment (gross) | 900 | 700 |
| Less: Accumulated depreciation | (230) | (180) |
| Goodwill | 40 | 60 |
| Investments (long-term) | 140 | 100 |
| Inventory | 190 | 150 |
| Trade receivables | 160 | 120 |
| Cash & cash equivalents | 78 | 150 |
| **Total** | **1,278** | **1,100** |

**Additional information:** (i) A machine costing ₹80 lakh (accumulated depreciation ₹30 lakh) was sold for ₹40 lakh. (ii) Goodwill was amortised during the year. (iii) Debentures were redeemed at par on 1 April 2025. (iv) Interest on debentures ₹18 lakh was charged and paid. (v) Dividend received on investments ₹8 lakh. (vi) Dividend of ₹40 lakh was paid during the year. (vii) Tax charged in the Statement of P&L was ₹45 lakh.

**Solution:**

**WN-1 — Net profit before tax (PBT):** Surplus increased 80→110 = ₹30. Add appropriations debited to surplus: transfer to General Reserve (120→150) = ₹30; dividend paid ₹40. So PAT = 30 + 30 + 40 = ₹100 lakh. PBT = PAT ₹100 + tax ₹45 = **₹145 lakh.**

**WN-2 — Depreciation for the year:** Accumulated dep: opening 180 − 30 (on machine sold) + Dep = 230 → Dep = **₹80 lakh.**

**WN-3 — PPE purchased:** Gross: 700 − 80 (sold) + Purchases = 900 → Purchases = **₹280 lakh.**

**WN-4 — Loss on sale of machine:** WDV = 80 − 30 = 50; Sale = 40 → **Loss ₹10 lakh** (non-cash, add back).

**WN-5 — Goodwill amortised:** 60 − 40 = **₹20 lakh** (non-cash, add back).

**WN-6 — Tax paid:** Provision opening 40 + charge 45 − closing 50 = **₹35 lakh.**

**WN-7 — Share issue proceeds:** Capital ↑100 + Securities premium ↑30 = **₹130 lakh.**

**Cash Flow Statement for the year ended 31 March 2026 (Indirect Method) (₹ in lakh)**

| Particulars | Amount | Total |
|---|---:|---:|
| **A. Operating Activities** | | |
| Net profit before tax (WN-1) | 145 | |
| Add: Depreciation | 80 | |
| Add: Goodwill amortised | 20 | |
| Add: Loss on sale of machine | 10 | |
| Add: Interest on debentures (financing) | 18 | |
| Less: Dividend received (investing) | (8) | |
| Operating profit before working-capital changes | 265 | |
| Increase in inventory | (40) | |
| Increase in trade receivables | (40) | |
| Increase in trade payables | 20 | |
| Increase in warranty provision | 8 | |
| Cash generated from operations | 213 | |
| Less: Tax paid (WN-6) | (35) | |
| **Net cash from operating activities** | | **178** |
| **B. Investing Activities** | | |
| Purchase of PPE (WN-3) | (280) | |
| Sale of machine | 40 | |
| Purchase of investments (140−100) | (40) | |
| Dividend received | 8 | |
| **Net cash used in investing activities** | | **(272)** |
| **C. Financing Activities** | | |
| Proceeds of share issue (WN-7) | 130 | |
| Redemption of debentures | (50) | |
| Interest paid | (18) | |
| Dividend paid | (40) | |
| **Net cash from financing activities** | | **22** |
| **Net decrease in cash (A+B+C)** | | **(72)** |
| Add: Opening cash & equivalents | | 150 |
| **Closing cash & equivalents** | | **78** |

**Answer:** Net cash — operating ₹178 lakh; investing ₹(272) lakh; financing ₹22 lakh; net decrease ₹72 lakh; closing cash ₹78 lakh (reconciles with Balance Sheet).

**Why this way (the reasoning):** The indirect method starts from PBT — *not* PAT — because tax is shown separately as an operating outflow at actual cash paid, and starting from PAT would understate operating profit and double-count tax. Every non-cash and mis-classified item embedded in PBT is reversed: depreciation, goodwill amortisation and loss on sale are non-cash charges, so they are added back; interest on debentures is added back because it belongs in *financing*, and dividend received is deducted because it belongs in *investing* — otherwise the same rupee appears in two sections. Working-capital changes convert accrual profit to cash: a rise in inventory/receivables locks up cash (outflow), a rise in payables/provisions defers cash (inflow). The tempting error is to net "purchases" from the change in gross PPE (200) and forget that ₹80 of assets *left* via sale — that gives ₹120 instead of the true ₹280 cash purchase. Reconstructing each account (WN-2, WN-3, WN-6) is what makes the statement tie exactly.

*(Full-marks tip: examiners reward correct **reclassification** of interest and dividends out of operating, and reconstruction of the fixed-asset, provision-for-tax and surplus accounts. Marks are lost for netting PPE without adjusting for the disposal, for treating proposed/paid dividend as operating, and for a closing-cash figure that does not tie to the Balance Sheet.)*

---

### Q36. Ch: AS 3 Cash Flow Statements — Classification of Interest, Dividends & Taxes (Marks: 6) [Theory]
**Question:** "AS 3 does not permit an enterprise total freedom in classifying interest and dividends." In light of AS 3, examine: (a) how interest and dividends **paid** and **received** are classified by a *financial* enterprise versus a *non-financial* enterprise, and why the standard distinguishes them; (b) the classification of **cash flows arising from taxes on income**; and (c) whether cash flows can be netted, giving the exception.

**Answer:**
**(a) Interest and dividends.** AS 3 requires that such flows be classified consistently from period to period, but the classification itself depends on the *nature of the enterprise's business*:
- For a **financial enterprise** (bank, NBFC), interest paid and interest & dividends received are **operating** cash flows, because lending and investing *are* its principal revenue-producing activities.
- For a **non-financial (other) enterprise**, interest and dividends **received** are **investing** cash flows (return on investments made), while interest and dividends **paid** are **financing** cash flows (cost of obtaining finance). AS 3 permits interest/dividend paid to alternatively be shown under operating only where that reflects the entity's judgement, but the common Indian practice and Study-Material position is financing for paid and investing for received.

**(b) Taxes on income.** Cash flows arising from income taxes are separately disclosed and classified as **operating** activities, *unless* they can be specifically identified with financing or investing activities (e.g., capital-gains tax on sale of an asset — investing). The default is operating because tax arises predominantly on trading results.

**(c) Netting.** Cash flows are generally reported **gross** (major classes of gross receipts and gross payments), because netting hides the scale of activity. Exception: flows may be reported **net** where they reflect the activities of the customer rather than the enterprise (e.g., rents collected on behalf of owners) or where turnover is quick, amounts large and maturities short (e.g., roll-over of short-term borrowings).

**Conclusion:** The enterprise has *no* free choice — classification is dictated by the nature of the business (financial vs other) and by the source of the flow, applied consistently each year.

**Why this way (the reasoning):** The logic is "classify by the activity that *generates* the flow." For a bank, interest is the equivalent of a manufacturer's sales revenue, so it is operating; for a manufacturer, interest received is merely a return on idle-fund investment, so it is investing. This preserves the analytical value of the three sections — a reader comparing two manufacturers can trust that "cash from operations" excludes financing costs. The tempting mistake is to think interest paid is "operating because it hits the P&L"; but *where it hits the P&L* is irrelevant to AS 3 — the standard classifies by economic activity, not by accounting presentation.

*(Full-marks tip: the examiner wants the explicit financial-vs-non-financial contrast with a reason, the "unless identifiable with financing/investing" qualifier on tax, and both netting exceptions. Bare one-word classifications without the *why* lose half the marks.)*

---

### Q37. Ch: AS 3 Cash Flow Statements — Investing Cash Flows with Non-Cash & Revaluation Traps (Marks: 8) [Problem]
**Question:** From the following, compute **Cash Flow from Investing Activities** of Nirmiti Ltd. for the year ended 31 March 2026 as per AS 3, clearly excluding non-cash transactions.

| Particulars | ₹ |
|---|---:|
| PPE (gross) — opening | 40,00,000 |
| PPE (gross) — closing | 55,00,000 |
| Upward revaluation of land included in closing PPE | 5,00,000 |
| Plant acquired by issue of equity shares (non-cash) | 3,00,000 |
| Machine sold (original cost ₹4,00,000; accumulated depreciation ₹1,50,000) | for 2,00,000 |
| Depreciation charged for the year | 6,00,000 |
| Purchase of 8% Government securities (investment) | 7,00,000 |
| Interest received on Government securities | 56,000 |
| Dividend received on shares held | 40,000 |

**Solution:**

**WN-1 — Cash purchase of PPE (reconstruct gross block):**
Opening 40,00,000 + Revaluation 5,00,000 (non-cash) + Share-financed plant 3,00,000 (non-cash) + Cash purchases (X) − Cost of asset sold 4,00,000 = Closing 55,00,000.
40,00,000 + 5,00,000 + 3,00,000 + X − 4,00,000 = 55,00,000 → **X = ₹11,00,000.**

**WN-2 — Profit/loss on sale (memo only):** WDV = 4,00,000 − 1,50,000 = 2,50,000; sold for 2,00,000 → loss ₹50,000. (Affects operating add-back, not the investing section — only the ₹2,00,000 proceeds appear here.)

**Statement of Cash Flow from Investing Activities (₹)**

| Particulars | Amount |
|---|---:|
| Purchase of PPE — cash (WN-1) | (11,00,000) |
| Proceeds from sale of machine | 2,00,000 |
| Purchase of 8% Government securities | (7,00,000) |
| Interest received on securities | 56,000 |
| Dividend received on shares | 40,000 |
| **Net cash used in investing activities** | **(15,04,000)** |

**Answer:** Net cash used in Investing Activities = **₹15,04,000.** The revaluation (₹5,00,000) and the plant bought by share issue (₹3,00,000) are **excluded** — they are non-cash and are disclosed by way of note.

**Why this way (the reasoning):** AS 3 reports only *cash* movements, so the gross block must be "peeled" of every non-cash change before backing out the cash purchase. Revaluation inflates the asset with no cash leaving the firm; a plant bought by issuing shares is simultaneously an investing purchase and a financing issue with zero net cash — AS 3 orders both to be kept out of the statement and disclosed separately so the statement is not distorted. The classic trap is to compute purchases as "closing − opening = 15,00,000" and stop; that silently bundles ₹5,00,000 revaluation and ₹3,00,000 share-financed plant into cash and ignores the ₹4,00,000 disposal, overstating the outflow. Interest and dividend *received* sit in investing (Nirmiti is a non-financial entity — see Q36), so they belong here, netting the outflow down.

*(Full-marks tip: reward for reconstructing the gross block and for explicitly excluding both non-cash items with a note. Deductions for putting the ₹50,000 loss in the investing section, and for classifying interest/dividend received as operating.)*

---

### Q38. Ch: AS 3 Cash Flow Statements — Classification & Cash-Equivalent Judgements (Marks: 5) [Case/Application]
**Question:** For each of the following, state and justify the correct AS 3 treatment: (i) a bank overdraft repayable on demand that forms an integral part of cash management; (ii) short-term highly liquid investment in a 2-month treasury bill; (iii) equity investment in another listed company; (iv) cash paid to acquire a **subsidiary**, net of cash acquired; (v) an insurance claim received for loss of stock by fire.

**Answer:**
**(i) Bank overdraft repayable on demand:** Included as a **component of cash and cash equivalents** (negative), *not* a financing flow — because such overdrafts, forming an integral part of the enterprise's cash management, fluctuate between positive and overdrawn and behave like the cash balance itself.
**(ii) 2-month treasury bill:** A **cash equivalent** — it is short-term, highly liquid, readily convertible into a known amount of cash and subject to insignificant risk of change in value (original maturity ≤ 3 months). Its purchase/redemption is not shown as an investing flow.
**(iii) Equity investment in a listed company:** **Not** a cash equivalent (equity carries significant price risk); the cash paid is an **investing** cash flow.
**(iv) Acquisition of a subsidiary:** The aggregate cash paid **net of cash and cash equivalents acquired** is classified as a single line under **investing activities**, and the total consideration with the portion discharged in cash is disclosed.
**(v) Insurance claim for stock destroyed:** An **operating** cash inflow, because the loss related to inventory — a trading asset. (Had the claim been for a fixed asset, it would be investing.)

**Conclusion:** Classification follows the *nature and liquidity* of each item, not its label.

**Why this way (the reasoning):** The dividing line for a cash equivalent is *purpose plus maturity plus insignificant risk* — held to meet short-term commitments, not for investment. A 2-month T-bill qualifies; equity never does, however liquid, because its value can swing. The overdraft rule recognises economic reality: if a firm sweeps cash and overdraft together to manage liquidity, treating the overdraft as "borrowing" would misstate both financing flows and the true cash position. The subsidiary rule nets acquired cash so the statement shows the *real* cash given up to gain control. And the insurance claim inherits the character of the asset lost — matching the flow to the activity that produced it, the same principle running through all AS 3 classification.

*(Full-marks tip: each answer must pair the classification with the deciding criterion — maturity/risk for equivalents, "integral to cash management" for the overdraft, "net of cash acquired" for the subsidiary. Naming the section without the justification earns only partial credit.)*

---

### Q39. Ch: Redemption of Preference Shares — Minimum Fresh Issue with Cash & CRR Constraints (Marks: 10) [Problem]
**Question:** The Balance Sheet of Aadhar Ltd. shows: 10,000 12% Redeemable Preference Shares of ₹100 each (fully paid), redeemable at a premium of 10%; Securities Premium ₹1,20,000; General Reserve ₹4,00,000; Surplus (P&L) ₹1,50,000; Capital Reserve (unrealised) ₹50,000; Bank ₹5,00,000. The company must redeem the preference shares and wishes to make the **minimum fresh issue of equity shares of ₹10 each at par**, while retaining a **minimum bank balance of ₹1,00,000** after redemption. Determine the minimum fresh issue and pass journal entries.

**Solution:**

**WN-1 — Cash required for redemption:** Face ₹10,00,000 + Premium 10% ₹1,00,000 = **₹11,00,000.**

**WN-2 — Own cash usable:** Bank ₹5,00,000 − minimum retention ₹1,00,000 = **₹4,00,000.**

**WN-3 — Minimum fresh issue (cash constraint binds):** Cash shortfall = 11,00,000 − 4,00,000 = **₹7,00,000.** At ₹10 par → **70,000 equity shares.**

**WN-4 — Check the reserves/CRR constraint:** Free reserves available for CRR = General Reserve ₹4,00,000 + Surplus ₹1,50,000 = ₹5,50,000. (Securities Premium and *unrealised* Capital Reserve are **not** free reserves.) Face value not covered by fresh issue = 10,00,000 − 7,00,000 = ₹3,00,000 → CRR needed ₹3,00,000 ≤ ₹5,50,000 available. **Feasible.** So the cash constraint (₹7,00,000) governs, not the reserve limit (which alone would need only ₹4,50,000 fresh issue).

**WN-5 — Premium on redemption ₹1,00,000** is provided out of **Securities Premium** (₹1,20,000 available).

**Journal Entries (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| Bank A/c ................ Dr | 7,00,000 | |
| &nbsp;&nbsp;To Equity Share Capital A/c | | 7,00,000 |
| *(Fresh issue of 70,000 equity shares of ₹10 at par)* | | |
| 12% Preference Share Capital A/c ...... Dr | 10,00,000 | |
| Premium on Redemption of Pref. Shares A/c ... Dr | 1,00,000 | |
| &nbsp;&nbsp;To Preference Shareholders A/c | | 11,00,000 |
| *(Amount due on redemption at 10% premium)* | | |
| Securities Premium A/c ...... Dr | 1,00,000 | |
| &nbsp;&nbsp;To Premium on Redemption of Pref. Shares A/c | | 1,00,000 |
| *(Premium on redemption provided out of securities premium)* | | |
| Preference Shareholders A/c ...... Dr | 11,00,000 | |
| &nbsp;&nbsp;To Bank A/c | | 11,00,000 |
| *(Payment to preference shareholders)* | | |
| General Reserve A/c ...... Dr | 3,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 3,00,000 |
| *(Nominal value redeemed out of profits transferred to CRR)* | | |

**Verification of Bank:** 5,00,000 + 7,00,000 (fresh) − 11,00,000 (paid) = **₹1,00,000** (matches required retention).

**Answer:** Minimum fresh issue = **70,000 equity shares of ₹10 = ₹7,00,000**; CRR = **₹3,00,000**; premium on redemption ₹1,00,000 met from securities premium.

**Why this way (the reasoning):** Two independent constraints govern the fresh issue and the answer is the *larger* of the two. (1) The **capital-maintenance / CRR rule** (Sec 55): every rupee of face value redeemed out of profits must be locked away in CRR so that shareholders' funds are not depleted — this caps redemption-out-of-profits at available free reserves (₹5,50,000), forcing at least ₹4,50,000 of fresh capital. (2) The **cash-availability constraint**: the company can only spare ₹4,00,000 of its own cash, so ₹7,00,000 of cash must be raised. Since ₹7,00,000 > ₹4,50,000, the cash need is binding. A student who solves only the reserve test gets ₹4,50,000 and is wrong, because there would then be insufficient cash to actually pay the shareholders. Note the two "premium" pools are distinct: securities premium can absorb the *premium on redemption* but can **never** be used to create CRR (it is not a free reserve). Capital Reserve is excluded because it is unrealised — CRR must be backed by realised, distributable profit that is being sterilised.

*(Full-marks tip: the examiner rewards testing *both* constraints and taking the higher, plus correctly excluding securities premium and unrealised capital reserve from free reserves. Common deductions: using securities premium to fund CRR, ignoring the cash constraint, and forgetting to verify the closing bank against the retention.)*

---

### Q40. Ch: Redemption of Preference Shares — "Proceeds of Fresh Issue of Shares" vs Debentures (Marks: 8) [Problem]
**Question:** Sthir Ltd. redeems 20,000 10% Preference Shares of ₹100 each (fully paid) at par. To finance the redemption it (a) issues 5,000 11% Preference Shares of ₹100 each at par, (b) issues 10% Debentures of ₹8,00,000, and (c) uses reserves/cash for the balance. Its General Reserve is ₹15,00,000. Determine the amount to be transferred to Capital Redemption Reserve, and pass the entry for the CRR transfer with reasoning. Also state the cash arranged.

**Solution:**

**WN-1 — Face value redeemed:** 20,000 × ₹100 = **₹20,00,000.**

**WN-2 — "Proceeds of a fresh issue of shares" (Sec 55):** Only proceeds of a fresh issue of **shares** reduce the CRR requirement. New 11% Preference Shares ₹5,00,000 **qualify**; the ₹8,00,000 **debentures do NOT** (debentures are borrowings, not shares).
→ Portion treated as redeemed **out of profits** = 20,00,000 − 5,00,000 = **₹15,00,000.**

**WN-3 — CRR transfer = ₹15,00,000** (from General Reserve, which is exactly ₹15,00,000 → reduced to nil).

**WN-4 — Cash arranged:** Fresh preference issue ₹5,00,000 + Debentures ₹8,00,000 = ₹13,00,000; balance ₹7,00,000 from existing bank → total ₹20,00,000 paid to old preference shareholders.

**Journal Entry (CRR) (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| General Reserve A/c ...... Dr | 15,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 15,00,000 |
| *(Nominal value of preference shares redeemed otherwise than out of proceeds of a fresh issue of shares, transferred to CRR)* | | |

**Answer:** Amount transferred to CRR = **₹15,00,000.** Fresh preference-share proceeds of ₹5,00,000 reduce the CRR requirement; the ₹8,00,000 debentures do **not**.

**Why this way (the reasoning):** Section 55 permits redemption "out of profits" or "out of the proceeds of a fresh issue of shares," and requires CRR only for the part *not* met by a fresh issue of shares. The economic idea is capital maintenance: when new **share capital** replaces the redeemed shares, permanent capital is preserved and no CRR is needed for that slice; but when redemption is funded from distributable profits (or from *borrowings*), those profits must be frozen in CRR so they can never be paid out as dividend — otherwise creditors' cushion would shrink. Debentures are debt, not permanent capital, so financing redemption with debentures is, in substance, redemption "out of profits/other sources," and the full ₹15,00,000 gap must go to CRR. The trap is to net *all* ₹13,00,000 of financing (including debentures) against the face value and wrongly compute CRR of ₹7,00,000.

*(Full-marks tip: examiners specifically test whether the student knows debenture proceeds do **not** count as "proceeds of a fresh issue of shares." State that phrase verbatim. Deduction for reducing CRR by the debenture amount.)*

---

### Q41. Ch: Redemption of Preference Shares — Rationale of CRR & Sourcing of Premium (Marks: 6) [Theory]
**Question:** (a) Explain the purpose of the **Capital Redemption Reserve** and why Section 55 mandates its creation, and state the permitted use of the CRR. (b) A company redeems preference shares at a premium. From which account may the **premium on redemption** be provided, and does the answer differ for a company whose financial statements comply with the notified Accounting Standards under Section 133? Give reasons.

**Answer:**
**(a) Purpose of CRR.** When preference shares are redeemed out of divisible profits, cash leaves the company and share capital is extinguished — this would reduce the "capital" that acts as a cushion for creditors. Section 55(2) therefore requires that a sum equal to the **nominal value of shares redeemed out of profits** be transferred from free reserves to the **Capital Redemption Reserve**. The CRR is treated as though it were **paid-up share capital**: it can *only* be applied in **paying up unissued shares to be issued as fully paid bonus shares**. This effectively converts distributable profit into non-distributable "quasi-capital," so redemption does not become a backdoor return of capital to shareholders that bypasses creditor protection.

**(b) Premium on redemption.** Section 55(2) allows the premium payable on redemption to be provided out of the **profits of the company** or out of the **Securities Premium Account**. **However**, for a company whose financial statements comply with the Accounting Standards notified under Section 133, the premium on redemption must be provided **out of the profits** of the company **before** the shares are redeemed (the securities-premium route is restricted for such companies). For companies not so covered, either source is available.

**Conclusion:** CRR protects capital and is usable only for bonus shares; premium sourcing depends on whether the company follows notified AS.

**Why this way (the reasoning):** The whole redemption regime rests on **capital maintenance** — creditors extend credit relying on the buffer of paid-up capital, so the law will not let that buffer silently erode when shares are cancelled. CRR is the mechanism: it re-labels an equal amount of *distributable* profit as *undistributable*, so total "locked-in" funds are unchanged. Limiting CRR's use to bonus shares keeps it permanently as capital. On premium, the restriction for AS-compliant companies reflects a stricter, prudence-driven view — securities premium is a capital receipt and the standard-setters prefer that the *cost* of redemption (the premium) be borne by trading profits, keeping the securities premium intact for its own statutory uses.

*(Full-marks tip: state the CRR = nominal value redeemed out of profits, the "only for bonus shares" use, and the AS-compliant-company premium restriction with the "before redemption / out of profits" wording. Vague "reserve for redemption" answers lose marks.)*

---

### Q42. Ch: Redemption of Preference Shares — Maximum Redeemable Out of Profits (Marks: 5) [Problem]
**Question:** Sulabh Ltd. has 8,000 9% Preference Shares of ₹100 each (fully paid) that it wishes to redeem at par **entirely out of profits** (no fresh issue). Its reserves are: General Reserve ₹3,00,000; Surplus (P&L) ₹1,50,000; Securities Premium ₹80,000; Revaluation Reserve ₹60,000; Dividend Equalisation Reserve ₹70,000. Determine the maximum face value of preference shares the company can redeem out of profits, and whether a full redemption is possible.

**Solution:**

**WN-1 — Free (distributable) reserves usable for CRR:** General Reserve ₹3,00,000 + Surplus ₹1,50,000 + Dividend Equalisation Reserve ₹70,000 = **₹5,20,000.** *Excluded:* Securities Premium (statutory, not free) and Revaluation Reserve (unrealised).

**WN-2 — Redemption out of profits requires CRR = face value redeemed.** Maximum face value redeemable out of profits = free reserves available = **₹5,20,000.**

**WN-3 — Full redemption needed:** 8,000 × ₹100 = ₹8,00,000 > ₹5,20,000.
Shortfall = 8,00,000 − 5,20,000 = **₹2,80,000.**

**Answer:** Maximum redeemable out of profits = **₹5,20,000** (i.e., 5,200 shares). Full redemption of ₹8,00,000 is **NOT possible** out of profits alone; the company must make a **fresh issue of shares of at least ₹2,80,000** to redeem the balance.

**Why this way (the reasoning):** Redemption "out of profits" is limited by the CRR rule — every rupee of face value so redeemed must be matched by a rupee moved into CRR from *free* reserves, so the maximum equals the pool of free reserves. Securities premium and revaluation reserve are excluded because they are not distributable profits available for CRR: securities premium is capital in nature and ring-fenced for specific uses, and revaluation reserve represents unrealised gains. The common error is to lump all five reserves (₹6,60,000) and conclude full redemption is possible — that overstates capacity by ₹1,40,000 and ignores the character of the reserves.

*(Full-marks tip: correctly separating *free* from statutory/unrealised reserves is the whole question. State the ₹2,80,000 shortfall must be met by a fresh **issue of shares**. Including securities premium or revaluation reserve in the CRR pool is the standard deduction.)*

---

### Q43. Ch: Redemption of Preference Shares — Redemption Followed by Bonus Issue from CRR (Marks: 8) [Problem]
**Question:** Punarva Ltd. redeems 5,000 8% Preference Shares of ₹100 each (fully paid) at par, **wholly out of profits** (General Reserve ₹9,00,000). Immediately after redemption, the company issues fully paid **bonus equity shares** to existing members, utilising the **entire Capital Redemption Reserve** so created plus ₹2,00,000 of its **Securities Premium** balance. Pass the journal entries for (i) redemption, (ii) CRR creation, and (iii) the bonus issue.

**Solution:**

**WN-1 — Redemption:** Face value = 5,000 × ₹100 = **₹5,00,000**, at par, wholly out of profits → cash paid ₹5,00,000; CRR to be created = **₹5,00,000.**

**WN-2 — Bonus issue funded by:** CRR ₹5,00,000 + Securities Premium ₹2,00,000 = **₹7,00,000** of fully paid bonus equity shares.

**Journal Entries (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| 8% Preference Share Capital A/c ...... Dr | 5,00,000 | |
| &nbsp;&nbsp;To Preference Shareholders A/c | | 5,00,000 |
| *(Amount due on redemption at par)* | | |
| Preference Shareholders A/c ...... Dr | 5,00,000 | |
| &nbsp;&nbsp;To Bank A/c | | 5,00,000 |
| *(Payment to preference shareholders)* | | |
| General Reserve A/c ...... Dr | 5,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 5,00,000 |
| *(Nominal value redeemed out of profits transferred to CRR)* | | |
| Capital Redemption Reserve A/c ...... Dr | 5,00,000 | |
| Securities Premium A/c ...... Dr | 2,00,000 | |
| &nbsp;&nbsp;To Bonus to Shareholders A/c | | 7,00,000 |
| *(Bonus declared out of CRR and securities premium)* | | |
| Bonus to Shareholders A/c ...... Dr | 7,00,000 | |
| &nbsp;&nbsp;To Equity Share Capital A/c | | 7,00,000 |
| *(70,000 bonus equity shares of ₹10 each issued as fully paid)* | | |

**Answer:** CRR of ₹5,00,000 is created and then fully applied, together with ₹2,00,000 securities premium, to issue **₹7,00,000 of fully paid bonus shares**.

**Why this way (the reasoning):** CRR is legally treated as paid-up capital, and the *one* permitted use of CRR is to pay up unissued shares issued as **fully paid bonus shares** — so channelling it straight into a bonus issue is entirely valid and does not violate capital maintenance, because the money simply moves from one form of non-distributable capital (CRR) to another (share capital). Securities Premium is likewise a permitted source for fully paid bonus shares under Section 52. The sequence matters: CRR can only be applied *after* it has been created on redemption; issuing bonus shares from reserves that could otherwise pay dividends would defeat the sterilisation the CRR achieved. The reason bonus is used to *pay up unissued shares* (not to issue at a discount or in cash) is that a bonus capitalises reserves permanently — no cash leaves and creditor cover is untouched.

*(Full-marks tip: show the "Bonus to Shareholders" intermediary account and use only CRR/securities premium (both permissible) — never general reserve for the bonus in this fact pattern would be *also* allowed but the question fixes the sources. Deduction for using CRR for anything other than fully paid bonus shares.)*

---

### Q44. Ch: Redemption of Preference Shares — Partly Paid Shares & Order of Steps (Marks: 6) [Case/Application]
**Question:** Drdha Ltd. proposes to redeem, on 1 April 2026, its 10,000 7% Preference Shares of ₹100 each on which **₹90 per share is called and paid up** (₹10 uncalled). The Board argues it can redeem immediately by paying ₹90 per share out of profits. Examine the validity of this proposal under Section 55, and advise the correct course of action.

**Answer:**
**Governing principle — Section 55(1)/(2):** Only **preference shares which are fully paid up** may be redeemed. A company cannot redeem shares that are partly paid; redemption presupposes that the shareholder's obligation to the company is complete, so that the transaction is purely a *return* of capital and not a set-off against an unpaid liability.

**Application to facts:** Drdha Ltd.'s shares are paid up only to ₹90; ₹10 per share remains uncalled. In their present state they are **not fully paid** and therefore **cannot be redeemed**. The Board's plan to simply pay ₹90 and redeem is **invalid**.

**Advice — correct course:** The company must **first call up and receive the balance ₹10 per share** (total ₹1,00,000), making the shares fully paid at ₹100. *Then* it may redeem all 10,000 shares at ₹100 each (₹10,00,000), either out of profits (creating CRR of ₹10,00,000) and/or out of the proceeds of a fresh issue of shares. If any shareholder fails to pay the call, those shares may be forfeited before redemption of the remainder.

**Conclusion:** Immediate redemption is not permissible. The correct sequence is: **call up the uncalled ₹10 → collect it → then redeem the now fully paid shares** with the usual CRR/fresh-issue mechanics.

**Why this way (the reasoning):** The "fully paid" precondition exists so that redemption is an unambiguous return of *contributed* capital, not a device to write off amounts still owed by shareholders. If a partly paid share could be redeemed, the company would be handing cash back to a member who has not yet given the company all it promised — mixing a capital return with debt forgiveness and eroding the capital base. Hence the law forces the company to complete the capital contribution first (make the share fully paid), restoring the clean logic of "capital in, then capital out with CRR replacement." Paying only ₹90 would also miscompute CRR, which must rest on the **nominal (face) value** of ₹100, not the amount paid.

*(Full-marks tip: cite the "fully paid" requirement of Sec 55, declare the proposal invalid, and give the two-step remedy (call up, then redeem). Note CRR is on face value ₹100. Answers that permit redeeming the partly paid share lose the core mark.)*

---

### Q45. Ch: Buy-back of Securities — Maximum Buy-Back: Three-Test Determination (Marks: 10) [Problem]
**Question:** Samartha Ltd. is considering a buy-back of its equity shares at **₹25 per share** (face value ₹10). Its relevant balances are: Paid-up equity capital ₹12,00,000 (1,20,000 shares of ₹10); General Reserve ₹8,00,000; Surplus (P&L) ₹4,00,000; Securities Premium ₹3,00,000; Secured + Unsecured loans ₹46,00,000. Applying all the tests of Section 68, determine the **maximum number of shares** the company can buy back (assume a special resolution is passed), and the amount to be transferred to CRR.

**Solution:**

**WN-1 — Shareholders' funds:** Paid-up capital ₹12,00,000 + Free reserves (Gen. Res. 8,00,000 + P&L 4,00,000 + Securities Premium 3,00,000 = ₹15,00,000) = **₹27,00,000.**

**WN-2 — Test 1: Shares Outstanding (Quantity) Test.** Maximum = 25% of paid-up equity capital = 25% × 1,20,000 shares = **30,000 shares.**

**WN-3 — Test 2: Resources Test.** Maximum amount = 25% of (paid-up capital + free reserves) = 25% × ₹27,00,000 = **₹6,75,000.** At ₹25/share → 6,75,000 ÷ 25 = **27,000 shares.**

**WN-4 — Test 3: Debt-Equity (Post-Buy-back) Test.** After buy-back, total debt must not exceed **2 ×** (paid-up capital + free reserves remaining).
Minimum funds to be maintained = Debt ÷ 2 = ₹46,00,000 ÷ 2 = ₹23,00,000.
Maximum permissible reduction in owners' funds = 27,00,000 − 23,00,000 = **₹4,00,000.**
Maximum shares = 4,00,000 ÷ 25 = **16,000 shares.**

**WN-5 — Maximum buy-back = lowest of the three tests** = lower of (30,000 ; 27,000 ; 16,000) = **16,000 shares.**

**Statement of Maximum Buy-Back**

| Test | Ceiling (shares) |
|---|---:|
| Shares outstanding test (25% of equity nos.) | 30,000 |
| Resources test (₹6,75,000 ÷ ₹25) | 27,000 |
| Debt-equity test (₹4,00,000 ÷ ₹25) | **16,000** ← binding |
| **Maximum permissible buy-back** | **16,000** |

**WN-6 — CRR on buy-back:** Nominal value of shares bought back (out of free reserves/securities premium) = 16,000 × ₹10 = **₹1,60,000** to be transferred to CRR.

**Answer:** Maximum buy-back = **16,000 shares** (amount ₹4,00,000); the **debt-equity test is the binding constraint**; CRR = **₹1,60,000.**

**Why this way (the reasoning):** Section 68 imposes three *independent* ceilings and the permissible buy-back is the **most restrictive** of them, because all three protect different interests simultaneously. The quantity test (25% of shares) prevents an excessive contraction of the shareholder base in one year; the resources test (25% of net worth by *amount*) ensures the company does not deplete more than a quarter of owners' funds; the debt-equity test guards **creditors** by forcing post-buy-back debt to stay within twice the reduced net worth. Here the firm is highly geared (₹46,00,000 debt), so even a small buy-back threatens the 2:1 cap — that is why the debt-equity test bites first at only 16,000 shares, far below the 27,000/30,000 the other tests would allow. The student's instinct to pick the *highest* number, or to stop at the quantity test, is exactly the trap: you must compute all three and take the **minimum**. CRR is then created for the face value bought back, mirroring the redemption logic — capital extinguished must be replaced by a non-distributable reserve.

*(Full-marks tip: examiners award marks test-by-test and specifically for identifying the *binding* constraint and taking the minimum. Include securities premium within the resources-test net worth, and remember CRR is on **face value**, not buy-back price. Deductions for taking the highest test or omitting the debt-equity test.)*

---

### Q46. Ch: Buy-back of Securities — Full Journal Entries & Sources (Marks: 8) [Problem]
**Question:** Utkarsh Ltd. buys back **20,000 equity shares of ₹10 each at ₹15 per share**. Before buy-back it has: Securities Premium ₹1,50,000; General Reserve ₹6,00,000; Surplus (P&L) ₹2,00,000; adequate bank balance. The company decides to use securities premium to the maximum extent for the premium payable on buy-back, and free reserves for the balance and for CRR. Pass all journal entries for the buy-back.

**Solution:**

**WN-1 — Amounts:** Total payout = 20,000 × ₹15 = **₹3,00,000.** Of this, nominal ₹2,00,000 (20,000 × ₹10) and premium ₹1,00,000 (20,000 × ₹5).

**WN-2 — Premium on buy-back ₹1,00,000** met fully from **Securities Premium** (₹1,50,000 available).

**WN-3 — CRR** = nominal value bought back = **₹2,00,000**, transferred from free reserves (General Reserve).

**Journal Entries (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| Equity Share Capital A/c ...... Dr | 2,00,000 | |
| Securities Premium A/c ...... Dr | 1,00,000 | |
| &nbsp;&nbsp;To Equity Shareholders (Buy-back) A/c | | 3,00,000 |
| *(Amount due on buy-back of 20,000 shares at ₹15, premium met from securities premium)* | | |
| Equity Shareholders (Buy-back) A/c ...... Dr | 3,00,000 | |
| &nbsp;&nbsp;To Bank A/c | | 3,00,000 |
| *(Payment to shareholders on buy-back)* | | |
| General Reserve A/c ...... Dr | 2,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 2,00,000 |
| *(Nominal value of shares bought back transferred to CRR out of free reserves)* | | |

**Answer:** Bank outflow ₹3,00,000; premium ₹1,00,000 absorbed by securities premium; CRR created ₹2,00,000 from general reserve.

**Why this way (the reasoning):** Two capital adjustments happen on buy-back. First, the *payment*: the shares' face value (₹2,00,000) is cancelled against Equity Share Capital and the excess paid (the ₹1,00,000 premium) is charged against a permitted source — Securities Premium is preferred because Section 52/68 expressly allow it and it preserves distributable free reserves. Second, the *capital-maintenance* step under Section 69: because the buy-back is financed from free reserves/securities premium (not fresh issue), a sum equal to the **nominal value** bought back must be parked in CRR, replacing the extinguished capital with a non-distributable reserve so creditors' cushion is intact. Students often forget the CRR entry, or wrongly compute CRR on ₹3,00,000 (the total payout) instead of ₹2,00,000 (face value) — CRR mirrors only the capital cancelled, never the premium.

*(Full-marks tip: three entries — cancellation (charging premium to securities premium), payment, and CRR on face value. Deductions for CRR on total consideration, or charging the buy-back premium to CRR.)*

---

### Q47. Ch: Buy-back of Securities — Conditions, Prohibitions & CRR Rationale (Marks: 6) [Theory]
**Question:** (a) State the key **conditions** a company must satisfy under Section 68 to buy back its own shares, and the **sources** from which buy-back may be financed. (b) Under Section 70, name **two** circumstances in which a company is **prohibited** from buying back its shares. (c) Explain why the Act bars buy-back "out of the proceeds of an earlier issue of the **same kind** of shares."

**Answer:**
**(a) Conditions (Sec 68).** (i) Buy-back must be **authorised by the articles**; (ii) a **special resolution** (or Board resolution for up to 10% of paid-up equity + free reserves) is passed; (iii) buy-back does not exceed **25% of aggregate paid-up capital and free reserves** (and, for equity, 25% of paid-up equity in a financial year); (iv) post-buy-back **debt-equity ratio ≤ 2:1**; (v) all shares are **fully paid up**; (vi) buy-back is **completed within one year** of the resolution; and (vii) a **gap of one year** between two buy-backs.
**Sources:** buy-back may be financed only out of (1) **free reserves**, (2) **securities premium account**, or (3) **proceeds of a fresh issue of shares** (not an issue of the same kind of shares).

**(b) Prohibitions (Sec 70).** A company must **not** buy back its shares (i) through any **subsidiary** company or through **investment companies**; or (ii) if it has **defaulted** in repayment of deposits/interest, redemption of debentures/preference shares, payment of dividend, or repayment of a term loan (unless the default has been remedied and three years have elapsed). *(Also: not if it has not complied with Sec 92/123/127/129.)*

**(c) Bar on "same kind" proceeds.** Buy-back cannot be financed out of the proceeds of an *earlier issue of the same kind of shares* because that would be a purely circular transaction — issuing equity only to immediately repurchase equity — which manipulates the share count and capital structure without any real inflow, defeating the purpose and protections of the buy-back regime.

**Why this way (the reasoning):** The conditions and prohibitions together enforce two themes — **creditor protection** and **anti-abuse**. The 25% and 2:1 caps and the CRR requirement ensure buy-back cannot hollow out the capital that secures creditors; the "fully paid," one-year-gap and Section 70 default rules stop a company in financial distress from returning cash to members ahead of creditors. The "same kind of shares" bar closes an obvious loophole: without it, a company could churn equity in and out to prop up EPS or share price using its own recycled capital. Requiring CRR for the free-reserve/securities-premium-funded portion (Sec 69) is the capital-maintenance backbone — capital cancelled is replaced by an equal, undistributable reserve.

*(Full-marks tip: quote the numeric limits (25%, 2:1, one year) and at least two Section 70 prohibitions precisely. The "circular transaction" reasoning for part (c) is what distinguishes a top answer.)*

---

### Q48. Ch: Buy-back of Securities — Debt-Equity Ceiling Single-Test (Marks: 5) [Problem]
**Question:** After a proposed buy-back, Vega Ltd. will have paid-up capital plus free reserves of ₹40,00,000 (post-buy-back) and total borrowings of ₹90,00,000. A director claims the buy-back is permissible. Examine compliance with the **debt-equity test** of Section 68, and state the maximum borrowings that would keep the buy-back valid at that level of owners' funds. If instead borrowings are fixed at ₹90,00,000, what minimum owners' funds must remain?

**Solution:**

**WN-1 — Debt-equity condition:** Post-buy-back total secured + unsecured debt must not exceed **twice** the (paid-up capital + free reserves) after buy-back, i.e., Debt ≤ 2 × Owners' funds.

**WN-2 — Test the claim:** Owners' funds ₹40,00,000 → permitted debt = 2 × 40,00,000 = **₹80,00,000.** Actual debt ₹90,00,000 **> ₹80,00,000** → **ratio 2.25 : 1 > 2 : 1** → the buy-back as proposed is **NOT valid.**

**WN-3 — Maximum borrowings for validity at ₹40,00,000 funds:** = 2 × 40,00,000 = **₹80,00,000** (must reduce debt by ₹10,00,000).

**WN-4 — Minimum owners' funds if debt stays ₹90,00,000:** Owners' funds ≥ Debt ÷ 2 = 90,00,000 ÷ 2 = **₹45,00,000** (i.e., the buy-back must be smaller so that at least ₹45,00,000 of net worth survives).

**Answer:** The claim is **wrong** — at ₹40,00,000 owners' funds the maximum debt is ₹80,00,000, but debt is ₹90,00,000 (2.25:1). Either reduce debt to **₹80,00,000**, or shrink the buy-back so post-buy-back owners' funds stay at least **₹45,00,000.**

**Why this way (the reasoning):** The 2:1 post-buy-back debt-equity cap is a *creditor-protection* limit — buy-back returns cash to shareholders and shrinks net worth, so the Act refuses to let leverage rise beyond twice the reduced equity, ensuring the debt remains adequately covered by owners' funds. The key subtlety is that the test is applied to the **post-buy-back** figures: buy-back simultaneously *reduces* owners' funds (numerator's denominator) while debt is unchanged, so a company already near 2:1 has almost no room. The director's error is checking the ratio before, or ignoring that owners' funds fall as cash goes out.

*(Full-marks tip: apply the test on *post-buy-back* funds, show the 2.25:1 breach, and give both remedies. Using pre-buy-back net worth is the classic deduction.)*

---

### Q49. Ch: Buy-back of Securities — Buy-back Part-Financed by Fresh Issue: CRR Effect (Marks: 8) [Problem]
**Question:** Pragati Ltd. buys back **1,00,000 equity shares of ₹10 each at ₹18 per share**. To part-finance it, the company makes a **fresh issue of 12% Preference Shares of ₹4,00,000 (at par)**; the rest is met from free reserves, securities premium and bank. Securities Premium before buy-back is ₹5,00,000; General Reserve is ₹20,00,000. Determine the amount to be transferred to **CRR**, and pass the journal entries for the fresh issue, the buy-back and the CRR transfer.

**Solution:**

**WN-1 — Buy-back amounts:** Total payout = 1,00,000 × ₹18 = **₹18,00,000.** Face value ₹10,00,000; premium ₹8,00,000 (1,00,000 × ₹8).

**WN-2 — Premium on buy-back ₹8,00,000:** met from Securities Premium ₹5,00,000 + General Reserve (free reserve) ₹3,00,000.

**WN-3 — CRR under Section 69:** CRR is required only for the portion **not** financed by the fresh issue of shares.
Nominal value bought back ₹10,00,000 − proceeds of fresh issue of shares ₹4,00,000 = **CRR ₹6,00,000** (from free reserves).

**Journal Entries (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| Bank A/c ...... Dr | 4,00,000 | |
| &nbsp;&nbsp;To 12% Preference Share Capital A/c | | 4,00,000 |
| *(Fresh issue of preference shares at par to finance buy-back)* | | |
| Equity Share Capital A/c ...... Dr | 10,00,000 | |
| Securities Premium A/c ...... Dr | 5,00,000 | |
| General Reserve A/c ...... Dr | 3,00,000 | |
| &nbsp;&nbsp;To Equity Shareholders (Buy-back) A/c | | 18,00,000 |
| *(Buy-back at ₹18; premium of ₹8,00,000 met from securities premium ₹5,00,000 and general reserve ₹3,00,000)* | | |
| Equity Shareholders (Buy-back) A/c ...... Dr | 18,00,000 | |
| &nbsp;&nbsp;To Bank A/c | | 18,00,000 |
| *(Payment to shareholders)* | | |
| General Reserve A/c ...... Dr | 6,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 6,00,000 |
| *(Nominal value bought back, less proceeds of fresh issue, transferred to CRR)* | | |

**Answer:** CRR = **₹6,00,000** (nominal ₹10,00,000 less fresh-issue proceeds ₹4,00,000). Total General Reserve utilised = ₹3,00,000 (premium) + ₹6,00,000 (CRR) = ₹9,00,000.

**Why this way (the reasoning):** Section 69 requires CRR only where buy-back is made "out of free reserves or securities premium." To the extent the buy-back is funded by a **fresh issue of shares**, fresh permanent capital replaces the cancelled capital, so no CRR is needed for that slice — exactly the mirror of the redemption-of-preference-shares logic. Hence CRR = face value bought back *minus* the fresh-issue proceeds. Note two subtleties: (1) the fresh issue is of **preference** shares to buy back **equity** — permitted, because it is not an issue of the *same kind* of shares (Sec 68); (2) the buy-back **premium** (₹8,00,000) is a separate charge from CRR and is met first from securities premium, then free reserves. The trap is to compute CRR on the full ₹10,00,000 ignoring the fresh issue, or to compute it on the ₹18,00,000 payout.

*(Full-marks tip: reward for CRR = nominal less fresh-issue proceeds, and for noting a preference-share issue validly funds an equity buy-back (not "same kind"). Deductions for CRR on total consideration or ignoring the fresh-issue offset.)*

---

### Q50. Ch: Buy-back of Securities — Examine Validity of a Proposed Buy-Back (Marks: 6) [Case/Application]
**Question:** Ojas Ltd. (articles authorise buy-back) proposes a buy-back and the following facts emerge: (i) it completed an earlier buy-back **8 months ago**; (ii) some of the shares proposed to be bought back are **partly paid** (₹8 paid on ₹10); (iii) the company has **defaulted** in repayment of a term loan to a bank, the default being **subsisting**; and (iv) it intends to route the buy-back **through its wholly-owned subsidiary**. Examine the validity of the proposal under Sections 68 and 70, dealing with each defect.

**Answer:**
**Governing law — Sections 68 & 70.**
**(i) One-year gap (Sec 68):** No offer of buy-back shall be made within a period of **one year** from the date of the closure of the preceding buy-back. Ojas Ltd.'s previous buy-back closed only **8 months ago** → the fresh buy-back is **premature and invalid**; it must wait until one year has elapsed.
**(ii) Partly paid shares (Sec 68):** Only **fully paid** shares can be bought back. Shares on which only ₹8 of ₹10 is paid are partly paid and are **ineligible**; the company must first call up and receive the balance ₹2 before those shares can be included.
**(iii) Default in repayment of term loan (Sec 70):** A company **cannot** buy back its shares while a default in repayment of a term loan to a bank/financial institution is **subsisting**. Since the default continues, buy-back is **prohibited** (it becomes permissible only after the default is remedied and three years have elapsed).
**(iv) Buy-back through subsidiary (Sec 70):** A company must **not** purchase its own shares **through any subsidiary company**, including its own subsidiaries. Routing the buy-back through the wholly-owned subsidiary is **expressly prohibited** and invalid.

**Conclusion:** The proposal is **invalid on all four counts**. Ojas Ltd. must: wait until one year from the last buy-back; make the shares fully paid; **cure the term-loan default** (and observe the three-year condition); and effect the buy-back **directly**, not through its subsidiary.

**Why this way (the reasoning):** Each condition targets a distinct abuse. The one-year gap stops repeated capital contractions that destabilise the capital base and manipulate market price. The "fully paid" rule ensures buy-back is a clean return of *contributed* capital, not a set-off against sums shareholders still owe. The Section 70 default bar embodies the **creditor-priority principle** — a company in default to its lenders cannot lawfully hand cash back to shareholders ahead of the creditors it has failed to pay. The subsidiary bar prevents indirect, opaque repurchases that could disguise the true extent of buy-back and evade the statutory limits. Reading these as protections rather than technicalities is what a top answer shows.

*(Full-marks tip: address **each** of the four defects with the specific Section (68 or 70) and the remedy; a generic "buy-back not allowed" without treating every defect loses marks. Note the "default cured + three years" nuance and that the subsidiary route is barred even for a wholly-owned subsidiary.)*

---

### Q51. Ch: Buy-back of Securities — Comprehensive: Tests, Entries & Balance Sheet After Buy-Back (Marks: 10) [Problem]
**Question:** The summarised Balance Sheet of Tejas Ltd. as at 31 March 2026 is given. The company buys back **60,000 equity shares at ₹20 per share** (special resolution passed; articles permit). Verify that the buy-back satisfies Section 68, pass the journal entries, and prepare the Balance Sheet **immediately after** the buy-back.

**Balance Sheet as at 31 March 2026 (₹)**

| Equity & Liabilities | ₹ | Assets | ₹ |
|---|---:|---|---:|
| Equity share capital (3,00,000 shares of ₹10) | 30,00,000 | Fixed assets | 41,00,000 |
| Securities premium | 6,00,000 | Investments | 10,00,000 |
| General reserve | 14,00,000 | Inventory | 8,00,000 |
| Surplus (P&L) | 5,00,000 | Trade receivables | 9,00,000 |
| 10% Debentures | 20,00,000 | Bank | 15,00,000 |
| Trade payables | 8,00,000 | | |
| **Total** | **83,00,000** | **Total** | **83,00,000** |

**Solution:**

**WN-1 — Compliance with Section 68 (three tests):** Net worth = 30,00,000 + free reserves (6,00,000 + 14,00,000 + 5,00,000 = 25,00,000) = ₹55,00,000. Buy-back = 60,000 × ₹20 = ₹12,00,000.
- *Quantity test:* 25% of 3,00,000 = 75,000 shares ≥ 60,000. **OK.**
- *Resources test:* 25% × ₹55,00,000 = ₹13,75,000 ≥ ₹12,00,000. **OK.**
- *Debt-equity test:* Post-buy-back net worth = 55,00,000 − 12,00,000 = ₹43,00,000; debt ₹20,00,000; 20,00,000 ≤ 2 × 43,00,000 (= ₹86,00,000). **OK.**
→ Buy-back of 60,000 shares is **valid** on all tests.

**WN-2 — Split of ₹12,00,000:** Face value 60,000 × ₹10 = ₹6,00,000; premium 60,000 × ₹10 = ₹6,00,000 (met fully from Securities Premium). CRR = face value = **₹6,00,000** from General Reserve.

**Journal Entries (₹)**

| Particulars | Dr | Cr |
|---|---:|---:|
| Equity Share Capital A/c ...... Dr | 6,00,000 | |
| Securities Premium A/c ...... Dr | 6,00,000 | |
| &nbsp;&nbsp;To Equity Shareholders (Buy-back) A/c | | 12,00,000 |
| *(Buy-back of 60,000 shares at ₹20; premium met from securities premium)* | | |
| Equity Shareholders (Buy-back) A/c ...... Dr | 12,00,000 | |
| &nbsp;&nbsp;To Bank A/c | | 12,00,000 |
| *(Payment on buy-back)* | | |
| General Reserve A/c ...... Dr | 6,00,000 | |
| &nbsp;&nbsp;To Capital Redemption Reserve A/c | | 6,00,000 |
| *(Nominal value bought back transferred to CRR)* | | |

**Balance Sheet immediately after Buy-Back (₹)**

| Equity & Liabilities | ₹ | Assets | ₹ |
|---|---:|---|---:|
| Equity share capital (2,40,000 × ₹10) | 24,00,000 | Fixed assets | 41,00,000 |
| Capital redemption reserve | 6,00,000 | Investments | 10,00,000 |
| Securities premium (6,00,000 − 6,00,000) | 0 | Inventory | 8,00,000 |
| General reserve (14,00,000 − 6,00,000) | 8,00,000 | Trade receivables | 9,00,000 |
| Surplus (P&L) | 5,00,000 | Bank (15,00,000 − 12,00,000) | 3,00,000 |
| 10% Debentures | 20,00,000 | | |
| Trade payables | 8,00,000 | | |
| **Total** | **71,00,000** | **Total** | **71,00,000** |

**Answer:** Buy-back of 60,000 shares (₹12,00,000) is valid on all three tests; CRR ₹6,00,000 created; post-buy-back Balance Sheet totals **₹71,00,000** and balances.

**Why this way (the reasoning):** Buy-back must first clear the *legality gate* (all three Section 68 tests) before any accounting — a buy-back that breaches even one test is void, so the tests are shown first. On the entries, two forces operate together: the payment cancels ₹6,00,000 of share capital and charges the ₹6,00,000 premium to Securities Premium (a permitted source that preserves distributable reserves), while Section 69's capital-maintenance rule moves an equal ₹6,00,000 (the *face value*) from General Reserve into CRR. The Balance Sheet then reconciles because the reduction in assets (Bank ₹12,00,000) exactly equals the reduction in the owners'-funds side: Share capital −6,00,000, Securities premium −6,00,000, General reserve −6,00,000, offset by CRR +6,00,000 — a net −12,00,000. Students who forget the CRR entry will find the two sides differ by ₹6,00,000; those who charge CRR on ₹12,00,000 instead of the ₹6,00,000 face value will exhaust reserves incorrectly.

*(Full-marks tip: examiners want all three tests verified *before* the entries, premium routed to securities premium, CRR on **face value**, and a post-buy-back Balance Sheet that balances. Marks are lost for skipping the compliance check, mis-stating CRR, or a Balance Sheet that does not tie.)*

### Q52. Ch: Bonus Issue — Sources permissible for partly-paid vs fully-paid bonus (Marks: 8) [Problem]
**Question:** Zenith Ltd. presents the following balances (extract) as on 31.03.2026:

| Particulars | ₹ |
|---|---|
| 40,000 Equity shares of ₹10 each, ₹8 paid up | 3,20,000 |
| Securities Premium | 1,50,000 |
| Capital Redemption Reserve | 80,000 |
| General Reserve | 3,00,000 |
| Surplus (Statement of P&L) | 2,60,000 |
| Revaluation Reserve | 1,20,000 |
| Capital Reserve (realised — profit on re-issue of forfeited shares) | 40,000 |

The Board resolves to **(a)** convert the existing partly-paid shares into fully-paid by a bonus, and **(b)** issue fully-paid bonus shares in the ratio 1 : 1. The company wants to conserve its distributable (free) reserves to the **maximum** extent permitted by law. Pass journal entries and show which sources are used.

**Solution:**

**WN-1 — Amount required for each leg.**
- (a) Make partly-paid fully-paid: 40,000 × (₹10 − ₹8) = 40,000 × ₹2 = **₹80,000**.
- (b) Fresh fully-paid bonus 1:1 on 40,000 shares = 40,000 × ₹10 = **₹4,00,000**.

**WN-2 — Which sources may be used where (Sec. 63).**
- Securities Premium and Capital Redemption Reserve may be applied **only** in paying up **unissued shares as fully-paid bonus shares** — they **cannot** be used to convert partly-paid shares into fully-paid. Revaluation Reserve (unrealised) cannot be used at all.
- Therefore leg (a) ₹80,000 must come from **free reserves only** (General Reserve / Surplus / realised Capital Reserve).
- Leg (b) ₹4,00,000: use Securities Premium ₹1,50,000 + CRR ₹80,000 = ₹2,30,000 first (to conserve free reserves), balance ₹1,70,000 from free reserves.

**WN-3 — Free reserves drawn.** Total free reserves used = ₹80,000 (leg a) + ₹1,70,000 (leg b) = **₹2,50,000**. Available free reserves = GR 3,00,000 + Surplus 2,60,000 + realised Capital Reserve 40,000 = ₹6,00,000 (adequate). Revaluation Reserve ₹1,20,000 left untouched.

**Journal Entries:**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| (a) General Reserve A/c ..... Dr | 80,000 | |
| &nbsp;&nbsp;&nbsp;To Bonus to Shareholders A/c | | 80,000 |
| Bonus to Shareholders A/c ..... Dr | 80,000 | |
| &nbsp;&nbsp;&nbsp;To Equity Share Final Call A/c | | 80,000 |
| Equity Share Final Call A/c ..... Dr | 80,000 | |
| &nbsp;&nbsp;&nbsp;To Equity Share Capital A/c | | 80,000 |
| (b) Securities Premium A/c ..... Dr | 1,50,000 | |
| Capital Redemption Reserve A/c ..... Dr | 80,000 | |
| General Reserve A/c ..... Dr | 1,70,000 | |
| &nbsp;&nbsp;&nbsp;To Bonus to Shareholders A/c | | 4,00,000 |
| Bonus to Shareholders A/c ..... Dr | 4,00,000 | |
| &nbsp;&nbsp;&nbsp;To Equity Share Capital A/c | | 4,00,000 |

**Answer:** Capital increases by ₹4,80,000 (paid-up capital rises from ₹3,20,000 to ₹8,00,000). Free reserves consumed ₹2,50,000; Securities Premium and CRR fully used (₹2,30,000); Revaluation Reserve ₹1,20,000 untouched.

**Why this way (the reasoning):** The heart of this question is that **not every reserve is a valid source for every kind of bonus.** Securities Premium and CRR are "capital-locked" reserves — the law lets them be capitalised only where nothing more than a book conversion of *unissued* capital into *issued fully-paid* capital happens (leg b), because there no cash ever leaves the company. Converting a *partly-paid* share to fully-paid, however, discharges the shareholder's real outstanding liability to pay the balance call — that is economically the same as paying a dividend to the members, so it must be met out of **distributable/free reserves** only. A student who naively dumps Securities Premium into leg (a) to "save" free reserves gets it exactly backwards and loses the marks — the whole trap is that the premium/CRR are *cheaper to the balance sheet but legally unavailable* for leg (a). Revaluation Reserve is barred throughout because it is an unrealised, notional surplus; capitalising it would issue shares against profits that have not been earned in cash.

*(Full-marks tip: examiners reward the explicit statement that premium/CRR cannot convert partly-paid to fully-paid, and the ordering of sources to conserve free reserves. Common deductions: using Revaluation Reserve, or a single lumped bonus entry that hides which source funds which leg.)*

---

### Q53. Ch: Bonus Issue — Validity under Sec. 63 (Marks: 5) [Case/Application]
**Question:** Apex Ltd. proposes to issue fully-paid bonus shares. You gather: (i) part of the bonus is to be met out of the **Revaluation Reserve** created on upward revaluation of land; (ii) the company has some **partly-paid** shares still outstanding which it does **not** intend to make fully-paid; (iii) it has **defaulted** in repayment of matured public deposits and interest thereon, the default subsisting; and (iv) the Articles are silent on bonus. Examine the validity of the proposal.

**Answer:**
**Governing provision — Sec. 63 of the Companies Act, 2013 read with the Companies (Share Capital and Debentures) Rules.** A company may capitalise its profits/reserves to issue fully-paid bonus shares **only if** its Articles authorise it (Sec. 63(2)(a)); and the issue must be **recommended by the Board and authorised in general meeting.**

Applying the four conditions of Sec. 63(2) and (3) to the facts:
- **(i) Source — Revaluation Reserve.** Sec. 63(1) permits bonus only out of (a) free reserves, (b) securities premium, or (c) capital redemption reserve. Sec. 63(3) expressly bars bonus out of **reserves created by revaluation of assets.** The land-revaluation reserve is therefore **not a valid source** — this leg is invalid.
- **(ii) Partly-paid shares outstanding.** Sec. 63(3) prohibits a bonus issue **unless the partly-paid shares are made fully-paid up.** Retaining partly-paid shares **defeats the issue** until they are made fully-paid.
- **(iii) Subsisting default in deposits.** Sec. 63(3) prohibits bonus where the company has **defaulted in payment of interest or principal on fixed deposits or debt securities** and the default subsists. The proposal is **invalid** while the deposit default continues.
- **(iv) Articles silent.** Since Sec. 63(2)(a) requires the Articles to authorise capitalisation, the company must **first alter its Articles** by special resolution.

**Conclusion/Advice:** The proposal as framed is **invalid**. Apex Ltd. must (1) fund the bonus only from free reserves / securities premium / CRR, dropping the revaluation reserve; (2) first make all partly-paid shares fully-paid; (3) cure the deposit default before declaring the bonus; and (4) amend its Articles to permit capitalisation. Once these are done, and once bonus is not declared *in lieu of dividend* (also barred), it may proceed.

**Why this way (the reasoning):** Sec. 63 is really an *anti-abuse* code. Each bar addresses a specific mischief. The revaluation-reserve bar stops a company from handing shareholders paper wealth backed by a mere upward re-estimate of asset value that has produced no cash — capitalising it would dilute the "real capital" cushion creditors rely on. The default bar embodies a **creditors-before-members** priority: you cannot enrich shareholders (even in kind) while the people you owe money to remain unpaid. The partly-paid condition prevents an anomalous capital structure where new fully-paid bonus shares sit beside old shares on which members still owe calls. A student who treats "bonus = capitalise any reserve" misses that the *quality and legality of the source*, and the *company's conduct toward creditors*, both gate the issue.

*(Full-marks tip: cite Sec. 63(3) for each of the three bars separately and name the mischief; a bare "not allowed" without the reason and section loses half the marks.)*

---

### Q54. Ch: Bonus Issue — Maximum bonus ratio constrained by authorised capital (Marks: 8) [Problem]
**Question:** Nova Ltd. has issued and fully-paid **5,00,000 equity shares of ₹10 each**. Its **authorised capital is ₹80,00,000** (8,00,000 equity shares of ₹10). Reserves available: Securities Premium ₹6,00,000; Capital Redemption Reserve ₹4,00,000; General Reserve ₹20,00,000; Surplus (P&L) ₹12,00,000; Dividend Equalisation Reserve ₹3,00,000; Revaluation Reserve ₹5,00,000. Determine the **maximum bonus ratio** Nova Ltd. can declare (fully-paid bonus shares) and state what constrains it. Show the funding.

**Solution:**

**WN-1 — Funds legally available for bonus.** Eligible sources (exclude Revaluation Reserve): Securities Premium 6,00,000 + CRR 4,00,000 + General Reserve 20,00,000 + Surplus 12,00,000 + Dividend Equalisation Reserve 3,00,000 = **₹45,00,000**. (Dividend Equalisation Reserve is a free reserve, hence eligible.) Revaluation Reserve ₹5,00,000 is **not** eligible.

**WN-2 — Maximum shares fundable by reserves.** ₹45,00,000 ÷ ₹10 = **4,50,000 shares** could be funded.

**WN-3 — Maximum shares permitted by authorised capital.** Unissued authorised capital = 8,00,000 − 5,00,000 = **3,00,000 shares** (₹30,00,000). This is the **binding constraint** (3,00,000 < 4,50,000).

**WN-4 — Maximum bonus ratio.** 3,00,000 new : 5,00,000 existing = **3 : 5** (i.e., 3 bonus shares for every 5 held).

**Statement Showing Utilisation of Reserves (bonus of 3,00,000 shares = ₹30,00,000):**

| Source | Amount used (₹) |
|---|---|
| Securities Premium | 6,00,000 |
| Capital Redemption Reserve | 4,00,000 |
| Dividend Equalisation Reserve | 3,00,000 |
| General Reserve | 12,00,000 |
| Surplus (P&L) (balancing) | 5,00,000 |
| **Total** | **30,00,000** |

**Answer:** Maximum bonus is **3 : 5** (3,00,000 shares, ₹30,00,000). The **authorised capital ceiling**, not the reserves, is the binding constraint; to go up to 4,50,000 shares Nova Ltd. must first **increase its authorised capital** (ordinary resolution + alter capital clause of MOA under Sec. 61/64).

**Why this way (the reasoning):** A bonus issue has **two independent ceilings** and you must find the *lower*: how much you can legally *fund* (eligible reserves) and how many shares you are legally *allowed to issue* (unissued authorised capital). Students routinely compute only the reserve capacity, declare a 9:10 bonus, and forget the company cannot issue a single share beyond its authorised capital without first amending the MOA — so the answer is wrong. Recognising which constraint bites is the analytical skill being tested; here reserves (4,50,000-share capacity) are ample, but the authorised-capital wall stops the issue at 3,00,000 shares. The examiner also checks that Revaluation Reserve is excluded and that a genuine free reserve like Dividend Equalisation is *included* — misclassifying either shifts the numbers.

*(Full-marks tip: state both ceilings, identify the binding one explicitly, and note the MOA amendment needed to relax it. Deductions for including Revaluation Reserve or omitting the authorised-capital test.)*

---

### Q55. Ch: Rights Issue — Ex-rights value, value of a right & wealth neutrality (Marks: 6) [Problem]
**Question:** Meridian Ltd. has **10,00,000 equity shares** quoted at **₹250 (cum-rights)**. It announces a **rights issue of 1 new share for every 4 held at ₹150** each. Compute (a) the theoretical ex-rights price, (b) the value of a right (per existing share and per new share), and (c) demonstrate that a holder of **400 shares** is wealth-neutral whether she subscribes or sells her rights entitlement in the market.

**Solution:**

**WN-1 — Theoretical ex-rights price (TERP).**
TERP = [(N × Cum-rights price) + (1 × Subscription price)] ÷ (N + 1), where N = 4.
= [(4 × 250) + (1 × 150)] ÷ 5 = (1,000 + 150) ÷ 5 = **₹230**.

**WN-2 — Value of a right.**
- Per **existing** share = Cum-rights price − TERP = 250 − 230 = **₹20**.
- Per **new** share = TERP − Subscription price = 230 − 150 = ₹80; per existing share = ₹80 ÷ 4 = **₹20** (reconciles).

**WN-3 — Holder of 400 shares.**
- Rights entitlement = 400 ÷ 4 = **100 new shares**.

| Scenario | Working | Wealth (₹) |
|---|---|---|
| Before issue | 400 × 250 | 1,00,000 |
| **(A) Subscribes** — shares held after | 500 × 230 (TERP) | 1,15,000 |
| &nbsp;&nbsp;less cash paid for new shares | 100 × 150 | (15,000) |
| &nbsp;&nbsp;**Net wealth** | | **1,00,000** |
| **(B) Sells rights** — shares held after | 400 × 230 | 92,000 |
| &nbsp;&nbsp;add sale proceeds of rights | 400 × 20 | 8,000 |
| &nbsp;&nbsp;**Net wealth** | | **1,00,000** |

**Answer:** TERP = **₹230**; value of a right = **₹20 per existing share** (₹80 per new share). Whether she subscribes or sells the rights, the holder's wealth stays at **₹1,00,000** — the rights issue is wealth-neutral.

**Why this way (the reasoning):** A rights issue is priced *below* market, so each existing share visibly "drops" from ₹250 to ₹230 — but that fall is **not a loss**; it is the market averaging in the cheaper new shares. The value of a right (₹20) is exactly the amount of that apparent drop, and it belongs to the *existing* shareholder — that is why the law compels the offer to go to existing members first (pre-emption). The neutrality proof is the whole point: the right is a **transferable, monetised entitlement**. If she subscribes, she captures the ₹20 as embedded discount in her new shares; if she sells, she captures it as cash. A shareholder is only worse off if she does *nothing* and lets the right lapse — then the ₹20 leaks to whoever the company allots the un-taken shares to. Students who think a rights issue "destroys ₹20 of value per share" have confused a *price adjustment* with a *wealth transfer*.

*(Full-marks tip: reconcile the right computed two ways (₹20 per old = ₹80 per new ÷ 4) and show both subscribe/sell columns landing on the same wealth. The examiner penalises stating TERP without proving neutrality.)*

---

### Q56. Ch: Rights Issue — Accounting for rights at premium with partial renunciation (Marks: 8) [Problem]
**Question:** Cobalt Ltd. (issued capital **6,00,000 equity shares of ₹10 each, fully paid**) makes a **rights issue of 1 : 3 at ₹15 (₹5 premium)**, payable in full on application. Holders of **1,20,000** of the rights shares **renounce** their entitlement; the company allots those renounced shares to the renouncees'/others as nominated, all at the same terms. All money is received. Pass the journal entries and state the effect on capital and reserves.

**Solution:**

**WN-1 — Number of rights shares.** 6,00,000 ÷ 3 = **2,00,000 rights shares**. Of these, 1,20,000 are renounced (and still allotted to nominees) and 80,000 taken by original holders — accounting is identical for both; renunciation only changes *who* pays, not the entries.

**WN-2 — Money raised.** 2,00,000 × ₹15 = ₹30,00,000 → Capital 2,00,000 × ₹10 = **₹20,00,000**; Securities Premium 2,00,000 × ₹5 = **₹10,00,000**.

**Journal Entries:**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Bank A/c ..... Dr | 30,00,000 | |
| &nbsp;&nbsp;&nbsp;To Equity Share Application & Allotment A/c | | 30,00,000 |
| *(Application money on 2,00,000 rights shares @ ₹15)* | | |
| Equity Share Application & Allotment A/c ..... Dr | 30,00,000 | |
| &nbsp;&nbsp;&nbsp;To Equity Share Capital A/c | | 20,00,000 |
| &nbsp;&nbsp;&nbsp;To Securities Premium A/c | | 10,00,000 |
| *(Allotment of 2,00,000 rights shares, ₹5 premium each)* | | |

**Answer:** Paid-up equity capital rises from ₹60,00,000 to **₹80,00,000**; Securities Premium increases by **₹10,00,000**. Renunciation of 1,20,000 shares has **no separate accounting effect** — the company neither records the renouncees' private consideration nor any charge; only the aggregate ₹30,00,000 received is booked.

**Why this way (the reasoning):** The subtle point is that **renunciation is a transaction between shareholders, off the company's books.** When holder A sells her right to B and B pays A (say ₹20 per right) and then pays the company ₹15, only the ₹15 per share ever reaches the company — the ₹20 renunciation premium is A's private gain and never touches Cobalt's ledgers. Hence there is a *single* set of entries for all 2,00,000 shares at ₹15, regardless of how many were renounced. Students err by trying to invent an entry for the renounced portion or by splitting entries — but from the *company's* standpoint a renounced right and an exercised right are indistinguishable. The premium of ₹5 is a **securities premium** (Sec. 52) because it is the excess of issue price over face value on shares issued *by the company*; it is capital-locked and cannot be treated as revenue. Note that pricing a rights issue *below* fair value is permitted (unlike a fresh preferential issue) precisely because the discount accrues to existing members through the value of the right — so no "shortfall" or notional loss is booked.

*(Full-marks tip: one combined entry for all rights shares plus a clear statement that renunciation is off-book. Deductions for double-counting the renounced shares or routing the ₹5 through P&L.)*

---

### Q57. Ch: Rights Issue — Sec. 62(1)(a) compliance (Marks: 5) [Case/Application]
**Question:** Titan Ltd. (an unlisted public company) wants to raise fresh equity. The Board proposes to: (i) offer the new shares **directly to a strategic outside investor**, bypassing existing members, because "they will subscribe anyway"; (ii) keep the offer **open for only 7 days**; (iii) **deny renunciation**, requiring members to either subscribe personally or let the shares lapse. Examine the validity of each proposal under Sec. 62 and advise.

**Answer:**
**Governing provision — Sec. 62(1)(a) of the Companies Act, 2013** (further issue of capital / pre-emptive rights). Where a company having a share capital proposes to increase its subscribed capital by a *further issue of shares*, they **must first be offered to existing equity shareholders** in proportion to their holdings, subject to the following statutory conditions.

Applying to the three proposals:
- **(i) Offering directly to an outsider.** This violates the **pre-emptive right** of existing members. Titan may allot to an outsider **only** if members do not take up the offer (Sec. 62(1)(a)(iii): the Board may dispose of un-subscribed shares as beneficial to the company), **or** by taking the **preferential-allotment route under Sec. 62(1)(c)** with a *special resolution* and a registered-valuer valuation. Directly bypassing members without either route is **invalid**.
- **(ii) Offer open only 7 days.** Sec. 62(1)(a)(i) requires the offer to specify a period of **not less than 15 days and not more than 30 days**, within which if not accepted it is deemed declined. A **7-day** window is **invalid** (below the statutory floor). *(Private companies may shorten by consent of 90% members — not available to Titan, a public company.)*
- **(iii) Denying renunciation.** Sec. 62(1)(a)(ii) provides the offer **shall be deemed to include a right to renounce** the shares in favour of any other person, **unless the Articles otherwise provide.** Renunciation is the default right; Titan can exclude it only if its **Articles expressly so provide.** A blanket denial without such an article is **invalid**.

**Conclusion/Advice:** All three proposals are defective as framed. Titan should (1) make the rights offer to existing members first (or use Sec. 62(1)(c) with special resolution + valuation if it genuinely wants the strategic investor); (2) keep the offer open **15–30 days**; and (3) **allow renunciation** unless its Articles already curtail it.

**Why this way (the reasoning):** Sec. 62(1)(a) exists to protect an existing shareholder's **proportionate stake and voting power** from being diluted by directors issuing fresh shares to favoured parties. The pre-emptive right is the core protection; the 15-day floor guarantees members a *real* chance to evaluate and fund the offer (7 days is designed to make members fail); and the renunciation right ensures the economic value of the entitlement is *monetisable* even by a member who cannot personally subscribe. A student who treats "the company can raise capital however the Board likes" misses that Sec. 62 is a *members-protection* section — the freedom to allot to outsiders (Sec. 62(1)(c)) is available only through the heavier safeguard of a special resolution and independent valuation, precisely because it overrides pre-emption.

*(Full-marks tip: pin each defect to the exact sub-clause (a)(i)/(a)(ii)/(a)(iii) or (c), and give the cure. Merely saying "rights must go to members first" without the 15–30 day and renunciation points loses marks.)*

---

### Q58. Ch: ESOP — Fair-value method, cliff vesting with revision of forfeiture estimate (Marks: 10) [Problem]
**Question:** On 01.04.2023 Stellar Ltd. grants **1,000 options to each of its 50 senior employees**, exercisable after a **3-year continuous-service (cliff) vesting** at an exercise price of **₹40** (face value ₹10). Fair value of each option at grant date = **₹25**. At grant, the company expects **10%** of the 50 employees to leave over three years. Actual/revised experience:
- End of Year 1 (31.03.2024): estimate unchanged (5 employees expected to leave in total).
- End of Year 2 (31.03.2025): estimate **revised** — 8 employees now expected to leave in total.
- End of Year 3 (31.03.2026): **7 employees actually left**; the rest vest. On 31.03.2026 all vested options are exercised.

Compute the annual employee-compensation cost and pass entries for each year including exercise.

**Solution:**

**WN-1 — Options expected to vest each year (fair value ₹25, total FV per option unchanged).**
- Yr 1: expected leavers 5 → vesting employees 45 → **45,000 options**.
- Yr 2: expected leavers 8 → vesting employees 42 → **42,000 options**.
- Yr 3: actual leavers 7 → vested employees 43 → **43,000 options**.

**WN-2 — Cumulative and annual cost (straight-line over 3-yr vesting).**

| Year | Options expected/actual to vest | Cumulative FV (options × ₹25 × elapsed/3) | Cumulative cost (₹) | Prior cumulative (₹) | Cost for the year (₹) |
|---|---|---|---|---|---|
| 1 | 45,000 | 45,000 × 25 × 1/3 | 3,75,000 | — | 3,75,000 |
| 2 | 42,000 | 42,000 × 25 × 2/3 | 7,00,000 | 3,75,000 | 3,25,000 |
| 3 | 43,000 (actual) | 43,000 × 25 × 3/3 | 10,75,000 | 7,00,000 | 3,75,000 |

**WN-3 — Exercise (31.03.2026).** 43,000 options × ₹40 cash = ₹17,20,000 received. Share Options Outstanding transferred = ₹10,75,000. Total credited = 43,000 × (40 + 25) = ₹27,95,000 → Share Capital 43,000 × ₹10 = ₹4,30,000; Securities Premium = balance ₹23,65,000.

**Journal Entries:**

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 31.03.24 | Employee Compensation Expense A/c ..... Dr | 3,75,000 | |
| | &nbsp;&nbsp;To Share Options Outstanding A/c | | 3,75,000 |
| 31.03.25 | Employee Compensation Expense A/c ..... Dr | 3,25,000 | |
| | &nbsp;&nbsp;To Share Options Outstanding A/c | | 3,25,000 |
| 31.03.26 | Employee Compensation Expense A/c ..... Dr | 3,75,000 | |
| | &nbsp;&nbsp;To Share Options Outstanding A/c | | 3,75,000 |
| 31.03.26 | Bank A/c ..... Dr | 17,20,000 | |
| | Share Options Outstanding A/c ..... Dr | 10,75,000 | |
| | &nbsp;&nbsp;To Equity Share Capital A/c | | 4,30,000 |
| | &nbsp;&nbsp;To Securities Premium A/c | | 23,65,000 |

**Answer:** Compensation cost = **₹3,75,000 (Yr 1), ₹3,25,000 (Yr 2), ₹3,75,000 (Yr 3)** = ₹10,75,000 total. On exercise, capital rises ₹4,30,000 and securities premium ₹23,65,000; the Share Options Outstanding balance is fully absorbed.

**Why this way (the reasoning):** The measurement principle is **grant-date fair value, frozen** — you never re-measure the ₹25 per option for an *equity-settled* plan even if the share price later moves, because the company has issued equity, not incurred a cash obligation. What you *do* revise every year is the **number** of options expected to vest — the "true-up" for a *service (vesting) condition*. That is why Year 2's charge falls to ₹3,25,000: the fresh estimate (42,000 options) is applied to the *cumulative* two-thirds and the previously-booked ₹3,75,000 is backed out, so the balance sheet always carries the best current estimate. Year 3 trues up to actuals (43,000). Students frequently make two mistakes: (1) re-measuring the option's fair value each year (that is the rule for *cash-settled* SARs, not equity options — see the SAR question), and (2) computing each year's charge in isolation instead of *cumulative-minus-prior*, which breaks when estimates change. The cost is charged **over the vesting period** because that is the period over which the employee renders the service that "buys" the options — matching the expense to the benefit received.

*(Full-marks tip: show the cumulative-less-prior table so the revision flows correctly; the examiner specifically checks that Year 2 is 3,25,000, not 3,50,000. Deductions for re-measuring fair value or for a wrong premium on exercise.)*

---

### Q59. Ch: ESOP — Intrinsic-value method and exercise entries (Marks: 8) [Problem]
**Question:** Orion Ltd. grants **20,000 options** to employees on 01.04.2024 at an exercise price of **₹80** (face value ₹10), vesting after **4 years**. Market price of the share on grant date = **₹120**; the company uses the **intrinsic-value method**. Fair value of each option (for disclosure) = **₹50**. On expiry of vesting all 20,000 options are exercised when market price is ₹200. Compute the annual charge under the intrinsic-value method, pass the exercise entry, and state the disclosure impact of the fair-value figure.

**Solution:**

**WN-1 — Intrinsic value at grant.** Market price − exercise price = ₹120 − ₹80 = **₹40 per option**. Total compensation = 20,000 × ₹40 = **₹8,00,000**.

**WN-2 — Annual amortisation (4-year vesting, straight line).** ₹8,00,000 ÷ 4 = **₹2,00,000 per year** (Years 1–4). *(The subsequent rise to ₹200 is irrelevant — intrinsic value is fixed at grant, not re-measured.)*

**WN-3 — Exercise.** Cash 20,000 × ₹80 = ₹16,00,000; Share Options Outstanding ₹8,00,000. Total = ₹24,00,000 → Capital 20,000 × ₹10 = ₹2,00,000; Securities Premium = ₹22,00,000.

**Journal Entries (representative):**

| Particulars | Dr (₹) | Cr (₹) |
|---|---|---|
| Each year: Employee Compensation Expense A/c ..... Dr | 2,00,000 | |
| &nbsp;&nbsp;To Share Options Outstanding A/c | | 2,00,000 |
| On exercise: Bank A/c ..... Dr | 16,00,000 | |
| Share Options Outstanding A/c ..... Dr | 8,00,000 | |
| &nbsp;&nbsp;To Equity Share Capital A/c | | 2,00,000 |
| &nbsp;&nbsp;To Securities Premium A/c | | 22,00,000 |

**WN-4 — Fair-value disclosure.** Under fair value the total cost would be 20,000 × ₹50 = **₹10,75,000... (20,000 × ₹50 = ₹10,00,000)**; i.e., ₹2,50,000 per year and total ₹10,00,000. The company must **disclose** the effect on net profit and EPS **had the fair-value method been used** — profit would be lower by the incremental ₹2,00,000 over the plan (₹10,00,000 − ₹8,00,000).

**Answer:** Charge under intrinsic value = **₹2,00,000 per year** (total ₹8,00,000). On exercise: capital ₹2,00,000, securities premium ₹22,00,000. Pro-forma fair-value cost = ₹10,00,000, disclosed by way of note with the impact on profit and EPS.

**Why this way (the reasoning):** Under the intrinsic-value method the cost is locked at the **grant-date spread** (market ₹120 − exercise ₹80 = ₹40); the market climbing to ₹200 by exercise is a gain that accrues to the *employee*, not an extra expense to the *company* — the company's "cost" of the equity instrument was fixed the moment it granted the option. That is why re-computing on ₹200 is wrong. The important conceptual layer is the **disclosure discipline**: intrinsic value systematically *under*states the true economic cost because it ignores the time-value and volatility captured only by an option-pricing (fair-value) model — here ₹50 vs ₹40. The Guidance Note therefore *requires* a company that uses intrinsic value to disclose the *pro-forma* fair-value effect on profit and EPS, so users are not misled into thinking ESOPs are "cheaper" than they are. A student should understand intrinsic value as a permitted-but-inferior measurement whose weakness must be transparently footnoted.

*(Full-marks tip: fix intrinsic value at grant (ignore ₹200), amortise over 4 years, and explicitly give the fair-value pro-forma disclosure — that disclosure line is where most candidates drop marks.)*

---

### Q60. Ch: ESOP — Cash-settled Stock Appreciation Rights (SARs) with re-measurement (Marks: 8) [Problem]
**Question:** Vega Ltd. grants **100 cash-settled SARs to each of 50 employees** on 01.04.2023, vesting after **3 years** of service; on vesting each SAR is settled in **cash** equal to the appreciation in share price. The **fair value of each SAR** at each year-end is: 31.03.2024 ₹10, 31.03.2025 ₹12, 31.03.2026 ₹15. All employees remain in service and the SARs are settled in cash on 31.03.2026 at their fair value of ₹15. Compute the expense each year and pass the entries. How would the treatment differ if the plan were **equity-settled**?

**Solution:**

**WN-1 — Total SARs.** 100 × 50 = **5,000 SARs**.

**WN-2 — Liability and expense (re-measured to fair value each year, accrued over 3-yr vesting).**

| Year-end | FV per SAR (₹) | Cumulative liability = 5,000 × FV × elapsed/3 (₹) | Prior liability (₹) | Expense for year (₹) |
|---|---|---|---|---|
| 31.03.24 | 10 | 5,000 × 10 × 1/3 = 16,667 | — | 16,667 |
| 31.03.25 | 12 | 5,000 × 12 × 2/3 = 40,000 | 16,667 | 23,333 |
| 31.03.26 | 15 | 5,000 × 15 × 3/3 = 75,000 | 40,000 | 35,000 |

**WN-3 — Settlement (31.03.2026).** Cash paid = 5,000 × ₹15 = **₹75,000** against the liability.

**Journal Entries:**

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| 31.03.24 | Employee Compensation Expense A/c ..... Dr | 16,667 | |
| | &nbsp;&nbsp;To SAR Liability A/c | | 16,667 |
| 31.03.25 | Employee Compensation Expense A/c ..... Dr | 23,333 | |
| | &nbsp;&nbsp;To SAR Liability A/c | | 23,333 |
| 31.03.26 | Employee Compensation Expense A/c ..... Dr | 35,000 | |
| | &nbsp;&nbsp;To SAR Liability A/c | | 35,000 |
| 31.03.26 | SAR Liability A/c ..... Dr | 75,000 | |
| | &nbsp;&nbsp;To Bank A/c | | 75,000 |

**Answer:** Expense = **₹16,667 (Yr 1), ₹23,333 (Yr 2), ₹35,000 (Yr 3)** = ₹75,000, settled in cash. If **equity-settled**, the fair value would be **frozen at grant date** (no annual re-measurement), the credit would go to **Share Options Outstanding (equity)** not a liability, and no cash would be paid — settlement would be by issuing shares.

**Why this way (the reasoning):** The decisive fork is **who bears the price risk after grant.** A cash-settled SAR creates a **liability** — the company will one day pay cash equal to the share appreciation — so, like any liability of uncertain amount, it must be **re-measured to fair value at every reporting date** until settled, with the change hitting the P&L. That is why the per-SAR value moves ₹10 → ₹12 → ₹15 through the computation and the final liability equals the actual cash paid (₹75,000). An **equity-settled** option is the opposite: the company will settle by handing over its *own shares*, so its "cost" is the grant-date fair value and it is **never re-measured** — the entity is indifferent to later price moves because it is not paying cash. Students constantly blur the two and either re-measure equity options (over-stating cost) or freeze SARs (under-stating the liability). Getting the *classification* right — liability vs equity — is the whole examinable insight; the arithmetic follows from it.

*(Full-marks tip: state the classification (liability, hence re-measured) up front, and contrast with equity-settled in one clean sentence. The examiner deducts heavily for crediting "Share Options Outstanding" instead of a liability, or for freezing the SAR value.)*

---

### Q61. Ch: ESOP — Lapse of options: before vs after vesting (Marks: 5) [Case/Application]
**Question:** Lumen Ltd. runs an equity-settled ESOP. Two situations arise: **(A)** Employee P leaves in **Year 2 of a 3-year vesting period**, so his options **never vest** (a service condition fails). **(B)** Employee Q's options **vest** at the end of Year 3, but Q **allows them to lapse unexercised** during the exercise window because the market price is below the exercise price. State the accounting treatment of the balance in the *Share Options Outstanding* account in each case, and explain the principle distinguishing them.

**Answer:**
**Governing framework — Guidance Note on Accounting for Employee Share-based Payments (equity-settled).**

**(A) Lapse *before* vesting (service condition not met).** Because a **service/vesting condition failed**, the employee is treated as never having earned the options. The cost previously recognised for P's options must be **reversed** — the *Employee Compensation Expense* (and the corresponding *Share Options Outstanding*) relating to P is **written back** to profit. Net effect over the plan: **no expense** is retained for options that never vest. (This is the true-up already seen in Q58 — expected forfeitures reduce the number of options costed.)

**(B) Lapse *after* vesting (options expired unexercised).** Here the employee **fully earned** the options by rendering the required service; the vesting condition **was satisfied.** The service has been consumed, so the expense **is not reversed.** The balance standing in the *Share Options Outstanding* account for Q's lapsed options is **transferred to General Reserve** (a transfer *within equity*), not credited back to P&L.

**Journal (case B):** Share Options Outstanding A/c ..... Dr | To General Reserve A/c.

**Conclusion:** Reverse the cost for **A** (fails vesting); **do not** reverse for **B** — merely move the ESOP-outstanding balance to General Reserve.

**Why this way (the reasoning):** The dividing line is **whether the employee earned the award.** ESOP cost is the fair value of *services received* from employees; the counter-entry (Share Options Outstanding) is only a *waiting room* in equity for shares that may later be issued. In case A the employee left early and never rendered the full service, so no service was received for those options — the expense was booked on an *expectation* that turned out false, and honesty requires reversing it. In case B the employee **did** render every year of service demanded; the company genuinely received and consumed that service, so the expense is a true cost of the period and *cannot* be un-booked merely because the employee later chose not to exercise. But since no shares will now be issued, the amount parked in Share Options Outstanding is no longer a "shares-in-waiting" reserve — it is simply retained within equity by transfer to General Reserve. Routing case B back through P&L would wrongly resurrect profit for a cost that was validly incurred; that is the classic error the examiner is testing.

*(Full-marks tip: the crisp rule — *pre-vesting lapse → reverse to P&L; post-vesting lapse → transfer within equity to General Reserve* — plus the "service earned or not" reasoning earns full marks. Saying "credit P&L" in case B is the standard trap.)*

---

### Q62. Ch: Underwriting of Shares — Full computation with firm underwriting treated as marked (Marks: 10) [Problem]
**Question:** Comet Ltd. issues **2,00,000 equity shares**, fully underwritten by **X, Y and Z in the ratio 5 : 3 : 2**. The underwriters also enter into **firm underwriting**: X 10,000, Y 6,000, Z 4,000 shares. Applications received (excluding firm underwriting): **marked** — X 50,000, Y 40,000, Z 30,000; **unmarked** 20,000. **Firm underwriting is treated as marked applications** (credited to the individual underwriter). Determine the net liability of each underwriter and the total shares each must take up.

**Solution:**

**WN-1 — Applications vs issue.** Marked 1,20,000 + Unmarked 20,000 + Firm 20,000 = 1,60,000 received. Shortfall to underwriters = 2,00,000 − 1,60,000 = **40,000 shares.**

**WN-2 — Gross liability (5:3:2 of 2,00,000).** X 1,00,000; Y 60,000; Z 40,000.

**Statement Showing Net Liability of Underwriters (shares):**

| Particulars | X | Y | Z | Total |
|---|---|---|---|---|
| Gross liability (5:3:2) | 1,00,000 | 60,000 | 40,000 | 2,00,000 |
| Less: Marked applications | (50,000) | (40,000) | (30,000) | (1,20,000) |
| Less: Firm underwriting (as marked) | (10,000) | (6,000) | (4,000) | (20,000) |
| Balance | 40,000 | 14,000 | 6,000 | 60,000 |
| Less: Unmarked 20,000 (5:3:2) | (10,000) | (6,000) | (4,000) | (20,000) |
| **Net liability (from shortfall)** | **30,000** | **8,000** | **2,000** | **40,000** |
| Add: Firm underwriting (shares subscribed) | 10,000 | 6,000 | 4,000 | 20,000 |
| **Total shares to be taken up** | **40,000** | **14,000** | **6,000** | **60,000** |

**Answer:** Net liability from the shortfall — **X 30,000, Y 8,000, Z 2,000** (= 40,000). Including their firm commitment the total shares each takes up are **X 40,000, Y 14,000, Z 6,000** (= 60,000, reconciling to shortfall 40,000 + firm 20,000).

**Why this way (the reasoning):** "Firm underwriting treated as **marked**" means each underwriter's firm shares are credited to *that* underwriter alone — so they reduce *his own* remaining liability, exactly like an application bearing his stamp. That is why firm is deducted in the *marked* row, benefiting X/Y/Z individually. **Unmarked** applications, by contrast, carry no underwriter's identity, so their benefit is shared by **all** underwriters in the **gross-liability ratio** (5:3:2) — the ratio, not the residual balances, because the unmarked pool is a common windfall attributable to the issue at large. The final, easily-missed step is that firm underwriting is a *definite* subscription: even after netting, each underwriter must **still take his firm shares in addition** — so total shares taken = net liability + firm. Students who stop at the "net liability" line under-report by the 20,000 firm shares. The reconciliation (60,000 = shortfall 40,000 + firm 20,000) is the built-in check that the treatment is internally consistent.

*(Full-marks tip: deduct firm in the *marked* section (individual benefit), distribute unmarked in the *gross ratio*, and add firm back at the end. The most common error is distributing unmarked in the ratio of *balances* or forgetting to add firm shares back.)*

---

### Q63. Ch: Underwriting of Shares — Firm underwriting treated as unmarked (Marks: 8) [Problem]
**Question:** Nebula Ltd. issues **1,00,000 equity shares**, fully underwritten by **A and B in the ratio 3 : 2**. Firm underwriting: A 6,000, B 4,000. Applications (excluding firm): **marked** — A 30,000, B 25,000; **unmarked** 15,000. **Firm underwriting is treated as unmarked** (added to the unmarked pool and shared in the gross-liability ratio). Determine the net liability and total shares to be taken by each underwriter.

**Solution:**

**WN-1 — Shortfall.** Marked 55,000 + Unmarked 15,000 + Firm 10,000 = 80,000 received. Shortfall = 1,00,000 − 80,000 = **20,000 shares.**

**WN-2 — Gross liability (3:2 of 1,00,000).** A 60,000; B 40,000. **Pool of unmarked + firm** = 15,000 + 10,000 = 25,000, shared 3:2 → A 15,000, B 10,000.

**Statement Showing Net Liability (shares):**

| Particulars | A | B | Total |
|---|---|---|---|
| Gross liability (3:2) | 60,000 | 40,000 | 1,00,000 |
| Less: Marked applications | (30,000) | (25,000) | (55,000) |
| Balance | 30,000 | 15,000 | 45,000 |
| Less: Unmarked + Firm 25,000 (3:2) | (15,000) | (10,000) | (25,000) |
| **Net liability (from shortfall)** | **15,000** | **5,000** | **20,000** |
| Add: Firm underwriting (subscribed) | 6,000 | 4,000 | 10,000 |
| **Total shares to be taken up** | **21,000** | **9,000** | **30,000** |

**Answer:** Net liability — **A 15,000, B 5,000** (= 20,000). Total shares taken up including firm — **A 21,000, B 9,000** (= 30,000 = shortfall 20,000 + firm 10,000).

**Why this way (the reasoning):** When firm underwriting is treated as **unmarked**, the firm shares lose their individual identity and are thrown into the common unmarked pool, then redistributed among *all* underwriters in the **gross-liability ratio** — so an underwriter no longer gets exclusive credit for his own firm commitment in the netting step. This *usually* produces a **different** (often higher net-liability) answer than the "firm-as-marked" method of Q62 — which is precisely why the exam specifies the treatment: the two conventions are not interchangeable, and the question tests whether you apply the *stated* one rather than a default. Note the pool is shared in the *gross* ratio (3:2), consistent with unmarked treatment, and — as always — firm shares are a firm subscription, so they are **added back** at the end. The reconciliation (30,000 = shortfall 20,000 + firm 10,000) confirms consistency. A candidate must not silently switch to the marked convention because it "feels" natural; matching the prescribed treatment is the discipline being marked.

*(Full-marks tip: pool firm with unmarked, distribute in the gross ratio, then add firm back. Deductions for crediting firm to the individual underwriter (that is the *other* convention) or distributing in the ratio of balances.)*

---

### Q64. Ch: Underwriting of Shares — Partial underwriting with surplus redistribution (Marks: 8) [Problem]
**Question:** Pulsar Ltd. issues **1,00,000 equity shares**, of which **only 80,000 are underwritten** — **P underwrites 50,000 and Q underwrites 30,000**; the balance **20,000 is not underwritten** (borne by the company). Applications: **marked** — P 40,000, Q 20,000; **unmarked** 25,000 (no firm underwriting). For sharing unmarked applications, the **company is treated as an underwriter for the un-underwritten 20,000**, and the gross-liability ratio is P : Q : Company = 5 : 3 : 2. Determine the net liability of each.

**Solution:**

**WN-1 — Shortfall.** Marked 60,000 + Unmarked 25,000 = 85,000 received. Shortfall = 1,00,000 − 85,000 = **15,000 shares.**

**WN-2 — Gross liability (5:3:2).** P 50,000; Q 30,000; Company 20,000. Unmarked 25,000 shared 5:3:2 → P 12,500; Q 7,500; Company 5,000.

**Statement Showing Net Liability (shares):**

| Particulars | P | Q | Company | Total |
|---|---|---|---|---|
| Gross liability (5:3:2) | 50,000 | 30,000 | 20,000 | 1,00,000 |
| Less: Marked applications | (40,000) | (20,000) | — | (60,000) |
| Balance | 10,000 | 10,000 | 20,000 | 40,000 |
| Less: Unmarked 25,000 (5:3:2) | (12,500) | (7,500) | (5,000) | (25,000) |
| Balance | (2,500) | 2,500 | 15,000 | 15,000 |
| Surplus of P (2,500) redistributed to Q & Co (3:2) | 2,500 | (1,500) | (1,000) | — |
| **Net liability** | **Nil** | **1,000** | **14,000** | **15,000** |

**Answer:** Net liability — **P Nil, Q 1,000, Company 14,000** (= 15,000, reconciling to the shortfall). P's applications exceeded his liability, so his 2,500 surplus is redistributed to the remaining parties (Q and Company) in their 3:2 ratio, and P bears nothing further.

**Why this way (the reasoning):** In a **partial** underwriting the un-underwritten portion is not "unprotected" in the calculation — the **company itself is treated as an underwriter** for that slice, so it too shares the common unmarked applications in the gross ratio and absorbs its own residual shortfall. When one underwriter's credits (marked + share of unmarked) *exceed* his gross liability, he cannot have a *negative* liability — the excess is a **surplus** that must be **redistributed to the other underwriters in their mutual ratio** (here Q : Company = 3 : 2). Failing to redistribute leaves the arithmetic not tying to the shortfall and wrongly hands P a phantom "credit" the company would have to eat. The examinable subtlety is recognising *when* a negative appears and reallocating it — many candidates simply floor P at zero and lose the 2,500 shares, breaking the reconciliation. Treating the company as the 2-part underwriter is what makes the un-underwritten portion accountable and the total tie to 15,000.

*(Full-marks tip: treat the company as an underwriter for the un-underwritten portion, and redistribute any underwriter's surplus in the *remaining* underwriters' ratio. Deductions for flooring at zero without reallocating, or for excluding the company from the unmarked split.)*

---

### Q65. Ch: Underwriting — Commission rate limits (Sec. 40) (Marks: 6) [Case/Application]
**Question:** Aurora Ltd. makes a public issue of **5,00,000 equity shares of ₹10 each at ₹12** (₹2 premium) and simultaneously **50,000 debentures of ₹100 each at par**. It agrees to pay underwriting commission of **5% on the shares** and **3% on the debentures**. The company's **Articles authorise a maximum commission of 4% on shares and 2.5% on debentures.** Examine the validity and compute the maximum commission legally payable.

**Answer:**
**Governing provision — Sec. 40(6) of the Companies Act, 2013 read with Rule 13 of the Companies (Prospectus and Allotment of Securities) Rules.** Underwriting commission may be paid only if authorised by the Articles, and it must **not exceed** (a) **5% of the price at which shares are issued**, or the rate authorised by the Articles, **whichever is less**; and (b) **2.5% of the price at which debentures are issued**, or the Articles' rate, **whichever is less.** The commission is computed on the **issue price** (including premium for shares).

**Application:**
- **Shares.** Statutory cap 5%; Articles cap 4% → **lower = 4%.** The agreed 5% is **invalid to the extent it exceeds 4%.** Issue price = 5,00,000 × ₹12 = ₹60,00,000. Maximum commission = 4% × ₹60,00,000 = **₹2,40,000.**
- **Debentures.** Statutory cap 2.5%; Articles cap 2.5% → **lower = 2.5%.** The agreed 3% is **invalid above 2.5%.** Issue price = 50,000 × ₹100 = ₹50,00,000. Maximum commission = 2.5% × ₹50,00,000 = **₹1,25,000.**

**Conclusion:** The agreed rates (5% / 3%) are **not fully valid.** Aurora Ltd. may pay at most **₹2,40,000 on shares and ₹1,25,000 on debentures**, i.e., **₹3,65,000 in aggregate** — being the lower of the statutory ceiling and the Articles' rate in each case.

**Why this way (the reasoning):** The commission ceiling is a **two-gate test**: the *statutory maximum* (5% shares / 2.5% debentures) sets the outer wall, and the *Articles' authorised rate* sets the company's own self-imposed inner wall — and the payable rate is the **lower** of the two, always. Students who apply only the 5% statutory limit miss that a *tighter* article (4%) legally binds the company below the statute. The computation base matters too: for shares the commission is on the **issue price including premium** (₹12, not ₹10), because the underwriter guarantees subscription of the *whole* offered amount, premium included; using face value would understate the base. The provision exists to stop promoters from siphoning company funds to underwriters (often related parties) through inflated commissions, so both the statutory cap and the shareholder-approved article act as spending controls. Recognising that debentures carry a *lower* statutory cap (2.5%) than shares (5%) — reflecting their lower placement risk — is also examinable.

*(Full-marks tip: apply "lower of statutory rate and Articles' rate" separately to shares and debentures, and compute on issue price incl. premium. Common deductions: applying only the statutory 5%/2.5%, or computing share commission on face value ₹10.)*

---

### Q66. Ch: Redemption of Debentures — DRR, 15% DRR-Investment and redemption at premium (Marks: 10) [Problem]
**Question:** Cygnus Ltd. (an **unlisted** company, **not** an NBFC/HFC) had issued **50,000 12% Debentures of ₹100 each**, redeemable **at a premium of 10%** on **31.03.2026**. As required by law it must (a) create a Debenture Redemption Reserve of at least **10% of the outstanding debentures** before redemption, and (b) on or before **30.04.2025**, invest/deposit **15% of the debentures maturing during the year ending 31.03.2026**. The premium on redemption was **not** provided at the time of issue. Pass the journal entries for creating the DRR, the DRR-Investment, providing the premium, and the redemption; and the transfer after redemption. (Surplus and Securities Premium are available.)

**Solution:**

**WN-1 — DRR required.** 10% of ₹50,00,000 (nominal) = **₹5,00,000**, created out of Surplus (P&L) before redemption.

**WN-2 — DRR-Investment (DRRI).** 15% of nominal value of debentures maturing during the year = 15% × ₹50,00,000 = **₹7,50,000**, deposited/invested by 30.04.2025.

**WN-3 — Premium on redemption.** 10% × ₹50,00,000 = **₹5,00,000**, provided (not done at issue) — met from Securities Premium (or Surplus). Total payable to holders = ₹50,00,000 + ₹5,00,000 = **₹55,00,000.**

**Journal Entries:**

| Date | Particulars | Dr (₹) | Cr (₹) |
|---|---|---|---|
| Before redemption | Surplus (Statement of P&L) A/c ..... Dr | 5,00,000 | |
| | &nbsp;&nbsp;To Debenture Redemption Reserve A/c | | 5,00,000 |
| 30.04.2025 | Debenture Redemption Reserve Investment A/c ..... Dr | 7,50,000 | |
| | &nbsp;&nbsp;To Bank A/c | | 7,50,000 |
| Before redemption | Securities Premium A/c ..... Dr | 5,00,000 | |
| | &nbsp;&nbsp;To Premium on Redemption of Debentures A/c | | 5,00,000 |
| 31.03.2026 | Bank A/c ..... Dr | 7,50,000 | |
| | &nbsp;&nbsp;To Debenture Redemption Reserve Investment A/c | | 7,50,000 |
| 31.03.2026 | 12% Debentures A/c ..... Dr | 50,00,000 | |
| | Premium on Redemption of Debentures A/c ..... Dr | 5,00,000 | |
| | &nbsp;&nbsp;To Debentureholders A/c | | 55,00,000 |
| 31.03.2026 | Debentureholders A/c ..... Dr | 55,00,000 | |
| | &nbsp;&nbsp;To Bank A/c | | 55,00,000 |
| After redemption | Debenture Redemption Reserve A/c ..... Dr | 5,00,000 | |
| | &nbsp;&nbsp;To General Reserve A/c | | 5,00,000 |

**Answer:** DRR created **₹5,00,000**; DRRI **₹7,50,000** (encashed at maturity); premium on redemption **₹5,00,000** provided from Securities Premium; total paid to holders **₹55,00,000**; after redemption the DRR of ₹5,00,000 is transferred to **General Reserve**.

**Why this way (the reasoning):** The DRR and the 15% investment do different jobs. The **DRR** is an *appropriation of profits* — it ring-fences ₹5,00,000 of distributable profit so that money is retained in the business (not paid out as dividend) to back the redemption; it is a *reserve*, not cash. The **DRR-Investment (15%)** is the *liquidity* leg — the law forces the company to park actual funds in specified investments/deposits by 30 April so that liquid resources genuinely exist when the debentures mature, computed on the **nominal** value of debentures maturing that year (₹7,50,000), *not* on the premium. The **premium on redemption** is a known future *loss* on a capital transaction; because it was not provided at issue, it must be provided now, ideally from **Securities Premium** (Sec. 52 expressly permits using the premium account to write off the premium payable on redemption of debentures), conserving revenue profits. Finally, once redemption is complete the DRR has served its purpose and is **transferred to General Reserve** (it is *not* credited back to P&L, as it is a capital-nature reserve now free of its earmark). Students commonly compute the 15% on the *total including premium*, or forget that DRR is only 10% of *outstanding* debentures, or write the premium off against P&L when securities premium is available — each costs marks.

*(Full-marks tip: DRR = 10% of nominal; DRRI = 15% of nominal maturing (encashed at redemption); premium via Securities Premium; DRR → General Reserve after redemption. Deductions for computing 15% on premium-inclusive figure or reversing DRR to P&L.)*

---

### Q67. Ch: Redemption of Debentures — Sinking Fund (redemption fund) method (Marks: 10) [Problem]
**Question:** Draco Ltd. issued **₹10,00,000 debentures** redeemable at par at the end of **3 years**. It operates a **sinking fund (debenture redemption fund)**: an equal annual amount is set aside and invested; interest earned on the investments is **re-invested** at **5% p.a.** The sinking-fund factor to accumulate ₹1 in 3 years at 5% is **0.317208**, so the annual appropriation is **₹3,17,208**. Interest is earned at each year-end on the opening balance of investments. At the end of Year 3 the investments are realised (assume at cost) and the debentures redeemed. Prepare the **Debenture Redemption Fund Account** and the **Debenture Redemption Fund Investment Account** for the three years.

**Solution:**

**WN-1 — Annual appropriation.** ₹10,00,000 × 0.317208 = **₹3,17,208** per year.

**WN-2 — Interest earned (5% on opening investment balance).**
- End Yr 1: no opening investment → interest **Nil**; invest ₹3,17,208.
- End Yr 2: 5% × ₹3,17,208 = **₹15,860**; total added to fund Yr 2 = 3,17,208 + 15,860; invest 3,17,208 + 15,860 = ₹3,33,068.
- End Yr 3: opening investment = 3,17,208 + 3,33,068 = ₹6,50,276; interest 5% × ₹6,50,276 = **₹32,514**.

**WN-3 — Fund accumulation check.** Appropriations 3 × 3,17,208 = 9,51,624 + interest (15,860 + 32,514) = 48,374 → total **₹9,99,998 ≈ ₹10,00,000** (₹2 rounding). Investments in Year 3 are **not** made (funds are needed to redeem); investments are realised instead.

**Debenture Redemption Fund Investment A/c (₹):**

| Year | Particulars | Dr | Year | Particulars | Cr |
|---|---|---|---|---|---|
| Yr 1 end | To Bank | 3,17,208 | Yr 1 end | By Balance c/d | 3,17,208 |
| Yr 2 beg | To Balance b/d | 3,17,208 | Yr 3 beg | (carried) | |
| Yr 2 end | To Bank | 3,33,068 | Yr 2 end | By Balance c/d | 6,50,276 |
| Yr 3 beg | To Balance b/d | 6,50,276 | Yr 3 end | By Bank (realised) | 6,50,276 |

**Debenture Redemption Fund A/c (₹):**

| Year | Particulars | Dr | Year | Particulars | Cr |
|---|---|---|---|---|---|
| Yr 1 end | To Balance c/d | 3,17,208 | Yr 1 end | By P&L Appropriation | 3,17,208 |
| Yr 2 end | To Balance c/d | 6,50,276 | Yr 2 beg | By Balance b/d | 3,17,208 |
| | | | Yr 2 end | By Interest on Investment | 15,860 |
| | | | Yr 2 end | By P&L Appropriation | 3,17,208 |
| Yr 3 end | To General Reserve (transfer) | 10,00,000* | Yr 3 beg | By Balance b/d | 6,50,276 |
| | | | Yr 3 end | By Interest on Investment | 32,514 |
| | | | Yr 3 end | By P&L Appropriation | 3,17,208 |

*After redeeming the debentures out of the realised investments and bank, the accumulated fund (≈₹10,00,000) is transferred to **General Reserve**.

**Answer:** Annual appropriation **₹3,17,208**; interest re-invested ₹15,860 (Yr 2) and ₹32,514 (Yr 3); fund accumulates to ≈**₹10,00,000** by the end of Year 3, whereupon investments are realised, debentures redeemed at par, and the fund transferred to **General Reserve.**

**Why this way (the reasoning):** The sinking-fund method solves a cash-planning problem: instead of scrambling for ₹10,00,000 on the redemption date, the company builds it up steadily by setting aside a *smaller* fixed sum each year and letting **compound interest do part of the work** — that is exactly why the annual appropriation (₹3,17,208) is *less* than ₹10,00,000 ÷ 3 (₹3,33,333); the shortfall is made up by re-invested interest. The mechanics have two mirror accounts: the **Fund account** (an appropriation of profit, credited with the annual sum *and* the interest earned) measures how much profit has been retained; the **Investment account** measures the actual assets held to back it. Interest is earned only on the *opening* investment balance, so Year 1 earns nothing — a point students often botch by charging interest from Year 1. Crucially, in the **final year investments are not purchased** — the cash is needed to pay off debenture-holders, so the fund is completed by that year's appropriation and interest, then the investments are sold and the debentures redeemed. Post-redemption the fund is transferred to **General Reserve**, mirroring the DRR treatment, because it is now a free capital reserve. The method disciplines the company against the temptation to distribute those profits as dividend in the intervening years.

*(Full-marks tip: no interest in Year 1, interest only on opening investments, no fresh investment in the final year, and transfer the fund to General Reserve after redemption. Deductions for charging Year-1 interest or for investing in Year 3.)*

---

### Q68. Ch: Redemption of Debentures — DRR applicability under the amended Rules (Marks: 6) [Case/Application]
**Question:** Four companies plan to redeem debentures next year and ask whether they must create a **Debenture Redemption Reserve (DRR)** and whether they must make the **15% investment/deposit**: (i) a **listed** manufacturing company (public issue); (ii) an **unlisted** manufacturing company (public issue); (iii) an **NBFC registered with the RBI** (privately placed debentures); (iv) a **banking company**. State the correct position for each and the quantum, under the Companies (Share Capital and Debentures) Rules as amended in 2019.

**Answer:**
**Governing provision — Rule 18(7) of the Companies (Share Capital and Debentures) Rules, 2014, as amended w.e.f. 16.08.2019**, read with Sec. 71 of the Companies Act, 2013. The 2019 amendment **substantially reduced/removed** the DRR requirement for several classes of issuers, while retaining a **15% liquidity requirement (DRR-Investment / deposit)** for specified issuers.

Applying to each:

| Company | DRR required? | 15% investment/deposit? |
|---|---|---|
| **(i) Listed manufacturing (public issue)** | **No DRR** (listed companies are exempt from DRR after the amendment) | **Yes** — invest/deposit 15% of debentures maturing during the year ending 31 March next, by 30 April |
| **(ii) Unlisted manufacturing (public issue)** | **Yes — DRR = 10% of the outstanding value of debentures** | **Yes** — 15% liquidity requirement applies |
| **(iii) NBFC (RBI-registered), privately placed** | **No DRR** (NBFCs/HFCs exempt for privately placed debentures) | **No** 15% requirement for privately placed debentures of NBFCs/HFCs |
| **(iv) Banking company** | **No DRR** | **No** — exempt |

**The 15% rule (where applicable):** the company must, **on or before 30 April** of each year, **deposit or invest** a sum **not less than 15% of the amount of debentures maturing during the year ending on 31 March of the next year**, in the specified modes (e.g., deposits with scheduled banks, specified government/other securities). The sum so invested must not be used for any purpose other than redemption of those maturing debentures.

**Conclusion:** DRR (10%) is now confined mainly to **unlisted non-financial companies**; listed companies, banking companies and NBFCs/HFCs (privately placed) are **exempt from DRR**. The **15% liquidity** leg applies to listed and unlisted companies (and to NBFCs/HFCs only for their *public* issues), but **not** to privately placed NBFC/HFC debentures or banking companies.

**Why this way (the reasoning):** The 2019 amendment reflects a deliberate policy shift — **regulatory arbitrage was being removed** and compliance costs eased for issuers already subject to strong external discipline. Listed companies live under SEBI's continuous-disclosure and monitoring regime, and banks/NBFCs under RBI's capital and prudential norms, so Parliament judged a *separate* DRR (an internal profit ring-fence) largely redundant for them. The one class left carrying the full **10% DRR** is the **unlisted non-financial company**, precisely because it has the *least* external oversight and the *highest* risk that profits are distributed away before redemption. Yet even for exempt-from-DRR issuers, the amendment kept the **15% investment** for many because DRR (a reserve) protects *profits* but not *cash* — the 15% deposit forces genuine **liquidity** to exist near the maturity date, which is what actually pays the holders. The examinable insight is therefore the **decoupling of the two safeguards**: a reserve (solvency/appropriation) versus an investment (liquidity), each switched on for different issuers. Answering "10% DRR for everyone" (the pre-2019 position) is the classic outdated error.

*(Full-marks tip: give a class-wise table, state DRR = 10% of *outstanding* debentures only for unlisted non-financial companies, and explain the 15%-by-30-April liquidity rule separately. Deductions for applying the pre-amendment blanket 25%/10% DRR or for merging the DRR and 15% requirements.)*

### Q69. Ch: Investment Accounts — Cum-interest vs Ex-interest Purchase and Sale of Fixed-Interest Securities (Marks: 10) [Problem]
**Question:** On 1 April 2024 Vidya Ltd held ₹4,80,000 (nominal) 12% Government Stock at a book value of ₹4,60,000. Interest is payable half-yearly on 30 June and 31 December. The following transactions took place during the year ended 31 March 2025:

| Date | Transaction | Nominal Value (₹) | Price / Terms |
|---|---|---|---|
| 01-06-2024 | Purchased | 1,20,000 | ₹98 cum-interest |
| 01-09-2024 | Sold | 2,00,000 | ₹101 cum-interest |
| 01-12-2024 | Purchased | 1,00,000 | ₹96 ex-interest |
| 01-02-2025 | Sold | 1,50,000 | ₹99 ex-interest |

Interest for the half-years was received on the due dates. Vidya Ltd values its closing investment on a **weighted-average cost** basis. Prepare the **Investment Account (12% Government Stock)** in the books of Vidya Ltd showing Nominal, Interest and Cost (Principal) columns, and compute the profit/loss on sale.

**Solution:**

**WN-1 — Separating interest embedded in cum/ex-interest prices (the accrual logic):**
Coupon = 12% p.a. Half-year period runs 01-Jan→30-Jun and 01-Jul→31-Dec. Accrued interest = Nominal × 12% × (months since last coupon ÷ 12).

- 01-06 Purchase (cum): last coupon 31-Dec-23 → accrued 5 months (Jan–May). Interest = 1,20,000 × 12% × 5/12 = **₹6,000**. Total cost 1,20,000×98/100 = ₹1,17,600 → Principal = 1,17,600 − 6,000 = **₹1,11,600**.
- 01-09 Sale (cum): last coupon 30-Jun → accrued 2 months (Jul–Aug). Interest = 2,00,000 × 12% × 2/12 = **₹4,000**. Total proceeds 2,00,000×101/100 = ₹2,02,000 → Principal = 2,02,000 − 4,000 = **₹1,98,000**.
- 01-12 Purchase (ex): price is clean; accrued interest 5 months (Jul–Nov) is paid **additionally**. Principal = 1,00,000×96/100 = **₹96,000**; Interest paid = 1,00,000×12%×5/12 = **₹5,000**.
- 01-02 Sale (ex): clean price; buyer pays seller 1 month accrued (Jan). Principal = 1,50,000×99/100 = **₹1,48,500**; Interest received = 1,50,000×12%×1/12 = **₹1,500**.

**WN-2 — Weighted-average cost for computing profit on each sale:**
Opening avg cost = 4,60,000/4,80,000 = ₹0.9583 per ₹1.
- Before 01-09 sale: holdings = Opening (4,80,000 @ ₹4,60,000) + 01-06 purch (1,20,000 @ ₹1,11,600) = 6,00,000 nominal @ ₹5,71,600 → avg = 0.95267.
  Cost of 2,00,000 sold = 2,00,000 × 0.95267 = **₹1,90,533**. Profit = 1,98,000 − 1,90,533 = **₹7,467**.
- After sale, balance = 4,00,000 nominal @ (5,71,600 − 1,90,533) = ₹3,81,067.
- Before 01-02 sale: + 01-12 purch (1,00,000 @ ₹96,000) = 5,00,000 nominal @ ₹4,77,067 → avg = 0.95413.
  Cost of 1,50,000 sold = 1,50,000 × 0.95413 = **₹1,43,120**. Profit = 1,48,500 − 1,43,120 = **₹5,380**.
- Closing balance = 3,50,000 nominal @ (4,77,067 − 1,43,120) = **₹3,33,947**.

**WN-3 — Interest column (income earned):**
30-Jun coupon on holding 6,00,000 = ₹36,000; 31-Dec coupon on holding 4,00,000 = ₹24,000. Plus accrued-in on purchases and accrued-out on sales as above. Closing accrued interest 01-Jan→31-Mar on 3,50,000 = 3,50,000×12%×3/12 = **₹10,500**.

**Investment Account — 12% Government Stock (for year ended 31-03-2025)**

| Date | Particulars | Nominal ₹ | Interest ₹ | Cost ₹ | Date | Particulars | Nominal ₹ | Interest ₹ | Cost ₹ |
|---|---|---|---|---|---|---|---|---|---|
| 01-04 | To Balance b/d | 4,80,000 | 14,400 | 4,60,000 | 30-06 | By Bank (int.) | — | 36,000 | — |
| 01-06 | To Bank | 1,20,000 | 6,000 | 1,11,600 | 01-09 | By Bank (sale) | 2,00,000 | 4,000 | 1,98,000 |
| 01-12 | To Bank | 1,00,000 | 5,000 | 96,000 | 31-12 | By Bank (int.) | — | 24,000 | — |
| 31-03 | To P&L (int.) | — | 62,480 | — | 01-02 | By Bank (sale) | 1,50,000 | 1,500 | 1,48,500 |
| 31-03 | To P&L (profit) | — | — | 12,847 | 31-03 | By Balance c/d | 3,50,000 | 10,500 | 3,33,947 |
| | **Total** | **7,00,000** | **87,880** | **6,80,447** | | **Total** | **7,00,000** | **65,500** | **6,80,447** |

Opening accrued interest b/d = 4,80,000×12%×3/12 = ₹14,400 (01-Jan→31-Mar). Interest to P&L balancing = 65,500 + 10,500 (c/d) − 14,400 − 6,000 − 5,000 = **₹62,480**.

**Answer:** Profit on sale credited to P&L = ₹7,467 + ₹5,380 = **₹12,847**; Interest income for the year = **₹62,480**; Closing investment (3,50,000 nominal) carried at **₹3,33,947** cost + ₹10,500 accrued interest.

**Why this way (the reasoning):** The whole discipline of the three-column investment account is to keep **capital (Principal) apart from revenue (Interest)**, because profit on sale must be measured only on the capital element — accrued interest is income, not part of what you "paid for the asset." A cum-interest price bundles the next coupon into the quoted figure, so you strip it out (buyer is effectively pre-paying the seller for interest already run up); an ex-interest price is already clean, so accrued interest is added on top. The tempting wrong approach — treating the full cum-interest outlay as cost — overstates the asset and understates interest income, and then the profit on sale is computed on an inflated base, distorting both the P&L classification and the carrying amount.

*(Full-marks tip: examiners award the split of every cum/ex price into interest vs principal and the month-count of accrual; the biggest deduction is forgetting that ex-interest means interest is paid *in addition* to the clean price, and mixing the two directions of accrual.)*

---

### Q70. Ch: Investment Accounts — Bonus Issue, Rights Issue and Sale of Rights (Marks: 8) [Problem]
**Question:** On 1 April 2024 Meera held 10,000 equity shares of Anand Ltd (face ₹10) at a cost of ₹1,80,000 (i.e. ₹18 each). The following occurred during 2024-25:

| Date | Event |
|---|---|
| 01-07-2024 | Company declared a bonus of 1 share for every 4 held. |
| 01-10-2024 | Company made a rights issue of 1 share for every 5 held (post-bonus) at ₹15; market price cum-rights ₹24. |
| 01-10-2024 | Meera subscribed to 60% of her rights and **sold the balance rights in the market at ₹6 per right**. |
| 01-02-2025 | Sold 5,000 shares at ₹26 each. |

Prepare the **Investment Account (Equity Shares of Anand Ltd)** and state the profit on sale. Investments are carried at average cost.

**Solution:**

**WN-1 — Bonus shares (01-07):** Bonus = 10,000 ÷ 4 = **2,500 shares** at **nil cost**. Nominal added = 2,500×10 = ₹25,000; cost added = ₹0. Holding now 12,500 shares; cost still ₹1,80,000.

**WN-2 — Rights entitlement (01-10):** Rights = 12,500 ÷ 5 = **2,500 rights shares** offered at ₹15.
- Subscribed 60% = **1,500 shares** → cash paid = 1,500×15 = **₹22,500** (added to cost, nominal ₹15,000).
- Rights renounced (sold) = 40% = 1,000 rights × ₹6 = **₹6,000**.

**WN-3 — Treatment of sale of rights (the key judgement):** The 1,000 rights sold relate to shares **not yet owned** (mere entitlement, no cost carried for them). Where rights are renounced without ever being taken up, the sale proceeds are **credited to the Profit & Loss Account as income** (not reduced from cost of the investment), because there is no cost of the underlying to write down. Hence ₹6,000 → **P&L**, cost column unaffected.

**WN-4 — Average cost after rights:** Holding = 12,500 + 1,500 = **14,000 shares**; total cost = 1,80,000 + 22,500 = **₹2,02,500** → avg = ₹14.464 per share.

**WN-5 — Sale on 01-02 (5,000 shares @ ₹26):** Proceeds = ₹1,30,000. Cost of 5,000 = 5,000 × 14.464 = **₹72,321**. **Profit = ₹57,679.** Balance 9,000 shares @ (2,02,500 − 72,321) = **₹1,30,179**.

**Investment Account — Equity Shares, Anand Ltd**

| Date | Particulars | No. | Cost ₹ | Date | Particulars | No. | Cost ₹ |
|---|---|---|---|---|---|---|---|
| 01-04 | To Balance b/d | 10,000 | 1,80,000 | 01-02 | By Bank (sale) | 5,000 | 1,30,000 |
| 01-07 | To Bonus | 2,500 | — | 31-03 | By Balance c/d | 9,000 | 1,30,179 |
| 01-10 | To Bank (rights) | 1,500 | 22,500 | | | | |
| 01-02 | To P&L (profit) | — | 57,679 | | | | |
| | **Total** | **14,000** | **2,60,179** | | **Total** | **14,000** | **2,60,179** |

Sale of rights ₹6,000 is credited directly to P&L (not shown in the investment cost column).

**Answer:** Profit on sale of shares = **₹57,679**; income from sale of rights = **₹6,000** to P&L; closing holding **9,000 shares** at cost **₹1,30,179** (avg ₹14.46).

**Why this way (the reasoning):** Bonus shares carry **no cost** because the company merely capitalises reserves — you get more paper for the same money, so average cost per share must fall (the market drop that follows is exactly this dilution). Rights are different: if you *subscribe*, the cash paid is genuine additional cost of a genuine additional asset. But if you *sell the rights without subscribing*, you have realised value from an entitlement for which you carry no cost, so the proceeds are pure income → P&L. The common trap is to net the ₹6,000 rights-sale proceeds against the cost of the investment; that is only correct when the rights relate to shares you *do* hold and you are trying to reflect the fall in their value — here the rights were renounced, so there is nothing to write down.

*(Full-marks tip: state explicitly that bonus is nil-cost and that renounced-rights proceeds go to P&L; students routinely lose marks either by valuing bonus shares at market or by wrongly deducting rights-sale money from cost.)*

---

### Q71. Ch: Investment Accounts — Right Renounced *Partly Sold, Partly Taken* with Cost Adjustment (Marks: 6) [Case/Application]
**Question:** An investor holds 8,000 shares (cost ₹96,000). A rights issue of 1:4 at ₹20 is announced when the cum-rights price is ₹35 and the theoretical ex-rights price works out to ₹32. The investor is advised by a friend that "the money received from selling rights should always be credited to the Investment Account to reduce cost, and rights you subscribe never affect cost." **Examine the validity** of this advice and state the correct accounting treatment, distinguishing the two situations.

**Answer:**

**Governing principle (AS 13 / Investment Accounting convention):** Investments are carried at **cost**, and cost is adjusted only for events that genuinely change the carrying amount of *shares actually held*. The treatment of rights turns on whether the entitlement is **subscribed** or **renounced (sold)**, and on whether the rights relate to shares the investor already owns.

**Application to the two limbs of the friend's advice:**
1. *"Proceeds from selling rights always reduce cost."* — **Only partly correct.** When rights are renounced (sold in the market) and the shares are **not** subscribed, the standard treatment is to credit the sale proceeds to **Profit & Loss** as income, because the investor carries no cost for shares never acquired. However, some texts permit reducing cost where the sale is made to restore the fall in value of existing holdings shortly after purchase — but the mainstream ICAI treatment is P&L. It is therefore *not* an absolute rule that proceeds always reduce cost.
2. *"Subscribed rights never affect cost."* — **Incorrect.** When the investor **subscribes**, the cash paid (here ₹20 per rights share) is genuine additional cost and is **added** to the Investment Account, increasing both the number of shares and the total cost.

**Numbers for illustration:** Rights = 8,000/4 = 2,000 shares. If investor subscribes all → add 2,000×20 = ₹40,000 to cost (holding 10,000 @ ₹1,36,000). If instead all 2,000 rights are sold at, say, ₹9 (≈ 35−32×... intrinsic value ₹35−₹20 spread reflected in the ₹3 fall) → ₹18,000 credited to P&L, cost unchanged at ₹96,000.

**Conclusion/Advice:** The advice is invalid as a blanket rule. Correct treatment: **subscribed rights → add cash paid to Investment Account (cost rises)**; **renounced/sold rights → credit proceeds to P&L** (cost of existing holding is normally left undisturbed). The friend has reversed both halves of the rule.

**Why this way (the reasoning):** The logic is "match cost to the asset you actually own." Subscribing creates a new asset paid for in cash — that cash is unambiguously cost. Selling a right monetises a *privilege* attached to shares you hold but creates no new asset, so the receipt is a gain, not a cost recovery. Calling subscription "cost-neutral" would make the balance sheet understate the investment (you'd have paid ₹40,000 and shown nothing), while routinely netting rights-sale proceeds against cost would understate the true carrying value of retained shares.

*(Full-marks tip: the examiner wants the *distinction* drawn crisply with the P&L-vs-cost rationale; a mere restatement of one rule without contrasting subscribe-vs-renounce earns half marks.)*

---

### Q72. Ch: Investment Accounts — Ex-Interest Purchase Straddling a Coupon with Brokerage (Marks: 6) [Problem]
**Question:** On 1 August 2024 Rohan purchased ₹2,00,000 (nominal) 10% Debentures of Zeal Ltd at ₹94 ex-interest. Brokerage was 1% of the price and stamp/transfer charges ₹400. Interest is payable on 30 September and 31 March. On 1 December 2024 he sold ₹80,000 (nominal) at ₹97 cum-interest, brokerage 1%. Show how you would compute (a) the principal cost of the purchase, (b) the interest received on 30 Sept, and (c) the profit/loss on the 1 Dec sale. Investments valued at average cost.

**Solution:**

**WN-1 — Principal cost of purchase (01-08, ex-interest):** Clean price = 2,00,000×94/100 = ₹1,88,000. Brokerage (added to cost on purchase) = 1% × 1,88,000 = ₹1,880. Stamp = ₹400. **Principal cost = 1,88,000 + 1,880 + 400 = ₹1,90,280.** Accrued interest paid separately (ex-interest, last coupon 31-Mar → Apr–Jul = 4 months) = 2,00,000×10%×4/12 = **₹6,667** (debited to interest column, not cost).

**WN-2 — Interest received 30-Sept:** Half-year coupon on ₹2,00,000 = 2,00,000×10%×6/12 = **₹10,000**. Of this, ₹6,667 relates to the pre-purchase period already paid to seller; net income for Rohan = 10,000 − 6,667 = **₹3,333** (the account self-corrects because ₹6,667 sits on the debit of the interest column).

**WN-3 — Sale 01-12 (cum-interest, ₹80,000 @ ₹97):** Gross = 80,000×97/100 = ₹77,600. Brokerage (deducted on sale) = 1%×77,600 = ₹776 → net realisation ₹76,824. Accrued interest in cum price (last coupon 30-Sep → Oct–Nov = 2 months) = 80,000×10%×2/12 = **₹1,333**. **Principal proceeds = 76,824 − 1,333 = ₹75,491.**

**WN-4 — Cost of ₹80,000 sold (average cost):** Avg = 1,90,280/2,00,000 = ₹0.9514 per ₹1. Cost of 80,000 = ₹76,112. **Loss on sale = 75,491 − 76,112 = ₹621 (loss).**

**Answer:** (a) Principal cost = **₹1,90,280**; (b) coupon received 30-Sept = **₹10,000** (net income ₹3,333 after the ₹6,667 accrual paid on purchase); (c) **loss on sale = ₹621**.

**Why this way (the reasoning):** Brokerage and stamp are **transaction costs of acquiring the asset**, so on purchase they are *added* to principal cost (they are part of what you sacrificed to own it); on sale they *reduce* the realisation (they are a cost of disposing). Interest accrued to the date of purchase belongs to the seller — you reimburse it as part of an ex-interest deal, so it goes to the interest column and is later recovered when the full coupon arrives, leaving only *your* share as income. The wrong instinct is to lump brokerage and accrued interest into one "cost" figure; that would corrupt the profit-on-sale calculation (measured only on principal) and misclassify interest income.

*(Full-marks tip: show brokerage moving in opposite directions on buy vs sell, and net the accrued interest against the coupon; a frequent error is adding brokerage to interest or ignoring it on the sale side.)*

---

### Q73. Ch: Investment Accounts — Integrated: Bonus after Rights, then Cum-Dividend Sale (Marks: 10) [Problem]
**Question:** On 1 April 2024 Kavya held 20,000 equity shares of Orbit Ltd (face ₹10) at cost ₹3,40,000. Transactions in 2024-25:

| Date | Event |
|---|---|
| 01-06-2024 | Rights 1:5 at ₹18; Kavya took up all rights. |
| 01-09-2024 | Company paid dividend @ 15% on paid-up capital (all shares fully paid ₹10) — dividend was declared out of pre-acquisition profits to the extent of ₹0.60 per original share. |
| 01-11-2024 | Bonus 1:2 on holdings as on that date. |
| 01-02-2025 | Sold 12,000 shares at ₹22 cum-dividend (no dividend actually accrued; "cum-dividend" here only reflects an expected future dividend and is ignored). |

Prepare the **Investment Account** and show profit on sale (average cost).

**Solution:**

**WN-1 — Rights (01-06):** Rights = 20,000/5 = 4,000 shares @ ₹18 = **₹72,000** added to cost. Holding = 24,000; cost = 3,40,000 + 72,000 = **₹4,12,000**.

**WN-2 — Dividend (01-09) and the pre-acquisition portion:** Dividend @15% on 24,000 shares×₹10 = ₹36,000 gross. But ₹0.60 per **original** share (20,000) = ₹12,000 relates to **pre-acquisition profits** → this portion is **capital receipt, credited to the Investment Account (reduces cost)**, not income. Revenue dividend to P&L = 36,000 − 12,000 = **₹24,000**.
Cost after dividend adjustment = 4,12,000 − 12,000 = **₹4,00,000**; holding 24,000.

**WN-3 — Bonus (01-11):** Bonus = 24,000/2 = **12,000 shares nil cost**. Holding = 36,000; cost unchanged ₹4,00,000. Avg = ₹11.111 per share.

**WN-4 — Sale (01-02, 12,000 @ ₹22):** Proceeds = ₹2,64,000 (cum-dividend ignored as instructed). Cost of 12,000 = 12,000 × 11.111 = **₹1,33,333**. **Profit = ₹1,30,667.** Balance 24,000 @ (4,00,000 − 1,33,333) = **₹2,66,667**.

**Investment Account — Equity Shares, Orbit Ltd**

| Date | Particulars | No. | Cost ₹ | Date | Particulars | No. | Cost ₹ |
|---|---|---|---|---|---|---|---|
| 01-04 | To Balance b/d | 20,000 | 3,40,000 | 01-09 | By Bank (pre-acq. div.) | — | 12,000 |
| 01-06 | To Bank (rights) | 4,000 | 72,000 | 01-02 | By Bank (sale) | 12,000 | 2,64,000 |
| 01-11 | To Bonus | 12,000 | — | 31-03 | By Balance c/d | 24,000 | 2,66,667 |
| 01-02 | To P&L (profit) | — | 1,30,667 | | | | |
| | **Total** | **36,000** | **5,42,667** | | **Total** | **36,000** | **5,42,667** |

Revenue dividend ₹24,000 credited to P&L separately.

**Answer:** Profit on sale = **₹1,30,667**; revenue dividend income = **₹24,000**; closing holding **24,000 shares** at cost **₹2,66,667** (avg ₹11.11).

**Why this way (the reasoning):** The engine here is the **pre-acquisition-profit rule**: a dividend paid out of profits earned *before* you bought the shares is, in substance, a return of part of your purchase price — you are being handed back money that was already reflected in the price you paid — so it reduces cost rather than counting as income. Bonus dilutes cost per share (nil-cost paper); rights add real cost. Getting the order right matters: the dividend adjustment must hit cost *before* the bonus recomputes the average, otherwise the per-share cost carried into the sale is wrong. The classic trap is to treat the entire ₹36,000 as income — that overstates P&L and leaves the investment carried too high, so the later profit on sale is understated.

*(Full-marks tip: the examiner specifically checks the pre-acquisition split going to *cost* and the nil-cost bonus; treating pre-acquisition dividend as income is the single most common and heavily penalised error.)*

---

### Q74. Ch: Internal Reconstruction — Capital Reduction Scheme with Surplus Utilisation (Marks: 10) [Problem]
**Question:** The summarised Balance Sheet of Nimbus Ltd as at 31 March 2025 is:

| Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| 40,000 Equity shares of ₹100 | 40,00,000 | Goodwill | 6,00,000 |
| 10% Preference shares of ₹100 (20,000) | 20,00,000 | Patents | 3,00,000 |
| 12% Debentures | 15,00,000 | Land & Building | 22,00,000 |
| Interest accrued on debentures | 1,80,000 | Plant & Machinery | 24,00,000 |
| Trade payables | 9,00,000 | Stock | 8,50,000 |
| Bank overdraft | 4,20,000 | Trade receivables | 7,00,000 |
| | | Profit & Loss (Dr.) | 19,50,000 |
| **Total** | **90,00,000** | **Total** | **90,00,000** |

The reconstruction scheme, approved by the court, provides:
1. Equity shares reduced to ₹40 each, fully paid.
2. 10% Preference shares reduced to ₹70 each; arrears of preference dividend of 2 years (not in books) to be cancelled.
3. Debenture-holders agreed to forgo ₹1,80,000 accrued interest and to accept a reduction of their claim to ₹13,50,000; rate reduced to 10%.
4. Trade payables agreed to forgo 25% of their claim.
5. Goodwill, Patents and the P&L debit balance to be written off; Land & Building to be revalued upward by ₹4,00,000; Plant & Machinery written down to ₹18,00,000; Stock reduced by ₹1,50,000; a provision of ₹70,000 to be made on receivables.

Pass the amount available and prepare the **Capital Reduction (Reconstruction) Account**, showing whether the scheme leaves any capital reserve.

**Solution:**

**WN-1 — Sacrifice by shareholders and creditors (sources / credit side):**
- Equity: 40,000 × (100 − 40) = **₹24,00,000**.
- Preference: 20,000 × (100 − 70) = **₹6,00,000**.
- Debentures: claim 15,00,000 → 13,50,000 = **₹1,50,000**; plus accrued interest waived **₹1,80,000**.
- Trade payables: 25% × 9,00,000 = **₹2,25,000**.
- **Total available = 24,00,000 + 6,00,000 + 1,50,000 + 1,80,000 + 2,25,000 = ₹35,55,000.**

**WN-2 — Losses / assets written down (applications / debit side):**
- Goodwill ₹6,00,000 + Patents ₹3,00,000 + P&L (Dr.) ₹19,50,000 = ₹28,50,000.
- Plant & Machinery: 24,00,000 → 18,00,000 = ₹6,00,000 down.
- Stock ₹1,50,000 + Provision on receivables ₹70,000 = ₹2,20,000.
- **Total write-offs = 28,50,000 + 6,00,000 + 2,20,000 = ₹36,70,000.**
- **Less** upward revaluation of Land & Building **₹4,00,000** (a credit that funds write-offs).

**WN-3 — Preference dividend arrears:** Cancellation of ₹4,00,000 (2 yrs × 10% × ₹20,00,000) arrears — **not in the books**, so no accounting entry; only a note. It does not enter the Capital Reduction Account.

**Capital Reduction (Reconstruction) Account**

| Particulars | ₹ | Particulars | ₹ |
|---|---|---|---|
| To Goodwill | 6,00,000 | By Equity Share Capital | 24,00,000 |
| To Patents | 3,00,000 | By 10% Preference Share Capital | 6,00,000 |
| To Profit & Loss A/c | 19,50,000 | By 12% Debentures (reduction) | 1,50,000 |
| To Plant & Machinery | 6,00,000 | By Interest accrued (waived) | 1,80,000 |
| To Stock | 1,50,000 | By Trade payables | 2,25,000 |
| To Provision for doubtful debts | 70,000 | By Land & Building (appreciation) | 4,00,000 |
| To Capital Reserve (bal. fig.) | 2,85,000 | | |
| **Total** | **39,55,000** | **Total** | **39,55,000** |

**Answer:** Total sacrifice (₹35,55,000) plus revaluation surplus (₹4,00,000) = ₹39,55,000; write-offs = ₹36,70,000; **Capital Reserve = ₹2,85,000** carried forward. The scheme is viable and leaves a small capital reserve.

**Why this way (the reasoning):** Internal reconstruction rests on a single equation: **value sacrificed by insiders (shareholders, debenture-holders, creditors) must at least cover the accumulated losses and asset overstatements** you want to purge, so the company can start with a clean, realistic balance sheet. Every reduction in a claim frees up "notional cash" that is pooled in the Capital Reduction Account and spent on writing off fictitious assets (goodwill, P&L debit) and overvalued real assets. Upward revaluation of a genuinely undervalued asset is *also* a source because it releases surplus into the same pool. Any excess after all write-offs cannot go to P&L (it did not arise from trading) — it is a **capital reserve**. The trap is to route the preference-dividend arrears cancellation through the account: since arrears were never recorded (dividends aren't a liability until declared), cancelling them is a memorandum note only.

*(Full-marks tip: examiners look for the arrears being disclosed by note (no entry), the revaluation surplus used as a *source*, and the balancing figure correctly labelled Capital Reserve — not transferred to P&L. Mislabelling the balance or passing an entry for arrears loses 2-3 marks.)*

---

### Q75. Ch: Internal Reconstruction — Sub-division, Consolidation and Fresh Issue to Fund Cash Needs (Marks: 8) [Problem]
**Question:** As part of a reconstruction, Crest Ltd (share capital: 1,00,000 equity shares of ₹10, fully paid, ₹10,00,000) undertakes:
1. Each ₹10 share is **sub-divided** into 10 shares of ₹1, then the **paid-up value written down** to ₹0.40 per ₹1 share (i.e., ₹0.60 sacrificed per re-denominated share).
2. The company then **consolidates** every 5 shares of ₹0.40 paid into 1 share of ₹2 (₹2 face, ₹2 paid).
3. To provide working capital, the company issues **2,00,000 new equity shares of ₹2 at par**, fully paid in cash.

Accumulated losses and asset write-downs requiring adjustment total ₹6,00,000. Show (a) the capital sacrificed and whether it covers the ₹6,00,000, (b) the number and denomination of shares after each step, and (c) the cash raised and post-scheme equity capital.

**Solution:**

**WN-1 — After sub-division:** 1,00,000 × 10 = **10,00,000 shares of ₹1**, ₹1 paid → capital ₹10,00,000 (no change in total, only denomination).

**WN-2 — Write-down of paid value:** Each ₹1 share written down to ₹0.40 paid → sacrifice = ₹0.60 × 10,00,000 = **₹6,00,000**. Paid-up capital now 10,00,000 × ₹0.40 = **₹4,00,000**.

**WN-3 — Consolidation:** Every 5 shares (₹0.40 paid = ₹2.00 total) → 1 share of ₹2 fully paid. Number = 10,00,000 ÷ 5 = **2,00,000 shares of ₹2** = ₹4,00,000. (Capital unchanged, only regrouped.)

**WN-4 — Fresh issue for cash:** 2,00,000 shares × ₹2 = **₹4,00,000 cash raised**. Equity now 2,00,000 (old) + 2,00,000 (new) = **4,00,000 shares of ₹2 = ₹8,00,000**.

**Reconciliation of capital sacrifice vs losses:**

| Item | ₹ |
|---|---|
| Sacrifice on write-down (WN-2) | 6,00,000 |
| Accumulated losses / write-downs to absorb | 6,00,000 |
| Surplus / (Deficit) | Nil |

**Answer:** (a) Sacrifice = **₹6,00,000**, exactly covering the ₹6,00,000 losses (no capital reserve, no shortfall). (b) 1,00,000 ×₹10 → 10,00,000 ×₹1 (₹0.40 paid) → **2,00,000 ×₹2 fully paid**. (c) Cash raised = **₹4,00,000**; post-scheme equity capital = **₹8,00,000** (4,00,000 shares of ₹2).

**Why this way (the reasoning):** Three distinct capital manoeuvres are at work and only one of them actually destroys value. **Sub-division** and **consolidation** are purely cosmetic re-denominations — total capital is untouched, you are just changing the size of the "unit" (helpful because a viable share must have a face value that markets will accept). The **write-down of paid-up value** is the only step that reduces capital, and that reduction is the source that absorbs losses. The **fresh issue** is separate again — reconstruction cures the *balance sheet* but not the *cash* problem, so a genuine cash injection is needed for working capital. Students often muddle sub-division/consolidation with reduction and double-count the sacrifice, or forget that only the write-down (not the regrouping) frees value to absorb losses.

*(Full-marks tip: track the *number × denomination × paid value* at each step and show that only the write-down changes total capital; conflating consolidation with a reduction of capital is the usual error.)*

---

### Q76. Ch: Internal Reconstruction — Debenture-holders Taking Over Assets + Contingent Liability Crystallising (Marks: 8) [Problem]
**Question:** Under a court-approved scheme for Delta Ltd:
1. 14% Debenture-holders (₹20,00,000) agree to accept Land (book value ₹8,00,000, revalued ₹11,00,000) in part settlement and to reduce the balance of their debentures by 20%.
2. A pending damages suit crystallises: ₹1,50,000 must now be provided (contingent liability, previously only disclosed).
3. Directors agree to waive loans of ₹3,00,000 given by them.
4. Equity capital (2,00,000 shares of ₹10) reduced to ₹6 per share.
5. Balance available is used to write off Debit P&L ₹9,00,000 and to write down Machinery; any residue is credited to Capital Reserve.

Compute the amount available, the amount by which Machinery is written down if the scheme leaves a Capital Reserve of ₹50,000, and prepare the **Capital Reduction Account**.

**Solution:**

**WN-1 — Debenture settlement:** Balance after taking Land = 20,00,000 − 11,00,000 = ₹9,00,000. Reduction 20% of this balance = 20% × 9,00,000 = **₹1,80,000** sacrifice by debenture-holders. Land given at revalued ₹11,00,000 vs book ₹8,00,000 → revaluation gain ₹3,00,000 is a **source**.

**WN-2 — Directors' loan waiver:** **₹3,00,000** source.

**WN-3 — Equity reduction:** 2,00,000 × (10 − 6) = **₹8,00,000** source.

**WN-4 — Contingent liability crystallising:** Now a real liability → **₹1,50,000 application** (a fresh loss to absorb).

**WN-5 — Total sources and required write-off of Machinery:**

| Sources | ₹ |
|---|---|
| Equity reduction | 8,00,000 |
| Debenture reduction | 1,80,000 |
| Land revaluation gain | 3,00,000 |
| Directors' loan waived | 3,00,000 |
| **Total sources** | **15,80,000** |

| Applications | ₹ |
|---|---|
| P&L (Dr.) written off | 9,00,000 |
| Provision for damages suit | 1,50,000 |
| Capital Reserve (given) | 50,000 |
| Machinery written down (bal. fig.) | **4,80,000** |
| **Total applications** | **15,80,000** |

**Capital Reduction Account**

| Particulars | ₹ | Particulars | ₹ |
|---|---|---|---|
| To Profit & Loss A/c | 9,00,000 | By Equity Share Capital | 8,00,000 |
| To Provision for damages | 1,50,000 | By 14% Debentures | 1,80,000 |
| To Machinery | 4,80,000 | By Land & Building (revaluation) | 3,00,000 |
| To Capital Reserve | 50,000 | By Directors' Loan | 3,00,000 |
| **Total** | **15,80,000** | **Total** | **15,80,000** |

**Answer:** Amount available (sources) = **₹15,80,000**; Machinery is written down by **₹4,80,000** to leave a Capital Reserve of ₹50,000.

**Why this way (the reasoning):** Two subtle mechanics drive this. First, when debenture-holders **take over an asset**, they accept it at its *agreed (revalued)* figure — so the excess of that figure over book value is a revaluation surplus available to the scheme, and only the *residual* claim (after deducting the asset value) is what the 20% reduction bites on. Applying the 20% to the full ₹20,00,000 would double-count the value already handed over as Land. Second, a **contingent liability that crystallises** is no longer a mere note — it becomes a real obligation, so it is an *additional loss* to be absorbed, sitting on the debit side alongside the P&L write-off. The balancing figure (Machinery write-down) then falls out once the desired Capital Reserve is pegged. The trap is forgetting that the crystallised suit *consumes* reconstruction resources rather than being ignored.

*(Full-marks tip: apply the 20% reduction to the *net* debenture balance after the asset takeover, and treat the crystallised suit as an application; errors on either point throw the Machinery balancing figure off.)*

---

### Q77. Ch: Internal Reconstruction — Validity of a Scheme (Buy-back vs Reduction Confusion) (Marks: 5) [Case/Application]
**Question:** The directors of Frontier Ltd, which has accumulated losses of ₹40,00,000 and a debit P&L balance, propose the following as an "internal reconstruction": (i) the company will *buy back* 30% of its equity shares from willing shareholders at par and cancel them; (ii) the amount of share capital so cancelled will be used to write off the accumulated losses; (iii) no court/tribunal approval will be obtained since "the shareholders agree." **Comment on the validity** of treating this as an internal reconstruction and advise the correct route.

**Answer:**

**Governing principle:** Internal reconstruction under Sections 61 and 66 of the Companies Act, 2013 involves **alteration and reduction of share capital** — writing down the paid/called-up value or cancelling capital *unrepresented by available assets* — to absorb accumulated losses, and it requires a **special resolution and confirmation by the National Company Law Tribunal (NCLT)** under Section 66. A **buy-back** (Section 68) is a fundamentally different transaction: it returns cash (or kind) to shareholders and is subject to its own conditions (funded out of free reserves/securities premium/fresh issue proceeds, 25% limit, debt-equity 2:1, etc.), and buy-back **cannot be used to write off accumulated losses** — indeed a company sitting on losses generally lacks the free reserves that fund a buy-back.

**Application to the facts:**
- Point (i)–(ii): Using a *buy-back at par* and then "using the cancelled capital to write off losses" is conceptually wrong — a buy-back *pays out* value to exiting shareholders (a cash outflow), it does not *free up* value to absorb losses. Reconstruction does the opposite: shareholders **sacrifice** value (their shares are written down) and that sacrifice absorbs the losses with **no cash leaving the company**. Frontier, being loss-laden and short of reserves, likely cannot even satisfy the buy-back funding conditions.
- Point (iii): Dispensing with Tribunal approval is invalid. A reduction of capital under Section 66 **mandatorily** requires NCLT confirmation (creditors' interests must be protected); mere shareholder agreement is insufficient.

**Conclusion/Advice:** The proposal is **not a valid internal reconstruction**. The company should instead pass a **special resolution for reduction of capital under Section 66**, writing down the paid-up value of *all* equity shares (the sacrifice), route the released capital through a Capital Reduction Account to write off the ₹40,00,000 losses and debit P&L balance, and obtain **NCLT confirmation**. A buy-back is the wrong instrument and cannot be used to eliminate losses.

**Why this way (the reasoning):** The heart of the matter is *direction of value flow*. Reconstruction works because shareholders **give up** book value they were never going to realise (capital "lost or unrepresented by assets"), and that internally generated sacrifice cleans the balance sheet without any cash moving. A buy-back **pushes cash out** to shareholders — the exact opposite — so it can never be the engine that absorbs losses, and the law rightly gates capital reductions behind Tribunal scrutiny to protect creditors whose cushion is being altered. Confusing the two treats a cash *outflow* as if it were a loss-absorbing *source*, which is economically impossible.

*(Full-marks tip: name Section 66 (reduction, NCLT route) vs Section 68 (buy-back) and stress that reconstruction absorbs losses via sacrifice with no cash outflow; simply saying "buy-back is not allowed" without the value-flow reasoning caps you at half marks.)*

---

### Q78. Ch: Internal Reconstruction — Post-Scheme Balance Sheet Preparation (Marks: 10) [Problem]
**Question:** Continuing from Nimbus Ltd (Q74), after the scheme is carried out prepare the **reconstructed Balance Sheet** (extracts of Equity & Liabilities and Assets) as at 1 April 2025. Use the balances and adjustments from the scheme in Q74. Assume bank overdraft and non-adjusted items remain unchanged.

**Solution:**

**WN-1 — Revised capital and claims (from Q74):**
- Equity: 40,000 × ₹40 = **₹16,00,000**.
- 10% Preference: 20,000 × ₹70 = **₹14,00,000**.
- 12% (now 10%) Debentures: **₹13,50,000**; accrued interest **nil** (waived).
- Trade payables: 9,00,000 − 2,25,000 = **₹6,75,000**.
- Bank overdraft **₹4,20,000** (unchanged).
- Capital Reserve **₹2,85,000** (from Q74).

**WN-2 — Revised assets:**
- Goodwill nil; Patents nil; P&L debit nil (all written off).
- Land & Building: 22,00,000 + 4,00,000 = **₹26,00,000**.
- Plant & Machinery: **₹18,00,000**.
- Stock: 8,50,000 − 1,50,000 = **₹7,00,000**.
- Trade receivables: 7,00,000 − 70,000 provision = **₹6,30,000**.

**Reconstructed Balance Sheet of Nimbus Ltd as at 1 April 2025 (extract)**

| Equity & Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Equity share capital (40,000 × ₹40) | 16,00,000 | Land & Building | 26,00,000 |
| 10% Preference capital (20,000 × ₹70) | 14,00,000 | Plant & Machinery | 18,00,000 |
| Capital Reserve | 2,85,000 | Stock | 7,00,000 |
| 10% Debentures | 13,50,000 | Trade receivables (net) | 6,30,000 |
| Trade payables | 6,75,000 | | |
| Bank overdraft | 4,20,000 | | |
| **Total** | **57,30,000** | **Total** | **57,30,000** |

**Answer:** The reconstructed balance sheet totals **₹57,30,000** on each side; fictitious assets and the debit P&L are eliminated, and a Capital Reserve of ₹2,85,000 appears — the balance sheet is now clean and self-balancing.

**Why this way (the reasoning):** The post-scheme balance sheet is the *proof* that the reconstruction is arithmetically sound: every reduction of a claim on the liabilities side must be exactly matched by the write-off/revaluation on the asset side, with the surplus surfacing as Capital Reserve. Preparing it forces you to carry through each scheme clause consistently — the same ₹4,00,000 revaluation that acted as a *source* in the Capital Reduction Account must show up as an *increased* Land value here. If the two sides don't tie, an item was double-counted or omitted in the reduction account. The reduced figures (₹40 equity, ₹70 preference, ₹13,50,000 debentures) are the *new* carrying claims — showing them at old values would leave the sheet unbalanced by exactly the sacrifice amount.

*(Full-marks tip: ensure the Capital Reserve from the reduction account flows onto the balance sheet and that the totals tie; a mismatch signals an internal error and the examiner will trace it — carry every clause through consistently.)*

---

### Q79. Ch: Amalgamation of Companies (AS 14) — Purchase Consideration by Net Payments vs Net Assets (Marks: 8) [Problem]
**Question:** Sun Ltd is absorbed by Moon Ltd. The Balance Sheet of Sun Ltd shows:

| Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Equity capital (50,000 × ₹10) | 5,00,000 | Sundry fixed assets | 8,20,000 |
| General reserve | 2,10,000 | Stock | 2,40,000 |
| 12% Debentures | 3,00,000 | Debtors | 1,80,000 |
| Trade payables | 1,50,000 | Bank | 20,000 |
| **Total** | **11,60,000** | **Total** | **12,60,000** |

(Note: totals differ because a P&L debit ₹1,00,000 exists on the asset side — include it.) Terms of absorption:
1. Moon Ltd will issue 4 of its ₹10 shares (market value ₹15) for every 5 shares of Sun Ltd.
2. Moon Ltd will pay ₹2 per Sun share in cash.
3. Debenture-holders of Sun Ltd will be issued 13% Debentures in Moon Ltd at a 10% premium to discharge their claim.

Compute the **purchase consideration** under the "Net Payments" method, and separately verify it under the "Net Assets" method assuming assets are taken at: fixed assets ₹9,00,000, stock ₹2,20,000, debtors ₹1,70,000, bank ₹20,000 and payables at book value. Explain any difference.

**Solution:**

**WN-1 — Purchase Consideration: Net Payments method (what the *shareholders* receive):**
- Shares issued: (50,000 × 4/5) = 40,000 shares of Moon Ltd. **Valued at agreed/market value ₹15** = 40,000 × 15 = **₹6,00,000**.
- Cash: 50,000 × ₹2 = **₹1,00,000**.
- **Purchase Consideration = 6,00,000 + 1,00,000 = ₹7,00,000.**
- (Debentures issued to *debenture-holders* are **excluded** from PC — they discharge a liability, not the owners' interest.)

**WN-2 — Net Assets method (verification):**
| Assets taken over (agreed values) | ₹ |
|---|---|
| Fixed assets | 9,00,000 |
| Stock | 2,20,000 |
| Debtors | 1,70,000 |
| Bank | 20,000 |
| **Total assets** | **13,10,000** |
| Less liabilities assumed: Trade payables | (1,50,000) |
| Less: 12% Debentures (taken over/discharged) | (3,00,000) |
| **Net assets = Purchase Consideration** | **8,60,000** |

**WN-3 — Explaining the difference:** Net Payments PC = ₹7,00,000; Net Assets = ₹8,60,000. The difference of **₹1,60,000** is **not** a discrepancy in method logic but reflects that:
- Under Net Payments, PC is *defined by AS 14* as the aggregate of shares + cash paid **to the shareholders** — debentures to debenture-holders are excluded. Here that is ₹7,00,000.
- The Net Assets figure of ₹8,60,000 is computed *after* deducting the ₹3,00,000 debentures. If we treat the debenture discharge (₹3,00,000 + 10% premium = ₹3,30,000 of new debentures) consistently, the "net assets to shareholders" also equals assets ₹13,10,000 − payables ₹1,50,000 − debenture settlement ₹3,30,000 = **₹8,30,000** ... The residual gap is the **capital reserve/goodwill** that arises because PC (₹7,00,000) is *less* than net assets acquired.

**Correct reconciliation (AS 14 basis):** PC = **₹7,00,000** (Net Payments, the AS-14-preferred definition when payments are specified). Goodwill/Capital Reserve on absorption = PC − Net assets taken over (excluding debentures & payables assumed) . Net assets available to owners = 13,10,000 − 1,50,000 − 3,30,000 = 8,30,000; since PC 7,00,000 < 8,30,000, **Capital Reserve = ₹1,30,000** arises in Moon Ltd's books.

**Answer:** **Purchase Consideration = ₹7,00,000** (40,000 shares @ ₹15 + ₹1,00,000 cash); debentures to debenture-holders are excluded from PC; on absorption Moon Ltd records a **Capital Reserve of ₹1,30,000** (net assets ₹8,30,000 exceed PC ₹7,00,000).

**Why this way (the reasoning):** AS 14 defines purchase consideration as the amount payable **to the shareholders** of the transferor company — it is the price of *ownership*, not of the whole business. That is why anything issued to *debenture-holders* (or paid to settle *creditors*) is excluded: those parties are being discharged as liabilities the transferee assumes, not bought out as owners. Shares issued as consideration are counted at their **agreed/fair value** (₹15), not face value, because that is the true value handed over. The Net Assets method is only an *alternative* to be used when payments to shareholders are *not* separately specified; when they are, the Net Payments figure governs, and the difference between PC and net assets taken over is simply goodwill (PC higher) or capital reserve (PC lower) — the balancing item, not an error.

*(Full-marks tip: state explicitly that debenture-holders' securities are outside PC and that consideration shares are valued at agreed value not par; counting debentures in PC or shares at ₹10 are the classic mistakes.)*

---

### Q80. Ch: Amalgamation of Companies (AS 14) — Merger Method vs Purchase Method Entries (Marks: 10) [Problem]
**Question:** A Ltd and B Ltd amalgamate to form AB Ltd. Balance Sheets:

| Particulars | A Ltd (₹) | B Ltd (₹) |
|---|---|---|
| Equity capital (₹10 shares) | 20,00,000 | 12,00,000 |
| General reserve | 6,00,000 | 3,00,000 |
| P&L balance | 4,00,000 | 2,00,000 |
| Trade payables | 5,00,000 | 3,00,000 |
| **Total equity & liabilities** | **35,00,000** | **20,00,000** |
| Fixed assets | 24,00,000 | 13,00,000 |
| Investments | 3,00,000 | 2,00,000 |
| Current assets | 8,00,000 | 5,00,000 |
| **Total assets** | **35,00,000** | **20,00,000** |

AB Ltd issues 10 equity shares of ₹10 each for every 8 shares held in A Ltd, and 10 shares of ₹10 for every 10 shares in B Ltd. All conditions of Section 2(1B)/AS 14 for an "amalgamation in the nature of merger" are satisfied. (i) Compute the purchase consideration. (ii) Show, contrasting, how AB Ltd would record the takeover under the **Pooling of Interests (merger) method** vs the **Purchase method**, and explain the treatment of reserves and any goodwill/capital reserve.

**Solution:**

**WN-1 — Purchase consideration (shares issued):**
- A Ltd: 2,00,000 shares × 10/8 = 2,50,000 shares → 2,50,000 × ₹10 = **₹25,00,000**.
- B Ltd: 1,20,000 shares × 10/10 = 1,20,000 shares → **₹12,00,000**.
- **Total PC = ₹37,00,000** (shares of AB Ltd, at par ₹10).

**WN-2 — Merger method (Pooling of Interests):** Assets and liabilities taken at **book values**; the identity of reserves is **preserved**; difference between PC and share capital of transferor is adjusted in **reserves** (no goodwill/capital reserve arises).

| Merger method — AB Ltd | ₹ |
|---|---|
| Fixed assets (24 + 13) | 37,00,000 |
| Investments (3 + 2) | 5,00,000 |
| Current assets (8 + 5) | 13,00,000 |
| **Total assets** | **55,00,000** |
| Trade payables (5 + 3) | 8,00,000 |
| Equity capital (PC) | 37,00,000 |
| General reserve (6 + 3) | 9,00,000 |
| P&L (4 + 2) | 6,00,000 |
| **Less: adjustment** (PC 37,00,000 − transferor capital 32,00,000 = 5,00,000 excess, adjusted against **reserves**) | (5,00,000) |
| **Total** | **55,00,000** |

Reserve after adjustment = (9,00,000 + 6,00,000) − 5,00,000 = ₹10,00,000. All statutory/free reserves of A and B **carried forward**.

**WN-3 — Purchase method:** Assets/liabilities at **agreed values** (here, assume same as book for simplicity); only **statutory reserves** are carried (none here); difference between PC and net assets = goodwill/capital reserve. Net assets = 55,00,000 − 8,00,000 = ₹47,00,000. PC = ₹37,00,000. **Capital Reserve = 47,00,000 − 37,00,000 = ₹10,00,000.** Free reserves of transferors are **not** carried forward (they are subsumed in net assets).

**Journal (Purchase method, AB Ltd):**
- Business Purchase A/c Dr. 37,00,000 → To Liquidator of A & B 37,00,000.
- Assets (various) Dr. 55,00,000 → To Trade payables 8,00,000, To Business Purchase 37,00,000, To Capital Reserve 10,00,000.
- Liquidators A/c Dr. 37,00,000 → To Equity share capital 37,00,000.

**Answer:** PC = **₹37,00,000**. Under **merger method** all reserves (₹9,00,000 GR + ₹6,00,000 P&L, less ₹5,00,000 adjustment) are preserved and **no goodwill/capital reserve** arises. Under **purchase method** reserves are *not* carried (except statutory) and a **Capital Reserve of ₹10,00,000** arises.

**Why this way (the reasoning):** The two methods answer a philosophical question: is this a genuine *pooling of two continuing businesses* or a *purchase of one by another*? In a **merger (pooling)**, AS 14 treats the combination as if the two entities simply continued together — so assets, liabilities *and reserves* are carried at book value and the historical identity of each reserve survives; because nothing is "bought," no goodwill or capital reserve can arise, and any gap between share capital issued and capital taken over is squared off against reserves. In a **purchase**, one company is acquiring the other's *business*, so assets are recorded at agreed (fair) values, the acquirer's payment is compared with net assets acquired to throw up goodwill or capital reserve, and the transferor's *free* reserves vanish (only statutory reserves like Development Rebate Reserve are carried, with a matching Amalgamation Adjustment account). Applying purchase-method goodwill logic to a genuine merger — or preserving free reserves in a purchase — is the fundamental error AS 14 guards against.

*(Full-marks tip: the examiner rewards the *contrast* — book vs agreed values, reserves preserved vs subsumed, no-goodwill vs capital-reserve — and the adjustment-against-reserves in pooling. Merely computing PC without contrasting the two methods forfeits half the marks.)*

---

### Q81. Ch: Amalgamation (AS 14) — Nature of Merger: Testing the Five Conditions (Marks: 6) [Case/Application]
**Question:** X Ltd proposes to amalgamate with Y Ltd and claims it is an "amalgamation in the nature of merger" so that pooling of interests can be applied. The facts: (a) all assets and liabilities of X Ltd become those of Y Ltd; (b) shareholders holding **88%** of the face value of X Ltd's equity become shareholders of Y Ltd; (c) the consideration is discharged **80% in equity shares of Y Ltd and 20% in cash**; (d) the business of X Ltd is intended to be continued; (e) assets taken over are recorded at revalued (fair) amounts. **Examine** whether the five conditions of AS 14 for a merger are satisfied and advise the correct method.

**Answer:**

**Governing principle — the five conditions (AS 14, para 3(e)) for "amalgamation in the nature of merger", ALL of which must be met:**
1. All assets and liabilities of the transferor become those of the transferee. 
2. Shareholders holding **not less than 90%** of the face value of equity shares of the transferor (other than those already held by the transferee) become shareholders of the transferee. 
3. Consideration to such equity shareholders is discharged **wholly by issue of equity shares**, except that cash may be paid for **fractional shares**. 
4. The business of the transferor is intended to be carried on. 
5. **No adjustment is made to the book values** of assets and liabilities except to achieve uniformity of accounting policies.

**Application to the facts:**
- Condition 1 — (a) satisfied: all assets and liabilities transfer.
- Condition 2 — (b) **NOT satisfied**: only 88% (< 90%) of shareholders become shareholders of Y Ltd.
- Condition 3 — (c) **NOT satisfied**: 20% of consideration is in cash, well beyond mere fractional-share adjustment; must be *wholly* equity.
- Condition 4 — (d) satisfied: business continues.
- Condition 5 — (e) **NOT satisfied**: assets are recorded at *revalued* amounts, not book values.

**Conclusion/Advice:** Since three of the five mandatory conditions (2, 3 and 5) fail, this is **NOT** an amalgamation in the nature of merger. It is an **amalgamation in the nature of purchase**, and Y Ltd **must apply the Purchase method** — record assets/liabilities at agreed (fair) values, exclude the transferor's free reserves, and recognise goodwill or capital reserve for the difference between purchase consideration and net assets acquired. Pooling of interests cannot be used.

**Why this way (the reasoning):** AS 14's five tests exist to identify a *true uniting of interests* — where the same body of owners simply continues in a combined entity, at unchanged values. Each failed condition breaks that continuity: paying 20% cash means a fifth of the old owners are being *bought out* rather than carried forward; only 88% continuing means more than a tenth are exiting; and revaluing assets means the combined entity is *not* carrying forward historical book values but stepping them up as an acquirer would. Because the conditions are **cumulative** ("all of the following"), a single failure is fatal — you cannot cherry-pick pooling just because the business continues. Students often wrongly treat "business continues" or "most shareholders stay" as sufficient; AS 14 demands the *complete* set.

*(Full-marks tip: list all five conditions, test each against the facts, and stress the cumulative "ALL must be satisfied" rule; concluding "merger" because some conditions hold is the trap that costs the most.)*

---

### Q82. Ch: Amalgamation (AS 14) — Inter-Company Holdings and Owings, PC Adjustment (Marks: 10) [Problem]
**Question:** P Ltd takes over Q Ltd. Balance Sheet of Q Ltd:

| Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Equity capital (60,000 × ₹10) | 6,00,000 | Fixed assets | 7,50,000 |
| Reserves | 2,50,000 | Stock | 2,00,000 |
| Trade payables (incl. ₹40,000 due to P Ltd) | 1,80,000 | Debtors | 1,30,000 |
| | | Bank | 50,000 |
| **Total** | **10,30,000** | **Total** | **11,30,000** |

(A P&L debit of ₹1,00,000 exists on assets side — include.) Additional information:
1. P Ltd already holds **12,000 shares** (20%) of Q Ltd, acquired at ₹1,80,000.
2. Purchase consideration: P Ltd will issue **1 share of ₹10 (issued at ₹12)** for every share of Q Ltd held **by the outside shareholders**, plus cash of ₹1 per outside share.
3. Fixed assets are revalued at ₹8,50,000; stock at ₹1,80,000; a provision of ₹10,000 on debtors.

Compute (a) purchase consideration, (b) goodwill/capital reserve in P Ltd's books, and note the treatment of inter-company owing.

**Solution:**

**WN-1 — Outside shareholders' shares:** Total 60,000; P Ltd holds 12,000 → **outside = 48,000 shares**. PC is paid **only to outsiders** (AS 14: consideration excludes shares already held by the transferee).

**WN-2 — Purchase consideration:**
- Shares: 48,000 × 1 = 48,000 P Ltd shares issued at ₹12 = **₹5,76,000**.
- Cash: 48,000 × ₹1 = **₹48,000**.
- **PC = 5,76,000 + 48,000 = ₹6,24,000.**

**WN-3 — Net assets taken over (agreed values) — full 100% of Q Ltd's assets/liabilities are absorbed:**
| Assets (agreed) | ₹ |
|---|---|
| Fixed assets | 8,50,000 |
| Stock | 1,80,000 |
| Debtors (1,30,000 − 10,000) | 1,20,000 |
| Bank | 50,000 |
| **Total assets** | **12,00,000** |
| Less: Trade payables | (1,80,000) |
| **Net assets = ₹10,20,000** | |

**WN-4 — Purchase method with existing 20% holding (the twist):** P Ltd acquires 100% of net assets (₹10,20,000) but the *cost* to it comprises **two parts**: (i) PC paid to outsiders ₹6,24,000, and (ii) the value of its **own 20% already held**, carried at ₹1,80,000. Total cost of investment = 6,24,000 + 1,80,000 = **₹8,04,000**.
- **Capital Reserve = Net assets ₹10,20,000 − Total cost ₹8,04,000 = ₹2,16,000.**

**WN-5 — Inter-company owing (₹40,000):** After amalgamation, the ₹40,000 that Q Ltd owed P Ltd becomes an amount owed by the company to itself → **eliminated**: cancel ₹40,000 from both Trade payables (in the combined books) and P Ltd's receivable. It does **not** affect PC or net assets of Q taken over (it is a book of P Ltd adjustment on consolidation of the two ledgers).

**Answer:** (a) **Purchase Consideration = ₹6,24,000** (paid only to the 48,000 outside shares); (b) net assets ₹10,20,000 less total cost (PC ₹6,24,000 + own holding ₹1,80,000 = ₹8,04,000) gives a **Capital Reserve of ₹2,16,000**; (c) the ₹40,000 inter-company owing is eliminated against P Ltd's receivable in the combined books.

**Why this way (the reasoning):** Two AS-14 subtleties combine. First, purchase consideration is what the transferee pays to become owner — but it *already owned 20%*, so it only needs to buy out the *other 80%*; paying PC on all 60,000 shares would mean paying yourself, which is nonsensical. Second, when computing goodwill/capital reserve, P Ltd still ends up owning *all* the net assets, so you compare the *full* net assets acquired against P Ltd's *total* outlay — the cash/shares given to outsiders **plus** the book cost of the stake it already held (that stake is effectively "used up" in acquiring the whole). Ignoring the pre-existing holding on either the PC side or the cost side distorts the reserve. The inter-company debt is a pure elimination: once both companies are one, a debt from one to the other cannot survive — it would overstate both assets and liabilities of the merged entity.

*(Full-marks tip: PC only for outside shareholders, and the existing investment cost must be added to PC when computing goodwill/capital reserve; forgetting the own-holding on the cost side is the headline error, and the inter-company owing must be eliminated, not counted in net assets.)*

---

### Q83. Ch: Amalgamation (AS 14) — Discharge of Debentures & Preference at Premium (Marks: 6) [Problem]
**Question:** In the absorption of Rex Ltd by Tex Ltd, the following claims of Rex Ltd are to be discharged by Tex Ltd:

| Claim in Rex Ltd | Book value ₹ | Discharge terms |
|---|---|---|
| 10% Preference shares | 4,00,000 | Issue 11% Preference shares of Tex at a 10% premium |
| 12% Debentures | 5,00,000 | Issue 13% Debentures of Tex at par, but holders accept only 90% of claim |
| Equity capital (80,000 × ₹10) | 8,00,000 | 3 equity shares of Tex (₹10, issued at ₹14) for every 4 equity shares of Rex |

Compute (a) the amount of Tex Ltd securities to be issued for each class, and (b) the purchase consideration under AS 14. Explain which items enter PC.

**Solution:**

**WN-1 — Preference shareholders:** Claim ₹4,00,000 discharged by 11% Pref of Tex at 10% premium → face value of Tex pref to issue = 4,00,000 ÷ 1.10 = **₹3,63,636** face (issued at premium to total ₹4,00,000 value). Preference shareholders **are members**, so this is **part of PC**: **₹4,00,000**.

**WN-2 — Debenture-holders:** Claim ₹5,00,000; holders accept 90% = ₹4,50,000, discharged by 13% Debentures of Tex at par = **₹4,50,000 debentures issued**. Debenture-holders are **creditors, NOT members** → **excluded from PC**. (The ₹50,000 they forgo is a gain to Tex, adjusted in capital reserve/goodwill computation, not PC.)

**WN-3 — Equity shareholders:** 80,000 × 3/4 = 60,000 Tex shares of ₹10 issued at ₹14 → value = 60,000 × 14 = **₹8,40,000**. Equity holders are members → **part of PC**.

**WN-4 — Purchase Consideration (AS 14 = amounts payable to shareholders/members):**
| Component | ₹ |
|---|---|
| Equity shares issued (60,000 × ₹14) | 8,40,000 |
| Preference shares issued (value) | 4,00,000 |
| **Purchase Consideration** | **12,40,000** |
Debentures (₹4,50,000) are **excluded**.

**Answer:** (a) Tex issues: **₹3,63,636 face** of 11% Preference (₹4,00,000 value), **₹4,50,000** of 13% Debentures, and **60,000 equity shares** (value ₹8,40,000). (b) **Purchase Consideration = ₹12,40,000** — comprising equity + preference to members; **debentures are excluded** from PC.

**Why this way (the reasoning):** AS 14 anchors purchase consideration to payments made to **shareholders (members)** — both equity *and* preference, because preference shareholders are owners of the company, not lenders. Debenture-holders, by contrast, are **creditors**: the transferee takes over/settles their claim as a liability, so whatever securities they receive sit *outside* PC. The premium at which Tex issues its shares matters because consideration is measured by the *value* handed to members, not face value — 60,000 shares "worth" ₹14 transfer ₹8,40,000 of value. And when debenture-holders accept only 90%, the 10% they waive is a windfall to the transferee that improves the capital reserve (or shrinks goodwill) but never touches PC. The frequent error is dumping the debenture securities into PC or valuing consideration shares at par ₹10 instead of the ₹14 issue value.

*(Full-marks tip: preference shares IN, debentures OUT of PC; value consideration shares at issue price (incl. premium). Including debentures or using par value are the two standard mark-losers.)*

---

### Q84. Ch: Amalgamation (AS 14) — Statutory Reserve & Amalgamation Adjustment Account (Marks: 5) [Case/Application]
**Question:** During the amalgamation of Alpha Ltd into Beta Ltd (an amalgamation **in the nature of purchase**), Alpha Ltd's balance sheet carries an **Investment Allowance Reserve (a statutory reserve) of ₹5,00,000** which must be maintained for two more years under tax law, and a **General Reserve of ₹8,00,000**. The accountant of Beta Ltd proposes to carry forward *both* reserves into Beta Ltd's books exactly as they stood. **Comment on the validity** and show the correct treatment, including any special account.

**Answer:**

**Governing principle (AS 14):** In an amalgamation in the **nature of purchase**, the transferee does **not** carry forward the **free reserves** (General Reserve, P&L, etc.) of the transferor — these are *subsumed* in the net assets acquired and effectively disappear (their value is captured in goodwill/capital reserve). However, where a **statutory reserve** (e.g., Investment Allowance Reserve, Development Rebate Reserve) of the transferor must legally be **maintained** for a period, it *is* carried forward — but to preserve the accounting identity, it is recorded by crediting the statutory reserve and **debiting a special account called the "Amalgamation Adjustment Reserve" (Amalgamation Adjustment Account)**, shown on the **assets side** (or netted in reserves per Schedule III), until the statutory requirement lapses, whereupon both are reversed.

**Application to the facts:**
- **General Reserve ₹8,00,000** — the accountant is **wrong** to carry it forward. In a purchase amalgamation, free reserves of Alpha Ltd are **not** brought into Beta Ltd's books; their worth is already reflected in the net assets taken over and thus in the goodwill/capital reserve computed. Carrying it separately would double-count.
- **Investment Allowance Reserve ₹5,00,000** — this **must** be carried forward because tax law requires its continuance for two more years, **but** by passing: *Amalgamation Adjustment Reserve A/c Dr. ₹5,00,000 / To Investment Allowance Reserve ₹5,00,000.* The Amalgamation Adjustment Reserve appears on the assets side (a debit balance) as it does not represent a real asset — it is a balancing entry. After two years, when the statutory need ends: reverse it — *Investment Allowance Reserve Dr. / To Amalgamation Adjustment Reserve*, and the reserve is then freed to General Reserve.

**Conclusion/Advice:** The proposal is **partly invalid**. The **General Reserve of ₹8,00,000 cannot be carried forward** (purchase method subsumes free reserves). The **Investment Allowance Reserve of ₹5,00,000 must be carried forward** but only *via* the Amalgamation Adjustment Reserve mechanism, to be reversed when the statutory period expires.

**Why this way (the reasoning):** The purchase method treats the transaction as Beta *buying Alpha's business* — so Alpha's own accumulated free reserves are not Beta's to inherit; they are paid for as part of the net assets and vanish into goodwill/capital reserve. But tax statutes sometimes *compel* a reserve to remain on the books (to prevent the tax benefit being clawed back). AS 14 resolves the tension with the Amalgamation Adjustment Reserve: it lets the statutory reserve appear (satisfying the law) while a matching debit balance signals that it is **not backed by free reserves or real assets** — a purely legal placeholder — so users are not misled into thinking distributable reserves exist. Reversing both when the obligation lapses restores a clean picture. Carrying the free General Reserve forward would overstate Beta's reserves and double-count value already inside the net assets acquired.

*(Full-marks tip: distinguish free reserves (not carried in purchase method) from statutory reserves (carried via Amalgamation Adjustment Reserve on the assets side, reversed on expiry); naming the special account and its later reversal is what secures full marks.)*

### Q85. Ch: Branch Accounts — Stock & Debtors System (Invoice Price, Shortage) (Marks: 10) [Problem]
**Question:** Delhi Head Office invoices goods to its Mumbai branch at **cost plus 25%**. The branch remits all cash and cannot purchase independently. From the following, prepare the **Branch Stock Account, Branch Adjustment Account and Branch Profit & Loss Account** for the year ended 31.03.2026, and determine the cost of the stock shortage.

| Particulars | ₹ (at Invoice Price unless stated) |
|---|---|
| Opening stock at branch | 1,20,000 |
| Goods sent to branch | 6,00,000 |
| Goods returned by branch to H.O. | 24,000 |
| Cash sales | 2,40,000 |
| Credit sales | 2,40,000 |
| Closing stock at branch (physically counted) | 2,04,000 |
| Branch expenses (salaries, rent, etc.) | 30,000 |

**Solution:**

**WN-1 — Loading rate.** Goods are invoiced at cost + 25%. Loading = 25/125 = **20% of invoice price**.

**WN-2 — Branch Stock A/c (all at invoice price); shortage = balancing figure.**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Opening Stock | 1,20,000 | By Cash Sales | 2,40,000 |
| To Goods sent to Branch | 6,00,000 | By Credit Sales | 2,40,000 |
| | | By Goods returned to H.O. | 24,000 |
| | | By **Shortage (bal. fig.)** | **12,000** |
| | | By Closing Stock c/d | 2,04,000 |
| **Total** | **7,20,000** | **Total** | **7,20,000** |

**WN-3 — Loading on each item (20% of invoice value):** Opening 24,000; Goods sent 1,20,000; Returns 4,800; Shortage 2,400; Closing 40,800.

**Branch Adjustment Account** (loading only)

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Loading on Returns to H.O. | 4,800 | By Loading on Opening Stock | 24,000 |
| To Loading on Shortage | 2,400 | By Loading on Goods sent | 1,20,000 |
| To Loading on Closing Stock (reserve) | 40,800 | | |
| To **Gross Profit c/d** | **96,000** | | |
| **Total** | **1,44,000** | **Total** | **1,44,000** |

**Branch Profit & Loss Account**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Cost of Shortage (12,000 − 2,400 loading) | 9,600 | By Gross Profit b/d | 96,000 |
| To Branch Expenses | 30,000 | | |
| To **Net Profit** | **56,400** | | |
| **Total** | **96,000** | **Total** | **96,000** |

**Answer:** Stock shortage at invoice ₹12,000 (cost ₹9,600); Gross Profit ₹96,000; **Branch Net Profit ₹56,400.**

**Why this way (the reasoning):** Under the stock-and-debtors system the Branch Stock A/c is maintained **at invoice price** because that is the value at which goods physically move; keeping it at invoice makes the *debit total the goods available* and the *credit total the goods accounted for*, so any un-reconciled figure is a genuine physical shortage — not an arithmetic artefact. But invoice price contains an unreal profit (the 20% loading) that the H.O. has not actually earned until the branch sells to outsiders. The **Branch Adjustment A/c strips out that loading** on every stream so that only the *realised* margin on goods actually sold survives as Gross Profit; the loading on unsold closing stock is retained as a *stock reserve* (never recognise profit on goods still in hand — the prudence concept). The tempting wrong move is to charge the full ₹12,000 shortage to P&L; that overstates the loss, because ₹2,400 of it was never real profit/cost — the true economic loss is the **cost** ₹9,600, so the loading portion is written back through the Adjustment A/c. That is why shortage is split between the two accounts.

*(Full-marks tip: examiners reward showing the shortage as a *balancing figure* in the Stock A/c and correctly splitting it (cost to P&L, loading to Adjustment A/c). Common deductions: applying 25% instead of 20% on invoice values, and forgetting the loading reserve on closing stock.)*

---

### Q86. Ch: Branch Accounts — Foreign Branch (AS 11, Non-Integral) (Marks: 10) [Problem]
**Question:** X Ltd (India) runs a **non-integral foreign operation** whose trial balance (in $) for the year ended 31.03.2026 is below. Translate it and determine the **Foreign Currency Translation Reserve (FCTR)**. Rates: opening 1$ = ₹60; average = ₹63; closing = ₹66. The Head Office account appears in H.O. books at **₹17,40,000**. Closing stock = $10,000.

| Dr ($) | Amount | Cr ($) | Amount |
|---|---|---|---|
| Plant & Machinery | 24,000 | Sales | 62,000 |
| Opening Stock | 8,000 | Creditors | 12,000 |
| Purchases | 40,000 | Head Office A/c | 30,000 |
| Wages & Expenses | 11,000 | | |
| Debtors | 16,000 | | |
| Bank | 5,000 | | |
| **Total** | **1,04,000** | **Total** | **1,04,000** |

**Solution:**

**WN-1 — Translation rules (non-integral, AS 11).** All **assets & liabilities at CLOSING rate (₹66)**; **income & expenses at rate on date of transaction ≈ AVERAGE (₹63)**; opening stock at the rate when it arose (opening ₹60); H.O. account at the actual figure in H.O. books; the net exchange difference goes to **FCTR (not P&L)**.

**WN-2 — Translated Profit & Loss (Trading result):**

| Particulars | $ | Rate | ₹ |
|---|---|---|---|
| Sales | 62,000 | 63 | 39,06,000 |
| Add: Closing Stock | 10,000 | 66 | 6,60,000 |
| **Total credits** | | | **45,66,000** |
| Less: Opening Stock | 8,000 | 60 | 4,80,000 |
| Less: Purchases | 40,000 | 63 | 25,20,000 |
| Less: Wages & Expenses | 11,000 | 63 | 6,93,000 |
| **Total debits** | | | **36,93,000** |
| **Net Profit** | | | **8,73,000** |

**Translated Balance Sheet (in ₹)**

| Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Head Office A/c | 17,40,000 | Plant & Machinery (24,000×66) | 15,84,000 |
| Creditors (12,000×66) | 7,92,000 | Debtors (16,000×66) | 10,56,000 |
| Net Profit | 8,73,000 | Bank (5,000×66) | 3,30,000 |
| **FCTR (bal. fig.)** | **2,25,000** | Closing Stock (10,000×66) | 6,60,000 |
| **Total** | **36,30,000** | **Total** | **36,30,000** |

**Answer:** **FCTR = ₹2,25,000 (credit — an exchange gain)**; translated net profit ₹8,73,000; balance sheet total ₹36,30,000.

**Why this way (the reasoning):** A **non-integral** foreign operation is financially and operationally autonomous — it accumulates cash and settles locally, so the reporting enterprise's *net investment* is exposed to currency movement only when profits are eventually repatriated. Because the exposure is on the **whole net investment, not on individual monetary items**, AS 11 says do **not** route the difference through P&L (that would distort operating results with a gain that is neither realised nor operational). Instead every asset and liability is carried at the closing rate — this keeps them consistent with each other so a *single* net difference emerges — and that difference is parked in FCTR in equity until disposal of the operation, when it is recycled to P&L. The average rate is used for income/expenses because they accrue evenly over the year. The classic trap is treating the branch as **integral** (which would restate only monetary items at closing rate, non-monetary at historical, and hit P&L). Here the branch is autonomous, so the closing-rate method and FCTR are mandatory. FCTR is a *balancing figure* precisely because it is the residual exchange effect of translating a self-balancing set of accounts at mixed rates.

*(Full-marks tip: state the classification test first, then translate. Marks are lost for putting the difference in P&L, restating non-monetary items at historical rate under the non-integral method, or translating the H.O. account at closing rate instead of taking the reciprocal H.O.-books figure.)*

---

### Q87. Ch: Branch Accounts — Integral vs Non-Integral Classification (AS 11) (Marks: 5) [Case/Application]
**Question:** P Ltd (India) has a branch in Country Z. The branch **buys all its raw material from P Ltd's Indian factory on inter-company credit**, sells only to customers introduced by P Ltd's marketing team, **remits its entire cash collection to India weekly**, and its price list and working capital are entirely funded and controlled by the Indian H.O. The branch accountant has translated the accounts using the **closing-rate (non-integral) method** and created an FCTR. **Examine the validity** of this treatment under AS 11.

**Answer:**
**Governing principle (AS 11):** The translation method depends on whether the foreign operation is **integral** or **non-integral**. AS 11 lists indicators of a *non-integral* operation: it carries on business with significant autonomy, accumulates cash and generates finance locally, transacts primarily in the local currency, and its cash flows are insulated from the reporting enterprise. Conversely, an **integral** operation is a mere extension of the parent — its cash flows *directly and immediately* affect the parent's cash flows.

**Application to facts:** Every indicator here points to **integral**, not non-integral: (i) the branch sources all raw material from the H.O. — its costs are H.O.-driven, not local; (ii) it sells only to H.O.-introduced customers, so its revenue depends on the parent; (iii) it **remits its entire collection weekly** to India — its cash flows directly and immediately affect P Ltd's cash flows, the hallmark of an integral unit; (iv) its pricing and working capital are H.O.-controlled — it has **no operational autonomy**. There is not a single factor supporting autonomy.

**Conclusion:** The branch is an **integral foreign operation**. The correct method is the *temporal method*: monetary items (debtors, creditors, cash) at closing rate, non-monetary items carried at cost (fixed assets, stock) at historical rate, income/expenses at transaction/average rate, and — crucially — **exchange differences to the Profit & Loss Account, NOT to an FCTR.** The accountant's closing-rate/FCTR treatment is **invalid**; it must be reworked on the temporal basis with the difference recognised in P&L.

**Why this way (the reasoning):** The distinction is not a labelling formality — it decides *where an unrealised currency difference lands*. For an integral branch the parent bears the currency risk on each transaction immediately (because cash flows through to it at once), so the difference is a real, current-period gain/loss and belongs in P&L. For a non-integral branch the risk is only on the long-term net investment, so it is deferred in equity. Classifying by the substance of the cash-flow relationship — here, weekly full remittance and total H.O. dependence — is what drives the answer; the tempting error is to look only at "it's in a foreign country, so translate at closing rate," ignoring that geography does not determine autonomy.

*(Full-marks tip: examiners want the *indicators* named and each mapped to a fact, then the P&L-vs-FCTR consequence stated. A bald conclusion without applying the autonomy indicators to the specific facts caps you at half marks.)*

---

### Q88. Ch: Departmental Accounts — Allocation of Common Expenses (Marks: 8) [Problem]
**Question:** A firm has two departments, A and B. Prepare a **Departmental Profit & Loss Account** for the year ended 31.03.2026, allocating each common expense on the most appropriate basis and justifying it.

| Particulars | Dept A (₹) | Dept B (₹) |
|---|---|---|
| Opening Stock | 60,000 | 40,000 |
| Purchases | 3,00,000 | 2,00,000 |
| Sales | 5,00,000 | 3,00,000 |
| Closing Stock | 80,000 | 50,000 |
| No. of employees | 30 | 20 |
| Floor area (sq. ft.) | 3,000 | 1,000 |

Common expenses: Rent & Rates ₹80,000; Staff Welfare ₹50,000; Selling Expenses ₹64,000 (allocate on turnover); General Manager's Salary ₹36,000 (allocate on sales).

**Solution:**

**WN-1 — Allocation bases:** Rent & Rates → **floor area 3,000:1,000 = 3:1**. Staff Welfare → **number of employees 30:20 = 3:2**. Selling Expenses & GM Salary → **turnover 5,00,000:3,00,000 = 5:3**.

| Expense | Total ₹ | Basis | Dept A ₹ | Dept B ₹ |
|---|---|---|---|---|
| Rent & Rates | 80,000 | Area 3:1 | 60,000 | 20,000 |
| Staff Welfare | 50,000 | Employees 3:2 | 30,000 | 20,000 |
| Selling Expenses | 64,000 | Turnover 5:3 | 40,000 | 24,000 |
| GM Salary | 36,000 | Turnover 5:3 | 22,500 | 13,500 |

**Departmental Profit & Loss Account for the year ended 31.03.2026**

| Particulars | Dept A ₹ | Dept B ₹ |
|---|---|---|
| Sales | 5,00,000 | 3,00,000 |
| Less: Cost of Goods Sold (Op + Pur − Cl) | 2,80,000 | 1,90,000 |
| **Gross Profit** | **2,20,000** | **1,10,000** |
| Less: Rent & Rates | 60,000 | 20,000 |
| Less: Staff Welfare | 30,000 | 20,000 |
| Less: Selling Expenses | 40,000 | 24,000 |
| Less: GM Salary | 22,500 | 13,500 |
| **Net Profit** | **67,500** | **32,500** |

COGS: A = 60,000+3,00,000−80,000 = 2,80,000; B = 40,000+2,00,000−50,000 = 1,90,000.

**Answer:** Net Profit — Dept A ₹67,500; Dept B ₹32,500; **Total ₹1,00,000.**

**Why this way (the reasoning):** Departmental accounting exists to reveal *which department actually earns*, so a common cost must be shared on the basis of the **factor that causes it** (cause-and-effect / benefit-received principle). Rent is a function of *space occupied*, so floor area is the driver — allocating rent on turnover would wrongly penalise the high-selling department for space it does not consume. Staff welfare responds to *headcount*, so employees is the driver. Selling expenses and the GM's salary vary with *sales effort/volume*, so turnover is the fair driver. Choosing the wrong base (e.g., splitting everything on turnover for convenience) mis-states each department's true profitability and can lead management to close a department that is actually profitable — defeating the entire purpose of departmentalisation. The discipline is: **identify the cost driver, then allocate.**

*(Full-marks tip: state the basis *and the reason* beside each expense. Examiners deduct marks when a single basis (usually turnover) is lazily applied to every expense, or when the ratio (3:1, 3:2, 5:3) is not shown.)*

---

### Q89. Ch: Departmental Accounts — Inter-Departmental Transfer & Unrealised Profit (Marks: 10) [Problem]
**Question:** M/s Rao & Co. has two departments — **Cloth (X)** and **Readymade Garments (Y)**. Department X transfers cloth to Department Y at its **usual selling price (cost + 25%)**. From the data below, prepare the **Departmental Trading & Profit and Loss Account** and compute the **Stock Reserve** for unrealised profit.

| Particulars | Dept X (Cloth) ₹ | Dept Y (Garments) ₹ |
|---|---|---|
| Opening Stock | 1,00,000 | 60,000 |
| Purchases (external) | 8,00,000 | 1,50,000 |
| Transfer of cloth to Dept Y (at transfer price) | 2,00,000 | — |
| Sales (external) | 9,50,000 | 4,50,000 |
| Closing Stock (own goods only) | 1,20,000 | — |
| Closing Stock of Dept Y — cloth received from X (at transfer price) | — | 50,000 |
| Closing Stock of Dept Y — own manufactured goods | — | 40,000 |
| Manufacturing wages (Dept Y) | — | 60,000 |

Opening stock of Dept Y includes cloth from X (at transfer price) ₹25,000. Assume the loading rate on opening-stock cloth is also 25% on cost.

**Solution:**

**WN-1 — Loading rate.** Transfer at cost + 25% ⇒ profit element = 25/125 = **20% of transfer price**.

**WN-2 — Unrealised profit in Dept Y's stock of transferred cloth.**
- Opening (Y): 20% × 25,000 = **₹5,000** (Opening Stock Reserve — created last year, now written back).
- Closing (Y): 20% × 50,000 = **₹10,000** (Closing Stock Reserve — to be created).

**Departmental Trading & Profit and Loss Account for the year ended 31.03.2026**

| Particulars | Dept X ₹ | Dept Y ₹ | Total ₹ |
|---|---|---|---|
| Sales (external) | 9,50,000 | 4,50,000 | 14,00,000 |
| Transfer to Dept Y | 2,00,000 | — | 2,00,000 |
| **Total (a)** | **11,50,000** | **4,50,000** | |
| Opening Stock | 1,00,000 | 60,000 | |
| Purchases | 8,00,000 | 1,50,000 | |
| Transfer from Dept X | — | 2,00,000 | |
| Manufacturing Wages | — | 60,000 | |
| Less: Closing Stock | (1,20,000) | (90,000) | |
| **Cost of Sales (b)** | **7,80,000** | **3,80,000** | |
| **Gross Profit (a − b)** | **3,70,000** | **70,000** | **4,40,000** |

Dept Y closing stock = 50,000 (cloth) + 40,000 (own) = 90,000.

**Combined Profit & Loss (Stock Reserve adjustment)**

| Particulars | ₹ |
|---|---|
| Total Gross Profit (X + Y) | 4,40,000 |
| Add: Opening Stock Reserve written back | 5,000 |
| Less: Closing Stock Reserve (unrealised profit) | (10,000) |
| **Net Profit after eliminating unrealised profit** | **4,35,000** |

**Answer:** Combined Gross Profit ₹4,40,000; net unrealised-profit adjustment = −₹5,000; **Net Profit ₹4,35,000.** Closing Stock Reserve to be carried in the balance sheet = **₹10,000** (deducted from inventory).

**Why this way (the reasoning):** When one department sells to another at a **mark-up**, the selling department books a "profit" — but from the *firm's* point of view no profit is earned until the goods leave the firm to an outside customer. So long as the transferred cloth is still lying in Dept Y's closing stock, the 20% mark-up sitting inside that inventory is **unrealised** — it is profit the firm has charged to itself. Recognising it would overstate both profit and asset value, breaching the realisation and prudence concepts. Hence we **create a Stock Reserve** equal to the loading in the *closing* transferred stock (₹10,000) and deduct it from profit and from inventory. Symmetrically, the loading in *opening* transferred stock (₹5,000) was reserved last year against goods that have now been sold onward, so it is **written back** (that profit is now realised). The common error is to eliminate profit on the *whole* closing stock of Dept Y or to net the two reserves incorrectly — only the loading portion of the *inter-departmentally transferred* goods is unrealised; Dept Y's own manufactured stock (₹40,000) carries no internal mark-up and needs no reserve.

*(Full-marks tip: apply 20% (not 25%) to the *transfer-price* value of transferred stock only, and show BOTH the write-back of opening reserve and creation of closing reserve. Biggest deductions: reserving on Dept Y's total closing stock, and using 25%.)*

---

### Q90. Ch: Departmental Accounts — Justifying the Stock Reserve (Marks: 5) [Case/Application]
**Question:** The accountant of a firm argues: "Both departments are part of the *same firm*; when Dept A transfers goods to Dept B at a profit and B still holds them, no cash has left the firm, so there is nothing to adjust — I will show the full transfer profit in the year's accounts." **Comment on the validity** of this view and explain what adjustment (if any) is required, with the accounting principle involved.

**Answer:**
**Governing principle:** Under the **realisation concept**, profit is recognised only when goods are sold to a party *outside the entity* — an inter-departmental transfer is an *internal* movement, not a sale. Under the **prudence concept**, unrealised gains must not be recognised, and inventory must be valued at **cost (or NRV), not at an internally inflated transfer price**.

**Application:** The accountant is partly right and critically wrong. He is right that inter-departmental transfers are *not* sales for the firm — which is exactly why the mark-up on transferred goods **still lying in the buying department's closing stock is unrealised profit**. That mark-up has been credited to the selling department but the firm has not earned it, because the goods have not yet reached an external customer. Recognising it would (a) overstate the year's profit and (b) overstate closing inventory (an asset) above its true cost to the firm — inflating the balance sheet. The correct adjustment is to compute the loading contained in the closing transferred stock and create a **Stock Reserve**, deducting it from combined profit and from the inventory figure. When those goods are sold next year, the reserve is written back and the profit becomes real.

**Conclusion:** The view is **invalid** to the extent it proposes to retain the full transfer profit. A stock reserve for the unrealised profit in unsold transferred stock is **mandatory**; only the mark-up on goods *sold onward* to outsiders is genuine profit for the year.

**Why this way (the reasoning):** The core insight is that a firm cannot make a profit by trading with itself. Inter-departmental margins are a *management tool* (to measure each department's performance), not a source of firm-level income. The stock reserve is the mechanism that reconciles these two perspectives — it lets each department show its notional margin for internal evaluation while ensuring the *consolidated* accounts recognise profit only on external sales. The seductive error is to treat "no cash movement" as meaning "no adjustment": cash timing is irrelevant to accrual profit; what matters is whether the earning process is *complete* by sale to a third party.

*(Full-marks tip: name both realisation and prudence, tie the unrealised profit specifically to *unsold* transferred stock, and mention the write-back next year. Merely saying "create a reserve" without the principle earns partial credit.)*

---

### Q91. Ch: Consolidated Financial Statements — Consolidated Balance Sheet (Marks: 10) [Problem]
**Question:** H Ltd acquired **40,000 equity shares (of ₹10 each) in S Ltd** — being **80%** — on **1.4.2025** for ₹6,00,000. On that date S Ltd's Reserves were ₹1,00,000 and P&L (credit) ₹50,000. Prepare the **Consolidated Balance Sheet as at 31.3.2026.**

| Balance Sheet (31.3.2026) | H Ltd ₹ | S Ltd ₹ |
|---|---|---|
| Equity Share Capital (₹10) | 10,00,000 | 5,00,000 |
| Reserves | 3,00,000 | 1,00,000 |
| Profit & Loss A/c | 2,00,000 | 1,50,000 |
| Trade Payables | 1,50,000 | 1,00,000 |
| **Total** | **16,50,000** | **8,50,000** |
| Investment in S Ltd | 6,00,000 | — |
| Fixed Assets | 6,00,000 | 4,50,000 |
| Inventory | 2,50,000 | 2,00,000 |
| Trade Receivables | 1,50,000 | 1,50,000 |
| Bank | 50,000 | 50,000 |
| **Total** | **16,50,000** | **8,50,000** |

Additional: (i) S Ltd sold goods to H Ltd at cost + 25%; H Ltd's closing inventory includes ₹60,000 of such goods. (ii) H Ltd's payables include ₹40,000 owed to S Ltd (in S's receivables).

**Solution:**

**WN-1 — Analysis of S Ltd's reserves/profits.** Reserves unchanged (1,00,000) ⇒ entirely **pre-acquisition (capital)**. P&L: at acquisition 50,000 (capital); at 31.3.26 1,50,000 ⇒ **post-acquisition (revenue) profit = 1,00,000**.

**WN-2 — Unrealised profit in stock.** Goods from S (upstream) in H's stock ₹60,000 at cost + 25% ⇒ profit = 25/125 × 60,000 = **₹12,000**. Deduct from consolidated inventory and from S's post-acquisition profit (seller is the subsidiary).
Revised S post-acquisition profit = 1,00,000 − 12,000 = **88,000**.

**WN-3 — Minority Interest (20% of S's net assets at 31.3.26, after stock reserve).**
Net assets = 5,00,000 + 1,00,000 + (1,50,000 − 12,000) = 7,38,000. MI = 20% × 7,38,000 = **₹1,47,600**.

**WN-4 — Cost of Control / Goodwill.**
| | ₹ |
|---|---|
| Cost of investment | 6,00,000 |
| Less: Parent's share of capital profits = 80% × (5,00,000 + 1,00,000 + 50,000) | 5,20,000 |
| **Goodwill** | **80,000** |

**WN-5 — Consolidated P&L.** H's own 2,00,000 + 80% of S's revised post-acq profit (80% × 88,000 = 70,400) = **₹2,70,400**.

**Consolidated Balance Sheet of H Ltd and its subsidiary as at 31.3.2026**

| Equity & Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Equity Share Capital | 10,00,000 | Goodwill (WN-4) | 80,000 |
| Reserves (H only) | 3,00,000 | Fixed Assets (6,00,000+4,50,000) | 10,50,000 |
| Consolidated P&L (WN-5) | 2,70,400 | Inventory (2,50,000+2,00,000−12,000) | 4,38,000 |
| Minority Interest (WN-3) | 1,47,600 | Trade Receivables (1,50,000+1,50,000−40,000) | 2,60,000 |
| Trade Payables (1,50,000+1,00,000−40,000) | 2,10,000 | Bank (50,000+50,000) | 1,00,000 |
| **Total** | **19,28,000** | **Total** | **19,28,000** |

**Answer:** **Goodwill ₹80,000; Minority Interest ₹1,47,600; Consolidated P&L ₹2,70,400;** balance sheet total ₹19,28,000.

**Why this way (the reasoning):** Consolidation rests on the **acquisition (parent) model**: goodwill is the *premium the parent paid over its share of the fair net assets it bought*, so only **pre-acquisition** equity (capital profits) is set against the cost of investment — post-acquisition profit is genuine earnings of the group and flows to consolidated P&L. Mixing the two is the single biggest error: crediting pre-acquisition profit to consolidated reserves would overstate distributable profit and understate goodwill. **Minority interest** is the outsiders' slice of the subsidiary's *total* net assets at the reporting date (not at acquisition), because minorities own their proportion of everything the subsidiary now holds. The **inter-company stock profit** is unrealised at group level (the group cannot profit by selling to itself), so it is stripped from both the asset and — because the *subsidiary* was the seller — from the subsidiary's post-acquisition profit, which correctly makes the minority bear its 20% share of the elimination too. Finally, **mutual owings** (₹40,000) are contra-eliminated because a group cannot owe money to itself; leaving them in would double-count both an asset and a liability.

*(Full-marks tip: examiners reward the four-schedule discipline — capital-profit analysis, cost of control, MI, consolidated P&L — plus correct elimination of BOTH the stock profit and the mutual debt. Deductions: taking MI at acquisition-date net assets, not reducing S's post-acq profit for upstream stock, and forgetting the mutual-owing contra.)*

---

### Q92. Ch: Consolidated Financial Statements — Mid-Year Acquisition, Pre/Post Split (Marks: 8) [Problem]
**Question:** H Ltd acquired **30,000 of the 40,000 equity shares (₹10 each) of S Ltd — 75%** — on **1.10.2025** for ₹4,50,000. S Ltd's balances on **1.4.2025** were: Reserves ₹60,000; P&L (credit) ₹40,000. Profit for the year ended 31.3.2026 was ₹1,20,000, **earned evenly** through the year; reserves were unchanged. Compute **Goodwill/Capital Reserve, Minority Interest, and the profit taken to Consolidated P&L.**

**Solution:**

**WN-1 — Time-apportion the current-year profit.** Acquisition on 1.10.2025 splits the year 6 months : 6 months. Since profit ₹1,20,000 accrues evenly ⇒ **Pre-acquisition (1.4–30.9) = 60,000; Post-acquisition (1.10–31.3) = 60,000.**

**WN-2 — Net assets / capital profits at acquisition (1.10.2025).**
| | ₹ |
|---|---|
| Share Capital | 4,00,000 |
| Reserves (all pre) | 60,000 |
| P&L: opening 40,000 + pre-acq portion 60,000 | 1,00,000 |
| **Net assets at acquisition** | **5,60,000** |

**WN-3 — Cost of Control.**
| | ₹ |
|---|---|
| Cost of investment | 4,50,000 |
| Less: 75% × 5,60,000 | 4,20,000 |
| **Goodwill** | **30,000** |

**WN-4 — Minority Interest (25% of net assets at 31.3.26).**
Net assets at 31.3.26 = 4,00,000 + 60,000 + (40,000 + 1,20,000) = 6,20,000. MI = 25% × 6,20,000 = **₹1,55,000**.

**WN-5 — Post-acquisition profit to Consolidated P&L.** Parent's share = 75% × 60,000 (post portion) = **₹45,000**.

**Answer:** **Goodwill ₹30,000; Minority Interest ₹1,55,000; ₹45,000 credited to Consolidated P&L.**

**Why this way (the reasoning):** When control is acquired **part-way through the year**, the subsidiary's *current-year* profit straddles the acquisition date: the portion earned *before* control is **capital profit** (it was already inside the net assets the parent bought, so it belongs to cost-of-control), while the portion earned *after* is the group's genuine post-acquisition income. Because the profit accrues evenly, **time apportionment** is the fair splitter (if it accrued unevenly — e.g., a seasonal spike — you would use actual dates). The error students make is treating the *whole* ₹1,20,000 as post-acquisition, which understates goodwill and overstates consolidated profit — effectively letting the parent claim earnings that predate its ownership. Note MI is still computed on the *full* year-end net assets (25% of everything the subsidiary owns on 31.3.26) because the minority owned its stake throughout; only the *parent's* consolidation splits pre/post.

*(Full-marks tip: show the 6:6 apportionment explicitly and add the pre-portion to capital profits, not to consolidated P&L. Marks are lost for splitting MI into pre/post — MI takes year-end net assets in full.)*

---

### Q93. Ch: Consolidated Financial Statements — Dividend out of Pre-Acquisition Profits (Marks: 6) [Case/Application]
**Question:** H Ltd acquired **80% of S Ltd (40,000 of 50,000 shares, ₹10 each)** on **1.4.2025** for ₹6,50,000. In August 2025, S Ltd paid a dividend of **15% for the year 2024-25** (i.e., ₹75,000 on capital of ₹5,00,000). H Ltd credited its share of this dividend to its **Profit & Loss Account**. **Examine the validity** of H Ltd's treatment and show the corrected effect on goodwill. S Ltd's net assets on 1.4.2025 (after providing for the 2024-25 dividend) were: Capital ₹5,00,000 + Reserves ₹75,000 = ₹5,75,000.

**Answer:**
**Governing principle:** A dividend received by a holding company out of the subsidiary's **pre-acquisition profits** is, in substance, a **return of part of the purchase price (a capital receipt)** — not income earned by the holding company. It must therefore be **credited to the Investment (Cost of Control) Account**, reducing the cost of the investment, and **not** taken to the Consolidated/holding company's Profit & Loss Account.

**Application:** The dividend of ₹75,000 was declared **for the year 2024-25**, i.e., out of profits that existed *before* H Ltd acquired control on 1.4.2025. H Ltd's share = 80% × 75,000 = **₹60,000**. By crediting this to its P&L, H Ltd has recognised as *revenue income* what is really a recovery of the price it paid — the profits distributed were among the very net assets H valued when it computed goodwill. This **overstates the group's distributable profit and overstates goodwill**.

**Corrected computation:**
| | ₹ |
|---|---|
| Original cost of investment | 6,50,000 |
| Less: Pre-acquisition dividend credited to investment | 60,000 |
| **Adjusted cost of investment** | **5,90,000** |
| Less: H's share of net assets = 80% × 5,75,000 | 4,60,000 |
| **Goodwill (corrected)** | **1,30,000** |

The ₹60,000 wrongly taken to P&L must be **removed from P&L and credited to Investment.**

**Conclusion:** H Ltd's treatment is **invalid.** The ₹60,000 is a capital receipt; correcting it reduces the carrying cost of the investment to ₹5,90,000 and results in goodwill of ₹1,30,000.

**Why this way (the reasoning):** The logic follows from *what the parent actually bought*. On the acquisition date the price of ₹6,50,000 bought a bundle of net assets that **included the undistributed 2024-25 profits**. When those very profits are later paid out as dividend, the parent is simply getting back a slice of what it already owned and paid for — no new wealth is created, so recognising income would be double-counting. Reducing the investment cost keeps goodwill (the true premium) intact and prevents inflating distributable reserves. The mirror rule — dividends out of **post-acquisition** profits *are* income (the group earned them) — is what makes the pre/post distinction decisive here.

*(Full-marks tip: state the capital-vs-revenue nature, quantify the 80% share, and show the reduction in investment cost feeding into goodwill. A common error is netting the dividend against consolidated P&L instead of against the investment/cost of control.)*

---

### Q94. Ch: Consolidated Financial Statements — Meaning of Control (Marks: 5) [Case/Application]
**Question:** A Ltd holds only **45% of the equity of B Ltd**, but under a shareholders' agreement it has the right to **appoint 4 of B Ltd's 6 directors** and thereby controls B's board and operating decisions. A Ltd's directors argue that since holding is below 50%, B is **not a subsidiary** and need not be consolidated. Separately, A Ltd holds **60% of C Ltd but intends to sell it within 3 months**. **Examine** whether A Ltd must consolidate B Ltd and C Ltd.

**Answer:**
**Governing principle:** "Subsidiary" is defined by **control**, which arises *either* from ownership of **more than one-half of the voting power**, *or* from **control over the composition of the Board of Directors** — i.e., the power to appoint/remove a majority of directors. Control, not mere shareholding percentage, is the test; a parent must consolidate all subsidiaries.

**Application — B Ltd:** Although A Ltd holds only 45% of equity, its contractual right to **appoint 4 of 6 directors** gives it control over the composition of the Board — it can direct B Ltd's operating and financial policies. This satisfies the *second limb* of the control test **independently of the voting-power test**. Therefore B Ltd **is a subsidiary** and the directors' "below 50%" argument is **invalid** — it wrongly treats voting percentage as the *only* route to control. B Ltd **must be consolidated.**

**Application — C Ltd:** A Ltd holds 60% (control exists), so C Ltd is a subsidiary. The intention to dispose of it shortly does not, by itself, remove it from consolidation for the current period; however, a subsidiary **acquired and held exclusively with a view to its subsequent disposal in the near future** may be excluded from consolidation (it is a temporary control). Since C was evidently held as a long-term investment (60% stake) and only *now* is disposal intended, control still exists at the reporting date and C Ltd **should be consolidated**, with appropriate disclosure of the intended disposal.

**Conclusion:** **B Ltd must be consolidated** (control via board composition); **C Ltd must be consolidated** as control subsists at the reporting date.

**Why this way (the reasoning):** Consolidation is driven by the **substance of control**, because the purpose of group accounts is to show the resources the parent *commands and directs* — regardless of the legal form of shareholding. If a 45% holder can steer the board, the economic reality is that it controls those assets, and excluding B would let A hide a controlled entity's leverage and results off its group balance sheet. Conversely, the disposal exemption is narrow — it applies only to control that was *temporary from inception*, not to a long-held subsidiary the parent later decides to sell — otherwise companies could dodge consolidation simply by declaring a disposal intention.

*(Full-marks tip: name *both* limbs of the control test and apply each — board-composition control is the crux for B. For C, distinguish "temporary control from acquisition" from "later intention to sell." Answers that stop at "45% < 50% so not a subsidiary" score near zero.)*

---

### Q95. Ch: Accounting for LLP — Conversion of Partnership Firm into LLP (Marks: 8) [Problem]
**Question:** A and B, sharing profits **3:2**, convert their firm **AB & Co.** into **AB LLP** on 31.3.2026. On conversion: Land is revalued to ₹3,50,000; Plant reduced to ₹1,70,000; Stock reduced to ₹1,10,000; a provision for doubtful debts of **5% on debtors** is created; goodwill is valued at ₹1,00,000 and recorded. The general reserve is distributed. Prepare the **Revaluation Account, Partners' Capital Accounts, and the opening Balance Sheet of AB LLP.**

| Balance Sheet of AB & Co. as at 31.3.2026 | ₹ | | ₹ |
|---|---|---|---|
| Capital: A | 3,00,000 | Land | 2,50,000 |
| Capital: B | 2,00,000 | Plant | 2,00,000 |
| General Reserve | 1,00,000 | Stock | 1,20,000 |
| Creditors | 1,50,000 | Debtors | 1,30,000 |
| | | Bank | 50,000 |
| **Total** | **7,50,000** | **Total** | **7,50,000** |

**Solution:**

**WN-1 — Revaluation changes:** Land +1,00,000; Goodwill +1,00,000 (gains). Plant −30,000; Stock −10,000; PDD 5% × 1,30,000 = −6,500 (losses).

**Revaluation Account**

| Dr | ₹ | Cr | ₹ |
|---|---|---|---|
| To Plant | 30,000 | By Land | 1,00,000 |
| To Stock | 10,000 | By Goodwill | 1,00,000 |
| To Provision for Doubtful Debts | 6,500 | | |
| To Profit t/f: A (3/5) 92,100; B (2/5) 61,400 | 1,53,500 | | |
| **Total** | **2,00,000** | **Total** | **2,00,000** |

**WN-2 — General Reserve distributed 3:2:** A 60,000; B 40,000.

**Partners' Capital Accounts**

| Particulars | A ₹ | B ₹ |
|---|---|---|
| Balance b/d | 3,00,000 | 2,00,000 |
| Add: General Reserve | 60,000 | 40,000 |
| Add: Revaluation Profit | 92,100 | 61,400 |
| **Balance c/d (to LLP)** | **4,52,100** | **3,01,400** |

**Opening Balance Sheet of AB LLP as at 1.4.2026**

| Contribution / Liabilities | ₹ | Assets | ₹ |
|---|---|---|---|
| Partners' Contribution: A | 4,52,100 | Goodwill | 1,00,000 |
| Partners' Contribution: B | 3,01,400 | Land | 3,50,000 |
| Creditors | 1,50,000 | Plant | 1,70,000 |
| | | Stock | 1,10,000 |
| | | Debtors 1,30,000 − PDD 6,500 | 1,23,500 |
| | | Bank | 50,000 |
| **Total** | **9,03,500** | **Total** | **9,03,500** |

**Answer:** Revaluation profit ₹1,53,500 (A ₹92,100, B ₹61,400); partners' contribution in LLP — A ₹4,52,100, B ₹3,01,400; **LLP balance sheet total ₹9,03,500.**

**Why this way (the reasoning):** On conversion the old firm's identity is superseded by the LLP, so all assets and liabilities are brought to their **agreed/fair values as at the conversion date** — the gains and losses on that revaluation belong to the *old* partners in their *old* profit-sharing ratio (3:2), because they arose during the firm's life. Routing them through a **Revaluation Account** keeps that ownership clean before the balances migrate into the LLP. Similarly, accumulated reserves are the old partners' undistributed profits and must be shared 3:2 *before* conversion — leaving them undistributed would wrongly hand a past profit to the LLP as an entity. Goodwill is recorded because the going concern has value beyond its tangible assets, and the partners are entitled to it as at the conversion date. The result is that each partner's opening **contribution** in the LLP faithfully reflects what they brought — original capital + their reserve share + their revaluation share — preserving equity between them across the change of legal form.

*(Full-marks tip: use the OLD ratio (3:2) for revaluation profit and reserves, create the PDD as a *deduction* from debtors in the LLP balance sheet, and label the equity as "Partners' Contribution" (LLP terminology), not "Capital." Deductions for using a new/equal ratio or mis-computing the 5% PDD.)*

---

### Q96. Ch: Accounting for LLP — Statement of Profit Distribution (Marks: 8) [Problem]
**Question:** X, Y and Z are partners in **XYZ LLP** sharing profits **2:2:1**. The LLP agreement provides: interest on capital @ **8% p.a.**; salary/remuneration of **₹1,00,000 each to X and Y** (the working partners); and interest @ **6% p.a. on Z's loan of ₹2,00,000** to the LLP. Capitals: X ₹5,00,000; Y ₹3,00,000; Z ₹2,00,000. The LLP's net profit for 2025-26 **before any of the above** was ₹6,00,000. Prepare the **Profit & Loss Appropriation Statement** and the distribution among partners.

**Solution:**

**WN-1 — Charge vs Appropriation.** Interest on a partner's *loan* is a **charge against profit** (an expense of the LLP, like interest to any lender), so it is deducted *before* arriving at appropriable profit. Interest on capital, remuneration and profit share are **appropriations** of profit.

**WN-2 — Interest on Z's loan:** 6% × 2,00,000 = **₹12,000** (charge).
**WN-3 — Interest on capital @ 8%:** X 40,000; Y 24,000; Z 16,000 → total **80,000**.
**WN-4 — Remuneration:** X 1,00,000 + Y 1,00,000 = **2,00,000**.

**Profit & Loss Appropriation Statement for the year ended 31.3.2026**

| Particulars | ₹ | ₹ |
|---|---|---|
| Net Profit before loan interest & appropriations | | 6,00,000 |
| Less: Interest on Z's Loan (charge) | | (12,000) |
| **Profit available for appropriation** | | **5,88,000** |
| Less: Interest on Capital — X 40,000; Y 24,000; Z 16,000 | 80,000 | |
| Less: Remuneration — X 1,00,000; Y 1,00,000 | 2,00,000 | (2,80,000) |
| **Balance of profit (divisible 2:2:1)** | | **3,08,000** |
| Share — X (2/5) | | 1,23,200 |
| Share — Y (2/5) | | 1,23,200 |
| Share — Z (1/5) | | 61,600 |

**Total credited to each partner:**

| Partner | Interest on Capital | Remuneration | Loan Interest | Profit Share | **Total ₹** |
|---|---|---|---|---|---|
| X | 40,000 | 1,00,000 | — | 1,23,200 | **2,63,200** |
| Y | 24,000 | 1,00,000 | — | 1,23,200 | **2,47,200** |
| Z | 16,000 | — | 12,000 | 61,600 | **89,600** |

**Answer:** Divisible profit ₹3,08,000; total appropriations to X ₹2,63,200, Y ₹2,47,200, Z ₹89,600 (₹6,00,000 fully accounted).

**Check:** 12,000 + 80,000 + 2,00,000 + 3,08,000 = **6,00,000.** ✓

**Why this way (the reasoning):** The pivotal distinction is **charge vs appropriation**. Interest on a partner's *loan* arises because the partner has lent money to the LLP *in the capacity of a lender*, not as an owner deploying capital — so it is a genuine business expense that reduces the profit *before* any owner-reward is calculated, exactly like bank interest. Interest on *capital*, remuneration and the residual profit are **distributions of ownership profit**, made only out of what remains after charges. Getting this order wrong — e.g., treating loan interest as an appropriation, or deducting it *after* computing profit share — would misstate divisible profit and every partner's entitlement, and in a loss year could even mean loan interest goes unpaid (which is legally wrong, since a lender is entitled to interest regardless of profit). The final reconciliation to ₹6,00,000 proves nothing has leaked.

*(Full-marks tip: place loan interest as a CHARGE above "profit available for appropriation," then the 2:2:1 split of the residual. Show the reconciliation. Marks lost for mixing loan interest into appropriations or splitting the whole ₹6,00,000 directly in 2:2:1.)*

---

### Q97. Ch: Accounting for LLP — Nature and Liability (Marks: 5) [Case/Application]
**Question:** Two partners of an LLP contend: (i) "An LLP is just a partnership firm with a fancy name, so it has **no separate legal existence** from us"; and (ii) "Since our liability is limited, a **designated partner can never be personally liable** for anything." A creditor also claims that one designated partner committed fraud and should be personally liable. **Examine the validity** of these contentions.

**Answer:**
**Governing principle (LLP Act, 2008):** An LLP is a **body corporate** with **perpetual succession** and a **legal identity separate from its partners**; it can own property, sue and be sued in its own name. Partners' liability is generally limited to their agreed contribution — **but** this limited-liability shield does **not** protect a partner from liability arising out of the partner's **own wrongful act or fraud**, and the LLP Act expressly makes an LLP and its partners liable in cases of fraud, and imposes unlimited liability for acts done with intent to defraud.

**Application:**
- Contention (i) is **invalid.** Unlike a traditional partnership firm (which has *no* separate legal personality and whose partners *are* the firm), an LLP is a distinct legal person. Its assets and liabilities are its own; the partners are agents of the LLP, not of one another. Calling it "just a partnership" ignores its corporate character and perpetual succession.
- Contention (ii) is **partly valid but overstated.** Limited liability protects a partner from the LLP's ordinary business debts beyond their contribution — that much is true. **However**, it is **not** an absolute shield: a partner remains **personally liable for their own wrongful acts, negligence or fraud.** A partner is *not* liable merely for another partner's wrongdoing (the whole point of LLP), but *is* liable for their own.
- The creditor's claim: if the designated partner **actually committed fraud**, that partner is **personally and unlimitedly liable**, and the LLP too may be liable for the fraud, though other innocent partners are shielded.

**Conclusion:** An LLP **is** a separate legal entity (contention i wrong); limited liability protects partners from the firm's debts but **not** from their own fraud/wrongful acts (contention ii wrong to the extent it claims blanket immunity). The fraudulent designated partner is **personally liable.**

**Why this way (the reasoning):** The LLP form was designed to give the *organisational flexibility of a partnership* with the *limited-liability and separate-personality benefits of a company* — that hybrid is its whole reason for existing, so treating it as "just a partnership" misses the point. But limited liability is a shield against *vicarious* exposure (one partner shouldn't lose everything for a colleague's ordinary business decisions), **not a licence for personal misconduct.** The law deliberately pierces the shield for fraud, otherwise the LLP structure would become a vehicle to defraud creditors with impunity — undermining the very trust that lets LLPs contract freely.

*(Full-marks tip: separate the two contentions and mark each valid/invalid with the reason; the crux is that the liability shield does NOT extend to a partner's own fraud/wrongful act. Answers that just recite "LLP has limited liability" without the fraud exception lose the discriminating marks.)*

---

### Q98. Ch: Company Financial Statements — Balance Sheet as per Schedule III (Marks: 10) [Problem]
**Question:** From the following balances of **XYZ Ltd** as at 31.3.2026, prepare the **Balance Sheet as per Schedule III (Division I) of the Companies Act, 2013**, with the relevant **Notes to Accounts.**

| Particulars | ₹ | Particulars | ₹ |
|---|---|---|---|
| Equity Share Capital | 10,00,000 | Land & Building | 8,00,000 |
| Securities Premium | 2,00,000 | Plant & Machinery (net) | 6,00,000 |
| General Reserve | 1,50,000 | Furniture | 1,00,000 |
| Surplus (P&L, Cr) | 1,20,000 | Goodwill | 1,50,000 |
| 10% Debentures (redeemable 2030) | 4,00,000 | Non-current Investments | 2,00,000 |
| Term Loan from Bank (long-term) | 3,00,000 | Inventories | 3,00,000 |
| Trade Payables | 2,10,000 | Trade Receivables | 2,80,000 |
| Bank Overdraft | 1,30,000 | Cash & Bank | 1,50,000 |
| Provision for Tax | 90,000 | Short-term Loans & Advances | 50,000 |
| Other Current Liabilities (o/s exp.) | 30,000 | | |

**Solution:**

**Balance Sheet of XYZ Ltd as at 31.3.2026** (Schedule III, Division I)

| Particulars | Note | ₹ |
|---|---|---|
| **I. EQUITY AND LIABILITIES** | | |
| (1) Shareholders' Funds | | |
| (a) Share Capital | 1 | 10,00,000 |
| (b) Reserves & Surplus | 2 | 4,70,000 |
| (2) Non-Current Liabilities | | |
| (a) Long-term Borrowings | 3 | 7,00,000 |
| (3) Current Liabilities | | |
| (a) Short-term Borrowings (Bank OD) | | 1,30,000 |
| (b) Trade Payables | | 2,10,000 |
| (c) Other Current Liabilities (o/s exp.) | | 30,000 |
| (d) Short-term Provisions (Provision for Tax) | | 90,000 |
| **TOTAL** | | **26,30,000** |
| **II. ASSETS** | | |
| (1) Non-Current Assets | | |
| (a) Property, Plant & Equipment and Intangibles | 4 | 16,50,000 |
| (b) Non-current Investments | | 2,00,000 |
| (2) Current Assets | | |
| (a) Inventories | | 3,00,000 |
| (b) Trade Receivables | | 2,80,000 |
| (c) Cash & Cash Equivalents | | 1,50,000 |
| (d) Short-term Loans & Advances | | 50,000 |
| **TOTAL** | | **26,30,000** |

**Notes to Accounts**

**Note 2 — Reserves & Surplus:** Securities Premium 2,00,000 + General Reserve 1,50,000 + Surplus (P&L) 1,20,000 = **4,70,000.**
**Note 3 — Long-term Borrowings:** 10% Debentures 4,00,000 + Term Loan from Bank 3,00,000 = **7,00,000.**
**Note 4 — PPE & Intangibles:** Land & Building 8,00,000 + Plant & Machinery 6,00,000 + Furniture 1,00,000 = 15,00,000 (PPE); Goodwill (Intangible) 1,50,000 → total **16,50,000.**

**Answer:** Balance Sheet total = **₹26,30,000** on both sides.

**Why this way (the reasoning):** Schedule III prescribes a **vertical format** ordered by the *nature and expected settlement/realisation period* of each item — non-current before current — because users judge solvency by how much is due/realisable soon versus later. So the **Bank Overdraft is a *short-term borrowing* (current liability)**, whereas the term loan and debentures are *long-term borrowings* (non-current) — classifying by tenure, not by lender type, is the discipline. **Securities Premium is not free profit**; it sits under Reserves & Surplus but is a *capital* reserve restricted by Sec 52 — grouping it here (not as income) reflects that. **Goodwill is an intangible**, disclosed within the PPE-and-intangibles line, not lumped with tangible assets or current assets. **Provision for tax is a short-term provision** (current), because it will be settled within the operating cycle. The whole point of the format is comparability — every company presents the same heads in the same order, so a reader can instantly locate and compare items across firms.

*(Full-marks tip: correct classification is everything — OD as short-term borrowing, tax provision as short-term provision, securities premium under reserves, goodwill as intangible — and each aggregated figure must be supported by a Note. Deductions for showing OD as non-current, or omitting Notes.)*

---

### Q99. Ch: Company Financial Statements — Classification under Schedule III (Marks: 8) [Case/Application]
**Question:** For each of the following items in the accounts of a manufacturing company (operating cycle = 12 months), **state the correct head and sub-head under Schedule III** and give the reasoning. Then indicate the treatment of any that require *splitting*.

| # | Item | ₹ |
|---|---|---|
| (a) | Calls-in-arrear | 20,000 |
| (b) | 12% Debentures ₹5,00,000, of which ₹1,00,000 is redeemable on 30.6.2026 | 5,00,000 |
| (c) | Provision for doubtful debts | 15,000 |
| (d) | Interest accrued but not due on a term loan | 8,000 |
| (e) | Loose tools | 25,000 |
| (f) | Balance with bank in a "unpaid dividend account" | 40,000 |
| (g) | Advance income-tax / TDS receivable | 60,000 |
| (h) | Capital advances (for machinery under purchase) | 1,20,000 |

**Answer:**

| # | Head → Sub-head | Reasoning |
|---|---|---|
| (a) Calls-in-arrear | **Shareholders' Funds → Share Capital** (shown as a *deduction* from Subscribed capital) | It is capital *called but not yet received*; Schedule III requires it to be deducted from called-up capital, not shown as an asset — the company does not yet own that cash. |
| (b) 12% Debentures | **Split:** ₹4,00,000 → Non-Current Liabilities → Long-term Borrowings; **₹1,00,000 → Current Liabilities → Other Current Liabilities (Current maturities of long-term debt)** | A debenture due within 12 months of the reporting date is a *current* obligation. The portion maturing on 30.6.2026 is payable within the operating cycle, so it must be reclassified out of long-term borrowings. |
| (c) Provision for doubtful debts | **Current Assets → Trade Receivables** (shown as a *deduction* from gross receivables) | It is a *contra to an asset*, not a liability; netting it against receivables shows their realisable value. |
| (d) Interest accrued but not due | **Current Liabilities → Other Current Liabilities** | It is a payable that has accrued; "not due" means it is not overdue but still a short-term obligation to be settled soon. |
| (e) Loose tools | **Current Assets → Inventories** | Schedule III specifically classifies loose tools within Inventories, not PPE, as they are consumable/short-lived stores. |
| (f) Unpaid dividend account balance | **Current Assets → Cash & Cash Equivalents → Other bank balances** (earmarked) | It is a bank balance, but *restricted* (earmarked for unpaid dividend), so disclosed separately from free cash. |
| (g) Advance tax / TDS receivable | **Current Assets → Short-term Loans & Advances** (or Other Current Assets) | It is an amount recoverable from the tax authorities, realisable within the operating cycle. |
| (h) Capital advances | **Non-Current Assets → Long-term Loans & Advances (Capital Advances)** | Even though "advance," it relates to acquisition of a *fixed asset* and is **never** classified as current — its benefit is long-term; it is expressly a non-current item under Schedule III. |

**Conclusion:** Item (b) must be **split** between non-current and current; (a) and (c) are **deductions** (from capital and receivables respectively); (h) is the classic trap — a *capital advance is non-current* despite the word "advance."

**Why this way (the reasoning):** Schedule III classification turns on **one question — will it be settled/realised within the operating cycle (or 12 months)?** — applied to the *substance* of each item. Two traps dominate: (1) **Current maturities of long-term debt** — a loan taken for 10 years still has its next-year instalment as a *current* liability, because the test is time-to-settlement from the *reporting date*, not the original tenure; failing to split overstates non-current liabilities and hides near-term repayment pressure. (2) **Capital advances** — the word "advance" tempts a current classification, but the *purpose* (buying a fixed asset) makes it non-current; classification follows the nature of what the advance will *become*, not the label. Contra items (calls-in-arrear, provision for doubtful debts) are *deductions*, never independent assets/liabilities, because they merely adjust the gross figure to its true value.

*(Full-marks tip: the marks concentrate on (b) split, (h) capital advance = non-current, and (a)/(c) as deductions. State the *reason* (settlement horizon / substance) for each, not just the head. A bare list without reasoning is capped.)*

---

### Q100. Ch: Company Financial Statements — Validity of Schedule III Presentation (Marks: 6) [Case/Application]
**Question:** The draft Balance Sheet of PQR Ltd (Schedule III) shows the following. **Examine the validity** of each presentation and state the correction:
(i) **Proposed dividend** of ₹1,50,000 (recommended by the Board after year-end) has been shown as a **current liability (short-term provision).**
(ii) **Debit balance of the Statement of Profit & Loss** (accumulated losses) ₹2,00,000 has been shown as an **asset under "Other Non-current Assets."**
(iii) **Trade receivables** ₹5,00,000 and **advance received from a customer** ₹80,000 have been **netted off** and shown at ₹4,20,000.
(iv) **Bank overdraft** has been shown under **Non-current Liabilities → Long-term Borrowings.**

**Answer:**

**(i) Proposed dividend — INVALID.** A dividend proposed/recommended by the Board *after* the reporting date is a **non-adjusting event**; it is not a present obligation at the balance sheet date (the shareholders have not yet approved it). Under Schedule III / AS 4 (revised), it must **not** be recognised as a liability/provision — it is only **disclosed in the Notes.** Correction: remove ₹1,50,000 from short-term provisions; disclose in Notes to Accounts. This *increases* retained surplus by ₹1,50,000.

**(ii) Debit balance of P&L — INVALID (presentation).** Accumulated losses are **not an asset** — they represent an *erosion of shareholders' funds*. Schedule III requires the debit balance of the Statement of Profit & Loss to be shown under **Reserves & Surplus as a *negative figure* (deduction).** Correction: show (₹2,00,000) within Reserves & Surplus; if reserves are insufficient, it can even make Reserves & Surplus negative — but it can never be an asset. Treating a loss as an asset overstates both assets and net worth.

**(iii) Netting receivables against customer advance — INVALID.** A trade receivable (asset) and an advance from a customer (liability) are **distinct items** and must be shown **gross** — receivables ₹5,00,000 under Current Assets and advance ₹80,000 under **Other Current Liabilities**. Schedule III prohibits set-off unless a legal right of set-off exists against the *same* party for the *same* transaction. Netting hides the true size of both assets and liabilities and distorts liquidity ratios.

**(iv) Bank overdraft as long-term borrowing — INVALID.** A bank overdraft is **repayable on demand**, hence a **current liability → Short-term Borrowings**, not a non-current item. Correction: reclassify ₹(OD amount) to Short-term Borrowings. Showing it as long-term understates current liabilities and flatters the current ratio.

**Conclusion:** All four presentations are **invalid.** Proposed dividend → Notes only; debit P&L → deduction in Reserves & Surplus; receivables and advance → shown gross on opposite sides; overdraft → short-term borrowing.

**Why this way (the reasoning):** Each error breaches a specific presentation principle that exists to prevent misleading the reader. **Proposed dividend** was historically provided for, but revised AS 4 recognises that no *obligation exists* at year-end until members approve — provisioning a non-obligation would understate equity and overstate liabilities. **Accumulated losses as an asset** is the most dangerous fiction: a loss has *destroyed* resources, so parking it on the asset side would let an insolvent company look solvent — hence it must reduce owners' funds. The **no-netting rule** protects the *gross* view of exposure; a company owed ₹5,00,000 and separately holding an ₹80,000 advance has both a real asset and a real obligation, and collapsing them conceals leverage. **Overdraft classification** follows the *repayable-on-demand* test — the whole current/non-current split is meant to signal near-term cash pressure, which mislabelling defeats. The unifying idea: Schedule III presentation must reflect **economic substance and settlement horizon**, never flatter the balance sheet.

*(Full-marks tip: for each item give the *rule* (AS 4 for dividend; Reserves-deduction for debit P&L; no set-off; repayable-on-demand) AND the corrected head. The proposed-dividend point (Notes only, per revised AS 4) and the loss-as-negative-reserve point are the high-value marks; a generic "wrong classification" without the governing principle scores low.)*
