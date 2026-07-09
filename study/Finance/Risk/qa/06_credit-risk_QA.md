# Q&A — Credit Risk

A practice bank for the Credit Risk chapter. Work each question before reading the answer. Numerical answers are self-checked against the master identities EL = PD × LGD × EAD and UL = EAD × LGD × √(PD(1−PD)).

---

## Section A — Concept-Check (short answer)

**A1. State the master identity of credit risk and define each term.**

Expected Loss: **EL = PD × LGD × EAD**.
- **PD** = Probability of Default over a horizon (usually 1 year), between 0 and 1.
- **LGD** = Loss Given Default = 1 − Recovery Rate; the fraction of exposure not recovered.
- **EAD** = Exposure at Default; the money amount outstanding when default occurs.
The three factors compound because each answers a logically independent question: *how likely* is default, *how much* is at risk when it happens, and *how severe* is the loss on that amount.

**A2. Why is Expected Loss described as "a cost, not a risk"?**

Because EL is the *average* outcome, which is predictable and repeatable. A bank that expects to lose 1.5% of its book each year is not being surprised — it should price that 1.5% into its lending rate and set it aside as a provision. The genuine risk is the *deviation above* that mean (Unexpected Loss), i.e. the chance that this year's losses come in far worse than the long-run average. Treating EL as "the risk" leads to holding zero capital for the part that actually threatens solvency.

**A3. What does Unexpected Loss (UL) represent and what covers it?**

UL is the volatility (standard deviation) of losses around the expected mean — the possibility that realised losses exceed EL. It is covered by **capital** (equity), whereas EL is covered by **provisions**. The division of labour: *provisions cover the mean, capital covers the tail.*

**A4. Why do defaults "bunching together" matter more than individual default odds?**

A single borrower defaulting is idiosyncratic and diversifiable. Thousands defaulting at once (a recession, a sector collapse) is systematic and is what generates the fat right tail of the loss distribution. Portfolio capital is sized off this correlated tail, so **default correlation — not the individual PDs — sets the capital number.** Idiosyncratic risk can be diversified away; systematic risk cannot.

**A5. Distinguish LGD from Recovery Rate, and give the trap.**

LGD = 1 − Recovery Rate. If a defaulted loan recovers 40 cents on the rupee, the recovery rate is 40% and **LGD is 60%, not 40%.** Always check which figure the question gives you before plugging in.

**A6. What is a Credit Conversion Factor (CCF) and why does it matter?**

CCF is the fraction of an *undrawn* commitment expected to be drawn before default. It matters because distressed borrowers draw down their credit lines precisely as they head toward default, so exposure balloons exactly when it hurts. EAD on a revolver = Drawn + CCF × (Limit − Drawn). Ignoring it and using only the drawn balance systematically understates exposure.

**A7. What is a rating transition matrix, and how do you get a multi-year PD from it?**

A transition (migration) matrix gives the probability of moving from one rating grade to another over one year; rows are the start grade, columns the end grade, the last column is default (D), and each row sums to 100%. The default column gives the 1-year PD per grade. Assuming a time-homogeneous Markov chain, the **n-year matrix is Mⁿ** — the 2-year matrix is M², and the 2-year cumulative PD for a grade is read from the D column of M².

**A8. Distinguish through-the-cycle (TTC) from point-in-time (PIT) PD.**

TTC PD is a long-run average that smooths over booms and busts; it is used for Basel regulatory capital and rating-agency grades. PIT PD reflects current conditions and rises in recessions; it is used for IFRS 9 / Ind AS 109 expected credit loss accounting. TTC is stable; PIT is cyclical.

**A9. Why is spread-implied PD "risk-neutral" and how does it compare to the actual default frequency?**

PD backed out of a bond or CDS spread embeds a risk premium and a liquidity premium on top of pure expected loss, so it is a *risk-neutral* probability that is typically **higher** than the physical (real-world) default frequency. You must not feed a spread-implied PD into an accounting ECL model that wants a real-world PD.

**A10. What is Economic Capital in terms of Credit VaR?**

