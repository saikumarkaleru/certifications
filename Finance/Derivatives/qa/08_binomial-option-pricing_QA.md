# Q&A — Binomial Option Pricing

Practice bank for Chapter 08. Every question is followed by a full worked answer. Attempt each one before reading the solution. Notation: S₀ = spot, u/d = up/down gross moves, K = strike, R = one-period gross risk-free factor (R = e^(rΔt) or 1 + r), p = risk-neutral up-probability, Δ = hedge ratio (delta).

---

## Section A — Concept Check

**A1. What is the single core idea that lets the binomial model price an option without knowing the stock's real expected return?**

Replication. Over one period the stock can only reach two values, so a portfolio of the stock plus borrowing/lending has exactly two future values too. Choose the holdings so those two values match the option's two payoffs, and the portfolio *is* the option. By no-arbitrage the option must cost what the replicating portfolio costs today — and that cost depends on u, d, R and the payoffs, never on the stock's real drift. The real-world probability of an up-move never enters.

**A2. Write the one-period risk-neutral probability and state the no-arbitrage condition it requires.**

p = (R − d)/(u − d), with the option value C = [p·C_u + (1 − p)·C_d]/R. For p to be a valid probability (strictly between 0 and 1) we need d < R < u. If R ≤ d the risk-free asset is dominated by the stock's worst case (arbitrage); if R ≥ u the stock never beats cash (arbitrage). So d < R < u is exactly the no-arbitrage band.

**A3. Why is p called "risk-neutral" rather than the true probability?**

Under p the stock's expected gross return equals the risk-free factor: p·u + (1 − p)·d = R. That is only true in a world where investors demand no risk premium — a risk-neutral world. We are not claiming the world is risk-neutral; we are exploiting the fact that a replicable payoff can be valued *as if* it were, because arbitrage pins the price regardless of anyone's risk preferences.

**A4. Give the delta (hedge ratio) formula and its interpretation.**

Δ = (C_u − C_d)/(S_u − S_d) = (C_u − C_d)/(S₀(u − d)). It is the number of shares that makes a share-plus-borrowing portfolio replicate the option — the sensitivity of option value to the stock price, the slope of the payoff. A call has 0 ≤ Δ ≤ 1; a put has −1 ≤ Δ ≤ 0. It is also the ratio for delta-hedging: short one call, hold Δ shares, and the position is riskless over the step.

**A5. Two ways to get the same one-period price — name them and say why they agree.**

(1) Risk-neutral valuation: discount the p-weighted expected payoff at R. (2) Replicating portfolio: value Δ shares plus the cash/bond position that reproduces the payoffs. They are algebraically the same equation rearranged, so they always give an identical price. The risk-neutral route is faster for multi-step trees; the replication route makes the no-arbitrage logic explicit.

**A6. In the Cox-Ross-Rubinstein (CRR) parameterisation, how are u and d chosen?**

u = e^(σ√Δt) and d = 1/u = e^(−σ√Δt), so the tree is symmetric in log-space and recombines (an up-then-down equals a down-then-up). σ is the annualised volatility and Δt the length of one step in years. This choice matches the variance of log-returns of the continuous (lognormal) model, so as the number of steps → ∞ the binomial price converges to Black-Scholes.

**A7. What does "recombining tree" mean and why does it matter computationally?**

With d = 1/u, an up move followed by a down move lands on the same node as down-then-up (S₀·u·d = S₀). So an n-step tree has only n + 1 terminal nodes instead of 2ⁿ paths. Cost grows linearly, not exponentially, which is what makes multi-step and American pricing tractable.

**A8. How does the binomial method handle an American option, and why can't Black-Scholes do the same directly?**

At every node you compare the *continuation value* (the discounted risk-neutral expectation of the next step) with the *immediate exercise value* (intrinsic value now) and take the larger. Working backward, this captures the optimal early-exercise decision at each node. Closed-form Black-Scholes assumes exercise only at expiry, so it cannot price the early-exercise right; the binomial lattice's node-by-node structure is exactly what accommodates it.

**A9. For which options does early exercise (and hence a binomial vs Black-Scholes gap) actually matter?**

American puts (deep in-the-money, where getting K now and earning interest beats waiting) and American calls on dividend-paying stocks (exercise just before a dividend to capture it). An American call on a *non-dividend* stock is never exercised early, so it equals the European call and the lattice reproduces Black-Scholes with no early-exercise premium.

**A10. As the number of steps increases, what happens to the binomial price?**

