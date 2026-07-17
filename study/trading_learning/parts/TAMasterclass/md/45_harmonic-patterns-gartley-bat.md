# Harmonic Patterns: Gartley & Bat

## What it is & why it works

Harmonic patterns are precise, geometry-based reversal setups defined by specific Fibonacci ratios between the legs of a five-point price structure (X, A, B, C, D). Where an ordinary chart pattern like a double top is judged by eye, a harmonic pattern is judged by *measurement*: each leg must retrace or extend the previous one by a defined Fibonacci amount, within tolerance, or the pattern does not qualify. The two most important and reliable are the **Gartley** (published by H.M. Gartley in 1935 and later ratio-formalised by Scott Carney and Larry Pesavento) and the **Bat** (defined by Carney in 2001). Both produce a completion point — the **D** point, called the **Potential Reversal Zone (PRZ)** — where the trader anticipates a reversal, enters against the last leg, and places a tight stop just beyond X.

Why do they work? The honest answer combines three strands. First, a harmonic pattern is really a **structured way of finding Fibonacci confluence**. The PRZ is the point where several Fib measurements — a retracement of the XA leg, an extension of the BC leg, and an AB=CD projection — all converge in a tight band. That convergence is the same order-clustering logic that makes any Fib cluster work, but harmonics impose strict rules so the confluence is not manufactured after the fact. Second, harmonics encode a specific **rhythm of a completing correction**: an impulse (XA), a partial retrace (AB), a counter-move (BC), and a final push (CD) that exhausts into the PRZ. That rhythm mirrors how a corrective wave typically loses steam. Third, like all popular patterns, there is a **self-fulfilling** element — a large community of harmonic traders places orders at the same computed D, so reactions cluster there.

Be clear-eyed. Harmonics are counter-trend reversal patterns, and counter-trend trading is inherently lower base-rate than trend-following. The patterns fail regularly. Their apparent precision — "the B point must be exactly 61.8%" — can create false confidence. The genuine edge is not mystical geometry; it is that a valid pattern gives you a *very tightly defined* entry and a *very tight* invalidation (just beyond X), which produces excellent reward-to-risk *when the pattern works*. You are paid not by a high win-rate but by a large payoff on a modest stop. Treat harmonics as a disciplined framework for locating high-R reversal trades, always confirmed by other evidence — never as a crystal ball.

## The mechanics

Every harmonic is a five-point structure. Label the initial leg **X→A**. Then **A→B** retraces part of XA, **B→C** retraces part of AB, and **C→D** is the final leg into the PRZ. The pattern's identity is defined by the exact ratios of these legs. The critical, discriminating measurement is the **B-point retracement of XA** — it is what separates a Gartley from a Bat.

**Gartley ratios (bullish; mirror for bearish):**

| Leg | Ratio of | Required value |
|---|---|---|
| B | Retracement of XA | **61.8%** (the defining ratio) |
| C | Retracement of AB | 38.2% – 88.6% |
| D | Extension of BC | 127.2% – 161.8% |
| D | Retracement of XA | **78.6%** (D sits at 78.6% of XA) |
| AB=CD | Projection | Present (CD ≈ AB) |

**Bat ratios (bullish; mirror for bearish):**

| Leg | Ratio of | Required value |
|---|---|---|
| B | Retracement of XA | **38.2% – 50%** (never beyond 61.8%) |
| C | Retracement of AB | 38.2% – 88.6% |
| D | Extension of BC | **161.8% – 261.8%** |
| D | Retracement of XA | **88.6%** (D sits deep, at 88.6% of XA) |
| AB=CD | Projection | Often an *extended* 127% AB=CD |

**The key distinction to remember:** the Gartley's B is a *moderate* 61.8% retrace and its D completes at a *shallower* 78.6% of XA. The Bat's B is a *shallow* 38.2–50% retrace and its D completes *deeper*, at 88.6% of XA — very close to X. This matters enormously in practice: because the Bat's D at 88.6% sits so near X, the Bat offers an even tighter stop and therefore a superior reward-to-risk, at the cost of the pattern only completing after a deeper, scarier-looking final leg.

