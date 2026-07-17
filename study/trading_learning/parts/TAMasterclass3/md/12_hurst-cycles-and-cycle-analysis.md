# Hurst Cycles & Cycle Analysis

Most technical tools live in the value dimension — where is support, what does momentum say. Cycle analysis lives almost entirely in the *time* dimension: it asks when the market is likely to make a low, when it is likely to make a high, and how those rhythms nest inside one another. J.M. Hurst, an American aerospace engineer, formalised this thinking in the 1970s in *The Profit Magic of Stock Transaction Timing*, and his framework remains the most rigorous, rule-based approach to market cycles ever published. This chapter unpacks Hurst's model — nominal cycles, the principles of commonality and summation, the FLD and centred moving averages — and applies it to Nifty and Bank Nifty with rupee levels. It is also unusually candid about where cycle analysis is real signal and where it is the human brain's genius for seeing rhythm in randomness.

## What it is and the logic

Hurst's central claim is that price is the *sum* of several periodic components (cycles of different lengths) plus a trend component and a small random residual. If you could isolate each cycle, you would know when each is due to bottom, and by adding the expected bottoms of several cycles you could forecast a *cluster* — a window where multiple cycles trough together, producing a strong, reliable low.

Hurst codified this in a set of principles. Five matter most:

1. **Commonality** — the same nominal cycle lengths appear across virtually all liquid instruments. Nifty, Bank Nifty, an NSE large-cap and even USDINR share a family of cycle lengths, differing mainly in amplitude.
2. **Cyclicality** — a large share of price motion is oscillatory, not trend, and those oscillations are approximately periodic.
3. **Summation** — the price you see is the arithmetic sum of the individual cycles; peaks look sharp when short and long cycles crest together, troughs look sharp when they bottom together.
4. **Harmonicity** — adjacent cycles in the model are related by roughly a factor of two (each cycle is about half the length of the next longer one).
5. **Synchronicity** — cycles tend to bottom *together*; troughs are more synchronised and reliable than peaks, which is why Hurst timing hunts for *lows*.
6. **Variation & Nominality** — real cycle lengths vary around their nominal value (a "20-day" cycle might run 18–22 days), so cycles are tendencies, not clockwork. This principle is the honest heart of the method: it tells you upfront that the tool is approximate.

The logic is genuinely appealing because it is *additive and testable* rather than mystical. But note the escape hatch built into "variation and nominality": because lengths flex, a determined analyst can almost always fit a cycle after the fact. The discipline is to commit to a nominal length and a tolerance *before* the low forms, and to trade only cycle-cluster lows confirmed by price.

## Construction, rules and settings

### The nominal cycle model

Hurst identified a nested set of nominal lengths, each roughly double the last. Adapted to trading-day counts for Indian equities:

| Nominal cycle | Approx length | Practical use |
|---------------|--------------|---------------|
| 5-day (weekly) | ~5 trading days | intraday-to-swing noise |
| 10-day | ~10 days | short-swing timing |
| 20-day | ~20 days (≈1 month) | the core swing-trading cycle |
| 40-day | ~40 days (≈2 months) | intermediate swings |
| 80-day | ~80 days (≈4 months) | position-trading cycle |
| 20-week (~100-day) | ~1 quarter | major intermediate low |
| 40-week (~200-day) | ~9–10 months | primary trend cycle |
| 18-month / 54-month | longer | investing horizon |

Each nominal length carries a tolerance of roughly ±10–15%. The **20-day cycle** is the workhorse for NSE swing traders; the **40-week (~200-day)** cycle governs the primary trend and lines up conceptually with the 200-DMA everyone already watches.

### Finding cycle lows

**Step 1 — Visual trough spacing.** Mark obvious swing lows on a Nifty daily and measure the bar-count between them. If lows cluster near 18–22 bars apart, you have located the 20-day cycle. Repeat for longer lows to find the 40- and 80-day cycles.

