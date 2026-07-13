# Strategy Group 8: Covered & Income Strategies

This family is built on one idea: you already hold (or short) the underlying, and you sell options against it to harvest premium and theta. The trade-off is always the same — you collect a small, high-probability credit in exchange for capping your upside and keeping most of your downside. A crucial NSE nuance runs through the whole chapter: Indian index options are European and cash-settled, so there is no early assignment and no real "shares" to deliver. A genuine covered call on Nifty therefore means holding a Nifty ETF, a basket, or **long a Nifty future** against the short call — not literally owning the index. Treat every "long underlying @ 24000" leg below as that future/ETF proxy, and remember the SEBI reality that most retail F&O traders lose money: premium selling is income with a tail, not free money.

## 113. Covered Call (OTM)

*Neutral to mildly bullish · Short vega · net debit*

**The idea (intuition).** You own the index and rent out the upside above 24300 for a monthly cheque. Like a landlord collecting rent on a flat you still live in — the rent is yours to keep, but if a buyer offers above your agreed price, you have to sell.

**When & why to use it.** Use it when you are long-term constructive on Nifty but expect a quiet-to-grinding month, and IV is rich enough that the OTM call pays a meaningful credit (India VIX elevated, IV rank above 50 helps). It is the workhorse of index income. Avoid it just before a strong directional catalyst (Budget, big earnings season, election results) where you would resent capping the upside, and avoid it in a clear downtrend — the small call premium barely dents a falling index.

**How to build it (₹, Nifty).** Long 1x Nifty (future/ETF) @ 24000, sell the 24300 CE @ 292. The option premium collected is 292 points = ₹21,900 per lot of 75. The position is a net debit of 23708.1 points because the index outlay dominates; the call simply lowers your effective cost.

