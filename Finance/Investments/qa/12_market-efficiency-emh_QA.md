# Q&A — Market Efficiency and the Active-Passive Debate

Practice bank for Chapter 12. Work each question before reading the answer. Returns are in percentages; betas are unit-free. Recurring theme: efficiency means *not predictably exploitable after costs*, not "always right."

---

## Section A — Concept Checks

**A1. State the Efficient Market Hypothesis in one sentence.**
A market is efficient if security prices fully and instantaneously reflect all available and relevant information, so abnormal returns cannot be reliably earned on that information set after costs.

**A2. Why does EMH imply that price changes follow a random walk?**
Prices already embed all current information, so they can only move on *new* information — which is by definition unforecastable. Hence the resulting price change is unpredictable: a random walk (with an upward drift equal to the required return).

**A3. Does "efficient" mean the price is always correct?**
No. Efficient means the price is *unbiased* and *not systematically exploitable*. Prices can be wrong at any moment; they simply cannot be *predictably* wrong in a way you can trade on profitably after costs.

**A4. Name the three forms of efficiency and the analysis each renders useless.**
Weak form reflects all past prices/volume → technical analysis is useless. Semi-strong reflects all public information → fundamental analysis on public data is useless. Strong form reflects all information including private → even insider trading is useless. The forms are nested: each stronger form contains the weaker.

**A5. Which form is almost certainly false in reality, and what is the evidence?**
Strong form. Insiders demonstrably earn abnormal returns on private information — precisely why insider trading is illegal (SEBI PIT Regulations 2015 in India; SEC Rule 10b-5 in the US). Empirically markets are broadly weak and semi-strong efficient but clearly not strong-form.

**A6. Explain the joint-hypothesis problem.**
To call a return "abnormal" you need a model of the "normal" required return (usually CAPM or a factor model). Every efficiency test is therefore simultaneously a test of (a) efficiency and (b) the asset-pricing model. Finding "abnormal" returns is ambiguous — the market may be inefficient, or your risk model may be wrong.

**A7. What is the Grossman–Stiglitz paradox?**
If prices reflected *all* information perfectly, no one could profit from gathering information, so no one would — and then prices couldn't reflect information. Efficiency must be incomplete: just enough mispricing survives to pay the analysts whose work removes it. Markets are "efficiently inefficient."

**A8. What enforces efficiency — smart individuals, or something else?**
Competition and arbitrage among *marginal* informed traders. Efficiency needs only *enough* well-funded rational traders at the margin, not universally rational investors. Irrational investors can exist; if arbitrageurs cheaply trade against them, prices stay efficient.

**A9. Define "limits to arbitrage" and give three examples.**
Frictions that stop traders correcting mispricing: short-selling constraints, noise-trader risk (prices can move further against the arbitrageur before converging, forcing liquidation), funding/liquidity risk, and transaction costs. Inefficiency persists where these are large.

**A10. State Sharpe's arithmetic of active management.**
Before costs, the average active dollar earns the same as the average passive dollar (both hold the market in aggregate). So after costs the average active dollar *must* underperform. This holds by arithmetic in any market, efficient or not.

**A11. Why is the Information Ratio the professional's preferred skill metric?**
It measures active return per unit of *active risk*: IR = alpha ÷ tracking error. It isolates skill relative to the benchmark rather than rewarding a manager for simply taking more market risk. A sustained IR above ~0.5 is good; above ~1.0 is elite and rare.

**A12. Give two anomalies and the form of efficiency each threatens.**
Momentum (past 3–12 month winners keep winning) threatens weak-form efficiency — a *price-based* predictive signal. Post-earnings-announcement drift (prices keep drifting in the surprise direction) threatens semi-strong efficiency — underreaction to *public* news.

**A13. If some funds beat the market, is EMH refuted?**
No. With thousands of funds, luck alone guarantees many winners ("lucky coin-flippers"). The real test is *persistence* and *significance* of alpha after fees and factor adjustment — not the mere existence of past winners.

---

## Section B — Numerical Problems (full working)

**B1. Alpha, Sharpe, and Treynor — does the "star" have skill?**
Fund: $R_p = 16\%$, $\beta_p = 1.4$, $\sigma_p = 22\%$. Market: $R_m = 13\%$, $\sigma_m = 15\%$. Risk-free $R_f = 6\%$.

- CAPM required return: $6 + 1.4(13-6) = 6 + 1.4(7) = 6 + 9.8 = 15.8\%$.
- Jensen's alpha: $16 - 15.8 = +0.2\%$.
- Sharpe: $S_p = (16-6)/22 = 0.455$; $S_m = (13-6)/15 = 0.467$.
- Treynor: $T_p = (16-6)/1.4 = 7.14\%$; $T_m = (13-6)/1.0 = 7.00\%$.

