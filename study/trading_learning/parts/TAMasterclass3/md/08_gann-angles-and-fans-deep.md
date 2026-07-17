# Gann Angles & Fans (Deep)

Gann angles are the part of W. D. Gann's work that survives most cleanly into the modern charting era, because they are, at bottom, a statement about **rate of change**: a trend is healthy only so long as price advances a fixed number of units of price per unit of time. The famous 1×1 line — one point per one bar — and its family of steeper and shallower rays are simply constant-slope trendlines whose slope is *anchored to the scaling of the chart itself* rather than drawn freehand. This chapter goes past the textbook "45-degree line" cliché into the mechanics that actually matter on Indian charts: how to fix the price-per-bar unit so the angles mean something on Nifty versus Bank Nifty versus a ₹300 stock, how the fan of angles behaves as support becomes resistance, and how to trade the 1×1 with real levels.

## What they are and the logic

A Gann angle is a line of **constant price-per-time slope** drawn from a significant pivot. The reference angle is the **1×1**, defined as one unit of price for one unit of time. If the chart is scaled so that one bar of horizontal distance equals one unit of price of vertical distance, the 1×1 renders at a visual 45°. That visual 45° is incidental; the *definition* is the slope, one price unit per one time unit.

From the pivot, Gann drew a whole fan:

| Angle name | Price × Time | Slope (price per bar) | Meaning |
|---|---|---|---|
| 1×8 | 1 price per 8 bars | 0.125 | very shallow — weak/slow trend |
| 1×4 | 1 per 4 | 0.25 | shallow |
| 1×3 | 1 per 3 | 0.333 | shallow |
| 1×2 | 1 per 2 | 0.5 | below-normal |
| **1×1** | **1 per 1** | **1.0** | **balanced / normal trend** |
| 2×1 | 2 per 1 | 2.0 | steep — strong trend |
| 3×1 | 3 per 1 | 3.0 | very steep |
| 4×1 | 4 per 1 | 4.0 | steep/unsustainable |
| 8×1 | 8 per 1 | 8.0 | near-vertical — blow-off |

The governing idea Gann called **balance between price and time.** When price rises exactly along the 1×1, price and time are in equilibrium — the market is advancing at its "natural" rate. Above the 1×1 (steeper, riding the 2×1 or 3×1) the market is *ahead of time* — strong but overextended and prone to correct back to the 1×1. Below the 1×1 (price has slipped under the 1×1 onto the 1×2) the market is *behind time* — weak, and the 1×1 that was support has become resistance. The single most important tradable proposition in the whole method is: **as long as price holds above the rising 1×1, the uptrend is intact; the first close decisively below the 1×1 is the first objective sign the trend has changed character.**

## Construction, rules and settings

### The scaling problem — the thing everyone gets wrong

A 1×1 line is meaningless until you define what "one unit of price" and "one unit of time" are. On a chart of a ₹50 stock, one point per bar is a violent slope; on Bank Nifty at 48,000, one point per bar is a flat line you'd never see. So the practitioner must choose a **price-per-bar unit** appropriate to the instrument. This is the equivalent of the Square-of-Nine pivot choice: get it wrong and every angle is noise.

Two disciplined ways to set it:

1. **ATR-based (recommended, objective).** Set the 1×1 slope to a fraction of the instrument's Average True Range per bar — commonly the 1×1 = 1 × ATR(14) per bar, so the "natural" trend advances roughly one ATR each bar. This auto-scales across instruments and is defensible in an interview.

2. **Range-based / Gann's own approach.** Divide a significant prior *range* (high minus low of an important swing) by the *number of bars* that swing took; that price-per-bar becomes your 1×1 unit. This ties the angle to the market's own demonstrated speed.

Whatever you choose, **fix it and keep it constant** for that instrument and timeframe. If you re-scale to make the line "fit," you are drawing freehand trendlines and calling them Gann.

### Reference units for Indian instruments

Rough, sane starting points for a **daily** chart (adjust to live ATR):

| Instrument | Typical daily ATR | Suggested 1×1 unit (price per bar) |
|---|---|---|
| Nifty 50 | ~180–250 pts | 200 pts/bar |
| Bank Nifty | ~500–800 pts | 600 pts/bar |
| Fin Nifty | ~250–350 pts | 300 pts/bar |
| Reliance | ~₹22–30 | ₹25/bar |
| A ₹300 midcap | ~₹8–12 | ₹10/bar |
| USDINR | ~₹0.20–0.35 | ₹0.25/bar |
| MCX Crude (₹/bbl) | ~₹120–180 | ₹150/bar |

