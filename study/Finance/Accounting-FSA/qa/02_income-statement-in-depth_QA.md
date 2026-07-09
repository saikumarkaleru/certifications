# Q&A — The Income Statement in Depth

A mixed practice bank: conceptual/theory questions (with model answers and interview delivery) and fully solved numerical problems. Every number is self-verified and reconciles. Work each problem before reading the solution.

---

## Section A — Conceptual / Theory

### Q1. Why is the income statement built on accrual accounting rather than cash accounting?

**Model answer.** Accrual accounting recognizes revenue when it is *earned* (control of goods/services transfers to the customer) and expenses when they are *incurred* to generate that revenue — the matching principle — regardless of when cash moves. This gives a faithful picture of a *period's* economic activity and makes periods comparable. Cash accounting would distort performance whenever cash timing differs from activity (upfront payments, credit sales, long projects). The trade-off is that net income diverges from cash flow, which is precisely why we also need the cash flow statement.

**How to say it in an interview.** "Accrual matches revenue to the period it's earned and costs to the revenue they generate, so profit reflects the period's real economics, not cash timing. That's the whole point — comparability — and it's also why net income isn't cash."

---

### Q2. Distinguish operating vs. non-operating and recurring vs. non-recurring. Why keep them separate?

**Model answer.** They are two independent axes. *Operating vs. non-operating* asks whether an item comes from the core business (revenue, COGS, SG&A are operating; interest, asset-sale gains, FX are non-operating) — this split determines EBIT and drives operating valuation multiples. *Recurring vs. non-recurring* asks whether an item will repeat (normal sales are recurring; restructuring, impairments, litigation gains are not) — this split drives *normalized* earnings and quality-of-earnings analysis. An item can be operating but non-recurring (a restructuring charge) or non-operating but recurring (steady interest income), so you must apply both lenses.

**Interview line.** "Operating vs. non-operating feeds EBIT and valuation; recurring vs. non-recurring feeds normalized earnings. They're orthogonal — a restructuring charge is operating but one-off; interest income is non-operating but recurring."

---

### Q3. What exactly is the difference between operating income and EBIT?

**Model answer.** Operating income is a defined subtotal: revenue minus operating expenses. EBIT — earnings before interest and taxes — is derived as pre-tax income plus interest expense (or net income + interest + taxes). They are equal only when there is no non-operating income. If the company earns interest income or books a gain on an asset sale (both below operating income but above interest expense), EBIT exceeds operating income by that non-operating amount.

**Interview line.** "Same number only when there's no non-operating income. EBIT includes items like interest income and asset-sale gains that sit below the operating line, so EBIT is usually operating income plus non-operating income."

---

### Q4. Explain EBITDA. Why do analysts use it and why is it dangerous?

**Model answer.** EBITDA = EBIT + depreciation + amortization. It removes non-cash D&A and, being before interest and taxes, is neutral to capital structure and tax regime — handy for comparing companies and as a rough operating-cash proxy (the basis of EV/EBITDA). It is dangerous because it is *non-GAAP* (no standard definition, so "adjusted EBITDA" varies), it ignores capex and working-capital needs, and it pretends the wear-and-tear that D&A represents is free. For capital-intensive businesses it flatters weak economics.

**Interview line.** "EBITDA is a capital-structure-neutral cash proxy and a good screen, but it ignores capex and treats D&A as if it weren't a real cost — so I cross-check with EBIT and free cash flow, especially for capital-heavy firms."

---

### Q5. Walk through basic vs. diluted EPS and the anti-dilution rule.

**Model answer.** Basic EPS = (net income − preferred dividends) / weighted-average common shares. We subtract preferred dividends (not available to common) and use weighted-average shares because shares issued mid-year only earned part of the year. Diluted EPS assumes all *dilutive* potential shares convert: options/warrants via the treasury stock method (assume exercise, buy back shares with proceeds at average market price, net the difference into the denominator); convertibles via if-converted (add conversion shares to the denominator and add back after-tax interest or preferred dividends to the numerator). The anti-dilution rule: include a security only if it *lowers* EPS; if it would raise EPS it is anti-dilutive and excluded, so diluted EPS is always ≤ basic.

**Interview line.** "Basic is net income less preferred over weighted-average shares. Diluted layers in dilutive options via treasury stock and convertibles via if-converted, with the numerator add-back for convertibles. Diluted can never beat basic — anti-dilutive securities are dropped."

---

### Q6. What is OCI, what goes in it, and what is 'recycling'?

