# TA Question Bank Part 3 (Concepts & Indicators)

This bank continues the interview-and-viva style preparation from Volume I, but it goes deeper into the *why* behind concepts and indicators. Each answer is written the way a strong candidate would speak in a trading-desk interview or a proprietary-desk viva: define the term, explain the mechanism, ground it in an Indian instrument with real-ish levels in rupees, then add the honest caveat. Treat the numbers as approximate reconstructions to verify on your own TradingView or Chartink charts. Nothing here is a certainty; everything is a probability with a defined risk.

Work through these out loud. If you cannot explain a concept in plain language to an imaginary junior analyst, you do not yet own it.

---

## Q1. Why does technical analysis "work" at all if markets are supposed to be efficient?

TA works to the extent that price reflects the collective behaviour of participants who are *not* perfectly rational and who face real constraints — margin calls, stop-losses, mandate limits, fear and greed. The Efficient Market Hypothesis says price already discounts known information; TA does not dispute that. It says something narrower: that the *path* price takes to discount information leaves footprints — support/resistance from where people transacted, momentum from herding, mean-reversion from over-extension. In Indian markets specifically, a large retail F&O base plus concentrated institutional flows around expiry create repeatable behavioural patterns. TA exploits behaviour and liquidity structure, not a violation of information efficiency. The honest framing: TA gives you a repeatable *edge in odds and timing*, typically shifting win-rate or risk-reward a few percentage points in your favour — not a crystal ball.

## Q2. Distinguish support/resistance as a "price level" from support/resistance as a "zone."

A level is a single price; a zone is a band. Beginners draw a line at exactly 22,000 on Nifty and are frustrated when price reverses at 22,043 or 21,968. Professionals draw a *zone* — say 21,960 to 22,060 — because support is created by clustered orders, prior swing highs/lows, and round-number psychology, none of which resolve to a single tick. The mechanism: a zone marks a region where enough resting demand or supply previously overwhelmed the opposing side. When drawing zones, use the candle *bodies* for the conservative edge and *wicks* for the extreme edge. On Bank Nifty, where 200-300 point intraday swings are normal, a support "zone" might be 300 points wide (e.g., 47,700-48,000). Trading a zone means you scale entries and place stops beyond the far edge, not at the line.

## Q3. What actually causes a moving average to act as support?

Nothing magical is in the average itself. A rising 50-DMA acts as support because a large cohort of trend-followers and institutions watch it, place buy orders near it, and their aggregate demand appears there. It is a self-fulfilling reference point *reinforced by real order flow*. The 200-DMA on Nifty is the most-watched such line in India — funds describe positions as "above/below the 200." When Nifty pulled back to its rising 200-DMA near 21,700 (approximate) and bounced, that bounce was demand from participants using the same reference. The caveat: in a strong downtrend the same average becomes resistance, and in choppy markets price whipsaws across it, generating false signals. A moving average is a *dynamic* support/resistance whose reliability rises with the strength and duration of the underlying trend.

## Q4. Explain the difference between SMA, EMA, and WMA, and when each is preferable.

- **SMA (Simple)** weights every period equally. Smooth, slow, fewer whipsaws — good for defining the *primary trend* (200-SMA) and for less noisy instruments.
- **EMA (Exponential)** weights recent prices more heavily via a smoothing constant (2/(n+1)). It reacts faster to fresh price, so traders use 9- and 21-EMA for intraday Nifty/Bank Nifty entries where responsiveness matters.
- **WMA (Weighted)** uses a linear weighting scheme; it sits between the two and is less common in Indian retail practice.

The trade-off is universal: faster reaction (EMA) means earlier signals but more false ones; slower reaction (SMA) means later but cleaner signals. A common Indian intraday stack is 9-EMA and 21-EMA on the 5-minute chart for momentum, with the 50-EMA on the 15-minute defining bias. There is no "best" — match the average's responsiveness to your holding period and the instrument's noise.

## Q5. Walk through RSI properly — what is it measuring, and why is "70/30 = overbought/oversold" a trap?

