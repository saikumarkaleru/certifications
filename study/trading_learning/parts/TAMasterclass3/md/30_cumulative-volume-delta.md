# Cumulative Volume Delta

Cumulative Volume Delta (CVD) is one of those tools that feels like a superpower the first time it works and a cruel joke the third time it doesn't. It sits at the boundary between price analysis and order-flow analysis. Where a normal volume bar tells you *how much* traded, CVD tries to tell you *who was the aggressor* — buyers lifting the offer or sellers hitting the bid — and then keeps a running total of that battle. For the Indian trader working Nifty and Bank Nifty futures on the NSE, CVD is genuinely useful, but it comes with a very specific set of traps that most YouTube explanations gloss over. This chapter treats it honestly.

## What it is and the logic

Every trade in a continuous auction market happens because one side crossed the spread. There is a resting bid and a resting offer. If an aggressive buyer accepts the offer, that trade is classified as a **buy** (or "up-tick" / "market buy" / "lift"). If an aggressive seller accepts the bid, it is a **sell** ("hit"). Volume Delta for a period is simply:

```
Delta = (volume traded at the offer)  −  (volume traded at the bid)
```

A single bar's delta can be +8,400 contracts (buyers were more aggressive) or −12,100 (sellers dominated). **Cumulative** Volume Delta just adds each bar's delta to a running sum across the session (or across a chosen window), producing a line that meanders up and down like a second price chart:

```
CVD(t) = CVD(t−1) + Delta(t)
```

The core logic is this: price is the *result* of the auction, but delta is the *effort* behind it. When price and cumulative effort agree, the move is "healthy." When they disagree — price making a new high while CVD makes a lower high — you have a **divergence**, a hint that the move is being driven by passive absorption or exhausted aggression rather than genuine demand. That divergence is the single most-traded CVD signal, and also the single most misused.

The philosophical anchor is auction market theory. Aggressive orders move price; passive orders (limit orders sitting in the book) provide the liquidity that *absorbs* aggression. CVD is an attempt to measure the aggressive side. Crucially it says nothing directly about the passive side — a point we return to repeatedly, because that omission is where the tool lies to you.

## Construction, rules and settings

### The classification problem (India-specific)

Here is the uncomfortable truth. To compute delta *properly* you need **tick-by-tick trade data with the bid/ask context at the moment of each trade** — true "aggressor flags." Exchanges like the CME disseminate this cleanly. On NSE, retail feeds and most charting platforms (TradingView, and many broker terminals) **do not** give you a reliable aggressor flag. So platforms *approximate* delta using one of these rules:

| Method | Rule | Quality |
|---|---|---|
| Tick-rule (up/down tick) | If trade price > previous, count as buy; if <, sell; if equal, carry prior sign | Crude, biased in fast moves |
| Bid/Ask assignment | Trade at or above ask = buy; at or below bid = sell | Good — but needs quote data |
| Volume split on 1-tick bars | Distribute intrabar volume by close position | Very crude estimation |

On TradingView's built-in "Cumulative Volume Delta" indicator for NSE symbols, the delta is estimated from **lower-timeframe candles** (it drills into, say, 1-second or 1-minute bars and assigns their volume as buy/sell based on whether that sub-candle closed up or down). This is the tick-rule in disguise. It is *directionally* useful but it is an estimate, not the truth. Real bid/ask CVD requires a genuine order-flow feed — GoCharting, Quantower with a suitable data adapter, or a broker's tick API. **Always know which one your chart is showing you.** A trader who believes an estimated CVD is a true footprint delta will eventually get badly hurt.

### Settings that matter

- **Anchor / reset point.** Intraday, most Indian futures traders reset CVD at the 09:15 open so the session starts at zero. This makes the day's accumulated pressure readable. Some anchor to the prior day's close or use a rolling lookback. For swing work you may run CVD un-reset across days, but beware: index futures roll over on expiry (last Thursday, now often weekly), and volume shifts to the next contract, corrupting a multi-day cumulative line unless you stitch continuous contracts.
- **Timeframe of the delta bars.** Finer sub-bars = more faithful estimate but noisier. For Nifty futures a 1-minute chart with delta estimated from 1-second sub-bars is a reasonable balance.
- **Instrument choice.** Compute CVD on the **futures** (NIFTY FUT, BANKNIFTY FUT), never on the spot index — the index has no traded volume of its own; it is a calculated number. This is the number-one beginner error in Indian CVD.

## Worked India example (levels and ₹)

Take a Bank Nifty futures session. Bank Nifty is trading around **48,200** at 09:15. Lot size 15, so one point on one lot is ₹15; a 100-point swing on a single lot is ₹1,500, and desk traders often carry 5–20 lots.

**Scene:** From 09:15 to 10:30 Bank Nifty grinds up from 48,200 to 48,520. CVD (reset at open) climbs steadily to **+42,000** contracts. Price up, effort up — clean trend. A pullback to 48,440 sees CVD dip only to +38,000. Buyers still net-aggressive. You are with the trend.

**The divergence:** By 13:15 price pushes to a fresh session high of **48,600**. But CVD, instead of exceeding its earlier +42,000 peak, tops out at **+31,000** and rolls over. Price = higher high; CVD = lower high. This is a **bearish CVD divergence**. Interpretation: the marginal new highs are being made on *weaker* net buying aggression — likely passive sellers are absorbing the lifts, or the aggressive buyers are exhausted and price is being levitated by thin liquidity.