**The Potential Reversal Zone (PRZ).** D is not a single price but a *zone* formed by the overlap of (a) the XA retracement (78.6% Gartley / 88.6% Bat), (b) the BC extension (127.2–161.8% Gartley / 161.8–261.8% Bat), and (c) the AB=CD completion. When these three computations land in a tight band, you have a valid PRZ. The tighter they cluster, the better.

**Tolerance.** Real charts never hit ratios to the decimal. Allow roughly ±2–3% around each target ratio. If the B point is at 64% instead of 61.8%, it can still be a Gartley; if it is at 72%, it is not. Discipline about tolerance is what keeps harmonics objective rather than a shape you talk yourself into.

**Tools.** TradingView's built-in XABCD pattern tool draws the five points and auto-displays each leg's ratio, so you can validate against the tables above instantly. Manual Fibonacci retracement/extension on each leg works too but is slower. Scanners on some platforms auto-detect forming harmonics, but always hand-verify the ratios.

## Reading it — a worked bullish Bat on a Nifty stock

Take Reliance Industries. Assume a clean five-point structure forms over several weeks on the daily chart.

- **X = ₹2,750** (swing low, the origin)
- **A = ₹3,050** (swing high; XA leg = ₹300 up)
- **B = ₹2,915** — retracement of XA. (3,050 − 2,750 = 300; B has retraced 3,050 − 2,915 = 135, i.e. 135/300 = **45%**). A 45% B-retrace is squarely in the Bat's 38.2–50% window and *rules out* a Gartley (which needs ~61.8%). **This is a Bat.**
- **C = ₹3,010** — retracement of AB. AB = 3,050 − 2,915 = 135 down; BC = 3,010 − 2,915 = 95 up, i.e. 95/135 = **70%** retrace of AB (inside the allowed 38.2–88.6%). Valid.
- **D = the PRZ.** Now compute where D should complete:
  - *XA 88.6% retracement:* D = 3,050 − (0.886 × 300) = 3,050 − 266 = **₹2,784**.
  - *BC 161.8% extension:* CD leg projected down = C − 1.618 × BC = 3,010 − (1.618 × 95) = 3,010 − 154 = **₹2,856**... a 200% BC extension gives 3,010 − 190 = **₹2,820**; a 261.8% gives 3,010 − 249 = **₹2,761**. The Bat's deep D usually needs a large BC extension, so the ~2,760–2,790 area is where BC-extension and XA-88.6% converge.
  - *AB=CD (extended 127%):* CD ≈ 1.27 × AB = 1.27 × 135 = 171; D = 3,010 − 171 = **₹2,839**; a full 1.618 extended CD gives 3,010 − 218 = **₹2,792**.

The overlap of these computations clusters the **PRZ at roughly ₹2,780–2,800**, anchored by the critical 88.6% XA level at ₹2,784. Notice how close that is to X at ₹2,750 — only ₹34 away. That proximity is the Bat's signature and the source of its tight-stop advantage.

**Phase-by-phase.** After A at ₹3,050, Reliance sells off in the AB leg but only to ₹2,915 — a *shallow* 45% retrace, the first clue this is a Bat, not a Gartley. It bounces to C at ₹3,010 (a strong 70% retrace of AB that might tempt trend-continuation bulls), then rolls over into the final CD leg. This CD decline looks ominous — it's deeper than the AB leg — and it drives price down toward the PRZ. As price enters ₹2,800, the daily candles shrink; at ₹2,786 a long-legged doji / hammer prints, tagging the 88.6% level almost exactly, then closes back at ₹2,825. The pattern has completed at D inside the PRZ, and the reversal candle is the first confirmation.

## Trading it

