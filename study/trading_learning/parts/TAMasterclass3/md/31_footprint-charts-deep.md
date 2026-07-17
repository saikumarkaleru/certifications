# Footprint Charts (Deep)

If Cumulative Volume Delta is the *summary* of the auction, the footprint chart is the *transcript*. Where a candlestick collapses an entire bar into four numbers — open, high, low, close — a footprint chart cracks the candle open and shows you, price level by price level, exactly how much volume traded and how it split between aggressive buyers and aggressive sellers. It is the closest a screen-based trader gets to standing on the trading floor and hearing where the paper actually changed hands. This chapter goes deep: the four display modes, how to read absorption and exhaustion inside a single candle, the numbers that matter on Nifty and Bank Nifty futures, and where the whole thing quietly lies to you in the Indian data environment.

## What it is and the logic

A footprint chart (also called a cluster chart, order-flow chart, or numbers-in-candles) takes each price bar and, instead of drawing a body and wicks, draws a *stack of cells*. Each cell is one price level (one tick) within the bar's range. Inside each cell it prints numbers describing the trading that occurred **at that exact price** during that bar:

- how much aggressive selling (volume that hit the bid), and
- how much aggressive buying (volume that lifted the offer).

So a single 5-minute Bank Nifty footprint candle isn't one candle — it might be forty stacked cells from 48,180 up to 48,380, each showing the bid/ask volume battle at that price. You are reading the *internal structure* of the move, not just its outcome.

The logic rests on the same auction foundation as CVD, but with resolution. CVD tells you the net aggression was, say, −8,000 over the bar. The footprint tells you *the selling was concentrated at the top of the bar around 48,360–48,380* — which is a completely different story from selling spread evenly, and a different story again from selling concentrated at the low. The footprint answers **"where inside the range did the fight happen, and who blinked?"**

## Construction, rules and settings

### The four display modes

