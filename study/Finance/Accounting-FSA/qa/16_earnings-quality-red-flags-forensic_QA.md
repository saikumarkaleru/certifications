# Q&A — Earnings Quality, Red Flags & Forensic Accounting

A practice bank mixing conceptual questions (with model answers and interview phrasing) and fully-solved numerical problems. Every number is self-verified and reconciles.

---

## Part A — Conceptual / theory

### Q1. What does "earnings quality" mean, and what are its two dimensions?

**Model answer.** Earnings quality is the degree to which reported profit reflects *sustainable, cash-backed* economic performance rather than one-off items or accounting discretion. Two dimensions: **sustainability** (will this profit recur next year, or is it a windfall like an asset-sale gain or reserve release?) and **cash conversion** (is it backed by operating cash flow, or does it live only in accruals management controls?). High quality = persistent + cash-backed. Low quality = one-off and/or non-cash.

**How to say it in an interview.** "Quality isn't *how much* they earned — it's *how real and repeatable* it is. I test two things: does it recur, and is it backed by cash. If profit is up but it came from a reserve release and cash flow fell, it's low quality and I discount it."

---

### Q2. "Net income is an opinion; cash is a fact." Explain and say why it matters forensically.

**Model answer.** Net income depends on hundreds of estimates — bad-debt allowances, depreciation lives, capitalize-vs-expense choices, provisions, revenue-recognition timing. Each is a judgment with a defensible range, so honest people can produce different numbers and dishonest people can produce convenient ones. Cash collection, by contrast, either happened or didn't — far harder to fake in the short run. Forensically, that makes the cash flow statement the anchor: when profit and cash diverge and stay diverged, the gap is accruals management controls, and that's where distortion hides.

**Interview line.** "Profit is built on estimates; cash mostly isn't. So when profit and cash tell different stories, I trust the cash and go hunting for the accrual that explains the gap."

---

### Q3. What is the accrual ratio, and why does a high ratio predict weak future returns?

**Model answer.** The accrual ratio isolates the non-cash portion of earnings. Cash-flow version: (NI − (CFO+CFI)) / average NOA. Balance-sheet version: ΔNOA / average NOA. A high ratio means net operating assets — receivables, inventory, capitalized costs — grew fast relative to the business, i.e. earnings are increasingly accrual-driven. Sloan's accrual anomaly (1996): the accrual component is *less persistent* than the cash component because accruals mean-revert (receivables get written off, capitalized costs get depreciated), but the market prices all earnings dollars equally. So high-accrual firms are over-valued and subsequently underperform — historically ~10%/year for the top-vs-bottom decile.

**Interview line.** "High accruals mean profit is outrunning cash and piling into balance-sheet items that will reverse. The market is slow to see it, so high-accrual firms tend to underperform — that's the accrual anomaly."

---

### Q4. Distinguish channel stuffing from premature revenue recognition and from fictitious revenue.

**Model answer.**
- **Channel stuffing:** shipping *real* product to distributors beyond what they can sell, often with return rights or extended terms, to pull future sales into the current period. Revenue and receivables spike now; returns/write-offs hit later. (Sunbeam, Bristol-Myers.)
- **Premature recognition:** booking a real sale *before* control has genuinely transferred — before delivery/acceptance, or with a return right so large that control hasn't passed. (Bill-and-hold abuses.)
- **Fictitious revenue:** pure fabrication — fake customers, fake invoices, no goods at all. (Satyam, Wirecard, Luckin.)

All three inflate revenue and, except fictitious-cash cases, inflate receivables — so DSO rising is the common tell.

**Interview line.** "Channel stuffing is too much *real* product too early; premature is booking a real deal before it's earned; fictitious is making it up. First two show up as ballooning receivables and rising DSO; the last one usually needs the notes and the auditor."

---

### Q5. How does capitalizing operating costs flatter earnings, and what's the one metric that sees through it?

