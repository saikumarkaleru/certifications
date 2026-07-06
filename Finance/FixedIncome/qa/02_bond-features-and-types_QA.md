# Q&A — Bond Features and Types

A practice bank for the "Bond Features and Types" chapter. Work each question before reading the answer. Numerical answers are worked step-by-step and reconciled.

---

## Section A — Concept Check

**A1. What are the four independent design axes of any bond, and why is this decomposition useful?**

The four axes are: (1) **Issuer** — who repays, and thus the credit risk (sovereign, supranational, agency, municipal, corporate); (2) **Cash-flow shape** — coupon structure, par value, and maturity, which define the cash-flow numerator; (3) **Embedded options** — rights that let one party alter the contract (call, put, conversion, sinking fund); (4) **Legal position** — covenants, seniority, and security, which govern behaviour and recovery. The decomposition is useful because any real bond is a single point in this four-dimensional space. It lets you price two bonds that both "pay 5%" completely differently once you locate them on each axis, and it maps each feature onto exactly one channel in the pricing equation.

**A2. State the "bond = straight bond ± option" identities and give the yield consequence of each.**

- Callable: $P_{callable} = P_{straight} - V_{call}$ → callable yields **more** (investor is short the call).
- Putable: $P_{putable} = P_{straight} + V_{put}$ → putable yields **less** (investor is long the put).
- Convertible = straight bond + call on the issuer's equity → **lowest** coupon (investor pays for equity upside with foregone income).

The identity gives direction from the sign of the option and magnitude from a lattice model.

**A3. Why does a floating-rate note (FRN) have very short interest-rate duration but still carry credit risk?**

The coupon resets each period to *reference rate + quoted margin*, so as market rates move, the coupon re-prices toward them and the price stays near par. Rate duration is therefore roughly the time to the next reset — very short. But the *quoted margin is fixed* at issue. If the issuer's credit deteriorates, the spread the market now demands (the **discount margin**) rises above the fixed quoted margin, and the FRN's price falls below par. Resetting fixes rate risk, not credit risk.

**A4. Why does a zero-coupon bond have the longest possible duration for its maturity?**

Macaulay duration is the PV-weighted average time to cash flows. A zero has exactly one cash flow, at maturity, so 100% of the weight sits at the final date and $D_{Mac} = N$ (the maturity). Any coupon bond of the same maturity pays some cash earlier, pulling the weighted average below $N$. The zero therefore has maximum price sensitivity to yield changes and no reinvestment risk.

**A5. Distinguish security from seniority. Can a bond be senior and unsecured at the same time?**

**Security** is about collateral — whether specific assets are pledged (mortgage bonds, equipment trust certificates). **Seniority** is about rank in the bankruptcy payment waterfall under the absolute priority rule. They are independent dimensions. Yes: a **senior unsecured** bond ranks high in the waterfall but has no specific collateral — it relies on the issuer's general unpledged assets. Both dimensions independently affect loss given default and therefore spread.

**A6. What is a make-whole call and why is it rarely exercised?**

A make-whole call lets the issuer redeem early at a price equal to the present value of the bond's remaining cash flows, discounted at a *small spread over Treasuries*. Because that discount rate is deliberately low, the call price is high (usually above market), making it uneconomic to exercise. It exists mainly to give the issuer legal flexibility (M&A, restructuring) without penalising holders — unlike a standard call, it does not cap the investor's upside in any meaningful way.

**A7. Distinguish General Obligation (GO) from revenue municipal bonds.**

A **GO bond** is backed by the full taxing power of the issuing government — broad and generally safer. A **revenue bond** is backed only by the cash flows of a specific project (toll road, airport). If the project underperforms, revenue-bond holders have no claim on general tax revenue, so revenue bonds are typically riskier and yield more.

---

## Section B — Numerical Bond-Math Problems

**B1. Price a straight bond and confirm par pricing.** A 3-year annual-pay bond, par 1,000, 6% coupon, yield 6%.

Cash flows: 60 at t=1, 60 at t=2, 1,060 at t=3.

Discount factors at 6%: $1/1.06 = 0.9434$; $1/1.06^2 = 0.8900$; $1/1.06^3 = 0.8396$.

