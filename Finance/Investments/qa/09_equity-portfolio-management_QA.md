# Q&A — Equity Portfolio Management

Practice bank for Chapter 09. Work each question before reading the answer. Weights and returns are in percentages unless stated; betas and ratios are unit-free.

---

## Section A — Concept Checks

**A1. State the core identity of equity portfolio management in one line.**
$\text{Portfolio} = \text{Benchmark} + \text{Active positions}$. Everything you get paid for — and every active risk you take — lives entirely in the deviations of your weights from the index. If every weight equals the index weight, active return is mathematically zero before fees and negative after.

**A2. Why is active management a "loser's game"?**
Sharpe's arithmetic: before costs, active managers *in aggregate are* the market — one manager's overweight is another's underweight, so they net to the index return. After fees and trading costs, the average active rupee must therefore underperform the average passive rupee. It is accounting, not a claim about efficiency. To win you must beat the average participant, who is a professional.

**A3. What are the four linked choices the chapter breaks the craft into?**
(1) Active vs passive — do you take active bets at all, and how aggressively; (2) Style — value, growth, GARP, or quality; (3) Process — top-down macro or bottom-up stock picking; (4) Structure — how concentrated the bets are and how far they push you from the benchmark (tracking error, active share).

**A4. Write the Fundamental Law of Active Management and say what it teaches.**
$IR \approx IC \times \sqrt{BR}$, where $IR$ is the information ratio, $IC$ is the information coefficient (per-bet skill, the correlation between forecasts and outcomes), and $BR$ is breadth (independent bets per year). Lesson: a strong track record can come from deep skill on a few bets *or* modest skill spread across many independent bets — which is why concentrated stock-pickers and diversified quants are both viable.

**A5. Distinguish tracking error from active share.**
Tracking error is the standard deviation of active return: return-based, backward-looking, measures the *volatility* of the active bet. Active share is $\tfrac{1}{2}\sum|w_p-w_b|$: holdings-based, forward-looking, measures *how much* of the portfolio differs from the index. They capture different things — a diversified stock-picker can have high active share but low TE (idiosyncratic bets wash out); a sector bettor can have modest active share but high TE.

**A6. Why the factor of one-half in the active-share formula?**
Because in a fully invested portfolio every overweight is matched by an equal-sized underweight, so the sum of absolute active weights double-counts the true difference. Halving it gives the fraction of the portfolio genuinely deviating from the index, on a 0%–100% scale.

**A7. What is a closet indexer, and which tool exposes it?**
A fund charging active fees while holding mostly the index — e.g. 1% fee for 20% active share means you pay 5x the index fee on the active portion (or ~1% for 20% of a differentiated product). Active share exposes it: high fee plus active share below ~40% is the tell.

**A8. Define the PEG ratio and the GARP counter-intuition.**
$PEG = (P/E)/g$, where $g$ is expected earnings growth in percent. PEG near 1.0 is "fair," below 1.0 attractive. The counter-intuition: a high-P/E, fast-growing stock can have a *lower* PEG than a low-P/E, slow grower — so the "expensive" stock is cheaper once you price the growth.

**A9. Why is quality "orthogonal" to value and growth?**
Value/growth is one axis (cheap vs fast-growing); quality (durable ROE, low leverage, stable margins) is an independent axis. You can have cheap junk (value trap), expensive junk (hyped growth), cheap quality (the holy grail), or expensive quality (the compounder). Quality cuts across the value/growth line.

**A10. What does the Fama-French-Carhart regression let you catch?**
Regressing fund returns on market, SMB (size), HML (value), and WML (momentum) strips out return that is merely a buyable factor tilt, isolating the intercept $\alpha$ as true selection skill. It catches a "star manager" who is really a leveraged small-cap-value bet — factor beta masquerading as alpha.

**A11. Why does the diversification benefit have a floor?**
With equal weights, portfolio variance is $\sigma_p^2 = \frac{\sigma^2}{N} + \frac{N-1}{N}\rho\sigma^2$. As $N\to\infty$ the own-variance term vanishes but the covariance term tends to $\rho\sigma^2$ — the systematic floor set by average correlation. Adding stocks past ~20–30 chips at almost nothing while diluting your best ideas.

**A12. Name the SAMURAI criteria for a valid benchmark.**
Specified in advance, Appropriate, Measurable, Unambiguous, Reflective of the manager's opinions, Accountable (owned by the manager), Investable. Benchmark a small-cap fund against Nifty 50 and every downstream metric is meaningless.

---

## Section B — Numerical Problems (full working)

