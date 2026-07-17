# Setups Library Part 1 (Trend, Pullback, Breakout)

## What it is & why it works

A "setup" is not a chart pattern in isolation. It is a *repeatable, rule-defined combination of context, trigger, and risk* that has produced a positive expectancy over a large sample of trades. The difference between a beginner who "sees a flag" and a professional who "takes the flag setup" is that the professional has pre-defined the exact conditions under which he acts, the exact price that says he is wrong, and the exact target that pays him. Everything else on the chart is noise he has trained himself to ignore.

This chapter is the first half of a working setups library for Indian equity and index traders. It covers the three foundational long/short families that together account for the majority of a swing and positional trader's profitable trades: the **trend-continuation entry** (getting on board an established move), the **pullback / retracement buy** (buying a dip inside an uptrend), and the **breakout** (entering as price escapes a consolidation). Parts of the same taxonomy — reversals, ranges, and OI-confluence setups — are covered in Part 2.

Why do these setups work at all? Because markets are driven by the collective positioning of participants who are slow to change their minds and slow to act. A trend persists because institutions accumulate over weeks, not minutes — an FII building a position in Reliance or HDFC Bank cannot buy ₹3,000 crore in one candle. A pullback works because in a genuine uptrend, dips are met by buyers who missed the first leg and by trend-followers adding on weakness. A breakout works because a horizontal level is a *memory* — it is where supply and demand fought last time, and when price finally clears it, the trapped shorts must cover and the sidelined longs must chase, creating a self-reinforcing thrust. Each setup is simply a way of harnessing a specific, recurring behaviour of the crowd.

The honest caveat, stated once here and true throughout: none of these setups is right more than roughly 45–60% of the time. They make money because the winners are engineered to be larger than the losers. A setup is a *risk framework* first and a *prediction* second.

## The mechanics

Every setup in this library shares the same skeleton. Define these six fields and you have a tradeable rule:

| Field | Question it answers |
|---|---|
| Context filter | Is the higher-timeframe trend aligned? Is this a trending or a choppy regime? |
| Trigger | The exact candle/event that puts me in |
| Entry | The precise price and how I get filled |
| Stop | The price that proves the idea wrong |
| Target / exit | Where I take profit or how I trail |
| Invalidation | Conditions under which I *don't* take the trade even if the trigger fires |

**1. Trend-continuation entry.** Context: price above a rising 20 and 50 EMA on the trading timeframe, with the daily also up (multi-timeframe alignment). The mechanic is to enter *on strength within strength* — either a break of a minor swing high after a shallow one-to-three-bar pause, or a bounce off the rising 20 EMA. Trigger: a bullish close reclaiming the prior bar's high. Stop: below the most recent higher-low swing. This is the lowest-drama family — you are paying up to join a move that is already proving itself.

**2. Pullback / retracement buy.** Context: same uptrend, but you deliberately wait for a *counter-move* to give you a better price and a tighter stop. The mechanics rest on three anchors that tend to coincide: (a) a Fibonacci retracement zone, typically the 38.2%–61.8% of the prior impulse leg; (b) a rising moving average (20 EMA for shallow pullbacks, 50 EMA for deeper ones); and (c) a prior structural level (old resistance now acting as support). The trigger is a *reversal candle* in that zone — a bullish engulfing, hammer, or pin bar — closing back up. The stop sits just below the pullback low.

