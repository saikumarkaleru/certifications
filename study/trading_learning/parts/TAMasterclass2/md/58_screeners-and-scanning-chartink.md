# Screeners & Scanning (Chartink/TradingView)

## What it is & why it works

A screener is a filter that runs your technical rules across the entire market at once and returns only the handful of stocks that qualify. Instead of eyeballing 500 charts every evening, you encode "close crossed above the 50-day EMA today, with volume above the 20-day average, and RSI between 50 and 65" once — and the machine hands you the ten names that match. Scanning is how a solo trader with a laptop competes against desks with analysts: you industrialise the search so your limited attention is spent only on setups that already passed your objective criteria.

Why it works: edge in trading is a repeatable, defined pattern with a positive expectancy. If your edge is defined, it can be coded. If it can be coded, it can be scanned. The screener does not create the edge — your rules do — but it removes the two biggest killers of discretionary traders: (1) *selection bias*, where you only notice the charts that confirm your mood, and (2) *missed opportunity*, where the best setup of the day was on a stock you never opened. A disciplined scan every evening on the NSE universe is the closest thing to a systematic process that a discretionary trader can run.

In India the two workhorse tools are **Chartink** (free, India-focused, NSE/BSE universe, purpose-built scanning language, superb for end-of-day and intraday scans) and **TradingView** (global, powerful Pine-based screener and the built-in stock screener, better charts, some features paid). Chartink is where most Indian retail scanning happens because it is free, fast, and speaks NSE natively. This chapter teaches you to build, refine and trade from scans on both.

## Mechanics — how a scan is structured

Every good scan has four logical blocks, whether you write it in Chartink's clause language or TradingView's screener:

1. **Universe / liquidity filter.** Which stocks are even eligible. You almost always want to exclude illiquid names to avoid slippage and manipulation. Typical filters: price > ₹50, average daily volume > 200,000 shares, or restrict to an index constituent list (Nifty 500, F&O stocks). In Chartink you approximate this with `Latest Volume > 100000` and `Latest Close > 50`; on TradingView you can filter by index membership directly.

2. **Trend / regime filter.** The backdrop. Are you buying strength or fading weakness? Example: `Latest Close > Latest SMA(200)` restricts to stocks in a long-term uptrend — you never fight the primary trend. Adding `Latest EMA(20) > Latest EMA(50)` ensures the short and medium trends agree.

3. **Trigger / signal.** The event that fires today. This is the heart of the scan: a crossover, a breakout of an N-day high, a candle pattern, an indicator threshold crossing. Example: `Latest Close crossed above Latest SMA(50)`.

4. **Confirmation / filter.** Quality control to cut false positives. Almost always volume (`Latest Volume > 1.5 * SMA(Volume,20)`) and often a momentum band (`Latest RSI(14) > 50 and Latest RSI(14) < 70`) so you avoid already-overbought entries.

A scan missing any of these blocks tends to be noisy. A price-crossed-EMA scan with no liquidity filter returns penny stocks; with no volume filter it returns limp, unconvincing crossings; with no trend filter it returns counter-trend traps.

## Chartink — the syntax you need

Chartink scans are written as clauses joined by `and`/`or`, referencing `Latest`, `1 day ago`, `Weekly`, `Monthly` timeframes and functions like `SMA`, `EMA`, `RSI`, `MACD`, `Volume`, and `crossed above / crossed below`. A few production-ready scans:

**Momentum breakout (EOD).**
```
( {cash} ( latest close > latest sma( close,200 ) and
latest ema( close,20 ) > latest ema( close,50 ) and
latest close = latest max( 20, latest high ) and
latest volume > 1.5 * latest sma( volume,20 ) and
latest close > 50 and latest volume > 200000 ) )
```
This returns liquid, uptrending stocks making a fresh 20-day closing high on 1.5× volume — a clean momentum-breakout list.

**50-EMA reclaim / pullback buy.**
```
( {cash} ( latest close crossed above latest ema( close,50 ) and
weekly close > weekly ema( close,50 ) and
latest rsi( 14 ) > 45 and latest rsi( 14 ) < 65 and
latest volume > latest sma( volume,20 ) ) )
```
Catches stocks that dipped to and reclaimed the 50-EMA while the weekly trend stays up — a pullback-continuation edge.

