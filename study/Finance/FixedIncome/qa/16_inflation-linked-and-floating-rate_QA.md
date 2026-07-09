# Q&A — Inflation-Linked and Floating-Rate Bonds

A practice bank covering inflation-linked bonds (ILBs/TIPS/IIBs) and floating-rate notes (FRNs). Work each question before reading the answer.

---

## Section A — Concept Checks

**A1. What two distinct risks does a plain vanilla fixed-coupon bond force the investor to bear, and which instrument neutralises each?**

A vanilla bond bundles two exposures. First, **inflation risk**: a fixed coupon and fixed redemption lose real purchasing power as prices rise, so the investor grows poorer in real terms even while "earning interest." Second, **interest-rate (price) risk**: if market yields rise, the fixed stream is now too stingy and the bond's price falls until its yield matches the market. Inflation-linked bonds neutralise the first (they index principal to a price index, locking a real yield); floating-rate notes neutralise the second (they reset the coupon to a reference rate, keeping price near par). Mnemonic: **ILBs protect the value of your money; FRNs protect the value of your bond.**

**A2. In an inflation-linked bond, which leg is fixed and which floats? Contrast with an FRN.**

An ILB fixes the **real coupon rate** and floats the **principal** (scaled by the index ratio). Because the coupon is a fixed percentage of an ever-growing principal, the coupon rupees also grow with inflation. An FRN does the opposite: it fixes the **principal at par** and floats the **coupon rate** (reference rate + spread) at each reset. So ILBs float the principal; FRNs float the coupon.

**A3. Define the index ratio and adjusted principal.**

The index ratio is the current reference CPI divided by the base (issue-date) CPI: `CPI(date) / CPI(base)`. The adjusted (indexed) principal is `Face × index ratio`. If CPI has risen 6% since issue, the index ratio is 1.06 and the adjusted principal is 6% above face — exactly offsetting the 6% loss of purchasing power.

**A4. Why does indexing the principal automatically protect the coupon too?**

Because the coupon is computed as `(real rate / frequency) × adjusted principal`. The real *rate* never changes, but the principal it is applied to grows with inflation, so the coupon cash amount inherits the same uplift. The real value of every cash flow is held constant by construction.

**A5. State the Fisher equation and the approximation for the nominal yield.**

Exact: `(1 + y_nominal) = (1 + y_real) × (1 + π_expected)`. Rearranged, `y_real = (1 + y_nominal)/(1 + π) − 1`. The small-number approximation is `y_nominal ≈ y_real + π`. This is the bridge that lets a nominal bond and an ILB of the same maturity be compared.

**A6. What is breakeven inflation (BEI), and what does it actually contain?**

BEI is the inflation rate at which a nominal bond and an inflation-linked bond of the same maturity deliver the same nominal return: `BEI ≈ y_nominal − y_real`. It is *not* a clean forecast — it equals **expected inflation + inflation risk premium − ILB liquidity premium**. It is the best market-implied read on inflation, but the premia can shift it a few tenths either way.

**A7. Explain the deflation floor and its one key limitation.**

At maturity, a TIPS repays `max(adjusted principal, face)`, so cumulative deflation cannot pull the redemption below original par. The limitation: the floor applies **only to the final redemption**, not to coupons. During a deflationary stretch, coupons are still computed on the (sub-par) adjusted principal, so coupon cash can fall below the nominal-coupon-on-face level.

**A8. Why is an FRN's effective duration so small?**

At each reset the coupon re-strikes to the current market rate + spread, so right after a reset the bond is worth par. The price can only wander from par between resets, by the small value of one period's mispricing. Effective (rate) duration ≈ time to next reset (~0.25 years for a quarterly resetter), not years-to-maturity. Its **spread duration**, however, is close to full maturity.

**A9. What is "phantom income"?**

In the US, the annual principal accretion (the inflation uplift on a TIPS) is taxable in the year it accrues even though no cash is received until maturity. This unpaid-but-taxed accretion is "phantom income," which is why TIPS are often held in tax-deferred accounts.

**A10. "Set in advance, pay in arrears" — what does it mean for an FRN?**

The coupon rate is *fixed* at the start of each period using the reference rate observed at that reset, and the coupon is *paid* at the end of the period. So the investor always knows the rate for the coming period at its start.

---

## Section B — Numerical / Applied (full solutions)

