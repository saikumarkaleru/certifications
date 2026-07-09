# Strategy Group 6: Ratio Spreads & Backspreads

This family is built on a single structural idea: trade an unequal number of options at two strikes so you hold *more* of one leg than the other. The direction of that imbalance splits the family in two. **Ratio spreads** are net short the extra options — you sell more than you buy, usually collect a credit, finance a cheap directional bet, and live with a dangerous tail because somewhere out there sits a naked short option. **Backspreads** are the mirror image — net long the extra options, paid for with a debit, with a small defined loss in the "dead zone" and an explosive, often unlimited, payoff if the move is violent. Both structures are really volatility-skew trades dressed up as directional ones: you exploit the fact that OTM options on the NSE chain trade at different implied vols, selling the richer skew and buying the cheaper one, and your real edge is being right about *how far and how fast* Nifty moves, not just which way.

## 79. Call Ratio Spread (1x2)
*Mildly bullish, caps out · Short vega · net credit*

**The idea (intuition).** Buy one call to ride a grind higher, and sell two further-out calls to pay for it. You pocket a small credit, profit best if Nifty drifts up to your short strike, and you are quietly short one naked call above that. Think of it as a covered-call's aggressive cousin where the "cover" is a long call instead of stock.

**When & why to use it.** Use when you are mildly bullish and expect Nifty to crawl toward a level but not blow through it — a slow post-results drift, a range that you think resolves gently upward. You want elevated IV (India VIX rich, IV rank > 60) because you are a net seller of the richer OTM skew; the upside calls you sell should be fatter than the one you buy. Do NOT use this ahead of a known explosive catalyst (Budget, RBI, a binary results print) or when Nifty is already pinned near your short strike with weeks to run — that is exactly where the naked tail bites.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 2x 24300 CE @ 292. Net = 456 − 2×292 = −127.9 points, a credit. In rupees: 127.9 × 75 ≈ ₹9,593 received per lot up front.

![Figure: Call Ratio Spread (1x2) payoff at expiry](figs/strategies/call_ratio_1x2.png)

**The numbers (modelled at Nifty 24000).** Max profit 425 points (≈ ₹31,875/lot), earned right at 24300 at expiry. Max loss is Unlimited — above the upside breakeven you are short one naked call into infinity. Breakeven 24728. Net credit 127.9 points (≈ ₹9,593). Risk:reward is undefined because the loss side is open-ended.

**Greeks & behaviour.** Net delta is mildly positive near the money but flips negative as Nifty approaches 24300 (you become net short calls). Theta is your friend — the two short calls decay faster than the one long. Vega is negative (short vega): a quiet, IV-bleeding tape pays you; a vol spike hurts even if price sits still.

**Management & exit.** Take profit if Nifty parks near 24300 and you have captured most of the 425; do not get greedy into expiry-week gamma where a gap through 24300 turns the position vicious. Standard adjustment: if price runs at the short strike, buy back one short call (converting to a vertical) or roll the shorts up and out. Hard rule — never carry the naked tail through a weekend with a catalyst.

**Risk note.** The honest danger is the open upside: a gap to 25000+ produces theoretically unlimited loss, and SPAN margin on the naked short will balloon as IV rises. Size in single lots and treat the upside breakeven as a real stop, not a suggestion.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹9,600 | +₹9,600 | +₹9,600 | +₹9,600 | -₹35,400 |

The table earns its credit across the flat-to-mildly-up grid but turns negative at 25,200, and any move beyond this +5% grid toward and past the naked short loses much more — the upside is unlimited.

**Adjustments, variants & timing.** The cleanest defence is to buy back one of the two short 24300 calls the moment Nifty trades through your long strike with conviction — that converts the position into a plain 24000/24300 bull call spread with no naked tail. If you still want the credit, roll the short pair up and out (to next-week 24500s) to re-centre the tent. A more permanent fix is to add a cheap 24600 wing, turning the 1x2 into a call ratio that is fully defined. The structure works best when you are selling rich upside skew into a high India VIX (IV rank > 60), which is why it suits index trades over single stocks. Prefer Nifty over Bank Nifty here: Bank Nifty's larger daily range and gappier behaviour make the naked upside far more dangerous. Enter 2-3 weeks to expiry so theta does the work, and never carry the naked leg through Budget, RBI or a results gap.

## 80. Put Ratio Spread (1x2)
*Mildly bearish, caps out · Short vega · net credit*

**The idea (intuition).** The bearish mirror of strategy 79. Buy one put, sell two lower puts, collect a credit, and profit most if Nifty eases down to your short strike. You are net short one extra put, so the danger lives on the downside — and on the NSE, downside is where gaps and panic actually happen.

**When & why to use it.** For a mild, controlled drift lower — a market you think leaks toward support but does not crash. You want rich downside put skew (which on Nifty is almost always present, since OTM puts carry a fear premium) and a high IV rank so the two puts you sell are juicy. Avoid it into known risk-off triggers — global selloffs, a hawkish Fed night, expiry-week — because a fast fall toward your short strike is precisely the scenario that hurts.

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 2x 23700 PE @ 219. Net = 318 − 2×219 = −119.3 points credit, i.e. 119.3 × 75 ≈ ₹8,948 received per lot.

![Figure: Put Ratio Spread (1x2) payoff at expiry](figs/strategies/put_ratio_1x2.png)

**The numbers (modelled at Nifty 24000).** Max profit 416 points (≈ ₹31,200/lot) at 23700. Max loss is shown as 23280 points (≈ ₹17.5 lakh/lot), with risk:reward 0.02. That worst case assumes the index collapses all the way to zero; in practice you size small and stop out at a multiple of the credit — but unlike the call version, the put side is mathematically bounded because Nifty cannot fall below zero. Breakeven 23281. Net credit 119.3 points.

**Greeks & behaviour.** Net delta turns increasingly negative below the money as the short puts dominate. Theta positive — time decay works for you while price holds above 23700. Vega negative: an IV pop (the natural companion of a selloff) hurts the position even before price arrives.

