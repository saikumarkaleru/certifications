# Gann: The Square of Nine

W. D. Gann's Square of Nine is the most famous — and most misunderstood — tool in his kit. Traders either treat it as a mystical price oracle or dismiss it as numerology. The truth sits in between: it is a **geometric map that arranges numbers in a spiral so that price levels which share a fixed angular relationship line up along the same ray or ring.** Stripped of the astrology, what remains is a disciplined way to project support and resistance from a single significant price using the square-root relationship that governs the spiral. This chapter builds the Square from scratch, derives the actual formulas your calculator or Pine script needs, and then trades it on Nifty, Bank Nifty and a rupee-priced NSE stock with real levels.

## What it is and the logic

Picture the number 1 at the centre of a grid. Spiral the integers outward — 2, 3, 4, 5, 6, 7, 8, 9 forming the first ring around it, then 10 through 25 forming the second ring, and so on. Each complete loop around the centre adds two to the square root: the number directly "below" the centre after one full turn is 9 (√9 = 3), after two turns is 25 (√25 = 5), after three turns 49 (√49 = 7). These are the **odd squares**, and they fall on the same diagonal — the south-west axis — because one full 360° rotation of the spiral corresponds to adding 2 to the square root of the centre value.

That single fact is the engine of the whole tool. **Moving 360° around the spiral = adding 2 to the square root of the price.** Therefore moving 180° (half a turn) adds 1 to the square root; moving 90° (a quarter turn) adds 0.5; moving 45° (an eighth) adds 0.25; moving 15° adds 1/12. Every angular step is just an increment on the square-root axis. Price, in Gann's framework, does not move linearly — it moves in the square-root domain, and the Square of Nine is the device that translates angles into price and back.

Why should a market care about the square root of its own price? Gann's answer was that markets vibrate, and vibration frequency scales with the root of the quantity, the same way a pendulum's period scales with the root of its length or a planet's orbit with the 3/2 power of its radius (Kepler). Whether or not you accept the physics, the *empirical* claim you can test is narrower and honest: **levels spaced evenly on the square-root axis often act as support and resistance more reliably than levels spaced evenly in raw price.** That is a falsifiable statement, and on Indian indices it holds up often enough to be tradable when combined with structure — not as a standalone system.

## Construction, rules and settings

### The core formulas

You never need to draw the spiral by hand. Two formulas do everything.

To find the price that sits a given number of degrees away from a starting price:

```
Target = ( √(Start) ± degrees/180 )²
```

Here `degrees/180` is the number of *half-turns*. A 90° move uses 90/180 = 0.5; a full 360° move uses 2.0 (adding 2 to the root, the odd-square relationship); a 45° move uses 0.25.

To find the *angle* between any two prices — how far apart they sit on the wheel:

```
Degrees = ( √(PriceB) − √(PriceA) ) × 180
```

Take the result modulo 360 to locate it on the ring. Angles near 0/360, 90, 180, 270 (the "cardinal cross"), and 45, 135, 225, 315 (the "ordinal cross" or "square-of-two" diagonals) are the ones Gann weighted most heavily.

### The angle table you actually use

For a chosen pivot price P, the projected levels are computed by stepping the square root and re-squaring. The standard fan of levels:

| Angle from pivot | Root increment | Formula | Meaning |
|---|---|---|---|
| +45° | +0.25 | (√P + 0.25)² | first minor resistance |
| +90° | +0.50 | (√P + 0.50)² | first major resistance |
| +135° | +0.75 | (√P + 0.75)² | minor resistance |
| +180° | +1.00 | (√P + 1.00)² | major (opposition) resistance |
| +270° | +1.50 | (√P + 1.50)² | strong resistance |
| +360° | +2.00 | (√P + 2.00)² | full-cycle resistance |
| −45° | −0.25 | (√P − 0.25)² | first minor support |
| −90° | −0.50 | (√P − 0.50)² | first major support |
| −180° | −1.00 | (√P − 1.00)² | major support |
| −360° | −2.00 | (√P − 2.00)² | full-cycle support |

The 90° and 180° levels are the workhorses. 45° increments give you a denser grid for intraday; 90° increments suit swing trading; 180°/360° suit positional levels.

### Choosing the pivot — the make-or-break decision

