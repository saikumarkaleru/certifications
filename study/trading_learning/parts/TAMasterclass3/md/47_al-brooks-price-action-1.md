# Al Brooks Price Action I

Al Brooks is a former ophthalmologist turned full-time trader who spent decades reducing chart reading to its irreducible atoms: the individual bar, the two-bar relationship, and the way bars cluster into trends and trading ranges. His method has almost no indicators — no moving average clouds, no MACD, no oscillator confluence. Just bars, on a single time frame, read as a running argument between buyers and sellers. For an Indian trader accustomed to indicator-heavy TradingView layouts, Brooks feels alien at first and then, once it clicks, almost impossible to un-see. This chapter builds the vocabulary — the bar, the signal bar, the trend bar versus doji, the gap, the trend from the open — and the reading discipline. Chapter II builds the trade: with-trend entries, the always-in concept, and the specific setups (H1/H2, L1/L2, wedges, final flags) that turn reading into rupees.

This is deliberately new territory relative to Volumes I and II. We are not re-teaching "what a hammer is." We are teaching how Brooks reads *every* bar as it closes, in real time, on a 5-minute Nifty or Bank Nifty chart, without waiting for a named pattern to complete.

## What it is and the logic

Brooks' core claim is that a bar chart is a complete record of an auction, and that price action alone — the sequence of highs, lows, opens, and closes — contains everything an indicator could tell you, but sooner. An indicator is a lagging transformation of price; the price already moved before the indicator confirmed. If you can read the bars, you front-run your own indicators.

The deeper logic is probabilistic. Brooks insists that at any moment the market is doing one of exactly three things: trending up, trending down, or in a trading range (which he treats as the default — markets are in some form of range perhaps 80% of the time on intraday charts). Every bar is a data point that shifts the probability of "always-in-long" versus "always-in-short." You are never certain; you are continuously updating odds. A strong bull trend bar closing on its high shifts probability toward more buying; a bull bar with a big tail on top says buyers pushed up but sellers sold the high, weakening the case.

Crucially, Brooks argues the market seeks a price where it can transact the maximum volume — an equilibrium — and that trends are simply the market moving *from* one area of agreement *to* another. A breakout is the market voting that the old range no longer represents fair value. Most breakouts fail because the old value was, in fact, fair; the minority that succeed are what trends are made of. This "breakouts usually fail, but the ones that don't run far" asymmetry underlies almost every Brooks setup.

For Indian markets this matters because Nifty and Bank Nifty spend enormous amounts of intraday time in tight ranges (the classic 10:30 a.m. to 2:00 p.m. "lunch drift"), punctuated by sharp expansions around the 9:15 open, RBI/Fed news, expiry-day OI unwinds, and the 2:30–3:15 closing push. Reading bars keeps you honest about which regime you are in.

## Construction: the vocabulary of the bar

Brooks assigns meaning to each bar's shape. Learn this table cold; it is the alphabet.

| Bar type | Definition | Message |
|---|---|---|
| **Trend bar (bull)** | Close well above open; small or no tail on top; body > tails | Buyers dominant this bar; urgency |
| **Trend bar (bear)** | Close well below open; small tail on bottom | Sellers dominant; urgency |
| **Doji** | Open ≈ close; small body relative to range | Balance/indecision; a one-bar trading range |
| **Bull trend bar with top tail** | Bull body but prominent upper wick | Buyers pushed, sellers pushed back; weaker |
| **Signal bar** | The bar *before* your entry bar; its extreme defines the trigger | The setup |
| **Entry bar** | The bar on which a stop order at the signal bar's extreme is triggered | The trigger fires |
| **Inside bar (ii)** | High lower than prior high AND low higher than prior low | Contraction; a mini range; breakout mode |
| **Outside bar (oo)** | High above prior high AND low below prior low | Both sides trapped; usually noise on 5-min |
| **Reversal bar** | Trend bar in the opposite direction with a tail on the "trend" side, at the end of a move | Potential exhaustion signal |

Two structural concepts sit on top of the single bar.

