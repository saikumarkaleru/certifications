# Fisher Transform & Connors RSI

Most oscillators — RSI, stochastics, CCI — share a hidden weakness. Their outputs pile up in the middle of their range and only rarely reach the edges. Because price itself does not follow a bell curve, the signals these indicators give are smeared: a "70" on the RSI today does not mean the same thing as a "70" last week. Two comparatively modern tools attack this problem from opposite ends. The **Fisher Transform** re-shapes the distribution of price so that turning points become sharp, unambiguous spikes. **Connors RSI** rebuilds the RSI concept from three components to produce a mean-reversion oscillator that is honest about how *stretched* a move really is. Both were designed for exactly the kind of choppy, headline-driven, gap-prone tape that Indian traders live with — Nifty gapping 150 points on a US CPI print, Bank Nifty whipping 800 points around the RBI policy, a midcap locking limits after results. This chapter builds both from the ground up, trades them on real NSE instruments, and is honest about where each one fails.

## Part A — The Fisher Transform

### What it is and why it works

John Ehlers, a signal-processing engineer who migrated into trading, observed that price does *not* have a Gaussian (normal) distribution. It has fat tails and a fat middle. The Fisher Transform is a mathematical function that takes an input bounded between -1 and +1 and converts it into an output whose distribution is roughly Gaussian — meaning extreme readings become genuinely rare and therefore genuinely meaningful. The formula amplifies values near the edges of the input range enormously. An input of 0.99 gets thrown out to roughly +2.6; an input of 0.5 barely moves. The practical effect: when price reaches a real extreme, the Fisher line *spikes* to a sharp peak or trough, and those spikes coincide remarkably well with short-term reversals.

The reason this matters for a trader is turning-point clarity. A slow-rolling RSI can hover at 68 for six candles while you wonder whether the move is done. The Fisher Transform, by contrast, tends to make a distinct pointed top and then hook down hard. You get a cleaner "the swing is exhausted" signal, at the cost of the tool being twitchy — it fires often, and many of its fires are noise. It is a scalpel, not a compass.

### Mechanics, formula and settings

The calculation runs in three steps. First, normalize price to a -1 to +1 range over a lookback period (commonly 9 or 10 bars). Using the median price (High+Low)/2, often called HL2:

```
Value1 = 0.33 * 2 * ((HL2 - LowestLow) / (HighestHigh - LowestLow) - 0.5)
         + 0.67 * PriorValue1
```

The 0.33/0.67 weighting is a light exponential smoothing that keeps Value1 from bouncing wildly. Value1 is then clamped to stay within -0.999 and +0.999 (the transform blows up to infinity at exactly ±1, so you must cap it).

Second, apply the Fisher function itself:

```
Fisher = 0.5 * ln((1 + Value1) / (1 - Value1)) + 0.5 * PriorFisher
```

That `ln((1+x)/(1-x))` is the inverse hyperbolic tangent — the mathematical heart of the transform. The final `+ 0.5 * PriorFisher` smooths the output line so it is tradeable rather than a hedge of spikes.

Third, plot a **trigger line**, which is simply the Fisher line lagged by one bar. Crossovers between Fisher and its trigger are the signal. On TradingView the built-in "Fisher Transform" indicator uses a default length of 9; on Chartink you would replicate the logic with a custom screener condition since it is not a native function.

**Settings guidance.** Length 9–10 is the standard for swing signals on the daily. For Bank Nifty on the 15-minute chart, many intraday traders shorten to 5–7 to get faster hooks; for a slow instrument like a Nifty ETF or a large-cap on the daily, lengthen to 13. Shorter = more signals, more noise. There is no magic number — match it to the instrument's volatility.

### Worked India example (levels & ₹)

Take **Reliance Industries** on the daily chart during a corrective stretch. Suppose RIL falls from around ₹2,980 to a low near ₹2,760 over eight sessions in a broad market pullback. On that final washout day the stock prints a lower low intraday to ₹2,758 but closes back at ₹2,795, forming a long lower wick. Because the Fisher Transform normalizes against the recent range, that deep intraday low pushes Value1 close to -0.95, and the Fisher line spikes down to roughly -2.3 — a genuinely rare reading. The next session the Fisher line hooks up and crosses above its trigger line while still in negative territory.