The Square is only as good as its anchor. Garbage pivot, garbage levels. Use one of:

- A **significant swing high or low** on the relevant timeframe (the most common and most defensible choice).
- The **prior day's close or the day's open** for intraday work.
- An **all-time high or a major cycle low** for positional projection.

The pivot must be a price the market actually *respected*. Anchoring off a random midday tick produces meaningless numbers. This is the single biggest source of "Gann doesn't work" complaints: the user anchored badly.

### Settings and tools

On TradingView there is no native Square of Nine, so most Indian traders use a **Chartink screener plus a standalone Square-of-Nine calculator** (many free web calculators exist) or a short Pine/Python script. The calculation is trivial — a spreadsheet with the two formulas above is enough. What matters is discipline in pivot selection and in *only* acting on levels that coincide with visible structure.

## Worked India example — Nifty 50

Suppose Nifty makes a clean, respected swing low at **21,800** (a level the index bounced from on strong volume — a proper pivot, not a random tick). We want the upside resistance ladder and the downside support ladder.

√21,800 = 147.648.

Now step the root:

| Angle | Root | Squared → level | Rounded |
|---|---|---|---|
| +45° | 147.898 | 21,873.9 | **21,874** |
| +90° | 148.148 | 21,947.8 | **21,948** |
| +135° | 148.398 | 22,022.0 | **22,022** |
| +180° | 148.648 | 22,096.2 | **22,096** |
| +270° | 149.148 | 22,245.1 | **22,245** |
| +360° | 149.648 | 22,394.5 | **22,395** |

Downside, subtracting from the root:

| Angle | Root | Squared → level | Rounded |
|---|---|---|---|
| −45° | 147.398 | 21,726.2 | **21,726** |
| −90° | 147.148 | 21,652.5 | **21,653** |
| −180° | 146.648 | 21,505.6 | **21,506** |
| −360° | 145.648 | 21,213.4 | **21,213** |

So from the 21,800 pivot, the tool says: first resistance shelf near **21,948** (90°), a stronger one at **22,096** (180°, the opposition point), then **22,245** and **22,395**. Downside, the first real support is **21,653** (90°) and major support **21,506** (180°).

Now overlay reality. If in the following sessions Nifty rallies and stalls three times in the 21,945–21,955 zone before breaking, the 90° level did its job — and because you had it marked in advance, you were selling into resistance while others chased. If it then accelerates and the 22,090–22,100 zone caps the move, the 180° opposition level is confirming. The Square gave you a *pre-computed ladder*; the tape tells you which rungs are live.

## Worked India example — Bank Nifty and a stock

Bank Nifty pivots off a swing high at **48,500**. √48,500 = 220.227.

- −90° support: (220.227 − 0.5)² = (219.727)² = **48,280**
- −180° support: (219.227)² = **48,060**
- −360° support: (218.227)² = **47,623**

A trader short from near 48,500 now has a first cover zone at 48,280 and a major target at 48,060 — levels derived purely from geometry, independent of any moving average.

For a rupee-priced stock, take **Reliance at a swing low of ₹1,225.** √1225 = 35.000 exactly (1225 is 35²) — a "square number", which Gann considered especially strong.

- +90°: (35.5)² = **₹1,260.25**
- +180°: (36)² = **₹1,296**
- +360°: (37)² = **₹1,369**
- −90°: (34.5)² = **₹1,190.25**
- −180°: (34)² = **₹1,156**

Notice how clean the levels are when the pivot is a perfect square: the 180° and 360° levels land on the next perfect squares (36², 37², 34²). This is why some Gann traders deliberately look for setups anchored near square numbers — the whole ladder becomes tidy and the levels are "natural" attractors.

## How to trade it

The Square of Nine is a **level-generator, not a signal-generator.** You still need a trigger. A robust workflow:

1. **Anchor** on the most recent respected swing pivot for your timeframe.
2. **Compute** the 45°/90°/180° ladder both ways and mark them on the chart as horizontal lines.
3. **Wait** for price to reach a Gann level. Do nothing until it does.
4. **Confirm** with a trigger *at* the level: a rejection candle (pin bar, engulfing), a failure to sustain a breakout, an RSI divergence, or a volume/OI signature in F&O. The Gann level tells you *where*; the trigger tells you *when*.
5. **Entry:** on the confirmation candle's close.
6. **Stop:** just beyond the *next* Gann level (not an arbitrary distance). If you sell resistance at the 90° level, your stop sits a few points above the 135° or 180° level — the geometry itself defines your invalidation.
7. **Target:** the next Gann level toward your trade's direction, or the opposition (180°) level for a bigger move. Book partials at each rung.