Economic Capital = Credit VaR(α) − EL. Credit VaR is a high percentile (Basel uses 99.9%) of the loss distribution; we subtract EL because provisions already cover the mean, so capital only needs to bridge from the mean out to the chosen confidence level.

---

## Section B — Numerical / Applied (full solutions)

**B1. Basic Expected Loss.** A bank lends ₹80 crore, fully drawn, to a borrower with 1-year PD = 2%. The loan is secured with an expected recovery of 55%. Find EL.

LGD = 1 − 0.55 = 0.45. EAD = ₹80 cr (fully drawn).
EL = PD × LGD × EAD = 0.02 × 0.45 × 80 = **₹0.72 crore** (₹72 lakh).
*Check:* 0.02 × 0.45 = 0.009; 0.009 × 80 = 0.72. ✓ The bank should provision ₹72 lakh and build 0.9% into the spread to break even on expected credit cost.

**B2. Unexpected Loss (default-event only).** For the loan in B1, compute UL using UL = EAD × LGD × √(PD(1−PD)).

√(0.02 × 0.98) = √0.0196 = 0.14.
UL = 80 × 0.45 × 0.14 = **₹5.04 crore**.
*Check via the ratio identity:* UL/EL = √((1−PD)/PD) = √(0.98/0.02) = √49 = 7.0, so UL = 7.0 × 0.72 = 5.04. ✓ UL is 7× the EL — the unexpected loss dwarfs the expected loss because the default event is binary and volatile.

**B3. UL with recovery volatility.** Same loan (EAD 80, PD 0.02, LGD 0.45) but now the standard deviation of LGD is σ_LGD = 0.25. Use the fuller formula UL = EAD × √(PD·σ_LGD² + LGD²·PD(1−PD)).

Inside the root: PD·σ_LGD² = 0.02 × 0.0625 = 0.00125; LGD²·PD(1−PD) = 0.2025 × 0.0196 = 0.0039690. Sum = 0.0052190. √0.0052190 = 0.07224.
UL = 80 × 0.07224 = **₹5.78 crore**.
*Check:* adding recovery-rate variance raised UL from ₹5.04 cr to ₹5.78 cr — correct direction, since uncertainty about *how much* you recover adds to the risk on top of the binary default event. ✓

**B4. EAD on a revolver.** A firm has a ₹60 crore revolving facility, ₹25 crore drawn. Distressed borrowers historically draw 70% of the remaining commitment (CCF = 0.70). PD = 3%, LGD = 50%. Find EAD and EL, and compare against naively using the drawn balance.

Undrawn = 60 − 25 = 35. EAD = 25 + 0.70 × 35 = 25 + 24.5 = **₹49.5 crore**.
EL = 0.03 × 0.50 × 49.5 = **₹0.7425 crore** (≈ ₹74.25 lakh).
*Naive (drawn only):* EL = 0.03 × 0.50 × 25 = ₹0.375 cr. Using the drawn balance would understate the risk by about half. ✓ The undrawn commitment is a real, dangerous exposure.

**B5. Portfolio UL and diversification.** Two loans have standalone UL₁ = ₹3 cr and UL₂ = ₹5 cr. Compute portfolio UL for (a) ρ = 0, (b) ρ = 0.30, (c) ρ = 1, and state the diversification benefit in case (b).

Formula: UL_P = √(UL₁² + UL₂² + 2ρ·UL₁·UL₂). UL₁² = 9, UL₂² = 25, 2·UL₁·UL₂ = 30.
- (a) ρ=0: √(9 + 25 + 0) = √34 = **₹5.83 cr**.
- (b) ρ=0.30: √(34 + 0.30×30) = √(34 + 9) = √43 = **₹6.56 cr**.
- (c) ρ=1: √(34 + 30) = √64 = **₹8.00 cr** = the arithmetic sum 3+5. ✓
Diversification benefit in (b) = arithmetic sum − portfolio UL = 8.00 − 6.56 = **₹1.44 cr** of UL saved. All three cases sit correctly between the fully diversified ₹5.83 cr and the perfectly correlated ₹8.00 cr, rising with ρ. ✓

