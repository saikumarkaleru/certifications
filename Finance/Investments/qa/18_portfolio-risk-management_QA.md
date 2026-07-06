# Q&A — Portfolio Risk Management

Practice bank for Chapter 18. Work each question before reading the answer. Currency is ₹ crore unless stated; volatilities and returns are in percent; betas and correlations are unit-free. Every numerical answer is worked in full and reconciled against a cross-check.

---

## Section A — Concept Checks

**A1. State the one sentence the whole chapter elaborates.**
The risk of a portfolio is not the sum of the risks of its parts, and the risk that matters is not the wiggle you see on normal days but the loss you suffer on abnormal ones. Everything — aggregation, VaR, stress testing, limits, budgets, hedges, drawdown rules — is machinery for acting on that sentence.

**A2. What is the difference between measuring risk and managing it?**
Measurement is diagnosis (variance, beta, VaR, duration); management is treatment (limits, budgets, hedges, drawdown rules). Blow-ups almost never come from failing to calculate the number — they come from calculating it, believing it too much, sizing too big, and having no plan for the day the number is wrong.

**A3. Define VaR precisely, and give one thing it does NOT tell you.**
Value at Risk at confidence $c$ over horizon $h$ is the loss $L$ such that $P(\text{loss} > L) = 1-c$ over that horizon. A 1-day 99% VaR of ₹10 cr means on 99 of 100 days you lose less than ₹10 cr. It tells you *nothing* about how bad the loss is on the 1 day you breach it — the tail beyond the threshold.

**A4. Why is VaR called an "incoherent" risk measure, and what fixes it?**
Because it is not sub-additive: the VaR of a combined book can exceed the sum of the two standalone VaRs, violating the intuition that merging can only diversify. Expected Shortfall (ES/CVaR) — the *average* loss given VaR is breached — is sub-additive (coherent) and tail-sensitive, which is why Basel III's FRTB migrated to 97.5% ES.

**A5. Name the three ways to compute VaR and each one's chief weakness.**
Parametric/delta-normal (fast, analytic — but wrong for options and fat tails); historical simulation (real correlations and tails — but only the tails that happened to occur in the window); Monte Carlo (flexible, handles non-linearity — but only as good as the assumed model, and computationally expensive).

**A6. Distinguish marginal VaR from component VaR.**
Marginal VaR is how much total VaR changes for a small increase in a position — the risk "price" of adding to it. Component VaR is each position's *contribution* to total VaR, and the components sum exactly to total VaR. Component VaR tells you where your risk actually lives, which is often startlingly different from where your capital lives.

**A7. Why is stress testing the necessary complement to VaR?**
VaR is a speedometer; stress testing is the crash-test. Stress testing abandons the probability distribution and asks a scenario question ("if 2008 happened again, what would we lose?"), deliberately relaxing the two assumptions that make VaR dangerous — the distribution and the calm-period correlation matrix. It captures the fat tail, the correlation break, and the liquidity freeze that VaR smooths over.

**A8. What is reverse stress testing and why is it uniquely revealing?**
It starts from the answer — "what set of moves would wipe out X% of capital?" — and works backward to the scenario. It is revealing because it surfaces hidden concentrations and the exact correlation assumptions the book is silently betting on, rather than testing only scenarios you already thought of.

**A9. What is basis risk, and give the canonical example.**
Basis risk is the residual risk from an imperfect hedge — the exposure and the hedging instrument are not perfectly correlated. Hedging Indian mid-caps with Nifty 50 futures covers large-cap market moves but not the mid-cap-vs-large-cap spread; in a flight to quality large-caps hold up while mid-caps fall harder, so the hedge under-protects. You exchange price risk for basis risk, which you must judge smaller and more acceptable.

**A10. Contrast a protective put with a collar.**
A protective put (long portfolio + long put) sets a downside floor at the strike while keeping upside, at the cost of an ongoing premium bleed. A collar finances that put by selling a call, giving up upside above the call strike; a "zero-cost collar" funds the put entirely with the call — you pay in foregone upside instead of cash.

