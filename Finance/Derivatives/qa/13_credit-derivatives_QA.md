# Q&A — Credit Derivatives

Practice bank for Chapter 13. Every question is followed by a full worked answer. Work each one before reading the solution. Spreads are quoted in basis points per annum; "protection buyer" pays the premium and is *short* credit risk; recovery rates are on face value unless stated; act/360 accrual on premium legs unless a problem says otherwise.

---

## Section A — Concept Check

**A1. In one sentence, what is a credit derivative, and what risk does it isolate?**

A credit derivative is a bilateral contract whose payoff is driven by the *creditworthiness* of one or more reference entities — it strips out and transfers **default / credit-deterioration risk** on its own, separate from the interest-rate, funding and ownership risks that are bundled together when you simply hold the underlying bond or loan.

**A2. Describe the two legs of a single-name credit default swap (CDS).**

The **premium (fee) leg**: the protection buyer pays a periodic spread (e.g. quarterly, act/360) on the notional to the protection seller until maturity *or* a credit event, whichever comes first — plus accrued premium up to a credit event. The **protection (contingent) leg**: if a credit event occurs, the seller pays the buyer the loss given default, i.e. notional × (1 − recovery), settled physically (deliver the defaulted bond for par) or in cash (par minus the auction-determined recovery price). No credit event, the protection leg never pays.

**A3. Why is a CDS often described as "insurance on a bond," and where does that analogy break?**

Like insurance, the buyer pays a small regular premium and is compensated on a defined adverse event. It breaks in three places: (i) you need not *own* the reference bond to buy a CDS — "naked" protection is allowed, so it is also a directional/speculative instrument; (ii) the payout is triggered by a standardised **credit event** determined by an ISDA committee, not by the buyer's actual loss; (iii) CDS is freely tradable and marked to market daily, so it has its own P&L even with no default.

**A4. List the standard ISDA credit events.**

**Bankruptcy**, **failure to pay** (after any grace period), and **restructuring** (a coupon cut, maturity extension, subordination or currency change imposed on creditors). For some reference types **obligation acceleration**, **obligation default**, and **repudiation/moratorium** (mainly sovereigns) also apply. A **Determinations Committee** rules whether an event has occurred.

**A5. What is the CDS spread and what does it compensate the seller for?**

The CDS spread is the annualised premium (in bp of notional) that sets the swap's value to zero at inception — the fair price of protection. It compensates the seller for the *expected loss* from default: roughly, spread ≈ hazard rate × (1 − recovery). A wider spread signals a higher market-implied probability of default and/or a lower expected recovery.

**A6. State the credit-triangle approximation linking spread, default intensity and recovery.**

$s \approx \lambda \,(1 - R)$, where $s$ is the annual CDS spread (as a decimal), $\lambda$ is the annual hazard rate (instantaneous default intensity), and $R$ is the recovery rate. So the market-implied *annual* default probability ≈ spread / (1 − recovery). It is an approximation because it ignores discounting, accrual timing and the term structure of hazard rates, but it is the workhorse mental model.

**A7. Distinguish a single-name CDS from a CDS index (e.g. CDX / iTraxx).**

A single-name CDS references *one* entity; the index references a *portfolio* of names (e.g. iTraxx Europe = 125 investment-grade names, equally weighted). Buying index protection is economically like buying protection on each constituent for 1/N of the notional. On a constituent default the index notional steps down and that name's loss settles, while the rest keeps running. Indices are more liquid and are the standard macro credit hedge.

**A8. What does a total-return swap (TRS) transfer that a CDS does not?**

A TRS transfers the *entire* economic return of the reference asset — price change (from **both** interest-rate and credit moves), coupon income, in both directions, every period — against a financing leg. A CDS transfers *only* default-type credit loss and pays *only* on a credit event. So a bond TRS carries interest-rate P&L and mark-to-market that a CDS does not; CDS is default protection alone.

