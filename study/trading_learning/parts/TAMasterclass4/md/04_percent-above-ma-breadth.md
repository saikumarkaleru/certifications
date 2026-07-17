# Percent-Above-Moving-Average Breadth

## What it is and the logic

Price tells you what the index did. Breadth tells you *how many soldiers were marching* when it did it. The Percent-Above-Moving-Average family of breadth indicators answers one blunt question at each close: of all the stocks in a defined universe, what fraction are trading above a chosen moving average — the 50-day, the 200-day, the 20-day? The number is a percentage between 0 and 100. On the Nifty 50 it is the count of constituents above their MA divided by 50. On a broader Nifty 500 or the full NSE universe of roughly 1,900 traded names, it is that count divided by the total.

The logic is that a headline index is a capitalization-weighted average. Reliance, HDFC Bank, ICICI Bank, Infosys and a handful of heavyweights carry a disproportionate load. On any given day the Nifty can close green while 60% of its members close red, because four large caps did the lifting. Percent-above-MA strips out the weighting entirely — every stock is one vote, one soldier. It is a *democratic* reading of the market against the *plutocratic* reading of the index. When the two disagree, the disagreement is the signal.

Three uses flow from this. First, **participation confirmation**: a rally where the percent-above-50DMA is climbing toward 80% is broad and healthy; a rally where the index makes a new high but percent-above-50DMA has slipped from 85% to 55% is a rally narrowing onto fewer shoulders — a classic pre-top divergence. Second, **washout / exhaustion timing**: when the percent-above-200DMA collapses under 10-15%, nearly everything is technically broken, panic is near-universal, and that is historically where durable bottoms form — not because things are good but because selling has run out of fuel. Third, **regime classification**: the level itself defines whether you are in a bull regime (indicator persistently 60-90%), a bear regime (persistently 10-40%), or a chop zone (oscillating around 50%).

The percent-above-MA indicator is *mean-reverting at the extremes and trending in the middle*. That dual character is the whole art of reading it.

## Construction and reading

**The formula.** For a universe of N stocks and a moving average of length L:

```
%Above(L) = (Number of stocks with Close > their own L-day SMA) / N × 100
```

Each stock is compared to *its own* moving average, not the index's. You compute L-day simple moving averages for every constituent, count how many closes sit above their line, divide by the universe size, multiply by 100. On TradingView these are pre-built symbols you can pull straight onto a chart. For the S&P 500 the ticker convention is `S5FI` (percent above 50DMA), `S5TH` (above 200DMA), `S5TW` (above 20DMA). India does not have official NSE breadth tickers as clean as the US, so Indian traders build these three ways: (1) TradingView's screener with a saved filter and a manual daily count, (2) Chartink screener scans that return the count directly, or (3) a broker/data-feed script over the Nifty 500 constituent list.

**The three horizons and what each is for:**

| MA length | Character | Primary use |
|---|---|---|
| 20-day | Fast, noisy, mean-reverts in days | Short-swing timing, overbought/oversold |
| 50-day | The workhorse; the "trend" gauge | Intermediate participation, divergences |
| 200-day | Slow, regime-defining | Bull/bear regime, major washouts/tops |

**Reading the levels.** Calibrate thresholds to the horizon:

| %Above 50DMA | Interpretation |
|---|---|
| > 80% | Strong broad uptrend; often overbought — chase carefully |
| 60–80% | Healthy bull participation |
| 40–60% | Neutral / transition / chop |
| 20–40% | Weak, distribution or downtrend |
| < 20% | Oversold washout; bottom-hunting zone |
| < 10% | Capitulation; historically near major lows |

The 200DMA version runs a bit different because the 200-day line is slower and stocks spend more time on one side of it. In a mature bull market percent-above-200DMA can sit pinned at 70-90% for months. When it *breaks below 50% for the first time in a while* after a long run, that is a regime-warning worth respecting.

**Two reading modes.** (1) *Level* — where is the number now, in which band. (2) *Direction and divergence* — is it rising or falling, and does its path agree with the index. The second is more powerful. Overlay percent-above-50DMA in a lower pane under the Nifty. When Nifty prints a higher high but the breadth line prints a lower high, you have a bearish breadth divergence: the new index high was built on fewer participants. The reverse — Nifty lower low, breadth higher low — is a bullish divergence, the market internally healing while the headline still bleeds.

