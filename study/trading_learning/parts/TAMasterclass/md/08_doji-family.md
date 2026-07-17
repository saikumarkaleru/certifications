# The Doji Family (Standard, Gravestone, Dragonfly, Long-Legged)

## What it is & why it works

A **doji** is a candle where the open and close are essentially equal, so the real body collapses to a thin horizontal line — a cross, a plus sign, a "t" or an inverted "t". After a session of trading, price has returned almost exactly to where it began. The doji is therefore the purest visual signature of **indecision**: the auction was fought, ground was taken in one or both directions (the wicks), yet neither buyers nor sellers could claim net progress. Balance.

Why does that matter? Because *trends are powered by imbalance*. An uptrend exists only while buyers keep paying higher prices with conviction; a downtrend only while sellers keep hitting lower bids. A doji is the moment that imbalance stalls. Appearing in the middle of a quiet range, a doji is noise — the market was already balanced, so of course the close matched the open. But a doji appearing *after an extended, one-directional move*, especially at a key level, is a genuine early warning: the fuel of the trend — persistent aggression by one side — has, for one period, run out. The crowd that was confidently pushing price has paused, disagreed, and gone home flat.

The doji "works" for the same behavioural reason all candlestick signals work: it is a footprint of crowd psychology. In a mature Nifty rally, every green day recruits more late buyers convinced the move continues. A doji at the top means that on this day, for the first time, the sellers matched the buyers punch for punch. That equilibrium frequently precedes a reversal or at least a pause, because the marginal buyer has been exhausted and there is no one left to pay up. The doji does not *cause* the reversal; it *reveals* the exhaustion that causes it.

The doji is not one shape but a **family**, and the family members carry different messages depending on where the wicks fall. The location of the long shadow tells you which side probed and got rejected:

- **Standard / neutral doji** — small, balanced wicks both sides: pure indecision.
- **Long-legged doji** — long wicks on both sides: violent indecision, a wide battle with no winner.
- **Gravestone doji** — long upper wick, no lower wick, open/close at the low: bearish rejection of higher prices.
- **Dragonfly doji** — long lower wick, no upper wick, open/close at the high: bullish rejection of lower prices.

Reading the family correctly is a core skill for an Indian derivatives analyst, because dojis cluster at exactly the inflection points — index tops, support tests, expiry-day balance — where the biggest, cleanest trades live.

## The mechanics

**Definition.** A candle is a doji when |Close − Open| is a very small fraction of the total range (High − Low). There is no universal threshold, but a practical rule: **body ≤ ~5–10% of the total range**. If body/range is under ~0.05 it is a textbook doji; up to ~0.1 many traders still call it a doji (sometimes a "near-doji" or "spinning-top-doji"). The key is that the body is negligible relative to the wicks.

**The four family members — construction table**

| Type | Open vs Close | Upper wick | Lower wick | Shape | Message |
|---|---|---|---|---|---|
| Standard doji | ≈ equal, mid-range | Small | Small | Thin plus (+) | Indecision / balance |
| Long-legged doji | ≈ equal, mid-range | Long | Long | Tall cross | High-volatility indecision |
| Gravestone doji | ≈ equal, at the **low** | Long | ~None | Inverted "T" (⊤) | Bearish rejection of highs |
| Dragonfly doji | ≈ equal, at the **high** | ~None | Long | "T" (⊥) | Bullish rejection of lows |

**How to read each shape's story**

- **Standard doji:** price wandered a little each way and closed flat. Weakest signal of the family — meaningful only with strong location/context.
- **Long-legged doji:** price ran up sharply *and* down sharply within the period, then closed dead centre. This is a wide, emotional tug-of-war — often marks a volatility climax or the exact pivot of a trend, because both sides threw everything and neither won.
- **Gravestone doji:** price opened at the low, rallied hard (the long upper wick), and then was driven all the way back to close at the low. Buyers seized ground and *lost all of it*. This is bearish, particularly at the top of an uptrend or at resistance — it is essentially a doji-strength shooting star.
- **Dragonfly doji:** price opened at the high, sold off hard (the long lower wick), and buyers reclaimed everything to close back at the high. Sellers seized ground and *lost all of it*. Bullish, especially at the bottom of a downtrend or at support — a doji-strength hammer.

**The "4-price doji"** is the extreme case where open = high = low = close (a single horizontal line, no wicks). It occurs in illiquid stocks or when a period has almost no trading — informationally empty, ignore it.

**Confirmation is mandatory.** A doji by itself signals only a *pause*, not a *turn*. The tradable signal is the doji **plus the next candle's follow-through**. A gravestone doji at Nifty resistance becomes actionable only when the next candle closes red, below the doji's low. Until then, it is a warning, not a trigger.

