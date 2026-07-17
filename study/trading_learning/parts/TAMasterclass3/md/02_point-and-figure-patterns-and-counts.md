# Point & Figure: Patterns & Price Objectives (Counts)

The previous chapter built the Point & Figure grid — X-columns, O-columns, box size, and the 3-box reversal. That is the alphabet. This chapter is the language: the **named signal patterns** that P&F traders act on, and — the feature that genuinely sets P&F apart from every candle-based method — its two **mechanical price-objective counts**. On a candlestick chart, a target is an eyeballed guess ("looks like it could reach the last swing high"). On a P&F chart, the target is *computed from the geometry of the base itself*, with arithmetic that any two traders will replicate identically. For an Indian trader who wants entries, stops, and targets that are all rule-bound rather than discretionary, this is P&F's crown jewel. We work everything in rupees and realistic Nifty / Bank Nifty / NSE-stock levels for 2026.

## What the patterns are and the logic

Every P&F pattern is ultimately a variation on one idea: **who wins the fight at a horizontal level of supply or demand.** Because columns sit on a tidy grid, prior column tops line up as resistance and prior column bottoms line up as support. A pattern is simply the story of price attacking those aligned levels. Two families exist — the **basic (two-column)** signals and the **complex (multi-column)** patterns — plus the P&F trendlines that filter them.

### The two primitive signals

| Pattern | Definition | Meaning |
|---|---|---|
| **Double-Top Buy** | An X-column rises **one box above** the immediately prior X-column's top | Demand overwhelms the supply that capped the last rally |
| **Double-Bottom Sell** | An O-column falls **one box below** the immediately prior O-column's bottom | Supply overwhelms the demand that held the last dip |

These are the atoms. Every other bullish pattern is a Double-Top Buy dressed up with more context; every bearish pattern is a Double-Bottom Sell with more context. The "double" refers to the two X (or O) columns whose tops (bottoms) are being compared.

### The complex bullish patterns

- **Triple-Top Buy:** three X-columns reaching the same top, separated by two O-columns, with the third X breaking one box above. Three failed supply tests broken on the fourth attack — stronger than a double because more supply has been absorbed.
- **Bullish Triangle:** a series of higher O-column bottoms and roughly equal X-tops (an ascending triangle in P&F form); the buy triggers when an X breaks the flat top. Rising demand line squeezing price into a resistance shelf.
- **Bullish Catapult:** a Triple-Top Buy followed by a small pullback that holds *above* the breakout, then a fresh Double-Top Buy. Two stacked signals — a continuation launch. Among the highest-reliability P&F setups.
- **Bullish Signal Reversed / Ascending Triple Top:** each successive top and bottom is higher, and the breakout confirms the staircase.

### The complex bearish patterns

Each is the mirror image: **Triple-Bottom Sell**, **Bearish Triangle** (descending), **Bearish Catapult**, and **Descending Triple Bottom**. The logic inverts — repeated demand tests failing, then a break of the demand shelf.

### The P&F trendlines (the pattern filter)

Two lines, drawn at a strict **45°** across the boxes, decide whether a signal is with or against trend:

- **Bullish Support Line:** starts one box below the lowest O of a base and rises at 45°. As long as price stays above it, the trend is up; buy signals above it are high-quality.
- **Bearish Resistance Line:** starts one box above the highest X of a top and falls at 45°. Sell signals below it are high-quality.

A Double-Top Buy *above* a rising bullish support line is an A-grade signal; the identical pattern *below* a falling bearish resistance line is a low-grade counter-trend signal you should usually skip. This internal, non-parameter trend filter is unique to P&F and is what tames the whipsaws the previous chapter warned about.

## The price objectives: counts

Here is the machinery that no candle chart offers. P&F gives **two independent methods** to project how far a move should travel, each derived purely from the size of the base or the launch column.

### Vertical count

The vertical count measures the *thrust* of the first move off a reversal.

**Formula (bullish):**
`Price target = base of the breakout X-column + (number of X's in that column × box size × reversal)`

The reversal (usually 3) enters the formula because a column of N boxes represents a move that "earned" the right to be that tall by surviving reversals — the multiplier converts column height into a projected extension.