**A11. Why do pre-committed limits beat in-the-moment judgment?**
Human risk appetite is pro-cyclical: we feel safest right after a long calm (when valuations are stretched and trades are crowded) and most frightened at the bottom (when risk is actually cheapest). Limits and risk budgets are a Ulysses-and-the-mast device — they bind the future, panicking-or-greedy version of you to the discipline of the calm, rational version.

**A12. Why is a 60/40 portfolio "not balanced"?**
Balanced by *capital*, not by *risk*. Equities are roughly 3–4× as volatile as bonds, so a 60/40 book carries about 90% of its risk in equities — practically an equity fund with a bond garnish. Balance must be judged in risk units, which is the whole point of risk budgeting.

**A13. State the master distinction of the chapter in one line.**
Volatility measures the bumpiness of the ride (symmetric, mark-to-market dispersion); true risk is the probability and magnitude of permanent, unrecoverable loss of capital. Every tool in the chapter exists to manage the gap between the two.

---

## Section B — Numerical Problems (full working)

**B1. Parametric VaR and Expected Shortfall.**
A fund holds ₹100 cr with annual return volatility 20%. Assume 250 trading days and normal returns. Find 1-day 99% VaR, 10-day 99% VaR, and 1-day 99% ES.

- 1-day vol: $\sigma_{1d} = 20\%/\sqrt{250} = 0.20/15.81 = 1.265\%$.
- 1-day 99% VaR ($z = 2.326$): $2.326 \times 0.01265 \times 100 = ₹2.94$ cr.
- 10-day VaR (√-time): $2.94 \times \sqrt{10} = 2.94 \times 3.162 = ₹9.30$ cr.
- ES factor for normal: $\phi(2.326)/(1-c) = 0.0267/0.01 = 2.67$. ES $= 2.67 \times 0.01265 \times 100 = ₹3.38$ cr.

**Reconcile:** ES (₹3.38 cr) > VaR (₹2.94 cr) always, because the average loss on a breach day exceeds the threshold — exactly the tail info VaR omits. And both numbers assume normality; if returns are fat-tailed, both understate reality. ✔

**B2. Beta hedge with index futures.**
A ₹50 cr equity book has beta 1.30 to the Nifty 50 at 24,000, lot size 50, so one contract = 24,000 × 50 = ₹12,00,000 = ₹0.12 cr. (a) Contracts to fully hedge to beta 0? (b) Verify the offset if the market falls 5%. (c) Contracts to move beta to 0.80 instead?

- (a) $N = \beta_p V_p/F = 1.30 \times 50/0.12 = 1.30 \times 416.7 = 542$ contracts short.
- (b) Portfolio loss $\approx 1.30 \times 5\% \times 50 = ₹3.25$ cr. Futures gain $\approx 5\% \times (542 \times 0.12) = 5\% \times 65.0 = ₹3.25$ cr. They offset — only idiosyncratic P&L remains. ✔
- (c) $N = (\beta^* - \beta_p)V_p/F = (0.80 - 1.30) \times 416.7 = -0.50 \times 416.7 = -208$ contracts (short 208).

**Cross-check:** part (c) shorts fewer contracts than part (a) — sensible, since dialing beta from 1.30 to 0.80 removes only 0.50 of beta versus the full 1.30. Ratio $208/542 = 0.384 = 0.50/1.30$. ✔

**B3. Diversified VaR, then a correlation-break stress.**
A ₹100 cr book is ₹50 cr equities (daily vol 1.5%) and ₹50 cr bonds (daily vol 0.4%), calm correlation −0.30. (a) 1-day 99% VaR. (b) Stress: equities −12%, bonds −3%, correlation flips to +0.70. Compare.

- (a) $\sigma_p = \sqrt{0.5^2(1.5)^2 + 0.5^2(0.4)^2 + 2(0.5)(0.5)(-0.30)(1.5)(0.4)}$
  $= \sqrt{0.5625 + 0.04 - 0.09} = \sqrt{0.5125} = 0.716\%$.
  VaR $= 2.326 \times 0.716\% \times 100 = ₹1.67$ cr.
