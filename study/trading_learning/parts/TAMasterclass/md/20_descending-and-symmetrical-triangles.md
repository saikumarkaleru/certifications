# Descending & Symmetrical Triangles

## What it is & why it works

The ascending triangle has two close relatives that complete the family: the **descending triangle** (its bearish mirror) and the **symmetrical triangle** (the neutral, tension-building coil). Together these three cover almost every triangular consolidation you will meet on Nifty, Bank Nifty and NSE stocks. A serious technical and derivatives analyst must read all three fluently, because they encode different balances of supply and demand and demand different tactics.

**The descending triangle** is the bearish counterpart. It has a **flat horizontal support line** across a series of lows that keep holding at roughly the same price, and a **descending trendline** connecting a series of *lower highs* above. The flat floor is a **demand zone** — a price where a wall of buyers keeps stepping in (a big put strike, an institution accumulating, an old support). But the lower highs tell the real story: sellers are getting more aggressive on every bounce, willing to sell at progressively lower prices. Demand is fixed; supply is pressing down and compressing time. Eventually buyers at the floor are exhausted, the support wall is eaten, and price breaks *down* on a surge of volume. In a downtrend it is a continuation pattern; it is the bearish twin of the ascending triangle's logic.

**The symmetrical triangle** is the pattern of pure *indecision resolving into a trend*. It has **two converging trendlines**: a descending line of lower highs and a rising line of higher lows, coiling toward an apex. Neither side has the upper hand — sellers cap each rally a little lower, buyers lift each dip a little higher, and the range narrows into a spring. The market is winding up energy. Because a symmetrical triangle has *no built-in directional bias*, it is best understood as a **continuation pattern by default**: it usually breaks in the *direction of the trend that preceded it*. A symmetrical triangle after a strong up-move tends to resolve up; after a sharp down-move, down. But it is genuinely two-sided, so you trade the break, not a prediction.

Why do these work? All three are visible maps of a **volatility contraction** — the market coiling as one side quietly wins the war of absorption. Volatility is mean-reverting: tight ranges are followed by expansion. The triangle tells you an expansion is coming and gives you defined lines that, when broken, reveal which side won. That is the edge: you don't predict the direction blindly, you let price *tell* you at a precise trigger, with a tight stop, capturing the volatility expansion.

Honesty: symmetrical triangles in particular are notorious for **fakeouts** — a false poke through one side before the real move the other way. And a descending triangle can, in a strong bull market, resolve *upward* against its bearish bias. These are probabilities. You trade them with defined risk.

## The mechanics

**Descending triangle — construction:**

| Element | Rule |
|---|---|
| Lows | ≥2 (ideally 3+) swing lows at ~the same price — a flat horizontal support. |
| Highs | ≥2 (ideally 3+) *lower* highs — a descending trendline. |
| Prior trend | Best as a continuation in a downtrend; can be a topping pattern after an uptrend. |
| Volume | Contracts through the coil; expands on the *downside* breakout (breakdowns need less volume confirmation than breakouts, but expansion helps). |
| Measured move | Height of triangle projected *down* from the breakdown point. |

> Descending-triangle target = Support level − (Highest high − Support)

**Symmetrical triangle — construction:**

| Element | Rule |
|---|---|
| Upper line | Descending trendline of ≥2 lower highs. |
| Lower line | Rising trendline of ≥2 higher lows. Both converge to an apex. |
| Bias | Neutral; defaults to continuation of the prior trend. |
| Volume | Should contract markedly as it coils; expand sharply on the resolving break. |
| Breakout timing | Ideally in the middle-to-two-thirds zone before the apex; late breaks fizzle. |
| Measured move | Two methods (below). |

**The two measured-move methods for a symmetrical triangle:**
1. **Height method:** take the widest part (the first/leftmost high minus the first low), and project that distance from the breakout point in the break direction.
2. **Apex/parallel (flagpole) method:** draw a line parallel to the *breakout* trendline starting from the first reaction high (for an up-break) — price often travels to that parallel channel line.

**Volume is the master mechanic for all three.** The coil must show *contracting* volume (declining participation as the spring winds). The resolving break must show *expanding* volume — for symmetrical triangles this is your single best fakeout filter. A break on limp volume is suspect; a break on 1.5–2x average volume is credible.

**Apex timing.** Draw the apex where the two lines meet. Statistically, breaks that occur between ~50% and ~75% of the horizontal distance to the apex are the most reliable. Once price grinds into the final tip, the stored energy dissipates and both breakout and follow-through weaken.

**Tools & settings.** TradingView Trendline tool for the lines; keep the volume pane visible and add a 20-period average-volume line if possible. Add a 20/50 EMA for trend context. For indices, overlay ATR to gauge how compressed the range is relative to normal — extreme compression precedes the biggest expansions. On Chartink you can approximate a symmetrical/descending coil by screening for narrowing Bollinger Band width plus lower highs (descending) or a flat support cluster.

