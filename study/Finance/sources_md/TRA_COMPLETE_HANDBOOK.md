# The Technical Research Analyst Handbook
### A complete, in-depth reference — every topic, explained from the ground up
*Prepared for Saikumar Kaleru. Read top to bottom; each part builds on the last. Bold terms are the vocabulary interviewers listen for.*

---

# PART 1 — FOUNDATIONS OF TECHNICAL ANALYSIS

## 1.1 What technical analysis really is
**Technical analysis (TA)** is the study of **price and volume data** — usually on charts — to forecast the *future direction* of a market. It does not care *what* a company does or *whether* it is "cheap." It only studies **how the price has behaved** and what that implies next.

A technical analyst believes the chart already contains the collective decisions of every buyer and seller — institutions, retail, algos — and that those decisions leave **repeatable footprints** because human emotion (fear and greed) repeats.

## 1.2 The three core assumptions (the philosophy)
1. **The market discounts everything.** Every known fact — earnings, news, interest rates, sentiment — is already reflected in the price. So studying price *is* studying all of it at once.
2. **Prices move in trends.** Once a direction is established, it is more likely to continue than reverse. This is *the* reason TA works — it lets you ride trends.
3. **History repeats itself.** Chart patterns and reactions recur because mass psychology is constant across decades.

## 1.3 Technical vs Fundamental vs Quantitative
- **Fundamental analysis** answers **WHAT to buy** — it values a business (earnings, growth, debt, management, macro). Time horizon: months to years.
- **Technical analysis** answers **WHEN to buy or sell** — timing entries and exits from price behaviour. Time horizon: minutes to months.
- **Quantitative analysis** uses **statistics and code** to find and test edges systematically (your backtester sits here).
- A strong analyst blends them: *fundamentals pick the stock, technicals time the trade, quant validates the rule.*

## 1.4 Dow Theory — the foundation everything is built on
Charles Dow's six tenets are the bedrock of TA:
1. **The averages discount everything** (same as assumption 1).
2. **The market has three trends:** *Primary* (months–years, the tide), *Secondary* (weeks–months, corrective waves), *Minor* (days, ripples).
3. **Primary trends have three phases:** **Accumulation** (smart money quietly buys), **Public Participation** (trend-followers pile in, biggest move), **Distribution** (smart money sells to the late crowd).
4. **The averages must confirm each other** — e.g., an index and a related index should move together to confirm a trend.
5. **Volume must confirm the trend** — volume should expand in the direction of the primary trend.
6. **A trend stays in force until a clear reversal** — don't call a top/bottom prematurely.

## 1.5 Types of charts
- **Line chart** — connects closing prices. Clean, good for seeing the big trend.
- **Bar chart (OHLC)** — each bar shows Open, High, Low, Close.
- **Candlestick chart** — same OHLC data but visual and colour-coded; the global standard (covered in depth in Part 2).
- **Heikin-Ashi** — averaged candles that smooth noise and make trends visually obvious.
- **Renko / Point & Figure** — plot price *movement* (not time); filter out noise to highlight S/R and trends.

## 1.6 Timeframes and "multiple timeframe analysis"
The same chart looks different on different timeframes. A pro **always checks more than one**:
- **Higher timeframe (e.g., weekly/daily)** = the *context / dominant trend*.
- **Lower timeframe (e.g., hourly/15-min)** = the *entry timing*.
- **Rule:** trade in the direction of the higher timeframe trend, time the entry on the lower one. Conflicting timeframes = lower-conviction trade.

---

# PART 2 — PRICE ACTION & CHART READING

## 2.1 Candlesticks — full anatomy
Each candle covers one period and shows four prices:
- **Open** and **Close** form the **real body**.
- The thin lines above/below are **wicks / shadows**, marking the **High** and **Low**.
- **Bullish candle** (green/white): close > open. **Bearish candle** (red/black): close < open.
- **A long body** = strong conviction; **a small body** = indecision; **long wicks** = rejection of a price level.

### Single-candle patterns
- **Doji** — open ≈ close (tiny body). Indecision; potential reversal, especially after a long trend.
- **Hammer** — small body at the top, long lower wick (≥2× body). After a downtrend = **bullish reversal** (buyers rejected lower prices).
- **Hanging Man** — same shape as hammer but after an *uptrend* = bearish warning.
- **Shooting Star** — small body at bottom, long upper wick, after an uptrend = **bearish reversal**.
- **Marubozu** — full body, no wicks = extreme conviction in that direction.

### Two/three-candle patterns
- **Bullish Engulfing** — a big green candle completely engulfs the prior red body = strong bullish reversal.
- **Bearish Engulfing** — mirror image = bearish reversal.
- **Piercing Line / Dark Cloud Cover** — partial engulfing reversals.
- **Morning Star** (bullish) / **Evening Star** (bearish) — three-candle reversals: big trend candle, small indecision candle, big opposite candle.
- **Three White Soldiers / Three Black Crows** — three strong candles in a row confirming a reversal.

**Interpretation rule:** candlestick signals matter most **at a level** (support/resistance) and **with volume** — a hammer at support on high volume is far stronger than one in mid-air.

## 2.2 Support and Resistance — the most important concept in TA
- **Support** = a price zone where **demand** repeatedly overwhelms supply and stops a fall. A "floor."
- **Resistance** = a price zone where **supply** overwhelms demand and stops a rise. A "ceiling."
- **Why they exist:** memory. Traders remember prices where they bought/sold and act again there.
- **Role reversal (polarity):** once **broken**, old resistance becomes new support, and old support becomes new resistance. This is one of the most reliable behaviours in markets.
- **Types of S/R:** horizontal levels (swing highs/lows), trendlines, moving averages, Fibonacci levels, round numbers (e.g., Nifty 24,000), and pivot points.
- **Strength factors:** the more times a level is tested, the more significant it is — *but* every test drains it, and eventually it breaks.

