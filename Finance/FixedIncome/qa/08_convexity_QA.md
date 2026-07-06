# Q&A — Convexity

Practice bank for the *Convexity* chapter. Work each problem before reading the answer. Every question is followed by a full worked solution; numerical items reconcile the approximation against the exact repricing.

---

## Section A — Concept Check

**A1. In one sentence, what does convexity measure?**

Convexity measures the *curvature* of the price–yield relationship — i.e. the rate at which a bond's modified duration itself changes as yields change. Formally it is the second derivative of price with respect to yield, scaled by price.

**A2. Duration is a straight-line estimate. Why is that line always wrong in the same direction for an option-free bond?**

The true price–yield curve is convex (bowed toward the origin). A straight tangent line lies *below* the curve everywhere except at the point of tangency. So the duration-only estimate always *understates* the actual price: it over-predicts the loss when yields rise and under-predicts the gain when yields fall. Convexity is the correction term that pulls the estimate back onto the curve.

**A3. Is positive convexity good or bad for a bondholder, and why?**

Positive convexity is good. It means prices rise more when yields fall than they fall when yields rise by the same amount — an asymmetry in the investor's favour. All else equal, a more convex bond outperforms a less convex bond of equal duration whenever yields move, in either direction.

**A4. Name three factors that increase the convexity of an option-free bond.**

(1) Longer maturity, (2) lower coupon, and (3) lower yield to maturity. Each of these also raises duration; convexity generally rises with duration and, for a given duration, with the dispersion of the cash flows across time.

**A5. What is negative convexity and which instruments exhibit it?**

Negative convexity means the price–yield curve bends the "wrong" way over some yield range — duration *shortens* as yields fall. Callable bonds and mortgage-backed securities (MBS) show it: as yields fall, the embedded call/prepayment option becomes more valuable to the issuer/borrower, capping the bond's price appreciation. The result is that these bonds gain less on a rally than they lose on a sell-off.

**A6. Distinguish "modified convexity" from "effective convexity."**

Modified (analytical) convexity is computed from the bond's own fixed cash flows using calculus, assuming those cash flows do not change with yield. Effective convexity re-prices the bond under an upward and a downward yield shock using a valuation model that *lets the cash flows change* (e.g. exercise of a call). Effective convexity is the correct measure for bonds with embedded options; modified convexity is fine for option-free bonds.

**A7. Convexity has units. What are they, and what does that imply for scaling?**

Convexity is expressed in years-squared (time²). Because the price-change term uses (Δy)², you must keep yield in decimal form consistently. A convexity of 80 contributes ½ × 80 × (0.01)² = 0.004 = 0.40% for a 100 bp move.

**A8. Two bonds have identical duration. What does convexity let you say about them?**

Duration alone makes them look equivalent for small moves. Convexity breaks the tie: the higher-convexity bond will do better for any large move in yields, up or down. Investors expecting volatility pay up for convexity; in calm markets the higher-convexity bond typically offers slightly lower yield as compensation.

---

## Section B — Numerical Bond-Math Problems

**B1. Effective duration and convexity from a repricing table.**

A bond is priced at P₀ = 100.00. Shocking the yield curve by ±25 bp gives:
- Yield **+25 bp**: P₊ = 98.15
- Yield **−25 bp**: P₋ = 101.90

Compute effective duration and effective convexity, then estimate the price change for a +100 bp move and comment.

*Step 1 — Effective duration.*
$$D_{eff}=\frac{P_- - P_+}{2\,P_0\,\Delta y}=\frac{101.90-98.15}{2\times100\times0.0025}=\frac{3.75}{0.5}=7.5$$

*Step 2 — Effective convexity.*
$$C_{eff}=\frac{P_- + P_+ - 2P_0}{P_0\,(\Delta y)^2}=\frac{101.90+98.15-200}{100\times(0.0025)^2}=\frac{0.05}{100\times0.00000625}=\frac{0.05}{0.000625}=80$$

