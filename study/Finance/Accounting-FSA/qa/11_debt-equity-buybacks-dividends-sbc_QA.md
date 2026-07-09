# Q&A — Debt, Equity, Buybacks, Dividends & Stock-Based Comp

A mixed bank of conceptual and numerical questions. Numericals are fully solved and self-verified. "Say it like this" lines give you the crisp interview delivery.

---

## Conceptual

### Q1. Why is interest tax-deductible but dividends are not?

**Answer.** Interest is the *cost of using someone else's capital* — a contractual price paid to a non-owner. That is a genuine business expense, so it reduces taxable income and net income. Dividends are a *distribution of profit that already belongs to the owners*; you can't "expense" giving people their own money, so dividends reduce retained earnings directly and get no tax deduction. This asymmetry is the entire source of the debt "tax shield."

**Say it like this:** "Interest is a cost of doing business paid to lenders, so it's deductible; dividends are just handing owners profit they already own, so no deduction — that's why debt has a tax shield and equity doesn't."

---

### Q2. Is stock-based compensation a real expense? Then why do we add it back?

**Answer.** Yes. The company received real labor and paid for it with equity. Under ASC 718 / IFRS 2 it's measured at grant-date fair value and expensed over the vesting period, reducing net income. We add it back in cash flow from operations only because *no cash left the company* — it's a non-cash expense. But it's not free: the cost reappears as **dilution** as awards vest. Adding it back to build "adjusted EBITDA" without loading the dilution double-counts the benefit.

**Say it like this:** "It's a real expense settled in stock, so we add it back in CFO because it's non-cash — but the cost never disappears, it just migrates from the P&L to the share count as dilution."

---

### Q3. Walk through the three statements when a company pays a $50 cash dividend.

**Answer.**
- **Income statement:** no impact — dividends are a capital transaction with owners.
- **Balance sheet:** cash −$50, retained earnings −$50; balances.
- **Cash flow:** −$50 financing outflow (when paid).

At declaration you'd book Dr Retained earnings / Cr Dividends payable; the cash moves at payment.

**Say it like this:** "Dividends never touch the income statement. Retained earnings and cash both drop $50, and it's a financing outflow."

---

### Q4. A bond is issued at a premium. Is interest expense above or below the coupon, and what happens to the carrying value?

**Answer.** A premium means the coupon is *above* the market yield, so investors paid more than face. Under the effective-interest method, interest expense = carrying value × market yield, which is **below** the cash coupon. The excess coupon amortizes the premium, so the carrying value **declines toward par** by maturity.

**Say it like this:** "Premium means expense is below the coupon; the difference amortizes the premium down so the liability drifts to par by maturity. Discount is the mirror image."

---

### Q5. What's the difference between treasury stock and retiring shares?

**Answer.** Buying back and holding as **treasury stock** keeps the shares legally alive in a contra-equity account; they can be reissued for options or M&A. **Retiring/cancelling** extinguishes the shares — you reduce common stock and APIC pro-rata and plug the remainder to retained earnings. Under IFRS neither ever produces a P&L gain or loss (IAS 32.33). Economically both reduce total equity and the effective share count.

**Say it like this:** "Treasury = held and reusable; retirement = permanently cancelled. Either way it's a capital transaction — never a P&L gain or loss on your own shares."

---

### Q6. Dividend vs. buyback — which should a company prefer and why?

