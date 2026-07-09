# Q&A — Interest Rate Risk

A practice bank for Chapter 09. Every question is followed by a full answer; work each before reading the answer. Convention: unless stated otherwise, bonds pay **annual** coupons on a face of 100, yields are annual, and "duration" unqualified means modified duration when used as a sensitivity and Macaulay when used as a time. Every numerical answer is reconciled against an exact reprice or a definitional check.

---

## Section A — Concept Checks

**A1. In one sentence, why does a bond's price move inversely with its yield?**

Price is the present value of a *fixed* cash-flow stream, $P=\sum CF_t/(1+y)^t$, and $y$ sits in every denominator — raise it and every discounted term shrinks, so the price must fall. It is arithmetic, not sentiment.

**A2. Interest rate risk splits into two opposing components. Name them and state which direction of rates hurts each.**

*Price (market) risk* — a capital loss if you sell after yields **rise**. *Reinvestment risk* — lower income when coupons must be reinvested after yields **fall**. A rate rise is bad for price but good for reinvestment; a rate fall is the reverse. They are always opposite-signed.

**A3. At what holding horizon do the two effects cancel, and what is that principle called?**

At a horizon equal to the bond's **Macaulay duration**. There the extra (or lost) reinvestment income exactly offsets the depressed (or elevated) sale price, so a one-time yield shift leaves realised return unchanged to first order. Deliberately setting horizon equal to duration is **immunisation**.

**A4. Give the two equally-correct interpretations of Macaulay duration.**

(1) The **present-value-weighted average time** to receive the bond's cash flows — the centre of mass of the cash-flow timeline. (2) The **break-even holding period** at which price and reinvestment risk offset. Both fall out of the same formula.

**A5. How does modified duration differ from Macaulay duration, in words and in formula?**

Macaulay answers "when, on average, am I paid?"; modified answers "how much does my price move?" They differ only by a discount factor: $D_{Mod}=D_{Mac}/(1+y/k)$, where $k$ is compounding periods per year. Modified duration gives $\Delta P/P \approx -D_{Mod}\,\Delta y$.

**A6. State the three drivers of duration and their direction.**

Duration rises with **maturity**, falls with **coupon rate**, and falls with **yield**. Higher coupons and higher yields both pull the cash-flow centre of mass forward, shortening duration; longer maturity pushes it back.

**A7. What is convexity, and why is it a "friend" for an option-free bond?**

Convexity is the second-order (curvature) term in the Taylor expansion, $\Delta P/P \approx -D_{Mod}\Delta y + \tfrac12 C(\Delta y)^2$. For an option-free bond it is **positive**, so it *adds* value in both directions: duration overstates the loss when rates rise and understates the gain when they fall. You pay for it in lower yield.

**A8. What is DV01 (PVBP) and why do traders hedge with it instead of duration?**

DV01 is the dollar P&L from a **1 bp** yield move on a position: $\text{DV01}=D_{Mod}\times P\times 0.0001$. It already bakes in price level and position size, so matching DV01s between a long and a hedge directly zeros the basis-point P&L — duration alone would ignore price and notional.

**A9. Portfolio duration is what kind of average, and what shift does it assume?**

A **market-value-weighted** average of component durations, $D_P=\sum_i (MV_i/MV_{\text{total}})D_i$. It assumes a **parallel** shift of the whole curve; it says nothing about twists.

**A10. Why do key-rate durations exist if we already have portfolio duration?**

Because real curves twist rather than shift in parallel. A key-rate duration measures sensitivity to a 1 bp move at **one** maturity with the rest held fixed. They **sum to the total effective duration** ($\sum_i KRD_i = D_{\text{eff}}$) but reveal *where* on the curve the risk lives — so two portfolios with identical total duration can behave oppositely under a steepener.

**A11. When must you use effective (rather than analytic) duration, and what odd property can appear?**

When the cash flows themselves depend on rates — callables, putables, MBS. You reprice up and down under a small parallel shift and take the numerical derivative. Near the call, a callable can show **negative convexity**: as rates fall the call caps the upside and the price-yield curve bends the wrong way.

