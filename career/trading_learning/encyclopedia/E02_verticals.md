# Strategy Group 2: Vertical Spreads

A vertical spread buys one option and sells another of the same type and expiry but a different strike — so your view is expressed inside a fixed corridor of strikes rather than on a single naked leg. That one extra leg is what turns options from a lottery ticket into a risk-defined trade: it caps your loss, caps your reward, and cuts the cost (debit spreads) or the margin (credit spreads). The whole family lives on one trade-off — directional debit spreads pay you when you are right about *where* price goes, while credit spreads pay you (via theta) when price simply *doesn't* go against you, and the art is choosing strike width and moneyness to dial probability against payout.

## 11. Bull Call Spread (ATM)
*Moderately bullish · Neutral vega · net debit*

**The idea (intuition).** You want Nifty higher but a naked call bleeds too much premium and theta. So you buy a call and sell a higher call to subsidise it — you keep all the upside between the two strikes and hand away everything above. Think of it as buying a call on instalment, where the short strike pays part of your bill.

**When & why to use it.** Use it when you are moderately bullish over the next one to three weeks and IV is middling-to-high — selling the upper strike claws back inflated premium. It is the bread-and-butter expression of "I think Nifty grinds up 1–2% into expiry." Because it is roughly vega-neutral, you are not betting on IV, which is exactly what you want when India VIX is elevated and a long call alone would get crushed. Avoid it when you expect an explosive breakout (the cap throttles you — prefer a naked call or an OTM/far spread) or when you have no directional edge at all.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24300 CE @ 292. Net debit 164 points, which at lot 75 is 164 × 75 = ₹12,300 per lot — that is also your entire risk. The 300-point gap is your earning corridor.

