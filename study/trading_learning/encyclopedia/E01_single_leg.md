# Strategy Group 1: Single-Leg & Stock Combinations

These are the atoms of options trading — one option bought or sold outright, or used as a leveraged proxy for the index itself. Every multi-leg structure later in this book is assembled from these primitives, so the trade-off here is the cleanest you will meet: buyers pay a fixed premium for defined risk and open-ended (or very large) reward, while sellers collect that premium up front and accept the mirror image — small capped gains against a tail that can be brutal. Master when each side of that bargain is worth taking and the rest of the encyclopedia falls into place.

## 1. Long Call (ATM)
*Strongly bullish · Long vega · net debit*

**The idea (intuition).** Buying an at-the-money call is the purest leveraged bullish bet there is. You pay a fixed premium today for the right to participate in everything Nifty does above your strike, with your downside frozen at what you paid. Think of it as a deposit that controls a much larger position — your loss can never exceed the deposit, but your upside rides the whole rally.

**When & why to use it.** Reach for the ATM call when you have a strong directional view that Nifty moves up meaningfully and soon, and you want leverage without the margin and gap risk of futures. It works best when implied volatility is reasonable (India VIX in the low-to-mid teens) rather than elevated — you are long vega, so buying after a VIX spike means overpaying and risking IV crush. Favour 25-45 days to expiry so theta is manageable. Do NOT use it as a slow, sit-and-wait position; time decay grinds an ATM option hard, and a flat or drifting market bleeds you even if you are eventually right.

**How to build it (₹, Nifty).** Buy the 24000 CE @ 456. That is a net debit of 456 points, or 456 × 75 = ₹34,200 per lot. You pay this in full; there is no SPAN margin beyond the premium for a long option.

