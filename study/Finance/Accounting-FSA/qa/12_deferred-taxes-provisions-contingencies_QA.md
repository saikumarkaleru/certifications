# Q&A — Deferred Taxes, Provisions & Contingencies

A practice bank mixing conceptual questions (with model answers and interview phrasing) and fully-worked numerical problems. Numbers are self-verified: debits equal credits and lifetime totals reconcile to cash.

---

## Part A — Conceptual

### Q1. Why do book income and taxable income differ at all?

**Model answer.** Because they're prepared under two different rule-books for two different purposes. Book income follows GAAP/IFRS and uses full accrual accounting to measure economic performance. Taxable income follows the tax code, which distrusts subjective accrual judgment and hard-codes its own timing rules — often nearer cash-basis, often loaded with policy incentives like accelerated depreciation and loss carryforwards. Same economic events, recognized in different periods (temporary differences) or in only one book at all (permanent differences).

**Interview line:** "Two rule-books, two purposes — accounting measures performance, tax law collects revenue and steers behavior."

### Q2. Distinguish permanent from temporary differences and give the consequence of each.

**Model answer.** A **temporary difference** is recognized in both books but in different periods — it *reverses* over time and creates a DTA or DTL; it moves cash tax versus book tax but leaves the effective tax rate near statutory. A **permanent difference** hits one book and never the other — it never reverses, creates no deferred balance, and *permanently* shifts the effective tax rate. Depreciation-method differences are temporary; tax-exempt muni interest and non-deductible fines are permanent.

**Interview line:** "Temporary differences change the *timing*; permanent differences change the *rate*."

### Q3. Is a deferred tax liability a "real" liability? Defend both sides.

**Model answer.** Textbook yes: it's a present obligation from a past event (you took a tax break by depreciating fast) that will require a future cash outflow (higher tax later when the depreciation runs out) — the definition of a liability. The nuance: for a company with steadily *growing* capex, new timing differences keep replacing the old ones, so the aggregate depreciation-driven DTL may never actually reverse. That's why some credit and DCF analysts treat that portion as **quasi-equity** — a permanent, interest-free source of funding — rather than a near-term obligation.

**Interview line:** "It's a genuine liability at the item level, but at the portfolio level a growing DTL can behave like permanent capital."

### Q4. What is the valuation allowance and when is it used?

**Model answer.** Under US GAAP (ASC 740) you recognize a DTA in full, then set up a contra-asset **valuation allowance** to write it down if it's *more likely than not* (>50%) that some or all won't be realized against future taxable profit. IFRS (IAS 12) reaches the same place differently — it recognizes the DTA only to the extent realization is probable, no separate allowance account. A loss-making firm with a big NOL-driven DTA and no path to profit should carry little to no net DTA. When it turns profitable and *releases* the allowance, that's a one-time deferred tax benefit that can push the effective rate below — even negative versus — statutory.

**Interview line:** "A DTA is only worth what you can realize; the valuation allowance is the reality check."

### Q5. Provision vs contingent liability vs remote — draw the line.

**Model answer.** It's a probability gate on an uncertain future outflow. If a present obligation from a past event is **probable** and **reliably estimable**, you recognize a **provision** (a liability on the balance sheet). If it's only **possible**, or can't be measured reliably, you don't book it — you **disclose** a contingent liability in the notes. If it's **remote**, you do nothing. IFRS "probable" is >50%; US GAAP "probable" is a higher bar, roughly 70-80%.

**Interview line:** "Probable and estimable → provide; possible → disclose; remote → ignore."

### Q6. Provision vs reserve — why is confusing them a serious error?

**Model answer.** A provision is a **liability** — an obligation to an outside party, created by charging the P&L (an expense that reduces profit). A reserve is part of **equity** — an appropriation of the owners' own retained profits (general reserve) or a valuation surplus (revaluation reserve), carved out *after* net income. Confusing them puts a number on the wrong side of the balance sheet: it either overstates leverage (calling an equity earmark a liability) or misstates distributable profit.

**Interview line:** "Provision is money you owe someone else; reserve is money you've set aside for yourself."

### Q7. Only permanent differences move the effective tax rate — true or false, and why?

**Model answer.** True (along with rate changes and valuation-allowance changes). The effective rate is total tax *expense* over pre-tax income. Total tax expense already includes the deferred portion, so a pure timing difference — which just shifts tax between current and deferred — leaves total expense, and hence the ETR, near statutory. It's the **cash** tax rate (cash paid ÷ pre-tax income) that timing differences move. So "accelerated depreciation lowers the effective tax rate" is *wrong* — it lowers the cash rate.

### Q8. Walk through the three statements when a DTL increases by $10.

