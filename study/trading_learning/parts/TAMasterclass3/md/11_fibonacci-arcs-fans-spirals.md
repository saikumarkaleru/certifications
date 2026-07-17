# Fibonacci Arcs, Fans & Spirals

Horizontal Fibonacci retracements assume the market cares about price and nothing else. The tools in this chapter reject that assumption. **Fibonacci Arcs** curve support and resistance through both price and time, so a level "moves" as the days pass. **Fibonacci Fans** radiate diagonal support/resistance rays from a pivot, tracking a trend's angle. **Fibonacci Spirals** — the most exotic and the most honestly speculative — attempt to combine growth and rotation into a single expanding curve. All three are geometric rather than arithmetic, and all three demand that you read them with more scepticism and more discipline than the flat retracement grid. This chapter gives the construction, Indian-market examples in rupees, trading rules, and a frank verdict on which of the three actually deserve room on your chart.

## What they are and the logic

A **Fibonacci Arc** is a set of concentric semicircles (or ellipses, depending on how the platform scales the axes) drawn from a pivot. The radius of each arc is a Fibonacci fraction — 38.2%, 50%, 61.8%, sometimes 100% and 161.8% — of the distance between two chosen pivots (a swing low to a swing high, say). Because the arc is a curve, the level it marks at *today's* bar is different from the level it marks *next week's* bar. The logic: support and resistance decay or strengthen with time, so a curved boundary models a market where "how far back the pullback can go" shrinks as time passes since the pivot. A pullback that would find support at 61.8% early may only reach the 38.2% arc if it comes later, because the arc has curved upward by then in an uptrend.

A **Fibonacci Fan** is a set of diagonal rays from a pivot. You anchor the base pivot (a swing low), draw to a second pivot (the swing high), and the tool constructs an invisible vertical line at the second pivot divided at 38.2%, 50% and 61.8%. It then draws rays from the base pivot through those division points and extends them forward. These rays act as *sloped* support/resistance that adjust automatically for the trend's angle — a fan is essentially a trend-anchored set of speed lines with Fibonacci spacing.

A **Fibonacci Spiral** (golden spiral / logarithmic spiral) winds outward from a centre pivot, with each quarter-turn expanding the radius by a factor tied to φ (1.618) or √φ. The idea, borrowed from the shells and galaxies that pop-finance books love, is that price rotates around a centre of gravity while expanding, and turns occur where the spiral crosses price. It is the most visually seductive and the least mechanically justifiable of the family. We will build it, use it once, and then say honestly what it is worth.

The unifying idea across all three: markets are not purely vertical phenomena. Trends have *angle* (fans), pullback capacity that *changes with time* (arcs), and — if you believe it — a rotational-growth geometry (spirals). Whether the market truly obeys these curves or whether we are pattern-matching on noise is a question we keep in front of us throughout.

## Construction, rules and settings

### Fibonacci Arcs

**Anchor:** two pivots defining the base radius. In an uptrend, click the swing low then the swing high. The straight-line distance (price and time combined) is the 100% radius.

**Arcs drawn:** at 38.2%, 50%, 61.8% of that radius, centred on the *second* pivot (the high) in most platform defaults — though some centre on the first. Know which your platform uses; TradingView centres the arcs on the second click.

| Arc | Radius (fraction of base) | Typical role after an up-swing |
|-----|---------------------------|-------------------------------|
| 38.2% | shallow | first curved support on a pullback |
| 50% | medium | mid support |
| 61.8% | deep | last-defence curved support |
| 100% | full | major support / trend-failure boundary |

**Critical setting — axis scaling.** Arcs are geometrically sensitive to the chart's aspect ratio. Resize the window or switch linear/log and the arcs change shape. Always read arcs on a *fixed, log-scaled* chart and never trust an arc level you cannot reproduce after a zoom. This single sensitivity is why arcs are the trickiest Fibonacci tool.

### Fibonacci Fans

**Anchor:** swing low then swing high in an uptrend (reverse for a downtrend).

**Rays:** from the base pivot through the 38.2%, 50%, 61.8% divisions of the vertical distance at the far pivot, projected forward indefinitely.

| Fan ray | Meaning in an uptrend pullback |
|---------|-------------------------------|
| 38.2% ray | shallow support; strong trends hold here |
| 50% ray | moderate support |
| 61.8% ray | deep support; break below warns of trend change |

Fans are far more robust to scaling than arcs because a ray's *identity* (which two points it passes through) does not change with zoom, only its visual angle does. This makes fans the most practically usable of the three.

### Fibonacci Spirals

**Anchor:** a centre pivot (often a major top or bottom) and a starting radius point. The tool winds a logarithmic spiral outward, expanding by φ per full turn (or per quarter turn, platform-dependent).

**Reading:** watch where the spiral arm crosses future price bars; those crossings are the candidate turn points — combining a price level and a time. There are no clean sub-levels; the spiral is one continuous curve. Direction (clockwise/anticlockwise) and expansion factor are user choices, which is exactly the tool's weakness: too many free parameters.

## Worked India example (levels & ₹)

### Arcs on Nifty 50

Nifty runs from a swing low of **23,400** to a swing high of **24,600** — a base move of 1,200 points. Drop arcs centred on the 24,600 high.

Now Nifty pulls back. *Timing matters because the boundary is curved.* If the pullback comes quickly — within a handful of sessions of the high — the 38.2% arc sits near **24,150** and the 50% arc near **24,000**. Nifty dips to 24,050, taps between the two arcs, and holds. Clean curved support; a reversal candle there is a continuation long.

