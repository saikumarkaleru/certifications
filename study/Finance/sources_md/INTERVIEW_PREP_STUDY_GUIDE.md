# Technical Research Analyst — One-Night Crash Course
**For Saikumar Kaleru. Everything here maps to your resume. Learn the definitions well enough to say them in your own words.**

---

## 0. Your 30-second self-intro (memorise the shape, not the words)
> "I'm an MBA-Finance candidate and NISM Series-XV Research Analyst certified. I have close to two
> years on a derivatives desk at D.E. Shaw as Member Technical, where I analysed F&O market data —
> implied volatility, open interest, option greeks — and prepared daily reports for the trading team.
> Alongside that I do technical analysis on Nifty, Bank Nifty and commodities, and I've built tools to
> backtest strategies and generate daily research reports. I'm certified to publish buy/sell research
> and I want to do exactly that as a Technical Research Analyst."

---

## PART A — What the job actually is
A **Technical Research Analyst (TRA)** studies **price charts** (not company balance sheets) to predict
where Commodity / Futures & Options / equity prices are headed, and publishes **Buy / Sell / Hold calls**
with a target and stop-loss in **daily, weekly and monthly reports**, and supports relationship managers
(RMs) with market views.

**Technical analysis vs Fundamental analysis** (very common question):
- **Fundamental** = *what to buy*. Studies company financials, earnings, valuation, economy.
- **Technical** = *when to buy/sell*. Studies price & volume charts, assuming price already reflects all
  information and that trends and patterns tend to repeat.

**The 3 assumptions of technical analysis** (say these and you sound legit):
1. **Price discounts everything** — all news/info is already in the price.
2. **Prices move in trends** — once a trend starts it tends to continue.
3. **History repeats** — patterns recur because human behaviour (fear/greed) repeats.

---

## PART B — The indicators ON YOUR RESUME (you MUST be able to explain each)

### 1. Trend
- **Uptrend** = higher highs + higher lows. **Downtrend** = lower highs + lower lows. **Sideways** = range.
- Golden rule: *"Trade with the trend."* You buy dips in an uptrend, sell rallies in a downtrend.

### 2. Support & Resistance
- **Support** = a price *floor* where buyers repeatedly step in and stop the fall.
- **Resistance** = a price *ceiling* where sellers repeatedly step in and stop the rise.
- A **breakout** above resistance (or below support) signals a new move. Old resistance, once broken,
  often becomes new support (and vice-versa).
- *Interview line:* "I buy near support with a stop just below it, and target the next resistance."

### 3. Moving Averages (MA / DMA — Daily Moving Average)
- Average of the last N closing prices; smooths out noise to show the trend.
- **SMA** = simple average. **EMA** = exponential, weights recent prices more (reacts faster).
- Common ones: **20-DMA** (short term), **50-DMA** (medium), **200-DMA** (long term).
- Price **above** its MA = bullish; **below** = bearish.
- **Golden Cross** = 50-DMA crosses *above* 200-DMA → bullish. **Death Cross** = opposite → bearish.

### 4. RSI — Relative Strength Index
- A momentum oscillator from **0 to 100** measuring how strong recent gains are vs losses (default 14 days).
- **Above 70 = overbought** (may pull back). **Below 30 = oversold** (may bounce).
- **Divergence** = price makes a new high but RSI doesn't → momentum weakening, possible reversal.
- *Interview line:* "RSI tells me if a move is overstretched; I don't chase a stock at RSI 80."

### 5. MACD — Moving Average Convergence Divergence
- = (12-day EMA − 26-day EMA), plus a **9-day signal line**, plus a **histogram** of the gap.
- **Bullish** when the MACD line crosses *above* the signal line; **bearish** when it crosses below.
- Tells you momentum and trend direction together.

### 6. Bollinger Bands
- A 20-day moving average with an upper and lower band at **±2 standard deviations**.
- They measure **volatility**: bands widen when volatile, narrow ("squeeze") when calm.
- Price near the **upper band** = strong/overbought; near the **lower band** = weak/oversold.
- A **squeeze** (very narrow bands) often comes *before* a big breakout.

### 7. Volume
- Number of shares/contracts traded. **Volume confirms price.** A breakout on high volume is reliable;
  on low volume it's suspect.

### 8. Candlestick patterns (each candle shows Open, High, Low, Close)
- Green/white = close above open (up day). Red/black = close below open (down day).
- **Body** = open-to-close; **wicks/shadows** = the highs/lows.
- **Doji** = tiny body → indecision, possible reversal.
- **Hammer** = small body at top + long lower wick → bullish reversal after a fall.
- **Bullish Engulfing** = a big green candle fully covers the prior red candle → bullish reversal.
- **Shooting Star** = small body at bottom + long upper wick → bearish reversal.

