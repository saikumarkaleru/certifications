# Q&A — Money Market Instruments and Yields

A practice bank for Chapter 13. Work each numerical item on paper before reading the solution. All yields follow the chapter conventions: BDY and MMY use a 360-day year, BEY and EAY use 365, and EAY compounds.

---

## Section A — Concept Checks

**A1. What defines the money market, and why is credit quality uniformly high?**
The money market is the wholesale market for high-quality debt with an original maturity of one year or less (most activity is overnight to 90 days). Credit quality is uniformly high because the buyers are cash managers whose mandate is capital preservation, not yield. Only very strong issuers — sovereigns, top-rated corporates and financials, and banks — can sell short paper cheaply. A weak credit simply cannot place short paper at a good price, which is itself a warning signal (e.g., firms that lost access to the CP market in 2008).

**A2. Name the two structural flavors of money-market instruments and give examples of each.**
(1) Pure discount / single-payment: you pay less than face today and receive full face at maturity, with no coupon; the interest is face minus price. Examples: T-bills, commercial paper, banker's acceptances. (2) Add-on / interest-bearing: you invest face today and receive face plus interest at maturity. Examples: negotiable CDs, repos, fed funds.

**A3. Why is short maturity such a powerful risk-control device?**
It attacks all three risks at once. Interest-rate (duration) risk is tiny because a 90-day instrument barely moves in price when rates jump. Credit risk is contained because a borrower's ability to survive 30–90 days is far more predictable than its ten-year solvency. Liquidity is high because standardized short paper is easy to value and sell. This is why cautious institutional cash lives here.

**A4. On which two dimensions do the four yield conventions differ?**
(1) The base you divide the interest by — face value (BDY) versus price paid (MMY, BEY, EAY). (2) The day-count / compounding used to annualize — 360 simple (BDY, MMY), 365 simple (BEY), or 365 compounded (EAY).

**A5. Why does the bank discount yield understate an investor's true return?**
Two reasons. It divides the dollar discount by face value F — the amount you do NOT pay — rather than by price P, the amount you actually invest. And it annualizes over a 360-day year instead of the actual 365. Both push the number down, so BDY is a quoting convention, not an investment return.

**A6. State the universal ordering of the four yields and justify each inequality.**
BDY < MMY < BEY < EAY. MMY beats BDY by fixing the base (price instead of face). BEY beats MMY by stretching the year from 360 to 365 days. EAY beats BEY by adding compounding on top of the same 365-day base.

**A7. Why is money-market yield also called "CD-equivalent yield"?**
Converting a discount instrument to MMY restates its return on a price base over a 360-day year — exactly the basis on which an add-on CD is quoted. So MMY expresses a discount instrument's return "as if" it were an add-on CD, letting the two be compared directly on identical footing.

**A8. What is rollover (refinancing) risk, and why is it central to commercial paper?**
CP issuers continuously re-issue maturing paper to fund ongoing needs. Rollover risk is the danger that when old paper matures, the market refuses to buy new paper. Because the issuer relies on constant re-issuance, a buyers' strike creates an instant funding crisis even for a fundamentally solvent firm.

**A9. Why is a banker's acceptance called "two-name paper"?**
It starts as a time draft drawn on a bank by a trade counterparty. When the bank stamps "accepted," it guarantees payment at maturity, adding its own credit to the drawer's. The instrument then carries two obligors' credit — the original drawer and the accepting bank — hence "two-name paper."

**A10. What does "breaking the buck" mean and what caused the classic case?**
A money-market fund normally holds a stable $1.00 NAV. "Breaking the buck" is the NAV falling below $1.00 (roughly below $0.995). The classic case was the Reserve Primary Fund in September 2008, which held Lehman Brothers commercial paper that became nearly worthless when Lehman failed. The fund broke the buck, triggering a run on prime MMFs and a freeze in the CP market.

---

## Section B — Numerical / Applied

