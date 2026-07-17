# Timeframes & Multi-Timeframe Analysis

## What it is & why it works

A timeframe is simply the amount of time each candle (or bar) on your chart represents. A 5-minute candle bundles five minutes of trading into one open, high, low and close; a daily candle bundles a whole session; a weekly candle bundles Monday-to-Friday into a single bar. Multi-timeframe analysis (MTFA) is the discipline of looking at the *same* instrument through two or three of these lenses at once — a higher timeframe to read the context and direction, a lower timeframe to time the entry — and only trading when the two agree.

The reason it works is not chart magic; it is a fact about markets. Price is fractal. The same behaviour — trends, pullbacks, ranges, breakouts — repeats at every scale, but the **weight** of a signal is proportional to the timeframe that produced it. A support level that formed on a 5-minute chart represents a few dozen crores of intent from intraday scalpers and algos; a support level on the weekly chart represents months of accumulated positioning from institutions, mutual funds, FIIs and DIIs who cannot enter or exit in a single tick. When those two disagree, the bigger money wins the argument. A weekly downtrend does not care that your 5-minute chart just printed a pretty bullish flag.

MTFA solves the single most common failure in retail trading: taking a technically valid signal that happens to be pointing *against* the dominant flow. A textbook bullish engulfing on the 15-minute Nifty chart is a real pattern — but if the daily chart is in a clean downtrend below a falling 20-EMA and the weekly just rejected a resistance zone, that engulfing is most likely a counter-trend bounce that will be sold. The pattern is not wrong; the *context* is wrong. Higher timeframes supply that context. Think of it as three questions asked in order: *Which way is the river flowing?* (higher timeframe — direction), *Where along the bank am I standing?* (intermediate timeframe — the level/structure), and *Is the current turning right now?* (lower timeframe — the trigger). You never let the lowest timeframe answer the first question.

There is also a behavioural edge. When you commit to trading only in the direction of the higher timeframe, you automatically filter out the majority of noise-driven, revenge, and boredom trades — the ones that come from staring at a 3-minute chart and mistaking wiggle for signal. MTFA is as much a psychological governor as an analytical tool.

## The mechanics

**The rule of "3 to 6".** The classic guidance is that your three chosen timeframes should each be roughly 4–6 times the one below it — enough separation that the higher chart genuinely represents a different class of participant, not just a slightly zoomed-out version of the same noise. Common India-desk stacks:

| Trader type | Higher (context) | Intermediate (structure) | Lower (trigger) | Typical hold |
|---|---|---|---|---|
| Scalper (index/F&O) | 15-min | 5-min | 1-min | seconds–minutes |
| Intraday | Daily | 1-hour (75-min) | 15-min / 5-min | minutes–hours |
| Swing (BTST/positional) | Weekly | Daily | 1-hour | days–weeks |
| Positional / investor | Monthly | Weekly | Daily | weeks–months |

Note the NSE-specific quirk: the Indian equity session runs 09:15–15:30, 375 minutes. That divides cleanly into **75-minute** bars (5 candles a day) and 15-minute bars (25 a day), which is why 75-min is a favourite "intermediate" chart on Indian desks — it respects the session boundary far better than the imported 60-minute bar, which leaves an ugly 15-minute stub candle at 15:15.

**The workflow (top-down, always).**
1. **Higher timeframe — set the bias.** Mark the trend (higher highs/lows or lower highs/lows), the position of price relative to a long anchor (200-DMA, weekly 20-EMA), and the nearest major support/resistance zones. Output: *long only / short only / no-trade*.
2. **Intermediate timeframe — find the location.** Within that bias, find the actual structure you will trade *from*: a pullback into a support zone, a demand/supply level, a trendline, a moving average. Output: *the price area where a trade is allowed*.
3. **Lower timeframe — time the trigger.** Only when price reaches that area, drop down and wait for a specific entry signal (break of a micro-swing, a reversal candle, a 5-min pattern completion). Output: *the exact entry, and the stop level*.

**Alignment vs conflict.** The four states:

| Higher | Lower | State | Action |
|---|---|---|---|
| Up | Up | Aligned bullish | Highest-probability longs |
| Down | Down | Aligned bearish | Highest-probability shorts |
| Up | Down | Conflict | Wait — likely a pullback in an uptrend; buy the *end* of the lower-TF down move |
| Down | Up | Conflict | Wait — likely a bounce in a downtrend; sell the *end* of the lower-TF up move |

The conflict states are the money-makers *if you read them correctly*: a lower-timeframe move against the higher timeframe is exactly what a healthy pullback looks like. You are not fighting it; you are waiting for it to exhaust and then joining the higher-timeframe direction with a tight, well-located stop.

