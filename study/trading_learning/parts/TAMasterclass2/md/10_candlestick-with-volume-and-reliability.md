# Candlesticks with Volume & Pattern Reliability Statistics

Most traders learn candlesticks as a picture book: "this shape means reversal, that shape means continuation." That is exactly why most traders lose money with candlesticks. A candlestick is not a picture — it is a **compressed record of an auction**, and the single most important number that never appears in the shape itself is **how many contracts changed hands to draw it**. A bullish engulfing candle on 3x average volume at a demand zone is a different animal from the identical shape printed on a dead Tuesday afternoon with volume 40% below average. One is a footprint of institutions; the other is noise dressed up as a signal.

This chapter does two things Volume I did not. First, it welds **volume onto every major candlestick** — the "why does this pattern work" is almost always a volume story, and reading them together turns a coin-flip into an edge. Second, it puts honest **reliability statistics** on the table. Candlestick research (Bulkowski's decades of hand-tabulated US data, plus what backtesting on Nifty/Bank Nifty confirms) shows that most single candles resolve barely better than a coin toss on their own, and that the *volume filter and the location filter* are what push a 52% pattern to a 62-65% pattern. Numbers matter here because they set expectations: candlesticks are a **timing and confirmation tool**, not a standalone system.

## Why volume is the missing half of every candle

Price tells you *where* the auction settled. Volume tells you *how much conviction* was behind that settlement. A candle is the net result of buyers and sellers; volume is the gross activity that produced it. The interpretive logic rests on three ideas:

**1. Effort vs. result (Wyckoff's core).** A large-range candle that closes strongly on huge volume is "effort rewarded" — demand overwhelmed supply. But a large-range up candle on *even larger* volume that closes in the *middle* of its range is "effort with poor result" — a lot of buying was absorbed by a wall of sellers. Same green candle, opposite meaning, and only volume tells you which.

**2. Confirmation of exhaustion.** Reversal candles work best when they mark a *transfer of ownership* from trapped weak hands to strong hands. That transfer requires volume. A hammer at the bottom of a fall on climactic volume means panic sellers finally found aggressive buyers. A hammer on thin volume means the sellers simply took a lunch break — nobody was transferred anything.

**3. Validation of breakouts.** A bullish marubozu or a gap that opens a new leg is only trustworthy if participation expands. Breakouts on shrinking volume are the raw material of bull and bear traps.

The practical rule I use on every timeframe: **judge the candle's volume relative to a 20-period average of volume.** On TradingView, drop the default Volume indicator and add a 20-SMA of volume onto it (the built-in has this option). Then classify each signal bar as *low* (below the average), *normal* (roughly 1x), *high* (1.5-2x), or *climactic* (2x+). That single classification changes the trade far more than the candle's name.

## The volume signatures of the major candles

**Hammer / Hanging Man.** Shape is identical: small body, long lower wick, little/no upper wick. Location and volume separate them. A hammer at the end of a downtrend is a *bottoming* signal; a hanging man after an uptrend is a *topping* signal. In both cases you want the wick to have been *bought/sold on high volume* — the long wick means price probed deep and got violently rejected, and high volume means the rejection had size. Bulkowski's data is humbling: the hammer as a pure reversal succeeds only about **60%** of the time in the "expected" direction, and the hanging man is close to a coin flip (~59% but often continues rather than reverses). Volume tightens both. On Reliance, a hammer at a rising trendline with volume 1.8x the 20-day average and a close back above the prior day's midpoint is worth acting on; the same hammer on 0.7x volume is a "watch, don't touch."

**Bullish / Bearish Engulfing.** The second candle's body swallows the first. The volume story is the whole story: you want the *engulfing* (second) candle to print on clearly higher volume than the engulfed (first) candle. That means the new direction attracted more participation than the old direction — a genuine shift. Engulfing patterns are among the *better* single candles: bullish engulfing reverses in the expected direction roughly **63%** of the time in backtests, and adding the volume-expansion filter pushes practical hit-rate into the mid-60s while cutting the ugliest failures. On Bank Nifty, a bullish engulfing at a support level where the up-candle traded ~2x the down-candle's volume is a high-quality long trigger.

**Doji.** A doji is *indecision made visible* — open and close nearly equal. But a doji on climactic volume is far more meaningful than a doji on thin volume. High-volume doji at the end of a strong trend = a huge fight where neither side won = potential exhaustion. Low-volume doji mid-range = the market simply went to sleep. The long-legged doji and the dragonfly/gravestone variants carry the same rule: *the wick tells you where the fight happened, volume tells you how big the fight was.* Dojis on their own are among the *least* reliable single candles (barely above 50%); they are best used as *alerts that demand a confirmation candle*, never as standalone triggers.

**Shooting Star / Inverted Hammer.** Long upper wick, small body near the low. A shooting star tops a rally; an inverted hammer bottoms a decline (with confirmation). The upper wick should be a *high-volume rejection* of higher prices. A shooting star on Nifty at an all-time-high extension, printing 1.7x average volume with the close back below the prior candle's body, is a classic distribution footprint.

**Marubozu.** A full-bodied candle with no or tiny wicks — pure directional conviction. Here you *want* high volume; a marubozu is only as trustworthy as the participation behind it. A bullish marubozu that breaks a consolidation on 2x volume is a momentum-ignition bar. The same shape on average volume is often the *last* push before a stall.

**Three White Soldiers / Three Black Crows.** Three consecutive strong candles in one direction. The healthy version shows *steady or rising* volume across the three; a version where volume *fades* candle-by-candle warns that the move is running out of fuel even as price climbs — a classic pre-reversal tell.

## The Volume Spread Analysis lens (effort vs. result, formalised)

VSA, descended from Wyckoff and Tom Williams, is the discipline of reading each bar as **spread (range) + close position + volume**, always relative to recent bars. A few high-value VSA signals every Indian intraday trader should recognise:

- **No Demand bar:** a narrow up-bar closing in the middle/low on *below-average* volume after a rally. Buyers are absent; the path of least resistance is down. Extremely useful on 5-min Nifty for fading weak pushes.
- **No Supply bar:** the mirror — narrow down-bar on low volume in an uptrend. Sellers are absent; dips are likely to hold.
- **Stopping Volume / Selling Climax:** a wide-range down bar on *ultra-high* volume that closes off its low. This is smart money absorbing panic selling — a bottoming footprint. On Bank Nifty crash days this often prints on the 15-min chart right before the low.
- **Buying Climax / Upthrust:** a wide up-bar (or a spike-and-fail bar) on huge volume closing weak, at the top of a move — distribution. The classic bull-trap bar above a prior high that snaps back inside.

VSA's power is that it forces the effort-vs-result question on *every* bar, not just named patterns. That habit alone upgrades a discretionary trader.

## Worked India example — Bank Nifty, 15-minute reversal (approximate reconstruction)

*Levels below are an illustrative reconstruction to verify against your own charts.*

Picture Bank Nifty selling off through a morning session, sliding from ~48,600 toward a well-watched support shelf near **48,200** (a level that had held twice in the prior week). Into 48,200 the 15-min candles are wide and red, volume rising — sellers are aggressive. Then the key bar prints: a **wide-range candle that pierces to 48,150, then closes back up at 48,320**, a long lower wick, on volume roughly **2.3x the 20-bar average**. That is *stopping volume* — a selling climax where panic supply was absorbed.

The next 15-min bar is a **bullish engulfing** that swallows the prior small red body and closes at 48,410 on **1.9x** volume — participation expanded in the new direction. This is the trigger.

- **Entry:** long on the close of the engulfing bar, ~48,410, or on a micro-pullback to ~48,350.
- **Stop:** below the climax wick, ~48,120 (a break there says the absorption failed). Risk ~230-290 points — sizeable, so this is a small-size or options-defined trade.
- **Target 1:** the session's mean / VWAP, often ~48,650. **Target 2:** the prior swing high ~48,900.
- **Option-chain confluence:** if the **48,000 put** shows large and *rising* OI (a defended floor) while **48,500 calls** are being *unwound*, the auction and the positioning agree — the strongest configuration. Conversely, if 48,000 puts are being *shed* on this bounce, be sceptical; the floor may be moving.

Outcome in the reconstruction: Bank Nifty grinds to 48,650 into early afternoon (T1 hit, book half, trail the rest), then tags 48,880 late — a clean 2-3R trade. The *lesson*: the engulfing shape alone was ordinary; the **climax-volume bar into a known support + volume expansion on the trigger + agreeing OI** is what made it high-probability.

## The reliability statistics — what the data actually says

Now the honest part. Traders quote candlestick "success rates" as if they were laws of physics. They are not. Here is a grounded synthesis of what long-run pattern research (primarily Bulkowski's tabulations on thousands of US stock instances, corroborated directionally by backtests on Indian index data) tells us. Treat these as *ranges and tendencies*, not guarantees — hit-rates drift with market regime, timeframe, exit rule, and how you define "success."

| Candlestick pattern | Nature | Approx. "works as expected" rate (unfiltered) | With volume + location filter |
|---|---|---|---|
| Bullish Engulfing | Reversal (bottom) | ~63% | mid-60s%, fewer deep failures |
| Bearish Engulfing | Reversal (top) | ~60-62% | low-to-mid 60s% |
| Hammer | Reversal (bottom) | ~60% | ~63-65% |
| Hanging Man | Reversal (top) | ~55-59% (often continues) | modestly better; weak alone |
| Shooting Star | Reversal (top) | ~57-60% | low-60s% |
| Inverted Hammer | Reversal (bottom) | ~55-60% | needs confirmation |
| Morning Star | Reversal (bottom) | ~65-70% | among the best; strong |
| Evening Star | Reversal (top) | ~65-70% | among the best; strong |
| Piercing Line | Reversal (bottom) | ~55-64% | improves notably |
| Dark Cloud Cover | Reversal (top) | ~55-60% | improves notably |
| Three White Soldiers | Reversal/continuation | ~65-70%+ | strong with steady volume |
| Three Black Crows | Reversal (top) | ~65-70%+ | strong |
| Doji (single) | Indecision | ~50-53% | alert only, not a trigger |
| Bullish/Bearish Marubozu | Continuation | ~55-60% | needs volume to trust |
| Harami | Reversal | ~53-58% | weak; confirmation essential |

Four uncomfortable truths sit inside that table:

**1. Most single candles are barely edges.** A 55-60% raw hit-rate is *not* free money — with a poor risk-reward exit it loses. The three-candle patterns (morning/evening star, three soldiers/crows) are meaningfully more reliable than single candles precisely because they encode *more information* — a full sequence of the auction, not one snapshot.

**2. "Success rate" depends entirely on your exit definition.** Bulkowski measures success as price moving in the expected direction to a set threshold before a reversal. Change the target or stop and the number changes. A pattern that hits its expected move 65% of the time but only by a small amount is worthless if your stop is wide. **Reliability and reward-to-risk must be judged together.** A 55% pattern at 2.5R beats a 65% pattern at 0.8R.

**3. Location dominates the shape.** The same candle is worth double at a fresh support/resistance, a prior swing, a round number (Nifty 25,000; Bank Nifty 52,000), a VWAP, or a Fibonacci level — and near-worthless mid-range. Every credible study finds that patterns *at meaningful levels* outperform the same patterns *in no-man's-land* by a wide margin. Context is not garnish; it is most of the edge.

**4. Volume is the cheapest filter that moves the needle.** Across patterns, requiring the signal bar (or the confirming bar) to trade on above-average volume typically lifts practical hit-rate by several points *and*, more importantly, culls the worst failures — the thin-volume fake-outs that give the biggest losses. You give up some trades; the ones that remain are cleaner.

## Turning candles into an actual edge: the confluence stack

Because no single candle is reliable enough to trade blindly, the professional approach is a **confluence stack** — you only take the candle when several independent factors agree. Think of it as adding weight to the scale:

1. **Location** — the candle sits at a real S/R, swing, round number, VWAP, or Fib level.
2. **Trend context** — a reversal candle is fighting a trend (needs more evidence) or a continuation candle is aligned with it (needs less).
3. **Volume** — the signal or confirmation bar shows above-average, ideally climactic, participation; or the *absence* of volume confirms a no-demand/no-supply read.
4. **Confirmation candle** — especially for weak single candles (doji, harami, inverted hammer), wait for the *next* candle to close in the expected direction before entering. This one habit rescues the weakest patterns.
5. **Momentum / indicator agreement** — RSI divergence, a MACD cross, or price reclaiming a moving average.
6. **Option-chain / OI** — for index and F&O names, PCR, max-pain, and the OI build/unwind at nearby strikes should not contradict the trade.

A candle backed by four or five of these is a genuinely high-probability setup even though the candle *by itself* is a coin flip plus a few percent. This is the single most important mental model in the chapter: **you are not trading the candle, you are trading the confluence, and the candle is the timing trigger that tells you the confluence has been acted on right now.**

## How to trade it — a repeatable checklist

For any candlestick signal on any Indian instrument, run this sequence before risking capital:

- **Where is it?** Mark the nearest support/resistance, swing, round number, VWAP, Fib. No level nearby → skip.
- **What's the trend?** Reversal against a strong trend needs more confirmation; with-trend continuation needs less.
- **What's the volume?** Compare the signal bar to the 20-period volume average. Below average on a reversal → demand confirmation or pass.
- **Do I need a confirmation candle?** For strong 3-bar patterns, often no. For weak single candles, yes — wait for the next close.
- **Does the option chain agree?** For index/F&O trades, check OI build at the relevant strikes and PCR direction.
- **Define the trade before entry.** Entry (candle close or micro-pullback), stop (beyond the pattern's invalidation wick/body), targets (next structural level and/or a multiple of risk), and size (risk a fixed % of capital; for wide-stop index trades, prefer defined-risk options).

## Pitfalls that quietly destroy candlestick traders

- **Trading shapes without volume or location.** The number-one error. A pattern in a vacuum is close to random.
- **Ignoring the close-position within the range.** A green candle that closes in its lower third is weak *even if the body is up*; VSA lives in the close.
- **Over-fitting timeframes.** A beautiful hammer on the 5-min is noise on the daily. Align your signal timeframe with your trade horizon and check the higher timeframe for context.
- **Confusing frequency with reliability.** Dojis and haramis appear constantly; that ubiquity is *why* they're unreliable — common patterns carry little information.
- **Fighting a trend on one candle.** Reversal candles against a powerful trend fail often; wait for structure to break, not just a single rejection.
- **Mistaking low liquidity for a signal.** In illiquid mid/small-caps, wide wicks and "engulfing" bars can be a single large order, not a crowd — the volume-relative read breaks down. Stick to liquid names (Nifty, Bank Nifty constituents, F&O stocks) where volume actually means participation.
- **Survivorship in the stat tables.** Published hit-rates are backward-looking averages across regimes; your live market may be trending or chopping in ways that shift them. Use the numbers to *rank* patterns and set expectations, never as a promise.

## Interview-ready summary

- **A candlestick is a compressed auction; volume is the conviction behind it.** Reading them together — via the effort-vs-result / VSA lens — is what turns a shape into a signal. The key operational tool is comparing each signal bar's volume to a **20-period volume average** and classifying it low / normal / high / climactic.
- **Reversal candles work best when they mark a high-volume transfer of ownership** (climax/absorption); breakout/continuation candles (marubozu, gaps) need **expanding** volume; and the *absence* of volume (no-demand / no-supply bars) is itself a tradable read.
- **Reliability statistics are humbling and honest:** most *single* candles resolve only ~55-63% in the expected direction unfiltered; three-candle patterns (morning/evening star, three soldiers/crows) are the most reliable at ~65-70%; dojis and haramis are essentially alerts, not triggers. **Success rate is meaningless without the paired reward-to-risk and exit definition** — a 55% setup at 2.5R beats a 65% setup at 0.8R.
- **Location dominates shape, and volume is the cheapest filter that moves the needle** — both lift practical hit-rate several points and, crucially, cut the worst failures.
- The professional method is the **confluence stack** — location + trend context + volume + confirmation candle + momentum/indicator + option-chain/OI. You don't trade the candle; you trade the confluence, and the candle is the timing trigger that says the confluence is being acted on *now*. For Indian F&O names, OI build/unwind and PCR must not contradict the read.
