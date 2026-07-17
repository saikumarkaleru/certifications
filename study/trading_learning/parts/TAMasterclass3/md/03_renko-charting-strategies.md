# Renko Charting Strategies

Renko sits beside Point & Figure in the small family of charts that throw time away and plot only meaningful price movement — but where P&F stacks X's and O's in shared columns, Renko draws a running staircase of equal **bricks** (the word *renga* is Japanese for brick). Each brick is the same fixed size; a new brick appears only when price travels that full distance in a direction. The result is the smoothest common price chart in existence: a clean flight of green steps up, red steps down, with the intraday chop that shakes traders out of candlestick positions simply erased. For Indian markets in 2026 — where Bank Nifty can whip 300 points in ten minutes and a candle chart looks like static — Renko's noise suppression is not cosmetic; it is a genuine edge for trend-followers, and a genuine trap for anyone who misunderstands what the smoothness costs. This chapter treats Renko as a *strategy* engine: exact rules, an Indian worked example in rupees, backtest realism, F&O adaptation, and the honest limitations.

## Origin and the idea

Renko came to the West via Steve Nison's work on Japanese charting techniques, alongside Kagi and Three-Line-Break. The idea is austere: **decide a brick size, and only print a brick when price moves that far.** Time, volume, and the exact path within a brick are all discarded. A brick is either up (bullish) or down (bearish). Crucially, in classic Renko a reversal requires price to move **two brick sizes** in the opposite direction — one brick to cancel the pause and one to establish the new direction — which is why Renko trends persist so cleanly and why reversals lag.

The strategic promise is simple and powerful: **if you only ever see bricks, you can only ever trade the trend.** A string of green bricks *is* an uptrend, definitionally. You cannot be faked out by a single vicious wick because a wick that doesn't complete a brick doesn't exist on the chart. The trade-off, equally simple, is that Renko is **repainting-adjacent and lagging**: the last brick can change until the move completes, and reversals arrive one-to-two bricks late. Everything strategic about Renko flows from managing that trade-off.

## Construction, brick types, and settings

### How bricks form

Assume brick size **B**. You have just printed a green (up) brick topping at price P.

- **Extend up:** when price reaches **P + B**, print another green brick. If price rockets, you may print several green bricks at once to catch up.
- **Reverse down:** a red brick only prints when price falls to **P − 2B** (two brick sizes below the top of the last green brick). The first red brick then spans from P − B down to P − 2B — it is offset, exactly like P&F's one-box reversal offset, so up and down bricks never share the same extreme. Symmetric rules apply for red-to-green reversal.

This **2×B reversal** is the heart of Renko's behaviour: trends need only 1B to continue but 2B to flip. That asymmetry is what makes the staircase so persistent — and what makes Renko lag turns.

### Brick-size methods

| Method | How the brick is set | Best for |
|---|---|---|
| **Traditional / fixed** | A hard number of points/rupees (e.g. Nifty 25 pts, a ₹500 stock ₹5) | Single instrument you know; stable, reproducible |
| **ATR-based** | Brick = current ATR (e.g. ATR-14) | Auto-adapts to volatility regime; the popular default |
| **Percentage** | Brick = X% of price | Comparing many instruments of different price levels |

**ATR Renko is the standard default on TradingView** and deserves a health warning: because ATR changes every bar, an ATR-Renko chart **repaints history** — past bricks redraw when the ATR value updates, so a backtest on ATR-Renko can look far better than it trades live. For any serious rule-testing, use a **fixed** brick so history is stable and reproducible. Use ATR-Renko for eyeballing the live trend, not for computing backtest statistics.

### Wicks, sources, and platform settings

- **Source: close vs high-low.** Traditional Renko builds bricks from the **close**; some platforms offer a high-low variant that reverses faster (and noisier). Close-based is the standard and what strategy rules below assume.
- **Wick Renko.** Some charts add thin wicks to bricks to show the intra-brick extreme. Informative, but the brick body is still what triggers signals — don't trade the wick.
- **TradingView:** chart type "Renko", *Box size assignment* = Traditional or ATR, *Source* = Close. For Nifty daily swing work, fixed 25–30 points; for Bank Nifty, 75–100 points; intraday Bank Nifty, 20–30 points. **Chartink** cannot render true Renko, so it is used only to pre-screen a universe; the Renko signal itself is read on TradingView.

## Worked India example (levels and ₹)

Build a **Nifty Renko, fixed brick = 25 points, close-based.** Suppose bricks form this sequence (each brick = 25 points of Nifty):

