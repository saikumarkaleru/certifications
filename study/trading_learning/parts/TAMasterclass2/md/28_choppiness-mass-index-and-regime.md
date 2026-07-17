# Choppiness Index, Mass Index & Regime Filters

The single most expensive mistake in technical analysis is not picking the wrong direction — it is trading the wrong *type of market* with the wrong *type of strategy*. A breakout system run in a choppy range gets chopped to death; a mean-reversion system run in a strong trend gets steamrolled. The market spends most of its life in one of a small number of **regimes** — trending, ranging, quiet, volatile — and the whole game is (a) knowing which regime you're in and (b) deploying the matching strategy. This chapter covers the two best-known regime-detection indicators, the **Choppiness Index** and the **Mass Index**, plus a broader toolkit of regime filters for Nifty, Bank Nifty and NSE stocks in 2026.

## Why regime detection matters more than signals

Consider a simple truth: a 20-day breakout entry has a completely different expectancy depending on the environment. In a trending market it captures big moves with a high payoff; in a range it produces a stream of small losses as every breakout fails. The *signal is identical* — only the regime changed. This is why professional systems almost always have a **regime filter** as the first gate: before any entry logic runs, the system asks "is this the kind of market where my edge exists?" and stands aside if not.

Regime detection answers questions like:
- Is the market **trending or ranging**? (Determines breakout vs fade.)
- Is volatility **expanding or contracting**? (Determines position size and whether a big move is coming.)
- Is a trend **exhausting**? (Determines whether to trail tight or exit.)

The Choppiness Index primarily answers the first; the Mass Index primarily flags the third; and a small suite of supporting filters (ADX, Bollinger BandWidth, ATR percentile) rounds out the picture.

## Part A — The Choppiness Index

### What it is & why it works

The Choppiness Index (CHOP), developed by Australian commodities trader E.W. Dreiss, measures **how directional versus how sideways** price action has been over a lookback window. It does *not* predict direction — it is deliberately direction-agnostic. It answers one question: is the market trending (efficiently moving) or chopping (moving a lot but going nowhere)?

The insight it exploits: in a strong trend, the market covers a lot of *net* distance relative to the total path it travels — it moves efficiently. In a choppy range, it travels a huge total path (lots of up-down candles) but nets almost no distance. CHOP quantifies exactly this ratio.

### Mechanics & formula

CHOP compares the **sum of the true ranges** over N periods against the **total range** (highest high to lowest low) over the same N periods:

```
CHOP = 100 × LOG10( SUM(TrueRange, N) / (MaxHigh(N) − MinLow(N)) ) / LOG10(N)
```

- **Numerator inside the log:** the sum of each bar's true range — the *total path travelled*.
- **Denominator:** the net high-to-low range over the window — the *net distance*.
- The LOG10 normalisation with LOG10(N) scales the output to a **0–100 range**.

Reading it:
- **CHOP > 61.8** → the market is **choppy / consolidating** (high total path relative to net range). Range/mean-reversion conditions; breakouts unreliable.
- **CHOP < 38.2** → the market is **trending** (efficient net movement). Breakout/trend-following conditions favoured.
- **38.2–61.8** → transitional / neutral.

Note the 61.8 and 38.2 thresholds are the Fibonacci levels Dreiss chose; they're conventions, not magic. **Default period: 14.** A crucial behavioural point: CHOP is *counter-intuitively inverted* — a **high CHOP often precedes a breakout** (energy is coiling in the range), and a **low CHOP often precedes consolidation** (the trend has spent itself). So CHOP is best used as a *setup* filter: high CHOP = "get ready for a directional move," low CHOP = "the trend may be maturing, don't chase."

### Worked India example (levels & ₹)

Take Bank Nifty on the daily chart (reconstructed; verify live):

Bank Nifty has been oscillating between **50,500 support** and **52,000 resistance** for three weeks. The 14-period CHOP is reading **68** — well above 61.8, confirming a choppy, coiled range. Your read: **do not** trade breakouts blindly here; either fade the edges (short near 52,000, long near 50,500) or wait for the coil to resolve.

Then price closes decisively above 52,000 on strong volume, and over the next three sessions CHOP collapses from 68 to **34** — below 38.2. This drop *confirms the regime has flipped to trending*. Now your breakout-continuation and pullback-buy strategies are live. You buy the first pullback to the breakout zone (~52,000, now support) with a stop below at 51,600 (400 pts; one lot of 35 = ₹14,000 risk), targeting a measured move equal to the range height (52,000 − 50,500 = 1,500 pts → target ~53,500).

The CHOP told you *when* to switch from range-fade mode to trend-follow mode — which is exactly the regime decision that determines whether your strategy has an edge.

