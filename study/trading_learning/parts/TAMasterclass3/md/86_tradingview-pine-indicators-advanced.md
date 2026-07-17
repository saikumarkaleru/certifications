# TradingView Pine: Advanced Indicators

## What it is and the logic

Pine Script is TradingView's domain-specific language for writing custom indicators, strategies, screeners (via `request.*`), and alerts. Most traders never leave the built-in library; the ones who build an *edge* on TradingView write their own tools — multi-timeframe confluence dashboards, volume-profile overlays, custom regime filters, and precise alert engines wired to their exact rules. This chapter assumes you already know Pine basics (a `study`/`indicator` header, `plot`, simple `ta.*` calls) and goes into the *advanced* machinery: the execution model, higher-timeframe data without repainting, arrays and matrices, tables for on-chart dashboards, sessions and India-specific time handling, `request.security` pitfalls, and writing alerts that fire on *your* logic rather than a canned crossover.

The mental model that unlocks advanced Pine: **Pine runs your whole script once per bar, left to right, on every historical bar and then on each real-time tick.** A variable declared with `var` persists across bars; everything else is recomputed each bar. Series like `close` are not single numbers but the whole history indexed by bar — `close[1]` is the previous bar's close. Almost every advanced bug (repainting, look-ahead, wrong alerts) comes from misunderstanding *when* code runs and *what data was available* at that moment. Get the execution model right and the rest is library knowledge.

We target **Pine v6** (the current version in 2026) and an Indian context: NSE symbols, IST sessions, Nifty/Bank Nifty, and F&O-aware timing.

## Construction, rules, and settings

### The execution model and repainting

A script that "repaints" shows different signals on historical bars than it did in real time — an indicator that looks psychic in the past and disappoints live. The three main causes and their fixes:

| Cause | What happens | Fix |
|---|---|---|
| Using a higher-timeframe value that isn't closed | HTF bar updates intrabar, so the plotted value shifts | request with `lookahead_off` and offset the series, or gate on `barstate.isconfirmed` |
| Signals that use the *current, unclosed* bar | Real-time bar's high/low/close change tick by tick | Evaluate signals on `close[1]`/confirmed bars, or plot with a 1-bar offset |
| `request.security(..., lookahead=barmerge.lookahead_on)` | Pulls future HTF data into the past | Never use `lookahead_on` for trading logic |

Rule of thumb: if a signal must be *actionable*, compute it on **confirmed** data. `barstate.isconfirmed` is true only on the final tick of a bar; guarding alerts with it prevents a signal that appears then vanishes.

### Correct multi-timeframe data

The idiomatic, non-repainting way to fetch a higher-timeframe series in v6:

```pine
//@version=6
indicator("MTF EMA (safe)", overlay=true)
htf = input.timeframe("60", "Higher timeframe")
len = input.int(50, "EMA length")

// compute the HTF EMA inside the request, ask for confirmed values only
htfEma = request.security(syminfo.tickerid, htf, ta.ema(close, len)[barstate.isrealtime ? 1 : 0],
                          lookahead = barmerge.lookahead_off)
plot(htfEma, "HTF EMA", color.orange, 2)
```

The `[1]` shift during real-time (and `lookahead_off`) guarantees you only ever read a *closed* HTF bar — the value you plot on history is the value you would have had live. This single pattern eliminates the most common source of "my indicator lied to me."

### Arrays, matrices, and `var`

Advanced indicators keep state. Examples: storing the last N swing highs to draw a dynamic supply zone, or accumulating volume by price for a session volume profile.

```pine
var float[] swingHighs = array.new_float()
ph = ta.pivothigh(5, 5)
if not na(ph)
    array.push(swingHighs, ph)
    if array.size(swingHighs) > 10
        array.shift(swingHighs)          // keep only the last 10
```

`var` means `swingHighs` is created once and survives across bars; without `var` it would reset every bar and store nothing. Matrices (`matrix.new`) and, in v6, **maps** (`map.new<string,float>`) let you build genuinely stateful tools — a rolling correlation matrix across Nifty constituents, or a keyed store of per-strike open interest.

### Tables: on-chart dashboards

Tables float in a fixed screen position regardless of scroll/zoom — ideal for a confluence dashboard.

