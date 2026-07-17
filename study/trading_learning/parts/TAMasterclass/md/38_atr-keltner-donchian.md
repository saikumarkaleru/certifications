# ATR, Keltner Channels & Donchian

## What it is & why it works

Three of the most practical tools in technical analysis share a common ancestry: they all describe price behaviour in terms of *range* rather than *direction*. Average True Range (ATR) measures how much an instrument moves per bar. Keltner Channels wrap a moving average in bands built from ATR. Donchian Channels plot the highest high and lowest low over a lookback. Together they form the "volatility and breakout" toolkit that underpins most systematic trend-following, and they are indispensable for position-sizing and stop-placement on the Nifty, Bank Nifty, and NSE stocks.

**Why range matters.** A trader's real enemy is not being wrong — it is being wrong *at the wrong size* or with a *stop in the noise zone*. If Bank Nifty routinely swings 700 points a day, a 150-point stop is inside the daily breathing room and will be hit by random noise even when your directional read is correct. ATR quantifies that breathing room objectively. It converts "the market is choppy today" from a feeling into a number. Every professional risk framework — from Turtle Trading to modern CTA books — sizes positions and sets stops as a multiple of ATR precisely because it normalises risk across instruments: 2×ATR on Nifty and 2×ATR on a mid-cap represent the *same* statistical stretch even though the rupee amounts differ wildly.

**Keltner Channels** answer a different question: is price stretched relative to its recent volatility, and is a trend underway? Because Keltner bands are built on ATR (a smoothed range) rather than standard deviation, they are *smoother* than Bollinger Bands and hug trending price more consistently. Chester Keltner's original 1960 version used the daily high-low range; Linda Raschke popularised the modern ATR-based version. The behavioural logic: in a genuine trend, price pushes *through* the upper (or lower) channel and stays there; in a range, it oscillates band to band. Keltner Channels are the tool of choice for detecting a "trend day" early.

**Donchian Channels**, created by Richard Donchian — the father of trend following — are the purest breakout tool. The upper line is the highest high of the last N bars, the lower line the lowest low. A close above the upper Donchian means "price is at a new N-bar high" — by definition a breakout. The famous Turtle system was built almost entirely on 20-day and 55-day Donchian breakouts. The reason it works is structural: new highs attract momentum, trigger stops of shorts, and reflect real demand overwhelming supply. Markets trend, and Donchian is the cleanest way to mechanically catch the start of a trend.

The three are complementary. ATR is the *engine* (raw volatility). Keltner is *ATR wrapped around a trend* (mean plus volatility bands). Donchian is *pure price extremes* (no averaging, no volatility scaling). A complete trend trader often uses all three: Donchian to enter breakouts, ATR to size and stop, Keltner to confirm the trend is real.

## The mechanics

**Average True Range (ATR).** ATR smooths the "True Range," which handles gaps that a simple high-minus-low misses. True Range for each bar is the greatest of:

| # | Measure |
|---|---|
| 1 | Current High − Current Low |
| 2 | \|Current High − Previous Close\| |
| 3 | \|Current Low − Previous Close\| |

TR = max(1, 2, 3). Taking the max of these three captures overnight gaps: if Reliance closes at ₹1,400 and gaps up to open at ₹1,440, the true range includes that ₹40 gap even though the intraday high-low might be small.

ATR is then a smoothed average of TR, classically Wilder's smoothing over 14 periods:

ATR_today = [ (ATR_prev × 13) + TR_today ] / 14

The default period is 14. ATR is expressed in the instrument's units (points for Nifty, rupees for a stock). Bank Nifty daily ATR might be ~700 points; Nifty ~180 points; a ₹1,400 stock might be ₹35. ATR has no direction — it is always positive and simply says "this is a typical bar's range."

**Keltner Channels.**

| Line | Formula | Default |
|---|---|---|
| Middle | EMA of close | EMA(20) |
| Upper | EMA + (m × ATR) | m = 2, ATR(10) |
| Lower | EMA − (m × ATR) | m = 2, ATR(10) |

The multiplier m (commonly 1.5 to 2.5) sets width. Because ATR changes slowly and smoothly, Keltner bands are cleaner than Bollinger Bands. A key relationship: when **Bollinger Bands contract inside the Keltner Channels**, volatility is unusually low — this is the "TTM Squeeze," a leading signal that expansion is near.

**Donchian Channels.**

| Line | Formula | Default |
|---|---|---|
| Upper | Highest high of last N bars | N = 20 |
| Lower | Lowest low of last N bars | N = 20 |
| Middle | (Upper + Lower) / 2 | — |

The Turtles used **20-day** for entries and a **10-day** opposite channel for exits, plus **55-day** as a longer, more selective breakout. On Indian intraday, a 20-period Donchian on the 15-min Bank Nifty chart flags the day's developing range breaks.

