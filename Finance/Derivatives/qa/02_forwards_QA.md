# Q&A — Forward Contracts

A companion practice bank for Chapter 02 (Forward Contracts). Every question is followed by a full worked answer. Numbers reconcile with the concept note. Work each problem yourself before reading the solution.

---

## Section A — Concept-check (short answer)

**A1. Define a forward contract in one sentence and name its four locked-in terms.**

A forward contract is a privately negotiated (OTC) agreement between two parties to buy or sell a specified asset, in a specified quantity, on a specified future date, at a price fixed today. The four locked-in terms are: (1) the underlying asset, (2) the quantity, (3) the delivery/maturity date *T*, and (4) the forward (delivery) price *K*. No money changes hands at inception.

**A2. Who is "long" and who is "short" a forward, and what does each lock in?**

The long party agrees to *buy* the asset at *T* and thereby locks in her *purchase* price. The short party agrees to *sell* the asset at *T* and locks in his *sale* price. Both give up optionality — each is *obligated*, not merely entitled.

**A3. Why is the forward price usually not equal to today's spot price?**

Because of the **cost of carry**. To be able to deliver the asset at *T*, the short can buy it today and carry it, incurring financing (interest at *r*) plus storage, minus any income the asset throws off. The forward price is the spot price grown by this net carry: *F₀ = S₀ (1 + net carry)*. No-arbitrage forces this exact relationship.

**A4. "The forward price is the market's forecast of the future spot price." True or false, and why?**

False. *F₀* is a purely mechanical, arbitrage-enforced function of *today's* spot and *today's* interest rate (and carry). It is not a prediction. Two traders with opposite views on where the asset will end up still agree on the same forward price, because carry — not opinion — sets it.

**A5. What does it cost to enter a forward, and when does cash actually move?**

It costs zero at inception — *K* is deliberately chosen so the contract is worth zero to both sides on day one. Cash moves only at maturity (physical delivery against payment of *K*, or a cash-settled net payoff). Any collateral/margin under a CSA is a credit mitigant, not a price.

**A6. Distinguish the forward *price* from the *value* of a forward.**

The **price** *K* is fixed at inception and never changes for that contract. The **value** starts at zero and drifts as spot moves: for a long forward on a no-income asset, value = *Sₜ − K e^{−r(T−t)}*. Confusing the two wrecks the credit-risk analysis, because credit exposure is driven by *value*, not by the fixed price.

**A7. Contango vs backwardation — define both.**

Contango is *F₀ > S₀* (the normal case, positive net carry from interest/storage). Backwardation is *F₀ < S₀*, arising when the asset has a high convenience yield, or in currencies when the foreign interest rate exceeds the domestic rate. Contango does not mean "the market is bullish" — it usually just reflects positive carry.

**A8. Why does a known income (dividend/coupon) *lower* the forward price?**

Because the holder of the *actual* asset receives that income while the forward buyer does not. The forward buyer is therefore willing to pay less. Formally *F₀ = (S₀ − I)(1 + rT)*, where *I* is the present value of the income — income is subtracted from carry.

**A9. What is the single defining hazard of an OTC forward that a futures contract removes?**

Counterparty (default) credit risk. A forward is bilateral with no clearing house guaranteeing performance and no daily margining, so losses accumulate over the whole life and land in one lump at *T*. Futures institutionalise this away via a clearing house plus daily mark-to-market and margin.

**A10. What is "wrong-way risk" on a forward?**

The tendency for your credit exposure to be largest exactly when the counterparty is most likely to default — i.e. after a violent market move that leaves your contract deeply in-the-money is precisely when the losing counterparty is most stressed. Exposure and default probability correlate badly.

---

## Section B — Numerical / payoff problems (full working, reconciled)

**B1. Price a 6-month forward on a non-dividend share. Spot S₀ = INR 500, r = 8% p.a., T = 0.5.**

Using discrete simple interest, *F₀ = S₀(1 + rT) = 500 × (1 + 0.08 × 0.5) = 500 × 1.04 = **INR 520.00**.*

*Arbitrage self-check.* Suppose a dealer quotes 530 (too high). Today: borrow 500 at 8%, buy the share, short the forward at 530 — net cash today 0. At *T*: deliver the share, receive 530, repay 500 × 1.04 = 520. Net = +10 risk-free from zero investment. That free lunch proves 530 is wrong; arbitrage drives *F* to 520, where the net at *T* is exactly 0. Formula reconciles with the no-arbitrage table. ✔