**Position sizing** flows from the stop. On the Nifty example, selling at 21,948 (90°) with a stop above 22,022 (135°) risks ~74 points; a trader risking ₹5,000 with Nifty at ₹... — on the index future (lot 25), 74 points ≈ ₹1,850 per lot, so up to ~2 lots stays inside the risk budget. The geometry makes sizing mechanical.

### F&O integration

The Square shines when its levels coincide with **option strikes and max-pain / high-OI zones.** If the 180° resistance at 22,096 sits right where the 22,100 call has the fattest open interest, you have geometric resistance *and* a dealer-positioning wall at the same price — a high-conviction fade. Selling a 22,100/22,300 call spread into that confluence, or simply shorting the future with the Gann stop, are both defensible expressions.

## Confluence — where the edge really lives

A raw Gann level in isolation is a coin-flip improved slightly. The edge multiplies when it stacks with independent methods:

- **Fibonacci:** when a 90° Square level lands within a few points of a 61.8% retracement, treat it as a primary decision zone.
- **Prior structure:** a Gann level sitting on a previous swing high/low, a gap fill, or a round number (22,000 on Nifty) is far stronger.
- **VWAP / moving averages:** intraday, a Gann level coinciding with the session VWAP or the 200-DMA positionally is a genuine confluence.
- **Option OI walls:** as above — the single most useful overlay in the Indian F&O context.
- **Time:** the strongest setups occur when a Gann *price* level is hit on a Gann *time* date (covered in the time-cycles chapter). Price-squared-with-time is the real Gann thesis.

Rule of thumb: **trade the two-plus confluences, ignore the lonely levels.**

## Pitfalls

- **Curve-fitting the pivot.** If you keep trying different anchors until the levels "fit" recent turns, you have proven nothing — you have drawn lines through points after the fact. Choose the pivot by an objective rule *before* computing, and live with it.
- **Treating every 15° tick as a level.** The denser you make the grid, the more likely price is "near a Gann level" by pure chance. Restrict yourself to 45°/90°/180°/360°. With enough lines everything looks predicted.
- **Ignoring the trigger.** Buying blindly at a support level in a strong downtrend is how accounts die. The level is a *venue*; you still need confirmation and you still respect the trend.
- **Mysticism creep.** The moment you find yourself adding planetary longitudes to justify a trade you can't otherwise defend, stop. Keep the geometry; drop the astrology unless you have personally backtested it.
- **Rounding sloppiness.** On a 50,000-level Bank Nifty, a 0.5 error in the root is ~220 points. Carry the square root to three decimals.
- **Over-attribution.** When a Gann level "works," ask whether a round number or obvious prior high at the same spot did the real work. Often the market respected the structure, not the spiral.

## Interview-ready summary

The Square of Nine arranges integers in a spiral so that a full 360° rotation adds 2 to the square root of the centre value; consequently every angular step around the wheel is a fixed increment on the *square-root* axis of price. Two formulas capture it: a target level is `(√Pivot ± degrees/180)²`, and the angle between two prices is `(√B − √A) × 180`. You anchor on a genuinely respected swing pivot, project the 45°/90°/180°/360° ladder both ways, and treat those levels as pre-computed support/resistance. It is a level-generator, never a signal: you wait for price to reach a level and only act on an independent trigger (rejection candle, divergence, OI wall), placing the stop beyond the next geometric level so sizing is mechanical. Its real edge appears in confluence — with Fibonacci, prior structure, VWAP, option open-interest, and above all with Gann *time* dates. Honest caveats: pivot choice is subjective and easy to curve-fit, a dense grid manufactures false "hits," and much of the classical mysticism is unfalsifiable. Kept disciplined — objective pivot, sparse grid, confluence-only, trigger-confirmed — the Square of Nine is a legitimate geometric framework for Indian indices and stocks, not a crystal ball.
