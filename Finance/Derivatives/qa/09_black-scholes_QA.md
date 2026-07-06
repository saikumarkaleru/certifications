# Q&A — The Black-Scholes-Merton Model

Practice bank for Chapter 09. Every question is followed by a full worked answer. Work each one before reading the solution. Normal-distribution values are quoted to four decimals; small rounding differences from your tables are expected.

Reference formulas used throughout (European options, continuous compounding):

- d₁ = [ln(S₀/K) + (r − q + σ²/2)·T] / (σ·√T)
- d₂ = d₁ − σ·√T
- Call: c = S₀·e^(−qT)·N(d₁) − K·e^(−rT)·N(d₂)
- Put: p = K·e^(−rT)·N(−d₂) − S₀·e^(−qT)·N(−d₁)
- With no dividends set q = 0.

---

## Section A — Concept Check

**A1. What single insight lets Black-Scholes price an option without knowing the stock's expected return?**

Risk-neutral valuation via a continuously rebalanced hedge. Black, Scholes and Merton showed that a portfolio of the option plus a short position of Δ = ∂c/∂S shares is instantaneously riskless, so it must earn the risk-free rate to prevent arbitrage. Once risk is hedged away, the stock's real drift μ drops out entirely and every asset is discounted at r. The option value depends on σ but not on how bullish or bearish investors are — the most counter-intuitive and powerful result in the model.

**A2. State the assumptions behind the model.**

(1) The stock follows geometric Brownian motion with constant volatility σ — so terminal price is lognormal; (2) no dividends over the life (relaxable via q); (3) a constant, known risk-free rate r; (4) frictionless markets — no costs or taxes, divisible assets, unrestricted short selling; (5) continuous trading so the hedge rebalances without gaps; (6) no arbitrage; (7) European exercise. Each broken assumption is a known source of pricing error — constant σ fails, producing the volatility smile.

**A3. In words, what do N(d₁) and N(d₂) represent?**

N(d₂) is the risk-neutral probability the call finishes in the money, Prob(S_T > K). N(d₁) is not a probability of exercise; it is the option's delta (non-dividend stock), arising because the expected stock price conditional on exercise, times that probability, collapses to S₀·N(d₁) after discounting. Loosely: S₀·N(d₁) is the present value of receiving the stock if exercised, K·e^(−rT)·N(d₂) the present value of paying the strike if exercised.

**A4. Why does volatility raise both call and put values, but the risk-free rate move them in opposite directions?**

Volatility widens the terminal distribution symmetrically while the payoff is one-sided (floored at zero), so more dispersion adds value on the winning tail without symmetric loss — true for calls and puts alike; both have positive vega. The rate r enters through the discounting of the strike, K·e^(−rT). A higher r shrinks the present value of the strike the call holder pays, raising the call; the put holder receives the strike, so a smaller present value hurts the put. Hence rho is positive for calls, negative for puts.

**A5. What is the lognormal assumption and one consequence for real markets?**

The model assumes ln(S_T) is normally distributed, so S_T itself is lognormal — bounded below by zero and right-skewed. A consequence is that Black-Scholes assigns thinner tails than markets actually show; real returns exhibit fat tails and skew, so deep out-of-the-money options trade richer than the model says. Traders reconcile this by quoting different implied volatilities across strikes — the volatility smile/skew.

**A6. Define implied volatility and explain why it is the model "run in reverse."**

Every input is observable except σ. Implied volatility is the σ that makes the model price equal the market price. Because c is strictly increasing in σ (positive vega), the inversion is unique and found numerically (Newton-Raphson or bisection). It is the market's consensus forecast of future volatility, not a historical measurement — the model becomes a translation device between prices and volatilities.

**A7. How is put-call parity used to check a Black-Scholes calculation?**

Parity states c − p = S₀·e^(−qT) − K·e^(−rT). Since Black-Scholes prices calls and puts off the same d₁, d₂, any correctly computed pair satisfies it exactly. Computing the put independently and confirming parity holds is the fastest self-check — a mismatch signals an arithmetic slip in one of the two.

**A8. What does "delta hedging" mean and why must it be dynamic?**

Delta is ∂c/∂S = e^(−qT)·N(d₁) for a call — the shares that neutralise the option's first-order price sensitivity. A writer short one call holds Δ shares to be locally hedged. But delta changes as S, T and σ move (that rate of change is gamma), so the hedge must be continuously rebalanced. This dynamic replication is the mechanism the derivation assumes, and its cost is what the premium compensates.

**A9. What are gamma and theta, and why are they usually of opposite sign for a long option?**