It converges to the continuous-time (Black-Scholes) price for a European option, oscillating as it converges. More steps refine the terminal distribution from a coarse two-point spread toward the lognormal. For practical accuracy a few hundred steps usually suffice; the binomial model is essentially a discrete approximation of the same risk-neutral valuation principle.

---

## Section B — Numerical / Pricing Problems

**B1. One-period call — both methods, full reconciliation.** S₀ = 100, u = 1.2, d = 0.9, R = 1.05, K = 100 (European call). Price it by risk-neutral valuation and by replication, and confirm they match.

Stock: S_u = 120, S_d = 90. Payoffs: C_u = max(120 − 100, 0) = 20, C_d = max(90 − 100, 0) = 0.

Risk-neutral probability: p = (R − d)/(u − d) = (1.05 − 0.9)/(1.2 − 0.9) = 0.15/0.30 = 0.5.
C = [p·C_u + (1 − p)·C_d]/R = [0.5·20 + 0.5·0]/1.05 = 10/1.05 = **9.5238**.

Replication: Δ = (C_u − C_d)/(S_u − S_d) = (20 − 0)/(120 − 90) = 20/30 = 0.6667 shares.
Cash M (lend +, borrow −) from the up equation Δ·S_u + M·R = C_u → 0.6667·120 + 1.05M = 20 → 80 + 1.05M = 20 → M = −57.1429 (borrow 57.14).
Check down: Δ·S_d + M·R = 0.6667·90 − 57.1429·1.05 = 60 − 60 = 0 = C_d. ✓
Portfolio cost today = Δ·S₀ + M = 0.6667·100 − 57.1429 = 66.6667 − 57.1429 = **9.5238**. ✓ Identical to the risk-neutral price.

**B2. Companion put + parity check.** Same tree as B1. Price the European put K = 100 and verify put-call parity.

Payoffs: P_u = max(100 − 120, 0) = 0, P_d = max(100 − 90, 0) = 10.
P = [p·P_u + (1 − p)·P_d]/R = [0.5·0 + 0.5·10]/1.05 = 5/1.05 = **4.7619**.
Parity: C − P should equal S₀ − K/R = 100 − 100/1.05 = 100 − 95.2381 = 4.7619.
Direct: C − P = 9.5238 − 4.7619 = 4.7619. ✓ Parity holds, confirming both prices are consistent.

**B3. Show that the real probability is irrelevant.** In B1, suppose the true up-probability is 0.7 (bullish) instead of, say, 0.4. Does the call price change?

No. The call price 9.5238 was computed entirely from u, d, R and the payoffs via p = 0.5 — the *risk-neutral* probability, fixed by no-arbitrage. The subjective real-world probability (0.7 or 0.4) never appears in either the risk-neutral formula or the replication argument. A bull and a bear who agree on u, d and R must agree on the option's arbitrage-free price. This is the model's headline lesson.

**B4. Two-period European call.** S₀ = 100, u = 1.1, d = 0.9, R = 1.02 per period, K = 100. Price the two-step European call.

p = (1.02 − 0.9)/(1.1 − 0.9) = 0.12/0.20 = 0.6.
Terminal stock values and payoffs:
- uu: 100·1.1·1.1 = 121 → payoff 21
- ud/du: 100·1.1·0.9 = 99 → payoff 0
- dd: 100·0.9·0.9 = 81 → payoff 0

Backward induction. Node u (S = 110): C_u = [0.6·21 + 0.4·0]/1.02 = 12.6/1.02 = 12.3529.
Node d (S = 90): C_d = [0.6·0 + 0.4·0]/1.02 = 0.
Node 0: C = [0.6·12.3529 + 0.4·0]/1.02 = 7.41176/1.02 = **7.2664**.

Cross-check via the direct terminal formula (only the uu path pays): C = p²·21/R² = 0.36·21/1.0404 = 7.56/1.0404 = **7.2664**. ✓

**B5. American put with early exercise.** S₀ = 100, u = 1.2, d = 0.8, R = 1.05 per period, K = 100, two steps. Price the American put and compare with the European put.

p = (1.05 − 0.8)/(1.2 − 0.8) = 0.25/0.40 = 0.625.
Terminal values/payoffs: uu = 144 → 0; ud = 96 → 4; dd = 64 → 36.

Node u (S = 120): continuation = [0.625·0 + 0.375·4]/1.05 = 1.5/1.05 = 1.4286; intrinsic = max(100 − 120, 0) = 0 → hold, value 1.4286.
Node d (S = 80): continuation = [0.625·4 + 0.375·36]/1.05 = (2.5 + 13.5)/1.05 = 16/1.05 = 15.2381; intrinsic = max(100 − 80, 0) = 20 → **exercise early**, value 20.
Node 0: value = [0.625·1.4286 + 0.375·20]/1.05 = (0.8929 + 7.5)/1.05 = 8.3929/1.05 = **7.9932**.