**B1. Active share of a focused fund.**
Benchmark and portfolio weights: A (40% / 30%), B (30% / 45%), C (20% / 25%), D (10% / 0%).
Absolute deviations: |30−40|=10, |45−30|=15, |25−20|=5, |0−10|=10; sum = 40%.
$AS = \tfrac{1}{2}(40\%) = \mathbf{20\%}$.
**Reconcile:** overweights (+15 B, +5 C = +20) exactly offset underweights (−10 A, −10 D = −20), so deviations net to zero and their absolute sum (40%) is exactly twice the active share. Despite dropping D entirely, this is a *low* active-share book — a near-closet-indexer. ✓

**B2. Tracking error and information ratio.**
Quarterly active returns: +1.5%, −0.5%, +2.0%, −1.0%.
Mean $\bar{R_A} = (1.5-0.5+2.0-1.0)/4 = 0.5\%$.
Deviations: +1.0, −1.0, +1.5, −1.5; squared: 1.0, 1.0, 2.25, 2.25; sum = 6.5.
$TE = \sqrt{6.5/(4-1)} = \sqrt{2.1667} = \mathbf{1.47\%}$ per quarter.
Annualise: active return $0.5\%\times4 = 2.0\%$; $TE = 1.47\%\times\sqrt{4} = 2.94\%$.
$IR = 2.0\%/2.94\% = \mathbf{0.68}$.
**Reconcile:** IR of 0.68 is respectable, but achieved with only 20% active share (B1) — small bets, moderate TE, a closet-indexer profile. ✓

**B3. Brinson-Hood-Beebower attribution.**
Two sectors: IT ($w_b$ 50%, $w_p$ 70%, $r_b$ 10%, $r_p$ 12%), Financials ($w_b$ 50%, $w_p$ 30%, $r_b$ 4%, $r_p$ 3%).
Benchmark return $= 0.5(10)+0.5(4) = 7.0\%$. Portfolio return $= 0.7(12)+0.3(3) = 8.4+0.9 = 9.3\%$. Active $= +2.3\%$.
*Allocation* $(w_p-w_b)(r_{b,i}-r_b)$: IT $0.20(10-7)=+0.60$; Fin $(-0.20)(4-7)=+0.60$; total $+1.20\%$.
*Selection* $w_b(r_{p,i}-r_{b,i})$: IT $0.50(12-10)=+1.00$; Fin $0.50(3-4)=-0.50$; total $+0.50\%$.
*Interaction* $(w_p-w_b)(r_{p,i}-r_{b,i})$: IT $0.20(2)=+0.40$; Fin $(-0.20)(-1)=+0.20$; total $+0.60\%$.
**Reconcile:** $1.20+0.50+0.60 = \mathbf{2.30\%}$ = active return computed directly. ✓ Over half came from allocation (overweighting IT, which beat the index) — a top-down profile, not a stock-picker.

**B4. GARP screen via PEG.**
Stock X: P/E 30, growth 25% → PEG $= 30/25 = \mathbf{1.20}$. Stock Y: P/E 18, growth 12% → PEG $= 18/12 = \mathbf{1.50}$.
**X is the better GARP buy** despite the higher headline P/E — you pay less per unit of growth.
**Reconcile:** the "expensive" stock is cheaper once growth is priced in — the classic GARP counter-intuition. ✓

**B5. Diversification floor.**
Each stock $\sigma = 30\%$ ($\sigma^2 = 0.09$), average correlation $\rho = 0.4$, equal weights.
Use $\sigma_p^2 = \frac{\sigma^2}{N} + \frac{N-1}{N}\rho\sigma^2$.
- $N=5$: $0.09/5 + (4/5)(0.4)(0.09) = 0.018 + 0.0288 = 0.0468 \Rightarrow \sigma_p = \mathbf{21.6\%}$.
- $N=20$: $0.0045 + (19/20)(0.036) = 0.0045 + 0.0342 = 0.0387 \Rightarrow \sigma_p = \mathbf{19.7\%}$.
- $N\to\infty$: $\sigma_p^2 \to \rho\sigma^2 = 0.036 \Rightarrow \sigma_p = \mathbf{18.97\%}$.
**Reconcile:** 5→20 stocks cuts risk 1.9 points; 20→infinite cuts only 0.7 more. Most benefit is captured by ~20 names; the ~19% floor is the covariance term you cannot diversify away. ✓

**B6. Effective number of stocks (hidden concentration).**
A 6-stock portfolio: top name 40%, then 20%, 15%, 10%, 10%, 5%.
$\sum w_i^2 = 0.16 + 0.04 + 0.0225 + 0.01 + 0.01 + 0.0025 = 0.245$.
$N_{eff} = 1/0.245 = \mathbf{4.08}$.
**Reconcile:** a raw count of 6 stocks behaves like only ~4 equally weighted names because 40% sits in one position — the Herfindahl gauge exposes concentration the headline count hides. (An equal-weighted 6-stock book would give $N_{eff} = 1/(6\times(1/6)^2) = 6$.) ✓