## Reading it — a worked India example

**Descending triangle on a single NSE stock (daily).** Take a realistic setup in a weak IT stock during a sector pullback.

- **Lead-in:** The stock has been sliding from ₹1,700 to ₹1,500 as Nifty IT weakens on soft US guidance. Downtrend is intact, price below the 50-DMA.
- **Flat floor forms:** The stock finds buyers at **₹1,500** — an old support and a level with a heavy put-writing strike. It bounces to ₹1,560. Two weeks later it sells off again to **₹1,502** — same floor, second touch. Demand is defending ₹1,500.
- **Lower highs appear:** The first bounce topped ₹1,560; the next rally only reaches **₹1,540**; the next just **₹1,522**. Connect 1,560 → 1,540 → 1,522: a clean descending trendline of lower highs. Meanwhile the floor holds a third time near ₹1,500. Five touch points, a textbook descending triangle. Volume is drying up as the coil tightens.
- **The squeeze & OI tell:** Price is now pinned between the falling trendline (~₹1,515) and the ₹1,500 floor. The option chain shows the **1,500 put OI starting to fall** — the put writers who were defending the floor are covering, losing conviction. That is the pre-breakdown warning.
- **The breakdown:** On a weak session for Nifty IT, the stock opens ₹1,505 and closes **₹1,472** — a decisive close below ₹1,500 — on volume ~1.7x the 20-day average, with a sharp drop in 1,500 put OI (writers stopped defending) and fresh put buying below. The demand wall is gone. Measured move: height = 1,560 − 1,500 = **₹60**, projected down from ₹1,500 → **target ≈ ₹1,440**.
- **Follow-through:** The stock slides to ₹1,445 over the next week; the old ₹1,500 support now caps a weak bounce as *resistance* (polarity flip), offering a lower-risk short-add for those who missed the break.

**Symmetrical triangle on Nifty (daily).** Now the neutral coil.

- **Lead-in:** Nifty has rallied hard from 24,000 to 25,200 — a strong up-move. It then enters a choppy consolidation.
- **The coil:** Each rally makes a *lower high* — 25,200, then 25,120, then 25,060 (descending upper line). Each dip makes a *higher low* — 24,700, then 24,820, then 24,900 (rising lower line). The range narrows from ~500 points to ~150 points over three weeks. Volume/turnover contracts; India VIX drifts down. A symmetrical triangle is coiling, and because the prior trend was up, the base case is an *upward* resolution.
- **The apex approach & option chain:** By week three Nifty oscillates in a tight 24,950–25,050 band. Max-pain and the heavy call/put strikes sit right around 25,000 — the market is pinned. VIX is unusually low: the spring is wound tight.
- **The breakout:** Nifty closes **25,180**, clearing the descending upper line on volume/turnover expansion and a *jump in India VIX*, with 25,000 call OI unwinding (writers covering) and put writers rolling up — buyers won. Height method: widest part ≈ 25,200 − 24,700 = **500 points**, projected from the breakout ~25,050 → **target ≈ 25,550**.
- **Alternative (bearish) resolution:** Had Nifty instead closed below 24,900 (the rising line) on expanding volume with call writers holding firm at 25,000, the target would have been ~500 points *down* toward 24,400. The pattern doesn't tell you which — the break does.

## Trading it

**Descending triangle (short setup):**
- **Trigger:** a *close* below the flat support, volume expansion preferred. Breakdowns can be sharp, so some traders act on a strong intraday break with a stop-close-only confirmation.
- **Stop:** above the most recent lower high, or above the descending trendline, or above the breakdown candle's high (~0.5–1x ATR buffer). In the IT-stock example, stop above ₹1,522 or the breakdown candle high ~₹1,505.
- **Target:** measured move (₹1,440), scaled; trail the rest below a declining 20-EMA or the descending trendline.
- **Retest short:** the highest-probability entry is often the pullback that retests the broken floor as new resistance.

**Symmetrical triangle (trade the break, either way):**
- **Trigger:** a decisive close beyond either converging line on expanding volume. Because fakeouts are common, *demand the volume expansion and the close* — this is non-negotiable for symmetricals.
- **Stop:** on an up-break, below the breakout candle low or back inside below the rising line; on a down-break, above the breakdown candle high or back inside above the descending line. A move back inside the triangle is your invalidation.
- **Target:** height method or the parallel-channel method, whichever is nearer for a first book; scale and trail.
- **Bias tilt:** lean toward the direction of the pre-triangle trend, but *never* pre-commit before the break — take the trade the break gives you.

**Scenarios (both patterns):**
- *A — clean break to target:* scale out at the measured move, trail a runner.
- *B — break then retest:* add on the retest (broken line flips role), move stop to break-even.
- *C — fakeout / whipsaw:* price breaks one way on weak volume, snaps back inside, then breaks the *other* way. Symmetricals do this often. The volume filter avoids most; if trapped, exit on the close back inside and be ready to flip.
- *D — apex fizzle:* price grinds to the tip and oozes out with no follow-through — stand aside; there's no energy left.

