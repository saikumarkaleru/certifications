# Q&A — Credit Risk and Spreads

A companion practice bank for Chapter 10. Every question is followed by a full answer. Unless stated otherwise, rates are **annually compounded**, spreads are quoted in **basis points (bp)**, and the workhorse relations are: expected loss $EL = PD \times LGD \times EAD$, loss given default $LGD = 1 - R$, cumulative default $PD_{\text{cum}}(t) = 1-(1-\lambda)^t$, and the credit triangle $s \approx \lambda \times LGD$.

---

## Section A — Concept Check

**A1. What exactly is a credit spread, and why must it be positive for a risky bond?**
A credit spread is the extra yield per year a risky bond offers over an otherwise-identical default-free benchmark: $\text{risky yield} = \text{risk-free rate} + \text{spread}$. It must be positive because the risky bond might not pay in full or on time, so investors will only buy it at a lower price (higher yield) than the safe bond. The spread is compensation, not free profit — it pays for expected loss plus a risk premium plus a liquidity premium. If the spread were zero, no-arbitrage would say the two bonds are identical claims, which they are not.

**A2. Decompose the credit spread into its economic parts.**
$\text{spread} \approx \text{expected loss} + \text{credit risk premium} + \text{liquidity premium}$. The expected-loss piece ($PD \times LGD$ annualized) is the actuarial cost of default. The risk premium rewards investors for bearing the *uncertainty* of the outcome (they are risk-averse, not risk-neutral). The liquidity premium compensates for corporates being harder to sell than Treasuries. This is why observed spreads sit consistently *above* realized default losses — the gap is the credit investor's historical edge.

**A3. Define PD, LGD, EAD, and recovery, and give the relations among them.**
PD is the probability of default over a horizon. LGD is the fraction of exposure lost if default occurs. EAD is the amount at risk when default hits (roughly face plus accrued for a plain bond). Recovery rate $R$ is cents-on-the-dollar recovered, so $LGD = 1 - R$ — they are the *same* information stated two ways. Together, $EL = PD \times LGD \times EAD$.

**A4. What is a hazard rate, and why isn't cumulative PD just $\lambda \times t$?**
The hazard rate $\lambda$ is the *conditional* probability of defaulting during a period given survival to its start. Cumulative PD by time $t$ is $1-(1-\lambda)^t$, which is *below* $\lambda t$ because to default in a later year you must first survive every earlier year. The linear approximation $\lambda t$ only holds for small $\lambda$ and short horizons; over long horizons it overstates default probability.

**A5. What is the biggest driver of the recovery rate?**
Seniority and collateral. Senior secured debt might recover 60–70 cents; senior unsecured around 40 cents (the common rule-of-thumb); subordinated debt 20 cents or less. Where you sit in the capital structure, and whether specific assets back the claim, dominate LGD far more than the identity of the issuer.