Gamma is ∂²c/∂S² — the curvature of value in the underlying, always positive for a long option. Theta is ∂c/∂t — the rate of value decay as time passes, usually negative for a long option. The trade-off is structural: a long option holder is paid in convexity (positive gamma lets the hedge buy low and sell high) but bleeds time value (negative theta). At fair value the two roughly offset for a delta-hedged book.

**A10. When does the dividend adjustment q matter, and how does it enter?**

A continuous dividend yield q reduces the stock's risk-neutral growth from r to (r − q), so it replaces S₀ with S₀·e^(−qT) everywhere and appears in the drift term of d₁. It matters for options on indices, currencies (where q is the foreign rate), and dividend-paying stocks. Ignoring a real dividend overprices calls and underprices puts, because dividends transfer value from the share price to holders the option owner does not receive.

---

## Section B — Numerical / Pricing Problems

**B1. Baseline European call — full step-by-step.** S₀ = 42, K = 40, r = 10%, σ = 20%, T = 0.5, no dividends. Price the call and put and reconcile via parity.

Step 1 — d₁: ln(42/40) = ln(1.05) = 0.04879. Drift term = (0.10 + 0.20²/2)·0.5 = (0.10 + 0.02)·0.5 = 0.06. Numerator = 0.04879 + 0.06 = 0.10879. Denominator σ√T = 0.20·√0.5 = 0.20·0.70711 = 0.14142. So d₁ = 0.10879 / 0.14142 = 0.7693.

Step 2 — d₂ = 0.7693 − 0.14142 = 0.6279.

Step 3 — N(d₁) = N(0.7693) = 0.7791; N(d₂) = N(0.6279) = 0.7349.

Step 4 — c = 42·0.7791 − 40·e^(−0.05)·0.7349. e^(−0.05) = 0.95123. c = 32.72 − 40·0.95123·0.7349 = 32.72 − 27.96 = **4.76**.

Step 5 — put via full formula: p = 40·0.95123·N(−0.6279) − 42·N(−0.7693) = 38.049·0.2651 − 42·0.2209 = 10.09 − 9.28 = **0.81**.

Reconcile via parity: c − p should equal S₀ − K·e^(−rT) = 42 − 38.049 = 3.951. And c − p = 4.76 − 0.81 = 3.95. ✓ Consistent.

**B2. At-the-money benchmark.** S₀ = 100, K = 100, r = 5%, σ = 20%, T = 1, no dividends. Price the call, then the put by parity.

d₁ = [ln(1) + (0.05 + 0.02)·1] / (0.20·1) = 0.07 / 0.20 = 0.35. d₂ = 0.35 − 0.20 = 0.15.

N(0.35) = 0.6368; N(0.15) = 0.5596. e^(−0.05) = 0.95123.

c = 100·0.6368 − 100·0.95123·0.5596 = 63.68 − 53.23 = **10.45**.

Put by parity: p = c − S₀ + K·e^(−rT) = 10.45 − 100 + 95.123 = **5.57**.

Sanity: an ATM one-year option at 20% vol is worth roughly 0.4·σ·S·√T ≈ 0.4·0.20·100 = 8 as a rough guide; the exact 10.45 is higher because r shifts the forward above the strike. Order of magnitude checks out.

**B3. Compute the Greeks for the B2 option.** Give delta, gamma, vega, theta (per year) and rho for the call. Use N'(x) = (1/√(2π))·e^(−x²/2).

N'(d₁) = N'(0.35) = 0.39894·e^(−0.35²/2) = 0.39894·e^(−0.06125) = 0.39894·0.94059 = 0.37524.

