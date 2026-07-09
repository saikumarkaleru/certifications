# Strategy Group 10: Synthetics & Arbitrage

This family is built on one equation — put-call parity: C - P = S - K*e^(-r*T). Read that as "a call minus a put at the same strike equals the stock minus the present value of the strike." It means any one of the four instruments (stock, call, put, cash) can be rebuilt from the other three, so every position has a synthetic twin that behaves identically at expiry. Traders use synthetics to replicate a payoff they cannot or do not want to hold directly, while desks and arbitrageurs assemble fully-hedged "locked" packages — conversions, reversals, boxes, jelly rolls — that strip out direction entirely and leave only the financing rate, dividends, and skew. Be warned up front: on NSE these locked trades earn the risk-free rate minus costs, and STT, brokerage and the bid-ask usually swallow the two-point edge. These are professional relative-value tools, not retail money trees.

## 143. Synthetic Long Stock
*Bullish (futures-like) · Neutral vega · net debit*

**The idea (intuition).** Buy a call and sell a put at the same strike and you own the index without owning the index. Above the strike the call carries you up; below it the short put drags you down one-for-one — exactly what a long future does. Parity guarantees the two are the same line.

**When & why to use it.** Use it when you are outright bullish on Nifty but want options-account flexibility — say the single-stock future is illiquid, margins are friendlier, or you want to leg into a spread later. It is a clean directional bet for someone who has a view and no desire to pay time value. Do NOT use it if you want defined risk: this has the full downside of a long future. Avoid when IV is so high that the call you buy is far richer than the put you sell, creating a needless debit.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24000 PE @ 318. Net debit 137.7 points, about ₹10,328 per lot (137.7 × 75). That small debit is essentially the cost-of-carry priced into the synthetic future.