**B1. TIPS cash flow.** Face $1,000, real coupon 2.00% annual (1.00% semiannual), base CPI 250.00. Reference CPI after 6 months = 252.50, after 12 months = 256.00. Compute both coupons and the year-end adjusted principal.

*Solution.* Index ratios: 252.50/250 = 1.0100; 256.00/250 = 1.0240.
- Adjusted principal at period 1 = 1,000 × 1.0100 = **$1,010.00**; coupon = 1.00% × 1,010.00 = **$10.10**.
- Adjusted principal at period 2 = 1,000 × 1.0240 = **$1,024.00**; coupon = 1.00% × 1,024.00 = **$10.24**.
- Total year-1 coupons = 10.10 + 10.24 = **$20.34**; year-end adjusted principal = **$1,024.00** (a $24 accretion, taxable in the US though unpaid).

**B2. Real-return reconciliation.** Using B1, verify the investor earned ≈2% real.

*Solution.* Total one-year economic gain = coupons + accretion = 20.34 + 24.00 = $44.34 on a $1,000 base → nominal return 4.434%. One-year inflation = 250 → 256 = 2.40%.
`y_real = 1.04434 / 1.02400 − 1 = 1.01986 − 1 = 1.99% ≈ 2.00%.` ✓ The real return lands on the stated 2% real coupon; inflation passed straight through the nominal cash flows.

**B3. Deflation floor.** Same bond, but CPI falls to 245 by maturity. What is redeemed?

*Solution.* Index ratio = 245/250 = 0.98, adjusted principal = $980. Redemption = `max(980, 1,000) = $1,000`. The investor is protected against sub-par principal at maturity — though coupons during the deflation would have been computed on the $980 base.

**B4. Breakeven inflation.** 10-year nominal Treasury yields 4.50%; 10-year TIPS (real) yields 2.00%. Compute BEI exactly and approximately, then verify.

*Solution.*
- Exact: `BEI = 1.0450 / 1.0200 − 1 = 1.02451 − 1 = 2.451%`.
- Approx: `4.50% − 2.00% = 2.50%`.
- Verify with Fisher: `(1.0200)(1.02451) − 1 = 1.0450 − 1 = 4.50%` = the nominal Treasury yield. ✓ The two bonds break even at 2.451% inflation.

**B5. Breakeven decision.** Using B4, you expect inflation of 3.5%. Which bond, and by roughly how much per year?

*Solution.* 3.5% > breakeven 2.451%, so buy the **TIPS**. Approximate nominal returns: TIPS ≈ 2.00% + 3.50% = 5.50%; nominal bond = 4.50% fixed. The TIPS outperforms by ≈ **100 bps per year**. (If instead you expected 1.5% inflation, below breakeven, the nominal bond's 4.50% beats the TIPS's ≈3.5%.)

**B6. FRN coupons in a rising-rate world.** 2-year FRN, face $1,000, coupon = 3-month SOFR + 0.40%, reset and paid quarterly. SOFR at the four resets: 3.00%, 3.75%, 4.50%, 5.00%. Compute each quarterly coupon and the year-1 total.

*Solution.* Coupon rate = SOFR + 0.40%; quarterly coupon = rate/4 × 1,000.
- Q1: 3.40% → 0.85% × 1,000 = **$8.50**
- Q2: 4.15% → **$10.375**
- Q3: 4.90% → **$12.25**
- Q4: 5.40% → **$13.50**
- Year-1 total = 8.50 + 10.375 + 12.25 + 13.50 = **$44.625**.

**B7. FRN vs fixed contrast.** Using B6, a fixed 3.40% bond struck at issue would have paid what for the year, and what happens to each bond's price as SOFR climbs 3%→5%?

*Solution.* Fixed bond pays 3.40% × 1,000 = **$34.00** for the year — far less than the FRN's $44.625 — and its **price falls sharply** as rates rise (it has full duration). The FRN raised its coupon from $8.50 to $13.50 and held its price near $1,000, because each reset re-struck the coupon to market; its duration was only ~0.25 years, so the 200 bps move barely dented the price. The fixed holder is hurt twice (low income *and* capital loss); the FRN holder is protected on both counts.

**B8. Discount margin.** The FRN in B6 has quoted margin 0.40%. Mid-life the issuer's credit worsens and the market demands SOFR + 0.90%. What happens to the price, and what residual risk does this illustrate?

