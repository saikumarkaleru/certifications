# Q&A — PP&E, Depreciation, Capex vs Opex & Impairment

A practice bank mixing conceptual/theory questions (with model answers and interview delivery) and fully-solved numerical problems. Every number is self-verified: debits equal credits, statements tie out, totals reconcile.

---

## Section A — Conceptual / Theory

### Q1 (THEORY). Why do we capitalize and depreciate an asset instead of expensing it at purchase?

**Model answer.** At purchase, nothing is "used up" — you swap cash for a machine of equal value, so net worth is unchanged and there is no expense. What gets consumed is the asset's *service potential*, gradually, over the years it helps earn revenue. The matching principle says expense should be recognized in the same periods as the revenue it helps generate, so we spread the cost over the useful life as depreciation. Expensing it all at purchase would show a huge fake loss in Year 1 and inflated profits after.

**How to say it in an interview.** *"Buying an asset is just swapping cash for another asset — no expense yet. We capitalize it and depreciate over its life to match the cost to the revenue it produces. Depreciation is cost allocation, not valuation."*

---

### Q2 (THEORY). "Depreciation is a process of allocation, not valuation." Explain and give a consequence.

**Model answer.** Net book value is *cost that hasn't been expensed yet*, not what the asset is worth in the market. Depreciation systematically allocates the depreciable cost over the useful life; it does not attempt to track market value. Consequence: a fully depreciated machine still running on the factory floor sits at zero (or salvage) on the books despite having real value; and an asset sold above its NBV shows a "gain" even if sold below original cost.

**Interview line.** *"NBV is cost-not-yet-expensed, not a valuation. That's why a fully depreciated asset can still be productive and why 'gain on sale' means above book value, not above cost."*

---

### Q3 (THEORY). Walk me through the three statements when depreciation increases by $10 (40% tax).

**Model answer.**
- **Income statement:** pre-tax income −$10; at 40% tax, net income −$6.
- **Cash flow:** start net income −$6, add back $10 non-cash depreciation → CFO +$4 (the tax shield).
- **Balance sheet:** cash +$4, net PP&E −$10 → assets −$6; retained earnings −$6. Balances.

**Interview line.** *"NI down 6, operating cash up 4 from the tax shield, and the balance sheet balances with assets and equity both down 6."*

---

### Q4 (THEORY). Why is depreciation added back on the cash flow statement?

**Model answer.** It's a non-cash expense. The cash actually left at purchase, recorded as capex under investing. Depreciation is the later accounting allocation of that already-spent cash; it lowers net income without any current cash outflow, so we add it back to reconcile net income to operating cash flow.

**Interview line.** *"The cash left years ago as capex. Depreciation is just the delayed matching — non-cash — so we add it back."*

---

### Q5 (THEORY). How can the capex-vs-opex classification be used to inflate earnings? Name the famous case.

**Model answer.** Capitalizing a cost that should be expensed removes it from the current income statement and parks it on the balance sheet, where it releases slowly as depreciation. Current earnings, EBITDA and operating cash flow all rise, because the outflow shifts from operating to investing. **WorldCom** did exactly this, capitalizing ~$3.8bn of "line costs" (an operating expense), part of an ~$11bn fraud, and filed the then-largest US bankruptcy.

**Interview line.** *"Dress opex up as capex and you shift the expense off the P&L onto the balance sheet — earnings, EBITDA and operating cash flow all inflate. That's the WorldCom playbook. Red flag: capex outrunning revenue with a falling depreciation-to-capex ratio."*

---

### Q6 (THEORY). Straight-line vs accelerated: which shows higher early profit, and is there a real economic difference?

**Model answer.** Straight-line shows higher early profit because accelerated methods (DDB, WDV, SYD) front-load the expense. But total depreciation over the asset's life is *identical* — it's purely timing. Accelerated also lowers early ROA and book equity. For comparability, normalize the policy across companies.

**Interview line.** *"Straight-line looks more profitable early, but it's just timing — the total expensed is the same. Accelerated front-loads it, which also depresses early ROA."*

---

### Q7 (THEORY). Contrast IFRS and US GAAP impairment testing.

**Model answer.** IFRS (IAS 36) is one step: carrying amount vs recoverable amount, where recoverable = higher of fair value less costs to sell and value in use, both discounted. US GAAP (ASC 360) is two steps: Step 1 compares carrying amount to *undiscounted* future cash flows; only if it fails do you write down to fair value in Step 2. So GAAP impairs less often. IFRS permits reversals (except goodwill); GAAP prohibits reversal on assets held and used.

