# Bollinger Band Advanced Systems

Almost every trader can draw Bollinger Bands and recite "price bounces between the bands." That recitation is where most Bollinger knowledge stops — and it is where most Bollinger money is lost, because the "bounce between the bands" reading is wrong roughly half the time. John Bollinger, who created the bands in the early 1980s, spent the rest of his career telling people they had misunderstood his own tool. This chapter is the correction and the upgrade. We assume you know the basic construction (a 20-period SMA with bands at ±2 standard deviations). What we build is the *systems* layer: the two derived indicators (%b and BandWidth), the Squeeze, the Walk, the W-bottom / M-top method, and Bollinger's own rules — all tuned for Nifty, Bank Nifty and liquid NSE stocks in 2026.

## What the bands actually are, and the one myth to kill

Standard construction:

```
Middle Band = SMA(Close, 20)
Upper Band  = Middle + 2 × StdDev(Close, 20)
Lower Band  = Middle − 2 × StdDev(Close, 20)
```

The bands are a *statistical envelope of recent volatility*. Because the width is driven by standard deviation, the bands automatically breathe: they widen when volatility rises and contract when it falls. That adaptivity is the whole point — a fixed-percentage envelope cannot do this.

Now the myth. The tags of the bands are **not** buy/sell signals. Bollinger himself: "a tag of the band is not a signal." In a range, price does oscillate band-to-band, so fading tags works. But in a trend, price *walks the band* — it rides the upper band up (or the lower band down) for extended stretches, and every trader shorting those upper-band tags gets run over. Roughly half of all market conditions are trending enough that naive band-fading is a losing proposition. So the very first Bollinger skill is the same as the Stochastic skill: **classify the regime before you act on the level.**

To do that rigorously, you don't eyeball it — you use the two indicators Bollinger derived from the bands.

## %b — where price sits inside the bands

%b normalises price into a single number describing its position relative to the bands:

```
%b = (Close − Lower Band) / (Upper Band − Lower Band)
```

Interpretation:

| %b value | Meaning |
|---|---|
| 1.0 | Close is exactly on the upper band |
| 0.5 | Close is exactly on the middle band (the SMA) |
| 0.0 | Close is exactly on the lower band |
| > 1.0 | Close is *above* the upper band (strong) |
| < 0.0 | Close is *below* the lower band (weak) |

%b is the engine of every serious Bollinger system because it turns "price is near the band" into a precise, comparable number you can code, backtest, and divergence-check against. A %b that reaches 1.1 then 0.9 then 0.7 on successive rallies while price makes higher highs is a textbook momentum divergence — cleaner than most oscillator divergences because it is measured directly against volatility, not an arbitrary range.

## BandWidth — the volatility gauge that finds the Squeeze

```
BandWidth = (Upper Band − Lower Band) / Middle Band
```

BandWidth measures how wide the bands are as a fraction of the moving average — i.e. how volatile the recent market is. Its usefulness is almost entirely in its *extremes*:

- **BandWidth at a multi-month low → the Squeeze.** Volatility has contracted to an unusual degree. Markets alternate between low-volatility contraction and high-volatility expansion; a Squeeze says expansion is statistically overdue. It does *not* say which direction — that is the Squeeze's honest limitation.
- **BandWidth at an extreme high → "The Bulge."** Volatility is stretched. Often marks the *end* of a sharp move rather than the start; a sign to tighten stops and stop chasing, not to initiate.

The practical trigger is the **Squeeze**: identify when BandWidth prints its lowest value in, say, the last 125 bars (roughly six trading months on a daily chart). That is Bollinger's own "the Squeeze" definition. It is the setup; the breakout out of the Squeeze is the signal.

## The Bollinger Squeeze system

**Exact rules (daily, NSE stock or index):**

| Element | Rule |
|---|---|
| Setup | BandWidth = lowest value of the last 125 bars (a "Squeeze") |
| Direction bias | Watch %b and volume: the side the first expansion bar closes on |
| Long trigger | Price closes above the upper band (%b > 1) on expanding volume, breaking the coil's high |
| Short trigger | Price closes below the lower band (%b < 0) on expanding volume, breaking the coil's low |
| Head-fake guard | Bollinger warns of a fake-out: price often pokes one way first, then reverses into the real move. Wait for a *close* beyond the band, and be willing to reverse if it fails within 1–2 bars |
| Stop | Middle band, or the opposite extreme of the coil |
| Target | Measured move = height of the coil projected from the breakout; or trail with the middle band |
| Exit | When BandWidth peaks and %b rolls back through the band — the expansion is maturing |

The Squeeze is the highest-quality Bollinger setup because it exploits the one thing about volatility that *is* reliable: it mean-reverts and cycles. Low volatility does not persist forever; it resolves into a move. You are not predicting direction from the coil — you are pre-positioning to jump on whichever way it breaks, with defined risk.