![Figure: Long Call (ATM) payoff at expiry](figs/strategies/long_call_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -456 points (₹34,200 per lot), capped at the premium. Breakeven: 24456. Net debit: 456 points. Risk:reward: undefined (reward side is unlimited). You need Nifty above 24456 at expiry just to recover cost — about a 1.9% move.

**Greeks & behaviour.** Net delta is positive (~+0.5 at the money), so you gain as Nifty rises. Theta is negative — every day that passes erodes the option, and decay accelerates into expiry. Vega is positive: rising IV helps you, falling IV hurts. Direction and the speed of the move dominate the P&L.

**Management & exit.** Take profits mechanically — booking at a 50-100% gain on premium stops a winner from round-tripping. If the move stalls, cut at a 40-50% loss of premium rather than hoping. Roll up-and-out if the trend is intact but slow, and always exit before the final expiry-week gamma/theta crunch unless you are deep in the money.

**Risk note.** The honest danger is not catastrophe — your loss is capped — but probability: most long ATM calls expire worthless because they need both direction AND timing. Treat the premium as fully at risk every time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | −34,200 | −34,200 | −34,200 | +10,800 | +55,800 |

The position loses the full premium of ₹34,200 anywhere at or below the 24000 strike, only crosses into profit past breakeven 24,456, and makes +₹55,800 if Nifty reaches 25,200.

**Adjustments, variants & timing.** If Nifty drifts or falls after entry, the cleanest fix is to roll down-and-out: book the bleeding 24000 CE and buy a lower strike (say 23800 CE) in the next monthly to re-centre delta and reset theta — but only if the bullish thesis survives; otherwise just cut at 40-50% of premium. If it runs your way but stalls near breakeven, roll up to a 24200/24400 CE to bank intrinsic and lower capital at risk. For a pure leveraged punt the Nifty/Bank Nifty weekly is tempting, but weekly theta is brutal on an ATM long — keep this monthly (25-45 DTE); use weeklies only around a known catalyst (RBI policy, Budget, monthly expiry pin). Single-stock ATM calls (Reliance, HDFC Bank) work the same but cost more in IV. A+ entry: India VIX in the low-to-mid teens with IV rank below ~30, so you are not overpaying vega ahead of the move. VIX above 20 — pass or switch to a debit spread.

## 2. Long Call (OTM Lottery)
*Aggressively bullish · Long vega · net debit*

**The idea (intuition).** This is the cheap, far-out call — a lottery ticket on a sharp rally. You pay a small premium for a strike well above spot, so it costs little, but it only pays if Nifty travels a long way fast. Low cost, low probability, outsized payoff if you are right.

**When & why to use it.** Buy the OTM call when you expect an explosive up-move — a breakout above resistance, a strong result season, a short-covering squeeze — and you want maximum leverage per rupee. It is also the sensible way to express a low-conviction bullish punt: risk a tiny amount, accept you will usually lose it. Best when IV is low so the lottery ticket is genuinely cheap. Do NOT size it like a core position or buy it repeatedly to "average down" — the base rate of these expiring worthless is high, and stacking them is how accounts bleed.

**How to build it (₹, Nifty).** Buy the 24500 CE @ 139. Net debit 139 points, or 139 × 75 = ₹10,425 per lot — roughly a third the cost of the ATM call.

![Figure: Long Call (OTM Lottery) payoff at expiry](figs/strategies/long_call_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -139 points (₹10,425 per lot). Breakeven: 24639. Net debit: 139 points. Risk:reward: undefined (unlimited upside). Nifty must clear 24639 — about 2.7% — before you make a paisa at expiry.

**Greeks & behaviour.** Net delta is positive but small (~+0.25 to +0.30), so early in the move the option barely responds; it springs to life only as spot approaches the strike. Theta is negative and vicious in percentage terms because the option is mostly time value. Vega is positive. A fast, large move is what makes this trade — slow grinds kill it.

**Management & exit.** Because the cost is small, many traders simply define the premium as the risk and let it ride to a target. If it doubles or triples on a quick pop, bank part of it. Do not hold deep-OTM tickets into the last few sessions hoping for a miracle; theta is total by then.

**Risk note.** Realistically this expires worthless far more often than it pays. The capped loss makes it feel safe, but a steady habit of buying cheap OTM calls is a slow, reliable way to donate premium to sellers.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | −10,425 | −10,425 | −10,425 | −2,925 | +42,075 |

The ticket loses its small ₹10,425 cost across most of the range and only pays off on a large up-move, clearing breakeven near 24,639 and returning +₹42,075 at 25,200.

**Adjustments, variants & timing.** Because the cost is tiny, the default "adjustment" is no adjustment — define the premium as the risk and let it run to a target. If a fast pop doubles or triples the ticket, sell half and ride the rest free; if it sits dead while spot drifts up slowly, don't average down — that habit is how accounts bleed. A productive repair when spot approaches the strike is to sell a further-OTM call against it (turning it into a cheap call spread, e.g. long 24500 / short 24800), locking some convexity before theta accelerates. This structure is genuinely suited to Nifty/Bank Nifty weeklies around an expected breakout or short-covering squeeze, where one big day makes the trade — weekly OTM tickets are cheap and the gamma works for you. Single-stock OTM calls fit event plays (results day). A+ entry: low India VIX (sub-13) and IV rank under ~25, so the lottery ticket is genuinely cheap; high-VIX OTM calls are overpriced — pass.

## 3. Long Call (Deep ITM / Stock Replacement)
*Bullish · Low vega · net debit*

**The idea (intuition).** A deep in-the-money call behaves almost like owning the index itself, but ties up far less capital. Most of what you pay is intrinsic value, so the option tracks Nifty nearly point-for-point — a "stock replacement" that frees up cash and caps your downside at the premium.

**When & why to use it.** Use the deep-ITM call when you want long index exposure with a high delta but don't want to post full futures margin or carry overnight gap risk on cash. It suits a steady, high-conviction uptrend rather than a fast pop, since you are not paying for much time value or leverage. Because vega is low, it is the right bullish vehicle when IV is high — you are not overpaying for volatility the way an ATM buyer would. Avoid it when you specifically want cheap convexity; here you pay up for delta, so a small adverse move costs real rupees.

**How to build it (₹, Nifty).** Buy the 23300 CE @ 1198. Net debit 1198 points, or 1198 × 75 = ₹89,850 per lot. Of that, roughly 700 points is intrinsic (24000 - 23300) and only ~498 is time value.

![Figure: Long Call (Deep ITM / Stock Replacement) payoff at expiry](figs/strategies/long_call_itm.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -1198 points (₹89,850 per lot). Breakeven: 24498. Net debit: 1198 points. Risk:reward: undefined (unlimited upside). Breakeven sits ~2.1% above spot — the cost of the embedded time value.

**Greeks & behaviour.** Net delta is high (~+0.80 to +0.90), so the position moves almost like a long future. Theta is negative but modest in percentage terms because time value is a small slice of the premium. Vega is low — IV shifts barely matter. Direction dominates; this is a delta play, not a volatility play.

**Management & exit.** Manage it like a futures position with a known maximum loss: trail a stop on the underlying, and roll out to a later expiry if the trend persists. Exit if your bullish thesis breaks; do not let a deep-ITM call round-trip a large unrealised gain back to the strike.

**Risk note.** The capital outlay is large, so while the loss is capped at premium, the rupee amount at risk is meaningful — a sharp reversal can cost most of ₹89,850. STT and exercise mechanics on ITM options at expiry also matter; square off rather than letting it auto-exercise where possible.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | −89,850 | −82,350 | −37,350 | +7,650 | +52,650 |

With its ~+0.85 delta the position tracks the index almost point-for-point — deeply red on a drop to 22,800 (−₹89,850) and profitable above breakeven 24,498, reaching +₹52,650 at 25,200.

**Adjustments, variants & timing.** Manage this like a long future with a capped loss. If Nifty falls, you have no margin call, but the rupee bleed is real — trail a stop on the underlying and exit if the uptrend structure breaks rather than hoping the deep-ITM call recovers. If the trend persists and expiry nears, roll out to the next month's deep-ITM strike to keep delta high and refresh the small time-value cushion. To reduce capital at risk after a good run, roll up toward ATM and pocket intrinsic. This is a monthly instrument by nature — weeklies offer too little time value to justify a stock-replacement stance, and weekly deep-ITM strikes are thinly quoted. It translates well to single stocks (a deep-ITM Infosys/Reliance call as a margin-light proxy for the shares). A+ entry: when you want delta but India VIX is elevated (above ~18) — low vega means you avoid the IV-crush that punishes an ATM buyer. Square off before expiry to dodge STT-on-exercise.

## 4. Long Put (ATM)
*Strongly bearish · Long vega · net debit*

**The idea (intuition).** Buying an at-the-money put is the bearish twin of the long call: a fixed-cost ticket that profits as Nifty falls, with loss capped at the premium. It doubles as portfolio insurance — pay a premium, and a market crash pays you back.

**When & why to use it.** Buy the ATM put when you expect a sharp decline — a breakdown of support, a global risk-off, a disappointing event — and want defined-risk downside exposure. As a hedge, it protects a cash or futures long through a known danger window. It works best bought when IV is still low; puts get expensive fast once fear and VIX spike, so insuring after the market has already cracked means overpaying. Avoid it in a calm, grinding-up tape where theta quietly bleeds you.

**How to build it (₹, Nifty).** Buy the 24000 PE @ 318. Net debit 318 points, or 318 × 75 = ₹23,850 per lot. Premium paid in full, no additional margin.

![Figure: Long Put (ATM) payoff at expiry](figs/strategies/long_put_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit: 23681 points (the index can only fall to zero), or 23681 × 75 = ₹17.76 lakh per lot in the theoretical extreme. Max loss: -318 points (₹23,850 per lot). Breakeven: 23682. Net debit: 318 points. Risk:reward: 74.41. The huge ratio simply reflects that the floor is zero — a real, tradeable target is far closer.

**Greeks & behaviour.** Net delta is negative (~-0.5), so you gain as Nifty drops. Theta is negative — time decay works against you. Vega is positive, and notably puts gain extra from the IV expansion that usually accompanies selloffs, so a falling market often helps you twice (price and vol).

**Management & exit.** Book partial profits into a fast drop; fear-driven IV makes puts richest exactly when you should take money off. As a hedge, roll the strike down to lock gains and re-establish protection. Cut losers at ~40-50% of premium if the breakdown fails to materialise.

**Risk note.** The capped loss is honest, but the win rate is the catch — directional puts bought in an uptrending market expire worthless often. The eye-catching max profit assumes Nifty goes to zero, which will not happen; price your target realistically.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +66,150 | +21,150 | −23,850 | −23,850 | −23,850 |

The put makes money as Nifty falls — +₹66,150 at 22,800, profitable down to breakeven 23,682 — and loses its capped ₹23,850 premium anywhere at or above the 24000 strike.

**Adjustments, variants & timing.** When a falling market spikes the put, book partial profit fast — fear-driven IV makes ATM puts richest exactly when you should be taking money off — and roll the strike down (24000 → 23700 → 23400) to lock gains and re-establish cheaper protection. If the breakdown fails and the tape grinds up, cut at 40-50% of premium rather than letting theta and vol-crush bleed you. As portfolio insurance, size the puts to your beta-weighted long delta and refresh monthly. This works as a Nifty/Bank Nifty weekly only across a specific danger window (event, global risk-off) where the move is expected within days; otherwise the monthly (25-45 DTE) is more forgiving on theta. A+ entry: buy when India VIX is still low/complacent (low teens, IV rank under ~30) — puts get expensive the moment fear arrives, so insuring after the market has already cracked means badly overpaying. VIX already above 20: pass or use a put spread to cut vega.

## 5. Long Put (OTM)
*Aggressively bearish · Long vega · net debit*

**The idea (intuition).** The out-of-the-money put is the cheap crash bet — a low-cost ticket that only pays on a real breakdown. Like buying flood insurance on a dry day: inexpensive, usually expires unused, but a genuine deluge pays many times over.

**When & why to use it.** Use the OTM put for aggressive bearish punts or as cheap tail protection on a portfolio when you fear a sharp drop but don't want to pay ATM premium. It shines when IV is low so the ticket is cheap, and when you expect a fast, sizeable fall rather than a slow drift. Do NOT lean on it as a high-probability income or directional trade — it needs a substantial move just to break even, and most of the time it lapses worthless.

**How to build it (₹, Nifty).** Buy the 23500 PE @ 125. Net debit 125 points, or 125 × 75 = ₹9,375 per lot — cheap by design.

![Figure: Long Put (OTM) payoff at expiry](figs/strategies/long_put_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit: 23374 points (₹17.53 lakh per lot in the zero extreme). Max loss: -125 points (₹9,375 per lot). Breakeven: 23375. Net debit: 125 points. Risk:reward: 186.95 — again, that giant number is the zero-floor artefact, not a realistic expectation. Nifty must fall ~2.6% below spot just to reach breakeven.

**Greeks & behaviour.** Net delta is negative but small (~-0.25), so the put is sluggish until spot approaches the strike. Theta is negative and harsh in percentage terms. Vega is positive — and a panic selloff typically detonates IV, which is where these cheap puts make their outsized returns. Speed and size of the drop dominate.

**Management & exit.** Treat the premium as the defined risk and let it work toward a target. If a selloff spikes the put 3-5x, take most of it off — these gains evaporate as fast as they appear when the market stabilises. Don't hold into the last sessions on hope.

**Risk note.** This is a low-probability trade by construction; expect it to expire worthless most of the time. The capped loss is small per trade, but routinely buying OTM puts as "protection" you never collect on is a steady drag on returns.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +43,125 | −1,875 | −9,375 | −9,375 | −9,375 |

The cheap put only pays on a real breakdown — +₹43,125 at 22,800, around breakeven 23,375 by 23,400 — and quietly loses its small ₹9,375 cost anywhere at or above the 23500 strike.

**Adjustments, variants & timing.** Treat the small premium as the defined risk and let it work toward a target; the "adjustment" is mostly discipline. If a selloff spikes the put 3-5x, take most of it off — these gains evaporate as fast as they appear once the market stabilises — and if you still want downside, roll to a fresh lower strike. A useful repair as spot nears the strike is to sell a deeper-OTM put against it, converting to a cheap put spread and recovering some premium before theta bites. This is the natural fit for Nifty/Bank Nifty weeklies as tail protection across a single event (Fed/RBI, expiry, geopolitical headline) — cheap, and one gap-down pays many times over. Single-stock OTM puts hedge concentrated equity holdings. A+ entry: low India VIX (sub-13) and low put-skew, so the crash ticket is genuinely cheap; never chase OTM puts after VIX has already detonated. Don't carry into the last two sessions on hope — theta is total by then.

## 6. Long Put (Deep ITM)
*Bearish · Low vega · net debit*

**The idea (intuition).** A deep in-the-money put gives you near one-for-one short exposure to Nifty with risk capped at the premium. It behaves like a short future, but you can never be margin-called beyond what you paid, and there's no unlimited upside risk against you.

**When & why to use it.** Choose the deep-ITM put when you want a high-delta bearish position — a synthetic short — without posting futures margin or facing unlimited loss on a squeeze. Its low vega makes it the right bearish tool when IV is already elevated (you're not overpaying for volatility), and it suits a steady decline rather than a violent crash. Avoid it if you want cheap convexity on a tail event; you are paying up for delta here, so a rally hurts almost point-for-point.

**How to build it (₹, Nifty).** Buy the 24700 PE @ 722. Net debit 722 points, or 722 × 75 = ₹54,150 per lot. Roughly 700 points (24700 - 24000) is intrinsic, leaving only ~22 points of time value.

![Figure: Long Put (Deep ITM) payoff at expiry](figs/strategies/long_put_itm.png)

**The numbers (modelled at Nifty 24000).** Max profit: 23977 points (₹17.98 lakh per lot, the zero extreme). Max loss: -722 points (₹54,150 per lot). Breakeven: 23978. Net debit: 722 points. Risk:reward: 33.19 — once more, an artefact of the zero floor. Breakeven sits just above spot because the option is already in the money.

**Greeks & behaviour.** Net delta is strongly negative (~-0.85 to -0.90), so it tracks a short future. Theta is negative but small because there's little time value to decay. Vega is low — IV moves barely register. Direction is everything; this is a delta instrument.

**Management & exit.** Manage like a short future with a capped loss: trail a stop on the underlying, roll to a later expiry if the downtrend continues, and book when your target is hit. Square off before expiry rather than relying on auto-exercise.

**Risk note.** The rupee outlay is large, so a reversal can cost most of ₹54,150 even though the loss is "capped." Watch STT and exercise treatment on ITM options at expiry, and mind that deep-ITM index puts can be less liquid — use limit orders.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +88,350 | +43,350 | −1,650 | −46,650 | −54,150 |

This synthetic short profits as Nifty falls — +₹88,350 at 22,800, profitable below breakeven 23,978 — and loses toward its capped ₹54,150 cost as the index rises through the 24700 strike.

**Adjustments, variants & timing.** Run it like a short future with a known floor on losses. If Nifty rallies against you, there is no squeeze risk, but the rupee loss mounts near point-for-point — trail a stop on the underlying and exit if the downtrend structure fails rather than nursing the position. If the decline persists into expiry, roll to the next month's deep-ITM put to keep the high delta and refresh the thin time value. After a strong down-move, roll the strike toward ATM to bank intrinsic and cut capital at risk. This is a monthly tool — weekly deep-ITM index puts carry too little time value and trade with wide spreads; use limit orders given thinner liquidity. It maps cleanly to a single-stock synthetic short when you want bearish exposure without borrowing/SLB. A+ entry: when your view is bearish but India VIX is already high (above ~18) — the low vega means you are not overpaying for volatility the way an ATM put buyer would. Square off before expiry to avoid STT-on-exercise on the ITM leg.

## 7. Short Call (Naked)
*Bearish / neutral · Short vega · net credit*

**The idea (intuition).** Selling a call with no underlying is a bet that Nifty stays below your strike. You collect the premium up front and keep it if the option expires worthless — but you have handed someone else unlimited upside, so a runaway rally is your nightmare. This is the textbook example of picking up rupees in front of a steamroller.

**When & why to use it.** Sell a naked call only when you are confident the index will stay capped — at strong resistance, in a fading rally, or after a blow-off top — and ideally when IV is high (India VIX elevated, IV rank > 70) so the premium is rich and likely to decay. Short tenor concentrates theta in your favour. Do NOT sell naked calls into an uptrend, before a known bullish catalyst, or without a stop — the unlimited risk is real and a gap-up can be ruinous. Most retail traders should prefer a defined-risk bear call spread instead.

**How to build it (₹, Nifty).** Sell the 24300 CE @ 292. Net credit 292 points, or 292 × 75 = ₹21,900 received per lot. This requires SPAN + exposure margin (often ₹1-1.5 lakh+ per lot), not just the premium.

![Figure: Short Call (Naked) payoff at expiry](figs/strategies/short_call_naked.png)

**The numbers (modelled at Nifty 24000).** Max profit: 292 points (₹21,900 per lot) — the credit, full stop. Max loss: Undefined — large (unlimited as Nifty rises). Breakeven: 24592. Net credit: 292 points. Risk:reward: undefined (loss side is unlimited). You keep the full credit only if Nifty is below 24300 at expiry.

**Greeks & behaviour.** Net delta is negative (you want the market down or flat). Theta is positive — time decay is your engine, and you profit as the option bleeds. Vega is negative — falling IV helps, an IV spike hurts. Theta and a quiet tape carry the P&L.

**Management & exit.** Close at ~50% of the credit captured rather than squeezing the last rupees. Set a hard stop — commonly buy back at 2x the credit received (a ~292-point loss) or if Nifty breaches the strike. Roll up-and-out if tested but your view holds. Exit before expiry-week gamma turns a small move into a large loss.

**Risk note.** This is the most dangerous single-leg trade in the book: losses are theoretically unlimited and an overnight gap-up gives you no chance to manage. Never sell naked calls without strict sizing and a stop; the rich win rate masks a fat, account-ending tail.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +21,900 | +21,900 | +21,900 | −600 | −45,600 |

You keep the full ₹21,900 credit anywhere at or below the 24300 strike, slip past breakeven 24,592, and face a large, open-ended loss as Nifty rallies — already −₹45,600 by 25,200 and climbing.

**Adjustments, variants & timing.** The non-negotiable rule is a stop: buy the call back at ~2x the credit (a ~292-point loss) or when Nifty breaches the strike — the unlimited tail is real and an overnight gap-up gives you no chance to manage. If tested but your cap-resistance view holds, roll up-and-out to a higher strike in the next expiry, ideally for a net credit, to widen the cushion. Most retail traders should convert this to a defined-risk bear call spread (sell 24300, buy 24600) so the disaster scenario is bounded. Theta favours short tenor, making Nifty/Bank Nifty weeklies attractive for the rapid decay — but weekly gamma near expiry can turn a small move into a fast loss, so size down and respect the strike. A+ entry: sell into a fading rally or firm resistance when India VIX is elevated and IV rank above ~70, so the premium is rich and likely to decay. Never sell naked calls into an uptrend or ahead of a bullish catalyst — pass.

## 8. Short Put (Naked / Cash-Secured)
*Bullish / neutral · Short vega · net credit*

**The idea (intuition).** Selling a put is getting paid to agree to buy Nifty lower. If the index stays above your strike you simply keep the premium; if it falls through, you're effectively "assigned" the index at the strike, cushioned by the credit you took in. It is the income workhorse of bullish-to-neutral traders.

**When & why to use it.** Sell the cash-secured put when you are mildly bullish or neutral and happy to "own" the index at a discount, ideally after a selloff has pumped IV (India VIX high, put skew rich) so the premium is fat. High IV rank and 20-45 DTE are the classic setup. Do NOT sell puts into a falling knife or ahead of a major risk event without protection — the downside, while bounded, is very large, and a crash will hurt badly. Size so that being assigned the full index value is something your account can actually absorb.

**How to build it (₹, Nifty).** Sell the 23700 PE @ 219. Net credit 219 points, or 219 × 75 = ₹16,425 received per lot. Requires SPAN margin; "cash-secured" means setting aside enough to buy the index at 23700 if assigned.

![Figure: Short Put (Naked / Cash-Secured) payoff at expiry](figs/strategies/short_put_naked.png)

**The numbers (modelled at Nifty 24000).** Max profit: 219 points (₹16,425 per lot) — the credit. Max loss: -23480 points (₹17.61 lakh per lot). Breakeven: 23481. Net credit: 219 points. Risk:reward: 0.01. *That worst case assumes the index collapses all the way to zero; in practice you size small and manage or stop out at a multiple of the credit long before then.* You keep the full credit if Nifty holds above 23700.

**Greeks & behaviour.** Net delta is positive (you want the market up or flat). Theta is positive — decay pays you. Vega is negative — falling IV (the post-selloff "vol crush") helps, a fresh fear spike hurts. Theta plus a stable-or-rising market drives the gains.

**Management & exit.** Book at ~50% of max credit. Stop or roll down-and-out if the put goes in the money or you reach a loss of ~2x the credit. Many traders treat assignment as acceptable and transition into a covered call (the "wheel"). Exit before expiry-week gamma if the strike is being tested.

**Risk note.** Premium selling is not free money — the tail is large and SEBI studies show most retail F&O traders lose. A gap-down through your strike can wipe out many months of collected credits in a single session; respect the position size.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | −51,075 | −6,075 | +16,425 | +16,425 | +16,425 |

You keep the full ₹16,425 credit anywhere at or above the 23700 strike, cross breakeven 23,481, and take a large loss as Nifty falls — already −₹51,075 by 22,800.

**Adjustments, variants & timing.** Book at ~50% of max credit rather than squeezing the last rupees. If the put goes in the money or you reach ~2x the credit in loss, stop or roll down-and-out to a lower strike in the next expiry for a net credit, buying time and a wider cushion. Many traders accept assignment and transition into a covered call — the classic "wheel" — which only makes sense if your account can genuinely absorb owning the full index value at the strike. To bound the tail, convert to a bull put spread (sell 23700, buy 23400). Theta and rapid decay make Nifty/Bank Nifty weeklies popular for income, but weekly gamma is unforgiving near expiry, so size down. A+ entry: sell after a selloff has pumped IV (India VIX high, IV rank above ~70, put skew rich) when you are mildly bullish or neutral and happy to own the index at a discount; 20-45 DTE is the classic window. Never sell into a falling knife or ahead of a major risk event without protection — pass.

## 9. Long LEAPS Call
*Long-term bullish · Long vega · net debit*

**The idea (intuition).** A LEAPS call is a long-dated call — months out — used to ride a multi-month uptrend. The long horizon slows the theta bleed to a trickle, so you can be patient and let a slow trend mature without daily decay grinding you down. It's a leveraged, defined-risk stand-in for buying and holding the index.

**When & why to use it.** Buy a LEAPS call when you have a structural bullish thesis — a multi-quarter rally, a re-rating story — and want leverage with capped risk and minimal time pressure. It's best entered when IV is low, because you are very long vega over a long horizon; buying long-dated calls when volatility is cheap is doubly rewarding if both price and IV rise. Note that index LEAPS liquidity on NSE is thinner than the near months, so use limits. Avoid it for short-term punts — you overpay for time you may not need.

**How to build it (₹, Nifty).** Buy the long-dated 24000 CE @ 2263. Net debit 2263 points, or 2263 × 75 = ₹1,69,725 per lot. Large outlay, but it's the full risk and there's no margin call.

![Figure: Long LEAPS Call payoff at expiry](figs/strategies/long_leaps_call.png)

**The numbers (modelled at Nifty 24000).** Max profit: Unlimited. Max loss: -2263 points (₹1,69,725 per lot). Breakeven: 26263. Net debit: 2263 points. Risk:reward: undefined (unlimited upside). Breakeven sits ~9.4% above spot — the price of buying so much time value.

**Greeks & behaviour.** Net delta is positive (~+0.55-0.60 and rising as spot climbs). Theta is negative but gentle per day given the long life. Vega is large and positive — this is genuinely a volatility-sensitive position; a rise in long-term IV can mark it up well before expiry. Direction over months plus IV drive the P&L.

**Management & exit.** Manage by thesis and time, not daily noise. Take profits as the trend matures or roll the strike up to harvest gains and reduce capital at risk. As expiry approaches, theta accelerates — don't let a LEAPS decay into the final weeks; roll to a new long-dated strike or close.

**Risk note.** The rupee outlay is the largest in this group, so a flat or falling market over the holding period can cost most of ₹1,69,725. Long vega cuts both ways: a sustained IV decline erodes the option even if Nifty is roughly flat.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | −169,725 | −169,725 | −169,725 | −124,725 | −79,725 |

These are at-expiry values of the long-dated call: the position loses its large ₹1,69,725 premium at or below the 24000 strike and recovers steadily as Nifty climbs, still −₹79,725 even at 25,200 because breakeven sits far up at 26,263.

**Adjustments, variants & timing.** Manage by thesis and time, not daily noise. If the market falls early, the gentle theta buys patience — but cut if the structural bullish story breaks rather than riding a large rupee loss. As the trend matures, roll the strike up (24000 → 24500 → 25000) in the same long-dated series to harvest gains and shrink capital at risk; as expiry approaches and theta finally accelerates, roll forward to a new long-dated strike rather than letting it decay into the final weeks. This is inherently a monthly/quarterly position — it has no weekly analogue, and NSE long-dated index liquidity is thin, so always use limit orders. Single-stock LEAPS are largely unavailable on NSE, so Nifty is the practical vehicle. A+ entry: a structural multi-quarter bullish thesis bought when India VIX is low and IV rank under ~25 — you are very long vega over a long horizon, so cheap volatility is doubly rewarding if both price and IV rise. High-VIX entry overpays for vega — pass.

## 10. Long LEAPS Put
*Long-term bearish / hedge · Long vega · net debit*

**The idea (intuition).** A long-dated put is strategic downside protection or a patient bearish position. Bought months out, it's standing insurance against a major decline, with slow theta so the cost of "carrying" the hedge per day is modest. You pay once and stay protected through a long, uncertain window.

**When & why to use it.** Use the LEAPS put to hedge a sizeable long portfolio against a structural downturn, or to express a slow-burn bearish macro view. It's best bought when IV is low and complacent — insurance is cheapest when no one wants it — and when you genuinely fear a multi-month drawdown rather than a one-day shock. Being long vega over a long horizon means an IV expansion alone can profit the position. Don't buy it as a short-term crash bet; a near-dated OTM put is far cheaper for that. Mind that long-dated index puts can be illiquid — trade with limits.

**How to build it (₹, Nifty).** Buy the long-dated 24000 PE @ 641. Net debit 641 points, or 641 × 75 = ₹48,075 per lot. Paid in full; this is your maximum risk.

![Figure: Long LEAPS Put payoff at expiry](figs/strategies/long_leaps_put.png)

**The numbers (modelled at Nifty 24000).** Max profit: 23358 points (₹17.52 lakh per lot in the zero extreme). Max loss: -641 points (₹48,075 per lot). Breakeven: 23359. Net debit: 641 points. Risk:reward: 36.44 — the large ratio is the zero-floor artefact, not a target. Breakeven sits ~2.7% below spot.

**Greeks & behaviour.** Net delta is negative (~-0.40), so it gains as Nifty falls. Theta is negative but slow given the long life. Vega is large and positive — a key feature: in a risk-off episode, surging long-term IV can mark the put up sharply even before price falls far. Direction over months and IV dominate.

**Management & exit.** As a hedge, roll the strike down after a decline to bank gains and re-set protection, or monetise the vega spike in a panic and re-establish cheaper later. As a directional trade, manage by thesis. Avoid carrying it into the last weeks where theta bites; roll to a fresh long-dated strike.

**Risk note.** If the market drifts up or sideways, the hedge is a sunk cost — you can lose most of ₹48,075 while the portfolio it protects does fine, which is the price of insurance. Long vega means a calm, falling-IV market erodes the put even without an up-move.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +41,925 | −3,075 | −48,075 | −48,075 | −48,075 |

These are at-expiry values of the long-dated put: it pays as Nifty falls — +₹41,925 at 22,800, around breakeven 23,359 by 23,400 — and loses its full ₹48,075 premium anywhere at or above the 24000 strike.

**Adjustments, variants & timing.** Manage by thesis and horizon. As a hedge, roll the strike down after a decline (24000 → 23500 → 23000) to bank gains and re-set protection, or monetise a vega spike during a panic and re-establish cheaper once IV calms. The slow theta means you can be patient, but if the market grinds up the hedge is a sunk cost — accept it as the price of insurance rather than rolling endlessly. Avoid carrying into the final weeks where theta finally bites; roll forward to a fresh long-dated strike. This is a monthly/quarterly instrument with no weekly analogue; for a short, sharp crash bet a near-dated OTM put is far cheaper. NSE long-dated index puts can be illiquid, so trade with limit orders, and single-stock LEAPS are largely unavailable here — Nifty is the practical vehicle. A+ entry: buy when IV is low and complacent (India VIX low teens, IV rank under ~25) and you genuinely fear a multi-month drawdown — being long vega over a long horizon, an IV expansion alone can profit the position. Buying after fear has already spiked overpays — pass.