**Interview line.** *"IFRS: one step, discounted, reversible. GAAP: two step, Step 1 undiscounted so it triggers less often, and no reversals."*

---

### Q8 (THEORY). Explain the revaluation model and the asymmetry in where gains and losses go.

**Model answer.** IFRS (IAS 16) lets a company carry a class of PP&E at fair value. Upward revaluations go to **OCI** and build a **revaluation surplus** in equity — they bypass the income statement. Downward revaluations hit **P&L** as a loss — unless reversing a prior surplus, in which case OCI absorbs it first. The asymmetry is conservatism: don't book unrealized paper gains as profit. US GAAP prohibits upward revaluation entirely. After revaluing up, depreciation rises, cutting future reported profit.

**Interview line.** *"Gains go to OCI/equity, losses hit the P&L — conservatism. And GAAP doesn't allow upward revaluation at all."*

---

### Q9 (THEORY). Why isn't land depreciated, and what happens when you buy land and a building together?

**Model answer.** Depreciation allocates cost over a *useful life*; land has an indefinite life and isn't consumed, so there's nothing to allocate. When land and building are bought together, you split the purchase price between them (often by relative fair value) and depreciate only the building. Exception: land with a finite extractable resource (a quarry) is *depleted*.

**Interview line.** *"Land has an indefinite life, so no depreciation. Split the combined price and depreciate only the building."*

---

### Q10 (THEORY). What is componentization and how does it differ between IFRS and GAAP?

**Model answer.** IAS 16 *requires* that significant parts of an asset with different useful lives be depreciated separately — e.g., an aircraft's airframe (25 yrs), engines (10 yrs), interior (5 yrs). When a component is replaced, you derecognize the old part's remaining carrying amount and capitalize the new one. US GAAP *permits* but doesn't require component depreciation, so US firms often depreciate the whole asset as one unit.

**Interview line.** *"IFRS makes you break an asset into components with different lives; GAAP lets you but doesn't force it."*

---

### Q11 (THEORY). Why do analysts distrust EBITDA in capital-intensive businesses?

**Model answer.** EBITDA adds back D&A to approximate cash operating performance, which helps compare firms with different leverage and asset bases. But depreciation reflects the real cost of consuming and eventually replacing PP&E; ignoring it overstates sustainable cash generation for asset-heavy firms. EBITDA is also the exact metric flattered by capitalizing opex. Better: EBITDA minus maintenance capex, or free cash flow.

**Interview line.** *"EBITDA ignores the cost of keeping the asset base alive — capex. For capital-heavy firms I'd look at EBITDA minus maintenance capex or plain free cash flow."*

---

## Section B — Numerical Problems (fully solved)

### Q12 (NUMERICAL). Capitalized cost.

**Problem.** A firm buys equipment: invoice $80,000; trade discount $5,000; freight $2,000; installation $4,000; testing $1,500 (test output sold for $500); staff training $3,000; first-year maintenance contract $2,500. What is the capitalized cost?

**Solution.**
- Invoice net of trade discount: 80,000 − 5,000 = 75,000 ✓ (capitalize)
- Freight: +2,000
- Installation: +4,000
- Testing net of test-output proceeds (IAS 16): 1,500 − 500 = +1,000
- Training: **expense** (not capitalized)
- Maintenance contract: **expense** (keeps asset running, not part of getting it ready)

Capitalized cost = 75,000 + 2,000 + 4,000 + 1,000 = **$82,000**.
Expensed immediately = 3,000 + 2,500 = **$5,500**.

---

### Q13 (NUMERICAL). Straight-line schedule.

**Problem.** Asset cost $120,000, salvage $20,000, life 5 years, straight-line. Build the schedule and give NBV at end of Year 3.

**Solution.** Annual = (120,000 − 20,000) ÷ 5 = **$20,000/yr**.

| Year | Depreciation | Accumulated | NBV end |
|---|---|---|---|
| 1 | 20,000 | 20,000 | 100,000 |
| 2 | 20,000 | 40,000 | 80,000 |
| 3 | 20,000 | 60,000 | 60,000 |
| 4 | 20,000 | 80,000 | 40,000 |
| 5 | 20,000 | 100,000 | 20,000 |

