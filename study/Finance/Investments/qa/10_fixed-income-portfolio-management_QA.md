# Q&A — Fixed Income Portfolio Management

> Scope: Investments — Chapter 10 (Fixed Income Portfolio Management). Every question is followed by a full model answer. All rates are annual and in percent unless stated; compounding is annual unless noted. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** numerical (full step-by-step, reconciling) · **C** interview-style with model answers · **D** MCQs with reasoning.

---

## The chapter in one line

$$P=\sum_{t=1}^{N}\frac{C_t}{(1+y)^{t}}\qquad\Rightarrow\qquad \frac{\Delta P}{P}\approx -D_{mod}\,\Delta y+\tfrac12 C(\Delta y)^2$$

**One-line statement:** A bond is a fixed stream of cash flows discounted at a market curve, so price moves inversely with yield; duration measures that first-order sensitivity, convexity corrects it, and the whole discipline is choosing your exposure to the level, slope and curvature of the curve (and to credit spreads) and aligning it with your objective.

---

## Section A — Concept Check

**A1. If a plain bond's cash flows are contractually fixed, what risk is the manager actually paid to manage?**
Three main risks. **Interest-rate risk** — the *fixed* cash flows are the problem: when market yields rise, the present value of those locked-in flows falls, so price drops even with no default (the dominant risk in a high-grade book). **Reinvestment risk** — coupons arrive along the way and must be reinvested at whatever rate then prevails. **Credit risk** — the issuer may default, and the spread that compensates for it moves, inflicting mark-to-market pain before any actual default. Liquidity, call/prepayment and inflation risk sit on top.

**A2. Why do price and yield move inversely — is it an empirical fact or a definition?**
A definition, forced by the maths. Yield $y$ is the discount rate sitting in the denominator of $P=\sum C_t(1+y)^{-t}$. A higher discount rate shrinks every present value, so price falls. It is inverse *by construction*, the first law of fixed income.

**A3. Distinguish Macaulay from modified duration — which is a time and which is a sensitivity?**
Macaulay duration is a **time**: the cash-flow-weighted average number of years to receipt, $D_{Mac}=\sum_t t\,C_t(1+y)^{-t}/P$. Modified duration is a **sensitivity**: $D_{mod}=D_{Mac}/(1+y)$, giving the approximate % price change per 100 bp yield change, $\Delta P/P\approx -D_{mod}\Delta y$. Confusing the two mis-sizes every hedge.

**A4. Why is duration "the" risk number rather than one metric among many?**
Because it is **additive across a portfolio** on a value-weighted basis, so a single number steers the entire rate exposure of a 300-bond book. Want less rate risk before a hike? Cut portfolio duration. It is the master lever.

**A5. Why does a coupon bond always have duration less than its maturity?**
Because the early coupons are cash received *before* maturity, and they pull the weighted-average time to receipt below the final date. Only a **zero-coupon bond** — one single payment at maturity — has duration exactly equal to its maturity.

**A6. What is convexity and why is positive convexity a "gift"?**
Duration is a linear approximation to a curved price–yield relationship. Convexity is the second-order correction, $+\tfrac12 C(\Delta y)^2$. Positive convexity means the bond **gains more when yields fall than it loses when yields rise by the same amount** — a favourable asymmetry. Investors pay for it (accept lower yield), and it matters most for large moves and barbell structures.