**A9. In a synthetic CDO, what do the equity, mezzanine and senior tranches represent?**

They are claims on a pool of credit risk (often a portfolio of CDS) sliced by loss-absorption priority. The **equity tranche** absorbs the *first* losses (say 0–3%) — highest risk, highest spread. **Mezzanine** absorbs the next band (e.g. 3–7%). The **senior/super-senior** tranche only takes losses after the lower tranches are wiped out — lowest risk, lowest spread. The key driver of relative tranche value is **default correlation** among the pool names.

**A10. Why does default correlation matter for tranche pricing, and which tranche is "long correlation"?**

Correlation reshapes the *distribution* of pool losses without changing the expected loss. High correlation makes extreme outcomes (either almost no defaults or many simultaneous defaults) more likely. That fattens the tail, which *helps* the equity tranche (fewer scenarios of a few isolated defaults wiping it out) and *hurts* the senior tranche (more scenarios of mass default reaching it). So the **senior tranche is short correlation** and the **equity tranche is long correlation** — a subtlety that detonated in 2008.

---

## Section B — Numerical / Pricing Problems

**B1. Credit-triangle: back out default probability.** A 5-year CDS on Entity X trades at 240 bp. Assuming 40% recovery, estimate the market-implied annual default probability and the cumulative 5-year probability.

Annual hazard: $\lambda \approx s/(1-R) = 0.0240 / (1 - 0.40) = 0.0240/0.60 = \mathbf{0.0400 = 4.0\%}$ per year.

Cumulative 5-year survival $= e^{-\lambda T} = e^{-0.04\times5} = e^{-0.20} = 0.8187$, so cumulative 5-year default probability $= 1 - 0.8187 = \mathbf{18.13\%}$.

Intuition: a 240 bp spread with 40% recovery implies roughly a 4% chance of default each year — the spread is the annual "toll" for bearing that expected loss. ✓

**B2. Expected-loss check on the spread.** Confirm that a 4% hazard and 40% recovery are consistent with roughly a 240 bp fair spread, ignoring discounting.

Expected annual loss $= \lambda \times (1-R) = 0.04 \times 0.60 = 0.024 = 240$ bp. The seller must be paid its expected loss each year to break even, so the fair running spread ≈ 240 bp. ✓ This is the credit triangle read the other way: $s \approx \lambda(1-R)$.

**B3. Protection-leg payout on default.** You bought \$10m notional of CDS protection on Entity Y. Y defaults; the ISDA auction sets the recovery price at 35. Compute the seller's payment under (a) cash settlement and (b) physical settlement.

Loss given default $= 1 - R = 1 - 0.35 = 0.65$.

(a) **Cash:** seller pays notional × (1 − R) $= \$10{,}000{,}000 \times 0.65 = \mathbf{\$6{,}500{,}000}$.

(b) **Physical:** buyer delivers \$10m face of deliverable Y bonds and receives par $= \$10{,}000{,}000$. Since those bonds are worth $0.35 \times 10\text{m} = \$3.5$m in the market, the buyer's net gain $= 10.0 - 3.5 = \mathbf{\$6.5\text{m}}$ — identical economics. ✓

**B4. Value a CDS position after spreads move.** You bought 5-year protection at 150 bp. One year later the fair 4-year spread on the same name is 300 bp. Approximate your mark-to-market gain per \$10m notional, using a risky annuity (RPV01) of 3.6.

You are paying 150 bp but the market now charges 300 bp for the same protection — you are locked into a *cheap* long-protection position. Value ≈ (market spread − contract spread) × RPV01 × notional $= (0.0300 - 0.0150) \times 3.6 \times 10{,}000{,}000 = 0.0150 \times 3.6 \times 10{,}000{,}000 = \mathbf{+\$540{,}000}$.

