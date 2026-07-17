# Fibonacci Retracement, Extension & Projection

## What it is & why it works

Fibonacci analysis is the practice of measuring a market swing and marking specific ratios along it — 38.2%, 50%, 61.8%, 78.6% inside the move (retracements) and 127.2%, 161.8%, 261.8% beyond it (extensions and projections). Traders use these levels to anticipate where a pullback is likely to end and where a trend is likely to run. On any liquid Indian instrument — Nifty 50, Bank Nifty, Reliance, HDFC Bank — you will repeatedly see price stall, base, and reverse near 61.8% of the prior leg. That is not mysticism. It is the visible footprint of how positioning, profit-taking, and fresh entries cluster.

The number sequence itself (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...) comes from Leonardo of Pisa. Each number is the sum of the previous two. Divide any number by the next and the ratio converges to 0.618 (the "golden ratio"). Divide by the number two places ahead and you get 0.382; three places ahead, 0.236. Take the reciprocal of 0.618 and you get 1.618. The square root of 0.618 gives 0.786. These are the only ratios that matter for trading; the biology-textbook stories about sunflowers and nautilus shells are irrelevant to whether a level holds.

Why do these levels actually work in markets? Three honest reasons. First, **self-fulfilling behaviour** — every serious desk in Mumbai runs the same Fibonacci grid on the same swing high and low, so a large, overlapping population places limit orders and stops around 61.8%. Orders create the reaction. Second, **natural proportion of pullbacks** — healthy trends do not retrace their entire prior leg; a normal, orderly correction against a strong trend tends to give back somewhere between one-third and two-thirds before buyers or sellers reassert. The Fibonacci band 38.2%–61.8% simply frames that empirically common "normal pullback" zone. Third, **it imposes discipline** — it forces you to define the swing, the invalidation point, and the reward objective before you commit capital.

Be honest about what Fibonacci is not. It is not a predictive law of physics. Levels fail routinely. A retracement tool by itself is a low-quality signal; its value appears only when it lines up with structure (a prior support/resistance shelf, a moving average, a trendline) and with order-flow evidence such as option-chain OI. Treat every level as a *decision zone*, not a magic price.

## The mechanics

**Retracement — pulling the tool.** You anchor the tool on a clearly defined impulse leg. In an uptrend you click the swing low (0%) and drag to the swing high (100%); the retracement levels then print below the high, marking how far a pullback has travelled. In a downtrend you click the swing high (0%) and drag to the swing low (100%); levels print above the low. The single most common beginner error is picking sloppy anchors — always use the *actual* extreme candle wick (or close, if you trade closing-basis) of a clean, obvious swing, not a random intraday spike.

The standard retracement ratios and how each is used:

| Level | Value | Character | Typical use |
|---|---|---|---|
| 23.6% | 0.236 | Shallow | Very strong trend; only the fastest movers pull back this little |
| 38.2% | 0.382 | Shallow-normal | First real support in a strong trend |
| 50.0% | 0.500 | Midpoint | Not a Fibonacci number but universally watched (Dow theory "half retrace") |
| 61.8% | 0.618 | Deep-normal | The "golden" level; the highest-probability turn zone |
| 78.6% | 0.786 | Deep | Last-ditch; beyond this the trend is in doubt |
| 100% | 1.000 | Full | Prior swing origin; a break negates the swing |

**The "golden pocket."** Traders on TradingView and Chartink often add a custom level at 65% or 66% and watch the **61.8%–65%** band as the golden pocket — the sweet spot where the highest concentration of reversal entries cluster. Add 0.65 as a custom level in your tool settings so the pocket is visible.

**Extension vs projection — an important distinction.**
- **Extension** measures how far price travels *beyond* the 100% of a single leg — it uses the same two anchors (low to high) and reads levels above 100%: 127.2%, 161.8%, 200%, 261.8%. This answers "how far can this leg run past its origin high?" It is a two-point tool.
- **Projection (a.k.a. trend-based Fib extension, or the ABCD/three-point extension)** uses *three* anchors: point A (leg start), point B (leg end), point C (the pullback low). It projects the length of the A–B leg forward from C. This answers "after this pullback to C, how far should the next leg run?" It is the more useful of the two for setting profit targets in a trending market.

Projection targets from a three-point (A–B–C) tool:

| Projection | Meaning |
|---|---|
| 61.8% of AB from C | Conservative first target, common in choppy markets |
| 100% of AB from C | "Measured move" — the C-leg equals the A-leg (very common) |
| 127.2% of AB from C | Standard extended target in a healthy trend |
| 161.8% of AB from C | Aggressive target; typical trend-day objective |
| 261.8% of AB from C | Rare, parabolic runs only |

**Settings that matter.** Trade on the timeframe you actually hold — a swing trader anchors on daily swings; an intraday Bank Nifty trader anchors on 15-minute or hourly swings. Decide once whether you anchor on wicks or closes and stay consistent. On TradingView, save a Fib template with 0, 0.236, 0.382, 0.5, 0.618, 0.65, 0.786, 1.0 and extension levels 1.272, 1.618, 2.618 so every chart is measured identically.

