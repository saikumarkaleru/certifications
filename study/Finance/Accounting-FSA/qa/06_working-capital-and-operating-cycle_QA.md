# Q&A — Working Capital & the Operating Cycle

A practice bank mixing conceptual/theory questions (with model answers and interview delivery) and fully-solved numerical problems. Every number is self-verified and reconciles.

---

## Section A — Theory & conceptual

### Q1. Define working capital, and distinguish net working capital from operating working capital.

**Model answer.** Working capital is the money tied up in day-to-day operations. **Net working capital (NWC) = current assets − current liabilities** — the classic liquidity measure, which *includes* cash and short-term debt. **Operating working capital (OWC) = (current assets − cash) − (current liabilities − short-term debt)** — it strips out financing items to isolate what *operations* tie up.

**Why the distinction matters.** Cash is a financing/investing choice, not an operating requirement; short-term debt is part of the capital structure. In a DCF or three-statement model, "change in working capital" means the *operating* figure — otherwise the free-cash-flow calculation is corrupted.

**How to say it:** "NWC is the liquidity view including cash and debt; OWC is the modeling view — what operations actually lock up. In valuation we always mean OWC."

---

### Q2. Explain from first principles why an increase in accounts receivable reduces cash.

**Model answer.** Under accrual accounting, revenue is recorded when *earned* (goods delivered), not when cash arrives. A credit sale books revenue and creates a receivable — "profit we've earned but not yet collected." Until the customer pays, that profit exists only on paper; no cash came in. So a rising receivable balance means profit is running ahead of cash collection, and the cash-flow statement must *subtract* the increase to reconcile net income to actual cash.

**How to say it:** "A receivable is revenue you've booked but haven't been paid for — the cash is still sitting in the customer's bank account, so cash is lower than profit."

---

### Q3. What is the cash conversion cycle, and how does it differ from the operating cycle?

**Model answer.** The **operating cycle = DIO + DSO** — total days from acquiring inventory to collecting from the customer. The **cash conversion cycle = DIO + DSO − DPO** — the operating cycle *minus* the free financing suppliers extend. The CCC is the number of days cash is actually locked up and must be financed. The operating cycle is about operational speed; the CCC is about the *net cash* the operation ties up after supplier credit.

---

### Q4. Why does DSO use revenue in the denominator while DIO and DPO use COGS?

**Model answer.** Receivables are recorded at *selling price*, so they must be matched against revenue (also at selling price). Inventory and payables are recorded at *cost*, so they must be matched against COGS. Mixing them — e.g., using revenue for DIO — compares a cost-based balance to a price-based flow, overstating turnover and understating DIO. It's a consistency-of-basis argument.

---

### Q5. "A company is highly profitable but keeps running out of cash." Give the most likely explanation and the mechanism.

**Model answer.** Growth consuming working capital. As revenue grows, receivables and inventory scale with it, trapping cash the income statement never expenses. If working-capital intensity is ~20% and the firm grows 30% a year, roughly 6% of revenue disappears into the balance sheet annually. Profit is accrual; converting it to cash requires the balance sheet to cooperate. Secondary causes: rising DSO (customers paying slower), inventory build-up, or heavy capex.

**How to say it:** "It's growing broke — profit on the P&L, cash trapped in receivables and inventory on the balance sheet."

---

### Q6. How can the cash conversion cycle be negative, and what are the advantages and risks?

**Model answer.** When **DPO > DIO + DSO** — the firm collects from customers before paying suppliers (Walmart, Amazon, Dell, SaaS with annual prepay). **Advantage:** suppliers and customers finance the operation, so growth *generates* cash and the firm earns float. **Risk:** in a downturn the cycle unwinds *against* the firm — payables come due while collections and inventory turns dry up — creating a liquidity squeeze exactly when conditions are worst.

---

### Q7. In an unlevered DCF, why do we subtract the increase in working capital from free cash flow?

**Model answer.** An increase in operating working capital is real cash the business must invest to keep operating and growing — cash not available to investors. FCFF = EBIT×(1−t) + D&A − Capex − ΔOWC. We use *operating* working capital (excluding cash and short-term debt) because those are financing items. Ignoring ΔWC would overstate the distributable cash of a growing company.

---

### Q8. List the levers to shorten each component of the CCC, and the trade-off of each.

