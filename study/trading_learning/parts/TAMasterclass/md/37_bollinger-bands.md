# Bollinger Bands: Squeeze, Walk, %B & Bandwidth

## What it is & why it works

Bollinger Bands, created by John Bollinger in the early 1980s, are a volatility-adaptive envelope drawn around a moving average. Unlike a fixed-percentage channel, the bands breathe: they widen when the market is volatile and contract when it is quiet. That single design choice — anchoring the band width to the *standard deviation* of price — is what makes the tool so durable across the Nifty, Bank Nifty, and individual NSE stocks.

The concept rests on a simple statistical intuition. Price over a lookback window has a mean (the middle band, usually a 20-period simple moving average) and a dispersion around that mean (the standard deviation). If you plot bands at ±2 standard deviations, then — *for a roughly normal distribution* — about 88–90% of price action tends to stay inside the envelope on daily data. The key phrase is "roughly." Markets are not normal; they have fat tails, trends, and volatility clustering. Bollinger never claimed the bands were a probability boundary. He built them as a *relative* framework: "high" and "low" are defined not in absolute rupee terms but relative to recent volatility.

Why does this work behaviourally? Three market truths sit underneath it:

1. **Volatility mean-reverts.** Quiet periods (a "squeeze") are almost always followed by expansion, and violent expansion eventually exhausts back to calm. The bands make this cycle visible. A trader who sees Bank Nifty's bands pinch to their tightest in three months knows a large directional move is loading — even if the direction is not yet decided.

2. **Trends "walk the band."** In a strong uptrend, price rides the upper band, closing near or on it for many bars. A naive trader shorts the "overbought" upper band and gets run over. The band walk is a *continuation* signal, not a reversal — one of the most misunderstood and most valuable behaviours the tool exposes.

3. **Price relative to its own recent range is information.** When a stock like Reliance closes above its upper band after a range, then pulls back to the middle band and holds, buyers are defending the mean. That pullback-to-mean-and-hold is a classic institutional accumulation footprint.

Bollinger Bands are best understood as a *context engine* rather than a signal generator. On their own they tell you the volatility regime and where price sits within it. Combined with the two derived indicators — %B (position within the bands) and Bandwidth (how wide the bands are) — they become a complete volatility-and-location toolkit.

## The mechanics

The three bands are built from a moving average and a standard deviation of closing prices over the same lookback.

| Component | Formula | Default |
|---|---|---|
| Middle band (MB) | Simple moving average of close | SMA(20) |
| Upper band (UB) | MB + (k × σ) | k = 2 |
| Lower band (LB) | MB − (k × σ) | k = 2 |
| σ (sigma) | Standard deviation of the last N closes | N = 20 |

The standard deviation used is the **population** standard deviation over the same N periods as the SMA:

σ = sqrt( Σ(closeᵢ − MB)² / N )

Bollinger's defaults — 20 periods and 2 standard deviations — are deliberate. He recommends: if you lengthen the period, widen k (e.g. 50 and 2.1); if you shorten it, tighten k (e.g. 10 and 1.9). The 20/2 pair keeps roughly 85–90% of daily bars inside on most instruments. On the Nifty daily, 20 sessions is about one calendar month of trading — a natural cycle.

**%B (percent B)** normalises where the last close sits within the band, on a 0-to-1 scale:

%B = (Close − LB) / (UB − LB)

- %B = 1.0 → close is exactly on the upper band
- %B = 0.5 → close is exactly on the middle band
- %B = 0.0 → close is exactly on the lower band
- %B > 1.0 → close is *above* the upper band (band walk / breakout)
- %B < 0.0 → close is *below* the lower band

%B is powerful because it lets you compare Nifty and a ₹80 penny stock on the same axis, and because it can be plotted as an oscillator to spot divergences against price.

**Bandwidth** measures the *width* of the envelope relative to the middle band:

Bandwidth = (UB − LB) / MB

Bandwidth is dimensionless (a fraction, often shown as a percentage), so it too is comparable across instruments and time. Two derived readings matter:

- **The Squeeze** — Bandwidth at a multi-month low. Bollinger's own rule of thumb: the lowest Bandwidth in the last **125 periods** (roughly six months on daily) flags "The Squeeze." On TradingView, the Bollinger BandWidth indicator plots this directly; you watch for it to bottom.
- **The Bulge** — Bandwidth at a multi-month high, warning that volatility is stretched and a directional move may be near exhaustion.

**Settings across timeframes (India practice):**

| Instrument / timeframe | MB | k | Note |
|---|---|---|---|
| Nifty / Bank Nifty daily swing | 20 SMA | 2.0 | Standard, well-behaved |
| Stock positional (weekly) | 20 SMA | 2.0 | Cleaner squeezes on liquid large-caps |
| Bank Nifty 15-min intraday | 20 SMA | 2.0 | Squeeze before the 9:15 open expansion |
| Scalping 5-min | 20 SMA | 1.9–2.0 | Faster, more band touches |

