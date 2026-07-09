# Q&A — Spot and Forward Rates

A companion practice bank for Chapter 05. Every question is followed by a full answer. Unless stated otherwise, rates are **annually compounded** and the spot curve from the chapter is reused: **z₁ = 5.00%, z₂ = 5.50%, z₃ = 6.00%**, with growth factors 1.05, (1.055)² = 1.113025, (1.06)³ = 1.191016.

---

## Section A — Concept Check

**A1. What is a spot (zero) rate, and why is it the "atom" of bond pricing?**
A spot rate zₜ is the yield on a pure discount (zero-coupon) bond that pays a single cash flow at time *t*. It is the correct rate to discount one cash flow arriving at *t*. It is the atom because any coupon bond is just a portfolio of single dated cash flows; by the law of one price, the bond must cost the sum of its cash flows each discounted at its own spot rate. Spot rates belong to the market and are coupon-independent, whereas YTM is a single blended rate belonging to one specific bond.

**A2. How does YTM relate to the spot curve?**
YTM is a single internal rate of return that reproduces a bond's price when applied to every cash flow. It is a cash-flow-weighted geometric average of the spot rates the bond touches. Two bonds of the same maturity but different coupons sample the spot curve with different weights, so they have different YTMs even in the same market. Both the spot equation and the YTM equation give the same price P; only the spot equation reflects the true term structure.

**A3. Is a forward rate a forecast of future interest rates?**
No. A forward rate is a no-arbitrage break-even implied by today's spot curve. It is the rate that makes an investor indifferent between (A) locking the long spot today and (B) investing short and rolling over at rates locked in today. It equals the market's expected future spot only under the pure expectations hypothesis with zero term premium. The gap between your own forecast and the implied forward is where a trade lives.

**A4. State the master no-arbitrage identity in words and symbols.**
Total growth from time 0 to *n* is path-independent: (1+zₙ)ⁿ = (1+z₁)(1+f₁,₂)(1+f₂,₃)···(1+f_{n-1,n}). Equivalently, the n-year spot rate is the geometric average of the sequence of one-year forward rates.

**A5. When the spot curve is upward-sloping, are forwards above or below spots? Why?**
Above. The n-year spot is the geometric average of the one-year forwards; the average of a rising sequence always lags its latest term, so the marginal (forward) rate must sit above the running average (spot). Chapter example: forwards 5% → 6% → 7.01% give a 3-year spot of 6.00%. An inverted curve reverses this — forwards lie below spots.

**A6. What is bootstrapping, and why must near coupons be stripped at previously-solved spot rates rather than at the bond's own YTM?**
Bootstrapping is the sequential extraction of the zero curve from coupon-bond (or swap) prices, shortest maturity first. Each new bond introduces exactly one new unknown spot rate; the earlier coupons are discounted at the already-solved spots, isolating that last unknown. Using the bond's own YTM to strip near coupons would re-inject the single-rate assumption you are trying to eliminate, defeating the purpose.

**A7. Give the discount-factor form of a forward growth factor.**
The forward growth factor is the ratio of the near discount factor to the far discount factor: (1+f_{k,m})^{m−k} = DF_k / DF_m, where DF_t = 1/(1+z_t)ᵗ. "Near over far" is the cleanest mnemonic.

**A8. What is an FRA, and what is its fair fixed rate?**
A Forward Rate Agreement is an OTC contract that locks an interest rate for a future borrowing/lending period on a notional principal. No principal changes hands; only the interest differential is cash-settled. Its fair fixed rate K is the implied forward rate from the spot curve. The long (would-be borrower) gains when the reference rate sets above K.

**A9. Why is an FRA settlement discounted by (1 + Lτ)?**
An FRA settles at the *start* of the reference period, but the interest differential (L−K)τ is naturally an *end*-of-period amount. Dividing by (1+Lτ) discounts that end-of-period cash flow back to the settlement date at the realized rate L. Omitting the discount overstates the payoff.