## Reading it — a worked India example

Consider a **Bank Nifty daily** sequence at a major top — the kind of setup that recurs at index highs.

**Phase 1 — the trend.** Bank Nifty has run from 50,800 to 52,400 over eleven sessions, a strong uptrend, mostly green candles, buyers firmly in charge. Momentum, however, is fading: the last two green bodies are smaller than the ones before, an early sign of tiring demand. Price is now approaching a prior swing high / supply zone near 52,500.

**Phase 2 — the gravestone doji.** The next session Bank Nifty opens at 52,380, surges to a high of 52,610 (a fresh high, tagging the supply zone), then reverses hard all afternoon to close at 52,395 — essentially back at the open. The candle:
- Open ≈ 52,380, Close ≈ 52,395 → body ≈ 15 points (negligible)
- High 52,610 → upper wick ≈ 215–230 points (long)
- Low 52,375 → lower wick ≈ 5 points (none)
- Body/range ≈ 15/235 ≈ 0.06 → a **gravestone doji**

The story is vivid: bulls made a new high, tried to run the trend, and were *completely* rejected — every rupee of the intraday rally was given back, close pinned at the low. After an extended run, into a supply zone, this is a textbook exhaustion warning. A research analyst writes in the evening note: *"Bank Nifty printed a gravestone doji at 52,610 resistance today — buyers rejected. Bias shifts to neutral/cautious; watch for confirmation below 52,375."*

**Phase 3 — confirmation.** Next day Bank Nifty opens at 52,340 and closes at 52,090 on a solid red body, decisively below the doji's 52,375 low. The pause has become a turn — sellers have follow-through. The two-candle combination (gravestone doji + red confirmation at resistance) is now a completed top signal.

**Phase 4 — the move.** Over the following five sessions Bank Nifty slides to 51,300 — roughly 1,300 points off the 52,610 high. A trader who shorted on the confirmation break of 52,375 caught the bulk of it. On 1 Bank Nifty lot (15 qty), a move of ~1,000 points captured is 1,000 × 15 = **₹15,000 per lot**. The doji did not predict the destination, but it flagged the exhaustion at the exact top, days before the line chart would have looked concerning.

**A dragonfly counter-example.** Flip the setup: Nifty falls from 24,600 to 23,850 over a week, and at a demand zone around 23,800 prints a **dragonfly doji** — opens 24,010, sells to a low of 23,780, then buyers reclaim everything to close at 24,020. Long lower wick, no upper wick, body at the top. Sellers pushed to new lows and lost all their ground. Confirmation comes the next day with a green close above the doji's high (~24,040), and Nifty bases and rallies. Same logic, mirror image: rejection of *lower* prices at *support* after a *downtrend*.

## Trading it

**Entry trigger.** Trade the *confirmation*, not the doji. 
- Bearish (gravestone/long-legged at resistance): enter short on a break **below the doji's low**. 
- Bullish (dragonfly/long-legged at support): enter long on a break **above the doji's high**.
On the Bank Nifty gravestone above, the short trigger is a break below 52,375.

**Stop-loss.** Beyond the doji's rejection wick plus a buffer. For the short: stop above the 52,610 high, say 52,660. Risk = 52,660 − 52,375 = 285 points. The wick already defines where the losing side quit; a move past it invalidates the read. This is a genuine advantage of doji trading — the long wick gives a *natural, tight* stop relative to the potential move.

**Target / measured move.** Use structure first: the prior swing low or demand zone (here ~51,300, and below that 50,800). A minimum 2R target off 285 points risk is 52,375 − 570 = 51,805 — comfortably reached. Because dojis mark reversals, they often precede moves several times the risk, giving excellent reward-to-risk.

**Scenario A — clean reversal.** Short triggers at 52,370 on the break. Price trends to 51,350; you exit near the demand zone for ~1,020 points ≈ 3.6R. On 1 lot: 1,020 × 15 = **₹15,300 gross** against ~₹4,275 risk. This is the doji-at-the-top ideal.

**Scenario B — failed doji / stop-out.** Short triggers at 52,370, price dribbles to 52,300, then a strong buy program lifts it back through 52,610 to stop you at 52,660. Loss ≈ 290 × 15 = **₹4,350**. Dojis fail when the trend is stronger than the pause — hence confirmation and stops are non-negotiable.

**Scenario C — expiry-day / range doji.** A doji forms mid-range on a quiet Thursday expiry with no trend behind it. Correct action: **no trade**. This doji is just balance in an already balanced market — pure noise. Filtering these out is as important as taking the good ones.