### 9. Chart patterns (know the names + what they signal)
- **Head & Shoulders** = reversal (top = bearish). **Double Top / Bottom** = reversal.
- **Triangles / Flags / Pennants** = continuation (trend resumes after a pause).

### 10. Fibonacci retracement
- After a move, prices often pull back to **23.6%, 38.2%, 50%, 61.8%** of that move before continuing.
- These levels act as support/resistance. **61.8%** is the "golden ratio" and the most watched.

### 11. ATR — Average True Range
- Measures **how much an asset typically moves in a day** (volatility). Used to **size stop-losses**:
  a wider ATR → wider stop. *Interview line:* "I set my stop ~1.5×ATR away so normal noise doesn't hit it."

---

## PART C — How to make a Buy/Sell call (the analyst's core job)
Every call has **4 parts**:
1. **View**: Buy / Sell / Hold.
2. **Entry**: the price to act at.
3. **Target**: where you book profit (often the next resistance, or a risk:reward multiple).
4. **Stop-loss**: where you admit you're wrong and exit (protects capital).

- **Risk:Reward** = (target − entry) ÷ (entry − stop). Aim for **at least 1:1.5 or 1:2**.
- *Example to say:* "Buy Bank Nifty at 58,400, target 60,300, stop 57,300 — that's roughly 1:1.7
  reward-to-risk, and I'd exit if it closes below the 50-DMA."
- **Golden rule:** a good analyst is disciplined about **stop-losses**. "I'd rather take a small loss than
  a big one." Never average down a losing trade without a reason.

---

## PART D — The markets you'll be asked about

### Nifty 50 & Bank Nifty
- **Nifty 50** = index of the 50 largest NSE companies → the benchmark for the Indian market.
- **Bank Nifty** = index of the 12 largest banks → **more volatile**, moves faster, heavily traded in F&O.
- **Sensex** = BSE's 30-stock equivalent of Nifty.