**Answer.** Both are financing outflows with no income-statement impact. A **dividend** is a sticky, credible signal but a taxable cash event that leaves share count unchanged. A **buyback** reduces the share count (raising EPS and each holder's ownership), is more flexible (no implied ongoing commitment), and defers shareholder tax until they sell. Buybacks make sense when the stock is undervalued and the firm wants flexibility; dividends suit stable, mature cash generators signaling durability.

**Say it like this:** "Buybacks are flexible and tax-efficient and shrink the share count; dividends are a sticky signal of durable cash flow. Choice depends on valuation, flexibility needs, and shareholder tax profile."

---

### Q7. Why does EPS use weighted-average shares rather than year-end shares?

**Answer.** Earnings are generated across the whole year, but shares can be issued or repurchased mid-year. Dividing a full year's profit by a share count that only existed for part of the year would misstate per-share earnings. Weighting each share by the fraction of the year it was outstanding matches the denominator to the period the earnings were actually earned.

**Say it like this:** "You match the denominator to the period earnings were earned — a share issued in December shouldn't get credit for a full year of profit."

---

### Q8. What is the difference between cash interest and interest expense, and when does it matter most?

**Answer.** Interest **expense** is the accrual income-statement figure: cash coupon plus discount/amortized-issuance-cost amortization (minus premium amortization). Cash **interest** is what actually leaves the company. They diverge on discount/premium bonds and, dramatically, on **PIK debt**, where interest expense accrues and the liability grows but zero cash is paid. It matters most for **credit analysis** — EBITDA/cash-interest coverage can look healthy on PIK structures while leverage quietly compounds.

**Say it like this:** "Interest expense is accrual, cash interest is what's actually paid — PIK is the extreme case where expense accrues but no cash moves, flattering coverage while leverage builds."

---

### Q9. Explain the treasury-stock method for diluting options.

**Answer.** Assume all in-the-money options are exercised. The company receives the strike proceeds and uses them to buy back shares at the **average market price**. Net new shares = options exercised − shares repurchased = n × (P − K) / P. Only in-the-money options (P > K) are included; out-of-the-money options are anti-dilutive and excluded.

**Say it like this:** "Assume exercise, use the strike cash to buy back stock at the average price, add the net new shares. Net dilution is n times price-minus-strike over price."

---

### Q10. A company issues $100 of stock instead of taking a $100 loan. Contrast the ongoing statement impact.

**Answer.** **Equity issuance:** cash +$100, equity +$100 at issue; no ongoing income-statement charge (dividends, if any, hit RE not NI); dilutes existing holders. **Debt:** cash +$100, liability +$100; ongoing interest expense reduces NI each period but earns a tax shield and doesn't dilute ownership; principal must be repaid. Debt is cheaper (tax shield, no dilution) but adds fixed obligations and default risk; equity is permanent and flexible but dilutive and costlier.

**Say it like this:** "Debt costs you deductible interest but no dilution and it must be repaid; equity costs you ownership dilution but no fixed charge and never matures."

---

## Numerical

### Q11. Bond issued at a discount — issue price and Year 1 interest.

**Facts.** $1,000,000 face, 3-year, 5% annual coupon, market yield 7%.

**Solution.**
- Coupon = 1,000,000 × 5% = $50,000/yr.
- PV coupons = 50,000 × [1 − 1.07⁻³]/0.07 = 50,000 × 2.624316 = $131,216.
- PV principal = 1,000,000 × 1.07⁻³ = 1,000,000 × 0.816298 = $816,298.
- **Issue price = 131,216 + 816,298 = $947,514.** Discount = $52,486.
- **Year 1 interest expense** = 947,514 × 7% = **$66,326**.
- Coupon paid = $50,000. Discount amortized = 66,326 − 50,000 = $16,326.
- End-Year-1 carrying value = 947,514 + 16,326 = **$963,840**. ✓ (rises toward par)

**Check:** expense ($66,326) > coupon ($50,000), consistent with a discount. ✓

---

### Q12. Bond issued at a premium — Year 1.

**Facts.** $1,000,000 face, 3-year, 9% coupon, market yield 7%.

**Solution.**
- Coupon = $90,000/yr.
- PV coupons = 90,000 × 2.624316 = $236,188.
- PV principal = 1,000,000 × 0.816298 = $816,298.
- **Issue price = $1,052,486.** Premium = $52,486.
- **Year 1 interest expense** = 1,052,486 × 7% = **$73,674**.
- Coupon paid = $90,000. Premium amortized = 90,000 − 73,674 = $16,326.
- End carrying value = 1,052,486 − 16,326 = **$1,036,160**. ✓ (falls toward par)

**Check:** expense ($73,674) < coupon ($90,000), consistent with a premium. ✓ (Note the symmetry with Q11 — same $52,486, same $16,326.)

---

### Q13. Cash-funded buyback accretion.

**Facts.** NI = $200m; 80m shares; price $50 (PE = 20, market cap $4,000m). Buy back $500m = 10m shares. Cash was earning 3% pre-tax; tax 25%.

**Solution.**
- After-tax yield lost = 3% × 0.75 = 2.25%. Lost income = 500 × 2.25% = $11.25m.
- New NI = 200 − 11.25 = $188.75m. New shares = 80 − 10 = 70m.
- New EPS = 188.75 / 70 = **$2.696**. Old EPS = 200 / 80 = **$2.50**.
- **Accretive +7.8%.** Rule check: earnings yield = 1/20 = 5% > 2.25% after-tax cash yield → accretive. ✓

---

### Q14. Debt-funded buyback break-even.

**Facts.** Same company as Q13 (earnings yield 5%, tax 25%). At what pre-tax cost of debt does a debt-funded buyback stop being accretive?

**Solution.**
- Accretive while after-tax cost of debt < earnings yield: rate × (1 − 0.25) < 5%.
- Break-even rate = 5% / 0.75 = **6.67%**.
- At 6% debt: after-tax = 4.5% < 5% → accretive. At 8%: after-tax = 6% > 5% → dilutive.

**Quick verify at 6%:** after-tax interest = 500 × 6% × 0.75 = $22.5m; NI = 177.5m; EPS = 177.5/70 = $2.536 > $2.50 → accretive. ✓

---

### Q15. Stock-based comp expense and CFO add-back.

**Facts.** Grant 3,000 RSUs, grant-date price $25, vesting 4 years. Pre-tax income before SBC = $400,000 in Year 1; tax 25%.

**Solution.**
- Total grant value = 3,000 × $25 = $75,000. Annual SBC = 75,000 / 4 = **$18,750**.
- Pre-tax income = 400,000 − 18,750 = $381,250. Tax = $95,313. NI = **$285,937**.
- CFO add-back: NI 285,937 + SBC 18,750 = cash-flow contribution **$304,687** (SBC restored as non-cash).
- Balance sheet: APIC +$18,750; RE up by NI; share count grows as RSUs vest.

**Check:** cash flow exceeds NI by exactly the $18,750 non-cash SBC. ✓

---

### Q16. Diluted EPS with options (treasury-stock method).

**Facts.** NI = $600,000; weighted-average shares = 300,000; options outstanding = 40,000 at strike $15; average price $25.

**Solution.**
- Basic EPS = 600,000 / 300,000 = **$2.00**.
- Proceeds = 40,000 × $15 = $600,000. Shares repurchased at $25 = 600,000/25 = 24,000.
- Net new shares = 40,000 − 24,000 = 16,000. (Shortcut: 40,000 × (25−15)/25 = 16,000. ✓)
- Diluted shares = 316,000. **Diluted EPS = 600,000 / 316,000 = $1.899 ≈ $1.90.**

**Check:** diluted ($1.90) < basic ($2.00). ✓

---

### Q17. Diluted EPS with a convertible bond (if-converted method).

**Facts.** NI = $1,000,000; 500,000 shares; a $2,000,000 convertible bond at 6% coupon, convertible into 100,000 shares; tax 25%.

**Solution.**
- Basic EPS = 1,000,000 / 500,000 = **$2.00**.
- If converted: add back after-tax interest = 2,000,000 × 6% × (1 − 0.25) = 120,000 × 0.75 = $90,000. New numerator = $1,090,000.
- New denominator = 500,000 + 100,000 = 600,000.
- **Diluted EPS = 1,090,000 / 600,000 = $1.817 ≈ $1.82.**

**Anti-dilution test:** $1.82 < $2.00, so the convertible **is** dilutive and is included. ✓ (Per-incremental-share effect = $90,000/100,000 = $0.90 < basic $2.00 → dilutive.)

---

### Q18. Stock dividend — capitalizing retained earnings.

**Facts.** 2,000,000 shares, $1 par, market price $18. Declare a 5% stock dividend (small — recorded at fair value).

**Solution.**
- New shares = 2,000,000 × 5% = 100,000. Fair value = 100,000 × $18 = $1,800,000.
- Entry:
```
Dr Retained earnings           1,800,000
   Cr Common stock (100,000 × $1)             100,000
   Cr Additional paid-in capital            1,700,000
```
- **Total equity unchanged** — $1,800,000 simply moved from RE into contributed capital. Shares now 2,100,000.

**Check:** debits = credits = $1,800,000; par credit 100,000 + APIC 1,700,000 = 1,800,000. ✓

---

### Q19. Full debt walk-through — three statements.

**Facts.** Company issues $1,000 debt at 8%, tax 40%. Show Year 1 impact assuming interest paid in cash and no other activity.

**Solution.**
- **Issuance:** cash +$1,000, debt +$1,000.
- **Income statement:** interest expense $80 → pre-tax income −$80 → tax saving $32 → **net income −$48**.
- **Cash flow:** NI −$48; interest is a real cash payment so CFO shows −$48 (the after-tax cost, since the $80 cash interest is offset by $32 tax shield); principal +$1,000 was a prior financing inflow.
- **Balance sheet:** retained earnings −$48; cash −$48 (net of tax shield). Debt stays $1,000. Balances. ✓

**Say it like this:** "$80 pre-tax interest, $48 hit to net income after the 40% shield, $48 cash out of CFO — principal is financing, interest is operating."

---

### Q20. Early extinguishment of debt — gain/loss.

**Facts.** Bond carrying value (net of unamortized discount) = $960,000. Company calls it at 102% of $1,000,000 face = $1,020,000.

**Solution.**
- Reacquisition price = $1,020,000. Net carrying value = $960,000.
- Gain/(loss) = 960,000 − 1,020,000 = **−$60,000 loss**.
- Entry:
```
Dr Bonds payable               1,000,000
Dr Loss on extinguishment         60,000
   Cr Discount on bonds payable                40,000
   Cr Cash                                   1,020,000
```
(Unamortized discount = 1,000,000 − 960,000 = $40,000.)

**Check:** debits 1,060,000 = credits 40,000 + 1,020,000 = 1,060,000. ✓ The loss hits the income statement — it's a settlement with a creditor, not with owners.

---

### Q21. Buyback held as treasury, then reissued (cost method).

**Facts.** Buy back 10,000 shares at $30 (hold as treasury). Later reissue 4,000 of them at $35.

**Solution.**
- Buyback:
```
Dr Treasury stock   300,000
   Cr Cash                     300,000
```
- Reissue 4,000 at $35 (cost was $30):
```
Dr Cash (4,000 × $35)      140,000
   Cr Treasury stock (4,000 × $30)   120,000
   Cr APIC — treasury                  20,000
```
**Note:** the $20,000 excess is credited to APIC, **never** to income — no P&L gain on your own shares. Remaining treasury = 6,000 × $30 = $180,000.

**Check:** debits 140,000 = credits 120,000 + 20,000. ✓

---

### Q22. Weighted-average shares for EPS.

**Facts.** 1,000,000 shares on 1 Jan. Issued 300,000 more on 1 Jul. Bought back 120,000 on 1 Oct. NI = $2,400,000. (Year = 12 months.)

**Solution.**
- 1,000,000 for 12/12 = 1,000,000.
- +300,000 for 6/12 (Jul–Dec) = +150,000.
- −120,000 for 3/12 (Oct–Dec) = −30,000.
- **Weighted-average shares = 1,000,000 + 150,000 − 30,000 = 1,120,000.**
- **Basic EPS = 2,400,000 / 1,120,000 = $2.143 ≈ $2.14.**

**Check:** end-of-year shares = 1,000,000 + 300,000 − 120,000 = 1,180,000; weighted average (1,120,000) sensibly sits below it because the new shares were outstanding only part-year. ✓
