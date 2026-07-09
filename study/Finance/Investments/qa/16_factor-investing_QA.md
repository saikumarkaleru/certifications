# Q&A — Factor Investing and Smart Beta

> Scope: Investments — Chapter 16 (Factor Investing and Smart Beta). Every question is followed by a full model answer. All rates are annual and in percent unless stated. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** applied/numerical (full step-by-step, reconciling) · **C** interview-style with model answers · **D** MCQs with reasoning.

---

## The chapter in one line

**One-line statement:** Factor investing harvests a handful of persistent return drivers — value, size, momentum, quality, low-volatility — through cheap, transparent, rules-based portfolios; **smart beta** is its ETF wrapper, sitting between pure passive indexing and expensive discretionary active management.

---

## Section A — Concept Check

**A1. What is a "factor," and what distinguishes it from an ordinary stock characteristic?**
A factor is a broad, **persistent, quantifiable** characteristic that helps explain the risk and return of a *group* of securities. A real factor clears five hurdles: persistence (works over long periods), pervasiveness (across countries, sectors, asset classes), robustness (survives changes in definition), investability (survives real trading costs), and an intuitive economic rationale. A characteristic that sorts returns in one back-test but has no economic story is a data-mining artifact, not a factor.

**A2. Define smart beta and place it on the passive–active spectrum.**
Smart beta (also "strategic beta" or "factor ETFs") is any **rules-based index that deliberately departs from market-cap weighting** to tilt toward one or more factors. It occupies the middle of the spectrum: the transparency and low cost of indexing, with the factor tilts once sold as expensive active skill. It is passive in *implementation* (mechanical rules, no discretion) but active in *exposure* (a real bet against the cap-weighted market).

**A3. The chapter claims "cap-weighting is itself a bet." Explain.**
A market-cap index automatically buys *more* of whatever has risen (the biggest, most expensive names) and *less* of what has fallen, embedding a built-in **large-size and momentum tilt**. There is no bet-free equity portfolio; the real choice is not "bet vs no bet" but "*which* bet, made deliberately or by accident."

**A4. Give the two competing rationales for why a factor premium persists.**
(1) **Risk-based (rational):** compensation for a systematic risk you cannot diversify away — value stocks are distressed, cyclically fragile firms that hurt precisely in recessions, so investors demand payment; the premium is permanent because the risk never disappears. (2) **Behavioral (mispricing):** persistent human errors (over-extrapolation, under-reaction) that limits to arbitrage prevent smart money from fully correcting; the premium *can* decay once discovered and crowded. Mature practitioners treat most factors as a **blend**.

**A5. Why does the risk-vs-behavioral debate matter for how you hold a factor?**
It changes expectations in a drought. If value is pure risk compensation, hold through the pain and expect the premium to endure. If it is pure mispricing, worry that post-publication crowding erodes it. Since the truth is usually a blend, expect real compensation but stay alert to crowding.

**A6. Name the five workhorse equity factors and their classic signal.**
Value (book-to-market / low P/E), Size (market cap), Momentum (12-month return skipping the most recent month, "12-1"), Quality (profitability, low debt), Low Volatility (low beta).

**A7. What are HML, SMB, WML, RMW, and CMA?**
Academic long-short factor portfolios. **HML** (High Minus Low) = value (long cheap, short expensive by B/M). **SMB** (Small Minus Big) = size. **WML/UMD** (Winners Minus Losers) = momentum, added by Carhart (1997). **RMW** (Robust Minus Weak, profitability) and **CMA** (Conservative Minus Aggressive, investment) are the two quality-adjacent factors from Fama-French's 2015 five-factor model.