- (b) Stress loss $= 0.5(-12\%) + 0.5(-3\%) = -6\% - 1.5\% = -7.5\% = -₹7.5$ cr.

**Reconcile:** the stress loss (₹7.5 cr) is ~4.5× the VaR (₹1.67 cr) — not because the VaR math was wrong, but because *both* its inputs (the −0.30 correlation and the no-fat-tail assumption) broke at once. This is the LTCM/2008 mechanism: the diversification you budgeted for vanishes exactly when you draw on it. Size to survive the stress loss, not the VaR. ✔ (Note the flipped +0.70 correlation does not enter the point-scenario loss — it is a fixed-move revaluation — but it is the reason both legs fall together instead of one cushioning the other.)

**B4. Risk budgeting — capital weights lie.**
A pension runs 60% equities (σ = 18%), 40% bonds (σ = 5%), correlation 0.20. Find portfolio vol, equities' risk contribution, and equities' share of total risk.

- $\sigma_p = \sqrt{0.6^2(18)^2 + 0.4^2(5)^2 + 2(0.6)(0.4)(0.20)(18)(5)}$
  $= \sqrt{116.64 + 4.0 + 8.64} = \sqrt{129.28} = 11.37\%$.
- Marginal contribution of equities $= \dfrac{w_E\sigma_E^2 + w_B\rho\sigma_E\sigma_B}{\sigma_p} = \dfrac{0.6(324) + 0.4(0.20)(90)}{11.37} = \dfrac{194.4 + 7.2}{11.37} = 17.73$.
- Equity risk contribution $= w_E \times 17.73 = 0.6 \times 17.73 = 10.64\%$.
- Share $= 10.64/11.37 = 93.6\%$.

**Cross-check:** bonds must supply the remaining 6.4%. Bond marginal $= \dfrac{0.4(25) + 0.6(0.20)(90)}{11.37} = \dfrac{10 + 10.8}{11.37} = 1.83$; bond RC $= 0.4 \times 1.83 = 0.73\%$; share $0.73/11.37 = 6.4\%$. The two contributions sum to $10.64 + 0.73 = 11.37 = \sigma_p$ exactly. ✔ A "60/40" book is ~94% equity risk; risk parity would lever bonds and cut equities to equalize.

**B5. Drawdown recovery asymmetry.**
A fund falls 40%. What gain recovers it? What if it falls 60%? State the general rule.

- Recovery gain $= \dfrac{1}{1-d} - 1$. For −40%: $1/0.60 - 1 = 1.667 - 1 = 66.7\%$.
- For −60%: $1/0.40 - 1 = 2.50 - 1 = 150\%$.

**Interpretation:** the required gain grows convexly with the drawdown — −50% needs +100%, −80% needs +400%. This asymmetry is why drawdown control is a *return* driver, not a comfort feature, and why leverage (which deepens the hole and can force selling via margin calls before the recovery) is so dangerous. ✔

---

## Section C — Interview-Style Questions (model answers)

**C1. "Your VaR model says the fund is safe. Why don't you trust it?"**
Because VaR answers one narrow question — the loss threshold at a chosen percentile — and is blind to three things. First, it says nothing about the tail beyond the cutoff; a book short deep-OTM options has a tiny VaR and a catastrophic loss just past the 99th percentile. Second, it is not sub-additive, so it can misstate the benefit of combining books. Third, it is only as good as its inputs — feed it a normal distribution and a calm-period correlation matrix and it systematically understates tail risk, because real returns are fat-tailed and correlations are unstable. So I read VaR as a speedometer, pair it with Expected Shortfall for the tail, and run stress tests as the crash-test. I never size a book to survive only its VaR; I size it to survive its stress loss.