**B1. A 90-day T-bill with face $100,000 trades at $98,000. Compute HPY, BDY, MMY, BEY, and EAY.**
D = 100,000 − 98,000 = 2,000; t = 90.
- HPY = 2,000 / 98,000 = 2.0408%.
- BDY = (D/F)(360/t) = (2,000/100,000)(360/90) = 0.02 × 4 = **8.0000%**.
- MMY = HPY × 360/t = 0.020408 × 4 = **8.1633%**.
- BEY = HPY × 365/t = 0.020408 × 4.05556 = **8.2766%**.
- EAY = (1.020408)^(365/90) − 1 = 1.020408^4.05556 − 1 = **8.5383%**.
Ordering holds: 8.00 < 8.16 < 8.28 < 8.54. The quoted 8.00% understates the true compounded return by over half a point.

**B2. Verify B1's MMY and BEY using the direct-from-BDY formulas.**
- MMY = 360·BDY / (360 − t·BDY) = (360 × 0.08)/(360 − 90 × 0.08) = 28.8 / 352.8 = **8.1633%** ✓
- BEY = 365·BDY / (360 − t·BDY) = (365 × 0.08)/352.8 = 29.2 / 352.8 = **8.2766%** ✓
Both routes reconcile exactly to the HPY-based answers.

**B3. A dealer quotes 60-day CP, face $1,000,000, at BDY = 5.25%. Find the price and the dollar discount.**
P = F(1 − BDY × t/360) = 1,000,000 × (1 − 0.0525 × 60/360) = 1,000,000 × (1 − 0.00875) = **$991,250**.
Discount D = 1,000,000 − 991,250 = **$8,750**.

**B4. Using B3, compute HPY, MMY, BEY, and EAY for the commercial paper.**
HPY = 8,750 / 991,250 = 0.8827%.
- MMY = 0.008827 × 360/60 = 0.008827 × 6 = **5.2963%**.
- BEY = 0.008827 × 365/60 = 0.008827 × 6.08333 = **5.3699%**.
- EAY = 1.008827^(365/60) − 1 = 1.008827^6.08333 − 1 = **5.4918%**.
The BEY of ~5.37% versus a comparable T-bill's BEY is the credit-plus-liquidity risk premium the money market prices daily.

**B5. A negotiable CD has face $1,000,000, term 180 days, add-on rate 4.80% (360 basis), bought at issue for face. Find interest, maturity value, BEY, and EAY.**
Interest = F × r × t/360 = 1,000,000 × 0.048 × 180/360 = **$24,000**. Maturity value = **$1,024,000**.
HPY = 24,000 / 1,000,000 = 2.400% (base is face, since price = face).
- BEY = 0.024 × 365/180 = 0.024 × 2.02778 = **4.8667%**.
- EAY = 1.024^(365/180) − 1 = 1.024^2.02778 − 1 = **4.9267%**.
Note the CD's quoted 4.80% sits close to its true return, because the add-on convention already divides interest by the amount actually invested.

**B6. A 91-day T-bill is quoted at BDY = 4.00%, face $100,000. Compute price, then MMY and BEY via the direct formulas.**
P = 100,000 × (1 − 0.04 × 91/360) = 100,000 × (1 − 0.0101111) = **$98,988.89**.
- MMY = (360 × 0.04)/(360 − 91 × 0.04) = 14.4 / (360 − 3.64) = 14.4 / 356.36 = **4.0409%**.
- BEY = (365 × 0.04)/356.36 = 14.6 / 356.36 = **4.0970%**.

**B7. Comparison decision: Instrument X is a 90-day discount bill quoted BDY = 5.00%. Instrument Y is a 90-day add-on CD quoted 5.05%. Which yields more on a comparable basis?**
Put both on MMY (360, price base). For X: MMY = 360 × 0.05 / (360 − 90 × 0.05) = 18 / 355.5 = 5.0633%. For Y, an add-on CD bought at face already has its quote on a price/360 basis, so its CD-equivalent (MMY) yield is simply 5.05%. Compare: X = 5.0633% vs Y = 5.0500%. **The discount bill X is slightly richer** — a raw-quote glance (5.00 vs 5.05) would have wrongly favored the CD. This is exactly why you must convert before choosing.

