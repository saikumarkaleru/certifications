# Q&A — Bond and Debt Markets

A companion practice bank for Chapter 07. Every question is followed by a full answer. Work each one before reading the answer; the goal is understanding, not recognition.

---

## Section A — Concept-Check Questions

**A1. In one sentence, what is a bond, and what makes it different from an ordinary bank loan?**

A bond is a **tradable, standardised IOU**: the issuer borrows a fixed principal and legally promises fixed periodic interest plus repayment of principal on a fixed date. It differs from a bank loan in that it is **sliced into thousands of identical, fungible units** that can be sold to a crowd of lenders and re-sold among them in a secondary market — so one giant, long-dated loan is funded by many small lenders rather than a single bank.

**A2. State the "iron law of bonds" and explain in one line why it holds.**

**Price and yield move in opposite directions.** It holds because the coupon is fixed forever, so when market rates rise the only way an old, lower-coupon bond can still offer a competitive return is for its **price to fall** until its yield matches the new market rate — and vice versa when rates fall.

**A3. Distinguish coupon, current yield, and yield to maturity. When are all three equal?**

**Coupon** is the fixed interest as a percentage of *face value*, unchanging for life. **Current yield** is annual coupon ÷ *current market price* — a rough snapshot. **YTM** is the single discount rate that equates the bond's price to the present value of all future coupons plus principal — the true "return if held to maturity." All three are equal only when the bond trades **exactly at par** (price = face value).

**A4. What is duration, and why does a longer-maturity bond carry more interest-rate risk?**

Duration is the approximate **percentage change in a bond's price for a 1% change in yield** — a measure of price sensitivity. A longer-maturity bond has more distant cash flows whose present values are more affected by discounting, giving it a **higher duration** and hence larger price swings for the same yield move. A duration-7 bond loses roughly 7% if yields rise 1%.

**A5. Why is a G-sec called "risk-free," and does that mean it carries no risk at all?**

A rupee G-sec is called risk-free because the sovereign can **tax and ultimately print rupees**, so its *default* (credit) risk in rupee terms is effectively zero. It does **not** mean zero risk: a G-sec still carries **interest-rate risk** (price falls when rates rise), **inflation risk** (fixed coupons lose real value), and, if sold early, **price risk**. "Risk-free" refers only to sovereign default risk.

**A6. How does a T-bill generate a return if it pays no coupon?**

A T-bill is a **zero-coupon** instrument sold at a **discount** to face value and redeemed at face value. The investor's return is the gap: buy at ₹97.20, receive ₹100 in 182 days — the ₹2.80 is the income. There are no periodic interest payments.

**A7. What is a credit spread, and what does a widening spread signal?**

A credit spread is the **extra yield a corporate (or riskier) bond offers over a G-sec of the same maturity** — the market's real-time price of default risk. A **widening** spread signals rising perceived default risk or stress: investors are demanding more compensation to hold corporate credit, often a warning of deteriorating credit conditions.

**A8. Which regulator oversees which segment of the Indian debt market?**

The **RBI** governs the government-securities and money markets and runs the sovereign borrowing calendar; **SEBI** regulates the corporate bond market, listing, disclosure, and credit-rating agencies. (US analogue: the Treasury/Fed handle Treasuries, the SEC regulates corporate bonds.)

**A9. What does a debenture trustee do, and why is it necessary?**

A debenture trustee is a **SEBI-registered entity that holds security on behalf of, and enforces rights for, a dispersed body of bondholders**. It is necessary because thousands of scattered NCD holders cannot individually monitor covenants or enforce claims against the issuer; the trustee acts collectively for them, especially in default.

**A10. Callable vs puttable bond — who holds the option, and how does each affect yield?**

A **callable** bond gives the *issuer* the right to redeem early (valuable to the issuer if rates fall), so the investor demands a **higher yield** as compensation. A **puttable** bond gives the *holder* the right to force early redemption (valuable to the investor), so the investor accepts a **lower yield**. The option always favours whoever holds it, and the yield adjusts to price that advantage.

---

## Section B — Applied / Scenario Questions

