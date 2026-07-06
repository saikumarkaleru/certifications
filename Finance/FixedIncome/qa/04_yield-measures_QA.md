# Q&A — Yield Measures

A practice bank for Chapter 04. Every question is followed by a full answer; work each before reading the answer. Convention: coupon bonds are semiannual pay, "BEY" is the semiannual periodic yield doubled, and face value is \$1,000 unless stated otherwise.

---

## Section A — Concept Checks

**A1. In one sentence, what is a bond yield?**

A yield is the discount rate implied by the market price — you take the observed price as given and solve the pricing equation *backwards* for the rate that equates the present value of the cash flows to that price. It is the internal rate of return (IRR) of the bond's cash-flow stream.

**A2. Every yield measure is the same inversion of the pricing equation. What three choices distinguish one measure from another?**

(1) *Which cash flows* are counted — this period's coupon only, all coupons to maturity, or all coupons to a call date; (2) *what terminal/redemption value* is assumed — par at maturity, the call price, or a sale price at some horizon; (3) *what compounding/annualisation convention* turns the periodic rate into a quoted annual figure.

**A3. Why is current yield a poor total-return measure?**

Current yield (annual coupon ÷ price) captures income return only. It ignores the capital gain or loss from buying at a discount or premium and pulling to par, ignores the timing and compounding of coupons, and ignores reinvestment. For a deep-discount bond it can badly understate total return.

**A4. State the three assumptions baked into YTM.**

(1) The bond is held to maturity; (2) there is no default — every coupon and the principal are paid in full and on time; (3) all coupons are reinvested at the YTM itself until maturity. Break any one and the realised return diverges from the quoted YTM.

**A5. Why is YTM an IRR rather than a simple ratio?**

A coupon in six months is worth more than the same coupon in five years, so an honest measure must discount for timing. The single rate making discounted inflows equal the price is exactly an IRR — and, like all IRRs, it embeds a reinvestment assumption: interim coupons are presumed reinvested at that same solved rate.

**A6. Write the yield ordering for discount, par, and premium bonds.**

- Discount bond: coupon rate < current yield < YTM
- Par bond: coupon rate = current yield = YTM
- Premium bond: coupon rate > current yield > YTM

**A7. Why does the discount-bond ordering hold?**

For a discount bond you paid less than par, so dividing the *same* coupon by a smaller price lifts current yield above the coupon rate. YTM sits higher still because it *also* captures the pull-to-par capital gain that current yield ignores.

**A8. Define yield to call and yield to worst.**

Yield to call (YTC) is the IRR computed with the cash-flow stream truncated at a call date and the terminal value set to the call price rather than maturity par; a separate YTC exists for each call date. Yield to worst (YTW) is the *minimum* across the YTM and every YTC (and yield-to-put where relevant) — the conservative floor quoted on callable bonds.

**A9. Distinguish bond-equivalent yield from effective annual yield.**

BEY simply *doubles* the semiannual periodic yield (a simple, non-compounding annualisation). EAY *compounds* it: $(1+y_{\text{semi}})^2 - 1$. Because compounding adds the interest-on-interest term, BEY is always less than EAY whenever the periodic rate is positive.

**A10. What two risks make the realised yield differ from the promised YTM, and which direction does each push?**

*Reinvestment risk*: if rates fall, coupons reinvest at lower rates, pulling realised yield below the YTM. *Price risk*: if rates rise before your horizon, the bond's sale price falls. They pull in opposite directions and roughly cancel at a horizon near the bond's duration (the basis of immunisation).

**A11. For a premium callable bond trading above its call price, is the yield to worst usually the YTM or the YTC? Why?**

Usually the YTC. The issuer has cheap-to-refinance incentive to call the bond, so the investor should assume the call scenario, which for a premium bond gives the lower yield. Quoting the YTM here would overstate the realistic return.

**A12. Why does linear interpolation slightly overstate the true YTM?**

The price–yield curve is convex (bowed toward the origin), so the straight line drawn between two priced points lies *below* the true curve. Reading a rate off that chord for a given price therefore returns a value a touch higher than the true yield. Always re-price to verify.

