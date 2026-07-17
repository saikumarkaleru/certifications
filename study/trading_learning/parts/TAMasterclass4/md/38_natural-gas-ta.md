# Natural Gas TA

Natural Gas is the widow-maker of the commodity world, and every Indian trader who has held an MCX Natural Gas position through a Thursday-night US inventory report knows exactly why the nickname stuck. It is the most volatile liquid contract most retail traders will ever touch, more violent tick-for-tick than Crude, Silver, or even Bank Nifty options. This chapter is a playbook: what drives the instrument, how its levels behave, which technical setups actually survive its volatility, a full worked trade, and the risk discipline without which Natural Gas will simply take your account apart one gap at a time.

## The instrument's character & drivers

On the MCX, Natural Gas trades as a monthly contract with a lot size of 1,250 mmBtu. That number matters enormously. The tick is Re 0.10 per mmBtu, so one tick is worth Rs 125 per lot. A move of Rs 10 in the price — which Natural Gas can do in a single session, sometimes in an hour — is Rs 12,500 per lot. During the 2021-2022 energy crisis and again in the cold snaps of 2024-2025, the contract printed daily ranges of Rs 25-40, meaning a single lot could swing Rs 30,000-50,000 intraday. Retail traders routinely carry 2-5 lots. Do the arithmetic and you understand why margin calls and blown accounts cluster around this symbol.

The MCX contract is a rupee-denominated mirror of the US Henry Hub futures (NG on NYMEX), converted through the USDINR rate. So the MCX Natural Gas trader is really trading three things at once: the US Henry Hub price, the rupee, and the basis/roll between them. Ninety-plus percent of the move comes from Henry Hub. This is the single most important fact for an Indian technical trader — you must watch the NYMEX NG chart on TradingView (symbol NG1! for continuous front-month) as your leading indicator, because MCX is a follower. When NYMEX gaps on a Thursday storage number released at 8:00 PM IST (10:00 AM Eastern), MCX gaps with it seconds later.

The fundamental drivers you must respect even as a chartist:

- **Weather.** This is the dominant driver. Natural Gas is a heating fuel (winter) and, increasingly, a cooling fuel via power generation for air-conditioning (summer). A forecast for a polar vortex or a heat dome sends prices vertical. Weather models update multiple times daily; the GFS and European (ECMWF) model runs at roughly 6:00 AM and 6:00 PM IST can move the market before any Indian trader is even watching.
- **EIA Weekly Storage Report.** Released Thursday 8:00 PM IST. This is the scheduled bomb. It reports the change in US working gas in underground storage. A number far from consensus produces an instant Rs 5-15 gap. Never hold a naked position across this print unless that IS your trade and it is sized for it.
- **Season.** Late-autumn "cold trade" (Oct-Jan) and mid-summer "cooling trade" (Jun-Aug) are the high-volatility windows. Shoulder seasons (spring, autumn) can chop sideways for weeks.
- **US production and LNG exports.** Structural, slower-moving, but they set the multi-month trend. Record US production caps rallies; surging LNG export demand (Freeport, Sabine Pass coming back online) puts a floor under selloffs.

Because Henry Hub can trade from $1.60 to $9.00 within a couple of years, MCX Natural Gas has traded from roughly Rs 130 to Rs 780 in living memory. This is not a range-bound instrument. It trends hard and reverts hard.

## Key levels & behaviour

Natural Gas respects technicals — but only round-number and swing levels, and only until a weather or storage catalyst overrides them. Here is how its levels behave in practice:

**Round numbers are magnets and battlegrounds.** On MCX, the Rs 10 and Rs 25 increments (200, 210, 225, 250, 275, 300) act as psychological shelves. On Henry Hub, the $0.25 and $0.50 increments ($2.50, $2.75, $3.00, $3.50) are the reference. The $3.00 Henry Hub level in particular is a decade-long pivot: below it, gas is "cheap" and producers curtail; above it, demand destruction and coal-switching begin. Watch it.