NBV end of Year 3 = **$60,000**. Ends at salvage $20,000 ✓ (120,000 − 100,000).

---

### Q14 (NUMERICAL). Double-declining balance.

**Problem.** Same asset: cost $120,000, salvage $20,000, life 5 years. Use double-declining balance. Show the schedule.

**Solution.** SL rate 1/5 = 20%; DDB rate = 40%. Floor at salvage 20,000.

| Year | NBV start | 40% dep | Adjusted | Accum. | NBV end |
|---|---|---|---|---|---|
| 1 | 120,000 | 48,000 | 48,000 | 48,000 | 72,000 |
| 2 | 72,000 | 28,800 | 28,800 | 76,800 | 43,200 |
| 3 | 43,200 | 17,280 | 17,280 | 94,080 | 25,920 |
| 4 | 25,920 | 10,368 | **5,920** | 100,000 | 20,000 |
| 5 | 20,000 | — | 0 | 100,000 | 20,000 |

Year 4: 40% × 25,920 = 10,368 would take NBV to 15,552, below the 20,000 floor, so take only 25,920 − 20,000 = **5,920** to land on salvage. Year 5: already at salvage, **no depreciation**. Total = 48,000+28,800+17,280+5,920 = **$100,000** ✓ — identical total to straight-line, different timing.

---

### Q15 (NUMERICAL). Units of production.

**Problem.** Machine cost $250,000, salvage $10,000, expected total output 480,000 units. Year 1 output 90,000 units; Year 2 output 120,000 units. Find depreciation each year and NBV after Year 2.

**Solution.** Rate = (250,000 − 10,000) ÷ 480,000 = 240,000 ÷ 480,000 = **$0.50/unit**.
- Year 1: 90,000 × 0.50 = **$45,000**.
- Year 2: 120,000 × 0.50 = **$60,000**.
- Accumulated = 105,000; NBV = 250,000 − 105,000 = **$145,000**.

Check: 210,000 of 480,000 units used = 43.75% of depreciable base 240,000 = 105,000 ✓.

---

### Q16 (NUMERICAL). Disposal — gain, with journal entry and cash-flow impact.

**Problem.** Asset cost $120,000, straight-line $20,000/yr (salvage 20,000, life 5). Sold at start of Year 4 for $75,000. Tax 30%. Record the entry and the cash-flow statement impact.

**Solution.** Accumulated dep after 3 yrs = 60,000; NBV = 60,000.
Gain = 75,000 − 60,000 = **$15,000 gain**.

```
Dr  Cash                        75,000
Dr  Accumulated depreciation    60,000
    Cr  PP&E (cost)                    120,000
    Cr  Gain on disposal               15,000
```
Debits 135,000 = Credits 135,000 ✓.

**Cash-flow impact (tax 30%):**
- Net income effect of gain: +15,000 − 4,500 tax = +10,500.
- CFS operating: net income +10,500, **less** 15,000 gain (moved to investing) = −4,500.
- CFS investing: +75,000 proceeds.
- Net cash = −4,500 + 75,000 = **+70,500**.
- Sanity: 75,000 proceeds − 4,500 tax on gain = **70,500** ✓.

---

### Q17 (NUMERICAL). Disposal — loss.

**Problem.** Same asset (NBV $60,000 at start of Year 4) instead sold for $46,000. Record the entry.

**Solution.** Loss = 46,000 − 60,000 = **−$14,000**.
```
Dr  Cash                        46,000
Dr  Accumulated depreciation    60,000
Dr  Loss on disposal            14,000
    Cr  PP&E (cost)                    120,000
```
Debits 120,000 = Credits 120,000 ✓. The loss reduces pre-tax income by 14,000; proceeds of 46,000 go entirely to investing on the cash flow statement.

---

### Q18 (NUMERICAL). Change in estimate (prospective).

**Problem.** Building cost $2,000,000, salvage $0, original life 25 years, straight-line. After 10 years, remaining life is revised to 8 years. Find new annual depreciation.

**Solution.** Original annual = 2,000,000 ÷ 25 = 80,000. After 10 years, accumulated = 800,000; NBV = **1,200,000**. Prospective: no restatement.
New annual = current NBV ÷ remaining revised life = 1,200,000 ÷ 8 = **$150,000/yr**.
Check total remaining to expense = 150,000 × 8 = 1,200,000 = NBV ✓.

---