**B2. Same share, now with a dividend. It pays INR 12 at t = 0.25. Re-price the 6-month forward.**

Present value of the dividend at 8%: *I = 12 / (1 + 0.08 × 0.25) = 12 / 1.02 = INR 11.76.*
Then *F₀ = (S₀ − I)(1 + rT) = (500 − 11.76) × 1.04 = 488.24 × 1.04 = **INR 507.77**.*

*Sense check.* The dividend lowers the forward from 520 to ≈ 507.77 — a drop of ≈ 12.23, which is roughly the dividend grown to maturity (12 × 1.02 ≈ 12.24). Correct direction and magnitude. ✔

**B3. Price a 3-month USD/INR forward. Spot = INR 83.00/USD, domestic r_d = 7% p.a., foreign r_f = 5% p.a., T = 0.25.**

Covered interest rate parity (discrete):
*F₀ = S₀ (1 + r_d T) / (1 + r_f T) = 83.00 × (1 + 0.07 × 0.25) / (1 + 0.05 × 0.25) = 83.00 × 1.0175 / 1.0125 = 83.00 × 1.004938 = **INR 83.41/USD**.*

The rupee trades at a forward premium on USD (domestic rate exceeds foreign), so USD is "expensive" forward — contango. ✔

**B4. Build the payoff/reconciliation table for the exporter who shorts the USD forward of B3 at K = 83.41 on USD 1,000,000.**

For a short forward the forward payoff is *(K − Sₜ) × quantity*. Total proceeds = market conversion + forward payoff.

| Realised Sₜ (INR/USD) | Market sale of 1m USD (INR cr) | Forward payoff (K − Sₜ)×1m (INR cr) | Total locked (INR cr) |
|---:|---:|---:|---:|
| 80.00 | 8.000 | +0.341 | **8.341** |
| 82.00 | 8.200 | +0.141 | **8.341** |
| 83.41 | 8.341 | 0.000 | **8.341** |
| 85.00 | 8.500 | −0.159 | **8.341** |
| 88.00 | 8.800 | −0.459 | **8.341** |

*Reconciliation.* Every row totals **INR 8.341 crore = K × quantity**. When the rupee strengthens to 80 the poor market conversion is topped up by the +0.341 cr forward gain; when it weakens to 88 the market windfall is clawed back by the −0.459 cr forward loss. Certainty achieved at the cost of upside. The bank's mirror long position earns exactly the negative of the forward column — a zero-sum outcome. ✔

**B5. A biscuit maker will buy 100 tonnes of wheat in 3 months. Spot = INR 25,000/t, r = 6% p.a., PV of storage = INR 200/t, T = 0.25. Price the forward and state the locked purchase cost.**

Storage adds to carry (treat like negative income — add its future value):
*F₀ = (S₀ + PV storage)(1 + rT) = (25,000 + 200)(1 + 0.06 × 0.25) = 25,200 × 1.015 = **INR 25,578/tonne**.*
Locked purchase cost for 100 t = **INR 25.578 lakh**. The firm fears rising prices, so it goes **long** the forward.

**B6. Build the hedge reconciliation table for B5 (long forward, K = 25,578).**

Long forward payoff = *(Sₜ − K) × 100*. Net effective cost = market purchase cost − forward gain.

| Sₜ (INR/t) | Buy 100 t in market (INR lakh) | Forward payoff (Sₜ − K)×100 (INR lakh) | Net effective cost (INR lakh) |
|---:|---:|---:|---:|
| 23,000 | 23.000 | −2.578 | **25.578** |
| 25,578 | 25.578 | 0.000 | **25.578** |
| 28,000 | 28.000 | +2.422 | **25.578** |

*Reconciliation.* Net effective cost is **INR 25.578 lakh in every scenario**. A long forward converts a variable purchase cost into a fixed one; the forward gain when prices rise offsets the higher market cost. ✔

**B7. Default twist on B6. Wheat rises to Sₜ = 28,000 and the short (grain trader) defaults. Quantify the loss.**

At 28,000 the biscuit maker's long forward is in-the-money by *(28,000 − 25,578) × 100 = INR 2.422 lakh*, which the counterparty owes. On default the firm loses that INR 2.422 lakh and must buy wheat in the open market at 28,000 — its cost jumps from the hedged 25.578 lakh to the unhedged **28.000 lakh**, a **2.422 lakh** loss versus plan. Default bites precisely when the contract has moved in your favour (wrong-way risk), and an OTC forward gives no clearing house to fall back on. An exchange-traded future with daily margin would have collected the gain in cash day-by-day, keeping default exposure near zero. ✔

