# Q&A — Stress Testing and Scenario Analysis

Practice bank for Chapter 13. Every question is followed by a full answer. Work each one before reading the solution. Stress testing is deliberately *not* probabilistic in the VaR sense — treat "how bad, if it happens" as the central question throughout.

---

## Section A — Concept Check

**A1. Give the one-line definition of stress testing and say how it differs in spirit from VaR.**

Stress testing estimates the loss a portfolio or institution would suffer under a specific, severe-but-plausible set of market or economic conditions. VaR answers "how bad, at what probability, under normal conditions"; stress testing answers "how bad *if* this particular nasty thing happens" and deliberately drops the probability question. VaR is distributional and statistical; stress testing is conditional and narrative. They are complements — VaR covers the body of the distribution, stress testing probes the tail VaR is silent about.

**A2. Distinguish "scenario analysis" from "sensitivity analysis."**

Sensitivity analysis moves **one** risk factor at a time (e.g. rates +100 bp, all else held) to isolate the portfolio's exposure to that single driver. Scenario analysis moves **many** factors together in an internally consistent way (e.g. equities −30%, credit spreads +250 bp, INR −10%, rates −150 bp — a coordinated flight-to-quality). Sensitivity is a partial derivative; scenario analysis is a coherent joint move that respects how factors actually co-move in a crisis.

**A3. Why is "severe but plausible" the governing phrase, and what fails if you drop either word?**

If a scenario is severe but *implausible* (e.g. equities −99% overnight), the board dismisses the output and no action follows — the test loses credibility. If it is plausible but *not severe*, it tells you nothing you did not already see in VaR — it fails to probe the tail. The value sits in the intersection: bad enough to hurt, believable enough to act on.

**A4. Contrast historical scenarios with hypothetical scenarios. Give one strength and one weakness of each.**

A **historical** scenario replays an actual episode (2008 GFC, March 2020 COVID crash, 2013 taper tantrum). Strength: it is indisputably plausible — it happened, so no one argues the calibration. Weakness: the next crisis rarely rhymes exactly with the last, so it can miss novel risks. A **hypothetical** scenario is constructed by experts (e.g. a Middle-East oil shock plus a domestic banking freeze). Strength: it can capture forward-looking, never-seen risks and current portfolio-specific vulnerabilities. Weakness: it is subjective and easy to challenge on calibration.

**A5. What is reverse stress testing and why is it psychologically valuable?**

Reverse stress testing starts from the *outcome* — "what set of events would make us insolvent / breach our capital floor / exhaust our liquidity?" — and works backwards to find the scenarios that produce it. Normal stress testing asks "given this shock, how bad?"; reverse asks "how bad does it have to get before we die, and how could that happen?" It is valuable because it removes the comforting bias of only testing scenarios management already believes are survivable, and it surfaces the specific vulnerabilities that would actually kill the firm.

**A6. Name the four broad categories a good stress-testing programme should span.**

(1) **Market risk** stresses (prices, rates, vols, spreads, FX). (2) **Credit risk** stresses (rating downgrades, default waves, rising PD/LGD). (3) **Liquidity** stresses (funding runs, margin calls, market illiquidity). (4) **Firm-wide / macro** stresses that combine the above into an integrated recession or systemic scenario. A programme that only stresses market prices misses how a crisis actually compounds across risk types.

**A7. Why does correlation "breaking down" matter so much in stress design?**

Diversification benefits rest on assumed correlations. In a crisis, correlations tend toward extremes — risky assets fall together (correlations → +1) while the safe-haven leg decouples — so the offsets your VaR relied on vanish exactly when you need them. A credible stress scenario must therefore override normal-period correlations, otherwise it will understate loss by crediting diversification that evaporates under stress.

**A8. What is a "second-round" or feedback effect, and why do simple stress tests miss it?**

A first-round effect is the direct mark-to-market loss from the shock. Second-round effects are the reactions the shock triggers: forced deleveraging that pushes prices down further, margin calls that drain liquidity, counterparty failures, and fire sales that feed back into prices. Simple stress tests revalue the book once and stop, so they capture only the first round and understate systemic losses, which are dominated by these amplifying feedback loops.

**A9. Why can two banks run "the same" 2008 scenario and get very different, both-correct results?**

The scenario is a set of factor shocks, but the loss depends on each bank's *own* positions, hedges, and sensitivities. A bank long credit and short volatility suffers very differently from one positioned the opposite way. Stress loss = scenario shocks applied to *this* portfolio — the scenario is shared, the exposure is not.