```pine
var table dash = table.new(position.top_right, 2, 4, border_width=1)
if barstate.islast
    table.cell(dash, 0, 0, "RSI",  text_color=color.white)
    table.cell(dash, 1, 0, str.tostring(ta.rsi(close,14), "#.0"))
    table.cell(dash, 0, 1, "ADX",  text_color=color.white)
    table.cell(dash, 1, 1, str.tostring(adxValue, "#.0"))
```

Guarding table writes with `barstate.islast` means you draw the dashboard only on the newest bar, saving computation.

### Sessions and India time

NSE cash trades 09:15–15:30 IST; F&O the same. Pine's session strings and the `"Asia/Kolkata"` timezone let you flag the opening range, avoid the illiquid last minutes, or restrict signals to a window:

```pine
inSession = not na(time("D", "0915-1530", "Asia/Kolkata"))
orbEnd    = not na(time("D", "0915-0930", "Asia/Kolkata"))  // opening 15-min range
```

For an **opening-range breakout** on Bank Nifty you would accumulate the high/low during `orbEnd`, then arm a breakout only while `inSession` and before, say, 14:45 to avoid the expiry-day close chaos.

## Worked India example: a Nifty MTF confluence + ORB alert tool

Let us build a single indicator that (a) shows daily-trend bias from a higher timeframe, (b) marks the opening range, (c) fires a clean, non-repainting alert on a Bank Nifty opening-range breakout that agrees with the higher-timeframe bias.

```pine
//@version=6
indicator("BNF ORB + MTF bias", overlay=true, max_lines_count=100)

// --- inputs ---
biasTf   = input.timeframe("D",  "Bias timeframe")
emaLen   = input.int(20, "Bias EMA")
buffTk   = input.float(10, "Breakout buffer (points)")

// --- higher-timeframe bias, non-repainting ---
biasEma = request.security(syminfo.tickerid, biasTf, ta.ema(close, emaLen)[1],
                           lookahead = barmerge.lookahead_off)
bullBias = close > biasEma
bg = bullBias ? color.new(color.green, 90) : color.new(color.red, 90)
bgcolor(bg)

// --- opening range (first 15 min, IST) ---
inOR   = not na(time("D", "0915-0930", "Asia/Kolkata"))
newDay = ta.change(time("D")) != 0
var float orH = na
var float orL = na
if newDay
    orH := na
    orL := na
if inOR
    orH := na(orH) ? high : math.max(orH, high)
    orL := na(orL) ? low  : math.min(orL, low)
plot(orH, "OR High", color.teal, 1, plot.style_linebr)
plot(orL, "OR Low",  color.maroon, 1, plot.style_linebr)

// --- breakout logic on CONFIRMED bars only ---
afterOR   = not inOR and not na(orH)
longBrk   = afterOR and bullBias and close > orH + buffTk
shortBrk  = afterOR and not bullBias and close < orL - buffTk

// fire once per day per direction
var bool tookLong  = false
var bool tookShort = false
if newDay
    tookLong  := false
    tookShort := false

longSig  = longBrk  and not tookLong  and barstate.isconfirmed
shortSig = shortBrk and not tookShort and barstate.isconfirmed
if longSig
    tookLong := true
if shortSig
    tookShort := true

plotshape(longSig,  "Long",  shape.triangleup,   location.belowbar, color.green, size=size.small)
plotshape(shortSig, "Short", shape.triangledown, location.abovebar, color.red,   size=size.small)

alertcondition(longSig,  "BNF ORB Long",  "BNF ORB long above OR high with daily bias")
alertcondition(shortSig, "BNF ORB Short", "BNF ORB short below OR low with daily bias")
```

**Reading it on a real day.** Suppose Bank Nifty opens 3 Feb 2026 at 51,200, and in the 09:15–09:30 window prints a high of 51,340 and low of 51,090 — that is the opening range. The daily EMA(20) sits at 50,700, so `bullBias` is true and the background tints green. At 10:12 a 5-minute candle *closes* at 51,362 — above 51,340 + 10-point buffer — with `barstate.isconfirmed` true. `longSig` fires exactly once; the green triangle prints and the alert dispatches. Because we gated on the confirmed close and the flag prevents re-firing, you get one clean, actionable signal, not a flickering repaint. A trader takes long ~51,362, stop below the OR low (51,090) or a tighter 51,300, target the prior-day high or a 1.5–2R multiple.

