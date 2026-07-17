# Setups: Trend Continuation (5 setups)

Trends are where the easy money hides — but only if you enter *with* the trend rather than trying to be the hero who calls the top or bottom. Trend-continuation setups are entries taken in the direction of an already-established trend, after a pause, a shallow pullback, or a small counter-trend structure that resolves back the original way. They are the bread and butter of the systematic Indian swing trader because the base rate is friendly: a stock already in a strong uptrend is far more likely to make a new high than a fresh reversal. Your job is not to predict — it is to *join a move already in progress* at a point where risk is small and the trend's momentum can carry you.

This chapter gives you five named, rules-based continuation setups tuned for Nifty 50, Bank Nifty and liquid NSE cash stocks. Each has an exact trigger, stop, target and the market regime in which it works. Continuation setups have one enemy above all others: a **choppy, trendless market**. Run these only when the instrument is genuinely trending — 20 EMA above 50 EMA above 200 EMA (or the reverse for shorts), ADX above 20-25, and higher highs / higher lows visible on the chart. In a sideways tape they will chop you to death.

## Why continuation setups work

Trends persist because of a chain of human and structural behaviours. Institutions accumulate over weeks, not minutes — a large mutual fund building a ₹500-crore position in an HDFC Bank or a Reliance cannot buy it all at once, so it feeds orders in on every dip, creating a staircase of higher lows. Momentum funds and CTAs pile on once a trend is measurable. Retail traders who missed the initial move wait for "a pullback to get in", and their buying supports every retracement. Short-sellers who faded the move too early are forced to cover, adding fuel. Each of these actors buys weakness in an uptrend, and the sum of their behaviour is the very pullback-and-continue pattern we are trading.

The edge is probabilistic, not certain. Roughly, a well-filtered continuation entry in a trending regime wins 45-55% of the time but pays 2-3x the risk when it works, because the trend does the heavy lifting on the winners. You lose small and often; you win big occasionally. That asymmetry — not a high hit-rate — is the entire source of profit. If you cannot stomach a string of four or five small stop-outs before a runner appears, continuation trading is not for you.

## Setup 1 — The Moving-Average Pullback (20 EMA bounce)

The workhorse. In a clean uptrend a liquid stock rarely trades in a straight line; it oscillates around a rising moving average, typically the 20 EMA on the daily. When price pulls back to touch or slightly pierce the 20 EMA and then shows a bullish rejection candle, you buy the resumption. The moving average acts as a dynamic support that trend-followers and algos watch, so the level becomes partly self-fulfilling.

| Element | Rule |
|---|---|
| Regime | Daily uptrend: 20 EMA > 50 EMA, price making higher highs, ADX > 20 |
| Trigger | Price pulls back to 20 EMA; entry on break above the high of a bullish rejection candle (hammer, bullish engulfing, or strong close) |
| Stop | Below the swing low / below the 50 EMA, whichever is tighter but gives ~1.5-2% room on a large-cap |
| Target | Prior swing high first (T1), then trail on 20 EMA close for the runner |
| Timeframe | Daily entry; can refine on 1-hour |
| Position | Risk 1% of capital; size = risk ÷ (entry − stop) |

**Worked example — Reliance Industries.** Suppose Reliance is trending up from ₹2,780 toward ₹3,000, with the 20 EMA rising through ₹2,910. Price drifts back over three sessions to ₹2,915, printing a hammer that closes at ₹2,930 with the low at ₹2,905 (a wick right onto the EMA). Next day price trades above ₹2,935 — your trigger. You buy at ₹2,938, stop at ₹2,898 (below the hammer low), risk ₹40/share. T1 is the prior high near ₹3,000 (a 1.5R target); you book half there and trail the rest below the 20 EMA. If the stock extends to ₹3,120 before closing under the EMA, the runner delivers roughly 4.5R on the second half. On ₹1,00,000 risked-at-1%, that single trade returns well over ₹2,500 net of the small first tranche.

