# Q&A — Futures Pricing and Hedging

A practice bank built around the *why*: every price you compute here is enforced by an arbitrage. If a futures price drifts away from its fair value, someone can borrow, trade the spot, carry it, and lock a riskless profit. Hedging is the mirror image — you deliberately take an offsetting futures position so that whatever the spot does to you, the future undoes.

---

## Section A — Concept Check

**A1. What is the cost-of-carry model, and why must the futures price obey it?**

The cost-of-carry model says the fair futures price equals today's spot price grown forward at the *net* cost of holding the asset until delivery:

F₀ = S₀ × (1 + r − q)^T (discrete) or F₀ = S₀ × e^(r − q)T (continuous),

where r is the financing rate, q is any yield the asset throws off (dividends, convenience, storage netted in). It must hold because a future is just a delayed purchase. Buying the asset now and financing it, versus buying the future and holding cash, must cost the same by delivery — otherwise the cheaper route is a free lunch. Arbitrage, not opinion, pins the price.

**A2. Distinguish "cash-and-carry" from "reverse cash-and-carry" arbitrage.**

Cash-and-carry is triggered when the future is *too expensive* (F > fair). You borrow cash, buy the asset spot, carry it, and simultaneously sell the future; at expiry you deliver the asset and repay the loan, pocketing the overpricing. Reverse cash-and-carry is triggered when the future is *too cheap* (F < fair). You short-sell the asset spot, invest the proceeds, and buy the future; at expiry you take delivery and return the borrowed asset. Each strategy locks a profit independent of where the spot finishes.

**A3. Define contango and backwardation. Which is "normal" for a financial asset?**

Contango is F > S (the futures curve slopes up); backwardation is F < S (it slopes down). For a pure financial asset with no yield, positive interest rates force F > S, so contango is the natural state. Backwardation appears when the asset pays a yield larger than the financing rate — a high dividend stock, or a commodity with a large convenience yield (people pay a premium to hold the physical good now).

**A4. What is basis, and why does basis risk defeat a "perfect" hedge?**

Basis = Spot price − Futures price. A hedge is perfect only if you can close it exactly at expiry, when basis converges to zero. In practice you often lift the hedge early, or you hedge an exposure whose asset differs slightly from the futures' deliverable (a cross-hedge). Then the basis at unwind is unknown, and that residual uncertainty — basis risk — is what survives an otherwise well-sized hedge.

**A5. Explain the minimum-variance hedge ratio. Why is it rarely exactly 1.0?**

The minimum-variance hedge ratio is h* = ρ × (σ_S / σ_F), the beta of spot returns on futures returns. It answers "how many units of futures per unit of exposure minimises the variance of my hedged position?" It equals 1.0 only when spot and futures move one-for-one. It deviates because the two have different volatilities or imperfect correlation — a jet-fuel buyer hedging with crude futures, for instance, uses h* well away from 1 because fuel and crude are correlated but not identical.

**A6. Why does convergence guarantee that basis goes to zero at expiry?**

At the delivery instant, the future *is* a spot transaction — holding it means receiving/delivering the asset immediately. There is no more carry period, so cost of carry collapses to zero and F must equal S. If it did not, you would buy the cheaper and sell the dearer for an instant, riskless gain. That no-arbitrage pressure is what drags basis to zero as expiry nears.

**A7. What is a "tailed" hedge, and why does daily marking-to-market create the need for it?**

Futures are marked to market daily, so gains and losses are realised (and can be reinvested or must be financed) before expiry, whereas a forward settles once at the end. That timing mismatch means a naive one-for-one futures hedge slightly over-hedges. Tailing multiplies the hedge quantity by a discount factor (≈ 1/(1+r)^t) so the present value of futures gains matches the exposure. It is a second-order correction, but real for large books.

---

## Section B — Numerical / Payoff Problems

**B1. Fair futures price of a non-dividend stock (discrete).**

*Given:* Spot S₀ = ₹1,000; risk-free rate r = 8% p.a.; maturity T = 6 months.

Step 1 — Time fraction: T = 0.5 years.
Step 2 — Apply cost of carry: F₀ = 1,000 × (1 + 0.08)^0.5.
Step 3 — (1.08)^0.5 = 1.03923.
Step 4 — F₀ = 1,000 × 1.03923 = **₹1,039.23**.

*Reconcile:* No dividend, positive rate, so the future must sit above spot (contango) — ₹1,039 > ₹1,000. Good.

**B2. Cash-and-carry arbitrage when the future is mispriced.**

*Given:* Using B1, the 6-month future trades in the market at ₹1,060 (above fair ₹1,039.23).

