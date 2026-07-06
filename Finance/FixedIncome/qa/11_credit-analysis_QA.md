# Q&A — Credit Analysis

Companion practice bank for Chapter 11. Every question is followed by a full answer. Unless stated otherwise, figures are in \$ millions, spreads are over the Treasury curve, and default probabilities are risk-neutral (market-implied).

---

## Section A — Concept Check

**A1. What are the two independent pillars of creditworthiness, and why must you underwrite both?**
**Capacity** (can the borrower generate enough cash to service the debt?) and **willingness** (will they pay, and are you protected if they waver?). They are independent: a cash-rich borrower can still stiff you, and an honest borrower can simply run out of money. Underwriting only one leaves the other flank exposed.

**A2. State the Four Cs of credit and map each to a pillar.**
**Capacity, Collateral, Covenants, Character.** Capacity is the ability-to-pay pillar, measured with leverage and coverage ratios. Collateral (recovery if things break), Covenants (contractual guardrails), and Character (management integrity and financial policy) sit on the willingness/protection pillar — they govern whether and how much you recover when capacity falters.

**A3. Why do credit analysts anchor on cash flow and EBITDA rather than net income?**
Coupons are paid in cash, not accounting profit. A firm can report healthy net income while starving for cash — booking revenue on receivables it never collects, or capitalising costs that bleed cash later. EBITDA is a rough cash-earnings proxy; free cash flow is the rigorous measure. Debt is serviced out of cash, so the analyst's job is to *find the cash*.

**A4. Explain the sentence "equity is a call option and a risky bond is a risk-free bond minus a put."**
Shareholders have limited liability. At maturity, if assets exceed the debt face value they keep the surplus (a call struck at the debt); if assets fall short, they hand you the insufficient assets and walk away — a put, struck at the debt face value, that shareholders own and the bondholder is *short*. So a risky bond = risk-free bond − short put. That is why spreads widen with asset volatility: more volatility makes the shareholders' put more valuable, so your short-put costs more.

**A5. Distinguish leverage ratios from coverage ratios.**
**Leverage** ratios (Debt/EBITDA, Debt-to-Capital) measure *how much debt is stacked on the earnings or capital*; lower is safer. **Coverage** ratios (EBITDA/Interest, DSCR) measure *how comfortably earnings cover the obligations owed*; higher is safer. Leverage asks "how big is the debt?"; coverage asks "how easily can I pay what's due?"

**A6. Why can interest coverage look healthy while the credit is actually at risk?**
Interest coverage ignores *principal*. A firm with 8x interest coverage can still fail when a wall of maturing principal arrives and it cannot refinance. DSCR (which adds principal to the denominator) and the debt maturity schedule catch what interest coverage misses.

**A7. What is the single most important line in fixed income, and why is it a cliff rather than a slope?**
The boundary between **BBB−/Baa3 (lowest investment grade)** and **BB+/Ba1 (highest junk)**. It is a cliff because enormous pools of capital — insurers, pensions, many index funds — are barred from holding sub-investment-grade paper. A downgrade across the line ("fallen angel") triggers forced selling that blows the spread out far beyond the fundamental change; an upgrade ("rising star") triggers forced buying.

**A8. Contrast structural and reduced-form default models in one line each.**
**Structural (Merton, KMV):** default happens when firm asset value falls below the face value of debt; derived from the balance sheet via option theory; gives economic *insight*. **Reduced-form (Jarrow–Turnbull, Duffie–Singleton):** default is an exogenous jump governed by a hazard rate λ calibrated to market prices (spreads, CDS); tractable for *pricing* but a-theoretical about *why*.

**A9. State the "credit triangle" and its most important caveat.**
Spread ≈ PD × LGD = λ × (1 − Recovery). It links hazard rate, recovery, and spread, letting you strip an implied default probability out of any spread. The caveat: **PD and recovery are jointly unidentified from a single spread** — you can only solve for one by assuming the other; get recovery wrong and your implied PD is wrong the opposite way.

**A10. Distinguish maintenance from incurrence covenants and explain why cov-lite worries creditors.**
**Maintenance** covenants are tested *every period* regardless of any action (e.g., leverage below 4.5x each quarter-end); a breach is immediate technical default, an early-warning tripwire. **Incurrence** covenants are tested only when the borrower *takes an action* (issues debt, pays a dividend). **Cov-lite** loans strip out maintenance covenants — so a firm can deteriorate passively without ever tripping a test, removing the creditor's early warning.

---

## Section B — Numerical Bond-Math Problems

### B1. Building the ratio picture

