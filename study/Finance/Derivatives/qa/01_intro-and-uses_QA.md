# Q&A — Introduction to Derivatives and Their Uses

A practice bank for the chapter "Introduction to Derivatives and Their Uses." Work each question before reading its answer. Numerical answers are self-verified by reconciliation. Continuous compounding is used throughout, matching the concept note.

---

## Section A — Concept Checks

**A1. In one sentence, what is a derivative, and what does the word "derived" refer to?**

A derivative is a financial contract whose value is a function of the price of some other asset, called the underlying. "Derived" refers to the fact that the contract's own value comes entirely from — is mechanically linked to — the price of that underlying: value of derivative = f(price of underlying). The derivative is not the asset; it is a claim whose payoff tracks the asset.

**A2. The chapter says derivatives solve one fundamental problem. State it.**

Economic decisions are made today, but the prices that determine their outcomes are only settled in the future. A farmer, an exporter, an airline, or a pension fund is exposed today to a price that has not yet happened. Derivatives let you fix, transfer, or reshape that future price today without moving the underlying asset today.

**A3. Define the "separation" that derivatives achieve, and give one example.**

Derivatives separate exposure to a price from ownership of the thing. You can gain or shed the price risk of an asset without buying or selling the asset itself. Example: a fund can hedge the market risk of its entire ₹5,000 crore equity portfolio using index futures without selling a single share — separating the price exposure from the ownership.

**A4. Name the five economic uses of derivatives and give a one-line description of each.**

1. Hedging — transferring unwanted risk to a party willing to bear it or holding mirror-image exposure.
2. Speculation — taking a directional view cheaply and precisely; speculators supply liquidity as the counterparties to hedgers.
3. Arbitrage — exploiting price inconsistencies between a derivative and its underlying, which enforces fair prices.
4. Price discovery — futures prices aggregate thousands of money-backed views into a collective forecast of the future spot.
5. Market completion — building payoff profiles that do not exist in the underlying market, so more states of the world can be insured and traded.

**A5. Why are speculators described as necessary rather than villains?**

Hedgers can only shed risk if someone takes the opposite side. Speculators are those counterparties: they absorb the risk hedgers want to offload, in exchange for expected return. In doing so they provide the liquidity that makes hedging possible at all. Without speculators, a hedger would frequently find no one to trade with.

**A6. Distinguish the payoff shapes of a forward and an option in one line each.**

A forward's payoff is linear and symmetric — a straight line through the forward price, with equal upside and downside, and both parties obligated. An option's payoff is non-linear and asymmetric — kinked at the strike — because the buyer holds a right, not an obligation, and pays a premium for that asymmetry.

**A7. True or false: "The futures price is the market's forecast of the future spot price." Explain.**

Mostly false / only loosely true. The futures price is primarily an arbitrage relation, F₀ = S₀·e^(rT) (cost of carry), not a prophecy. It embeds the spot price plus the net cost of carrying the asset to maturity. It does aggregate views and aids price discovery, but it is pinned by no-arbitrage, not set by pure expectation.

**A8. Why is a swap called "a portfolio of forwards"?**

A swap exchanges two streams of cash flows on scheduled dates. Each individual exchange date is economically one forward contract on the floating leg. Stringing those forwards together across all the payment dates reconstructs the swap. It is priced so the present value of the two legs is equal — zero value at inception.

**A9. Distinguish notional from market value, and explain why confusing them is dangerous.**

Notional is the face quantity of underlying a contract references (e.g. 50 NIFTY units at 24,000 = ₹12,00,000 notional). Market value is what the position is actually worth or costs right now — the margin posted or premium paid, usually a small fraction of notional. Confusing them overstates systemic risk (the "$600 trillion" headline is gross notional, not money at stake) and, for an individual, hides how much leverage a small outlay carries.

**A10. What two weaknesses of forwards do futures eliminate, and how?**

Counterparty default risk and illiquidity. A clearing house inserts itself as counterparty to both sides and guarantees performance (removing default risk), and standardisation of contract size, quality, and dates lets you offset the position anytime by taking the opposite trade (removing illiquidity). Daily mark-to-market backs the guarantee by settling gains and losses each day.

---

## Section B — Numerical / Payoff Problems

