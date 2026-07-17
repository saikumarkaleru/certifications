# Other DeMark Indicators (TD Lines, REI, Pressure)

TD Sequential and TD Combo get the headlines, but Tom DeMark built an entire ecosystem of objective indicators, and several of them are genuinely more useful for **day-to-day trading** than the famous 13s. Where Sequential is a slow exhaustion timer, this chapter's tools are about **trendlines drawn without discretion**, **oscillators built to avoid the flaws of RSI**, and **intrabar pressure and reference levels** you can act on every session. The unifying DeMark philosophy runs through all of them: *remove the trader's eye, define everything mechanically, and anchor to the most recent, most relevant price pivots rather than to arbitrary lookbacks.* This chapter covers TD Lines (with TD Points and price projectors), the TD Range Expansion Index (REI), and the TD Pressure / accumulation-distribution family, plus a note on the everyday workhorses — TD Points, TD Demarker, and the reference levels most Indian traders actually put on their charts.

## The unifying idea — objective, backward-anchored analysis

Conventional technical analysis is riddled with subjectivity: two analysts draw two different trendlines on the same chart. DeMark's obsession was **reproducibility**. Every one of his tools starts from a mechanically defined pivot — a **TD Point** — and builds outward with fixed rules, so that any two people applying the method get the *same* line, the *same* oscillator, the *same* projection. That is the through-line connecting TD Lines, REI, and Pressure.

### TD Points — the atomic pivot

A **TD Point** is DeMark's objective swing pivot:

| Pivot | Definition |
|---|---|
| **TD Point High** | A bar whose high is greater than the high of the bar immediately before **and** after it |
| **TD Point Low** | A bar whose low is less than the low of the bar immediately before **and** after it |

DeMark also defined higher-magnitude points (a "level 2" TD Point compares against two bars either side, and so on) so you can filter for more significant pivots. Everything else is built on these. Crucially, TD Points are identified **objectively** — no "does this look like a swing high to you?" ambiguity.

## TD Lines — trendlines without discretion

### What they are and the logic

A **TD Line** is a trendline drawn using the **two most recent** qualifying TD Points, moving **backward from the most recent** pivot. This is the opposite of conventional trendline drawing, where analysts anchor to the *oldest, most obvious* pivots and connect forward. DeMark's insight: the market cares about the *most recent* supply/demand pivots, not ancient ones, and anchoring to the latest points makes the line **dynamic** — it redraws itself as new TD Points form, always reflecting current structure.

- **TD Demand Line** (support) connects the two most recent TD Point *lows*, sloping up when the more recent low is higher.
- **TD Supply Line** (resistance) connects the two most recent TD Point *highs*, sloping down when the more recent high is lower.

Because you use the two most recent points, the line's slope updates automatically; there is exactly one demand line and one supply line at any time, and they are the same for everyone applying the rules.

### Construction, qualifiers and price projectors

A **breakout** of a TD Line is only tradeable if it **qualifies** — DeMark added qualifiers precisely to filter the false breaks that plague ordinary trendline trading. For a downside break of a TD Demand Line, DeMark's three qualifiers (any one can validate, but the classic is #1) are:

| Qualifier | Condition (downside break of demand line) |
|---|---|
| **Q1** | The close on the bar *before* the breakout is **down** (close < prior close), suggesting genuine supply rather than a gap that gets bought |
| **Q2** | The breakout bar **gaps/opens below** the line by more than the previous bar's net price move |
| **Q3** | The close two bars earlier plus the difference to the current close indicates real momentum, filtering exhausted moves |

The most-used is Q1: a qualified break requires that the market was already weak going into the break, filtering the "poke through and reverse" fakeout.

**TD Line price projector.** When a TD Line breaks and qualifies, DeMark projects a target objectively. For a broken TD Demand Line: take the **largest distance** between the line and the *lowest low* (or a specific intervening low) beneath it during the line's life, and subtract that distance from the breakout point. This gives a mechanical measured-move target rather than an eyeballed one. Supply-line breaks project symmetrically upward.

### Worked India example — Nifty 50 daily TD Demand Line

Suppose two recent TD Point lows on the Nifty daily sit at **22,050** (older) and **22,240** (more recent) — an upward-sloping TD Demand Line. Projected forward, the line sits at about **22,380** on the current bar. Nifty has been drifting and now a bar closes at **22,300**, *below* the line.

- **Qualifier check (Q1):** was the prior bar's close down? Say yesterday closed at 22,410 vs. the day before at 22,470 — yes, down. **Qualified break.**
- **Projector:** during the line's life the deepest distance from the line to an intervening low was ~180 points. Subtract from the ~22,380 break level → target **≈ 22,200**, with a stretch to the older pivot at 22,050.