**Reconcile:** Treynor and alpha agree the fund beat the market per unit of *beta* (alpha > 0 ⟺ Treynor > market Treynor, always). But Sharpe says it *lost* on total risk (0.455 < 0.467). Why: a perfectly diversified fund with β 1.4 would have σ = $1.4 \times 15 = 21\%$; the actual 22% carries $\sqrt{22^2 - 21^2} = \sqrt{43} \approx 6.6\%$ of diversifiable risk that Sharpe penalises but beta ignores. Verdict: the +0.2% alpha is noise, and the fund took uncompensated idiosyncratic risk. The "16% beat 13%" headline collapses under risk adjustment. ✓

**B2. The arithmetic of active management, made concrete.**
Index returns 12% gross. Market split: 70% passive (fee 0.10%), 30% active (fee 1.20% + 0.40% trading drag).

- Gross: passive holds the index = 12.0%; by Sharpe's arithmetic active *in aggregate* also = 12.0%.
- Passive net: $12.0 - 0.10 = 11.90\%$.
- Active net (average): $12.0 - 1.20 - 0.40 = 10.40\%$.
- Gap: $11.90 - 10.40 = 1.50\%$ per year — exactly the fee-plus-cost differential.

**Reconcile — compounding over 20 years.** ₹100 at 11.90% → $100 \times 1.119^{20} = ₹945$. At 10.40% → $100 \times 1.104^{20} = ₹722$. The passive investor ends with $945/722 - 1 = 31\%$ more wealth, purely from lower costs, no skill required. This mirrors SPIVA data: ~80–90% of active large-cap funds trail their benchmark over 10–15 years. ✓

**B3. Information Ratio and required gross alpha.**
A manager delivers 1.8% alpha with 3.0% tracking error. (a) Find the IR. (b) If the fund charges 1.6% in fees/costs, what *gross* alpha is needed just to match a passive net return, given the passive fund charges 0.10%?

- (a) $IR = 1.8 / 3.0 = 0.60$ — good, above the ~0.5 threshold.
- (b) To match passive net, gross alpha must cover the cost disadvantage: active 1.6% vs passive 0.10% = 1.5% gap. So gross alpha must be at least $+1.5\%$ before the manager adds any value above indexing.

**Reconcile:** the 1.8% gross alpha clears the 1.5% hurdle by only 0.3% of net value to the client — despite a respectable IR of 0.60. Costs dominate: even genuine skill is mostly consumed by the fee load. ✓

**B4. Filter rule versus buy-and-hold under a random walk.**
Daily log returns are i.i.d. with mean $\mu = 0.0004$ (~10% over 250 days) and SD $\sigma = 0.015$. A chartist buys after every up-day, trading ~120 times/year; round-trip cost is 0.10%. Buy-and-hold trades once (cost 0.10%).

- Under weak-form efficiency $\text{Corr}(r_t, r_{t+1}) = 0$, so $E[r_{t+1} \mid r_t > 0] = \mu$. The up-day carries no information.
- Buy-and-hold: gross $= 250 \times 0.0004 = 10.0\%$; net $= 10.0 - 0.10 = 9.90\%$.
- Filter rule: gross $= 10.0\%$ (identical — no edge from noise); costs $= 120 \times 0.10 = 12.0\%$; net $= 10.0 - 12.0 = -2.0\%$.

**Reconcile:** the gross returns *must* match under a random walk — the rule cannot manufacture edge from serially uncorrelated returns. The only difference is transaction costs, which churning multiplies, converting a +10% asset into a −2% strategy. Weak-form efficiency biting in practice. ✓

**B5. Semi-strong efficiency and an event study.**
A firm announces earnings 20% above consensus at 10:00 a.m. The stock jumps from ₹500 to ₹560 within minutes, then trades flat around ₹560. (a) Consistent with semi-strong efficiency? (b) What pattern would instead signal PEAD?

- (a) Yes. The full $+12\%$ adjustment happens *instantaneously* on the public announcement, then no drift. Investors buying at ₹560 earn only the normal required return going forward — the surprise is already priced. Textbook semi-strong efficiency.
- (b) PEAD would show the price drifting *further* up over the following weeks — e.g., ₹560 → ₹580 over a month — as the market *underreacts* and slowly incorporates the surprise. That gradual, predictable drift is the exploitable inefficiency.

**Reconcile:** the test is *speed and completeness* of adjustment. Instant full jump = efficient; slow continued drift in the surprise direction = semi-strong inefficiency (PEAD). ✓

