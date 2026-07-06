# Q&A — Duration

A practice bank for Chapter 07. Every question is followed by a full answer; work each before reading the answer. Conventions: face value is 100 unless a position size is stated, "bp" is a basis point (0.01%), $y$ is the annual yield and $m$ the coupon periods per year. Compute Macaulay/modified duration in the bond's native period, then divide by $m$ to state it in years and per annual-yield move.

---

## Section A — Concept Checks

**A1. In one sentence, what does duration measure, and why does the desk care?**

Duration compresses the whole price–yield relationship into one number — the approximate percentage change in a bond's price for a 1-unit change in yield — so a risk manager can answer "if yields move X, how much do I make or lose?" for a 400-line book without repricing everything.

**A2. State the two "faces" of duration and the bridge between them.**

Face 1 is *time*: Macaulay duration is the present-value-weighted average time until you receive the cash flows (in years), the balance point of the cash-flow timeline. Face 2 is *sensitivity*: modified duration is the percentage price change per unit yield. The bridge is division by one plus the periodic yield: $D_{Mod} = D_{Mac}/(1+y/m)$. They fall out of the same derivative of the pricing equation.

**A3. Why is duration strictly less than maturity for a coupon bond, but equal to maturity for a zero?**

Coupons return money along the way, so some of the bond's present value arrives *before* maturity, pulling the weighted-average time (the fulcrum) in from the final date. A zero pays everything at one instant — maturity — so its balance point *is* the maturity date and $D_{Mac} = N$.

**A4. Which way does a higher coupon push duration, and why is the intuition often reversed by beginners?**

A higher coupon *lowers* duration. More present value arrives early, pulling the balance point in, which *reduces* rate sensitivity. Beginners think "more coupon = more cash flow = more risk," but the opposite is true: low-coupon and zero-coupon bonds are the *most* rate-sensitive at a given maturity.

**A5. Which way does a higher yield push duration?**

A higher yield *lowers* duration. Distant cash flows are discounted harder, so they carry less present-value weight, shifting the weighted-average time toward the earlier flows.

**A6. When must you abandon modified duration for effective duration?**

Whenever cash flows change with the yield path — callables, putables, MBS, any embedded option. The analytic derivative behind modified duration assumes fixed $CF_t$; once cash flows move with rates that assumption breaks, so you shock the curve up and down and reprice with a model: $D_{Eff} = (P_- - P_+)/(2 P_0 \Delta y)$.

**A7. Define money (dollar) duration and PV01, and say why traders prefer PV01.**

Money duration $= D_{Mod} \times P$ — the currency price change per unit yield. PV01 (a.k.a. DV01, PVBP) $= D_{Mod} \times P \times 0.0001$ — the currency change per 1 bp. Traders prefer PV01 because it is *additive* across long and short positions, so a book's total risk is just the sum of position PV01s, and hedging reduces to matching equal-and-opposite PV01.

**A8. How do you compute a portfolio's duration, and what is the classic weighting mistake?**

Weight each bond's modified duration by its *market value*: $D_P = \sum w_i D_i$, $w_i = MV_i/\sum MV_j$. Equivalently, sum the PV01s. The mistake is weighting by *face value* or by count, which is wrong whenever bonds trade away from par.

**A9. Duration is a "local" measure. What does that mean, and what corrects it?**

Duration is the tangent line to the convex price–yield curve at the current yield. For small yield moves the tangent hugs the curve and the estimate is excellent; for large moves the curve bends away from the straight line, so duration alone overstates losses on sell-offs and understates gains on rallies. **Convexity** — the second-order term — mops up the residual.

**A10. What is the duration of a perpetuity, and why is it finite despite infinite maturity?**

$D_{Mac} = (1+y)/y$. At 8% that is 13.5 years. Even though the bond never matures, cash flows far in the future are discounted so heavily that they contribute almost nothing to the PV-weighted average, capping the balance point at a finite value.

