# Strategy Group 7: Calendars & Diagonals

Calendars and diagonals are *time spreads*: you sell a near-dated option and buy a longer-dated option, so the two legs decay at different speeds. The structure makes money two ways — the front leg bleeds theta faster than the back leg you own, and because the long back leg carries more vega than the short front leg, the position is net **long vega** and gains when implied volatility rises. That is the family's signature trade-off: you want the index to *pin* near your strike (so the front option expires worthless) while volatility *climbs* (so your back option re-prices up). Diagonals tilt the same machine in a direction by separating the strikes, and the poor-man's-covered-call stretches it into a capital-light income trade against a long-dated (LEAPS-style) anchor. Reverse calendars flip the legs and become short-vega bets on a big move or a term-structure collapse.

A practical India note before we begin: on NSE, Nifty weeklies and monthlies usually trade at *different* implied vols (the term structure), and around events — Budget, RBI policy, big earnings clusters — the front week's IV spikes far above the back month. That gap is the raw material of every trade in this chapter. The cleanest entries come when front IV is rich relative to back IV and the overall IV *rank* is low (so you are buying back-month vega cheaply with room to rise).

## 95. Call Calendar (Horizontal)

*Pin near strike, rising IV · Long vega · net debit*

**The idea (intuition).** Sell the front-week 24000 call, buy the same-strike back-month 24000 call. The near option melts faster than the far one you hold, so if Nifty sits at 24000 into the front expiry, the short call dies and you are left owning a still-valuable longer-dated call. It is renting out the fast-decaying option while keeping the slow one.

**When & why to use it.** You want a quiet, range-bound tape that drifts toward 24000 into the near expiry, plus an IV regime that is *low and likely to rise* — India VIX near the bottom of its range, IV rank under ~30, ideally a catalyst (policy meeting, results season) further out that can lift the back month. Avoid it when front IV is already crushed flat against the back, when a trend is running, or right before a gap-risk event that can blow you past a breakeven overnight.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 24000 CE @ 689. Net debit 232.7 points, or about ₹17,453 per lot (232.7 × 75). That debit is your entire capital at risk; there is no margin beyond it because the long covers the short.