Step 1 — Future is overpriced → cash-and-carry. Sell the future at ₹1,060; borrow ₹1,000 at 8% and buy the stock now.
Step 2 — Loan repayment at 6 months = 1,000 × 1.03923 = ₹1,039.23.
Step 3 — At expiry deliver the stock into the short future, receive the locked ₹1,060.
Step 4 — Arbitrage profit = 1,060 − 1,039.23 = **₹20.77 per share**, riskless.

*Reconcile:* The profit equals exactly the mispricing (1,060 − 1,039.23). Where the stock finishes is irrelevant — that is the signature of a true arbitrage.

**B3. Fair price with a discrete dividend.**

*Given:* S₀ = ₹1,000; r = 8% p.a.; T = 6 months; a dividend of ₹15 is paid in 3 months.

Step 1 — Remove the present value of the dividend from spot first. PV(div) = 15 / (1.08)^0.25.
Step 2 — (1.08)^0.25 = 1.01943, so PV(div) = 15 / 1.01943 = ₹14.71.
Step 3 — Investable spot = 1,000 − 14.71 = ₹985.29.
Step 4 — F₀ = 985.29 × (1.08)^0.5 = 985.29 × 1.03923 = **₹1,024.94**.

*Reconcile:* A holder of the future forgoes the ₹15 dividend the stockholder collects, so the fair future must be *lower* than the no-dividend ₹1,039.23. It is (₹1,024.94). Consistent.

**B4. Continuous compounding with a dividend yield.**

*Given:* Index spot S₀ = 20,000; continuous r = 7% p.a.; continuous dividend yield q = 2% p.a.; T = 3 months.

Step 1 — Net carry = r − q = 0.05; time = 0.25.
Step 2 — Exponent = 0.05 × 0.25 = 0.0125.
Step 3 — e^0.0125 = 1.012578.
Step 4 — F₀ = 20,000 × 1.012578 = **20,251.6 index points**.

*Reconcile:* Financing (7%) exceeds yield (2%), net carry positive, so future > spot. 20,252 > 20,000. Good.

**B5. Number of contracts to hedge an equity portfolio.**

*Given:* Portfolio value = ₹5,00,00,000 (₹5 crore); portfolio beta = 1.2; index future price = 20,000 points; contract multiplier = ₹50 per point. You fear a market fall and want to fully hedge.

Step 1 — Value of one futures contract = 20,000 × 50 = ₹10,00,000.
Step 2 — Beta-adjusted exposure = portfolio value × beta = 5,00,00,000 × 1.2 = ₹6,00,00,000.
Step 3 — Contracts N = beta-adjusted exposure ÷ contract value = 6,00,00,000 ÷ 10,00,000 = **60 contracts, sold short**.

*Reconcile check:* If the index drops 10%, a β=1.2 portfolio loses ≈ 12% × ₹5 cr = ₹60,00,000. The 60 short futures gain 60 × (2,000 points × ₹50) = 60 × 1,00,000 = ₹60,00,000. Losses and gains cancel — the hedge is correctly sized.

**B6. Adjusting portfolio beta with futures (not full hedge).**

*Given:* Same portfolio (₹5 cr, β = 1.2). You want to *lower* target beta to 0.8, not zero.

Step 1 — Contracts required N = (β_target − β_current) × Portfolio ÷ Contract value.
Step 2 — N = (0.8 − 1.2) × 5,00,00,000 ÷ 10,00,000 = (−0.4 × 5,00,00,000) ÷ 10,00,000.
Step 3 — = −2,00,00,000 ÷ 10,00,000 = **−20 contracts (sell 20)**.

*Reconcile:* Sign is negative → sell futures, which reduces beta. Full hedge to β = 0 would need (0 − 1.2) route = −60 contracts, matching B5. Selling only 20 lands you partway, at β = 0.8. Internally consistent.

**B7. Minimum-variance hedge ratio and optimal contract count.**

*Given:* An airline must buy 10,00,000 gallons of jet fuel in 3 months. It hedges with heating-oil futures (42,000 gallons each). σ_spot (fuel) = 0.032, σ_futures (heating oil) = 0.040, correlation ρ = 0.80.

Step 1 — h* = ρ × (σ_S / σ_F) = 0.80 × (0.032 / 0.040) = 0.80 × 0.80 = 0.64.
Step 2 — Quantity to hedge = h* × exposure = 0.64 × 10,00,000 = 6,40,000 gallons.
Step 3 — Contracts N = 6,40,000 ÷ 42,000 = 15.24 → **round to 15 contracts, long** (buying fuel, so hedge long).

*Reconcile:* h* < 1 because the two commodities are imperfectly correlated and futures are more volatile than spot; over-hedging one-for-one would add variance rather than remove it. A long hedge is right because the airline is short fuel (needs to buy). Consistent.

