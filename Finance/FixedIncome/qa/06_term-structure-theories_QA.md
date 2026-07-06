# Q&A — The Term Structure of Interest Rates

Companion practice bank for Chapter 06. Every question is followed by a full answer. Unless stated otherwise, all rates are **annually compounded**, face value is **100**, and coupons are **annual**.

---

## Section A — Concept Check

**A1. What is the term structure of interest rates, and how does it differ from "the yield curve"?**
The term structure is the relationship between yield and time to maturity, holding credit quality, liquidity, and all other features constant. It answers "what rate applies to each horizon?" The *yield curve* is simply the graphical plot of that relationship — maturity on the x-axis, yield on the y-axis. The term structure is the concept; the yield curve is its picture.

**A2. Why can a single interest rate not correctly price a coupon bond?**
A coupon bond is really a portfolio of zero-coupon cash flows arriving at different dates. Each date has its own time value of money, captured by its own spot rate. The year-1 coupon should be discounted at the 1-year spot, the year-5 redemption at the 5-year spot. Applying one blended yield (YTM) to all cash flows is a convenient shortcut that generally misprices the bond and distorts relative-value comparisons — the "coupon effect."

**A3. Distinguish the spot curve, the par curve, and the forward curve.**
- **Spot (zero) curve:** the yield on a single cash flow received at time *t* — the theoretically correct discount rate.
- **Par curve:** the coupon rate that makes a newly issued bond of each maturity price exactly at 100. This is usually what market commentary means by "the 10-year yield."
- **Forward curve:** rates for periods that *begin in the future* but are locked in *today*, implied arithmetically by the spot curve.
They are three views of the same no-arbitrage information: given any one, you can derive the other two.

**A4. Why are spot rates the "honest" discount rates? What enforces them?**
No-arbitrage. A coupon bond must equal the sum of its cash flows valued at each maturity's spot rate; if it did not, a trader would strip the bond into zeros (or reconstitute it) and pocket the difference. The US Treasury **STRIPS** market makes this literal — it is the real-world mechanism that enforces the spot curve rather than leaving it an academic construct.

**A5. What is bootstrapping, in one sentence?**
Bootstrapping is the recursive extraction of spot rates from observed coupon-bond prices, one maturity at a time: the 1-year rate comes directly from a 1-year instrument, then each longer spot is solved after discounting the earlier coupons at the already-known spots.

**A6. State the four canonical curve shapes and the typical signal of each.**
- **Normal (upward):** long > short; healthy expansion, modest expected rises and/or term premium.
- **Flat:** yields roughly equal; a transition point, often preceding inversion.
- **Inverted (downward):** short > long; market expects rate *cuts*, usually because it expects a slowdown.
- **Humped:** rises then falls (peak in the belly); near-term tightening expected to reverse later.

**A7. On an upward-sloping curve, rank par yield, spot rate, and forward rate at a given maturity, and explain why.**
**Par < spot < forward.** The spot rate is a geometric average of forwards, so it lags the rising forwards. The par yield is a coupon-weighted blend that puts weight on cheaper near-dated rates, so it sits below the spot. On an inverted curve the inequalities reverse.

**A8. Name the four term-structure theories and give the one-line distinction of each.**
- **Pure (unbiased) expectations:** long rate = geometric average of expected future short rates; forwards are unbiased forecasts.
- **Liquidity preference:** add a rising term premium; forwards *overstate* expected future spots.
- **Market segmentation:** separate maturity clienteles set local yields independently.
- **Preferred habitat:** the realistic hybrid — investors have preferred habitats but will leave them for a large enough premium; premiums can be positive or negative.

**A9. Why is an inverted curve read as a recession warning rather than a recession cause?**
An inverted curve reflects the market *pricing in future rate cuts*, and the central bank cuts when it expects the economy to weaken — so inversion is a symptom of that aggregated expectation, not the cause. It can still *amplify* a downturn: banks borrow short and lend long, so when short rates exceed long rates their net interest margins compress, credit tightens, and the slowdown can become partly self-fulfilling.

---

## Section B — Numerical Bond-Math Problems

### B1. Bootstrap a 2-year spot curve

You observe a 1-year zero priced at **96.1538** and a 2-year 5% annual-coupon bond priced at **100.05**. Find the 1- and 2-year spot rates.

**Step 1 — one-year spot.** The zero pays 100 in one year:
$$1+s_1 = \frac{100}{96.1538} = 1.04000 \Rightarrow \boxed{s_1 = 4.00\%}$$

**Step 2 — two-year spot.** The 2-year bond pays 5 at *t*=1 and 105 at *t*=2. Discount the year-1 coupon at the known $s_1$:
$$\frac{5}{1.04} = 4.8077 \Rightarrow \frac{105}{(1+s_2)^2} = 100.05 - 4.8077 = 95.2423$$
$$(1+s_2)^2 = \frac{105}{95.2423} = 1.10244 \Rightarrow 1+s_2 = 1.04998 \Rightarrow \boxed{s_2 = 5.00\%}$$