**A11. Can effective duration be negative? Give the mechanism.**

Yes, for negatively convex instruments like deep-in-the-money MBS. When rates fall, prepayments accelerate, shortening the bond and capping price appreciation so sharply that price can actually *fall* as rates fall — a negative $D_{Eff}$.

**A12. What is the duration gap, and what does a positive gap imply for a bank?**

Duration gap = asset duration − (equity-weighted) liability duration. A positive gap means assets are more rate-sensitive than liabilities, so a rate *rise* cuts asset value more than liability value and the institution loses net worth. Immunization sets the gap to zero.

---

## Section B — Numerical Problems (full step-by-step)

**B1. A 5-year zero-coupon bond yields 6% annually. Find its Macaulay and modified duration, then verify the sensitivity against an actual +100 bp reprice.**

Price $= 100/1.06^5 = 100/1.3382256 = 74.72582$.
A zero has a single cash flow at year 5, so $D_{Mac} = 5.00000$ years.
$D_{Mod} = 5/1.06 = 4.71698$ — i.e. ~4.717% per 100 bp.

*Verify.* Reprice at 7%: $100/1.07^5 = 100/1.4025517 = 71.29862$.
Actual change $= (71.29862 - 74.72582)/74.72582 = -4.5860\%$.
Duration estimate $= -4.71698 \times 0.01 = -4.7170\%$.
The estimate overstates the loss by 0.131% — that residual is convexity (the curve lies above the tangent). Reconciles: duration is a local first-order estimate.

**B2. A 4-year, 5% annual-coupon bond is priced to yield 5% (a par bond). Build out the duration and reconcile with a +100 bp reprice.**

Cash flows: 5, 5, 5, 105. Discount at 5%.

| $t$ | $CF_t$ | $PV_t = CF_t/1.05^t$ | $t\cdot PV_t$ |
|---:|---:|---:|---:|
| 1 | 5 | 4.761905 | 4.761905 |
| 2 | 5 | 4.535147 | 9.070295 |
| 3 | 5 | 4.319188 | 12.957563 |
| 4 | 105 | 86.383761 | 345.535043 |
| **Sum** | | **100.000001** | **372.324806** |

Price $= 100.0000$ (confirms par). 
$D_{Mac} = 372.324806/100 = 3.72325$ years. 
$D_{Mod} = 3.72325/1.05 = 3.54595$ — ~3.546% per 100 bp.

*Verify.* Reprice at 6%: $5/1.06 + 5/1.06^2 + 5/1.06^3 + 105/1.06^4 = 4.716981 + 4.450695 + 4.198769 + 83.169860 = 96.536305$.
Actual change $= (96.536305 - 100)/100 = -3.4637\%$.
Duration estimate $= -3.54595\%$. Overstatement of 0.082% is convexity. Reconciles.

**B3. A 3-year, 6% coupon bond pays semiannually and yields 8% annually. Find duration in years and reconcile with a +100 bp reprice. (Watch the periodicity.)**

Work in half-years: $N = 6$, coupon $= 3$, periodic yield $= 4\%$.

| $t$ (½-yr) | $CF_t$ | $PV_t = CF_t/1.04^t$ | $t\cdot PV_t$ |
|---:|---:|---:|---:|
| 1 | 3 | 2.884615 | 2.884615 |
| 2 | 3 | 2.773669 | 5.547337 |
| 3 | 3 | 2.667008 | 8.001024 |
| 4 | 3 | 2.564449 | 10.257796 |
| 5 | 3 | 2.465817 | 12.329085 |
| 6 | 103 | 81.402440 | 488.414640 |
| **Sum** | | **94.757998** | **527.434497** |

Price $= 94.7580$. 
$D_{Mac}$ in periods $= 527.434497/94.757998 = 5.56610$ half-years; divide by $m = 2$: **$D_{Mac} = 2.78305$ years**. 
$D_{Mod}$ in periods $= 5.56610/1.04 = 5.35202$; divide by 2: **$D_{Mod} = 2.67601$** (per 100 bp annual-yield move).