**Model answer.** Other comprehensive income holds specific unrealized gains and losses that standard-setters keep out of net income to avoid whipsawing reported performance: foreign-currency translation of foreign subsidiaries (IAS 21), mark-to-market on FVOCI debt/equity securities (IFRS 9), the effective portion of cash-flow hedges (IFRS 9), pension remeasurements/actuarial gains and losses (IAS 19), and PP&E revaluation surplus (IAS 16, IFRS only). Comprehensive income = net income + OCI, and OCI accumulates on the balance sheet as AOCI within equity. *Recycling* (reclassification) is moving an OCI item into net income when it's realized — e.g., when an FVOCI debt security is sold or a hedged transaction hits the P&L. Some items never recycle: pension remeasurements and PP&E revaluation surplus stay in equity permanently.

**Interview line.** "OCI parks volatile unrealized items — translation, FVOCI marks, hedge effectiveness, pension remeasurements — outside net income to keep the earnings signal stable. Some recycle into net income when realized; pension remeasurements and revaluation surplus never do."

---

### Q7. Single-step vs. multi-step income statement — which and why?

**Model answer.** Single-step groups all revenues and all expenses and subtracts once, showing only net income — simple, common for small/private firms, but it hides the useful subtotals. Multi-step builds the waterfall — gross profit, operating income, pre-tax income — and separates operating from non-operating. Analysts and public companies use multi-step because gross margin and operating margin are essential to understanding *where* profit is made and lost.

**Interview line.** "Multi-step, every time, for analysis — single-step hides gross profit and operating income, which is exactly where the story is."

---

### Q8. A company's net income rose but the stock fell. Give three plausible reasons.

**Model answer.** (1) *Low-quality beat* — the increase came from a one-time gain, a lower tax rate, or an accounting change rather than growing operating income, so recurring earning power didn't improve. (2) *Margin deterioration masked by volume* — revenue and net income grew but gross/operating margins compressed, signalling pricing or cost pressure. (3) *Guidance/forward-looking miss* — reported earnings beat but management guided future quarters down, or a key segment or bookings metric weakened. Markets price the future and the *durability* of earnings, not last period's headline.

**Interview line.** "Because quality and the forward look matter more than the headline. If the beat was a one-off, or margins compressed, or guidance was cut, the market discounts a higher net income number."

---

### Q9. How are discontinued operations and non-controlling interest presented, and why?

**Model answer.** Discontinued operations — the results of a major business line or geography being sold or shut — are stripped out of continuing operations and shown as a single line, *net of tax*, below net income from continuing operations (IFRS 5 / ASC 205-20). This keeps continuing operations clean and comparable across periods. Non-controlling interest arises in consolidation: the parent's P&L includes 100% of a partly-owned subsidiary's results, so consolidated net income is split into "attributable to parent" and "attributable to NCI." EPS is always computed on the *parent* portion.

**Interview line.** "Discontinued ops sit below the line, net of tax, to keep continuing operations comparable. NCI carves out the minority owners' slice of consolidated profit, and EPS uses only the parent share."

---

### Q10. Why can a highly profitable company still run out of cash?

