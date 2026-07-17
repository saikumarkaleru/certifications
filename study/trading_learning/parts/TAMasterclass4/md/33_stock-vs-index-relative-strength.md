# Stock-vs-Index Relative Strength

## What it is and the logic

Relative strength (RS) — in the technical sense, not the RSI oscillator — is the simplest, most under-used edge in Indian equity trading. It asks one blunt question: **is this stock outperforming or underperforming the market it belongs to?** Not "is it going up" — plenty of stocks go up in a bull tape and are still laggards. The question is whether a rupee parked in the stock grew faster than the same rupee parked in the index over the same window.

The logic is that money is a flow, not a stock. On any given day there is a finite pool of institutional capital — DIIs, FIIs, prop desks, mutual-fund SIP inflows — chasing returns. That capital does not spread itself evenly. It hunts. It rotates into the names showing the best momentum-adjusted risk and starves the rest. Relative strength is the fingerprint of that hunt. When RIL is beating Nifty week after week, you are literally watching capital choose RIL over the average. When a stock leads its own sector index and the sector leads the broad index, you have a **three-tier confirmation** that is very hard to fake, because it requires sustained buying, not a one-day pop.

Why does this matter more in India than in some Western markets? Because our market is **narrow at the top and treacherous below**. Nifty 50 is heavily weighted to a handful of names — HDFC Bank, ICICI Bank, RIL, Infosys, TCS, Bharti Airtel, L&T. The headline index can be green while 30 of the 50 constituents are red, dragged up by two heavyweight banks. If you buy "the market is up so I'll buy any stock," you routinely buy a laggard that bleeds while the index climbs. RS is the filter that stops you doing that. It forces you to buy strength and sell weakness — the whole point of trend trading — rather than buying "cheap" (a value habit that gets traders killed in downtrends).

The honest caveat up front: RS is a **relative** tool. A strong stock in a falling market can still lose you money — it just loses less than the index. "Best house in a bad neighbourhood" still gets flooded when the river bursts. So RS tells you *what* to buy and *what* to short; it does not by itself tell you *whether* to be long or in cash. That second decision comes from the index's own trend and from breadth. Use RS for selection, not for market timing, and it will not betray you.

## Construction and reading

There are three practical ways to build RS on Indian charts. All three are available on TradingView and Chartink; pick by taste.

**1. The RS ratio line (the purest).** Plot `Stock ÷ Index` as its own chart. On TradingView type the symbol as a ratio: `TATAMOTORS/NIFTY` or `HDFCBANK/CNXBANK` (stock over its sector) or `CNXIT/NIFTY` (sector over broad). The resulting line is the relative-strength line. Its *direction* is everything:

| RS line behaviour | Meaning |
|---|---|
| Rising | Stock is outperforming the benchmark — a leader |
| Falling | Stock is underperforming — a laggard |
| Flat | Moving in line with benchmark — market performer |
| New high in RS line while stock price is still below its price high | Emerging leadership; often precedes a price breakout |
| RS line makes lower high while price makes higher high | Relative divergence — leadership fading even as price rises |

The critical discipline: **read the RS line's own trend and structure, exactly as you'd read a price chart.** Draw trendlines on it. Mark its higher-highs / higher-lows. An RS line breaking to a new 52-week high is one of the most reliable "institutions are accumulating this" signals available to a retail screen.

**2. Mansfield Relative Strength.** A normalised version that oscillates around a zero line, so you can compare across stocks. The formula:

```
RS_raw = Close(stock) / Close(index)
Mansfield RS = ((RS_raw / SMA(RS_raw, 52)) - 1) × 100
```

Above zero = outperforming its own 52-week average relationship; below zero = underperforming. The zero-line cross is a clean, mechanical rotation signal. Weekly timeframe is standard (52 weeks ≈ one year).

**3. Rate-of-change spread (RRG-style).** Compute the stock's N-period return minus the index's N-period return:

```
RS_momentum = ROC(stock, N) − ROC(index, N)
```

Positive means the stock outgained the index over the last N bars. This is the engine behind Relative Rotation Graphs (RRG), which plot two axes — RS-Ratio (leadership level) and RS-Momentum (whether leadership is improving or decaying) — and place each stock or sector in one of four quadrants:

| Quadrant | RS-Ratio | RS-Momentum | Interpretation |
|---|---|---|---|
| Leading | High | High | Established leaders, still improving — hold longs |
| Weakening | High | Low | Leaders losing steam — trim / tighten |
| Lagging | Low | Low | Weak and getting weaker — avoid / short |
| Improving | Low | High | Turnaround candidates — watchlist for entry |

The natural clockwise rotation Improving → Leading → Weakening → Lagging → Improving is the sector-rotation cycle. RRGs for NSE sectoral indices vs Nifty are available on some Indian platforms and are worth a weekly glance even if you trade single stocks.

## Worked India example

Take a realistic 2025 rotation. Assume Nifty is grinding up in a broad uptrend, roughly +6% over three months. Under the hood two names diverge sharply.

**Trent Ltd (retail).** Over the same three months Trent rallies +22%. Plot `TRENT/NIFTY`: the RS line is in a clean rising channel, making a fresh all-time high two weeks *before* Trent's price itself clears its prior swing high near, say, ₹6,800. That RS-first breakout is the tell. When price finally clears ₹6,800 on above-average volume, you already knew from the RS line that this was the strongest hand in the index. Overlay `TRENT/CNXCONSUMER` (stock vs its own consumption sector) and it too is rising — so Trent is not just riding a hot sector, it's the *leader within* a hot sector. Three-tier alignment: Trent > Consumption index > Nifty. This is the textbook long: buy the price breakout, stop below the breakout base, and the RS line tells you to *hold through noise* as long as it keeps rising.