Sign check: spreads *widened*, credit deteriorated, and the protection *buyer* profits from deterioration — positive MTM. ✓ (The RPV01 is the PV of 1 bp of premium over the remaining life, adjusted for survival probability; multiplying the spread change by it converts a running-spread differential into an upfront value.)

**B5. Upfront vs running under the standard coupon.** Post-"Big Bang," a CDS trades with a fixed 100 bp running coupon but a fair spread of 250 bp. Using RPV01 = 4.2, compute the upfront the protection buyer must pay per \$10m, and explain the sign.

Upfront $\approx$ (fair spread − fixed coupon) × RPV01 × notional $= (0.0250 - 0.0100) \times 4.2 \times 10{,}000{,}000 = 0.0150 \times 4.2 \times 10{,}000{,}000 = \mathbf{\$630{,}000}$ paid by the buyer.

Because the standardised running coupon (100 bp) is *below* the fair spread (250 bp), the buyer is underpaying on the running leg and must compensate the seller with a positive upfront. If the fair spread were *below* 100 bp, the upfront would flip and the *seller* would pay the buyer. ✓

**B6. Index protection and a constituent default.** You hold \$125m of iTraxx-style index protection on 125 equally weighted names (\$1m each). One name defaults with recovery 30%; the index spread was 80 bp running.

**Default settlement:** that name's slice is \$1m notional; protection pays $1{,}000{,}000 \times (1 - 0.30) = \mathbf{\$700{,}000}$ to you.

**Notional step-down:** the index factor drops to 124/125; your remaining notional $= \$125\text{m} \times 124/125 = \$124\text{m}$, and premium now accrues on \$124m: $0.0080 \times 124{,}000{,}000 = \$992{,}000$/yr vs \$1,000,000 before. The defaulted name is removed and the surviving 124 keep running. ✓

**B7. Basis-trade P&L (bond vs CDS).** A bond yields 6.0% (i.e. trades at a 250 bp Z-spread over swaps); the 5-year CDS on the same issuer is 200 bp. The **CDS basis** = CDS spread − bond spread. Compute it, say whether it is positive or negative, and describe the arbitrage.

Basis $= 200 - 250 = \mathbf{-50\ \text{bp}}$ (negative basis). Protection is *cheaper* than the credit risk embedded in the bond. Arbitrage: **buy the bond** (earn 250 bp of credit spread) and **buy CDS protection** (pay 200 bp), locking in ≈ +50 bp of near-riskless carry while the credit risk is hedged. The trade profits if the basis converges toward zero; the residual risk is funding cost, counterparty risk on the CDS seller, and the bond/CDS not being perfectly matched (deliverability, coupon). ✓

**B8. Hazard-rate term structure and survival.** A name has a flat hazard rate of 3% for years 1–3 and 6% for years 4–5. Compute the cumulative survival probability to 5 years.

Survival $= e^{-(0.03\times3 + 0.06\times2)} = e^{-(0.09 + 0.12)} = e^{-0.21} = \mathbf{0.8106}$, so cumulative 5-year default probability $= 1 - 0.8106 = \mathbf{18.94\%}$.

The rising hazard term structure (credit expected to worsen) means later years contribute more default probability per year — the survival curve steepens after year 3. ✓

---

## Section C — Interview-Style Questions with Model Answers

**C1. "Walk me through what happens, step by step, when a name in your CDS portfolio defaults."**

Model answer: "First, a market participant asks ISDA's Determinations Committee to rule whether a credit event — bankruptcy, failure to pay or restructuring — has occurred. If the DC says yes, it fixes an event date and the premium leg stops accruing there, with the buyer owing accrued premium up to that point. Then an **auction** is held to establish a single market-wide recovery price for the cheapest-to-deliver obligations, so all contracts settle at the same number. Protection sellers pay buyers par minus that recovery — cash settlement — or, if physically settled, buyers deliver the defaulted bonds and receive par. The contract then terminates. For an index, only the defaulted name settles and drops out; the index notional steps down and the survivors keep running."

