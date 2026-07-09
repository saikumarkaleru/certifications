# Q&A — Repo and Funding Markets

Practice bank for Chapter 14. Work each question before reading the answer. Numerical answers use India money-market conventions (simple interest, actual/365) unless stated otherwise.

---

## Section A — Concept Checks

**A1. In one sentence, what is a repurchase agreement, and who is borrowing what?**

A repo is the sale of a security today combined with a binding agreement to buy it back at a fixed price on a future date; economically it is a secured loan in which the *seller of the security borrows cash* and the *buyer of the security lends cash*, with the security serving as collateral.

**A2. Why does the same trade have two names — "repo" and "reverse repo"?**

Because a single transaction looks different from each side. The party who owns the bond and needs cash is doing a **repo** ("I repo out my bonds"). The party who has cash and wants collateral is doing a **reverse repo** ("I reverse in the bonds"). One trade, two labels; the name depends purely on perspective. Anchor on cash: give cash + take bond = reverse repo; take cash + give bond = repo.

**A3. Why does a repo rate sit *below* the comparable unsecured interbank rate?**

Interest compensates a lender for the time value of money and for repayment risk. Good collateral strips out most of the repayment risk, so the lender demands less. The gap between the unsecured benchmark and the secured repo rate is effectively a real-time market price of bank credit risk — it widened dramatically in 2008.

**A4. What is a haircut, and in which direction does a larger haircut help or hurt each party?**

The haircut is the cushion by which collateral value exceeds cash lent — the lender advances less than the bond is worth. A *larger* haircut is *safer for the lender* (more protection if the collateral falls in value before liquidation) and *worse for the borrower* (less cash per bond, i.e., tighter funding). Higher haircut = more protection = tighter funding.

**A5. Name the five factors that push haircuts higher and give the intuition for one.**

(1) Higher collateral price volatility, (2) lower collateral liquidity, (3) longer repo term, (4) weaker counterparty credit, and (5) wrong-way risk (collateral correlated with the borrower). Intuition for wrong-way risk: the collateral loses value at exactly the moment the borrower defaults, so the lender's protection evaporates when it is needed most — hence a much larger haircut.

**A6. What legally distinguishes a repo from an ordinary pledged loan, and why does that distinction matter on default?**

A repo is structured as a true *sale* with an agreement to repurchase, so ownership (title) of the collateral actually transfers to the cash lender. In most major jurisdictions this earns **safe-harbour** treatment: on the borrower's bankruptcy the lender can immediately liquidate the collateral without waiting behind an automatic stay. This legal certainty is precisely why lenders accept such thin margins.

**A7. Distinguish General Collateral (GC) repo from special repo.**

In **GC repo** the lender accepts any bond from an agreed basket and cares only about the *cash rate*; it is pure financing and the rate tracks the policy rate. In **special repo** the lender wants one *specific* scarce bond (usually to deliver into a short sale or fail), so the trade is about sourcing the bond and the cash rate drops below GC by the "specialness spread."

**A8. Why does a bond "on special" trade at a *lower* repo rate, not a higher one?**

Demand is for the *bond*, not the cash. To obtain the scarce security, the cash lender must accept less interest on the cash it lends — they are effectively paying to borrow the scarce bond. So heavy demand for a specific bond depresses its repo *cash* rate, sometimes to near zero or negative.

**A9. Write the net-carry relationship for a repo-financed bond and state when carry is positive.**

Net carry = coupon accrued on the bond − repo interest paid. Carry is **positive** when coupon accrual exceeds repo cost — normal in an upward-sloping curve where long-bond coupons exceed short repo rates. It turns negative and dangerous when funding spikes above coupon income.

**A10. What is rehypothecation, and why is it both powerful and dangerous?**

Because title transfers to the cash lender, that lender can (subject to the agreement) re-use — rehypothecate — the collateral by repo-ing it out again to a third party. This lets a single bond support a long chain of financing, multiplying market funding capacity. It is dangerous because those same collateral chains transmit stress rapidly through the system, as 2008 demonstrated.

**A11. In tri-party repo, what does the agent bank do?**

A third-party agent bank sits between the two principals and holds, values, and manages the collateral — applying haircuts, marking to market, issuing margin calls, and swapping (substituting) collateral in and out. It industrialises GC financing and removes the operational burden of delivery from both principals (CCIL performs this role in India).

**A12. Why is SOFR relevant to a chapter on repo?**

SOFR (Secured Overnight Financing Rate), the US risk-free benchmark that replaced LIBOR, is literally a volume-weighted median of overnight Treasury repo transaction rates. The risk-free short-end benchmark is now a repo curve — LIBOR (unsecured, survey-based) was replaced by SOFR (secured, transaction-based) after the LIBOR scandal.

