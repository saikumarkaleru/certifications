# Building a TA Trading System (Confluence & Rules)

## What it is & why it works

A trading *system* is the difference between someone who "knows technical analysis" and someone who actually makes money from it. Knowing what a hammer candle looks like, being able to spot an RSI divergence, or recognising a Bank Nifty double-top — these are ingredients, not a meal. A system is the written, repeatable recipe that turns those ingredients into decisions: *what* you trade, *when* you enter, *how much* you risk, *where* you exit, and *what* you do when the trade goes against you. It removes the two things that quietly destroy retail traders — discretion under stress and inconsistency across trades.

Why does codifying rules work when the market is supposedly random? Because edge in technical trading is statistical, not deterministic. No single setup wins every time; a good breakout system on Nifty might win only 45% of the time. But if the winners are twice the size of the losers, you make money over 200 trades. That mathematics only holds if you take *every* valid signal the same way. The moment you start skipping trades that "feel wrong", cutting winners early out of fear, or holding losers hoping for a bounce, you break the sample and the edge evaporates. A system enforces the sample.

There is also a behavioural reason rooted in how Indian markets actually move. The NSE is dominated by institutional flows, algo execution, and expiry-day option dynamics. A retail discretionary trader watching a 5-minute chart is reacting emotionally to noise that professionals have already priced. A rules-based system with clear confluence requirements forces you to wait for the small number of moments each week when multiple independent signals align — trend, level, momentum, and often option-chain positioning — which is precisely when the probability tilts in your favour. Confluence is the core idea: any one indicator is a coin-flip with a slight bias; three *independent* signals agreeing is a genuinely different bet.

A system is honest about its own limits. It tells you your expected win rate, your worst realistic drawdown, and the market regimes where it will bleed. That honesty is what lets you keep trading through a losing streak instead of abandoning a good method at exactly the wrong time.

## The mechanics — the seven components of a complete system

A complete discretionary-systematic TA system in Indian markets has seven written components. If any one is missing, you don't have a system — you have a hobby.

**1. Universe & instrument.** Define exactly what you trade. "Nifty 50 and Bank Nifty index futures/options, plus the F&O-200 large-cap stocks with average daily turnover above Rs 300 crore." Avoid illiquid mid-caps where slippage eats your edge. Specify the instrument: cash, futures, or options — a breakout system executed via ATM options behaves very differently from the same signal in futures because of theta and IV.

**2. Timeframe & regime filter.** State your primary timeframe (say, 15-minute for intraday, daily for swing) and one higher timeframe for context (hourly, or weekly). Add a regime filter that classifies the market as trending or range-bound, because most systems only work in one regime. A common, robust filter is ADX: ADX > 20 and rising = trending (trade breakouts/pullbacks); ADX < 18 = range (fade extremes or stand aside). Another is price relative to the 50-EMA slope.

**3. Setup (the pattern).** The specific configuration that must exist before you even look for an entry. Example: "Price above rising 20 and 50 EMA, pulls back to the 20 EMA, and forms a bullish reversal candle." The setup is a *state*, not a trigger.

**4. Entry trigger.** The precise, objective event that puts you in. "Buy on a break of the pullback candle's high by 2 points" or "enter on 15-min close above resistance." It must be so specific that two traders reading it would enter at the same price.

**5. Stop-loss.** Placed at the price that proves the setup wrong — below the pullback swing low, below the pattern, or an ATR-based buffer beyond structure. Never a round-number "I can afford to lose Rs 2,000" stop; the *chart* defines where you're wrong, and position size adjusts to the risk (covered in the ATR chapter).

**6. Target & exit management.** Measured move, fixed R-multiple, or trailing stop. Define whether you scale out, and the rule for trailing (e.g., trail below each new higher-low, or below the 20-EMA).

**7. Risk & sizing rules.** Fixed fractional risk per trade (typically 0.5–1% of capital), max open risk, max trades per day, and a daily/weekly loss limit that stops you trading.

Here is a compact table of a sample intraday Nifty/Bank Nifty trend-pullback system:

| Component | Rule |
|---|---|
| Universe | Nifty & Bank Nifty futures; ATM/ITM options for execution |
| Timeframe | 15-min entry, 1-hour trend |
| Regime filter | 1-hr ADX > 20 and price above rising 50-EMA (longs only) |
| Setup | Pullback to 20-EMA on 15-min, holds above it |
| Entry | Break of prior 15-min candle high after a bullish close at EMA |
| Stop | Below the pullback swing low (structure) |
| Target | 1.5R partial, trail remainder below 20-EMA |
| Risk | 0.75% of capital per trade, 2 losers = stop for the day |

The discipline is that these seven live in a written document, not your head. You should be able to hand the page to another trader and have them take the same trades.

## Reading it — a worked Bank Nifty example, phase by phase

Let's walk a single real-style trade through the system so the abstract components become concrete. Assume capital of Rs 10,00,000 and a 0.75% risk budget = Rs 7,500 per trade. Date: a normal expiry-week Wednesday. Bank Nifty is trading around 48,000.

