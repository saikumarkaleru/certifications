# Q&A — Bond Portfolio Strategies

A companion practice bank for Chapter 15. Work each question before reading the answer. Numerical answers show full working so you can audit every step.

---

## Section A — Concept Checks

**A1. What single axis organises the entire menu of bond portfolio strategies, and how does it split the menu?**

The organising axis is *how much you trust the market's current pricing × how much freedom the mandate gives you to bet against it*. It splits strategy into **passive** (accept today's curve and spreads as the best available forecast and *match* an index, liability or horizon) and **active** (reject the idea that current pricing is the last word and *beat* the market by positioning around a forecast that diverges from what prices imply). Between the poles is a spectrum — enhanced indexing, core-satellite, contingent immunisation — not a binary.

**A2. Why is passive fixed-income management rarely literal replication?**

A broad aggregate index can contain thousands of illiquid issues that never trade, so buying every CUSIP ("full replication") is impossible. Passive managers instead use **stratified sampling / cell-matching**: partition the index by sector × quality × maturity/duration bucket and hold a tractable subset whose weight and contribution-to-duration match the index cell by cell. It works because *matching the risk factors matches the return* even without holding every bond.

**A3. Explain the mechanism by which immunisation protects a horizon value.**

Rate risk is two-sided: a rate rise depresses a bond's sale price but raises the coupon reinvestment rate; a fall does the opposite. These forces cross at exactly one horizon — the **Macaulay duration**. Set asset duration equal to the liability horizon (and PV assets = PV liability), and to first order a one-time parallel shift leaves the horizon accumulated value unchanged: the reinvestment loss/gain offsets the price gain/loss. You have deliberately positioned at the crossover point.

**A4. Why does cash-flow matching need no interest-rate assumption while immunisation does?**

Cash-flow matching *eliminates* rate risk by construction — bonds whose coupons and principal land on the liabilities' dates and amounts mean the cash is already there when each liability falls due, so you neither sell nor reinvest and the intervening rate path is irrelevant. Immunisation only *offsets* risk via the duration crossover, which holds exactly only for small parallel shifts — hence it assumes parallel movement and needs rebalancing.

**A5. State the three Redington conditions for multiple-liability immunisation.**

1. PV(assets) = PV(liabilities).
2. Duration of assets = duration of liabilities (dollar durations equal).
3. Convexity/dispersion of assets ≥ convexity of liabilities, with asset cash flows *bracketing* the liability cash flows in time. Condition 3 makes the surplus a local minimum that is protected against small parallel shifts.

**A6. Where does the "edge" that justifies any active trade come from?**

Always the same shape: a probability-weighted forecast of realised rates/curve/spreads that *diverges from the forecast baked into current prices* (forward rates for the curve, the spread itself for credit). Extend duration if you expect rates to fall by more than forwards imply; steepen/flatten if you expect the curve to reshape differently than forwards imply; overweight credit if you expect spreads to tighten more than the carry already pays for. No divergence, no trade — only tracking error.

**A7. What are the three roughly independent ways the yield curve moves, and which strategy family targets each?**

**Level (parallel shift)** — targeted by rate-anticipation duration tilts. **Slope (steepen/flatten)** — targeted by steepener/flattener and barbell/bullet trades held duration-neutral. **Curvature (butterfly/hump)** — targeted by bullet vs barbell positioning across the belly. Key-rate (partial) durations decompose total duration by maturity point so a manager can target a specific section.

**A8. Distinguish a ladder, a bullet, and a barbell.**

A **ladder** spreads maturities evenly across a horizon; it is self-averaging (constant average maturity, continually reinvesting a slice), needs no forecast, and has low curve-shape risk. A **bullet** clusters all maturities at one point — outperforms when the curve flattens/becomes less curved (benefits from the belly), earns more carry on a stable curve. A **barbell** holds only short + long ends (no belly) — more convex than a duration-matched bullet, so it wins on large parallel moves and steepeners, but the market charges for that convexity via a lower yield.

**A9. What is contingent immunisation?**

Active management wrapped in a stop-loss. You manage actively as long as portfolio value stays above a **floor** (the amount that, immunised today, would still fund the liability at horizon). The gap between current value and the floor is the **cushion**. Trade actively while a cushion exists; the instant active losses erode the cushion to zero, stop and immunise, locking the minimum acceptable return. It buys upside optionality with a hard floor.

---

## Section B — Numerical / Applied

**B1. Single-liability immunisation with a zero.** A fund owes 1,000,000 in 5 years. The flat curve is 8%. How much is invested today, what face of a 5-year zero is bought, and prove the liability is still met if yields jump to 10% immediately after purchase.