**A10. How does stress testing relate to regulatory capital and to management action?**

Regulators (Basel, and supervisory exercises like the Fed's CCAR/DFAST or the RBI's stress-testing guidance) require banks to hold capital and liquidity sufficient to survive prescribed stresses, making stress results a direct input to capital adequacy. Internally, results must trigger *action* — reducing exposures, buying hedges, raising limits on liquidity buffers — or the exercise is theatre. A stress test that never changes a decision has failed regardless of how sophisticated the modelling is.

---

## Section B — Numerical / Applied (with full solutions)

**B1. Single-scenario revaluation.** A ₹500 crore portfolio holds 60% equities (beta 1.0 to Nifty) and 40% in a 7-year bond (modified duration 6.0). A scenario specifies Nifty −35% and yields +200 bp. Estimate the stressed loss.

Solution.
- Equity leg = 0.60 × 500 = ₹300 cr. Loss = 300 × 35% = **₹105 cr**.
- Bond leg = 0.40 × 500 = ₹200 cr. Price change ≈ −Duration × Δy = −6.0 × 0.02 = −12%. Loss = 200 × 12% = **₹24 cr**.
- Total stressed loss ≈ 105 + 24 = **₹129 cr**, i.e. 25.8% of the portfolio.

Sanity check: both legs lose (equity crash + rising rates hit bonds), so no offset here — consistent with a rate-hike-plus-equity-selloff scenario rather than a flight-to-quality.

**B2. Same portfolio, flight-to-quality scenario.** Now Nifty −35% but yields *fall* 150 bp (safe-haven rally into bonds). Estimate the loss.

Solution.
- Equity leg loss = 300 × 35% = ₹105 cr (unchanged).
- Bond leg gain ≈ −6.0 × (−0.015) = +9%. Gain = 200 × 9% = +₹18 cr.
- Net loss ≈ 105 − 18 = **₹87 cr** (17.4%).

Teaching point: same equity shock, but the *direction of the rate move* flips the bond leg from a ₹24 cr loss to an ₹18 cr gain — a ₹42 cr swing. This is exactly why scenarios must specify factors jointly and consistently; the correlation assumption is the scenario.

**B3. Adding second-order (convexity/gamma) correction.** Reconsider B1's bond leg. The bond has convexity 50. Refine the price change for Δy = +200 bp.

Solution. Price change ≈ −D·Δy + ½·C·(Δy)² = −6.0(0.02) + 0.5(50)(0.02)² = −0.12 + 0.5(50)(0.0004) = −0.12 + 0.01 = −0.11, i.e. −11% (not −12%).
Refined bond loss = 200 × 11% = **₹22 cr**; refined total ≈ 105 + 22 = **₹127 cr**.

Point: convexity cushions large moves, so a duration-only stress *overstates* the loss for big yield jumps. For genuinely severe stresses, full revaluation beats greek-based approximation.

**B4. Historical scenario scaling.** During March 2020 the portfolio's key factor (a credit spread) widened 350 bp over 20 trading days. Your book has spread DV01 (sensitivity to 1 bp) of ₹8 lakh. What is the historical stress loss, and what is the 1-day-equivalent if you want to compare with 1-day VaR?

Solution.
- Full-episode loss = 350 bp × ₹8 lakh/bp = **₹2,800 lakh = ₹28 cr**.
- To put on a 1-day footing you would *not* simply divide by 20 (that assumes linear time). If comparing to a 1-day VaR under an i.i.d. assumption, scale the *shock* by √: 1-day-equivalent spread move ≈ 350/√20 ≈ 78 bp, giving ≈ 78 × 8 = ₹624 lakh ≈ **₹6.2 cr**. But note the honest answer: stress tests are usually reported at the full episode horizon precisely because crisis moves are *not* i.i.d., and the 20-day cumulative figure is the economically meaningful one.

**B5. Reverse stress test.** A bank has ₹1,200 cr of capital and a policy that it must never fall below ₹300 cr (its regulatory floor plus buffer). Its trading book loses ₹3 cr per 1% equity decline (linear). Ignoring other exposures, what equity crash would breach the floor?

Solution. Allowable loss before breach = 1,200 − 300 = ₹900 cr. Required equity move = 900 / 3 = **300%** decline — impossible, so equities *alone* cannot break the bank. The reverse-stress insight: the killing scenario is not a pure equity crash but a *combination* — equity losses plus credit blow-ups plus a funding freeze acting together. Reverse stress testing forces you to find that combination rather than resting on "no single shock can sink us."