---

## Section B — Numerical / Applied (full solutions)

**B1. Plain overnight government repo.** A dealer owns ₹100 crore face of a G-sec; dirty price 101.50. Lender applies a 1% haircut; overnight repo rate 6.50% (actual/365, n = 1). Find the cash advanced, the one-day interest, and the repurchase price.

*Solution.*
Market value M = 100,00,00,000 × 101.50/100 = ₹101,50,00,000.
Cash advanced P₀ = M(1 − h) = 101,50,00,000 × 0.99 = **₹100,48,50,000**.
Interest = P₀ × r × n/B = 100,48,50,000 × 0.065 × (1/365) = **₹17,894.52**.
Repurchase price P₁ = P₀ + Interest = **₹100,48,67,894.52**.

*Self-check:* the lender's return on cash = 17,894.52 / 100,48,50,000 × 365 = 0.0650 = 6.50% annualised. ✓

**B2. Term repo.** Same collateral (dirty value ₹101,50,00,000), now a 14-day term repo at 6.75%, haircut 2%. Find near-leg cash, 14-day interest, and repurchase price.

*Solution.*
P₀ = 101,50,00,000 × 0.98 = **₹99,47,00,000**.
Interest = 99,47,00,000 × 0.0675 × (14/365) = 99,47,00,000 × 0.00258904 = **₹2,57,533.60**.
P₁ = 99,47,00,000 + 2,57,533.60 = **₹99,72,57,533.60**.

**B3. Margin call.** Continue B2 with a maintained margin ratio of 102% (collateral ≥ 1.02 × cash lent). On Day 5 the bond's dirty price falls from 101.50 to 100.20. How much variation margin must the borrower post?

*Solution.*
New collateral value = 100,00,00,000 × 100.20/100 = ₹100,20,00,000.
Required collateral = 1.02 × 99,47,00,000 = ₹101,45,94,000.
Shortfall = 101,45,94,000 − 100,20,00,000 = **₹1,25,94,000** (₹1.2594 crore).

*Self-check:* after topping up, (100.20 + 1.2594) cr / 99.47 cr = 101.4594 / 99.47 = 1.0200 exactly — the 102% ratio is restored. ✓

**B4. Net carry and return on equity.** A dealer buys ₹50 crore face of a 7.20% annual-coupon bond, dirty price 100.00, financed overnight-rolled in GC repo at an average 6.40% for 30 days, haircut 1%. Compute the dealer's own capital in the trade, coupon accrued, repo cost, net carry, and annualised return on equity.

*Solution.*
M = ₹50,00,00,000. P₀ = 50,00,00,000 × 0.99 = ₹49,50,00,000, so own capital = M − P₀ = **₹50,00,000**.
Coupon (actual/365, 30 days) = 50,00,00,000 × 0.072 × 30/365 = **₹2,95,890.41**.
Repo cost = 49,50,00,000 × 0.064 × 30/365 = **₹2,60,432.88**.
Net carry = 2,95,890.41 − 2,60,432.88 = **₹35,457.53** (positive).
Return on equity, annualised = (35,457.53 / 50,00,000) × (365/30) = 0.00709 × 12.1667 = **8.63%**.

*Lesson:* a bond yielding ~7.20% delivers 8.63% on equity because 99% of the position was financed at 6.40% — a 0.80% gross carry spread magnified by ~100× leverage.

**B5. Negative carry stress.** In B4, suppose overnight repo spikes to 7.60% (above the 7.20% coupon). Recompute net carry.

*Solution.*
Repo cost = 49,50,00,000 × 0.076 × 30/365 = ₹3,09,264.66.
Net carry = 2,95,890.41 − 3,09,264.66 = **−₹13,374.25** (negative).
The position now bleeds cash daily — exactly the dynamic that forces leveraged holders to dump bonds when funding tightens, transmitting repo stress into bond prices.

**B6. USD day-count contrast.** A US dealer does a $200 million overnight Treasury repo at 5.30% (actual/360, haircut 0.5%). Find the cash advanced and one-day interest. Assume dirty value $200m.

*Solution.*
P₀ = 200,000,000 × (1 − 0.005) = **$199,000,000**.
Interest = 199,000,000 × 0.0530 × (1/360) = 199,000,000 × 0.00014722 = **$29,297.22**.
Note the /360 basis: the same rate on the same day count earns slightly more interest per day than /365 because the denominator is smaller.

**B7. Back out the haircut.** A lender advances ₹98,00,00,000 against collateral with dirty value ₹100,00,00,000. What is the haircut (percentage-of-value convention) and the implied margin ratio?

