# Andrews Pitchfork & Gann Tools

Most traders draw two things on a chart: horizontal support/resistance and diagonal trendlines. Andrews Pitchfork and the Gann family of tools are the next tier of *geometry* — they add slope-aware channels, time-based projections and angle analysis. They are simultaneously among the most powerful and the most abused instruments in technical analysis, because both reward disciplined anchoring and punish curve-fitting mercilessly. This chapter treats them honestly: what actually works, what is folklore, and how to use them on Nifty, Bank Nifty and NSE stocks in 2026 without deluding yourself.

## Part A — Andrews Pitchfork

### What it is & why it works

The Andrews Pitchfork (also called the median line study) was developed by Dr Alan Andrews. It is drawn from **three pivots**: a starting pivot P0 (the "handle" anchor) and two subsequent pivots P1 and P2 that define a swing. The tool draws:

- A **median line (ML)** from P0 through the midpoint of the P1–P2 segment.
- Two **outer tines** parallel to the median line, passing through P1 and P2 respectively.

The result looks like a three-pronged fork projected into the future. The core idea Andrews taught is a *statistical* one: price tends to return to the median line roughly 80% of the time after leaving a pivot. That number is not a law — it is Andrews' observation from decades of hand-charting — but the mechanism behind it is sound. The median line is effectively a **dynamic equilibrium/mean** of the swing, and the outer tines are one-standard-deviation-style channel boundaries built from real swing geometry rather than an arbitrary parallel-channel guess.

Why does it work at all? Because trending markets oscillate around a fair-value drift. The pitchfork encodes both the *drift* (slope of the median line) and the *dispersion* (width between the tines) from the market's own recent behaviour. When price reaches an outer tine and stalls, you are seeing the swing return to its statistical edge — a natural place for mean reversion. When price accelerates *through* a tine, the dispersion is expanding, which is information too.

### Mechanics, anchoring & settings

Anchoring is everything. Garbage pivots produce a garbage fork. Rules that keep you honest:

1. **P0, P1, P2 must be clean, obvious swing pivots** — points a second trader would also mark. If you have to squint, the fork is invalid.
2. For an **up-fork**: P0 = a swing low, P1 = the next swing high, P2 = the higher swing low. Median line then slopes up.
3. For a **down-fork**: P0 = a swing high, P1 = the next swing low, P2 = the lower swing high.
4. **Do not re-anchor** to make the fork "fit" recent price. If price has invalidated the fork, delete it and redraw from fresh pivots.

Two useful variants:

- **Schiff Pitchfork**: shifts P0 down (or up) to the midpoint between P0 and P1 vertically, reducing the exaggerated slope you sometimes get when P0 is a sharp spike. Use it when a V-shaped P0 gives an unrealistically steep median line.
- **Modified Schiff**: shifts P0 to the midpoint of P0–P1 in both price and time. This is the version many Indian intraday traders prefer on Bank Nifty because the index makes violent single-candle spikes that distort a raw pitchfork.

**Warning lines** are parallels drawn outside the tines at 1x, 1.5x and 2x the ML-to-tine distance. When price blows through the upper tine and reaches the first warning line, the trend is unusually strong; when it can't even reach the median line on a pullback, the trend is weakening — that "failure to reach the median line" is one of Andrews' most reliable signals and is called a **Median Line Failure**.

### Worked India example (levels & ₹)

Take a reconstructed Nifty daily swing (verify the exact prints on your chart — treat these as approximate):

- **P0** = swing low at 21,150
- **P1** = swing high at 22,800
- **P2** = higher swing low at 22,050

The midpoint of P1–P2 = (22,800 + 22,050)/2 = 22,425, at the time-midpoint of those two pivots. The **median line** is drawn from 21,150 through that 22,425 midpoint and extended forward — an up-sloping line. The **upper tine** runs parallel through P1 (22,800 level, sloping up), the **lower tine** parallel through P2 (22,050 level, sloping up).

Now the trade logic over the following weeks:

- Price rallies to 23,400, tags the **upper tine**, and stalls. This is your first mean-reversion short-scalp or, if you are long, your first profit-booking zone.
- Price pulls back and finds the **median line** near, say, 23,050 (the median line has risen with time). Andrews' 80% rule says this pullback-to-median is the highest-probability continuation buy in an uptrend.
- You go long at ~23,060 with a stop just below the median line at 22,960 (₹100 risk per Nifty unit; on one lot of 25 that is ₹2,500). Target = the upper tine again, projected to ~23,600 by that date — roughly a 1:5 reward:risk on the geometry.