**A7. Explain the immunisation insight: how do two opposite risks cancel?**
When yields *rise*, prices fall (bad) but coupons reinvest at higher rates (good); when yields *fall*, prices rise (good) but reinvestment suffers (bad). Price risk and reinvestment risk push in opposite directions. There is a holding horizon where they exactly offset — and that horizon is the **duration**. Set portfolio duration equal to the investment horizon (or the liability's duration) and terminal wealth is locked in to a first approximation.

**A8. Why is bond *indexing* harder than equity indexing?**
A bond index can hold thousands of illiquid issues that trade rarely, so full replication is impractical. Managers use **stratified sampling (cellular matching)**: partition the index into cells by duration, sector, credit quality and coupon, hold a small basket matching each cell's weight, and crucially match the index's overall duration. The risk metric is tracking error.

**A9. Contrast bullet, barbell and ladder maturity structures.**
A **bullet** clusters maturities at one horizon (lower convexity). A **barbell** concentrates at the short and long ends (higher convexity, expresses a view that curvature will rise). A **ladder** spreads holdings evenly across the curve — automatic diversification, steady reinvestment that averages over rate cycles, and no forecasting required.

**A10. What is DV01 (PVBP) and why do traders prefer it to duration?**
DV01 is the rupee change in a position's value for a 1 bp yield move: $\text{DV01}=D_{mod}\times P\times 0.0001$. Traders hedge with it because it is **additive in currency terms** — you can neutralise a whole book by summing DV01s across positions and offsetting with futures or swaps.

**A11. A single duration assumes a parallel shift. What captures non-parallel risk?**
**Key-rate (partial) durations** — sensitivity to a yield move at *specific* maturity points (2y, 5y, 10y, 30y). They reveal and let the manager control curve-reshaping (twist) risk that one aggregate duration hides.

**A12. What is spread duration and why is it the key number for a corporate book?**
Spread duration is the sensitivity of price to a change in the *credit spread*, holding the government curve fixed. A corporate bond can lose money purely from spread widening with no default, so spread duration — not just default probability — is the live risk for a credit portfolio.

**A13. State the classical immunisation conditions for a single liability.**
(1) Set **portfolio Macaulay duration = liability horizon $H$**; (2) set **PV(assets) = PV(liability)** (fund it fully); (3) **rebalance** periodically, because duration drifts as time passes and yields move (duration falls slower than calendar time, degrading the match).

**A14. How do the conditions generalise for multiple liabilities?**
(i) PV(assets) = PV(liabilities); (ii) asset duration = liability duration; (iii) assets have **greater convexity/dispersion** than the liabilities (the Fong–Vasicek dispersion condition) so asset value dominates liability value for any parallel shift. Residual twist risk is handled with key-rate matching.

**A15. Immunisation vs cash-flow matching (dedication) — one-line each.**
Immunisation matches *duration*, protects mainly against parallel shifts, and needs rebalancing. Cash-flow matching buys bonds whose coupons and maturities *exactly* replicate the liability stream, so no rebalancing or forecast is ever needed — but it costs more yield (fewer degrees of freedom).

**A16. What is contingent immunisation?**
A hybrid: manage the portfolio **actively** as long as the surplus cushion exceeds the cost of locking in an acceptable immunised return; if the cushion erodes to that trigger, switch to pure immunisation. Active upside with a floor.

**A17. Where does convexity turn *negative*, and why is that dangerous?**
In **callable bonds and mortgage-backed securities**. As rates fall, the issuer calls or borrowers prepay, capping price gains at the strike — you hold the downside when rates rise but forfeit the upside when they fall. Falling rates are therefore not unambiguously good for such books.

**A18. Why can "higher yield to maturity" not be equated with "higher realised return"?**
YTM is realised only if every coupon is reinvested at that same yield and the bond is held to maturity. Reinvestment risk breaks the equality, so horizon (holding-period) return can differ sharply from the quoted YTM.

---

## Section B — Numerical Problems

**B1. Duration, DV01 and a convexity-corrected price move.** A 3-year annual-coupon bond, face ₹1,000, coupon 8%, yields 8% (trades at par). Find price, Macaulay and modified duration, DV01, and estimate the price change for **+100 bp**, first with duration alone then with convexity. Verify against full repricing.

**Solution.**
Cash-flow table at $y=8\%$:

| $t$ | $C_t$ | $DF=(1.08)^{-t}$ | $PV$ | $t\cdot PV$ | $t(t{+}1)\cdot PV$ |
|---|---|---|---|---|---|
| 1 | 80 | 0.92593 | 74.074 | 74.074 | 148.148 |
| 2 | 80 | 0.85734 | 68.587 | 137.174 | 411.523 |
| 3 | 1080 | 0.79383 | 857.339 | 2572.017 | 10288.07 |
| **Σ** | | | **1000.00** | **2783.265** | **10847.74** |

Price $P=₹1{,}000$ (par ✓). Macaulay $D_{Mac}=2783.265/1000=2.7833$ yr. Modified $D_{mod}=2.7833/1.08=2.5771$. DV01 $=2.5771\times1000\times0.0001=₹0.2577$. Convexity $C=10847.74/(1000\times1.08^2)=10847.74/1166.4=9.300$.

For $\Delta y=+0.01$: duration only $\Rightarrow \Delta P/P\approx -2.5771\% \Rightarrow \Delta P\approx -₹25.77$. With convexity $\Rightarrow -0.025771+\tfrac12(9.300)(0.0001)=-0.025771+0.000465=-0.025306 \Rightarrow \Delta P\approx -₹25.31$.

Full repricing at 9%: $80/1.09+80/1.09^2+1080/1.09^3=73.394+67.331+833.958=₹974.69$, so actual change $=-₹25.31$.

**Reconciliation.** Duration alone overstated the loss (−₹25.77); adding the positive convexity term shrank it to −₹25.31, matching exact repricing to the paisa. Positive convexity made the real loss *smaller* than the linear estimate. ✓

**B2. Portfolio duration and rebalancing to a target.** A ₹100 crore book holds ₹60 cr of Bond X ($D_{mod}=3.0$) and ₹40 cr of Bond Y ($D_{mod}=7.0$). (a) Find portfolio duration. (b) The manager expects a rate cut and wants duration 6.0. What rupee shift from X to Y achieves it?

**Solution.** (a) $D_P=0.60(3.0)+0.40(7.0)=1.8+2.8=4.6$.
(b) Let new weight in Y be $w$: $3.0(1-w)+7.0w=6.0\Rightarrow 3.0+4.0w=6.0\Rightarrow w=0.75$. So Y must be ₹75 cr and X ₹25 cr — **shift ₹35 cr from X into Y**. Check: $0.25(3.0)+0.75(7.0)=0.75+5.25=6.0$ ✓. Extending duration ahead of an expected cut maximises the price gain.

**B3. Immunising a single liability with a two-bond barbell.** An insurer owes **₹10,00,000 in exactly 3 years**; the flat curve is 8%. Fund with Bond A ($D=1.5$) and Bond B ($D=5.0$). Find weights, rupee allocation, and stress-test at 9%.

**Solution.** $PV_L=1{,}000{,}000/1.08^3=1{,}000{,}000/1.259712=₹793{,}832$; liability duration $=3.0$ (single payment). Match: $1.5w_A+5.0(1-w_A)=3.0\Rightarrow -3.5w_A=-2.0\Rightarrow w_A=0.5714,\ w_B=0.4286$. Allocation: A $=0.5714\times793{,}832=₹453{,}618$; B $=0.4286\times793{,}832=₹340{,}214$. Duration check $0.5714(1.5)+0.4286(5.0)=0.857+2.143=3.00$ ✓.

Stress to 9% ($D_{mod}=D/1.08$): Liability $\Delta=-2.778\%\Rightarrow 793{,}832\times0.97222=₹771{,}780$. Bond A $\Delta=-1.389\%\Rightarrow 453{,}618\times0.98611=₹447{,}316$. Bond B $\Delta=-4.630\%\Rightarrow 340{,}214\times0.95370=₹324{,}462$. New assets $=447{,}316+324{,}462=₹771{,}778$.

**Reconciliation.** Assets ₹7,71,778 vs liability ₹7,71,780 — matched within ₹2 (rounding/convexity). Equal durations meant the parallel shift moved both sides by the same %, preserving surplus. Because the barbell has more convexity than the single-payment liability, for larger shocks assets pull slightly ahead — the favourable dispersion condition. Rebalancing is still needed as time passes. ✓

**B4. DV01-neutral flattener.** A trader expects the 2s10s to flatten. 10y bond: price ₹100, $D_{mod}=8.0$. 2y bond: price ₹100, $D_{mod}=1.9$. (a) Size a duration-neutral long-10y/short-2y trade per ₹100 of 10y. (b) Show it is flat to a +10 bp parallel shift. (c) Show the P/L if the 10y falls 10 bp and the 2y is unchanged.

**Solution.** DV01(10y) $=8.0\times100\times0.0001=₹0.080$; DV01(2y) $=1.9\times100\times0.0001=₹0.019$.
(a) Face of 2y short $=100\times0.080/0.019=₹421.05$. Long ₹100 face 10y, short ₹421 face 2y.
(b) +10 bp both: 10y long $-0.080\times10=-₹0.80$; 2y short $+0.019\times10\times4.2105=+₹0.80$; net ≈ **₹0** ✓.
(c) 10y −10 bp: long $-0.080\times(-10)=+₹0.80$; 2y unchanged $\Rightarrow ₹0$; net **+₹0.80** from the slope alone. The DV01 weighting stripped out parallel-shift risk and isolated the pure curve bet. ✓

**B5. Riding the yield curve (rolldown).** The curve is stable and upward-sloping: a 3-year zero yields 7%, a 2-year zero yields 6%. A manager with a 1-year horizon buys the 3-year zero (face ₹1,000). If the curve is unchanged in one year, compute the 1-year holding return and compare with simply holding a 1-year bond at 5%.

**Solution.** Buy price $=1000/1.07^3=1000/1.225043=₹816.30$. After 1 year it is a 2-year bond; with the curve unchanged it now yields 6%: value $=1000/1.06^2=1000/1.1236=₹889.99$. Holding return $=889.99/816.30-1=0.0903=\textbf{9.03\%}$. The 1-year bond returns just 5%. The extra ≈4.03% is the **rolldown**: as the bond ages it "rolls down" to a lower yield (6% instead of 7%), gaining price on top of carry — but only because the curve did not shift up. ✓

**B6. Credit spread decomposition and spread-duration P/L.** A 5-year corporate yields 9.2%; the matched 5-year government yields 7.0%; the estimated liquidity premium is 0.3%. (a) What is the pure credit spread? (b) The bond's spread duration is 4.2. If the credit spread widens 40 bp (govt curve unchanged), what is the % price change?

**Solution.** (a) $\text{Yield}_{corp}=\text{Yield}_{govt}+\text{credit spread}+\text{liquidity premium}\Rightarrow 9.2=7.0+\text{CS}+0.3\Rightarrow \text{CS}=\textbf{1.9\%}$. (b) $\Delta P/P\approx -\text{SpreadDur}\times\Delta\text{spread}=-4.2\times0.0040=-0.0168=\textbf{-1.68\%}$. The bond loses 1.68% purely from spread widening — no default needed, no move in the govt curve. This is exactly why spread duration is the live risk on a corporate book. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through what duration really measures and its main limitation."**
Duration is the first derivative of price with respect to yield, scaled by price — the % price change per 100 bp move, i.e. the portfolio's interest-rate beta. Its power is additivity: one number steers a whole book. Its limitation is that it is a *linear* approximation to a *convex* price–yield curve, so it is accurate only for small moves, and a single aggregate duration assumes a **parallel** shift. For large moves I add convexity; for curve-reshaping (twist) risk I use key-rate durations.

**C2. "You expect the RBI to cut rates. Position a debt fund."**
Extend duration — buy longer-dated bonds (or receive fixed via swaps / go long bond futures) to maximise price gains from falling yields. I would size the extension to my conviction and the fund's mandate risk limits, because duration timing is the highest-impact and riskiest active bet; if my rate call is wrong, the same lever amplifies losses. I would watch reinvestment: falling rates hurt coupon reinvestment, and if I hold callable/MBS paper, negative convexity caps the upside.

**C3. "An insurer must pay a fixed sum in seven years. How would you fund it, and what can still go wrong?"**
Classical immunisation: set the asset portfolio's Macaulay duration to 7 years, fund the full present value of the liability, ensure asset convexity/dispersion at least matches the liability, and rebalance periodically as duration drifts. What can still go wrong: immunisation protects mainly against *parallel* shifts, so a curve **twist** (short rates and long rates moving differently) can break it — I mitigate with key-rate matching. Duration also drifts immediately, so neglecting rebalancing degrades the match. If certainty is paramount and yield give-up is acceptable, I would instead cash-flow match (dedication) and remove reinvestment and rebalancing risk entirely.

**C4. "Bullet or barbell — which do you buy?"**
Same duration, different convexity. A barbell has higher convexity, so it outperforms a duration-matched bullet on **large** rate moves in either direction; but you pay for that convexity with lower yield. A bullet earns more carry and wins if the curve **stays put**. So it is a bet on realised volatility: if I expect a big move or rising curvature, barbell; if I expect a quiet, stable curve, bullet to harvest the yield pickup.

**C5. "How do you express a credit view without taking a rate view?"**
Buy (or sell) the corporate bond against a **duration-matched government** position — an asset swap. Matching duration neutralises the level of rates, leaving pure exposure to the credit spread. I size it by **spread duration**, not modified duration, because spread duration is what governs the P/L per basis point of spread move. That isolates the compensated credit/liquidity risk I actually want.

**C6. "Why can a bond fund lose money even when interest rates fall?"**
Two reasons. **Reinvestment drag**: coupons and maturities now reinvest at lower rates, so realised compound return disappoints. **Negative convexity**: if the book holds callable bonds or MBS, falling rates trigger calls and prepayments that cap the price upside while carry deteriorates — the classic "heads you lose, tails you don't win" of embedded short optionality. Whether the fund nets a gain depends on its horizon versus duration and the option content of its holdings.

**C7. "What is the single biggest risk in a high-grade bond fund versus a high-yield fund?"**
In a high-grade (sovereign/AAA) fund it is **interest-rate / duration risk** — spreads are thin and stable, so the yield curve dominates the P/L. In a high-yield fund it is **credit / spread risk** — defaults and spread widening drive returns, and duration matters less because prices are governed more by issuer fundamentals and recovery than by the risk-free curve. The right risk metric shifts from modified duration to spread duration and default probability.

---

## Section D — MCQs with Reasoning

**D1. A 10-year coupon bond and a 10-year zero-coupon bond, same yield. Which has the higher duration?**
(a) The coupon bond (b) The zero (c) Equal (d) Depends on coupon size
**Answer: (b).** The zero has a single payment at year 10, so its Macaulay duration equals 10. The coupon bond's early coupons pull its weighted-average time to receipt below 10. A zero always has the maximum duration for a given maturity.

**D2. Modified duration is 6.0 and the bond is priced at ₹95. DV01 per ₹100 face is approximately:**
(a) ₹0.057 (b) ₹0.57 (c) ₹5.70 (d) ₹0.0095
**Answer: (a).** $\text{DV01}=D_{mod}\times P\times 0.0001=6.0\times95\times0.0001=₹0.057$. A 1 bp move changes value by about 5.7 paise per ₹100 of price.

**D3. Positive convexity implies that, for equal-sized yield moves:**
(a) Price falls more than it rises (b) Price rises more than it falls (c) Price change is symmetric (d) Duration is zero
**Answer: (b).** The convex price–yield curve bows toward the origin: the second-order term $+\tfrac12 C(\Delta y)^2$ is always positive, adding to gains when yields fall and cushioning losses when they rise. The favourable asymmetry is why investors pay for convexity.

**D4. To immunise a single liability, the manager sets:**
(a) Coupon = liability payment (b) Maturity = liability horizon (c) Portfolio duration = liability horizon and PV(assets) = PV(liability) (d) Convexity = 0
**Answer: (c).** Matching duration to horizon makes price and reinvestment risk offset; funding the PV ensures the money is there. Matching *maturity* is not enough — a longer-maturity coupon bond can have the right duration, and a bullet at the horizon still needs full PV funding.

**D5. Which structure has the highest convexity for a given duration?**
(a) Bullet (b) Barbell (c) Ladder (d) All equal
**Answer: (b).** Spreading cash flows to the short and long ends (barbell) increases the dispersion of payment times, which raises convexity above a bullet of the same duration. The trade-off is lower yield.

**D6. A callable bond exhibits negative convexity primarily when:**
(a) Rates rise sharply (b) Rates fall toward the call strike (c) The issuer defaults (d) The curve steepens
**Answer: (b).** As rates fall, the issuer's call option moves into the money; the market prices in redemption, capping the bond's price appreciation. The price–yield curve bends the "wrong" way near the strike, giving negative convexity.

**D7. A DV01-weighted long-long-end / short-short-end trade is designed to profit from:**
(a) A parallel upward shift (b) A parallel downward shift (c) A flattening of the curve (d) Rising credit spreads
**Answer: (c).** DV01 weighting neutralises parallel-shift P/L, leaving exposure only to the *slope*. Long the long end and short the short end gains when the spread between them narrows — a flattener.

**D8. Cash-flow matching (dedication) differs from immunisation chiefly because it:**
(a) Requires more frequent rebalancing (b) Requires no rebalancing or rate forecast, but costs more yield (c) Protects only against parallel shifts (d) Ignores present value
**Answer: (b).** Dedication buys bonds whose cash flows exactly meet the liabilities, so no rebalancing or forecasting is ever needed; the cost is a lower yield from the loss of flexibility. Immunisation, by contrast, matches duration, needs rebalancing, and mainly guards against parallel shifts.

**D9. Which measure best captures a corporate bond portfolio's risk to a widening of credit spreads with the government curve unchanged?**
(a) Modified duration (b) Macaulay duration (c) Spread duration (d) Convexity
**Answer: (c).** Spread duration is the sensitivity of price to a change in credit spread holding the risk-free curve fixed — precisely the exposure that widening spreads hit. Modified/Macaulay duration measure sensitivity to the risk-free yield, not the spread.

**D10. A single aggregate duration fails to capture which risk?**
(a) Parallel shift risk (b) Non-parallel (twist/curve-reshaping) risk (c) Default risk only (d) Reinvestment risk
**Answer: (b).** Aggregate duration assumes the whole curve moves by the same amount. A twist — short and long rates moving differently — is invisible to it; key-rate durations are needed to see and control that non-parallel risk.

**D11. Riding the yield curve (rolldown) earns extra return only when:**
(a) The curve is downward-sloping (b) The curve is upward-sloping and stays put (c) Rates rise (d) Credit spreads tighten
**Answer: (b).** On a stable, upward-sloping curve, a bond ages into lower yields and gains price on top of coupon. If the curve shifts up, the roll-up in yield offsets or reverses the gain, so stability of the curve is essential.

**D12. Yield to maturity equals realised return only if:**
(a) The bond is investment grade (b) Every coupon is reinvested at the YTM and the bond is held to maturity (c) Duration equals maturity (d) The curve is flat
**Answer: (b).** YTM embeds the assumption that all coupons compound at that same yield to maturity. Reinvestment at any other rate — or an early sale — breaks the equality, which is the essence of reinvestment risk.

---

*End of Q&A — Fixed Income Portfolio Management.*
