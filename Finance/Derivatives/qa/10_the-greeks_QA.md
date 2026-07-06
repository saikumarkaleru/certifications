# Q&A — The Greeks

Practice bank for Chapter 10. Every question is followed by a full worked answer. The running Black-Scholes data throughout is **S = 100, K = 100, r = 5%, σ = 20%, T = 0.5 yr** → d₁ = 0.2475, d₂ = 0.1061, N(d₁) = 0.5977, φ(d₁) = 0.3869, and the Greek sheet: call 6.89, put 4.42; Δ_call +0.598, Δ_put −0.402; Γ 0.0274; ν 0.274/vol-pt; Θ_call −0.0222/day, Θ_put −0.0089/day; ρ_call +0.264, ρ_put −0.223.

---

## Section A — Concept Check

**A1. What is a "Greek", in one sentence, and why is it a partial derivative?**

A Greek is a *local sensitivity* of an option's value to one of its pricing inputs — the partial derivative of V(S, σ, t, r) with respect to that single input, everything else held fixed. It answers "how much does value change per unit change in this one factor, right now, on today's marks?" — which is exactly what a partial derivative computes.

**A2. Write the one equation that ties all the primary Greeks together.**

The Taylor expansion of option P&L over a small interval:

```
ΔV ≈ Δ·ΔS + ½·Γ·(ΔS)² + ν·Δσ + Θ·Δt + ρ·Δr
```

Delta is the first-order price term, gamma the second-order (curvature) correction, and theta/vega/rho are the first-order sensitivities to time, volatility, and rate. Every application in the chapter is a special case of this line.

**A3. Give three distinct interpretations of delta.**

(1) The **hedge ratio** — shares of the underlying to hold per option to be first-order neutral. (2) The **equivalent stock position** — a delta of 0.6 means the option behaves like 0.6 shares for small moves. (3) A rough **risk-neutral probability of finishing ITM** — exactly N(d₂), of which call delta N(d₁) is a close proxy for short maturities.

**A4. Why is delta a hedge ratio and not merely a slope?**

Because if the option gains Δ·ΔS per ₹1 spot move, then holding Δ shares against one short option cancels that first-order move exactly — the option's loss and the shares' gain net to zero. That cancellation is the replication argument at the heart of Black-Scholes: delta *is* the recipe, not just a description.

**A5. What does gamma measure, and why does a delta hedge go stale?**

Gamma is ∂²V/∂S² = ∂Δ/∂S — the rate at which delta itself changes as spot moves, i.e. the curvature of the value function. A delta hedge is exact only at one spot; the moment spot moves, gamma has shifted delta, so the hedge is off and must be rebalanced. Larger gamma ⇒ faster drift ⇒ more frequent rebalancing.

**A6. Which Greeks are identical for a call and a put at the same strike and expiry, and why?**

Gamma and vega. From put-call parity C − P = S − K·e^(−rT); the right side has zero second derivative in S (so ΔΓ = 0 between call and put) and zero derivative in σ (so equal vega). Delta differs by exactly 1, theta and rho differ.

**A7. State the sign profile of a long option position (call or put).**

Long delta (sign depends on call vs put), **long gamma**, **long vega**, and **short theta**. You pay time decay (negative theta) to own convexity (gamma) and volatility exposure (vega). A short option is the exact mirror: short gamma, short vega, long theta.

**A8. "Delta-neutral means no risk." What is wrong with this?**

It removes only *first-order spot* risk. The book still carries gamma (loss on a large move), vega (loss on a vol spike), theta (time bleed), and rho. A delta-neutral book can lose heavily if the underlying jumps or implied vol moves.

**A9. Can you hedge vega with the underlying stock? Why or why not?**

No. Stock has zero vega — its value does not depend on implied volatility. Vega (and gamma) can only be hedged with other *options*. This is why isolating a pure directional view requires trading options against options, not just shares.

**A10. Where do gamma and vega peak, and how does maturity affect each?**

Both peak **at-the-money**, the point of maximum uncertainty about which side of the strike the option lands. Gamma additionally **spikes as expiry approaches** (the ATM density blows up), while vega **grows with maturity** via its √T factor — long-dated options carry the most vega, short-dated the most gamma near expiry.

**A11. Why is "long gamma ⇒ negative theta" the beating heart of options trading?**

Owning convexity is valuable, so the market charges rent for it: the price of holding positive gamma is a negative theta bleed. Conversely, a seller collects theta as compensation for being short gamma. Whether that trade wins depends entirely on whether realised moves exceed what the theta pays for — the gamma-theta trade-off.

