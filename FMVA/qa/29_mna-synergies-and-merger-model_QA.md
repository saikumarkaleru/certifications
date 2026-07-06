# Q&A — M&A Synergies and the Full Merger Model

A practice bank for FMVA Chapter 29. Work each build problem in Excel before reading the answer. Tax rate is 25% unless stated otherwise, and all earnings adjustments are tax-affected because they sit above the tax line.

---

## Section A — Concept Check

**A1. What single question does a merger model answer, and what makes a deal "accretive"?**
It answers whether the combined company's pro-forma EPS is higher or lower than the acquirer's standalone EPS. If pro-forma EPS is higher, the deal is accretive; if lower, dilutive. EPS is a fast screening proxy: underneath it, accretion happens when the earnings you buy (target NI plus synergies) exceed the cost of how you paid (interest incurred or given up, share dilution, and amortization).

**A2. Name the three engines that feed the pro-forma income statement.**
Sources and Uses (how much and paid how), Purchase Price Allocation (write-ups, DTL, goodwill), and Financing Effects (new interest and foregone interest). Synergies are layered on top. All feed the pro-forma income statement, which produces EPS.

**A3. Distinguish equity value from enterprise value in a deal, and state which one each of these uses: (a) share issuance, (b) the acquisition multiple.**
Equity value (offer price x diluted shares) is what common holders receive; it drives share issuance and P/E. Enterprise value (equity value + target net debt) drives the acquisition multiple (EV/EBITDA). Share issuance uses equity value; the acquisition multiple uses enterprise value.

**A4. Why do you subtract foregone interest income when a deal is funded with cash?**
The cash on hand was earning interest income. Spending it removes that income stream, so combined earnings fall by the after-tax foregone interest. Omitting it makes every cash deal look falsely accretive.

**A5. Is goodwill amortized through the income statement? What about the intangibles created in the PPA?**
Goodwill is not amortized for book purposes — it is tested for impairment and only hits EPS if impaired. The newly recognized identifiable intangibles (customer relationships, technology, trade names) ARE amortized over their useful life, and that amortization reduces pro-forma EPS.

**A6. Give the two quick financing heuristics for accretion and state what they ignore.**
All-debt: accretive if the target's earnings yield (NI ÷ purchase equity value) exceeds the after-tax cost of the new debt. All-stock: accretive if the acquirer's P/E exceeds the P/E it pays for the target. Both heuristics ignore PPA amortization and foregone interest/fees, so the full model is the arbiter.

**A7. Why do analysts trust cost synergies but haircut or exclude revenue synergies?**
Cost synergies (eliminating duplicate overhead, procurement scale, closing redundant facilities) are credible and modelable, usually phased in with one-time integration costs. Revenue synergies (cross-selling, pricing power) are soft because customers and salesforces rarely behave as promised, so base cases lean on cost synergies and push revenue synergies into an upside case with a heavy haircut.

**A8. What is a deferred tax liability in the PPA and why does it arise?**
When you write up assets to fair value for book purposes but the tax basis does not step up, a future book-vs-tax difference is created. The DTL = write-up amount x tax rate captures the future taxes owed as the difference reverses. It is added back in the goodwill bridge.

**A9. Write the one-equation summary of a merger model.**
Pro-Forma EPS = (Acquirer NI + Target NI + after-tax synergies − after-tax new interest − after-tax foregone interest − after-tax new amortization) ÷ (Acquirer diluted shares + new shares issued). Compare to standalone EPS; a higher result is accretive.

**A10. Why is a "cash EPS" figure (excluding acquired-intangible amortization) attractive to acquirers?**
Amortization of acquired intangibles is a non-cash GAAP charge that can flip a directionally-sound deal into reported dilution. Adding it back yields cash EPS, which is often accretive even when GAAP EPS is not — which is why acquirers prefer to quote it.

---

## Section B — Build / Computational Problems

Reproduce each in Excel. Blue for hard-coded inputs, black for formulas; add a Sources = Uses check driven to zero.

**B1. Offer price, equity value, enterprise value.**
Target unaffected price $35.00, control premium 40%, diluted shares 30m, target debt $250m, target cash $50m.
- Offer price = 35 × (1 + 0.40) = **$49.00**
- Offer equity value = 49 × 30 = **$1,470m**
- Target net debt = 250 − 50 = $200m
- Enterprise value = 1,470 + 200 = **$1,670m**

**B2. Sources and Uses (balancing plug).**
Total Uses = $1,470m equity purchase + $30m fees = $1,500m. Financing: 40% new debt of the $1,470m consideration, remainder cash on hand; fees paid from cash.
- New debt = 40% × 1,470 = **$588m**
- Cash used = Total Uses − New debt = 1,500 − 588 = **$912m**
- Check: Sources (588 + 912) = 1,500 = Uses. **Balances to zero.**

