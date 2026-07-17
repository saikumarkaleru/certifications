# Engulfing & Harami Patterns

## What it is & why it works

Engulfing and Harami are the two most important **two-candle reversal patterns** in Japanese candlestick analysis, and they sit at opposite ends of a single idea: the relationship between a candle and the one before it. In an **Engulfing** pattern, the second candle's real body completely swallows the prior candle's real body — the new session's participants overwhelm the old ones. In a **Harami** ("pregnant" in Japanese), it is the reverse: a large real body is followed by a small body that sits *inside* it — the momentum that was driving the trend suddenly stalls and gets absorbed.

Both patterns work because they are visual, compressed stories about **who won the fight for control of price over two sessions**, and about the *rate of change* of conviction.

Consider a **Bullish Engulfing**. Price has been falling. The first candle is red (bearish) — sellers still in charge, closing near the low. Then a second candle opens at or below the prior close (often gapping down at the open, so bears feel comfortable), and by the close of the session buyers have not merely held the line, they have driven price *above the entire body of the prior red candle*. Everyone who sold on that red candle, and everyone who shorted at the open expecting continuation, is now sitting on a loss. That is the mechanism: the pattern marks the exact bar where the marginal seller was exhausted and demand took over. A **Bearish Engulfing** is the mirror at a top — a green up-day is entirely engulfed by a large red day, trapping the last buyers.

The **Harami** works on a different, subtler behaviour: **momentum decay**. A long trend candle (say a big green day in an uptrend) shows maximum enthusiasm. The very next day, price opens *inside* that body and spends the whole session unable to expand the range in either direction — a small, indecisive body forms wholly within the prior day's body. Nothing has reversed yet, but the *acceleration has gone to zero*. Trends usually die of momentum loss before they reverse in price, and the Harami is the earliest fingerprint of that deceleration. It is a "warning" candle, not a "confirmation" candle — a distinction that matters enormously for how you trade each.

The reason these patterns have edge in Indian markets specifically is the same reason they work anywhere: they encode **stop-loss cascades and trapped positions**, which are universal. When a Nifty stock puts in a clean bullish engulfing at a support zone, the red-candle sellers' stops become the fuel for the next leg up. But India adds two texture points: overnight gaps are common (SGX Nifty / GIFT Nifty and US close set the tone), which makes engulfing bodies form more readily off gap opens; and single-stock circuit limits and low-float midcaps can produce *exaggerated* engulfing bodies that look powerful but are really just illiquidity. We will filter for both.

## The mechanics

Candlestick patterns are about the **real body** (open-to-close), not the wicks, unless a specific variant says otherwise. Here are the precise construction rules.

### Bullish Engulfing
| Rule | Requirement |
|---|---|
| Prior trend | A downtrend or a pullback into support must precede it |
| Candle 1 | A **down** (red) real body |
| Candle 2 | An **up** (green) real body |
| Engulfing condition | Candle 2 open ≤ Candle 1 close **and** Candle 2 close ≥ Candle 1 open (body engulfs body) |
| Strength cues | Larger candle-2 body, candle-2 close near its high, higher volume, candle-2 engulfs multiple prior bodies |

### Bearish Engulfing
| Rule | Requirement |
|---|---|
| Prior trend | An uptrend or a rally into resistance must precede it |
| Candle 1 | An **up** (green) real body |
| Candle 2 | A **down** (red) real body |
| Engulfing condition | Candle 2 open ≥ Candle 1 close **and** Candle 2 close ≤ Candle 1 open |
| Strength cues | Bigger red body, close near the low, volume expansion, occurs at a known resistance/round number |

A **strict** engulfing requires the wicks to also be engulfed (a full "outside bar"), but the classical definition is body-over-body. In practice, many traders demand the body-engulf plus a close in the outer third of the range, which combines engulfing with **closing strength**.

### Bullish Harami
| Rule | Requirement |
|---|---|
| Prior trend | Downtrend |
| Candle 1 | A **large down** (red) real body |
| Candle 2 | A **small** real body (colour matters less) contained within candle 1's body |
| Containment | Candle 2 open and close both lie *inside* candle 1's open–close range |
| Harami Cross | If candle 2 is a doji (open ≈ close), it is a **Harami Cross** — a stronger, more reliable variant |

### Bearish Harami
Same, mirrored: a large **green** body in an uptrend, followed by a small body sitting inside it. A Bearish Harami Cross (doji inside) is the stronger form.

### The comparison that clarifies everything
| Feature | Engulfing | Harami |
|---|---|---|
| Candle-2 size | **Large** (bigger than candle 1) | **Small** (smaller than candle 1) |
| What it signals | Reversal **underway** (control changed) | Momentum **stall** (control uncertain) |
| Signal strength | Stronger, more immediate | Weaker, needs confirmation |
| Best use | Entry on close or minor pullback | Wait for a confirming next candle |
| Analogy | A goal is scored | The attack breaks down at the box |