**A10. Under continuous compounding, how does the forward simplify?**
The chaining identity becomes additive: zₙ·n = z₁·1 + f₁,₂·1 + ···, so f_{k,m} = (z_m·m − z_k·k)/(m−k) — a simple weighted difference of spot rates.

---

## Section B — Numerical Bond-Math Problems (step-by-step, reconciling)

**B1. Bootstrap a 2-year spot curve.** Two annual-coupon bonds, face 100: Bond X (1-yr, 5% coupon, price 100.9615) and Bond Y (2-yr, 5% coupon, price 100.9612). Find z₁ and z₂.

Step 1 — z₁ from Bond X (pays 105 at t=1):
105 / 100.9615 = 1.04000 ⟹ **z₁ = 4.00%**.

Step 2 — z₂ from Bond Y (pays 5 at t=1, 105 at t=2). Strip the year-1 coupon at the known z₁:
5 / 1.04 = 4.80769.
100.9612 = 4.80769 + 105/(1+z₂)² ⟹ 105/(1+z₂)² = 96.15351.
(1+z₂)² = 105 / 96.15351 = 1.092025 ⟹ 1+z₂ = √1.092025 = 1.04500 ⟹ **z₂ = 4.50%**.

Reconcile — re-price Bond Y with the two spots: 5/1.04 + 105/1.092025 = 4.80769 + 96.15346 = 100.9611 ≈ 100.9612 ✓ (rounding in the last digit).

**B2. From B1's curve, find the implied one-year forward f₁,₂ and verify chaining.**
1+f₁,₂ = (1+z₂)²/(1+z₁) = 1.092025 / 1.04 = 1.050024 ⟹ **f₁,₂ = 5.00%**.
Chaining check: (1+z₁)(1+f₁,₂) = 1.04 × 1.050024 = 1.092025 = (1+z₂)² ✓. The rising curve (4% → 4.5%) produces a forward (5.00%) above both spots, as expected.

**B3. Full forward curve from a 4-year spot curve.** Given z₁=3%, z₂=3.5%, z₃=4%, z₄=4.5% (annual). Compute the three consecutive one-year forwards and confirm they chain to (1+z₄)⁴.

Growth factors: 1.03; (1.035)²=1.071225; (1.04)³=1.124864; (1.045)⁴=1.192519.

f₁,₂ = 1.071225/1.03 − 1 = 1.040024 − 1 = **4.00%**.
f₂,₃ = 1.124864/1.071225 − 1 = 1.050072 − 1 = **5.01%**.
f₃,₄ = 1.192519/1.124864 − 1 = 1.060144 − 1 = **6.01%**.

Chaining check: 1.03 × 1.040024 × 1.050072 × 1.060144
= 1.071225 × 1.050072 = 1.124864; × 1.060144 = 1.192519 = (1+z₄)⁴ ✓.
Geometric-average check: 1.192519^{1/4} = 1.045 ⟹ z₄ = 4.50% = geometric average of the four one-year rates (3%, 4.00%, 5.01%, 6.01%). The average lags the last forward because the curve rises.

**B4. Two-year forward, one year forward (f₁,₃) on the chapter curve.** Use z₁=5%, z₃=6%.
(1+f₁,₃)² = (1+z₃)³/(1+z₁) = 1.191016 / 1.05 = 1.134301.
1+f₁,₃ = √1.134301 = 1.065036 ⟹ **f₁,₃ = 6.50%**.
Cross-check via one-year forwards: (1+f₁,₂)(1+f₂,₃) = 1.060024 × 1.070073 = 1.134301, and √1.134301 = 1.065036 ✓. The 2-year forward is the geometric average of the two embedded one-year forwards (6.00% and 7.01%), giving 6.50%.