**Confluence to demand:** the pullback should come on *lighter* volume than the advance (weak selling), and the rejection candle should come on a volume uptick (buyers stepping in). If the stock has liquid options, a rising Put OI at the strike just below your entry (say the 2,900 PE building open interest) tells you writers see that zone as support — a quiet institutional vote in your favour.

**Pitfalls:** the 20 EMA bounce fails when the trend is already exhausted (price extended far above the 200 EMA, RSI diverging) or when the "pullback" is actually the start of a distribution top. Never take this setup after a climactic, gap-driven blow-off; wait for the first *orderly* pullback, not the first violent one.

## Setup 2 — Flag / Pennant Breakout

After a sharp, near-vertical advance (the "flagpole"), price often consolidates in a tight, slightly down-sloping channel (a flag) or a small symmetrical triangle (a pennant) for 3-10 sessions. This is the market catching its breath while weak hands take profit and new buyers accumulate. The breakout above the flag resumes the pole's move, and the classic measured target projects the pole's height from the breakout point.

| Element | Rule |
|---|---|
| Regime | Strong impulsive move just completed (the pole); intraday or daily |
| Trigger | Break and close above the flag's upper trendline on rising volume |
| Stop | Below the flag low (or below the lower trendline) |
| Target | Measured move = flagpole height added to breakout price; partial at 1:1, trail rest |
| Timeframe | Works on 5-min/15-min intraday and on daily swing |
| Regime filter | Avoid if the pole itself looks like a news-gap that may reverse |

**Worked example — Bank Nifty intraday.** Bank Nifty rallies from 48,200 to 48,900 in the first ninety minutes (a 700-point pole) on a strong global cue. It then chops sideways-to-down between 48,780 and 48,900 for the next hour — a bull flag. You mark the upper edge at 48,900. When a 15-minute candle closes at 48,940 on expanding volume, you go long the index via a near-the-money call or a futures proxy. Stop goes below the flag low at 48,760 (risk ~180 points). Measured target = 48,940 + 700 = 49,640. You book half near 49,300 (roughly 1:2) and trail the rest with a 15-min swing-low stop; if the index runs to 49,600 you capture most of the projected move. Because Bank Nifty options decay fast, prefer slightly ITM calls or futures for the pole-continuation leg so theta does not eat the flag's consolidation time.

**Confluence:** the tighter and lower-volume the flag, the better — it signals genuine rest, not distribution. A flag that widens, sags heavily, or eats more than half the pole is suspect; that is often a reversal in disguise.

**Pitfalls:** false breakouts are common on the very first push, especially near round numbers (49,000 on Bank Nifty). Demand a *close* beyond the line, not just a wick, and ideally a small retest that holds.

## Setup 3 — Higher-High / Higher-Low Continuation (structure break)

This is pure price-structure trading with no indicators. In an uptrend price makes a higher high (HH), then a higher low (HL). When price breaks above the most recent minor swing high — confirming the next HH — you enter, because the structure has printed one more leg up. It is the most timeframe-agnostic continuation setup and the backbone of price-action trading.

| Element | Rule |
|---|---|
| Regime | Visible sequence of HH-HL on your trading timeframe |
| Trigger | Break above the last confirmed minor swing high after a fresh higher low forms |
| Stop | Below the fresh higher low |
| Target | 1:2 minimum; trail by moving stop under each new HL |
| Timeframe | Any — 15-min intraday to weekly positional |
| Filter | Skip if the last HL barely cleared the previous low (weak structure) |

**Worked example — Tata Motors positional.** Tata Motors is in an uptrend on the daily. It prints a high at ₹1,020 (HH), pulls back to ₹958 and turns up — a higher low versus the prior low of ₹930. Once price breaks ₹1,020 you buy at ₹1,024 with the stop below the ₹958 higher low, risking ₹66/share. As the trend extends, each new HL (say ₹1,050, then ₹1,110) becomes your new trailing stop location. This "stop under the last higher low" method keeps you in a multi-week move while defining risk objectively at every step. If the stock runs from ₹1,024 to ₹1,280 over six weeks, you ride most of it, exiting only when a lower low finally breaks the structure.