**Gaps.** Brooks reads three kinds. A *bar gap* is when a bar's low is above the prior bar's high (a bull gap) — rare intraday but a strong sign of urgency. A *measuring gap* in the middle of a trend projects a target (the move often doubles from the gap). A *gap in the moving average* — Brooks does keep a single 20-period EMA as a reference, not a signal — occurs when bars trade entirely above or below the EMA, marking a strong trend.

**Signal bar quality.** A good signal bar for a with-trend entry has: a body in the trend direction, a tail on the *entry side* (a bull signal bar ideally has a small tail below, showing buyers stepped in), close near the extreme, and reasonable size relative to recent bars. A tiny doji signal bar or a signal bar with a huge opposing tail is low quality — Brooks would either skip it or wait for a second signal (the "second entry" idea, central to Chapter II's H2/L2).

### The 20-EMA as the only tool

Brooks uses a 20-bar exponential moving average purely as a visual anchor for trend strength, never as a crossover signal:

```
EMA_t = Close_t * (2/21) + EMA_{t-1} * (1 - 2/21)
```

In a strong bull trend, most bar *lows* stay above the EMA and pullbacks touch it and bounce. When price closes on the far side of the EMA and stays there, the always-in flips. On a 5-minute Bank Nifty chart, the 20-EMA is the single line most institutional intraday desks and retail scalpers both watch, so it self-fulfills.

## The trend-from-the-open and the first hour

Brooks devotes enormous attention to the opening range because the first hour sets the day's character. He classifies the day type early:

- **Trend from the open (TFTO):** The first bar or two are strong trend bars in one direction, price never looks back, and pullbacks are shallow (bull pullbacks hold above the EMA). Roughly the strongest and rarest day.
- **Trend from the open that becomes a trading range:** Common — a sharp move, then chop.
- **Trading range day:** Open near the middle, price oscillates between a high and low established in the first hour.
- **Reversal day:** Trend one way into mid-morning, then a large opposite move.

The practical rule: in the first hour, be willing to trade *both* directions with-trend swings and fade extremes at the developing range edges, because you do not yet know the day type. By the second hour, commit to the emerging structure.

## Worked India example: Nifty 5-minute, a trend-from-the-open morning

Consider a Nifty 50 futures session. Suppose Nifty settled the prior day at 24,180 and opens at 24,240 — a 60-point gap up, likely on positive SGX/GIFT Nifty cues.

- **09:15 bar:** Opens 24,240, runs to 24,272, closes 24,268 — a strong bull trend bar, close on the high, tiny tails. Message: buyers urgent, gap holding.
- **09:20 bar:** A smaller bull bar, 24,268 to 24,281, closes 24,277. Higher high, higher low. The EMA is far below at ~24,200.
- **09:25 bar:** A doji-ish pullback bar, dips to 24,265, closes 24,271. This is the *signal bar* for a with-trend long — Brooks calls the first pullback in a new bull trend an **H1** (high 1, the first bar whose high gets exceeded after a one-bar pullback).
- **09:30 bar:** Trades above 24,281 (the signal bar high). A buy-stop one tick above the H1 signal bar high fills the long.

Entry logic, in Brooks' terms: a gap-up followed by two strong bull bars means the always-in is long. The first shallow pullback that holds well above the EMA is a high-probability H1 buy. Stop goes below the signal bar low (24,265) — about a 16-point risk. Target: at minimum a measured move (the initial 09:15–09:20 leg was ~40 points, so project ~40 points, to ~24,320), with a runner if the day stays trend-from-the-open.

If instead the 09:25 pullback had been a *bear trend bar* closing below the EMA, Brooks would downgrade the setup: the buyers lost control, and the day is likely to become a trading range rather than a trend. He would wait for a **second** signal (an H2) before buying — the market frequently needs two attempts.

Now the same open, different sequel: suppose after the gap up, the 09:20 and 09:25 bars are both bear trend bars closing back below 24,240, filling the gap. This is a **failed breakout / gap reversal** — the gap up was rejected. Brooks would flip to always-in-short and look to sell the first pullback (an L1/L2). Bank Nifty especially loves this "gap-and-fail" on expiry Thursdays when option writers defend a strike.

## How to trade it: reading discipline before setups

Chapter II covers the exact setups. Here the discipline is *reading*, and the rules are:

1. **Trade with the always-in direction.** Ask after every bar closes: if I had to be long or short right now with no exit, which would I choose? That is the always-in. With-trend trades win more often.
2. **Demand a signal bar.** Never enter on a hunch; enter on a stop order beyond a defined signal bar. This forces the market to prove the move by trading through your level.
3. **Grade the context, then the signal.** A perfect signal bar in a bad location (e.g., buying into strong resistance in a bear trend) is a bad trade. Context (trend vs range, EMA relationship, prior structure) outranks the pretty bar.
4. **Respect the two-legged pullback.** Pullbacks in trends usually have two legs (an A-B-C shape). The second leg often ends at or just past the EMA and is the higher-probability entry — this is why H2/L2 beat H1/L1 in most conditions.
5. **In a trading range, do the opposite of breakouts.** Sell rallies to the top, buy dips to the bottom, and fade the first breakout of either edge — because most range breakouts fail.

## Confluence: what strengthens a Brooks read

Brooks is anti-indicator but not anti-confluence; his confluence is *structural*:

- **EMA agreement:** Longs are stronger when the pullback holds above a rising 20-EMA.
- **Measured moves and magnets:** Prior-day high/low, the day's opening range, round numbers (Nifty 24,000/24,500; Bank Nifty 52,000), and gap edges act as targets and stalls.
- **Trend-line and trend-channel-line touches:** A pullback that touches a rising trendline and prints a bull signal bar is stronger.
- **F&O levels:** The max-pain strike, highest-OI call (resistance) and put (support) strikes, and VWAP behave as Brooks "magnets" — a with-trend signal bar right at a high-OI put strike (support) is high-quality confluence for a long. This is the natural India-first bridge: Brooks structure plus option-chain levels.
- **Second-attempt logic:** A second signal at the same level (double bottom bull flag, an L2 at resistance) is worth more than a first.

## Pitfalls

- **Over-trading the range as if it were a trend.** Beginners buy every H1 in what is actually a tight range and get chopped. If bars are overlapping heavily and the EMA is flat and being crossed repeatedly, you are in a range — fade edges, do not chase breakouts.
- **Taking low-quality signal bars.** A doji signal bar, or a signal bar with a large tail on the wrong side, has a low win rate. Brooks would rather skip it. Discipline to *not* trade is half the method.
- **Ignoring the always-in flip.** Holding a long after two strong bear trend bars have flipped the always-in to short is how small losses become large ones.
- **Forcing setups in the lunch chop.** On Nifty, 11:30 a.m.–1:30 p.m. is often a barbwire range (tight overlapping bars around the EMA). Brooks' explicit advice: reduce size or stand aside in barbwire; the reward-to-risk collapses.
- **Confusing a strong trend bar mid-range with a breakout.** One big bar inside a range is usually a trap, not a trend. Wait for follow-through — a second trend bar in the same direction.
- **Applying 5-minute reading to a 1-minute chart.** The 1-minute has far more noise; Brooks' probabilities were built primarily on the 5-minute. Indian retail traders drop to 1-minute for "precision" and get whipsawed.

## Interview-ready summary

Al Brooks reads a bar chart as a continuous auction, using no indicators beyond a single 20-EMA reference. The market is always in one of three states — bull trend, bear trend, or (most often) trading range — and every bar updates the probability of being "always-in-long" versus "always-in-short." Trades are taken with-trend, on stop orders beyond a graded *signal bar*, with the *entry bar* triggering the fill and the stop placed beyond the signal bar's opposite extreme. Context (trend vs range, EMA relationship, structure) always outranks the individual bar's prettiness. The governing asymmetry is that most breakouts fail but the few that succeed run far, so in ranges you fade the edges and in trends you buy pullbacks — ideally the second leg (H2/L2). For Nifty and Bank Nifty, the method pairs naturally with opening-range analysis, VWAP, and high-OI option strikes as structural magnets. Chapter I is the alphabet — the bar vocabulary, the always-in concept, the trend-from-the-open day classification, and the reading discipline. Chapter II turns that reading into specific, tradable setups with entries, stops, targets, and management.
