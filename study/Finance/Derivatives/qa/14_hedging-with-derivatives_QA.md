# Q&A — Hedging with Derivatives

A practice bank built around one master equation: ΔΠ = ΔS + h·ΔF. Every question below is really asking "how do I choose h so the price risk cancels — and what is left over when it can't cancel perfectly?" Direct hedges, cross-hedges, delta, and duration are all the same idea with a different h.

---

## Section A — Concept Check

**A1. What does a hedge actually do, and what is the single equation that captures it?**

A hedge is a deliberately taken position whose value moves *opposite* to an existing exposure, so the combined portfolio is far less sensitive to the risky price. If the exposure has spot value S and you hold h units of an instrument with value F, the hedged portfolio is Π = S + h·F, and its change for a small market move is ΔΠ = ΔS + h·ΔF. The entire craft is choosing h so that h·ΔF ≈ −ΔS across the likely range of moves. Hedging does not eliminate risk; it engineers an offsetting payoff so the risk factor drops out of the sum.

**A2. Why does a currency forward hedge lock in a rate *exactly*, while a jet-fuel-with-crude hedge does not?**

Because the forward is written on the *same* asset as the exposure. An exporter with USD 1,000,000 receivable worth 1,000,000 × S in rupees, who sells USD forward at F₀, receives 1,000,000 × (F₀ − S) on the forward; the two add to 1,000,000 × F₀ and S cancels algebraically. When the hedge instrument is a *different* asset (crude for jet fuel), ΔF is only correlated with ΔS, not identical to it, so the cancellation is statistical, not algebraic — a residual (basis) always survives.

**A3. State and interpret the minimum-variance hedge ratio.**

h* = ρ·(σ_S/σ_F), where σ_S and σ_F are the standard deviations of spot and futures changes and ρ their correlation. It is the h that minimizes the variance of the hedged portfolio, and it is exactly the slope coefficient β from regressing spot changes on futures changes, ΔS = α + β·ΔF + ε. Practically, you estimate it by OLS on historical data matched to your rebalancing frequency.

**A4. What is "hedge effectiveness," and how is it read off the same regression?**

Hedge effectiveness is the fraction of variance the optimal hedge removes, and it equals ρ² — the R² of the ΔS-on-ΔF regression. Substituting h* back into the variance formula gives a minimized variance of σ_S²(1 − ρ²), so ρ² is removed and (1 − ρ²) survives as basis risk. This tells you *before* you trade the best the hedge can possibly do: if ρ = 0.90, at most ~81% of variance is removable.

**A5. Define basis and basis risk, and name the two distinct sources.**

Basis b = S − F (spot minus futures). Basis risk is the uncertainty in the *terminal* basis b_T, because a hedge locks the initial futures price F₀ but leaves the effective price = F₀ + b_T exposed to how the basis ends up. Two sources: (1) **cross-asset basis** — the hedge asset differs from the exposure asset (jet fuel ≠ crude), governed by ρ < 1; and (2) **calendar/convergence basis** — even for the same asset, if the hedge is lifted before delivery, S and F may not have converged. Choosing a maturity just beyond the horizon minimizes the second.

**A6. Why is delta hedging *dynamic* while an FX forward hedge is *static*?**

An option's payoff is curved, so its sensitivity to the underlying (delta, Δ = ∂V/∂S) is not constant — it changes as the underlying moves, and the rate of that change is gamma (Γ = ∂Δ/∂S). Setting h = −Δ neutralizes the position only *locally*; as S moves, Δ drifts and the hedge must be rebalanced. An FX forward's sensitivity to the exchange rate is constant (−1 per unit), so it is placed once and held — "set and forget."

**A7. Why can *over-hedging* be more dangerous than not hedging at all?**

Beyond full coverage (h > h*), the hedge overshoots the exposure and becomes a *net speculative position in the opposite direction*. If prices then move favorably for the underlying business, the oversized hedge loses more than the exposure gains. Maximum safety sits at the minimum-variance ratio, not the maximum position. The usual trigger is quantity/volumetric risk — you hedge a forecast volume, demand collapses, and you are left holding hedges against volume you never buy.