**Worked Nifty example.** Box size = 20, reversal = 3. Nifty sells off and bottoms; the first X-column that reverses up runs from **24,500 to 24,760** — that is 14 X's (24,500, 24,520, … 24,760 → (24,760−24,500)/20 = 13 intervals, 14 boxes counting the base).

Vertical count target = 24,500 + (14 × 20 × 3) = 24,500 + 840 = **25,340**.

So the first strong up-column off the low mechanically projects Nifty toward **25,340**. You did not draw a Fibonacci extension or guess a "measured move" — you counted boxes and multiplied. Two traders will get the same 25,340.

**Bearish vertical count** inverts: `top of the first O-column − (number of O's × box size × reversal)`. If Bank Nifty tops with a first down O-column from 51,600 to 50,100 (box 100), that's 16 O's; target = 51,600 − (16 × 100 × 3) = 51,600 − 4,800 = **46,800**.

### Horizontal count

The horizontal count measures the *width of the base* — the congestion — on the theory that the wider the accumulation, the bigger the eventual move (the "cause builds the effect," echoing Wyckoff).

**Formula (bullish):**
`Price target = bottom of the base + (width of the base in columns × box size × reversal)`

where "width" is the number of columns in the congestion pattern at the breakout row.

**Worked NSE-stock example.** Take a ₹500 stock, box size ₹5, reversal 3. It bases sideways and the congestion at the breakout level is **9 columns** wide, with the base bottom at **₹480**.

Horizontal count target = 480 + (9 × 5 × 3) = 480 + 135 = **₹615**.

The wider the base, the higher the target — a 15-column base on the same stock would project 480 + (15 × 5 × 3) = ₹705. This captures the intuition that long accumulation fuels long markups, but does so numerically.

**Bearish horizontal count:** `base top − (width in columns × box size × reversal)`.

### Reconciling the two counts

The two counts rarely agree exactly, and that is useful. Treat them as a **target zone**, not a point:

- When the vertical and horizontal counts **cluster** (e.g. both land Nifty near 25,300–25,340), confidence is high and you can plan a single primary exit there.
- When they **diverge widely**, take the *nearer* count as your first profit-booking level (T1) and the *farther* as a stretch target (T2) if momentum persists. Book part, trail the rest.
- Counts can be **partially or fully negated** — if price fails to reach a count and instead prints an opposite signal, the count is void. Counts are projections with a probability attached, not guarantees. Historically, a meaningful fraction of counts are never fully met; treat ~2/3 realisation as a working expectation, not a promise.

## How to trade patterns + counts together

The complete P&F trade fuses the three legs into one plan:

1. **Entry** = the pattern signal. Prefer a Triple-Top Buy or a Bullish Catapult over a bare Double-Top, and demand it fire *above the bullish support line*.
2. **Stop** = one box below the breakout column's controlling low, or below the bullish support line. Convert to rupees and size to your per-trade risk budget.
3. **Target** = the count(s). Book T1 at the nearer count, trail the remainder toward the farther count using the rising support line.