$$P = 60(0.9434) + 60(0.8900) + 1060(0.8396)$$
$$= 56.60 + 53.40 + 890.00 = 1{,}000.00$$

**Reconciliation.** Coupon rate (6%) equals yield (6%), so the bond must price exactly at par (1,000). It does. ✓

**B2. Price the callable and putable versions.** Using B1's straight price, a lattice values $V_{call} = 18$ and $V_{put} = 12$.

$$P_{callable} = 1000 - 18 = 982.00$$
$$P_{putable} = 1000 + 12 = 1012.00$$

**Reconciliation.** Ordering must be $P_{callable} < P_{straight} < P_{putable}$: $982 < 1000 < 1012$. ✓ The callable is cheaper (investor sold the issuer a right, so needs a lower price / higher yield); the putable is dearer (investor bought a right and pays for it / lower yield). Consistent with the identities.

**B3. Zero-coupon price and duration.** A 5-year zero, par 1,000, yield 5% annual.

$$P = \frac{1000}{1.05^5} = \frac{1000}{1.276282} = 783.53$$

Macaulay duration: single cash flow at t=5, weight 1.0, so $D_{Mac} = 5 \times 1.0 = 5.0$ years.

Modified duration: $D_{Mod} = \dfrac{D_{Mac}}{1+y} = \dfrac{5}{1.05} = 4.762$ years.

Estimated price change for a +1% (100 bp) yield rise: $\approx -D_{Mod} \times \Delta y = -4.762 \times 0.01 = -4.76\%$, i.e. price falls to roughly $783.53 \times (1 - 0.0476) = 746.24$.

**Reconciliation.** A 5-year 5% *coupon* bond would have $D_{Mac} \approx 4.5$ years (some cash arrives at years 1–4), so the zero's 5.0 is strictly larger — confirming a zero maximises duration for its maturity. ✓

**B4. Taxable-equivalent yield.** Investor in the 35% bracket. Muni GO yields 3.8% (tax-exempt); comparable corporate yields 5.6% (taxable). Which wins after tax?

$$\text{TEY}_{muni} = \frac{0.038}{1 - 0.35} = \frac{0.038}{0.65} = 5.846\% \approx 5.85\%$$

Since 5.85% > 5.6%, the muni wins.

**Cross-check from the other side** (tax the corporate): after-tax corporate = $5.6\% \times (1 - 0.35) = 3.64\%$, which is below the muni's tax-free 3.8%. Same conclusion. ✓

**Sensitivity.** At a 12% bracket: $\text{TEY} = 0.038 / 0.88 = 4.32\%$, now below 5.6% — the corporate wins. The tax feature only has value relative to the holder's bracket.

**B5. Seniority waterfall / recovery.** A firm defaults with 1,000 of assets. Stack: senior secured 400, senior unsecured 500, subordinated 400 (total owed 1,300). Apply absolute priority.

- Senior secured: paid 400 in full → recovery 100%. Remaining assets: $1000 - 400 = 600$.
- Senior unsecured: paid 500 in full → recovery 100%. Remaining: $600 - 500 = 100$.
- Subordinated: receives residual 100 on 400 owed → recovery $100/400 = 25\%$.

**Reconciliation.** Total paid = $400 + 500 + 100 = 1000$ = assets available. ✓ Total shortfall = $1300 - 1000 = 300$, borne entirely by the subordinated class (LGD 75%), while senior classes have LGD 0%. This is precisely why the subordinated bond of the *same issuer* must price at a wider spread: identical PD, higher LGD.

**B6. Convertible bond arithmetic.** Par 1,000; conversion ratio 25 shares/bond; current share price 32; bond trades at 1,050. Find conversion price, conversion value (parity), market conversion price, and conversion premium.

- Conversion price = Par / ratio = $1000 / 25 = 40.00$ per share.
- Conversion value (parity) = ratio × share price = $25 \times 32 = 800$.
- Market conversion price = bond price / ratio = $1050 / 25 = 42.00$ per share.
- Conversion premium (per share) = $42.00 - 32.00 = 10.00$, i.e. $10/32 = 31.25\%$ over the current share price.