**Step 2 — The Centred Moving Average (CMA).** Hurst's core smoothing tool. A CMA of length *n* is a simple moving average shifted *backward* by (n−1)/2 bars so it sits centred over the data it smooths. A CMA tuned to a cycle length flattens that cycle and reveals the *next longer* one. Because it is shifted back, its most recent portion is undefined — Hurst's method estimates the missing end, which is where subjectivity enters. Setting: to isolate the 20-day cycle, use a CMA around the length of the *next* cycle (≈40) and read the residual.

**Step 3 — The FLD (Future Line of Demarcation).** Hurst's cleanest, most rule-based signal. The FLD for a cycle of length *n* is simply the price series displaced *forward* by n/2 bars:

> FLD(n) at time *t* = Price at time *t − n/2*

For the 20-day cycle, plot today's chart with the closing price shifted 10 bars into the future. When *current price crosses its own FLD upward*, the cycle has bottomed and turned up; a downward cross signals the cycle top. The FLD also yields price targets (see below). Because it is a mechanical displacement, the FLD removes much of the eyeballing that plagues cycle work — its main virtue.

**Step 4 — Nesting / the cluster.** Overlay the 20-, 40- and 80-day cycle low projections. Where their next-expected-lows fall within a few days of each other, you have a **cycle cluster** — the high-probability window for a durable bottom.

## Worked India example (levels & ₹)

### Nifty 20-day cycle and FLD

Suppose over the past several months Nifty printed clear swing lows spaced 19, 21, 20 and 18 trading days apart — a textbook 20-day cycle averaging ~19.5 days. The last such low was at **23,600**. Project the next 20-day low: roughly 19–20 trading days later, tolerance ±3 days, so a *window* rather than a date.

Now plot the 20-day FLD (close displaced forward 10 bars). As the projected low window approaches, Nifty is falling toward **23,700**. On the third day of the window it prints **23,680**, a hammer forms, and the next session **price crosses above its 20-day FLD**. That upward FLD cross inside the cycle-low window is the buy signal.

**FLD price target.** Hurst's rule of thumb: when price crosses the FLD, the move often travels a distance roughly equal to the gap between the crossing price and the FLD's prior peak/trough, projected forward. If at the cross the FLD's recent peak sat at 24,100 and price crossed at 23,700, a first objective near **24,100 + (24,100 − 23,700) = 24,500** is reasonable — treat it as a guide, not a guarantee.

### Nesting with the 40- and 80-day cycles

Extend the analysis. Say the 40-day cycle also projects a low in the same week (its prior low was ~40 days before this window), and the 80-day cycle's next trough is due within five sessions too. Three cycles cluster. The 23,680 low therefore is not just a 20-day low — it is a **20-40-80 cluster low**, which historically produces the most durable Nifty rallies. Conviction and size can be higher here than for a lone 20-day low, and the stop can be placed just below the cluster low at, say, **23,550**.

### Bank Nifty 40-day cycle

Bank Nifty, being higher-beta, shows the same nominal lengths with larger amplitude. Suppose its 40-day cycle lows sit around **48,900** two months ago and the next 40-day trough is projected for a given week. Price falls to **49,200**, crosses its 40-day FLD upward, and rallies. The FLD target math projects toward **51,000**, hit over the following three weeks. Note the amplitude: the same cycle that moves Nifty ~500–700 points moves Bank Nifty ~1,800–2,000 — commonality in *timing*, not in *size*.

## How to trade cycles

**Entry.** The clean, rule-based entry is the **FLD cross inside a projected cycle-low window**, confirmed by a reversal candle. Do not buy merely because a cycle is "due" — due-ness is a heads-up; the FLD cross plus candle is the trigger. Prefer cluster lows (multiple cycles troughing together) for your largest positions.

**Stop.** Below the cycle low that formed at the FLD cross (or below the cluster low). If price re-enters and closes back below the FLD, the cycle read is failing — exit. Keep monetary risk at a fixed fraction of capital; on Bank Nifty size by points-to-stop given its wider swings.

