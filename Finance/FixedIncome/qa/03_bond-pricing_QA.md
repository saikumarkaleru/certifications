# Q&A — Bond Pricing

A practice bank for Chapter 03. Every question is followed by a full worked answer. Work each one on paper before reading the solution.

---

## Section A — Concept Check

**A1. In one sentence, what is a bond's price?**
The present value of every cash flow the bond will pay (coupons plus principal), discounted back to today at the yield the market currently requires for a bond of that risk and maturity. It is nothing more than PV-of-an-annuity plus PV-of-a-lump-sum.

**A2. Why do price and yield move in opposite directions?**
Because the cash flows in the numerator are fixed and the yield sits in the denominator. Raising the discount rate shrinks every term `C/(1+y)^t` and `F/(1+y)^n`, so the sum — the price — must fall. It is arithmetic, not sentiment. Even though the bondholder still receives every promised rupee, the present value of those unchanged rupees drops when rates rise.

**A3. What is the difference between the coupon rate and the yield?**
The coupon rate is fixed at issue and printed on the bond; it determines the rupees paid. The yield floats with the market and determines how those rupees are valued today. They coincide only when the bond trades at par.

**A4. State the premium / par / discount test.**
Compare coupon rate with required yield. Coupon > yield → premium (price above par). Coupon = yield → par (price equals face). Coupon < yield → discount (price below par). The premium or discount equals the PV of the coupon surplus or shortfall versus the market rate.

**A5. What must you do to the inputs when a bond pays semi-annually?**
Halve the coupon, halve the annual yield, and double the number of periods. Discounting semi-annual periods at a full annual rate is the single most common beginner error.

**A6. Define clean price, dirty price, and accrued interest, and give the identity linking them.**
Dirty (full/invoice) price is the actual PV of remaining cash flows on the settlement date and the amount that changes hands. Accrued interest is the slice of the current coupon that has economically accrued to the seller since the last coupon date. Clean (quoted/flat) price is dirty minus accrued. The identity: `Dirty = Clean + Accrued Interest`.

**A7. Why do screens quote the clean price rather than the dirty price?**
The dirty price jumps down by the full coupon on each ex-coupon date — a mechanical sawtooth that has nothing to do with the bond becoming cheaper or richer. Stripping out accrued interest leaves a clean price that moves only when yields move, which is what a trader wants to watch.

**A8. What is the yield to maturity (YTM), formally?**
The single discount rate that makes the present value of all the bond's cash flows equal its observed market price. Equivalently, the bond's internal rate of return if held to maturity with all coupons reinvested at that same rate.

**A9. Is the price–yield relationship linear?**
No. It is downward-sloping and convex (bowed toward the origin). Symmetric yield moves produce asymmetric price changes: the price gain from a rate fall exceeds the price loss from an equal rate rise.

**A10. Where does a discount bond's return come from?**
From two sources: the below-market coupons plus a capital gain as the price is pulled up to par at maturity. A premium bond is the mirror — fat coupons offset by a capital loss pulling down to par. Priced correctly, both deliver exactly the market YTM.

---

## Section B — Numerical Bond-Math Problems

### B1 — Pricing a zero-coupon bond

**Problem.** A zero-coupon bond, face ₹1,000, matures in 3 years. The required annual yield is 7%. Price it.

A zero pays no coupons, so the price is just the PV of the single principal repayment:
```
P = F / (1 + y)^n = 1000 / (1.07)^3
```
- `1.07^3 = 1.225043`
- `P = 1000 / 1.225043 = ₹816.30`

**Reconcile.** With no coupons, the bond can only sell at a deep discount (₹816.30 < ₹1,000); the entire return is the pull to par. Check: growing ₹816.30 at 7% for 3 years gives `816.30 × 1.225043 = ₹1,000`. ✓

### B2 — Premium bond, annual coupons

**Problem.** Face ₹1,000, 10% annual coupon (`C = ₹100`), 3 years to maturity, required yield 8%. Price it and verify the regime.

```
P = C × [1 − (1+y)^(−n)] / y + F × (1+y)^(−n)
```
- `(1.08)^(−3) = 1 / 1.259712 = 0.793832`
- Annuity factor `= (1 − 0.793832) / 0.08 = 0.206168 / 0.08 = 2.577097`
- PV of coupons `= 100 × 2.577097 = 257.710`
- PV of principal `= 1000 × 0.793832 = 793.832`
- **Price `= 257.710 + 793.832 = ₹1,051.54`**

**Reconcile.** Coupon rate (10%) > yield (8%), so we expect a premium — and ₹1,051.54 > ₹1,000. ✓ The premium of ₹51.54 should equal the PV of the excess coupon (₹100 paid vs ₹80 the market demands on face = ₹20/year extra): `20 × 2.577097 = ₹51.54`. Matches exactly. ✓