**A12. State the three conditions for immunising a single liability.**

(1) Match present values: $P_{\text{assets}}=PV(L)$. (2) Match duration to horizon: $D_{\text{assets}}=H$. (3) Set asset **convexity ≥ liability convexity** (dispersion) so the position survives non-parallel shifts. Rebalance as time and yields drift the duration out of step.

---

## Section B — Numerical Bond-Math Problems

**B1. A 4-year, 5% annual-coupon bond is priced at par (100) to yield 5%. Compute Macaulay duration, modified duration, and convexity, then predict the price if the yield rises 100 bp to 6% — with and without convexity — and reconcile against an exact reprice.**

*Step 1 — Price and the weighting table.* Cash flows are 5, 5, 5, 105; discount at 5%.

| t | CF | DF = 1/1.05^t | PV | t·PV | t(t+1)·CF/1.05^(t+2) |
|---|----|--------------|-----|------|----------------------|
| 1 | 5 | 0.952381 | 4.76190 | 4.76190 | 8.63838 |
| 2 | 5 | 0.907029 | 4.53515 | 9.07029 | 24.68107 |
| 3 | 5 | 0.863838 | 4.31919 | 12.95756 | 47.01157 |
| 4 | 105 | 0.822702 | 86.38376 | 345.53504 | 1567.05389 |
| **Σ** | | | **100.00000** | **372.32480** | **1647.38491** |

Price = 100.000 (par, as expected since coupon = yield). ✓

*Step 2 — Macaulay duration.* $D_{Mac}=372.32480/100=3.72325$ years. Below the 4-year maturity because coupons pull the centre of mass forward — correct for a coupon bond.

*Step 3 — Modified duration.* $D_{Mod}=3.72325/1.05=3.54595$.

*Step 4 — Convexity.* $C=1647.38491/100=16.4738$.

*Step 5 — Predict at 6%.*
Duration only: $\Delta P/P \approx -3.54595\times0.01=-0.0354595 \Rightarrow P\approx 96.4540$.
Add convexity: $\tfrac12\times16.4738\times(0.01)^2=+0.000824 \Rightarrow P\approx 96.4540+0.0824=96.5364$.

*Step 6 — Reconcile with exact reprice at 6%.*
$$P_{6\%}=\frac{5}{1.06}+\frac{5}{1.06^2}+\frac{5}{1.06^3}+\frac{105}{1.06^4}=4.71698+4.45070+4.19877+83.16844=96.5349$$

| Method | Predicted | Error vs exact |
|---|---|---|
| Duration only | 96.4540 | −0.0808 |
| Duration + convexity | 96.5364 | +0.0015 |
| Exact reprice | 96.5349 | — |

The convexity term cut the error from about 8 cents to under 0.2 cents, and the duration-only estimate sits *below* the true price — confirming positive convexity makes the straight-line estimate too pessimistic on a sell-off. **Reconciled.**

**B2. You are long 5,000,000 face of Bond X (price 95.00, $D_{Mod}=6.0$). Hedge the rate risk with Bond Y (price 102.00, $D_{Mod}=3.5$). How much face of Y do you short?**

*Step 1 — DV01 per 100 face.*
$$\text{DV01}_X=6.0\times95.00\times0.0001=0.05700, \qquad \text{DV01}_Y=3.5\times102.00\times0.0001=0.03570$$

*Step 2 — DV01 of the X position* (5,000,000 face = 50,000 units of 100):
$$\text{DV01}_X^{\text{pos}}=50{,}000\times0.05700=2{,}850.00 \text{ per bp}$$

*Step 3 — Face of Y needed.*
$$\text{Face}_Y=5{,}000{,}000\times\frac{0.05700}{0.03570}=5{,}000{,}000\times1.596639=7{,}983{,}193 \approx \textbf{7,983,200 face}$$

*Step 4 — Check.* $\text{DV01}_Y^{\text{pos}}=79{,}832\times0.03570=2{,}850.0$ per bp — equal and opposite to X, net DV01 ≈ 0. **Reconciled.** You need *more* face of Y because it is the less rate-sensitive (shorter-duration) bond; it takes more of it to generate the same basis-point P&L.