*Solution.* PV of liability = 1,000,000 / 1.08⁵ = 1,000,000 / 1.469328 = **680,583**, invested today. A 5-year zero has Macaulay duration = 5 exactly, matching the horizon. Face needed = 680,583 × 1.469328 = **1,000,000** at maturity. If yields jump to 10% right after purchase, the zero still matures at 1,000,000 in year 5 — it has no coupons to reinvest and is held to maturity, so its terminal value is unaffected by the intervening yield. Accumulated value at year 5 = **1,000,000 = liability**. The zero immunises *exactly* for any shift because each side of the offset (price risk, reinvestment risk) is individually zero.

**B2. The offset for a coupon bond.** Explain qualitatively, for a duration-5 portfolio built from an 8% six-year coupon bond funding the same 1,000,000 liability, what happens to the two effects if yields jump to 10%, and why the horizon value still lands near 1,000,000.

*Solution.* Coupons in years 1–5 now reinvest at 10% not 8% → the reinvestment pot at year 5 is **larger** than planned. The bond is sold at year 5 with one year left, discounted at 10% not 8% → the sale price is **lower** than planned. Because duration = horizon = 5, these effects **offset** to first order, landing the accumulated value very close to 1,000,000 (slightly above, thanks to positive convexity). Had yields fallen to 6%, the pot shrinks but the sale price rises — again offsetting. Unlike the zero, this is only approximate for small shifts and must be rebalanced as its duration drifts.

**B3. Riding the curve.** Static upward curve: 1y spot 3.0% (price 97.087), 2y 4.0% (92.456), 3y 5.0% (86.384). Compare buy-and-hold a 1-year zero versus buying the 3-year zero and selling in one year.

*Solution.* Buy-and-hold 1y zero: 100 / 97.087 − 1 = **3.00%**. Ride the curve: buy 3y zero at 86.384; one year later, if the curve is unchanged, it is a 2-year zero priced at the 2y point = 100 / 1.04² = 92.456. Return = 92.456 / 86.384 − 1 = **7.03%**. The bond's own yield fell from 5% to 4% purely by aging down a static curve.

**B4. Decompose the rolldown return in B3.**

*Solution.* Carry/yield portion — one year of accretion at the original 5% purchase yield: 86.384 × 1.05 = 90.703, i.e. **+4.99%**. Rolldown portion — extra price gain because the yield dropped to 4%: 92.456 − 90.703 = 1.753, i.e. 1.753 / 86.384 = **+2.03%**. Total 4.99% + 2.03% = **7.03%**, matching B3.

**B5. The catch in B3.** If instead the whole curve shifts up 1% over the year (so the bond becomes a 2y zero yielding 5.0%), what is the ride-the-curve return, and what does the shrunk edge represent?

*Solution.* New price = 100 / 1.05² = 90.703. Return = 90.703 / 86.384 − 1 = **5.00%**. Still beats the 3% buy-and-hold, but the rolldown edge shrank from ~4 pts to ~2 pts. A larger rise (belly to ~5.9% → price ~89.2 → return ~3.3%) erases nearly the whole advantage. The extra return in the static case was **compensation for the curve-shift risk you bear**, not free money.

**B6. Duration tilt / enhanced indexing.** Benchmark modified duration 6.0. Portfolio of 100 mn; mandate keeps duration within ±0.5 of benchmark. Manager is mildly bearish and targets duration 5.6 using short bond S (dur 2.0) and long bond L (dur 9.0). Find the weights.

*Solution.* Let w = weight in L. D_P = 9.0w + 2.0(1−w) = 5.6 → 2.0 + 7.0w = 5.6 → w = 3.6 / 7.0 = **0.5143**. So **51.43 mn in L, 48.57 mn in S**. Check: 0.5143(9) + 0.4857(2) = 4.629 + 0.971 = **5.60**.

**B7. P&L of the B6 tilt.** Rates rise 50 bp parallel. What does the defensive tilt save versus a benchmark-duration portfolio?

*Solution.* Portfolio: ΔP/P ≈ −5.6 × 0.005 = −2.80% → loss ≈ 2.80 mn. Benchmark-duration (6.0): ≈ −3.00% → loss ≈ 3.00 mn. The tilt **saved ≈ 0.20 mn = 20 bp**, exactly (6.0 − 5.6) × 0.005 = 0.20%. Had rates *fallen* 50 bp, the tilt would have *cost* 0.20% — the symmetric price of being wrong. Relative return vs benchmark = (benchmark duration − portfolio duration) × Δy.

