# Anchored VWAP Strategies (Deep)

Session VWAP, covered in the previous chapter, always starts at the day's open — a mechanical, calendar-driven anchor. **Anchored VWAP (AVWAP)** breaks that constraint. You choose the starting point. Instead of "the average price paid *today*", AVWAP answers "the average price paid by everyone who has traded *since the event that actually matters*" — since the earnings gap, since the swing high, since the day the FII selling began, since the budget, since the IPO listing. That single freedom transforms VWAP from a day-trading tool into one of the most powerful swing- and position-trading references in technical analysis, because it lines the tool up with the memory of the participants who are actually trapped or in-profit.

This chapter goes deep: where to anchor and why, how AVWAP encodes the collective break-even of a cohort of traders, a full toolkit of multi-anchor strategies, and detailed India examples on Nifty, Bank Nifty and cash stocks with levels and rupees. Anchored VWAP is more discretionary than session VWAP — the anchor choice is a judgement call — so we will be honest about where subjectivity lives and how to discipline it.

## What it is & the logic

An anchored VWAP is computed with exactly the same volume-weighted formula as session VWAP, but the cumulative sums begin at a **user-chosen bar** and never reset until you say so:

```
AVWAP(t) = Σ[from anchor to t] (TP_i × V_i)  /  Σ[from anchor to t] (V_i)
```

Because it accumulates from the anchor, AVWAP represents **the average price every participant has paid since that event**. That is its entire power. Consider the anchor set to a major swing low. Every trader who bought from that low is, on average, in profit while price trades above the AVWAP and in loss below it. AVWAP therefore maps directly onto the *collective break-even of a cohort* — and break-even is where human behaviour clusters: trapped longs sell to "get out even", underwater shorts cover, dip-buyers add. Support and resistance from AVWAP is not mystical; it is the arithmetic of a crowd defending its cost basis.

Where you anchor decides *whose* cost basis you are tracking:

- **Anchor to a swing low** → the break-even of the buyers who caught the bottom. Holds as support in an uptrend.
- **Anchor to a swing high** → the break-even of the buyers who caught the top (the trapped bulls). Acts as resistance on the way back up — the level where trapped longs finally escape flat.
- **Anchor to an earnings/results gap** → the average price of everyone who traded the new information regime. The most-watched AVWAP for a stock post-results.
- **Anchor to an IPO/listing day** → the break-even of every investor since listing. Powerful for newly listed names (a very active category on NSE).
- **Anchor to a macro event** (Budget day, RBI policy, election result, a big FII-flow reversal) → the fair value the market has assigned since the regime shifted.

## Construction, rules & settings

### Choosing the anchor (the whole discipline)

The rule of thumb: **anchor to the bar of maximum significance and, ideally, maximum volume.** A valid anchor is a bar the market will *remember* — a visible pivot, a gap, an event everyone saw. Anchoring to a random mid-trend bar produces a line no cohort is defending, and it will not work. Good anchor candidates:

| Anchor type | When to use | What it tells you |
|---|---|---|
| Major swing low | Uptrend / bottom-fishing | Bull cohort break-even; trend support |
| Major swing high | Downtrend / trapped-bull tracking | Bear/trapped-long break-even; resistance |
| Earnings gap bar | Post-results trading | Fair value under new fundamentals |
| Listing day | Newly listed stocks | All-holders break-even |
| Budget / RBI / election bar | Index & rate-sensitive trades | Post-regime fair value |
| Highest-volume bar of the move | Any | Where the most capital committed |

### Multi-anchor overlay

Professionals rarely use one AVWAP; they stack several — from the last swing low, the last swing high, and the most recent event — and read the *interaction*. Where two independent AVWAPs converge, you get a high-conviction level defended by two different cohorts at once.

### Settings & platform notes

- **TradingView** ships the "Anchored VWAP" tool natively; click the anchor bar, and optionally enable ±σ bands off the anchor (same band maths as the previous chapter, computed from the anchor forward).
- Use **futures** for Nifty/Bank Nifty (spot has no volume — the AVWAP would be volume-fictional); use native volume for cash stocks.
- Anchored bands widen as the window lengthens; on a months-long anchor the ±1σ band is a genuinely useful swing channel.
- Redraw discipline: pick the anchor, then leave it. Constantly "re-anchoring" to make the line touch price is curve-fitting after the fact.

