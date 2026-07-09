# Strategy Group 4: Butterflies

Butterflies are cheap, fully defined-risk bets on *where* the index will sit at expiry rather than *which way* it moves. Every one is built from three strikes — buy one wing, sell two of a body, buy the other wing — so the structure is self-financing enough to cost a few points and pay a multiple of that if spot "pins" the body. The family's unifying trade-off is probability versus payoff: the tent only pays in full at one exact strike, so you accept a low hit-rate in exchange for a fat reward-to-risk ratio, and you can tilt, widen, narrow, or break a wing to trade direction, IV, and the width of your target zone.

## 43. Long Call Butterfly
*Pin near body strike · Short vega · net debit*

**The idea (intuition).** Think of it as renting a tent pitched over the 24000 strike: you pay a small fixed rent and collect a payout that peaks if the index camps exactly at the centre pole by expiry. Buy one in-the-money call, sell two at the body, buy one out-of-the-money call — the two short calls fund most of the structure, leaving you a tiny bill and a capped, generous upside.

**When & why to use it.** Use it when you have a precise level in mind and expect the index to gravitate there into expiry — a consolidating Nifty, a max-pain pin, or a post-event drift after IV has already collapsed. It is short vega, so it is happiest entered when IV is elevated and likely to fall (India VIX spiking into a known event), because falling IV pulls the body back toward intrinsic and fattens the tent. Avoid it when a strong trend or a fresh catalyst (Budget, RBI, results) can blow the index clean through a wing.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655, sell 2x 24000 CE @ 456, buy 24300 CE @ 292. Net debit 34.8 points, about ₹2,610 per lot (34.8 × 75) — that is your entire risk.

