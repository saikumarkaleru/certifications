# Strategy Group 3: Straddles, Strangles & Volatility

This family is the purest expression of a view on *movement* rather than *direction*. Every structure here is built from a call and a put together — when you buy both you are long volatility (you want a big move and you pay theta for the privilege); when you sell both you are short volatility (you want the index to sit still and you collect theta while carrying tail risk). The single decision that unites the whole group is your read on India VIX and realised movement: is the option market over-pricing the coming move (sell premium) or under-pricing it (buy premium)? Everything below is a variation on that one trade-off — strike width, expiry distance, directional lean, and how brutally an IV crush or a gap can punish the wrong side.

## 27. Long Straddle
*Big move, direction unknown · Long vega · net debit*

**The idea (intuition).** Buy the call and the put at the same strike and you have bought a bet that "something big happens," up or down, you don't care which. It is the trade you put on when you are certain a move is coming but genuinely cannot call the direction — think of it as buying an insurance policy that pays whichever way the building falls.

**When & why to use it.** Use it ahead of a known catalyst when implied vol is still cheap — before a budget, an RBI policy, a large-cap earnings print, or an election count — and you expect realised movement to exceed what the premium implies. The killer condition is IV rank: enter when India VIX is *low* and likely to rise, because you are long vega. Do NOT buy a straddle into an already-elevated VIX or the night before results when premiums are fat — the post-event IV crush will gut you even if the index moves, because the vol you paid for evaporates at the open.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456 and buy 24000 PE @ 318 for a net debit of 774.2 points. At lot 75 that is about ₹58,065 of premium at risk per lot — real money, all of it bleeding to theta every day you wait.

![Figure: Long Straddle payoff at expiry](figs/strategies/long_straddle.png)

**The numbers (modelled at Nifty 24000).** Max profit is Unlimited (the call leg has no ceiling). Max loss is 766.0 points (about ₹57,450 per lot) if Nifty pins exactly 24000 at expiry. Breakevens are 23226 and 24774 — Nifty must travel roughly 774 points either way just to get you flat. Net debit 774.2 points; risk:reward is undefined because the upside is open-ended.

**Greeks & behaviour.** Net delta is near zero at inception (the call and put deltas offset), so it is direction-neutral at the start but becomes directional fast as the index moves — positive gamma is the whole point. Theta is firmly negative: time is your enemy. Vega is positive and large; a rise in India VIX helps you even before the index budges. P&L is dominated by gamma and vega in a fight against theta.

**Management & exit.** Have a plan before you enter: if the catalyst delivers, take profit into the spike — close into strength rather than holding for "more." A common discipline is to exit at a fixed gain (say the position doubles) or cut at a partial loss if the move doesn't materialise within a day or two. Never carry a long straddle into expiry week hoping; theta accelerates and the breakevens widen against you.

**Risk note.** The honest danger is the IV crush: you can be *right* on the move and still lose if you overpaid for vol and it collapses post-event. The full debit is at risk, and a quiet, range-bound tape will quietly bleed the whole 774 points to zero.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +31,950 | -13,050 | -58,050 | -13,050 | +31,950 |

A 5% move either way (to 22,800 or 25,200) hands you about +₹31,950, while a pin at 24,000 realises the full -₹58,050 loss — the classic V-shaped long-vol payoff.

**Adjustments, variants & timing.** When the tape moves and one leg swells, leg out the winner (sell the profitable call or put) and let the cheap remaining leg run, or roll the untested leg toward the money to re-center delta. To blunt theta you can sell OTM wings, converting it into a reverse iron fly that caps cost. Gamma-scalp by selling Nifty futures against a rallying call (or buying futures against a falling put) to bank intraday swings. The structure fits Bank Nifty weeklies, where high gamma makes scalping lucrative, but theta there is brutal — a Nifty monthly gives the thesis more time to play out. Timing: buy when India VIX and IV rank are low (sub-12 VIX, bottom-quartile rank) and a catalyst looms; never pay up the night before results when IV is fat — the post-event crush guts you even on a correct move.

## 28. Short Straddle
*Range-bound / falling IV · Short vega · net credit*

**The idea (intuition).** Sell the call and the put at the same strike and you are the insurance company — you pocket the premium and win as long as the index does *not* move much. It is the highest-octane premium-selling trade in the book: maximum credit, maximum theta, and maximum tail risk.

**When & why to use it.** Deploy it when you expect a dead, range-bound market and, crucially, when IV is rich and likely to fall — sell *after* an event-day VIX spike, not before. The classic NSE setup is selling the ATM straddle the morning after results or a budget, harvesting the IV crush that punishes long-vol holders. Do NOT sell a naked straddle ahead of an unknown catalyst, into a trending market, or when VIX is already low (you are collecting little for unlimited risk).

**How to build it (₹, Nifty).** Sell 24000 CE @ 456 and sell 24000 PE @ 318 for a net credit of 774.2 points — about ₹58,065 received per lot. That cash is yours to keep only if Nifty behaves.

![Figure: Short Straddle payoff at expiry](figs/strategies/short_straddle.png)

**The numbers (modelled at Nifty 24000).** Max profit is 766.0 points (~₹57,450 per lot), earned if Nifty expires pinned at 24000. Max loss is Undefined — large: theoretically unlimited as the index runs away in either direction. Breakevens are 23226 and 24774 — you keep some profit anywhere inside that ~1,550-point band. Net credit 774.2 points; risk:reward is undefined because the loss side is open-ended.

**Greeks & behaviour.** Net delta starts near zero but turns sharply against you as the index moves (short gamma — the worst feature). Theta is strongly positive: time decay is your paycheck. Vega is negative; falling India VIX is pure profit, rising VIX hurts even before the index moves. The trade lives and dies on negative gamma versus positive theta.