**B6. Correlation breakdown, quantified.** In normal times two ₹100 cr positions have return correlation +0.3, each with 20% volatility. Under stress, correlation jumps to +0.9. Compare portfolio volatility (in ₹) normal vs stressed. (σ_p = √(w₁²σ₁² + w₂²σ₂² + 2ρw₁w₂σ₁σ₂), equal weights, absolute ₹ terms with each leg σ = ₹20 cr.)

Solution. Each leg contributes σ = ₹20 cr.
- Normal: σ_p = √(20² + 20² + 2·0.3·20·20) = √(400 + 400 + 240) = √1040 = **₹32.2 cr**.
- Stressed: σ_p = √(400 + 400 + 2·0.9·20·20) = √(400 + 400 + 720) = √1520 = **₹39.0 cr**.

Risk rises ~21% purely from correlation moving 0.3 → 0.9, with *no change in individual volatilities or positions*. This is the diversification benefit evaporating — the single most under-appreciated driver of stress losses.

**B7. Aggregating a multi-factor scenario with offsets.** A scenario gives four factor P&Ls: equities −₹40 cr, credit −₹25 cr, rates +₹15 cr (flight to quality helps the bond book), FX −₹10 cr. State the total and explain why you must not take the worst single factor.

Solution. Net stress P&L = −40 − 25 + 15 − 10 = **−₹60 cr**. Reporting only the worst factor (equities, −₹40 cr) understates the loss by ₹20 cr because the credit and FX legs pile on; reporting the sum of *only* the losing legs (−75 cr) overstates it by ignoring the ₹15 cr rate hedge. The correct number is the coherent net across all factors moving together. Consistency of the joint move is the whole point.

---

## Section C — Interview-Style (with model answers)

**C1. "VaR already gives us a tail number. Why does the firm also spend money on stress testing?"**

Model answer: VaR describes the distribution *under normal conditions* and is estimated from recent history, so it is structurally blind to the rare, regime-shifting events that do the real damage — and those are precisely the events that matter for solvency. Stress testing fills three gaps VaR cannot: it probes losses *beyond* the confidence level (the tail VaR ignores), it uses forward-looking or historical crisis scenarios rather than only the recent calm window, and it captures correlation breakdown and feedback effects that a covariance-based VaR assumes away. VaR is for day-to-day limit-setting; stress testing is for survival. You need both.

**C2. "Walk me through how you would design a firm-wide stress scenario from scratch."**

Model answer: I would start from the firm's *material vulnerabilities* — the largest concentrations and the exposures whose loss would threaten capital or liquidity. Then choose a narrative: anchor on a historical analogue (a 2008-style credit-and-liquidity crisis) or build a hypothetical macro story (a sharp domestic slowdown with capital outflows and INR depreciation). I translate the narrative into a *consistent* set of factor shocks — equity, rates, spreads, FX, defaults — with correlations reflecting crisis behaviour, not calm-period estimates. I apply them by full revaluation, then layer second-round effects: margin calls, funding cost increases, forced sales. Finally I map the loss to capital and liquidity metrics and define the management actions it would trigger. The deliverable is not a number — it is a decision.

**C3. "Our stress test showed we survive 2008 comfortably. Are we safe?"**

Model answer: Not necessarily, and I would push back gently on the framing. Surviving a *replay* of 2008 tells you that you are prepared for the *last* war. The value of that result is limited by three things: the next crisis will have a different epicentre and different correlations; your current portfolio is not the one that existed in 2008; and a single historical scenario cannot reveal your specific kill-switch. I would want to complement it with hypothetical forward-looking scenarios tailored to today's concentrations and, most importantly, a *reverse* stress test that asks what it would actually take to breach our capital or liquidity floor. Comfort against one historical scenario is a starting point, not a clean bill of health.

**C4. "How do you decide the severity of a scenario — where's the line between 'severe but plausible' and 'fantasy'?"**

Model answer: I calibrate against evidence. Historical episodes give hard anchors — the actual peak-to-trough moves in 2008, 2013, and 2020 bound what markets have really done. For hypothetical scenarios, I keep individual factor moves within, or modestly beyond, historically observed extremes and — critically — keep the *joint* move coherent, since implausibility usually creeps in through incoherent combinations rather than any single shock. I also let the audience set the bar: the scenario must be severe enough that the board takes the loss seriously, yet grounded enough that they cannot wave it away as impossible. If risk managers and the business can both look at it and say "yes, that could happen," it is in the right zone. Reverse stress testing then deliberately pushes *past* plausibility to find the breaking point, but that is labelled as such.