**B7. Sector active-return contribution.**
IT is 15% of the index; you hold 20%. The IT sector returned 18% while the benchmark returned 9%.
Active weight $= 20\% - 15\% = +5\%$. Contribution $= (w_p-w_b)(r_i - r_b) = 0.05(18\%-9\%) = 0.05\times9\% = \mathbf{+0.45\%}$.
**Reconcile:** overweighting a sector that beat the benchmark by 9 points adds 0.45% to active return — positive because both the active weight and the relative sector return are positive. Had IT lagged the index, the same overweight would have subtracted. ✓

**B8. Information ratio target via the Fundamental Law.**
A quant has $IC = 0.05$ and takes 400 independent bets a year. Estimate IR. Then find the IC a 4-bet macro manager needs for the same IR.
Quant: $IR = IC\sqrt{BR} = 0.05\times\sqrt{400} = 0.05\times20 = \mathbf{1.0}$.
Macro for $IR = 1.0$ with $BR=4$: $IC = IR/\sqrt{BR} = 1.0/2 = \mathbf{0.50}$.
**Reconcile:** the macro manager needs 10x the per-bet skill (0.50 vs 0.05) to match the quant, because breadth (400 vs 4) does the heavy lifting on the quant side. Same equation, opposite ends of the skill-breadth curve. ✓

---

## Section C — Interview-Style Questions (model answers)

**C1. "How do you think about active vs passive?"**
It is a continuum, not a switch. Sharpe's arithmetic says active management is zero-sum before costs and negative-sum after, so passive — harvesting the equity premium at near-zero fee — beats most active managers over long horizons. I only pay for active management where I can name a structural edge: informational, analytical, or behavioural (patience, contrarianism, holding through drawdowns). Absent a named edge, I index the core and spend the risk budget only where the edge is real.

**C2. "A fund has 1.2% fees and 25% active share. Your verdict?"**
Closet indexer — the worst product in the market. Three-quarters of the book is the index, so the client pays a full active fee on a portfolio that is mostly free beta in disguise. The effective fee on the genuinely active quarter is roughly 5%. I'd either demand far higher active share for that fee or replace it with a cheap index fund plus a small high-conviction satellite.

**C3. "Tracking error and active share — aren't they the same?"**
No. Tracking error is return-based: the volatility of active return, how bumpy the ride relative to the index has been. Active share is holdings-based: how much of the portfolio's *positions* differ from the index right now. They can diverge sharply — a diversified stock-picker holding 100 idiosyncratic bets has high active share but low TE because the bets wash out; a manager making two big sector bets has low active share but high TE. You need both to characterise a manager: one is active *positioning*, the other active *risk*.

**C4. "A manager beat the benchmark by 3% last year. How do you tell skill from luck?"**
Two moves. First, Brinson attribution — split the 3% into allocation (sector-weight bets) and selection (stock picks) and confirm it reconciles to the total; that tells me *what* they were right about and whether it matches their stated process. Second, a Fama-French-Carhart regression — if the 3% collapses once I control for size, value, and momentum, it was a factor tilt I can buy for 30 bps, not alpha. Real skill is a positive intercept that survives the factor controls, repeated across enough independent periods to clear the luck threshold.

**C5. "Why not just hold 200 stocks to be safe?"**
Because diversification is nearly free up to ~25 names and nearly useless past that. Portfolio variance falls like $1/N$ on the idiosyncratic term but converges to the average-covariance floor set by correlation — beyond ~30 stocks you cut almost no risk while diluting your best ideas toward the index. Over-diversification is a real cost: you drift into closet indexing and pay active fees for index performance. Concentration is a deliberate bet that your per-bet skill justifies giving up breadth.

**C6. "Value or growth — which do you prefer, and is that even the right question?"**
It is an incomplete question, because quality is an independent axis. I care less about the value/growth label than about paying a sensible price for durable earnings — which is why GARP and quality-value strategies cut across the divide. Value works when the market over-extrapolates bad news, but its risk is the value trap: cheap because the business is dying. Growth works when the market under-appreciates the duration of growth, but its risk is multiple compression when growth disappoints. I'd rather own cheap quality than argue the label.

**C7. "What's the single most important number on a fund fact sheet to you?"**
Active share relative to fee, closely followed by the information ratio. Active share tells me whether I'm actually buying a differentiated product or the index in disguise; the IR tells me whether the active risk has been rewarded with skill. A fund with high active share and a consistently positive IR is taking real, well-sized bets and getting paid for them — that is the entire job described in two numbers.