![Figure: Long Call Butterfly payoff at expiry](figs/strategies/long_call_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 257 points (~₹19,275/lot) if Nifty finishes exactly at 24000. Max loss 35 points (~₹2,625/lot) outside the wings. Breakevens 23735 and 24265. Net debit 34.8 points. Risk:reward 7.38 — you risk one to make roughly seven.

**Greeks & behaviour.** Near the body net delta is close to flat; it leans slightly directional as spot wanders off-centre. Theta is your friend once price sits inside the tent — time decay drags the payoff up toward the peak. Vega is negative, so a drop in IV helps; a spike hurts before expiry.

**Management & exit.** Treat it as a hold-to-decay trade but do not be greedy: the centre value only materialises in the last day or two, so booking 40-60% of the modelled max when spot is parked on the body is sensible. If price runs to a wing early, the position is cheap enough to let expire, or roll the whole fly to recentre on the new level.

**Risk note.** The honest danger is whipsaw: the tent is narrow, so a single trending session can push spot past a breakeven and turn the trade into a near-total loss of the 35-point debit. It is cheap, but the probability of a perfect pin is genuinely low.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹2,625 | -₹2,625 | +₹19,875 | -₹2,625 | -₹2,625 |

The table shows the full +₹19,875 peak only in the 24,000 column, with every other strike on this ±5% grid handing back the –₹2,625 debit — a stark picture of how narrowly the body must be pinned.

**Adjustments, variants & timing.** The cleanest adjustment is to roll the body to follow price: if Nifty drifts from 24000 toward 24200, close the 24000 body and re-sell the 24200 strike, re-centring the tent on the new pin. If a move is gathering pace you can leg into wider wings to buy room, or convert to a broken-wing by pushing one outer strike out a strike and skipping one — that cheapens the structure into a near-credit and erases the loss zone on the side you no longer fear. On NSE this fly suits a Nifty monthly expiry-week pin trade better than a Bank Nifty weekly, where larger point swings breach the narrow body too often. Place the body at the heaviest open-interest / max-pain strike rather than spot, and enter in the last five to seven sessions when India VIX has already cooled — butterflies shine in the final week as gamma and pinning, not direction, drive the close.


## 44. Long Put Butterfly
*Pin near body strike · Short vega · net debit*

**The idea (intuition).** The put-built twin of the call butterfly: same tent, same peak over 24000, just assembled from puts instead of calls. By put-call parity the expiry payoff is identical, so you choose puts when their strikes are more liquid or better priced, or when you simply prefer holding puts into a falling tape.

**When & why to use it.** Identical conditions to the long call fly — a precise pin expectation into expiry, ideally with IV elevated and set to fade. Desk traders often pick the put version on the downside skew side of the chain, where OTM puts carry richer premium and the short body collects more. Skip it when a trend or catalyst threatens to drive Nifty through either wing.

**How to build it (₹, Nifty).** Buy 24300 PE @ 453, sell 2x 24000 PE @ 318, buy 23700 PE @ 219. Net debit 34.8 points, about ₹2,610 per lot — and that debit is the whole risk.

![Figure: Long Put Butterfly payoff at expiry](figs/strategies/long_put_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 257 points (~₹19,275/lot) at a 24000 finish. Max loss 35 points (~₹2,625/lot) beyond the wings. Breakevens 23735 and 24265. Net debit 34.8 points. Risk:reward 7.38.

**Greeks & behaviour.** Net delta hovers near zero at the body and tilts as spot drifts. Theta works for you inside the tent, pulling the mark toward the peak as expiry nears. Vega is negative — falling IV is a tailwind, rising IV a drag before expiry.

**Management & exit.** Same discipline as the call fly: this is a decay play whose value concentrates in the final sessions. Book 40-60% of the modelled peak if Nifty sits on the body with a few days left; let it expire if it drifts to a wing, since the cost is trivial. Roll to recentre if your view of the pin level shifts. On NSE the put strikes around and below ATM often quote tighter spreads than the equivalent calls, so legging in on the put chain can shave a point or two off entry — worth doing when liquidity is thin in the back-month.

**Risk note.** Low probability of a clean pin is the core risk. The position is cheap and capped, but a trending move past a breakeven converts most of the 35-point debit into a loss. Because you hold three different put strikes, watch the bid-ask on the wings near expiry — illiquid OTM puts can make exit prints worse than the screen suggests. Treat the high 7.38 reward:risk as a lottery-like edge, not a base case.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹2,625 | -₹2,625 | +₹19,875 | -₹2,625 | -₹2,625 |

Identical to its call-built twin, the +₹19,875 maximum appears solely at 24,000 while the 22,800–23,400 and 24,600–25,200 wings each forfeit the –₹2,625 debit, underscoring the low-probability nature of a clean pin.

**Adjustments, variants & timing.** Manage it exactly as the call version, with the put chain's quirks in mind. The core adjustment is rolling the body down or up to chase the developing pin, re-selling the 24000 puts at the strike open interest is migrating toward. If the tape trends, leg into wider put wings for breathing room, or skip a lower strike to break the wing into a credit and shed the downside loss zone. On NSE the sub-ATM put strikes usually quote tighter than the equivalent calls, so this build is the better vehicle for a Nifty monthly expiry-week pin where fills matter; Bank Nifty weeklies move too violently relative to the body. Anchor the body on the max-pain / peak-put-OI strike, not raw spot, and put the trade on in the final week once India VIX has deflated post-event — the last few sessions are when theta and pinning, rather than vega, do the heavy lifting.


## 45. Short Call Butterfly
*Move away from body · Long vega · net credit*

**The idea (intuition).** Flip the long butterfly upside down. You sell the wings and buy the body, collecting a small credit, and you *want* the index to leave the 24000 zone in either direction. It is a defined-risk way to fade a pin — betting the market refuses to sit still.

**When & why to use it.** Use it when you expect a breakout but are unsure of direction, and when IV is low and likely to rise — it is long vega, so an expansion in India VIX (ahead of results season, a policy event, a global risk-off) lifts the position. It is the inverse of the income trade, so deploy it when premium-sellers are crowded and you suspect the consensus pin will break. Avoid it in a dead, range-bound tape where time decay grinds you toward max loss.

**How to build it (₹, Nifty).** Sell 23700 CE @ 655, buy 2x 24000 CE @ 456, sell 24300 CE @ 292. Net credit 34.8 points, about ₹2,610 per lot received.

![Figure: Short Call Butterfly payoff at expiry](figs/strategies/short_call_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 35 points (~₹2,625/lot) if Nifty finishes outside the wings. Max loss 257 points (~₹19,275/lot) if it pins exactly at 24000. Breakevens 23735 and 24265. Net credit 34.8 points. Risk:reward 0.14 — you risk roughly seven to make one, the mirror of the long fly.

**Greeks & behaviour.** Delta near zero at the body. Theta is negative — time decay hurts, because the structure loses as spot is dragged toward the body over time. Vega is positive, so rising IV helps and IV crush is your enemy.

**Management & exit.** The credit is small and the worst case large, so this is a tactical, short-horizon trade. Take profit quickly if the index breaks out and the position approaches the 35-point cap; cut it well before expiry-week gamma if spot stalls at the body, rather than risk the full 257-point loss. In practice few desks trade the short butterfly outright — it is more useful as the conceptual inverse that explains why the long fly is priced as cheaply as it is.

**Risk note.** The risk geometry is brutal: a quiet, pinned market hands you the maximum 257-point loss for a 35-point credit. Position tiny and treat it as a low-probability volatility bet, never as steady income. Note the credit here is not the kind of premium you "keep" — it is dwarfed by the pinning risk, so do not confuse this with an income trade.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹2,625 | +₹2,625 | -₹19,875 | +₹2,625 | +₹2,625 |

Mirror-imaged, the short fly collects a tidy +₹2,625 at every grid point except 24,000, where a pin inflicts the –₹19,875 maximum loss — the ±5% grid happens to straddle exactly the strike you fear.

**Adjustments, variants & timing.** Because this is the inverted, long-vol fly, adjustments run the other way: if Nifty stalls on the body you want out, not deeper in. The practical move is to leg out of the bought body and keep the short wings as a cheap strangle if a breakout finally fires, or convert to an outright debit fly if your pin view flips. It is rarely worth running on a Nifty monthly into expiry week, where decay drags you to max loss; if you trade it at all, a Bank Nifty weekly ahead of a catalyst gives the explosive move it needs. Place it away from max-pain, not on it — you are fading the pin. Enter when India VIX is low and set to expand, never in the last sleepy sessions when gamma and pinning crush long-vol structures; this is the one fly in the family that does not want the quiet expiry-week tape.


## 46. Iron Butterfly
*Pin near ATM, high IV · Short vega · net credit*

**The idea (intuition).** Sell an at-the-money straddle for rich premium, then buy a call and a put wing to cap the disaster on both sides. The result is a credit-collected tent: you keep the most if Nifty pins 24000, and your loss is bounded by the wings. It is the income trader's butterfly.

**When & why to use it.** This is a high-IV, expect-a-pin trade. Sell it when IV rank is high — after a Budget-day or results-driven volatility spike, with India VIX elevated and likely to mean-revert — so the short straddle collects fat premium that decays in your favour. Best in the back half of a monthly cycle on a range-bound index. Do NOT sell it into a building trend or just before a fresh catalyst that can gap spot past a wing.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 24300 CE @ 292, buy 23700 PE @ 219. Net credit 263.5 points, about ₹19,763 per lot received up front.

![Figure: Iron Butterfly payoff at expiry](figs/strategies/iron_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 255 points (~₹19,125/lot) at a 24000 pin — essentially keeping the credit. Max loss 36 points (~₹2,700/lot) beyond a wing. Breakevens 23736 and 24264. Net credit 263.5 points. Risk:reward 6.99.

**Greeks & behaviour.** Delta near flat at the body. Theta is strongly positive — this is a decay engine, and time is your ally. Vega is negative, so falling IV after a spike accelerates profit; a fresh IV expansion works against you.

**Management & exit.** Standard income discipline: close at roughly 50% of the max credit rather than squeezing the last points, since gamma risk explodes in expiry week. If a side is tested, roll the untested wing in for more credit or roll the whole structure out and recentre. Exit before the final two sessions to dodge pin-and-gap risk.

**Risk note.** The narrow tent means even a moderate trending move puts you at the breakeven fast; the defined 36-point loss is comforting, but it triggers easily. Assignment risk on the short ATM options exists near expiry if they go in-the-money — manage early. Remember the breakevens sit barely 264 points either side of spot, roughly a single trending session in Nifty, so the rich 263.5-point credit is genuinely at risk, not free.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹2,700 | -₹2,700 | +₹19,800 | -₹2,700 | -₹2,700 |

The credit is kept in full (+₹19,800) only if Nifty pins 24,000; the 600-point and 1,200-point moves on either side all surrender the defined –₹2,700, showing how tightly the income depends on a central settle.

**Adjustments, variants & timing.** The standard repair is to roll the untested wing inward for extra credit when one side is threatened, or roll the whole structure out to the next expiry and re-centre on the new pin. If Nifty trends, convert to a broken-wing iron fly by moving one wing further out, shifting risk to the side you fear less and harvesting more credit. This is a Nifty monthly back-half trade by temperament — sell it once India VIX has spiked and is mean-reverting so the ATM straddle decays in your favour; Bank Nifty weeklies carry richer premium but breach the tight body far more often, so size down there. Centre the short straddle on the max-pain strike rather than spot, and put it on in the final one to two weeks when theta dominates. Flatten before the last two sessions to dodge pin-and-gap and short-ATM assignment risk on in-the-money legs.


## 47. Reverse Iron Butterfly
*Big move from ATM · Long vega · net debit*

**The idea (intuition).** Buy the at-the-money straddle and sell wings to part-fund it. You now own a defined-risk long-volatility tent that pays if Nifty makes a real move away from 24000 in either direction. It is the long-vol cousin of the iron fly.

**When & why to use it.** Use it ahead of a known binary catalyst when IV is still cheap — pre-results, pre-RBI, pre-election-count — where you expect a sharp directional resolution but cannot call the side. Being long vega, an IV ramp into the event helps even before the move. Avoid it in a sleepy, range-bound market: theta bleeds you toward max loss while spot sits on the body.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, buy 24000 PE @ 318, sell 24300 CE @ 292, sell 23700 PE @ 219. Net debit 263.5 points, about ₹19,763 per lot at risk.

![Figure: Reverse Iron Butterfly payoff at expiry](figs/strategies/reverse_iron_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 36 points (~₹2,700/lot) on a move beyond a wing. Max loss 255 points (~₹19,125/lot) if Nifty pins 24000. Breakevens 23736 and 24264. Net debit 263.5 points. Risk:reward 0.14.

**Greeks & behaviour.** Delta near zero at entry, turning directional as spot moves off the body. Theta is negative — every quiet day costs you. Vega is positive, so an IV spike into the event is a tailwind and IV crush after a non-event is the killer.

**Management & exit.** This is an event trade with a short fuse. Take profit fast on a clean breakout toward a wing; do not hold through the post-event IV crush hoping for more. If the catalyst passes with no move, cut quickly — the 255-point loss builds as theta and falling IV combine.

**Management & exit (continued).** Because the profit is capped at just 36 points while the debit risked is 263.5, the math only works if you exit on the vol expansion or the initial thrust, not at expiry. Many traders prefer a plain long straddle here unless they specifically want the defined-risk cap; the short wings finance the position but throttle the upside hard.

**Risk note.** The payoff is unforgiving for the patient: a pinned, low-vol outcome delivers the maximum 255-point loss. The capped 36-point profit also means even a correct breakout pays modestly, so the edge depends on a large, fast move plus an IV tailwind — a demanding combination that often does not arrive.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹2,700 | +₹2,700 | -₹19,800 | +₹2,700 | +₹2,700 |

Reversed, the structure pays a capped +₹2,700 at every wing but loses the full –₹19,800 if Nifty pins 24,000 — the ±5% grid straddles the body, so any of these outer strikes is the outcome you want.

**Adjustments, variants & timing.** As a long-vol debit tent, the only good adjustments are exits: bank the move the instant a breakout reaches a wing, or leg off the short wings to hold a clean long straddle if you want open-ended upside. If the catalyst misfires, cut at once rather than rolling — there is no decay-friendly repair for a structure that bleeds theta daily. It is an event tool, so a Bank Nifty weekly or a Nifty expiry-week straddling a binary catalyst (results, RBI, election count) is its natural home; never run it on a quiet monthly. Place the body on spot, not max-pain — you are betting against the pin. Enter while India VIX is still cheap and ramping into the event, because being long vega the IV build helps before price even moves, and the post-event crush is exactly what guts it if you overstay. Speed of exit, not pin precision, defines the trade.


## 48. Broken-Wing Call Butterfly
*Bullish pin, no upside risk · Short vega · net credit*

**The idea (intuition).** Take a long call butterfly and push the upper wing further out, skipping a strike. Widening that wing lowers its cost so much that the whole structure flips to a *credit*, and — crucially — it erases the loss zone on the upside. You are paid to hold a bullish-leaning tent with risk only on one side.

**When & why to use it.** Use it when you are neutral-to-bullish and want a no-cost or paid bet on a pin near or above spot, with the comfort that an upside breakout no longer hurts. Good in a grinding-higher Nifty where downside surprises are the real worry. Short vega, so elevated IV that fades into expiry helps. Avoid it if your main fear is a sharp drop, since the residual risk sits on the downside.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655, sell 2x 24000 CE @ 456, buy 24500 CE @ 204 (the skipped, wider upper wing). Net credit 52.9 points, about ₹3,968 per lot received.

![Figure: Broken-Wing Call Butterfly payoff at expiry](figs/strategies/broken_wing_call_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 344 points (~₹25,800/lot) at a 24000 pin. Max loss 147 points (~₹11,025/lot) on the downside. Single breakeven 24353. Net credit 52.9 points. Risk:reward 2.34 — and note there is no upside loss zone, so a rally above the wings still leaves you the credit.

**Greeks & behaviour.** Slight bullish delta from the skewed wing. Theta is positive inside the tent. Vega is negative — falling IV helps, a spike hurts before expiry.

**Management & exit.** Because the upside is risk-free, you can let a rally run and keep the credit. Manage the downside: if Nifty breaks lower toward the 147-point loss, close or roll the body down. Book partial profit if spot pins the body with the credit already in hand.

**Risk note.** The trade-off for removing upside risk is a larger, asymmetric downside loss (147 points) concentrated below the body — a sharp sell-off is the danger. The credit is small comfort against that, so size for the downside tail. The honest way to read a broken-wing credit fly: you are not paid for free; you have sold away the protection on one side and concentrated all the risk on the other, and the credit is simply the market's price for that lopsided exposure.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹3,975 | +₹3,975 | +₹26,475 | -₹11,025 | -₹11,025 |

The +₹26,475 peak sits at 24,000, the lower strikes (22,800/23,400) retain the +₹3,975 credit, but the 24,600 and 25,200 columns show a –₹11,025 loss — the grid reveals where the asymmetric risk actually lives.

**Adjustments, variants & timing.** Since one side is risk-light, the management is one-sided too: defend the heavy side by rolling the body toward price if Nifty moves against you, or buy back the unmatched leg to neutralise the skew. You can also widen or narrow the skipped wing to dial the credit and the loss-zone width up or down. This broken-wing build suits a Nifty monthly where you hold a directional lean and want a paid-for tent; on Bank Nifty weeklies the larger swings test the loaded side too readily, so size smaller. Place the body at the max-pain strike that also matches your bias rather than at spot. Enter in the last week with India VIX elevated and fading — short vega means a cooling IV pulls the body toward intrinsic and fattens the peak, while the final sessions let gamma and pinning, not trend, finish the job. Read the credit honestly: risk is moved, not removed.


## 49. Broken-Wing Put Butterfly
*Bearish pin, no downside risk · Short vega · net credit*

**The idea (intuition).** The mirror of the broken-wing call: build a put butterfly but push the lower wing further out, skipping a strike to cheapen it into a credit and remove the *downside* loss zone. You hold a bearish-leaning tent and get paid to do it, with risk only if the market rallies.

**When & why to use it.** Use it when you lean neutral-to-bearish but mainly want to be protected against a crash to the downside — a market where a slow drift down or a pin is likely but a melt-up is your tail fear. Being paid a credit with no downside risk suits a nervous, top-heavy index. Short vega favours entry when IV is high and fading. Avoid it if you expect a strong upside breakout, since that is where the loss lives.

**How to build it (₹, Nifty).** Buy 24300 PE @ 453, sell 2x 24000 PE @ 318, buy 23500 PE @ 169 (the skipped, wider lower wing). Net credit 15.4 points, about ₹1,155 per lot received.

![Figure: Broken-Wing Put Butterfly payoff at expiry](figs/strategies/broken_wing_put_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 307 points (~₹23,025/lot) at a 24000 pin. Max loss 185 points (~₹13,875/lot) on the upside. Single breakeven 23685. Net credit 15.4 points. Risk:reward 1.66 — with no downside loss zone, a deep sell-off still leaves you the credit.

**Greeks & behaviour.** Slight bearish delta from the skewed lower wing. Theta is positive within the tent. Vega is negative, so easing IV helps and an IV spike works against you before expiry.

**Management & exit.** Let a decline run since the downside is risk-free, keeping the credit. Watch the upside: a rally toward the 185-point loss zone is the cue to close or roll the body up. Take partial profit on a body pin.

**Management & exit (note).** Because there is a single breakeven at 23685 and no downside loss zone, this is one of the more relaxing flies to hold in a falling tape — you can let a decline run without fear. The whole job is to defend the upside. Roll the body up or close if a melt-up develops.

**Risk note.** Removing downside risk shifts a larger 185-point loss onto the upside. A sharp rally is the real danger, and the thin 15.4-point credit barely cushions it. Size the position around that upside tail, not the small credit — a gap-up open on positive global cues or a surprise policy easing is exactly the scenario that hurts here.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹13,875 | -₹13,875 | +₹23,625 | +₹1,125 | +₹1,125 |

The +₹23,625 peak prints at 24,000 while the upside strikes hold a small +₹1,125 and the 22,800–23,400 columns carry the –₹13,875 loss — the grid lays bare the lopsided downside exposure.

**Adjustments, variants & timing.** Defence lives on the upside here: roll the body up to chase a rallying Nifty, or buy in the unmatched wing to cap a melt-up before it dominates the P&L. Adjust the skipped lower wing's width to trade credit against the size of the upside loss zone. As a neutral-to-bearish paid tent it fits a Nifty monthly in a top-heavy, drifting-lower tape; Bank Nifty weeklies gap up too sharply on positive global cues, so keep size modest if you use them. Anchor the body on the max-pain or heavy-put-OI strike consistent with your soft bearish lean, not on raw spot. Put it on in the closing week with India VIX high and fading, since short vega rewards an IV slide and the last sessions hand the trade to gamma and pinning. Remember the single breakeven leaves the downside relaxed but the upside thinly hedged until the far wing — a gap-up is the real failure mode.


## 50. Skip-Strike Butterfly (Call)
*Bullish drift · Short vega · net credit*

**The idea (intuition).** A directional broken-wing call fly: the upper wing is skipped further out and the lower leg tightened, so the tent both pays for itself (a credit) and leans hard to the upside. You are positioning for a gentle bullish drift while collecting premium.

**When & why to use it.** Use it when your base case is a slow grind higher in Nifty rather than an explosive rally — a constructive but not euphoric tape. The credit and the wide upper wing mean an overshoot above your target costs nothing, so it suits markets where upside surprises are the norm and downside is the real risk. Short vega, so high-and-fading IV is the friendly regime. Avoid it ahead of a downside catalyst.

**How to build it (₹, Nifty).** Buy 23800 CE @ 585, sell 2x 24000 CE @ 456, buy 24600 CE @ 167 (the skipped wing). Net credit 159.7 points, about ₹11,978 per lot received.

![Figure: Skip-Strike Butterfly (Call) payoff at expiry](figs/strategies/skip_strike_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 351 points (~₹26,325/lot) near the 24000 body. Max loss 240 points (~₹18,000/lot) on the downside. Single breakeven 24360. Net credit 159.7 points. Risk:reward 1.46 — no upside loss zone.

**Greeks & behaviour.** Net bullish delta from the directional skew. Theta is positive inside the tent. Vega is negative — falling IV helps the structure mature toward its peak.

**Management & exit.** Since the upside carries no loss, you can hold through a rally and bank the credit. Discipline lives on the downside: scale out or roll the body down if Nifty slides toward the 240-point loss. Book a chunk if price pins the body region.

**Risk note.** The wide upper wing buys directional comfort at the cost of a sizeable 240-point downside loss. A sharp drop is the failure mode, and the larger 159.7-point credit here does not change that the risk is real and one-sided — size accordingly. This is the most directional of the credit flies so far: the wider the upper wing, the cheaper it gets and the more it behaves like a bullish bet with a downside stop, so treat it as a directional position, not a neutral income trade.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹12,000 | +₹12,000 | +₹27,000 | -₹18,000 | -₹18,000 |

Maximum +₹27,000 lands at 24,000, the lower grid keeps +₹12,000 of credit, and the 24,600–25,200 columns reveal the –₹18,000 directional downside — the ±5% grid neatly straddles the body it must pin.

**Adjustments, variants & timing.** This is the most directional credit fly, so treat it like a bullish position with a stop, not neutral income. The key adjustment is to roll the body up as Nifty grinds higher, keeping the tent under price, and to scale out or buy protection if the index slides toward the downside loss. Tightening or widening the skipped upper wing trades credit for directional reach. It suits a Nifty monthly in a constructive, slow-grind tape where upside overshoots cost nothing; Bank Nifty weeklies move too fast for a structure that wants a measured drift, so prefer the monthly. Place the body just above max-pain in the direction of your lean rather than at spot. Enter in the final week with India VIX elevated and fading — short vega means the cooling IV matures the tent toward its peak, and gamma and pinning take over in the last sessions. Size for the one-sided downside tail, never for the headline credit.


## 51. Unbalanced (Ratio) Butterfly
*Directional pin · Short vega · net credit*

**The idea (intuition).** A standard butterfly sells two body options against one of each wing; here you sell three of the body and buy two of the upper wing, so the leg counts no longer balance. That extra short skews the tent and the credit toward one side, turning a neutral structure into a directional, income-leaning bet.

**When & why to use it.** Use it when you have a directional pin view and want a larger credit than a plain fly offers — you are willing to take on a residual naked-ish exposure from the unmatched short leg in exchange. Suits a trader with a firm level target and a high-IV backdrop set to fade. Avoid it if you cannot actively manage the position, because the ratio leaves a leg that behaves more aggressively if spot runs through it.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655, sell 3x 24000 CE @ 456, buy 2x 24300 CE @ 292. Net credit 129.3 points, about ₹9,698 per lot received.

![Figure: Unbalanced (Ratio) Butterfly payoff at expiry](figs/strategies/unbalanced_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 414 points (~₹31,050/lot) around the body. Max loss 171 points (~₹12,825/lot). Single breakeven 24215. Net credit 129.3 points. Risk:reward 2.42.

**Greeks & behaviour.** Net delta is skewed by the unbalanced leg, giving the position a directional tilt. Theta is positive in the profit zone. Vega is negative — IV decline supports the trade.

**Management & exit.** The extra short means you must watch the tested side closely. Book partial profit on a body pin; if spot pushes through the skewed wing, roll or close the unmatched leg before it dominates the P&L. Do not let this run unmanaged into expiry-week gamma.

**Risk note.** Ratio structures are less forgiving than balanced flies: the unmatched short can accelerate losses if the index trends hard through it. The defined 171-point figure assumes the wings hold their hedge ratio — treat the position as needing active oversight, not set-and-forget. On NSE, margin for the extra short leg is also higher than a plain fly, so check that the SPAN-plus-exposure requirement still leaves the trade capital-efficient before putting it on.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹9,675 | +₹9,675 | +₹32,175 | -₹12,825 | -₹12,825 |

The ratio's +₹32,175 peak appears at 24,000 with +₹9,675 retained on the downside and a –₹12,825 loss on the 24,600–25,200 strikes, the unbalanced leg's skew visible across the grid.

**Adjustments, variants & timing.** The ratio's extra short demands active care: if Nifty pushes through the skewed wing, buy back or roll the unmatched leg before it behaves like a naked short and dominates the P&L. You can rebalance back to a plain fly by buying one more wing, or roll the body to follow price. It fits a Nifty monthly where you hold a firm level target and want a fatter credit than a balanced fly; avoid running unbalanced legs on Bank Nifty weeklies, where a fast move through the loaded strike is punishing. Note SPAN-plus-exposure margin on NSE is higher for the extra short, so confirm capital efficiency first. Place the body at the max-pain strike that matches your directional pin, not at spot. Enter in the closing week with India VIX high and fading so short vega works for you, and never leave the ratio unmanaged into expiry-week gamma — the unmatched leg is exactly what accelerates a loss if spot trends hard.


## 52. Long Butterfly (Wide Wings)
*Broad pin zone · Short vega · net debit*

**The idea (intuition).** A standard long call fly with the wings pushed far apart. Widening the wings stretches the profit tent over a much broader band of strikes, so you no longer need a perfect pin — a roomy target zone will do — but the wider, more expensive wings raise the cost.

**When & why to use it.** Use it when you expect Nifty to settle somewhere in a broad neighbourhood of 24000 but cannot pinpoint the exact strike — a gently consolidating market where you want forgiveness on the pin. The wider breakevens raise the probability of finishing in profit versus a tight fly. Short vega, so a fading-IV regime helps. Avoid it if you need the absolute cheapest defined-risk bet, since width costs points.

**How to build it (₹, Nifty).** Buy 23400 CE @ 882, sell 2x 24000 CE @ 456, buy 24600 CE @ 167. Net debit 137.2 points, about ₹10,290 per lot at risk.

![Figure: Long Butterfly (Wide Wings) payoff at expiry](figs/strategies/long_butterfly_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 454 points (~₹34,050/lot) at a 24000 pin. Max loss 137 points (~₹10,290/lot) beyond the wings. Breakevens 23537 and 24463 — a wide 926-point profit band. Net debit 137.2 points. Risk:reward 3.31.

**Greeks & behaviour.** Delta near flat at the body, gently directional toward the wide breakevens. Theta is positive inside the tent. Vega is negative, so falling IV helps the structure converge to its peak.

**Management & exit.** The broad tent gives you room to be patient; book 40-60% of the peak if spot sits central with time left. Because the breakevens are far apart, you rarely need to panic on a moderate move — but recentre with a roll if a strong trend threatens a wing.

**Risk note.** You pay 137 points for that comfort, a meaningfully larger debit than a narrow fly, and the full max profit still requires a near-perfect central pin. A move past either wide breakeven (23537 or 24463) still loses the whole debit. The wide-wing fly is best understood as buying a higher probability of *some* profit in exchange for a larger absolute cost and a lower reward ratio — the opposite end of the spectrum from the narrow fly that follows.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹10,275 | -₹10,275 | +₹34,725 | -₹10,275 | -₹10,275 |

The wide-wing peak of +₹34,725 still requires the 24,000 pin, but because the breakevens are far apart the loss columns show a contained –₹10,275 — the ±5% grid straddles a genuinely broad profit tent.

**Adjustments, variants & timing.** The wide tent's whole point is forgiveness, so adjustments are gentle: you rarely panic on a moderate move, but recentre with a body roll if a strong trend threatens a far wing, or narrow one wing to lock in a broken-wing credit once price has chosen a side. Because the breakevens are far apart, this suits a Nifty monthly consolidation where you expect a broad-neighbourhood settle rather than an exact pin; Bank Nifty weeklies do not need this much width and the larger debit is wasted there. Place the body at max-pain or the centre of the expected range, not at spot if they differ. Enter in the last one to two weeks with India VIX elevated and fading, since short vega lets the cooling IV converge the structure to its peak. The trade-off to respect: you pay a larger debit for a higher probability of *some* profit, and the full peak still wants a near-perfect central pin.


## 53. Long Butterfly (Narrow)
*Tight pin · Short vega · net debit*

**The idea (intuition).** The opposite extreme: pull the wings in tight around the body. The tent is razor-thin and very cheap, and it pays a spectacular multiple if Nifty lands precisely on the body — a true sniper's bet on an exact level.

**When & why to use it.** Use it on expiry-week when you have a strong, specific pin thesis — a max-pain level, a heavy open-interest strike — and want maximum reward for minimal outlay. The tiny cost makes it a low-conviction-friendly lottery ticket. Short vega and most potent when IV has already collapsed so the body trades near intrinsic. Do NOT use it as a core position: the probability of a clean pin in a narrow band is genuinely low.

**How to build it (₹, Nifty).** Buy 23850 CE @ 388, sell 2x 24000 CE @ 296, buy 24150 CE @ 216. Net debit 13.2 points, about ₹990 per lot at risk.

![Figure: Long Butterfly (Narrow) payoff at expiry](figs/strategies/long_butterfly_narrow.png)

**The numbers (modelled at Nifty 24000).** Max profit 128 points (~₹9,600/lot) at a precise 24000 finish. Max loss 13 points (~₹990/lot) beyond the wings. Breakevens 23862 and 24138 — a tight 276-point band. Net debit 13.2 points. Risk:reward 9.72.

**Greeks & behaviour.** Delta flat at the body, sharply directional just outside it. Theta is strongly positive in the final days as the tent springs up. Vega is negative.

**Management & exit.** This is an end-of-cycle, hold-to-near-expiry trade — the value materialises only in the last session or two as gamma peaks. Given the ₹990 cost, many simply let it ride to expiry. If spot is glued to the body late, taking 50-70% of the peak is reasonable rather than risking a final-hour drift.

**Risk note.** The eye-catching 9.72 reward:risk is offset by a very low probability of finishing inside the 276-point band. Expect most of these to lose the small debit — treat the high payoff as the rare exception, not the plan. The contrast with the wide-wing fly is the whole lesson of butterfly width: tighter wings multiply the reward ratio but shrink the win zone, so the headline number flatters a trade you will lose far more often than you win.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹975 | -₹975 | +₹10,275 | -₹975 | -₹975 |

The razor-thin fly peaks at +₹10,275 only at 24,000 and loses just –₹975 everywhere else on the grid — a cheap bet whose win zone the 600-point grid spacing comfortably overshoots on both sides.

**Adjustments, variants & timing.** This is a sniper's expiry-week instrument, so the main adjustment is restraint — the ₹990 cost makes letting it ride to settlement reasonable. If your pin thesis shifts, simply roll the whole tight fly to the new strike; legging adjustments rarely pay on so cheap a structure. It is purpose-built for a Nifty monthly expiry-week pin on a heavy open-interest or max-pain strike, or a Bank Nifty weekly with a clear pinning magnet — the razor band needs the gamma and pinning of the final sessions to spring. Place the body exactly on the max-pain / peak-OI strike, never on raw spot. Enter only once India VIX has collapsed so the body trades near intrinsic and the tent is cheapest; earlier entry just bleeds. Treat the dazzling reward ratio as a low-probability lottery ticket sized in single lots — most expire worthless, and the headline multiple flatters a trade you lose far more often than you win.


## 54. OTM Call Butterfly (Bullish Target)
*Bullish to a target · Short vega · net debit*

**The idea (intuition).** A standard long call fly, but centred *above* spot. You pitch the tent over a higher strike you think Nifty will drift up to, paying a small debit for a fat payoff if the index reaches that target by expiry. It is a cheap, defined-risk way to express "I think we grind to 24500."

**When & why to use it.** Use it when you have a specific upside target and a timeframe — a measured-move projection, a resistance level you expect to be tagged, a post-breakout drift. Far cheaper than buying calls outright, and the cost is the whole risk. Short vega, so a high-IV-fading backdrop helps. Avoid it if you expect an explosive rally far past the target, since the upper wing caps and then cuts the payoff.

**How to build it (₹, Nifty).** Buy 24200 CE @ 342, sell 2x 24500 CE @ 204, buy 24800 CE @ 107. Net debit 40.4 points, about ₹3,030 per lot at risk.

![Figure: OTM Call Butterfly (Bullish Target) payoff at expiry](figs/strategies/otm_call_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 248 points (~₹18,600/lot) if Nifty pins 24500. Max loss 40 points (~₹3,000/lot). Breakevens 24240 and 24760. Net debit 40.4 points. Risk:reward 6.15.

**Greeks & behaviour.** Net positive (bullish) delta at entry since the tent sits above spot; delta flattens as price approaches the target. Theta turns helpful once spot is inside the tent. Vega is negative.

**Management & exit.** As Nifty climbs toward 24500, the position gains value — book partial profit on the approach rather than demanding a perfect pin. If the rally stalls well below the target, the cheap debit can be left to expire. Roll up if price blows past 24500 and you still want exposure.

**Risk note.** Two ways to lose: the index fails to reach the target, or it overshoots past the upper wing — both forfeit the 40-point debit. The structure rewards a *measured* move to a level, not an open-ended trend. If you genuinely expect a runaway rally, a call vertical or outright calls serve better; the OTM fly is specifically a tool for a defined upside target where you also believe momentum will fade once it is reached.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹3,000 | -₹3,000 | -₹3,000 | +₹12,000 | -₹3,000 |

Because the tent is centred at 24,500, the grid never lands on the exact peak: the 24,600 column shows +₹12,000 while every other strike forfeits the –₹3,000 debit, a reminder the ±5% grid can straddle but not pin an OTM body.

**Adjustments, variants & timing.** Because the tent is centred above spot at 24500, manage it as a directional target trade: roll the whole fly higher if Nifty blows past the target and you still want exposure, or take partial profit on the approach rather than demanding the exact pin. Converting the upper wing to a wider, skipped strike turns it into a skip-strike bullish fly that no longer caps an overshoot. It suits a Nifty monthly measured-move or resistance-tag thesis where momentum is expected to fade at the level; Bank Nifty weeklies trend too hard for a capped target structure. Place the body at the resistance / projected-move strike, and check it against max-pain — a target well above heavy call OI is less likely to be reached. Enter in the last two weeks with India VIX elevated and fading so short vega helps the tent mature. The structure rewards a measured drift to a level, not an open-ended rally.


## 55. OTM Put Butterfly (Bearish Target)
*Bearish to a target · Short vega · net debit*

**The idea (intuition).** The downside mirror: a long put fly centred *below* spot, over a lower strike you expect Nifty to fall to. A small debit buys a generous payoff if the index drifts down to that target — a cheap, capped way to play "I think we slip to 23500."

**When & why to use it.** Use it when you have a defined downside target and a timeframe — a support level you expect to be tested, a measured pullback after a rally, a seasonal soft patch. Much cheaper than long puts, with the debit as the only risk. Short vega favours a high-and-fading-IV entry. Avoid it if you expect a crash far below the target, since the lower wing caps the gains.

**How to build it (₹, Nifty).** Buy 23800 PE @ 248, sell 2x 23500 PE @ 169, buy 23200 PE @ 113. Net debit 23.8 points, about ₹1,785 per lot at risk.

![Figure: OTM Put Butterfly (Bearish Target) payoff at expiry](figs/strategies/otm_put_butterfly.png)

**The numbers (modelled at Nifty 24000).** Max profit 272 points (~₹20,400/lot) if Nifty pins 23500. Max loss 24 points (~₹1,800/lot). Breakevens 23224 and 23776. Net debit 23.8 points. Risk:reward 11.4 — the richest reward ratio in the group.

**Greeks & behaviour.** Net negative (bearish) delta at entry as the tent sits below spot; it flattens as price nears the target. Theta helps once spot is inside the tent. Vega is negative.

**Management & exit.** Book partial profit as Nifty falls toward 23500 rather than holding out for an exact pin. If the decline fails to develop, the tiny debit can simply expire. Roll the fly lower if price overshoots and you keep a bearish view.

**Risk note.** The headline 11.4 reward:risk — the richest in the group — reflects a low-probability outcome: Nifty must land near 23500, neither stopping short nor crashing through the lower wing. Most attempts lose the small 24-point debit; the payoff is a tail event, not the expectation. Note too that on a genuine market crash the index can slice straight past 23500 to the lower wing and beyond, capping your gain exactly when an outright put would have paid most — so this is a target trade, not a crash hedge.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹1,800 | +₹13,200 | -₹1,800 | -₹1,800 | -₹1,800 |

Centred at 23,500, the body falls between grid points — the 23,400 column captures +₹13,200 while all other strikes lose the –₹1,800 debit, illustrating how a ±5% grid may straddle an off-centre target.

**Adjustments, variants & timing.** Centred below spot at 23500, this is the bearish-target mirror: roll the fly lower if Nifty overshoots and your bearish view holds, or bank partial profit as price approaches the target instead of waiting for a perfect pin. Widening the lower wing into a skip-strike removes the cap if you want a deeper slide to keep paying. It fits a Nifty monthly support-test or measured-pullback thesis where the fall is expected to stall at the level; a genuine crash slices straight through to the lower wing and caps you exactly when an outright put pays most, so it is a target trade, not a crash hedge. Place the body at the support / projected strike and sanity-check against max-pain and heavy put OI. Enter in the closing fortnight with India VIX high and fading so short vega aids the structure. As the richest reward ratio in the group, treat it as a tail bet — most attempts lose the small debit.


## 56. Iron Butterfly (Wide Wings)
*Pin near ATM · Short vega · net credit*

**The idea (intuition).** A standard iron fly with the protective wings pushed further out. You still sell the ATM straddle for income, but the wider, cheaper wings collect less credit while shrinking the maximum loss and widening the profitable band. A more forgiving version of the income trade.

**When & why to use it.** Use it when you want iron-fly income but with a broader margin for error on the pin — a range-bound Nifty where you would rather sacrifice some credit for a smaller, more comfortable max loss. Good for traders who found the standard iron fly's tight breakevens too easily breached. Short vega, so high-and-fading IV remains the ideal backdrop. Avoid it before a catalyst that can gap past even the wider wings.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 24500 CE @ 204, buy 23500 PE @ 169 (wider wings). Net credit 401.3 points, about ₹30,098 per lot received.

![Figure: Iron Butterfly (Wide Wings) payoff at expiry](figs/strategies/iron_butterfly_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 393 points (~₹29,475/lot) at a 24000 pin. Max loss 99 points (~₹7,425/lot) beyond a wing. Breakevens 23599 and 24401 — an 802-point profit band. Net credit 401.3 points. Risk:reward 3.98.

**Greeks & behaviour.** Delta near flat at the body. Theta is strongly positive — a decay engine like the standard iron fly. Vega is negative, so IV crush after a spike accelerates profit.

**Management & exit.** Close at roughly 50% of max credit; the wider tent gives more room before a tested side demands action. Roll the untested wing in for credit or roll out to recentre if a side is breached. Exit before expiry-week gamma.

**Risk note.** Wider wings cut the max loss to 99 points but a sustained trend can still breach a breakeven — defined risk is not no risk. Short ATM legs carry assignment risk near expiry if in-the-money; manage before the last sessions. The larger 401-point credit collected here is misleading on its own: most of it merely offsets the wider strikes, and the true edge is the modest 393-point peak against a 99-point loss in a market that actually pins.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹7,425 | -₹7,425 | +₹30,075 | -₹7,425 | -₹7,425 |

The wider iron fly keeps +₹30,075 at a 24,000 pin and limits the wing loss to –₹7,425, the grid showing a more forgiving, broader-banded version of the income tent.

**Adjustments, variants & timing.** The wider wings give more room before a side demands action, so adjustments are unhurried: roll the untested wing in for credit when one side is tested, or roll the whole structure out and recentre on the new pin. Converting to a broken-wing by moving one wing further still trades the symmetric loss for extra credit and a skew. This is a Nifty monthly income trade for a range-bound tape where the tight standard iron fly's breakevens felt too easily breached; on Bank Nifty weeklies the broader band helps but the faster moves still argue for smaller size. Centre the short straddle on the max-pain strike, not spot, and sell it once India VIX has spiked and is mean-reverting so the wider, cheaper wings still leave a worthwhile credit. Enter in the last one to two weeks for peak theta, and flatten before the final two sessions to dodge pin-and-gap and short-ATM assignment on any in-the-money leg.


## 57. Broken-Wing Iron Butterfly
*Neutral with a skew · Short vega · net credit*

**The idea (intuition).** An iron fly with mismatched wing distances — one wing closer, one further — so the protection is asymmetric. That shifts the risk toward one side and squeezes out extra credit, turning the neutral income tent into a skewed, slightly directional bet.

**When & why to use it.** Use it when you want iron-fly income but have a mild directional lean and are willing to concentrate risk on the side you fear less. The asymmetric wings let you collect more credit than a balanced fly. Suits a range-bound market with a soft directional bias. Short vega, so high-and-fading IV is the friendly regime. Avoid it if the side carrying the larger risk is also where a catalyst could push spot.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 24300 CE @ 292 (near wing), buy 23500 PE @ 169 (far wing). Net credit 313.7 points, about ₹23,528 per lot received.

![Figure: Broken-Wing Iron Butterfly payoff at expiry](figs/strategies/broken_wing_iron_fly.png)

**The numbers (modelled at Nifty 24000).** Max profit 305 points (~₹22,875/lot) near the body. Max loss 186 points (~₹13,950/lot). Single breakeven 23686. Net credit 313.7 points. Risk:reward 1.64.

**Greeks & behaviour.** Net delta carries a mild skew from the asymmetric wings. Theta is positive — time decay drives the trade. Vega is negative, so easing IV helps.

**Management & exit.** Close at around 50% of max credit. Watch the side with the closer wing and larger residual risk; roll or close if spot tests it. Recentre with a roll if your directional lean changes. Exit before expiry-week gamma. A practical NSE tip: leg into the credit on a day the index ticks toward your favoured side, so the short straddle is sold into slightly richer premium and the skew works in your favour from the open.

**Risk note.** The extra credit comes from accepting a larger, skewed 186-point loss on one side. The single breakeven at 23686 means a downside move is only thinly hedged until the far put wing — manage actively, and remember the short ATM legs carry assignment risk near expiry. As with every broken-wing structure, read the credit honestly: you have moved the risk, not removed it, and the heavier loss now lives below the market.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹13,950 | -₹13,950 | +₹23,550 | +₹1,050 | +₹1,050 |

The skewed iron fly peaks at +₹23,550 at 24,000, holds a slim +₹1,050 on the upside, and carries the heavier –₹13,950 loss on the 22,800–23,400 columns — the grid exposes which side is thinly hedged.

**Adjustments, variants & timing.** The asymmetric wings mean you watch the side with the closer wing and larger residual risk: roll or close that side if spot tests it, and recentre the body with a roll if your directional lean changes. You can rebalance toward a symmetric iron fly by moving the far wing in, trading credit for protection. It suits a Nifty monthly range with a soft directional bias where you will accept more risk on the side you judge safer for a fatter credit; Bank Nifty weeklies leave the thin side too exposed to a fast move. Centre the short straddle on max-pain and skew the wings toward your lean. A practical NSE tip: leg in on a day the index ticks toward your favoured side so the straddle is sold into richer premium. Enter in the closing week with India VIX high and fading, and exit before expiry-week gamma — the short ATM legs also carry assignment risk if they finish in-the-money.


## 58. Put Broken-Wing (Income)
*Neutral to bullish · Short vega · net credit*

**The idea (intuition).** A put-side skip-strike butterfly taken for a credit, structured to lean neutral-to-bullish. By widening the lower wing you cheapen the downside protection into a credit and tilt the payoff so a flat-to-rising market pays you — income with a constructive bias.

**When & why to use it.** Use it when you expect Nifty to hold up or grind higher and want to harvest premium on the put side, with defined risk if you are wrong on the downside. Good in a steady, mildly bullish tape after IV has spiked and is fading. Short vega supports a high-IV entry. Avoid it ahead of a downside catalyst, since the residual risk sits below the market.

**How to build it (₹, Nifty).** Buy 24200 PE @ 404, sell 2x 23900 PE @ 282, buy 23400 PE @ 148 (skipped lower wing). Net credit 11.9 points, about ₹893 per lot received.

![Figure: Put Broken-Wing (Income) payoff at expiry](figs/strategies/put_broken_wing_credit.png)

**The numbers (modelled at Nifty 24000).** Max profit 301 points (~₹22,575/lot) near the 23900 body. Max loss 188 points (~₹14,100/lot) on the downside. Single breakeven 23588. Net credit 11.9 points. Risk:reward 1.6.

**Greeks & behaviour.** Slight bullish-to-neutral delta from the skew. Theta is positive in the profit zone. Vega is negative, so falling IV helps the structure mature.

**Management & exit.** Hold for decay; book partial profit if spot sits near or above the body. The action point is the downside — close or roll the body down if Nifty slides toward the 188-point loss zone. Exit before expiry-week gamma. Because the bias is gently bullish, a flat-to-up grind quietly works in your favour through theta, but resist the temptation to add size after a couple of easy wins — that is precisely when the downside tail tends to show up.

**Risk note.** The thin 11.9-point credit barely cushions a 188-point downside loss, so this is really a directional risk-acceptance trade dressed as income. A sharp sell-off below the breakeven at 23588 is the failure mode — size for that downside tail, not the small credit. The "income" label is the dangerous part: collecting a tiny credit feels like the safe premium-selling trades retail loves, but SEBI's own studies show most F&O traders lose, and a structure that risks 188 to keep 12 is exactly how that happens if left unmanaged.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹14,100 | -₹14,100 | +₹15,900 | +₹900 | +₹900 |

The body sits at 23,900, so the 24,000 column shows the near-peak +₹15,900 while the upside keeps +₹900 and the downside strikes reveal the –₹14,100 loss — the grid makes the directional risk plain.

**Adjustments, variants & timing.** With the body at 23900 and a neutral-to-bullish tilt, defence lives below the market: roll the body down or buy in the skipped wing if Nifty slides toward the downside loss zone, and let a flat-to-up grind quietly pay you through theta. Widening the lower wing dials the credit against the size of the downside tail. It fits a Nifty monthly steady-to-mildly-bullish tape after an India VIX spike has begun to fade; avoid it before a downside catalyst, since the residual risk sits there, and keep Bank Nifty weekly size small given sharper gap risk. Place the body at the max-pain or heavy-call-support strike consistent with your bullish lean, not at spot. Enter in the final week with IV high and easing so short vega helps the structure mature. Resist adding size after a couple of easy wins — SEBI's F&O studies show most retail loses, and a trade risking 188 to keep 12 is exactly how, if left unmanaged.


## 59. Iron Butterfly (Weekly)
*Pin this week · Short vega · net credit*

**The idea (intuition).** The iron fly compressed into a weekly expiry. With only days to run, the short ATM straddle decays fast and the tent is sharp — rich theta in exchange for vicious gamma. A short, intense bet that Nifty pins 24000 by week's end.

**When & why to use it.** Use it on a quiet expiry week with no major scheduled catalyst, when you want to harvest the steep weekly theta on a range-bound index — Nifty or Bank Nifty weeklies are the natural home. Best when weekly IV is elevated relative to the expected move. Short vega and short gamma, so it demands active management. Do NOT run it through an event week or leave it unattended into expiry day.

**How to build it (₹, Nifty).** Sell 24000 CE @ 202, sell 24000 PE @ 170, buy 24250 CE @ 91, buy 23750 PE @ 83. Net credit 198.0 points, about ₹14,850 per lot received.

![Figure: Iron Butterfly (Weekly) payoff at expiry](figs/strategies/iron_fly_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 189 points (~₹14,175/lot) at a 24000 pin. Max loss 52 points (~₹3,900/lot) beyond a wing. Breakevens 23802 and 24198. Net credit 198.0 points. Risk:reward 3.64.

**Greeks & behaviour.** Delta near flat at the body but it swings fast as spot moves — high gamma. Theta is strongly positive and front-loaded in the final days, which is the whole reason to trade the weekly rather than the monthly version. Vega is negative, so a midweek IV pop against you is unwelcome even if spot has not moved much.

**Management & exit.** Manage actively: take 25-50% of the credit early since weekly gamma can flip a winner to a loser in one session. Roll the tested side or close outright if a breakeven is threatened. Many desks flatten the day before expiry to avoid pin-and-gap risk entirely.

**Risk note.** Weekly gamma is the headline danger — a single sharp move blows through the tight 23802/24198 breakevens fast, and the defined 52-point loss arrives quickly. Short ATM legs risk assignment into expiry. This is a hands-on trade, never set-and-forget. Bank Nifty weeklies amplify everything here: bigger point moves relative to the wing width mean the tent is breached more often, so size smaller on Bank Nifty than the headline Nifty numbers suggest.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹3,900 | -₹3,900 | +₹14,850 | -₹3,900 | -₹3,900 |

The weekly fly keeps +₹14,850 only at a 24,000 pin and surrenders the defined –₹3,900 at every other strike, the tight grid spacing underscoring how easily weekly gamma breaches the body.

**Adjustments, variants & timing.** Weekly gamma is the headline, so adjustments are fast and frequent: take 25–50% of the credit early, roll the tested side or close outright the moment a breakeven is threatened, and many desks simply flatten the day before expiry to sidestep pin-and-gap entirely. Rolling the untested wing in for credit is the standard repair. Nifty and Bank Nifty weeklies are the natural home, but Bank Nifty's bigger point moves relative to the wing width breach the tent more often — size smaller there than the Nifty numbers suggest. Centre the short straddle on the max-pain strike, and trade it only on a quiet expiry week with no scheduled catalyst, when weekly IV is elevated relative to the expected move so theta is front-loaded in your favour. This is a hands-on, final-sessions trade where steep weekly decay is the whole edge — short vega means even a midweek IV pop against you stings, so never leave it unattended into expiry day.


## 60. Reverse Iron Butterfly (Event)
*Event breakout · Long vega · net debit*

**The idea (intuition).** A long-vol weekly tent for a catalyst: buy the ATM straddle and sell wings to fund part of it, so you own a defined-risk bet that Nifty breaks sharply away from 24000 during an event week. You pay a debit and want fireworks.

**When & why to use it.** Use it into a known binary catalyst on a short fuse — results, a policy decision, an election count — when you expect a large move but cannot call direction, and weekly IV is still cheap enough to buy. Long vega, so an IV ramp into the event helps before the move even happens. Avoid it if the event is already priced and IV is rich, since the post-event crush will gut a long-vol position.

**How to build it (₹, Nifty).** Buy 24000 CE @ 202, buy 24000 PE @ 170, sell 24300 CE @ 75, sell 23700 PE @ 71. Net debit 225.9 points, about ₹16,943 per lot at risk.

![Figure: Reverse Iron Butterfly (Event) payoff at expiry](figs/strategies/reverse_iron_fly_event.png)

**The numbers (modelled at Nifty 24000).** Max profit 74 points (~₹5,550/lot) on a move beyond a wing. Max loss 217 points (~₹16,275/lot) if Nifty pins 24000. Breakevens 23774 and 24226. Net debit 225.9 points. Risk:reward 0.34.

**Greeks & behaviour.** Delta near zero at entry, turning directional as spot moves. Theta is negative — every flat day costs you, sharply so on a weekly. Vega is positive, so an IV ramp helps and the post-event crush hurts.

**Management & exit.** This is a fast in-and-out trade. Take profit immediately on a clean breakout toward a wing — do not wait for the wing to cap. If the event passes with a muted move, cut at once before theta and IV crush combine to deliver the 217-point loss.

**Risk note.** The risk:reward is steep — a 217-point downside for a capped 74-point gain (risk:reward 0.34) — so the trade only works on a large, fast move plus a vol tailwind. A pinned, anticlimactic event with IV crush is the maximum-loss outcome, and it is common: results and policy days frequently see weekly IV inflated beforehand and crushed after, punishing long-vol buyers even when the move is decent. Buy the wings cheap or do not buy at all.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹5,550 | +₹5,550 | -₹16,950 | +₹5,550 | +₹5,550 |

The event tent loses the full –₹16,950 if Nifty pins 24,000 but pays a capped +₹5,550 at all four outer strikes — the ±5% grid straddles the body, so any of these moves is the breakout you are paying for.

**Adjustments, variants & timing.** As a long-vol weekly debit tent, the only good adjustments are quick exits: bank the move the instant a breakout reaches a wing, do not wait for the cap, and cut at once if the event passes muted before theta and IV crush combine. Legging off the short wings to hold a clean long straddle is the only constructive variant if you want uncapped upside. It is an event-week tool — a Nifty or Bank Nifty weekly straddling a binary catalyst (results, a policy decision, an election count); never run it on a quiet week. Place the body on spot, not max-pain, since you are betting against the pin. The critical timing rule: buy only while weekly IV is still cheap and ramping into the event — if the event is already priced and IV is rich, the post-event crush guts the position even on a decent move. Buy the wings cheap or do not buy at all.


## 61. Expiry-Day Pin Butterfly
*Expiry pin · Short vega · net debit*

**The idea (intuition).** A very tight, very cheap call fly placed on expiry day itself, betting the index gets nailed to a max-pain strike as dealers hedge into the close. With hours left, the structure is almost pure intrinsic — a low-cost sniper shot at the closing print.

**When & why to use it.** Use it on expiry afternoon when open interest clusters around a strike and you believe pinning forces will drag the close to 24000 — a classic Nifty/Bank Nifty expiry-day phenomenon. The minimal cost makes it a cheap punt with a fat ratio. Short vega is largely moot this late; it is really a gamma/pin bet. Avoid it if a late catalyst or strong trend is overriding the pin.

**How to build it (₹, Nifty).** Buy 23900 CE @ 164, sell 2x 24000 CE @ 104, buy 24100 CE @ 59. Net debit 15.8 points, about ₹1,185 per lot at risk.

![Figure: Expiry-Day Pin Butterfly payoff at expiry](figs/strategies/atm_butterfly_pin.png)

**The numbers (modelled at Nifty 24000).** Max profit 76 points (~₹5,700/lot) if Nifty closes at 24000. Max loss 16 points (~₹1,200/lot) beyond the wings. Breakevens 23916 and 24085 — a tiny 169-point band. Net debit 15.8 points. Risk:reward 4.79.

**Greeks & behaviour.** Delta flat at the body, flipping sharply just outside — extreme gamma this close to expiry. Theta is intensely positive in the final hours as the tent snaps to its peak. Vega is negligible.

**Management & exit.** This trade lives and dies in a single session — hold toward the close if spot hugs 24000, or cut quickly if it drifts to a wing. Given the ₹1,185 cost, many let it run to settlement. Take profit if the body pin firms up an hour before close.

**Risk note.** The 169-point band is razor-thin, so any late directional push forfeits the small debit. Pinning is a tendency, not a law — a trending or news-driven expiry overrides it, and intraday spreads on the expiring strikes can widen sharply in the last hour, so the screen payoff may not be the fill you get. Treat this as a tiny, high-variance punt sized in single lots, not a repeatable income method.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹1,200 | -₹1,200 | +₹6,300 | -₹1,200 | -₹1,200 |

The expiry-day fly peaks at a modest +₹6,300 at 24,000 and loses just –₹1,200 elsewhere — the 600-point grid steps far past the 169-point band, showing how precise the close must be to pay.

**Adjustments, variants & timing.** This trade lives and dies in a single session, so adjustments are minimal: hold toward the close if spot hugs 24000, cut quickly if it drifts to a wing, and given the ₹1,185 cost many simply let it run to settlement. If a clearer pin strike emerges intraday, roll the tiny fly to it rather than legging. It is an expiry-afternoon Nifty or Bank Nifty instrument, placed only when open interest clusters tightly and pinning forces are dragging the close toward the max-pain strike — set the body exactly on that strike, never on raw spot. Vega is moot this late; it is a pure gamma/pin bet, so India VIX hardly matters. Enter in the last hour or two when the structure is almost all intrinsic and cheapest. Beware that intraday spreads on the expiring strikes widen sharply near the close, so the screen payoff may not be your fill — size in single lots and treat it as a high-variance punt.


## 62. Unbalanced Iron Butterfly
*Skewed neutral · Short vega · net credit*

**The idea (intuition).** An iron fly with wings placed at *different distances* from the body, so the call-side and put-side risk-reward no longer match. The unequal wings tilt the payoff and the credit toward one side — a deliberately lopsided income tent for a trader with a directional lean.

**When & why to use it.** Use it when you want iron-fly income but hold a mild bias and are content to carry more risk on the side you judge safer, in return for a larger or more efficiently placed credit. Suits a range-bound market with a soft skew view. Short vega, so high-and-fading IV is the backdrop. Avoid it when the heavier-risk side faces a live catalyst, because the asymmetry leaves that side thinly protected.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 24250 CE @ 317 (near call wing), buy 23400 PE @ 148 (far put wing). Net credit 310.0 points, about ₹23,250 per lot received.

![Figure: Unbalanced Iron Butterfly payoff at expiry](figs/strategies/unbalanced_iron_fly.png)

**The numbers (modelled at Nifty 24000).** Max profit 301 points (~₹22,575/lot) near the body. Max loss 290 points (~₹21,750/lot). Single breakeven 23690. Net credit 310.0 points. Risk:reward 1.04 — nearly symmetric reward and risk in points.

**Greeks & behaviour.** Net delta carries a skew from the mismatched wings. Theta is positive — the income engine. Vega is negative, so easing IV helps.

**Management & exit.** Close at around 50% of max credit; with risk and reward nearly equal there is little margin to be greedy. Watch the side with the more distant wing and larger 290-point exposure, and roll or close if spot tests it. Exit before expiry-week gamma.

**Risk note.** With risk:reward near 1.04, this is a near-coin-flip in points — the large 290-point downside is almost as big as the 301-point profit you can keep, so a single trending move can erase a season of gains. Short ATM legs add assignment risk near expiry. Size small and manage the skewed side closely. The lesson that closes this family: every twist on the butterfly — wider, narrower, broken, unbalanced, iron — is just a way of trading width and skew for credit, and none of them escapes the iron rule that a bigger credit or a removed loss zone is always paid for with more risk somewhere else.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹21,750 | -₹21,750 | +₹23,250 | +₹4,500 | +₹4,500 |

The unbalanced iron fly keeps +₹23,250 at 24,000, retains +₹4,500 on the upside, but carries a near-symmetric –₹21,750 on the 22,800–23,400 strikes — the grid lays the coin-flip risk bare.

**Adjustments, variants & timing.** With unequal wing distances the risk is lopsided, so manage the side carrying the more distant wing and larger exposure: roll or close it if spot tests that side, and recentre with a roll if your skew view changes. Rebalancing the far wing inward trades credit for protection and pulls the near-coin-flip back toward neutral. It suits a Nifty monthly range with a soft directional skew where you will carry more risk on the side you judge safer; Bank Nifty weeklies leave the distant side too exposed to a fast trending move, so keep size minimal. Centre the short straddle on max-pain and place the wings to reflect your lean. Enter in the closing week with India VIX high and fading so short vega works for you, and exit before expiry-week gamma — short ATM legs add assignment risk if in-the-money. With risk:reward near 1.04 this is almost a coin-flip in points, so size small: one trending session can erase a season of gains.