**Settings hygiene.** Keep indicator settings *identical* across timeframes (a 20-EMA on all three), so the numbers are comparable. Use "regular trading hours" only for intraday charts (exclude pre-open). For continuous instruments, be aware that MTFA on options is treacherous — the higher-timeframe chart of an option premium is distorted by theta and IV; for MTFA always read the **underlying** (Nifty/Bank Nifty spot or futures), then express the trade in options.

## Reading it — a worked India example

Take a realistic Nifty swing setup. Suppose it is a Tuesday in 2026 and Nifty spot is trading around **24,650**.

**Weekly (context).** The weekly chart shows a sequence of higher highs and higher lows since a swing low near 22,800. Price sits above a rising weekly 20-EMA around 24,100. The last three weekly candles are small-bodied and overlapping — a pause, not a reversal — sitting just under a prior weekly high at **24,900**. Verdict: primary trend **up**; we are long-biased; the ceiling to respect is 24,900 and the floor is 24,100.

**Daily (structure).** On the daily, Nifty rallied from 24,050 to 24,880, then pulled back over five sessions to **24,600**, landing exactly on (a) the rising 20-DMA and (b) a prior breakout shelf around 24,580–24,650 that used to be resistance and should now act as support (role reversal). Volume shrank on the pullback — classic healthy retracement, not distribution. Verdict: this is a textbook *buy-the-dip location* inside the weekly uptrend. The "allowed zone" is **24,580–24,660**.

**Hourly / 75-min (refine).** The 75-min chart shows the five-day drop as a clean falling channel. Price is now sitting at the lower channel line and the RSI(14) on this timeframe has ticked up from 34 to 41 — momentum is turning but no trigger yet. This tells us we are *at* the location and *close* to a turn, but we do not buy the falling knife; we drop one more level.

**15-min (trigger).** At 11:30 the 15-min chart prints a higher low at **24,632** versus an earlier low at 24,608, then a strong green candle closes back above the minor swing high at **24,690** on visibly larger volume. That break of the micro-swing high, occurring *inside* the daily support zone, *inside* the weekly uptrend, is the aligned trigger. All three timeframes now point the same way: weekly up, daily buy-zone, 15-min bullish break.

**The trade.** Long Nifty (via a futures lot or an in-the-money call / bull call spread) at **24,695**, stop just below the 15-min higher low and the daily zone at **24,590** (risk ≈ 105 points), first target the swing high **24,880** and the weekly ceiling **24,900** (reward ≈ 190–205 points, roughly 1.9R). If 24,900 breaks on a daily close, the measured move from the 24,100→24,900 base projects toward **25,300**, so the runner target extends. This is the entire value of MTFA in one picture: the higher timeframe told us *long only and where the ceiling is*, the daily told us *the exact shelf to buy*, and the 15-min told us *the precise moment and the tight stop* — turning a vague "Nifty looks okay" into a defined 105-point-risk, ~200-point-reward trade.

## Trading it

**Entry trigger.** Never enter on the higher timeframe's signal alone — it is too coarse and its stop would be enormous. Wait until price reaches the higher-timeframe location, then take the *lower* timeframe's confirmation: a break of a micro-swing, a reversal candle (engulfing, pin/hammer) closing in your direction, or a lower-TF pattern completion. The alignment is the edge; the lower TF is the timing.

**Stop.** Place it beyond the structure on the *timeframe you entered from*, not the higher timeframe. In the example, the stop hugs the 15-min higher low (24,590), which is also the edge of the daily zone — a happy coincidence of two timeframes agreeing on the invalidation point. This is why aligned trades give the best risk-reward: the natural stop is tight (lower-TF structure) while the target is generous (higher-TF room).

**Scenario A — clean run (aligned).** Price breaks 24,690, never revisits, tags 24,880, stalls at 24,900. Book half, trail the rest under rising 15-min higher lows. If 24,900 gives way on a daily close with volume, hold the runner for 25,300.

**Scenario B — failed trigger (the fake).** Price breaks 24,690, pops to 24,720, then rolls straight back and closes a 15-min candle below 24,632. The trigger failed; the pullback was not done. You are stopped at 24,590 for a defined ~105-point loss. Crucially, the *weekly bias is unchanged* — so you do not flip short; you wait for the next 15-min higher low inside the zone and re-attempt. MTFA makes you patient because you know the river is still flowing your way.

**Scenario C — conflict, don't trade.** Suppose instead the weekly had just closed below its 20-EMA and printed a lower high. Now the 15-min bullish engulfing is a *counter-trend* signal. You either skip it entirely or treat it as a quick scalp with a tiny target and no expectation of a swing — never as a positional long. Same candle, opposite decision, because the higher timeframe changed.

**Position sizing by alignment.** A practical rule: full size only when all three timeframes agree; half size when the higher timeframe agrees but the intermediate is merely neutral; no trade when the higher timeframe disagrees. Let the degree of alignment scale your risk.