**Management & exit.** Discipline is everything. Take profit early — close at roughly 50% of the credit captured rather than squeezing the last points. Set a hard stop at a multiple of the credit (e.g., exit if the loss reaches 1.5–2x the premium received) and roll the tested side out or up/down to defend. Never hold a short straddle into expiry-week gamma, where a small move produces a violent P&L swing.

**Risk note.** This is the most dangerous structure in the chapter. The "Undefined — large" max loss is not a rounding artefact — a gap-up or gap-down (an SGX-led open, a geopolitical shock) can blow past your breakeven before you can act. Size small, define a stop, and respect that most retail F&O traders selling premium lose money (per SEBI studies). Never treat the credit as free money.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -31,950 | +13,050 | +58,050 | +13,050 | -31,950 |

A pin at 24,000 banks the full +₹58,050, but the table only spans ±5% — beyond 25,200 or 22,800 the loss keeps growing without limit, far past the -₹31,950 shown.

**Adjustments, variants & timing.** When one side is tested, roll the untested leg in to collect more credit, or roll the tested strike out and away; if the move persists, go inverted (roll the call below the put) to widen the band. The cleanest defence is to buy OTM wings, converting it to an iron fly with defined risk, or to delta-hedge with Nifty futures to flatten directional exposure. Bank Nifty weeklies offer rich premium but vicious gamma into Thursday's expiry — size tiny; a Nifty monthly or 45-DTE position is far calmer. Timing: sell only when India VIX is elevated and IV rank is high (above the 70th percentile), ideally into the post-event IV crush the morning after a budget or RBI policy. Avoid selling ahead of unknown catalysts or when VIX is already low — you would be collecting little for unlimited risk.

## 29. Long Strangle
*Big move, cheaper than straddle · Long vega · net debit*

**The idea (intuition).** Same long-volatility bet as the straddle, but you buy out-of-the-money strikes instead of ATM — a cheaper call above and a cheaper put below. You pay less, so you risk less, but the index has to move *further* before you profit.

**When & why to use it.** Use it when you expect a large move and want the long-vol exposure at a lower cash outlay than a straddle — ideal when you are confident the move will be *big* (not just moderate). Same IV logic: enter when India VIX is low and rising, ahead of a catalyst. Do NOT use it for small expected moves; OTM strikes need a meaningful travel to pay, and a modest wiggle leaves both legs worthless.

**How to build it (₹, Nifty).** Buy 24400 CE @ 246 and buy 23600 PE @ 192 for a net debit of 438.1 points — about ₹32,858 per lot, noticeably cheaper than the 774-point ATM straddle.

![Figure: Long Strangle payoff at expiry](figs/strategies/long_strangle.png)

**The numbers (modelled at Nifty 24000).** Max profit is Unlimited. Max loss is 438.0 points (~₹32,850 per lot) — the full debit, lost if Nifty expires anywhere between the two strikes (23600–24400). Breakevens are 23162 and 24838, slightly wider than the straddle's. Net debit 438.1 points; risk:reward undefined (open-ended upside).

**Greeks & behaviour.** Net delta near zero at inception; positive gamma kicks in once the index moves past either strike. Theta negative — time decay erodes both OTM legs steadily. Vega positive and large; a VIX pop lifts the whole position. The cheaper entry is bought with a wider dead-zone, so gamma needs a bigger move to overcome theta.

**Management & exit.** Take profit into the move — if the catalyst delivers, close the winning leg's gains rather than waiting for the loser to come back. Cut the position if the expected move stalls within a day or two; OTM premiums decay fast. As with all long-vol trades, do not carry into expiry week.

**Risk note.** The full debit can go to zero in a flat market — and it does so *more easily* than a straddle because both legs are OTM and need real movement just to retain value. IV crush after the event is again the silent killer.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +27,150 | -17,850 | -32,850 | -17,850 | +27,150 |

A 5% move to either 22,800 or 25,200 returns about +₹27,150, while anywhere between the strikes around 24,000 forfeits the full -₹32,850 debit.

**Adjustments, variants & timing.** Manage it like a straddle but with OTM legs. When the index runs to one strike, sell the now-ITM leg's gains and ride the cheap far leg, or roll the untested put/call closer to harvest value. Adding short wings further out converts it to a reverse iron condor, trimming cost and theta. Delta-hedge with Nifty futures once a leg goes ITM to lock gains. Cheaper than a straddle, so it suits a Bank Nifty weekly punt on a big move, but the wider dead-zone needs real travel; a Nifty monthly suits a slower thesis. Timing: enter on low IV rank and a sub-12 VIX before a catalyst, then exit into the IV spike. Do not buy into already-elevated weekly IV — OTM premiums decay fast and a modest wiggle leaves both legs worthless.

## 30. Short Strangle
*Range-bound, high IV · Short vega · net credit*

**The idea (intuition).** Sell an OTM call and an OTM put — you are the insurer again, but now you've left a wider safe zone between the strikes. You collect less premium than a short straddle but you give the index more room to wander before you're hurt. This is the bread-and-butter premium-selling trade on NSE.

**When & why to use it.** The textbook setup: high IV rank (India VIX elevated, say > 70th percentile), a range-bound or mean-reverting tape, and 30–45 days to expiry so theta does the work without expiry-week gamma. Sell after a vol spike. Do NOT sell into a trending market or ahead of an unhedged binary event — a one-way move blows through your strike.

**How to build it (₹, Nifty).** Sell 24400 CE @ 246 and sell 23600 PE @ 192 for a net credit of 438.1 points — about ₹32,858 received per lot.

![Figure: Short Strangle payoff at expiry](figs/strategies/short_strangle.png)

**The numbers (modelled at Nifty 24000).** Max profit is 438.0 points (~₹32,850 per lot), kept if Nifty expires between the strikes. Max loss is Undefined — large (unlimited on a runaway move). Breakevens 23162 and 24838 — a ~1,676-point safe band. Net credit 438.1 points; risk:reward undefined.