A useful refinement is adding a **third pair at ±1σ** to create "Bollinger zones": the region between +1σ and +2σ is the strong-uptrend zone where band walks live. TradingView lets you overlay a second Bollinger study with k=1 to see these.

## Reading it — a worked Bank Nifty example

Take Bank Nifty on the daily chart through a realistic sequence (levels illustrative of a 2025-style range around 50,000).

**Phase 1 — The Squeeze (consolidation).** Bank Nifty spends three weeks grinding sideways between 49,600 and 50,200. The 20-SMA flattens at roughly 49,900. Standard deviation collapses because closes cluster tightly. The upper band drifts down to ~50,300 and the lower band up to ~49,500 — a band width of only about 800 points, or Bandwidth ≈ (50,300 − 49,500) / 49,900 ≈ 0.016 (1.6%). Checking the BandWidth panel, this is the lowest reading in five months. This is The Squeeze: volatility has coiled. %B oscillates gently around 0.5 as price bounces mid-band. No trade yet — the squeeze tells you *when*, not *which way*.

**Phase 2 — The expansion (breakout).** On the fourth Monday, on a heavy-volume session, Bank Nifty closes at 50,650 — decisively above the 50,300 upper band. %B jumps to about 1.15 (above 1.0, confirming a genuine band break). Bandwidth ticks up sharply as σ expands. This is the resolution of the squeeze. Crucially, the close is *outside* the band on strong volume — the difference between a real breakout and a fake wick.

**Phase 3 — The walk.** Over the next six sessions Bank Nifty keeps closing near the upper band: 50,900, 51,150, 51,050, 51,400, 51,600, 51,550. Each close keeps %B between roughly 0.9 and 1.1. The 20-SMA is now rising and acts as a dynamic floor. This is "walking the band" — the hallmark of a strong trend. A trader who shorted the first upper-band tag at 50,650 thinking "overbought" is now 900 points offside. The band walk is the tool telling you the trend is real; you *hold*, you don't fade.

**Phase 4 — The pullback to the mean.** After 51,600, momentum cools. Bank Nifty slips to 51,050, then tags the rising 20-SMA at ~50,900 (%B ≈ 0.35). Buyers step in and it closes back at 51,300. This first pullback-to-mean-and-hold in a fresh uptrend is a textbook re-entry. The middle band did its job as support.

**Phase 5 — The bulge and exhaustion.** Two weeks later Bank Nifty spikes to 52,400 on an RBI-policy surprise. Bandwidth is now at a six-month *high* (a Bulge). %B prints 1.4. The next day it fails to make a new high and closes back inside the band at 52,050 — %B drops to 0.85. When a strong move can no longer close outside a *widening* band, momentum is fading. This is the pros' exit warning, not a short signal on its own.

## Trading it

Bollinger Bands support several distinct, rule-based strategies. Pick one per regime — do not mix reversal and continuation logic on the same bar.