**Model answer.** IS: deferred tax expense +$10, so total tax +$10 and net income −$10. CFS: start from NI −$10, add back the $10 DTL increase as a non-cash item → cash from operations unchanged, cash flat (correct — no cash moved). BS: DTL +$10 on liabilities, retained earnings −$10 from lower NI, cash unchanged → it balances.

**Interview line:** "Cash is flat, RE down 10, DTL up 10 — the tax was expensed but not paid."

### Q9. What is a constructive obligation? Give the restructuring example.

**Model answer.** A constructive obligation isn't a legal contract — it arises when an established pattern of past practice or a specific public statement creates a valid expectation in others that the entity will act. For restructuring, IAS 37 requires a **detailed formal plan** *and* that it has been **announced or begun**, creating a valid expectation among those affected. Only then can a provision be booked — and only for direct exit costs, **not** future operating losses, staff retraining, or relocating continuing operations.

### Q10. Why can the same lawsuit be a booked liability under IFRS but only a footnote under US GAAP?

**Model answer.** The recognition threshold differs. IFRS recognizes a provision when an outflow is "probable," meaning *more likely than not* (>50%). US GAAP's "probable" under ASC 450 is a higher bar — "likely," roughly 70-80%. A lawsuit assessed at, say, 60% likely to lose crosses the IFRS line (provide) but not the US GAAP line (disclose only). The two frameworks also differ on ranges: IFRS accrues the **midpoint**, US GAAP the **minimum**.

### Q11. A company reports a negative effective tax rate this quarter. What are the likely causes?

**Model answer.** Most commonly the **release of a valuation allowance** — the company became profitable enough to use its NOLs, so it reverses the write-down against its DTA and books a large deferred tax benefit. Other causes: a favorable tax settlement, a big permanent benefit (e.g., tax credits exceeding current tax), or an enacted rate change revaluing deferred balances. All are typically **non-recurring**, so you'd normalize the rate back toward statutory for forecasting.

### Q12. Where does deferred tax sit in the cash flow statement, and why?

**Model answer.** In the operating section as a **non-cash adjustment**. Because tax *expense* includes a deferred portion that never touched cash, you reverse it: add back an increase in net DTL (expense not paid) and subtract a decrease. This bridges accrual net income to the cash actually generated. The genuinely paid amount is "cash taxes paid," often disclosed as a supplemental item.

---

## Part B — Numerical

### Q13. Basic DTL from accelerated depreciation.

**Problem.** Book pre-tax income is $600. Tax depreciation exceeds book depreciation by $120 this year. Rate 25%. Compute taxable income, current tax, deferred tax, total tax expense, net income, and both tax rates.

**Solution.**
- Taxable income = 600 − 120 = **480.**
- Current (cash) tax = 480 × 25% = **120.**
- Temporary difference $120 builds a DTL → deferred tax = 120 × 25% = **30.**
- Total tax expense = 120 + 30 = **150.**
- Net income = 600 − 150 = **450.**
- Effective rate = 150 / 600 = **25%.** Cash rate = 120 / 600 = **20%.**

**Entry:**
```
Dr Income tax expense   150
   Cr Income tax payable        120
   Cr Deferred tax liability     30
```
Debits = credits. The ETR stays at statutory 25% (timing difference); only the cash rate drops.

### Q14. Full three-year DTL build and reversal.

**Problem.** Equipment $600, Day 1 Year 1. Book depreciation straight-line over 3 years ($200/yr). Tax depreciation: $360 / $180 / $60. Income before depreciation $900/yr. Rate 25%. Show book vs taxable income, current tax, DTL balance, total tax expense, and net income for all three years.

**Solution.**

| | Yr 1 | Yr 2 | Yr 3 | Total |
|---|---|---|---|---|
| Income before dep | 900 | 900 | 900 | 2,700 |
| Book dep | 200 | 200 | 200 | 600 |
| **Book pre-tax income** | **700** | **700** | **700** | **2,100** |
| Tax dep | 360 | 180 | 60 | 600 |
| **Taxable income** | **540** | **720** | **840** | **2,100** |
| Current tax (25%) | 135 | 180 | 210 | 525 |
| Tax dep − book dep | +160 | −20 | −140 | 0 |
| Deferred tax (25%) | +40 | −5 | −35 | 0 |
| **Cumulative DTL** | **40** | **35** | **0** | |
| **Total tax expense** | **175** | **175** | **175** | **525** |
| **Net income** | **525** | **525** | **525** | **1,575** |

**Checks.** Lifetime depreciation ties ($600 both books). Lifetime taxable = lifetime book income = 2,100. Net income smooth at $525/yr, ETR = 175/700 = **25%** every year, even though cash tax rose from $135 to $210. DTL builds to $40 then fully reverses to $0. All internally consistent.