*Step 3 — Estimate for Δy = +100 bp (+0.01).*
$$\frac{\Delta P}{P}\approx -D_{eff}\,\Delta y+\tfrac12 C_{eff}(\Delta y)^2=-7.5(0.01)+\tfrac12(80)(0.01)^2$$
$$=-0.0750+0.0040=-0.0710=-7.10\%$$

*Comment.* Duration alone predicts −7.50%. Convexity adds back +0.40%, giving −7.10%. The convexity term is positive for *both* directions of move, which is exactly the favourable asymmetry positive convexity provides.

**B2. Computing convexity directly from cash flows.**

A 3-year annual bond, 6% coupon, face 100, trades at par (YTM = 6%, so P = 100). Use the closed form
$$C=\frac{1}{P(1+y)^2}\sum_{t=1}^{n}\frac{t(t+1)\,CF_t}{(1+y)^t}$$

*Step 1 — Build the t(t+1)·CFₜ/(1+y)ᵗ column* with y = 0.06:

| t | CFₜ | t(t+1) | t(t+1)·CFₜ | (1.06)ᵗ | Term |
|---|-----|--------|-----------|---------|------|
| 1 | 6   | 2      | 12        | 1.0600  | 11.3208 |
| 2 | 6   | 6      | 36        | 1.1236  | 32.0399 |
| 3 | 106 | 12     | 1272      | 1.191016| 1068.0079 |

Sum of terms = 11.3208 + 32.0399 + 1068.0079 = **1111.369**.

*Step 2 — Scale.*
$$C=\frac{1111.369}{100\times(1.06)^2}=\frac{1111.369}{112.36}=9.891\ \text{years}^2$$

*Step 3 — Get modified duration for the reconciliation in B3.* Macaulay duration:
$$D_{mac}=\frac{1}{P}\sum\frac{t\,CF_t}{(1+y)^t}=\frac{5.6604+10.6800+267.006}{100}=2.8335\ \text{yrs}$$
$$D_{mod}=\frac{2.8335}{1.06}=2.6731$$

**B3. Reconcile the estimate against exact repricing (continuing B2).**

Estimate the price change for a +100 bp rise to 7%, then reprice exactly and compare.

*Step 1 — Approximation.*
$$\frac{\Delta P}{P}\approx -2.6731(0.01)+\tfrac12(9.891)(0.01)^2=-0.026731+0.000495=-0.026236=-2.6236\%$$

*Step 2 — Exact repricing at y = 7%.*
$$P=\frac{6}{1.07}+\frac{6}{1.07^2}+\frac{106}{1.07^3}=5.6075+5.2407+86.5275=97.3757$$
$$\frac{\Delta P}{P}=\frac{97.3757-100}{100}=-2.6243\%$$

*Step 3 — Compare.* Estimate −2.6236% vs actual −2.6243%: a residual of under 0.001%. The duration-plus-convexity model captures essentially the entire move. Duration alone would have predicted −2.6731%, an error of about +0.05%, which the convexity term corrects.

**B4. Show convexity's symmetry in the investor's favour (continuing B2).**

Reprice the same bond for a −100 bp move to 5% and compare the gain against the loss from B3.

*Exact repricing at y = 5%:*
$$P=\frac{6}{1.05}+\frac{6}{1.05^2}+\frac{106}{1.05^3}=5.7143+5.4422+91.5776=102.7341$$
Gain = +2.7341%.

*Compare with the −100 bp loss of −2.6243% (B3).* The rally gain (+2.73%) exceeds the sell-off loss (−2.62%) in absolute terms by about 0.11%. Same yield shock, bigger upside than downside — the hallmark of positive convexity.

**B5. Dollar convexity contribution.**

A portfolio holds \$50 million (market value) of a bond with modified duration 6.0 and convexity 90. Estimate the value change for a −150 bp parallel shift.