**Model answer.**
- **Receivables (lower DSO):** tighter credit terms, prompt invoicing, early-payment discounts, factoring, aging-schedule follow-up. *Trade-off:* terms too tight lose sales to easier-credit competitors.
- **Inventory (lower DIO):** JIT, better forecasting, EOQ, ABC analysis, dropshipping. *Trade-off:* too lean risks stockouts, lost sales, and fragile supply chains.
- **Payables (raise DPO):** negotiate longer terms, pay on the due date, supply-chain finance. *Trade-off:* stretching too far forfeits discounts, harms supplier relationships, signals distress.

The goal is to *optimize*, not maximize, each lever — minimize the CCC without breaking the operation.

---

### Q9. What is deferred revenue, and how does it affect working capital and cash?

**Model answer.** Deferred (unearned) revenue is cash collected *before* the good/service is delivered — e.g., a SaaS annual subscription paid upfront. It's an operating *liability* (a "contract liability" under ASC 606 / IFRS 15). When it grows, it *releases* cash — the customer finances the business — so it's a source of working-capital funding. Forgetting it understates a subscription company's cash generation.

---

### Q10. Two companies in the same industry have identical margins but very different CCCs. What does that tell you?

**Model answer.** The shorter-CCC firm ties up far less capital per dollar of sales, so it needs less financing to grow and earns a higher return on invested capital. Same profitability, better capital efficiency. It also suggests superior operational execution — tighter collections, leaner inventory, or stronger supplier bargaining power. For an equity analyst, the low-CCC firm likely deserves a higher multiple on capital-efficiency grounds; for a credit analyst, it has more liquidity headroom.

---

## Section B — Numerical problems

### Q11. Compute DSO, DIO, DPO, the operating cycle, and the CCC.

**Given:** Revenue $2,000,000; COGS $1,460,000; AR $250,000; Inventory $200,000; AP $180,000. Use 365 days, ending balances.

**Solution.**
```
DSO = (250,000 / 2,000,000) × 365 = 0.125 × 365      = 45.63 days
DIO = (200,000 / 1,460,000) × 365 = 0.136986 × 365   = 50.00 days
DPO = (180,000 / 1,460,000) × 365 = 0.123288 × 365   = 45.00 days

Operating cycle = DIO + DSO       = 50.00 + 45.63       = 95.63 days
CCC             = DIO + DSO − DPO = 50.00 + 45.63 − 45.00 = 50.63 days
```
**Answer:** DSO ≈ 45.6, DIO = 50.0, DPO = 45.0, operating cycle ≈ 95.6 days, **CCC ≈ 50.6 days.**

*Verification:* 200,000/1,460,000 = 0.136986 → ×365 = 50.0 ✓; 180,000/1,460,000 = 0.123288 → ×365 = 45.0 ✓.

---

### Q12. Walk through the three statements: buy $20 of inventory for cash.

**Solution.**
- **Balance sheet:** Inventory +$20, Cash −$20. Net assets unchanged; balances.
- **Income statement:** No change (not an expense until sold). Net income unchanged, no tax effect.
- **Cash flow statement:** Operating section — increase in inventory is a −$20 use of cash. Ending cash −$20.

*Journal entry:*
```
Dr Inventory   20
   Cr Cash          20
```
**Key line:** buying inventory for cash simply swaps one asset for another and drains cash; no P&L impact until the goods sell.

---

### Q13. Same purchase, but on credit — then sold. Full cycle with tax.

**Given:** Buy $20 inventory on credit; later sell for $32 cash; COGS $20; tax 40%.

**Event A — buy on credit:**
```
Dr Inventory   20
   Cr Accounts payable   20
```
Cash impact: inventory +20 (use) and payables +20 (source) → **net $0.** No P&L impact.

**Event B — sell for $32 cash, COGS $20, tax 40%:**
```
Dr Cash            32
   Cr Revenue           32
Dr COGS            20
   Cr Inventory         20
Dr Tax expense      4.8      (40% × (32 − 20) = 4.8)
   Cr Taxes payable      4.8
```
*Income statement:*
```
Revenue        32.0
COGS         (20.0)
Pretax        12.0
Tax (40%)     (4.8)
Net income     7.2
```
*Cash flow (indirect) for Event B:*
```
Net income                    +7.2
(+) Decrease in inventory    +20.0
(+) Increase in taxes payable +4.8
Cash from operations         +32.0
```
Direct check: cash in $32, cash out $0 → +$32 ✓.

*Balance sheet, both events combined:*
```
Assets:     Cash +32, Inventory 0 (+20 then −20)          = +32
Liab & Eq:  AP +20, Taxes payable +4.8, Ret. earnings +7.2 = +32  ✓
```
**Balances.** Profit and cash only materialize at the point of sale.

