# Q&A — Introduction to Fixed Income

A practice bank for Chapter 01. Every question is followed by a full answer. Work each one before reading the answer.

---

## Section A — Concept Checks

**A1. In one sentence, what is a fixed-income security?**

A fixed-income security is a tradable loan with a contractually defined repayment schedule — the issuer receives cash today and promises periodic interest payments (coupons) plus repayment of principal (face value) at a stated maturity date.

**A2. Why does fixed income exist at all? What economic need does it meet?**

Savers hold surplus money but have no direct use for it; borrowers (governments, companies, households) have uses but no cash. Fixed income is the mechanism to move purchasing power from savers to borrowers across time, in a way that (1) compensates the saver for the time value of money, (2) compensates for the risk of non-repayment, and (3) is standardised and tradable so the saver is not locked in and a large need can be split among many lenders.

**A3. Why would a company issue a bond instead of equity?**

Debt lets the company borrow, pay a defined cost, and be done — without giving away ownership, control, or an unlimited share of future profits. Debt is also cheaper (interest is tax-deductible and lenders demand less return than shareholders because they bear less risk) and non-dilutive.

**A4. State the single master equation of fixed income in words.**

A bond's price today equals the present value of its future cash flows, discounted at a rate that reflects time and risk: $P = \sum_{t=1}^{N} C_t /(1+y)^t$. Everything else in the subject is an elaboration of this one equation.

**A5. Why do bond prices and yields move in opposite directions?**

Because it is arithmetic, not convention. The cash flows are fixed. A fixed stream discounted at a higher rate has a smaller present value. So the instant the market demands a higher yield, the fixed stream is worth less, and the price falls. Raise $y$, and $P$ falls, always.

**A6. What are the layers that build up the discount rate (yield)?**

$y$ = real risk-free rate + expected inflation + credit (default) risk premium + liquidity premium + term/maturity premium. A government bond in its own currency carries essentially the first two plus a term premium; a small-company bond carries all five.

**A7. Define the credit spread.**

The credit spread is the difference in yield between a risky bond and a government bond of the same maturity. It is the market's price of that particular borrower's default risk.

**A8. Distinguish coupon rate from yield to maturity.**

The coupon rate is fixed forever at issuance and is measured on face value. The yield to maturity floats with the market and is measured on the current price. They coincide only when the bond trades exactly at par.

**A9. Name the three headline risks of holding a bond and the metric that measures or prices each.**

Interest-rate risk (measured by duration), credit/default risk (priced by the credit spread and summarised by ratings), and liquidity risk (priced as a liquidity premium in yield).

**A10. Why is fixed income the largest asset class on earth?**

Three structural reasons: (1) governments can only tax or borrow — they cannot issue equity — so all government financing is fixed income; (2) companies finance heavily with cheap, non-dilutive debt on the margin; (3) each borrower has one equity but issues many bonds over time, multiplying the number of instruments. Global bonds outstanding are roughly US$130 trillion-plus, larger than global equity market capitalisation.

---

## Section B — Numerical Bond-Math Problems

**B1. Price a 3-year bond, face ₹1,000, annual coupon 8% (₹80/yr), at a market yield of 8%.**

Cash flows: ₹80 at t=1, ₹80 at t=2, ₹1,080 at t=3 (final coupon plus face).

- $80 / 1.08 = 74.074$
- $80 / 1.08^2 = 80 / 1.1664 = 68.587$
- $1{,}080 / 1.08^3 = 1{,}080 / 1.259712 = 857.339$
- Sum $= 74.074 + 68.587 + 857.339 = ₹1{,}000.00$

The bond prices at par. Reconciliation: coupon rate (8%) equals yield (8%), so by the par regime we expect $P = F$, and the arithmetic confirms exactly ₹1,000.00.

**B2. Reprice the same bond at a yield of 10%. Which regime, and by how much did the price change?**

- $80 / 1.10 = 72.727$
- $80 / 1.21 = 66.116$
- $1{,}080 / 1.331 = 811.420$
- Sum $= ₹950.26$