Meridian Foods reports: EBITDA 300; D&A 90; Interest 60; Cash from operations 220; Capex 100; Total debt 1,050; Cash 150; Scheduled principal 90; Equity 700. Compute the core credit ratios and give a verdict.

**Step 1 — derive EBIT.** EBIT = EBITDA − D&A = 300 − 90 = **210**.

**Step 2 — leverage.**
Debt/EBITDA = 1,050 / 300 = **3.5x**.
Net Debt/EBITDA = (1,050 − 150) / 300 = 900 / 300 = **3.0x**.
Debt-to-Capital = 1,050 / (1,050 + 700) = 1,050 / 1,750 = **60%**.

**Step 3 — coverage.**
EBITDA interest coverage = 300 / 60 = **5.0x**.
EBIT interest coverage = 210 / 60 = **3.5x**.
DSCR = EBITDA / (Interest + Principal) = 300 / (60 + 90) = 300 / 150 = **2.0x**.

**Step 4 — cash generation.**
FCF = CFO − Capex = 220 − 100 = **120**.
FCF/Debt = 120 / 1,050 = **11.4%**.

**Verdict.** 3.5x gross leverage (3.0x net) with 5.0x interest coverage is **levered-but-healthy** — sub-investment grade but not distressed, a **BB / Ba** profile. Lend at a high-yield spread with a maintenance leverage covenant.

**Self-check.** Net < gross leverage (cash subtracted): 3.0x < 3.5x ✓. EBIT < EBITDA coverage (D&A subtracted): 3.5x < 5.0x ✓. DSCR < interest coverage (principal added to denominator): 2.0x < 5.0x ✓. Ordering coherent.

### B2. Stripping a default probability from a spread

A 5-year Meridian bond trades at a **200 bp** spread; convention assumes **50% recovery** (LGD = 50%). Find the implied annual hazard rate and cumulative 5-year default probability.

**Step 1 — credit triangle for the hazard rate.** λ ≈ Spread / LGD = 0.0200 / 0.50 = **4.0% per year**.

**Step 2 — convert to cumulative 5-year PD** using the reduced-form survival formula:
$$P_{\text{survive}} = e^{-\lambda T} = e^{-0.04 \times 5} = e^{-0.20} = 0.8187 \;\Rightarrow\; P_{\text{default}} = 1 - 0.8187 = \mathbf{18.1\%}.$$

**Step 3 — sensitivity to recovery.** If recovery is only **30%** (LGD = 70%), as for a *subordinated* note: λ ≈ 0.0200 / 0.70 = **2.86%**.

**Reconcile.** A *higher* recovery assumption forces a *higher* implied PD to justify the same spread — the joint-identification caveat. The base case (~18% five-year PD) is squarely high-yield, coherent with B1's BB assessment.

### B3. Distance to default (Merton structural model)

A firm has asset value $A_0 = 120$, debt face value $D = 100$, asset drift $\mu = 8\%$, asset volatility $\sigma_A = 25\%$, horizon $T = 1$ year. Compute the distance to default and the model PD.

**Step 1 — distance to default.**
$$\text{DD} = \frac{\ln(A_0/D) + (\mu - \tfrac{1}{2}\sigma_A^2)\,T}{\sigma_A\sqrt{T}}.$$
Numerator: $\ln(1.20) = 0.18232$; drift $= (0.08 - 0.5\times0.25^2) = 0.04875$. So DD $= \dfrac{0.18232 + 0.04875}{0.25} = \dfrac{0.23107}{0.25} = \mathbf{0.924}$.

**Step 2 — default probability.** PD = N(−DD) = N(−0.924) ≈ **0.178** from the standard normal CDF — about a **17.8%** one-year PD.

**Self-check.** Assets sit only 0.92 standard deviations above the default point — thin. A less levered firm ($D = 80$) gives DD ≈ 1.815 and PD = N(−1.815) ≈ 3.5% — far safer. PD falls sharply as leverage falls, as the structural logic requires ✓.

### B4. Fair spread from an agency default table

An agency table says a BB name has a **12% cumulative 5-year default probability** with **40% recovery** (LGD = 60%). What annualized credit spread does this imply?

**Step 1 — back out the constant hazard rate.** Survival = 1 − 0.12 = 0.88 = e^(−5λ), so λ = −ln(0.88)/5 = 0.12783/5 = **2.56%**.

**Step 2 — apply the credit triangle:** Spread ≈ λ × LGD = 0.02557 × 0.60 = **153 bp**.

**Step 3 — cross-check.** Cumulative expected loss = 0.12 × 0.60 = 7.2% over 5 years; ÷5 gives ≈ 144 bp. The two agree within ~9 bp; the exponential-hazard method (153 bp) is more precise as it accounts for compounding survival. Both land near 150 bp for a BB name — tighter than B2's 200 bp, consistent with the different recovery inputs ✓.