That crossover, occurring near a Fisher reading below -1.5, is the archetypal signal. You are not calling a bottom in a vacuum — the stock is near a prior demand shelf at ₹2,760 and the daily RSI is around 32. Entry on the cross at ₹2,800, stop below the wick at ₹2,745 (₹55 risk), and RIL rebounds to ₹2,920 over the next six sessions as the tape stabilizes — roughly ₹120 of reward against ₹55 risk, better than 2:1. The point is not that this always works; it is that the Fisher spike *flagged the exhaustion* far more crisply than a slow RSI would have.

### How to trade it — entry, stop, target

| Element | Long setup | Short setup |
|---|---|---|
| Trigger | Fisher crosses **above** trigger line while Fisher < -1.5 | Fisher crosses **below** trigger line while Fisher > +1.5 |
| Location filter | At/near a known support/demand zone or Fib level | At/near resistance/supply or Fib level |
| Entry | Next bar open after the cross confirms | Next bar open after the cross confirms |
| Stop | Below the swing low that produced the spike | Above the swing high that produced the spike |
| Target 1 | Prior swing high / mean (20-EMA) | Prior swing low / mean (20-EMA) |
| Target 2 | Opposite Fisher extreme (+1.5) | Opposite Fisher extreme (-1.5) |
| Best timeframe | Daily for swings; 15-min for intraday index | Same |
| Regime | Range-bound or late-trend exhaustion | Range-bound or late-trend exhaustion |

The single most important rule: **only take Fisher signals that fire from an extreme (beyond ±1.5), and only with location confluence.** Crosses that happen near the zero line are meaningless chop.

### Confluence, including OI

The Fisher Transform is a timing tool, not a standalone system. It shines when it *confirms* something else:

- **Divergence.** Price makes a lower low but the Fisher trough is higher than the previous trough — classic bullish divergence, and the Fisher's sharpness makes the two troughs easy to compare visually.
- **Volume.** A Fisher bottom spike on a high-volume climax bar is far more reliable than one on thin volume.
- **Option chain / OI.** On a Bank Nifty 15-minute Fisher buy signal near a level like 51,200, check the option chain: if 51,000 PE is showing the highest OI (a put wall / support) and PE writers are adding while CE unwinding is visible, the Fisher exhaustion signal and the OI-defined support agree. That confluence — technical exhaustion plus structural support from writers — is a much higher-quality trade than the Fisher cross alone. Conversely, if 51,000 PE OI is being *shed* aggressively (writers running), the "support" is dissolving and you skip the long.

### Pitfalls

- **Whipsaw in trends.** In a strong up-trend the Fisher will repeatedly spike to +2 and hook down, generating short signals that get run over. Never fade a strong trend on Fisher alone.
- **The ±1 blow-up.** If you code it yourself and forget to clamp Value1, the `ln` term explodes. Always cap at ±0.999.
- **Over-optimization.** Traders tune the length until it "looks perfect" on history. On the daily, 9 or 10 is fine; resist curve-fitting.
- **Gap distortion.** A big overnight gap in a stock (results, block deal) can jam the normalization and print a spike that is not a genuine reversal, just a gap. Treat post-gap Fisher signals with suspicion.

### Interview-ready summary

*The Fisher Transform converts price, which is not normally distributed, into a near-Gaussian oscillator so that turning points become sharp, rare spikes. Built by normalizing HL2 to a -1/+1 range over ~9 bars, applying the inverse hyperbolic tangent, and smoothing, it signals on crossovers with a one-bar-lagged trigger line. Best used at extremes (beyond ±1.5) with location and OI confluence; its weakness is whipsaw in strong trends.*

## Part B — Connors RSI

### What it is and why it works