---

### Q14. One-time cash release from improving DSO.

**Given:** Revenue $3,650,000. DSO falls from 60 to 40 days. How much cash is released? (365 days.)

**Solution.**
```
Daily revenue = 3,650,000 / 365 = 10,000 per day
AR at DSO 60  = 60 × 10,000 = 600,000
AR at DSO 40  = 40 × 10,000 = 400,000
Cash released = 600,000 − 400,000 = 200,000
```
**Answer:** a **one-time** cash inflow of **$200,000**. It permanently lowers capital employed but does not recur — you can't collect faster than day zero.

*Verification:* 20 days × 10,000/day = 200,000 ✓.

---

### Q15. Working-capital drag on free cash flow from growth.

**Given:** Revenue grows $200M → $260M (30%). COGS 65% of revenue. DSO 50, DIO 70, DPO 40 (stable). Net income $22M; D&A $9M; capex $11M. Compute ΔOWC and FCF. (365 days, ending balances.)

**Solution.**

Year 0 (Rev 200, COGS 130):
```
AR  = 50/365 × 200 = 27.397
Inv = 70/365 × 130 = 24.932
AP  = 40/365 × 130 = 14.247
OWC0 = 27.397 + 24.932 − 14.247 = 38.082
```
Year 1 (Rev 260, COGS 169):
```
AR  = 50/365 × 260 = 35.616
Inv = 70/365 × 169 = 32.411
AP  = 40/365 × 169 = 18.521
OWC1 = 35.616 + 32.411 − 18.521 = 49.507
```
```
ΔOWC = 49.507 − 38.082 = 11.425   (increase → use of cash)
```
Intensity check: OWC0/Rev0 = 38.082/200 = 19.04%; 0.1904 × 60 = 11.42 ✓.

**Free cash flow:**
```
Net income     22.000
(+) D&A          9.000
(−) ΔOWC       (11.425)
(−) Capex      (11.000)
FCF              8.575
```
**Answer:** ΔOWC = **$11.43M**; **FCF ≈ $8.58M** despite $22M net income — growth consumed over $11M through working capital.

*Verification:* ΔOWC computed two ways agrees (11.425 ≈ 11.42) ✓; FCF: 22 + 9 − 11.425 − 11 = 8.575 ✓.

---

### Q16. Negative working capital and float.

**Given:** DIO 15, DSO 3, DPO 45. Revenue $600M, COGS $450M. Compute CCC, sign-check OWC, and estimate the supplier float in dollars.

**Solution.**
```
CCC = 15 + 3 − 45 = −27 days
```
Balances:
```
AR  = 3/365  × 600 = 4.932
Inv = 15/365 × 450 = 18.493
AP  = 45/365 × 450 = 55.479
OWC = 4.932 + 18.493 − 55.479 = −32.055   (negative ✓)
```
Float estimate:
```
Daily COGS = 450 / 365 = 1.2329
27 days × 1.2329 = 33.29M of supplier-provided financing
```
**Answer:** CCC = **−27 days**, OWC ≈ **−$32M**, ~$33M of operations financed by suppliers/customers. Growth here *releases* cash.

*Verification:* CCC 15+3−45 = −27 ✓; OWC negative ✓.

---

### Q17. The economics of an early-payment discount (2/10 net 30).

**Given:** A supplier offers 2/10 net 30. Should the company pay on day 10? Compute the implied annualized cost of *not* taking the discount.

**Solution.**
```
Discount = 2%; you forgo it to keep cash from day 10 to day 30 = 20 extra days.
Cost per period = discount / (1 − discount) = 2 / 98 = 2.0408%
Periods per year = 365 / 20 = 18.25
Annualized (simple) = 2.0408% × 18.25 = 37.24%
```
**Answer:** the implied cost of skipping the discount is ≈ **37.2% annualized.** Unless the firm's cost of capital exceeds that (or it's in a cash crisis), it should **pay on day 10 and take the discount** — a superb return on cash.

*Verification:* 2/98 = 0.020408; ×18.25 = 0.3724 ✓.

---

### Q18. Effect of extending DPO on cash.

**Given:** COGS $1,825,000. The company negotiates supplier terms from 30 to 50 days (DPO 30 → 50). How much cash does this free? (365 days.)

