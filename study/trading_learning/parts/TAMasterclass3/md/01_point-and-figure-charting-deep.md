# Point & Figure Charting (Deep)

Point & Figure (P&F) is the oldest surviving Western charting method — older than the bar chart, older than the candle in Western usage. It strips price of two things almost every other chart obsesses over: **time** and **noise**. There is no fixed x-axis of trading days, no gaps, no doji shadows, no volume bars. A P&F chart plots only *meaningful price movement* and ignores everything else. For an Indian trader drowning in the intraday chop of Nifty and Bank Nifty, that filtering property is not a gimmick — it is the whole point. This chapter builds P&F from first principles for the 2026 Indian market, with rupee-level examples, TradingView/Chartink settings, and a trading framework. The *patterns and price objectives* (counts) get their own dedicated chapter next; here we master the chart itself.

## What it is and the logic

A P&F chart is a grid of **X-columns** and **O-columns**. X's represent rising prices; O's represent falling prices. Each X or O is a "box" worth a fixed number of price points — the **box size**. A column keeps growing in its own direction as long as price keeps moving that way by at least one box. Price only shifts to a *new column of the opposite type* when it reverses by a defined amount — the **reversal**, almost always 3 boxes. That is why the standard method is called **3-box reversal P&F**.

The logic is auction-driven. An X-column says buyers are in control and are willing to pay progressively higher prices. An O-column says sellers are in control. Because a reversal requires price to move *against* the current column by three boxes before a single mark is made in the new direction, small wiggles are structurally invisible. A 40-point pullback in Nifty when the box size is 20 points and reversal is 3 is only 2 boxes — not enough. Nothing changes on the chart. The trend column simply pauses. This is the mechanical embodiment of "don't react to noise."

Two consequences follow immediately, and they define the entire method:

1. **Time is destroyed.** A P&F column can represent five minutes or five weeks. A quiet, ranging Nifty in a festival-thinned October can produce almost no new boxes for days, while a budget-day crash prints a long O-column in one session. The chart compresses boring periods and expands violent ones. You are looking at *effort*, not calendar.
2. **Support and resistance become brutally clean.** Because every column sits in a tidy grid, horizontal congestion — the repeated tug-of-war at a price — shows up as walls of X's and O's at the same row. These walls are the supply/demand levels that P&F traders trade against, and they are far less ambiguous than the fuzzy "zones" you eyeball on a candle chart.

## Construction, rules and settings

### The three parameters

Every P&F chart is defined by three numbers:

| Parameter | What it controls | Typical Indian choice |
|---|---|---|
| **Box size** | Points (or %) per box — the sensitivity | Nifty: 20–25 pts; Bank Nifty: 50–100 pts; a ₹500 stock: ₹5 |
| **Reversal** | Boxes needed to start a new column | 3 (standard) |
| **Scaling** | Fixed points, ATR-based, percentage, or log | % or ATR for wide universes; fixed for a single index |

Box size is the master dial. Too small and the chart fills with columns and gives back its noise-immunity; too large and it reverses so rarely that signals arrive late. A widely used starting rule is a percentage scale where box size scales with price, so a ₹100 stock and a ₹3,000 stock are treated on comparable sensitivity. Stockcharts-style **traditional scaling** uses tiered box sizes (e.g. ₹0.50 boxes under ₹5, ₹1 boxes ₹5–20, and larger boxes higher up). For a single instrument you know well — say you only trade Nifty futures — a **fixed** box of 20 points is cleaner and more intuitive.

### The core plotting rules (3-box reversal)

Assume box size **B** and reversal **R = 3**. You are in an X-column at the moment.

- **Extend the X-column:** if price rises by at least one full box above the highest X, add X's up to the new level. Only whole boxes count; a partial box is ignored until it is completed.
- **Reverse to O:** if price *falls* by **R × B** (3 boxes) from the highest X, you abandon the X-column. Move **one column to the right**, drop **one row down** from the top X, and print three (or more) O's downward to the reversal level.
- The reverse rules apply symmetrically for O-columns.

Two subtleties that trip up beginners:

- **The one-box offset on reversal.** When you switch from X's to O's, the first O is plotted one box *below* the top X, never at the same row. This is why an X-column and the neighbouring O-column never share their extreme box. It keeps columns readable and preserves the count arithmetic used later for targets.
- **High-Low vs Close-only.** Classic P&F uses the day's **high** to extend X's and the day's **low** to extend O's (the "high-low" method). A stricter variant uses only the **close**. High-low reacts faster and is standard on most platforms; close-only is quieter. For NSE data, high-low on daily bars is the default and what the worked example below uses.

### Log vs arithmetic scaling

