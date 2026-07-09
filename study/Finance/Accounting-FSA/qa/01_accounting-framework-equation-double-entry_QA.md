# Q&A — The Accounting Framework, the Equation & Double-Entry

A mix of conceptual/theory questions (with model answers and interview phrasing) and fully-solved numerical problems. Every number is self-verified: debits = credits, statements tie out, totals reconcile.

---

## Section A — Conceptual / Theory

### Q1. State the accounting equation and explain why it can never be out of balance.

**Answer.** The accounting equation is **Assets = Liabilities + Equity**. It cannot go out of balance because equity is *defined* as the residual — `Equity = Assets − Liabilities` — so the identity is true by construction. Operationally, double-entry bookkeeping enforces it: every transaction is recorded with total debits equal to total credits, which means every entry either moves two items on the same side (netting to zero) or moves one item on each side by an equal amount. Either way the equality is preserved after every single entry.

**How to say it in an interview:** "Assets = Liabilities + Equity, and it balances by definition, not luck — everything the firm owns is financed by either creditors or owners, and equity is the leftover. Double-entry keeps it true after every transaction."

---

### Q2. What is double-entry bookkeeping and what three advantages does it give over single-entry?

**Answer.** Double-entry records every transaction in at least two accounts with equal debits and credits, reflecting the give-and-get nature of every economic event. Three advantages:
1. **Self-checking** — the trial balance must balance; if debits ≠ credits you know there's an error.
2. **Completeness** — you can't record cash leaving without recording where it went; nothing vanishes silently (fraud/error control).
3. **Linkage** — because each event hits two accounts, the three financial statements are mechanically welded and cannot contradict one another if the books balance.

**Interview line:** "It's a faithful transcription of reality — every give has a get — and it buys you self-checking, completeness, and statement linkage in one stroke."

---

### Q3. Explain debits and credits without using the words "increase" or "decrease" as if they were fixed meanings.

**Answer.** Debit means the *left* side of an account; credit means the *right* side. Neither is inherently good or bad or an increase. What a debit *does* depends on which side of the equation the account sits: left-side accounts (**assets and expenses**) increase with a debit; right-side accounts (**liabilities, equity, and revenue**) increase with a credit. Reason: assets sit on the left of A = L + E so they grow on the left; liabilities and equity sit on the right so they grow on the right; expenses reduce equity so they behave opposite to equity (grow with a debit); revenue raises equity so it grows with a credit.

**Mnemonic:** DEAD-CLIC — **D**ebit increases **E**xpenses, **A**ssets, **D**ividends; **C**redit increases **L**iabilities, **I**ncome, **C**apital.

---

### Q4. Differentiate accrual accounting from cash accounting and justify why accrual is the standard for published financials.

**Answer.** Cash accounting recognizes transactions only when cash moves. Accrual recognizes **revenue when earned** and **expenses when incurred**, independent of cash timing. Accrual is standard because it applies the **matching principle** — expenses are reported in the same period as the revenues they generate — so profit reflects economic performance of the period rather than the accident of cash timing. Accrual is what creates receivables, payables, prepaids, accruals, and deferred revenue, and it's the reason a profitable firm can still be cash-poor, which is precisely why the cash flow statement exists.

**Interview line:** "Profit is an accrual concept, cash is fact. Accrual matches effort to reward in the right period; the cash flow statement then reconciles the two."

---

### Q5. Name the two fundamental and four enhancing qualitative characteristics of useful financial information (IFRS framework).

**Answer.**
- **Fundamental (must have both):** (1) **Relevance** — capable of making a difference to decisions, with predictive and/or confirmatory value, bounded by materiality; (2) **Faithful representation** — complete, neutral, free from error.
- **Enhancing:** (1) **Comparability**, (2) **Verifiability**, (3) **Timeliness**, (4) **Understandability**.
- **Pervasive constraint:** cost (benefit of information must exceed cost of producing it).