## Worked India example (levels & ₹)

### Example 1 — Swing-low AVWAP as trend support (cash stock)

**Tata Motors.** Suppose a decisive swing low prints at **₹620** on heavy volume, and the stock rallies. Anchor AVWAP to that ₹620 bar. Over the next six weeks the stock climbs to ₹760, and every pullback is bought precisely at the rising AVWAP: pullback 1 to ₹688 (AVWAP 686), pullback 2 to ₹714 (AVWAP 712). The bull cohort is defending its collective break-even.

**The trade:** buy the third pullback into the AVWAP at ~₹730 (AVWAP 728), stop at ₹716 — *below* AVWAP, which invalidates the "buyers in profit" thesis. Target the prior high ₹760 and trailing beyond. Risk ₹14, first target ₹30 → 1:2+. On roughly a 550-share F&O lot (confirm current lot on NSE), ₹30 captured ≈ **₹16,500** gross per lot. The AVWAP loss at ₹716 would have flipped the cohort underwater — a disciplined, structural exit, not a guess.

### Example 2 — Swing-high AVWAP as resistance (index futures)

**Nifty futures.** A blow-off top prints at **24,850**, the market sells off to 23,400, then recovers. Anchor AVWAP to the 24,850 high bar. As Nifty grinds back up, the AVWAP from the high sits at, say, **24,300** and *slopes down* — it is the average price of everyone who bought near the top and is desperate to get out flat. Price rallies into 24,300, stalls exactly at the AVWAP, and rolls over. **Short at 24,300**, stop above 24,420 (a decisive reclaim would mean the trapped-bull supply is absorbed), target back to 23,800/23,400. Risk 120 points, reward 500 → deep asymmetry. At 25/lot (confirm Nifty lot), 500 points ≈ **₹12,500** gross.

### Example 3 — Earnings-gap AVWAP (the post-results reference)

**HDFC Bank** gaps up on results from 1,640 to 1,700. Anchor AVWAP to the gap bar. For the next month the stock consolidates, and the earnings-AVWAP (rising through ~1,690–1,710) becomes the pivot: above it, the results are being "paid up" for; a close back below it signals the gap is failing. A swing trader goes long only while price holds the earnings-AVWAP, stop on a daily close below it — a clean, event-grounded rule that keeps you on the right side of the post-results regime.

### Example 4 — Two anchors converging (confluence trade)

On **Bank Nifty futures**, the swing-low AVWAP (rising from 46,900) reaches **48,150** at the same time the swing-high AVWAP (falling from 49,600) also reaches **48,150**. Two cohorts — bottom-buyers in profit and top-buyers at break-even — both have a stake at 48,150. That convergence is a decision point: a break and hold above it flips the trapped-bull supply into support (long, target 48,600+); a rejection sends price back toward the low AVWAP. Trade the resolution, not the guess, with the stop just beyond the convergence.

## How to trade it (entry, stop, target, management)

### Strategy 1 — Swing-low AVWAP pullback (trend-following)

| Element | Rule |
|---|---|
| Setup | Uptrend; AVWAP anchored to the launch swing low; price above and holding it |
| Entry | Buy pullbacks that tag the rising AVWAP with a rejection candle |
| Stop | A daily/structural close *below* AVWAP (cohort flips underwater) |
| Target | Prior high, then trail with the rising AVWAP or its +1σ band |
| Add | Add on each successful re-test that holds AVWAP |

### Strategy 2 — Swing-high AVWAP fade (counter-trend / mean-reversion)

| Element | Rule |
|---|---|
| Setup | Market recovering into a falling AVWAP anchored at a significant high |
| Entry | Short the first tag of the AVWAP that stalls |
| Stop | Decisive reclaim above the AVWAP (supply absorbed) |
| Target | Prior swing low / next support; take partials into it |

### Strategy 3 — Event-AVWAP regime filter (position bias)