**C2. "Walk me through how you'd hedge an equity portfolio's market risk, and what's left afterward."**
Short index futures sized as $N = \beta_p V_p / F$ to take net beta to zero, or $N = (\beta^* - \beta_p)V_p/F$ to dial to a target beta. Futures are cheap, liquid, and symmetric — they strip out market direction so I keep only stock-selection alpha. What's left is idiosyncratic risk (the alpha and its risk — intentional), basis risk if the hedging index doesn't match the book (e.g., mid-caps hedged with Nifty 50), and factor/sector tilts the beta hedge doesn't touch. If I wanted asymmetric crash protection instead of removing upside, I'd buy protective puts and accept the premium bleed, or cheapen them into a collar by capping upside. A hedge never eliminates risk — it *transforms* price risk into basis risk plus cost.

**C3. "A junior analyst says our 60/40 fund is well diversified because no asset class exceeds 60%. Correct him."**
He's judging balance in capital units; risk lives in different units. Equities are 3–4× as volatile as bonds, so decomposing portfolio volatility into risk contributions shows equities supply roughly 90–94% of the total risk — the fund is effectively an equity fund with a bond garnish. If I want genuine balance I budget *risk*, not capital: toward risk parity, where each class contributes equal risk, which means levering the low-vol bonds up and cutting the equity weight down. The lesson is that risk, not capital, is the scarce and dangerous resource, so it's the one you allocate deliberately.

**C4. "Buffett says volatility isn't risk. Is he wrong, given everything CAPM and Sharpe rest on?"**
He's making a real distinction, not denying the math. Volatility is a symmetric measure of mark-to-market dispersion — an excellent risk proxy for a diversified, liquid, unlevered, roughly-normal book, and rightly central to Markowitz, CAPM, Sharpe and VaR. But true risk is the probability of *permanent, unrecoverable* loss, and the two diverge whenever leverage, illiquidity, concentration, fat tails, or overvaluation enter. A stable, levered, illiquid income strategy can show low volatility and carry huge true risk; a quality stock down 40% on temporary fear can be high volatility yet low true risk if you can hold it. So volatility is *a* dimension of risk — the one that bites if you can be forced to sell — but not *the* risk. My job as a risk manager is precisely to manage the gap: ES and stress for fat tails, limits for leverage and concentration, liquidity limits for illiquidity, drawdown rules for the forced-seller path.

**C5. "Give me one crisp case study per major failure mode."**
LTCM (1998) — *leverage plus correlation*: ~25× balance-sheet leverage and models that treated correlations as independent; Russia's default snapped them all to 1 and a "few percent" month became a ~90% loss. Amaranth (2006) — *concentration plus liquidity*: one natural-gas trader held a calendar spread so large it was a material fraction of open interest, and there was no one to sell to when it moved — over half the fund, ~$6.6 bn, gone in a week. 1987 — *dynamic-hedging feedback*: portfolio insurance rules all said "sell futures as the market falls," so everyone sold at once and amplified the crash. Quant quake (August 2007) — *crowded trades*: many market-neutral funds ran the same factor bets; one deleveraging forced everyone's longs down and shorts up. The common thread: the danger was never the calm-Tuesday volatility — it was leverage, concentration, liquidity, and correlations that only appear when everyone needs the exit at once.

---

## Section D — Multiple Choice (with reasoning)

**D1. A 1-day 99% VaR of ₹5 cr means:**
(a) The most you can lose in a day is ₹5 cr.
(b) On about 1 day in 100 you lose more than ₹5 cr.
(c) Your average daily loss is ₹5 cr.
(d) You will lose ₹5 cr on 99 days out of 100.
**Answer: (b).** VaR is a threshold not exceeded with 99% confidence, so on ~1 day in 100 the loss is worse. (a) is the "VaR is the worst case" fallacy — losses beyond it can be far larger. (c) describes something closer to Expected Shortfall. (d) misreads the confidence level as a frequency of the loss amount.

**D2. Which risk measure is sub-additive (coherent) and captures the tail beyond the cutoff?**
(a) Parametric VaR (b) Historical VaR (c) Expected Shortfall (d) Standard deviation
**Answer: (c).** ES/CVaR averages losses *given* VaR is breached, making it tail-sensitive, and it is sub-additive — the two defects of VaR it is designed to fix. Any flavour of VaR (a, b) shares VaR's incoherence. Standard deviation (d) is symmetric and says nothing specifically about the tail.

