# Backtesting a TA System & Performance Metrics

## What it is & why it works

Backtesting is the process of applying your trading rules to historical price data to estimate how the system would have performed before you risk a single rupee live. It is the bridge between a plausible-sounding idea ("buy Nifty pullbacks to the 20-EMA in an uptrend") and evidence that the idea actually has an edge. Without it, you are trading a hypothesis with real money and calling the market your test lab — an expensive way to learn.

Why does backtesting work — and where are its limits? It works because markets, while unpredictable trade-by-trade, exhibit repeatable *statistical* tendencies. Trends persist more often than pure randomness would suggest; volatility clusters; support and resistance levels attract price because thousands of participants watch them. If your rules exploit a genuine tendency, a large sample of historical trades will reveal it as a positive expectancy that is *stable* across time and market conditions. The keyword is stable. A single good year proves nothing; an edge that shows up in 2019's trend, 2020's crash-and-recovery, 2022's chop, and 2023–24's grind is far more likely to be real.

But backtesting has a fundamental honesty problem: it is trivially easy to fool yourself. The past is *known*, and a determined analyst can always tweak parameters until the equity curve looks beautiful. That curve is then a description of past noise, not a prediction of future edge. So the discipline of backtesting is really the discipline of *not lying to yourself* — using out-of-sample data, keeping parameters few, modelling costs honestly, and judging the system by robust metrics rather than the headline return. A backtest's job is not to make you excited; it's to give you a realistic, sobering estimate of expectancy *and* the drawdown you'll have to survive to collect it.

In the Indian context, backtesting is both easier and trickier than it looks. Easier because clean historical data for Nifty, Bank Nifty, and F&O stocks is widely available (NSE, TradingView, and data vendors). Trickier because options data (the instrument many Indians actually trade) is messy — historical IV, bid-ask spreads, and STT make an options backtest much harder to model faithfully than a futures or cash backtest. A common, pragmatic compromise is to backtest the *signal* on the underlying (Nifty futures) and then stress-test whether option execution can capture that edge after theta and costs.

## The mechanics — how to run a rigorous backtest

A rigorous backtest has a fixed procedure. Cutting corners on any step produces a pretty but useless result.

**1. Fully specify the rules.** Every one of the seven system components (universe, timeframe, regime filter, setup, entry, stop, target/management, sizing) must be objective enough to code or to apply identically by hand. If a rule requires judgement ("enter when it looks strong"), you cannot backtest it honestly.

**2. Choose the data and split it.** Get clean historical data covering *multiple regimes* — ideally 5+ years spanning trends, crashes, and ranges. Then split it: reserve the most recent ~30% as **out-of-sample** data you do *not* look at while designing. Build and tune on the in-sample portion; validate on the out-of-sample. If performance collapses out-of-sample, you curve-fitted.

**3. Model execution realistically.** Assume you enter at the *next* candle's open or a realistic fill, not the exact signal price. Add slippage (a point or two on Nifty, more on illiquid stocks) and full round-trip costs: brokerage, STT (heavy on options — roughly 0.0625% on sell-side option premium plus other charges), exchange and SEBI fees, GST, and stamp duty. For an intraday options system these costs can consume 20–40% of gross edge; ignoring them is the single most common way backtests lie.

**4. Avoid look-ahead and survivorship bias.** *Look-ahead bias* is using information not available at decision time — e.g., using the day's close to decide a trade you'd have taken at midday, or using a revised indicator. *Survivorship bias* is testing on today's Nifty 50 constituents over ten years, forgetting that the index membership changed and the losers were removed. Use point-in-time universes.

**5. Record every trade.** Entry, exit, R-multiple, date, and regime. The output is a *trade log*, from which all metrics are computed.

**6. Walk-forward, not just one backtest.** The gold standard is walk-forward analysis: optimise on a window (say 2019–2021), test on the next (2022), roll forward, and repeat. This simulates how you'd actually re-tune over time and is far more honest than a single optimisation over the whole history.

Here is a table of the biases and their fixes:

| Bias | What it does | Fix |
|---|---|---|
| Curve-fitting / over-optimisation | Fits past noise, fails live | Few round parameters; out-of-sample test |
| Look-ahead | Uses future info at decision time | Enter on next candle; lag indicators |
| Survivorship | Tests only today's survivors | Point-in-time constituent lists |
| Ignoring costs | Overstates net edge | Model STT, slippage, brokerage |
| Small sample | Random luck looks like edge | Require 100+ trades across regimes |

A minimum sample of **100 trades** is a rough floor for statistical meaning; 200+ across different years is better. A dazzling system with 18 trades tells you almost nothing.

## Reading it — a worked Nifty backtest, phase by phase

Let's backtest the trend-pullback system from the previous chapter on Nifty futures, daily-swing version, over 2019–2024, and read the output honestly. Capital Rs 10,00,000; risk 0.75% (Rs 7,500) per trade.