**Reconciliation.** The bond (1,050) trades above parity (800) by 250 — the value of the embedded equity call plus the bond floor above parity. Converting now would yield only 800 of stock versus a 1,050 bond, so a rational holder would **not** convert yet; they hold for the coupon and the option. ✓ Conversion price (40) > current price (32), so the option is out-of-the-money on parity but still valuable for time and volatility.

**B7. Perpetual bond price.** A perpetual (consol) pays 45 per year; required yield 6%.

$$P = \frac{\text{Coupon}}{y} = \frac{45}{0.06} = 750.00$$

**Reconciliation.** If yield rose to 7.5% (equal to the coupon rate on par 600? — check against par-neutral): at $y = c$ on par we'd get $P = 45/0.075 = 600$. So the perpetual prices at par only when yield equals the coupon rate on face; here 45/750 = 6% coupon-on-price, consistent. ✓

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Why does a callable bond yield more than an otherwise identical straight bond?"**

Model answer: The investor in a callable bond is *short* a call option — the issuer holds the right to redeem early. The issuer exercises when rates have fallen and it can refinance more cheaply, which is exactly when the investor would least want to lose a high-coupon bond and would have to reinvest at lower rates. Because the investor gives up this valuable right, they must be compensated with a higher yield. Formally $P_{callable} = P_{straight} - V_{call}$: a lower price means a higher yield. The call also caps upside, producing negative convexity — as yields fall, the callable's price flattens toward the call price rather than rising freely.

**C2. "An FRN is trading at 97, below par. What does that tell you?"**

Model answer: An FRN's price stays near par because its coupon resets to reference + a fixed quoted margin. A price below par signals that the market now demands a *higher* spread than the fixed quoted margin — i.e. the **discount margin has risen above the quoted margin**, almost always because the issuer's credit has deteriorated (or liquidity has worsened). It is not an interest-rate story: rate duration is near zero. So a 97 price is a credit-risk warning, and I'd look at the issuer's spread, ratings trajectory, and the size of the gap between discount margin and quoted margin.

**C3. "Same issuer, same maturity: senior secured vs subordinated. Which yields more and why — walk me through it."**

Model answer: Both share the *same probability of default* because it's the same company and the same default event triggers both. What differs is **loss given default**. The senior secured bond has first claim on pledged collateral and sits at the top of the priority waterfall, so its recovery is high (low LGD). The subordinated bond is paid only after all senior claims are made whole, so it absorbs the shortfall and has high LGD. Since expected loss $\approx$ PD × LGD and PD is common, the subordinated bond has higher expected loss, hence a wider spread and higher yield. This is why one issuer can have a whole capital stack trading at different spreads.

**C4. "Why do convertible bonds carry the lowest coupons?"**

Model answer: A convertible is a hybrid — a straight bond plus a call option on the issuer's equity. The equity conversion right is valuable: it gives the holder unlimited upside if the stock rises while the bond floor limits downside. Investors pay for that upside by accepting a lower coupon than they'd demand on a plain bond from the same issuer. So the low coupon is not a sign of low risk; it's the price of the embedded equity option. In distress, the option can be worthless and the holder is left with a low-coupon bond — that's the trade-off.

**C5. "Which single covenant matters most to a bondholder, and why?"**

Model answer: I'd point to two working together, but if forced to one, the **negative pledge**. It bars the issuer from pledging assets to *other* lenders without equally securing existing bondholders — protecting your claim rank and recovery. Close behind are **leverage / interest-coverage limits**, which cap how much additional debt the issuer can pile on and thus constrain the probability of default. Negative pledge protects LGD; leverage limits protect PD. Together they defend both terms of expected loss, which is why they compress the spread. Covenant-lite deals strip these and compensate with wider spreads.

**C6. "How would you quote the yield on a callable bond?"**

Model answer: On **yield-to-worst** — the lowest of the yield-to-maturity and every yield-to-call across the call schedule. Because the issuer will call when it's advantageous to them and disadvantageous to the investor, the conservative assumption is the scenario that gives the investor the worst outcome. Quoting YTM alone would overstate the return an investor can rely on.

---

## Section D — Multiple Choice (with reasoning)

