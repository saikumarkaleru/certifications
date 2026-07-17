# The Ascending Triangle

## What it is & why it works

The ascending triangle is one of the cleanest, most tradeable continuation patterns in technical analysis, and it is a workhorse in Indian equity and index charts. Visually it is defined by two lines: a **flat, horizontal resistance line** across a series of highs that keep stalling at roughly the same price, and a **rising trendline** connecting a series of higher lows underneath. Price gets squeezed into the apex between these two lines until it eventually resolves — most often, in an established uptrend, to the upside through the flat resistance.

To trade it well you must understand the *behaviour* it encodes, not just the shape. The flat top is a **supply zone** — a price at which a cluster of sellers keeps offering stock. Every time price rallies up to, say, ₹1,480 on a stock, a wall of limit sell orders appears (profit-takers, an institution distributing a tranche, option writers defending a strike, an old resistance level where trapped buyers want to exit at break-even). Price gets rejected and falls back. So far this is just resistance.

What makes it an *ascending* triangle — and bullish — is what happens on the pullbacks. The **higher lows** tell you that buyers are getting more aggressive. Instead of waiting for a deep discount, demand steps in earlier and earlier on each dip. The first pullback might bottom at ₹1,400, the next at ₹1,430, the next at ₹1,455. Buyers are willing to pay up. This is the signature of **accumulation**: strong hands are absorbing the supply sitting at the flat top, soaking it up on every dip, refusing to let price fall far.

The market behaviour is essentially a contest with a foregone conclusion bias. There is a fixed quantity of supply at the ceiling. Demand is rising and compressing time. Eventually the buyers absorb all the resting supply at the ceiling, the sellers are exhausted, and the next wave of buying has nothing to push against — price breaks out on a surge of volume. Because the pattern most commonly appears *within* an existing uptrend or after a base, it usually acts as a **continuation** pattern: a pause that refreshes the trend. This is why it "works" — it is a visible map of supply being eaten and demand tightening.

Honesty demands two caveats up front. First, an ascending triangle is a *probability*, not a guarantee. The flat resistance can hold and the pattern can fail downward — especially in a weak broader market. Second, apex direction is biased but not fixed; roughly two-thirds of clean ascending triangles in trending contexts break up, which is an edge, not a certainty. You trade it with defined risk, not conviction.

## The mechanics

A valid ascending triangle has strict-enough construction rules that separate it from random chop.

**Construction requirements:**

| Element | Rule |
|---|---|
| Highs | At least 2 (ideally 3+) swing highs at approximately the same price — a horizontal resistance line. Tolerance ~0.3–0.5% around the level. |
| Lows | At least 2 (ideally 3+) *higher* lows, forming an upward-sloping trendline. |
| Touches | The more touches of each line, the more reliable — 5 total touch points is a textbook minimum. |
| Prior trend | Best as a continuation: a prior uptrend or a base breakout leading in. |
| Duration | Typically forms over 3–7 weeks on the daily chart; intraday versions form over hours. |
| Volume | Should *contract* as the triangle matures — a hallmark of coiling. Then *expand* sharply on the breakout. |
| Apex | Price should ideally break out before it reaches ~75% of the way to the apex. Patterns that drift to the very tip lose energy and often fizzle. |

**The flat line** is drawn across the highs. Do not demand a perfect tick-for-tick match; use closing highs or the body cluster and allow a small band. On Nifty, if the swing highs print 24,850 / 24,862 / 24,845, that is a flat top at ~24,850.

**The rising line** connects the reaction lows. It should have a genuine positive slope. If the lows are flat too, you have a rectangle; if the lows fall, it is not ascending.

**Volume signature** is the mechanical tell that most beginners ignore. Through the coil, daily volume should *dry up* — this reflects reduced disagreement and the market winding a spring. On TradingView, watch the volume bars step down as the apex approaches. The breakout candle should print volume well above the 20-day average — a common filter is **1.5x to 2x the 20-day average volume** on the breakout close.

**The measured-move target.** The classic price objective is the **height of the triangle projected from the breakout point.** Measure the vertical distance from the flat top down to the *first* (lowest, leftmost) low — that is the widest part of the pattern. Add that height to the breakout level.

> Target = Resistance level + (Resistance − Lowest low of the pattern)

Example: flat top ₹1,480, lowest low ₹1,380 → height ₹100 → breakout target ≈ ₹1,580.

**Settings & tools.** On TradingView use the Trendline tool for both lines, add a 20-day (or 50-day) moving average for trend context, and keep volume visible. On Chartink you can screen for the setup with conditions like "price within 1% of a 20-day high AND rising 10-day low AND volume contracting" — imperfect, but a starting filter. For indices, overlay the option-chain view separately.

