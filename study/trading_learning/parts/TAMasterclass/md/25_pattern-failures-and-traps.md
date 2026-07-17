# Pattern Failures, Fakeouts & Traps

## What it is & why it works

Every chart pattern you have learned in this book — the flag, the head-and-shoulders, the double top, the ascending triangle, the opening-range breakout — has a published "textbook" success story. What the textbook rarely tells you is that the *failure* of a pattern is often a higher-probability, cleaner-edged trade than the pattern working as advertised. A pattern failure is not noise to be lamented; it is information. When price sets up a widely-watched formation, gathers a crowd of traders who all place their stops and entries at the same obvious level, and then *refuses* to do what that crowd expects — the resulting stampede as they are forced to reverse is one of the most reliable, repeatable moves in the market.

This chapter is about the dark half of pattern trading: fakeouts, bull traps, bear traps, failed breakouts, false breakdowns, and the deliberate (or emergent) hunting of stop-loss clusters. Understanding these is what separates a retail chart-reader who gets repeatedly chopped up from a professional who *anticipates* the trap and positions on the correct side of it.

The behaviour behind traps is simple crowd psychology plus liquidity mechanics. Markets move to where the orders are. Below an obvious support, and above an obvious resistance, sit dense clusters of stop-loss orders. A stop to *sell* (a long's protective stop) is a resting sell order; a stop to *buy* (a short's stop) is a resting buy order. Large participants — institutions filling big positions, and yes sometimes proprietary desks — need liquidity to transact size without slippage. The most efficient place to find a pool of resting orders is exactly at these obvious levels. So price is repeatedly drawn *to* and *through* the levels every amateur has marked, triggers the stops, fills the big order against that flood of liquidity, and then reverses. The retail trader who "did everything right" — bought the breakout, put the stop below the base — is left holding a loss precisely *because* the setup was so obvious.

A fakeout works, in other words, for the same reason a real breakout works: both are about where the orders sit. The difference is direction and intent. Your job is not to memorise more patterns; it is to learn to read *whether a break is being absorbed or accepted*, and to have a plan for both outcomes.

Three families of failure dominate Indian intraday and positional trading:

1. **The bull trap** — price breaks above a resistance/pattern high, sucks in breakout buyers, then collapses back inside the range. Longs are trapped; their stops fuel the fall.
2. **The bear trap** — price breaks below an obvious support/pattern low, panics longs into selling and lures shorts, then snaps back up. Shorts are trapped; their buy-stops fuel the rally.
3. **The failed pattern / throwback-that-fails** — a legitimate-looking H&S, triangle, or double top that completes and then invalidates, producing a violent move in the *opposite* direction (the "from failed moves come fast moves" principle articulated by Wyckoff and popularised by Adam Grimes).

## The mechanics

A pattern is only "failed" relative to a rule, so you must define failure precisely *before* the trade. Vague failure ("it kind of didn't work") produces vague, late exits. Here is the taxonomy with mechanical definitions.

| Trap / failure | Textbook expectation | Failure trigger (precise) | The resulting trade |
|---|---|---|---|
| Bull trap | Break above resistance R → continuation up | Close back **below R** within 1–3 bars of the breakout | Short, target mid-range / opposite boundary |
| Bear trap | Break below support S → continuation down | Close back **above S** within 1–3 bars of the breakdown | Long, target mid-range / opposite boundary |
| Failed H&S (top) | Neckline break → measured fall | Price re-crosses neckline and takes out the **right shoulder high** | Long; often fast because bears are trapped |
| Failed double top | Break below the valley → downmove | Reclaim of the valley low and the nearer peak | Long |
| Failed triangle break | Break of trendline → measured move | Close back inside the triangle beyond the apex zone | Fade toward opposite side |
| Failed flag | Break in trend direction → continuation | Break the *far* side of the flag against the prior trend | Reversal, exit any continuation longs |
| ORB fakeout | Break of opening range → trend day | Return inside opening range after poking out | Fade back to other end of the range |

The single most useful mechanical filter across all of these is the **close vs. the wick**. Amateurs react to price *touching* a level; professionals wait for price to *close* beyond it on the relevant timeframe. A 15-minute candle that spikes ₹40 above Nifty resistance and closes ₹5 below it is not a breakout — it is a rejection wick, and often the first evidence of a bull trap. So rule one of trap avoidance: **judge breakouts on closing basis, not on the touch.**