**A12. Rho is usually ignored — when is that a mistake?**

For short-dated equity options rho is tiny. But it grows with maturity (the K·T·e^(−rT) factor) and dominates for **long-dated options, FX, and interest-rate products**, where discounting and forward effects compound over years. Assuming rho is negligible on a 10-year option is a genuine error.

---

## Section B — Numerical / Pricing Problems

**B1. Compute Δ, Γ, ν from the running data and confirm the sheet.**

- Δ_call = N(d₁) = **0.5977 ≈ +0.598**; Δ_put = N(d₁) − 1 = **−0.4023 ≈ −0.402**.
- Γ = φ(d₁)/(S·σ·√T) = 0.3869 / (100 × 0.20 × 0.7071) = 0.3869 / 14.142 = **0.02736**.
- ν = S·φ(d₁)·√T = 100 × 0.3869 × 0.7071 = 27.36; per vol point ÷100 = **0.2736**.

Parity checks: Δ_call − Δ_put = 0.598 − (−0.402) = **1.000** ✓; call and put share the same Γ and ν ✓.

**B2. Delta-gamma reprice on a down-move.** Spot falls from 100 to **95** (ΔS = −5). Estimate the long call's new value by delta-only and delta-gamma, then reconcile against an exact reprice.

Delta-only:
```
ΔV ≈ Δ·ΔS = 0.598 × (−5) = −2.99   →   6.89 − 2.99 = 3.90
```
Delta-gamma:
```
ΔV ≈ Δ·ΔS + ½·Γ·(ΔS)² = −2.99 + ½ × 0.02736 × 25 = −2.99 + 0.342 = −2.65   →   6.89 − 2.65 = 4.24
```
Exact Black-Scholes at S = 95: d₁ = −0.1152, d₂ = −0.2566, giving **C = 4.26** (delta there = 0.454).

| Method | Estimated C at 95 | Error vs exact 4.26 |
|--------|-------------------|---------------------|
| Delta-only | 3.90 | −0.36 |
| Delta + gamma | 4.24 | −0.02 |
| Exact BS | 4.26 | — |

Gamma recovers almost the entire error. Note the curvature helped the long holder on the way down — the true loss (−2.63) is smaller than delta alone predicted (−2.99). Long gamma cuts losses on down-moves and boosts gains on up-moves.

**B3. Set up and rebalance a delta hedge.** A dealer **sells 500** of these calls and wants first-order immunity.

- Initial book delta = short 500 × 0.598 = **−299**. To neutralise, **buy 299 shares** (delta +299). Net ≈ 0.
- Spot rises to **103**; new call delta = 0.676. Book delta = −500 × 0.676 + 299 = −338 + 299 = **−39**. Buy **39 more shares** to restore neutrality.
- Direction of trade: spot rose, dealer **bought** shares (higher price). Had spot fallen, delta shrinks and the dealer **sells** (lower price). A short-gamma hedger is structurally forced to **buy high, sell low** — the rebalancing bleed that theta is meant to compensate.

**B4. Gamma-theta daily P&L and break-even move.** The dealer above is short 500 calls, delta-hedged. Ignoring vega and rho, find the daily P&L formula, the theta earned on a still day, and the break-even daily move.

Book gamma = −500 × 0.02736 = **−13.68**; book theta = +500 × 0.0222 = **+11.10/day**.
```
Daily P&L ≈ ½·Γ_book·(ΔS)² + Θ_book·Δt = −½ × 13.68 × (ΔS)² + 11.10
```
- Still day (ΔS = 0): earn the full **+11.10** theta.
- Break-even move: ½ × 13.68 × (ΔS)² = 11.10 → (ΔS)² = 11.10 / 6.84 = 1.623 → **ΔS = ±1.27**.

A ₹1.27 move on a ₹100 stock is 1.27% daily; annualised 1.27% × √252 = **20.2% ≈ the 20% implied vol** we priced at. The delta-hedged seller breaks even exactly when **realised vol = implied vol**. (The break-even move is independent of position size — scaling both gamma and theta by 500 leaves the ratio unchanged.)

| Scenario | Daily move | Gamma P&L | Theta P&L | Net |
|----------|-----------|-----------|-----------|-----|
| Quiet | ±0.5 | −1.71 | +11.10 | **+9.39** |
| Break-even | ±1.27 | −11.10 | +11.10 | **0.00** |
| Wild | ±3.0 | −61.6 | +11.10 | **−50.5** |