RSI (Relative Strength Index, 14-period default) measures the *magnitude and velocity* of recent gains versus losses, normalised to 0-100: RSI = 100 − 100/(1 + RS), where RS is the average gain divided by average loss over the lookback. It is a momentum oscillator. The trap is treating 70/30 as automatic sell/buy triggers. In a strong uptrend — say Nifty grinding from 21,000 to 24,000 — RSI can sit above 70 for weeks; shorting each time it "crosses 70" is a way to lose money against a trend. The professional reading:

- In a **range**, 70/30 mean-reversion works reasonably.
- In a **trend**, RSI *shifts its range* — bullish trends respect 40-80, bearish trends respect 20-60. The 40 and 60 levels become the real support/resistance for momentum.
- The highest-value RSI signal is **divergence** (Q6), not the absolute level.

## Q6. What is RSI divergence, and how reliable is it?

Divergence is a disagreement between price and momentum. *Bearish* (negative) divergence: price makes a higher high but RSI makes a lower high — buyers are pushing price up on weakening momentum, warning of exhaustion. *Bullish* (positive) divergence: price makes a lower low but RSI makes a higher low — selling is losing force. Example (approximate): a stock like Reliance rallies to a new high near ₹3,020 while RSI prints 68 versus 74 at the prior high near ₹2,980 — that lower RSI high is bearish divergence, a caution flag.

Reliability, honestly: divergence is a *warning, not a trigger*. Divergences can persist for a long time in strong trends (the "divergence can stay divergent" problem). Trade it only with confirmation — a break of a short-term trendline, a reversal candle, or a failure at resistance. Weight *regular* divergence at swing highs/lows more than *hidden* divergence, and never short a raging trend on divergence alone.

## Q7. MACD — components, what a crossover really means, and its main weakness.

MACD has three parts: the **MACD line** (12-EMA minus 26-EMA), the **signal line** (9-EMA of the MACD line), and the **histogram** (MACD minus signal). It measures the *relationship between two trends of momentum*. A bullish crossover (MACD crossing above signal) says short-term momentum is accelerating relative to medium-term — a shift in favour of buyers. The zero line matters: MACD above zero means the 12-EMA is above the 26-EMA (uptrend context); crossovers above zero are higher-probability longs than crossovers below zero.

Its main weakness is **lag** — it is built from EMAs, so in a choppy, sideways Bank Nifty session it will hand you a string of losing crossovers. It also has no upper/lower bound, so you cannot read "overbought" from it directly. Best use: trend confirmation and the histogram for momentum *deceleration* (histogram shrinking while price rises = fading push). Combine with a trend filter; never trade MACD crossovers in a range.

## Q8. Compare RSI and Stochastic — when would you prefer one over the other?

Both are momentum oscillators bounded 0-100, but they measure different things. RSI measures gain/loss magnitude. **Stochastic** measures *where the close sits within the recent high-low range* — %K = (close − lowest low)/(highest high − lowest low) × 100, with %D a smoothing of %K. Because stochastic keys off the range, it is *faster and noisier* than RSI and better suited to **range-bound** instruments and shorter timeframes. Prefer stochastic for mean-reversion scalps in a sideways stock; prefer RSI for trend context and cleaner divergence on swing timeframes. Many Indian intraday traders use the *stochastic RSI* (stochastic applied to RSI values) for very responsive turns, accepting the extra whipsaw. Rule of thumb: trending regime → RSI/MACD; ranging regime → stochastic/Bollinger reversion.

## Q9. Explain Bollinger Bands and the concept of the "squeeze."

Bollinger Bands plot a middle band (usually 20-SMA) with upper and lower bands at ±2 standard deviations of price. They are an *adaptive volatility envelope*: bands widen when volatility rises and contract when it falls. Two core ideas:

1. **Mean reversion in ranges**: in a sideways market, tags of the upper band are relative-highs and lower band tags are relative-lows.
2. **The squeeze**: when bands contract sharply, volatility is compressed — the market is coiling. A squeeze does not tell you *direction*, only that a large expansion is likely soon. India example: before a big Bank Nifty expiry-week move, the daily bands often narrow, then a breakout candle expands them violently.