**Position sizing:** fixed fractional risk (e.g., 1%). Size = risk ÷ (entry − stop). Symmetricals often give tight stops (the apex is close), which can mean attractive R:R when the volatility expansion arrives.

## Confluence

**Trend context.** A descending triangle *in a downtrend* (below a falling 50-DMA) is a high-conviction continuation short; the same pattern deep in a strong bull market is more likely to fail up — respect the tape. A symmetrical triangle strongly favours the prior trend's direction, so align with the higher timeframe.

**Volume & volatility.** All three need the contraction-then-expansion signature. For indices, **India VIX** is a superb companion: an unusually low, falling VIX during the coil signals a wound spring, and a VIX *jump* on the break confirms the volatility expansion is real, not noise. Bollinger Band width at multi-week lows into the apex says the same.

**Option-chain / OI (the Indian analyst's edge):**
- *Descending triangle:* the flat floor usually sits on a heavy **put-writing strike** — that put OI *is* the demand wall. If price breaks down and **put OI at the floor collapses** (writers covering), the breakdown is validated by the defenders themselves. Persistent put OI at the floor warns of a failed breakdown.
- *Symmetrical triangle:* watch which side's writers blink. If, on the break, **call OI unwinds** at the upper strike, buyers are winning; if **put OI unwinds** at the lower strike, sellers are winning. Max-pain shifting in the break direction and PCR turning add confidence.
- A rising VIX + call unwind + PCR turning up = strong up-break confluence; falling floor put OI + weak PCR + downtrend = strong down-break confluence.

**Support/resistance & round numbers.** A descending-triangle floor on a big round level or major prior support carries extra weight when it finally breaks. A symmetrical apex pinned to max-pain / a round number (Nifty 25,000) is classic.

**Momentum.** RSI/MACD alignment with the break direction (e.g., MACD crossing down as a descending triangle breaks) filters fakeouts. A bullish divergence at a descending-triangle floor is a warning the breakdown may fail.

**Breadth & sector.** Trade breakdowns when market breadth is weak and the stock's sector index is also breaking down; trade up-breaks when breadth and sector are supportive.

## Pitfalls & false signals

**Symmetrical fakeouts are the number-one trap.** These patterns whipsaw both sides before resolving. **Filter:** require a closing break *and* volume expansion; be willing to sit out the first poke and enter on the second, confirmed break — or on the retest.

**Descending triangle failing upward in a bull market.** The bearish bias is context-dependent. In a raging bull tape, a flat floor with lower highs can resolve *up* as buyers overwhelm the descending line. **Filter:** only press descending-triangle shorts when the broader trend and sector are also weak; treat one forming inside an uptrend as suspect.

**Apex drift.** Grinding to the tip kills the energy for all three. **Filter:** favour breaks in the 50–75% zone; abandon stale coils.

**Volume neglect.** A break with no volume/VIX expansion is the single most common reason a triangle trade fails. **Filter:** no expansion, no trade — especially for symmetricals.

**Over-drawing.** Not every convergence is a triangle. Demand the touch points, genuine converging lines, and the volatility contraction. Two random lines squeezed onto noise will "break" meaninglessly.

**Ignoring the retest / stop.** A break that closes back inside the triangle is failed — this is a high-quality reversal signal, not a dip to buy/sell into. **Management:** honour the invalidation; a failed symmetrical often runs hard the *other* way, and a failed descending-triangle breakdown (bear trap) can rocket up. Pros keep a small position to flip on a decisive failure.

**Counter-trend greed.** Taking a descending-triangle short against a strong up-market, or forcing a directional symmetrical bet before the break, is how accounts bleed. Let the break decide; align with the bigger picture.

## Interview-ready summary

"A descending triangle is the bearish mirror of the ascending: a flat support floor with lower highs pressing down. The floor is a demand wall; the lower highs show sellers getting more aggressive. It breaks down when buyers are exhausted, on expanding volume, and I target the triangle's height projected down from the floor — stop above the last lower high. On an NSE stock the floor is usually a heavy put strike, and when that put OI collapses on the break, the writers themselves confirm it. A symmetrical triangle is a neutral coil — lower highs and higher lows converging — that stores volatility and usually breaks in the direction of the prior trend, but it's genuinely two-sided, so I trade the break, not a prediction. I demand a *closing* break on expanding volume, ideally with an India VIX jump, because symmetricals are fakeout-prone. Target is the height projected from the break, or the parallel-channel method. All three are volatility-contraction patterns: tight range, then expansion. They're probabilities, not certainties, so I always define the invalidation — a close back inside the triangle means the pattern failed, and I respect it."