**B5. Price a 3-year 4% annual-coupon bond off the chapter spot curve, then find its YTM sign relative to spots.**
Cash flows: 4, 4, 104.
PV = 4/1.05 + 4/1.113025 + 104/1.191016
= 3.80952 + 3.59380 + 87.31989 = **94.7232**.
Because the bond trades below par (94.72 < 100) with a below-market coupon, its YTM exceeds its coupon and lands between z₁ and z₃, weighted toward z₃ (the largest cash flow, 104, is at t=3). Quick sanity: discounting all flows at a flat 5.94% gives ≈ 4/1.0594 + 4/1.0594² + 104/1.0594³ ≈ 3.776 + 3.564 + 87.38 ≈ 94.72, so YTM ≈ 5.94%, just below z₃ = 6.00% — consistent, since a coupon bond's YTM is a cash-flow-weighted average of spots dominated by the final payment. ✓

**B6. Price a 6×12 FRA and settle it.** Notional \$10,000,000. Money-market spots (simple, Act with τ=0.5 each period): 6-month = 4.00%, 12-month = 4.50%.
Fair rate: (1 + 0.04×0.5)(1 + K×0.5) = (1 + 0.045×1).
1.02 (1 + 0.5K) = 1.045 ⟹ 1 + 0.5K = 1.045/1.02 = 1.024510 ⟹ **K = 4.902%**.
Settlement at L = 5.50%:
Payoff to long = N·(L−K)τ / (1+Lτ) = 10,000,000 × (0.055 − 0.04902)(0.5) / (1 + 0.055×0.5)
= 10,000,000 × (0.00598×0.5) / 1.0275 = 29,900 / 1.0275 = **\$29,101** received at the 6-month settlement.
Reconcile the hedge: the extra borrowing cost of paying 5.50% instead of 4.902% over the 6-month loan, measured at period-end (month 12), is 10,000,000 × 0.00598 × 0.5 = \$29,900. Carry the FRA receipt forward at realized 5.50%: 29,101 × 1.0275 = \$29,901 ≈ \$29,900 ✓. The effective all-in borrowing rate stays 4.902%.

**B7. Price and settle a 3×9 FRA (new numbers).** Notional \$5,000,000. Simple money-market spots: 3-month = 3.00% (τ₁=0.25), 9-month = 3.60% (τ₂=0.75); reference period τ_fwd = 0.50.
Fair rate: (1 + 0.03×0.25)(1 + K×0.5) = (1 + 0.036×0.75).
1.0075 (1 + 0.5K) = 1.0270 ⟹ 1 + 0.5K = 1.0270/1.0075 = 1.019355 ⟹ **K = 3.871%**.
Settlement at L = 4.50%:
Payoff to long = 5,000,000 × (0.045 − 0.03871)(0.5) / (1 + 0.045×0.5)
= 5,000,000 × (0.00629×0.5) / 1.0225 = 15,725 / 1.0225 = **\$15,379** at the 3-month settlement.
Direction check: rates rose above the locked K, and the long (borrower) receives cash — correct sign. ✓

**B8. Continuous-compounding forward.** Given continuously-compounded spots z₂ = 5.50% and z₃ = 6.00%, find the one-year forward f₂,₃.
f₂,₃ = (z₃·3 − z₂·2)/(3−2) = (0.18 − 0.11)/1 = 0.07 = **7.00%**.
Note this matches the annually-compounded answer (7.01%) only approximately — the tiny gap is the compounding convention, illustrating Common Confusion #6: always state the convention.

---

## Section C — Interview-Style (with model answers)

**C1. "Walk me through why we bother with a whole spot curve instead of one YTM."**
Model answer: A single YTM discounts a coupon arriving in six months at the same rate as principal arriving in ten years, which misprices the term structure — money for different horizons genuinely commands different rates. The market prices each maturity separately, so the right primitive is a schedule of spot (zero) rates. A coupon bond is a portfolio of single cash flows, and by the law of one price it must equal the sum of those flows discounted at their own spot rates; the STRIPS program makes this literally tradeable. YTM is still useful as a summary, but it is an output — a cash-flow-weighted average of spots that is bond-specific, not a market primitive.