The classic error is "price touched the upper band, so sell." In a strong trend price *walks* the upper band — repeated tags are strength, not a sell signal. Use band tags for reversion only after confirming the regime is a range.

## Q10. What is ATR and why is it more useful for risk than for direction?

ATR (Average True Range, 14-period default) measures volatility — the average of the True Range, where True Range is the greatest of: current high−low, |high−previous close|, |low−previous close|. It has no directional information at all; a high ATR simply means large candles. Its power is in **position sizing and stop placement**. If Bank Nifty's daily ATR is ~600 points, a 100-point stop is noise-level and will be hit randomly; a sensible swing stop might be 1.5-2× ATR. For sizing: risk per trade (say ₹5,000) divided by (ATR-based stop distance × point value) gives your quantity. ATR also adapts stops to regime — the same stock needs wider stops in a volatile month than a quiet one. Use ATR to answer "how much room does this instrument need?" — never "which way is it going?"

## Q11. Define ADX and DMI. How do you read them together?

ADX (Average Directional Index) measures **trend strength, not direction**, on a 0-100 scale. It is derived alongside the DMI lines: **+DI** (positive directional indicator) and **−DI** (negative). Reading them together:

- **ADX below ~20**: weak/absent trend — a *range*. Favour mean-reversion tools; avoid breakout and trend systems.
- **ADX rising above ~25**: a trend is establishing. Now direction matters: **+DI above −DI** = uptrend; **−DI above +DI** = downtrend.
- **ADX above ~40 and turning down**: trend is mature and may be exhausting.

Practical India use: run ADX as a *regime filter*. On Nifty daily, if ADX is 15, you stop taking trend-following signals and switch to fading the range edges. ADX's weakness is lag — it confirms a trend after it has begun, so it is a filter, not a timing tool.

## Q12. What are pivot points and why are they popular with Indian intraday traders?

Pivot points are pre-calculated support/resistance levels derived from the *previous day's* high, low, and close: Pivot (P) = (H+L+C)/3, with R1/R2/R3 and S1/S2/S3 spaced off it by formula. They are popular because they are **objective, universal, and known in advance** — thousands of intraday traders and algos watch the same Bank Nifty and Nifty pivots, making them self-fulfilling reference points. A common playbook: price opening above the daily pivot with S1 as support is bullish bias; R1 and R2 are logical profit targets and reversal zones. Central Pivot Range (CPR) — the band between the pivot and the top/bottom central levels — is heavily used in India; a *narrow* CPR signals a likely trending day, a *wide* CPR a range day. Caveat: pivots are just reference maths, best combined with price action and volume at those levels.

## Q13. Explain VWAP and why institutions care about it.

VWAP (Volume-Weighted Average Price) is the average price over the session weighted by volume — cumulative (price×volume) divided by cumulative volume, reset each day. It represents the "fair average price" at which the day's business transacted. Institutions care because their execution is benchmarked against it: a fund buying below VWAP has beaten the day's average. For intraday traders, VWAP acts as a **dynamic magnet and bias line**: price above a rising VWAP = intraday bullish control; pullbacks to VWAP in an uptrending stock are classic long entries; price rejecting VWAP from below confirms bearish control. On liquid names like HDFC Bank or an index future, VWAP plus its standard-deviation bands frame mean-reversion and trend-pullback trades. Its limitation: it is an intraday tool that resets daily and loses meaning near the close as denominators grow large.

## Q14. What is the "volume precedes price" idea, and how do you actually use volume?

Volume is the fuel — it measures *conviction* behind a move. "Volume precedes price" means changes in participation often show up before decisive price moves: accumulation (rising volume on up-days, quiet down-days) can precede a breakout. Practical uses:

- **Breakout confirmation**: a resistance break on volume well above the 20-day average is far more trustworthy than a quiet break. If Nifty breaks 22,500 on tepid volume, suspect a fake-out.
- **Climax/exhaustion**: a huge volume spike after an extended move often marks capitulation or blow-off — a *turning* signal, not a continuation.
- **Effort vs. result**: big volume with tiny price progress (large effort, small result) signals absorption by the opposing side.

Weakness in India: cash-equity volume is meaningful, but for indices you must read *futures volume and options OI* since the index itself has no volume. Always compare current volume to a moving-average baseline, never in absolute terms.

## Q15. Contrast OBV and the Volume Profile — what does each tell you?

**OBV (On-Balance Volume)** is a cumulative running total that adds the day's volume on up-closes and subtracts it on down-closes. It is a *momentum-of-volume* line; its slope and divergences from price matter more than its absolute value. Rising OBV while price consolidates hints at stealth accumulation.

**Volume Profile** is entirely different: instead of plotting volume over *time*, it plots volume traded at each *price* level over a chosen range, producing a horizontal histogram. Its key outputs are the **Point of Control (POC)** — the price with the most traded volume (a magnet and strong support/resistance) — and **high/low volume nodes**. On a Bank Nifty chart, the POC of the last month might sit at 48,200; price tends to gravitate to and pause at that heavily-traded level, while low-volume gaps get crossed quickly. OBV answers "is volume flowing in or out over time?"; Volume Profile answers "at which prices is the real business being done?"

## Q16. What is Ichimoku, in plain terms, and what is the single most useful part for a beginner?

Ichimoku Kinko Hyo is an all-in-one trend system with five components: Tenkan-sen (fast line), Kijun-sen (slow/baseline), Senkou Span A and B (which form the **Cloud/Kumo** projected forward), and Chikou Span (lagging line). It looks intimidating but encodes trend, momentum, and support/resistance in one view. For a beginner the single most useful part is the **Kumo (Cloud)**: price *above* the cloud = bullish regime, *below* = bearish, *inside* = no-trade chop. The cloud's thickness measures the strength of support/resistance ahead. On a daily Nifty chart, staying long only while price holds above the cloud, and treating the Kijun-sen as a trailing reference, is a clean, mechanical way to ride trends and avoid ranges. Master the cloud first; add the crossovers later.

## Q17. Explain Fibonacci retracements — why 61.8%, and how do you use them without over-fitting?

Fibonacci retracements mark likely pullback levels within a trend: 23.6%, 38.2%, **50%**, 61.8%, and 78.6% of a prior swing. The 61.8% ("golden ratio") derives from the Fibonacci sequence and appears widely in natural growth; in markets its real power is that *so many traders watch it* that it becomes a self-fulfilling reaction zone. Usage on, say, a Nifty leg from 21,000 to 22,000: the 38.2% pullback sits at ~21,618 and the 61.8% at ~21,382 — shallow pullbacks (to 38.2%) signal a strong trend; deep pullbacks (to 61.8-78.6%) warn the trend may be failing. The over-fitting danger is drawing dozens of Fib levels until one "explains" every wiggle. Discipline: draw from one clear, significant swing; use Fib levels as *confluence* with structure (a 61.8% retracement that coincides with a prior support and the 50-EMA is a high-quality zone), not as standalone triggers.

## Q18. What is a trendline, and what makes one "valid" versus arbitrary?

A trendline connects successive swing lows (uptrend) or swing highs (downtrend) to visualise the trend's slope and dynamic support/resistance. Validity criteria that separate a real line from wishful drawing:

1. **At least two touches to draw, three to confirm** — the third touch validates the line.
2. **Touches should be meaningful swing points**, ideally on candle bodies/wicks that reversed, not random mid-candle grazes.
3. **A sensible slope** — an over-steep line (45°+) will break quickly and is unsustainable; the most durable Indian index trendlines rise at moderate angles.

A break of a valid trendline on volume signals a possible trend change or acceleration, but *retests* are common — price often breaks, pulls back to the line (now flipped), then resumes. The honest caveat: trendlines are somewhat subjective; two analysts draw slightly different lines. Use them for structure and bias, and confirm breaks with a close beyond the line plus volume, not an intrabar poke.