**Smoothing.** The raw daily line whipsaws. Many desks apply a 5-day or 10-day EMA to the breadth series itself to see the signal through the noise, especially on the 20DMA version.

## Worked India example

Take a composite, realistic sequence on the Nifty 500 through a typical Indian market cycle — the kind of tape Indian swing traders lived through repeatedly in 2022-2025.

**Phase 1 — the broad bull (say, Nifty around 22,000 rising to 24,000).** Percent-above-50DMA sits in the 72-84% band for weeks. Percent-above-200DMA holds 78%. Every dip in the Nifty of 2-3% is met by the breadth line bouncing off ~60% and re-expanding. Reading: this is a *buy-the-dip* regime. Broad participation means sector rotation is doing the work — when IT cools, PSU banks and capital-goods pick up, and the aggregate stays high. Your bias: long, aggressive on pullbacks, trailing stops wide.

**Phase 2 — the narrowing top (Nifty grinds 24,000 → 24,850, a new all-time high).** Here is the tell. The Nifty makes a fresh high, but percent-above-50DMA, which had peaked near 84% at the 24,000 print, now reads only 58% at the 24,850 print. Fewer than three-fifths of stocks are above their 50DMA even as the index tops out. The heavyweights — a couple of large private banks and Reliance — are carrying the tape while the mid-cap and small-cap majority has already rolled over. This is a **bearish breadth divergence**. It does not mean *sell everything today*; breadth divergences can persist for weeks. It means *stop adding, tighten stops, reduce leverage, and watch for a price trigger* (a failed breakout, a break of a 10-day swing low). The divergence is the yellow light; price confirmation is the red.

**Phase 3 — the break and slide (Nifty 24,850 → 22,300).** Price finally cracks. Now percent-above-50DMA falls through 40%, then 25%, and percent-above-200DMA — which had been comfortable at 78% — plunges toward 30%. The regime has flipped. In this phase the *level* is your guide, not divergence: you are in a sell-rallies market until the internals stabilize.

**Phase 4 — the washout bottom (Nifty capitulation toward 21,800).** On the final flush, percent-above-50DMA prints 6% and percent-above-200DMA prints 11%. Almost nothing is above any moving average. This is the fear extreme. India VIX is spiking above 20-22, headlines are apocalyptic. But this is precisely the mean-reversion zone. You do not buy the low tick; you wait for the *first thrust* — the breadth line ripping from 6% back through 20% and 40% within a handful of sessions. That expansion, off a washout, is one of the most reliable long signals in the breadth toolkit, and it dovetails with the Zweig-style thrust logic covered in the companion chapter.

**The trade discipline this produced.** A trader who was long in Phase 1, stopped adding and tightened in Phase 2 on the divergence, was flat or short in Phase 3, and re-entered on the Phase 4 thrust captured the cycle without needing to predict a single top or bottom. Breadth did not forecast; it *described the crowd*, and the trader acted on the description.

## How to use it for bias and timing

**Bias (the regime filter).** Run percent-above-200DMA as a slow master switch. Above 60% and rising: bullish regime, favor longs, treat dips as opportunities, let winners run. Below 40% and falling: bearish regime, favor shorts and cash, treat rallies as exits. Between 40-60%: no-man's-land — reduce size, trade lighter, demand cleaner setups. This single filter keeps you on the right side of the crowd far more often than staring at the index alone.

**Timing (the tactical layer).** Use the 20DMA and 50DMA versions for entries within the regime:

- *In a bull regime*, buy when percent-above-20DMA dips into 30-40% (a shallow oversold reset) and turns up. You are buying a pullback in a healthy market — the highest-odds swing entry.
- *In a bear regime*, sell rallies when percent-above-20DMA pushes into 60-70% (an oversold-market bounce that has run its course) and rolls over.
- *At suspected turns*, wait for the divergence at tops and the thrust at bottoms rather than the raw level.

**A concrete checklist to keep on the desk:**