**Choosing parameters (India practice):**

| Use | Tool & setting |
|---|---|
| Position sizing | ATR(14) daily |
| Stop placement | 1.5–3× ATR(14) from entry |
| Trend confirmation | Keltner EMA(20), 2× ATR(10) |
| Swing breakout entry | Donchian 20-day |
| Selective/longer trend | Donchian 55-day |
| Intraday range break | Donchian 20 on 15-min |

## Reading it — a worked Nifty example

Consider Nifty on the daily chart emerging from a consolidation (illustrative levels around 24,800).

**Setup.** Nifty has ranged between 24,600 and 24,950 for a month. Daily ATR(14) has fallen from 210 points to just 130 — volatility has contracted. The Donchian 20-day upper line sits at 24,950 (the range high); the lower at 24,600. The Keltner EMA(20) is flat at ~24,780 with the upper channel at 25,040 and lower at 24,520 (2× ATR of ~130). Bollinger Bands are pinched *inside* the Keltner Channels — the TTM Squeeze is "on." Everything says a move is loading; nothing yet says which way.

**Breakout.** On a strong global cue, Nifty closes at 25,080 — above the 24,950 Donchian upper (a fresh 20-day high) *and* above the Keltner upper channel at 25,040. Two independent tools confirm: pure price is at a new extreme, and price has pushed through the ATR-volatility band. ATR immediately starts rising as ranges expand — the squeeze has fired. This dual confirmation (Donchian new high + Keltner breach) is far stronger than either alone.

**Sizing and stop.** Suppose a trader risks ₹20,000 per Nifty position. ATR(14) at the breakout is now 175 points. Using a 1.5×ATR stop = ~260 points, the stop goes at 24,820 (below the breakout and back inside the old range). Nifty's lot and per-point value then determine quantity so that 260 points of adverse move equals the ₹20,000 risk. Note how ATR — not a round number — defined a stop that sits *outside* the noise but not absurdly far.

**Trend day / walk.** Over the next two weeks Nifty rides the Keltner upper channel: closes of 25,180, 25,310, 25,290, 25,450. Each stays above the EMA(20), which now slopes up at ~25,050 as dynamic support. The Donchian 20-day upper keeps ratcheting higher with each new high. ATR has expanded to ~230, so the trailing stop (now 2.5×ATR below, or via the Donchian 10-day lower "chandelier" logic) widens with volatility, keeping the trader in the trend without getting shaken by normal pullbacks.

**Exit.** The move stalls near 25,600. Nifty closes back below the Keltner upper, then a session closes below the Donchian 10-day lower line at 25,320 — the Turtle exit trigger. The trader exits around 25,320: a ~240-point pullback from the high locked a large gain against an initial 260-point risk (better than 2R). ATR-based trailing did the work; no prediction of the top required.

## Trading it

**Strategy A — Donchian breakout (Turtle-style trend entry).**
- *Entry:* Close above the 20-day Donchian upper (long) or below the 20-day lower (short). Use 55-day for a more selective, higher-conviction version.
- *Filter:* Require the higher-timeframe trend to agree, or use the Keltner breach as a second confirmation to cut false breaks.
- *Stop:* 2×ATR(14) below entry (Turtles used 2N where N = ATR).
- *Position size:* Quantity = (Account risk per trade) / (Stop distance in points × point value). This makes every trade risk the same rupee amount regardless of instrument volatility.
- *Exit:* Opposite 10-day Donchian channel (a shorter channel exits faster than it enters), or a fixed ATR trail.
- *Management:* Add ("pyramid") on further 0.5×ATR advances, raising the stop each time — classic Turtle scaling.

**Strategy B — Keltner trend-day intraday (Bank Nifty 15-min).**
- *Context:* First 15-min candle after 9:15 closes firmly outside the Keltner channel with expanding ATR → likely trend day.
- *Entry:* On the breakout candle or the first pullback to the EMA(20) that holds.
- *Stop:* 1.5×ATR (15-min) or below the EMA.
- *Target:* Ride the channel; exit when a candle closes back through the EMA(20) or on the opposite channel tag.

**Strategy C — ATR as a universal stop (works with ANY entry).**
- Whatever your entry method, place the stop at entry ± (2 to 3 × ATR). This is the single most valuable use of ATR: it keeps stops out of random noise. On Bank Nifty with ATR ~700, a 350-point stop (0.5×ATR) is guaranteed noise-death; ~1,400 points (2×ATR) respects the instrument's real volatility.

**Scenarios:**
- *Clean trend:* Donchian entry + ATR trail rides the whole move; exits on the 10-day opposite channel with multi-R gains.
- *Whipsaw range:* Donchian breakouts fail repeatedly (the known weakness). Filter with Keltner confirmation and HTF trend; accept that trend-following loses small, often, in ranges and pays off in the occasional big trend.
- *Volatility spike (event):* ATR jumps; ATR-based stops automatically widen, preventing premature exits during a genuine expansion — but also demand smaller position size, which ATR sizing handles automatically.

