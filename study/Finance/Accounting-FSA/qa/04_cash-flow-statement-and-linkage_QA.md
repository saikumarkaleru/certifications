# Q&A — The Cash Flow Statement & Linking the Three Statements

A mixed bank of conceptual and numerical questions. Numerical answers are fully worked and self-verified. Use the "How to say it in an interview" lines to rehearse out loud.

---

## Q1 (Theory). Why can a profitable company run out of cash?

**Model answer.** Profit is measured on an accrual basis — revenue is recognized when earned and expenses when incurred, regardless of when cash moves. Cash is a physical reality with different timing. A company can book large profits while cash is trapped in growing receivables (sales made but not collected) and inventory (goods bought but not sold), or drained by heavy CapEx and debt repayments that never touch the income statement. The classic signature is positive net income alongside negative or sharply lower operating cash flow, with the gap sitting in working capital.

**How to say it in an interview.** *"Profit is an opinion, cash is a fact. The usual culprit is working capital — receivables and inventory ballooning faster than payables — so the company earns profit it hasn't collected. Positive net income with negative operating cash flow is the tell."*

---

## Q2 (Theory). Walk me through how the three statements link.

**Model answer.** Net income from the income statement flows to two places: it increases retained earnings on the balance sheet, and it is the first line of the cash flow statement's operating section. The cash flow statement adjusts net income for non-cash items (add back depreciation, amortization, stock comp), for working-capital changes, and for investing and financing flows, arriving at the net change in cash — which updates the balance sheet's cash line. The balance sheet must always balance (Assets = Liabilities + Equity). So it is one system: the income statement feeds the other two, and the cash flow statement reconciles accrual profit to the actual cash on the balance sheet.

**How to say it in an interview.** Deliver it in the order income statement → retained earnings + top of CFS → net change in cash → balance sheet cash → "and the balance sheet balances." Crispness signals mastery.

---

## Q3 (Theory). Why do we add back depreciation in the operating section?

**Model answer.** Depreciation is a non-cash expense — it reduced net income but no cash left the business this period. The cash actually went out earlier, when the asset was purchased, and that outflow already appeared in investing as CapEx. Depreciation merely allocates that historical cost over the asset's useful life. To convert accrual profit to cash, we reverse it. Its only real cash effect is the tax it shields.

**How to say it in an interview.** *"It's non-cash. The cash left when we bought the asset — that was CapEx in investing. Depreciation just spreads that cost over time, so I add it back to get to cash. The one real cash effect is the tax shield."*

---

## Q4 (Numerical). The classic depreciation walk-through. Depreciation rises by $10; tax rate 40%. Trace all three statements.

**Worked answer.**

Income statement:
- Depreciation +10 → pretax income −10.
- Tax at 40% falls by 10 × 0.40 = 4.
- Net income −10 + 4 = **−6.**

Cash flow statement:
- Net income enters CFO at −6.
- Add back non-cash depreciation +10.
- CFO = −6 + 10 = **+4.** No investing or financing effect.
- Net change in cash = **+4.**

Balance sheet:
- Cash +4.
- Net PP&E −10 (accumulated depreciation rose 10).
- Asset side: +4 − 10 = **−6.**
- Retained earnings −6 (from lower net income).
- Both sides −6 → **balances.** ✓

**Key line.** Cash goes *up* by 4 — the tax shield — even though depreciation is a non-cash charge. Anyone who says net income falls by the full 10, or that cash falls, has missed it.

---

## Q5 (Numerical). Build a full cash flow statement from these statements (indirect method) and prove it ties out.

**Given — Income statement (Year 2):** Revenue 1,000; COGS 600; OpEx ex-D&A 150; Depreciation 50; Interest 20; Tax @ 25%. **Net income = (1,000 − 600 − 150 − 50 − 20) × (1 − 0.25) = 180 × 0.75 = 135.**

**Balance sheets:**

| Account | Y1 | Y2 | Δ |
|---|---:|---:|---:|
| Cash | 100 | 155 | +55 |
| Accounts receivable | 120 | 150 | +30 |
| Inventory | 80 | 110 | +30 |
| Prepaid expenses | 10 | 15 | +5 |
| PP&E, net | 400 | 470 | +70 |
| Accounts payable | 70 | 90 | +20 |
| Accrued liabilities | 30 | 25 | −5 |
| Income taxes payable | 15 | 25 | +10 |
| Long-term debt | 200 | 250 | +50 |
| Common stock | 150 | 170 | +20 |
| Retained earnings | 245 | 340 | +95 |