## Reading it — a worked Nifty example

Take a realistic Nifty 50 swing. Suppose Nifty rallies from a swing low of **23,300** to a swing high of **24,850** — a clean 1,550-point impulse leg over a couple of weeks. Price then rolls over and begins to pull back. We anchor the retracement tool: 0% at 24,850 (top) and 100% at 23,300 (bottom), so the levels print as support below the high.

Compute the grid:
- 23.6% → 24,850 − (0.236 × 1,550) = 24,850 − 366 = **24,484**
- 38.2% → 24,850 − 592 = **24,258**
- 50.0% → 24,850 − 775 = **24,075**
- 61.8% → 24,850 − 958 = **23,892**
- 65.0% (pocket base) → 24,850 − 1,008 = **23,842**
- 78.6% → 24,850 − 1,218 = **23,632**

**Phase 1 — the shallow test.** Price drifts down and first pauses near 24,484 (23.6%). Volume on the down-move is unremarkable; this is orderly profit-taking, not distribution. A shallow hold here would signal a very strong trend, but on this occasion 23.6% breaks on a daily close — the pullback has further to run. Do not marry the first level.

**Phase 2 — the 38.2% shelf.** Price reaches 24,258. Notice that this happens to coincide with a prior consolidation shelf from three weeks earlier around 24,240–24,280 — structure and Fib overlap. Price bounces 150 points intraday but the bounce is sold. When a *confluent* level gives way, it tells you the correction is deeper than shallow; the odds now favour a test of the golden pocket.

**Phase 3 — the golden pocket.** Nifty grinds down to **23,892–23,842** (61.8%–65%). Here several things line up: the rising 50-day EMA is sitting at ~23,870; the pocket base at 23,842 sits just above a round psychological 23,800; and on the option chain the 23,800 and 23,900 puts show the heaviest open interest for the current monthly expiry — meaning writers expect that band to hold. This is where a disciplined trader gets interested. Price makes a lower wick to 23,861, closes back at 23,940 forming a bullish pin/hammer on the daily, and the next day opens firm.

**Phase 4 — confirmation and the new leg.** The reversal from the pocket is real. Now flip to the projection tool. Anchor A = 23,300 (leg start), B = 24,850 (leg end), C = 23,861 (pocket low). AB length = 1,550. Project from C:
- 61.8% AB from C = 23,861 + 958 = **24,819** (roughly the old high — first resistance)
- 100% AB from C = 23,861 + 1,550 = **25,411** (measured move)
- 127.2% AB from C = 23,861 + 1,972 = **25,833**
- 161.8% AB from C = 23,861 + 2,508 = **26,369**

The reading gives you a full map: buy the pocket around 23,880–23,920, expect resistance near the old high, and if that clears, the measured-move objective is ~25,400.

## Trading it

**Entry trigger.** Do not buy blindly at a Fib line — that is how you get run over. Wait for the zone to *do something*. Concretely, in the Nifty example: with the pocket at 23,842–23,892, the trigger is a bullish reversal candle on your holding timeframe that closes back above 23,892, ideally a hammer, bullish engulfing, or a strong hourly close reclaiming the level. Aggressive traders scale a first tranche with a resting limit inside the pocket; conservative traders wait for the confirmation candle's close and enter on the next open or on a break of the confirmation candle's high (24,000).

**Stop-loss.** The invalidation is structural: a decisive close below the 78.6% level (**23,632**), or below the pocket low with a buffer. If you entered on confirmation at ~24,000 with a stop below 23,630, risk is ~370 points. Beyond 78.6%, the reversal thesis is broken and the more likely path is a full retest of 23,300. Never widen the stop to "give it room" — the 78.6% break is the market telling you the swing failed.

**Targets and measured move.** Use the projection levels as staged exits:
- T1 = 61.8% projection ≈ 24,819 (old high) — book one-third, trail the rest.
- T2 = 100% projection ≈ 25,411 (measured move) — book another third.
- T3 = 127.2% ≈ 25,833 — runner, trailed under rising swing lows or the 20-EMA.

With entry 24,000, stop 23,630 (risk 370) and T1 24,819 (reward 819), the first target alone is ~2.2R; carrying a runner to the measured move pushes blended reward toward 3–4R. That asymmetry — small defined risk at a high-probability zone, multiple of that in reward — is the entire point of trading Fibonacci.

**Scenario management.**
- *Clean hold and run:* pocket holds, price confirms, you trail up. Standard best case.
- *Deep wick then hold:* price briefly pierces to 78.6% (23,632) intraday but closes back inside the pocket. This "spring" below the level is often the strongest signal of all — it flushes weak-handed stops before reversing. If your stop was on a *closing* basis below 78.6%, you survive; if it was a tight intraday stop, you get shaken out. This is why closing-basis stops on a wide, high-conviction swing level are often superior.
- *Clean break down:* daily closes below 78.6%. Exit, stand aside, and re-measure — the market may now be building a larger top, and the next play could be a *short* on the retest of a broken level.

## Confluence

A Fibonacci level in isolation is a coin-flip-plus; a Fibonacci level with three other things pointing at the same price is a trade. Stack the following:

**Moving averages.** When the 50-day or 200-day EMA sits inside your retracement zone, the level gains weight. In the Nifty example, the 50-EMA at 23,870 fell right inside the golden pocket — that overlap is a classic high-probability "buy the dip in an uptrend" configuration.

**Prior structure.** The best Fib levels land on old support/resistance shelves, gap fills, or the breakout point of a prior range. The 38.2% at 24,258 overlapping the old 24,240–24,280 shelf is an example; when it broke, that told you the shallow-hold thesis was wrong and pushed focus to the pocket.

**Option-chain / OI (the India edge).** This is where you convert a chart level into a positioning read. Around the golden pocket, look at the monthly option chain:
- **Heavy put OI** at 23,800/23,900 means option writers are defending that band — they are effectively selling insurance that Nifty stays above it, and they hedge to keep it there. That supports the pocket.
- **PCR** rising as price hits the pocket, plus put writers *adding* OI rather than unwinding, signals confidence in the floor.
- If, instead, put writers are *unwinding* (OI falling) as price approaches 23,900, the floor is being pulled — a warning that the pocket may fail.
- **Max Pain** near 24,000 for the expiry gives a magnet that aligns with a bounce from the pocket back toward 24,000+.

**Momentum divergence.** If price makes its pocket low while RSI or MACD makes a higher low (bullish divergence), the reversal odds improve materially. A pocket low with divergence, on a confluent EMA, defended by put OI, is about as good as a mean-reversion long gets.

**Multi-timeframe agreement.** The daily golden pocket is far stronger if the weekly chart shows price merely pulling back into its own rising 20-week average. Higher-timeframe context filters out counter-trend traps.

The discipline: require **at least two independent confluences** beyond the Fib line before sizing a full position. Fib + EMA + put-OI floor + divergence is an A-setup; a lone 61.8% line on a random swing is not a trade.

## Pitfalls & false signals

**Bad anchors, garbage levels.** The most common failure isn't the market, it's the trader picking an ambiguous swing. Two analysts measuring different highs will get pockets 200 points apart, then argue about "why Fib didn't work." Use only clean, obvious, high-timeframe swings, and note that experienced traders often draw two or three plausible grids and treat the *overlap zone* as the real level.

**Trending markets ignore retracements.** In a runaway trend — think a post-Budget momentum thrust or a stock in a fresh breakout — price may only pull back 23.6% or not at all before continuing. Waiting for a "deep" 61.8% dip means missing the whole move. Conversely, in a violent bear leg, retracements can be shallow to the downside and fast. Fib retracement is a *pullback* tool; it presumes an orderly, mean-reverting correction, which strong trends don't always give.

**Levels are zones, not lines.** Price rarely reverses to the tick. Treat each ratio as a band of roughly ±0.2–0.3% (on Nifty, ~50–75 points around a level). Traders who place tick-perfect limit orders at 61.8% get filled and then stopped when price overshoots by 30 points into a cluster of stops. Build the buffer in.

**The overshoot / stop-hunt.** Liquid instruments frequently spike *just past* an obvious level to trigger clustered stops before reversing (the "spring" below 78.6% described earlier). If your stop sits exactly at the obvious level, you are donating to the flush. Place stops beyond the *next* level or use closing-basis stops on conviction trades.

**Fitting the data after the fact.** It is trivially easy to look at a completed chart, find the one swing whose 61.8% caught the low, and declare Fibonacci magic — while ignoring the twenty swings where it didn't. This hindsight bias is the single biggest reason people over-trust the tool. Judge Fibonacci only on forward, pre-committed levels with a stop and a plan.

**Over-cluttering the chart.** Ten Fib grids, three extension sets, and every ratio visible turns analysis into a Rorschach test where you can justify any trade. Keep it clean: one or two grids, the pocket, and the key extension targets.

How pros filter it: they never trade a naked Fib level, they demand structural and order-flow confluence, they trade closing confirmation over the raw touch, they buffer their stops beyond the obvious flush point, and they accept that even A-grade setups fail perhaps a third of the time — which is exactly why the reward-to-risk must be 2:1 or better before they commit.

## Interview-ready summary

"Fibonacci retracements mark where a normal pullback is likely to end — 38.2%, 50%, 61.8% and 78.6% of the prior impulse leg — with the 61.8%–65% 'golden pocket' being the highest-probability turn zone. Extensions and three-point projections then set profit targets beyond the move, with the 100% projection giving a symmetric measured move and 161.8% a trend-day objective. The levels work partly because they frame the empirically normal depth of a healthy correction, and partly because every desk draws the same grid, so orders cluster there. But a Fib line alone is weak — I only trade it where it overlaps real structure, a key moving average, and, in Indian markets, supportive option-chain OI, ideally with a bullish reversal candle for confirmation. I set my stop beyond the 78.6% level because a decisive break there invalidates the swing, and I target the projection levels for a 2:1-or-better payoff. The honest caveat: strong trends barely retrace, levels are zones not exact prices, and hindsight makes Fibonacci look more reliable than it is — so I treat every level as a decision zone requiring confluence, never a guarantee."