Timeframe matters. On the **daily** chart these carry the most weight for swing trades. On **weekly** charts an engulfing is a serious signal (weekly bearish engulfing on Nifty after a strong run is a genuine caution flag). On **5-/15-min intraday** charts they fire constantly and are far noisier — treat intraday engulfings only at key levels (VWAP, PDH/PDL, opening range) with volume.

## Reading it — a worked India example

Let me walk through a **Bullish Engulfing on Reliance Industries** on the daily chart, phase by phase, with realistic rupee levels.

**Phase 1 — the decline into support.** Reliance has drifted from about ₹1,320 down to a well-watched demand zone near **₹1,215–1,225**, an area that had acted as support twice in the previous three months and coincides roughly with the rising 200-DMA. Over five sessions the candles are mostly red, each closing near its low — sellers in control, sentiment sour, and the financial-news chatter negative. The final red candle closes at **₹1,222**, opening at **₹1,238** — a wide red body, apparent capitulation.

**Phase 2 — the engulfing session.** The next morning GIFT Nifty is soft and Reliance **gaps down** to open at **₹1,216**, printing a fresh low intraday at ₹1,209 that briefly undercuts the support zone. This is the crucial behavioural moment: the undercut triggers stop-losses of weak longs and tempts fresh shorts. But buyers step in — you can see it as the candle refuses to stay down, grinds higher through the afternoon, and closes strong at **₹1,245**.

Now check the rule: candle 2 opened at ₹1,216 (below candle 1's close of ₹1,222 ✓) and closed at ₹1,245 (above candle 1's open of ₹1,238 ✓). The green body ₹1,216→₹1,245 fully engulfs the red body ₹1,238→₹1,222. It is a textbook **bullish engulfing**, made stronger by three things: it printed a false breakdown of support (a spring), it closed near the session high, and volume was about 1.7× the 20-day average — the trapped-seller mechanism is fully in play.

**Phase 3 — confirmation and follow-through.** The next session opens at ₹1,248 and holds above the engulfing candle's midpoint (₹1,230). This "no pullback" behaviour confirms demand. Over the next two weeks Reliance travels to **₹1,300**, then **₹1,335**, retracing the entire prior decline.

Now contrast with a **Bearish Harami on Bank Nifty** (as an index, traded via futures/options). Bank Nifty has rallied hard from ~50,800 to **53,600** in eight sessions — a steep, near-vertical advance. The eighth day is a **huge green candle**, open 52,900, close 53,580, spanning nearly 700 points of enthusiasm. The ninth day opens *inside* that body at 53,300 and closes at 53,250 — a small red body wholly contained within the prior green body. That is a **bearish harami**. Note what it does *not* say: it does not say "sell now." It says the buyers who were adding 700 points a day just added nothing. Momentum has flatlined at a stretched level. The trader's job now is to wait for the *confirming* candle (a red close below the harami's low) before acting — which, in this example, arrives on day ten with a close at 52,700, and Bank Nifty then mean-reverts toward 51,800.

## Trading it

### Bullish Engulfing — the swing long (Reliance example continued)
- **Entry trigger:** Two acceptable styles. (a) *Aggressive:* buy on the close of the engulfing candle at ~₹1,245. (b) *Conservative:* place a buy-stop just above the engulfing candle's high (say ₹1,247) so you only enter if the next session confirms upward. The conservative entry avoids "engulf then fade" traps at the cost of a slightly worse price.
- **Stop-loss:** Below the *low* of the engulfing candle — here ₹1,209, so a stop at **₹1,205**. That is the level that, if broken, invalidates the whole trapped-seller thesis (the spring would have failed). Risk from a ₹1,245 entry ≈ ₹40 per share.
- **Target / management:** First target the prior swing high / measured retracement — ₹1,300 (₹55 reward, ~1.4R on the first leg; better on the conservative-plus-add basis). Second target ₹1,335. A clean approach: book half at ₹1,300, trail the rest under the rising 20-DMA or under each higher swing low. Move stop to breakeven once price closes above ₹1,265.

### Bearish Engulfing — the swing short / long exit
On an index like Nifty, a daily bearish engulfing at resistance is often better used to **exit longs and buy puts** than to naked-short cash. Say Nifty rallies to a supply zone at **24,850**, prints a green day, then a large red engulfing day closing at **24,640**. Entry: short Nifty future on close, or buy a slightly ITM put; stop above the engulfing high (24,880); target the prior demand shelf at 24,300, then 24,050. Because engulfings mark momentum shifts, options traders like them for **directional debit spreads** — a bear put spread 24,700/24,300 caps cost and defines risk.