### How to trade it

| CHOP reading | Regime | Strategy to deploy |
|---|---|---|
| **> 61.8** (rising/high) | Choppy range, energy coiling | Fade the range edges; prepare breakout orders; reduce size |
| **Falling through 61.8** | Range breaking, trend starting | Activate breakout/trend-follow entries |
| **< 38.2** (low) | Strong trend, but maturing | Trail stops tight; don't initiate fresh breakout longs; watch for exhaustion |
| **Rising off a low** | Trend losing efficiency | Tighten management; expect consolidation |

CHOP is a **filter and context tool, never a standalone entry signal.** It tells you which *strategy* to run, not when to click buy.

## Part B — The Mass Index

### What it is & why it works

The Mass Index, developed by Donald Dorsey, is a very different regime tool. It doesn't measure trend-vs-range; it measures **volatility expansion via the widening and narrowing of the daily high-low range**, and it's designed to flag one specific, powerful event: an impending **trend reversal**.

The logic: before a trend reverses, the range between highs and lows tends to *widen* (a "range bulge") as the trend makes its final, emotional push and volatility expands. Dorsey found that when this range-widening reaches a threshold and then contracts, a reversal frequently follows. The Mass Index captures the bulge.

### Mechanics & formula

```
Single EMA  = 9-period EMA of (High − Low)
Double EMA  = 9-period EMA of the Single EMA
EMA Ratio   = Single EMA / Double EMA
Mass Index  = SUM(EMA Ratio, 25 periods)
```

- The high-low range is smoothed once (9-EMA), then that is smoothed again (9-EMA of the 9-EMA).
- The **ratio** of single to double EMA rises when the range is expanding (single EMA outruns the slower double EMA) and falls when contracting.
- Summing the ratio over 25 periods gives the Mass Index, which typically oscillates around **25–27**.