**D3. To reduce a ₹50 cr book's beta from 1.20 to 0.60 with futures where one contract = ₹0.10 cr, you should:**
(a) Short 600 contracts (b) Short 300 contracts (c) Long 300 contracts (d) Short 250 contracts
**Answer: (b).** $N = (\beta^* - \beta_p)V_p/F = (0.60 - 1.20)(50/0.10) = -0.60 \times 500 = -300$, i.e. short 300. (a) is the full hedge to beta 0 ($1.20 \times 500 = 600$). (c) has the wrong sign — you short to reduce beta. (d) uses no clean formula.

**D4. In a market crisis, cross-asset correlations typically:**
(a) Fall toward zero, boosting diversification (b) Stay stable (c) Rise toward 1, eroding diversification (d) Become irrelevant
**Answer: (c).** Everything is sold to raise cash, so correlations converge toward 1 and the diversification you budgeted for evaporates precisely when you need it — the LTCM/2008 mechanism. This is why a risk process never trusts a single calm-period correlation matrix and stresses it instead.

**D5. A 60/40 (equity/bond) portfolio is best described as:**
(a) ~60% of risk in equities (b) ~40% of risk in equities (c) ~90% of risk in equities (d) Equal risk in both
**Answer: (c).** Because equities are ~3–4× as volatile as bonds, equities contribute roughly 90% of portfolio risk despite 60% of capital. (a) confuses capital weight with risk weight; (d) would require risk parity, achieved by levering bonds and cutting equities.

**D6. A strategy that sells deep out-of-the-money puts for steady premium shows low reported volatility. Its true risk is:**
(a) Low, matching the volatility (b) High — a fat left tail can deliver a catastrophic loss (c) Zero, since premium is collected (d) Equal to the premium received
**Answer: (b).** This is the textbook divergence of volatility and true risk: low σ and steady income until a crash delivers a huge left-tail loss. Volatility misses skew and fat tails; ES and stress testing are what catch this exposure.

**D7. The chief limitation of historical-simulation VaR is that it:**
(a) Assumes normally distributed returns (b) Cannot handle correlations (c) Only reflects the tails that occurred in the sample window (d) Requires a full covariance matrix
**Answer: (c).** Historical simulation makes *no* distributional assumption and captures real correlations — so (a), (b), (d) describe the parametric method, not this one. Its weakness is that it can only replay events present in the window and weights a 1-in-N event as exactly 1/N; a tail that hasn't happened yet is invisible to it.

**D8. A stop-loss rule that cuts exposure at a −10% drawdown primarily protects against ___, but can ___.**
(a) Turning a manageable loss into a terminal one; whipsaw you out before a rebound (b) Basis risk; increase leverage (c) Inflation; reduce taxes (d) Counterparty risk; raise correlation
**Answer: (a).** Drawdown/de-grossing triggers mechanize the discipline of not letting a survivable loss become terminal, respecting the recovery asymmetry (−50% needs +100%). The trade-off is whipsaw — cutting right before a rebound and locking in the loss — so triggers must be calibrated to the strategy's natural volatility.

---

## Self-Verification Notes

- **B1:** $0.20/\sqrt{250} = 0.01265$; VaR $2.326\times0.01265\times100 = 2.94$; $\times\sqrt{10}=9.30$; ES $2.67\times0.01265\times100 = 3.38 >$ VaR. ✔
- **B2:** $1.30\times(50/0.12) = 542$; $(0.80-1.30)\times416.7 = -208$; ratio $208/542 = 0.50/1.30$. ✔
- **B3:** $\sqrt{0.5125} = 0.716$; VaR $= 1.67$; stress $-7.5$; ratio $4.5\times$. ✔
- **B4:** $\sqrt{129.28} = 11.37$; equity RC $10.64$ (93.6%), bond RC $0.73$; sum $= 11.37 = \sigma_p$. ✔
- **B5:** $1/0.60-1 = 66.7\%$; $1/0.40-1 = 150\%$. ✔ **D3:** $-0.60\times500 = -300$ (short 300). ✔