**Trap:** "Faithful representation" replaced the older term "reliability" — don't use the old word.

---

### Q6. State the IFRS Conceptual Framework definitions of the five elements.

**Answer.**
- **Asset:** a present economic resource controlled by the entity as a result of past events (an economic resource = a right with potential to produce economic benefits).
- **Liability:** a present obligation to transfer an economic resource as a result of past events.
- **Equity:** the residual interest in assets after deducting liabilities.
- **Income:** increases in assets or decreases in liabilities that increase equity, other than contributions from owners.
- **Expense:** decreases in assets or increases in liabilities that decrease equity, other than distributions to owners.

**Insight to voice:** "Income and expense are defined *in terms of* changes in assets and liabilities — the equation is baked into the definitions, which is why profit equals the change in net assets excluding owner transactions."

---

### Q7. Explain the going-concern and prudence concepts, and give an example where prudence produces asymmetry.

**Answer.** **Going concern** assumes the entity will continue operating for the foreseeable future, which justifies carrying assets at cost (not liquidation value) and deferring costs to future periods. **Prudence (conservatism)** says do not overstate assets or income and recognize likely losses early. The asymmetry: inventory is carried at the **lower of cost and net realizable value** — if cost is $100 and market falls to $70, write it down to $70 now (recognize the loss); if market rises to $130, leave it at $100 (do not recognize the gain until realized). Losses are anticipated; gains wait.

---

### Q8. Walk through the accounting cycle in order.

**Answer.** (1) Identify/analyze transactions from source documents; (2) journalize; (3) post to the ledger; (4) unadjusted trial balance; (5) adjusting entries (accruals, deferrals, depreciation); (6) adjusted trial balance; (7) prepare financial statements; (8) closing entries (reset temporary accounts — revenue, expense, dividends — into retained earnings); (9) post-closing trial balance (only permanent balance-sheet accounts remain). Temporary accounts measure one period and are zeroed each year; permanent accounts carry forward — which is why the P&L covers a period and the balance sheet is a point in time.

---

### Q9. Why is depreciation added back on the cash flow statement, and where does it show on all three statements?

**Answer.** Depreciation is a **non-cash** expense — it allocates the cost of a long-lived asset over its useful life (matching) without any cash leaving in that period (the cash left at purchase, recorded as investing). So on the **cash flow statement** we start from net income and add depreciation back because it reduced profit but not cash. It appears: **income statement** as an expense; **cash flow** as an add-back in operating activities; **balance sheet** as accumulated depreciation, a contra-asset reducing net PP&E.

---

### Q10. Is a dividend an expense? Explain its statement impact.

**Answer.** No. A dividend is a **distribution of profit to owners**, not a cost of generating revenue, so it never appears on the income statement and does not affect net income. It reduces **retained earnings** and reduces **cash** (a financing outflow). The roll-forward: `RE_end = RE_beg + Net Income − Dividends`.

---

### Q11. Distinguish IFRS and US GAAP at the conceptual/framework level, with two concrete divergences.

**Answer.** Both share the same objective (useful information to investors/lenders/creditors) and the same qualitative characteristics. The style differs: **IFRS is principles-based** (more judgment, fewer bright lines); **US GAAP is more rules-based** (detailed, industry-specific). Two concrete divergences: (1) **Inventory** — IFRS prohibits LIFO and permits reversal of prior write-downs; US GAAP allows LIFO and prohibits write-down reversals. (2) **Development costs** — IFRS may capitalize development costs meeting IAS 38 criteria; US GAAP generally expenses R&D as incurred. At the level of the accounting equation and double-entry, the two are identical.

---

### Q12. What is deferred revenue, and why is it a liability rather than revenue?