## Reading it — a worked India example

Let us walk through a realistic ascending triangle on **Bank Nifty** on the daily chart, phase by phase, with levels in points (and the rupee logic for a position trader).

**Phase 1 — the lead-in trend.** Bank Nifty rallies from 48,000 to 51,000 over three weeks on strong PSU-bank and HDFC Bank participation. Momentum is clearly up; the index is above its 20- and 50-DMA. This uptrend is the context that biases any consolidation to resolve upward.

**Phase 2 — the flat top forms.** The index pushes to **51,000** and stalls. FIIs are booking some profits and there is heavy call writing at the 51,000 strike, so a supply wall sits right there. Price pulls back to **50,100**. Three sessions later it rallies again to **51,020** — same ceiling — and is rejected. We now have two touches of a flat top at ~51,000. This is the resistance line.

**Phase 3 — higher lows appear.** The pullback from the second rejection only reaches **50,400** before dip-buyers step in — a *higher low* than the 50,100 of Phase 2. A third rally tags **50,980** (the ceiling again, third touch), and the next dip holds even higher at **50,650**. Connect 50,100 → 50,400 → 50,650: a clean rising trendline. The triangle is now visible and confirmed with five touch points. Volume has been stepping down through this fortnight — the coil is winding.

**Phase 4 — the squeeze.** Price is now oscillating in a narrowing band between the rising line (~50,750 and climbing) and the 51,000 ceiling. Daily ranges shrink. The option chain shows the 51,000 call open interest starting to get bought back / rolled up — a subtle sign the writers are losing confidence in the ceiling holding. This is the pre-breakout tell.

**Phase 5 — the breakout.** On the next session, Bank Nifty opens at 50,950 and, on a positive global cue and PSU-bank buying, closes decisively at **51,280** — a clean close above 51,000 — on volume roughly 1.8x the 20-day average, with a visible expansion in futures volume and a sharp drop in 51,000 call OI (writers covering). The supply wall has been eaten. The measured move: triangle height = 51,000 − 50,100 = **900 points**, projected from 51,000 → **target ≈ 51,900**. A position trader risking to the last higher low (50,650) has a defined, favourable structure.

**Phase 6 — the follow-through.** Over the next week Bank Nifty grinds to 51,850, tags near the measured-move target, and the old resistance at 51,000 now acts as support on a shallow retest — the classic **polarity flip** (resistance-becomes-support), which offers a second, lower-risk entry for anyone who missed the breakout.

## Trading it

There are three viable entry approaches, each with a different risk/reward and hit-rate trade-off.

**1. The breakout-close entry (standard).**
- **Trigger:** a candle *closing* above the flat resistance, ideally with volume ≥ 1.5–2x the 20-day average. Demanding a close (not just an intraday poke) filters most fakeouts.
- **Stop:** below the most recent higher low, or below the breakout candle's low, or below the flat line by a buffer (~0.5–1x ATR). In the Bank Nifty example, stop below 50,650 or below the breakout candle low ~50,900.
- **Target:** the measured move (51,900), often scaled — book part at the measured target, trail the rest with a moving average or a rising-low trendline if the trend is strong.

**2. The anticipation entry (aggressive).**
- **Trigger:** buy on the bounce off the rising trendline *inside* the triangle, near the third or fourth higher low, betting the pattern resolves up.
- **Stop:** just below that trendline. This gives a *tighter stop and better R:R* because you enter lower — but a lower hit rate, since the breakout is not yet confirmed. Position size smaller.

**3. The retest entry (conservative).**
- **Trigger:** wait for the breakout, then buy the pullback that retests the broken flat line as new support (51,000 in the example).
- **Stop:** below the retest low. This is the highest-probability, best-R:R entry when it occurs — but sometimes the breakout runs away and never retests, so you miss it. Pros often split: take a starter on the breakout, add on the retest.

**Position sizing & scenarios.** Fix your risk per trade (say 1% of capital). With a defined stop, position size = risk amount ÷ (entry − stop). 

- *Scenario A — clean breakout, straight to target:* trail behind the 20-DMA, book the measured move, let a runner ride.
- *Scenario B — breakout then shallow retest:* add on the retest, move stop to break-even on the starter.
- *Scenario C — false breakout (poke above then close back inside):* the demand for a *close* usually saves you; if you entered intraday, exit on the failed close and consider that the pattern may now break down.
- *Scenario D — breakdown through the rising trendline:* the pattern has failed as bullish. Do not average down. A close below the rising line, especially on volume, negates the setup and can trigger a sharp fall to the pattern's base.

## Confluence

An ascending triangle in isolation is a decent setup; stacked with confluence it becomes a high-probability one. The professional edge is in *filtering*.