### Harami — the "wait for the third candle" trade
Never trade a Harami on the pattern alone. The rule: **the confirming candle is your trigger.**
- Bearish Harami (Bank Nifty example): sell/short only when a candle closes **below the harami's low** (53,250 region). Stop above the large green candle's high (53,620). Target the last consolidation, ~52,000, then 51,800.
- Because Harami is a *deceleration* signal, it is ideal for **tightening stops on existing positions** and for **option sellers** — a bearish harami at the top of a range is a cue to write call spreads, since it signals the up-thrust is losing fuel even before price rolls over.

### Scenario management
1. **Clean follow-through:** trail and let it run to targets.
2. **Engulf then immediate reversal (fakeout):** if price closes back inside/through the engulfing candle's body against you the very next session, exit — the pattern failed; don't "hope."
3. **Harami with no confirmation:** if the third candle expands *in the trend's direction* instead (breaks the harami's high, in an uptrend), the momentum stall was temporary — stand aside or stay with the trend.

## Confluence

These patterns are mediocre in isolation and excellent at **decision zones**. Stack them:

- **Support/resistance & round numbers:** A bullish engulfing means far more at a tested demand zone or a round number (₹1,200, Nifty 24,000) than in the middle of nowhere. Location first, candle second.
- **Moving averages:** Engulfing off the 50-DMA or 200-DMA in an uptrend (a "buy the dip" signal) is one of the highest-quality swing setups on Nifty large-caps.
- **Fibonacci:** Bullish engulfing at the 61.8% retracement of a prior up-leg is a classic pullback long.
- **RSI divergence:** A bullish engulfing coinciding with bullish RSI divergence (price lower low, RSI higher low) is a powerful bottoming combination.
- **Volume:** Demand engulfing candles *want* above-average volume; a low-volume engulfing on an illiquid midcap is suspect.
- **Option-chain / OI (index & F&O stocks):** This is where India-specific confluence shines. A **bullish engulfing on Nifty near a strike with the highest Put OI** (a support wall where put writers are defending) is a high-probability long — the option writers' incentive aligns with the candle. Conversely, a **bearish engulfing at a heavy Call-OI strike** (resistance ceiling where call writers sit) confirms the supply. Watch for **PCR** shifting and for **Call writers adding OI** as price fails at the engulfing high — that adds weight to a bearish engulfing/harami. A bullish engulfing accompanied by **short-covering** (OI falling while price rises) is especially clean, because it shows trapped shorts fuelling the move — exactly the mechanism the candle depicts.

The general rule: **candlestick + location + confirmation + one momentum/flow tool.** Three aligned signals beat any single one.

## Pitfalls & false signals

1. **Engulfing in a range = noise.** In a sideways market you get bullish and bearish engulfings alternately at the range edges, most of which just oscillate. These patterns are *reversal* signals; they need a *trend* to reverse. No prior trend, no trade.

2. **Ignoring the close location.** A bullish engulfing whose candle closes in the *middle* of its range (long upper wick) is weak — sellers pushed back. Demand the close in the top third.

3. **Illiquidity fakes the body.** On thin midcaps and smallcaps, a single large order can create a huge "engulfing" body that reverses the next day. Filter by volume and by whether the stock is liquid enough to trust.

4. **Gap-driven engulfings on index-heavy days.** After a big US move, half the Nifty basket gaps together and prints engulfings that are really just the overnight gap, not genuine two-day battles. Discount engulfings caused purely by a large opening gap with no intraday follow-through.

5. **Trading the Harami as if it were an Engulfing.** The single most common error. A Harami is a *warning*, not a *trigger*. Acting on the harami candle itself, before confirmation, gets you chopped up because trends often pause (harami) and then resume.

6. **Fighting the higher timeframe.** A daily bearish engulfing inside a powerful weekly uptrend is usually just a pullback entry for the bulls, not a reversal. Always check the timeframe above.

**How pros filter:** location at a real level, close in the outer third, volume confirmation, alignment with the higher-timeframe trend for continuation setups (or a clear exhaustion context for reversals), and — for Harami — patience for the confirming candle. They also size for the *pattern's own invalidation* (stop beyond the pattern), not an arbitrary rupee amount.

## Interview-ready summary

"Engulfing and Harami are two-candle patterns describing opposite dynamics. An **engulfing** is a second candle whose body completely swallows the first — a *bullish engulfing* (red then a larger green that closes above the prior open) marks demand overwhelming supply after a decline, and traps the sellers; a *bearish engulfing* is the mirror at a top. It signals control has *changed*. A **harami** is the reverse geometry — a large trend candle followed by a small body inside it — signalling momentum has *stalled*, not reversed; the doji version, the *harami cross*, is stronger. The key discipline: an engulfing can be traded near its close with a stop beyond the pattern's low/high, but a harami must be *confirmed by the next candle* before acting. Both need context — a prior trend, a real support/resistance level, closing strength, and volume — and in Indian F&O they're most reliable when the candle sits at a heavy Put-OI support or Call-OI resistance strike, ideally with short-covering behind a bullish engulfing. In isolation they're coin-flips; at a decision zone with confluence they're high-probability."