**B3. A 5-year zero-coupon bond yields 5% annually. State its Macaulay and modified duration, and separately compute effective duration and convexity for a bond that reprices to 103.20 when yields fall 50 bp and to 96.90 when yields rise 50 bp from a base price of 100.**

*Zero-coupon durations.* A zero has a single cash flow at maturity, so its Macaulay duration equals its maturity exactly: $D_{Mac}=5.00$ years. Modified: $D_{Mod}=5.00/1.05=4.7619$. (A zero also carries no reinvestment risk — nothing to reinvest.)

*Effective duration and convexity* with $P_-=103.20$, $P_+=96.90$, $P_0=100$, $\Delta y=0.005$:
$$D_{\text{eff}}=\frac{P_--P_+}{2P_0\,\Delta y}=\frac{103.20-96.90}{2\times100\times0.005}=\frac{6.30}{1.00}=6.30$$
$$C_{\text{eff}}=\frac{P_-+P_+-2P_0}{P_0(\Delta y)^2}=\frac{103.20+96.90-200}{100\times(0.005)^2}=\frac{0.10}{0.0025}=40.0$$

The up and down moves are not symmetric (6.30 vs 3.10 in raw price terms) — that asymmetry *is* the convexity, and its positive sign (0.10 > 0) confirms the bond gains slightly more than duration predicts on the rally and loses slightly less on the sell-off. **Reconciled** against the definition.

**B4. You owe 2,000,000 in exactly 7 years. The curve is flat at 5%. You immunise with two bonds of Macaulay duration 4 and 9 years. What present value do you invest, and what weights hit the target duration?**

*Step 1 — PV of the liability.*
$$PV=\frac{2{,}000{,}000}{1.05^{7}}=\frac{2{,}000{,}000}{1.407100}=1{,}421{,}363$$

*Step 2 — Duration-matching weights.* Solve $w\cdot 9+(1-w)\cdot 4=7$:
$$5w=3 \Rightarrow w=0.60$$
Put **60%** (852,818) in the 9-year-duration bond and **40%** (568,545) in the 4-year-duration bond. Portfolio Macaulay duration = $0.6(9)+0.4(4)=7.0$ = the horizon, with PV = 1,421,363 = PV of the liability. Both immunisation conditions met; because the blended assets have cash flows dispersed around year 7 (positive convexity vs the point liability), a parallel shift leaves you at worst break-even. **Reconciled** — rebalance as duration drifts.

**B5. A portfolio holds three bonds: A (market value 40, $D_{Mod}=2.0$), B (MV 35, $D_{Mod}=6.0$), C (MV 25, $D_{Mod}=12.0$). Compute portfolio duration and the value change for a 100 bp parallel rise.**

$$D_P=\frac{40(2.0)+35(6.0)+25(12.0)}{100}=\frac{80+210+300}{100}=\frac{590}{100}=5.90$$

A 100 bp rise gives $\Delta P/P\approx -5.90\times0.01=-5.90\%$, so the 100 of market value falls to about **94.10** (a loss of 5.90). Note this is a *market-value-weighted* average — the long C bond, though only 25% of value, contributes $300/590=51\%$ of the duration. **Reconciled** against the weighted-average definition.

**B6. Two portfolios each have modified duration 6.0 but convexities of 50 (bullet) and 120 (barbell). Compare their predicted returns under a large ±200 bp parallel move, and explain the pattern.**

Using $\Delta P/P \approx -D_{Mod}\Delta y+\tfrac12 C(\Delta y)^2$ with $\Delta y=\pm0.02$:

| Move | Bullet (C = 50) | Barbell (C = 120) |
|---|---|---|
| +200 bp | $-6(0.02)+\tfrac12(50)(0.0004)=-0.12+0.01=\mathbf{-11.0\%}$ | $-0.12+\tfrac12(120)(0.0004)=-0.12+0.024=\mathbf{-9.6\%}$ |
| −200 bp | $+0.12+0.01=\mathbf{+13.0\%}$ | $+0.12+0.024=\mathbf{+14.4\%}$ |