**C8. "Explain the Fundamental Law of Active Management to a client."**
Your information ratio — skill per unit of active risk — is roughly your accuracy per bet times the square root of how many independent bets you make. So there are two honest ways to be good: be very right on a handful of calls, or be slightly right across hundreds of uncorrelated ones. A focused fund of 20 names is betting on depth; a systematic fund of 400 is betting on breadth. Neither is inherently better; what fails is being mediocre on few bets — low skill and low breadth.

---

## Section D — MCQs (with reasoning)

**D1.** Active share is calculated as:
(a) $\sigma(R_p-R_b)$ (b) $\tfrac{1}{2}\sum|w_p-w_b|$ (c) $\sum w_i^2$ (d) $(R_p-R_b)/TE$
**Answer: (b).** Half the sum of absolute active weights, a holdings-based measure. (a) is tracking error, (c) relates to the Herfindahl/$N_{eff}$, (d) is the information ratio.

**D2.** Before costs, the average actively managed rupee earns:
(a) more than the index (b) exactly the index return (c) the risk-free rate (d) less than the index
**Answer: (b).** Sharpe's arithmetic — active managers in aggregate are the market, so they net to the index *before* costs. Only *after* fees does the average active rupee fall below passive (option d describes the after-cost result).

**D3.** A fund with high active share but low tracking error is best described as:
(a) a closet indexer (b) a concentrated stock picker (c) a diversified stock picker (d) a factor bettor
**Answer: (c).** Many small, idiosyncratic bets differ from the index (high AS) yet wash out at the portfolio level (low TE). Closet indexer = low AS; concentrated picker and factor bettor = high TE.

**D4.** Stock X has P/E 30 and growth 25%; Stock Y has P/E 18 and growth 12%. On PEG:
(a) Y is cheaper (b) X is cheaper (c) equal (d) PEG cannot compare them
**Answer: (b).** PEG X $= 1.20$ < PEG Y $= 1.50$. X pays less per unit of growth despite the higher multiple — the GARP counter-intuition.

**D5.** In Brinson attribution, the allocation effect for a sector is:
(a) $w_b(r_p-r_b)$ (b) $(w_p-w_b)(r_p-r_b)$ (c) $(w_p-w_b)(r_{b,i}-r_b)$ (d) $w_p(r_p-r_b)$
**Answer: (c).** Allocation isolates the sector-weight bet against the sector's benchmark return relative to the total benchmark. (a) is selection, (b) is interaction.

**D6.** As the number of equally weighted stocks grows without limit, portfolio variance tends to:
(a) zero (b) the average variance (c) the average covariance $\rho\sigma^2$ (d) the market variance
**Answer: (c).** The own-variance term dies like $1/N$; what remains is the average covariance $\rho\sigma^2$ — the systematic floor diversification cannot remove.

**D7.** The information ratio is defined as:
(a) $(R_p-R_f)/\sigma_p$ (b) $(R_p-R_b)/TE$ (c) $(R_p-R_f)/\beta_p$ (d) $IC\times BR$
**Answer: (b).** Active return per unit of tracking error. (a) is Sharpe, (c) is Treynor, (d) misstates the Fundamental Law (it uses $\sqrt{BR}$, not $BR$).

**D8.** A "star" manager's excess return disappears after a Fama-French-Carhart regression. This means:
(a) genuine alpha (b) the return was a factor tilt (c) negative skill (d) a data error
**Answer: (b).** The return was explained by size, value, or momentum exposure — buyable cheaply as smart beta — leaving no intercept alpha. It was beta in disguise, not selection skill.

**D9.** Which best captures hidden concentration in a portfolio?
(a) raw stock count (b) tracking error (c) $N_{eff} = 1/\sum w_i^2$ (d) active share
**Answer: (c).** The effective number of stocks (inverse Herfindahl) falls far below the raw count when weights are lopsided, exposing concentration a headline count misses.

**D10.** The Fundamental Law implies a manager can achieve a high information ratio by:
(a) high skill on few bets only (b) many independent bets only (c) either high per-bet skill or high breadth (d) raising fees
**Answer: (c).** $IR \approx IC\sqrt{BR}$ — a strong record can come from deep skill on few bets or modest skill across many independent ones, which is why focused pickers and diversified quants both exist.

---

*End of Chapter 09 Q&A. Drill Section B until active share, tracking error, IR, Brinson attribution (reconciling to the basis point), PEG, and the diversification floor are reflexive — and be ready to name a fund's profile from its active-share/TE quadrant on demand.*