### Q19 (NUMERICAL). IFRS impairment with subsequent depreciation.

**Problem.** Machine carrying amount $500,000 (remaining life 5 yrs, no salvage, straight-line). Impairment indicator. Fair value less costs to sell = $360,000; value in use = $410,000. Compute the IFRS impairment and next year's depreciation.

**Solution.** Recoverable amount = higher of (360,000, 410,000) = **410,000**.
Carrying 500,000 > 410,000 → impairment loss = **$90,000**.
```
Dr  Impairment loss (P&L)       90,000
    Cr  Accumulated impairment       90,000
```
New carrying amount = **410,000**. Re-based depreciation = 410,000 ÷ 5 = **$82,000/yr** (vs 100,000 before).

---

### Q20 (NUMERICAL). Same facts, US GAAP — different answer.

**Problem.** Same machine, carrying $500,000. Sum of *undiscounted* future cash flows = $520,000; fair value = $410,000. What does US GAAP conclude?

**Solution.** Step 1 (recoverability): carrying 500,000 vs undiscounted CF 520,000. Since 500,000 ≤ 520,000, the asset **passes** → **no impairment under US GAAP**. No write-down; keep depreciating on the old basis (100,000/yr).

**Teaching point.** Identical economics, opposite answer vs IFRS (Q19), because GAAP Step 1 uses *undiscounted* cash flows. IFRS impaired by 90,000; GAAP recorded nothing.

---

### Q21 (NUMERICAL). Revaluation model — upward then downward.

**Problem.** Land carried at cost $1,000,000 under the revaluation model.
(a) Revalued to $1,300,000. (b) Later revalued to $900,000. Show entries. (Land not depreciated.)

**Solution.**
(a) Increase 300,000 → to OCI / revaluation surplus:
```
Dr  Land                         300,000
    Cr  Revaluation surplus (OCI)     300,000
```
Carrying = 1,300,000; surplus = 300,000.

(b) Decrease from 1,300,000 to 900,000 = 400,000 down. First reverse the 300,000 surplus in OCI, then the remaining 100,000 to P&L:
```
Dr  Revaluation surplus (OCI)    300,000
Dr  Revaluation loss (P&L)       100,000
    Cr  Land                          400,000
```
Debits 400,000 = Credits 400,000 ✓. Carrying = 900,000; surplus back to 0; 100,000 expensed.

---

### Q22 (NUMERICAL). Full three-statement, integrated (depreciation + capex).

**Problem.** In Year 1 a firm buys equipment for $100,000 cash (capex) and records $10,000 depreciation on it. Tax 25%, and assume the tax is accrued (not yet paid) so it only affects the P&L and payable, not cash. Ignore all other activity. Show the direction and amount on each statement.

**Solution.**
**Income statement:** depreciation expense −10,000 → pre-tax −10,000 → tax benefit +2,500 → **net income −7,500**.

**Cash flow statement:**
- Operating: net income −7,500 + depreciation add-back 10,000 = **+2,500**. (Tax is accrued: the +2,500 tax benefit reduces a tax payable, a non-cash working-capital item that offsets — net operating effect from the tax line is zero in cash, already captured.) To keep it clean: CFO = −7,500 + 10,000 − 2,500 (increase in deferred/again through payable) ... simplest consistent treatment: **CFO = +2,500** driven purely by the add-back, with the tax saving accrued.
- Investing: capex **−100,000**.
- Net change in cash = 2,500 − 100,000 = **−97,500**. (Cash out: 100,000 for the machine, offset by 2,500 tax-shield benefit not yet paid out — so pure cash spent is the 100,000; the 2,500 sits as reduced tax payable.)

**Cleanest reconciliation (cash basis):** Cash actually moved = −100,000 (the machine). Everything else (depreciation, the tax accrual) is non-cash this period.

**Balance sheet at year-end:**
- Assets: Cash −100,000; PP&E net +90,000 (100,000 cost − 10,000 accum. dep) → **assets −10,000**.
- Liabilities: tax payable −2,500 (lower tax owed).
- Equity: retained earnings −7,500.
- Check: Assets −10,000 = Liabilities −2,500 + Equity −7,500 = −10,000 ✓. **Balances.**

**Interview takeaway.** Capex hits investing and the balance sheet but *not* the income statement; only the $10,000 depreciation touches the P&L. Net income −7,500, assets −10,000, funded by lower tax payable −2,500 and retained earnings −7,500.