**Bullish MACD crossover with trend.**
```
( {cash} ( latest macd line( 26,12,9 ) crossed above latest macd signal( 26,12,9 )
and latest close > latest sma( 200 ) and latest volume > 200000 ) )
```

**Intraday 15-minute ORB-style (open-high scan).** Chartink supports intraday timeframes; a scan for stocks trading above the first 15-minute high with rising volume approximates an opening-range-breakout watchlist.

Chartink lets you **backtest** many scans (the "Backtest" tab) and, crucially, **run scans on a schedule during market hours** with alerts — the foundation of an intraday process.

## TradingView — screener and Pine

TradingView offers two routes. The **built-in Stock Screener** (Products → Screener) has India-specific filters: exchange NSE, index membership, price, volume, RSI, moving-average relationships, performance, and fundamental columns. It is point-and-click and excellent for a quick liquid-uptrend-with-momentum list.

For anything custom, TradingView's **Pine screener** lets you write a Pine script that computes a condition and screen the whole watchlist for it — this is where you replicate a Chartink-style crossover scan with full control, and you can reuse the exact indicator logic your charts already display. The advantage over Chartink is charting fidelity and the ability to attach the scan to the same script you trade from; the disadvantage is that deeper features sit behind paid tiers and the India universe is less front-and-centre.

A pragmatic Indian workflow: **scan on Chartink (free, fast, NSE-native), then chart the survivors on TradingView** for the final discretionary read before committing.

## Worked India example (levels & ₹)

Suppose it is a Thursday evening. You run the momentum-breakout EOD scan on Chartink and it returns eight names. You discard the illiquid two and the two that are up 60% in a month (extended). Of the remaining four, one is a mid-cap capital-goods stock — call the reconstruction a name trading at ₹1,240, closing at a fresh 20-day high on volume of 4.1 lakh shares versus a 20-day average of 2.3 lakh (1.8×). Its 20-EMA (₹1,190) is above the 50-EMA (₹1,150), price is well above the 200-SMA (₹980), and daily RSI is 62 — strong but not yet overbought.

You pull it up on TradingView. The breakout is above a three-week consolidation ceiling near ₹1,235, the volume node is convincing, and the sector (capital goods / defence) is in favour. This is a textbook survivor: the scan found it objectively; the chart confirms it discretionarily.

**The trade plan:** buy on a close above ₹1,240 (already qualified) or on a next-day hold above ₹1,235 to avoid a fakeout. Stop below the breakout base and 20-EMA at ₹1,185 (risk ≈ ₹55, ~4.4%). Target the measured move of the consolidation height (~₹90) projected up, to ₹1,330, and trail the rest with the 20-EMA. Position size so that the ₹55 risk is 1% of capital: on ₹10 lakh, risk ₹10,000, so ~180 shares (₹2.23 lakh position). The scan did the discovery; your risk rules did the sizing.

## How to trade it (workflow, not just entry)

The screener is step one of a funnel, not a signal to click buy. A disciplined process:

1. **Run the EOD scan(s)** after market close, on your fixed set of two or three saved scans (momentum breakout, pullback-reclaim, and a reversal/oversold scan for range regimes).
2. **Cull to a shortlist** by liquidity, extension, sector strength and news. Twenty raw hits become four to six candidates.
3. **Chart each survivor** for structure, level quality, and confluence the scan cannot see (round numbers, prior swing highs, gaps).
4. **Pre-plan entry, stop, target and size** in writing before the open. Set alerts at the trigger levels.
5. **Execute only if the trigger fires with agreeing tape** the next session. Many survivors will not trigger — that is correct; you want confirmation, not prediction.
6. **Log every scan-sourced trade** so you can later measure which scan produces which win rate and expectancy.

## Confluence (including OI)