**B1. Long forward reconciliation.** A copper fabricator will need 100 tonnes of copper in six months. It enters a long forward at F = ₹800 per kg (100 tonnes = 100,000 kg). Show its effective cost if spot at maturity is (a) ₹950/kg and (b) ₹700/kg.

*Step 1 — forward payoff (long) = S_T − F, per kg.*
(a) S_T = 950: payoff = 950 − 800 = +₹150/kg → 150 × 100,000 = +₹15,000,000.
(b) S_T = 700: payoff = 700 − 800 = −₹100/kg → −100 × 100,000 = −₹10,000,000.

*Step 2 — physical purchase in the spot market.*
(a) buy at 950 → 950 × 100,000 = ₹95,000,000 outflow.
(b) buy at 700 → 700 × 100,000 = ₹70,000,000 outflow.

*Step 3 — net effective cost = spot purchase − forward gain (or + forward loss).*
(a) 95,000,000 − 15,000,000 = ₹80,000,000 → 80,000,000 ÷ 100,000 = ₹800/kg. ✔
(b) 70,000,000 + 10,000,000 = ₹80,000,000 → ₹800/kg. ✔

*Reconciliation:* both scenarios lock the effective cost at exactly the forward price ₹800/kg. The hedge removed uncertainty (and the downside-price windfall in case b). That is the linear, symmetric, obligated signature of a forward.

**B2. Fair forward price (cost of carry).** A non-dividend stock trades at S₀ = ₹1,000. The continuously compounded rate is r = 6%, maturity T = 1 year. Compute the no-arbitrage forward price, and state the arbitrage if the market quoted F = ₹1,080.

*Step 1 — F₀ = S₀·e^(rT) = 1,000 · e^(0.06×1) = 1,000 · e^0.06.*
e^0.06 = 1.061837 → F₀ = ₹1,061.84.

*Step 2 — market quote ₹1,080 > fair ₹1,061.84, so the forward is too expensive.* Cash-and-carry arbitrage: today borrow ₹1,000 at 6%, buy the stock, and sell it forward at ₹1,080. At T repay the loan of 1,000·e^0.06 = ₹1,061.84 and deliver the stock for ₹1,080.

*Step 3 — riskless profit = 1,080 − 1,061.84 = ₹18.16 per share*, with zero net investment and zero price risk. Arbitrageurs doing this push F down toward ₹1,061.84. ✔

**B3. Long call profit table and break-even.** A trader buys one call on a stock: strike K = ₹500, premium c = ₹20. Build the profit at expiry for S_T = 460, 500, 520, 540, 600, and state the break-even and maximum loss.

| S_T | Intrinsic max(S_T − K, 0) | Profit = intrinsic − c |
|---|---|---|
| 460 | 0 | −20 |
| 500 | 0 | −20 |
| 520 | 20 | 0 |
| 540 | 40 | +20 |
| 600 | 100 | +80 |

Break-even = K + c = 500 + 20 = ₹520 (matches the table row where profit = 0). Maximum loss = premium = ₹20, no matter how far the stock falls. Upside is unlimited. ✔ (self-check: at 600, intrinsic 600 − 500 = 100, minus 20 = 80. ✔)

**B4. Long put profit and break-even.** A trader buys one put, K = ₹500, premium p = ₹15. Give the payoff and profit at S_T = 470 and S_T = 520, and the break-even.

*At S_T = 470:* payoff = max(K − S_T, 0) = max(500 − 470, 0) = ₹30. Profit = 30 − 15 = +₹15.
*At S_T = 520:* payoff = max(500 − 520, 0) = 0. Profit = 0 − 15 = −₹15 (max loss = premium).
*Break-even = K − p = 500 − 15 = ₹485.* Check: at S_T = 485, payoff = 500 − 485 = 15, profit = 15 − 15 = 0. ✔

**B5. Option writer's mirror.** For the call in B3 (K = 500, c = 20), give the short-call (writer's) profit at S_T = 460 and S_T = 600, and confirm it is the mirror of the long.

Short call profit = c − max(S_T − K, 0).
*At 460:* = 20 − 0 = +₹20 (keeps the premium).
*At 600:* = 20 − 100 = −₹80.
Long call at those spots was −20 and +80. Sum of long + short = (−20 + 20) = 0 and (+80 − 80) = 0. Zero-sum between buyer and writer, confirmed. ✔ The writer's gain is capped at ₹20; the loss is potentially unlimited.