*Solution.* The discount margin (0.90%) now exceeds the quoted margin (0.40%), so the fixed 0.40% spread is too thin. Price falls below par by roughly `(0.90% − 0.40%) × remaining spread duration`. This shows the FRN neutralised *interest-rate* risk but **retained credit-spread risk** — the residual exposure, measured by the discount margin.

**B9. Fisher reverse-check.** A linker offers 1.20% real. You forecast 4% inflation. What nominal return do you expect, exactly and approximately?

*Solution.* Exact: `(1.0120)(1.0400) − 1 = 1.05248 − 1 = 5.25%`. Approx: `1.20% + 4.00% = 5.20%`. The exact figure is slightly higher because of the cross-term (real × inflation).

**B10. Negative real yield.** A TIPS is quoted at a real yield of −0.80%. With expected inflation of 2.5%, what nominal return is implied, and what is the investor effectively doing?

*Solution.* `(1 − 0.0080)(1.0250) − 1 = 0.9920 × 1.0250 − 1 = 1.0168 − 1 = 1.68%` nominal. The investor accepts a return *below* inflation (−0.80% real) to lock in guaranteed inflation protection — effectively paying an insurance premium for certainty, as was common in 2020–21.

---

## Section C — Interview-Style (model answers)

**C1. "Does a TIPS have interest-rate risk?"**

Yes — it has **real-rate duration**. A TIPS is inflation-*protected*, not rate-immune. It is still a long-dated instrument, and if *real* yields rise, its price falls just like any long bond. What it sheds is inflation risk, not duration. The instrument that sheds duration is the FRN, not the ILB.

**C2. "Why is an FRN's duration so low, and what duration does it keep?"**

Because the coupon resets to the market reference rate + spread every period, the price is pulled back to par at each reset, so it can only drift within one reset window. Effective rate duration ≈ time to next reset (~0.25 years for a quarterly note). However, its **spread duration is close to full maturity** — if the issuer's credit spread widens, the price still moves substantially. So an FRN keeps credit-spread risk while shedding rate risk.

**C3. "If inflation rises, is an FRN a good hedge?"**

Only *indirectly and conditionally*. FRNs track *nominal* short rates. If inflation rises and the central bank hikes in response, the reference rate — and the coupon — rises with it, giving partial protection. But under financial repression (rates deliberately held below inflation, negative real rates), the FRN does **not** protect real purchasing power. Only an inflation-linked bond guarantees a real return regardless of policy.

**C4. "What does breakeven inflation actually contain — is it the market's forecast?"**

It's market-*implied*, not a clean forecast. BEI = expected inflation **+ inflation risk premium − ILB liquidity premium**. The risk premium reflects compensation for inflation uncertainty; the liquidity premium reflects that linkers are typically less liquid than nominals. These can move BEI a few tenths of a percent away from pure expectations.

**C5. "Can real yields be negative? What would justify buying at a negative real yield?"**

Yes, and it happens — many TIPS traded at negative real yields in 2020–21. Buying at a negative real yield means accepting a guaranteed sub-inflation return in exchange for *certainty* of inflation protection. An investor with inflation-linked liabilities, or one who fears an inflation surprise, may rationally pay this premium rather than risk a nominal bond being eroded.

**C6. "Difference between India's sovereign IIB and the retail IINSS-C?"**

The **sovereign IIB (2013)** is capital-indexed like TIPS: the principal is indexed (WPI initially, later CPI) and a fixed real coupon is paid on that indexed principal — so both principal and coupon are inflation-protected. The **retail IINSS-C (Dec 2013)** used a simpler *additive* design: coupon = 1.5% p.a. + realised CPI inflation, with the **principal fixed at face**. So the IINSS-C protects income against inflation but does not grow the principal — an additive structure, not a capital-indexed one. The sovereign series' switch from WPI to CPI reflected CPI becoming the RBI's official inflation target.

**C7. "What risk does an FRN NOT remove?"**

Credit-spread risk. The FRN strips out interest-rate risk but isolates and concentrates credit exposure into the **discount margin**. If the issuer's credit deteriorates, the market demands a discount margin above the fixed quoted margin, and the price falls below par. The quoted margin is locked at issue; only the price can adjust.

**C8. "How would you use these two instruments to hedge liabilities?"**

Match the instrument to the liability shape. Pension funds and insurers with **inflation-linked liabilities** (indexed pensions) buy ILBs to match real cash flows and lock a real return. Institutions with **floating-rate assets or a desire to minimise duration** in a rising-rate cycle use FRNs to stay near par and let income track the policy rate. If both inflation and rate risk are live, blend them or use an inflation-linked FRN.