**B6. Two managers with identical raw returns — rank by IR.**
Both funds return 15% with the benchmark at 12%, so both have 3% active return. Fund P has tracking error 4%; Fund Q has tracking error 8%.

- $IR_P = 3/4 = 0.75$; $IR_Q = 3/8 = 0.375$.

**Reconcile:** identical headline outperformance, but P generated it with half the active risk — twice the skill per unit of tracking error. Q's higher tracking error suggests its 3% is more likely luck that could reverse. Raw active return alone is misleading; the IR is the correct lens. ✓

---

## Section C — Interview-Style Questions (model answers)

**C1. "Are markets efficient?"**
I'd answer with a spectrum, not a yes/no. Markets are broadly weak- and semi-strong efficient and definitely not strong-form efficient — insiders demonstrably profit. They're efficient enough that the *average* active manager can't beat the index net of fees; that's Sharpe's arithmetic, and SPIVA confirms 80–90% of active funds trail over a decade-plus. But limits to arbitrage leave persistent pockets — momentum, small caps, distressed debt, illiquid markets, short windows around information events — where genuine skill can be paid. So: index the core, be active only where you can name a structural reason the inefficiency survives.

**C2. "Walk me through the three forms of efficiency."**
Fama classified efficiency by the information set prices reflect, and the forms are nested. Weak form: prices embed all past price/volume data, so technical analysis is futile and returns follow a random walk. Semi-strong adds all public information, so fundamental analysis on public data only pays if your *interpretation* is genuinely superior. Strong form adds private information, meaning even insiders couldn't profit — empirically false, which is why insider trading is banned. Consensus: markets are close to semi-strong efficient with documented exceptions like momentum.

**C3. "If markets are efficient, why does anyone gather information?"**
This is the Grossman–Stiglitz paradox. If prices already reflected everything, there'd be no return to research, so no one would do it — but then prices couldn't reflect information. So efficiency must be incomplete: exactly enough mispricing survives to compensate the analysts whose trading removes it — an "efficiently inefficient" equilibrium. This is also why passive is self-limiting: if everyone indexed, price discovery would collapse and inefficiency would explode, reviving active. Active never fully dies.

**C4. "How do you tell skill from luck in a fund manager?"**
Three filters. First, *persistence* — does outperformance repeat across independent periods, or is this one lucky run among thousands of funds where luck guarantees winners? Second, *statistical significance* of alpha over a long record. Third, and most important, does the alpha survive *factor adjustment*? I'd regress the fund's returns on the Fama–French–Carhart factors — market, size (SMB), value (HML), momentum (WML). If the "alpha" disappears once I control for these, the manager wasn't skilled; they were tilted toward known factors a cheap smart-beta fund could replicate. True alpha is what remains.

**C5. "Why can't active management beat passive on average?"**
It's arithmetic, not opinion — Sharpe's insight. Active and passive investors together own the entire market. Passive holds the market portfolio by construction, so active as a group must hold the same residual — its aggregate gross return equals the index. Since active managers charge more and trade more, their aggregate *net* return is lower by exactly the cost differential. Active is zero-sum before costs, negative-sum after. Individuals can win, but only by another's loss, and every one still pays the cost drag.

**C6. "Doesn't the existence of bubbles disprove EMH?"**
Not automatically. EMH says prices aren't *predictably* exploitable, not that they're always fair. Spotting a bubble in hindsight proves nothing; *profiting* from spotting one before it bursts is what would challenge efficiency — and that's extraordinarily hard because of limits to arbitrage. As Keynes put it, markets can stay irrational longer than you can stay solvent: an arbitrageur shorting an overvalued stock risks it climbing further, forcing liquidation before convergence. So bubbles are more evidence *for* limits to arbitrage than *against* tradable efficiency.

**C7. "Where would you actually look for inefficiency?"**
The single most useful principle: inefficiency lives where arbitrage is hardest, not where analysis is easiest. I wouldn't hunt for edge in large, liquid, heavily-covered stocks where a hundred analysts already priced the news. I'd point active effort at *frictions* — short-sale constraints, illiquidity, transaction costs, noise-trader risk. Concretely: small caps with thin coverage, distressed debt, private/illiquid markets, and short windows around earnings where underreaction (PEAD) creates drift. The friction is what protects the skill from being competed away.

**C8. "What's your asset allocation philosophy given all this?"**
A barbell, or core-satellite. The core holds broad, low-cost index funds that capture the market return cheaply; costs are the one variable I control with certainty, and a 1.5% annual drag compounds to ~30% less wealth over 20 years. The satellite is a smaller active allocation, only where I can name a structural reason the inefficiency survives arbitrage. This respects both truths: markets are efficient enough that most investors should index, yet scarce skill persists at the margins.