For instruments that move in wide ranges over years — think a stock that ran from ₹200 to ₹2,000 — **percentage/log scaling** keeps each box a constant *percentage* move, so a box near ₹200 is smaller in rupees than a box near ₹2,000. This prevents the chart from becoming absurdly tall and keeps the sensitivity honest across the whole range. For index intraday or swing work over months, arithmetic (fixed-point) is fine and easier to read.

### Platform settings (TradingView & Chartink)

On **TradingView**, choose the "Point & Figure" chart type, then set: *Style* = HLC or Close, *Box size assignment* = Traditional / ATR / Fixed / Percentage, *Reversal amount* = 3. For Nifty spot on a daily basis, Fixed box 20, reversal 3, HLC is a solid default. TradingView's **ATR box** (e.g. 14-period ATR) auto-adapts the box to recent volatility — useful when you flip between a calm and a violent regime without re-tuning. **Chartink** doesn't render true P&F but you can screen for the *signals* P&F produces (double-top breakouts) by encoding the equivalent price logic. Most Indian P&F practitioners keep the chart on Trading.com/TradingView and use Chartink only for the initial universe scan.

## Worked India example (levels and ₹)

Let's build a Nifty daily P&F by hand. **Box size = 20 points, reversal = 3 (so a reversal needs 60 points), high-low method.** Boxes align to multiples of 20 (…24,500 / 24,520 / 24,540…). Suppose Nifty spot trades through this sequence of daily highs and lows:

| Day | High | Low | Action |
|---|---|---|---|
| 1 | 24,565 | 24,510 | Start X-column; fill X's to 24,560 |
| 2 | 24,640 | 24,580 | High 24,640 → extend X's to 24,640 |
| 3 | 24,690 | 24,630 | Extend X's to 24,680 |
| 4 | 24,700 | 24,600 | Low only pulls back 80 pts from 24,680 top? No new high box; check reversal |
| 5 | 24,655 | 24,590 | Low 24,590: fall from 24,680 = 90 pts = 4 boxes ≥ 60 → **reverse to O** |
| 6 | 24,600 | 24,505 | Extend O's down to 24,520 |
| 7 | 24,560 | 24,500 | Extend O's to 24,500 |
| 8 | 24,640 | 24,540 | High 24,640: rise from 24,500 low = 140 pts = 7 boxes ≥ 60 → **reverse to X** |

Reading it: the first X-column ran 24,560→24,680 (buyers pushing). On Day 5 sellers forced a 3-box reversal, printing an O-column from 24,660 down to 24,520 (the first O sits one box below the 24,680 top). On Day 7 that O-column bottomed at 24,500. On Day 8 buyers reversed it back into a fresh X-column starting at 24,520 and climbing to 24,640.

Now the *tradeable event*. Notice the first X-column topped at **24,680** and the O-column bottomed at **24,500**. If the new X-column climbs one box *above the previous X-column's top* — i.e. prints an X at **24,700** — that is a **Double-Top Buy signal**, P&F's most fundamental entry. Conversely, had the O-column dropped one box below a prior O-bottom, that's a **Double-Bottom Sell**. Here, a print at 24,700 says demand has overwhelmed the supply that capped the last rally at 24,680 — a clean, unambiguous breakout with no candle-wick ambiguity about whether it "really" broke.

For **Bank Nifty**, scale up: box 100, reversal 3 (300-point reversal) suits its ~50,000 level and larger daily range. A Bank Nifty O-column bottoming at 49,500 that later reverses and prints an X above the previous X-top at 50,600 gives the same double-top buy — but each box is ₹100 of index, so the structural moves are chunkier and the signals rarer and arguably more reliable.

## How to trade it

P&F entries are refreshingly rule-bound, which is exactly why systematic Indian traders like it.

**Entry.** The two workhorse signals are the **Double-Top Buy** (X exceeds the prior X-column high by one box) and **Double-Bottom Sell** (O breaks the prior O-column low by one box). Enter on the box that completes the breakout. In our Nifty example, buy Nifty futures (or the ATM/slightly-OTM call, or a bull call spread) the moment 24,700 prints. Because P&F ignores intraday noise, you are only acting on a level that already survived the 3-box filter.

**Stop.** The natural stop is *one box below the breakout column's origin* or below the most recent O-column low. For the 24,700 buy, a stop under the 24,500 O-bottom (or a tighter stop under the reversal box) is logical. Translate to points: risk ≈ 24,700 − 24,500 = 200 points on the wide stop, or ~80 points on the tight one. Size the position so that rupee risk = your per-trade risk budget. With Nifty lot 75 (2026), 80 points × 75 = ₹6,000 risk per lot — set lots accordingly.

