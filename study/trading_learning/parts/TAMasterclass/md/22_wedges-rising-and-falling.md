# Rising & Falling Wedges

## What it is & why it works

A wedge is a chart pattern where price gets squeezed between two **converging trendlines that both slope in the same direction**. That single feature — both lines tilting the same way while narrowing — is what separates a wedge from a triangle (where at least one line is roughly flat) and from a channel (where the lines are parallel). The wedge is fundamentally a **momentum-exhaustion pattern**: price keeps making progress in the direction of the slope, but each new push travels less distance than the last, and the pattern tells you the trend is running out of fuel.

There are two shapes and, crucially, the *bias is opposite to the slope*:

- A **rising wedge** slopes up (both trendlines rising, the lower rising faster so the lines converge) and is **bearish**. Price is grinding higher, but with shrinking enthusiasm — buyers have to work harder for smaller gains. When it breaks, it breaks *down*.
- A **falling wedge** slopes down (both lines falling, the upper falling faster) and is **bullish**. Sellers keep pressing lower but the down-legs are shortening. When it breaks, it breaks *up*.

The behaviour behind it is straightforward once you picture the order flow. In a rising wedge, imagine a Nifty rally where each higher high comes on weaker breadth and thinner volume. The trend-followers are still buying, but the marginal buyer is arriving slower while early longs quietly distribute into the strength. The converging lines are the geometric fingerprint of demand decelerating faster than supply. Eventually the last marginal buyer is used up, the ascending support line snaps, and the accumulated longs rush the exit at once — hence wedges often break *sharply*, retracing a large part of the move that built them.

Wedges appear in two contexts, and telling them apart matters:

1. **Reversal wedges** form at the *end* of a mature trend. A rising wedge after a long uptrend warns of a top; a falling wedge after a long downtrend warns of a bottom. These are the higher-conviction versions.
2. **Continuation wedges** form as a *counter-trend pause* inside an ongoing trend. A falling wedge that appears as a pullback within a strong uptrend resolves upward (with the trend); a rising wedge as a bounce within a downtrend resolves downward. Here the wedge is just a "breather" against the primary trend.

The common thread — and why the pattern earns its place in a serious trader's toolkit — is that a wedge lets you position *ahead* of a directional resolution with a tight, well-defined stop, because the converging apex mechanically compresses the risk. In Indian markets, wedges show up constantly on Bank Nifty (which trends hard and reverses hard) and on momentum midcaps that grind up on retail froth before rolling over.

## The mechanics — construction, rules and settings

**Drawing the lines.** A valid wedge needs at least two touches on each line, ideally three, so you have four to six reaction points total. Both lines must slope the same direction and must *converge* — if you extend them, they meet at an apex. The angle of convergence is what gives the wedge its "squeeze."

| Feature | Rising wedge | Falling wedge |
|---|---|---|
| Slope of both lines | Up | Down |
| Which line is steeper | Lower (support) rises faster | Upper (resistance) falls faster |
| Directional bias | Bearish (breaks down) | Bullish (breaks up) |
| Volume through pattern | Typically declining | Typically declining |
| As reversal | Top of uptrend | Bottom of downtrend |
| As continuation | Bounce in downtrend | Pullback in uptrend |
| Break confirmation | Close below lower line | Close above upper line |

**Volume signature.** The textbook wedge shows **volume contracting** as the pattern matures — fewer shares/contracts traded on each successive swing, mirroring the fading momentum. The confirming break should then come on a **volume expansion**. On Indian intraday charts you can proxy this with tick volume or, better, use cumulative delta / the futures volume; on daily charts, use NSE delivery-based volume for stocks. A rising wedge that breaks down on a volume surge is far more trustworthy than one that leaks out quietly.

**Duration and timeframe.** Wedges are scale-invariant — you'll see them on a 5-minute Bank Nifty chart and on a weekly Reliance chart. The rule of thumb: a wedge usually resolves somewhere between **two-thirds of the way to the apex and the apex itself**. If price grinds all the way to the apex and just fizzles, the pattern loses energy and the break becomes unreliable. Best breaks come in that 60–75% zone.

**The break point and confirmation.** Do not act on the first poke through a line. Require a **candle close beyond the line** on your trading timeframe (a 15-min or hourly close for intraday; a daily close for swing). Many pros add a filter: the breakout candle should close beyond the line by more than a fraction of ATR (e.g., > 0.25× ATR) to filter noise, or wait for a **retest** of the broken line that holds.

**The measured move / target.** Two standard methods:

- **Pattern-height projection:** measure the vertical height of the wedge at its *widest* point (the base), then project that distance from the breakout point in the break direction.
- **Full-retracement expectation:** wedges frequently retrace to (or beyond) the point where the wedge *began* — its origin. For a rising wedge, that means a slide back to the level where the rally into the wedge started. This is often the more generous and, empirically, common target for reversal wedges.

