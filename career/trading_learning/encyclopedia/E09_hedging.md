# Strategy Group 9: Hedging & Protective Strategies

This family is not about making money on options — it is about keeping money you already have. Every structure here sits on top of a long position (a Nifty future, an ETF, a cash-equity or mutual-fund book) and reshapes its downside: a put buys a floor like an insurance policy with a deductible, a collar funds that floor by selling away some upside, and spread-based hedges trade full protection for a cheaper premium and a gap-risk caveat. The honest through-line: hedges cost money and usually expire worthless — that drag is the premium you pay for sleeping at night, exactly like home insurance you are glad not to claim.

A note on the numbers below: the `net_cost` figure quoted from the data includes the roughly 24000-point index outlay (about 18 lakh per Nifty lot of 75). The number that actually matters for a hedge is the option premium — the cost of the cover — so that is described separately in words throughout.

## 129. Protective Put (OTM)
*Bullish, insured · Long vega · net debit*

**The idea (intuition).** You own the index and you buy an out-of-the-money put below it. Think of it as fire insurance with a deductible: you absorb the first slice of any fall yourself, and the put pays for everything beyond the strike. Cheaper than full cover, because you self-insure the small dips.

**When & why to use it.** Use it when you are structurally long and want to stay long through a known risk — an RBI policy date, a Budget, US CPI, election counting — but cannot stomach a gap-down. Buy the put when India VIX is low and puts are cheap; do NOT load up on protection right after a crash when IV is already at 18-20 and the put is fat. The OTM strike suits investors who accept a modest drawdown and only want to cap the tail.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23700 PE at 219. The hedge costs 219 points, about 16,425 per lot — that premium is your entire insurance bill. You keep all upside above 24219 (entry plus premium).