*Verify.* Reprice at 9% annual (4.5% per period): $3/1.045 + 3/1.045^2 + \dots + 103/1.045^6 = 2.870813 + 2.747189 + 2.628880 + 2.515894 + 2.407512 + 79.093830 = 92.264118$.
Actual change $= (92.264118 - 94.757998)/94.757998 = -2.6319\%$.
Duration estimate $= -2.67601\%$. Overstatement of 0.044% is convexity. Reconciles. **Lesson: always compute in the native period, then divide by $m$.**

**B4. You hold 20,000,000 face of the B2 par bond ($D_{Mod} = 3.54595$, price 100). Compute money duration, position PV01, and the expected P&L on a +40 bp sell-off.**

Market value $= 20{,}000{,}000 \times (100/100) = \$20{,}000{,}000$.
Money duration per 100 $= 3.54595 \times 100 = 354.595$.
PV01 per 100 $= 354.595 \times 0.0001 = 0.0354595$.
Scale to 20mm face (factor $20{,}000{,}000/100 = 200{,}000$): **PV01 $= 0.0354595 \times 200{,}000 = \$7{,}091.90$ per 1 bp**.
On a +40 bp move, expected loss $\approx 40 \times \$7{,}091.90 = \$283{,}676$.
*Cross-check via money duration:* $-D_{Mod} \times MV \times \Delta y = -3.54595 \times 20{,}000{,}000 \times 0.004 = -\$283{,}676$. ✓ Two routes agree.

**B5. A book holds Bond X (MV $12mm, $D_{Mod}=3.546$) and Bond Y (MV $8mm, $D_{Mod}=6.5$). Find portfolio duration and PV01, then size a hedge to cut duration to 3.0 using 10-yr futures with DV01 $75/contract.**

Weights: $w_X = 12/20 = 0.60$, $w_Y = 8/20 = 0.40$.
$D_P = 0.60 \times 3.546 + 0.40 \times 6.5 = 2.1276 + 2.6000 = 4.7276$.
PV01: $\text{X} = 3.546 \times 12{,}000{,}000 \times 0.0001 = \$4{,}255.20$; $\text{Y} = 6.5 \times 8{,}000{,}000 \times 0.0001 = \$5{,}200.00$; **portfolio PV01 $= \$9{,}455.20$**.
*Cross-check:* $4.7276 \times 20{,}000{,}000 \times 0.0001 = \$9{,}455.20$. ✓

*Hedge.* Required PV01 reduction $= (4.7276 - 3.0) \times 20{,}000{,}000 \times 0.0001 = 1.7276 \times 2{,}000 = \$3{,}455.20$.
Contracts to short $= 3{,}455.20/75 = 46.07 \approx \textbf{46 contracts short}$. This converts a duration target into an executable trade.

**B6. A callable bond is priced at $P_0 = 98$. A model reprices it after a ±30 bp curve shift: $P_- = 99.50$ (down), $P_+ = 96.30$ (up). Compute effective duration and compare with an option-free modified duration of 6.8.**

$$D_{Eff} = \frac{P_- - P_+}{2 P_0 \Delta y} = \frac{99.50 - 96.30}{2 \times 98 \times 0.0030} = \frac{3.20}{0.588} = 5.442$$

The embedded call shortens effective duration to **5.44** versus the 6.8 of an otherwise-identical straight bond: the bond can't rally freely when rates fall (the call caps upside), so it responds asymmetrically. That asymmetry — a bigger drop on the sell-off than the gain on the rally — is the negative-convexity fingerprint that modified duration misses.

**B7. Two 10-year annual bonds yield 7%: Bond A pays a 4% coupon, Bond B pays 10%. Use the closed form to show which has the higher duration.**