Same duration, but the high-convexity barbell **loses less on the sell-off and gains more on the rally** — a 1.4-point convexity advantage in each direction. That asymmetry is why an investor pays (accepts lower yield) for convexity, and why it matters most for large or volatile moves. **Reconciled**: for a small move (say 10 bp) the convexity term is only $\tfrac12(120)(0.0001)^2 \approx 0.0006\%$ and the two are indistinguishable — convexity is a large-move phenomenon.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Explain duration to me as if I've never seen the formula."**

Model answer: Duration is two things at once. Physically, it's the average time you wait to get your money back, weighting each cash flow by its present value — the centre of gravity of the payments. As a risk number, it's the percentage your price moves for a 1% change in yield: a duration of 6 means a 100 bp rise costs you about 6% of price, before the convexity kicker. The two meanings coincide because both come from differentiating the pricing equation. Higher for long, low-coupon bonds; lower for short, high-coupon ones.

**C2. "Why does matching duration to my horizon protect me from interest-rate moves?"**

Model answer: You face two opposite exposures. If rates rise, your sale price falls but your coupons reinvest at higher rates; if rates fall, the reverse. The price effect shrinks as the bond pulls to par with the horizon, while the reinvestment effect grows with the horizon — so they cross at exactly one point, and that point is the Macaulay duration. Hold to that horizon and a small one-time yield change leaves your realised return unchanged: the loss on one leg is made up by the gain on the other. That crossover is the whole basis of immunisation — set duration equal to when you need the money.

**C3. "Duration says my two portfolios are identical, but I don't trust it. What am I missing?"**

Model answer: Duration assumes the curve moves in parallel, which it rarely does. Two portfolios with the same total duration can have completely different key-rate profiles — a bullet concentrates its risk at one maturity, a barbell spreads it to the 2-year and 30-year wings. Under a steepener the barbell's long-end exposure gets punished while the bullet barely moves, even though a single duration number called them equal. I'd pull the key-rate durations, which sum to the total duration but show me *where* on the curve the risk sits, and stress each portfolio under a steepener and flattener, not just a parallel shift.

**C4. "Is convexity always good? Sell me on it, then tell me when it isn't."**

Model answer: For an option-free bond convexity is pure upside — it's asymmetry in my favour: I lose less than duration predicts on a sell-off and gain more on a rally, so I'll pay a little yield to own more of it, which is why barbells trade richer than duration-matched bullets. But it isn't free and it isn't always positive. Callables and mortgage-backed securities have *negative* convexity near the money: as rates fall the call or prepayment caps my upside, so the price-yield curve bends the wrong way and duration will mis-hedge me. There I have to use effective duration and convexity computed from a model that reprices the embedded option.

**C5. "How would you hedge the rate risk of a corporate bond position on a desk?"**

Model answer: I'd hedge on **DV01**, not raw duration, because DV01 already folds in the price level and my notional — it's the dollar P&L per basis point. I compute my position's DV01, then short enough of a liquid instrument — a Treasury future, an on-the-run Treasury, or an interest-rate swap — so its DV01 exactly offsets mine, leaving net DV01 near zero. Because the hedge instrument usually has a different duration, the face amounts won't match one-for-one: a shorter-duration hedge needs more notional. And I'd watch the residuals DV01 hedging leaves behind — curve risk (I'd DV01-match by key-rate bucket for a big book) and the credit spread, which a rates hedge doesn't touch.

**C6. "A bank held long-dated bonds funded by deposits and blew up when rates rose. What's the one-line diagnosis?"**

Model answer: A **duration gap** — the assets had far longer duration than the liabilities. When rates rose, the market value of the long assets fell hard while the short-duration deposits barely repriced, so net worth collapsed; formally, the equity's sensitivity is driven by $D_A - D_L\times(L/A)$, and that gap was large and positive. That's the SVB story: economically insolvent on a mark-to-market basis long before any borrower defaulted. The fix is asset-liability management — shorten asset duration or lengthen liability duration (or swap fixed to floating) so the gap closes.

