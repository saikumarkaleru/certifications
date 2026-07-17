# High-Low Index & New Highs/Lows

There is a question that cuts straight to the health of any bull market, and price alone cannot answer it: *is the number of stocks making genuinely new highs expanding or shrinking as the index climbs?* When an index prints a fresh all-time high, the honest, healthy version of that event has hundreds of individual stocks also breaking out to new 52-week highs alongside it — broad, durable leadership. The dishonest, fragile version has the index at a new high while the count of new 52-week highs is *falling* — a handful of mega-caps carrying a market whose leadership is quietly narrowing. New Highs/New Lows data, and the High-Low Index built from it, is the cleanest instrument for telling those two situations apart.

Where the McClellan family works off daily advances and declines (one-day moves) and TRIN works off volume, the New Highs/New Lows series works off a **52-week lookback**. That longer memory makes it a *leadership and trend-quality* gauge rather than a short-term momentum gauge. A stock at a new 52-week high is, by definition, in a confirmed uptrend that has overcome a full year of overhead supply. Counting how many stocks are in that state — versus how many are at new 52-week lows — is one of the most powerful reads on the market's underlying condition.

## What it is and the logic

Each day the exchange (or your screener) produces two counts for your universe: **New Highs (NH)** — stocks closing at a new 52-week high — and **New Lows (NL)** — stocks closing at a new 52-week low. On a strong, broadening advance, NH runs into the hundreds while NL is a trickle. In a deteriorating market the two counts converge and then cross, with NL overtaking NH — a serious warning.

From these two raw counts we build three progressively refined tools:

1. **Net New Highs = NH − NL.** The raw daily balance. Persistently positive = healthy uptrend leadership; persistently negative = downtrend; a cross from positive to negative is a regime warning.

2. **High-Low Ratio (Record High Percent) = NH / (NH + NL) × 100.** This normalises the balance to a 0–100 scale. Above 50 means new highs dominate; below 50 means new lows dominate. At exactly 50, highs and lows are balanced — a market at an inflection.

3. **High-Low Index = a 10-day simple moving average of the Record High Percent.** Smoothing the daily ratio removes noise and produces an oscillator that swings between 0 and 100, ideal for spotting overbought/oversold leadership and, crucially, *divergences* against the index.

The core logic is leadership breadth. A rising index needs an expanding cavalry of new-high stocks behind it. When that cavalry thins — index up, new-high count down — you have a **leadership divergence**, and leadership divergences precede most significant tops. Symmetrically, at bottoms, a surge in new lows that then *contracts* while the index makes a marginal new low signals selling exhaustion.

## Construction: formulas and reading

| Tool | Formula | What it shows |
|---|---|---|
| Net New Highs | NH − NL | Raw leadership balance |
| Record High Percent (RHP) | NH / (NH + NL) × 100 | Normalised 0–100 leadership |
| High-Low Index (HLI) | 10-day SMA of RHP | Smoothed leadership oscillator |

**Worked calculation.** On the NSE broad universe today, 180 stocks make new 52-week highs and 20 make new 52-week lows.

- Net New Highs = 180 − 20 = **+160** (strongly positive, healthy)
- RHP = 180 / (180 + 20) × 100 = 180/200 × 100 = **90** (new highs overwhelmingly dominate)

Average today's RHP with the prior nine days' RHP values to get the High-Low Index. If the HLI is sitting at 85, leadership is broad and bullish but stretched.

Now a deteriorating day: 40 new highs, 160 new lows.

- Net New Highs = 40 − 160 = **−120**
- RHP = 40 / 200 × 100 = **20** — new lows dominate, distribution/downtrend leadership.

### Reading levels for the High-Low Index

| HLI (10-day SMA of RHP) | Condition | Bias |
|---|---|---|
| Above 90 | Extreme bullish leadership, overbought | Strong but stretched |
| 70 – 90 | Healthy bull, broad leadership | Bullish |
| 30 – 70 | Mixed / transitional | Neutral |
| 10 – 30 | Weak, new lows dominating | Bearish |
| Below 10 | Washout / capitulation leadership | Oversold; bottom watch |
| Crossing above 50 | Leadership turning bullish | Buy signal region |
| Crossing below 50 | Leadership turning bearish | Sell signal region |

The 50 line is the pivot — above it, highs lead; below it, lows lead. Crossings of 50, especially by the smoothed HLI, are meaningful regime markers.

## Worked India example

Return to the intermediate-top scenario, but now watch it through the leadership lens. Nifty grinds from 24,400 to a record 25,500 over two months — a strong-looking 4.5% advance. The headlines celebrate the record. Beneath the surface, track the daily new-high count on the Nifty 500:

| Phase | Nifty | Daily New Highs | RHP | HLI (10-day) |
|---|---|---|---|---|
| Early advance | 24,400 → 24,900 | 140–170 | ~85 | 82 |
| Mid advance | 24,900 → 25,300 | 90–110 | ~72 | 74 |
| Final push | 25,300 → 25,500 (record) | 45–60 | ~58 | 61 |