The bond trades at a discount ($P < F$) because yield (10%) now exceeds coupon (8%). Price fell from ₹1,000.00 to ₹950.26, a drop of ₹49.74 (−4.97%) for a +2% yield move.

**B3. Reprice the same bond at a yield of 6%. Which regime?**

- $80 / 1.06 = 75.472$
- $80 / 1.1236 = 71.199$
- $1{,}080 / 1.191016 = 906.956$
- Sum $= ₹1{,}053.63$

The bond trades at a premium ($P > F$) because yield (6%) is below coupon (8%). Reconciliation across B1–B3: the three prices ₹1,053.63 (6%), ₹1,000.00 (8%), ₹950.26 (10%) fall in strictly decreasing order as yield rises — confirming the inverse price–yield relationship and all three regimes from one bond.

**B4. Compute the current yield of the discount bond in B2 (price ₹950.26, coupon ₹80).**

$$\text{Current Yield} = \frac{\text{Annual coupon}}{\text{Price}} = \frac{80}{950.26} = 8.42\%$$

**B5. The bond in B4 has a YTM of 10%. Explain the ordering of current yield (8.42%) versus YTM (10%).**

For a discount bond, current yield < YTM. The buyer of a discount bond earns two things: the coupon income and a capital gain as the price pulls up to par (₹1,000) at maturity. Current yield captures only the coupon income and ignores the capital gain and time value; YTM captures both. Hence YTM (10%) exceeds current yield (8.42%). The ordering reverses for a premium bond (current yield > YTM), and for a par bond coupon = current yield = YTM.

**B6. Find the YTM of the ₹950.26 discount bond by iteration and linear interpolation, pretending you do not already know it.**

Try bracketing yields and pricing:

- At $y = 8\%$: price = ₹1,000.00 (too high; we need the lower price ₹950.26, so raise the yield).
- At $y = 12\%$: $80/1.12 = 71.43$; $80/1.2544 = 63.78$; $1{,}080/1.404928 = 768.72$; sum = ₹903.93 (too low; overshot).

Target ₹950.26 lies between the 8% price (₹1,000.00) and the 12% price (₹903.93). Interpolate:

$$y \approx 8\% + \frac{1{,}000 - 950.26}{1{,}000 - 903.93} \times (12\% - 8\%) = 8\% + \frac{49.74}{96.07} \times 4\% = 8\% + 2.07\% = 10.07\%$$

Interpolation gives 10.07%, very close to the true 10%. The small overshoot arises because price is convex (curved), not linear, in yield — the seed of the convexity concept.

**B7. Estimate the price of the par bond (B1) if yields rise 100 bps to 9%. Do it by exact repricing.**

- $80 / 1.09 = 73.394$
- $80 / 1.1881 = 67.335$
- $1{,}080 / 1.295029 = 833.958$
- Sum $= ₹974.69$

Price fell from ₹1,000.00 to ₹974.69, a change of −₹25.31, or −2.531% for a +1% yield move.

**B8. Compute Macaulay and modified duration for the par bond at 8%, then predict the B7 price move and reconcile.**

Using the PVs from B1:

| $t$ | $C_t$ | $PV = C_t/1.08^t$ | $t \times PV$ |
|---|---|---|---|
| 1 | 80 | 74.074 | 74.074 |
| 2 | 80 | 68.587 | 137.174 |
| 3 | 1,080 | 857.339 | 2,572.017 |
| | | **1,000.00** | **2,783.265** |

$$D_{\text{Mac}} = \frac{2{,}783.265}{1{,}000} = 2.783 \text{ years}, \qquad D_{\text{Mod}} = \frac{2.783}{1.08} = 2.577$$

Predicted change for +1% yield: $\Delta P / P \approx -D_{\text{Mod}} \times \Delta y = -2.577 \times 1\% = -2.577\%$.