Every serious order-flow platform (GoCharting, Quantower, Sierra Chart, ATAS, TradingView's newer order-flow tier) offers these modes. Know all four; each answers a different question.

| Mode | What each cell shows | Best for |
|---|---|---|
| **Bid × Ask** | Two columns per price: sell-volume (bid) on the left, buy-volume (ask) on the right | Spotting absorption/exhaustion at a level |
| **Delta** | Single number per price: (ask − bid) volume, colored | Fast read of net aggression by level |
| **Volume profile** | Total volume per price (no split) | Seeing where volume concentrated (HVN/LVN inside the bar) |
| **Delta % / imbalance** | Percentage skew or highlighted diagonal imbalances | Systematic imbalance detection |

### Diagonal imbalance — the key mechanic

The single most important footprint concept is the **diagonal imbalance**, and beginners get it wrong by reading horizontally. In a Bid×Ask footprint you compare the **ask volume at one price** to the **bid volume at the price one tick below it** (a diagonal, staircase comparison). Why diagonal? Because the buyer lifting the offer at price P and the seller hitting the bid at price P are trading against *different* resting orders; the meaningful contest is between aggressive buyers at P and aggressive sellers at P−1, since those are the orders competing to set the next print.

A common rule: flag a **buy imbalance** when ask-volume at P is ≥ 3× (300%) the bid-volume at P−1, and a **sell imbalance** when bid-volume at P is ≥ 3× the ask-volume at P+1. Stacked imbalances — three or more consecutive imbalanced cells in the same direction — mark aggressive initiative and often become support/resistance on the retest (an "imbalance shelf").

### Reading absorption and exhaustion

- **Absorption:** heavy aggressive volume at a price that *fails to move price further*. Example: at the high of the bar, ask (buying) volume is enormous — 4,200 contracts lifted the offer at 48,380 — yet price does not print higher. Someone passive absorbed all that buying with limit sell orders. That is a bearish tell: aggression met a wall.
- **Exhaustion:** the *opposite* footprint — aggressive volume *dwindles* at the extreme. Sellers pushed price down bar after bar, but the final cell at the low shows tiny bid volume (say 180 contracts) versus thousands above. The aggressive selling ran out; the low is likely to hold.
- **Unfinished auction / naked point of control:** a bar high or low that printed *both* bid and ask volume (buying and selling still active at the extreme) tends to get revisited — the auction wasn't "finished" there.

### Settings for NSE futures

- **Tick per row:** Bank Nifty is volatile; grouping every price tick makes cells too sparse. Group rows by 5 or 10 points so each cell holds meaningful volume. Nifty FUT: group by 2–5 points. Otherwise you get a spray of tiny numbers with no statistical weight.
- **Bar interval:** 5-minute or volume/range bars beat 1-minute for footprints — you need enough trades per cell for the bid/ask split to be reliable.
- **Instrument:** futures only. The spot index has no traded volume to footprint.
- **Data quality:** this is the crux (see Pitfalls).

## Worked India example (levels and ₹)

Bank Nifty futures, 5-minute footprint, rows grouped by 10 points. Lot size 15 (₹15/point/lot).

Price has rallied all morning and is testing the prior-day high at **48,600**. The 11:05 candle prints a high of 48,610 then closes back at 48,555. You open the Bid×Ask footprint on that candle:

```
Price      Bid(sell)   Ask(buy)
48,610        120        3,980   <- massive buying, price barely tagged it
48,600        260        4,410   <- buy imbalance vs 48,590 bid
48,590        180        3,050
48,580      2,900          640
48,570      3,400          520   <- selling now dominating on the way back down
48,560      3,100          410
```

Read it: at 48,600–48,610 buyers were *ferociously* aggressive — 4,410 and 3,980 contracts lifted the offer — yet price could not sustain above 48,610. That is textbook **absorption**: passive sellers (likely defending the prior-day high and a heavy 48,600 call strike) soaked up ~8,000 contracts of aggressive buying without giving ground. Then, on the same candle, delta flips hard negative in the 48,560–48,580 zone as trapped longs bail and initiative sellers press.

**The trade:** short on the close back below 48,590 (the failed breakout), stop above 48,620 (above the absorbed high) — risk 30 points = ₹450/lot. Target the session VWAP at 48,400 — reward 190 points = ₹2,850/lot, better than 6:1. On 10 lots that's roughly ₹28,500 for ₹4,500 of risk. Price grinds to 48,410 by 12:20; you cover most into VWAP. The footprint gave you what CVD alone could not: *proof of where* the absorption happened and *confirmation* via the delta flip on the same bar.

Contrast: had the 48,600 cells shown buying that *did* push price to 48,650 with **stacked buy imbalances** all the way up and thin bid volume, that's initiative buying, not absorption — you'd stand aside or join long on the retest of 48,600 as new support.

## How to trade it

### Setup 1 — Absorption reversal at a level
- **Location first:** PDH/PDL, VWAP band, big option strike, prior imbalance shelf.
- **Trigger:** heavy aggressive volume at the extreme that fails to extend + delta flip on the reversal bar.
- **Entry:** on the close back inside the level. **Stop:** just beyond the absorbed extreme. **Target:** VWAP / value-area edge.

### Setup 2 — Stacked-imbalance continuation
- Three-plus consecutive buy (or sell) imbalances mark an aggressive initiative leg.
- Trade the **retest** of the imbalance shelf: buy the pullback to the lowest imbalanced cell holding, stop below the shelf.

### Setup 3 — Exhaustion at the extreme
- Diminishing aggressive volume into a new low (exhaustion tail).
- Enter on the first bar that shows delta flipping positive off the low; tight stop under the exhaustion print.

### Setup 4 — Unfinished-auction target
- Mark bar extremes that printed both bid and ask volume as "magnets." Use them as *targets* for the next session, not entries.

**Management across all:** footprint trades are precise, so stops are tight and R-multiples are high, but hit-rate is moderate. Scale out half at 1.5–2R, trail the remainder to the opposite value-area edge. If price re-enters an absorbed zone with fresh aggression that *isn't* absorbed the second time, you were wrong — exit immediately.

## Confluence

- **Volume profile / value area:** absorption at a naked POC or value-area high is far more reliable.
- **CVD:** the running total (previous chapter) plus the footprint's *location detail* is the complete order-flow picture — CVD says pressure is fading, footprint says exactly where.
- **Options OI:** absorption at a strike with a huge call/put OI wall is the same event seen from two angles — passive option-writers hedging is often the very liquidity doing the absorbing.
- **VWAP:** footprints work best when the level coincides with VWAP or its standard-deviation bands.

## Pitfalls

1. **Data quality is the whole ballgame — and it's shaky on NSE.** A footprint is only as truthful as its bid/ask classification. NSE retail feeds frequently lack clean aggressor flags, so many platforms *reconstruct* the bid/ask split from tick data or lower-timeframe candles. That reconstruction can misclassify volume, especially in fast moves. A beautiful footprint built on estimated data can be confidently, precisely wrong. Verify what your platform actually receives.
2. **Snapshot vs true tick data.** Some Indian feeds are *snapshots* (updates every few hundred ms), not every trade. Volume between snapshots gets bucketed imperfectly. Footprints demand genuine tick-by-tick data.
3. **Too few contracts per cell.** On thin instruments or too-fine row grouping, each cell has so little volume that imbalances are statistical noise. Group rows sensibly; only footprint liquid futures (Nifty, Bank Nifty, Fin Nifty, top single-stock futures).
4. **Reading horizontally instead of diagonally.** Imbalances are diagonal by definition. Comparing bid vs ask *at the same price* is a beginner error that fabricates signals.
5. **Absorption that isn't.** Heavy volume at a high sometimes just precedes a *breakout* — the buying wasn't absorbed, it was *accumulating*, and one more push clears the level. Distinguish by whether price *holds* after the volume (absorption) or *extends* (initiative). Require the delta flip and the close back inside before calling absorption.
6. **Overtrading the resolution.** The footprint shows so much detail that you can find a "signal" in every candle. Discipline: only act at *pre-defined levels*. The footprint refines your entry; it does not manufacture your thesis.
7. **Cost and latency.** True order-flow data and platforms cost money and demand a fast feed. For a swing trader on end-of-day data, footprints are irrelevant — this is an intraday, execution-grade tool.

## Interview-ready summary

A footprint chart decomposes each price bar into per-price cells showing the bid (aggressive sell) versus ask (aggressive buy) volume that traded at every level inside the bar — the auction's full transcript rather than its four-number summary. Its four modes (Bid×Ask, Delta, Volume, Imbalance) each answer a different question, and its central mechanic is the **diagonal imbalance**: aggressive buying at price P compared to aggressive selling at P−1, flagged at a 3× threshold, with stacked imbalances marking initiative and forming retest shelves. The two highest-value reads are **absorption** (huge aggressive volume at an extreme that fails to move price — passive liquidity winning) and **exhaustion** (aggressive volume dwindling into the extreme). In Indian markets, footprint only the liquid futures (Nifty, Bank Nifty, Fin Nifty), group rows sensibly (Bank Nifty ~10 points), trade only at pre-defined locations (PDH/PDL, VWAP, option strikes), and pair it with CVD and options OI. The honest caveat is data quality: NSE retail feeds often lack clean aggressor flags, so many footprints are *reconstructed estimates* — precise-looking but only as truthful as the underlying tick data. Used at the right level with the right data, the footprint gives an execution edge — a tighter, better-proven entry — that no summary indicator can match.