**D1. All else equal, which bond has the *highest* yield?**
A. Putable  B. Straight  C. Callable  D. Convertible

**Answer: C (Callable).** The yield ordering is putable < straight < callable, because the callable investor is short an option and must be compensated. The convertible (D) actually has the *lowest* coupon of all, since the equity option is paid for with foregone income. A and B are lower than C by the identities.

**D2. A 6-year zero and a 6-year 6% coupon bond, same yield. Which statement is true?**
A. The coupon bond has higher duration.  B. Both have duration 6.  C. The zero has duration 6; the coupon bond less.  D. Duration is unrelated to coupon.

**Answer: C.** A zero's Macaulay duration equals its maturity (6), because all cash is at the end. The coupon bond pays earlier cash flows, pulling its PV-weighted average time below 6. So the zero has the higher, and maximum-for-maturity, duration. A and D are wrong; B ignores the coupon effect.

**D3. An FRN's price falls from 100 to 96 while the reference rate is unchanged. The most likely cause is:**
A. Rising market interest rates  B. Widening issuer credit spread  C. An approaching reset date  D. A coupon step-down

**Answer: B.** With the reference rate unchanged, rate risk is not the driver, and an FRN's rate duration is near zero anyway. A price drop below par means the required discount margin now exceeds the fixed quoted margin — a credit-spread widening. A is largely neutralised by resets; C would push price *toward* par; D is not a standard FRN feature.

**D4. A firm defaults; assets 800. Senior secured owed 300, senior unsecured owed 400, subordinated owed 300. Subordinated recovery rate is:**
A. 0%  B. 33%  C. 50%  D. 100%

**Answer: B (33%).** Pay top-down: secured 300 (full), leaving 500; senior unsecured 400 (full), leaving 100; subordinated gets 100 on 300 owed = 33.3%. Reconciliation: 300 + 400 + 100 = 800 = assets. ✓ The junior class absorbs the whole shortfall of 200.

**D5. An investor in the 40% tax bracket compares a 3% tax-exempt muni with a 4.8% taxable corporate. Which is better after tax?**
A. Corporate  B. Muni  C. Equal  D. Cannot tell

**Answer: B (Muni).** TEY = $0.03 / (1 - 0.40) = 0.03 / 0.60 = 5.0\%$, which exceeds the corporate's 4.8%. Cross-check: after-tax corporate = $4.8\% \times 0.60 = 2.88\%$ < muni 3.0%. Both methods agree the muni wins for this high-bracket investor.

**D6. Which pairing correctly matches feature to convexity?**
A. Callable → positive convexity  B. Putable → negative convexity  C. Callable → negative convexity  D. Zero → negative convexity

**Answer: C.** A callable exhibits negative convexity because the call caps price appreciation as yields fall (price compresses toward the call price). A putable has positive convexity (the put floors the downside). A zero has ordinary positive convexity. A, B, and D are reversed or wrong.

**D7. A make-whole call is rarely exercised because:**
A. It is illegal in most indentures  B. Its call price is set at PV of remaining cash flows at a tiny spread over Treasuries, making it expensive  C. It requires bondholder consent  D. It only applies to floating-rate notes

**Answer: B.** The make-whole price discounts remaining cash flows at a small spread over Treasuries, producing a high (usually above-market) redemption price, so it is uneconomic to exercise. It exists for issuer flexibility, not routine refinancing. The other options are fabricated constraints.

**D8. "Senior unsecured" means the bond is:**
A. Backed by specific collateral and top of the waterfall  B. High in the priority waterfall but with no specific collateral  C. Subordinated but collateralized  D. Equivalent to preferred equity

**Answer: B.** Seniority (waterfall rank) and security (collateral) are independent. Senior unsecured ranks high but pledges no specific assets — it relies on the issuer's general unpledged assets for recovery. A describes senior secured; D is far lower in the stack.

---

*End of Q&A bank. Every numerical answer above has been reconciled against the chapter identities: $P_{callable} < P_{straight} < P_{putable}$, zero duration = maturity, TEY = $y_{muni}/(1-\text{tax})$, and absolute-priority recovery summing to available assets.*