With the unit fixed, the 2×1 is simply twice that slope, the 1×2 half of it, and so on.

### Tools

TradingView ships a **Gann Fan** and a **Gann Box** under the drawing tools. The critical setting is the box's price/time proportion — TradingView lets you fix the number of bars and the price range the box spans, which *is* your scaling choice. Set the box so its diagonal (the 1×1) matches your ATR- or range-derived unit, and the fan's other rays fall out automatically. Chartink can screen for "price crossed below its N-day rising-slope line" as a crude proxy, but the drawing is done on TradingView.

## Worked India example — Nifty 1×1 on the daily

Nifty bottoms at a decisive swing low of **21,800** on day 0. We fix the 1×1 unit at **200 points per bar** (roughly one daily ATR). The rising fan from that low:

| Bars elapsed | 1×2 (100/bar) | 1×1 (200/bar) | 2×1 (400/bar) |
|---|---|---|---|
| 0 | 21,800 | 21,800 | 21,800 |
| 5 | 22,300 | 22,800 | 23,800 |
| 10 | 22,800 | 23,800 | 25,800 |
| 15 | 23,300 | 24,800 | 27,800 |
| 20 | 23,800 | 25,800 | 29,800 |

Read this as a decision framework, not a forecast:

- If, ten bars after the low, Nifty is trading at **23,900**, it is *above* the 1×1 (23,800) — a healthy, on-schedule uptrend. The 1×1 at 23,800 is now dynamic support; a dip that holds it is a buy-the-pullback opportunity with a tight, well-defined invalidation.
- If instead Nifty is at **24,900** — riding the 2×1 (25,800 not yet, but well above 1×1) — the trend is *ahead of time*, strong but stretched. Gann's expectation is a correction *back toward the 1×1*, i.e. toward ~23,800, not necessarily a full trend reversal. You'd trail stops, not add aggressively.
- If Nifty has slipped to **22,750**, below the 1×1 (23,800) and hugging the 1×2 (22,800), the trend is *behind time* — weak. The former-support 1×1 now caps rallies as resistance. You stand aside or look short into the 1×1 from below.

The magic is that these are *dynamic, sloping* levels — they rise every bar — so unlike a horizontal support they tell you the trend's *health over time*, not just a static price.

## Worked India example — Bank Nifty fan flip

Bank Nifty tops at **48,500** and rolls over; we draw a *descending* fan from that high with the 1×1 unit at **600 points/bar**.

| Bars from high | 1×1 down (600/bar) | 1×2 down (300/bar) |
|---|---|---|
| 0 | 48,500 | 48,500 |
| 4 | 46,100 | 47,300 |
| 8 | 43,700 | 46,100 |
| 12 | 41,300 | 44,900 |

Eight bars in, the falling 1×1 sits at **43,700.** If Bank Nifty is trading at 43,500, it is *below* the descending 1×1 — the downtrend is on schedule and the 1×1 is resistance overhead. A pullback into 43,700 that fails is a textbook short with a stop above the 1×2 (46,100 region is far; a tighter structural stop is used intraday). The **line that was support in the up-fan becomes resistance in the down-fan** — this "old support becomes resistance across the fan flip" is the recurring Gann-angle pattern worth internalising.

## How to trade it

**Setup A — Buy the 1×1 pullback (trend continuation).**
- Context: clean rising 1×1 from a valid pivot; price has been holding above it.
- Entry: price pulls back to the rising 1×1 and prints a rejection/reversal candle *on the line*.
- Stop: one 1×2-line's distance below, or below the pivot-swing structure — objective because the geometry defines it.
- Target: the 2×1 line above, or a prior high; trail along the 1×1 as it rises.

**Setup B — 1×1 break (trend change).**
- Signal: first *decisive daily close* below a long-respected rising 1×1.
- Action: exit longs; consider shorts on the retest of the 1×1 from below (the fan flip).
- Stop: back above the 1×1.
- This is the highest-value Gann-angle signal — it front-runs the horizontal-trendline break that everyone else waits for, because the sloping 1×1 is usually breached earlier.

**Setup C — Angle-to-angle rotation.**
- When price falls off the 2×1, the *next* support is the 1×1, then the 1×2. Trade the rotation from one ray to the next: exit/trim at each broken ray, target the next ray down.