**1. The Squeeze breakout (the flagship setup).**
- *Context:* Bandwidth at a 125-period (or 3-month) low. Price coiled.
- *Entry trigger:* A close *outside* the band (upper for long, lower for short) with %B > 1.0 (or < 0.0), ideally on above-average volume. On Bank Nifty intraday, the first 15-min candle closing outside after a tight overnight squeeze.
- *Confirmation of direction:* Because a squeeze can fake one way then reverse ("head fake," Bollinger's own term), many traders wait for the *second* bar to hold outside, or use a companion momentum tool.
- *Stop:* Below the middle band (for a long) or below the breakout candle's low. In the Bank Nifty example, long at 50,650, stop under 50,200 (below MB and the range) — risk ~450 points.
- *Target / measured move:* Squeezes have no built-in target. Use the prior range height projected from the breakout (range 49,500–50,300 = 800 points → target ~51,450), or trail the middle band. In the example the walk carried to 51,600 — well past the first target.
- *Management:* Once price walks the band, trail the stop up to the middle band. Exit when price closes back inside on a *widening* band (exhaustion) or when the 20-SMA is broken on a closing basis.

**2. The band-walk trend ride (continuation).**
- *Context:* Price already closing repeatedly at/above the upper band, %B persistently > 0.8, MB rising.
- *Entry:* On the pullback to the middle band that *holds* (%B bounces from ~0.3–0.4 back up). Bank Nifty at 50,900 in Phase 4.
- *Stop:* Below the swing low that formed at the middle band.
- *Target:* Prior high, then trail. Never short the band tags — in a walk they are continuation.

**3. The reversal/mean-reversion fade (range regime ONLY).**
- *Context:* Sideways market, flat MB, Bandwidth mid-range (NOT a squeeze, NOT a walk). Nifty stuck in a 24,800–25,200 box.
- *Entry:* A tag of the lower band that fails to *close* below it (a lower-band "M" or spring), with %B curling up from below 0.1 → buy toward the middle band. Mirror for the upper band.
- *Stop:* Just beyond the band tag.
- *Target:* The middle band (mean reversion), occasionally the opposite band.
- *Warning:* This is the setup that destroys accounts when the range breaks into a trend. It requires an independent read that you are still in a range.

## Confluence

Bollinger Bands sharpen dramatically when paired with orthogonal tools, because on their own they cannot tell direction out of a squeeze.

- **RSI / momentum divergence with %B.** Plot %B as an oscillator. In the Bank Nifty top at 52,400, if price makes a higher high but %B makes a *lower* high (1.4 → then a failed 0.9 peak), that is a classic momentum divergence flagging exhaustion — much cleaner than eyeballing the bands.

- **Volume.** A squeeze breakout that closes outside the band on volume 1.5–2× the 20-day average is materially higher-probability than a low-volume drift outside. Volume is the single best filter for head fakes.

- **Keltner Channel overlay (the TTM Squeeze).** The most popular confluence: when the Bollinger Bands contract *inside* the Keltner Channels, the squeeze is "on"; when they pop back outside, the squeeze "fires." This gives an objective squeeze-on/off signal and a directional cue via a momentum histogram. Extremely popular on Bank Nifty 15-min.

- **Option-chain / OI confluence (India-specific).** This is where a derivatives analyst earns their edge. When Bank Nifty is in a daily squeeze and the weekly option chain shows a *narrowing* gap between the highest-OI Call strike (resistance) and highest-OI Put strike (support) — say Calls stacked at 50,500 and Puts at 49,500 — the market is coiling and premiums (IV) are cheap. A squeeze breakout *through* the high-OI Call strike, forcing call writers to cover, adds fuel; %B > 1.0 plus OI unwinding on the 50,500 Call is a high-conviction long. Conversely, low Bandwidth + low IV means options are cheap — favour *buying* straddles/strangles ahead of the expansion rather than selling premium. When the Bulge appears (Bandwidth six-month high, IV elevated), that favours premium *selling* strategies as volatility mean-reverts down.

- **Higher-timeframe trend.** Only take squeeze longs when the weekly 20-SMA slopes up; fade only in confirmed ranges. Multi-timeframe alignment turns a coin-flip breakout into an edge.

## Pitfalls & false signals

1. **Treating band tags as overbought/oversold.** The number-one error. A tag of the upper band in a trending market is *strength*, not a short. In a band walk, "overbought" stays overbought for weeks. Only fade band tags when you have independently confirmed a range.

2. **The head fake.** Bollinger himself warned that squeezes frequently break one way, suck in traders, then reverse hard. Filter with a close-outside requirement (not just an intraday wick), a second confirming bar, and volume. Many pros wait for the pullback after the initial break rather than chasing the first candle.

3. **Assuming the ±2σ band is a hard probability wall.** It is not. Markets have fat tails; price can and does close well outside for many consecutive bars. The bands are a *relative* framework, never a guarantee that 95% of price stays inside.

4. **Squeeze with no directional plan.** A squeeze tells you volatility will expand, not which way. Trading a squeeze without a companion direction tool (momentum, OI, HTF trend) is gambling on a coin flip with a stop.

5. **Parameter over-fitting.** Endlessly tweaking N and k to make past signals look perfect produces a curve-fit that fails live. Stick close to 20/2; adjust only with Bollinger's period-vs-k rule, and keep it consistent.

6. **Ignoring the middle band.** Newcomers stare at the outer bands and forget the 20-SMA is the real trend anchor. In a healthy trend the middle band is dynamic support/resistance; a decisive close through it is often the earliest reversal warning.

7. **Bandwidth without a reference window.** A Bandwidth reading is meaningless in isolation — 2% is "tight" for Nifty but normal for a volatile small-cap. Always judge it against that instrument's own recent history (the 125-period low/high).

## Interview-ready summary

"Bollinger Bands are a volatility-adaptive envelope: a 20-period SMA with bands at ±2 standard deviations, so they widen in volatile markets and pinch in quiet ones. I read them through three lenses. **%B** normalises where price sits within the bands — 0 at the lower band, 0.5 at the mean, 1.0 at the upper band, above 1.0 on a breakout — so I can compare Nifty and a small-cap on the same scale and spot momentum divergences. **Bandwidth** — (upper minus lower) over the middle — measures how wide the bands are; a multi-month low is 'The Squeeze,' signalling a big move is loading, and a multi-month high is 'The Bulge,' warning of exhaustion. The two behaviours I trade are the **squeeze breakout** — enter on a close outside the band with %B beyond 1.0 on volume, stop at the middle band, target the projected range height — and the **band walk**, where price rides the upper band in a trend, which is continuation, not a short. The classic mistake is fading band tags as overbought; in a walk that gets you run over. Bands don't give direction, so I confirm with volume, RSI/%B divergence, the higher-timeframe trend, and on Indian F&O, the option chain — a squeeze with cheap IV and tightening high-OI strikes tells me to buy volatility and trade the break through the call wall. TA is probability, not certainty: the bands set context and location; the trade needs confluence and a defined stop."