## 2.3 Trendlines and channels
- **Uptrend line** — drawn under **higher lows**; acts as support.
- **Downtrend line** — drawn over **lower highs**; acts as resistance.
- **Channel** — two parallel trendlines containing price; buy near the lower rail, sell near the upper rail in a sideways/rising channel.
- A trendline needs **at least two touches** to draw and a **third** to confirm. A decisive break warns of a trend change.

## 2.4 Chart patterns
Chart patterns are recognisable shapes that tend to resolve in a predictable direction. They fall into **reversal** and **continuation** groups.

### Reversal patterns (trend likely to flip)
- **Head & Shoulders** — three peaks, the middle (head) highest, with a "neckline." Break below the neckline = bearish target ≈ head-to-neckline distance projected down. **Inverse H&S** = bullish bottom.
- **Double Top (M) / Double Bottom (W)** — two failed attempts at a level = reversal.
- **Triple Top / Bottom** — stronger version.
- **Rounding Top / Bottom (saucer)** — slow, gradual reversal.

### Continuation patterns (trend likely to resume)
- **Triangles:** *Ascending* (flat top, rising lows — bullish bias), *Descending* (flat bottom, falling highs — bearish bias), *Symmetrical* (converging — breakout in trend direction).
- **Flags & Pennants** — short pause after a sharp move ("flagpole"), then continuation. Target ≈ flagpole height.
- **Wedges** — rising wedge = bearish, falling wedge = bullish (counter-intuitive — learn this).
- **Rectangles** — sideways consolidation between S/R, then breakout.
- **Cup & Handle** — a rounded base then a small pullback (handle), then breakout = bullish.

### Gaps
- A **gap** is empty space where price jumps between sessions. Types: **breakaway** (starts a move), **runaway/continuation** (mid-trend), **exhaustion** (end of move), **common** (noise). Gaps often "fill" later.

---

# PART 3 — TECHNICAL INDICATORS (IN DEPTH)
Indicators are math applied to price/volume to make a signal clearer. They fall into four families: **trend, momentum, volatility, volume.** *Use them to confirm price action, never blindly.*

## 3.1 Trend indicators
- **Moving Average (MA):** average of the last N closes; smooths noise.
  - **SMA** weights all days equally; **EMA** weights recent days more (faster, less lag).
  - Use: price above MA = uptrend; MA slope = trend direction; MAs act as dynamic S/R.
  - **Crossovers:** short MA crossing above long MA = bullish. **Golden Cross** = 50-DMA above 200-DMA (major bullish). **Death Cross** = opposite.
- **MACD (Moving Average Convergence Divergence):** (12-EMA − 26-EMA) = MACD line; its 9-EMA = signal line; the gap = histogram.
  - Bullish when MACD crosses above signal; histogram shows momentum strength; **MACD divergence** warns of reversals.
- **ADX / DMI (Average Directional Index):** measures **trend strength** (0–100), not direction. **ADX > 25 = strong trend; < 20 = weak/range.** +DI and −DI lines show direction. *Crucial because indicators like RSI work differently in trends vs ranges.*
- **Parabolic SAR:** dots that flip above/below price; trailing-stop and trend-direction tool.
- **Supertrend:** ATR-based trend line, very popular in Indian markets for intraday F&O.
- **Ichimoku Cloud:** an all-in-one system (trend, S/R, momentum) using a "cloud" (Kumo); price above the cloud = bullish.

## 3.2 Momentum indicators (oscillators)
Oscillators move within a range and flag **overbought/oversold** and **divergence**. Best in **sideways** markets.
- **RSI (Relative Strength Index):** 0–100 (default 14). >70 overbought, <30 oversold. In strong uptrends RSI can *stay* overbought — don't short blindly. **Divergence** (price up, RSI down) is its most powerful signal. The 50 line = trend bias.
- **Stochastic Oscillator:** compares close to the high-low range (%K and %D lines), 0–100, >80/<20 zones. Good for ranges and divergence.
- **CCI (Commodity Channel Index):** measures deviation from average price; ±100 thresholds.
- **Williams %R:** like stochastic, inverted scale (0 to −100).
- **ROC / Momentum:** raw rate of price change.
- **MFI (Money Flow Index):** "volume-weighted RSI" — momentum that includes volume.

## 3.3 Volatility indicators
- **Bollinger Bands:** 20-SMA ± 2 standard deviations. Bands **widen** in volatility, **narrow** ("squeeze") before big moves. Price riding the upper band = strength; tags of the lower band in a range = bounce candidates. **Bollinger squeeze** is a classic breakout setup.
- **ATR (Average True Range):** the average daily range (true range accounts for gaps). Pure **volatility gauge** — does not give direction. Used to **size stop-losses** (e.g., 1.5–2× ATR) and position sizing so each trade risks a similar amount.
- **Keltner Channels:** like Bollinger but ATR-based; squeeze strategies combine both.
- **Donchian Channels:** highest high / lowest low over N periods — the basis of classic breakout systems.

## 3.4 Volume indicators
*Volume is the fuel; price is the car.* Moves on rising volume are trustworthy.
- **OBV (On-Balance Volume):** cumulative volume (added on up days, subtracted on down days); confirms trends and shows accumulation/distribution via divergence.
- **VWAP (Volume-Weighted Average Price):** the average price weighted by volume during the day — institutions benchmark fills against it; a key **intraday** S/R level.
- **Volume Profile:** shows volume **by price level** (not time), revealing high-volume nodes (strong S/R) and the **Point of Control (POC)**.
- **A/D Line (Accumulation/Distribution)** and **Chaikin Money Flow (CMF):** measure buying vs selling pressure.