### B3 — Semi-annual bond, getting the halving right

**Problem.** Face ₹1,000, 7% annual coupon paid semi-annually, 3 years to maturity, quoted annual yield 8% (semi-annual compounding). Price it.

Convert to per-period inputs:
- Coupon per period `C = 7% × 1000 / 2 = ₹35`
- Per-period yield `y = 8% / 2 = 0.04`
- Periods `n = 3 × 2 = 6`

Compute:
- `1.04^6 = 1.265319`, so `(1.04)^(−6) = 0.790315`
- Annuity factor `= (1 − 0.790315) / 0.04 = 0.209685 / 0.04 = 5.242137`
- PV of coupons `= 35 × 5.242137 = 183.475`
- PV of principal `= 1000 × 0.790315 = 790.315`
- **Price `= 183.475 + 790.315 = ₹973.79`**

**Reconcile.** Coupon rate (7%) < yield (8%), so we expect a discount — and ₹973.79 < ₹1,000. ✓ Common-error check: had we discounted 6 periods at the full 8% or used ₹70 coupons, the answer would be nonsense. The discipline holds — coupon halved, yield halved, periods doubled.

### B4 — Accrued interest and dirty price

**Problem.** A ₹100 face bond pays a 9% annual coupon semi-annually (₹4.50 every six months). Coupon dates are 15 February and 15 August. Settlement is 15 May. Day-count is 30/360. The clean price is quoted at ₹101.20. Find the accrued interest and the dirty price.

**Step 1 — days elapsed (30/360).** From 15 Feb to 15 May, each month counts as 30 days: Feb→Mar = 30, Mar→Apr = 30, Apr→May = 30 → **90 days elapsed**. Full coupon period (15 Feb to 15 Aug) = 180 days.

**Step 2 — accrued interest.**
```
AI = Coupon per period × (days elapsed / days in period)
   = 4.50 × (90 / 180) = 4.50 × 0.5 = ₹2.25
```

**Step 3 — dirty price.**
```
Dirty = Clean + Accrued = 101.20 + 2.25 = ₹103.45
```

**Interpretation.** The buyer pays ₹103.45 on 15 May and will collect the entire ₹4.50 coupon on 15 August despite holding the bond only three of the six months. The ₹2.25 paid up front reimburses the seller for the three months (Feb–May) the seller held it; the buyer's own share of the coupon is `4.50 − 2.25 = ₹2.25`, matching the three months (May–Aug) they own the bond: `4.50 × 90/180 = ₹2.25`. ✓ The accrual splits the coupon fairly.

### B5 — Backing out the YTM by bracketing

**Problem.** A ₹1,000 face, 5% annual-coupon (`C = ₹50`), 3-year bond trades at ₹986.51. Find its YTM.

YTM is the `y` solving `986.51 = 50 × [1 − (1+y)^(−3)]/y + 1000 × (1+y)^(−3)`. There is no closed-form inverse, so we bracket and iterate.

| Trial yield | Resulting price | vs target 986.51 |
|---|---|---|
| 5% | 1,000.00 | too high → raise yield |
| 6% | 973.27 | too low → lower yield |
| 5.5% | 986.51 | exact ✓ |

Check the winning trial at y = 5.5%:
- `(1.055)^(−3) = 1 / 1.174241 = 0.851614`
- Annuity factor `= (1 − 0.851614) / 0.055 = 0.148386 / 0.055 = 2.697927`
- PV of coupons `= 50 × 2.697927 = 134.896`
- PV of principal `= 1000 × 0.851614 = 851.614`
- Price `= 134.896 + 851.614 = ₹986.51` ✓ → **YTM = 5.5%**

**Reconcile.** The bond trades at a discount (₹986.51 < ₹1,000), so its yield must exceed its 5% coupon — and 5.5% > 5%. ✓ The monotonic (inverse) price–yield relationship is what lets us bracket: the target price sits between the 5% and 6% prices, so the yield sits between 5% and 6%.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Rates rose and I still receive every coupon, so why did I lose money?"**
Model answer: "You will indeed receive every promised rupee, but valuation is about the present value of those rupees, not their face amount. When the market's discount rate rises, each fixed cash flow is discounted harder, so the sum — the mark-to-market price — falls. If you sell today you crystallise that loss; if you hold to maturity you get par back, but you have still suffered an opportunity cost versus newly issued bonds now paying higher coupons."

**C2. "A bond pays an 8% coupon. Does it yield 8%?"**
Model answer: "Only if it trades at par. The 8% coupon rate fixes the rupees paid; the yield depends on the price you pay for those rupees. Buy it below par and the yield exceeds 8% because a capital gain to par is added; buy it above par and the yield is below 8% because of the capital loss to par. Coupon rate and YTM coincide exactly at par and diverge everywhere else."