**Year 1 entry:**
```
Dr Income tax expense   175
   Cr Income tax payable        135
   Cr Deferred tax liability     40
```
**Year 3 entry:**
```
Dr Income tax expense   175
Dr Deferred tax liability  35
   Cr Income tax payable        210
```

### Q15. NOL carryforward with 80% cap.

**Problem.** Year 1 tax loss $600. Year 2 taxable income before NOL $500; Year 3 taxable income before NOL $400. Post-2017 rules: indefinite carryforward, offset up to 80% of a year's taxable income. Rate 25%. Assume the DTA is fully realizable (no valuation allowance). Compute the DTA at end of Year 1, NOL used and cash tax each of Years 2-3, and the remaining NOL.

**Solution.**
- End Year 1: gross DTA = 600 × 25% = **$150.** NOL carryforward balance = $600.
- **Year 2:** max usable = min(NOL $600, 80% × 500 = 400) = **$400.** Taxable after NOL = 500 − 400 = 100. Cash tax = 100 × 25% = **$25.** Remaining NOL = 600 − 400 = **$200.**
- **Year 3:** max usable = min(NOL $200, 80% × 400 = 320) = **$200.** Taxable after NOL = 400 − 200 = 200. Cash tax = 200 × 25% = **$50.** Remaining NOL = **$0.**
- DTA drawdown: $150 consumed across Years 2-3 ($100 then $50 of tax shield used). DTA end Year 2 = 150 − (400×25%)=150−100 = **$50**; end Year 3 = 50 − (200×25%) = **$0.**

**Check.** Total NOL used = 400 + 200 = 600 = original loss. DTA fully consumed. Consistent.

### Q16. Valuation allowance and its release.

**Problem.** Year 1 tax loss $800, rate 25%. At end of Year 1, management judges only $300 of the loss is more-likely-than-not realizable. Year 2: company earns taxable income (before NOL) of $1,000; the 80% cap applies; allowance is released. Show the Year-1 net tax line and the Year-2 effective tax rate. Assume book pre-tax income equals taxable income before NOL each year.

**Solution.**
- **Year 1.** Gross DTA = 800 × 25% = **$200.** Realizable portion = 300 × 25% = $75. Valuation allowance = 200 − 75 = **$125.** Net Year-1 tax line = $200 benefit − $125 allowance expense = **$75 net benefit** (negative tax expense, adds to NI).
- **Year 2.** NOL usable = min($800, 80% × 1,000 = 800) = **$800.** Taxable after NOL = 1,000 − 800 = 200. Current tax = 200 × 25% = **$50.** DTA of $200 now fully consumed → deferred tax **expense** $200. Allowance of $125 released → **benefit** $125. Total tax expense = 50 + 200 − 125 = **$125.** ETR = 125 / 1,000 = **12.5%.**

**Reading.** The 12.5% rate versus 25% statutory is entirely the one-time allowance release — normalize it out. Over both years, total tax = −75 (Yr1) + 125 (Yr2) = $50 = tax on lifetime net taxable income (1,000 − 800 loss = 200 × 25% = $50). Reconciles.

### Q17. Warranty provision, expected value, and DTA.

**Problem.** 20,000 units sold in Year 1. 5% expected to fail; average repair cost $30. Warranties deductible for tax only when paid. Rate 25%. In Year 2, actual claims paid $28,000. Compute the Year-1 provision and DTA, and the Year-2 entries.

**Solution.**
- **Year 1 provision** = 20,000 × 5% × $30 = **$30,000.**
```
Dr Warranty expense   30,000
   Cr Warranty provision   30,000
```
- Tax timing → DTA = 30,000 × 25% = **$7,500** (booked now for books, deductible only when paid).
```
Dr Deferred tax asset   7,500
   Cr Income tax expense (deferred benefit)   7,500
```
- **Year 2** actual claims $28,000:
```
Dr Warranty provision   28,000
   Cr Cash                     28,000
```
Remaining provision = 30,000 − 28,000 = **$2,000**; remaining DTA = 2,000 × 25% = **$500**. DTA reversed in Year 2 = 7,500 − 500 = **$7,000** (deferred tax expense as the $28,000 becomes deductible: 28,000 × 25% = $7,000).

**Check.** If the remaining $2,000 provision is later released, total warranty expense = 30,000 − 2,000 = $28,000 = cash actually spent. DTA nets to zero. Fully reconciles.

### Q18. Litigation — provision vs contingent, with a range.

**Problem.** A firm faces a lawsuit. Counsel says a loss is probable and estimates the outcome somewhere between $2m and $6m, with no single amount more likely. What does the firm record under (a) IFRS and (b) US GAAP?

**Solution.**
- **(a) IFRS (IAS 37):** loss is probable (>50%) and estimable → recognize a provision at the **best estimate**; with a continuous range and no single most-likely point, use the **midpoint** = (2 + 6)/2 = **$4m.**
```
Dr Litigation expense   4m
   Cr Litigation provision   4m
```
- **(b) US GAAP (ASC 450):** if probable and estimable but no amount in the range is better than any other, accrue the **minimum** = **$2m**, and disclose the range up to $6m.