European put (no early exercise): node d uses continuation 15.2381 instead of 20, so
P_euro = [0.625·1.4286 + 0.375·15.2381]/1.05 = (0.8929 + 5.7143)/1.05 = 6.6071/1.05 = **6.2925**.
Early-exercise premium = 7.9932 − 6.2925 = **1.70**. The American put is worth more precisely because of the optimal exercise at node d.

**B6. Building a CRR tree from volatility.** σ = 20% p.a., r = 5% p.a. (continuous), step Δt = 0.25 yr. Compute u, d, R and p.

u = e^(σ√Δt) = e^(0.20·0.5) = e^0.10 = **1.10517**.
d = 1/u = e^(−0.10) = **0.90484**.
R = e^(rΔt) = e^(0.05·0.25) = e^0.0125 = **1.01258**.
p = (R − d)/(u − d) = (1.01258 − 0.90484)/(1.10517 − 0.90484) = 0.10774/0.20033 = **0.5378**.
Sanity check the no-arbitrage band: d = 0.905 < R = 1.013 < u = 1.105. ✓ And p·u + (1 − p)·d = 0.5378·1.10517 + 0.4622·0.90484 = 0.59436 + 0.41822 = 1.01258 = R. ✓ The tree grows the stock at the risk-free rate under p, as required.

**B7. Delta hedging in practice.** Using B1's call (Δ = 0.6667), a market-maker writes 300 such calls. What stock position neutralises the one-period risk, and verify the hedge?

Writing 300 calls has delta −0.6667·300 = −200. To be delta-neutral, buy 200 shares. Check the two states with the hedged book (long 200 shares, short 300 calls, ignoring the premium/financing which is fixed):
- Up: shares 200·120 = 24,000; calls −300·20 = −6,000 → 18,000.
- Down: shares 200·90 = 18,000; calls −300·0 = 0 → 18,000.
Both states give 18,000 — the position is riskless over the step, exactly what delta-hedging with the binomial Δ guarantees. (Over multiple steps Δ changes at each node, so the hedge must be rebalanced — dynamic hedging.)

---

## Section C — Interview-Style (Model Answers)

**C1. "Explain the binomial model to me like I'm a smart non-specialist."**

Imagine a stock that over the next period can only go up or down. I can build a mini-portfolio of that stock plus some borrowing whose value in both those futures exactly equals the option's value in both futures. If two things have identical payoffs in every state, they must cost the same today — else you'd arbitrage the gap. So the option's fair price is just today's cost of that replicating portfolio. Remarkably, that price doesn't depend on whether you think the stock will rise or fall, only on how far it can move and the interest rate. String many one-step trees together and you can price almost any option, including American ones with early exercise.

**C2. "Why don't we use the stock's expected return anywhere?"**

Because the price is set by no-arbitrage, not by forecasting. The replicating portfolio matches the option in *every* state, so its cost is forced regardless of how likely each state is. The stock's real expected return would matter if we were computing an expected value to be discounted at a risk-adjusted rate — but replication sidesteps that entirely. The mathematical shortcut is the risk-neutral probability p: a synthetic probability under which everything grows at the risk-free rate, letting us value by simple discounting. It's a valuation device, not a belief about the world.

**C3. "When does the binomial model beat Black-Scholes, and when are they the same?"**

They agree in the limit for European options on non-dividend stocks — with enough steps the binomial converges to Black-Scholes, and an American call on such a stock equals its European counterpart. The binomial model *beats* Black-Scholes whenever early exercise or discrete events matter: American puts, American calls on dividend payers, options with discrete dividends, or path-flexible features. The lattice lets you check "exercise vs hold" at every node, which the closed-form formula can't. The trade-off is speed and elegance (Black-Scholes) versus flexibility (binomial).

**C4. "Walk me through pricing an American put on a lattice."**

Build the recombining stock tree forward using u and d. At the terminal nodes set the option value to the intrinsic payoff, max(K − S, 0). Then roll backward: at each earlier node compute the continuation value as the discounted p-weighted average of the two child values, compute the immediate exercise value max(K − S, 0), and set the node value to the *larger* of the two. Record where exercise wins — that's the early-exercise boundary. The value at the root is the American put price. The only difference from a European put is that "take the max with intrinsic" step at every interior node.

