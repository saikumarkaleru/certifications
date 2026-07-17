# Harmonic Patterns: Butterfly, Crab & Trading Rules

## What it is & why it works

Harmonic patterns are precise, geometry-based reversal patterns built from **Fibonacci ratios that measure the retracements and extensions between five turning points** — labelled X, A, B, C and D. Where a classic double top or head-and-shoulders is loosely defined by shape, a harmonic pattern is defined by *numbers*: each leg must retrace or extend a prior leg by a specific Fibonacci ratio, within a tolerance, or the pattern is simply not valid. The trade is taken at point D — the **Potential Reversal Zone (PRZ)** — where several Fibonacci projections cluster and price is expected to turn.

The two patterns this chapter concentrates on — the **Butterfly** and the **Crab** — belong to the family codified by Scott Carney (building on H.M. Gartley's 1935 work and Larry Pesavento's Fibonacci overlay). They share a common skeleton with the Gartley and Bat but differ in one decisive way: **the D point finishes *beyond* the origin X**, not inside it. That single fact changes everything about how you trade them. The Butterfly and Crab are *extension* patterns — they catch exhaustion moves and blow-off spikes, whereas the Gartley and Bat are *retracement* patterns that finish inside the XA leg.

Why does this geometry work at all? Not magic. Three behavioural forces are at play. First, **Fibonacci self-similarity in crowd behaviour** — markets move in impulsive and corrective waves, and the proportions of those waves cluster around 0.382, 0.5, 0.618, 0.786, 1.272, 1.618 because traders anchor their profit-taking and re-entry to prior swings. Second, **stop-loss and liquidity engineering** — the Crab in particular finishes at a 1.618 extension of XA, which is exactly where a fresh trend looks most convincing and where breakout traders pile in and late shorts capitulate. That is precisely the point of maximum vulnerability to a snap-back. Third, **confluence of levels** — a valid PRZ is not one number but a tight band where a BC extension, an XA extension and often a round number or option strike all overlap, giving a genuine supply/demand shelf.

Be honest about what this is: harmonics are a **probability framework with a superb reward-to-risk profile, not a crystal ball.** The edge is not that D is guaranteed to reverse — it isn't. The edge is that you know *exactly* where you are wrong (just beyond D) and *exactly* where you profit (back toward C, then A), so a 40-45% hit rate still compounds because the winners pay 2-4x the losers. Indian traders using these on Nifty, Bank Nifty and liquid F&O stocks get the added bonus that the PRZ frequently lines up with a heavy option strike, and OI data can confirm the turn.

## The mechanics

Every harmonic has five points and four legs:

- **XA** — the initial impulse leg (the reference for everything).
- **AB** — the first retracement of XA.
- **BC** — a retracement of AB.
- **CD** — the final leg into the PRZ; measured two ways: as a retracement/extension of BC, and as an extension of XA.

The **AB=CD** structure (two equal legs, or a Fibonacci-scaled version) sits inside the pattern as a confirming sub-structure. The distinguishing ratios are:

| Ratio | Butterfly | Crab |
|---|---|---|
| **B retracement of XA** | **0.786** (strict) | **0.382 – 0.618** (flexible) |
| **BC retracement of AB** | 0.382 – 0.886 | 0.382 – 0.886 |
| **CD extension of BC** | 1.618 – 2.24 | **2.24 – 3.618** (deep) |
| **D as extension of XA** | **1.272** (ideal), up to 1.618 | **1.618** (strict) |

Read that table carefully — the two identifiers that matter most are the **B point** and the **D point**:

- **Butterfly:** B must sit at the **0.786 retracement of XA**. D projects to the **1.272 extension of XA** (occasionally 1.618). It is a moderate overshoot of the origin.
- **Crab:** B is shallow and flexible (0.382-0.618). D projects to the **1.618 extension of XA** — a *deep* overshoot. The Crab is the most extended of all harmonics, which is why its stop is tight relative to its target and its reward-to-risk is the best in the family.

A quick way to remember it: **Butterfly = 0.786 B, 1.272 D. Crab = shallow B, 1.618 D.** The Crab flies further out.