**The "Reversal Bulge" signal (Dorsey's rule):**
1. The Mass Index rises **above 27** (a significant range bulge — volatility has expanded).
2. Then it falls back **below 26.5**.
3. That drop-back from 27 to below 26.5 is the **reversal bulge** — it flags that the current trend is likely to reverse *soon*.

Critically, the Mass Index says **nothing about direction.** It only says "a reversal is likely." You must consult the price trend and other tools to know *which way*: if the market was trending up into the bulge, expect a top; if down, expect a bottom.

### Worked India example (levels & ₹)

Take a strongly trending NSE large-cap stock — say it has run from ₹2,800 to ₹3,600 over two months (reconstructed):

As the stock makes its final parabolic push toward ₹3,600, the daily high-low ranges widen dramatically (big emotional candles). The Mass Index climbs from its baseline ~25 to **27.4** — the bulge. A few sessions later, as the ranges start to contract, the Mass Index falls back to **26.3**, completing the reversal bulge.

Your read: **a reversal is likely.** The prevailing trend was up, so you expect a **top**. You don't short blindly on the Mass Index alone — you now watch for a *price confirmation*: a bearish engulfing candle, a break of the rising trendline, or a close below the 20-EMA. When price breaks the trendline at ₹3,520, you exit longs and/or initiate a short with a stop above the recent high ₹3,610 (₹90 risk), targeting the prior consolidation near ₹3,300.

The Mass Index gave you the *early warning* — days before the trendline broke — that this trend was structurally exhausting. That lead time is its entire value.

### How to trade it

| Element | Rule |
|---|---|
| **Signal** | Mass Index rises above **27**, then falls below **26.5** = reversal bulge |
| **Direction** | Determined by the *existing* trend (up trend → expect top; down trend → expect bottom) — Mass Index alone is direction-agnostic |
| **Confirmation** | Require a price trigger: trendline break, engulfing candle, MA cross |
| **Entry** | On the price confirmation, not on the bulge itself |
| **Stop** | Beyond the extreme made during the bulge |
| **Target** | Prior consolidation / support-resistance zone |
| **Timeframe** | Daily is the classic; works on higher intraday TFs too |
| **Regime** | Use it specifically to catch the *end* of mature trends |

## Part C — Supporting regime filters

CHOP and Mass Index are specialists. A complete regime toolkit adds a few more:

### ADX (Average Directional Index)
The workhorse trend-strength filter. **ADX > 25** = trending (deploy trend strategies); **ADX < 20** = ranging (deploy mean-reversion). ADX rising = strengthening trend; ADX falling from a high = trend weakening. Many Indian system traders use ADX(14) as the *primary* regime gate and CHOP as a cross-check — when both agree (ADX>25 and CHOP<38.2), trend conviction is high.

### Bollinger BandWidth
BandWidth = (Upper Band − Lower Band) / Middle Band. It measures volatility. A **historically low BandWidth (the "Squeeze")** signals volatility contraction that typically precedes a large expansion move — the coil before the spring. On Bank Nifty, a tight BandWidth squeeze on the daily often precedes an explosive expiry-week move. BandWidth doesn't give direction; pair it with the range breakout.

### ATR Percentile
Rank the current ATR against its own last 100 sessions. **Low ATR percentile (<20%)** = quiet regime, expect expansion and use *wider* relative stops as a % once it expands; **high ATR percentile (>80%)** = already volatile, reduce position size (your fixed-₹ risk buys fewer units when ATR is high). ATR-based position sizing is the practical bridge between regime detection and risk management.

### Combining into a regime dashboard

A robust regime read stacks these into a simple table you can glance at each morning:

| Filter | Trending signal | Ranging signal | Volatility signal |
|---|---|---|---|
| **ADX(14)** | > 25 | < 20 | — |
| **CHOP(14)** | < 38.2 | > 61.8 | — |
| **BandWidth** | expanding | flat | squeeze = expansion coming |
| **ATR percentile** | — | — | low = quiet, high = volatile |
| **Mass Index** | — | — | bulge = reversal risk |

When ADX and CHOP *agree*, trust the regime read. When they disagree (e.g., ADX 22, CHOP 45 — both neutral), stand aside; ambiguous regime is itself a signal to reduce activity.

## How the whole thing drives strategy selection

The payoff of regime detection is a simple decision tree you run *before* looking at any entry signal:

1. **Is it trending?** (ADX>25 AND CHOP<38.2) → run **trend/breakout/pullback** strategies. Ride winners, trail stops. Ignore overbought/oversold oscillator signals.
2. **Is it ranging?** (ADX<20 AND CHOP>61.8) → run **mean-reversion**: fade range edges, buy support/sell resistance, use RSI/Stochastic reversals. Ignore breakout signals — most will fail.
3. **Is volatility squeezing?** (low BandWidth, low ATR percentile) → **prepare**: set breakout orders both sides, reduce size until the move resolves, expect a big directional expansion.
4. **Is a mature trend bulging?** (Mass Index reversal bulge, CHOP very low) → **defend**: tighten stops, book partials, watch for the reversal trigger; don't add to the trend.

An India-specific overlay: layer the **event calendar** on top. F&O expiry (last Thursday), RBI policy, Union Budget, and quarterly results all inject regime shifts. A BandWidth squeeze *into* expiry week on Bank Nifty is a classic coiled-spring setup; a Mass Index bulge *into* a results announcement warns you a trend may be pricing in the event and is set to reverse on the news.

## Pitfalls

- **Using regime indicators as entry triggers.** CHOP, Mass Index, ADX are *context* tools. They tell you *which strategy to run*, never *when to click buy*. Always pair with a price trigger.
- **Threshold worship.** 38.2/61.8 (CHOP), 27/26.5 (Mass Index), 25/20 (ADX) are conventions. Backtest them on *your* instrument and timeframe; a Bank Nifty intraday CHOP behaves differently from a Nifty daily.
- **Lag.** All these indicators smooth data and therefore lag. By the time CHOP confirms a trend, part of the move is gone — that's the price of avoiding false starts. Accept the trade-off or use faster settings and accept more whipsaw.
- **Direction confusion on the Mass Index.** It flags *that* a reversal is likely, never *which way*. Traders who short a Mass Index bulge in an uptrend without waiting for the price break get caught in the trend's final push.
- **Conflicting filters.** When ADX says trend and CHOP says chop, don't cherry-pick the one you like — treat disagreement as "unclear regime, reduce activity."
- **Regime changes are the danger zone.** The transition from range to trend (and back) is where most losses cluster, because your regime read lags the actual change. Size down during transitions.

## Interview-ready summary

*The Choppiness Index (CHOP) measures whether the market is trending or ranging by comparing the total path travelled (sum of true ranges) to the net range over N periods, scaled 0–100: above 61.8 = choppy/consolidating (fade edges, expect a coiled breakout), below 38.2 = trending (run breakout/trend strategies). The Mass Index measures volatility via a range bulge — when it rises above 27 then falls below 26.5, it flags an impending trend reversal (direction-agnostic; the existing trend tells you which way). Both are regime/context filters, not entry triggers. Round out the toolkit with ADX (trend strength), Bollinger BandWidth (squeeze detection), and ATR percentile (position sizing). The core discipline: detect the regime first, then deploy the matching strategy — breakouts in trends, fades in ranges, preparation in squeezes, defence in exhaustion — and stand aside when the filters disagree.*
