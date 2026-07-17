# CCI & Williams %R

Two oscillators, two very different design philosophies, one shared job: telling you when price has stretched too far from its own centre of gravity and where momentum sits inside its recent range. Donald Lambert's **Commodity Channel Index (CCI)**, from 1980, is an *unbounded* deviation oscillator built around a statistical measure of dispersion. Larry Williams's **Williams %R**, from the 1970s, is a *bounded* range oscillator — essentially an inverted, un-smoothed cousin of Stochastic. This chapter treats them together because a serious trader uses them for complementary purposes: CCI for detecting the *emergence and strength* of a trend or a "zero-line" thrust, and %R for precise *timing* of overbought/oversold turns, especially in fast Indian intraday markets like Bank Nifty.

## What it is & why it works

**CCI** measures how far the current price has deviated from its statistical average, scaled by that period's typical dispersion. Despite "Commodity" in the name, it applies to any instrument. The genius of Lambert's design is the scaling: he divides the deviation by a *mean absolute deviation* and a constant (0.015) chosen so that roughly **70–80% of readings fall between −100 and +100**. That means a move *outside* ±100 is statistically unusual — a sign that price has broken meaningfully away from its recent mean. The market behaviour it captures: strong trends produce persistent deviation (CCI stays above +100 for a real uptrend, below −100 for a downtrend), while a return toward zero signals the deviation is closing. Because CCI is *unbounded*, it can register the *intensity* of a move (a CCI of +250 is a far more powerful thrust than +110) — information a bounded oscillator throws away.

**Williams %R** measures, like Stochastic, where the close sits within the recent high–low range — but plotted on an *inverted* scale from 0 (at the top of the range, the strongest) to −100 (at the bottom, the weakest). The behaviour it captures: in strong buying, closes hug the top of the range and %R sits near 0; in strong selling, closes hug the bottom and %R sits near −100. It is deliberately *un-smoothed*, making it the fastest of the range oscillators — it turns a hair before Stochastic, which is why scalpers favour it for timing, and why it is noisier.

Why do these work? Both exploit mean reversion at extremes and momentum persistence in trends — the same statistical truths behind RSI and Stochastic, expressed through different maths. CCI's edge is *magnitude and trend-emergence detection*; %R's edge is *speed of turn*. Honest framing: neither is a system. CCI whipsaws in choppy markets and stays "overbought" for entire trends; %R, being un-smoothed, fires constantly. Both demand trend filters and confluence.

## The mechanics

**CCI.** Three steps.

1. **Typical Price (TP)** for each period: `TP = (High + Low + Close) / 3`.
2. **SMA of TP** over n periods (default n = 20).
3. **Mean Deviation** = average of the absolute differences between each TP and that SMA over n periods.

Then:

```
CCI = (TP − SMA of TP) / (0.015 × Mean Deviation)
```

The 0.015 constant is the calibration that puts ~75% of values within ±100. Default period is **20**; shorter (14, 10) is faster and noisier, longer (30, 50) is smoother.

*Worked micro-example:* if TP today is ₹1,015, the 20-period SMA of TP is ₹1,000, and the mean deviation is ₹10, then CCI = (1015 − 1000) / (0.015 × 10) = 15 / 0.15 = **+100**. Price is exactly at the upper edge of its "normal" band. A reading of +200 would mean price is twice as far from the mean as that threshold — an unusually strong thrust.

**Williams %R.**

```
%R = −100 × (Highest High(n) − Close) / (Highest High(n) − Lowest Low(n))
```

Default n = 14. If the close equals the highest high, %R = 0 (top of range, strongest). If close equals the lowest low, %R = −100 (bottom, weakest). It is literally Fast Stochastic's %K inverted and shifted onto a 0 to −100 scale (%R ≈ %K − 100).

**Bands and settings.**

| Oscillator | Overbought | Oversold | Neutral pivot | Default |
|---|---|---|---|---|
| CCI | > +100 | < −100 | 0 (zero line) | 20 |
| Williams %R | > −20 | < −80 | −50 | 14 |

**Signal types.**

