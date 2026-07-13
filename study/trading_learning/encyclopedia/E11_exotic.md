# Strategy Group 11: Exotic & Named Combinations

These are the desk's "named combos" — structures that traders invented to fix one specific flaw in a plainer position. Most start from a familiar building block (a strangle, a butterfly, a vertical, a backspread) and then bolt on, shift, or skew one leg so the payoff hugs the way the trader actually wants to be exposed: keep the full credit if it rips one way, ride the volatility skew, mimic the stock with a clean delta, or stretch a condor so wide it almost never loses. The trade-off is always the same — you buy a nicer shape with either a smaller credit, an extra leg's slippage, or an honestly admitted unlimited tail on one side. Read the loss flags carefully; several of these names hide a naked short.

## 155. Jade Lizard
*Neutral to bullish, high IV · Short vega · net credit*

**The idea (intuition).** A jade lizard is a short put plus a short call spread, sized so the total credit you collect is bigger than the width of the call spread. The clever bit: if you pocket more premium than the call spread can ever lose, there is literally no upside risk — the index can rip to the moon and you still keep money. You only lose if the market falls hard through your short put.

**When & why to use it.** Reach for it when IV is rich (India VIX elevated, IV rank > 60, post-event premium still fat) and your bias is neutral-to-mildly-bullish. It solves the short-strangle's worst nightmare — a melt-up that blows out the naked call — by capping the call side while keeping the credit large. Ideal on Nifty/Bank Nifty monthly after a fear spike. Avoid it when you genuinely expect a sharp sell-off, because the put is your only real risk and it is naked below the strike.

**How to build it (₹, Nifty).** Sell 23700 PE @ 219, sell 24300 CE @ 292, buy 24600 CE @ 167. The call spread is 300 wide; net credit is 343.4 points = about ₹25,755 per lot (343.4 × 75). Because 343 credit > 300 call-spread width, the upside is risk-free by construction.

![Figure: Jade Lizard payoff at expiry](figs/strategies/jade_lizard.png)

**The numbers (modelled at Nifty 24000).** Max profit 343 points (~₹25,725/lot), kept on any close above 23700. Max loss -23356 points (~₹17.5 lakh/lot) only if Nifty goes to zero. Breakeven 23357. Net credit 343.4 points. Risk:reward 0.01 — that tiny figure is the zero-collapse artefact, not the real trade.

**Greeks & behaviour.** Net delta slightly positive (short put dominates), theta strongly positive (you are a net premium seller), vega negative — falling IV and the passage of time both pay you. P&L is driven by staying above the short put.

**Management & exit.** Standard tasty-style: close at ~50% of max credit. Defend the put if Nifty approaches 23700 — roll it down-and-out or convert to a spread. The call side needs no babysitting since it can't lose.

**Risk note.** That worst case assumes the index collapses to zero; in practice you size small and stop at a multiple of the credit. The honest danger is a gap-down through 23700 where the naked put assigns — keep it small and define a mental stop at 2x credit.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹41,775 | +₹3,225 | +₹25,725 | +₹3,225 | +₹3,225 |

The grid shows the signature jade-lizard shape — full credit kept anywhere at or above the short put and flat-positive on a rip — but the -₹41,775 at 22,800 is only the start of the pain, because the naked 23700 put keeps losing roughly ₹75 per point for every further point Nifty falls below the grid.

**Adjustments, variants & timing.** The only leg that ever needs managing is the short 23700 put. If Nifty drifts toward it, roll the put down-and-out to the next expiry for a credit, or buy a cheap lower put to convert the naked side into a defined put spread (turning the whole thing into an iron structure). The call spread is risk-free by construction, so leave it alone and let it decay. Take the trade off at 50% of max credit. Build it only when IV rank is above 60 and the put skew is steep — you need the fat downside premium so total credit comfortably exceeds the 300-wide call spread; in thin-IV weeks the credit won't cover the width and the "no upside risk" feature disappears. Nifty monthly is the cleaner vehicle here because its softer skew still pays enough while keeping gap risk smaller; Bank Nifty pays a richer credit but its violent gap-downs make the naked put genuinely dangerous, so size Bank Nifty at roughly half the lots.

## 156. Reverse Jade Lizard
*Neutral to bearish, high IV · Short vega · net credit*

**The idea (intuition).** Mirror image of the jade lizard: a short call plus a short put spread, with the credit collected exceeding the put spread's width. That removes the *downside* risk — a crash can't hurt the defined put spread once the credit covers it — leaving the naked call above as your only real exposure.

**When & why to use it.** Use it when IV is high and you lean neutral-to-bearish, expecting the market to drift down or chop rather than melt up. It fixes the short-strangle's downside tail (gap-downs are the more violent move on Indian indices) by capping the put side. Good after a relief rally into resistance when you think upside is limited. Do NOT use it ahead of a known bullish catalyst — your loss is open above.

**How to build it (₹, Nifty).** Sell 24300 CE @ 292, sell 23700 PE @ 219, buy 23400 PE @ 148. The put spread is 300 wide; net credit 363.1 points = about ₹27,233 per lot. Since 363 > 300, the downside is covered and risk-free.

![Figure: Reverse Jade Lizard payoff at expiry](figs/strategies/reverse_jade_lizard.png)

**The numbers (modelled at Nifty 24000).** Max profit 363 points (~₹27,225/lot), kept on any close below 24300. Max loss Undefined — large (the naked 24300 call has no upper bound). Breakeven 24663. Net credit 363.1 points. Risk:reward null because one side is unlimited.

**Greeks & behaviour.** Net delta slightly negative (short call leads), theta positive, vega negative. You make money on time decay and IV contraction as long as Nifty stays under the call strike.

**Management & exit.** Take profit at ~50% of credit. The put spread can be left alone; all your attention goes to the naked call — roll it up-and-out if Nifty pushes toward 24300, or cap it by buying a higher call to convert into a defined iron structure.

**Risk note.** This one is honestly open-ended to the upside — a runaway rally (think a surprise rate cut or a global risk-on gap) can produce a large, theoretically unlimited loss on the naked call. Size for the worst single-day move and pre-plan the roll.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹4,725 | +₹4,725 | +₹27,225 | +₹4,725 | -₹40,275 |

The mirror image of the jade lizard — full credit kept on any close at or below the short call, with the put spread covering the downside — but the -₹40,275 at 25,200 is not the floor: above the grid the naked 24300 call keeps bleeding about ₹75 per further point, so a runaway rally is genuinely unlimited.

**Adjustments, variants & timing.** Here the protected leg is the put spread (leave it to decay) and every adjustment is about the naked 24300 call. If Nifty climbs toward it, roll the call up-and-out for a credit, or buy a higher call to cap the structure into a defined iron condor. Set a hard mental stop at 2x credit on the call side and pre-load the roll order before entry. Manage the winner at 50% of max credit. The right setup is high IV rank with a neutral-to-bearish lean and, ideally, a market sitting under resistance after a relief rally where you judge upside is capped. Because the open tail is to the upside and Indian indices gap down more violently than up, this structure is actually safer in gap terms than the standard jade lizard — but a surprise rate cut or global risk-on session is its nightmare. Prefer Nifty; on Bank Nifty the wider strikes and faster rallies demand smaller size and a tighter roll trigger.

## 157. Big Lizard
*Neutral, high IV · Short vega · net credit*

**The idea (intuition).** A big lizard is a short ATM straddle with a long OTM call bolted on top. You sell both the at-the-money call and put for a fat credit, then spend a little buying a higher call so that — just like the jade lizard — the credit exceeds the call-spread width and your upside risk vanishes. It is the most aggressive premium-collector of the lizard family because the straddle is sold right at the money.