**B1. You bought the 7.18% GS 2033 at par (₹100). Two years later, comparable yields have risen to 7.70%. The bond's duration is about 6. Estimate the new price and explain what you have and haven't lost.**

Price change ≈ −duration × yield change = −6 × (7.70% − 7.18%) = −6 × 0.52% ≈ **−3.1%**, so the price falls to about **₹96.9**. If you **sell now**, you crystallise a ~3% capital loss. If you **hold to maturity**, you still receive every ₹3.59 coupon and ₹100 back — you have lost nothing in cash terms; you simply earned a rate below what the market now offers. This is why hold-to-maturity investors (LIC, EPFO) fret less about rate moves than mark-to-market debt funds.

**B2. The RBI auctions a 182-day T-bill at ₹97.20 per ₹100 face. Compute the annualised return.**

Period return = (100 − 97.20)/97.20 = 2.80/97.20 = **2.88%** over 182 days.
Annualised ≈ 2.88% × (365/182) ≈ **5.78% p.a.**
This becomes a benchmark short-term risk-free rate that treasuries and money-market funds price against.

**B3. Reliance can raise USD 1 billion for 10 years either via a syndicated bank loan at SOFR + 1.5% or by issuing 10-year bonds to global funds at a fixed 3.7%. Beyond the headline rate, give three reasons a strong issuer prefers the bond route.**

(1) **Fixed long-term certainty** — the bond locks a known 3.7% for a decade, whereas the floating loan re-prices with SOFR. (2) **A far larger lender pool** — global insurers, pension and sovereign funds dwarf any single bank syndicate, deepening demand and lowering cost. (3) **Lighter covenants** — bond documentation is typically less restrictive than a bank loan's. This is **disintermediation**: going around banks straight to savers, which lowers the whole economy's cost of capital.

**B4. IL&FS carried AAA ratings on much of its debt, then collapsed from AAA to D within weeks in 2018. Trace how a single issuer's default froze funding for an entire sector.**

IL&FS funded long-dated infrastructure assets by constantly **rolling over short-term commercial paper**. When it began defaulting, agencies slashed its paper nine notches to D, and **debt mutual funds holding it had to write it down to near zero**, hammering NAVs. Investors then distrusted *every* NBFC's short-term paper, so spreads on all NBFC debt blew out and the CP market for the sector **froze** — solvent NBFCs suddenly could not refinance. The lesson: ratings can lag reality, prices reflect *perceived* risk, and one high-profile default can reprice an entire market segment.

**B5. A treasurer compares a 7-year AAA corporate NCD yielding 8.1% with a 7-year G-sec yielding 7.3%. What is the 0.8% gap called, and what should drive the decision?**

The 0.8% (80 bps) gap is the **credit spread** — compensation for the corporate's default and liquidity risk over the risk-free sovereign. The decision should turn on mandate and view: if the book must be pristine and highly liquid, the G-sec's safety and superior tradability justify giving up 80 bps; if the mandate permits measured AAA credit risk for extra return, the NCD is defensible — but with attention to issuer concentration, security terms, and the fact that corporate bonds are far **less liquid** and often held to maturity.

**B6. A mid-sized company issues a "secured NCD" rated AA and a bank issues an AT1 perpetual bond rated AA. Both say "AA." Why might the AT1 be far riskier?**

An AT1 (Additional Tier-1) perpetual has **no fixed maturity**, its coupons can be **skipped**, and — critically — its principal can be **written down to zero** if the bank breaches capital thresholds, as happened to **YES Bank's AT1 bonds in 2020**. A secured NCD ranks as a creditor with specific security and a defined redemption. Despite the identical letter grade, the AT1's loss-absorbing, equity-like features make it structurally far riskier — a reminder to read the **security and structure**, not just the rating symbol.

**B7. During the 2020 Franklin Templeton episode, six debt funds were frozen even though many underlying bonds had not defaulted. Which risk does this illustrate, and how does it differ from credit risk?**

