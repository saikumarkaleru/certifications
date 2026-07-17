# VWAP & Anchored VWAP

## What it is & why it works

VWAP stands for Volume-Weighted Average Price. It answers a single, deceptively powerful question: *what is the average price at which every share (or contract) traded today, weighted by how much size changed hands at each price?* A simple moving average treats the 9:20 candle and the 2:45 candle as equal. VWAP does not. It gives a ₹2,300-crore turnover 15-minute burst far more influence over the line than a sleepy ₹40-crore drift. That single design choice is why VWAP is the most-watched intraday reference line on Indian desks — from the prop trader scalping Bank Nifty to the mutual-fund dealer who is literally *benchmarked* against it.

That last point is the deepest reason VWAP "works." It is not a pattern someone drew; it is an execution benchmark with real money enforcing it. When a large domestic institution (an LIC, an SBI MF, an HDFC MF) is told to accumulate 8 lakh shares of Reliance over the session, the dealer's performance is graded against the day's VWAP. Beat VWAP on a buy (fill below it) and the dealer looks good; fill above it and they underperformed. So institutions *lean into* VWAP: they buy when price dips below it and slow down when price runs above it. This creates a self-reinforcing gravitational pull. Price that stretches far from VWAP tends to get pulled back, because the biggest, least price-sensitive, most persistent buyers in the market are mechanically programmed to buy the dip toward their benchmark. That is genuine, structural order flow — not folklore.

The behavioural read is therefore about *who is winning*. If price is above VWAP and holding, the average buyer of the day is in profit and sellers are trapped or absent — bullish control. Below VWAP, the average buyer is underwater; rallies into VWAP become supply as break-even sellers unload. VWAP is, in one line, the intraday fair-value line and the dividing line between bulls' and bears' control.

Anchored VWAP (AVWAP) takes the same maths and frees it from the "start of day" restriction. Instead of resetting at 9:15, you *anchor* the calculation to any event you choose — a swing high, a swing low, an earnings gap, a budget-day candle, the day the RBI cut rates. From that anchor forward, AVWAP tells you the true average price paid by everyone who transacted *since that event*. That makes it a swing and positional tool, not just an intraday one, and it turns "where is fair value since the news that matters" into a plottable, tradeable line.

## The mechanics

The formula is straightforward. For each trade or each intraday bar you take the typical price and weight it by volume:

VWAP = Σ(Typical Price × Volume) / Σ(Volume)

where Typical Price = (High + Low + Close) / 3 for that bar. The Σ runs cumulatively from the anchor point. On a standard intraday VWAP the anchor is the first bar of the session (9:15 for NSE cash and index; note the derivatives session and pre-open at 9:00–9:15 are usually excluded so most platforms start the sum at 9:15).

A concrete micro-example. Suppose Bank Nifty's first three 5-minute bars are:

| Bar | Typical Price (₹) | Volume (contracts) | TP × Vol | Cumulative TP×Vol | Cumulative Vol | VWAP |
|-----|-------------------|--------------------|---------:|------------------:|---------------:|-----:|
| 1 | 48,000 | 1,000 | 48,000,000 | 48,000,000 | 1,000 | 48,000 |
| 2 | 48,050 | 3,000 | 144,150,000 | 192,150,000 | 4,000 | 48,037.5 |
| 3 | 48,100 | 1,000 | 48,100,000 | 240,250,000 | 5,000 | 48,050 |

Notice bar 2 carried three times the volume, so VWAP (48,037.5) sits much closer to bar 2's price than a simple average of the three typical prices (48,050 would be the simple mean — here they coincidentally converge by bar 3, but intraday the volume weighting routinely pulls VWAP away from the simple mean by 15–40 points on Bank Nifty).

**Key mechanical properties to internalise:**