**B6. Leverage, both directions.** A trader posts ₹80,000 margin to go long one index futures lot: 40 units at 25,000. Find the notional, the leverage, and the return on capital if the index (a) rises 4% and (b) falls 4%.

*Notional = 40 × 25,000 = ₹10,00,000. Leverage = 10,00,000 ÷ 80,000 = 12.5×.*
(a) +4% → index to 26,000; gain per unit = 1,000; total = 1,000 × 40 = ₹40,000. Return = 40,000 ÷ 80,000 = +50%.
(b) −4% → index to 24,000; loss per unit = 1,000; total = −₹40,000. Return = −50%.

*Check via leverage: 4% × 12.5 = 50%. ✔* A 4% index move became a 50% capital move in either direction — leverage is symmetric, and a further fall would trigger a margin call.

**B7. Put-call parity — consistency test.** European options on a non-dividend stock: S₀ = ₹1,000, K = ₹1,020, r = 7%, T = 0.5 yr. The market quotes c = ₹55, p = ₹40. Is this arbitrage-free? If not, what call price restores parity?

*Step 1 — discounted strike: K·e^(−rT) = 1,020 · e^(−0.07×0.5) = 1,020 · e^(−0.035).*
e^(−0.035) = 0.965605 → 1,020 × 0.965605 = ₹984.92.

*Step 2 — parity requires c − p = S₀ − K·e^(−rT) = 1,000 − 984.92 = ₹15.08.*

*Step 3 — quoted c − p = 55 − 40 = ₹15.00.* The gap is only 15.08 − 15.00 = ₹0.08 — essentially at parity (within rounding). Effectively arbitrage-free. To be exact, holding p = 40, the parity call is c = p + 15.08 = ₹55.08. Check: 55.08 − 40 = 15.08 = S₀ − K·e^(−rT). ✔

**B8. Put-call parity — solve for the put.** Same data as B7 (S₀ = 1,000, K = 1,020, r = 7%, T = 0.5), and a quoted call c = ₹70. What is the arbitrage-free put price?

From c − p = S₀ − K·e^(−rT) = ₹15.08, we get p = c − 15.08 = 70 − 15.08 = ₹54.92.
Check: c − p = 70 − 54.92 = 15.08 = 1,000 − 984.92. ✔

**B9. Futures daily mark-to-market path.** A trader is long one lot (lot size 50) at entry price 24,000. Over three days the settlement prices are 24,100, 23,950, 24,050. Show the daily MTM cash flows and confirm the total equals the position's economic payoff.

Day 1: (24,100 − 24,000) × 50 = +₹5,000 credited.
Day 2: (23,950 − 24,100) × 50 = −₹7,500 debited.
Day 3: (24,050 − 23,950) × 50 = +₹5,000 credited.
Total MTM = 5,000 − 7,500 + 5,000 = +₹2,500.
Economic payoff = (final − entry) × lot = (24,050 − 24,000) × 50 = 50 × 50 = ₹2,500. ✔ Daily settlement sums to the same total as a single settlement at maturity; futures merely realise it in increments.

**B10. Option vs outright share, best and worst case.** Spot S₀ = ₹2,500. Compare buying the share to buying one call (K = 2,600, c = 50) at S_T = 2,300 and S_T = 3,000.

*Share:* at 2,300 loss = 2,300 − 2,500 = −₹200; at 3,000 gain = +₹500.
*Call:* at 2,300, intrinsic 0, profit = −50; at 3,000, intrinsic = 400, profit = 400 − 50 = +₹350.
The call cuts the worst case from −200 to −50 (a ₹150 improvement) and trims the best case from +500 to +350 (a ₹150 give-up). The trader paid, in effect, ₹150 of forgone upside for downside insurance plus the ₹100 out-of-the-money strike gap — the asymmetric trade-off options offer. ✔

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Explain to a non-finance person what a derivative is and why anyone needs one."**