It illustrates **liquidity risk** — the risk that a bond **cannot be sold at a fair price when you need to**, regardless of whether the issuer is still paying. Franklin's funds held low-rated, thinly traded corporate paper; when redemptions surged, there were no buyers, so the funds had to gate. Credit risk is about the borrower *defaulting*; liquidity risk is about the *market* disappearing. India's shallow corporate-bond secondary market makes this a live, structural concern.

---

## Section C — Interview-Style Questions

**C1. "Explain to me why bond prices and yields move in opposite directions."**

Because a bond's coupon is fixed for its entire life. Suppose you hold a bond paying a fixed 7% while new bonds of similar risk start paying 8% — no one will pay full price for your lower-paying bond, so its **price falls** until a buyer purchasing at that lower price earns an effective return, or yield, of 8%. Conversely, if new bonds pay only 6%, your 7% bond looks generous and its **price rises** to a premium until its yield drops to 6%. The price is simply whatever level makes the fixed cash flows deliver the return the market currently demands — so price and yield are two ends of the same see-saw. This inverse relationship, magnified by duration for longer bonds, is the single most important idea in fixed income.

**C2. "What's the difference between a G-sec, a T-bill, and an SDL?"**

All three are sovereign-backed rupee instruments, but they differ on issuer and tenor. A **G-sec** (dated security) is medium-to-long-term central-government borrowing — 2 to 40 years — that pays a coupon, and its yield curve is the risk-free benchmark for the whole economy. A **T-bill** is *short-term* central-government paper — 91, 182, or 364 days — issued at a discount with *no coupon*; it anchors the short end of the curve. An **SDL (State Development Loan)** is issued by a *state* government to fund its deficit; it is legally sovereign-backed but yields roughly **30–60 bps more** than central G-secs because states are marginally less liquid and carry a whisper of extra risk. So: central long (G-sec), central short zero-coupon (T-bill), state (SDL).

**C3. "How do bond markets transmit monetary policy into the rest of the economy?"**

The G-sec yield curve *is* the risk-free curve, so it sits underneath every other rupee rate. When the RBI changes the repo rate, the short end of the curve re-prices first, and the move ripples out along the whole curve — repricing every G-sec, and through the credit spread, every corporate bond and bank loan too. Because the risk-free rate is the anchor in every DCF and cost-of-capital calculation, rising yields also mechanically **lower equity valuations**. Banks feel it directly because they must hold G-secs for SLR, so their treasuries gain or lose as bond prices move. In short, the bond market is the **transmission belt**: policy rates set at one end, and the cost of capital for households, firms, and the government adjusts at the other.

**C4. "Why do issuers so often prefer debt over equity for large, routine funding?"**

Three reasons. First, **tax**: interest is a deductible expense, whereas dividends are paid out of after-tax profit — so debt is cheaper on an after-tax basis. Second, **no dilution**: bondholders are creditors, not owners, so issuing debt doesn't hand voting control or a share of future profits to outsiders. Third, **scale and cost**: deep bond markets let an issuer tap a vast global pool of lenders at a fixed long-term rate, often below a bank loan, with lighter covenants. The trade-off is that debt is a **fixed obligation** — it must be serviced in bad years as well as good, and too much of it raises bankruptcy risk. But for a creditworthy borrower funding routine, large, long-dated needs, debt is the natural first choice.

**C5. "A bond is rated AAA. How much comfort should that give you?"**

A rating is a **third-party opinion on default risk, not a guarantee** — and it has three well-known limitations. It can be **late**: IL&FS was rated AAA days before it began defaulting in 2018. It reflects a **conflict of interest**, because the agency is paid by the issuer it rates. And it says nothing about the *other* risks a bond carries — interest-rate, liquidity, or the loss-absorbing features of instruments like AT1 perpetuals. So AAA is a useful **input** that narrows the field to high-quality credits, but it is not a verdict. I'd still read the security terms, the issuer's cash flows and refinancing profile, and the market's own signal — the credit spread — before taking comfort.

**C6. "Give me the one-sentence framing of what a bond market is."**

A bond market is society's machine for **channelling savings into long-lived investment while continuously pricing the two great risks of lending — time and default.**

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Market yields on comparable bonds rise from 7% to 8%. An existing fixed-coupon bond will:**
(a) Rise in price (b) Fall in price (c) Stay at par (d) Convert to equity

