# Q&A — Accrual Accounting & Revenue Recognition

A mixed bank of theory and numerical problems. Every numerical answer is self-checked so debits equal credits and totals tie. Use the "How to say it" lines verbatim in interviews.

---

## Section A — Theory / conceptual

### Q1. What is the fundamental difference between accrual and cash accounting?
**Answer.** Cash accounting records revenue and expenses when cash is received or paid. Accrual accounting records revenue when it is *earned* (goods/services transferred) and expenses when they are *incurred* (resources consumed), regardless of cash timing. Accrual reflects economic performance; cash reflects liquidity. IFRS and US GAAP require accrual for all material entities.

**How to say it:** "Cash accounting tracks when money moves; accrual tracks when value is created. The two only agree over the life of the business — in any single period they diverge by the change in accruals."

### Q2. Why can a highly profitable company still go bankrupt?
**Answer.** Profit is an accrual measure; solvency needs cash. A firm can book revenue faster than it collects (ballooning receivables), tie up cash in inventory, or over-invest in capex, so operating cash flow lags net income. If it can't fund payroll or debt service, it fails despite profits.

**How to say it:** "Profit pays no bills — cash does. Watch the gap between net income and operating cash flow; if receivables and inventory are eating the profit, that's the warning."

### Q3. Deferred revenue vs accrued revenue — define and classify each.
**Answer.** **Deferred (unearned) revenue** = cash received *before* delivery → a **liability** (you owe a service). **Accrued revenue** = revenue earned *before* billing/collection → an **asset** (the customer owes you). They sit on opposite sides of the balance sheet and reflect opposite cash-vs-delivery timing.

**How to say it:** "Cash first, work later — that's a liability. Work first, cash later — that's an asset."

### Q4. What are the four types of adjusting entries?
**Answer.** (1) Accrued revenue — Dr receivable / Cr revenue; (2) accrued expense — Dr expense / Cr payable; (3) deferred revenue — Dr unearned revenue / Cr revenue; (4) prepaid/deferred expense — Dr expense / Cr prepaid asset. Types 1–2 are accruals (recorded ahead of cash), 3–4 are deferrals (catching up to cash already moved). Each hits one income-statement and one balance-sheet account and **never** touches cash.

**How to say it:** "Two accruals, two deferrals; every one has an income-statement leg and a balance-sheet leg, and none of them ever touches cash."

### Q5. State the matching principle and its three forms.
**Answer.** Expenses are recognized in the same period as the revenues they help generate. Three forms: (1) direct cause-and-effect (COGS matched to sales); (2) systematic and rational allocation over benefit periods (depreciation, amortization); (3) immediate recognition when there's no future benefit (most admin costs, advertising). Matching is the reason prepaids, accruals, and depreciation exist.

### Q6. Name and briefly explain the five steps of IFRS 15 / ASC 606.
**Answer.** (1) Identify the contract — approved, committed, collection probable. (2) Identify performance obligations — each distinct promise. (3) Determine the transaction price — including variable consideration subject to the constraint. (4) Allocate price to obligations by standalone selling price. (5) Recognize revenue as each obligation is satisfied — over time or at a point in time when control transfers.

**How to say it:** "Contract, obligations, price, allocate, recognize — the whole thing answers 'what did we deliver and what price will we keep?'"

### Q7. When is revenue recognized *over time* rather than at a point in time?
**Answer.** Over time if any one of the three IFRS 15 §35 criteria is met: (a) the customer simultaneously receives and consumes the benefit as the entity performs; (b) the entity's work creates/enhances an asset the customer controls as it's created; (c) the asset has no alternative use to the entity and there's an enforceable right to payment for work done to date. Otherwise, recognize at the point control transfers.

### Q8. Explain the "constraint" on variable consideration.
**Answer.** Variable amounts (discounts, rebates, bonuses, penalties) are estimated by expected value or most likely amount, but included in the transaction price only to the extent it is *highly probable* that a significant revenue reversal will not subsequently occur. This prevents over-optimistic estimates from inflating revenue.

### Q9. Gross vs net revenue (principal vs agent) — what's the test?
**Answer.** **Control.** If the entity controls the good/service *before* transfer to the customer, it's the principal and recognizes revenue **gross** (full price, supplier cost in COGS). If it merely arranges for another party to provide it, it's an agent and recognizes revenue **net** (only its commission). Critical for marketplaces and platforms because it swings headline revenue enormously.

### Q10. Contract asset vs accounts receivable — what's the difference?
**Answer.** Both are assets. **Accounts receivable** = an *unconditional* right to consideration (billed; only the passage of time remains). **Contract asset** = a right to consideration that is still *conditional* on something other than time (e.g., completing another obligation) — i.e., earned but not yet billable.