**C2. "A client insists the 1-year rate one year forward is the market's forecast for next year's rate. Correct them."**
Model answer: The forward is a no-arbitrage break-even, not a forecast. If z₁ = 5% and z₂ = 5.5%, then f₁,₂ = (1.055²/1.05) − 1 = 6.00% purely from arithmetic — it is the rate that equalizes investing two years at spot versus rolling one year then reinvesting. It equals the expected future spot only under the pure expectations hypothesis with no term premium. In reality, liquidity-preference and term-premium effects mean forwards typically exceed expected future spots. So a 6% forward is consistent with the market expecting, say, 5.5% next year plus a 0.5% term premium. The divergence between a client's genuine forecast and the implied forward is exactly where a directional rates trade is expressed.

**C3. "How would you build a zero curve from the instruments you can actually trade?"**
Model answer: Bootstrapping. Start at the short end: the 1-year instrument gives z₁ directly. Then take the 2-year coupon bond, discount its year-1 coupon at the already-known z₁, subtract that from the price, and the residual is the single discounted final cash flow — solve for z₂. March outward; each successive bond adds exactly one new unknown spot rate. The critical discipline is to strip earlier coupons at previously-solved *spot* rates, never at the bond's own YTM, otherwise you smuggle the single-rate error back in. In modern practice the swap curve, not government bonds, is what gets bootstrapped, because swap par rates give a clean, liquid, evenly-spaced set of tenors.

**C4. "Explain how an FRA is priced and how it hedges a future funding cost."**
Model answer: An FRA's fixed rate is just the implied forward from the money-market spot curve, enforced by cash-and-carry replication — a dealer quoting off-market gets arbitraged. Suppose a treasurer must borrow \$10m for six months, six months from now. From 6-month and 12-month spots the fair 6×12 rate solves to about 4.902%. Going long the FRA locks that rate. If the reference rate later sets at 5.50%, the firm borrows more expensively in cash markets, but the FRA pays the discounted differential — about \$29,101 at settlement, which carried forward at the realized rate exactly offsets the extra \$29,900 of interest at period-end. The effective all-in rate is pinned at 4.902% regardless of where rates set. Key subtlety: settlement is at the *start* of the reference period, so the differential is discounted by (1+Lτ).

**C5. "The spot curve is steeply upward-sloping. What does that tell you about forwards, and what does it not tell you?"**
Model answer: Mechanically, an upward-sloping spot curve forces forwards to lie above spots — the spot is the geometric average of the one-year forwards, and an average must trail a rising marginal series. So each successive one-year forward is higher than the last. What it does *not* cleanly tell you is that the market expects rates to rise by that much: forwards embed a term premium. A steep curve is consistent with flat expected future short rates plus a positive term premium. So I would decompose the forward into an expectations component and a premium before drawing any macro conclusion.

**C6. "What's the single identity you'd never want a fixed-income analyst to forget?"**
Model answer: Path-independence of growth under no arbitrage: (1+zₙ)ⁿ = ∏(1+f_{k,k+1}). Whether you hold the long spot to maturity or roll a sequence of forwards you locked in today, terminal wealth is identical — otherwise there is a riskless arbitrage. Everything else in the chapter — spot-to-forward conversion, the geometric-average intuition, bootstrapping, FRA pricing — is a rearrangement of that one statement.

---

## Section D — Multiple Choice (with reasoning)

**D1.** With z₁ = 5%, z₂ = 5.5%, the one-year forward f₁,₂ is closest to:
(a) 5.0% (b) 5.25% (c) 6.0% (d) 5.5%
**Answer: (c).** f₁,₂ = (1.055²/1.05) − 1 = (1.113025/1.05) − 1 = 6.00%. Since the curve rises, the forward exceeds both spots, ruling out (a), (b), (d).