For F&O stocks, cross the scan against derivatives data. A breakout survivor is far stronger when the option chain shows call writers being pushed out (call OI unwinding at the breakout strike) and put OI building below — writers betting the level holds. A momentum-breakout name that is *also* seeing long build-up in futures (price up + OI up) is a high-conviction continuation; one where the breakout comes on short-covering (price up + OI down) may be shorter-lived. Add "F&O stock, futures OI rising" as a mental filter on your shortlist. Rising sector index (e.g., Nifty Auto, Nifty PSU Bank) behind the individual name is another free confluence — screen the sector indices too and prefer stocks whose sector is itself breaking out. India VIX regime matters: momentum-breakout scans work best in low-to-moderate VIX trending tapes; in a VIX spike, mean-reversion/oversold scans earn their keep instead.

## Pitfalls

**Curve-fitting the scan.** It is tempting to keep adding clauses until the scan returns only past winners. That over-optimised scan will return almost nothing useful in live conditions. Keep scans simple — four or five clauses. Robust beats clever.

**No regime awareness.** A momentum-breakout scan run every day, including in a choppy, mean-reverting market, will feed you a stream of failed breakouts. Match the scan to the regime: breakout scans in trends, pullback and oversold-bounce scans in ranges. Read the index regime first, then choose the scan.

**Ignoring liquidity.** The single most common retail error is trading a beautiful scan hit that turns out to trade 15,000 shares a day — you cannot enter or exit without moving it, and stops slip badly. Hard-filter volume and price, always.

**Treating a hit as a buy signal.** A scan hit means "this stock met objective criteria today," not "buy now." The confirmation-and-plan steps exist precisely to stop reflexive entries. Survivors that never trigger the next day saved you money.

**Survivorship and repainting.** Chartink's "Latest" refers to the current (possibly incomplete) candle intraday — an intraday scan can flip before the candle closes. For EOD reliability, scan after close. Backtest results on any tool are optimistic; treat them as relative comparisons, not live-expectancy promises.

**Over-scanning.** Running fifteen different scans produces forty hits and decision paralysis. Two or three well-chosen, regime-matched scans beat a wall of them. Fewer, better, logged.

## Building your personal scan library

Maintain a small, versioned set of saved scans, each with a one-line note on the regime it suits and the historical win-rate you have observed from your own log:
- **Momentum breakout** (trending market) — fresh 20-day high, 1.5× volume, EMA stack up.
- **Pullback reclaim** (trending market, buy the dip) — 50-EMA reclaim, weekly uptrend, RSI 45–65.
- **Oversold bounce** (range/oversold market) — RSI < 30 turning up, at prior support, above 200-SMA.
- **Volume shocker** (any) — volume > 3× average, for early detection of institutional interest.
- **Breakdown / short** (downtrend) — fresh 20-day low, below 200-SMA, rising volume, for the bearish side.

Review the library quarterly against your trade log: kill scans whose survivors underperform, keep the ones that pay. The scan library becomes a living record of your edge, expressed in code.

## Interview-ready summary

Screening industrialises your technical edge: you encode your rules once and the tool applies them to the whole NSE universe, eliminating selection bias and missed setups. Every robust scan has four blocks — liquidity/universe filter (price and volume, or index membership), trend/regime filter (e.g., price above 200-SMA, EMA stack up), the trigger (crossover, N-day breakout, candle), and a confirmation filter (volume above average, RSI band). Chartink is the free, NSE-native workhorse with a clause language (`Latest close crossed above Latest ema(close,50)…`), backtesting, and intraday scheduled alerts; TradingView offers a point-and-click screener plus Pine-based custom scans and superior charts, some behind paid tiers. The pragmatic Indian workflow is scan on Chartink, chart survivors on TradingView. Critically, a scan hit is *discovery, not a buy signal*: it feeds a funnel — cull by liquidity/extension/sector, chart for structure and confluence (option-chain OI, sector-index strength, VIX regime the scan cannot see), pre-plan entry/stop/target/size in writing, and execute only when the trigger fires with agreeing tape the next session. Match the scan to the regime (breakout scans in trends, oversold/pullback scans in ranges), keep scans simple to avoid curve-fitting, always hard-filter liquidity, and log every scan-sourced trade so you can measure which scan actually pays. The screener never creates the edge — your rules do — but it is how a solo trader runs a near-systematic discovery process against the whole market every single evening.