## Q19. Define a channel and explain how you trade within and out of one.

A channel is a pair of parallel trendlines containing price — an ascending, descending, or horizontal band. It says price is trending (or ranging) within a defined slope. **Trading within** the channel: buy near the lower rail and sell/short near the upper rail in a range or gentle trend, using the opposite rail as target and a close outside the rail as your stop. **Trading the breakout**: a decisive close *outside* the channel, especially on volume, signals acceleration or reversal; a rising channel broken to the downside often precedes a sharp fall as trapped longs exit. A useful India pattern: Nifty grinding up a well-defined ascending channel for weeks, then a break of the lower rail flags the first real trend-change warning. Measure the channel's *height* to project a rough breakout target. Caveat: channels, like trendlines, are partly subjective and work best when price has respected both rails at least twice.

## Q20. What is confluence, and why do professionals insist on it?

Confluence is the *stacking of independent signals at the same price/time*, raising the probability that a level matters. No single indicator is reliable enough alone; each has a failure mode. When several unrelated tools agree, the odds improve materially. A high-confluence Nifty long might combine: price at a prior support zone (21,950-22,000), the rising 50-EMA at the same level, a 61.8% Fibonacci retracement landing there, a bullish hammer candle, RSI turning up from ~40, *and* meaningful Put writing / call unwinding showing at that strike in the option chain. Any one of these is weak; together they form a genuine edge. Professionals insist on confluence because it filters out the majority of low-quality setups — you trade less, but each trade has better odds and a cleaner invalidation point.

## Q21. How does open interest add a dimension that price and volume alone cannot?

Open interest (OI) is the number of outstanding F&O contracts — it measures *money committed and positions held*, whereas volume measures *activity* and price measures *level*. The classic four-way read: **price up + OI up** = fresh longs (bullish, strong); **price up + OI down** = short-covering (bullish but weaker, may fade); **price down + OI up** = fresh shorts (bearish, strong); **price down + OI down** = long unwinding (bearish but weaker). OI gives you *who is doing what*. In the Indian option chain, heavy **Call OI** at a strike marks likely resistance (writers defending it), heavy **Put OI** marks likely support; **Max Pain** and the PCR add context. Around expiry, OI shifts and unwinding can override pure price patterns — the highest-quality index setups have TA levels *and* an OI story that agrees. The caveat: OI is a *positioning* map, not a timing signal, and can be misread if you ignore whether options are being written or bought.

## Q22. When indicators conflict, how do you decide? Give a framework.

Conflict is normal; a decision framework matters more than any single indicator:

1. **Establish regime first** (ADX / higher-timeframe structure). Trend vs. range determines *which* indicators to trust. In a trend, momentum tools (MACD, RSI trend-range) win; in a range, oscillators (stochastic, Bollinger reversion) win. Applying the wrong toolkit to the regime is the root cause of most conflict.
2. **Weight higher timeframes over lower.** A daily uptrend outranks a 5-minute sell signal; trade in the direction of the dominant timeframe.
3. **Prefer price action over lagging indicators.** Structure (higher highs/lows, breaks, candles at levels) is the primary; indicators are secondary confirmation.
4. **Demand confluence; when it is absent, stand aside.** Conflicting signals with no clear winner is itself information — it usually means "no trade."

The professional's edge is often *not trading* the ambiguous majority of setups. Define the regime, respect the higher timeframe, let price lead, and only act when the weight of evidence lines up.

---

### One-line memory hooks

- Support/resistance are **zones**, not lines.
- RSI/Stoch/Bollinger 70-30 rules work in **ranges**, fail in **trends** — divergence is the real edge.
- MACD, ADX, moving averages = **trend**; Stochastic, Bollinger reversion = **range**.
- ATR sizes risk; ADX gauges strength; neither gives direction.
- VWAP is the intraday fair-value magnet; POC is the multi-day one.
- OI tells you *who* holds positions; confluence tells you *when to act*.