**Model answer.** Capitalizing moves an outlay from the income statement (immediate expense) to the balance sheet (an asset expensed slowly via depreciation). Current expense falls, so profit rises. But the cash still left the business — it's merely relabeled from operating expense to capex. So CFO rises, capex rises, and **free cash flow (CFO − capex) is unchanged.** FCF is the metric that sees through it. WorldCom did exactly this with line costs.

**Interview line.** "It boosts profit and even CFO, but not free cash flow, because the cash still went out as capex. And it just defers the expense into future depreciation — borrowing profit from tomorrow."

---

### Q6. What is a cookie-jar reserve? Where does it sit on the legal-to-fraud spectrum?

**Model answer.** Over-providing in a good year (booking an unnecessarily large reserve/provision) to create a cushion released into income in a bad year — a non-cash way to smooth earnings. The tell: earnings smoother than cash flow, and reserve balances swinging inversely to profitability. On the spectrum: conservative estimation is legitimate; *deliberately* over- or under-stating reserves to hit targets is earnings management, and if material and intentional it's securities fraud. The SEC has prosecuted exactly this.

**Interview line.** "Save profit in fat years, release it in lean years to smooth EPS. Legal estimation shades into fraud once it's a deliberate device to hit numbers — and the tell is earnings that are smoother than the cash."

---

### Q7. Pick three famous frauds and give the scheme plus the ratio that flagged each.

**Model answer.**
- **Enron:** off-balance-sheet SPEs hiding debt + mark-to-market gains on speculative deals + round-trip trades. Tell: CFO far below reported profit; huge off-BS obligations; opaque related-party entities.
- **WorldCom:** capitalized ~$11bn of line-cost operating expenses as capex. Tell: capex vs depreciation and capex/sales spiking while the industry was contracting.
- **Satyam:** fabricated ~₹5,040 crore of cash and fake revenue/interest. Tell: enormous "cash" earning implausibly little interest; margins too high for an IT-services peer set.

**Interview line.** Deliver one crisply — scheme → statement → ratio — to show you connect the accounting to the evidence.

---

### Q8. Why is inventory build a *leading* indicator of earnings-quality problems?