**C3. "Walk me through why a bond trades at a premium."**
Model answer: "A premium arises when the coupon rate exceeds the market's required yield. The coupon stream is more generous than what the market demands, so buyers compete for it and bid the price above par until the effective return on the higher purchase price falls back to the market yield. Mechanically, the premium above par equals the present value of the excess coupons — the extra rupees per period versus what the market rate would pay on face, discounted over the bond's life."

**C4. "Which is the better buy, a premium bond or a discount bond?"**
Model answer: "Neither is inherently better; if both are priced correctly they deliver exactly the market YTM. The difference is only where the return is packaged. A premium bond front-loads return into fat coupons but you book a capital loss pulling down to par; a discount bond pays skinny coupons but delivers a capital gain pulling up to par. The choice is about tax treatment, reinvestment risk, and cash-flow timing preferences, not about one being cheap and the other dear."

**C5. "Explain the difference between clean and dirty price to a new analyst."**
Model answer: "The dirty price is the true economic value and the amount that actually settles — the present value of all remaining cash flows on the settlement date. The clean price is the dirty price with accrued interest stripped out, and it is the number quoted on screens. We quote clean because the dirty price mechanically drops by a full coupon on every ex-coupon date; stripping accrued interest removes that sawtooth so the quoted price moves only with yields. 'Dirty' is not pejorative — it is the honest, full price."

**C6. "How would you find a bond's yield if you only know its price?"**
Model answer: "There is no closed-form inverse of the pricing equation, so I solve for the YTM iteratively. Because price is a strictly decreasing, monotonic function of yield, I can bracket the answer: pick a yield that prices the bond too high and one that prices it too low, then converge by bisection or Newton-Raphson until the model price matches the market price. A quick sanity check first: if the bond trades below par the yield is above the coupon rate, and vice versa — that tells me which side to start from."

---

## Section D — Multiple-Choice Questions with Reasoning

**D1. A bond's required yield rises from 6% to 7%. Holding cash flows fixed, its price will:**
A) rise   B) fall   C) stay the same   D) rise then fall

**Answer: B.** The fixed cash flows sit in the numerator and the yield in the denominator; raising the discount rate shrinks every discounted term, so the price must fall. The relationship is monotonic and inverse.

**D2. A bond with a 9% coupon trades at a required yield of 11%. It is a:**
A) premium bond   B) par bond   C) discount bond   D) cannot be determined

**Answer: C.** Coupon rate (9%) < required yield (11%), so the price falls below par to compensate the buyer with a capital gain to par plus the below-market coupons — the definition of a discount bond.

**D3. For a bond quoted at a clean price of ₹98 with ₹1.50 of accrued interest, the amount the buyer actually pays is:**
A) ₹96.50   B) ₹98.00   C) ₹99.50   D) ₹1.50

**Answer: C.** `Dirty = Clean + Accrued = 98.00 + 1.50 = ₹99.50`. The dirty price is what settles; the buyer reimburses the seller for interest accrued since the last coupon and later collects the whole next coupon.

**D4. A 6% annual-coupon bond paid semi-annually, priced at a 6% annual yield, over any whole number of years, trades at:**
A) a premium   B) par   C) a discount   D) depends on maturity

**Answer: B.** When the coupon rate equals the required yield, the coupons exactly compensate the market rate and no price adjustment is needed, so the bond trades at par regardless of maturity. (Halving both the coupon and the yield preserves the equality: 3% per period coupon against 3% per period yield.)

**D5. Dropping a bond's yield by 1% raises its price by ₹42, while raising the yield by 1% lowers its price by only ₹38. This asymmetry reflects:**
A) an arithmetic error   B) convexity of the price–yield curve   C) accrued interest   D) a rating change

**Answer: B.** The price–yield curve is convex (bowed toward the origin), so the price gain from a rate fall exceeds the price loss from an equal rate rise. This is a genuine property of the pricing function, not an error — its formal measure is convexity.

**D6. The current yield of a discount bond, relative to its coupon rate and YTM, will:**
A) equal the coupon rate   B) equal the YTM   C) lie between the coupon rate and the YTM   D) exceed both

**Answer: C.** Current yield (annual coupon ÷ price) ignores the pull-to-par capital gain and the time value of intermediate coupons, so it always sits between the coupon rate and the YTM. For a discount bond, coupon rate < current yield < YTM; it should never be used as the bond's true return.

---

*Self-check reminders when solving any pricing problem: (1) put coupon, yield, and periods on the same per-period footing; (2) confirm the premium/discount agrees with the coupon-vs-yield comparison; (3) verify the premium/discount magnitude equals the PV of the coupon surplus/shortfall; (4) sanity-check the limits — as y → 0 the price approaches the undiscounted sum of cash flows, and as y → ∞ it approaches zero.*