Closed form: $D_{Mac} = \dfrac{1+y}{y} - \dfrac{(1+y)+N(c-y)}{c[(1+y)^N - 1]+y}$, with $y=0.07$, $N=10$, $(1.07)^{10}=1.967151$, $(1+y)/y = 15.285714$.

*Bond A ($c=0.04$):* second term numerator $= 1.07 + 10(0.04-0.07) = 0.77$; denominator $= 0.04(0.967151)+0.07 = 0.108686$; ratio $= 7.08461$. $D_{Mac} = 15.285714 - 7.08461 = \textbf{8.2011 years}$.

*Bond B ($c=0.10$):* numerator $= 1.07 + 10(0.10-0.07) = 1.37$; denominator $= 0.10(0.967151)+0.07 = 0.166715$; ratio $= 8.21742$. $D_{Mac} = 15.285714 - 8.21742 = \textbf{7.0683 years}$.

The lower-coupon Bond A has the higher duration (8.20 vs 7.07), confirming the rule: **higher coupon → lower duration**, because more PV arrives early.

---

## Section C — Interview-Style (model answers)

**C1. "Explain duration to me like I'm a new analyst who only knows how to price a bond."**

You already know price is the sum of discounted cash flows. Duration is what you get when you ask how that price *moves* when the yield moves — it is literally the first derivative of the pricing equation, scaled by price. Two useful readings fall out of the same math: it's the PV-weighted average time to get your money back (in years), and it's the percentage price change per 1% yield move. So a duration of 6 means roughly a 6% price drop if yields rise 100 bp. It's the single most important risk number in fixed income because it's *additive* — a whole portfolio collapses to one figure and one hedge.

**C2. "A PM says 'just use modified duration on this MBS.' What do you push back with?"**

I'd stop them. Modified duration assumes the cash flows are fixed, because it's the analytic derivative of a fixed-cash-flow pricing formula. An MBS has cash flows that move with rates — when rates fall, homeowners prepay, so the bond shortens exactly when you'd want it to extend. Modified duration can't see that; it can materially misstate or even mis-sign the risk. The correct tool is effective duration: shock the curve up and down, reprice with a prepayment model, and take $(P_- - P_+)/(2P_0\Delta y)$. For deep-in-the-money pools you can even get negative effective duration.

**C3. "You have a $500mm book. Walk me through how you'd hedge its rate risk overnight."**

I'd reduce the book to a single PV01 by summing every position's PV01 — valid because PV01 is additive across longs and shorts. Say the book's PV01 is $180,000 per bp. I pick a liquid instrument — 10-year Treasury futures or a receive-fixed swap — compute its DV01, and short enough to offset $180,000. If the future's DV01 is $75/contract, I short 180,000/75 = 2,400 contracts. I'd also check key-rate durations so I'm not flattening a parallel shift while leaving a curve-steepening exposure open.

**C4. "Why does duration overstate the loss on a big sell-off? Is that conservative or dangerous?"**

Because the price–yield curve is convex — bowed toward the origin — while duration is a straight tangent line. On a large sell-off the true price sits *above* the tangent, so the linear estimate predicts a bigger loss than actually occurs; on a rally the true price sits above the tangent too, so duration *understates* the gain. For a long-only holder that's conservative — reality is kinder than the estimate in both directions. It becomes dangerous when you're short convexity (short options, some MBS), where the curvature works against you and you need the convexity term to see the true risk.

**C5. "Rank a 10-year zero, a 10-year 4% bond, and a 10-year 10% bond by duration, and explain."**

Highest to lowest: the zero, then the 4%, then the 10%. The zero pays everything at maturity so its duration equals its 10-year maturity — the maximum for that maturity. Adding coupons pulls the balance point in, and the bigger the coupon the more PV arrives early, so the 4% bond has a longer duration than the 10% bond. Same maturity, opposite rate sensitivity, driven entirely by how early the money comes back.

**C6. "What are the limitations of duration, and how do you address each?"**