**A8. Under Modigliani-Miller hedging is value-neutral. So why do firms hedge?**

Because real markets have frictions MM assumes away: reducing financial-distress and bankruptcy costs by smoothing cash flows (the strongest justification); preserving debt capacity and investment (the Froot-Scharfstein-Stein underinvestment argument); lowering expected taxes under a convex tax schedule; and exploiting an information advantage (an airline knows its own fuel volume better than outside investors). Absent these frictions, hedging just burns transaction costs.

---

## Section B — Numerical / Applied Problems (full solutions)

**B1. Direct FX forward hedge — prove the rate locks in both directions.**

*Given:* Exporter receives USD 1,000,000 in 3 months; sells it forward at F₀ = 83.60 INR/USD.

Scenario A — rupee strengthens to S_T = 81.00:
- Receivable at spot = 1,000,000 × 81.00 = ₹81,000,000
- Forward payoff = 1,000,000 × (83.60 − 81.00) = +₹2,600,000
- Total = **₹83,600,000**

Scenario B — rupee weakens to S_T = 85.00:
- Receivable at spot = 1,000,000 × 85.00 = ₹85,000,000
- Forward payoff = 1,000,000 × (83.60 − 85.00) = −₹1,400,000
- Total = **₹83,600,000**

*Reconcile:* Both net to 1,000,000 × F₀ = ₹83,600,000. Spot has cancelled. The hedge removed downside *and* upside — the defining trade-off of a forward.

**B2. Minimum-variance hedge ratio for a cross-hedge.**

*Given:* Airline buys 2,100,000 gallons of jet fuel in 2 months; hedges with WTI crude futures (42,000 gallons/contract). σ_S = 0.036, σ_F = 0.040, ρ = 0.90.

Step 1 — h* = ρ·(σ_S/σ_F) = 0.90 × (0.036/0.040) = 0.90 × 0.90 = **0.81**.
Step 2 — N* = h* × (Q_A/Q_F) = 0.81 × (2,100,000/42,000) = 0.81 × 50 = 40.5 ≈ **41 contracts, long**.
Step 3 — Effectiveness = ρ² = 0.81 → the hedge removes ~**81% of variance**; ~19% survives as basis risk.

*Reconcile:* The airline is short fuel (must buy), so it goes long the hedge. h* < 1 because ρ < 1 and σ_S < σ_F; using a naïve 1:1 hedge would over-hedge.

**B3. Realized outcome of the cross-hedge with a basis move.**

*Given:* Over 2 months crude futures gain \$5.00/barrel = \$0.1190/gallon; jet fuel rises \$0.105/gallon.

Step 1 — Futures gain = 41 × 42,000 × 0.1190 ≈ **\$204,600**.
Step 2 — Extra fuel cost = 2,100,000 × 0.105 = **\$220,500**.
Step 3 — Net residual = 220,500 − 204,600 = **\$15,900** unhedged.

*Reconcile:* Unhedged, the airline faced \$220,500 of exposure; the hedge absorbed 204,600/220,500 ≈ 93% of *this* move. The \$15,900 gap is realized basis risk (fuel rose more per unit than the 0.81 ratio predicted). Over many moves, average variance reduction converges to the ρ² = 81% figure.

**B4. Duration hedge of a bond portfolio.**

*Given:* Portfolio value P = \$50,000,000, modified duration D_P = 6.5. T-bond futures at F = \$120,000/contract, futures duration D_F = 8.0. Treasurer fears rising rates.

Step 1 — N* = −(D_P × P)/(D_F × F) = −(6.5 × 50,000,000)/(8.0 × 120,000) = −325,000,000/960,000 ≈ **−338.5 → sell 339 contracts**.

