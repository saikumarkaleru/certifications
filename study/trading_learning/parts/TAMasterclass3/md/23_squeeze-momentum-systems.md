# The Squeeze (TTM) Momentum System

John Carter's TTM Squeeze is one of the most widely used "advanced" indicators on TradingView, and for good reason: it fuses two ideas we developed in the last chapter — Bollinger Band contraction and Keltner Channel context — into a single, elegant volatility-cycle detector, then bolts on a momentum histogram that tells you *which way* the energy is about to release. Where a plain Bollinger Squeeze tells you "a move is coming but not which direction," the TTM Squeeze's momentum component gives you a directional bias with the same signal. This chapter builds the whole system from the two-channel logic up, with exact settings, a Pine-style construction, and worked Nifty / Bank Nifty examples for 2026.

## The core idea — Bollinger inside Keltner

Carter's insight (from *Mastering the Trade*) is a relationship between two volatility envelopes:

- **Bollinger Bands** widen and narrow based on *standard deviation* of price.
- **Keltner Channels** widen and narrow based on *Average True Range (ATR)*.

These two measure volatility slightly differently, and here is the trick: **when the Bollinger Bands contract to sit entirely *inside* the Keltner Channels, the market is in a Squeeze** — volatility has compressed to an unusual degree. When the Bollinger Bands expand back *outside* the Keltner Channels, the Squeeze has "fired" — volatility is releasing and a move is underway.

Why does the Bollinger-inside-Keltner condition capture compression so well? Because standard deviation (Bollinger) reacts faster and more sharply to a quiet, low-range market than ATR (Keltner) does. When price goes truly dead — small ranges, tiny closes-to-closes — the standard-deviation bands collapse faster than the ATR channels, and slip inside them. That nesting is a clean, binary, mechanical signal for "coiled spring." No eyeballing BandWidth lows required — the two envelopes cross and you have your answer.

## Construction — exact settings and formula

The classic TTM Squeeze defaults:

```
# --- Volatility envelopes (length 20) ---
basis      = SMA(Close, 20)
dev        = 2.0 × StdDev(Close, 20)
BB_upper   = basis + dev
BB_lower   = basis − dev

atr        = ATR(20)                 # or SMA of True Range, 20
KC_upper   = basis + 1.5 × atr
KC_lower   = basis − 1.5 × atr

# --- Squeeze state ---
squeeze_on  = (BB_lower > KC_lower) AND (BB_upper < KC_upper)   # BB inside KC
squeeze_off = (BB_lower < KC_lower) AND (BB_upper > KC_upper)   # BB outside KC → fired
```

On the chart this is drawn as a row of dots on the zero line:

| Dot colour | State | Meaning |
|---|---|---|
| Red dot | `squeeze_on` | Squeeze active — energy building, do not trade yet |
| Green dot | `squeeze_off` | Squeeze released ("fired") — the move is starting |

Carter also popularised a "wide/mid/narrow" refinement using a 2.0× / 1.5× / 1.0× Keltner set so you can see *how tight* the squeeze is (a low-compression, mid, or high-compression squeeze — the tightest ones tend to fire hardest), but the two-state red/green version is the workhorse.

### The momentum histogram

The second half of the indicator is a momentum oscillator plotted as a histogram, giving direction:

```
# Linear-regression-based momentum (Carter's version)
mom = LinReg( Close − avg( avg(HighestHigh(20), LowestLow(20)), SMA(Close,20) ), 20 )
```

In words: take price relative to a blend of the 20-bar Donchian midline and the 20-SMA, then run a 20-period linear regression to smooth it into a momentum value. Plotted as a histogram around zero with four colours:

| Histogram | Reading |
|---|---|
| Rising above zero (bright) | Bullish momentum, accelerating |
| Falling above zero (dark) | Bullish but decelerating |
| Falling below zero (bright) | Bearish momentum, accelerating |
| Rising below zero (dark) | Bearish but decelerating |

The **colour of the histogram at the moment the Squeeze fires** is your directional bias. Red dots (building) + histogram above zero and rising → when it fires, lean long. Red dots + histogram below zero and falling → lean short.

## The trade — exact rules

**Setup:** a series of red dots (Squeeze on) — the longer the run of red dots, the more energy stored and the more explosive the eventual fire tends to be.