*Step 1 — Percentage change.* Δy = −0.015.
$$\frac{\Delta P}{P}=-6.0(-0.015)+\tfrac12(90)(-0.015)^2=0.09+0.010125=0.100125=10.0125\%$$

*Step 2 — Dollar change.*
$$\Delta V = 0.100125 \times \$50{,}000{,}000 = \$5{,}006{,}250$$

*Comment.* Duration alone gives +9.00% (\$4.5m). Convexity adds +1.01% (\$506,250). For a large 150 bp move the convexity term is material — more than 10% of the total estimated gain.

**B6. Which bond wins? Same duration, different convexity.**

Bond X: D_mod = 7, C = 60. Bond Y: D_mod = 7, C = 130. Both yield the same. Estimate each bond's return for a ±200 bp shock and state which you would hold if you expected a large move of uncertain direction.

*Rates up 200 bp (Δy = +0.02):*
- X: −7(0.02) + ½(60)(0.02)² = −0.14 + 0.012 = **−12.80%**
- Y: −7(0.02) + ½(130)(0.02)² = −0.14 + 0.026 = **−11.40%**

*Rates down 200 bp (Δy = −0.02):*
- X: +0.14 + 0.012 = **+15.20%**
- Y: +0.14 + 0.026 = **+16.60%**

*Decision.* Y loses 1.4% less on the sell-off and gains 1.2% more on the rally. If a large move is likely but its direction is uncertain, hold Y — higher convexity dominates in both tails.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through why we bother with convexity if we already have duration."**

*Model answer.* Duration is a first-order, linear approximation of a curved relationship. It is accurate only for infinitesimal yield changes. Real markets move in tens or hundreds of basis points, and over those ranges the curvature matters: the true price line bows away from the duration tangent, so duration systematically overstates losses and understates gains. Convexity is the second-order term that captures that curvature. In a Taylor-series sense, price change ≈ −duration × Δy + ½ × convexity × (Δy)². Duration handles the slope; convexity handles how the slope changes. For risk management and for comparing bonds of equal duration, ignoring convexity leaves real money on the table.

**C2. "A client says two bonds have the same duration so they're the same risk. Correct them."**

*Model answer.* Equal duration means equal *sensitivity to small moves* — the first-order risk. But it says nothing about behaviour in large moves, which is governed by convexity. The more convex bond will outperform for any sizeable shift in yields, up or down, because its price gains accelerate on rallies and decelerate on sell-offs. So two equal-duration bonds are not equivalent risk: one is a better holding in volatile markets. The market prices this — the higher-convexity bond usually trades at a slightly lower yield. Duration-matching alone is insufficient for immunization or hedging when large or volatile rate moves are plausible.

**C3. "Explain negative convexity to a portfolio committee and why it matters for an MBS book."**

*Model answer.* Negative convexity means the bond's price appreciation is capped as yields fall. In an MBS, homeowners refinance when rates drop, prepaying their mortgages at par; the investor's high-coupon cash flows get returned early and must be reinvested at the new, lower rate. So the bond fails to rally the way an option-free bond would — its duration actually *shortens* into a rally, exactly when you'd want it to lengthen. The practical consequences: (1) the book gains less on rate declines than a Treasury of similar duration but loses roughly the full amount on rate rises — an unfavourable asymmetry; (2) duration is unstable, so hedges must be rebalanced dynamically; and (3) you should be compensated with extra yield (option-adjusted spread) for writing that embedded prepayment option to borrowers.

**C4. "How would you measure convexity for a callable bond, and why not use the textbook formula?"**