**Trend & moving averages.** The pattern is strongest as a *continuation* — so an ascending triangle sitting above a rising 50-DMA, within a clear uptrend, is far more reliable than one forming after a long downtrend (where a flat top is more likely to hold and the pattern to fail). Align with the higher-timeframe trend.

**Volume & the coil.** Confirm the textbook signature: contracting volume through the triangle, expansion on breakout. A breakout on *weak* volume is a yellow flag for a fakeout.

**Option-chain / OI (indices & liquid stocks).** This is where an Indian derivatives analyst gets a real edge. The flat resistance often coincides with a **heavy call-OI strike** — that call writing *is* the supply wall. Watch it on breakout day:
- If price closes above the strike and **call OI at that strike drops sharply** (short covering by writers), the breakout is being validated by the very sellers who built the wall — a powerful confluence.
- If price pokes above but **call OI keeps building**, writers are defending; treat the breakout with suspicion.
- Rising **Put OI** at a strike just below the rising trendline confirms buyers are defending the higher lows.
- A falling **PCR turning up**, or a shift of max-pain higher, adds confidence.

**Support/resistance polarity.** If the flat top also aligns with a prior all-time high or a big round number (Nifty 25,000; a stock's ₹1,000), the breakout carries extra significance because it clears psychological supply.

**Momentum oscillators.** RSI holding above 50 through the coil and making higher lows (or a bullish divergence at the final higher low) supports the up-resolution. Beware a *bearish* RSI divergence into the flat top on each push — that warns the up-break may fail.

**Relative strength & sector.** A stock forming an ascending triangle while its sector index is also strong (e.g., an auto stock coiling while Nifty Auto breaks out) has tailwind. Trade the leaders.

The ideal high-conviction setup: uptrend + clean ascending triangle + contracting volume + flat top on a heavy call strike + call OI unwinding on the breakout + RSI > 50 + strong sector. When five of these line up, you press size.

## Pitfalls & false signals

**The false breakout (bull trap).** The most common failure: price pokes above the flat line intraday, sucks in breakout buyers, then closes back inside and reverses. **Filter:** require a *closing* breakout, ideally on the daily timeframe, with volume expansion. Intraday-only pokes on thin volume are the classic trap.

**Drifting to the apex.** If price coils all the way to the tip of the triangle without breaking, the pattern loses energy and the breakout — in either direction — is weaker and choppier. **Filter:** favour patterns that resolve in the first two-thirds of the distance to the apex. Avoid entering a triangle that has gone stale at the point.

**Wrong context.** An ascending triangle appearing at the *end of a long, extended uptrend* can be a distribution trap where the higher lows are retail chasing while institutions quietly sell into the flat top. **Filter:** check *who* is buying — flat/declining delivery volumes, weakening breadth, or building (not unwinding) call OI on the ceiling suggest distribution, not accumulation.

**Ignoring the broader market.** In a falling Nifty, even a beautiful ascending triangle on a single stock is fighting the tide; its breakout is more likely to fail or fizzle. **Filter:** trade breakouts with the market, not against it. Size down when the index is weak.

**Forcing the pattern.** Beginners draw triangles onto random noise — two vaguely-flat highs and two vaguely-rising lows are not a triangle. **Filter:** demand the minimum touch points, a genuinely flat top and genuinely rising lows, and the volume coil. If you have to squint, it is not there.

**The break-then-fail-back.** Even a valid breakout can fail if the follow-through buying doesn't arrive — a close back below the flat line after breaking out is a strong reversal signal. **Management:** honour the stop; do not rationalise. A failed ascending triangle can drop rapidly to its base as trapped breakout buyers bail.

Pros treat every triangle as a hypothesis with an invalidation level, not a prophecy. The edge comes from taking many well-filtered setups with defined risk, letting the winners run to the measured move (and beyond via a trailer), and cutting the fakeouts fast.

## Interview-ready summary

"An ascending triangle is a bullish continuation pattern: a flat horizontal resistance across equal highs, with a rising trendline of higher lows underneath. The flat top is a fixed supply wall; the higher lows show demand getting more aggressive and absorbing that supply. Volume contracts as it coils, then expands on the breakout. I enter on a *close* above the flat line with volume ≥ 1.5–2x average — or on a retest of the broken level as new support — stop below the last higher low, and target the measured move: the triangle's height added to the breakout level. On Nifty or Bank Nifty I get extra confluence from the option chain: the flat resistance usually sits on a heavy call strike, and if that call OI unwinds as price breaks out, the writers themselves are confirming the move. It's a probability, not a certainty — roughly two-thirds resolve up in a trending context — so I always trade it with a defined stop, and I respect a close back inside the pattern or a break of the rising trendline as failure."