**Entry.** Never buy the instant price touches the PRZ — the D-point is a zone and the final leg can overshoot. Two disciplined approaches:
- *Confirmation entry (preferred):* wait for a bullish reversal candle *inside* the PRZ that closes back up — here, the hammer closing at ₹2,825 — and enter on the close or on the break of that candle's high (₹2,850). This sacrifices a little price for a large jump in reliability.
- *Scaled limit entry:* place staggered buy limits across the PRZ band (e.g. ₹2,800 and ₹2,785) for a better average, accepting that you may be filled before the reversal confirms.

**Stop-loss — the heart of the edge.** The pattern is invalidated if price closes below **X (₹2,750)**, because D by definition must sit *above* X (at 88.6%). So the stop goes just below X — say **₹2,730**, a small buffer beyond the origin. This is the whole point of harmonics: entering near ₹2,825 with a stop at ₹2,730 risks only ~₹95. For a Gartley, whose D sits at the shallower 78.6% of XA, the stop below X is proportionally a bit wider relative to entry; the Bat's 88.6% D places entry closer to X, giving the tightest stop and best R.

**Targets.** Standard harmonic profit objectives are Fibonacci retracements of the *CD leg* (or of the whole AD move):
- **T1 = 38.2% retrace of AD**, or simply the C point ₹3,010 — book a third.
- **T2 = 61.8% retrace of AD**, near the A point ₹3,050 — book a third.
- **T3 = point A / full measured objective** ₹3,050 and beyond for a runner if momentum carries.

With entry ₹2,825, stop ₹2,730 (risk ₹95), and T1 at ₹3,010 (reward ₹185), the first target alone is ~1.9R; carrying to A at ₹3,050 (reward ₹225) makes it ~2.4R, and a runner beyond A on a trend continuation can push blended reward past 3R. That asymmetry on a ~₹95 stop is exactly why traders tolerate the pattern's modest win-rate.

**Scenario management.**
- *Clean reversal:* PRZ holds, confirmation candle prints, price rallies to targets. Base case — trail the runner under rising swing lows once T2 is booked.
- *PRZ overshoot then reclaim:* price dips to ₹2,760 (still above X), wicks, and closes back inside the PRZ. Because the stop is below X at ₹2,730, not inside the PRZ, you survive the flush. This is common and is precisely why the stop belongs beyond X, not at D.
- *Pattern failure:* a decisive daily close below X (₹2,750) invalidates the Bat. Exit immediately — do not hope. A failed harmonic often accelerates in the breakdown direction (the trapped counter-trend longs fuel the move), so a broken bullish Bat can even flip into a short setup on the retest of X from below.

## Confluence

A harmonic pattern is already Fibonacci confluence in structured form, but the highest-probability trades layer independent, non-harmonic evidence at the PRZ:

**Structure.** The best PRZs land on a prior support/resistance shelf, a gap fill, or a prior breakout level. If the ₹2,780–2,800 PRZ overlaps an old Reliance demand zone, the pattern's reliability jumps.

**Moving averages.** A rising 200-day average sitting inside the PRZ adds trend-following buy orders to the reversal — turning a counter-trend bounce into a with-the-higher-trend dip-buy.

**Momentum divergence.** Because the CD leg is a final exhaustion push, it very often prints a **bullish RSI/MACD divergence** at D — price makes a lower low into the PRZ while the oscillator makes a higher low. This is one of the single most powerful harmonic confirmations; a valid Bat *plus* divergence at D is an A-grade reversal.

**Option-chain / OI — the India edge.** For an F&O stock like Reliance, read the PRZ through the option chain. Heavy **put OI at the ₹2,800 strike** with writers *adding* OI as price falls into the PRZ signals a defended floor coinciding with D — strong support for the reversal thesis. A rising PCR and Max Pain near ₹2,850 for the expiry reinforce a bounce. Conversely, put writers *unwinding* at ₹2,800 as price approaches warns the floor is being pulled and even a textbook Bat may fail. On index harmonics (Nifty/Bank Nifty), the same OI read applies to the PRZ strike band.