**Greeks & behaviour.** Net delta near zero, turning against you with the move (short gamma). Theta positive — your daily income. Vega negative — falling VIX is profit, rising VIX is pain. Positive theta versus negative gamma, exactly like the short straddle but with a wider cushion.

**Management & exit.** Close at ~50% of max credit; the last rupees aren't worth the tail risk. Hard stop at ~2x credit, and roll the tested side (e.g., roll the breached call up and out) to re-center. Take it off before expiry-week gamma turns small moves into big losses.

**Risk note.** This worst case assumes the index collapses (or rockets) far past a strike — bounded in practice only by where you stop out. Gap risk is real: a weekend shock can open beyond your breakeven. Size small, manage at a multiple of the credit, and remember premium selling is not free money — most retail sellers lose.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -27,150 | +17,850 | +32,850 | +17,850 | -27,150 |

The index sitting near 24,000 keeps the full +₹32,850, and the table's ±5% edges show only -₹27,150 — a larger break past 22,800 or 25,200 loses far more, without bound.

**Adjustments, variants & timing.** Roll the tested side out-and-away and the untested side in to rebalance deltas; if price keeps trending, go inverted or convert to an iron condor by buying wings for defined risk. Delta-hedge with Nifty futures to neutralise drift. This is NSE's bread-and-butter income trade. Bank Nifty weeklies pay fat premium but gamma bites hard near Thursday expiry, so the 30-45 DTE Nifty monthly is the sustainable home. Timing: sell at high IV rank (India VIX above its 70th percentile), after a vol spike, in a range-bound or mean-reverting tape; book at roughly 50% of credit and stop at about 2x. Never sell into a trending market or ahead of an unhedged binary event — a one-way move blows through your strike.

## 31. Long Strangle (Wide)
*Very big move · Long vega · net debit*

**The idea (intuition).** A long strangle pushed even further out — far OTM call and far OTM put. The cheapest way to own a "tail event" via vanilla options: tiny cost, but you only get paid on a genuinely violent move.

**When & why to use it.** Use it when you anticipate an outsized, fat-tail move — a crash or a melt-up — and want maximal convexity for minimal outlay. Good as a cheap hedge against a portfolio, or a pure punt on a major event you think the market is mispricing. Enter on low VIX. Do NOT expect it to pay on ordinary volatility; a "normal" 1–2% day leaves it worthless.

**How to build it (₹, Nifty).** Buy 24700 CE @ 135 and buy 23300 PE @ 129 for a net debit of 263.7 points — about ₹19,778 per lot, the cheapest long-vol structure so far except the lotto.

