# Q&A — Corporate Actions

Theory and worked numerical scenarios on dividends, splits, bonuses, rights issues, and buybacks.

---

### Q1. Does a 2-for-1 stock split make a shareholder wealthier? Walk through why or why not with numbers.

**Model answer.** No. If an investor holds 100 shares at ₹500 (₹50,000 total value) and the company executes a 2-for-1 split, they now hold 200 shares at ₹250 (still ₹50,000 total value) — the market capitalisation and the investor's total holding value are mechanically unchanged; only the share count and per-share price have changed. The purpose of a split is to improve affordability (a lower per-share price may attract more retail participation) and liquidity (more shares outstanding can mean tighter spreads and more trading volume), not to create value.

---

### Q2. Worked — buyback impact on EPS.
*A company has net income of ₹240 cr and 60 mn shares outstanding (EPS = ₹4.00). It executes a buyback, repurchasing and cancelling 6 mn shares.*

**Model answer.**
New share count = 60 − 6 = 54 mn.
New EPS = 240 / 54 = ₹4.44.
EPS rose from ₹4.00 to ₹4.44 (an 11.1% increase) purely from the reduced share count, with no change in the underlying net income or business performance. Whether this buyback *created value* for remaining shareholders depends entirely on whether the repurchase price was below the shares' intrinsic value — buying back overvalued shares actually destroys value even while mechanically boosting EPS, a distinction the chapter emphasises as a common analytical trap.

---

### Q3. Worked — theoretical ex-rights price (TERP) calculation.
*A stock trades at ₹450 before a 1:3 rights issue (one new share for every three held) priced at ₹300.*

**Model answer.**
For every 3 existing shares (value 3 × 450 = ₹1,350), the holder can buy 1 new share at ₹300, giving 4 shares for a total cost of 1,350 + 300 = ₹1,650.
TERP = 1,650 / 4 = ₹412.50.
The price is expected to settle around ₹412.50 post-rights — a fall from ₹450, but this is not a loss for a shareholder who subscribes to their full entitlement: they now hold more shares at a lower average cost, and total portfolio value is preserved. A shareholder who does *not* subscribe is diluted and their proportional ownership falls, though they can potentially recoup some value by selling the rights entitlement itself if it's tradeable.

---

### Q4. Distinguish which corporate actions are "cosmetic" (no total value change) from which are "value-changing," and explain the underlying reason for the distinction.

**Model answer.** Cosmetic actions — stock splits and bonus issues — merely restructure the existing equity claim into a different number of shares/different face value, drawing from the company's own reserves (bonus) or simply redefining share units (split), with no cash or assets actually leaving or entering the company; total value is mechanically preserved. Value-changing actions — dividends and buybacks — involve actual cash leaving the company to shareholders, directly reducing the company's asset base (and, in the case of a dividend, typically causing an ex-date price adjustment roughly equal to the dividend). Rights issues are value-changing in the other direction — real new cash enters the company, funding growth or debt reduction, at the cost of dilution for non-subscribers.

---

### Q5. Why does a stock's price typically fall by roughly the dividend amount on the ex-dividend date, and is this a "loss" for existing shareholders?

**Model answer.** On the ex-dividend date, buyers of the stock are no longer entitled to the declared dividend (only holders as of the record date receive it) — so the stock is mechanically worth roughly the dividend amount less than it was the day before, reflecting that upcoming cash payment no longer being part of what a new buyer receives. This is not a loss for the existing shareholder who is entitled to the dividend: they hold a slightly lower-priced stock plus a dividend payment equal (approximately) to the price drop — their total value (stock plus declared dividend receivable) is essentially unchanged by the mechanical ex-date adjustment itself.

---

### Q6. What's the difference between a bonus issue and a rights issue, and why would a company prefer one over the other?

**Model answer.** A bonus issue gives existing shareholders additional shares for free, funded by capitalising the company's own reserves — no new cash enters the company, and it's purely a cosmetic restructuring (Q4) often used as a signal of management confidence or to improve share liquidity/affordability. A rights issue requires shareholders to pay for the new shares (at a discount to market) — it genuinely raises new capital for the company. A company needing actual growth capital or debt reduction uses a rights issue; a company wanting to signal confidence or improve trading liquidity without needing new cash uses a bonus issue.

---

### Q7. An analyst is building a 10-year historical price chart for a stock that underwent a 1:1 bonus issue five years ago. What adjustment must they make, and what happens if they skip it?

**Model answer.** They must adjust all historical prices *before* the bonus issue date by the bonus ratio (halving pre-bonus prices, in a 1:1 case) so the entire price series is on a consistent, comparable per-share basis. If they skip this adjustment, the chart will show an artificial, dramatic price "crash" exactly at the bonus-issue date that has nothing to do with the company's actual performance — a classic and easily avoidable analytical error that would badly distort any technical analysis, historical-return calculation, or valuation multiple trend built on the unadjusted series.

---

### Q8. A company announces a large buyback funded entirely by increasing debt (leverage), rather than using existing cash reserves. What should an analyst think about beyond the simple EPS-accretion math?

**Model answer.** Beyond the mechanical EPS boost (Q2), a debt-funded buyback increases financial leverage and interest expense, raising the company's financial risk — the analyst should assess whether the resulting capital structure remains prudent (debt/EBITDA, interest coverage) and whether management is buying back shares because they're genuinely undervalued (a legitimate capital-allocation decision) or simply to engineer a short-term EPS increase without a corresponding improvement in the underlying business, sometimes to hit management compensation targets tied to EPS — a distinction directly relevant to assessing management quality and capital-allocation discipline (a recurring theme from the fundamental-analysis chapter).
