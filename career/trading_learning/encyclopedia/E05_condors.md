# Strategy Group 5: Condors

A condor is a strangle with insurance: you sell two out-of-the-money options to collect premium, then buy two further-out options as wings so the loss is capped and SPAN margin stays manageable. The whole family trades the same core thesis — Nifty stays inside a band until expiry — and the levers you pull (wing width, how far OTM you place the shorts, days to expiry, and whether you skew the structure) decide how often you win versus how much you keep. The iron condor is the desk workhorse for monthly income; its cousins (all-call, all-put, reverse, broken-wing, weekly, skewed) are the same skeleton bent to express a lean, a tenor, or a volatility view.

## 63. Iron Condor
*Range-bound, elevated IV · Short vega · net credit*

**The idea (intuition).** Sell a call spread above the market and a put spread below it. You are renting out the space on both sides of Nifty and pocketing rent (the credit) as long as price stays in the middle. The bought wings are a cheap fire-extinguisher that converts an unlimited short strangle into a defined-risk trade.

**When & why to use it.** This is the bread-and-butter income trade for a sideways-to-choppy market with rich premium. Put it on when India VIX is elevated or IV rank is high (say > 50-70), ideally just after an IV spike — a Budget print, an RBI policy day, or a results-season pop — so you sell expensive options into a coming IV crush. The 16-delta shorts here sit a comfortable distance from 24000. Do NOT sell condors into a trending, low-IV tape: you collect peanuts and a single 1.5% Nifty day blows through a short strike.

**How to build it (₹, Nifty).** Sell 24400 CE @ 246, buy 24700 CE @ 135; sell 23600 PE @ 192, buy 23300 PE @ 129. Net credit 174.4 points, about 174.4 × 75 = ₹13,080 received per lot. Both wings are 300 points wide.