---

## Section B — Numerical Bond-Math Problems

**B1. A bond has face \$1,000, an 8% semiannual coupon (\$40 every six months), 5 years (10 periods) to maturity, and trades at \$960.44. Compute the current yield and the YTM (as BEY), then confirm the discount ordering.**

Current yield $= 80 / 960.44 = 8.33\%$.

For YTM, since the bond trades at a discount we expect YTM > coupon (8%). Try a semiannual $y = 4.5\%$:

- $(1.045)^{10} = 1.553069$, so $(1.045)^{-10} = 0.643928$
- Annuity factor $= (1 - 0.643928)/0.045 = 0.356072/0.045 = 7.912711$
- PV coupons $= 40 \times 7.912711 = 316.51$
- PV principal $= 1000 \times 0.643928 = 643.93$
- Total $= 316.51 + 643.93 = 960.44$ ✓

The semiannual yield is exactly 4.5%, so YTM $= 2 \times 4.5\% = 9.00\%$ BEY.

Ordering: coupon 8.00% < current yield 8.33% < YTM 9.00%. This is the discount ordering. The 39.56 gap between price and par is the pull-to-par capital gain that current yield omits but YTM captures.

**B2. Solve the same bond's YTM by interpolation, bracketing between 4% and 5% semiannual, and explain the direction of the error.**

At $y = 4\%$ (yield = coupon → price = par): $P = 1000.00$.

At $y = 5\%$: $(1.05)^{10} = 1.628895$, inverse $= 0.613913$; annuity factor $= (1-0.613913)/0.05 = 7.721735$; $P = 40(7.721735) + 1000(0.613913) = 308.87 + 613.91 = 922.78$.

Interpolate for the target \$960.44:

$$y \approx 4\% + \frac{1000 - 960.44}{1000 - 922.78}\times 1\% = 4\% + \frac{39.56}{77.22}\times 1\% = 4\% + 0.512\% = 4.512\%$$

That gives BEY $\approx 9.02\%$ versus the true 9.00%. The interpolation *overstates* by ~2 bps because convexity puts the true price–yield curve above the chord. Re-pricing at exactly 4.5% returns \$960.44, confirming the true yield.

**B3. Using B1's 4.5% semiannual yield, compute the BEY and the effective annual yield, and quantify the convention gap.**

- BEY (simple doubling) $= 2 \times 4.5\% = 9.00\%$
- EAY (compounded) $= (1.045)^2 - 1 = 1.092025 - 1 = 9.2025\%$

The 9.00% quote understates the true annually-compounded return by about 20 bps — a pure artefact of doubling instead of compounding.

**B4. A competing annual-pay bond quotes a 9.20% effective annual yield. Put it on a bond-equivalent basis and compare it to B1's 9.00% BEY.**

$$\text{BEY} = 2\left[(1 + \text{EAY})^{1/2} - 1\right] = 2\left[(1.092)^{1/2} - 1\right] = 2[1.044988 - 1] = 2(0.044988) = 8.998\% \approx 9.00\%$$

On a like-for-like BEY basis the two bonds are essentially identical (9.00% vs 9.00%), even though the naive "9.00% vs 9.20%" comparison made the annual-pay bond look better. This is exactly the trap the convention exists to prevent — always convert to a common basis before comparing.

**B5. A 90-day T-bill is priced at \$98.50 per \$100 face. Compute its money-market bond-equivalent yield.**

Holding-period return $= (100 - 98.50)/98.50 = 1.5228\%$. Annualise on a 365-day add-on basis:

$$\text{BEY} = 1.5228\% \times \frac{365}{90} = 6.18\%$$

This 365-day add-on figure is now directly comparable to a coupon bond's yield.

**B6. Take the B1 bond (bought \$960.44, ten \$40 coupons, redeemed at \$1,000, held to maturity). Show that reinvesting coupons at the 4.5% semiannual YTM reproduces exactly the 9.00% BEY.**

Future value of the reinvested coupon stream:

$$\text{FV}_{\text{coupons}} = 40 \times \frac{(1.045)^{10} - 1}{0.045} = 40 \times \frac{0.553069}{0.045} = 40 \times 12.29042 = 491.62$$

Terminal value $= 491.62 + 1000 = 1491.62$. Realised semiannual yield:

$$\left(\frac{1491.62}{960.44}\right)^{1/10} - 1 = (1.55307)^{0.1} - 1 = 1.045 - 1 = 4.5\%$$

Realised BEY $= 9.00\% = $ the YTM exactly. This proves YTM's reinvestment assumption is "reinvest at the YTM": when it holds, promised and realised yields coincide.

**B7. Repeat B6 but reinvest coupons at only 3% semiannual (6% annual). Quantify the shortfall and reconcile with B6.**

$$\text{FV}_{\text{coupons}} = 40 \times \frac{(1.03)^{10} - 1}{0.03} = 40 \times \frac{0.343916}{0.03} = 40 \times 11.46387 = 458.55$$

Terminal value $= 458.55 + 1000 = 1458.55$. Realised semiannual yield:

$$\left(\frac{1458.55}{960.44}\right)^{1/10} - 1 = (1.518635)^{0.1} - 1 = 1.042650 - 1 = 4.265\%$$

Realised BEY $= 8.53\%$ — a full 47 bps below the promised 9.00%. The *only* thing that changed from B6 was the reinvestment rate, and realised yield moved in the same direction (down), so the two cases reconcile cleanly. This is reinvestment risk in hard numbers.

| Reinvestment rate (annual) | Terminal value | Realised BEY |
|---|---|---|
| 9.0% (= YTM) | \$1,491.62 | 9.00% |
| 6.0% | \$1,458.55 | 8.53% |

**B8. Now hold the B1 bond only 2 years (4 periods) and sell when market yields have risen to 10% BEY (5% semiannual). Compute the realised yield and explain why it fell below 9%.**

*Sale price* (6 periods remain, discount at 5% semiannual): $(1.05)^6 = 1.340096$, inverse $= 0.746215$; annuity factor $= (1-0.746215)/0.05 = 5.07570$; price $= 40(5.07570) + 1000(0.746215) = 203.03 + 746.22 = 949.24$.

*Reinvested coupons* (4 coupons compounded at 5%): $\text{FV} = 40 \times \frac{(1.05)^4 - 1}{0.05} = 40 \times 4.31013 = 172.41$.

*Terminal value* $= 949.24 + 172.41 = 1121.65$. Realised semiannual yield over 4 periods:

$$\left(\frac{1121.65}{960.44}\right)^{1/4} - 1 = (1.16785)^{0.25} - 1 = 1.03955 - 1 = 3.955\%$$

Realised BEY $= 7.91\%$ — below 9.00% despite the *higher* 5% reinvestment rate. Over this short horizon the price risk (capital loss from selling into a higher yield) swamped the reinvestment benefit. Near the bond's duration the two effects would cancel; at maturity only reinvestment matters (B6–B7).

**B9. Bond B: face \$1,000, 8% semiannual coupon (\$40), 5 years (10 periods) to maturity, callable in 3 years (6 periods) at \$1,020, trading at a premium of \$1,050. Find YTM, YTC, and YTW (all as BEY).**

*YTM (par \$1,000).* Premium → YTM < coupon. Try 3.4% semiannual: $(1.034)^{10} = 1.397028$, inverse $= 0.715806$; annuity factor $= (1-0.715806)/0.034 = 8.35865$; $P = 40(8.35865) + 1000(0.715806) = 334.35 + 715.81 = 1050.15 \approx 1050$ ✓. So YTM $\approx 3.40\%$ semiannual $= 6.80\%$ BEY.

*YTC (6 periods, call price \$1,020).* Bracket it. At $y_c = 3.4\%$: $(1.034)^6 = 1.222134$, inverse $0.818238$; annuity $= (1-0.818238)/0.034 = 5.34594$; price $= 40(5.34594) + 1020(0.818238) = 213.84 + 834.60 = 1048.44$. At $y_c = 3.3\%$: $(1.033)^6 = 1.215039$, inverse $0.823019$; annuity $= 5.36306$; price $= 214.52 + 839.48 = 1054.00$. Interpolate for \$1,050:

$$y_c \approx 3.3\% + \frac{1054.00 - 1050}{1054.00 - 1048.44}\times 0.1\% = 3.3\% + \frac{4.00}{5.56}(0.1\%) = 3.372\%$$

YTC $\approx 3.37\%$ semiannual $= 6.74\%$ BEY.

*YTW* $= \min(6.80\%, 6.74\%) = 6.74\%$, the yield-to-call. Classic result for a premium callable trading above its call price: assume the issuer calls, so the honest quote is the lower YTC.

**B10. A 2-year zero-coupon bond, face \$1,000, trades at \$888.49. Find its YTM as BEY.**

A zero has one cash flow, so the yield solves directly with no interpolation. On a semiannual (4-period) basis:

$$888.49 = \frac{1000}{(1+y)^4} \Rightarrow (1+y)^4 = \frac{1000}{888.49} = 1.125491 \Rightarrow 1+y = 1.125491^{0.25} = 1.030000$$

So $y = 3.00\%$ semiannual and YTM $= 6.00\%$ BEY. Check: $1000/(1.03)^4 = 1000/1.125509 = 888.48$ ✓ (rounding). A zero carries no reinvestment risk — there are no interim coupons — so its promised YTM *is* its realised yield if held to maturity.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "A client says a bond's coupon is its return. How do you correct them?"**

Model answer: The coupon rate is fixed at issuance and measured against *face value*, not what you actually paid. Buy below par and your income return per dollar is higher than the coupon rate, plus you gain as the price pulls to par; buy above par and both work against you. The coupon equals your return only at par. The right total-return measure is yield to maturity, which folds in price, all coupons, their timing, and the redemption value.

**C2. "Walk me through why YTM is a 'promised' rather than a 'guaranteed' yield."**

Model answer: YTM is an IRR, and every IRR silently assumes you reinvest interim cash flows at that same rate. So the quoted YTM is realised only if three things hold: you hold to maturity, the issuer never defaults, and every coupon is reinvested at the YTM. In a falling-rate world coupons reinvest below the YTM and realised return drops — a 9% bond whose coupons reinvest at 6% realises only about 8.5%. That is reinvestment risk: YTM is a promise conditional on assumptions, not a guarantee.

**C3. "Two bonds: one pays semiannually and yields 9.00%, the other pays annually and yields 9.20%. Which is better?"**

Model answer: You can't compare them until they share a convention. The 9.00% is a bond-equivalent yield (a doubled semiannual rate); the 9.20% is an effective annual yield. Convert the annual-pay figure to BEY: $2[(1.092)^{1/2}-1] = 9.00\%$ — identical. Equivalently the semiannual bond's EAY is $(1.045)^2 - 1 = 9.20\%$. Either way they tie; the naive quote comparison is exactly the trap the conventions exist to expose.

**C4. "Why would you ever quote yield-to-worst instead of yield-to-maturity?"**

Model answer: With embedded issuer options — mainly callables — the YTM assumes survival to maturity, but the issuer calls whenever that benefits them, which is precisely when it hurts you. Yield-to-worst takes the minimum yield across maturity and every call date, so it is the conservative floor. For a premium callable above its call price the worst case is almost always the call: the issuer refinances cheap debt and you lose the remaining premium quickly. Quoting the YTM there would systematically overstate return.

**C5. "You immunise a liability by matching duration. Intuitively, why does that neutralise interest-rate risk?"**

Model answer: A bondholder faces two opposing rate exposures. If rates rise, the sale price falls (price risk) but coupons reinvest at higher rates; if rates fall, the reverse. These effects grow at different speeds with the horizon. At a horizon roughly equal to the bond's duration, a small rate change moves price and reinvestment by offsetting amounts, so the realised yield is locked in whichever way rates move. Matching the asset's duration to the liability's horizon is therefore what immunises the position against small rate shifts.