## Confluence

MTFA is itself a confluence engine, but it becomes far more powerful stacked with other tools:

- **Moving averages as timeframe anchors.** A daily 20-EMA pullback that *also* sits on the weekly 20-EMA is a double-timeframe support. In the example, buying at the daily 20-DMA while the weekly 20-EMA sat just below at 24,100 meant even a deeper flush had a catcher's mitt.
- **Fibonacci across scales.** Draw the retracement on the higher timeframe (weekly swing) and trade the touch on the lower. A 24,600 daily level that coincides with the weekly 38.2% retracement is stronger than either alone.
- **Option-chain / OI confirmation (index F&O).** This is where India-first MTFA shines. Before taking the long, check the current-expiry option chain: heavy **Put OI at 24,600** (matching the daily support) and the highest **Call OI at 24,900** (matching the weekly ceiling) means the options market has independently drawn the *same* floor and ceiling your charts did. Max-pain sitting near 24,700 supports a rangebound-to-up drift. When the OI walls and the chart levels line up, conviction rises and you can size up. If, instead, Put OI at 24,600 is thin and being aggressively written *above*, the support is weaker than the chart suggests — a reason to wait for a cleaner trigger.
- **PCR and VWAP for intraday timing.** On the 15-min trigger, an entry taken as price reclaims the day's VWAP, with the intraday PCR turning up, adds a same-session tailwind to the multi-day thesis.
- **Volume across timeframes.** Shrinking volume on the daily pullback (supply drying up) plus expanding volume on the 15-min break (demand arriving) is the ideal volume signature — one timeframe shows exhaustion, the other shows ignition.

The principle: each higher timeframe you add is one more independent witness. Three timeframes plus an OI wall pointing at the same price is four witnesses to the same level — that is a high-probability trade.

## Pitfalls & false signals

- **Analysis paralysis / too many charts.** Four, five, six timeframes do not multiply your edge; they multiply contradictions until you can always find *some* chart that agrees with the trade you already wanted. Cap it at three. If you need a fourth, you are rationalising, not analysing.
- **Timeframes too close together.** Watching 5-min, 6-min and 10-min is not multi-timeframe analysis — it is the same noise three times. Keep the 4–6× spacing so each chart genuinely represents a different participant.
- **Letting the low timeframe override the high.** The cardinal sin. A gorgeous 5-min setup against a clean weekly downtrend feels irresistible precisely because it is a trap for the impatient. When in conflict, the higher timeframe is the tie-breaker, always.
- **The repainting higher-TF candle.** The current weekly or daily candle is *unfinished* — its "signal" can vanish by the close. Read completed candles for bias; only the entry-timeframe candle may be acted on intrabar, and even then with care. Beginners get faked out by a mid-week weekly candle that looks bullish on Wednesday and closes bearish on Friday.
- **Ignoring the session structure.** Using a 60-minute chart on NSE leaves a distorted stub candle and misaligns your levels; prefer 75-min or 15-min, which divide the 375-minute session evenly.
- **Event risk collapses all timeframes.** On RBI policy day, Budget day, or a major earnings/expiry, a gap can leap straight through your daily support and blow past the 15-min stop before it can fill. Around known events, either stand aside or pre-size for gap risk; MTFA reads *orderly* markets, not headline shocks.
- **Higher-TF right, but you're early.** Being correct on direction but entering before the location is reached is the most common way to lose on a "right" idea. Discipline is: bias first, *then wait for price to come to the level*, then trigger. Do not front-run the zone.

Pros filter these by treating the higher timeframe as a veto (it can forbid a trade but a lone lower-TF signal can never authorise one against it), by acting only on closed higher-TF candles, and by demanding that the entry location be *pre-marked* before price arrives — never drawn after the fact to justify a fill.

## Interview-ready summary

"Multi-timeframe analysis means reading the same instrument on three timeframes that are 4–6× apart — a higher one for **direction**, an intermediate for **location**, and a lower one for the **trigger** — and trading only when they align. Markets are fractal, so the same patterns appear at every scale, but bigger timeframes carry bigger money and therefore win when they conflict. I work top-down: the weekly sets long-or-short bias, the daily marks the support/resistance zone I'm allowed to trade from, and the 15-minute times the exact entry and the tight stop. For Indian index trading I use 75-minute bars because the 375-minute NSE session divides into five of them cleanly, and I cross-check my chart levels against the option chain — Put OI at my support, Call OI at my resistance — so the OI walls become an independent witness to the same levels. The higher timeframe is a veto: it can forbid a trade, but no lower-timeframe signal is ever allowed to authorise one against it. That single rule filters out most low-quality, counter-trend, noise-driven trades."