**Solution.**
```
Daily COGS = 1,825,000 / 365 = 5,000 per day
AP at DPO 30 = 30 × 5,000 = 150,000
AP at DPO 50 = 50 × 5,000 = 250,000
Cash released = 250,000 − 150,000 = 100,000
```
**Answer:** a **one-time $100,000** cash inflow (payables rising = source of cash). Caveat: don't stretch so far you forfeit early-payment discounts or damage supplier relationships.

*Verification:* 20 extra days × 5,000/day = 100,000 ✓.

---

### Q19. Full CCC comparison — which company is more capital-efficient?

**Given:**
| | Company A | Company B |
|---|---|---|
| Revenue | $1,000 | $1,000 |
| COGS | $700 | $700 |
| AR | $110 | $60 |
| Inventory | $140 | $90 |
| AP | $58 | $115 |

Compute each CCC and interpret. (365 days.)

**Solution.**
```
Company A:
 DSO = 110/1000 × 365 = 40.15
 DIO = 140/700  × 365 = 73.00
 DPO = 58/700   × 365 = 30.24
 CCC = 73.00 + 40.15 − 30.24 = 82.91 days

Company B:
 DSO = 60/1000 × 365 = 21.90
 DIO = 90/700  × 365 = 46.93
 DPO = 115/700 × 365 = 59.96
 CCC = 46.93 + 21.90 − 59.96 = 8.87 days
```
**Answer:** A's CCC ≈ **83 days** vs. B's ≈ **9 days.** With identical margins, **B is far more capital-efficient** — it collects faster, holds less inventory, and pays suppliers slower, so it ties up ~74 fewer days of cash per cycle and needs much less financing to grow. B likely earns a higher return on invested capital and deserves a premium on capital-efficiency grounds.

*Verification:* A CCC: 73.00 + 40.15 − 30.24 = 82.91 ✓; B CCC: 46.93 + 21.90 − 59.96 = 8.87 ✓.

---

### Q20. Shrinking releases cash — the symmetric case.

**Given:** A firm with WC intensity of 25% sees revenue *fall* from $400M to $320M. Estimate the working-capital cash effect.

**Solution.**
```
ΔRevenue = 320 − 400 = −80
ΔOWC ≈ intensity × ΔRevenue = 0.25 × (−80) = −20
```
A *decrease* in OWC of $20M is a **source of cash** of **+$20M.**
**Interpretation:** As sales fall, receivables collect and inventory sells down faster than replaced, releasing ~$20M of trapped cash. This is why declining businesses often show a temporary FCF boost that can *mask* deteriorating fundamentals — a trap for the unwary analyst.

*Verification:* 0.25 × −80 = −20; decrease in asset-like WC → +$20M cash ✓.

---

### Q21. Reconcile net income to operating cash flow via working capital.

**Given:** Net income $50; D&A $12; AR increased $8; inventory increased $15; AP increased $6; accrued expenses increased $4. Compute operating cash flow (indirect method).

**Solution.**
```
Net income                          50
(+) D&A                             12
(−) Increase in AR                  (8)
(−) Increase in inventory          (15)
(+) Increase in AP                   6
(+) Increase in accrued expenses     4
Cash from operations                49
```
**Answer:** **$49.** Net working-capital change = −8 − 15 + 6 + 4 = **−13** (a net use of cash); OCF = 50 + 12 − 13 = 49.

*Verification:* 50 + 12 − 8 − 15 + 6 + 4 = 49 ✓.

---

### Q22. Financing gap from a big new contract.

**Given:** A manufacturer wins a contract adding $73M of annual revenue. Its ratios: DSO 60, DIO 45, DPO 30; COGS is 70% of revenue. Estimate the incremental working capital the contract requires. (365 days.)

**Solution.**
```
Incremental COGS = 70% × 73 = 51.1
Incremental AR  = 60/365 × 73   = 12.000
Incremental Inv = 45/365 × 51.1 = 6.300
Incremental AP  = 30/365 × 51.1 = 4.200
Incremental OWC = 12.000 + 6.300 − 4.200 = 14.100
```
**Answer:** the contract locks up **~$14.1M** of additional working capital that must be financed *before* the profit is realized. Winning the contract is a cash *outflow* in year one — the classic reason a growing manufacturer must arrange a credit line alongside a big new order.

*Verification:* AR 73×60/365 = 12.0 ✓; Inv 51.1×45/365 = 6.30 ✓; AP 51.1×30/365 = 4.20 ✓; OWC 12 + 6.3 − 4.2 = 14.1 ✓.