- **It is cumulative and path-dependent.** Early-session volume anchors the line. By 2:30 pm, VWAP is "heavy" — a huge cumulative denominator means a late spike barely moves it. That is why VWAP is responsive in the first hour and sticky in the last hour.
- **It resets each day** (standard VWAP). Yesterday's VWAP is irrelevant to today's line unless you deliberately use AVWAP.
- **VWAP bands / standard-deviation bands.** Most platforms plot VWAP with ±1, ±2, ±3 standard-deviation bands (volume-weighted variance of price around VWAP). +1σ and +2σ act like an intraday overbought envelope; −1σ/−2σ like oversold. On Bank Nifty a typical calm day sees ±1σ roughly ±120–180 points from VWAP; on an event day the bands flare wide. Bands are where mean-reversion scalps live.

**Settings that matter:**

| Setting | Recommended | Why |
|---|---|---|
| Source | HLC/3 (typical price) | Standard; some use HL/2 or Close — keep it consistent |
| Session VWAP anchor | 09:15 | Excludes pre-open auction noise |
| Bands | ±1σ and ±2σ on | Defines reversion zones |
| Timeframe to plot on | Any intraday (1/3/5/15-min) | VWAP value is identical across intraday TFs on the same day — it depends on the session, not the candle size |

That last row surprises people: VWAP for a given moment is the *same number* whether you view a 1-minute or 15-minute chart, because it sums the same trades. The candles look different; the blue line does not move.

**Anchored VWAP mechanics** are identical except the sum starts at your chosen bar and never resets at session close — it keeps accumulating across days, weeks, months. Anchor it to the intraday low of a capitulation day and it runs forward carrying every trade since that bottom. On TradingView it is the "Anchored VWAP" tool (drop it on any candle); on Chartink you approximate it with custom logic; most Indian retail platforms (Zerodha Kite, Fyers, Dhan) now expose both session VWAP and a manual anchored-VWAP tool.

## Reading it — a worked India example

Take a realistic Bank Nifty intraday session. Bank Nifty opens at 48,120, roughly flat to the previous close of 48,150. Walk it phase by phase.

**Phase 1 — Opening drive and VWAP formation (9:15–9:45).** The first fifteen minutes are volatile; price whips between 48,050 and 48,220 on heavy volume. VWAP forms around 48,110. By 9:45 price is trading at 48,180, sitting *above* VWAP, and each pullback toward 48,120–48,130 (just above the VWAP line) is bought. Read: the average buyer is in profit; dips to VWAP are being defended. Bullish control established.

**Phase 2 — The VWAP retest that holds (10:15).** A wave of selling drags Bank Nifty down to 48,125, kissing VWAP (now 48,140). It touches, wicks, and bounces. This is the highest-probability long of the morning: price returned to fair value in an uptrending, above-VWAP tape and buyers stepped in exactly where the benchmark buyers are programmed to. Price rallies to 48,300 — roughly the +1σ band — where it stalls. The +1σ tag warns the move is intraday-stretched.

**Phase 3 — The break below (12:30).** Around noon a soft news headline hits; price slices through VWAP (now 48,190) with a wide-range down candle on rising volume and does *not* immediately reclaim. Now the tape has flipped: the average buyer is underwater. The very same VWAP line that was support becomes resistance. Price rallies back to 48,190 at 1:10 pm — a "return to VWAP from below" — and gets sold hard, rolling over to 48,020 (−1σ). This VWAP-rejection short is the mirror image of the Phase-2 long.

**Phase 4 — The heavy, sticky close (2:30–3:15).** By afternoon VWAP is around 48,110 and barely moves even as price oscillates 48,020–48,160, because the cumulative volume is now enormous. Price closes at 48,060, *below* VWAP. The daily read: sellers won the second half; a close below VWAP after being above it all morning is a distribution day and biases the next session's open cautiously.

