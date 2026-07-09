# Build-Tonight Guide — 3 Technical-Research Projects

Goal: make each resume project REAL enough that you can confidently answer "walk me through this"
in tomorrow's interview. Each is a few hours. Use free data (`yfinance`). Save your code + a few
output screenshots/charts so you have something to show and talk about.

Tickers to use (NSE on Yahoo): Nifty 50 = `^NSEI`, Bank Nifty = `^NSEBANK`, e.g. Reliance = `RELIANCE.NS`.

Setup once:
```
pip install yfinance pandas numpy matplotlib mplfinance pandas_ta
```

---

## 1. Nifty & Bank Nifty Technical Strategy Backtester (Python)

What it does: tests a simple rules-based strategy and compares it to just buying and holding.

Steps:
1. Download ~3 years of daily data: `df = yfinance.download("^NSEI", period="3y")`.
2. Compute indicators with `pandas_ta`:
   - Fast & slow moving averages (e.g. `df.ta.sma(20)`, `df.ta.sma(50)`)
   - `df.ta.rsi(14)`, `df.ta.macd()`
3. Define entry/exit rules, e.g. **go long when 20-SMA crosses above 50-SMA AND RSI > 50**; exit on the
   opposite crossover or RSI < 50.
4. Build a `position` column (1 when in trade, 0 when out). Strategy daily return = `position.shift(1) * df['Close'].pct_change()`.
5. Metrics to print:
   - **Win-rate** = % of trades that closed positive
   - **Cumulative return** = `(1 + strat_ret).cumprod()` final value
   - **Max drawdown** = biggest peak-to-trough drop of the equity curve
   - **Sharpe** = `mean(strat_ret)/std(strat_ret) * sqrt(252)`
6. Plot strategy equity curve vs buy-and-hold. Save the chart.

Talking points: "I'm not claiming it beats the market — the point was to learn how to translate
indicator signals into rules and measure them honestly with win-rate, drawdown, and Sharpe versus a
benchmark." Be ready to say what worked and what didn't (e.g. crossover strategies lag in choppy markets).

---

## 2. Daily Technical Research Report: Nifty & Bank Nifty (Excel / TradingView)

What it does: a 1-page research note like a real analyst publishes each morning.

Steps:
1. Open Nifty 50 and Bank Nifty daily charts on **TradingView** (free account).
2. Mark up each chart: **support & resistance** levels, trendline, recent **candlestick pattern**
   (e.g. doji/engulfing), **Fibonacci retracement** of the last swing, **Bollinger Bands**, and RSI/MACD.
3. Screenshot the marked-up charts.
4. In Excel/Word, write a short note per index:
   - Trend (up/down/sideways) and key levels (support, resistance)
   - What the indicators say (RSI overbought/oversold, MACD cross, price vs Bollinger Bands)
   - A clear **view: Buy / Sell / Hold** with **entry, target, and stop-loss**
5. Export as PDF. That PDF *is* the deliverable.

Talking points: this is closest to the actual job. Be ready to defend ONE call end-to-end: "I'd go
long Bank Nifty above X because it held support at Y, RSI turned up from oversold, with target Z and
stop below Y." Know WHY each level matters.

---

## 3. Candlestick Pattern Detector (Python)

What it does: scans price data and flags reversal candles.

Steps:
1. Download data: `df = yfinance.download("RELIANCE.NS", period="1y")`.
2. Detect patterns from OHLC with simple logic (don't need TA-Lib):
   - **Doji**: `abs(Open-Close) <= 0.1 * (High-Low)`
   - **Bullish engulfing**: today's green body fully covers yesterday's red body
   - **Hammer**: small body near the top, long lower wick (lower wick >= 2x body)
3. Add a column flagging the pattern on each day.
4. Plot the candles with `mplfinance` and mark detected patterns (arrows/markers). Save the chart.

Talking points: "I coded the pattern rules myself from the OHLC definitions, so I understand exactly
what a doji or engulfing means rather than just calling a library." Know what each pattern signals
(reversal vs indecision).

---

## General interview prep (5 min)
- Re-read your own resume top to bottom; every keyword (Bollinger Bands, Fibonacci, MACD, GARCH,
  option greeks) is fair game — be able to define each in one sentence.
- For the F&O desk experience, be ready to explain implied volatility, open interest, and one option
  strategy (e.g. a straddle) simply.
- NISM Series-XV: know what a Research Analyst regulation covers at a high level (research reports,
  disclosures, no front-running).