Larry Connors built this indicator specifically for **short-term mean reversion** — the observation that liquid instruments, after a stretched move, tend to snap back. The plain RSI answers one question: how strong is recent momentum? Connors RSI answers three at once by combining three separate components, each measuring a different flavor of "how overdone is this?" The result is a 0–100 oscillator that spends most of its time in the middle and only reaches genuine extremes (below 10, above 90) when a move is truly stretched. Those extremes are the tradeable events.

The philosophy is important: Connors RSI is **not** a trend-following tool and it is **not** for shorting strong stocks blindly. It is designed to buy short-term oversold conditions in instruments that are in a longer-term up-trend, and to fade short-term overbought conditions — a "buy the dip in an uptrend" quantified engine.

### Mechanics, formula and settings

Connors RSI is the simple average of three components:

```
Connors RSI = ( RSI(close, 3)  +  RSI(Streak, 2)  +  PercentRank(ROC(1), 100) ) / 3
```

**Component 1 — RSI of price, short period (default 3).** A very fast standard RSI. This captures raw short-term momentum. A 3-period RSI is jumpy by design.

**Component 2 — RSI of the streak (default 2).** First compute the "streak": the number of consecutive up-days (positive) or down-days (negative). Three up-closes in a row = +3; a down-close = -1, and so on; an unchanged close resets to 0. Then take a 2-period RSI of that streak value. This component measures *persistence* — how relentless the run has been. A stock that has closed down five days straight will have a deeply negative streak and a very low Component-2 reading.

**Component 3 — Percent Rank of the 1-day rate of change (default lookback 100).** Take today's 1-day ROC (percentage change) and ask: over the last 100 days, what fraction of daily returns were smaller than today's? If today's drop is bigger than 95 of the last 100 daily moves, this component reads near 5. This measures the *magnitude* of today's move relative to the instrument's own recent behavior — an elegant, self-calibrating volatility filter.

Average the three, and you get a value from 0 to 100. The three defaults are usually written CRSI(3, 2, 100). On TradingView the "Connors RSI" indicator ships with exactly these defaults. On Chartink you cannot compute the streak-RSI or percent-rank natively, so pure CRSI screening there requires approximation.

**Settings guidance.** The 3/2/100 defaults are Connors' own and hold up well on liquid Indian large-caps and indices. For a very fast intraday application you might drop to 2/2/50, but the tool was designed for daily-bar mean reversion and works best there.

### Worked India example (levels & ₹)

Consider **HDFC Bank** on the daily during an orderly market correction. The stock is above its rising 200-DMA (longer-term uptrend intact — the precondition), but it has closed *down four sessions in a row*, sliding from ₹1,720 to ₹1,648. On the fourth down-day it falls another 1.4% — a move bigger than most of its recent daily changes.

Now the three components align:
- **Component 1**, RSI(3), is near 8 — deeply oversold on fast momentum.
- **Component 2**, RSI(2) of the streak, is near 5 — the four-day down-streak makes persistence extremely stretched.
- **Component 3**, percent-rank of today's ROC, is near 6 — today's drop is in the bottom few percent of the last 100 days.

Average ≈ (8 + 5 + 6) / 3 ≈ **6.3** — a reading below 10, the classic Connors buy zone. Because HDFC Bank is above its 200-DMA, this is a textbook "oversold dip in an uptrend" long. Entry near the close at ₹1,648, or next-morning; the Connors mean-reversion exit is *not* a fixed target but a signal: exit when CRSI closes back above 50 (or when the stock has two consecutive up-closes / a higher-high day). Over the next three sessions HDFC Bank rebounds to ₹1,700, CRSI pushes past 60, and you book roughly ₹52 per share. A protective stop sits below the swing at ₹1,625, ₹23 risk. The trade's edge came from all three dimensions — momentum, streak persistence, and magnitude — agreeing that the drop was overdone.

### How to trade it — entry, stop, target