![Figure: Bull Call Spread (ATM) payoff at expiry](figs/strategies/bull_call_spread_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit 136 points (₹10,200), realised at 24300 or higher. Max loss 164 points (₹12,300), at 24000 or below. Breakeven 24164. Net debit 164. Risk:reward 0.83 — you risk a bit more than you can make, the price of a high-probability ATM structure.

**Greeks & behaviour.** Net delta is positive (long bias), roughly +0.15 to +0.20 per lot of the index at entry. Theta is mildly *negative* while price sits below the short strike — time decay nibbles your long leg faster — but it flips helpful once Nifty pushes above 24300. Vega is close to zero, so an IV swing barely moves you. Direction dominates P&L.

**Management & exit.** A common discipline is to take profit at 60–70% of the 136-point max rather than squeezing the last few points into expiry-week gamma. If Nifty stalls or rolls over, cut at a 50% loss of the debit instead of hoping. You can roll the whole spread up-and-out if the trend is intact but slow.

**Risk note.** Defined risk is your friend — the worst case is the 164-point debit, no margin calls, no assignment surprise. The real danger is time: a flat, choppy tape lets the debit decay even though you were "right" directionally.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹12,300 | -₹12,300 | -₹12,300 | +₹10,200 | +₹10,200 |

Reading across: the spread is pinned to its full -₹12,300 loss anywhere at or below 24,000 and locked to its +₹10,200 max gain once Nifty clears the 24,300 short strike, with the payoff already maxed out by the 24,600 column.

**Adjustments, variants & timing.** When Nifty grinds up and tags the 24,300 short call, the cleanest adjustment is to roll that short leg up-and-out (say to 24,500 of the next week) for an extra debit, widening the corridor while the trend runs; if it stalls, roll the whole spread up and out a week to buy time. If price drifts sideways, convert to a call butterfly by selling a second 24,300 and buying a higher wing, turning a dead directional bet into a theta-positive pin trade. This ATM debit structure suits Nifty monthly and liquid single stocks (Reliance, HDFC Bank) better than Bank Nifty weeklies, where gamma is too violent for a slow-grind thesis. As a debit spread you want a LOW IV-rank window — roughly the bottom third (India VIX 11-13) — so you are not overpaying for the long 24000 call; entering when VIX is calm and a catalyst looms is the A+ setup.

## 12. Bull Call Spread (OTM)
*Bullish breakout · Neutral vega · net debit*

**The idea (intuition).** Same machine as the ATM version, but both strikes sit above spot. You are no longer paying for intrinsic value — you are buying a cheaper, lower-probability bet that Nifty *moves up* to reach your zone. Less cost in, more reward out, but the market has to come to you.

**When & why to use it.** Reach for this when you expect a genuine breakout — a move up *through* a level, not just a drift. Good fits: a bullish catalyst (results, a policy event, a chart breakout above resistance) with one to three weeks to expiry. The lower entry cost means a small account can take a defined-risk swing without committing much capital. Skip it if you only have a mild lean; an OTM spread that never gets in-the-money expires worthless, and "mildly bullish but flat" is its kryptonite.

**How to build it (₹, Nifty).** Buy 24200 CE @ 342, sell 24500 CE @ 204. Net debit 138.1 points ≈ 138 × 75 = ₹10,350 per lot. Notice the debit is lower than the ATM spread even though the corridor is the same 300 points wide — that is the OTM discount.

![Figure: Bull Call Spread (OTM) payoff at expiry](figs/strategies/bull_call_spread_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit 162 points (₹12,150), at 24500+. Max loss 138 points (₹10,350), at 24200 or below. Breakeven 24338 — Nifty must climb about 1.4% just to break even. Net debit 138. Risk:reward 1.17 — now you can make more than you risk, the reward for accepting a lower hit-rate.

**Greeks & behaviour.** Net delta positive but smaller in points-terms at entry than the ATM spread, because both legs start out of the money; delta builds as price rises toward the strikes. Theta is negative until Nifty enters the corridor — out-of-the-money time decay works against you. Vega is near zero. This is a pure "did it move enough, in time?" trade.

**Management & exit.** Because the payoff is back-loaded, partial profit-taking matters less here — but if the spread doubles before expiry, banking it is sensible. Set a mental stop at roughly 50% of the debit; an OTM spread that is not working tends to keep not working. Don't average down on a stalled breakout.

**Risk note.** The honest risk is probability, not size: you can be directionally correct and still lose if the move is too small or too slow. Breakeven well above spot means most of these expire worthless unless the breakout actually arrives — size accordingly.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹10,350 | -₹10,350 | -₹10,350 | +₹12,150 | +₹12,150 |

Reading across: below the 24,200 long strike the spread sits at its full -₹10,350 loss, and from the 24,500 short strike upward it is capped at +₹12,150 — the 24,000 column still shows max loss because Nifty has not yet climbed into the corridor.

**Adjustments, variants & timing.** Because both strikes start above spot, the key adjustment is patience first, then action: if Nifty breaks out and tags 24,500, roll the short call up to 24,800 for more debit and keep riding the breakout; if the move stalls just below 24,200, roll the long leg down toward spot to rescue delta rather than letting it expire worthless. A failed breakout can be salvaged by rolling the entire spread out one week to give the catalyst time. This OTM debit play fits Nifty monthly and event-driven single-stock breakouts (results-season movers) where a clean directional thrust is plausible; it is a poor fit for Bank Nifty weeklies unless you have a same-week trigger. Being a debit spread, enter in a LOW IV-rank window (India VIX in its lower third) so the breakout bet is cheap — buying convexity when vol is rich is the classic OTM-spread trap.

## 13. Bull Call Spread (ITM)
*Bullish, high probability · Neutral vega · net debit*

**The idea (intuition).** Push both strikes below spot and the spread starts life already in the money. You pay a fat debit, but you are paying for *certainty* — as long as Nifty doesn't fall, you collect close to the full width. It behaves almost like a high-delta proxy for being long the index with a defined floor.

**When & why to use it.** Use it when you are confidently bullish or simply want a high-probability "Nifty holds or rises" bet with a known, capped loss. It suits a strong uptrend where you want most of the move with less premium-at-risk than buying the index outright, and far less than a naked call's theta. It is a poor choice when IV is rich and you want vega exposure (this is flat vega), or when you are only mildly bullish — the cost-to-reward is unattractive for a half-hearted view.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655, sell 24100 CE @ 397. Net debit 257.6 points ≈ 258 × 75 = ₹19,350 per lot. The spread is already 300 points in the money at entry, so much of that debit is intrinsic value you simply hold.

![Figure: Bull Call Spread (ITM) payoff at expiry](figs/strategies/bull_call_spread_itm.png)

**The numbers (modelled at Nifty 24000).** Max profit 142 points (₹10,650), at 24100+. Max loss 258 points (₹19,350), only if Nifty drops below 23700. Breakeven 23958 — *below* current spot, so even a small dip still pays. Net debit 258. Risk:reward 0.55 — you risk almost twice the reward, the toll for a high win-rate.

**Greeks & behaviour.** Net delta is the most positive of the bull-call trio at entry, since both legs are ITM and behave nearly one-for-one with the index. Theta is roughly neutral-to-slightly-positive here — the deep structure has little extrinsic value left to decay against you. Vega near zero. This trades almost like a defined-risk long position in Nifty.

**Management & exit.** With breakeven below spot, you can often just hold to expiry and let it settle near max. If Nifty cracks the lower strike, the defined loss caps you — but consider rolling down if the trend genuinely reverses. Take profit if it reaches ~90% of max early; the last few points aren't worth gamma risk.

**Risk note.** The danger is asymmetry: you stake 258 to make 142. One sharp gap below 23700 — an overnight global selloff — and you eat the full debit. High probability is not certainty; the loss, when it comes, is larger than the win.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹19,350 | -₹19,350 | +₹3,150 | +₹10,650 | +₹10,650 |

Reading across: the deep-ITM structure shows its full -₹19,350 loss only on a slide below the 23,700 long strike, is already positive (+₹3,150) at today's 24,000 spot, and caps at +₹10,650 from the 24,100 short strike upward — a high-probability profile that pays even if Nifty merely holds.

**Adjustments, variants & timing.** Since the spread is born in-the-money with breakeven below spot, it needs little babysitting — but if Nifty cracks the 23,700 long strike on a genuine reversal, roll the whole spread down a week to follow the new trend rather than eating the 258-point debit. If the index simply pins near 24,100, hold to expiry to collect near-max; there is no theta to fight. As a near-linear long proxy it suits Nifty monthly and high-priced single stocks where you want index-like exposure with a hard defined floor and no futures mark-to-market. Bank Nifty weeklies are too whippy for this slow-burn structure. Crucially it is vega-flat, so the LOW IV-rank window matters less than for OTM spreads — but you still prefer calm vol (India VIX low) so the intrinsic-heavy debit is not padded with expensive extrinsic value, making entry cheaper and the A+ edge cleaner.

## 14. Bear Put Spread (ATM)
*Moderately bearish · Neutral vega · net debit*

**The idea (intuition).** The mirror image of the bull call spread, for a falling market. Buy an at-the-money put, sell a lower put to cheapen it. You profit as Nifty slides into the corridor between your strikes, with loss capped at the small debit. A defined-risk way to short the index without unlimited downside-to-you on a bounce.

**When & why to use it.** Use it when you are moderately bearish over the next week or three — a pullback, a failed rally, a risk-off tape. It shines when you want downside exposure but selling naked options ties up SPAN margin and carries gap risk; a debit put spread needs only the premium. Because it is roughly vega-flat, it is cleaner than a naked long put when IV is already high and a vol crush would otherwise hurt you. Avoid it if you expect a crash (the cap leaves money on the table — go far-OTM) or if you have no real bearish trigger.

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 23700 PE @ 219. Net debit 99.5 points ≈ 99 × 75 = ₹7,425 per lot — cheap, and that is your whole risk.

![Figure: Bear Put Spread (ATM) payoff at expiry](figs/strategies/bear_put_spread_atm.png)

**The numbers (modelled at Nifty 24000).** Max profit 201 points (₹15,075), at 23700 or below. Max loss 99 points (₹7,425), at 24000 or above. Breakeven 23901. Net debit 99. Risk:reward 2.02 — you can make roughly twice what you risk, an attractive ratio for an ATM structure.

**Greeks & behaviour.** Net delta is negative (bearish), around -0.15 to -0.20 of the index per lot at entry. Theta is mildly negative above the short strike — time decay works against the long put until price falls into the zone — then turns supportive. Vega near zero, so an IV move barely registers. Direction is the driver.

**Management & exit.** Take profit around 60–70% of the 201-point max; bearish moves are often fast and mean-revert, so don't be greedy. If Nifty rallies against you, cut at ~50% of the debit. Roll down-and-out if the downtrend is intact but grinding slowly rather than impulsive.

**Risk note.** Risk is fully defined at 99 points — no assignment drama, no margin spiral. The catch is direction and timing: a flat or rising market quietly decays your debit even when your thesis eventually proves right after expiry.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹15,075 | +₹15,075 | -₹7,425 | -₹7,425 | -₹7,425 |

Reading across: the bearish spread banks its +₹15,075 max gain on any close at or below the 23,700 short strike and sits at its full -₹7,425 loss from 24,000 upward — a clean mirror of the bull call, paying only when Nifty actually falls into the corridor.

**Adjustments, variants & timing.** When Nifty drops and tests the 23,700 short put, roll that leg down-and-out (to 23,500 next week) for additional debit to extend the run, or convert to a put butterfly by selling a second 23,700 and buying a lower wing if you think the slide is exhausting. If the market rallies against you, cut at ~50% of the debit rather than rolling a losing directional bet. This ATM debit put spread fits Nifty monthly and liquid large-cap stocks for a defined-risk short without SPAN margin or gap-against-you risk; Bank Nifty weeklies move too fast for the modest 99-point debit thesis. As a debit structure it favours a LOW IV-rank entry — but note India's well-known put skew means downside puts are perpetually bid, so the genuine A+ window is when VIX is in its lower third AND skew is flat, before fear inflates the long 24000 put.

## 15. Bear Put Spread (OTM)
*Bearish breakdown · Neutral vega · net debit*

**The idea (intuition).** Same bearish machine, but both puts sit below spot. You pay less and stand to make more, but Nifty has to actually fall to your zone — you are buying a breakdown, not a drift. Cheaper ticket, lower odds, fatter payout.

**When & why to use it.** Deploy it when you expect a real break *down* through support — a topping pattern, a global risk-off catalyst, a failed breakout that rolls over hard, with one to three weeks left. The low debit lets a small account take a defined-risk bearish swing. It is the wrong tool for a mild lean or a slow grind lower: if Nifty only dribbles down and never reaches the strikes, the spread expires worthless despite a "correct" direction.

**How to build it (₹, Nifty).** Buy 23800 PE @ 248, sell 23500 PE @ 169. Net debit 79.9 points ≈ 80 × 75 = ₹6,000 per lot. Same 300-point corridor as the ATM version but materially cheaper, because both legs start out of the money.

![Figure: Bear Put Spread (OTM) payoff at expiry](figs/strategies/bear_put_spread_otm.png)

**The numbers (modelled at Nifty 24000).** Max profit 220 points (₹16,500), at 23500 or below. Max loss 80 points (₹6,000), at 23800 or above. Breakeven 23720 — Nifty must drop about 1.2% to break even. Net debit 80. Risk:reward 2.76 — nearly three to one, the reward for accepting lower probability.

**Greeks & behaviour.** Net delta negative but modest in points at entry (both legs OTM), steepening as price falls toward the strikes. Theta negative while above the corridor — OTM extrinsic decay leans against you. Vega near zero. This is a "did it fall far enough, fast enough?" bet.

**Management & exit.** The payoff is back-loaded, so let a working trade run, but bank it if it doubles before expiry. Stop out near 50% of the debit if Nifty refuses to break down. Don't add to a stalled position hoping for a late flush.

**Risk note.** The real risk is probability: breakeven sits well below spot, so most such spreads expire worthless unless the breakdown genuinely materialises. You can be right on direction and still lose on magnitude — size it as the speculative ticket it is.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹16,500 | +₹16,500 | -₹6,000 | -₹6,000 | -₹6,000 |

Reading across: the lower-probability breakdown bet pays its full +₹16,500 only on a real fall to the 23,500 short strike, and sits at its small -₹6,000 loss across the entire upper half of the table — cheap to hold, but it needs the drop to arrive.

**Adjustments, variants & timing.** Because the payoff is back-loaded below spot, manage it as a convex bet: if a sharp leg down tags 23,500, bank it or roll the short put down to 23,300 to keep riding the panic; if Nifty merely drifts and the spread stalls above 23,800, there is little to adjust — stop at ~50% of the small debit and redeploy. A topping pattern that takes time can be rolled out one week. This OTM bearish spread suits Nifty monthly and single-stock breakdowns (a stock losing key support on volume); Bank Nifty weeklies need a same-week catalyst to justify it. As a debit spread you want a LOW IV-rank entry so the breakdown is cheaply owned, but because India's put skew keeps these wings expensive, the A+ window is a calm tape (VIX low) just before a feared event — buying the move before fear is priced in.

## 16. Bear Put Spread (ITM)
*Bearish, high probability · Neutral vega · net debit*

**The idea (intuition).** Lift both puts above spot and the bearish spread is born in the money. You pay a heavier debit for a higher-probability payout — as long as Nifty doesn't rally, you bank most of the width. It is a defined-risk way to lean short with the odds on your side.

**When & why to use it.** Use it when you are confidently bearish, or want a high-probability "Nifty holds down or falls" structure with a capped, known loss. It fits a clear downtrend where you want most of the move with defined risk and no naked-short margin or tail exposure. It is a weak choice for a half-hearted bearish view (the cost-to-reward is poor) or when you specifically want long-vega exposure into a feared selloff — this structure is vega-flat.

**How to build it (₹, Nifty).** Buy 24300 PE @ 453, sell 23900 PE @ 282. Net debit 171 points ≈ 171 × 75 = ₹12,825 per lot. The spread starts in the money, so a chunk of that debit is intrinsic value you carry.

![Figure: Bear Put Spread (ITM) payoff at expiry](figs/strategies/bear_put_spread_itm.png)

**The numbers (modelled at Nifty 24000).** Max profit 229 points (₹17,175), at 23900 or below. Max loss 171 points (₹12,825), only if Nifty climbs above 24300. Breakeven 24129 — *above* current spot, so even a flat-to-slightly-up tape still leaves you in profit. Net debit 171. Risk:reward 1.34 — reward exceeds risk while keeping a high win-rate, an unusually friendly combination.

**Greeks & behaviour.** Net delta is the most negative of the bear-put trio at entry, both legs ITM and tracking the index closely. Theta is roughly neutral — little extrinsic value left to decay against you. Vega near zero. It behaves like a defined-risk short position in Nifty.

**Management & exit.** With breakeven above spot, holding toward expiry to capture near-max is reasonable. If Nifty rips above 24300, the defined loss caps you — consider rolling up if the view changed. Take profit at ~90% of max if it gets there early rather than risking a late bounce.

**Risk note.** The capped loss of 171 points is genuine protection, but a sharp upside gap — a relief rally, a global rebound — through 24300 hands you the full debit. The favourable structure does not remove the need to be right on direction.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹17,175 | +₹17,175 | +₹9,675 | -₹12,825 | -₹12,825 |

Reading across: this high-probability bearish structure books its +₹17,175 max on a close at or below the 23,900 short strike, is still comfortably positive (+₹9,675) at 24,000 because breakeven sits above spot, and only flips to its -₹12,825 loss once Nifty rallies past the 24,300 long strike.

**Adjustments, variants & timing.** Born in-the-money with breakeven above spot, it pays even on a flat tape, so the main adjustment is upside defence: if Nifty rips and threatens 24,300, roll the whole spread up a week to chase the move only if your bearish view genuinely changed — otherwise take the defined loss. A stall near 23,900 is ideal; hold to expiry. As a near-linear short proxy with a hard ceiling, it suits Nifty monthly and large-cap single stocks where you want defined-risk downside without naked-short SPAN or tail exposure; Bank Nifty weeklies are too jumpy. It is vega-flat, so unlike credit spreads it does not need high IV — but you still prefer a calm-to-low VIX so the intrinsic-rich debit is not inflated by extrinsic value, keeping the A+ entry cheap while the favourable above-spot breakeven does the heavy lifting.

## 17. Bull Put Spread (Credit)
*Neutral to bullish · Short vega · net credit*

**The idea (intuition).** Now we flip to selling premium. You sell a put and buy a lower put for protection, pocketing a net credit up front. You win if Nifty simply stays above your short strike — you don't need it to rise, just not to fall. The income classic: get paid for being patient and roughly right.

**When & why to use it.** This is a high-IV trade. Sell it when IV rank is elevated (say India VIX spiking after a selloff or event) so the premium is rich and theta is on your side, with one to two weeks to expiry to harvest fast decay. It suits a neutral-to-bullish view: you think Nifty has found a floor and will hold or drift up. Don't sell it into a falling knife or just before a known binary catalyst (Budget, election count, Fed) where a gap can blow through both strikes; and don't sell when IV is already crushed — the credit won't pay for the tail risk.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 23700 PE @ 219. Net credit 99.5 points ≈ 99 × 75 = ₹7,425 received per lot. The long 23700 put defines your risk and slashes the SPAN margin versus a naked short put.

![Figure: Bull Put Spread (Credit) payoff at expiry](figs/strategies/bull_put_spread.png)

**The numbers (modelled at Nifty 24000).** Max profit 99 points (₹7,425) — the credit kept if Nifty stays at/above 24000. Max loss 201 points (₹15,075), if Nifty falls below 23700. Breakeven 23901. Net credit 99. Risk:reward 0.5 — you risk roughly twice the credit, the standard shape of premium selling: you win often but small, lose seldom but bigger.

**Greeks & behaviour.** Net delta positive (you want price up or flat). Theta is *positive* — this is the whole point, time decay pays you every day Nifty holds. Vega is negative (short vega): falling IV helps, rising IV (usually alongside a drop) hurts. Theta and the short-vega tailwind dominate when price cooperates.

**Management & exit.** Standard discipline: buy it back at ~50% of the max credit rather than holding for the last rupees into expiry-week gamma. Set a stop if the loss reaches roughly 1.5–2× the credit, or if the short strike is breached. Roll the spread down-and-out for a further credit if Nifty tests 24000 but your bullish thesis holds.

**Risk note.** Defined risk caps the disaster at 201 points, but the payoff is lopsided — a gap below 23700 hands you near-max loss in one session, wiping out several winning trades. Most retail F&O sellers lose money (SEBI studies); size small, respect the stop, and never treat the credit as free money.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹15,075 | -₹15,075 | +₹7,425 | +₹7,425 | +₹7,425 |

Reading across: this credit trade keeps its full +₹7,425 anywhere from spot upward, needing only that Nifty hold the 24,000 short strike, and realises its -₹15,075 max loss on a fall below the 23,700 long put — the lopsided shape of premium selling.

**Adjustments, variants & timing.** As a high-IV income trade, the core adjustment when the 24,000 short put is tested is to roll down-and-out for a further credit (sell the 23,800 of the next week) — pushing the strike below the new price while your bullish-floor thesis holds — or convert to an iron condor by adding a bear call spread overhead to collect more premium in a range. If 23,700 is breached, take the defined loss; don't double down into a falling knife. This suits Nifty monthly and Bank Nifty weeklies alike — weeklies actually shine here because theta is brutal in the final days — plus liquid single stocks at support. Being a credit spread it demands a HIGH IV-rank window: sell when India VIX has spiked into its top third (post-selloff, pre-event fear) so the 99-point credit is fat and mean-reverting vol becomes a tailwind. Selling into low IV is the cardinal error.

## 18. Bull Put Spread (Wide)
*Neutral to bullish · Short vega · net credit*

**The idea (intuition).** The same sell-a-put-buy-a-lower-put income trade, but with the strikes spread far apart. A wider gap means you collect a bigger credit — but your protective put is further away, so the potential loss balloons too. More premium, more rope.

**When & why to use it.** Use the wide version when you want a larger absolute credit per lot and have strong conviction Nifty holds above the short strike — and when IV is high enough to justify the bigger exposure. It can make sense when margin efficiency matters less than collecting meaningful premium on a single position. Avoid it if your account is small relative to the now-larger max loss, or near event risk where a deep gap could approach the full 429-point loss.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 23400 PE @ 148. Net credit 170.7 points ≈ 171 × 75 = ₹12,825 received per lot. The 600-point width nearly doubles both the credit and the risk versus the standard bull put spread.

![Figure: Bull Put Spread (Wide) payoff at expiry](figs/strategies/bull_put_spread_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 171 points (₹12,825), kept if Nifty stays at/above 24000. Max loss 429 points (₹32,175), if Nifty falls below 23400. Breakeven 23829. Net credit 171. Risk:reward 0.4 — worse than the narrow version: the wider strikes lift max profit but the risk grows faster, so the ratio sags.

**Greeks & behaviour.** Net delta positive. Theta positive — time decay pays you while Nifty holds. Vega negative; rising IV (typically with a selloff) hurts on two fronts. Because the strikes are far apart, the position behaves more like a lightly-hedged short put: more directional sensitivity than a tight spread.

**Management & exit.** Close at ~50% of the 171-point credit. The larger max loss makes a hard stop essential — exit if loss hits ~1.5× credit or the short strike is tested. Rolling is possible but the wide structure is clumsier to adjust; many traders simply cut and redeploy.

**Risk note.** This is the cautionary member of the family: a 429-point max loss is over 2.5× the credit, and a sharp gap below 23400 realises most of it instantly. The fatter premium is compensation for genuinely fatter tail risk — size for the loss, not the credit, and remember most premium sellers lose over time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹32,175 | -₹32,175 | +₹12,825 | +₹12,825 | +₹12,825 |

Reading across: the wide credit keeps a meatier +₹12,825 from spot upward but the distant 23,400 long put means a breakdown delivers a punishing -₹32,175 — the bigger premium bought with genuinely bigger tail risk.

**Adjustments, variants & timing.** The wide structure is clumsier to adjust, so defence is mostly binary: if the 24,000 short put is tested, roll down-and-out for credit while the floor thesis holds, but the 600-point width makes a clean roll expensive, so many traders simply cut at ~1.5× credit and redeploy. You can also buy back nothing and instead add a far-OTM long put to cap the now-large tail if an event looms. It suits Nifty monthly where the larger absolute credit is the goal and Bank Nifty weeklies only for experienced sellers who respect the 429-point max loss; size it for the loss, not the credit. As a credit spread it needs a HIGH IV-rank window — sell only when India VIX is elevated (top third) so the 171-point credit compensates for the fat tail; the wider the wing, the more you depend on rich IV and mean reversion to make the math work.

## 19. Bear Call Spread (Credit)
*Neutral to bearish · Short vega · net credit*

**The idea (intuition).** The bearish income mirror of the bull put spread. You sell a call and buy a higher call for protection, banking a credit. You win if Nifty stays *below* your short strike — it doesn't have to fall, it just must not rally. Get paid to cap the upside.

**When & why to use it.** A high-IV, neutral-to-bearish trade. Sell it when IV rank is high and you think Nifty is capped — stalling at resistance, after an overbought run, or in a sideways-to-down tape — with one to two weeks to expiry for brisk theta. It pairs naturally with overhead resistance you trust. Don't sell it into a strong uptrend or ahead of a bullish catalyst that could gap price through both strikes; and don't bother when IV is already low and the credit is thin.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 24300 CE @ 292. Net credit 164 points ≈ 164 × 75 = ₹12,300 received per lot. The long 24300 call defines risk and keeps SPAN margin modest versus a naked short call.

![Figure: Bear Call Spread (Credit) payoff at expiry](figs/strategies/bear_call_spread.png)

**The numbers (modelled at Nifty 24000).** Max profit 164 points (₹12,300), kept if Nifty stays at/below 24000. Max loss 136 points (₹10,200), if Nifty rises above 24300. Breakeven 24164. Net credit 164. Risk:reward 1.21 — unusually, the credit exceeds the risk here, because the short call is struck right at spot, making this an aggressive, lower-probability credit trade.

**Greeks & behaviour.** Net delta negative (you want price down or flat). Theta positive — time decay is your engine. Vega negative: falling IV helps, and IV often falls as markets drift up calmly, which also pushes price the wrong way — a tension to watch. Theta dominates when Nifty stays capped.

**Management & exit.** Buy it back at ~50% of the credit. Because the short strike sits at the money, this trade tests quickly — set a stop near 1.5× credit or on a clean break above 24000. Roll up-and-out for a further credit if Nifty grinds higher but you still expect a ceiling.

**Risk note.** Defined risk caps loss at 136 points, but an at-the-money short call means a real chance of being breached — and a sharp rally gap through 24300 delivers the full loss in one move. Selling the upside is not free; rallies can be faster than selloffs.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹12,300 | +₹12,300 | +₹12,300 | -₹10,200 | -₹10,200 |

Reading across: this bearish credit keeps its full +₹12,300 anywhere at or below the 24,000 short call and flips to its -₹10,200 max loss once Nifty pushes above the 24,300 long strike — an aggressive, at-the-money credit trade with only moderate probability.

**Adjustments, variants & timing.** With the short call struck right at spot, this tests fast, so the standard move when Nifty grinds up to 24,000 is to roll the short leg up-and-out (to 24,300 next week) for a further credit, or convert to an iron condor by adding a bull put spread below to widen the profit zone. If price breaks cleanly above 24,000 with momentum, take the defined loss rather than fighting an uptrend — rallies in Nifty can be relentless. It pairs best with trusted overhead resistance on Nifty monthly or Bank Nifty weeklies (weeklies maximise the theta harvest), and with single stocks stalling at a known cap. As a credit spread it requires a HIGH IV-rank window: sell when India VIX sits in its upper third so the 164-point credit is rich. Note that IV often falls as markets drift up calmly, helping vega while price works against you — manage actively.

## 20. Bear Call Spread (Wide)
*Neutral to bearish · Short vega · net credit*

**The idea (intuition).** The bearish credit spread with strikes pulled far apart. A wider corridor means a much bigger credit collected, but the protective call is distant, so the loss potential swells too. More premium in your pocket, more room for pain.

**When & why to use it.** Choose the wide version when you want a substantial credit per lot and are confident Nifty stays capped below the short strike, with IV high enough to reward the larger exposure. It can suit traders who prefer one meatier position over several tight ones. Avoid it when your account can't comfortably absorb the larger max loss, or near bullish event risk where a gap up could push toward the full 311-point loss.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 24600 CE @ 167. Net credit 288.7 points ≈ 289 × 75 = ₹21,675 received per lot. The 600-point width roughly doubles both credit and risk versus the standard bear call spread.

![Figure: Bear Call Spread (Wide) payoff at expiry](figs/strategies/bear_call_spread_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 289 points (₹21,675), kept if Nifty stays at/below 24000. Max loss 311 points (₹23,325), if Nifty rises above 24600. Breakeven 24289. Net credit 289. Risk:reward 0.93 — close to one-to-one, with the larger width lifting both sides; the at-the-money short call keeps probability moderate, not high.

**Greeks & behaviour.** Net delta negative. Theta positive — your daily tailwind while Nifty stays capped. Vega negative. With strikes far apart, the position carries more directional punch than a tight spread, behaving like a lightly-hedged short call.

**Management & exit.** Close at ~50% of the credit. The big max loss demands a firm stop — exit near 1.5× credit or on a decisive break above the at-the-money short strike. Adjusting a wide spread is awkward; many traders just cut and reset rather than roll.

**Risk note.** With a 311-point max loss against a 289-point credit, the risk slightly exceeds the reward and an upside gap through 24600 realises it fast. The generous premium is paid because the tail is genuinely wider — size for the worst case, and recall that the majority of premium sellers lose over time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹21,675 | +₹21,675 | +₹21,675 | -₹23,325 | -₹23,325 |

Reading across: the wide bearish credit banks a generous +₹21,675 across the whole lower half of the table, holding below the 24,000 short call, but a rally above the distant 24,600 long strike inflicts a -₹23,325 loss that slightly exceeds the credit taken in.

**Adjustments, variants & timing.** The 600-point width makes clean rolls costly, so management is mostly stop-driven: if Nifty breaks above the at-the-money 24,000 short call, cut near 1.5× credit or roll the short leg up-and-out only if resistance overhead is still trusted. You can also bolt on a bull put spread below to form a wide iron condor and offset some risk with extra premium. It fits Nifty monthly when you want one meaty position over several tight ones, and Bank Nifty weeklies only for those who can absorb the 311-point tail; size for the worst case, never the credit. As a credit spread it demands a HIGH IV-rank entry — sell only with India VIX in its top third so the 289-point credit justifies the wide exposure. The richer the premium, the more you are relying on elevated IV mean-reverting and the feared rally simply not arriving.

## 21. Bull Call Spread (Far OTM Cheapie)
*Bullish breakout · Neutral vega · net debit*

**The idea (intuition).** A lottery-style debit spread struck well above spot. You pay a tiny premium for a shot at a big payout if Nifty rallies hard into a distant corridor. Low cost, high reward ratio, low odds — a defined-risk way to bet on a sharp upside move.

**When & why to use it.** Use it when you expect an outsized rally — a powerful breakout, a short-squeeze, a momentum thrust into resistance — within the expiry window. It is ideal for expressing a high-conviction "this could run" idea for a few hundred rupees of risk, the kind of asymmetric punt you can take repeatedly. It is wrong as a core position or for a mild lean: far-OTM spreads expire worthless most of the time, so treat them as cheap convexity, not income.

**How to build it (₹, Nifty).** Buy 24300 CE @ 292, sell 24700 CE @ 135. Net debit 157.2 points ≈ 157 × 75 = ₹11,775 per lot. Both legs sit well above spot, so the entire debit is extrinsic — pure time-and-volatility value.

![Figure: Bull Call Spread (Far OTM Cheapie) payoff at expiry](figs/strategies/bull_call_spread_far.png)

**The numbers (modelled at Nifty 24000).** Max profit 243 points (₹18,225), at 24700+. Max loss 157 points (₹11,775), at 24300 or below. Breakeven 24457 — Nifty must climb roughly 1.9% just to break even. Net debit 157. Risk:reward 1.54 — well over one-to-one, the payoff for a genuinely lower-probability bet.

**Greeks & behaviour.** Net delta positive but small at entry (both legs far OTM), building sharply only if price rallies toward the strikes. Theta negative throughout while Nifty stays below the corridor — distant extrinsic value bleeds quickly as expiry nears. Vega near zero net, though each leg is vega-sensitive. This is a "big, fast move or nothing" trade.

**Management & exit.** If the spread doubles or triples on a fast rally, bank it — far-OTM gains evaporate just as fast on a pullback. There is little point in a tight stop on such a cheap, convex position; many traders simply risk the full debit knowing the odds. Don't roll it up chasing a move that has already happened.

**Risk note.** The honest truth is low probability: breakeven is nearly 2% above spot, so most of these expire worthless. Risk only what you can comfortably write off, and treat repeated small losses as the cost of occasionally catching a large move.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹11,775 | -₹11,775 | -₹11,775 | +₹10,725 | +₹18,225 |

Reading across: the far-OTM cheapie sits at its -₹11,775 loss across the lower half, only turns positive between the strikes (+₹10,725 at 24,600), and reaches its +₹18,225 max once Nifty rallies hard past the 24,700 short call — a true big-move-or-nothing payoff.

**Adjustments, variants & timing.** Treat this as cheap convexity, not a managed position: if a fast rally doubles or triples the spread, bank it immediately because far-OTM gains evaporate on the smallest pullback. There is little point in a tight stop on so cheap a structure — many traders simply risk the full debit. The one productive adjustment is to roll up to fresh strikes if a new catalyst appears before expiry, but never chase a move that has already happened. It suits Nifty monthly for expressing a high-conviction melt-up idea and Bank Nifty weeklies as a lottery-style punt into a known event (policy day, results); single stocks work for squeeze setups. As a debit spread it favours a LOW IV-rank window — buy when India VIX is calm so the distant strikes are cheap; entering far-OTM convexity when IV is already high means overpaying for a low-base-rate bet, the quickest way to bleed an account.

## 22. Bear Put Spread (Far OTM)
*Bearish breakdown · Neutral vega · net debit*

**The idea (intuition).** The downside lottery ticket. A cheap put spread struck well below spot that pays handsomely if Nifty drops sharply into the corridor. Small premium out, large reward ratio, low base-rate — defined-risk convexity for a fast fall.

**When & why to use it.** Deploy it when you anticipate a sharp break lower — a panic leg down, a global risk-off shock, a decisive breakdown through support — inside the expiry window. It is the way to own crash-like convexity for a few hundred rupees while keeping risk fully defined (unlike shorting futures). It is the wrong tool for a slow grind down or a mild bearish lean; if the drop is shallow or late, the spread expires worthless.

**How to build it (₹, Nifty).** Buy 23700 PE @ 219, sell 23300 PE @ 129. Net debit 89.8 points ≈ 90 × 75 = ₹6,750 per lot. Both puts are well below spot, so the whole debit is extrinsic value.

![Figure: Bear Put Spread (Far OTM) payoff at expiry](figs/strategies/bear_put_spread_far.png)

**The numbers (modelled at Nifty 24000).** Max profit 310 points (₹23,250), at 23300 or below. Max loss 90 points (₹6,750), at 23700 or above. Breakeven 23610 — Nifty must fall about 1.6% to break even. Net debit 90. Risk:reward 3.45 — the richest ratio in the group, the reward for the lowest probability.

**Greeks & behaviour.** Net delta negative but modest at entry (both legs far OTM), steepening only as price falls toward the strikes. Theta negative while Nifty sits above the corridor — distant time value decays fast. Vega near zero net, though a volatility spike on a selloff can lift the long put en route. A "sharp drop or nothing" bet.

**Management & exit.** If a fast selloff multiplies the spread, take the money — far-OTM downside gains reverse quickly on any bounce. A tight stop matters little on so cheap a position; sizing is the real risk control. Don't chase by rolling lower after the move has already played out.

**Risk note.** Low probability is the headline: breakeven is well under spot and most of these expire worthless. Use it as inexpensive tail insurance or a speculative punt, risking only what you can write off, and accept frequent small losses as the price of occasional big wins.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹23,250 | +₹15,750 | -₹6,750 | -₹6,750 | -₹6,750 |

Reading across: the downside lottery ticket reaches its +₹23,250 max on a deep fall to the 23,300 short strike, is still partly in profit (+₹15,750) at 23,400, and sits at its small -₹6,750 loss across the entire upper half — large reward for a low base-rate crash bet.

**Adjustments, variants & timing.** This is bought as crash convexity, so manage it like one: if a panic leg down multiplies the spread, take the money fast because far-OTM downside gains reverse on any bounce. A tight stop matters little on so cheap a position — sizing is the real control. Don't roll lower chasing a drop that has already played out; instead re-strike fresh only if a new risk-off catalyst emerges. It suits Nifty monthly as inexpensive portfolio tail-insurance and Bank Nifty weeklies as a speculative punt into a feared event; single stocks work for breakdown-through-support setups. As a debit spread it favours a LOW IV-rank entry, yet India's persistent put skew keeps downside wings perpetually bid — so the genuine A+ window is a complacent, low-VIX tape before fear is priced, when you can own crash convexity cheaply. Buying these after VIX has already spiked is overpaying for protection.

## 23. Bull Put Spread (Narrow / High Prob)
*Neutral to bullish · Short vega · net credit*

**The idea (intuition).** A tight, further-OTM put credit spread built for a high win-rate. The short strike sits well below spot and the two strikes are close together, so you collect a small credit but the odds of keeping it are high. Sell a little, win often.

**When & why to use it.** Use it when you want steady, high-probability income and are comfortable with a small reward for a small chance of a larger loss — the classic premium-seller's bread. It works best in a calm-to-firm market with elevated IV, one to two weeks out, where Nifty is unlikely to fall to the short strike. Avoid it when IV is low (the credit is too thin to justify the tail) or before a known catalyst that could gap price through your narrow protective wing.

**How to build it (₹, Nifty).** Sell 23800 PE @ 248, buy 23600 PE @ 192. Net credit 56.2 points ≈ 56 × 75 = ₹4,200 received per lot. The tight 200-point width keeps both the credit and the defined risk small, and the margin light.

![Figure: Bull Put Spread (Narrow / High Prob) payoff at expiry](figs/strategies/bull_put_spread_narrow.png)

**The numbers (modelled at Nifty 24000).** Max profit 56 points (₹4,200), kept if Nifty stays at/above 23800. Max loss 144 points (₹10,800), if Nifty falls below 23600. Breakeven 23744 — comfortably below spot, the source of the high win-rate. Net credit 56. Risk:reward 0.39 — you risk well over twice the credit, the textbook shape of a high-probability income trade.

**Greeks & behaviour.** Net delta slightly positive. Theta positive — the daily decay you are harvesting. Vega negative: calm or falling IV helps, an IV spike (usually on a drop toward your strike) hurts. Theta dominates as long as Nifty stays clear of 23800.

**Management & exit.** With a small credit, the 50% take-profit comes quickly — bank it and redeploy rather than risking gamma late. Discipline on the stop is critical because the loss is nearly 2.6× the credit; exit if the short strike is threatened or loss hits ~1.5× credit. Roll down-and-out only if your bullish floor thesis still holds.

**Risk note.** The seductive trap of high-probability selling: many small wins can be erased by one breach below 23600, since the max loss dwarfs the credit. A gap-down realises it in a session. Most retail F&O sellers lose money (SEBI studies) precisely by over-sizing trades like this — keep size small and honour the stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹10,800 | -₹10,800 | +₹4,200 | +₹4,200 | +₹4,200 |

Reading across: the narrow high-probability put credit keeps its small +₹4,200 across the whole upper half, holding above the 23,800 short strike, and turns to its -₹10,800 max loss only on a fall below the 23,600 long put — many small wins shadowed by one larger loss.

**Adjustments, variants & timing.** With a tight 200-point wing, rolling is cheap and effective: if Nifty slides toward the 23,800 short strike, roll down-and-out for a fresh small credit while the floor thesis holds, or pair it with a narrow bear call spread to form a tight iron condor and double the theta in a range. The small credit means the 50% take-profit comes quickly — bank and redeploy rather than risk late gamma. It is tailor-made for Bank Nifty weeklies and Nifty weekly/monthly where high win-rate income is the goal, and liquid single stocks above support. As a credit spread it lives or dies on the IV-rank window: sell only when India VIX is in its upper third so the thin 56-point credit is worth the 144-point tail. Selling this narrow structure into low IV is the textbook over-sizing trap that SEBI studies show wipes out retail sellers.

## 24. Bear Call Spread (Narrow / High Prob)
*Neutral to bearish · Short vega · net credit*

**The idea (intuition).** The high-probability income trade on the upside. A tight call credit spread struck above spot: you sell a small credit betting Nifty stays below your short strike. Close strikes, modest premium, high odds of keeping it.

**When & why to use it.** Reach for it when you want steady income with a high win-rate and a mildly bearish-to-neutral view, ideally in elevated IV with one to two weeks to expiry. It suits a market capped under resistance that you expect to chop or ease lower. Don't sell it into a strong uptrend or before a bullish catalyst, and skip it when IV is depressed and the thin credit won't compensate for the tail.

**How to build it (₹, Nifty).** Sell 24200 CE @ 342, buy 24400 CE @ 246. Net credit 96.5 points ≈ 97 × 75 = ₹7,275 received per lot. The tight 200-point width keeps risk and margin contained while the short strike sits safely above spot.

![Figure: Bear Call Spread (Narrow / High Prob) payoff at expiry](figs/strategies/bear_call_spread_narrow.png)

**The numbers (modelled at Nifty 24000).** Max profit 97 points (₹7,275), kept if Nifty stays at/below 24200. Max loss 103 points (₹7,725), if Nifty rises above 24400. Breakeven 24297 — above spot, giving room for the trade to work. Net credit 97. Risk:reward 0.93 — close to one-to-one, with the OTM short strike supplying the probability edge rather than the ratio.

**Greeks & behaviour.** Net delta slightly negative. Theta positive — your income engine. Vega negative: calm or falling IV helps, a vol pop hurts. As long as Nifty holds below 24200, theta and the short-vega tailwind carry the P&L.

**Management & exit.** Take profit at ~50% of the credit and redeploy. Although risk and reward are near-balanced here, still set a stop near 1.5× credit or on a clean break above the short strike — an OTM cushion is not a guarantee. Roll up-and-out for further credit if Nifty drifts toward 24200 but you still expect a ceiling.

**Risk note.** Defined risk caps the loss near 103 points, but a sharp upside gap through 24400 hands it to you at once, and a string of small wins can vanish in one breach. Selling the upside is never free; rallies can be abrupt — keep size modest and respect the stop.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹7,275 | +₹7,275 | +₹7,275 | -₹7,725 | -₹7,725 |

Reading across: the narrow high-probability call credit keeps its +₹7,275 across the whole lower half, holding below the 24,200 short strike, and flips to its -₹7,725 max loss only on a rally past the 24,400 long call — a high win-rate offset by a near one-to-one ratio.

**Adjustments, variants & timing.** The tight 200-point wing rolls cleanly: if Nifty drifts up toward the 24,200 short strike, roll up-and-out for a fresh credit while resistance overhead still holds, or add a narrow bull put spread below to build a compact iron condor and harvest theta from both sides of a range. Take profit at ~50% of the credit and redeploy rather than risk expiry-week gamma. It fits Bank Nifty weeklies and Nifty weekly/monthly perfectly for steady high-probability income, plus single stocks capped under resistance. As a credit spread it needs a HIGH IV-rank window: sell when India VIX sits in its upper third so the 97-point credit fairly compensates for the 103-point tail. The OTM cushion supplies the probability edge, not the ratio — so disciplined sizing and an honoured stop, not the cushion, keep you in the game.

## 25. Deep-ITM Bull Call Spread
*Bullish, very high prob · Neutral vega · net debit*

**The idea (intuition).** Push both call strikes well below spot and you get a debit spread that is almost certain to pay near-max — it behaves like a high-delta proxy for being long Nifty, with a hard, defined floor. You pay up for near-certainty: as long as the index doesn't fall meaningfully, you collect most of the width.

**When & why to use it.** Use it when you are strongly bullish or want an index-like long exposure with capped, known downside and minimal theta drag — a cleaner alternative to a naked deep-ITM call or to holding futures with their mark-to-market swings. It is also handy when IV is high and you want directional exposure without paying for vega (this is vega-flat). It is a poor fit for a small reward appetite — you stake a lot to make a little — or when you actually want cheap convexity (use a far-OTM spread instead).

**How to build it (₹, Nifty).** Buy 23500 CE @ 803, sell 23800 CE @ 585. Net debit 218.4 points ≈ 218 × 75 = ₹16,350 per lot. The spread starts deep in the money, so most of that debit is intrinsic value you simply carry to expiry.

![Figure: Deep-ITM Bull Call Spread payoff at expiry](figs/strategies/deep_itm_bull_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 82 points (₹6,150), at 23800+. Max loss 218 points (₹16,350), only if Nifty falls below 23500. Breakeven 23718 — far below spot, so even a sizeable dip still pays. Net debit 218. Risk:reward 0.37 — you risk nearly three times the reward, the toll for very high probability.

**Greeks & behaviour.** Net delta is strongly positive at entry, the closest of any spread here to a one-for-one index long. Theta is roughly neutral — little extrinsic value remains to decay. Vega near zero. The position tracks Nifty almost linearly within the corridor and pins to max once above 23800.

**Management & exit.** With breakeven far below spot, holding to expiry to collect near-max is the usual plan. If Nifty breaks below 23500, the defined loss caps you — consider rolling down only if the trend has genuinely reversed. Bank it early at ~90% of max if offered, since the remaining upside is tiny.

**Risk note.** The asymmetry is stark: 218 at risk to make 82, so one deep gap below 23500 erases the gains of several winners. Very high probability is not certainty — a sharp risk-off shock still delivers the full, larger loss. Use it as a directional proxy, sized for that downside.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹16,350 | -₹16,350 | +₹6,150 | +₹6,150 | +₹6,150 |

Reading across: the deep-ITM proxy pays its full -₹16,350 loss only on a fall below the 23,500 long strike, is already at its +₹6,150 max by today's 24,000 spot, and stays pinned to that cap all the way up — a near-certain payoff bought with a heavy debit.

**Adjustments, variants & timing.** Born deep in-the-money with breakeven far below spot, it behaves like a defined-risk long Nifty and needs almost no management: if the index breaks the 23,500 long strike on a genuine reversal, roll the whole spread down a week to follow the new trend rather than eat the 218-point debit; otherwise hold to expiry and collect near-max. Bank it early at ~90% of max since the remaining upside is tiny. It suits Nifty monthly and high-priced single stocks as a cleaner substitute for a deep-ITM naked call or for holding futures without daily mark-to-market swings; Bank Nifty weeklies are too volatile for this slow, capital-heavy structure. It is vega-flat, so the IV-rank window is secondary — but you still prefer a LOW VIX so the intrinsic-dominated debit carries minimal extrinsic padding, making the directional proxy as cheap and efficient as possible at entry.

## 26. Deep-OTM Bear Call Spread
*Mildly bearish / range · Short vega · net credit*

**The idea (intuition).** A far-OTM call credit spread that sells the upside tail. You collect a credit betting Nifty stays below a distant strike — steady income from the premise that the market simply won't rip higher. Sell the part of the distribution you think won't happen.

**When & why to use it.** Use it for income with a mildly bearish-to-range view, when you expect Nifty to stall or drift and want to monetise an upside that looks unlikely, ideally in elevated IV with one to two weeks to expiry. It pairs well with strong overhead resistance and a calm-to-soft tape. Avoid it in a powering uptrend or ahead of a bullish catalyst, and skip it when IV is low and the credit doesn't pay for the still-real tail.

**How to build it (₹, Nifty).** Sell 24400 CE @ 246, buy 24700 CE @ 135. Net credit 111.2 points ≈ 111 × 75 = ₹8,325 received per lot. The short strike sits well above spot, giving a wide cushion before the trade is threatened.

![Figure: Deep-OTM Bear Call Spread payoff at expiry](figs/strategies/deep_otm_bear_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 111 points (₹8,325), kept if Nifty stays at/below 24400. Max loss 189 points (₹14,175), if Nifty rises above 24700. Breakeven 24511 — a comfortable 2.1% above spot, the source of the high win-rate. Net credit 111. Risk:reward 0.59 — you risk more than the credit, the familiar shape of selling an unlikely tail.

**Greeks & behaviour.** Net delta slightly negative. Theta positive — the daily decay you harvest while Nifty stays capped. Vega negative: calm or falling IV helps, a vol spike hurts. With a wide OTM cushion, theta and short-vega dominate unless a strong rally develops.

**Management & exit.** Take profit at ~50% of the credit and redeploy. The far cushion tempts complacency — still set a stop near 1.5× credit or on a decisive push toward 24400. Roll up-and-out for additional credit if Nifty rallies but you still expect a ceiling overhead.

**Risk note.** Selling the upside tail wins most of the time, which is exactly why one breach above 24700 — a melt-up or a gap on good news — can erase many quiet winners, with max loss well above the credit. This worst case assumes a real rally through your wing; in practice you size small and manage at a multiple of the credit. Most retail F&O sellers lose money (SEBI studies) by treating such trades as free income — they are not.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹8,325 | +₹8,325 | +₹8,325 | -₹6,675 | -₹14,175 |

Reading across: selling the upside tail keeps the full +₹8,325 across the whole lower half below the 24,400 short call, gives back a partial -₹6,675 between the strikes at 24,600, and only realises its -₹14,175 max once Nifty clears the distant 24,700 long call.

**Adjustments, variants & timing.** The wide OTM cushion tempts complacency, so the disciplined move when Nifty rallies toward the 24,400 short strike is to roll up-and-out for additional credit while overhead resistance still holds, or add a deep-OTM bull put spread below to form a wide iron condor and monetise both unlikely tails. Take profit at ~50% of credit and redeploy; do not wait for the last rupees into expiry-week gamma. It suits Nifty monthly and Bank Nifty weeklies for income against trusted resistance, plus range-bound single stocks. As a credit spread it demands a HIGH IV-rank window — sell only when India VIX is in its top third so the 111-point credit pays for the still-real tail; selling a distant wing into low IV collects too little to justify the gap risk, the precise habit that turns high-probability income into a slow account drain.