**Target.** Use the FLD projection (crossing-to-prior-extreme distance projected forward) as a first objective, and the *next longer cycle's expected high* as a second. Because peaks are less synchronised than troughs (synchronicity applies to lows), trail stops on the way up rather than trusting a precise top forecast.

**Management.** As the *next* cycle low approaches while you are long, expect a pullback and decide in advance whether to hold through it (if the larger cycle is still rising) or trim. In F&O, align option expiries with the expected cycle span — do not buy a weekly option to express a 20-day-cycle thesis; the theta math will beat you before the cycle plays out. A monthly or next-month option, or futures, fits a 20-day cycle better.

## Confluence — where cycles earn trust

- **Cycle-low window + horizontal support:** a projected 20-day low coinciding with a prior support shelf and a round number is far stronger than the cycle alone.
- **FLD cross + momentum turn:** the FLD cross with a simultaneous RSI turn up from oversold is a high-quality trigger.
- **Cluster low + Fibonacci time zone:** if a Fibonacci time line (previous chapter) and a Hurst cycle cluster fall in the same window, two independent timing methods agree — the strongest time-based signal available.
- **200-DMA and the 40-week cycle:** when the 40-week cycle low is due near the 200-DMA, trend and cycle reinforce for position entries.

## Pitfalls

1. **Apophenia — seeing cycles in noise.** The human brain finds rhythm everywhere. Some cyclicality in markets is real (options expiry, quarterly results, budget/policy calendars impose genuine periodicity), but much apparent regularity is coincidence. Guard against it by *pre-committing* nominal lengths and tolerances and by demanding an FLD-cross confirmation.
2. **The CMA end-point problem.** The centred average is undefined at the most recent (n−1)/2 bars — exactly where you need it. Estimating the missing end is subjective and is where most cycle "forecasts" quietly become curve-fits. The FLD, being a pure displacement, is more honest; lean on it.
3. **Right/left translation ignored.** In strong uptrends cycle peaks shift *right* (late), in downtrends *left* (early). Traders who expect the high at the exact cycle midpoint get whipsawed. Read translation as a trend gauge, not a bug.
4. **Cycle length drift.** Nominal ±15% variation means a "20-day" cycle can genuinely run 17 or 23 days. Trading a fixed calendar date rather than a window is a classic error.
5. **Peaks are unreliable.** Synchronicity applies to *lows*. Hunting cycle *tops* with the same confidence as cycle bottoms is a known trap — trail stops instead.
6. **Event overrides.** A budget shock, an RBI surprise, or a global risk-off can blow through any cycle projection. Cycles describe the market's *internal* rhythm; large exogenous news dominates it. Never trade a cycle low into a known binary event without adjusting size.

## Interview-ready summary

Hurst cycle analysis models price as the *summation* of several nested, roughly harmonic cycles (each about double the last — 5, 10, 20, 40, 80 days, up through the 40-week primary cycle) plus trend and noise. Its principles — commonality (same lengths across instruments), summation, harmonicity, synchronicity (lows bottom together and are more reliable than peaks) and nominality/variation (lengths flex ±10–15%) — make it the most rigorous, rule-based cycle framework available. The two working tools are the **Centred Moving Average**, which smooths one cycle to reveal the next longer one but suffers an undefined recent end-point, and the **Future Line of Demarcation (FLD)** — price displaced forward n/2 bars — whose upward cross inside a projected cycle-low window is a genuinely mechanical buy trigger with a built-in price target. The high-conviction setup is a **cluster low**, where 20-, 40- and 80-day cycles trough together, ideally in confluence with support, momentum, a Fibonacci time line, or the 200-DMA. The honest caveats to state plainly: markets contain some real periodicity (expiry, results, policy calendars) but the brain over-detects rhythm, the CMA's end-point invites curve-fitting, cycle lengths drift, peaks are far less reliable than troughs, and any large scheduled event overrides the internal rhythm. Used with pre-committed lengths, FLD confirmation and strict risk control, Hurst cycles add a disciplined *when* to the technician's *where* on Nifty, Bank Nifty and liquid NSE names — and used loosely, they become the most elegant way to fool yourself with hindsight.