*Solution.*
Haircut h: P₀ = M(1 − h) → 98 = 100(1 − h) → h = 1 − 0.98 = **2%**.
Margin ratio = M / P₀ = 100 / 98 = **1.0204 = 102.04%**.

**B8. Specialness spread as a cost.** GC repo is 6.50%. A short-seller must borrow a specific bond that is trading special at a 4.00% repo rate for 7 days on ₹20 crore of cash. What is the specialness spread in bps, and what does it cost the short over the week versus funding at GC?

*Solution.*
Specialness spread = 6.50% − 4.00% = 2.50% = **250 bps**.
The short lends ₹20 cr of cash to source the bond and earns only 4.00% instead of the 6.50% GC rate, forgoing 2.50%.
Cost over 7 days = 20,00,00,000 × 0.025 × 7/365 = **₹95,890.41**.
This forgone interest is the running cost of maintaining the short position.

---

## Section C — Interview-Style (model answers)

**C1. "Walk me through what actually happens, leg by leg, in an overnight repo."**

On Day 0 the cash borrower delivers the bond to the cash lender and simultaneously receives cash equal to the collateral's dirty market value less the haircut. The lender now holds legal title to the bond. On Day 1 the borrower pays back the cash plus repo interest (the repurchase price P₁ = P₀(1 + r·n/B)) and the lender returns the same bond. Throughout the loan the lender holds the collateral, so if the borrower fails to repay, the lender simply keeps and sells the bond. Credit risk has been transformed into the much smaller risk that the collateral loses value faster than it can be liquidated — and even that residual is managed by the haircut and daily margining.

**C2. "The RBI's use of 'repo' seems backwards to me. Explain."**

The market defines repo from the cash borrower's side — the party giving up the bond and taking cash. The RBI, by contrast, names its operation from the *system's* function. Under the LAF, an RBI **repo** operation *injects* cash: the RBI lends cash to banks against G-secs. Strictly, the RBI is receiving securities and giving cash, which by the market definition is a reverse repo — but it is called "repo" because the banks (the counterparties) are the ones repo-ing out their securities. The RBI's "reverse repo" (and now the SDF) *absorbs* cash — banks park funds with the RBI. The clean rule for India: RBI repo = RBI injects cash (the policy rate you hear about); RBI reverse repo / SDF = RBI absorbs cash. Learn the central-bank convention separately rather than forcing it into the market-side definition.

**C3. "Why do people say repo is the plumbing of the financial system?"**

Almost every fixed-income position is financed, and repo is the cheapest financing because it is secured. Dealer inventories, leverage, short-selling, money funds, and central-bank policy transmission all sit on top of the repo market. When it functions, no one notices. When it seizes — 2008, the September 2019 US repo spike, the March 2020 dash-for-cash — funding evaporates, leveraged holders are forced to sell, and stress propagates upward into every market above it.

**C4. "What are haircut spirals and why are they dangerous?"**

Haircuts are procyclical: they widen in stress precisely when funding is scarcest. As collateral values fall and volatility rises, lenders demand bigger haircuts, so borrowers get less cash per bond and must sell assets to cover the shortfall. Those sales push prices down further, raising volatility and haircuts again — a self-reinforcing "haircut spiral." This feedback loop was a documented amplifier of the 2008 crisis: deleveraging fed on itself through the collateral market.

**C5. "How does repo enable short-selling, and what is specialness telling you?"**

You cannot sell a bond you do not own unless you can deliver it. So the short-seller does a reverse repo — lends cash and receives the specific bond — then sells that bond in the market. If many traders short the same bond, demand to borrow it surges and the bond goes "on special": its repo rate falls below GC. The specialness spread (GC minus the special rate) is the running cost of holding the short and the market's price signal for crowded short positions. It also drives cheapest-to-deliver dynamics in bond futures, where the CTD bond often trades special because shorts in the future need to deliver it.

**C6. "Give me the intuition for why leverage in a repo carry trade cuts both ways."**

The dealer funds nearly the whole position with borrowed cash and puts up only the haircut as equity, so a small gross carry spread — coupon accrual minus repo cost — is magnified into a large return on that thin equity (a 0.80% spread on a 100×-levered position became 8.63% on capital in my example). The same leverage works in reverse: if repo rises above the coupon, carry turns negative and the position bleeds daily on the full financed amount while equity is tiny. That asymmetry is why leveraged carry trades unwind violently when funding tightens.

**C7. "Where does the 'risk-free' story of repo actually break down?"**