Check with a +50 bp shift (Δy = +0.005):
- Portfolio loss ≈ −D_P × P × Δy = −6.5 × 50,000,000 × 0.005 = −\$1,625,000.
- Each futures gains ≈ D_F × F × Δy = 8.0 × 120,000 × 0.005 = \$4,800; total = 339 × 4,800 = \$1,627,200.
- Net = 1,627,200 − 1,625,000 = **+\$2,200** (essentially flat; surplus is rounding 338.5 → 339).

*Reconcile:* She is long bonds and fears rate rises, so she shorts futures. Residuals remain: non-parallel twists, convexity for large Δy, and duration drift — all needing rebalancing.

**B5. Delta hedge of a short call.**

*Given:* A dealer is short 100 call options (each on 1 share) with delta Δ = 0.6.

Step 1 — Hedge = −Δ per option written; being short the call, the dealer holds +Δ shares to offset. Shares to buy = 0.6 × 100 = **60 shares**.
Step 2 — Stock rises \$1: short calls lose ≈ 100 × 0.6 × \$1 = \$60; 60 shares gain 60 × \$1 = \$60. Net ≈ **0** for the small move.

*Reconcile:* Correct locally. But if the stock keeps rising, Δ climbs toward 1 (positive gamma on the long-stock/short-call book behaves the opposite way), so the 60-share hedge is soon wrong and must be rebalanced. That rebalancing need *is* gamma.

**B6. Beta hedge of an equity portfolio (same formula, different h).**

*Given:* Portfolio V_P = ₹6,00,00,000, beta = 1.1. Index futures contract value V_F = ₹10,00,000. Fully hedge market risk.

Step 1 — N = β × (V_P/V_F) = 1.1 × (6,00,00,000/10,00,000) = 1.1 × 60 = **66 contracts, short**.
Step 2 — Sanity: index falls 10% → β=1.1 portfolio loses ≈ 11% × 6,00,00,000 = ₹66,00,000; 66 short futures gain 66 × (10% × 10,00,000) = 66 × 1,00,000 = ₹66,00,000. Cancels.

*Reconcile:* This is h* = ρσ_S/σ_F rebadged — β is the hedge ratio, and the hedge neutralizes *systematic* risk only; idiosyncratic (stock-specific) risk survives.

**B7. Effective price via the basis rule.**

*Given:* A miller shorts wheat futures at F₀ = ₹2,250 to hedge a May sale. At unwind, spot = ₹2,100, futures = ₹2,130.

Step 1 — Terminal basis b_T = S_T − F_T = 2,100 − 2,130 = −₹30.
Step 2 — Effective price = F₀ + b_T = 2,250 + (−30) = **₹2,220/quintal**.
Step 3 — Cross-check via cash flows: spot sale ₹2,100 + futures gain (2,250 − 2,130 = ₹120) = ₹2,220. Same.

*Reconcile:* The miller locked the ₹2,250 futures level adjusted by the ending basis. Two independent methods agree; the residual vs the naïve ₹2,250 is precisely realized basis risk.

**B8. Over-hedging turns a hedge into speculation.**

*Given:* Airline hedges 50 contracts of expected fuel burn; a recession cuts flying so true need is only 30 contracts' worth. Crude then *falls* \$8/barrel; each contract = 1,000 barrels.

Step 1 — Benefit from cheaper fuel actually bought = 30 × 1,000 × 8 = **\$240,000 saved**.
Step 2 — But the airline is long 50 futures, which lose 50 × 1,000 × 8 = **\$400,000**.
Step 3 — Net = 240,000 − 400,000 = **−\$160,000**.

*Reconcile:* The 20 excess contracts are a naked speculative long that lost when prices moved *favorably* for the business — exactly how well-intentioned hedges (airlines in 2008, Metallgesellschaft) produced losses. Defense: hedge a conservative fraction of uncertain volume, or use options.

---

## Section C — Interview-Style (model answers)

**C1. "Walk me through hedging an Indian IT exporter's dollar receivable. What are you giving up?"**