## 3.5 Fibonacci tools
Based on the ratios 0.236, 0.382, 0.5, 0.618 (golden ratio), 0.786.
- **Fibonacci Retracement:** after a move, pullbacks often reverse at these % levels. **38.2%–61.8%** is the key zone; 61.8% is the most watched.
- **Fibonacci Extension:** projects targets beyond the prior move (1.272, 1.618) — used to set profit targets.
- **Confluence:** Fib levels lining up with S/R or a moving average = high-probability zone.

## 3.6 Pivot points
Calculated from the prior day's High, Low, Close: a central **Pivot (P)** plus support (S1, S2, S3) and resistance (R1, R2, R3) levels. Hugely popular **intraday** for indices and F&O; price above P = bullish bias for the day.

## 3.7 The golden rule of indicators
**Indicators lag — price leads.** Use 2–3 *non-redundant* indicators (e.g., one trend + one momentum + volume), look for **confluence**, and let **price action at key levels** make the final call. Stacking five momentum indicators that all say the same thing is false confidence.

---

# PART 4 — MARKET THEORIES & FRAMEWORKS

## 4.1 Divergence (master this)
**Divergence** = price and an oscillator (RSI/MACD) disagree.
- **Regular bearish divergence:** price makes a **higher high**, indicator makes a **lower high** → uptrend weakening, possible top.
- **Regular bullish divergence:** price makes a **lower low**, indicator makes a **higher low** → downtrend weakening, possible bottom.
- **Hidden divergence:** signals trend *continuation* (e.g., price higher low, indicator lower low in an uptrend = trend resumes).

## 4.2 Elliott Wave Theory
Markets move in repetitive **wave cycles** driven by crowd psychology:
- A trend unfolds in **5 waves** (1-2-3-4-5, "impulse") followed by a **3-wave correction** (A-B-C).
- Waves are **fractal** (the same pattern appears on every timeframe).
- Powerful but subjective; used to anticipate where a move is in its life-cycle.

## 4.3 The Wyckoff Method
Explains how "smart money" operates through cycles: **Accumulation → Markup → Distribution → Markdown.** Teaches you to read **accumulation/distribution ranges**, springs (false breakdowns), and the relationship between price and volume to follow institutional footprints.

## 4.4 Market cycles & sector rotation
- Markets cycle with the economy: early-cycle, mid, late, recession. Different **sectors** lead at each stage (e.g., financials early, energy/materials late, defensives in downturns).
- **Relative strength analysis** (comparing a stock/sector to the index) tells you what's leading — analysts rotate coverage toward leaders.

## 4.5 Sentiment & breadth
- **India VIX** — the "fear gauge"; high VIX = fear/volatility, often near bottoms.
- **Put-Call Ratio (PCR)** — options sentiment (covered in Part 5).
- **Market breadth** — **Advance/Decline line**, % of stocks above their 200-DMA, new highs vs new lows. Breadth confirms or warns against an index move (a rally on narrow breadth is fragile).

---

# PART 5 — DERIVATIVES: FUTURES & OPTIONS (F&O)
*Your D.E. Shaw desk was F&O — expect deep questions here.*

## 5.1 What derivatives are
A **derivative** derives its value from an **underlying** (stock, index, commodity). Used for **hedging, speculation, and leverage**. Traded in **lots** (fixed quantity), with monthly/weekly **expiries**.

## 5.2 Futures
- A **futures contract** is a binding agreement to buy/sell the underlying at a set price on a future date.
- **Long futures** = bullish; **short futures** = bearish. Leverage via **margin** (you post a fraction of contract value).
- **Basis** = futures price − spot price. **Contango** = futures > spot (normal); **Backwardation** = futures < spot (often tight supply, common in commodities).
- **Cost of carry** = interest + storage − dividends; explains the futures-spot gap.
- **Rollover** — moving a position to the next expiry; high rollover % signals trend conviction.

## 5.3 Options — the core
An **option** is the **right, not the obligation**, to buy/sell the underlying at a **strike price** before/at **expiry**, for a **premium**.
- **Call option** = right to **buy** → bought when **bullish**.
- **Put option** = right to **sell** → bought when **bearish**.
- **Buyer** pays premium, has limited risk (premium) and unlimited upside. **Seller (writer)** receives premium, has limited profit but large risk.

### Moneyness
- **ITM (In-the-Money):** has intrinsic value (call strike < spot; put strike > spot).
- **ATM (At-the-Money):** strike ≈ spot.
- **OTM (Out-of-the-Money):** no intrinsic value, only time value.
- **Premium = Intrinsic value + Time value.** Time value decays to zero by expiry.

## 5.4 The Option Greeks (know all five)
- **Delta** — change in option price per ₹1 move in the underlying (also ≈ probability of expiring ITM). Calls 0→1, puts 0→−1.
- **Gamma** — the rate of change of delta; highest for ATM options near expiry (the "acceleration").
- **Theta** — **time decay**: how much value the option loses each day. Negative for buyers, positive for sellers.
- **Vega** — sensitivity to a 1% change in **implied volatility**. Long options are long vega.
- **Rho** — sensitivity to interest rates (least important intraday).

## 5.5 Implied Volatility (IV) — you worked on IV surfaces
- **IV** is the market's **expectation of future volatility**, backed out of option prices (via Black-Scholes). High IV → expensive options.
- **IV vs HV:** implied (forward-looking) vs historical/realised (backward-looking).
- **IV Rank / IV Percentile** — where current IV sits versus its own past range; tells you if options are "cheap" or "expensive."
- **Volatility Skew / Smile** — IV differs across strikes; equity index puts usually have higher IV (crash protection demand). Plotting IV across strikes **and** expiries gives the **volatility surface** (your project).
- **Trading logic:** buy options when IV is low, sell premium when IV is high.