**When & why to use it.** This is a high-IV, expect-it-to-pin trade. Sell it when India VIX is elevated and you believe Nifty will sit near 24000 into expiry — a classic post-event IV-crush play (day after Budget, RBI, or a big earnings cluster). The huge ATM credit gives you a wide downside cushion while the long call erases blow-up risk on a rip. Don't use it if you expect a directional trend; the short straddle bleeds fast once price leaves the strike.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 24300 CE @ 292. Call spread width 300, net credit 482.3 points = about ₹36,173 per lot. Credit (482) > width (300), so the upside is risk-free.

![Figure: Big Lizard payoff at expiry](figs/strategies/big_lizard.png)

**The numbers (modelled at Nifty 24000).** Max profit 474 points (~₹35,550/lot) at a 24000 pin. Max loss -23517 points only on a collapse to zero. Breakeven 23518 (downside only). Net credit 482.3 points. Risk:reward 0.02 — again the zero-floor artefact.

**Greeks & behaviour.** Net delta near zero at inception (ATM straddle is delta-balanced, long call tilts it slightly positive), theta strongly positive — this is a time-decay machine — vega sharply negative. IV crush is your friend; a big move in either direction is the enemy on the put side.

**Management & exit.** Manage at 25-50% of max profit because the ATM straddle reaches profit fast but also reverses fast. Defend the naked put aggressively below 23518 — roll down or add a long put to define it. Exit before expiry-week gamma turns the ATM short into a hand grenade.

**Risk note.** Worst case assumes a fall to zero; realistically you stop out at a multiple of the credit. The live danger is a sharp down-move: the naked ATM put gains delta fast and can hand you a painful loss in a single gap. Trade small and respect the breakeven.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹53,850 | -₹8,850 | +₹36,150 | +₹13,650 | +₹13,650 |

Maximum reward sits at a 24000 pin (+₹36,150) and the upside flattens to a risk-free +₹13,650 once past the long call, but the -₹53,850 at 22,800 understates the downside — the naked ATM 24000 put loses about ₹75 per point all the way down, so a move below the grid loses far more.

**Adjustments, variants & timing.** This is the most aggressive lizard, so manage it early — bank 25-50% of max because the ATM straddle gives back gains as fast as it makes them. The only defended task is the naked 24000 put: roll it down if Nifty slides toward breakeven, or add a long put to cap the structure into a defined iron fly. Always close before expiry week, where ATM gamma turns the short straddle into a hand grenade. The textbook setup is a post-event IV crush — the session after Budget, RBI policy, or a heavy results cluster — when India VIX is high and you expect Nifty to pin near 24000. You need IV rank above 60 so the ATM straddle credit is fat enough to exceed the 300-wide call spread. Strongly prefer Nifty: Bank Nifty's wider ATM straddle pays more but its larger gap moves make the naked ATM put punishing, so halve the size if you trade it there.

## 158. Twisted Sister
*Neutral, high IV · Short vega · net credit*

**The idea (intuition).** The twisted sister is the big lizard flipped to the put side: a short ATM straddle plus a long OTM put. The credit collected exceeds the put-spread width, so the *downside* is the protected, risk-free side and the naked call above is your only open exposure. Think of it as "I'll sell the straddle but I refuse to be caught naked in a crash."

**When & why to use it.** Pick it over the big lizard when your tail fear is a gap-down rather than a melt-up — which on Indian indices is usually the more violent direction. High IV, neutral view, expecting a pin near 24000. Good when you're happy to defend a call but want hard protection beneath the market. Avoid ahead of bullish catalysts since the upside is uncapped.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, sell 24000 PE @ 318, buy 23700 PE @ 219. Put spread width 300, net credit 555.4 points = about ₹41,655 per lot — the richest credit in the lizard family because both ATM legs are sold.

![Figure: Twisted Sister payoff at expiry](figs/strategies/twisted_sister.png)

**The numbers (modelled at Nifty 24000).** Max profit 547 points (~₹41,025/lot) at a 24000 pin. Max loss Undefined — large (naked 24000 call). Breakeven 24555. Net credit 555.4 points. Risk:reward null — one side is unlimited.

**Greeks & behaviour.** Net delta roughly flat to slightly negative, theta strongly positive, vega negative. You are paid by time and falling volatility; the protected put side means a crash actually has a floor, but a rally is open-ended.

**Management & exit.** Bank 25-50% of the credit early. All defence goes to the upside: roll the naked call up-and-out if Nifty climbs toward 24000-24300, or buy a higher call to convert to a defined structure. Close before expiry-week gamma.

**Risk note.** The loss here is genuinely unlimited above — a strong trending rally can run the naked call far past breakeven. This is not a set-and-forget trade; size small and have the upside roll planned before you put it on.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹19,125 | +₹19,125 | +₹41,625 | -₹3,375 | -₹48,375 |

Peak +₹41,625 at a 24000 pin, with the protected put side flooring the downside at a healthy +₹19,125, but the -₹48,375 at 25,200 is not the floor — above the grid the naked 24000 call keeps losing about ₹75 per point without bound.

**Adjustments, variants & timing.** This is the big lizard flipped, so all defence is on the naked 24000 call above; the long 23700 put protects the downside and can be left alone. Roll the call up-and-out for a credit if Nifty rallies through breakeven, or buy a higher call to convert to a defined iron fly. Bank 25-50% of the rich credit early and exit before expiry-week gamma. Pick this over the big lizard precisely when your tail fear is a melt-up rather than a crash — but note the irony that on Indian indices the more common violent move is the gap-down you've already protected, leaving you exposed to the rarer (and more damaging when it hits) trending rally. The setup is high IV rank, neutral view, expected pin near 24000, and no bullish catalyst pending. Nifty is the safer instrument; Bank Nifty's faster upside trends make the naked call dangerous, so size down and pre-stage the roll.

## 159. Christmas Tree Butterfly (Call)
*Bullish to a target · Short vega · net credit*

**The idea (intuition).** A christmas tree is a 1-3-2 call structure — buy one lower call, sell three at a middle strike, buy two higher. It's a butterfly with a deliberately uneven, "skewed" shape that leans the profit zone toward a specific upside target while staying cheap (often a small credit). The lopsided wings are why it's named after a tree: the payoff has an asymmetric, leaning silhouette.

**When & why to use it.** Use it when you have a directional target in mind — you think Nifty drifts up toward roughly 24300 by expiry but won't run away — and you want a cheap, defined bet that profits if you're right and costs almost nothing if you're wrong. Low net outlay makes it attractive when IV is moderate. Skip it for explosive breakout views; the upper wing caps and then erodes your gain past the peak.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 3x 24300 CE @ 292, buy 2x 24600 CE @ 167. Net credit 85.3 points = about ₹6,398 per lot collected up front. The structure peaks near the 24300 short strike.

