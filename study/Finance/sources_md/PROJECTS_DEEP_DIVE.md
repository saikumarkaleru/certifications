# Projects Deep-Dive & Interview Defense
### How each project works, what every number means, and how to answer when grilled
*Prepared for Saikumar Kaleru. If an interviewer says "walk me through this project," everything you need is here. Read it until you can explain each project without notes.*

*Project numbers below match your project folder: `1_nifty_banknifty_backtester`, `2_daily_technical_research_report`, `3_technical_coverage_watchlist`.*

---

## The portfolio narrative (say this if asked "tell me about your projects")
> "I built three projects that mirror the technical-research workflow end to end: a **backtester** that
> validates whether technical strategies actually work, a **research-report generator** that produces the
> daily/weekly/monthly notes an analyst publishes, and a **coverage watchlist** that screens a sector
> universe for setups. The reports and watchlist are the analyst's daily output; the backtester is where
> my coding background adds an edge — I can test an idea on data instead of trusting it blindly."

**Golden rule for all three:** they use **free market data (yfinance)**, and I **coded the indicators
by hand** (moving averages, RSI, MACD, ATR, Bollinger, candlestick rules) — so I understand the math,
I'm not just calling a black box.

---

# PROJECT 1 — Multi-Strategy Technical Backtester
*Tool: Python. This is my differentiator — coding lets me test an idea on data instead of trusting it blindly.*

### The one-line pitch (memorise this)
> "I built a backtesting engine in Python that tests eight technical strategies on Nifty 50 and Bank Nifty
> over ~6 years of daily data and compares each one against buy-and-hold on risk-adjusted metrics like
> CAGR, Sharpe and max drawdown — so a strategy is validated with evidence before anyone trades it."

### Why this matters for a TRA
A research analyst recommends trade ideas. **Backtesting is how you prove an idea has an edge instead of
guessing** — it's the difference between "RSI looks good" and "RSI mean-reversion returned X% with a
Sharpe of Y over six years." It shows I can quantify whether a strategy actually works.

### The eight strategies (be able to describe each)
All are **long/flat** — you either own the index (position = 1) or sit in cash (position = 0). No
short-selling, no leverage.

| # | Strategy | Type | Buy signal | Exit signal |
|---|----------|------|------------|-------------|
| 1 | **MA Crossover + RSI** | trend | 20-MA > 50-MA **and** RSI > 50 | when that's no longer true |
| 2 | **RSI Mean-Reversion** | mean-revert | RSI < 30 (oversold) | RSI > 55 (bounce done) |
| 3 | **MACD Trend** | trend | MACD line > signal line | MACD line < signal line |
| 4 | **Bollinger Breakout** | breakout | close breaks above upper band | close falls below the 20-MA |
| 5 | **Golden Cross 50/200** | trend | 50-MA > 200-MA (golden cross) | 50-MA < 200-MA (death cross) |
| 6 | **Bollinger Mean-Reversion** | mean-revert | close dips below the lower band | close back above the 20-MA |
| 7 | **Stochastic Reversal** | mean-revert | %K < 20 and crossing up through %D | %K > 80 |
| 8 | **Donchian Breakout** | breakout | close > prior 20-day high (Turtle) | close < prior 10-day low |

Simple on/off rules (MA-cross, MACD, golden cross) are one-line conditions. Mean-reversion and breakout
strategies are **stateful** — a helper "remembers" you're in the trade and keeps you in until the exit
fires. *(Why? RSI < 30 triggers the buy, but you stay in while RSI climbs to 55 — a plain condition would
drop you out the very next day.)*

**The result worth quoting:** on Nifty, **Bollinger Mean-Reversion matched buy-and-hold's Sharpe (1.16)
with half the drawdown** (−10.4% vs −17.2%) and an 88% win-rate, while invested only ~16% of the time —
a clean example of a *risk-adjusted* edge even when raw return trails a bull market.

### How it works — the 5-step pipeline (data → indicators → positions → performance → report)
1. **Get the data.** Download 6 years of daily Open/High/Low/Close for Nifty (`^NSEI`) and Bank Nifty
   (`^NSEBANK`) via the free **yfinance** library — about 1,500 trading days each.
2. **Compute indicators by hand (pandas).** I calculate them myself, not via a black-box library, so I
   can explain the formula: **SMA20/SMA50** (`.rolling().mean()`), **RSI(14)** =
   `100 − 100 / (1 + avgGain/avgLoss)`, **MACD** = 12-EMA − 26-EMA with a 9-EMA signal line, and
   **Bollinger Bands** = SMA20 ± 2 standard deviations.
3. **Turn indicators into a position.** Each strategy outputs the 0/1 position series above.
4. **The single most important line — no look-ahead bias.** The position is **shifted by one day**:
   today's signal is acted on *tomorrow*. You can't trade on a close you haven't seen yet — shifting the
   position by one bar removes look-ahead bias and makes the backtest realistic. **If they ask one hard
   question about this project, it's this.**