**C2. "Spread ≈ hazard × (1 − recovery). Where does that come from, and what breaks it?"**

Model answer: "It's the *credit triangle*, an equilibrium condition: the protection seller must be paid, each year, the loss it expects to suffer. Expected annual loss is the probability of defaulting that year, the hazard rate, times the loss if it does, one minus recovery. Set the premium equal to that expected loss and you get $s \approx \lambda(1-R)$. It's an approximation because it ignores discounting, the timing of the accrued-premium rebate on default, and the fact that hazard rates have a term structure rather than being constant. For pricing I'd build a full survival curve and discount both legs, but the triangle is the intuition I carry in my head — and it tells me spreads and recoveries are jointly identified, so I can't back out a default probability without assuming a recovery."

**C3. "A PM says CDS is just insurance. Push back."**

Model answer: "It rhymes with insurance but differs in three material ways. One, you don't need an insurable interest — naked CDS lets you buy protection on debt you don't own, so it's also an outright directional short on credit, which is why regulators restricted naked sovereign CDS in Europe. Two, the payout isn't your actual loss; it's driven by a standardised credit event ruled on by a committee and a par-minus-auction-recovery formula, so basis and deliverability can leave you imperfectly hedged. Three, it's a traded, mark-to-market instrument with daily P&L and counterparty risk on the seller — AIG in 2008 is the cautionary tale of a seller that wrote protection it couldn't collateralise. So CDS is insurance, a short-credit trade, and a marked position all at once."

**C4. "How would you use CDS indices to hedge a corporate bond book, and what's the residual risk?"**

Model answer: "For a macro credit hedge I'd buy protection on the relevant index — CDX IG or iTraxx Main for investment grade, the crossover/high-yield index for lower quality — sized so the index's spread duration times notional matches my book's spread DV01. That neutralises broad spread-widening cheaply and liquidly. The residuals are: **basis risk**, because the index constituents aren't my exact names; **idiosyncratic risk**, since a blow-up in one of my holdings that isn't in the index is unhedged; and the **skew** between the index and the theoretical sum of its single-name constituents. For single-name concentrations I'd overlay specific CDS. The index is the blunt, liquid instrument; single names are the scalpel."

**C5. "Explain how correlation, not just default probability, drove the 2008 CDO losses."**

Model answer: "Tranches slice a portfolio's loss distribution. Correlation doesn't change expected losses, but it reshapes the distribution — high correlation makes 'all together' outcomes more likely, thinning the middle and fattening both tails. The senior and super-senior tranches were priced as if defaults were largely independent, so reaching them required an implausible number of simultaneous defaults. When housing turned, defaults became highly *correlated* — everything deteriorated at once — and losses punched straight through the mezzanine into the 'safe' senior tranches that were rated AAA. The models used a single **Gaussian copula** correlation number that badly understated tail co-movement. So the senior tranches were structurally *short correlation*, and the correlation they were short of spiked to near one. It's the canonical lesson that in credit, the joint distribution matters as much as the marginals."

---

## Section D — Multiple-Choice Questions with Reasoning

**D1.** In a single-name CDS, the protection buyer:

A) receives a premium and is long the credit  B) pays a premium and is short the credit  C) pays a premium and is long the credit  D) receives a premium and is short the credit

**Answer: B.** The buyer *pays* the periodic spread and profits if credit *deteriorates* (spreads widen or the name defaults) — economically **short** the credit. A and D reverse the cash flow; C reverses the risk direction.

**D2.** Which of the following is *not* a standard ISDA credit event?

A) Bankruptcy  B) Failure to pay  C) Restructuring  D) Credit-rating downgrade

**Answer: D.** A ratings downgrade alone is *not* a CDS credit event — bonds keep paying and no ISDA trigger fires. Bankruptcy, failure to pay and restructuring are the core events. (A downgrade may move the *spread*, i.e. the mark-to-market, but never triggers the protection leg.)