**Reconcile:** reprice the bond off the curve: $\dfrac{5}{1.04} + \dfrac{105}{1.05^2} = 4.8077 + 95.2381 = 100.046 \approx 100.05.$ ✓

### B2. Implied forward rates

Extend the curve with a 3-year spot of **5.50%** (so $s_1=4.0\%,\ s_2=5.0\%,\ s_3=5.5\%$). Compute the one-year forwards.

$$1+f(1,2) = \frac{(1+s_2)^2}{1+s_1} = \frac{1.1025}{1.04} = 1.06010 \Rightarrow \boxed{f(1,2)=6.01\%}$$
$$1+f(2,3) = \frac{(1+s_3)^3}{(1+s_2)^2} = \frac{1.174241}{1.1025} = 1.06507 \Rightarrow \boxed{f(2,3)=6.51\%}$$

**Reconcile** the 3-year spot as the geometric average of one-year forwards:
$$(1+s_1)(1+f(1,2))(1+f(2,3)) = 1.04 \times 1.06010 \times 1.06507 = 1.174246 = (1+s_3)^3$$
Cube root $= 1.05500 \Rightarrow s_3 = 5.50\%.$ ✓ Note the forwards (4.00%, 6.01%, 6.51%) rise faster than the spots (4.0%, 5.0%, 5.5%) and sit above them — exactly the upward-curve pattern.

### B3. Par yield and the ordering rule

From the same spot curve, compute the 3-year par yield. First the discount factors:

| t | $s_t$ | $DF_t = 1/(1+s_t)^t$ |
|---|---|---|
| 1 | 4.00% | 0.961538 |
| 2 | 5.00% | 0.907029 |
| 3 | 5.50% | 0.851614 |
| | **Sum** | **2.720182** |

$$c_3 = \frac{100\,(1 - DF_3)}{\sum DF_t} = \frac{100\,(1 - 0.851614)}{2.720182} = \frac{14.8386}{2.720182} = \boxed{5.455\%}$$

**Reconcile:** price a 3-year 5.455% bond: $5.455 \times 2.720182 + 100 \times 0.851614 = 14.839 + 85.161 = 100.00.$ ✓

**Ordering check** at the 3-year point: par **5.455%** < spot **5.50%** < forward $f(2,3)$ **6.51%** — confirms *par < spot < forward* for the upward curve.

### B4. Coupon vs par yield — where does a bond trade?

Using the curve above, price a 3-year **6% annual-coupon** bond off the spot curve.
$$P = 6(DF_1) + 6(DF_2) + 106(DF_3) = 6(0.961538) + 6(0.907029) + 106(0.851614)$$
$$P = 5.7692 + 5.4422 + 90.2711 = \boxed{101.48}$$
The bond trades **above par** because its 6% coupon exceeds the 3-year par yield of 5.455% — a premium bond. This is the direct link between the par yield and whether a given coupon prices above or below 100.

### B5. Inverted curve — forwards decline

Now the curve flips: $s_1 = 5.0\%,\ s_2 = 4.5\%,\ s_3 = 4.0\%$. Extract the one-year forwards.
$$1+f(1,2) = \frac{1.045^2}{1.05} = \frac{1.092025}{1.05} = 1.04002 \Rightarrow \boxed{f(1,2)=4.00\%}$$
$$1+f(2,3) = \frac{1.04^3}{1.045^2} = \frac{1.124864}{1.092025} = 1.03007 \Rightarrow \boxed{f(2,3)=3.01\%}$$

**Reconcile:** $1.05 \times 1.04002 \times 1.03007 = 1.124864 = (1+s_3)^3$; cube root $= 1.04000 \Rightarrow s_3 = 4.00\%.$ ✓

The forwards **fall** (5.0% → 4.0% → 3.0%). Under pure expectations the market is pricing the 1-year rate dropping year by year — i.e., expected central-bank cuts, the classic slowdown signal.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through bootstrapping a spot curve. Why not just use YTM?"**
*Model answer:* "Start with the shortest instrument — a 1-year bill or zero gives the 1-year spot directly. For the 2-year bond, I already know how to value its first coupon using the 1-year spot, so whatever price is left over must be explained by the 2-year spot; I solve for it. I repeat maturity by maturity, each step reusing all the spots I've already recovered. I bootstrap rather than use YTM because YTM applies a *single* rate to every cash flow, which is only correct for a zero. The spot curve gives each cash flow its own honest discount rate, and no-arbitrage — enforced by the STRIPS market — says the bond must equal the sum of its zeros valued that way."

**C2. "The 2-year yield is 5% and the 3-year is 5.5%. What does that tell you about next year's rates?"**
*Model answer:* "The implied one-year forward from year 2 to 3 is $(1.055^3/1.05^2) - 1 \approx 6.5\%$. So the *curve* implies the 1-year rate two years out is around 6.5%. But I'd immediately caveat: that forward equals the market's expected future spot **only under the pure expectations hypothesis**. Once you allow a term premium — liquidity preference — the forward overstates the expected rate by that premium, so the true expectation is lower. I'd never say the curve 'predicts' 6.5% without that qualifier."