*CCI:* (a) **±100 breakouts** — CCI crossing above +100 flags an emerging uptrend/strong thrust (Lambert's original *trend* interpretation), while crossing below −100 flags a downtrend. (b) **Zero-line crosses** — a momentum/trend-bias filter. (c) **OB/OS reversal** — in ranges, turning back from extreme readings (e.g., +200 rolling under +100). (d) **Divergence.**

*Williams %R:* (a) **OB/OS turns** — %R rising back above −80 (bullish) or falling below −20 (bearish). (b) **Failure swings & the −50 midline** cross for momentum bias. (c) **Divergence.** A refined use: in an uptrend, %R holding above −50 and only dipping toward −50/−60 on pullbacks (not to −80) signals trend strength — the with-trend timing tell.

Note the dual personality of CCI's ±100: it means *overbought/reversal* in a **range** but *trend confirmation/entry* in a **trending** market. Knowing which regime you're in is everything.

## Reading it — a worked India example

Take **Bank Nifty on the 15-minute chart** during an intraday session, CCI(20) and %R(14). Assume Bank Nifty opens around ₹51,000.

**Phase 1 — Opening chop (range).** For the first hour Bank Nifty oscillates ₹50,920–₹51,120. CCI swings between roughly +130 and −140, and %R flips between −15 and −85, giving several crossovers. In this balance, CCI turning down from +150 back under +100 near ₹51,110, *with* %R dropping below −20, is a decent short-scalp *back into the range* — but only because there's no trend yet. R:R is modest; these are range fades.

**Phase 2 — The thrust (trend emerges).** At 11:00 Bank Nifty breaks ₹51,120 on volume and CCI **surges to +240** and *holds above +100*. This is the regime switch: CCI above +100 now means *trend*, not "sell." %R pins near **−5 to −10**, hugging the top. A trader who keeps fading overbought here gets run over as Bank Nifty trends to ₹51,600.

**Phase 3 — With-trend pullback timing.** Bank Nifty pulls back to ₹51,440. CCI dips but *holds above zero* (bottoming near +30) and turns up; %R falls only to about **−55** (not −80) and curls back above −50. That shallow, above-midline pullback that refuses to reach oversold is the classic **buy-the-dip trigger in a trend** — CCI staying positive and %R holding the −50 line both confirm the uptrend is intact. Entry on the turn; Bank Nifty resumes to ₹51,850.

**Phase 4 — Divergence and fade.** Late session Bank Nifty tags a marginal new high ₹51,900, but CCI peaks at only **+120** versus the earlier +240, and %R makes a lower high (−12 vs −5) — bearish divergence on both. As CCI then breaks back below +100 and %R falls under −20, momentum has cooled; exit longs, and the drift back toward ₹51,650 confirms the thrust is spent.

The sequence shows the key discipline: read CCI's ±100 as *reversal* in the opening range but as *trend confirmation* once the thrust and hold occur — and use %R's midline (−50) behaviour, not just its −20/−80 bands, to gauge trend health.

## Trading it

**Setup A — CCI ±100 trend-emergence breakout.**
- *Context:* Consolidation resolving; you want to catch the start of a directional move.
- *Long trigger:* CCI crosses above **+100** as price breaks consolidation resistance on volume. E.g., Bank Nifty breaking ₹51,120 with CCI printing +180.
- *Stop:* Below the breakout level / the consolidation low (₹50,980).
- *Target:* Measured move of the consolidation range projected from the breakout, or the next resistance; trail as long as CCI holds above 0.
- *Exit signal:* CCI falling back below +100 (momentum fading) or below 0 (bias flipped).

**Setup B — Williams %R with-trend pullback (fast timing).**
- *Context:* Established uptrend (price above rising EMA, CCI positive).
- *Trigger:* On a dip, %R falls toward −50/−70 and turns back up above −50 (don't demand −80 in a trend). Because %R is un-smoothed, it gives the earliest turn signal.
- *Entry:* On the %R up-turn with a bullish candle at EMA/structure support.
- *Stop:* Below the pullback low. *Target:* prior high, then trail. Mirror for shorts in downtrends.

**Setup C — Range reversal (both oscillators).**
- *Context:* Clearly ranging; price at a defined edge.
- *Trigger:* At resistance, CCI rolls under +100 *and* %R falls under −20 together → short back into the range. At support, CCI back above −100 and %R above −80 → long. Requiring *both* filters cuts false fades.
- *Stop:* Just beyond the range extreme. *Target:* opposite edge.

**Management.** These are fast oscillators; on 15-min Bank Nifty their signals are frequent, so R:R discipline is decisive. Define rupee risk (e.g., 120 Bank Nifty points × 15 = ₹1,800), size to ≤1% of capital, take partials at 1R, trail the rest. Never fade a CCI that is *holding* above +100 in a confirmed thrust — that's fighting the trend the indicator is telling you exists.

## Confluence

**CCI + Williams %R together (complementary by design).** CCI tells you *regime and strength* (is this a trend thrust or a range?); %R gives the *fast timing tick*. Best combination: use CCI's position (above/below 0, above/below ±100) to set the *bias and regime*, then use %R's OB/OS turn to *time* the entry within that bias. Agreement between an unbounded deviation reading and a bounded range reading is genuinely additive information, not redundancy.

**With trend (the essential filter).** Overlay a 50-EMA (or use CCI's own zero line as a proxy). Take %R oversold-turn longs only when CCI > 0 / price above EMA; take overbought-turn shorts only when CCI < 0 / below EMA. This converts both from whipsaw generators into disciplined timers.

**With structure & Fibonacci.** A CCI −100-to-up turn or a %R rise above −80 *at* a tested support or 61.8% retracement is worth far more than the same signal in open space. Structure = location, oscillator = timing.

**With volume & candles.** A CCI +100 breakout on expanding volume with a strong bullish candle is a real thrust; the same on thin volume is a fake-out. Reversal turns confirmed by engulfing/pin-bar candles are higher quality.

**With option chain / OI (India F&O).** For Bank Nifty/Nifty, marry the oscillator to positioning. A %R oversold up-turn (or CCI recovering above −100) at a strike carrying the **highest Put OI** — a put-writer-defended floor with rising PCR — is a high-conviction intraday long. A CCI thrust above +100 that *breaks through* a heavy Call-OI wall on volume signals short-covering fuel and a possible trend day. Conversely, CCI rolling under +100 / %R under −20 right into a stacked Call-OI ceiling times the short. Use OI walls and **Max Pain** to set targets; use CCI/%R to time the trigger. Momentum (CCI/%R) + positioning (OI) + level (S/R) agreeing is the professional's high-probability stack.

## Pitfalls & false signals

**1. Reading CCI ±100 as "always sell/buy."** The biggest CCI error. Above +100 means *reversal* in a range but *trend confirmation* when price has thrust and holds. Misjudging the regime turns a good indicator into a losing one. Fix: only fade ±100 in confirmed ranges; ride it in confirmed thrusts.

**2. %R's noise (un-smoothed).** Being the fastest oscillator, %R fires overbought/oversold constantly and can sit pinned near 0 (or −100) for an entire trend. Mechanical −20/−80 trading against a trend is a fast loss. Fix: trend-filter, use the −50 midline for bias, and prefer with-trend timing.

**3. Persistent divergence in strong trends.** Both CCI and %R can diverge repeatedly while a powerful trend continues. Divergence is a *warning*, activated only by a structure break or a zero-line/midline break — never a standalone counter-trend entry.

**4. Over-fitting parameters.** Endlessly tuning CCI's length or the bands to fit past charts yields curve-fits that fail live. Keep CCI(20)/%R(14) unless a specific timeframe demands otherwise, and let confluence filter.

**5. Choppy/illiquid instruments.** In low-volume smallcaps, both oscillators thrash meaninglessly (erratic ranges and deviations). Demand liquidity; prefer indices and large caps for oscillator work.

**6. Event distortions.** Results, RBI policy, budget, and expiry-day dynamics can spike CCI far beyond ±200 or jam %R to 0/−100 on a one-off repricing, not tradeable momentum. Stand aside for a candle or two.

**7. Ignoring the zero line.** Traders fixate on ±100 and forget CCI's zero-line cross is the cleaner *bias* filter, and %R's −50 the cleaner momentum pivot. The midlines often carry more reliable information than the extremes.

## Interview-ready summary

"CCI and Williams %R are two momentum oscillators built on different maths. **CCI** = (Typical Price − SMA of TP) / (0.015 × Mean Deviation), typically 20-period — it's *unbounded* and Lambert scaled the 0.015 so ~75% of readings sit within ±100, so a move outside ±100 is statistically significant. Its dual personality is the key: above +100 signals *reversal* in a range but *trend confirmation* once price has thrust and held, and because it's unbounded it also shows the *magnitude* of a move. **Williams %R** = −100 × (Highest High − Close) / (Highest High − Lowest Low), 14-period — it's Fast Stochastic inverted onto a 0 to −100 scale, *bounded* and un-smoothed, so it's the fastest to turn and the best for timing, with −20/−80 bands and a −50 momentum midline. I use them complementarily: CCI for regime and strength — is this a trend thrust or a range, and how strong — and %R for the precise entry tick within that bias. Both whipsaw in chop and pin in trends, so I always trend-filter them, anchor to structure, and in Indian F&O cross-check against option-chain positioning — a %R oversold turn at a heavy Put-OI floor, or a CCI +100 thrust breaking a Call-OI wall on volume, is far stronger than the oscillator alone. They tilt probabilities; every signal still gets a defined stop and disciplined size."