**A6. Explain the ladder of spread measures and what each rung strips out.**
From least to most precise: **G-spread** (corporate YTM minus a matching-maturity government YTM — one blended yield vs one blended yield); **I-spread** (same, but over the swap curve); **Z-spread** (a constant add-on to *every* benchmark spot rate that reprices the bond — curve-consistent); **OAS** (the Z-spread after an embedded option's value is modelled out). Each rung removes one distortion: curve shape, then reference base, then optionality — leaving a cleaner read on pure credit-plus-liquidity compensation.

**A7. State the credit triangle and say what it is used for.**
$s \approx \lambda \times (1-R) = \lambda \times LGD$: spread approximately equals default intensity times loss given default. It is the reduced-form bridge for moving between a quoted market spread and an implied default probability, and it links cash-bond spreads to the CDS market.

**A8. What is credit migration, and why does it matter more than default for an IG portfolio?**
Credit migration is a change in an issuer's rating/quality while you hold the bond. A downgrade from BBB to BB misses no coupon, yet the price falls because the market now demands a wider spread. For a diversified investment-grade portfolio — where outright defaults are rare — year-to-year mark-to-market volatility is driven far more by these migration and general spread moves than by the handful of names that actually default. "You only lose money if it defaults" is the single most expensive misconception in credit.

**A9. Structural vs reduced-form models — one line each.**
Structural (Merton): a firm defaults when asset value falls below the face value of debt; equity is a call option on the firm's assets, so credit risk rises with leverage and asset volatility. Reduced-form: treat default as a random event arriving with hazard rate $\lambda$ calibrated directly from market prices (spreads, CDS). Reduced-form dominates day-to-day pricing because it fits observed spreads by construction.

**A10. How do spreads behave over the business cycle?**
Counter-cyclically. They tighten in expansions (strong earnings, few defaults, yield-hunting), begin widening late-cycle as leverage builds, and blow out in recessions — crucially by *more* than expected losses alone justify, because risk and liquidity premiums both surge in stress. They then mean-revert tighter in recovery, usually the best period for credit *returns* (carry plus tightening gains).

---

## Section B — Numerical Bond-Math Problems (step-by-step, reconciling)

**B1. Expected loss and the fair spread.** A one-year bond, face 100, hazard 2%, recovery 40%. Find LGD, expected loss, and the actuarial fair spread; confirm with the credit triangle.
Step 1 — LGD $= 1 - 0.40 = 0.60$.
Step 2 — $EL = PD \times LGD = 0.02 \times 0.60 = 0.012 = 1.20\%$ of face = **120 bp**.
Step 3 — Credit-triangle check: $s \approx \lambda \times LGD = 0.02 \times 0.60 = 0.012 =$ **120 bp** ✓. Both routes agree.
Interpretation: if the bond actually trades at 200 bp, ~120 bp covers expected loss and the remaining ~80 bp is risk plus liquidity premium.

**B2. Cumulative vs marginal PD over three years.** Constant hazard $\lambda = 3\%$. Find cumulative PD by years 2 and 3 and the marginal PD in year 3; reconcile.
Survival each year $= 0.97$.
$PD_{\text{cum}}(2) = 1 - 0.97^2 = 1 - 0.9409 = 0.0591 = \mathbf{5.91\%}$.
$PD_{\text{cum}}(3) = 1 - 0.97^3 = 1 - 0.912673 = 0.087327 = \mathbf{8.73\%}$.
$PD_{\text{marg}}(3) = 0.97^2 \times 0.03 = 0.9409 \times 0.03 = 0.028227 = \mathbf{2.82\%}$.
Reconcile: $PD_{\text{cum}}(3) = PD_{\text{cum}}(2) + PD_{\text{marg}}(3) = 0.0591 + 0.028227 = 0.087327$ ✓. Note the naive $3 \times 3\% = 9\%$ overstates the true 8.73%, because you can only default in year 3 if you survived years 1 and 2.

**B3. Implied hazard from a quoted spread (credit triangle in reverse).** A bond trades at a 300 bp spread; assumed recovery is 25%. Back out the implied annual default intensity.
$LGD = 1 - 0.25 = 0.75$.
$\lambda \approx \dfrac{s}{LGD} = \dfrac{0.03}{0.75} = 0.04 = \mathbf{4.0\%}$.
Reconcile forward: $s \approx \lambda \times LGD = 0.04 \times 0.75 = 0.03 =$ 300 bp ✓. A higher assumed recovery would imply a *higher* hazard for the same spread — with less lost per default, more defaults are needed to justify the same compensation.

**B4. Solve for a Z-spread by trial and interpolation.** A 2-year bond pays a **6% annual coupon** on face 100 and trades at **99.1163**. Benchmark spot rates are 1-yr 3.00%, 2-yr 3.50%. Find the Z-spread.
Set up: $99.1163 = \dfrac{6}{(1.03+Z)} + \dfrac{106}{(1.035+Z)^2}$.
Trial $Z = 2.00\%$ → rates 5.0%, 5.5%: $\frac{6}{1.05} + \frac{106}{1.055^2} = 5.7143 + 95.2359 = 100.950$ (too high).
Trial $Z = 4.00\%$ → rates 7.0%, 7.5%: $\frac{6}{1.07} + \frac{106}{1.075^2} = 5.6075 + 91.7266 = 97.333$ (too low).
Trial $Z = 3.00\%$ → rates 6.0%, 6.5%: $\frac{6}{1.06} + \frac{106}{1.065^2} = 5.6604 + 93.4559 = 99.1163$ ✓.
The present value hits the market price exactly at $Z = \mathbf{300\ bp}$.

**B5. Reconcile a Z-spread against a G-spread on a mild curve.** A 3-year bond pays a **5% annual coupon**, face 100, price **98.739**; benchmark spots are 3.00%, 3.50%, 4.00%.
Z-spread: at $Z = 1.50\%$ the discount rates are 4.5%, 5.0%, 5.5%:
$\frac{5}{1.045} + \frac{5}{1.05^2} + \frac{105}{1.055^3} = 4.7847 + 4.5351 + 89.4194 = 98.739$ ✓ → **Z = 150 bp**.
G-spread: the corporate YTM solving the price is $y_{\text{corp}} \approx 5.47\%$. A default-free 3-year 5% bond priced off the *same* spots ($Z=0$) is worth $\frac{5}{1.03}+\frac{5}{1.035^2}+\frac{105}{1.04^3} = 102.867$, whose YTM is $y_{\text{govt}} \approx 3.97\%$. So $\text{G-spread} = 5.47\% - 3.97\% = \mathbf{150\ bp}$.
Reconcile: G-spread and Z-spread coincide (150 bp) *only because the curve is gently sloped*. On a steep curve they would diverge, and the Z-spread — which respects the whole term structure — is the number to trust.

**B6. OAS from a Z-spread for callable and putable bonds.**
(a) Callable bond: Z-spread = 220 bp, modelled call cost = 60 bp. $\text{OAS} = 220 - 60 = \mathbf{160\ bp}$. The investor is *short* the call, so its value is subtracted — OAS < Z-spread.
(b) Putable bond: Z-spread = 180 bp, modelled put value = 40 bp. $\text{OAS} = 180 + 40 = \mathbf{220\ bp}$. The investor is *long* the put (a benefit), so its value is added back — OAS > Z-spread.
Check the direction: for an *option-free* bond both option terms are zero, so OAS = Z-spread. Consistent ✓.

**B7. Credit migration — expected value and its decomposition.** You hold a BBB bond worth 100. Over one year:

| State | Probability | Value | Prob × Value |
|---|---|---|---|
| Upgrade to A | 5% | 101.0 | 5.050 |
| Stay BBB | 88% | 100.0 | 88.000 |
| Downgrade to BB | 5% | 96.5 | 4.825 |
| Default | 2% | 40.0 | 0.800 |
| **Total** | **100%** | | **98.675** |

Expected value = **98.675**, an expected change of **−1.325**.
Decompose (probability × change from 100): upgrade $0.05\times(+1)=+0.050$; stay $0$; downgrade $0.05\times(-3.5)=-0.175$; default $0.02\times(-60)=-1.200$. Sum $= +0.050 - 0.175 - 1.200 = \mathbf{-1.325}$ ✓.
Interpretation: default (−1.20) is the single biggest drag, but the migration states together move value by −0.125 *with no missed payment*. Scale that across a large IG book where default is rare and migration dominates the mark-to-market swings.

**B8. Spread duration P&L.** A bond has spread duration 4.5 and its spread widens by 80 bp with the risk-free curve unchanged. Estimate the price impact.
$\Delta P/P \approx -(\text{spread duration}) \times \Delta s = -4.5 \times 0.0080 = -0.036 = \mathbf{-3.6\%}$.
Reconcile the concept: spread duration is the analogue of interest-rate duration but for a move in the *spread* only. An 80 bp widening on a 4.5-duration bond costs about 3.6 points per 100 of price — and it happens whether or not the bond ever defaults.

---

## Section C — Interview-Style (with model answers)

**C1. "Why is a corporate bond's spread wider than its expected default loss?"**
Model answer: Expected loss ($PD \times LGD$) is only the actuarial floor. Investors are risk-averse, so they demand a premium for bearing the *uncertainty* of default timing and severity, not just its average. On top of that, corporates are less liquid than Treasuries, so there's a liquidity premium. Empirically, high-grade spreads have exceeded realized default losses by a comfortable margin over long horizons — that persistent gap is precisely the excess return credit investors have historically earned. So when I see a 200 bp spread on a name whose expected loss is 120 bp, I don't call it mispriced; I ask whether the 80 bp of premium adequately compensates for the risk and illiquidity I'm taking.

**C2. "Walk me through the difference between a Z-spread and an OAS, and when they diverge."**
Model answer: The Z-spread is the constant number you add to every point on the benchmark spot curve so the discounted cash flows equal the market price — it's curve-consistent and it's the right measure for an option-free bond. But if the bond has an embedded option, the Z-spread is contaminated by that option's value. The OAS strips the option out using an interest-rate model that averages the bond's value across many simulated rate paths, leaving a spread that's comparable across bonds regardless of their option features. For a callable bond the OAS is *below* the Z-spread — the investor is short the call, so you subtract its value. For a putable bond the OAS is *above* the Z-spread — the put benefits the investor. For an option-free bond they're identical. So the moment I'm comparing a callable to a bullet, I insist on OAS, not Z-spread.

**C3. "A junior analyst says the two-year default probability on a 2% hazard name is 4%. Correct them."**
Model answer: That's the linear approximation, and it double-counts. To default in year two you must first survive year one. Survival each year is $1-0.02 = 0.98$, so cumulative default by year two is $1 - 0.98^2 = 3.96\%$, not 4%. The marginal probability of defaulting *in* year two is $0.98 \times 0.02 = 1.96\%$, and it reconciles: year-one default 2.00% plus year-two marginal 1.96% equals the cumulative 3.96%. The $\lambda t$ shortcut is fine for a quick mental estimate at small hazards and short horizons, but over long maturities or high-yield names it materially overstates default risk, so I'd never use it for pricing.

**C4. "How would you translate a market spread into an implied default probability?"**
Model answer: The credit triangle: spread $\approx$ hazard rate times loss given default, $s \approx \lambda \times LGD$. So the implied hazard is $\lambda \approx s / LGD$. If a name trades at 300 bp and I assume a 40% recovery — so LGD is 0.60 — the implied annual default intensity is roughly 0.03/0.60 = 5%. The key caveat is the recovery assumption: it's an input, not an observable, and the implied hazard is quite sensitive to it. A higher assumed recovery implies a higher hazard for the same spread, because each default costs less, so more of them are needed to justify the compensation. In practice I'd calibrate against the CDS curve, where the same triangle links the CDS premium to $\lambda$ and LGD, and watch the CDS-bond basis.

**C5. "Where do most credit losses actually come from in an investment-grade portfolio?"**
Model answer: Not from default — from spread widening and downgrades, i.e. migration. In an IG book, actual defaults are rare in any given year, but every name is marked to market, and a downgrade from, say, BBB to BB widens the spread the market demands and drops the price several points with no coupon missed. Over a one-year horizon, the mark-to-market volatility of a diversified IG portfolio is dominated by these migration and general spread moves, not by the one or two names that default. That's why credit risk management focuses on transition matrices and spread duration, and why credit VaR is built from the whole distribution of next-year values across rating states, not just the default state.

**C6. "The economy is heading into a recession. What happens to spreads, and why more than the models say?"**
Model answer: Spreads widen — they're counter-cyclical, tightest in booms and widest in recessions. But the important point for a trader is that they blow out by *more* than the rise in expected losses alone would justify. Two premiums surge simultaneously in stress: the risk premium, because investors become more risk-averse exactly when uncertainty is highest, and the liquidity premium, because dealers pull back and forced sellers can't find bids. So the spread overshoots fair value. That overshoot is painful if you're already long, but it's also why the recovery phase tends to deliver the best credit *returns* — you earn the carry plus capital gains as spreads mean-revert tighter. The relationship with equities is tight too: a VIX spike almost always comes with wider credit spreads, because both are pricing the same underlying fear.

---

## Section D — Multiple Choice (with reasoning)

**D1.** A bond has PD = 4%, recovery = 30%, EAD = 100. Its one-period expected loss is closest to:
(a) 1.2 (b) 2.8 (c) 4.0 (d) 3.0
**Answer: (b).** $EL = PD \times LGD \times EAD = 0.04 \times (1-0.30) \times 100 = 0.04 \times 0.70 \times 100 = 2.8$. Choice (a) forgets the LGD, (c) forgets both LGD and uses PD directly, (d) mistakenly uses recovery instead of LGD.

**D2.** With a constant hazard $\lambda = 5\%$, cumulative default probability over 3 years is closest to:
(a) 15.0% (b) 14.3% (c) 5.0% (d) 4.75%
**Answer: (b).** $1 - 0.95^3 = 1 - 0.857375 = 0.142625 = 14.3\%$. Choice (a) is the naive $\lambda t$, which overstates because you must survive earlier years to default later.

**D3.** For a callable bond, the OAS is:
(a) larger than the Z-spread (b) smaller than the Z-spread (c) equal to the Z-spread (d) always negative
**Answer: (b).** OAS = Z-spread − call cost. The investor is short the call, so its value is subtracted, leaving OAS below the Z-spread. For a *putable* bond the relationship reverses.

**D4.** Which is the correct relationship between recovery and LGD?
(a) $LGD = R$ (b) $LGD = 1 + R$ (c) $LGD = 1 - R$ (d) they are unrelated
**Answer: (c).** Loss given default is the fraction *not* recovered, $1 - R$. They carry the same information stated two ways.

**D5.** The Z-spread is best described as:
(a) the corporate YTM minus one government YTM (b) a constant added to every benchmark spot rate so the discounted cash flows equal the market price (c) the spread after removing embedded-option value (d) the spread over the swap curve
**Answer: (b).** That's the definition of the zero-volatility spread. (a) is the G-spread, (c) is the OAS, (d) is the I-spread.

**D6.** The credit triangle states that a bond's spread is approximately:
(a) $\lambda / LGD$ (b) $\lambda \times LGD$ (c) $\lambda + LGD$ (d) $\lambda \times R$
**Answer: (b).** $s \approx \lambda \times LGD = \lambda \times (1-R)$: default intensity times loss severity.

**D7.** In an investment-grade portfolio, the largest source of one-year mark-to-market loss is typically:
(a) outright default (b) coupon reinvestment risk (c) credit migration and spread widening (d) inflation
**Answer: (c).** Defaults are rare in IG; downgrades and general spread widening reprice bonds with every coupon still paid, dominating year-to-year MTM swings.

**D8.** A G-spread and a Z-spread on the same bond coincide when:
(a) the bond is callable (b) the spot curve is steep (c) the spot curve is flat or gently sloped (d) recovery is zero
**Answer: (c).** The G-spread's single-yield approximation only distorts when the curve has shape; on a flat/gentle curve it collapses onto the curve-consistent Z-spread. A steep curve makes them diverge.

**D9.** Which model views equity as a call option on the firm's assets?
(a) reduced-form (b) structural (Merton) (c) transition-matrix (d) credit-triangle
**Answer: (b).** The Merton structural model treats default as assets falling below the debt face value at maturity, making equity a call struck at the debt level — linking credit risk to leverage and asset volatility.

**D10.** A bond's spread duration is 6.0 and its spread narrows by 50 bp (curve unchanged). The approximate price impact is:
(a) −3.0% (b) +3.0% (c) +0.3% (d) −0.5%
**Answer: (b).** $\Delta P/P \approx -(\text{spread duration}) \times \Delta s = -6.0 \times (-0.0050) = +0.030 = +3.0\%$. A *narrowing* (negative $\Delta s$) raises the price.

---

*End of Q&A — Credit Risk and Spreads. All numerical answers were self-verified: expected loss (120 bp) matches the credit triangle; cumulative PD at $\lambda=3\%$ reconciles as 5.91% + 2.82% marginal = 8.73%; the Z-spread solves exactly to 300 bp at price 99.1163 and to 150 bp at price 98.739; the implied hazard 0.03/0.75 = 4.0% reconciles forward; and the migration expected value 98.675 decomposes cleanly back to −1.325.*