**Target.** P&F provides its own objective via **counts** (horizontal and vertical), covered fully in the next chapter. As a preview: a vertical count multiplies the number of boxes in the breakout column by the box size and the reversal, then adds to the base. It gives a mechanical, non-discretionary target — one of P&F's biggest edges over eyeballed candle targets.

**Management.** Because the chart only updates on real movement, trade management is unusually calm. Trail your stop up to *one box below each successive O-column low* in an uptrend (the "bullish support line," a 45° line rising from the pattern low, is the classic trailing guide). Exit on the opposite signal — a Double-Bottom Sell — or when price breaks the bullish support trendline. There is nothing to do on quiet days; the chart simply doesn't move, which enforces patience.

**Position vs intraday.** P&F works on any timeframe *feed*. Feed it daily highs/lows for swing/positional trades (box 20–25 on Nifty). Feed it 1-minute or tick data with a small box (e.g. 5–10 points on Nifty) for intraday. Intraday P&F on Bank Nifty with a 20–30 point box is a genuinely popular Indian day-trading tool because it silences the vicious minute-to-minute whipsaw that shakes candle traders out.

## Confluence

P&F is strongest when its clean signals are stacked with independent evidence:

- **Trendlines on the P&F grid.** The **45° bullish support line** and **bearish resistance line** are drawn at exact 45 degrees from a column bottom/top across the boxes. A Double-Top Buy that occurs *above* a rising bullish support line is a far higher-quality signal than one fighting a falling resistance line. This internal trend filter is unique to P&F.
- **Relative strength P&F.** Plot the *ratio* of a stock to Nifty as its own P&F chart. A stock on a P&F buy signal whose RS chart is *also* on a P&F buy is a leadership setup — the backbone of P&F sector rotation.
- **Options OI.** Align a Nifty P&F Double-Top Buy at 24,700 with an OI-based resistance that has just been cleared (call writers unwinding above 24,700). Two unrelated methods pointing the same way.
- **Breadth / Bullish Percent Index.** The BPI — the percent of stocks in an index on a P&F buy signal — is itself a P&F chart of market breadth. A Nifty index buy signal while the Nifty BPI is rising off an oversold sub-30 level is a powerful confluence.

## Pitfalls

- **Box size is destiny.** The single most common mistake is a poorly chosen box. Too small on Bank Nifty and you get a "noisy" P&F that defeats the purpose; too large on a slow midcap and signals arrive after most of the move. Re-tune box size when volatility regime-shifts, or use ATR scaling to automate it.
- **Late by design.** The 3-box reversal that gives P&F its calm also means you never buy the exact low or sell the exact high. P&F is a *trend/breakout* tool, not a bottom-picker. Accept that it forfeits the first leg for the sake of avoiding false signals.
- **Whipsaws in tight ranges.** In a genuinely rangebound market, a small-box P&F can still produce a cluster of failing double-top/double-bottom signals as price ping-pongs across a congestion zone. The bullish/bearish trendline filter and demanding the signal occur on the correct side of the trend line cuts most of these.
- **High-low vs close confusion.** Mixing methods across charts gives inconsistent signals. Pick high-low (default) or close-only and stay consistent, especially when computing counts later.
- **Illiquidity distortion.** On thin NSE small-caps or far-month options, a single erratic print can trigger a false reversal. Prefer P&F on liquid instruments — Nifty, Bank Nifty, Fin Nifty, F&O stocks, MCX crude/gold/silver, USDINR — where the tape is dense enough that box moves are real.
- **Over-optimising in backtests.** Because there are only three knobs, it is tempting to curve-fit box/reversal to historical Nifty. Validate any tuned setting on out-of-sample data and across at least one bull and one bear regime.

## Interview-ready summary

Point & Figure charts price movement, not time: rising prices are stacked as **X-columns**, falling prices as **O-columns**, each mark worth a fixed **box size**, and price only jumps to a new opposite column after a **3-box reversal** — which mechanically filters out noise. There is no time axis, no gaps, no wicks. This makes support/resistance walls, trendlines (drawn at a strict 45°), and breakout signals unusually clean. The two primitive signals are the **Double-Top Buy** (an X exceeds the prior X-high by one box) and the **Double-Bottom Sell**. For Indian markets, sensible daily settings are box ≈ 20–25 points on Nifty and ≈ 50–100 on Bank Nifty with a 3-box reversal; ATR-based boxes adapt automatically across regimes. Its strengths are objective entries, self-generated price targets via counts, and forced patience; its weaknesses are lateness by design, sensitivity to box size, and vulnerability to whipsaw in tight ranges and illiquid names. Confluence with the P&F trendlines, relative-strength P&F, the Bullish Percent Index, and options OI turns it from a standalone signal generator into a robust decision framework. In one line: *P&F is the discipline of only reacting to price moves large enough to matter.*