**Answer: (b) Fall in price.** By the iron law, price and yield move inversely. The old bond's fixed coupon now looks cheap, so its price must fall to a discount until its yield rises to match the new 8% market rate.

**D2. A 91-day T-bill is bought at ₹98.30 (face ₹100). Its approximate annualised return (365-day basis) is closest to:**
(a) 5.6% (b) 6.5% (c) 7.0% (d) 8.2%

**Answer: (c) 7.0%.** Period return = 1.70/98.30 = 1.729%. Annualised = 1.729% × (365/91) = 1.729% × 4.011 ≈ **6.94%**, i.e. about 7.0%. The gain is the discount, since a T-bill pays no coupon.

**D3. Which statement about coupon and yield is correct?**
(a) They are always equal (b) Coupon changes daily with price (c) They are equal only when the bond trades at par (d) YTM ignores the principal repayment

**Answer: (c).** Coupon is fixed on face value; yield varies daily with price. They coincide only at par. YTM does include the principal — it discounts all coupons *and* the face value back to the price.

**D4. In India, corporate bonds are primarily issued through:**
(a) RBI E-Kuber auctions (b) Private placement via the Electronic Bidding Platform (c) Public NCD issues to retail (d) NDS-OM

**Answer: (b) Private placement via the EBP.** Over 95% of Indian corporate issuance is privately placed to large institutions on the EBP — fast and cheap. E-Kuber and NDS-OM are RBI G-sec platforms; public NCD issues exist but are a small minority.

**D5. An SDL typically yields more than a central G-sec of the same maturity because:**
(a) It has higher default risk from the sovereign guarantee (b) It is unsecured (c) It is marginally less liquid and carries a whisper of extra risk (d) It pays no coupon

**Answer: (c).** Both are sovereign-backed, but SDLs are state-level and less liquid, so they yield roughly 30–60 bps more. They are not unsecured, not zero-coupon, and not more likely to default in any headline sense.

**D6. The 2020 YES Bank episode is most directly an illustration of the risk in:**
(a) Zero-coupon T-bills (b) AT1 perpetual bonds being written down to zero (c) Callable G-secs (d) Currency mismatch on masala bonds

**Answer: (b) AT1 write-down.** YES Bank's Additional Tier-1 perpetual bonds were written down to zero to absorb losses — the defining risk of AT1 instruments, despite their bond label and often-decent ratings.

**D7. A bond has a duration of 8. If yields fall by 0.5%, its price will approximately:**
(a) Fall 4% (b) Rise 4% (c) Rise 8% (d) Be unchanged

**Answer: (b) Rise 4%.** Price change ≈ −duration × yield change = −8 × (−0.5%) = **+4%**. Falling yields raise prices, and the longer the duration, the larger the move.

**D8. "Corporate yield minus G-sec yield of the same maturity" defines:**
(a) Duration (b) Current yield (c) The credit spread (d) The coupon

**Answer: (c) The credit spread.** It is the market's compensation for the corporate's default and liquidity risk over the risk-free sovereign, and a widening spread warns of credit stress.

**D9. Which risk applies even to a G-sec held by a mutual fund that marks to market daily?**
(a) Default risk (b) Interest-rate (price) risk (c) Currency risk (d) None — G-secs are risk-free

**Answer: (b) Interest-rate risk.** A G-sec has effectively no rupee default risk, but its price still falls when yields rise, hurting a fund that marks to market. "Risk-free" covers default only, not price risk on early sale or revaluation.

**D10. RBI Retail Direct (launched 2021) is significant because it:**
(a) Lets banks meet their SLR (b) Lets individuals buy G-secs, T-bills, and SDLs directly with zero fees (c) Replaces credit rating agencies (d) Guarantees corporate bonds

**Answer: (b).** Retail Direct lets individuals open a gilt account with the RBI and buy government securities at auction with no fees — a genuine democratisation of a once-institutional market.

---

*End of Q&A bank — Chapter 07, Bond and Debt Markets.*