**B8. Basis and the outcome of an early-unwound hedge.**

*Given:* On 1 March a miller shorts wheat futures at ₹2,250/quintal to hedge grain it will sell in May. Spot on 1 March = ₹2,200 (basis = 2,200 − 2,250 = −₹50). On the May sale date, spot = ₹2,100 and futures = ₹2,130 (basis = −₹30).

Step 1 — Spot sale proceeds = ₹2,100.
Step 2 — Futures gain (short) = entry − exit = 2,250 − 2,130 = +₹120.
Step 3 — Effective realised price = spot sale + futures gain = 2,100 + 120 = **₹2,220/quintal**.
Step 4 — Cross-check via basis rule: effective price = futures entry price + ending basis = 2,250 + (−30) = ₹2,220. Same answer.

*Reconcile:* The miller locked roughly the ₹2,250 futures level, adjusted by the basis change. Basis strengthened from −50 to −30 (up ₹20), and indeed the realised ₹2,220 beats the naive expectation of ₹2,200 by ₹20. Basis risk is exactly this ₹20 uncertainty. Both methods agree.

**B9. Convergence — verifying basis to zero at expiry.**

*Given:* S₀ = 20,000, F₀ = 20,251.6 (from B4), T = 3 months. Show basis at t = 0 and t = T assuming spot is unchanged at expiry.

Step 1 — Basis at t = 0 = S − F = 20,000 − 20,251.6 = −251.6 points.
Step 2 — At expiry the carry period is zero, so F_T = S_T. If spot is still 20,000, F_T = 20,000.
Step 3 — Basis at expiry = 20,000 − 20,000 = **0**.

*Reconcile:* The −251.6 opening basis is precisely the carry cost (net financing over 3 months). It bleeds to zero as the future ages, which is why a hedge held to expiry has no basis risk. Correct.

---

## Section C — Interview-Style (Model Answers)

**C1. "A stock future is trading above its cost-of-carry fair value. Walk me through how you'd make riskless money."**

*Model answer:* I would run a cash-and-carry. The future is dear relative to spot, so I sell the future and simultaneously buy the underlying stock, financing the purchase by borrowing at the risk-free rate. I now hold the stock, owe interest, and am committed to deliver at the locked futures price. At expiry I hand over the shares, collect the futures price, and repay principal plus interest. Because the futures price exceeds spot-plus-carry, the delivery proceeds more than cover my loan, and the surplus is exactly the mispricing. Crucially it does not matter where the stock trades at expiry — I am fully hedged both ways — which is what makes it arbitrage rather than a bet. In reality transaction costs, borrowing spreads, and dividend uncertainty define a no-arbitrage *band*; I only trade when the mispricing clears that band.

**C2. "Your equity portfolio is fully hedged with index futures, yet you still lost money last quarter. How?"**

*Model answer:* Two usual suspects. First, basis risk: index futures hedge market (systematic) risk, not the stock-specific risk of my particular holdings. If my names underperformed the index, the hedge protected against the market move but not the relative underperformance — my portfolio beta captures average sensitivity, not idiosyncratic drift. Second, beta instability: I sized the hedge on an estimated beta, and if realised beta differed, the hedge was mis-sized. There is also the rolling and marking-to-market cost — if I rolled contracts through a steep contango, each roll bled a little. A "full hedge" removes market direction, not tracking error, financing drag, or estimation error.

**C3. "When would you deliberately choose a cross-hedge even though a direct future exists?"**

*Model answer:* Liquidity and cost usually. If the direct future is thinly traded, its bid-ask and slippage can exceed the basis risk I take on by using a deep, liquid, closely-correlated proxy — for example hedging a corporate bond position with liquid government-bond futures, or a regional jet-fuel exposure with the benchmark crude or heating-oil contract. I accept some basis risk to gain execution certainty and tighter spreads. I would size it with the minimum-variance hedge ratio, h* = ρ σ_S/σ_F, so the correlation and relative volatility are explicitly priced into the contract count rather than assuming one-for-one.

**C4. "Explain backwardation to a non-specialist and tell me what it signals."**

*Model answer:* Backwardation is when a futures contract for later delivery is *cheaper* than buying the thing today. That seems odd — you would expect to pay extra for storage and financing — but it happens when holding the physical asset gives you a benefit greater than that cost. For a commodity that means a convenience yield: a refiner short of crude will pay a premium to have oil now rather than in three months, pushing spot above futures. For a stock it means the dividend yield exceeds the financing rate. So backwardation signals scarcity or a strong yield-of-holding today, and it is often read as a bullish, tight-supply condition in commodity markets.

