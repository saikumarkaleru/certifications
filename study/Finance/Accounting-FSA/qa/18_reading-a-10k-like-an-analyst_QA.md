# Q&A — Reading a 10-K / Annual Report Like an Analyst

A practice bank mixing conceptual questions (with model answers and interview phrasing) and fully solved numerical problems. Every number is self-verified and reconciles.

---

## Section A — Conceptual / theory

### Q1. In what order should an analyst read a 10-K, and why?

**Model answer.** Back-to-front, roughly. Start with (1) the **auditor's report** — opinion type, going-concern paragraph, and Critical Audit Matters — because it tells you whether the numbers are trustworthy and where the accounting is most fragile. Then (2) the **cash-flow statement**, reconciling net income to operating cash flow. Then (3) the **notes** — significant accounting policies, revenue recognition, receivables, debt, leases. Then (4) the **MD&A**, read adversarially against the numbers. The **press-release adjusted figures** you trust least.

**How to say it in an interview.** *"I read the mandatory disclosures to check the voluntary narrative. Auditor report and cash flow first, notes second, MD&A last, adjusted numbers never on their own."*

### Q2. Why are the notes more valuable than the face of the statements?

**Model answer.** The face of the statements is arithmetic; the notes reveal the *choices* behind that arithmetic — depreciation lives, inventory method, revenue-recognition timing, capitalization policy, lease and debt terms, tax positions. Two identical businesses can report very different profits by choosing differently, and the only place those choices are visible is the notes. That is where accounting becomes interpretation, which is where the analyst adds value.

**Interview line.** *"The income statement tells me what they earned; the notes tell me how they decided to measure it."*

### Q3. What is the single best test of earnings quality?

**Model answer.** Whether earnings convert to cash — compare net income to operating cash flow over multiple years. Earnings can be engineered through accruals (receivables, inventory, contract assets, capitalized costs); operating cash flow is far harder to fake for long. A persistent gap where net income exceeds operating cash flow signals low-quality, accrual-heavy earnings. A useful metric is the accruals ratio: (Net income − CFO) / average total assets — the higher it is, the lower the quality.

### Q4. What is a Critical Audit Matter (CAM) / Key Audit Matter (KAM), and why do analysts care?

**Model answer.** A CAM (US, PCAOB) or KAM (international, ISA 701) is an area the auditor found especially challenging, subjective, or judgment-intensive — commonly revenue recognition, goodwill impairment, or hard-to-value assets. It is the auditor publicly pointing at where the accounting is most fragile and where a misstatement is most likely. Analysts treat it as a map of where to concentrate scrutiny.

### Q5. Rank the four auditor opinions by concern, and explain the going-concern paragraph.