**Full Nifty walk-through.** Box 20, reversal 3, Nifty lot 75.
- Nifty forms a base and prints a **Triple-Top Buy at 24,700** (X breaks two prior X-tops at 24,680), and the print is above a rising 45° support line. **Enter long** (futures or a 24,700/25,000 bull call spread).
- The first up-column off the low ran 24,500→24,760 (14 X's) → **vertical count 25,340**. The base was 9 columns wide with bottom 24,480 → **horizontal count** 24,480 + (9×20×3) = 24,480 + 540 = **25,020**.
- **Targets:** T1 = 25,020 (nearer, horizontal), T2 = 25,340 (farther, vertical). Book half at 25,020, trail the rest.
- **Stop:** one box below the last O-low at 24,480 → stop ~24,460. Risk = 24,700 − 24,460 = 240 points × 75 = ₹18,000/lot; size lots so that equals your risk budget. Reward to T1 = 320 pts, to T2 = 640 pts → R:R of ~1.3 and ~2.7. The catapult/triple-top quality justifies the trade.
- **Manage:** trail stop up to one box below each new O-column low; exit remainder either at 25,340 or on a Double-Bottom Sell / break of the support line, whichever comes first.

**Bank Nifty and F&O nuance.** Because Bank Nifty counts produce chunky point targets (thousands of points on a wide base), they map neatly onto **spreads and ratio structures**. A 46,800 bearish vertical count off a 51,600 top argues for a bear put spread with the long strike near the entry and the short strike near the count — the count *chooses your strikes*. This is a concrete, underused way to let P&F geometry design an options position rather than picking strikes by feel.

## Confluence

- **Counts meeting other levels.** A P&F count that lands on a prior swing high, a round number (25,000 on Nifty), a monthly VWAP, or a heavy options OI strike is a high-conviction target. When 25,340 also happens to be the strike with the largest call OI, expect real resistance there — book more.
- **Bullish Percent Index.** Take index-level buy signals (and trust their counts more) when the Nifty/Bank Nifty BPI is rising off oversold. A count generated in a market where breadth is broadly on P&F buys is more likely to be met.
- **Relative-strength P&F.** A stock giving a Triple-Top Buy whose RS-vs-Nifty P&F is *also* on a buy — take the count seriously and prefer that name for the trade.
- **Catapult stacking.** The catapult itself is confluence: two signals (triple-top then double-top) at the same structure. Its counts, especially the horizontal count off the wide base, tend to be the most reliable in the P&F toolkit.

## Pitfalls

- **Counting the wrong column.** The vertical count uses the *first* clean thrust column off the reversal, not a random tall column mid-trend, and not the breakout column itself unless it *is* that first thrust. Mis-identifying the column throws the whole target off. Be disciplined and consistent.
- **Base-width ambiguity.** The horizontal count depends on where you decide the congestion starts and ends. Reasonable traders can disagree on the column count. Anchor the base to the clearly-bounded consolidation and, when unsure, take the more conservative (narrower) width.
- **Treating counts as certainties.** A large share of P&F counts are never fully met and some are exceeded. They are probabilistic projections. Always book partial at the nearer count; never bet the whole position on the far count being hit.
- **Ignoring negation.** If price prints an opposite signal or breaks the trendline before reaching the count, the count is dead — exit; don't "wait for the target."
- **Counter-trend patterns.** A textbook Triple-Top Buy occurring *below* a falling bearish resistance line is low-probability. The pattern filter (trendlines) exists precisely to stop you taking pretty patterns fighting the dominant trend.
- **Box/reversal inconsistency.** Because the reversal multiplier is baked into both count formulas, changing box size or reversal mid-analysis silently invalidates earlier counts. Lock the parameters for an instrument and keep them fixed.
- **Illiquidity.** Counts on thin small-caps or far options can be distorted by a single erratic print that fabricates a false column. Keep P&F counting to liquid Nifty/Bank Nifty/Fin Nifty, F&O stocks, MCX, and USDINR.

## Interview-ready summary

P&F patterns are all variations on two atoms — the **Double-Top Buy** (an X exceeds the prior X-top by a box) and the **Double-Bottom Sell** — elaborated into **triple tops/bottoms, triangles, and catapults**, and filtered by two 45° trendlines (**bullish support**, **bearish resistance**) that grade a signal as with-trend or counter-trend. P&F's defining edge is its **two mechanical price objectives**: the **vertical count** (base of the first thrust column + boxes × box-size × reversal) which measures thrust, and the **horizontal count** (base + congestion-width-in-columns × box-size × reversal) which measures the width/cause of the base. Where the two counts cluster, confidence is high; where they diverge, use the nearer as T1 and the farther as T2. A complete P&F trade is entry-on-pattern, stop-below-controlling-low-or-trendline, and target-by-count — all three rule-bound, which is why systematic Indian traders favour it. Worked at Nifty box-20/reversal-3, a Triple-Top Buy at 24,700 might carry a vertical count to ~25,340 and a horizontal count to ~25,020, and on Bank Nifty the count can directly *choose your option strikes*. The honest caveats: counts are probabilistic (a meaningful fraction never fully complete), base width is somewhat subjective, and any count is void once an opposite signal or trendline break appears. In one line: *P&F is the rare method where the chart tells you not just when to buy, but exactly how far the move should go — with arithmetic anyone can reproduce.*