### Futures & Options (F&O / Derivatives) — you worked on this desk
- A **derivative** derives its value from an underlying (stock/index/commodity).
- **Futures** = an *obligation* to buy/sell at a set price on a future date.
- **Options** = a *right* (not obligation):
  - **Call option** = right to **buy** (you buy calls if you're bullish).
  - **Put option** = right to **sell** (you buy puts if you're bearish).
  - **Strike price** = the agreed price. **Premium** = what you pay for the option. **Expiry** = last day.
- **Open Interest (OI)** = total open contracts; rising OI + rising price = strong trend.
- **Implied Volatility (IV)** = the market's expectation of future volatility, priced into options.
  High IV = expensive options. (You analysed IV surfaces — be ready to say "IV across strikes/expiries".)
- **Option Greeks** (you tracked these):
  - **Delta** = how much the option moves per ₹1 move in the underlying.
  - **Gamma** = how fast delta changes.
  - **Theta** = time decay (options lose value as expiry nears).
  - **Vega** = sensitivity to volatility.
- **Strategies**: **Straddle** (buy call+put same strike — bet on a big move either way),
  **Strangle** (same idea, different strikes, cheaper), **Spread** (buy+sell options to cap risk/cost).

### Commodities (MCX) — the JD's first bullet
- Traded on **MCX** (Multi Commodity Exchange) in India: **Gold, Silver, Crude Oil**, natural gas, copper.
- Indian prices track **global benchmarks**: Gold → COMEX (USD/ounce), Crude → WTI/Brent (USD/barrel).
- **Drivers**: the **US dollar** (stronger USD → weaker gold), **interest rates & inflation** (gold is an
  inflation hedge / safe haven), **geopolitics & supply** (crude reacts to OPEC, wars), and **demand**.
- Same technical tools (S/R, RSI, MACD, MAs) apply to commodity charts.

---

## PART E — NISM & the rules (you're certified — know the basics)
- **NISM Series-XV: Research Analyst** is the SEBI-mandated certification to legally publish research /
  buy-sell recommendations in India.
- Key principles a Research Analyst must follow:
  - **Disclosure** of any holding/conflict of interest in a stock you recommend.
  - **No front-running** — you can't trade ahead of your own published call.
  - **Separation** of research from the dealing/trading function.
  - Recommendations must have a **rational basis** and be documented.
- *Interview line:* "Being NISM-certified means I can publish compliant research with proper disclosures
  and a documented rationale."

---

## PART F — How to explain YOUR 3 projects (they WILL ask)

**1. Daily/Weekly/Monthly Technical Research Reports (Nifty, Bank Nifty, Gold, Crude):**
> "I prepare a morning note on indices and commodities — I mark support/resistance, check RSI, MACD,
> Bollinger Bands and candlestick patterns, and give a Buy/Sell/Hold call with entry, target and an
> ATR-based stop-loss. I automated the data part in Python so the levels stay current."

**2. Multi-Strategy Technical Backtester (Python):**
> "I backtested four technical strategies — MA crossover, RSI mean-reversion, MACD trend and Bollinger
> breakout — on six years of Nifty and Bank Nifty data, and compared them to buy-and-hold on CAGR,
> Sharpe, Sortino, max drawdown, win-rate and profit factor. The active strategies underperformed
> buy-and-hold in a strong bull market, but **MACD-trend gave the best risk-adjusted return with the
> smallest drawdown** — the real lesson was validating strategies with data instead of trusting them
> blindly." *(This honesty + the metrics vocabulary impresses interviewers.)*

**Backtesting metrics — be able to define these (they're in your report):**
- **CAGR** = the smoothed annual growth rate of the strategy (return per year).
- **Sharpe ratio** = return per unit of *total* risk (volatility). Higher is better; >1 is good.
- **Sortino ratio** = like Sharpe but only penalises *downside* volatility — a fairer risk measure.
- **Max Drawdown** = the worst peak-to-trough fall the strategy suffered (how much pain you'd endure).
- **Win-rate** = % of trades that were profitable.
- **Profit Factor** = gross profit ÷ gross loss; above 1 means the system made money overall.
- **Exposure** = % of the time the strategy was actually invested (rest in cash).

**3. Multi-Asset Technical Coverage Watchlist:**
> "A ranked watchlist of 10 NSE stocks plus Gold and Crude, scored on trend, momentum and candlestick
> signals, tagging Buy/Sell/Hold with stop-losses — the kind of coverage sheet you'd hand to RMs each
> morning."

---

## PART G — 20 likely questions (one-line answers to expand on)
1. **What is technical analysis?** → Studying price/volume charts to forecast prices; price discounts everything.
2. **Technical vs fundamental?** → Fundamental = what to buy; technical = when to buy/sell.
3. **What is support & resistance?** → Floor where buyers step in / ceiling where sellers step in.
4. **Explain RSI.** → 0–100 momentum; >70 overbought, <30 oversold.
5. **Explain MACD.** → 12-EMA minus 26-EMA with a 9-signal line; cross above = bullish.
6. **What are moving averages? Golden cross?** → Smoothed avg price; 50 crossing above 200 = bullish.
7. **Bollinger Bands?** → 20-MA ±2 SD; measures volatility; squeeze precedes breakout.
8. **What's a candlestick? Name a reversal pattern.** → OHLC bar; hammer / bullish engulfing.
9. **Fibonacci retracement levels?** → 23.6/38.2/50/61.8%; pullback support/resistance.
10. **How do you decide a buy?** → Trend up + price above MAs + RSI not overbought + MACD bullish + near support.
11. **What is a stop-loss and why?** → A pre-set exit to cap losses; protects capital and emotions.
12. **Risk-reward ratio?** → Reward ÷ risk; want ≥1:2.
13. **Difference between Nifty and Bank Nifty?** → 50-stock benchmark vs 12 banks, Bank Nifty more volatile.
14. **Call vs Put option?** → Right to buy vs right to sell.
15. **What is Open Interest / Implied Volatility?** → Open contracts / market's expected future volatility.
16. **Name the option greeks.** → Delta, Gamma, Theta, Vega.
17. **What's a straddle?** → Buy call + put at same strike to profit from a big move either way.
18. **What drives gold / crude prices?** → USD, rates, inflation, safe-haven / OPEC, supply-demand, geopolitics.
19. **What does NISM RA certification allow?** → To publish compliant research with disclosures.
20. **Walk me through one of your buy calls.** → Use the Bank Nifty example in Part C.

---

## PART H — Smart questions to ASK them (shows interest)
- "Which segments will I cover — equity, F&O, or commodities — and on what timeframes?"
- "Do analysts here publish their own calls or support senior analysts first?"
- "What tools/terminals does the desk use — TradingView, broker terminal, Bloomberg?"
- "How is a call's performance tracked here?"

## Dos & Don'ts
- ✅ Speak in terms of **trend, levels, risk-reward, stop-loss** — that's the analyst's language.
- ✅ Admit what you don't know briefly, then pivot to what you do.
- ✅ Always attach a **stop-loss** to any call you mention — never sound reckless.
- ❌ Don't claim you made live buy/sell calls at D.E. Shaw — you were **Member Technical** (analysis/support).
- ❌ Don't guarantee returns or say "this will definitely go up." Analysts talk in probabilities and risk.

---

### Tonight's priority order (if short on time)
1. Part B (indicators) + Part C (buy/sell call) — **non-negotiable**, it's your core.
2. Part A (TA vs fundamental, 3 assumptions) — easy marks.
3. Part D (Nifty/Bank Nifty, options basics, commodity drivers).
4. Part F (your projects) + Part G (Q&A) — rehearse out loud.
5. Part E (NISM) + Part H — quick skim.
```
Good luck. You know more than you think once you read this twice.
```