### B5. Covenant stress test

Meridian's indenture has a **maintenance covenant**: Debt/EBITDA ≤ **4.0x** each quarter-end. Using B1's figures (Debt 1,050; EBITDA 300; Interest 60), a recession cuts EBITDA by **15%**. Test the covenant and gauge distress.

**Step 1 — recompute leverage after the shock.**
New EBITDA = 300 × (1 − 0.15) = **255**. New Debt/EBITDA = 1,050 / 255 = **4.12x**.

**Step 2 — test the covenant.** 4.12x **exceeds 4.0x** → the maintenance covenant is **breached**. Meridian is in **technical default** despite missing no payment — the early-warning power of a maintenance covenant. The lender can now demand repricing, extra collateral, or acceleration.

**Step 3 — liquidity crisis or ratio breach?** New EBITDA interest coverage = 255 / 60 = **4.25x** (down from 5.0x). Still well above the ~1.5x danger zone, so the firm can *service* its interest — a leverage-*ratio* breach and negotiating event, not yet a missed coupon.

**Self-check.** The 15% drop raised leverage (4.12x > 3.5x) and cut coverage (4.25x < 5.0x) — both move against the creditor, as an earnings decline must ✓.

---

## Section C — Interview-Style (with model answers)

**C1. "You have thirty seconds. How do you decide whether a corporate bond's spread is worth it?"**
Model answer: I frame it as two legs — lending at the risk-free rate plus selling default insurance — and ask whether the spread over-compensates me for the expected loss, PD × LGD. I underwrite capacity through cash-flow-anchored leverage and coverage ratios, check protection through covenants and collateral, and sanity-check character. Then I reconcile my fundamental view against the spread's market-implied view, and lend only when the spread pays more than my honest expected loss plus a premium for its *uncertainty*.

**C2. "Why do you insist on cash flow when the income statement already shows profit?"**
Model answer: Because coupons are paid in cash, and net income can diverge wildly from it — a firm can grow earnings while free cash flow turns negative through uncollected receivables, capitalised costs, or ballooning working capital. EBITDA is my first cash proxy, but it ignores capex, taxes, and working-capital swings, so I reconcile it to cash from operations and then to free cash flow. My job is to find the cash that services the debt, not the accounting story.

**C3. "Walk me through structural versus reduced-form models and when you'd use each."**
Model answer: Structural models — Merton and KMV — say a firm defaults when asset value falls below the debt face value. Equity is a call on assets, so I back out an implied PD from leverage and asset volatility via Black–Scholes, summarised as a distance to default. Their strength is economic insight into *why* spreads widen; their weakness is they need the unobservable asset value and vol, and under-predict short-term spreads. Reduced-form models ignore the balance sheet and treat default as an exogenous jump with a hazard rate calibrated to CDS and bond spreads — tractable for pricing but a-theoretical about causation. I use structural for surveillance, reduced-form for pricing and stripping market-implied PDs.

**C4. "A client says a BBB and a BB bond are basically the same risk one notch apart. Correct them."**
Model answer: One notch on paper, but it straddles the most consequential line in fixed income — the investment-grade floor at BBB−/Baa3. Below it, huge mandate-constrained pools of capital are forbidden to hold the paper, so the transition isn't a gradient; it's a cliff. A downgrade to BB+ makes the bond a fallen angel, and forced selling by insurers, pensions, and index funds widens the spread far beyond what the fundamental change warrants. The default-rate step across that line is discontinuous, not linear.

**C5. "Interest coverage on this credit is 9x. Are you comfortable?"**
Model answer: Not on that number alone. Interest coverage ignores principal — a firm can cover interest nine times and still fail when a maturity wall arrives and refinancing is shut. I'd pull the maturity schedule, compute DSCR to fold in principal, and check liquidity — cash and undrawn revolver against near-term maturities. I'd also stress the earnings: 9x today can become 3x in a downturn if the business is cyclical. Coverage is necessary but never sufficient.

**C6. "What's the one equation you'd never want a credit analyst to forget, and what's its trap?"**
Model answer: The credit triangle — Spread ≈ PD × LGD = λ × (1 − Recovery). Give me a spread and a recovery assumption and I'll hand you the market-implied default probability. The trap is joint identification — PD and recovery are entangled inside one spread, so I can only solve for one by assuming the other. Too high a recovery and I overstate implied PD; too low and I understate it. So I always state the recovery assumption alongside any implied PD.

---

## Section D — Multiple Choice (with reasoning)