If instead price *fails to reach the median line* on the pullback — turning back down at 23,250 while the median line sits at 23,050 — that Median Line Failure warns the uptrend is losing steam, and you would flip your bias toward a break of the lower tine.

### How to trade it (entry / stop / target)

| Element | Rule |
|---|---|
| **Primary entry** | Pullback into the **median line** in the direction of the fork's slope; enter on a reversal candle (hammer/engulfing) at the line |
| **Aggressive entry** | Tag of an **outer tine** against the trend, for a mean-reversion scalp back to the median line |
| **Stop** | ~0.3–0.5 ATR beyond the line being traded (median or tine); if the line is decisively broken and price closes through, the fork is invalid |
| **Target 1** | The median line (for tine-reversion trades) |
| **Target 2** | The opposite tine (for median-line continuation trades) |
| **Timeframe** | Works on any TF, but the pivots must be visible and clean; daily and 75-min charts on Indian indices are the sweet spot |
| **Regime** | Trending / channelling markets only. In a tight range the fork flattens and gives false parallels |

### Confluence (including OI)

A pitchfork line means far more when something else agrees with it:

- **Fibonacci**: if the median line intersects a 0.5/0.618 retracement of the same swing at the same price, that confluence zone is high-conviction.
- **Moving averages**: median line crossing the 20/50-EMA at the same level strengthens the signal.
- **Option OI (F&O)**: on Bank Nifty, if the upper tine sits at 52,000 and the option chain shows the heaviest **call OI** (max resistance) at the 52,000 strike, the tine and the OI wall reinforce each other — a genuine ceiling. If the lower tine aligns with the highest **put OI** strike, that's a floor. Watch for **OI unwinding** at those strikes as price approaches; call writers covering as price nears the tine tells you the wall may break.
- **Volume**: a median-line pullback on shrinking volume, then a bounce on expanding volume, is the textbook continuation.

### Pitfalls

- **Over-anchoring / redraw addiction.** The single biggest failure. If you keep dragging P0 to make the fork "look right," you are fitting noise. Commit to pivots and let the fork be wrong sometimes.
- **Spike pivots.** A P0 on a news-spike wick gives a distorted slope. Use Schiff/Modified Schiff instead.
- **Range markets.** Forks are trend tools. In consolidation they produce near-horizontal, meaningless tines.
- **Confirmation bias on the 80% rule.** You will remember the tags and forget the misses. Journal every fork trade with its outcome; your realised hit-rate will be lower than 80%, probably 55–65% on median-line pullbacks, which is still tradeable with good R:R.
- **Too many forks.** One clean fork per instrument per timeframe. A chart with four overlapping pitchforks is a Rorschach test, not analysis.

### Interview-ready summary