## Confluence

- **Keltner + Bollinger = the Squeeze.** Bollinger inside Keltner → squeeze on; Bollinger back outside → squeeze fires. Pair with a momentum histogram for direction. This is the most-used ATR-based confluence in Indian intraday trading.

- **Donchian + volume.** A 20-day Donchian breakout on 1.5–2× average volume is far more reliable than a low-volume drift to new highs. Volume separates real demand from a thin melt-up.

- **ATR + support/resistance for stops.** Place the stop 1×ATR *beyond* a structural level (below a swing low, below a VWAP) rather than exactly at it — this defeats stop-hunt wicks that reach precisely to the obvious level.

- **Option-chain / OI (India-specific).** ATR and implied volatility (IV) tell complementary stories: ATR is *realised* range, IV is *expected* range priced into options. When Bank Nifty ATR is contracting and IV is also low (cheap options), a Donchian breakout is a high-value long-volatility trade — buy a straddle/strangle to capture the coming expansion, since option premiums under-price the pending move. When ATR spikes above what IV implied, realised vol has outrun expectations — mean-reversion of vol favours premium sellers. Also, a Donchian breakout *through* the highest-OI Call strike forces call-writer covering, adding directional fuel; combining "new 20-day high" with "breaking the call wall on OI unwind" is a strong, India-specific confluence.

- **Multi-timeframe Donchian.** Use the 55-day for the trend filter and the 20-day for entries — only take 20-day longs when price is above the 55-day midline. This alignment sharply cuts false breakouts.

## Pitfalls & false signals

1. **Donchian whipsaws in ranges.** Pure breakout systems bleed in sideways markets — many small false breaks before one real trend. This is a *feature* of trend-following (small losses, large wins), but undisciplined traders abandon the system right before the payoff trend. Filter with volume and HTF trend; accept the loss cadence.

2. **Fixed-point stops instead of ATR.** Using a flat 100-point Nifty stop across all regimes means you are far too tight in high-volatility periods (stopped by noise) and needlessly wide in quiet ones. Always scale stops to current ATR.

3. **Misreading ATR as directional.** ATR is always positive and says nothing about up or down. Rising ATR means "bigger bars," which can be a violent rally *or* a crash. Never infer trend direction from ATR alone.

4. **Lagging ATR after a vol collapse.** Because ATR is smoothed (Wilder 14), it adjusts slowly. Right after a squeeze fires, ATR still reflects the quiet period, so an ATR-based stop may be too tight for the first explosive bars. Some traders widen the multiplier immediately after a breakout.

5. **Donchian look-ahead illusion.** The upper Donchian line only updates *after* a new high prints. Backtests that mistakenly reference the *current* bar's high create look-ahead bias and overstate results. Enter on the *close* beyond the *prior* bar's channel.

6. **Over-tight Keltner multiplier.** A multiplier of 1 produces constant band touches and false trend signals. Keep m around 2 for daily trend detection.

7. **Ignoring that all three are lagging.** ATR, Keltner, and Donchian are built from past bars. They excel at *confirming* and *managing* trends, not predicting reversals. Use them for what they are — risk and continuation tools — not as leading reversal signals.

## Interview-ready summary

"These three tools describe *range*, not direction. **ATR** — Average True Range — is Wilder's 14-period smoothed average of the true range, where true range is the max of high-low, high-minus-prior-close, and low-minus-prior-close, so it captures gaps. ATR is the professional's unit of risk: I size positions and set stops as a multiple of ATR — typically 2 to 3× — so a stop sits outside random noise but not absurdly far, and every trade risks the same rupees regardless of whether it's Nifty at 180-point ATR or Bank Nifty at 700. **Keltner Channels** wrap an EMA(20) in bands at 2× ATR; because they're ATR-based they're smoother than Bollinger and hug trends well — a firm close outside the channel flags a trend day, and when Bollinger Bands contract inside the Keltner Channels you get the classic squeeze. **Donchian Channels** plot the highest high and lowest low of the last N bars — a close above the 20-day upper is by definition a new 20-day high, the purest breakout signal, and the basis of the Turtle system: enter on the 20-day breakout, stop at 2×ATR, exit on the 10-day opposite channel. The weakness is whipsaw in ranges, so I filter with volume, the higher-timeframe trend, and on Indian F&O, the option chain and IV — a Donchian breakout with cheap IV and a break through the call wall is a high-value long-volatility trade. They're lagging tools: brilliant for entering and *managing* trends with objective risk, not for predicting tops. TA is probability and risk control, and this trio is the risk-control backbone."