1. What band is %Above 200DMA in? → sets my directional bias.
2. Is %Above 50DMA confirming or diverging from the latest index high/low? → sets my alertness.
3. Is %Above 20DMA at a tactical extreme (below 30% or above 70%)? → sets my entry timing.
4. Does price agree yet? → only act when price confirms the breadth read.

**Position sizing tie-in.** Let the breadth level scale your risk. Full size when %Above 200DMA is above 65% and %Above 50DMA is expanding. Half size in the 40-60% chop zone. Longs off a sub-15% washout thrust can be sized up *because* the risk (a fresh new low from an already-washed-out condition) is statistically limited — but only after the thrust, never into the falling knife.

## Pitfalls

**1. Universe drift and reconstitution.** The Nifty 50, Nifty 500, and sectoral indices are rebalanced periodically. When constituents change, the breadth series has a small discontinuity. Over long histories this matters; for day-to-day reading it is minor, but do not treat a single-day jump around a reconstitution date as a real signal.

**2. Small universes are jumpy.** Computing percent-above-MA on just the Nifty 50 gives a coarse, jerky line — each stock is worth two full percentage points, so five names crossing their MA moves the reading 10 points. Prefer the Nifty 500 or the full NSE universe for a smooth, meaningful series. Reserve the Nifty 50 version for a quick heavyweight-participation check, not for divergence analysis.

**3. Divergences can persist far longer than you can stay solvent.** A bearish breadth divergence is a *warning*, not a *timer*. In strong momentum markets breadth can narrow for months while the index melts up. Never short on the divergence alone. Wait for price to break structure. The graveyard of Indian traders is full of people who shorted the Nifty at 24,000 "because breadth was weak" and got run over to 25,000.

**4. Confusing the horizons.** A 20DMA reading of 25% is *oversold and often a buy in a bull market*; a 200DMA reading of 25% is *a broken market, favor shorts*. Same number, opposite meaning, because the horizon differs. Always know which line you are reading.

**5. Sector concentration masquerading as breadth.** If PSU banks and defence stocks are all ripping together, they can push the count up even though the "breadth" is really one or two themes. Cross-check with a sector-level breadth view — how many *sectors* are participating, not just how many stocks — to avoid mistaking a narrow thematic run for genuine market-wide strength.

**6. Data-source inconsistency.** Because India lacks a single official breadth ticker, two traders using different universes or different SMA conventions (simple vs exponential, close vs adjusted close) get different numbers. Pick one construction and stay with it so your historical thresholds remain comparable.

**7. Mean-reversion is not guaranteed at extremes.** Sub-10% readings *usually* precede bounces, but in a genuine bear market (2008-style) the indicator can grind at single digits for weeks and re-break lower. The washout-thrust rule exists precisely because you wait for the *turn* to confirm, rather than assuming the extreme itself is the bottom.

## Interview-ready summary

Percent-above-moving-average breadth measures the fraction of a stock universe trading above a chosen moving average — 20, 50, or 200-day — giving every stock one equal vote regardless of market cap. It corrects the blind spot of cap-weighted indices like the Nifty, where a few heavyweights can mask a rotting majority. Read it two ways: by *level* (above 80% = broad and strong but overbought; below 15% = washout and bottom-hunting territory) and by *divergence* against the index (new index high on falling breadth = narrowing top; new index low on rising breadth = internal healing). Use the 200DMA version as a slow regime filter for directional bias, the 50DMA version for intermediate participation and divergence, and the 20DMA version for tactical swing entries. The highest-odds signals are the *bearish divergence* at tops (stop adding, tighten stops, wait for price to break) and the *washout thrust* at bottoms (percent-above-50DMA ripping from single digits back through 40%). The cardinal discipline: breadth describes the crowd, it does not time the market — never act on a divergence until price confirms, because narrowing markets can melt up for months. In India, build it over the Nifty 500 or the full NSE universe (not the jumpy Nifty 50) using a consistent SMA convention, and cross-check against sector-level participation so you do not mistake a two-theme thematic run for real market breadth. The one-liner: *price is the average, breadth is the attendance — when the average rises but attendance falls, the party is ending.*
