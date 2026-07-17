# Delivery %, FII/DII Data & Participant Positioning

## What it is & why it works

Everything else in technical analysis reads *price* — the footprint left behind by buyers and sellers. This chapter reads the *flow and intent* behind the footprint. Delivery percentage, FII/DII cash-flow data, and F&O participant positioning (the NSE's "Participant-wise Open Interest" report) are India-specific datasets that let you ask a question price alone cannot answer: *who is doing the buying and selling, and do they mean it?* A ₹200 up-move on huge volume where most of it settled as intraday churn is a very different animal from the same move where most shares were actually taken into demat accounts by long-term holders. Price is identical; conviction is not.

**Delivery percentage** is the share of a stock's traded volume that resulted in actual delivery — shares moved from one demat account to another — rather than being bought and sold within the same day (intraday, squared off, no delivery). It is reported by NSE/BSE at end of day. High delivery % means a large fraction of the day's buyers *intend to hold* — they paid full value and took the stock home. Low delivery % means the volume was dominated by intraday traders and jobbers who netted out by 3:30 pm. The logic is simple and powerful: **delivery-based buying is stickier, more informed, and less likely to reverse than intraday froth.** A breakout backed by rising delivery % is far more trustworthy than one on high volume but low delivery, which is often a traders' pump destined to fade.

**FII/DII data** is the daily net cash-market buying/selling by Foreign Institutional (now FPI) and Domestic Institutional Investors — mutual funds, insurers (LIC), pension money. These two are the whales of the Indian market and they are structurally different animals. FIIs are large, momentum-and-macro driven, sensitive to the rupee, US rates, and global risk appetite — when they sell, they sell hard and in size, and they can drive multi-week trends. DIIs — flush with relentless monthly SIP inflows — are the great domestic counterweight, habitually *absorbing* FII selling by buying the dips. The daily tug-of-war between "FII selling ₹3,500 crore, DII buying ₹3,200 crore" is one of the most-watched sentiment gauges on Indian desks. Sustained one-sided flow is a genuine, tradeable trend driver; the *balance* between them explains why India often holds up when global markets wobble.

**Participant positioning** goes one layer deeper into F&O: the NSE publishes daily open-interest by participant category — FIIs, DIIs, Pro (proprietary desks), and Clients (retail) — split into index futures, stock futures, index calls and index puts. The prize metric is the **FII long-short ratio in index futures**: are the smart-money foreigners net long or net short Nifty/Bank Nifty futures, and how extreme is it? This tells you how the most influential derivatives players are *positioned*, which is often a better tell than what they say.

Why does reading flow work? Because technicals show you the *what*; flow shows you the *conviction and the fuel*. A chart breakout with FIIs turning net buyers, DIIs supporting, and delivery % surging is a move with real money behind it. The same breakout with FIIs dumping futures and delivery collapsing is a bull trap. Flow is the fundamental-cum-behavioural confirmation layer under the price.

## The mechanics

**Delivery % — the numbers.**

Delivery % = (Delivery Quantity / Total Traded Quantity) × 100

Published daily by NSE (security-wise delivery data) and available on Chartink, Trendlyne, and broker terminals. Typical reference bands (they vary by stock — always compare to the stock's *own* history, not an absolute):

| Delivery % | Typical read |
|---|---|
| < 30% | Trader-dominated, speculative, intraday froth |
| 30–50% | Mixed — normal for a liquid large-cap |
| 50–70% | Investor interest, accumulation-tilted |
| > 70% | Strong conviction holding / possible accumulation or distribution |

The gold is **relative delivery**: today's delivery % versus the stock's 20/50-day average delivery %, and delivery *quantity* (not just percentage) versus average. A day where price rises, volume is above average, *and* delivery % jumps well above its own norm is the signature of institutional accumulation. High delivery % on a *down* day near support = value buyers absorbing; high delivery % on an *up* day into resistance can be *distribution* (informed sellers delivering stock to weak hands) — so delivery must always be read *with price and location*.

**FII/DII data — where and what.** NSE publishes the "FII/FPI & DII trading activity" (cash segment) daily after market close; also available on Moneycontrol, NSDL (FPI flows), and broker dashboards. You read three things: (1) net figure today (₹ crore, buy or sell), (2) the *trend* — is it day 1 of selling or day 12?, and (3) the FII-vs-DII *balance*. Note the cash-market number is the classic figure; FIIs' *derivatives* positioning (below) often diverges from and leads their cash flow.

**Participant OI — the FII index-futures long-short ratio.** From NSE's daily "Participant wise Open Interest" file:

FII Net Long-Short Ratio (index futures) = FII Long Index-Futures Contracts / FII Short Index-Futures Contracts

Read as a ratio or as net contracts. A ratio well above 1 (and rising) = FIIs net long, bullish positioning; well below 1 = net short, bearish. Extremes matter most:

| FII index-fut long % (of their index-fut OI) | Read |
|---|---|
| > 65–70% net long | Aggressively bullish; but crowded — reversal risk if news turns |
| ~50% balanced | Neutral / hedged |
| < 30–35% net long (heavily short) | Aggressively bearish; but crowded short — squeeze risk on good news |

The *change* day-over-day is the signal: FIIs adding longs into a rally confirms it; FIIs adding shorts while price rises is a bearish divergence warning of distribution. Combine with their index-options positioning (heavy Put buying vs Call buying) for the fuller hedged picture.

**Rollover data** (near expiry) is a cousin metric: high rollover % of positions to the next series with rising OI signals conviction carried forward; poor rollovers signal position unwinding.

## Reading it — a worked India example

**Case A — a delivery-confirmed breakout in a large-cap.** Suppose Tata Motors has been basing between ₹960 and ₹1,000 for a month. Its 50-day average delivery % is ~42%. Today it breaks ₹1,000 on a wide bullish candle, volume 1.8× the 20-day average, and delivery % prints **61%** — a sharp jump above its 42% norm, with delivery *quantity* also well above average. Read the layers: price broke resistance (technical), on expanded volume (participation), and the majority of that volume was *taken into demat* (conviction). This is not an intraday pump; real holders are accumulating on the breakout. High conviction to trade the breakout long and to *hold* it, not scalp it. Contrast: had the same ₹1,000 break come on 1.8× volume but delivery of just **24%** (well below norm), the move would read as trader froth — a likely bull trap to fade or at least not to chase.

**Case B — distribution hiding in a rally.** Reliance grinds up from ₹2,850 to ₹2,980 over five sessions. Price looks strong. But delivery % has been *falling* each day (55% → 48% → 41% → 35%) even as price rises, and on the ₹2,980 day, volume spikes with delivery at just 30% while the candle prints a long upper wick into resistance. The tell: rising price on *deteriorating* delivery and a rejection wick = informed sellers distributing stock to late momentum buyers. Flow contradicts price. This is a caution-to-exit / potential-short setup, invisible to price-only analysis.

**Case C — the FII/DII macro read.** Nifty has fallen from 25,000 to 24,300 over two weeks. The FII/DII table shows FIIs net sellers for eleven straight sessions (cumulative ~₹42,000 crore sold) while DIIs bought ~₹38,000 crore — the classic tug-of-war, DIIs cushioning the fall. Two forward scenarios:
- *Capitulation-to-turn:* on day 12 FIIs sell a huge ₹6,000 crore (a selling *climax*), Nifty spikes down to 24,150 and *closes green* — and the next day FII cash selling shrinks to ₹800 crore while their index-futures long-short ratio ticks up from 28% to 34% long. Flow is turning. The heavy DII absorption plus fading FII selling plus improving FII futures positioning = the bottoming process; align longs with the price reversal.
- *Trend continues:* FIIs keep selling ₹3,000–4,000 crore daily *and* their index-futures short position keeps growing while price makes lower lows — one-sided, conviction selling. Do not bottom-fish; respect the downtrend until flow balances.

**Case D — positioning extreme as a contrarian warning.** Before an event (say an RBI policy or election result), FIIs' index-futures net-long shoots to **72%** — everyone's on the same side, max bullish. Price is euphoric. This crowded positioning is itself a risk flag: with almost everyone already long, there is little marginal buying left and any disappointment triggers a violent unwind. The positioning data warns you to tighten stops and be sceptical of chasing, precisely when the tape feels safest.

## Trading it

This data is primarily a **confirmation and conviction filter** layered onto a price setup — you rarely trade it in isolation, and you never trade it *against* clear price structure. Used well, it upgrades position size and holding conviction, and flags traps.

**Setup 1 — Delivery-confirmed swing breakout (long).**
- *Trigger:* price closes above a well-defined resistance/base on above-average volume *and* delivery % meaningfully above the stock's own average (e.g., Tata Motors > ₹1,000, delivery 61% vs 42% norm).
- *Stop:* below the breakout level / base low (e.g., ₹975).
- *Target:* measured move of the base height, trailed under swing lows. Because delivery signals holders, you hold for the swing rather than scalping.
- *Size:* upsize versus a delivery-weak breakout — the flow says the move has legs.

**Setup 2 — Distribution short / exit.** Rising price + falling delivery % + rejection candle at resistance (Case B). Trigger a short (or exit longs) on the first bearish price confirmation — a break of the prior day's low — with stop above the distribution high, target the prior support/POC. Flow gives you the *early warning*; price gives you the *trigger*.

**Setup 3 — FII/DII flow-aligned trend trade.** Trade index/large-cap swings *in the direction of sustained institutional flow*. When FIIs are consistent net buyers (cash + growing futures longs) and DIIs support, favour longs and buy pullbacks. When FIIs are relentless sellers with growing futures shorts, favour shorts and sell rallies. Enter on price triggers (VWAP reclaim, support/resistance breaks); let the flow trend keep you on the right side and size you appropriately.

**Setup 4 — Contrarian fade at positioning extremes.** When FII index-futures long-short hits a crowded extreme (>70% long or <30% long) into an event, *don't chase*; tighten stops on existing positions and be ready to trade the *unwind* on any adverse news, since crowded positioning fuels violent reversals. This is a risk-management and mean-reversion overlay, taken only with a price trigger (a reversal candle, a failed breakout), never on positioning alone.

**Management across all:** flow data is *slow* (daily, end-of-day) — it sets the bias and the size, price sets the entry and the stop. Never override a hard price stop because "FIIs are still buying." Use flow to decide *whether and how big*, use price to decide *when and where*.

## Confluence

- **Delivery + volume + breakout structure.** The core triad: a breakout is graded A only when volume *and* delivery *and* structure agree. Volume without delivery is froth; delivery without a clean level is aimless.
- **Delivery + VWAP / Anchored VWAP.** A stock holding above its earnings-gap Anchored VWAP *with* elevated delivery % is genuine post-results accumulation — two independent conviction reads agreeing. Loss of the AVWAP with collapsing delivery confirms the buyers have quit.
- **FII futures positioning + option-chain OI (the compound India edge).** Read participant OI *with* the option chain. FIIs net long index futures *and* aggressively writing Puts (Put OI building = support) = strongly bullish, aligned positioning; expect dips bought. FIIs net short futures *and* buying Puts / writing Calls (Call OI building overhead) = aligned bearish; sell rallies into the Call wall. When the smart-money futures stance and the options structure point the same way, conviction is highest; when they diverge (net long futures but heavy Put buying), someone is hedging and you trade smaller.
- **FII/DII cash flow + index price trend + market breadth.** Sustained FII buying + rising advance-decline breadth + price uptrend = a healthy, broad, fuelled rally. FII selling absorbed by DIIs but with *narrowing* breadth warns the index is being held up by a few heavyweights.
- **Delivery + Volume Profile.** Heavy delivery accumulating at a Value-Area Low / POC support confirms real buyers are defending the auction's fair-value shelf.

## Pitfalls & false signals

**Delivery % is a lagging, end-of-day number.** You get it after the close, so it confirms and contextualises rather than triggers. Do not expect it to time entries — pair it with intraday price action for the trigger.

**High delivery is ambiguous without price and location.** High delivery on an up-day into resistance can be *distribution*, not accumulation — informed sellers delivering to weak hands. High delivery on a down-day at support is absorption. The *same* delivery number means opposite things depending on where price is and which way it moved. Never read delivery in isolation from price and level.

**Absolute thresholds mislead — always use the stock's own baseline.** Some stocks (heavy investor names) habitually run 60%+ delivery; some F&O-heavy traders' stocks habitually run 20%. "61% delivery" is bullish for a 42%-norm stock and unremarkable for an 80%-norm stock. Compare to the security's own moving average, not a universal cutoff.

**FII/DII daily numbers are noisy; the trend is the signal.** One day's ₹2,000-crore FII sell means little — it can be a single fund rebalancing, an index-inclusion adjustment, or block deals. Read the multi-day trend and the FII-DII balance, not a single print. Also note: large *block/bulk deals* and index rebalancing can distort a day's figure without reflecting genuine directional conviction.

**Cash flow vs derivatives divergence.** FIIs can be net *sellers in cash* while net *long in index futures* (or vice versa) — hedging, arbitrage, and their cash and F&O books tell different stories. Reading only the cash number misses the positioning picture. Always cross-check participant OI.

**Crowded positioning cuts both ways.** An extreme FII net-long is bullish confirmation *and* a contrarian reversal risk — the very crowdedness that confirms the trend also fuels the unwind. Don't treat an extreme as a simple "keep buying" signal; treat it as "trend intact but fragile, manage risk."

**Data-source lags and revisions.** Provisional FII/DII figures released at ~5–6 pm are sometimes revised; NSDL FPI data and NSE provisional cash data can differ. Use it directionally, not to three decimal places.

**Retail (Client) positioning is usually the wrong-way crowd.** In participant OI, the "Client" (retail) category is frequently on the losing side of extremes — heavy retail longs into a top, heavy retail shorts into a bottom. Fading crowded retail *with* smart-money (FII/Pro) confirmation is an edge; but "retail is long so short it" *alone*, without price and FII confirmation, is a lazy trap.

## Interview-ready summary

"Price shows what happened; flow data shows who did it and whether they meant it. Delivery percentage is the share of volume actually taken into demat rather than squared off intraday — a breakout on high volume *and* high delivery, read against the stock's own average, signals real holders accumulating, while high volume with low delivery is trader froth likely to fade; and high delivery into resistance on an up-day can actually be distribution, so I always read it with price and location. FII/DII data is the daily cash flow of the market's whales — FIIs are momentum-and-macro, global-risk-sensitive money; DIIs are the SIP-fuelled domestic counterweight that absorbs FII selling — and it's the multi-day *trend* and the FII-DII balance, not one print, that matters. Participant open-interest adds the FIIs' index-futures long-short ratio: how the smart money is actually positioned in derivatives, with crowded extremes above ~70% long or below ~30% acting as both trend confirmation and contrarian reversal risk. I use all of it as a conviction and risk filter layered on a price setup — flow decides whether and how big, price decides when and where — and the highest-conviction India trades are where price structure, delivery, FII positioning and option-chain OI all point the same way."