**Overnight gaps define the day.** Because the bulk of information (weather runs, US session, storage) arrives when India sleeps or in the evening, MCX Natural Gas opens at 9:00 AM with a gap versus the previous close about 60% of the time. The first job every morning is to mark the NYMEX close-to-now move and expect MCX to have already priced it in at open. Fading the open gap without confirmation is a classic beginner's grave.

**Volatility clusters.** Natural Gas has strong volatility autocorrelation: a big-range day is very likely to be followed by another big-range day. When ATR expands, keep it expanded in your mind for several sessions. Conversely, a series of narrow-range doji days in the shoulder season warns that a coil is building for an explosive break.

**Trends are persistent, pullbacks are violent.** In a genuine cold-trade uptrend, Natural Gas can rise 40-60% over three to five weeks. But the pullbacks inside that trend routinely retrace 38-50% in one or two sessions and shake out every weak long before resuming. This is the behavioural signature that makes the widow-maker: the trend is real, but the noise around it is large enough to stop out anyone using a Crude-sized stop.

A practical level table for reading the MCX chart:

| Level type | How it behaves in Natural Gas | Trading implication |
|---|---|---|
| Prior day high/low | Frequently swept then reversed on open | Wait for reclaim, don't chase break |
| Round Rs 10 shelf | Pauses and consolidations form here | Good place for limit entries/targets |
| Weekly VWAP / anchored VWAP from swing | Trend gas respects it as support | Buy pullbacks to it in uptrend |
| Prior swing high after a base | Break with volume = trend continuation | Breakout setup, but confirm on NYMEX |
| Gap from storage day | Often acts as support/resistance for weeks | Mark it and trade around it |

## Best setups

Given the character above, only a handful of technical setups earn their keep in Natural Gas. Reckless pattern-trading gets punished. These are the survivors.

**1. The trend-pullback to anchored VWAP (the bread-and-butter).** In an established cold-trade or cooling-trade uptrend, anchor a VWAP on TradingView to the swing low that launched the move. Natural Gas in a healthy trend pulls back to this line and bounces. Entry is on a bullish reversal candle (hammer, engulfing) tagging the VWAP with the NYMEX chart confirming the same structure. Stop goes below the pullback swing low. This is the highest-probability recurring setup because it aligns with the fundamental trend while buying fear.

**2. The storage-report fade (advanced, sized small).** The EIA number at 8:00 PM often produces an over-reaction spike that reverses within 30-60 minutes as the market digests the print against the whisper number. The setup: wait for the initial spike to exhaust into a prior level, look for a rejection candle on the 5-minute chart, and fade back toward the pre-report price. This is only for experienced traders with tight risk — the spike can extend, not reverse, and you are trading directly into the news.

**3. The shoulder-season range fade.** In April-May and September-October, gas often chops in a Rs 15-25 range for weeks. Buy the bottom rail, sell the top rail, with stops just outside. Bollinger Bands and RSI(2) work well here because mean-reversion dominates. The moment the range breaks on a weather shift, you flip to trend mode and stop fading.

**4. The volatility-contraction breakout.** A series of inside days / narrowing Bollinger Bands in Natural Gas is a loaded spring. When the ATR compresses to multi-week lows, position for an explosive break in the direction of the eventual first strong close outside the coil. This is where the biggest one-directional multi-day moves begin.

**5. Momentum divergence at extremes.** After a parabolic weather-driven spike, a bearish RSI/price divergence into a round number is one of the more reliable reversal tells in this contract, because weather-driven spikes are fundamentally unstable — once the forecast normalizes, the fuel for the rally vanishes and the reversion is fast.

## A worked example

Set the scene in a realistic 2025 winter. NYMEX Henry Hub had based around $2.90-$3.00 through late November as production ran near record highs. In the first week of December, the European weather model flipped decisively cold for the third consecutive run, projecting a sustained Arctic outbreak across the US Midwest and Northeast for mid-December. Henry Hub broke $3.05 resistance and ran to $3.45 over four sessions. MCX Natural Gas, mirroring this, moved from roughly Rs 258 to Rs 302.