**How to trade it.** Short (or buy a bear put spread) on the qualified close below the line at 22,300; stop back above the most recent TD Point high or a true-range increment above the line (say 22,470); first target the 22,200 projector, then 22,050. Reverse the entire logic for a qualified **upside** break of a TD Supply Line — a clean, objective breakout entry that most traders draw by feel.

### Pitfalls of TD Lines

- **Redrawing whiplash.** Because the line uses the two most recent points, a new TD Point can suddenly re-slope the line; you must re-evaluate each time a fresh pivot forms.
- **Skipping the qualifier.** An *unqualified* break is exactly the fakeout DeMark designed the qualifiers to avoid — never trade a bare line touch.
- **Level selection.** Higher-magnitude TD Points give more significant, slower lines; using level-1 points on a noisy 5-min chart produces constant, low-value signals.

## TD Range Expansion Index (REI) — a better-behaved oscillator

### What it is and the logic

The **TD Range Expansion Index** is DeMark's momentum oscillator, engineered to fix two flaws he saw in RSI and stochastics: (1) they can stay pinned at extremes for long stretches, giving premature signals, and (2) they treat all overbought/oversold readings alike regardless of whether price is actually in a *mild* pullback (which reverts) or an *outright* trend (which doesn't). REI oscillates roughly between **+100 and −100**, with **overbought above +40** (some use +45/+60) and **oversold below −40**.

### Construction

REI, over a lookback (default **5 bars**), sums a **conditioned** measure of range expansion. Simplified, for each of the last 5 bars it computes:

1. The sum of two differences: (current high − high 2 bars ago) + (current low − low 2 bars ago).
2. That value is **conditioned to zero** unless a momentum condition holds — specifically, unless the current high ≥ the low 5 or 6 bars ago **or** the current low ≤ the high 5 or 6 bars ago (this filters out bars that are not genuinely expanding relative to recent range).
3. The numerator (sum of conditioned differences over 5 bars) is divided by the sum of the **absolute** high-to-2-bars-ago and low-to-2-bars-ago ranges over the same 5 bars, then ×100.

The conditioning step is the clever bit: it zeroes out contributions from bars that are not truly expanding the range in a directional way, so REI doesn't get "stuck" the way RSI does during quiet drifts.

### TD POQ and using REI

DeMark paired REI with a **duration** concept for signals ("TD POQ" — price oscillator qualifier / duration analysis): an oscillator reading that stays overbought/oversold for **fewer than ~6 bars** signals a *mild* condition likely to reverse; one that stays extreme for **more than 6 bars** signals a genuine trend that will *persist*. This mild-vs-extreme distinction is REI's real edge — it tells you whether to fade the extreme or respect it.

### Worked India example — Reliance daily REI

On Reliance daily, REI drops to **−48** (oversold) after a three-day dip and stays below −40 for only **2 bars** — a *mild* oversold. Per DeMark, mild + short-duration favors a **bounce**. Confluence: the dip lands on a prior TD Demand Line and a round ₹2,900 level. You buy the reversal with a stop under the swing low. Contrast: if REI had sat below −40 for **8 bars**, that persistence would warn the downtrend is real — do *not* buy the dip. Same oscillator value, opposite meaning, decided by duration. That is why REI beats a naive RSI-oversold rule.

### Pitfalls of REI

- **Treating it like RSI.** The overbought/oversold levels and the duration rule are specific to REI; importing RSI habits misuses it.
- **Ignoring duration.** The mild-vs-extreme (POQ) distinction *is* the tool; a bare −40 reading without duration context is half the signal.
- **Default lookback on wrong timeframe.** The 5-bar default is tuned for daily-ish charts; adjust and re-test for intraday Nifty.

## TD Pressure and the accumulation-distribution family

### What it is and the logic

DeMark's **TD Pressure** is a volume-and-price accumulation/distribution measure that answers, "are buyers or sellers in control **within** each bar?" Unlike close-only oscillators, Pressure uses **where the close sits inside the bar's range**, weighted by volume — the same instinct behind classic accumulation/distribution, but with DeMark's specific formulation.

### Construction

For each bar, TD Pressure computes a buying-pressure fraction based on the **close's position within the day's range** — essentially (close − open) or (close − low)/(high − low) type ratios — multiplied by **volume**, then accumulated and normalized over a lookback (commonly ~5 bars) into a bounded oscillator. When price rises but the close keeps landing in the *lower* part of each bar on heavy volume, Pressure diverges bearishly — distribution beneath a rising tape. When price falls but closes keep landing near the *highs* of bars, Pressure diverges bullishly — accumulation beneath a falling tape.