**Confluence:** align with a higher timeframe — a daily HH-HL entry is stronger when the weekly is also trending up. On liquid F&O names, watch futures open interest: rising price with *rising* OI on each up-leg means fresh longs are being added (healthy continuation); rising price with falling OI is short-covering that may fizzle.

**Pitfalls:** the danger is entering after an over-extended run where the next "higher high" is a bull trap. Combine with a distance-from-mean check — if price is 8-10% above the 20 EMA on a large-cap, the odds of a shallow continuation shrink and a deeper pullback becomes likely.

## Setup 4 — Pullback to Broken Resistance (role reversal)

When price breaks above a well-tested horizontal resistance, that old ceiling frequently becomes new support. A pullback that holds the broken level offers a low-risk continuation entry with a razor-tight stop just under the level. This "polarity flip" is one of the most reliable continuation patterns because it is watched by both breakout traders (who add on the retest) and value buyers (who missed the breakout and want a second chance).

| Element | Rule |
|---|---|
| Regime | Fresh breakout of a horizontal level that had been tested 2+ times |
| Trigger | Pullback to the broken level; entry on a bullish reversal candle holding above it |
| Stop | Below the level (allow a small buffer for the usual dip beneath) |
| Target | Next resistance / measured move of the range; partial + trail |
| Timeframe | Daily swing ideal; also intraday |
| Filter | Best when the breakout closed strongly, not on a marginal wick |

**Worked example — Nifty 50 index.** Suppose Nifty repeatedly failed at 22,800 over several weeks, then finally closed decisively at 22,950. Over the next few sessions it eases back to 22,810 — right onto old resistance now acting as support — and prints a bullish engulfing candle closing at 22,880. You go long (via an index proxy or an ATM call spread) at 22,890 with a stop at 22,740 (a 150-point buffer below the flip zone). The measured move of the prior 22,400-22,800 range projects roughly 400 points, targeting ~23,200. You scale out into strength and trail the balance. The beauty here is the *location* of the stop: just under a level the whole market agrees is important, so if it fails you are out cheaply and correctly.

**Confluence:** in the option chain, watch the 22,800 strike flip from heavy Call OI (resistance) to heavy Put OI (support) after the breakout — writers migrating their bets is a strong tell that the polarity flip is real. Rising volume on the breakout and *declining* volume on the pullback complete the picture.

**Pitfalls:** the "buffer below the level" is critical — markets routinely dip a touch under a broken level to shake out tight stops before resuming. Place your stop below the *noise*, not exactly at the level, or you will be stopped out of trades that then work.

## Setup 5 — ADX-Confirmed Trend Ride (momentum add-on)

The other four setups are entries; this one is a *filter-and-add* framework that turns a single entry into a compounding trend ride. It uses ADX to confirm trend strength and pyramids into winners as the trend proves itself, which is how you convert an ordinary continuation trade into an outsized one.

| Element | Rule |
|---|---|
| Regime | ADX rising and above 25; +DI above −DI (uptrend) |
| Trigger | Initial entry on any of Setups 1-4; add on each new pullback that holds |
| Stop | Trail the whole position under the most recent higher low; never widen |
| Target | No fixed target — exit when ADX rolls over from a high or structure breaks |
| Timeframe | Daily positional |
| Add rule | Each add is half the previous size; move combined stop to keep total risk ≤ 1% |