**Answer.** Deferred (unearned) revenue arises when cash is received *before* the good or service is delivered — e.g., an annual subscription paid up front. It's a **liability** because the company owes future performance (or a refund) to the customer; the revenue has not been *earned* yet under accrual/revenue-recognition rules (IFRS 15 / ASC 606). As the obligation is satisfied over time, deferred revenue is reduced and revenue is recognized.

---

## Section B — Numerical Problems

### Q13. Journalize and prove the equation holds.

A firm has these transactions. Record journal entries, then show Assets = Liabilities + Equity after all of them.
1. Owner invests $150,000 cash.
2. Buys equipment $40,000, paying $10,000 cash and $30,000 on a note payable.
3. Buys inventory $20,000 on account (payable).
4. Pays $5,000 of the account payable.

**Solution — journal entries (Dr = Cr each):**
```
1) Cash            Dr. 150,000
       Share Capital        150,000
2) Equipment       Dr.  40,000
       Cash                  10,000
       Note Payable          30,000
3) Inventory       Dr.  20,000
       Accounts Payable      20,000
4) Accounts Payable Dr.  5,000
       Cash                   5,000
```

**Ending balances:**
- Cash = 150,000 − 10,000 − 5,000 = **135,000**
- Equipment = **40,000**
- Inventory = **20,000**
- **Total Assets = 135,000 + 40,000 + 20,000 = 195,000**
- Accounts Payable = 20,000 − 5,000 = **15,000**
- Note Payable = **30,000**
- Share Capital = **150,000**
- **Liabilities + Equity = 15,000 + 30,000 + 150,000 = 195,000** ✓

Assets $195,000 = Liabilities + Equity $195,000. Balanced.

---

### Q14. Build the income statement and retained earnings.

In its first year a company records: Revenue $500,000; COGS $300,000; Operating expenses $120,000; Depreciation $20,000; Interest expense $10,000; Tax rate 25%. It pays a $15,000 dividend. Beginning retained earnings = $0. Compute net income and ending retained earnings.

**Solution:**

| | $ |
|---|---|
| Revenue | 500,000 |
| COGS | (300,000) |
| **Gross profit** | **200,000** |
| Operating expenses | (120,000) |
| Depreciation | (20,000) |
| **Operating income (EBIT)** | **60,000** |
| Interest expense | (10,000) |
| **Pre-tax income** | **50,000** |
| Tax @ 25% | (12,500) |
| **Net income** | **37,500** |

Retained earnings: `RE_end = 0 + 37,500 − 15,000 = **22,500**`.

**Check:** Tax = 50,000 × 0.25 = 12,500 ✓. Net income 50,000 − 12,500 = 37,500 ✓.

---

### Q15. Accrual vs cash — reconcile profit to cash.

During the year a firm: makes credit sales of $200,000, of which $160,000 cash is collected ($40,000 still in receivables); incurs operating expenses of $90,000, of which $80,000 is paid in cash ($10,000 accrued unpaid); records depreciation of $15,000. No tax. Compute net income and net operating cash, and reconcile.

**Solution — Income statement:**

| | $ |
|---|---|
| Sales (earned) | 200,000 |
| Operating expenses (incurred) | (90,000) |
| Depreciation | (15,000) |
| **Net income** | **95,000** |

**Operating cash (direct):**

| | $ |
|---|---|
| Cash collected from customers | 160,000 |
| Cash paid for expenses | (80,000) |
| **Operating cash** | **80,000** |

**Reconciliation (indirect):**

| | $ |
|---|---|
| Net income | 95,000 |
| Add back depreciation (non-cash) | +15,000 |
| Less increase in receivables | (40,000) |
| Add increase in accrued expenses payable | +10,000 |
| **Operating cash** | **80,000** ✓ |

Both methods give **$80,000**. Net income $95,000 exceeds cash $80,000 by $15,000, explained by: +15,000 depreciation add-back, −40,000 receivables build, +10,000 accrual = net −15,000 versus profit. Reconciles exactly.

---

### Q16. The classic "$100 of depreciation, 40% tax" three-statement walk.