**Stop placement.** For a rising wedge short, the stop sits just above the last swing high inside the wedge (or above the upper line). For a falling wedge long, just below the last swing low (or below the lower line). Because the lines converge, the later in the pattern you enter, the tighter this stop — that is the wedge's structural gift to your risk-reward.

## Reading it — a worked India example, phase by phase

Let's walk a **rising wedge as a top on Bank Nifty**, using realistic 2026-style levels on the hourly chart.

**Phase 1 — the run-up (context).** Bank Nifty has rallied from around ₹48,200 to ₹51,000 over two weeks on strong FII buying and a good earnings season from HDFC Bank and ICICI. The move is mature; RSI on the daily has been pinned above 65. This is exactly the environment where a rising *reversal* wedge tends to form — a tiring uptrend, not a fresh one.

**Phase 2 — the wedge builds.** Over the next five sessions, price keeps ticking higher but in a visibly narrowing pattern:

- Swing high 1: ₹51,050, pullback low ₹50,700 (range ₹350)
- Swing high 2: ₹51,240, pullback low ₹50,980 (range ₹260)
- Swing high 3: ₹51,360, pullback low ₹51,180 (range ₹180)

Connect the highs (₹51,050 → ₹51,240 → ₹51,360): an upper line rising gently. Connect the lows (₹50,700 → ₹50,980 → ₹51,180): a lower line rising *faster*. The two converge — a rising wedge. The height at the base is roughly ₹51,050 − ₹50,700 = **₹350**. Volume on the futures has thinned on each new high, and the daily RSI is now printing a lower high against price's higher high — a **bearish divergence** that confirms the momentum story.

**Phase 3 — the option-chain tell.** As price grinds to ₹51,360, the weekly option chain shows heavy **call writing** building at the 51,500 strike (open interest jumping), while put OI at 51,000 is starting to *unwind*. Translation: sophisticated participants are selling upside and stepping back from downside protection — they don't expect much more up, and they're comfortable that a fall is coming. This is confluence that the wedge's bearish bias is real, not just a drawing.

**Phase 4 — the break.** On the sixth session, price fails at ₹51,340 (a lower high — the wedge is now near 70% to its apex), then an hourly candle closes at ₹51,120, **below the lower line** which was around ₹51,250 at that time. The break candle is a wide-range bearish bar and futures volume spikes to well above the session average. This is the confirmed breakdown.

**Phase 5 — the resolution.** Price accelerates. The pattern-height target: ₹51,250 (break point) − ₹350 = **₹50,900**, hit within the same session. The fuller reversal target — back to the wedge's origin around ₹50,700 — is reached the next morning, and price keeps sliding to ₹50,450 as the 51,000 puts that were unwound get hastily re-bought. A trader who read the wedge caught roughly ₹700–900 of Bank Nifty downside from a low-risk entry.

## Trading it — entries, stops, targets, management

I'll lay out both directions with concrete triggers.

**Rising wedge (short bias):**

- **Entry trigger:** Confirmed hourly/daily close below the lower (support) line. Aggressive traders may pre-position on a *lower high* forming against the upper line with a bearish reversal candle; conservative traders wait for the close-below, then take the *retest* of the broken line as the entry.
- **Stop:** Just above the most recent swing high inside the wedge. In the Bank Nifty example, short at ₹51,120 with a stop at ₹51,400 — risk ₹280.
- **Target 1:** Pattern height from break point → ₹50,900. Book partial, trail the rest.
- **Target 2:** Wedge origin / full retrace → ₹50,700 and beyond.
- **Reward-to-risk:** Risking ₹280 to make ₹350–650 is roughly 1.3R to 2.3R — respectable, and it improves the later you enter because the converging stop tightens.

**Falling wedge (long bias):** the mirror image. Say Nifty pulls back within an uptrend from ₹24,800 to ₹24,300 in a falling wedge (down-legs shortening: −180, −120, −70). Entry on a 15-min close above the upper line at, say, ₹24,420; stop below the last swing low at ₹24,290 (risk ₹130); target the pattern height (~₹250) → ₹24,670, then the prior high near ₹24,800. This is a classic **continuation** falling wedge — a bull-flag-like pause that resumes the uptrend.

**Multiple scenarios and management:**

1. **Clean break, no retest (momentum break):** price leaves the line and runs. Move stop to breakeven after Target 1, trail under/over swing points. Don't chase a re-entry — the R:R is gone.
2. **Break-and-retest:** the ideal. Price breaks, pulls back to kiss the broken line, and rejects. Enter (or add) on the rejection candle with a very tight stop beyond the line. Highest-probability version.
3. **False break / fake-out:** price closes beyond the line then snaps back inside within a candle or two. Honour your stop *immediately* — wedges are notorious for one fake move before the real one. If stopped, you can often re-enter on the genuine break that follows.
4. **Apex fizzle:** if price crawls all the way to the apex and coils sideways, stand aside. The energy has bled out; the eventual move is weak and directionless. Wait for a fresh setup.