**3. Breakout.** Context: a defined consolidation — a rectangle, triangle, flag, or a multi-week base — with a clear horizontal or trendline resistance. The mechanics require you to pre-mark the level, then wait for a *decisive* close beyond it. "Decisive" must be operationalised: a close beyond the level by more than a small buffer (e.g., 0.3–0.5% for an index, or beyond the average bar's noise), ideally on above-average volume. The measured move — the projected target — is the height of the consolidation added to the breakout point.

A note on the two breakout entry styles, because it is where most traders lose money:

| Style | Entry | Pro | Con |
|---|---|---|---|
| Breakout entry | On the close above the level | Never misses the move | Whipsawed by false breaks |
| Retest entry | On the pullback back to the broken level | Tighter stop, filters fakes | Misses runaway breakouts that don't retest |

The professional default in Indian markets — where morning gaps and news-driven fakeouts are common — leans toward the **retest**, or toward waiting for a *retest that holds* before committing full size.

## Reading it — a worked India example

Take **Bank Nifty over a hypothetical but realistic four-week stretch.** Assume the index has rallied from 47,200 to 49,800 over three weeks, riding a rising 20-day EMA. This is our trending context: daily up, 20 EMA rising beneath price, each dip holding a higher low. All three of our setups appear inside this single move — that is the point, they are phases of one trend.

**Phase 1 — the trend-continuation entry.** Early in the run, Bank Nifty pauses for two sessions between 48,000 and 48,200 after a strong thrust day. The pause is shallow — price never closes below the prior swing low at 47,900. On the third day it opens at 48,150 and pushes through the two-day high of 48,220. That break of the minor swing high, with price hugging the rising EMA, is the continuation trigger. You are buying strength that has just refused to pull back — the shallowness of the pause is itself the tell that demand is aggressive.

**Phase 2 — the pullback buy.** After tagging 49,000, Bank Nifty finally corrects. Over three sessions it slides to 48,300. Now measure the leg that ran from the 47,900 swing low to the 49,000 high — that is 1,100 points. The 61.8% retracement sits at 49,000 − (0.618 × 1,100) = 48,320. The rising 20 EMA has climbed to roughly 48,350. And 48,300 was itself minor resistance a week earlier. Three anchors converge in a 48,300–48,350 pocket. On the third down-day, price wicks to 48,290 and closes back at 48,480 — a bullish pin bar rejecting the zone. That is the pullback trigger, and it is a *better* trade than Phase 1 because your stop can go just under 48,290, a far tighter risk than a fresh breakout stop.

**Phase 3 — the breakout.** Bank Nifty now consolidates for five sessions in a tight 49,400–49,800 rectangle, coiling under the round-number 49,800 ceiling. The range height is 400 points. On day six, an event day, it closes at 50,050 — a decisive break above 49,800 on volume 40% above the 20-day average. Measured move: 49,800 + 400 = 50,200, with a stretch target at the next round number, 50,500. This is the classic base-breakout: weeks of coiling energy released in one thrust as trapped shorts near 49,800 cover.

Reading the three phases together teaches the core lesson: the *same* trend offered three distinct, mechanically different entries, each with its own risk profile, and a disciplined trader would have taken whichever one matched his style and appeared with the cleanest trigger.

## Trading it — entries, stops, targets, management

Let us make each phase concrete with rupees, using a ₹5 lakh account risking 0.75% (₹3,750) per trade. Bank Nifty is traded via futures/options; here we reason in index points, where each Bank Nifty futures lot is 15 units (1 point = ₹15 per lot).

**Trend-continuation (Phase 1).**
- Entry: 48,230 on the break of 48,220.
- Stop: 47,880, just below the 47,900 swing low. Risk = 350 points.
- Position size: ₹3,750 ÷ (350 × 15) = 0.71 → round down to *no full lot at this stop*, so either widen to a spread structure or skip. This is a crucial realism check: index point-risk of 350 is *too wide* for one lot on a small account. The professional response is either to use a debit call spread (defined, cheaper risk) or to wait for a tighter setup — which is exactly why Phase 2 is preferred.
- Target: trail under each new higher-low; first objective the 49,000 prior high.

**Pullback buy (Phase 2).**
- Entry: 48,500 on the close above the pin bar.
- Stop: 48,270, below the 48,290 wick. Risk = 230 points × ₹15 = ₹3,450 per lot ≈ your ₹3,750 budget. One lot is now clean.
- Target 1: retest of 49,000 (500 points, ~2.2R). Target 2: measured continuation to 49,800 (5.6R) if the breakout in Phase 3 fires. Book half at T1, trail the rest under the rising 20 EMA.
- Management: once price clears 49,000, move stop to breakeven. This converts a good trade into a free option on the breakout.

**Breakout (Phase 3).**
- Entry option A (breakout): 50,050 on the decisive close. Stop below the range at 49,750 — a 300-point risk.
- Entry option B (retest, preferred): wait. If price pulls back to 49,850 and holds with a bullish candle, enter there with a stop at 49,650 — only 200 points risk, tighter, and the fakeout is filtered.
- Target: 50,200 measured move (book half), stretch 50,500.
- Scenario management: if after the breakout close price falls straight back *inside* the range below 49,800 within one to two sessions, that is a failed breakout — exit immediately, do not "give it room." Failed breakouts often reverse violently as the breakout longs get trapped.

Across all three, the non-negotiable rule is that the *stop is placed before entry and never widened.* You may trail it only in the direction of profit.

## Confluence — stacking the odds

A setup taken in isolation is a coin flip weighted slightly in your favour. Confluence is how you turn a 52% edge into a 60% edge by only firing when multiple independent signals agree.

**Trend + momentum.** Take the pullback buy only when RSI(14) on the trading timeframe holds above ~40 and turns up from the pullback low — a genuine uptrend rarely lets RSI collapse below 40 on a dip. If RSI breaks 40 and keeps falling, the "pullback" may be a reversal in disguise.

**Level + volume.** For the breakout, demand that volume on the breakout bar exceed the 20-bar average by a meaningful margin. A breakout on falling volume is the market's way of telling you few participants believe it.

**Multi-timeframe.** Never take a long pullback on the 15-minute chart if the daily is rolling over. Align the trade timeframe with the higher timeframe trend; the higher timeframe is the tide, your setup is the wave.

**Option-chain / OI confluence (index and F&O stocks).** This is where Indian traders have a genuine edge the West under-uses. For the Bank Nifty breakout above 49,800:
- Check the option chain. If 50,000 CE has heavy open interest that has *started to unwind* (falling OI with rising price), call writers are covering — a bullish confirmation of the breakout.
- If the Put-Call Ratio is rising and puts are being written at 49,500 and 49,800, put writers are defending those strikes as support — confluence with your pullback zone.
- A "max pain" that has migrated higher over the week corroborates upward drift.
- Conversely, if 50,000 CE OI is *building* as price approaches, heavy call writing is capping the move — a warning that your breakout may fail at the strike. Professionals routinely fade breakouts into a wall of fresh call writing.

The synthesis: price gives you the *level*, structure gives you the *trigger*, and the option chain tells you *who is defending or abandoning* that level. When all three point the same way, you size up.

## Pitfalls & false signals

**The false breakout (the "bull trap").** The single most expensive error. Price pokes above resistance, sucks in breakout buyers, then reverses. Filters: demand a *closing* break not an intraday poke; demand above-average volume; prefer the retest entry; and watch for fresh call writing at the strike. In Indian markets, first 15-minute gaps frequently reverse — be wary of breakouts that happen entirely inside the opening candle.

**Buying the pullback that is actually a reversal.** A pullback assumes the trend resumes. But if the pullback breaks the prior higher-low structure, or slices through the 50 EMA on heavy volume, it is no longer a pullback — it is a trend change. The structural rule: a pullback that makes a *lower low* below the last swing low has forfeited its "pullback" status. Do not average down into it.

**Chasing extended trend entries.** Getting on board a trend is good; getting on board *after five straight up-days far from the mean* is buying euphoria. The continuation entry works best off shallow pauses near the moving average, not after a parabolic stretch. If price is more than roughly 2–3 ATRs above the 20 EMA, the risk-reward on a fresh long is poor — wait for the pullback.

**Ignoring regime.** All three setups assume a trending or breakout-friendly environment. In a choppy, range-bound tape (low ADX, price oscillating around a flat moving average), breakouts fail repeatedly and pullbacks have no trend to resume. Pros check ADX or simply eyeball whether the moving averages are sloped or flat before deploying trend setups. Wrong setup, right execution still loses.

**Over-tight stops on the breakout.** Placing the stop just one tick under the level invites a stop-hunt: the market wicks below, triggers you, then rallies. Give the stop room *below the structure*, and size down to keep rupee-risk constant, rather than choking the stop to fit a lot.

## Interview-ready summary

"A setup is a rule-defined edge, not a pattern. I run three trend-side families. The **continuation entry** joins an established uptrend on a shallow pause near a rising moving average — lowest drama, but often too wide a stop for a small account. The **pullback buy** is my bread-and-butter: I wait for price to retrace to a confluence of the 38–61.8% Fib zone, a rising 20 or 50 EMA, and prior structure, then enter on a reversal candle with a tight stop below the pullback low — best risk-reward of the three. The **breakout** enters on a decisive *closing* break of a consolidation on above-average volume, with a measured-move target equal to the range height; I usually prefer the *retest* entry to filter fakeouts. Across all three I fix the stop before entry, size to a constant rupee-risk of well under 1%, and confirm with the option chain — call unwinding above the breakout is bullish, fresh call writing at the strike is a red flag. Every setup wins under 60% of the time; it makes money because I engineer the winners bigger than the losers and never widen a stop."