**C3. "Why is the yield curve usually upward-sloping even when nobody expects rates to rise?"**
*Model answer:* "The liquidity/term premium. Longer bonds have higher duration and more price risk, so lenders demand extra yield to hold them. That premium generally rises with maturity, which tilts the curve upward on its own — independent of any expected rate change. So a mildly upward curve is the 'normal' resting state; only an unusually *steep* curve signals strongly expected hikes."

**C4. "An interviewer says: 'The curve just inverted. Recession?' How do you respond?"**
*Model answer:* "Inversion means short yields sit above long yields, which means the market is pricing future rate cuts — and the central bank cuts when it expects the economy to weaken. So historically the 10y–2y and 10y–3m spreads going negative have preceded nearly every US recession of the last 60 years. Two nuances: first, inversion is a *symptom* of expectations, not a cause, though it can amplify a slowdown by compressing bank net interest margins since banks borrow short and lend long. Second, with a positive term premium an inverted curve is an even *stronger* signal, because expected cuts must be large enough to overcome the premium before long yields fall below short ones."

**C5. "Compare the four term-structure theories and tell me which one practitioners actually believe."**
*Model answer:* "Pure expectations says the long rate is just the geometric average of expected short rates, so forwards are unbiased forecasts — clean but unrealistic because it assumes risk-neutrality. Liquidity preference adds a rising term premium, so forwards overstate expected rates and the normal curve is mildly upward. Market segmentation says different clienteles — banks short, pensions and insurers long — trade in separate maturity buckets set by local supply and demand, which explains kinks expectations can't. Preferred habitat is the hybrid and the modern consensus: investors have preferred habitats but will leave them for a big enough premium, so both expectations and premiums matter and the premium can be positive or negative depending on supply-demand at each maturity."

---

## Section D — Multiple Choice (with Reasoning)

**D1.** On an upward-sloping spot curve, which ordering is correct at a given maturity?
A) forward < spot < par  B) par < spot < forward  C) spot < par < forward  D) forward < par < spot
**Answer: B.** The spot is a geometric average of forwards so it lags the rising forwards (spot < forward); the par yield is a coupon-weighted blend weighted toward cheaper near-dated rates, so par < spot. Hence par < spot < forward.

**D2.** A forward rate equals the expected future spot rate only under which theory?
A) Liquidity preference  B) Market segmentation  C) Pure expectations  D) Preferred habitat
**Answer: C.** Only pure expectations assumes a zero term premium, making forwards unbiased forecasts. Every other theory embeds a premium, so the forward is a biased (usually upward) estimate.

**D3.** The 1-year spot is 4% and the 2-year spot is 5%. The one-year forward $f(1,2)$ is closest to:
A) 4.5%  B) 5.0%  C) 6.0%  D) 4.0%
**Answer: C.** $1+f(1,2) = 1.05^2/1.04 = 1.1025/1.04 = 1.0601$, so ≈6.0%. On an upward curve the forward must exceed the longer spot, which rules out A, B, and D.

**D4.** Which best explains a persistent kink or bump at one maturity that expectations theory cannot?
A) Pure expectations  B) Market segmentation / preferred habitat  C) The Fisher effect  D) Convexity
**Answer: B.** Localized supply-demand imbalances from distinct maturity clienteles are exactly what segmentation and preferred habitat capture; pure expectations produces a smooth curve driven only by expected short rates.

**D5.** A 3-year bond's coupon is 6% and the 3-year par yield is 5.455%. The bond will trade:
A) at par  B) at a discount  C) at a premium  D) cannot tell
**Answer: C.** Coupon (6%) exceeds the par yield (5.455%), so the bond pays more than a par bond of the same maturity and prices above 100 — a premium bond (here ≈101.48, per B4).

**D6.** An inverted curve most directly reflects that the market expects:
A) rising inflation  B) future rate cuts  C) higher term premiums  D) heavy bond issuance
**Answer: B.** Short above long means the implied forwards decline, i.e., the market prices the short rate falling — future rate cuts, which the central bank delivers when it expects a slowdown.

**D7.** For which instrument do YTM and the spot rate always coincide?
A) A par coupon bond  B) A premium bond  C) A zero-coupon bond  D) A floating-rate note
**Answer: C.** A zero has a single cash flow, so its single internal rate of return (YTM) is exactly the spot rate for that maturity. Coupon bonds blend many spot rates, so their YTM only approximates the curve.

---

*Self-verification note:* All bootstrapped spots, forwards, and par yields in Section B were cross-checked by repricing each bond off the recovered curve and by rebuilding each long spot as the geometric average of its one-year forwards; every figure reconciles to within rounding.