**D2.** Which statement about YTM is TRUE?
(a) It is coupon-independent. (b) It equals the average spot rate weighted equally. (c) It is a cash-flow-weighted average of spot rates and is bond-specific. (d) It always exceeds every spot rate the bond touches.
**Answer: (c).** YTM blends the spots the bond's cash flows touch, weighted by timing and size, so it differs across bonds of equal maturity but different coupons — hence bond-specific, not coupon-independent, eliminating (a). Weights are not equal (b), and YTM lies within the range of relevant spots, not above all of them (d).

**D3.** In bootstrapping the 2-year spot, the year-1 coupon should be discounted at:
(a) the 2-year bond's YTM (b) the already-solved 1-year spot z₁ (c) the 2-year spot z₂ (d) the coupon rate
**Answer: (b).** The whole point is to isolate z₂; earlier coupons must be stripped at previously-solved spot rates. Using YTM (a) reintroduces the single-rate assumption; z₂ (c) is the unknown you are solving for.

**D4.** A 6×12 FRA covers a reference period that:
(a) starts today, ends in 6 months (b) starts in 6 months, ends in 12 months (c) starts in 12 months, lasts 6 months (d) starts in 6 months, lasts 12 months
**Answer: (b).** "a×b" means the period starts at month a and ends at month b, so 6×12 is the 6-month period beginning in 6 months.

**D5.** The FRA settlement amount is divided by (1+Lτ) because:
(a) it converts to continuous compounding (b) the differential is an end-of-period amount settled at period start, so it must be discounted (c) it adjusts for credit risk (d) it annualizes the payoff
**Answer: (b).** FRAs settle at the start of the reference period while the interest differential accrues to period-end; discounting at the realized rate L brings it back to the settlement date.

**D6.** Under continuous compounding, the forward f_{k,m} equals:
(a) (z_m·m − z_k·k)/(m−k) (b) (z_m − z_k)/(m−k) (c) z_m·m − z_k·k (d) √(z_m·z_k)
**Answer: (a).** Continuous compounding makes the chaining identity additive in rate×time, so the forward is the weighted difference (z_m·m − z_k·k)/(m−k).

**D7.** When the spot curve is inverted (downward-sloping), forward rates:
(a) lie above spot rates (b) equal spot rates (c) lie below spot rates (d) are undefined
**Answer: (c).** The spot is the geometric average of the forwards; if the average falls with maturity, the marginal forward must be below the running average — forwards lie below spots. Mirror image of the rising-curve case.

**D8.** Given z₁=5%, z₂=5.5%, z₃=6%, the 3-year spot is BEST described as:
(a) the arithmetic mean of the three spots (b) the geometric average of the one-year forwards 5%, 6%, 7.01% (c) equal to the 3-year forward (d) the highest forward rate
**Answer: (b).** (1+z₃)³ = 1.05 × 1.060024 × 1.070073 = 1.191016, so z₃ = 6.00% is the geometric average of the one-year forwards. It is below the last forward (7.01%), ruling out (d).

**D9.** The forward growth factor between k and m in discount-factor terms is:
(a) DF_m / DF_k (b) DF_k / DF_m (c) DF_k × DF_m (d) DF_k − DF_m
**Answer: (b).** (1+f_{k,m})^{m−k} = DF_k/DF_m — "near over far." DF_k (nearer, larger) divided by DF_m (farther, smaller) exceeds 1, as a growth factor must.

**D10.** A long FRA position profits when:
(a) the reference rate sets below K (b) the reference rate sets above K (c) the spot curve inverts (d) the notional is repaid
**Answer: (b).** The long is a would-be borrower who locked K; if the reference rate sets above K, borrowing got more expensive and the FRA pays the long to compensate.

---

*End of Q&A — Spot and Forward Rates. All numerical answers were self-verified against the chapter's growth factors (1.05, 1.113025, 1.191016) and the no-arbitrage chaining identity.*