**B6. Market-implied PD from a spread.** A corporate bond trades at a 250 bps spread over the risk-free rate; assume LGD = 50%. Estimate the risk-neutral PD, then verify.

PD ≈ s / LGD = 0.025 / 0.50 = **0.05 = 5.0%**.
*Check:* implied EL = PD × LGD = 0.05 × 0.50 = 0.025 = 250 bps = the spread we started with. ✓ The market is pricing the bond to compensate for expected credit loss (ignoring risk/liquidity premia, which push the real-world PD below this 5%).

**B7. Two-year cumulative PD from a survival argument.** A BB-rated name has a 1-year marginal PD of 1.10% in year 1 and a (conditional) 1.30% in year 2. Compute the 2-year cumulative PD.

Survive year 1: 1 − 0.011 = 0.989. Survive year 2 given survival: 1 − 0.013 = 0.987. Two-year survival = 0.989 × 0.987 = 0.976143. Cumulative 2-year PD = 1 − 0.976143 = **0.023857 ≈ 2.39%**.
*Check:* it is slightly less than the naive sum 1.10% + 1.30% = 2.40%, because you can only default in year 2 if you survived year 1. The tiny gap (0.01%) equals 0.011 × 0.013. ✓

**B8. Economic Capital.** A portfolio has EL = ₹12 crore and a 99.9% Credit VaR of ₹85 crore. What economic capital is required?

Economic Capital = Credit VaR − EL = 85 − 12 = **₹73 crore**. Provisions of ₹12 cr already cover the mean; the ₹73 cr of capital covers the unexpected loss out to the 99.9% confidence level.

**B9. RAROC loan-pricing decision.** A ₹100 cr loan earns spread income + fees of ₹3.0 cr per year, has EL of ₹0.5 cr and operating cost of ₹0.3 cr. Economic capital held is ₹15 cr, and the bank's hurdle (cost of equity) is 14%. Should the loan be approved?

RAROC = (Spread + Fees − EL − Operating cost) / Economic Capital = (3.0 − 0.5 − 0.3) / 15 = 2.2 / 15 = **14.67%**.
Since 14.67% > 14% hurdle, the loan clears the cost of equity and should be **approved** (marginally). *Check:* had economic capital been ₹16 cr, RAROC = 2.2/16 = 13.75% < 14% and it would be rejected — showing how sensitive the decision is to capital consumption. ✓

**B10. Provision vs capital split.** A bank's loan book has aggregate EL = ₹40 cr and UL = ₹120 cr, and it holds economic capital equal to 4 × UL. State the provision, the capital, and why they are not double-counted.

Provisions = EL = **₹40 cr** (against the mean, a P&L charge). Capital = 4 × 120 = **₹480 cr** (equity, against the tail). They are separate, stacked buffers: provisions reduce book value for the expected cost; capital absorbs the deviation above it. Conflating them would mis-size the balance sheet — you need *both*.

---

## Section C — Interview-Style (model answers)

**C1. "Walk me through what happens to expected loss versus capital when a loan's PD doubles."**

EL is linear in PD, so doubling PD roughly **doubles EL** — a proportional rise in the cost you price and provision for. Capital is driven by *unexpected* loss and the conditional stressed PD, which scale with √(PD(1−PD)) at the single-name level and, more importantly, with the *correlated tail* at the portfolio level — so capital rises too, but not linearly. The more damaging effect is that a broad PD increase usually coincides with rising correlation in a downturn, so the tail fattens faster than the mean. Headline: EL responds proportionally and predictably; capital responds through volatility and correlation, which is why a stress event hurts capital far more than a simple doubling of the average suggests.

**C2. "Why can't I just add up the unexpected losses of my loans the way I add expected losses?"**

Because expectations always add regardless of correlation — E[A+B] = E[A]+E[B] — so portfolio EL is a clean sum. But UL is a standard deviation, and standard deviations combine like volatilities: UL_P = √(UL₁² + UL₂² + 2ρ·UL₁·UL₂). Unless ρ = 1, the portfolio UL is strictly *less than* the arithmetic sum, and the gap is the diversification benefit. Adding ULs directly would overstate required capital and completely ignore the only free lunch in credit. Concretely, two ₹4 cr ULs at ρ = 0 combine to √32 = ₹5.66 cr, not ₹8 cr.