**Bullish vs bearish.** A **bullish** Butterfly/Crab is an M-into-a-low shape: XA down, AB up, BC down, CD down to a *new low* below X, where you go **long**. A **bearish** one is the mirror: XA up, AB down, BC up, CD up to a *new high* above X, where you go **short**. Point D always pokes past X — that is the trap.

**Tolerance.** Ratios are never exact. Professionals allow roughly **±3-5%** on the key ratios. If B is at 0.80 instead of 0.786, fine; if it's at 0.71, it's drifting toward a Gartley and you should relabel. Purists demand the D projections (the two lines that form the PRZ) fall within a narrow band; a PRZ that is 4% wide on Nifty (say 180 points) is too loose to trade with a tight stop.

**Construction workflow (TradingView / Chartink users):**

1. Identify a clean impulse leg XA on your timeframe (1H, 4H or daily for swings; 5-15 min for intraday index scalps).
2. Use the **XABCD Pattern** tool (built into TradingView) — it auto-labels and displays the live ratios so you don't compute by hand.
3. Draw a **Fibonacci extension** from X-A-B: the 1.272 and 1.618 lines are your Butterfly and Crab D targets.
4. Draw a **Fibonacci extension of BC** (using the 1.618, 2.24, 3.618 levels).
5. Where the XA-extension line and the BC-extension line **cluster within a tight band, that band is your PRZ.** That is D.

**The PRZ is a zone, not a point.** In practice you get two or three numbers within a few points/rupees of each other. On Nifty that might be a 30-50 point band; on a ₹1,500 stock, an ₹8-12 band. You wait for price to *enter* the zone and *show a reaction* — you do not blindly buy the exact line.

## Reading it — a worked Bank Nifty example

Let me walk a **bearish Crab on Bank Nifty on the 1-hour chart** phase by phase, with realistic 2026 levels.

**Phase 1 — the XA impulse (X = 48,200, A = 49,600).** Bank Nifty bottoms at **48,200** after a two-day slide and rips 1,400 points to **49,600** on a strong RBI-policy-day candle. This up-leg is XA. Because the pattern will be *bearish*, we are hunting a high above A where price exhausts and turns down — a short.

**Phase 2 — the AB retracement (B = 49,060).** Price pulls back from 49,600 to **49,060**. Measure it: the drop is 540 points against a 1,400-point XA leg = **0.386 retracement**. That is a shallow B, squarely in the Crab's 0.382-0.618 window. (Had it retraced to 49,000-ish giving 0.786, we'd be building a Butterfly instead.) So we tentatively label this a Crab.

**Phase 3 — the BC leg (C = 49,470).** Price rallies again from 49,060 to **49,470**, retracing the AB down-move. AB was 540 points; BC is 410 points up = **0.759 retracement of AB** — comfortably inside the 0.382-0.886 band. Good. Now C is set at 49,470, just *below* the A high — a lower high that keeps the structure alive.

**Phase 4 — projecting D (the PRZ).** Two calculations define where to short:

- **XA 1.618 extension:** XA = 1,400 points. 1.618 × 1,400 = 2,265. From X (48,200), D = 48,200 + 2,265 = **50,465**.
- **BC 3.618 extension:** BC = 410 points. 3.618 × 410 = 1,483. From C (49,470)... but for the extension we project the CD leg; using Carney's deep BC extension the projection lands near **50,400-50,500.**

Both lines cluster around **50,430-50,470** — a tight ~40-point PRZ. Note D (≈50,465) sits *well above* the A high of 49,600. That deep poke above the origin is the Crab's signature: it looks like a breakout to fresh highs, sucking in longs and stopping out shorts, right at the point of exhaustion.

**Phase 5 — the reaction.** Bank Nifty grinds up over the next few hours, tags **50,455** intraday on a spike, prints a bearish pin bar / shooting star on the 1-hour, and the volume on the spike is lower than the XA rally's volume (bearish divergence of effort). RSI on the 1H is at 78 and diverging — price made a higher high, RSI made a lower high. The PRZ has done its job. This is your short trigger.