Now overlay **Anchored VWAP** on the swing picture. Suppose three weeks ago Bank Nifty made a capitulation low of 46,800 on an RBI-policy day with the highest volume of the quarter. Anchor a VWAP there. Today that AVWAP reads 47,650. Every intraday dip that has held above 47,650 over the last three weeks confirms buyers-since-the-bottom are in control. The day Bank Nifty finally closes below 47,650 on volume, the entire post-capitulation advance is in question — the average participant since the low is now losing money, and the path of least resistance turns down.

## Trading it

VWAP gives you three canonical setups. In every one, VWAP defines the *reference*; you still need a trigger, a stop, and a target.

**Setup A — VWAP reclaim / trend-day pullback (the bread-and-butter long).**
- *Context:* price is above a rising VWAP; you want to buy the dip, not chase.
- *Entry trigger:* price pulls back to VWAP and prints a reversal candle (bullish engulfing / pin-bar) that holds the line — e.g., Bank Nifty dips to 48,125 against VWAP 48,140 and closes the 5-min candle back at 48,175.
- *Stop:* just below the VWAP touch and below the swing, say 48,080 (a clean close below VWAP invalidates the thesis). Risk ≈ 95 points.
- *Target:* +1σ band first (48,300, ~1.7R), then previous day's high or the round number. Trail the rest under higher swing lows or under VWAP itself.

**Setup B — VWAP rejection short (mirror image).** Price below a falling VWAP rallies into the line, tags it, and rejects with a bearish candle. Short on the rejection, stop just above VWAP / above the rally high, target −1σ then session low. In Phase 3 above, short at 48,180, stop 48,230, target 48,020 — roughly 3R.

**Setup C — Band mean-reversion scalp (range days).** On a non-trending, choppy day where price is oscillating around a flat VWAP, fade the extremes: sell tags of +2σ back toward VWAP, buy tags of −2σ back toward VWAP. Tight stops just beyond the band. This is a scalper's tool and *only* works when VWAP is flat and price is respecting bands — the moment VWAP tilts and price rides a band, mean-reversion stops working and you must flip to trend logic (see Pitfalls).

**Anchored-VWAP swing setup.** Anchor to a major swing low. Enter longs on positional pullbacks to the AVWAP when it is rising and price has been holding above it; stop on a *daily close* below the AVWAP. Anchor to a major swing high for the short side. Because AVWAP is a moving, dynamic level, your stop and your invalidation are the same clean line — elegant for position trades. Example: anchor to Nifty's June swing low of 24,500; AVWAP now at 24,900; Nifty pulls back to 24,930 and holds — a positional long with stop on a daily close under 24,900, targeting the prior high at 25,400.

**Management across all setups:** book partial at the first band/target to lock the win, move stop to break-even once price clears +1σ (long) so a VWAP re-loss can't turn a winner into a loser, and respect the clock — VWAP mean-reversion edges decay into the last 30 minutes when the line goes sticky and moves become directional into the close.

## Confluence

VWAP is at its most powerful when it *stacks* with independent evidence. A VWAP touch alone is a coin-flip-plus; a VWAP touch that coincides with three other things is a high-conviction trade.

- **VWAP + prior-day levels / round numbers.** When session VWAP sits right at the previous day's close, or at a round number (Bank Nifty 48,000, Nifty 24,500), the reaction is sharper because two independent reference crowds are defending the same price.
- **VWAP + market profile POC / Value Area.** If today's VWAP coincides with yesterday's Point of Control (the volume-heaviest price), you have two volume-derived fair-value estimates agreeing — a magnet and a strong reversion target (see the Volume Profile chapter).
- **VWAP + option-chain / OI.** This is the India-specific edge. Suppose Bank Nifty VWAP is 48,140 and the heaviest Put OI (support) sits at the 48,000 strike while the heaviest Call OI (resistance) is at 48,500. A VWAP-reclaim long above 48,140 now has a clear runway to 48,500 with option sellers defending the downside at 48,000. When VWAP, Put-writing support and a demand zone align, the long is A+. Conversely, price rejecting VWAP from below *and* sitting under a wall of Call OI (fresh Call writing = resistance being built) is a clean short. Watch OI *change*, not just absolute OI: rising Call OI as price fails at VWAP confirms sellers are pressing.
- **VWAP + volume.** A VWAP reclaim on a volume spike is trustworthy; a VWAP reclaim on thin volume is a trap waiting to fade. Institutions move price on VWAP with size — insist on seeing the size.
- **Anchored VWAP + earnings/events.** Anchor AVWAP to an earnings-gap candle for a stock. If price holds above the earnings-day AVWAP, the market is endorsing the results; a loss of that AVWAP says the post-results buyers have given up. Pair with delivery % (see the delivery chapter) — high delivery holding above the earnings AVWAP is genuine accumulation.