*Model answer:* The exporter is long dollars — it will receive USD and convert to rupees, so it loses if the rupee strengthens. I'd sell the dollars forward at the locked rate F₀; the forward pays 1,000,000 × (F₀ − S), which rises exactly as the receivable's rupee value falls, so the two sum to 1,000,000 × F₀ regardless of spot. What I give up is the upside: if the rupee weakens, the better conversion is handed straight back on the forward. If the firm wants to keep that upside, I'd use a dollar put (a floor) instead, paying a premium to remove downside while retaining upside. Choosing forward versus option is really a decision about the *shape* of the hedge, not just its size.

**C2. "Why is the minimum-variance hedge ratio for a cross-hedge usually well below 1?"**

*Model answer:* Because h* = ρ·σ_S/σ_F, and for a cross-hedge neither ρ = 1 nor σ_S = σ_F holds. Jet fuel and crude are correlated but not identical (ρ maybe 0.9), and their volatilities differ, so h* comes out around 0.8, not 1. If I blindly hedged 1:1, I'd over-hedge — putting on more futures than the correlation justifies — which *adds* variance in the opposite direction rather than removing it. The clean way to say it: h* is the regression beta of spot changes on futures changes, and hedge effectiveness is that regression's R² = ρ². The numbers tell me both how much to trade and how good the hedge can possibly be.

**C3. "Your portfolio was 'fully hedged' with index futures and still lost money. Explain."**

*Model answer:* Index futures neutralize *systematic* (market) risk, not the stock-specific risk of my particular names. Beta captures average sensitivity to the index, so a full beta-adjusted short takes market beta to roughly zero — but if my holdings underperformed the index, that idiosyncratic drift leaks straight through. Beta is also estimated: if realized beta differed, the hedge was mis-sized, and rolling contracts through contango bleeds a little each roll. "Fully hedged" removes direction, not tracking error, financing drag, or estimation error.

**C4. "When would you use options instead of futures to hedge?"**

*Model answer:* Primarily when the hedged *quantity* is uncertain, or when the firm values keeping upside. A future or forward locks the price both ways and commits me to a fixed notional; if my volume forecast is wrong, I can be left with an oversized position that becomes a speculative leg — the classic airline-in-a-recession trap. An option caps my maximum loss at the premium, so I can't be forced into a losing speculative position on volume I never had. The cost is the premium — I'm paying for asymmetry. So: known quantity and pure variance reduction → forwards/futures; uncertain quantity or valued upside → options.

**C5. "Explain basis risk to a treasurer who thinks a hedge should be perfect."**

*Model answer:* A hedge is perfect only if the instrument is the same asset held to convergence. In practice you often hedge with a related but different asset — a corporate bond with Treasury futures — because that's what's liquid. The basis, S − F, then moves for three reasons: the assets differ, they trade in different locations, and you usually lift the hedge before expiry when S and F haven't converged. You lock the *initial* futures price but stay exposed to the *terminal* basis. You can minimize this — most correlated asset, nearest maturity just beyond your horizon, right location — but not remove it. If you could, it would be a direct hedge. Basis risk is the price of using a liquid but imperfect instrument.

---

## Section D — MCQs with Reasoning

**D1.** The minimum-variance hedge ratio equals exactly 1.0 only when:
A) Correlation is zero
B) Spot and futures volatilities are equal AND correlation is 1
C) The futures is more volatile than the spot
D) The asset pays no dividend

**Answer: B.** h* = ρ·σ_S/σ_F = 1 requires both ρ = 1 and σ_S = σ_F. A) gives h* = 0; C) makes σ_S/σ_F < 1 so h* < 1; D) is unrelated to the hedge ratio. Only B satisfies the algebra.

**D2.** Hedge effectiveness — the fraction of variance removed by the optimal hedge — equals:
A) ρ
B) ρ²
C) 1 − ρ
D) σ_S/σ_F

**Answer: B.** Substituting h* back gives minimized variance σ_S²(1 − ρ²), so the fraction removed is ρ² (the regression R²). A) confuses correlation with variance explained; C) is the *residual* fraction; D) is part of the hedge ratio, not effectiveness.