Second mechanical tool: **volume and the character of the break.**

- A *genuine* breakout typically shows expanding volume on the break and, crucially, follow-through: the next one or two candles hold above the level and extend.
- A *fakeout* often shows either (a) a volume spike that immediately fails to follow through, or (b) a suspiciously *quiet* break — price drifts through a level on thin volume, nobody defends it, and then a large seller appears. On NSE you can watch this on the tape and on the 1-/5-minute volume histogram in TradingView.

Third tool, unique to derivatives-heavy Indian markets: the **option chain and OI.** Because Nifty, Bank Nifty and Fin Nifty are so liquid, the option chain tells you where the pain is. A move that breaks a technical level but is *fighting* against the highest OI strike (a wall of call writers above, or put writers below) is a prime fakeout candidate — the writers have every incentive, and the capital, to defend that strike into expiry. We will use this in the confluence section.

Fourth: **time.** Traps resolve fast. Wyckoff's principle — *from failed moves come fast moves* — is literally about elapsed bars. If a breakout is real, price should not spend much time back below the breakout level. A useful heuristic: a valid intraday breakout on the 5-minute chart should not close back inside the range for more than one to two candles; a positional daily breakout should not close back below the level for more than two to three sessions. When it lingers, suspect a trap and tighten or exit.

**The "2B" rule (Victor Sperandeo).** One of the cleanest mechanical trap setups. In an uptrend, price makes a new high above the prior swing high, fails to follow through, and trades back below that prior high — that is a 2B top, a bull trap, and a short trigger. Mirror image for a 2B bottom (bear trap): a marginal new low that fails and reclaims the prior low is a long. The *marginal, brief* penetration is the tell.

## Reading it — a worked Bank Nifty example

Let me walk a composite but realistic Bank Nifty bull trap of the kind you see around expiry, phase by phase, with levels and rupees.