---

## Section D — MCQs (with reasoning)

**D1.** Weak-form efficiency implies that which analysis is useless?
(a) fundamental analysis (b) technical analysis (c) insider trading (d) factor analysis
**Answer: (b).** Weak form says prices already reflect all past price/volume data, so charting past prices yields no edge. Fundamental analysis is defeated by semi-strong; insider trading by strong.

**D2.** A random walk with drift means:
(a) prices go nowhere (b) prices are perfectly predictable (c) prices trend up but deviations are unpredictable (d) returns are negatively autocorrelated
**Answer: (c).** The drift is the equity risk premium (prices trend up); the deviations *around* the drift are unforecastable. "Goes nowhere" ignores the drift.

**D3.** The joint-hypothesis problem states that any efficiency test is simultaneously a test of:
(a) two different markets (b) the asset-pricing model used (c) the risk-free rate (d) investor rationality
**Answer: (b).** Judging a return "abnormal" requires a benchmark for "normal" return, so you jointly test efficiency and that asset-pricing model. Abnormal returns could mean inefficiency *or* a wrong model.

**D4.** According to Sharpe's arithmetic, after costs the average active dollar must:
(a) beat the average passive dollar (b) equal the average passive dollar (c) underperform the average passive dollar (d) beat the risk-free rate
**Answer: (c).** Active and passive earn the same gross return in aggregate; higher active costs make active's aggregate net return lower by the cost differential. This holds in any market.

**D5.** The Information Ratio is defined as:
(a) alpha ÷ beta (b) alpha ÷ tracking error (c) excess return ÷ standard deviation (d) excess return ÷ beta
**Answer: (b).** IR = alpha ÷ tracking error — active return per unit of active risk. Option (c) is Sharpe; (d) is Treynor.

**D6.** The Grossman–Stiglitz paradox implies markets must be:
(a) perfectly efficient (b) perfectly inefficient (c) efficiently inefficient (d) strong-form efficient
**Answer: (c).** Some mispricing must survive to reward the information-gatherers whose trading removes it; otherwise no one would gather information. Hence "efficiently inefficient."

**D7.** Post-earnings-announcement drift (PEAD) is an anomaly that most directly challenges:
(a) weak-form efficiency (b) semi-strong efficiency (c) strong-form efficiency (d) the random walk
**Answer: (b).** PEAD is a predictable drift following *public* earnings news — a failure to instantly price public information, which is the semi-strong claim.

**D8.** Momentum is notable among anomalies because it challenges:
(a) semi-strong efficiency using private data (b) weak-form efficiency using past prices (c) strong-form efficiency only (d) no form of efficiency
**Answer: (b).** Momentum is a *price-based* signal (past winners keep winning), so it contradicts weak-form efficiency, which says past prices carry no usable predictive information.

**D9.** "Limits to arbitrage" best explain why:
(a) all prices are always correct (b) anomalies get instantly eliminated (c) mispricing can persist despite rational traders (d) insiders never profit
**Answer: (c).** Frictions — short constraints, noise-trader risk, costs — prevent arbitrageurs from fully correcting mispricing, so it can survive. Inefficiency lives where arbitrage is hardest.

**D10.** A fund shows positive raw returns above its benchmark, but the outperformance vanishes after Fama–French–Carhart adjustment. This indicates:
(a) genuine skill (alpha) (b) disguised factor exposure, not skill (c) a strong-form inefficiency (d) a violation of Sharpe's arithmetic
**Answer: (b).** If controlling for size, value, and momentum removes the "alpha," the manager was merely tilted toward known factors replicable by cheap smart-beta — factor beta, not skill.

**D11.** Which statement about strong-form efficiency is correct?
(a) it is empirically well-supported (b) it implies insiders cannot profit, and is empirically false (c) it is the weakest form (d) it only concerns past prices
**Answer: (b).** Strong form claims prices reflect even private information, so insiders couldn't profit — but they demonstrably do, which is why insider trading is illegal. It is the strongest and empirically rejected form.

**D12.** The most reliable practical case for low-cost index investing rests on:
(a) markets always being perfectly efficient (b) no manager ever winning (c) the certainty of cost savings compounding, versus the uncertainty of alpha (d) technical analysis being useful
**Answer: (c).** Costs are controllable with certainty and compound powerfully (~1.5% drag ≈ 30% less wealth over 20 years), whereas alpha is uncertain and scarce. That asymmetry drives the indexing case.

---

*End of Chapter 12 Q&A. Master three reflexes: (1) restate efficiency as "not predictably exploitable after costs," (2) recite Sharpe's arithmetic on demand, (3) always risk- and factor-adjust before crediting a manager with skill.*