But suppose the pullback is *slow*, grinding sideways-down over three weeks. By then the arcs have curved higher in time-space, so the 38.2% arc might intersect the price path nearer **24,300** and the 50% nearer **24,180**. The same 24,050 price, arriving later, now sits *below* the 50% arc — a warning that the pullback is deeper-than-ideal relative to elapsed time, and momentum should be checked before buying. This time-sensitivity is the whole point of arcs, and also why they confuse beginners who expect a fixed number.

### Fans on Bank Nifty

Bank Nifty swing low **50,200**, swing high **53,200** (a 3,000-point up-leg). Draw the fan from the low through the high. As price pulls back over the next two weeks:

- Price drifts down and meets the **38.2% ray**, which by that bar sits around **52,400**. A hammer prints; strong-trend behaviour, so a continuation long with a stop below the 50% ray (near **51,700** at that bar).
- The rally resumes to new highs. On the next pullback, price slices the 38.2% ray and finds footing exactly on the **50% ray** near **51,900** — deeper, hinting the trend is tiring but not broken.
- Weeks later price closes below the **61.8% ray**. That break is the fan's trend-change signal; longs stand aside.

The fan adjusted its support levels automatically for the passage of time and the trend's angle — no manual redrawing needed, and robust to zoom.

### A spiral on Nifty — used once, honestly

Centre a golden spiral on the 24,600 major top, expansion φ per turn. Suppose an arm crosses the price path near **23,900** about eight sessions later, and price does indeed base there. Impressive — until you flip the spiral's direction or nudge the centre by one bar and the crossing jumps to **24,100** and a different date. That fragility is the verdict: the spiral *can* be made to fit almost any turn after the fact, so it fails the "would I have taken this in advance and can I reproduce it?" test. Keep it as a curiosity, not a signal generator.

## How to trade them

**Fans (the workhorse).** Entry: buy pullbacks to the 38.2% or 50% ray in an uptrend confirmed by a reversal candle or momentum turn; sell rallies to the rays in a downtrend. Stop: just beyond the next-deeper ray (below the 50% ray when long off the 38.2%; the 61.8% break is the hard invalidation). Target: prior swing high, then Fibonacci price extensions. Management: as long as price rides above the 38.2% ray, hold; a decisive close below the 61.8% ray is the exit for the trend thesis. Fans integrate cleanly into F&O — a long-futures or long-call held while price respects the 38.2% ray, trimmed on a 50%-ray break.

**Arcs (the specialist).** Only trade arcs on a fixed log chart you will not rescale. Use the arc *cluster* — where 38.2% and 50% arcs sit close together in the pullback path — as a curved buy zone, and require a candle trigger. Because the level shifts with time, place the stop by price (below the recent swing low) not by the arc itself. Arcs are best as a *confluence overlay* on horizontal retracements: when a flat 50% retracement and a 38.2% arc coincide at the same bar, that intersection is a high-quality level.

**Spirals.** No standalone trading. At most, note a spiral crossing as one more soft timing flag inside a broader time-and-price confluence, and never size a position on it.

## Confluence — where these earn trust

- **Fan ray + horizontal retracement:** when the 50% fan ray and the flat 50% price retracement meet at the same bar, the intersection is a strong, reproducible level.
- **Arc + horizontal S/R + time zone:** an arc that curves into a prior support shelf on the same session a Fibonacci time line falls due is a genuine time-and-price cluster.
- **Fan + trendline / channel:** a fan ray reinforcing a hand-drawn trendline is more trustworthy than either alone.
- **Momentum and OI:** as always, a reversal candle, an RSI turn, or an OI shift at the level converts geometry into a trade.

## Pitfalls

1. **Aspect-ratio dependence (arcs and spirals).** These curves change shape when you resize or rescale the chart. A level you "found" at one zoom vanishes at another. If you cannot reproduce it, it is not real. Fans are largely immune — a strong reason to prefer them.
2. **Parameter freedom (spirals).** Centre, direction and expansion factor are all adjustable, giving enough degrees of freedom to fit almost any history. That is textbook overfitting.
3. **Anchor sensitivity (all three).** As with every Fibonacci tool, a shaky anchor produces meaningless output. Anchor on structurally obvious pivots only.
4. **Curve-fitting after the fact.** Because curves sweep across many price/time combinations, hindsight always finds a "hit". Judge only on reproducible, pre-committed signals.
5. **Over-cluttering the chart.** Arcs plus fans plus spirals plus retracements produce a spaghetti chart where some line is always near price, which means none of them is informative. Pick one geometric tool per analysis.
6. **The Indian calendar again.** Expiry Thursdays, RBI dates and the Budget create scheduled turns that geometry will appear to "predict". Credit the event, not the curve.

## Interview-ready summary

Fibonacci Arcs, Fans and Spirals extend the sequence from the flat price axis into geometry. **Fans** — diagonal Fibonacci rays from a pivot — are the genuinely useful one: they give trend-anchored, zoom-robust sloped support/resistance, they self-adjust for time and angle, and they trade cleanly with candle confirmation and next-ray stops. **Arcs** — concentric Fibonacci-radius curves — encode the idea that pullback capacity shrinks as time passes since the pivot; they can add value as a confluence overlay on a fixed log chart, but their sensitivity to axis scaling makes them a specialist's tool, not a beginner's. **Spirals** are visually beautiful and analytically weak: too many free parameters (centre, direction, expansion) let them fit any history, so they fail the reproducibility test and belong in the curiosity drawer, not the trade log. The honest hierarchy to state in an interview: fans deserve a permanent place, arcs a conditional one used only in confluence, and spirals essentially none. Across all three, the discipline is identical to the rest of Fibonacci work — anchor on obvious pivots, demand price and momentum confluence, respect the Indian event calendar, and never trade a line you cannot reproduce after a zoom.