![Figure: Iron Condor payoff at expiry](figs/strategies/iron_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 174 points (₹13,050/lot) if Nifty expires between 23600 and 24400. Max loss 126 points (₹9,450/lot). Breakevens 23426 and 24574 — a roughly ±2.4% band. Net credit 174.4 points; risk:reward 1.39 (you risk less than you can make, the mark of a tight, balanced condor).

**Greeks & behaviour.** Net delta near zero at entry (direction-neutral). Theta is positive and is your engine — every quiet day bleeds the shorts in your favour. Vega is negative, so falling IV helps and an IV spike hurts even if price hasn't moved. Theta-versus-gamma is the whole game.

**Management & exit.** Standard playbook: take it off at ~50% of max credit (here ~₹6,500/lot) rather than squeezing the last rupee. If a short strike is breached or its delta doubles, roll the untested spread closer to recentre, or roll out in time. Don't carry into expiry-week gamma.

**Risk note.** Defined risk, but losses arrive fast: near a short strike, gamma makes the position lose on every point and an overnight gap can land you near max loss before you can act. Manage mechanically.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -9,450 | -1,950 | +13,050 | -1,950 | -9,450 |

The table shows the symmetric defined-risk profile: the full +13,050 credit lands only on a 24,000 pin, sliding to the -9,450 max loss once Nifty clears either wing at 22,800 or 25,200.

**Adjustments, variants & timing.** Manage mechanically: buy the condor back at ~50% of the 174-point credit (around Rs 6,500/lot), and as a hard rule close or roll at 21 DTE to sidestep expiry-week gamma. If Nifty tags a short strike or its delta doubles toward 30, roll the untested spread inward to recentre the body and harvest extra credit, or roll the whole structure out to the next monthly. To defend a breached call short, roll it up-and-out; for a breached put short, roll down-and-out, accepting a debit only if it materially cuts risk. Run this on the Nifty monthly series, not Bank Nifty weeklies - Bank Nifty's fatter gamma and bank-heavy gap moves punish a balanced condor's tight band. Enter only when IV rank sits above 50-70 (a post-Budget or post-RBI vol pop is ideal), place the ~16-delta shorts about 45 DTE, and size so one max-loss month costs no more than 1-2% of capital.

## 64. Iron Condor (Wide)
*Range-bound · Short vega · net credit*

**The idea (intuition).** Same machine as the standard condor, but the short strikes are pushed further from spot and the wings widened. You are renting out a much bigger room, so you win more often — but each wing now covers more points, so when you are wrong the loss is larger than the credit.

**When & why to use it.** Reach for the wide condor when you want a high hit-rate, low-touch trade and you genuinely believe Nifty will stay broadly contained — for example a slow grind between events with no near-term catalyst. The wider shorts (here ~24600 / 23400) give a fat profit zone. The catch: risk:reward inverts, so you must win frequently to come out ahead. Avoid it if you can't commit to managing the rare but painful losing month.

**How to build it (₹, Nifty).** Sell 24600 CE @ 167, buy 25000 CE @ 63; sell 23400 PE @ 148, buy 23000 PE @ 85. Net credit 166.8 points, about ₹12,510 per lot. Wings are 400 points wide.

![Figure: Iron Condor (Wide) payoff at expiry](figs/strategies/iron_condor_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 167 points (₹12,525/lot) between 23400 and 24600. Max loss 233 points (₹17,475/lot) — notably bigger than the credit. Breakevens 23233 and 24767, roughly a ±3.2% band. Net credit 166.8 points; risk:reward 0.72 — you risk more than you can make.

**Greeks & behaviour.** Delta-neutral at entry. Positive theta (the income), negative vega (short volatility). Because the shorts are far OTM, day-to-day delta and gamma are small until price travels meaningfully — this trade behaves sleepily right up until a wing is threatened.

**Management & exit.** With a sub-1 risk:reward, discipline matters more, not less. Close at 50% of credit and resist greed. Because the loss exceeds the credit, set a hard mental stop (e.g. exit if the loss reaches the credit you took in) so one bad month doesn't erase several good ones.

**Risk note.** The structural danger is the lopsided payoff: many small wins lull you, then a trending month delivers a loss bigger than two prior wins combined. SPAN margin is also higher on the wider wings. Size accordingly.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -17,475 | +12,525 | +12,525 | +12,525 | -17,475 |

The flat +12,525 profit shelf spans the whole 23,400-24,600 core, but the table makes the lopsidedness plain - a tail print at 22,800 or 25,200 costs -17,475, more than the credit.

**Adjustments, variants & timing.** Because the loss (Rs 17,475) dwarfs the credit, discipline is everything: take profits at ~50% of the 167-point credit and set a hard stop at roughly one credit of loss. Close or roll at 21 DTE; the wide shorts feel safe but expiry-week gamma still bites. If Nifty pushes toward a far short, roll the untested side in to recentre, or roll the tested spread out-and-away in time. Keep this on the Nifty monthly - the wide band needs room and the slow decay that Bank Nifty weeklies don't give. Enter on IV rank above 50-70 after a vol spike, with ~16-delta shorts around 45 DTE. Size small: the lopsided payoff means a single trending month can erase two or three quiet wins, so cap exposure to 1-2% of capital and never add to a tested position hoping for mean-reversion.

## 65. Iron Condor (Narrow)
*Tightly range-bound · Short vega · net credit*

**The idea (intuition).** Pull the short strikes in close to spot and tighten the wings. The shorts are nearly at-the-money, so they are fat with premium — you collect a big credit for renting a small room. The trade-off is obvious: the room is so small that Nifty barely has to twitch to put you in trouble.

**When & why to use it.** A narrow condor is a high-conviction "nothing happens this expiry" bet — a dead, pinned tape with low realised volatility and an expiry magnet near 24000. It is most attractive when premium is rich relative to the tiny range. Use it for a short window (the last week or two of a sleepy cycle), not as a set-and-forget monthly. Never run it through a known catalyst; the shorts are too close to survive a surprise.

**How to build it (₹, Nifty).** Sell 24250 CE @ 317, buy 24500 CE @ 204; sell 23750 PE @ 233, buy 23500 PE @ 169. Net credit 176.9 points, about ₹13,270 per lot. Wings are only 250 points wide.

![Figure: Iron Condor (Narrow) payoff at expiry](figs/strategies/iron_condor_narrow.png)

**The numbers (modelled at Nifty 24000).** Max profit 177 points (₹13,275/lot) between 23750 and 24250. Max loss only 73 points (₹5,475/lot) thanks to the tight wings. Breakevens 23573 and 24427 — a slim ±1.8% band. Net credit 176.9 points; risk:reward 2.42, the best in the family because of those narrow wings.

**Greeks & behaviour.** Delta-neutral at entry but very twitchy: with shorts near the money, gamma is high, so net delta swings hard as Nifty moves. Theta is strong (lots of premium decaying fast) and vega is sharply negative — an IV pop hurts immediately.

**Management & exit.** This is an active trade. Take profits early and often — 40-50% of the credit can come in a day or two if the market pins. Because gamma is high, do not let it run into expiry week; the same gamma that decays fast can flip a winner to a loser on one gap.

**Risk note.** High gamma is the killer: the small range means breakevens are close, and an intraday move of a percent can swing you from near-max-profit to near-max-loss. Treat it as a short-fuse trade, watched daily.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -5,475 | -5,475 | +13,275 | -5,475 | -5,475 |

The narrow body pays the full +13,275 only at a tight 24,000 pin, and even a one-step drift to 23,400 or 24,600 already books the -5,475 max loss.

**Adjustments, variants & timing.** This is a watched-daily trade. With shorts near the money, take 40-50% of the 177-point credit fast - it can arrive in a day or two if Nifty pins - and never carry it into expiry week; close at 21 DTE at the latest. Defending a breached short is hard because the wings are tight, so favour closing over rolling; if you must adjust, roll the tested spread out in time rather than chasing it in price. A narrow condor actually fits a Bank Nifty weekly or a Nifty weekly better than the monthly: a short, dead window is its only safe habitat. Enter only on high IV rank (>50-70) into a pinned, low-realised-vol tape, place the shorts by delta near the money but size tiny - a one-percent intraday move swings you max-profit-to-max-loss, so risk no more than a fraction of a normal condor's capital.

## 66. Call Condor
*Range-bound · Short vega · net debit*

**The idea (intuition).** A condor built entirely from calls. Buy a lower call, sell two middle calls, buy a higher call — a long call spread financed by a short call spread above it. The payoff is the same flat-topped tent as an iron condor, just assembled from one option type. You pay a small net debit instead of receiving a credit, but the economics rhyme.

**When & why to use it.** Functionally interchangeable with the iron condor for a range view; pick whichever offers better fills and liquidity on the day. On NSE the call side is often very liquid around Nifty's at-the-money strikes, so an all-call condor can sometimes be built with tighter spreads than mixing puts and calls. Use it when you expect Nifty to drift around 24000 into expiry and you'd rather pay a defined debit than manage a credit's margin.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655, sell 24000 CE @ 456, sell 24300 CE @ 292, buy 24600 CE @ 167. Net debit 74.1 points, about 74.1 × 75 = ₹5,558 paid per lot. Strikes are evenly 300 points apart.

![Figure: Call Condor payoff at expiry](figs/strategies/call_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 226 points (₹16,950/lot) when Nifty expires between 24000 and 24300, the flat top. Max loss is just the 74-point debit (₹5,550/lot) if price exits beyond either outer wing. Breakevens 23774 and 24526. Net debit 74.1 points; risk:reward 3.05 — attractive because your loss is capped at the small premium paid.

**Greeks & behaviour.** Net delta roughly flat at entry because the long and short call spreads offset. Theta is positive once Nifty sits inside the body (the short middle calls decay for you); vega is negative. As with all condors, time and calm are your allies.

**Management & exit.** Target a partial close once the position reaches a good fraction of max profit — you rarely capture the full 226 points unless Nifty pins the body at expiry. If price runs toward an outer strike, the trade approaches its capped loss; cut it and recycle the margin.

**Risk note.** The risk is benign and fully defined (you can lose at most the debit), but the maximum profit only materialises if Nifty parks in a narrow band at expiry — realistically you book a fraction. Watch the bid-ask on four call legs; slippage eats a small debit quickly.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -5,550 | -5,550 | +16,950 | -5,550 | -5,550 |

The all-call body delivers its +16,950 peak only with Nifty parked at 24,000; any exit beyond the wings caps the loss at the -5,550 debit.

**Adjustments, variants & timing.** Loss is capped at the 74-point debit, so management is about banking profit, not survival. You rarely capture the full 226 points without an expiry pin in the 24000-24300 body - scale out as you reach 50-60% of max, and roll the whole structure to the next cycle near 21 DTE rather than let four call legs decay into expiry gamma. If Nifty runs toward an outer wing, the trade drifts to its capped loss; cut it and recycle the margin. Build it on the Nifty monthly where at-the-money call liquidity is deepest and four-leg slippage is smallest; Bank Nifty's wider call spreads eat a thin debit. Enter when IV rank is elevated (>50-70) so the short body is rich, place strikes around the ~16-delta band at ~45 DTE, and size so the full debit is an acceptable loss - it is the entire downside.

## 67. Put Condor
*Range-bound · Short vega · net debit*

**The idea (intuition).** The mirror image of the call condor, built from four puts. Buy a higher put, sell two middle puts, buy a lower put. Same flat-topped, defined-risk range payoff — just expressed on the put side of the chain. Think of it as betting Nifty sits still, paid for with a modest debit.

**When & why to use it.** Choose the all-put construction when the put chain prices better, or to lean into the natural put skew on NSE indices — Nifty puts usually carry richer implied vol than equidistant calls, which can make the short middle puts juicier. Same regime as any condor: range-bound, ideally elevated IV that you expect to fade. Don't deploy into a market that's breaking down; puts gain value fast on the downside and your short body gets run over.

**How to build it (₹, Nifty).** Buy 24300 PE @ 453, sell 24000 PE @ 318, sell 23700 PE @ 219, buy 23400 PE @ 148. Net debit 63.1 points, about ₹4,733 paid per lot. Strikes are 300 points apart.

![Figure: Put Condor payoff at expiry](figs/strategies/put_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 237 points (₹17,775/lot) when Nifty expires between 23700 and 24000. Max loss is the 63-point debit (₹4,725/lot) beyond the outer wings. Breakevens 23463 and 24237. Net debit 63.1 points; risk:reward 3.76 — even better than the call condor here, because the put skew let you build the body for a smaller net debit.

**Greeks & behaviour.** Near delta-neutral at entry. Positive theta when Nifty is inside the body, negative vega — rising IV (a fear spike) works against you even before price moves. The structure behaves identically to a same-strike iron condor.

**Management & exit.** Manage like any condor: scale out as you approach a healthy share of max profit, and accept that the full 237 points needs a pin. If Nifty trends down toward the body, the short puts swell — take the capped loss rather than hoping for a bounce.

**Risk note.** Defined risk equal to the small debit, but four put legs mean four bid-ask spreads; on a thin expiry the slippage can be a meaningful chunk of a 63-point debit. The profit also assumes a tidy expiry pin that the market rarely gifts in full.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -4,725 | -4,725 | +17,775 | -4,725 | -4,725 |

The put-built body tops out at +17,775 on a 24,000 pin, with downside capped at the small -4,725 debit everywhere else in the table.

**Adjustments, variants & timing.** Risk is the small 63-point debit, so manage for profit capture. The full 237 points needs an expiry pin in the 23700-24000 body; scale out at 50-60% of max and roll to the next series near 21 DTE before expiry-week gamma distorts the four put legs. If Nifty trends down through the body, the short puts swell toward the capped loss - take it rather than hoping for a bounce. Build on the Nifty monthly, where the persistent index put skew makes the short body richer and the all-put construction cheaper than on Bank Nifty weeklies. Enter on IV rank above 50-70 so you sell into expensive downside vol, place the body around the ~16-delta zone at ~45 DTE, and size for the debit as total loss. Watch the bid-ask: four put spreads on a thin expiry can quietly consume a meaningful slice of a 63-point debit.

## 68. Reverse Iron Condor
*Break out of a range · Long vega · net debit*

**The idea (intuition).** Flip the iron condor inside-out: buy the inner strangle and sell the outer wings. Now you WANT Nifty to move — a big swing in either direction pushes one of your long spreads to full value. It's a defined-risk, two-sided breakout bet; you pay a debit and profit if price leaves the body.

**When & why to use it.** This is a long-volatility trade for when you expect a large move but don't know the direction, and you want the cost (and risk) capped by selling wings against your long options. Good ahead of a binary catalyst when IV is still cheap — pre-Budget, pre-RBI, pre-election-result — so you're long vega before the IV ramp. Do NOT hold it through a calm, decaying tape; theta grinds against you every quiet day and IV crush after the event can sink it even if Nifty moves a little.

**How to build it (₹, Nifty).** Buy 24400 CE @ 246, sell 24700 CE @ 135; buy 23600 PE @ 192, sell 23300 PE @ 129. Net debit 174.4 points, about ₹13,080 paid per lot — the exact inverse of the standard iron condor's credit.

![Figure: Reverse Iron Condor payoff at expiry](figs/strategies/reverse_iron_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 126 points (₹9,450/lot) if Nifty travels beyond a wing (above 24700 or below 23300). Max loss 174 points (₹13,050/lot) — the debit — if it expires inside the body around 24000. Breakevens 23426 and 24574. Net debit 174.4 points; risk:reward 0.72 — you risk more than you make, the price of a defined-risk long-vol position.

**Greeks & behaviour.** Delta-neutral at entry but long gamma — it gains as Nifty accelerates away from 24000. Theta is negative (time is the enemy) and vega is positive, so an IV expansion helps even before price commits. This is the mirror of the income condor in every Greek.

**Management & exit.** Have a plan to exit fast — capture the move within a few days of the catalyst before theta and IV crush erode it. If the event passes and Nifty sits in the body, cut the loss rather than hoping; the trade decays daily. Take profits into the spike; don't wait for the wing to be fully reached.

**Risk note.** The double drag of negative theta and post-event IV crush means you can be right on direction yet still lose if the move is too small or too slow. Treat it as a short-window event play, not a position to sit on.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +9,450 | +1,950 | -13,050 | +1,950 | +9,450 |

The mirror image of the income condor: the table pays +9,450 in the tails (22,800 / 25,200) and takes the -13,050 debit as max loss on a 24,000 pin.

**Adjustments, variants & timing.** This is a hit-and-run event trade, not a hold. Have a profit target and take it into the spike - capture the move within a day or two of the catalyst, well before theta and post-event IV crush erode the debit; don't wait for a wing to be fully reached. If the event passes and Nifty sits in the body near 24000, cut immediately rather than bleed daily; effectively your manage-at-50% rule lives on the long side, taking half the move. Run it on a Nifty monthly only if the catalyst is weeks out; for near-term binaries a Bank Nifty or Nifty weekly keeps the debit small. Enter when IV rank is still LOW (the inverse signal) ahead of a known event - pre-Budget, pre-RBI, pre-result - so you're long vega before the ramp, place the long inner strangle near the ~16-delta-equivalent body, and size the position for total loss of the debit.

## 69. Broken-Wing Iron Condor
*Range with a lean · Short vega · net credit*

**The idea (intuition).** A normal iron condor with one wing stretched wider than the other. By widening the put wing (here 500 points versus the 300-point call wing), you collect a bigger credit and push your risk onto one side — you're saying "I'm more comfortable being wrong to the upside than the downside," or the reverse, while still running an income trade.

**When & why to use it.** Use a broken wing when you have a mild directional lean inside a range view, or when index skew makes one side's far wing cheap to widen. On NSE, downside puts are pricey, so widening the put wing harvests more credit but leaves a bigger gap to the protective strike — fine if you judge a sharp sell-off unlikely. Skip it if you have no real lean; the standard balanced condor is cleaner.

**How to build it (₹, Nifty).** Sell 24400 CE @ 246, buy 24700 CE @ 135 (call wing 300 wide); sell 23600 PE @ 192, buy 23100 PE @ 98 (put wing 500 wide). Net credit 205.3 points, about ₹15,398 per lot.

![Figure: Broken-Wing Iron Condor payoff at expiry](figs/strategies/broken_wing_iron_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 205 points (₹15,375/lot) between 23600 and 24400. Max loss 295 points (₹22,125/lot), concentrated on the wider put side. Breakevens 23395 and 24605. Net credit 205.3 points; risk:reward 0.70 — the extra credit comes at the cost of a fatter tail on the broken side.

**Greeks & behaviour.** Slight directional delta at entry (the asymmetry tilts it away from delta-neutral). Positive theta, negative vega like any short condor. The wider put wing means downside losses, when they come, are larger and accelerate faster than on the tight call side.

**Management & exit.** Manage at 50% of credit as usual, but watch the broken (wide) side most closely — that's where the damage lives. If Nifty drifts toward the wide put short, roll it up or close early; you cannot afford to let the worst-case side run.

**Risk note.** The honest cost of the extra credit is a max loss well above the credit, all loaded on one side. A gap through the wide put wing is the nightmare scenario — defined, but the largest defined loss in the basic-condor set. Size for that tail, not the average month.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -22,125 | +375 | +15,375 | +375 | -7,125 |

The asymmetry is visible in the tails - a 25,200 print loses only -7,125 on the tight call side, while a 22,800 print loses -22,125 through the wide put wing; the body still pays +15,375.

**Adjustments, variants & timing.** Manage at ~50% of the 205-point credit, but watch the wide (broken) put side hardest - that's where the 295-point loss lives. Close or roll at 21 DTE. If Nifty drifts toward the wide put short, roll it up-and-out or close early; you cannot let the worst-case side run, because a gap through the 500-wide put wing is the nightmare. Defend a breached call short by rolling up-and-out as usual. Keep this on the Nifty monthly - the asymmetric tail needs slow decay and reaction time that Bank Nifty weeklies don't offer. Enter on IV rank above 50-70, place the ~16-delta shorts at ~45 DTE, and widen the wing only on the side you genuinely fear less. Size for the broken-side tail, not the average month: the max loss here is among the largest in the basic condor set, so trim lot count accordingly and respect the higher SPAN on the wide wing.

## 70. Unbalanced Iron Condor
*Directional range · Short vega · net credit*

**The idea (intuition).** Take a standard iron condor and trade extra contracts on one side — here two put spreads against one call spread. The doubled side collects more premium and gives the position a directional tilt: you're leaning bullish (selling more puts) while still capping risk with wings. It's a ratio'd condor that says "range, but I favour the upside."

**When & why to use it.** Deploy when you're range-bound but with a directional bias you want to monetise — e.g. you think Nifty holds 23600 and would rather sell richer downside premium. The extra put spread juices the credit and pulls your delta positive. Don't use it if you can't stomach the larger loss on the doubled side, and never double the side you secretly fear — that's where the contracts pile the risk.

**How to build it (₹, Nifty).** Sell 24400 CE @ 246, buy 24700 CE @ 135 (one call spread); sell 2× 23600 PE @ 192, buy 2× 23300 PE @ 129 (two put spreads). Net credit 237.7 points, about ₹17,828 per lot — fattened by the extra put spread.

![Figure: Unbalanced Iron Condor payoff at expiry](figs/strategies/unbalanced_iron_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 238 points (₹17,850/lot) between 23600 and 24400. Max loss 362 points (₹27,150/lot), concentrated on the doubled put side. Breakevens 23481 and 24638. Net credit 237.7 points; risk:reward 0.66 — the richest credit in the basic set, paid for with the largest downside.

**Greeks & behaviour.** Positive net delta at entry (the extra short puts lean the trade bullish). Strong positive theta from selling more premium; negative vega. The doubled side carries roughly twice the gamma and loss-per-point, so a move against it hurts disproportionately.

**Management & exit.** Manage the doubled side actively — that's where the size is. Take the trade off at ~50% of credit. If Nifty falls toward the short puts, the 2-lot side losses compound fast; roll or close early rather than defend a position that's twice your normal size.

**Risk note.** Ratioing amplifies everything: more credit, but the worst case (~362 points) is the biggest in this group and lands on one side. A gap down through the put shorts is a double-sized hit. Trade it smaller than a balanced condor and respect the SPAN margin on the extra contracts.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -27,150 | -12,150 | +17,850 | +2,850 | -4,650 |

The doubled put side shows up as the worst cell: -27,150 at 22,800 versus just -4,650 at 25,200, with the body paying +17,850 and a 24,600 print still green at +2,850.

**Adjustments, variants & timing.** Ratioing piles risk on the doubled put side, so manage that side actively. Take the trade off at ~50% of the 238-point credit and close or roll by 21 DTE. If Nifty falls toward the short puts, the 2-lot side loses roughly double per point - roll those puts down-and-out or close early rather than defend size that's twice your normal exposure. Never double the side you secretly fear. Run it on the Nifty monthly for reaction time; Bank Nifty weeklies make a doubled, gappy side unmanageable. Enter on IV rank above 50-70 with ~16-delta shorts at ~45 DTE, and crucially size DOWN - trade fewer lots than a balanced condor because the ~362-point worst case is the biggest in this group and a gap down through the put shorts is a double-sized hit. Budget the SPAN margin on the extra contracts and cap the position well under your usual condor risk.

## 71. Iron Condor (Weekly)
*Quiet week · Short vega · net credit*

**The idea (intuition).** The same condor structure, but on a weekly expiry. With only days to run, the options are cheap and decay screams — you're harvesting fast theta over a short window, betting Nifty chops sideways for a week. Quick in, quick out.

**When & why to use it.** Weekly condors suit a calm, news-light week with no scheduled catalyst, where you want to compound small theta repeatedly. NSE weekly expiries (now the dominant retail product) are liquid and let you place tight 200-point wings near 23700-24300. The flip side: with little time value, the credit is small and gamma is brutal near expiry. Avoid weeklies across event days — one surprise in a five-day window leaves no room to recover.

**How to build it (₹, Nifty).** Sell 24300 CE @ 75, buy 24500 CE @ 31; sell 23700 PE @ 71, buy 23500 PE @ 36. Net credit 79.0 points, about ₹5,925 per lot. Wings are 200 points wide.

![Figure: Iron Condor (Weekly) payoff at expiry](figs/strategies/iron_condor_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 79 points (₹5,925/lot) between 23700 and 24300. Max loss 121 points (₹9,075/lot). Breakevens 23621 and 24379 — a tight ±1.6% band for the week. Net credit 79.0 points; risk:reward 0.65 — you risk more than the credit, typical of short-dated wings.

**Greeks & behaviour.** Delta-neutral at entry but extremely gamma-sensitive — with days to go, net delta lurches with every Nifty move. Theta is large relative to the premium (fast decay is the whole appeal); vega is small because little time value remains.

**Management & exit.** Weeklies move fast — take 30-50% of the credit quickly, often within a day or two. There's little time to repair a tested side, so favour closing over rolling. Strongly consider exiting before the final expiry-day gamma spike; the last day can turn a winner into a max-loss on a single swing.

**Risk note.** Gamma risk dominates: the short tenor means breakevens are close and an intraday 1% move can blow through a strike with no time to mean-revert. Small credits and a sub-1 risk:reward mean a single bad week can erase several good ones. Discipline over greed.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -9,075 | -9,075 | +5,925 | -9,075 | -9,075 |

The weekly's small +5,925 credit sits only at the 24,000 pin, with the -9,075 max loss appearing at every other strike in the table - a tight, gamma-heavy band.

**Adjustments, variants & timing.** Weeklies move fast: take 30-50% of the 79-point credit quickly, often within a day or two, and strongly prefer closing over rolling - with days to run there's no time to repair a tested side. The 21-DTE rule collapses to exiting before the final expiry-day gamma spike, which on a weekly can flip a winner to max-loss on one swing. If a short is breached, close; don't chase. This structure naturally lives on Nifty (or Bank Nifty) weeklies, but only in a news-light week - never carry it across an event day, since one surprise in a five-day window leaves no recovery room. Enter when IV rank is elevated relative to the week's expected range, place tight ~200-point wings near the 16-delta shorts, and size small: the sub-1 risk:reward means a single bad week erases several good ones. For a steadier program, prefer the Nifty monthly 45-DTE condor over stacking weeklies.

## 72. Iron Condor (10-delta)
*Strongly range-bound · Short vega · net credit*

**The idea (intuition).** Push the short strikes way out to roughly the 10-delta level — far OTM, low-probability-of-touch options. You're renting a very large room, so Nifty almost always stays inside and you win most months. The price of that comfort: each option is cheap, so the credit is thin while the wings still cover real distance.

**When & why to use it.** The 10-delta condor is the high-probability, low-and-slow income choice — for traders who prioritise hit-rate and a wide margin of safety over big monthly credits. It shines in genuinely range-bound regimes where you want the shorts (here ~24800 / 23200) far from spot. The trade-off, and it's a real one, is a poor risk:reward — the occasional loss is multiples of the credit, so you must avoid the rare disaster and never over-size into the apparent safety.

**How to build it (₹, Nifty).** Sell 24800 CE @ 107, buy 25100 CE @ 46; sell 23200 PE @ 113, buy 22900 PE @ 74. Net credit 98.5 points, about ₹7,388 per lot. Wings are 300 points wide.

![Figure: Iron Condor (10-delta) payoff at expiry](figs/strategies/iron_condor_delta10.png)

**The numbers (modelled at Nifty 24000).** Max profit 98 points (₹7,350/lot) across the wide 23200-24800 zone. Max loss 202 points (₹15,150/lot) — over twice the credit. Breakevens 23102 and 24898, roughly a ±3.7% band. Net credit 98.5 points; risk:reward 0.49 — the lowest in the family, the structural cost of high probability.

**Greeks & behaviour.** Delta-neutral and very low gamma at entry — far-OTM shorts barely react to ordinary Nifty wiggles, so the position sits quietly. Positive theta (slow but steady), negative vega. It behaves like a sleepy bond clipping coupons until a big move suddenly threatens a wing.

**Management & exit.** Because the credit is small, the 50% target comes in absolute terms quickly; many traders hold these closer to expiry to capture more decay, accepting the gamma risk late. The key discipline is the stop: with a 0.49 risk:reward, you cannot let a loser run to max — exit if the loss reaches roughly the credit you collected.

**Risk note.** This is the classic premium-seller's trap: a long string of easy wins, then one trending or gapping month that loses 2× the credit and wipes out a quarter's gains. The far strikes feel safe, which tempts over-sizing — the real danger. Size small, manage the tail.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -15,150 | +7,350 | +7,350 | +7,350 | -15,150 |

The far shorts keep the table green across 23,400-24,600 at +7,350, but the tails at 22,800 and 25,200 each lose -15,150 - over twice the credit.

**Adjustments, variants & timing.** The credit is thin (98 points), so the 50% target arrives quickly in absolute terms; many traders instead hold these closer to expiry to capture more decay, accepting late gamma - but still close or roll by 21 DTE. The non-negotiable discipline is the stop: with a 0.49 risk:reward, exit if the loss reaches roughly the credit collected, because one trending month loses 2x the credit. If a far short is breached, roll it out-and-away or close. Run it on the Nifty monthly where far-OTM strikes still have liquidity; Bank Nifty weeklies have too little time value at the 10-delta. Enter on IV rank above 50-70 so even cheap far options are worth selling, place the ~10-16-delta shorts at ~45 DTE, and above all size small - the far strikes feel safe and tempt over-sizing, which is the real trap. The danger isn't any single month; it's the rare gap that wipes a quarter of wins.

## 73. Bullish Skewed Condor
*Drift up within a range · Short vega · net debit*

**The idea (intuition).** A condor whose entire body is shifted above the current spot. Built from calls, with the flat profit top sitting north of 24000, it pays best if Nifty drifts gently higher and parks in the 24300-24600 zone. It's a range trade with a built-in upward bias.

**When & why to use it.** Reach for it when you expect a mild grind higher that stalls inside a band — a slow risk-on drift, not a breakout. The skew lets you target where you think Nifty settles rather than assuming it pins the current price. Use it when you have a soft bullish view but not enough conviction to buy a directional call spread outright. Don't use it if you expect a sharp rally (you'll cap out and miss the move) or a drop (the body is above you, so a fall is the loss zone).

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24300 CE @ 292, sell 24600 CE @ 167, buy 24900 CE @ 83. Net debit 79.4 points, about ₹5,955 paid per lot. The body straddles 24300-24600, above spot.

![Figure: Bullish Skewed Condor payoff at expiry](figs/strategies/condor_skewed_bull.png)

**The numbers (modelled at Nifty 24000).** Max profit 221 points (₹16,575/lot) if Nifty expires between 24300 and 24600. Max loss is the 79-point debit (₹5,925/lot) beyond the outer strikes. Breakevens 24079 and 24821 — note both sit above current spot, so Nifty must rise just to reach the profit tent. Net debit 79.4 points; risk:reward 2.78.

**Greeks & behaviour.** Net positive delta at entry — the shifted body gives it a bullish tilt that you want to play out toward 24450. Theta turns favourable once price climbs into the body; vega is negative. Early on, while Nifty is below the structure, the position behaves like a patient bullish range bet.

**Management & exit.** This needs Nifty to cooperate by drifting up. If it rallies into the body, scale out as you approach a good share of the 221-point max. If it stalls below 24079 or sells off, the trade leaks toward its capped loss — cut it; the thesis (drift up) is simply wrong.

**Risk note.** Defined risk equal to the small debit, but the directional skew means you need both range AND a modest up-move; a flat market that never reaches 24300 still loses. You're paying a debit for a specific outcome — be right on the destination, not just the calm.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -5,925 | -5,925 | -5,925 | +16,575 | -5,925 |

The upward skew is obvious: the +16,575 peak sits in the 24,600 column, not 24,000, while every other outcome including a flat 24,000 close books the -5,925 debit.

**Adjustments, variants & timing.** This needs Nifty to cooperate by drifting up into the 24300-24600 body. If it rallies in, scale out at 50-60% of the 221-point max; you won't bank the full tent without an expiry pin, so roll or close by 21 DTE rather than risk a reversal in gamma week. If Nifty stalls below the lower breakeven (24079) or sells off, the thesis is simply wrong - cut to the capped debit. There's no rolling a tested short in the credit sense here; management is directional, so treat a failed drift as a stop. Build it on the Nifty monthly where the call body has depth; Bank Nifty weeklies are too jumpy for a precise destination bet. Enter when IV rank is moderate-to-high (>50-70) so the short body is rich, place the shifted body around the ~16-delta band above spot at ~45 DTE, and size for the debit as total loss - you're paying for a specific destination, not just calm.

## 74. Bearish Skewed Condor
*Drift down within a range · Short vega · net debit*

**The idea (intuition).** The mirror of the bullish skew: a put-built condor with its flat top shifted below spot, around 23400-23700. It pays best if Nifty eases gently lower and settles in that zone. A range trade with a downward lean, for when you think the market drifts off but doesn't crash.

**When & why to use it.** Use it on a soft, distribution-y tape — Nifty leaking lower on tired momentum, no panic — where you expect price to settle a few hundred points below current. The downside put skew on NSE indices actually helps you here: richer puts let you build the body for a smaller net debit, which is why this structure shows the best risk:reward in the group. Avoid it if you fear a genuine crash (you'll cap out short of it) or expect a bounce (the body is below you).

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 23700 PE @ 219, sell 23400 PE @ 148, buy 23100 PE @ 98. Net debit 50.0 points, about ₹3,750 paid per lot. The body sits at 23400-23700, below spot.

![Figure: Bearish Skewed Condor payoff at expiry](figs/strategies/condor_skewed_bear.png)

**The numbers (modelled at Nifty 24000).** Max profit 250 points (₹18,750/lot) if Nifty expires between 23400 and 23700. Max loss is the 50-point debit (₹3,750/lot) beyond the outer strikes. Breakevens 23150 and 23950 — both below spot, so Nifty must fall to reach the tent. Net debit 50.0 points; risk:reward 5.00 — the highest in the entire group, courtesy of cheap construction off the put skew.

**Greeks & behaviour.** Net negative delta at entry — a bearish tilt aimed at a drift toward ~23550. Theta becomes your friend once price is inside the body; vega is negative, so a fear-driven IV spike (common on down-moves) works against the position even as direction goes your way. That tension is the thing to watch.

**Management & exit.** You need a controlled drift lower, not a vol explosion. If Nifty eases into the body, scale out toward the 250-point max. If it bounces above 23950 or crashes through 23150, take the small capped loss — either way the "gentle drift down" thesis has failed.

**Risk note.** Tiny defined risk (₹3,750/lot) and a superb headline risk:reward, but the catch is conditionality: you need range AND a measured down-move. A flat market that holds 24000, or a violent crash that overshoots the body, both leave you with the loss. Cheap, but specific.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -3,750 | +18,750 | -3,750 | -3,750 | -3,750 |

The downward skew puts the +18,750 peak in the 23,400 column; a flat 24,000 close and every other strike lose the tiny -3,750 debit.

**Adjustments, variants & timing.** Management is directional: you need a controlled drift into the 23400-23700 body, not a vol explosion. If Nifty eases in, scale out at 50-60% of the 250-point max and roll or close by 21 DTE rather than chase the full tent through gamma week. If it bounces above the upper breakeven (23950) or crashes through 23150, the gentle-drift-down thesis has failed - take the tiny Rs 3,750 capped loss. Build it on the Nifty monthly, where the persistent index put skew lets you construct the body for the cheapest debit in the group; Bank Nifty weeklies sacrifice that skew edge. Enter when IV rank is above 50-70 so the short body is rich, place the shifted put body around the ~16-delta zone below spot at ~45 DTE, and size for the debit as total loss. Watch the tension: a fear-driven IV spike on a down-move hurts the negative-vega structure even as direction goes your way.

## 75. Iron Condor (45-DTE)
*Range-bound · Short vega · net credit*

**The idea (intuition).** The textbook premium-selling condor: ~16-delta shorts, balanced wings, and roughly 45 days to expiry. That tenor is the sweet spot where time decay is meaningful but expiry-week gamma is still far away — the structure most studied and traded by systematic income desks.

**When & why to use it.** This is the strategy you reach for to run a repeatable monthly income program. Enter when IV rank is high (the classic guidance is IV rank > 50, ideally after a vol spike), sell the ~45-DTE expiry, and let theta work in the calm middle of the cycle. On NSE you'd use the monthly series rather than the weeklies for this. The whole edge is selling rich premium and managing mechanically; don't run it in low-IV regimes where the credit doesn't compensate for the risk.

**How to build it (₹, Nifty).** Sell 24500 CE @ 305, buy 24900 CE @ 153; sell 23500 PE @ 227, buy 23100 PE @ 150. Net credit 228.9 points, about ₹17,168 per lot. Wings are 400 points wide; the longer tenor and ~16-delta shorts give the fatter premium.

![Figure: Iron Condor (45-DTE) payoff at expiry](figs/strategies/iron_condor_45d.png)

**The numbers (modelled at Nifty 24000).** Max profit 229 points (₹17,175/lot) between 23500 and 24500. Max loss 171 points (₹12,825/lot). Breakevens 23271 and 24729 — a roomy ±3% band. Net credit 228.9 points; risk:reward 1.34 — the credit exceeds the risk, a healthy, balanced profile.

**Greeks & behaviour.** Delta-neutral at entry. With 45 days on, gamma is low and the position is forgiving — net delta drifts slowly, giving you time to adjust. Theta is positive and accelerates as expiry nears; vega is negative, so the trade benefits from the IV mean-reversion you entered to capture.

**Management & exit.** This is the home of the manage-at-50% rule: close (or roll out to the next 45-DTE cycle) once you've captured ~50% of the 229-point credit, typically with 2-3 weeks left. Defend a tested side by rolling the untested spread in, and exit before the position enters expiry-week gamma — the low-gamma comfort of 45 DTE evaporates in the final days.

**Risk note.** The most balanced condor here, but still short premium: a trending month or a vol spike can push it to a 171-point loss, and the worst losses arrive near a short strike where gamma bites. The 45-DTE structure buys you reaction time — use it, don't sit frozen.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -12,825 | +9,675 | +17,175 | +9,675 | -12,825 |

The balanced 45-DTE profile pays +17,175 at the 24,000 pin and stays green at +9,675 across 23,400-24,600, with the -12,825 max loss reserved for the 22,800 / 25,200 tails.

**Adjustments, variants & timing.** This is the home of the manage-at-50% rule: buy the condor back once you've captured ~50% of the 229-point credit, typically with 2-3 weeks left, and as a hard rule close or roll to the next 45-DTE cycle at 21 DTE - the low-gamma comfort of 45 DTE evaporates in the final days. Defend a tested side by rolling the untested spread in to recentre; if a short's delta doubles toward 30, roll that spread out-and-away. Run it on the Nifty monthly series, not Bank Nifty weeklies - the 45-DTE tenor and ~16-delta shorts are designed for the monthly. Enter strictly on IV rank above 50 (ideally after a vol spike) so the credit compensates for the risk; in low-IV regimes, stand aside. Size so a max-loss month (171 points, Rs 12,825) costs 1-2% of capital. The 45 days buy reaction time - use it, don't sit frozen near a tested strike.

## 76. Wide Call Condor
*Broad range · Short vega · net debit*

**The idea (intuition).** An all-call condor stretched wide — 400-point strike spacing — so the flat profit top spans a generous band. You're betting Nifty stays inside a large range, and the width buys you a comfortable cushion on both sides for a modest debit.

**When & why to use it.** Use it when you want condor economics with a wide margin of safety and you expect Nifty to roam but stay broadly contained over the cycle. The wide flat top (24400-24700) means you don't need a precise pin to profit, just containment. It's a good fit when call-side liquidity is strong and you'd rather pay a defined debit than manage a credit's margin. Skip it if you expect a real trend that runs past 24978 or below 24122.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24400 CE @ 246, sell 24700 CE @ 135, buy 25100 CE @ 46. Net debit 121.8 points, about ₹9,135 paid per lot. Strikes span a wide 24000-25100.

![Figure: Wide Call Condor payoff at expiry](figs/strategies/wide_call_condor.png)

**The numbers (modelled at Nifty 24000).** Max profit 278 points (₹20,850/lot) when Nifty expires between 24400 and 24700, the wide flat top. Max loss is the 122-point debit (₹9,150/lot) beyond the outer wings. Breakevens 24122 and 24978. Net debit 121.8 points; risk:reward 2.28 — solid, with loss capped at the premium paid.

**Greeks & behaviour.** Slight positive delta at entry because the body sits a touch above spot. Positive theta once Nifty is inside the body; negative vega. The wide construction keeps gamma low, so the position is calm and forgiving until price nears an outer wing.

**Management & exit.** Like other debit condors, you rarely bank the full 278 points without a clean expiry settle in the body — scale out as you reach a good share of max profit. If Nifty trends toward an outer strike, the trade drifts to its capped loss; recycle the capital. The wide top gives you patience the narrow condors don't.

**Risk note.** Risk is fully defined at the 122-point debit, and the broad profit zone makes for a high-probability range bet. The catch is the four-leg call build: spreads and slippage matter, and the headline max profit needs Nifty to settle inside a band it may only pass through. A real breakout simply caps you at the small loss.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -9,150 | -9,150 | -9,150 | +20,850 | -9,150 |

The wide call body peaks at +20,850 in the 24,600 column and caps every other outcome at the -9,150 debit, including a flat 24,000 close that hasn't yet reached the tent.

**Adjustments, variants & timing.** Loss is capped at the 122-point debit, so manage for profit. You rarely bank the full 278 points without a clean expiry settle in the 24400-24700 body - scale out at 50-60% of max and roll the four-leg structure to the next cycle near 21 DTE rather than let it decay into expiry gamma. If Nifty trends toward an outer wing, the trade drifts to its capped loss; recycle the capital. The wide top gives patience the narrow condors lack. Build it on the Nifty monthly where call-side liquidity is strong and four-leg slippage is smallest; Bank Nifty's wider spreads erode the edge. Enter when IV rank is elevated (>50-70) so the short body is rich, place the body around the ~16-delta band at ~45 DTE, and size for the debit as total loss. A genuine breakout past 24978 or below 24122 simply caps you at the small loss - accept that as the cost of a high-probability range bet.

## 77. Reverse Iron Condor (Weekly Event)
*Weekly breakout · Long vega · net debit*

**The idea (intuition).** A reverse iron condor on a weekly expiry, built to capture a big move around a near-term event. Buy the inner strangle, sell the outer wings, and profit if Nifty breaks hard either way within the week. It's a cheap, defined-risk long-vol punt on a catalyst.

**When & why to use it.** This is an event trade: a weekly with a known binary in it — a major data print, a policy decision, a results-heavy session — where you expect a sharp move but not the direction, and you want to be long volatility before the IV ramp. The weekly tenor keeps the debit small. The danger is the same that haunts all long-vol structures: if the event fizzles, theta and the post-event IV crush gut the position in days. Never hold it through a quiet, eventless week.

**How to build it (₹, Nifty).** Buy 24300 CE @ 75, sell 24600 CE @ 18; buy 23700 PE @ 71, sell 23400 PE @ 25. Net debit 102.7 points, about ₹7,703 paid per lot. Wings are 300 points wide.

![Figure: Reverse Iron Condor (Weekly Event) payoff at expiry](figs/strategies/reverse_iron_condor_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 197 points (₹14,775/lot) if Nifty breaks beyond a wing (above 24600 or below 23400). Max loss is the 103-point debit (₹7,725/lot) if it expires inside the body near 24000. Breakevens 23597 and 24403 — Nifty must move ~1.7% to clear them. Net debit 102.7 points; risk:reward 1.92 — a favourable payoff if the breakout comes.

**Greeks & behaviour.** Delta-neutral at entry but long gamma — it springs to life as Nifty accelerates from 24000. Theta is negative (a fast bleed on a weekly) and vega is positive, so a pre-event IV expansion helps even before price moves. Everything is the inverse of the income condor.

**Management & exit.** This is a hit-and-run trade. If the event delivers a move, take profits into the spike within a day — don't wait for the full wing. If the catalyst passes and Nifty sits in the body, cut immediately; on a weekly, the combined theta-plus-IV-crush decay is merciless and there's no time to recover.

**Risk note.** The lethal combination is being right on a small move but losing anyway, because IV crush after the event outweighs the modest price travel. On a five-day clock there's no margin for a slow burn. Treat it strictly as a short-window event play sized for total loss of the debit.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +14,775 | +14,775 | -7,725 | +14,775 | +14,775 |

The long-vol weekly inverts the pattern: the table pays +14,775 at every strike except the 24,000 body, where it takes the -7,725 debit as max loss.

**Adjustments, variants & timing.** Strictly hit-and-run. If the event delivers a move, take profits into the spike within a day - don't wait for the full wing; effectively bank ~50% of the move and leave. If the catalyst passes and Nifty sits in the body near 24000, cut immediately: on a five-day clock, theta plus post-event IV crush gut the position with no recovery time, so there's no 21-DTE grace - exit on the event, win or lose. This lives on Nifty or Bank Nifty weeklies by design, around a known binary; never hold it through a quiet, eventless week. The entry signal inverts the income rules: enter when IV rank is still LOW ahead of the catalyst so you're long vega before the ramp, place the long inner strangle near the ~16-delta-equivalent body, and size the whole position for total loss of the 103-point debit. The lethal case is a small right-way move swamped by IV crush - plan for it.

## 78. Iron Condor (Credit-Skewed)
*Range with put skew · Short vega · net credit*

**The idea (intuition).** An iron condor deliberately built asymmetrically to harvest index skew: a tighter call spread up top and a wider put spread below. Because NSE puts carry richer implied vol, leaning the structure toward the put side lets you bank extra credit for the same neutral range view.

**When & why to use it.** Use it when you want standard condor income but with the construction tuned to NSE's persistent put skew — selling the relatively expensive downside while keeping the upside tight. It suits a range-bound market where you're comfortable carrying slightly more risk on the put side in exchange for a better credit. Don't deploy it if you fear a downside break; the wider put wing means a larger loss exactly where index sell-offs tend to go.

**How to build it (₹, Nifty).** Sell 24350 CE @ 268, buy 24550 CE @ 185 (call wing 200 wide); sell 23550 PE @ 180, buy 23250 PE @ 120 (put wing 300 wide). Net credit 142.7 points, about ₹10,703 per lot.

![Figure: Iron Condor (Credit-Skewed) payoff at expiry](figs/strategies/iron_condor_unbalanced_credit.png)

**The numbers (modelled at Nifty 24000).** Max profit 143 points (₹10,725/lot) between 23550 and 24350. Max loss 157 points (₹11,775/lot), the larger figure sitting on the wider put wing. Breakevens 23407 and 24493. Net credit 142.7 points; risk:reward 0.91 — close to even, with the asymmetry buying extra credit at the cost of a slightly larger put-side loss.

**Greeks & behaviour.** Modestly non-neutral delta at entry from the asymmetric wings. Positive theta and negative vega like any short condor — and because the put wing is wider, a down-move both moves delta against you and threatens the bigger loss. The skew you harvested cuts both ways.

**Management & exit.** Manage at ~50% of the credit, watching the put side most closely since that's where the larger loss lives. If Nifty drifts toward the short put, roll it up or close early. The tighter call side is cheaper to defend, so the upside rarely needs much attention.

**Risk note.** You're paid extra for accepting more downside risk — be honest that a fast Nifty sell-off (the move puts are priced for) lands you on the wider, costlier wing. Defined risk, but the danger is concentrated precisely where index gaps tend to occur. Size for the put-side tail.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -11,775 | -525 | +10,725 | -4,275 | -4,275 |

The credit skew shows in the asymmetric tails - a 22,800 print loses -11,775 on the wider put side versus -4,275 at 25,200, while the body pays +10,725 and a 23,400 close nearly breaks even at -525.

**Adjustments, variants & timing.** Manage at ~50% of the 143-point credit, watching the wider put side most closely since the larger 157-point loss sits there. Close or roll at 21 DTE. If Nifty drifts toward the short put, roll it up-and-out or close early; the tighter call side is cheaper to defend and rarely needs attention. A breached put short is the real risk - roll down-and-out only if it cuts exposure. Run it on the Nifty monthly, where the persistent index put skew you're harvesting is most reliable; Bank Nifty weeklies are too gappy to lean asymmetrically into. Enter on IV rank above 50-70, sell the relatively expensive ~16-delta downside while keeping the upside tight, at ~45 DTE. Size for the put-side tail, not the average month: a fast Nifty sell-off - exactly the move puts are priced for - lands you on the wider, costlier wing, so trim lots and respect the larger SPAN on the wide put spread.

