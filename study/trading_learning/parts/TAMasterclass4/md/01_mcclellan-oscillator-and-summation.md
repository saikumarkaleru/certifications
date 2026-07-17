# McClellan Oscillator & Summation Index

Price tells you what the *index* is doing. Breadth tells you what the *army behind the index* is doing. In a cap-weighted world where five stocks — Reliance, HDFC Bank, ICICI Bank, Infosys, TCS — can drag Nifty up 200 points while 900 other names quietly bleed, that distinction is not academic. It is the difference between chasing a rally that is about to reverse and standing aside because you saw the internals rot before the tape did.

The McClellan Oscillator and its running total, the McClellan Summation Index, are the two most refined breadth tools ever built. They were designed by Sherman and Marian McClellan in 1969 for the NYSE, but the mathematics is index-agnostic — it works on any universe where you can count advancers and decliners. For an Indian trader that universe is the NSE: roughly 2,000+ listed equities, or if you want a cleaner signal, the constituent counts of the Nifty 500, Nifty Midcap 150, or the all-important Nifty 50 itself. This chapter builds both indicators from the ground up, shows you exactly how to read them off a real NSE breadth series, and — most importantly — teaches you when they lie.

## What it is and the logic

Every trading day, the exchange publishes how many stocks closed higher than the previous day (**advances**) and how many closed lower (**declines**). The raw difference, **Net Advances = Advances − Declines**, is the heartbeat of the market. On a broad-based rally day you might see 1,600 advances against 400 declines on the NSE — a net of +1,200. On a distribution day the numbers flip.

The problem with raw net advances is that it is impossibly noisy — it whips from +1,200 to −900 day to day and tells you nothing about *trend* in participation. The McClellan brothers' insight was to smooth net advances with two **exponential moving averages** of different speeds and take the difference between them. That difference is the McClellan Oscillator.

Why two EMAs? Because the gap between a fast average and a slow average of the same series *is* momentum. When breadth is accelerating — each day bringing broader participation than the fading memory of the slow average — the fast EMA pulls above the slow one and the oscillator rises. When participation decelerates, the fast EMA rolls over first and the oscillator falls, often *while price is still making highs*. That early roll-over is the entire reason the tool exists: **breadth momentum peaks before price.**

The **Summation Index** is simply the running cumulative total of the daily oscillator. If the oscillator is breadth *momentum* (a first derivative), the Summation Index is breadth *trend* (the integral). It is slow, it is smooth, and its crossings of zero and its own turning points define bull and bear market phases with a reliability that price-only tools cannot match.

## Construction: the formulas

Start with the two EMAs of Net Advances. The classic McClellan settings are a 19-day and a 39-day EMA, which correspond to smoothing constants of 10% and 5% respectively.

| Component | Formula | Smoothing constant |
|---|---|---|
| Net Advances (NA) | Advances − Declines | — |
| Fast EMA (19-day) | Prev + 0.10 × (NA − Prev) | 10% |
| Slow EMA (39-day) | Prev + 0.05 × (NA − Prev) | 5% |
| **McClellan Oscillator** | Fast EMA − Slow EMA | — |
| **Summation Index** | Prior Summation + today's Oscillator | — |

Worked mechanics. Suppose yesterday the Fast EMA stood at +150 and the Slow EMA at +90 (oscillator +60). Today the NSE prints 1,500 advances and 500 declines, so NA = +1,000.

- New Fast = 150 + 0.10 × (1000 − 150) = 150 + 85 = **235**
- New Slow = 90 + 0.05 × (1000 − 90) = 90 + 45.5 = **135.5**
- New Oscillator = 235 − 135.5 = **+99.5**

The oscillator jumped from +60 to +99.5 — a strong broad day pushed breadth momentum up. Add +99.5 to the running Summation Index and it climbs too.

**The ratio-adjusted version (use this for India).** Raw net advances have a fatal flaw for long-term comparison: the number of listed stocks grows over time. A net of +1,000 on the NSE in 2010 (fewer listings) meant something different from +1,000 in 2026. The fix is **Ratio-Adjusted Net Advances (RANA)**:

> RANA = (Advances − Declines) / (Advances + Declines) × 1000