**B8. Show that ignoring the 360-vs-365 difference on an 8% instrument mis-states the yield by roughly 11 bps.**
The two conventions differ by the factor 365/360 = 1.013889. On an 8% yield the gap is 8% × (365/360 − 1) = 8% × 0.013889 = 0.1111% ≈ **11 bps**. Compare B1: MMY 8.1633% (360) vs BEY 8.2766% (365) — a difference of 11.3 bps, enough to flip which of two close instruments is cheaper.

---

## Section C — Interview-Style

**C1. "Walk me through why a T-bill quoted at 8% doesn't actually return 8% to the investor."**
The 8% is a bank discount yield, a legacy convention. It divides the dollar discount by the bill's face value — but the investor never pays face; she pays the discounted price, a smaller number, so dividing by the larger face understates the return. It also annualizes over a 360-day year rather than the real 365. Fix the base (divide by price) and you get the money-market yield, ~8.16%; stretch to 365 days and you get the bond-equivalent yield, ~8.28%; add compounding and you get the effective annual yield, ~8.54%. So the true economic return is about half a point above the quote. Never quote BDY as "the return."

**C2. "A client says commercial paper is a better deal than T-bills because it yields more. How do you respond?"**
First, make sure we compare on a common basis — convert both quotes to bond-equivalent yield so the calendar and base match. Once that's done, the CP will still yield more, but that spread isn't free money: it's compensation for credit risk (CP is unsecured corporate debt, a T-bill is sovereign) and liquidity risk (CP is thinner and can seize up). The right question isn't "does it yield more?" — it's "does the spread adequately pay for the extra credit and rollover risk?" In calm markets that spread is small and stable; when it blows out, it's one of the earliest warnings of system stress.

**C3. "Explain the difference between a discount instrument and an add-on instrument, and why it matters for the yield math."**
A discount instrument (T-bill, CP, BA) is bought below face with no coupon — the interest is face minus price, and your investment base is the discounted price. An add-on instrument (negotiable CD) is bought at face and pays face plus interest at maturity — your investment base is face itself. It matters because the yield base is the price you actually paid: for a discount instrument that's below face, which is why converting a quoted discount yield to a price-based yield raises it noticeably; for an add-on CD bought at face, the quote is already close to the true return. Mixing up the structure corrupts the denominator and the whole calculation.

**C4. "What happened to money market funds in 2008, and how did regulators respond?"**
The Reserve Primary Fund held Lehman commercial paper. When Lehman failed in September 2008, that paper collapsed, pushing the fund's true value below $1.00 — it "broke the buck." Investors, who had treated MMF shares as cash-equivalent, ran on prime funds, and the CP market froze because funds are major CP buyers. Regulators (via the SEC's Rule 2a-7 framework, tightened after 2008 and again in 2014 and 2023) responded by tightening credit-quality, maturity, and diversification limits, requiring minimum daily and weekly liquid assets, splitting funds so government funds keep a stable $1.00 NAV while prime/institutional funds must float their NAV to reflect true market value, and permitting liquidity fees to slow runs.

**C5. "Why do central bankers care so much about the money market?"**
Because it's where monetary policy enters the interest-rate system. Open-market operations, repos, and the policy rate all act on the money market first — the overnight rate is the anchor from which the rest of the yield curve is built. When the central bank injects reserves, the short rate falls and the effect ripples out along the curve. It's also where liquidity is priced every single day, so its credit spreads (like the TED or CP-over-bills spread) are among the most reliable real-time gauges of financial stress.

**C6. "You see the CP-over-T-bill spread suddenly widen. What does it tell you?"**
That spread is a short-maturity credit spread — the extra yield investors demand to lend to corporates rather than the sovereign for a few weeks. A sudden widening means investors are being paid much more to take short corporate credit, i.e., they're fleeing toward the safety of bills (a flight to quality). It typically signals that lenders are pulling back from short-term funding, which raises rollover risk for issuers who must continuously re-issue. Historically it's an early, reliable warning of a funding squeeze, precisely because it's the market where willingness to lend short is tested daily.