**Management and sizing.** Because each ray is a defined line, your stop is never arbitrary — it is "the next ray" or "back through the ray just reclaimed." On the Nifty Setup A, buying the 1×1 pullback at ~23,800 with a stop near the 1×2 at ~22,800 risks ~1,000 points on the index; that is too wide for a tight trader, so you'd use an intraday structural stop (below the day's swing) instead and treat the 1×2 as the *thesis-invalidation* level rather than the money-stop. The angle defines the thesis; your risk rule defines the size.

### F&O integration

The 1×1 break pairs naturally with **options.** When Nifty closes below a long-standing rising 1×1, buying a modest put spread (or rolling long-delta positions off) expresses the "trend character has changed" thesis with defined risk, while you wait for the fan-flip retest to add. Conversely, holding above a rising 1×1 supports staying in covered-call or bull-put-spread structures. On Bank Nifty's steeper ATR, the 1×1 crossing often coincides with a shift in the option skew — worth checking OI as confirmation.

## Confluence

- **Horizontal S/R + the 1×1:** when the rising 1×1 arrives at the same price as a prior horizontal support on the same day, that intersection is a high-odds bounce/decision point.
- **Fibonacci retracement + 1×1:** a 1×1 that coincides with the 50%/61.8% retracement of the prior swing is a premium long zone.
- **Square-of-Nine levels + angles:** a Gann *price* level (previous chapter) sitting on the rising 1×1 combines price geometry with rate-of-change geometry — a core Gann confluence.
- **Moving averages:** the 1×1 crossing the 50-DMA at the same spot doubles the significance for swing traders.
- **Volume/OI:** a 1×1 break on expanding volume or a clear OI shift is far more trustworthy than a quiet drift through it.

## Pitfalls

- **Unstable scaling.** The number-one failure: re-scaling the chart or the Gann box until the angle "fits" recent bars. That is hindsight trendline-drawing. Fix the price-per-bar unit by an objective rule (ATR or a chosen prior range) *before* drawing, and never touch it.
- **Log vs linear.** Gann angles are inherently *arithmetic* (constant points per bar). On a log-scaled chart they curve and the whole framework distorts. Use **linear** price scaling for Gann angles, always.
- **Instrument-blind slopes.** A 1×1 unit that works on Nifty is nonsense on a ₹200 stock. Re-derive the unit for every instrument.
- **Confusing steepness with strength forever.** A market riding the 2×1 is strong *and* overextended; the tool's own logic says expect reversion to the 1×1. Don't mistake the steep ray for a promise it continues.
- **Over-fanning.** Drawing all nine rays clutters the chart and guarantees price is "near a Gann angle" at all times. Keep the 1×2, 1×1, and 2×1 for most work; add others only with reason.
- **Ignoring the pivot's validity.** Like the Square of Nine, everything hangs on anchoring to a *respected* swing pivot. A fan from a meaningless low is a meaningless fan.

## Interview-ready summary

Gann angles are constant price-per-time trendlines drawn from a significant pivot, the reference being the 1×1 — one unit of price per one unit of time — with steeper rays (2×1, 3×1) and shallower rays (1×2, 1×4) forming a fan. The core proposition is *balance between price and time*: price holding above a rising 1×1 signals a healthy on-schedule trend, price riding the steeper 2×1 signals strength but overextension prone to revert to the 1×1, and the first decisive close below the 1×1 is the earliest objective sign the trend's character has changed — a signal that front-runs the horizontal-trendline break. The make-or-break setup step is *scaling*: the 1×1's price-per-bar unit must be fixed objectively (an ATR-per-bar or a chosen prior-range-per-bar), instrument by instrument — 200 pts/bar on Nifty, ~600 on Bank Nifty, ~₹25 on Reliance — on a **linear** (never log) chart, and never re-fitted. You trade the 1×1 pullback for continuation, the 1×1 break plus fan-flip retest for reversal, and rotations from ray to ray, with stops defined by the next ray. The edge concentrates in confluence — 1×1 meeting horizontal S/R, a Fibonacci level, a Square-of-Nine price, or a moving average, confirmed by volume/OI. The honest caveats are that scaling is subjective and trivially curve-fit, log charts break the method, and slopes must be re-derived per instrument. Disciplined, the 1×1 is one of the most robust rate-of-change trend filters available for Indian indices, stocks and MCX.