**Worked example — Bharti Airtel positional.** Airtel begins a trend with ADX crossing 25 rising. You take an initial position on a 20 EMA pullback (Setup 1) at ₹1,180, 100 shares, stop ₹1,150. Two weeks later it pulls back to a higher low at ₹1,240 and resumes; you add 50 shares and lift the combined stop to ₹1,215 (locking the first tranche green and keeping net open risk near zero). A third pullback to ₹1,320 lets you add 25 shares, stop to ₹1,300. The pyramided position rides from ₹1,180 to ₹1,480 before ADX peaks and rolls, and a lower low finally stops you out around ₹1,440. Because you added into strength with shrinking size and a rising stop, your average is favourable and the trend paid for the whole structure.

**Confluence:** ADX tells you *how much* trend energy is present, not direction — always pair it with +DI/−DI or simple structure. Falling ADX from a high (say from 40 down through 30) is your warning to stop adding and start tightening.

**Pitfalls:** pyramiding is a double-edged sword. If you add without raising the stop, one sharp reversal gives back everything. The iron rule: total open risk across all tranches must never exceed your single-trade risk budget. Never average *down* — that is the opposite of a continuation setup and the classic account-killer.

## Putting the five together — a regime map

These setups are not mutually exclusive; the professional runs them as one system. In a strong, clean daily uptrend with ADX above 25, Setup 5 governs and Setups 1-4 supply the entries and the add points. When a name breaks a major horizontal level, Setup 4 gives the highest-quality first entry. After a sharp news-driven surge, Setup 2 (flag) is the natural continuation vehicle. On quieter trends, Setups 1 and 3 do the everyday work.

The single most important decision precedes all five: **is this a trending regime at all?** If ADX is under 20, if the moving averages are tangled, if price is chopping in a range, none of these setups has an edge — you are better off flat or trading the range from its edges (a different playbook entirely). Continuation trading rewards patience: you wait for a trend to establish, wait for a pullback within it, wait for the trigger candle, and only then act. Most of your time is spent watching, not clicking.

## Risk, sizing and the honest maths

Fix your risk per trade at 1% of capital and never exceed it, including pyramids. With continuation setups winning perhaps half the time at an average 2R, your expectancy per trade is roughly (0.5 × 2R) − (0.5 × 1R) = +0.5R. Over 100 trades that is +50R, or +50% on a 1%-risk model *before* the drag of costs and slippage — an excellent year, achieved through dozens of small losses and a handful of large wins. The emotional trap is that the losses cluster: you can easily lose five in a row when trends stall, and it is precisely then that traders abandon the method right before the next runner. Trust the process, keep the size constant, and let the winners run to their trailing stop.

Costs matter in India: STT, exchange fees, GST and brokerage on frequent trailing exits add up. Prefer fewer, larger continuation swings over many tiny scalps, and use the measured-move and trailing-stop logic to hold winners rather than churning. On F&O, mind expiry and theta — for multi-day continuation on indices, futures or slightly ITM options preserve your directional edge better than cheap OTM weeklies that bleed while the flag consolidates.

## Interview-ready summary

Trend-continuation setups enter *with* an established trend after a pause or shallow pullback, exploiting the fact that a trending instrument is more likely to extend than reverse. The five core setups are: **(1) the 20 EMA pullback** — buy the bounce off the rising average on a rejection candle; **(2) the flag/pennant breakout** — buy the resolution of a tight consolidation after a sharp pole, targeting a measured move; **(3) the HH-HL structure break** — buy the break of the last swing high after a fresh higher low, trailing under each new higher low; **(4) the pullback to broken resistance** — buy the retest of an old ceiling now acting as support, with a tight stop below the flip; and **(5) the ADX-confirmed trend ride** — pyramid into a proven trend with shrinking size and a rising stop. All five demand a genuine trending regime (aligned EMAs, ADX > 20-25, visible HH-HL) and die in chop. Confluence from volume, higher-timeframe alignment and option-chain OI (Put writing at support, rising OI with rising price) sharpens the edge. Risk is fixed at ~1% per trade; the profit comes from asymmetry — many small losses, occasional large trend-following winners — not from a high win-rate.