The signal of interest is almost always **divergence**: price makes a new extreme, Pressure does not.

### Worked India example — Bank Nifty distribution

Bank Nifty grinds from 48,900 to 49,400 over four sessions on decent volume, but each daily close lands in the *lower third* of its range and volume is rising — classic distribution. TD Pressure makes a **lower high** while price makes a **higher high**: a bearish divergence. Combine this with a TD Supply Line just overhead at 49,450 and a Sequential/Combo sell Countdown maturing, and you have a stacked short setup: enter on a qualified TD Supply/Demand-line break or a bearish price flip, stop above 49,600, target the prior TD Demand Line near 48,600.

### Related DeMark oscillators — quick reference

| Indicator | What it measures | Everyday use |
|---|---|---|
| **TD DeMarker (DeM)** | A range-based momentum oscillator (0–1), overbought >0.6, oversold <0.4 | Simple, robust momentum/exhaustion read; popular default on MT-style and NSE platforms |
| **TD Pressure** | Volume-weighted intrabar accumulation/distribution | Divergence detection under a trend |
| **TD Rate of Change / Alignment** | Objective momentum & multi-timeframe agreement | Filter: only take signals when timeframes align |
| **TD Reference levels (TD Camo / TD Open/Trap)** | Objective intraday reference and "trap" levels off the open | Intraday Nifty/Bank Nifty bias and fade levels |

## How these tools combine — a DeMark confluence stack

The DeMark ecosystem is designed to be **layered**, and this is how professionals actually use it on Indian markets:

1. **Structure — TD Lines:** define the objective, current supply/demand trendlines and their qualified break levels and projectors.
2. **Momentum — REI / DeMarker:** confirm whether the move is a mild (fade) or extreme (respect) condition via the duration rule.
3. **Order flow — TD Pressure:** check for accumulation/distribution divergence beneath the trend.
4. **Exhaustion — Sequential / Combo (Ch. 15–16):** time the turn with the 9s and 13s.
5. **Reference — TD Points & intraday levels:** anchor stops and targets to objective pivots.

A Nifty short that has a qualified TD Supply-line break, an *extreme-but-rolling* REI, a bearish TD Pressure divergence, and a maturing sell 13 — all anchored to recent TD Points — is a textbook stacked DeMark signal. No single tool is a system; the **agreement** is.

## Honest limitations

- **Objectivity is not accuracy.** DeMark's tools are reproducible, which is valuable, but reproducible is not the same as *profitable*. Qualified TD-Line breaks still fail; REI and Pressure divergences can persist for a long time in strong trends.
- **Parameter and platform variance.** REI lookbacks, TD Point magnitudes, TD-Line qualifier settings, and Pressure formulas differ across TradingView scripts, GoCharting, Bloomberg (which licensed the official versions), and free NSE tools. The "official" DeMark Studies (Bloomberg/Symbolik) differ from community re-implementations — verify what you're running.
- **Counter-trend bias.** Like the 13s, much of this toolkit is about fading or catching turns, which is inherently lower-hit-rate than trend-following. Respect regime.
- **Cost and timeframe.** On Indian markets, STT/brokerage/GST make low-timeframe DeMark signals unprofitable; these tools earn their keep on swing timeframes where moves dwarf costs.
- **Over-fitting the qualifiers.** The many qualifier variants invite curve-fitting. Pick a standard configuration, test it honestly, and resist optimizing per chart.

## Interview-ready summary

Beyond Sequential and Combo, Tom DeMark built a full ecosystem of **objective** indicators anchored on **TD Points** — mechanically defined swing pivots. **TD Lines** draw the supply and demand trendlines from the *two most recent* TD Points (backward-anchored, self-updating), and their breaks are traded only when **qualified** (e.g., prior bar down, or a large gap) with an objective **price projector** for the target. The **TD Range Expansion Index (REI)** is a −100/+100 momentum oscillator whose conditioning step stops it getting "stuck" like RSI, and whose **duration rule (POQ)** distinguishes *mild* extremes (fade) from *persistent* ones (respect). **TD Pressure** is a volume-weighted intrabar accumulation/distribution oscillator used mainly for divergence — distribution beneath a rising tape, accumulation beneath a falling one. Alongside sit **TD DeMarker**, rate-of-change/alignment, and objective intraday reference levels. The whole toolkit is meant to be **layered** — structure (TD Lines) + momentum (REI) + order flow (Pressure) + exhaustion (Sequential/Combo) + reference (TD Points) — with the *agreement* of tools, not any single one, forming the signal. Its virtue is reproducibility; its limits are that objective is not the same as profitable, platform implementations vary, much of it is counter-trend, and it only pays on swing timeframes after Indian transaction costs.