**What actually happened (two possibilities, both real):**
1. Genuine distribution — big passive sellers parked offers at 48,600, soaked up the buying, and price collapsed to 48,300 by 14:30. The divergence "worked." A short from ~48,590 with a stop at 48,650 (−60 pts = −₹900/lot) targeting 48,350 (+240 pts = +₹3,600/lot) is a 4:1 winner.
2. The divergence was noise — a few large limit-buy orders (which add *zero* to delta because they're passive) quietly built a position, price broke 48,600 decisively and ran to 48,900. Your short stopped out.

The honest lesson: the *same chart pattern* produced both outcomes on different days. CVD divergence is a **conditional probability enhancer**, not a signal. You trade it only with location and confirmation, never alone.

## How to trade it

### Setup A — Trend confirmation / continuation

- **Context:** established intraday trend, price pulling back to a value area or moving-average.
- **Signal:** on the pullback, CVD holds well above its prior swing low (in an uptrend) — aggression is *not* leaving.
- **Entry:** on the resumption candle at the pullback low, e.g. Nifty FUT bounces off 24,450 VWAP with CVD flat-to-rising.
- **Stop:** below the pullback swing low (below 24,435).
- **Target:** prior high / measured move / 2R.
- This is the *higher-probability* use of CVD and gets far less attention than divergence because it's less glamorous.

### Setup B — Absorption reversal (divergence at a level)

- **Context:** price at a *pre-identified* level — prior day high/low, PDH/PDL, a big option strike, VWAP band edge.
- **Signal:** price makes a marginal new extreme; CVD refuses to confirm (lower high / higher low). Ideally you also see **delta flipping** on the reversal bar.
- **Entry:** on the reversal candle *back inside* the level, not on the divergence itself.
- **Stop:** just beyond the extreme (tight, because if it's real, price shouldn't revisit the high).
- **Target:** back to VWAP / value-area low / opposite band.
- **Management:** scale out half at 1.5R, trail the rest. Absorption trades either work quickly or they're wrong.

### Setup C — CVD breakout confirmation

- **Context:** range breakout, e.g. Nifty FUT breaking 24,600 range high.
- **Signal:** breakout accompanied by a **sharp CVD surge** (a near-vertical delta impulse). A breakout with *flat* CVD is suspect — price moved without net aggression, often a stop-run.
- **Entry:** on the retest of 24,600 holding, with CVD staying elevated.

## Confluence

CVD is a *supporting actor*. Pair it with:

- **VWAP and its bands** — divergence at the upper VWAP band is far more tradable than in the middle of a range.
- **Prior-day levels / PDH-PDL / initial balance** — location is everything.
- **Options open interest** — a bearish CVD divergence into a heavy Bank Nifty call OI wall (e.g. huge OI at 48,600 CE) is a *confluence*: passive sellers defending a strike is exactly what would flatten CVD while price stalls.
- **Footprint / delta-per-price** (next chapter) — CVD tells you the running total; the footprint tells you *where* in the candle the absorption happened.
- **Market breadth** on index trades — CVD on Nifty FUT diverging while advance-decline deteriorates is a stronger tell.

## Pitfalls

1. **Estimated vs true delta.** As covered, most NSE retail CVD is tick-rule estimation. Treat it as a proxy. Don't obsess over exact numbers; read the *shape* and *slope*.
2. **CVD says nothing about passive size.** A giant iceberg buyer (passive limit orders) can absorb sellers, flip price up, and *lower* CVD the whole way (because the aggressors were sellers). You'd see a "bullish price with falling CVD" and call it bearish divergence — and be dead wrong. This is the tool's fundamental blind spot: it measures aggressors, not the resting liquidity that decides who wins.
3. **Divergence is not a timing signal.** Divergences can persist and extend. "Price can make higher highs on falling CVD" for a long time in a squeeze. Never short *because* of a divergence; short because of a *reversal at a level* that a divergence *supports*.
4. **Session resets and contract rolls.** A CVD line carried across an expiry roll is garbage. Reset intraday; stitch continuous contracts for multi-day.
5. **Comparing CVD across instruments/scales.** CVD's absolute value is arbitrary (depends on anchor). Only its *slope and swings relative to price* mean anything. Don't compare +40,000 on Bank Nifty to +40,000 on Nifty.
6. **Low-liquidity instruments.** CVD on an illiquid NSE midcap future or a far-month contract is noise — too few trades to classify meaningfully.
7. **Spot index CVD.** Meaningless. Repeat: use the future.
8. **Over-fitting reset points.** It's easy to slide the anchor until a divergence appears. That's curve-fitting your own chart. Fix your rules before the session.

## Interview-ready summary

Cumulative Volume Delta is the running sum of (aggressive-buy volume − aggressive-sell volume), designed to reveal the *effort* behind price versus the *result*. Its flagship signal is **divergence** — price making a new extreme while CVD fails to confirm, hinting at absorption or exhausted aggression. In Indian markets, compute it on **futures** (Nifty FUT, Bank Nifty FUT), reset intraday at 09:15, and know whether your platform gives **true bid/ask delta** or a **tick-rule estimate** (most retail feeds give the estimate). The tool's core weakness is that it measures only aggressors and is blind to passive resting liquidity, so a large hidden limit buyer can produce a *false* bearish divergence. Trade CVD as a **confirmation and confluence tool** — strongest for trend continuation on pullbacks and for absorption reversals *at pre-defined levels* with options-OI and VWAP confluence — never as a standalone signal. Entries go on the *reversal or resumption candle*, stops beyond the extreme, and you respect that the same divergence pattern historically produces both clean reversals and violent continuations. Honesty about that base rate is what separates a trader who uses CVD from one who is used by it.