**Phase 1 — Regime check (context).** On the 1-hour chart, Bank Nifty has been grinding up for three sessions. The 50-EMA sits at 47,650 and is sloping up; price is comfortably above it. ADX on the hourly is 24 and rising. The regime filter says: *trending, longs only.* This single gate has already eliminated the temptation to short into strength — the number-one killer of intraday accounts.

**Phase 2 — Setup formation.** Through the morning, Bank Nifty rallies to 48,180, then drifts back during the 11:00–12:00 lull. On the 15-minute chart it pulls into the rising 20-EMA at 47,940. Two candles print small bodies right at the EMA with lower wicks — buyers are defending the average. The *setup* now exists: uptrend + pullback to 20-EMA + holding. I am now on alert, but I have not entered.

**Phase 3 — Entry trigger.** The 12:15 candle closes bullish at 47,995, its high at 48,020. My rule: buy on a break of that candle's high by a small buffer. At 12:31, price ticks to 48,024. Filled at 48,025 (futures reference). This is objective — no "I think it looks strong."

**Phase 4 — Stop placement.** The pullback swing low was 47,928. I place the stop at 47,905, just below structure, giving 120 points of risk. In rupees per lot (Bank Nifty lot = 15), that's 15 × 120 = Rs 1,800 risk per lot. My budget is Rs 7,500, so I can take 7,500 ÷ 1,800 ≈ 4 lots. I take 4.

**Phase 5 — Target & management.** My first target is 1.5R = 180 points, at 48,205. Around 13:20 Bank Nifty prints 48,210; I sell 2 lots there, banking roughly 15 × 180 × 2 = Rs 5,400 and moving my stop on the remaining 2 lots to breakeven (48,025). Now the trade is risk-free. I trail the last 2 lots below the rising 15-min 20-EMA.

**Phase 6 — Exit.** The index runs to 48,380 into the afternoon, then a 15-min candle closes back below the 20-EMA at 48,300. My trailing rule exits the final 2 lots there: 15 × 275 × 2 = Rs 8,250. Total on the trade: roughly Rs 13,650 against a Rs 7,500 risk — a 1.8R win. Every decision was rule-driven; my emotions never touched the trade.

Notice what the system did: it kept me out of shorts, made me wait for the pullback rather than chasing the high at 48,180, sized me correctly off the *chart-defined* stop, and let a winner run without letting greed hold it into a reversal.

## Trading it — entry, stop, target, and multiple scenarios

The single worked trade above is the "textbook win." A real system must define behaviour across *all* outcomes, because most trades are not clean. Consider four scenarios from the same setup.

**Scenario A — Clean winner (above).** Trigger hit, ran to target, trailed out at +1.8R. Nothing to add.

**Scenario B — Immediate stop-out.** You enter at 48,025; instead of bouncing, a block of selling hits and price slices through 47,905 within two candles. You lose 1R (Rs 7,500 minus costs). The correct behaviour is *nothing* — no averaging down, no re-entering out of revenge. The stop is data: this particular pullback failed. If the trend is intact and a *fresh* valid setup forms later, you may take it. One loss is a cost of doing business; the system expects roughly half of them.

**Scenario C — Chop / breakeven grind.** You enter, price stalls, oscillates around entry for an hour without hitting target or stop, and your daily time-stop (say 15:00 for intraday) arrives. Rule: exit at market near the close, take the small win or loss, don't carry an intraday-designed trade overnight. Many beginners have no time-stop and end up "investing" in a failed day trade.

**Scenario D — Gap against an overnight swing version.** If you run the same logic as a *swing* system on the daily chart, a stock can gap below your stop overnight (e.g., a bank reports weak asset quality). You will lose more than 1R — say 1.8R. This is *slippage/gap risk*, and it's why swing sizing is often smaller and why single-stock swing systems benefit from an event filter (avoid holding through results). The system must acknowledge that stops are not guaranteed fills.

Across these scenarios, the *management rules* matter more than the entry. A useful default management ladder:

| Trade progress | Action |
|---|---|
| +1R reached | Sell one-third to one-half, stop to breakeven |
| +2R reached | Trail behind swing structure or key EMA |
| Stop hit | Exit fully, no re-entry without a new setup |
| Time-stop reached | Exit at market (intraday) |
| Adverse gap | Exit at open, accept the slippage |

The point is that entries are roughly 20% of results; sizing and management are the other 80%. A mediocre entry with disciplined 1.5–2R management and correct sizing beats a brilliant entry managed emotionally.

## Confluence — stacking independent signals (and option-chain/OI)

Confluence is the engine of a high-probability system, but only if the signals are *independent*. Stacking RSI, Stochastic, and MACD is fake confluence — they're all momentum oscillators derived from price, so they mostly say the same thing. Real confluence combines signals from *different information sources*:

1. **Trend / structure** — higher-timeframe trend and market structure (higher highs/lows).
2. **Level** — a horizontal support/resistance, prior day high/low, VWAP, or a Fibonacci retracement.
3. **Momentum / trigger** — a candle pattern or oscillator confirming the turn.
4. **Positioning / flow** — option-chain OI, PCR, and where big option writers are sitting.

The fourth is India's edge, because the NSE options market is enormous and its open-interest data is public. Suppose our Bank Nifty long setup at 47,940 also coincides with the *max Put OI strike* at 47,900 — meaning option writers have sold huge quantities of the 47,900 put and are financially motivated to defend that floor. That is a genuinely independent reason to believe the pullback holds. Now you have four aligned reasons: uptrend (structure), 20-EMA + prior support (level), bullish reversal candle (momentum), and heavy put writing below (positioning). That is an A+ trade, and the system can justify sizing at the top of the range.

Conversely, if your bullish setup runs *into* the max Call OI / max-pain strike just overhead — say resistance at 48,100 where call writers dominate — the system should reduce the target or the size, because you're buying straight into a wall of sellers. Option-chain data doesn't replace price analysis; it tells you where the *dealers* will lean, which is where price often stalls or reverses.

A practical confluence-scoring rule: require a minimum of **three of four** buckets to align before taking a trade, and reserve full size for **four of four**. This single rule filters out most low-quality signals and is the reason a good system trades *less* than a beginner expects. On Nifty and Bank Nifty you might get only two or three A-grade setups a week — and that's fine, because size and management do the heavy lifting.

VWAP deserves special mention as a confluence tool for intraday India: institutions benchmark to VWAP, so a pullback that holds *above* rising VWAP with price also above the 20-EMA is a strong long context; a bounce that fails *at* VWAP from below is a strong short context. Adding VWAP to the level bucket materially sharpens intraday systems on liquid indices.

## Pitfalls & false signals — where systems break and how pros filter

**Over-optimisation and curve-fitting.** The most seductive failure. You tweak the EMA from 20 to 21, the ADX from 20 to 22, add a filter, and suddenly your backtest looks perfect. You've fitted the system to *past noise*; it will fall apart live. Pros keep parameters few and round, prefer rules that make *structural sense* (a 20-EMA works because everyone watches it), and test on out-of-sample data.

**Regime blindness.** A trend-pullback system that made money all of 2023–24 will bleed in a choppy, range-bound market where every pullback is actually a reversal. The regime filter (ADX, EMA slope) exists precisely to keep you flat when your edge is absent. When a good system starts losing, the first question is not "is the system broken?" but "has the regime changed?"

**Signal-shopping and rule-drift.** The discretionary trap: you take the trades that "look nice" and skip the ones that don't, then wonder why your live results don't match the backtest. If the setup is valid, you take it — full stop. Keeping a trade journal that scores each trade against the written rules exposes rule-drift ruthlessly.

**Fake confluence.** As noted, stacking three momentum oscillators feels like confirmation but is really one signal counted thrice. Pros audit their indicators for independence and deliberately combine orthogonal sources — price structure, level, momentum, and flow.

**Expiry-day and event distortion.** On Nifty/Bank Nifty expiry, price can be pinned to max-pain by option dynamics, breaking normal breakout behaviour. Around RBI policy, Union Budget, US Fed, and single-stock results, volatility gaps invalidate stop assumptions. Mature systems either stand aside on these days or explicitly reduce size — a written event filter.

**Ignoring costs.** Brokerage, STT (heavy on options), exchange fees, and slippage can turn a marginally-positive backtest into a live loser, especially for high-frequency intraday systems. Always model realistic round-trip costs before trusting an edge.

**Confusing a losing streak with a broken system.** Even a 55%-win, 1.5R system will have runs of 5–6 losers. Traders who quit during the drawdown lock in the losses and miss the recovery. The defence is knowing your system's expected drawdown *in advance* (from backtesting) so a normal streak doesn't feel like an emergency.

## Interview-ready summary

A TA trading system is a written, repeatable rulebook with seven parts: universe, timeframe and regime filter, setup, entry trigger, stop, target/management, and risk/sizing. It works because technical edge is statistical — you only profit if you take every valid signal identically, and a system enforces that consistency while removing emotion. The core principle is *confluence of independent signals*: trend/structure, level, momentum, and — uniquely in India — option-chain positioning (max Put/Call OI, PCR, max-pain), requiring at least three of four to align before trading and reserving full size for four of four. Stops are defined by the chart (where the setup is wrong), and position size flexes to keep risk at a fixed 0.5–1% per trade. Management — scaling at 1R, breakeven stops, trailing — drives most of the results, not the entry. The system must be honest about regime dependence, expected drawdown, and costs (STT, slippage), and it must include a regime filter (e.g., ADX) so you stand aside when your edge is absent. The one-line version: *"A system converts pattern-recognition into a positive-expectancy business by pairing high-confluence, chart-defined entries with fixed-fraction risk and mechanical management, taken the same way every single time."*