**Model answer.** Least to most worrying: **Unqualified/clean** (fairly stated) → **Qualified "except for"** (one contained issue — isolate and quantify) → **Adverse** (statements as a whole don't present fairly — can't rely) → **Disclaimer** (auditor couldn't form any opinion, usually a scope limitation — worst). Separately, a **going-concern paragraph** means the auditor has substantial doubt the company survives the next 12 months — a major flag that can appear even with an otherwise clean opinion.

### Q6. How can two identical companies legally report different net income?

**Model answer.** Through accounting choices within GAAP/IFRS: longer vs shorter depreciation lives, FIFO vs LIFO (US) in an inflationary environment, capitalizing vs expensing R&D/software/interest, and point-in-time vs over-time revenue recognition. Aggressive choices pull income into the present and push expense into the future — boosting this year's EPS at the expense of next year's. Cash flow is largely immune to these choices, which is why cross-checking earnings against cash normalizes across them.

### Q7. Name five earnings-quality red flags that are *divergences*.

**Model answer.**
1. Net income up while operating cash flow is flat or down.
2. Receivables (DSO) rising faster than sales.
3. Inventory (DIO) rising faster than sales.
4. GAAP-to-adjusted gap widening over time.
5. Effective tax rate falling (e.g., valuation-allowance release) while pre-tax profit is flat.
Each is two things that should move together diverging — far stronger evidence than any single ratio in isolation.

### Q8. Where does off-balance-sheet leverage hide, and how do you surface it?

**Model answer.** In the lease note (variable and short-term leases still partly off-balance-sheet even after ASC 842 / IFRS 16), commitments and contingencies (purchase/take-or-pay commitments, guarantees), and pension disclosures (deficits). You surface it by capitalizing lease liabilities and pension deficits into net debt and recomputing leverage on an EBITDAR basis — often revealing true leverage well above the reported figure.

### Q9. How should an analyst treat non-GAAP "adjusted" add-backs?

**Model answer.** Skeptically and item by item. **Reject** stock-based compensation add-backs (a real recurring cost that dilutes shareholders) and "one-time" charges that recur (serial restructuring or acquisition costs). You may **accept** truly non-cash, non-recurring items and amortization of acquired intangibles for a *cash-EPS* view, but not for an economic-earnings view. Under SEC Reg G the company must reconcile non-GAAP to GAAP — read that reconciliation.

### Q10. What's the difference between the ICFR opinion and the financial-statement opinion in a US 10-K?

**Model answer.** They are two separate opinions. The financial-statement opinion says the numbers are fairly stated per GAAP. The **ICFR opinion** (SOX 404, Item 9A) says whether internal control over financial reporting is effective. A company can have clean financials but a **material weakness** in controls — meaning a reasonable possibility that a material misstatement wouldn't be prevented or detected. That doesn't prove the numbers are wrong, but it discounts their reliability and raises restatement risk.

### Q11. What in the MD&A do you read most carefully?

**Model answer.** The revenue bridge (price vs volume vs FX vs acquisitions — organic growth is the real signal), the margin bridge (what moved gross and operating margin), liquidity and capital resources (debt maturities, revolver headroom, covenant room, capex plans), and the "known trends and uncertainties" disclosure required by Reg S-K Item 303, where a softening order book or customer loss often hides in one careful sentence. I also compare this year's MD&A to last year's for dropped disclosures or redefined KPIs.

---

## Section B — Numerical problems

### Q12. Reconstruct operating cash flow and judge earnings quality.

**Given.** Net income 90; depreciation 55; receivables rose from 150 to 260; inventory rose from 100 to 170; payables rose from 90 to 100. Revenue 1,200; COGS 700.

**Solution.**
```
CFO = 90 + 55 − (260−150) − (170−100) + (100−90)
    = 90 + 55 − 110 − 70 + 10
    = −25
```
DSO = 260/1,200 × 365 = **79.1 days** (up from 150/1,000 × 365 = 54.8). DIO = 170/700 × 365 = **88.6 days** (up from 100/600 × 365 = 60.8).

**Verdict.** Net income +90 but CFO −25. Earnings did not convert to cash; a 24-day DSO jump and 28-day DIO jump absorbed all of it and more. **Low earnings quality** — challenge revenue recognition and collectability.

### Q13. Normalize "adjusted" earnings.

**Given.** GAAP net income 120. Company adds back: restructuring 40 (charged four years running), stock-based comp 60, "one-time" acquisition costs 25 (serial acquirer), amortization of acquired intangibles 30. Company "adjusted" net income = 275.

**Solution.**
- Restructuring 40 — recurring, **reject.**
- Stock comp 60 — real recurring dilutive cost, **reject.**
- Acquisition costs 25 — recur for a serial acquirer, **reject.**
- Amortization of acquired intangibles 30 — non-cash, **accept only for cash-EPS view.**

```
Analyst normalized (economic) NI = 120 + 30 = 150
```
Company's 275 is **83% above GAAP** and **83% above the defensible 150**. Reject roughly 125 of the 155 in add-backs.

### Q14. Off-balance-sheet lease leverage.

**Given.** Reported debt 400; cash 100; EBITDA 200; PV of lease liabilities (from note) 420; annual rent in EBITDA 60.

**Solution.**
```
Reported net debt / EBITDA = (400−100)/200 = 300/200 = 1.5x
Adjusted net debt = 400 + 420 − 100 = 720
Adjusted EBITDAR  = 200 + 60 = 260
Adjusted leverage = 720 / 260 = 2.77x
```
True economic leverage is **2.8x, not 1.5x** — nearly double. Against a 3.0x covenant, headroom is thin.

### Q15. Fixed-charge coverage with leases.

**Given.** (Continuing Q14) reported interest 25; rent 60; EBITDAR 260.

**Solution.**
```
Fixed-charge coverage = EBITDAR / (interest + rent)
                      = 260 / (25 + 60)
                      = 260 / 85
                      = 3.06x
```
Only ~3x coverage of fixed charges once leases are included — far tighter than an EBIT/interest figure that ignored rent would suggest.

### Q16. DSO channel-stuffing detection.

**Given.** Year 1: revenue 800, receivables 110. Year 2: revenue 880 (+10%), receivables 200 (+82%).

**Solution.**
```
DSO Y1 = 110/800 × 365 = 50.2 days
DSO Y2 = 200/880 × 365 = 83.0 days
```
Receivables grew 82% on 10% revenue growth; DSO jumped ~33 days. **Red flag** — revenue booked far ahead of cash, consistent with channel stuffing or aggressive recognition. Cross-check contract assets and the bad-debt allowance.

### Q17. Cash conversion cycle.

**Given.** DSO 79.1; DIO 88.6; payables 100, COGS 700.

**Solution.**
```
DPO = 100/700 × 365 = 52.1 days
CCC = DSO + DIO − DPO = 79.1 + 88.6 − 52.1 = 115.6 days
```
The company finances ~116 days of operations — cash is tied up nearly four months between paying suppliers and collecting from customers. Rising CCC signals a deteriorating working-capital position and pressure on liquidity.

### Q18. Depreciation-life accounting choice — quantify the EPS effect.

**Given.** Gross PP&E 1,000, no salvage, straight-line. Management extends useful life from 10 years to 12.5 years. Tax rate 25%, shares outstanding 100.

**Solution.**
```
Old depreciation = 1,000/10   = 100/yr
New depreciation = 1,000/12.5 = 80/yr
Pre-tax boost to profit = 100 − 80 = 20
After-tax boost = 20 × (1−0.25) = 15
EPS boost = 15 / 100 shares = 0.15 per share
```
Extending the life lifts net income 15 and EPS 0.15 with **zero change in cash flow or economic reality**. Interview point: a pure accounting choice, visible only in the PP&E note, flatters earnings — exactly why cash flow is the check.

### Q19. Accruals ratio.

**Given.** Net income 90; CFO −25; total assets beginning 900, ending 1,100.

**Solution.**
```
Average total assets = (900 + 1,100)/2 = 1,000
Accruals ratio = (NI − CFO) / avg assets = (90 − (−25)) / 1,000 = 115/1,000 = 11.5%
```
An 11.5% accruals ratio is high — a large share of reported profit is non-cash accrual. **Low earnings quality**, consistent with the CFO reconstruction in Q12.

### Q20. Effective vs cash tax gap.

**Given.** Pre-tax book income 160; book tax expense 40; cash taxes paid (per cash-flow statement) 8.

**Solution.**
```
Effective (book) tax rate = 40/160 = 25.0%
Cash tax rate             = 8/160  = 5.0%
```
A 20-point gap between book and cash tax, if sustained, means book earnings overstate the cash the business keeps — driven by deferred-tax timing differences or a valuation-allowance release. Watch the deferred-tax note; a rising DTL confirms the timing story, while a VA release would flatter the P&L unsustainably.

### Q21. Goodwill vs equity impairment-risk screen.

**Given.** Goodwill 600; total equity 750; the acquired segment's operating profit fell from 90 to 20 over two years; no impairment recorded.

**Solution.**
```
Goodwill / equity = 600/750 = 80%
```
Goodwill is 80% of equity, and the segment that generated it saw operating profit collapse 78% (90 → 20) with **no impairment taken**. A future impairment could wipe out most of book equity. **Red flag** — pressure-test the impairment note's assumptions (discount rate, growth) against the deteriorating segment performance.

### Q22. Contract-asset (unbilled revenue) growth test.

**Given.** Revenue grew 12% (1,000 → 1,120). Contract assets / unbilled receivables grew from 60 to 150.

**Solution.**
```
Revenue growth        = 1,120/1,000 − 1 = 12%
Contract-asset growth = 150/60 − 1       = 150%
```
Unbilled revenue grew 150% on 12% revenue growth. Revenue is being recognized far ahead of billing and cash collection — a classic over-time / percentage-of-completion aggressiveness signal. If revenue recognition is also flagged as a CAM, escalate to a deep dive on the contract accounting.