**C3. "A borrower has an undrawn line. Our system books zero exposure until they draw. What's wrong with that?"**

It ignores the single most predictable behaviour in credit distress: borrowers draw down their committed lines as they slide toward default, because a committed facility is contractual liquidity they can't be denied. So exposure is smallest when the borrower is healthy and largest at the moment of default — exactly the wrong correlation. We model this with a Credit Conversion Factor: EAD = Drawn + CCF × (Limit − Drawn). A facility that looks like zero exposure today can convert to tens of crores at default. Booking zero until drawdown means we hold zero provision and zero capital against a real, and adversely-timed, exposure.

**C4. "Explain the difference between the PD you'd read off a CDS spread and the PD you'd use for IFRS 9 provisioning."**

The CDS/bond-implied PD is *risk-neutral*: it's extracted from prices, so it bundles the pure default probability with a risk premium (investors demand extra return to bear default risk) and a liquidity premium. That makes it systematically higher than the actual physical default frequency. IFRS 9 expected credit loss wants a *real-world, point-in-time* PD — your best forecast of what will actually happen, forward-looking and conditioned on the current cycle. Feeding a risk-neutral spread-implied PD into an ECL model would overstate provisions, and mixing the two is a classic error. Rule of thumb: risk-neutral PD for pricing and hedging, real-world PD for accounting and economic capital.

**C5. "Our whole loan book is in one booming sector and it's performing beautifully. Why are you worried?"**

Because performance today tells you about the *mean* (low realised EL in a good year), not the *tail*. Concentrating in one sector means borrowers share a common systematic factor — the sector's fortunes — so default correlation is high, and high correlation is exactly what fattens the loss tail: in the good state everyone pays, but in the bad state they default together and wipe out years of spread at once. Diversification removes idiosyncratic risk; concentration leaves the systematic risk fully intact. A book that looks safe on average can be lethal on its tail — concentration is the standard way banks die (IL&FS, DHFL). I'd want single-name and sector limits and a sector-wide stress test, not comfort from clean current performance.

**C6. "What is the Merton model intuition, in one minute?"**

Treat a firm's equity as a call option on its assets: shareholders get whatever is left after debt is repaid, and their downside is capped at zero (limited liability). The firm defaults if asset value V falls below the debt face value F at maturity. The key output is distance-to-default — how many standard deviations of asset value the firm sits above its default point: DD = [ln(V/F) + (μ − ½σ²)T] / (σ√T), and PD = N(−DD). It links equity-market information (asset value and volatility, inferred via Black-Scholes) directly to credit risk, and it's the engine behind Moody's KMV EDF. The practical appeal: it updates in real time from the stock price rather than waiting for a rating action.

**C7. "Provisions and capital — aren't they just two names for the same rainy-day fund?"**

No — they sit against different parts of the loss distribution and come from different pools. Provisions are an accounting charge against Expected Loss, the mean of the distribution; they reduce reported earnings and carrying value for a cost you already expect. Capital is shareholders' equity held against Unexpected Loss, the deviation above the mean out to a high confidence level; it exists to absorb the bad years. They stack: EL first (provisions), then UL (capital), then the extreme stress zone beyond capital where banks actually fail. Conflating them either under-provisions (you carry loans at inflated value) or under-capitalises (you have no buffer for the tail).

---

## Section D — MCQs (with reasoning)

**D1.** A loan has PD = 4%, recovery rate = 70%, EAD = ₹50 cr. Expected Loss is:
(a) ₹1.40 cr  (b) ₹0.60 cr  (c) ₹1.00 cr  (d) ₹2.00 cr

**Answer: (b).** LGD = 1 − 0.70 = 0.30. EL = 0.04 × 0.30 × 50 = ₹0.60 cr. The trap is (a), which wrongly uses LGD = 0.70 (the recovery, not the loss): 0.04 × 0.70 × 50 = ₹1.40 cr. Always convert recovery to LGD first.

**D2.** Which is covered by *capital* rather than *provisions*?
(a) Expected Loss  (b) Unexpected Loss  (c) Operating cost  (d) Funding cost