**C5. "A colleague computes p = 1.3 for a one-step tree. What went wrong?"**

p above 1 (or below 0) signals a violated no-arbitrage condition — specifically R > u, meaning the risk-free asset dominates even the stock's up-state, so the stock is mispriced relative to cash and a pure arbitrage exists. Practically, the inputs are inconsistent: either u and d are set too tight around 1 for the given interest rate/step size, or R was entered per-annum instead of per-step. The fix is to check d < R < u; in a CRR tree, ensure u = e^(σ√Δt) and R = e^(rΔt) use the *same* Δt. A valid tree can never produce a probability outside [0, 1].

---

## Section D — Multiple Choice (with reasoning)

**D1. The one-period risk-neutral probability is:**
(a) (u − R)/(u − d)  (b) (R − d)/(u − d)  (c) (R − u)/(u − d)  (d) (d − R)/(u − d)

**Answer: (b).** p = (R − d)/(u − d). It sits in (0, 1) exactly when d < R < u. Option (a) is (1 − p), the down-probability. Signs in (c)/(d) are wrong and would give negative values.

**D2. In the binomial model, the option price does NOT depend on:**
(a) the up/down factors  (b) the risk-free rate  (c) the real-world probability of an up move  (d) the strike

**Answer: (c).** No-arbitrage replication makes the real probability irrelevant; only u, d, R, K and S₀ matter. This is the model's central insight.

**D3. The delta of a European call in a one-step tree equals:**
(a) (C_u − C_d)/(S_u − S_d)  (b) (C_u + C_d)/(S_u + S_d)  (c) p  (d) 1/R

**Answer: (a).** Delta is the payoff spread over the stock-price spread, the number of shares in the replicating portfolio. For a call it lies between 0 and 1.

**D4. For a valid arbitrage-free binomial tree we require:**
(a) u > d > R  (b) R > u > d  (c) d < R < u  (d) u = d

**Answer: (c).** d < R < u keeps p strictly between 0 and 1. If R falls outside this band, a riskless arbitrage exists between the stock and the bond.

**D5. In the CRR parameterisation, the down factor is:**
(a) d = 1 − u  (b) d = e^(σ√Δt)  (c) d = 1/u  (d) d = −u

**Answer: (c).** d = 1/u = e^(−σ√Δt) makes the tree symmetric in log-space and recombining, so up-down and down-up land on the same node.

**D6. An American call on a non-dividend-paying stock, priced on a binomial tree, will:**
(a) always exceed the European call  (b) equal the European call  (c) be worth less than the European call  (d) be worth zero

**Answer: (b).** Early exercise of such a call is never optimal (you'd forfeit time value and interest on K), so the "max with intrinsic" step never binds and the American value equals the European value.

**D7. Increasing the number of steps in a European binomial tree causes the price to:**
(a) diverge  (b) stay exactly constant  (c) converge to the Black-Scholes price  (d) fall to zero

**Answer: (c).** The binomial model is a discretisation of the same lognormal risk-neutral valuation; as steps → ∞ it converges (oscillating) to Black-Scholes.

**D8. At an interior node, the value of an American put is:**
(a) the continuation value only  (b) the intrinsic value only  (c) max(continuation value, intrinsic value)  (d) min(continuation value, intrinsic value)

**Answer: (c).** You choose optimally between holding (continuation) and exercising now (intrinsic), so the node value is the maximum of the two. Taking the min would misprice the early-exercise right.

**D9. If a one-step calculation returns p = −0.2, the correct conclusion is:**
(a) the put is overpriced  (b) the inputs violate no-arbitrage (likely R < d)  (c) volatility is negative  (d) the option is American

**Answer: (b).** A negative p means R < d — the stock beats the risk-free asset even in its down-state, a pure arbitrage. The inputs (often mismatched step conventions for R vs u, d) must be corrected.

**D10. Risk-neutral valuation discounts the expected payoff at:**
(a) the stock's expected return  (b) the risk-free rate  (c) a risk-adjusted rate  (d) zero

**Answer: (b).** Under the risk-neutral measure every asset earns the risk-free rate, so expected payoffs are discounted at R (= e^(rΔt)). Using a risk-adjusted rate would double-count risk that the p-measure has already removed.

---

*Self-check: B1 replication (9.5238) reconciles with risk-neutral valuation; B2 satisfies put-call parity; B4 matches the closed-form p²-path value (7.2664); B5's American put (7.9932) exceeds the European (6.2925) by the early-exercise premium; B6's CRR tree satisfies d < R < u and p·u + (1−p)·d = R.*