**D1.** Debt/EBITDA of 4.0x is best read as:
(a) 4% of assets are debt (b) roughly four years of cash earnings to repay all debt (c) interest is covered four times (d) equity is 4x debt
**Answer: (b).** Debt/EBITDA = years of EBITDA to repay the whole debt if every dollar went to paydown. A leverage measure, not coverage (c) or a capital-structure share (a).

**D2.** Which is always true for the same firm and period?
(a) Net Debt/EBITDA ≥ Gross Debt/EBITDA (b) DSCR ≥ EBITDA interest coverage (c) DSCR ≤ EBITDA interest coverage (d) EBIT coverage ≥ EBITDA coverage
**Answer: (c).** DSCR adds principal to the denominator, so it is never above interest coverage. Netting cash lowers net leverage below gross, killing (a); subtracting D&A lowers EBIT coverage below EBITDA coverage, killing (d).

**D3.** A 200 bp spread with a 50% recovery assumption implies an annual hazard rate of about:
(a) 1.0% (b) 2.0% (c) 4.0% (d) 8.0%
**Answer: (c).** λ ≈ Spread / LGD = 0.0200 / 0.50 = 4.0%. Halving LGD doubles the implied hazard versus a naive spread-equals-PD read.

**D4.** Under a constant hazard rate λ, the probability of default within T years is:
(a) λT (b) 1 − e^(−λT) (c) e^(−λT) (d) λ/T
**Answer: (b).** Survival is e^(−λT), so cumulative default is its complement, 1 − e^(−λT). (c) is the survival probability, and (a) is only the linear first-order approximation.

**D5.** In the Merton model, the firm defaults when:
(a) interest coverage falls below 1.0x (b) asset value at maturity falls below the face value of debt (c) the credit rating is cut to D (d) EBITDA turns negative
**Answer: (b).** Structural models define default as asset value < debt at maturity — where the shareholders' put finishes in the money. The others are accounting or agency signals, not the model's trigger.

**D6.** A maintenance covenant differs from an incurrence covenant in that it is:
(a) tested only when the firm issues new debt (b) never enforceable (c) tested every period regardless of any action (d) applicable only to investment-grade issuers
**Answer: (c).** Maintenance covenants are tested each period, an early-warning tripwire; incurrence covenants (a) are tested only on a specific action. Cov-lite deals drop the maintenance test.

**D7.** LGD is best defined as:
(a) the probability of default (b) 1 − Recovery rate (c) the hazard rate (d) the spread over Treasuries
**Answer: (b).** LGD is the fraction not recovered, 1 − Recovery. PD (a) and λ (c) are separate inputs; the spread (d) is roughly PD × LGD.

**D8.** For the same spread, assuming a *higher* recovery rate implies:
(a) a lower implied PD (b) a higher implied PD (c) no change in implied PD (d) a lower spread
**Answer: (b).** Since Spread ≈ λ × (1 − Recovery), a higher recovery shrinks LGD, so λ must rise to keep the product equal to the spread.

**D9.** A "fallen angel" is a bond that:
(a) rose from junk into investment grade (b) was downgraded from investment grade to high yield (c) defaulted and recovered fully (d) had its coupon cut
**Answer: (b).** A fallen angel crosses the BBB−/BB+ line downward and suffers forced selling by mandate-constrained holders. The reverse is a "rising star" (a).

**D10.** Which statement about credit ratings is TRUE?
(a) A rating is a cardinal default probability (b) A rating is a buy/sell recommendation (c) A rating is an ordinal, through-the-cycle opinion on relative default risk (d) Market spreads are less volatile than ratings
**Answer: (c).** Ratings are ordinal, through-the-cycle opinions — stickier than the point-in-time spread (killing (d)), neither a precise probability (a) nor a price recommendation (b).

**D11.** DSCR is most central in which context?
(a) short-dated Treasury trading (b) project finance and real estate with amortising principal (c) equity valuation (d) money-market funds
**Answer: (b).** DSCR folds principal into the denominator, mattering most where amortising principal is a cash drain. Lenders want DSCR > ~1.25x.

**D12.** Rising asset volatility, holding leverage fixed, tends to:
(a) narrow the credit spread (b) widen the credit spread (c) leave the spread unchanged (d) raise the recovery rate
**Answer: (b).** More asset volatility makes the shareholders' walk-away put more valuable; the bondholder is short that put, so the spread widens — the structural bridge between volatility and spreads.

---

*End of Q&A — Credit Analysis. Numerical answers self-verified: ratio ordering in B1, e^(−0.20) = 0.8187 in B2, DD = 0.924 in B3, −ln(0.88)/5 = 2.56% in B4, breach 4.12x > 4.0x in B5.*