Because the denominator is total issues traded, RANA is self-normalising — it always ranges between −1000 and +1000 regardless of how many stocks are listed. Feed RANA (instead of raw NA) into the same two EMAs. This is the version that keeps overbought/oversold thresholds stable across years, and it is the one you should build in TradingView or Chartink for the NSE. Most charting platforms that offer a McClellan study default to ratio-adjusted.

### Reading levels

For the **Oscillator** (ratio-adjusted, on a broad NSE universe):

| Reading | Interpretation |
|---|---|
| Above +100 | Overbought breadth thrust; strong but stretched |
| +50 to +100 | Healthy bullish participation |
| −50 to +50 | Neutral / churn zone |
| −100 to −50 | Bearish participation |
| Below −100 | Oversold; capitulation or panic breadth |
| Crossing zero upward | Short-term momentum turning bullish |
| Crossing zero downward | Short-term momentum turning bearish |

For the **Summation Index**, absolute levels matter less than direction and zero-line position:

| Condition | Meaning |
|---|---|
| Summation rising and above zero | Confirmed bull phase; buy dips |
| Summation falling but above zero | Bull losing steam; tighten stops |
| Summation crossing below zero | Regime shift to bearish |
| Summation rising from deep negative | Early accumulation; bottoming |

## Worked India example

Consider a stylised but realistic Nifty scenario across a five-week stretch, the kind that plays out around every intermediate top. Nifty grinds from 24,600 to a fresh all-time high of 25,400, up roughly 3.2%. The financial-heavyweight names — HDFC Bank, ICICI, SBI — do the lifting. Retail sentiment is euphoric; the news flow is all "record highs."

Now watch the breadth underneath. During the first leg (24,600 to 25,000) the daily NSE advance figures are broad: 1,400–1,600 advancers repeatedly. RANA prints strongly positive, the Oscillator sits between +80 and +120, and the Summation Index rises steeply. This is a *confirmed* advance — index up, breadth up, everything aligned. You hold longs and buy the shallow dips.

During the second leg (25,000 to 25,400) something changes. Nifty makes three successive higher highs, but on those exact days advancers barely edge out decliners — 1,050 advances against 950 declines. RANA collapses toward the zero line even as price prints new highs. The Oscillator, which had been at +110, rolls over to +40, then +10, then dips *negative* on the day of the marginal new price high. The Summation Index stops rising and flattens.

This is a **breadth divergence** — the single most valuable pattern the McClellan family produces. Price high, breadth momentum lower. It says: fewer and fewer stocks are participating; the index is being held aloft by a shrinking cluster of large-caps while the broad market has already begun to distribute. In the Indian context this is the classic "Nifty green, portfolio red" trap that catches retail longs in mid- and small-caps.

The trade logic: you do not short the first divergence day — divergences can persist. But you (a) stop adding longs, (b) tighten stops on existing positions to just under the last swing low, and (c) prepare a short/hedge trigger. The trigger fires when the **Oscillator closes decisively below zero** *and* the **Summation Index turns down**. When both happen — say Nifty is at 25,350, Oscillator at −60, Summation rolling over — you have confirmation that momentum and trend in participation have both flipped. Historically, Nifty then gave back the entire final leg and more, sliding to 24,700 over the following two weeks. The trader who read the internals exited near 25,300; the trader who read only price sold in the panic near 24,800.

The mirror image works at bottoms. In a washout, the Oscillator plunges below −150 (a rare oversold extreme), advancers dry to 200 against 1,800 decliners for several days, and then — while Nifty is still grinding to a marginal new low — the Oscillator prints a *higher* low. Fewer stocks are making the new low than made the prior one. That positive breadth divergence, followed by the Oscillator reclaiming zero and the Summation Index hooking up from its trough, is one of the highest-quality intermediate bottom signals available on the NSE.

## The breadth thrust

There is a special, powerful configuration worth isolating: the **McClellan breadth thrust**. When the Oscillator rockets from a deeply oversold reading (below −100) to a strongly overbought one (above +100) within a handful of sessions, it signals that money has flooded back into the *broad* market with violence. This is not the same as the index bouncing; it means overwhelming, universal buying. After genuine market bottoms — the COVID low of March 2020 on the Nifty, the recovery off major corrections — such thrusts appear and reliably mark the start of durable up-legs. A thrust off a bottom is a "get long and stay long" message; the breadth is telling you the rally has a broad base of support, not just a handful of index heavyweights.