Three main ones. First, it's *linear/local* — fine for small moves, off for large ones; I add convexity for anything beyond ~25 bp. Second, it assumes a *parallel* shift of a single yield; real curves twist, so I use key-rate durations to hedge reshaping. Third, it assumes *fixed cash flows*; for embedded options I switch to effective duration. Duration is the right first number, but never the only number.

---

## Section D — Multiple Choice (with reasoning)

**D1. A bond's modified duration is 7.0. Yields rise 50 bp. The approximate price change is:**

A. −7.0% B. −3.5% C. +3.5% D. −0.35%

**Answer: B.** $\Delta P/P \approx -D_{Mod}\,\Delta y = -7.0 \times 0.005 = -0.035 = -3.5\%$. A applies a full 100 bp; C flips the sign; D is off by a factor of ten.

**D2. Which bond has the highest duration, all else equal?**

A. 10-yr, 8% coupon B. 10-yr, 4% coupon C. 10-yr zero-coupon D. 5-yr zero-coupon

**Answer: C.** For a given maturity the zero has the maximum duration (duration = maturity = 10), and lower coupons raise duration, so C > B > A. D is a zero but only 5-year, so its duration is 5. Longer maturity plus zero coupon wins.

**D3. To convert Macaulay duration to modified duration you:**

A. multiply by (1 + y/m) B. divide by (1 + y/m) C. multiply by price D. divide by price

**Answer: B.** $D_{Mod} = D_{Mac}/(1+y/m)$, using the periodic yield. A inverts the operation; C and D confuse the step with computing money duration.

**D4. Effective duration should be used instead of modified duration when:**

A. the bond pays semiannually B. yields are very high C. the bond has embedded options or path-dependent cash flows D. the portfolio is large

**Answer: C.** Modified duration assumes fixed cash flows; once cash flows change with the yield path (callables, putables, MBS) you must shock-and-reprice. A is handled by the periodicity convention; B and D don't invalidate the analytic derivative.

**D5. A trader says "my position's PV01 is $2,400." This means:**

A. the position loses $2,400 if it defaults B. the position value changes ~$2,400 per 1 bp yield move C. the position yields 2,400 bp D. the coupon is $2,400

**Answer: B.** PV01 (DV01/PVBP) is the currency change in value for a 1 bp yield move — the additive unit desks hedge in. The others confuse it with default loss, yield, or coupon.

**D6. Duration overstates the loss on a large yield increase because:**

A. the price–yield curve is concave B. the price–yield curve is convex, so the true price lies above the tangent C. convexity is negative D. the yield used is wrong

**Answer: B.** The convex curve lies above its tangent, so the true price is higher (loss smaller) than the linear estimate predicts. A misstates the curvature; C is false for option-free bonds (convexity is positive); D is irrelevant.

**D7. A portfolio holds $6mm at duration 2.5 and $4mm at duration 7.0. Its modified duration is:**

A. 4.75 B. 4.30 C. 9.50 D. 3.50

**Answer: B.** Market-value weighting: $0.6 \times 2.5 + 0.4 \times 7.0 = 1.5 + 2.8 = 4.30$. A is a simple (equal-weight) average; C sums the durations; D is wrong entirely.

**D8. An MBS shows a negative effective duration. The most likely cause is:**

A. a data error — duration can't be negative B. falling rates trigger prepayments that shorten the bond and cap its price C. the coupon exceeds the yield D. the bond is a zero

**Answer: B.** Negative convexity: when rates fall, prepayments accelerate, so price can fall as rates fall, giving negative effective duration. A is wrong — effective duration *can* be negative; C and D are unrelated to the prepayment mechanism.

---

*Self-check: every numerical answer was verified by re-pricing at the shocked yield and confirming the duration estimate reconciles with the true move (residual = convexity) — B1–B3 tie out, the money-duration/PV01 cross-checks in B4–B5 agree by two routes, and B7's closed-form durations confirm the coupon-effect ordering used in D2 and C5.*