**D3.** Using the credit triangle, a 300 bp CDS spread with 25% recovery implies an annual default probability of approximately:

A) 2.25%  B) 3.00%  C) 4.00%  D) 12.0%

**Answer: C.** $\lambda \approx s/(1-R) = 0.03/(1-0.25) = 0.03/0.75 = 0.04 = 4.0\%$. B ignores the recovery adjustment; A multiplies instead of divides by (1 − R); D uses (1 − R) in the wrong place.

**D4.** Compared with a CDS, a total-return swap on the same bond:

A) pays only on a credit event  B) transfers the entire return including interest-rate P&L  C) transfers no credit risk  D) requires no financing leg

**Answer: B.** A TRS passes the whole economic return — price change from rates *and* credit, plus coupons, in both directions — against a financing leg. A describes a CDS; C is false (it *includes* credit risk); D is false (the receiver pays a financing rate + spread).

**D5.** In a synthetic CDO, the tranche that absorbs the *first* losses and earns the *highest* spread is the:

A) super-senior tranche  B) senior tranche  C) mezzanine tranche  D) equity tranche

**Answer: D.** The equity (first-loss) tranche takes the initial defaults, so it carries the most risk and the highest spread. Senior and super-senior (A, B) only take losses after the lower tranches are exhausted; mezzanine (C) sits in between.

**D6.** All else equal, an increase in default correlation across the pool:

A) helps the senior tranche, hurts the equity tranche  B) helps the equity tranche, hurts the senior tranche  C) helps both  D) changes the pool's expected loss

**Answer: B.** Higher correlation fattens the tails: fewer isolated-default scenarios (good for first-loss equity) but more mass-default scenarios (bad for the senior tranche). D is wrong — correlation reshapes the loss *distribution* but leaves expected loss unchanged. Equity is long correlation; senior is short it.

**D7.** The CDS basis is defined as CDS spread minus bond (cash) spread. A *negative* basis means:

A) protection is expensive relative to the bond  B) protection is cheap relative to the bond, favouring buy-bond + buy-protection  C) the bond is mispriced upward  D) default is certain

**Answer: B.** Negative basis = CDS spread < bond spread, i.e. protection is cheap. The classic negative-basis trade is to buy the bond (earn its wider spread) and buy CDS protection (pay the narrower spread), locking near-riskless carry until convergence. A reverses it; C and D don't follow.

**D8.** Post-2009 "Big Bang," standard single-name CDS trade with fixed running coupons (e.g. 100/500 bp) plus an upfront. The upfront exists to:

A) replace the protection leg  B) reconcile the fixed coupon with the name's fair spread  C) pay the ISDA committee  D) collateralise the trade

**Answer: B.** Standardising the coupon means it rarely equals the fair spread, so an **upfront** payment bridges the difference — buyer pays if the fair spread exceeds the coupon, seller pays if it's below. This standardisation improves fungibility and netting. A, C and D describe unrelated mechanics.

---

*Self-verification notes: B1 and B2 are mutual inverses of the credit triangle $s \approx \lambda(1-R)$ and reconcile at 240 bp / 4% hazard / 40% recovery. B3's cash and physical settlements both net to \$6.5m, confirming settlement-method equivalence. B4's sign (protection buyer gains when spreads widen) matches the short-credit direction in D1. B5's upfront is positive because the fair spread (250) exceeds the fixed coupon (100), consistent with D8. B6's step-down (124/125 factor) and D6/C5's correlation logic (equity long, senior short) are internally consistent. B7's −50 bp negative basis matches the buy-bond/buy-protection trade in D7. Formulas used: $s \approx \lambda(1-R)$, survival $= e^{-\int \lambda\,dt}$, MTM ≈ Δspread × RPV01 × notional, upfront ≈ (fair spread − coupon) × RPV01 × notional, basis = CDS spread − bond spread.*