## 5.6 Open Interest (OI) & option-chain analysis
- **Open Interest** = total outstanding contracts. **Rising OI + rising price** = fresh longs (strong); **rising OI + falling price** = fresh shorts; **falling OI** = unwinding.
- **Option chain** = the full grid of calls/puts by strike with price, OI, IV, volume.
- **Put-Call Ratio (PCR)** = put OI ÷ call OI. **PCR > 1** = bearish positioning (often contrarian bullish); **< 0.7** = bullish/greedy.
- **Support/Resistance from OI:** the strike with the **highest call OI** acts as resistance; **highest put OI** acts as support.
- **Max Pain** = the strike where option buyers lose the most / writers gain the most; price often gravitates there near expiry.

## 5.7 Core option strategies
- **Covered Call** — hold stock + sell a call: income, caps upside.
- **Protective Put** — hold stock + buy a put: insurance.
- **Long Straddle** — buy call + put at the **same strike**: profit from a **big move either way** (event/earnings plays); needs a move bigger than the combined premium.
- **Long Strangle** — same idea with **different OTM strikes**: cheaper, needs a bigger move.
- **Bull Call Spread / Bear Put Spread** — buy one option, sell another to **reduce cost** and cap risk/reward.
- **Iron Condor** — sell an OTM call spread + put spread: profit when price stays **range-bound** (income in low volatility).
- **Butterfly** — bet on price pinning a specific strike.

## 5.8 Worked example — reading the Greeks on a real position
*Nifty spot at 24,500. You buy 1 lot (75 units) of a 24,600 Call, premium ₹180, with Delta 0.42, Gamma 0.003, Theta −8.5, Vega 12.**

**Interpreting each Greek on this position:**
- **Delta 0.42** — if Nifty rises 100 points, this option gains ≈ 0.42 × 100 = ₹42 per unit, or ₹42 × 75 = **₹3,150** on the lot (before Gamma's second-order effect). Delta also approximates a 42% probability of expiring ITM.
- **Gamma 0.003** — as Nifty moves, Delta itself changes by ≈0.003 per point. After a 100-point rise, new Delta ≈ 0.42 + (0.003 × 100) = 0.72 — the position gains sensitivity *faster* as it moves further ITM, which is why Gamma is called the "acceleration" of the option's price move.
- **Theta −8.5** — this position loses ≈₹8.5 per unit *per day* purely from time decay if nothing else changes, i.e. ₹8.5 × 75 = **₹637.50/day** — a buyer is fighting this decay every single day the trade is held, which is why option buying requires the underlying to move meaningfully and soon, not just eventually.
- **Vega 12** — a 1-percentage-point rise in implied volatility adds ≈₹12 per unit (₹900 on the lot); a fall in IV costs the position the same amount even if the underlying doesn't move at all — this is why buying options right before a scheduled event (results, a central-bank decision) is risky even if the *direction* call is correct: IV often collapses ("IV crush") right after the event, working against a long-option holder even on a correct directional move.

**The synthesis a TRA must be able to state out loud:** "This is a long-delta, long-gamma, negative-theta, positive-vega position — it wants the underlying to move up, fast, with rising or at least stable implied volatility; every day that passes without a move, and any drop in IV, works against it."

## 5.9 Worked example — a long straddle P&L around an earnings event
*Stock at ₹500 ahead of results. Buy the 500 Call for ₹18 and the 500 Put for ₹16 — total premium paid ₹34. Breakevens: 500 + 34 = ₹534 (upside) and 500 − 34 = ₹466 (downside).*

**Model answer.** The position profits if the stock moves *outside* the ₹466-₹534 range by expiry (or sooner, from an IV spike), regardless of direction — this is the textbook "big move either way" trade for a binary event like earnings. If the stock closes at ₹560 post-results: the call is worth 560 − 500 = ₹60, the put expires worthless, net P&L = 60 − 34 = **+₹26 per share**. If the stock closes at ₹495 (a modest, unremarkable move): the call expires worthless, the put is worth 500 − 495 = ₹5, net P&L = 5 − 34 = **−₹29 per share** — a straddle loses money on a move that's "real" in direction but not big enough to clear the combined premium cost, which is precisely why sizing the expected move (often estimated from the option chain's implied volatility itself) against the premium paid is the core skill in event-driven options trading, not just having a directional view.

---

# PART 6 — COMMODITIES
*The JD's first line is "Analyze Commodity, Futures & Options."*

## 6.1 The Indian commodity market
- Traded mainly on the **MCX (Multi Commodity Exchange)**; agri commodities on **NCDEX**.
- Categories: **Bullion** (gold, silver), **Energy** (crude oil, natural gas), **Base metals** (copper, zinc, aluminium, lead), **Agri** (cotton, soybean, etc.).
- Indian prices **track global benchmarks** and adjust for the **USD/INR** rate.

## 6.2 Gold
- **Drivers:** the **US dollar** (inverse — strong USD weakens gold), **real interest rates** (rising real yields hurt gold, which pays no income), **inflation** (hedge), **safe-haven demand** in crises, and central-bank buying.
- Benchmark: **COMEX** (USD/oz); Indian MCX gold also moves with **USD/INR** and import duty.

## 6.3 Silver
- Part precious metal, part **industrial** (solar, electronics) → more volatile than gold. The **gold-silver ratio** is watched for relative value.

## 6.4 Crude Oil
- Benchmarks: **WTI** (US) and **Brent** (global). **Drivers:** **OPEC+** supply decisions, geopolitics (Middle East), global demand/growth, US inventory data (EIA), and the USD.
- **Contango/backwardation** in the futures curve signals supply tightness.

## 6.5 Natural gas & base metals
- **Natural gas** — extremely volatile, weather-driven (heating/cooling demand).
- **Copper ("Dr. Copper")** — a barometer of global economic health due to its industrial use.