![Figure: Call Calendar (Horizontal) payoff at expiry](figs/strategies/call_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 219 points (~₹16,425/lot) at the strike on front expiry; max loss 233 points (~₹17,475/lot) if price runs far from 24000; breakevens 23521 and 24757; net debit 232.7 points; risk:reward 0.94. The payoff is a tent peaked at 24000 and sloping to the full debit loss on either wing.

**Greeks & behaviour.** Near the strike net delta is roughly flat, theta is positive (front decay dominates), and vega is positive — a rise in back-month IV inflates the long leg and is your biggest tailwind. Move away from the strike and delta picks up against you.

**Management & exit.** Take it off near the front expiry. A common target is +20–30% on the debit, or roll the short call out a week to harvest more theta if 24000 still looks like the magnet. Cut if price breaches a breakeven and keeps going.

**Risk note.** The danger is a directional move plus an IV *crush* in the back month — both legs work against you and you can lose most of the debit. Pin risk on the short strike at expiry can also leave you briefly assigned; close rather than carry through expiry.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹12,975 | -₹3,075 | +₹16,725 | +₹2,325 | -₹4,200 |

The table peaks sharply at 24,000 (+₹16,725) and rolls into losses on both wings as the index leaves the strike, the classic single-strike calendar tent — and because this is a time spread the back-month call is still alive, so these figures assume the modelled back-month IV holds.

**Adjustments, variants & timing.** Run this on Nifty rather than Bank Nifty: Nifty's tighter weekly-to-monthly IV gaps and deeper liquidity make the term-structure cleaner and slippage smaller. The core management is rolling — if 24,000 still looks like the magnet at front expiry, buy back the dying short call and sell the next week's 24,000 call for a fresh credit, repeating against the same back-month long. If price drifts, recentre by closing and reopening the whole calendar at the new ATM strike rather than nursing a skewed tent. Bank Nifty works only if you size down for its larger point swings. On timing, enter when India VIX sits in the bottom third of its range and IV rank is under ~30, ideally with a catalyst (RBI policy, Budget, results) seated in the back month so a vol rise lifts your long. Close into any sharp IV spike — a vega win you should bank rather than hold through front-expiry gamma.

## 96. Put Calendar

*Pin near strike · Long vega · net debit*

**The idea (intuition).** The mirror of the call calendar, built from puts: sell the front 24000 put, buy the back-month 24000 put. Same tent-shaped payoff peaked at the strike, but assembled on the put side — handy when the put skew makes near-dated puts richer to sell.

**When & why to use it.** Reach for the put version when downside skew is steep (front-week 24000 puts fat from fear) and you still expect Nifty to hover around 24000 into the near expiry. Same IV logic as the call calendar — low IV rank, scope for the back month to firm. Skip it in a clear uptrend (the structure is delta-neutral, not bullish) or when an air-pocket sell-off could rocket price below the lower breakeven.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 24000 PE @ 414. Net debit only 95.8 points, about ₹7,185 per lot — noticeably cheaper than the call calendar because the put term-structure spread is tighter here.

![Figure: Put Calendar payoff at expiry](figs/strategies/put_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 219 points (~₹16,425/lot); max loss 233 points (~₹17,475/lot); breakevens 23523 and 24752; net debit 95.8 points; risk:reward 0.94. Note the modelled max loss (233) exceeds the cash debit (95.8) — that is the engine's worst-case across the back-leg's life, not just the entry outlay.

**Greeks & behaviour.** Delta near flat at the strike, theta positive, vega positive. The put build behaves identically to the call calendar in P&L terms; the choice between them is purely about which side's term structure you are selling more cheaply.

**Management & exit.** Same playbook: aim to close into front expiry near peak value, roll the short put for another cycle if 24000 holds, and abandon the trade if price trends decisively through a breakeven.

**Risk note.** A sharp down-move that overshoots 23523, combined with back-month IV softening once the panic passes, is the classic loser. Manage the short put before expiry to avoid assignment and the associated cash-settlement surprises.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹13,050 | -₹3,150 | +₹16,650 | +₹2,250 | -₹4,200 |

P&L peaks at +₹16,650 with Nifty pinned to 24,000 and decays to losses either side, the put build's tent mirroring the call calendar — a time spread, so the surviving back-month put is marked at the modelled IV rather than crushed.

**Adjustments, variants & timing.** Favour the put build on Nifty when downside skew is steep so the front put you sell is richer. Manage by rolling the short 24,000 put into the next weekly for another credit while 24,000 holds, and recentre the entire spread if the index trends away from the strike rather than defending a lopsided tent. Bank Nifty is viable but its wider swings demand smaller size. The IV window is the same as every long calendar: enter when IV rank is low (under ~30) and front IV is rich relative to the back month, ideally with a later catalyst — RBI policy or a results cluster — that can firm the back-month put you own. Close into an IV spike to harvest the vega gain. Always exit before front expiry to avoid assignment and the cash-settlement quirks of index options; don't let weekly gamma decide the trade for you in the final session.

## 97. Call Diagonal

*Bullish drift to strike · Long vega · net debit*

**The idea (intuition).** Take a calendar and pull the strikes apart so it leans bullish: buy a lower, longer-dated 23700 call and sell a higher, near-dated 24000 call. You now own a deep-ish call that profits as Nifty climbs, financed partly by selling the front 24000 call against it — a calendar with a directional engine bolted on.

**When & why to use it.** Use it when you are gently bullish — you expect a grind up toward 24000 by the front expiry rather than an explosive rally — and you like collecting front-week theta while you wait. Best when IV rank is modest so the long leg is not overpaid. Wrong tool if you expect a violent breakout (a simple long call or call spread captures that better) or a hard reversal lower.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456, buy 23700 CE @ 894. Net debit 438.4 points, about ₹32,880 per lot. Pricier than a plain calendar because the long leg is closer to the money and carries real intrinsic-plus-time value.

![Figure: Call Diagonal payoff at expiry](figs/strategies/call_diagonal.png)

**The numbers (modelled at Nifty 24000).** Max profit 214 points (~₹16,050/lot); max loss 438 points (~₹32,850/lot, essentially the full debit); breakevens 23645 and 26130; net debit 438.4 points; risk:reward 0.49. The wide upper breakeven (26130) shows the bullish tilt — you keep participating well above the short strike.

**Greeks & behaviour.** Net delta is positive (the directional tilt), theta positive while price sits below the short strike, vega positive. Direction and time both help here; a sell-off is the enemy.

**Management & exit.** Target a partial close as price approaches 24000 into front expiry, or roll the short call up-and-out to keep the bullish structure alive if the trend continues. Stop out near the lower breakeven where the long leg starts bleeding intrinsic value.

**Risk note.** Worst case is a drop that strands the long 23700 call out-of-the-money while the front call you sold expires worthless — you lose the bulk of the 438-point debit. The poor risk:reward (0.49) means you must be right on *both* direction and timing.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹23,775 | -₹9,075 | +₹16,200 | +₹5,925 | +₹1,650 |

The bullish lean shows in the numbers: the structure peaks at 24,000 (+₹16,200) yet stays positive up at 24,600 and 25,200 while the 22,800 downside is the worst cell (-₹23,775) — and as a time spread the long back-month call still carries value at the modelled IV.

**Adjustments, variants & timing.** Because this leans bullish, manage it directionally: roll the short 24,000 call up-and-out as Nifty grinds higher to keep collecting credit and lift the cap, or recentre the whole diagonal if the trend stalls. On a reversal lower, cut near the 23,645 breakeven before the long 23,700 call sheds intrinsic value. Run it on Nifty for tighter strikes and cleaner term structure; Bank Nifty suits it only when you want bigger directional punch and can size down. Weekly short against a monthly long gives the fastest theta; a monthly-against-further build is calmer if you want room. Enter with IV rank low so the closer-to-money long is not overpaid, and ideally with a back-month catalyst to add a vega tailwind. Since you need both direction and timing right (risk:reward 0.49), keep size modest and bank profit into any IV spike or as price approaches the short strike.

## 98. Put Diagonal

*Bearish drift to strike · Long vega · net debit*

**The idea (intuition).** The bearish cousin: buy a higher, longer-dated 24300 put and sell a nearer 24000 put. You own downside protection that gains as Nifty slips, subsidised by the front put you sell against it. A calendar that wants the index to drift *down* to the short strike.

**When & why to use it.** Deploy when you are mildly bearish — a slow leak toward 24000, not a crash — and want front-week theta working for you. Fits a market rolling over from a top with IV still cheap enough that the long put is not overpriced. Avoid if you expect a sharp gap down (buy puts or a put spread instead) or a snap-back rally.

**How to build it (₹, Nifty).** Sell 24000 PE @ 318, buy 24300 PE @ 528. Net debit 209.8 points, roughly ₹15,735 per lot.

![Figure: Put Diagonal payoff at expiry](figs/strategies/put_diagonal.png)

**The numbers (modelled at Nifty 24000).** Max profit 238 points (~₹17,850/lot); max loss 210 points (~₹15,750/lot, the debit); breakevens 23067 and 24545; net debit 209.8 points; risk:reward 1.13 — the most favourable ratio among the basic diagonals here. The lower breakeven 23067 shows how far the bearish tilt lets you ride a decline.

**Greeks & behaviour.** Net delta negative (bearish), theta positive while price stays above the short strike, vega positive. A controlled drift lower with steady-to-rising IV is the dream scenario.

**Management & exit.** Book partial profits as Nifty eases toward 24000 near front expiry; roll the short put down-and-out to extend a continuing decline. Exit near the upper breakeven if the index rallies instead.

**Risk note.** A fast rally leaves your long 24300 put withering while the short put decays — but unlike a naked short, your loss is capped at the 210-point debit. The cap is the comfort; the timing requirement is the catch.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹1,800 | +₹3,975 | +₹18,225 | -₹1,350 | -₹10,950 |

The bearish tilt is visible — P&L peaks at 24,000 (+₹18,225), holds a gain down at 23,400, and bleeds hardest on the 25,200 upside (-₹10,950) — with the long back-month put still alive and marked at the modelled IV.

**Adjustments, variants & timing.** Manage the bearish tilt actively: roll the short 24,000 put down-and-out as Nifty eases lower to keep the credit flowing and extend the decline, or recentre if the move stalls. On a snap-back rally, exit near the 24,545 upper breakeven before the long 24,300 put withers. Nifty is the natural vehicle for the tighter strikes and cleaner skew; Bank Nifty works for a harder bearish view if you size down for its swings. A weekly short against a monthly long maximises theta; lengthen both legs for a calmer, more vega-led version. Enter with IV rank low so the long put is cheap, ideally with a back-month event that can firm vol. This is the most favourable basic diagonal here (risk:reward 1.13), but it still needs a measured drift, not a crash — a gap straight through the short strike caps you. Bank gains into IV spikes.

## 99. Double Calendar

*Range-bound, rising IV · Long vega · net debit*

**The idea (intuition).** Run two calendars at once — one on the call side above spot, one on the put side below — to stretch the profit tent across a wider zone. Sell front options at 24300 (call) and 23700 (put), buy the same strikes in the back month. You profit anywhere price lands inside the band into front expiry, not just at a single strike.

**When & why to use it.** Ideal for a range-bound Nifty you expect to chop between roughly 23700 and 24300, with IV low and a catalyst further out to lift the back month. A textbook pre-event setup: sell the rich front week, own the cheaper back month, and let an IV rise into the event pad both long legs. Avoid in a trending tape or when front and back IV are already equal.

**How to build it (₹, Nifty).** Sell 24300 CE @ 292 / buy 24300 CE @ 506, and sell 23700 PE @ 219 / buy 23700 PE @ 323. Net debit 318.5 points, about ₹23,888 per lot.

![Figure: Double Calendar payoff at expiry](figs/strategies/double_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 260 points (~₹19,500/lot) with price inside the band at front expiry; max loss 455 points (~₹34,125/lot); breakevens 23452 and 24839; net debit 318.5 points; risk:reward 0.57. Two peaks (one over each strike) merge into a broad plateau around spot.

**Greeks & behaviour.** Delta near flat across the centre of the range, theta positive, vega strongly positive — with two long back-month legs, this is one of the more vega-heavy structures in the chapter, so an IV rise is a powerful tailwind.

**Management & exit.** Target ~25% of the debit, or close into front expiry. If price drifts to one side, roll that side's short option or close the untested wing to lock value. The double vega exposure means a back-month IV pop is often your cue to take profit early.

**Risk note.** A breakout past either breakeven plus a back-month IV crush hits both legs at once — the wide profit zone costs you a larger maximum loss (455 points) than a single calendar. Size accordingly.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹23,100 | -₹2,625 | +₹14,400 | +₹7,050 | -₹6,825 |

The twin-strike build spreads the gain into a plateau that peaks near 24,000 (+₹14,400) and stays positive out to 24,600, falling away only past the breakevens — a time spread, so both back-month longs are marked at the modelled IV, not zero.

**Adjustments, variants & timing.** The two-sided build is a pre-event workhorse: enter 7–10 days before a known catalyst (Budget, RBI, a heavy results week) when front weekly IV is rich and IV rank is low, so an IV rise into the event inflates both back-month longs. Manage by rolling the tested side's short option if price drifts to one wing, or close the untested wing to lock value; recentre both strikes if the range itself shifts. The double vega means a back-month IV pop is your cue to bank profit early rather than chase the peak. Run it on Nifty for the cleaner term structure and tighter strikes; Bank Nifty needs smaller size for its swings. Weekly shorts against monthly longs give the punchiest theta-plus-vega; lengthen for a calmer build. Target ~25% of the debit and exit before expiry-week gamma turns the dual shorts against you on any breakout.

## 100. Double Diagonal

*Range-bound, rising IV · Long vega · net debit*

**The idea (intuition).** A double calendar with the long legs pushed further out-of-the-money — buy the 24500 call and 23500 put wings against short 24300 call and 23700 put fronts. The result looks like an iron-condor's range-bound profile but, crucially, it is *long* vega because the longs are dated later than the shorts.

**When & why to use it.** Use when you want condor-style range income *and* a positive vega kicker — for instance ahead of an event where you expect price to stay boxed but IV to climb. The OTM long wings make it cheaper to put on than a same-strike double calendar. Skip it when you genuinely expect IV to fall (a short-vega iron condor fits that better) or when a trend is in force.

**How to build it (₹, Nifty).** Sell 24300 CE @ 292 / buy 24500 CE @ 399, and sell 23700 PE @ 219 / buy 23500 PE @ 273. Net debit 161.8 points, about ₹12,135 per lot — the cheapest of the multi-leg tents here.

![Figure: Double Diagonal payoff at expiry](figs/strategies/double_diagonal.png)

**The numbers (modelled at Nifty 24000).** Max profit 269 points (~₹20,175/lot); max loss 497 points (~₹37,275/lot); breakevens 23418 and 24806; net debit 161.8 points; risk:reward 0.54. Note the low entry cash (161.8) versus the larger modelled worst case (497) — the OTM wings cheapen entry but cap protection further out.

**Greeks & behaviour.** Delta roughly flat inside the range, theta positive, vega positive. Compared with the same-strike double calendar it gives up a little peak height for a lower cost and a slightly wider profit band.

**Management & exit.** Manage like an iron condor with a vega tilt: take ~25–30% of max, defend the tested side by rolling its short, and don't carry into expiry-week gamma. A rise in IV is a reason to bank profit rather than press.

**Risk note.** Because the long wings sit beyond the shorts, a violent move *outside* the wings, paired with an IV drop, produces the full 497-point loss. The cheap entry can lull you into oversizing — don't.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹22,875 | -₹900 | +₹15,825 | +₹6,825 | -₹8,700 |

P&L peaks at 24,000 (+₹15,825) across a broad band and turns negative only at the 22,800 and 25,200 extremes — the OTM long wings keep the back-month legs alive at the modelled IV.

**Adjustments, variants & timing.** Treat it as an iron condor with a long-vega kicker. Manage by rolling the tested short (call or put) as price pushes toward a wing, and consider closing the untested side once it has decayed to lock value; recentre the whole structure if the range migrates. The OTM longs make entry cheap, which tempts oversizing — don't. Enter ahead of an event when you expect price boxed but IV climbing: IV rank low, front weekly IV rich versus the back month, a catalyst seated later. A back-month IV pop is the signal to bank ~25–30% of max rather than press for the peak. Nifty suits the tighter wings and cleaner term structure; Bank Nifty works only with reduced size given its range. Weekly-against-monthly gives the fastest decay; lengthen both legs to soften gamma. Always close before expiry-week so the twin shorts don't gap outside the wings against you.

## 101. Poor Man's Covered Call (Diagonal)

*Bullish income · Long vega · net debit*

**The idea (intuition).** Replace the 24000-odd points of cash a real covered call would tie up with a single deep-in-the-money long-dated (LEAPS-style) 22500 call that behaves almost like owning the index, then sell a front 24300 call against it for income. It is a covered call on a fraction of the capital — hence "poor man's."

**When & why to use it.** A core income trade for a steadily-bullish-to-neutral view when you want covered-call-style cash flow without locking up lakhs in the underlying. The deep LEAPS call (high delta, near 1.0) tracks Nifty; the short front call rents out time each cycle. Best entered when IV rank is low so the long leg is cheap; less attractive when you expect a sharp decline (the long call still loses, just less than stock).

**How to build it (₹, Nifty).** Buy 22500 CE @ 3514 (deep ITM, long-dated), sell 24300 CE @ 292. Net debit 3222.5 points, about ₹2,41,688 per lot — large, but a fraction of the ~₹18 lakh a 75-lot of index would cost outright.

![Figure: Poor Man's Covered Call (Diagonal) payoff at expiry](figs/strategies/pmcc.png)

**The numbers (modelled at Nifty 24000).** Max profit 394 points (~₹29,550/lot) if price sits at the short strike; max loss 3223 points (~₹2,41,725/lot); single breakeven 23809; net debit 3222.5 points; risk:reward 0.12. The tiny ratio reflects that the modelled max loss assumes the long LEAPS call expires worthless — only if Nifty collapses far below 22500. In practice you manage long before that and roll the short call for repeated income, so the realistic risk is a fraction of the headline number.

**Greeks & behaviour.** Net delta strongly positive (the deep long call dominates), theta positive (you collect front decay each cycle), vega positive. Direction is the main P&L driver; the short call caps your upside above 24300.

**Management & exit.** Roll the short 24300 call out (and up if price runs) every cycle to keep harvesting premium — that recurring credit is the strategy's income engine. Close or roll the long call well before its expiry; reassess if Nifty breaks below the long strike's profitability.

**Risk note.** The honest danger is a large, sustained decline: the long call can lose most of its 3514-point value. The headline max loss assumes a near-total index collapse — improbable but not zero — so size the position small and treat the LEAPS as risk capital, not a free stock substitute.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹56,775 | -₹23,775 | +₹11,400 | +₹25,950 | +₹19,575 |

The deeply directional profile rises with the index — from -₹56,775 at 22,800 up to a +₹25,950 peak near the 24,300 short strike at 24,600 — and because the deep LEAPS-style long call is still alive, the downside cells assume it is marked at the modelled IV, far gentler than outright expiry.

**Adjustments, variants & timing.** The PMCC is an income engine, so the recurring action is rolling the short 24,300 call out (and up if Nifty runs) every cycle to bank a fresh credit against the same deep LEAPS-style long — that repeated premium is the strategy's yield. Recentre by rolling the long strike only when the index moves far enough to change its delta materially. Manage or roll the long well before its own expiry; reassess hard if Nifty threatens the long strike's profitability. Run it on Nifty — the deeper long-dated chain and tighter spreads make the deep-ITM leg far cheaper to trade than Bank Nifty's thinner far-month strikes. Enter when IV rank is low so the LEAPS call is cheap to buy. On a sustained decline the long call still loses (less than stock), so size small and treat the debit as risk capital. An IV rise helps the net-long-vega position — a reason to hold the long through quiet stretches.

## 102. Poor Man's Covered Put

*Bearish income · Long vega · net debit*

**The idea (intuition).** The bearish mirror of the PMCC: own a deep-ITM long-dated 25500 put (which acts like a short index position) and sell a front 23700 put against it for income. Covered-put economics without shorting the index or posting its full margin.

**When & why to use it.** For a sustained bearish-to-neutral view when you want to collect premium on the way down. The deep put gives you negative delta exposure; the short front put funds part of the carry. Enter with IV rank low so the long put is cheap. Not the tool for a sharp V-bottom reversal, which would whipsaw the long put.

**How to build it (₹, Nifty).** Buy 25500 PE @ 898, sell 23700 PE @ 219. Net debit 679.4 points, about ₹50,925 per lot.

![Figure: Poor Man's Covered Put payoff at expiry](figs/strategies/pmcp.png)

**The numbers (modelled at Nifty 24000).** Max profit 390 points (~₹29,250/lot); max loss 679 points (~₹50,925/lot, the debit); breakevens 22733 and 24584; net debit 679.4 points; risk:reward 0.57. The deep long put keeps the worst case to the debit paid — far tamer than the PMCC's headline because this long leg sits deep ITM with real intrinsic value.

**Greeks & behaviour.** Net delta negative (bearish), theta positive from the short front put, vega positive. A measured decline with firm IV is ideal; the short put caps gains below 23700.

**Management & exit.** Roll the short 23700 put down-and-out each cycle to keep income flowing as price falls. Close the long put before its expiry. Reassess on any decisive rally back above 24584.

**Risk note.** A strong rally erodes the long put toward worthless and you bleed the debit. Assignment risk on the short put if it goes ITM means you should roll rather than hold into expiry. Premium selling here is *not* free money — manage the tested side.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹1,650 | +₹19,050 | +₹18,375 | -₹450 | -₹15,150 |

The bearish engine pays on the way down — +₹19,050 at 23,400 — and loses up at 25,200 (-₹15,150), with the deep long put still alive and marked at the modelled IV.

**Adjustments, variants & timing.** Mirror the PMCC mechanics on the bearish side: roll the short 23,700 put down-and-out each cycle as Nifty falls to keep the credit flowing, and roll the deep long put's strike only when the move is large enough to reset its delta. Close the long put before its own expiry; reassess on any decisive rally back above 24,584. Because the long sits deep ITM with real intrinsic value, the worst case is contained to the debit — tamer than the PMCC headline. Run it on Nifty for the deeper, tighter long-dated chain; Bank Nifty's far-month puts are thinner and costlier to roll. Enter with IV rank low so the long put is cheap, and remember the position is net long vega, so a vol rise helps even as you wait for the slide. Manage the short put before expiry to avoid assignment — premium selling here is not free money.

## 103. Reverse Call Calendar

*Big move / falling IV · Short vega · net credit*

**The idea (intuition).** Flip the call calendar around: *buy* the cheap front-week 24000 call and *sell* the richer back-month 24000 call, taking in a credit. You now want exactly what a normal calendar fears — a big move away from the strike, or a collapse in the volatility term structure.

**When & why to use it.** A specialist trade for when back-month IV is unusually rich versus the front (an inverted or steep term structure) and you expect it to normalise, or when you anticipate a large directional break. Useful after an IV spike has lifted the back month disproportionately. Wrong when price is likely to pin the strike — that is the loss zone for this structure.

**How to build it (₹, Nifty).** Buy 24000 CE @ 456, sell 24000 CE @ 689. Net credit 232.7 points, about ₹17,453 per lot received — but note the short back-month leg requires margin, unlike a long calendar.

![Figure: Reverse Call Calendar payoff at expiry](figs/strategies/reverse_calendar_call.png)

**The numbers (modelled at Nifty 24000).** Max profit 233 points (~₹17,475/lot) achieved on a large move away from 24000; max loss 219 points (~₹16,425/lot) if price pins the strike; breakevens 23521 and 24757; net credit 232.7 points; risk:reward 1.06. The payoff is an inverted tent — a valley at the strike, profit on the wings.

**Greeks & behaviour.** Delta near flat at the strike, theta *negative* (time hurts — the front long decays faster than the short back), and vega *negative* — a falling IV term structure is your friend. This is the short-vega outlier of the family.

**Management & exit.** Take profit if the index breaks hard or back-month IV deflates toward the front. Because theta works against you, this is a shorter-horizon, thesis-driven trade — exit promptly if price stalls at the strike.

**Risk note.** The short back-month call carries open-ended-style risk if not covered by the front, but here the front long caps it — loss is bounded to ~219 points if price pins 24000. Margin and the negative theta mean you cannot sit in this trade indefinitely waiting to be right.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹12,975 | +₹3,075 | -₹16,725 | -₹2,325 | +₹4,200 |

The numbers are an inverted tent — the worst cell sits at 24,000 (-₹16,725) while the wings (22,800 and 25,200) turn positive — exactly the anti-pin payoff, and as a short-vega time spread the figures assume the modelled back-month IV.

**Adjustments, variants & timing.** This is a short-vega, time-boxed trade, so timing dominates: enter only when the back-month IV is unusually rich versus the front (a steep or inverted term structure) and you expect it to normalise, or when a large directional break looks imminent — often just after an IV spike has lifted the back month disproportionately. Manage by taking profit the moment the index breaks hard or the back-month IV deflates toward the front; do not sit waiting, because negative theta bleeds you daily. Recentre is rarely worth it — if price pins the strike, simply exit. Run it on Nifty where the term structure is cleanest and the short back-month leg's margin is manageable; Bank Nifty's wider swings actually help the anti-pin payoff but demand smaller size. The short back-month call needs margin, so account for that. Reverse calendars belong to high-IV regimes — the opposite window from every long calendar in this chapter.

## 104. Reverse Put Calendar

*Big move / falling IV · Short vega · net credit*

**The idea (intuition).** The put-side reverse calendar: buy the front 24000 put, sell the back-month 24000 put for a credit. Same short-vega, anti-pin profile as the reverse call calendar, expressed in puts.

**When & why to use it.** Choose the put build when the put term structure is the one that looks dislocated — back-month puts richly bid from hedging demand that you expect to fade — or when you want the reverse-calendar payoff with put-side margin treatment. Same caution: it loses if price pins 24000 into front expiry.

**How to build it (₹, Nifty).** Buy 24000 PE @ 318, sell 24000 PE @ 414. Net credit 95.8 points, about ₹7,185 per lot.

![Figure: Reverse Put Calendar payoff at expiry](figs/strategies/reverse_calendar_put.png)

**The numbers (modelled at Nifty 24000).** Max profit 233 points (~₹17,475/lot) on a large move; max loss 219 points (~₹16,425/lot) at the strike; breakevens 23523 and 24752; net credit 95.8 points; risk:reward 1.07. Inverted tent, valley at 24000.

**Greeks & behaviour.** Delta near flat, theta negative, vega negative. A move out of the range or a back-month IV slide pays; a quiet pin and rising IV both hurt.

**Management & exit.** Exit on a decisive break or once the back-month put IV normalises. Don't overstay — negative theta erodes the position daily if the index goes nowhere.

**Risk note.** Loss is capped at ~219 points by the long front put, but the short back-month put needs margin and risks assignment if it ends ITM. Treat it as a tactical, time-boxed term-structure trade, not a hold-to-expiry position.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹13,050 | +₹3,150 | -₹16,650 | -₹2,250 | +₹4,200 |

An inverted tent again — valley at 24,000 (-₹16,650), profit on a large move to either wing — with the short back-month put marked at the modelled IV.

**Adjustments, variants & timing.** Choose the put-side reverse when the back-month put IV looks dislocated — richly bid from hedging demand you expect to fade — or when you want the anti-pin payoff with put-side margin treatment. Like its call cousin it is short vega and carries negative theta, so it is strictly tactical: enter on a stretched term structure or ahead of an expected large move, and exit promptly once the index breaks or the back-month put IV normalises toward the front. Don't overstay a quiet pin — that is the loss zone and time works against you. Run it on Nifty for the cleanest term structure and manageable short-leg margin; Bank Nifty's bigger swings aid the wing payoff but need reduced size. The short back-month put requires margin and risks assignment if it ends ITM, so roll rather than carry into expiry. This is a high-IV, time-boxed term-structure bet, not a hold-to-expiry position.

## 105. OTM Call Calendar (Bullish)

*Drift up to strike · Long vega · net debit*

**The idea (intuition).** Place the calendar *above* spot at 24400: sell the front 24400 call, buy the back-month 24400 call. The profit tent peaks at 24400, so the trade quietly bets that Nifty drifts up to that strike by the near expiry — a directional flavour built into a neutral structure.

**When & why to use it.** Use when you are mildly bullish and want a cheaper, defined-risk way to express "I think we grind up to 24400." Front IV should be rich and overall IV rank low. Skip it if you expect an explosive rally (the short call caps you) or no move at all (price stays under the tent and the trade underperforms).

**How to build it (₹, Nifty).** Sell 24400 CE @ 246, buy 24400 CE @ 451. Net debit 205.1 points, about ₹15,383 per lot.

![Figure: OTM Call Calendar (Bullish) payoff at expiry](figs/strategies/otm_call_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 229 points (~₹17,175/lot) if Nifty sits at 24400 on front expiry; max loss 205 points (~₹15,375/lot); breakevens 23890 and 25271; net debit 205.1 points; risk:reward 1.12. The peak sits up at the OTM strike, rewarding the bullish drift.

**Greeks & behaviour.** Net delta mildly positive (the tent is above spot), theta positive once price approaches the strike, vega positive. Best case is a slow climb to 24400 with steady-to-rising IV.

**Management & exit.** Close as price reaches 24400 near front expiry where the tent peaks. Roll the short call out for another cycle if the up-drift thesis holds. Cut near the breakevens.

**Risk note.** If Nifty stalls well below 24400 or rallies straight through it, the structure underdelivers and you can lose most of the 205-point debit. The bet needs the *right amount* of up-move — neither too little nor too much.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹14,025 | -₹9,375 | +₹3,075 | +₹11,625 | +₹750 |

The peak has shifted up to the 24,400 strike: P&L tops out at 24,600 (+₹11,625) and is still mildly positive at 25,200, rewarding the up-drift, while a flat-to-down tape (22,800: -₹14,025) is the loss zone — the back-month call stays alive at the modelled IV.

**Adjustments, variants & timing.** Manage the bullish drift like a directional calendar: roll the short 24,400 call out for another credit if the up-drift thesis holds, and recentre the strike higher if Nifty climbs past 24,400 so the tent tracks price. Cut near the 23,890 or 25,271 breakevens when the move proves too small or too large — this trade needs the right amount of up-move. Run it on Nifty for tighter OTM strikes and cleaner weekly-monthly structure; Bank Nifty suits a stronger directional view with smaller size. A weekly short against a monthly long gives the fastest theta; lengthen for a calmer build. Enter with IV rank low and front IV rich so the back-month long is cheap, ideally with a catalyst seated later to add vega lift. Bank profit into any IV spike or as price reaches 24,400 near front expiry, rather than holding through the short leg's expiry-week gamma.

## 106. OTM Put Calendar (Bearish)

*Drift down to strike · Long vega · net debit*

**The idea (intuition).** Drop the calendar *below* spot at 23600: sell the front 23600 put, buy the back-month 23600 put. The tent peaks at 23600, so it pays off on a measured slide down to that level — a bearish lean inside a calendar shell.

**When & why to use it.** For a mildly bearish view when you expect Nifty to ease toward 23600 by the near expiry, with front IV rich and IV rank low. Avoid if you expect a crash through 23600 (the short put caps you) or a flat-to-up tape that never reaches the tent.

**How to build it (₹, Nifty).** Sell 23600 PE @ 192, buy 23600 PE @ 297. Net debit 105.1 points, about ₹7,883 per lot.

![Figure: OTM Put Calendar (Bearish) payoff at expiry](figs/strategies/otm_put_calendar.png)

**The numbers (modelled at Nifty 24000).** Max profit 232 points (~₹17,400/lot) if price reaches 23600 on front expiry; max loss 240 points (~₹18,000/lot); breakevens 23098 and 24372; net debit 105.1 points; risk:reward 0.96. As with several put calendars, the modelled max loss (240) exceeds the entry cash (105.1) because it spans the back leg's full life.

**Greeks & behaviour.** Net delta mildly negative, theta positive as price nears the strike, vega positive. A controlled drift lower with firm IV is the sweet spot.

**Management & exit.** Take profit as Nifty approaches 23600 near front expiry. Roll the short put down for another cycle if the decline continues. Exit if price climbs back through the upper breakeven.

**Risk note.** A flat or rising index leaves the tent unreached and the debit bleeds; a crash straight through 23600 caps your gain at the short strike. You need the move to be both bearish *and* measured.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹6,900 | +₹9,600 | +₹6,525 | -₹2,625 | -₹6,375 |

The peak sits below spot at the 23,600 strike — best cell is 23,400 (+₹9,600) — rewarding a measured slide, while a rally to 25,200 loses (-₹6,375); the back-month put is marked at the modelled IV.

**Adjustments, variants & timing.** Manage the bearish drift symmetrically: roll the short 23,600 put down for another cycle if the slide continues, and recentre the strike lower if Nifty falls past 23,600 so the tent follows. Exit if price climbs back through the 24,372 upper breakeven, and remember you need the move both bearish and measured — a crash straight through 23,600 caps your gain at the short strike. Run it on Nifty for the tighter OTM strikes and cleaner term structure; Bank Nifty fits a stronger bearish view if you size down. Weekly short against monthly long gives the steepest theta; lengthen both legs for a gentler, more vega-led version. Enter when IV rank is low and front-week put IV is rich relative to the back, ideally with a later catalyst that can firm back-month vol. Bank profit into an IV spike or as Nifty nears 23,600 close to front expiry, before weekly gamma flips the trade.

## 107. Weekly-vs-Monthly Calendar

*Pin near strike · Long vega · net debit*

**The idea (intuition).** The purest expression of the time-spread engine on NSE: sell the cheap-but-fast-decaying *weekly* 24000 call and buy the slower *monthly* 24000 call. The weekly's theta runs hot while the monthly barely moves, so a pinned index hands you the difference.

**When & why to use it.** This is the bread-and-butter Nifty/Bank Nifty calendar — sell the rich weekly, own the steadier monthly, and let the steep weekly decay work. Best when the index is range-bound around 24000 and weekly IV is elevated versus the month (common into and around weekly expiry). Avoid when a trend or event threatens to move price off the strike within the week.

**How to build it (₹, Nifty).** Sell 24000 CE @ 202 (weekly), buy 24000 CE @ 499 (monthly). Net debit 296.8 points, about ₹22,260 per lot.

![Figure: Weekly-vs-Monthly Calendar payoff at expiry](figs/strategies/calendar_weekly_monthly.png)

**The numbers (modelled at Nifty 24000).** Max profit 137 points (~₹10,275/lot) at the strike on weekly expiry; max loss 297 points (~₹22,275/lot); breakevens 23719 and 24396; net debit 296.8 points; risk:reward 0.46. The breakevens (23719–24396) are tighter than a monthly-vs-further calendar — a narrower tent reflecting the short weekly window.

**Greeks & behaviour.** Delta near flat at the strike, theta strongly positive (the weekly leg decays fast — the whole point), vega positive. Fast front theta is the dominant driver over this short horizon.

**Management & exit.** Close at weekly expiry, or roll the short weekly into the next week to keep harvesting decay against the same monthly long — a repeatable income cadence. Exit before expiry-day gamma whips the short leg.

**Risk note.** The tight breakevens mean even a modest move off 24000 within the week erodes the trade; the short weekly's gamma spikes near expiry, so a late move can flip a winner to a loser quickly. Manage actively into the final session.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹18,300 | -₹9,000 | +₹10,575 | -₹3,750 | -₹9,975 |

The weekly tent is tight and lower — it peaks at 24,000 (+₹10,575) but turns negative by 24,600, reflecting the narrow one-week window — with the monthly long still alive at the modelled IV.

**Adjustments, variants & timing.** This is the bread-and-butter NSE calendar and its defining action is the weekly roll: at each weekly expiry, buy back the dying short 24,000 call and sell the next week's 24,000 call against the same monthly long, harvesting decay cycle after cycle. Recentre to the new ATM strike if Nifty has drifted, rather than defending a skewed tent. The tight breakevens (23,719–24,396) mean you must manage actively — roll or recentre the moment price threatens a side. Both Nifty and Bank Nifty run this well; Bank Nifty's hotter weekly IV gives more decay but needs smaller size for its swings. Enter when weekly IV is elevated versus the month — common into weekly expiry — and IV rank is low so the monthly long is cheap. Always close or roll before expiry-day, when the short weekly's gamma spikes and a late move can flip a winner to a loser in a single session.

## 108. Aggressive Bullish Diagonal

*Bullish trend · Long vega · net debit*

**The idea (intuition).** A PMCC dialled up for trend-following: buy a mid-dated in-the-money 23200 call (high delta, strong index tracking) and sell a further-out 24200 front call against it. More directional punch than the standard poor-man's-covered-call, with income from the short leg.

**When & why to use it.** For a confident bullish trend where you want stock-like upside participation on a fraction of the capital, plus a recurring short-call credit. The deep ITM long gives high delta; the OTM short gives room to run before it caps you. Enter with IV rank low so the long is cheap. Not for choppy or bearish markets — the large long-call debit is at stake.

**How to build it (₹, Nifty).** Buy 23200 CE @ 1669, sell 24200 CE @ 342. Net debit 1327.1 points, about ₹99,533 per lot.

![Figure: Aggressive Bullish Diagonal payoff at expiry](figs/strategies/pmcc_aggressive.png)

**The numbers (modelled at Nifty 24000).** Max profit 309 points (~₹23,175/lot) near the short strike; max loss 1327 points (~₹99,525/lot); single breakeven 23789; net debit 1327.1 points; risk:reward 0.23. The low ratio reflects the modelled worst case where the long 23200 call expires worthless — only on a deep decline; in practice you roll the short and manage the long well before that.

**Greeks & behaviour.** Net delta strongly positive (trend engine), theta positive from the short call, vega positive. Direction dominates the P&L; the short 24200 call caps gains above it.

**Management & exit.** Roll the short call up-and-out as the trend extends to keep collecting credit and lifting the cap. Manage or roll the long before its expiry. Cut if the trend fails and price breaks below 23789.

**Risk note.** A sustained decline can erode most of the 1669-point long-call value. The headline max loss assumes the index falls far below 23200 — unlikely but real — so size small and treat the long call as risk capital. This is a directional bet first, an income trade second.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹46,050 | -₹19,875 | +₹11,625 | +₹17,700 | +₹12,075 |

Strongly directional — from -₹46,050 at 22,800 the P&L climbs to a +₹17,700 peak near the 24,200 short strike at 24,600 — and the deep ITM long call is still alive, so the loss cells assume it is marked at the modelled IV rather than expired.

**Adjustments, variants & timing.** This is a directional bet first, income trade second, so manage it like a trend position: roll the short 24,200 call up-and-out as the rally extends to keep collecting credit and lift the cap, and roll the deep ITM long's strike only when a large move resets its delta. Manage or roll the long before its own expiry; cut decisively if the trend fails and price breaks below 23,789. Run it on Nifty for the deeper mid-dated chain and tighter strikes; Bank Nifty delivers more punch but needs smaller size for its swings. Enter with IV rank low so the high-delta long call is cheap, and note the position is net long vega, so a vol rise adds to a winning trend. A sustained decline erodes most of the long-call value, so size small and treat the debit as risk capital. Bank partial profit near the short strike rather than chasing the headline peak.

## 109. Bearish Diagonal (PMCP-style)

*Bearish trend · Long vega · net debit*

**The idea (intuition).** The bearish trend-follower: buy a mid-dated in-the-money 24800 put (strong negative delta) and sell a further-out 23800 front put against it. Stock-like downside exposure on a fraction of the capital, with income from the short put.

**When & why to use it.** For a committed bearish trend where you want sustained downside participation plus a recurring credit, without shorting the index outright. The ITM long put tracks declines; the OTM short put funds part of the carry. Enter with IV rank low. Avoid in rangebound or rising markets — the long-put debit is the exposure.

**How to build it (₹, Nifty).** Buy 24800 PE @ 796, sell 23800 PE @ 248. Net debit 547.1 points, about ₹41,033 per lot.

![Figure: Bearish Diagonal (PMCP-style) payoff at expiry](figs/strategies/bearish_diagonal.png)

**The numbers (modelled at Nifty 24000).** Max profit 363 points (~₹27,225/lot) near the short strike; max loss 547 points (~₹41,025/lot, the debit); single breakeven 24460; net debit 547.1 points; risk:reward 0.66. The deep ITM long put keeps the worst case to the debit paid.

**Greeks & behaviour.** Net delta strongly negative (bearish engine), theta positive from the short put, vega positive. A sustained decline is the driver; the short 23800 put caps gains below it.

**Management & exit.** Roll the short put down-and-out as the decline extends to keep income flowing and lower the cap. Manage the long put before its expiry. Exit on a reversal back above 24460.

**Risk note.** A rally erodes the long put and you bleed toward the full 547-point debit. Assignment risk on the short put if it goes ITM — roll rather than carry into expiry. Defined risk, but it still demands you be right on direction and timing.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | +₹9,375 | +₹18,225 | +₹18,225 | -₹4,650 | -₹20,550 |

The bearish trend-follower pays as Nifty falls — +₹18,225 at both 23,400 and 24,000 — and loses hardest on a 25,200 rally (-₹20,550), with the deep ITM long put still marked at the modelled IV.

**Adjustments, variants & timing.** Manage the bearish trend actively: roll the short 23,800 put down-and-out as the decline extends to keep income flowing and lower the cap, and reset the deep ITM long put's strike only on a large enough move. Manage or roll the long before its own expiry; exit on a reversal back above 24,460. The deep ITM long keeps the worst case to the debit, but you still need direction and timing right (risk:reward 0.66). Run it on Nifty for the deeper mid-dated put chain and tighter strikes; Bank Nifty offers more downside punch but demands smaller size for its larger swings. Enter with IV rank low so the long put is cheap, and remember the structure is net long vega — a vol rise into a falling market is a double tailwind. Watch assignment risk on the short put if it goes ITM; roll rather than carry into expiry, and bank profit near the short strike.

## 110. Double Calendar (Wide)

*Broad range, rising IV · Long vega · net debit*

**The idea (intuition).** A double calendar with the strikes pushed wider — sell/buy at 24500 on the call side and 23500 on the put side — to spread the long-vol tent over a larger zone. You sacrifice peak height for a broader band of profitability.

**When & why to use it.** For a market you expect to stay range-bound but over a *wider* band (say 23500–24500), with IV low and scope to rise into a back-month catalyst. The wide strikes suit higher-volatility regimes where the narrow double calendar would get run over. Avoid in a tight pin (a narrower structure pays more) or a clear trend.

**How to build it (₹, Nifty).** Sell 24500 CE @ 204 / buy 24500 CE @ 399, and sell 23500 PE @ 169 / buy 23500 PE @ 273. Net debit 299.6 points, about ₹22,470 per lot.

![Figure: Double Calendar (Wide) payoff at expiry](figs/strategies/double_calendar_wide.png)

**The numbers (modelled at Nifty 24000).** Max profit 202 points (~₹15,150/lot); max loss 434 points (~₹32,550/lot); breakevens 23322 and 24989; net debit 299.6 points; risk:reward 0.46. The wide breakevens (23322–24989) cover a broad range, but the lower peak (202) is the price of that width.

**Greeks & behaviour.** Delta near flat across a wide centre, theta positive, vega strongly positive (two back-month longs). An IV rise is a major tailwind across the whole band.

**Management & exit.** Target ~25% of debit, or close into front expiry. Roll the tested side if price drifts to a wing. Bank profit on a back-month IV pop rather than chasing the peak.

**Risk note.** A breakout past 23322 or 24989, especially with an IV crush, delivers the 434-point loss. The wide tent tempts oversizing because each strike feels far away — keep position size disciplined.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹18,225 | +₹3,750 | +₹5,475 | +₹11,475 | -₹3,975 |

The wide build spreads a flatter gain — positive from 23,400 through 24,600, peaking at 24,600 (+₹11,475) — and loses only at the 22,800 and 25,200 extremes, the two back-month longs marked at the modelled IV.

**Adjustments, variants & timing.** Manage the wide build like a roomy iron condor with a long-vega tilt: roll the tested side's short toward a wing as price drifts, close the untested side to lock value, and recentre the whole structure if the range itself migrates. The wide strikes feel safe and tempt oversizing — keep size disciplined. Enter when you expect Nifty range-bound over a broad band (say 23,500–24,500) with IV rank low and a back-month catalyst to lift vol; the width suits higher-volatility regimes where a narrow double calendar would be run over. A back-month IV pop is the signal to bank ~25% of the debit rather than chase the flatter peak. Run it on Nifty for the cleaner term structure; Bank Nifty fits its naturally wider range but needs smaller size. Weekly shorts against monthly longs give the fastest decay; lengthen for calm. Always close before expiry-week gamma can gap the shorts outside the band.

## 111. Calendar Straddle

*Pin near ATM, rising IV · Long vega · net debit*

**The idea (intuition).** Stack a short front straddle under a long back-month straddle, all at 24000: sell the front 24000 call and put, buy the back-month 24000 call and put. It is a calendar built on *both* sides at the same strike — a powerful, vega-rich tent peaked at the money.

**When & why to use it.** The maximal long-vol calendar: for when you strongly expect Nifty to pin 24000 into the front expiry *and* IV to rise. Front straddle IV should be rich relative to the back. Excellent into a quiet stretch before a later catalyst. Avoid when a move is likely (the dual short legs make pin-failure expensive) or when IV is already high and set to fall.

**How to build it (₹, Nifty).** Sell 24000 CE @ 456 and 24000 PE @ 318, buy 24000 CE @ 689 and 24000 PE @ 414. Net debit 328.5 points, about ₹24,638 per lot.

![Figure: Calendar Straddle payoff at expiry](figs/strategies/calendar_straddle.png)

**The numbers (modelled at Nifty 24000).** Max profit 438 points (~₹32,850/lot) at the strike on front expiry — the highest peak in this chapter; max loss 466 points (~₹34,950/lot); breakevens 23522 and 24754; net debit 328.5 points; risk:reward 0.94. A tall, narrow tent centred on 24000.

**Greeks & behaviour.** Delta near flat at the strike, theta strongly positive (two front legs decaying), vega strongly positive (two back legs). This is among the most vega-sensitive structures here — an IV rise massively boosts the longs.

**Management & exit.** Take profit aggressively — the peak is high but the breakevens are tight. Close into front expiry, or roll both short legs for another cycle if 24000 still pins. Exit before expiry-week gamma on the dual shorts turns violent.

**Risk note.** A move off 24000, especially with an IV crush, hits all four legs and can take the full ~466-point loss fast. The two short front legs mean gamma risk near expiry is acute — manage actively and do not carry through.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹25,950 | -₹6,300 | +₹33,450 | +₹4,500 | -₹8,400 |

The dual-sided straddle delivers the chapter's tallest peak — +₹33,450 right at 24,000 — collapsing to losses once price leaves the strike, with both back-month long legs still alive at the modelled IV.

**Adjustments, variants & timing.** The maximal long-vol calendar demands aggressive profit-taking — the +₹33,450 peak is tall but the breakevens (23,522–24,754) are tight, so bank gains quickly rather than reaching for the apex. Roll both short legs into the next cycle if 24,000 still pins, or recentre the entire straddle to a new ATM strike if price has moved. Enter in a quiet stretch before a later catalyst, when front straddle IV is rich versus the back and IV rank is low so the dual back-month longs are cheap — an IV rise massively inflates this vega-heavy structure, making any spike a take-profit cue. Run it on Nifty for tighter strikes and cleaner term structure; Bank Nifty's swings make pin-failure expensive, so size down sharply. The two short front legs mean acute expiry-week gamma — close before then and never carry through, or a move off 24,000 plus an IV crush can take the full loss fast.

## 112. Calendar (45/75-DTE)

*Pin near strike · Long vega · net debit*

**The idea (intuition).** A longer-dated calendar — sell a ~45-day 24000 call, buy a ~75-day 24000 call. Both legs decay more slowly than a weekly calendar, so the trade is calmer: less theta per day, more vega, and far more room to manage.

**When & why to use it.** For a patient, range-bound view with a longer horizon and a vega tilt — you want exposure to an IV rise over weeks, not days, and you prefer to avoid the knife-edge gamma of weekly structures. Suits low IV rank with a medium-term catalyst. Less efficient if you specifically want fast weekly theta (the weekly-vs-monthly calendar does that better).

**How to build it (₹, Nifty).** Sell 24000 CE @ 579 (~45 DTE), buy 24000 CE @ 790 (~75 DTE). Net debit 211.1 points, about ₹15,833 per lot.

![Figure: Calendar (45/75-DTE) payoff at expiry](figs/strategies/calendar_45_75.png)

**The numbers (modelled at Nifty 24000).** Max profit 241 points (~₹18,075/lot) at the strike on the front (45-DTE) expiry; max loss 211 points (~₹15,825/lot, the debit); breakevens 23460 and 24894; net debit 211.1 points; risk:reward 1.14 — the best ratio in the chapter. The longer horizon gives wide breakevens (23460–24894).

**Greeks & behaviour.** Delta near flat at the strike, theta positive but *gentler* than short-dated calendars, vega strongly positive — with more days to expiry on both legs, IV sensitivity is high and gamma risk is low. Vega is the dominant lever here.

**Management & exit.** With a longer runway you can be patient: target a share of the debit as IV rises, roll the front leg as it approaches its expiry, and you have ample room to adjust if price drifts. Take profit on an IV pop rather than holding for the exact peak.

**Risk note.** The longer dating means more exposure to a *back-month IV decline* — if vol falls over the holding period, the vega-heavy long leg suffers even if price behaves. Wide breakevens cushion direction, but the trade lives and dies on the volatility path.

**Scenario P&L (₹ per lot, at the front-month expiry).**

| Nifty at expiry | 22,800 | 23,400 | 24,000 | 24,600 | 25,200 |
|---|---|---|---|---|---|
| **P&L (₹/lot)** | -₹11,325 | -₹1,500 | +₹18,375 | +₹3,900 | -₹2,550 |

The longer-dated build peaks at 24,000 (+₹18,375) with gentle, wide shoulders — still positive at 24,600 — reflecting the calmer 45/75-day horizon, and the 75-day long is very much alive at the modelled IV.

**Adjustments, variants & timing.** The longer 45/75-day horizon rewards patience: with gentler theta and lower gamma you have room to roll the ~45-day short as it nears expiry against the same 75-day long, or recentre both legs if price drifts — there is no knife-edge to manage. This is the most vega-led calendar here, so it lives and dies on the volatility path: enter when IV rank is low with a medium-term catalyst weeks out, and take profit on any IV pop rather than holding for the exact price peak. Conversely, watch for a back-month IV decline over the holding period — the vega-heavy long suffers even if price behaves. Run it on Nifty for the deeper longer-dated chain and cleaner term structure; Bank Nifty's far-month strikes are thinner. Use this build when you want weeks of exposure to a vol rise without weekly gamma; switch to the weekly-vs-monthly calendar when you specifically want fast front-week theta instead.