**Model answer.** Because net income is accrual-based and includes non-cash revenue (credit sales creating receivables) while excluding real cash outflows. Rapid growth ties up cash in receivables and inventory (rising working capital); heavy capex consumes cash that never appears as an expense in one period (it's capitalized and depreciated over years); debt principal repayments aren't on the income statement at all. So reported profit can be strong while operating and financing cash flows are deeply negative. This is the classic "profitable but insolvent" growth-company trap.

**Interview line.** "Profit is accrual; cash isn't. Fast growth soaks cash into receivables, inventory, and capex, and debt repayments never touch the P&L — so you can be profitable and still short of cash."

---

## Section B — Numerical Problems

### Q11. Build the multi-step income statement and all margins.

**Facts (₹ crore):** Gross sales 8,000; returns and discounts 300; COGS 4,600; SG&A 1,200; R&D 300; depreciation 400; interest expense 250; interest income 60; tax rate 25%.

**Solution.**
- Net revenue = 8,000 − 300 = **7,700**.
- Gross profit = 7,700 − 4,600 = **3,100**. Gross margin = 3,100 / 7,700 = **40.26%**.
- Operating income = 3,100 − 1,200 − 300 − 400 = **1,200**. Operating margin = 1,200 / 7,700 = **15.58%**.
- EBITDA = 1,200 + 400 = **1,600**. EBITDA margin = 1,600 / 7,700 = **20.78%**.
- Pre-tax income = 1,200 + 60 (interest income) − 250 (interest expense) = **1,010**.
- Tax = 1,010 × 25% = **252.5**. Net income = 1,010 − 252.5 = **757.5**. Net margin = 757.5 / 7,700 = **9.84%**.
- Check EBIT (before interest & taxes) = pre-tax 1,010 + interest expense 250 = 1,260 = operating income 1,200 + interest income 60. Ties. ✓

---

### Q12. Basic EPS with a mid-year share issuance (weighted average).

**Facts:** Net income ₹360 crore; preferred dividends ₹30 crore. Shares outstanding: 80 crore for the first 9 months, then a new issue took it to 100 crore for the final 3 months.

**Solution.**
- Weighted-average shares = 80 × (9/12) + 100 × (3/12) = 60 + 25 = **85 crore**.
- Numerator = 360 − 30 = **330**.
- Basic EPS = 330 / 85 = **₹3.882 ≈ ₹3.88**.
- Sanity: using ending shares (100) would give 3.30 and using opening (80) would give 4.125; the weighted answer ₹3.88 sits correctly between them. ✓

---

### Q13. Diluted EPS — treasury stock method for options.

**Facts:** Net income ₹450 crore; no preferred. Weighted-average shares 120 crore. Options on 20 crore shares, strike ₹30, average market price ₹50.

**Solution.**
- Basic EPS = 450 / 120 = **₹3.75**.
- Options in-the-money (50 > 30) → dilutive.
- Proceeds = 20 × 30 = 600. Shares bought back = 600 / 50 = 12. Net new shares = 20 − 12 = **8 crore**.
- Diluted shares = 120 + 8 = 128. Numerator unchanged (options have no numerator effect).
- Diluted EPS = 450 / 128 = **₹3.516 ≈ ₹3.52**.
- Check: diluted ₹3.52 < basic ₹3.75. ✓

---

### Q14. Diluted EPS — if-converted for a convertible bond, with dilution test.

**Facts:** Net income ₹600 crore; preferred dividends ₹0. Weighted-average shares 150 crore. Convertible bond: ₹500 crore face, 10% coupon (interest ₹50 crore/yr), convertible into 25 crore shares. Tax rate 30%.

**Solution.**
- Basic EPS = 600 / 150 = **₹4.00**.
- After-tax interest add-back = 50 × (1 − 0.30) = **35**.
- Incremental EPS of the bond = 35 / 25 = ₹1.40. Since ₹1.40 < basic ₹4.00 → **dilutive**, include.
- Diluted numerator = 600 + 35 = 635. Diluted denominator = 150 + 25 = 175.
- Diluted EPS = 635 / 175 = **₹3.6286 ≈ ₹3.63**.
- Check: ₹3.63 < ₹4.00. ✓

---

### Q15. Anti-dilution — show why an out-of-the-money convertible is excluded.

**Facts:** Net income ₹200 crore; weighted-average shares 40 crore. Convertible preferred paying ₹36 crore dividend, convertible into 6 crore shares.

**Solution.**
- Basic EPS = (200 − 36) / 40 = 164 / 40 = **₹4.10**.
- If-converted test: add back preferred dividend ₹36 to numerator, add 6 crore shares to denominator.
- Incremental EPS = 36 / 6 = ₹6.00. Since ₹6.00 > basic ₹4.10, converting would *raise* EPS → **anti-dilutive**, exclude it.
- Diluted EPS = basic EPS = **₹4.10** (the security is excluded).
- Proof it would be wrong to include: (164 + 36) / (40 + 6) = 200 / 46 = ₹4.348 > ₹4.10 — including it inflates EPS, which is not allowed. ✓

---

### Q16. Normalized (quality-of-earnings) net income.

**Facts (₹ crore):** Reported pre-tax income 900, which *includes* a one-off ₹120 gain on sale of land and a one-off ₹200 restructuring charge. Tax rate 25%.

**Solution.**
- Remove the one-offs from pre-tax: normalized pre-tax = 900 − 120 (gain out) + 200 (charge back) = **980**.
- Reported net income = 900 × (1 − 0.25) = **675**.
- Normalized net income = 980 × (1 − 0.25) = **735**.
- Interpretation: durable earning power (₹735) is *higher* than reported (₹675) because the restructuring charge outweighed the land gain. Value off ₹735. ✓

---

### Q17. Effective tax rate reconciliation.

**Facts (₹ crore):** Pre-tax income 1,000. Statutory rate 30%. The company had ₹80 of tax-exempt income (permanent difference) and ₹40 of non-deductible expenses (permanent difference). Ignore deferred-tax timing.

**Solution.**
- Taxable income = pre-tax 1,000 − 80 (exempt) + 40 (non-deductible) = **960**.
- Current tax = 960 × 30% = **288**.
- Net income = 1,000 − 288 = **712**.
- Effective tax rate = 288 / 1,000 = **28.8%**, below the 30% statutory rate — the tax-exempt income (a bigger permanent benefit than the non-deductible cost) pulls the effective rate down.
- Reconciliation check: statutory 30% × 1,000 = 300; less exempt benefit 80 × 30% = 24; plus non-deductible cost 40 × 30% = 12; 300 − 24 + 12 = 288. ✓

---

### Q18. Comprehensive income build-up.

**Facts (₹ crore):** Net income 500. OCI items for the year: foreign-currency translation gain 60; unrealized loss on FVOCI debt securities 25; cash-flow hedge gain (effective) 15; pension actuarial loss 40.

**Solution.**
- Net OCI = 60 − 25 + 15 − 40 = **10**.
- Comprehensive income = net income + OCI = 500 + 10 = **510**.
- Note for the analyst: of the OCI items, translation, FVOCI, and hedge gains/losses will *recycle* into net income when realized; the pension actuarial loss will *not* recycle and stays in AOCI. So AOCI rises ₹10 net this year. ✓

---

### Q19. Depreciation change flowing through the three statements (numerical).

**Facts:** A company increases depreciation by ₹200 crore. Tax rate 25%. Show the effect on net income, cash from operations, and the balance sheet.

**Solution.**
- Income statement: pre-tax income falls ₹200; tax falls 200 × 25% = 50; **net income falls ₹150**.
- Cash flow (indirect): start from net income −150, add back non-cash depreciation +200 → **cash from operations rises ₹50** (the depreciation tax shield = 200 × 25%).
- Balance sheet: PP&E −200 (accumulated depreciation), cash +50, so total assets −150; retained earnings −150. Assets −150 = equity −150. **Balances.** ✓

---

### Q20. Full statement with non-operating items, discontinued ops, and NCI.

**Facts (₹ crore):** Operating income 700; interest expense 90; interest income 30; gain on investment sale 50 (one-off); tax rate 25%. Below the line: discontinued operations loss ₹60 (pre-tax). The company owns 80% of a subsidiary; total consolidated net income needs a 20% NCI carve-out, and the NCI's share of net income is ₹48 crore.

**Solution.**
- Pre-tax income (continuing) = 700 + 30 + 50 − 90 = **690**.
- Tax on continuing = 690 × 25% = 172.5. Net income continuing = 690 − 172.5 = **517.5**.
- Discontinued ops, net of tax = −60 × (1 − 0.25) = **−45**.
- Total net income = 517.5 − 45 = **472.5**.
- Attributable to NCI = **48** (given). Attributable to parent = 472.5 − 48 = **424.5**.
- Interview note: EPS would be computed on the parent's ₹424.5, not the consolidated ₹472.5. Normalized continuing net income would also strip the ₹50 one-off gain: (690 − 50) × 0.75 = 480 pre-NCI. ✓

---

### Q21. Gross margin vs. operating margin divergence — diagnose.

**Facts:** Year 1 → revenue 1,000, COGS 600, operating expenses 250. Year 2 → revenue 1,200, COGS 660, operating expenses 400.

**Solution.**
- Year 1: gross profit = 400 (gross margin 40.0%); operating income = 150 (operating margin 15.0%).
- Year 2: gross profit = 540 (gross margin 45.0%); operating income = 140 (operating margin 11.67%).
- Diagnosis: **gross margin improved (40% → 45%)** — better product economics or pricing — but **operating margin fell (15% → 11.67%)** because operating expenses jumped from 25% to 33.3% of revenue. The product got more profitable, but overhead (SG&A/R&D) grew faster than sales, eroding operating profit. An analyst flags the OpEx bloat as the issue to probe. ✓

---

### Q22. Reconstruct revenue from a change in receivables and cash collected (accrual vs. cash).

**Facts (₹ crore):** Cash collected from customers during the year = 4,500. Accounts receivable rose from 600 (opening) to 800 (closing). Assume all sales are on credit and no write-offs.

**Solution.**
- Revenue (accrual) = cash collected + increase in receivables = 4,500 + (800 − 600) = **4,700**.
- Logic: revenue = cash collected + ending AR − beginning AR = 4,500 + 800 − 600 = 4,700. The ₹200 rise in receivables is revenue earned but not yet collected — exactly the accrual-vs-cash gap.
- Cross-check (AR roll-forward): opening AR 600 + revenue 4,700 − collections 4,500 = closing AR 800. ✓

---

## One-line answer key (numericals)

| Q | Answer |
|---|---|
| Q11 | GP 3,100 (40.26%); OI 1,200 (15.58%); EBITDA 1,600 (20.78%); NI 757.5 (9.84%) |
| Q12 | WA shares 85; Basic EPS ₹3.88 |
| Q13 | Net new shares 8; Diluted EPS ₹3.52 |
| Q14 | Add-back 35; Diluted EPS ₹3.63 |
| Q15 | Anti-dilutive; Diluted = Basic = ₹4.10 |
| Q16 | Reported NI 675; Normalized NI 735 |
| Q17 | Current tax 288; Effective rate 28.8% |
| Q18 | Net OCI 10; Comprehensive income 510 |
| Q19 | NI −150; CFO +50; assets −150 = equity −150 |
| Q20 | Continuing NI 517.5; Total NI 472.5; Parent 424.5 |
| Q21 | GM 40%→45%; OM 15%→11.67% (OpEx bloat) |
| Q22 | Revenue 4,700 |