**A laggard PSU, say a mid-tier oil marketing name.** Price is *up* +3% over the quarter — a naive trader calls it "going up, looks fine." But `SYMBOL/NIFTY` is a steadily falling line: the stock gained 3% while the index gained 6%, so a rupee here underperformed by roughly 300 bps. The RS line has been in a downtrend for the whole quarter. This is the trap RS saves you from: the stock is green on your screen and red relative to the market. In a pullback it will fall *harder* than the index, because it has no relative-strength cushion and the marginal buyer is elsewhere. If you must be short something as an index hedge, laggards like this are your candidates, not the leaders.

Now watch the rotation flip. Suppose two months later Trent's `TRENT/NIFTY` line rolls over — it makes a lower high while price grinds one more high (relative divergence). On the RRG it slides from Leading into Weakening. Simultaneously the PSU's RS line bottoms and turns up, crossing into Improving. That is your cue: leadership is rotating. Trim Trent into strength, put the improving name on the watchlist, and wait for *its* price to confirm with a breakout before committing. RS gave you a two-to-three-week head start on both the exit and the next entry.

## How to use it for bias and timing

RS is a **selection and conviction** engine layered on top of your normal setup. A disciplined workflow for an Indian swing trader:

**Step 1 — Top-down screen (weekly).** Rank all 11–12 NSE sectoral indices by their RS vs Nifty (Mansfield or 13-week ROC spread). Note the top three (your hunting ground) and bottom three (your short/avoid list). On Chartink you can run a scan for "close/1-year-ago-close > nifty's same ratio" to surface relative leaders mechanically.

**Step 2 — Drill into leaders.** Within the top sectors, rank constituent stocks by RS vs *both* Nifty and the sector index. You want names that beat both. A stock beating Nifty but lagging its own sector is a weak hand in a strong group — pass.

**Step 3 — Time the entry with price, not RS.** RS tells you *which* stock; your usual price setup (breakout from a base, pullback to a rising 20-EMA, VWAP reclaim) tells you *when*. Never enter purely because the RS line is rising — RS lines can rise for months while price consolidates; you'd be dead money. Wait for the price trigger in an RS-confirmed name.

**Step 4 — Manage with RS.** While in the trade, the RS line is your "am I still right?" gauge. As long as it keeps making higher highs, hold through price noise and trail your stop. When the RS line breaks its own uptrend or diverges (price high, RS lower high), that's an early warning to tighten stops or scale out — often *before* price itself breaks.

**For directional bias**, combine RS with the index's own trend: only take RS-leader longs when Nifty is above its 20/50-day averages and breadth is healthy; only press laggard shorts when Nifty is under its averages. RS refines *what*; the index and breadth decide *whether*.

## Pitfalls

**Confusing "up" with "outperforming."** The single most common error. A stock at a 52-week high that is *lagging* the index (RS line falling) is a distribution candidate, not a leader. Always read the ratio, not the raw price.

**Falling knives that "look strong" relatively.** In a bear market the "strongest" stock (least-bad RS) still loses money. RS is relative; it does not immunise you against a falling index. Pair RS selection with market-trend and breadth filters, or you'll be long the best boat on the *Titanic*.

**RS line whipsaw in choppy tape.** When both stock and index chop sideways, the ratio whipsaws and generates false leadership/lagging flips. RS is most reliable in *trending* markets. In a range, widen the timeframe (weekly Mansfield) and demand bigger, cleaner RS moves.

**Illiquidity distortion.** A thin small-cap can post a monster RS reading on one gap-up that no institution can actually trade. Restrict serious RS work to liquid F&O and large/mid-cap names where the RS line reflects real, tradeable flows. On a ₹30-crore-a-day counter, RS is noise.

**Index choice matters.** Comparing a bank to Nifty is less informative than comparing it to Bank Nifty. Always benchmark a stock against *its own sector* first (does it lead its peers?) and the broad index second (does the sector lead the market?). Wrong benchmark, wrong conclusion.

**Corporate-action gaps.** Splits, bonuses, and demergers create artificial jumps in the raw ratio. Use adjusted data (TradingView adjusts by default) and be suspicious of an RS spike that coincides with an ex-date.

**Recency bias in ranking.** A 4-week RS ranking is jumpy and news-driven; a 52-week ranking is stable but slow. Use two windows — a slow one for the strategic sector map, a faster one for timing rotation — and don't over-trade every wiggle in the fast one.

## Interview-ready summary

Relative strength measures whether a stock is outperforming its benchmark, computed as the ratio of stock price to index price (or a normalised/ROC version). A **rising RS line means the stock is a leader — capital is choosing it over the average**; a falling line means it's a laggard. The core edge: it forces you to *buy strength and sell weakness* instead of buying cheap, and it filters out the trap of stocks that are "up" but still lagging a strong index. Best practice is three-tier confirmation — **stock leads its sector, sector leads the broad index** — for the highest-conviction longs, and the mirror for shorts. On NSE, benchmark a stock against its own sectoral index first (e.g., a PSU bank vs Bank Nifty) then Bank Nifty vs Nifty. Use RS for *selection and conviction*, price structure for *entry timing*, and always overlay the index trend and breadth for the *whether-to-be-long* decision — because in a falling market even the strongest relative name can still lose money. The RRG framework packages this into four quadrants (Leading, Weakening, Lagging, Improving) that map the sector-rotation cycle and give a two-to-three-week head start on both exits and the next entries. Honest caveat: RS shines in trending markets and whipsaws in ranges, so demand clean, sustained ratio moves and restrict the analysis to liquid names where the line reflects tradeable institutional flow.