Read the last row against the first. Nifty is at its *highest* level ever — 25,500 — yet the new-high count has collapsed from 140–170 down to 45–60, and the High-Low Index has slid from 82 to 61. **The index made a new high; the leadership breadth made a series of lower highs.** This is a textbook bearish leadership divergence. Fewer and fewer individual stocks are participating in each new index high — the advance is narrowing onto a shrinking group of heavyweights (in India, typically the banking and IT giants that dominate Nifty's weight).

This is precisely the "index green, my portfolio red" experience retail traders complain about at tops — because the *average* stock stopped making new highs weeks before the index did. The mid- and small-cap universe, in fact, may already be rolling over while Nifty prints records.

The trade logic mirrors the McClellan approach: the divergence is a *warning*, not a trigger. You stop initiating new longs, tighten stops, and set a confirmation trigger. The trigger fires when (a) the daily new-*low* count starts expanding and overtakes new highs — RHP drops below 50 — and (b) Nifty breaks its most recent swing low. When RHP crosses below 50 while Nifty cracks 25,100, the leadership regime has flipped and price has confirmed; that is the signal to exit longs and/or initiate hedges. In the historical pattern, Nifty then gives back the narrow final leg — sliding toward 24,300 — as the deferred weakness in the broad market finally drags the heavyweights down too.

The bottom mirror: in a decline, the daily new-low count explodes to 300+ as everything sells off. Then Nifty grinds to a *marginal* new low, but the new-low count comes in far *lower* — say 120 instead of 300. Fewer stocks are making new lows even as the index makes a new low: selling is exhausting, the weakest hands are out. The High-Low Index, having plunged below 10, hooks up and reclaims the 50 line. Combined with a price reversal, that contraction-of-new-lows plus HLI recovery is a high-quality intermediate bottom signal on the NSE.

## How to use it for bias and timing

1. **Gauge trend health continuously.** In an uptrend, you *want* to see the new-high count expanding or at least holding as the index rises. As long as new highs stay broad and the HLI holds above 50–70, the bull is healthy — buy dips with confidence. The day the new-high count starts shrinking against a rising index, downgrade the trend's quality.

2. **Trade the 50-line crossings of the HLI.** The smoothed High-Low Index crossing above 50 from below is a leadership-turning-bullish signal (confirm with price); crossing below 50 is leadership-turning-bearish. These are cleaner than raw daily prints.

3. **Hunt leadership divergences at index extremes.** Index new high + falling new-high count = bearish divergence, top watch. Index new low + contracting new-low count = bullish divergence, bottom watch. Always require price confirmation before acting.

4. **Watch the NH/NL crossover.** When new lows overtake new highs (RHP through 50 to the downside) after a long uptrend, treat it as a serious regime warning — leadership has flipped from expansion to contraction.

5. **Segment the universe.** Run the count separately on large-caps (Nifty 100) and on the broad market (Nifty 500 or full NSE). Divergence *between* them — large-cap new highs healthy while broad-market new highs collapse — is itself the classic late-cycle narrowing signal, and it tells you the small/mid-cap unwind has begun even while the index looks fine.

## Pitfalls

**The 52-week lookback creates edge effects.** Around anniversaries of major market events — one year after a crash low or a blow-off high — the new-high and new-low counts can jump or drop mechanically as extreme prior-year prices roll out of the 52-week window. A sudden surge in new highs exactly 52 weeks after a major bottom is partly a calendar artefact; read it in context.

**Newly-listed stocks and IPOs distort new-high counts.** A freshly-listed stock trading above its issue price technically registers as being at or near a "new high" with little trading history. In an active IPO market — and India has had waves of them — this can inflate the new-high count artificially. Use a universe that filters for adequate listing history, or lean on the smoothed index.

**It is a slower, leadership tool — not a day-trader's trigger.** Because of the 52-week base, this series moves more slowly than daily advance/decline breadth. It is superb for gauging trend quality and spotting multi-week divergences; it is poor for timing an intraday entry.

**Divergences can persist for weeks.** As with all breadth divergences, a narrowing new-high count can precede the actual top by a long time. Strong bulls narrow their leadership *and keep rising* for a surprisingly long stretch. The divergence lowers your conviction and tightens your risk; the price-confirmation trigger is what times the exit.

**Universe consistency, again.** New-high/new-low counts must come from one stable universe every day. Full NSE, Nifty 500, and Nifty 50 will give very different absolute counts; comparing across universes corrupts the read. Fix your universe and learn its normal ranges.

**A cluster of new lows in a strong tape is a red flag, not noise.** Even when the index is healthy, a *rising* new-low count (stocks quietly breaking down beneath a calm surface) is early evidence of internal rot. Do not dismiss expanding new lows just because the index is green.

## Interview-ready summary

The New Highs/New Lows series counts, each day, how many stocks close at a new 52-week high versus a new 52-week low, giving a read on *leadership breadth* — the quality and durability of a trend rather than short-term momentum. Net New Highs (NH − NL) is the raw balance; Record High Percent, NH/(NH+NL)×100, normalises it to 0–100 with 50 as the pivot; and the High-Low Index, a 10-day SMA of the Record High Percent, is the smoothed oscillator used in practice — above 70 healthy bull, below 30 bearish, crossings of 50 marking regime shifts. Its signature signal is the leadership divergence: when an index (Nifty) prints a new high while the new-high count shrinks — the "index green, portfolio red" top — the advance is narrowing onto a few heavyweights and is fragile. The mirror at bottoms is a contraction in new lows even as the index makes a marginal new low, signalling selling exhaustion. Because of the 52-week lookback, beware anniversary edge effects and IPO-inflated new-high counts, keep the universe consistent, and treat it as a slower leadership/trend-quality gauge — divergences warn and lower conviction, but you time actual entries and exits with a price-confirmation trigger such as the Record High Percent crossing 50 while price breaks a swing level. Splitting the count between large-caps and the broad market exposes late-cycle narrowing before the index shows any weakness.