**Position sizing** should be driven by the stop distance and a fixed fractional risk (e.g., 1% of capital). Because wedge stops are tight, you can carry a meaningful position without oversized risk — but resist the temptation to widen the stop just to "give it room," which defeats the pattern's whole advantage.

## Confluence — stacking the odds

A wedge in isolation is a decent signal; a wedge with confluence is a high-conviction trade. Layer these:

- **Momentum divergence:** the single most powerful confirmer. A rising wedge with **bearish RSI/MACD divergence** (price higher high, oscillator lower high) is textbook exhaustion. A falling wedge with **bullish divergence** signals a bottom. In the Bank Nifty example, the RSI lower-high was the early warning before the break.
- **Volume:** contracting into the pattern, expanding on the break. Falling volume through a rising wedge is precisely the "fading demand" the pattern is meant to capture.
- **Option-chain / OI:** as shown — call writing stacking above a rising wedge, or put writing / call unwinding below a falling wedge, tells you where the smart money expects price to *not* go. Max-pain shifting toward the break direction adds weight. A rising wedge topping right into a wall of call OI is a gift.
- **Key levels:** a rising wedge that tops out exactly at a prior swing high, a round number (Nifty 25,000), a VWAP band, or a Fibonacci retracement (61.8% of a prior down-move) is far more likely to fail there. Confluence of pattern + horizontal resistance is potent.
- **Higher-timeframe alignment:** a falling wedge on the hourly is much stronger if the daily trend is up (continuation with the tide). Trade wedge breaks *in the direction of the higher-timeframe bias* preferentially.
- **Candlestick trigger:** a bearish engulfing or shooting star at the top of a rising wedge, or a hammer/bullish engulfing at the base of a falling wedge, gives you a precise entry candle and a tighter stop.

The mental model: the wedge tells you *what* is likely (exhaustion + directional break) and *where* (the lines). Divergence tells you *momentum agrees*. OI tells you *positioning agrees*. Volume tells you *the crowd committed to the break*. When three or four line up, size up.

## Pitfalls & false signals

Wedges are genuinely useful but they trap the careless. Know the failure modes:

- **Over-drawing / seeing wedges everywhere.** Two converging lines are easy to force onto noisy price. Demand at least two clean touches per line and a genuine narrowing. If you have to ignore wicks or cherry-pick points, it isn't a wedge. Nifty and Bank Nifty in choppy, rangebound weeks generate dozens of "wedges" that mean nothing.
- **Trading before the close-confirmation.** The intra-candle poke through a line is the wedge's favourite bait. Wait for the *close* beyond the line. This one discipline filters out most fakeouts.
- **The single fake-out before the real move.** Even confirmed breaks often see one whipsaw. This is why the *retest* entry is safer than the break entry, and why a hard stop is non-negotiable.
- **Apex exhaustion.** Entering a wedge that has already crawled to its apex is low-odds — the compression is spent. The sweet spot is the 60–75% zone.
- **Confusing wedge direction with break direction.** Beginners see a rising wedge and think "it's going up." No — rising wedge is *bearish*. The slope and the bias are opposite. Burn this in.
- **Ignoring the higher timeframe.** A rising wedge on the 5-min inside a screaming daily uptrend can break down 100 points and then the primary trend simply eats it. Counter-trend wedge breaks against a strong higher-timeframe trend are lower-probability and should be traded smaller, if at all.
- **News override.** An RBI policy surprise, a Budget announcement, or a US CPI print will blow through any wedge. Around scheduled high-impact events, wedges are unreliable — either the break front-runs the news or the news invalidates the pattern. Size down or stand aside into known event risk.

Pros filter wedges by insisting on the *combination*: proper construction, contracting volume, a close-confirmed break on expanding volume, momentum divergence, and — for Indian index trades — an option-chain that isn't fighting the direction. Absent that stack, they treat a lone wedge as a *watch*, not a *trade*.

## Interview-ready summary

"A wedge is two trendlines converging while both slope the same way, and the key counter-intuitive point is that the bias is *opposite* to the slope. A **rising wedge** — both lines up, lower line steeper — is **bearish**: it marks demand decelerating and typically breaks down, often retracing the whole move that built it. A **falling wedge** — both lines down, upper line steeper — is **bullish** and breaks up. It works because the narrowing captures fading momentum: each new push travels less distance than the last. I confirm with contracting volume into the pattern, a *close* beyond the line on expanding volume, and ideally momentum divergence. On an Indian index like Bank Nifty I add the option chain — a rising wedge topping into heavy call-writing at the strike above is a high-conviction short. I measure the target as the pattern's base height projected from the break, or a full retrace to the wedge's origin, place my stop just beyond the last swing inside the wedge (which tightens as the lines converge), and I prefer the break-and-retest entry because a single fakeout before the real move is common. As reversal patterns at the end of a mature trend they're strongest; as continuation patterns against the primary trend they're just pauses. Above all, TA is probabilities — I trade the wedge with a defined stop and never bet the pattern is certain."