**Management & exit.** Book profit when Nifty hovers near 23700 and most of the credit is captured. If price accelerates down through the short strike, buy back one short put to defang the tail, or roll the pair lower. Be out before the last two sessions — downside gamma plus a gap-down is the classic account-killer here.

**Risk note.** A crash gap (a 23700 print becoming a 22500 print overnight) realises a large, fast loss and a margin call as VIX spikes. The "bounded" max loss is still catastrophic relative to the ₹8,948 credit. Trade tiny, define your mental stop, and never confuse "defined" with "small."

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹36,075 | +₹8,925 | +₹8,925 | +₹8,925 | +₹8,925 |

P&L is positive everywhere the index holds at or above the short strike, but a slide to 22,800 already shows a deep loss, and a fall beyond this -5% grid toward the naked short loses far more.

**Adjustments, variants & timing.** Defend by buying back one short 23700 put as soon as Nifty breaks toward it, collapsing the trade into a defined 24000/23700 bear put spread. Alternatively roll the short pair down and out to re-establish room, or bolt on a long 23400 wing to cap the tail into a true ratio with defined risk. The edge is selling the persistent downside put skew on the NSE, which is reliably fat, so high IV rank improves the credit. Favour Nifty: Bank Nifty crashes harder and faster, and the naked put is exactly the leg that a banking-sector shock will detonate. Put it on 2-3 weeks out so decay accrues while the index holds above the short, and be flat before the final two sessions — a gap-down through 23700 in expiry-week gamma is the classic account-killer, made worse by the IV spike that always accompanies an Indian selloff.

## 81. Call Ratio Spread (1x3)
*Mildly bullish · Short vega · net credit*

**The idea (intuition).** Same blueprint as 79 but more aggressive — buy one call, sell *three* higher calls. The extra short funds a bigger credit and a wider profit tent, but you are now net short two naked calls, so the upside tail is twice as steep.

**When & why to use it.** Only for a genuinely capped, mildly bullish view where you are confident Nifty stalls near the short strike. It suits a richly priced upside skew you want to harvest harder. This is a step up in danger and demands more conviction that no breakout is coming — never deploy it into momentum, a trending tape, or any event that can ignite a melt-up.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 3x 24400 CE @ 246. Net = 456 − 3×246 = −281.6 points credit ≈ ₹21,120 received per lot.

![Figure: Call Ratio Spread (1x3) payoff at expiry](figs/strategies/call_ratio_1x3.png)

**The numbers (modelled at Nifty 24000).** Max profit 674 points (≈ ₹50,550/lot) at 24400. Max loss Unlimited — two naked calls run to infinity above breakeven. Breakeven 24741. Net credit 281.6 points (≈ ₹21,120). Risk:reward undefined.

**Greeks & behaviour.** Delta mildly long near spot, flipping sharply negative past 24400 where the three shorts overwhelm the one long. Theta strongly positive (three sellers, one buyer). Vega clearly negative — a rising-IV tape is doubly painful with two extra short calls feeding the loss.

**Management & exit.** Treat the second short call as the thing that will hurt you. Take profits early and often; close into any sign of trend. If tested, buy back one or two shorts to step down to a 1x2 or vertical. Do not hold the double-naked tail through expiry-week gamma under any circumstances.

**Risk note.** Two uncovered calls mean loss accelerates faster than the 1x2, and SPAN margin is heavier and more volatile. A single overnight gap can dwarf the entire credit many times over. This is a professional's harvest trade, not a starter position.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹21,150 | +₹21,150 | +₹21,150 | +₹21,150 | -₹68,850 |

The richer credit prints across the calm grid yet flips to a heavy loss by 25,200, and a push beyond this +5% grid into the two naked calls loses much more — the tail is unlimited.

**Adjustments, variants & timing.** With two naked calls the defence must be earlier and firmer: buy back one short at the first sign of a trend to step down to a 1x2, and a second to reach a defined vertical if momentum builds. Rolling all three shorts up and out re-centres the tent but does not remove the tail — only buying a 24700 wing does that. This is a skew-harvest trade for a richly priced upside in elevated IV (IV rank > 60), best on Nifty where the chain is liquid and gaps are tamer; Bank Nifty's velocity makes a double-naked upside reckless. Time it 2-3 weeks out and take profit early — the marginal points near expiry are not worth the gamma. Absolutely avoid carrying two uncovered calls through any catalyst (Budget, RBI, monthly expiry) where a melt-up can multiply the credit into a multiple-of-margin loss overnight.

## 82. Put Ratio Spread (1x3)
*Mildly bearish · Short vega · net credit*

**The idea (intuition).** The bearish 1x3 — one long put financed by three lower short puts. Bigger credit, wider tent down to the short strike, but you carry two extra naked puts into the most dangerous direction on Indian indices.

**When & why to use it.** For a controlled drift toward a support level with rich downside skew to sell and elevated IV rank. The view must be "slow leak, then stall," not "breakdown." Avoid entirely when macro tail-risk is live — global risk-off, geopolitical flare-ups, a heavy expiry — because a fast flush toward your shorts is the loss scenario, magnified by the third short.

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 3x 23600 PE @ 192. Net = 318 − 3×192 = −258.4 points credit ≈ ₹19,380 received per lot.

![Figure: Put Ratio Spread (1x3) payoff at expiry](figs/strategies/put_ratio_1x3.png)

**The numbers (modelled at Nifty 24000).** Max profit 658 points (≈ ₹49,350/lot) at 23600. Max loss shown as 46540 points (≈ ₹34.9 lakh/lot), risk:reward 0.01. That figure assumes Nifty falls to zero — bounded only by that floor; you must size small and stop at a multiple of the credit long before then. Breakeven 23271. Net credit 258.4 points (≈ ₹19,380).

**Greeks & behaviour.** Delta swings strongly negative below 23600 as three short puts dominate. Theta positive while price holds up. Vega negative — and recall that falling markets bring rising IV, so price and vega losses compound here.