**Point.** Same facts, $2m difference in the booked liability purely from framework mechanics — exactly the kind of comparability adjustment an analyst makes.

### Q19. Effective tax rate reconciliation.

**Problem.** Pre-tax book income $1,000. Statutory rate 21%. Permanent items: $80 of tax-exempt income; $40 of non-deductible fines. Tax credits $30. No timing effect on the rate. Compute taxable income for the permanent items, total tax expense, and the effective tax rate. Reconcile statutory to effective.

**Solution.**
- Adjust book income for permanent items to get the tax base effect: taxable-basis income = 1,000 − 80 (exempt) + 40 (non-deductible) = **$960.**
- Tax before credits = 960 × 21% = **$201.60.** Less credits $30 = total tax expense = **$171.60.**
- ETR = 171.60 / 1,000 = **17.16%.**

**Reconciliation:**
| Line | Amount | % of pre-tax |
|---|---|---|
| Tax at statutory 21% | 210.00 | 21.00% |
| Tax-exempt income (−80 × 21%) | −16.80 | −1.68% |
| Non-deductible fines (+40 × 21%) | +8.40 | +0.84% |
| Tax credits | −30.00 | −3.00% |
| **Total / effective** | **171.60** | **17.16%** |

**Check.** 21.00 − 1.68 + 0.84 − 3.00 = **17.16%.** Ties to the direct computation.

### Q20. Enacted rate change remeasuring deferred balances.

**Problem.** A company holds a net DTA of $200 measured at a 25% tax rate (i.e., underlying temporary differences of $800). The government enacts a rate cut to 20%, effective next year. What's the immediate P&L effect?

**Solution.**
- The DTA must be **remeasured** at the new 20% rate: 800 × 20% = **$160.**
- Write-down = 200 − 160 = **$40.**
```
Dr Income tax expense   40
   Cr Deferred tax asset   40
```
- Effect: a one-time **$40 charge**, reducing net income in the year of enactment — even though the rate *cut* is favorable long-term, a company holding net DTAs takes a hit because its future tax shields are now worth less.

**Point.** Symmetrically, a company holding a large net **DTL** would book a one-time **benefit** on a rate cut (its future tax owed shrinks). Rate direction and net-deferred-position direction together determine the sign.

### Q21. Deferred revenue creates a DTA.

**Problem.** A SaaS firm collects $120,000 cash upfront in Year 1 for a 3-year subscription. Tax law taxes it on receipt; books recognize $40,000/year as earned. Rate 25%. Show the Year-1 book vs tax revenue, and the resulting deferred tax balance.

**Solution.**
- **Year 1:** tax revenue = $120,000 (all taxed on receipt); book revenue = $40,000. Tax base of the deferred-revenue liability is $0 (already taxed); carrying value $80,000. Carrying value of a *liability* > tax base → **DTA.**
- Temporary difference = 120,000 − 40,000 = **$80,000.** DTA = 80,000 × 25% = **$20,000** (tax paid now, book revenue — and matching expense recognition — comes later).
```
Dr Deferred tax asset   20,000
   Cr Income tax expense (deferred benefit)   20,000
```
- **Years 2-3:** as each $40,000 is recognized for books (no further tax), the difference reverses $40,000/yr, drawing the DTA down $10,000/yr to $0 by end of Year 3.

**Check.** Lifetime book revenue $120,000 = lifetime tax revenue $120,000; DTA builds to $20,000 then fully reverses. Consistent.

### Q22. Distinguishing the two rates in a mini-DCF context.

**Problem.** EBIT $1,000, statutory rate 25%. Accelerated depreciation makes cash taxes only $180 this year while book tax expense is $250. For an unlevered free cash flow calculation, which tax figure matters, and what's the difference worth?

**Solution.**
- Book tax expense = 250 (ETR 25%); cash tax = 180 (cash rate 18%). The $70 gap = increase in DTL.
- Unlevered FCF wants **cash** taxes. Two equivalent routes: (a) tax EBIT at cash rate → 1,000 − 180 = **$820** after-tax; or (b) tax at book rate (1,000 − 250 = 750) then add back the $70 non-cash deferred tax increase → 750 + 70 = **$820.**
- Both give **$820** — the deferred tax add-back exactly bridges book to cash.

**Interview line:** "For unlevered FCF I use cash taxes; I either tax EBIT at the cash rate or tax at the book rate and add back the change in deferred taxes — same answer."

---

*End of Q&A bank. All numerical answers self-checked: journal entries balance, lifetime book and tax totals reconcile, and deferred balances build and reverse to zero over each item's life.*