![Figure: Protective Put (OTM) payoff at expiry](figs/strategies/protective_put.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited (the index can keep rising). Max loss: -519 points, about 38,925 per lot — the 300-point gap to the strike plus the 219 premium. Breakeven: 24219. Net debit (option only): 219 points. Risk:reward is undefined because the upside is open-ended.

**Greeks & behaviour.** Net delta is positive but less than the bare long (the put's negative delta trims it). Theta is negative — the put bleeds time value daily, the cost of carrying insurance. Vega is positive: a spike in IV lifts the put's value, so the hedge is worth more precisely when markets panic.

**Management & exit.** If the index rallies and the put decays to near zero, let it lapse and re-strike a fresh one closer to spot (roll up). If the market falls and the put goes deep ITM, you can monetise it — sell the put, bank the gain, and decide whether to re-hedge. Roll the put forward a few sessions before expiry to avoid the last-week gamma and theta cliff.

**Risk note.** The premium is a near-certain small loss every cycle — most insurance expires worthless, and that is the point. The real danger is over-hedging: buy protection every month in a bull market and the cumulative drag can eat much of your return.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹38,925 | -₹38,925 | -₹16,425 | +₹28,575 | +₹73,575 |

Read across, the protected long still earns +₹73,575 at 25,200, yet a 1,200-point slide to 22,800 costs only -₹38,925 instead of the roughly ₹90,000 a bare long would lose — the OTM put has bolted a hard floor under the position.

**Adjustments, variants & timing.** As the market climbs, roll the 23700 put up toward spot every few weeks so the floor ratchets behind your gains rather than lagging 300 points below them; fund part of that roll by closing the old put for whatever time value remains. After a sharp fall, monetise the deep-ITM put and decide whether to re-strike lower or bank the cover. For a cash-equity or mutual-fund book, size the hedge by beta: lots = (portfolio value x portfolio beta) / (Nifty x 75), rounded to whole lots, and keep an annual premium budget near 1.5-2% of the book so the drag stays tolerable. Accept basis risk when you hold mid-caps against a Nifty put. Put OTM cover on ahead of identifiable events — RBI policy, the Budget, US CPI, results season — or when valuations look stretched and India VIX is low; in calm, richly-valued grinds, carrying it always quietly erodes returns, so hedge the window, not the calendar.

## 130. Protective Put (ATM)
*Bullish, fully insured · Long vega · net debit*

**The idea (intuition).** Same insurance, no deductible. You buy the at-the-money put, so the floor sits right at your entry — any fall from here is fully covered. You pay up for the privilege of a tight floor.

**When & why to use it.** Reach for the ATM put when you genuinely cannot afford a drawdown — you are sitting on a large unrealised gain you must protect, or you are running borrowed/leveraged exposure into a binary event. It is expensive, so use it tactically over a short window (event week), not as a permanent overlay. Avoid it when IV is rich: paying 318 points for a one-month floor is a heavy carry if VIX is elevated.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 24000 PE at 318. The cover costs 318 points, about 23,850 per lot. Your floor is locked at 24000 minus the premium.

![Figure: Protective Put (ATM) payoff at expiry](figs/strategies/protective_put_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -318 points, about 23,850 per lot — purely the premium, since the strike equals entry. Breakeven: 24318. Net debit (option only): 318 points. Risk:reward undefined (open upside).

**Greeks & behaviour.** Net delta is close to +0.5x of the bare long at inception (long index +1, ATM put roughly -0.5). Theta is sharply negative — ATM options carry the most time value to lose. Vega is strongly positive; an IV spike materially helps this position.

**Management & exit.** Because ATM theta is brutal, do not hold this to expiry. Take it off once the event passes and IV crushes, or roll down to an OTM strike to cut carry once the worst-case window closes. If the market falls, the put gains delta fast and you can sell it for a strong profit, effectively flat on the round-trip minus a small cost.

**Risk note.** The biggest enemy is IV crush: buy the ATM put into an event at high IV and, even if the index drifts down a little, the volatility collapse afterward can leave the put worth less than you paid. Match the put's expiry to your risk window so you are not paying for time you do not need.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹23,850 | -₹23,850 | -₹23,850 | +₹21,150 | +₹66,150 |

The ATM floor is tighter still: the loss is pinned at -₹23,850 (pure premium) all the way down to 22,800, where an unhedged long would be down about ₹90,000, while the upside at 25,200 remains a healthy +₹66,150.

**Adjustments, variants & timing.** The ATM floor is expensive to carry, so manage it as a short-dated event overlay: once the catalyst passes and IV crushes, either lift it or roll down to an OTM strike to cut theta. As the market rises, roll the put up to lock the new level; after a fall, the put gains delta fast — sell it and re-hedge cheaper. To protect a cash or MF portfolio with an ATM index put, beta-adjust the lots = (book value x beta) / (Nifty x 75) and budget for the heavier premium (here about ₹23,850 a lot), which only makes sense over a tight window, not as a standing overlay. Watch basis risk on a mid-cap-heavy book. Put full ATM cover on only when you cannot afford any drawdown — a large unrealised gain into a binary event, or leveraged exposure into results — and buy it when VIX is low, never into an already-elevated event premium.

## 131. Collar
*Bullish, low-cost hedge · Neutral vega · net debit*

**The idea (intuition).** A protective put is insurance; a collar is insurance you pay for by selling your upside. You buy a put for a floor and sell a call above the market — the call premium funds the put. You are fencing the position into a known range.

**When & why to use it.** The classic use is protecting a large gain you do not want to sell (for tax or conviction reasons) at very low cost. Use it when you are mildly bullish-to-neutral and content to cap upside in exchange for cheap or free downside cover — common around year-end or before a long holiday gap. Do NOT collar if you expect a strong breakout; you will hand the rally to the call buyer.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23700 PE at 219, sell the 24300 CE at 292. The short call brings in 292 and the put costs 219, so the option legs net a 73-point credit — you are paid 73 points (about 5,475 per lot) to be hedged.

![Figure: Collar payoff at expiry](figs/strategies/collar.png)

**The numbers (modelled at Nifty 24000).** Max profit: 373 points (about 27,975 per lot), reached at or above the 24300 call. Max loss: -227 points (about 17,025 per lot), at or below the 23700 put. Breakeven: 23927. Net: the options are a small credit; the quoted net_cost is just the index outlay minus that credit. Risk:reward 1.64.

**Greeks & behaviour.** Net delta is positive but capped — it fades to zero as price approaches either strike. Vega is roughly neutral (long put vega offsets short call vega). Theta is close to flat or mildly positive, since the short call you sold decays in your favour.

**Management & exit.** If the index rallies into the short call, either let it get called away (you keep the capped gain) or roll the call up and out for more room, paying a small debit. If it falls to the put, your floor holds; consider rolling the whole collar down to re-establish protection at a lower level. Manage the short call before expiry week to avoid assignment surprises.

**Risk note.** The capped upside is the real cost — a runaway rally is forgone profit, which traders feel more painfully than a paid premium. On single stocks, watch assignment and STT on an exercised ITM call; on the index (cash-settled) that risk disappears.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹17,025 | -₹17,025 | +₹5,475 | +₹27,975 | +₹27,975 |

The collar fences the outcome between -₹17,025 at 22,800 and +₹27,975 at 25,200 — the put caps the fall at roughly a fifth of a bare long's loss, while the short call is what holds the gain to its ceiling.

**Adjustments, variants & timing.** Manage the short call first: if the index rallies into 24300, roll the call up-and-out for a small debit to recapture room, or let it cap and keep the maximum gain; if the market falls to the put, hold the floor and consider rolling the whole fence down to re-protect at a lower level. Reset the collar each expiry to keep the band centred. For a cash-equity or MF book, beta-adjust the lots = (portfolio value x beta) / (Nifty x 75) and prefer Nifty or Bank Nifty options matched to the book's character; a credit collar can make the hedge self-funding, so the cost budget is mainly forgone upside, not cash. Mind basis risk on non-Nifty names. A collar suits the late stage of a rally or a long holiday gap when you want cheap cover and are content to cap upside — not when you expect a breakout, which you would simply hand to the call buyer.

## 132. Costless (Zero-Cost) Collar
*Bullish, free hedge · Neutral vega · net debit*

**The idea (intuition).** The same collar, but you pick the strikes so the call you sell pays for the put you buy — protection for (almost) nothing out of pocket. Free insurance, financed entirely by giving up upside above the call.

**When & why to use it.** This is the institutional favourite for hedging a concentrated long without spending cash — promoters, PMS books, and long-term holders use it to lock a range around a position. Use it when you want a defined band and are indifferent to upside beyond a level. Do NOT mistake "zero cost" for "zero downside": you still own the gap between spot and the put strike, and you have sold your rally.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23600 PE at 192, sell the 24300 CE at 292. The call's 292 more than covers the put's 192, leaving a 100-point credit — genuinely better than free, you are paid 100 points (about 7,500 per lot) to wear the collar.

![Figure: Costless (Zero-Cost) Collar payoff at expiry](figs/strategies/costless_collar.png)

**The numbers (modelled at Nifty 24000).** Max profit: 400 points (about 30,000 per lot) above 24300. Max loss: -300 points (about 22,500 per lot) below 23600 — the distance to the put strike, softened by the credit. Breakeven: 23900. Risk:reward 1.33.

**Greeks & behaviour.** Delta positive within the band, pinned at the edges. Vega near neutral. Theta slightly positive because the richer short call decays faster than the cheaper long put.

**Management & exit.** Roll annually or each expiry to keep the band centred on a moving market. If the index pushes through the short call, roll it up-and-out to recapture some upside, accepting a small debit that breaks the "costless" label. If it sags to the put, the floor engages and you re-strike lower.

**Risk note.** The fence cuts both ways — in a strong bull run a zero-cost collar can badly lag a naked long, and that opportunity cost compounds year after year. It is a sleep-well structure, not a return-maximising one.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹22,500 | -₹22,500 | +₹7,500 | +₹30,000 | +₹30,000 |

Financed entirely by the call, the band runs from -₹22,500 at 22,800 to a capped +₹30,000 at 25,200 — the put halts the downside near the strike for no cash outlay, the trade-off being the surrendered upside.

**Adjustments, variants & timing.** Re-strike the band each expiry, or at least annually, so it tracks a moving market; if the index pushes through the short call, roll it up-and-out, accepting a small debit that breaks the strict 'costless' label but recaptures upside; if it sags to the put, the floor engages and you reset lower. For promoters, PMS books and long-term holders, this is the zero-cash way to fence a concentrated long — beta-adjust the lot count = (position value x beta) / (Nifty x 75) and choose the call strike so its premium exactly funds the put, leaving the cost budget at roughly nil. The real expense is opportunity cost, which compounds, so review the upside cap annually against your conviction. Basis risk applies if you hedge a broad book with one index. Put it on when valuations are full and you want a defined range — and lift or widen it before a genuine breakout you do not want to surrender.

## 133. Put-Spread Collar
*Bullish, cheaper hedge · Neutral vega · net debit*

**The idea (intuition).** A collar where the floor is a put SPREAD instead of a single put. You buy a put, sell a further-OTM put to cheapen it, and sell a call to fund the rest. The trade-off: protection now only runs down to the lower put strike — below that, you are exposed again.

**When & why to use it.** Use it when you want the cheapest possible "normal-correction" cover and judge a full-blown crash unlikely. It is a partial hedge: it shields the most probable 2-3% dip while you bank an extra credit. Do NOT use it as crash insurance — the lower short put re-opens your downside in exactly the scenario where you most need cover.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23700 PE at 219, sell the 23300 PE at 129, sell the 24400 CE at 246. Option legs net -219 +129 +246 = a 156-point credit (about 11,700 per lot). The protected band runs only from 23700 down to 23300.

![Figure: Put-Spread Collar payoff at expiry](figs/strategies/put_spread_collar.png)

**The numbers (modelled at Nifty 24000).** Max profit: 556 points (about 41,700 per lot) above 24400. Breakeven: 23844. Max loss is quoted as -23443 points — the theoretical figure if the index collapsed all the way to zero, because below 23300 the put spread's protection is exhausted and you are a naked long again. In practice your realistic worst case is a deep selloff through 23300; you would re-hedge or cut rather than ride the index to zero. Risk:reward shows 0.02 only because of that catastrophic-tail accounting.

**Greeks & behaviour.** Delta positive, capped above by the short call. Vega roughly neutral inside the band but turns net-short of protection below the lower strike. Theta mildly positive from the two short premiums.

**Management & exit.** If the market falls toward 23300, that is your signal to act — buy back the lower short put to restore a full floor, or close the position. On a rally into the short call, roll it up. Treat the lower strike as a hard mental stop, not a comfortable floor.

**Risk note.** This structure lulls you with a fat credit and a tidy payoff diagram, then fails in a gap-down through the lower strike — the one event a hedge exists to cover. Size it as a partial hedge only, and know where the protection stops.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹48,300 | -₹10,800 | +₹11,700 | +₹41,700 | +₹41,700 |

Protection holds the 2.5% dip to 23,400 at just -₹10,800, but a 5% fall to 22,800 already costs -₹48,300 — confirming the floor only spans 23700-23300, beyond which the long is exposed again, while the upside caps at +₹41,700.

**Adjustments, variants & timing.** Treat the lower put strike (23300) as a hard line, not a floor: if the market falls toward it, buy back the short put to restore a full floor or close the structure, because below it you are a naked long again. On a rally into the short call, roll it up to free upside. Refresh the spread each expiry. For a cash or MF book, this is a deliberately partial hedge — beta-adjust lots = (book value x beta) / (Nifty x 75) and use it only to cover the most probable 2-3% dip, banking the credit, never as crash insurance. Keep a modest annual cost budget since the structure usually nets a credit, and accept basis risk on mid-cap exposure. Put it on when you expect an orderly, shallow correction that stalls around support and judge a gap-down unlikely; before a known crash catalyst, switch to a full put or a tail hedge instead.

## 134. Married Put
*Bullish, protected entry · Long vega · net debit*

**The idea (intuition).** A protective put bought at the same moment you buy the underlying — the put and the stock are "married" at entry. From day one your maximum loss is fixed; you have defined your risk before you have made a rupee.

**When & why to use it.** Ideal for entering a fresh long into uncertainty: you like the level but a known catalyst (results, macro print) could gap it down. New or risk-averse traders use it to bound a position from the outset rather than bolting on a hedge after a fall. Skip it for slow, low-conviction holdings where the recurring premium will quietly erode returns.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 24000 PE at 414. The insurance costs 414 points, about 31,050 per lot — a richer premium here (more time value / higher IV baked in than the cheaper protective-put cases). Floor sits at the strike less premium.

![Figure: Married Put payoff at expiry](figs/strategies/married_put.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -414 points, about 31,050 per lot — exactly the premium, since the strike equals entry. Breakeven: 24414. Net debit (option only): 414 points. Risk:reward undefined (open upside).

**Greeks & behaviour.** Net delta about +0.5x of the bare long at inception. Theta negative — the ATM put decays steadily. Vega strongly positive, so the hedge gains value if fear spikes.

**Management & exit.** Set a re-hedge plan up front: if the index rallies, roll the put up to lock the new floor; if it falls, monetise the put. Do not carry the full ATM premium to expiry — the last-week theta is punishing. Many traders downgrade to an OTM strike once the initial entry risk has passed.

**Risk note.** The breakeven is a steep 414 points above entry — the index must rally over 1.7% just to clear the insurance bill. Marrying a put on every entry is a fast way to underperform a simple long in a calm, grinding market; reserve it for entries that genuinely warrant the cover.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹31,050 | -₹31,050 | -₹31,050 | +₹13,950 | +₹58,950 |

The married put pins the loss at -₹31,050 (pure premium) all the way down to 22,800 — where a bare long would shed about ₹90,000 — while leaving +₹58,950 on the table at 25,200; risk is bounded from the first rupee.

**Adjustments, variants & timing.** Plan the re-hedge before you enter: if the index rallies, roll the ATM put up to lock the new floor; if it falls, monetise the put for its gain. Do not carry the full ATM premium into expiry week — the theta is punishing — so many traders downgrade to an OTM strike once the initial entry risk has passed, cutting carry. For a fresh cash-equity position or a new MF allocation made into uncertainty, size the index put by beta: lots = (position value x beta) / (Nifty x 75), rounded whole, and budget for a richer premium (here about ₹31,050 a lot) that only pays off if the catalyst is real. Mind basis risk against non-Nifty holdings. Marry a put when you are buying into a known event — results, a macro print — and want risk bounded from rupee one; skip it on slow, low-conviction holdings where the recurring premium will quietly erode the return.

## 135. Wide Collar
*Bullish, loose hedge · Neutral vega · net debit*

**The idea (intuition).** A collar with the strikes pushed far apart, giving the position room to breathe. You only cap the extreme tails and leave a wide corridor in the middle where the underlying moves freely, almost like an unhedged long.

**When & why to use it.** Use it when you want the index to participate in normal swings but still want guardrails against a violent move either way — a "let it run, but not off a cliff" stance. Good for medium-term holders who find a tight collar too constraining. Avoid it if your real fear is a routine 3% dip: the far put may be below the dip, so it pays nothing.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23400 PE at 148, sell the 24600 CE at 167. The call funds the put with 19 points to spare — a small 19-point credit (about 1,425 per lot). Wide 1200-point fence around spot.

![Figure: Wide Collar payoff at expiry](figs/strategies/protective_collar_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit: 620 points (about 46,500 per lot) above 24600. Max loss: -580 points (about 43,500 per lot) below 23400. Breakeven: 23980. Risk:reward 1.07 — nearly symmetric, reflecting the loose, balanced fence.

**Greeks & behaviour.** Delta positive across most of the corridor and only pins near the far strikes. Vega close to neutral. Theta near flat, with a slight positive tilt from the marginally richer short call.

**Management & exit.** Because the strikes are far out, there is little to manage day to day. Roll the whole fence out in time as expiry approaches to keep the tail cover alive. If the index trends to one edge, recentre by rolling both legs. Treat it as a set-and-monitor overlay.

**Risk note.** The 1200-point span means you wear a sizeable loss before the put even engages — this is tail cover, not dip cover. Do not confuse the comfort of "I have a collar on" with meaningful near-money protection.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹43,500 | -₹43,500 | +₹1,500 | +₹46,500 | +₹46,500 |

The wide fence lets the book breathe but only catches the extremes: a 5% drop to 22,800 still costs -₹43,500 before the far put bites, and the upside runs to +₹46,500 at 25,200 — tail cover, not dip cover.

**Adjustments, variants & timing.** With strikes far apart there is little day-to-day management; the main job is to roll the whole fence forward in time as expiry nears so the tail cover stays alive, and to recentre by rolling both legs if the index trends to one edge. For a cash or MF book this is tail cover, not dip cover — beta-adjust lots = (book value x beta) / (Nifty x 75) and accept that a routine 3% slip may fall inside the corridor and pay nothing. The cost budget is near zero (the wide call usually funds the wide put), so the real price is the wide loss you wear before the put engages. Basis risk still applies. Put a wide collar on when you want the book to participate in normal swings but want guardrails against a violent move either way — a 'let it run, but not off a cliff' stance for medium-term holders — rather than as protection against ordinary corrections.

## 136. Fence (Risk-Reversal Hedge)
*Bullish, OTM hedge · Neutral vega · net debit*

**The idea (intuition).** A fence is a collar built from out-of-the-money options around a long position — an OTM put for a floor, an OTM short call for funding. The name fits: you fence the long inside a band, paying little or nothing for the rails.

**When & why to use it.** Use it to hedge a long when you are constructively bullish but want cheap insurance against a sharp drop, and you are willing to surrender gains beyond an OTM call. It is the workhorse hedge for medium-conviction holdings. Do NOT deploy it ahead of an expected breakout — the short call caps exactly the move you want.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23500 PE at 169, sell the 24500 CE at 204. Option legs net a 35-point credit (about 2,625 per lot) — you are paid a little to wear the fence. Band runs 23500 to 24500.

![Figure: Fence (Risk-Reversal Hedge) payoff at expiry](figs/strategies/fence.png)

**The numbers (modelled at Nifty 24000).** Max profit: 536 points (about 40,200 per lot) above 24500. Max loss: -464 points (about 34,800 per lot) below 23500. Breakeven: 23964. Risk:reward 1.15.

**Greeks & behaviour.** Delta positive inside the band, flattening at the strikes. Vega roughly neutral. Theta near flat to slightly positive from the short call's decay edging out the long put's.

**Management & exit.** Roll the tested side: if the index climbs toward 24500, roll the call up-and-out to free upside; if it drops toward 23500, the floor holds and you can re-strike the fence lower. Refresh in time before expiry-week gamma makes the short call jumpy.

**Risk note.** As with any short-call hedge, a strong rally is forgone profit, and on cash-settled Nifty there is no assignment worry — but on stock fences mind STT and assignment on an ITM call. The fence protects a band, not a crash beyond the put.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹34,800 | -₹34,800 | +₹2,700 | +₹40,200 | +₹40,200 |

The fence brackets the long between -₹34,800 at 22,800 and +₹40,200 at 25,200 — the OTM put softens the crash and the OTM call funds it, but a 5% move still runs most of the way to each rail before the strikes engage.

**Adjustments, variants & timing.** Roll the tested side: if the index climbs toward the 24500 call, roll it up-and-out to free upside; if it drops toward the 23500 put, the floor holds and you can re-strike the fence lower. Refresh before expiry-week gamma makes the short call jumpy. For a cash-equity or MF book, beta-adjust the lot count = (portfolio value x beta) / (Nifty x 75) and use OTM Nifty or Bank Nifty strikes so the call funds most of the put, keeping the annual cost budget near zero. Basis risk applies on mid-cap-heavy books. The fence is the workhorse for medium-conviction holdings: put it on when you are constructively bullish but want cheap insurance against a sharp drop and can surrender gains beyond the call — and take it off, or roll the call up, ahead of an expected breakout, since the short call caps exactly the move you are hoping for.

## 137. Put-Ratio Hedge
*Hedge a long, cheaply · Mixed vega · net debit*

**The idea (intuition).** You hedge with a 1x2 put ratio: buy one near-the-money put and sell two further-OTM puts to pay for it. The two short puts make the hedge almost free in the protected zone — but they also leave you over-short below the lower strike, where a crash hurts instead of helps.

**When & why to use it.** Use it for very cheap protection against a moderate, orderly decline that you expect to stall around the lower strike. It shines in low-VIX drifts. Do NOT use it as crash cover: the extra short put means a violent gap-down past the lower strike turns your hedge into a second losing long.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 24000 PE at 318, sell 2x the 23400 PE at 148 each (296 total). Option legs net just -22 points — about a 1,650-per-lot debit for a full 600-point protected band. The cover is nearly self-financing.

![Figure: Put-Ratio Hedge payoff at expiry](figs/strategies/put_ratio_hedge.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited (still long the index). Breakeven: 24023. Max loss is quoted as -46821 points — the theoretical figure if the index fell to zero, because below 23400 you hold the long index PLUS a net-short put, a doubly leveraged downside. That worst case assumes a collapse to zero; in practice you size this small and stop out or buy back the extra short put if the market breaks the lower strike. Risk:reward undefined.

**Greeks & behaviour.** Delta positive near spot but swings sharply negative-exposure below the lower strike as the net-short put dominates. Vega is mixed and turns short below the strikes — rising IV in a selloff hurts the uncovered short put. Theta mildly positive from the two shorts.

**Management & exit.** Define a hard line at 23400: if the index threatens it, buy back one short put to neutralise the dangerous leg. Take the hedge off once the feared dip has played out around the long-put strike. Never let this run unmanaged into expiry week.

**Risk note.** This is the most deceptive structure in the group — beautiful for a mild dip, ruinous in a true crash, which is the one event you hedge for. Treat it as a tactical cheapener for a small portion of the book, never as portfolio insurance.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹91,725 | -₹1,725 | -₹1,725 | +₹43,275 | +₹88,275 |

The ratio hedge looks benign at a moderate dip — only -₹1,725 at 23,400 — but a 5% crash to 22,800 costs -₹91,725, worse than a bare long, as the extra short put turns the hedge into a second losing position below 23400.

**Adjustments, variants & timing.** This needs active management, not set-and-forget. Define a hard line at the lower strike (23400): if the index threatens it, buy back one short put immediately to neutralise the dangerous net-short leg, because below there you hold the long index plus a short put — a doubly leveraged downside. Take the hedge off once the feared dip stalls around the long-put strike, and never carry it unmanaged into expiry. For a cash or MF book, size it small — beta-adjust lots = (book value x beta) / (Nifty x 75) but apply only to a fraction you can actively watch — with a near-zero cost budget since the two shorts almost self-finance the cover. Basis risk compounds the tail danger. Use it only in a low-VIX drift when you expect a moderate, orderly decline that halts around the lower strike; never as portfolio crash insurance, the exact scenario where the extra short put turns the hedge into a second losing long.

## 138. Tail-Risk Hedge
*Crash insurance · Long vega · net debit*

**The idea (intuition).** Buy a far-out-of-the-money put as cheap, persistent catastrophe cover. It is lottery-ticket insurance: most of the time it expires worthless, but in a crash it pays off many times over, exactly when the rest of your book is bleeding.

**When & why to use it.** This is the structure for the investor who wants to stay fully long but hold a small, standing hedge against a market dislocation — a 2008/2020-style gap. Buy it when VIX is low and far puts are cheap; that is when crash cover is on sale and nobody wants it. Do NOT expect it to cover ordinary 3-5% dips — the strike is too far away for that.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 22500 PE at 118. The cover costs just 118 points, about 8,850 per lot — under 0.5% of notional for a deep-tail floor 1500 points away.

![Figure: Tail-Risk Hedge payoff at expiry](figs/strategies/tail_risk_hedge.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -1618 points, about 121,350 per lot — the 1500-point drop to the strike plus the 118 premium (the long index loses on the way down before the put engages). Breakeven: 24118. Net debit (option only): 118 points. Risk:reward undefined.

**Greeks & behaviour.** Delta barely below the bare long (the far put has tiny delta). Theta is small and negative — the cheap premium bleeds slowly. Vega is positive and is the star: far-OTM puts are pure convexity, so an IV explosion in a crash can multiply the put's value even before the strike is breached.

**Management & exit.** The classic trade is to monetise into panic — when the market gaps down and IV spikes, the put's value can balloon; sell it, harvest the convexity, and redeploy. Otherwise roll the cheap put forward each month or quarter as a standing line item in the cost of being invested.

**Risk note.** The painful truth: this hedge loses a little money almost every single month, and that recurring drag is the whole cost of owning crash protection. The mistake is abandoning it after a long calm stretch — that is precisely when the next crash arrives.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹98,850 | -₹53,850 | -₹8,850 | +₹36,150 | +₹81,150 |

Tail cover does little for ordinary moves — a 2.5% dip still costs -₹53,850 — and the table's linear -₹98,850 at 22,800 actually understates its worth, since it ignores the IV-driven convexity that makes the far put explode in a real crash; the upside meanwhile reaches +₹81,150.

**Adjustments, variants & timing.** The signature move is to monetise into panic: when the market gaps down and IV explodes, the far put's value can balloon through pure convexity even before the strike is breached — sell it, harvest the gain, and redeploy. Otherwise roll the cheap put forward each month or quarter as a standing line item. For a cash-equity or MF book, beta-adjust the lots = (book value x beta) / (Nifty x 75) and keep the annual cost budget tiny (here under 0.5% of notional per cover) since deep-OTM puts are cheap; that small drag is the whole price of crash insurance. Basis risk matters less here because a true dislocation drags everything down together. Carry it always, not tactically — the discipline is to keep paying when markets are calm and far puts are on sale, precisely because the urge to drop the hedge after a long quiet stretch is exactly when the next crash tends to arrive.

## 139. Put-Backspread Hedge
*Long, with crash kicker · Long vega · net debit*

**The idea (intuition).** Overlay a put backspread on your long: sell one near put and buy two lower puts. In a crash the two long puts overpower the short one, so a deep selloff actually turns into a gain — your hedge has a built-in profit kicker beyond a mild dip.

**When & why to use it.** Use it when you are long but assign real probability to a large, fast move down — you want ordinary cover and a payoff if the tail actually hits. Best entered when skew is reasonable and lower puts are not too expensive relative to the near put. Avoid it if you expect a shallow grind lower that stalls between the strikes — that is its worst zone.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, sell the 24000 PE at 318, buy 2x the 23600 PE at 192 each (384 total). Option legs net -66 points — about a 4,950-per-lot debit. Below 23600 the extra long put accelerates gains.

![Figure: Put-Backspread Hedge payoff at expiry](figs/strategies/put_backspread_hedge.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited — both from the long index on the upside and from the extra long put on a deep downside. Max loss: -866 points, about 64,950 per lot, occurring around the lower strike (23600) where the short put has cost you but the long puts have not yet taken over. Breakeven: 24066. Risk:reward undefined.

**Greeks & behaviour.** Delta positive near spot, then flips to strongly negative-exposure below the lower strike as the two long puts dominate — that flip is the crash kicker. Vega is positive and grows in a selloff. Theta is negative in the trough zone, since you are net-long two decaying puts there.

**Management & exit.** The worst outcome is pinning at the lower strike into expiry, where time decay and the payoff valley meet — exit or roll well before expiry week if the index is camped near 23600. If a crash develops, the long puts surge; harvest them. If the market rallies, let the cheap overlay lapse and keep your long.

**Risk note.** The maximum-pain point is a slow drift to the lower strike — the exact path a nervous market often takes. This is a sophisticated overlay; size it modestly and respect the trough between the strikes.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹64,950 | -₹64,950 | -₹4,950 | +₹40,050 | +₹85,050 |

The trough sits at the lower strike — -₹64,950 at both 23,400 and 22,800 in this expiry snapshot — but below 23600 the two long puts begin clawing the loss back toward a crash gain, while the long index still delivers +₹85,050 at 25,200.

**Adjustments, variants & timing.** The worst outcome is pinning at the lower strike (23600) into expiry, where decay and the payoff valley meet, so exit or roll well before expiry week if the index is camped there. If a crash develops, the two long puts surge — harvest them; if the market rallies, let the cheap overlay lapse and keep the long. For a cash or MF book, size it modestly — beta-adjust lots = (book value x beta) / (Nifty x 75) on only the slice you want a tail kicker on — with a small net-debit budget (here about ₹4,950 a lot). Enter when skew is reasonable and the lower puts are not dear relative to the near put. Basis risk applies. Use it when you are long but assign real probability to a large, fast move down and want both ordinary cover and a payoff if the tail hits — but avoid it when you expect a shallow grind that stalls between the strikes, its worst zone.

## 140. Collar for a Credit
*Bullish, paid to hedge · Neutral vega · net debit*

**The idea (intuition).** A collar where the call you sell is worth more than the put you buy, so you pocket a net credit for putting the hedge on. You are quite literally paid to insure your long — the catch is a tighter, lower upside cap.

**When & why to use it.** Use it when you are neutral-to-mildly-bullish and happy to cap upside fairly close in exchange for both downside cover and a credit — a sensible stance late in a rally when you doubt much more upside but want protection. The credit cushions your breakeven below spot. Do NOT use it if you still see meaningful upside; the near call gives it away cheaply.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23500 PE at 169, sell the 24200 CE at 342. Option legs net a 173-point credit — about 12,975 per lot collected to be hedged. The credit drops your breakeven to 23826, below the spot.

![Figure: Collar for a Credit payoff at expiry](figs/strategies/collar_for_credit.png)

**The numbers (modelled at Nifty 24000).** Max profit: 374 points (about 28,050 per lot) above 24200. Max loss: -326 points (about 24,450 per lot) below 23500. Breakeven: 23826 — notably under spot, thanks to the credit. Risk:reward 1.15.

**Greeks & behaviour.** Delta positive but capped fairly near, because the short call sits only 200 points above spot. Vega roughly neutral. Theta positive — the richer, nearer short call decays faster than the OTM long put, so time works for you.

**Management & exit.** Watch the near-money short call: if the index pushes toward 24200, roll it up-and-out to avoid surrendering a rally, accepting a smaller credit. If the market falls, the floor holds and the credit is yours to keep. Manage assignment risk on stock versions before expiry.

**Risk note.** That nearby call cap is the price of the credit — a brisk rally is capped quickly, and the credit is small consolation against a big missed move. The sub-spot breakeven is the genuine attraction: you are hedged and already a touch ahead.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹24,450 | -₹24,450 | +₹13,050 | +₹28,050 | +₹28,050 |

The credit collar brackets the long between -₹24,450 at 22,800 and a capped +₹28,050 at 25,200, and its sub-spot breakeven means the floor and the upfront credit together blunt the downside more than a plain collar would.

**Adjustments, variants & timing.** Watch the near-money short call closely: if the index pushes toward 24200, roll it up-and-out to avoid surrendering a rally, accepting a smaller credit; if the market falls, the floor holds and the credit is yours to keep. Reset each expiry. The attraction is the sub-spot breakeven (23826) — the credit puts you slightly ahead the moment you hedge. For a cash or MF book, beta-adjust lots = (portfolio value x beta) / (Nifty x 75) and choose a nearer call so the structure nets a credit, making the cost budget negative — you are paid to hedge. Basis risk applies on non-Nifty names. Put it on late in a rally when you are neutral-to-mildly-bullish, doubt much further upside, and want both downside cover and a small credit; do not use it while you still see meaningful upside, because the near call gives that rally away cheaply for a modest payment.

## 141. Protective Put Spread
*Bullish, partial hedge · Neutral vega · net debit*

**The idea (intuition).** Hedge with a put SPREAD rather than a single put: buy a put, sell a lower put to cheapen it. You get a defined band of protection at a fraction of the cost — but the cover stops at the lower strike, below which you are a naked long again.

**When & why to use it.** Use it when you want cheap insurance against a specific, bounded decline — you think the index might slip to a support level but not crash through it. It is a partial hedge for cost-conscious holders. Do NOT rely on it through a known crash catalyst; the lower short put caps your protection at exactly the wrong moment.

**How to build it (₹, Nifty).** Long 1x underlying at 24000, buy the 23800 PE at 248, sell the 23300 PE at 129. Option legs net a 119-point debit — about 8,925 per lot for a 500-point protected band (23800 down to 23300).

![Figure: Protective Put Spread payoff at expiry](figs/strategies/protective_put_spread.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited (still long the index above). Breakeven: 24119. Max loss is quoted as -23618 points — the theoretical figure if the index fell to zero, because below 23300 the spread's protection is spent and you ride the index down unhedged. That worst case assumes a collapse to zero; realistically you would re-hedge or exit on a break of 23300 and size the position with that line in mind. Risk:reward undefined.

**Greeks & behaviour.** Delta positive, reduced inside the protected band by the long put spread. Vega is roughly neutral within the band (long and short put vegas offset) and turns unprotected below the lower strike. Theta slightly negative from the net long premium.

**Management & exit.** Treat 23300 as a hard stop, not a floor — if the market approaches it, buy back the short put to restore full cover or close out. On a rally, let the cheap spread decay and re-strike. The spread is most useful as a defined, expiry-matched dip hedge.

**Risk note.** The danger is psychological as much as financial: the tidy payoff diagram suggests you are covered, but a gap-down through 23300 leaves you fully exposed. Use it as a deliberate partial hedge and never confuse it with crash insurance.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹61,425 | -₹23,925 | -₹8,925 | +₹36,075 | +₹81,075 |

The put spread cushions a move to support — only -₹8,925 at 23,400 — but a 5% drop to 22,800 already costs -₹61,425 as protection runs out below 23300, while the long keeps +₹81,075 of upside at 25,200.

**Adjustments, variants & timing.** Treat the lower strike (23300) as a hard stop, not a floor: if the market approaches it, buy back the short put to restore full cover or close out, since below it you ride the index down unhedged. On a rally, let the cheap spread decay and re-strike; match the spread's expiry to your dip horizon. For a cash-equity or MF book this is a defined, partial hedge — beta-adjust lots = (book value x beta) / (Nifty x 75) and use it to cover a specific, bounded decline to a support level, budgeting the modest net debit (here about ₹8,925 a lot). Accept basis risk on mid-cap exposure. Put it on when you think the index may slip to support but not crash through it; do not rely on it through a known crash catalyst, where the lower short put caps your protection at exactly the wrong moment — switch to a full put or tail hedge for that.

## 142. Index Put Hedge Overlay
*Portfolio insurance · Long vega · net debit*

**The idea (intuition).** Buy Nifty puts to hedge an entire long book — a basket of cash equities or mutual funds — for a fixed period. Rather than insuring each holding, you buy one index put against the whole portfolio's market exposure. This is how real money runs portfolio insurance.

**When & why to use it.** This is the practical answer to "how does an Indian investor hedge a cash-equity or MF book?" Use Nifty puts when you want to stay invested through a risky window (results season, a global event) without selling holdings and triggering tax or exit loads. Buy when VIX is low. Do NOT over-rely on it if your portfolio is full of mid/small-caps — Nifty puts hedge large-cap beta, and the basis mismatch can be large.

**How to build it (₹, Nifty).** Long 1x underlying (your book's index-equivalent) at 24000, buy the 23600 PE at 251. The cover costs 251 points, about 18,825 per lot. The key real-world step is lot-sizing: hedge ratio equals portfolio value times its Nifty beta, divided by (Nifty level times 75); round to whole lots.

![Figure: Index Put Hedge Overlay payoff at expiry](figs/strategies/index_hedge_overlay.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited (your long book keeps appreciating). Max loss on this single-lot model: -651 points, about 48,825 per lot — the 400-point gap to the strike plus the 251 premium. Breakeven: 24251. Net debit (option only): 251 points. Risk:reward undefined.

**Greeks & behaviour.** Net delta positive but trimmed by the put. Theta negative — the overlay bleeds time value, the standing cost of insurance. Vega positive: the hedge gains value as fear and IV rise, partly offsetting book losses in a selloff.

**Management & exit.** Roll the put forward each month or quarter, re-striking near spot as the market moves and re-computing the lot count as the book's value changes. Monetise the put into a spike and redeploy. Reduce or lift the hedge once the risk window passes to stop the carry drag.

**Risk note.** Basis risk is the central caveat — Nifty puts will not perfectly track a portfolio of non-Nifty or smaller-cap names, so the hedge can under- or over-cover. Add tracking error from rounding to whole lots, plus the certain premium drag, and you have a useful but imperfect shield. The discipline is to hedge the beta you can, accept the rest, and keep paying the premium that, most months, you will be glad went to waste.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹48,825 | -₹48,825 | -₹18,825 | +₹26,175 | +₹71,175 |

The single-lot overlay caps a 5% fall at -₹48,825 versus the roughly ₹90,000 a bare index lot would lose, and keeps +₹71,175 at 25,200 — but on a real book those rupees only land cleanly to the extent the holdings track Nifty.

**Adjustments, variants & timing.** Roll the put forward each month or quarter, re-striking near spot as the market moves and re-computing the lot count as the book's value changes; monetise the put into a spike and redeploy, and lift the hedge once the risk window passes to stop the carry drag. The core discipline is lot-sizing: lots = (portfolio value x portfolio Nifty beta) / (Nifty x 75), rounded to whole lots, so a 30-lakh book at beta 1.1 against Nifty 24000 needs about 18 lots. Use Bank Nifty puts instead if the book is bank-heavy. Budget 2-4% of the book a year for cover and accept basis risk — Nifty puts hedge large-cap beta, not mid/small-cap names. Put the overlay on ahead of a risky window — results season, a global event — when you want to stay invested without selling and triggering tax or exit loads, and buy when VIX is low; carry it always only if your mandate forbids drawdowns.