Anchor to the earnings gap, Budget bar, or listing day and use it purely as a **bias line**: only take longs while price holds above the event-AVWAP, only shorts below. It won't time entries by itself — pair it with a session-VWAP or breakout trigger — but it keeps you aligned with the post-event fair value, which is where most of the edge in swing trading lives.

### Strategy 4 — Convergence / "AVWAP squeeze"

When two or more meaningful AVWAPs coil into the same price, volatility compresses and a directional resolution usually follows. Set a break-and-hold trigger either side of the convergence, stop just inside it, and target the measured range. This is AVWAP's version of a squeeze setup.

**Universal management:** because AVWAP encodes a cohort's break-even, the *cleanest possible stop* is the point where that break-even thesis fails — a decisive close on the wrong side of the line. Size to a fixed rupee risk against that structural stop; never a fixed point stop, because different anchors sit different distances from price.

## Confluence

- **Session VWAP (previous chapter):** session VWAP for *today's* fair value plus an event-AVWAP for the *regime's* fair value is a professional pairing — the anchored line frames the swing, the session line times the day.
- **Value Area / naked POC:** an AVWAP that lands on a prior naked POC is doubly defended — two independent "fair-price" references at one level.
- **Fibonacci & structure:** AVWAP tagging a 61.8% retracement or a prior breakout shelf multiplies conviction.
- **Options OI:** an event-AVWAP sitting at a heavy-OI strike tells you the options market and the cash cohort agree on the pivot — a strong magnet/wall.
- **Multiple timeframes:** a weekly-swing AVWAP defining the big picture and a recent-event AVWAP defining the trade keeps top-down and bottom-up aligned.

## Pitfalls

- **Anchoring to insignificant bars.** The cardinal sin. If no cohort remembers the bar, no one defends the line. Anchor only to visible, high-volume, event bars.
- **Re-anchoring to fit price.** Sliding the anchor until the line "works" is curve-fitting after the outcome is known. Choose the anchor from the chart's structure, then commit.
- **Index AVWAP on spot.** Same India trap as session VWAP — Nifty/Bank Nifty spot has no volume, so anchor on **futures**.
- **Anchor-proliferation.** Ten AVWAPs on one chart is noise. Keep two or three meaningful anchors; more obscures rather than clarifies.
- **Treating the line as an exact price.** AVWAP is a zone; use candle confirmation at the tag, not a limit order to the tick.
- **Forgetting the anchor ages.** A months-old AVWAP flattens and loses sensitivity; a very recent anchor is jumpy. Match the anchor's age to your holding period.
- **Ignoring corporate actions.** Splits, bonuses and heavy delivery-based restructurings distort long AVWAPs on cash stocks; verify the volume/price series is adjusted.
- **Over-trusting a counter-trend fade.** Shorting a swing-high AVWAP in a powerful V-recovery can get run over if the trapped supply is fully absorbed on the first tag. Demand a stall/rejection before entering.

## Interview-ready summary

Anchored VWAP is a volume-weighted average price computed from a *user-chosen* event bar rather than the session open, and its power is that it maps the **collective break-even of the cohort that traded since that event** — which is exactly where crowd behaviour, and therefore support and resistance, clusters. Anchor to a swing low and it is bull-cohort support; to a swing high, trapped-bull resistance; to an earnings gap, listing day or macro event, the post-regime fair value. The core strategies are the swing-low pullback (buy tags of the rising AVWAP, exit on a close below it), the swing-high fade (short stalls into a falling AVWAP), the event-AVWAP bias filter (trade only on the favourable side of the line), and the multi-anchor convergence squeeze (trade the resolution where two AVWAPs coil). On Indian markets, anchor on **futures** for indices and native volume for stocks, choose only significant high-volume anchor bars and never re-anchor to fit, and stop out where the cohort's break-even thesis fails — a decisive close on the wrong side of the line. Paired with session VWAP, Value Area, Fibonacci and options OI, anchored VWAP is the bridge between intraday fair value and swing-trading conviction, honest about its one weakness: the anchor is a judgement call, and the discipline is in choosing it well and leaving it alone.