**D3.** An airline that will *buy* fuel in three months should, to hedge, take which futures position?
A) Short futures
B) Long futures
C) No position — buying is not an exposure
D) Sell options

**Answer: B.** The airline is short the commodity (it must buy), so it goes long the hedge — a price rise costs it more on the physical but is offset by gains on the long futures. A) would double the exposure; C) ignores that a future purchase at an unknown price *is* an exposure.

**D4.** Basis is defined as, and converges to, respectively:
A) F − S; converges to F₀
B) S − F; converges to zero at delivery
C) S − K; converges to intrinsic value
D) F − fair value; converges to the risk-free rate

**Answer: B.** Basis = Spot − Futures, and at delivery the carry period is zero so F = S, making the basis zero. A) sign-flips the standard hedging convention; C) confuses futures with options; D) describes mispricing, not basis.

**D5.** Over-hedging (holding more contracts than the exposure) is dangerous because:
A) It always increases transaction costs to infinity
B) Beyond full coverage the hedge becomes a net speculative position in the opposite direction
C) It makes the basis negative
D) It suspends convergence

**Answer: B.** Past h*, the excess contracts are an unhedged directional bet; if prices move favorably for the business, the oversized hedge loses more than the exposure gains. A) overstates a real but secondary cost; C) and D) are unrelated mechanisms.

**D6.** Delta hedging must be rebalanced, whereas an FX forward hedge need not, because:
A) FX markets never move
B) Delta changes as the underlying moves (gamma), while a forward's sensitivity is constant
C) Options have no sensitivity to the underlying
D) Forwards are marked to market and options are not

**Answer: B.** An option's delta drifts with the underlying (that drift is gamma), so a delta hedge is only locally correct and needs continual rebalancing; a forward's sensitivity to the exchange rate is a constant −1 per unit, so it is static. C) is false; D) is backwards (futures, not options, are the marked-to-market ones).

**D7.** Under Modigliani-Miller, corporate hedging is value-neutral. Therefore real-world hedging creates value primarily through:
A) Guaranteeing the firm beats the market
B) Frictions — distress costs, taxes, underinvestment, and information advantages
C) Eliminating all business risk
D) Raising the firm's beta

**Answer: B.** Every genuine justification is a *deviation* from MM's frictionless world: smoothing cash flows to avoid distress and underinvestment, lowering expected taxes under convexity, and exploiting an information edge. A) misstates hedging as a bet; C) hedging removes *price* risk, not business risk; D) is unrelated.

**D8.** The number of futures to duration-hedge a bond portfolio is N* = −(D_P·P)/(D_F·F). This hedge protects against:
A) Any interest-rate move of any size
B) Small, parallel yield shifts only
C) Curve twists specifically
D) Credit-spread widening

**Answer: B.** Duration is a first-order, linear approximation, so the hedge covers only small, *parallel* shifts. Large moves leak through convexity (duration's gamma-analogue) and non-parallel twists leak through entirely; A) and C) overstate coverage. D) is a different risk factor.

---

## Self-Verification Notes

- B2's h* = 0.81 and N* = 41 contracts feed directly into B3, where the futures gain (41 × 42,000 × 0.1190 ≈ \$204,600) is computed on that exact position; the \$15,900 residual matches the ρ²/basis-risk narrative.
- B1's forward hedge nets to ₹83,600,000 = 1,000,000 × F₀ in *both* scenarios — the algebraic cancellation is demonstrated, not asserted.
- B4's duration hedge reconciles to +\$2,200 (≈0) on a 50 bp shift, the small surplus explained by rounding 338.5 → 339.
- B7's effective price ₹2,220 is confirmed by two independent methods (F₀ + terminal basis, and spot sale + futures P&L).
- B6 (beta hedge) is explicitly flagged as the same h* = ρσ_S/σ_F formula with β as the hedge ratio, consistent with Section A3.
- MCQ answers cross-reference the worked numbers and concepts: D1↔A3, D2↔A4, D3↔B2, D5↔B8/A7, D6↔A6/B5, D7↔A8, D8↔B4. No internal contradictions found.