**Phase 1 — In-sample build (2019–2022).** Applying the rules to daily Nifty, the system fires 84 trades. Wins: 42 (50%). Average winner: +1.9R; average loser: −1.0R. Gross expectancy per trade = (0.50 × 1.9) − (0.50 × 1.0) = 0.95 − 0.50 = **+0.45R**. On Rs 7,500 risk, that's about Rs 3,375 expected profit per trade before costs. Looks promising.

**Phase 2 — Cost adjustment.** Round-trip costs on a Nifty futures swing trade are small relative to the move (a few hundred rupees), trimming expectancy to roughly +0.42R. Costs barely dent a swing-futures system — but note that the *same* signal traded via weekly ATM options would bleed far more to theta and STT, which is why instrument choice matters.

**Phase 3 — Out-of-sample validation (2023–2024).** Now the honest test. On the untouched 2023–24 data the system fires 51 trades, wins 24 (47%), average winner +1.8R, loser −1.0R. Expectancy = (0.47 × 1.8) − (0.53 × 1.0) = 0.846 − 0.53 = **+0.32R**. Lower than in-sample (as expected — some in-sample shine was luck), but *still positive*. This degradation-but-survival pattern is exactly what a genuine edge looks like. A curve-fitted system would have gone *negative* out-of-sample.

**Phase 4 — Reading the equity curve and drawdown.** Plotting cumulative R across all 135 trades, the curve rises but not smoothly. There's a stretch in mid-2022 (choppy market) of 6 consecutive losers — a **−6R drawdown**, about −4.5% of capital at 0.75% risk. There's another shallow dip in early 2024. The *maximum drawdown* is the deepest peak-to-trough decline: here about −6.2R (≈ −4.6%). This number is more important than the total return, because it's what you must emotionally and financially survive.

**Phase 5 — Regime attribution.** Splitting trades by regime shows the truth: in trending stretches the system made +0.6R/trade; in the range-bound 2022 middle it made −0.1R/trade. The edge is *entirely* a trend-following edge. That immediately suggests an improvement — a stricter regime filter to stand aside in ranges — and warns that a prolonged rangebound year will be flat-to-losing. That is honesty the raw return number would hide.

What the backtest tells us: a modest, *real* positive expectancy (~+0.3R net out-of-sample), a survivable ~5% max drawdown, and a clear dependence on trending regimes. That is a tradeable — if unglamorous — system. Most real edges look like this. Anything claiming +2R per trade with a 5% win-rate-of-70% and tiny drawdown is almost certainly fitted.

## Trading it — turning metrics into position and expectation management

A backtest is not just a go/no-go stamp; its numbers directly configure how you trade the system live.

**Sizing from drawdown, not hope.** The backtest said max drawdown was ~6R. Live drawdowns are usually *worse* than backtested (markets find new ways to hurt you), so plan for 1.5–2× — say 10–12R, or ~8–9% of capital at 0.75% risk. If an 8–9% account dip would make you abandon the system, your size is too big; drop risk to 0.5% per trade. The metric sets the size.

**Expectancy sets your realistic return.** At +0.32R net and, say, 25 trades a year, expected annual return in R is 25 × 0.32 = 8R ≈ 6% of capital at 0.75% risk. That's a *swing* system on the index alone; leverage via futures or adding more instruments scales it, but so does the drawdown. Knowing this prevents the fantasy of "10% a month" that blows up beginners.

**Scenario planning from the trade distribution.** The backtest gives you the *distribution* of outcomes, so you can rehearse:
- *Normal streak of 4–5 losers* — expected several times a year; you keep trading unchanged.
- *Drawdown exceeds backtested max by 50%* — a yellow flag; reduce size and investigate regime.
- *Drawdown exceeds 2× backtested max* — a red flag; the edge may have decayed or regime shifted structurally; stop and re-validate.

This turns the emotional experience of losing into a pre-decided, mechanical response — the single biggest practical benefit of having backtested.

**Forward-testing (paper) before capital.** Between backtest and full size, run the system *live on paper* (or micro-size) for 20–40 trades. This catches execution problems the backtest couldn't model — slippage on real fills, the psychological difficulty of taking the signal, data-feed lag. Only after forward results roughly match the backtest do you scale to full size.

## Confluence — combining metrics for a true picture (and with option data)

No single metric describes a system; they must be read together, because each can be gamed in isolation.