| Element | Long (mean-reversion buy) | Short (mean-reversion fade) |
|---|---|---|
| Precondition | Price **above** rising 200-DMA | Price **below** falling 200-DMA (or index-level overbought) |
| Trigger | CRSI closes **below 10** (aggressive: below 5) | CRSI closes **above 90** (aggressive: above 95) |
| Entry | On the close or next open | On the close or next open |
| Stop | Below the recent swing low / 2×ATR | Above the recent swing high / 2×ATR |
| Exit (primary) | CRSI closes back **above 50** | CRSI closes back **below 50** |
| Alt exit | Two up-closes / touch of 5-EMA | Two down-closes / touch of 5-EMA |
| Timeframe | Daily (its native home) | Daily |
| Regime | Pullback within a larger trend | Overextension within a range/downtrend |

The defining discipline: **Connors RSI exits on a signal, not a price target.** You are harvesting a snap-back of unknown size, so you let the oscillator tell you when the rubber band has returned to neutral (the 50 cross).

### Confluence, including OI

- **The 200-DMA gate** is non-negotiable for the long side — it converts a dangerous "catch a falling knife" into a "buy the dip in a bull." Skipping this filter is the number-one reason Connors RSI strategies blow up.
- **Support/resistance.** A CRSI-below-10 reading that coincides with price tagging a well-tested support zone is materially stronger than one in mid-air.
- **Breadth.** For an *index* Connors signal (e.g., Nifty CRSI < 10), check the advance-decline and the percentage of Nifty stocks above their 20-DMA. If breadth is washed out simultaneously, the mean-reversion odds improve.
- **Option chain / OI.** On a Nifty daily CRSI oversold reading near, say, 24,600, look at where put OI is stacked. If 24,500 PE holds the largest OI and PE writers are defending it, structural support and statistical oversold agree — a cleaner long. If instead OI is thin below and PCR is falling, the market is not yet defending, and the snap-back may be shallow or delayed.

### Pitfalls

- **Trending straight through.** In a genuine crash (2020 March, a sharp global de-risk), CRSI can pin below 5 for many days as the instrument keeps falling. Mean reversion assumes the trend eventually holds; when the *regime* breaks, the tool bleeds. The 200-DMA filter and a hard stop are your defenses.
- **Illiquid names.** The percent-rank and streak components need a clean daily series. On thin midcaps with frequent gaps and circuits, CRSI readings are unstable.
- **Shorting strong stocks.** CRSI > 90 in a powerful uptrend is *not* a short signal — strong stocks stay overbought. Only fade overbought when the larger structure is weak.
- **Over-trading.** Because CRSI reaches extremes fairly often on volatile names, it is tempting to take every signal. Wait for confluence; quality over quantity.

### Interview-ready summary

*Connors RSI is a short-term mean-reversion oscillator averaging three components — a 3-period RSI of price (momentum), a 2-period RSI of the up/down streak (persistence), and the percent-rank of the 1-day ROC over 100 days (magnitude). Readings below 10 flag oversold, above 90 overbought; exits trigger on the CRSI 50 cross, not a fixed target. It is meant for buying dips above the 200-DMA, and its cardinal sin is being used to fight a broken regime.*

## Fisher vs Connors — when to reach for which

They solve different problems and pair well. The **Fisher Transform is a turning-point timer** — it tells you *when* a swing looks exhausted with a sharp, visual spike, and it works on any timeframe including intraday index trading. **Connors RSI is a stretch quantifier** — it tells you *how statistically overdone* a daily move is, and it comes with a built-in trend filter philosophy. A robust workflow: use Connors RSI on the daily to *select* which liquid, above-200-DMA name is oversold enough to buy the dip, then drop to the 15-minute or hourly chart and use the Fisher Transform to *time* the actual entry on the intraday exhaustion hook. One picks the trade; the other picks the moment.

Both share the same honest caveat that governs all oscillators: they measure *relative* extremes, not absolute tops or bottoms. In a strong trend, "overbought" and "oversold" are just descriptions of strength, not reversal signals. Use them to fade *within a range* or to time *pullbacks within a trend* — never to stand in front of a freight train. Combine either with location (support/resistance, Fibonacci), with breadth for indices, and with option-chain OI for structural confirmation, and you convert a twitchy math trick into a disciplined edge.