A derivative is a contract whose value simply tracks the price of something else — oil, a stock, an exchange rate. Its purpose is to let people deal with prices that haven't happened yet. An airline that must buy fuel in December can lock December's price today; a farmer can lock the harvest price before planting; an exporter can lock the rupee-dollar rate before the dollars arrive. The magic is separation: you get the price protection without having to buy and store the physical thing today. The same contracts also let others bet on prices, correct mispricings, and reveal where prices are heading.

**C2. "Are derivatives zero-sum? Are they gambling?"**

At the contract level, forwards and futures are zero-sum: one party's gain is exactly the other's loss. But that misses the economic point. When a hedger with genuine exposure trades with a speculator willing to bear risk, the transaction is positive-sum for the economy — risk moves from someone who can't afford it to someone who can, and the hedger gets a stable budget. It's not gambling when it offsets a real exposure; it's insurance. The instrument is neutral. Danger comes from leverage and un-hedged speculation, not from the tool.

**C3. "What's the difference between a forward and a future — and why does it matter?"**

Economically they're the same bet: a locked price to trade later, with linear symmetric payoff. Mechanically they differ. A forward is a private, customisable OTC contract, settled once at maturity, carrying counterparty default risk and low liquidity. A future is standardised, exchange-traded, guaranteed by a clearing house, and marked-to-market daily. It matters because it's a trade-off: forwards give a perfect fit (exact quantity, date, delivery point) but you're exposed to the other side defaulting and you can't easily exit; futures give safety and liquidity but force you into standard terms and daily cash settlement that can trigger margin calls.

**C4. "Walk me through put-call parity and why it's an arbitrage relationship, not a forecast."**

Put-call parity says c − p = S₀ − K·e^(−rT) for European options on a non-dividend asset. The intuition: a long call plus a short put at the same strike replicates a forward on the stock, so a call minus a put must equal the value of that forward position, which is spot minus the discounted strike. It's enforced by arbitrage, not opinion: if the relationship broke, you could build the cheaper synthetic and short the dearer real one, pocketing a riskless profit. No view on where the stock is going is involved — it's a structural link between the two option prices, the spot, and the interest rate.

**C5. "A headline says the global derivatives market is $600 trillion. Should we panic about systemic risk?"**

Not at face value — that figure is gross notional, the face amount all contracts reference, not money actually at stake. The gross market value, what it would cost to replace all contracts, is a small fraction of notional, and the net exposure after offsetting opposite positions is smaller still. A firm can hold a ₹5,000 crore notional swap book worth only tens of crores. Notional measures the size of the reference; value measures money at risk. That said, leverage means small values can still cause large damage if capital is thin — which is the real lesson of AIG in 2008, where huge CDS notional was written against too little capital.

**C6. "Why did leverage bring down firms like Barings, LTCM, and AIG if derivatives are just neutral tools?"**

Because leverage is a symmetric multiplier taken beyond the capital that could absorb a loss. You post only margin or a small premium, so a small adverse move becomes a huge percentage loss on your capital — and with futures or written options the loss can exceed what you posted. Daily mark-to-market can demand fresh cash at the worst moment, forcing liquidation near the bottom. In each collapse the instruments weren't evil; the position size relative to capital was un-respected. The discipline is to size exposure to the notional, not to the small upfront outlay.

**C7. "How does a swap let a company change its interest-rate exposure without touching its loan?"**

In a plain-vanilla interest-rate swap the firm agrees to exchange cash flows on a notional: say it pays fixed and receives floating. If it already has a floating-rate loan, the received-floating leg offsets its loan payments, and it's left effectively paying fixed — it has converted floating debt to fixed without renegotiating the loan. Only the net difference changes hands each period; the notional is never exchanged. This is the separation principle again: it reshapes the exposure without moving the underlying debt.

---

## Section D — Multiple-Choice Questions with Reasoning

**D1. The payoff to a long forward at maturity is:**
(a) max(S_T − F, 0) (b) S_T − F (c) F − S_T (d) max(F − S_T, 0)

**Answer: (b).** A forward is an unconditional obligation, so there is no max() — the payoff is linear: the long gains S_T − F when spot exceeds the locked price and loses when it is below. (a) and (d) are option payoffs; (c) is the short forward.

**D2. Which is NOT one of the five economic uses of derivatives listed in the chapter?**
(a) Hedging (b) Price discovery (c) Tax evasion (d) Market completion