Gross PP&E rose from 500 to 620 (+120); no disposals. Accumulated depreciation rose from 100 to 150 (+50 = the year's depreciation).

**Step 1 — dividends.** Ending RE = Beginning RE + NI − Dividends → 340 = 245 + 135 − Div → Dividends = **40.**

**Step 2 — CFO:**

| | |
|---|---:|
| Net income | 135 |
| + Depreciation | 50 |
| − ΔAR | (30) |
| − ΔInventory | (30) |
| − ΔPrepaid | (5) |
| + ΔAP | 20 |
| − ΔAccrued | (5) |
| + ΔTaxes payable | 10 |
| **CFO** | **145** |

**Step 3 — CFI:** CapEx = gross PP&E increase 120 (no disposals) → **CFI = (120).**

**Step 4 — CFF:** Debt +50, equity +20, dividends −40 → **CFF = 30.**

**Step 5 — tie-out:** 145 − 120 + 30 = **55** net change. Beginning cash 100 + 55 = **155** = balance sheet cash line. ✓

---

## Q6 (Numerical). Same company — reconstruct operating cash flow with the direct method and confirm it equals 145.

**Worked answer.**

| Line | Working | Amount |
|---|---|---:|
| Cash from customers | 1,000 − ΔAR 30 | 970 |
| Cash to suppliers | −(600 + ΔInv 30 − ΔAP 20) | (610) |
| Cash for operating expenses | −(150 + ΔPrepaid 5 − ΔAccrued (−5)) | (160) |
| Cash for interest | −20 | (20) |
| Cash for taxes | −(45 − ΔTaxes payable 10) | (35) |
| **CFO** | | **145** |

970 − 610 − 160 − 20 − 35 = **145.** ✓ Identical to the indirect method — the two are the same journey to the same number.

---

## Q7 (Numerical). A $10 increase in inventory, purchased for cash. Walk the three statements. Then repeat if bought on credit.

**Bought for cash:**
- Income statement: no impact (inventory is capitalized on the balance sheet until sold).
- Cash flow statement: inventory (asset) up 10 → use of cash → CFO −10 → cash −10.
- Balance sheet: inventory +10, cash −10 → asset side nets to zero → balances, other side unchanged. ✓

**Bought on credit:**
- Income statement: still no impact.
- Cash flow statement: inventory use −10 offset by accounts payable source +10 → net CFO effect 0 → cash unchanged.
- Balance sheet: inventory +10, accounts payable +10 → assets +10, liabilities +10 → balances. ✓

**Key line.** *"Inventory alone is non-cash until it's sold — the cash question is how you paid for it."*

---

## Q8 (Numerical). Asset disposal. Equipment cost 100, accumulated depreciation 60, sold for 55. Net income 200, total depreciation 50. Show the journal entry and the cash flow treatment.

**Journal entry:**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 55 | |
| Accumulated depreciation | 60 | |
| Equipment (gross) | | 100 |
| Gain on sale | | 15 |
| **Totals** | **115** | **115** |

Gain = proceeds 55 − net book value (100 − 60 = 40) = **15.** Debits = credits. ✓

**Cash flow treatment:**

| Section | Line | Amount |
|---|---|---:|
| CFO | Net income | 200 |
| CFO | + Depreciation | 50 |
| CFO | − Gain on sale | (15) |
| CFI | Proceeds from sale | 55 |

**Why subtract the gain?** The full 55 of cash is an investing inflow shown in CFI. Net income already contains the 15 gain; leaving it in CFO would double-count. So strip 15 out of CFO. Net cash across both sections = −15 + 55 = **40**, equal to the net book value released. ✓

**Mirror rule.** A *loss* is added back in CFO; proceeds still go in CFI.

---

## Q9 (Numerical). Profitable but cash-negative. NI 50, depreciation 20, ΔAR +120, ΔInventory +80, ΔAP +40. Compute CFO and interpret.

**Worked answer.**

| | |
|---|---:|
| Net income | 50 |
| + Depreciation | 20 |
| − ΔAR | (120) |
| − ΔInventory | (80) |
| + ΔAP | 40 |
| **CFO** | **(90)** |

50 + 20 − 120 − 80 + 40 = **(90).** The company earned 50 of profit yet burned 90 of operating cash. Fast revenue growth swelled receivables and inventory far beyond what payables funded. It must raise external financing to survive. A credit analyst flags the +50 NI / −90 CFO divergence as a liquidity warning.

**How to say it in an interview.** *"Positive earnings, negative operating cash — the gap is in working capital. Growth is being financed off the balance sheet, so the company will keep needing outside capital."*

---

## Q10 (Theory). Direct vs indirect method — difference, and which is used?

**Model answer.** Both produce identical operating cash flow. Indirect starts from net income and adjusts for non-cash items and working-capital changes. Direct lists actual cash receipts and payments — cash from customers, cash to suppliers, to employees, for interest, for taxes. Nearly all companies use indirect: less disclosure, cleaner tie to the income statement, and even direct-method filers must include the indirect reconciliation anyway. Both IAS 7 and ASC 230 permit either and encourage direct, but the market uses indirect.

---

## Q11 (Theory). If you could see only one statement, which would you pick?

**Model answer.** The cash flow statement. Cash is far harder to manipulate than earnings, it reveals whether the core business actually generates cash, how much the firm invests, and how it funds itself. It's what a DCF discounts and what actually services debt and pays dividends. Net income can be shaped by accounting choices; cash generation is the truth.

**How to say it.** *"Cash flow statement — cash is a fact, profit is an opinion, and cash is what a DCF values."*

---

## Q12 (Numerical). Reconstruct CapEx from the balance sheet and income statement.

**Given.** Beginning net PP&E 400, ending net PP&E 470, depreciation expense for the year 50, no asset disposals.

**Worked answer.** Net PP&E roll-forward: Ending = Beginning + CapEx − Depreciation − Disposals.
470 = 400 + CapEx − 50 − 0 → CapEx = 470 − 400 + 50 = **120.**

**Check with gross PP&E:** if gross rose 500 → 620 (+120) with no disposals, CapEx = 120. ✓ Consistent.

**How to say it.** *"Change in net PP&E plus depreciation equals CapEx when there are no disposals — 70 plus 50 is 120."*

---

## Q13 (Theory). Where does interest expense appear, and does it differ by standard?

**Model answer.** Interest expense hits the income statement and lowers net income, so under US GAAP (ASC 230) it flows through operating cash flow. Under IFRS (IAS 7) interest paid may be classified in operating *or* financing at the company's policy election, and interest/dividends received may be operating or investing. So before comparing an IFRS company's CFO to a US GAAP one, check the policy — a levered IFRS firm can flatter operating cash flow by parking interest in financing.

---

## Q14 (Numerical). Stock-based compensation of 30 is expensed; net income is 100. What's the CFO effect, and why?

**Worked answer.** Stock comp reduced net income by 30 (it's an operating expense) but no cash left the company — employees were paid in equity. So it's a non-cash charge and is added back in CFO.

| | |
|---|---:|
| Net income | 100 |
| + Stock-based compensation | 30 |
| **CFO contribution** | **130** |

**Trap.** Forgetting stock comp badly understates CFO for tech companies, where it can be a huge expense. It is added back exactly like depreciation.

---

## Q15 (Numerical). Deferred taxes. Tax expense on the income statement is 45, but cash taxes paid were only 30 (the 15 difference is a deferred tax liability increase). Show the CFO adjustment.

**Worked answer.** The income statement expensed 45, but only 30 of cash actually left; the 15 gap increased the deferred tax liability — a non-cash portion of the tax expense. In the indirect method, add back the 15 increase in the deferred tax liability.

| | |
|---|---:|
| ... net income (already reduced by 45 of tax expense) | |
| + Increase in deferred tax liability | 15 |

This restores cash by the 15 that was expensed but not paid, so CFO reflects the true 30 of cash taxes. **Check via direct method:** cash taxes = tax expense 45 − ΔDTL 15 = 30. ✓

---

## Q16 (Theory). Why does the cash flow statement always tie out to the balance sheet cash line?

**Model answer.** Because of the accounting identity. From Assets = Liabilities + Equity, isolating cash gives ΔCash = ΔLiabilities + ΔEquity − ΔNon-cash assets. Every cash flow line is one of those change terms sorted into operating, investing, or financing. So the sum of all sections *must* equal the change in cash — it's algebra, not bookkeeping luck. If it doesn't tie, you've mis-signed or omitted one balance sheet change; the identity guarantees a correct answer exists.

---

## Q17 (Numerical). A company issues 100 of debt, repays 40 of old debt, issues 25 of equity, buys back 15 of stock, and pays 20 of dividends. Compute CFF.

**Worked answer.**

| | |
|---|---:|
| Debt issued | 100 |
| Debt repaid | (40) |
| Equity issued | 25 |
| Share buyback | (15) |
| Dividends paid | (20) |
| **CFF** | **50** |

100 − 40 + 25 − 15 − 20 = **50.** Only *principal* debt movements are financing; the interest on that debt would sit in operating (US GAAP). Dividends never touch the income statement — they reduce retained earnings directly and appear only here.

---

## Q18 (Numerical). Compute levered free cash flow and FCFF.

**Given.** CFO 145, CapEx 120, EBIT 200, tax rate 25%, D&A 50, increase in net working capital 40, net borrowing 50.

**Worked answers.**
- **Levered / simple FCF = CFO − CapEx = 145 − 120 = 25.**
- **FCFE = CFO − CapEx + Net borrowing = 145 − 120 + 50 = 75.**
- **FCFF = EBIT×(1−t) + D&A − CapEx − ΔNWC = 200×0.75 + 50 − 120 − 40 = 150 + 50 − 120 − 40 = 40.**

**How to say it.** *"Levered FCF is CFO minus CapEx — 25 here. FCFF strips out the financing and starts from after-tax EBIT — 40 here — and it's what a DCF discounts to enterprise value."*

---

## Q19 (Theory). A negative-working-capital business generates cash as it grows. Explain.

**Model answer.** Some businesses collect from customers before paying suppliers — subscriptions billed upfront, supermarkets that sell inventory before supplier terms come due. Their operating current liabilities exceed operating current assets, so working capital is negative. As they grow, that negative working capital gets *more* negative, which is a *source* of cash — the opposite of the growth trap. It's a hallmark of a great business model because growth is self-funding.

**How to say it.** *"They're financed by their customers and suppliers. Growing negative working capital throws off cash, so scale funds itself — a prized quality."*

---

## Q20 (Numerical). A loss on sale. Equipment with net book value 40 is sold for 25. Net income 80, depreciation 30. Show the CFO/CFI treatment.

**Worked answer.** Loss = proceeds 25 − net book value 40 = **(15).** The loss reduced net income but wasn't an operating cash outflow, so add it back in CFO; the 25 of proceeds goes to CFI.

| Section | Line | Amount |
|---|---|---:|
| CFO | Net income | 80 |
| CFO | + Depreciation | 30 |
| CFO | + Loss on sale | 15 |
| CFI | Proceeds from sale | 25 |

Net cash from the deal across sections = +15 (CFO) + 25 (CFI) − wait, the loss add-back is a reclassification, not new cash. The only real cash is the 25 proceeds in CFI. The +15 in CFO exactly offsets the −15 the loss put into net income, so operating cash is undistorted. Net book value released (40) = proceeds 25 + loss 15. ✓

**Mirror of Q8.** Gain → subtract in CFO; loss → add back in CFO. Proceeds always go to CFI.

---

## Q21 (Theory). What non-cash items, beyond depreciation, get adjusted in the indirect method? Name them and why.

**Model answer.** Add back: amortization of intangibles (non-cash, like depreciation); stock-based compensation (paid in equity, no cash); asset write-downs and impairments (non-cash charges); increases in deferred tax liabilities (expensed but not paid). Reverse: gains on asset sales (subtract — cash belongs in investing) and losses (add back). Adjust: all working-capital changes. The unifying principle — anything that hit net income but didn't move operating cash must be reversed, and anything that moved operating cash but bypassed net income must be added.

---

## Q22 (Numerical). Full tie-out stress test. A company reports CFO 80, CFI (110), CFF 45, beginning cash 60. What is ending cash, and what must the balance sheet cash line read?

**Worked answer.** Net change in cash = 80 − 110 + 45 = **15.** Ending cash = beginning 60 + 15 = **75.** The balance sheet's ending cash line *must* equal 75; if it doesn't, a balance sheet change was mis-signed or omitted. This is the mandatory final check on every cash flow statement — the reconciliation *is* the proof of correctness.