![Figure: Synthetic Long Stock payoff at expiry](figs/strategies/synthetic_long_stock.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -24137.0 points (the index falling to zero — catastrophic but bounded). Breakeven: 24138. Net debit 137.7 points (~₹10,328). Risk:reward undefined (one side unlimited).

**Greeks & behaviour.** Net delta ≈ +1.0 per unit — pure direction. Theta and vega roughly cancel because you are long one option and short another at the same strike, so this is genuinely a futures proxy, not a volatility trade.

**Management & exit.** Manage it like a long future: trail a stop under support, or convert to a risk-defined structure by buying a protective put if the tape turns. Take it off when your price target prints or your thesis breaks.

**Risk note.** The honest danger is the same as any leveraged long — a gap-down hits the short put with no floor. This worst case assumes the index collapses to zero; in practice you size small and stop out at a multiple of the debit.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹100,350 | -₹55,350 | -₹10,350 | +₹34,650 | +₹79,650 |

Read left to right the line climbs steadily, losing -₹100,350 if Nifty falls to 22,800 and gaining +₹79,650 at 25,200 — a clean one-for-one bullish profile, exactly like a long future.

**Adjustments, variants & timing.** A desk treating this as a futures proxy simply carries it and manages delta like any long future, rolling to the next series before expiry or unwinding the moment the cash-future basis makes the listed future cheaper to hold. Put-call parity (C - P = S - K*e^(-r*T)) is the screen tell: when the 24000 call trades rich to the put by more than fair carry, the synthetic long is being offered below the future, and an arbitrage desk will leg in. For a retail bull, though, the honest accounting matters — STT on the option legs, brokerage on two strikes, and the bid-ask you cross to get filled usually exceed the thin carry edge versus simply buying the Nifty future. The synthetic earns its keep only when the future is illiquid or margin treatment is friendlier. It is a financing / relative-value construction first; as a directional punt the listed future is almost always cheaper and cleaner on NSE.

## 144. Synthetic Short Stock
*Bearish (futures-like) · Neutral vega · net credit*

**The idea (intuition).** Flip the previous trade: sell the call, buy the put at one strike and you are synthetically short the index. The long put pays as the market falls, the short call bleeds against you on a rally — a mirror of a short future.

**When & why to use it.** Reach for it when you want downside exposure but shorting the cash index is awkward and the future is thin or carries an unfavourable basis. It suits a tactical bearish swing into an event — a hawkish RBI, a weak global cue — where you want one-for-one participation without paying for a put outright. Do NOT use it as "cheap insurance"; it is a naked directional short with an unlimited tail. Skip it when borrow/financing makes the short call expensive relative to the put.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 24000 PE @ 318. Net credit 137.7 points, about ₹10,328 per lot received. The credit is the carry working in your favour as the synthetic short seller.

![Figure: Synthetic Short Stock payoff at expiry](figs/strategies/synthetic_short_stock.png)

**The numbers (modelled at Nifty 24000).** Max profit: 24137.0 points (index to zero — the bounded best case). Max loss: Undefined — large (a runaway rally through the short call). Breakeven: 24138. Net credit 137.7 points (~₹10,328). Risk:reward undefined.

**Greeks & behaviour.** Net delta ≈ -1.0 per unit. Like its long twin, theta and vega offset, so P&L is driven almost entirely by price, not time or volatility.

**Management & exit.** Treat it as a short future: hard stop above resistance, or cap the tail by buying a cheap OTM call to cut the structure into a defined-risk short. Cover when your downside target is met.

**Risk note.** An overnight gap-up — a surprise global rally or a positive policy shock — is the killer, since the short call's loss is theoretically unlimited. Always pre-define the stop; never let a synthetic short run unhedged through results season.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹100,350 | +₹55,350 | +₹10,350 | -₹34,650 | -₹79,650 |

The line is the mirror image — a gain of +₹100,350 if Nifty drops to 22,800 fading to a loss of -₹79,650 at 25,200 — one-for-one downside participation like a short future.

**Adjustments, variants & timing.** Managed as a short future, the desk trails delta and rolls the series, unwinding whenever the basis turns favourable enough to short the listed future outright instead. Parity flags the entry: when the 24000 call is cheap to the put beyond fair carry, the synthetic short can be assembled above the future's price, and an arb book captures the gap risk-free. But for a retail bear the same caution applies as everywhere in this group — STT (charged more harshly on the sold call), brokerage across two legs, and the spread you pay typically swamp the few points of edge over a plain short future. The synthetic is justified only when the future is thin or the short-borrow on cash is awkward. Treat it as a financing-and-access tool a desk reaches for to stay delta-neutral while warehousing inventory, not a money-making engine; the locked component here is carry, and carry minus NSE costs is close to nothing.

## 145. Synthetic Long Call
*Bullish, insured · Long vega · net debit*

**The idea (intuition).** Own the index and buy a put against it, and your combined payoff curves exactly like a long call: unlimited upside, a hard floor below. Parity says stock-plus-put equals call-plus-cash, so this protective-put package is a call in disguise.

**When & why to use it.** Use it when you already hold the underlying (or want to) and a known catalyst — earnings, Budget, a Fed meeting — could trigger a sharp drop you want to survive while keeping all the upside. It is the textbook "stay long but sleep at night" trade. It is also a way to express a long-call view when the listed call is mispriced versus the put. Do NOT use it in dead, low-IV drift markets — you pay put premium every cycle for protection you may not need.

**How to build it (₹, Nifty).** Long 1x underlying @ 24000, buy 24000 PE @ 318. Net outlay 24318.3 points including the index; the option cost that matters is the 318-point put premium, about ₹23,850 per lot of insurance.

![Figure: Synthetic Long Call payoff at expiry](figs/strategies/synthetic_long_call.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -318.0 points (~₹23,850 per lot) — capped at the put premium. Breakeven: 24318. Net debit 24318.3 points (index included). Risk:reward undefined (upside unlimited).

**Greeks & behaviour.** Net delta is positive but less than the bare stock because the put offsets some downside delta. Theta is negative (the put decays) and vega is positive — rising IV lifts your insurance. Direction still dominates the P&L.

**Management & exit.** Roll the put up after a rally to lock in gains (a "ratchet"), or let it expire if your bullish view firms up. Exit the whole package if the thesis is done; sell the put back if a vol spike makes it rich and you want to harvest the hedge.

**Risk note.** The cost is the drag: pay for the put too often and it erodes returns in calm markets. IV crush right after the event can shrink the put's value even if you were right to be cautious.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹23,850 | -₹23,850 | -₹23,850 | +₹21,150 | +₹66,150 |

The loss is floored at -₹23,850 across the three lower columns (the put protection), then the position climbs to +₹66,150 at 25,200 — the capped-downside, open-upside shape of a long call.

**Adjustments, variants & timing.** Desks run this protective-put package to expiry when they want the insurance through a known catalyst, then either let the put lapse or ratchet it up after a rally to bank gains; they unwind the hedge early if an IV spike makes the put rich enough to monetise. Put-call parity is what tells the trader whether to build the call synthetically (stock plus put) or just buy the listed call — when the put screens cheap to the call beyond fair carry, the synthetic route is the better fill on NSE. The honest caveat: each protective cycle costs real put premium plus STT and brokerage, and in calm, low-IV drift those frictions quietly exceed the protection's value. This is a risk-management and relative-value construction for someone who already holds the underlying, not a retail income idea; if you find yourself paying for the put every month in a dead tape, the structure is bleeding you, not protecting you.

## 146. Synthetic Short Call
*Bearish income · Short vega · net credit*

**The idea (intuition).** Be short the index and sell a put against it. Your payoff is capped on the downside and bleeds on a rally — the same shape as a short call. You collect premium and have a modest cushion, but the upside is open against you.

**When & why to use it.** This is an income-with-a-bearish-lean position: you want the market to stall or drift down and are happy to pocket the put premium. On NSE it shows up when a desk is short the underlying and writes a put to subsidise carry. Use it in a range-bound-to-soft tape with elevated IV so the put you sell is fat. Do NOT use it ahead of a possible squeeze — the short stock plus short put both lose on a rip higher.

**How to build it (₹, Nifty).** Short 1x underlying @ 24000, sell 24000 PE @ 318. Net credit 24318.3 points including the short-index proceeds; the income that matters is the 318-point put premium, ~₹23,850 per lot collected.

![Figure: Synthetic Short Call payoff at expiry](figs/strategies/synthetic_short_call.png)

**The numbers (modelled at Nifty 24000).** Max profit: 318.0 points (~₹23,850 per lot) — the premium kept if it expires worthless and the short works. Max loss: Undefined — large (a rally through your short index and short put). Breakeven: 24318. Net credit 24318.3 points. Risk:reward undefined.

**Greeks & behaviour.** Net delta negative; theta positive (the sold put decays in your favour); vega negative (falling IV helps). Time and a soft market both pay you, but a melt-up overwhelms everything.

**Management & exit.** Buy back the put at ~50% of the credit, or cap the tail with a long OTM call if momentum turns up. Cover the short and close the put together once the down-move plays out.

**Risk note.** Premium-selling is never free money — most retail F&O traders lose (SEBI studies). The unlimited rally risk is real; size small and stop at a multiple of the credit rather than hoping the put cushion saves you.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹23,850 | +₹23,850 | +₹23,850 | -₹21,150 | -₹66,150 |

The premium of +₹23,850 is kept flat across the lower columns while the market is soft, then turns into a growing loss reaching -₹66,150 at 25,200 as the rally runs through you — a short-call profile.

**Adjustments, variants & timing.** This income-with-a-bearish-lean overlay is carried to collect the put premium and managed by buying the put back near 50% of the credit, or rolling it down if the market drifts your way; the desk unwinds if a squeeze threatens the open upside on the short index. Parity is the screen signal — a put trading fat relative to the call (steep skew, elevated IV) is what makes writing it worthwhile. The blunt truth, repeated across this group: STT falls heaviest on sold options, and brokerage plus the bid-ask on two legs routinely eat the thin edge, so this is a desk financing / relative-value tool, not retail income. SEBI's own studies show most retail F&O participants lose money writing premium like this. Treat the put income as subsidy on a short-inventory carry, size it small, and respect that a melt-up overwhelms the cushion long before the premium ever pays for the tail.

## 147. Synthetic Long Put
*Bearish, insured · Long vega · net credit*

**The idea (intuition).** Short the index and buy a call as a stop. The payoff bends exactly like a long put — big money if the market falls, with a defined, small loss capped by the call if it rallies. It is a protected short.

**When & why to use it.** Use it when you want clean bearish exposure with a hard ceiling on losses — a directional short into a feared event where a gap-up would otherwise be lethal. The long call is your seatbelt above the strike. It also expresses a synthetic-put view when the listed put is dear versus the call. Avoid it as a perpetual hedge in a grinding bull market; the call premium and the short's carry both bleed.

**How to build it (₹, Nifty).** Short 1x underlying @ 24000, buy 24000 CE @ 456. Net credit 23544.1 points net of the short proceeds; the protection cost that matters is the 456-point call, ~₹34,200 per lot.

![Figure: Synthetic Long Put payoff at expiry](figs/strategies/synthetic_long_put.png)

**The numbers (modelled at Nifty 24000).** Max profit: 23543.0 points (index toward zero — the bounded best case). Max loss: -456.0 points (~₹34,200 per lot), capped by the long call. Breakeven: 23544. Net credit 23544.1 points. Risk:reward 51.64 — a striking ratio, but remember the "reward" assumes a collapse to zero.

**Greeks & behaviour.** Net delta negative; theta negative (you own the call); vega positive — a vol spike lifts your call hedge. Direction drives P&L while the call defines the worst case.

**Management & exit.** Roll the call down after a sell-off to lock gains and cut hedge cost, or take the structure off when your downside target prints. If IV pops and the call gets rich, consider monetising it.

**Risk note.** The honest read on that 51.64 risk:reward is that the huge "reward" needs the index near zero; realistic profits are far smaller. The steady cost is the call premium and any negative carry on the short while you wait.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹55,800 | +₹10,800 | -₹34,200 | -₹34,200 | -₹34,200 |

Profit builds as Nifty falls (+₹55,800 at 22,800) while the loss is capped at -₹34,200 across the three upper columns by the long call — the protected-short, long-put shape.

**Adjustments, variants & timing.** A protected short like this is carried toward expiry and managed by rolling the long call down after a sell-off — locking gains and cheapening the hedge — or by monetising the call if a volatility spike makes it rich. The desk unwinds once the downside target prints or the basis lets it short the listed future more cheaply. Put-call parity decides whether to build the synthetic put (short stock plus call) or buy the listed put outright: when the call screens cheap to the put beyond carry, the synthetic is the better fill. The honest note holds — the long-call premium, the carry on the short index, plus STT and brokerage usually exceed the relative-value edge, so this is a professional hedging / financing construction rather than a retail trade. It earns its place when shorting cash is awkward or the listed put is dear; otherwise the frictions on NSE quietly erode the small advantage the synthetic was meant to capture.

## 148. Synthetic Short Put (Covered Call)
*Bullish income · Short vega · net debit*

**The idea (intuition).** Own the index and write a call against it. You keep dividends-style carry and the call premium, you give up upside above the strike, and you carry the full downside of the stock. That payoff is identical to a short put — hence "synthetic short put." It is the familiar covered call.

**When & why to use it.** The classic income overlay: you are long Nifty (via ETF/futures/basket), mildly bullish to neutral, and willing to cap upside to harvest premium each cycle. It shines when IV rank is high so the written call is rich — sell into a post-Budget or post-results IV spike on a name you are happy to hold. Do NOT use it if you expect a big breakout (you cap your gain) or a crash (you eat the full drop).

**How to build it (₹, Nifty).** Long 1x underlying @ 24000, sell 24000 CE @ 456. Net debit 23544.1 points including the index; the income is the 456-point call premium, ~₹34,200 per lot collected.

![Figure: Synthetic Short Put (Covered Call) payoff at expiry](figs/strategies/synthetic_short_put.png)

**The numbers (modelled at Nifty 24000).** Max profit: 456.0 points (~₹34,200 per lot) — the call premium if you are called away at the strike. Max loss: -23543.0 points (the index to zero). Breakeven: 23544. Net debit 23544.1 points. Risk:reward 0.02.

**Greeks & behaviour.** Net delta positive but muted by the short call; theta positive (the written call decays for you); vega negative (an IV drop helps). Income and mild upside pay you; a crash hurts.

**Management & exit.** Buy the call back at ~50% of premium and re-write, or roll up-and-out if the market rallies toward the strike. Take assignment calmly if called away — that is the plan working.

**Risk note.** That 0.02 risk:reward and the huge max loss assume the index collapses to zero; in practice you size small and manage the underlying with a stop. Premium income is not free — a sharp sell-off erases many months of collected calls, and most retail F&O traders lose.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹55,800 | -₹10,800 | +₹34,200 | +₹34,200 | +₹34,200 |

The gain is capped at +₹34,200 once Nifty is at or above the strike, while losses mount to +₹34,200 as the index falls — the covered-call / short-put profile.

**Adjustments, variants & timing.** The covered call is the most retail-accessible structure here, but desks still run it as a financing overlay: carry to expiry to collect the written call, buy it back near 50% of premium and re-write, or roll up-and-out if the index rallies toward the strike. Parity is the entry screen — write when the call is rich (high IV rank), since a fat call is what pays you. Even so, STT on the sold call plus brokerage and the spread shave the income, and a single sharp sell-off erases many months of collected premium; SEBI studies confirm most retail F&O writers lose. Treat it as a yield-enhancement on inventory you genuinely want to hold, not a money tree. The locked piece is the premium minus costs; over many cycles in calm markets the edge is real but modest, and it is always paid for by capping your upside and wearing the full downside of the index.

## 149. Conversion (Arbitrage)
*Locked, rate arbitrage · net debit*

**The idea (intuition).** Combine long stock, a long put and a short call at one strike. The put and short call form a synthetic short that exactly cancels your long stock, leaving a position with no direction at all — a locked box whose only return is the financing built into the option prices. You have, in effect, lent money at the implied rate.

**When & why to use it.** This is a market-maker / arbitrage trade, deployed when the call is overpriced relative to the put (parity is dislocated), letting the desk lock a tiny, near-riskless spread. It is run continuously by professionals managing inventory, not as a directional view. Retail should understand it but rarely trade it: the edge is too thin to survive costs.

**How to build it (₹, Nifty).** Long 1x underlying @ 24000, buy 24000 PE @ 318, sell 24000 CE @ 456. Net debit 23862.3 points. The locked payoff is 138 points either way — that is the carry the structure captures.

![Figure: Conversion (Arbitrage) payoff at expiry](figs/strategies/conversion.png)

**The numbers (modelled at Nifty 24000).** Max profit: 138.0 points. Max loss: 138.0 points — the payoff is flat at this level regardless of where Nifty lands, so there is no real "loss," just a fixed locked outcome. No breakeven (the line is horizontal). Net debit 23862.3 points. Risk:reward 1.0.

**Greeks & behaviour.** Net delta, theta and vega are all essentially zero — fully hedged. The position does not respond to price or volatility; it simply accretes toward its locked value as expiry approaches, like a bond pulling to par.

**Management & exit.** Hold to expiry and let the legs settle, or unwind early if a richer dislocation frees the capital. There is nothing to "manage" directionally; you are warehousing a rate.

**Risk note.** Be honest: that ~138-point "profit" is essentially the risk-free financing rate embedded in the options, and after STT, brokerage and bid-ask it nearly vanishes. Pin risk and assignment on the ITM call at expiry are the practical hazards, plus the cost of carrying the full index outlay.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹10,350 | +₹10,350 | +₹10,350 | +₹10,350 | +₹10,350 |

The P&L is +₹10,350 in every single column — dead flat regardless of where Nifty lands, which is the whole point of a locked conversion arbitrage.

**Adjustments, variants & timing.** This is a market-maker trade carried to expiry to collect the locked financing, or unwound early when a richer dislocation elsewhere frees the capital — there is nothing directional to manage. The opportunity is read straight off put-call parity and the futures basis on the NSE screen: when the 24000 call trades rich to the put (or the future to fair value) by more than carry, the conversion locks the gap. Be blunt about the economics — that flat ~₹10,350 is essentially the risk-free rate embedded in the options, and STT, brokerage across three legs, and the bid-ask you cross usually exceed it. So this is a professional relative-value / financing instrument, not a retail trade. In the same family, box spreads are used as synthetic lending and borrowing, and SEBI has scrutinised brokers who mis-sold such locked structures as "guaranteed return" products — the return is real but tiny, fully exposed to assignment and pin risk on the ITM leg, and rarely survives costs.

## 150. Reversal (Arbitrage)
*Locked, rate arbitrage · net credit*

**The idea (intuition).** The mirror of the conversion: short stock, short put, long call at one strike. The long call plus short put make a synthetic long that cancels your short stock, again leaving a locked, directionless package. Here you have effectively borrowed at the implied rate.

**When & why to use it.** Desks run a reversal when the call is cheap relative to the put — the opposite dislocation to a conversion — capturing the mispricing risk-free. It also lets a market maker carry a short-index hedge while staying delta-neutral. As with the conversion, it is professional inventory management, not a retail income idea; the spread is wafer-thin.

**How to build it (₹, Nifty).** Short 1x underlying @ 24000, sell 24000 PE @ 318, buy 24000 CE @ 456. Net credit 23862.3 points. The locked outcome is -138 points — the financing cost the desk pays (or the parity edge it captures) on the package.

![Figure: Reversal (Arbitrage) payoff at expiry](figs/strategies/reversal.png)

**The numbers (modelled at Nifty 24000).** Max profit: -138.0 points. Max loss: -138.0 points — flat at -138 wherever Nifty settles, a fully locked line. No breakeven. Net credit 23862.3 points. Risk:reward 1.0. The negative locked value reflects that, at these modelled prices, the package settles 138 points against the credit — exactly the mirror of the conversion's +138.

**Greeks & behaviour.** Delta, theta and vega all sit at zero — completely hedged and inert to price and IV. It converges to its locked value as time passes; nothing else moves it.

**Management & exit.** Carry to expiry or unwind when the dislocation that justified it closes. No directional adjustment applies — the legs are self-cancelling by construction.

**Risk note.** The economics are the financing rate minus costs, and on NSE the STT, brokerage and bid-ask typically eat the edge entirely. Watch ITM-call pin/assignment at expiry and the cost of maintaining the short index. This is a relative-value tool, never a money tree.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹10,350 | -₹10,350 | -₹10,350 | -₹10,350 | -₹10,350 |

The P&L is -₹10,350 in every column — a perfectly flat, locked line whatever Nifty does, the mirror of the conversion.

**Adjustments, variants & timing.** A reversal is desk inventory management: carry it to expiry to earn the locked value, or unwind when the dislocation that justified it closes — the self-cancelling legs leave nothing to adjust directionally. Put-call parity and the futures basis are the screen flags: when the 24000 call is cheap to the put (or the future trades under fair value) beyond carry, the reversal captures the gap risk-free while the desk stays delta-neutral on a short-index hedge. The honest economics: the locked ~₹10,350 against you is the financing the package pays, and on NSE the STT, brokerage on three legs and bid-ask typically eat any parity edge entirely. This is a professional relative-value / financing tool, never retail income. It sits in the same family as the box spread used for synthetic borrowing — and SEBI's scrutiny of "guaranteed return" box mis-selling is a reminder that even a fully locked line carries assignment and pin risk on the ITM call at expiry and only makes sense for a desk that nets the costs.

## 151. Box Spread
*Locked synthetic loan · net debit*

**The idea (intuition).** A box is a bull call spread plus a bear put spread on the same two strikes. The two spreads together have no directional payoff — whatever the index does, the box is worth exactly the distance between the strikes at expiry. So you pay a fixed amount today and receive a fixed amount later: a synthetic loan whose interest is the risk-free rate baked into the options.

**When & why to use it.** Treasuries and prop desks use boxes to lend or borrow synthetically at a rate that can beat money-market alternatives, or to capture a parity mispricing. Buying the box (net debit) is lending; the gap between what you pay and the strike width is your interest. Use it as a financing/relative-value instrument, not a punt. Retail should know it exists mainly to recognise a locked structure — and to avoid the infamous "I sold a box and got assigned" disasters.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24300 CE @ 292, buy 24300 PE @ 453, sell 24000 PE @ 318. Net debit 298.3 points. The strikes are 300 apart, so the box is worth ~300 at expiry — you pay 298.3 to collect 300.

![Figure: Box Spread payoff at expiry](figs/strategies/box_spread.png)

**The numbers (modelled at Nifty 24000).** Max profit: 2.0 points. Max loss: 2.0 points — a flat, locked 2-point gain regardless of where Nifty expires. No breakeven (horizontal payoff). Net debit 298.3 points (~₹22,373 per lot of capital deployed). Risk:reward 1.0.

**Greeks & behaviour.** Delta, theta and vega are all zero — the box is volatility- and direction-proof. It simply pulls from 298.3 toward 300 as expiry nears, exactly like a discount bond accreting to face value.

**Management & exit.** Hold to expiry for the locked value, or close early if you need the capital or find a better rate. There is no adjusting a box — it is a financing position you carry.

**Risk note.** Be brutally honest: that 2-point "profit" is just the risk-free rate minus costs, and STT plus brokerage plus the four-leg bid-ask will usually wipe it out on NSE. Early assignment on the American-style legs and execution slippage across four strikes are the real dangers; a mispriced unwind can turn the tiny edge negative.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹150 | +₹150 | +₹150 | +₹150 | +₹150 |

The P&L is a flat +₹150 across all five columns — a fully locked outcome that is direction- and volatility-proof, the signature of a box.

**Adjustments, variants & timing.** A box is pure synthetic financing: buying it (net debit) lends cash at the implied rate, selling it borrows, and the desk simply carries it to expiry to collect the strike width, or unwinds early if it finds a better rate. Put-call parity across the two strikes is the entire signal — if the four legs imply a yield that beats the money-market alternative, the box is worth doing. But be brutally honest: that flat ~₹150 is just the risk-free rate minus costs, and STT, brokerage on four legs, and the four-strike bid-ask will usually wipe it out on NSE. This is the canonical synthetic lending / borrowing instrument for treasuries and prop desks, not a retail trade. Critically, SEBI has scrutinised brokers who mis-sold short boxes as "guaranteed return" products: early assignment on the American-style legs can blow up the supposed lock, and a mispriced four-leg unwind turns the tiny edge negative. Know it to recognise a locked structure — and to avoid the "I sold a box and got assigned" disaster.

## 152. Jelly Roll
*Calendar arbitrage · net debit*

**The idea (intuition).** A jelly roll is the difference between two synthetics at the same strike but different expiries — long a synthetic in one month, short it in another. All the directional pieces cancel, leaving only the value of carry and dividends between the two expiries. It isolates the "cost of time" itself.

**When & why to use it.** This is pure calendar/financing arbitrage for desks: it lets you trade the interest-rate-and-dividend spread between two expiry cycles without any market-direction exposure. Use it when the term structure of implied financing is dislocated — the near and far synthetics imply inconsistent carry. It is among the most professional trades in this group and is almost never a retail position; the payoff is a rounding error per lot.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 24000 CE @ 689, buy 24000 PE @ 318, sell 24000 PE @ 414 (near-month synthetic short versus far-month synthetic long at the 24000 strike). Net debit 136.9 points. The locked value is just 1 point — the isolated carry differential.

![Figure: Jelly Roll payoff at expiry](figs/strategies/jelly_roll.png)

**The numbers (modelled at Nifty 24000).** Max profit: 1.0 point. Max loss: 1.0 point — a flat, locked 1-point outcome whatever Nifty does. No breakeven (horizontal). Net debit 136.9 points. Risk:reward 1.0.

**Greeks & behaviour.** Net delta is zero by construction. Theta and vega are near-zero because the long and short synthetics in the two months largely offset; what little is left reflects the differential decay and the carry/dividend spread between expiries.

**Management & exit.** Roll or unwind around the near-month expiry, then re-establish if the term-structure edge persists. There is no directional management — you are trading the spread between two financing rates.

**Risk note.** The honest truth: a 1-point edge cannot survive STT, brokerage and four legs of bid-ask on NSE. The trade only makes sense for a desk that already holds the inventory and can net the costs. Dividend-assumption error and pin risk at the near expiry are the practical hazards.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹75 | +₹75 | +₹75 | +₹75 | +₹75 |

The P&L is a flat +₹75 in every column — a locked, rounding-error outcome that does not move with Nifty, exactly as a jelly roll should.

**Adjustments, variants & timing.** A jelly roll is carried and then rolled or unwound around the near-month expiry, re-established only if the term-structure edge in implied financing persists — there is no directional management, you are warehousing a spread between two carry rates. The signal comes from put-call parity applied to each expiry: when the near and far synthetics imply inconsistent carry-and-dividend, the roll captures the difference. The honest truth, sharper here than anywhere: a flat ~₹75 edge cannot survive STT, brokerage and four legs of bid-ask on NSE. The trade only makes sense for a desk that already holds the inventory and can net the costs against an existing book. It belongs to the same professional financing family as the box — used to lend or borrow synthetically across expiries — and the same SEBI caution about "guaranteed return" mis-selling applies: dividend-assumption error and pin risk at the near expiry are real, and for retail this is a rounding error dressed up as arbitrage.

## 153. Synthetic Straddle (from Stock)
*Big move · Long vega · net debit*

**The idea (intuition).** Hold the index long but buy two at-the-money puts against it. One put neutralises the stock's downside delta; the second put turns the position net-bearish below the strike while the stock still runs above it. The result is a V-shaped payoff that profits from a big move either way — a long straddle built from stock and puts.

**When & why to use it.** Use it when you expect a large move but are unsure of direction — ahead of a binary event like a Budget, election result, a major earnings cluster, or a macro shock — and IV is still reasonable so the puts are not overpriced. It is a long-volatility / long-gamma bet. Do NOT put it on in a quiet, range-bound tape: theta will grind the double-put premium away while you wait.

**How to build it (₹, Nifty).** Long 1x underlying @ 24000, buy 2x 24000 PE @ 318. Net debit 24636.5 points including the index; the option spend that matters is two puts at 318 = 636 points, about ₹47,700 per lot of premium at risk.

![Figure: Synthetic Straddle (from Stock) payoff at expiry](figs/strategies/synthetic_straddle.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited (the long stock above, the net-short puts below both run). Max loss: -628.0 points (~₹47,100 per lot) at the strike, where both puts expire near-worthless and you have paid full premium. Breakevens: 23363 and 24637 — Nifty must travel roughly ±640 points to pay. Net debit 24636.5 points. Risk:reward undefined.

**Greeks & behaviour.** Net delta is near zero at inception (the two puts offset the stock), so it is delta-neutral and long gamma. Theta is strongly negative — time is the enemy — and vega is positive, so a rise in India VIX helps even before the index moves.

**Management & exit.** Trade the gamma: scalp delta as the index swings, or close for a target after the event resolves. Take it off before the move's energy fades — the worst outcome is the index pinning the strike into expiry. Cut losses if IV collapses post-event.

**Risk note.** The danger is a non-event: the market sits still, IV crushes, and the 628-point premium decays to near zero. Sizing matters — buying two puts doubles your theta bleed, so only deploy it when you genuinely expect a large, timely move.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹42,225 | -₹2,775 | -₹47,775 | -₹2,775 | +₹42,225 |

The table is V-shaped — +₹42,225 at both the 22,800 and 25,200 wings but -₹47,775 at the 24,000 strike — a long-straddle payoff that pays only on a big move either way.

**Adjustments, variants & timing.** Unlike the locked trades around it, this is an active long-gamma position: the desk scalps delta as Nifty swings, banking the volatility, and closes for a target once the event resolves — the worst outcome is the index pinning the strike into expiry, so it is taken off before the move's energy fades. Put-call parity is still the construction check (stock plus two puts versus buying two calls outright tells you the cheaper synthetic), and the futures basis matters because the long index leg carries financing. The honest note: buying two puts doubles the theta bleed, and STT, brokerage and the spread on every roll add up, so size only for a genuinely expected large, timely move. This is a tactical volatility trade rather than a locked-financing one, but the same NSE-cost discipline applies — a non-event with IV crush decays the premium to near zero, and frictions ensure you must be right about both magnitude and timing to come out ahead.

## 154. Reverse Conversion (Skew)
*Locked, skew capture · net credit*

**The idea (intuition).** A reversal built across different strikes to harvest the volatility skew rather than just the financing rate. Short the index, sell a slightly OTM put and buy a slightly OTM call: because OTM puts usually trade richer than OTM calls (the equity skew), the structure locks a small outcome that reflects how steep that skew is.

**When & why to use it.** Desks use it to monetise an unusually steep put skew — when fear has bid up downside protection and the OTM put you sell is fat relative to the OTM call you buy. It is a relative-value, near-locked position taken on a skew view, not a directional one. It is strictly professional; the captured amount is tiny and direction is hedged away.

**How to build it (₹, Nifty).** Short 1x underlying @ 24000, sell 23900 PE @ 282, buy 24100 CE @ 397. Net credit 23884.4 points. The legs straddle the spot 100 points either side, locking a small skew-driven outcome rather than a clean carry number.

![Figure: Reverse Conversion (Skew) payoff at expiry](figs/strategies/reverse_conversion_skew.png)

**The numbers (modelled at Nifty 24000).** Max profit: -16.0 points. Max loss: -216.0 points. Unlike the same-strike reversal, the different strikes leave a small residual payoff band, so the outcome ranges between -16 and -216 across the 23900–24100 zone rather than a single flat line. No listed breakeven. Net credit 23884.4 points. Risk:reward 0.07.

**Greeks & behaviour.** Net delta is close to zero (the synthetic largely offsets the short index), with small residual delta between the strikes. Theta and vega are minor; the position's value is driven by where the index settles relative to the two strikes and by the put-versus-call skew you sold.

**Management & exit.** Carry toward expiry and let the legs resolve, or unwind if the skew normalises and the edge is captured. Watch the 23900–24100 window into expiry, since that is where the residual payoff is decided.

**Risk note.** The numbers are stark: a -16 to -216 modelled outcome means this only works if you put it on when the skew is genuinely rich enough to overcome that range — and STT, brokerage and three legs of bid-ask still bite. Pin and assignment risk near the strikes at expiry are the practical hazards. Like every locked trade here, it is a desk relative-value tool, not retail income.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹1,200 | -₹1,200 | -₹8,700 | -₹16,200 | -₹16,200 |

The P&L is nearly flat but drifts from -₹1,200 in the lower columns to -₹16,200 at the top — a near-locked, skew-driven band rather than a single clean line.

**Adjustments, variants & timing.** A skew-capture reversal is carried toward expiry and managed by watching the 23900-24100 window where the residual payoff is decided, then unwound once the skew normalises and the edge is banked — there is little directional adjustment. Put-call parity across the offset strikes is the signal: the desk puts it on only when the OTM put it sells screens genuinely rich to the OTM call it buys, i.e. when fear has steepened the skew. The honest economics are stark — a -1,200 to -16,200 modelled band means the captured skew must clear that range, and STT, brokerage on three legs and the bid-ask still bite. This is strictly a desk relative-value tool, not retail income, in the same financing / locked family as the box used for synthetic lending and borrowing. SEBI's scrutiny of "guaranteed return" locked-structure mis-selling is the relevant warning: assignment and pin risk near the two strikes at expiry are real, and the edge survives only for a book that nets its costs.

