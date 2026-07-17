# Donchian Channel Systems

The Donchian channel is deceptively simple — it is nothing more than the highest high and the lowest low over the last *n* bars, plotted as two lines with an optional midline between them. Yet this humble construction is the direct ancestor of the entire mechanical trend-following industry. Richard Donchian, a Yale-educated Armenian-American who is widely called the "father of trend following," began publishing his "weekly rule" and moving-average methods in the 1950s and 1960s. His most famous rule — the **4-week rule** (buy a new 4-week high, sell a new 4-week low) — was studied and reportedly ranked among the best-performing mechanical systems of its era, and it became the seed from which the Turtle system's 20-day/55-day breakouts grew. This chapter treats the Donchian channel not as a single indicator but as a **family of complete trading systems**: the pure breakout, the exit/trailing variant, the midline pullback, and the volatility-adaptive versions — all worked through for Nifty, Bank Nifty, and MCX with rupee levels.

The reason the Donchian channel deserves its own chapter (separate from the Turtles, who are one *application* of it) is that it is the cleanest possible expression of a profound market truth: **a new extreme is information.** When price closes above every high of the past *n* periods, every single person who bought in that window is now in profit, there is no overhead supply of trapped sellers, and the balance of demand has objectively shifted. Whether you trade it, fade it, or use it as a stop, the Donchian channel forces you to define "trend" and "breakout" objectively — no subjective trendlines, no eyeballing.

## What it is and the logic

A Donchian channel over lookback *n* has three lines:

```
Upper Band  = Highest High over the last n bars
Lower Band  = Lowest Low over the last n bars
Middle Band = (Upper Band + Lower Band) / 2
```

Note two subtleties that matter enormously in practice:

1. **Include or exclude the current bar?** For a *breakout* signal you must compute the channel using the **prior n bars excluding the current one** — otherwise the current bar's own high defines the upper band and price can never "break out" of it. So the tradeable upper band is "highest high of the previous n bars." Charting platforms differ; TradingView's built-in Donchian *includes* the current bar, which is fine for visualisation but wrong for signalling — offset it or code it explicitly.
2. **Close vs. intrabar touch.** You can trigger on an intrabar penetration (aggressive, more signals, more whipsaw) or on a **closing break** (conservative, fewer false signals). Donchian's original weekly rule used closes; most robust implementations use closing breaks or a small buffer.

The channel **widens** in volatile expansions and **narrows** in quiet consolidations, so its shape itself is a volatility read — a long narrowing channel ("coiling") often precedes an energetic breakout, echoing the Bollinger "squeeze" idea but with hard high/low bounds instead of standard deviations.

The **logic hierarchy**:
- Upper-band break = trend up begins / continues (buy or hold longs).
- Lower-band break = trend down (sell/short or exit longs).
- Price oscillating around the midline with no band breaks = range/no-trend (stand aside or trade the range).

## Construction: rules, settings, and the system variants

### Parameter selection

| Lookback (bars) | Character | Typical use |
|---|---|---|
| 10-20 | Fast, many signals, whippy | Short-term entries; Turtle exit (10) and entry (20) |
| 20-30 | Balanced | Swing trend entries on daily charts |
| 40-55 | Slow, robust, fewer signals | Position trend entries (Turtle System 2 = 55) |
| 4-week / 20-day | Donchian's classic "4-week rule" | The original benchmark |

A common robust pairing is an **asymmetric** channel: a **longer entry** channel and a **shorter exit** channel, so you require conviction to enter but leave quickly. Turtles used 20-in/10-out and 55-in/20-out. This asymmetry is the key design lever.

### Variant 1 — Pure breakout system (long/short)

| Rule | Definition |
|---|---|
| Entry long | Close > upper band of prior 20 bars |
| Entry short | Close < lower band of prior 20 bars |
| Exit long | Close < lower band of prior 10 bars (or hit stop) |
| Exit short | Close > upper band of prior 10 bars |
| Stop | Below recent swing / 2×ATR / opposite short-channel band |

### Variant 2 — Donchian as a trailing stop (exit-only)