**C5. "Forwards and futures on the same asset — when do their fair prices actually diverge?"**

*Model answer:* Under deterministic interest rates they are theoretically equal. They diverge when interest rates are stochastic and correlated with the asset price, because futures are marked to market daily. If the asset tends to rise when rates rise, a long futures holder banks daily gains and reinvests them at now-higher rates, and finances losses when rates are lower — a systematic advantage that makes the futures price slightly higher than the forward. Negative correlation reverses it. For short maturities and typical assets the gap is tiny and ignored, but for long-dated interest-rate products it is material, which is why practitioners apply a convexity adjustment.

---

## Section D — MCQs with Reasoning

**D1.** The fair futures price of a non-dividend-paying stock, relative to spot, is:
A) Always below spot
B) Always above spot when interest rates are positive
C) Equal to spot
D) Independent of interest rates

**Answer: B.** With no yield to offset financing, F = S(1+r)^T > S whenever r > 0. A) and C) ignore carry; D) is wrong because r directly drives the carry. This is why financial futures are normally in contango.

**D2.** Basis is defined as:
A) Futures price − Spot price
B) Spot price − Futures price
C) Spot price − Strike price
D) Futures price − Fair value

**Answer: B.** Basis = Spot − Futures, and it converges to zero at expiry. A) is the sign-flipped convention some texts use for "spread" but the standard hedging definition is B; C) confuses futures with options; D) describes mispricing, not basis.

**D3.** A portfolio manager holds ₹5 cr with beta 1.2 and shorts the exact beta-adjusted number of index futures. Immediately after, the portfolio's market exposure is approximately:
A) Beta 1.2
B) Beta 0.6
C) Beta 0
D) Beta −1.2

**Answer: C.** A full beta-adjusted short hedge neutralises systematic exposure, taking effective beta to ~0. It does not flip to negative (that would be over-hedging, D), nor leave it unchanged (A). Residual idiosyncratic risk remains, but market beta is ~0.

**D4.** The minimum-variance hedge ratio h* = ρ(σ_S/σ_F) equals 1.0 only when:
A) Correlation is zero
B) Spot and futures volatilities are equal and correlation is 1
C) The futures is more volatile than spot
D) The asset pays no dividend

**Answer: B.** h* = 1 requires ρ = 1 and σ_S = σ_F simultaneously. A) gives h* = 0; C) makes σ_S/σ_F < 1 so h* < 1 (all else equal); D) is unrelated to the hedge ratio. Only B satisfies the algebra.

**D5.** A market is in backwardation. This is most consistent with:
A) Zero dividends and positive rates
B) A dividend/convenience yield exceeding the financing rate
C) Storage costs exceeding all other factors
D) The future being mispriced above fair value

**Answer: B.** Backwardation (F < S) needs net carry negative, i.e. yield q > r. A) produces contango; C) storage cost raises F, pushing toward contango; D) confuses a curve shape with an arbitrage. Only B drives F below S on a fair-value basis.

**D6.** A hedge held all the way to the futures' expiry has essentially no basis risk because:
A) Marking-to-market is suspended near expiry
B) Convergence forces the futures price to equal spot at delivery
C) Correlation always rises to 1 near expiry
D) Transaction costs vanish at expiry

**Answer: B.** At delivery the carry period is zero, so F = S — basis is zero by construction, eliminating the residual uncertainty. A) and D) are false; C) is not guaranteed and is not the mechanism. Basis risk is a problem only for hedges lifted *early*.

**D7.** In a cash-and-carry arbitrage, the arbitrageur's profit at expiry is:
A) Dependent on the terminal spot price
B) Equal to the observed mispricing, independent of terminal spot
C) Larger if the spot rises
D) Zero if rates are positive

**Answer: B.** The whole point of arbitrage is that both legs are locked, so terminal spot cancels out and the profit equals the initial mispricing (see B2: ₹20.77). A) and C) describe a directional bet, not arbitrage; D) is nonsense — positive rates are already inside the fair value.

---

## Self-Verification Notes

- B1 (₹1,039.23) is reused as the arbitrage benchmark in B2; the ₹20.77 profit equals 1,060 − 1,039.23 exactly.
- B3 dividend case (₹1,024.94) correctly sits below the no-dividend B1 value, as theory demands.
- B5 (60 contracts) is validated by an independent P&L cancellation check; B6 (20 contracts for β 0.8) reconciles with it.
- B8 effective price ₹2,220 is confirmed by two independent methods (spot + futures P&L, and entry + ending basis).
- MCQ answers cross-reference the worked numbers (D7↔B2, D3↔B5, D6↔B9). No internal contradictions found.