**Setup.** It is a Wednesday, weekly expiry day. Bank Nifty has spent three sessions coiling between 48,200 (support, an obvious round-ish level and the prior week's high) and 48,600 (resistance, a triple-tested ceiling). Chartists across every Telegram group have drawn the same horizontal line at 48,600 and are watching for the "breakout." The 48,600 call strike carries the highest call OI on the chain — heavy call writing — meaning option writers have sold a wall there and profit if BNF stays below.

**Phase 1 — the bait (9:45–10:30 a.m.).** BNF grinds up and, at 10:20, a 5-minute candle pokes to 48,640, printing a fresh high above 48,600. Breakout scanners fire on Chartink. Retail longs pile in at 48,610–48,640, placing stops just under the level at ~48,570. The move *looks* clean: green candle, a little volume. On the option chain, though, something else is happening — 48,600 call OI is *rising* even as price nudges above it. Writers are *adding*, not covering. That is the divergence a pro notices: price up, but the smart-money option flow is leaning short.

**Phase 2 — the failure (10:30–10:50).** The breakout candle *closes at 48,585* — back below 48,600. That is the trigger: a poke above, a close below, within one bar. The wick above the level with a close below it is the fingerprint of a bull trap. Follow-through has failed. The 48,700 calls barely moved; the market never believed the break.

**Phase 3 — the trap springs (10:50–12:30).** As BNF ticks back to 48,570, the breakout longs' stops trigger — a cascade of *sell* orders. Their forced selling drives price down through 48,500, which triggers a second layer of stops from earlier intraday longs. Call writers at 48,600, now comfortably in profit, are unbothered; put writers below step back. BNF slides to 48,300, then tags 48,200 support by lunch. A trader who was long the "breakout" at 48,620 with a stop at 48,570 lost 50 points (₹15 × 50 = ₹750 per lot on the BNF lot of 15 — using the current contract size). A trader who *recognised the trap* and shorted the close-back-below at 48,585, stop above the fakeout high at 48,660 (75-point risk), rode it to 48,300 for a +285-point / roughly +₹4,275 per lot win — and had the option to press to 48,220.

**Phase 4 — resolution.** BNF holds 48,200, and the day settles into an expiry pin between the big OI strikes. The lesson is compact: the *same level*, 48,600, produced a small loss for the crowd that bought the touch and a clean gain for the trader who waited for the close and read the OI. Nothing about the chart pattern changed — only the discipline of confirmation did.

## Trading it — entries, stops, targets, management

There are two distinct ways to trade traps, and you must know which you are doing.

**A. Defensive — avoiding being the trapped one.**
This is risk management, and it is the more important of the two for most traders.

- **Entry discipline:** never buy the *touch* of a breakout. Require a close beyond the level on your execution timeframe (5-min intraday, daily for positional). Optionally require a *retest* that holds — enter on the pullback to the broken level once it acts as support, not on the initial thrust. You will miss the occasional runaway breakout; you will avoid the large majority of fakeouts.
- **Stop placement:** do *not* place your stop at the single most obvious spot (a tick under the base low, or a round number). That is where the cluster is and where price is drawn. Place it a sensible ATR-based distance beyond the noise — e.g. 0.5–1.0× the 14-period ATR beyond the structural level — so a routine liquidity sweep does not take you out before the real move.
- **Scaling:** take partial size on the break, add on confirmed follow-through/retest. This caps your loss if it's a trap.

**B. Offensive — trading the trap itself.**
Here you *want* the pattern to fail.

- **Entry trigger:** the confirmed re-cross. For a bull trap: a 5-min close back below the broken resistance (or the 2B trigger — trade back below the prior swing high). For a failed H&S: reclaim of the right-shoulder high. Enter on the close that confirms, or on the first weak retest of the level from the wrong side.
- **Stop:** just beyond the fakeout extreme — above the trap high (bull trap short) or below the trap low (bear trap long). This is a *tight, well-defined* stop, which is precisely why failed-pattern trades have such attractive reward:risk. If price reclaims the fakeout extreme, the trap thesis is wrong — get out.
- **Target:** the first target is the *opposite* side of the range or pattern. A bull-trap short from the top of a range targets the range low; a failed H&S long targets the head or beyond. Because trapped traders are being forced out, these moves are fast — Wyckoff's fast move from a failed move. Take partials at the mid-range, trail the rest.

**Scenario 1 — trap confirms and runs:** you short the failed BNF breakout at 48,585, stop 48,660 (75 pts). It falls to 48,300. Book half at 48,450 (mid-range, +135), trail the rest with a 5-min swing-high stop; exit balance at 48,320. Net well over 2R.

**Scenario 2 — trap fails (the fakeout of the fakeout):** you short at 48,585, but BNF reclaims 48,600 and closes 48,640. Your stop at 48,660 is doing its job — you're out for a defined ~75-pt loss, and now the *original* breakout may be real. Markets do produce double-fakeouts; your tight stop is what makes surviving them cheap.

**Scenario 3 — you were the trapped long:** you bought 48,620, it closed back at 48,585. Do not "hope." The close-back-below is *itself* your exit signal — flip your bias. The best trap traders are simply traders who, on being proven wrong, reverse fast rather than averaging down.

## Confluence — stacking filters so traps become high-probability trades

Traps are far more tradeable when several independent tells line up. The idea is that any one filter can lie, but three rarely lie together.

**1. Option-chain / OI confluence (the India edge).** This is your most powerful filter on Nifty/BNF/Fin Nifty. A breakout *into* a wall of call OI, with that call OI *rising* on the break, is a fakeout tell — writers are defending and adding, betting price stays below. Conversely a genuine breakout usually shows call writers *covering* (OI falling, price rising) — a short-covering unwind that fuels continuation. Mirror logic for breakdowns and put OI. Practically: pull the NSE option chain (or a Sensibull/Opstra view) and ask, *is the level I'm breaking a high-OI strike, and is that OI building or unwinding as we break?* Building OI against you = suspect a trap.

**2. Max-pain and expiry gravity.** On expiry day especially, price is pulled toward the max-pain / highest-combined-OI strike. A "breakout" away from max pain in the last hours of expiry is fighting the writers' gravitational pull and frequently traps. Fade with the pin, not against it.

**3. Volume and delivery.** A breakout on a stock (say Reliance or HDFC Bank) with poor volume and low delivery percentage is weak-handed and trap-prone. Genuine institutional accumulation shows in volume *and* the % deliverable quantity.

**4. Higher-timeframe context.** A 5-minute "breakout" against the daily trend is fighting the tide and is a classic fakeout. Trade breakouts *with* the higher-timeframe trend; fade breakouts *against* it. The trap trade is highest-probability when a lower-timeframe pattern fails *in the direction of* the higher-timeframe trend — the crowd got faked into fighting the primary trend, and the snap-back is the trend resuming.

**5. Market internals / breadth.** For index trades, check the advance-decline and whether the move is broad or driven by one or two heavyweights. A Nifty "breakout" powered only by Reliance while the rest of the index is red is narrow and prone to failure.

**6. VWAP.** Intraday, VWAP is where institutional flow anchors. A breakout that immediately loses VWAP is suspect; a fakeout that gets rejected at VWAP from below confirms the trap. VWAP reclaim/loss is an excellent secondary trigger stacked on the pattern-failure trigger.

When OI (building against the break) + close-back-inside + loss of VWAP + counter-higher-timeframe-trend all align, you have a near-textbook trap short. That is a setup worth pressing.

## Pitfalls & false signals

Trading failures is powerful precisely because it is contrarian — and contrarian trading has its own ways of hurting you. Guard against these:

- **The fakeout of the fakeout (double whipsaw).** Ranges near expiry, or in low-volatility drift, can whipsaw *both* ways — faking a breakout, faking a breakdown, chopping everyone. If you find you've been stopped on both a trap short *and* the reversal, the honest read is "this is a chop range, stand aside." Do not force trades in a two-sided liquidity grind. The single biggest mistake is over-trading a range that is designed to hurt directional traders.
- **Calling failure too early.** A brief wick above resistance that closes back *just* below on the *first* candle is a trap tell — but a level being *retested* after a genuine break is normal, healthy backing-and-filling, not a failure. Distinguish a *throwback* (retest that holds, then continues) from a *failure* (reclaim of the range, then reversal). The difference is whether the level holds on close. Don't short every retest.
- **Fighting a truly strong trend.** In a powerful trend, "obvious" breakouts *keep working*, and fading them because they "look too obvious" is a fast way to lose. Trap-trading is highest-probability at *range boundaries* and against *counter-trend* breaks — not against strong, well-supported trend continuation. Respect momentum.
- **Over-reading intent.** You do not need a conspiracy of "operators hunting your stop." Whether the sweep is deliberate manipulation or just the emergent result of where liquidity sits, your response is identical: confirm on close, size for the stop being swept, trade the reversal. Skip the story; trade the level.
- **Stops that are too tight.** Ironically, placing your stop *at* the obvious level to "keep risk small" makes you the liquidity. Use ATR-based buffers so a routine sweep doesn't remove you before the move you correctly anticipated.
- **News and events override structure.** A trap read assumes normal order-flow mechanics. On an RBI policy day, a surprise global cue, a large block, or a stock-specific result, price can break a level and *keep going* on genuine new information. Don't fade a break that is being driven by a real fundamental catalyst — that isn't a trap, it's repricing.
- **Ignoring the option-chain warning on your own trade.** If you took a breakout long and see the resisting call OI *building* against you while VWAP is lost, that is the market telling you you're the trapped one. The discipline is to act on your own contrary evidence, not to explain it away.

## Interview-ready summary

*"A pattern failure is often a better trade than the pattern itself, because markets move to where the orders are — and the densest clusters of stop-loss orders sit right beyond the levels everyone can see. A bull trap is a break above resistance that closes back below and triggers trapped longs' stops on the way down; a bear trap is the mirror image below support. I confirm a break on a *closing* basis, not the touch, and I judge its quality by follow-through, volume, VWAP, and — this is the India-specific edge — the option chain: a breakout *into rising* call OI is writers defending a strike and a prime fakeout tell, whereas a breakout with call OI *unwinding* is genuine short-covering fuel. When a widely-watched pattern fails, I trade the reversal: entry on the confirmed re-cross, a tight stop just beyond the fakeout extreme, and a target at the opposite side of the range — Wyckoff's 'from failed moves come fast moves.' The key risk is chop and double-whipsaw ranges near expiry, so I only press trap trades at range boundaries or against counter-trend breaks, size for the level being swept, and stand aside when both sides are getting faked."*