**C5. "What are the main limitations of stress testing itself? Sell me the weaknesses."**

Model answer: Four honest ones. First, *scenario selection risk* — you can only stress what you imagine, and the crisis that gets you is usually the one no one scripted. Second, *no probability* — it tells you how bad, not how likely, so it cannot be aggregated the way VaR can, and it is hard to size capital against a scenario with no attached probability. Third, *model and data limits* — feedback effects, liquidity spirals, and contagion are very hard to model, so most tests understate systemic loss. Fourth, *false comfort and gaming* — passing a regulator's prescribed scenario breeds complacency, and firms can position to look good against the published test. The discipline is only as good as the imagination and follow-through behind it.

---

## Section D — Multiple Choice (with reasoning)

**D1. The defining feature that separates stress testing from VaR is that stress testing:**
(a) always produces a larger number
(b) attaches no probability to the scenario
(c) uses only historical data
(d) is required by regulators

Answer: **(b).** Stress testing deliberately answers "how bad if this happens" without assigning a probability. (a) is usually but not necessarily true; (c) is false (scenarios can be hypothetical); (d) is a consequence, not the defining feature.

**D2. Moving only interest rates +100 bp while holding all other factors fixed is an example of:**
(a) scenario analysis
(b) reverse stress testing
(c) sensitivity analysis
(d) Monte Carlo simulation

Answer: **(c).** One factor moved in isolation is sensitivity analysis. Scenario analysis moves multiple factors jointly and consistently.

**D3. A reverse stress test begins by specifying:**
(a) a set of factor shocks
(b) the failure outcome, then finds scenarios that cause it
(c) the probability distribution of losses
(d) the regulatory capital requirement

Answer: **(b).** Reverse stress testing starts from the outcome (e.g. insolvency) and works backwards to the scenarios. (a) describes a conventional forward stress test.

**D4. In a crisis scenario, assuming *normal-period* correlations between risky assets will tend to:**
(a) overstate the stress loss
(b) understate the stress loss
(c) have no effect on the loss
(d) always leave the loss unchanged

Answer: **(b).** In crises, risky-asset correlations rise toward +1, so diversification offsets shrink. Using lower normal-period correlations credits offsets that vanish, understating the loss.

**D5. "Second-round effects" in stress testing refer to:**
(a) running the test a second time for accuracy
(b) the direct mark-to-market loss from the shock
(c) reactions like margin calls, forced sales, and contagion that amplify the initial loss
(d) the second most severe scenario in the suite

Answer: **(c).** Second-round (feedback) effects are the amplifying reactions triggered by the first-round loss; ignoring them understates systemic loss. (b) is the first-round effect.

**D6. The phrase "severe but plausible" fails on the "plausible" side when a scenario is:**
(a) too mild to reveal new risk
(b) so extreme the board dismisses it and takes no action
(c) taken from an actual historical crisis
(d) tailored to the firm's concentrations

Answer: **(b).** Losing plausibility means the scenario is dismissed as fantasy and drives no action. Being too mild (a) is the failure on the "severe" side.

**D7. Two banks run the identical 2008 historical scenario and report very different losses. The best explanation is:**
(a) one of them made a calculation error
(b) the scenario was applied inconsistently
(c) their portfolios and hedges differ, so the same shocks produce different P&L
(d) historical scenarios are unreliable

Answer: **(c).** Stress loss depends on each firm's own exposures. The same shocks acting on different books legitimately give different results — no error required.

**D8. Which is the strongest argument for supplementing a historical 2008 scenario with hypothetical scenarios?**
(a) hypothetical scenarios are always more severe
(b) regulators forbid historical scenarios
(c) the next crisis may have a different epicentre and correlations that 2008 does not capture
(d) hypothetical scenarios are easier to calibrate

Answer: **(c).** Historical replays are backward-looking; hypothetical scenarios add forward-looking, portfolio-specific risks. (a) and (d) are false, and (b) is untrue.

---

## Self-check summary

- **Numbers verified:** B1 (₹129 cr), B2 (₹87 cr — sign flip on the bond leg), B3 (convexity cushions to ₹127 cr), B6 (correlation 0.3→0.9 lifts risk ₹32.2 cr→₹39.0 cr), B7 (net −₹60 cr).
- **Recurring theme:** the danger lives in what the model assumes away — correlation breakdown, second-round feedback, and the scenario you failed to imagine. A stress test is a decision tool, not a number generator.