**A8. Why is size the weakest and most contested of the classic factors?**
The raw size premium is small, concentrated in tiny illiquid micro-caps, largely evaporates after costs, and has been near-zero since the early 1980s. Research (AQR's "Size Matters, If You Control Your Junk") argues size only works once you strip out low-quality "junk" firms — so it needs a **quality filter** to shine and is barely a standalone premium.

**A9. Why does momentum have the highest average premium yet frighten practitioners?**
Momentum has historically earned ~8%+ but suffers rare, violent **crashes** with fat left-tail skew. After a market crash the "loser" leg fills with beaten-down cyclicals; a V-shaped rebound sends those losers rocketing and the short leg blows up — March–May 2009 saw momentum lose 30%+ in weeks.

**A10. Why do quality and value pair so well together?**
They are complementary. Cheap-and-junky is a **value trap**; cheap-and-high-quality is the sweet spot. A quality filter (profitable, low-debt) screens out distressed value firms that keep sinking, and quality is defensive — so the combination historically improves both return and risk versus either alone.

**A11. Why is the low-volatility factor a direct rebuke to CAPM?**
CAPM says higher beta *must* earn higher return; the low-vol anomaly shows low-beta stocks deliver returns as high as or higher than high-beta stocks on a risk-adjusted basis. Explanations: leverage constraints (Frazzini-Pedersen "Betting Against Beta" — investors who cannot lever overpay for high-beta stocks), lottery-ticket demand, and agency (benchmarked managers shun low-beta names for tracking-error reasons).

**A12. What is the "factor zoo," and how do you defend against it?**
The 400+ published "factors," most of which are data-mining artifacts that fail out-of-sample. The defense is discipline: demand a credible economic story, out-of-sample and cross-country evidence, robustness, and low correlation with factors you already own. A fifth correlated value-variant adds cost and noise, not diversification.

**A13. Distinguish a long-short factor portfolio from a long-only tilt.**
A **long-short** portfolio goes long the high-scoring quintile and short the low-scoring quintile, isolating the *pure*, market-neutral factor return (how academics measure HML, SMB). A **long-only tilt** overweights high-scoring and underweights low-scoring names within a fully invested portfolio (no shorting). Most retail factor ETFs are long-only tilts, carrying market beta plus a diluted dose of the factor.

**A14. Why is "growth" not a factor in the way value is?**
Value is a documented, rewarded premium; "growth" is simply the *absence* of value — the expensive leg of the sort — not a separately rewarded premium. There is no robust "growth premium." What looks like growth's dominance (e.g., 2010–2020) is usually momentum + quality + a low-rate regime, not a factor of its own.

---

## Section B — Applied / Numerical Problems

**B1. Carhart four-factor attribution — how much is real alpha?**
A manager returns 13.5% when R_f = 4.0%. Given the loadings and the year's realized factor premia, compute each contribution and the residual alpha.

| Factor | Loading β | Premium | Contribution |
|---|---|---|---|
| Market | 1.05 | 7.0% | ? |
| SMB | 0.40 | 1.5% | ? |
| HML | 0.55 | 3.0% | ? |
| WML | –0.20 | 5.0% | ? |

**Solution.** Excess return = 13.5% − 4.0% = **9.5%**.
- Market: 1.05 × 7.0% = 7.35%
- SMB: 0.40 × 1.5% = 0.60%
- HML: 0.55 × 3.0% = 1.65%
- WML: −0.20 × 5.0% = −1.00%
- Total factor-explained = 7.35 + 0.60 + 1.65 − 1.00 = **8.60%**

Alpha = 9.5% − 8.6% = **0.9%**. Of the 9.5% "outperformance," 8.6 points are replicable factor beta buyable for ~20 bps; only 0.9% is genuine skill. The negative momentum loading *cost* 1.0% because momentum was positive that year — a value manager leaning away from recent winners bleeds return when momentum works.

**B2. Two-factor diversification — the Sharpe uplift.**
Value and Momentum each have a premium of 5% and volatility of 14%, correlation ρ = −0.3. Find the volatility and premium-to-vol ratio of a 50/50 blend versus a single factor.

**Solution.** Blend premium = **5%** (unchanged).
$$\sigma_p=\sqrt{0.5^2(0.14^2)+0.5^2(0.14^2)+2(0.5)(0.5)(-0.3)(0.14)(0.14)}$$
- Term 1 = 0.25 × 0.0196 = 0.0049
- Term 2 = 0.25 × 0.0196 = 0.0049
- Term 3 = 2 × 0.25 × (−0.3) × 0.0196 = −0.00294
- Sum = 0.0049 + 0.0049 − 0.00294 = 0.00686
- σ_p = √0.00686 = **8.28%**

Ratio single factor = 5/14 = **0.357**; ratio blend = 5/8.28 = **0.604** — a **69% improvement** with no drop in expected return. The negative correlation smooths value's droughts (momentum often thrives when value suffers): the core quantitative case for multi-factor investing.

**B3. Smart-beta tilt construction.**
Cap-weighted benchmark: X 50%, Y 30%, Z 20%. Combined value+quality z-scores: X −0.6, Y +1.0, Z +0.4. Tilt rule: new weight = cap weight × (1 + 0.5 × score), then renormalize. Find tilted weights and active bets.

**Solution.** Step 1 — multipliers:
- X: 50% × (1 + 0.5×−0.6) = 50% × 0.70 = 35.0%
- Y: 30% × (1 + 0.5×1.0) = 30% × 1.50 = 45.0%
- Z: 20% × (1 + 0.5×0.4) = 20% × 1.20 = 24.0%

Step 2 — sum = 35 + 45 + 24 = **104.0%**. Renormalize (÷1.04):
- X: 35.0/1.04 = **33.65%** → active −16.35%
- Y: 45.0/1.04 = **43.27%** → active +13.27%
- Z: 24.0/1.04 = **23.08%** → active +3.08%

Check: 33.65 + 43.27 + 23.08 = 100.0% ✓. The rule mechanically overweights the high-scoring Y and slashes the low-scoring X — transparent and judgment-free, exactly how a smart-beta index rebalances.

**B4. Fee arithmetic — paying alpha fees for beta.**
Using B1 (gross alpha 0.9%), the manager charges 1.10%; an equivalent smart-beta ETF charges 0.25%. Net alpha after fee = 0.9% − 1.10% = **−0.20%** — the client is *net negative* on skill, and overpays 1.10% − 0.25% = **0.85%** for beta available cheaply. The heart of the fee-compression argument.

**B5. Momentum crash — asymmetric payoff.**
A momentum long-short book returns +1.2% per month in 11 months but −28% in a single crash month. Annual arithmetic return?

**Solution.** 11 × 1.2% = +13.2%; plus −28% → **−14.8%** for the year. Despite a positive premium in most months, one fat-tail crash wipes out more than a year of gains — momentum's **negative skew** means standard deviation understates its true risk.

---

## Section C — Interview-Style Questions

**C1. "In one minute, what is factor investing and why did it disrupt the fund industry?"**
Factor investing systematically harvests the handful of persistent return drivers — value, size, momentum, quality, low-vol — through cheap, rules-based portfolios. It disrupted the industry by revealing that much of what active managers charged 1%+ for was not alpha but *replicable factor beta* you could buy for 10–40 bps. Once value and momentum were shown to be harvestable, transparent premia, the discretionary "genius" premium collapsed, and smart-beta ETFs packaged those tilts for retail — compressing fees industry-wide.

**C2. "A manager beat the S&P by 4% last year. How would you tell if that's skill?"**
Run a factor attribution — a Carhart four-factor regression (market, size, value, momentum), ideally extended with quality and low-vol. Estimate the fund's loadings, multiply each by the factor's realized premium, and sum. Whatever the factors explain is *beta*, not skill; the residual is alpha. If 3.5 of the 4 points come from a value-plus-small tilt, the manager delivered only 0.5% of true alpha — and if fees exceed that, the client pays alpha prices for beta. I'd also insist on multi-year data, since one year is noisy.

**C3. "Is a factor premium a free lunch?"**
No. Under the risk view it is compensation for *real pain* in bad times — value crashes in recessions, momentum crashes on sharp rebounds — so you are paid to hold assets that hurt when you can least afford it. Under the behavioral view it is a mispricing that *can decay* once discovered and crowded. Either way you endure uncomfortable positions and long droughts; the premium rewards that discomfort, not a costless edge.

**C4. "Why bother with multiple factors instead of just picking the best one?"**
Two reasons. First, factor timing is notoriously unreliable. Second, factors are cyclical and their premia are often low or negatively correlated: value and momentum run about −0.3 to −0.4 because value buys losers while momentum buys winners. Combining them raises risk-adjusted return materially — the premium-to-vol ratio can jump from ~0.35 to ~0.60 with no loss of expected return. Diversifying across return *drivers* is the most reliable edge in factor investing.

**C5. "What are the main ways factor investing can disappoint an investor?"**
Long droughts (value lagged growth roughly 2010–2020); sharp crashes (momentum lost ~30% in weeks in spring 2009); factor decay from crowding after publication and ETF launch; hidden concentration (low-vol overweights utilities and staples, adding rate sensitivity); and the factor zoo — data-mined "factors" with no real premium. Long-only retail ETFs also deliver a diluted factor dose plus full market beta, so the tilt is weaker than clients assume.

**C6. "A client says smart beta is passive and therefore low-risk. Respond."**
Smart beta is passive in *implementation* — mechanical rules, no discretion — but an *active bet* relative to the cap-weighted market. A value ETF that trails growth for a decade delivers real, painful underperformance. Passive implementation means transparency and low cost, not low risk. The exposure is deliberately non-market, and that is where both the risk and the reward live.

**C7. "Who are the real-world players, and what should I know about them?"**
MSCI and FTSE Russell build the factor indices; iShares (BlackRock), Vanguard, and Invesco run the big smart-beta ETFs. On the factor-purist end, DFA (Dimensional), Avantis, AQR, and Research Affiliates (which popularized "Fundamental Indexing") are essentially "factor premia in a fund" shops. Factor investing is a large, competitive industry — and that competition is one source of the crowding risk that compresses premia.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Which best describes where smart beta sits?**
A. It is identical to a cap-weighted index fund.
B. It is a rules-based index that tilts away from cap-weighting toward factors.
C. It is a discretionary active strategy.
D. It is a leveraged derivatives overlay.

**Answer: B.** Smart beta is rules-based (unlike discretionary active, C) but departs from cap-weighting (unlike A) to capture factor tilts; it needs no leverage or derivatives (D). It sits in the middle of the passive–active spectrum.

**D2. The low-volatility anomaly is significant primarily because it:**
A. Confirms the CAPM prediction that beta drives return.
B. Contradicts CAPM by showing low-beta stocks are not rewarded with lower returns.
C. Proves markets are perfectly efficient.
D. Is only observable in emerging markets.

**Answer: B.** CAPM predicts higher beta → higher return; the low-vol anomaly shows low-beta stocks earn as much or more on a risk-adjusted basis, contradicting CAPM (A wrong). It appears across developed and emerging markets (D wrong) and is evidence *against* strict efficiency (C wrong).

**D3. The standard momentum signal is:**
A. Past 1-month return.
B. Past 12-month return including the most recent month.
C. Past 12-month return skipping the most recent month (12-1).
D. Forecast next-year earnings growth.

**Answer: C.** Momentum uses the past 12-month return but *skips the most recent month* to avoid short-term reversal. Including month −1 (B) mixes in reversal; a 1-month signal (A) is reversal; D is a growth forecast.

**D4. Which factor is considered the weakest and most contested?**
A. Value  B. Momentum  C. Size  D. Quality

**Answer: C.** The size premium is small, concentrated in illiquid micro-caps, largely gone after costs, and near-zero since the early 1980s; it only works with a quality filter to remove "junk" small caps. Value, momentum, and quality have stronger evidence.

**D5. Value and momentum are frequently combined because their returns are:**
A. Perfectly positively correlated.
B. Negatively (or lowly) correlated, improving diversification.
C. Uncorrelated with the market.
D. Identical in every period.

**Answer: B.** Value buys recent losers while momentum buys recent winners, so they tend to be negatively (≈ −0.3 to −0.4) or lowly correlated. Combining them lowers volatility and raises risk-adjusted return without cutting expected return — the classic multi-factor diversification benefit. A and D are false; C misstates the reason.

**D6. In a Carhart four-factor attribution, "alpha" is:**
A. The fund's total return.
B. The market's return.
C. The residual return not explained by the four factor exposures.
D. The largest single factor contribution.

**Answer: C.** Alpha is the residual — excess return minus the sum of (loading × factor premium) across the four factors — measuring skill relative to those factors. Not total return (A), the market leg (B), or a single factor's contribution (D).

**D7. "Cap-weighting is itself a bet" because a cap-weighted index:**
A. Equally weights every stock.
B. Mechanically overweights the largest, best-performing (often most expensive) stocks.
C. Rebalances daily into losers.
D. Holds only value stocks.

**Answer: B.** Cap-weighting buys more of whatever has risen and grown largest, embedding a large-size and momentum tilt. It does not equal-weight (A), tilt into losers (C), or hold only value (D). Even "neutral" indexing is an implicit bet.

**D8. A "real" factor should clear all of the following EXCEPT:**
A. Persistence across long periods.
B. Pervasiveness across markets and asset classes.
C. Guaranteed positive return every single year.
D. A credible economic (risk or behavioral) rationale.

**Answer: C.** No factor returns positively every year — all suffer droughts and some crash; that variability is the risk you are paid for. The genuine hurdles are persistence, pervasiveness, robustness, investability, and rationale (A, B, D).

**D9. The primary danger of the "factor zoo" is:**
A. Too few published factors to choose from.
B. Most published factors are data-mining artifacts that fail out-of-sample.
C. Factors are impossible to compute.
D. Regulators ban most factors.

**Answer: B.** With 400+ published factors, most are statistical flukes that vanish out-of-sample. The defense: require an economic story, out-of-sample evidence, robustness, and low correlation with existing factors. A, C, D misstate the problem.

**D10. The most defensible reason to prefer multi-factor over single-factor investing is:**
A. It guarantees a higher return every year.
B. Factor timing is unreliable, and low/negative cross-factor correlations raise risk-adjusted returns.
C. It eliminates all market risk.
D. It removes the need to pay any fees.

**Answer: B.** Timing factors is notoriously hard, and factors are cyclical with low/negative correlations, so combining them lifts risk-adjusted return without sacrificing expected return. No annual guarantee (A), market risk remains in long-only form (C), fees still apply (D).

---

## Self-check summary

Numerical answers reconcile: B3 tilted weights sum to 100%; B1 alpha = 9.5% − 8.6% = 0.9%; B2 blend vol 8.28% < 14% single-factor. Every question has a full worked answer; coverage maps to chapter sections 2–6 and the section-10 interview points.