## Trading it

**Entry.** Do not short the instant price touches 50,430. Wait for the PRZ to be *entered* and a **reversal confirmation** to print: a bearish engulfing, shooting star, or a lower-timeframe (5-min) structure break below the last swing low. In our example, enter short on the close of the 1H shooting star at **≈50,410**, or on a 5-min break of 50,380.

**Stop.** The beauty of the Crab is a tight, logical stop. Place it just **beyond the PRZ's outer edge plus a buffer** — say above **50,560** (about 100-120 points, or one ATR of 1H Bank Nifty). If price closes above the 1.618 extension by more than the buffer, the pattern is invalidated — the "reversal" was a real breakout. Risk = 50,560 − 50,410 = **150 points.**

**Targets (measured moves).** Harmonics have standard profit targets derived from the CD leg:

- **T1 = 0.382 retracement of CD** → partial book. CD ran roughly from C (49,470) to D (50,465) ≈ 995 points; 0.382 × 995 ≈ 380 → T1 ≈ **50,085.** Reward ≈ 325 points → **~2.2R**, booked on a third of the position.
- **T2 = 0.618 retracement of CD** → 0.618 × 995 ≈ 615 → T2 ≈ **49,850.** ~3.7R.
- **T3 = point A (49,600)** or the B point → the classic full target for extension patterns is a return to A. Reward ≈ 810 points → **~5.4R.**

**Management.** Book a third at T1, move stop to entry (risk-free). Book a third at T2, trail the remainder using the 1H swing highs or a short EMA. On the final third let a return to A run; if momentum stalls at the 0.618, take it. A realistic outcome: T1 and T2 hit, final third trailed out near 49,900 — a blended ~3R trade on a 150-point risk.

**Scenario B — it fails cleanly.** Price tags 50,455, you short at 50,410, and instead of rolling over it grinds up and closes above 50,560. You are stopped for −150 points. No drama — the invalidation was crisp and cheap. This is the point: with harmonics you lose small and known amounts, and the extension geometry means failures are usually *fast* (a genuine breakout accelerates), so you're not bled slowly.

**Scenario C — Butterfly variant.** Had B printed at 0.786 (≈49,500 on a bullish setup, or the mirror), D would have projected to the **1.272** extension = 48,200 + 1.272×1,400 ≈ **49,980** rather than 50,465. The Butterfly's shallower overshoot means a *closer* entry to A, a slightly wider relative stop, and a target back to A that is a smaller move — a lower R multiple than the Crab but a higher hit rate because the overshoot is less extreme.

## Confluence — stacking the odds

A harmonic taken in isolation is a 40-something-percent bet. Layer confluence and you push it toward 55-65%:

- **Structural S/R.** Does the PRZ sit at a prior swing high/low, a supply zone, or a weekly pivot? Our 50,465 PRZ landing near a round 50,500 and a prior monthly high massively strengthens it.
- **RSI / momentum divergence.** The single best harmonic filter. Price makes the new extreme at D while RSI/MACD makes a *lower* high (bearish) — that divergence at the PRZ is your green light. No divergence = weaker trade.
- **Candlestick trigger at D.** Never enter on the ratio alone. Demand a pin bar, engulfing, or lower-timeframe CHoCH (change of character).
- **Option-chain / OI (the India edge).** This is where Indian index harmonics shine. At a bearish PRZ of 50,400-50,500 Bank Nifty, check the option chain: is there **massive Call OI at the 50,500 strike** acting as a supply wall? Is Call writing *increasing* as price approaches (writers confident of a cap)? Heavy Call OI + rising Call writing at your PRZ is powerful confluence — the option market is independently marking the same ceiling. Conversely, a bullish PRZ that coincides with a fat **Put OI strike** (a floor) and aggressive Put writing confirms the demand shelf. **Max-pain** sitting near your PRZ on expiry week adds a magnetic pull toward the reversal.
- **VWAP / anchored VWAP.** If D also tags the anchored VWAP from the swing origin, institutions are likely to defend it.
- **Higher-timeframe trend.** A bearish harmonic *against* a strong daily uptrend is a counter-trend fade — take it smaller or wait for a full 5-min trend break. A bearish harmonic that turns down *into* an established daily downtrend is a with-trend continuation — press it.