**Answer: (c).** The five uses are hedging, speculation, arbitrage, price discovery, and market completion. Tax evasion is not among them (and is illegal); tax deferral is at most an incidental motive for not selling a physical position, not a stated use.

**D3. The forward price of a non-dividend asset under continuous compounding is:**
(a) S₀·e^(−rT) (b) S₀·e^(rT) (c) S₀ + rT (d) the market's expected S_T

**Answer: (b).** Cost of carry compounds spot up at the financing rate: F₀ = S₀·e^(rT). (a) discounts instead of compounds; (c) uses simple arithmetic wrongly; (d) is the common misconception — the forward is an arbitrage relation, not a pure expectation.

**D4. A trader posts ₹1,00,000 margin to control ₹15,00,000 of notional. Leverage is:**
(a) 6.67× (b) 10× (c) 15× (d) 0.067×

**Answer: (c).** Leverage = notional ÷ capital committed = 15,00,000 ÷ 1,00,000 = 15×. (a) inverts the ratio incorrectly; (d) is the reciprocal.

**D5. Which statement about options is correct?**
(a) Both buyer and writer are obligated to transact.
(b) The buyer's maximum loss is unlimited.
(c) The writer receives a premium and takes on the obligation to perform if exercised.
(d) A call gives the right to sell at the strike.

**Answer: (c).** Only the writer is obligated; the buyer holds a right and loses at most the premium (so (a) and (b) are wrong). A call is the right to buy, not sell, so (d) is wrong.

**D6. Put-call parity for European options on a non-dividend stock states c − p equals:**
(a) S₀ − K (b) S₀ − K·e^(−rT) (c) K·e^(−rT) − S₀ (d) S₀ + K·e^(−rT)

**Answer: (b).** c − p = S₀ − K·e^(−rT). (a) forgets to discount the strike; (c) reverses the sign; (d) wrongly adds.

**D7. The single feature that best distinguishes a future from a forward is:**
(a) Futures have non-linear payoffs.
(b) Futures are marked-to-market daily and cleared by a clearing house.
(c) Forwards require a premium; futures do not.
(d) Forwards are exchange-traded.

**Answer: (b).** Standardisation, central clearing, and daily mark-to-market are the futures signature. (a) is false — both are linear; (c) confuses options (premium) with forwards; (d) is backwards — forwards are OTC.

**D8. "Notional" in a derivatives context refers to:**
(a) The money actually at stake right now.
(b) The premium paid.
(c) The face quantity of underlying the contract references.
(d) The daily margin call.

**Answer: (c).** Notional is the reference face amount (e.g. 50 units × 24,000). What is actually at stake is the market value/margin/premium — the answer options (a) and (b) — which are typically a small fraction of notional.

**D9. A perfect hedge is best described as producing:**
(a) Guaranteed profit (b) Certainty of outcome, often forgoing upside (c) Unlimited upside with capped downside (d) Leverage

**Answer: (b).** A perfect hedge removes uncertainty; it does not make money and it often sacrifices favourable moves (e.g. the airline forgoes cheap fuel in the down scenario). (c) describes a long option, not a hedge in general; (a) and (d) misunderstand hedging.

**D10. Which is the correct order of magnitude, largest to smallest, for a large swap book?**
(a) Market value > gross notional > net exposure
(b) Gross notional > gross market value > net exposure
(c) Net exposure > gross notional > market value
(d) They are all equal

**Answer: (b).** Gross notional is the largest headline figure; the gross market value (replacement cost) is a small fraction of it; and net exposure after offsetting opposite positions is smaller still. This ordering is exactly why the "$600 trillion" notional headline overstates risk.

---

## Self-Verification Note

Every Section B problem is reconciled inline (✔): B1 both scenarios lock ₹800/kg; B2 F₀ = ₹1,061.84 with ₹18.16 arbitrage; B3/B4 break-evens K + c = 520 and K − p = 485; B5 long + short sum to zero; B6 4% × 12.5× = 50%; B7/B8 use the parity gap ₹15.08 consistently; B9 daily MTM sums to ₹2,500; B10 ±₹150 vs the share. All formulas match the concept note's Quick-Reference (payoffs, F₀ = S₀·e^(rT), break-evens K ± premium, put-call parity, leverage = notional ÷ capital).