Reconciliation: duration predicts −2.577%; exact repricing (B7) gave −2.531%. They agree to within 0.05%. Duration slightly overstates the fall because the true price–yield curve is convex; that curvature gap is exactly what convexity corrects. Duration is a first-order (straight-line) estimate; convexity is the second-order correction.

**B9. A zero-coupon bond, face ₹1,000, matures in 3 years and is priced to yield 8%. What is its price and its Macaulay duration?**

A zero pays nothing until maturity, so the only cash flow is ₹1,000 at t=3.

$$P = \frac{1{,}000}{1.08^3} = \frac{1{,}000}{1.259712} = ₹793.83$$

Macaulay duration of a zero equals its maturity, because all present value sits at the single final date: $D_{\text{Mac}} = 3.0$ years. Note this exceeds the 2.783-year duration of the 8% coupon bond of the same maturity — lower (here zero) coupon means longer duration and greater interest-rate sensitivity.

**B10. A 30-year zero yields 5%, then yields spike to 6.5% (+150 bps). Roughly why can it lose about a third of its value with zero default?**

Price at 5%: $1{,}000/1.05^{30} = 1{,}000/4.3219 = ₹231.38$. Price at 6.5%: $1{,}000/1.065^{30} = 1{,}000/6.6144 = ₹151.19$. Change $= (151.19 - 231.38)/231.38 = -34.7\%$. A long-dated zero has a duration near 30 years, so a 1.5% yield move produces roughly $-30 \times 1.5\% \approx -45\%$ on a first-order basis, moderated by convexity to about −35% in exact terms. This illustrates that a default-free government bond can still carry enormous interest-rate risk.

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Give me a two-sentence definition of fixed income to open your answer."**

Model answer: "Fixed income is a tradable loan with a contractually fixed cash-flow schedule — periodic coupons plus principal at maturity. Its price is the present value of those cash flows at the market yield, which is why price and yield move inversely."

**C2. "A bond's coupon is 8% but you say its yield is 10%. Is the bond trading above or below par, and why?"**

Model answer: "Below par — at a discount. The coupon of 8% is fixed and pays less than the 10% the market now demands. To make the fixed stream competitive with a 10% required return, the price must fall below face value so the buyer picks up the shortfall as a capital gain to par. Concretely, an 8% three-year bond at a 10% yield prices around ₹950 against ₹1,000 face."

**C3. "Interest rates just rose. A client says, 'Good — my bonds now pay more, so I made money.' Correct them."**

Model answer: "Two things are being confused. New bonds issued now pay more, but the client's existing bond has a fixed coupon that did not change. When market yields rose, the present value of that fixed stream fell, so the existing bond's price dropped — the client took a mark-to-market capital loss. Rising yields are bad news for existing bondholders even though the market is 'paying more.' The client only benefits from higher rates on money reinvested at the new, higher yields."

**C4. "Why is a long-dated government bond not 'safe'?"**

Model answer: "Safe from default, not safe from price movement. A government borrowing in its own currency has minimal credit risk, but it has substantial interest-rate risk. Because price is the present value of cash flows, a long maturity means a high duration, and a rate spike drives the price down sharply. A 30-year zero can lose a third of its value on a 1.5% yield jump with zero chance of default. 'Government bond' answers the credit question, not the interest-rate question."

**C5. "Walk me through why a bond's market price equals the present value of its cash flows — what enforces that?"**

Model answer: "No-arbitrage. If a bond's cash flows are worth ₹98 in present-value terms but it trades at ₹95, buyers rush in to capture the ₹3 and bid the price up to ₹98. If it trades at ₹101, holders sell and the price falls to ₹98. Rational buyers won't overpay and rational sellers won't undersell, so the market price settles at the present value of the cash flows discounted at the market's required yield. The price is the PV — enforced by arbitrage."

**C6. "For a discount bond, is current yield above or below YTM? Explain the intuition."**