![Figure: Christmas Tree Butterfly (Call) payoff at expiry](figs/strategies/christmas_tree_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 382 points (~₹28,650/lot) near the 24300 target. Max loss -215 points (~₹16,125/lot). Breakeven 24493. Net credit 85.3 points. Risk:reward 1.78 — a genuinely favourable defined-risk ratio.

**Greeks & behaviour.** Net delta positive (bullish lean), theta positive near the body once price sits under the peak, vega negative. The position wants Nifty to grind toward 24300 and pin; it behaves like a directional butterfly with extra short gamma in the upper wing.

**Management & exit.** Take profit if Nifty reaches the peak zone and the structure shows 50-70% of max — these pin trades give back gains fast if price overshoots. Cut if it breaks above 24600 toward the descending wing. Close before expiry-week gamma whip.

**Risk note.** Defined risk both ways (the 215-point max loss is real and capped), so the danger is mostly opportunity cost and the extra leg slippage of a six-contract structure — fill it as a package, not leg by leg, to control NSE bid-ask drag.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹6,375 | +₹6,375 | +₹6,375 | -₹16,125 | -₹16,125 |

Risk is fully defined both ways — you keep the small +₹6,375 credit on any close at or below 24000 and lose a capped -₹16,125 if Nifty pushes past the descending upper wing — and nothing worsens beyond the grid because every leg is part of a defined call structure.

**Adjustments, variants & timing.** Because this 1-3-2 leans bullishly toward roughly 24300, the management is target-driven: take 50-70% of max if Nifty grinds into the peak zone, since these skewed flies give back gains fast on overshoot. Cut the trade if price breaks above 24600 into the falling wing where the structure flips to its capped loss. There's no naked leg to defend, so the only real enemy is execution — fill all six contracts as one package to avoid NSE bid-ask drag, and don't leg in. Use it in moderate IV when you have a specific upside target rather than a breakout view; the small net credit makes it cheap to be wrong. Strongly prefer Nifty: its tighter strike grid and deeper liquidity keep the six-leg slippage manageable, whereas Bank Nifty's wider strikes and thinner far-OTM calls can erode the modest edge. Roll the whole structure up a strike set if your bullish target shifts higher before expiry week.

## 160. Christmas Tree Butterfly (Put)
*Bearish to a target · Short vega · net credit*

**The idea (intuition).** Same 1-3-2 idea on the put side: buy one higher put, sell three at a middle strike, buy two lower. It's a cheap, skewed, defined-risk bet that leans toward a downside target — the put-side mirror of strategy 159.

**When & why to use it.** Deploy it when you expect a measured drift lower — Nifty easing toward roughly 23700 by expiry without crashing. It gives you a low-cost (here a small credit) bearish position that profits in a target zone and loses little if you're wrong. Best in moderate IV. Avoid it for crash views; like all butterflies, the lower wing turns your big down-move back into a loss past the peak.

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 3x 23700 PE @ 219, buy 2x 23400 PE @ 148. Net credit 42.9 points = about ₹3,218 per lot. The profit peaks near the 23700 short strike.

![Figure: Christmas Tree Butterfly (Put) payoff at expiry](figs/strategies/christmas_tree_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 336 points (~₹25,200/lot) near the 23700 target. Max loss -257 points (~₹19,275/lot). Breakeven 23529. Net credit 42.9 points. Risk:reward 1.31.

**Greeks & behaviour.** Net delta negative (bearish lean), theta positive once price sits inside the body, vega negative. The structure rewards a controlled slide into the peak and short gamma in the lower wing.

**Management & exit.** Bank 50-70% of max if Nifty reaches the peak zone — don't be greedy, these reverse quickly on overshoot. Exit if it accelerates below 23400 into the falling wing. Take it off before the final expiry session's gamma noise.

**Risk note.** Risk is fully defined at 257 points, so the real cost is execution: a six-leg put package on Nifty can suffer meaningful slippage, and far OTM put strikes can be thin — trade liquid monthly strikes and price it as one spread.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹19,275 | -₹19,275 | +₹3,225 | +₹3,225 | +₹3,225 |

The put-side mirror — you keep the small +₹3,225 credit on any close at or above 24000 and the capped -₹19,275 loss appears only if Nifty falls past the lower wing toward 22,800 — and the loss does not deepen beyond the grid because the structure is fully defined.

**Adjustments, variants & timing.** This 1-3-2 leans bearishly toward roughly 23700, so manage to the target: bank 50-70% of max if Nifty slides into the peak zone, and don't get greedy because the skewed fly reverses quickly on overshoot. Exit if price accelerates below 23400 into the lower falling wing. No naked leg means execution is the only real risk — price the six puts as a single package and stick to liquid monthly strikes, since far-OTM Nifty puts can be thin. Deploy in moderate IV when you expect a measured drift down rather than a crash; the tiny net credit keeps the cost of being wrong negligible. Nifty is the right vehicle for its strike depth and tighter spreads; Bank Nifty's thinner low-delta puts make the six-leg fill expensive and can swamp the small edge. If your downside target moves lower before expiry, roll the entire fly down a strike set rather than adjusting individual legs.

## 161. ZEBRA (Zero-Extrinsic Back-Ratio, Call)
*Bullish, stock proxy · Low vega · net debit*

**The idea (intuition).** A ZEBRA — Zero-Extrinsic Back-Ratio — buys two in-the-money calls and sells one at-the-money call so that the long deltas total roughly +100 (one synthetic long unit) while the premium you sell offsets almost all the time value you bought. The result behaves like owning the index outright but with defined, limited downside and almost no theta bleed. It's a clean "stock replacement."

**When & why to use it.** Use it when you want long exposure to Nifty/Bank Nifty without paying the full index outlay or carrying margin on futures, and you dislike the time decay of a plain long call. Because extrinsic value nets to near zero, IV level barely matters — good in either vol regime. Ideal as a directional core you can hold. Don't use it if you want leverage to a sudden vol spike; vega is deliberately low.

**How to build it (₹, Nifty).** Buy 2x 23600 CE @ 728, sell 24000 CE @ 456. Net debit 999.3 points = about ₹74,948 per lot. That debit is your entire risk; above breakeven you gain point-for-point like long stock.

![Figure: ZEBRA (Zero-Extrinsic Back-Ratio, Call) payoff at expiry](figs/strategies/zebra_call.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (it's a net-long-delta position). Max loss -999 points (~₹74,925/lot), the full debit, only if Nifty sits at or below 23600 at expiry. Breakeven 24199. Net debit 999.3 points. Risk:reward null (upside open).

**Greeks & behaviour.** Net delta about +100 (full long unit), theta near zero by design (the sold call funds the bought time value), vega low. P&L tracks the index almost one-for-one above breakeven — that's the whole point.

**Management & exit.** Manage it like a stock position: trail a stop, take profit at your price target, or roll the strikes up to lock gains and re-center the +100 delta. No urgent expiry-week decay panic since theta is minimal, but close or roll before expiry to avoid pin risk on the short call.

**Risk note.** The defined loss is the full 999-point debit if Nifty closes below your lower long strike — a real, sizable rupee figure. Treat it as a leveraged long: a sharp index drop loses the whole premium, so position-size as you would for an equivalent futures long.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹74,925 | -₹74,925 | -₹14,925 | +₹30,075 | +₹75,075 |

The payoff tracks the index almost one-for-one — the full -₹74,925 debit is lost flat below 23600 and the gain rises about ₹75 per point above breakeven — so beyond the grid the upside keeps climbing without limit while the loss is already capped at the debit.

**Adjustments, variants & timing.** Manage a ZEBRA exactly like a leveraged long future: trail a stop, take profit at your price target, or roll both long strikes up to lock gains and re-centre the +100 delta. Because extrinsic value nets to near zero, theta is minimal, so there's no expiry-week decay panic — but still roll or close before expiry to avoid pin risk on the short 24000 call. The structure is genuinely vol-agnostic (vega is deliberately low), so don't wait for an IV setup; the only entry criterion is a sustained bullish view where you'd otherwise buy futures but prefer defined downside and lower margin. It suits being a directional core you can hold for weeks. Both Nifty and Bank Nifty work, but Bank Nifty's wider strikes mean the two ITM longs tie up more premium per lot, so the rupee debit (and thus max loss) is larger — size the lot count to the rupee risk you'd accept on an equivalent index-future long, not to the point count.

## 162. ZEBRA (Put)
*Bearish, stock proxy · Low vega · net debit*

**The idea (intuition).** The put-side ZEBRA: buy two ITM puts, sell one ATM put, to manufacture roughly -100 delta — a synthetic short index unit — with the extrinsic value bought and sold cancelling out. It's the clean short-stock proxy with limited, defined risk and minimal time decay.

**When & why to use it.** Use it for a sustained bearish view on Nifty/Bank Nifty when you'd otherwise short futures but want capped risk and no theta drag. Vol-agnostic because extrinsic nets to near zero. Good as a core bearish hold or a portfolio hedge with a hard maximum loss. Avoid if your edge is a vol explosion — vega is intentionally small, so you won't profit much from an IV spike alone.

**How to build it (₹, Nifty).** Buy 2x 24400 PE @ 506, sell 24000 PE @ 318. Net debit 693.5 points = about ₹52,013 per lot — your full risk. Below breakeven you gain point-for-point like short stock.

![Figure: ZEBRA (Put) payoff at expiry](figs/strategies/zebra_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 24106 points (the bounded figure if Nifty fell to zero). Max loss -693 points (~₹51,975/lot), the full debit. Breakeven 24053. Net debit 693.5 points. Risk:reward 34.76 — flattering because the "max profit" assumes an index collapse.

**Greeks & behaviour.** Net delta about -100 (full short unit), theta near zero by design, vega low. The position tracks the index inversely below breakeven, behaving like a defined-risk short future.

**Management & exit.** Trade it like a short: cover at your downside target, trail a stop, or roll the puts down to lock gains and re-center -100 delta. Theta is benign, but close or roll before expiry to dodge pin risk on the short put.

**Risk note.** The 34.76 risk:reward and the 24106-point "max profit" both assume Nifty going to zero — not a real target. The genuine outcome is: defined max loss of the 693-point debit if Nifty rallies above your long strikes. Size it as a leveraged short and respect that a rally can take the whole premium.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹98,025 | +₹53,025 | +₹8,025 | -₹51,975 | -₹51,975 |

The put-side ZEBRA tracks the index inversely — gains rise about ₹75 per point as Nifty falls and the loss caps at the -₹51,975 debit above the long strikes — so below the grid the profit keeps growing while the upside risk is already fixed at the debit.

**Adjustments, variants & timing.** Trade it like a defined-risk short future: cover at your downside target, trail a stop, or roll both long puts down to lock gains and re-centre the -100 delta. Theta is benign by design, so there's no decay urgency, but close or roll before expiry to dodge pin risk on the short 24000 put. Vega is intentionally small, so it's vol-agnostic — enter on a sustained bearish view or as a portfolio hedge with a hard maximum loss, not on an IV signal. This is the cleaner way to be short Indian indices than short futures because gap-downs (the violent direction here) can't blow past your defined max loss on the long side; your only real risk is a rally chewing through the debit. Both indices work; Bank Nifty's wider strikes make the debit (and max loss) larger in rupees, so size the lots to the rupee risk you'd accept on an equivalent short future rather than the point figure.

## 163. Risk Reversal (Bullish)
*Bullish · Skew play · net debit*

**The idea (intuition).** A bullish risk reversal sells an OTM put to finance buying an OTM call — synthetic long exposure built almost for free. The reason it exists: index options carry a volatility skew where downside puts are pricier than upside calls, so selling the "expensive" put pays for the "cheap" call. You're trading the skew, not just direction.

**When & why to use it.** Use it when you're outright bullish on Nifty/Bank Nifty and put skew is steep (fear elevated, India VIX up, puts bid). The richer the put relative to the call, the closer to zero-cost — or even a credit — the structure becomes, giving leveraged upside for little outlay. Great as a cheap leveraged long into an expected up-move. Do NOT use it if you're not prepared to be effectively long from the put strike down — a crash hurts exactly like being long.

**How to build it (₹, Nifty).** Sell 23700 PE @ 219, buy 24300 CE @ 292. Net debit just 73.2 points = about ₹5,490 per lot — almost free synthetic-long exposure thanks to the skew.

![Figure: Risk Reversal (Bullish) payoff at expiry](figs/strategies/risk_reversal_bull.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (long call, open upside). Max loss -23772 points only on a collapse to zero (driven by the short put). Breakeven 24373. Net debit 73.2 points. Risk:reward null (upside open).

**Greeks & behaviour.** Net delta strongly positive (synthetic long), theta roughly flat (long call decay offset by short put decay), vega mixed but small net. The position lives and dies on direction — it's a directional play dressed in a skew trade.

**Management & exit.** Manage like a leveraged long: take profit at your target, trail a stop. Defend the short put if Nifty drops toward 23700 — roll it down-and-out or buy a lower put to cap. Close before expiry to avoid assignment on the short put.

**Risk note.** Worst case assumes a fall to zero; in practice you stop at a multiple of the premium. The honest danger: below 23700 you have a naked short put with effectively long-index risk, so a gap-down can hurt as much as being long futures. Size accordingly.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹72,975 | -₹27,975 | -₹5,475 | +₹17,025 | +₹62,025 |

This trades like a synthetic long — upside rises about ₹75 per point above the call strike — but the -₹72,975 at 22,800 is not the floor: below 23700 the naked short put adds full long-index risk, so a deeper fall loses about ₹75 per further point.

**Adjustments, variants & timing.** Manage it like a leveraged long: take profit at your target, trail a stop. The exposed leg is the short 23700 put — if Nifty drops toward it, roll the put down-and-out or buy a lower put to cap the downside into a defined structure. Close before expiry to avoid assignment. The whole point is the skew: build it when put skew is steep (fear elevated, India VIX up, downside puts bid richer than upside calls) so the sold put almost fully funds the long 24300 call, giving near-zero-cost leveraged upside — sometimes even a credit. That makes it the right tool when you're outright bullish and willing to be effectively long from 23700 down. Nifty is the standard vehicle; Bank Nifty offers a steeper skew (so cheaper entry) but a gap-down through the short put hurts far more, so size Bank Nifty smaller and treat the short put's risk as identical to a long futures position of the same notional.

## 164. Risk Reversal (Bearish)
*Bearish · Skew play · net credit*

**The idea (intuition).** The bearish risk reversal sells an OTM call to finance a long OTM put — synthetic short exposure, and here you even collect a small credit. You're harvesting the same skew from the other side: selling a call and buying a put when the structure works in your favour.

**When & why to use it.** Use it for an outright bearish view when you can build the position at or near zero-cost (or a credit). It gives leveraged downside participation cheaply. Best when you expect a real decline rather than a grind. Don't use it if a rally is plausible — above the call strike you're effectively short the index with open-ended risk.

**How to build it (₹, Nifty).** Buy 23700 PE @ 219, sell 24300 CE @ 292. Net credit 73.2 points = about ₹5,490 per lot received — you're paid to put on a synthetic short.

![Figure: Risk Reversal (Bearish) payoff at expiry](figs/strategies/risk_reversal_bear.png)

**The numbers (modelled at Nifty 24000).** Max profit 23772 points (the bounded zero-floor figure from the long put). Max loss Undefined — large (the naked 24300 call is open above). Breakeven 24373. Net credit 73.2 points. Risk:reward null — one side is unlimited.

**Greeks & behaviour.** Net delta strongly negative (synthetic short), theta roughly flat, vega small net. It's a directional bearish bet; the skew just makes the entry cheap or free.

**Management & exit.** Manage like a leveraged short: cover at target, trail a stop. The defence is all on the naked call — roll it up-and-out if Nifty rallies toward 24300, or buy a higher call to define the risk. Close before expiry to avoid assignment.

**Risk note.** This is genuinely unlimited to the upside — a strong rally runs the naked short call without bound. The 23772 "max profit" is the index-to-zero artefact, not a target. Trade small and pre-plan the upside roll; a surprise risk-on gap is the killer here.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹72,975 | +₹27,975 | +₹5,475 | -₹17,025 | -₹62,025 |

This is a synthetic short — gains rise about ₹75 per point as Nifty falls — but the -₹62,025 at 25,200 is not the floor: above 24300 the naked short call runs without bound, losing about ₹75 per further point in a rally.

**Adjustments, variants & timing.** Manage like a leveraged short: cover at target, trail a stop. All defence is on the naked 24300 call — roll it up-and-out if Nifty rallies toward the strike, or buy a higher call to define the risk into a spread. Set a hard 2x-credit stop and pre-stage the roll, since a surprise risk-on gap is the killer. Close before expiry to avoid assignment. The structure is a skew harvest: put it on when call premium relative to puts lets you build at or near zero-cost (or a credit) for an outright bearish view, ideally expecting a real decline rather than a grind. Because the open tail is to the upside while Indian indices gap down harder, the protected direction is unfortunately the violent one — so the rare trending rally is your true risk. Nifty is the safer instrument; Bank Nifty's faster upside trends make the naked call dangerous, so halve the size and keep the roll trigger tight.

## 165. Seagull (Bullish)
*Bullish, cost-reduced · Mixed vega · net debit*

**The idea (intuition).** A bullish seagull is a bull call spread whose cost is reduced by selling a far OTM put underneath. Three legs — long call, short higher call, short lower put — give a shape with two "wings" and a body, like a bird in flight. It exists to make directional upside almost free by financing the debit spread with put premium.

**When & why to use it.** Use it when you're bullish but want defined upside (the short call caps it) and you're willing to take on some downside obligation (the short put) to cheapen the trade. Good when put skew is rich so the sold put pays well. Suits a moderate-IV bullish view with a target near the short call. Avoid it if you fear a sharp sell-off — the short put leaves a cushioned but real downside tail.

**How to build it (₹, Nifty).** Sell 23500 PE @ 169, buy 24000 CE @ 456, sell 24400 CE @ 246. Net debit just 41.5 points = about ₹3,113 per lot — the short put nearly pays for the call spread.

![Figure: Seagull (Bullish) payoff at expiry](figs/strategies/seagull_bull.png)

**The numbers (modelled at Nifty 24000).** Max profit 358 points (~₹26,850/lot), capped at the 24400 short call. Max loss -23541 points only on a collapse to zero (from the short 23500 put). Breakeven 24042. Net debit 41.5 points. Risk:reward 0.02 — the zero-floor artefact again.

**Greeks & behaviour.** Net delta positive (bullish), theta roughly flat to slightly positive, vega mixed (long the call spread's vega, short the put's). Between the strikes it behaves like a capped bullish position; below 23500 the short put dominates.

**Management & exit.** Take profit as Nifty approaches the 24400 cap. Defend the short put if price slides toward 23500 — roll down-and-out or buy a lower put. Close before expiry to avoid put assignment.

**Risk note.** Worst case assumes a fall to zero; realistically you stop at a multiple of the cost. The real exposure is the naked short put below 23500 — a gap-down assigns you long the index at that strike. Size for the downside, not the tiny debit.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹55,650 | -₹10,650 | -₹3,150 | +₹26,850 | +₹26,850 |

The bull call spread caps the gain at +₹26,850 above 24400, but the -₹55,650 at 22,800 is not the floor — below 23500 the naked short put keeps losing about ₹75 per point, so a move beyond the grid loses far more.

**Adjustments, variants & timing.** Take profit as Nifty approaches the 24400 cap, where the upside is fully realised. The only exposed leg is the short 23500 put: if price slides toward it, roll the put down-and-out for a credit or buy a lower put to convert the open tail into a defined iron structure; close before expiry to avoid assignment that would leave you long the index at 23500. The cost-reduction logic depends on rich put skew — sell it when the far-OTM 23500 put is bid up by fear so it nearly pays for the 24000/24400 call spread, giving almost-free capped upside. That makes it the right tool for a moderate-IV bullish view with a defined target around 24400 and a tolerance for cushioned downside. Nifty suits the three-leg fill best; Bank Nifty's richer skew funds the spread more fully but its gap-downs make the short put genuinely dangerous, so size for the downside notional rather than the tiny debit, and reduce lots on Bank Nifty.

## 166. Seagull (Bearish)
*Bearish, cost-reduced · Mixed vega · net credit*

**The idea (intuition).** The bearish seagull is a bear put spread financed by selling a far OTM call above. Long put, short lower put, short higher call — the sold call cheapens (here more than pays for) the debit spread, giving low-cost defined downside with an open tail above.

**When & why to use it.** Use it for a bearish view when you want a defined profit zone on the downside (the short put caps the gain) and you'll accept upside obligation from the short call to fund it. Works best when call skew or overall premium lets the sold call cover the put-spread cost — here you even bank a credit. Avoid ahead of bullish catalysts; the naked call is your open risk.

**How to build it (₹, Nifty).** Sell 24500 CE @ 204, buy 24000 PE @ 318, sell 23600 PE @ 192. Net credit 78.2 points = about ₹5,865 per lot received.

![Figure: Seagull (Bearish) payoff at expiry](figs/strategies/seagull_bear.png)

**The numbers (modelled at Nifty 24000).** Max profit 478 points (~₹35,850/lot), capped at the 23600 short put. Max loss Undefined — large (naked 24500 call above). Breakeven 24578. Net credit 78.2 points. Risk:reward null — one side is unlimited.

**Greeks & behaviour.** Net delta negative (bearish), theta roughly flat, vega mixed. Between strikes it's a capped bearish payoff; above 24500 the naked call drives an open-ended loss.

**Management & exit.** Bank the profit as Nifty approaches the 23600 cap. All defence is on the short call — roll it up-and-out if price climbs toward 24500, or buy a higher call to define it. Close before expiry to avoid assignment.

**Risk note.** Honestly unlimited above 24500 — a strong rally runs the naked call without bound. Don't treat the small credit as the risk; size for a worst-case up-gap and have the call roll ready.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹35,850 | +₹35,850 | +₹5,850 | -₹1,650 | -₹46,650 |

The bear put spread caps the gain at +₹35,850 below 23600, but the -₹46,650 at 25,200 is not the floor — above 24500 the naked short call runs without bound, losing about ₹75 per further point in a rally.

**Adjustments, variants & timing.** Bank the profit as Nifty approaches the 23600 cap. All defence is on the naked 24500 call — roll it up-and-out if price climbs toward the strike, or buy a higher call to define the upside into an iron structure; close before expiry to avoid assignment. The financing logic wants overall premium or call skew rich enough that the sold call more than covers the 24000/23600 put spread (here you bank a credit), so deploy it when premium is fat and you hold a bearish view expecting a real decline. The open tail is to the upside, the rarer but more damaging direction when it hits, so never size off the small credit — size for a worst-case up-gap and pre-stage the roll. Nifty is the cleaner three-leg fill; Bank Nifty pays a bigger credit but its faster rallies make the naked call riskier, so reduce lots and tighten the roll trigger there. Avoid the trade entirely ahead of a known bullish catalyst.

## 167. Batman (Double Butterfly)
*Range with twin targets · Short vega · net debit*

**The idea (intuition).** A batman is two OTM butterflies — one on the call side, one on the put side — placed so the payoff has two profit "peaks" with a dip between them, like the silhouette of a bat's ears (or the logo). It pays best if the index lands near one of two distinct levels rather than dead-center, making it a twin-target range bet.

**When & why to use it.** Use it when you expect Nifty to move to one of two zones away from the current price by expiry — for example, settling near 23600 or near 24400 — but not stay pinned exactly at 24000 and not break far outside the wings. Cheap, fully defined risk. Suits a range-bound-but-not-static view in moderate IV. Avoid it if you expect a hard pin at the money (you'd want a single ATM butterfly) or a big trend.

**How to build it (₹, Nifty).** Buy 24200 CE @ 342, sell 2x 24400 CE @ 246, buy 24600 CE @ 167 (call fly), and buy 23800 PE @ 248, sell 2x 23600 PE @ 192, buy 23400 PE @ 148 (put fly). Net debit 29.5 points = about ₹2,213 per lot — tiny, fully defined cost.

![Figure: Batman (Double Butterfly) payoff at expiry](figs/strategies/batman.png)

**The numbers (modelled at Nifty 24000).** Max profit 170 points (~₹12,750/lot) at either peak (near 23600 or 24400). Max loss -29 points (~₹2,175/lot), the full debit. Breakevens 23429, 23771, 24229, 24571 (four crossings — the twin-peak shape). Net debit 29.5 points. Risk:reward 5.76 — excellent for defined risk.

**Greeks & behaviour.** Net delta near zero at inception (balanced two-sided), theta positive once price approaches either body, vega negative. Short gamma at each peak — gains evaporate if price overshoots a wing.

**Management & exit.** Take profit if Nifty reaches one peak and the structure shows 50-70% of max. This is a precise, twelve-contract package — exit before expiry-week gamma turns the peaks into knife-edges. Don't overstay near a wing edge.

**Risk note.** Risk is fully capped at the 29-point debit, so the danger is execution, not blow-up: a six-strike package on Nifty carries real slippage and the outer strikes can be thin. Always trade it as one spread, never leg by leg.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹2,175 | -₹2,175 | -₹2,175 | -₹2,175 | -₹2,175 |

The grid lands in the dead zones between and outside the two peaks, so it shows the flat -₹2,175 full-debit loss everywhere — the twin profit humps near 23600 and 24400 fall between these sampled strikes — and nothing worsens beyond the grid because risk is fully defined.

**Adjustments, variants & timing.** This twin-target structure pays only if Nifty lands near one of the two peaks (here ~23600 or ~24400), so manage to a peak: take profit at 50-70% of max if price reaches one body, and don't overstay near a wing edge where short gamma evaporates the gain on overshoot. With no naked leg, the entire risk is execution — it's a twelve-contract package, so fill it as one spread, never leg by leg, and stick to liquid monthly strikes since the outer wings can be thin. The right setup is a range-bound-but-not-static view in moderate IV: you expect Nifty to drift to one of two zones away from the current 24000, but not pin dead-centre (use a single ATM fly for that) and not trend hard out of the wings. Strongly prefer Nifty — its tight strike grid and deep liquidity are essential for filling twelve legs cheaply; Bank Nifty's wider, thinner strikes make the slippage on a double fly punishing. Roll one fly's strikes if your two target zones shift.

## 168. Iron Albatross (Ultra-Wide Condor)
*Broadly range-bound · Short vega · net credit*

**The idea (intuition).** An iron albatross is just an iron condor with the short strikes pushed far out and wide — a big bird with a long wingspan. You collect a smaller credit than a tight condor, but the profit zone is enormous, so the position almost never gets tested. It trades a modest premium for a high probability of keeping it.

**When & why to use it.** Use it when you want steady, high-probability income and are willing to accept a small credit for a wide margin of safety — Nifty expected to stay broadly range-bound. Good in normal-to-elevated IV where even far strikes pay something. Suits traders who hate getting tested every week. Don't use it when premium is thin (the far strikes pay too little to justify the defined risk) or when you expect a big trending move.

**How to build it (₹, Nifty).** Sell 24700 CE @ 135, buy 25200 CE @ 33, sell 23300 PE @ 129, buy 22800 PE @ 64. Each spread is 500 wide. Net credit 165.8 points = about ₹12,435 per lot.

![Figure: Iron Albatross (Ultra-Wide Condor) payoff at expiry](figs/strategies/iron_albatross.png)

**The numbers (modelled at Nifty 24000).** Max profit 166 points (~₹12,450/lot), kept if Nifty stays between the short strikes. Max loss -334 points (~₹25,050/lot), fully defined. Breakevens 23134 and 24866. Net credit 165.8 points. Risk:reward 0.5 — you risk 334 to make 166, the price of a wide, high-probability zone.

**Greeks & behaviour.** Net delta near zero, theta positive (premium decay), vega negative. The wide profit band means low gamma until price nears a far strike; it's a slow, steady income shape.

**Management & exit.** Because the credit is small relative to risk, manage tightly — take profit at ~50% and don't let a tested side run, since the 2:1 loss-to-credit ratio means one bad expiry erases two good ones. Roll the tested spread out or close if a breakeven is threatened.

**Risk note.** Defined risk both sides (max loss 334 points), so no blow-up — but the unfavourable risk:reward is the catch: you must win often to come out ahead, and a single trend through 24700 or 23300 costs twice the credit. Discipline on the stop matters more here than on richer condors.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹25,050 | +₹12,450 | +₹12,450 | +₹12,450 | -₹25,050 |

The wide zone keeps the full +₹12,450 credit across the whole 23,400-24,600 middle and the defined -₹25,050 max loss appears only at the far 22,800 and 25,200 wings — and risk does not worsen beyond the grid because both spreads are capped.

**Adjustments, variants & timing.** Because the credit is small relative to the 2:1 defined risk, discipline is everything: take profit at ~50% and never let a tested side run, since one bad expiry erases two good ones. If a breakeven (23134 / 24866) comes into play, roll the tested spread out or close it rather than hoping. There are no naked legs, so this is purely a probability-and-discipline trade. The setup is steady high-probability income in normal-to-elevated IV where even the far 24700/23300 short strikes still pay something — if premium is thin, the credit won't justify the defined risk and you should skip it. It suits traders who value not being tested over collecting much, expecting Nifty to stay broadly range-bound. Both indices work, but Bank Nifty's higher premium often makes the far strikes pay enough to be worthwhile, whereas on Nifty you may need elevated IV to get a meaningful credit at such wide strikes. Avoid it ahead of any expected trending move.

## 169. Slingshot (Call Backspread)
*Bullish breakout · Long vega · net debit*

**The idea (intuition).** A slingshot is a skewed call ratio backspread — sell one near call, buy two further calls — structured for near-zero cost but explosive upside. You're net long extra calls, so a big rally launches the P&L like a slingshot, while a quiet or down market costs little. The single short call funds most of the two longs.

**When & why to use it.** Use it when you expect a sharp upside breakout in Nifty/Bank Nifty and want long gamma and long vega cheaply — ahead of a catalyst (results, policy, breakout from consolidation) where a big move and a vol pop are both plausible. Best entered when IV is low so the long calls are cheap. Don't use it for a slow grind up; the worst outcome is price stalling in the dead zone at the short strike.

**How to build it (₹, Nifty).** Sell 24100 CE @ 397, buy 2x 24400 CE @ 246. Net debit 94.6 points = about ₹7,095 per lot. The extra long call gives unlimited upside above breakeven.

![Figure: Slingshot (Call Backspread) payoff at expiry](figs/strategies/slingshot_call.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (net long an extra call). Max loss -387 points (~₹29,025/lot), occurring if Nifty pins at the 24400 long strike. Breakeven 24795 (upside). Net debit 94.6 points. Risk:reward null (upside open).

**Greeks & behaviour.** Net delta positive and rising with price (long gamma), theta negative (you pay to hold), vega positive — a rise in IV helps even before the move. The defining trait: the max loss sits at the long strike, not at the extremes.

**Management & exit.** This is a catalyst trade — give it a defined window and exit if the move doesn't come, because theta bleeds the long calls. Take profits into a sharp rally rather than waiting for "more." Avoid carrying it into the dead-zone pin near 24400 at expiry.

**Risk note.** Defined max loss of 387 points, but note the trap: the *worst* result is a moderate rally that parks Nifty right at 24400, not a crash. Long theta bleed and the pin risk at the long strike are the real dangers, not unlimited loss.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹7,125 | -₹7,125 | -₹7,125 | -₹14,625 | +₹30,375 |

The backspread shows its trap clearly — quiet or down markets cost only the small -₹7,125, the worst cell is the -₹14,625 partial pin near the 24400 long strike, and the +₹30,375 at 25,200 keeps rising about ₹75 per point beyond the grid as the extra long call runs.

**Adjustments, variants & timing.** This is a catalyst trade, so give it a defined window and exit if the breakout doesn't arrive, because theta bleeds the long calls daily. Take profits into a sharp rally rather than waiting for more, and crucially avoid carrying it into the expiry-week dead-zone pin near 24400, which is the maximum-loss spot. There's no unlimited-loss tail (you're net long an extra call), so the real management is timing, not defence. Enter when IV rank is low so the two long 24400 calls are cheap, and when you expect both a sharp upside breakout and a likely vol pop — ahead of results, policy, or a breakout from tight consolidation, where price and IV can expand together (long gamma plus long vega). Bank Nifty is often the better vehicle here: its larger, faster directional moves and richer vol expansion pay backspreads more handsomely than Nifty's tamer breakouts, though you can run the same structure on Nifty in lower size when its IV is unusually cheap.

## 170. Slingshot (Put Backspread)
*Bearish breakdown · Long vega · net debit*

**The idea (intuition).** The put-side slingshot: sell one near put, buy two lower puts, built cheaply for a violent downside breakout. You're net long an extra put, so a crash launches the P&L while a flat or up market costs little. It's a cheap "crash kicker."

**When & why to use it.** Use it when you expect a sharp breakdown and a vol spike in Nifty/Bank Nifty — these are the moves that pay backspreads handsomely because skew and IV both expand as the market falls. Enter when IV is low so the long puts are cheap. Excellent as a tail hedge for a long book. Don't use it for a slow drift down; the dead-zone pin at the long strike is the worst case.

**How to build it (₹, Nifty).** Sell 23900 PE @ 282, buy 2x 23600 PE @ 192. Net debit 102.9 points = about ₹7,718 per lot. The extra long put delivers large downside payoff.

![Figure: Slingshot (Put Backspread) payoff at expiry](figs/strategies/slingshot_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 23196 points (the bounded zero-floor figure as Nifty falls). Max loss -402 points (~₹30,150/lot), at a 23600 pin. Breakeven 23197. Net debit 102.9 points. Risk:reward 57.65 — flattering, since the "max profit" assumes a near-total index collapse.

**Greeks & behaviour.** Net delta negative and growing as price falls (long gamma), theta negative, vega positive — a vol spike on the way down adds to the gain. As with the call version, max loss sits at the long strike, not the extremes.

**Management & exit.** Treat it as a catalyst/hedge trade with a defined holding window; exit if the breakdown doesn't arrive, since theta erodes the long puts. Bank profits into a fast crash. Keep it off the expiry-week pin near 23600.

**Risk note.** Defined max loss of 402 points. The 57.65 risk:reward and 23196 "max profit" both assume a collapse toward zero — not a target. The genuine pitfalls are theta bleed and a moderate sell-off that pins price at 23600, handing you the maximum defined loss.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹29,775 | -₹15,225 | -₹7,725 | -₹7,725 | -₹7,725 |

The put backspread mirrors the call version — flat or up markets cost only -₹7,725, the worst cell is the partial pin near the 23600 long strike (the -₹15,225 at 23,400), and the +₹29,775 at 22,800 keeps growing about ₹75 per point below the grid as the extra long put runs.

**Adjustments, variants & timing.** Treat it as a catalyst or tail-hedge trade with a defined holding window: exit if the breakdown doesn't arrive, since theta erodes the long puts, and bank profits into a fast crash rather than waiting. Keep it off the expiry-week pin near 23600, which is the maximum-loss spot. There's no naked tail (you're net long an extra put), so the management is timing and the dead-zone pin, not unlimited risk. Enter when IV rank is low so the two long 23600 puts are cheap, expecting a sharp breakdown plus a vol spike — the moves that pay put backspreads best because skew and IV both expand as the market falls. It's excellent as a cheap tail hedge bolted onto a long cash or futures book. Bank Nifty is the natural fit: its faster, deeper sell-offs and sharper vol expansion reward the convex wing far more than Nifty's gentler declines, though Nifty works in lower size when its IV is unusually depressed and you want index-level protection.

## 171. Call Ratio Calendar
*Pin, rising IV · Long vega · net credit*

**The idea (intuition).** A call ratio calendar sells two front-month calls against one longer-dated call at the same strike. It's a calendar spread with extra short premium — you harvest fast front-month decay while staying net long vega via the back-month call. The ratio juices the credit but adds a naked short on the front.

**When & why to use it.** Use it when you expect Nifty to pin near the strike into the front expiry while back-month IV stays firm or rises — a classic "front decays, term structure holds" setup. The long back-month call benefits if IV rises; the two short fronts pay you theta. Good around 24000 when you expect range now but want vega exposure. Don't use it ahead of a breakout — the extra short front call is naked and uncapped on a rally.

**How to build it (₹, Nifty).** Sell 2x 24000 CE @ 456 (front), buy 24000 CE @ 689 (back). Net credit 223.2 points = about ₹16,740 per lot.

![Figure: Call Ratio Calendar payoff at expiry](figs/strategies/call_ratio_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 671 points (~₹50,325/lot) near a 24000 pin at front expiry. Max loss Undefined — large (the extra naked front call is open above). Breakeven 24508. Net credit 223.2 points. Risk:reward null — one side is unlimited.

**Greeks & behaviour.** Net delta roughly flat near the strike, theta positive (front decay outweighs back), vega positive (net long the back-month). The position wants a pin plus steady-or-rising IV; a rally is the enemy.

**Management & exit.** Manage and close the position before or at front expiry — never let the extra short front call go into expiry naked. Take profit at a pin; if Nifty rallies toward 24508, buy a front call to cap the ratio or roll up. Watch the calendar's vega P&L, not just the pin.

**Risk note.** Honestly unlimited above breakeven because of the extra short front call — a sharp rally beats the single long back call and runs. This is not a beginner set-and-forget; manage the tail actively and size for a gap.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹21,225 | +₹31,125 | +₹50,925 | -₹8,475 | -₹60,000 |

The calendar peaks at a 24000 pin (+₹50,925) and holds positive on the downside as the front calls expire worthless, but the -₹60,000 at 25,200 is not the floor — above breakeven the extra naked front call beats the single long back call and keeps losing without bound.

**Adjustments, variants & timing.** The cardinal rule: manage and close before or at front expiry — never let the extra short front call go into settlement naked. Take profit at a pin; if Nifty rallies toward 24508, buy a front call to cap the ratio into a defined calendar, or roll the whole structure up. Watch the position's vega P&L, not just the pin, because the long back-month call is your vega engine. The right setup is a "front decays, term structure holds" environment: you expect Nifty to pin near 24000 into the near expiry while back-month IV stays firm or rises, so the two short fronts pay theta and the long back gains on any IV lift. Don't deploy it ahead of a breakout — the extra short front is uncapped on a rally. Nifty is the safer instrument given its tamer trends; Bank Nifty's larger rallies make the naked front call dangerous, so size down there and pre-stage the cap. Size for a gap regardless — this is an actively managed trade, not set-and-forget.

## 172. Put Ratio Calendar
*Pin, rising IV · Long vega · net credit*

**The idea (intuition).** The put-side ratio calendar: sell two front-month puts against one longer-dated put at the same strike. You collect front-month decay while staying net long vega on the back month — with an extra short front put adding credit and a downside caveat.

**When & why to use it.** Use it when you expect Nifty to pin near the strike into front expiry while back-month IV holds or rises — and your tail worry is mild. The two short puts pay theta; the long back put gives vega. Good around 24000 for a range view with a vega tilt. Don't use it ahead of a sharp sell-off — the extra short front put is your exposed leg below.

**How to build it (₹, Nifty).** Sell 2x 24000 PE @ 318 (front), buy 24000 PE @ 414 (back). Net credit 222.4 points = about ₹16,680 per lot.

![Figure: Put Ratio Calendar payoff at expiry](figs/strategies/put_ratio_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 537 points (~₹40,275/lot) near a 24000 pin at front expiry. Max loss -23914 points only on a collapse to zero (the extra short front put). Breakeven 23637. Net credit 222.4 points. Risk:reward 0.02 — the zero-floor artefact.

**Greeks & behaviour.** Net delta roughly flat near the strike, theta positive, vega positive (net long the back-month put). It wants a pin and steady-or-rising IV; a fast drop hurts via the extra short front put.

**Management & exit.** Close before or at front expiry — don't leave the extra short put naked into settlement. Take profit at a pin; if Nifty slides toward 23637, buy a front put to cap the ratio or roll down. Track the calendar's vega, not just price.

**Risk note.** Worst case assumes a fall to zero; in reality you stop at a multiple of the credit. The real danger is a gap-down that overwhelms the single long back put with the two short fronts — short gamma below the strike. Size small and defend the downside.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹79,125 | -₹24,300 | +₹40,575 | +₹26,100 | +₹19,650 |

The calendar peaks at a 24000 pin (+₹40,575) and holds positive on the upside as the front puts expire worthless, but the -₹79,125 at 22,800 is not the floor — below breakeven the two short front puts overwhelm the single long back put, losing about ₹75 per further point on a deeper drop.

**Adjustments, variants & timing.** Close before or at front expiry — never leave the extra short front put naked into settlement. Take profit at a pin; if Nifty slides toward 23637, buy a front put to cap the ratio into a defined calendar, or roll the structure down. Track the calendar's vega, not just price, since the long back-month put carries your vega exposure. The setup is a range view with a vega tilt: you expect Nifty to pin near 24000 into front expiry while back-month IV holds or rises, and your tail fear is mild — the two short fronts pay theta while the long back gains on any IV lift. Don't use it ahead of a sharp sell-off; short gamma below the strike means a gap-down overwhelms the single long back put. Because Indian indices gap down harder than up, the exposed direction here is the dangerous one, so size small and defend the downside. Prefer Nifty for its softer declines; on Bank Nifty reduce lots and pre-stage the front-put cap.

## 173. Range Forward (Zero-Cost)
*Directional hedge · Neutral vega · net debit*

**The idea (intuition).** A range forward — the FX desk's zero-cost collar — takes a held long position and wraps it: buy an OTM put for protection and sell an OTM call to pay for it, ideally at net zero option cost. The underlying can only "travel" within a band: protected below the put, capped above the call. It's how you hold a position through uncertainty without paying for insurance.

**When & why to use it.** Use it on an existing long Nifty/Bank Nifty (or stock) position you want to keep but protect through an event — Budget, results, election count — without spending net premium. The sold call funds the bought put. Choose strikes to define an acceptable band. Don't use it if you want full upside; the short call caps your gains, and don't use it when you have no underlying — then it's just a risk reversal.

**How to build it (₹, Nifty).** Long 1x underlying @ 24000, buy 23600 PE @ 192, sell 24400 CE @ 246. The option legs are a small net credit (54 points) against the index; total net cost including the ~24000 outlay is 23946.4 points. Per lot the index leg is the bulk; the collar itself is near zero-cost.

![Figure: Range Forward (Zero-Cost) payoff at expiry](figs/strategies/range_forward.png)

**The numbers (modelled at Nifty 24000).** Max profit 454 points (~₹34,050/lot), capped at the 24400 short call. Max loss -346 points (~₹25,950/lot), floored at the 23600 long put. Breakeven 23946. Net debit 23946.4 points (includes the index). Risk:reward 1.31.

**Greeks & behaviour.** Net delta positive (you're long the underlying inside the band), theta and vega roughly neutral by design (long put offsets short call). Between the strikes you ride the index; outside, you're pinned to the band edges.

**Management & exit.** Hold it through the event window, then unwind the collar to free the underlying once risk passes. Roll the band up if Nifty rises and you want to keep participating; roll the put down to loosen protection. Close the short call before expiry to avoid capping a continued rally by assignment.

**Risk note.** Risk is defined by the band (max loss 346 points on the position), so the danger is mostly opportunity cost — a big rally past 24400 is forfeited to the short call. On stock names, watch STT on exercised ITM options and assignment on the short call near expiry.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹25,950 | -₹25,950 | +₹4,050 | +₹34,050 | +₹34,050 |

The collar pins the held long into a band — gains cap at +₹34,050 above the 24400 short call and losses floor at -₹25,950 below the 23600 long put — and nothing worsens beyond the grid because both edges of the band are fixed.

**Adjustments, variants & timing.** This wraps an existing long Nifty/Bank Nifty (or stock) position, so the management follows the underlying: hold it through the event window, then unwind the collar to free the position once risk passes. Roll the band up if Nifty rises and you want to keep participating, or roll the put down to loosen protection. Close the short 24400 call before expiry so a continued rally isn't capped by assignment. The setup is event-driven rather than IV-driven — Budget, results, election count — when you want to keep a position but not pay net premium for insurance; choose strikes to define an acceptable band, ideally letting the sold call fully fund the bought put for true zero cost. Don't use it without an underlying (then it's just a risk reversal) or when you want full upside. Both indices suit it; on stock names specifically, watch STT on exercised ITM options and assignment on the short call near expiry, and prefer cash-settled index collars to avoid delivery hassle.

## 174. Pterodactyl (Far-Wing Condor)
*Very broad range · Short vega · net credit*

**The idea (intuition).** The pterodactyl is an even wider iron condor than the albatross — short strikes pushed out to the far reaches with distant wings. The credit is minimal, but the profit zone is vast, so the position almost never gets tested. It's the maximal-zone, minimal-premium extreme of the condor family.

**When & why to use it.** Use it when you want the highest-probability range income and will accept a very small credit for an enormous margin of safety — Nifty expected to stay in a wide band. Best when far OTM strikes still carry enough premium to bother (elevated IV). Suits traders who prize not being tested over collecting much. Don't use it when premium is razor-thin (the tiny credit won't justify the defined risk) or when a large directional move is likely.

**How to build it (₹, Nifty).** Sell 25000 CE @ 124, buy 25500 CE @ 33, sell 23000 PE @ 136, buy 22500 PE @ 80. Each spread is 500 wide. Net credit 146.2 points = about ₹10,965 per lot.

![Figure: Pterodactyl (Far-Wing Condor) payoff at expiry](figs/strategies/pterodactyl.png)

**The numbers (modelled at Nifty 24000).** Max profit 146 points (~₹10,950/lot), kept if Nifty stays between the short strikes. Max loss -354 points (~₹26,550/lot), fully defined. Breakevens 22854 and 25146. Net credit 146.2 points. Risk:reward 0.41 — you risk 354 to make 146, the cost of an extremely wide zone.

**Greeks & behaviour.** Net delta near zero, theta positive, vega negative. Very low gamma across a huge band — the slowest, steadiest income shape in this group, until price approaches the far strikes.

**Management & exit.** With such a small credit against larger defined risk, discipline is everything: take profit at ~50%, and never let a tested side run, because one loss equals more than two wins. Roll the tested spread out or close if a breakeven (22854 / 25146) comes into play.

**Risk note.** Defined risk both sides (max loss 354 points) — no blow-up — but the poor risk:reward is the trade-off: you must win very frequently to net out ahead, and a rare move beyond 25000 or 23000 costs well over double the credit. Only worth it when far-strike premium is genuinely fat.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹4,050 | +₹10,950 | +₹10,950 | +₹10,950 | -₹4,050 |

The enormous zone keeps the full +₹10,950 credit across the whole sampled 23,400-24,600 middle, and even the far 22,800 and 25,200 cells only show a partial -₹4,050 because they sit inside the wings — the fully defined -₹354-point max loss requires a move beyond 22,500 or 25,500.

**Adjustments, variants & timing.** With such a small credit against larger defined risk, discipline is everything: take profit at ~50% and never let a tested side run, because one loss equals more than two wins. If a breakeven (22854 / 25146) comes into play, roll the tested spread out or close it. No naked legs, so this is purely a probability trade taken to the extreme. Deploy it only when far-OTM strikes still carry enough premium to bother — elevated IV — otherwise the razor-thin credit can't justify the defined risk. It suits traders who prize never being tested over collecting much, expecting Nifty to stay in a very wide band with no large directional move pending. Bank Nifty is often the more practical vehicle because its higher premium gives the distant 25000/23000 short strikes enough value to be worthwhile, whereas Nifty's far strikes may pay too little outside high-IV regimes. As with the albatross, stop discipline matters more than on a tight condor, since a rare trend costs well over double the credit.