## 6.6 Cross-asset & seasonality
- Commodities have **seasonal** tendencies (e.g., gold demand around Indian festivals/weddings; gas in winter).
- Same TA toolkit (trend, S/R, RSI, MACD, MAs, Fibonacci) applies directly to commodity charts.

---

# PART 7 — INDICES & THE BROADER MARKET

## 7.1 Indian indices
- **Nifty 50** — 50 largest, most liquid NSE stocks; the national benchmark.
- **Sensex** — BSE's 30-stock benchmark.
- **Bank Nifty** — 12 major banks; **more volatile**, the most traded F&O index in India.
- **Fin Nifty, Nifty Midcap, Nifty Next 50,** and **sectoral indices** (IT, Pharma, Auto, FMCG, Metal) — used for sector rotation and relative strength.

## 7.2 Global cues
- **GIFT Nifty (formerly SGX Nifty)** — signals the likely opening of Nifty based on overnight global moves.
- **US indices** — **Dow, S&P 500, Nasdaq**; **Asian** (Nikkei, Hang Seng) and **European** opens set the tone.
- **Dollar Index (DXY), US 10-year yield, crude, and FII/DII flows** all drive Indian markets.

## 7.3 Volatility & breadth
- **India VIX** — expected 30-day volatility; spikes in fear.
- **Advance/Decline, % above 200-DMA, new highs/lows** — breadth gauges that confirm index health.

---

# PART 8 — RISK & TRADE MANAGEMENT
*This is what separates a professional from a gambler. Interviewers test it hard.*

## 8.1 The stop-loss
A **stop-loss** is a pre-decided exit price that caps your loss if you're wrong. **Non-negotiable.** Types:
- **Fixed % stop**, **level-based stop** (below support), **ATR/volatility stop**, **moving-average stop**, **time stop**.
- **Trailing stop** — moves with price to lock in profit while letting winners run.

## 8.2 Risk:Reward and R-multiples
- **Risk:Reward (R:R)** = potential reward ÷ potential risk. Demand **≥ 1:2** so you can be right less than half the time and still profit.
- **R-multiple** — express every result in units of initial risk (R). A trade that makes 3× your risk = +3R. Thinking in R keeps you objective.

## 8.3 Position sizing
- **Risk a fixed small % of capital per trade** (commonly 1–2%). Position size = (capital × risk%) ÷ (entry − stop). This ensures no single trade can hurt you and that volatile instruments get smaller size (via wider stops).

## 8.4 Portfolio-level risk
- **Diversification & correlation** — don't hold five positions that are really the same bet (e.g., all bank stocks + Bank Nifty).
- **Max drawdown discipline, exposure limits, and avoiding over-leverage** in F&O (leverage cuts both ways).

## 8.5 The money-management rules pros live by
Cut losses quickly, let winners run, never add to a loser hoping it recovers, size to volatility, and **survive first — returns come second.**

## 8.6 Worked example — position sizing and a full R-multiple trade
*Capital: ₹10,00,000. Risk per trade rule: 1.5% of capital. Stock trades at ₹842; support/stop level at ₹810; target at ₹930.*

**Position sizing:**
```
Risk amount = 10,00,000 × 1.5% = ₹15,000
Risk per share = Entry − Stop = 842 − 810 = ₹32
Position size = Risk amount / Risk per share = 15,000 / 32 ≈ 468 shares
```
Round to 468 shares (or down to 460 for a round lot, whichever the broker/market convention requires) — this is the *maximum* size that keeps the pre-defined loss at exactly ₹15,000 (1.5% of capital) if the stop is hit, regardless of how "confident" the analyst feels about the trade; conviction should show up in written rationale, never in oversizing beyond the risk rule.