---

## Section D — MCQs (with reasoning)

**D1. Which yield always sits highest for a given discount trade?**
(a) BDY (b) MMY (c) BEY (d) EAY
**Answer: (d) EAY.** It uses the largest base (price), the longer 365-day year, AND adds compounding — every lever that raises the number. The fixed ordering is BDY < MMY < BEY < EAY.

**D2. The money-market yield differs from the bond-equivalent yield only in:**
(a) the base (face vs price) (b) the day-count (360 vs 365) (c) whether it compounds (d) the instrument it applies to
**Answer: (b).** Both divide by price; MMY uses 360 days (CD-comparable), BEY uses 365 (coupon-bond-comparable). Neither compounds.

**D3. A negotiable CD is best described as:**
(a) bought at a discount to face (b) bought at face, redeemed above face (c) a coupon bond (d) a zero-coupon perpetual
**Answer: (b).** It's an add-on instrument: invest face, receive face plus interest. Only discount instruments (T-bill, CP, BA) are bought below par. Assuming a CD is discounted is a classic trap.

**D4. The price of a discount instrument from its quoted BDY is:**
(a) F(1 + BDY × t/360) (b) F(1 − BDY × t/360) (c) F / (1 + BDY × t/365) (d) F × BDY × t/360
**Answer: (b).** BDY quotes interest as a fraction of face over 360 days, so the discount is F × BDY × t/360 and price is face minus that discount: F(1 − BDY × t/360).

**D5. Which spread is a widely used real-time gauge of money-market stress?**
(a) the bid-ask spread on 30-year bonds (b) the TED / CP-over-bills spread (c) the dividend yield spread (d) the on-the-run/off-the-run Treasury spread
**Answer: (b).** The TED spread (and CP-over-bills) is a short-term credit spread; it stays narrow in calm markets and widens sharply under stress, signaling a flight to quality and rollover strain.

**D6. After 2008 reforms, which category of MMF is REQUIRED to use a floating NAV?**
(a) government MMFs (b) prime/institutional MMFs (c) tax-exempt retail MMFs (d) all MMFs
**Answer: (b).** Prime/institutional funds hold CP and CDs (credit-sensitive paper) and must float their NAV to reflect true market value. Government MMFs (bills, agencies, government repo) may keep the stable $1.00 NAV.

**D7. Converting a discount instrument to MMY makes it directly comparable to:**
(a) a coupon Treasury bond (b) an add-on CD (c) a common stock (d) an effective annual rate
**Answer: (b).** MMY is the "CD-equivalent yield" — price base, 360-day year, the same basis on which add-on CDs are quoted. BEY (365) is the one comparable to coupon bonds.

**D8. Which is a genuine reason BDY understates the true return?**
(a) it compounds too aggressively (b) it divides interest by price (c) it divides interest by face and uses a 360-day year (d) it uses a 365-day year
**Answer: (c).** BDY divides by face (larger than the price actually paid) and annualizes over 360 days — both flaws push it below the investor's true return.

---

## Self-Verification of Key Calculations

- B1 EAY: ln(1.020408) = 0.0202029; × 4.05556 = 0.081934; e^0.081934 − 1 = 0.08538 → 8.538% ✓
- B4 EAY: ln(1.008827) = 0.0087882; × 6.08333 = 0.053461; e^0.053461 − 1 = 0.054916 → 5.492% ✓
- B6: 91 × 0.04 = 3.64; 360 − 3.64 = 356.36; 14.4/356.36 = 0.040409 ✓; 14.6/356.36 = 0.040969 ✓
- B7: 90 × 0.05 = 4.5; 360 − 4.5 = 355.5; 18/355.5 = 0.050633 ✓ (> 0.0505, so X wins)
- All four-yield tables respect BDY < MMY < BEY < EAY. ✓