### Q11. How does a $10 increase in deferred revenue flow through the three statements? (indirect method)
**Answer.** Income statement: no impact at the moment of increase (it's unearned). Cash flow statement: +$10 add-back in operating activities (cash came in). Balance sheet: cash +$10, deferred revenue liability +$10 → balances. Revenue hits the P&L only later, when the liability is drawn down.

### Q12. Why is the completed-contract method generally disallowed under IFRS 15?
**Answer.** If a contract meets the over-time criteria, economic value is transferred continuously, so recognizing nothing until completion would misrepresent years of activity as zero then a lump. IFRS 15 requires over-time recognition by a progress measure. Point-in-time (completion) recognition survives only when the over-time criteria are *not* met.

---

## Section B — Numerical problems

### Q13. Basic deferred revenue (subscription)
**Problem.** On 1 Sep 20X1 a firm collects $6,000 for a 12-month service, earned evenly, and its year ends 31 Dec 20X1. Give the entries and the year-end balances.

**Solution.**
- Monthly revenue = 6,000 / 12 = $500.
- Months earned in 20X1: Sep, Oct, Nov, Dec = 4 → revenue = 4 × 500 = **$2,000**.

```
1 Sep:   Dr Cash 6,000 / Cr Deferred revenue 6,000
31 Dec:  Dr Deferred revenue 2,000 / Cr Revenue 2,000
```

- Revenue 20X1 = **$2,000**; Deferred revenue (liability) = 6,000 − 2,000 = **$4,000**.
- **Check:** revenue $2,000 + deferred $4,000 = $6,000 = cash collected ✓.

### Q14. Prepaid expense adjustment
**Problem.** On 1 Oct 20X1 a firm pays $9,000 for 18 months of insurance. Year ends 31 Dec 20X1. Entries and balances.

**Solution.**
- Monthly cost = 9,000 / 18 = $500.
- Months consumed in 20X1: Oct, Nov, Dec = 3 → expense = 3 × 500 = **$1,500**.

```
1 Oct:  Dr Prepaid insurance 9,000 / Cr Cash 9,000
31 Dec: Dr Insurance expense 1,500 / Cr Prepaid insurance 1,500
```

- Expense 20X1 = **$1,500**; Prepaid asset remaining = 9,000 − 1,500 = **$7,500**.
- **Check:** expense $1,500 + prepaid $7,500 = $9,000 paid ✓.

### Q15. Accrued expense (wages) spanning year-end
**Problem.** Employees earn $10,000 of wages in the last week of Dec 20X1, paid 3 Jan 20X2. Show both entries and the effect on 20X1.

**Solution.**
```
31 Dec 20X1: Dr Wages expense 10,000 / Cr Wages payable 10,000
3 Jan 20X2:  Dr Wages payable 10,000 / Cr Cash 10,000
```
- 20X1: expense +$10,000, liability +$10,000. No cash in 20X1.
- **Check:** the payable created in 20X1 ($10,000) is exactly extinguished by the 20X2 cash payment ($10,000) ✓.

### Q16. Accrued revenue (interest) at a mid-quarter year-end
**Problem.** A bank holds a loan paying $1,800 interest per quarter in arrears; the quarter runs Nov–Jan. At 31 Dec 20X1, two of the three months (Nov, Dec) are earned. Show the year-end accrual and the January cash-receipt entry.

**Solution.**
- Monthly interest = 1,800 / 3 = $600. Earned by 31 Dec = 2 × 600 = **$1,200**.

```
31 Dec 20X1: Dr Accrued interest receivable 1,200 / Cr Interest income 1,200
31 Jan 20X2: Dr Cash 1,800
                Cr Accrued interest receivable 1,200
                Cr Interest income 600
```
- **Check:** total interest recognized across the quarter = 1,200 (20X1) + 600 (20X2) = $1,800 = cash received ✓; the accrued asset is fully reversed ✓.

### Q17. Five-step allocation (bundle)
**Problem.** A company sells software + 2 years of support for a single $50,000 price, paid up front. Standalone selling prices: software $40,000 (delivered day 1, point in time), support $20,000 (over 24 months). Allocate and give Year-1 revenue.

**Solution.**
- Total SSP = 40,000 + 20,000 = 60,000. Allocate the $50,000 price by SSP:

| PO | SSP | % | Allocated |
|---|---|---|---|
| Software | 40,000 | 66.667% | 33,333 |
| Support | 20,000 | 33.333% | 16,667 |
| **Total** | **60,000** | **100%** | **50,000** ✓ |

- Software: recognized day 1 → **$33,333**.
- Support: 16,667 / 24 = $694.44/month. Year 1 (12 months) = **$8,333**.
- **Year-1 revenue = 33,333 + 8,333 = $41,666.** Deferred revenue end of Year 1 = 16,667 − 8,333 = **$8,334** (rounding). Year 2 recognizes the remaining $8,334.
- **Check:** total recognized over 2 years = 33,333 + 16,667 = $50,000 = cash ✓.

### Q18. Percentage-of-completion, three-year contract
**Problem.** Contract price $20,000,000. Total estimated cost $16,000,000 (unchanged). Costs incurred: 20X1 $4,000,000; 20X2 $8,000,000; 20X3 $4,000,000. Cost-to-cost. Compute revenue and gross profit each year.

**Solution.**

| Year | Cost in yr | Cum cost | % complete | Rev to date | Revenue in yr | GP in yr |
|---|---|---|---|---|---|---|
| 20X1 | 4,000,000 | 4,000,000 | 25% | 5,000,000 | 5,000,000 | 1,000,000 |
| 20X2 | 8,000,000 | 12,000,000 | 75% | 15,000,000 | 10,000,000 | 2,000,000 |
| 20X3 | 4,000,000 | 16,000,000 | 100% | 20,000,000 | 5,000,000 | 1,000,000 |

- **Checks:** revenue 5+10+5 = **$20m** = price ✓. Cost 4+8+4 = **$16m** ✓. GP 1+2+1 = **$4m** = 20 − 16 ✓.

### Q19. Percentage-of-completion with a cost re-estimate
**Problem.** Price $12,000,000. At end 20X1 costs incurred $3,000,000, total estimated cost $12,000,000... corrected: original total est cost $10,000,000. At end 20X2 the estimate is revised: cumulative cost $8,400,000, revised total cost $12,000,000. Contract finishes in 20X3 at that cost. Compute revenue and profit each year.

**Solution.**
- **20X1:** % = 3,000,000 / 10,000,000 = 30%. Rev = 30% × 12,000,000 = 3,600,000. Cost 3,000,000 → **GP 600,000**.
- **20X2:** revised total cost 12,000,000; cumulative cost 8,400,000 → % = 70%. Rev to date = 70% × 12,000,000 = 8,400,000. Rev in 20X2 = 8,400,000 − 3,600,000 = **4,800,000**. Cost in 20X2 = 8,400,000 − 3,000,000 = 5,400,000 → **GP −600,000** (a catch-up; the profit estimate fell because total cost rose to equal price... check below).
- **20X3:** % = 100%. Rev to date 12,000,000. Rev in 20X3 = 12,000,000 − 8,400,000 = **3,600,000**. Cost 20X3 = 12,000,000 − 8,400,000 = 3,600,000 → **GP 0**.

- **Checks:** revenue 3,600,000 + 4,800,000 + 3,600,000 = **12,000,000** = price ✓. Cost 3,000,000 + 5,400,000 + 3,600,000 = **12,000,000** ✓. Total GP = 600,000 − 600,000 + 0 = **$0** = 12,000,000 − 12,000,000 ✓. The re-estimate correctly claws back the early profit.

### Q20. Onerous (loss-making) contract
**Problem.** Price $8,000,000. At end 20X1, costs incurred $2,000,000; the firm now estimates total cost at $9,000,000 (> price). % complete on a cost basis = 2/9. How much revenue, cost, and profit/loss in 20X1?

**Solution.**
- % complete = 2,000,000 / 9,000,000 = 22.22%.
- Revenue 20X1 = 22.22% × 8,000,000 = **1,777,778**.
- The contract is onerous: total expected loss = 8,000,000 − 9,000,000 = **−1,000,000**, recognized *in full immediately*.
- Cost recognized in 20X1 = revenue − loss to be shown so total P&L = loss. Profit already implied by % of a loss is zero cost basis... practical booking: recognize revenue 1,777,778 and a cost sufficient to reflect the *entire* $1,000,000 loss now.
- **Book:** revenue 1,777,778; recognize the full onerous loss of $1,000,000 in 20X1. Costs to date $2,000,000 are expensed and an additional provision of $777,778 is raised so that 20X1 loss = revenue 1,777,778 − (2,000,000 + 777,778) = **−1,000,000**.
- **Check:** the entire anticipated loss of $1,000,000 hits 20X1, none is deferred ✓ (conservatism / IAS 37 onerous-contract provision alongside IFRS 15).

**How to say it:** "Foreseeable total loss is booked immediately and in full — you never spread a loss by percentage complete."

### Q21. Profit-to-cash reconciliation
**Problem.** Net income $500,000. During the year: AR increased $120,000, inventory increased $40,000, accounts payable increased $30,000, deferred revenue increased $60,000, depreciation $80,000. Compute operating cash flow (indirect method).

**Solution.**
```
Net income                         500,000
+ Depreciation                      80,000
− Increase in AR                  (120,000)
− Increase in inventory            (40,000)
+ Increase in AP                    30,000
+ Increase in deferred revenue      60,000
= Cash from operations             510,000
```
- **Check:** 500,000 + 80,000 − 120,000 − 40,000 + 30,000 + 60,000 = **$510,000** ✓. CFO exceeds NI because non-cash depreciation and the deferred-revenue/payables inflows outweigh the receivables and inventory build.

### Q22. Contract asset vs contract liability
**Problem.** On a project, cumulative revenue recognized to date is $2,500,000 and cumulative amounts billed to the customer are $2,000,000. (a) What appears on the balance sheet? (b) If instead billings were $2,900,000, what appears?

**Solution.**
- (a) Recognized 2,500,000 > billed 2,000,000 by $500,000 → **contract asset (unbilled receivable) $500,000**.
- (b) Billed 2,900,000 > recognized 2,500,000 by $400,000 → **contract liability (deferred revenue) $400,000**.
- **How to say it:** "Recognized more than billed is an asset; billed more than recognized is a liability. Compare the two cumulative numbers and the sign tells you the side."
