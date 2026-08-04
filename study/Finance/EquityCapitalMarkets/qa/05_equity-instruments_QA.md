# Q&A — Equity Instruments

Theory and worked scenarios on common, preferred, convertible, and depositary-receipt instruments.

---

### Q1. Common vs preferred shares — what's given up and what's gained by holding preferred instead of common?

**Model answer.** Preferred shareholders give up voting rights (in most standard structures) and uncapped upside participation, in exchange for priority over common holders on dividends (often a fixed rate) and on residual assets in liquidation. Common shareholders retain full voting rights and an uncapped, residual claim on profits and assets, but sit last in the priority stack — first to lose in a downturn, last to be paid even in a good year if the board doesn't declare a dividend. The trade is control-and-upside versus priority-and-a-capped-return.

---

### Q2. Worked — cumulative preferred dividends in a bad year.
*A company owes ₹8 cr/year in cumulative preferred dividends. In Year 1 it can only pay ₹3 cr total. In Year 2, profits recover and ₹15 cr is available for distribution. How much does each class receive in each year?*

**Model answer.**
Year 1: preferred is owed ₹8 cr but only ₹3 cr is available — preferred receives the full ₹3 cr (still short by ₹5 cr, which accrues as arrears since it's cumulative); common receives ₹0.
Year 2: preferred is owed the current year's ₹8 cr *plus* the ₹5 cr arrears from Year 1 = ₹13 cr, paid first from the ₹15 cr available; common receives the remaining ₹15 − 13 = ₹2 cr.
This illustrates why "cumulative" matters: a missed preferred dividend doesn't disappear, it compounds as a prior claim against future distributable profit before common sees anything.

---

### Q3. Worked — convertible bond conversion decision at two different stock prices.
*A ₹1,000 face-value convertible bond converts into 10 shares (conversion price ₹100). At maturity the bond can be redeemed at face value (₹1,000) or converted.*

**Model answer.**
If the stock is at ₹80: conversion value = 10 × 80 = ₹800, less than the ₹1,000 redemption value — the holder redeems for cash, the debt-like floor protects them.
If the stock is at ₹150: conversion value = 10 × 150 = ₹1,500, more than the ₹1,000 redemption value — the holder converts to capture the equity upside.
The convertible's value is effectively the greater of its bond floor and its as-converted equity value, which is exactly why issuers can offer a lower coupon than a plain bond — investors are compensated with this embedded option instead.

---

### Q4. What is an ADR, and why would the ADR price of an Indian company track its NSE/BSE price closely rather than diverge freely?

**Model answer.** An ADR (American Depositary Receipt) is a US-listed certificate representing shares of a non-US company held by a depositary bank — it lets US investors hold and trade the company in dollars without a full separate US listing. Because the ADR and the home-market shares represent the same underlying economic claim (adjusted for the ADR ratio and the USD/INR exchange rate), any meaningful price divergence creates a pure arbitrage opportunity: arbitrageurs would buy the cheaper instrument and sell the more expensive one (or convert between them via the depositary mechanism), which pulls the two prices back into alignment — the arbitrage mechanism itself is what keeps the ADR "tracking" the home share, not any inherent property of the ADR.

---

### Q5. Distinguish a warrant from an exchange-traded call option — same payoff shape, different mechanics and consequences.

**Model answer.** Both give the right to buy shares at a set price by a set date, and both have a similar payoff diagram. The key difference: exercising a warrant creates *new* shares issued by the company (dilutive to existing shareholders, and the exercise proceeds go to the company), while exercising an exchange-traded call option transfers *existing* shares between two market participants (no dilution, no cash to the company — the option writer delivers shares they already own or must acquire in the market). A candidate who conflates the two in an interview signals they haven't thought through where the shares actually come from.

---

### Q6. Where do preferred shares sit in the capital-structure priority stack, and what does that imply about their risk relative to bonds and common equity?

**Model answer.** Priority order (highest to lowest claim): secured debt → unsecured debt → preferred equity → common equity. Preferred sits below all debt (both secured and unsecured), meaning in a liquidation or severe distress scenario, all debtholders must be paid in full before preferred holders receive anything — so preferred is meaningfully riskier than any debt instrument despite sometimes being marketed as a "safer" or "income" instrument. It is, however, senior to common, so it carries less risk than common equity. This full ordering — not just "preferred is safer than common" — is the complete, correct answer.

---

### Q7. What's the difference between a rights issue entitlement and a bonus share, from the shareholder's perspective?

**Model answer.** A rights entitlement gives an existing shareholder the option to *buy* additional shares (usually at a discount to market price) — it requires the shareholder to pay in additional capital to exercise it, and if they don't, their proportional ownership is diluted. A bonus share is issued to existing shareholders *for free*, in proportion to their existing holding, funded by capitalising the company's reserves — it requires no payment and, because more shares now represent the same underlying company value, the share price mechanically adjusts downward (similar to a stock split) with no real change in the shareholder's proportional wealth or ownership percentage.

---

### Q8. Why might a company issue convertible preferred shares rather than either straight debt or a straight equity issue?

**Model answer.** Convertible preferred lets a company raise capital at a lower cost than straight preferred/debt (investors accept a lower fixed return in exchange for the embedded equity-upside option) while deferring dilution — dilution only occurs if and when the instrument converts, typically once the stock has appreciated enough to make conversion attractive to holders. This is a common structure in growth-stage and PE/VC financing rounds specifically because it balances the investor's downside protection (priority, fixed return if it doesn't convert) against the company's desire to avoid selling common equity outright at what may be a depressed current valuation.