Depreciation increases by $100 (tax rate 40%). Show the impact on all three statements.

**Solution.**
- **Income statement:** pre-tax income −$100; tax −$40 (a saving); **net income −$60**.
- **Cash flow statement:** start at net income −$60; add back the full $100 non-cash depreciation; **cash from operations +$40**. (This +$40 is the depreciation tax shield = $100 × 40%.)
- **Balance sheet:** Cash +$40; PP&E (net) −$100 → **assets −$60**. On the other side retained earnings −$60 (from lower net income). Assets −$60 = Equity −$60. **Balances.** ✓

**One-line takeaway to say:** "Depreciation is non-cash but saves $40 of taxes, so cash actually rises $40 even though net income falls $60."

---

### Q17. Full three-statement construction from a capex.

Start of Year 1: Cash $100,000, Share Capital $100,000. During Year 1: buy a machine for $60,000 cash (6-year life, straight-line, no salvage); cash revenue $90,000; cash operating costs $40,000; tax rate 30%. Build all three statements and confirm the balance sheet balances.

**Solution.**

Depreciation = 60,000 / 6 = **10,000/yr**.

**Income statement (Year 1):**

| | $ |
|---|---|
| Revenue | 90,000 |
| Operating costs | (40,000) |
| Depreciation | (10,000) |
| **Pre-tax income** | **40,000** |
| Tax @ 30% | (12,000) |
| **Net income** | **28,000** |

**Cash flow statement (Year 1):**

| | $ |
|---|---|
| Net income | 28,000 |
| Add back depreciation | +10,000 |
| **Cash from operations** | **38,000** |
| Investing — buy machine | (60,000) |
| Financing | 0 |
| **Net change in cash** | **(22,000)** |

Ending cash = 100,000 − 22,000 = **78,000**.
*Direct check:* +90,000 revenue − 40,000 costs − 12,000 tax − 60,000 machine = **−22,000** ✓.

**Balance sheet (end Year 1):**

| Assets | $ | | Liab. & Equity | $ |
|---|---|---|---|---|
| Cash | 78,000 | | Share Capital | 100,000 |
| Machine (gross) | 60,000 | | Retained Earnings | 28,000 |
| Less: Accum. deprec. | (10,000) | | | |
| Machine (net) | 50,000 | | | |
| **Total Assets** | **128,000** | | **Total Liab. & Equity** | **128,000** |

Assets $128,000 = Liab. + Equity $128,000. ✓ Retained earnings = 0 + 28,000 − 0 = 28,000 ✓. Everything ties.

---

### Q18. Deferred revenue over two periods.

On 1 October a firm receives $24,000 cash for a 12-month service contract (service delivered evenly). Its fiscal year ends 31 December. Show the entries and the revenue vs. deferred revenue at year-end.

**Solution.**
At 1 Oct (cash received, nothing earned yet):
```
Cash               Dr. 24,000
     Deferred Revenue      24,000
```
By 31 Dec, 3 of 12 months delivered → earned = 24,000 × 3/12 = **6,000**.
```
Deferred Revenue   Dr. 6,000
     Service Revenue       6,000
```
**Year-end position:**
- Revenue recognized (income statement) = **$6,000**
- Deferred revenue remaining (liability on balance sheet) = 24,000 − 6,000 = **$18,000**

Cash received ($24,000) ≠ revenue earned ($6,000); the $18,000 gap is a liability for future service. Illustrates accrual and revenue recognition.

---

### Q19. Prudence — inventory write-down.

A firm holds three inventory lines. Apply lower-of-cost-and-NRV item by item and compute the write-down.

| Item | Cost | NRV |
|---|---|---|
| A | 30,000 | 34,000 |
| B | 25,000 | 19,000 |
| C | 40,000 | 40,000 |