| Element | Rule (long side; short is the mirror) |
|---|---|
| Universe | Nifty, Bank Nifty, Fin Nifty, liquid NSE stocks, MCX (Crude, Gold), USDINR — any liquid instrument |
| Setup | ≥ 5–6 consecutive red dots (active Squeeze) |
| Direction filter | Momentum histogram above zero **and** rising at/just before the fire |
| Entry | First **green dot** (Squeeze fires) with histogram confirming up; enter at that bar's close or next-bar open |
| Higher-TF gate | Higher timeframe not in an opposing strong trend (e.g. don't take a long fire while the daily is in a clean downtrend) |
| Initial stop | Below the Squeeze's consolidation low (or the Keltner middle/basis) |
| Target | Measured move = height of the consolidation range projected from the breakout; or trail |
| Management | Carter's rule of thumb: Squeeze fires tend to run **~8–10 bars** of momentum before stalling; ride while histogram bars keep growing in the trade direction, exit when they start contracting (colour dims) for 2 consecutive bars |
| Kill | If a green dot fires but the histogram is flat/ambiguous, stand aside — no directional edge |

The "exit when the histogram contracts" rule is the disciplined heart of the system. You are not trying to catch the exact top; you are harvesting the *impulse* the coil released, and getting out when the impulse is spent — signalled by momentum bars shrinking, not by price making a new extreme.

## Worked India example — Nifty TTM Squeeze fires long

A realistic 2026 Nifty daily sequence. After a strong run, Nifty consolidates in a tight range between 24,800 and 25,100 for about two weeks. On the daily TTM Squeeze, red dots appear and persist — seven consecutive red dots as the Bollinger Bands nest inside the Keltner Channels. Throughout the coil, the momentum histogram holds *above zero* and starts curling up in the last two bars: the coil is compressing while the underlying bias stays bullish. This "red dots + histogram above zero and rising" is the highest-quality long setup.

- **The coil:** height ≈ 300 points (25,100 − 24,800).
- **Fire bar:** Nifty closes at 25,160, breaking the coil high. The Squeeze dot turns **green** (Bollinger Bands pop back outside the Keltner Channels), and the histogram prints a bright, rising bar above zero. Index-futures volume expands; the 25,000/25,100 call writers are covering (OI at those strikes falling). **Long confirmed.**
- **Entry:** at the fire bar close 25,160 (or next-day open).
- **Stop:** below the consolidation low 24,800 for a swing version (risk ~360), or tighter under the fire-bar low ~25,020 (risk ~140).
- **Target:** measured move 300 points from the ~25,100 breakout → 25,400 primary; then ride the histogram.
- **Outcome:** the histogram grows brighter and taller for the next six sessions — classic post-fire impulse. Nifty runs to 25,470, exceeding the measured move. On the eighth session the histogram bars begin to *shrink* (colour dims) for two consecutive days even as price nudges slightly higher — momentum divergence. **Exit ~25,420.** That is ~260 points against ~140 risked on the tight version, roughly 1.9R, and the histogram-contraction rule got you out near the top without needing to predict it.

**F&O expression.** A pre-fire Squeeze is a low-IV, coiled state — the same condition where a long straddle/strangle shines *before* the break if you're direction-agnostic. But because the TTM histogram gives a directional bias, the cleaner expression here is a **directional debit spread** (a bull call spread on the long fire) — defined risk, cheaper than a naked call because you're buying into low IV, and you avoid paying for the "which direction" uncertainty that a straddle charges you for.

## Worked example 2 — Bank Nifty intraday fire

The Squeeze works across timeframes; only the holding period changes. Bank Nifty on the 15-minute chart, a realistic morning: after the opening volatility settles, Bank Nifty coils between 52,600 and 52,850 through late morning. Red dots stack up on the 15-min TTM Squeeze; the histogram sits just below zero and is *falling* — bearish bias building inside the coil.

- **Fire:** at 12:15 the 15-min bar closes at 52,560, below the coil low, the dot turns green, histogram prints a bright falling bar below zero. Price is below the session VWAP (~52,700) — confluence for a short.
- **Entry:** short 52,560. Stop above the coil high 52,850 (risk 290) or tighter above the fire-bar high ~52,660 (risk 100).
- **Target:** coil height 250 points from the ~52,600 breakdown → 52,350; trail with the histogram.
- **Outcome:** momentum expands down for ~7 fifteen-minute bars to 52,310, then the histogram bars start shrinking — cover ~52,360. ~200 points on ~100 risked, ~2R.

The lesson repeated: same indicator, same logic, different timeframe. The Squeeze is fractal — the red-dots-then-green-dot-with-histogram-direction template is identical on a 5-minute Crude chart on MCX or a weekly USDINR chart.

## Backtest / edge notes and realistic costs

Honest words on the edge, because this is a quant-adjacent chapter:

- **The volatility-cycle edge is real but not magic.** Low volatility genuinely mean-reverts into high volatility — that is the most robust, best-documented feature of markets, and the Squeeze exploits it directly. The *timing* edge (a move is coming soon) is stronger than the *directional* edge (which way).
- **The directional histogram is a bias, not a certainty.** In backtests across index and large-cap NSE names, fires that agree with the higher-timeframe trend materially outperform counter-trend fires. Counter-trend fires (a long fire in a daily downtrend) are the main source of losing trades. The higher-TF gate is not optional.
- **Fire quality varies.** The tightest, longest squeezes (many red dots, Bollinger deep inside Keltner) fire hardest; shallow squeezes often produce weak, choppy fires. Filtering for compression depth improves the hit rate at the cost of fewer trades.
- **Costs matter, especially intraday.** On Bank Nifty 15-min fires you might take several trades a week; STT (on the sell), brokerage, exchange transaction charges, GST, SEBI fees and stamp duty on an F&O round trip, plus slippage on the fill, can easily eat 15–30% of a small edge. A Squeeze system with a raw expectancy of, say, 0.4R can dwindle to break-even after costs if you over-trade shallow fires. Trade fewer, higher-quality fires.
- **Whipsaw fires.** A green dot can appear, price pokes out, and it immediately squeezes back (red dots resume) — a failed fire, especially around news. Requiring the histogram to *confirm and expand* for a bar after the fire cuts many of these, at the cost of a slightly later entry.

Treat any backtest with proper scepticism: use realistic costs, out-of-sample data, no look-ahead in the linear-regression momentum (it uses only past bars — good), and expect live results below backtest because of slippage and the discretionary exit. If a Squeeze backtest only works on one instrument in one year, it is curve-fit.

## Adaptations for NSE / F&O

- **Multi-timeframe Squeeze stack.** The strongest version: require a Squeeze on a higher timeframe (daily) *and* time the entry off a fire on a lower one (hourly/15-min). A daily Squeeze that fires in agreement with an hourly fire is a high-conviction, larger-position setup.
- **Squeeze + option IV.** Because a Squeeze *is* a low-realised-volatility state, it often coincides with low implied volatility (cheap options). Buying a directional debit spread as the Squeeze fires means you buy premium cheap and profit from both direction and the IV expansion — a genuine edge over buying options mid-trend when IV is already elevated.
- **Event coiling.** Pre-RBI, pre-budget, pre-results, instruments coil and the Squeeze goes red. The fire on the event is direction-uncertain — respect that with a straddle if you must be in, or wait for the post-event fire with the histogram confirming.
- **Instrument fit.** Works best on trending, liquid instruments: Nifty, Bank Nifty, Fin Nifty, large-cap NSE stocks, Crude/Gold on MCX, USDINR. Illiquid mid/small-caps produce erratic, gappy squeezes that fire falsely.

## Confluence

- **Volume / OI:** a fire on expanding volume with supportive option-chain behaviour (short covering at breached strikes) is far more reliable than a thin-volume fire.
- **VWAP (intraday):** align the fire direction with the correct side of session VWAP.
- **Structure:** best fires break a real horizontal level or trendline, not just the coil's edge.
- **Higher-TF trend:** the single most important filter — take fires with the bigger trend, avoid counter-trend fires.
- **Breadth (indices):** an index fire backed by broad participation is trustworthy.

## Pitfalls — the honest list

1. **Trading the red dots.** Red dots mean *wait* — energy is building, not released. Entering during the Squeeze, before the green dot, is jumping the gun; you don't know the direction yet and you'll bleed in the chop.
2. **Ignoring histogram direction.** The green dot alone is not a trade — it's "a move is starting." The histogram tells you *which way*. Green dot with a flat/ambiguous histogram = no trade.
3. **Counter-trend fires.** The biggest loser category. A long fire against a strong daily downtrend usually fails. Gate every fire against the higher-timeframe trend.
4. **Failed/whipsaw fires around news.** Fires on event headlines can reverse instantly. Require post-fire histogram expansion, or wait out the event.
5. **Over-trading shallow squeezes.** Many weak squeezes fire feebly. Trade the tight, long, deep ones; costs will punish a portfolio of marginal fires.
6. **Chasing after the impulse is spent.** By the time the histogram is huge and everyone sees the move, most of the ~8–10 bar impulse is gone. Enter at the fire, not five bars later.
7. **Blindly reusing 20/2.0/1.5 defaults everywhere.** They're good defaults, but very fast timeframes or unusually volatile instruments (Crude) may warrant testing the Keltner multiplier. Don't curve-fit, but don't assume the daily-equity defaults are optimal for a 5-min MCX chart either.

## Interview-ready summary

The TTM Squeeze detects volatility compression by nesting two envelopes: when the **Bollinger Bands (standard-deviation-based) contract entirely inside the Keltner Channels (ATR-based)**, the market is in a Squeeze — plotted as red dots — because standard deviation collapses faster than ATR in a dead market. When the Bollinger Bands expand back *outside* the Keltner Channels, the Squeeze "fires" — a green dot — and a volatility expansion is underway. A **linear-regression momentum histogram** supplies direction: its colour and slope at the moment of firing tell you whether to lean long or short, converting a direction-agnostic Bollinger Squeeze into a directional system. The trade is: wait through a run of red dots (longer = more stored energy), enter on the first green dot in the direction the histogram confirms, stop below the consolidation, target the measured move, and **exit when the histogram bars start contracting** — harvesting the ~8–10 bar impulse rather than predicting the top. The volatility-cycle edge (a move is coming) is robust; the directional edge is weaker, so gating every fire against the higher-timeframe trend is essential. On Nifty, Bank Nifty, MCX and USDINR in 2026 it is fully fractal across timeframes, pairs naturally with low-IV directional debit spreads in F&O, and — provided you never trade the red dots, never ignore the histogram, avoid counter-trend and shallow fires, and respect real trading costs — it is one of the cleanest volatility-based momentum systems available.