**B5. Vega P&L.** The same delta-hedged short-500 book sees spot unchanged overnight but implied vol jumps 20% → 23% (Δσ = +3 vol points). Find the P&L.

Book vega = −500 × 0.2736 = **−136.8 per vol point**.
```
Vega P&L = −136.8 × 3 = −410.4
```
The dealer loses **₹410** despite being right that spot would not move. Short options are short vega; a vol spike marks up what you owe. Only options carry vega, so this risk cannot be hedged with the underlying.

**B6. Aggregate a two-leg book.** A desk holds **long 500 calls** and **short 800 puts** on the same underlying. Compute net Greeks by addition (short flips sign) and read the risk.

| Greek | Long 500 calls | Short 800 puts | **Net** |
|-------|---------------|----------------|---------|
| Delta | 500 × (+0.598) = +299 | −800 × (−0.402) = +322 | **+621** |
| Gamma | 500 × 0.0274 = +13.7 | −800 × 0.0274 = −21.9 | **−8.2** |
| Vega | 500 × 0.274 = +137 | −800 × 0.274 = −219 | **−82** |
| Theta/day | 500 × (−0.0222) = −11.1 | −800 × (−0.0089) = +7.1 | **−4.0** |

Reading: **net long 621 deltas** (bullish — sell 621 shares to neutralise), **short gamma and short vega** (the 800 short puts dominate), so the desk profits if the market stays calm and loses on a swing or vol spike. Net theta is only mildly negative because long-call decay is largely offset by short-put decay collected.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through what delta tells you and how you'd use it on a desk."**

Delta is ∂V/∂S — the change in option value per ₹1 move in the underlying. On a desk it plays three roles at once: it is my hedge ratio, so if I'm short 1,000 calls at delta 0.6 I buy 600 shares to be first-order neutral; it is my equivalent stock position, so I can read the whole book's directional exposure as one net delta number; and it approximates the probability of the option finishing in the money, which shapes how I think about the position's likely outcome. I hedge delta first and most often because it's the cheapest risk to remove — I use the underlying or futures, often intraday, targeting near-zero net delta.

**C2. "Your book is delta-neutral. Why might you still lose a lot of money tomorrow?"**

Delta-neutral kills only first-order spot risk. I'm still exposed to gamma, vega, theta, and rho. If I'm short gamma and the underlying makes a big move, the ½·Γ·(ΔS)² term produces a real loss no matter which way it goes — my delta hedge was correct only for an instant and went stale immediately. Separately, if implied vol spikes and I'm short vega, my options get marked up against me even if spot never moves. So "delta-neutral" means "no directional view," not "no risk" — it's the starting point for managing the remaining Greeks, not the end.

**C3. "Explain the gamma-theta trade-off and why it maps onto a vol view."**

The daily P&L of a delta-hedged position is roughly ½·Γ·(ΔS)² + Θ·Δt. Gamma and theta always carry opposite signs: if I'm long gamma I'm short theta, and vice versa. So if I buy options I'm long convexity — I make money from big realised moves but pay theta every day; if I sell options I collect theta but bleed on large moves. Setting the two terms equal gives a break-even daily move that, annualised, equals exactly the implied volatility I traded at. That's the punchline: a delta-hedged option position breaks even when realised vol equals implied vol. It converts a fuzzy "I think vol is too high" into a precise, hedgeable trade — sell options and delta-hedge if I think the world will be calmer than implied, buy and hedge if wilder.

**C4. "Which Greeks are the same for a call and a put, and how would that catch a bug?"**

At the same strike and expiry, a call and put share identical **gamma** and **vega**, and their deltas differ by exactly 1. This falls straight out of put-call parity: C − P = S − K·e^(−rT). Differentiate once in S and you get 1 (the delta difference); differentiate twice in S, or once in σ, and you get zero (equal gamma, equal vega). So if I'm handed a Greek sheet where a call and its paired put show different gammas or vegas, or deltas that don't differ by 1.00, I know there's a bug before I check anything else. These parity identities are the fastest sanity check on any risk report.

**C5. "You're long a straddle and perfectly right that the stock is about to move. Can you still lose?"**

Yes. A long straddle is long gamma but also long vega and short theta. If the move takes days to arrive, theta bleeds me every day — the position is a wasting asset. Worse, if implied vol *falls* while I wait (the event resolves as low-risk and the vol premium collapses), my long vega loses even before the stock moves. And if the eventual realised move is smaller than the implied vol I paid for, gamma gains won't cover the theta paid. Being right on direction isn't enough; I need realised vol's *timing and magnitude* to beat the implied vol in the premium.