**Management & exit.** Defend aggressively: if Nifty heads for 23600, buy back one or two short puts to revert to a 1x2 or a defined vertical. Book the bulk of the credit early; never ride the double-naked structure into the final sessions where a gap-down is unmanageable.

**Risk note.** This carries the steepest realistic downside in the ratio-spread set. A crash plus IV spike produces a large, fast, margin-calling loss against a modest credit. The "bounded" loss is still life-altering at scale — keep size minimal.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹70,650 | +₹19,350 | +₹19,350 | +₹19,350 | +₹19,350 |

The structure collects across the upper grid but shows a large loss at 22,800, and any extension beyond this -5% grid toward the two naked puts loses far more.

**Adjustments, variants & timing.** Two naked puts demand aggressive, staged defence: buy back one short 23600 put to revert to a 1x2, then a second to reach a defined spread if the flush continues. Rolling the trio down and out buys room but keeps the tail live; only a long 23300 wing defines it. The thesis is selling expensive downside skew in a high IV-rank tape, which the NSE offers persistently. Strongly prefer Nifty over Bank Nifty — banking names lead every risk-off cascade, and a double-naked put into a Bank Nifty flush is how accounts blow up. Enter 2-3 weeks out to bank decay while the index holds, and exit well before expiry week. Remember the compounding trap unique to the downside: a falling market simultaneously moves price against you and spikes India VIX, so your short vega and short delta lose together — size in single lots only.

## 83. Call Ratio Backspread (1x2)
*Bullish explosive · Long vega · net debit*

**The idea (intuition).** Flip the call ratio spread upside down: sell one lower call and buy two higher calls. Now you are net *long* an extra call. Your loss is small and defined in the middle, and if Nifty rips higher your two long calls run away to the upside. It is a cheap lottery ticket on a breakout, partly funded by the call you sold.

**When & why to use it.** Use when you expect a sharp, fast rally and want explosive convex upside with defined risk — a breakout setup, a results gap, a momentum thrust. Backspreads love *rising* IV, so they shine when you buy them in a low-IV lull (IV rank < 30) right before an expected vol expansion. The enemy is a slow grind that stalls in the dead zone between strikes and a quiet, IV-bleeding tape that decays your longs. Do not put this on when you only expect a mild drift — that is the ratio spread's job, not the backspread's.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 2x 24300 CE @ 292. Net = −456 + 2×292 = +127.9 points debit ≈ ₹9,593 paid per lot.