Wrong-way risk. Repo converts counterparty credit risk into collateral (market plus liquidity) risk, and that transformation is clean only when the collateral's value is independent of the borrower's solvency. When the collateral is correlated with the borrower — its value falls exactly when the borrower defaults — the lender's protection collapses at the worst moment. The canonical case is subprime mortgage repo in 2008: dealers financing mortgage collateral that was deteriorating for the same reasons the dealers were failing. That is why wrong-way risk commands a much larger haircut and is the one place the "risk-free" framing genuinely breaks.

---

## Section D — MCQs (with reasoning)

**D1. In a repo, the party that delivers the bond on the near leg is:**
A) lending cash B) borrowing cash C) earning the specialness spread D) the tri-party agent

**Answer: B.** The bond-deliverer is the cash *borrower* (doing a repo); they give the bond and take cash. The bond-receiver lends the cash (reverse repo). The agent (D) never a principal.

**D2. A bond trading "on special" has a repo rate that is:**
A) above GC B) equal to GC C) below GC D) equal to the coupon

**Answer: C.** Heavy demand for the specific bond forces the cash lender to accept *less* interest on the cash to obtain the scarce security, so the special rate sits below GC. Assuming "special = high rate" is the classic trap.

**D3. All else equal, increasing the haircut on a repo:**
A) gives the borrower more cash B) reduces the lender's protection C) reduces the cash advanced to the borrower D) raises the repo interest rate

**Answer: C.** With P₀ = M(1 − h), a larger h means less cash for a given collateral value — worse funding for the borrower and more protection for the lender. It does not by itself change the quoted repo rate.

**D4. Repo interest is calculated on:**
A) the bond's face value B) the collateral's market value C) the cash advanced (P₀) D) the repurchase price (P₁)

**Answer: C.** Interest = P₁ − P₀ = P₀ · r · n/B, computed on the cash advanced. The collateral value only determines *how much* cash via the haircut; it is not the interest base.

**D5. Which statement about an RBI LAF "repo" operation is correct?**
A) It absorbs liquidity from banks B) It injects cash into the banking system C) It is the corridor floor D) It is uncollateralised

**Answer: B.** An RBI repo injects cash (RBI lends to banks against G-secs); it is the policy rate at the corridor centre and is collateralised. The SDF (uncollateralised, absorbs cash) is the floor.

**D6. SOFR is best described as:**
A) an unsecured survey-based rate like LIBOR B) the RBI's overnight absorption rate C) a volume-weighted median of overnight Treasury repo rates D) a semi-annually compounded bond yield

**Answer: C.** SOFR is secured and transaction-based, built from overnight Treasury repo, and replaced the unsecured survey-based LIBOR after the LIBOR scandal.

**D7. Positive carry on a repo-financed bond position occurs when:**
A) the repo rate exceeds the coupon accrual B) the coupon accrual exceeds the repo cost C) the haircut is zero D) the bond is on special

**Answer: B.** Net carry = coupon accrued − repo interest; it is positive when coupon accrual exceeds repo cost, typical in an upward-sloping curve.

**D8. The legal feature that lets a repo lender liquidate collateral immediately on the borrower's bankruptcy is:**
A) rehypothecation B) the margin ratio C) safe-harbour / title-transfer treatment D) the GMRA close-out netting alone

**Answer: C.** Because repo is a true sale with title transfer, it enjoys safe-harbour treatment exempting it from the automatic stay, so the lender can liquidate at once. This legal certainty is why repo rates can be so thin. (The GMRA documents the terms, but the enabling feature is the sale/title-transfer structure.)

**D9. In the RBI's LAF corridor, the ceiling and floor are, respectively:**
A) Repo rate and SDF B) MSF and SDF C) MSF and Repo rate D) SDF and MSF

**Answer: B.** MSF (repo + 25 bps, RBI lends) is the ceiling; SDF (repo − 25 bps, RBI absorbs, uncollateralised) has been the floor since April 2022; the repo rate anchors the centre where the RBI steers the WACR.

**D10. A dealer finances ₹100 cr of collateral (dirty) at a 2% haircut. The cash advanced is:**
A) ₹102 cr B) ₹100 cr C) ₹98 cr D) ₹99 cr

**Answer: C.** P₀ = 100 × (1 − 0.02) = ₹98 cr. The 2% haircut is the lender's cushion; the margin ratio is 100/98 ≈ 102%.

---

*Self-verification note: all numerical answers (B1–B8) were recomputed by both the additive (Interest = P₀·r·n/B) and multiplicative (P₁ = P₀(1 + r·n/B)) forms where applicable, and margin-ratio checks reconcile to the stated tolerances. Day-count bases: 365 for India/GBP, 360 for USD/EUR.*