5. **Measure & report.** Daily strategy return = (yesterday's position) × today's market return,
   compounded into an **equity curve**; individual **trades** (entry→exit) are extracted for win-rate and
   profit factor; the full metric set is computed; and it renders an equity-curve chart plus a landscape
   **PDF** with a metrics table per index (the buy-and-hold row highlighted as the benchmark).

### Every metric explained (they WILL ask)
| Metric | Plain meaning |
|--------|---------------|
| **Total Return %** | How much ₹1 grew over the whole 6 years |
| **CAGR %** | That return as a smooth *annual* growth rate |
| **Sharpe** | Return per unit of **total** volatility; higher is better, >1 is good |
| **Sortino** | Like Sharpe but counts only **downside** volatility (upside swings aren't "risk") |
| **Max DD %** | Worst peak-to-trough fall — the most pain you'd have sat through |
| **Win %** | Share of trades that were profitable |
| **Profit Factor** | Gross profit ÷ gross loss; above 1 means winners outweigh losers |
| **Exposure %** | Fraction of the time actually invested (the rest in cash — no return, no risk) |

### The honest, impressive talking point
> "The active strategies **underperformed buy-and-hold** over this period — because it was a strong bull
> market and being in cash part of the time cost returns. But some had a **better Sharpe or a smaller max
> drawdown**, meaning they took less risk to get there. The real lesson was learning to judge a strategy
> honestly with Sharpe, Sortino and drawdown — risk-*adjusted* returns and the market regime — instead of
> chasing a back-fitted 'winner'."

*(Admitting the strategies lost to buy-and-hold shows maturity and that you didn't fake results — this
impresses far more than a suspiciously perfect backtest.)*

### Likely questions & answers
- **"How did you avoid look-ahead bias?"** → "I act on the *previous* day's signal — I shift the position
  by one bar, so I never trade on information I wouldn't have had in time."
- **"Did you calculate RSI/MACD yourself?"** → "Yes, by hand in pandas, so I understand the formulas
  rather than calling a black box."
- **"What's overfitting / curve-fitting?"** → "Tuning a strategy so perfectly to past data that it fails
  live. I used fixed, standard parameters instead of optimising them to flatter the result."
- **"Why long/flat, no shorting?"** → "Keeps it realistic for cash-index trading — you're either invested
  or in cash."
- **"Why Sortino as well as Sharpe?"** → "Sharpe penalises *all* volatility, including good upside moves;
  Sortino only penalises downside, which is what actually hurts."
- **"Why did buy-and-hold win?"** → "Strong uptrend + the active strategies sit in cash part of the time
  (see the Exposure column). In a sideways or bear market their lower drawdown would matter more."
- **"What would you add?"** → "Transaction costs and slippage, out-of-sample / walk-forward testing, and
  position sizing — right now it's all-in / all-out."

---

# PROJECT 2 — Daily / Weekly / Monthly Technical Research Reports
*Tools: Excel + Python. This is the actual job.*

### What it does (one line)
Produces a research note for **Nifty 50, Bank Nifty, Gold and Crude Oil** on three timeframes, each
giving a **Buy/Sell/Hold** call with entry, target and stop-loss, backed by indicators and a chart.

### How it works — step by step
1. **Pull data** for each asset (yfinance). For weekly/monthly, the daily data is **resampled** into
   weekly (Friday close) or monthly (month-end) candles using Open=first, High=max, Low=min, Close=last.
2. **Compute indicators** on the last bar: 20- and 50-period moving averages, RSI(14), MACD(12/26/9),
   Bollinger Bands (20, ±2σ), and ATR(14).
3. **Find levels:** support and resistance from the recent swing low/high, and Fibonacci retracement
   levels (23.6 / 38.2 / 50 / 61.8%) of that swing.
4. **Score the view:** a points system — +1 if price > 20-MA, +1 if 20-MA > 50-MA, +1 if MACD > signal,
   ±1 for RSI extremes, ±1 for Bollinger position. Score ≥ +2 = BUY, ≤ −2 = SELL, else HOLD.
5. **Guardrail:** if the model says SELL but RSI < 25 (deeply oversold), it steps aside to HOLD — you
   don't short a tape that's already collapsed. Same for chasing an overbought BUY (RSI > 80).
6. **Set risk levels:** stop-loss = 1.5 × ATR from entry, target = 2.5 × ATR — so the levels are sized
   to each asset's actual volatility (≈ 1:1.7 reward-to-risk).
7. **Render** an annotated chart + a styled PDF per timeframe.

### What the output shows
A clean PDF per timeframe with one card per asset: the call badge (green/red/amber), entry/target/stop,
a table of all indicator values, Fibonacci levels, and a 6-month/2-year chart with support, resistance
and Fib lines drawn.

### The real artifacts (what to actually open in the interview)
This is genuinely an **Excel + Python** workflow:
- **`Daily_Levels_Tracker.xlsx`** — an Excel workbook I maintain each morning. The **Pivot Levels** sheet
  takes yesterday's High/Low/Close and computes pivot, R1/R2 and S1/S2 with live formulas
  (`P = (H+L+C)/3`, `R1 = 2P − Low`, `S1 = 2P − High`); the **Trade Calls** sheet auto-calculates
  reward:risk for each entry/stop/target.
- **Python** — automates the same analysis across four assets and three timeframes so it stays current.
> *Demo line:* "I keep the levels and calls in this Excel workbook — here's the formulas — and I automated
> the repetitive part in Python so the daily note builds itself."

### The standout talking point (multi-timeframe)
> "Gold recently flagged **SELL on the daily** but **BUY on the monthly** — that's a short-term pullback
> inside a long-term uptrend. A good analyst reconciles timeframes: I'd be cautious shorting it because
> the bigger trend is up."

### Likely questions & answers
- **"Why ATR-based stops instead of a fixed %?"** → "A fixed 2% stop is too tight for Bank Nifty and too
  wide for a calm stock. ATR sizes the stop to how much the asset actually moves, so I'm not stopped out
  by normal noise."
- **"What if all your indicators disagree?"** → "That's a HOLD. I only act on confluence; mixed signals
  mean no edge."
- **"Is this automated or your analysis?"** → "The data and levels are automated in Python to save time;
  the judgement — which call to publish and how to frame it — is mine. Automation just keeps it current."

---

# PROJECT 3 — Multi-Asset Technical Coverage Watchlist
*Tools: Excel + Python.*

### What it does (one line)
Screens **21 assets across 6 sectors** (indices, banking, IT, energy/materials, auto/FMCG, commodities)
and tags each **Buy/Sell/Hold** with a ★ strength rating and a stop-loss — a morning coverage sheet for
relationship managers.

### How it works — step by step
1. Pull 2 years of daily data for each name.
2. Compute the **daily trend** (from 20/50-MA and price) and, by resampling, the **weekly trend** — this
   is the **multi-timeframe confluence**.
3. Compute RSI, MACD, a candlestick read (engulfing/hammer/doji/shooting-star), ATR.
4. **Composite score** across daily trend + weekly trend + MACD + price-vs-50MA + RSI extremes +
   candlestick. The **★ strength** reflects how many factors align.
5. Apply the same oversold/overbought guardrail; set an ATR stop on actionable calls.
6. Group by sector, sort by conviction, and render a one-page PDF + CSV with a Buy/Sell/Hold summary count.

### The real artifacts (what to actually open in the interview)
An **Excel + Python** coverage workflow:
- **`Coverage_Watchlist.xlsx`** — 21 assets grouped by sector. I read daily trend, weekly trend, RSI and
  MACD and drop them in; the **View** column computes via formula (daily Up *and* weekly Up = BUY; both
  Down = SELL; else HOLD), the **★ Strength** counts how many factors align, RSI cells colour red/green
  at 70/30, and a **Summary** box counts BUY/SELL/HOLD with `COUNTIF`.
- **Python** — runs the same scan automatically across all 21 names.
> *Demo line:* "This is my Excel coverage sheet — it scores each name from the reads I enter; the Python
> version just does the whole scan for me in one run."

### The edge — multi-timeframe confluence
> "The strongest setups are where the **daily and weekly trends agree**. A name that's up on both is a
> higher-conviction buy than one that's up on the daily but down on the weekly — that second one is just
> a bounce in a downtrend."

### Likely questions & answers
- **"How do you rank what to look at first?"** → "By conviction — the ★ strength — within each sector,
  so an RM can scan the strongest setups per sector instantly."
- **"Why group by sector?"** → "Sector rotation matters; an RM covering banking wants the banking view
  together, and clustering shows when a whole sector is trending."
- **"Isn't this just the report for more stocks?"** → "Different purpose — the report is a deep note on a
  few assets; the watchlist is broad coverage to *spot* where to look. They're the scan and the deep-dive."

---

# HONEST LIMITATIONS (acknowledging these shows maturity)
If asked "what are the weaknesses?", say any of these — it signals you think critically:
- **No transaction costs / slippage** in the backtest yet — real returns would be a bit lower.
- **Rules-based, not discretionary** — the scoring is mechanical; a human analyst adds context (news,
  events, macro) the model can't see.
- **Commodity data uses global benchmarks** (COMEX gold, WTI crude) as proxies for MCX — the technicals
  transfer, but exact MCX levels differ with USD/INR and duties.
- **Backtest is in-sample** — I'd add walk-forward / out-of-sample testing to be rigorous.

---

# 60-SECOND ELEVATOR VERSION (if they want it short)
> "Three projects covering the analyst workflow: a **backtester** that tested eight strategies over ~6
> years on proper metrics — Sharpe, Sortino, drawdown, profit factor; a Python-automated **research
> report** for indices and commodities across daily/weekly/monthly with Buy/Sell/Hold calls and ATR
> stops; and a **sector watchlist** that screens 21 assets on daily+weekly confluence. The honest finding
> from the backtest was that the simple strategies didn't beat buy-and-hold in a bull market, which taught
> me to validate ideas with data rather than trust them."

---
*Run everything before the interview with:* `python run_all.py` *— outputs land in each project's
`output/` folder. Pair this with the Handbook (theory) and the crash course (rapid revision).*