**B8. Duration-neutral steepener sizing.** You want a 2s10s steepener: long the 2y (mod dur 1.9), short the 10y (mod dur 8.2), and you commit 50 mn face to the 2y leg. What 10y face makes the trade duration-neutral, and what remains as the exposure?

*Solution.* Duration-neutral means equal dollar duration on each leg. Taking price ≈ par for both, dollar duration ∝ face × duration. Set 50 × 1.9 = F₁₀ × 8.2 → F₁₀ = 95 / 8.2 = **11.59 mn** face short in the 10y. The trade is (approximately) immune to a parallel level shift and is exposed only to a change in the **2s10s slope** — it profits if the curve steepens (2y yield falls relative to 10y). (In practice you match dollar durations using actual prices, not the par approximation.)

**B9. Spread duration / carry.** A corporate bond has spread duration 4.5 and trades at a 150 bp spread over Treasuries. (a) Price impact if the spread tightens 30 bp. (b) One-line statement of the carry argument.

*Solution.* (a) ΔP/P ≈ −D_spread × Δs = −4.5 × (−0.0030) = **+1.35%**. (b) Even if the spread is unchanged, you out-yield Treasuries by the 150 bp spread (the carry) — valid only until a default or spread blow-out; the credit overweight is simultaneously earning carry and betting on tightening (Δs < 0).

---

## Section C — Interview-Style

**C1. "A trustee says passive bond management is just being lazy — you're doing nothing. How do you respond?"**

*Model answer.* Passive means *non-predictive*, not inactive. Immunisation and cash-flow matching are precise engineering: you solve for exact face amounts so PVs and durations match a liability, and immunisation requires *ongoing rebalancing* as duration drifts with time and yields. Indexing requires stratified sampling to match a benchmark's key-rate and sector profile within a tight tracking-error budget. The choice to be passive is a considered judgement that we have no reliable edge over deeply liquid, competitively priced markets — after costs, the median active government-bond manager struggles to beat the index — or that the mandate doesn't reward betting. That is discipline, not laziness.

**C2. "Walk me through why you'd choose cash-flow matching over immunisation for a pension book — and when you wouldn't."**

*Model answer.* Cash-flow matching *eliminates* rate risk by dating the assets' cash flows to the liabilities, so it needs no interest-rate assumption, no rebalancing, and no parallel-shift hope — the highest certainty available. Immunisation only *offsets* risk via the duration crossover; it protects only small parallel shifts, breaks on twists, and must be rebalanced. So for a mandate that prizes certainty above all, cash-flow match. The cost is yield: a perfectly matching, usually non-callable bond set is expensive and constraining, so it typically has the lowest yield. When the yield give-up is unacceptable or the far-dated liabilities are hard to match precisely, I'd use **horizon matching** — cash-flow match the near term (where reinvestment and liquidity risk bite) and immunise the long tail (where shifts are more parallel and matching is expensive).

**C3. "Is a barbell a free lunch because it has more convexity than a bullet?"**

*Model answer.* No. For equal duration, the more convex barbell does outperform on *large* moves and on steepeners — convexity is a positive-gamma benefit. But the market *charges* for that convexity via a lower yield, so on a *stable* curve the lower-convexity bullet earns more carry and wins. Convexity is bought, not free. The right structure depends on your view: barbell if you expect large moves or a steepening; bullet if you expect a calm curve or a flattening that benefits the belly.

**C4. "You put on a ride-the-curve trade and made 7% while the benchmark made 3%. Was that skill?"**

*Model answer.* Partly — but I'd be honest that most of the excess was *risk compensation*, not alpha. Riding the curve is an active bet that the curve stays put. The 7% decomposed into ~5% carry at the purchase yield plus ~2% rolldown from the bond aging to a lower yield on a static curve. Had the curve shifted up meaningfully, the rolldown would have shrunk or reversed — a large enough rise erases the entire edge. So the trade needs an upward-sloping curve to exist at all and a stable-to-falling curve to pay off. The excess over hold-to-maturity is pay for the curve-shift risk I accepted; calling it pure skill would misrepresent the risk taken.

**C5. "How do you actually decide passive versus active for a new mandate?"**