Here you enter by some *other* method (a pullback, a pattern, a moving-average cross) and use a short Donchian channel purely to **trail the exit**: stay long until price closes below the N-bar low. This is one of the most practical uses — an objective, self-widening trailing stop that gives room in volatile trends and tightens as ranges narrow. A 10-bar or 20-bar lower band is a superb "let winners run" trail.

### Variant 3 — Midline (mean-reversion / pullback) system

In a **confirmed uptrend** (e.g., price above the 200-day and the channel sloping up), buy pullbacks to the **midline** rather than chasing the upper-band breakout. Entry: price dips to the middle band and holds; stop below the lower band; target back toward the upper band. This turns the Donchian channel into a pullback tool and reduces the "buy the extreme high" discomfort — but it only works *with* a trend filter; fading in a downtrend is a losing proposition.

### Variant 4 — Volatility-adaptive / filtered breakout

Because raw breakouts whipsaw in choppy markets, professional versions add filters:
- **Trend filter:** only take upper-band breaks when price is above the 200-day SMA (and lower-band breaks below it). This single filter historically improves breakout robustness dramatically.
- **Volatility/squeeze filter:** only trade breakouts that emerge from a **narrow channel** (channel width < some ATR multiple), targeting genuine range-expansion moves and skipping breakouts that occur mid-trend when the channel is already wide.
- **ATR buffer:** require the close to exceed the band by **0.25-0.5 ATR** to filter marginal pokes.

## Worked India example (levels and ₹)

**Instrument: Bank Nifty futures.** Lot size (₹/point) = **15** (2025). Account = ₹15,00,000. We'll run **Variant 1** (20-in / 10-out) with an ATR stop.

**Setup.** Bank Nifty has consolidated for a month between roughly 47,200 and 48,000. Over the last 20 sessions:
- Highest high (prior 20 bars, excluding today) = **48,000** → upper band.
- Lowest low = **47,000** → lower band.
- Midline = **47,500**.
- 14-day ATR = **520 points**.

**Entry.** Today Bank Nifty closes at **48,120**, a clean close above the 48,000 upper band → **go long at ~48,150** (next-open or on-close fill). Trend filter check: price is above its 200-day, so the long breakout is confirmed.

**Position size.** Risk 1% = ₹15,000. Stop at 2×ATR below entry = 48,150 − 1,040 = **47,110** (also just under the 47,000 channel floor — good confluence). Risk per lot = 1,040 points × ₹15 = ₹15,600. That is ~1 lot for ~1% risk → **trade 1 lot** (round down from 0.96).

**Trailing exit.** As the trend develops, we trail with the **10-bar lower band**:
- Bank Nifty rallies over three weeks to **50,400**.
- The 10-bar lower band ratchets up to **49,600**.
- On a pullback, Bank Nifty closes at **49,540**, below the 10-bar low → **exit at ~49,500**.

**P&L.** Entry 48,150, exit 49,500 → 1,350 points × ₹15 = **₹20,250** (+1.35% on account) on one trade. Had the breakout failed and reversed to the 47,110 stop, the loss would have been −₹15,600 (−1.04%) — the defined, acceptable cost of a false breakout.

**Contrast — a whipsaw.** Suppose instead the 48,120 close was a "fakeout": next day Bank Nifty reverses hard to 47,050, hitting the 47,110 stop → −₹15,600. In a choppy, rangebound month this happens repeatedly, which is exactly why the trend filter and squeeze filter (Variant 4) earn their keep — they would have kept you out of many of these mid-range pokes.

## How to trade it: entry, stop, target, management

1. **Choose the channel length to your horizon** — 20/10 for swing, 55/20 for position. Decide *closing break vs. intrabar* and stick to it (closing breaks are more robust).
2. **Apply a trend filter** (200-day) unless you deliberately want a symmetric long/short system in all regimes.
3. **Enter** on the confirmed band break, optionally requiring a 0.25-0.5 ATR buffer.
4. **Stop** at the opposite short-channel band or 2×ATR, whichever is tighter/logical; size the position so that stop = ~1% of equity.
5. **Manage** by trailing with the exit-channel lower band (longs) — an objective "ride the trend" stop. Optionally scale out a portion at a measured target (e.g., channel width projected from the breakout) and let the rest trail.
6. **Stand aside** when the channel is wide and price is chopping around the midline with no clean breaks — Donchian systems bleed in rangebound regimes and you must accept many small losses or filter them out.