**B8. Value an existing long forward mid-life. You are long a 1-year forward on a non-income share struck at K = 520. Six months later the share is at Sₜ = 540 and r = 8% p.a. What is the contract now worth?**

*f_long = Sₜ − K e^{−r(T−t)}*, with remaining time *T − t = 0.5*.
Discount factor *e^{−0.08 × 0.5} = e^{−0.04} = 0.960789.*
*f_long = 540 − 520 × 0.960789 = 540 − 499.61 = **INR 40.39** (positive — in-the-money to the long).*

*Cross-check via the forward-price form.* Current fair 6-month forward *Fₜ = 540 × e^{0.04} = 540 × 1.040811 = 562.04.* Then *f_long = (Fₜ − K)e^{−r(T−t)} = (562.04 − 520) × 0.960789 = 42.04 × 0.960789 = INR 40.39.* Both routes agree. ✔ This INR 40.39 is exactly the biscuit-maker-style credit exposure the short now owes the long.

---

## Section C — Interview-style (model answers)

**C1. "Walk me through why a forward price equals spot times one-plus-carry, using an arbitrage argument."**

Model answer: Take the short's replication. To guarantee delivery of the asset at *T*, I can buy it today at *S₀* — funded by borrowing at the risk-free rate *r* — and carry it, paying storage and receiving any income along the way. My total outlay grown to *T* is *S₀* plus net carry. If the forward were quoted above that, I would buy spot, short the forward, deliver at maturity, repay my loan, and pocket the difference risk-free with zero capital. Everyone piling into that trade pushes spot up and the forward down until the gap closes. The mirror (reverse cash-and-carry: short the asset, invest the proceeds, buy the forward) disciplines the price from below. The only quote that admits no free lunch is *F₀ = S₀(1 + net carry)*. The forward price is enforced by arbitrage off today's spot and rate — it is not a forecast.

**C2. "A CFO says: 'Hedging with forwards is pointless — half the time the rupee moves my way and I lose money on the hedge.' How do you respond?"**

Model answer: The CFO is confusing *outcome variance* with *risk*. A hedge is not a bet that pays off; it is the deliberate purchase of *certainty*. By shorting a USD forward the exporter locks total proceeds at K × quantity — say INR 8.341 crore — no matter where the rupee lands. Yes, if the rupee weakens the forward shows a "loss," but that loss is exactly offset by a better market conversion, so the firm is no worse off than planned. The firm is not in the business of forecasting currencies; it gave up the upside precisely to remove the downside that could threaten payroll and supplier payments. Judging a hedge by whether the derivative leg alone made money is the wrong scorecard — you judge the *combined* position, which is fixed by design.

**C3. "What are the risks that a forward *introduces* even as it removes price risk?"**

Model answer: Three. First, **counterparty/default risk** — being bilateral and OTC with no clearing house and no daily margin, losses accumulate to a lump at maturity, and the in-the-money party carries an uncollateralised claim. Second, **loss of upside / opportunity cost** — the hedger forgoes favourable price moves; a forward is symmetric, unlike an option. Third, **illiquidity / no easy exit** — a custom contract cannot simply be sold; to unwind you negotiate a tear-up with the same counterparty or take an offsetting forward with a third party, leaving two contracts and two counterparties. So risk is transferred and transformed, not deleted. Mitigants: ISDA Master Agreement with a Credit Support Annex requiring collateral, netting, and dealing only within credit limits with high-rated names.

**C4. "How would you construct a synthetic long forward from options, and why does it matter?"**

Model answer: By put-call parity, *long call + short put at the same strike K and maturity = a long forward at K*. Their combined payoff is *max(Sₜ − K, 0) − max(K − Sₜ, 0) = Sₜ − K*, which is exactly the long-forward payoff — linear, unlimited, break-even at K. It matters because it shows forwards are the linear backbone from which option payoffs are assembled, it lets a desk manufacture forward exposure when the forward market is illiquid but options trade, and it is the arbitrage relationship that keeps call, put, and forward prices mutually consistent.

**C5. "Explain the difference between a forward and a futures contract in under a minute."**