**Candlestick confirmation.** A hammer, bullish engulfing, or piercing pattern *inside* the PRZ is the trigger that converts geometry into a trade. Geometry says *where*; the candle says *now*.

**The discipline:** require at least one strong independent confluence — divergence, a defended OI floor, or overlapping structure — beyond the raw pattern before taking full size. A valid Bat with divergence at D, on an old demand shelf, defended by put OI, is about as good as a counter-trend reversal gets. A lone pattern on a clean trend with no other evidence is a small, confirmation-only trade at best.

## Pitfalls & false signals

**Forcing the ratios.** The commonest failure is bending tolerance to make a pattern "count" — calling a 72% B-retrace a Gartley, or a PRZ that doesn't actually cluster. If the ratios don't fall within ±2–3% of spec, it is not the pattern. Objective measurement is the entire defence against seeing shapes that aren't there.

**Counter-trend danger.** Harmonics fade the prevailing short-term move by design. In a powerful trend, the CD leg can blow straight through the PRZ and X without pausing — the pattern simply fails and price keeps trending. Never take a harmonic against a violent momentum leg without strong confirmation, and respect the X-stop absolutely.

**The PRZ is a zone, not a price.** Traders who buy the exact 88.6% tick and stop just below D get flushed by routine overshoots. Enter with confirmation or scale across the band, and always keep the stop beyond X — not inside the PRZ.

**Confirmation bias and hindsight.** On a completed chart it's easy to find the one Bat that nailed a low and ignore the many that failed. Judge harmonics only forward, with a pre-committed entry, stop, and target. Backtest or forward-test your own execution before trusting the pattern with size.

**Over-reliance on the pattern alone.** The geometry locates a *candidate* reversal; it does not confirm one. Pros never trade a naked harmonic — they demand divergence, structure, OI support, or a reversal candle. Skipping confirmation to "get a better entry at D" is how the pattern's modest win-rate becomes a losing strategy.

**Timeframe and liquidity.** Harmonics on very low timeframes or illiquid names are noisy and unreliable — the ratios form by chance and reactions are thin. Favour daily/weekly (or clean intraday on liquid index/large-caps) structures where the order-clustering that gives the PRZ meaning actually exists.

How pros filter it: strict ratio tolerance, the stop always beyond X, confirmation candle or divergence required at D, non-harmonic confluence for full size, and full acceptance that these are lower-base-rate counter-trend trades whose edge lives entirely in the tight stop and the 2:1-plus payoff — plus the discipline to exit instantly, and even reverse, when X breaks.

## Interview-ready summary

"Harmonic patterns are five-point (X-A-B-C-D) reversal structures defined by exact Fibonacci ratios between the legs. The Gartley and the Bat differ mainly at two points: the B-retracement of XA and the depth of D. A Gartley has a moderate 61.8% B and completes at 78.6% of XA; a Bat has a shallow 38.2–50% B and completes deeper, at 88.6% of XA — very close to the origin X. That deep Bat completion is why I like it: the D-point sits just above X, so my stop just below X is extremely tight, giving a superior reward-to-risk. The D-zone is a Potential Reversal Zone where an XA retracement, a BC extension, and an AB=CD projection all converge — essentially structured Fibonacci confluence. I never buy the raw touch; I wait for a reversal candle or bullish divergence inside the PRZ, and in Indian F&O names I want put OI defending the PRZ strike. My stop is always just beyond X — a close below X invalidates the pattern and I exit, because failed harmonics often accelerate the other way. The honest caveat is that these are counter-trend trades with a modest win-rate; the edge is not magic geometry but a tightly defined entry and stop that produce a large payoff on a small risk when the pattern works, which is why I always demand confirmation and 2:1-or-better reward before committing."