*Model answer.* Use *effective* convexity, not the closed-form modified convexity. The textbook formula assumes fixed cash flows, but a callable bond's cash flows change when the issuer exercises the call — precisely the behaviour that creates negative convexity. Effective convexity re-prices the bond with an option-aware model (a binomial/lattice or Monte Carlo model) under a small up-shock and down-shock to the curve: C_eff = (P₋ + P₊ − 2P₀) / [P₀ (Δy)²]. Because the model lets the option kick in, P₋ (the rally price) is suppressed relative to an option-free bond, which is what drives the numerator negative over the relevant range. That negative reading is the true economic risk the analytical formula would miss entirely.

**C5. "When would you deliberately give up convexity, and when would you pay for it?"**

*Model answer.* You pay for convexity when you expect volatility — large or uncertain rate moves — because convexity is a free lunch in both tails and acts like a long-volatility position. Long-maturity, low-coupon, and zero-coupon bonds, plus barbell structures, are ways to buy it. You give it up — selling convexity for extra carry — when you expect a calm, range-bound market: writing calls, holding callable bonds, MBS, or bullet structures earns you higher yield/spread as the premium for the short-volatility exposure. The trade-off is symmetric to an options view: convexity is essentially the gamma of the bond, and its price is the yield you forgo or earn.

---

## Section D — Multiple Choice (with reasoning)

**D1. For an option-free bond, the duration-only price estimate versus the actual price is:**
A. Always too high B. Always too low C. Too high for rate rises only D. Exactly correct

**Answer: B.** The convex price curve lies above the duration tangent line at every yield except the tangency point, so the actual price is always at least as high as the linear estimate. Duration alone therefore always understates the true price (over-predicts losses, under-predicts gains).

**D2. Which change *decreases* a bond's convexity, holding all else constant?**
A. Lengthening maturity B. Lowering the coupon C. Raising the yield to maturity D. Reducing the yield to maturity

**Answer: C.** Higher yields discount distant cash flows more heavily, compressing cash-flow dispersion and reducing both duration and convexity. Longer maturity, lower coupon, and lower yield all *raise* convexity.

**D3. A bond has D_mod = 5 and convexity = 70. For a +200 bp move, the estimated price change is closest to:**
A. −10.0% B. −8.6% C. −9.6% D. −11.4%

**Answer: B.** −5(0.02) + ½(70)(0.02)² = −0.10 + 0.014 = −0.086 = −8.6%. Duration alone gives −10.0%; the +1.4% convexity correction brings it to −8.6%.

**D4. Negative convexity is most associated with:**
A. Zero-coupon Treasuries B. Long-dated par bonds C. Mortgage-backed securities D. Short T-bills

**Answer: C.** MBS carry an embedded prepayment option that caps price appreciation as rates fall, producing negative convexity. Zeros and option-free Treasuries have positive convexity.

**D5. The correct formula for effective convexity is:**
A. (P₋ − P₊)/(2P₀Δy) B. (P₋ + P₊ − 2P₀)/(P₀(Δy)²) C. (P₊ − P₋)/(P₀Δy) D. (P₋ + P₊)/(P₀(Δy)²)

**Answer: B.** Option A is effective *duration*. B correctly captures the second difference of price around P₀, scaled by P₀ and (Δy)². D omits the −2P₀ term and would not vanish for a linear (zero-convexity) instrument.

**D6. Two bonds have identical duration. In a volatile market of uncertain direction, an investor should prefer the one with:**
A. Higher coupon B. Higher convexity C. Lower convexity D. Shorter maturity

**Answer: B.** Higher convexity outperforms in both tails — smaller losses on sell-offs, larger gains on rallies — which is exactly what you want when a large move is likely but its direction is unknown.

**D7. Convexity is analogous to which option Greek?**
A. Delta B. Theta C. Gamma D. Vega

**Answer: C.** Convexity is the second derivative of price with respect to yield, just as gamma is the second derivative of option value with respect to the underlying. Duration is the bond analogue of delta.

---

*End of Convexity Q&A bank. Rework B2–B4 until the approximation-versus-exact reconciliation falls out naturally; that single worked loop encodes the entire chapter.*