The ideal trade: Crab PRZ + round number + RSI divergence + shooting star + heavy Call OI at the strike. That five-way stack is a high-conviction short.

## Pitfalls & false signals

**1. Force-fitting the pattern.** The commonest failure. Traders drag the XABCD tool until the ratios *almost* fit, then trade a pattern that isn't there. Discipline: if B is not within ±5% of its required ratio (0.786 for Butterfly, 0.382-0.618 for Crab), it is a different pattern or no pattern. Relabel or pass.

**2. Trading the line, not the reaction.** D is a *zone* where reversals become probable, not a guaranteed turn. Entering the instant price touches the extension line — with no candle confirmation — gets you run over when the PRZ is exceeded. Always wait for the reaction.

**3. Deep extensions can keep extending.** The Crab's 1.618 is a point of exhaustion *often*, not always. In a genuine breakout or news-driven trend day, price blows through 1.618 to 2.0 and beyond. This is why the hard-stop just past the PRZ is non-negotiable — no "give it room," no averaging into the loser.

**4. Wrong timeframe / illiquid names.** Harmonics need clean swings and real two-sided flow. They work well on Nifty, Bank Nifty, Fin Nifty and liquid large-caps (Reliance, HDFC Bank, ICICI, Infosys). On thin mid/small-caps the swings are gappy and the Fibonacci proportions are noise. On sub-5-minute index charts, spread and whipsaw eat the edge.

**5. News overrides geometry.** An RBI surprise, a US CPI print, a budget announcement, or a stock's earnings will invalidate any pattern instantly. Never hold a harmonic through a known event at the PRZ — flat or hedge into the event.

**6. Ignoring the higher-timeframe trend.** A textbook bearish Crab in a raging bull market is a low-probability fade. Pros filter every harmonic through the dominant trend and either skip counter-trend signals or size them down and demand extra confluence.

**7. Confirmation via cherry-picking.** It's easy to find *a* Fibonacci level near any price. The honest test is whether the ratios were defined *before* D formed and whether the PRZ is genuinely tight. A 200-point-wide "PRZ" on Nifty is unfalsifiable and untradeable.

How pros filter: they demand (a) clean, unambiguous swing points; (b) ratios within tolerance defined in advance; (c) a tight PRZ (ideally two projections within ~0.3-0.5% of price); (d) momentum divergence; (e) a candle/structure trigger; and (f) for Indian indices, corroborating OI at the strike. Fail two or more of those and the setup is skipped, not forced.

## Interview-ready summary

*"Harmonic patterns are five-point (XABCD) reversal structures defined by Fibonacci ratios, where you trade the reversal at point D — the Potential Reversal Zone. The Butterfly and Crab are the *extension* patterns: unlike the Gartley and Bat, their D point finishes **beyond** the origin X. The **Butterfly** is identified by B at the **0.786** retracement of XA and D at the **1.272** extension of XA. The **Crab** has a shallower, flexible B (0.382-0.618) and a deeper D at the **1.618** extension of XA — it's the most extended harmonic, which gives it the tightest stop and best reward-to-risk in the family.*

*The trade: wait for price to enter the PRZ, demand a reaction — a candlestick trigger plus momentum divergence — then enter with a hard stop just beyond D and targets at the 0.382 and 0.618 retracements of the CD leg, with a full target back to point A. On Indian indices I stack confluence: the PRZ against a round number or supply zone, RSI divergence, and crucially the option chain — heavy Call OI and rising Call writing at a bearish PRZ, or a fat Put strike at a bullish one, independently confirms the level. The honest framing is that this is a probability-and-risk framework: maybe a 40-45% hit rate, but because you know exactly where you're wrong and win 2-5R when right, it compounds. The cardinal sins are force-fitting the ratios and trading the line instead of the reaction."*