**Solution.** Take the lower of cost and NRV for each:
- A: lower of 30,000 and 34,000 = **30,000** (no write-down — do NOT write up to 34,000)
- B: lower of 25,000 and 19,000 = **19,000** (write down 6,000)
- C: lower of 40,000 and 40,000 = **40,000** (no change)

Carrying value = 30,000 + 19,000 + 40,000 = **$89,000**. Total cost was 95,000, so write-down = **$6,000**, recognized as an expense (loss) now.
```
Inventory write-down expense  Dr. 6,000
     Inventory                       6,000
```
Item A's unrealized $4,000 gain is ignored — prudence: losses anticipated, gains not.

---

### Q20. Identify the missing figure using the equation.

A company's balance sheet shows Total Assets $850,000 and Total Liabilities $520,000 at year-start. During the year: net income $140,000, dividends $30,000, and a new share issue of $50,000. No other equity movements. What is end-of-year equity, and if end-of-year liabilities are $600,000, what are end-of-year total assets?

**Solution.**
- Beginning equity = Assets − Liabilities = 850,000 − 520,000 = **330,000**.
- Ending equity = 330,000 + net income 140,000 − dividends 30,000 + share issue 50,000 = **490,000**.
- Ending total assets = Liabilities + Equity = 600,000 + 490,000 = **$1,090,000**.

**Check:** equity change = 490,000 − 330,000 = 160,000 = 140,000 − 30,000 + 50,000 ✓.

---

### Q21. Closing entries and temporary accounts.

At year-end before closing, a firm's temporary accounts show: Service Revenue $180,000 (credit balance); Wages Expense $70,000; Rent Expense $24,000; Depreciation Expense $16,000; Dividends $20,000. Show the closing entries and the effect on retained earnings (beginning RE = $95,000).

**Solution.**
Total expenses = 70,000 + 24,000 + 16,000 = **110,000**. Net income = 180,000 − 110,000 = **70,000**.

Closing entries:
```
1) Service Revenue     Dr. 180,000
        Income Summary          180,000
2) Income Summary      Dr. 110,000
        Wages Expense            70,000
        Rent Expense             24,000
        Depreciation Expense     16,000
3) Income Summary      Dr.  70,000
        Retained Earnings        70,000   (net income to RE)
4) Retained Earnings   Dr.  20,000
        Dividends                20,000   (dividends to RE)
```
Ending RE = 95,000 + 70,000 − 20,000 = **$145,000**. All temporary accounts now zero; only permanent accounts carry forward.

**Check:** Income Summary after entries 1–2 = 180,000 − 110,000 = 70,000 credit, cleared to RE in entry 3 ✓.

---

### Q22. Working-capital effect on cash — receivables and payables swing.

A firm reports net income of $120,000. During the year, accounts receivable rose by $25,000, inventory fell by $10,000, accounts payable rose by $18,000, and depreciation was $30,000. Compute cash from operations (indirect method).

**Solution.**

| | $ | Effect on cash |
|---|---|---|
| Net income | 120,000 | — |
| Depreciation (non-cash add-back) | +30,000 | up |
| Increase in receivables | (25,000) | down (cash tied up) |
| Decrease in inventory | +10,000 | up (cash released) |
| Increase in payables | +18,000 | up (cash deferred) |
| **Cash from operations** | **153,000** | |

Working-capital logic: an asset *increase* uses cash (subtract); an asset *decrease* frees cash (add); a liability *increase* defers cash outflow (add). Result: **$153,000**, which is $33,000 above net income mainly due to the $30,000 depreciation add-back plus net favorable working-capital moves (−25,000 + 10,000 + 18,000 = +3,000).

**Check:** 120,000 + 30,000 − 25,000 + 10,000 + 18,000 = 153,000 ✓.

---

*End of Q&A bank. Every numerical answer above has debits equal to credits and every statement ties out — verify each yourself as practice; reproducing the reconciliations from scratch is the fastest way to internalize the mechanics.*