![Figure: Covered Call (OTM) payoff at expiry](figs/strategies/covered_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 592 points (₹44,400) if Nifty finishes at or above 24300. Max loss -23707 points if the index fell all the way to zero. Breakeven 23708. Net debit 23708.1 points. Risk:reward 0.02. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is positive but below 1 (long index minus the short call's delta), so you stay bullish-lite. Theta is positive — time decay on the short call works for you. Vega is negative; falling IV after entry helps the short call.

**Management & exit.** A clean rule is to buy back the call at roughly 50% of the credit (around 145 points), then either re-sell next month or let the index run. If Nifty rips through 24300, roll the call up-and-out to keep some upside. Take the trade off before expiry-week gamma whipsaws the short strike.

**Risk note.** Your real danger is downside in the index, not the capped call — a gap-down erases far more than the 292-point cushion. Cash settlement removes assignment worry, but STT and slippage on rolling the call still nibble returns.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -68,100 | -23,100 | +21,900 | +44,400 | +44,400 |

Reading across, the +21,900 at 24,000 and the +44,400 cap above 24,300 sit against -23,100 and -68,100 as the index falls, and because these figures include the long index leg the loss keeps deepening below 22,800 toward the index-to-zero worst case.

**Adjustments, variants & timing.** The core lever is the short 24300 call. If Nifty rallies toward it, roll the call up-and-out, buy it back and sell a higher strike in the next expiry, to lift the cap and bank a net credit; if the index drifts down, roll the call down to a lower strike to harvest more premium while your view stays neutral. Let it be "called away" (settle at the cap) only when the fixed gain meets your target and you are content to redeploy. In India you cannot literally own the index, so build this on a Nifty ETF/basket or, more commonly, long the Nifty future plus the short 24300 CE; index options are European and cash-settled, so there is no early assignment to fear and no scramble over dividends or delivery. Time the entry to elevated IV, India VIX rich and IV rank above 50, and prefer 30-45 days to expiry so monthly theta works without expiry-week gamma.

## 114. Covered Call (ATM)

*Neutral · Short vega · net debit*

**The idea (intuition).** Same landlord, but now you sell the upside starting right at today's price for the fattest possible rent. You expect Nifty to go nowhere, so you grab the maximum time value the ATM strike offers.

**When & why to use it.** This is the highest-income, lowest-upside version. Reach for it when your view is flat-to-slightly-down and IV is high — an ATM call holds the most extrinsic value, so a post-event IV crush is your friend. Skip it if you actually want participation in a rally; you have given up essentially all of it from the first point.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the 24000 CE @ 456. Premium collected is 456 points = ₹34,200 per lot. Net debit 23544.1 points — the large credit pulls your effective entry down to 23544.

![Figure: Covered Call (ATM) payoff at expiry](figs/strategies/covered_call_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit 456 points (₹34,200), reached at or above 24000 — you are already at max profit if the index simply holds. Max loss -23543 points if Nifty went to zero. Breakeven 23544. Net debit 23544.1. Risk:reward 0.02. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is near flat — the ATM call's ~0.5 delta cancels much of your long. Theta is strongly positive and is the main engine of P&L here. Vega is meaningfully negative; this trade loves IV falling.

**Management & exit.** Because you start at max profit, the play is to harvest decay early — close near 50-60% of the credit and redeploy, rather than holding to expiry for the last few points. If Nifty drops, the call's gains cushion you; consider rolling the call down to keep collecting if your neutral view persists.

**Risk note.** You have almost no upside and full downside, so an unexpected rally feels like a loss-of-opportunity and a selloff still hurts. The ATM short strike has the highest gamma, so P&L swings sharply into expiry — don't hold an ATM write into the last day.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -55,800 | -10,800 | +34,200 | +34,200 | +34,200 |

The table is flat at +34,200 from 24,000 upward (you start at max profit) but slides to -10,800 and -55,800 as Nifty drops, and since the P&L embeds the long index the red continues to widen below the grid toward the zero-index tail.

**Adjustments, variants & timing.** Because the ATM write starts at max profit, management is mostly about decay capture and defending the downside. If Nifty rises through 24000, roll the call up-and-out to a higher strike to reclaim some upside and take in a credit; if it falls, roll the call down to keep collecting premium while your neutral view holds, the call's gains cushioning the long. Let the position settle at the cap when you have banked most of the credit. On NSE this is a Nifty ETF/basket or long future plus the short 24000 CE, European and cash-settled, so no early assignment and no delivery mechanics; the "assignment" is just a cash difference at expiry. The ATM strike holds the most extrinsic value, so enter when IV is high and you expect a post-event IV crush; 30-45 days out is ideal, and never carry the high-gamma ATM short into the final session.

## 115. Covered Call (Deep ITM)

*Neutral, defensive · Short vega · net debit*

**The idea (intuition).** You sell a call that is already deep in the money, so almost all the premium is intrinsic value acting as a downside buffer. You are effectively pre-selling your index near 23600 and pocketing a small, near-certain return — a defensive, bond-like posture.

**When & why to use it.** Use it when you want to stay nominally long but are nervous, and you would happily exit at the short strike for a small fixed gain. The deep-ITM call gives the most downside cushion of any covered call. It is a poor choice if you are bullish — you have capped yourself below the current price.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the 23600 CE @ 728. Premium 728 points = ₹54,600 per lot, mostly intrinsic. Net debit 23272.4 points — your effective cost drops to 23272, the lowest of the covered-call set.

![Figure: Covered Call (Deep ITM) payoff at expiry](figs/strategies/covered_call_deep_itm.png)

**The numbers (modelled at Nifty 24000).** Max profit 328 points (₹24,600) anywhere at or above 23600. Max loss -23271 points in the zero-index scenario. Breakeven 23272. Net debit 23272.4. Risk:reward 0.01. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is low — the deep-ITM call has a high delta near 0.8-0.9, leaving you only lightly long. Theta is positive but smaller, since little extrinsic value remains to decay. Vega is mildly negative.

**Management & exit.** This is a hold-to-target trade: you are aiming for the fixed ~328-point return as long as Nifty stays above 23600. If the index falls below the strike, the intrinsic cushion absorbs it down to 23272; below that you take a managed loss. Roll down only if your view turns more defensive.

**Risk note.** The cushion is finite — a crash through 23272 still puts you in the red, and the tiny 0.01 risk:reward reflects that you risk a large base to earn a thin yield. Liquidity in deep-ITM strikes can be thin; mind the spread.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -35,400 | +9,600 | +24,600 | +24,600 | +24,600 |

The deep-ITM write locks +24,600 anywhere at or above 23,600 and still shows +9,600 at 23,400, but the -35,400 at 22,800, index loss included, keeps growing below the grid toward the index-to-zero worst case.

**Adjustments, variants & timing.** The deep-ITM write is a hold-to-target trade, so adjustments are defensive. If Nifty rallies, simply let it be "called away" at 23600 for the fixed ~328-point gain; there is little upside to chase. If the index falls toward and below 23600, roll the call down to a deeper strike to add cushion, or take the managed loss below 23272. You rarely roll up here. Implement on a Nifty ETF/basket or long future plus the short 23600 CE; index options are European and cash-settled, so the deep-ITM short carries no early-assignment risk despite being well in the money, a real edge over US single-stock covered calls. Note that deep-ITM strikes are often thin, so mind the bid-ask. Timing matters less than for ATM writes since little extrinsic value remains; enter when you want defensive carry and reasonable IV, and avoid it entirely if you expect a rally.

## 116. Cash-Secured Put (Entry)

*Bullish accumulation · Short vega · net credit*

**The idea (intuition).** You want to own Nifty cheaper, so you get paid to wait. Selling a put below the market is a standing limit-buy order with a rebate — if Nifty dips to your strike you "buy" it (in cash terms, settle the difference), and if it doesn't, you simply keep the premium.

**When & why to use it.** Ideal when you are bullish on a horizon but think the index is a touch rich today, and IV is elevated so the put pays well. It shines after a sharp selloff when fear has pumped put premiums. Don't sell puts into a falling knife or ahead of a known bearish catalyst — you can be filled far above where the index actually settles.

**How to build it (₹, Nifty).** Sell the 23500 PE @ 169. You receive 169 points = ₹12,675 per lot as a net credit (net_cost -168.6). In India this is "cash-secured" by keeping enough margin/cash to absorb assignment at 23500; remember there is no early assignment — settlement is cash at expiry.

![Figure: Cash-Secured Put (Entry) payoff at expiry](figs/strategies/cash_secured_put_entry.png)

**The numbers (modelled at Nifty 24000).** Max profit 169 points (₹12,675), kept in full if Nifty stays above 23500. Max loss -23330 points only if the index fell to zero. Breakeven 23331. Net credit 169 points. Risk:reward 0.01. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is positive (short put is bullish). Theta is positive — the put bleeds in your favour each day. Vega is negative; an IV drop after entry accelerates your gains.

**Management & exit.** Standard income management: buy the put back at ~50% of credit and redeploy, or let it expire worthless if far OTM. If Nifty breaks 23500 and you are still constructive, accept the "assignment" view and roll into a covered call (the wheel). If your thesis breaks, close for a stop at, say, 2x the credit received.

**Risk note.** The benign-looking 0.01 ratio hides a real tail — a gap below 23331 turns the rebate into a loss many times the credit. This is the classic trade where retail sellers feel safe right up until a crash. Size to the loss you can survive, not the premium you want.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -39,825 | +5,175 | +12,675 | +12,675 | +12,675 |

The put keeps its full +12,675 while Nifty holds at or above 23,500, fades to +5,175 at 23,400, and turns to -39,825 at 22,800, and that loss, the cash-settled assignment hit, deepens further below the grid toward the index-to-zero tail.

**Adjustments, variants & timing.** Manage the short 23500 put as a standing limit-buy. Close it at ~50% of credit and redeploy, or let it expire worthless if far OTM. If Nifty breaks 23500 and you remain constructive, take the cash-settled "assignment" view, re-establish the long via a Nifty ETF or future and pivot into a covered call (the wheel); if your thesis breaks, roll the put down-and-out to a lower strike to buy time, or stop out at ~2x the credit. Crucially, NSE index options are European and cash-settled, so there is no early assignment; settlement is a single cash difference at expiry, and "cash-secured" means holding the SPAN-plus-exposure margin, not parking the full notional. Sell into elevated IV, the trade shines after a sharp selloff when fear pumps put premium, at roughly 30-delta and 30-45 days out so theta bleeds steadily in your favour.

## 117. The Wheel

*Neutral to bullish, systematic · Short vega · net credit*

**The idea (intuition).** The wheel is a loop, not a single trade. You sell a cash-secured put; if Nifty stays up you keep the premium and repeat; if it drops to your strike you take the long position, then sell covered calls against it until it gets called away — and you start the put cycle again. It is a disciplined way to be paid at every step of accumulating and distributing the index.

**When & why to use it.** Run the wheel when you are structurally bullish-to-neutral on Nifty over many months and want a rules-based income engine rather than a directional bet. It suits patient, well-capitalised accounts in normal-to-high IV. Avoid running it through a sustained bear market — you keep getting "assigned" lower and your covered calls cap the eventual bounce.

**How to build it (₹, Nifty).** The cycle's opening leg here is sell the 23600 PE @ 192 — a credit of 192 points = ₹14,400 per lot (net_cost -192.2). If Nifty settles below 23600 you take the long (cash-settled in India, so you re-establish via a future/ETF), then sell an OTM call against it; rinse and repeat.

![Figure: The Wheel payoff at expiry](figs/strategies/the_wheel.png)

**The numbers (modelled at Nifty 24000).** For the current put leg: max profit 192 points (₹14,400) if Nifty holds above 23600. Max loss -23407 points in the zero scenario. Breakeven 23408. Net credit 192 points. Risk:reward 0.01. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Each leg is short vega and positive theta; the put leg is positive delta, the covered-call leg is reduced-positive delta. Across the full cycle you are a persistent theta harvester with a long bias.

**Management & exit.** Mechanise it: sell ~30-delta puts about 30-45 days out, close at 50% credit, and only accept assignment at strikes you genuinely want to own. After assignment, sell calls at or just above your cost basis so you are never forced to sell at a loss. Track cumulative basis, not single-leg P&L.

**Risk note.** The wheel's weakness is a trending decline — you collect small credits while the underlying grinds lower, and the math turns ugly fast. It is income with embedded downside, not a yield product; the SEBI loss statistics apply most to traders who run wheels too large.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -45,600 | -600 | +14,400 | +14,400 | +14,400 |

The opening put leg holds +14,400 above 23,600, is roughly flat (-600) at 23,400, and shows -45,600 at 22,800, the loss continuing well below the grid toward the index-to-zero worst case once you are carrying the long.

**Adjustments, variants & timing.** The wheel is mechanised: sell ~30-delta puts 30-45 days out, close each at 50% credit, and only accept assignment at strikes you genuinely want to own. If a put is tested but your view holds, roll it down-and-out for a credit; if Nifty settles below 23600, take the long (cash-settled, so re-establish via a Nifty ETF or future) and immediately sell OTM covered calls at or above your cost basis so you are never forced to sell at a loss, then let the call run to call-away and restart the put cycle. On NSE every leg is European and cash-settled: no early assignment, no delivery, just margin and cash differences. Run it in normal-to-high IV; avoid initiating fresh rungs ahead of a known bearish catalyst. Track cumulative basis across the whole loop, not single-leg P&L, and size so a trending decline cannot force you off the wheel.

## 118. Covered Strangle

*Bullish, own the stock · Short vega · net debit*

**The idea (intuition).** Own the index and sell both an OTM call and an OTM put against it. You are doubling your premium income on a view that Nifty drifts inside a range — but you have implicitly agreed to buy even more index if it falls (the short put) on top of the downside you already carry.

**When & why to use it.** Use it when you are genuinely happy to add to a long position lower and you expect a quiet, rangebound month with elevated IV on both wings. It is for accumulators with capital to absorb a second tranche. Do not use it if you cannot stomach being effectively 2x long after a drop — the short put stacks risk on the same side as your existing exposure.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the 24400 CE @ 246 and the 23600 PE @ 192. Combined premium 438 points = ₹32,850 per lot. Net debit 23561.9 points; the put adds income but also a second downside leg.

![Figure: Covered Strangle payoff at expiry](figs/strategies/covered_strangle.png)

**The numbers (modelled at Nifty 24000).** Max profit 838 points (₹62,850) between the strikes at expiry. Max loss -47160 points — roughly double a plain covered call, reflecting the long index plus the short put both losing as Nifty falls toward zero. Breakeven 23581. Net debit 23561.9. Risk:reward 0.02. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is positive and rises if Nifty falls (the short put adds long delta on the way down). Theta is strongly positive — two short options decaying. Vega is doubly negative; an IV spike hurts both short legs.

**Management & exit.** Manage the wings independently: buy back whichever short option reaches 50% profit, and roll the tested side rather than the whole structure. If Nifty drops to the put strike, decide deliberately whether to add the index or close — that is the whole point of the trade. Take it off before expiry-week gamma.

**Risk note.** This is the most downside-heavy income trade in the group — the ~-47160 max loss is the honest signal that you are short the put on top of a long. A fast selloff hits the long index and the short put simultaneously. Reserve it for index/ETF positions you truly want to double, sized accordingly.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -117,150 | -27,150 | +32,850 | +62,850 | +62,850 |

The strangle peaks at +62,850 between the strikes but the doubled downside shows starkly, -27,150 at 23,400 and -117,150 at 22,800, and with both the long index and the short put losing together the red accelerates below the grid toward the zero-index tail.

**Adjustments, variants & timing.** Manage the two wings independently. Buy back whichever short, the 24400 call or the 23600 put, reaches 50% profit, and roll the tested side rather than the whole structure: roll the call up-and-out on a rally, roll the put down-and-out on a dip if you are not yet ready to add. When Nifty touches the put strike, decide deliberately whether to accept the second tranche of index (cash-settled, re-established via ETF/future) or close; that choice is the whole point of the trade. Build on a Nifty ETF/basket or long future plus the two short legs; European cash settlement means no early assignment on either wing. Enter when IV is elevated on both wings and you expect a quiet, rangebound month, 30-45 days out, and take it off before expiry-week gamma whips the short strikes. Reserve it for positions you truly want to double.

## 119. Covered Combo

*Bullish income · Short vega · net debit*

**The idea (intuition).** A close cousin of the covered strangle, but the short put is placed further out of the money than the call. You tilt the structure: more comfortable income on the upside cap, a deeper, less likely entry point on the downside add. It is a covered call with a discounted "buy lower" order attached.

**When & why to use it.** Choose the combo over the strangle when you want the second-tranche entry to sit at a level you would only buy on a real dip, while still grabbing decent call premium today. Good in neutral-to-bullish, moderate-IV conditions. Avoid it if you are not prepared to be longer after a fall — the short put still stacks downside.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the 24300 CE @ 292 and the 23400 PE @ 148. Combined premium 440 points = ₹33,000 per lot. Net debit 23560.5 points.

![Figure: Covered Combo payoff at expiry](figs/strategies/covered_combo.png)

**The numbers (modelled at Nifty 24000).** Max profit 739 points (₹55,425) in the zone between the strikes. Max loss -46959 points in the zero-index case, again reflecting the doubled downside from the short put. Breakeven 23561. Net debit 23560.5. Risk:reward 0.02. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Positive net delta with a long bias that increases as Nifty falls toward the put. Theta positive from two short legs. Vega negative — quiet, decaying tape is ideal.

**Management & exit.** Same discipline as the strangle: close each short at ~50% profit, roll the tested wing, and treat a touch of the 23400 put as a planned accumulation, not an accident. Because the put is further OTM than the call, the call usually needs management first in a rising market.

**Risk note.** The asymmetric strikes make the upside cap bind sooner while the downside add sits deeper, so a sharp rally caps you quickly and a deep selloff still doubles your loss. The headline -46959 figure is the zero-collapse tail; real risk management is sizing and a credit-multiple stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -102,075 | -12,075 | +32,925 | +55,425 | +55,425 |

The combo tops out at +55,425 in the zone, prints -12,075 at 23,400 and -102,075 at 22,800, and because the figures fold in the long index plus the short put the loss keeps doubling lower toward the index-to-zero worst case.

**Adjustments, variants & timing.** Same discipline as the strangle but with asymmetric strikes. Close each short at ~50% profit and roll the tested wing: because the 23400 put is further OTM than the 24300 call, the call usually needs attention first in a rising market, so roll it up-and-out to lift the cap. Treat a touch of the 23400 put as planned accumulation, not an accident; on a dip, either accept the cash-settled second tranche (re-established via ETF/future) or roll the put down-and-out if you want a still-deeper entry. Implement on a Nifty ETF/basket or long future plus the two shorts; NSE index options are European and cash-settled, so neither leg can be assigned early. Choose the combo over the strangle when you want the downside add to sit at a level you would only buy on a real dip. Enter in neutral-to-bullish, moderate-IV tape, 30-45 days out, and clear it before expiry-week gamma.

## 120. Ratio Write

*Neutral, range-bound · Short vega · net debit*

**The idea (intuition).** You own one unit of the index but sell two calls against it. The extra (naked) call supercharges your premium and pins your best outcome to a tight zone, but above that zone the second call turns the position net short and your profit reverses. It is income with a ceiling and a trapdoor.

**When & why to use it.** Deploy it only when you have a firm conviction that Nifty stalls near the short strike — a pinned, low-momentum expiry with rich call IV. It is a tactician's neutral trade. Never use it casually: the extra short call means open-ended risk above, so it is unsuitable when any upside breakout is plausible (results day, global risk-on).

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell 2x 24200 CE @ 342 each (684 points total = ₹51,300 per lot of premium). Net debit 23315.2 points. The second call is uncovered, which is what creates the upside tail.

![Figure: Ratio Write payoff at expiry](figs/strategies/ratio_write.png)

**The numbers (modelled at Nifty 24000).** Max profit 884 points (₹66,300) at the short strike 24200. Max loss is Undefined — large: above the upper breakeven the naked call runs without limit. Two breakevens, 23315 and 25085 — you profit only between them. Net debit 23315.2. Risk:reward is undefined because the upside is open. This worst case assumes an uncapped move; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta starts near flat and turns negative as Nifty rises past the strike (the two short calls overpower the single long). Theta is strongly positive at the pin. Vega is sharply negative — a volatility spike with an up-move is the nightmare combination.

**Management & exit.** Define an upside stop in advance — buy back one call or add a long call above 25085 to cap the tail if Nifty trends up. Harvest profit if the index sits near 24200 into expiry, but never let an unmanaged ratio run into a breakout. Roll the extra short up-and-out if tested.

**Risk note.** This is the one genuinely open-ended trade in the chapter on the upside — the naked call can lose far more than all the premium collected. Treat the second short as a position to be hedged, not forgotten.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -38,625 | +6,375 | +51,375 | +36,375 | -8,625 |

The ratio is richest near the 24,200 pin (+51,375 at 24,000, +36,375 at 24,600) but the naked second call bites on the upside, only +6,375 at 23,400, -38,625 at 22,800, and crucially -8,625 already at 25,200 with the loss running open-ended above the grid.

**Adjustments, variants & timing.** The ratio write demands a pre-defined upside stop because the second, naked call is open-ended. If Nifty trends up toward the 25085 breakeven, buy back one call or add a long call above it to convert the tail into a defined-risk butterfly or ratio spread; roll the extra short up-and-out if tested but never let it run unmanaged into a breakout. Harvest profit if the index pins near 24200 into expiry. Build on a Nifty ETF/basket or long future plus the two short 24200 CE; NSE index options are European and cash-settled, so there is no early assignment, but the naked call's expiry loss is still real cash. Deploy only when you have firm conviction Nifty stalls near the strike, in rich call IV, 20-40 days out; avoid it entirely around results, Budget or global risk-on events where an upside breakout, the nightmare with sharply negative vega, is plausible.

## 121. Covered Call (Weekly)

*Neutral · Short vega · net debit*

**The idea (intuition).** Instead of one monthly rent cheque, you collect a small one every week. Weekly options decay fastest in their final days, so selling them repeatedly against your index harvests theta at a quicker clip — at the cost of more transactions and tighter caps.

**When & why to use it.** Best on Nifty/Bank Nifty where weekly expiries are deeply liquid and you want frequent, fast-decaying income with the flexibility to re-strike each week to your latest view. Suits a flat tape where you can adjust nimbly. Avoid it if you cannot monitor weekly — an unattended weekly short call through a rally caps you with no time to roll.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the weekly 24250 CE @ 91. Premium 91 points = ₹6,825 per lot for the week. Net debit 23909.3 points — the smaller weekly credit means a higher effective cost than monthly writes.

![Figure: Covered Call (Weekly) payoff at expiry](figs/strategies/covered_call_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 341 points (₹25,575) at or above 24250 for this expiry. Max loss -23908 points in the zero scenario. Breakeven 23909. Net debit 23909.3. Risk:reward 0.01. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive but reduced by the short call. Theta is the strongest of the covered-call variants per day, because weekly extrinsic value decays rapidly. Vega negative but small in absolute terms given the short tenor.

**Management & exit.** The weekly cadence is the management: let it expire or close near 50% early in the week, then re-sell the next weekly at a strike matching your fresh view. Roll up-and-out intra-week if Nifty threatens 24250. Annualised, the repeated small credits can exceed a single monthly write — if you avoid getting run over on a breakout week.

**Risk note.** Weeklies carry the highest gamma into Thursday/Friday expiry, so the short strike can flip from safe to deep-ITM in hours. Frequent trading also multiplies STT, brokerage and slippage — net yield is lower than the gross premiums suggest.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -83,175 | -38,175 | +6,825 | +25,575 | +25,575 |

The weekly write holds +25,575 above 24,250 and +6,825 at 24,000 but turns to -38,175 and -83,175 as the index drops, index loss included, so the red keeps deepening below the grid toward the zero-index tail.

**Adjustments, variants & timing.** With weeklies the cadence is the management. Let the 24250 call expire or close near 50% early in the week, then re-sell the next weekly at a strike matching your fresh view; re-striking weekly is the main lever. Roll up-and-out intra-week if Nifty threatens 24250 to keep some upside; roll down to collect more if it sags and your neutral view holds. On NSE, Nifty and Bank Nifty weeklies are deeply liquid, European and cash-settled, so there is no early assignment; build on an ETF/basket or long future plus the short weekly call. Watch the calendar: weekly gamma spikes into Thursday/Friday expiry, so the short strike can flip from safe to deep-ITM in hours, never leave it unattended. Annualised, the repeated small credits can exceed a single monthly write, but only if you avoid run-over weeks and respect that frequent trading multiplies STT and slippage.

## 122. Covered Put

*Bearish income · Short vega · net credit*

**The idea (intuition).** This is the mirror image of the covered call. You are short the index and sell a put against the short, collecting premium while expressing a bearish-to-neutral view. The short put caps how much you gain on the downside, just as a covered call caps upside on a long.

**When & why to use it.** Use it when you are bearish on Nifty but expect a controlled grind lower rather than a crash, and you want income to offset the cost of carrying a short. It fits high-IV, risk-off regimes. Avoid it in a rallying or squeeze-prone market — being short the index leaves your upside loss open, and a sharp bounce is brutal.

**How to build it (₹, Nifty).** Short 1x Nifty @ 24000, sell the 23700 PE @ 219. Premium 219 points = ₹16,425 per lot, taken in as a net credit (net_cost -24218.8 reflects the short index proceeds plus the put credit).

![Figure: Covered Put payoff at expiry](figs/strategies/covered_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 519 points (₹38,925) if Nifty falls to or below 23700. Max loss is Undefined — large: because you are short the index, your loss grows without limit as Nifty rises. Breakeven 24219. Net credit. Risk:reward undefined (open-ended upside loss). This worst case is an uncapped up-move rather than a collapse; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is negative — bearish. Theta is positive from the short put. Vega is negative; an IV spike (often accompanying the selloff you want) ironically pressures the short put even as your short index profits.

**Management & exit.** Target the 519-point max as Nifty approaches 23700, closing the put at ~50% profit and deciding whether to keep the short. Place a hard stop on the upside — this is the dangerous side. Roll the put down to keep collecting if the decline extends and your view holds.

**Risk note.** The open-ended loss sits on the upside here, not the downside. Short-index positions can be squeezed violently on good news; never run a covered put without an upside stop, and respect that shorting the index carries its own carry and gap risks.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +38,925 | +38,925 | +16,425 | -28,575 | -73,575 |

This bearish trade is the mirror, +38,925 at and below 23,700 and +16,425 at 24,000 but -28,575 and -73,575 as Nifty rises, and because you are short the index the loss is open-ended, continuing to grow above the grid rather than below it.

**Adjustments, variants & timing.** This bearish trade's danger is the open-ended upside, so a hard upside stop is non-negotiable. Target the 519-point max as Nifty approaches 23700, closing the short put at ~50% profit and deciding whether to keep the short index leg. Roll the put down-and-out to keep collecting if the decline extends and your view holds; if Nifty squeezes higher, cover the short and the put together at your stop rather than hoping. In India you express the short via a short Nifty future (or inverse ETF) plus the short 23700 PE; index options are European and cash-settled, so no early assignment, but the short future carries its own carry and gap risk. Enter in high-IV, risk-off regimes when you expect a controlled grind lower, 30-45 days out. Beware: an IV spike that accompanies the selloff you want actually pressures the short put even as the short index profits.

## 123. Dividend-Capture Covered Call

*Neutral, yield · Short vega · net debit*

**The idea (intuition).** You hold the index (or a dividend-paying ETF/basket) primarily for its yield, and you sell a call on top to enhance the total return. Two income streams — dividends plus call premium — stacked on one long position. The call funds part of your cost and boosts realised yield in a flat market.

**When & why to use it.** Best when you are a yield-oriented holder of a Nifty ETF or dividend basket and want to juice returns in a sideways tape with reasonable call IV. The strike is set just OTM so you keep some upside to any ex-dividend drift. Avoid it if a strong rally is likely — you would rather not cap a holding you intend to keep long term.

**How to build it (₹, Nifty).** Long 1x index/ETF @ 24000, sell the 24200 CE @ 459. Premium 459 points = ₹34,425 per lot. Net debit 23540.9 points; dividends accrue separately on the long.

![Figure: Dividend-Capture Covered Call payoff at expiry](figs/strategies/dividend_covered_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 659 points (₹49,425) at or above 24200, excluding any dividend received. Max loss -23540 points in the zero scenario. Breakeven 23541. Net debit 23540.9. Risk:reward 0.03 — among the better ratios in the group, helped by the rich call. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive, reduced by the short call. Theta positive. Vega negative. The dividend adds a small, non-Greek positive carry independent of the options.

**Management & exit.** Hold for the dividend window and let the call decay; close it at 50% credit if Nifty stalls, then re-sell. Because index options are cash-settled and European, there is no early-exercise-to-grab-dividend dynamic as there is on US single stocks — the "capture" here is simply combining yield with premium, not exploiting assignment timing.

**Risk note.** You still own all the downside of the index; a price drop swamps any dividend and call premium combined. On single-stock covered calls (vs the index) STT on exercised ITM options and dividend taxation can erode the edge — model the all-in, post-tax yield, not the gross.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -55,575 | -10,575 | +34,425 | +49,425 | +49,425 |

The dividend write caps at +49,425 above 24,200, holds +34,425 at 24,000, then falls to -10,575 and -55,575, excluding any dividend, and with the long index embedded the loss keeps widening below the grid toward the zero-index worst case.

**Adjustments, variants & timing.** Hold through the dividend/ex-date window and let the 24200 call decay; close it at ~50% credit if Nifty stalls, then re-sell. Roll up-and-out on a rally to preserve some upside on a holding you intend to keep, or roll down to collect more in a soft tape. Crucially, because NSE index options are European and cash-settled, there is none of the US single-stock early-exercise-to-grab-dividend dynamic; the "capture" is simply stacking ETF/basket yield on top of call premium, not exploiting assignment timing. Implement on a dividend-paying Nifty ETF or basket (not a future, which earns no dividend) plus the short 24200 CE. Enter in a sideways tape with reasonable call IV, strike just OTM to keep ex-dividend drift, 30-45 days out. If you run it on single stocks rather than the index, model the all-in post-tax yield, since STT on exercised ITM options and dividend taxation can quietly erode the edge.

## 124. Short Put Ladder (Income)

*Bullish accumulation · Short vega · net credit*

**The idea (intuition).** Rather than one put, you sell two at different lower strikes, layering your willingness to buy across price levels. Each rung pays premium and marks an accumulation point — a staircase of "buy lower" orders, each with its own rebate.

**When & why to use it.** Use it when you want to scale into a long Nifty position on weakness and collect more premium than a single put, in a bullish-accumulation frame with elevated IV. The laddered strikes let you average in if the index falls in steps. Avoid it ahead of a potential crash — selling two puts doubles your assignment exposure on the same downside.

**How to build it (₹, Nifty).** Sell the 23700 PE @ 219 and the 23400 PE @ 148. Combined premium 367 points = ₹27,525 per lot, taken as a net credit (net_cost -366.3). Each rung is cash-secured by the margin to absorb settlement at its strike.

![Figure: Short Put Ladder (Income) payoff at expiry](figs/strategies/short_put_ladder_income.png)

**The numbers (modelled at Nifty 24000).** Max profit 366 points (₹27,525) if Nifty holds above 23700 and both puts expire worthless. Max loss -46732 points in the zero-index case — roughly double a single short put, since both rungs lose together. Breakeven 23367. Net credit 366 points. Risk:reward 0.01. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive and increasing as Nifty falls (more long exposure builds with each rung). Theta strongly positive — two decaying puts. Vega negative; an IV crush after entry is ideal.

**Management & exit.** Manage rung by rung: close the higher 23700 put at 50% profit first, keep the lower 23400 as a deeper standing bid. If both get tested, you have accumulated at two levels — exactly the plan — and you can pivot into covered calls (the wheel). Stop the structure if your bullish thesis breaks.

**Risk note.** Two short puts mean the downside tail is doubled; the modest credit looks safe until a gap blows through both strikes at once. This is layered accumulation for traders who can fund and survive being long at both levels — not a free-yield ladder.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -85,050 | +4,950 | +27,450 | +27,450 | +27,450 |

The ladder keeps its full +27,450 above 23,700 and still +4,950 at 23,400, but two short puts show their weight at -85,050 by 22,800, the loss roughly doubling a single put and deepening further below the grid toward the index-to-zero tail.

**Adjustments, variants & timing.** Manage the ladder rung by rung. Close the higher 23700 put at 50% profit first and keep the lower 23400 as a deeper standing bid; if the upper rung is tested but your view holds, roll it down-and-out for a credit. If both get tested, you have accumulated at two levels exactly as planned, so re-establish the long (cash-settled via ETF/future) and pivot the rungs into covered calls (the wheel). Stop the structure if your bullish thesis breaks. On NSE both puts are European and cash-settled, so neither can be assigned early; "cash-secured" means holding the combined SPAN margin for two strikes, not the full notional of both. Enter in a bullish-accumulation frame with elevated IV, ~30-delta on the upper rung and a deeper lower rung, 30-45 days out. Size for the doubled downside tail, since a gap through both strikes at once is the real risk, not the modest combined credit.

## 125. Buy-Write

*Neutral to mildly bullish · Short vega · net debit*

**The idea (intuition).** A buy-write is simply a covered call opened in a single transaction — you "buy" the index and "write" the call simultaneously as one packaged trade. The point is execution: one net price, no leg risk, a clean defined-income position from the first tick.

**When & why to use it.** Use it whenever you want covered-call income but prefer to enter the long and short together at a known net debit, avoiding the slippage of legging in. Common as a structured product wrapper and for disciplined income desks. Same caveats as any covered call — skip it before a catalyst you want full upside for, or in a downtrend.

**How to build it (₹, Nifty).** Buy 1x Nifty @ 24000 and sell the 24300 CE @ 404 in one ticket. Premium 404 points = ₹30,300 per lot. Net debit 23595.8 points — your packaged cost basis.

![Figure: Buy-Write payoff at expiry](figs/strategies/buy_write.png)

**The numbers (modelled at Nifty 24000).** Max profit 704 points (₹52,800) at or above 24300. Max loss -23595 points in the zero scenario. Breakeven 23596. Net debit 23595.8. Risk:reward 0.03. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive, dampened by the short call. Theta positive — the short call decays for you. Vega negative; you want IV to fall after you open.

**Management & exit.** Treat it exactly like an OTM covered call: close the call at ~50% credit, roll up-and-out on a rally, and take profit as the index approaches 24300. The single-ticket entry also makes a single-ticket exit clean if you want out of the whole structure.

**Risk note.** All the covered-call risks apply — capped upside, full downside in the index. The "packaged" nature can lull you into thinking it is a product rather than a leveraged long with a sold call; the underlying index exposure is what can hurt you.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -59,700 | -14,700 | +30,300 | +52,800 | +52,800 |

The buy-write caps at +52,800 above 24,300 and holds +30,300 at 24,000, sliding to -14,700 and -59,700 as the index falls, the figures including the packaged long so the loss keeps growing below the grid toward the zero-index worst case.

**Adjustments, variants & timing.** Treat the buy-write exactly like an OTM covered call once on. Close the short 24300 call at ~50% credit, roll it up-and-out on a rally to lift the cap, or roll it down to collect more if the index sags and your view stays neutral; take the fixed gain as Nifty approaches 24300. The single-ticket structure means you can also exit the whole position in one clean ticket if you want out. In India the "buy" leg is a Nifty ETF/basket or long future, packaged with the short 24300 CE at one net debit to avoid legging slippage; index options are European and cash-settled, so no early assignment and no delivery. Enter when IV is elevated enough that the call pays a meaningful credit, 30-45 days out, and avoid it just before a catalyst you would want full upside for. Remember the packaging hides a leveraged long with a sold call, and the index downside is what hurts.

## 126. In-the-Money Covered Call

*Defensive income · Short vega · net debit*

**The idea (intuition).** You sell a call that is slightly in the money, trading away near-term upside for a thicker premium and a bigger downside cushion. It sits between the OTM income write and the deep-ITM defensive write — more protection than the former, more yield than the latter.

**When & why to use it.** Reach for it when you are cautious-but-still-holding and want a fixed, modest target with a real buffer beneath the current price. Useful in choppy, slightly soft markets with good IV. Not for bulls — you have capped yourself below 24000 from the outset, so any rally just delivers the small fixed gain.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the 23800 CE @ 585. Premium 585 points = ₹43,875 per lot, part intrinsic. Net debit 23415.0 points — effective cost pulled down to 23415.

![Figure: In-the-Money Covered Call payoff at expiry](figs/strategies/itm_covered_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 385 points (₹28,875) anywhere at or above 23800. Max loss -23414 points if Nifty fell to zero. Breakeven 23415. Net debit 23415.0. Risk:reward 0.02. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta is low — the ITM call's higher delta offsets much of the long. Theta positive but moderate (less extrinsic value than ATM). Vega negative.

**Management & exit.** A target trade: you are already at max profit if Nifty simply holds above 23800, so harvest early and redeploy rather than chasing the last points. The 585-point premium cushions a fall to 23415 before you are in the red. Roll down further if you want even more protection.

**Risk note.** The buffer is finite — below 23415 the long index losses overwhelm the premium. The slightly ITM strike has elevated gamma near expiry, and the position quietly carries full crash risk despite its defensive label.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -46,125 | -1,125 | +28,875 | +28,875 | +28,875 |

The slightly-ITM write locks +28,875 anywhere at or above 23,800 (already +28,875 at 24,000), but the buffer is finite, -1,125 at 23,400 and -46,125 at 22,800, the loss deepening below the grid toward the index-to-zero tail.

**Adjustments, variants & timing.** The slightly-ITM write is a defined-target trade: you are already at max profit if Nifty simply holds above 23800, so harvest early and redeploy rather than chasing the last points. If the index falls toward 23415, roll the call down to a deeper strike for more cushion, or take the managed loss below it; if it rallies, just accept the fixed gain via call-away, since there is little upside to defend. Build on a Nifty ETF/basket or long future plus the short 23800 CE; NSE index options are European and cash-settled, so the in-the-money short carries no early-assignment risk. Enter in a choppy, slightly soft tape with good IV when you want a buffer beneath the current price, 30-45 days out. Watch expiry-week gamma, since the slightly-ITM strike is gamma-sensitive near expiry, and never forget the position still carries full crash risk below 23415 despite its defensive label.

## 127. Cash-Secured Put (Weekly)

*Bullish, systematic · Short vega · net credit*

**The idea (intuition).** The cash-secured put run on a weekly cadence — sell a short-dated OTM put, harvest its fast theta, and repeat every week while you wait to buy Nifty lower. Small credits, collected often, with the quickest decay clock.

**When & why to use it.** Best for systematic sellers on liquid Nifty/Bank Nifty weeklies who want frequent income and the flexibility to re-strike to each week's view. Suits a flat-to-up tape with steady IV. Avoid it if you cannot watch weekly expiries — a weekly put can go from far-OTM to ITM in a single bad session with no time to adjust.

**How to build it (₹, Nifty).** Sell the weekly 23750 PE @ 83. Premium 83 points = ₹6,225 per lot for the week, taken as a net credit (net_cost -83.2). Hold margin/cash to settle at 23750 if assigned at expiry (cash-settled, European — no early assignment).

![Figure: Cash-Secured Put (Weekly) payoff at expiry](figs/strategies/cash_secured_put_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 83 points (₹6,225) if Nifty stays above 23750 this week. Max loss -23666 points in the zero scenario. Breakeven 23667. Net credit 83 points. Risk:reward 0.00 — the rounding flags just how thin the reward is versus the buffered base. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive but small (far-OTM, short tenor). Theta is the highest per-day of the put writes, thanks to rapid weekly decay. Vega negative but modest in absolute terms.

**Management & exit.** Let it expire worthless or close at 50% mid-week, then re-sell the next weekly. If Nifty drops toward 23750, roll down-and-out or accept the long and pivot to a covered call. The repeated tiny credits compound only if you avoid the occasional run-over week.

**Risk note.** The 0.00 ratio is the honest warning: you are risking a large buffered base to earn a few thousand rupees a week. Weekly gamma is unforgiving near expiry, and transaction costs eat a real share of an 83-point premium. This is the archetype of the trade where retail sellers misjudge the tail.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -65,025 | -20,025 | +6,225 | +6,225 | +6,225 |

The weekly put keeps its full +6,225 while Nifty holds at or above 23,750, then drops to -20,025 and -65,025 as the index falls, a vivid picture of risking a large buffered base for a thin credit, with the loss continuing below the grid toward the zero-index tail.

**Adjustments, variants & timing.** The weekly put run is managed by cadence. Let the 23750 put expire worthless or close at ~50% mid-week, then re-sell the next weekly at a strike matching your fresh view; re-striking is the main lever. If Nifty drops toward 23750, roll down-and-out to a lower strike for a credit, or accept the cash-settled long (re-established via ETF/future) and pivot into a covered call. On NSE, Nifty and Bank Nifty weeklies are deeply liquid, European and cash-settled, so there is no early assignment; "cash-secured" means holding the SPAN margin, not the full strike notional. Sell in a flat-to-up tape with steady IV, far-OTM, and respect that weekly gamma is unforgiving into Thursday/Friday expiry, since a far-OTM put can go ITM in one bad session. The tiny credits compound only if you avoid run-over weeks and remember transaction costs eat a real share of an 83-point premium.

## 128. Covered Call (Long-Dated)

*Neutral, patient · Short vega · net debit*

**The idea (intuition).** Sell a longer-dated call against your index instead of a near-month one. You collect a larger upfront premium and set a wider upside cap, trading the speed of weekly theta for a bigger one-time credit and less frequent management. The patient holder's covered call.

**When & why to use it.** Use it when you intend to hold Nifty for the long haul and want substantial premium and a higher strike that still leaves room to run, without re-writing every month. Good in elevated long-dated IV. Less suitable if you want fast decay — long-dated options bleed theta slowly, so the income accrues gradually.

**How to build it (₹, Nifty).** Long 1x Nifty @ 24000, sell the longer-dated 24500 CE @ 573. Premium 573 points = ₹42,975 per lot. Net debit 23427.5 points.

![Figure: Covered Call (Long-Dated) payoff at expiry](figs/strategies/covered_call_leaps.png)

**The numbers (modelled at Nifty 24000).** Max profit 1073 points (₹80,475) at or above 24500 — the widest cap and largest absolute profit of the covered-call set, thanks to the higher strike plus the fat premium. Max loss -23426 points in the zero scenario. Breakeven 23427. Net debit 23427.5. Risk:reward 0.05 — the best ratio in the chapter. This worst case assumes the index collapses to zero; in practice you size small and manage/stop at a multiple of the credit.

**Greeks & behaviour.** Net delta positive, only modestly reduced (a higher-strike call has lower delta), so you retain more bullish participation than near-ATM writes. Theta positive but slow. Vega is the most negative of the covered calls in absolute terms — long-dated options are vega-heavy, so an IV drop is a meaningful tailwind.

**Management & exit.** You can hold for the wide 1073-point target or, because long-dated extrinsic value is large, buy the call back after a good IV-driven decay and re-write. Roll up if Nifty approaches 24500 well before expiry. The slow theta rewards patience over tinkering.

**Risk note.** The bigger premium does not change that you own the full index downside; a long holding period also means more time for a drawdown to develop. The heavy negative vega cuts both ways — a volatility spike marks the short call against you even if price is unchanged.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -47,025 | -2,025 | +42,975 | +80,475 | +80,475 |

The long-dated write offers the widest cap, +80,475 above 24,500 and +42,975 at 24,000, but still carries full downside, -2,025 at 23,400 and -47,025 at 22,800, with the index loss embedded and deepening below the grid toward the zero-index worst case.

**Adjustments, variants & timing.** The long-dated write rewards patience over tinkering because its theta bleeds slowly. You can hold for the wide 1073-point target or, since long-dated extrinsic value is large and the trade is vega-heavy, buy the call back after a good IV-driven decay and re-write at a fresh strike. Roll up-and-out if Nifty approaches 24500 well before expiry to lift the cap; roll down only if you turn defensive. Implement on a Nifty ETF/basket or long future plus the longer-dated 24500 CE; NSE index options are European and cash-settled, so even a far-dated short carries no early-assignment risk. Enter when long-dated IV is elevated, since the most negative vega of the covered-call set makes an IV drop a meaningful tailwind, while a spike marks the short against you even at unchanged price. A longer holding period means more time for a drawdown, so size for the full index downside you still own.