## Confluence

- **Volume / delivery:** an NSE upper-band breakout on volume ≥ 1.5× the 20-day average, with rising delivery %, is far more trustworthy than a light-volume poke.
- **Volatility squeeze:** a Donchian breakout that coincides with a Bollinger Band squeeze (bands inside the channel, both narrow) flags genuine range expansion — high-quality breakouts.
- **Higher-timeframe alignment:** take daily-chart long breakouts only when the weekly channel is also trending up. Multi-timeframe agreement sharply reduces false signals.
- **Round numbers and prior structure:** in Indian indices, band breaks that also clear a psychological level (Nifty 24,000; Bank Nifty 50,000) or a prior swing high carry extra weight because they trigger stop and options-related flows.
- **Options open interest:** a Bank Nifty upper-band break that clears the strike with the largest call OI (a resistance shelf) can trigger call-writer unwinding and accelerate the move — TA+OI confluence.

## Pitfalls

- **The current-bar inclusion bug.** If your channel includes today's bar, "breakout" signals are structurally impossible or mistimed. Always signal off the *prior* n bars. This is the single most common coding error.
- **Whipsaw in ranges.** Pure breakout Donchian is a **trend system**; in sideways markets it produces a stream of small losses. Roughly 35-45% win rates are normal even when profitable. Without a trend/squeeze filter, rangebound months are painful.
- **Lookback over-optimisation.** Curve-fitting the "best" n to recent data yields a fragile system. Prefer round, robust values (20, 55) validated out-of-sample over a hyper-tuned 37-day channel.
- **Intrabar vs. close ambiguity.** Mixing intrabar entries in backtest with closing-break assumptions inflates results — be consistent, and remember intrabar fills incur more whipsaw and slippage.
- **Ignoring costs and gaps.** Many small trades mean brokerage, STT, and slippage add up; overnight gaps can blow through the channel stop, especially in single-stock futures on results/news.
- **Fading breakouts without a trend context.** Variant 3 (midline pullbacks) works only *with* the trend; using the midline to fade a strong breakout in the wrong direction is a classic beginner loss.
- **Edge decay.** Like all classic breakout methods, unfiltered Donchian breakouts have weakened since the 1990s as markets grew choppier and counter-trend algos proliferated. Modern robustness comes from filters and volatility adaptation, not from the raw rule alone.

## Interview-ready summary

The Donchian channel — highest high and lowest low over the last *n* bars, with a midline — is Richard Donchian's foundational trend-following tool and the root of the Turtle system. Its core insight: **a new n-bar extreme is objective information** that supply/demand has shifted and no overhead sellers remain. It powers a **family of systems**: (1) pure **breakout** — buy a close above the prior-n upper band, sell below the lower band, exit on a shorter opposite channel; (2) an **exit-only trailing stop** — enter by any method and trail with the n-bar low; (3) a **midline pullback** system that buys dips to the middle band *in a confirmed uptrend*; and (4) **volatility-adaptive/filtered** breakouts that add a 200-day trend filter, a squeeze filter, and an ATR buffer to cut whipsaw. Use asymmetric lengths (e.g., 20-in/10-out or 55-in/20-out), always signal off the *prior* n bars (never include the current bar), prefer closing breaks, size positions so the ATR/opposite-band stop equals ~1% of equity, and trail winners with the exit channel. Worked on Bank Nifty (₹15/point), a 20/10 breakout at 48,150 with a 2×ATR stop at 47,110 trailing to a 49,500 exit nets ~₹20,250 per lot on a clean trend, against defined −₹15,600 false-breakout losses. Be honest: it is a trend system with a ~40% win rate that whipsaws in ranges and whose raw parameters have decayed — the durable edge is the *architecture* (objective breakouts + volatility-scaled risk + trend filtering), not any magic lookback.