**Management.** After entry, watch the *next* candle. If price closes back inside the doji's range (above 52,375 for the short), the reversal is failing and discretionary traders exit early. If it follows through, trail the stop behind each new lower swing high.

## Confluence

A doji is a high-value signal *only* with context; alone it is among the weakest candles. Stack these:

- **Location.** The doji must sit at a meaningful level — resistance/supply, support/demand, a round number (Nifty 25,000; Bank Nifty 52,000/52,500), a key moving average (20/50/200 EMA), or a prior swing extreme. A gravestone at supply and a dragonfly at demand are the money setups.
- **Trend extension.** Reversal dojis are strongest *after an extended move* — the longer and more one-sided the run into the doji, the more exhaustion it represents. A doji three candles into a fresh trend is far less meaningful than one on the eleventh green day.
- **Volume.** A long-legged or gravestone doji on a **volume spike** signals real institutional battle and distribution; a doji on thin volume is often just a dull session. High volume + wide wicks = climax.
- **Option-chain / OI confluence (F&O).** For Indian index traders this is decisive. A **gravestone doji forming exactly at the strike with the heaviest call OI** (the call wall / structural ceiling) is a premium short setup — the candle's rejection aligns with where call writers are defending. If intraday **OI data shows fresh call writing** building at that strike as price rejects, smart money is confirming your read in real time. Mirror for the bull side: a **dragonfly doji at the max-put-OI strike** (put wall / floor) is a premium long, backed by put writers defending support. Also note **IV**: dojis at extremes often coincide with a volatility inflection — a long-legged doji after a spike frequently marks the point where IV starts to cool.
- **Multi-timeframe.** A daily doji at resistance is stronger if the weekly is also stretched. A doji on the higher timeframe overrides several candles on the lower one.

The model: a doji is a *question the market is asking* ("is the trend over?"). Confluence — level + extension + volume + OI wall — is the market answering "yes."

## Pitfalls & false signals

- **Trading dojis mid-range.** The single biggest error. In a sideways market dojis appear constantly and mean nothing — the market is already balanced. Demand a level and a preceding trend, or pass.
- **Skipping confirmation.** A doji is a *pause*, not a *reversal*. Traders who short every gravestone the instant it forms get run over when the trend simply resumes. Always wait for the break of the doji's high/low.
- **Over-loose "doji" definitions.** Calling every small-bodied candle a doji dilutes the signal. Hold the discipline: body ≤ ~5–10% of range. A spinning top (small body, but clearly present) is not the same as a doji and carries a weaker message.
- **Ignoring gaps (India-specific).** Because Indian indices and stocks gap on overnight cues (GIFT Nifty, US close), a daily candle's open can be dislocated from the prior close, and a "doji" body may reflect a gap-and-fill rather than genuine intraday equilibrium. Read gap dojis with care.
- **The 4-price doji trap.** In illiquid small-caps a doji may simply mean *almost nothing traded*. That is not indecision between two engaged sides; it is absence of participation. Trade dojis only in liquid names — Nifty/Bank Nifty and F&O stocks — where the flat close reflects a real, contested auction.
- **Counter-trend over-eagerness.** Even a perfect gravestone at resistance fails a meaningful fraction of the time in a powerful bull trend, because strong trends absorb pauses. Pros size these reversal attempts modestly, insist on confirmation, and keep stops tight behind the wick — accepting that the doji improves the odds without ever guaranteeing the turn.

## Interview-ready summary

*"A doji is a candle where open and close are essentially equal, so the body vanishes to a line — the market's clearest picture of indecision, buyers and sellers in balance. On its own it means only a *pause*; its power comes from **where** it appears. After an extended trend and at a key level, a doji flags exhaustion because the imbalance that drives trends has stalled. I read the family by the wicks: a **gravestone** — long upper wick, close at the low — is rejection of higher prices, bearish at resistance; a **dragonfly** — long lower wick, close at the high — is rejection of lower prices, bullish at support; a **long-legged** doji with wide wicks both sides is a volatility climax, often the exact pivot; a **standard** doji is weak indecision. I never trade the doji alone — I wait for the next candle to confirm by closing beyond the doji's range, I put my stop just past the rejection wick (which gives a naturally tight risk), and I target the next structural level for a 2R-plus payoff. In Indian F&O I stack option-chain confluence: a gravestone at the max-call-OI strike or a dragonfly at the max-put-OI strike, with fresh option writing confirming, is a high-probability reversal because the candle and the option writers agree on where price should turn. The doji asks 'is the trend over?' — confluence answers it."*