A disciplined MCX trader is not chasing this vertical move. Instead they anchor a VWAP on the Rs 258 swing low. On the fifth session, a warmer model run overnight triggers a sharp intraday pullback: MCX drops from Rs 302 toward Rs 284, tagging the anchored VWAP which now sits around Rs 283. On the 15-minute chart, a bullish engulfing candle forms right on the VWAP at 11:40 AM. Crucially, the trader checks NYMEX NG1! — Henry Hub has held its equivalent $3.28 support and printed the same reversal. The underlying cold trend is intact; this was model noise, not a trend change.

The trade:
- **Entry:** Rs 285 on the close of the engulfing candle, 1 lot.
- **Stop:** Rs 277, below the pullback low and the VWAP. Risk = Rs 8 = Rs 10,000 per lot.
- **Target 1:** Rs 300 (round number, prior high), booking half.
- **Target 2:** Rs 315, trailing the rest under the rising VWAP.

Over the next two sessions the cold forecast held, Henry Hub pushed to $3.55, and MCX ran to Rs 314 before the trader's trailing stop under the VWAP took them out at Rs 308 on a subsequent warm-model pullback. Result: roughly +Rs 15 on the first half (Rs 18,750) and +Rs 23 on the second half (Rs 28,750) against Rs 10,000 risk — a blended reward near 4.7R.

Now the honest counter-scenario. Suppose instead that after entry, the overnight GFS run had flipped warm and stayed warm. Henry Hub gaps down $0.20 on the 9:00 AM open equivalent, MCX opens at Rs 274 — through the Rs 277 stop. The trader is filled not at Rs 277 but at Rs 273 on the gap, a Rs 12 loss (Rs 15,000), 1.5R worse than planned. This gap-through-stop is the defining risk of Natural Gas, and it is why position sizing must assume your stop can slip by 30-50%.

## Risk notes

Natural Gas risk management is not optional dressing — it is the entire game. The setups above have positive expectancy only if the losers are contained, and Natural Gas specializes in uncontained losers.

**Size for the gap, not the stop.** Because roughly 60% of days gap and storage days can gap Rs 10-15, assume your worst-case loss is 1.5-2x your intended stop distance. If your account can only tolerate a Rs 10,000 loss, do not size a position whose planned stop is Rs 10,000 — size it for Rs 6,000-7,000 planned so the gap-slipped reality still lands near your limit.

**Never hold naked size across the EIA storage report** unless the report is your explicit, pre-sized trade. This single rule prevents more account destruction than any other in this contract.

**Cap total exposure.** A common professional guideline: risk no more than 1% of capital per Natural Gas trade and no more than 2% aggregate if holding multiple energy positions (Crude and Natural Gas are correlated enough that they are not true diversifiers during an energy shock).

**Respect the roll and expiry.** MCX Natural Gas expires monthly. Volume and liquidity thin near expiry and the contract can decouple from a fresh front-month. Roll to the active contract with the rest of the market; do not trade a dying contract on technicals.

**Trade the leading chart.** Always keep NYMEX NG1! open. If MCX and NYMEX disagree, NYMEX is right and MCX is lagging or distorted by a stale USDINR print. Your edge as a technician improves dramatically when you read the source, not the mirror.

**Volatility-scale your stops.** Use an ATR-based stop (say 1.5x the 14-period ATR) rather than a fixed rupee stop. When ATR is Rs 12, a Rs 6 stop is noise-tight and will be shredded. The stop must be wide enough to survive normal noise and the position small enough that the wide stop is still affordable — that trade-off, not a magic entry, is what separates survivors from the widow-maker's victims.

The final honest word: most retail traders lose money in Natural Gas, and they lose it faster here than anywhere else on the MCX. The volatility that attracts them is precisely what ruins them when they size for the average day and get the tail day. If you cannot state your maximum loss on a position to the rupee before you enter, you are not trading Natural Gas — you are donating to it.