**Risk:Reward and R-multiple:**
```
Reward per share = Target − Entry = 930 − 842 = ₹88
R:R = Reward / Risk = 88 / 32 = 2.75  (i.e. "1:2.75")
```
This clears the ≥1:2 minimum bar comfortably — meaning the trade can be *wrong* more than a third of the time (specifically, a bit above a 26.7% win rate, from the breakeven formula in 10.4's expectancy calculation) and still be profitable over a large enough sample, which is the entire point of thinking in R-multiples rather than any single trade's outcome.

**If the trade hits target:** P&L = 468 × 88 = ₹41,184, or **+2.75R** relative to the ₹15,000 initial risk.
**If the trade hits the stop instead:** P&L = −468 × 32 = −₹14,976 ≈ **−1R**, exactly as sized — the loss was known and bounded *before* the trade was placed, which is the entire discipline this section is testing.

---

# PART 9 — RESEARCH REPORT WRITING & RECOMMENDATIONS
*Your actual daily output as a TRA.*

## 9.1 Report cadence
- **Daily** — pre-market note: overnight global cues, key levels for Nifty/Bank Nifty/commodities, top trade ideas.
- **Weekly** — trend review, sector view, positional calls.
- **Monthly** — bigger-picture market outlook and themes.

## 9.2 Anatomy of a good call
Every recommendation must state: **Instrument · View (Buy/Sell/Hold) · Entry · Target(s) · Stop-loss · Time horizon · Rationale.**
- The **rationale** ties together trend, levels, indicators, and (for F&O) OI/IV.
- Always give a **stop** and an honest **risk:reward** — a call without a stop is unprofessional.

## 9.3 Communicating to clients & RMs
- Be **clear and concise** — RMs relay to clients who aren't technical. Lead with the call, then the reason.
- Talk in **probabilities, not certainties** ("favourable risk-reward to go long above X," not "this will go up").
- **Track and own your calls** — record hit/miss; credibility is built on a transparent track record.

---

# PART 10 — BACKTESTING & QUANTITATIVE BASICS
*Your differentiator — but you must understand it, not just run it.*

## 10.1 What backtesting is
Applying a **rules-based strategy to historical data** to estimate how it would have performed — to validate an edge **before** risking capital.

## 10.2 Methodology & pitfalls
- **No look-ahead bias** — only use data available at decision time (act on *yesterday's* signal).
- **Survivorship bias** — include delisted names, or results are too rosy.
- **Overfitting (curve-fitting)** — tuning a strategy so perfectly to the past that it fails live. Guard with **out-of-sample testing** and **walk-forward analysis**.
- **Costs** — include brokerage, slippage, and taxes, or live results disappoint.

## 10.3 Performance metrics (define each)
- **CAGR** — smoothed annual growth rate.
- **Sharpe ratio** — excess return ÷ total volatility; risk-adjusted return. >1 good, >2 excellent.
- **Sortino ratio** — like Sharpe but only penalises **downside** volatility (fairer).
- **Maximum Drawdown** — worst peak-to-trough loss; measures pain/risk of ruin.
- **Win rate** — % of profitable trades (high win rate ≠ profitable if losses are huge).
- **Profit factor** — gross profit ÷ gross loss; >1 = profitable.
- **Exposure** — % of time invested.
- **Calmar ratio** — CAGR ÷ max drawdown.

## 10.4 Statistics you should know
- **Mean, median, standard deviation** (volatility = std of returns), **normal distribution & fat tails** (markets have more extreme moves than "normal" predicts), **correlation** (−1 to +1), **mean reversion vs momentum**, and **probability/expectancy** = (win% × avg win) − (loss% × avg loss).

## 10.5 Worked example — evaluating a backtested strategy's full metric set
*A backtested strategy over 3 years: 240 trades, 96 winners (avg win ₹4,200), 144 losers (avg loss ₹1,800). Starting capital ₹5,00,000, ending capital ₹8,90,000. Worst peak-to-trough equity decline during the period: ₹1,10,000 from a peak of ₹7,20,000. Strategy's daily returns have a standard deviation implying an annualised volatility of 18%; risk-free rate assumed 6%.*

**Win rate and expectancy:**
```
Win rate = 96/240 = 40%
Expectancy = (0.40 × 4,200) − (0.60 × 1,800) = 1,680 − 1,080 = +₹600/trade (positive → profitable edge)
```
Note the strategy is profitable *despite* a 40% win rate — well below 50% — because winners are more than double the average loser in size, directly illustrating why win rate alone is a misleading metric without pairing it with average win/loss size (10.3's explicit warning).

**Profit factor:**
```
Gross profit = 96 × 4,200 = ₹4,03,200
Gross loss = 144 × 1,800 = ₹2,59,200
Profit factor = 4,03,200 / 2,59,200 ≈ 1.56  (>1 = profitable; a common quality bar is >1.5)
```

**CAGR:**
```
Total return = 8,90,000/5,00,000 = 1.78x over 3 years
CAGR = 1.78^(1/3) − 1 ≈ 21.1%
```

**Maximum drawdown:**
```
Max DD = 1,10,000 / 7,20,000 ≈ 15.3%
```
A ~21% CAGR against a ~15% max drawdown is a reasonable, though not exceptional, risk-adjusted profile — the next step is checking the **Calmar ratio** (CAGR ÷ Max DD = 21.1/15.3 ≈ 1.38) to see how the return compares directly to the worst pain endured, which is often more intuitive to a risk-averse allocator than the Sharpe ratio alone.

**Sharpe ratio** (using the 21.1% CAGR as the return proxy and 18% annualised volatility):
```
Sharpe ≈ (21.1% − 6%) / 18% ≈ 0.84
```
Below the ">1 good, >2 excellent" bar from 10.3 — a red flag that, despite a healthy-looking CAGR, this strategy's return isn't especially well-compensated for the volatility it experiences along the way, and an interviewer would expect the candidate to flag this tension (good CAGR, mediocre Sharpe) explicitly rather than only citing the flattering CAGR number.

---

# PART 11 — REGULATION, COMPLIANCE & ETHICS

## 11.1 NISM Series-XV: Research Analyst
The **SEBI-mandated certification** required to legally publish research/recommendations in India. It covers TA, fundamentals, valuation, and — importantly — **regulations and ethics**.

## 11.2 SEBI (Research Analysts) Regulations — key duties
- **Disclosure of conflicts** — reveal any holding or interest in a recommended security.
- **No front-running** — never trade ahead of your own published research.
- **Separation** of research from trading/dealing and investment-banking functions.
- **Rational basis & records** — recommendations must be justified and documented; maintain research records.
- **Fair dealing** — no misleading claims, no guaranteed returns, suitability in mind.

## 11.3 Why it matters in interviews
Showing you understand **disclosures, conflict management, and that research must be compliant** signals maturity beyond just chart-reading.

---

# PART 12 — BEHAVIOURAL FINANCE & MARKET PSYCHOLOGY
Markets are driven by **fear and greed**; TA is, at heart, the study of crowd psychology.
- **The emotional cycle:** optimism → euphoria (tops) → anxiety → panic/capitulation (bottoms) → hope → optimism.
- **Common biases to know:** **herd mentality**, **FOMO**, **loss aversion** (holding losers, cutting winners early), **confirmation bias** (seeing only what supports your view), **anchoring**, **recency bias**, and **overconfidence**.
- **The professional edge** is *discipline* — a written plan, predefined stops, and the emotional control to follow them when the crowd panics.

---

# PART 13 — TOOLS OF THE TRADE
- **Charting:** **TradingView** (industry standard), broker terminals, MetaTrader, and pro terminals like **Bloomberg / Refinitiv (Reuters)**.
- **Data & screening:** NSE/MCX option chains, **Chartink / screeners**, Excel for tracking and models.
- **Coding (your edge):** **Python** (pandas, yfinance, matplotlib) for backtesting, screening, and automating reports — exactly what your projects demonstrate.
- **Knowing the workflow:** pre-market prep → global cues + levels → intraday monitoring → end-of-day report → calls tracking.

---

# PART 14 — COMMON TRADING SETUPS (putting it together)
- **Trend-following / pullback:** in an uptrend, buy a dip to a moving average or support with the trend.
- **Breakout:** enter when price clears a key level/range on rising volume; stop just inside the range.
- **Reversal:** trade a confirmed reversal pattern + divergence at a major level (higher risk).
- **Mean-reversion:** in a range, fade extremes (buy oversold support, sell overbought resistance).
- **Momentum:** buy strength/relative-strength leaders; ride until momentum fades.
- **Event/volatility (F&O):** straddles/strangles around results or events when a big move is expected.
- **Every setup needs:** a trigger, an entry, a **stop**, a target, and a reason. No exceptions.

---

# QUICK REVISION — THE ANALYST'S MENTAL CHECKLIST
1. What's the **trend** on the higher timeframe?
2. Where are the key **support/resistance** levels?
3. What do **price action / candles** say at those levels?
4. Do **indicators** (one trend + one momentum + volume) confirm? Any **divergence**?
5. For F&O: what do **OI, PCR and IV** say?
6. Define the trade: **entry, target, stop, risk:reward, horizon.**
7. **Size** the position to risk a small fixed % .
8. Write the call **clearly with a rationale** — and **track** it.

---

# APPENDIX A — TWO FULLY WORKED TRADE SETUPS, START TO FINISH

## A.1 A trend-following pullback setup (cash equity)
*Stock XYZ, daily chart: higher highs and higher lows for 4 months (confirmed uptrend). Price pulls back to the rising 50-day EMA at ₹455, which has held as support on the last two pullbacks. RSI on the pullback reads 44 (not oversold, healthy pullback in an uptrend rather than a breakdown). Volume on the pullback is below average (no aggressive selling); a bullish hammer candle forms exactly at the EMA.*

**Full call, in the "Anatomy of a good call" format from 9.2:**
- **Instrument**: XYZ equity (cash).
- **View**: Buy.
- **Rationale**: Established uptrend (Dow Theory higher-highs/higher-lows) intact; pullback to a proven dynamic support (50-day EMA, held twice before) on low, non-aggressive volume; RSI healthy (not overbought going in, not showing bearish divergence); a bullish reversal candle (hammer) confirms buyers stepping in exactly at the level — trend + level + price action + momentum all align (the "confluence" principle from Part 3.7).
- **Entry**: ₹458 (on confirmation above the hammer's high).
- **Stop**: ₹446 (just below the hammer's low and the EMA — invalidates the setup if hit).
- **Target**: ₹512 (prior swing high — the next logical resistance).
- **Risk:Reward**: Risk = 458−446 = ₹12; Reward = 512−458 = ₹54; R:R ≈ 1:4.5 — well above the ≥1:2 bar.
- **Horizon**: 3-6 weeks (swing trade, matches the daily-chart timeframe used for analysis).

## A.2 An event-driven F&O setup (results-day straddle, sized correctly)
*A large-cap stock reports quarterly results tomorrow after market close. Current price ₹1,240. The at-the-money straddle (1240 Call + 1240 Put) costs a combined ₹58. Implied volatility has risen sharply into the event (IV Rank in the 85th percentile of its own 1-year range) — a signal options are relatively expensive heading into the event.*

**Full call:**
- **Instrument**: 1240 CE + 1240 PE (long straddle), 1-lot.
- **View**: Volatility/event play, direction-agnostic.
- **Rationale**: A quarterly result is a known, scheduled binary event likely to produce a move larger than the market's average daily range; a long straddle profits from the *size* of the move in either direction. **Caution flagged explicitly**: IV Rank at the 85th percentile means the straddle is pricing in a large expected move already — the position needs the *actual* move to exceed what's already priced (roughly, the combined premium as a % of spot: 58/1240 ≈ 4.7%), and is additionally exposed to an IV-crush loss (Part 5.9) if the actual move disappoints even directionally.
- **Breakevens**: 1240 + 58 = ₹1,298 (up) and 1240 − 58 = ₹1,182 (down).
- **Risk**: capped at the ₹58/share premium paid (known, bounded loss) if the stock closes between the breakevens.
- **Position size**: sized so the *maximum* loss (full premium paid, a realistic outcome for a straddle on a quiet result) still respects the account's 1-2% per-trade risk rule from Part 8.3 — treating the entire premium as "at risk" capital, not assuming a partial, softer loss the way a stop-managed directional trade might.
- **Exit plan**: exit immediately post-results on the opening move rather than holding into further time decay — once the event that justified the trade has occurred, theta (Part 5.4) becomes a pure headwind with no further edge-justifying catalyst ahead.

# APPENDIX B — INTERVIEW Q&A (THEORY + WORKED)

1. **Q: What's the difference between technical, fundamental, and quantitative analysis, in one line each?**
   A: Fundamental answers *what* to buy (business value); technical answers *when* (price/volume timing); quantitative uses statistics/code to systematically find and validate an edge (often combining elements of both).

2. **Q: Why does Dow Theory require volume to confirm a trend?**
   A: Price movement on weak volume reflects a thin, low-conviction market that can reverse easily; volume expanding in the trend's direction shows broad participant conviction behind the move, making the trend more likely to persist — this is why a breakout on light volume (Part 2 chart-pattern content) is treated with suspicion.

3. **Q: A stock's RSI shows bearish divergence (price makes a new high, RSI makes a lower high) at a known resistance level. How would you construct the trade?**
   A: This is a confluence setup (trend/level + momentum divergence) suggesting weakening momentum right at a level where sellers have historically emerged — a short/reduce-exposure candidate with an entry on confirmation (e.g. a bearish reversal candle), a stop just above the resistance/recent high, and a target at the next support — always sized per the fixed-risk-% rule (Part 8.3), never on conviction alone.

4. **Q: Explain Max Pain and its practical use, including its limits.**
   A: Max Pain is the strike price at which the largest number of options (by value) would expire worthless, theoretically the point option writers "prefer" and price sometimes gravitates toward near expiry due to hedging flows from large option writers. Its limit: it's a probabilistic tendency observed empirically, not a guarantee, and can be overridden by strong fundamental/news-driven moves — it should inform, not solely determine, an expiry-week view.

5. **Q: Worked — what does a rising Put-Call Ratio (PCR) from 0.6 to 1.3 over a week suggest, and what's the contrarian read?**
   A: A PCR rising from 0.6 (call-heavy, bullish positioning) to 1.3 (put-heavy, bearish positioning) suggests growing bearish sentiment/hedging in the options market. The contrarian read many technical analysts apply: an extremely high PCR can signal excessive bearishness/hedging that's already priced in, sometimes preceding a relief rally, particularly if it coincides with price holding above a known support level rather than breaking it — PCR is best read alongside price action, not in isolation.

6. **Q: Why is "no look-ahead bias" one of the most common backtesting errors, and give a concrete example of how it creeps in accidentally.**
   A: Look-ahead bias means a backtest accidentally uses information not actually available at the moment a real trading decision would have been made — e.g. a strategy using a day's closing price to generate a signal that's then assumed to be actionable at that same day's open, when in reality the closing price isn't known until after the market closes; the fix is lagging every signal by at least one full period so the backtest only ever "sees" what would genuinely have been known at decision time.

7. **Q: Why might a strategy with a higher CAGR have a worse Sharpe ratio than a strategy with a lower CAGR (as in the Part 10.5 worked example)?**
   A: Sharpe measures return *per unit of volatility taken*, not raw return — a higher-CAGR strategy that achieves its return via a bumpier, more volatile equity curve can have a worse (lower) Sharpe than a steadier, lower-CAGR strategy, because the denominator (volatility) grew faster than the numerator (excess return). A professional evaluates both, since a smoother, lower-CAGR strategy may be preferable for capital that can't tolerate large drawdowns.

8. **Q: What specifically must a SEBI-registered Research Analyst disclose, and why does this matter beyond just "following the rules"?**
   A: Any personal holding or financial interest in a security they're recommending, and any conflict of interest (e.g. the analyst's firm has an investment-banking relationship with the company). This matters because undisclosed conflicts undermine the very reason clients pay attention to research in the first place — credibility — and disclosure is what lets a client correctly weight the analyst's view knowing the incentives behind it.

9. **Q: Worked — an options seller has collected ₹40,000 in premium across a month writing weekly iron condors, but one adverse week produces a ₹65,000 loss. Was the strategy "wrong"?**
   A: Not necessarily — premium-selling/income strategies (like iron condors) typically have a high win rate but an asymmetric payoff (many small wins, occasional larger losses when price moves outside the range), which is the mirror image of a long-option buyer's payoff (many small losses, occasional large win). A single adverse week doesn't invalidate the strategy; what matters is whether the *sized* risk on each individual position respected account risk rules (Part 8) and whether the cumulative expectancy (Part 10.4) across a large enough sample is positive — the same discipline of judging a strategy by process and expectancy, not any single outcome, that Part 8's "survive first" principle emphasises.

10. **Q: What's the difference between IV Rank and IV Percentile, and why might a trader care about the distinction?**
    A: IV Rank measures where current IV sits between the highest and lowest IV over a lookback period (a simple range-based measure); IV Percentile measures the percentage of days in that lookback period where IV was *lower* than the current level (a distribution-based measure) — the two can genuinely differ (e.g. IV could be near the top of its range by Rank, but only in, say, the 60th Percentile if IV spent a lot of time clustered near that high level) — Percentile is generally considered the more robust measure since it isn't distorted by a single historical outlier high or low the way Rank can be.

11. **Q: How would you structure an answer to "walk me through your process for a single trade idea," combining multiple parts of this handbook?**
    A: State the structure explicitly: (1) higher-timeframe trend context (Part 1.6, 1.4), (2) key levels — support/resistance from price structure and, for F&O names, from OI (Part 5.6), (3) price-action confirmation at that level (candlestick/pattern, Part 2), (4) indicator confluence — one trend + one momentum + volume, checking for divergence (Part 3.7, 4.1), (5) for derivatives specifically, a check of IV/OI/PCR context (Part 5.5-5.6), (6) a fully defined trade — entry, stop, target, R:R, horizon, and (7) correctly sized per the fixed-risk-% rule (Part 8.3). Walking through this structure explicitly, rather than describing an ad hoc impression of a chart, is exactly what the "Anatomy of a good call" section (9.2) and this appendix's worked examples (A.1-A.2) are modelling.

12. **Q: Why does the handbook insist a call is unprofessional without a stated stop-loss, even for a high-conviction idea?**
    A: A stop-loss is the mechanism that bounds risk to a known, pre-decided amount *before* the trade is placed — without one, a losing trade has no defined exit discipline and can compound into a much larger loss than any reasonable position-sizing calculation assumed, silently invalidating the entire risk-management framework (Part 8) the position size itself was built on. High conviction is not a substitute for a defined worst-case exit; it should, if anything, only affect position size within the fixed-risk-% rule, never remove the stop entirely.

*End of handbook. Read it twice; the second pass is where it clicks. Pair this with the one-night crash course (`INTERVIEW_PREP_STUDY_GUIDE.pdf`) for the rapid revision version.*
