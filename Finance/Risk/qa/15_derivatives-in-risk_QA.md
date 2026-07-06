# Q&A — Using Derivatives to Manage Risk

*Practice bank for Chapter 15 (Using Derivatives to Manage Risk). Every question is followed by a full answer. Attempt each before reading the solution. Numerical answers are reconciled at least two independent ways where possible. Conventions: long = agree to buy / benefits when price rises; a "hedge" offsets an existing exposure, "speculation" creates a new one.*

---

## Section A — Concept Check

**A1. In one sentence, what is a derivative, and what is the single feature that makes it useful for risk management?**
A derivative is a contract whose value is *derived* from an underlying variable (a price, rate, index or event) rather than from any intrinsic worth of its own. The feature that makes it a risk tool is **leverage without ownership**: it lets you take on, or shed, exposure to the underlying with little or no upfront capital, so you can offset an existing exposure precisely instead of buying or selling the physical asset.

**A2. State the one-line difference between a forward, a future, and an option.**
A **forward** is a private, customised agreement to trade at a set price on a future date — both sides are obligated. A **future** is the same economics but exchange-traded, standardised, and daily margined. An **option** gives the holder the *right but not the obligation* to trade — obligation is one-sided (the writer's), and the holder pays a premium for that asymmetry.

**A3. Why does hedging with a forward or future eliminate downside but *also* remove upside, while an option does not?**
A forward/future locks a price: whatever the market does, you transact at the agreed level, so a favourable move is surrendered along with the unfavourable one — the payoff is *symmetric* and linear. An option only pays out on one side; you keep the good outcome and cap the bad one, because you can simply let the option lapse. That asymmetry is exactly what the premium buys.

**A4. Explain the distinction between hedging, speculation, and arbitrage using derivatives.**
**Hedging** uses a derivative to *offset* a pre-existing exposure, reducing net risk. **Speculation** uses a derivative to *take* a directional view with no offsetting position, increasing risk in exchange for expected return. **Arbitrage** exploits a price discrepancy between a derivative and its underlying (or between two derivatives) to lock a riskless profit. The same instrument serves all three; intent and existing exposure decide which it is.

**A5. Define the hedge ratio and explain why it is rarely exactly 1.**
The hedge ratio is the number of units of the hedging instrument per unit of exposure being hedged. It departs from 1 because the hedge and the exposure differ in sensitivity: the futures contract may cover a different quantity (contract-size mismatch), the underlying may differ (cross-hedge), or the price relationship may be less than one-for-one (a beta below/above 1 for equities, a duration mismatch for bonds). The minimum-variance hedge ratio is $h^* = \rho\,\sigma_S/\sigma_F$.

**A6. What is basis risk, and why does it survive even a "perfect-sized" futures hedge?**
Basis = spot price − futures price. Basis risk is the risk that this gap moves unpredictably before the hedge is unwound. It survives because a futures hedge fixes the *futures* price you transact at, not the *spot* you actually face; unless spot and futures converge exactly at your horizon (same asset, same date, same location/grade), the residual basis changes your net outcome. It converts absolute price risk into the much smaller — but non-zero — risk of the basis.

**A7. A firm buys a put option on an asset it owns. What insurance analogy applies, and what are the "premium" and "deductible"?**
It is a **protective put** — portfolio insurance. The option **premium** is literally the insurance premium; the gap between the current price and the strike is the **deductible** (the loss you bear before protection kicks in). Below the strike you are made whole (less the premium); above it you keep all the upside and have simply spent the premium.

**A8. Why might a treasurer prefer a collar to a plain protective put?**
A collar buys a protective put *and* sells a call to fund it, so the premium is reduced or zeroed. In return the firm gives up upside above the call strike. A treasurer who wants cheap downside protection and is willing to cap gains — a common trade-off when the priority is certainty, not speculation — prefers the collar's lower (often zero) cost.

**A9. What does an interest-rate swap let a borrower do, in one sentence, and what risk does it convert?**
A plain-vanilla interest-rate swap lets a borrower exchange floating-rate cash flows for fixed (or vice versa) on a notional principal, converting **interest-rate (cash-flow) risk** — the uncertainty of future floating payments — into certainty, without refinancing the underlying loan.

**A10. Why is the notional principal in a swap "notional" — and what actually gets exchanged?**
The notional is never exchanged; it is only the reference figure used to *calculate* the interest payments. What changes hands is the **net difference** between the fixed and floating legs on each settlement date. That is why a large swap can carry huge notional but modest actual cash flows and credit exposure.

**A11. How does a currency forward hedge a foreign-currency receivable, and what is the cost of the hedge?**
An exporter expecting foreign currency in three months sells that currency forward today, locking the domestic-currency amount it will receive regardless of spot moves. The "cost" is not a premium (forwards have zero initial value) but the **forward points** — the difference between spot and forward rates, set by the interest-rate differential (covered interest parity). You may end up worse than the eventual spot; that surrendered upside is the price of certainty.

**A12. What is a credit default swap (CDS), and how does a lender use it to manage risk?**
A CDS is a contract in which the protection buyer pays a periodic premium (the spread) and receives a payout if a reference entity defaults. A lender holding a bond or loan buys CDS protection to **transfer the credit risk** to the seller while keeping the asset — effectively insurance against default — for the cost of the ongoing spread.

**A13. Distinguish exchange-traded from OTC derivatives on three axes.**
**Customisation**: OTC is bespoke, exchange-traded is standardised. **Counterparty risk**: OTC faces the counterparty directly (mitigated by CSAs/collateral); exchange-traded is novated to a central clearing house that guarantees performance. **Liquidity/transparency**: exchange contracts are liquid and price-transparent; OTC can be illiquid and opaque. The trade-off is precision (OTC) versus safety and liquidity (exchange).

**A14. Why can a derivative hedge *increase* risk if mismatched or over-sized?**
If the notional exceeds the exposure, the "hedge" becomes a net directional bet in the opposite direction — over-hedging speculates. If the underlying, maturity, or sensitivity is wrong (a bad cross-hedge), the derivative may move independently of the exposure and add variance rather than remove it. A hedge only reduces risk when its payoff is genuinely negatively correlated with, and correctly scaled to, the exposure.

**A15. State the four principal option Greeks and what each measures in one phrase.**
**Delta** — sensitivity of option value to the underlying price. **Gamma** — rate of change of delta (curvature). **Vega** — sensitivity to implied volatility. **Theta** — sensitivity to the passage of time (decay). Rho (rate sensitivity) is the common fifth.

---

## Section B — Numerical / Applied

### B1 — Futures hedge and basis risk

**Setup.** A refiner will buy 1,000,000 litres of crude in three months. Spot today is ₹60/litre; the 3-month future is ₹62/litre (one contract = 100,000 litres). It hedges by going long 10 futures. At delivery, spot = ₹70 and the future it sells to close = ₹71.

**Step 1 — Physical cost.** Buys 1,000,000 × ₹70 = ₹7,00,00,000.
**Step 2 — Futures gain.** Long at 62, close at 71 → gain ₹9/litre × 1,000,000 = ₹90,00,000.
**Step 3 — Net effective cost.** ₹7,00,00,000 − ₹90,00,000 = ₹6,10,00,000 → **₹61.00/litre.**
**Cross-check via basis.** Effective price = futures entry (₹62) + change in basis. Initial basis (spot − fut) = 60 − 62 = −2; final basis = 70 − 71 = −1. Basis rose by ₹1. Effective price = 62 + (−1) = **₹61**, matching. Had basis been unchanged at −2, the firm would have locked exactly ₹62; the ₹1 improvement is pure basis risk — it helped here, but could equally have hurt.

### B2 — Minimum-variance hedge ratio and contract count

**Setup.** A fund holds ₹50 crore of equity with portfolio beta 1.20 relative to the Nifty. Nifty future = 20,000 index points; lot size = 50; so one contract notionally covers 20,000 × 50 = ₹10,00,000.

**Step 1 — Beta-adjusted exposure.** Effective exposure to hedge = ₹50 crore × 1.20 = ₹60 crore.
**Step 2 — Number of contracts.** N = 60,00,00,000 ÷ 10,00,000 = **600 contracts, sold short.**
**Check.** If Nifty falls 10%, portfolio (β 1.2) falls ≈ ₹50cr × 12% = ₹6 crore. Futures: index drops 2,000 pts × 50 × 600 = ₹6 crore gain. Offsetting — the hedge neutralises systematic risk. Residual (idiosyncratic) risk remains, which is why a single-index hedge is never perfect for a specific portfolio.

### B3 — Protective put payoff

**Setup.** An investor owns a share at ₹100 and buys a 3-month put, strike ₹95, premium ₹3.

**Case price = ₹80.** Stock loss = 100 − 80 = ₹20. Put pays 95 − 80 = ₹15. Net position value = 80 + 15 − 3 = **₹92.** Maximum loss is fixed: 100 − 95 + 3 = ₹8, whatever the price below 95.
**Case price = ₹120.** Put expires worthless. Net = 120 − 3 = **₹117.** Upside kept, less the ₹3 premium.
**Break-even on the upside** = 100 + 3 = ₹103. Interpretation: the put converts an open-ended downside into a capped ₹8 loss, in exchange for a ₹3 drag on gains — textbook insurance economics.

### B4 — Zero-cost collar

**Setup.** Same share at ₹100. Buy put strike 95 for ₹3; sell call strike 110 for ₹3. Net premium = 0.

**Below 95:** protected — floor value 95 (net of zero premium).
**Between 95 and 110:** you ride the stock one-for-one.
**Above 110:** call is exercised against you; upside capped at 110.
So the outcome is bounded to the corridor **[95, 110] at zero cost.** The price of free protection is the surrendered gains above 110 — a fair trade only if you value certainty over the tail upside.

### B5 — Interest-rate swap converting floating to fixed

**Setup.** A firm has a ₹100 crore loan at floating MIBOR + 1.5%. It enters a swap to **pay fixed 7%, receive MIBOR** on ₹100 crore notional.

**Net cost after swap.** Loan pays (MIBOR + 1.5%); swap: receives MIBOR, pays 7%.
Combined = −(MIBOR + 1.5%) + MIBOR − 7% = **−8.5% fixed.** MIBOR cancels.
**Check at MIBOR = 6%:** loan = 7.5%, swap net = pay 7% − receive 6% = pay 1% → total 8.5%. At MIBOR = 9%: loan = 10.5%, swap net = pay 7% − receive 9% = receive 2% → total 8.5%. Rate risk is fully removed; the firm now pays a certain 8.5% regardless of MIBOR.

### B6 — Currency forward on a receivable

**Setup.** An Indian exporter will receive \$1,000,000 in 90 days. Spot = ₹83.00/\$; 90-day forward = ₹83.60/\$. It sells the dollars forward.

**Locked receipt** = 1,000,000 × 83.60 = **₹8,36,00,000**, guaranteed.
**If spot at settlement = ₹81:** unhedged would have got ₹8,10,00,000 → hedge saved ₹26,00,000.
**If spot = ₹85:** unhedged would have got ₹8,50,00,000 → hedge cost ₹14,00,000 of upside.
The forward removes all FX uncertainty; whether it "wins" ex post is irrelevant to its risk-management purpose — it delivered certainty, which was the objective.

### B7 — Delta hedging an option book

**Setup.** A desk is short 100 call contracts (100 shares each = 10,000 shares) with delta 0.40.

**Step 1 — Net delta.** Short calls → position delta = −0.40 × 10,000 = **−4,000.** The book loses if the stock rises.
**Step 2 — Hedge.** Buy 4,000 shares to bring net delta to zero.
**Step 3 — Why it is not "done".** As the stock rises, gamma raises the call's delta toward, say, 0.55, so position delta becomes −5,500 while the hedge still holds only 4,000 shares → net −1,500; the desk must buy 1,500 more shares. Delta-neutral is a one-instant state; gamma forces continuous re-hedging, and each re-hedge is "buy high / sell low," which is the cost that the option premium (theta) compensates.

---

## Section C — Interview-Style

**C1. "Your CFO says derivatives are dangerous and wants to ban them. How do you respond?"**
I'd separate the instrument from its use. Derivatives are dangerous only when used to *take* risk without an offsetting exposure, or when sized wrongly. Used as intended — a forward on a known receivable, a swap on a floating loan, a put on a held asset — they *reduce* the firm's risk and smooth cash flows, which lowers the cost of capital and protects covenants. The famous blow-ups (Barings, Amaranth, LTCM) were speculation or leverage failures, not hedging failures. The right response is a policy: hedge only identified exposures, cap notionals to underlying quantities, mark to market daily, and separate the dealing desk from settlement. Banning hedging would leave the firm *more* exposed, not less.

**C2. "When would you hedge with options rather than futures, and what do you pay for that choice?"**
Options when the exposure is *uncertain* or when I want to keep upside. If a bid I've tendered might not be won, a forward would over-hedge and create a naked position if the bid fails — an option lets me walk away. Options also suit asymmetric views: protect the downside, keep the rally. The cost is the premium — a certain cash outflow versus a forward's zero upfront cost. So the decision is: pay a known premium for optionality and retained upside (options), or lock a price for free but surrender the upside (futures/forwards). Contingent exposures and convex payoffs argue for options; certain, symmetric exposures argue for forwards.

**C3. "Walk me through the risks that *remain* after you put on a 'perfect' futures hedge."**
Four residuals. **Basis risk** — spot and futures may not converge at my horizon. **Rollover risk** — if my exposure outlasts the liquid contract, I must roll and face uncertain roll costs. **Margin/liquidity risk** — daily variation margin can demand large cash even when the hedge is "working," which sank Metallgesellschaft. **Correlation/quantity risk** — in a cross-hedge or when the hedged quantity itself is uncertain (a farmer's crop yield), the offset is imperfect. A hedge doesn't make risk vanish; it *transforms* price risk into these smaller, more manageable residuals.

**C4. "A trader shows a huge notional swap position but says credit exposure is small. Is that possible?"**
Yes, and it's the norm. Notional is only the reference for computing payments — it is never exchanged. The actual credit exposure on a swap is the *replacement cost* if the counterparty defaults, i.e. the current mark-to-market of the net future cash flows, which is a small fraction of notional and can be near zero at inception. Add potential future exposure for how it might grow, then net across trades and subtract collateral held under the CSA. So a ₹1,000 crore notional swap might carry only a few crore of current exposure. The caveat: that exposure is *live* and grows with rate moves, so it must be monitored, not dismissed.

**C5. "How do you decide the hedge ratio for a bond portfolio using interest-rate futures?"**
I match *dollar duration*, not face value. Compute the portfolio's DV01 (or PV01), compute the DV01 of one futures contract via the cheapest-to-deliver bond's DV01 divided by its conversion factor, then N = portfolio DV01 ÷ futures DV01. If I want to *reduce* duration to a target rather than zero it, I hedge the DV01 gap. I'd then stress the hedge for a non-parallel curve shift, because a duration hedge only neutralises parallel moves — twists and butterflies leave residual risk that may need key-rate or multiple-maturity futures.

**C6. "Explain to a non-finance board member why a zero-cost collar isn't actually free."**
Nothing is free; "zero-cost" only means no cash changes hands upfront. We buy downside protection and pay for it by *selling away* our upside above a ceiling. If the asset soars, we forgo those gains — that surrendered profit is the real cost, paid in the future and only if things go well. So it's the right tool when we value certainty and don't need the home-run outcome, but the board should understand we've traded the top of the range for protection on the bottom.

---

## Section D — MCQs (with reasoning)

**D1. A wheat farmer expecting a harvest in three months is most naturally hedged by:**
(a) buying wheat futures (b) selling wheat futures (c) buying a wheat call (d) selling a wheat put
**Answer: (b).** The farmer is *long* physical wheat (will own it) and fears a price *fall*. Selling futures locks the sale price. Buying futures (a) would double the long exposure — speculation. A call (c) protects against a rise, the wrong direction. Selling a put (d) adds downside risk for premium — the opposite of a hedge.

**D2. Basis risk in a futures hedge is best described as the risk that:**
(a) the futures exchange defaults (b) the spot–futures gap changes before the hedge is closed (c) volatility rises (d) the option expires worthless
**Answer: (b).** Basis = spot − futures; basis risk is uncertainty in that gap at the horizon. (a) is clearing/counterparty risk, essentially removed by the CCP. (c) is vega, an options concept. (d) applies to options, not futures.

**D3. The notional principal of an interest-rate swap:**
(a) is exchanged at maturity (b) is exchanged at inception and maturity (c) is never exchanged and only scales the interest calculation (d) equals the credit exposure
**Answer: (c).** Only net interest differences change hands; the notional is a reference figure. (a)/(b) describe cross-currency principal exchange, not a single-currency IRS. (d) is false — credit exposure is the mark-to-market replacement cost, far smaller than notional.

**D4. Which position has a symmetric (linear) payoff?**
(a) long call (b) long put (c) long forward (d) protective put
**Answer: (c).** A forward gains and loses one-for-one with the underlying — symmetric. Calls (a), puts (b), and the protective put (d) all have kinked, asymmetric payoffs because of the option's one-sided exercise.

**D5. A firm sells a call against stock it owns (a covered call). Its main risk is:**
(a) unlimited loss if the stock falls (b) forgone gains if the stock rises above the strike (c) margin calls on the stock (d) losing the premium
**Answer: (b).** The covered call keeps the premium and full downside exposure of the stock but caps upside at the strike; the real "cost" is the surrendered rally. (a) is wrong — the loss is bounded by the stock going to zero, cushioned by the premium. (d) is wrong — the writer *receives* the premium.

**D6. Over-hedging (notional greater than exposure) causes the hedge to:**
(a) remain a perfect hedge (b) become a net speculative position in the opposite direction (c) eliminate basis risk (d) reduce margin requirements
**Answer: (b).** Beyond the exposure, the extra notional is unmatched and creates fresh directional risk opposite to the original — speculation. It neither removes basis risk (c) nor lowers margin (d).

**D7. A lender wanting to keep a loan on its books but shed the default risk should:**
(a) sell the loan (b) buy CDS protection on the borrower (c) sell CDS protection (d) buy a call on the borrower's stock
**Answer: (b).** Buying CDS transfers default risk to the seller while the lender retains the asset and relationship. Selling the loan (a) removes the asset entirely; selling CDS (c) *adds* credit risk; an equity call (d) is a directional bet, not credit protection.

**D8. Delta-hedging a short option position requires continuous re-hedging chiefly because of:**
(a) theta (b) rho (c) gamma (d) the risk-free rate
**Answer: (c).** Gamma makes delta change as the underlying moves, so a static share hedge drifts out of neutrality and must be rebalanced. Theta (a) is time decay — the P&L cost, not the trigger for re-hedging. Rho (b) and the rate (d) are second-order for equity option hedging.

**D9. Compared with an OTC forward, an exchange-traded future primarily reduces:**
(a) basis risk (b) counterparty (default) risk (c) market risk (d) the need to hedge
**Answer: (b).** Central clearing and daily margining substitute the clearing house's guarantee for direct counterparty exposure. Standardisation can actually *increase* basis risk (a) relative to a bespoke forward; market risk (c) is unchanged; the need to hedge (d) is unaffected.

**D10. A treasurer buys a floor on a floating-rate *asset* (an investment earning MIBOR). This protects against:**
(a) rates rising (b) rates falling below the floor strike (c) the counterparty defaulting (d) currency moves
**Answer: (b).** A floor pays when the reference rate drops below the strike, protecting the income on a floating-rate *asset* from falling rates. Rising rates (a) would be a *cap*, which protects a floating-rate *borrower*. (c)/(d) are unrelated risk types.

---

*End of practice bank. If you can explain **why** each hedge removes risk — which exposure it offsets, in which direction, and what residual (basis, gamma, roll, margin) survives — you understand the chapter, not just the formulas.*