`… 24,500 → 24,525 → 24,550 → 24,575 (four green bricks) …`

then price stalls. For a red brick to print, Nifty must fall to 24,575 − (2×25) = **24,525**. Say it only dips to 24,540 — **no red brick**, the uptrend stays intact and unshaken despite a 35-point wobble that would have rattled a candle trader. Price then resumes: green bricks to 24,600, 24,625, 24,650.

Now a genuine reversal. From the 24,650 top, Nifty falls to 24,600 (= 24,650 − 2×25) → the **first red brick** prints, spanning 24,625→24,600. More red bricks follow to 24,575, 24,550. The staircase has flipped from green to red — a clean, unambiguous trend-change signal.

**The trade.** A common Renko rule set:
- **Enter long** on the *first green brick after a run of red* (a colour flip), or more conservatively on the **second** confirming green brick to reduce single-brick whipsaw.
- Here, suppose after the red run down to 24,550 the market bottoms and prints a green brick to 24,575, then another to 24,600 — **buy on the second green brick at 24,600** (Nifty futures, or a 24,600/24,900 bull call spread).
- **Stop:** below the low of the reversal — one brick below the last red-brick low, so a stop near 24,525 (24,550 low − one brick). Risk = 24,600 − 24,525 = 75 points × lot 75 = ₹5,625/lot.
- **Target/exit:** trend-follow — stay long while green bricks print; **exit on the first red brick** (or a 2-red-brick confirmation for less whipsaw). If green bricks run to 24,850 before the first red brick prints, you exit around 24,800 (one brick back from 24,850 top on the flip), capturing ~200 points against 75 risked — R:R ≈ 2.7.

**Bank Nifty intraday version.** Fixed brick 25 points, close-based, on a 5-minute feed. Bank Nifty near 50,000: buy on the second green brick after a red run, stop one brick below the reversal low (~50 points risk), ride green bricks, exit on first red brick. The whole appeal is that the 25-point brick silences the sub-25-point noise that makes 5-minute candle scalping so hostile.

## How to trade it: the strategy rules

Renko strategies cluster into three families. Rules stated for the long side; invert for short.

### 1. Brick-flip trend following (the core system)

| Element | Rule |
|---|---|
| Universe | Liquid, trending instruments: Nifty, Bank Nifty, Fin Nifty, F&O stocks, MCX crude/gold, USDINR |
| Brick | Fixed; Nifty 25–30, Bank Nifty 75–100 (swing), 20–30 (intraday) |
| Entry | Buy on 2nd consecutive green brick after a red run (confirmation) |
| Exit | Sell on 1st (or 2nd) red brick |
| Stop | One brick below the reversal low |
| Sizing | Fixed rupee risk per trade; lots = risk-budget ÷ (stop-distance × lot × point-value) |

This is a **pure trend system**: it wins big in trends and bleeds small losses in ranges. Its equity curve is choppy-then-explosive — you *must* have the temperament to sit through the chop.

### 2. Renko + moving average / indicator overlay

Add a filter to cut range-bound whipsaws. Popular Indian variants:
- **Renko + EMA(10 on brick close):** only take green-brick entries while price is above the brick EMA; skip signals against it. Filters the flat, back-and-forth single-brick reversals that plague pure flip trading.
- **Renko + supertrend / ADX-on-bricks:** require a trend-strength confirmation. When ADX on the brick series is rising, trade flips; when it's flat and low, stand aside (the range regime where Renko whipsaws most).

### 3. Renko pattern / breakout trading

Because Renko removes noise, classic patterns render with startling clarity: **brick-based support/resistance** (multiple bricks stalling at the same price), **double tops/bottoms**, and **trendlines** across brick corners. Trade a breakout when a green brick prints *above* a brick-resistance shelf, stop below the shelf. The clean grid makes these levels less ambiguous than on candles — the same virtue P&F offers.

## Backtest / edge notes and realistic costs

Renko backtests are **notoriously misleading**, and honesty here matters more than in almost any other method:

- **ATR repaint inflates results.** An ATR-Renko backtest can show a gorgeous equity curve that is partly an artefact of history redrawing. Always backtest on **fixed bricks** with a stable, reproducible series. If your platform builds Renko from OHLC bars rather than tick data, intra-bar path assumptions further distort fills — prefer tick-based Renko for realistic testing.
- **The "one big trend" illusion.** Because Renko catches trends beautifully, a backtest over a strongly trending Nifty year (say a persistent bull run) will flatter the system. Test across at least one bull, one bear, and one **sideways** year — the sideways year is where Renko's whipsaw losses reveal the true edge.
- **Costs are the killer in ranges.** Every flip is a round-trip. In a choppy Bank Nifty week a small-brick system can flip 8–12 times. With brokerage, STT, exchange fees, GST, and stamp duty, plus **slippage** (a brick completes *at* a level but you fill a few points worse), a realistic all-in cost of ₹40–80 per Bank Nifty round-trip on futures — and far more in option premium decay — can turn a gross-profitable range-period into a net loss. Model costs explicitly per flip; do not assume frictionless fills.
- **Slippage and brick timing.** A brick "prints" at a clean number but you cannot always fill there; assume you enter one tick-to-a-few-points into the next brick. On illiquid names this gap widens sharply — another reason to stay in liquid instruments.
- **Realistic edge.** Well-built fixed-brick Renko trend systems on liquid Indian instruments tend to show **modest win rates (~35–45%) with high reward-to-risk** — the classic trend-follower profile: many small losses, few large wins. If your backtest shows a high win rate *and* high R:R, suspect repaint or look-ahead bias.

## Adaptations for NSE / F&O

- **Brick size to the instrument's tick and lot.** Choose a brick that is a clean multiple of the tick and large enough that a round-trip's costs are small versus the brick. A 5-point Bank Nifty brick is too small — costs and slippage dominate. 25–100 points is the workable band.
- **Options: buy directional, respect theta.** Renko flips can be slow (2B lag), and long options bleed **theta** while you wait for confirmation. Prefer **spreads** (bull call / bear put) over naked long options so decay is partly financed, and prefer **futures** for pure trend capture where margin allows. On a strong multi-brick trend, futures or spreads outperform naked options badly hurt by the entry lag.
- **Expiry awareness.** Renko ignores time, but options don't. Avoid initiating fresh Renko option trades late in the weekly expiry cycle where theta swamps a slow brick signal; futures are time-agnostic and pair more naturally with a time-agnostic chart.
- **Regime switch via ATR brick — for viewing only.** Use an ATR-Renko chart to *judge* whether the market is trending or ranging (long clean runs vs constant flipping), then execute on a **fixed-brick** chart so your rules and risk are stable.

## Pitfalls

- **Whipsaw in ranges is the whole risk.** Renko's smoothness in trends becomes a rapid-fire flip machine in a tight range. Every strategy above lives or dies on a range filter (EMA/ADX) or the discipline to sit out low-volatility regimes.
- **Repaint / last-brick uncertainty.** The forming brick isn't final until the move completes. Never act on a half-formed brick; wait for the brick to close. With ATR bricks, even past bricks can shift — do not trust ATR-Renko for backtests.
- **Lag at reversals.** The 2×B reversal means you always give back one-to-two bricks at every turn. That is the price of noise immunity. Accept it; don't try to "front-run" the flip.
- **No time or volume.** Renko hides *how long* a level took to build and *how much* traded — information a Wyckoff or volume-profile trader would want. Pair Renko with an OI/volume read on a separate panel for context.
- **Brick size over-optimisation.** Only one real knob exists, and it is tempting to curve-fit it to a favourable period. Validate out-of-sample and across regimes.
- **Illiquidity distortion.** On thin names, a single print can complete a brick that mid-market never really justified. Trade Renko only on liquid Nifty/Bank Nifty/Fin Nifty, F&O stocks, MCX, USDINR.

## Summary

Renko charts price as a staircase of **equal fixed-size bricks**, printing a new brick only when price travels a full brick in a direction and requiring a **two-brick move to reverse** — which erases intraday noise and renders trends as clean runs of same-coloured bricks. Its strategic identity is a **pure trend-follower**: enter on a confirmed colour flip (ideally the second brick), stop one brick beyond the reversal, ride same-coloured bricks, and exit on the opposite brick — all rule-bound. For Indian markets, use **fixed** bricks (Nifty 25–30, Bank Nifty 75–100 swing / 20–30 intraday) for stable, reproducible rules, and treat **ATR-Renko as a viewing tool only** because it repaints and inflates backtests. Add an EMA/ADX range filter to survive the sideways regimes where Renko whipsaws, model **per-flip costs and slippage** honestly (they can flip a gross-profitable range period into a net loss), and test across bull, bear, and — critically — sideways years. In F&O, prefer futures or spreads over naked options because Renko's reversal lag punishes theta. The honest bottom line: Renko trades a **modest win rate for high reward-to-risk** and buys noise immunity at the cost of lag and range-whipsaw. In one line: *Renko is the chart that lets you hold a trend without flinching — provided you accept that it will always be a beat late at the turn.*