## How to use it for bias and timing

Breadth tools are **context** instruments, not standalone trade triggers. Layer them into your process like this:

1. **Set the regime with the Summation Index.** Above zero and rising: your default bias is long; you take long setups off support and treat shorts as counter-trend scalps only. Below zero and falling: default bias short; longs are counter-trend. This one filter keeps you on the right side of the intermediate trend.

2. **Time entries and exits with the Oscillator.** Within a bull regime, an Oscillator dip to oversold (−50 to −100) that then hooks back up is your dip-buy timing. Within a bear regime, an Oscillator push to overbought that rolls over is your short-the-bounce timing.

3. **Hunt divergences at extremes.** When price makes a new high/low and the Oscillator does not, flag it. Do not act on the divergence alone — wait for the zero-line confirmation described above.

4. **Respect the thrust.** A genuine breadth thrust off a bottom overrides bearish price memory. Do not fight it with shorts.

5. **Match the universe to the trade.** If you trade Nifty and Bank Nifty index F&O, compute breadth on the Nifty 500 or the full NSE — broad participation. If you trade a specific segment, use that segment's breadth. Broad-market breadth can be healthy while the small-cap universe is collapsing, and vice versa; know which one your position lives in.

## Pitfalls

**Do not use it as a trigger by itself.** Every breadth tool generates apparent signals that never resolve into trades. Divergences can run for weeks; overbought can stay overbought through the strongest part of a bull run. The Oscillator turning negative is only actionable *with* price and Summation confirmation.

**Cap-weight vs. breadth mismatch is a feature, not a bug — but you must know which one your instrument tracks.** Nifty is cap-weighted; the McClellan is equal-vote (every stock counts once). When they disagree, that *is* the signal — but if you are trading Nifty futures and blindly short because breadth is weak, you can still lose while the top-five heavyweights melt up. Breadth warns of fragility; it does not time the heavyweight roll-over precisely.

**Data quality matters.** Your advance/decline counts must come from a consistent universe every day. Mixing "all NSE issues" one day with "Nifty 500 only" the next corrupts the EMAs. Use a single, stable source (a Chartink screener count, or a platform's built-in NSE breadth feed).

**Illiquid and newly-listed stocks pollute raw counts.** Thinly-traded SME names and fresh IPOs create noise in the advance/decline tally. The ratio-adjusted formula and a liquid universe (Nifty 500) mitigate this.

**Holidays and short weeks distort EMAs briefly.** Indian market holidays create gaps; the EMAs recover within a few sessions, but do not over-read a single post-holiday print.

**Overbought is not "sell" in a young bull.** After a breadth thrust, the Oscillator will scream overbought for weeks — that is strength, not a top. Only late-cycle overbought readings *with divergence* warn of exhaustion.

## Interview-ready summary

The McClellan Oscillator is the difference between a 19-day and a 39-day exponential moving average of net advances (advances minus declines), best computed in ratio-adjusted form — (A−D)/(A+D)×1000 — so thresholds stay stable as the number of listed NSE stocks grows. It measures breadth *momentum*: readings above +100 are overbought, below −100 oversold, and zero-line crossings flag short-term momentum shifts. Its cumulative running total is the McClellan Summation Index, which measures breadth *trend* — rising above zero defines a bull phase, falling below zero a bear phase. The tool's highest-value pattern is the breadth divergence: price makes a new high while the Oscillator makes a lower high, warning that a shrinking group of large-caps is holding a cap-weighted index (Nifty) aloft while the broad market distributes. Act only when the Oscillator confirms below zero and the Summation Index turns down. A "breadth thrust" — the Oscillator surging from below −100 to above +100 — off a bottom is a durable buy signal. Use the Summation Index to set regime bias and the Oscillator to time entries; never trade breadth in isolation, always with price and level confirmation. In India, compute it on the Nifty 500 or full NSE universe to keep the equal-vote signal clean.