![Figure: Call Ratio Backspread (1x2) payoff at expiry](figs/strategies/call_backspread_1x2.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited — two long calls into a runaway rally. Max loss 425 points (≈ ₹31,875/lot), the most you can lose, realised right at 24300 where the short is ITM and the longs expire worthless. Breakeven 24728. Net debit 127.9 points (≈ ₹9,593). Risk:reward undefined (unlimited upside).

**Greeks & behaviour.** Net delta is long and *gets longer* as Nifty rallies (positive gamma working for you). Theta is negative — every quiet day costs you. Vega is positive: an IV expansion lifts your two longs and is a core part of the thesis.

**Management & exit.** This is a move-or-die trade. Give it a defined window (often expiry week into a catalyst) and exit if the move does not come — do not let theta grind the debit to zero. Once Nifty clears 24728 and the position is convex, scale out into strength or trail a stop to lock the open-ended gains.

**Risk note.** The real risk is time and silence: a flat market simply bleeds you to the 425-point max loss. The worst single point is sitting pinned at 24300 into expiry. Defined risk, yes — but you can lose all of it if the breakout never arrives.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹9,600 | -₹9,600 | -₹9,600 | -₹9,600 | +₹35,400 |

As a backspread the picture inverts: the small defined loss sits across the quiet grid and only at 25,200 does the position turn profitable — beyond this +5% grid the upside runs unlimited.

**Adjustments, variants & timing.** This is a move-or-die debit trade, so the main defence is time discipline: window it to a known catalyst and cut it if the breakout does not arrive rather than feed theta. If Nifty stalls in the dead zone you can sell a higher call (e.g. 24600) against the longs to recoup some debit, turning it into a defined butterfly-like structure. Once the move comes and the position is convex past 24728, scale out into strength and trail a stop to protect the open-ended leg. Backspreads want to be bought cheap in a low-IV lull (IV rank < 30) just before an expected vol expansion — that is the whole edge. Bank Nifty actually suits this better than Nifty: its larger, faster directional thrusts give the long calls more room to run, and its richer premiums reward a genuine breakout. Avoid quiet, rangebound regimes where decay simply bleeds the debit to the full max loss.

## 84. Put Ratio Backspread (1x2)
*Bearish explosive · Long vega · net debit*

**The idea (intuition).** The bearish backspread: sell one higher put, buy two lower puts. Net long an extra put, so a crash pays explosively while your loss in the middle is capped. This is the structure to own when you fear a flush, because downside moves on the NSE come with a vol spike that supercharges your long vega.

**When & why to use it.** Deploy when you expect a fast, deep selloff — a breakdown through support, a global risk-off night, a feared event. Best entered in a calm, low-IV tape so you buy your puts cheap before fear repriced them. The trap is a slow drift that dies in the dead zone, and a placid market that decays the longs. Not for a mild bearish lean — use a put ratio spread for that.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 2x 23700 PE @ 219. Net = −318 + 2×219 = +119.3 points debit ≈ ₹8,948 paid per lot.

![Figure: Put Ratio Backspread (1x2) payoff at expiry](figs/strategies/put_backspread_1x2.png)

**The numbers (modelled at Nifty 24000).** Max profit 23280 points (≈ ₹17.5 lakh/lot if Nifty went to zero — practically, a very large gain on any real crash). Max loss 416 points (≈ ₹31,200/lot), realised at 23700. Breakeven 23281. Net debit 119.3 points (≈ ₹8,948). Risk:reward a striking 55.98 — small defined risk against an enormous skewed payoff.

**Greeks & behaviour.** Net delta short and getting shorter as Nifty falls (positive gamma in your favour). Theta negative — patience costs money. Vega strongly positive, and because crashes spike India VIX, the vega tailwind here is real and large.

**Management & exit.** A conviction-and-timing trade: define a window, and if the breakdown does not materialise, cut it rather than feed theta. On a flush below 23281, the position goes convex fast — take partial profits into the panic and trail the rest, because mean-reversion bounces can give the gains back quickly.

**Risk note.** The danger is opportunity cost and decay: in a calm market you lose the full 416 points. The eye-catching 55.98 reward:risk only pays if a genuine, fast move occurs — most days, nothing happens and theta nibbles. Defined loss, but it is a real loss.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹36,075 | -₹8,925 | -₹8,925 | -₹8,925 | -₹8,925 |

The defined loss occupies the calm middle of the grid and only the 22,800 flush pays — a move beyond this -5% grid toward zero pays far more, the convex reward this trade is built for.

**Adjustments, variants & timing.** Treat it as a timed convexity bet: define a window around a feared event and cut it if the flush does not come, rather than let theta erode the debit. If the index drifts but does not break, sell a lower put (e.g. 23400) against your longs to defray cost into a defined structure. On a break below 23281 the position turns sharply convex — bank partial profits into the panic and trail the rest, because Indian selloffs mean-revert violently and bounces give gains back fast. The setup wants cheap puts bought in a calm, low-IV tape before fear reprices them; the crash-driven India VIX spike is the core profit lever via long vega. Bank Nifty is the better vehicle for a true flush — it leads every risk-off move with bigger, faster drops and a sharper vol pop — while Nifty offers a steadier, slightly less explosive version. Not for a mild bearish lean.

## 85. Call Ratio Backspread (1x3)
*Strongly bullish · Long vega · net debit*

**The idea (intuition).** A more leveraged bullish backspread — sell one call, buy three higher calls. Net long two extra calls, so the upside convexity is steeper, paid for with a larger debit and a wider, deeper dead zone you must clear.

**When & why to use it.** For a strong, fast melt-up conviction where you want maximum convex upside with defined risk. Buy it cheap in a low-IV regime expecting vol expansion on the breakout. The cost: a bigger debit and more theta to overcome, so the move needs to be both large and reasonably prompt. Never for a mild or slow view — the dead zone will eat you.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 3x 24400 CE @ 246. Net = −456 + 3×246 = +281.6 points debit ≈ ₹21,120 paid per lot.

![Figure: Call Ratio Backspread (1x3) payoff at expiry](figs/strategies/call_backspread_1x3.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (three long calls in a runaway rally). Max loss 674 points (≈ ₹50,550/lot) at 24400. Breakeven 24741. Net debit 281.6 points (≈ ₹21,120). Risk:reward undefined (open upside).

**Greeks & behaviour.** Net delta long and accelerating with price — strong positive gamma. Theta negative and heavier than the 1x2 because three longs decay. Vega strongly positive; an IV expansion is a major driver of profit before price even arrives.

**Management & exit.** Tight time discipline matters more here — three decaying longs make the bleed faster. Tie it to a specific catalyst window. Beyond 24741 the payoff is convex; scale out into strength and trail the remainder to capture the unlimited leg.

**Risk note.** The full 674-point debit is at risk if Nifty stalls near 24400 — the worst spot to be pinned. Larger debit means a larger defined loss than the 1x2, and theta bites harder. Only trade it when you genuinely expect a big, fast move.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹21,150 | -₹21,150 | -₹21,150 | -₹21,150 | +₹68,850 |

The deeper defined loss spans the grid and only a 25,200 breakout turns it green, with profit beyond this +5% grid running unlimited as the three long calls take over.

**Adjustments, variants & timing.** Three decaying longs make time discipline paramount — tie it to a specific catalyst and cut it promptly if the melt-up stalls. In a dead-zone drift, sell a higher call (around 24700) against the longs to recover some of the heavier debit, defining the structure. Beyond 24741 the payoff is convex; scale out into strength and trail to capture the unlimited leg. The trade is bought cheap in a low-IV regime (IV rank < 30) expecting vol expansion on the breakout, so entry timing into a coiled range is everything. Bank Nifty suits the leveraged version well: its powerful, fast thrusts let three long calls run hard, and its fatter premiums reward conviction — though the larger debit also bites harder if you are wrong. On Nifty the move tends to be smoother and may not fully clear the wider dead zone. Only deploy when you genuinely expect a large, prompt move.

## 86. Put Ratio Backspread (1x3)
*Strongly bearish · Long vega · net debit*

**The idea (intuition).** The leveraged bearish backspread — sell one put, buy three lower puts. Net long two extra puts for steep downside convexity, ideal when you expect not just a fall but a genuine flush with a VIX spike.

**When & why to use it.** For high-conviction crash views — a decisive breakdown, a feared macro event, a fragile market on the edge. Enter in calm IV so the three long puts are cheap before fear reprices them. The drawback is the larger debit and a wider dead zone; the move must be deep and reasonably quick. Not for mild bearishness.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 3x 23600 PE @ 192. Net = −318 + 3×192 = +258.4 points debit ≈ ₹19,380 paid per lot.

![Figure: Put Ratio Backspread (1x3) payoff at expiry](figs/strategies/put_backspread_1x3.png)

**The numbers (modelled at Nifty 24000).** Max profit 46540 points (≈ ₹34.9 lakh/lot at the zero bound — in practice a very large gain on a real crash). Max loss 658 points (≈ ₹49,350/lot) at 23600. Breakeven 23271. Net debit 258.4 points (≈ ₹19,380). Risk:reward 70.74 — the most convex payoff in this chapter.

**Greeks & behaviour.** Net delta short, steepening as Nifty drops (powerful positive gamma). Theta negative and heavier than the 1x2. Vega strongly positive — the crash-plus-VIX dynamic is the whole point and the biggest profit lever.

**Management & exit.** Window it to a catalyst; cut it if the flush does not come rather than bleed three longs. On a break below 23271 it turns sharply convex — bank partial profits into the panic and trail the rest, since violent bounces can erase open gains fast.

**Risk note.** In a quiet or grinding tape you lose the full 658-point debit — larger than the 1x2's. The headline 70.74 reward:risk only materialises on a real, fast collapse. Treat the debit as fully at risk.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹70,650 | -₹19,350 | -₹19,350 | -₹19,350 | -₹19,350 |

The defined debit is lost across the quiet grid and only a 22,800 crash pays — beyond this -5% grid the three long puts deliver a far larger, convex gain.

**Adjustments, variants & timing.** With three long puts the bleed is faster, so window it tightly to a catalyst and cut if the breakdown does not come. If the index merely softens, sell a lower put (around 23300) against the longs to claw back some debit into a defined structure. Below 23271 it goes sharply convex — take partial profits into the panic and trail the rest, since violent relief bounces erase open gains quickly. Enter in calm, low-IV conditions so the three puts are cheap before fear reprices them; the crash-plus-India-VIX dynamic is the entire thesis and the biggest profit lever. Bank Nifty is the natural home for a leveraged crash bet — it leads and amplifies every risk-off cascade with the deepest, fastest drops and the sharpest vol spike — whereas Nifty gives a calmer, less explosive payoff. Reserve this for high-conviction flush views, never a mild bearish drift, and treat the full debit as at risk.

## 87. Call Ratio Spread (For Credit)
*Neutral to mildly bullish · Short vega · net credit*

**The idea (intuition).** A call ratio spread placed entirely above the money so it is built purely for the credit and a neutral-to-mildly-bullish lean. Buy one OTM call, sell two further-OTM calls, collect cash, and profit if Nifty drifts gently up to the short strike or simply goes nowhere.

**When & why to use it.** When you think Nifty stays rangebound with a slight upward tilt and you want to monetise rich upside skew and elevated IV. The OTM placement keeps both strikes out of the money, so a flat-to-slightly-up tape lets the whole thing decay in your favour. Avoid it before any catalyst that can spark a breakout through the short strike, where the naked call awakens.

**How to build it (₹, Nifty).** Buy 24200 CE @ 342, sell 2x 24450 CE @ 224. Net = 342 − 2×224 = −106.6 points credit ≈ ₹7,995 received per lot.

![Figure: Call Ratio Spread (For Credit) payoff at expiry](figs/strategies/call_ratio_credit.png)

**The numbers (modelled at Nifty 24000).** Max profit 347 points (≈ ₹26,025/lot) at 24450. Max loss Unlimited above breakeven (one naked call). Breakeven 24807. Net credit 106.6 points (≈ ₹7,995). Risk:reward undefined.

**Greeks & behaviour.** Net delta near flat at inception (both legs OTM), turning negative as price approaches 24450. Theta positive — the structure earns its keep through decay. Vega negative; a vol spike that lifts the upside calls hurts.

**Management & exit.** Because the edge is the credit, take it off once you have captured roughly half and the position has decayed — do not chase the last few points into expiry-week gamma. If Nifty rallies toward 24450, buy back a short to cap the tail or roll up and out.

**Risk note.** Genuinely unlimited upside loss if Nifty breaks out and trends — the naked call and rising SPAN margin punish complacency. Premium selling is not free money; size small and respect the breakeven as a stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹8,025 | +₹8,025 | +₹8,025 | +₹15,525 | -₹29,475 |

The credit decays in your favour across the flat grid, steps up near the short strike, then collapses to a loss by 25,200 — a breakout beyond this +5% grid into the naked call loses much more, unlimited.

**Adjustments, variants & timing.** Because both legs start OTM, the defence is straightforward: if Nifty rallies toward 24450, buy back one short 24450 call to cap the tail into a defined 24200/24450 spread, or roll the shorts up and out to keep the credit alive. Adding a 24700 wing converts it to a fully defined ratio for those who cannot hold a naked leg. The edge is monetising rich upside skew in a high IV-rank, rangebound tape, so it is an index trade — prefer Nifty, whose flatter, more orderly behaviour suits a sit-and-decay structure better than Bank Nifty's whippy range. Put it on 2-3 weeks out so the OTM strikes decay in your favour, and take profit once roughly half the credit is captured rather than chasing the last points into expiry-week gamma. Avoid placing it ahead of any catalyst that can spark a breakout through the short strike and wake the naked call.

## 88. Put Ratio Spread (For Credit)
*Neutral to mildly bearish · Short vega · net credit*

**The idea (intuition).** The bearish, all-OTM credit version. Buy one OTM put, sell two lower puts, collect the credit, and profit if Nifty drifts gently down to the short strike or stays flat.

**When & why to use it.** For a rangebound-to-slightly-soft view where you want to harvest the persistent downside put skew and a high IV rank. Both strikes sit below the money, so a calm or mildly weak tape decays nicely. Steer clear when risk-off is brewing — a fast drop toward your shorts is the loss case.

**How to build it (₹, Nifty).** Buy 23800 PE @ 248, sell 2x 23550 PE @ 180. Net = 248 − 2×180 = −111.7 points credit ≈ ₹8,378 received per lot.

![Figure: Put Ratio Spread (For Credit) payoff at expiry](figs/strategies/put_ratio_credit.png)

**The numbers (modelled at Nifty 24000).** Max profit 359 points (≈ ₹26,925/lot) at 23550. Max loss shown as 23187 points (≈ ₹17.4 lakh/lot), risk:reward 0.02. That assumes the index falls to zero — bounded by that floor but catastrophic; size small and stop at a multiple of the credit. Breakeven 23188. Net credit 111.7 points (≈ ₹8,378).

**Greeks & behaviour.** Net delta near flat at entry, turning negative as price nears 23550. Theta positive. Vega negative — and a falling market's IV pop works against you on both price and vol.

**Management & exit.** Book around half the credit and exit before expiry-week downside gamma. If Nifty slides toward 23550, buy back a short put to revert to a defined vertical, or roll lower.

**Risk note.** A crash gap realises a large, fast loss and a margin spike against a modest ₹8,378 credit. "Bounded" is not "safe" — most retail F&O sellers lose money per SEBI data, so keep size minimal and stops honest.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹29,100 | +₹15,900 | +₹8,400 | +₹8,400 | +₹8,400 |

P&L is positive while the index drifts gently down toward the short strike but turns sharply negative at 22,800, and a fall beyond this -5% grid into the naked put loses far more.

**Adjustments, variants & timing.** Defend by buying back one short 23550 put if Nifty slides toward it, reverting to a defined 23800/23550 bear put spread, or roll the shorts down and out to re-open room. A long 23300 wing defines the tail outright. The trade harvests the NSE's persistent downside put skew in a high IV-rank, rangebound-to-soft tape, so favour Nifty over the gappier Bank Nifty, where a banking shock detonates exactly the naked put you are short. Enter 2-3 weeks to expiry so the OTM strikes bleed in your favour while the index holds above the short, and book around half the credit before expiry-week downside gamma. Keep the size minimal: a fast flush moves price against you and spikes India VIX simultaneously, so your short delta and short vega lose together, and SEBI data shows most retail F&O sellers lose money precisely by underestimating this tail.

## 89. Front-Ratio Call Spread
*Slow grind up · Short vega · net credit*

**The idea (intuition).** A front-ratio call spread buys one nearer call and sells two further calls, structured so the long leg sits in front (closer to the money). You collect a credit, profit best on a slow grind up into the short strike, and carry one naked call above. It is the "I think we drift higher but not much" expression.

**When & why to use it.** For a gentle, grinding uptrend with no breakout expected — the kind of low-energy bull tape that creeps higher day by day. Rich upside skew and decent IV make the two shorts worth selling. Do not use it when momentum or a catalyst could turn the grind into a thrust through your short strike.

**How to build it (₹, Nifty).** Buy 23900 CE @ 519, sell 2x 24250 CE @ 317. Net = 519 − 2×317 = −114.6 points credit ≈ ₹8,595 received per lot.

![Figure: Front-Ratio Call Spread payoff at expiry](figs/strategies/front_ratio_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 463 points (≈ ₹34,725/lot) at 24250. Max loss Unlimited above breakeven. Breakeven 24715. Net credit 114.6 points (≈ ₹8,595). Risk:reward undefined.

**Greeks & behaviour.** Net delta slightly long near spot (the long call is closer to the money), flipping negative past 24250. Theta positive. Vega negative — a quiet, decaying tape is ideal; an IV jump hurts.

**Management & exit.** Capture most of the 463 as Nifty approaches 24250, then take it off ahead of expiry gamma. If the grind accelerates, buy back one short to neutralise the tail or roll the shorts up.

**Risk note.** The single naked call means a true melt-up produces unlimited loss with escalating margin. A slow grind is friendly; a breakout is not. Treat 24715 as a real stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹8,625 | +₹8,625 | +₹16,125 | +₹8,625 | -₹36,375 |

The credit grinds up to its best near the short strike then reverses to a loss by 25,200, and any thrust beyond this +5% grid into the naked call loses much more — unlimited.

**Adjustments, variants & timing.** The front-ratio's single naked call is defused by buying back one short 24250 call when the grind accelerates, leaving a defined 23900/24250 spread, or by rolling the short pair up and out to chase the drift. A 24600 wing makes it a fully defined structure. The trade sells rich upside skew into a slow, low-energy bull tape with decent IV, so it suits Nifty's orderly grind better than Bank Nifty's lurchy momentum, where a thrust through the short strike is more likely. Enter 2-3 weeks out so theta compounds on the OTM shorts, and capture most of the 463-point tent as price approaches 24250 rather than holding into expiry gamma. The key timing rule: this expression dies if the grind becomes a breakout, so step out the instant momentum or a catalyst threatens to turn the creep into a thrust through 24715.

## 90. Front-Ratio Put Spread
*Slow grind down · Short vega · net credit*

**The idea (intuition).** The bearish front-ratio: buy one nearer put, sell two lower puts, take a credit, and profit on a slow leak down into the short strike. One naked put rides below as the source of tail risk.

**When & why to use it.** For a low-energy downward drift — a tired market leaking toward support without panic. Sell into rich downside skew and a high IV rank. Avoid it whenever a fast risk-off move is plausible, because acceleration toward your shorts is the loss scenario.

**How to build it (₹, Nifty).** Buy 24100 PE @ 359, sell 2x 23750 PE @ 233. Net = 359 − 2×233 = −107.5 points credit ≈ ₹8,063 received per lot.

![Figure: Front-Ratio Put Spread payoff at expiry](figs/strategies/front_ratio_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 452 points (≈ ₹33,900/lot) at 23750. Max loss shown as 23291 points (≈ ₹17.5 lakh/lot), risk:reward 0.02 — the figure assumes Nifty falls to zero, bounded by that floor; size small and stop at a multiple of the credit. Breakeven 23292. Net credit 107.5 points (≈ ₹8,063).

**Greeks & behaviour.** Net delta slightly short near spot, more negative as price nears 23750. Theta positive. Vega negative — a downside vol spike works against the position.

**Management & exit.** Book around half the credit, exit before expiry-week downside gamma. If Nifty leaks faster than expected, buy back a short put to cap the tail or roll lower.

**Risk note.** A crash gap turns the bounded-but-huge loss real and fast, with a margin spike, against an ₹8,063 credit. Keep size tiny and stops disciplined — selling premium is not free money.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹36,900 | +₹8,100 | +₹15,600 | +₹8,100 | +₹8,100 |

P&L peaks on a slow leak toward the short strike but a 22,800 print already shows a heavy loss, and acceleration beyond this -5% grid into the naked put loses far more.

**Adjustments, variants & timing.** Defend the lone naked put by buying back one short 23750 put as Nifty leaks toward it, leaving a defined 24100/23750 bear put spread, or roll the shorts down and out to re-open room; a 23400 wing defines the tail. The structure sells the NSE's reliably rich downside skew into a tired, low-energy drift with a high IV rank, so prefer Nifty — Bank Nifty's faster, deeper drops are exactly what turn a slow leak into the loss scenario. Enter 2-3 weeks out so the OTM shorts decay while the index holds above 23750, and book around half the credit before expiry-week downside gamma. Stay alert to the asymmetry of Indian downside: a drift can flip to a flush in one session, and the accompanying India VIX spike compounds the short-vega loss, so keep the size tiny and treat 23292 as a hard mental stop.

## 91. Call Backspread (OTM)
*Bullish breakout · Long vega · net debit*

**The idea (intuition).** An out-of-the-money call backspread: sell one OTM call, buy two further-OTM calls. Cheaper than an at-the-money backspread because everything is OTM, with a small defined loss and explosive upside if Nifty breaks out hard.

**When & why to use it.** For an anticipated upside breakout where you want convex, defined-risk leverage at low cost — a coiled range you expect to resolve up, ahead of a bullish catalyst. The OTM placement and low-IV entry keep the debit small; you are betting on both a big move and IV expansion. Useless for a mild drift that stalls below the long strikes.

**How to build it (₹, Nifty).** Sell 24200 CE @ 342, buy 2x 24500 CE @ 204. Net = −342 + 2×204 = +66.2 points debit ≈ ₹4,965 paid per lot.

![Figure: Call Backspread (OTM) payoff at expiry](figs/strategies/call_backspread_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (two long calls in a runaway move). Max loss 355 points (≈ ₹26,625/lot) at 24500. Breakeven 24866. Net debit 66.2 points (≈ ₹4,965). Risk:reward undefined (open upside).

**Greeks & behaviour.** Net delta long and accelerating with a rally; positive gamma. Theta negative — quiet days cost you. Vega positive — an IV expansion is a key profit driver, and the cheap OTM longs are very vega-sensitive.

**Management & exit.** A defined-window breakout bet — cut it if the move and vol pop do not arrive rather than feed theta. Above 24866 it goes convex; scale out into strength and trail the rest.

**Risk note.** The full 355-point debit is lost if Nifty stalls at 24500 into expiry, the worst pin point. Cheap, defined risk — but a complete loss is the base-rate outcome when no breakout comes.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹4,950 | -₹4,950 | -₹4,950 | -₹19,950 | +₹25,050 |

The small defined debit is lost across the quiet grid and only a 25,200 breakout pays — beyond this +5% grid the two long calls run the profit up without limit.

**Adjustments, variants & timing.** As a cheap defined-risk debit, the primary lever is timing: window it to a bullish catalyst and cut it if the breakout and vol pop do not arrive rather than feeding theta. If Nifty drifts but stays below the long strikes, sell a higher 24700 call against them to recover part of the small debit. Above 24866 the position goes convex — scale out into strength and trail the rest to capture the open-ended upside. The OTM placement plus a low-IV entry (IV rank < 30) keeps the cost tiny and the vega leverage high, since cheap OTM calls are exquisitely vol-sensitive. Bank Nifty suits this better than Nifty: its larger, faster breakouts give the long calls room to run and its richer premiums reward a genuine thrust. The base-rate outcome is a full loss of the modest debit when no breakout comes, so only deploy it when you expect a big, prompt move.

## 92. Put Backspread (OTM)
*Bearish breakdown · Long vega · net debit*

**The idea (intuition).** The OTM bearish backspread: sell one OTM put, buy two lower puts. Low-cost, defined-risk convexity that pays explosively on a breakdown-and-flush.

**When & why to use it.** For an expected downside breakout — a range about to crack lower, a fragile tape into a risk-off catalyst. Enter in calm IV so the long puts are cheap before fear reprices them; the crash-driven VIX spike is a core part of the payoff. Not for a mild bearish lean that dies in the dead zone.

**How to build it (₹, Nifty).** Sell 23800 PE @ 248, buy 2x 23500 PE @ 169. Net = −248 + 2×169 = +88.7 points debit ≈ ₹6,653 paid per lot.

![Figure: Put Backspread (OTM) payoff at expiry](figs/strategies/put_backspread_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit 23110 points (≈ ₹17.3 lakh/lot at the zero bound — a very large gain on a real crash). Max loss 384 points (≈ ₹28,800/lot) at 23500. Breakeven 23111. Net debit 88.7 points (≈ ₹6,653). Risk:reward 60.15.

**Greeks & behaviour.** Net delta short, steepening as Nifty falls; positive gamma. Theta negative. Vega strongly positive — the downside vol spike supercharges the long puts.

**Management & exit.** Window it to a catalyst and cut if the flush does not come. Below 23111 it turns convex — bank partial profits into the panic and trail the rest, since sharp bounces can give gains back.

**Risk note.** In a calm or grinding market you lose the full 384-point debit. The 60.15 reward:risk only pays on a genuine, fast collapse — defined, but a real loss most of the time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹23,325 | -₹21,675 | -₹6,675 | -₹6,675 | -₹6,675 |

The defined loss sits across the calm grid and only a 22,800 breakdown pays, with the gain beyond this -5% grid growing far larger as the two long puts dominate.

**Adjustments, variants & timing.** Treat it as a timed, cheap convexity bet: define a window around a risk-off catalyst and cut it if the breakdown stalls. If the index softens without breaking, sell a lower 23300 put against the longs to defray the debit into a defined structure. Below 23111 it turns convex — bank partial profits into the panic and trail the rest, since Indian selloffs snap back hard. Enter in calm, low-IV conditions so the OTM long puts are cheap before fear reprices them; the crash-driven India VIX spike supercharges the position through long vega and is central to the payoff. Bank Nifty is the stronger vehicle for a downside break — it leads every risk-off cascade with the deepest, fastest drops and the sharpest vol pop — while Nifty gives a steadier, less explosive version. Not for a mild bearish lean that dies in the dead zone; expect to lose the full debit when no flush comes.

## 93. Call Ratio Spread (2x3)
*Mildly bullish · Short vega · net debit*

**The idea (intuition).** A balanced ratio: buy two lower calls, sell three higher calls. Closer to a ratioed vertical, it carries a defined-profit tent with a single net-naked call up top. Unusually for this set it is a small *debit*, and it has two breakevens — a profit window rather than a one-sided tent.

**When & why to use it.** For a mild bullish view targeting a specific zone, where the 2x3 structure gives a wider, more symmetric profit band than a 1x2. Suits rich upside skew you want to partly sell while keeping defined risk over most of the range. Avoid it ahead of a breakout that can punch through the upper breakeven into the naked call.

**How to build it (₹, Nifty).** Buy 2x 24000 CE @ 456, sell 3x 24300 CE @ 292. Net = 2×456 − 3×292 = +36.2 points debit ≈ ₹2,715 paid per lot.

![Figure: Call Ratio Spread (2x3) payoff at expiry](figs/strategies/call_ratio_2x3.png)

**The numbers (modelled at Nifty 24000).** Max profit 557 points (≈ ₹41,775/lot) at 24300. Max loss Unlimited above the upper breakeven (one net-naked call). Breakevens 24018 and 24864 — a defined profit window between them. Net debit 36.2 points (≈ ₹2,715). Risk:reward undefined.

**Greeks & behaviour.** Net delta long near the lower breakeven, turning negative past 24300 as the three shorts dominate. Theta positive once price is parked near 24300. Vega negative — an IV spike hurts, especially near the upper breakeven.

**Management & exit.** Aim to have Nifty settle near 24300 to capture the 557. Take profits before expiry-week gamma; if price pushes past 24864, buy back the net-naked short to cap the tail or roll up.

**Risk note.** Despite two breakevens and a small debit, the upside loss is genuinely unlimited beyond 24864 — one net-naked call into a trend. Margin scales with IV; respect the upper breakeven as a hard stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹2,700 | -₹2,700 | -₹2,700 | +₹19,800 | -₹25,200 |

The small debit shows a modest loss across most of the grid, a strong gain near the short strike, then a loss again by 25,200 — beyond this +5% grid the net-naked call loses much more, unlimited.

**Adjustments, variants & timing.** Despite the small debit and two breakevens, one net-naked call lives above 24864, so defend by buying it back if price pushes past the upper breakeven, leaving a defined 2x2 vertical, or roll the short trio up and out to re-centre the wider profit band. A 24600 wing defines the structure entirely. The 2x3 sells rich upside skew while keeping defined risk over most of the range, suiting a mild bullish view that targets a specific zone — prefer Nifty, whose orderly behaviour lets price settle near 24300, over Bank Nifty's range that can blow through the upper breakeven into the naked call. Enter 2-3 weeks out so theta works once price parks near the short strike, and take the 557-point peak before expiry-week gamma. Margin scales with India VIX, so a rising-IV tape both hurts the vega and inflates the SPAN requirement on the net-naked leg.

## 94. Put Ratio Spread (2x3)
*Mildly bearish · Short vega · net credit*

**The idea (intuition).** The bearish balanced ratio: buy two higher puts, sell three lower puts, for a small credit. A defined-profit band centred near the short strike, with one net-naked put carrying the downside tail.

**When & why to use it.** For a mild bearish view aimed at a specific support zone, where the 2x3 gives a broader profit band than a 1x2 plus a small credit. Sell into rich downside skew and elevated IV. Do not deploy when a fast flush is plausible — acceleration through the lower breakeven into the naked put is the loss case.

**How to build it (₹, Nifty).** Buy 2x 24000 PE @ 318, sell 3x 23700 PE @ 219. Net = 2×318 − 3×219 = −19.8 points credit ≈ ₹1,485 received per lot.

![Figure: Put Ratio Spread (2x3) payoff at expiry](figs/strategies/put_ratio_2x3.png)

**The numbers (modelled at Nifty 24000).** Max profit 616 points (≈ ₹46,200/lot) at 23700. Max loss shown as 23079 points (≈ ₹17.3 lakh/lot), risk:reward 0.03 — the figure assumes Nifty falls to zero, bounded by that floor; size small and stop at a multiple of the credit. Breakeven 23080. Net credit 19.8 points (≈ ₹1,485).

**Greeks & behaviour.** Net delta turns negative below 23700 as the three shorts dominate. Theta positive while price holds. Vega negative — a downside vol spike works against you on both price and vol.

**Management & exit.** Target a settle near 23700 to capture the 616, and exit before expiry-week downside gamma. If Nifty breaks the lower breakeven, buy back the net-naked short put to revert to a defined structure or roll lower.

**Risk note.** The small ₹1,485 credit belies a large, fast potential loss if Nifty crashes through 23080 — the net-naked put plus a VIX spike. Bounded by zero but catastrophic at scale; keep size minimal and stops honest, because premium selling is never free money.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹21,000 | +₹24,000 | +₹1,500 | +₹1,500 | +₹1,500 |

The thin credit sits near flat across most of the grid, prints its best near the short strike, and a 22,800 crash shows a large loss — beyond this -5% grid the net-naked put loses far more.

**Adjustments, variants & timing.** The thin credit hides one net-naked put below 23080, so defend by buying it back if Nifty breaks the lower breakeven, reverting to a defined 2x2 bear put spread, or roll the short trio down and out to re-centre the band; a 23400 wing defines the tail. The structure sells the NSE's rich downside skew while keeping defined risk over most of the range, suiting a mild bearish view aimed at a specific support zone. Favour Nifty over Bank Nifty: banking names lead every flush and are far likelier to crash through the lower breakeven into the naked put. Enter 2-3 weeks out so decay accrues while the index holds near 23700, and bank the 616-point peak before expiry-week downside gamma. Mind the compounding India-specific trap — a crash drives price and India VIX against you together — so keep the size minimal and treat 23080 as a hard stop.