- **Win rate** alone is meaningless — a 90% win rate with tiny wins and rare huge losses (selling naked options) is a disaster waiting to happen; a 40% win rate with 2.5R winners is excellent.
- **Reward:risk / average R** must be paired with win rate. Together they give **expectancy** = (Win% × AvgWin) − (Loss% × AvgLoss), the single most important number.
- **Profit factor** = gross profit ÷ gross loss; above 1.5 is good, above 2.0 is strong. Robust because it's less sensitive to a single outlier than average R.
- **Maximum drawdown** and **drawdown duration** describe survivability — how deep and how *long* the pain lasts. A system can be net profitable yet spend 14 months underwater, which few can psychologically tolerate.
- **Sharpe / risk-adjusted return** normalises return by volatility, letting you compare systems.
- **Expectancy per unit time** (R per month) matters because a +0.5R system trading weekly beats a +0.8R system trading twice a year.

Here is the metric cheat-sheet:

| Metric | Formula / meaning | Healthy zone |
|---|---|---|
| Expectancy (R) | (W% × avgWin) − (L% × avgLoss) | > +0.2R net |
| Profit factor | gross profit / gross loss | > 1.5 |
| Win rate | wins / total | context-dependent |
| Max drawdown | deepest peak-to-trough | survivable (< ~15%) |
| Payoff ratio | avgWin / avgLoss | > 1.5 for low win-rate systems |
| Sharpe | return / volatility | > 1 is decent |

**Confluence with option-chain and volatility data** sharpens a backtest's interpretation in India. If your system's losing clusters coincide with *high-IV* (India VIX spikes) periods, that's actionable — add an IV filter or reduce size when VIX > 20. If wins concentrate around expiry weeks, that hints at an option-flow tailwind worth isolating. And critically, before trusting a *signal* backtested on futures to be tradeable via options, overlay the option cost: a +0.3R futures signal that needs three days to play out may be net *negative* in a weekly ATM option because theta decay eats the premium — so the metric that matters is expectancy *in the instrument you'll actually trade*.

## Pitfalls & false signals — where backtests deceive

**The beautiful curve trap.** The prettier and smoother the backtested equity curve, the more suspicious you should be. Real edges are lumpy. A curve that never draws down is almost always over-optimised or contains look-ahead bias.

**Optimising to the peak.** If your best parameter is 20-EMA making 40R but 18 and 22 both make 5R, you've found a *fragile spike* in a noisy landscape — it will not repeat. A robust parameter sits on a broad *plateau* where neighbouring values also work. Always test a range and prefer plateaus over peaks.

**Ignoring costs and slippage.** Bears repeating because it kills more retail options systems than anything else. STT on the sell side of options, bid-ask slippage on non-index strikes, and impact cost on illiquid stocks routinely turn a "profitable" backtest into a live loser. Model them pessimistically.

**Data-snooping across many systems.** If you backtest 50 different systems and pick the best, that "best" is partly luck — with enough tries, something looks great by chance. The fix is out-of-sample validation and demanding a *structural reason* the edge should exist.

**Non-stationary markets.** Markets evolve. A microstructure edge from 2015 may be arbitraged away by 2025's algos. Options behaviour changed with weekly expiries and later with expiry-day rule tweaks. A backtest over old data may describe a market that no longer exists — hence walk-forward testing and periodic re-validation.

**Confusing backtest with guarantee.** Even a perfectly-run backtest gives a *probability distribution*, not a promise. The future will contain a regime the past didn't. Position sizing (never risking ruin) is what protects you when the backtest's assumptions eventually break — which they will.

**Too-small samples and single-market fit.** A system that only worked on Bank Nifty and nowhere else may be fitted to Bank Nifty's specific past. Testing the same logic across Nifty, Fin Nifty, and several stocks builds confidence that you've found a *principle*, not a coincidence.

## Interview-ready summary

Backtesting applies fully-specified rules to historical data to estimate a system's expectancy and, crucially, its drawdown — before risking capital. It works because markets have repeatable statistical tendencies, but it's dangerously easy to fool yourself, so rigour means: objective rules, multi-regime data split into in-sample (build) and out-of-sample (validate), realistic execution with full costs (STT, slippage) modelled, avoidance of look-ahead and survivorship bias, a sample of 100+ trades, and ideally walk-forward analysis. Judge the system by a *combination* of metrics, never one alone: expectancy = (Win% × AvgWin) − (Loss% × AvgLoss) as the headline, plus profit factor (>1.5), payoff ratio, and above all maximum drawdown and its duration, which define survivability. A genuine edge degrades but stays positive out-of-sample; a curve-fitted one goes negative. In India, backtest the signal on the underlying but check expectancy *in the instrument you'll actually trade* — an options version loses far more to theta and STT. The metrics then configure live trading: max drawdown sets position size (plan for 1.5–2× the backtested figure), expectancy sets realistic return, and the outcome distribution lets you pre-decide responses to losing streaks. The one-liner: *"A backtest doesn't tell you how much you'll make — it tells you whether you have an edge and how much pain you must survive to collect it, and its honesty depends entirely on out-of-sample validation and realistic costs."*