## Worked India example — Nifty Squeeze into a breakout

A realistic 2026 Nifty daily sequence. Through a quiet late-summer stretch, Nifty drifts in a tightening range between 24,600 and 24,950 — a 350-point band narrowing daily. BandWidth compresses to its lowest reading in six months: a textbook Squeeze. The 20-day SMA sits around 24,780, upper band ~24,980, lower band ~24,580 — bands visibly pinched.

- **The coil:** height ≈ 350 points (24,950 − 24,600).
- **Trigger day:** Nifty closes at 25,010, a close *above* the upper band (%b ≈ 1.08), and NSE cash volume plus index-futures volume both jump versus the 20-day average. The option chain shows call writers at 25,000 getting squeezed (falling OI at 25,000 as it is breached). **Long signal.**
- **Entry:** next-day open, ~25,020, or on a small pullback that holds above the upper-band-turned-support.
- **Stop:** the middle band ~24,790 for a swing version (risk ~230), or tighter under the trigger-day low ~24,880 (risk ~140) for an aggressive version.
- **Target:** measured move 350 points from the ~24,950 breakout → 25,300 primary; then trail with the rising middle band.
- **Outcome:** price begins to **walk the upper band** — six of the next eight sessions close with %b above 0.9, the hallmark of a healthy trend. Nifty reaches 25,380, exceeding the measured move. A trailing stop under the 20-SMA middle band keeps you in until price finally closes back below the middle band around 25,300 — banking ~280 points against ~140 risked, roughly 2R on the tight version.

Crucially, note the head-fake guard: two weeks earlier the same coil had produced a single intraday poke *below* 24,600 that closed back inside — a classic Bollinger fake-out. A trader who waited for a *close* beyond the band was not trapped by it.

## Walking the band — trading *with* strength

The upper-band walk is the regime that destroys band-faders and rewards trend-followers. Bollinger's rule for confirming a genuine walk uses %b together with volume or an independent momentum measure: **price is walking the band, not merely tagging it, when successive closes hold %b above ~0.8 and the middle band is rising steadily.** In that state:

- **Do not short upper-band tags.** You are in a trend.
- **Buy pullbacks to the middle band (the 20-SMA).** In a strong uptrend the middle band is dynamic support; a dip to it with %b falling to ~0.5 then turning up is the with-trend entry.
- **Exit the walk** when price closes below the middle band, or when %b makes lower highs (divergence) while price makes higher highs — momentum is leaking even as the walk continues.

This is the Bollinger equivalent of the Stochastic "bull-support-zone buy": the middle band is your dip-buy anchor, %b is your momentum monitor, and the band-walk is your regime license.

## W-bottoms and M-tops — Bollinger's pattern method

Arthur Merrill's W and M patterns, adapted by Bollinger with %b, are his signature reversal setups and are more reliable than naked band tags because they build in a *non-confirmation*.

**W-bottom (bullish reversal):**

1. Price makes a reaction low, tagging or piercing the lower band — %b at or below 0.
2. Price bounces toward the middle band.
3. Price makes a *second* low, at or slightly below the first in price terms — but this time %b is *higher* (the second low does not pierce the band as deeply, or holds inside it).
4. That non-confirmation — a lower/equal price low with a higher %b — is the tell. Confirmation comes when price breaks above the interim bounce high, ideally on expanding volume.

**M-top (bearish reversal)** is the mirror: a higher/equal price high made on a *lower* %b (the second high fails to reach the upper band as the first did), confirmed by a break of the interim low.

The power of the W and M is that they are *divergence patterns expressed through %b*, and %b measures momentum against live volatility. On NSE stocks that gap around results, %b W-bottoms filter out fake capitulation lows because the second low's %b tells you whether real selling pressure is still there.

**Worked mini-example — HDFC Bank W-bottom.** HDFC Bank sells off to ₹1,642, piercing the lower band with %b = −0.05. It bounces to ₹1,678 (middle band). A week later it dips again to ₹1,638 — a *lower* price low — but this time %b = 0.12, holding inside the band. That is the non-confirmation: price lower, momentum higher. Buy the break of ₹1,678 at, say, ₹1,681, stop under ₹1,635 (risk ₹46), targeting the recent swing high near ₹1,730 — ~₹49 for ₹46, and the second-low %b told you the sellers had run dry before price did.

## The complete Bollinger rule-set (Bollinger's own)

John Bollinger published 22 rules; the load-bearing ones for a system:

1. Bands measure high/low relative to volatility — a framework, not a system by itself.
2. **%b tells you where you are** relative to the bands; **BandWidth tells you how wide** they are. Master these two before anything else.
3. Tags of the band are **not** signals.
4. Use bands with **independent, non-derivative** indicators — volume, breadth, open interest, sentiment — never a second price-based oscillator that just re-measures the same thing.
5. When indicators *confirm* price at a band, no signal; when they *diverge* (via %b), that is the signal.
6. Default (20, 2). If you lengthen the period, widen the multiplier (e.g. 50, 2.1); if you shorten it, narrow it (e.g. 10, 1.9). Keep ~90% of price inside the bands.
7. The average should describe the intermediate-term trend — do **not** optimise it to be a signal-generating crossover average.

Rule 4 is the one traders violate most: they "confirm" Bollinger Bands with RSI, but both are price-derived — you learn nothing new. Confirm with **volume, OI or breadth** — genuinely orthogonal information.

## Settings and adaptations for NSE / F&O

- **Default (20, 2)** works well on Nifty and Bank Nifty daily and hourly. Verify the ~90% containment on your instrument; adjust the multiplier, not wildly, to keep it.
- **Intraday Bank Nifty (5-min):** bands react fast and Squeezes/expansions happen around the open and around events. Pair with VWAP — a Squeeze breakout that also clears VWAP in the same direction is far higher quality.
- **F&O expression:** A Squeeze is, in options language, a *low implied-volatility, coiled* condition. The clean expression of "expansion is overdue but direction unknown" is a **long straddle/strangle** placed *before* the break — you profit from the volatility expansion itself, not the direction. Conversely, when BandWidth is at a bulge extreme (volatility stretched), premium selling (iron condors) around the exhausted move can work — but only with strict risk limits, because a band-walk trend will run over a short-vol position.
- **Event awareness:** BandWidth naturally collapses ahead of RBI policy, budget and big results as price coils, then explodes on the headline. The Squeeze-into-event is real, but the direction is a coin flip on the news — the straddle expression respects that honesty; a directional bet does not.

## Confluence — what turns a band signal tradeable

- **Volume:** the single most important confirmation (Bollinger Rule 4). Squeeze breakouts and W-bottom confirmations need expanding volume; without it, suspect a fake-out.
- **Open interest / option chain:** for index breakouts, falling OI at the strikes being breached (short covering) validates the move.
- **Breadth:** an index band-walk backed by broad advance/decline participation is trustworthy; one on narrowing breadth is fragile.
- **VWAP (intraday):** align band breakouts with the correct side of VWAP.
- **Structure:** take Squeeze breakouts that also break a horizontal level or trendline — two independent reasons beat one.

## Pitfalls — the honest list

1. **Fading band tags in a trend.** The cardinal error. In a band-walk, upper-band tags are strength, not shorts. Classify regime with %b/BandWidth first.
2. **Confirming price-bands with price-oscillators.** RSI + Bollinger is one measurement twice. Use volume, OI, breadth.
3. **The Squeeze head-fake.** Price frequently pokes the wrong way before the real move. Demand a *close* beyond the band and be ready to reverse. This is Bollinger's own explicit warning.
4. **Trading direction off the Squeeze itself.** A Squeeze predicts a *volatility expansion*, not a direction. If you need a directional-agnostic bet, use a straddle; if you go directional, wait for the break.
5. **Over-optimising the middle band.** It is a trend descriptor, not a crossover signal generator. Leave it at 20.
6. **Gap distortion on NSE stocks.** A results gap can blow BandWidth and %b around for a couple of bands; let them re-stabilise before trusting a signal.
7. **Selling volatility into a bulge blindly.** A BandWidth bulge often marks exhaustion, but "often" is not "always" — a fresh trend can bulge and keep going. Short-vol needs hard risk limits.

## Interview-ready summary

Bollinger Bands are a volatility envelope — a 20-SMA with ±2 standard-deviation bands that breathe with volatility. The foundational skill is that **band tags are not signals**; you must first classify the regime, and the tools for that are Bollinger's two derived indicators: **%b** (position of price within the bands, where 1 = upper band, 0.5 = middle, 0 = lower) and **BandWidth** (band width relative to the average). BandWidth at a multi-month low is **the Squeeze**, Bollinger's premier setup — volatility contraction that must eventually expand — traded by pre-positioning for whichever direction the coil breaks, with a measured-move target and a head-fake guard requiring a *close* beyond the band. In trends, price **walks the band**: you stop fading tags and instead buy dips to the middle band, using %b to monitor momentum. **W-bottoms and M-tops** are %b-based divergence patterns — a lower price low on a higher %b is a bullish non-confirmation — more reliable than naked tags. Bollinger's own rules insist you confirm with **non-price** data (volume, open interest, breadth), never a second price oscillator. On Nifty, Bank Nifty and NSE stocks in 2026, this converts "price bounces between the bands" into a genuine volatility-regime system — and in F&O, a Squeeze is best expressed as a long straddle, honestly respecting that the coil predicts *expansion*, not *direction*.