Model answer: "Below. A discount bond returns the coupon plus a capital gain as its price pulls up to par by maturity. Current yield is just coupon over price — it ignores that capital gain and the time value of money. YTM includes it. So YTM exceeds current yield for a discount bond. For a premium bond the ordering flips, because the premium erodes to par, imposing a capital loss that pulls YTM below the current yield. At par all three — coupon rate, current yield, YTM — are equal."

**C7. "What does a modified duration of 2.6 actually tell a portfolio manager?"**

Model answer: "It's a sensitivity: a 1% (100 bps) rise in yield costs roughly 2.6% of the bond's price, and a 1% fall gains roughly 2.6%, from $\Delta P/P \approx -D_{\text{Mod}} \times \Delta y$. It lets the manager translate a rate view into a price impact and size positions to a target risk. But it's a first-order, straight-line estimate; for large yield moves the manager adds a convexity correction because the true price–yield relationship curves."

---

## Section D — Multiple Choice Questions (with reasoning)

**D1. A bond trades at a premium. Which must be true?**

A. Coupon rate < yield  B. Coupon rate = yield  C. Coupon rate > yield  D. Maturity is long

Answer: **C.** A premium ($P > F$) arises precisely when the coupon exceeds the required yield, so the bond pays more than the market demands and is worth more than face. A and B give discount and par respectively; D is irrelevant to the regime.

**D2. Market yields fall by 50 bps. An existing fixed-coupon bond's price will:**

A. Fall  B. Rise  C. Stay unchanged  D. Depend on the coupon direction

Answer: **B.** Price and yield move inversely. Discounting the fixed cash flows at a lower rate raises their present value, so the price rises. The coupon is fixed and does not change direction.

**D3. Which risk affects even a default-free government bond?**

A. Credit risk  B. Interest-rate risk  C. Liquidity risk only  D. None

Answer: **B.** Interest-rate risk flows straight from the pricing equation and hits every bond regardless of creditworthiness — raise the yield and the price falls. A government bond in its own currency has negligible credit risk but full interest-rate risk.

**D4. The credit spread is best described as:**

A. Coupon minus yield  B. A risky bond's yield minus a same-maturity government bond's yield  C. Current yield minus YTM  D. Yield minus inflation

Answer: **B.** The credit spread is the extra yield a risky borrower must offer over a government bond of equal maturity — the market's price of that borrower's default risk.

**D5. For a par bond, which relationship holds?**

A. Coupon rate = current yield = YTM  B. Current yield > YTM  C. YTM > coupon rate  D. Price > face value

Answer: **A.** At par there is no capital gain or loss to maturity, so coupon rate, current yield, and YTM all coincide.

**D6. Two 3-year bonds have the same yield; Bond X has an 8% coupon, Bond Z is a zero. Which has the greater interest-rate sensitivity (duration)?**

A. Bond X  B. Bond Z  C. Equal  D. Cannot tell

Answer: **B.** A zero's Macaulay duration equals its maturity (3.0 years) because all its present value sits at the final date, whereas the coupon bond's duration is shorter (about 2.78 years) because early coupons pull weight forward. Lower coupon means longer duration and greater sensitivity.

**D7. Which correctly orders the layers of a yield?**

A. Real rate + inflation + credit + liquidity + term premium  B. Coupon + inflation  C. YTM − current yield  D. Face value × coupon

Answer: **A.** The discount rate is built up as the real risk-free rate plus inflation compensation plus credit, liquidity, and term premia. A government bond carries mainly the first two plus a term premium; a risky corporate carries all five.

**D8. "Fixed income means a fixed return." This statement is:**

A. True always  B. True only for zeros  C. False — cash flows are fixed, but return depends on price paid and whether held to maturity  D. True only for government bonds

Answer: **C.** For a plain bond the cash flows are fixed, but the realised return depends on the purchase price and on selling before maturity (yields may have risen, imposing a capital loss) and on reinvestment rates. Fixed cash flows are not a fixed return.

---

*End of Q&A — Chapter 01: Introduction to Fixed Income.*