---

## Section D — MCQs (with reasoning)

**D1.** In a capital-indexed TIPS, the coupon *rate* is:
(a) reset each period to CPI  (b) fixed in real terms  (c) fixed in nominal terms  (d) CPI + a fixed spread

**Answer: (b).** The real rate is fixed; what grows is the principal it's applied to, so coupon *cash* grows while the *rate* stays constant. (c) describes a vanilla bond; (a)/(d) describe the additive Indian IINSS-C, not a capital-indexed TIPS.

**D2.** A 5-year FRN resetting quarterly has an effective (rate) duration closest to:
(a) 5 years  (b) 2.5 years  (c) 0.25 years  (d) 0 exactly

**Answer: (c).** Duration ≈ time to next reset. It is not literally zero because there is still a fraction of a period of rate exposure; it is nowhere near the 5-year maturity.

**D3.** Nominal yield is 5.0%, real yield is 2.0%. Approximate breakeven inflation is:
(a) 2.5%  (b) 3.0%  (c) 7.0%  (d) 10.0%

**Answer: (b).** BEI ≈ nominal − real = 5.0% − 2.0% = 3.0%. (Exact: 1.05/1.02 − 1 = 2.94%.)

**D4.** The deflation floor on a TIPS guarantees:
(a) every coupon is at least the nominal-on-face amount  (b) redemption is at least original face  (c) the index ratio never falls below 1  (d) the real yield stays positive

**Answer: (b).** `Redemption = max(adjusted principal, face)`. It protects only the maturity redemption; coupons can still fall below the nominal-on-face level during deflation, so (a) is wrong.

**D5.** An FRN's price falls below par mainly when:
(a) the reference rate rises  (b) the reference rate falls  (c) the issuer's discount margin exceeds the quoted margin  (d) inflation rises

**Answer: (c).** Rate moves are absorbed by resets. Price drifts below par when credit deteriorates so the required discount margin exceeds the fixed quoted margin. (a) is largely neutralised by the reset mechanism.

**D6.** "Phantom income" on a TIPS refers to:
(a) the coupon paid in kind  (b) the inflation accretion taxed before it is received in cash  (c) the deflation adjustment  (d) the liquidity premium in BEI

**Answer: (b).** US tax rules tax the annual principal accretion in the accrual year, though the cash arrives only at maturity.

**D7.** You expect inflation of 2%. The market's breakeven inflation is 3%. You should prefer:
(a) the TIPS  (b) the nominal bond  (c) indifferent  (d) cannot tell

**Answer: (b).** Your expected inflation (2%) is below breakeven (3%), so the nominal bond is expected to outperform; the linker only wins if realised inflation exceeds breakeven.

**D8.** Which statement is TRUE?
(a) ILBs have no interest-rate risk  (b) FRNs fully hedge inflation  (c) ILBs shed inflation risk but keep real-rate duration  (d) FRNs have high rate duration and low spread duration

**Answer: (c).** ILBs remain long instruments exposed to real-rate moves. (a) and (b) are classic confusions; (d) is exactly backwards — FRNs have low rate duration and high spread duration.

**D9.** India's retail IINSS-C bond paid a coupon of:
(a) a fixed real rate on indexed principal  (b) 1.5% + realised CPI inflation, principal fixed  (c) WPI-linked principal with a fixed coupon  (d) SOFR + spread

**Answer: (b).** The IINSS-C was additive (1.5% + CPI) with principal fixed at face — distinct from the capital-indexed sovereign IIB in (a)/(c).

**D10.** In "set in advance, pay in arrears," the coupon rate is:
(a) fixed at period end, paid at start  (b) fixed at period start, paid at period end  (c) fixed and paid both at end  (d) unknown until maturity

**Answer: (b).** The rate is observed and fixed at the reset (start of period); the cash is paid at the end.

---

*Self-verification note: B1–B10 solved and cross-checked against the chapter's worked examples and formula table; Fisher reverse-checks (B2, B4, B9) tie back exactly to the stated nominal yields. Formula usage — index ratio, adjusted principal, `max(adjusted, face)`, Fisher exact/approx, BEI, FRN coupon = reference + margin, and DM > quoted margin ⇒ sub-par price — matches Section 10's quick-reference table.*