**B3. Purchase Price Allocation and goodwill.**
Equity purchase price $1,470m; target book equity $500m; PP&E write-up $150m; intangibles created $400m; target's existing goodwill $50m (written off); tax rate 25%.
- DTL = (150 + 400) × 25% = **$137.5m**
- Goodwill = Equity price − Book equity − Write-ups + DTL + old goodwill written off
- = 1,470 − 500 − (150 + 400) + 137.5 + 50 = **$607.5m**

Top-down check: 1,470 − 500 = 970 excess; −550 write-ups = 420; +137.5 DTL = 557.5; +50 old goodwill = **607.5m**. Matches.

**B4. Financing and amortization adjustments (using B2's mix).**
New debt $588m at 7%; cash used $912m earning 3%; intangibles $400m over 8-year life.
- New interest expense = 588 × 7% = **$41.16m** (pre-tax)
- Foregone interest income = 912 × 3% = **$27.36m** (pre-tax)
- New intangible amortization = 400 ÷ 8 = **$50m/yr** (pre-tax)

**B5. Full pro-forma income statement and EPS — Year 2 (synergies fully phased in).**
Acquirer NI $500m, 200m diluted shares (standalone EPS $2.50). Target NI $120m. Cost synergies $60m pre-tax fully in by Year 2. Use B4 adjustments but with cash used = $882m (60% cash / 40% debt on the $1,470m, fees ignored for this clean version), so foregone interest = 882 × 3% = $26.46m.

| Line | $m |
|---|---|
| Acquirer NI | 500.0 |
| + Target NI | 120.0 |
| + After-tax synergies (60 × 0.75) | 45.0 |
| − After-tax new interest (41.16 × 0.75) | (30.87) |
| − After-tax foregone interest (26.46 × 0.75) | (19.845) |
| − After-tax amortization (50 × 0.75) | (37.50) |
| **Pro-forma NI** | **576.785** |

- Pro-forma EPS = 576.785 ÷ 200 = **$2.884**
- Accretion = 2.884 / 2.50 − 1 = **+15.4% accretive.**

**B6. Same deal — Year 1 (synergies 50% phased in).**
After-tax synergies = 30 × 0.75 = $22.5m (half of Year 2).
- Pro-forma NI = 500 + 120 + 22.5 − 30.87 − 19.845 − 37.5 = **$554.285m**
- EPS = 554.285 ÷ 200 = **$2.771**; accretion = **+10.9%.**

**B7. Breakeven synergies for Year 1.**
Standalone EPS $2.50 requires pro-forma NI of 200 × 2.50 = $500m. Pro-forma NI with zero synergies = 500 + 120 − 30.87 − 19.845 − 37.5 = **$531.785m** — already above $500m. So the deal accretes on financing alone; breakeven after-tax synergy = 500 − 531.785 = −$31.785m, i.e., pre-tax = −31.785 ÷ 0.75 = **−$42.4m**. Interpretation: the deal could absorb up to about $42m of pre-tax dis-synergies (or extra costs) before turning dilutive.

**B8. All-stock variant (P/E rule check).**
Acquirer NI $300m, 100m shares (EPS $3.00), share price $60. Target NI $80m, offer equity value $1,300m all in stock. Intangibles $300m over 10 years ($30m/yr). No debt, no cash used.
- New shares = 1,300 ÷ 60 = **21.67m**; pro-forma shares = **121.67m**
- Pro-forma NI = 300 + 80 − (30 × 0.75) = **$357.5m**
- EPS = 357.5 ÷ 121.67 = **$2.938**; accretion = **−2.1% dilutive.**
- P/E rule: acquirer P/E = 60 / 3.00 = 20.0×; P/E paid = 1,300 / 80 = 16.25×. Rule says accretive (20 > 16.25), but the $22.5m after-tax amortization tips GAAP EPS to dilution — confirming the heuristic ignores PPA.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through a merger model in five steps."**
First, set the offer: unaffected price times (1 + premium) gives offer price; times diluted shares gives equity value; add target net debt for enterprise value. Second, build Sources and Uses — total the uses (buy equity, refinance debt, fees) and fund them with new debt, cash, and/or stock so sources equal uses. Third, run the PPA: write up assets to fair value, book a DTL on the write-ups, and plug goodwill. Fourth, assemble the pro-forma income statement — add the two companies, add after-tax synergies, subtract after-tax new interest, foregone interest, and new intangible amortization, then tax the result. Fifth, divide pro-forma NI by pro-forma shares (old plus any newly issued) to get EPS, and compare to standalone EPS for accretion or dilution.

**C2. "A deal passes the P/E rule but the model shows dilution. Why?"**
The P/E rule ignores two real charges. First, purchase-price-allocation amortization: the intangibles you recognize amortize through the income statement as a GAAP expense that the heuristic never sees. Second, foregone interest and transaction/financing fees. Either can turn a directionally accretive swap into reported dilution — which is exactly why the full model is trusted over the shortcut, and why acquirers often quote cash EPS that adds the amortization back.

**C3. "All else equal, will an all-cash deal or an all-stock deal be more accretive, and why?"**
Usually all-cash (especially cash from cheap debt). Issuing stock increases the share-count denominator without adding proportionate earnings, so it dilutes unless the acquirer's P/E comfortably exceeds the P/E it pays. Cheap debt adds earnings to the numerator at an after-tax cost often below the target's earnings yield, so it accretes. The swing factor either way is synergies.

**C4. "How do you treat target debt — assumed or refinanced?"**
Decide once and be consistent. If refinanced, the repayment appears in Uses and the target's old interest expense disappears from the pro-forma. If assumed (rolled), you keep the target's existing interest and do not fund a repayment. The classic error is doing both — funding a repayment while still carrying the old interest — which double-counts.

**C5. "Your CEO wants to know the breakeven premium. What is it and how do you show it?"**
The breakeven premium is the offer premium at which accretion turns to dilution — pro-forma EPS exactly equals standalone EPS. I solve for it by flexing the premium input until accretion hits zero (goal-seek), and present it inside a sensitivity Data Table of accretion % against premium and % stock consideration, the two variables the board actually debates. It tells the CEO how much room exists before the deal destroys near-term EPS.

**C6. "Why tax-affect synergies and interest but not goodwill?"**
Synergies, new interest, foregone interest, and intangible amortization all sit above the tax line, so their effect on net income is the pre-tax amount times (1 − tax rate). Goodwill is not an income-statement item at all under current book rules — it is only tested for impairment — so there is nothing to tax-affect unless it is impaired.

---

## Section D — Common-Error Spotting

Each snippet contains one mistake. Identify and correct it.

**D1.** "It's an all-cash deal, so there is no interest adjustment and no dilution — pure accretion from the target's $80m NI."
Error: forgetting foregone interest on the cash spent. The cash was earning interest income; spending it reduces combined earnings by the after-tax foregone interest. Cash deals are not free.

**D2.** "Goodwill of $600m amortized over 15 years reduces pro-forma NI by $40m pre-tax per year."
Error: goodwill is not amortized for book EPS. Only the identifiable intangibles created in the PPA amortize. Amortizing goodwill understates earnings.

**D3.** "New interest = $588m × 7% = $41.16m; I subtracted the full $41.16m from net income."
Error: not tax-affecting. Interest sits above the tax line, so the hit to net income is 41.16 × (1 − 0.25) = **$30.87m**.

**D4.** "We refinanced the target's $250m of debt (shown in Uses) and kept its $15m of interest expense in the pro-forma."
Error: double-counting target debt. If the debt is refinanced/repaid, its old interest disappears. Keep the interest only if the debt is assumed (rolled), not repaid.

**D5.** "New shares = $1,300m consideration ÷ acquirer's target-implied price... I used the target's $52 offer price."
Error: new shares issued = stock consideration ÷ the acquirer's share price (or exchange ratio × target shares), not the target's price. Using the wrong price mis-sizes dilution.

**D6.** "P/E paid = enterprise value $1,500m ÷ target NI $80m = 18.75×."
Error: confusing enterprise and equity value. P/E uses equity value (1,300 ÷ 80 = 16.25×). Enterprise value is for EV/EBITDA. Mixing them corrupts both the premium and the multiple.

**D7.** "Base-case accretion of +12% relies on $50m of revenue synergies from cross-selling."
Error: over-relying on revenue synergies in the base case. They are soft and should be haircut or moved to an upside case; base-case accretion should rest on credible cost synergies.

**D8.** "Sources total $1,460m, Uses $1,500m — close enough, I'll proceed to the balance sheet."
Error: Sources must equal Uses exactly. A $40m gap flows into a broken balance sheet downstream. Build the check cell first and drive it to zero before continuing.

**D9.** "I used basic shares (100m acquirer, 25m target) throughout the model."
Error: always use diluted share counts (treasury-stock method) for both companies; basic shares understate the denominator and overstate EPS.

---

*Self-verification note:* B1–B8 were recomputed independently; Year 2 pro-forma NI reconciles to $576.785m and EPS $2.884 (+15.4%), and the all-stock case to $2.938 (−2.1%), matching the chapter's checkpoints.