*Model answer.* Read the mandate and the view together. The mandate: liability-driven money (pension, insurer) → immunise, cash-flow match, or run LDI; a total-return fund benchmarked to an index → index or enhanced-index with controlled tilts; an explicit active remit → active tilts sized to a tracking-error budget. The view: active deviation is only justified by a nameable forecast that diverges from market-implied pricing. So the mandate sets the objective and constraints; the view justifies any deviation from passive. No view *or* no freedom → stay passive. Cardinal rule: every active basis point of expected excess return must correspond to a divergence you can name — if you can't name it, you don't have a trade, you have tracking error.

---

## Section D — Multiple Choice (with reasoning)

**D1.** To immunise a single 10-year liability with coupon bonds, you should hold bonds whose:

A. maturity = 10 years
B. Macaulay duration = 10 years
C. yield = the liability discount rate
D. convexity is maximised

**Answer: B.** You match *duration* to the horizon, not maturity — a 10-year coupon bond has duration well below 10, so it under-hedges. A is the classic "duration = maturity" trap. C is irrelevant to the offset mechanism. D is wrong: among duration-matched options you want convexity/dispersion *close to the liability's*, not maximal, to avoid non-parallel-shift risk.

**D2.** Cash-flow matching differs from immunisation primarily because it:

A. requires periodic rebalancing
B. assumes only parallel yield shifts
C. eliminates rate risk rather than offsetting it, needing no rate assumption
D. always earns a higher yield

**Answer: C.** Cash-flow matching dates assets to liabilities so risk is eliminated by construction — no rate assumption, no rebalancing. A and B describe *immunisation*, not cash-flow matching. D is backwards: cash-flow matching usually has the *lowest* yield, the price of its certainty.

**D3.** An immunised (duration-matched) coupon portfolio is most vulnerable to:

A. a small parallel upward shift
B. a small parallel downward shift
C. a non-parallel twist of the curve
D. the passage of time with no rate change

**Answer: C.** Duration matching protects only *small parallel* shifts to first order. Two portfolios with equal duration can have very different key-rate profiles, so a twist can break the hedge — hence key-rate-duration and convexity matching. A and B are exactly what immunisation is built to handle. D causes duration *drift* (handled by rebalancing) but is not the primary vulnerability.

**D4.** Riding the curve generates excess return over hold-to-maturity only when the curve is:

A. inverted and steepening
B. flat and stable
C. upward-sloping and stable (or falling)
D. upward-sloping and rising sharply

**Answer: C.** Rolldown requires an upward-sloping curve (so the bond's yield falls as it ages down the curve) that stays put or falls (so the shift doesn't offset the rolldown). A inverted curve gives negative rolldown; a flat curve gives none; a sharply rising curve erases the edge.

**D5.** A manager expecting rates to fall by *more* than the forward curve implies should:

A. shorten duration below the benchmark
B. extend duration above the benchmark
C. hold duration equal and buy a bullet
D. move down in credit quality

**Answer: B.** Bullish on price = extend duration to maximise the price gain when rates fall. A is the opposite (a rising-rate view). C is a *curve-shape* view, not a level view. D is a *spread* bet, unrelated to the rate-level forecast.

**D6.** In a duration-neutral 2s10s steepener, the two legs are sized to have equal:

A. face value
B. market value
C. dollar (money) duration
D. yield to maturity

**Answer: C.** Sizing the legs to equal dollar duration makes the trade approximately immune to a parallel *level* shift, leaving only *slope* exposure. Equal face or market value would leave a residual duration mismatch and hence unwanted level exposure.

**D7.** "Enhanced indexing" is best described as:

A. full replication of every index constituent
B. a benchmark match with small, controlled tilts within a tight tracking-error budget
C. maximum-conviction duration betting
D. cash-flow matching a liability stream

**Answer: B.** Enhanced indexing permits a few bp of duration or minor sector tilts to add modest excess return while keeping tracking error tight. A is (usually infeasible) pure indexing. C is aggressive active management. D is a liability-driven passive strategy, not benchmark-relative.

**D8.** Spread duration of 4.5 means a 25 bp *widening* in credit spread causes an approximate price change of:

A. +1.125%
B. −1.125%
C. −0.5625%
D. +0.5625%

**Answer: B.** ΔP/P ≈ −D_spread × Δs = −4.5 × (+0.0025) = **−1.125%**. Widening (Δs > 0) hurts price. A has the wrong sign; C and D use the wrong magnitude.

---

*Self-check note:* All numerical answers reconcile with the chapter's worked examples — B1–B2 (immunisation offset), B3–B5 (rolldown 4.99% + 2.03% = 7.03%; shift-up return 5.00%), B6–B7 (weight 0.5143, 20 bp relative saving), and the first-order duration/spread-duration price formulas in B7–B9 and D8.