## Pitfalls & false signals

**The single biggest error: fading a trend day.** On a strong trend day (budget day, big-result day, gap-and-go), Bank Nifty can open, ride the +1σ/+2σ band all day, and *never* return to VWAP. Traders who mechanically "buy the dip to VWAP" or "sell the +2σ tag" get run over repeatedly. The filter: mean-reversion to VWAP only works when VWAP is roughly *flat* and price is *oscillating*. When VWAP is steeply sloped and price is riding a band, you are on a trend day — you must trade *with* the trend (buy shallow pullbacks that never reach VWAP) and stop fading the bands. Judge the slope of VWAP and the character of the day in the first hour before choosing your playbook.

**VWAP is a lagging, path-dependent line late in the day.** By 2:45 pm the line is anchored by six hours of volume and is almost inert. A "VWAP reclaim" at 3:05 pm means far less than one at 10:00 am because the line no longer reflects the current balance of power. Weight morning VWAP signals more heavily.

**Chop around VWAP eats accounts.** On a low-conviction, low-volume day price crisscrosses VWAP a dozen times, stopping out both longs and shorts. If price is knifing back and forth through VWAP with no follow-through, that *is* the signal — stand aside. VWAP works when one side is in control; it whipsaws when neither is.

**Illiquid stocks distort VWAP.** In thin small-caps a single large print can jerk VWAP unnaturally, and the "institutions defend VWAP" logic barely applies because institutions aren't there. VWAP is most reliable on Nifty, Bank Nifty, Fin Nifty and liquid large-caps (Reliance, HDFC Bank, Infosys) — exactly where the benchmark pressure is real.

**Anchor-point cherry-picking.** With AVWAP you can always find *some* anchor whose line "explains" the chart in hindsight. Discipline yourself to anchor only to *objectively significant* events — the highest-volume day, a clear swing high/low, a scheduled event (budget, RBI, earnings) — not to a random candle that happens to fit. An AVWAP is only as meaningful as the event it is anchored to.

**Gap days reset the picture.** A large overnight gap means the session VWAP starts far from yesterday's close; early VWAP values are noisy until enough volume accumulates. Give the line 20–30 minutes to stabilise before trusting reversion signals.

## Interview-ready summary

"VWAP is the volume-weighted average price since the session open — the intraday fair-value line and the benchmark that institutional dealers are graded against, which is why price gravitates to it: the biggest buyers are mechanically programmed to buy dips toward it. Above a rising VWAP the average buyer is in profit and dips get bought; below a falling VWAP, rallies into the line get sold. I trade three things — reclaim pullbacks in the trend direction, rejections at VWAP, and band mean-reversion only on flat, range-bound days — always with a defined stop on the far side of the line. Anchored VWAP applies the same maths from any chosen event — a swing low, an earnings gap, an RBI day — so it becomes a swing and positional tool: hold above the anchor and buyers-since-the-event are in control; lose it on a daily close and the move is in doubt. The India edge is stacking VWAP with option-chain OI walls and delivery data — a VWAP reclaim toward a Call-OI ceiling with Put-writing support beneath it is a far higher-probability trade than VWAP alone. The main trap is fading a trend day: when VWAP is steeply sloped and price rides a band, you trade with it, not against it."