**C6. "A junior analyst interpolated a YTM and got 9.02%; the solver says 9.00%. Is the analyst wrong?"**

Model answer: Not wrong, just approximate and predictably biased. Linear interpolation draws a straight chord between two priced points, but the price–yield relationship is convex, bowing above that chord, so a rate read off the chord comes out slightly too high — the 2-bp overstatement is exactly what convexity predicts. Treat interpolation as a first pass, then re-price at the interpolated rate to confirm and narrow the bracket if needed.

---

## Section D — Multiple-Choice Questions with Reasoning

**D1. A bond trades at a premium. Which ordering is correct?**

A. coupon < current yield < YTM  
B. coupon > current yield > YTM  
C. coupon = current yield = YTM  
D. current yield > coupon > YTM

**Answer: B.** For a premium bond you paid more than par, so dividing the coupon by a larger price pushes current yield below the coupon rate, and YTM sits still lower because it also captures the pull-to-par capital *loss*. A is the discount ordering; C is the par case; D violates the fixed relationship between coupon and price.

**D2. Which statement about bond-equivalent yield is TRUE?**

A. BEY always exceeds the effective annual yield.  
B. BEY compounds the semiannual rate.  
C. BEY simply doubles the semiannual rate and is therefore below the EAY.  
D. BEY and EAY are identical for semiannual bonds.

**Answer: C.** BEY is a simple doubling; EAY compounds, adding an interest-on-interest term, so EAY > BEY whenever the periodic rate is positive (e.g. 9.00% vs 9.2025%). A and D reverse or erase the gap; B confuses BEY with EAY.

**D3. A premium bond is callable and currently trades above its call price. Its yield to worst is most likely:**

A. the yield to maturity  
B. the current yield  
C. the yield to call  
D. the coupon rate

**Answer: C.** The issuer is incentivised to call and refinance cheap debt, and for a premium bond the call scenario produces the lower yield, so YTW = YTC. A would understate the risk of being called; B and D are not scenario yields at all.

**D4. An investor holds a coupon bond to maturity in a falling-rate environment. Relative to the purchase-date YTM, the realised yield will be:**

A. higher, because the bond's price rose  
B. lower, because coupons reinvest below the YTM  
C. exactly the YTM, because it was held to maturity  
D. unaffected by reinvestment

**Answer: B.** Held to maturity, the ending value is par regardless of rates, so price risk is irrelevant; the only open variable is the reinvestment rate. Coupons reinvested below the YTM drag realised yield beneath the promised figure. C ignores reinvestment; A confuses this with a sell-before-maturity scenario; D is simply false for a coupon bond.

**D5. Which yield measure ignores capital gain/loss and the time value of coupons entirely?**

A. yield to maturity  
B. current yield  
C. realised yield  
D. yield to call

**Answer: B.** Current yield is just annual coupon ÷ price — an income snapshot with no discounting and no pull-to-par adjustment. The other three all discount cash flows over time and account for the redemption or sale value.

**D6. Linear interpolation of a YTM between two priced points tends to:**

A. understate the true yield, because the curve is concave  
B. overstate the true yield, because the price–yield curve is convex  
C. exactly equal the true yield  
D. overstate the price, not the yield

**Answer: B.** The price–yield curve is convex, so the interpolating chord lies below it; reading a yield off the chord for a given price returns a value slightly too high. A misstates the curvature; C ignores convexity; D confuses the axes.

**D7. A zero-coupon bond held to maturity has:**

A. high reinvestment risk  
B. no reinvestment risk, because there are no interim coupons  
C. a realised yield below its YTM  
D. a current yield equal to its YTM

**Answer: B.** With no interim coupons there is nothing to reinvest, so the promised YTM equals the realised yield if held to maturity. A and C wrongly import coupon-bond reinvestment risk; D is meaningless since a zero pays no coupon, giving a current yield of zero.

---

*Self-check: every numerical answer was verified by substituting the solved rate back into the pricing or terminal-value equation and confirming it reproduces the stated price or yield; the discount ordering (B1), reinvestment cases (B6–B8), and callable YTW (B9) all reconcile internally.*