**C6. "Why does rho barely matter for a one-month equity option but dominate a ten-year one?"**

Rho scales with K·T·e^(−rT), so it grows roughly linearly with maturity. On a one-month option (T ≈ 0.08), a 1% rate move barely nudges the discount factor or forward — swamped by delta, gamma, and vega. On a ten-year option, T is 120× larger; discounting of the strike and the forward's rate dependence compound over a decade, so a rate move materially reprices the option. That's why rate desks and long-dated structured products hedge rho with swaps or bond futures, while a short-dated equity market-maker can ignore it.

---

## Section D — Multiple Choice (with reasoning)

**D1. An ATM call on a non-dividend stock has a delta closest to:**
(a) 0.20 (b) 0.50 (c) 0.60 (d) 1.00

**Answer: (b) 0.50** (with (c) also defensible). ATM delta is approximately 0.5; with positive carry (r > 0 lifting the forward) it sits slightly above, e.g. 0.598 in our data. Of the offered options 0.50 is the textbook ATM answer; 0.60 reflects the carry adjustment. Deep-OTM would approach 0 and deep-ITM approach 1.

**D2. Gamma is largest when the option is:**
(a) deep in the money (b) deep out of the money (c) at the money, near expiry (d) at the money, long-dated

**Answer: (c).** Gamma = φ(d₁)/(S·σ·√T) peaks at-the-money (where φ(d₁) is largest) and blows up as √T → 0. Deep ITM/OTM options have delta pinned near 1 or 0, so it barely moves (near-zero gamma). Long-dated ATM options have high vega but *lower* gamma than short-dated ones, because the √T in the denominator grows.

**D3. Which statement about a long option is correct?**
(a) long gamma, long theta (b) short gamma, short vega (c) long gamma, short theta (d) short gamma, long theta

**Answer: (c) long gamma, short theta.** Owning an option means owning convexity (positive gamma) and paying time decay (negative theta) for it — long gamma always pairs with short theta. Buyers are also long vega. Options (a) and (d) mix the signs incorrectly; (b) describes an option *seller*.

**D4. You are short options and delta-hedged. You make money if:**
(a) realised vol > implied vol (b) realised vol < implied vol (c) rates fall (d) implied vol rises

**Answer: (b) realised vol < implied vol.** Short options means short gamma / long theta: you collect decay and lose on moves, so you win when the market is calmer than the implied vol you sold — realised below implied. (a) is the long-option case. (d) hurts you (short vega). (c) affects rho, second-order and direction-dependent, not the core condition.

**D5. Which Greek cannot be hedged using the underlying stock?**
(a) delta (b) gamma (c) vega (d) both gamma and vega

**Answer: (d).** Stock has a constant delta of 1 and zero gamma, vega, theta, and rho. So the underlying can neutralise delta but is useless for gamma and vega — both require trading other options. This is why isolating a directional view means hedging gamma and vega with options, not shares.

**D6. The Black-Scholes PDE written in Greek terms is Θ + rSΔ + ½σ²S²Γ = rV. This says:**
(a) all Greeks sum to zero (b) a delta-hedged position's theta plus gamma P&L equals the risk-free carry (c) delta equals gamma at expiry (d) vega is redundant

**Answer: (b).** Rearranged, the PDE states that for a delta-hedged position, the theta bleed plus the gamma P&L must equal the risk-free return on the position's value — the gamma-theta trade-off expressed as a differential equation. It is the continuous-time statement of why a replicating portfolio earns exactly the risk-free rate, which is what pins down the option price.

**D7. For which position is theta positive?**
(a) long ATM call (b) long ATM put (c) short call (d) long straddle

**Answer: (c) short call.** Any short option position is theta-positive — you *earn* decay as the option you owe loses time value. All the long positions (a, b, d) are theta-negative, paying decay to hold optionality. (A deep-ITM European long put can be a rare positive-theta exception, but that's not offered here.)

---

*Self-check performed: all Greek values recomputed from the Black-Scholes closed forms (Δ = N(d₁); Γ = φ(d₁)/(Sσ√T); ν = Sφ(d₁)√T; Θ and ρ per §4.3/§4.5), the B2 reprice reconciled against an exact BS valuation at S = 95 (C = 4.26), and the parity identities Δ_call − Δ_put = 1 with equal Γ and ν confirmed.*