![Figure: Long Strangle (Wide) payoff at expiry](figs/strategies/long_strangle_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited. Max loss 264.0 points (~₹19,800 per lot) — the full debit, lost if Nifty expires inside the wide 23300–24700 band. Breakevens 23036 and 24964 — Nifty must move nearly 1,000 points to break even. Net debit 263.7 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; gamma is small until the index approaches a far strike, then ramps. Theta negative but small in absolute terms (cheap legs). Vega positive — a VIX explosion lifts it sharply. This is a convexity bet: it does almost nothing until it does everything.

**Management & exit.** Because the cost is low, you can give it more time than a tight strangle, but still cut it if the thesis (a big move) clearly fails. Sell into any volatility spike — these far-OTM options can multiply many times over on a fast move, so take the windfall rather than rounding-tripping it.

**Risk note.** The most likely outcome is a 100% loss of the (small) debit — far-OTM options usually expire worthless. Treat it as a low-cost lottery/hedge, not a core position, and size it as money you can afford to lose entirely.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +17,700 | -19,800 | -19,800 | -19,800 | +17,700 |

Only a genuine ±5% move to the edges turns a profit (+₹17,700); the whole middle band from 23,400 through 24,600 loses the entire -₹19,800 debit.

**Adjustments, variants & timing.** This is a convexity / tail bet, so the main "adjustment" is to sell into any volatility spike — far-OTM legs can multiply many times over. If a strike goes ITM, leg out the winner and delta-hedge with Nifty futures to bank the gain. You can finance it by selling even-further wings (a wide reverse iron condor) to cut net cost. It is cheap enough to use as a Bank Nifty weekly lottery on an expected shock, or as a portfolio crash hedge layered on Nifty monthly. Timing: buy only when IV rank is rock-bottom (VIX low) and you expect a fat-tail event the market is underpricing; a normal 1-2% day leaves it worthless, so do not pay up into elevated vol — the most likely outcome is a 100% loss of the small debit.

## 32. Short Strangle (Wide / 16-delta)
*Range-bound · Short vega · net credit*

**The idea (intuition).** Sell far-OTM strikes (around 16-delta) so the probability of either being breached is low. You collect a smaller credit but enjoy a wide, high-probability safe zone — the conservative cousin of the standard short strangle, and a staple of systematic premium-selling.

**When & why to use it.** High IV rank, range-bound expectations, 30–45 DTE. The 16-delta strikes are the classic "one standard deviation" sale — roughly 70% chance of expiring inside the band. Sell after VIX spikes. Do NOT mistake "high probability" for "safe" — the rare loss is large relative to the modest credit.

**How to build it (₹, Nifty).** Sell 24700 CE @ 135 and sell 23300 PE @ 129 for a net credit of 263.7 points — about ₹19,778 received per lot.

![Figure: Short Strangle (Wide / 16-delta) payoff at expiry](figs/strategies/short_strangle_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 264.0 points (~₹19,800 per lot), kept if Nifty stays within the strikes. Max loss Undefined — large. Breakevens 23036 and 24964 — a wide ~1,928-point cushion. Net credit 263.7 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; short gamma but mild near the money because strikes are far. Theta positive (your income); vega negative (falling VIX helps). Lower theta than a tight strangle, but also a far lower chance of the gamma turning against you.

**Management & exit.** Close at ~50% of credit, or even earlier given the small absolute reward. Stop or roll the tested side if price marches toward a strike. Take it off before expiry week. With a small credit, one undefended loss can erase many winning months — discipline matters most here.

**Risk note.** This worst case assumes a violent move far beyond a 16-delta strike — low probability but catastrophic relative to the credit. Size small and manage at a multiple of the credit; the seductive high win-rate is exactly what lulls sellers into oversizing.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -17,700 | +19,800 | +19,800 | +19,800 | -17,700 |

Anywhere inside the wide band (23,400-24,600) banks the full +₹19,800, and even a ±5% move shows only -₹17,700 here — a violent break beyond the 16-delta strikes loses much more, without bound.

**Adjustments, variants & timing.** Roll the tested side out-and-away and the untested side in; if breached, convert to an iron condor by buying cheap wings, or go inverted. Delta-hedge with Nifty futures when a strike is threatened. The 16-delta ("one standard deviation") strikes are the systematic seller's staple, roughly a 70% chance of expiring inside the band. Bank Nifty weeklies give high theta but the rare loss arrives fast; the 30-45 DTE Nifty monthly is steadier. Timing: sell at high IV rank after a VIX spike in a range-bound regime; the high win-rate seduces oversizing, so keep size small, book at ~50% of credit, and manage at a multiple of the modest premium received.

## 33. Long Guts
*Big move · Long vega · net debit*

**The idea (intuition).** A long strangle built from *in-the-money* options instead of OTM ones — buy an ITM call (strike below spot) and an ITM put (strike above spot). It behaves like a straddle/strangle but is built from intrinsic-heavy legs, so much of the debit is real value you get back, not pure time premium.

**When & why to use it.** Mostly a structural/arbitrage curiosity in liquid NSE index options, but it makes sense when ITM strikes are better priced or more liquid than the OTM equivalents, or to capture a mispricing between ITM and OTM vol. Same long-vol thesis: big move expected, low IV. Do NOT use it casually — the wide bid-ask on ITM options and the large cash outlay usually make a plain strangle cleaner.

**How to build it (₹, Nifty).** Buy 23700 CE @ 655 (ITM) and buy 24300 PE @ 453 (ITM) for a net debit of 1107.2 points — about ₹83,040 per lot. Note: much of that is intrinsic value (the strikes straddle spot), so the *true* premium at risk is far smaller than the headline debit.

![Figure: Long Guts payoff at expiry](figs/strategies/long_guts.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited. Max loss 507.0 points (~₹38,025 per lot) — this is the time-value-at-risk, NOT the full 1107-point debit, because the intrinsic value (the 600-point gap between the ITM strikes) is recovered if Nifty stays between them. Breakevens 23193 and 24807. Net debit 1107.2 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero at the money (the two ITM legs offset). Positive gamma, negative theta (you only lose the time-value portion), positive vega. Functionally identical exposure to a long strangle once you net out the intrinsic value.

**Management & exit.** Manage it like a long strangle — exit into a move, cut if the catalyst fails. Be especially mindful of liquidity: closing ITM legs can cost you in slippage, so favour it only where the ITM book is tight.

**Risk note.** The headline debit (₹83,040) overstates the real risk — your true exposure is the ~507 points of time value. The practical danger is execution: poor ITM liquidity and wider spreads can quietly cost more than the theoretical edge.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +29,475 | -15,525 | -38,025 | -15,525 | +29,475 |

A ±5% move pays roughly +₹29,475, while a pin near 24,000 loses -₹38,025 of time value — not the headline ₹83,040 debit, since the intrinsic between the strikes is recovered.

**Adjustments, variants & timing.** It behaves like a long strangle once intrinsic is netted out, so manage it identically — leg out the winning ITM option into a move and delta-hedge the runner with Nifty futures. Watch ITM liquidity: a wide bid-ask makes legging costly, so prefer it only where the ITM book is tight. You can sell OTM wings to defray the time-value bleed. It is rarely worth it on Bank Nifty weeklies (thinner ITM books, fast theta); it works better on liquid Nifty monthly where ITM spreads are tighter. Timing: enter on low IV rank before a big-move catalyst and exit into the vol spike — and only when ITM pricing genuinely beats the equivalent OTM long strangle.

## 34. Short Guts
*Range-bound · Short vega · net credit*

**The idea (intuition).** The mirror of long guts: sell an ITM call and an ITM put. You take in a large credit (full of intrinsic value you'll have to return), and you profit if the index stays *between* the two ITM strikes, where the options' intrinsic value shrinks toward zero.

**When & why to use it.** A range-bound, high-IV play used when ITM options carry a vol or liquidity edge over selling the OTM strangle. Same short-vol regime: elevated VIX, expectation of a quiet tape. Do NOT prefer it over a short strangle unless the ITM pricing genuinely favours it — the large credit is mostly intrinsic and must be paid back, so it ties up margin without proportionate reward.

**How to build it (₹, Nifty).** Sell 23700 CE @ 655 and sell 24300 PE @ 453 for a net credit of 1107.2 points — about ₹83,040 received per lot, most of which is intrinsic value you are effectively holding in trust.

![Figure: Short Guts payoff at expiry](figs/strategies/short_guts.png)

**The numbers (modelled at Nifty 24000).** Max profit 507.0 points (~₹38,025 per lot) — the time value you keep if Nifty expires between the strikes (the intrinsic part is returned). Max loss Undefined — large. Breakevens 23193 and 24807. Net credit 1107.2 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; short gamma; theta positive (you keep the eroding time value); vega negative. Identical risk profile to a short strangle once intrinsic value is netted out — same unlimited tails on a breakout.

**Management & exit.** Manage exactly as a short strangle: take ~50% of the keepable credit (the 507 points), stop/roll the tested side, and exit before expiry-week gamma. Watch assignment risk closely — ITM short options can be exercised, especially near expiry.

**Risk note.** This worst case assumes a large move beyond a strike; the loss is bounded in practice only by your stop. Added wrinkle: short ITM options carry real assignment/early-exercise risk and STT on exercised ITM contracts. Size small, manage the credit, and don't be seduced by the large headline premium — most of it isn't yours to keep.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -29,475 | +15,525 | +38,025 | +15,525 | -29,475 |

Staying between the ITM strikes around 24,000 keeps the +₹38,025 of time value; the ±5% edges show -₹29,475, but a bigger break loses without limit.

**Adjustments, variants & timing.** The risk is identical to a short strangle once intrinsic nets out — roll the tested side out, buy wings to define risk as an iron structure, or delta-hedge with Nifty futures. Note that Nifty and Bank Nifty index options are European, cash-settled, so there is no early-exercise assignment, but STT on exercised ITM contracts and heavy margin on a mostly-intrinsic credit still bite. That margin and liquidity drag means it is seldom preferred over a plain short strangle, and it sits better on Nifty monthly than on Bank Nifty weeklies. Timing: deploy only at high IV rank when ITM vol or liquidity genuinely favours it; book around 50% of the keepable time value, stop at a multiple of credit, and exit before expiry-week gamma.

## 35. Strip (Bearish Straddle)
*Big move, bearish bias · Long vega · net debit*

**The idea (intuition).** A long straddle with a bearish tilt: same ATM call and put, but you buy *two* puts for every call. You still profit on a big move either way, but you make more (and break even sooner) on a fall — you've geared the structure to your downside lean.

**When & why to use it.** Use it when you expect a large move and lean bearish but want protection in case you're wrong and the index rips up. Good ahead of an event where the risk skews to the downside (a feared policy shock, weak global cues). Enter on low IV. Do NOT use it if you have no directional view — a plain straddle is cheaper and cleaner for pure neutrality.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456 and buy 2x 24000 PE @ 318 for a net debit of 1092.4 points — about ₹81,930 per lot. The extra put is what creates the downside gearing.

![Figure: Strip (Bearish Straddle) payoff at expiry](figs/strategies/strip.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (and steeper to the downside — two puts gaining versus one call). Max loss 1084.0 points (~₹81,300 per lot) if Nifty pins 24000. Breakevens 23454 (down) and 25092 (up) — note the asymmetry: you break even with a smaller fall than rise. Net debit 1092.4 points; risk:reward undefined.

**Greeks & behaviour.** Net delta is negative at inception (two puts outweigh one call), so it leans short. Positive gamma, negative theta, positive vega — a long-vol trade with a bearish delta tilt. A down-move pays roughly twice as fast as an equivalent up-move.

**Management & exit.** Exit into a down-move where the two puts do the heavy lifting; take profits rather than holding for the floor. Cut if the move stalls — you're carrying extra theta versus a plain straddle. Don't hold into expiry week.

**Risk note.** You pay more debit than a straddle (₹81,930) for the bearish gearing, so a flat market hurts more. If the index drifts sideways or grinds up modestly, the two-put cost bleeds faster than a symmetric straddle would.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +98,100 | +8,100 | -81,900 | -36,900 | +8,100 |

The bearish gearing shows — a 5% fall to 22,800 pays +₹98,100, far more than the +₹8,100 from an equal 5% rise, while a pin at 24,000 loses -₹81,900.

**Adjustments, variants & timing.** When the index falls, leg out one of the two puts into strength and let the rest run; if it rallies instead, sell the single call's gains and delta-hedge the puts with short Nifty futures. Convert to a defined-risk structure by selling deeper OTM wings. The extra put means heavy theta, so it suits a Bank Nifty weekly with a clear bearish catalyst (feared policy shock, weak global cues) more than a slow Nifty monthly grind. Timing: buy on low IV rank ahead of a downside-skewed event; exit into the down-move and the IV spike, and never carry the doubled theta into expiry week. If the index drifts sideways or grinds up modestly, cut quickly — the two-put cost bleeds fast.

## 36. Strap (Bullish Straddle)
*Big move, bullish bias · Long vega · net debit*

**The idea (intuition).** The bullish mirror of the strip: same ATM straddle base, but you buy *two* calls for every put. Big move either way still pays, but you're geared to make more on a rally — a long-vol trade for when you lean up but want downside insurance.

**When & why to use it.** Use it when you expect a large move with an upside bias — ahead of a result or event where good news could trigger a sharp rally but you still want protection against a fall. Low IV entry. Do NOT use it as a neutral bet; the extra call costs money and only pays if your bullish lean is right.

**How to build it (₹, Nifty).** Buy 2x 24000 CE @ 456 and buy 24000 PE @ 318 for a net debit of 1230.1 points — about ₹92,258 per lot, the priciest structure in this group (two ATM calls are expensive).

![Figure: Strap (Bullish Straddle) payoff at expiry](figs/strategies/strap.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited (steeper to the upside — two calls running). Max loss 1215.0 points (~₹91,125 per lot) if Nifty pins 24000. Breakevens 22770 (down) and 24615 (up) — asymmetric: you break even with a smaller *rise* than fall. Net debit 1230.1 points; risk:reward undefined.

**Greeks & behaviour.** Net delta positive at inception (two calls outweigh one put), so it leans long. Positive gamma, negative theta, positive vega — long volatility with a bullish delta tilt. An up-move pays about twice as fast as the equivalent down-move.

**Management & exit.** Take profit into a rally where the doubled calls accelerate; close into strength. Cut if the move fails to appear — you carry the most theta of any structure here. Avoid expiry week.

**Risk note.** Highest debit in the group (₹92,258 per lot), so a flat or mildly-down tape bleeds you fastest. The bullish gearing is only an asset if you're right on direction; if the index falls, the single put can't fully rescue the two dead calls.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -2,250 | -47,250 | -92,250 | -2,250 | +87,750 |

The bullish tilt is visible — a 5% rally to 25,200 pays +₹87,750 while the same-sized fall barely breaks even (-₹2,250), and a pin at 24,000 loses the full -₹92,250.

**Adjustments, variants & timing.** On a rally, leg out one of the two calls into strength and ride the rest; on a fall, bank the single put and delta-hedge the calls with long Nifty futures. Sell OTM wings to cap the priciest debit in the group. With the most theta of any structure here, it favours a Bank Nifty weekly on a clear bullish trigger (results beat, dovish RBI) over a slow Nifty monthly. Timing: enter at low IV rank before an upside-skewed event; close into the rally and the vol spike. A flat or mildly-down tape bleeds it fastest, so cut quickly if the move fails to appear, and avoid carrying into expiry week.

## 37. Long Straddle (Weekly)
*Big move within days · Long vega · net debit*

**The idea (intuition).** A long straddle on the weekly expiry — same buy-the-call-and-put bet, but on options with only days to live. Cheaper entry, but vicious theta: it's a sharp, short-fuse punt on an imminent move.

**When & why to use it.** Use it for a catalyst landing *this week* — a mid-week data print, an RBI decision, a stock-specific event spilling into the index. The low premium gives high gamma per rupee. Do NOT hold it idly; weekly theta is brutal and a day of no movement is expensive. Avoid buying it into an already-pumped weekly IV the day before a known event.

**How to build it (₹, Nifty).** Buy 24000 CE @ 202 and buy 24000 PE @ 170 for a net debit of 371.9 points — about ₹27,893 per lot, roughly half the cost of the monthly straddle.

![Figure: Long Straddle (Weekly) payoff at expiry](figs/strategies/long_straddle_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited. Max loss 363.0 points (~₹27,225 per lot) if Nifty pins 24000 at the weekly close. Breakevens 23628 and 24372 — a tight ~744-point band, much narrower than the monthly, so a smaller move pays. Net debit 371.9 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero, but gamma is enormous (short-dated ATM options), so P&L swings fast on any move. Theta is severe and negative — the dominant force if the index sits still. Vega positive but smaller than a monthly's (less time = less vega). This is a gamma trade above all.

**Management & exit.** Be quick and decisive. Take profit into the move within a day or two — weekly straddles can double fast and decay just as fast. If the catalyst passes without a move, cut immediately; holding overnight into a flat tape is pure theta bleed.

**Risk note.** Theta is the enemy here more than anywhere else — a quiet two days can vaporise the debit. The tight breakevens cut both ways: easy to reach, but the position is hyper-sensitive, so a fakeout move that reverses can still leave you with a loss at expiry.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +62,100 | +17,100 | -27,900 | +17,100 | +62,100 |

The tight weekly breakevens mean even a 2.5% move (to 23,400 or 24,600) already pays +₹17,100, and a 5% move balloons to +₹62,100, versus the -₹27,900 max loss at a 24,000 pin.

**Adjustments, variants & timing.** Be fast — leg out the winning side into the move and gamma-scalp the runner with Nifty or Bank Nifty futures, since weekly gamma is enormous. Sell same-expiry OTM wings to convert it to a reverse iron fly and blunt the savage theta. This structure is built for Bank Nifty weeklies (the highest gamma per rupee) far more than a Nifty monthly. Timing: buy only for a catalyst landing this week, on low or normal weekly IV; do not buy into an already-pumped weekly IV the night before a known event. If the move doesn't come within a day or two, cut — overnight theta bleed is unforgiving, and a quiet two days can vaporise the debit.

## 38. Short Strangle (Weekly)
*Quiet week · Short vega · net credit*

**The idea (intuition).** Sell an OTM call and OTM put on the weekly expiry — harvest the fast theta of short-dated options during a week you expect to be dull. The premium-seller's favourite income trade on NSE, and also its most over-traded one.

**When & why to use it.** Use it in a genuinely quiet week with no scheduled catalyst, when weekly IV is rich relative to expected movement. The rapid weekly decay means theta accrues fast. Do NOT sell weeklies through an event, and respect that with only days to expiry, gamma risk is high the moment price approaches a strike. This is the structure behind many blown retail accounts — handle with care.

**How to build it (₹, Nifty).** Sell 24350 CE @ 61 and sell 23650 PE @ 61 for a net credit of 121.6 points — about ₹9,120 received per lot. Small credit, fast decay.

![Figure: Short Strangle (Weekly) payoff at expiry](figs/strategies/short_strangle_weekly.png)

**The numbers (modelled at Nifty 24000).** Max profit 122.0 points (~₹9,150 per lot), kept if Nifty stays within the strikes to Thursday's close. Max loss Undefined — large. Breakevens 23528 and 24472 — a ~944-point band. Net credit 121.6 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; short gamma that bites hard near expiry; theta strongly positive (fast weekly decay is the appeal); vega negative. Of every short trade here, this has the most violent gamma-versus-theta dynamic because expiry is days away.

**Management & exit.** Take profit early — 50% of a small weekly credit can come in a day. Stop or roll aggressively the instant price threatens a strike; with weeklies you have little time to recover. Many traders simply close by Wednesday to dodge the final-day gamma spike.

**Risk note.** This worst case assumes a sharp move past a strike; near expiry, gamma makes that loss arrive fast and large relative to the tiny ₹9,120 credit. A single bad weekly can erase months of income. Size small, manage at a multiple of credit, and don't mistake a high weekly win-rate for safety — most retail F&O sellers lose over time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -54,600 | -9,600 | +9,150 | -9,600 | -54,600 |

Only a near pin keeps the thin +₹9,150 credit; even a 2.5% move already shows -₹9,600, and a 5% break to the edges loses -₹54,600 — far more than the credit, and it keeps growing beyond.

**Adjustments, variants & timing.** Defend fast — roll the tested side out-and-away and the untested side in, or buy wings to cap risk as a weekly iron condor; delta-hedge with futures the instant price nears a strike. Many traders simply close by Wednesday to dodge final-day gamma. This is the most over-traded retail income trade on NSE and the cause of many blown accounts. Bank Nifty weeklies maximise theta but the gamma tail is violent, so size tiny. Timing: sell only in a genuinely quiet week with no scheduled catalyst, when weekly IV is rich relative to expected movement; book ~50% early, stop at a multiple of the small credit, and never sell weeklies through an event.

## 39. Long Strangle (Weekly Lotto)
*Explosive move · Long vega · net debit*

**The idea (intuition).** A near-worthless far-OTM weekly call and put bought for pocket change — a literal lottery ticket on an explosive move in the next few days. Almost always expires at zero; occasionally pays many multiples.

**When & why to use it.** Use it as a cheap punt or tail-hedge when you suspect a violent surprise this week that the market is ignoring. The appeal is pure convexity: risk a tiny sum for a shot at a 10x. Do NOT treat it as a real strategy or size it meaningfully — the base rate is a total loss. It's the cheapest seat in the casino.

**How to build it (₹, Nifty).** Buy 24700 CE @ 10 and buy 23300 PE @ 17 for a net debit of 27.2 points — about ₹2,040 per lot. Genuinely lottery-ticket money.

![Figure: Long Strangle (Weekly Lotto) payoff at expiry](figs/strategies/long_strangle_lotto.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited. Max loss 27.0 points (~₹2,025 per lot) — the whole tiny debit, lost (the most likely outcome) if Nifty stays within the wide band. Breakevens 23273 and 24727 — needs a ~700+ point move in days. Net debit 27.2 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; gamma negligible until a strike is approached, then explosive; theta small in rupee terms but 100% of value disappears by Thursday; vega positive. It does nothing, then everything — or, usually, nothing.

**Management & exit.** If a violent move occurs and these balloon, *sell immediately* — far-OTM weekly options can 10–20x and then collapse within hours. Otherwise expect to write it off. Never average down or "give it more time" — there is no more time.

**Risk note.** The overwhelmingly likely outcome is a 100% loss of the small debit. This is entertainment-grade risk: only deploy money you've already mentally written off, and never let a rare win tempt you into upsizing the next ticket.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +35,475 | -2,025 | -2,025 | -2,025 | +35,475 |

The overwhelming base case is the tiny -₹2,025 total loss across the middle; only a violent ±5% move to the edges flips it to +₹35,475.

**Adjustments, variants & timing.** There is little to adjust on a ₹2,040 ticket — the only discipline is to sell immediately if a shock balloons the legs (far-OTM weeklies can 10-20x and then collapse within hours), and otherwise write it off. Never average down or "give it more time" — by Thursday there is no time. You can optionally finance it by selling an even-further wing, but the cost is already trivial. It is purely a Bank Nifty / Nifty weekly instrument and meaningless as a monthly. Timing: deploy only when you suspect a violent surprise the market is ignoring this week, with money already mentally written off; a rare win must never tempt you into upsizing the next ticket.

## 40. Short Straddle (45-DTE)
*Range-bound, rich IV · Short vega · net credit*

**The idea (intuition).** An ATM short straddle placed with ~45 days to expiry rather than on the weekly. You give up the fast weekly decay for a smoother, more manageable position with less expiry-week gamma — the "professional" version of selling a straddle.

**When & why to use it.** The 45-DTE window is the systematic premium-seller's sweet spot: enough theta to earn, enough time to manage and roll, and you're not yet in the gamma danger zone. Deploy in high IV rank, range-bound conditions. Sell after a VIX spike. Do NOT hold it all the way to expiry — the whole point is to harvest decay early and exit before gamma ramps.

**How to build it (₹, Nifty).** Sell 24000 CE @ 579 and sell 24000 PE @ 373 for a net credit of 951.6 points — about ₹71,370 received per lot (richer than the near-dated straddle because 45-DTE options carry more time value).

![Figure: Short Straddle (45-DTE) payoff at expiry](figs/strategies/short_straddle_45d.png)

**The numbers (modelled at Nifty 24000).** Max profit 943.0 points (~₹70,725 per lot) if Nifty expires at 24000. Max loss Undefined — large. Breakevens 23048 and 24952 — a wide ~1,904-point band, the widest of any straddle here thanks to the fat credit. Net credit 951.6 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; short gamma, but *gentler* than weekly/monthly versions because 45 days out the gamma is low. Theta positive and steady; vega negative and large — this position is heavily exposed to a VIX move, so a vol spike hurts well before expiry. Vega, not gamma, dominates early.

**Management & exit.** Manage on the calendar: take ~50% of max credit and close, typically with 21+ days still left, rather than riding into the gamma zone. Roll the tested side or delta-hedge if the index trends. The defined exit discipline is what makes 45-DTE selling sustainable.

**Risk note.** This worst case assumes a large directional move; bounded in practice only by your stop. The big near-term risk is vega — a sudden India VIX spike inflates both short legs and shows a mark-to-market loss even with the index still inside the band. Size small, manage the credit, and never treat the large premium as free money.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -18,600 | +26,400 | +71,400 | +26,400 | -18,600 |

A 24,000 pin banks the full +₹71,400, and thanks to the fat 45-day credit even a 5% move only shows -₹18,600 here — though a larger break still loses without limit.

**Adjustments, variants & timing.** Manage on the calendar — take ~50% of credit and close with 21+ days left, before gamma ramps. Roll the tested side or delta-hedge with Nifty futures if the index trends. Because vega dominates early, a sudden India VIX spike shows a mark-to-market loss even with spot inside the band, so size for that. Add wings to define risk as a wide iron fly if needed. This 45-DTE window is the systematic seller's sweet spot — a Nifty monthly trade, not a Bank Nifty weekly. Timing: sell at high IV rank after a VIX spike in a range-bound regime; harvest decay early and exit before the gamma zone rather than riding all the way to expiry.

## 41. Long Straddle (Pre-Event)
*Event move · Long vega · net debit*

**The idea (intuition).** A long straddle bought specifically to capture an event-driven move — results, RBI, budget, election count. You're betting the realised move (and/or the IV run-up into the event) exceeds the premium. The catch is that everyone knows the event is coming, so the premium is already inflated.

**When & why to use it.** Buy it *early*, before the market has fully bid up event vol — days ahead of the catalyst while IV is still climbing, so you ride the vega run-up and have gamma for the move. Do NOT buy it the night before the event when IV is at its peak; you'll pay top dollar and get crushed when vol collapses at the open, often losing even if the index moves.

**How to build it (₹, Nifty).** Buy 24000 CE @ 169 and buy 24000 PE @ 146 for a net debit of 314.2 points — about ₹23,565 per lot.

![Figure: Long Straddle (Pre-Event) payoff at expiry](figs/strategies/long_straddle_event.png)

**The numbers (modelled at Nifty 24000).** Max profit Unlimited. Max loss 305.0 points (~₹22,875 per lot) if Nifty pins 24000. Breakevens 23686 and 24314 — a tight ~628-point band, so a fairly modest event move pays. Net debit 314.2 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; high gamma (short-dated, ATM); theta negative; vega positive — and vega is the headline here. The pre-event play is as much a bet on rising IV into the event as on the move itself; a VIX run-up can profit you before the announcement even lands.

**Management & exit.** The disciplined play is often to exit *into* the IV peak just before the event, capturing the vega run-up and side-stepping the post-event crush entirely. If you hold through the announcement, close immediately into the move — do not linger while IV deflates.

**Risk note.** The defining danger is IV crush: the moment the event passes, event vol collapses and both legs lose extrinsic value fast. You can call the direction correctly and still lose if the move is smaller than the (already pricey) premium implied. Tight breakevens help, but the crush is relentless.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +66,450 | +21,450 | -23,550 | +21,450 | +66,450 |

The tight breakevens mean a modest 2.5% event move (to 23,400 or 24,600) already pays +₹21,450 and a 5% move +₹66,450, against a -₹23,550 loss if Nifty pins 24,000.

**Adjustments, variants & timing.** The disciplined play is to exit into the IV peak just before the event, capturing the vega run-up and side-stepping the crush entirely; if you hold through, close instantly into the move. Leg out the winner and delta-hedge the runner with futures. Sell OTM wings to defray cost if IV is already rich. It works on both Bank Nifty weeklies (results, high gamma) and Nifty monthly (budget, RBI policy, election count). Timing: buy early — days ahead while IV is still climbing — at low IV rank; never buy the night before when event vol peaks, or the post-event IV crush will gut you even on a correct directional call.

## 42. Short Strangle (10-delta)
*Strongly range-bound · Short vega · net credit*

**The idea (intuition).** Sell very far-OTM strikes — around 10-delta, roughly a 90% chance each expires worthless. The ultra-conservative premium sale: a small credit for a very wide safe zone. High win-rate, but each rare loss is large relative to the thin premium.

**When & why to use it.** Use it when you're strongly convinced the index will stay range-bound and you want maximum probability of profit — high IV rank, no catalyst, 30–45 DTE. The 10-delta strikes sit well outside the expected range. Do NOT confuse the ~90% win-rate with safety; the loss when it comes can dwarf many winners, and oversizing on the high hit-rate is the classic trap.

**How to build it (₹, Nifty).** Sell 24900 CE @ 83 and sell 23100 PE @ 98 for a net credit of 180.7 points — about ₹13,553 received per lot.

![Figure: Short Strangle (10-delta) payoff at expiry](figs/strategies/short_strangle_delta10.png)

**The numbers (modelled at Nifty 24000).** Max profit 181.0 points (~₹13,575 per lot), kept if Nifty stays within the strikes. Max loss Undefined — large. Breakevens 22919 and 25081 — a very wide ~2,162-point cushion, the widest in this group. Net credit 180.7 points; risk:reward undefined.

**Greeks & behaviour.** Delta near zero; short gamma, but minimal near the money because the strikes are so far out; theta positive (modest); vega negative. Of the short strangles, this has the lowest day-to-day gamma risk — until price makes an unexpected run at a strike.

**Management & exit.** Close at ~50% of the (already small) credit, or roll the tested side early if price drifts toward a strike. With such a thin reward, even one undefended loss is costly, so a hard stop at a multiple of credit and disciplined sizing are non-negotiable. Take it off before expiry-week gamma.

**Risk note.** This worst case assumes a violent move past a 10-delta strike — improbable, but devastating relative to the ₹13,553 credit. The high win-rate is precisely what seduces sellers into oversizing; size small, manage at a multiple of the credit, and never treat the steady premium as free money — most retail F&O sellers lose over time.

**Scenario P&L (₹ per lot, at expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -8,925 | +13,575 | +13,575 | +13,575 | -8,925 |

The very wide 10-delta band keeps the full +₹13,575 across 23,400-24,600, and even a 5% move shows only -₹8,925 here — but a rare break past the strikes loses many multiples of the thin credit.

**Adjustments, variants & timing.** Roll the tested side out-and-away early, buy cheap wings to convert it to a wide iron condor, or delta-hedge with Nifty futures if price drifts toward a strike. With a ~90% theoretical win-rate, the trap is oversizing — one undefended tail can erase many winning months, so keep size small and stop at a multiple of credit. It has the lowest day-to-day gamma of the short strangles, suiting a 30-45 DTE Nifty monthly over twitchy Bank Nifty weeklies. Timing: sell only at high IV rank, with no catalyst and a strongly range-bound tape; book ~50% (or earlier given the thin reward) and never treat the steady premium as free money — most retail F&O sellers lose over time.