**Model answer.** Inventory rising faster than sales (rising DIO / falling turnover) means one of two bad things: demand is softening (product isn't selling, so obsolescence and write-downs loom), or COGS is being under-costed — more cost parked in inventory on the balance sheet instead of expensed — which inflates current margin. Either way it's an early warning, often *before* receivables reveal a demand problem, because the goods pile up before the desperate sell-through (which then shows as channel stuffing and rising DSO).

**Interview line.** "Inventory outrunning sales is an early red flag — either demand is weakening or they're stuffing cost into inventory to lift margin. It usually shows up before the receivables story does."

---

### Q9. Give five items on your red-flag checklist you'd run before any deep dive.

**Model answer.** (1) Cash conversion CFO/NI below one and falling. (2) DSO rising / receivables growing faster than revenue. (3) Capex persistently above depreciation with no growth story. (4) Margins improving against the industry or far above peers with no moat. (5) Reserve/provision balances swinging inversely to profitability, or recurring "one-time" charges. Governance overlays: auditor/CFO turnover, restatements, related-party deals, SPEs, heavy non-GAAP reliance.

**Interview line.** "Cash conversion, DSO, capex-vs-depreciation, margins-vs-peers, and reserve swings — five fast screens. Anything anomalous, I go to the notes."

---

### Q10. Is all earnings management fraud? How do you draw the line in practice?

**Model answer.** No. Accrual accounting *requires* estimates, and choosing conservatively or aggressively within GAAP is legal earnings management. Fraud requires **intent to misrepresent** and usually a departure from GAAP or fabrication. The practical line: is the choice a defensible estimate given the facts, or is it engineered specifically to hit a target and does it misstate economic reality? Reserves timed to earnings targets, revenue booked before control transfers, and expenses capitalized against the standard cross into fraud when material and intentional.

**Interview line.** "Estimation is legal; deception is fraud. The question is whether the number reflects the economics or was reverse-engineered to hit a target."

---

### Q11. What is the Beneish M-Score and how would you use it?

**Model answer.** An eight-variable statistical model (Beneish, 1999) estimating the probability that a firm has manipulated earnings. Key inputs: DSRI (days-sales-in-receivables index — revenue-recognition stress), GMI (gross-margin index — deteriorating margins as a manipulation motive), AQI (asset-quality index — capitalizing/soft assets), SGI (sales-growth index — growth pressure), and TATA (total accruals to total assets). A score above roughly **−1.78** flags a likely manipulator. Use it as a screen across a universe, then confirm bottom-up in the notes. Famously, Cornell students used it to flag Enron before collapse.

**Interview line.** "It's a manipulation-probability screen from eight accounting ratios — receivables, margins, asset quality, growth, accruals. Above about −1.78 is a red flag. I'd screen with it, then convict with the disclosures."

---

## Part B — Numerical problems

### Q12. Cash conversion and accrual diagnosis

**Problem.** A company reports:

| Item | Amount |
|---|---|
| Net income | 500 |
| Depreciation & amortization | 120 |
| Increase in accounts receivable | 260 |
| Increase in inventory | 140 |
| Increase in accounts payable | 60 |

(a) Compute CFO (indirect method). (b) Compute the cash conversion ratio. (c) Compute accruals (NI − CFO). (d) Comment on quality.

**Solution.**
```
(a) CFO = NI + D&A − ΔAR − ΔInv + ΔAP
        = 500 + 120 − 260 − 140 + 60
        = 280

(b) Cash conversion = CFO / NI = 280 / 500 = 0.56

(c) Accruals = NI − CFO = 500 − 280 = 220

(d) Quality ratio 0.56 (well below 1). Of $500 profit, only
    $280 is cash; $220 (44%) is accrual — dominated by a $260
    receivables build and $140 inventory build. Revenue is being
    booked well ahead of collection and product is piling up.
    LOW quality; investigate revenue recognition and demand.
```
*Self-check:* 500 + 120 = 620; − 260 = 360; − 140 = 220; + 60 = 280 ✓. Accruals 220 = 500 − 280 ✓.

---

### Q13. Accrual ratio (balance-sheet method)

**Problem.** Net operating assets: beginning 1,600, ending 2,300. Net income 400. Compute the balance-sheet accrual ratio and interpret.

**Solution.**
```
ΔNOA = 2,300 − 1,600 = 700
Average NOA = (2,300 + 1,600) / 2 = 1,950
Accrual ratio = 700 / 1,950 = 35.9%
```
**Interpretation.** ~36% is very high (low-to-mid single digits is normal). NOA grew nearly 44% (700/1,600) while — if revenue grew far less — the balance sheet is absorbing profit that hasn't become cash. Accruals of ~$700 exceed reported net income of $400, meaning the business consumed more cash into operating assets than it earned. Low earnings quality; likely reversal ahead.

*Self-check:* 700/1,950 = 0.359 ✓; 700/1,600 = 43.75% growth ✓.

---

### Q14. Capitalizing opex — three-statement impact

**Problem.** A firm spends $200 cash on costs that *should* be expensed but capitalizes $150 of it (depreciated over 5 years, straight-line), expensing only $50. Tax rate 25%. Show, versus honest accounting, the effect on: pre-tax profit, net income, CFO, capex, and free cash flow, in year 1. Assume revenue 1,000 and all other expenses 600.

**Solution.**
```
HONEST:
  Pre-tax = 1,000 − 600 − 200 = 200
  Tax (25%) = 50 ;  Net income = 150
  CFO (start from NI, add back D&A=0, cash costs already in NI) :
      NI 150 + D&A 0 = 150  (the full 200 opex reduced NI/cash)
  Capex = 0
  FCF = 150 − 0 = 150

AGGRESSIVE (capitalize 150, expense 50, depr = 150/5 = 30):
  Pre-tax = 1,000 − 600 − 50 − 30 = 320
  Tax (25%) = 80 ;  Net income = 240
  CFO: NI 240 + D&A 30 = 270  (only 50 of cash cost is in NI;
       the 150 cash outflow was moved to investing)
  Capex = 150
  FCF = 270 − 150 = 120

DELTAS (aggressive − honest):
  Pre-tax:  +120   (=150 deferred − 30 depreciation)
  Net income: +90  (=120 × (1−0.25))
  CFO:      +120   (270 − 150)
  Capex:    +150
  FCF:      −30    (120 − 150)  ... see note
```
**Note / reconciliation.** Reported profit jumps +$90 and CFO jumps +$120, yet FCF *falls* $30 — because the aggressive firm pays $30 *more* cash tax (80 vs 50) on its inflated profit while the operating cash saving is exactly offset by the capex. This is the crucial forensic point: **capitalizing does not create free cash — it can even destroy it via higher cash taxes — while making profit and CFO look better.**

*Self-check:* Honest pre-tax 200, tax 50, NI 150 ✓. Aggressive pre-tax 320, tax 80, NI 240 ✓. Pre-tax delta 120 = 150 − 30 ✓. NI delta 90 = 120 × 0.75 ✓. FCF: honest 150, aggressive 120, delta −30 = −(extra tax 30) ✓.

---

### Q15. Channel stuffing — DSO reveals the pull-forward

**Problem.** Q3 revenue 800, Q4 revenue 1,200. Accounts receivable: end-Q3 400, end-Q4 900. Using days = quarter revenue × 90 / average... use simple DSO = AR / quarterly revenue × 90. Compute DSO each quarter and interpret.

**Solution.**
```
DSO Q3 = 400 / 800 × 90 = 45.0 days
DSO Q4 = 900 / 1,200 × 90 = 67.5 days     → +22.5 days

Revenue growth Q3→Q4 = 1,200/800 − 1 = +50%
Receivables growth   = 900/400 − 1   = +125%
```
**Interpretation.** Receivables grew 125% while revenue grew 50% — collections badly lagging sales, DSO up 22.5 days. The Q4 revenue surge is not converting to cash; it's sitting in receivables. Consistent with **channel stuffing** — product pushed to distributors (with generous terms) to book the sale before quarter-end. Expect Q1 next year to show weak revenue and possible returns/write-offs as the channel de-stocks. Flag Q4 earnings as low quality.

*Self-check:* 400/800×90 = 45 ✓; 900/1,200×90 = 67.5 ✓; receivables 900/400 = 2.25 → +125% ✓.

---

### Q16. Cookie-jar reserve — smoothing and its unwind

**Problem.** Real pre-tax profits: Year 1 = 260, Year 2 = 80. Management targets a smooth reported 170 each year using a warranty reserve. (a) What reserve action each year? (b) Show reported profit and reserve balance. (c) Write the journal entries. (d) What happens if Year 3 real profit is 60 and the jar is empty?

**Solution.**
```
(a) Year 1: real 260, target 170 → over-provide 90 (build jar).
    Year 2: real 80, target 170 → release 90 (raid jar).

(b)
  | Year | Real | Reserve action | Reported | Reserve balance |
  |------|------|----------------|----------|-----------------|
  | 1    | 260  | +90 build      | 170      | 90              |
  | 2    | 80   | −90 release    | 170      | 0               |

(c) Year 1:  Dr Warranty expense (P&L)      90
                Cr Warranty provision (BS)      90
    Year 2:  Dr Warranty provision (BS)     90
                Cr Warranty expense/other (P&L) 90

(d) Year 3 real = 60, jar = 0. No reserve to release, so reported = 60.
    Reported EPS drops from a smooth 170 to 60 — a 65% cliff —
    even though real profit only fell from 80 to 60. The market,
    conditioned to expect ~170, is blindsided. Cookie-jar firms
    blow up the first year they run out of reserve.
```
**Reconciliation.** Two-year real total = 260 + 80 = 340; reported total = 170 + 170 = 340 ✓ (smoothing is timing, not magnitude). Debits = credits in both entries ✓. Reserve builds +90 then releases −90, ending 0 ✓.

---

### Q17. Quality-of-earnings comparison across two firms

**Problem.** Same industry, same reported net income of 300 each:

| | Firm X | Firm Y |
|---|---|---|
| Net income | 300 | 300 |
| CFO | 330 | 150 |
| Gain on asset sale (in NI) | 0 | 90 |
| Reserve release (in NI) | 0 | 40 |
| DSO | 42 days | 71 days |

Rank the two on earnings quality with numbers.

**Solution.**
```
Cash conversion:
  X: 330/300 = 1.10   (cash-backed, > 1)
  Y: 150/300 = 0.50   (half is non-cash)

"Core" recurring earnings (strip one-offs):
  X: 300 − 0 − 0 = 300
  Y: 300 − 90 (asset-sale gain) − 40 (reserve release) = 170

DSO: X 42 (stable) vs Y 71 (elevated — recognition/collection risk)
```
**Conclusion.** Firm X earns $300 that is fully cash-backed and recurring; on a normalized, cash basis it may be worth *more* than its $300 headline. Firm Y's $300 is only $170 of recurring core earnings, half-covered by cash, with a stretched DSO signalling further receivables risk. **X is high quality; Y is low quality.** Two identical headline numbers, opposite realities — value X on ~$300 sustainable, Y on ~$150–170.

*Self-check:* X 330/300 = 1.10 ✓; Y 150/300 = 0.50 ✓; Y core 300 − 90 − 40 = 170 ✓.

---

### Q18. Under-reserving to boost income

**Problem.** Receivables grew from 1,000 to 1,800. The allowance for doubtful accounts went from 100 (10% of AR) to 90 (5% of AR). (a) What allowance would holding 10% imply? (b) By how much did under-reserving boost pre-tax income? (c) Interpret.

**Solution.**
```
(a) 10% of 1,800 = 180 required allowance to hold the ratio.
(b) Actual allowance = 90. Shortfall = 180 − 90 = 90.
    Bad-debt expense = ΔAllowance + write-offs. Holding 10% needed
    the allowance to rise 100 → 180 = +80 expense. Instead it fell
    100 → 90 = −10 (a release). 
    Income boost vs the 10% policy = 80 − (−10) = 90 pre-tax.
(c) While receivables (and thus credit risk) grew 80%, the company
    CUT its allowance both absolutely (100 → 90) and as a % (10% →
    5%). That under-provisioning flattered pre-tax profit by ~90.
    Classic income-boosting via reserve manipulation — and it
    stores up future write-offs. Red flag.
```
*Self-check:* Required at 10% = 180; actual 90; gap 90 ✓. Expense under old policy would be +80 (100→180); actual was −10 (100→90); swing 90 ✓.

---

### Q19. Free cash flow as the acid test

**Problem.** Two years for one firm:

| | Year 1 | Year 2 |
|---|---|---|
| Net income | 200 | 280 |
| CFO | 210 | 300 |
| Capex | 90 | 210 |
| Depreciation | 85 | 95 |

Profit grew 40% and CFO grew 43% — looks great. Test it with FCF and capex/depreciation.

**Solution.**
```
FCF = CFO − Capex:
  Year 1: 210 − 90  = 120
  Year 2: 300 − 210 = 90       → FCF FELL 25% despite profit +40%

Capex / Depreciation:
  Year 1: 90 / 85  = 1.06   (roughly maintenance level)
  Year 2: 210 / 95 = 2.21   (capex more than 2x depreciation)
```
**Interpretation.** Profit and CFO both rose, but **free cash flow fell** because capex more than doubled and now runs 2.2x depreciation. If there's no genuine expansion story, this pattern is consistent with **capitalizing operating costs** — inflating profit and CFO while the cash still leaks out as "capex," leaving FCF weaker. The headline growth is lower quality than it looks. Investigate what's in that capex line.

*Self-check:* FCF 120 → 90 = −25% ✓; capex/depr 90/85 = 1.06, 210/95 = 2.21 ✓; profit 200→280 = +40% ✓.

---

### Q20. Round-trip / gross-vs-net revenue

**Problem.** An online marketplace facilitates $500 of goods sold by third parties, keeping a 10% commission. It also does a "round-trip" arrangement swapping $200 of services with a peer at cost (no margin). It currently reports revenue = 500 + 200 = 700. What should revenue be, and what's the quality issue?

**Solution.**
```
Agent (marketplace) revenue should be NET commission, not gross GMV:
  Correct revenue from marketplace = 10% × 500 = 50   (not 500)

Round-trip swap has no economic substance (no margin, circular):
  Correct revenue from swap = 0

Correct total revenue = 50 + 0 = 50   (vs 700 reported)
Overstatement = 700 − 50 = 650  (13x inflation)
```
**Interpretation.** Two abuses: (1) **gross-up** — an agent booking the full $500 GMV instead of its $50 net fee (ASC 606 principal-vs-agent test turns on who controls the good before transfer); (2) **round-tripping** — reciprocal deals inflating the top line with zero real profit. Revenue is overstated ~14x. Profit dollars are unaffected by the gross-up (only revenue and matching cost inflate), but the growth story and multiple are fake. Major red flag; dot-com and energy-trading frauds lived here.

*Self-check:* Net fee 500×10% = 50 ✓; swap 0 ✓; correct total 50; reported 700; overstated 650 ✓.

---

### Q21. Beneish-style receivables index (DSRI)

**Problem.** Year t−1: revenue 2,000, receivables 250. Year t: revenue 2,400, receivables 480. Compute the days-sales-in-receivables index (DSRI) and interpret.

**Solution.**
```
Days receivables t−1 = 250 / 2,000 = 0.125 (as fraction of a year)
Days receivables t   = 480 / 2,400 = 0.200
DSRI = (Recv_t / Sales_t) / (Recv_{t−1} / Sales_{t−1})
     = 0.200 / 0.125 = 1.60
```
**Interpretation.** DSRI = 1.60 means days-sales-in-receivables jumped 60% year over year. A DSRI meaningfully above 1 is one of the strongest Beneish signals of revenue-recognition manipulation — receivables are ballooning relative to sales, consistent with premature recognition or channel stuffing. Revenue grew 20% but receivables grew 92% (480/250 − 1). Feeds a higher (worse) M-Score; investigate.

*Self-check:* 250/2,000 = 0.125 ✓; 480/2,400 = 0.20 ✓; 0.20/0.125 = 1.60 ✓; receivables 480/250 = 1.92 → +92% ✓.

---

### Q22. Putting it together — full red-flag scorecard

**Problem.** Score this company (all trends year over year):

| Signal | Value |
|---|---|
| CFO / Net income | 0.62 |
| DSO | 44 → 68 days |
| DIO (inventory days) | 55 → 82 days |
| Capex / Depreciation | 2.4x |
| Allowance for doubtful accts (% of AR) | 8% → 4% |
| Reserve balance vs profit | released in a down year |
| "One-time" restructuring charges | 4th consecutive year |

Give a verdict and the interview-ready summary.

**Solution / verdict.**
```
Every one of the seven flags points the wrong way:
  1. CFO/NI 0.62  → profit not cash-backed
  2. DSO 44→68    → revenue outrunning collections (recognition risk)
  3. DIO 55→82    → inventory build; demand soft / margin stuffing
  4. Capex 2.4x depr → likely capitalizing opex
  5. Allowance halved as AR presumably grew → under-reserving to boost income
  6. Reserve released in a down year → cookie-jar smoothing
  7. "One-time" for 4 straight years → recurring costs mislabeled
Verdict: multi-front earnings management. VERY low quality.
```
**Interview-ready summary.** "This fails every screen at once. Cash conversion is 0.62, DSO and DIO are both blowing out, capex is 2.4x depreciation, they cut the bad-debt allowance while receivables grew, released a reserve in a weak year, and have booked 'one-time' charges four years running. Individually any one is a yellow flag; together it's a company managing earnings on multiple fronts. I'd normalize earnings down toward cash flow, expect write-offs and a margin reversal, and treat it as a short candidate pending a read of the notes and auditor history."

*Self-check:* all seven signals independently defined above map to the five levers (revenue, capitalize, cookie-jar, under-reserve, classification) ✓.

---

**End of Q&A bank — 22 questions (11 conceptual, 11 numerical), all figures self-verified and reconciling.**