---

## Section D — Multiple-Choice Questions with Reasoning

**D1. A bond has modified duration 8 and convexity 100. For a 100 bp rise in yield, the estimated price change is closest to:**

A. −8.5% B. −8.0% C. −7.5% D. −7.95%

**Answer: D.** $\Delta P/P \approx -8(0.01)+\tfrac12(100)(0.01)^2 = -0.08+0.005 = -0.0795 = -7.95\%$. Answer B (−8.0%) is the duration-only estimate that ignores the +0.5% convexity offset; A and C are distractors. Convexity always makes the true loss smaller than duration alone predicts.

**D2. Which change would *increase* a bond's duration?**

A. a rise in its yield B. an increase in its coupon rate C. a lengthening of its maturity D. adding a call feature

**Answer: C.** Longer maturity pushes the cash-flow centre of mass further out, raising duration. A higher yield (A) and a higher coupon (B) both pull the centre of mass forward, *reducing* duration; a call feature (D) shortens expected life and reduces effective duration.

**D3. Price risk and reinvestment risk:**

A. both hurt the investor when rates rise
B. are opposite-signed and offset at a horizon equal to duration
C. both hurt the investor when rates fall
D. never offset for a coupon bond

**Answer: B.** A rate rise hurts price but helps reinvestment; a fall does the reverse, so they are opposite-signed and cancel at the duration horizon — the immunisation result. A and C wrongly make them same-signed; D denies the offset that defines duration.

**D4. Two portfolios have the same modified duration but different key-rate duration profiles. Under a curve steepener they will:**

A. always move identically, since duration is equal
B. potentially move in opposite directions
C. both gain, because steepeners help all bonds
D. both lose exactly the same amount

**Answer: B.** Total duration only captures parallel shifts; a steepener is a twist, and the portfolio with more long-end key-rate duration suffers while a front-loaded one may gain. That divergence — despite equal total duration — is precisely why desks monitor KRD profiles. A, C, and D all assume the parallel-shift world that a twist violates.

**D5. A callable bond trades near its call price as rates fall. Its convexity is best described as:**

A. positive and rising B. zero C. negative D. undefined

**Answer: C.** As rates fall toward the call, the issuer's option to call caps the price appreciation, so the price-yield curve bends the wrong way — negative convexity. This is why callables need effective (model-based) duration and convexity; A describes an option-free bond, B and D are simply wrong.

**D6. DV01 of a position is best described as:**

A. the percentage price change for a 1% yield move
B. the dollar P&L for a 1 bp yield move
C. the Macaulay duration times price
D. always equal across two bonds with equal duration

**Answer: B.** $\text{DV01}=D_{Mod}\times P\times 0.0001$ — the dollar value of a basis point on the actual position. A describes modified duration (a percentage, per 1%); C omits the $1/(1+y)$ and the 0.0001 scaling and confuses Macaulay with dollar duration; D is false because DV01 depends on price and notional, not duration alone.

**D7. To immunise a single fixed liability, the standard prescription is to:**

A. maximise portfolio yield
B. match asset duration to the liability horizon and PV, with asset convexity ≥ liability convexity
C. buy the longest-duration bond available
D. match the coupon rate to the liability's discount rate

**Answer: B.** Immunisation sets $D_{\text{assets}}=H$ and $P_{\text{assets}}=PV(L)$ so price and reinvestment risk offset, with asset convexity at least the liability's so non-parallel shifts leave you no worse off. A ignores risk entirely; C over-hedges duration and courts huge price risk; D confuses coupon with duration and provides no protection.

---

*Self-check: every numerical answer was reconciled — B1's duration-plus-convexity estimate matched the exact reprice to within 0.2 cents; B2's hedge DV01 (2,850/bp) exactly offset the long; B3's effective-duration inputs satisfied the definition and its positive numerator confirmed positive convexity; B4's weights reproduced duration 7.0 at the correct PV; B5's weighted average summed to 5.90; and B6's ±200 bp asymmetry followed directly from the sign and size of the convexity term.*