Model answer: A future is a forward that has been standardised, exchange-traded, and centrally cleared with daily mark-to-market and margining. A forward is a custom OTC deal — any size, any date — settling entirely at maturity, carrying bilateral counterparty risk and low liquidity. Futures trade fixed contract sizes and dates, so they are highly liquid and essentially free of default risk because the clearing house is the counterparty and daily margin keeps exposure near zero, but you sacrifice flexibility and face daily cash-flow variability from margin calls. When interest rates are deterministic, forward and futures prices are theoretically equal.

---

## Section D — MCQs (with reasoning)

**D1. At inception, the value of a forward contract to each party is:**
(a) equal to the spot price  (b) equal to the forward price  (c) zero  (d) the present value of the forward price

**Answer: (c).** *K* is set equal to the fair forward price *F₀* precisely so the contract is worth zero to both sides on day one; no premium is exchanged. (a) and (b) confuse value with price; (d) misapplies discounting.

**D2. A stock pays a known dividend before a forward matures. Relative to an identical non-dividend stock, the forward price is:**
(a) higher  (b) lower  (c) unchanged  (d) indeterminate

**Answer: (b).** Income is subtracted from carry: *F₀ = (S₀ − I)(1 + rT)*. The holder of the actual share receives the dividend that the forward buyer does not, so the forward should cost less.

**D3. An exporter will receive USD in three months and wants certainty. She should:**
(a) go long a USD forward  (b) go short a USD forward  (c) buy a USD call  (d) do nothing

**Answer: (b).** Her natural exposure is "receive/sell the asset later," so she is hurt if USD falls; she hedges by shorting the forward to lock the sale price. Hedge the *opposite* of your natural exposure. (a) doubles the exposure; (c) is a right, not the requested lock, and costs a premium.

**D4. The payoff to a short forward with delivery price K when the spot at maturity is Sₜ equals:**
(a) Sₜ − K  (b) K − Sₜ  (c) max(K − Sₜ, 0)  (d) max(Sₜ − K, 0)

**Answer: (b).** The short locked in a sale at K; profit is *K − Sₜ*, the mirror image of the long's *Sₜ − K*. (c) and (d) are *option* payoffs — a forward has no truncation at zero.

**D5. "Contango" describes a market in which:**
(a) F₀ < S₀  (b) F₀ = S₀  (c) F₀ > S₀  (d) the market expects prices to fall

**Answer: (c).** Contango is forward above spot, the normal case driven by positive net carry (interest plus storage). (a) is backwardation. (d) is wrong — contango reflects carry, not a directional forecast.

**D6. For a currency forward under covered interest rate parity, if the domestic interest rate exceeds the foreign rate, the foreign currency trades at a:**
(a) forward discount  (b) forward premium  (c) flat forward  (d) it depends on spot

**Answer: (b).** *F₀ = S₀ (1 + r_d T)/(1 + r_f T)*; with *r_d > r_f* the ratio exceeds 1, so the foreign currency is more expensive forward — a forward premium (contango), exactly as in the 83.00 → 83.41 USD/INR example.

**D7. Counterparty credit exposure on an existing forward is largest when:**
(a) the contract is deeply out-of-the-money to you  (b) at inception  (c) the contract is deeply in-the-money to you  (d) it never changes

**Answer: (c).** Exposure equals the contract's positive value to you; when the trade is deeply in-the-money the counterparty owes you the most and their default costs the most. This is the wrong-way-risk concern. At inception (b) value is zero, so exposure is zero.

**D8. Which single feature most distinguishes a forward from a futures contract?**
(a) forwards are riskier assets  (b) forwards are OTC/bilateral with no daily margining, futures are exchange-cleared with daily mark-to-market  (c) forwards always cost a premium  (d) futures cannot be used to hedge

**Answer: (b).** The defining structural difference is standardisation plus central clearing and daily margin. (c) is false — neither charges a premium. (d) is false — futures are core hedging tools.

---

## Self-verification notes

- B1 (520.00), B2 (507.77), B3 (83.41), B5 (25,578), B8 (40.39) recomputed and cross-checked against the concept note — all match.
- B4 and B6 tables confirm the total locked outcome is constant across all spot scenarios (8.341 cr; 25.578 lakh), the acid test of a correct hedge.
- B8 verified by two independent routes, both yielding INR 40.39. Payoff signs checked: long = Sₜ − K, short = K − Sₜ, summing to zero.