*The Andrews Pitchfork is a three-pivot median-line channel. The median line acts as a dynamic mean that price returns to ~80% of the time (per Andrews' observation), and the outer tines act as statistical channel edges built from the swing's own geometry. Best trade: buy the pullback to the median line in a trend; the highest-value warning is a Median Line Failure, where price can't reach the median on a pullback, signalling trend exhaustion. Anchor to clean pivots, never re-anchor to fit price, and confirm with Fibonacci or option OI walls.*

## Part B — Gann Tools

### What they are & the honest verdict

W.D. Gann (1878–1955) was a trader whose methods blended price-time geometry, angles, and astrology/numerology. The mystical claims (planetary influences, "the market is mathematical because the universe is") are unfalsifiable and should be discarded. But a *subset* of Gann's toolkit survives on its practical merit, because it enforces a genuinely useful idea most traders ignore: **price and time should be analysed on the same footing.**

The tools worth knowing:

1. **Gann Angles / Gann Fans** (1x1, 2x1, 1x2, etc.)
2. **Gann Squares** (Square of 9, Square of 144)
3. **Gann Time Cycles** (anniversary dates, 90/144/180-day counts)

Approach all of them as *structured hypothesis generators*, not prophecy. Where they place a level that coincides with real support/resistance, trade the confluence; where they don't, ignore them.

### Gann Angles & the 1x1 line

A Gann angle is a trendline drawn at a fixed **price-per-unit-of-time** slope. The master angle is the **1x1** (also "45-degree line"), meaning one unit of price per one unit of time. The critical, endlessly-misunderstood point: **a 1x1 line is only 45 degrees if you have correctly scaled the chart** so that one unit of price occupies the same physical distance as one unit of time. This requires setting a Gann scale.

For Nifty, "one unit of price" is not one point — Nifty moves in thousands. You must choose a scale, e.g. **100 points per day** for the 1x1. Then:

- **1x1**: 100 points/day — the trend's spine. Price above it = bullish control; below = bearish control.
- **2x1**: 200 points/day — a steeper line; too fast to sustain, breaks flag exhaustion.
- **1x2**: 50 points/day — a shallower line; the fallback support if 1x1 breaks.

The Gann Fan draws all these from a single significant pivot. The trading idea: when price breaks below the 1x1, it typically falls to the next-shallower angle (1x2), then 1x3, in a stair-step. Each angle is dynamic support/resistance.

**Worked example (reconstructed, verify on chart):** Anchor a Gann Fan at a Bank Nifty swing low of 48,000 with a scale of 200 points/day.

- The **1x1** line rises 200/day: after 20 trading days it sits at 48,000 + 4,000 = 52,000.
- Price trends above the 1x1 — bullish. On a pullback it holds the 1x1 at ~52,000: long entry, stop below at ~51,700 (300 pts; one lot of 35 = ₹10,500 risk), target the 2x1 line.
- Two weeks later price closes below the 1x1. Expect a slide to the **1x2** (100/day) line, which by then sits near 51,000 — that becomes the next support and profit target for shorts.

The honest caveat: the scale (200 points/day) is a *choice*, and different scales give different fans. Gann angles are most defensible when the chosen scale makes the 1x1 line repeatedly act as real support/resistance historically — i.e., you calibrate the scale to the instrument, then use it consistently. If you have to change the scale every month, you're curve-fitting.

### Gann Square of 9

The Square of 9 is a spiral of numbers arranged so that consecutive perfect squares (1, 4, 9, 16, 25 …) fall on the same diagonal. Traders use it to compute **support/resistance levels and time turning points** by taking the square root of a price, adding a fixed increment, and squaring back.

The mechanics for a price level:

1. Take a significant price, e.g. Nifty pivot **22,500**.
2. Square root: √22,500 = **150.00**.
3. Add increments corresponding to angular moves on the spiral. A **90-degree** move = +0.5 to the root; **180-degree** = +1.0; **360-degree** (full rotation) = +2.0.
4. Square the result to get the projected level.

So from 22,500:
- +0.5 → 150.5² = **22,650** (next 90-degree resistance)
- +1.0 → 151² = **22,801** (180-degree)
- +2.0 → 152² = **23,104** (360-degree / one full rotation)

And downside:
- −0.5 → 149.5² = **22,350**
- −1.0 → 149² = **22,201**

Notice these are just **≈150-point and ≈300-point steps** near this price — which is *why* the Square of 9 sometimes "works": it generates a grid of roughly equidistant levels that overlaps with round numbers and prior pivots. The tighter increments (¼, ⅛ rotations) create intraday levels. Many Indian intraday tools (the "Gann Square of 9 calculator" widely used for Nifty/Bank Nifty scalping) automate exactly this: feed the opening price, get buy-above and sell-below levels for the day.

**Practical use, stated honestly:** treat Square-of-9 outputs as *candidate* levels. Where a Square-of-9 resistance at 22,650 coincides with the day's VWAP, a prior high, and heavy call OI at 22,650 — that's a strong level worth trading. Where it stands alone with no other confluence, don't bet on it. The calculator's edge is *psychological structure*, not cosmic mathematics.

### Gann Time Cycles

Gann's most genuinely underused contribution is **time symmetry**. The idea: markets turn on anniversaries and on counts of significant numbers — **90, 144, 180, 270, 360 calendar days**, and the **anniversary** of major highs/lows. A major top or bottom often produces a reaction a "Gann count" of days later.

For Indian indices, practical application:

- Mark the date of a major Nifty swing high/low. Project **forward 90, 144 and 180 calendar days.** Watch those windows (±3 days) for a change in trend. You are not predicting direction — you are flagging *when* to be alert for a turn.
- Combine with **budget-day, RBI-policy and expiry cycles**, which impose India-specific time structure. A Gann 90-day count that lands in the same week as an RBI policy or the monthly F&O expiry is a higher-alert window.

Example (reconstructed): if Nifty made a significant low on 1 March, the +144-day window falls around 23 July. If price is also stretched and momentum is diverging into that window, treat late July as a probable turn zone — but only act on an actual price signal (a reversal candle, a break of the pitchfork median line, an MACD cross), never on the date alone.

### How to trade Gann tools (entry / stop / target)

| Element | Rule |
|---|---|
| **Angle entry** | Buy the hold/reclaim of the **1x1** line in an uptrend; sell the loss of it |
| **Square-of-9 entry** | Trade a Square-of-9 level **only with confluence** (VWAP, prior pivot, OI wall, round number) |
| **Time-cycle use** | Flag 90/144/180-day windows as *alert zones*; require a separate price trigger to act |
| **Stop** | Beyond the angle/level being traded, ~0.3–0.5 ATR |
| **Target** | The next Gann angle (fan) or next Square-of-9 rotation level |
| **Regime** | Angles: trends. Square-of-9: intraday grids. Time cycles: any, as a filter |

### Confluence (including OI)

Gann tools are *most useful as a confluence layer* over conventional analysis:

- **Square-of-9 level + option OI**: a 22,650 Square-of-9 resistance sitting on the max-call-OI strike is a real ceiling; fade it or take profit there.
- **1x1 angle + moving average**: when the Gann 1x1 and the 50-EMA converge, the combined support is stronger than either alone.
- **Time cycle + Fibonacci price target**: if the 144-day time window coincides with price reaching a 1.618 Fibonacci extension, the price-and-time symmetry is Gann's whole thesis in one setup — that is the highest-conviction Gann signal.
- **Volume/breadth**: a time-window turn confirmed by breadth divergence (advance-decline rolling over) is more trustworthy.

### Pitfalls

- **Mysticism.** Ignore all astrological/planetary claims. There is no verified mechanism and the evidence is anecdotal.
- **Scale-fitting.** The 1x1 line depends entirely on the price/time scale you pick. Calibrate once per instrument and freeze it, or you are just drawing lines that fit the past.
- **Level worship.** Square-of-9 levels are candidates, not certainties. Standalone, their hit-rate is barely better than random round numbers. Their value is confluence.
- **Date determinism.** A Gann time window tells you *when to watch*, never *what will happen*. Trading a date with no price confirmation is gambling.
- **Tool overload.** Running a pitchfork, a Gann fan, a Square-of-9 grid and three Fibonacci sets simultaneously produces a chart where *something* is always near price — the illusion of precision. Pick the one or two that show real, repeatable confluence for your instrument.

### Interview-ready summary

*Gann tools analyse price and time on equal footing. The 1x1 Gann angle is the trend's spine — dynamic support/resistance whose validity depends on a correctly calibrated price/time scale. The Square of 9 generates a grid of support/resistance by adding rotational increments to the square root of a price (√22,500=150; +0.5 → 22,650 as 90-degree resistance); it is useful only as a confluence layer, not a standalone oracle. Gann time cycles (90/144/180 days, anniversaries) flag alert windows for trend changes but require a separate price trigger. Discard all the astrological mysticism; keep the disciplined price-time geometry.*

## Combining Andrews & Gann — the practical synthesis

The two families answer different questions. **Andrews Pitchfork answers "where is fair value and the channel edge right now?"** — it is a *price-structure* tool. **Gann tools answer "at what time and at what mathematically-derived level should I expect a turn?"** — they add a *time* and *grid* dimension.

A clean combined workflow on, say, Nifty daily:

1. Draw one pitchfork from the current dominant swing. Note the median line and tines.
2. Overlay a Square-of-9 grid from the most recent major pivot. Note where its levels coincide with the pitchfork tines.
3. Mark the 90/144-day Gann time windows from the last major high/low.
4. **Trade only where they stack**: e.g., price pulls back to the pitchfork median line (23,050), that level equals a Square-of-9 rotation level, heavy put OI sits one strike below, *and* you're three days inside a 144-day time window. That four-way confluence is a genuinely high-probability long — take it with a tight stop below the median line and target the upper tine.

The discipline that separates a professional from a chartist-mystic is the willingness to say "no confluence today, no trade." Both Andrews and Gann reward the trader who uses them as *filters that mostly say no*, and punish the one who uses them to justify a trade they already wanted to take. Anchor honestly, calibrate once, demand confluence, and both toolsets earn their place on an Indian-market chart.