**Answer: (b).** Provisions cover the mean (EL); capital covers the volatility around the mean (UL). Operating and funding costs are ordinary expenses recovered in the loan's pricing, not risk buffers.

**D3.** Two loans each have standalone UL = ₹6 cr. At a default correlation of ρ = 1, the portfolio UL is:
(a) ₹6 cr  (b) ₹8.49 cr  (c) ₹12 cr  (d) ₹0 cr

**Answer: (c).** At ρ = 1, √(36 + 36 + 2×1×36) = √144 = ₹12 cr, which equals the arithmetic sum 6 + 6 — perfect correlation gives zero diversification benefit. Option (b) √72 = 8.49 is the ρ = 0 case; the maximum diversification, not the minimum.

**D4.** A revolving facility has limit ₹40 cr, drawn ₹10 cr, CCF = 0.50. EAD is:
(a) ₹10 cr  (b) ₹25 cr  (c) ₹40 cr  (d) ₹30 cr

**Answer: (b).** EAD = 10 + 0.50 × (40 − 10) = 10 + 15 = ₹25 cr. Option (a) ignores the undrawn commitment; (c) wrongly assumes the full line is drawn (CCF = 1).

**D5.** A bond's credit spread is 180 bps and assumed LGD is 45%. The approximate risk-neutral PD is:
(a) 2.0%  (b) 4.0%  (c) 8.1%  (d) 0.81%

**Answer: (b).** PD ≈ s / LGD = 0.018 / 0.45 = 0.04 = 4.0%. Check: PD × LGD = 0.04 × 0.45 = 0.018 = 180 bps, recovering the spread. Option (c) multiplies instead of dividing.

**D6.** In a rating transition matrix, the 2-year cumulative default probabilities are obtained from:
(a) 2M  (b) M²  (c) M/2  (d) the last row of M

**Answer: (b).** For a time-homogeneous Markov chain the n-year matrix is Mⁿ, so the 2-year matrix is M² and 2-year cumulative PDs are read from its default column. Option (a) 2M is not even a valid probability matrix (rows wouldn't sum to 1).

**D7.** Which PD is appropriate for Basel regulatory capital?
(a) Point-in-time  (b) Risk-neutral  (c) Through-the-cycle  (d) Spread-implied

**Answer: (c).** Basel regulatory capital uses through-the-cycle PD (a stable long-run average). Point-in-time is for IFRS 9 ECL; risk-neutral/spread-implied PDs are for pricing and hedging, not capital.

**D8.** Economic capital is best defined as:
(a) Credit VaR  (b) Expected Loss  (c) Credit VaR − Expected Loss  (d) Unexpected Loss × PD

**Answer: (c).** Economic Capital = Credit VaR(α) − EL, because provisions already absorb EL and capital need only bridge from the mean out to the confidence level. Option (a) double-counts the EL that provisions already cover.

**D9.** Which statement about diversification in a credit portfolio is TRUE?
(a) It removes all credit risk  (b) It removes only idiosyncratic risk, leaving systematic risk  (c) It has no effect when ρ < 1  (d) It increases the tail loss

**Answer: (b).** Diversification cancels name-specific (idiosyncratic) risk but leaves the common systematic factor untouched — that residual correlated risk is exactly what portfolio capital is sized against. (a) overclaims; (c) is backwards (diversification helps most when ρ < 1); (d) is the opposite of the truth.

**D10.** For a single risky loan with a low PD, the ratio UL/EL is approximately:
(a) always 1  (b) √((1−PD)/PD), which is large for small PD  (c) PD × LGD  (d) always less than 1

**Answer: (b).** Using EL = PD·LGD·EAD and UL = EAD·LGD·√(PD(1−PD)), the LGD and EAD cancel: UL/EL = √(PD(1−PD)) / PD = √((1−PD)/PD). For small PD this is large (e.g. PD = 1% gives √99 ≈ 9.95), which is why UL dwarfs EL for a single low-PD loan. This is the quantitative core of "expected loss is a cost, unexpected loss is the risk."

---

*End of Q&A — Credit Risk.*