- Delta = N(d₁) = **0.6368** (per $1 of stock).
- Gamma = N'(d₁)/(S₀·σ·√T) = 0.37524 / (100·0.20·1) = 0.37524/20 = **0.01876**.
- Vega = S₀·N'(d₁)·√T = 100·0.37524·1 = **37.52** per 1.00 (i.e. 100%) change in σ, so about **0.375 per 1 volatility point**.
- Theta = −[S₀·N'(d₁)·σ/(2√T)] − r·K·e^(−rT)·N(d₂) = −[100·0.37524·0.20/2] − 0.05·100·0.95123·0.5596 = −3.7524 − 2.663 = **−6.42 per year** (≈ −0.0175/day).
- Rho = K·T·e^(−rT)·N(d₂) = 100·1·0.95123·0.5596 = **53.23** per 1.00 change in r, i.e. **0.532 per 1% (100 bp)**.

**B4. Reprice B2 with a dividend yield.** Same data but q = 3%. Show that the call falls.

Drift now uses (r − q + σ²/2) = (0.05 − 0.03 + 0.02) = 0.04. d₁ = 0.04/0.20 = 0.20. d₂ = 0.20 − 0.20 = 0.00.

N(0.20) = 0.5793; N(0.00) = 0.5000. e^(−qT) = e^(−0.03) = 0.97045.

c = 100·0.97045·0.5793 − 100·0.95123·0.5000 = 56.22 − 47.56 = **8.66**.

The call dropped from 10.45 to 8.66 — the dividend lowers the effective forward price of the stock, exactly as theory predicts. The matching put would rise.

**B5. Back out implied volatility (concept + one iteration).** A one-year ATM call (S₀ = K = 100, r = 5%, q = 0) trades at 12.00. From B2, σ = 20% gives a price of 10.45. Is implied vol above or below 20%, and estimate it.

Because vega is positive, a higher market price requires a higher σ. The market price 12.00 exceeds the 20%-vol price 10.45, so implied vol is above 20%. Estimate the increment using vega: from B3, vega ≈ 0.375 per volatility point. Needed increase = (12.00 − 10.45)/0.375 ≈ 1.55/0.375 ≈ 4.1 points, giving a first estimate of **≈ 24%**. (Vega falls slightly as σ rises, so the true root is a touch above 24%; one more Newton step would refine it. The method — price, compare, divide the gap by vega, repeat — is the whole algorithm.)

**B6. Deep in-the-money call sanity check.** S₀ = 150, K = 100, r = 5%, σ = 25%, T = 1, q = 0. Price it and confirm it behaves like a forward.

d₁ = [ln(1.5) + (0.05 + 0.03125)·1] / (0.25·1) = [0.40546 + 0.08125]/0.25 = 0.48671/0.25 = 1.9469. d₂ = 1.9469 − 0.25 = 1.6969.

N(1.9469) = 0.9743; N(1.6969) = 0.9551. e^(−0.05) = 0.95123.

c = 150·0.9743 − 100·0.95123·0.9551 = 146.15 − 90.85 = **55.30**.

Check against the "certain exercise" floor: if exercise were certain the call is worth S₀ − K·e^(−rT) = 150 − 95.123 = 54.88. The model price 55.30 sits just above this floor — the small excess is residual time value from the slim chance the stock still falls below 100. Delta N(d₁) = 0.974, near 1, confirms the option now tracks the stock almost one-for-one. ✓

**B7. Volatility sensitivity table.** For the B2 ATM one-year call, tabulate price as σ moves. Confirm monotonic increase.

| σ | d₁ | d₂ | N(d₁) | N(d₂) | Call |
|---|---|---|---|---|---|
| 10% | 0.550 | 0.450 | 0.7088 | 0.6736 | 6.81 |
| 20% | 0.350 | 0.150 | 0.6368 | 0.5596 | 10.45 |
| 30% | 0.317 | 0.017 | 0.6243 | 0.5068 | 14.23 |
| 40% | 0.325 | −0.075 | 0.6274 | 0.4701 | 18.02 |

(For σ = 30%: d₁ = [0 + (0.05 + 0.045)]/0.30 = 0.095/0.30 = 0.317; call = 100·0.6243 − 95.123·0.5068 = 62.43 − 48.20 = 14.23.) Price rises monotonically with σ — the signature of positive vega. Note d₁ is not monotonic in σ, but the call price is.

---

## Section C — Interview-Style (Model Answers)

**C1. "Explain Black-Scholes to me as if I don't know calculus."**

An option is worth the average of its future payoffs, weighted by how likely each outcome is and discounted back to today. Black-Scholes makes two moves. First, it assumes the stock wanders randomly with a fixed level of jitteriness (volatility), which pins down the probability of every future price. Second — the clever part — anyone holding the option can cancel its risk moment to moment by holding a specific number of shares against it; because that combined position is riskless it must earn only the risk-free rate, and that fact yields the fair price without ever guessing direction. The answer depends on five things you can look up — spot, strike, time, rate, volatility — plus the one you can't, future volatility, which is where all the real debate lives.

**C2. "Which input are traders actually trading, and why?"**

Volatility. Every other input — spot, strike, rate, time — is observable and agreed; volatility is the sole forecast and carries all the disagreement. When a desk "buys an option" it is really going long future realised volatility versus the implied vol it paid. That's why option markets quote in vol terms, why the smile exists, and why a delta-hedged option position is a clean bet on realised versus implied vol.

**C3. "The model assumes constant volatility, which is false. Why do people still use it?"**

Because it fails in a well-understood, parameterisable way. Rather than discard it, the market treats implied volatility as a per-option quote and lets it vary across strikes and maturities — the smile and the term structure. Black-Scholes then survives not as a truth about the world but as a universal quoting language: it maps a price to a single number, implied vol, that traders can compare and hedge. Richer models (local vol, stochastic vol, jump diffusion) exist to explain the smile the flat-vol model can't, yet are almost always calibrated back to Black-Scholes implied vols. It is the shared coordinate system even when nobody believes the assumption.

**C4. "Walk me through why the stock's expected return doesn't appear in the formula."**

Set up a portfolio: long the option, short delta shares. Over an instant, option and share are driven by the same Brownian shock, and choosing delta = ∂c/∂S makes the shocks cancel exactly, so the portfolio's change is deterministic — riskless. A riskless portfolio can only earn the risk-free rate without arbitrage. In writing that condition down, the drift term μ carrying the stock's expected return has already been hedged out and never re-enters. Economically: since you can replicate the option with stock and cash, its price can't depend on your view of direction — only on how much the stock wiggles.

**C5. "A client asks why their deep out-of-the-money put costs more than your model says. What's happening?"**

Black-Scholes assumes lognormal returns with thin tails, but real markets crash more often and more violently — the left tail is fatter. Deep OTM puts are crash insurance, so buyers bid them above the flat-vol price. This shows up as the volatility skew: implied vol at low strikes exceeds at-the-money. So the put isn't mispriced — the market is telling you, through that higher implied vol, that it assigns more probability to a large downward move than a single volatility number would. My quote reflects the skew; the flat-vol textbook number doesn't.

---

## Section D — Multiple Choice (with Reasoning)

**D1. In Black-Scholes, N(d₂) is best interpreted as:**
(a) the option's delta; (b) the risk-neutral probability the call expires in the money; (c) the probability the stock doubles; (d) the option's gamma.

**Answer: (b).** N(d₂) = Prob(S_T > K) under the risk-neutral measure. Delta is N(d₁), which rules out (a); (c) and (d) are unrelated. The term K·e^(−rT)·N(d₂) is exactly the discounted strike paid, weighted by the chance of paying it.

**D2. Holding all else fixed, an increase in the risk-free rate r will:**
(a) raise both call and put; (b) lower both; (c) raise the call, lower the put; (d) have no effect.

**Answer: (c).** Rho is positive for calls, negative for puts. A higher r shrinks the present value of the strike K·e^(−rT): good for the call holder who pays K, bad for the put holder who receives it.

**D3. Which quantity is always positive for a long option, call or put?**
(a) delta; (b) theta; (c) vega; (d) rho.

**Answer: (c).** Vega is positive for both long calls and long puts — more volatility helps either. Delta is positive for calls but negative for puts; theta is typically negative for long options; rho differs in sign by type.

**D4. The volatility smile is evidence that:**
(a) Black-Scholes overprices ATM options; (b) real return distributions have fatter tails / skew than lognormal; (c) interest rates are stochastic; (d) dividends were ignored.

**Answer: (b).** The smile/skew — implied vol varying with strike — arises because the market prices tail risk that the single-volatility lognormal model does not capture. It is a direct symptom of the constant-volatility, thin-tail assumption breaking.

**D5. For a European ATM option, most of the premium consists of:**
(a) intrinsic value; (b) time value; (c) dividend value; (d) interest.

**Answer: (b).** An ATM option has essentially zero intrinsic value (S ≈ K), so nearly the entire premium is time value — the value of remaining uncertainty. This is also where vega and gamma peak.

**D6. If a call's Black-Scholes delta is 0.63, delta-hedging a short position in 100 calls (each on 1 share) requires:**
(a) shorting 63 shares; (b) buying 63 shares; (c) buying 100 shares; (d) no shares.

**Answer: (b).** Short 100 calls has delta −63; to neutralise it you buy 63 shares (delta +63). The hedge must then be rebalanced as delta drifts (gamma risk).

**D7. Increasing time to expiry T on a European call (no dividends) generally:**
(a) always lowers its value; (b) generally raises it via more time value; (c) has no effect; (d) only matters for puts.

**Answer: (b).** More time means more chance to finish further in the money and a smaller present value of the strike paid, so a longer-dated non-dividend European call is worth more. (European puts can occasionally behave non-monotonically when rates are high, which is why the question specifies the call.)

**D8. Implied volatility is found by:**
(a) averaging past returns; (b) solving Black-Scholes so the model price equals the market price; (c) reading it off the balance sheet; (d) differentiating the payoff.

**Answer: (b).** Implied vol is the σ that equates model and market price. It is forward-looking and unique because vega is positive, unlike historical volatility in (a) which is backward-looking.

---

*End of Chapter 09 practice bank. If a numerical answer differs by more than a rounding cent, recheck N(·) table values first, then the σ√T term — the two most common slip points.*