This one script fuses three of the volume's themes — higher-timeframe context, session/opening-range structure, and disciplined alerting — into a tool you actually trade from.

## How to trade it: entry, stop, target, management

- **Entry:** on the alert (confirmed breakout close beyond OR ± buffer) *with* HTF bias agreeing. The bias filter is what stops you from buying every failed breakout in a down-trending tape.
- **Stop:** opposite side of the opening range, or a fixed points/ATR stop — Bank Nifty moves fast, so size for the *rupee* risk of that distance, not a fixed lot count.
- **Target:** prior-day high/low, a round number, or an R-multiple; trail behind 5-min swings once in profit.
- **Management:** disable new entries after ~14:45 (avoid the illiquid, gappy close, especially on weekly-expiry days); one trade per direction per day via the flags. For F&O, translate the spot breakout into the appropriate ATM/slightly-ITM option or a debit spread to cap theta and gap risk.

## Confluence

The Pine tool becomes reliable only *with* confluence. Layer the ORB breakout with: (1) the daily-bias EMA already built in; (2) India VIX regime — skip breakouts when VIX is spiking into event risk; (3) volume expansion on the breakout bar (`volume > ta.sma(volume, 20)`); (4) breadth or Nifty agreeing with Bank Nifty; (5) not immediately into a known level (previous-day high, VWAP, a big option-OI strike). Add these as extra boolean gates before `longSig`. The best Pine indicators do not add signals — they *subtract* the ones that lack confluence.

## Pitfalls

- **Repainting via `lookahead_on`** — never use it for anything you trade; it back-dates future data.
- **Signalling on the live bar** — the current bar's `close` changes every tick; a signal can appear then vanish. Gate on `barstate.isconfirmed` or use `close[1]`.
- **Alerts that re-fire** — without a `var` flag, an `alertcondition` that stays true across bars floods you. Latch it per day/direction as shown.
- **`request.security` timeframe soup** — requesting a *lower* timeframe from a higher chart, or mismatched sessions, gives garbage; keep requests same-or-higher and confirmed.
- **`max_lines_count` / `max_labels_count`** — drawing objects accumulate and hit limits; delete old ones (`line.delete`) or cap counts.
- **Timezone assumptions** — hard-coding exchange time without `"Asia/Kolkata"` breaks when the viewer's chart timezone differs; always specify IST for NSE sessions.
- **Strategy vs indicator backtests** — TradingView's `strategy` backtester defaults can fill on the signal bar and ignore slippage; set `calc_on_order_fills`, realistic `commission` and `slippage`, and remember the earlier chapter's warnings — the built-in report is optimistic by default.
- **Free-plan limits** — alert counts, historical bars, and `request.security` calls are capped; heavy dashboards may need a paid plan.

## Interview-ready summary

Advanced Pine Script mastery rests on the execution model: the script runs once per bar left-to-right, `var` persists state, series are indexed histories, and the current bar is *unconfirmed* until its last tick. The headline skill is writing **non-repainting** tools — fetch higher-timeframe data with `request.security(..., lookahead=barmerge.lookahead_off)` and a real-time `[1]` shift, and fire signals only on `barstate.isconfirmed` so what you see on history equals what you'd have seen live. Beyond that: arrays, matrices, and maps for stateful indicators (swing stores, volume profiles, OI maps); tables for fixed-position dashboards drawn on `barstate.islast`; and session/timezone handling with `"Asia/Kolkata"` for NSE hours and opening-range logic. The worked Bank Nifty tool fuses a daily-EMA bias filter, a 15-minute opening range, and a latched, confirmed breakout alert into one tradeable indicator — entry on the confirmed breakout with bias agreement, stop at the opposite OR edge, target at an R-multiple, and no new trades near the volatile expiry-day close. The recurring pitfalls — `lookahead_on`, live-bar signals, re-firing alerts, timezone bugs, and the optimistic default backtester — all trace back to the same discipline that governs every quantitative method in this volume: only ever act on information that was genuinely available at the moment of decision.
